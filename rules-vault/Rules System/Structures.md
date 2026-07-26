---
type: rule-phase
phase: "36"
stage: S4 Settlement & Campaign
build_order: 16
status: Drafted
depends_on:
  - Settlement
  - Terrain
  - Terrain Interaction
  - Infrastructure
  - Deployables
feeds_into:
  - Economy
  - Components
  - Scenarios
  - Downtime
  - Final Alpha
tags:
  - settlements/phase
  - settlements/stage/s4
---
# 36 · Structures
> **S4 Settlement & Campaign** · status **Drafted** · build order **16**

**Depends on:** [[Settlement]], [[Terrain]], [[Terrain Interaction]], [[Infrastructure]], [[Deployables]]
**Feeds into:** [[Economy]], [[Components]], [[Scenarios]], [[Downtime]], [[Final Alpha]]

## Focus
The **catalogue** — the 25 things a player can build, what each one costs in floor space and **Power**, what it does in the campaign layer, and what it becomes on the table when someone raids you. [[Settlement]] owns founding, layout and the resource loop; **this note owns the buildings themselves.**

The lot itself is a **barren, battle-scarred site** — a vacant lot between brownstones, a dead mall car park, an overgrown city park, a gutted warehouse. Damaged, overgrown, showing recent conflict. You build onto it.

> [!info] This note supersedes Interview 1
> Drafted **2026-07-26** from a working session that revisited the catalogue from scratch. Where it disagrees with the earlier answers in [[Interviews — Completing the Rules System]], **this note wins**:
> - **Currency is Goods**, not Cash · **Power comes from a Generator**, not a Reactor.
> - **Five categories** — Sustain / Convert / Operate / Recover / Defend — not the earlier seven.
> - **25 structures**, not 5–10.
> - **Four starting structures** (HQ · Water Reclaimer · Generator · Processor). Goods needs no gatherer; it flows in from battles, raids and scavenging.
>
> Four earlier ideas are **not** in the 25 and are still live candidates if you want them: the **Vault** (an HQ add-on holding Goods/loot, hard to breach in a raid), **Robotics Workshop**, **Server / AI Core**, **Advanced Weapons Lab**. Adding any means cutting an equal number below.

## Design contract — the five rules that keep this honest

