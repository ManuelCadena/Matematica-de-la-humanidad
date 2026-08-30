# Matemática de la humanidad

Modelo matemático y corpus para leer la historia humana como un **fibrado multicapa** sobre el espacio-tiempo, realizado sobre la Tierra como **conos de influencia datados**.

No es una ley de la historia. Es un estado `s ∈ R⁺⁶`, un operador de transferencia `A_t` armado con acoples, y una geometría que se apaga cuando el JSON dice que la polidad murió.

## Qué hay aquí

| Ruta | Contenido |
|---|---|
| `docs/` | Especificaciones para reimplementar |
| `modelo/` | Cartas matemáticas (lentes, fibrado, mandala, cono, evolución) |
| `datos/` | Árbol cronológico, ontología, fibras, acoples, conos |
| `app/index.html` | Analizador: mapa, Φ(x,t) calculado, −4000 a 2026 |

Abrir el analizador: descargar `app/index.html` y abrirlo en el navegador (lleva los datos incrustados).

## Capas

```
0  Lentes          un hecho, cinco lecturas
1  Fibrado         B = R × T,  C = (W_C, F_C)
2  Campo-mandala   φ_{C,d}(x,t) sobre la Tierra
3  Cono / sábana   H = ||s||, R = H tan α, Φ = Σ z
```

Reglas que el código debe respetar:

- Un cono es una **polidad datada** `[t0, t1]`, no una civilización eterna.
- Mesoamérica no empieza en Teotihuacan: San Lorenzo → La Venta → Cuicuilco / El Mirador → Teotihuacan → Tula → Tenochtitlan.
- Teotihuacan −100 a 650. Tenochtitlan 1325–1521.
- No hay métrica escalar canónica de cercanía histórica. El objeto es `(d_T, d_R, d_D)`.
- `A^n u` es escenario, no predicción.
- «Qué gana» (militar, cultura, fe, población) es una norma `||W s||_p`, no un descubrimiento.

## Datos

- `datos/cronologia_mundial_arbol.json` — ~2180 nodos
- `datos/historia_ontologia.json` — lentes + árbol religioso
- `datos/civilizaciones_fibras.json` — 22 secciones
- `datos/acoples_multicapa.json` — puertos tipados
- `datos/sim_meta.json` — conos con lon/lat y ventanas

Origen temporal del analizador: **−4000** (Uruk, Nilo, Caral). El árbol de especie llega a −7 000 000; eso no se dibuja como cono de Estado.

## Implementación

```
python docs/referencia_modelos.py
# selftest ok
```

Leer primero `docs/00_LEEME_IMPLEMENTADOR.md`.

## Autor

Proyecto de Manuel Cadena. Corpus y modelo, 2026-08-30.
