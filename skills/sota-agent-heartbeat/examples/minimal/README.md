# Minimal demo

From the skill root:

```
python scripts/init_heartbeat.py --root /tmp/demo-hb --repo demo/minimal
cp examples/minimal/data/example.json /tmp/demo-hb/data/example.json
# edit /tmp/demo-hb/heartbeat/heartbeat.config.json so path is data/example.json
python /tmp/demo-hb/heartbeat/validate_heartbeat.py --write-pulse
python /tmp/demo-hb/heartbeat/validate_heartbeat.py
```

Expected: `heartbeat ok`.
