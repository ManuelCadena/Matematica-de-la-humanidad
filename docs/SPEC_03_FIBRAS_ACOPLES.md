# SPEC 03 — Civilización como sección y acoples

## Civilización

No es un nodo. Es el par

```
C = (W_C, F_C)
W_C = σ_C × [tmin, tmax] ⊂ R × T
F_C(d) = { v ∈ V | σ(v)∩σ_C ≠ ∅, I(v) overlaps [tmin,tmax], d ∈ φ(v) }
```

Esquema (`civilizaciones_fibras.json` → `civilizaciones[id]`):

```
Civilizacion {
  id: string
  name: string
  support: { regions: string[], t0: int, t1: int }
  notes: string
  n_nodes: int
  n_por_dim: { [d in D]: int }
  fibers: { [d in D]: string[] }   # ids de nodos
}
```

`indice_nodo_a_civilizaciones[nid] = [cid, ...]`
Si la lista tiene longitud > 1, `nid` es un **puerto**.

## Algoritmo de asignación (reconstruir fibras)

Entrada: nodos de la ontología + registro de civilizaciones (support).
Salida: `fibers` y el índice inverso.

```
def assign_to_civs(nodes, civs, region_tags):
    inverted = {}
    for C in civs:
        support = (C.t0, C.t1)
        regs = set(C.regions)
        fibers = {d: [] for d in D}
        for nid, n in nodes.items():
            I = (n.start, n.end)
            if I[0] is None or I[1] is None: continue
            if not overlaps(I, support): continue
            r = n.region
            if r and r not in regs and r != "humanidad":
                continue
            if r == "humanidad" or n.arbol in TRANSVERSALES:
                if not (set(n.tags) & region_tags.get(C.id, set())):
                    continue
            dims = assign_dims(n)          # SPEC 01
            for d in dims:
                if d in fibers:
                    fibers[d].append(nid)
            inverted.setdefault(nid, []).append(C.id)
        C.fibers = fibers
    return inverted
```

`region_tags` ejemplo: `egypt → {egipto}`, `india → {india}`,
`islamicate → {abrahámico}`, `mesoamerica → {meso,maya,mexica}`.

Nodos religiosos transversales **no** se clavan a todas las civilizaciones
solo por solape temporal. Sin tag de área, se descartan.

## Acoples

```
Acople {
  from: string          # id de civilizacion
  to: string
  type: enum            # ver 00_LEEME
  via: string | null    # id de nodo o etiqueta
  interval: {t0:int, t1:int}
  dims: string[]        # subset de D
  symmetric: bool
}
```

Semántica: en `I_e`, las secciones `from` y `to` se tocan en las lentes `dims`
a través de `via`.

```
join(Ci, Cj, t):
    out = []
    for e in acoples:
        ends = {e.from, e.to}
        if ends != {Ci, Cj} and not (e.symmetric and ends == {Cj, Ci}):
            if Ci not in ends or Cj not in ends: continue
        if e.interval.t0 <= t <= e.interval.t1:
            out.append(e)
    return out
```

Si `symmetric=false`, conservar dirección (`conquest`: from conquista a to).

## Tipos — contrato

| tipo | dirigido | dims típicas |
|---|---|---|
| war, conquest | sí | historico, politico |
| treaty | sí/simétrico puntual | historico |
| trade, exchange | no | social, politico |
| translation, diffusion | no | religioso, cultural |
| conversion, diaspora | sí | religioso, social |
| succession | sí | politico, cultural |
| fusion | no | cultural, politico |
| contact, expansion | sí | historico, social |
| coexist | no | cultural |

## Tests

- Alejandría (si existe como nodo) puede listar ≥2 civilizaciones.
- `join("sahel","islamicate",1324)` incluye el hajj / conversión.
- `join("egypt","levante",-1274)` incluye war Qadesh.
- Un nodo con región `andes` no entra en `egypt.fibers`.
- `F_C(d)` puede ser vacío; no rellenar con nodos de otra lente.
