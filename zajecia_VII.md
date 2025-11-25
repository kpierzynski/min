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

# Zajęcia VII

---

## Problem

Jak wyszukiwać w sposób rozmyty?

---

## Przypomnienie operacji

$µ_{A\cup B} (x) = max(µ_A(x), µ_B(x))$
$µ_{A\cap B} (x) = min(µ_A(x), µ_B(x))$

---

## Zadanie lab I

Dla danych relacji $K$ i $L$:

<div class="grid grid-cols-2 gap-4">
<div>

| a      | b     | $\mu$ |
| ------ | ----- | ----- |
| $a_1%$ | $b_1$ | 0.9   |
| $a_2%$ | $b_1$ | 1     |
| $a_2%$ | $b_2$ | 0     |
| $a_3%$ | $b_2$ | 0.7   |

</div>
<div>

| a      | b     | $\mu$ |
| ------ | ----- | ----- |
| $a_1%$ | $b_1$ | 0.4   |
| $a_1%$ | $b_2$ | 0.6   |
| $a_2%$ | $b_2$ | 0.2   |
| $a_1%$ | $b_3$ | 0.8   |

</div>
</div>

Oblicz $K \cup L$, $K \cap L$, $K - L$.

---

## Zadanie lab II

<small>

$\mu_{proj_X(t)} = sup_{T(X)=t(X)} \mu_R(T)$

Dana jest relacja $duza\ produkcja$:

| id  | factory  | production | type    | $\mu$ |
| --- | -------- | ---------- | ------- | ----- |
| 0c6 | Poznań   | 1.1M       | metal   | 0.8   |
| 1fa | Warszawa | 0.9M       | metal   | 0.7   |
| 224 | Łódź     | 2.5M       | plastic | 1     |
| 18d | Rzeszów  | 0.2M       | metal   | 0.2   |
| 45e | Gdańsk   | 1.9M       | plastic | 0.9   |

Dokonaj projekcji relacji na zbiór $A = \{type\}$
</small>

---

## Zadanie lab III

Dokonał złączenia $G * H$ relacji $G$ i $H$

<div class="grid grid-cols-2 gap-4">
<div>

| a      | b     | $\mu$ |
| ------ | ----- | ----- |
| $a_1%$ | $b_1$ | 0.9   |
| $a_2%$ | $b_1$ | 0.6   |
| $a_2%$ | $b_2$ | 0.7   |
| $a_3%$ | $b_2$ | 0.8   |

</div>
<div>

| b      | c     | $\mu$ |
| ------ | ----- | ----- |
| $b_1%$ | $c_1$ | 1     |
| $b_2%$ | $c_1$ | 0.9   |
| $b_2%$ | $c_2$ | 0.8   |
| $b_3%$ | $c_2$ | 0.7   |

</div>
</div>

---

## Implikacja między relacjami

Iloraz $P ÷ S$ mówi, w jakim stopniu relacja $P$ spełnia wymagania określone przez relację $S$.

---

<small>

Algorytm:

1. Z relacji $P(a, o)$ wybieramy krotki o tych wartościach $a$, dla których istnieją wszystkie krotki $o$ z relacji $S(o)$.

- Jeśli dla danego $a$ brakuje krotki $(a,o)$, to pomijamy $a$.

2. Dla każdego $a$ sprawdzamy, czy $\mu_S(o) \leq \mu_P(a,o)$.

- Jeśli tak: $\mu_{P÷S​}(a) = min_o\ \mu_P(a,o)$
- Jeśli nie: $\mu_{P÷S​}(a) = min_o\ I_G(\mu_S(o), \mu_P(a,o))$

$$
I_G(p,q) =
\begin{cases}
1, & p \le q,\\[6pt]
q, & p > q.
\end{cases}
$$

</small>

---

## Zadanie lab IV

Oblicz $E÷F$

<small>

<div class="grid grid-cols-2 gap-4">
<div>

| X     | Y     | mi    |
| ----- | ----- | ----- |
| $x_1$ | $y_1$ | $1$   |
| $x_1$ | $y_2$ | $0.4$ |
| $x_1$ | $y_3$ | $0.7$ |
| $x_2$ | $y_1$ | $0.2$ |
| $x_2$ | $y_2$ | $1$   |
| $x_2$ | $y_3$ | $0.7$ |
| $x_3$ | $y_2$ | $0.4$ |

</div>
<div>

| Y     | mi    |
| ----- | ----- |
| $y_1$ | $0.5$ |
| $y_2$ | $0.4$ |
| $y_3$ | $0.7$ |

</div>
</div>

</small>

---

## Zadanie I

Dane są klawiatury:

<small>
<small>

| nr  | model            | cena (€) | czas reakcji (ms) | poziom hałasu (dB) |
| --- | ---------------- | -------- | ----------------- | ------------------ |
| 1f2 | KeyPro Rapid     | 89       | 1.5               | 46                 |
| 3a2 | MechaStorm TKL   | 120      | 1.0               | 58                 |
| 443 | SilentType S     | 45       | 8.0               | 32                 |
| ade | Aurora RGB K700  | 99       | 2.0               | 52                 |
| 7f7 | OfficeLite Mini  | 29       | 12.0              | 38                 |
| dad | Titan Switch Pro | 150      | 0.9               | 60                 |
| 902 | ClassicBoard 104 | 19       | 18.0              | 55                 |

</small>
</small>

---

1. Zamodeluj termy $tania$, $szybka$, $glosna$ dla zmiennych lingwistycznych
2. Korzystając z podanych niżej t-norm określ $top_3$ tanich, szybkich i cichych klawiatur:

- t-norma minimm
- t-norma algebraiczna
- t-norma Łukasiewicza
