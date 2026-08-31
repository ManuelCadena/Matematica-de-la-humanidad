# Evolución temporal de las dimensiones

Propuesta anclada al corpus y contrastada con quien ya matematizó la historia.
No es una ley. Es un sistema observable + un operador de transferencia.

## 1. Qué mide este dataset (y qué no)

| Símbolo | Qué es | Qué no es |
|---|---|---|
| \(Ñ_d(t)\) | nodos con lente \(d\) cuyo \([t_0,t_1]\) cubre \(t\) | poder, PIB, energía, población |
| \(n_{\mathrm{pol}}(t)\) | polidades vivas | complejidad social de Seshat |
| \(z_C(x,t)\) | cono de una polidad datada | “civilización eterna” |
| \(\Phi(x,t)\) | sábana | frontera westfaliana |

\(Ñ_d\) crece hacia 1500 en parte porque el archivo es más denso y porque
este corpus se taladró más en siglos tardíos. Tratar \(Ñ\) como “auge de la
humanidad” es un error de especificación.

Observado en el corpus (nodos ontológicos activos):

| t | histórico | científico | religioso | cultural | social | político (árbol) |
|---|---|---|---|---|---|---|
| 0 | 108 | 9 | 49 | 47 | 20 | 54 |
| 600 | 186 | 10 | 70 | 50 | 26 | 105 |
| 1000 | 262 | 10 | 96 | 68 | 40 | 183 |
| 1400 | 356 | 9 | 118 | 65 | 44 | 258 |

La lente científica casi no crece: el corpus no es un recuento de invenciones.
La política sí: es donde más se perforó. Eso informa el modelo, no lo refuta.

## 2. Estado

Por entidad \(C\) (polidad o sección civilizatoria):

\[
s_C(t)=\bigl(s_{\mathrm{pol}},s_{\mathrm{hist}},s_{\mathrm{rel}},s_{\mathrm{cie}},s_{\mathrm{cul}},s_{\mathrm{soc}}\bigr)\in\mathbb{R}_+^{6}.
\]

Altura del cono (norma, no suma ciega):

\[
H_C(t)=\|s_C(t)\|_2\cdot \pi_C,\qquad
R_C(t)=H_C(t)\tan\alpha,\qquad \alpha=52^\circ.
\]

\(\pi_C\in(0,1]\) es el `peak` de archivo / escala visual, no un dato excavado.

Envolvente temporal (obligatoria):

\[
\mathrm{env}(t;t_0,t_1)=
\begin{cases}
0 & t\notin[t_0,t_1]\\
(t-t_0)/40 & t\in[t_0,t_0+40)\\
(t_1-t)/40 & t\in(t_1-40,t_1]\\
1 & \text{resto.}
\end{cases}
\]

Sin esto Teotihuacan sigue hasta 1500. El JSON lo prohíbe.

## 3. Dinámica propuesta

\[
s_C(t+\Delta)=
\mathrm{env}(t;t_0^C,t_1^C)\cdot
\Bigl[(1-\delta)\,s_C(t)
+\sum_{e\ni t} w(e)\,P_{e\to C}\,s_{\mathrm{src}(e)}(t)
+b_C(t)\Bigr]
\]

- \(\delta\in(0,1)\): olvido / pérdida de archivo institucional (bajo en un canon, alto en una corte que se quema).
- \(e\ni t\): acoples cuyo intervalo cubre \(t\) (`acoples_multicapa.json`).
- \(w(e)\): peso del *tipo* (trade 0.15, translation 0.10, conquest 0.20…). El llamador los declara.
- \(P_{e\to C}\): máscara \(6\times 6\) que solo mueve las lentes listadas en `e.dims`.
- \(b_C(t)\): nacimiento interno (un texto, una reforma) cuando \(t\) cae en un nodo hijo de \(C\).

Agregado mundial (no es un mundo-sistema único):

\[
S_d(t)=\sum_C s_{C,d}(t).
\]

Proxy observable:

\[
Ñ_d(t)\;\approx\; c_d\,S_d(t)+\varepsilon_d(t)
\]

donde \(\varepsilon\) incluye sesgo documental. **No invertir** \(Ñ\to S\)
sin un modelo de ese sesgo.

Matricial, en una lente, sobre celdas geográficas:

\[
u(t+\Delta)=A_t u(t)+s_t.
\]

\(A_t\) se estima con acoples, no se inventa. Autovectores de un tramo
estable ≈ rutas (Índico, Sahel, Mediterráneo): “de dónde vino”.
\(A^{n}u\) es `scenario`, nunca `predict`. 476, 650, 1258, 1492 rompen \(A\).

## 4. Relación con la literatura

### Turchin, Goldstone, Seshat (cliodinámica)

- Goldstone 1991: teoría estructural-demográfica (SDT).
- Turchin 2003 *Historical Dynamics*: SDT en ecuaciones.
- Seshat: 414 sociedades, 51 variables, 10 000 años.
- PNAS 2018: *una* dimensión principal organiza la complejidad social.
- \(\Psi = \mathrm{MMP}\times\mathrm{EMP}\times\mathrm{SFD}\).
  MMP = inmiseración × urbanización × youth bulge.
  EMP = competencia intraélite. SFD = apuro fiscal.
