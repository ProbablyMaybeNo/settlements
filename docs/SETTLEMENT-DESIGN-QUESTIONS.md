# Settlement System — Design Analysis & Question Set
*Generated 2026-07-20 from the Settlement note + a full cross-impact pass over every drafted rule. This is the working doc for drafting the SETTLEMENT rules and the edits they force on existing notes. Answer Part D first — everything else hangs off it.*

---

## Part A — What your notes actually ask for (intent, faithfully)

**The 12 settlement mechanics your Settlement note describes or gestures at:**
1. **Founding — choose a location** (hospital→med-bay, police→holding cells, scrapyard→+resources…) each granting an asymmetric starting boost.
2. **Starting structures + starting credits** — a common base set + location-specific extras + a build budget.
3. **Starting layout — the 12×36 grid** (app or paper); placements *become the boards* for some battles (raids).
4. **Hiring a crew gated by structures** — base structures allow ~10 crew; a crew cabin/housing unlocks more recruit (and specialist) slots.
5. **Assigning roles** — recruit people to *work and live* in the settlement and run scout / scavenge / sabotage missions (separate from the battle crew?).
6. **Structure damage** — you *hesitate* on tracking it; float replacing it with **sabotage** (enter → plant → detonate, "not simply firing a rocket at a wall").
7. **Structure repair** — lightweight: a damaged structure gives no benefit / can't be placed until half its cost is repaid.
8. **Building structures** — every building must grant a benefit (list-building / resource-gen / in-battle defence / crew-cap / at minimum a defensive wall).
9. **In-battle buffs from structures** — turrets, reinforced doors, traps on the table.
10. **Resources** — **Goods/stash** (currency), **Materials** (build/repair/research/craft), **Power** (run structures via generators). "Water" is named in the header but never defined.
11. **Upgrading structures** — tiers/costs, undefined.
12. **Settlements in battles** — the narrative fix: fight over territory/supply lines using **encampments** built from owned defensive structures; the **main settlement** is only the board when someone's raided at base; **scavenge** battles use themed random terrain.

**The hard constraints these must respect (your voice + the tenets):**
- **Persist even outside campaigns** — rosters AND settlements grow game-to-game; a **points limit**, not a campaign wrapper, keeps it balanced.
- **Keep list-building minimal — let terrain + base-building shine** (your flagged BIG RULE). Depth lives in the settlement layer, not in point-buy.
- **The board is balanced only on a legal board (9–12 features)** — terrain density is the strongest dial in the game (66-pt swing). Sacred.
- **Tabletop-first** — no rule may *require* the app. The global-map dream stays a meta layer.
- **No pay-to-win / collection-to-win** — a bigger settlement must not beat better play.
- **Lightweight bookkeeping** — you explicitly resist tracking granular damage.
- **Skirmish scale, WND-1 lethality, ±3 modifier cap, one core dice mechanic** — all still hold.

---

## Part B — Master list of settlement mechanics to draft (grouped)

**Founding & Content**
- Location→boost table (each boost pinned to an existing system, not a new minigame)
- Structure catalogue framework: taxonomy (gatherer / crafting / defence / utility / housing), per-building cost, every-entry-maps-to-a-battle-object rule, upgrade tiers
- Faction template & the location-vs-faction axis
- Starting package: base structures + location extras + starting Goods

**Economy (Economy.md — currently empty)**
- Final resource roster (resolve Water + the 5th)
- Inflow (battle awards + settlement production + trade routes + scavenge) & sinks (build / upgrade / repair / recruit / research / craft)
- Power as a capacity/flow model (generator output vs draw), separate from banked currencies
- Anti-inflation levers (storage caps / escalating costs / raids / decay) & upkeep friction
- Persistent armoury / owned-gear ownership vs "weapons are built fresh"
- Research/tech-unlock + crafting pipeline
- Raid resource-theft (the one zero-sum exception to "both crews profit")

**Roster & Crew (affects List Building, Unit Design, Progression)**
- Two-currency roster: Goods to *hire* + points to *field*
- Housing/population cap on the OWNED roster (vs points capping the FIELDED crew)
- Founding/roster-genesis procedure
- Roster-depth anti-snowball friction (upkeep / cap) beyond the +2/−2 valve
- Roster assignment layer (battle vs work vs mission)
- BUILDER as an emergent role (not a new rank)
- Bottomed-out-roster recovery floor

