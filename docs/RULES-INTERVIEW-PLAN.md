# Settlements — Rules Interview Plan
*Our working script for completing the ruleset. Started 2026-07-24. Each interview is linked to a vault note (or cross-edit set), dependency-ordered. We walk them one at a time; I propose concrete values, Ross rules, I draft the note + its cross-edits as decisions land. Expect already-drafted sections to shift as we go — that's fine; only genuine game-breakers get flagged mid-flow.*

**Locked context this plan inherits:**
- Setting = **2051, near-future grounded tech** (`docs/SETTING-TECH-2051.md`). 5 factions + 10 locations at release.
- Ownership ⟂ fielding: **Cash / Materials / Power / Water** = what you own; **crew-points** (sim-validated 100-pt) = what you field. Structures build off-table (single Materials cost), deploy for points inside the sacred **9–12** density.
- The 8 pivotal forks are all locked (see `SETTLEMENT-DESIGN-QUESTIONS.md`).
- **Resources:** Cash (currency, formerly "Goods"), Materials (build/repair/craft), Water (per-head upkeep), Power (generator *capacity*, not gathered). One gatherer structure each for Cash / Materials / Water; Power comes from the Reactor.
- **Design law:** every structure has a mechanical purpose, never décor. Every structure that can be fought over appears on the board as *something* (Feature / Terrain / Deployable / terminal).

---

## PHASE 1 — Settlement Core

### Interview 1 — Structures & the Catalogue
**Section:** [[Settlement]] (structures) · new **Structure Catalogue** reference note
**Goal:** the full building list — category, cost, benefit, board-object — every entry mapping to an existing system.
- **[ANSWERED] The picture / aesthetic:** barren battle-scarred lots (lot between brownstones, dead mall car park, overgrown city park, gutted warehouse); build structures onto the space starting with Start-structures; every structure earns its keep.
- **[ANSWERED] HQ** added as a core Start-structure (leaders plan & manage; possible link to leader/downtime upgrades).
- **[ANSWERED] One gatherer per resource** (Cash / Materials / Water); Power via Reactor.
- Q2 · Sixth category? Keep gatherer/crafting/defence/utility/housing, or add **Robotics/Cyber** (drone bay, robot hangar, server/AI core, EW mast)?
- Q3 · Which 2051 structures earn a slot: Drone Bay · Robotics Hangar · Comms/EW Array · Fabricator · Reactor/Microgrid · Server/AI Core · Laser point-defence · HPM swarm-breaker · Multispectral smoke generator?
- Q4 · Scale & tiers: rough total count at release; flat single-tier vs T1→T3 upgrades (bigger board presence per tier)?
- Q5 · HQ's exact job: pure command/downtime hub, or also a board-objective when raided? Does it upgrade with the crew Leader?

### Interview 2 — Founding & Locations
**Section:** [[Settlement]] (founding) · **10-location roster** · socket to [[Factions]]
**Goal:** the founding sequence + all 10 locations and their starting boosts, balanced against each other.
- The 10 locations and each one's single starting boost (pinned to an existing system).
- Founding sequence: pick Location + Faction (orthogonal) → base Start-structures + location extra + starting Cash → place on the barren lot.
- Base Start-structure set (HQ + the three gatherers + Bunkhouse?) and starting Cash/Materials amounts.
- Can two players share a location? Permanent, or re-foundable after a razing?
- Location vs Faction: confirm orthogonal (two independent pre-game picks).

### Interview 3 — Economy & Resources
**Section:** [[Economy]] (Not Started)
**Goal:** the four resource flows, sinks, anti-inflation, armoury, research.
- Inflow confirmed: equal base + objective bonuses. Set the base numbers + what objectives/deeds pay.
- Water upkeep: per-head consumption rate; what happens when you can't pay (soft cap → can't hire? attrition?).
- Anti-inflation set: storage caps + escalating costs + raids (no decay) — confirm and set caps.
- Power model: settlement-wide output-vs-draw sum (each structure draws N, Reactor supplies M); brown-out behaviour.
- Gatherer gating: does a gatherer produce when Built / Built+Powered / Built+Powered+Staffed?
- Persistent armoury: gear OWNED with Cash **and** points-costed to field (two-gate), or ownership replaces points?
- Research & crafting: one Materials pipeline at the Fabricator/Workshop; what does the tree unlock (new characteristics vs rank gates vs 2051 gear)?

