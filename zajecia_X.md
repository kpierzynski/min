---
marp: true
theme: uncover
class: invert
author: Konrad
math: mathjax
---

# Modelowanie i przetwarzanie informacji nieprecyzyjnej

---

# Zajęcia X

---

## Miara podobieństwa

$$
S: F(U) \times F(U) \rightarrow [0,1]
$$

Określa, jak bardzo dwa zbiory rozmyte są do siebie podobne.

- $S(A,B) = S(B,A)$
- $S(A,A) = 1$

---

## Współczynnik Jaccarda

Dla zbiorów rozmytych $A$ i $B$:

$$
S_J(A,B) = \frac{\sum_{i=1}^n \min(A(x_i), B(x_i))}{\sum_{i=1}^n \max(A(x_i), B(x_i))}
$$

---

## Zadanie lab I

Dane są zbiory rozmyte:

$$
A = \{0.2/a, 0.6/b, 0.9/c, 0.4/d\}
$$

$$
B = \{0.5/a, 0.4/b, 0.3/c, 0.1/d\}
$$

Oblicz współczynnik Jaccarda $S_J(A,B)$
Czy zbiory są podobne?

---

## Zadanie I

Dla zbiorów:

$$
A = \{0.7/x_1, 0.2/x_2, 0.5/x_3, 0.9/x_4\}
$$

$$
B = \{0.6/x_1, 0.9/x_2, 0.1/x_3, 0.9/x_4\}
$$

1. Oblicz miarę Jaccarda

---

## Miara odległości

$$
D: F(U) \times F(U) \rightarrow [0, \infty)
$$

która określa jak bardzo różne są dwa zbiory rozmyte.

- $D(A,B) = D(B,A)$
- $D(A,A) = 0$

---

## Odległość euklidesowa

$$
D_2(A,B) = \sqrt{\sum_{i=1}^n (A(x_i) - B(x_i))^2}
$$

---

## Zadanie lab II

Dla zbiorów:

$$
A = \{0.4/a, 0.6/b, 0.1/c, 0.9/d \}
$$

$$
B = \{0.2/a, 0.9/b, 0.3/c, 0.1/d \}
$$

Oblicz odległość euklidesową $D_2(A,B)$

---

## Zadanie II

Dla zbiorów:

$$
A = \{0.8/x_1, 0.3/x_2, 0.4/x_3, 0.1/x_4, 1/x_5 \}
$$

$$
B = \{0.5/x_1, 0.1/x_2, 0.9/x_3\, 0.2/x_4, 0.9/x_5 \}
$$

Oblicz odległość Czebyszewa

---

## Miara relacyjna

Opisuje relację pomiędzy zbiorami, np.:

- stopień inkluzji
- stopień spełnienia wymagań
- zgodność z relacją wzorcową

Przykład – inkluzja:

$$
I(A,B) = \inf_x (A(x) \Rightarrow B(x))
$$

---

## Zadanie lab III

Dane są zbiory:

$$
A = \{0.5/a, 1/b, 0.6/c\}
$$

$$
B = \{0.7/a, 0.8/b, 0.4/c\}
$$

Oblicz stopień inkluzji $I(A,B)$, użyj implikacji Łukasiewicza

---

## Zadanie III

Dla zbiorów:

$$
A = \{0.9/x_1, 0.4/x_2, 0.3/x_3, 1/x_4, 0.8/x_5 \}
$$

$$
B = \{0.6/x_1, 0.7/x_2, 0.4/x_3, 1/x_4, 0.9/x_5 \}
$$

Oblicz inkluzję $I(B,A)$ używając implikacji Goguen’a.  
Porównaj wynik z inkluzją $I(A,B)$.

---

## Całka rozmyta

Miara rozmyta mówi jak ważne są podzbiory,  
ale nie agreguje wartości liczbowych.

Całka rozmyta łączy:

- miarę rozmytą $\mu$
- wartości kryteriów $h(x)$

w jedną ocenę globalną.

---

## Całka Choqueta

- sortujemy wartości $h(x)$ malejąco
- dodajemy je z wagami zależnymi od **kombinacji elementów**
- uwzględniamy **synergię i redundancję**

<hr />

- $h$ to oceny spełnienia danego kryterium (np. cena, osiągi, spalanie)
- $\mu$ to stopie ważności kryteriów i ich kombinacji (cena sama nie jest ważna, ale cena i osiągi razem są istotne)

---

## Zadanie lab IV

Dane są kryteria:

$$
h = (0.2, 0.5, 0.9)
$$

oraz miara rozmyta:

$$
\mu(\{1\})=0.2,\ \mu(\{2\})=0.3,\ \mu(\{3\})=0.4
$$

$$
\mu(\{2,3\})=0.8,\ \mu(\{1,2,3\})=1
$$

Oblicz całkę Choqueta

---

## Zadanie IV

Dane są kryteria:

$$
h = (0.6, 0.5, 0.8)
$$

oraz miara rozmyta:

$$
\mu(\{1\})=0.1,\ \mu(\{2\})=0.2,\ \mu(\{3\})=0.3
$$

$$
\mu(\{2,3\})=0.7,\ \mu(\{1,2,3\})=1
$$

Oblicz całkę Choqueta
