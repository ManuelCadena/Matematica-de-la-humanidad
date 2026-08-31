# Geometría de la historia — modelo R × T × D

## El problema

Los árboles (político, religioso, científico, cultural, social) no son mundos
separados. Son **capas de un mismo espacio-tiempo**. Una civilización es una
*sección* de ese fibrado: avanza en el tiempo, ocupa regiones, y en cada punto
tiene fibras distintas que pueden acoplarse a las de otra civilización.

## Estructura

```
B = R × T
D = {politico, historico, religioso, cientifico, cultural, social}
v  ↦ (I(v), σ(v), φ(v))     intervalo, regiones, dimensiones
C  = (W_C, F_C)              worldline + fibras
e  = (C_i, C_j, tipo, vía, I_e, D_e)
```

Relación temporal: **álgebra de intervalos de Allen** (13 relaciones:
`precedes`, `meets`, `overlaps`, `during`, `equals`, …).

## Distancia (importante)

No hay una métrica escalar canónica de “cercanía histórica”.

| Coordenada | Distancia |
|---|---|
| tiempo `d_T` | 0 si los intervalos se cortan; si no, el hueco en años |
| espacio `d_R` | saltos en el grafo de adyacencia regional |
| dimensión `d_D` | 0 si comparten lente; 1 si no |

Una suma `α d_T + β d_R + γ d_D` **elige valores**. El objeto honesto es el
vector `(d_T, d_R, d_D)`.

## Operaciones

```python
import json
C = json.load(open("civilizaciones_fibras.json"))["civilizaciones"]
E = json.load(open("acoples_multicapa.json"))["acoples"]

# fibra religiosa de Egipto
C["egypt"]["fibers"]["religioso"]

# qué conecta el Sahel, y en qué dimensión
[e for e in E if "sahel" in (e["from"], e["to"])]

# un nodo en varias civilizaciones (puerto)
idx = json.load(open("civilizaciones_fibras.json"))["indice_nodo_a_civilizaciones"]
```

## Archivos

- `modelo_espacio_tiempo.json` — notación, adyacencia, operaciones
- `civilizaciones_fibras.json` — 22 secciones con fibras reales
- `acoples_multicapa.json` — 39 puertos tipados
- `historia_ontologia.json` — nodos y lentes (capa semántica)
- `cronologia_mundial_arbol.json` — capa política

Conteos de nodos asignados a cada sección:

- `islamicate`: 509 nodos
- `atlantic-mod`: 398 nodos
- `rome`: 367 nodos
- `iran`: 235 nodos
- `china`: 209 nodos
- `korea-civ`: 202 nodos
- `japan-civ`: 198 nodos
- `india`: 192 nodos
- `latin-west`: 190 nodos
- `mesoamerica`: 149 nodos
- `hellas`: 136 nodos
- `sahel`: 134 nodos
- `seasia-civ`: 119 nodos
- `steppe`: 118 nodos
- `levante`: 115 nodos
- `andes-civ`: 115 nodos
- `egypt`: 110 nodos
- `mesopotamia`: 103 nodos
- `aksum-et`: 89 nodos
- `kush-nubia`: 88 nodos
- `am-woodland`: 76 nodos
- `oceania-civ`: 54 nodos

Un nodo puede vivir en **varias** civilizaciones (p. ej. Alejandría: Egipto × Helade × Roma).
Eso no es ruido: es la definición de puerto.

## Qué no es este modelo

No es un GIS. No es una física. Las regiones son categorías historiográficas,
no polígonos. El tiempo es entero (año), no continuo. La utilidad es
**computar cortes y acoplamientos** sin aplastar las lentes.