**Board & Battle (affects Scenarios, Core Game Format, Terrain, Infrastructure, Deployables)**
- Board-provenance selector: main-settlement window / owned-structure encampment / themed neutral terrain — each normalized to 9–12 features
- 12×36 grid scale, per-structure footprint, raid-windowing
- Asymmetric raid/defence deployment geometry + attacker-side balancing lever
- New scenario types as reskins (Settlement Raid, Defence, Territory Capture, Supply-Line, Scavenge)
- Sabotage action (enter/plant/detonate + defuse) → structure "go dark" + persistent disabled flag
- Demolition/breach charge as a structure-target deployable class
- Settlement structures → pre-placed Deployables/Infrastructure rights, priced & density-capped
- BUILDER on-table construction (terminals/connections) — adopt / minimal / park?

**Campaign Loop (affects Campaign, Progression; drafts Downtime, Events)**
- Re-frame Campaign as the persistent post-battle loop (runs after *every* game, not just campaigns)
- Downtime action menu + actions-per-cycle + the "cycle" timekeeping tick
- Roles & Missions dispatch (scout/scavenge/sabotage) + resolution + failure→consequence
- Reconcile growth (post-battle Advances vs a downtime "train" action — pick one)
- Bottle→withdrawal roster-save promoted to a real rule, with a price
- Settlement Event tables (disaster / visitor / incoming raid)
- Capture → holding-cells → recovery loop (rescue / ransom / exchange)
- Med-bay healing reconciled with the Advance-heal + the −2 scar rebate

**Territory & Meta (drafts Territory, Diplomacy, Solo & Co-op)**
- Persistent territory ledger (paper-first) + claim/contest/flip state machine
- Supply lines as a meta-scale reuse of Power-Supply run-a-line/cut-a-line
- What holding territory grants (kept anti-snowball — strategic edge, not raw trickle)
- Diplomacy re-scoped: capture loop + light reputation now; alliances parked
- Solo/co-op strategic-map AI + independent per-player tracking
- Global faction-map dream: parked to meta-only

**Cross-cutting gaps the critic flagged (currently unowned)**
- Physical component/representation pipeline (Components.md) — how the layout physically hits the table
- Meta victory/end-state — is persistence bounded (season/settlement victory) or endless?
- Settlement razing/elimination + guaranteed comeback path
- Narrative story-generation engine (Narrative.md)
- Companion-app scope + paper-equivalent fallback for each feature
- Save/ledger format + GM-less trust/verification
- Secondary bases/outposts; layout mutability over time; building-menu unlock gating
- Raid-frequency limits / anti-griefing; new-player strategic catch-up
- Player-to-player trade/gifting; setting-tone guard on the catalogue; mirror-match balance intent

---

## Part C — Already-drafted rules that WILL change

| Note | Change forced | Severity |
|---|---|---|
| **List Building** | "No unit cap" re-scoped to per-battle only; add housing roster cap; add Goods hire-cost alongside points; add founding step | **Breaking** |
| **Core Game Format** | "Resources" (one currency) → typed Goods/Materials; carve raid/sabotage zero-sum exception to "both crews profit" | **Breaking** |
| **Campaign** | Re-frame from campaign-only → persistent post-battle loop; split the bank step by resource; fully define Captured; add downtime hand-off | **Breaking** |
| **Terrain Interaction** | Amend "structural damage out of scope (maybe forever)" + locked note #5 to admit a sabotage benefit-disable (still no wall HP); add Sabotage action; rework the settlement-upgrade→board-state hook off "free/unlimited" | **Breaking** |
| **Infrastructure** | Replace symmetric setup with an asymmetric raid/encampment board-build; defender's layout drives feature placement | **Breaking** |
| **Deployables** | Rework "pre-placed settlement deployable skips the roll" so it isn't strictly-better-and-free; add a structure-target demolition charge class | **Breaking** |
| **Scenarios** | Add a board-provenance axis + density-normalization pass; add the new scenario types as reskins; rename to avoid the "Raid" collision (existing Raid = loot caches) | Additive |
| **Progression** | Reconcile scar-heal vs med-bay; pick single growth home vs downtime "train" | Breaking/minor |
| **Terrain** | Add the mandatory density-normalization pass any player-built board must pass | Breaking |
| **Territory / Economy / Downtime / Events / Diplomacy / Solo & Co-op / Factions / Narrative / Components** | Drafted from empty to match everything above | Additive |
| **Board Representation / Weapons / Conditions** | Minor: new tokens (layout tiles, prisoner, disabled-structure); armoury ownership note | Minor |

