# Fuentes

El corpus no cita cada nodo con un DOI. Esta lista es el **piso
académico** que un implementador debe conocer antes de “corregir”
una fecha. Las fechas del JSON son convenciones de handbook, no
mediciones nuevas.

## Periodización y handbooks

- UNESCO *General History of Africa*.
- *Cambridge World History*; *Cambridge History of China / Islam / Southeast Asia*.
- *Oxford Handbook of World History* (periodización).
- Xia-Shang-Zhou Chronology Project (China).
- Cronología media mesopotámica (Hammurabi 1792–1750 a.C.).
- Willey & Phillips 1958; Rowe–Lanning / Lumbreras (Andes); INAH / Coe (Mesoamérica).
- UsefulCharts / ChartOrigin: solo forma visual previa, no autoridad de fechas.

## Paleoantropología y migraciones (SPEC_05)

- Wood & Boyle 2016/2019, *Hominin taxic diversity* (FAD/LAD conservadores).
- Institute of Human Origins, timeline ASU (grados 7 Ma → presente).
- Hublin et al. 2017, Jebel Irhoud ~300 ka (*Nature*).
- Ragsdale et al. 2023, *Nature*: sapiens como mosaico de dos stems africanos.
- Cousins et al. 2025 / Hawks 2025: fusión ~80/20 hacia 300 ka, split ~1.5 Ma.
- Li & Akey et al. 2024, *Science*: flujo sapiens→neandertal 250–200 ka y 120–100 ka.
- Fewlass / Prüfer et al. 2025, *Nature*: Ranis–Zlatý kůň; introgresión neandertal
  compartida por no africanos ~49–45 ka.
- Hallett et al. 2025, *Nature*: expansión del nicho africano desde ~70 ka
  precede la salida exitosa ~50 ka.
- Ferring / Lordkipanidze, Dmanisi ~1.85–1.77 Ma.
- Zhu et al. 2018, Shangchen ~2.12 Ma (industria; especie abierta).
- Herries et al. 2020, Drimolen ~2.04 Ma (posible *erectus* africano temprano).
- Stringer, Scerri, Hublin: modelo pan-africano de sapiens.

## Cliodinámica (capa de evolución, no de origen)

- Turchin, Structural-Demographic Theory; Seshat Databank.
- Korotayev, crecimiento hiperbólico.
- Morris, Social Development Index.
- Taagepera 1978, área de imperios.
- Goldstone, revolución y presión demográfica.

El modelo de este repo **no** adopta el SDI ni el índice Seshat como
variable de estado. Usa `s ∈ R₊⁶` anclado al archivo. Ver
`modelo/MODELO_EVOLUCION_DIMENSIONAL.md`.

## Cómo citar un nodo nuevo

En `datos/origenes/` el campo `sources` es una lista
`{ "cite": "Autor Año", "claim": "qué fecha o hecho se toma" }`.
En el árbol corto, condensar en `notes`.
