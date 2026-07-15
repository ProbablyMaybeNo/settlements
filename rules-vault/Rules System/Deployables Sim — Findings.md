---
type: reference
title: Deployables Sim — Findings
tags: [settlements/reference, settlements/analysis]
---
# 🛠️ Deployables Sim — Findings

First validation pass on the [[Deployables]] catalogue — turrets, mines, traps and beacons — against the core engine. Exact-math probabilities plus a Monte-Carlo cross-check that imports the [[Weapons|weapon]] battle engine. Run: `test-bench/deployables_sim.py` (seed `20260715`).

> [!success] Headline
> **The catalogue is clean — no ceiling breaks, and every item prices out against the sim-validated armoury.** One item was mispriced on the first pass (**Burst Turret**, undercosted at 16) and was corrected to **18** before locking. Two items are flagged to watch at the table — Burst and the Revive Beacon — not because they're broken, but because they touch the two most powerful levers in the game (multi-attack and casualty recovery).

## 1 · Nothing breaks the engine
Structural check passed on every deployable: no Damage over the **+4 ceiling**, no aura over the **±3 cap**, no range over **24"**, and every mine's `chassis + payload` cost adds up to the quoted number. **No deployable introduces a new dice mechanic** — a turret shot and a mine detonation are ordinary Injury rolls; a deploy is one INT test.

## 2 · INT is a real gate on deploying
`1d10 + INT + Build ≥ 7`, so the harder hardware genuinely needs a technician:

| INT | Simple +1 | Standard 0 | Complex −1 | Intricate −2 |
|:--:|:--:|:--:|:--:|:--:|
| **+0** (Rabble) | 50% | 40% | 30% | 20% |
| **+2** (Specialist) | 70% | 60% | 50% | 40% |
| **+4** (Leader) | 90% | 80% | 70% | 60% |

A Rabble fumbles a Sniper Turret ~70% of the time; a Specialist stands it up half the time and better with a Breach Kit. **This is the INT-restoration the whole note exists for** — it works.

## 3 · Turrets price out — except Burst, now fixed
Expected **wounds/round** (open cover, unarmoured), against the Assault-Rifle body baseline (21 pts → 0.42 w/rd → **0.0200 w/rd/pt**):

| Turret | w/rd | Cost | w/rd/pt | Verdict |
|---|:--:|:--:|:--:|---|
| Autoturret | 0.28 | 12 | 0.0233 | fair |
| Sniper | 0.35 | 15 | 0.0233 | fair (24" reach) |
| **Burst** | 0.48 | ~~16~~ → **18** | ~~0.0300~~ → 0.0267 | **was HOT — repriced** |
| Blast | 0.28 | 14 | 0.0200 | fair (shines vs clusters) |
| Reinforced | 0.28 | 15 | 0.0187 | fair (pays for durability, not DPS) |

Turrets sit slightly above the body's raw output-per-point — correct, because they cost **zero activation** after setup and fire 360°, and the discount is their **one-hit fragility**. The Monte-Carlo (turret vs an advancing rifleman over 6 rounds) matched the analytic numbers within 1–4 points (73 / 88 / 93 / 63 / 73%), confirming a turret kills ~0.6–1.0 bodies *if it survives to contact* — which a single hit prevents.

> [!warning] Watch Burst at the table
> Multi-shot is the biggest DPS lever in the game ([[Skill Sim — Findings]]). Even repriced to 18 and gated behind an **Intricate −2** build, two shots/round is the first thing to re-check with real crews. Fallback already noted: one shot with **Spread**.

## 4 · Mines land hard but are one-use and avoidable
A Proximity + Explosion mine (9 pts) auto-applies a **70%** wound vs unarmoured on the model that trips it (no to-hit roll), plus 2" Blast — but it is single-use, stationary, and visible if the deploy failed. That is in line with the **Molotov** (9 pts, one use). Fire/Poison/Shock/Smoke payloads route to existing hazards and conditions.

| Payload | Damage | vs none | vs light | vs heavy |
|---|:--:|:--:|:--:|:--:|
| Explosion | +3 | 70% | 60% | 50% |
| Fire | +2 | 60% | 50% | 40% |

## 5 · Beacon auras are ~+10% each — the brakes matter
Each ±1 aura moves the relevant roll about **10%** per affected ally. That is cheap and strong **if allies cluster**, which is why two brakes are load-bearing: standing hardware eats **both** equipment slots, and **a model benefits from at most two beacon auras at once**. Confirm both bite at the table.

> [!warning] Revive Beacon is the high-swing item
> Returning **Down** units in a **WND-1** game is a real momentum lever. It is bounded to *one unit, to Prone, Down-only (a melee Out stays dead)* and priced at 12 with an Intricate build — but if it makes games grind, cut it to a flat Med/Cleansing effect.

## Verdict
**Locked for playtest.** Every cost is a first-pass anchor validated against proven-balanced gear, not yet seen at a table. The next sim is crew-integration: turrets, mines and beacons inside the full [[Crew Sim — Findings|crew battle loop]] to measure win-rate swing, once first playtests show how the deploy-Action tempo actually feels.

---
See [[Deployables]] · [[Weapons]] · [[Rules System MOC]].
