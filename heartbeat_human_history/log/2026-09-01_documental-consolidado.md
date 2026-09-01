# Sesión `2026-09-01-documental-consolidado`

```
id:          2026-09-01-documental-consolidado
agent:       Devin v1.0
started:     2026-09-01T05:42:56.410499+00:00
ended:       2026-09-01T05:51:52.141170+00:00
activity:    docs
protocol:    heartbeat.v1.1
```

## Intent

Generar el entregable final del masterplan: HTML consolidado del documental matemático de la humanidad (intro + 8 capítulos), índice, capítulos individuales, georreferenciación de las 16 regiones, figuras derivadas de `referencia_modelos.py` y un video HD 1080p60, todo en español y respetando los invariantes del corpus.

## Chain

```
prev_session_id: 2026-08-31-historia-modelada-html
prev_sha256:     0285fdb7355edbc976a6d9dc0675941721a97e01d86306ba04eeb2c8523bad79
```

## Used (prov:used)

```
- role: protocol
  path: docs/referencia_modelos.py
  why:  Algoritmos canónicos importados por el generador.
- role: corpus-meta
  path: datos/civilizaciones_fibras.json
  why:  22 fibras con soportes [t0,t1] para conos geográficos.
- role: corpus-meta
  path: datos/ontologia_nodos.jsonl
  why:  2562 nodos para conteos y top-10 por lente.
- role: corpus-meta
  path: datos/acoples_multicapa.json
  why:  39 acoples tipados para matrices A_t.
- role: corpus-meta
  path: datos/modelo_espacio_tiempo.json
  why:  Grafo de 16 regiones y 6 lentes.
- role: skill
  path: skills/heartbeat-human-history/SKILL.md
  why:  Protocolo de pulso y attestation.
```

## Generated (prov:generated)

```
- role: protocol
  path: datos/regiones_geograficas.json
  change: docs
- role: protocol
  path: datos/regiones_geograficas.md
  change: docs
- role: derived-artefact
  path: scripts/generar_documental.py
  change: alta
- role: protocol
  path: docs/estilo_documental.md
  change: docs
- role: derived-artefact
  path: app/index.html
  change: alta
- role: derived-artefact
  path: app/documental_consolidado.html
  change: alta
- role: derived-artefact
  path: app/capitulo_0.5.html
  change: alta
- role: derived-artefact
  path: app/capitulo_1.html
  change: alta
- role: derived-artefact
  path: app/capitulo_2.html
  change: alta
- role: derived-artefact
  path: app/capitulo_3.html
  change: alta
- role: derived-artefact
  path: app/capitulo_4.html
  change: alta
- role: derived-artefact
  path: app/capitulo_5.html
  change: alta
- role: derived-artefact
  path: app/capitulo_6.html
  change: alta
- role: derived-artefact
  path: app/capitulo_7.html
  change: alta
- role: derived-artefact
  path: media/global/video_mapa_conos_1080p60.mp4
  change: alta
- role: derived-artefact
  path: media/segmentos/*/data.json
  change: alta
- role: derived-artefact
  path: media/segmentos/*/*.png
  change: alta
```

## Evidence

Sin nuevos nodos; los conteos y fechas se derivaron del corpus existente.

## Complements

- Añade georreferenciación como capa opcional; no modifica el grafo de adyacencia `R` del modelo.
- Añade `scripts/generar_documental.py` como generador reproducible; el corpus canónico no se edita.

## Invariants

- [x] sin métrica escalar canónica
- [x] cono = polidad `[t0,t1]`
- [x] Teotihuacan apagada en t=700
- [x] species/migration/site/admixture ≠ cono de Estado
- [x] `A^n u` = escenario
- [x] sapiens pan-africano
- [x] OoA = pulsos, no una flecha
- [x] `flat` reconstruido si se tocó el árbol (no se tocó)
- [x] `python docs/referencia_modelos.py` → selftest ok
- [x] `python skills/heartbeat-human-history/scripts/validate_heartbeat.py` → heartbeat ok
- [x] conteos del pulso = `meta` atestado, no memoria del agente

## Counts (solo si tocaste corpus)

```
cronologia n_nodes: 2336
ontologia n_nodos:  2562
sim_meta n_conos:   81
origenes species/sites/migrations/admixture/anclas: 37/41/14/7/9
```

## Pending left for the next agent

- Expandir narrativa de cada capítulo a ~1500 palabras con citas y contexto histórico detallado.
- Generar videos por capítulo y no solo el mapa global.
- Mejorar georreferenciación con polígonos curados por fuentes.
- Sincronizar y comparar `corpus-completo_2026-08-31` contra el repo.

## Notes

- `aion` MCP no pudo generar código por API key inválida; `unified-llm` con `claude-sonnet-4-20250514` no estaba disponible; el script final se redactó localmente.
- Se usó `python3.11` porque `python3.14` fallaba al importar `pyexpat` en este entorno.
- Video renderizado con matplotlib + ffmpeg a 1920x1080 @ 60 fps.
