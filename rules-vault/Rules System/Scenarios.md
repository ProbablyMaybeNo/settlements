---
type: rule-phase
phase: "18"
stage: S3 Battle Layer
build_order: 17
status: Drafted
depends_on:
  - Damage
  - Morale
  - Terrain
  - Terrain Interaction
  - Hacking
  - Infrastructure
  - Deployables
feeds_into:
  - Campaign
  - Settlement
  - Factions
  - Final Alpha
  - Balance
tags:
  - settlements/phase
  - settlements/stage/s3
---
# 18 · Scenarios
> **S3 Battle Layer** · status **Drafted** · build order **17**

**Depends on:** [[Damage]], [[Morale]], [[Terrain]], [[Terrain Interaction]], [[Hacking]], [[Infrastructure]], [[Deployables]]
**Feeds into:** [[Campaign]], [[Settlement]], [[Factions]], [[Final Alpha]], [[Balance]]

## Focus
The note that turns the combat sandbox into a **game**. A scenario supplies the *reason to move* — the objectives, the deployment, the win condition, the clock. Everything else in the rules is how you fight; this is what you fight **over**.

> [!success] The one rule that defines Settlements scenarios
> **You win by objectives, never by kills.** Removing the enemy is *never* a victory condition. But a crew that is wiped or **BugsOut** ([[Morale]]) can no longer contest or score — so combat is the *tool*, the objective is the *win*. Shoot the enemy because they're standing on your objective, not because killing them is the point.

