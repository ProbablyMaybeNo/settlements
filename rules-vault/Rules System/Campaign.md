---
type: rule-phase
phase: "19"
stage: S4 Settlement & Campaign
status: Drafted
build_order: 18
depends_on: ["Scenarios", "Settlement"]
feeds_into: ["Progression", "Territory", "Downtime", "Events", "Narrative", "Diplomacy", "Solo & Co-op"]
tags: [settlements/phase, settlements/stage/s4]
---
# 19 · Campaign
> **S4 Settlement & Campaign** · status **Drafted** · build order **18**

**Depends on:** [[Scenarios]], [[Settlement]]
**Feeds into:** [[Progression]], [[Territory]], [[Downtime]], [[Events]], [[Narrative]], [[Diplomacy]], [[Solo & Co-op]]
**Raw dependency (from Notion):** Scenarios, Settlement

## Focus
The post-battle loop that ties individual games into an ongoing war.

The Rules column should nail down:
- The campaign sequence: battle → resolve → downtime → next battle.
- What carries over between games (roster, injuries, resources, territory) and how each player tracks it solo.
- Drop-in / drop-out support so a warband always progresses whether playing one-offs, co-op, or a 2-player narrative.
- Post-battle rewards and consequences (loot, injuries, XP, reputation).
- The map/territory frame that battles are fought over (links to the Territory phase).

## Working rules / decisions

### Post-battle sequence
1. **Survival** — resolve each unit's fate (below).
2. **Advances** — survivors spend earned Advances (see [[Progression]]).
3. **Resources** — bank scenario Resources for the crew (see [[Core Game Format]], [[Economy]]).

### Survival — who is Safe
A unit is **Safe** (no roll) if, at the end of the battle, it:
- is still standing with its crew, **or**
- left the board via a friendly edge (fled / limped off), **or**
- ends in **base contact with a friendly**.

### Post-battle — the Fate table
Any unit that ends the battle **Down and alone**, or that **bled out** during it, rolls on **FATE** (`1d10`):

**+1 with a Med-bay** (+2 if it has a Tier-1 worker).

| d10 | Fate | Specific result | Effect |
|:---:|---|---|---|
| 1 | **Dead** | Death | Removed from the roster permanently |
| 2–3 | **Grievous injury** | Severed leg *or* severed arm | Leg: permanent **−2 MOV**. Arm: permanent **−1 STR**, no two-handed weapons |
| 4–5 | **Captured** | Recruits and Fighters only | Full sequence below |
| 6–8 | **Lasting scar** | Gouged eye · Broken leg · Broken arm · Concussion · Deep scar | Eye: permanent **−1 ranged to-hit**. Broken leg/arm: −1 MOV or STR, **next battle only**. Concussion: −1 all rolls, next battle only. Deep scar: cosmetic |
| 9 | **Full recovery** | Shaken loose | No lasting injury; starts the next battle at **1 Stress** |
| 10 | **Hardened** | Hardened | No injury, and **one free Level immediately** at zero Credits, on top of anything else earned that battle |

^tbl-post-battle-the-fate-table

**Specialists and Leaders cannot be Captured** — a 4–5 for either re-rolls onto the Lasting Scar band. Ranked fighters are too dangerous, too well-protected, or too valuable to bag cleanly; only Recruits and Fighters get taken alive.

**2–3 and 6–8 are Scars** for the third-Scar retirement rule ([[Progression]]). **Captured is not a Scar** — it is a separate campaign thread. **Scars never touch Crew Rating** — pure rules penalties, no refund.

### Captured — resolution
1. The fighter is **held by the capturing crew**, unavailable to their owner for the owner's **next battle**.
2. **Rescue window.** Before that battle the owner may declare a **Raid** on the capturing settlement specifically to free them, played before any other non-raid battle they take. **If the captor cannot or will not accept that raid inside the window, the prisoner is released immediately, free.** Win the raid → the fighter returns unharmed. Lose → the sequence continues.
3. **If no rescue happens,** in the captor's Settlement Phase following their own next battle they must choose one, no stalling:
	- **Ransom** — offer the fighter back for **half their Credits cost**. If the owner won't or can't pay, the fighter is lost permanently, as Dead.
	- **Brainwash** *(requires upgraded Holding Cells)* — opposed `1d10+INT`, capturing Leader vs captive. **Win** → mark one success. **Lose** → the fighter breaks free and goes home unharmed; thread over.
4. A marked success carries to the captor's **next** Settlement Phase for a second opposed INT test. **Win again** → the fighter **permanently defects**, joining the captor's roster at their current Level and stats. **Lose** → they escape home unharmed.

So the captor picks between a guaranteed half-price payday and a two-phase gamble for a free permanent recruit that can end with nothing.

> [!question] Fate is a first-draft spread — tune once campaigns are played. The per-injury effects, Captured and Hardened were drafted 2026-08-05 ([[Full Rules System v1]] §26.3), closing the long-standing gap where the table pointed at scar content that had never been written. Scars hook into [[Progression]] and the *every scar tells a story* tenet.

## Rule ledger
- [[adv-005 Campaign rules]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
