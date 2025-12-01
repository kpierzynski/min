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

# Zajęcia VIII

---

## Problem

Jak wybrać drogę przejazdu (np. gps)?

Trasa $x$:

- czas przejazdu 0.6
- koszt 0.9
- bezpieczeństwo 0.7
- komfort 0.5

---

## Agregacja

- porównywanie obiektów
- redukcja danych
- tłumienie wartości odstających

---

## Agregacja

$Arg: [0,1]^n \rightarrow [0,1]$

<small>
Warunki:

- monotoniczność
- warunek identyczności $\forall_a:  Agr(a) = a$
- warunki brzegowe $Arg(0, \dotsc, 0) = 0$ oraz $Arg(1, \dotsc, 1) = 1$
  </small>

---

## Zadanie lab I

Zagreguj zbiór $ocena\ pozytywna = \frac{0.5}{o_1} + \frac{0.9}{o_2} + \frac{0.7}{o_3} + \frac{0.4}{o_4}$
za pomocą:

1. t-normy minimum
2. t-normy algebraicznej
3. t-normy Łukasiewicza
4. średnia ważona wektorem wag $[0.1, 0.5, 0.3, 0.1]$
5. OWA z wektorem wag $[0.1, 0.5, 0.3, 0.1]$

---

## Agregacja

<small>

| cel                                             | agregator           |
| ----------------------------------------------- | ------------------- |
| ocenić obiekt restrykcyjnie                     | t-norma             |
| ocenić obiekt łagodnie                          | t-konorma           |
| uśrednić wartości                               | średnie             |
| złagodzić działanie t-normy w kierunku średniej | miękka t-norma      |
| uwypuklić dane parametry                        | OWA, średnie ważone |
| tłumić wybrane rodzaje wielkości                | OWA                 |

</small>

---

## Model Bellmana-Zadeha

Podejmowanie decyzji, gdy:

- mamy cel do osiągnięcia
- mamy ograniczenia do spełnienia

$D = G \ast (C_1 \ast ... \ast C_i)$
$d\ast = arg_x\ max\ D(x)$

<small><small><small>
$\ast - agregator$
</small></small></small>

---

## Zadanie lab II

Wybierz najlepszego kandydata:

Zbiór celu:
$G = \{\frac{0.6}{k1​} , \frac{0.3}{k2}, \frac{0.9}{k3}​, \frac{1}{k4}​ \}$

<hr />

$C1 = \{\frac{0.9}{k1}, \frac{0.7}{k2}, \frac{0.6}{k3}, \frac{0.5}{k4} \}$
$C2 = \{\frac{0.2}{k1}, \frac{0.6}{k2}, \frac{0.2}{k3}, \frac{0.2}{k4} \}$
$C3 = \{\frac{0.7}{k1}, \frac{0.5}{k2}, \frac{0.7}{k3}, \frac{0.8}{k4} \}$
$C4 = \{\frac{0.3}{k1}, \frac{0.4}{k2}, \frac{0.6}{k3}, \frac{0.9}{k4} \}$

---

korzystając z agregatorów:
a) minimum
b) średniej ważonej z wagami $[1, 0.5, 1, 0.5, 0]$
c) OWA dla wektora $[0.1, 0.3, 0.4, 0.1, 0.1]$

---

# Zadanie I

Zaproponuj metodę wyboru najlepszego komputera z podanych w oparciu o model Bellmana-Zadeha.

Cel: wybrać komputer najlepszy według preferencji
$G = \{\frac{0.2}{asus​} , \frac{0.6}{hp}, \frac{0.4}{acer}​, \frac{0.5}{lenovo}, \frac{0.1}{dell}, \frac{0.2}{huawei}​ \}$

---

Ograniczenia:
$C_1$ - ma dobry CPU
$C_1 = \{\frac{0.4}{asus​} , \frac{0.6}{hp}, \frac{0.2}{acer}​, \frac{0.2}{lenovo}, \frac{0.1}{dell}, \frac{0.8}{huawei}​ \}$

$C_2$ - ma dobre GPU
$C_2 = \{\frac{0.2}{asus​} , \frac{0.7}{hp}, \frac{0.6}{acer}​, \frac{0.4}{lenovo}, \frac{1}{dell}, \frac{0.7}{huawei}​ \}$

$C_3$ - jest w przystępnej cenie
$C_3 = \{\frac{0.8}{asus​} , \frac{0.7}{hp}, \frac{0.6}{acer}​, \frac{0.4}{lenovo}, \frac{0.5}{dell}, \frac{0.1}{huawei}​ \}$

<small>

Użyj:
a) operatora agregacji średniej ważonej $[0.8, 0.5, 0.4, 0.9]$
b) innego wybranego agregatora.

</small>
