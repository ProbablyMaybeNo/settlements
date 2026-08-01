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

> [!check] Reconciled against Interview 1 — ruled 2026-07-26
> Every conflict with [[Interviews — Completing the Rules System]] was checked against the source and ruled on:
> - ~~**Currency stays Goods**~~ — **superseded 2026-08-01. The currency is Credits.** "Goods" read as cargo rather than money, which is the job the word had to do. The 07-24 Cash rename was reverted on 07-26 on a scavenging-flavour argument; Credits replaces both. See `POINTS-DECISIONS.md` D24.
> - **Power stays the Generator** — the Reactor rename is reverted.
> - **One gatherer per resource, but you may build more.** Adopted, with the restriction loosened: the starting set gives one gatherer each for Credits / Materials, and **additional output always costs another structure or an upgrade** — never a free multiplier.
> - **Water is cut** *(ruled 2026-08-01)*. Resources are **Credits · Materials · Power**. The Water Reclaimer, Cistern and Water Tower are gone, per-head Water upkeep is gone, and **housing slots are the only population brake**. The catalogue is **23 structures**, not 25.
> - **Five categories kept** — Sustain / Convert / Operate / Recover / Defend, over the earlier seven.
> - **25 structures** — the "5 to 10" answer was scoped to *release* count, a different question.
> - **No build prerequisites.** Structures are never chained; cost and floor space are the only gates. Upgrade ladders stay, because a tier is one structure maturing rather than a second structure.
> - **All four late ideas adopted:** **Vault** (as an HQ add-on), **Robotics Workshop**, **Server Core**, **Advanced Weapons Lab**. Four entries were cut to make room — Hydroponics, Vehicle Yard, Bunker (the Vault supersedes it) and Recruiting Board (blocked on hiring rules that don't exist yet).

## Design contract — the five rules that keep this honest

1. **Every structure earns its slot.** No flat `+1`. A structure must do at least one of: unlock a campaign action · raise a meaningful capacity · convert one resource into another · expand list-building options · protect something you could otherwise lose · change how a raid is fought.
2. **Every structure is a real object on a real board.** Each entry ships with a [[Terrain#Setup procedure|terrain line]] in the standard format. If it can't be placed and described, it isn't a structure — it's a bonus, and it doesn't belong here.
3. **Space is the scarcest resource.** The canvas holds roughly ten structures. Twenty-five entries against ten slots means **specialisation is forced, not offered.**
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

|Tier|Canvas|Squares|
|---|---|---|
|Base|12" × 36"|432|
|Groundworks I|**18" × 36"**|648 *(+50%)*|
|Groundworks II *(4'×4' play)*|**18" × 48"**|864|

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
|**HQ**|command|Campaign actions, mission dispatch, and the base **10** body slots|
|**Generator**|**Power**|Everything with a draw needs it|
|**Processor**|**Materials** gatherer|Scrap → Materials. Nothing gets built without it|
|**Salvage Yard**|**Credits** gatherer|Sorts and values what scavengers haul back — goods, scrap, equipment|

^tbl-starting-structures-five

Starting footprint is **104 of 432 squares — 24%.** A new settlement should read as a found shell with a genset, a water tank and a heap of sorted scrap.

#### One gatherer each — but never a hard ceiling
The starting set gives you exactly one gatherer per resource. **You may always build more.** What you may never do is raise output without paying floor space:

- **Build another** gatherer of the same type — a second Processor, a second Salvage Yard. Each is a full structure and eats the canvas accordingly.
- **Upgrade** the one you have — a tier costs Materials, and where the tier promotes a Station into a Building it costs space too.

That is the whole anti-inflation shape for production: output scales, but only against the scarcest resource in the game — **room on a 12×36 lot**. A settlement that doubles its Materials is a settlement with fewer guns.

### Founding — choosing your first few

At founding you spend a **Credits** budget on **anything in the catalogue**. Your picks are placed on the canvas immediately, before your first game. There is no founding-only subset and no prerequisite — the budget and the lot are the only limits.

Your **location** ([[Settlement]]) grants **one structure free** — hospital → Med-bay, police station → Holding Cells, scrapyard → a free Salvage Yard upgrade. Location and founding budget draw on the **same catalogue**, so a location is a head start and a flavour, never a building nobody else can reach.

> [!question] Founding budget not yet set
> The Credits budget and every build cost below are unpriced. Set them with [[Economy]] — they need the Credits/Materials inflow rates first.

### Power

The **Generator** produces **+3**. Every powered structure has a **draw**. The settlement runs on a single sum: **total output ≥ total draw**, tracked on the sheet ([[Economy]]). A structure without Power is **Disabled** and gives no benefit.

The four starters draw **2** — HQ 1, Processor 1, Salvage Yard 0 — against one Generator's **+3**.

> [!question] The start-at-capacity tension needs a new dial
> Cutting the Water Reclaimer took a **−1** draw off the opening board, so a new settlement now begins with **1 Power spare** instead of at exactly capacity. That tension was deliberate and is worth keeping. Two ways back: drop the Generator to **+2**, or give the Salvage Yard a **−1** draw. Decide in [[Economy]].
>
> Note also that `docs/POINTS-DECISIONS.md` **D9** sets the Generator at **+5** with draws of T1 1 / T2 2 / T3 3, which this note's **+3** contradicts. One of the two is wrong; resolve it with the same decision.

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

> [!info] Why storage is standalone and not all in the HQ
> If everything lived in the HQ, every raid would have exactly **one** objective and every raid would play identically. Spreading storage across the lot makes the attacker choose which target is worth the crossing, and makes the defender choose what to cluster behind the wall and what to leave in the open. That is a real layout decision on a 12×36 lot, and it is the main reason the settlement is worth drawing at all.

> [!success] The Vault trade — safe *or* plentiful, never both
> The **Vault** holds little but is nearly untouchable. **Storehouses** hold a lot and are Breachable. So a settlement sitting on a fortune has to split it: the irreplaceable part goes in the Vault, the working stock sits in sheds where a determined attacker can get it. Losing a raid should cost you something, and this is the dial that decides how much.

**Storage is repeatable across the board.** Build as many **Storehouses** as you have room for. The ceiling on hoarding is floor space, exactly like production.

> [!question] Cutting Water cost the raid its destroy-only target
> Water was the one resource an attacker **destroyed rather than looted** — you cannot carry a tank away, but you can hole it. That gave raids a second kind of objective and made tank placement a real defensive decision. With Water gone every raid target is now a *loot* target. If raids play flat, this is the hole to fill — most likely by making the **Generator** or the **Processor** sabotage-worthy in the same way. Decide in [[Economy]] / the raid pass.

### HQ tiers — the scavenger pipeline

The **HQ** is the only structure with a full upgrade ladder, and dispatch capacity is what the ladder buys:

- **Each HQ tier raises the number of crew you can send out per cycle** — scavenging, scouting, sabotage. This is how a settlement fields more scavengers on the map.
- It also raises the HQ's own base storage, and gates the **Vault** add-on.

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

### Sustain — keep people alive, keep the grid up

|Structure|Class|Size|Pwr|What it does|
|---|---|---|---|---|
|**Generator** ★|Plant|3×3|**+3**|**Power** output|
|**Bunkhouse**|Building|6×9|0|**+N owned body slots** above HQ's base 10|
|**Storehouse** *(repeatable)*|Building|6×6|0|Bulk storage for **Credits and Materials** above the HQ's base cap. **The loot target in a raid**|
|**Equipment Shed** *(→ Armory 6×6)*|Station|3×2|0|Holds every **unequipped** weapon, armour and piece of kit the crew owns. Caps the size of your persistent armoury; the Armory tier raises it and adds a lock|

^tbl-sustain-keep-people-alive-keep-the-grid-up

- Generator — `Feature · Impassable · Heavy · Powered, Hackable, Explosive`
- Bunkhouse — `Building · Interior Open · Heavy · Openable, Lockable, Searchable, Climbable`
- Storehouse — `Building · Interior Open · Heavy · Lockable, Searchable, Breachable`
- Equipment Shed — `Scatter · Open · Light · Searchable` · Armory — `Building · Interior Open · Heavy · Lockable, Searchable, Breachable`

### Convert — turn one resource into another, and make gear

|Structure|Class|Size|Pwr|What it does|
|---|---|---|---|---|
|**Processor** ★|Plant|3×5|−1|**Materials** gatherer — scrap → Materials|
|**Salvage Yard** ★|Yard|5×7|0|**Credits** gatherer — sorts and values what scavengers haul back; better break-down rates on gear. Expandable|
|**Trader's Kiosk** *(→ Trade House 6×6)*|Station|3×2|0|Sell owned gear and surplus → **Credits**; the Trade House tier improves rates|
|**Workbench** *(→ Workshop 6×8, −1)*|Station|3×2|0|Craft and repair. **Workshop tiers unlock the weapon / armour / chem branches** — upgrades, not separate buildings|
|**Fabricator**|Building|6×6 → 6×10|−2 / −3|**Research**, in three tiers. **T1 Fabricator** unlocks new blueprints · **T2 Robotics Workshop** builds robots and UGVs and services the Drone Bay's airframes · **T3 Advanced Weapons Lab** unlocks the 2051 arsenal — directed-energy, guided small-arms, drone-delivered payloads ([[Weapons]])|

^tbl-convert-turn-one-resource-into-another-and-m

- Processor — `Feature · Impassable · Heavy · Powered, Hackable, Climbable`
- Salvage Yard — `Scatter cluster · Difficult · Light/Heavy by piece · Searchable, Movable, Unstable`
- Trader's Kiosk — `Scatter · Open · Light · Searchable` · Trade House — `Building · Interior Open · Heavy · Lockable, Searchable`
- Workbench — `Scatter · Open · Light · Searchable` · Workshop — `Building · Interior Difficult · Heavy · Lockable, Searchable, Powered`
- Fabricator — `Building · Interior Open · Heavy · Lockable, Powered, Hackable, Searchable`
- Robotics Workshop (T2) — adds `Interior Difficult, Openable`
- Advanced Weapons Lab (T3) — adds `Explosive`

### Operate — what you can do outside the walls

|Structure|Class|Size|Pwr|What it does|
|---|---|---|---|---|
|**HQ** ★|Building|6×6|−1|Campaign actions, base **10** body slots, base storage. **Tiers raise how many crew you can dispatch per cycle** and gate the Vault|
|**Vault** *(attaches to HQ)*|Plant|3×3|−1|**Secure** storage — small capacity, near-unbreachable. Where the irreplaceable goes|
|**Scout Post**|Plant|3×3|0|Pre-**battle** information: see a Twist, choose attacker/defender, reroll deployment|
|**Comms Mast**|Plant|3×3|−1|**Mission quality**: reroll a mission test, reach longer-range targets, broadcast for recruits. Dispatch *count* comes from HQ tiers|
|**Server Core**|Building|6×6|−2|Intelligence and networked control — rival roster intel, and friendly terminals on the board count as **Linked** ([[Hacking]])|
|**Drone Bay**|Building|6×8|−2|Drone [[Deployables]] **and** a recon drone that runs a scout mission **without spending a fighter**|

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

|Structure|Class|Size|Pwr|What it does|
|---|---|---|---|---|
|**Med-bay**|Building|6×6|−1|**+X** to the post-battle Fate roll; the T2 tier heals scars at a Credits/Materials cost|
|**Holding Cells**|Building|6×6|−1|Prisoner capacity **+** reduced escape chance|
|**Mess Hall**|Building|6×8|−1|Lower starting **Stress**, or one free clear per battle ([[Morale]])|

^tbl-recover-people-come-back

- Med-bay — `Building · Interior Open · Heavy · Lockable, Searchable, Powered`
- Holding Cells — `Building · Interior Open · Heavy · Lockable, Breachable, Hackable`
- Mess Hall — `Building · Interior Open · Heavy · Openable, Searchable`

> [!info] Why scar healing is still gated, now that the rebate is gone
> This callout used to argue that the Med-bay must not undo [[List Building#Campaign rosters|the −2 scar rebate]]. **That rebate was cut on 2026-08-01** — a scar is a pure nerf and does not touch Crew Rating — so the free-lunch argument no longer applies.
>
> The gate stays anyway, for a better reason: **removing a permanent penalty is one of the strongest things a settlement can do for a fighter**, and a veteran who can be scrubbed clean between every battle never carries a scar for long enough to matter. That would hollow out the *scars tell the story* tenet ([[Game Vision]]) far more effectively than any points exploit would have. Scar healing stays **T2 only** and costs Credits/Materials. See [[Progression]] · [[Campaign]].

### Defend — this is the raid board

|Structure|Class|Size|Pwr|What it does|
|---|---|---|---|---|
|**Perimeter Wall**|Line|1" thick, **6" segments**|0|The floor benefit — bought by the segment; shapes the whole raid board|
|**Gatehouse**|Building|6×6|−1|A controlled chokepoint: the attacker breaches it or routes around it|
|**Watchtower**|Plant|3×3|0|The defender starts one model in it; denies the attacker surprise|
|**Turret Mount** *(attaches to a Wall or Gatehouse)*|Plant|2×2|−2|Hardpoint. The turret **auto-deploys** — but costs Credits against your Crew Rating and keeps full fragility|
|**EW Mast**|Plant|3×3|−2|Counter-hack and counter-drone: penalises enemy [[Hacking]] in a raid on you; blocks enemy drone deployables|

^tbl-defend-this-is-the-raid-board

- Perimeter Wall — `Scatter · Impassable · Heavy · Climbable, Breachable, Barricadable`
- Gatehouse — `Building · Interior Open · Heavy · Openable, Lockable, Hackable, Climbable`
- Watchtower — `Scatter · Impassable · Light · Climbable`
- Turret Mount — `Feature · Impassable · Light · Powered, Hackable` — hosts one turret [[Deployables|deployable]]
- EW Mast — `Feature · Impassable · Open · Climbable, Powered, Hackable`

> [!danger] The Turret Mount is not free board power
> Owning the mount grants **auto-deploy** only — the turret skips the [[Deployables#Deploying — the INT test|INT test]] and starts online. It still **costs Credits against your Crew Rating** to field, still counts against the **9–12** density band, and keeps full fragility: `WND−1`, repairable once, hijackable. This is the settled answer to a pre-placed settlement deployable being strictly better and free.

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

- [ ] Confirm the board size — **3'×3'** recommended
- [ ] Build cost in **Materials** per structure ([[Economy]])
- [ ] Storage numbers — HQ base cap, gatherer buffer, Storehouse, Vault, Equipment Shed/Armory
- [ ] Persistent armoury: is owned gear **also** points-costed to field (two-gate), or does ownership replace the points cost? ([[Economy]] E2)
- [ ] Replace the destroy-only raid target Water used to provide
- [ ] Generator output: this note says **+3**, `POINTS-DECISIONS.md` D9 says **+5** — reconcile
- [ ] HQ housing: this note says **10** slots, D10 says **12** — reconcile
- [ ] HQ tier costs and the dispatch-slot increment per tier
- [ ] How much a successful raider actually takes from each container
- [ ] Founding **Credits** budget and per-structure founding price
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
