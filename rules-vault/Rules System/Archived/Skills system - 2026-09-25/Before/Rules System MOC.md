---
type: moc
title: Settlements — Rules System
tags: [settlements/moc]
---
# 🏚️ Settlements — Rules System

> [!success] 📕 **The source of truth is [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Full Rules System v1]]** *(adopted 2026-08-05)*
> The complete ruleset in one document — core format, combat spine, fighter construction, weapons, skills, and the settlement/campaign layer. **Where a phase note below disagrees with it, the master document wins** and that note is owed an edit. Phase notes keep the long-form reasoning; the master keeps the ruling.

Visual, editable map of the whole rules system, ported from the Notion **Build Roadmap** + **Rules** database. Open **[[_Rules Map.canvas|🗺️ the Rules Map canvas]]** to see everything at once, drag pieces around, and follow the dependency arrows.

> 🧮 **Every table in the system, side by side:** [[_Rules Tables.canvas|the Rules Tables canvas]] — 91 live-embedded tables plus the skill and condition catalogues, grouped by system, with printed points costs. Use it when designing something new to see what components already exist. Regenerate after adding a table: `py -3.13 scripts/build_rules_tables_canvas.py` in the Settlements repo.

> 🗺️ **The whole project, all eight phases:** [[SETTLEMENTS PROJECT ROADMAP]] — draft → references → testing → setting → lock → app → visuals → release. Everything in *this* note lives inside its Phase 1.
> 📋 **Start here to build it:** [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Rules System — Master Roadmap]] — the ordered, tickable checklist of every decision needed to reach a complete, book-ready rules system.
> 📖 **New to Obsidian?** [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Obsidian Guide — Building Settlements]] — a complete noob-to-fluent guide for writing the rules here (interface, links, the workflow, every plugin, your first session).
> ⌨️ **Keep this docked while you work:** [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Quick Reference — Writing Rules]] — the workflow + every key/command on one screen (right-click its tab → Move to right sidebar).
> 📚 **Every table in one place:** [[_Rules Catalogue]] — live embeds of every rules table, grouped for design review. Regenerate with `py -3.13 scripts/build_catalogue.py`.
> 🔓 **What's still open:** [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Open Decisions]] — auto-generated from unticked boxes and `status:` fields.
> 💡 **Random idea? Dump it here:** [[Ideas Inbox]] — a no-structure scratchpad; triage into rules later.
> 🔬 **What other games do:** [[Wargaming Research Hub]] — the mechanics catalogue. Every notable system or mechanic we come across, one row each, linked to a full write-up. Research only — nothing there is adopted until it lands in [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Full Rules System v1]].
> 📇 **Rules reference:** [[Weapons]] · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Basic Weapon System]] · [[Skill Paths]] — the current weapon construction and skill catalogues.
> 🧪 **Sim findings:** [[Dice Mechanic — Sim Findings]] · [[Skill Sim — Findings]] · [[Terrain Hacking Cover — Sim Findings]] · [[Crew Sim — Findings]] · [[Deployables Sim — Findings]]
> 📑 **Rules Ledger:** short *graduated* rule cards under `Rules Ledger/` — the durable one-page text (not the full phase discussion). Phase notes draft; ledger stores the clean final wording for embeds / the eventual rulebook.

**Pitch:** miniatures-agnostic skirmish wargame of brutal, ultra-realistic firefights on battlefields dense with interactive terrain; build a settlement, persist your crew, fight for your region. Full detail in [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Game Vision]].

✅ Core dice locked in draft. Lethality first pass drafted in [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Damage]] — final **Lock** after playtest.

✅ **[[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/List Building]] + [[Weapons]] drafted and sim-validated** (2026-07-13). Eight archetypes sit within an **11-point spread** — on a legal 9–12-feature board. See [[Crew Sim — Findings]]. *(Validated on the retired 100-point scale. Everything is now on the **850-Credit** scale — bodies re-derived from the measured stat ladder 2026-08-19, scale rebased 2026-08-20, propagated to every note 2026-08-27. **Match Play 850 · Campaign Start 425**, one body ladder, differing only in cap and starting skill count.)*

## Modifier design framework

[[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Modifier Design Framework]] — the six unit categories, their effect boundaries, and limited-use Equipment. Design direction recorded 2026-09-09; integration into live rules remains pending. Ledger: [[design-001 Modifier framework]].

[[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Basic Weapon System]] — the seven basic weapon classes, construction sequence, basic characteristics, and named build examples. Current weapon-system entry point from 2026-09-19; the named catalogue and Credits values remain the next content pass. Ledger: [[design-002 Basic Weapon System]].

## Stages
### S1 Foundation
- [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Game Vision]] — *Drafted*
- [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Core Game Format]] — *Drafted*
- [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Rules Engine]] — *Drafted*

### S2 Core Combat
- [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Unit Design]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Initiative & Activation]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Movement]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Shooting]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Melee]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Damage]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Conditions]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Morale]] — *Drafted*
- ✅ After [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Morale]] you have a playable combat skirmish (sandbox). Needs [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Scenarios]] for a real game.

### S3 Battle Layer
- [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Terrain]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Terrain Interaction]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Hacking]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Infrastructure]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Deployables]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/List Building]] — *Drafted* ✅ · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Scenarios]] — *Drafted*

### S4 Settlement & Campaign
- [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Settlement]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Structures]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Economy]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Campaign]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Progression]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Territory]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Downtime]] — *Drafted* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Events]] — *Drafted (battlefield only)* · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Narrative]] · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Diplomacy]] · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Solo & Co-op]]
- ✅ **The campaign layer closed on 2026-08-05.** Economy, Territory and Events were empty and are now drafted from the master note; Settlement gained its founding rules; Downtime's three-phase turn is what everything else meant by "Settlement Phase". **Diplomacy, Narrative and Solo & Co-op are the remaining gaps.**

### 🎯 Milestone
- [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Final Alpha]] — first public playtest gate (thin slice of everything above).

### S5 Content
- [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Factions]] — *Drafted* · framework **and** the six-faction roster adopted; the faction *names* are still open

### S6 Production
- [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Balance]] · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Components]] · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Rulebook]] · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Edge Cases]] · [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Playtesting]]

## Rule ledger
**Core (graduated v0.1):** [[core-000 Core Test]] · [[core-001 Movement]] · [[core-002 Shooting]] · [[core-003 Melee]] · [[core-004 Cover and line of sight]] · [[core-005 Activation order]] · [[core-006 Morale and suppression]] · [[core-007 Casualties]] · [[core-008 Victory and end of game]]

**Advanced (parking-lot):** [[adv-001 Vehicles]] · [[adv-002 Drones]] · [[adv-003 Civilians and non-combatants]] · [[adv-004 Weather and climate]] · [[adv-005 Campaign rules]]

---
*Edit phase notes in Obsidian; ledger cards are the short form for citation. Sync mirrors into the Settlements repo `rules-vault/`.*
