# Raw sim outputs — Packet Design Review tests

Verbatim stdout from the runs that produced `docs/PACKET-TEST-RESULTS.md`.
Committed so every number in that document can be re-derived rather than trusted.

| File | Produced by | Sample |
|---|---|---|
| `stealth2d-n700.txt` | `py -3.13 stealth2d.py 700` | 700 games/cell |
| `packet_battle-n2000.txt` | `py -3.13 packet_battle.py 2000` | 2000 games/cell (T8: 8000 battles) |
| `packet_campaign-n800-6000.txt` | `py -3.13 packet_campaign.py 800 6000` | 800 games/cell calibration, 6000 campaigns |

Run from `test-bench/balance/`. Each harness sets the engine dials it needs and
restores them, so the runs are order-independent.

**Why these are in the repo.** `POINTS-TABLE.md` §7 and `points/ticks.py` both cite
`balance/armourprice.py` as the source of the Light 30 / Heavy 60 armour level —
and that file does not exist, so the number cannot be re-derived by anyone. These
outputs exist so the packet-test numbers never end up in the same position.
