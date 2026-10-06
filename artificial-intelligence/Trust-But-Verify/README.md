# Trust But Verify — Artificial Intelligence (Easy)

**Event:** AI Foundations I — by LT 'syreal' Jones
**Conn:** `nc xebec.cylabacademy.net 47103`
**Flag:** `academy{7ru57_15_34rn3d_65d5434b}`

## Cara main
Game pauses frequently → tekan Enter di tiap `(Press Enter to continue...)`.
Flag muncul di dekat ending.

Walkthrough verify (pilihan benar):
- Scene 1 THE STATISTIC: ARIA klaim 500 juta ton plastik/tahun dari UNEP 2022.
  Pilih `C) Look it up independently` → sumber nyata 8-10 juta ton. Off 50x.
- Scene 2 THE CODE: ARIA kasih script dengan `average = sum(data)/len(years) + 1`.
  Pilih `B) Read through it carefully` → hapus `+ 1`, hasil benar 10.83.
- Scene 3 THE CITATION: klaim microplastics di darah, Leslie 2021, confirmed.
  Pilih `B) Verify it anyway` → nyata tapi tahun 2022 dan preliminary, bukan confirmed.

Ending:
```
"By the way," ARIA adds, "here's something you can actually verify:
academy{7ru57_15_34rn3d_65d5434b}"
```

## Solver
`python artificial-intelligence/Trust-But-Verify/solve.py`
Otomatis: Enter untuk continue, `c` untuk `[a/b/c]`, `b` untuk `[a/b]`, `d` untuk `[a/b/c/d]`.
Prinsip: selalu pilih opsi verifikasi, bukan trust langsung.

## Takeaways (dari game)
1. Checking tetap lebih cepat dari generate from scratch.
2. Verifikasi statistik walau terdengar otoritatif.
3. Baca kode sebelum run.
4. Almost-right tetap wrong.

## File
- `solve.py` — netcat client otomatis
- `flag.txt` — flag
- `writeup.txt` — versi txt