## Design philosophy
1. **Objective-primary.** A canny crew can *win without winning the firefight* — outmanoeuvre, out-hack, out-run. Every scenario below can be lost by the side that killed more models.
2. **Terrain is mandatory, not scenery.** Every scenario **requires terrain interactions** — a hack, a search, a forced door, an operated bridge, a line built with an INT test. The board is the game ([[Terrain#Setup procedure]]), so a scenario that could be played on a bare table is a failed scenario.
3. **Objectives are interactive terrain.** Claiming, looting, arming and connecting all use the **core test** and the existing verbs ([[Terrain Interaction#Interaction verbs]]) — nothing here invents a new resolution mechanic.
4. **Five shapes, not five maps.** Each scenario below is a *type* — Control, Mobile, Retrieve, Timer, Network. Future scenarios reskin a shape (a **Kidnapping** is Retrieve + Mobile; a settlement **Defence** is an asymmetric Hold); the shape is the rule.

## The scenario template
Every scenario fills in the same seven slots. Build new ones by answering these.

| Slot | What it sets |
|---|---|
| **Shape** | Control · Mobile · Retrieve · Timer · Network — the win *pattern*. |
| **Board & terrain** | 3'×3', **9–12 large features** (the legal-board density from [[Crew Sim — Findings]]). Below this it isn't a Settlements game. |
| **Deployment** | Zones **24" apart** ([[Core Game Format]]). Symmetric or **attacker/defender** asymmetric. |
| **Objectives** | What they are, where they sit, and the **Interact** that claims/uses them. |
| **Scoring & victory** | How points are earned and what wins. Never "eliminate the enemy." |
| **Length** | **6 rounds** standard ([[Rules Engine]]); Timer/Network shapes can end in **sudden death**. |
| **Twist** | One variable rolled at setup (below) so no two games are identical. |

## Shared rules

### Objectives are Interacts
An **objective** is a marker or a piece of interactive terrain. Acting on one needs **base contact**, costs the unit's **Action**, and resolves as the listed test (`1d10 + Stat ≥ 7`, nat 1/10 as always). The scenario names the stat:
- **Claim / activate / connect** → **INT** (a hack or a technical Interact — [[Hacking]] / [[Terrain Interaction]]).
- **Loot / search** → **INT**, and the piece takes a **Searched/Looted token** (it's spent — [[Terrain Interaction#Searching and looting]]).
- **Arm / defuse a charge** → **INT** to arm, **DEX** to defuse (like a [[Deployables]] mine).
- **Open the route** → **Force STR** / **Lockpick DEX** / **hack a door INT** / operate [[Infrastructure]] (bridge, blast door).

A unit that is **Down, Out or Broken** cannot hold, claim or score. **Shaken** units may act normally (at their −1).

### Holding & contesting
For any "hold" objective:
- You **hold** it if you have a **standing** (not Down/Out) unit within **3"** and **no** enemy within 3".
- **Contested** (models from both sides within 3") → **nobody** holds it that round. Break the contest by removing or driving off the enemy — *that* is what combat is for.

### Scoring clock
Points are scored in the **End Phase** (step after conditions resolve, [[Rules Engine#Turn / Round Structure]]), so a mid-round grab that is lost by End Phase scores nothing. **No scoring in Round 1** — the first round is the advance.

### Concession, bottling & the wipe
- **Wiped out.** A crew reduced to **zero standing models** (all Down / Out / BugOut) can no longer contest or score; the opponent **plays on to bank objectives** (a **Retrieve** or **Network** win can still be raced against the clock). If **both** crews are wiped in the same round, the side **ahead on objectives** at that moment wins.
- **Bottling** ([[Morale#Bottling — voluntary concession]]) is a *choice*, and resolves by timing. **Rounds 1–3**, a crew can only quit by a **fighting withdrawal** off its own edge (which becomes a wipe once the board is clear, above) or by an **accepted surrender** (immediate opponent win). **Round 4+**, a declared bottle **ends the game at once as the opponent's win**, regardless of the objective score.

### The Twist (roll 1d6 at setup)
| d6 | Twist |
|:--:|---|
| 1 | **Blackout** — true LOS is capped at **12"** all game (night fight). |
| 2 | **Live Board** — one printed terrain **hazard** starts active ([[Terrain#Hazards (the Dangerous overlay)]]); place it centrally. |
| 3 | **Reinforcements** — at the End Phase of Round 3, each crew returns **one Down** model to its own board edge. |
| 4 | **Scavengers** — a neutral **bonus objective** (worth +1 / a looted cache) sits dead-centre; either side may take it. |
| 5 | **Foul Weather** — the open is **Difficult** ground (double movement cost outside cover); rewards fighting through terrain. |
| 6 | **Clean** — no twist. A straight fight over the objectives. |

---

## The five scenarios

### 1 · Take a Hold  *(Shape: Control)*
**Premise.** Three power terminals sit on the centreline; light them up and stand on them.

- **Objectives.** **3 terminals**, one central and one 12" to each flank, all on the centreline ([[Hacking]]-style Interacts). A terminal is neutral until **claimed** (base contact, **INT 7+** → your marker). A claimed terminal that no one holds stays claimed until an enemy re-claims it.
- **Scoring.** Each **End Phase (Rounds 2–6)**, score **1 VP** per terminal you **hold** (claimed *and* uncontested, per Holding rules). Max **15 VP**.
- **Victory.** Most VP after Round 6.
- **Terrain hook.** You can't score a terminal you haven't hacked — so a fast body isn't enough; you need the **INT** to claim and the bodies to hold.
- **Twist flavour.** *Blackout* turns the flanks into knife-fights; *Live Board* often lands the hazard on the centre terminal.

### 2 · Escort  *(Shape: Mobile · asymmetric)*
**Premise.** The **Attacker** walks a caravan across the board; the **Defender** runs out the clock.

- **Setup.** One **Caravan** model starts in the Attacker's deployment zone. It has **no activation of its own** and cannot be destroyed — only delayed. It **cannot** cross **Impassable/Blocked** terrain.
- **Moving it.** A friendly (Attacker) unit in base contact may spend its **Action** to move the caravan up to **6"** (an **Order** can move it again — [[Initiative & Activation]]). It moves at half rate through Difficult ground.
- **The route.** The board is laid with a **chokepoint** the caravan must pass — a door, bridge or blast door ([[Infrastructure]]). The **Defender** may operate/close it (or raise barriers, drop shutters); the **Attacker** must **hack or Force** it back open. *This is the scenario's beating heart — terrain gates the escort.*
- **Victory.** **Attacker** wins the instant the caravan **exits the far edge**. **Defender** wins if it hasn't by the end of Round 6.
- **Terrain hook.** Built-in: the caravan literally cannot finish without the crews fighting over an operated feature.

### 3 · Raid  *(Shape: Retrieve)*
**Premise.** Both crews cache loot at home and send raiders for the enemy's.

- **Setup.** Each player places **3 loot caches** in their **own half**, each **6"+ apart** and **6"+ from any board edge**, tucked into or behind terrain (a building, a locked room). One of your three is secretly your **Jackpot** (worth **2**).
- **Looting.** An **enemy** unit in base contact spends its **Action** on an **INT 7+** Search → the cache is **Looted** (your token; it's spent). A cache in a **locked/reinforced** container first needs the door **Forced (STR)**, **picked (DEX)** or **hacked (INT)** — [[Terrain Interaction]].
- **Victory.** Most **enemy** loot value taken by end of Round 6 (Jackpot = 2). You score by raiding *theirs*, not by defending *yours* — so both crews must attack.
- **Terrain hook.** Caches live inside terrain; the Interact suite (Force / Lockpick / Hack / Search) is the scenario.

### 4 · Sabotage  *(Shape: Timer · sudden death)*
**Premise.** Each crew nominates a building it must **defend**, and plants a charge on the enemy's.

- **Setup.** Each player nominates one **target building** in their own half. It is the objective the *enemy* is coming for.
- **The charge.** An enemy unit in base contact with your target spends its **Action** + **INT 7+** to **arm** a charge (a scenario [[Deployables|deployable]]). Once armed it **counts down at each End Phase**; after it survives **3 End Phases armed**, it **detonates**.
- **Defusing.** A defender in base contact spends its **Action** + **DEX 7+** to **defuse** (nat 1 = it goes off now). A defused charge is removed; the enemy may re-arm from scratch.
- **Victory.** **Detonating the enemy's building wins immediately** (sudden death). If neither detonates by the end of Round 6, the side whose charge reached the **most countdown** wins; equal = **draw**.
- **Terrain hook.** The target is a real building — often **locked or reinforced** ([[Terrain Interaction#In-battle repair / settlement hook]]); you fight *into* it to arm and *around* it to defend.

### 5 · Power Supply  *(Shape: Network · INT-primary)*
**Premise.** Bring the grid back online — run lines from the central transformer out to the supplies. The showcase for the **INT / terrain** engine.

- **Setup.** A neutral **Transformer** (a hub terminal) sits **dead-centre**. **Four Power Supply** nodes are placed in the terrain around it, each **>8"** from the hub and from each other.
- **Claiming the hub.** A unit in base contact hacks it (**INT 7+**) to bring it online **for your side**.
- **Running a line.** A unit in base contact with a node you already control (the hub, or a connected supply) spends its **Action** + **INT 7+** to **run a line** to an **uncontrolled supply within 8"**, claiming it — building the chain **outward** from the hub.
- **Cutting a line.** An enemy unit in base contact with one of your claimed nodes spends its **Action** to **sever** it (**DEX 7+**, or a successful melee/ranged hit on it as a Feature); the node and everything downstream of it revert to neutral.
- **Victory.** First crew to hold the **hub + 2 connected supplies** at an **End Phase wins** (sudden death). If neither does by Round 6, **most connected supplies** wins.
- **Terrain hook.** Lines route through contested terrain; nodes sit in cover; the whole scenario is a spatial **INT** race with the firefight deciding who gets to keep building.

---

## Does the math close?
Not a dice sim — scenario balance is a **table** question — but the clocks have to physically work in a 6-round game. They do:

- **Take a Hold** — 3 objectives × 5 scoring rounds = **15 VP** ceiling; a crew that claims two terminals turn 2 and holds leads ~6–9 VP, so contests, not blowouts, decide it.
- **Escort** — ~30–36" to cross at 6–12"/round (one or two lead Actions) = **3–6 rounds** unopposed; the chokepoint is what pushes it to the wire, which is the point.
- **Sabotage** — earliest arm ~Round 2–3 (cross + reach) + 3-round fuse = detonation **Round 5–6**: sudden death is reachable but never guaranteed.
- **Power Supply** — hub (1 Action) + 2 lines (2 Actions, must reach ≤8" nodes) = **~3 turns** of uninterrupted work; cutting lines is what stops it, so it's a real race.
- **Raid** — 6 caches, each an Action + a 7+ (≈60–80% for a Specialist); loot is quick, so the game is about *reaching* enemy caches alive.

## Open dials
- [ ] **Hold radius (3") and no-Round-1 scoring** — the two levers on how fast Control games resolve.
- [ ] **Caravan speed (6"/Action)** and whether the Defender may *also* escort a second caravan (symmetric variant).
- [ ] **Sabotage fuse (3 rounds)** — the whole scenario's tension knob.
- [ ] **Power Supply node count (4) and line range (8")** — board-size dependent; validate on the 3'×3'.
- [ ] **Crew-integration sim** — the honest next test: run these scoring/clock rules inside the [[Crew Sim — Findings|full battle loop]] (with [[Deployables]]) to confirm objective-primary doesn't reward a lone-runner degenerate.

## Rule ledger
_Stubs to graduate after first playtests:_
- [[core-008 Victory and end of game]] — the shared scoring clock, contest rule, and concession/wipe.
- [[adv-003 Civilians and non-combatants]] — the Caravan and other neutral objective-models.

---
See [[Rules System MOC]] · the win layer over [[Damage]] / [[Morale]] · objectives use [[Terrain Interaction]] · [[Hacking]] · [[Infrastructure]] · [[Deployables]] · feeds [[Campaign]] & [[Settlement]].
