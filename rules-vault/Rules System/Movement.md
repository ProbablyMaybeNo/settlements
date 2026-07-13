---
type: rule-phase
phase: "07"
stage: S2 Core Combat
status: Drafted
build_order: 6
depends_on: ["Unit Design"]
feeds_into: ["Shooting", "Melee", "Terrain", "Edge Cases"]
tags: [settlements/phase, settlements/stage/s2]
---
# 07 · Movement
> **S2 Core Combat** · status **Drafted** · build order **6**

**Depends on:** [[Unit Design]]
**Feeds into:** [[Shooting]], [[Melee]], [[Terrain]], [[Edge Cases]]
**Raw dependency (from Notion):** Unit Design

## Focus
All the ways a model relocates — basic, vertical, through terrain, in combat, and forced.

The Rules column should nail down:
- Base move (from the Move stat) plus run/charge/advance variants and their costs/trade-offs.
- Vertical and athletic movement: climbing, jumping, leaping, swimming, falling — all driven by **Agility**.
- Moving through/over terrain: difficult ground, obstacles, squeezing through gaps.
- Movement around engagement: disengaging, falling back, and what (if anything) it provokes.
- Forced movement (push / knockback / drag) and how it interacts with terrain edges and falling.
- Measuring rules: pre-measuring allowed? base-to-base? — must agree with the Rules Engine conventions.

## Inherits from the engine
> [!info] Recall — baseline move and the measuring conventions are fixed by the engine (S1). Build run/charge/climb/fall on top; don't contradict these.

![[Rules Engine#House Conventions]]

## Working rules / decisions

### Basic move
The **Move** slot moves up to **MOV"** (baseline 6"), any direction, around obstacles. It can't be split around the Action, and a unit is never forced to move.

**Facing:** when you Move (including Charge / Sprint / Disengage), place the model facing its final direction as part of that move. You may also spend the **Move** slot to **change facing only** — no displacement — to aim your 180° arc ([[Rules Engine#House Conventions]]). Facing does not affect melee.

### Sprint & Charge
- **Sprint** (both slots): move up to **2× MOV"** — nothing else — no Shoot, no Ready. You may set facing at the end.
- **Charge** (both slots): move **MOV x2** into base contact, then a free melee attack at **+1** (see [[Melee]]). Declaring a Charge needs the target in your forward 180° + true LOS; once Engaged, facing no longer matters.

### Terrain movement
Open ground, marked stairs, and clear paths are normal movement — no test.

**Low leap** — leaping over an obstacle **under 2" tall** needs **no AGI test**, but always costs **2"** from your Move allowance for that activation (flat cost — a 6" curb and an 18" rail both cost 2"). Measure height at the narrowest point you cross.

**Athletic traversal** (everything else) uses an **AGI** test (`1d10 + AGI + mods` vs **7+**), paid from the **Move** slot (counts against MOV). These are **not** Interact Actions — see [[Terrain Interaction]] for STR/DEX/INT verbs.

| Maneuver | When | On fail |
|---|---|---|
| **Climb** | Ascending / descending **Climbable** terrain, walls, roofs, fire escapes | Stop at the base / last safe level; if already mid-climb, **fall** |
| **Jump / Leap** | Crossing a horizontal **gap**, or an obstacle **2" or taller** | Fall short — place at the near edge, or **fall** if you committed past it |
| **Vault** | Crossing a waist-high obstacle onto / over it (when not covered by low leap) | Bounce off — end short of the obstacle; no fall unless the far side is a drop |
| **Swim** | Entering or crossing **deep water** / swimmable hazard | End the move in the water; gain **Pinned** (or hazard effect from the scenario) |

- No job-difficulty modifiers — only skills, conditions, **Shaken**, etc.
- Skills may auto-succeed or soften fails (**Sure-Footed**, **Leaper**, **Vault**, **Water Walker**, **Like a Cat** — [[Skill Paths]]).
- Difficult ground costs double movement. *(exact categories in [[Terrain]].)*
- Fall damage / fall tests → [[Terrain]] (verticality).

### Disengaging
Breaking away from melee is a **Disengage** — it costs **both slots** (your whole activation):
- Move up to **MOV"** (6") in any direction.
- You **cannot end within 1" of *any* enemy** — not just the ones you left (no using Disengage to lock down a different enemy).
- **Every enemy you were Engaged with gets a free swing at −2** (you're ducking and scrambling clear).

> [!question] Double-cost check: both slots **and** free swings may make Disengage a dead option. Playtest whether the −2 swing is enough on its own, or if losing the whole activation should be the only cost.

## Rule ledger
- [[core-001 Movement]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
