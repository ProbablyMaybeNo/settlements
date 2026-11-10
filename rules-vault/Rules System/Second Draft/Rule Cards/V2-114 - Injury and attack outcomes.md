---
type: settlements-rule-card
rule_id: V2-114
rule_name: Injury and attack outcomes
entry_type: Rule
category: Casualties
book_chapter: 4
book_section: Fighting Battles
book_subsection: Injuries and Resolving Combat
tags:
- settlements/v2
- combat
- injury
- stress
- pinned
- limits
summary: 'Each hit adds 1 Stress; surviving a Wound causes Pinned; zero Wounds causes Down. Wound limits: 3, or
  4 for leaders.'
status: Drafted
review_status: Unreviewed
publication: Included
created: '2026-10-18'
source:
- '[[Archive/Settlements/2026-10-25 - Rule card consolidation/Rule Cards/V2-114 - Injury roll]]'
- '[[Archive/Settlements/2026-10-25 - Rule card consolidation/Rule Cards/V2-115 - Injury outcomes]]'
- '[[Archive/Settlements/2026-10-25 - Rule card consolidation/Rule Cards/V2-116 - Attack-pool casualties]]'
review_notes: ''
related_rules:
- '[[Settlements/Rules System/Second Draft/Rule Cards/V2-114 - Injury and attack outcomes|Injury outcomes]]'
planned_section: 04 · Fighting Battles
rule_parent: Injuries and Resolving Combat
consolidated: '2026-10-25'
legacy_rule_ids:
- V2-114
- V2-115
- V2-116
component_rules:
- rule_id: V2-114
  rule_name: Injury roll
  status: Drafted
  last_rule_update: '2026-11-10'
  review_status: Unreviewed
  review_notes: ''
- rule_id: V2-115
  rule_name: Injury outcomes
  status: Drafted
  last_rule_update: '2026-11-10'
  review_status: Unreviewed
  review_notes: ''
- rule_id: V2-116
  rule_name: Attack-pool casualties
  status: Drafted
  last_rule_update: '2026-11-10'
  review_status: Unreviewed
  review_notes: ''
last_rule_update: '2026-11-10'
---

# Injury and attack outcomes

## Summary

Each hit adds 1 Stress; surviving a Wound causes Pinned; zero Wounds causes Down. Wound limits: 3, or 4 for leaders.

## Rule text

### Injury roll

Each successful hit adds 1 Stress. For each hit, roll **1d20 + Damage − Armour + Injury modifiers vs 13+**. Natural 1 fails; natural 20 succeeds. Stress does not affect Injury.

^text-s035-b000

### Injury outcomes

Each successful Injury roll removes 1 Wound. A unit that loses a Wound becomes **Pinned** if it has Wounds remaining, or **Down** at zero. A hit that causes no Wound adds Stress only, unless another rule says otherwise. Resolve the attack’s Injury dice together; they add no further Stress or extra lasting-injury rolls.

^text-s035-b001

Units normally start with 1 Wound. Maximum Wounds are 3, or 4 for a crew leader. Skills such as Tough can increase Wounds within those limits.

^text-s035-b002

## Links

- [[Settlements/Rules System/Second Draft/Rule Cards - Complete Index|Rule index]]

<!-- conditions-reference:start -->
## Conditions referenced

[[Settlements/Rules System/Second Draft/Conditions Reference#^condition-pinned|Pinned]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-down|Down]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-stress|Stress]]
<!-- conditions-reference:end -->

## Design notes

Consolidated without changing rule meaning on 2026-10-25. Original per-rule statuses, dates and feedback are retained in `component_rules` and the dated source snapshot.

### Ross’s clarification — 2026-11-10

Hits alone do not Pin. Keep +1 Stress per successful hit for now; per-hit versus per-attack Stress is reserved for simulation testing. Wound ceilings are 3, or 4 for leaders.
