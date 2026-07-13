---
type: roadmap
title: Settlements — Rules System Master Roadmap
tags: [settlements/roadmap]
---
# 🗺️ Settlements — Rules System Master Roadmap

Everything needed to take Settlements from *scaffold* to a *complete, book-ready rules system*, in dependency order. Checkboxes are live — tick them as you lock each decision; the Tasks plugin can roll them up. See also [[Rules System MOC]] and [[_Rules Map.canvas|the map]].

## 1 · Where it stands today

**33 phases** (incl. [[Hacking]]) — ✅ **17 drafted** · 🎯 1 milestone · ⬜ 15 not started.  
Reference notes: [[Weapons]] · [[Skill Paths]] · *(Terrain Features catalogue TBD)*

| Stage | Phases | Status |
|---|---|---|
| **S1 Foundation** | 3 | ✅ All Drafted |
| **S2 Core Combat** | 8 | ✅ All Drafted (some Focus items still open) |
| **S3 Battle Layer** | 5 | 🟡 4 Drafted · Scenarios empty |
| **S4 Settlement & Campaign** | 10 | 🟡 Campaign + Progression Drafted · rest empty |
| **Milestone** | 1 | 🎯 Final Alpha |
| **S5 Content** | 1 | ⬜ Not Started |
| **S6 Production** | 5 | ⬜ Not Started |

## 2 · The decisions that unblock everything

- [x] **Core dice mechanic** ([[Rules Engine]] / [[core-000 Core Test]]) — `1d10 + Stat + mods, 7+`, nat 1/10 auto.
- [x] **Lethality first pass** ([[Damage]]) — Injury roll, WND 1, Down / Stabilize / bleed-out, Fate hook. **Not Locked** until playtested — treat as Drafted, not Done.

Secondary opens: Glorious Deed name ([[Core Game Format]] / [[Scenarios]]), List Building point values, catch-up rule ([[Initiative & Activation]]), Skill Paths 9+/11+ cleanup to flat 7+.

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
- [x] Rank structure (Recruit / Specialist / Leader) + emergent Role — replaces elite/non-elite unlock tree.
- [ ] The data-card layout: stats + skills + equipment + narrative/identity.
- [ ] How weapons & armour attach (separate profiles vs baked-in) — decide here explicitly (*de facto* separate in [[Weapons]], not locked in this note).
- [x] Baseline human numbers (civilian 0, path-stat scale to +6) and rank point budgets.

#### 12 · [[Initiative & Activation]] — ✅ Drafted
<small>depends on: Rules Engine</small>

- [x] Alternating activation; Move + Action per activation; Orders by rank.
- [x] Priority each turn (1d10 + underdog +1).
- [x] Action-economy detail (Move / Action / Sprint / Charge / Ready) — sourced from [[Rules Engine]].
- [ ] Reaction options fully defined (Snap Shot, Charge, Throw, Interact, Trigger are *named* only — need resolution text).
- [ ] Catch-up / rubber-band so a larger crew can't dogpile the last models.

#### 07 · [[Movement]] — ✅ Drafted
<small>depends on: Unit Design</small>

- [x] Base move, Sprint, Charge.
- [x] Athletic traversal: climb / jump / leap / vault / swim — **AGI** 7+; low leap under 2" = no test, −2" Move.
- [x] Difficult ground = double Move; Impassable handled via [[Terrain]].
- [x] Disengage (both slots + free swings at −2) — playtest dial still open.
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

- [x] Terminal Interact sequence (declare → range → INT 7+ or opposed).
- [x] Range bands as modifiers (0 / −1 / −2 / −3), max 24".
- [x] Linked functions menu; turrets controlled-only.
- [x] Hacker-vs-hacker shut-outs: opposed INT → Effect roll → Shut-out table.
- [ ] Playtest dials: Take Over frequency, Overload lethality, Shut down duration.

#### 05 · [[List Building]] — ✅ Drafted *(thin)*
<small>depends on: Unit Design</small>

- [x] Fielding caps: 1 Leader · ≤2 Specialists · rest Recruits; ~⅓ budget anti-hero.
- [ ] Exact costing numbers (rank base, per-stat, weapons, skills).
- [ ] Faction selection / buffs & nerfs at list level.
- [ ] Pickup list vs persistent campaign roster differences.
- [x] Caps / restrictions that keep lists legal (no-heroes honour).

