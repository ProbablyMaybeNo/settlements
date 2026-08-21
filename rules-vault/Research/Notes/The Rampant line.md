---
type: research-note
title: The Rampant line
game: Lion Rampant / Dragon Rampant / Xenos Rampant
publisher: Osprey Games
designer: Daniel Mersey
depth: 21 published unit builds reconciled arithmetically
tags: [settlements/research]
---
# 🎲 The Rampant line

> [!abstract] In one breath
> **Coarse integer atoms on a very small budget — and essentially no balance complaints, because legibility bought forgiveness.** Its most important contribution to us is the granularity lesson: when 24 points stopped being enough, Mersey **raised the budget to 30 rather than subdividing the atom.**

| | |
|---|---|
| **Designer · publisher** | Daniel Mersey · Osprey |
| **Budget** | **24 points**, 4–10 units (Lion / Dragon Rampant 1e & 2e; Xenos Rampant per detachment) |
| **Depth of read** | Xenos Rampant **verified arithmetically across 21 independent published builds** by two authors, all reconciling exactly |
| **Long-form** | `docs/POINTS-RESEARCH.md` §7.7 |

---
## Raise the budget, not the resolution

**Type:** Costing · **Take:** ⭐ steal — the most important row for the rescale

**Dragon Rampant 2e (Oct 2025) raised the warband from 24 to 30 points** because 24 *"never quite gave them enough scope to buy the units they wished to field along with the special rules they wanted"* — and grew the upgrade list from 16 to ~48. **[FACT]**

> **He solved granularity pressure by raising the budget, not by subdividing the atom.**

**Why it works.** Subdividing the atom means re-deriving every price and re-teaching every player. Raising the budget leaves every price legible and every relationship intact, and simply buys more room. It is the cheaper move by a wide margin — **when it's available.**

**For Settlements — the honest read.** Our 100 → **1000** rescale is the *other* move, and it is still the right one, for a reason Mersey's game doesn't face: **we need headroom for multipliers and conditional discounts to land on integers.** A ×0.75 discount on a 40-point characteristic is 30; on a 4-point characteristic it's 3, and the distinction between ×0.7 and ×0.8 disappears entirely. **[INFERENCE]** Rampant has no multipliers, so it never needed the resolution. **The corollary is the warning: if we rescale and then keep pricing in round tens, we have gained nothing. Spend the granularity on the multipliers.** Compare [[Warmachine and Hordes#The MK2 to MK3 rescale]].

---
## Context pricing

**Type:** Costing · **Take:** ⭐ steal

The atomic layer is real and repeatable: **"Veteran" is +2 on every archetype it appears on**; Fearsome +2; Bloodthirsty +3, universally. Lion Rampant 2e archetypes: Elite Cavalry 6 · Elite Infantry 6 · Heavy Cavalry 4 · Heavy Infantry 4 · Archers 4 · Light Infantry 3 · Skirmishers 2 · Levied Infantry 1. **[FACT]**

**But it context-prices where it matters:**

> **Javelins are −1 on cavalry and +1 on foot** — the same widget, priced by its *net swing* on that chassis.

**Why it works.** It's a deliberate, small exception to an otherwise flat list, applied only where the same item genuinely does a different job. Compare [[Warhammer 40000#The full arc]], where the heavy bolter costing +5 on one squad and +15 on another was a *symptom* — because there the number was secretly pricing the slot. **The difference is whether you can say, in one sentence, why the two prices differ. Mersey can. GW couldn't.**

**For Settlements.** A defensible pattern for [[Weapons]]: a characteristic may carry a different price on a different weapon **class** if the swing genuinely differs — but the reason has to be stateable, or it's the 40k bug.

---
## Integers, and negative costs

**Type:** Costing · **Take:** 📎 reference

**No fractional costs exist anywhere in the line** **[NOT FOUND — checked LR1e, LR2e, DR1e, DR2e and both published and fan Xenos Rampant]**. Every cost is an integer. **What creates the impression of fine granularity is the routine use of negative-cost options.**

Dragon Rampant is the most explicit build system — base chassis plus purchased Fantastical Rules (Cleric 4, Spellcaster 4, Flying 3, Fear 2, Undead 2, Venomous 1, **Fearful −2**) with a hard clamp: *"no unit's cost may be boosted above 10 points or reduced below 1 point."* **[FACT]**

**The clamp is the piece worth stealing.** A floor and a ceiling on a *derived* cost is a cheap, universal guard against every stacking exploit at once — you never have to find the specific combination that breaks it.

**For Settlements.** A `min`/`max` clamp on any computed unit or weapon cost in `test-bench/points/` is one line of code and closes a whole exploit class. Related: refunds must be **smaller** than purchases, or negative traits become arbitrage (`docs/POINTS-RESEARCH.md` §8.9).

---
## The true failure mode of additive systems

**Type:** Costing · **Take:** ⚠️

**Verdict** **[CONSENSUS]**: essentially no balance complaints, because legibility bought forgiveness. The sharpest structural critique, on Xenos Rampant, names the real flaw:

> *"The points values of basic heavy and light infantry are **deceptively low**. Once you start adding upgrades the units become expensive."*

> **A cheap chassis barely constrains anything.**

**For Settlements.** Our rank bodies (Match Play 65/95/165/245) are the chassis. If the body is cheap relative to what it can carry, the body's price does no gating work and every crew converges on the same loadout hung off whatever frame is legal. That's a check to run against the costing engine — **what fraction of a fielded model's cost is the body?** — and it connects directly to the [[List Building]] pyramid doing the real work.

---
## Source

- Primary: Lion Rampant 1e/2e, Dragon Rampant 1e/2e, Xenos Rampant published cost tables and unit builds
- Long-form: `docs/POINTS-RESEARCH.md` §7.7
- Related: [[Wargaming Research Hub]] · [[Warmachine and Hordes]] · [[Bolt Action]] · [[Balance]]
