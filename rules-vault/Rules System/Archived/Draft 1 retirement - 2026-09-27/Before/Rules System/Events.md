---
type: rule-phase
phase: "23"
stage: S4 Settlement & Campaign
status: Drafted
build_order: 23
depends_on: ["Settlement", "Campaign"]
feeds_into: []
tags: [settlements/phase, settlements/stage/s4]
---
# 23 · Events
> **S4 Settlement & Campaign** · status **Drafted** · build order **23**

**Depends on:** [[Settlement]], [[Campaign]]
**Feeds into:** —
**Raw dependency (from Notion):** Settlement, Campaign

## Focus
Settlement and world events that inject variety and emergence into the campaign.

The Rules column should nail down:
- Event triggers (start of campaign turn, during downtime, random table) and frequency.
- Settlement events (visitors, disasters, sabotage) vs world/map events.
- Effect scope: one-off boons/banes vs lasting consequences.
- How events feed the narrative and keep no two campaigns the same.

## Working rules / decisions

*Drafted 2026-08-05 from [[Full Rules System v1]] §27. What exists in v1 is the **battlefield** event table; settlement- and map-scale events are still open (below).*

### Battlefield Events — exactly two rolls, no running clock

Roll **1d10** twice per battle: at the **start of Round 1**, and at the **start of the midpoint round**. That is the whole schedule — there is no per-round event roll and no escalating clock, because a running event track competes with the scenario for the players' attention and turns every round into table-lookup.

| d10 | Event | Effect |
|:--:|---|---|
| 1 | **Clear skies** | No effect |
| 2 | **Rain rolls in** | Ranged range **−3"**; **Hide** test **+1** |
| 3 | **Trader's caravan** | Place a neutral **Trader** marker; a unit in base contact may buy one item |
| 4 | **Pack on the move** | A neutral hostile token attacks the nearest model within **12"** |
| 5 | **Power flicker** | Powered terrain within **12"** of centre is **Disabled** this round ([[Infrastructure]]) |
| 6 | **Distant gunfire** | Every model within **12"** of centre gains **1 Stress** ([[Morale]]) |
| 7 | **Scavenger's luck** | An extra loot token appears at an unclaimed **Side Objective** ([[Territory]]) |
| 8 | **Structural failure** | One Building piece within **12"** of centre becomes **Difficult** ground ([[Terrain]]) |
| 9 | **Radio chatter** | Both players may reroll one failed **Spot** this round |
| 10 | **All quiet** | No effect |

^tbl-battlefield-events

**Two of the ten entries do nothing on purpose.** A 20% chance of "the world stays out of it" is what keeps the table feeling like weather rather than a second scenario.

Events are layered by [[Territory|territory cards]], which may add location-specific entries over the standard table — a subway territory rolling *Power flicker* differently to an open lot.

> [!info] Events vs the Twist — different jobs, don't merge them
> The **Twist** ([[Scenarios#The Twist (roll 1d6 at setup)]]) is rolled **once at setup** and changes the whole game's shape before a die is thrown, so both players can plan around it. An **Event** fires mid-battle and is something you *react* to. One is a condition of the fight; the other is an interruption. Keeping them separate is why neither needs to be gentle.

## Open dials
- [ ] **First-draft table, 10 entries** — expand toward **15–20** once the rhythm is confirmed at the table.
- [ ] **Settlement events are not drafted** — visitors, disasters, sabotage-from-off-table. §27 covers the battlefield only ([[Settlement]]).
- [ ] **Map/world events are not drafted** — anything that fires in the Settlement Phase rather than during a battle ([[Downtime]]).
- [ ] Whether any event should carry a **lasting** consequence past the battle, or whether all of them stay one-off.
- [ ] The **midpoint round** on a 6-round game is Round 3 or 4 — pick one and print it.

## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
