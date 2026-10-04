# WAVE COMPUTATIONAL CELL (WCC-1)

WCC-1 adalah unit konseptual untuk transformasi Y = A X.

Contoh:

A = [[2,1],[-1,3]]
X = [1,2]^T
Y = [4,5]^T

Input dapat direpresentasikan sebagai amplitude dan phase.

Weight dapat direpresentasikan melalui coupling, transmission, phase shift, geometry, resonance, dan delay.

Negative weight:
-X = A exp(i pi)

Implementasi memerlukan phase-sensitive detection atau dual-rail bila tanda harus dipertahankan.

## Prototype 4x4

Y = A X

Y1 = a11 X1 + a12 X2 + a13 X3 + a14 X4

Routing konseptual:

X1 --[a11]--[delay 3]---X2 --[a12]--[delay 2]----> Y1
X3 --[a13]--[delay 1]---/
X4 --[a14]--[delay 0]---/

Kontribusi bertemu pada event/readout.

Bobot dan routing tidak gratis. Menggandakan jalur dapat menambah energi, area, loss, dan control.

WCC adalah model awal, bukan desain fabrikasi.
