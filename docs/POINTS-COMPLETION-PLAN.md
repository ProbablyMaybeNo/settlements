# Global Points System — Completion Plan

**Created 2026-07-30.** Seven milestones to take the costing system from ~40% populated to complete enough that a new weapon, skill, unit, condition or structure can be priced accurately from the table alone.

Work them **in order**. Several are gated on a decision that belongs to Ross — those are marked **🚦 DECISION GATE** and you must **stop and ask**, not choose.

---

## Ground rules

1. **The live rules vault is `C:\Users\Admin\Documents\Obsidian Vault\Settlements\Rules System\`.** The repo's `rules-vault/` is an auto-overwritten mirror — **never edit it.**
2. **The costing engine is `test-bench/points/`** — `ticks.py` holds the atoms, and every value in it is currently marked *"legacy ×10"*, meaning inherited from the old hand-set table, **not derived**. Changing a number there changes the whole catalogue.
3. **Balance harnesses live in `test-bench/balance/`** (2.5D, via `test-bench/engine2d/`). They are how claims get verified. Re-run rather than reason.
4. **Never state a number you have not measured or read in a file.** If something is unpriced, write "unpriced", not an estimate.
5. **When you make a mistake, log it** to `C:\Users\Admin\.claude\CLAUDE-ERRORS.md` using the schema at the top of that file.
6. Commit per milestone. Do not push to `main` without asking.

---

## Measured data — 2026-07-30

**This is the only written record of these measurements.** All from `test-bench/balance/` against the 2.5D engine, sides swapped.

### Primitive exchange rates
Free +1 given to one side, win-rate delta per model buffed, averaged over realistic all-armed lists (4 / 6 / 8 models):

| Primitive | medium | dense | **relative to +1 Damage** |
|---|:--:|:--:|:--:|
| **+1 to-hit** | +1.44 | +1.87 | **1.50×** |
| **+1 Damage** | +1.17 | +1.06 | **1.00×** |
| **+1 Armour** | +0.98 | +1.27 | **1.01×** |
| **+1 Stress** | +0.57 | +0.44 | **0.45×** |

**Why to-hit beats damage:** average cover is ≈ −1.1, so the hit roll (~49%) is the bottleneck against the injury roll (~70%). A multiplicative engine rewards fixing the bottleneck. `P(kill) = P(hit) × P(injure)`.

**Anchoring on +1 Damage = 15 Goods:** to-hit **22** · Damage **15** · Armour **15** · Stress **7**.

### Other measurements
- **Rate of Fire 2** ≈ **+50** on a 100-Goods weapon class. Measured by rebuilding the list to pay for it (dropping a 12-point model returned the crew to baseline: −3/−2/−6). **RoF 3 is unpriced.**
- **Stress context:** of all hits landing, the target was already at 0 Stress 26.5% / 1 Stress 33.5% / 2 Stress 24.9% / 3+ 15.1% (medium density).
- **Armour is archetype-neutral** — per model it is worth 1.6 to an elite crew and 1.24 to a swarm (only 1.3× apart), where offensive primitives are 3.5–4.6× better on elites.
- **Stat allocation** (`engine2d/run.py statsys`): GENTLE (strong primary + one real secondary) **beats** SPREAD (one spike + dabbles) **by 26 points**, and edges STACKED by 4.6. **Forced maximal spread produces the weakest crews. +1 dabbles are near-dead weight.**
- **Scenario scoring is the dominant balance lever.** Objectives scored by *presence*: 68-point spread. Scored by *Action + test*: 37–40. Nothing else tested came close.
- **Negative results — do not revisit without new evidence:** body repricing (Recruit 5→12, Fighter 8→20) moved the spread only 30→25 across a 2.4× range; removing Knockback moved it 3 points; varying *which stat* an objective tests changed nothing measurable (board presence is the binding constraint, not the test).

---

## Milestone 1 — Fold the measured primitives into the engine

**Goal:** `test-bench/points/ticks.py` reflects measurement instead of legacy inheritance.

**Do:**
- Set the injury atom from the measurement: **+1 Damage = 15**, so `Brutal` and `Armour Piercing` become **15**, not 40.
- Add an explicit **to-hit atom of 22** (unconditional +1 to hit). `Accurate` and `Spread` are conditional versions — apply the ladder in Milestone 4's method, provisionally ×0.8 → **18**.
- Add a **Stress atom of 7**.
- Add **`rate_of_fire_2 = 50`**. Leave RoF 3 out with a comment that it is unpriced.
- Update `docs/POINTS-TABLE.md` §5 to match, and mark every changed row **[measured]**.

**Done when:** `py -3.13 -m points` regenerates the catalogue without error, and `verify.py` passes or its failures are reported.

> ⚠️ This will move most weapon prices **downward** — Brutal alone drops 25 per weapon. Report the before/after catalogue diff; do not smooth it.

---

## Milestone 2 — Resolve the armour discrepancy 🚦

**The problem:** measurement puts +1 Armour at **1.01× +1 Damage** (so ~15 Goods per point). `ticks.py` prices Light armour (−1) at **60** and Heavy (−2) at **100**. That is a **4× gap**.

**Do first (autonomous):** re-run `test-bench/balance/primitives.py` and `melee_armour.py` and confirm both results still hold against current `ticks.py`.

**Complicating evidence — both are real:**
- Given free, +1 Armour is worth +13.8 win% to a melee crew.
- *Paid for in bodies*, armour loses: an armoured 8-model melee crew beats a bare 11-model one only 37.9% of the time (1D). But in **2.5D** the armoured 7-model crew matched the bare 11 (63% vs 67% mean) — **the 1D result was an artefact.** Trust the 2.5D number.

🚦 **STOP AND ASK.** Armour is on the defensive side of every fighter; a 4× move reprices the entire game. Present the evidence and let Ross set the number.

---

## Milestone 3 — Range bands

**Goal:** replace the implicit linear treatment of range with the threshold structure the evidence shows.

**Established:** 18"→24" is worth **60**, derived twice independently — `Long Range` costs 60, and Heavy Ranged = Standard + 6" + built-in Cumbersome (`140 = 100 + 60 − 20`). But 8"→18" is worth only ~20. **Range value accelerates toward the ceiling because 24" equals the deployment distance.** A second threshold exists near **12"**: a rifle at 18" closes 6" and fires on turn one; a pistol at 8" must cross 16" and cannot.

**Do:**
- Write range as **bands** in `ticks.py`, not a per-inch rate.
- Fix `Short Range` so the refund scales with what is lost: currently a flat −30 whether it halves 8" or 24". Suggested: Sidearm/Thrown **−20**, Standard **−30**, Heavy **−70** (a Heavy losing 24"→12" loses the threshold entirely).
- Document both thresholds (12" and 24") in `POINTS-TABLE.md` §4 as costing preconditions, not priced features.

---

## Milestone 4 — Conditions, individually 🚦

**The problem:** every payload (Fire, Poison, Blind, Shocked, Off-Balance, Hobbled) is flat-priced at 30 by grouping. Ross has explicitly rejected tier-grouping — *"how do we make sure each skill in a tier provides the same level of benefit without making them boring."* The same objection applies here. **Bleed is a death clock at WND 1; Blind is a temporary penalty. They cannot share a price.**

**Do:**
- Extend the 2.5D engine to model each condition distinctly (several are currently stubbed).
- Measure each one's win-rate contribution using the `primitives.py` method — free buff, per model, sides swapped.
- Price each from its measured value against the +1 Damage = 15 anchor.

🚦 **STOP AND ASK before extending the engine** — implementing conditions changes the simulator that every other result rests on, and the implementation choices are design decisions.

---

## Milestone 5 — The skill costing method 🚦 **(the keystone)**

**Why it matters most:** ~150 skills are uncosted, **and the stat ladder depends on them.** `POINTS-TABLE.md` §2 prices the 2nd/4th/6th point in a stat using tier values of 20/35/55 — the game's Advance prices, which are estimates. Ross wants skills costed individually from their rules. Once they are, those tier numbers become *outputs* and the ladder becomes real.

**Proposed method** (design it, get it approved, then apply):
```
skill cost = Σ(primitive values it grants) × conditionality multiplier
```
using the measured primitives above and the conditional ladder `L = (1 − f)/f`, where `f` is the fraction of activations the skill's condition is met. **`f` is measurable** — instrument the trait in the sim and count. No published game does this; every one of them guesses.

**Guardrails:**
- **Action-economy skills cannot be priced** — one extra attack is a ×1.58 on output, ~81% of the value of maxing every stat and damage cap at once, and the existing Skill Sim measured Quick Shot at **+24 win%**. These stay **rank-gated, never sold.**
- Skills that grant `+1 WND` or `+MOV` likewise gate rather than price.

🚦 **STOP AND ASK once the method is drafted and demonstrated on 5 skills.** Do not process all 150 before the method is approved.

---

## Milestone 6 — Structures ⛔ BLOCKED

**Blocked on `Economy.md`, which is an empty file.** Do not attempt.

Structures cannot be priced on the battle-layer anchor — a Storehouse buys zero win probability. They need a **payback-period** anchor: cost in Materials against production per cycle. That requires inflow rates, which do not exist yet.

`ticks.py` already contains a `FOOTPRINT_BAND` / `ROLE_BAND` formula, but it is hand-set and unvalidated. Leave it and say so.

**When unblocked:** the 25 structures are catalogued in the vault's `Structures.md` with footprints, power draw and terrain lines.

---

## Milestone 7 — Additive or multiplicative? 🚦

**The open structural question**, currently `POINTS-TABLE.md` §9.

The engine is multiplicative, so a 100-Goods rifle delivers ~33% more kill probability on a DEX+4 Leader than a DEX+2 Fighter — **for the same price**. One Page Rules solves this by multiplying weapon cost by the carrier's Quality; verified 4/4 against their own worked examples.

**The tension:** a carrier-dependent multiplier means **a gun no longer has one price**, which conflicts with the single summable table Ross asked for.

**The test:** `test-bench/balance/suite.py` — run the elite Gunline against the Mob at equal points. Today's measurement says offensive primitives are worth **3.5–4.6× more per model on an elite crew**, which is a strong signal that flat pricing leaks. Quantify it, then present.

🚦 **STOP AND ASK.** This decides the shape of the whole system.

---

## Definition of done

The system is complete when someone can price, from the table alone and without judgement calls:

- [ ] a new weapon *(already possible)*
- [ ] a new weapon characteristic *(M1, M3, M4)*
- [ ] a new unit / stat line *(M5 — depends on skills)*
- [ ] **a new skill** *(M5)*
- [ ] a new condition *(M4)*
- [ ] a new deployable *(composable after M1/M4)*
- [ ] a new structure *(M6 — blocked)*

**Sequence:** M1 → M3 → (M2 gate) → (M7 gate) → (M4 gate) → M5 → M6 when Economy exists.

---

## Status — 2026-08-01

| Milestone | State |
|---|---|
| **M1** primitives into the engine | ✅ done |
| **M3** range bands | ✅ done |
| **M7** additive vs multiplicative | ✅ **CLOSED — additive** (`POINTS-DECISIONS.md` D21). The evidence contradicted the section's own prediction: elite lists drift *down* under flat pricing, so a carrier multiplier would push them further down |
| **M4** conditions, individually | ✅ **done.** Condition layer implemented in `engine2d/` and verified by `engine2d/test_conditions.py` (21/21). Nine payload/characteristic prices measured in `balance/conditions2d.py` and folded into `ticks.py`. Two traits measure at zero and are flagged as a **rules** defect — see `POINTS-TABLE.md` §5.5 |
| **M2** armour | ⚠ **re-open.** `ticks.py` and `POINTS-TABLE.md` §7 both cite `balance/armourprice.py` as the source of Light 30 / Heavy 60. **That file does not exist in the repo.** The number may be right, but nothing can re-derive it. Rebuild the sweep before the level is locked |
| **M5** skills | next — method approved as **measure-but-never-charge** (D22): each skill priced from its primitives, the price used as a **design band**, never as a purchase price |
| **M6** structures | unblocked by D23 — `Economy.md` is to be drafted as part of this pass, giving structures their second anchor (payback period in Materials) |

### Method note added by M4 — use mirror matches
Measuring a buff against a *fixed* opponent clips: if the baseline sits at 8% or 92% there is no room for the buff to move it, and every delta is compressed toward zero. **Mirror matches** (identical crews, one side buffed) have a 50% baseline by construction. Every low-value trait rose when the method changed. `primitives2d.py` and `realistic.py` both still use the asymmetric method, so **the M1 atoms inherit the same bias** and are candidates for re-measurement.

### Artefact caught in M4 — check the test lists can express the trait
Armour Piercing first measured at ~0. The cause was that **none of the test lists wore armour**, against which AP does exactly nothing by definition. A trait can only be measured in a configuration where it is able to act. `conditions2d.py` now carries an `ARMOURED6` list for this reason.
