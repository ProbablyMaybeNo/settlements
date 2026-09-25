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
This is **Phase 1** of the campaign turn — the full three-phase cycle lives in [[Downtime]].

1. **Survival** — resolve each unit's fate (below).
2. **Level-ups** — apply every qualifying trigger from the battle to each survivor, subject to the **6-source soft cap**; anyone crossing a Level resolves it now (see [[Progression]]). *(This replaced the old freeform Advance spend on 2026-08-05.)*
3. **Resources** — bank scenario Resources for the crew, capped by storage (see [[Core Game Format]], [[Economy]]).

### Survival — who is Safe
A unit is **Safe** (no roll) if, at the end of the battle, it:
- is still standing with its crew, **or**
- left the board via a friendly edge (fled / limped off), **or**
- ends in **base contact with a friendly**.

### Post-battle — the Fate table
Any unit that ends the battle **Down and alone**, or that **bled out** during it, rolls on **FATE** (`1d10`):

> [!important] A natural 1 is always Dead; a natural 10 is always Hardened
> Fate modifiers shift every other result but never overwrite the die's own
> extremes, and **total Fate modifiers are capped at +2**
> ([[Full Rules System v1]] §26.3). Without this rule a staffed Med-bay made
> death arithmetically impossible.

**+1 with a Med-bay**, **+2 if that Med-bay has an assigned worker** ([[Structures#Worker benefits]]). *(The old "Tier-1 worker" wording went with the Proficiency track, cut 2026-08-05 — a worker is assigned or not.)*

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

### Glorious Deeds
*The signature-feat Level trigger, named and listed 2026-08-05 ([[Full Rules System v1]] §26.2). This retires the "name WIP" placeholder in [[Core Game Format]].*

A **Glorious Deed** is a high-risk feat that earns a fighter a Level trigger. **Once per fighter per battle** — a fighter banks at most one Deed no matter how many they perform, and the whole battle is still capped at **6 distinct Level sources per fighter** ([[Progression]]).

| Deed | Earned by |
|---|---|
| **Daredevil** | Clear a gap on a Jump/Leap test |
| **Wrecking Crew** | Kill using a terrain verb ([[Infrastructure]]) |
| **Duelist** | Win a head-to-head melee |
| **Last One Standing** | Be the crew's only survivor still standing |
| **Medic** | Revive a **Down** friendly |
| **Steady Hand** | Rally an ally, or Talk Them Down |
| **Ghost** | Finish the battle never having been targeted |
| **Ambush Predator** | Land an Ambush ([[Conditions#Stealth & Ambush]]) |
| **Trapper** | Kill with a trap or deployable ([[Deployables]]) |
| **Against the Odds** | Win a fight while carrying **2+ Stress** |

^tbl-glorious-deeds

Each **territory card** also carries **1–5 Territory Deeds** themed to that location ([[Territory]]).

> [!warning] Two names collide — **still open, needs a ruling**
> **Wrecking Crew** is both this Deed and a **T3 STR skill** ([[Skill Paths]]), and **Trapper** is both this Deed and a **T1 INT skill**. A player asking "did I earn Wrecking Crew?" cannot tell which system is being talked about.
>
> **Rename the Deeds, not the skills** — the skills are referenced from the stat ladder and the costing engine, the Deeds only from this table. Suggested: **Wrecking Crew → Demolition Man** · **Trapper → Sprung the Trap**. Not applied; it is a naming call, not a propagation fix.

### The third Scar — forced retirement
*Options drafted 2026-08-05 ([[Full Rules System v1]] §26.4). **2–3** and **6–8** on the Fate table are Scars; **Captured is not**.*

On taking a **third Scar**, a fighter must retire. Choose one, resolved in the **Settlement Phase** ([[Downtime]]):

- **Reassign** to Worker — the fighter leaves the crew and takes a structure slot ([[Structures#Worker benefits]]).
- **One last mission** — field them for one more battle, then retire regardless of the outcome.
- **Special treatment** — a **T2 Med-bay**, at significant cost, **heals one Scar**. **Once per career, full stop.**
- **Retire outright.**

> [!success] The once-per-career cap on Special Treatment is measured, not taste — T9
> Uncapped, Special Treatment gets bought **3.98 times per 20-battle campaign** — routine rather than exceptional. Capping it at once per career brings that to **1.00**. **Do not ship it uncapped.**

> [!question] Fate is a first-draft spread — tune once campaigns are played. The per-injury effects, Captured and Hardened were drafted 2026-08-05 ([[Full Rules System v1]] §26.3), closing the long-standing gap where the table pointed at scar content that had never been written. Scars hook into [[Progression]] and the *every scar tells a story* tenet.

## Rule ledger
- [[adv-005 Campaign rules]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
