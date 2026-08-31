# Install map

Target layout after `init_heartbeat.py --root REPO`:

```
REPO/
  AGENTS.md
  heartbeat/
    README.md
    HEARTBEAT.json
    heartbeat.schema.json
    heartbeat.config.json
    CHANGELOG.md
    validate_heartbeat.py
    session.template.md
    log/INDEX.md
  skills/sota-agent-heartbeat/
```

Copy this whole skill directory, run init against the other root.
Edit heartbeat.config.json only. Keep AGENTS.md short.
Claimed counts are invalid until measured.
