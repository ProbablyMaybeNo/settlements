---
type: roadmap
title: Settlements — Rules System Master Roadmap
tags: [settlements/roadmap]
---
# 🗺️ Settlements — Rules System Master Roadmap

Everything needed to take Settlements from *scaffold* to a *complete, book-ready rules system*, in dependency order. Checkboxes are live — tick them as you lock each decision; the Tasks plugin can roll them up. See also [[Rules System MOC]] and [[_Rules Map.canvas|the map]].

## 1 · Where it stands today

**32 phases total** — ✅ 14 drafted · 🟡 1 designing · 🎯 1 milestone · ⬜ 16 not started. *(+ [[Weapons]] & [[Skill Paths]] reference notes.)*

| Stage | Phases | Status |
|---|---|---|
| **S1 Foundation** | 3 | ✅ Drafted |
| **S2 Core Combat** | 8 | 🟡 Drafting (7 drafted, Unit Design designing) |
| **S3 Battle Layer** | 4 | 🟡 Started (Terrain, List Building drafted) |
| **S4 Settlement & Campaign** | 10 | 🟡 Started (Campaign, Progression drafted) |
| **Milestone** | 1 | Milestone |
| **S5 Content** | 1 | Not Started |
| **S6 Production** | 5 | Not Started |

## 2 · The decisions that unblock everything

These two gate the entire combat engine. **Lock them first — nothing in S2 can be finalised until they are.**

- [x] **Core dice mechanic** ([[Rules Engine]]) — *the* resolution every other system reuses. ✅ Drafted: 1d10 + Stat + mods, 7+, nat 1/10 auto.
- [ ] **Lethality dial** ([[Damage]]) — how deadly combat is and whether rosters persist between games (Tenet 3). Set deliberately before locking combat.

Secondary opens to resolve as you reach them: 6-turn length vs objective soft-cap ([[Core Game Format]]), base-size→rules brackets ([[Terrain]]), costing method ([[List Building]] / [[Balance]]).

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

#### 06 · [[Unit Design]] — ⬜ Not started
<small>depends on: Rules Engine</small>

- [ ] Each stat and exactly what it governs: Wounds, Move, Strength, Dexterity, Intelligence, Mental, Morale.
- [ ] Elite units (unique, player-built statline) vs non-elite (shared statline by type), and how leader/elite picks unlock which non-elites you can field.
- [ ] The data-card layout: stats + skills/abilities + equipment + narrative/identity.
- [ ] How weapons & armour attach (separate profiles vs baked into the unit) — decide this here, it drives Shooting/Melee/Damage.
- [ ] Baseline human numbers to anchor the whole game; how champions/leaders/veterans scale above baseline.

#### 12 · [[Initiative & Activation]] — ⬜ Not started
<small>depends on: Rules Engine</small>

- [ ] The activation model: alternating activation; ~2 activations per unit; leaders/champions sometimes more.
- [ ] How initiative is rolled and applied each turn, including the underdog edge.
- [ ] Action-economy detail: what a single activation lets a unit do (move + one action? two actions?).
- [ ] Out-of-activation rules: reactions, overwatch, interrupts — or explicitly none, to keep it clean.
- [ ] A catch-up / rubber-band rule so a larger crew can't simply burn through your activations and then dogpile.

#### 07 · [[Movement]] — ⬜ Not started
<small>depends on: Unit Design</small>

- [ ] Base move (from the Move stat) plus run/charge/advance variants and their costs/trade-offs.
- [ ] Vertical movement: climbing, jumping gaps, falling and fall damage (driven by Dexterity).
- [ ] Moving through/over terrain: difficult ground, obstacles, squeezing through gaps.
- [ ] Movement around engagement: disengaging, falling back, and what (if anything) it provokes.
- [ ] Forced movement (push / knockback / drag) and how it interacts with terrain edges and falling.
- [ ] Measuring rules: pre-measuring allowed? base-to-base? — must agree with the Rules Engine conventions.

#### 13 · [[Shooting]] — ⬜ Not started
<small>depends on: Unit Design, Movement</small>

- [ ] The step-by-step ranged sequence: declare → check LOS/range → to-hit → saves → damage.
- [ ] Which stat drives ranged to-hit (Dexterity) and the target-number method.
- [ ] The ranged-weapon profile fields: range (or bands), attacks, strength/AP, damage, traits.
- [ ] Target-priority rules (closest visible? cover interplay) — a key lever for the terrain pillar.
- [ ] Modifiers: cover, range, moving vs stationary, elevation, suppression.
- [ ] Realism touches if wanted: ammo, reload, misfire/jam — kept streamlined to one die where possible.

#### 14 · [[Melee]] — ⬜ Not started
<small>depends on: Unit Design, Movement</small>

