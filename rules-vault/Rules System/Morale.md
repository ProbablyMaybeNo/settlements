---
type: rule-phase
phase: "17"
stage: S2 Core Combat
status: Drafted
build_order: 11
depends_on: ["Damage"]
feeds_into: ["Scenarios", "Final Alpha", "Solo & Co-op", "Factions", "Edge Cases"]
tags: [settlements/phase, settlements/stage/s2]
---
# 17 · Morale
> **S2 Core Combat** · status **Drafted** · build order **11**

**Depends on:** [[Damage]]
**Feeds into:** [[Scenarios]], [[Final Alpha]], [[Solo & Co-op]], [[Factions]], [[Edge Cases]]
**Raw dependency (from Notion):** Damage

## Focus
When crews break — fear, insanity, bottling, rout, surrender. ✅ After this you have a playable combat skirmish.

The Rules column should nail down:
- Morale / Fear / Insanity tests: what triggers them, the stat used (Morale), and target numbers.
- Bottling: when a crew tests to flee the field — design it to be the NORM, not the exception.
- Individual vs crew-wide effects (a single fighter pinned/fleeing vs the whole crew bottling).
- Insanity and Fear mechanics and how they alter behaviour and tie back to the initiative phase.
- Recovery / rally rules and how leaders steady nearby fighters.

## Inherits from the engine
> [!info] This note **is** the source of the Stress system. The engine only reserves it: [[Rules Engine#Nerve / Stress]] (Stress does not affect Priority). Everything else lives below.

## Working rules / decisions

### Stress
Stress represents fear, panic, suppression and shock. It is tracked as points on a unit and tested against **NRV**. Stress does **two separate jobs** — a small always-on penalty, and a break test once it piles up.

**A unit gains +1 Stress when it:**
- Is targeted by a ranged attack (hit *or* miss)
- Is hit by a ranged attack
- Loses a melee
- Gains a negative condition (Fire, Poison, Pinned, etc.)
- Has a friendly go **Down** within line of sight

> [!info] More triggers are coming
> The sim shows Stress from combat alone barely fires in a 1v1 ([[Dice Mechanic — Sim Findings]]). That's expected — most Stress will come from **skills, hazards, terrain and scenario events**, which stack far faster at crew scale. Tune trigger *frequency* before touching the numbers below.

### Shaken — the always-on penalty
Any unit with **1+ Stress is Shaken: −1 to all rolls.** Flat, passive, no test — it does **not** grow with more Stress. This is the reliable "under fire, rattled, shooting worse" effect, and it is the *only* thing 1 Stress does. You risk actually breaking only once Stress reaches 2.

### Break test — End Phase, 2+ Stress
Every End Phase, each unit with **2+ Stress** tests:

`1d10 + NRV − (Stress − 1)` vs **7+**

- The first Stress point is a free buffer — it costs you the −1, not the test.
- The **Shaken −1 does not apply to this roll.** Stress is already in the formula; don't double-count it.
- **Natural 10 →** auto-pass. **Natural 1 →** auto-fail.

- **Pass →** the unit steadies: remove **all** Stress.
- **Fail →** the unit **breaks** into the state set by its Stress level, then removes **1** Stress:

| Stress | Break state |
|:---:|---|
| 2 | **Bolt** |
| 3 | **Broken** |
| 4+ | **BugOut** |

**Chance of breaking** on a failed roll (`1 − pass%`):

| NRV | 2 → Bolt | 3 → Broken | 4 → BugOut |
|:---:|:---:|:---:|:---:|
| +0 | 70% | 80% | 90% |
| +2 | 50% | 60% | 70% |
| +4 | 30% | 40% | 50% |

### Nerve states
Full status entries in [[Conditions]]. A state governs the unit's **next activation**; it clears when the unit passes its next Break test or is steadied by Rally/Interact.
- **Bolt** — flees toward the nearest board edge, hugging cover.
- **Broken** — freezes; cannot act.
- **BugOut** — routs: moves full speed off the nearest board edge and is **removed from play** (a casualty).

> [!question] BugOut replaces the old "Insanity"
> The worst state is now a clean **rout off the table**, not attack-nearest-model. Fits the name and the gritty-realism pillar better than berserk-attacks-allies. Flag to revisit if you want the chaos option back.

### Recovery
Stress and Nerve states come off by:
- **Passing a Break test** (2+ Stress) → clears **all** Stress.
- A **Leader/Specialist Order** ("Rally") → clears all Stress on a friendly in range.
- A friendly moving into base contact and spending its **Action** to **Interact** → clears all Stress.

A unit sitting at exactly **1 Stress** never tests — it stays lightly **Shaken** until it climbs to 2+ (and passes a Break test) or is Rallied/steadied. Being rattled sticks until something clears it.

## Rule ledger
- [[core-006 Morale and suppression]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
