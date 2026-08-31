# sota-agent-heartbeat

Generic, drop-in provenance layer for any repository that more than
one agent (or one agent across many sessions) will touch.

Protocol **heartbeat.v1.1**. Skill package **v1.2.0**.

Not git. Not OpenTelemetry. A short `AGENTS.md`, a `SKILL.md`, and a
text-first pulse + append-only session log that any model can write
with an editor.

## Install into another project

```bash
unzip sota-agent-heartbeat.zip
python sota-agent-heartbeat/scripts/init_heartbeat.py \
  --root /path/to/your/repo \
  --repo owner/name
```

Then edit only `your-repo/heartbeat/heartbeat.config.json`:

- `files[]` — JSON (or any file) to hash and, if JSON, to count
- `invariants[]` — equality checks (`select` + `equals`)
- `disjoint[]` — pairs of id-sets that must not overlap

```bash
python your-repo/heartbeat/validate_heartbeat.py --write-pulse
python your-repo/heartbeat/validate_heartbeat.py
```

Exit 0 = the pulse matches the files. Exit 2 = diverged.

## What you get

```
your-repo/
  AGENTS.md                      # created only if missing / empty
  heartbeat/
    README.md
    HEARTBEAT.json               # pulse (cache + attestation)
    heartbeat.schema.json
    heartbeat.config.json        # YOU fill this
    CHANGELOG.md
    validate_heartbeat.py
    session.template.md
    log/INDEX.md
    log/genesis.md
  skills/sota-agent-heartbeat/   # copy of this package
```

## Contract in one screen

A session is valid only if all of these exist:

1. `heartbeat/log/YYYY-MM-DD_<slug>.md` from the template
2. `chain.prev_session_id` + `chain.prev_sha256` of the previous log
   (both `null` on genesis)
3. a new bullet at the top of `heartbeat/log/INDEX.md`
4. `HEARTBEAT.json` with `schema=heartbeat.v1.1` and `attestation`
   produced by the validator, not from memory
5. no invented counts

Do not rewrite old session files. To correct, add a `correction`
session that cites the old `id` and a `delta`.

## Status values

| status | meaning |
|---|---|
| `ok` | pulse matches local files; invariants not known broken |
| `degraded` | workspace is ahead of the remote / a derived artefact lags |
| `diverged` | claimed count ≠ measured, or a hash / invariant failed |
| `blocked` | cannot finish without a human |

Never paint `degraded` as `ok`.

## Three layers (do not collapse them)

| Layer | File | Job |
|---|---|---|
| Instruction | `AGENTS.md` | short table of contents |
| Capability | `skills/*/SKILL.md` | how to do one craft |
| Provenance | `heartbeat/` | who did what to what |

Keep `AGENTS.md` under ~80 lines. Domain rules live in a contract
file of your choosing (`LLM.md`, `CONTRIBUTING.md`, specs).

## This zip vs a project-specific skill

This package is **generic**. It must not contain another project's
invariants, node counts, or dataset paths. Bind those in
`heartbeat.config.json` after init.

## License

MIT. See `LICENSE`.
