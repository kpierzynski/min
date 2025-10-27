---
marp: true
theme: uncover
class: invert
author: Konrad
---

# Modelowanie i przetwarzanie informacji nieprecyzyjnej

---

# Zajęcia IV

---

## Zmienna lingwistyczna

Pojęcie, które próbujemy zamodelować, np.
$wzrost$, $temperatura$

Dla wzrostu, $\{niski, średni, wysoki\}$ to zbiory rozmyte.

---

## Zadanie lab I

Zamodeluj zmienną lingwistyczną $wzrost$ i przedstaw ją graficznie.
Zastosuj 3 wyżej wymienione termy.

Podpowiedź: "średni" = "nie niski" i "nie wysoki"
$A' \cap B' = (A \cup B)'$

---

## Zadanie I

Zamodeluj zmienną lingwistyczną $temperatura$ dla przedziału od 0°C do 40°C z 3 termami:
zimno, ciepło, gorąco.

- Określ uniwersum
- Przedstaw funkcje przynależności dla każdego z termów
- Zamodeluj dodatkowy term: mniej więcej ciepło (skorzystaj z rozrzedzenia)

---

## Wnioskowanie klasyczne

- modus ponens

|            | modus ponens |
| ---------- | ------------ |
| implikacja | p => q       |
| przesłanka | p            |
| wniosek    | q            |

Czyli jeśli pierwsze zdanie mówi, że coś wynika z czegoś, a drugie potwierdza ten warunek, to wniosek musi być prawdziwy.

---

|            |                                        |
| ---------- | -------------------------------------- |
| Implikacja | Jeśli pada deszcz, to ulica jest mokra |
| Przesłanka | Pada deszcze                           |
| Wniosek    | Ulica jest mokra                       |

---

|            | modus tollens |
| ---------- | ------------- |
| implikacja | p => q        |
| przesłanka | ~p            |
| wniosek    | ~q            |

---

|            |                                        |
| ---------- | -------------------------------------- |
| Implikacja | Jeśli pada deszcz, to ulica jest mokra |
| Przesłanka | Ulica nie jest mokra                   |
| Wniosek    | Nie pada deszcz                        |

---

## Wnioskowanie rozmyte

|            |                                                               |
| ---------- | ------------------------------------------------------------- |
| implikacja | Jeśli Jan jedzi do Warszawy, to często wraca do domu po 22:00 |
| przesłanka | Jan często jeździ do Warszawy                                 |
| wniosek    | Jan często wraca do domu po 22:00                             |

---

|            |                                               |
| ---------- | --------------------------------------------- |
| implikacja | Jeśli pomidor jest dojrzały, to jest czerwony |
| przesłanka | Pomidor jest bardzo czerwony                  |
| wniosek    | Pomidor jest bardzo dojrzały                  |

---

## Reguły

$IF\ \alpha\ is\ A$ $THEN$ $\beta\ is\ B$

---

## Uogólnione modus ponens

|                                           |
| :---------------------------------------- |
| $IF\ \alpha\ is\ A$ $THEN$ $\beta\ is\ B$ |
| $\alpha = \tilde{A}$                      |
| $\beta = \tilde{B}$                       |

$\tilde{B} = \tilde{A} ∘_t ​(A→B)$
$∘_t$ - złożenie względem t-normy
(Szczegółowo: $\tilde{B}(y) = sup_{x\in X}\{\tilde{A}(x)\ t \ [A(x) \rightarrow B(y)] \}$)

---

|                                            |
| :----------------------------------------- |
| IF pęknięcie = rozległe THEN wyciek = duży |
| pęknięcie = niewielkie                     |
| wyciek = mały                              |

---

## Zadanie lab II

Dokonaj wnioskowania modus ponens dla zbiorów:

$A=\{(x_1​,0.4),(x_2​,0.3),(x_3​,0.1)\}$
$B=\{(y_1​,0.3),(y_2​,0.1)\}$

$\tilde{A}=\{(x_1​,0.8),(x_2​,0.5),(x_3​,0.4)\}$

Użyj implikację Łukasiewicza i t-normę minimum.

---

## Zadanie II

Wyciągnij wniosek używając rozmytej uogólnionego modus tollens. Użyj implikacji Goguen’a i t-normy Łukasiewicza

$A=\{(x_1​,0.5),(x_2​,1),(x_3​,0.6)\}$
$B=\{(y_1​,1),(y_2​,0.4)\}$

$\tilde{B}=\{(y_1​,0.9),(y_2​,0.7)\}$

---

## Zadanie III

Dane są dwa zbiory rozmyte:
$A = 0.5/x_1 + 0.6/x_2 + 0.1/x_3$
$B = 0.2/y_1 + 0.1/y_2$

Zbiór A opisuje sformułowanie "pomidor jest czerwony", a zbiór B opisuje "pomidor jest dojrzały". Wyznacz wniosek B' dla faktu, że pomidor jest prawie dojrzały opisanego zbiorem:

---

$A' = 0.8/x_1 + 0.5/x_2 + 0.4/x_3$

Zastosuj:

- implikację Łukasiewicza i t-normę minimum
- implikację algebraiczną i t-normę maximum
