---
type: rule-phase
phase: "13"
stage: S2 Core Combat
status: Drafted
build_order: 7
depends_on: ["Unit Design", "Movement"]
feeds_into: ["Damage"]
tags: [settlements/phase, settlements/stage/s2]
---
# 13 · Shooting
> **S2 Core Combat** · status **Drafted** · build order **7**

**Depends on:** [[Unit Design]], [[Movement]]
**Feeds into:** [[Damage]]
**Raw dependency (from Notion):** Unit Design, Movement

## Focus
The ranged attack sequence + weapon stats — pin down the to-hit and damage math.

The Rules column should nail down:
- The step-by-step ranged sequence: declare → check LOS/range → to-hit → saves → damage.
- Which stat drives ranged to-hit (Dexterity) and the target-number method.
- The ranged-weapon profile fields: range (or bands), attacks, strength/AP, damage, traits.
- Target-priority rules (closest visible? cover interplay) — a key lever for the terrain pillar.
- Modifiers: cover, range, moving vs stationary, elevation, suppression.
- Realism touches if wanted: ammo, reload, misfire/jam — kept streamlined to one die where possible.

## Inherits from the engine
> [!info] Recall — ranged to-hit **is** the core test (1d10 + Dexterity + mods, 7+). Cover and armour are negative modifiers on the die; don't invent a second dice method.

![[core-000 Core Test#Text]]

Worked cover × armour matrix already lives with the rule → [[core-000 Core Test#Worked example — a shooting matrix]].

## Working rules / decisions

### Ranged attack sequence
1. Declare a target in **range**, **true LOS**, and your **forward 180°** facing arc ([[Rules Engine#House Conventions]]).
2. Measure range vs weapon range.
3. **Attack roll:** `1d10 + DEX + modifiers` vs **7+**.
4. On a hit → **Injury roll** (see [[Damage]]).
5. A clean **miss** does nothing. A hit's outcome is the **Injury roll** (step 4): a wound, or **Pinned (+1 Stress)** if it fails to wound. **Only a hit that connects generates Stress** — see [[Damage]] / [[Morale]].

You may set facing for free as part of a Move (including a facing-only Move — [[Movement]]). Declaring Shoot does **not** itself rotate you — turn first if the target is outside your arc.

> [!info] The target can react. A **Ready** enemy you Shoot may **Dodge** — an opposed **AGI vs DEX** roll that, if it wins, negates the shot and lets it dive out of LOS (then Pinned). A Ready enemy in its own forward arc may **Snap Shot** back *after* your shot resolves. See [[Initiative & Activation#Reaction options]].

### Modifiers
- Cover: **Light −1 · Heavy −2 · Hidden −3** (see [[Terrain]]).
- Out of range or outside forward arc / no LOS: cannot target.
- **Weapons rarely add to hit** — only via a conditional trait such as **Accurate** (see [[Weapons]]). Stats decide the hit; weapons decide the injury.

### Firing while Engaged
- Most ranged weapons **cannot** fire while in base contact with an enemy.
- A **Sidearm** weapon may fire while Engaged, using DEX and targeting only the Engaged enemy (see [[Weapons]]) — facing still required toward that enemy.
- Some skills may give a unit the ability to fire while engaged.

## Rule ledger
- [[core-002 Shooting]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
