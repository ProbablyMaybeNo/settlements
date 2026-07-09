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
Stress represents fear, panic, suppression and shock. It is tracked as points on a unit and tested against **NRV**.

**A unit gains +1 Stress when it:**
- Is targeted by a ranged attack (hit *or* miss)
- Is hit by a ranged attack
- Loses a melee
- Gains a negative condition (Fire, Poison, Pinned, etc.)
- Has a friendly go **Down** within line of sight

### Nerve test — End Phase
Every unit with **1+ Stress** tests:

`1d10 + NRV` — if the result is **under its Stress total**, the unit **cracks**.

The **margin of failure** sets the severity:

| Fail by | State |
|:---:|---|
| 1–2 | **Shook** |
| 3–4 | **Bolt** |
| 5–6 | **Break** |
| 7+ *(or Nat 1)* | **Insanity** |

- **Pass →** the unit steadies: remove Stress equal to its **NRV** (min 0).
- **Natural 10 →** auto-steady, clear **all** Stress.

### Nerve states
Full status entries in [[Conditions]]:
- **Shook** — −1 to all rolls until end of round.
- **Bolt** — flees toward the nearest board edge, hugging cover.
- **Break** — freezes; cannot act.
- **Insanity** — attacks the nearest model, friend or foe (Shoots if DEX > STR, else Charges).

### Recovery
A Nerve state clears at the End Phase (re-test), when a friendly moves into base contact and **Interacts**, or via a Leader/Specialist **Order**.

## Rule ledger
- [[core-006 Morale and suppression]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
