# Perceptron Train Classic 0 — Artificial Intelligence (Easy)

**Event:** AI Foundations I — by LT 'syreal' Jones
**URL:** `http://chatelaine.cylabacademy.net:22251/`
**Flag:** `academy{perceptron_classic_mode_3ddb3b37}`

## Setup
`GET /config.json` (dataset gentle, dua cluster well-separated):
```json
{"points": [[-4,-2,0],[-3,-4,0],[-2,-3,0],[-3,-1,0],
            [3,4,1],[4,2,1],[2,3,1],[3,1,1]],
 "maxSteps": 16, "lrMin": 0.02, "lrMax": 2.0,
 "initialModel": {"weights": [1.0,-1.0], "bias": 0.0, "accuracy": 0.5}}
```
Berbeda dari Classic 1/2: hanya butuh **satu** run 100% (mode dasar),
dan rentang LR (`0.02–2.0`) lebih sempit.

## Exploit
```http
POST /train
{"learningRate": 0.02}
```
→ `{"accuracy": 1.0, "success": true, "flag": "academy{...}", ...}`

Karena cluster jauh terpisah, hampir semua LR rendah–sedang langsung
mencapai 100% dalam 16 update.

## Manual
Buka URL, klik Run training (slider default 0.02) → flag muncul.

## File
- `solve.py` — config + train + print flag
- `flag.txt` — flag
- `writeup.txt` — versi txt
