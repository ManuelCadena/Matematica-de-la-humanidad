# Datos

## Canónico

En el entorno de trabajo los JSON grandes viven también en la raíz de
`artifacts/`. Aquí, `datos/` es la vista de repositorio.

| Archivo | Qué contiene | Capa |
|---|---|---|
| `cronologia_mundial_arbol.json` | 16 árboles, `trees` + `flat` | política + humanidad |
| `historia_ontologia.json` | nodos, lentes, índices, religión | 0 |
| `civilizaciones_fibras.json` | 22 secciones `C = (W, F)` | 1 |
| `acoples_multicapa.json` | puertos tipados | 1 |
| `modelo_espacio_tiempo.json` | R, Allen, notación | 1 |
| `dimensiones_por_civilizacion.json` | dimensiones constitutivas | 1 |
| `sim_meta.json` | conos datados lon/lat | 3 |
| `origenes/homininos.json` | taxones Hominina / *Homo* | 0.5 |
| `origenes/migraciones.json` | pulsos OoA y poblamiento | 0.5 |
| `origenes/yacimientos.json` | sitios ancla | 0.5 |
| `origenes/introgresion.json` | admixture datada | 0.5 |
| `schemas/nodo.schema.json` | contrato de nodo | — |

## Convención

- `flat` se **reconstruye** desde `trees`. No editar el plano a mano.
- Un `id` es estable. Fibras y acoples lo citan.
- `kind` de SPEC_05 no entra en `sim_meta` como cono de Estado.
- `start ≤ end`. Precisión gruesa en el Pleistoceno no es un error.

## Cómo regenerar índices ontológicos

Ver `LLM.md` §6 y el script de fusión que produjo `origenes/`
(sesión 2026-08-30). Cualquier alta nueva debe:

1. existir en `origenes/` si es especie/migración/sitio/admixture;
2. existir como hijo en `trees[humanidad]`;
3. existir en `historia_ontologia.json` → `nodos`;
4. aparecer en los seis índices.

## Conteos de referencia (actualizar al cambiar)

Anotar en el commit, no aquí a mano cada semana. Ver `meta` de cada JSON.
