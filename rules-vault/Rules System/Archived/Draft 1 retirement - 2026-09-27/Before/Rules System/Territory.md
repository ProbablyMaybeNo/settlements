---
type: rule-phase
phase: "20"
stage: S4 Settlement & Campaign
status: Drafted
build_order: 20
depends_on: ["Campaign"]
feeds_into: ["Final Alpha"]
tags: [settlements/phase, settlements/stage/s4]
---
# 20 · Territory
> **S4 Settlement & Campaign** · status **Drafted** · build order **20**

**Depends on:** [[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Campaign]]
**Feeds into:** [[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Final Alpha]]
**Raw dependency (from Notion):** Campaign

## Focus
Controlling the campaign map — acquisition, bonuses, and defence.

The Rules column should nail down:
- How territories are claimed and contested, and how control is tracked on the map.
- Supply routes between settlements — what they enable and what raiding them does.
- The bonuses each territory grants (resources, strategic edge).
- Defending held territory: raids on your settlement, who attacks and when.
- Loss conditions and how control of a territory flips hands.

## Working rules / decisions

*Drafted 2026-08-05 from [[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Full Rules System v1]] §23. The **territory card** is the unit of content here — a territory is not a hex with a bonus printed on it, it is a bundle of a board, a scenario, a loot profile and a reason to go there.*

### The territory card — eleven required fields
Every territory ships as one card. A card missing any of these fields is not finished:

| # | Field | What it carries |
|:--:|---|---|
| 1 | **Terrain recipe** | What fills the density squares — still inside the sacred **9–12** band ([[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Terrain#Setup procedure]]) |
| 2 | **Scenario weighting** | Which of the five shapes this place tends to produce ([[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Scenarios]]) |
| 3 | **Side Objective(s)** | The optional secondary goal, revealed or hidden |
| 4 | **Infrastructure** | Which operable features are bolted into this board ([[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Infrastructure]]) |
| 5 | **Events** | Any location-specific entries layered over the standard table ([[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Events]]) |
| 6 | **Loot table** | The default table below, or this card's overrides |
| 7 | **Control benefit** | **Access, never power** — what holding it lets you *do* |
| 8 | **Supply requirement** | What it costs to keep held |
| 9 | **Control state** | Claimed · Controlled · Isolated (below) |
| 10 | **Adjacent territories** | The map graph — what it borders, and therefore what can cut it off |
| 11 | **Raid profile** | How a raid on this territory is laid out and fought |

^tbl-the-territory-card

> [!important] A control benefit grants **access**, never power
> This is [[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Game Vision|the first tenet]] applied to the map: holding ground widens what a crew can *choose to do*, and never makes a fighter flatly stronger for standing somewhere. A territory printing "+1 DEX to your crew" would be an unpriced power grant and does not belong on a card.

Each card also carries **1–5 Territory Deeds** — Glorious Deeds themed to that location, on top of the ten standard ones ([[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Campaign#Glorious Deeds]]).

### The default loot table

Every territory needs a Loot table. **This is the base table** any territory uses unless its own card overrides specific entries to fit its flavour — an industrial territory might swap found jewellery for found tools.

It is also what [[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Terrain Interaction#Searching and looting|Search]] rolls on for its *Supply cache* and *Gear* results, what the **Raid** scenario draws for loot ([[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Scenarios]]), and what a **Scavenge** dispatch rolls ([[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Downtime]]).

Roll **1d10** whenever a Search, Raid loot or Scavenge action calls for it:

| d10 | Result |
|:--:|---|
| 1 | Nothing usable — spoiled, broken, or already picked clean |
| 2 | **+5 Credits** |
| 3 | **+10 Materials** |
| 4 | **+10 Credits** |
| 5 | A basic **Light Melee or Sidearm** weapon, unbuilt — the player picks the class, no characteristics ([[Weapons]]) |
| 6 | **+15 Materials** |
| 7 | **+15 Credits** |
| 8 | **+20 Credits** |
| 9 | One piece of **equipment** — Med-Kit, Breach Kit, or a basic Trap/Mine, player's choice ([[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/List Building]] · [[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Deployables]]) |
| 10 | **Jackpot** — roll twice more on this table, ignoring further 10s |

^tbl-the-default-loot-table

Small, fast and deliberately low-stakes. The job is to make searching worth doing **even when a battle is going badly** — not to be a second economy.

> [!warning] First-draft values, and deliberately not tuned yet
> These numbers have **not** been checked against the economy-sink problem flagged in [[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Economy#Open — the economy sink]], and probably shouldn't be tuned until that is addressed. Loot is one of the few natural places to route a sink fix through if the economy needs one, so tuning it first would mean tuning it twice.

### Control states

A territory moves through three states:

| State | Reached by | Benefit |
|---|---|:--:|
| **Claimed** | Winning a battle fought there | **None yet** — you hold the ground, not the output |
| **Controlled** | Assigning a worker, or paying Materials | **Active** |
| **Isolated** | An enemy holds an adjacent territory and cuts it off | **Suspended** until the link is restored |

^tbl-control-states

**Claimed is not Controlled.** Winning the battle is the easy half; a territory only starts paying once you spend something to hold it, which is what makes a wide, thin empire a real risk rather than a free win.

## Open dials
- [ ] **Territory terrain-type → pre-built terrain list mapping** — each card's terrain recipe needs to resolve to pieces a player actually owns ([[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Terrain]], [[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Components]]).
- [ ] **Loot markers vs the 9–12 density budget** — confirm loot markers count **separately** from large features, so a loot-heavy territory doesn't quietly blow the band ([[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Terrain#Setup procedure]]).
- [ ] **Supply requirement** — what a territory costs per cycle to stay Controlled ([[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Economy]]).
- [ ] How many territories a campaign map carries, and whether **Isolated** can chain.
- [ ] A worked example of objective-completion → a specific settlement benefit.

## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Settlements/Rules System/Archived/Draft 1 retirement - 2026-09-27/Before/Rules System/Rules System MOC]] and [[_Rules Map.canvas|the map]]._
