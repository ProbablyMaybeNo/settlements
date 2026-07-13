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

### Ready
- A unit gains **Ready** by spending its **Action** on Ready, or by receiving Ready from an **Order** (Specialist 1 / Leader 2).
- **Move then Ready** is legal (Action only).
- A unit may have **at most one Ready token**. Spending it clears the token. It may gain Ready again later that round (another Ready Action, or an Order) — never two tokens at once.
- Ready **persists across rounds** until spent or cancelled.
- **Cancelled** when the unit:
  - takes any other Action (Shoot, Fight, Interact, Hide, Stabilize, etc.), or
  - is **hit** by an attack, a hostile hack effect, or a terrain/hazard effect (Injury pass, condition applied, feature shut-out that lands, etc.).
- Sprint / Charge consume both slots and leave no Ready; starting a Sprint or Charge cancels Ready.

### Reaction triggers
A Ready unit may react **once** (spend the token) **after** an enemy finishes a Move or Action, if all are true:
1. The enemy (or the relevant terrain trigger) is in the reactor's **forward 180°** and **true LOS** ([[Rules Engine#House Conventions]]).
2. The trigger is one of: ended Move in that arc · finished a Shoot · finished an Interact (open door, etc.) · finished / resolved a Charge · sprung a visible trap / Triggerable feature the reactor can see.

No mid-move interrupts — wait until the Move or Action resolves.

### Reaction options
Resolve immediately, interrupting the enemy's next steps if any remain. A Reaction **attack** does **not** spend the reactor's next activation attack.

| Option | Effect |
|---|---|
| **Snap Shot** | Make a ranged attack at the triggering enemy at **−2**. Must be in range + forward LOS. Any eligible ranged weapon (Sidearm rules still apply if Engaged). Counts as an attack. |
| **Charge** | Move up to **MOV"** into Engagement with the triggerer (not 2×). Free melee with **no** Charge +1. Needs forward LOS when declared. |
| **Throw** | Resolve a normal thrown-weapon / thrown-object attack at the triggerer (**no** extra −2 beyond Snap Shot's — Throw uses the weapon's normal profile). |
| **Interact** | One **interrupt Interact** only: open/close a door, Lift-block / clear a Block, press a simple button, or similar. **No** Search, Hack, Repair, or Stabilize. |
| **Trigger** | Set off one of **your** armed traps or a **Linked** feature you already control, if in forward LOS to the trigger point / feature. |

### Catch-up
Alpha ships with **underdog +1 Priority only**. No extra surge/hold rule until playtest says the dogpile is a problem.

> [!question] Playtest dials
> - Ready re-acquire same round (flexible) vs hard once-per-round cap.
> - Snap Shot −2 harsh enough / too soft.
> - Whether finishing a Charge in someone's arc feels oppressive (they Charge, then eat a Snap Shot / counter-Charge).

## Rule ledger
- [[core-005 Activation order]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
