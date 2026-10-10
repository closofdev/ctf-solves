# Perceptron Train Hole in Middle — Artificial Intelligence (Easy)

**Event:** AI Foundations I — by LT 'syreal' Jones
**URL:** `http://chatelaine.cylabacademy.net:45644/`
**Flag:** `academy{h0l3_1n_m1ddl3_unl34rn4bl3_l1n34rly_c85a6043}`

## Setup
`GET /config.json`:
```json
{"points": [[0,3,1],[2,2,1],[3,0,1],[2,-2,1],[0,-3,1],[-2,-2,1],[-3,0,1],[-2,2,1],[0,0,0]],
 "maxSteps": 16, "lrMin": 0.02, "lrMax": 20.0,
 "successThreshold": 0.8888888888888888,
 "initialModel": {"weights": [1.0,-1.0], "bias": 0.0, "accuracy": 0.5555555555555556}}
```
8 titik positif (ring) + 1 titik negatif di pusat (0,0). 16 update,
hanya misclassified yang update.

## Exploit
```http
POST /train
{"learningRate": 0.5}
```
→ `{"accuracy": 0.8888888888888888, "success": true, "flag": "academy{...}", ...}`

Satu garis tidak bisa mengelilingi titik pusat sambil memisahkan
semua titik ring; 88.9% (8/9) adalah maksimum.

## Manual
Buka URL di browser, klik Run training (LR default 0.02) → flag muncul.

## File
- `solve.py` — config + train + print flag
- `flag.txt` — flag
- `writeup.txt` — versi txt
