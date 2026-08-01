---
type: rule-phase
phase: "34"
stage: S3 Battle Layer
status: Drafted
build_order: 15
depends_on:
  - Terrain
  - Terrain Interaction
  - Hacking
  - Movement
  - Conditions
feeds_into:
  - Scenarios
  - Settlement
  - Skill Paths
tags:
  - settlements/phase
  - settlements/stage/s3
---
# 34 · Infrastructure
> **S3 Battle Layer** · status **Drafted** · build order **15**

**Depends on:** [[Terrain]], [[Terrain Interaction]], [[Hacking]], [[Movement]], [[Conditions]]
**Feeds into:** [[Scenarios]], [[Settlement]], [[Skill Paths]]

## Focus
The operable machines built into the city — cranes, doors, bridges, shutters, floodlights, vents — and how crews **reshape the battlefield** by operating them. The physical acts of forcing/searching/lifting terrain stay in [[Terrain Interaction]]; the hack itself lives in [[Hacking]]. This note is the layer that turns a static board into a machine both crews fight to control.

> [!info] Naming — this is the "Terrain Interactions & Infrastructure" system, kept as its own note (`Infrastructure`) so it doesn't collide with the existing [[Terrain Interaction]] note (doors/lift/search/traps). Rename later if you'd rather merge.

## Design philosophy
The city itself is the battlefield. Buildings contain infrastructure both crews can operate, hack, and exploit.

