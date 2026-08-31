# Install map

Target layout after

```
python scripts/init_heartbeat.py --root REPO --repo owner/name --copy-skill
```

```
REPO/
  AGENTS.md                     # short ToC (created only if missing)
  LLM.md                        # optional domain contract — you write this
  heartbeat/
    README.md                   # protocol (generic)
    HEARTBEAT.json              # pulse
    heartbeat.schema.json
    heartbeat.config.json       # project-specific counts + invariants
    CHANGELOG.md
    validate_heartbeat.py
    session.template.md
    log/
      INDEX.md
      genesis.md
  skills/
    sota-agent-heartbeat/       # this package, if --copy-skill
```

## heartbeat.config.json

```json
{
  "schema": "heartbeat.config.v1",
  "repo": "owner/name",
  "pulse_schema": "heartbeat.v1.1",
  "files": [
    {
      "id": "main-dataset",
      "path": "data/tree.json",
      "hash": true,
      "counts": [
        {"key": "n_nodes", "pointer": "/n_nodes"}
      ]
    }
  ],
  "invariants": [
    {
      "id": "example-interval",
      "path": "data/entities.json",
      "select": {"id": "entity-1"},
      "equals": {"t0": 0, "t1": 100}
    }
  ],
  "disjoint": [
    {
      "id": "kinds-do-not-collide",
      "a": {"path": "data/kind_a.json", "pointer": "/ids"},
      "b": {"path": "data/kind_b.json", "pointer": "/ids"}
    }
  ]
}
```

`pointer` is a JSON pointer (`/n_nodes`, `/meta/n`).
If the pointed value is an array and you want its length, use
`{"key": "n", "pointer": "/items", "length": true}`.

`select` finds an object in a list by key match (`id`, or the first
list field among `items`, `conos`, `nodes`, or any list-of-objects
value). `equals` is then checked on that object.

`disjoint` lists pairs of id-sets that must not overlap. Leave
empty if unused.

## Pulse fields the validator expects (v1.1)

Required: `schema`, `t`, `status`, `repo`, `corpus`, `last_session`,
`pending`, `invariants_ok`.

v1.1 also requires `attestation` and `chain`.

`corpus.<id>` counts must match measured values.
`attestation.hashes[<path>]` must match sha256 of that file.
`chain.prev_sha256` must match the previous session markdown.

## First session after init

1. Edit `heartbeat.config.json` so `files` point at real paths.
2. Copy `session.template.md` to `log/YYYY-MM-DD_<slug>.md`.
3. `prev_session_id` / `prev_sha256` may stay `null` if you replace
   genesis, or point at `genesis` if you keep it.
4. Run `--write-pulse`.
5. Add an INDEX line.
6. Validate (no flags). Exit 0.

## Copy into another project

Unzip this folder next to the target, or copy it under
`skills/sota-agent-heartbeat/`, then run init against that root.
Edit `heartbeat.config.json` only. Keep `AGENTS.md` short.