- [ ] What counts as "engaged" (range), and how combats start (charge vs being in reach).
- [ ] The melee sequence: who strikes first (Initiative / charging), simultaneous vs alternating blows.
- [ ] Which stat drives melee (Strength) and any defence/parry interplay.
- [ ] Positional modifiers: charging, flank/rear, outnumbering, high ground, terrain.
- [ ] The melee-weapon profile fields and how they differ from ranged weapons.
- [ ] How the result feeds into the shared Damage sequence (don't duplicate damage logic here).

#### 15 · [[Damage]] — ⬜ Not started
<small>depends on: Shooting, Melee</small>

- [ ] How a hit converts to a wound: armour/save roll, AP/rend modifier, then wounds dealt.
- [ ] The wound model: most units have 1 wound (down on a successful hit); multi-wound leaders/champions.
- [ ] Down/injury states in-battle: knocked down, out of action, bleeding out.
- [ ] Criticals: what triggers one and what it does (extra damage / roll on an injury table).
- [ ] The armour profile and how it modifies the save.
- [ ] The hook into the persistent roster: post-battle survival vs death vs lasting injury (brutal-realism pillar).

#### 16 · [[Conditions]] — ⬜ Not started
<small>depends on: Damage</small>

- [ ] The full condition list and what each one does mechanically.
- [ ] How conditions are applied, tracked (tokens), and removed/expire.
- [ ] Stacking rules and how conditions interact with each other.
- [ ] Which sources cause which conditions (weapons, terrain hazards, psychic/Mental).
- [ ] Realism-flavoured states tied to the setting (suppressed, bleeding, panicked) that reinforce the gritty tone.

#### 17 · [[Morale]] — ⬜ Not started
<small>depends on: Damage</small>

- [ ] Morale / Fear / Insanity tests: what triggers them, the stat used (Morale), and target numbers.
- [ ] Bottling: when a crew tests to flee the field — design it to be the NORM, not the exception.
- [ ] Individual vs crew-wide effects (a single fighter pinned/fleeing vs the whole crew bottling).
- [ ] Insanity and Fear mechanics and how they alter behaviour and tie back to the initiative phase.
- [ ] Recovery / rally rules and how leaders steady nearby fighters.


### S3 Battle Layer
*The board comes alive — terrain (the core pillar), list-building, and scenarios.*

#### 08 · [[Terrain]] — ⬜ Not started
<small>depends on: Movement</small>

- [ ] A terrain category system (light/heavy/impassable, cover levels) that classifies ANY piece a player owns — DIY, 3D-printed, or bought.
- [ ] Cover and line-of-sight rules: full vs partial cover, obscuring, how blocking is judged.
- [ ] Hazard terrain (fire, water, rubble, height) and its effects on units.
- [ ] Verticality/elevation: ranged and melee benefits of height, plus fall risk.
- [ ] A setup procedure so mixed terrain collections all plug into the same rules.
- [ ] The interactive-terrain hooks that deliver the headline promise: no two battles the same.

#### 09 · [[Terrain Interaction]] — ✅ Drafted
<small>depends on: Terrain</small>

- [x] Interaction actions: opening/breaking doors, Lift (not barricade), climbing, operating objects — gated by STR / DEX / INT / AGI.
- [x] Searching and looting terrain: what's found, the rolls, and who can search.
- [x] Structural integrity: out of scope for launch; feature damage (turrets/terminals/etc.) instead.
- [x] In-battle repair of features; settlement upgrades as board state.
- [x] Traps and deployable defences: how they're placed, triggered, and disarmed.

#### 33 · [[Hacking]] — ✅ Drafted
<small>depends on: Terrain, Terrain Interaction, Rules Engine</small>

- [x] Terminal Interact sequence (declare → range → INT 7+ or opposed).
- [x] Range bands as modifiers (0 / −1 / −2 / −3), max 24".
- [x] Linked functions menu; turrets controlled-only.
- [x] Hacker-vs-hacker shut-outs: opposed INT → Effect roll → Shut-out table.
- [ ] Playtest dials: Take Over frequency, Overload lethality, Shut down duration.

#### 05 · [[List Building]] — ⬜ Not started
<small>depends on: Unit Design</small>

- [ ] Roster structure: 1 leader + elite fighters + the non-elites those choices unlock; min/max crew size.
- [ ] The costing method (points? threat rating? scenario-defined?) and what gets costed (units, weapons, gear).
- [ ] Faction selection at list level and how each faction's buffs AND nerfs apply.
- [ ] How a persistent campaign roster differs from a one-off pickup list.
- [ ] Restrictions/keywords that keep lists legal and on-theme.

#### 18 · [[Scenarios]] — ⬜ Not started
<small>depends on: Damage, Morale, Terrain</small>

- [ ] A scenario template (setup, deployment, objectives, twist, victory conditions, length).
- [ ] A starter suite featuring the campaign battles named in the vision: Caravan Escort, Settlement Raid, Kidnapping, Sabotage.
- [ ] Asymmetric attacker/defender setups — the settlement defender fights on the board they actually built.
- [ ] Win conditions beyond kills, how/when a game ends, and how bottling interacts.
- [ ] A variability/twist mechanic so each scenario replays differently.


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

#### 19 · [[Campaign]] — ⬜ Not started
<small>depends on: Scenarios, Settlement</small>

- [ ] The campaign sequence: battle → resolve → downtime → next battle.
- [ ] What carries over between games (roster, injuries, resources, territory) and how each player tracks it solo.
- [ ] Drop-in / drop-out support so a warband always progresses whether playing one-offs, co-op, or a 2-player narrative.
- [ ] Post-battle rewards and consequences (loot, injuries, XP, reputation).
- [ ] The map/territory frame that battles are fought over (links to the Territory phase).

#### 21 · [[Progression]] — ⬜ Not started
<small>depends on: Campaign</small>

- [ ] XP sources and how units earn and spend it.
- [ ] Advancement tables: new skills, stat increases, unlocked equipment.
- [ ] The injury / permanent-scar system: debilitating injuries, death, and survivors becoming powerful veterans.
- [ ] How leader/elite progression differs from non-elite.
- [ ] Grudges, bonds, and character traits that build the narrative attachment the vision promises.

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