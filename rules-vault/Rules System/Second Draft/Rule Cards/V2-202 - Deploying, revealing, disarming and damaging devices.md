---
type: settlements-rule-card
rule_id: V2-202
rule_name: Deploying, revealing, disarming and damaging devices
entry_type: Rule
category: Devices
book_chapter: 4
book_section: Fighting Battles
book_subsection: Deployables and Drones
tags:
- settlements/v2
- device
- core
- timing
- stealth
- inventory
- combat
- mine
- drone
summary: Deploy equipment; Device arming delay; Concealed devices; Disarm; Recover device; Device damage; Device
  targeting; Friendly mine triggers
status: Drafted
review_status: Unreviewed
publication: Included
created: '2026-10-18'
source:
- '[[Archive/Settlements/2026-10-25 - Rule card consolidation/Rule Cards/V2-202 - Deploy equipment]]'
- '[[Archive/Settlements/2026-10-25 - Rule card consolidation/Rule Cards/V2-203 - Device arming delay]]'
- '[[Archive/Settlements/2026-10-25 - Rule card consolidation/Rule Cards/V2-204 - Concealed devices]]'
- '[[Archive/Settlements/2026-10-25 - Rule card consolidation/Rule Cards/V2-205 - Disarm]]'
- '[[Archive/Settlements/2026-10-25 - Rule card consolidation/Rule Cards/V2-206 - Recover device]]'
- '[[Archive/Settlements/2026-10-25 - Rule card consolidation/Rule Cards/V2-207 - Device damage]]'
- '[[Archive/Settlements/2026-10-25 - Rule card consolidation/Rule Cards/V2-208 - Device targeting]]'
- '[[Archive/Settlements/2026-10-25 - Rule card consolidation/Rule Cards/V2-217 - Friendly mine triggers]]'
review_notes: ''
action_cost: Core
related_rules:
- '[[Settlements/Rules System/Second Draft/Rule Cards/V2-202 - Deploying, revealing, disarming and damaging devices|Device arming delay]]'
planned_section: 04 · Fighting Battles
rule_parent: Deployables and Drones
consolidated: '2026-10-25'
legacy_rule_ids:
- V2-202
- V2-203
- V2-204
- V2-205
- V2-206
- V2-207
- V2-208
- V2-217
component_rules:
- rule_id: V2-202
  rule_name: Deploy equipment
  status: Drafted
  last_rule_update: null
  review_status: Unreviewed
  review_notes: ''
- rule_id: V2-203
  rule_name: Device arming delay
  status: Drafted
  last_rule_update: null
  review_status: Unreviewed
  review_notes: ''
- rule_id: V2-204
  rule_name: Concealed devices
  status: Drafted
  last_rule_update: null
  review_status: Unreviewed
  review_notes: ''
- rule_id: V2-205
  rule_name: Disarm
  status: Drafted
  last_rule_update: null
  review_status: Unreviewed
  review_notes: ''
- rule_id: V2-206
  rule_name: Recover device
  status: Drafted
  last_rule_update: null
  review_status: Unreviewed
  review_notes: ''
- rule_id: V2-207
  rule_name: Device damage
  status: Drafted
  last_rule_update: null
  review_status: Unreviewed
  review_notes: ''
- rule_id: V2-208
  rule_name: Device targeting
  status: Drafted
  last_rule_update: null
  review_status: Unreviewed
  review_notes: ''
- rule_id: V2-217
  rule_name: Friendly mine triggers
  status: Drafted
  last_rule_update: null
  review_status: Unreviewed
  review_notes: ''
---

# Deploying, revealing, disarming and damaging devices

## Summary

Deploy equipment; Device arming delay; Concealed devices; Disarm; Recover device; Device damage; Device targeting; Friendly mine triggers

## Rule text

### Deploy equipment

| Field | Value |
| --- | --- |
| Action | Deploy or Repair |
| Cost | Core |
| Main effect | Place or restore one carried device |

^text-s019-b011

Carried devices already count in Crew Rating. Spend Core to place one in base contact, outside other bases and away from an occupied objective marker. A barricade or ordinary ladder is automatic. Arming a mine, trap, or electronic device requires INT. Success arms it; failure leaves it placed but inert and visible. A natural 1 does not detonate it during deployment. A later Deploy action in contact can retry using the same item.

^text-s058-b000

### Device arming delay

After deployment, turn its card to Active or Inert. It cannot trigger on models already in its trigger area at the moment it is armed; their subsequent movement can trigger it. Devices cannot act the turn they are deployed except passive smoke or physical cover. A sentry first gains READY at the next Start Phase.

^text-s058-b001

### Concealed devices

All device locations are public. A concealed mine or trap is a face-down numbered marker: its type is written privately beside its number. Concealment hides the payload, not the location. It is revealed when triggered, successfully Observed, or approached within 2 inches and LOS by a conscious fighter. No dummy markers are required.

^text-s059-b000

### Disarm

An unengaged fighter in contact may spend Core and test DEX to disarm a mine or trap. Success makes it inert; failure leaves it armed; natural 1 triggers it. An electronic device can instead be disabled with portable hacking. An inert device can be recovered with Interact into a free equipment slot.

^text-s059-b001

### Device damage

A visible device can be shot or struck. Use normal shooting to hit; an adjacent unengaged fighter may spend Core to hit it automatically. There is **no Injury roll** against these small devices. One hit makes standing equipment Offline; a further hit makes it Destroyed. A mine or trap hit while armed is disarmed and ruined without an explosion. A utility drone is Destroyed by its first hit. Device cover follows its actual position. Devices have no Stress, morale, skills, or objective-control presence.

^text-s059-b002

### Friendly mine triggers

For mines and traps, **either crew can trigger them**. Placing one is a positional decision, not permission for your own fighters to walk through it safely. A flying drone does not trigger a ground-contact tripwire or clamp; it can trigger an electronic proximity mine if actually within its three-dimensional radius.

^text-s060-b008

## Links

- [[Settlements/Rules System/Second Draft/Rule Cards - Complete Index|Rule index]]

## Design notes

Consolidated without changing rule meaning on 2026-10-25. Original per-rule statuses, dates and feedback are retained in `component_rules` and the dated source snapshot.
