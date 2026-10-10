# Perceptron Play Alpha — Artificial Intelligence (Easy)

**Event:** AI Foundations I — by LT 'syreal' Jones
**Conn:** `nc chatelaine.cylabacademy.net 37297`
**Flag:** `academy{11n34r1y_53p4r4813_9938a80d}`

## Setup
REPL: `SET w1 w2 b`, `ADJUST dw1 dw2 db`, `POINTS`, `CHECK`, `SHOW`.
Points (`POINTS`) — dua cluster terpisah diagonal:
```
(-3,-2) -> 0      (+3,+1) -> 1
(-1,-1) -> 0      (+2,+2) -> 1
(-4,-2) -> 0      (+1,+3) -> 1
```
Class 0 di kiri-bawah (kuadran III), class 1 di kanan-atas (kuadran I).

## Exploit
Mulai w1=1, w2=-1 (salah). Set boundary `y = -x`:
```
SET 1 1 0
CHECK
```
activation = x + y. Class 0 (x+y < 0) → pred 0 ✓, class 1 (x+y > 0)
→ pred 1 ✓. Semua benar:

```
Perfect! All points are classified correctly.
academy{11n34r1y_53p4r4813_9938a80d}
```

## Solver
`python artificial-intelligence/Perceptron-Play-Alpha/solve.py`
Kirim `SET 1 1 0` lalu `CHECK`.

## File
- `solve.py` — koneksi nc + set weights + print flag
- `flag.txt` — flag
- `writeup.txt` — versi txt
