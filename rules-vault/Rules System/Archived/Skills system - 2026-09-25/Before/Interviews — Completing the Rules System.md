---
type: interview-script
title: Interviews — Completing the Rules System
tags: [settlements/interview, settlements/dashboard]
---
# 🎙️ Interviews — Completing the Rules System

The live working script for finishing the ruleset. **16 interviews**, dependency-ordered, each linked to its rule note(s). We walk them one at a time: I propose concrete values, you rule, I draft the note + its cross-edits. **Tick a box when a question's answered and jot the call on the `Answer:` line** — the Tasks plugin rolls up what's left. See [[Rules System — Master Roadmap]] · [[Rules System MOC]] · `docs/RULES-INTERVIEW-PLAN.md` (repo mirror of this).

>[!danger] SUPERSEDED — historical record, not live rules (flagged 2026-08-29)
> This is the **2026-07 working script**. Its "locked context" below is **three generations stale** and must not be cited as current: **Cash** is now **Credits** · **Water was cut** (2026-08-01) · the **100-point / 5-8-16-24 scale** is retired (now **850 Credits**, ranks **70/100/145/185**) · **Reactor** is **Power**. The live source of truth is [[Full Rules System v1]]; its §29 carries what is actually open. Keep this note for the decision trail, not for values.

> [!info] Locked context every interview inherits
> - **Setting = 2051, near-future grounded tech** (`docs/SETTING-TECH-2051.md`). **5 factions + 10 locations** at release.
> - **Ownership ⟂ fielding:** Cash / Materials / Power / Water = what you *own*; **crew-points** (sim-validated 100-pt) = what you *field*. Structures build off-table (single **Materials** cost), deploy for points inside the sacred **9–12** density.
> - **Resources:** **Cash** (currency, was "Goods") · **Materials** (build/repair/craft) · **Water** (per-head upkeep) · **Power** (Reactor *capacity*, not gathered). One gatherer each for Cash / Materials / Water.
> - **Design law:** every structure has a mechanical purpose, never décor. Everything fought-over shows on the board as *something* (Feature / Terrain / Deployable / terminal).
> - The 8 pivotal forks are all locked — see `docs/SETTLEMENT-DESIGN-QUESTIONS.md`.

---

## PHASE 1 · Settlement Core

### Interview 1 — Structures & the Catalogue
**Notes:** [[Settlement]] (structures) · new **Structure Catalogue** reference
**Goal:** the full building list — category, Materials cost, benefit, board-object — each mapping to an existing system.

- [x] **The picture / aesthetic.**
	- *Answer:* Barren, battle-scarred lot (vacant lot between brownstones · dead mall car park · overgrown city park · gutted warehouse) — damaged, overgrown, showing recent conflict. You build structures onto it starting with the **Start-structures**. Every structure earns its keep mechanically.
- [x] **HQ** is a core Start-structure.
	- *Answer:* Command hub — crew leaders plan tactics & manage the settlement. Likely the mandatory first build; candidate to link to leader / downtime upgrades. *(Exact job → Q5.)*
- [x] **One gatherer per resource** (Cash / Materials / Water); Power via the Reactor.
	- *Answer:* Confirmed.
- [ ] **Q2 — Sixth category?** Keep gatherer / crafting / defence / utility / housing, or add **Robotics/Cyber** (drone bay, robot hangar, server/AI core, EW mast)?
	- *Answer:* I think, Scavenger (Scavenging, gathering, looting, basically anything related to generating resources), Processor (Anything related to turing resources into cash, materials, water, power, etc.), Crafter (Self explanitory), systems (Anything tech related), utility (Power, water, resources things like generators, water pumps, etc), defenses (Self explanitory), housing (Self explanitory).
- [ ] **Q3 — Which 2051 structures earn a slot?** Drone Bay · Robotics Hangar · Comms/EW Array · Fabricator · Reactor/Microgrid · Server/AI Core · Laser point-defence · HPM swarm-breaker · Multispectral smoke generator — in/out, and what's missing?
	- *Answer:* Drone Bay, Robotics Workshop, Server, those should cover everything...maybe an Advanced Weapons lab.
- [ ] **Q4 — Scale & tiers?** Rough total structure count at release; flat single-tier vs **T1→T3** upgrades (bigger board presence per tier)?
	- *Answer:* There should be 5 to 10 structures.
