---
marp: true
theme: uncover
class: invert
author: Konrad
---

# Modelowanie i przetwarzanie informacji nieprecyzyjnej

---

### Konrad Pierzyński

konrad.pierzynski@amu.edu.pl
konpie1

---

# Harmonogram

| Data     |       |       |       |       |       |       |
| -------- | ----- | ----- | ----- | ----- | ----- | ----- |
| ~~7.10~~ | 14.10 | 21.10 | 28.10 | 4.11  | 18.11 | 25.11 |
| 2.12     | 9.12  | 16.12 | 13.01 | 20.01 | 27.01 | 3.02  |
| 4.02     |

---

# Warunki zaliczenia

Uzyskanie pozytywnej oceny z zadań i kolokwium według skali:

| bdb  | db+  | db   | dst+ | dst  |
| ---- | ---- | ---- | ---- | ---- |
| >90% | >80% | >70% | >60% | >50% |

Gdzie kolokwium to $\frac{2}{3}$ oceny, a zadania to $\frac{1}{3}$.

Termin oddania zadań to tydzień.

---

# Zajęcia I

---

## Problem

Budujemy urządzenie, sprawdza temperaturę na zewnątrz i wyświetla trzy możliwe stany: "zimno", "neutralnie" oraz "ciepło".

Czujnik dokonuje pomiaru: 15.52°C. Co należy wyświetlić?

---

## Inny problem

Program przyjmuje liczbę na wejściu od użytkownika. Po wpisaniu około 17, program powinien przejść dalej. Jak sprawdzić "około 17"?

---

## Zbiory

$A = \{x | x > 12\}$

$$
\mu_A(x) =
\begin{cases}
1 & \text{jesli } x \in A, \\
0 & \text{jesli } x \notin A.
\end{cases}
$$

, gdzie $\mu_A$ to funkcja **przynależności**.

---

## Zbiory rozmyte

$$
\mu_A(x): U → [0,1]
$$

$$
\mu_A(x) =
\begin{cases}
0 & \text{jesli } x < 0, \\
\frac{x}{2} & \text{jesli } 0 < x < 2, \\
1 & \text{jesli } x > 2.
\end{cases}
$$

---

## Zadanie lab I

Przedstaw powyższą funkcję przynaleźności w sposób graficzny.

---

## Zadanie lab II

Czy podana funkcja może być funkcją przynależności dla zbioru rozmytego?

$$
\mu_A(x) =
\begin{cases}
0 & \text{jesli } x < 0, \\
-\frac{1}{3}x^{2\ }+\frac{4}{3}x & \text{jesli } 0 < x < 3, \\
1 & \text{jesli } x > 3.
\end{cases}
$$

---

## Zadanie lab III

Zaproponuj własną funkcję przynależności dla zbioru "osób wysokich". Przedstaw ją w postaci graficznej.

---

## Zadanie I

Dla uniwersum $U = \{\, x \in \mathbb{N} \mid 0 \leq x \leq 10 \,\}$, przedstaw pojęcie "około 4":

1. Skonstruuj funkcję przynależności,
2. Przedstaw ją w sposób graficzny,
3. Określ nośnik oraz jądro zbioru rozmytego,
4. Czy zbiór jest typu "singleton"? Udowodnij swoją odpowiedź.
