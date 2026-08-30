# AGENTS.md

Instrucciones de proyecto para cualquier agente. Estándar [AGENTS.md](https://agents.md) (AAIF / Linux Foundation). Este archivo es un **índice**, no una enciclopedia.

## Qué es esto

Corpus + modelo matemático de la historia humana como fibrado sobre `R × T`, realizado como conos datados sobre la Tierra, asentado en una capa de origen de la especie.

Idioma de trabajo: español. IDs: `kebab-case`. Años: enteros astronómicos.

## Antes de tocar nada

1. `LLM.md` — invariantes. Romper uno = implementación inválida.
2. `heartbeat_human_history/README.md` — cómo registrar la sesión.
3. `heartbeat_human_history/HEARTBEAT.json` — pulso actual (status, conteos, pending).
4. Si vas a cambiar el corpus, el oficio está en `skills/heartbeat-human-history/SKILL.md`.

## Dónde está cada cosa

| Pregunta | Archivo |
|---|---|
| Cómo añadir un nodo | `LLM.md` §6 |
| Lentes | `docs/SPEC_01_LENTES.md` |
| Fibrado / Allen | `docs/SPEC_02_FIBRADO_ALLEN.md` |
| Fibras / acoples | `docs/SPEC_03_FIBRAS_ACOPLES.md` |
| Cono / sábana | `docs/SPEC_04_MANDALA_CONO_SIM.md` |
| Especie y migraciones | `docs/SPEC_05_ORIGENES_MIGRACIONES.md` |
| Algoritmos | `docs/referencia_modelos.py` |
| Schema de nodo | `datos/schemas/nodo.schema.json` |
| Status del repo | `heartbeat_human_history/HEARTBEAT.json` |

## Constraints (las que caben aquí)

- Cono = polidad `[t0,t1]`. Teotihuacan no vive en t=700.
- `species|migration|site|admixture|technocomplex` no es cono de Estado.
- No hay métrica escalar canónica de cercanía histórica.
- `A^n u` se llama `scenario`, nunca `predict`.
- Toda sesión que escriba archivos **registra heartbeat**. Sin log, no cuenta.

## Validar

```
python docs/referencia_modelos.py
python skills/heartbeat-human-history/scripts/validate_heartbeat.py
```

## Commits

Mensaje corto, en español o inglés. No reescribir historia del log de sesiones.
