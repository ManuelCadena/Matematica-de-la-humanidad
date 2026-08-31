# SPEC 04 — Campo-mandala, cono, sábana, simulación datada

## 4.1 Campo-mandala

Sea `M` la superficie terrestre (o una malla lon/lat).
Para cada civilización o polidad `C` y cada `d ∈ D`:

```
φ_{C,d} : M × T → [0, ∞)
```

Forma local con centro móvil `c(t) ∈ M`:

```
φ(x,t) = a(t) * K( dist_g(x, c(t)) / r(t) )
```

`K` decrece: gaussiana `exp(-ρ²)`, exponencial `exp(-ρ)`, o `1/(1+ρ²)`.
`a(t)` amplitud. `r(t)` radio.

Solape permitido:

```
sum_C 1{φ_{C,d}(x,t) > ε}  puede ser > 1
```

Eso es el mandala (Wolters). Westfalia pediría producto cero.

`φ` político y `φ` religioso **no** comparten radio por defecto.

Distancia geográfica recomendada: haversine en km. La simulación actual
usa euclidiana en grados (aproximación de tablero; declararla).

## 4.2 Transferencia

Discretizar `M` en `n` celdas y `k` entidades. Estado en lente `d`:

```
u_d(t) ∈ R^{n·k}
u(t+1) = A_t u(t) + s_t
```

- `A_t` se construye desde `acoples_multicapa.json` (tipo → peso).
- `s_t` = fuentes (aparece un canon, una capital).
- Autovectores de un tramo estable ≈ rutas persistentes.
- `u(t+Δ) = A^Δ u(t)` SOLO si el API se llama `scenario(...)`, nunca `predict`.

Pesos sugeridos (el llamador puede cambiarlos; no son datos):

```
trade,exchange = 0.15
translation,diffusion = 0.10
conversion,diaspora = 0.12
conquest,war = 0.20     # trasvase político, no “destrucción de φ cultural”
succession,fusion = 0.25
contact,expansion = 0.08
coexist = 0.02
```

`A_t[i←j]` se incrementa si existe acople cuyo `I_e` contiene `t`.

## 4.3 Cono, altura, radio

Vector de fuerza:

```
s_C(t) = (s_pol, s_hist, s_rel, s_cie, s_cul, s_soc) ∈ R_+^6
H_C(t) = ||s_C(t)||_p
R_C(t) = H_C(t) * tan(α)
```

- `p=1` suma dimensiones.
- `p=2` euclidiana (default geométrico).
- `p=∞` solo la dimensión máxima.

`α` es parámetro de escala. Default de simulación: `52°`.
Declararlo en la salida.

Cono:

```
z_C(x,t) = H * max(0, 1 - dist(x, c_C) / R)
```

Si `H=0` o `R=0`, `z=0`.

Sábana:

```
Φ(x,t)   = sum_C z_C(x,t)      # interferencia / puertos
Φ∨(x,t)  = max_C z_C(x,t)      # cuencas
```

Curvas de nivel:

```
γ_c(t) = { x ∈ M | Φ(x,t) = c }
```

Collado (puerto): punto silla de `Φ` entre dos picos, o lugar
`z_C = z_{C'}` si se usa `Φ∨`.

## 4.4 Unidad temporal del cono = polidad datada

PROHIBIDO un cono `mesoamerica` de −2000 a 1697.

```
Cono {
  id, name,
  xy: [lon, lat],     # centro histórico, no centroide de Estado moderno
  t0, t1,             # start/end del nodo en cronologia_mundial_arbol.json
  peak: float,        # ∈ (0,1], amplitud máxima ilustrativa
  src: string         # id del nodo fuente
}
```

Envolvente (rampa 40 años):

```
def envelope(t, t0, t1, rise=40, fall=40):
    if t < t0 or t > t1: return 0.0
    if t < t0 + rise:    return max(0.0, (t - t0) / rise)
    if t > t1 - fall:    return max(0.0, (t1 - t) / max(1.0, fall))
    return 1.0

amp(t) = peak * envelope(t, t0, t1)
H(t)   = amp(t) * HMAX
```

`HMAX` default = 16 (unidades de dibujo, no km).

Ventanas canónicas (tests de regresión):

```
teotihuacan   lon=-98.84 lat=19.69   [-100, 650]
tula          lon=-99.34 lat=20.06   [900, 1150]
tenochtitlan  lon=-99.13 lat=19.43   [1325, 1521]
tikal         lon=-89.62 lat=17.22   [200, 900]
cuzco         lon=-71.97 lat=-13.52  [1438, 1572]
rome          lon=12.50  lat=41.90   [-50, 476]
constantinopla lon=28.98 lat=41.01   [330, 1453]
bagdad        lon=44.39  lat=33.34   [762, 1258]
timbuktu      lon=-3.01  lat=16.77   [1235, 1460]
changan       lon=108.94 lat=34.27   [-221, 907]
karakorum     lon=102.84 lat=47.21   [1206, 1260]
```

Lista completa: `sim_meta.json` → `conos` (81 entradas, −4000…2026).

## 4.5 Simulación sobre mapa real

Base: imagen **equirectangular** (p. ej. NASA Blue Marble 2048×1024).
Extent: `lon ∈ [-180,180]`, `lat ∈ [-90,90]`, origin upper.

```
x_px = (lon + 180) / 360 * width
y_px = (90 - lat) / 180 * height
```

Pasos:

1. Cargar `sim_meta.json` conos.
2. Para cada `t` en `years` (0..1500 paso 50):
   a. `amp_C = peak * envelope(t,t0,t1)`
   b. malla lon/lat; `Φ = Σ z_C`
   c. `contourf` + `contour` sobre el mapa
   d. etiquetar solo conos con `amp ≥ 0.04`
3. Guardar fotogramas `f000.png`…
4. `ffmpeg -framerate 6 -i f%03d.png -c:v libx264 -pix_fmt yuv420p out.mp4`

`vmax` global = 1.05 × max_t Φ, para que la escala de color no salte.

## 4.6 Tests de regresión (obligatorios)

```
assert teotihuacan ∉ active(700)
assert teotihuacan ∈ active(100)
assert tenochtitlan ∉ active(100)
assert tenochtitlan ∈ active(1400)
assert cuzco ∉ active(1000)
assert cuzco ∈ active(1450)
assert rome ∉ active(500)          # occidente cae 476; queda Constantinopla
assert bagdad ∉ active(700)
assert bagdad ∈ active(800)
assert bagdad ∉ active(1300)       # 1258
```

`active(t) = { C.id | amp_C(t) ≥ 0.04 }`

## 4.7 Lectura del relieve

| Forma | Lectura |
|---|---|
| Pico alto, anillos juntos | núcleo intenso, poco alcance |
| Pico alto, anillos abiertos | dimensiones llenas → radio grande |
| Collado | puerto |
| Anillo que se contrae | la polidad deja de levantar Φ |
| Varios picos en la misma cota baja | periferia de mandala compartida |
