# Sesión `2026-09-01-documental-v2`

```
id:          2026-09-01-documental-v2
agent:       Devin v1.0
started:     2026-09-01T05:58:05Z
ended:       2026-09-01T06:19:53Z
activity:    docs
protocol:    heartbeat.v1.1
```

## Intent

Reescribir el documental para dejar de ser un listado de viñetas y convertirlo en una narrativa histórica documental con arco de tres actos, gancho y reflexión final, siguiendo la investigación de Consensus y Perplexity. Mejorar la georreferenciación con mapas de Cartopy y un video 1080p60 con conos simultáneos sobre un mapa real del mundo.

## Chain

```
prev_session_id: 2026-09-01-documental-consolidado
prev_sha256:     95d7ca4624bfd2de5bc01bf41616e523c5e9fda2f1b5a2f8cb050a6da757ac4c
```

## Used

- `datos/civilizaciones_fibras.json`, `datos/ontologia_nodos.jsonl`, `datos/acoples_multicapa.json`, `datos/regiones_geograficas.json`.
- `docs/referencia_modelos.py`.
- `media/segmentos/*/data.json` generados en la sesión anterior.

## Generated

- `datos/narrativas_capitulos.json` (~1500 palabras por capítulo, gancho, tesis, tres actos, reflexión).
- Nuevas figuras `media/segmentos/*/mapa_conos_*.png` con Cartopy (costas, fronteras, conos georreferenciados).
- Nuevo video `media/global/video_mapa_conos_1080p60.mp4` 1920×1080 @ 60fps, 4.18s, con conos simultáneos sobre mapa real.
- `app/documental_consolidado.html` y `app/capitulo_*.html` con narrativas integradas.
- `scripts/generar_documental.py` v2 con Cartopy y carga de narrativas.

## Invariants

- [x] sin métrica escalar canónica
- [x] cono = polidad `[t0,t1]`
- [x] Teotihuacan apagada en t=700
- [x] species/migration/site/admixture ≠ cono de Estado
- [x] `A^n u` = escenario
- [x] sapiens pan-africano
- [x] OoA = pulsos, no una flecha
- [x] `python docs/referencia_modelos.py` → selftest ok
- [x] `python skills/heartbeat-human-history/scripts/validate_heartbeat.py` → heartbeat ok

## Counts

Cronología n_nodes: 2336, ontología n_nodos: 2562, sim_meta n_conos: 81, orígenes 37/41/14/7/9.

## Notes

- Investigación con Consensus y Perplexity confirmó estructura de tres actos, geocodificación EPSG:4326, proyección fija y conos simultáneos anclados.
- AION Brain no pudo usarse por API key inválida; todo se generó localmente.
- El video es una prueba de concepto de ~4s; una versión de 3-5 min requeriría ~10k frames y render por lotes, pendiente.
