---
type: reference
title: Crew Sim — Findings
tags: [settlements/reference, settlements/analysis]
---
# 👥 Crew Sim — Findings

First simulation at **crew scale** — full battles, 4 to 14 models a side, alternating activation, Priority, Orders, Ready/Reactions, Stress and Break tests, built weapons, conditions, and a probabilistic terrain model. Seed `20260713`. Run: `test-bench/crew_sim.py` · `crew_calibrate.py` · `weapon_sim.py` · `weapon_tests.py`.

> [!success] Headline
> **The list-building and weapon systems balance — but only on a legal board.** Eight archetypes at 100 points sit within an **11-point spread** at 9–12 terrain features. Push the board sparse and the shooters win by 35; push it crowded and the swarms win by 34. **Terrain density is the most powerful dial in the game — bigger than any points cost — and it is the only reason the system works.**

## 1 · Terrain is a bigger lever than any point cost
Cadre (4 models) vs Recruit horde (14), as LOS-blocking rises:

| LOS blocked | 10% | 20% | 30% | **40%** | 50% | 60% |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| **Cadre wins** | 81% | 73% | 62% | **45%** | 29% | 15% |

A **66-point swing** from terrain alone. No points value could move a matchup that far. Parity sits at **40–45% blocked** — which is exactly what **9–12 large features** on a 3'×3' produces ([[Terrain#Setup procedure]]).

> [!danger] This is why terrain density needs a **ceiling**, not just a floor
> Density is chosen *after* lists are locked. "Nine minimum, as crowded as you like" hands the game to whoever pushes the dial — a swarm player wants a jungle, a gunline wants a car park. **9–12.**

## 2 · The final balance table
Eight archetypes, every list legal at ≤100 points under the [[List Building]] pyramid, 3,000 battles per pairing.

> [!note] **Doctrines were pulled from the battle ruleset** (they're a campaign / list-building mechanic). The rows tagged *Firebase / Storm / Cadre / Mob* below are the crew **archetypes** the sim ran — the doctrine **discounts** some leaned on (especially **Storm**'s free melee classes → armour budget) are no longer in the rules, so read those rows as archival. See the melee-elite note in §5.

**On a legal board (42% blocked) — spread 11 points:**

| List | Models | Pts | Win rate |
|---|:--:|:--:|:--:|
| Firebase *(MG gunline)* | 4 | 99 | **54%** |
| Snipers *(24" rifles)* | 4 | 96 | 53% |
| Standard *(no doctrine)* | 6 | 96 | 52% |
| Pyramid *(legal max)* | 11 | 93 | 52% |
| Storm *(armoured melee)* | 8 | 100 | 51% |
| Horde *(9 STR Fighters)* | 9 | 100 | 51% |
| Cadre *(4 riflemen)* | 4 | 96 | 44% |
| Mob *(13 Recruits)* | 13 | 96 | 43% |

**Off a legal board it falls apart, exactly as designed:**

| Board | Winner | Spread |
|---|---|:--:|
| Sparse 30% *(illegal)* | Firebase 67% · Snipers 64% — **shooters** | 35 |
| **Legal 42%** | **everything, within 11 points** | **11** |
| Crowded 55% *(illegal)* | Pyramid 65% · Storm 64% · Horde 64% — **swarms** | 34 |

## 3 · Morale — change nothing
The friendly-Down Stress trigger *looked* like it would wipe crews (3 casualties in LOS = 3 Stress; a Break test at NRV 0 / Stress 3 fails **80%** of the time). Two softeners were tested. **Both broke the game:**

| Recruit horde win% vs Cadre | 10% blocked | 30% | 40% | 60% |
|---|:--:|:--:|:--:|:--:|
| **As written** | 19% | 39% | 54% | 85% |
| + "ignore Stress while bunched" | **93%** | **93%** | **94%** | 96% |
| + "cap Stress from Downs at 1/round" | **60%** | **65%** | **70%** | 88% |

On a legal board the cascade is mild — **0.6 BugOuts per battle** versus 5.3 on a sparse one. **The cascade is not a bug; it is the only thing keeping a swarm honest.** [[Morale]] stays exactly as written.

## 4 · Ready is the answer to uneven crew sizes
No new rule is needed for a 4-model crew facing a 14-model one. The elite crew converts its last activations into **Ready** and snap-shoots the tail as it moves — 4 models = 4 banked reactions, so every fighter effectively shoots twice. The **underdog +1 Priority** likewise stays: it is not an exploit for small crews, it is their **compensation**. WND is fixed at 1 and the Injury roll ignores stats, so **quality has a hard ceiling that numbers don't** — swarms out-produce elites on raw output, and fewer models *should* go first. See [[Initiative & Activation]].

## 5 · What the weapon system taught us
- **A drawback must bite no matter how you play.** Caught twice: **Slow on a rifle** is free points (a rifleman never Charges) and **Awkward on a sniper** is free points (he never moves — and it *synergises* with Accurate). Slow is now melee-only; **Awkward is cut**.
- **Range is a threshold, not a curve.** Deployment zones are 24" apart, so a 24" weapon fires from its own deployment zone on turn one. Uncapped, a long-range crew beat every list by 13–30 points *at any price*. **Hard cap: 24".**
- **Melee elites cannot exist without the Storm doctrine.** A 4-model melee crew wins about **10%** — four fighters with axes cannot cross 24" of street. With Storm (free melee classes → an armour budget) it lands at **51%**. *(Storm is now removed with the Doctrine layer — so melee-elite viability is a live balance question for the table, or for a campaign that reintroduces the discount.)*
- **A Fighter has one real build: STR.** Win rates sparse/mid/dense — STR+2: **14/35/63** · NRV+2: **10/21/40** · DEX+2: **5/16/36**. A swarm cannot buy composure or guns; it can only buy muscle and get there.
- **The rank ladder holds.** The 9-Fighter horde, the 11-model pyramid and the 14-model Recruit horde land within **three points of each other** at every density. Recruit-at-5 and Fighter-at-8 are priced correctly against one another.

## What this sim does NOT model
Objectives, skills, hacking, terrain interaction, verticality, Hidden, flanking. It prices the **combat floor** only — AGI and INT are worth literally zero in it by construction, which is precisely why **the board has to price them** ([[Dice Mechanic — Sim Findings]] §6). It cannot tell you whether a Techie is worth 16 points. It *can* tell you that the Cadre and the horde trade evenly at equal cost — which they now do.

---
*Next: a scenario-aware pass once [[Scenarios]] exists, so objective-runners and hackers finally register.*

See [[List Building]] · [[Weapons]] · [[Terrain]] · [[Morale]] · [[Initiative & Activation]] · [[Dice Mechanic — Sim Findings]] · [[Skill Sim — Findings]].
