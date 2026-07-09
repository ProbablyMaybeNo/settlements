---
type: rule-phase
phase: "19"
stage: S4 Settlement & Campaign
status: Drafted
build_order: 18
depends_on: ["Scenarios", "Settlement"]
feeds_into: ["Progression", "Territory", "Downtime", "Events", "Narrative", "Diplomacy", "Solo & Co-op"]
tags: [settlements/phase, settlements/stage/s4]
---
# 19 · Campaign
> **S4 Settlement & Campaign** · status **Drafted** · build order **18**

**Depends on:** [[Scenarios]], [[Settlement]]
**Feeds into:** [[Progression]], [[Territory]], [[Downtime]], [[Events]], [[Narrative]], [[Diplomacy]], [[Solo & Co-op]]
**Raw dependency (from Notion):** Scenarios, Settlement

## Focus
The post-battle loop that ties individual games into an ongoing war.

The Rules column should nail down:
- The campaign sequence: battle → resolve → downtime → next battle.
- What carries over between games (roster, injuries, resources, territory) and how each player tracks it solo.
- Drop-in / drop-out support so a warband always progresses whether playing one-offs, co-op, or a 2-player narrative.
- Post-battle rewards and consequences (loot, injuries, XP, reputation).
- The map/territory frame that battles are fought over (links to the Territory phase).

## Working rules / decisions

### Post-battle sequence
1. **Survival** — resolve each unit's fate (below).
2. **Advances** — survivors spend earned Advances (see [[Progression]]).
3. **Resources** — bank scenario Resources for the crew (see [[Core Game Format]], [[Economy]]).

### Survival — who is Safe
A unit is **Safe** (no roll) if, at the end of the battle, it:
- is still standing with its crew, **or**
- left the board via a friendly edge (fled / limped off), **or**
- ends in **base contact with a friendly**.

### Post-battle — the Fate table
Any unit that ends the battle **Down and alone**, or that **bled out** during it, rolls on **FATE** (`1d10`):

| d10 | Fate |
|:---:|---|
| 1 | **Dead** — removed from the roster |
| 2–3 | **Grievous injury** — a permanent stat/scar penalty |
| 4–5 | **Captured** — recover via a later scenario, else lost |
| 6–8 | **Lasting scar** — a minor permanent injury (flavour + small effect) |
| 9 | **Full recovery** — no lasting effect |
| 10 | **Hardened** — survives *and* gains a bonus (the scar that made them stronger) |

> [!question] Fate is a first-draft spread — tune once campaigns are played. Scars/injuries hook into [[Progression]] and the *every scar tells a story* tenet.

## Rule ledger
- [[adv-005 Campaign rules]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
