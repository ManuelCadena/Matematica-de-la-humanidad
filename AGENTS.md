# AGENTS.md

Instrucciones de proyecto para cualquier agente. Estandar [AGENTS.md](https://agents.md) (AAIF / Linux Foundation). Este archivo es un indice, no una enciclopedia.

## Que es esto

Corpus + modelo matematico de la historia humana como fibrado sobre R x T, realizado como conos datados sobre la Tierra, asentado en una capa de origen de la especie.

Idioma de trabajo: espanol. IDs: kebab-case. Anios: enteros astronomicos.

## Antes de tocar nada

1. LLM.md — invariantes. Romper uno = implementacion invalida.
2. heartbeat_human_history/README.md — como registrar la sesion.
3. heartbeat_human_history/HEARTBEAT.json — pulso actual.
4. Oficio del corpus: skills/heartbeat-human-history/SKILL.md (heartbeat.v1.1).
5. Oficio portable para otros repos: skills/sota-agent-heartbeat/SKILL.md.

## Donde esta cada cosa

| Pregunta | Archivo |
|---|---|
| Como anadir un nodo | LLM.md §6 |
| Lentes | docs/SPEC_01_LENTES.md |
| Fibrado / Allen | docs/SPEC_02_FIBRADO_ALLEN.md |
| Fibras / acoples | docs/SPEC_03_FIBRAS_ACOPLES.md |
| Cono / sabana | docs/SPEC_04_MANDALA_CONO_SIM.md |
| Especie y migraciones | docs/SPEC_05_ORIGENES_MIGRACIONES.md |
| Algoritmos | docs/referencia_modelos.py |
| Schema de nodo | datos/schemas/nodo.schema.json |
| Status del repo | heartbeat_human_history/HEARTBEAT.json |

## Constraints

- Cono = polidad [t0,t1]. Teotihuacan no vive en t=700.
- species|migration|site|admixture|technocomplex no es cono de Estado.
- No hay metrica escalar canonica de cercania historica.
- A^n u se llama scenario, nunca predict.
- Toda sesion que escriba archivos registra heartbeat. Sin log, no cuenta.

## Validar

```
python docs/referencia_modelos.py
python skills/heartbeat-human-history/scripts/validate_heartbeat.py
```
