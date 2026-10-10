# Perceptron Play Naught — Artificial Intelligence (Easy)

**Event:** AI Foundations I — by LT 'syreal' Jones
**Conn:** `nc chatelaine.cylabacademy.net 20759`
**Flag:** `academy{n4ught_bu7_53p4r4b13_277a702d}`

## Setup
Interactive REPL: `SET w1 w2 b`, `ADJUST dw1 dw2 db`, `POINTS`, `CHECK`, `SHOW`.
Points (`POINTS`):
```
(-4,-1) -> 0
(-1,+2) -> 1
(+0,-1) -> 0
(+0,+2) -> 1
(+2,-1) -> 0
(+3,+1) -> 1
(+4,+2) -> 1
```
Semua class 0 punya y=-1 → separabel saja di sumbu x, tapi dgn y
jadi linearly separable: batas horizontal y=0.

## Exploit
Mulai w1=1, w2=-1, b=0 (salah). Set:
```
SET 0 1 0
CHECK
```
activation = 0*x + 1*y + 0 = y. Class 0 (y=-1) → -1 (<0 → pred 0 ✓),
class 1 (y>=1) → >0 (→ pred 1 ✓). Semua benar:

```
Perfect! All points are classified correctly.
academy{n4ught_bu7_53p4r4b13_277a702d}
```

## Solver
`python artificial-intelligence/Perceptron-Play-Naught/solve.py`
Kirim `SET 0 1 0` lalu `CHECK`.

## File
- `solve.py` — koneksi nc + set weights + print flag
- `flag.txt` — flag
- `writeup.txt` — versi txt