### Interview 4 — Roster, Housing & Hiring
**Section:** [[List Building]] (edit) · [[Settlement]] (housing) · [[Unit Design]] (BUILDER role socket)
**Goal:** own-vs-field split made concrete.
- Cash hire-price per rank — separate scale from the 5/8/16/24 battle points, or reuse them?
- Housing: generic bunks (locked) — base headcount (~10?) and Bunkhouse increment.
- Does the pyramid still bind the fielded crew once housing exists? (recommend keep.)
- Roster-depth friction beyond Water upkeep — hard cap, per-head Cash upkeep, or trust the points valve?
- Per-cycle assignment: Battle / Work / Mission — how many can go on Work/Mission vs must-hold-the-line?
- Bottomed-out recovery floor: guaranteed cheap re-hire so attrition can't soft-lock below min-4 / one-Leader.

---

## PHASE 2 — Settlement on the Board

### Interview 5 — Board Provenance & Settlement Scenarios
**Section:** [[Scenarios]] (edit) · [[Terrain]] (density-normalization) · [[Infrastructure]] (asymmetric build) · [[Core Game Format]]
**Goal:** how "your layout becomes the board" without breaking 9–12 or collection-to-win.
- Board-provenance selector: main-settlement window / owned-structure encampment / themed neutral scavenge — each normalized to 9–12.
- Grid scale (inches/cell) and is the settlement canvas larger than one board (raid = a window)?
- Fill-and-cap: under-fill → neutral to 9, over-fill → bench to 12 — who places neutral fill?
- ~~Raid window: fixed by defender / randomized / attacker-chosen?~~ **DEAD 2026-07-26** — the 12"×36" settlement fits the board, so a raid always uses all of it. Attacker-side balancing lever still open.
- New scenario reskins: Settlement Raid, Defence, Territory Capture, Supply-Line, Scavenge (rename to avoid the existing loot "Raid").
- Do raids keep 6 rounds + equal points, or asymmetric length/points?

### Interview 6 — Sabotage & In-Battle Structures
**Section:** [[Terrain Interaction]] (edit) · [[Infrastructure]] · [[Deployables]] (edit)
**Goal:** binary destruction + settlement pieces on the table, fairly priced.
- Sabotage sequence/stat: multi-turn INT plant (slow, counterable) vs 2-step DEX same-turn (fast, infiltrator)?
- Defuse: reuse trap-disarm (DEX 7+, nat-1 = boom) + optional INT-Jam?
- Sabotage effect: go-dark only (no collapse) — confirm; persistent disabled flag; flat Materials repair.
- Demolition charge: structure-only, or also Blast vs adjacent models?
- Settlement deploy-rights: pre-placed pieces keep full fragility (WND-1, repair-once, hijackable) + slot/aura caps; deploy costs points, skip only the INT test.
- Defensive-structure buffs expressed purely as existing Terrain properties (Cover/Impassable/Lockable), no new durability stat?