1. **Every structure earns its slot.** No flat `+1`. A structure must do at least one of: unlock a campaign action · raise a meaningful capacity · convert one resource into another · expand list-building options · protect something you could otherwise lose · change how a raid is fought.
2. **Every structure is a real object on a real board.** Each entry ships with a [[Terrain#Setup procedure|terrain line]] in the standard format. If it can't be placed and described, it isn't a structure — it's a bonus, and it doesn't belong here.
3. **Space is the scarcest resource.** The canvas holds roughly ten structures. Twenty-five entries against ten slots means **specialisation is forced, not offered.**
4. **Ownership buys availability, never free board power.** Built structures grant **auto-deploy** (skipping the [[Deployables#Deploying — the INT test|INT test]]); the piece itself still costs crew-points and still sits inside the **9–12** density band. A bigger settlement never means a bigger army.
5. **Binary state only.** A structure is **Functional** or **Disabled**. No structure HP, no collapse tracking. Destruction runs through **Sabotage**; repair is a flat **Materials** cost.

## Working rules / decisions

### The settlement canvas

Your settlement occupies a strip **12" deep × 36" wide**, drawn on a **1" grid** — a 12 × 36 sheet of one-inch squares, 432 squares total.

The strip is sized so that **your whole settlement always fits on a standard board.** [[Terrain#Setup procedure|Terrain]] divides the 3'×3' board into nine 12"×12" density squares; your settlement is exactly the **back three squares**, on your own board edge.

|Term|Value|
|---|---|
|Canvas|**12" × 36"**, 1" grid|
|Board|**3' × 3'** — the standard board|
|Settlement occupies|the defender's **back three density squares**|
|Attacker crosses|~24" of neutral ground|

- **No raid window.** Because the settlement fits the board, a raid always uses **all of it**. There is no sub-section to pick, randomise or argue about — the attacker deploys on the far edge and comes at the whole compound.
- **Density normalisation is automatic.** Count your placed structures as the large features of your three squares; fill the attacker's six squares with neutral terrain until the board sits at **9–12 large features** total. The band in [[Terrain]] is sacred and a settlement never overrides it.
- **Bigger boards.** On a 4'×4' the strip widens to **12" × 48"**. Both players use the same canvas size in a given game.

> [!question] Confirm the board size for alpha testing
> **3'×3'** is recommended: the attacker crosses 24" instead of 36", which is the fairer approach against a defender in prepared positions. 4'×4' is playable but favours the defence.

#### Groundworks — the expansion project

**Groundworks** is a settlement **project**, not a catalogue entry — it clears ground rather than occupying it. It costs **Materials** and extends the canvas:

|Tier|Canvas|Squares|
|---|---|---|
|Base|12" × 36"|432|
|Groundworks I|**18" × 36"**|648 *(+50%)*|
|Groundworks II *(4'×4' play)*|**18" × 48"**|864|

A maxed settlement reaches roughly **14–15 structures** — still well short of 25.

### Footprint classes

A structure's footprint follows **the physical thing it is**, not its game function. Three classes:

|Class|Footprint|What it is|
|---|---|---|
|**Building**|**6×6" minimum**|An enclosed structure with an interior you can enter|
|**Plant**|**~3×3"**|Tanks, towers, gensets, masts — bulk with no interior|
|**Station**|**3×1" minimum**|Kiosks, benches, boards — open-air, no walls|

*Yards (Salvage, Vehicle) are scatter clusters and are sized to their sprawl. The Perimeter Wall is a line, bought by the segment.*

Because Buildings are 6×6" minimum on a 12"-deep strip, you can fit **at most two rows of Buildings**. The natural compound is a building line at the back with plant and stations in the yard in front of it.

> [!example] The mix is a strategic axis
> An all-Buildings settlement fits about **six** structures and is a fortress. A plant-and-stations settlement fits **fifteen** and is made almost entirely of things that don't block line of sight — far more capable, far harder to hold.

### On terrain sizes

> [!important] The footprints in this catalogue are grid sizes, not shopping lists
> A structure's size tells you how much room it takes on your **settlement sheet** — how much of your 12×36 it costs you. It is **not** a requirement about the model on your table.
>
> Use whatever terrain you own that comes closest. A water tank measuring 2½" is a **3×3" Water Reclaimer**. A ruined house 7" on a side is a **6×6" HQ**. Get in the neighbourhood and carry on — **nobody measures your scenery.**

**Tolerance**

1. **Close enough is correct.** Within **2"** in any dimension for Buildings and yards, within **1"** for Plant and Stations. Just use the piece.
2. **Undersized is always legal.** You already paid for the space on the sheet; a smaller model costs you nothing and gains you nothing.
3. **Badly oversized re-reserves.** If a model exceeds the tolerance, **increase its footprint on your sheet to match what's actually on the table.** No policing needed — a 12"-wide mansion standing in for a 6×6 HQ is allowed, it just eats an extra 72 square inches and costs you two other structures.

**Build the detail in.** Where you can, model what the structure actually *does* — a working gate, a ladder to a firing platform, a roof hatch, a wall terminal, a turret hardpoint. The closer your scenery matches its record, the more the table reads itself at a glance, and the better a raid plays.

> [!important] Mark every interactive point
> Any **Tag** a structure carries — Openable, Lockable, Hackable, Searchable, Climbable, Powered — must be **physically visible on the table**, either modelled onto the piece or marked with a token. If a door can be locked, there is a door or a door token. If there's a terminal, there's a terminal. Nothing interactive is invisible.

### Starting structures — four

Every settlement begins with these, free:

|Structure|Why it's mandatory|
|---|---|
|**HQ**|Campaign actions, mission dispatch, and the base **10** body slots|
|**Water Reclaimer**|**Water** income — Water is consumed per head each cycle|
|**Generator**|**Power** output — everything with a draw needs it|
|**Processor**|**Goods → Materials** — nothing else gets built without it|

**Goods needs no starting structure.** It flows in from battles, raids, scavenging and trade routes ([[Economy]]). The four starters are the bare necessities: somewhere to plan, water to drink, power for the grid, and a way to turn scrap into build material.

Starting footprint is **69 of 432 squares — 16%.** A new settlement is meant to look like a found shell with a genset and a water tank plugged into it.

### Founding — choosing your first few

At founding you spend a **Goods** budget on structures marked **⚑ Founding** below. They are placed on the canvas immediately, before your first game.

Your **location** ([[Settlement]]) grants **one ⚑ structure free** — hospital → Med-bay, police station → Holding Cells, scrapyard → Salvage Yard. Location and founding budget draw on the **same pool**, so a location is a head start and a flavour, never a building nobody else can reach.

> [!question] Founding budget not yet set
> The Goods budget and every build cost below are unpriced. Set them with [[Economy]] — they need the Goods/Materials inflow rates first.

### Power

The **Generator** produces **+3**. Every powered structure has a **draw**. The settlement runs on a single sum: **total output ≥ total draw**, tracked on the sheet ([[Economy]]). A structure without Power is **Disabled** and gives no benefit.

The four starters draw exactly **3** — HQ 1, Water Reclaimer 1, Processor 1 — against one Generator's **+3**. **You begin at exactly capacity.** The first powered thing you add forces a second Generator or a decision about what to run cold. That tension is deliberate and starts on day one.

### Station → Building upgrades

Three entries begin as a **Station** and upgrade into a **Building**. The upgrade costs **Materials and floor space**:

|Tier 1 — Station|Tier 2 — Building|Space cost|
|---|---|---|
|**Workbench** 3×2|**Workshop** 6×8|6 → 48 sq in|
|**Trader's Kiosk** 3×2|**Trade House** 6×6|6 → 36 sq in|
|**Recruiting Board** 3×1|**Recruiting Hall** 6×6|3 → 36 sq in|

A young settlement is a scatter of stalls and gensets; growing up means those stalls swallow the yard. This is why **Groundworks** gets bought to *upgrade*, not only to expand.

---

## The catalogue — 25 structures

**★** starting · **⚑** founding-eligible · **T2 / T3** require the named prerequisite
Terrain line format: `Type · Movement · Cover · Tags` ([[Terrain#Setup procedure]])

### Sustain — keep people alive, keep the grid up

|Structure|Class|Size|Pwr|What it does|
|---|---|---|---|---|
|**Water Reclaimer** ★|Plant|3×3|−1|**Water** income per cycle; Water is consumed per head, so this sets what your population costs|
|**Generator** ★|Plant|3×3|**+3**|**Power** output|
|**Bunkhouse** ⚑|Building|6×9|0|**+N owned body slots** above HQ's base 10|
|**Storehouse** ⚑|Building|6×6|0|Raises the storage cap on Goods and Materials; shields a share from raid theft|
|**Hydroponics** T2 *(Water Reclaimer)*|Plant|3×8|−1|Power + Water → **Goods**|

- Water Reclaimer — `Scatter · Impassable · Heavy · Climbable, Breachable`
- Generator — `Feature · Impassable · Heavy · Powered, Hackable, Explosive`
- Bunkhouse — `Building · Interior Open · Heavy · Openable, Lockable, Searchable, Climbable`
- Storehouse — `Building · Interior Open · Heavy · Lockable, Searchable, Breachable`
- Hydroponics — `Scatter · Difficult · Concealing · Searchable, Breachable` — *glass hides you, it does not stop bullets*

### Convert — turn one resource into another

|Structure|Class|Size|Pwr|What it does|
|---|---|---|---|---|
|**Processor** ★|Plant|3×5|−1|**Goods → Materials**|
|**Trader's Kiosk** ⚑ *(→ Trade House 6×6)*|Station|3×2|0|Sell owned gear and surplus → **Goods**; the Trade House tier improves rates|
|**Workbench** ⚑ *(→ Workshop 6×8, −1)*|Station|3×2|0|Craft and repair. **Workshop tiers unlock the weapon / armour / chem branches** — those are upgrades, not separate buildings|
|**Salvage Yard** ⚑|Yard|8×10|0|Post-battle **Materials** recovery; better break-down rates on gear|
|**Fabricator** T2 *(Workshop)*|Building|6×6|−2|**Research** — unlocks new blueprints. The Workshop makes what you know; this learns what you don't|

- Processor — `Feature · Impassable · Heavy · Powered, Hackable, Climbable`
- Trader's Kiosk — `Scatter · Open · Light · Searchable` · Trade House — `Building · Interior Open · Heavy · Lockable, Searchable`
- Workbench — `Scatter · Open · Light · Searchable` · Workshop — `Building · Interior Difficult · Heavy · Lockable, Searchable, Powered`
- Salvage Yard — `Scatter cluster · Difficult · Light/Heavy by piece · Searchable, Movable, Unstable`
- Fabricator — `Building · Interior Open · Heavy · Lockable, Powered, Hackable, Searchable`

### Operate — what you can do outside the walls

|Structure|Class|Size|Pwr|What it does|
|---|---|---|---|---|
|**HQ** ★|Building|6×6|−1|Campaign actions, mission dispatch, base **10** body slots, crew-wide unlocks|
|**Scout Post** ⚑|Plant|3×3|0|Pre-**battle** information: see a Twist, choose attacker/defender, reroll deployment|
|**Comms Mast** T2 *(HQ)*|Plant|3×3|−1|**Mission** reach: +1 dispatch per cycle, reroll a mission test|
|**Vehicle Yard** T2|Yard|6×10|0|Expedition capacity — haul more back, +1 assignment slot per cycle|
|**Drone Bay** T3 *(Fabricator)*|Building|6×8|−2|Drone [[Deployables]] **and** a recon drone that runs a scout mission **without spending a fighter**|

- HQ — `Building · Interior Open · Heavy · Openable, Lockable, Searchable, Climbable, Powered`
- Scout Post — `Scatter · Impassable · Light · Climbable`
- Comms Mast — `Feature · Impassable · Open · Climbable, Powered, Hackable`
- Vehicle Yard — `Scatter cluster · Difficult · Heavy · Movable, Searchable`
- Drone Bay — `Building · Interior Open · Heavy · Openable, Powered, Hackable, Searchable`

> [!info] Why the Drone Bay matters more than it looks
> [[Settlement]] locks **one roster with per-cycle assignment** — sending a fighter on a mission means they can't fight. That opportunity cost is the whole tension of the downtime layer, and it bites hardest on small crews. The recon drone is the **pressure valve**: it buys back one mission without costing a body, at a T3 price.

### Recover — people come back

|Structure|Class|Size|Pwr|What it does|
|---|---|---|---|---|
|**Med-bay** ⚑|Building|6×6|−1|**+X** to the post-battle Fate roll; the T2 tier heals scars at a Goods/Materials cost|
|**Holding Cells** ⚑|Building|6×6|−1|Prisoner capacity **+** reduced escape chance|
|**Mess Hall** ⚑|Building|6×8|−1|Lower starting **Stress**, or one free clear per battle|
|**Recruiting Board** ⚑ *(→ Recruiting Hall 6×6)*|Station|3×1|0|Reroll or widen the available recruit offers; cheaper hires|

- Med-bay — `Building · Interior Open · Heavy · Lockable, Searchable, Powered`
- Holding Cells — `Building · Interior Open · Heavy · Lockable, Breachable, Hackable`
- Mess Hall — `Building · Interior Open · Heavy · Openable, Searchable`
- Recruiting Board — `Scatter · Open · Open · Searchable`

> [!warning] Med-bay must not undo the scar rebate
> [[List Building#Campaign rosters]] pays a **−2** rebate for a lasting scar — the anti-snowball valve that lets veterans crowd out rookies. If the Med-bay heals scars for free that valve becomes a free lunch. Scar healing is the **T2 tier only** and costs Goods/Materials, so the trade stays a trade. See also [[Progression]] · [[Campaign]].

### Defend — this is the raid board

|Structure|Class|Size|Pwr|What it does|
|---|---|---|---|---|
|**Perimeter Wall** ⚑|Line|1" thick, **6" segments**|0|The floor benefit — bought by the segment; shapes the whole raid board|
|**Gatehouse** ⚑|Building|6×6|−1|A controlled chokepoint: the attacker breaches it or routes around it|
|**Watchtower** ⚑|Plant|3×3|0|The defender starts one model in it; denies the attacker surprise|
|**Bunker** T2|Building|6×6|0|Shields stored resources; cuts casualties on a lost defence|
|**Turret Mount** T2 *(Wall or Gatehouse)*|Plant|2×2|−2|Hardpoint. The turret **auto-deploys** — but costs crew-points and keeps full fragility|
|**EW Mast** T3 *(Comms Mast + Fabricator)*|Plant|3×3|−2|Counter-hack and counter-drone: penalises enemy [[Hacking]] in a raid on you; blocks enemy drone deployables|

- Perimeter Wall — `Scatter · Impassable · Heavy · Climbable, Breachable, Barricadable`
- Gatehouse — `Building · Interior Open · Heavy · Openable, Lockable, Hackable, Climbable`
- Watchtower — `Scatter · Impassable · Light · Climbable`
- Bunker — `Building · Interior Open · Heavy · Lockable, Breachable`
- Turret Mount — `Feature · Impassable · Light · Powered, Hackable` — hosts one turret [[Deployables|deployable]]
- EW Mast — `Feature · Impassable · Open · Climbable, Powered, Hackable`

> [!danger] The Turret Mount is not free board power
> Owning the mount grants **auto-deploy** only — the turret skips the [[Deployables#Deploying — the INT test|INT test]] and starts online. It still **costs crew-points** to field, still counts against the **9–12** density band, and keeps full fragility: `WND−1`, repairable once, hijackable. This is the settled answer to *"a pre-placed settlement deployable is strictly better and free."*

---

## Space budget

|Build|Squares|% of 432|
|---|---|---|
|Starting four|**69**|16%|
|Typical ten-structure settlement|**~290**|~67%|
|Practical ceiling *(lanes to move through)*|**~300**|~70%|

The two yards genuinely hurt: the **Salvage Yard** eats **18%** of your entire settlement, the **Vehicle Yard** **16%**. Those are decisions, not shopping.

**Twenty-five structures, room for about ten.** You cannot build the good version of everything, and demolishing to rebuild is a real move rather than a footnote.

## Open decisions

- [ ] Confirm the board size — **3'×3'** recommended
- [ ] Build cost in **Materials** per structure ([[Economy]])
- [ ] Founding **Goods** budget and per-structure founding price
- [ ] Upgrade tier costs, including the Station → Building space cost
- [ ] **Groundworks** cost
- [ ] Repair cost — flat Materials per structure, or a single flat rate
- [ ] Med-bay `+X` value on the Fate roll
- [ ] Mess Hall **Stress** value ([[Morale]])
- [ ] Recruiting Board effect — depends on the hiring rules in [[List Building]]
- [ ] Whether all 25 are available at founding or gated behind research / blueprints
- [ ] Print-and-cut tile art for every entry ([[Components]])

## Rule ledger
_none yet — the catalogue entries become ledger entries once costed._

---
*Catalogue for [[Settlement]]. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]].*
