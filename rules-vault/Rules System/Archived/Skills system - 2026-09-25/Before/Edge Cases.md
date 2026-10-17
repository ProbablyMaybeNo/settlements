---
type: rule-phase
phase: "31"
stage: S6 Production
status: Not Started
build_order: 31
depends_on: ["Movement", "Terrain", "Morale"]
feeds_into: []
tags: [settlements/phase, settlements/stage/s6]
---
# 31 · Edge Cases
> **S6 Production** · status **Not Started** · build order **31**

**Depends on:** [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Movement]], [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Terrain]], [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Morale]]
**Feeds into:** —
**Raw dependency (from Notion):** Movement, Terrain, full combat loop (all rules drafted)

## Focus
Audit the nasty interactions (movement / terrain / combat) before locking a Release Candidate.

The Rules column should nail down:
- A systematic audit of system pairs that collide (forced movement + falling + collapsing terrain; suppression + morale; etc.).
- Priority rulings for ambiguous stacks of rules.
- A FAQ/errata list seeded from playtest breakages.
- A stress-test of the realism mechanics that intentionally create emergent chaos, so they break in fun ways, not broken ways.

## Working rules / decisions
_Not drafted yet._

## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Settlements/Rules System/Archived/Skills system - 2026-09-25/Before/Rules System MOC]] and [[_Rules Map.canvas|the map]]._
