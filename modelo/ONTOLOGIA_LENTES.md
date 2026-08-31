# Ontología v7 — lentes y árbol religioso

Archivos:
- `historia_ontologia.json` — capa de análisis (2403 nodos, 34 edges)
- `ontologia_nodos.jsonl` — una ficha por línea
- `cronologia_mundial_arbol.json` — capa política + humanidad (sin borrar)

## Por qué cambió la estructura

Un solo eje temporal obliga a elegir *una* visión. El hajj de 1324 es a la vez:
- **histórico**: un rey viaja y altera precios en El Cairo;
- **religioso**: un pilar del islam cumplido por un soberano;
- **social**: redistribución de oro y prestigio saheliano;
- **cultural**: entra en el *Atlas catalán*;
- **científico**: las cifras de al-ʿUmarī se critican.

La ontología guarda el hecho una vez y lo **corta por lente**.

## Las cinco lentes

| Lente | Pregunta | No hace |
|---|---|---|
| histórico | ¿Qué ocurrió según fuente pública? | No decide si una revelación es verdadera |
| científico | ¿Qué data el método (C-14, ADN, filología)? | No sustituye el sentido émico |
| religioso | ¿Qué afirma la comunidad sobre lo sagrado? | No se reduce a 'mito vs hecho' |
| cultural | ¿Qué formas (texto, rito, estilo) se transmiten? | No es ornamento del Estado |
| social | ¿Quién organiza a quién? | No es la lista de reyes |

`precision: emic` = fecha de fe (p. ej. primera revelación, 610).  
`precision: debated` = disputa académica.  
`tag: analitico` = etiqueta de investigador (animismo, era axial, secularización), no una iglesia.

## Árbol religioso (lo que faltaba)

Familias, no una lista plana:

1. Práctica paleolítica (categoría científica)
2. Cosmologías indígenas (Dreaming, andina, mesoamericana, ATR, Oceanía) + diásporas (Candomblé, Vodou)
3. Antiguo Oriente (Sumer, Egipto, Ugarit)
4. Iranias (Zoroastro, Mani, mandeos, yazidíes)
5. Índicas: Veda ≠ śramaṇa ≠ hinduismo; vehículos budistas; darsanas; sijismo
6. Sínicas: Ru / Dao eclesiástico / Fo / minjian
7. Corea–Japón: muísmo, shintō (incluido el de Estado), escuelas japonesas
8. Abrahámicas con cismas reales: yahvismo → judaísmos; concilios y ramas cristianas; fitna, madhhabs, ṭuruq
9. Modernas: deísmo, secularización (tesis), NRM

La era axial está marcada como **categoría comparativa**, no como hecho.

Conteos de lente sobre el corpus unido:
{'historico': 1933, 'cientifico': 92, 'cultural': 222, 'social': 140, 'religioso': 222}

## Cómo indexar

```python
import json
O = json.load(open("historia_ontologia.json"))

# todo lo religioso en el siglo VII
ids = set(O["indices"]["por_lente"]["religioso"]) & set(O["indices"]["por_siglo"].get("600s", []))
for i in ids:
    n = O["nodos"][i]
    print(n["start"], n["kind"], n["name"])

# cismas
print(O["indices"]["por_tag"].get("cisma"))

# qué interpreta qué
for e in O["edges"]:
    if e["rel"] in ("cisma_de", "cisma_en", "rama_de"):
        print(e)
```

## Cómo NO usarlo

- No mezclar `wahy` (émico) con `hijra-622` (histórico) como si fueran el mismo tipo de verdad.
- No llamar 'Edad Media' a Song o a Mali.
- No fundir Ifá, Vodún y minkisi en 'animismo africano'.
- No tratar el confucianismo como iglesia.

## Qué queda para v8

Anuario teológico año a año, cada fatwa o cada sínodo local. Eso es monografía, no ontología mundial. Esta v7 es la **rejilla** para ese análisis.
