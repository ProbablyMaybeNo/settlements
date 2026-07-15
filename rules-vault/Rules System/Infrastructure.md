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
The operable machines built into the city — cranes, doors, bridges, shutters, floodlights, vents — and how crews **reshape the battlefield** by operating them. The physical acts of forcing/searching/lifting terrain and Feature damage stay in [[Terrain Interaction]]; the hack itself lives in [[Hacking]]. This note is the layer that turns a static board into a machine both crews fight to control.

> [!info] Naming — this is the "Terrain Interactions & Infrastructure" system, kept as its own note (`Infrastructure`) so it doesn't collide with the existing [[Terrain Interaction]] note (doors/lift/search/traps). Rename later if you'd rather merge.

## Design philosophy
The city itself is the battlefield. Buildings contain infrastructure both crews can operate, hack, and exploit.

- **Infrastructure changes the board — it does not exist to damage models.** Damaging the enemy is the job of units and their gear (see [[#Infrastructure vs Deployables]]).
- It opens and closes routes, alters line of sight, moves terrain, changes elevation, and creates or removes cover.
- Any direct harm is a **secondary rider** on a board change, it is **rare**, and it always resolves through a rule we already have — never a bespoke number (see [[#Damage riders — all through the existing engine]]).
- Every feature should read as something with a **believable civilian or industrial origin**, repurposed by the crews — never a pre-built death trap.

## Infrastructure vs Deployables
Two different jobs; keep them separate.

| | Infrastructure | Deployables |
|---|---|---|
| What | Fixed parts of the board (crane, door, bridge, shutters, generator) | Gear a unit carries (turret, mine, tripwire, barricade, med-station) |
| Job | **Reshape the battlefield** | **Deal or deny damage** |
| Rules home | This note | [[Terrain Interaction]] · [[Weapons]] · [[Skill Paths]] |

**Turrets are Deployables, not Infrastructure.** If a scenario or [[Settlement]] upgrade bolts a security turret to a building, it is **controlled-only** and operated through [[Hacking]] — never an auto-sentry. A thing that exists *only* to hurt people belongs in gear, not in the walls.

## The five categories
Every Infrastructure Feature belongs to one category, which names its battlefield role. Each category is built from the shared **board verbs** below, so a feature's category tells you which verbs it uses.

| Category | Role | Verbs it draws on |
|---|---|---|
| **Mobility** | new ways to move (verticality, transit) | Create/Remove Route · Change Elevation |
| **Access** | gate existing chokepoints | Open/Close Path |
| **Visibility** | create or remove sight | Block/Clear LOS |
| **Manipulation** | physically move parts of the board | Shift Terrain · Create/Remove Cover · Displace |
| **Utilities** | change the environment of an area | Field a Zone |

*(Mobility **creates** movement options; Access **gates** ones that already exist — that's the line between them.)*

## The board verbs
Every feature is **[category] + one or two verbs + an optional damage rider.** Eight verbs cover the whole system. Each is a **toggle** unless a feature says otherwise, and each has a "caught in the change" clause that routes to an existing rule.

1. **Open / Close Path** — toggle an opening between passable and **Impassable / Blocked** ([[Terrain]] · [[Terrain Interaction#Lift → Blocked openings]]). *Caught in it:* a model in the closing gap is **Displaced** 1" to the nearer open side (a heavy blast door **Crushes** instead — see riders). *Sealed room:* every exit Blocked means a model can't leave until someone **operates** the door or **Forces** it (STR 7+, [[Terrain Interaction]]).
2. **Create / Remove Route** — add or delete a traversal line: a bridge span, a lift car, a running conveyor. *Caught in it:* removing an **elevated** route with a model on it → **Fall** ([[Terrain#Verticality]]); a ground route just closes.
3. **Block / Clear LOS** — toggle a facade or zone between clear sight and **Blocked LOS**, or set **Concealing** / strip **Hidden** ([[Terrain#Cover]]). No model harm — this reshapes fire lanes, not bodies.
4. **Create / Remove Cover** — set down or lift away a cover piece, or change a piece's Cover value (Open / Light / Heavy, [[Terrain#Cover]]). A model that was relying on removed cover is now **Open**.
5. **Shift Terrain** — slide a **Movable** piece up to **4"** ([[Terrain Interaction]] Movable/Lift framework). *Caught in it:* a model in the path is Displaced clear; a model pinned against a wall or another piece is **Crushed** (rider).
6. **Change Elevation** — raise or lower a platform/lift, carrying the models on it to the new level. A model half-on steps to the nearer level (no Fall under 3").
7. **Field a Zone** — apply a **Dangerous / Difficult / Impassable** overlay to an area using the existing hazard→condition map ([[Terrain#Hazards (the Dangerous overlay)]]): flood → Deep water (Swim) or Difficult; gas → 3" Dense Smoke (Blind + Concealing). **Never invent a new condition here.**
8. **Displace** — force-move a model **2"** directly away from the source, stopping at terrain or another fighter (matches [[Skill Paths|Knockback]] / Sledgehammer). Off a ledge → **Fall**; into a **Dangerous** area → triggers it immediately ([[Terrain]]); **Rooted** resists (STR test). A powerful effect may push **4"**.

## Damage riders — all through the existing engine
Infrastructure *can* hurt someone, as a side effect of a board change. When it does, it uses a rule we already have. **No new conditions are required for any of it.**

| Rider | Resolves as | Source rule |
|---|---|---|
| **Crush** (crane load, compactor, blast door on a body) | Injury roll **as a hazard**: `1d10 + 3` vs 7+, **ignoring Armor**; 0 WND → **Down** (hazard, not Out) | [[Damage]] · dial to **+2** if too hot, as with falls |
| **Knock down** | **Prone** | [[Conditions]] |
| **Push / thrown off a ledge** | **Displace 2"**, then **Fall** if it leaves an edge (<3" nothing · 3"+ Prone · 6"+ Injury +1 per 2") | [[Terrain#Verticality]] |
| **Locked in** | openings **Blocked / Impassable**; escape by operating the door or **Forcing** it (STR 7+) | [[Terrain Interaction]] |
| **Environmental** | the mapped **Condition** — Fire→Fire, Acid→Poison, deep water→Swim, smoke→Blind, electrified→Shocked | [[Terrain#Hazards (the Dangerous overlay)]] |

Because a crush and a hazard leave a model **Down** (not Out), a fighter dropped by infrastructure can still be reached and Stabilized — the board maims, it rarely executes.

## Feature state & toggles
This is what makes crews *fight over the city* rather than just grab objectives.

- **Everything starts Powered Down** — inert, at its default physical state (door closed, bridge retracted, lights off). No effect on play until operated.
- **Operating it** (hack or manual) powers it and **sets or flips its state.** It holds that state until operated again.
- **It toggles.** Either crew may operate a feature to flip it back — open↔close, raise↔lower, on↔off. That back-and-forth is the contest. Track the current state with the token's orientation.
- **One-way exceptions** are flagged per feature: a **Destroyed** terminal ([[Terrain Interaction#Feature damage]]) or a spent single-use effect doesn't toggle.
- **Optional Generator gate:** a scenario may leave a zone's infrastructure Powered Down until its **Generator** is switched on — hacking or destroying the Generator powers a whole district on or off. A macro-toggle (see the catalogue).

## Activating infrastructure
Two ways to operate a feature. Both spend the unit's **Action**.

### 1 · Remote hack — the [[Hacking]] v1 test
`1d10 + INT − range band` vs **7+**.

| Band | Distance | Mod |
|---|---|:---:|
| Close | 0–6" | 0 |
| Short | 6–12" | −1 |
| Medium | 12–18" | −2 |
| Long | 18–24" | −3 |
| Out | 24"+ | illegal |

- **Pass** → operate **one** compatible feature within the range band you hacked at (set or flip its state).
- **Fail** → the terminal **locks out** until the start of your next activation.
- **Interrupt:** an enemy in base contact with another live terminal may Interrupt — declared *before* your roll, it jams a hack that would otherwise land and **Overloads** their terminal. Full rules in [[Hacking]]. **There is no breach roll** — v1 hacking has none.

### 2 · Manual operation
A model in **base contact** with the feature may operate it by hand: **DEX** Interact vs **7+** ([[Terrain Interaction]]). A heavy manual mechanism (a hand-crank blast door, a lever bank) is **STR** instead — flagged on the feature.

- **Pass** → operate the feature (set or flip its state). **Fail** → no effect.
- **Manual operation cannot be Interrupted** — you're physically pulling the lever. That immunity is the payoff for exposing yourself in base contact, and the reason to close the distance instead of hacking from safety.

## Feature catalogue
Each entry: **Name** — *Category · verb(s)*. `Operate` how, then effect and any rider. All riders resolve through [[#Damage riders — all through the existing engine]].

- **Cargo Crane** — *Manipulation · Shift Terrain / Create-Remove Cover / Displace*. The signature piece. Move a Movable piece up to 4" (open a lane, drop a crate as **Heavy cover**, or lift cover away). Drop a load on a model → **Crush**; sweep a model → **Displace 2"** (off a ledge → Fall). Carry a junked car between rooftops to make a shielded crossing.
- **Blast Door** — *Access · Open-Close Path*. Heavy security door. Toggle a doorway Passable↔Impassable; a model caught in the gap when it shuts is **Crushed** (dial to a 1" Displace if too lethal). Locked = **sealed room** (Blocked); Force STR 7+ to break out. *Manual = STR.*
- **Roller / Security Gate** — *Access · Open-Close Path*. Lighter door: toggles a chokepoint, **never crushes** — a caught model is just Displaced 1" to the near side.
- **Retractable Bridge** — *Mobility · Create-Remove Route*. Extend to span a gap (new route); retract to remove it — a model on it when it retracts **Falls** ([[Terrain#Verticality]]).
- **Elevator / Cargo Lift** — *Mobility · Change Elevation*. Raise/lower a platform between levels, carrying models on it. A vertical shortcut either crew can recall to their level.
- **Conveyor Belt** — *Mobility · Create-Remove Route*. While running, a model that ends its Move on the belt is carried **+4"** along it in the End Phase — and can stay **Hidden** behind a load as it rides ([[Terrain#Cover]]). Toggle on/off, or reverse direction.
- **Window Shutters** — *Visibility · Block-Clear LOS*. Toggle a facade between open (LOS through the windows, Light cover) and shut (**Blocked LOS**). Close a fire lane, or open one onto an enemy, without moving a model.
- **Floodlights** — *Visibility · Clear LOS*. Light a zone: models in it **cannot be Hidden** while lit ([[Terrain#Cover]]), stripping ambush cover. Toggle on/off.
- **Flood Gates** — *Utilities · Field a Zone*. Open to flood a low area → **Deep water** (Swim on entry) or **Difficult**; close to drain. Reshapes which routes exist.
- **HVAC / Gas Vent** — *Utilities · Field a Zone / Displace*. Vent a blast: **Displace 2"** every model in the vent's line (off a ledge → Fall), and/or fill an area with **3" Dense Smoke** (Blind + Concealing, per [[Weapons]] Smoke). Blocks a crossing and covers movement at once.
- **Trash Compactor / Crusher** — *Utilities · bounded hazard*. The one overt hazard feature — industrial and believable. Activate to run it: a model inside the compactor zone takes a **Crush** Injury roll. Scenario-flagged, controlled, never passive.
- **Power Generator / Junction** — *Utilities · enabler*. The optional macro-toggle: while off, all infrastructure in its zone is **Powered Down**. Hacking or manually operating the Generator powers the zone on or off; **Destroying** it ([[Terrain Interaction#Feature damage]]) blacks the zone out for the game.

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

- **Symmetry:** assign features **alternately** (or mirror them across the centreline) so neither crew hand-picks all the strong ones near its own deployment.
- **Density tie-in:** infrastructure rides on the terrain the board already needs — the [[Terrain]] density band is **9–12 large features**; put infrastructure on **roughly half** of the eligible buildings, not all of them.

### Placement
Infrastructure belongs to the **building**, not a spot inside it. Put the token on or beside the structure to show it possesses that feature; the building is the source unless a feature states otherwise (a crane's arm, a vent's line — use the model).

## Design rules
Every feature should pass these.

1. **It changes the battlefield.** Direct damage is rare and always a rider on a board change.
2. **One clear purpose.** A player should read the token and know what it does.
3. **It's believable.** If it would naturally exist in that building, it belongs. If it only exists to hurt people, it's a **Deployable**, not infrastructure.
4. **It creates a choice.** Open or close a route, move cover, reveal or hide, block a sight line, change elevation, redirect movement. *Not:* random explosions, hidden death effects, instant damage.

## Design goal
Crews should fight for **control of the city**, not only over objectives. A winning crew reshapes the board in its favour — opening routes and closing them, revealing and concealing, making and removing cover, moving terrain, changing elevation. Every battle should feel like two crews fighting each other *and* fighting for the machine they're standing inside.

> [!question] Playtest dials
> - **Crush lethality** — `+3` ignoring Armor is ~70% to drop a WND-1 model (same as a 6" fall). Drop to **+2** if the crane/compactor feel too executioner-ish.
> - **Blast Door crush vs displace** — a door that crushes on close is dramatic but swingy; the 1" Displace fallback is the safe default. Pick per table.
> - **Conveyor / vent distances** — `+4"` carry and `2"` push are first guesses off the existing forced-move convention; tune once movement-heavy boards are played.
> - **Features per building** — one is the clean default; if boards feel inert, allow two on large structures but keep the total inside the density band.
> - **Generator gate** — powerful (blacks out a district); start with it **off** in standard scenarios and switch on only where a scenario calls for it.

## Rule ledger
_none yet — graduate a `core-00X Infrastructure` stub after first playtest_

---
*See [[Rules System MOC]] and [[_Rules Map.canvas|the map]].*
