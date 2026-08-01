---
type: rule-phase
phase: "28"
stage: S6 Production
status: Not Started
build_order: 29
depends_on: ["Structures"]
feeds_into: []
tags: [settlements/phase, settlements/stage/s6]
---
# 28 · Components
> **S6 Production** · status **Not Started** · build order **29**

**Depends on:** —
**Feeds into:** —
**Raw dependency (from Notion):** All combat + campaign systems locked

## Focus
The physical bits — tokens, cards, and sheets — designed once the rules are locked.

The Rules column should nail down:
- The full component list: tokens (conditions, objectives, wounds), cards (units, scenarios, events), sheets (roster, settlement map).
- What each component must display, in a print- and DIY-friendly format.
- The settlement-map sheet players use to build their boards.
- A rule of thumb: don't finalise any component until the system it represents is locked.

## Working rules / decisions

### The settlement sheet
The one component the settlement layer cannot ship without.

- A **12 × 36 grid of 1" squares** — 432 squares, one page. Groundworks II needs an 18 × 48 version.
- It is the **mechanical source of truth**: every placed structure's footprint, Power draw and one-line terrain profile is read off the sheet at setup, not measured off the models ([[Structures#On terrain sizes]] · [[Board Representation#Settlement structures]]).
- Also carries: the Power sum (output vs draw), the four resource tracks, roster/housing count, and the Functional/Disabled flag per structure.

### Structure tiles
Every entry in [[Structures]] ships as a **print-and-cut tile at its exact grid footprint**. This is the reference implementation and it must stay complete — a player with no scenery at all builds a full settlement from the printed sheet, which is what keeps the **no-collection-to-win** tenet honest.

- [ ] Tile art for all 25 entries + the three Station→Building upgrade forms
- [ ] Who authors the art
- [ ] Token set for the interactive points: door, terminal, hatch, ladder, hardpoint, **Disabled**

> [!warning] Don't finalise ahead of [[Economy]]
> Tiles can be drawn now — footprints are settled. **Costs cannot**: nothing in [[Structures]] is priced until the Credits/Materials inflow rates exist.

## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
