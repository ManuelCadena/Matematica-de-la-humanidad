# Cono, sábana y curvas de nivel

El mandala deja de ser un círculo pintado sobre el mapa. Es un **cono
en el espacio producto** \(M\times\mathbb{R}_+\):

- la **altura** es la fuerza de las dimensiones de esa civilización;
- el **radio de la base** crece con la altura (un cono más alto es
  necesariamente más ancho si el ángulo de apertura es fijo);
- la **sábana** es la superficie que todos los conos levantan juntos;
- las **curvas de nivel** son los conjuntos de nivel de esa sábana.

---

## 1. Fuerza dimensional → altura

Cada civilización \(C\) tiene, en el año \(t\), un vector de fuerza

\[
s_C(t)=\bigl(s_{C,\text{pol}},\,s_{C,\text{hist}},\,s_{C,\text{rel}},\,
s_{C,\text{cie}},\,s_{C,\text{cul}},\,s_{C,\text{soc}}\bigr)\in\mathbb{R}_+^{6}.
\]

La altura del cono es una norma de ese vector:

\[
H_C(t)=\|s_C(t)\|_p
=\Bigl(\sum_{d\in D}s_{C,d}(t)^{p}\Bigr)^{1/p}.
\]

- \(p=1\): las dimensiones se suman (un imperio con religión, fisco y
  escritura altas es muy alto).
- \(p=2\): norma euclidiana; una sola dimensión enorme no basta para
  dominar el paisaje si las otras están vacías.
- \(p=\infty\): solo cuenta la dimensión más fuerte.

En este corpus \(s_{C,d}\) se inicializa con la masa de la fibra
\(F_C(d)\) (conteo de nodos) como *proxy de archivo*, no como
“poder real”. La geometría no depende de esa elección: cualquier
estimación mejor (PIB, alcance epigráfico, radio de moneda) se
enchufa en \(s\) sin cambiar las fórmulas.

Se puede también **no colapsar** las seis componentes: entonces hay
seis conos apilados por civilización, uno por lente, y seis sábanas.

---

## 2. Altura → radio (el cono)

Ángulo de apertura \(\alpha\) fijo (parámetro del modelo):

\[
R_C(t)=H_C(t)\cdot\tan\alpha.
\]

El cono sobre el centro geográfico \(c_C(t)\in M\):

\[
z_C(x,t)=H_C(t)\cdot\max\Bigl(0,\;
1-\frac{\mathrm{dist}_g\bigl(x,c_C(t)\bigr)}{R_C(t)}\Bigr).
\]

Quien es más alto cubre más suelo. Eso no es un adorno visual: es
la afirmación histórica de que una civilización con más dimensiones
activas (escritura + fisco + canon + flota) proyecta más lejos que
una que solo tiene una de ellas.

El ángulo \(\alpha\) es una **elección de escala**. No es un dato
arqueológico. Hay que declararlo.

---

## 3. Sábana

Dos lecturas, las dos legítimas:

**Suma** (interferencia, puertos, zonas mixtas):

\[
\Phi(x,t)=\sum_C z_C(x,t).
\]

Donde dos conos se montan, la sábana sube más: Alejandría, Malaca,
Timbuktú, Chang’an.

**Máximo** (cuenca de influencia, “quién manda aquí”):

\[
\Phi_\vee(x,t)=\max_C z_C(x,t).
\]

Las divisorias de \(\Phi_\vee\) son las crestas de Voronoi ponderadas
por altura: fronteras blandas que se mueven cuando un cono crece.

La sábana es una función

\[
\Phi(\,\cdot\,,t):M\to\mathbb{R}_+.
\]

Animar \(t\) es ver el relieve histórico deformarse.

---

## 4. Curvas de nivel

Para cada cota \(c>0\),

\[
\gamma_c(t)=\bigl\{x\in M:\Phi(x,t)=c\bigr\}.
\]

\(\gamma_c\) es una curva (o unión de curvas) sobre el mapa.
Son las **isobaras de influencia**:

- \(c\) alta, cerca de un pico: el núcleo (capital, templo, archivo);
- \(c\) baja, lejos: la periferia del mandala, donde se tributa a
  dos centros a la vez.

Si se usa \(\Phi_\vee\), la curva que separa la cuenca de \(C\) de la
de \(C'\) es el lugar donde \(z_C=z_{C'}\). Esa curva se corre cuando
cambia \(H\) o \(c(t)\).

---

## 5. Lo que esta geometría deja ver

1. Un pico alto y estrecho = poder intenso, poco alcance (ciudad-templo).
2. Un pico alto y ancho = las dimensiones están llenas *y* \(\alpha\)
   deja que esa altura se vuelva radio (imperio-canon-flota).
3. Dos picos que se tocan = puerto. La sábana allí tiene un collado.
4. Un pico que se apaga (\(H\to 0\)) = la curva de nivel se contrae
   hasta desaparecer. No es que “se borre del mapa”: es que deja de
   levantar la sábana.

---

## 6. Relación con el fibrado discreto

| Capa anterior | Esta capa |
|---|---|
| \(W_C\subset R\times T\) | centro \(c_C(t)\in M\) |
| \(F_C(d)\) | componente \(s_{C,d}\) |
| acople \(e=(C_i,C_j,\ldots)\) | collado de \(\Phi\) entre dos picos |
| mandala de Wolters | cono + curvas de nivel |

El JSON discreto sigue siendo el índice. El cono es su realización
geométrica sobre la Tierra.

---

## 7. Archivos

- `conos_influencia.json` — centros, \(H\), \(R\), \(\alpha\)
- `sabana_conos_3d.png` — relieve de conos
- `sabana_curvas_nivel.png` — sábana + isobaras
- CGI: conos y sábana como objeto de estudio, no como mapa escolar
