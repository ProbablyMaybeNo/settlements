---
type: rule-phase
phase: "12"
stage: S2 Core Combat
status: Drafted
build_order: 5
depends_on: ["Rules Engine"]
feeds_into: []
tags: [settlements/phase, settlements/stage/s2]
---
# 12 · Initiative & Activation
> **S2 Core Combat** · status **Drafted** · build order **5**

**Depends on:** [[Rules Engine]]
**Feeds into:** —
**Raw dependency (from Notion):** Rules Engine

## Focus
Whose turn it is and how units act — the alternating-activation loop and any reactions.

The Rules column should nail down:
- The activation model: alternating activation; ~2 activations per unit; leaders/champions sometimes more.
- How initiative is rolled and applied each turn, including the underdog edge.
- Action-economy detail: what a single activation lets a unit do (move + one action? two actions?).
- Out-of-activation rules: reactions, overwatch, interrupts — or explicitly none, to keep it clean.
- A catch-up / rubber-band rule so a larger crew can't simply burn through your activations and then dogpile.

## Inherits from the engine
> [!info] Recall — the activation skeleton is set in [[Rules Engine]] (S1). Refine it here (reactions/overwatch, a catch-up rule so a bigger crew can't dogpile); don't restate it.

![[Rules Engine#Turn / Round Structure]]

![[Rules Engine#Priority]]

![[Rules Engine#Universal Action Economy]]

## Working rules / decisions

### Activation
- Players **alternate**, activating one unit at a time. Who activates first each round is set by the **Priority** roll ([[Rules Engine#Priority]]).
- Each activation = **Move slot + Action slot** ([[Rules Engine#Universal Action Economy]]). One attack per activation.

### Reactions (Ready)
- A unit spends its **Action to Ready**, or receives a Reaction via an **Order** (Specialist 1 / Leader 2).
- It reacts **once**, interrupting, when an enemy enters its line of sight or takes an exposed action (crosses a gap, opens a door, shoots, charges, triggers terrain).
- Options: Snap Shot, Charge, Throw, Interact, Trigger.

> [!question] Catch-up: with alternating activation, a bigger crew can finish activating and dogpile the last models of a smaller one. Playtest whether the underdog **+1 Priority** is enough, or if the outnumbered side needs a small surge/hold rule.

## Rule ledger
- [[core-005 Activation order]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
