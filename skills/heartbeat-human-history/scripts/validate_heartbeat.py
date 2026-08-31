#!/usr/bin/env python3
"""Validate heartbeat pulse against schema, corpus meta, invariants, hashes, chain.

Exit 0 = pulse agrees with files.
Exit 2 = diverged.
--write-attestation prints a JSON attestation object measured from disk.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

SCHEMA_OK = {"heartbeat.v1", "heartbeat.v1.1"}
STATUS_OK = {"ok", "degraded", "diverged", "blocked"}
TEO_T0, TEO_T1 = -100, 650
ORIGIN_KIND_FILES = {
    "species": "homininos.json",
    "sites": "yacimientos.json",
    "migrations": "migraciones.json",
    "admixture": "introgresion.json",
    "anclas": "anclas_regionales.json",
}
# kind SPEC_05 that must never share an id with a political cone
NO_CONE_KINDS = ("species", "sites", "migrations", "admixture")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / "heartbeat_human_history" / "HEARTBEAT.json").exists():
            return p
        nested = p / "Modelo_Matematico_de_la_Humanidad"
        if (nested / "heartbeat_human_history" / "HEARTBEAT.json").exists():
            return nested
    return start


def resolve_datos(root: Path) -> Path:
    d = root / "datos"
    if d.exists():
        return d
    alt = Path("/home/workdir/artifacts")
    if (alt / "cronologia_mundial_arbol.json").exists():
        return alt
    return d


def _load(path: Path):
    return json.loads(path.read_text())


def item_ids(doc: dict) -> set[str]:
    out = set()
    for it in doc.get("items") or []:
        if isinstance(it, dict):
            for k in ("id", "slug", "key"):
                if it.get(k):
                    out.add(str(it[k]))
                    break
    return out


def measure(root: Path) -> dict:
    datos = resolve_datos(root)
    measured: dict = {"available": True, "files": {}, "counts": {}, "invariants": {}}
    tree_p = datos / "cronologia_mundial_arbol.json"
    if not tree_p.exists():
        tree_p = Path("/home/workdir/artifacts/cronologia_mundial_arbol.json")
    onto_p = datos / "historia_ontologia.json"
    if not onto_p.exists():
        onto_p = Path("/home/workdir/artifacts/historia_ontologia.json")
    fib_p = datos / "civilizaciones_fibras.json"
    if not fib_p.exists():
        fib_p = Path("/home/workdir/artifacts/civilizaciones_fibras.json")
    sim_p = datos / "sim_meta.json"
    if not sim_p.exists():
        sim_p = Path("/home/workdir/artifacts/sim_meta.json")
    ori_dir = datos / "origenes"
    if not ori_dir.exists():
        ori_dir = Path("/home/workdir/artifacts/Modelo_Matematico_de_la_Humanidad/datos/origenes")

    hashes = {}
    counts = {}

    if tree_p.exists():
        tree = _load(tree_p)
        counts["cronologia_n_nodes"] = int(tree.get("n_nodes") or (tree.get("meta") or {}).get("n_nodes"))
        hashes["datos/cronologia_mundial_arbol.json"] = sha256_file(tree_p)
    if onto_p.exists():
        onto = _load(onto_p)
        counts["ontologia_n_nodos"] = int((onto.get("meta") or {}).get("n_nodos") or len(onto.get("nodos") or []))
        hashes["datos/historia_ontologia.json"] = sha256_file(onto_p)
    if fib_p.exists():
        fib = _load(fib_p)
        n = (fib.get("meta") or {}).get("n_civilizaciones")
        if n is None:
            n = len(fib.get("civilizaciones") or {})
        counts["fibras"] = int(n)
        hashes["datos/civilizaciones_fibras.json"] = sha256_file(fib_p)
    if sim_p.exists():
        sim = _load(sim_p)
        cones = sim.get("conos") or []
        counts["sim_meta_n_conos"] = int(sim.get("n_cones") or len(cones))
        hashes["datos/sim_meta.json"] = sha256_file(sim_p)
        teo = next((c for c in cones if c.get("id") == "teotihuacan"), None)
        if teo:
            t0, t1 = int(teo["t0"]), int(teo["t1"])
            measured["invariants"]["teotihuacan_interval"] = [t0, t1]
            measured["invariants"]["teotihuacan_off_at_700"] = not (t0 <= 700 <= t1)
        cone_ids = {c.get("id") for c in cones if c.get("id")}
        measured["invariants"]["n_cone_ids"] = len(cone_ids)
    else:
        cone_ids = set()

    origenes = {}
    if ori_dir.exists():
        for key, fname in ORIGIN_KIND_FILES.items():
            p = ori_dir / fname
            if not p.exists():
                continue
            doc = _load(p)
            n = doc.get("n")
            if n is None:
                n = len(doc.get("items") or [])
            origenes[key] = int(n)
            hashes[f"datos/origenes/{fname}"] = sha256_file(p)
            ids = item_ids(doc)
            if key in NO_CONE_KINDS and cone_ids:
                overlap = sorted(cone_ids & ids)
                measured["invariants"][f"overlap_{key}_cones"] = overlap
    counts["origenes"] = origenes

    measured["counts"] = counts
    measured["hashes"] = hashes
    measured["files"] = {k: True for k in hashes}
    return measured


def compare_counts(pulse: dict, measured: dict, errors: list[str]) -> None:
    corpus = pulse.get("corpus") or {}
    counts = measured.get("counts") or {}
    declared = (corpus.get("cronologia_mundial_arbol") or {}).get("n_nodes")
    actual = counts.get("cronologia_n_nodes")
    if declared is not None and actual is not None and int(declared) != int(actual):
        errors.append(f"diverged cronologia n_nodes pulse={declared} file={actual}")
    declared = (corpus.get("historia_ontologia") or {}).get("n_nodos")
    actual = counts.get("ontologia_n_nodos")
    if declared is not None and actual is not None and int(declared) != int(actual):
        errors.append(f"diverged ontologia n_nodos pulse={declared} file={actual}")
    declared = (corpus.get("civilizaciones_fibras") or {}).get("n")
    actual = counts.get("fibras")
    if declared is not None and actual is not None and int(declared) != int(actual):
        errors.append(f"diverged fibras pulse={declared} file={actual}")
    declared = (corpus.get("sim_meta") or {}).get("n_conos")
    actual = counts.get("sim_meta_n_conos")
    if declared is not None and actual is not None and int(declared) != int(actual):
        errors.append(f"diverged sim_meta n_conos pulse={declared} file={actual}")
    ori_p = corpus.get("origenes") or {}
    ori_m = counts.get("origenes") or {}
    for key in ("species", "sites", "migrations", "admixture", "anclas"):
        if key in ori_p and key in ori_m and int(ori_p[key]) != int(ori_m[key]):
            errors.append(f"diverged origenes.{key} pulse={ori_p[key]} file={ori_m[key]}")


def compare_hashes(pulse: dict, measured: dict, errors: list[str]) -> None:
    claimed = ((pulse.get("attestation") or {}).get("hashes")) or {}
    actual = measured.get("hashes") or {}
    for path, digest in claimed.items():
        if path in actual and actual[path] != digest:
            errors.append(f"hash mismatch {path}")


def check_invariants(measured: dict, errors: list[str]) -> None:
    inv = measured.get("invariants") or {}
    interval = inv.get("teotihuacan_interval")
    if interval and list(interval) != [TEO_T0, TEO_T1]:
        errors.append(f"teotihuacan interval {interval} != [{TEO_T0}, {TEO_T1}]")
    if "teotihuacan_off_at_700" in inv and not inv["teotihuacan_off_at_700"]:
        errors.append("teotihuacan still on at t=700")
    for key in NO_CONE_KINDS:
        overlap = inv.get(f"overlap_{key}_cones") or []
        if overlap:
            errors.append(f"origin kind {key} shares cone ids: {overlap}")


def check_chain(hb_dir: Path, pulse: dict, errors: list[str]) -> None:
    chain = pulse.get("chain") or {}
    prev_id = chain.get("prev_session_id")
    prev_hash = chain.get("prev_sha256")
    if not prev_id or not prev_hash:
        return
    # locate previous session file
    candidates = list((hb_dir / "log").glob("*.md"))
    match = None
    for p in candidates:
        if p.name == "INDEX.md":
            continue
        text = p.read_text()
        if prev_id in text.splitlines()[0] or f"id:          {prev_id}" in text or f"`{prev_id}`" in text[:200]:
            match = p
            break
        if prev_id.replace("-", "_") in p.stem or prev_id in p.name:
            match = p
            break
    if match is None:
        # fallback: last_session of previous pulse is not stored; try slug after date
        slug = prev_id.split("-", 3)[-1] if prev_id.count("-") >= 3 else prev_id
        for p in candidates:
            if slug and slug in p.name:
                match = p
                break
    if match is None:
        errors.append(f"chain.prev_session_id not found on disk: {prev_id}")
        return
    digest = sha256_file(match)
    if digest != prev_hash:
        errors.append(
            f"chain.prev_sha256 mismatch file={match.name} disk={digest} pulse={prev_hash}"
        )


def validate_schema_json(schema_p: Path, pulse: dict, errors: list[str]) -> None:
    if not schema_p.exists():
        return
    try:
        import jsonschema  # optional
    except ImportError:
        return
    try:
        jsonschema.validate(pulse, json.loads(schema_p.read_text()))
    except Exception as e:
        errors.append(f"schema: {e}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="", help="project root that contains heartbeat_human_history/")
    ap.add_argument(
        "--write-attestation",
        action="store_true",
        help="print measured attestation JSON and exit 0",
    )
    args = ap.parse_args()
    root = Path(args.root).resolve() if args.root else find_root(Path.cwd())
    hb_dir = root / "heartbeat_human_history"
    pulse_p = hb_dir / "HEARTBEAT.json"
    schema_p = hb_dir / "heartbeat.schema.json"
    index_p = hb_dir / "log" / "INDEX.md"
    errors: list[str] = []

    measured = measure(root)
    if args.write_attestation:
        att = {
            "method": "validate_heartbeat.py",
            "measured": measured.get("counts"),
            "hashes": measured.get("hashes"),
            "invariants": measured.get("invariants"),
        }
        json.dump(att, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
        return 0

    if not pulse_p.exists():
        print("heartbeat missing:", pulse_p, file=sys.stderr)
        return 2
    pulse = json.loads(pulse_p.read_text())
    if pulse.get("schema") not in SCHEMA_OK:
        errors.append(f"schema != heartbeat.v1|v1.1 ({pulse.get('schema')})")
    for k in ("t", "status", "repo", "corpus", "last_session", "pending", "invariants_ok"):
        if k not in pulse:
            errors.append(f"missing field {k}")
    if pulse.get("status") not in STATUS_OK:
        errors.append(f"bad status {pulse.get('status')}")

    if pulse.get("schema") == "heartbeat.v1.1":
        if "attestation" not in pulse:
            errors.append("v1.1 missing attestation")
        if "chain" not in pulse:
            errors.append("v1.1 missing chain")

    last = pulse.get("last_session") or {}
    log_rel = last.get("log")
    log_p = None
    if log_rel:
        log_p = hb_dir / log_rel if not str(log_rel).startswith("log/") else hb_dir / log_rel
        if not log_p.exists():
            alt = hb_dir / "log" / Path(str(log_rel)).name
            if not alt.exists():
                errors.append(f"last_session.log missing: {log_rel}")
            else:
                log_p = alt
        if log_p and log_p.exists() and last.get("id") and last["id"] not in log_p.read_text():
            errors.append(f"last_session.id {last.get('id')} not found in {log_p.name}")
        if log_p and log_p.exists() and last.get("sha256"):
            digest = sha256_file(log_p)
            if digest != last["sha256"]:
                errors.append("last_session.sha256 mismatch")

    if index_p.exists() and last.get("id"):
        if last["id"] not in index_p.read_text():
            errors.append("last_session.id not in log/INDEX.md")

    compare_counts(pulse, measured, errors)
    compare_hashes(pulse, measured, errors)
    check_invariants(measured, errors)
    check_chain(hb_dir, pulse, errors)
    validate_schema_json(schema_p, pulse, errors)

    if errors:
        print("heartbeat diverged:")
        for e in errors:
            print(" -", e)
        return 2
    print("heartbeat ok")
    print(" status:", pulse.get("status"))
    print(" last  :", last.get("id"), last.get("activity"))
    print(" t     :", pulse.get("t"))
    print(" schema:", pulse.get("schema"))
    counts = measured.get("counts") or {}
    print(" attested cronologia/ontologia/conos:",
          counts.get("cronologia_n_nodes"),
          counts.get("ontologia_n_nodos"),
          counts.get("sim_meta_n_conos"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
