# Sesión `2026-08-30-heartbeat`

```
id:          2026-08-30-heartbeat
agent:       Grok 4.6
started:     2026-08-30T23:27:00Z
ended:       2026-08-30T23:40:00Z
activity:    heartbeat
```

## Intent

Agregar `heartbeat_human_history` al repo — estatus, adiciones, cambios y log obligatorio — más un README de protocolo y un skill portable para cualquier modelo que toque el corpus.

## Used

- SOTA 2025–2026: AGENTS.md (AAIF/Linux Foundation), SKILL.md (agentskills.io), W3C PROV, Keep a Changelog, OpenTelemetry gen_ai.agent spans
- `LLM.md` §6 (contrato de extensión)
- `/root/.grok/skills/skill-creator/SKILL.md` (formato local)

## Generated

- `heartbeat_human_history/` (README, HEARTBEAT.json, schema, CHANGELOG, log/)
- `AGENTS.md` (ToC corto, estándar AAIF)
- `skills/heartbeat-human-history/` (SKILL.md + scripts + assets)
- skill persistente en `/home/workdir/.grok/skills/heartbeat-human-history/`

## Complements

No reemplaza `LLM.md` ni git. Cierra la capa de provenance que AGENTS.md y SKILL.md dejan abierta.

## Invariants

- [x] sin métrica escalar canónica
- [x] cono = polidad `[t0,t1]`
- [x] Teotihuacan apagada en t=700
- [x] species/migration/site/admixture ≠ cono de Estado
- [x] `A^n u` = escenario
- [x] sapiens pan-africano
- [x] OoA = pulsos, no una flecha
- [x] no se tocó el árbol en esta sesión
- [ ] selftest no aplica (solo docs + pulse)

## Counts

Sin cambio de corpus. Pulse cachea 2259 / 2485.

## Pending left for the next agent

- Push de esta carpeta + skill + AGENTS.md a GitHub.
- Seguir issue #1 (JSON grandes).

## Notes

Status del pulso = `degraded` a propósito: GitHub main aún no tiene el corpus local completo.