---

## DECISIONS LOCKED — 2026-07-20 (round 1)

**Unifying spine (derived):** *Ownership and fielding are orthogonal.* Goods/Materials establish what you **own** (persistent, campaign layer); crew-points establish what you **field** (per battle). Everything below inherits this.

1. **Battle budget → Hybrid (build then deploy).** Structures built with Materials off-table; deploying a structure's piece (turret/door/wall) on a board costs **crew-points**, competing with bodies. Points stay the sole battle gate. Settlement pieces occupy density slots *within* 9–12 (replace neutral terrain, never stack on top). Settlement ownership buys **availability + auto-deploy** (skip the INT deploy test), **not** free board power — this resolves the "free settlement deployable is strictly better" breaking issue.
2. **Structure damage → Binary + sabotage.** No structure HP. Functional | Disabled only. Destroy = the enter/plant/detonate Sabotage scenario (defender DEX-defuses). Repair = flat Materials cost. Terrain Interaction's "out of scope" lock gets a narrow benefit-disable carve-out (still no wall/cover HP). Rebuild-vs-recruit-vs-research tension lives in the Materials economy.
3. **Meta end-state → Endless default + optional season.** Endless points-balanced play is the baseline (base damaged, never razed). Opt-in season layer adds a terminal goal and permits razing, always with a guaranteed comeback. core-008 stays battle-only.
4. **Alpha meta scope → Local slice + capture loop.** Alpha = 2-settlement (or solo-vs-AI) territory frame + capture/holding/recovery loop. Global map, alliances, faction-war PARKED. Diplomacy.md → the capture loop; Factions → 1.

**Confirmed principle:** the settlement **sits on top** of the sim-validated 100-pt point-buy (roster = the pool; points = the gate; 9–12 density stays sacred, any player-built board normalized to it).

### Round 2 (2026-07-20)
5. **Resources → Goods + Materials + Power + Water.** Water = **population upkeep**: consumed per head each cycle, soft-caps crew/worker count, raidable — the single lightweight friction sink AND the 4th resource. Power = generator capacity/flow (output vs draw), not a banked currency.
6. **Roster → one roster + per-cycle assignment.** Same fighters assigned each cycle to Battle / settlement-Work / Mission; sending one out = it can't fight that cycle (opportunity cost). One housing pool.
7. **Physical board → owned scenery as the flagship look, FENCED.** Your scenery provides the *look*; the **settlement sheet is the mechanical source of truth**. Board = your layout normalized to **9–12 features**, each piece's Cover/Movement/Tags **declared at setup from the sheet, never inferred from the model**. Owning more/better terrain changes the table's look, never what the board does. A DIY/paper path remains equally valid (paper-first + no-collection-to-win preserved). Matches the existing Board Representation philosophy.
8. **Housing → generic bunks.** N total OWNED body slots (base ~10, build bunks to raise N); the **pyramid** alone governs the fielded mix. No rank-segmented quarters — hiring a specialist is gated by Goods cost + the pyramid, not a dedicated structure.

