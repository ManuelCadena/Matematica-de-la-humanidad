# Método de las gráficas 1–7

Fuente: `datos/sim_meta.json` (81 conos), `datos/acoples_multicapa.json` (39),
`datos/civilizaciones_fibras.json` (22), árbol plano 2 296 nodos.
Implementación de `z_C`, `env`, `assign_dims`: `docs/referencia_modelos.py`.

## Constantes (no se ocultan)

| Símbolo | Valor | Qué decide |
|---|---|---|
| α | 52° | Radio del cono = altura × tan α |
| umbral | 0,04 | Debajo, la cima no cuenta |
| rampa | 40 años | Subida/bajada en t0 y t1 |
| HMAX | 16 | Tope de altura |
| métrica espacial | euclidiana en grados | tablero, no esfera |

## Qué mide cada lámina

1. Morse / Cech sobre soportes de cono activos. Pico = centro con amp×env ≥ 0,04. Collado = z_C = z_C' en el segmento. Arista si dist(c,c') < R+R'.
2. Nacimiento / muerte = primer / último t con amp×env ≥ 0,04. No es persistencia de superlevel sets de Φ.
3. A[to, from] += w(tipo) si el intervalo del acople corta la ventana. ρ(A) < 1 en las cuatro ventanas. A^n u = escenario.
4. μ_t = medida atómica en los centros, masa = amp×env. W1 exacto (OT). No es W1 de Φ dx.
5. 1 135 polidades; filtro d_R ≤ 1 y d_T ≤ 200. Sin el filtro temporal, `precedes` se traga el resto.
6. Φ_d = suma π_{C,d} z_C en t = 1000. π = n_{C,d} / ||n_C||_1. Radio aún compartido entre lentes.
7. Color = log(1+n) de nodos cuyo intervalo corta el bin de 200 años. Azul = acople cuya lista de lentes incluye esa.

## Lo que el método no autoriza

- Un escalar de «poder» o «complejidad».
- Rellenar 197 pares vacíos.
- Cerrar White Sands / Sahul / Shangchen.
- Tratar Menfis 3026 años como una sola polidad.
