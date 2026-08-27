---
type: roadmap
title: Settlements — Rules System Master Roadmap
tags: [settlements/roadmap]
---
# 🗺️ Settlements — Rules System Master Roadmap

Everything needed to take Settlements from *scaffold* to a *complete, book-ready rules system*, in dependency order. Checkboxes are live — tick them as you lock each decision; the Tasks plugin can roll them up. See also [[Rules System MOC]] and [[_Rules Map.canvas|the map]].

> [!important] [[Full Rules System v1]] is the source of truth as of 2026-08-05
> This roadmap is a **log of what got decided when**, so some ticked items below record numbers that have since been superseded — they are marked where that happened. Where this file and the master note disagree, **the master note wins.**

## 1 · Where it stands today

**37 phases** — ✅ **27 drafted** · 🎯 1 milestone · ⬜ 9 not started. *(Recounted 2026-08-05.)*  
Reference notes: [[Weapons]] · [[Skill Paths]] · *(Terrain Features catalogue TBD)*

| Stage | Phases | Status |
|---|---|---|
| **S1 Foundation** | 3 | ✅ All Drafted |
| **S2 Core Combat** | 9 | ✅ All Drafted (bar the Obsidian Guide; some Focus items still open) |
| **S3 Battle Layer** | 7 | ✅ All Drafted |
| **S4 Settlement & Campaign** | 11 | ✅ **8 Drafted** — Campaign · Downtime · **Economy** · **Events** · Progression · **Settlement** · Structures · **Territory** · ⬜ Diplomacy, Narrative, Solo & Co-op |
| **Milestone** | 1 | 🎯 Final Alpha |
| **S5 Content** | 1 | ✅ **Factions Drafted** — framework + roster adopted, names still open |
| **S6 Production** | 5 | ⬜ Not Started — Balance · Components · Edge Cases · Playtesting · Rulebook |

**The 2026-08-05 pass drafted five notes that were empty** — [[Economy]], [[Events]], [[Territory]] and [[Factions]] from the master note's §17–§27, and [[Settlement]]'s founding rules. What remains genuinely unstarted is **Diplomacy · Narrative · Solo & Co-op** in S4 and the whole of **S6 Production**.

## 2 · The decisions that unblock everything

