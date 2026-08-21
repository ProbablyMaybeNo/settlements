---
type: research-note
title: BattleTech
game: BattleTech
publisher: Catalyst Game Labs
depth: fully published, verified against open-source implementation
tags: [settlements/research]
---
# 🎲 BattleTech

> [!abstract] In one breath
> **The gold standard, and the only system in this research where the entire derivation is public, complete, and machine-checkable.** Battle Value 2 multiplies mobility and pilot skill, adds armour and weapons, and applies type multipliers per component.

| | |
|---|---|
| **Publisher** | Catalyst Game Labs |
| **Cost system** | **Battle Value 2 (BV2)** — fully published |
| **Depth of read** | Published derivation, **independently verifiable in open-source code** (MegaMek) |
| **Long-form** | `docs/POINTS-RESEARCH.md` §1.1 |

---
## Battle Value 2

**Type:** Costing · **Take:** ⭐ steal the shape

```
BV = (Defensive Battle Rating) + (Offensive Battle Rating)
   = (Defense × DefensiveFactor) + (Offense × SpeedFactor)
then × PilotSkillMultiplier
```

**Defensive side** **[FACT]**:

`Defense = 2.5 × ArmorPoints + 1.5 × StructurePoints + 0.5 × Tonnage (gyro)`

Each term carries a **type multiplier** — structure ×0.5 for Industrial/Composite, ×2.0 for Reinforced; engine ×1.0 standard, ×0.75 Clan XL, ×0.5 IS XL. Defensive equipment (AMS = 32, ECM, probes, pods) is a **flat additive block**. Explosive ammo and Gauss criticals **subtract**.

`DefensiveFactor = 1 + (max Target Movement Modifier / 10)` — verified in MegaMek source as `1 + (Math.max(tmmRunning, Math.max(tmmJumping, tmmUmu)) / 10.0)`.

**The structural lesson, and it is the most consistent one across every system examined:**

> **Multiply the things that multiply. Add the things that add.**
>
> Mobility and crew quality are **multipliers**. Armour and weapons are **addends**.

The same shape appears independently in [[Song of Blades and Heroes#The Quality multiplier]] (`(5×Combat + ΣAbilities) × (7−Quality)/2`), [[One Page Rules#Quality adds, then multiplies]] (weapons × Quality), and Hero System (advantages multiply, limitations divide). **Four systems, no shared lineage, same architecture.**

**Round once, at the end.** BV2 operates in the ~500–3,000 range per unit and **keeps full floating-point precision throughout, rounding only at the very finish** (0.5 rounds up). **[FACT]**

---
## The threshold bug, unfixed in published form

**Type:** Costing · **Take:** ⚠️ instructive failure

BattleTech has the same breakpoint problem every points system has, and it is visible in print: **weapons dealing 60+ damage get a flat 20% BV bonus.** **[FACT]** So the AC/20 pays a threshold premium and the AC/10 pays nothing, **with no gradation between.**

> **Thresholds are the one failure mode no points system anywhere has solved with points.** Every game examined solves them by **hard cap, hard gate, or removal** — never by charging more.

**For Settlements.** We discovered this independently: the 24" range ceiling exists because a sim found an uncapped long-range crew *"beat every list by 13–30 points **at any price**."* **The design instruction: enumerate the game's breakpoints explicitly, and put a gate on each. Do not attempt to price them.** See [[Weapons]], [[List Building]] and `docs/POINTS-RESEARCH.md` §6.1.

---
## Why it matters that this one is public

Every other system in this vault is either unpublished ([[Infinity]], [[Malifaux]], [[Gaslands]], [[Warmachine and Hordes]]), recoverable but not stated ([[Song of Blades and Heroes]]), or officially published and then withdrawn ([[One Page Rules]]). BattleTech is the only one where you can read the formula, read an open-source implementation of the formula, and check them against each other.

**For Settlements — the practical read.** Our costing engine (`test-bench/points/`) plays the role MegaMek plays here: **the executable statement of the derivation.** That makes engine/doc divergence a correctness bug, not a documentation nit — and we currently have one on record (`points/ticks.py` carries armour at 30/60 while the master note says **60/100**, re-measured 2026-08-05). Fix the engine.

---
## Source

- Primary: published BV2 rules; MegaMek open-source implementation
- Long-form: `docs/POINTS-RESEARCH.md` §1.1, §6.1
- Related: [[Wargaming Research]] · [[One Page Rules]] · [[Song of Blades and Heroes]] · [[Balance]]