### Round 3 (2026-07-20)
9. **Location ⟂ Faction (orthogonal).** FACTION = ideological allegiance + faction-wide buffs AND nerfs + unique units (the future global-map pledge axis). LOCATION = the physical settlement seed + one starting boost. Two independent pre-game choices.
10. **Capture → hook-only + cells raise capacity.** No new in-battle action. A post-battle Fate 'Captured' (4–5) on an enemy left Down-and-held converts to a prisoner. Anyone may hold a few; holding cells (police-station boost) raise capacity + cut escape chance.
11. **Growth → post-battle Advances only; one downtime cycle between EVERY game.** Cut the downtime 'train' action (protects the +2/Advance valve). The cycle runs campaign or not, so settlements/rosters grow in one-offs.
12. **BUILDER → minimal version.** An emergent construction ROLE (a skill off STR's build-defenses clause, not a new rank); one on-table build per game (a terminal OR a connection). Expandable post-alpha.

> **Remaining Part D/E items are now detail-level** — resolve them by proposing concrete values during drafting (sabotage stat, what territory grants, winner-pays-more vs equal, med-bay specifics, actions-per-cycle count, etc.), not another fork round.

---

## Part D — The 8 pivotal forks (answer these first; everything downstream inherits their shape)

**1. Battle budget: single shared pool vs separate settlement/terrain budget.**
When a settlement enters battle, is terrain pointed from the *same* pool as the crew (a "more terrain OR more bodies" dial) or a *separate* allowance? — *You flagged this "needs testing." It's the single most cross-cutting knob: it decides whether resources fund a battle budget, whether the 9-12 density floor can be starved, and whether owned terrain is a density choice or a provenance/buff choice.*
- (a) Separate crew-100 + a capped terrain allowance
- (b) Single combined pool, with terrain layered **above** a mandatory neutral 9-12 floor
- (c) Hybrid: resources build off-table, built pieces cost crew-points to deploy

**2. Does the settlement SIT ON TOP of point-buy, or REPLACE it?**
Roster = merely the pool you draw a points-costed crew from (sim-validated 100-pt system stays the battle gate) **vs** housing headcount becomes the fielding gate (no points). — *Replace collapses the sim-proven balance into a roster-size snowball. Strong recommendation: sit on top.*
- (a) **Sit on top** (recommended) — points stay the battle gate; housing caps only what you *own*
- (b) Replace — housing headcount fields the crew

**3. Structural-damage model.**
Keep granular per-structure HP **vs** go binary functional/disabled with a flat Materials repair and route all destruction through the existing enter-plant-detonate **Sabotage** scenario. — *You already hesitate on tracking; Terrain/Infra twice lock structural damage out. Binary+sabotage is the only path that satisfies both. Recommended.*
- (a) **Binary + flat Materials repair + Sabotage-to-destroy** (recommended)
- (b) Two-state graduated
- (c) Light per-structure HP for base defence only

**4. Is the meta layer bounded or endless — and can a settlement be destroyed?**
Does persistence ever *resolve* (season reset / settlement-development victory / faction-war end) or is it deliberately endless-and-points-balanced? Can a main settlement be permanently razed, and what's the guaranteed comeback? — *core-008 defines only per-battle victory; nothing owns the strategic end-state. This sets the purpose and pacing of the whole persistence pillar.*
- (a) Endless, points-balanced; a base can be damaged but never eliminated
- (b) Season/campaign arcs with a terminal goal; razing possible with a comeback path
- (c) Both supported (endless default + optional season)

**5. Roster model: one shared roster + assignment, or separate combatant/worker populations?**
Send a fighter scavenging = they can't fight this cycle (one roster, opportunity cost) **vs** a separate non-combatant population that staffs jobs. — *The structural spine of the roles/missions/downtime/economy layer.*
- (a) One roster + per-cycle assignment (leaner)
- (b) Separate battle + worker rosters
- (c) Hybrid (fighters *can* work; cheap non-combatants also exist)

**6. Alpha scope of the meta: full Territory/global-map/factions, or a local slice + the capture loop only?**
- (a) Local 2-settlement (or solo-vs-AI) slice + capture loop; park global map & alliances
- (b) Ship a full territory system in the alpha
- (c) Capture loop only; defer all territory

**7. Physical board representation.**
When "your layout becomes the board," is it abstract proxy/DIY print-tiles (fixed footprints) or owned scenery? — *If it needs owned scenery, a developed settlement literally brings more/better terrain = the collection-to-win the tenets forbid. Components.md is empty and owns this.*
- (a) Print-and-cut DIY tiles with fixed grid footprints (paper-complete, no collection)
- (b) Any proxy terrain + a layout sheet (loosest)
- (c) Owned scenery (rejected candidate — collection-to-win risk)

**8. Resolve the resource roster: what is "Water," and what's the 5th resource?**
- (a) Ship on Goods + Materials + Power only; revise the "~5" down
- (b) Water = population/upkeep sustainment (the lightweight friction sink) → 4 resources
- (c) Add Intel (from scouting) and/or a research currency to reach 5

---

## Part E — Full question set (grouped; answer after Part D)

*Each question notes why it matters; a recommended default is marked where the constraints point to one. Budget/density questions that all reduce to Fork 1 are omitted here — answer Fork 1 once.*

### E1 · Founding & Locations
- Complete location roster + each boost (balanced against each other)? Can two players share a location? Is it permanent or re-foundable after a razing?
- Location vs Faction axis — orthogonal (rec.), merged, or nested? (Fork-adjacent; decides if Factions.md and founding co-design.)
- Base starting-structure set + how many extras each location grants + starting Goods amount?
- Alpha founding scope: 1 faction + short location list, 1 faction + fixed location, or locations-only?

### E2 · Economy & Resources
- Inflow: does winning pay *more* than losing, equal base + scenario bonuses (rec.), or a loser catch-up salvage?
- Upkeep friction: none (Power-only), Water/population per-head (one number, rec. if lightweight), or per-building maintenance (heaviest)?
- Anti-inflation set: storage caps + escalating tier costs + raids, no decay (lightest, rec.)? add decay? raids-only?
- Power gating: settlement-wide sum output-vs-draw (rec., trivial to track), grid-adjacency on the 12×36, or district generators?
- How many gates before a gatherer produces: built / built+powered / built+powered+staffed?
- Research & crafting: one Materials pipeline at a crafting station, output priced normally in points (rec.)? split? what does the tree touch — new characteristics vs rank gates?
- Persistent armoury: gear OWNED (Goods) *and* points-costed to field (two-gate), or ownership replaces the points cost?
- Starting "credits" = starting Goods (rec.) — confirm, and set the amount.

### E3 · Roster, Crew & Hiring
- Goods hire-price per rank — a separate scale from the 5/8/16/24 battle points (rec., don't conflate balance with economy pacing), or reuse the numbers?
- Housing: rank-segmented (recruit cabin / specialist quarters / leader's house — matches your note) or generic bunks + pyramid?
- Base housing headcount — ~10 (growth-gate only, near-non-binding day one) or lower (binds from game one)?
- Roster-depth friction — Goods upkeep per housed fighter, a hard roster cap, or trust the points valve? (ties to Fork 5 & E2 upkeep)
- Does the pyramid still bind the fielded crew once housing exists? (rec. keep it — it's the only structural rule)
- Bottomed-out recovery: guaranteed cheap/free re-hire floor so attrition can't soft-lock a player below min-4/one-Leader?

### E4 · Board Building & New Scenarios
- ~~12×36 grid scale (inches/cell) & is the settlement canvas larger than one board?~~ **RESOLVED 2026-07-26 — the "12×36" in the Settlement note always meant INCHES.** The earlier reading (12 cells × 36 cells × 3"/cell → a 3'×9' canvas) was an error. Canvas = **12" × 36" on a 1" grid**, sized to fit a standard **3'×3'** board as the defender's back three 12"×12" density squares. **Groundworks** project expands it to 18"×36" (and 18"×48" for 4'×4' play). See `Structures.md` in the vault.
- ~~Raid window: fixed by defender, randomized, or attacker-chosen?~~ **DEAD — the question no longer exists.** The settlement fits the board, so a raid always uses all of it. Attacker deploys on the far edge and crosses ~24" of neutral ground.
- Fill-and-cap: under-fill → neutral to 9, over-fill → bench down to 12 — confirm, and who places the neutral fill?
- Attacker-side lever offsetting the defender's home-built board: compensation VP/reinforcements, randomized window, capped defensive budget, or asymmetric points?
- Raid win-condition: sabotage a nominated target (Timer), loot the base (Retrieve), or a small family per scenario?
- Do raids keep 6 rounds + equal points, or asymmetric length/points?
- What qualifies as a "defensive structure" for encampments, and the encampment feature budget (tagged subset + fixed 9-12, rec.)?
- Scavenge terrain: fixed printed maps per location, or a themed subset of the 9-12 setup (rec. — preserves variety)?

### E5 · Sabotage & In-Battle Structures
- Sabotage on hit: go-dark only (rec., preserves no-collapse) or full collapse via an Infrastructure keyword?
- Sabotage sequence/stat: 3-step multi-turn INT plant (slow, counterable, engineer) or 2-step DEX same-turn (fast, infiltrator)?
- Defuse: reuse trap-disarm (DEX 7+, nat 1 = boom, rec.), plus INT-Jam if wired?
- Confirm the firewall: in-battle Offline feature damage resets next battle; ONLY sabotage sets the persistent disabled flag. (rec. confirm)
- Demolition charge: structure-only (rec., contract-clean) or also a Blast vs adjacent models (needs a contract exception)?
- Defensive-structure buffs expressed purely as existing Terrain properties (Cover/Impassable/Lockable), never a new durability stat? (rec. confirm)
- Do pre-placed settlement deployables keep full fragility (WND-1, repair-once, hijackable) + the slot/aura caps? (rec. yes)

### E6 · BUILDER / On-table construction
- Adopt BUILDER terminals+connections for the alpha, park it, or ship a minimal one-build-per-game version?
- If adopted: are built terminals destructible (two-class terminal model) or indestructible like scenery? How is automated "control without a hacker" bounded (cap connections / cuttable / only while the source terminal is held)?

### E7 · Campaign Loop, Downtime, Roles & Missions
- Mission resolution: single core test per mission (rec.), a d10 table per type, or narrative?
- Can a fighter be injured/captured/killed on a mission (routes to Fate, rec.), capped light injury only, or missions cost only time/resources?
- Actions per cycle: fixed N, N = assigned workers, or N scales with housing (the crew-cabin model)?
- Growth home: keep Advances post-battle only + cut downtime "train" (rec.), move to a train action, or both (risks the valve)?
- The "cycle" outside a campaign: one downtime cycle between every battle (rec.), campaign-only, or growth-per-battle + passive income per session?
- Event trigger/cadence: roll each cycle, specific triggers only, or minimal-for-alpha?
- What does a successful scout buy (shape / reroll Twist / attacker-defender / see opponent's list)?

### E8 · Capture / Holding / Recovery
- How does capture happen: hook-only conversion of Fate-Captured on enemies you Downed-and-held (rec.), a new mid-battle action, or both?
- Does capture REQUIRE owning holding cells, or do cells just raise capacity/reduce escape? (sets the police-station boost's value)
- Recovery: rescue (Retrieve) scenario, ransom in Goods, prisoner-exchange — and what happens with no ongoing opponent (one-off fallback)?
- Med-bay: +X to the post-battle Fate roll only (no scar removal), a free Med-Kit each battle, or heal scars at a Goods/Materials cost (preserves the −2 rebate trade)?

### E9 · Territory, Diplomacy, Solo/Co-op
- Territory tracking between drop-in/drop-out players: personal frontier ledger (rec.), shared map only in opted campaigns, or a per-settlement territory count?
- What holding territory grants (anti-snowball): strategic edge only (rec.), capped resource trickle w/ upkeep, or a build-slot unlock?
- Supply lines: full node-graph (reuses Power-Supply) or a simple "each connected pair = +X, a won raid cuts it"?
- Control flip on a lost defence: immediate, two-step contested buffer, or an attrition threshold?
- Territory upkeep as an anti-snowball sink: yes per node, no, or only above a threshold?
- Diplomacy alpha content: capture loop + light reputation (rec.), capture only, or add a 2p rematch grudge bonus?
- Faction allegiance: meta-only (rec.), selects your 1 alpha faction's buffs/nerfs, or gates claimable nodes?
- Solo AI on the strategic map: priority list / d10 table (rec.), fixed escalation script, or a scenario deck?
- Co-op: separate settlements + shared frontier (rec.), one pooled settlement, or separate + alliance-territory bonus?

### E10 · Cross-cutting (critic gaps to rule on)
- Components: every structure ships as a print-and-cut tile with a defined footprint + battle-piece mapping? Who authors the art so the paper path is complete?
- Settlement razing: what's lost vs recoverable + the guaranteed re-founding path?
- Trust in GM-less persistent play: honour system, signed/checksummed sheet, or app attestation?
- Narrative engine: mandatory mechanic or optional flavour bolted onto the ledger? What tables convert death/raid/betrayal/scar into beats?
- Companion app: exact ownership (builder / tracker / global map / solo-AI) + a guaranteed paper fallback per feature?
- Secondary bases/outposts: persistent capturable mini-settlements or ephemeral per-battle?
- Layout mutability: can placed structures be moved/demolished/redesigned between battles, at what cost?
- Building-menu unlock: all ~10 available at founding, or gated behind research/blueprints/location?
- Raid-frequency / anti-griefing: cooldown, respite, battered-settlement protection?
- New-player strategic catch-up vs veteran settlements?
- Player-to-player trade/gifting: allowed diplomacy channel or forbidden (collusion)?
- Mirror match (same location/faction): balanced by intent, or asymmetry embraced?
- Setting-tone guard: how far can structures push (grids, terminals, turrets) before it stops feeling like a fought-over suburb?

---
*Next: lock Part D, then we walk Part E section by section, drafting each note and its cross-edits as decisions land.*