- [x] **Core dice mechanic** ([[Rules Engine]] / [[core-000 Core Test]]) — `1d10 + Stat + mods, 7+`, nat 1/10 auto.
- [x] **Lethality first pass** ([[Damage]]) — Injury roll, WND 1, Down / Stabilize / bleed-out, Fate hook. **Not Locked** until playtested — treat as Drafted, not Done.
- [x] **List Building + Weapons** (2026-07-13) — ranks 5/8/16/24 at a 100-pt budget; weapons built from class + characteristics. Sim-validated to an 11-point spread across 8 archetypes. → [[Crew Sim — Findings]] *(**Scale superseded twice.** 2026-08-05: 1000 Credits, ranks 65/95/165/245. **2026-08-19/20: bodies re-derived from the measured stat ladder and the scale rebased to 850 — ranks are now 70/100/145/185 in both tiers, at 850 Match Play / 425 Campaign Start.** See [[List Building]].)*
- [x] **Terrain density is a BAND (9–12 features), not a floor** — it swings win rate by 66 points, more than any cost. → [[Terrain#Setup procedure]]

Secondary opens: Glorious Deed name ([[Core Game Format]] / [[Scenarios]]), List Building point values, catch-up rule ([[Initiative & Activation]]). *(Skill Paths 9+/11+ → flat 7+ with modifiers: done.)*

## 3 · Critical path to a *playable* game

```
Game Vision → Core Game Format → Rules Engine ⚠dice
   → Unit Design → Movement → { Shooting, Melee } → Damage ⚠lethality → Morale = ✅ PLAYABLE SKIRMISH
Movement → Terrain (core pillar) ─┐
Damage + Morale + Terrain ────────┴→ Scenarios
Core Game Format → Settlement (can start in parallel early)
thin slice of all the above → 🎯 Final Alpha → Playtesting (continuous)
```
Everything in S4–S6 hangs off that spine. Build the spine, gate at a playable skirmish, then widen.

## 4 · Build sequence — per-phase decision checklists

Each phase lists exactly what must be *nailed down* to consider it done. Order = dependency order.


### S1 Foundation
*The skeleton. Pitch, physical format, and the turn+dice engine everything reuses.*

#### 01 · [[Game Vision]] — ✅ Drafted
<small>depends on: —</small>

- [x] A tight elevator pitch: what Settlements is, who fights, and why it's unlike other wargames.
- [ ] 5 ranked design tenets/pillars — ⚠️ **two conflicting lists exist** (Game Vision prose vs the MOC's ranked list). Reconcile into one canonical set before locking.
- [x] The 3–4 signature experiences every battle must deliver (terrain mastery, brutal stakes, emergent stories, persistent attachment).
- [x] The hard non-negotiables (terrain as a major focus, persistent character rosters, ultra-realism, drop-in/out campaign).
- [x] An explicit "what Settlements is NOT" to guard scope creep.

#### 02 · [[Core Game Format]] — ✅ Drafted
<small>depends on: Game Vision</small>

- [x] Board size (3'×3') and any alternates; deployment zones and starting distance / approach march.
- [x] Player counts supported (2p standard now; multiplayer; later solo/co-op/PvPvE) and what each mode needs.
- [x] Game length in turns (6) and in real time (~1.5 hrs); exactly how a game ends.
- [x] Win-condition philosophy: objective-driven, killing optional but conflict inevitable, bottling is the norm.
- [x] Miniature-agnostic standard: base sizes (25/32/50mm) and which fighter types map to each.

#### 03 · [[Rules Engine]] — ✅ Drafted
<small>depends on: Core Game Format</small>

- [x] The turn/round structure and the order of phases within a turn. Standard games = 6 turns.
- [x] How priority/initiative is decided each turn (dice roll + underdog +1) and what winning it grants.
- [x] The universal action economy (activations per unit; leaders/champions may get more; what an activation buys).
- [x] The ONE core dice/resolution mechanic every other system reuses (how a test, hit, or save is rolled).
- [x] Where Morale / Fear / Insanity hook into the timing (e.g. modifying the initiative phase).
- [x] House conventions every section assumes: measuring (pre-measure?), rounding, line-of-sight basis.


### S2 Core Combat
*One playable firefight. ✅ Gate: after Morale you can play a standalone skirmish.*

#### 06 · [[Unit Design]] — ✅ Drafted
<small>depends on: Rules Engine</small>

- [x] Each stat and what it governs: WND, MOV, STR, AGI, DEX, INT, NRV.
- [x] Rank structure (Fighter / Specialist / Leader) + emergent Role — replaces elite/non-elite unlock tree.
- [ ] The data-card layout: stats + skills + equipment + narrative/identity.
- [ ] How weapons & armour attach (separate profiles vs baked-in) — decide here explicitly (*de facto* separate in [[Weapons]], not locked in this note).
- [x] Baseline human numbers (civilian 0, path-stat scale to +6) and rank point budgets.

#### 12 · [[Initiative & Activation]] — ✅ Drafted
<small>depends on: Rules Engine</small>

- [x] Alternating activation; Move + Action per activation; Orders by rank.
- [x] Priority each turn (1d10 + underdog +1).
- [x] Action-economy detail (Move / Action / Sprint / Charge / Ready) — sourced from [[Rules Engine]].
- [x] Reaction options defined (Snap Shot, Dodge, Charge, Throw, Interact, Trigger) + facing / Ready persistence.
- [x] Catch-up — alpha: underdog Priority +1 only (playtest dial).

#### 07 · [[Movement]] — ✅ Drafted
<small>depends on: Unit Design</small>

- [x] Base move, Sprint, Charge.
- [x] Athletic traversal: climb / jump / leap / vault / swim — **AGI** 7+; low leap under 2" = no test, −2" Move.
- [x] Difficult ground = double Move; Impassable handled via [[Terrain]].
- [x] Disengage (Move slot + free swings at −2) — Resolved 2026-07-13.
- [ ] Forced movement (push / knockback / drag) as a universal Movement rule (currently skill-owned).
- [x] Measuring conventions — pre-measure, base-edge, round down ([[Rules Engine]]).

#### 13 · [[Shooting]] — ✅ Drafted
<small>depends on: Unit Design, Movement</small>

- [x] Ranged sequence: declare → range/LOS → `1d10 + DEX` vs 7+ → Injury → +1 Stress.
- [x] DEX drives to-hit; core test method.
- [x] Weapon profile fields live in [[Weapons]] (range, Damage, traits).
- [ ] Target-priority rules (closest? must shoot?).
- [x] Cover modifiers (Light/Heavy/Hidden). Elevation / moving-and-shooting still open.
- [ ] Ammo / reload / jam — deferred (traits TBD in [[Weapons]]); not required for alpha.

#### 14 · [[Melee]] — ✅ Drafted
<small>depends on: Unit Design, Movement</small>

- [x] Engaged within 1"; Charge vs Move-in.
- [x] Opposed STR (or AGI for some weapons); ties to defender; winner → Injury.
- [x] Charge grants +1; no charge bonus if already Engaged / just charged.
- [ ] Positional modifiers (flank / rear / outnumber / high ground) — none at launch, or add later.
- [x] Melee weapon profiles in [[Weapons]].
- [x] Feeds shared [[Damage]] sequence.

#### 15 · [[Damage]] — ✅ Drafted
<small>depends on: Shooting, Melee</small>

- [x] Injury roll: `1d10 + Damage − Armor` vs 7+ → wound or Pinned.
- [x] WND 1 (extra only via skill); Down at 0.
- [x] Down / Stabilize / bleed-out.
- [ ] Criticals beyond nat-10 auto-success — no separate crit table at launch *(confirm reject)*.
- [x] Armour profile (0 / −1 / −2) — see [[Weapons]].
- [x] Post-battle Fate hook ([[Campaign]]).

#### 16 · [[Conditions]] — ✅ Drafted
<small>depends on: Damage</small>

- [x] Full condition list (combat, control, persistent, Nerve, markers).
- [x] Tokens, apply / refresh / expire.
- [x] No stacking; ±3 mod cap; Stress on first apply.
- [x] Sources: Damage, skills, hazards, devices.
- [x] Gritty states: Pinned, Suppressed, Fire, Bleed, Shocked, Bolt / Broken / BugOut.

#### 17 · [[Morale]] — ✅ Drafted
<small>depends on: Damage</small>

- [x] Stress + NRV Break tests (7+); Shaken at 1+; Break at 2+.
- [ ] Crew-wide bottling as the NORM — currently **individual** BugOut / Bolt only.
- [x] Individual Nerve states (Bolt / Broken / BugOut).
- [x] Insanity dropped in favour of BugOut (rout) — playtest Q remains.
- [x] Recovery: Break pass clears; Bravery-path skills for early rally.


### S3 Battle Layer
*The board comes alive — terrain (the core pillar), list-building, and scenarios.*

#### 08 · [[Terrain]] — ✅ Drafted
<small>depends on: Movement</small>

- [x] Terrain properties (Movement / Cover / Tags) + Types that classify ANY piece.
- [x] Cover and true LOS rules.
- [x] Dangerous overlay + hazard → Conditions table.
- [x] Verticality / height advantage / falling.
- [x] Setup procedure + Building access (stairs/ladder) rule.
- [x] Interactive hooks via tags → [[Terrain Interaction]] / [[Hacking]].

#### 09 · [[Terrain Interaction]] — ✅ Drafted
<small>depends on: Terrain</small>

- [x] Interaction actions: Force, Lift, Lockpick, Search, Repair — STR / DEX / INT; AGI is Move-slot.
- [x] Searching and looting (exhaust token + find table).
- [x] Structural integrity: out of scope; feature damage instead.
- [x] In-battle repair of features; settlement upgrades as board state.
- [x] Traps and deployable defences.

#### 33 · [[Hacking]] — ✅ Drafted
<small>depends on: Terrain, Terrain Interaction, Rules Engine</small>

- [x] Terminal Interact sequence (declare → range → INT 7+; Interrupt contests).
- [x] Range bands as modifiers (0 / −1 / −2 / −3), max 24".
- [x] Linked functions menu; hijack an enemy's deployed turret ([[Deployables]]).
- [x] Hacking **v1**: one INT test + **Interrupt** (Overload). Deeper breach system parked ([[Hacking]]).
- [ ] Playtest dials (v1): interrupt strength, gear/skill hack modifiers.

#### 05 · [[List Building]] — ✅ Drafted · **sim-validated**
<small>depends on: Unit Design, Weapons</small>

- [x] The pyramid: 1 Leader · 2 lower-rank per Specialist · 1 Fighter per Recruit · min 4. **No unit cap.**
- [x] Exact costing: ~~ranks **5 / 8 / 16 / 24**, budget **100**~~ → **superseded 2026-08-05** by the 1000-Credit scale and **two starting tiers** (Match Play / Campaign Start). Stats & skills are still FREE — rank is the bundle.
- [x] **Recruit** rank added — the 0-stat body that makes a swarm legally fieldable.
- [ ] **Doctrine** layer (crew identity, 8 archetypes) — **pulled to the campaign layer.** It's a list-building / campaign mechanic, not a first-battle rule; revisit when the campaign phase is built.
- [x] Campaign roster: ~~**+2 per Advance**~~; **scars change nothing** (veterans crowd out rookies = anti-snowball). *(The −2 scar rebate was cut 2026-08-01 — it made scarred veterans cheaper, working against the valve it sat inside. The flat +2 was replaced 2026-08-05 by the priced **10-Level track** — 15/stat point · 20/35/55 per skill tier · 41 for the Level-7 wound, **+241 Credits** for a full track — [[Progression]].)*
- [x] Anti-hero ⅓ cap **cut** — redundant at WND 1.
- [x] Validated: **11-point spread across 8 archetypes** on a legal board → [[Crew Sim — Findings]].
- [ ] Faction selection / buffs & nerfs at list level → socket left open in [[Factions]].
- [ ] Table playtest (all numbers are sim-derived, not table-derived).

#### 34 · [[Infrastructure]] — ✅ Drafted
<small>depends on: Terrain, Terrain Interaction, Hacking, Movement, Conditions</small>

- [x] Infrastructure **reshapes the board**; it does not deal damage (that's [[Deployables]]).
- [x] Five categories + eight board verbs; every feature = category + verb(s) + optional keyword.
- [x] Damage routes through **two** keywords only — **FALL** and **CRUSH** — both built on existing rules.
- [x] 12-feature catalogue; triggers indestructible; operate via hack / manual DEX / Reaction.
- [ ] Table playtest — feature density, toggle tempo.

#### 35 · [[Deployables]] — ✅ Drafted · **sim-validated**
<small>depends on: Weapons, Conditions, Terrain Interaction, Damage</small>

- [x] Bought like gear; **deploy = INT test** (restores INT's battlefield job); one use/battle, kept on roster.
- [x] Four families, 5+ each: turrets (auto-fire), mines (chassis × payload), movement traps, buff/debuff beacons.
- [x] Damage/repair reuse the Feature-damage engine (Offline → repair once → Destroyed).
- [x] Validated: no ceiling breaks, costs price out vs the armoury; Burst Turret repriced 16→18 → [[Deployables Sim — Findings]].
- [ ] Crew-integration sim — deployables inside the full battle loop for win-rate swing.

#### 18 · [[Scenarios]] — ✅ Drafted
<small>depends on: Damage, Morale, Terrain, Terrain Interaction, Hacking, Infrastructure, Deployables</small>

- [x] A scenario template (7 slots: shape, board, deployment, objectives, scoring/victory, length, twist).
- [x] A starter suite — five **shapes**: Take a Hold (Control), Escort (Mobile), Raid (Retrieve), Sabotage (Timer), Power Supply (Network). *Kidnapping = Retrieve+Mobile reskin.*
- [x] Asymmetric attacker/defender (Escort, Sabotage).
- [x] Win conditions beyond kills — **objective-primary**; concession / wipe interaction defined.
- [x] Variability / twist mechanic (1d6 Twist table).
- [ ] Crew-integration sim + table playtest (scoring pace, lone-runner degeneracy check).


### S4 Settlement & Campaign
*The meta-game: bases, economy, and the persistent war between battles.*

#### 10 · [[Settlement]] — ✅ Drafted *(founding drafted 2026-08-05)*
<small>depends on: Core Game Format · catalogue split out to [[Structures]]</small>

- [x] The settlement map and how players place built structures — **12"×36" canvas on a 1" grid**, the defender's back three density squares on a 3'×3' board ([[Structures#The settlement canvas]]).
- [x] Building types and what each does: resource gatherers, crafting stations, defences, utility structures. — **25 drafted in [[Structures]]**
- [ ] Build/upgrade costs and the in-battle buffs structures grant (turrets, reinforced doors, traps).
- [ ] Structural damage and collapse, driving the tough choices: rebuild/reinforce vs recruit vs research.
- [ ] The minimum viable slice the Final Alpha needs (~10 buildings, **4 resources**).

#### 36 · [[Structures]] — ✅ Drafted
<small>depends on: Settlement, Terrain, Terrain Interaction, Infrastructure, Deployables</small>

- [x] **23** structures across Sustain / Convert / Operate / Recover / Defend; 4 starting, the rest founding-eligible from turn one, no prerequisites. *(Was 25 — the Water Reclaimer and Cistern went with Water on 2026-08-01.)*
- [x] Footprint classes — Building 6×6" min · Plant ~3×3" · Station 3×1" min; terrain sizes are approximate, tolerance rule included.
- [x] Every entry ships a [[Terrain#Setup procedure|terrain line]] and a Power draw; **Generator +5** against a starting draw of **3**. *(The old +3 was retired 2026-08-05 — `POINTS-DECISIONS.md` D9 won.)*
- [x] **Costs in Materials — printed 2026-08-05**, plus HQ tiers, Groundworks, and a flat **30 Materials** repair. First-draft, untested.
- [x] **Worker benefits per structure — drafted; the 0–100 Proficiency track is cut.** A worker is assigned or not.
- [x] **Any structure is sabotage-chargeable in any raid** — closes the destroy-only target Water used to provide.

#### 11 · [[Economy]] — ✅ Drafted *(2026-08-05)*
<small>depends on: Settlement</small>

- [x] Resource types and gathering — **Credits · Materials** banked, **Power** a flow. Gatherers, Scavenge dispatches, Search, raiding.
- [x] The spending sinks — structures, upgrades, Groundworks, flat-30 repair, research, crafting; bodies, weapons, Levels, Chems, ransom.
- [x] **Upkeep is deliberately absent** — per-head upkeep was measured, found unnecessary and harmful, and cut. **Crew Rating is the friction** instead: veterans get dearer, so the fielded crew shrinks.
- [x] Anti-inflation — **storage caps with overflow lost**, housing **12 (+6/Bunkhouse)**, equipment **30 (+30/Armory tier)**.
- [x] Founding budget **250 Materials + 150 Credits**; battle reward **65 Cr + 33 Mat** (T12).
- [ ] **The economy sink is still open** — a rich settlement has nothing dear enough to buy. The headline unresolved item.
- [ ] Storage *numbers*, raid take per container, territory supply cost.
- [ ] How a solo or drop-in player tracks their own economy independently.

#### 19 · [[Campaign]] — ✅ Drafted *(thin)*
<small>depends on: Scenarios, Settlement</small>

- [x] Post-battle sequence stub: Survival → Advances → Resources.
- [x] Safe vs Fate table (death / injury / capture / scar / recovery / Hardened).
- [ ] Drop-in / drop-out support spelled out.
- [ ] Full carry-over list (roster, scars, resources, territory tracking).
- [ ] Map / territory frame (→ [[Territory]]).

#### 21 · [[Progression]] — ✅ Drafted *(thin)*
<small>depends on: Campaign</small>

- [x] Advances spend: +1 stat / +1 skill / heal scar.
- [x] Caps (+6 campaign; WND/MOV only via skills); Promotion into open rank slots.
- [ ] Exact Advance award rates (kills / deeds / survive / objectives).
- [ ] Full scar / injury effect tables.
- [ ] Grudges, bonds, narrative traits.

#### 20 · [[Territory]] — ✅ Drafted *(2026-08-05)*
<small>depends on: Campaign</small>

- [x] **The territory card — eleven required fields.** A card missing any of them is not finished.
- [x] Control runs through three states: **Claimed → Controlled → Isolated.** Claimed grants nothing until you spend to hold it.
- [x] **The bonus is access, never power** — holding ground widens what you can do, never makes a fighter stronger.
- [x] **The default loot table** (1d10) — shared by Search, Raid loot and Scavenge dispatches.
- [x] Defending held territory runs through the settlement raid board ([[Terrain]]), with the defender taking all Priority ties.
- [ ] **Supply routes are undrafted** — the card carries a *supply requirement* field, but what a route enables and what raiding it does is unwritten.
- [ ] Terrain-recipe → actual-pieces mapping; loot markers vs the 9–12 density budget; how many territories a map carries.


### Milestone
*First public playtest gate — a thin vertical slice of #1–20.*

#### 32 · [[Final Alpha]] — 🎯 Milestone
<small>depends on: Morale, Scenarios, Settlement, Territory</small>

- [ ] 🎯 FIRST PUBLIC PLAYTEST GATE: 1 faction, 10 units, 10 buildings, 4 resources, 3 scenarios, 1 of each core system. Don't deepen anything until this slice plays.


### S4 Settlement & Campaign
*The meta-game: bases, economy, and the persistent war between battles.*

#### 22 · [[Downtime]] — ✅ Drafted *(2026-08-05)*
<small>depends on: Campaign, Settlement</small>

- [x] **The three-phase campaign turn** — Post-Battle → Settlement → Battle Prep. Everything that said "Settlement Phase" was assuming this sequence before it existed.
- [x] Dispatch menu and count — **one action per HQ tier** (I=1 · II=2 · III=3), two types: **Scout** and **Scavenge**.
- [x] **Train is cut** — growth comes only from post-battle Levels. Craft/repair lives inside the Workbench/Workshop, not a menu entry.
- [x] **Sabotage-by-dispatch is deliberately out of v1** — wrecking a structure needs a raid, which keeps the interesting decision on the table.
- [ ] How solo and co-op players resolve downtime.

#### 23 · [[Events]] — ✅ Drafted *(battlefield only, 2026-08-05)*
<small>depends on: Settlement, Campaign</small>

- [x] **Triggers and frequency — exactly two rolls**, Round 1 and the midpoint round. No running clock.
- [x] **The 1d10 battlefield table**, ten entries, two of them deliberately nothing.
- [x] Effect scope — all one-off; territory cards layer location-specific entries over the standard table.
- [ ] **Settlement events are undrafted** — visitors, disasters, sabotage from off-table.
- [ ] **Map/world events are undrafted** — anything firing in the Settlement Phase rather than during a battle.
- [ ] Expand toward **15–20** entries once the rhythm is confirmed; pick whether the midpoint is Round 3 or 4.

#### 24 · [[Narrative]] — ⬜ Not started
<small>depends on: Campaign</small>

- [ ] How the game generates and prompts story (battle reports, character logs, grudge/bond tracking).
- [ ] Arc frameworks for individual characters, the settlement, and the regional war.
- [ ] Tools/tables that convert mechanical outcomes (a death, a raid, a betrayal) into story beats.
- [ ] Any campaign-chapter hooks that drive a multi-battle narrative forward.

#### 25 · [[Diplomacy]] — ⬜ Not started
<small>depends on: Campaign</small>

- [ ] Reputation/standing tracking and what it affects mechanically.
- [ ] Alliance mechanics: temporary truces, shared objectives, and betrayal.
- [ ] Rivalry/grudge systems between crews and the payoffs they create.
- [ ] How diplomacy scales from 2-player up to multiplayer and PvPvE.

#### 26 · [[Solo & Co-op]] — ⬜ Not started
<small>depends on: Morale, Campaign, Settlement</small>

- [ ] The automated-opponent system: how enemy units choose actions (priority lists / simple flowcharts).
- [ ] Solo scenario setup and difficulty scaling.
- [ ] Co-op: shared vs separate settlements, how players combine crews, and how rewards are split.
- [ ] PvPvE handling (AI threats appearing during a 2-player game).
- [ ] How all of this reuses the core rules rather than spawning a parallel ruleset.


### S5 Content
*Real factions, built on systems that already exist.*

#### 04 · [[Factions]] — ✅ Drafted *(2026-08-05)*
<small>depends on: Unit Design, List Building, Settlement, Morale</small>

- [x] **The template: one battlefield rule + one settlement affinity.** No flat stat bonus, **no matched drawback**, no exclusive unlock — balanced peer-to-peer.
- [x] Every rule hooks into an existing system — a discount, a conditional modifier, an action-economy nudge, or a terrain-verb exception. **None touches a hard ceiling.**
- [x] **Six factions adopted** — Military · First Responders · Labor · Residents · Tech Workers · Criminals. Supersedes the flat-bonus WIP roster.
- [x] Asymmetry comes from the setting — each faction is who these people *were* before the war.
- [ ] **Final names** — the WIP list's voice (Lost Batallion, The HACKERS) may beat the plain labels. Your call.
- [ ] Tighten each rule to an actionable number — First Responders' "improved Build test" has no value yet.
- [ ] Confirm at the table that each rule is genuinely *identity-defining* rather than merely flavourful.


### S6 Production
*Balance maths, physical components, the written rulebook, edge-case audit, and playtest cycle.*

#### 27 · [[Balance]] — ⬜ Not started
<small>depends on: Factions, Scenarios, Economy</small>

- [ ] Costing formulas for units, weapons, gear, buildings, and resources.
- [ ] Faction win-rate balancing once the factions exist.
- [ ] Scenario balance — keeping asymmetric setups fair and fun.
- [ ] Campaign-economy balance so no player snowballs out of reach.
- [ ] The spreadsheet/data model you tune from playtest results.

#### 28 · [[Components]] — ⬜ Not started
<small>depends on: —</small>

- [ ] The full component list: tokens (conditions, objectives, wounds), cards (units, scenarios, events), sheets (roster, settlement map).
- [ ] What each component must display, in a print- and DIY-friendly format.
- [ ] The settlement-map sheet players use to build their boards.
- [ ] A rule of thumb: don't finalise any component until the system it represents is locked.

#### 29 · [[Rulebook]] — ⬜ Not started
<small>depends on: —</small>

- [ ] Document structure: a quickstart/learn-to-play, the core rules, the advanced/campaign layer, and a reference section.
- [ ] Worked examples and diagrams for every tricky system.
- [ ] A glossary of keywords/USRs and a usable index.
- [ ] A natural-English writing standard — minimal jargon, readable by a newcomer.
- [ ] Page-layout discipline: scenarios on a spread, profiles that fit their box.

#### 31 · [[Edge Cases]] — ⬜ Not started
<small>depends on: Movement, Terrain, Morale</small>

- [ ] A systematic audit of system pairs that collide (forced movement + falling + collapsing terrain; suppression + morale; etc.).
- [ ] Priority rulings for ambiguous stacks of rules.
- [ ] A FAQ/errata list seeded from playtest breakages.
- [ ] A stress-test of the realism mechanics that intentionally create emergent chaos, so they break in fun ways, not broken ways.

#### 30 · [[Playtesting]] — ⬜ Not started
<small>depends on: Final Alpha</small>

- [ ] The playtest stages and the gate criteria to advance from each.
- [ ] What you measure: game length, bottling rates, balance, fun, and rules clarity.
- [ ] How feedback is captured and fed back into the rules.
- [ ] A coverage matrix across factions, scenarios, player counts, and solo/co-op.

## 5 · Gates & milestones

- [ ] **G1 — Engine locked:** dice + turn + activation fixed ([[Rules Engine]]). Unblocks all combat.
- [ ] **G2 — Playable skirmish:** [[Unit Design]]→[[Morale]] drafted; two crews can fight one board start-to-finish.
- [ ] **G3 — Board alive:** [[Terrain]] + [[Scenarios]] drafted; a battle has a point and interactive terrain.
- [ ] **G4 — Campaign loop:** [[Settlement]] + [[Campaign]] thin slice; crews and bases persist between games.
- [ ] **🎯 Final Alpha:** [[Final Alpha]] — 1 faction, 10 units, 10 buildings, 4 resources, 3 scenarios, 1 of each core system.
- [ ] **G5 — Content complete:** [[Factions]] + [[Balance]] done; the game is feature-complete and tuned.
- [ ] **G6 — Book-ready:** [[Components]], [[Rulebook]], [[Edge Cases]] done; [[Playtesting]] through Release Candidate.

## 6 · From rules → rulebook (target table of contents)

When the systems below are *locked*, they drop straight into these chapters ([[Rulebook]] is the phase that writes them):

**Learn to Play (quickstart)** — a stripped 1-page skirmish using [[Core Game Format]] + [[Rules Engine]] + [[Movement]]/[[Shooting]]/[[Melee]].

**Part I — Core Rules**
- [ ] [[Core Game Format]]
- [ ] [[Rules Engine]]
- [ ] [[Unit Design]]
- [ ] [[Initiative & Activation]]
- [ ] [[Movement]]
- [ ] [[Shooting]]
- [ ] [[Melee]]
- [ ] [[Damage]]
- [ ] [[Conditions]]
- [ ] [[Morale]]
- [ ] [[Terrain]]
- [ ] [[Terrain Interaction]]
- [ ] [[Hacking]]
- [ ] [[List Building]]
- [ ] [[Scenarios]]

**Part II — Campaign & Settlement**
- [ ] [[Settlement]]
- [ ] [[Economy]]
- [ ] [[Campaign]]
- [ ] [[Downtime]]
- [ ] [[Events]]
- [ ] [[Progression]]
- [ ] [[Territory]]
- [ ] [[Narrative]]
- [ ] [[Diplomacy]]
- [ ] [[Solo & Co-op]]

**Part III — Factions & Content**
- [ ] [[Factions]]  · unit/weapon/equipment/scenario data appendices

**Reference** — glossary of keywords/USRs, component & token list ([[Components]]), settlement-map sheet, index.

## 7 · Definition of a *complete* rules system

You can call the rules system complete when **all of these are true**:
- [ ] Every S1–S4 phase is at least **Drafted**, and every *core* system is **Playtested → Locked**.
- [ ] The two headline opens (dice, lethality) are **Locked**, not just recommended.
- [ ] One faction plays a full campaign loop end-to-end without a rules gap (the Final Alpha slice, widened).
- [ ] Every rule in the [[Rules System MOC|ledger]] has real text, a category, and a locked status.
- [ ] [[Edge Cases]] audit passed — no unresolved system collisions.
- [ ] [[Rulebook]] chapters above are all backed by a locked phase → the book can be written without inventing rules.

---
*Generated from the canonical phase notes. Re-run the importer after Notion changes to refresh both this and the map.*