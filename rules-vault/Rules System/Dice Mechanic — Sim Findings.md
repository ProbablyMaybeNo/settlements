---
type: reference
title: Dice Mechanic — Sim Findings
tags: [settlements/reference, settlements/analysis]
---
# 🎲 Dice Mechanic — Sim Findings

First full simulation pass over the locked core engine. Every test = **10,000 rolls** (the standard sample), engine mirrors the [[Rules Engine|Test Bench]] exactly, seed `20260708` (reproducible). Run: `test-bench/sim_report.py`.

> [!success] Headline
> **The engine is sound and the design thesis holds up.** Cover is the single biggest lever (it roughly *halves* lethality), and — the big one — **in a terrain-free 1v1, combat specialists crush the utility builds**. That's not a bug: it's proof that **[[Terrain|terrain]] and scenario objectives *must* carry the balance**, exactly as the pillar says. One dial still wants attention: **mobility/utility needs scenario structure to be worth taking**. (The Stress/Nerve worry from the first pass is **resolved** — see §7, re-run on the revised system.)

## 1 · Engine validation — [[core-000 Core Test]]
Simulated vs exact across the stat range. They match within sampling noise → the RNG is fair and the curve is exactly as designed: **clean ±10% per point, floored/capped 10–90%**, and **+5 = +6 on a flat roll** (the natural-1 cap).

| Stat mod | Exact | Sim (10k) |
|:---:|:---:|:---:|
| −1 | 30% | 30.9% |
| +0 | 40% | 40.2% |
| +1 | 50% | 50.5% |
| +2 | 60% | 60.5% |
| +3 | 70% | 70.5% |
| +4 | 80% | 79.8% |
| +5 | 90% | 89.7% |
| +6 | 90% | 90.0% |

## 2 · Difficulty ladder — [[Shooting|stat checks]]
Success % by the number you have to beat. **Raising the target by 2 ≈ −20%.** Use this to price Hard/Punishing checks (locks, hacks, breaching).

| Stat mod | 7+ (standard) | 9+ (hard) | 11+ (punishing) |
|:---:|:---:|:---:|:---:|
| +0 | 40% | 20% | 10% |
| +2 | 60% | 40% | 20% |
| +4 | 80% | 60% | 40% |
| +6 | 90% | 80% | 60% |

## 3 · Shooting — [[Shooting]] + [[Damage]]
Standard shooter **DEX +2**, medium weapon (**+2**), open unarmoured target unless noted.

**Cover is the dominant lever.** Going from open to Hidden cuts wounds-per-shot roughly in half and nearly *doubles* the shots needed to put a target down.

| Target cover | To-hit | Wound / shot | Avg shots to Down |
|:---:|:---:|:---:|:---:|
| Open | 59.8% | 35.8% | 2.8 |
| Light (−1) | 49.8% | 29.9% | 3.3 |
| Heavy (−2) | 40.1% | 24.0% | 4.2 |
| Hidden (−3) | 30.0% | 17.7% | 5.7 |

**Weapon vs armour** (wound/shot, open target). Each class ≈ ±5–6%. A **heavy weapon (+3) is almost exactly cancelled by heavy armour (−2)** — the damage/armour bands are well spaced and doing their job.

| Weapon | Armour 0 | Armour −1 | Armour −2 |
|:---:|:---:|:---:|:---:|
| Light +1 | 29.8% | 24.0% | 17.8% |
| Medium +2 | 35.1% | 29.1% | 23.8% |
| Heavy +3 | 41.9% | 36.6% | 29.4% |

> [!note] Lethality read
> A competent shooter downs an open, unarmoured target in **~3 shots** (~36%/shot). Fast but not instant — units trade a few shots, and **cover buys survival more than armour does**. That's the right feel for the pillar.

## 4 · Melee — [[Melee]]
Opposed STR, **ties to the defender**. Attacker light weapon (+1), no armour.

| STR Δ (atk−def) | Atk wins | Atk wins **on a charge** | Downs per clash |
|:---:|:---:|:---:|:---:|
| −2 | 28.1% | 37.0% | 14.3% |
| −1 | 36.3% | 45.6% | 18.3% |
| **0 (even)** | **46.5%** | **54.8%** | 23.4% |
| +1 | 55.4% | 64.0% | 27.1% |
| +2 | 63.8% | 72.1% | 31.2% |