#### 18 · [[Scenarios]] — ⬜ Not Started
<small>depends on: Damage, Morale, Terrain</small>

- [ ] A scenario template (setup, deployment, objectives, twist, victory conditions, length).
- [ ] A starter suite: Caravan Escort, Settlement Raid, Kidnapping, Sabotage.
- [ ] Asymmetric attacker/defender setups.
- [ ] Win conditions beyond kills; bottling interaction.
- [ ] Variability / twist mechanic.


### S4 Settlement & Campaign
*The meta-game: bases, economy, and the persistent war between battles.*

#### 10 · [[Settlement]] — ⬜ Not started
<small>depends on: Core Game Format</small>

- [ ] The settlement map and how players place built structures — these placements literally become the boards battles are fought on.
- [ ] Building types and what each does: resource gatherers, crafting stations, defences, utility structures.
- [ ] Build/upgrade costs and the in-battle buffs structures grant (turrets, reinforced doors, traps).
- [ ] Structural damage and collapse, driving the tough choices: rebuild/reinforce vs recruit vs research.
- [ ] The minimum viable slice the Final Alpha needs (~10 buildings, ~5 resources).

#### 11 · [[Economy]] — ⬜ Not started
<small>depends on: Settlement</small>

- [ ] The resource types and how they're gathered (gatherer buildings, scavenging, scenario rewards).
- [ ] The spending sinks: building, crafting, recruiting, researching, upkeep.
- [ ] Upkeep/maintenance costs so growth carries friction.
- [ ] Anti-snowball / anti-inflation mechanics (raids, decay, caps) so an early leader can't run away.
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

#### 20 · [[Territory]] — ⬜ Not started
<small>depends on: Campaign</small>

- [ ] How territories are claimed and contested, and how control is tracked on the map.
- [ ] Supply routes between settlements — what they enable and what raiding them does.
- [ ] The bonuses each territory grants (resources, strategic edge).
- [ ] Defending held territory: raids on your settlement, who attacks and when.
- [ ] Loss conditions and how control of a territory flips hands.


### Milestone
*First public playtest gate — a thin vertical slice of #1–20.*

#### 32 · [[Final Alpha]] — 🎯 Milestone
<small>depends on: Morale, Scenarios, Settlement, Territory</small>

- [ ] 🎯 FIRST PUBLIC PLAYTEST GATE: 1 faction, 10 units, 10 buildings, 5 resources, 3 scenarios, 1 of each core system. Don't deepen anything until this slice plays.


### S4 Settlement & Campaign
*The meta-game: bases, economy, and the persistent war between battles.*

#### 22 · [[Downtime]] — ⬜ Not started
<small>depends on: Campaign, Settlement</small>

- [ ] The downtime action menu and how many actions a crew gets per cycle.
- [ ] Each action's effect: scout (intel / pick next scenario), train (XP/skills), craft (gear/tech), build (settlement), heal/recover.
- [ ] How downtime sequences against the campaign turn, plus any costs or risks.
- [ ] How solo and co-op players resolve downtime.

#### 23 · [[Events]] — ⬜ Not started
<small>depends on: Settlement, Campaign</small>

- [ ] Event triggers (start of campaign turn, during downtime, random table) and frequency.
- [ ] Settlement events (visitors, disasters, sabotage) vs world/map events.
- [ ] Effect scope: one-off boons/banes vs lasting consequences.
- [ ] How events feed the narrative and keep no two campaigns the same.

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

#### 04 · [[Factions]] — ⬜ Not started
<small>depends on: Unit Design, List Building, Settlement, Morale</small>

- [ ] A faction template: identity, unique units, signature ability, and faction-wide buffs AND nerfs.
- [ ] How each faction's special rules hook into existing systems rather than inventing new subsystems.
- [ ] Roster and unlock differences per faction.
- [ ] The starter factions (the alpha needs just 1; plan a small spread to follow).
- [ ] Asymmetry that's born from the setting/lore, not bolted on for its own sake.


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
- [ ] **🎯 Final Alpha:** [[Final Alpha]] — 1 faction, 10 units, 10 buildings, 5 resources, 3 scenarios, 1 of each core system.
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