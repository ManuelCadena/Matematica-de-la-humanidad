# Contrato para modelos de lenguaje

Este archivo es la **puerta de máquina** del repositorio. Un LLM que llegue
en frío debe leerlo antes de tocar un JSON o de “mejorar” el modelo.

Idioma de trabajo: español. Identificadores: ASCII `kebab-case`.
Años: enteros astronómicos (`-44` = 44 a.C.; el modelo **usa** el año 0).

---

## 1. Orden de lectura (obligatorio)

1. `README.md` — tesis de una página y mapa de carpetas.
2. Este archivo (`LLM.md`) — invariantes y cómo extender.
3. `docs/00_LEEME_IMPLEMENTADOR.md` — contratos numéricos.
4. `docs/SPEC_01_LENTES.md` … `docs/SPEC_05_ORIGENES_MIGRACIONES.md`.
5. `modelo/CARTA.md` y `modelo/proyecto.json`.
6. `datos/README.md` y el schema en `datos/schemas/nodo.schema.json`.
7. Recién entonces: JSON. No inferir el esquema desde un nodo suelto.

Validación mínima:

```
python docs/referencia_modelos.py
# debe imprimir: selftest ok
```

---

## 2. Qué es este proyecto (y qué no)

Es un **fibrado multicapa** sobre `B = R × T`, realizado sobre la Tierra
como campos-mandala / conos **datados**. No es una ley de la historia.
No profetiza. No aplasta lentes. No dibuja un Estado eterno.

Cuatro capas, en este orden:

```
0  Lentes          un hecho, varias lecturas
1  Fibrado         B = R × T,  D = 6,  C = (W_C, F_C)
2  Campo-mandala   φ_{C,d}(x,t) sobre M (lon/lat)
3  Cono / sábana   H = ||s||, R = H tan α, Φ = Σ z, γ_c = {Φ = c}
```

Capa transversal **especie / migración** (SPEC_05): explica *dónde nace*
el soporte geográfico de la historia. **No es un cono de Estado.**

---

## 3. Invariantes (romper uno = implementación inválida)

1. Un nodo puede tener varias `lentes`. No forzar una sola narración.
2. Una civilización no es un nodo: es el par `C = (W_C, F_C)`.
3. Un nodo puede pertenecer a varias civilizaciones (puerto).
4. No existe métrica escalar canónica de cercanía. El objeto es
   `(d_T, d_R, d_D)`. Si el llamador quiere un escalar, debe pasar
   `α, β, γ` explícitos.
5. Un cono geográfico es una **polidad datada** `[t0, t1]`.
   `amp(t) = 0` si `t ∉ [t0, t1]` (rampa de 40 años en los bordes).
6. Teotihuacan no está activa en t=700. Tenochtitlan no lo está en t=100.
   San Lorenzo −1500 a −900. Mesoamérica no es un cono de −2000 a 1697.
7. `A_t` se estima con acoples tipados. No inventar pesos de conquista.
8. `u(t+Δ) = A^Δ u(t)` es **escenario**. El API se llama `scenario`,
   nunca `predict`.
9. `kind ∈ {species, migration, site, admixture, technocomplex}`
   **no produce cono político**. Se indexa, se corta por lente
   científica/social, no se pinta como imperio.
10. Fechas FAD/LAD de homininos son convenciones con incertidumbre de
    10⁴–10⁵ años. `precision: debated` cuando el estatus de hominino
    o la ruta está en disputa (Sahelanthropus, Shangchen 2.1 Ma, etc.).

---

## 4. Mapa de archivos

| Ruta | Rol | Quién lo escribe |
|---|---|---|
| `docs/SPEC_0*.md` | especificación implementable | humano / LLM con review |
| `docs/referencia_modelos.py` | algoritmos + `selftest()` | código |
| `modelo/*.md` | carta matemática | humano |
| `modelo/proyecto.json` | manifiesto máquina de capas | máquina |
| `datos/cronologia_mundial_arbol.json` | capa política + humanidad | corpus |
| `datos/historia_ontologia.json` | lentes, religión, índices | corpus |
| `datos/civilizaciones_fibras.json` | 22 secciones | corpus |
| `datos/acoples_multicapa.json` | puertos tipados | corpus |
| `datos/origenes/*.json` | especie, migración, yacimiento, ADN | corpus SPEC_05 |
| `datos/schemas/*.json` | JSON Schema draft-07 | contrato |
| `app/index.html` | analizador Φ(x,t) | UI |

