# Session `<id>`

```
id:          YYYY-MM-DD-<slug>
agent:       <model and version>
started:     <ISO-8601>
ended:       <ISO-8601>
activity:    <read|add|fix|docs|repo-push|schema|app|heartbeat|refactor|correction>
protocol:    heartbeat.v1.1
```

## Intent

One sentence.

## Chain

```
prev_session_id: <previous id or null>
prev_sha256:     <sha256 of that markdown or null>
```

## Used (prov:used)

```
- role: protocol|corpus-meta|domain|derived-artefact|skill|config
  path: <path>
  why:  <one line>
```

## Generated (prov:generated)

```
- role: protocol|corpus-meta|domain|derived-artefact|skill|config
  path: <path>
  change: add | fix | docs | pulse
```

## Evidence

Required when the session mutates domain data. Empty for docs/heartbeat.

```
- source: <short citation>
  supports: <what>
```

## Complements

What this extends without replacing.

## Counts

Read from file meta or from `--write-attestation`. Never from memory.

```
<id> <key>: <n>
```

## Correction (only if activity=correction)

```
corrects: <old session id>
delta:    <what changed, from → to>
```

## Pending left for the next agent

-

## Notes

Facts. No transcript.
