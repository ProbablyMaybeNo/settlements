---
type: rule-phase
phase: "03"
stage: S1 Foundation
status: Drafted
build_order: 3
depends_on:
  - Core Game Format
feeds_into:
  - Unit Design
  - Initiative & Activation
tags:
  - settlements/phase
  - settlements/stage/s1
---
# 03 · Rules Engine
> **S1 Foundation** · status **Drafted** · build order **3**

**Depends on:** [[Core Game Format]]
**Feeds into:** [[Unit Design]], [[Initiative & Activation]]
**Raw dependency (from Notion):** Format

## Focus
The timing + priority skeleton everything hangs on — get this clean before layering any rules on top.

The Rules column should nail down:
- The turn/round structure and the order of phases within a turn. Standard games = 6 turns.
- How priority/initiative is decided each turn (dice roll + underdog +1) and what winning it grants.
- The universal action economy (activations per unit; leaders/champions may get more; what an activation buys).
- The ONE core dice/resolution mechanic every other system reuses (how a test, hit, or save is rolled).
- Where Morale / Fear / Insanity hook into the timing (e.g. modifying the initiative phase).
- House conventions every section assumes: measuring (pre-measure?), rounding, line-of-sight basis.
## Working Rules / Decisions

### Turn / Round Structure
- Standard game length = 6 rounds.
- Each round consists of:
  1. Priority Phase
  2. Alternating Activations
  3. End Phase
- End Phase:
  1. Refresh Actions, Orders and Reactions.
  2. Resolve persistent conditions (Fire, Poison, etc.) — see [[Conditions]].
  3. **Break tests** — every unit with **2+ Stress** tests (1 Stress = Shaken, no test). See [[Morale]].
  4. Score objectives / victory points.

---

### Priority
- Both players roll:
  - 1d10
  - +1 if they have fewer surviving models.
- Highest result chooses whether to activate first or second this round.
- Ties are re-rolled.

---

### Universal Action Economy
Each activation is **one Move slot + one Action slot**.

- **Move** (slot 1): up to **MOV"**. Any direction, around obstacles; may not be split before/after the Action. A unit is never forced to move.
- **Action** (slot 2): Shoot, Fight, Interact, Hide, Stabilize, etc. It may **not** be a second normal Move, and a unit makes at most **one attack per activation**.
- **Sprint** (both slots): move up to **2× MOV"**, nothing else.
- **Charge** (both slots): move up to **2× MOV"** into base contact, then a **free melee attack** at the charge bonus. See [[Melee]].

#### Orders
- **Recruits and Fighters have none · Specialists have 1 · Leaders have 2.**
- An Order grants a **free Action or Reaction** to the issuing unit or another friendly unit.
- Orders can't chain (an ordered action can't itself be an Order).
- **Orders are issued only during the issuing unit's own activation.** *(Locked 2026-07-13.)*
- Each unit may **receive only one Order** per round.

> [!success] Why Orders are activation-bound
> A 4-model elite crew gets 4 activations **plus** 4 banked **Ready** tokens — every fighter effectively shoots twice, which is the right ceiling against a swarm's extra activations. Letting a Leader issue Orders *at any time* would push that to 7 shots from 4 models, and would turn Reactions into a gotcha — a unit with no Ready suddenly snapping into overwatch the instant you enter its LOS. **Ready already persists across rounds**; bank it on your own activation. See [[Initiative & Activation#Ready]] and [[Crew Sim — Findings]].

#### Reactions
- Full Ready / Reaction rules live in [[Initiative & Activation]].
- Summary: Ready via Action or Order → react once when an enemy ends a Move/Action in your forward LOS → Snap Shot, Charge, Throw, Interact, or Trigger.
---

### Universal Resolution Mechanic

#### Standard Test

```
1d10 + Stat + Modifiers

7+ = Success
```

- This mechanic is used for all attacks, skill tests, terrain interactions and objective interactions.
- Natural **1** = Automatic Failure.
- Natural **10** = Automatic Success.

Example:

```
Shoot

1d10 + Dexterity + Positive Modifiers - Negative Modifiers

7+ = Hit
```

Example:

```
Standard fighter shooting an enemy behind Heavy Cover

1d10
+1 Dexterity
-2 Heavy Cover

Needs 8+ on the die to hit.
```

- Terrain and cover are intended to have a major impact on gameplay. Well-positioned units should be extremely difficult to hit.
- **Armor never affects the hit** — it only reduces the **Injury roll**. Cover protects against *being hit*; armor protects against *being hurt*. See [[Damage]].

### Combat — two rolls
Every attack resolves in two steps:
1. **Attack roll** — *did it land?* Ranged = `1d10 + DEX + mods vs 7+` (cover is a negative modifier; weapons rarely add to hit). Melee = **opposed** (see [[Melee]]).
2. **Injury roll** — *how bad?* `1d10 + Weapon Damage − Armor vs 7+`. **Pass** → target loses 1 WND (**Down** at 0 WND). **Fail** → target is **Pinned** (+1 Stress). Full detail in [[Damage]].

> [!info] The engine in one line
> **Stats decide if you land it · Weapons decide how bad it is · Skills decide what else happens.** Terrain and Stress sit on top as pressure.

#### Opposed Tests

Some situations use opposed rolls instead.

```
1d10 + Stat + Modifiers
```

Highest total wins.

- Ties are won by the defender.
- **Melee attacks are opposed** (STR vs STR/AGI) — see [[Melee]]. Ranged attacks use the fixed 7+ target instead, because you can't dodge a bullet — cover is your defence.

---

### Nerve / Stress
- Fear, suppression and morale are all handled by the **Stress** system, tested against **NRV**.
- **1+ Stress = Shaken:** −1 to all rolls (always-on). **2+ Stress:** also a **Break test** in the End Phase.
- Stress does **not** affect Priority.
- Full rules: [[Morale]].

---

### House Conventions
- Pre-measuring is always allowed.
- **Facing & ranged LOS:** every model faces a direction — use the miniature's orientation (head / weapon / torso toward the front). A unit has a **180° forward arc**. **Ranged** attacks, Ready triggers, and other shoot-based actions need the target in that arc **and** true LOS. No facing notches required — how you place the model *is* the facing.
- **Melee ignores facing.** Once Engaged, you fight normally regardless of which way either model faces.
- Measurements are always Base Edge to Base Edge.
- A unit is **Engaged** while within **1"** of an enemy; you fight enemies you're Engaged with. Direct interaction with terrain/objects needs base contact.
- Enter melee by **Charging** (needs ranged LOS to declare) or a normal **Move** into an enemy's 1" zone (no LOS needed); reposition *within* that zone, but leaving it is a **Disengage** ([[Movement#Disengaging]]).
- Standard movement and range increments are based around 6".
- Always round down.

## Rule ledger
- [[core-000 Core Test]] — the resolution mechanic, distilled + probability table

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
