#!/usr/bin/env python3
"""Scaffold a portable heartbeat/ tree in any repo."""
from __future__ import annotations

import argparse
import json
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
Claimed counts are invalid until `validate_heartbeat.py --write-attestation`.
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="target repository root")
    ap.add_argument("--repo", default="", help="owner/name for the pulse")
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
        cfg_dst.write_text(cfg_src.read_text())
    elif not cfg_dst.exists():
        cfg_dst.write_text(json.dumps({
            "schema": "heartbeat.config.v1",
            "repo": args.repo or root.name,
            "pulse_schema": "heartbeat.v1.1",
            "files": [],
            "invariants": [],
        }, indent=2) + "\n")

    schema_src = ASSETS / "heartbeat.schema.json"
    if schema_src.exists() and not (hb / "heartbeat.schema.json").exists():
        (hb / "heartbeat.schema.json").write_text(schema_src.read_text())

    tpl_src = ASSETS / "session.template.md"
    if tpl_src.exists():
        (hb / "session.template.md").write_text(tpl_src.read_text())

    val_src = HERE / "validate_heartbeat.py"
    if val_src.exists():
        (hb / "validate_heartbeat.py").write_text(val_src.read_text())

    index = log / "INDEX.md"
    if not index.exists():
        index.write_text("# Session index\n\nNewest first.\n\n- `genesis` — scaffold — heartbeat.v1.1\n")
    genesis = log / "genesis.md"
    if not genesis.exists():
        genesis.write_text("# Session `genesis`\n\n```\nid:          genesis\nagent:       sota-agent-heartbeat\nactivity:    heartbeat\nprotocol:    heartbeat.v1.1\n```\n\nScaffold only. Replace with a real session after the first edit.\n")

    changelog = hb / "CHANGELOG.md"
    if not changelog.exists():
        changelog.write_text("# Changelog\n\n## [Unreleased]\n\n- heartbeat.v1.1 scaffolded.\n")

    pulse = hb / "HEARTBEAT.json"
    if not pulse.exists():
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        pulse.write_text(json.dumps({
            "schema": "heartbeat.v1.1",
            "protocol_version": "1.1.0",
            "t": now,
            "status": "ok",
            "repo": args.repo or root.name,
            "corpus": {},
            "attestation": {"method": "init", "measured": {}, "hashes": {}, "invariants": {}},
            "chain": {"prev_session_id": None, "prev_sha256": None},
            "pending": ["fill heartbeat.config.json", "register first real session"],
            "invariants_ok": True,
            "last_session": {
                "id": "genesis",
                "agent": "sota-agent-heartbeat",
                "activity": "heartbeat",
                "log": "log/genesis.md",
            },
        }, indent=2) + "\n")

    print("heartbeat scaffolded at", hb)
    print("edit", cfg_dst)
    print("then run: python", hb / "validate_heartbeat.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
