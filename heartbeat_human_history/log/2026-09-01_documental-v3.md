# Sesión `2026-09-01-documental-v3`

```
id:          2026-09-01-documental-v3
agent:       Devin v1.0
started:     2026-09-01T06:22:10Z
ended:       2026-09-01T06:40:19Z
activity:    docs
protocol:    heartbeat.v1.1
```

## Intent

Corregir las coordenadas geográficas de los conos usando el corpus `Analizador_Humanidad` del `Grok content`, extender el video a más de 15 segundos, evitar gráficos de acoples vacíos y generar siete figuras del modelo matemático perfectamente explicadas.

## Chain

```
prev_session_id: 2026-09-01-documental-v2
prev_sha256:     2f49ae6ec1063c54e631ffc7ecd445c164afc7cbb9768894f64ea5d1584d45ca
```

## Used

- `datos/analizador_conos.json` extraído de `Grok content/Analizador_Humanidad (2).html`.
- `datos/centros_conos.json` con centroides reales por fibra.
- `datos/civilizaciones_fibras.json`, `datos/ontologia_nodos.jsonl`, `datos/acoples_multicapa.json`.
- `docs/referencia_modelos.py`.

## Generated

- `datos/centros_conos.json` (georreferenciación canónica 22 fibras).
- Nuevos mapas `media/segmentos/*/mapa_conos_*.png` con centroides correctos sobre Cartopy.
- Nuevos gráficos de acoples `media/segmentos/*/acoples_*.png` (ya no vacíos).
- Video extendido `media/global/video_mapa_conos_1080p60.mp4` 1920×1080 @ 60fps, 1006 frames, ~16.7 s.
- `media/modelos/*.png` siete figuras del modelo: envelope, cono, distancia, A_t, W₁, Allen, fibrado.
- `app/modelos_matematicos.html` con explicación de cada figura.
- `app/documental_consolidado.html` e `indice_documental.html` con links a modelos y video actualizado.

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

- AION Brain sigue sin estar disponible por API key; ejecución local.
- Los gráficos de acoples quedan poblados en capítulos 0-7.
- Algunos centroides (`am-woodland`, `oceania-civ`) son aproximaciones por ausencia de cono específico en el corpus analizador.
