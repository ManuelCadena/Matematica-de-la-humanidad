# Guía del implementador

Este directorio especifica **todos** los modelos matemáticos del proyecto
*Modelo Matemático de la Humanidad* para que otro LLM o un humano los
reimplemente sin la sesión original.

## Orden de lectura

1. Este archivo (contratos globales e invariantes).
2. `SPEC_01_LENTES.md` — ontología de visiones.
3. `SPEC_02_FIBRADO_ALLEN.md` — espacio-tiempo discreto + álgebra de intervalos.
4. `SPEC_03_FIBRAS_ACOPLES.md` — civilización como sección y puertos.
5. `SPEC_04_MANDALA_CONO_SIM.md` — campo continuo, cono, sábana, simulación datada.
6. `referencia_modelos.py` — algoritmos canónicos copiables.

Datos de entrada (`datos/`):

- `cronologia_mundial_arbol.json`
- `historia_ontologia.json`
- `civilizaciones_fibras.json`
- `acoples_multicapa.json`
- `modelo_espacio_tiempo.json`
- `sim_meta.json`
- `dimensiones_por_civilizacion.json`

## Convención temporal

- Año entero `t ∈ ℤ`. Negativo = a.C. astronómico (`-44` = 44 a.C.).
- No hay año 0 en el calendario histórico vulgar; este modelo **usa** 0 como
  entero (convención astronómica). No convertir a “1 a.C.” en el código.
- Intervalos cerrados `[t0, t1]` con `t0 ≤ t1`. `t1` inclusive.

## Convención espacial

Dos bases distintas; **no mezclarlas en la misma función**.

| Símbolo | Tipo | Dónde |
|---|---|---|
| `R` | 16 regiones + `humanidad` | fibrado discreto |
| `M` | superficie terrestre, lon/lat | campo, cono, sábana |

`humanidad` es transversal: `d_R(humanidad, ·) = 1` por convenio.

## Dimensiones `D` (orden canónico)

```
politico, historico, religioso, cientifico, cultural, social
```

Índices 0..5 en vectores `s ∈ R_+^6`.

## Invariantes (fallar el test = implementación inválida)

1. Un nodo puede tener varias lentes. No forzar una sola.
2. Una civilización no es un nodo: es `(W_C, F_C)`.
3. Un nodo puede pertenecer a varias civilizaciones (puerto).
4. No existe métrica escalar canónica de cercanía. El objeto es `(d_T, d_R, d_D)`.
5. Un cono geográfico es una **polidad datada**. `amp(t)=0` si `t∉[t0,t1]`.
6. Teotihuacan no puede estar activa en t=700. Tenochtitlan no puede estarlo en t=100.
7. `A_t` se estima con acoples tipados. No inventar pesos de conquista.
8. `u(t+Δ)=A^Δ u(t)` es escenario, no predicción. Documentarlo en la API.
9. Mesoamérica no empieza en Teotihuacan: hay registro desde el paleolítico y polidades desde San Lorenzo.
10. Si `t1 >= 2026`, el Estado vivo mantiene `amp=1` (no matar polidades contemporáneas).

## Tipos de acople (enum cerrado)

`exchange, trade, war, treaty, conquest, fusion, succession, translation,
diffusion, conversion, diaspora, contact, expansion, coexist`

Simétricos por defecto: `exchange, trade, coexist, fusion, translation`.
Los demás son dirigidos `from → to`.

## Qué no implementar

- GIS con polígonos de Estados modernos.
- “Edad Media” como periodo mundial.
- Un cono llamado `mesoamerica` de −2000 a 1697.
- Suma ponderada de distancias sin que el llamador pase `α,β,γ` explícitos.
