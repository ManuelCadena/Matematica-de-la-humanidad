# Sesión `<id>`

```
id:          YYYY-MM-DD-<slug>
agent:       <modelo y versión>
started:     <ISO-8601>
ended:       <ISO-8601>
activity:    <read|add-node|fix-date|add-origin|add-cone|docs|repo-push|schema|app|heartbeat|refactor|correction>
protocol:    heartbeat.v1.1
```

## Intent

Una frase. Qué pidió el usuario.

## Chain

```
prev_session_id: <id de la sesión anterior o null>
prev_sha256:     <sha256 del markdown de esa sesión o null>
```

## Used (prov:used)

Cada ítem lleva rol. No mezclar evidencia cruda con claims.

```
- role: protocol|corpus-meta|origin-layer|cone|derived-artefact|skill
  path: <ruta>
  why:  <una línea>
```

## Generated (prov:generated)

```
- role: protocol|corpus-meta|origin-layer|cone|derived-artefact|skill
  path: <ruta>
  change: alta | correccion | docs | pulse
```

## Evidence

Obligatorio si `activity` ∈ `add-node|add-origin|fix-date|add-cone`.
Una fuente de handbook / paper por claim tocado. Vacío solo en docs/heartbeat.

```
- source: <cita corta>
  supports: <qué nodo / fecha / ruta>
```

## Complements

Qué parte del modelo se extiende sin sustituir otra (ej. capa 0.5 no apaga capa 3).

## Invariants

- [ ] sin métrica escalar canónica
- [ ] cono = polidad `[t0,t1]`
- [ ] Teotihuacan apagada en t=700
- [ ] species/migration/site/admixture ≠ cono de Estado
- [ ] `A^n u` = escenario
- [ ] sapiens pan-africano
- [ ] OoA = pulsos, no una flecha
- [ ] `flat` reconstruido si se tocó el árbol
- [ ] `python docs/referencia_modelos.py` → selftest ok (si aplica)
- [ ] `python skills/heartbeat-human-history/scripts/validate_heartbeat.py` → heartbeat ok
- [ ] conteos del pulso = `meta` atestado, no memoria del agente

## Counts (solo si tocaste corpus)

Leídos de `meta`, no inventados.

```
cronologia n_nodes:
ontologia n_nodos:
sim_meta n_conos:
origenes species/sites/migrations/admixture/anclas:
```

## Correction (solo si activity=correction)

```
corrects: <id de la sesión que se enmienda>
delta:    <qué número o claim cambia y de qué a qué>
```

## Pending left for the next agent

-

## Notes

Hechos. Sin transcript.
