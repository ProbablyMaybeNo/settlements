---
type: roadmap
title: Settlements Project Roadmap
tags:
  - settlements/roadmap
---
# 🗺️ Settlements — Project Roadmap

The eight phases from draft to release. For the *rules-writing* build order inside
Phase 1, see [[Rules System — Master Roadmap]]; for the rules themselves,
[[Full Rules System v1]] and the [[_Rules Catalogue]].

|Phase|Name|Description|Status|
|---|---|---|---|
|**1**|Rules System Draft|Create a draft version of the complete rules system and mechanics.|🟡 Draft complete and **pushed** (2026-08-09) — two design sessions remain: **regional map** and **capstone structures**|
|**2**|Reference Materials & Cheat Sheets|Create a series of rules PDFs, cheat sheets, and rules references that players can use to test the game.|⚪ Not started|
|**3**|Testing|Refine and optimize the rules system draft through IRL test games and an in-depth simulation pipeline.|⚪ Not started|
|**4**|The Setting|Create a complete drafted version of the Settlements setting, narrative, and lore/backstory.|⚪ Not started|
|**5**|Rules & Narrative Lock|Lock in the final Settlements rules system and mechanics, plus the game's setting and lore.|⚪ Not started|
|**6**|Companion App|Plan and build the Settlements companion app — used instead of a rulebook, covering list building, crew management, settlement management, the regional map, campaign setup/tracking, and a rules reference tool.|⚪ Not started|
|**7**|Companion App Visuals|Create visuals for the companion app — brand colors, fonts, style, tone, icons/symbols, tables, map system, territories, and how-to graphs/charts.|⚪ Not started|
|**8**|Settlements Release|—|⚪ Not started|

---

_Status legend: ⚪ Not started · 🟡 In progress · 🟢 Complete_

## Where Phase 1 actually stands

**27 of 37** rule-phase notes are Drafted. The remaining gaps, from the vault:

- **Not started in S4:** [[Diplomacy]] · [[Narrative]] *(overlaps Phase 4)* · [[Solo & Co-op]]
- **Not started in S6:** [[Balance]] · [[Components]] · [[Rulebook]] · [[Edge Cases]] · [[Playtesting]] — these are Phase 2/3 work, not Phase 1
- **Your two named sessions:** the **regional map** extends [[Territory]] (the card and control states exist; the *map* — how territories connect, supply routes, who can attack whom — does not). **Capstone structures** would be new top-tier entries beyond the 23-structure catalogue in [[Structures]].
- **Decisions waiting on you:** the ten unticked recommendations in `docs/SETTLEMENTS-WHOLE-SYSTEM-AUDIT.md`, and the faction *names* in [[Factions]].

## Phase 3 already has a head start

The simulation pipeline exists rather than being a blank: `test-bench/engine2d/` is a
headless 2.5D engine that plays whole games at **~1,000/sec** (measured), plus
subsystem sims in `test-bench/balance/` and a costing engine in `test-bench/points/`.
Roughly **6 million games** have been run against the current rules.

What it still needs, and what a Phase 3 plan should carry:
1. **IRL table games** — every number so far is sim-derived, not table-derived.
2. **A fidelity check on the sim's geometry.** `engine2d` approximates line of sight
   with boxes; Tabletop Simulator can raycast real meshes at ~45,000/sec. Nobody has
   verified the approximation, and terrain density is the game's biggest balance dial
   (a measured 66-point swing), so a systematic error there would taint every terrain
   finding.
3. **The two items the audit deferred:** the FIX 4 Annihilate skew (WND 3 dominates
   pure-kill missions) and FIX 5 Dodge, which the engine AI cannot currently stress.

---
*See [[Rules System MOC]] for the rules index.*