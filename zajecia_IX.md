---
marp: true
theme: uncover
class: invert
author: Konrad
math: mathjax
style: @import url('https://unpkg.com/tailwindcss@^2/dist/utilities.min.css');
---

# Modelowanie i przetwarzanie informacji nieprecyzyjnej

---

# Zajęcia IX

---

## Problem

Ile jest gruszek w pudle?

<img src="pear.png" class="w-5/12">

---

## Problem

Ile jest dużych gruszek w pudle?

<img src="pear.png" class="w-5/12">

---

## Liczebność zbiorów rozmytych

Prosta rozmyta liczebność $|A|$

$|A| = |A_t|,\ gdzie\ A_t = \{ x \in U: A(x) \ge t\}$

---

## Zadanie lab I

Jaka jest liczebność skalarna zbioru $A$ dla $t=\frac{1}{2}$?

$A = \{ \frac{1}{Polska}, \frac{0.0}{Rosja}, \frac{0.3}{Niemcy}, \frac{0.9}{Czechy}, \frac{0.8}{Slowacja}  \}$

---

## Liczność skalarna w ogólności

Liczność: $\sigma: FFS \rightarrow [0,\inf)$

1. Zgodność
   $\sigma(\frac{1}{x}) = 1$
2. Monotoniczność
   $a \le  b \implies \sigma(\frac{a}{x}) \le \sigma(\frac{b}{y})$
3. Addytywność
   $A \cap B = \varnothing \implies \sigma(A \cup B) = \sigma(A) + \sigma(B)$

---

Ponadto, musi istnieć funkcja niemalejąca $f: [0,1] \rightarrow [0,1]$, taka, że:

1. $f(0) = 0$
2. $f(1) = 1$
   stąd: $\sigma(A) = \sum_{x \in supp(A)} f(A(x))$

---

## Zadanie lab II

W zadaniu lab I, jaka została zastosowana funkcja $f$?

---

## Funkcje $f$

$$
f_{1,t}(x) = \begin{cases}
  1 & x \ge t, \\
  0 & otherwise
\end{cases}
$$

$$
f_{2,t}(x) = \begin{cases}
  1 & x > t, \\
  0 & otherwise
\end{cases}
$$

$$f_{3,p}(x) = x^p \ \  p > 0$$

$$
f_{5,t,p}(x) = \begin{cases}
  x^p & x \ge t, \\
  0 & otherwise
\end{cases}
$$

---

## Zadanie lab III

Dane są firmy $\{c_1\,c_2,c_3,c_4,c_5\}$:

- tani abonament: $A = \{\frac{1}{c_2}, \frac{0.4}{c_3}, \frac{0.1}{c_4}, \frac{0.3}{c_5}\}$
- długa umowa: $B = \{\frac{0.2}{c_1}, \frac{1}{c_2}, \frac{0.1}{c_3}, \frac{0.2}{c_4}, \frac{0.2}{c_5}\}$
- dużo minut: $C = \{\frac{1}{c_1}, \frac{0.7}{c_3}, \frac{0.2}{c_4}, \frac{0.7}{c_5}\}$

---

1. Ile firm oferuje tani abonament?
   a) $f = id$
   b) $f = f_{1,t}\ ,\ \ gdzie\ t=0.2$

2. Ile firm oferuje długoterminową umowę z dużą ilością minut?
   a) $f = id$
   b) $f = f_{1,t}\ ,\ \ gdzie\ t=0.2$
   c) $f = f_{2,t}\ ,\ \ gdzie\ t=0.2$

---

## Liczność względna

$\sigma_f(A | B) =\frac{\sigma_f(A \cap_t B)}{\sigma_f(B)}$

"jak bardzo A jest w B"

---

## Zadanie I

<small>

$U = \{ Anna, Bartek, Celina, Dawid \}$

| osoba  | szczupła | umiarkowanie wysoka |
| ------ | -------- | ------------------- |
| Anna   | 0.9      | 0.6                 |
| Bartek | 0.4      | 0.7                 |
| Celina | 0.8      | 0.3                 |
| Dawid  | 0.2      | 0.1                 |

Na ile osoby szczupłe są jednocześnie umiarkowanie wysokie?
(patrzymy na stosunek, które osoby są szczupłe, a zarazem umiarkowanie wysokie)
$t$-norma minimum, $f = f_{5,0.2,1}$

</small>

---

## Zadanie II

W odniesieniu do Zadanie lab III, ile firm oferuje drogi abonament i mało minut?
Użyj $f = f_{5,0.2,1}$ oraz $f = id$

---

