---
type: rule-phase
phase: "16"
stage: S2 Core Combat
status: Drafted
build_order: 10
depends_on: ["Damage"]
feeds_into: []
tags: [settlements/phase, settlements/stage/s2]
---
# 16 · Conditions
> **S2 Core Combat** · status **Drafted** · build order **10**

**Depends on:** [[Damage]]
**Feeds into:** —
**Raw dependency (from Notion):** Damage

## Focus
Status effects that layer onto units — burning, pinned, suppressed, bleeding, etc.

The Rules column should nail down:
- The full condition list and what each one does mechanically.
- How conditions are applied, tracked (tokens), and removed/expire.
- Stacking rules and how conditions interact with each other.
- Which sources cause which conditions (weapons, terrain hazards, psychic/Mental).
- Realism-flavoured states tied to the setting (suppressed, bleeding, panicked) that reinforce the gritty tone.

## Inherits from the engine
> [!info] Recall — persistent conditions are resolved in the **End Phase** each round (engine turn structure). Define each condition's effect and expiry against that clock.

![[Rules Engine#Turn / Round Structure]]

## Working rules / decisions

A condition is a status token on a unit. Combat conditions come from [[Damage]]; Nerve states from [[Morale]].

### Combat conditions
- **Pinned** — must spend its **Move** to clear before acting; may still Shoot but can't Move/Charge/Sprint. Persists until cleared. Applying it gives +1 Stress.
- **Down** — prone and out of the fight; may be attacked again; Stabilize or bleed out (see [[Damage]]).
- **Hidden** — −3 to be hit. Gained by the **Hide** action in [[Terrain|Concealing terrain]] or from gear/skill; lost on moving, shooting, or being revealed.

### Nerve states (from [[Morale]])
- **Shaken** — any unit with **1+ Stress**: −1 to all rolls. Always-on, doesn't stack, no test. Clears when all Stress clears.
- **Bolt** — flees toward the nearest board edge, using cover. *(Break test fail at Stress 2.)*
- **Broken** — frozen; cannot act. *(fail at Stress 3.)*
- **BugOut** — routs off the nearest board edge and is removed from play. *(fail at Stress 4+.)*

### Persistent conditions (resolve in the End Phase)
- **Fire** — an Injury roll each End Phase until the unit spends an action to put it out; +1 Stress.
- **Poison / Bleed** — lose 1 WND each End Phase until treated.
- **Blind / Shocked** — −2 to actions for 1 round.

> [!question] The persistent-condition values (Fire/Poison severity and durations) are placeholders — lock them in playtest.

## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