- [ ] **Q5 — HQ's exact job?** Pure command/downtime hub, or also a board-objective when raided — and does it upgrade alongside the crew Leader?
	- *Answer:* I think it is mainly out of battle stuff but during battle maybe it's the location for the players cash and equipment, loot, etc. The player can build vaults which is a literally vault add on to the HQ building that holds cash, equipment, resources, etc, and is exceptionally hard to break into during a raid. 

### Interview 2 — Founding & Locations
**Notes:** [[Settlement]] (founding) · **10-location roster** · socket to [[Factions]]
**Goal:** the founding sequence + all 10 locations and their starting boosts, balanced against each other.

- [ ] The 10 locations and each one's single starting boost (pinned to an existing system).
	- *Answer:* 
- [ ] Founding sequence: Location + Faction (orthogonal) → base Start-structures + location extra + starting Cash → place on the lot.
	- *Answer:* 
- [ ] Base Start-structure set (HQ + the three gatherers + Bunkhouse?) and starting Cash / Materials amounts.
	- *Answer:* 
- [ ] Can two players share a location? Permanent, or re-foundable after a razing?
	- *Answer:* 
- [ ] Confirm Location ⟂ Faction (two independent pre-game picks).
	- *Answer:* 

### Interview 3 — Economy & Resources
**Notes:** [[Economy]] *(Not Started)*
**Goal:** the four resource flows, sinks, anti-inflation, armoury, research.

- [ ] Inflow (equal base + objective bonuses): set the base numbers + what objectives/deeds pay.
	- *Answer:* 
- [ ] Water upkeep: per-head rate; what happens when you can't pay (can't hire? attrition?).
	- *Answer:* 
- [ ] Anti-inflation: storage caps + escalating costs + raids (no decay) — confirm + set caps.
	- *Answer:* 
- [ ] Power model: settlement-wide output-vs-draw (each structure draws N, Reactor supplies M); brown-out behaviour.
	- *Answer:* 
- [ ] Gatherer gating: produces when Built / Built+Powered / Built+Powered+Staffed?
	- *Answer:* 
- [ ] Persistent armoury: gear OWNED (Cash) **and** points-costed to field, or ownership replaces points?
	- *Answer:* 
- [ ] Research & crafting: one Materials pipeline at Fabricator/Workshop; what does the tree unlock?
	- *Answer:* 

### Interview 4 — Roster, Housing & Hiring
**Notes:** [[List Building]] (edit) · [[Settlement]] (housing) · [[Unit Design]] (BUILDER socket)
**Goal:** own-vs-field split made concrete.

- [ ] Cash hire-price per rank — separate scale from the 5/8/16/24 battle points, or reuse them?
	- *Answer:* 
- [ ] Housing: generic bunks — base headcount (~10?) and Bunkhouse increment.
	- *Answer:* 
- [ ] Does the pyramid still bind the fielded crew once housing exists?
	- *Answer:* 
- [ ] Roster-depth friction beyond Water — hard cap, per-head Cash upkeep, or trust the points valve?
	- *Answer:* 
- [ ] Per-cycle assignment: Battle / Work / Mission — how many can leave the line?
	- *Answer:* 
- [ ] Bottomed-out recovery floor so attrition can't soft-lock below min-4 / one-Leader.
	- *Answer:* 

---

## PHASE 2 · Settlement on the Board

### Interview 5 — Board Provenance & Settlement Scenarios
**Notes:** [[Scenarios]] (edit) · [[Terrain]] (density-normalization) · [[Infrastructure]] · [[Core Game Format]]
**Goal:** "your layout becomes the board" without breaking 9–12 or collection-to-win.

- [ ] Board-provenance selector: settlement window / owned-structure encampment / themed scavenge — each normalized to 9–12.
	- *Answer:* 
- [x] Grid scale (inches/cell); is the canvas larger than one board (raid = a window)?
	- *Answer:* **1" grid. Canvas is 12" × 36" — it is NOT larger than one board.** It fits the defender's back three 12"×12" density squares on a 3'×3'. [[Structures#The settlement canvas]]
- [ ] Fill-and-cap: under-fill → neutral to 9, over-fill → bench to 12. Who places neutral fill?
	- *Answer:* 
