# Perceptron Train 3-Bit Parity — Artificial Intelligence (Easy)

**Event:** AI Foundations I — by LT 'syreal' Jones
**URL:** `http://xebec.cylabacademy.net:29078/`
**Flag:** `academy{3b1t_p4r1ty_unl34rn4bl3_l1n34rly_5d1cd0f2}`

## Setup
`GET /config.json` (3-bit parity, 8 titik di 3D, `dimensions: 3`):
```json
{"points": [[-2,-2,-2,0],[-2,-2,2,1],[-2,2,-2,1],[-2,2,2,0],
            [2,-2,-2,1],[2,-2,2,0],[2,2,-2,0],[2,2,2,1]],
 "maxSteps": 16, "lrMin": 0.02, "lrMax": 20.0,
 "successThreshold": 0.75,
 "initialModel": {"weights": [1.0,1.0,1.0], "bias": 0.0, "accuracy": 0.25}}
```
Label = parity (jumlah bit 1 ganjil → 1). Tidak linearly separable
oleh satu bidang; 75% (6/8) adalah maksimum.

## Exploit
```http
POST /train
{"learningRate": 0.2}
```
→ `{"accuracy": 0.75, "success": true, "flag": "academy{...}", ...}`

Sweep: 0.02/0.05/0.1 → 0.25 (gagal), **0.2 → 0.75** (sukses).

## Manual
Buka URL, geser slider ke 0.2, Run training → flag muncul.

## File
- `solve.py` — config + train + print flag
- `flag.txt` — flag
- `writeup.txt` — versi txt
