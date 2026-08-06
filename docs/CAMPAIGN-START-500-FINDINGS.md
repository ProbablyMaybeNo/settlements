# Campaign Start @ 500 Crew Rating — sim findings

**Run 2026-08-05** · harness `test-bench/balance/campaign500.py` · 2.5D engine (`test-bench/engine2d/`)
**Method:** six crew archetypes × four scenarios (Hold · Hold+Claim · Annihilate · Breakthrough), every pairing, **sides swapped**, 500 games per pairing = **30,000 games per configuration**. Every crew is rebuilt to the cap at whatever prices the configuration sets, so cheaper bodies genuinely buy more models.

**What was being tested:** the Campaign Start ladder proposed in `FULL-RULES-SYSTEM-V1` §16 — **Recruit 65 · Fighter 75 · Specialist 125 · Leader 170 at a 500 cap**, with one starting skill per rank (none/T1/T2/T3) and the loosened pyramid (one Leader, minimum three models, no ratio). The document flags those prices as *"first-draft, backed out from the skill Credit values, not a validated number."*

---

## Headline

**The 500 cap is the problem, not the rank ladder.** Six ladders spanning a 4× range in body cost were swept and none produced a balanced game at 500. Sweeping the *cap* instead, with the ladder held fixed, fixed most of it — and the penalty is specific to 500, gone by 625.

---

## 1 · Price authority fixed as a precondition

`engine2d/data.py` hand-set its own 100-scale prices, so the simulator had never priced a crew with the costing engine — the gap `POINTS-DECISIONS.md` records as *"until they share one table, a price cannot be verified end-to-end."* This harness takes every weapon, armour and equipment price from `points/`, so one table drives both:

| | bat | crowbar | sledge | pistol | rifle | molotov | light | heavy |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Credits | 0 | 70 | 80 | 40 | 100 | 85 | 30→**60** | 60→**100** |

---

## 2 · Ladder sweep — no ladder fixes it

All at a 500 cap. Spread = best archetype's mean win % minus worst.

| Ladder | R/F/S/L | Swarm | Line | Elite | Gunline | Armoured | Mixed | **Spread** |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **doc** | 65/75/125/170 | 55 | 57 | 54 | **18** | 64 | 53 | **46** |
| matchplay | 65/95/165/245 | 59 | 56 | 37 | 31 | 57 | 61 | 30 |
| charged | 65/115/200/300 | 57 | 57 | 45 | 38 | 59 | 44 | 21 |
| ×0.75 | 49/71/124/184 | 57 | 55 | 55 | 18 | 63 | 53 | 45 |
| ×0.5 | 33/48/83/123 | 66 | 51 | 46 | 23 | 64 | 49 | 43 |
| ×0.35 | 23/33/58/86 | 65 | 48 | 43 | 33 | 58 | 54 | 32 |

**The 21-point "best" result is a mirage.** At the `charged` ladder every crew is **two models** — the spread is tight because there is almost no game left to be unbalanced. Crew sizes:

| Ladder | Swarm | Line | Elite | Gunline | Armoured | Mixed |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| doc | 4 | 3 | 4 | **2** | 3 | 3 |
| matchplay | 3 | 2 | 2 | 2 | 2 | 3 |
| charged | 2 | 2 | 2 | 2 | 2 | 2 |
| ×0.5 | 10 | 4 | 3 | 4 | 5 | 4 |
| ×0.35 | 15 | 5 | 6 | 5 | 7 | 5 |

Making bodies cheaper doesn't help either: at ×0.35 the Swarm reaches 15 models and the spread *widens* to 32 as body count reasserts itself — consistent with the existing measurement that model count is the dominant win driver.

---

## 3 · A shooting crew is unbuildable at 500

Gunline wins **18%** at the doc ladder, and the arithmetic says why:

```
Leader + rifle      170 + 100 = 270
Fighter + rifle      75 + 100 = 175   → 445
cheapest third body            =  65   → 510  ✗ over cap
```

