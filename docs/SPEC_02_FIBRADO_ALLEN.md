# SPEC 02 — Fibrado discreto y álgebra de Allen

## Objeto

```
G = (V, D, E_intra, E_inter, I, σ, φ)
B = R × T
```

- `R` = 16 regiones + `humanidad` (ver `datos/modelo_espacio_tiempo.json` → `regiones`).
- `T = ℤ` años.
- `D` = {politico, historico, religioso, cientifico, cultural, social}.

Un punto de `B` es el par `(r, t)`: “el Nilo en 1258”.

## Mapeo de nodo

```
v  ↦  ( I(v)=[t0,t1],  σ(v)⊆R,  φ(v)⊆D )
```

`σ(v)` se toma de `node.region`. Si `region` es nulo y `arbol` es
religioso/social/cientifico/cultural, tratar como transversal (`humanidad`).

## Grafo de adyacencia de R

Lista canónica (no inventar fronteras):

```
am-north -- meso -- andes
af-west -- maghreb -- eu-west -- eu-east -- iran-steppe -- sasia -- easia -- seasia -- oceania
af-west -- af-nile -- near-east
af-nile -- af-cs -- af-west
af-nile -- maghreb
maghreb -- near-east
eu-west -- near-east
eu-east -- near-east
iran-steppe -- near-east
iran-steppe -- easia
sasia -- seasia
humanidad  (sin aristas; d_R(humanidad, x)=1 para x≠humanidad)
```

## Distancia espacial `d_R`

BFS no ponderado sobre el grafo anterior.

```
d_R(r,r) = 0
d_R(humanidad, x) = 1   si x ≠ humanidad
d_R(r,s) = hops, o 3 si desconectados (no ocurre en el grafo salvo error)
```

## Distancia temporal `d_T`

Intervalos cerrados `A=[a0,a1]`, `B=[b0,b1]`.

```
si A ∩ B ≠ ∅:   d_T = 0
si a1 < b0:     d_T = b0 - a1
si b1 < a0:     d_T = a0 - b1
si algún extremo es None: d_T = None
```

## Distancia dimensional `d_D`

```
d_D(φ,ψ) = 0  si φ ∩ ψ ≠ ∅
         = 1  si no
```

## Producto (lo que se devuelve)

```
dist(u,v) = (d_T(I(u),I(v)), d_R(σ(u),σ(v)), d_D(φ(u),φ(v)))
```

Si el llamador pide un escalar, **exige** pesos explícitos:

```
s = α d_T + β d_R + γ d_D
```

y documenta que `α,β,γ` son una elección, no geometría.

Si `σ` tiene varios elementos, `d_R` = mínimo entre pares.

## Álgebra de Allen (13 relaciones)

Intervalos cerrados en `ℤ`. “Meets” = se tocan en un entero consecutivo
(`a1 + 1 == b0`).

```
def allen(A, B):
    a0,a1 = A; b0,b1 = B
    if None in (a0,a1,b0,b1): return None
    if a1 < b0:
        return "meets" if a1 + 1 == b0 else "precedes"
    if b1 < a0:
        return "met_by" if b1 + 1 == a0 else "preceded_by"
    if a0==b0 and a1==b1: return "equals"
    if a0==b0 and a1 < b1: return "starts"
    if a0==b0 and a1 > b1: return "started_by"
    if a1==b1 and a0 > b0: return "finishes"
    if a1==b1 and a0 < b0: return "finished_by"
    if a0 > b0 and a1 < b1: return "during"
    if a0 < b0 and a1 > b1: return "contains"
    if a0 < b0 < a1 < b1: return "overlaps"
    if b0 < a0 < b1 < a1: return "overlapped_by"
    return "overlaps"
```

Tabla de comprobación (obligatoria):

| A | B | allen |
|---|---|---|
| [0,10] | [20,30] | precedes |
| [0,10] | [11,20] | meets |
| [0,15] | [10,20] | overlaps |
| [0,10] | [0,20] | starts |
| [5,15] | [0,20] | during |
| [10,20] | [0,20] | finishes |
| [0,10] | [0,10] | equals |
| [20,30] | [0,10] | preceded_by |

## Operaciones

```
slice(t) = { v | v.start ≤ t ≤ v.end }

fiber(C, d) = civilizaciones_fibras[C].fibers[d]

join(Ci, Cj, t) = { e ∈ acoples |
    {e.from, e.to} == {Ci, Cj}
    and e.interval.t0 ≤ t ≤ e.interval.t1 }

project_T(v) = I(v)
project_R(v) = σ(v)
project_D(v) = φ(v)
```

## Solape de intervalos

```
def overlaps(A,B):
    if None in A or None in B: return False
    return not (A[1] < B[0] or B[1] < A[0])
```

Usar esta función (no Allen) para pertenencia a fibras.

## Tests

- `allen([0,10],[11,20]) == "meets"`
- `d_R("af-nile","near-east") == 1`
- `d_R("andes","iran-steppe") >= 2`
- `slice(800)` no incluye un nodo con `end=799`
- `dist` nunca devuelve un float único si no se pasaron pesos
