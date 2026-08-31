# SPEC 05 — Orígenes de la especie y migraciones

## Problema

La cronología política nace *después*. El soporte geográfico de cada
civilización es el resultado de una historia más larga: divergencia
Pan–Homo, radiaciones de Hominina, salidas de África del género *Homo*,
introgresión con arcaicos, y el poblamiento de Sahul / Eurasia / Américas.

Sin esa capa no se puede responder “dónde se origina la historia”.
Con esa capa mal dibujada se pinta a Teotihuacan como si durara
hasta 1500, o a *H. sapiens* como un Estado.

## Qué entra y qué no

| Entra | No entra |
|---|---|
| taxón con FAD/LAD publicado | cono de Estado para una especie |
| yacimiento ancla (lon/lat) | GIS de fronteras modernas |
| pulso migratorio con ventana | una sola flecha “Out of Africa” |
| evento de introgresión datado | raza, esencia, destino |
| technocomplex (Olduvayense…) | “progreso” como eje único |

`kind ∈ {species, site, migration, admixture, technocomplex, climate}`
se indexa en el árbol `humanidad` y en `datos/origenes/`.
La simulación de conos **ignora** estos kind (invariante 9 de `LLM.md`).

## Consenso operativo (2023–2026)

No es un cladograma sagrado. Es el piso que el corpus usa para datar.
Cada nodo lleva `status` y `sources`.

### Filogenia y grado

- Divergencia Pan–Homo: ~7–10 Ma (el corpus abre Hominina en −7 000 000).
- Basales africanos: *Sahelanthropus* (~7.2–6.8 Ma, hominino **debatido**),
  *Orrorin* (~6.1–5.5), *Ardipithecus kadabba* (~5.8–5.2),
  *Ar. ramidus* (~4.5–4.3).
- Australopitecinos generalizados: *anamensis* → *afarensis* →
  *africanus* / *garhi* / *sediba*; *Kenyanthropus* en paralelo.
- Robustos: *Paranthropus aethiopicus*, *boisei*, *robustus* (rama
  colateral, no ancestro de *Homo*).
- Primer *Homo*: Ledi-Geraru ~2.8 Ma (atribución abierta);
  *H. habilis* ~2.3–1.6; *H. rudolfensis* ~2.1–1.8 (separados).
- *H. erectus* s.l. desde ~1.9 Ma en África; Dmanisi ~1.85–1.77;
  Java ~1.8–1.5; China (Zhoukoudian y otros) Pleistoceno medio;
  Ngandong ~0.13–0.11. *H. ergaster* = grado africano temprano.
- *H. antecessor* Atapuerca ~1.2–0.8 Ma.
- *H. heidelbergensis* / *rhodesiensis* ~0.7–0.2 Ma (grado, no especie
  limpia). Sima de los Huesos ~0.43 Ma ya en linaje neandertal.
- *H. naledi* 335–236 ka, Sudáfrica, coexistiendo con sapiens temprano.
- *H. floresiensis* ~190–50 ka (ocupación de Flores mucho antes).
- *H. luzonensis* ~67–50 ka, Callao.
- Neandertales ~400–40 ka; denisovanos ~300–40 ka (genética + pocos fósiles).
- *H. sapiens*: fósiles ~300 ka (Jebel Irhoud; Florisbad ~260; Omo ~230;
  Herto ~160). Modelo **pan-africano**, no un único Edén oriental.

### Dos stems y fusión (genética)

Ragsdale et al., *Nature* 2023; modelos posteriores (Cousins / Hawks 2025):
dos poblaciones africanas se separan ~1.5 Ma y se refundan ~300 ka
(~80 % / ~20 %) para dar el tronco de sapiens actuales. El corpus
guarda esto como nodo `stem-fusion-300ka` (`kind: admixture`,
`precision: debated` en la geografía de los stems, no en el hecho
del mestizaje profundo).

### Salidas de África — varios pulsos, no uno

| id | Qué | Ventana | Destino fósil / genético | Contribución a vivos |
|---|---|---|---|---|
| `ooa-0-tools` | industria en Asia anterior a Dmanisi | ~2.1 Ma (Shangchen) | debatido, sin fósil claro | nula conocida |
| `ooa-i-erectus` | *H. erectus* s.l. | ~1.85–1.5 Ma | Dmanisi, Java, China | nula directa |
| `heidelbergensis-europa` | grado medio a Europa | ~0.7–0.5 Ma | Mauer, Boxgrove, Petralona | vía neandertal |
| `sapiens-misliya` | sapiens en Levante | ~194 ka | Misliya | linaje probablemente extinto |
| `sapiens-skhul-qafzeh` | ocupación levantina | ~130–90 ka | Skhul, Qafzeh | no el tronco no africano actual |
| `sapiens-al-wusta` | Arabia | ~85 ka | Al Wusta | incierta |
| `admixture-nean-250ka` | flujo sapiens → neandertal | 250–200 ka | genomas neandertales | 2.5–3.7 % sapiens en neandertal (Li/Akey 2024) |
| `admixture-nean-120ka` | segundo pulso | 120–100 ka | idem | idem |
| `ooa-ii-exitosa` | dispersión que sí deja descendencia extra-africana | ~60–50 ka | genomas no africanos | casi toda Eurasia / Américas / Oceanía |
| `admixture-nean-45ka` | introgresión compartida por no africanos | 49–45 ka | Ranis / Zlatý kůň 2025 | ~2 % en no africanos |
| `peopling-sahul` | Australia / Nueva Guinea | ~65–50 ka | Mungo, Madjedbebe (debatido 65 vs 50) | papúes / aborígenes |
| `admixture-denisova-sahul` | denisova en ancestros de Sahul | Pleistoceno tardío | genomas papúes | ~3–5 % |
| `peopling-europe-up` | Europa paleolítico superior | ~45 ka | Ranis, Bacho Kiro, Kostenki | reemplazo + restos |
| `peopling-americas` | Beringia → Américas | ~23–14 ka | Anzick, Cooper’s Ferry, debate pre-Clovis | nativas americanas |

