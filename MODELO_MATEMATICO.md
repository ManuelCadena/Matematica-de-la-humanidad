# Modelo matemático — historia como fibrado multicapa sobre el espacio-tiempo

Versión 7.1 documentada. Archivos de datos: `modelo_espacio_tiempo.json`, `civilizaciones_fibras.json`, `acoples_multicapa.json`, `historia_ontologia.json`.

---

## 1. Por qué no basta un árbol

Un árbol impone una sola relación de inclusión: *A es hijo de B*.
La historia humana no es así. El mismo año, en el mismo valle, conviven
una dinastía, un rito, una técnica y un régimen de trabajo. Esas capas
no son subapartados unas de otras. Se cruzan.

El objeto correcto es un **grafo multicapa con soporte en el espacio-tiempo**,
que en geometría se lee como un **fibrado discreto**.

---

## 2. Espacio base

\[
B \;=\; R \times T
\]

- \(R\): conjunto finito de regiones historiográficas
  (16 árboles regionales + el eje transversal `humanidad`).
- \(T = \mathbb{Z}\): años, con convención astronómica (negativo = a.C.).

Un punto de \(B\) es un par \((r,t)\): “el Nilo en el 1258”.

Las regiones no son polígonos GIS. Son categorías con un **grafo de
adyacencia** \(A\subset R\times R\) (Nilo–Levante son vecinos; Andes–Estepa no).
La distancia espacial es la distancia de grafos

\[
d_R(r,s) \;=\; \mathrm{dist}_{A}(r,s)\in\{0,1,2,3\}.
\]

---

## 3. Dimensiones (fibras abstractas)

\[
D \;=\; \{\text{político},\;\text{histórico},\;\text{religioso},\;\text{científico},\;\text{cultural},\;\text{social}\}
\]

Cada \(d\in D\) es una **capa**. Un hecho puede vivir en varias a la vez:
el hajj de Mansa Musa es histórico *y* religioso *y* social.

La distancia dimensional es discreta:

\[
d_D(\varphi,\psi) \;=\; 0 \text{ si }\varphi\cap\psi\neq\varnothing,\quad 1\text{ si no.}
\]

---

## 4. Nodos

Un nodo \(v\in V\) (entidad del corpus) se mapea

\[
v \;\longmapsto\; \bigl(\,I(v),\;\sigma(v),\;\varphi(v)\,\bigr)
\]

- \(I(v)=[t_0,t_1]\subset\mathbb{Z}\): intervalo cerrado de existencia.
- \(\sigma(v)\subseteq R\): soporte espacial.
- \(\varphi(v)\subseteq D\): lentes en las que el nodo es legible.

El álgebra temporal no es “antes / después”. Es el **álgebra de intervalos
de Allen** (13 relaciones): `precedes`, `meets`, `overlaps`, `during`,
`starts`, `finishes`, `equals`, y sus inversas.

Distancia temporal:

\[
d_T(I,J) \;=\;
\begin{cases}
0 & \text{si }I\cap J\neq\varnothing,\\
\mathrm{gap}(I,J) & \text{si no.}
\end{cases}
\]

---

## 5. Civilización = sección + fibras

Una civilización no es un nodo. Es un par

\[
C \;=\; (W_C,\; F_C)
\]

- **Línea de mundo** (sección sobre el base):

\[
W_C \;\subset\; B,\qquad
W_C \;=\; \sigma_C \times [t_C^{\min}, t_C^{\max}].
\]

Ejemplo: Egipto \(= \{\text{af-nile}\}\times[-4000,640]\).

- **Fibra** en la dimensión \(d\):

\[
F_C(d) \;=\; \bigl\{\, v\in V \;\big|\;
\sigma(v)\cap\sigma_C\neq\varnothing,\;
I(v)\cap[t_C^{\min},t_C^{\max}]\neq\varnothing,\;
d\in\varphi(v) \,\bigr\}.
\]

\(F_{\text{Egipto}}(\text{religioso})\) contiene *maat*, Osiris, el atonismo, la Iglesia copta.
\(F_{\text{Egipto}}(\text{político})\) contiene las dinastías. Mismo soporte \(W_C\),
distinta fibra.

Un nodo puede pertenecer a **varias** civilizaciones (Alejandría: Egipto ∩ Hélade ∩ Roma).
Eso no es un error de clasificación: es un **puerto**.

---

## 6. Acoples (cruces)

Un acople es una arista tipada entre secciones:

\[
e \;=\; \bigl(C_i,\; C_j,\; \lambda,\; v_\star,\; I_e,\; D_e\bigr)
\]

- \(\lambda\): tipo (`conquest`, `translation`, `diaspora`, `trade`, …).
- \(v_\star\): nodo-vía (Qadesh, hajj, Cajamarca).
- \(I_e\): cuándo ocurre el cruce.
- \(D_e\subseteq D\): en qué dimensiones ocurre.

El hajj de 1324–25 acopla Sahel e *islamicate* en
\(D_e=\{\text{religioso},\text{social},\text{histórico}\}\).
La traducción budista Chang’an acopla India y China en
\(\{\text{religioso},\text{cultural}\}\), no en “lo político en general”.

---

## 7. Distancia (lo que el modelo *prohíbe*)

El espacio natural es el producto

\[
\bigl(d_T,\; d_R,\; d_D\bigr) \;\in\; \mathbb{N}\times\mathbb{N}\times\{0,1\}.
\]

**No hay métrica escalar canónica** de “cercanía histórica”.
Una suma ponderada \(\alpha d_T+\beta d_R+\gamma d_D\) elige valores.
Eso ya no es geometría: es una decisión de investigación.

---

## 8. Operaciones computables

| Operación | Definición |
|---|---|
| `slice(t)` | \(\{v: t_0\le t\le t_1\}\) — simultaneidad |
| `fiber(C,d)` | \(F_C(d)\) |
| `join(C_i,C_j,t)` | acoples cuyo \(I_e\) contiene \(t\) |
| `project` | \(\pi_T\), \(\pi_R\), \(\pi_D\) |
| `allen(I,J)` | una de las 13 relaciones |

Implementación: `modelo_espacio_tiempo.json` → `matematica.operaciones`.

---

## 9. Lo que el modelo no es

No es un GIS. No es una física. \(R\) no son lat/lon; \(T\) no es \(\mathbb{R}\).
La utilidad es **cortar y cruzar sin aplastar lentes**: se puede preguntar
qué fibras religiosas del campo índico se acoplan al sínico por *traducción*
entre 65 y 800, sin convertir eso en una dinastía china.

---

## 10. Figura

`geometria_fibrado_3d.png` — las 22 líneas de mundo en el plano \(T\times C\),
las 6 capas dimensionales en \(Z\), y los acoples como puentes de color.
