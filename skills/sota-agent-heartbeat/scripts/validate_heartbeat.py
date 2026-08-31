#!/usr/bin/env python3
"""Generic heartbeat validator (protocol heartbeat.v1.1).

Reads heartbeat.config.json when present. Works in any repo.
Exit 0 = ok. Exit 2 = diverged.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA_OK = {"heartbeat.v1", "heartbeat.v1.1"}
STATUS_OK = {"ok", "degraded", "diverged", "blocked"}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / "heartbeat" / "HEARTBEAT.json").exists():
            return p
        if (p / "heartbeat_human_history" / "HEARTBEAT.json").exists():
            return p
    return start


def hb_dir_of(root: Path) -> Path:
    if (root / "heartbeat" / "HEARTBEAT.json").exists():
        return root / "heartbeat"
    if (root / "heartbeat_human_history" / "HEARTBEAT.json").exists():
        return root / "heartbeat_human_history"
    if (root / "heartbeat").is_dir():
        return root / "heartbeat"
    return root / "heartbeat_human_history"


def pointer_get(doc: Any, pointer: str) -> Any:
    if not pointer or pointer == "/":
        return doc
    cur = doc
    for part in pointer.lstrip("/").split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(cur, dict):
            cur = cur.get(part)
        elif isinstance(cur, list):
            try:
                cur = cur[int(part)]
            except (ValueError, IndexError):
                return None
        else:
            return None
    return cur


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def resolve(root: Path, rel: str) -> Path:
    return root / rel


def _as_id_set(val: Any) -> set[str]:
    if val is None:
        return set()
    if isinstance(val, list):
        out = set()
        for item in val:
            if isinstance(item, str):
                out.add(item)
            elif isinstance(item, dict) and "id" in item:
                out.add(str(item["id"]))
        return out
    if isinstance(val, dict):
        if all(isinstance(k, str) for k in val.keys()):
            return set(val.keys())
    return set()


def measure(root: Path, cfg: dict) -> dict:
    measured: dict[str, Any] = {"counts": {}, "hashes": {}, "invariants": {}}
    for spec in cfg.get("files") or []:
        rel = spec.get("path")
        if not rel:
            continue
        path = resolve(root, rel)
        if not path.exists():
            measured["invariants"][f"missing:{rel}"] = {"ok": False, "got": None}
            continue
        fid = spec.get("id") or rel
        if spec.get("hash", True):
            measured["hashes"][rel] = sha256_file(path)
        if path.suffix == ".json":
            try:
                doc = load_json(path)
            except Exception as e:
                measured["invariants"][f"unreadable:{rel}"] = str(e)
                continue
            for c in spec.get("counts") or []:
                key = c.get("key")
                val = pointer_get(doc, c.get("pointer") or "/")
                if c.get("length") and isinstance(val, (list, dict)):
                    val = len(val)
                if key is not None and val is not None:
                    measured["counts"][f"{fid}.{key}"] = val
                    measured["counts"][key] = val
            for inv in spec.get("invariants") or []:
                check_one_invariant(doc, inv, measured)
    for inv in cfg.get("invariants") or []:
        path = resolve(root, inv.get("path") or "")
        if not path.exists():
            measured["invariants"][inv.get("id") or "inv"] = {"ok": False, "got": "missing-file"}
            continue
        try:
            doc = load_json(path)
        except Exception:
            continue
        check_one_invariant(doc, inv, measured)
    for pair in cfg.get("disjoint") or []:
        pid = pair.get("id") or "disjoint"
        try:
            a = pointer_get(load_json(resolve(root, pair["a"]["path"])), pair["a"].get("pointer") or "/")
            b = pointer_get(load_json(resolve(root, pair["b"]["path"])), pair["b"].get("pointer") or "/")
            overlap = sorted(_as_id_set(a) & _as_id_set(b))
            measured["invariants"][pid] = {"ok": overlap == [], "got": overlap}
        except Exception as e:
            measured["invariants"][pid] = {"ok": False, "got": str(e)}
    return measured


def check_one_invariant(doc: Any, inv: dict, measured: dict) -> None:
    iid = inv.get("id") or "inv"
    target = doc
    sel = inv.get("select")
    if sel:
        arr = None
        if isinstance(doc, list):
            arr = doc
        elif isinstance(doc, dict):
            for key in ("conos", "items", "nodes", "nodos", "entries"):
                if isinstance(doc.get(key), list):
                    arr = doc[key]
                    break
            if arr is None:
                for v in doc.values():
                    if isinstance(v, list) and v and isinstance(v[0], dict):
                        arr = v
                        break
        if arr is not None:
            target = next((x for x in arr if all(x.get(k) == val for k, val in sel.items())), None)
    equals = inv.get("equals") or {}
    ok = True
    if target is None:
        ok = False
        got = None
    else:
        got = {k: target.get(k) for k in equals}
        for k, val in equals.items():
            if target.get(k) != val:
                ok = False
    measured["invariants"][iid] = {"ok": ok, "got": got}


def compare(pulse: dict, measured: dict, cfg: dict, errors: list[str]) -> None:
    corpus = pulse.get("corpus") or {}
    for spec in cfg.get("files") or []:
        fid = spec.get("id")
        entry = corpus.get(fid) or {}
        for c in spec.get("counts") or []:
            key = c.get("key")
            declared = entry.get(key) if isinstance(entry, dict) else None
            if declared is None:
                declared = corpus.get(key)
            actual = (measured.get("counts") or {}).get(f"{fid}.{key}")
            if actual is None:
                actual = (measured.get("counts") or {}).get(key)
            if declared is not None and actual is not None and declared != actual:
                errors.append(f"diverged {fid}.{key} pulse={declared} file={actual}")
    claimed_hashes = ((pulse.get("attestation") or {}).get("hashes")) or {}
    actual_hashes = measured.get("hashes") or {}
    for rel, digest in claimed_hashes.items():
        if rel in actual_hashes and actual_hashes[rel] != digest:
            errors.append(f"hash mismatch {rel}")
    for iid, result in (measured.get("invariants") or {}).items():
        if isinstance(result, dict) and result.get("ok") is False:
            errors.append(f"invariant failed {iid} got={result.get('got')}")


def check_chain(hb_dir: Path, pulse: dict, errors: list[str]) -> None:
    chain = pulse.get("chain") or {}
    prev_id = chain.get("prev_session_id")
    prev_hash = chain.get("prev_sha256")
    if not prev_id or not prev_hash:
        return
    match = None
    log_dir = hb_dir / "log"
    if log_dir.is_dir():
        for p in log_dir.glob("*.md"):
            if p.name == "INDEX.md":
                continue
            text = p.read_text()
            if prev_id in text[:400] or prev_id.replace("-", "_") in p.stem:
                match = p
                break
    if match is None:
        errors.append(f"chain.prev_session_id not found: {prev_id}")
        return
    digest = sha256_file(match)
    if digest != prev_hash:
        errors.append(f"chain.prev_sha256 mismatch file={match.name}")


def attestation_payload(measured: dict) -> dict:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "method": "validate_heartbeat.py",
        "t": now,
        "measured": measured.get("counts") or {},
        "hashes": measured.get("hashes") or {},
        "invariants": measured.get("invariants") or {},
    }


def write_pulse(pulse_p: Path, measured: dict) -> None:
    pulse = load_json(pulse_p) if pulse_p.exists() else {}
    att = attestation_payload(measured)
    pulse.setdefault("schema", "heartbeat.v1.1")
    pulse["attestation"] = att
    pulse["t"] = att["t"]
    failed = [
        k
        for k, v in (measured.get("invariants") or {}).items()
        if isinstance(v, dict) and v.get("ok") is False
    ]
    if failed and pulse.get("status") == "ok":
        pulse["status"] = "diverged"
        pulse["invariants_ok"] = False
    elif not failed:
        pulse["invariants_ok"] = True
    pulse_p.write_text(json.dumps(pulse, indent=2, ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="")
    ap.add_argument("--write-attestation", action="store_true")
    ap.add_argument(
        "--write-pulse",
        action="store_true",
        help="write measured attestation into HEARTBEAT.json",
    )
    args = ap.parse_args()
    root = Path(args.root).resolve() if args.root else find_root(Path.cwd())
    hb_dir = hb_dir_of(root)
    pulse_p = hb_dir / "HEARTBEAT.json"
    cfg_p = hb_dir / "heartbeat.config.json"
    if not cfg_p.exists():
        cfg_p = root / "heartbeat.config.json"
    cfg = load_json(cfg_p) if cfg_p.exists() else {"files": []}
    measured = measure(root, cfg)

    if args.write_attestation and not args.write_pulse:
        json.dump(attestation_payload(measured), sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
        return 0

    if args.write_pulse:
        if not pulse_p.exists():
            print("heartbeat missing:", pulse_p, file=sys.stderr)
            return 2
        write_pulse(pulse_p, measured)
        print("wrote attestation into", pulse_p)

    errors: list[str] = []
    if not pulse_p.exists():
        print("heartbeat missing:", pulse_p, file=sys.stderr)
        return 2
    pulse = load_json(pulse_p)
    if pulse.get("schema") not in SCHEMA_OK:
        errors.append(f"bad schema {pulse.get('schema')}")
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
    if log_rel:
        log_p = hb_dir / log_rel
        if not log_p.exists():
            log_p = hb_dir / "log" / Path(str(log_rel)).name
        if not log_p.exists():
            errors.append(f"last_session.log missing: {log_rel}")
        elif last.get("id") and last["id"] not in log_p.read_text():
            errors.append("last_session.id not in log file")
        elif last.get("sha256") and sha256_file(log_p) != last["sha256"]:
            errors.append("last_session.sha256 mismatch")
    index_p = hb_dir / "log" / "INDEX.md"
    if index_p.exists() and last.get("id") and last["id"] not in index_p.read_text():
        errors.append("last_session.id not in log/INDEX.md")

    compare(pulse, measured, cfg, errors)
    check_chain(hb_dir, pulse, errors)

    schema_p = hb_dir / "heartbeat.schema.json"
    if schema_p.exists():
        try:
            import jsonschema  # type: ignore

            jsonschema.validate(pulse, load_json(schema_p))
        except ImportError:
            pass
        except Exception as e:
            errors.append(f"schema: {e}")

    if errors:
        print("heartbeat diverged:")
        for e in errors:
            print(" -", e)
        return 2
    print("heartbeat ok")
    print(" status:", pulse.get("status"))
    print(" last  :", last.get("id"), last.get("activity"))
    print(" t     :", pulse.get("t"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
