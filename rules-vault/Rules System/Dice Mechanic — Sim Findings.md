---
type: reference
title: Dice Mechanic — Sim Findings
tags: [settlements/reference, settlements/analysis]
---
# 🎲 Dice Mechanic — Sim Findings

First full simulation pass over the locked core engine. Every test = **10,000 rolls** (the standard sample), engine mirrors the [[Rules Engine|Test Bench]] exactly, seed `20260708` (reproducible). Run: `test-bench/sim_report.py`.

> [!success] Headline
> **The engine is sound and the design thesis holds up.** Cover is the single biggest lever (it roughly *halves* lethality), and — the big one — **in a terrain-free 1v1, combat specialists crush the utility builds**. That's not a bug: it's proof that **[[Terrain|terrain]] and scenario objectives *must* carry the balance**, exactly as the pillar says. Two dials want attention: the **Stress/Nerve** system barely fires, and **mobility/utility needs scenario structure to be worth taking**.

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

## 7 · Stress / Nerve — barely fires ⚠️ — [[Morale]]
Fight length and how often a unit *cracks* under Stress:

| Matchup | Avg rounds | Cracks / fight |
|---|:---:|:---:|
| Jack vs Jack (WND 1) | 2.1 | 0.000 |
| Gunner vs Brawler (WND 1) | 1.4 | 0.000 |
| Jack vs Jack (WND 3) | 8.2 | 0.000 |

> [!warning] Dial to tune
> The Stress/Nerve system **almost never triggers** in a 1v1 — even in long WND-3 fights. Two reasons: (1) at WND 1 fights end on the first wound before Stress can build, and (2) the End-Phase Nerve test **sheds NRV-worth of Stress every round**, so it drains faster than a single attacker piles it on. As modelled, morale is inert.
> *Caveat:* the sim only models Stress from being wounded/pinned — the full [[Morale]] rules add more triggers (targeted by ranged, friendly Down in LOS, losing melee). In a **multi-model** game those stack much faster, so this may self-correct at real crew scale. But it's worth a deliberate test: if we want Stress to matter, we likely need **more/heavier triggers, slower shedding, or a lower crack threshold**.

## Design takeaways
1. ✅ **Engine is locked-in correct** — no maths surprises.
2. 🗺️ **Terrain/objectives are load-bearing for balance, confirmed** — build the scenario deck to demand INT/AGI, or utility builds are dead weight.
3. 💥 **Cover > armour for survival** — good, on-pillar.
4. ⚔️ **Charge and the defender tie-edge both matter** — melee has real texture.
5. ⚠️ **Stress/Nerve needs a tuning pass** — currently near-inert 1v1; retest at crew scale before deciding.
6. 🎯 **Watch Heavy Gunner** as a potential auto-include; price it and gate it with terrain.

---
*Next passes worth running: multi-model crew fights (does Stress wake up?), the same duels **with cover** (does the Grabber/Techie survivability change?), and points-cost balancing once [[List Building]] numbers exist.*

See [[Rules Engine]] · [[core-000 Core Test]] · [[Shooting]] · [[Melee]] · [[Damage]] · [[Morale]] · [[Terrain]].
