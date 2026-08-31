---
name: sota-agent-heartbeat
description: Install and operate a SOTA-plus agentic provenance layer in any repository. Use when adding AGENTS.md, SKILL.md, session logs, an attested pulse, a hash chain, heartbeat protocol, or reusable agent documentation that other models must follow.
metadata:
  type: workflow
  version: "1.2.0"
  protocol: heartbeat.v1.1
  portable: "true"
license: MIT
---

# SOTA Agent Heartbeat

Portable protocol for any repo that multiple agents will touch.
Not git. Not OpenTelemetry. A W3C-PROV-shaped pulse + append-only
session log that an agent can write with a text editor.

Generic form of the three-layer stack (AGENTS.md + SKILL.md +
attested heartbeat). Domain invariants stay in the target repo
via `heartbeat.config.json`. This skill has no project-specific facts.

## When to use

- User asks for SOTA agent docs, heartbeat, provenance, AGENTS.md,
  session log, or a protocol other models must register against.
- Starting or hardening a multi-agent repository.
- Copying this pattern into another project.

## Do this in order

1. Read `references/install.md` for the file map.
2. Read `references/protocol.md` for the contract an agent must keep.
3. Read `references/sota.md` only if you must justify the design.
4. Run the init script against the target repo root.
5. Fill `heartbeat.config.json` (what to count, which invariants).
6. Keep `AGENTS.md` under 80 lines. Domain rules go in a separate
   contract file (`LLM.md`, `CONTRIBUTING.md`, `SPEC_*.md`).
7. After every session that writes files, append a log, update
   the pulse from `--write-pulse`, run the validator.

## Three layers that must not collapse

| Layer | File | Job | Not its job |
|---|---|---|---|
| Instruction | `AGENTS.md` | short ToC | history, skills, essays |
| Capability | `SKILL.md` in `skills/` | how to do one craft | repo status |
| Provenance | `heartbeat/` | who did what to what | runtime traces |

A bloated `AGENTS.md` is a known failure mode. Keep it an index.

## v1.1 rules (SOTA-plus)

Claimed counts are invalid until measured.

- `corpus` in the pulse is a cache.
- `attestation.measured` + `attestation.hashes` come from disk.
- Sessions form a sha256 chain. Do not rewrite old logs.
- Invariants in `heartbeat.config.json` are executed by the
  validator, not ticked by memory.
- `used` / `generated` carry a `role`.
- Mutation activities require an evidence line.

Status values: `ok` | `degraded` | `diverged` | `blocked`.
`degraded` means the remote lags the workspace. Do not paint it `ok`.

## Init

```
python skills/sota-agent-heartbeat/scripts/init_heartbeat.py --root /path/to/repo --repo owner/name
```

Creates `AGENTS.md` if missing, `heartbeat/`, `heartbeat.config.json`,
a copy of the validator, and (optional) `skills/sota-agent-heartbeat/`.
Does not overwrite a non-empty `AGENTS.md`.

## Validate

```
python heartbeat/validate_heartbeat.py --write-attestation
python heartbeat/validate_heartbeat.py --write-pulse
python heartbeat/validate_heartbeat.py
```

`--write-attestation` prints measured counts/hashes to stdout.
`--write-pulse` writes those into `heartbeat/HEARTBEAT.json` and
refreshes `t`. Then run with no flags. Exit 0 = pulse matches files.
Exit 2 = diverged.

## Config

`heartbeat.config.json` is the only project-specific file the
validator needs. Example in `assets/heartbeat.config.json`.

Declare files to hash, JSON pointers for counts, optional equality
invariants, and optional disjoint id-sets. Do not put domain
essays in this skill.

## Session file

Copy `assets/session.template.md` to
`heartbeat/log/YYYY-MM-DD_<slug>.md`. Fill chain, roles, evidence.

Generic `activity` values:

`read` `add` `fix` `docs` `repo-push` `schema` `app` `heartbeat` `refactor` `correction`

A project may add its own verbs. Mutation of domain data still
requires an Evidence line.

## What not to do

- Do not store chat transcripts, secrets, or user PII in the pulse.
- Do not treat the pulse as the source of truth.
- Do not invent counts. Measure.
- Do not add a collector, DID stack, or RDF export unless the
  user asked for infrastructure. This protocol is text-first.
- Do not grow `AGENTS.md` past about 80 lines. Link out.
- Do not hard-code another project's invariants in this skill.
