# Protocol heartbeat.v1.1 (generic)

Any agent that writes files in a repo using this skill must
leave an auditable session. The next agent, on a cold start,
must be able to reconstruct who did what to what without the
chat transcript.

## Before declaring done

1. Read `heartbeat/HEARTBEAT.json` (current pulse).
2. Read `heartbeat/README.md` (this contract, copied at init).
3. Do the user work.
4. Copy `heartbeat/session.template.md` to
   `heartbeat/log/YYYY-MM-DD_<slug>.md` and fill it.
5. Add one bullet at the top of `heartbeat/log/INDEX.md`.
6. Run `python heartbeat/validate_heartbeat.py --write-pulse`.
7. Run `python heartbeat/validate_heartbeat.py`. Exit 0.
8. If you cannot write the log, say so. Do not pretend.

## Session identity

```
id:       YYYY-MM-DD-<slug>
agent:    <model and version>
activity: read|add|fix|docs|repo-push|schema|app|heartbeat|refactor|correction
```

Projects may add verbs. If the activity mutates domain data,
the Evidence section is required.

## Chain

```
prev_session_id: <previous id or null>
prev_sha256:     <sha256 of that markdown or null>
```

Genesis may use `null` / `null`. Every later session points at
the previous markdown. Rewriting an old log breaks the chain.
To correct, add a `correction` session.

## Roles

`used` and `generated` rows carry `role`:

`protocol` `corpus-meta` `domain` `derived-artefact` `skill` `config`

## Status

`ok` · `degraded` · `diverged` · `blocked`

`degraded` is honest when the workspace is ahead of the remote.
Do not paint it `ok`.

## What not to record

- Chat transcripts.
- Secrets, tokens, local absolute paths of a user's machine.
- Invented counts. Measure.

## PROV mapping (no RDF export)

| Session field | PROV |
|---|---|
| `agent` | `prov:Agent` |
| `activity` | `prov:Activity` |
| `used` + `role` | `prov:used` |
| `generated` + `role` | `prov:generated` |
| `started` / `ended` | `prov:startedAtTime` / `endedAtTime` |
| `chain` | `prov:wasInformedBy` |
| `attestation.hashes` | integrity of Entity |