Reconciliación fósil vs genoma (Nature 2025, expansión de nicho):
hubo sapiens fuera de África *antes* de 50 ka. Esos pulsos **no**
son el tronco de los no africanos actuales. El pulso ~50 ka coincide
con una ampliación del nicho ecológico africano desde ~70 ka.

### Qué significa “origen de la historia”

En este modelo el origen no es un punto. Es la **intersección**:

```
origen(historia) =
    soporte geográfico de sapiens
  ∩ rutas de los pulsos que sí dejaron descendencia
  ∩ paquetes culturales que sobreviven al Holoceno
```

Las civilizaciones del árbol político se sientan sobre ese soporte.
Por eso `datos/origenes/` es capa 0.5: debajo de las lentes políticas,
encima de la geología.

## Archivos

```
datos/origenes/homininos.json      taxones + grado
datos/origenes/migraciones.json    pulsos y poblamiento
datos/origenes/yacimientos.json    sitios ancla lon/lat
datos/origenes/introgresion.json   admixture datada
```

Cada objeto de esos ficheros se **proyecta** al árbol `humanidad`
con el esquema corto de `nodo.schema.json`. Los campos extra
(`lon`, `lat`, `sources`, `fad_ma`) viven solo en `origenes/`.

## Reglas de proyección

```
def proyectar(origen):
    return {
      "id": origen.id,
      "name": origen.name,
      "name_en": origen.name_en,
      "kind": origen.kind,          # species|site|migration|admixture|...
      "start": origen.start,
      "end": origen.end,
      "precision": origen.precision,
      "level": origen.level,
      "parent": origen.parent,
      "region": "humanidad",        # o región si el sitio es inequívoco
      "notes": origen.notes,
    }
```

Ontología: `lentes = ["cientifico"]` por defecto; una migración añade
`"social"`; un rito funerario paleolítico añade `"religioso"` solo si
la interpretación ritual está argumentada (y se marca `debated`).

## Álgebra con el resto del modelo

- `d_T`, `d_R`, `d_D` valen igual. Un *erectus* en Dmanisi y un
  sapiens en Jebel Irhoud tienen `d_R` grande y `d_T` de cientos
  de miles de años: no son “la misma humanidad” por decreto.
- `join(Ci, Cj, t)` no mezcla una especie con una dinastía.
- Φ(x,t) **no** se calcula con taxones. Si un implementador quiere
  un campo de “presencia hominina”, debe crear un `φ_especie`
  aparte, con otro `α` y sin llamarlo cono de Estado.

## Proyección origenes → árbol (conteo)

`datos/origenes/homininos.json` declara `n: 37`. Eso **no** son 37 especies.

| kind en el catálogo | n | ¿En el árbol? |
|---|---|---|
| `species` | 31 | sí, `kind=species` |
| `period` | 5 (`pan-homo-split`, `basal-hominina`, `australopithecus`, `paranthropus`, `homo-genus`) | sí |
| `site` | 1 (`ledi-geraru`) | sí |

Los 37 ids del catálogo ya estaban proyectados el 2026-08-30. El “faltan 6 taxones” era un error de categoría (37 ítems vs 31 `species`).

Yacimientos 38→41 el 2026-08-31: se añadieron `site-xiahe`, `site-harbin`, `site-shangchen` con `precision: debated` / `status: open`. No resuelven la especie.

## Qué queda abierto (no rellenar con invención)

- Estatus hominino de *Sahelanthropus* y *Graecopithecus*.
- Relación exacta *habilis* / *rudolfensis* / *erectus*.
- Si Shangchen 2.1 Ma es hominino y de qué especie (`site-shangchen`).
- Geografía de los dos stems africanos de Ragsdale/Cousins.
- Fecha alta vs baja de Sahul y de las Américas pre-Clovis.
- Identidad fósil de los denisovanos (Harbin / *H. longi* / Xiahe: nodos `longi`, `site-harbin`, `site-xiahe`).

Esos huecos se modelan con `precision: debated` y `status: open`.
No se resuelven en el JSON.
