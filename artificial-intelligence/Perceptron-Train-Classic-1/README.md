# Perceptron Train Classic 1 — Artificial Intelligence (Easy)

**Event:** AI Foundations I — by LT 'syreal' Jones
**URL:** `http://chatelaine.cylabacademy.net:42143/`
**Flag:** `academy{perceptron_classic_5rates_432f0bf5}`

## Setup
`GET /config.json` (dua cluster well-separated → linearly separable):
```json
{"points": [[-4,-2,0],[-3,-4,0],[-2,-3,0],[-3,-1,0],
            [3,4,1],[4,2,1],[2,3,1],[3,1,1]],
 "maxSteps": 16, "lrMin": 0.02, "lrMax": 20.0,
 "successTarget": 5, "successCount": 0,
 "initialModel": {"weights": [1.0,-1.0], "bias": 0.0, "accuracy": 0.5}}
```
Butuh **5 learning rate** yang masing-masing mencapai 100%. Karena cluster
jauh terpisah, hampir semua rate rendah–sedang berhasil.

## Exploit
```http
POST /train
{"learningRate": 0.02}
```
LR yang sukses di instance ini: `0.02, 0.05, 0.1, 0.2, 0.3` (semua acc=1.0).
Setelah 5 sukses → `flag: academy{perceptron_classic_5rates_432f0bf5}`

`successCount` disimpan di server (global); 5 run sukses sudah cukup.

## Manual
Buka URL, Run di LR 0.02 → 0.05 → 0.1 → 0.2 → 0.3 sampai flag muncul.

## File
- `solve.py` — config + 5 train sukses + print flag
- `flag.txt` — flag
- `writeup.txt` — versi txt
