# Perceptron Train XNOR — Artificial Intelligence (Easy)

**Event:** AI Foundations I — by LT 'syreal' Jones
**URL:** `http://chatelaine.cylabacademy.net:45959/`
**Flag:** `academy{xn0r_unl34rn4bl3_by_p3rc3ptr0ns_da5e1216}`

## Setup
`GET /config.json`:
```json
{"points": [[-2,-2,1],[2,2,1],[-2,2,0],[2,-2,0]], "maxSteps": 16,
 "lrMin": 0.02, "lrMax": 20.0, "successThreshold": 0.75,
 "initialModel": {"weights": [1.0,1.0], "bias": 0.0, "accuracy": 0.25}}
```
XNOR, 4 titik, 16 update, hanya misclassified yang update.
Sama seperti XOR tetapi label dibalik dan init w=[1,1].

## Exploit
```http
POST /train
{"learningRate": 0.5}
```
→ `{"accuracy": 0.75, "success": true, "flag": "academy{...}", ...}`

XNOR tidak linearly separable, 75% (3/4 titik) adalah maksimum
untuk satu perceptron.

## Manual
Buka URL di browser, klik Run training (LR default 0.02) → flag muncul.

## File
- `solve.py` — config + train + print flag
- `flag.txt` — flag
- `writeup.txt` — versi txt