**A rifle-armed Leader puts the crew below the document's own three-model minimum.** The legal workaround is to downgrade the Leader to a pistol (Leader 210 + rifle Fighter 175 + Recruit 65 = 450). That a whole weapon class is priced out of the format is a design consequence worth taking a position on, not a rounding error: at 1000 a rifle is 10% of the crew; at 500 it is 20%.

---

## 4 · The cap sweep — this is the actual lever

Doc ladder held fixed, only the cap moves:

| Cap | Swarm | Line | Elite | Gunline | Armoured | Mixed | **Spread** | Gunline size |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **500** | 55 | 57 | 54 | **18** | 64 | 53 | **46** | 2 |
| 625 | 53 | 55 | 51 | 31 | 63 | 47 | **32** | 3 |
| 750 | 50 | 54 | 55 | 30 | 62 | 49 | **32** | 4 |
| 875 | 49 | 55 | 48 | 28 | 65 | 56 | 37 | 5 |
| 1000 | 43 | 58 | 53 | 27 | 63 | 56 | 36 | 5 |
| 1250 | 43 | 52 | 56 | 28 | 60 | 61 | 33 | 7 |

The spread falls **46 → 32** between 500 and 625 and then flattens. Gunline recovers from 18% to 31% over the same step. **500 is the only cap tested that is materially worse than its neighbours.**

Two ways to fix it, both untested as fixes:
1. **Raise the Campaign Start cap to 625–750.** Cheapest change; keeps the ladder and the "starts small, grows" intent.
2. **Cut the mandatory Leader's price specifically.** At 500 the Leader is 34% of the crew against 24% at Match Play — the pyramid rule forces you to buy the single most expensive model in the game with a third of a budget that was halved.

---

## 5 · Armour — 60/100 wins, and this closes M2

Armoured topped the table at **every** cap, which pointed at the one price with two live values: `points/ticks.py` carries **30/60** *[measured]*; `FULL-RULES-SYSTEM-V1` §15 prints **60/100**. `POINTS-COMPLETION-PLAN.md` M2 has this marked **re-open** because the cited source file, `balance/armourprice.py`, **is missing from the repo** — the 30 could not be re-derived by anyone.

Swapping only these two numbers, everything else fixed:

| Armour price | Armoured win % | Overall spread |
|---|:--:|:--:|
| engine **30 / 60** | **64%** — best crew in the game | 46 |
| doc **60 / 100** | **51%** — mid-table | **37** |

**Adopt 60 / 100; `ticks.py` is owed the correction.** Honest caveats: at 60 the Armoured crew drops to two models, so some of the fall is affordability rather than pricing, and this was run at a 500 cap only. Repeat at 1000 before calling it locked.

---

## What this harness cannot see

**It prices bodies, not skills.** Only four skills are implemented in the engine — `knockback`, `stare_down`, `keep_moving`, `hacker` — and all four are Tier 1. A Specialist's T2 and a Leader's T3 do nothing here. So the sweep measures stat points, Orders and model count, and says nothing about whether 20/35/55 are the right tier premiums. That is Milestone 5 and it needs skills implemented first.

Consequence for reading these tables: the sim **undervalues** Specialists and Leaders, because it sees their stat line and Orders but not their skill. Any ladder it recommends is a floor for those two ranks, not a final price.

Other limits worth stating: crews are greedy auto-fills, not optimised lists, so an archetype's ceiling is understated; deployables are excluded entirely (the costing engine has no price for them); and the baseline spread of this harness is ~32 points, which is **not** comparable to the 11-point figure in `Crew Sim — Findings` — different archetypes, different scenario mix, different builder.

---

## Reproduce

```
cd test-bench/balance
py -3.13 campaign500.py 500 ladder     # six rank ladders at a 500 cap
py -3.13 campaign500.py 500 budget     # doc ladder, caps 500 → 1250
py -3.13 campaign500.py 500 armour     # 30/60 vs 60/100, everything else fixed
```
