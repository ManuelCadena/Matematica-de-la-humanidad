# SPEC 01 — Lentes (ontología de visiones)

## Problema

Un solo eje temporal obliga a elegir *una* verdad. El hajj de 1324 es a la
vez hecho público, rito, redistribución, motivo pictórico y cifra criticable.
La ontología guarda el hecho **una vez** y lo corta por lente.

## Conjuntos

```
L = {historico, cientifico, religioso, cultural, social}
```

En el fibrado aparece además `politico` (forma de autoridad). Unión:

```
D = L ∪ {politico}
```

| Lente | Pregunta | Prohibición |
|---|---|---|
| historico | ¿Qué ocurrió según fuente pública? | No decide si una revelación es verdadera |
| cientifico | ¿Qué data C-14, ADN, filología? | No sustituye el sentido émico |
| religioso | ¿Qué afirma la comunidad sobre lo sagrado? | No reducir a mito vs hecho |
| cultural | ¿Qué formas se transmiten? | No es ornamento del Estado |
| social | ¿Quién organiza a quién? | No es la lista de reyes |
| politico | ¿Qué polidad / dinastía / imperio? | No absorbe las otras lentes |

## Esquema de nodo (`historia_ontologia.json` → `nodos[id]`)

```
Nodo {
  id: string
  name: string
  name_en: string
  kind: string
  start: int          # t0, inclusive
  end: int            # t1, inclusive
  precision: string   # year | decade | century | millenium | emic | debated
  level: int
  parent: string | null
  region: string | null
  notes: string
  lentes: string[]    # subset of L
  tags: string[]
  arbol: string
}
```

`precision: emic` = fecha de fe (p. ej. primera revelación 610).
`precision: debated` = disputa académica.
`tag: analitico` = etiqueta de investigador, no una iglesia.

## Esquema de arista ontológica

```
Edge {
  rel: string     # cisma_de | cisma_en | rama_de | interpreta | ...
  from: string    # id
  to: string
}
```

## Índices obligatorios

```
indices.por_lente[lente] -> [id]
indices.por_siglo["600s"] -> [id]   # cubo start<=699 y end>=600
indices.por_tag[tag] -> [id]
indices.por_arbol[arbol] -> [id]
```

Siglo `k00s` contiene nodos con `start <= k+99` y `end >= k`.
Para negativos: siglo `-600s` = años −600 a −501.

## Algoritmo: asignar lentes a un nodo político

Entrada: nodo del árbol cronológico (sin campo `lentes`).
Salida: `lentes` y dimensión política.

```
KIND_DIM = {
  polity,empire,dynasty,nation,colony,city-state,
  khanate,caliphate,sultanate,confederation,civilization -> politico
  war,treaty,event -> historico
  religion,denomination,canon,council,rite,cosmology,order -> religioso
  species,climate,invention,pandemic -> cientifico
  culture,text,school,site -> cultural
  person -> historico
  migration -> social
}

def assign_dims(node):
    dims = set(node.get("lentes") or [])
    k = node.get("kind")
    if k in KIND_DIM:
        dims.add(KIND_DIM[k])
    if not dims:
        dims.add("historico")
    return sorted(dims)
```

## Consulta canónica

“Todo lo religioso activo en el siglo VII”:

```
ids = set(indices["por_lente"]["religioso"]) & set(indices["por_siglo"]["600s"])
```

## Tests

- Un nodo con `lentes=["historico","religioso"]` no se parte en dos ids.
- `precision=="emic"` no se usa como ancla de `slice` diplomático sin aviso.
- No fusionar Ifá, Vodún y minkisi en un solo nodo “animismo”.
