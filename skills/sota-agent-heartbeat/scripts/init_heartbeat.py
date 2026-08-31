#!/usr/bin/env python3
"""Scaffold a portable heartbeat/ tree in any repo."""
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
ASSETS = SKILL / "assets"

AGENTS_STUB = """# AGENTS.md

Project-level instructions for coding agents. Standard AGENTS.md
(AAIF / Linux Foundation). This file is an index, not an encyclopedia.

## Before touching anything

1. Read the domain contract (`LLM.md` or `CONTRIBUTING.md`) if it exists.
2. Read `heartbeat/README.md`.
3. Read `heartbeat/HEARTBEAT.json`.
4. Register every session that writes files.

## Validate

```
python heartbeat/validate_heartbeat.py
```

## Commits

Short message. Do not rewrite heartbeat session history.
"""

README_STUB = """# Heartbeat

Append-only session log + attested pulse. Protocol heartbeat.v1.1.

See the portable skill `sota-agent-heartbeat` for the contract.
Claimed counts are invalid until `validate_heartbeat.py --write-pulse`.

Status values: `ok` | `degraded` | `diverged` | `blocked`.
`degraded` means the remote lags the workspace. Do not paint it `ok`.

## After every session that writes files

1. Copy `session.template.md` to `log/YYYY-MM-DD_<slug>.md`.
2. Point `chain` at the previous session markdown.
3. Add a bullet at the top of `log/INDEX.md`.
4. `python heartbeat/validate_heartbeat.py --write-pulse`
5. `python heartbeat/validate_heartbeat.py` — exit 0.
"""


def _copy_if_missing(src: Path, dst: Path) -> None:
    if src.exists() and not dst.exists():
        dst.write_text(src.read_text())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="target repository root")
    ap.add_argument("--repo", default="", help="owner/name for the pulse")
    ap.add_argument(
        "--copy-skill",
        action="store_true",
        help="copy this package into <root>/skills/sota-agent-heartbeat/",
    )
    args = ap.parse_args()
    root = Path(args.root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    hb = root / "heartbeat"
    log = hb / "log"
    hb.mkdir(exist_ok=True)
    log.mkdir(exist_ok=True)

    agents = root / "AGENTS.md"
    if not agents.exists() or agents.stat().st_size == 0:
        agents.write_text(AGENTS_STUB)

    if not (hb / "README.md").exists():
        hb.joinpath("README.md").write_text(README_STUB)

    cfg_src = ASSETS / "heartbeat.config.json"
    cfg_dst = hb / "heartbeat.config.json"
    if not cfg_dst.exists() and cfg_src.exists():
        text = cfg_src.read_text()
        if args.repo:
            try:
                cfg = json.loads(text)
                cfg["repo"] = args.repo
                text = json.dumps(cfg, indent=2) + "\n"
            except Exception:
                pass
        cfg_dst.write_text(text)
    elif not cfg_dst.exists():
        cfg_dst.write_text(
            json.dumps(
                {
                    "schema": "heartbeat.config.v1",
                    "repo": args.repo or root.name,
                    "pulse_schema": "heartbeat.v1.1",
                    "files": [],
                    "invariants": [],
                    "disjoint": [],
                },
                indent=2,
            )
            + "\n"
        )

    _copy_if_missing(ASSETS / "heartbeat.schema.json", hb / "heartbeat.schema.json")

    tpl_src = ASSETS / "session.template.md"
    if tpl_src.exists():
        (hb / "session.template.md").write_text(tpl_src.read_text())

    val_src = HERE / "validate_heartbeat.py"
    if val_src.exists():
        (hb / "validate_heartbeat.py").write_text(val_src.read_text())

    index = log / "INDEX.md"
    if not index.exists():
        index.write_text(
            "# Session index\n\nNewest first.\n\n"
            "- `genesis` — scaffold — heartbeat.v1.1\n"
        )
    genesis = log / "genesis.md"
    if not genesis.exists():
        genesis.write_text(
            "# Session `genesis`\n\n"
            "```\n"
            "id:          genesis\n"
            "agent:       sota-agent-heartbeat\n"
            "activity:    heartbeat\n"
            "protocol:    heartbeat.v1.1\n"
            "```\n\n"
            "## Chain\n\n"
            "```\n"
            "prev_session_id: null\n"
            "prev_sha256:     null\n"
            "```\n\n"
            "Scaffold only. Replace with a real session after the first edit.\n"
        )

    changelog = hb / "CHANGELOG.md"
    if not changelog.exists():
        changelog.write_text("# Changelog\n\n## [Unreleased]\n\n- heartbeat.v1.1 scaffolded.\n")

    pulse = hb / "HEARTBEAT.json"
    if not pulse.exists():
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        pulse.write_text(
            json.dumps(
                {
                    "schema": "heartbeat.v1.1",
                    "protocol_version": "1.1.0",
                    "t": now,
                    "status": "ok",
                    "repo": args.repo or root.name,
                    "corpus": {},
                    "attestation": {
                        "method": "init",
                        "t": now,
                        "measured": {},
                        "hashes": {},
                        "invariants": {},
                    },
                    "chain": {"prev_session_id": None, "prev_sha256": None},
                    "pending": [
                        "fill heartbeat.config.json",
                        "register first real session",
                    ],
                    "invariants_ok": True,
                    "last_session": {
                        "id": "genesis",
                        "agent": "sota-agent-heartbeat",
                        "activity": "heartbeat",
                        "log": "log/genesis.md",
                    },
                },
                indent=2,
            )
            + "\n"
        )

    if args.copy_skill:
        dest = root / "skills" / "sota-agent-heartbeat"
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            ignore = shutil.ignore_patterns("__pycache__", "*.pyc", ".git")
            shutil.copytree(SKILL, dest, ignore=ignore)
            print("skill copied to", dest)
        else:
            print("skill already present at", dest)

    print("heartbeat scaffolded at", hb)
    print("edit", cfg_dst)
    print("then run: python", hb / "validate_heartbeat.py --write-pulse")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