### Interview 7 — BUILDER / On-table Construction
**Section:** [[Skill Paths]] (new skill) · [[Infrastructure]] hook
**Goal:** the minimal emergent BUILDER.
- Confirm minimal: an emergent construction role (skill off STR's build clause), one on-table build per game (a terminal OR a connection).
- Are built terminals destructible or indestructible? How is "control without a hacker" bounded (cap connections / cuttable / only while source held)?

---

## PHASE 3 — Campaign & Meta

### Interview 8 — The Campaign Cycle & Downtime
**Section:** [[Campaign]] (reframe) · [[Downtime]] (Not Started)
**Goal:** the persistent post-battle loop that runs after *every* game.
- Confirm: one downtime cycle between every battle; growth = post-battle Advances only (cut the "train" action).
- Downtime action menu (scout / scavenge / sabotage / build / heal / recover) + actions-per-cycle (fixed N / = assigned workers / scales with HQ).
- Roles & Missions dispatch: resolution (single core test / d10 table / narrative); can a fighter be hurt/captured/killed on a mission?
- What a successful scout buys (pick scenario / reroll Twist / attacker-defender / see opponent's list).
- Bottle → withdrawal roster-save promoted to a real rule, with a price.

### Interview 9 — Capture, Holding, Recovery & Diplomacy
**Section:** [[Campaign]] · [[Diplomacy]] (capture loop) · [[Progression]] (med-bay reconcile)
**Goal:** the prisoner economy + light reputation.
- Capture: hook-only conversion of Fate-Captured on enemies you Downed-and-held (confirm); cells raise capacity + cut escape.
- Recovery: rescue (Retrieve) scenario / ransom in Cash / prisoner-exchange — and the no-ongoing-opponent fallback.
- Med-bay: +X to post-battle Fate only / free Med-Kit each battle / heal scars at a Cash-Materials cost (preserves the −2 scar rebate).
- Diplomacy alpha: capture loop + light reputation; alliances parked.

### Interview 10 — Progression & Roster Persistence
**Section:** [[Progression]] (Drafted, thin)
**Goal:** how fighters grow and scar over a campaign.
- Exact Advance award rates (kills / deeds / survive / objectives).
- Full scar / injury effect tables.
- Grudges, bonds, narrative traits.
- Promotion into open rank slots; caps (+6 campaign; WND/MOV only via skills).

### Interview 11 — Events & Narrative
**Section:** [[Events]] · [[Narrative]] (both Not Started)
**Goal:** what keeps two campaigns different + how the game tells stories.
- Event triggers/cadence (roll each cycle / specific triggers / minimal-for-alpha); settlement vs world events; one-off vs lasting.
- Narrative engine: mandatory mechanic or optional flavour; tables that convert death / raid / betrayal / scar into beats; character & settlement & regional arcs.

### Interview 12 — Territory & Supply Lines
**Section:** [[Territory]] (Not Started)
**Goal:** the local strategic frame (alpha = 2-settlement slice).
- Territory tracking (personal frontier ledger for drop-in/out) + claim/contest/flip state machine.
- What holding territory grants (anti-snowball: strategic edge, not raw trickle).
- Supply lines as a meta reuse of Power-Supply (run-a-line / cut-a-line on a won raid).
- Control-flip on a lost defence: immediate / two-step contested / attrition threshold. Territory upkeep sink yes/no.

### Interview 13 — Solo & Co-op
**Section:** [[Solo & Co-op]] (Not Started)
**Goal:** automated opponent + shared play, reusing the core loop.
- Solo AI: priority list / d10 table / flowchart; difficulty scaling; strategic-map AI for the meta.
- Co-op: separate settlements + shared frontier / one pooled settlement; how crews combine; reward split. PvPvE handling.

---

## PHASE 4 — Content (2051)

### Interview 14 — Factions
**Section:** [[Factions]] (Not Started) · uses `SETTING-TECH-2051.md`
**Goal:** ~5 factions — identity + one faction-wide buff AND nerf + unique units, each hooking existing systems.
- The 5 faction concepts (interview from scratch — Ross has none drafted). Raw material: the research's rock-paper-scissors triangle (military remnant / scavengers / drone-swarm / EW-cyber / robotics-automation).
- Faction template: identity, unique units, signature ability, faction-wide buff + nerf, roster differences.
- Which faction is stood up *live* first for the playtest; how asymmetry stays lore-born not bolted-on.

### Interview 15 — Near-Future Arsenal & Setting
**Section:** [[Weapons]] (expand) · [[Deployables]] · new **Equipment** · [[Game Vision]] (fold in 2051)
**Goal:** the 2051 kit, built on the existing weapon-construction system.
- New weapon classes/characteristics from the research: directed-energy (laser heat/cooldown, HPM anti-drone), guided small-arms, drone-delivered.
- Equipment layer: AR combat HUD (squad network — jam it and models isolate), exosuits, adaptive camo vs multispectral sensors, APS intercept-save.
- Deployables expansion: recon/attack drones, robot dogs/UGVs, jammer zones, laser point-defence, HPM swarm-breaker, smoke.
- Fold the 2051 setting + tone + the "grounded, not triumphalist" texture into Game Vision.

---

## PHASE 5 — Production

### Interview 16 — Balance · Components · Edge Cases · Rulebook · Playtesting
**Section:** [[Balance]] · [[Components]] · [[Edge Cases]] · [[Rulebook]] · [[Playtesting]] (all Not Started)
**Goal:** the book-ready cluster (mostly downstream of locked systems — lighter interviews).
- Balance: costing formulas for buildings/gear/2051 kit; the tuning spreadsheet.
- Components: every structure as a print-and-cut tile with footprint + battle-piece mapping; token/card/sheet list; who authors art so the paper path is complete.
- Edge Cases: the systematic collision audit (the 2026-07-23 rules audit is a preview).
- Rulebook: chapter structure (the roadmap's target ToC) + worked examples + glossary.
- Playtesting: stages, gate criteria, coverage matrix.

---

*Sequencing note: Interviews 1–4 unblock the most and should land first (they let us draft Settlement + Economy + the roster edits — the true critical path). Phase 4 (Factions/Arsenal) can start early in parallel since the 2051 research is done, but it depends on the economy/armoury decisions in Interview 3. Production (16) is last.*
