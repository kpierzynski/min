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

# Zajęcia XI

---

## Powtórka

---

## Zadanie lab

Czy można skonstruować podane $t$-normy? Jeśli nie - dlaczego? Jeśli tak - podaj przykład.
a) 0.3 $t$ 0 = 0
b) 0.6 $t$ 0.6 = 0.2
c) 1 $t$ 0.8 = 0.8
d) 0.4 $t$ 0.2 = 0.4

---

## Zadanie lab

Wyciągnij wniosek używając metody wnioskowania modus ponens. Użyj:

1. implikacji Łukasiewicza
2. implikacji Zadeha $I_Z(a,b) = max(1-a, min(a,b))$

Przesłanka: $A = \frac{0.6}{x_1} + \frac{1}{x_2} + \frac{0.5}{x_3} + \frac{0.4}{x_4}$
Wniosek: $B = \frac{1}{y_1} + \frac{0.4}{y_2} + \frac{0.3}{y_3}$

Fakt: $A' = \frac{0.5}{x_1} + \frac{0.9}{x_2} + \frac{0.4}{x_3} + \frac{0.3}{x_4}$

---

## Zadanie lab

<small><small>

Zdzisiu wybiera telefon. Do wyboru są: $t_1$, $t_2$, $t_3$, $t_4$.
$t_1$ jest nawet ładny, $t_2$ jest odrzucający, $t_3$ ujdzie, $t_4$ jest ok.

Musi jednak wziąć pod uwagę:

- $t_1$ jest drogi, $t_2$ jest tani, $t_3$ jest optymalnie wyceniony, $t_4$ trochę przeceniony;
- $t_1$ i $t_2$ mają mało pamięci, $t_3$ ma sensowne minimum pamięci, a $t_4$ ma jej dużo;
- $t_1$ i $t_2$ nie mają GPS, a Zdzisław chciałby go raczej mieć.

Dla Zdzisia, ważny jest ogólny wygląd, bardzo ważna jest cena, a pamięć i gps jest średnio ważne.

Wybierz telefon dla Zdzisława, stosując model Bellmana-Zadeha, opisz swoje założenia.

</small></small>

---

## Zadanie lab

<small><small>

Dane są informacje na temat dań w restauracji:

| Danie | Cena | Czas wykonania (min) | Liczba kalorii (kcal) | Jakość (0-5) |
| ----- | ---- | -------------------- | --------------------- | ------------ |
| 1     | 15   | 10                   | 300                   | 4            |
| 2     | 20   | 15                   | 600                   | 5            |
| 3     | 22   | 20                   | 500                   | 5            |
| 4     | 6    | 5                    | 1000                  | 1            |
| 5     | 10   | 6                    | 900                   | 1            |
| 6     | 12   | 7                    | 800                   | 2            |

Ile jest:
a) dań wysokiej jakości?
b) drogich, niskokalorycznych dań?
Użyj $f_{1, t}$, dobierz $t$ i uzasadnij krótko wybór.

</small></small>

---

## Zadanie lab

<small><small>

Dane są komputery $(k_1, k_2, k_3)$ oraz preferencja użykownika $u$:

| komputer | $a_1$ | $a_2$ | $a_3$ | $a_4$ |
| -------- | ----- | ----- | ----- | ----- |
| $k_1$    | 0.9   | 0.8   | 0.1   | 0.5   |
| $k_2$    | 0.3   | 1     | 0.8   | 0.1   |
| $k_3$    | 0.6   | 0.3   | 0     | 1     |
|          |
| u        | 0.1   | 0.6   | 0.3   | 0.7   |

Znajdź komputer, który najlepiej spełnia preferencję $u$ korzystając ze współczynnika Jaccarda.

</small></small>

---

## Zadanie lab

<small><small>

Dane są zmienne:

- wypełnienie zbiornika (w litrach)
  - pusty: $Tr(0,0,40,100)$
  - pełny: $Tr(40,70,100,100)$
- prędkość napełniania (w litrach na minutę)
  - niska: $Tr(0,0,10,140)$
  - wysoka: $Tr(100,120,140,140)$
- zmiana otwartości zaworu:
  - mała: $Tr(-10,-10,-5,0)$
  - utrzymuj: $T(-5,0,5)$
  - duża: $Tr(0,5,10,10)$

</small></small>

---

<small><small>

Dane są reguły:

<table>
  <tr>
    <th>wypełnienie\przepływ</th>
    <th>słaby</th>
    <th>dobry</th>
  </tr>
  <tr>
    <th>pusty</th>
    <td>duża</td>
    <td>utrzymuj</td>
  </tr>
  <tr>
    <th>pełen</th>
    <td>utrzymuj</td>
    <td>mała</td>
  </tr>
</table>

Przdstaw graficznie stan sterownika dla:

- wypełnienie = 55L
- prędkość = 120L/min

</small></small>

---

## Zadanie lab

<small><small>

Uruchomienie dodatkowego serwera z aplikacją trwa około 1 godziny (A), a dotarcie devopsa do serwerowni zajmuje przeciętnie 1.5 godzin (B). Szef chce, aby o 10:30 nowa instancja aplikacji była już uruchomiona. O której devops powinien wyjść z domu?

$A = \{ \frac{0.2}{0.5h} + \frac{1}{1h} + \frac{0.5}{1.5h} + \frac{0.1}{2h} \}$
$B = \{ \frac{0.4}{1h} + \frac{1}{1.5h} + \frac{0.6}{2h} \}$

</small></small>
