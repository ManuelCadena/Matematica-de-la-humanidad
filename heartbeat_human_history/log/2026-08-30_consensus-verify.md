# Sesión `2026-08-30-consensus-verify`

```
id:          2026-08-30-consensus-verify
agent:       Grok 4.6 (equipo Harper / Benjamin / Lucas)
started:     2026-08-30T23:34:00Z
ended:       2026-08-30T23:55:00Z
activity:    heartbeat
```

## Intent

Confirmar con el conector Consensus MCP si el diseño heartbeat
(AGENTS.md + SKILL.md + PROV-lite + pulso + CHANGELOG + logs) es
estado del arte, y verificar que el pulso coincide con el corpus.

## Used (prov:used)

- Consensus MCP `consensus___search` — 4 queries (agentic provenance,
  W3C PROV + LLM agents, AGENTS.md context files, OpenTelemetry GenAI)
- GitHub MCP — árbol remoto `ManuelCadena/Matematica-de-la-humanidad`
- `heartbeat_human_history/HEARTBEAT.json` (pulso previo)
- `datos/cronologia_mundial_arbol.json` meta
- `datos/historia_ontologia.json` meta
- `datos/civilizaciones_fibras.json` meta
- `datos/sim_meta.json`
- `datos/origenes/{homininos,yacimientos,migraciones,introgresion}.json`
- `AGENTS.md`, `skills/heartbeat-human-history/SKILL.md`

## Generated (prov:generated)

- `heartbeat_human_history/log/2026-08-30_consensus-verify.md` — esta sesión
- `heartbeat_human_history/log/INDEX.md` — línea nueva
- `heartbeat_human_history/HEARTBEAT.json` — counts corregidos
- `heartbeat_human_history/CHANGELOG.md` — counts de capa 0.5 corregidos

## Complements

No toca el corpus histórico. Solo audita el protocolo contra literatura
2025–2026 y contra `meta` real. Capa 0.5 sigue sin producir conos.

## Invariants

- [x] sin métrica escalar canónica
- [x] cono = polidad `[t0,t1]`
- [x] Teotihuacan apagada en t=700 (`sim_meta` t0=-100 t1=650)
- [x] species/migration/site/admixture ≠ cono de Estado
- [x] `A^n u` = escenario
- [x] sapiens pan-africano
- [x] OoA = pulsos, no una flecha
- [x] no se tocó el árbol
- [ ] selftest no aplica (solo auditoría)

## Counts (leídos de `meta` / top-level)

```
cronologia n_nodes:           2259   (pulse previo OK)
ontologia n_nodos:            2485   (pulse previo OK)
civilizaciones_fibras n:      22     (pulse previo OK)
sim_meta n_cones:             81     (pulse previo decía 42 — CORREGIDO)
origenes.species/homininos:   37     (pulse previo decía 31 — CORREGIDO)
origenes.sites/yacimientos:   38     (pulse previo decía 57 — CORREGIDO)
origenes.migrations:          14     (pulse previo decía 13 — CORREGIDO)
origenes.admixture:            7     (OK)
```

## Pending left for the next agent

- Subir a GitHub: README/CHANGELOG/schema/logs del heartbeat + skill
  (remoto hoy solo tiene `HEARTBEAT.json` + `log/INDEX.md`).
- Issue #1: corpus grande y specs 03–05.
- Extender el validador para cruzar `sim_meta.n_cones` y `origenes/*.n`.
- Taladro dinástico restante por región.

## Notes

Veredicto Consensus (no es un sí/no plano):

1. Las tres capas del diseño coinciden con el stack 2025–2026:
   AGENTS.md (AAIF/LF), SKILL.md (agentskills.io), provenance explícito
   (W3C PROV extendido a agentes).
2. AGENTS.md corto (49 líneas) es la decisión correcta: la evidencia
   empírica es mixta sobre success rate y documenta Context Bloat.
3. SKILL.md con frontmatter + `assets/` + `scripts/` + `references/`
   cumple progressive disclosure.
4. El heartbeat es un subconjunto justificado de PROV-AGENT / traces
   de ejecución: semántica Agent/Activity/Entity sin collector OTel.
   No equivale a sistemas 2026 con ledger criptográfico o spans runtime.
5. OTel GenAI no cubre planning/reasoning/memory/delegation; no usarlo
   como pulso de un corpus de conocimiento es coherente con AgentTelemetry.
6. El pulso fallaba su propia regla «no inventar counts» en conos y
   orígenes. Eso se corrige en esta sesión. Status sigue `degraded`
   porque GitHub no tiene el protocolo completo.
