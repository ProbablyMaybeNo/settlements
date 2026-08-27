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
  - is **hit** by an attack, a hostile hack effect, or a terrain/hazard effect (Injury pass, condition applied, a feature triggered on it, etc.).
- Sprint / Charge consume both slots and leave no Ready; starting a Sprint or Charge cancels Ready.

### Reaction triggers
A Ready unit may react **once** (spend the token) **after** an enemy finishes a Move or Action, if all are true:
1. The enemy (or the relevant terrain trigger) is in the reactor's **forward 180°** and **true LOS** ([[Rules Engine#House Conventions]]).
2. The trigger is one of: ended a **Move greater than half its MOV"** in that arc (a short shuffle of ≤ half MOV doesn't draw fire) · finished a Shoot · finished an Interact (open door, etc.) · finished / resolved a Charge · sprung a visible trap / Triggerable feature the reactor can see.

No mid-move interrupts — wait until the Move or Action resolves.

### Reaction options
Resolve immediately, interrupting the enemy's next steps if any remain. A Reaction **attack** does **not** spend the reactor's next activation attack.

| Option | Effect |
|---|---|
| **Snap Shot** | Make a normal ranged attack at the triggering enemy (**no** extra −2). Must be in range + forward LOS. Any legal ranged weapon (Sidearm rules still apply if Engaged). **This is your "return fire":** when an enemy Shoots, a Ready model may Snap Shot back — but it resolves *after* the enemy's shot, so if that shot Downs it first, it can't reply (that's the shooter's first-mover incentive). |
| **Charge** | Move up to **MOV"** into Engagement with the triggerer (not 2×). Free melee with **no** Charge +1. Needs forward LOS when declared. *Playtest whether full-strength Charge feels better.* |
| **Throw** | Resolve a normal thrown-weapon / thrown-object attack (no extra −2). |
| **Interact / Operate** | Open/close a door, Lift-block / clear a Block, hit a button/lever, **operate an Infrastructure feature you can reach** — by hand in base contact, or by hacking a terminal within range — or **Interrupt** an enemy hack ([[Infrastructure#3 · As a Reaction]] / [[Hacking#Interrupt — contesting a hack]]). Still **no** Search, Repair, or Stabilize as a Reaction. |
| **Trigger** | Only your own traps with the **Remote Detonation** tag (set by the placer, or by a Hacker). Not every trap is remote. |
| **Dodge** | When **targeted by a ranged attack** (from **any angle** — no facing needed, so this is your answer to flank/rear shots), make an opposed roll: **`1d10 + AGI`** vs the shooter's **`1d10 + DEX`** (ties to you). This *replaces* the shot's to-hit; **cover doesn't apply** (you traded cover for evasion). **Win →** the shot misses; move up to **half MOV"** (round down) in any direction, preferably **ending out of the shooter's LOS**; this scramble draws **no** reactions; then you gain **Pinned**. **Lose →** the shot hits — resolve the Injury roll as normal. |

^tbl-reaction-options

#### Orders received
Each unit may **receive only one Order** per round. So max Ready opportunities in a round = own Action Ready + one Order Ready.

**Orders are issued only during the issuing unit's own activation** ([[Rules Engine#Orders]], locked 2026-07-13). A Leader cannot hold Orders in reserve and spend them reactively.

### Catch-up
Alpha ships with **underdog +1 Priority only**. No free-hold surge rule unless playtests feel unfair.

> [!question] Playtest dials
> - Reaction Charge: MOV" + no +1 vs full Charge (2× MOV" + +1)
> - Whether finishing a move in a Ready arc feels oppressive on dense boards
> [!success] Uneven crew sizes — **Ready is the answer** (validated 2026-07-13)
> [[List Building]] lets crews run from 4 to 14 models, so a small crew runs out of activations first and the big crew dumps its tail unopposed. **No new rule is needed.** The elite crew converts its last activations into **Ready** and snap-shoots the tail as it moves — 4 models = 4 banked reactions, so every fighter effectively shoots twice.
> The **underdog +1 Priority** likewise stays exactly as written. It is not an exploit for small crews — it is their **compensation**: [[Crew Sim — Findings|the crew sim]] shows swarms out-produce elites on raw output, because WND is fixed at 1 and the Injury roll ignores stats, so quality has a hard ceiling that numbers don't. Fewer models *should* go first.

### BLKOUT import — status (drafted 2026-07-23)
> [!note] From the BLKOUT read-through (Settlements repo → `docs/BLKOUT-RULES-ANALYSIS.md` §19). Now **drafted into the live rules above** — playtest before graduating further, and propagate any further change through every note that references these reactions before committing.
> - **Return Fire — cut.** Sequential "shoot back at a shooter" already **is** Snap Shot (above): it resolves *after* the enemy's shot, so a shooter can Down its target before it replies — the attacker keeps a first-mover incentive to shoot. Simultaneous resolution was rejected as too swingy / anti-shooter.
> - **Dodge — added** (reaction, above): opposed **AGI vs DEX** active evasion. A deliberate, resourced exception to *"you can't dodge a bullet"* ([[Rules Engine]]) — it costs your Ready, can be lost, and ends you **Pinned**.
> - **Distance-gated Snap Shot — added** (trigger #2): only a Move **> half MOV"** ending in an enemy's LOS draws a reaction; a short shuffle (≤ half MOV) is safe.
> - **Orders** already limited to Specialist 1 / Leader 2 — no change needed.
>
> **Playtest dials:** the escape move was **cut from full MOV to half** in the 2026-08-07 audit ([[Full Rules System v1]] §3) — a full move out of LOS made Dodge strictly better than cover. Is half still too strong? should the shooter's aim traits (Accurate / range) modify their side of the Dodge roll? keep Dodge-ends-Pinned? Reactions still don't cost the reactor's own activation — watch for overwatch stacking when many units are Ready.

## Rule ledger
- [[core-005 Activation order]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
