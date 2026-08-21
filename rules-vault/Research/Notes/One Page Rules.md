---
type: research-note
title: One Page Rules
game: Age of Fantasy / Grimdark Future
publisher: One Page Rules
designer: Gaetano Ferrara
depth: official calculator recovered, verified 4/4
tags: [settlements/research]
---
# 🎲 One Page Rules

> [!abstract] In one breath
> **The most complete atomic costing system in modern tabletop, and the single most directly applicable find in the research.** Its whole formula was recovered and reproduces OPR's own worked examples exactly — and the one elegant thing it does (Quality adds to the base but multiplies every weapon) hands you correct offence/defence coupling for free.

| | |
|---|---|
| **Publisher · design** | One Page Rules · *Game Design: Gaetano Ferrara* |
| **Source document** | **"AoF: Point Calculator v1.10"**, 18pp, official. Paywalled behind Patreon Tier 3 and since removed from the public resources page; an archived copy was recovered and read in full |
| **Depth of read** | Formula implemented and **verified 4/4** against OPR's own worked examples |
| **Long-form** | `docs/POINTS-RESEARCH.md` §1.3 ⭐ |

---
## Quality adds, then multiplies

**Type:** Costing · **Take:** ⭐ steal — the single most elegant thing in the corpus

**Unit construction** **[FACT]**:

```
Base Cost       = (Quality + Defense) × X          where X = Tough(X), else 1
Total Unit Cost = (Base + Weapons + Special Rules) × Models
                → rounded to the nearest multiple of 5
```

**Weapon construction** **[FACT]**:

```
Weapon Cost = Range × Attacks × Special Rules
Total Cost  = Weapon Cost × Quality        ← the unit's Quality POINT VALUE, not its die number
```

Range multipliers: Melee 0.25 · 6" 0.125 · 12" 0.25 · 18" 0.375 · 24" 0.5 · 30" 0.625 · 36" 0.75 · 42" 0.875 · 48" 1.0. Weapon-rule multipliers: AP(1) ×1.5 · AP(2) ×2 · AP(3) ×2.5 · AP(4) ×3 · Blast(X) ×X · Deadly(3) ×2 · Deadly(6) ×4 · Indirect ×1.25 · Poison ×1.25 · Rending ×1.5.

**Because Quality is *additive* in the base but *multiplicative* on every weapon, while Defense enters only the base** **[INFERENCE — computed, 5 models with Bow + Hand Weapon]**:

| Quality | Cost | | Defense | Cost |
|---|---|---|---|---|
| 6+ | 37.5 | | 6+ | 45 |
| 5+ | 55.0 | | 5+ | 55 |
| 4+ | 72.5 | | 4+ | 65 |
| 3+ | 90.0 | | 3+ | 75 |
| 2+ | **160.0** | | 2+ | **115** |

> **A Quality step costs ~1.75× a Defense step, automatically, with no separate offence/defence budget.**

And `Tough(X)` multiplies the whole base but **not** weapons — so durability compounds while guns stay linear.

**For Settlements.** This is the concrete recommendation for our cost function: **DEX/STR should multiply the weapon's cost, not sit beside it.** A rifle in the hands of a Specialist genuinely *is* worth more than the same rifle on a Recruit, and **no additive table will ever say so.** We currently add everything — which is fine for weapon characteristics (they mostly land on different terms of the same product) and **wrong for skills, ranks, and anything touching the action economy.** See `docs/GLOBAL-POINTS-SYSTEM.md` and `test-bench/points/`. Same structural lesson as [[Song of Blades and Heroes#The Quality multiplier]] and [[BattleTech#Battle Value 2]] — **multiply the things that multiply, add the things that add.**

---
## The stat ladder doubles at the top

**Type:** Costing · **Take:** ⭐ steal

The identical lookup is used for both Quality and Defense **[FACT]**:

| Stat | 6+ | 5+ | 4+ | 3+ | 2+ |
|---|---|---|---|---|---|
| Points | 2 | 4 | 6 | 8 | **16** |

**+2 per step, then a doubling at 2+.** A deliberate super-linear term at the top of the ladder to make extreme stats **self-limiting**.

