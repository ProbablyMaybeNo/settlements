---
type: rule
rule_id: core-006
category: core
status: draft
version: v0.3
parent_phase: "[[Morale]]"
tags: [settlements/rule, settlements/cat/core]
---
# core-006 · Morale and suppression
> **core** · status **draft** · v0.3

**Parent phase:** [[Morale]]

## Text
**Stress** tracks fear / suppression. Gain +1 when: you take a **non-wounding hit** (Pinned from ranged, Shaken from melee — the failed-Injury result), gain a negative condition, or a **friendly goes Down or Out in LOS**. A clean miss does nothing; a wounding hit wounds instead of stressing.

- **1+ Stress = Shaken:** −1 to all rolls (flat; does not deepen).
- **2+ Stress:** End Phase Break test — `1d10 + NRV − (Stress − 1)` vs **7+** (Shaken −1 does not apply here).
  - Pass → clear all Stress.
  - Fail → Nerve state by Stress, then lose 1 Stress: **2 Bolt · 3 Broken · 4+ BugOut**.
- Recovery otherwise comes from Bravery skills ([[Skill Paths]]). BugOut cannot be rallied after it starts.
- **Stress survives going Down** ([[Full Rules System v1]] §§9–11, drafted 2026-08-29, **pending playtest**). A Down unit **keeps its Stress and takes no Break tests until Stabilized** — the clock stops, the pressure does not reset. Measured in [[Stress Persistence — Sim Findings]].
- **Surplus Attack Dice hits convert to +1 Stress each** ([[core-002 Shooting]], §15, ruled 2026-08-29) — a burst wastes nothing. With persistence in force this is where a burst's suppression actually lands.

**Suppressed** (condition) = Pinned + cannot React until Pinned cleared.

*Graduated from [[Morale]] / [[Conditions]]. See [[Rules System MOC]].*
