---
type: moc
title: Settlements — Rules System
tags: [settlements/moc]
---
# 🏚️ Settlements — Rules System

> [!success] 📕 **The source of truth is [[Full Rules System v1]]** *(adopted 2026-08-05)*
> The complete ruleset in one document — core format, combat spine, fighter construction, weapons, skills, and the settlement/campaign layer. **Where a phase note below disagrees with it, the master document wins** and that note is owed an edit. Phase notes keep the long-form reasoning; the master keeps the ruling.

Visual, editable map of the whole rules system, ported from the Notion **Build Roadmap** + **Rules** database. Open **[[_Rules Map.canvas|🗺️ the Rules Map canvas]]** to see everything at once, drag pieces around, and follow the dependency arrows.

> 🧮 **Every table in the system, side by side:** [[_Rules Tables.canvas|the Rules Tables canvas]] — 91 live-embedded tables plus the skill and condition catalogues, grouped by system, with printed points costs. Use it when designing something new to see what components already exist. Regenerate after adding a table: `py -3.13 scripts/build_rules_tables_canvas.py` in the Settlements repo.

> 🗺️ **The whole project, all eight phases:** [[SETTLEMENTS PROJECT ROADMAP]] — draft → references → testing → setting → lock → app → visuals → release. Everything in *this* note lives inside its Phase 1.
> 📋 **Start here to build it:** [[Rules System — Master Roadmap]] — the ordered, tickable checklist of every decision needed to reach a complete, book-ready rules system.
> 📖 **New to Obsidian?** [[Obsidian Guide — Building Settlements]] — a complete noob-to-fluent guide for writing the rules here (interface, links, the workflow, every plugin, your first session).
> ⌨️ **Keep this docked while you work:** [[Quick Reference — Writing Rules]] — the workflow + every key/command on one screen (right-click its tab → Move to right sidebar).
> 📚 **Every table in one place:** [[_Rules Catalogue]] — live embeds of every rules table, grouped for design review. Regenerate with `py -3.13 scripts/build_catalogue.py`.
> 🔓 **What's still open:** [[Open Decisions]] — auto-generated from unticked boxes and `status:` fields.
> 💡 **Random idea? Dump it here:** [[Ideas Inbox]] — a no-structure scratchpad; triage into rules later.
> 🔬 **What other games do:** [[Wargaming Research Hub]] — the mechanics catalogue. Every notable system or mechanic we come across, one row each, linked to a full write-up. Research only — nothing there is adopted until it lands in [[Full Rules System v1]].
> 📇 **Rules reference:** [[Weapons]] · [[Skill Paths]] — catalogues the combat notes point to.
> 🧪 **Sim findings:** [[Dice Mechanic — Sim Findings]] · [[Skill Sim — Findings]] · [[Terrain Hacking Cover — Sim Findings]] · [[Crew Sim — Findings]] · [[Deployables Sim — Findings]]
> 📑 **Rules Ledger:** short *graduated* rule cards under `Rules Ledger/` — the durable one-page text (not the full phase discussion). Phase notes draft; ledger stores the clean final wording for embeds / the eventual rulebook.

**Pitch:** miniatures-agnostic skirmish wargame of brutal, ultra-realistic firefights on battlefields dense with interactive terrain; build a settlement, persist your crew, fight for your region. Full detail in [[Game Vision]].

✅ Core dice locked in draft. Lethality first pass drafted in [[Damage]] — final **Lock** after playtest.

✅ **[[List Building]] + [[Weapons]] drafted and sim-validated** (2026-07-13). Eight archetypes sit within an **11-point spread** — on a legal 9–12-feature board. See [[Crew Sim — Findings]]. *(Validated on the retired 100-point scale; everything is on the **1000-Credit** scale as of 2026-08-05, with separate **Match Play** and **Campaign Start** starting tiers.)*

## Stages
### S1 Foundation
- [[Game Vision]] — *Drafted*
- [[Core Game Format]] — *Drafted*
- [[Rules Engine]] — *Drafted*

### S2 Core Combat
- [[Unit Design]] — *Drafted* · [[Initiative & Activation]] — *Drafted* · [[Movement]] — *Drafted* · [[Shooting]] — *Drafted* · [[Melee]] — *Drafted* · [[Damage]] — *Drafted* · [[Conditions]] — *Drafted* · [[Morale]] — *Drafted*
- ✅ After [[Morale]] you have a playable combat skirmish (sandbox). Needs [[Scenarios]] for a real game.

### S3 Battle Layer
- [[Terrain]] — *Drafted* · [[Terrain Interaction]] — *Drafted* · [[Hacking]] — *Drafted* · [[Infrastructure]] — *Drafted* · [[Deployables]] — *Drafted* · [[List Building]] — *Drafted* ✅ · [[Scenarios]] — *Drafted*

### S4 Settlement & Campaign
- [[Settlement]] — *Drafted* · [[Structures]] — *Drafted* · [[Economy]] — *Drafted* · [[Campaign]] — *Drafted* · [[Progression]] — *Drafted* · [[Territory]] — *Drafted* · [[Downtime]] — *Drafted* · [[Events]] — *Drafted (battlefield only)* · [[Narrative]] · [[Diplomacy]] · [[Solo & Co-op]]
- ✅ **The campaign layer closed on 2026-08-05.** Economy, Territory and Events were empty and are now drafted from the master note; Settlement gained its founding rules; Downtime's three-phase turn is what everything else meant by "Settlement Phase". **Diplomacy, Narrative and Solo & Co-op are the remaining gaps.**

### 🎯 Milestone
- [[Final Alpha]] — first public playtest gate (thin slice of everything above).

### S5 Content
- [[Factions]] — *Drafted* · framework **and** the six-faction roster adopted; the faction *names* are still open

### S6 Production
- [[Balance]] · [[Components]] · [[Rulebook]] · [[Edge Cases]] · [[Playtesting]]

## Rule ledger
**Core (graduated v0.1):** [[core-000 Core Test]] · [[core-001 Movement]] · [[core-002 Shooting]] · [[core-003 Melee]] · [[core-004 Cover and line of sight]] · [[core-005 Activation order]] · [[core-006 Morale and suppression]] · [[core-007 Casualties]] · [[core-008 Victory and end of game]]

**Advanced (parking-lot):** [[adv-001 Vehicles]] · [[adv-002 Drones]] · [[adv-003 Civilians and non-combatants]] · [[adv-004 Weather and climate]] · [[adv-005 Campaign rules]]

---
*Edit phase notes in Obsidian; ledger cards are the short form for citation. Sync mirrors into the Settlements repo `rules-vault/`.*
