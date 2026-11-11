---
type: settlements-testing-note
testing_id: TST-009
testing_section: Modules
status: Planning
created: 2026-11-11
updated: 2026-11-11
summary: "Prioritise the battle core, then rotate related mechanics and integrate them again."
cssclasses:
- settlements-rule-group
tags:
- settlements/testing
---

# Modules and priorities

## Summary

Prioritise the battle core, then rotate related mechanics and integrate them again.

^testing-summary

## What needs testing first?

**Priority 0:** objective/scoring and board setup; legal activations and actions; movement/facing/LOS/cover; shooting and Injury; melee and defensive dice; ALERT/Orders and timing; Stress, morale, Pinning and casualty recovery. These determine whether a basic battle works and whether its decisions feel worthwhile.

**Priority 1:** vertical movement, stealth/marking, area attacks, medical/utility gear, interactive terrain/hacking and deployables. They introduce strong counterplay and state interactions but can be added in packs.

**Priority 2:** the complete skill/catalogue spread, advanced cross-build combinations, roster construction and later campaign progression. Lower priority means later coverage, not permission to ship untested.

## Module catalogue

| ID / priority | Question and fixture | Record | Current owners |
| --- | --- | --- | --- |
| M00 / P0 | Basic matched objective battle: do legal turns, attacks, End Phase and scoring make sense? | Interventions, lookups, timings, VP, completion, decision examples | V2-044/052/055/073/454 |
| M01 / P0 | Same shooter/target in open, Light and Heavy cover; normal battle afterwards | Eligible shots, chosen targets, hits, Wounds, position and perceived alternatives | V2-049/097/099/114 |
| M02 / P0 | Sword/shield, club/shield and unarmed defence; Charge and rear approach | Dice/criticals, cancellations, attacks initiated, Wounds and avoidance | V2-082/093/102/106, V2-543 |
| M03 / P0 | ALERT before/after activation; incoming shot/Charge; one Order available | Reaction opportunity/use, interruptions, lost actions, token timing | V2-061/065/485 |
| M04 / P0 | Non-wounding hits, extra Wound then Pinning, Down/revive and Break/Rally | Stress, recovery delay, functional activations lost, revivals, morale duration | V2-114/117/122/126/139/150 |
| M05 / P1 | Climb, jump, approach/escape a ledge, Carry and forced movement | Route, reach, tests, falls, time/action costs, physical ambiguity | V2-074/078/084/089/090 |
| M06 / P1 | Hidden approach, Observe, Mark expiry and smoke | Target eligibility, reveal, missed options, useful choices | V2-154, V2-316/258 |
| M07 / P1 | Frag placement/scatter, friendly fire, smoke and one consumable | Footprints, casualties, resource use, timing and handling | V2-248/492/493/498 |
| M08 / P1 | One terminal with a door/bridge, manual route and enemy response | INT attempts, freezes, denied access, actions saved, counterplay | V2-162/165/176/496 |
| M09 / P1 | One operator/device per side; then contested deployment and shutdown | Operator/device actions, uptime, reactions, control failures, responses | V2-202/218/220/497 |
| M10 / P2 | Intended-use fixture for each skill; risk-based legal pairs/triples | Opportunity/use, effect, counters, rules exceptions and loops | V2-305/487/488/489/490/491 |
| M11 / P2 | Later legal roster construction and equal-Credit matches | Build errors, dominant packages, omissions and trade-offs | V2-029/034/037/025 |
| M12 / later | Linked battles, advancement and campaign incentives after costs | Progression, injury/replacement and runaway advantage | V2-153/386/389/392 |

## Coverage is evidence, not a tick for having printed a card

For every rule/item intended for release, distinguish **documented, exercised, understood, measured, integrated and retested**. Use the owner-level CSV in Data to attach session IDs and evidence. A procedure can share evidence with several cards; a catalogue wrapper is not a new mechanic requiring an artificial separate battle.

The first pack tests only five selected skills and a small loadout set. All 60 skills and all approved battle profiles need an eventual disposition before a game-wide claim. Prioritise shared foundations and high-risk interactions; do not exhaustively demand every theoretical permutation in human play.

High-risk examples to rotate later: Rage/Implode; sword/shield and extra defence; Gun-fu/Gunslinger; repeated reactions and turret control; operator/device activation advantage; armour/Wounds/revival; terrain displacement/fall damage; chem stacking; slots/actions/resource loops. These are hypotheses to examine, not predetermined nerfs.

## Links

- [[Settlements/Testing/START HERE - Settlements Testing|Testing workspace]]
- [[Settlements/Rules System/Master Rules System/Master Rules System|Approved Master Rules System]]