- [x] Raid window: fixed by defender / randomized / attacker-chosen? Attacker-side balancing lever?
	- *Answer:* **Question is dead** — the settlement fits the board, so a raid always uses all of it. Attacker deploys on the far edge and crosses ~24" of neutral ground; that approach is the attacker-side cost. Lever still open.
- [ ] New scenario reskins: Settlement Raid / Defence / Territory Capture / Supply-Line / Scavenge (rename vs the loot "Raid").
	- *Answer:* 
- [ ] Raids: keep 6 rounds + equal points, or asymmetric length/points?
	- *Answer:* 

### Interview 6 — Sabotage & In-Battle Structures
**Notes:** [[Terrain Interaction]] (edit) · [[Infrastructure]] · [[Deployables]] (edit)
**Goal:** binary destruction + settlement pieces on the table, fairly priced.

- [ ] Sabotage sequence/stat: multi-turn INT plant vs 2-step DEX same-turn?
	- *Answer:* 
- [ ] Defuse: reuse trap-disarm (DEX 7+, nat-1 = boom) + optional INT-Jam?
	- *Answer:* 
- [ ] Sabotage effect = go-dark only (no collapse); persistent disabled flag; flat Materials repair.
	- *Answer:* 
- [ ] Demolition charge: structure-only, or also Blast vs adjacent models?
	- *Answer:* 
- [ ] Settlement deploy-rights keep full fragility (WND-1, repair-once, hijackable) + slot/aura caps; cost points, skip only the INT test.
	- *Answer:* 
- [ ] Defensive buffs = existing Terrain properties only (Cover/Impassable/Lockable), no new durability stat?
	- *Answer:* 

### Interview 7 — BUILDER / On-table Construction
**Notes:** [[Skill Paths]] (new skill) · [[Infrastructure]] hook
**Goal:** the minimal emergent BUILDER.

