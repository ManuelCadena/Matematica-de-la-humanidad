# Sesión `2026-08-31-docs-paper-figuras`

```
id:          2026-08-31-docs-paper-figuras
agent:       Devin
started:     2026-08-31T22:05:11Z
ended:       2026-08-31T22:05:11Z
activity:    docs
protocol:    heartbeat.v1.1
```

## Intent

Integrar los ensayos e imágenes de `Paper_Evolucion_de_la_Humanidad` al repo `Matematica-de-la-humanidad`, dejando solo las versiones más completas y complementarias.

## Chain

```
prev_session_id: 2026-08-31-higiene-taladro-40
prev_sha256:     16d96946f048faef1f7cf160d91fd05f7bf17ae6a36a1f3d9ebb1d034371623f
```

## Used (prov:used)

```
- role: derived-artefact
  path: /Users/manuelcadena/Fight For Life Club Dropbox/Manuel Cadena/Mi Mac (MacBook-Pro.localdomain)/Downloads/Paper_Evolucion_de_la_Humanidad (5).docx
  why:  redacción más completa del ensayo (11.716 palabras)
- role: derived-artefact
  path: /Users/manuelcadena/Fight For Life Club Dropbox/Manuel Cadena/Mi Mac (MacBook-Pro.localdomain)/Downloads/Paper_Evolucion_de_la_Humanidad (4).docx
  why:  guía de lectura complementaria de las láminas (7.668 palabras)
```

## Generated (prov:generated)

```
- role: derived-artefact
  path: docs/papers/Paper_Evolucion_de_la_Humanidad.md
  change: docs — sustituye stub por ensayo completo
- role: derived-artefact
  path: docs/papers/Paper_Evolucion_de_la_Humanidad.docx
  change: docs — fuente maquetada del ensayo
- role: derived-artefact
  path: docs/papers/guia-de-lectura-laminas.md
  change: docs — guía complementaria
- role: derived-artefact
  path: docs/papers/guia-de-lectura-laminas.docx
  change: docs — fuente maquetada de la guía
- role: derived-artefact
  path: docs/papers/figuras/media/*
  change: docs — láminas 1–9 extraídas de los .docx
- role: protocol
  path: docs/papers/README.md
  change: docs — índice actualizado
```

## Evidence

No requerido para actividad `docs`; se conservan las fuentes de las capturas del .docx originales.

## Complements

Capa documental; no toca corpus, conos ni invariantes. Las versiones (1), (2), (3) y (6) fueron descartadas por ser duplicadas o versiones parciales de (4) y (5).

## Invariants

- [x] sin métrica escalar canónica
- [x] cono = polidad `[t0,t1]`
- [x] Teotihuacan apagada en t=700
- [x] species/migration/site/admixture ≠ cono de Estado
- [x] `A^n u` = escenario
- [x] sapiens pan-africano
- [x] OoA = pulsos, no una flecha
- [x] `flat` reconstruido si se tocó el árbol
- [x] `python docs/referencia_modelos.py` → selftest ok
- [x] `python skills/heartbeat-human-history/scripts/validate_heartbeat.py` → heartbeat ok
- [x] conteos del pulso = `meta` atestado, no memoria del agente

## Counts

No se tocó el corpus; conteos sin cambio:

cronologia n_nodes: 2336
ontologia n_nodos: 2562
sim_meta n_conos: 81

## Pending left for the next agent

- Revisar que las imágenes rendericen correctamente en GitHub.
- Si se recibe una versión corregida del .docx, regenerar con `pandoc` y no duplicar archivos en `figuras/media/`.

## Notes

Conversión con `pandoc -f docx -t gfm --wrap=none --extract-media=docs/papers/figuras`.
