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

A condition is a **status token on a unit**. Combat conditions come from [[Damage]] and skills ([[Skill Paths]]); Nerve states come from [[Morale]]; persistent conditions come from weapons, terrain hazards and skills.

### General rules
- **Tokens.** Every condition is one token beside the model. If a unit has no token, it has no condition — nothing is tracked in your head.
- **No stacking.** The same condition never applies twice. Reapplying it refreshes its duration; it does not deepen the effect.
- **Stress hook.** Gaining a negative condition gives **+1 Stress** (see [[Morale]]) — the *first* time it's applied, not on a refresh.
- **Modifier cap.** However many conditions a unit carries, the total modifier on any single roll never exceeds **−3** (or +3). Conditions past the cap still matter — they still restrict actions and still have to be cleared.
- **Timing.** "Until the End Phase" clears in step 2 of the End Phase ([[Rules Engine#Turn / Round Structure]]). "Until the end of its next activation" clears when that activation ends, even if the unit did nothing.

### Core combat conditions
- **Pinned** — must spend its **Move** to clear before doing anything else; may still Shoot (Action slot) but cannot Move, Charge or Sprint. Persists until cleared.
- **Down** — prone and out of the fight; no normal actions. Attacks against it auto-hit (Injury roll still made; a pass finishes it). Stabilize by the end of its next activation or it bleeds out — full rules in [[Damage]].
- **Hidden** — **−3 to be hit.** Earned via the **Hide** action in Concealing terrain, or from gear/skill. Lost on moving (except where a skill allows it), shooting, or being revealed.

### Control conditions (from skills, weapons and terrain)
- **Grappled** — grappler and target stay within 1". The target cannot Move, Charge, Sprint or Disengage; it may only attack its grappler, or spend its Action on an **opposed STR test** to escape. The grappler may release it freely, or move at **half MOV** while dragging it. Grappling ends if either model goes Down.
- **Suppressed** — counts as **Pinned**, and the unit **cannot React** until it has cleared the Pinned effect.
- **Off-Balance** — cannot Sprint or Charge. Ends at the end of the unit's next activation.
- **Hobbled** — **−2" MOV**. Ends at the end of the unit's next activation.
- **Provoked** — the unit's first attack against anyone *except* the source suffers **−1**. Ends after that attack, or at the end of its next activation.

### Persistent conditions (resolve in the End Phase)
- **Fire** — each End Phase, the unit suffers an **Injury roll at +1 Damage, ignoring Armor**. It (or an adjacent friendly) may spend an **Action** to extinguish it — automatic, no test. Persists until extinguished.
- **Bleed** — each End Phase, the unit loses **1 WND** unless treated. Treating = an Action + **INT test (7+)** by the unit or an adjacent friendly, **−2 without a Med-Kit**; a **Medic** ([[Skill Paths]]) treats automatically.
- **Poison** — **−1 to all rolls.** Each End Phase the unit makes a **STR test (7+)**: pass ends it. It can also be treated exactly like Bleed.
- **Blind** — **−2 on all rolls that need sight** (attacks, Spot, Reactions, targeted Interacts). Clears in the End Phase.
- **Shocked** — **−2 to all rolls** and **cannot React**. Clears in the End Phase.

### Nerve states (from [[Morale]])
- **Shaken** — any unit with **1+ Stress**: −1 to all rolls. Always-on, doesn't stack, no test. Clears when all Stress clears.
- **Bolt** — flees toward the nearest board edge, hugging cover. *(Break test fail at Stress 2.)*
- **Broken** — frozen; cannot act. *(fail at Stress 3.)*
- **BugOut** — routs off the nearest board edge and is removed from play. *(fail at Stress 4+.)*
- **Fight** — *skill-induced only* (e.g. Fanatic, [[Skill Paths]]): instead of cracking, the unit must move by the shortest route toward the nearest visible enemy on its next activation and attack it if able. It cannot Hide, detour for cover, or move away from that enemy.

### Morale modifiers (from skills)
- **Braced** — **+1 on Break tests**, and reduce the first Stress gained from losing a melee by 1. Ends at the start of the unit's next activation.
- **Cowed** — **−1 on the unit's next Break test**, then ends.
- **Frightened** — **cannot React** and **−1 on Break tests**. Ends at the end of the unit's next activation.

### Marker & device states (not conditions on units)
These sit on terrain, devices or as table markers — they never give Stress and don't count against the modifier cap:
- **Spotted** — the observing unit has identified the target for named skills, until the stated expiry. Spotted does not remove Hidden by itself.
- **Jammed** — remote activation and wireless control of the device fail; local and manual operation still work. Ends at the start of the jammer's next activation.
- **Compromised** — the next opposed hack against the device's controller gains **+2**, then Compromised ends.
- **Linked** — devices explicitly share a terminal or local network. Range alone never makes devices Linked.

> [!info] Locked for playtest
> The persistent-condition values above (Fire +1 ignoring Armor, Bleed's 1-WND clock, Poison's STR recovery, the −2 Blind/Shocked penalties) are the first locked pass — validate them at the table before graduating this note to the ledger.

## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
