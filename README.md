# Matemática de la humanidad

Modelo matemático y corpus para leer la historia humana como un **fibrado
multicapa** sobre el espacio-tiempo, realizado sobre la Tierra como
**conos de influencia datados**, y asentado sobre una capa de **origen
de la especie** (homininos, migraciones, introgresión).

No es una ley de la historia. Es un estado `s ∈ R⁺⁶`, un operador de
transferencia `A_t` armado con acoples, y una geometría que se apaga
cuando el JSON dice que la polidad murió.

**Si eres un modelo de lenguaje: abre `LLM.md` ahora.**

## Mapa del repositorio

```
LLM.md                 contrato para cualquier IA (leer primero)
README.md              esta página
CITATIONS.md           piso académico
docs/
  00_LEEME_IMPLEMENTADOR.md
  SPEC_01_LENTES.md
  SPEC_02_FIBRADO_ALLEN.md
  SPEC_03_FIBRAS_ACOPLES.md
  SPEC_04_MANDALA_CONO_SIM.md
  SPEC_05_ORIGENES_MIGRACIONES.md
  referencia_modelos.py          selftest()
modelo/                cartas matemáticas
  CARTA.md  proyecto.json  MODELO_*.md  ONTOLOGIA_LENTES.md
datos/
  schemas/nodo.schema.json
  cronologia_mundial_arbol.json  (~2260 nodos)
  historia_ontologia.json        (~2485 nodos)
  civilizaciones_fibras.json     22 secciones + hominina en dimensiones
  origenes/{homininos,migraciones,yacimientos,introgresion}.json
app/index.html         analizador Φ(x,t)
```

## Capas

```
0    Lentes            un hecho, cinco lecturas
0.5  Orígenes          especie, pulso, yacimiento, ADN   ← no es un Estado
1    Fibrado           B = R × T,  C = (W_C, F_C)
2    Campo-mandala     φ_{C,d}(x,t) sobre la Tierra
3    Cono / sábana     H = ||s||, R = H tan α, Φ = Σ z
```

## Reglas que el código debe respetar

- Un cono es una **polidad datada** `[t0, t1]`, no una civilización eterna.
- Mesoamérica no empieza en Teotihuacan: San Lorenzo → La Venta →
  Cuicuilco / El Mirador → Teotihuacan → Tula → Tenochtitlan.
- Teotihuacan −100 a 650. Tenochtitlan 1325–1521.
- `kind ∈ {species, migration, site, admixture, technocomplex}` **no**
  produce cono político.
- *Homo sapiens* no nace en un solo Edén: modelo pan-africano + fusión
  de dos stems ~300 ka (Ragsdale 2023; Jebel Irhoud 2017).
- Out of Africa no es un evento: OoA-I (*erectus* ~1.8 Ma) no explica a
  los vivos; OoA-II (~60–50 ka) sí. Los pulsos de Misliya / Skhul /
  Al Wusta no son ese tronco.
- No hay métrica escalar canónica de cercanía. El objeto es
  `(d_T, d_R, d_D)`.
- `A^n u` es escenario, no predicción.

## Cómo validar

```
python docs/referencia_modelos.py
# selftest ok
```

## Cómo extender

`LLM.md` §6. Alta nueva = `id` inédito + padre existente + fuente +
reconstrucción de `flat` e índices. Sin fuente no entra.

## Autor

Proyecto de Manuel Cadena. Corpus y modelo, 2026-08-30.
Repo: https://github.com/ManuelCadena/Matematica-de-la-humanidad
