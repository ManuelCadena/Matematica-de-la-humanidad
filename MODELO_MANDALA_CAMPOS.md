# Extensión: campos-mandala sobre la Tierra

El modelo v7.1 vive en R discreto (16 regiones). Esta nota añade la
capa continua que el análisis pide: influencia como campo sobre el
globo, deformándose en el tiempo.

## Campo

Sea M la superficie terrestre (o una malla). Para cada civilización C
y cada dimensión d ∈ D,

    φ_{C,d} : M × T → [0, ∞)

φ_{C,d}(x,t) = intensidad de C en x, año t, en la lente d.

Un mandala político no coincide con el religioso: el φ político de
Ayutthaya y el φ theravāda no tienen el mismo radio.

## Forma local (cono / manto)

Si c(t) ∈ M es el centro móvil (capital, puerto, templo),

    φ(x,t) = a(t) · K( dist_g(x, c(t)) / r(t) )

K decrece (exponencial, gaussiana, o 1/(1+ρ²)).
r(t) es el radio de influencia.
a(t) es la amplitud (prestigio, flota, canon).

Los conos se solapan: Σ_C 1_{φ_{C,d}(x,t)>ε} puede ser > 1.
Eso es el mandala, no el Estado westfaliano.

## Sábana temporal

La “sábana” es la sección

    S_d(t) = { (x, φ_{•,d}(x,t)) : x ∈ M }

Animar t es ver S_d deformarse. No es una sola sábana: hay seis
(una por dimensión), y se cruzan.

## Capa matricial

Se discretiza M en celdas i = 1..n y C en k civilizaciones.
El estado en la lente d, año t, es un vector (o matriz)

    u_d(t) ∈ ℝ^{n·k}

La evolución retrospectiva se escribe

    u(t+1) = A_t u(t) + s_t

A_t es el operador de transferencia (comercio, conquista, traducción,
diáspora). s_t son fuentes (fundación de un canon, hallazgo técnico).

A_t se estima con los acoples ya tipados (acoples_multicapa.json),
no se inventa.

Autovectores de A_t ≈ rutas persistentes (Índico, Sahel, Mediterráneo).
Eso es “de dónde vino”.

## Límite

“A dónde va” no es un teorema. No hay ley de conservación de la
historia. Una proyección u(t+Δ) = A^Δ u(t) solo vale como escenario
bajo A constante — y A nunca lo es (1492, 1914, 1945 rompen A).
La matriz explica el pasado y acota inercias. No profetiza.
