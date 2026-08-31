---
name: heartbeat-human-history
description: Register every session that touches Matematica de la humanidad. Use when starting or ending work on the corpus, repo, cones, ontologia, origenes, or when the user mentions heartbeat, log de agentes, status del repo, o registrar cambios. Mandatory before claiming a file was saved.
metadata:
  type: workflow
  version: "1.1.0"
  repo: Matematica-de-la-humanidad
  protocol: heartbeat.v1.1
---

# Heartbeat of Human History

Append-only session log + attested status pulse. Not git. Not OpenTelemetry.
W3C-PROV-shaped record any agent can write with a text editor.

Protocol **v1.1**: claimed counts are invalid until the validator measures
them. Sessions form a sha256 chain. Historical invariants are executable.

## When this skill is active

1. Read `heartbeat_human_history/HEARTBEAT.json` first (current pulse).
2. Read `heartbeat_human_history/README.md` (protocol).
3. Do the user work.
4. Before declaring done, append a session file and update the pulse.
5. Run the validator. If you cannot write the log, say so.

Repo-relative root (workspace) — `Modelo_Matematico_de_la_Humanidad/heartbeat_human_history/`.
GitHub root — `heartbeat_human_history/`.

## Protocol in one screen

A session is valid only if all of these exist

- a file `log/YYYY-MM-DD_<slug>.md` using `assets/session.template.md`
- `chain.prev_session_id` + `chain.prev_sha256` of the previous log
- a new bullet at the top of `log/INDEX.md`
- `HEARTBEAT.json` with `schema=heartbeat.v1.1`, `attestation` from
  `--write-attestation`, `corpus` copied from measured counts
- no invented node counts

Do not rewrite previous session files. Append. If you must correct, add
a `correction` session that cites the old `id` and a `delta`.

## Status values

- `ok` — pulse matches local corpus; invariants not known broken
- `degraded` — work landed locally but GitHub or a derived artefact lags
- `diverged` — `corpus` ≠ attestation, or a hash / invariant failed
- `blocked` — cannot complete the user request without a human

## Actions (`activity.type`)

`read` `add-node` `fix-date` `add-origin` `add-cone` `docs` `repo-push` `schema` `app` `heartbeat` `refactor` `correction`

## Invariants the validator executes

- Teotihuacan `[t0,t1] = [-100, 650]` and off at t=700
- `species|site|migration|admixture` ids ∩ cone ids = ∅
- pulse counts = file `meta` for árbol, ontología, fibras, sim_meta, orígenes
- `attestation.hashes` match sha256 on disk
- `chain.prev_sha256` matches the previous session file

Checklist ticks from `LLM.md` still go in the session markdown.

## Evidence rule

If activity ∈ `add-node|add-origin|fix-date|add-cone`, the session lists
at least one scholarly source. Docs/heartbeat sessions may leave Evidence empty.

## Files this skill owns

| path | role |
|---|---|
| `heartbeat_human_history/README.md` | protocol |
| `heartbeat_human_history/HEARTBEAT.json` | pulse + attestation |
| `heartbeat_human_history/heartbeat.schema.json` | draft-07 |
| `heartbeat_human_history/CHANGELOG.md` | Keep a Changelog |
| `heartbeat_human_history/log/INDEX.md` | newest-first |
| `heartbeat_human_history/log/*.md` | one session each |
| `scripts/validate_heartbeat.py` | measure + compare |
| `assets/session.template.md` | copy this |

## Validate

```
python skills/heartbeat-human-history/scripts/validate_heartbeat.py --write-attestation
python skills/heartbeat-human-history/scripts/validate_heartbeat.py
```

Exit 0 = pulse and files agree. Exit 2 = diverged.

## What not to do

- Do not dump a chat transcript into the log.
- Do not put secrets or private user data in the pulse.
- Do not treat `HEARTBEAT.json` as the corpus. Counts are a cache of `meta`.
- Do not skip the log because it was only docs.
- Do not inflate `AGENTS.md`. Point to this skill.
- Do not use this skill as a substitute for `LLM.md` §6 when adding a node.