- Predicción 2010 de inestabilidad 2010–20 (PLOS ONE 2020): presiones, no el atentado.

**Qué tomar.** Formalizar presión y no el evento. Medir. Rechazar teorías
con Seshat (agricultura + caballería/hierro como drivers, 2022).

**Qué no tomar.** Colapsar nuestras 6 lentes en el PC1 de Seshat. Ese PC1
existe como correlación empírica; no autoriza a borrar lo religioso-émico.
Datos premodernos de salarios y élites son frágiles (críticas UnHerd,
Kairos 2024, Davies). Popper sigue valiendo para “leyes de la historia”.

### Korotayev, Malkov, Khaltourina

\[
U(t)=\frac{C}{(t_0-t)^2}
\]

Urbanización y población mundiales hasta ~1970, \(R^2\) altísimo.
Fases A1/A2/A3 (urbano/alfabetización). Centro–periferia tribal.

**Qué tomar.** El mundo-sistema *tiene* escalares hiperbólicos en demografía.
**Qué no tomar.** Esa hipérbola no es \(s_{\mathrm{rel}}(t)\) ni \(\Phi(x,t)\).
Una singularidad en 2047 es un artefacto del régimen, no un destino.

### Ian Morris

Índice: energía, organización/urbanización, guerra, información.
Él mismo: el gráfico “no es correcto”; sirve para ver la forma a explicar.

**Qué tomar.** Separar *medida* de *explicación*.
**Qué no tomar.** Cuatro rasgos con peso igual como ontología de D.

### Taagepera 1978

Área imperial → logística hacia 133 Mm² (tierra firme). Saltos ~2800 a.C.,
~600 a.C., ~1600.

**Qué tomar.** El radio \(R_C=H\tan\alpha\) es el primo geométrico de esa área.
**Qué no tomar.** El techo 133 Mm² como ley de nuestros conos locales.

### HANDY / Motesharrei 2014

Lotka–Volterra élites/comunes. Se vendió como “NASA predice colapso”.
Sin datos históricos. No entra al modelo.

### Maya collapse (Hamblin–Pitcher vs Lowe 1982)

Curvas que ajustan monumentos ajustan también hipótesis rivales.
Lección para \(Ñ(t)\): un buen fit no identifica el mecanismo.

## 5. Veredicto sobre *este* planteamiento

Es correcto:

1. No aplastar lentes.
2. Civilización = sección + fibras, no un nodo.
3. Cono atado a \([t_0,t_1]\) del JSON.
4. Distancia como vector \((d_T,d_R,d_D)\).
5. \(A_t\) salido de acoples tipados.
6. Animar el estado no es profetizar.

Es incorrecto si:

- se lee \(Ñ_d\) como “fuerza de la humanidad”;
- se deja un cono de Mesoamérica de −2000 a 1697;
- se vende \(A^n u\) como el siglo XXII;
- se ignora que Seshat ya midió complejidad con otra ontología (y encontró
  un PC1 que el nuestro no debe fingir que no existe: las lentes *correlacionan*).

Puente honesto con Seshat: el PC1 es una *proyección* \(\mathbf{1}^\top s_C\).
Nosotros guardamos \(s_C\) antes de proyectar. Se puede calcular el PC1
sobre nuestras 6 componentes *después*, no en vez.

## 6. Cómo se analiza en la app

`app/index.html` (copia: `Analizador_Humanidad.html`).

- Mapa: \(\Phi\) se evalúa en cada celda, no se pinta un CGI.
- Clic: muestra \(\Phi(x,t)\) y los \(z_C\) que contribuyen.
- Dimensiones: \(Ñ_d(t)\) del corpus.
- Conos: lista filtrada por `env ≥ 0.04`.
- Acoples: \(e\) con \(t\in I_e\) (insumos de \(A_t\)).
- ▶ recorre \(t=0,25,\ldots,1500\). Fuente de verdad temporal = JSON.


## 7. La duda existencial: si hubiera una sola ecuación, ¿qué gana?

Corta: **nada gana por ley**. Una sola ecuación que declare al ganador no es un descubrimiento; es una norma \(\|W s\|_p\).

| Si eliges… | Estás afirmando… | Quién ya lo hizo | Contraejemplo |
|---|---|---|---|
| población | más gente → más inventores → más capacidad | Korotayev | Atenas, Florencia, el hebreo |
| militar | la guerra hace al Estado | Tilly | mongol sin lengua; británico sin mapa |
| cultura/religión | el canon sobrevive al cono | Weber / mundos-sistema culturales | el rito no paga un ejército en t+1 |
| organización | la complejidad escala | Seshat PC1 | el PC1 es \(1^	op s\), no \(s\) |

El horizonte cambia el “ganador”:

- 10 años: coerción
- 100 años: fisco + demografía
- 500 años: institución
- 2000 años: lengua, escritura, rito

Por eso el estado del modelo es \(s\in\mathbb{R}_+^6\) y no un escalar. Quien quiera un ganador debe publicar \(W\) y \(p\).