- [ ] Confirm minimal: emergent role (skill off STR's build clause), one on-table build per game (terminal OR connection).
	- *Answer:* 
- [ ] Built terminals destructible or indestructible? How is "control without a hacker" bounded?
	- *Answer:* 

---

## PHASE 3 · Campaign & Meta

### Interview 8 — The Campaign Cycle & Downtime
**Notes:** [[Campaign]] (reframe) · [[Downtime]] *(Not Started)*
**Goal:** the persistent post-battle loop that runs after *every* game.

- [ ] Confirm: one downtime cycle between every battle; growth = post-battle Advances only (cut "train").
	- *Answer:* 
- [ ] Downtime action menu (scout / scavenge / sabotage / build / heal / recover) + actions-per-cycle (fixed N / = workers / scales with HQ).
	- *Answer:* 
- [ ] Roles & Missions: resolution (single test / d10 table / narrative); can a fighter be hurt/captured/killed?
	- *Answer:* 
- [ ] What a successful scout buys (pick scenario / reroll Twist / attacker-defender / see list).
	- *Answer:* 
- [ ] Bottle → withdrawal roster-save as a real rule, with a price.
	- *Answer:* 

### Interview 9 — Capture, Holding, Recovery & Diplomacy
**Notes:** [[Campaign]] · [[Diplomacy]] (capture loop) · [[Progression]] (med-bay reconcile)
**Goal:** the prisoner economy + light reputation.

- [ ] Capture = hook-only conversion of Fate-Captured on enemies you Downed-and-held; cells raise capacity + cut escape.
	- *Answer:* 
- [ ] Recovery: rescue scenario / ransom in Cash / exchange — plus the no-opponent fallback.
	- *Answer:* 
- [ ] Med-bay: +X to Fate only / free Med-Kit each battle / heal scars at a Cash-Materials cost (keeps the −2 rebate).
	- *Answer:* 
- [ ] Diplomacy alpha = capture loop + light reputation; alliances parked.
	- *Answer:* 

### Interview 10 — Progression & Roster Persistence
**Notes:** [[Progression]] *(Drafted, thin)*
**Goal:** how fighters grow and scar over a campaign.

- [ ] Exact Advance award rates (kills / deeds / survive / objectives).
	- *Answer:* 
- [ ] Full scar / injury effect tables.
	- *Answer:* 
- [ ] Grudges, bonds, narrative traits.
	- *Answer:* 
- [ ] Promotion into open rank slots; caps (+6; WND/MOV only via skills).
	- *Answer:* 

### Interview 11 — Events & Narrative
**Notes:** [[Events]] · [[Narrative]] *(both Not Started)*
**Goal:** what keeps two campaigns different + how the game tells stories.

- [ ] Event triggers/cadence (roll each cycle / triggers / minimal-for-alpha); settlement vs world; one-off vs lasting.
	- *Answer:* 
- [ ] Narrative engine: mandatory or optional; tables that convert death / raid / betrayal / scar into beats; character/settlement/regional arcs.
	- *Answer:* 

### Interview 12 — Territory & Supply Lines
**Notes:** [[Territory]] *(Not Started)*
**Goal:** the local strategic frame (alpha = 2-settlement slice).

- [ ] Territory tracking (personal frontier ledger) + claim/contest/flip state machine.
	- *Answer:* 
- [ ] What holding territory grants (anti-snowball: strategic edge, not raw trickle).
	- *Answer:* 
- [ ] Supply lines as a meta reuse of Power-Supply (run-a-line / cut-a-line on a won raid).
	- *Answer:* 
- [ ] Control-flip on a lost defence: immediate / two-step / attrition. Territory upkeep sink yes/no.
	- *Answer:* 

### Interview 13 — Solo & Co-op
**Notes:** [[Solo & Co-op]] *(Not Started)*
**Goal:** automated opponent + shared play, reusing the core loop.

- [ ] Solo AI: priority list / d10 table / flowchart; difficulty scaling; strategic-map AI.
	- *Answer:* 
- [ ] Co-op: separate settlements + shared frontier / pooled; how crews combine; reward split; PvPvE.
	- *Answer:* 

---

## PHASE 4 · Content (2051)

### Interview 14 — Factions
**Notes:** [[Factions]] *(Not Started)* · uses `docs/SETTING-TECH-2051.md`
**Goal:** ~5 factions — identity + one faction-wide buff AND nerf + unique units, each hooking existing systems.

- [ ] The 5 faction concepts (from scratch). Raw material: research triangle — military remnant / scavengers / drone-swarm / EW-cyber / robotics-automation.
	- *Answer:* 
- [ ] Faction template: identity, unique units, signature ability, buff + nerf, roster differences.
	- *Answer:* 
- [ ] Which faction is stood up live first for the playtest; asymmetry stays lore-born.
	- *Answer:* 

### Interview 15 — Near-Future Arsenal & Setting
**Notes:** [[Weapons]] (expand) · [[Deployables]] · new **Equipment** · [[Game Vision]] (fold in 2051)
**Goal:** the 2051 kit, built on the existing weapon-construction system.

- [ ] New weapon classes/characteristics: directed-energy (laser heat/cooldown, HPM anti-drone), guided small-arms, drone-delivered.
	- *Answer:* 
- [ ] Equipment layer: AR combat HUD (squad network — jam it, models isolate), exosuits, adaptive camo vs multispectral sensors, APS intercept-save.
	- *Answer:* 
- [ ] Deployables expansion: recon/attack drones, robot dogs/UGVs, jammer zones, laser point-defence, HPM swarm-breaker, smoke.
	- *Answer:* 
- [ ] Fold the 2051 setting + tone (grounded, not triumphalist) into Game Vision.
	- *Answer:* 

---

## PHASE 5 · Production

### Interview 16 — Balance · Components · Edge Cases · Rulebook · Playtesting
**Notes:** [[Balance]] · [[Components]] · [[Edge Cases]] · [[Rulebook]] · [[Playtesting]] *(all Not Started)*
**Goal:** the book-ready cluster (mostly downstream — lighter interviews).

- [ ] Balance: costing formulas for buildings / gear / 2051 kit; the tuning spreadsheet.
	- *Answer:* 
- [ ] Components: every structure as a print-and-cut tile (footprint + battle-piece mapping); token/card/sheet list; art path.
	- *Answer:* 
- [ ] Edge Cases: the systematic collision audit (the 2026-07-23 rules audit is a preview).
	- *Answer:* 
- [ ] Rulebook: chapter structure (roadmap ToC) + worked examples + glossary.
	- *Answer:* 
- [ ] Playtesting: stages, gate criteria, coverage matrix.
	- *Answer:* 

---
> [!tip] How we use this
> Interviews **1–4 are the critical path** (they draft Settlement + Economy + the roster edits). Phase 4 can start early in parallel since the 2051 research is done. Production (16) is last. Tick boxes as we lock each answer; I draft the linked note + cross-edits as we go.
