---
type: rule-phase
phase: "14"
stage: S2 Core Combat
status: Drafted
build_order: 8
depends_on: ["Unit Design", "Movement"]
feeds_into: ["Damage"]
tags: [settlements/phase, settlements/stage/s2]
---
# 14 · Melee
> **S2 Core Combat** · status **Drafted** · build order **8**

**Depends on:** [[Unit Design]], [[Movement]]
**Feeds into:** [[Damage]]
**Raw dependency (from Notion):** Unit Design, Movement

## Focus
Close combat — engagement, the fight sequence, and positional modifiers.

The Rules column should nail down:
- What counts as "engaged" (range), and how combats start (charge vs being in reach).
- The melee sequence: who strikes first (Initiative / charging), simultaneous vs alternating blows.
- Which stat drives melee (Strength) and any defence/parry interplay.
- Positional modifiers: charging, flank/rear, outnumbering, high ground, terrain.
- The melee-weapon profile fields and how they differ from ranged weapons.
- How the result feeds into the shared Damage sequence (don't duplicate damage logic here).

## Inherits from the engine
> [!info] Recall — melee resolves as an **opposed** core test (Strength; ties go to the defender). A unit is **Engaged** within **1"** of an enemy.

![[core-000 Core Test#Text]]

Engagement conventions → [[Rules Engine#House Conventions]] (Engaged within 1"; enter by Charge or Move-in).

## Working rules / decisions

### Engagement
A unit is **Engaged** while within **1"** of an enemy. You reach it two ways:
- **Move in** (Move slot, no LOS needed) → enter the enemy's **1" zone**. You may move *within* the zone but can't enter and leave it in the same move. Then **Fight** with your Action — a straight opposed attack, no bonus.
- **Charge** (both slots, LOS required) → extra reach *and* a free attack at **+1** (below).

### Melee attack (opposed)
Melee is an **opposed** test — a brawler really is harder to hit than a shaking medic, because you *can* dodge a blow (you can't dodge a bullet):

`Attacker 1d10 + STR` vs `Defender 1d10 + STR`

- **Highest total wins. Ties go to the defender.**
- Some weapons/skills swap the stat — a knife or agile skill may use **AGI**; a heavy weapon is **STR only** (see [[Weapons]]).
- The **winner lands the hit** → **Injury roll** (see [[Damage]]).
- **Facing does not apply in melee.** Once Engaged, either fighter attacks regardless of which way the models face.

### Charging
- **Charge** = both slots. Requires **line of sight** to the target (the path need not be straight). Move up to **2× MOV"** into the enemy's 1" zone, then a **free melee attack at +1** — the surprise bonus.
- A unit that was just charged, or that started the turn already Engaged, gets **no** charge bonus.
- **Charge vs Move-in:** charging needs LOS (terrain blocking sight blocks the charge) and grants +1; moving in works anywhere but gives no bonus. That's the trade.

### Losing a melee
The loser gains **+1 Stress** (see [[Morale]]).

## Rule ledger
- [[core-003 Melee]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
