---
marp: true
theme: uncover
class: invert
author: Konrad
---

# Modelowanie i przetwarzanie informacji nieprecyzyjnej

---

# Zajęcia II

---

## Operacje

Na zbiorach rozmytych można wykonywać operacje, analogicznie do klasycznych zbiorów.

---

## Zadanie lab I

|                              |                           |
| ---------------------------- | ------------------------- |
| Dopełnienie zbioru rozmytego | $µ_{A'} (x) = 1 − µ_A(x)$ |
|                              |                           |

Znajdź dopełnienie zbioru rozmytego $T(2,3,5)$ dla $U = \{\, x \in \mathbb{R} \mid 0 \leq x \leq 10 \,\}$, przedstawiając je graficznie.

---

## Zadanie lab II

|                        |                                         |
| ---------------------- | --------------------------------------- |
| Suma zbiorów rozmytych | $µ_{A\cup B} (x) = max(µ_A(x), µ_B(x))$ |
|                        |                                         |

Znajdź sumę dla zbiorów:
$A = \{ \frac{0.4}{a}, \frac{0.6}{b}, \frac{0.9}{c}, \frac{0.1}{d} \}$
$B = \{ \frac{0.5}{b}, \frac{1}{c}, \frac{0.1}{d}, \frac{0.3}{e} \}$

---

## Zadanie lab III

|                           |                                         |
| ------------------------- | --------------------------------------- |
| Iloczyn zbiorów rozmytych | $µ_{A\cap B} (x) = min(µ_A(x), µ_B(x))$ |
|                           |                                         |

Znajdź iloczyn zbiorów rozmytych:
$C = \{ \frac{0.4}{a}, \frac{0.6}{b}, \frac{0.9}{c}, \frac{0.1}{d} \}$
$D = \{ \frac{0.5}{b}, \frac{1}{c}, \frac{0.1}{d}, \frac{0.3}{e} \}$

---

## Zadanie lab IV

|                           |                                         |
| ------------------------- | --------------------------------------- |
| Różnica zbiorów rozmytych | $µ_{A-B} (x) = min(µ_A(x), 1 - µ_B(x))$ |
|                           |                                         |

Znajdź różnicę zbiorów rozmytych:
$E = \{ \frac{0.5}{b}, \frac{0.4}{c}, \frac{0.3}{d}, \frac{0.2}{e} \}$
$F = \{ \frac{1}{a}, \frac{0.5}{b}, \frac{0.4}{c}, \frac{0.3}{d}, \frac{0.2}{e} \}$

---

## Zadanie lab V.1

Dane są cztery pralki $p,q,r,s$ o cenach odpowiednio $1000, 1100, 1300, 1700$ i klasami energetycznymi $D, C, A, B$.

Która pralka jest tania ($T$) i energooszczędna ($E$)?

---

## Zadanie lab V.2

Wyznacz $T \cup E$. Oblicz $supp(T \cup E)$, $ker(T \cup E)$ i t-przekrój dla $t=0.8$.

---

## Logiczne "i" oraz "lub"

|              |                         |
| ------------ | ----------------------- |
| Logiczne AND | $t$-norma               |
| Logiczne OR  | $t$-konorma ($s$-norma) |

---

## Warunki t-normy

1. Komutatywność:
   $t(a,b) = t(b,a)$
2. Monotoniczność:
   jeśli $a_1 ≤ a_2$ i $b_1 ≤ b_2$, to $t(a_1, b_1) ≤ t(a_2,b_2)$
3. Asocjatywność:
   $t(a, t(a,c)) = t(t(a,b),c)$
4. Jedynka neutralna:
   $t(a,1) = a$

---

## Warunki t-konormy

4. Zero neutralne:
   $s(a,0) = a$

---

## Zadanie I

Dany jest zbiór samochodów $S = \{ x_1, x_2, x_3, x_4, x_5 \}$

Wsród tych samochodów wyszczególniamy zbiór szybkich samochodów:
$A = \{ \frac{0.9}{x_1}, \frac{1}{x_2}, \frac{0.5}{x_3}, \frac{0.6}{x_4} \}$

oraz zbiór samochodów dużo palących:
$B = \{ \frac{0.7}{x_1}, \frac{0.2}{x_2}, \frac{0.4}{x_3}, \frac{0.5}{x_4}, \frac{0.1}{x_5} \}$

---

1. Znajdź zbiór samochodów szybkich i mało palących. Skorzystaj z $t$-normy Łukasiewicza
2. Znajdź zbiór samochodów szybkich lub dużo palących. Skorzystaj z $t$-konormy Yagera dla $p=2$
3. Dla zbiorów z podpunktów 1 oraz 2, określ nośnik oraz jądro zbioru.

---

## Zadanie II

Sprawdź, czy funkcja $t(a,b) = ab^2$ może być $t$-normą? Udowodnij swoją odpowiedź.
