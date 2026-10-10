# Perceptron Train Classic 2 Alpha — Artificial Intelligence (Easy)

**Event:** AI Foundations I — by LT 'syreal' Jones
**URL:** `http://chatelaine.cylabacademy.net:23404/`
**Flag:** `academy{perceptron_classic_2_alpha_5rates_c2b1487d}`

## Setup
`GET /config.json` (linearly separable, 12 titik):
```json
{"points": [[-2,4,1],[1,1,1],[-2,0,0],[3,-1,1],[-3,-4,0],[3,-4,0],
 [4,1,1],[1,3,1],[-1,-3,0],[-3,2,0],[2,-2,0],[4,-2,1]],
 "maxSteps": 16, "lrMin": 0.02, "lrMax": 20.0,
 "successTarget": 5, "successCount": 0,
 "initialModel": {"weights": [1.0,-1.0], "bias": 0.0, "accuracy": 0.5}}
```
Butuh **5 learning rate berbeda** yang masing-masing mencapai 100% accuracy.
`successCount` disimpan di server (global), jadi 5 run sukses berturut cukup.

## Exploit
```http
POST /train
{"learningRate": 1.0}
```
LR yang sukses di instance ini: `0.8, 1.0, 1.5, 2.0, 3.0` (semua acc=1.0).
Setelah 5 sukses → `flag: academy{perceptron_classic_2_alpha_5rates_c2b1487d}`

Sweep untuk menemukan sweet spot:
- `0.02` → 0.583, `0.05` → 0.75, `0.1-0.3` → 0.917, `0.5` → 0.833 (gagal)
- `0.8, 1.0, 1.5, 2.0, 3.0` → 1.0 (sukses)

## Manual
Buka URL, geser slider ke 0.8, Run; ulangi dengan 1.0, 1.5, 2.0, 3.0.

## File
- `solve.py` — config + 5 train sukses + print flag
- `flag.txt` — flag
- `writeup.txt` — versi txt
