---
marp: true
theme: uncover
class: invert
author: Konrad
---

# Modelowanie i przetwarzanie informacji nieprecyzyjnej

---

# Zajęcia V

---

## Problem

Chcemy mieć autonomiczny samochód. Jak to osiągnąć?

---

## Reguły

Jeśli samochód jest blisko lewej krawędzi,
skręcamy w prawo

##### IF (left_sensor IS close) THEN (steering IS right)

---

##### _IF (left_sensor IS close) AND (front_sensor IS far) THEN (steering IS right)_

---

## Etapy sterowania

1. Fuzyfikacja
2. Wnioskowanie
3. Agregacja
4. Defuzyfikacja

---

## Fuzyfikacja

Odczyt temperatury z czujnika: 24.7°C

| Zmienna       | Term     | Stopień przynaleźności $\mu$ |
| ------------- | -------- | ---------------------------- |
| $temperatura$ | $zimno$  | 0                            |
| $temperatura$ | $cieplo$ | 0.9                          |
| $temperatura$ | $goraco$ | 0.5                          |

---

## Wnioskowanie

Reguły postaci:
_IF (x IS a) AND/OR (y IS b) THEN (y IS c)_

<hr />

Jeśli temperatura jest ciepła i wilgotność jest duża, to wentylacja powinna być mocna

---

## Agregacja

Każda reguła produkuje fragment zbioru rozmytego. Fragmenty łączone są w jeden zbiór, na podstawie którego będzie podjęta decyzja.

---

## Defuzyfikacja

Konwersja otrzymanego zbioru rozmytego decyzji na wartość liczbową przekazywaną do elementu wykonawczego.

Najczęściej używana metoda: wyznaczenie centroidu, czyli środka pola pod funkcją przynależności.

---

# Zadanie I

Korzystając z programu symulatora w materiałach, doimplementuj opis potrzebnych zmiennych lingwistycznych oraz opisz reguły tak, aby samochód jeździł po torze.

---

## Samochód:

- ma 3 czujniki, po lewej, na wprost oraz po prawej
- ma prędkościomierz
<hr />

- posiada hamulec oraz gaz
- posiada kierownicę

---

## Wymagania:

- Samochód jeździ po torze, nie po trawie (dbamy o przyrodę)
- Nie modyfikuj stałych w programie innych niż dotyczących sterowania rozmytego
- Liczba punktów za zadanie:
  $min(10, loops)$ dla $loops < 20$ oraz $15$ dla $loops \geq 20$
- Jako rozwiązanie, prześlij klasę `FuzzyController`
