# Sesión `2026-08-31-github-skill-zip`

```
id:          2026-08-31-github-skill-zip
agent:       Grok 4.6
started:     2026-08-31T00:18:00Z
ended:       2026-08-31T00:45:00Z
activity:    repo-push
protocol:    heartbeat.v1.1
```

## Intent

Asegurar que GitHub hospede modelos + skill, y entregar un zip
genérico de `sota-agent-heartbeat` aplicable a cualquier proyecto.

## Chain

```
prev_session_id: 2026-08-31-repo-push-sota-skill
prev_sha256:     6c592a87ff586a78004de76ef0f612493754a8795973283e11646893a7650c3a
```

## Used (prov:used)

```
- role: protocol
  path: heartbeat_human_history/HEARTBEAT.json
  why:  lag list and pending
- role: skill
  path: skills/sota-agent-heartbeat/
  why:  harden to v1.2.0 generic
- role: domain
  path: docs/SPEC_03_FIBRAS_ACOPLES.md
  why:  remote is a stub; local is the contract
```

## Generated (prov:generated)

```
- role: skill
  path: skills/sota-agent-heartbeat/
  change: add
- role: derived-artefact
  path: /home/workdir/artifacts/sota-agent-heartbeat.zip
  change: add
- role: protocol
  path: heartbeat_human_history/log/2026-08-31_github-skill-zip.md
  change: add
```

## Evidence

Vacío: docs/protocolo/skill. No mutó nodos del corpus.

## Complements

v1.2.0 no sustituye heartbeat-human-history. El zip es el oficio
portable; este repo sigue usando el skill de dominio.

## Counts

Sin cambio de corpus. 2259 / 2485 / 81 / 37-38-14-7-9.

## Pending left for the next agent

- Empujar a GitHub (main o rama skill-v1.2-full-corpus) el skill
  v1.2.0 completo, SPEC_03-05 íntegros, validate_heartbeat.py,
  datos/, modelo/, logs. El conector bloqueó push_files y
  create_or_update_file esta sesión (duplicate lock).
- Comentario dejado en issue #1. Rama skill-v1.2-full-corpus
  creada apuntando a 8458842 (mismo árbol que main).
- Taladro dinástico por región — no inventar nodos.
- JSON grandes (~1.5 MB / 1.7 MB) pueden superar el límite de
  Contents API (1 MB). Usar Git Data API o un clone con credencial.

## Notes

- Zip local: artifacts/sota-agent-heartbeat.zip
  sha256 b0abb98b1c1cb17f9dde0738463c404e98e87099f243fe85587e7d17635e14a7
  21 archivos, protocol heartbeat.v1.1, skill v1.2.0, MIT.
- Demo init+validate en /tmp/demo-hb: heartbeat ok (tmp efímero).
- GitHub main HEAD 8458842. SPEC_03 remoto 605 B vs local 3498 B.
- No se pintó status=ok. Sigue degraded.
