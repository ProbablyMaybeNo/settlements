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
The **catalogue** — the 23 things a player can build, what each one costs in **Materials**, floor space and **Power**, what it does in the campaign layer, and what it becomes on the table when someone raids you. [[Settlement]] owns founding, layout and the resource loop; **this note owns the buildings themselves.**

The lot itself is a **barren, battle-scarred site** — a vacant lot between brownstones, a dead mall car park, an overgrown city park, a gutted warehouse. Damaged, overgrown, showing recent conflict. You build onto it.

> [!check] Reconciled against Interview 1 — ruled 2026-07-26
> Every conflict with [[Interviews — Completing the Rules System]] was checked against the source and ruled on:
> - ~~**Currency stays Goods**~~ — **superseded 2026-08-01. The currency is Credits.** "Goods" read as cargo rather than money, which is the job the word had to do. The 07-24 Cash rename was reverted on 07-26 on a scavenging-flavour argument; Credits replaces both. See `POINTS-DECISIONS.md` D24.
> - **Power stays the Generator** — the Reactor rename is reverted.
> - **One gatherer per resource, but you may build more.** Adopted, with the restriction loosened: the starting set gives one gatherer each for Credits / Materials, and **additional output always costs another structure or an upgrade** — never a free multiplier.
> - **Water is cut** *(ruled 2026-08-01)*. Resources are **Credits · Materials · Power**. The Water Reclaimer, Cistern and Water Tower are gone, per-head Water upkeep is gone, and **housing slots are the only population brake**. The catalogue is **23 structures**, not 25.
> - **Five categories kept** — Sustain / Convert / Operate / Recover / Defend, over the earlier seven.
> - ~~**25 structures**~~ **23** *(the "5 to 10" answer was scoped to release count, a different question; the count itself dropped to 23 when Water was cut)*.
> - **No build prerequisites.** Structures are never chained; cost and floor space are the only gates. Upgrade ladders stay, because a tier is one structure maturing rather than a second structure.
> - **All four late ideas adopted:** **Vault** (as an HQ add-on), **Robotics Workshop**, **Server Core**, **Advanced Weapons Lab**. Four entries were cut to make room — Hydroponics, Vehicle Yard, Bunker (the Vault supersedes it) and Recruiting Board (blocked on hiring rules that don't exist yet).

## Design contract — the five rules that keep this honest

1. **Every structure earns its slot.** No flat `+1`. A structure must do at least one of: unlock a campaign action · raise a meaningful capacity · convert one resource into another · expand list-building options · protect something you could otherwise lose · change how a raid is fought.
2. **Every structure is a real object on a real board.** Each entry ships with a [[Terrain#Setup procedure|terrain line]] in the standard format. If it can't be placed and described, it isn't a structure — it's a bonus, and it doesn't belong here.
3. **Space is the scarcest resource.** The canvas holds roughly ten structures. Twenty-three entries against ten slots means **specialisation is forced, not offered.**
4. **Ownership buys availability, never free board power.** Built structures grant **auto-deploy** (skipping the [[Deployables#Deploying — the INT test|INT test]]); the piece itself still costs Credits against your Crew Rating and still sits inside the **9–12** density band. A bigger settlement never means a bigger army.
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

^tbl-the-settlement-canvas

- **No raid window.** Because the settlement fits the board, a raid always uses **all of it**. There is no sub-section to pick, randomise or argue about — the attacker deploys on the far edge and comes at the whole compound.
- **Density normalisation is automatic.** Count your placed structures as the large features of your three squares; fill the attacker's six squares with neutral terrain until the board sits at **9–12 large features** total. The band in [[Terrain]] is sacred and a settlement never overrides it.
- **Bigger boards.** On a 4'×4' the strip widens to **12" × 48"**. Both players use the same canvas size in a given game.

> [!question] Confirm the board size for alpha testing
> **3'×3'** is recommended: the attacker crosses 24" instead of 36", which is the fairer approach against a defender in prepared positions. 4'×4' is playable but favours the defence.

#### Groundworks — the expansion project

**Groundworks** is a settlement **project**, not a catalogue entry — it clears ground rather than occupying it. It costs **Materials** and extends the canvas:

|Tier|Canvas|Squares|Materials|
|---|---|---|:--:|
|Base|12" × 36"|432|—|
|Groundworks I|**18" × 36"**|648 *(+50%)*|**60**|
|Groundworks II *(4'×4' play)*|**18" × 48"**|864|**100**|

^tbl-groundworks-the-expansion-project

A maxed settlement reaches roughly **14–15 structures** — still well short of 25.

### Footprint classes

A structure's footprint follows **the physical thing it is**, not its game function. Three classes:

|Class|Footprint|What it is|
|---|---|---|
|**Building**|**6×6" minimum**|An enclosed structure with an interior you can enter|
|**Plant**|**~3×3"**|Tanks, towers, gensets, masts — bulk with no interior|
|**Station**|**3×1" minimum**|Kiosks, benches, boards — open-air, no walls|

^tbl-footprint-classes

*Yards (Salvage, Vehicle) are scatter clusters and are sized to their sprawl. The Perimeter Wall is a line, bought by the segment.*

Because Buildings are 6×6" minimum on a 12"-deep strip, you can fit **at most two rows of Buildings**. The natural compound is a building line at the back with plant and stations in the yard in front of it.

> [!example] The mix is a strategic axis
> An all-Buildings settlement fits about **six** structures and is a fortress. A plant-and-stations settlement fits **fifteen** and is made almost entirely of things that don't block line of sight — far more capable, far harder to hold.

### On terrain sizes

> [!important] The footprints in this catalogue are grid sizes, not shopping lists
> A structure's size tells you how much room it takes on your **settlement sheet** — how much of your 12×36 it costs you. It is **not** a requirement about the model on your table.
>
> Use whatever terrain you own that comes closest. A fuel-drum cluster measuring 2½" is a **3×3" Generator**. A ruined house 7" on a side is a **6×6" HQ**. Get in the neighbourhood and carry on — **nobody measures your scenery.**

**Tolerance**

1. **Close enough is correct.** Within **2"** in any dimension for Buildings and yards, within **1"** for Plant and Stations. Just use the piece.
2. **Undersized is always legal.** You already paid for the space on the sheet; a smaller model costs you nothing and gains you nothing.
3. **Badly oversized re-reserves.** If a model exceeds the tolerance, **increase its footprint on your sheet to match what's actually on the table.** No policing needed — a 12"-wide mansion standing in for a 6×6 HQ is allowed, it just eats an extra 72 square inches and costs you two other structures.

**Build the detail in.** Where you can, model what the structure actually *does* — a working gate, a ladder to a firing platform, a roof hatch, a wall terminal, a turret hardpoint. The closer your scenery matches its record, the more the table reads itself at a glance, and the better a raid plays.

> [!important] Mark every interactive point
> Any **Tag** a structure carries — Openable, Lockable, Hackable, Searchable, Climbable, Powered — must be **physically visible on the table**, either modelled onto the piece or marked with a token. If a door can be locked, there is a door or a door token. If there's a terminal, there's a terminal. Nothing interactive is invisible.

### Starting structures — four

Every settlement begins with these, free. **One gatherer per resource**, plus the command hub.

|Structure|Role|Why it's mandatory|
|---|---|---|
|**HQ**|command|Campaign actions, mission dispatch, and the base **12** body slots|
|**Generator**|**Power**|Everything with a draw needs it|
|**Processor**|**Materials** gatherer|Scrap → Materials. Nothing gets built without it|
|**Salvage Yard**|**Credits** gatherer|Sorts and values what scavengers haul back — goods, scrap, equipment|

^tbl-starting-structures-five

Starting footprint is **95 of 432 squares — 22%.** A new settlement should read as a found shell with a genset and a heap of sorted scrap.

#### One gatherer each — but never a hard ceiling
The starting set gives you exactly one gatherer per resource. **You may always build more.** What you may never do is raise output without paying floor space:

- **Build another** gatherer of the same type — a second Processor, a second Salvage Yard. Each is a full structure and eats the canvas accordingly.
- **Upgrade** the one you have — a tier costs Materials, and where the tier promotes a Station into a Building it costs space too.

That is the whole anti-inflation shape for production: output scales, but only against the scarcest resource in the game — **room on a 12×36 lot**. A settlement that doubles its Materials is a settlement with fewer guns.

### Founding — choosing your first few

At founding you spend **125 Materials + 75 Credits** on **anything in the catalogue** ([[Full Rules System v1]] §17.3). Your picks are placed on the canvas immediately, before your first game. There is no founding-only subset and no prerequisite — the budget and the lot are the only limits.

**125 Materials is roughly two Tier-1 structures** on top of the four free starters. Structures are bought and repaired in **Materials**; the Credits half of the budget goes on the crew ([[List Building]]).

Your **location** ([[Settlement#Choosing a location]]) grants **one structure or upgrade free, at zero Materials cost** — hospital → Med-bay, police station → Holding Cells, scrapyard → a Salvage Yard upgraded one tier. Location and founding budget draw on the **same catalogue**, so a location is a head start and a flavour, never a building nobody else can reach.

> [!check] Founding budget is set — 2026-08-05
> **125 Materials + 75 Credits**, with per-structure Materials costs printed in the catalogue below and generated from the costing engine. Checked against the reward rate: a normal battle pays **70 Credits + 15 Materials**, so a **Tier I structure still takes ~3 battles** to afford ([[Economy#Income]], T12). *(Halved with the rest of the economy on the 2026-08-20 rescale — leaving the budget at 250 against halved structure costs would have quietly doubled a founding player's buying power.)*

### Power

The **Generator** produces **+5**. Every powered structure has a **draw** scaled to its tier — **T1 −1 · T2 −2 · T3 −3**. The settlement runs on a single sum: **total output ≥ total draw**, tracked on the sheet ([[Economy#Power — output vs draw]]). A structure without Power is **Disabled for the round** and gives no benefit.

The four starters draw **3** — HQ 1, Processor 1, Salvage Yard 1 — against one Generator's **+5**, leaving **two spare**.

> [!check] Resolved — the Generator is **+5**, and D9 was right
> This note carried **+3** and flagged the contradiction with `docs/POINTS-DECISIONS.md` **D9** (+5, draws T1 1 / T2 2 / T3 3). [[Full Rules System v1]] §19 rules **+5** with exactly D9's draw ladder, so **D9 wins and the +3 is retired**.
>
> That also settles the old start-at-capacity question by choosing the other side of it: a new settlement opens with **two Power spare** rather than sitting at exactly capacity. The tension arrives on the *second* build, not the first, which is the better place for it — a founding player shouldn't have to buy a second Generator before they buy anything interesting.

### Storage & caps — what you can hold, and what a raider can take

**Both hoardable resources are capped by what you have built.** Credits and Materials go in sheds — you cannot fit unlimited scrap in one shed. Only **Power** is never banked: it is output-vs-draw ([[Economy]]), a flow rather than a store.

**Your cap on each resource is the sum of what you have built:**

|Source|Holds|Exposure in a raid|
|---|---|---|
|**HQ** — base|a small amount of every resource|must be entered; Lockable|
|**Gatherer buffer**|a little of *its own* resource — the scrap heap beside the Processor, the pallet by the Salvage Yard|**easy pickings** — open ground, Searchable|
|**Storehouse** — repeatable|the bulk of **Credits and Materials** (dry stores only)|**the loot target** — Breachable and Searchable|
|**Vault** — HQ upgrade|small, and **secure**|Sabotage or an INT hack, nothing else|

^tbl-storage-caps-what-you-can-hold-and-what-a-ra

**Overflow is lost.** Income above your cap does not bank; it spoils, walks off, or never gets hauled home. That is the anti-inflation lever ([[Economy]]) and it is why a rich settlement must keep building sheds instead of sitting on a pile.

**Two other caps run on the same principle:**
- **Housing** — **12** body slots from the HQ, **+6 per Bunkhouse**. Housing is the **only** population brake; there is no per-head upkeep ([[List Building]]).
- **Equipment** — **30** slots to start, **+30 per Armory tier**.

> [!info] Why storage is standalone and not all in the HQ
> If everything lived in the HQ, every raid would have exactly **one** objective and every raid would play identically. Spreading storage across the lot makes the attacker choose which target is worth the crossing, and makes the defender choose what to cluster behind the wall and what to leave in the open. That is a real layout decision on a 12×36 lot, and it is the main reason the settlement is worth drawing at all.

> [!success] The Vault trade — safe *or* plentiful, never both
> The **Vault** holds little but is nearly untouchable. **Storehouses** hold a lot and are Breachable. So a settlement sitting on a fortune has to split it: the irreplaceable part goes in the Vault, the working stock sits in sheds where a determined attacker can get it. Losing a raid should cost you something, and this is the dial that decides how much.

**Storage is repeatable across the board.** Build as many **Storehouses** as you have room for. The ceiling on hoarding is floor space, exactly like production.

> [!check] Closed — **any structure can be sabotage-charged in any raid** (2026-08-05)
> Water was the one resource an attacker **destroyed rather than looted** — you cannot carry a tank away, but you can hole it — and cutting it left every raid target a *loot* target. [[Full Rules System v1]] §21 closes that with a mechanic **that already existed** rather than a new resource:
>
> During any raid, an attacker may target **any** of the defender's structures with the **Sabotage** charge the [[Scenarios|Sabotage scenario]] already uses. A fighter in base contact spends an **Action + INT 7+** to **arm** a charge; it detonates after surviving **3 End Phases** armed, unless a defender spends an **Action + DEX 7+** to **defuse** it (**nat 1 = it goes off immediately**).
>
> A detonated structure goes **Disabled** until repaired at its flat Materials cost (below). It does not need to be looted, and it was never a bespoke "Water tank" target. **Any** Generator, Processor, Trader's Kiosk or Storehouse is a legitimate sabotage target under this rule.
>
> Watch the **3-round fuse** — it is now doing double duty as both the Sabotage scenario's tension knob and the general raid structure-sabotage timer, so tuning one tunes the other ([[Scenarios#Open dials]]).

### HQ tiers — the scavenger pipeline

The **HQ** is the only structure with a full upgrade ladder, and dispatch capacity is what the ladder buys:

| Tier | Materials | Dispatch actions / cycle | Housing | Unlocks |
|---|:--:|:--:|:--:|---|
| **HQ I** | *(starter, free)* | **1** | **12** | — |
| **HQ II** | **110** | **2** | **18** | the **Vault** add-on |
| **HQ III** | **195** | **3** | **24** | — |

^tbl-hq-tiers

- **Each HQ tier raises the number of crew you can send out per cycle** — scavenging, scouting, sabotage. This is how a settlement fields more scavengers on the map ([[Downtime#Phase 2 — Settlement]]).
- It also raises the HQ's own base storage and housing, and gates the **Vault** add-on.
- An assigned **worker** adds **+1 dispatch action** on top of the tier's rate (below).

*HQ tier costs are **first-draft and untested** ([[Full Rules System v1]] §21).*

[[Downtime]] owns the mission rules; the **Comms Mast** is a separate axis — it improves mission *quality* (rerolls, longer-range targets, recruitment broadcasts), never the number of bodies you can dispatch. Build the HQ to send more people, the Mast to send them further.

### Three ways to grow — and how to tell them apart

The lot is small on purpose, so the catalogue must not waste slots on things that are really the same building twice. Every expansion resolves to one of three moves:

|Move|Use when|Costs|Example|
|---|---|---|---|
|**Upgrade**|The later thing is the **same job at greater scale**|Materials, and often floor space|Equipment Shed → **Armory** · Workbench → **Workshop**|
|**Build another**|You want **more throughput** of something you already have|A whole new footprint|A second Processor, another Storehouse, another tank|
|**Groundworks**|You are out of lot|Materials + its own footprint|12×36 → 18×36|

^tbl-three-ways-to-grow-and-how-to-tell-them-apar

> [!danger] Nothing is chained — no structure requires another
> **There are no build prerequisites.** Every entry in the catalogue is available from founding onward, and the only gates are **Materials cost** and **room on the lot**. You may build an EW Mast before you build a wall if that is the settlement you want.
>
> This is deliberate. Space already stops you building everything — the catalogue is ~651 square inches against a 432-square lot — and it stops each player building a *different* everything, because everyone cuts something different. A prerequisite tree does the opposite: it makes every settlement climb the same ladder in the same order. Scarcity produces divergence; tech trees produce convergence.
>
> **Upgrades are not chains.** A tier is the same structure maturing — an Equipment Shed becoming an Armory raises your gear cap without costing a second slot on the lot. That is the point of the ladders, and it is the only kind of sequencing the catalogue has.
>
> **Two structures attach rather than gate.** The **Vault** is bolted to the HQ and the **Turret Mount** is a hardpoint on a wall — they must be *placed* in contact with their host because they are physically part of it. That is a placement rule, not a prerequisite, and the HQ is a starting structure anyway.

**A new catalogue entry has to earn itself by doing a different job.** If it does the same job bigger, it is a tier of something you already own — that is the test every entry below passes.

**Entries are named at their first tier**, so the ladder reads naturally as it grows. An Equipment Shed becoming an Armory is the same structure maturing; it does not consume a second slot on the lot.

> [!info] Why this matters — the space is genuinely tight
> Building the entire catalogue would take roughly **651 square inches**. The base lot is **432**, of which about **300** is usable once you leave lanes to move through. So the base lot fits under **half** the catalogue, Groundworks I fits about **70%**, and even a fully expanded 18×48 lot falls short of everything.
>
> That pressure is the point — but it only works if the catalogue is honest. Three separate research buildings would have burned **28% of the lot** on one activity, which is why the **Fabricator** ladder exists instead.

### Upgrade ladders

Every ladder in the catalogue, and what each tier costs in floor space. Where a tier promotes a **Station** into a **Building**, the space cost is the real price of growing up.

|T1|T2|T3|Space|
|---|---|---|---|
|**Equipment Shed** 3×2|**Armory** 6×6|—|6 → 36|
|**Workbench** 3×2|**Workshop** 6×8|—|6 → 48|
|**Trader's Kiosk** 3×2|**Trade House** 6×6|—|6 → 36|
|**Fabricator** 6×6|**Robotics Workshop** 6×8|**Advanced Weapons Lab** 6×10|36 → 48 → 60|
|**HQ** 6×6|HQ II|HQ III|dispatch slots + storage; gates the **Vault**|
|**Med-bay** 6×6|Med-bay II|—|scar healing unlocks at T2|
|**Storehouse** 6×6|Storehouse II|—|capacity, not footprint|

^tbl-upgrade-ladders

A young settlement is a scatter of stalls, tanks and gensets; growing up means those stalls swallow the yard. This is why **Groundworks** gets bought to *upgrade*, not only to expand.

---

## The catalogue — 23 structures

**★** free starting structure. **Everything else is buildable from founding onward** — no structure requires another.
Terrain line format: `Type · Movement · Cover · Tags` ([[Terrain#Setup procedure]])

**Costs are in Materials**, printed 2026-08-05 from [[Full Rules System v1]] §21. **Repair is a flat 30 Materials per structure**, whatever it cost to build. Every number here is **first-draft** — see [[Economy#Open dials]].

### Sustain — keep people alive, keep the grid up

|Structure|Class|Size|Pwr|Materials|What it does|
|---|---|---|---|:--:|---|
|**Generator** ★|Plant|3×3|**+5**|**20**|**Power** output|
|**Bunkhouse**|Building|6×9|−1|**60**|**+6 owned body slots** above HQ's base 12|
|**Storehouse** *(repeatable)*|Building|6×6|−1|**50**|Bulk storage for **Credits and Materials** above the HQ's base cap. **The loot target in a raid**|
|**Equipment Shed** *(→ Armory 6×6)*|Station|3×2|−1 → −2|**25 → 96**|Holds every **unequipped** weapon, armour and piece of kit the crew owns — **30 slots**, **+30 per Armory tier**. The Armory tier raises the cap and adds a lock|

^tbl-sustain-keep-people-alive-keep-the-grid-up

- Generator — `Feature · Impassable · Heavy · Powered, Hackable, Explosive`
- Bunkhouse — `Building · Interior Open · Heavy · Openable, Lockable, Searchable, Climbable`
- Storehouse — `Building · Interior Open · Heavy · Lockable, Searchable, Breachable`
- Equipment Shed — `Scatter · Open · Light · Searchable` · Armory — `Building · Interior Open · Heavy · Lockable, Searchable, Breachable`

### Convert — turn one resource into another, and make gear

|Structure|Class|Size|Pwr|Materials|What it does|
|---|---|---|---|:--:|---|
|**Processor** ★|Plant|3×5|−1|**45**|**Materials** gatherer — scrap → Materials|
|**Salvage Yard** ★|Yard|5×7|−1|**45**|**Credits** gatherer — sorts and values what scavengers haul back; better break-down rates on gear. Expandable|
|**Trader's Kiosk** *(→ Trade House 6×6)*|Station|3×2|−1 → −2|**45 → 128**|Sell owned gear and surplus → **Credits**; the Trade House tier improves rates|
|**Workbench** *(→ Workshop 6×8)*|Station|3×2|−1 → −2|**45 → 128**|Craft and repair. **Workshop tiers unlock the weapon / armour / chem branches** — upgrades, not separate buildings|
|**Fabricator**|Building|6×6 → 6×8 → 6×10|−1 / −2 / −3|**70 → 110 → 195**|**Research**, in three tiers. **T1 Fabricator** unlocks new blueprints · **T2 Robotics Workshop** builds robots and UGVs and services the Drone Bay's airframes · **T3 Advanced Weapons Lab** unlocks the 2051 arsenal — directed-energy, guided small-arms, drone-delivered payloads ([[Weapons]])|

^tbl-convert-turn-one-resource-into-another-and-m

- Processor — `Feature · Impassable · Heavy · Powered, Hackable, Climbable`
- Salvage Yard — `Scatter cluster · Difficult · Light/Heavy by piece · Searchable, Movable, Unstable`
- Trader's Kiosk — `Scatter · Open · Light · Searchable` · Trade House — `Building · Interior Open · Heavy · Lockable, Searchable`
- Workbench — `Scatter · Open · Light · Searchable` · Workshop — `Building · Interior Difficult · Heavy · Lockable, Searchable, Powered`
- Fabricator — `Building · Interior Open · Heavy · Lockable, Powered, Hackable, Searchable`
- Robotics Workshop (T2) — adds `Interior Difficult, Openable`
- Advanced Weapons Lab (T3) — adds `Explosive`

### Operate — what you can do outside the walls

|Structure|Class|Size|Pwr|Materials|What it does|
|---|---|---|---|:--:|---|
|**HQ** ★|Building|6×6|−1|**70**|Campaign actions, base **12** body slots, base storage. **Tiers raise how many crew you can dispatch per cycle** and gate the Vault|
|**Vault** *(attaches to HQ)*|Plant|3×3|−1|**50**|**Secure** storage — small capacity, near-unbreachable. Where the irreplaceable goes|
|**Scout Post**|Plant|3×3|−1|**50**|Pre-**battle** information: see a Twist, choose attacker/defender, reroll deployment|
|**Comms Mast**|Plant|3×3|−1|**50**|**Mission quality**: reroll a mission test, reach longer-range targets, broadcast for recruits. Dispatch *count* comes from HQ tiers|
|**Server Core**|Building|6×6|−2|**128**|Intelligence and networked control — rival roster intel, and friendly terminals on the board count as **Linked** ([[Hacking]])|
|**Drone Bay**|Building|6×8|−2|**144**|Drone [[Deployables]] **and** a recon drone that runs a scout mission **without spending a fighter**|

^tbl-operate-what-you-can-do-outside-the-walls

- HQ — `Building · Interior Open · Heavy · Openable, Lockable, Searchable, Climbable, Powered`
- Vault — `Feature · Impassable · Heavy · Lockable, Hackable`
- Scout Post — `Scatter · Impassable · Light · Climbable`
- Comms Mast — `Feature · Impassable · Open · Climbable, Powered, Hackable`
- Server Core — `Building · Interior Open · Heavy · Lockable, Powered, Hackable, Searchable`
- Drone Bay — `Building · Interior Open · Heavy · Openable, Powered, Hackable, Searchable`

> [!info] The Vault — the one thing a raid cannot just kick open
> The HQ is where your Credits, gear and loot sit during a raid, which makes it the natural target. The **Vault** is the answer, and it is deliberately the hardest object in the game to open. It is **not Breachable** — a Breach charge does nothing to it. The only ways in are the full **Sabotage** sequence (enter → plant → detonate, DEX-defusable) or an **INT hack** at the vault door.
>
> It cannot be separated from the HQ: it is an add-on placed in base contact, and it falls if the HQ does.

> [!info] Why the Drone Bay matters more than it looks
> [[Settlement]] locks **one roster with per-cycle assignment** — sending a fighter on a mission means they cannot fight. That opportunity cost is the whole tension of the downtime layer, and it bites hardest on small crews. The recon drone is the **pressure valve**: it buys back one mission without costing a body, at a price that competes with everything else on the lot.

### Recover — people come back

|Structure|Class|Size|Pwr|Materials|What it does|
|---|---|---|---|:--:|---|
|**Med-bay**|Building|6×6|−1|**65**|**+1** to the post-battle Fate roll ([[Campaign#Post-battle — the Fate table]]); the **T2** tier heals scars at a Credits/Materials cost|
|**Holding Cells**|Building|6×6|−1|**65**|Prisoner capacity ([[Campaign#Captured — resolution]]); the upgraded tier is what allows a **Brainwash** attempt|
|**Mess Hall**|Building|6×8|−1|**75**|**Once per battle, one fighter clears 1 Stress free** ([[Morale]])|

^tbl-recover-people-come-back

- Med-bay — `Building · Interior Open · Heavy · Lockable, Searchable, Powered`
- Holding Cells — `Building · Interior Open · Heavy · Lockable, Breachable, Hackable`
- Mess Hall — `Building · Interior Open · Heavy · Openable, Searchable`

> [!info] Why scar healing is still gated, now that the rebate is gone
> This callout used to argue that the Med-bay must not undo [[List Building#Campaign rosters|the −2 scar rebate]]. **That rebate was cut on 2026-08-01** — a scar is a pure nerf and does not touch Crew Rating — so the free-lunch argument no longer applies.
>
> The gate stays anyway, for a better reason: **removing a permanent penalty is one of the strongest things a settlement can do for a fighter**, and a veteran who can be scrubbed clean between every battle never carries a scar for long enough to matter. That would hollow out the *scars tell the story* tenet ([[Game Vision]]) far more effectively than any points exploit would have. Scar healing stays **T2 only** and costs Credits/Materials. See [[Progression]] · [[Campaign]].

### Defend — this is the raid board

|Structure|Class|Size|Pwr|Materials|What it does|
|---|---|---|---|:--:|---|
|**Perimeter Wall**|Line|1" thick, **6" segments**|−1|**50** / segment|The floor benefit — bought by the segment; shapes the whole raid board|
|**Gatehouse**|Building|6×6|−1|**75**|A controlled chokepoint: the attacker breaches it or routes around it|
|**Watchtower**|Plant|3×3|−1|**55**|The defender starts one model in it; denies the attacker surprise|
|**Turret Mount** *(attaches to a Wall or Gatehouse)*|Plant|2×2|−2|**104**|Hardpoint. The turret **auto-deploys** — but costs Credits against your Crew Rating and keeps full fragility|
|**EW Mast**|Plant|3×3|−2|**104**|Counter-hack and counter-drone: penalises enemy [[Hacking]] in a raid on you; blocks enemy drone deployables|

^tbl-defend-this-is-the-raid-board

- Perimeter Wall — `Scatter · Impassable · Heavy · Climbable, Breachable, Barricadable`
- Gatehouse — `Building · Interior Open · Heavy · Openable, Lockable, Hackable, Climbable`
- Watchtower — `Scatter · Impassable · Light · Climbable`
- Turret Mount — `Feature · Impassable · Light · Powered, Hackable` — hosts one turret [[Deployables|deployable]]
- EW Mast — `Feature · Impassable · Open · Climbable, Powered, Hackable`

> [!danger] The Turret Mount is not free board power
> Owning the mount grants **auto-deploy** only — the turret skips the [[Deployables#Deploying — the INT test|INT test]] and starts online. It still **costs Credits against your Crew Rating** to field, still counts against the **9–12** density band, and keeps full fragility: `WND−1`, repairable once, hijackable. This is the settled answer to a pre-placed settlement deployable being strictly better and free.

## Worker benefits

*Drafted 2026-08-05 from [[Full Rules System v1]] §22. Workers are assigned in the **Settlement Phase** ([[Downtime#Phase 2 — Settlement]]); a retiring third-Scar veteran can be **reassigned** into one of these slots instead of leaving the roster ([[Campaign#The third Scar — forced retirement]]).*

**One worker slot per structure that accepts one. A worker is either assigned or not.** The listed benefit applies while they are assigned and **stops the moment they are reassigned** — full stop. There is no number to track and nothing to level.

> [!important] **Ten of these twenty ship in v1. Ten are parked.**
> [[Full Rules System v1]] §22 rules that only the benefits carrying the campaign loop are live: **Processor · Salvage Yard · Generator · Med-bay · Storehouse · Equipment Shed/Armory · Trader's Kiosk/Trade House · Workbench/Workshop · HQ · Mess Hall**.
>
> The other ten — **Fabricator ladder · Scout Post · Comms Mast · Server Core · Drone Bay · Holding Cells · Gatehouse · Watchtower · Turret Mount · EW Mast** — are **parked for a future supplement**. They are either battle-facing micro-buffs that complicate a raid, or intel and unlock effects serving systems that are themselves thin in v1. Marked ⏸ in the table below.

> [!check] Proficiency is cut — ruled 2026-08-05
> The earlier design had a **0–100 Proficiency** track per worker with three unlocking bands. That was real bookkeeping — a number per worker, per structure, growing over time — for a mechanic that ultimately still just says *"a structure works better with a person in it."*
>
> It is the same category of complexity this project has cut everywhere else — per-head upkeep, the Heat/Attention track, HP-based structure damage — and worker progression didn't earn an exception by arriving later. The flat benefits below are each drawn from what used to be that system's T1 or T2 tier.
>
> **Not thrown away:** the three-tier version is parked in [[Full Rules System v1]] §22 as a candidate for a future settlement-focused supplement, where granular management is something players opt into rather than something everyone carries.

| | Structure | Assigned worker gives |
|:--:|---|---|
| ✅ | **Generator** | **+1 Power** output |
| ✅ | **Storehouse** | **+10%** effective storage cap |
| ✅ | **Equipment Shed / Armory** | **+10 equipment slots** on top of the structure's own |
| ✅ | **Processor** | **+1 Materials** per gather |
| ✅ | **Salvage Yard** | **+1 Credits** per gather |
| ✅ | **Trader's Kiosk / Trade House** | Sell rate **+10%** |
| ✅ | **Workbench / Workshop** | Crafted item Materials cost **−10%** |
| ⏸ | **Fabricator ladder** | Unlock one blueprint **one tier early** |
| ✅ | **HQ** | **+1 dispatch action** per cycle, on top of the tier's base rate |
| ⏸ | **Scout Post** | Reveal a territory's hidden **Side Objective**, not just its Twist |
| ⏸ | **Comms Mast** | The mission-quality reroll applies to **two rolls** instead of one |
| ⏸ | **Server Core** | Rival intel includes one fighter's current **Level and skills**, not just roster size |
| ⏸ | **Drone Bay** | The free recon mission also reveals a territory's **Loot table** entries ([[Territory]]) |
| ✅ | **Med-bay** | **+1 further to the Fate roll** — stacks with the structure's own +1, **total +2** ([[Campaign]]) |
| ⏸ | **Holding Cells** | The opposed INT test for **Brainwashing** gets **+1** ([[Campaign#Captured — resolution]]) |
| ✅ | **Mess Hall** | The free Stress-clear triggers on **two fighters** instead of one |
| ⏸ | **Gatehouse** | The chokepoint counts as **Heavy** cover, not Light, for defenders behind it in a raid |
| ⏸ | **Watchtower** | The starting model in the tower also **starts Readied**, no Action spent |
| ⏸ | **Turret Mount** | The turret gains **+1** to its auto-fire hit roll |
| ⏸ | **EW Mast** | Counter-hack / counter-drone radius extends to **12"** from the structure |

^worker-benefits

**✅ ships in v1 (10) · ⏸ parked for a future supplement (10)** — per [[Full Rules System v1]] §22.

^tbl-worker-benefits

**Three structures take no worker** — **Bunkhouse**, **Vault** and **Perimeter Wall**. They are passive amenities or board shaping, with no operational job for a person to hold.

> [!warning] All twenty numbers are first-draft and untested
> Same flag as everything else content-shaped in the 2026-08-05 pass — though they are now much simpler to check, since there is no Proficiency curve to validate alongside them ([[Downtime#Still open]]).

### Category counts
Sustain **4** · Convert **5** · Operate **6** · Recover **3** · Defend **5** = **23**. Deliberately uneven — forcing five per category is what produced filler in the first pass. *(Was 25; the Water Reclaimer and Cistern were cut with Water on 2026-08-01.)*

## Space budget

|Build|Squares|% of 432|
|---|---|---|
|Starting four|**95**|22%|
|Typical ten-structure settlement|**~290**|~67%|
|Practical ceiling *(lanes to move through)*|**~300**|~70%|

^tbl-space-budget

The sprawl costs are real: the **Salvage Yard** eats **8%** of the lot at its starting size and more once expanded, and every 6×8 Building is another **11%**. Those are decisions, not shopping.

**Twenty-three structures, room for about ten.** You cannot build the good version of everything, and demolishing to rebuild is a real move rather than a footnote.

## Open decisions

**Closed on 2026-08-05** by [[Full Rules System v1]] §17.3 · §19 · §20 · §21 · §22:

- [x] Build cost in **Materials** per structure — printed in the catalogue above *(first-draft)*
- [x] Replace the destroy-only raid target Water used to provide — **any structure is sabotage-chargeable in any raid**
- [x] Generator output — **+5**, D9 wins, the +3 is retired
- [x] HQ housing — **12** slots, D10 wins
- [x] HQ tier costs and the dispatch increment — **HQ I/II/III = free/210/370**, dispatch **1/2/3**, housing **12/18/24**
- [x] Founding budget — **125 Materials + 75 Credits** *(rescaled 2026-08-27)*
- [x] **Groundworks** cost — **120** / **200** Materials
- [x] Repair cost — **flat 30 Materials** per structure
- [x] Med-bay `+X` on the Fate roll — **+1** *(+2 with a worker)*
- [x] Mess Hall effect — **once per battle, one fighter clears 1 Stress free**
- [x] Whether the whole catalogue is available at founding — **yes, all 23, no research gate, no prerequisites**
- [x] Worker benefits per structure — drafted above; **Proficiency tiers cut**
- [x] Persistent armoury / two-gate — **stashed gear counts 0 toward Crew Rating; fielded gear counts full** ([[Full Rules System v1]] §16). *Confirm this closes [[Economy]] E2.*

**Still open:**

- [ ] Confirm the board size — **3'×3'** recommended
- [ ] Storage **numbers** — the actual caps for HQ base, gatherer buffer, Storehouse, Vault
- [ ] How much a successful raider actually takes from each container
- [ ] Upgrade tier costs beyond the ones printed, including the Station → Building space cost
- [ ] Every Materials cost above is **untested** — HQ tiers, Med-bay and Mess Hall are explicitly flagged as guesses
- [ ] Recruiting Board effect — depends on hiring rules that don't exist yet in [[List Building]]
- [ ] Print-and-cut tile art for every entry ([[Components]])

## Rule ledger
_none yet — the catalogue entries become ledger entries once costed._

---
*Catalogue for [[Settlement]]. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]].*