- **The defender's tie-edge is real:** an *even* fight is 46.5% / 53.5% for the defender (~3–4% swing). Being attacked isn't a coin flip — it slightly favours the one who holds.
- **Charge (+1) is worth ~+8%** and *flips an even fight* in the attacker's favour (46.5% → 54.8%). The surprise bonus earns its keep.
- Melee is **grindier per exchange** than shooting with light weapons (~23% to down at even STR) — melee wants weapon/skill investment to bite.

## 5 · Head-to-Head (contests) — terminals, arm-wrestles
Opposed test, ties to the defender. **Each point of advantage ≈ ±9–10%.** Reference for hacking duels / tug-of-war objectives.

| A's advantage | P(A wins) |
|:---:|:---:|
| −2 | 28% |
| 0 | 45% |
| +2 | 64% |
| +3 | 72% |

## 6 · Duel matrix — the archetypes fight ⚔️
Every [[Skill Paths|archetype]] vs every other, **10k fights each**, random who-goes-first, Stress on. **WND all = 1, and crucially NO terrain or cover** — a pure attrition vacuum. Cells = row's win %.

| | Braw | Gunn | Tech | Buil | Obje | Heav | Quic | Jack |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Brawler** | — | 47 | 67 | 61 | 86 | 37 | 62 | 76 |
| **Gunner** | 54 | — | 69 | 57 | 75 | 49 | 58 | 66 |
| **Techie** | 33 | 31 | — | 36 | 58 | 30 | 37 | 47 |
| **Builder** | 38 | 42 | 64 | — | 80 | 33 | 51 | 67 |
| **Obj. Grabber** | 14 | 24 | 43 | 20 | — | 15 | 19 | 33 |
| **Heavy Gunner** | 63 | 51 | 72 | 68 | 85 | — | 68 | 77 |
| **Quick Muscle** | 38 | 43 | 64 | 50 | 80 | 33 | — | 67 |
| **Jack** | 24 | 34 | 54 | 34 | 67 | 23 | 33 | — |

**Overall win rate** (avg vs the other 7):

| Rank | Archetype | Win rate |
|:---:|---|:---:|
| 1 | Heavy Gunner | 68.9% |
| 2 | Brawler | 62.4% |
| 3 | Gunner | 61.3% |
| 4 | Quick Muscle | 53.6% |
| 5 | Builder | 53.3% |
| 6 | Techie | 38.9% |
| 7 | Jack of All Trades | 38.5% |
| 8 | Objective Grabber | 24.1% |

> [!important] The big finding — this *validates* the design
> In a terrain-free slugfest, **combat specialists dominate and utility builds get stomped** — the Objective Grabber wins just **24%** and loses 86–14 to the Brawler. That is *exactly what should happen*: raw stats say a mobility/tech build is near-useless in a straight fight. **Their value can only come from the [[Terrain|board]] and [[Scenarios|scenario]]** — locked doors that need the Techie, gaps and objectives that need the Grabber, cover that lets the fragile survive. **This sim is the proof that terrain/objectives must be the balancer.** If a scenario is just "kill each other on open ground," the game collapses to Heavy Gunners — so the scenario deck has to reliably demand non-combat stats.
> Also: **Heavy Gunner (STR+DEX, heavy weapon, armour) is the raw-power king.** Watch it doesn't become an auto-include — it should pay for that in points and be punished by terrain it can't shoot through.

## 7 · Stress / Nerve — fires where it should ✅ — [[Morale]]
Re-run on the **revised** system (Shaken −1 always-on · Break test at 2+ · pass clears all Stress). Fight length and how often a unit breaks:

| Matchup | Avg rounds | Cracks / fight (old → **new**) |
|---|:---:|:---:|
| Jack vs Jack (WND 1) | 2.3 | 0.000 → **0.089** |
| Gunner vs Brawler (WND 1) | 1.6 | 0.000 → **0.089** |
| Jack vs Jack (WND 3) | 9.5 | 0.000 → **1.75** |