**For Settlements.** An alternative to a hard cap. Our stats cap at **+6** and our modifier cap at **±3**; a super-linear price on the last step would let extremes exist while making them genuinely expensive. Worth noting that GW independently reached the same conclusion in 1987 — see [[Games Workshop published formulas#Rogue Trader, 1987]].

---
## Points are not balance

**Type:** Production · **Take:** ⭐ steal

OPR ship a **second, orthogonal validator** **[FACT — patch notes, 26 Jan 2024]**:

> *"In order to make sure that individual units are not too overpowered, we use a simple system of comparing **how many potential wounds a unit can deal vs how many wounds the unit can take**."*

It drives the "balanced"/"not balanced" badges on community armies, and OPR concede unbadged armies *"may have wildly unbalanced units."*

> **Architecture: the formula sets the price; a damage-ratio cap catches what the formula misses.**

And they add a written guideline where maths can't reach **[FACT — from the calculator book itself]**:

> *"Avoid using Quality 2+ and 6+ because players feel like they are not very balanced, even if point costs compensate for the rolls."*

> **Costing the extremes correctly is not the same as making them fun.**

**For Settlements.** We already have the better version of the second instrument: `test-bench/` runs whole games in the 2.5D engine, which is a stronger validator than a wounds ratio. What we lack is the **badge** — a stated pass/fail criterion a list must meet. And the written-guideline point is worth taking literally in the [[Rulebook]]: some advice belongs in prose, not in the price list.

---
## Deltas and a coarse grid

**Type:** Costing · **Take:** ⭐ steal

- **Price upgrades as deltas** — `cost(new) − cost(old)`, **rounded up**. Kills the "sidegrade costs 0" exploit dead.
- **Round to a coarse grid** — nearest 5. Hides floating-point noise and keeps lists mentally addable.
- **Multiplicative rule modifiers self-scale** across cheap and expensive weapons — no per-weapon tables to maintain.

Special rules mix flat, derived and multiplicative forms **[FACT]**: Fear = 20 · Artillery = 15 · Impact(X) = 3X · Regeneration = 6×Tough(X) · Stealth = 2×Tough(X) · Wizard(X) = 20X+5 · Flying/Fast/Scout/Ambush = Quality · Slow = −Quality · Immobile = −3×Quality · Strider = Quality/2 · **Hero = 0** · Fearless = recompute the base at Quality+1.

**Round once, at the end.** [[BattleTech]] keeps full floating-point precision throughout and rounds only at the very finish; SoBH rounds each cell. **[INFERENCE]** The real argument for our 1000-point scale is not "more points is better" — it is **headroom for multipliers and conditional discounts to land on integers.** A ×0.75 discount on a 40-point characteristic is 30; on a 4-point characteristic it's 3 and loses the distinction between ×0.7 and ×0.8 entirely. **The corollary: if you rescale and then keep pricing in round tens, you have gained nothing. Spend the granularity on the multipliers.**

---
## Caveats

**[CONSENSUS]** Balance opinion is mixed — *"it's definitely easy to break if you want and some stuff is overpowered or underpowered"* versus *"surprisingly well balanced for what it is."* OPR's own 3rd-edition notes admit an offensive/defensive cost-ratio problem needing a global retune.

**[NOT FOUND / unverified]** The recovered v1.10 is ~2020, and a forum thread title indicates the live **Army Forge** engine has since **diverged** from the published book (thread body unreadable — search-index snippet only). A community reverse-engineering exists (`kdj0c/onepagepoints`, MIT) but is a *different, continuous* model — `defense_cost(d) = (0.9d² + d + 10)/2`, `ap_cost(ap) = 1.2^ap` — with two hard-coded fudge factors *"to match onepagerules current prices."*

---
## Source

- Primary: "AoF: Point Calculator v1.10" (official, archived copy), OPR patch notes
- Long-form: `docs/POINTS-RESEARCH.md` §1.3, §1.4, §8
- Related: [[Wargaming Research Hub]] · [[Song of Blades and Heroes]] · [[BattleTech]] · [[Balance]]
