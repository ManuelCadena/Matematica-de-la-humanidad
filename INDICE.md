# Modelo Matemático de la Humanidad

Proyecto unificado. Sesión integrada: 30 agosto 2026.
Los datos canónicos viven en `/home/workdir/artifacts/` (raíz). Esta carpeta es el **índice y la carta** del modelo.

## Tesis

La historia humana no es un árbol ni un mapa de losas. Es un **fibrado multicapa** sobre el espacio-tiempo, realizado sobre la Tierra como **campos-mandala** (conos que se encienden y se apagan con las fechas del archivo).

## Capas

Puerta de máquina para otro LLM: `LLM.md`. Spec de orígenes: `docs/SPEC_05_ORIGENES_MIGRACIONES.md`.

```
0    Lentes          un hecho, cinco lecturas (no se aplastan)
0.5  Orígenes        especie, pulso OoA, yacimiento, introgresión
1    Fibrado         B = R × T,  D = 6 dimensiones,  C = (W_C, F_C)
2    Campo-mandala   φ_{C,d}(x,t) sobre la superficie terrestre
3    Cono / sábana   H = ||s||,  R = H tan α,  Φ = Σ z,  γ_c = {Φ = c}
```

Regla de la simulación (corrección 2026-08-30): un cono es una **polidad datada** `[t0, t1]` del JSON, no una civilización eterna. Teotihuacan −100–650; Tula 900–1150; Tenochtitlan 1325–1521. `amp = 0` fuera de la ventana.

Lo que el modelo prohíbe: una métrica escalar canónica de “cercanía histórica”; una frontera westfaliana donde hay mandala; un cono que sobrevive a sus propias fechas; una proyección `A^Δ u` vendida como destino.

## Carta matemática (esta carpeta)

| Archivo | Capa |
|---|---|
| `ONTOLOGIA_LENTES.md` | 0 |
| `MODELO_MATEMATICO.md` | 1 (formal) |
| `GEOMETRIA_HISTORIA.md` | 1 (operaciones) |
| `MODELO_MANDALA_CAMPOS.md` | 2 |
| `MODELO_CONO_TOPOGRAFICO.md` | 3 |
| `CARTA.md` | las cuatro capas en un solo texto |
| `proyecto.json` | manifiesto máquina |

## Datos (raíz de artifacts)

| Archivo | Rol |
|---|---|
| `cronologia_mundial_arbol.json` | capa política + humanidad (2296 nodos, v6.3.0-gaps) |
| `cronologia_mundial_flat.jsonl` | mismo árbol, plano |
| `historia_ontologia.json` | lentes + religión + orígenes (2522 nodos, v7.2.0-gaps) |
| `ontologia_nodos.jsonl` | fichas planas |
| `civilizaciones_fibras.json` | 22 secciones / fibras |
| `acoples_multicapa.json` | 39 puertos tipados |
| `modelo_espacio_tiempo.json` | notación, adyacencia R, Allen |
| `dimensiones_por_civilizacion.json` | dimensiones constitutivas por campo |
| `conos_influencia.json` | parámetros ilustrativos de época (v. anterior) |
| `sim_meta.json` | 81 conos datados, años −4000–2026 |
| `CRONOLOGIA_MUNDIAL_FUENTE_DEL_CHART.md` | investigación previa al gráfico |

## Figuras y películas (raíz)

| Archivo | Qué es |
|---|---|
| `TIMELINE_MUNDIAL_SIMULTANEIDAD.svg/.png` | cronología en columnas |
| `geometria_fibrado_3d.png` | fibrado T × C × D |
| `sabana_conos_3d.png` | relieve de conos (tres cortes) |
| `sabana_curvas_nivel.png` | isobaras |
| `video_mapa_topografico.mp4` | dinámica 0–1500 sobre mapa real (fuente de verdad) |
| `video_sabana_3d.mp4` | mismo Φ como relieve |
| `video_cgi_globo_conos.mp4` | CGI ilustrativo (no respeta fechas) |

## Aplicación de análisis

`app/index.html` (copia en raíz: `Analizador_Humanidad.html`).
Φ se evalúa celda a celda. Slider 0–1500. Carta: `MODELO_EVOLUCION_DIMENSIONAL.md`.

## Especificaciones para reimplementar (otro LLM)

Carpeta `docs/`. Empezar por `docs/00_LEEME_IMPLEMENTADOR.md`.

| Spec | Modelo |
|---|---|
| `docs/SPEC_01_LENTES.md` | ontología de visiones |
| `docs/SPEC_02_FIBRADO_ALLEN.md` | R×T, distancias, Allen |
| `docs/SPEC_03_FIBRAS_ACOPLES.md` | sección C=(W,F) y puertos |
| `docs/SPEC_04_MANDALA_CONO_SIM.md` | campo, cono, sábana, simulación datada |
| `docs/referencia_modelos.py` | algoritmos + `selftest()` |

## Cómo continuar en otra sesión

1. Leer `CARTA.md`, `proyecto.json` y `docs/00_LEEME_IMPLEMENTADOR.md`.
2. No reintroducir un cono eterno de “Mesoamérica” o “Andes”.
3. Cualquier cono nuevo nace de un `id` con `start`/`end` en `cronologia_mundial_arbol.json`.
4. Preguntas típicas ya computables: `slice(t)`, `fiber(C,d)`, `join(Ci,Cj,t)`, Φ(x,t) en lon/lat.
5. Correr `python docs/referencia_modelos.py` (debe imprimir `selftest ok`).
