# Sesión `2026-08-31-historia-modelada-html`

```
id:          2026-08-31-historia-modelada-html
agent:       Devin v1.0
started:     2026-09-01T00:17:34Z
ended:       2026-09-01T00:17:34Z
activity:    docs
protocol:    heartbeat.v1.1
```

## Intent

Generar un HTML autocontenido y navegable (`historia_modelada.html`) que consolide la narrativa matemática del proyecto, el abecedario de símbolos y ecuaciones del HTML (1), el ensayo largo `Paper_Evolucion_de_la_Humanidad` (5), su guía de lectura (4), los nuevos gráficos `phi_cortes_t0_700_1400.png`, `evolucion_archivo_densidad_conos.png` y los videos CGI; integrarlo en el repo sin alterar conos ni corpus.

## Chain

```
prev_session_id: 2026-08-31-higiene-taladro-40
prev_sha256:     16d96946f048faef1f7cf160d91fd05f7bf17ae6a36a1f3d9ebb1d034371623f
```

## Used (prov:used)

- role: derived-artefact
  path: docs/papers/Paper_Evolucion_de_la_Humanidad.md
  why:  Ensayo largo de civilización por civilización; cuerpo narrativo del documento.
- role: derived-artefact
  path: docs/papers/guia-de-lectura-laminas.md
  why:  Guía visual de las siete láminas y su lectura prohibida.
- role: derived-artefact
  path: Grok content/Modelos_Matematicos_Humanidad (1).html
  why:  V6.4.0 con ejemplos históricos; abecedario y ecuaciones 0-9.
- role: derived-artefact
  path: media/phi_cortes_t0_700_1400.png
  why:  Nuevos cortes de Phi en t=0, 700, 1400.
- role: derived-artefact
  path: media/evolucion_archivo_densidad_conos.png
  why:  Densidad de archivo por lente y conos vivos.
- role: derived-artefact
  path: media/video_*.mp4
  why:  Videos CGI del modelo para embeber en la narración.

## Generated (prov:generated)

- role: derived-artefact
  path: historia_modelada.html
  change: docs
- role: derived-artefact
  path: media/phi_cortes_t0_700_1400.png
  change: alta
- role: derived-artefact
  path: media/evolucion_archivo_densidad_conos.png
  change: alta

## Evidence

No aplica: actividad de documentación; no se modificaron conos ni nodos.

## Complements

Capa de documentación autocontenida; no reescribe ni apaga capas de corpus, conos, origen o fibrado. Se conserva el lenguaje y los invariantes del modelo v7.1.

## Invariants

- [x] sin métrica escalar canónica
- [x] cono = polidad `[t0,t1]`
- [x] Teotihuacan apagada en t=700
- [x] species/migration/site/admixture != cono de Estado
- [x] `A^n u` = escenario
- [x] sapiens pan-africano
- [x] OoA = pulsos, no una flecha
- [x] `flat` reconstruido si se tocó el árbol (no se tocó)
- [ ] `python docs/referencia_modelos.py` -> selftest ok
- [ ] `python skills/heartbeat-human-history/scripts/validate_heartbeat.py` -> heartbeat ok
- [x] conteos del pulso = `meta` atestado, no memoria del agente

## Counts

```
cronologia n_nodes: 2336
ontologia n_nodos: 2562
sim_meta n_conos: 81
origenes species/sites/migrations/admixture/anclas: 37/41/14/7/9
```

## Notas

El HTML se generó con `pandoc` a partir de `intro.md`, `Modelos_Matematicos_Humanidad (1).html` convertido a GFM, `Paper_Evolucion_de_la_Humanidad.md` y `guia-de-lectura-laminas.md`, con CSS oscuro autocontenido, navegación por TOC e inserción de videos. Rutas de imágenes normalizadas a raíz.