> [!success] Right shape — quiet in fast kills, bites in grinds
> The revised model **self-corrected the "inert morale" problem** without a single new combat trigger. At **WND 1** the lethality band is fast enough that fights usually end before Stress hits 2 — so nerve stays out of the way (~0.09 breaks/fight). In a sustained **WND-3** fight it wakes up hard: **~1.75 breaks per fight**, because Stress now *accumulates* (a passed test clears all, a failed one only sheds 1) instead of draining NRV-worth every round. Morale is now a **duration** mechanic — it takes over exactly when a fight drags, which is the intended feel.
> *Still true:* combat triggers alone are thin — the full [[Morale]] trigger list (ranged targeting, friendly Down in LOS, hazards, skills) will push WND-1 rates up too at crew scale. But the engine is no longer inert, so that's headroom, not a fix we need.

> [!note] System revised since this sim (2026-07-09)
> The Nerve system was reworked after these runs. **Shook is now the always-on "Shaken" state** — any 1+ Stress = −1 to all rolls, no roll. **Break tests only start at 2+ Stress** (`1d10 + NRV − (Stress−1) ≥ 7`, Shaken's −1 excluded), failing into **Bolt (2) / Broken (3) / BugOut (4+)**. The −1-severity analysis below still holds (Shaken *is* that −1); the old margin-ladder above it is superseded — see [[Morale]].

### The Shook −1 — is it the right penalty? (added 2026-07-09)
The real question isn't whether Stress *fires* (more triggers are coming) — it's whether **Shook's −1-to-all-rolls** is the right severity. **Shook is the mildest and most common crack** (fail by 1–2), so it's what most morale failures feel like. What −1 actually costs (40k rolls each):

| Situation | Normal | **Shook −1** | −2 (for scale) |
|---|:---:|:---:|:---:|
| Shooter wound/shot | 35.7% | 30.0% | 23.8% |
| Even melee clash — attacker win% | 44.9% | 35.6% | 28.0% |
| Even duel, **melee**, Shook whole fight | 50% | **33%** | 20% |
| Even duel, **ranged**, Shook whole fight | 50% | **39.5%** | 28% |

> [!success] Verdict — keep the −1
> −1 = **exactly one stat-point** (~10%/roll). A Shook brawler drops an even fight to **33%**, a Shook shooter to **~40%** — a real bite, not a death sentence. That's the right weight for the *entry* crack tier: big enough to hurt, mild enough to leave headroom for Bolt/Break/Insanity (which remove the unit). **Raising it to −2 makes the mildest failure hit like a 2-stat gap and compresses the whole ladder.** The lever for "how much morale matters" is **frequency + duration, not the −1 size** — and triggers are already being added.

Two things to decide (they matter more than the −1):
- **Melee compounds — ranged doesn't.** −1 hits *both* attack and defence in an opposed melee, so Shook punishes brawlers ~1.7× harder (−17 pts vs −10). Thematically fine; if you want parity, apply Shook's −1 only to the unit's *own* actions, not forced defensive rolls.
- **Death-spiral risk.** Many triggers × a compounding −1 → a pressured unit keeps failing and eating −1s, losing harder the more it loses. Brutal and on-theme, but a deliberate choice — if unwanted, add a valve (an already-Shook unit doesn't re-test, or cap Stress).

## Design takeaways
1. ✅ **Engine is locked-in correct** — no maths surprises.
2. 🗺️ **Terrain/objectives are load-bearing for balance, confirmed** — build the scenario deck to demand INT/AGI, or utility builds are dead weight.
3. 💥 **Cover > armour for survival** — good, on-pillar.
4. ⚔️ **Charge and the defender tie-edge both matter** — melee has real texture.
5. ✅ **Stress/Nerve fires correctly** on the revised system — quiet in fast WND-1 kills, ~1.75 breaks/fight in sustained WND-3 grinds. Morale is now a duration mechanic.
6. 🎯 **Watch Heavy Gunner** as a potential auto-include; price it and gate it with terrain.

---
*Next passes worth running: multi-model crew fights (does Stress wake up?), the same duels **with cover** (does the Grabber/Techie survivability change?), and points-cost balancing once [[List Building]] numbers exist.*

See [[Rules Engine]] · [[core-000 Core Test]] · [[Shooting]] · [[Melee]] · [[Damage]] · [[Morale]] · [[Terrain]].