- **Infrastructure changes the board — it does not exist to damage models.** Damaging the enemy is the job of units and their gear (see [[#Infrastructure vs Deployables]]).
- It opens and closes routes, alters line of sight, moves terrain, changes elevation, and creates or removes cover.
- Any direct harm is a **secondary effect** of a board change, it is **rare**, and it resolves through exactly two keywords, both built on rules we already have (see [[#Damage — two keywords]]).
- Every feature should read as something with a **believable civilian or industrial origin**, repurposed by the crews — never a pre-built death trap.

## Infrastructure vs Deployables
Two different jobs; keep them separate.

| | Infrastructure | Deployables |
|---|---|---|
| What | Fixed parts of the board (crane, door, bridge, shutters, generator) | Gear a unit carries (turret, mine, tripwire, barricade, med-station) |
| Job | **Reshape the battlefield** | **Deal or deny damage** |
| Rules home | This note | [[Deployables]] · [[Terrain Interaction]] · [[Weapons]] · [[Skill Paths]] |

^tbl-infrastructure-vs-deployables

Turrets, mines, and traps are **[[Deployables]]**, not Infrastructure — a thing that exists only to hurt people belongs in gear, not in the walls.

## The five categories
Every Infrastructure Feature belongs to one category, which names its battlefield role. Each category is built from the shared **board verbs** below, so a feature's category tells you which verbs it uses.

| Category | Role | Verbs it draws on |
|---|---|---|
| **Mobility** | new ways to move (verticality, transit) | Create/Remove Route · Change Elevation |
| **Access** | gate existing chokepoints | Open/Close Path |
| **Visibility** | create or remove sight | Block/Clear LOS |
| **Manipulation** | physically move parts of the board | Shift Terrain · Create/Remove Cover · Displace |
| **Utilities** | change the environment of an area | Field a Zone |

^tbl-the-five-categories

*(Mobility **creates** movement options; Access **gates** ones that already exist — that's the line between them.)*

## The board verbs
Every feature is **[category] + one or two verbs + an optional damage keyword.** Eight verbs cover the whole system. Each is a **toggle** unless a feature says otherwise, and each has a "caught in the change" clause that routes to an existing rule.

1. **Open / Close Path** — toggle an opening between passable and **Impassable / Blocked** ([[Terrain]] · [[Terrain Interaction#Lift → Blocked openings]]). *Caught in it:* a model in the closing gap is **Displaced** 1" to the nearer open side (a heavy blast door prints **CRUSH** instead). *Sealed room:* every exit Blocked means a model can't leave until someone **operates** the door or **Forces** it (STR 7+, [[Terrain Interaction]]).
2. **Create / Remove Route** — add or delete a traversal line: a bridge span, a lift car, a running conveyor. *Caught in it:* removing an **elevated** route with a model on it → **FALL**; a ground route just closes.
3. **Block / Clear LOS** — toggle a facade or zone between clear sight and **Blocked LOS**, or set **Concealing** / strip **Hidden** ([[Terrain#Cover]]). No model harm — this reshapes fire lanes, not bodies.
4. **Create / Remove Cover** — set down or lift away a cover piece, or change a piece's Cover value (Open / Light / Heavy, [[Terrain#Cover]]). A model that was relying on removed cover is now **Open**.
5. **Shift Terrain** — slide a **Movable** piece up to **4"** ([[Terrain Interaction]] Movable/Lift framework). *Caught in it:* a model in the path is Displaced clear; a model pinned against a wall or another piece prints **CRUSH**.
6. **Change Elevation** — raise or lower a platform/lift, carrying the models on it to the new level. A model half-on steps to the nearer level (no FALL under 3").
7. **Field a Zone** — apply a **Dangerous / Difficult / Impassable** overlay to an area using the existing hazard→condition map ([[Terrain#Hazards (the Dangerous overlay)]]): flood → Deep water (Swim) or Difficult; gas → 3" Dense Smoke (Blind + Concealing). **Never invent a new condition here.**
8. **Displace** — force-move a model **2"** directly away from the source, stopping at terrain or another fighter (matches [[Skill Paths|Knockback]] / Sledgehammer). Off a ledge → **FALL**; into a **Dangerous** area → triggers it immediately ([[Terrain]]); **Rooted** resists (STR test). A powerful effect may push **4"**.

## Damage — two keywords
Infrastructure deals damage in exactly two ways. Both are **keywords a feature prints**, and both resolve on rules we already have. Everything else a feature does is a **board verb** (movement/position) or an **existing condition** — not damage. **No new conditions are required.**

- **FALL** — resolve a fall for the height dropped ([[Terrain#Verticality]]): under 3" nothing · 3"+ **Prone** · 6"+ **Injury roll** (+1 Damage per full 2", ignoring Armor). Caused by retracting a route, opening a floor, or a **Displace** that leaves a ledge.
- **CRUSH** — an **Injury roll as a hazard**: `1d10 + 3` vs 7+, **ignoring Armor**; a wound → **Down** (hazard, not Out). Dial to **+2** if too lethal. Caused by a crane load, a compactor, or a heavy door on a body.

Both leave a model **Down**, never straight **Out** — the board maims, it doesn't execute, so a dropped fighter can still be reached and Stabilized ([[Damage]]).

Everything else needs no keyword: a shove is the **Displace** verb (it only hurts if it becomes a FALL); a knockdown is **Prone**; flood / gas / fire apply their existing **Conditions** ([[Terrain#Hazards (the Dangerous overlay)]]); a sealed room is a **Blocked** opening ([[Terrain Interaction]]).

## Feature state & toggles
This is what makes crews *fight over the city* rather than just grab objectives.

- **Everything starts Powered Down** — inert, at its default physical state (door closed, bridge retracted, lights off). No effect on play until operated.
- **Operating it** (hack or manual) powers it and **sets or flips its state.** It holds that state until operated again.
- **It toggles.** Either crew may operate a feature to flip it back — open↔close, raise↔lower, on↔off. That back-and-forth is the contest. Track the current state with the token's orientation.
- **Triggers can't be destroyed.** A terminal or a feature's controls are permanent fixtures — they can't be shot off the board. You deny an *enemy's* control only by **Overloading** their terminal with an interrupt ([[Hacking#Interrupt — contesting a hack]]) — and **manual operation in base contact always remains** available to anyone who reaches it.
- **One-way exceptions** are flagged per feature: a spent single-use effect doesn't toggle.
- **Optional Generator gate:** a scenario may leave a zone's infrastructure Powered Down until its **Generator** is switched on — operating the Generator (hack or manual) powers a whole district on or off. A macro-toggle (see the catalogue).

## Activating infrastructure
Three ways to operate a feature. On your turn each spends the unit's **Action**; the third is a Reaction.

### 1 · Remote hack — the [[Hacking]] v1 test
`1d10 + INT − range band` vs **7+**, using the range bands from [[Hacking#Range bands]] (Close 0 · Short −1 · Medium −2 · Long −3, max 24").

- **Pass** → operate **one** compatible feature within that band (set or flip its state).
- **Fail** → nothing happens; the terminal stays **live**, so a different unit may try it ([[Hacking]]).
- **Interrupt:** an enemy in base contact with another live terminal may Interrupt — declared *before* your roll, it jams a hack that would otherwise land and **Overloads** their terminal. Full rules in [[Hacking#Interrupt — contesting a hack]]. **There is no breach roll** — v1 hacking has none.

### 2 · Manual operation
A model in **base contact** with the feature may operate it by hand: **DEX** Interact vs **7+** ([[Terrain Interaction]]). A heavy manual mechanism (a hand-crank blast door, a lever bank) is **STR** instead — flagged on the feature.

- **Pass** → operate the feature (set or flip its state). **Fail** → no effect.
- **Manual operation cannot be Interrupted** — you're physically pulling the lever. That immunity is the payoff for exposing yourself in base contact, and the reason to close the distance instead of hacking from safety.

### 3 · As a Reaction
A **Readied** unit ([[Initiative & Activation#Reaction options]]) may operate **one** feature as its Reaction when an enemy's move or action triggers the moment — retract the bridge as they finish crossing, slam the door on a runner, drop the crane. It must be able to **reach** it: **base contact** to work it by hand (DEX), or **within range of its terminal** to hack it (INT). Same test as on your turn. *(The [[Hacking]] Interrupt is the special case of this — the feature you operate is the enemy's own terminal.)*

## Feature catalogue
Each entry: **Name** — *Category · verb(s)*. How to operate, then effect and any damage keyword. Damage uses the two keywords in [[#Damage — two keywords]].

- **Cargo Crane** — *Manipulation · Shift Terrain / Create-Remove Cover / Displace*. The signature piece. Move a Movable piece up to 4" (open a lane, drop a crate as **Heavy cover**, or lift cover away). Drop a load on a model → **CRUSH**; sweep a model → **Displace 2"** (off a ledge → **FALL**). Carry a junked car between rooftops to make a shielded crossing.
- **Blast Door** — *Access · Open-Close Path*. Heavy security door. Toggle a doorway Passable↔Impassable; a model caught in the gap when it shuts prints **CRUSH** (dial to a 1" Displace if too lethal). Locked = **sealed room** (Blocked); Force STR 7+ to break out. *Manual = STR.*
- **Roller / Security Gate** — *Access · Open-Close Path*. Lighter door: toggles a chokepoint, **no CRUSH** — a caught model is just Displaced 1" to the near side.
- **Retractable Bridge** — *Mobility · Create-Remove Route*. Extend to span a gap (new route); retract to remove it — a model on it when it retracts → **FALL**.
- **Elevator / Cargo Lift** — *Mobility · Change Elevation*. Raise/lower a platform between levels, carrying models on it. A vertical shortcut either crew can recall to their level.
- **Conveyor Belt** — *Mobility · Create-Remove Route*. While running, a model that ends its Move on the belt is carried **+4"** along it in the End Phase — and can stay **Hidden** behind a load as it rides ([[Terrain#Cover]]). Toggle on/off, or reverse direction.
- **Window Shutters** — *Visibility · Block-Clear LOS*. Toggle a facade between open (LOS through the windows, Light cover) and shut (**Blocked LOS**). Close a fire lane, or open one onto an enemy, without moving a model.
- **Floodlights** — *Visibility · Clear LOS*. Light a zone: models in it **cannot be Hidden** while lit ([[Terrain#Cover]]), stripping ambush cover. Toggle on/off.
- **Flood Gates** — *Utilities · Field a Zone*. Open to flood a low area → **Deep water** (Swim on entry) or **Difficult**; close to drain. Reshapes which routes exist.
- **HVAC / Gas Vent** — *Utilities · Field a Zone / Displace*. Vent a blast: **Displace 2"** every model in the vent's line (off a ledge → **FALL**), and/or fill an area with **3" Dense Smoke** (Blind + Concealing, per [[Weapons]] Smoke). Blocks a crossing and covers movement at once.
- **Trash Compactor / Crusher** — *Utilities · bounded hazard*. The one overt hazard feature — industrial and believable. Activate to run it: a model inside the compactor zone takes **CRUSH**. Scenario-flagged, controlled, never passive.
- **Power Generator / Junction** — *Utilities · enabler*. The optional macro-toggle: while off, all infrastructure in its zone is **Powered Down**. Operating the Generator (hack or manual) powers the zone on or off. It can't be destroyed — deny it by **Overloading** its terminal (an interrupt).

## Setup & placement

### Standard battles
Infrastructure is fixed by the **scenario** ([[Scenarios]]): which buildings hold a feature, and which feature each holds. Fast, balanced, cinematic — no random combos.

### Custom battles
Assign features before deployment, guideline **one Infrastructure Feature per building**, chosen to fit the terrain (pick one from the menu):

| Building | Menu (choose one) |
|---|---|
| Warehouse | Cargo Crane · Roller Door |
| Factory | Conveyor · Generator |
| Office | Window Shutters · Floodlights |
| Apartment | Elevator · Blast Door |
| Hospital | Generator · Flood/Fire Suppression |

^tbl-custom-battles

- **Symmetry:** assign features **alternately** (or mirror them across the centreline) so neither crew hand-picks all the strong ones near its own deployment.
- **Density tie-in:** infrastructure rides on the terrain the board already needs — the [[Terrain]] density band is **9–12 large features**; put infrastructure on **roughly half** of the eligible buildings, not all of them.

### Settlement battles
The **defender's own layout** supplies the back three density squares ([[Terrain#Settlement boards — the same procedure, one square-set pre-filled]]), which replaces the symmetric assignment above on that half of the board. This is deliberately asymmetric — you are fighting in someone's home.

- **The defender's structures carry their own features.** A built [[Structures|structure]] arrives with the tags printed in its catalogue entry — a Gatehouse is Openable/Lockable/Hackable because it is a gate, not because a scenario assigned it. No alternate-assignment pass over the settlement squares.
- **The attacker's six squares assign as normal**, alternately or mirrored, on roughly half the eligible buildings.
- **The one-per-building guideline still holds** — a structure's catalogue tags *are* its feature; don't stack a scenario feature on top.
- The attacker's compensation is the ~24" of open approach, not a matching set of toys.

### Placement
Infrastructure belongs to the **building**, not a spot inside it. Put the token on or beside the structure to show it possesses that feature; the building is the source unless a feature states otherwise (a crane's arm, a vent's line — use the model).

## Design rules
Every feature should pass these.

1. **It changes the battlefield.** Direct damage is rare and always a side effect of a board change (only ever **FALL** or **CRUSH**).
2. **One clear purpose.** A player should read the token and know what it does.
3. **It's believable.** If it would naturally exist in that building, it belongs. If it only exists to hurt people, it's a **Deployable**, not infrastructure.
4. **It creates a choice.** Open or close a route, move cover, reveal or hide, block a sight line, change elevation, redirect movement. *Not:* random explosions, hidden death effects, instant damage.

## Design goal
Crews should fight for **control of the city**, not only over objectives. A winning crew reshapes the board in its favour — opening routes and closing them, revealing and concealing, making and removing cover, moving terrain, changing elevation. Every battle should feel like two crews fighting each other *and* fighting for the machine they're standing inside.

> [!question] Playtest dials
> - **Crush lethality** — `+3` ignoring Armor is ~70% to drop a WND-1 model (same as a 6" fall). Drop to **+2** if the crane/compactor feel too executioner-ish.
> - **Blast Door crush vs displace** — a door that CRUSHes on close is dramatic but swingy; the 1" Displace fallback is the safe default. Pick per table.
> - **Conveyor / vent distances** — `+4"` carry and `2"` push are first guesses off the existing forced-move convention; tune once movement-heavy boards are played.
> - **Features per building** — one is the clean default; if boards feel inert, allow two on large structures but keep the total inside the density band.
> - **Generator gate** — powerful (blacks out a district); start with it **off** in standard scenarios and switch on only where a scenario calls for it.

## Rule ledger
_none yet — graduate a `core-00X Infrastructure` stub after first playtest_

---
*See [[Rules System MOC]] and [[_Rules Map.canvas|the map]].*
