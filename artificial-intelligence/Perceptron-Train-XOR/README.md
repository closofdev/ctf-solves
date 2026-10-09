# Perceptron Train XOR — Artificial Intelligence (Easy)

**Event:** AI Foundations I — by LT 'syreal' Jones
**URL:** `http://chatelaine.cylabacademy.net:10996/`
**Flag:** `academy{x0r_unl34rn4bl3_by_p3rc3ptr0ns_5307b2ae}`

## Setup
`GET /config.json`:
```json
{"points": [[-2,-2,0],[2,2,0],[-2,2,1],[2,-2,1]], "maxSteps": 16,
 "lrMin": 0.02, "lrMax": 20.0, "successThreshold": 0.75,
 "initialModel": {"weights": [1.0,-1.0], "bias": 0.0, "accuracy": 0.25}}
```
XOR, 4 titik, 16 update, hanya misclassified yang update.

## Exploit
```http
POST /train
{"learningRate": 0.5}
```
→ `{"accuracy": 0.75, "success": true, "flag": "academy{...}", ...}`

Semua LR 0.02–20.0 memberi 75% di instance ini. Satu perceptron
tidak bisa 100% untuk XOR (tidak linearly separable), 75% = 3/4 titik.

## Manual
Buka URL, biarkan slider 0.02, klik Run training → flag muncul.

## File
- `solve.py` — config + train + print flag
- `flag.txt` — flag
- `writeup.txt` — versi txt
