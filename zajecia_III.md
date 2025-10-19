---
marp: true
theme: uncover
class: invert
author: Konrad
---

# Modelowanie i przetwarzanie informacji nieprecyzyjnej

---

# Zajęcia III

---

## Problem

Umiemy odpowiedzieć na pytania:
"Która pralka jest tania ($T$) i energooszczędna ($E$)?"

Niestety, spójniki "i" oraz "lub" nie wystarczają aby opisać wszystkie pytania.

---

## Relacje rozmyte

Relacja to funkcja:

$$R(x,y): X \times Y \rightarrow [0,1] $$

$$R(x,y) = \{((x,y), \mu_R(x,y)): x \in X, y \in Y, \mu_R(x,y) \in [0,1]\}$$

---

$A = \{ s_1, s_2, s_3 \}$
$B = \{  s_4, s_5 \}$

| samochód | max. prędkość | śr. spalanie |
| -------- | ------------- | ------------ |
| $s_1$    | 320           | 23           |
| $s_2$    | 150           | 8            |
| $s_3$    | 210           | 9            |
|          |               |              |
| $s_4$    | 150           | 3            |
| $s_5$    | 240           | 14           |

---

## Zadanie lab I.1

Zaproponuj relację "samochód A jadący maksymalnie tyle samo co samochód B"

---

## Zadanie lab I.2

Zaproponuj relację $R$: "samochód A jadący maksymalnie podobnie co samochód B"

---

## Zadanie lab I.3

Zaproponuj nową relację $T$: "samochód A o większym spalaniu niż samochód B"

---

## Zadanie lab I.4

Na jakie pytanie odpowie iloczyn $T \cap R$?
A na jakie $\neg T \cup R$

---

## Zadanie dom I

Wiedząc, że
$A = \{ Poznan, Warszawa, Wroclaw \}$ $B = \{ Gdansk, Poznan \}$

| miasto | Poznań | Warszawa | Wrocław |
| ------ | ------ | -------- | ------- |
| Gdańsk | 312km  | 418km    | 485km   |
| Poznań | 0km    | 311km    | 183km   |

---

1. Zamodeluj pojęcie duże miasto oraz relację bliskości
2. Odpowiedz na pytanie: "w jakim stopniu miasto A jest blisko dużego miasta B?"
3. Czy można powiedzieć, że Warszawa jest daleko dużych miast? Dlaczego tak/nie?
4. Jaka jest wysokość zbioru rozmytego duże miasto?
5. Czy zbiór duże miasto jest normalny?

<sup><sub>(Zauważ, że tutaj nie ma dwóch relacji, tylko relacja oraz zbiór rozmyty. Skorzystaj ze złożenia relacji rozmytej ze zbiorem rozmytym. Załóż t-normy i t-konormy Łukasiewicza)</sub></sup>

---

## Wartościowanie

Proces przypisania wartości logicznej formułom zdaniowym.

$[[p]]$ - wartość logiczna zdania $p$
$\neg_m$ - negacja w logice wielowartościowej

---

| logika       | zbiory      |
| ------------ | ----------- |
| koniunkcja   | iloczyn     |
| alternatywa  | suma        |
| negacja      | dopełnienie |
| implikacja   | inkluzja    |
| równoważność | równość     |

---

## Zadanie lab II

Zapisz tabelę wartości logicznych dla implikacji Łukasiewicza w $Ł_3$

$a \rightarrow_Ł b = 1 \land (1-a+b)$

---

## Zadanie lab III

Jaka jest wartość logiczna zdania w $Ł_\infty$ dla $[[p]] = 0.2$ oraz $[[q]] = 0.3$ zdań:

1. $[(p \Rightarrow_m q)\ \&_m \ (q \Rightarrow_m p)] \Rightarrow_m p$
2. $[(p\ \&_m \ q)\ \bot_m \ q] \Rightarrow_m p$

$a \rightarrow_Ł b = 1 \land (1-a+b)$

---

## Zadanie lab IV

Udowodnij, że w logice Łukasiewicza $Ł_\infty$

1. działo prawo podwójnej negacji
2. działa zasa sprzecznośći
3. nie działa prawo wyłączonego środka

---

## Zadanie II

Niech $[[p]], [[q]] \in \{0,1\}$. Wykaż, że wartości logiczne zdań:

1. $[[p\ \&_m \ q]]$
2. $[[p\ \bot_m \ q]]$
3. $[[p\ \Rightarrow_m \ q]]$
   w logice wielowartościowej $Ł_\infty$ są równoważne logice dwuwartościowej

---

## Zadanie III

Wykaż, że w ($Ł_\infty$):
$[[ \neg_m p\ \bot_m \ q]]\ \neq [[p \Rightarrow_m q]]$

---

## Zadanie IV

Sprawdź, czy w $Ł_\infty$ działa prawo **modus ponendo ponens**