Los JSON canónicos locales de trabajo también viven en la raíz de
`artifacts/` del proyecto. Si hay divergencia, gana el archivo con
`meta.fecha` más reciente y se documenta en `datos/README.md`.

---

## 5. Esquema mínimo de nodo

Todo nodo del árbol o de la ontología carga al menos:

```
id          kebab-case ASCII, estable
name        español
name_en     inglés o nombre técnico
kind        ver enum en datos/schemas/nodo.schema.json
start, end  int, start ≤ end, inclusive
precision   year | decade | century | millenium | emic | debated
level       int ≥ 0
parent      id o null
region      una de R, o "humanidad"
notes       hechos + incertidumbre, no ensayo
```

La ontología añade `lentes[]`, `tags[]`, `arbol`.
Los ficheros de `datos/origenes/` añaden `lon`, `lat`, `sources[]`,
`status`, `fad_ma`, `lad_ma` cuando aplica.

---

## 6. Cómo añadir un nodo sin romper el corpus

1. Elegir `id` que no exista en `cronologia_mundial_arbol.json` → `flat`
   ni en `historia_ontologia.json` → `nodos`.
2. Colocar el nodo como hijo del padre correcto en `trees[]`.
3. Reconstruir `flat` recorriendo el árbol (el plano no se edita a mano).
4. Copiar el nodo a la ontología con `lentes` y `arbol`.
5. Reconstruir `indices.por_lente`, `por_kind`, `por_tag`, `por_siglo`,
   `por_arbol`, `por_region`.
6. Si es polidad y se quiere cono: añadir entrada en `sim_meta.json`
   con `lon`, `lat`, `[t0,t1]`, `peak`. Nunca reutilizar un cono
   de “civilización eterna”.
7. Si es especie / migración / yacimiento / admixture: va a
   `datos/origenes/` **y** al árbol `humanidad`. No va a `sim_meta`
   como cono de Estado.
8. Correr `python docs/referencia_modelos.py`.
9. Anotar la fuente en `notes` o `sources[]`. Sin fuente no entra.

No renombrar un `id` ya citado por fibras o acoples. Si hay choque,
crear `id` nuevo y dejar el viejo como alias en `notes`.

---

## 7. Cómo “mejorar” el modelo (lo permitido)

Un LLM **puede**:

- Añadir ramificaciones locales con fuente handbook / paper.
- Corregir un `[t0,t1]` si el JSON de origenes o un paper posterior
  lo exige, y dejar rastro en `notes`.
- Añadir un acople tipado del enum cerrado.
- Implementar un `K` o una norma `||·||_p` alternativa, declarada.
- Extender `datos/origenes/` con un yacimiento o un pulso migratorio.

Un LLM **no puede**:

- Introducir métrica escalar canónica.
- Encender un cono fuera de `[t0,t1]`.
- Fundir las cinco lentes en “lo que realmente pasó”.
- Llamar predicción a `A^n u`.
- Inventar una dinastía, una especie o una ruta sin cita.
- Tratar *Out of Africa* como un único evento.
- Tratar *Homo sapiens* como nacido en un solo jardín de Edén
  (el consenso vigente es pan-africano + fusión de stems; SPEC_05).

---

## 8. Preguntas ya computables

```
slice(t)              nodos con start ≤ t ≤ end
fiber(C, d)           F_C(d)
join(Ci, Cj, t)       puertos simultáneos
allen(I, J)           13 relaciones
Phi(x, t)             sábana de conos vivos
especie_en(t)         taxones con kind=species activos
rutas_en(t)           kind=migration activos
introgresion_en(t)    kind=admixture activos
```

---

## 9. Versión de este contrato

`LLM.md` v1.0 — 2026-08-30. Cualquier cambio de invariante incrementa
el entero y se menciona en el commit.