## Kwantyfikatory lingwistyczne

1. Klasyczne: $\forall$ i $\exists$
2. Rozmyte:

- absolutne: (np. około 17, więcej niż 17)
- względne: (np. około połowy, większość)

---

## Kwantyfikator absolutny

Liczba rozmyta: $Q: \mathbb{N} \rightarrow [0,1]$

"ile kontretnie?"

---

## Kwantyfikator względny

Liczba rozmyta: $Q: [0,1] \rightarrow [0,1]$

"jaka proporcja?"

---

## Zdania typu I dla kwantyfikatora względnego

$[[Qx\ jest\ A]]$

$Q$ - kwantyfikator
$x$ - elementy ze zbioru
$A$ - zbiór rozmyty

$[[Qx\ jest\ A]] = Q(\sigma_f(A | 1_U )) = Q(\frac{1}{|U|} \sum_{x \in supp(A)} f(A(x))$

Q: "Większość" x: "gruszek" A: "jest dużych"

---

## Zdania typu II dla kwantyfikatora względnego

$[[Q\ Bx\ jest\ A]]$

$Q$ - kwantyfikator
$x$ - elementy ze zbioru
$B$ - również zbiór rozmyty, tzw. kwalifikator
$A$ - zbiór rozmyty

$[[Q\ Bx\ jest\ A]] = Q(\sigma_f(A | B )) = Q(\frac{\sigma_f(A \cap_t B)}{\sigma_f(B)})$

Q: "Około 25%" B: "dojrzałych" x: "gruszek" A: "jest mała"

---

## Zdania typu I dla kwantyfikatora absolutnego

$[[Qx\ jest\ A]]$

$[[Qx\ jest\ A]] = Q(\sigma_f(A))$

Q: "Około 4" x: "gruszki" A: "są duże"

---

## Zdania typu II dla kwantyfikatora absolutnego

$[[Q\ Bx\ jest\ A]]$

$[[Q\ Bx\ jest\ A]] = Q(\sigma_f(A \cap_t B))$

Q: "Około 3" B: "pachnących" x: "gruszek" A: "jest średnia"

---

## Zadanie lab IV

W odniesieniu do Zadanie lab III, określ prawdziwość zdania:
"Większość ofert jest droga", gdzie większość zamodeluj jako $Tr(0.3,0.8,1,1)$ oraz $f = id$

---

## Zadanie III

W odniesieniu do Zadanie lab III, określ prawdziwość:

1. "Około połowa ofert ma dość dużo minut", gdzie około połowa zamodeluj jako $T(0.3,0.5,0.7)$ oraz $f = f_{5,0.1,1}$
2. "Około 2 długich ofert ma tani abonament", gdzie około 2: $T(0,2,4)$, $f = id$, $t$-norma Łukasiewicza

Dla każdego przykładu określ rodzaj kwantyfikatora oraz typ zdania ($I$/$II$).

---

## Liczba rozmyta

Liczba rozmyta to szczególny zbiór rozmyty, który:

- ma ograniczony nośnik w dziedzinie $\mathbb{R}$
- jest normalny
- jest wypukły

---

## Zadanie lab V

Narysuj kilka przykładów liczb rozmytych oraz zbiorów rozmytych, które nie są liczbami rozmytymi.

---

## Operacje na liczbach rozmytych

$$
\mu_{A+B}(z) = \sup_{z = x + y} \; t\!\left( \mu_A(x), \mu_B(y) \right)
$$

$$
\mu_{A-B}(z) = \sup_{z = x - y} \; t\!\left( \mu_A(x), \mu_B(y) \right)
$$

$$
\mu_{A \times B}(z) = \sup_{z = x \cdot y} \; t\!\left( \mu_A(x), \mu_B(y) \right)
$$

$$
\mu_{A / B}(z) = \sup_{z = x / y} \; t\!\left( \mu_A(x), \mu_B(y) \right)
$$

---

## Zadanie lab VI

Dane są liczby rozmyte:
$A = \{\frac{0.2}{3}, \frac{1}{4}, \frac{0.6}{5} \}$
$B = \{\frac{0.5}{1}, \frac{1}{2} \}$

Oblicz $A + B$ dla $t$-normy minimum.

---

## Zadanie IV

Dane są liczby rozmyte:
$A = \{\frac{0.1}{3}, \frac{1}{4}, \frac{0.7}{5}, \frac{0.3}{6} \}$
$B = \{\frac{0.5}{2}, \frac{1}{3}, \frac{0.1}{4} \}$

Oblicz $A + B$ i $A/B$ dla $t$-normy minimum.
