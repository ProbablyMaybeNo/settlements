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
| M00 / P0 | Basic matched objective battle: do legal turns, attacks, End Phase and scoring make sense? | Interventions, lookups, timings, VP, completion, decision examples | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-044 - Setup and deployment|V2-044]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-052 - Round refresh and initiative|V2-052]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-055 - Activations, action costs and attack limit|V2-055]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-073 - End Phase|V2-073]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-454 - Objective limits and control areas|V2-454]] |
| M01 / P0 | Same shooter/target in open, Light and Heavy cover; normal battle afterwards | Eligible shots, chosen targets, hits, Wounds, position and perceived alternatives | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-049 - Cover and elevation|V2-049]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-097 - Shooting and target allocation|V2-097]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-099 - Aim|V2-099]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-114 - Injury and attack outcomes|V2-114]] |
| M02 / P0 | Sword/shield, club/shield and unarmed defence; Charge and rear approach | Dice/criticals, cancellations, attacks initiated, Wounds and avoidance | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-082 - Charge|V2-082]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-093 - Engagement and Disengage|V2-093]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-102 - Weapon pools, dual wielding and unarmed attacks|V2-102]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-106 - Melee exchanges, Unanswered and Shove|V2-106]], [[Settlements/Rules System/Master Rules System/Item Cards/Weapon Characteristic Cards/V2-543 - Parry|V2-543]] |
| M03 / P0 | ALERT before/after activation; incoming shot/Charge; one Order available | Reaction opportunity/use, interruptions, lost actions, token timing | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-061 - ALERT and reaction eligibility|V2-061]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-065 - Reactions and interruption|V2-065]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-485 - Orders|V2-485]] |
| M04 / P0 | Non-wounding hits, extra Wound then Pinning, Down/revive and Break/Rally | Stress, recovery delay, functional activations lost, revivals, morale duration | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-114 - Injury and attack outcomes|V2-114]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-117 - Pinned and recovery|V2-117]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-122 - Down and Unconscious casualties|V2-122]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-126 - Treatment and revival|V2-126]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-139 - Stress, Break and forced flight|V2-139]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-150 - Rally|V2-150]] |
| M05 / P1 | Climb, jump, approach/escape a ledge, Carry and forced movement | Route, reach, tests, falls, time/action costs, physical ambiguity | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-074 - Facing, visibility and rear attacks|V2-074]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-078 - Move, obstacles and Sprint|V2-078]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-084 - Climbing, jumping and falling|V2-084]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-089 - Forced movement|V2-089]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-090 - Carrying and releasing loads|V2-090]] |
| M06 / P1 | Hidden approach, Observe, Mark expiry and smoke | Target eligibility, reveal, missed options, useful choices | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-154 - Hidden and Observe|V2-154]], [[Settlements/Rules System/Master Rules System/Item Cards/Skill Cards/V2-316 - Mark Target|V2-316]], [[Settlements/Rules System/Master Rules System/Item Cards/Equipment Cards/V2-258 - Smoke grenade|V2-258]] |
| M07 / P1 | Frag placement/scatter, friendly fire, smoke and one consumable | Footprints, casualties, resource use, timing and handling | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-248 - Area attacks, smoke and fire|V2-248]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-492 - Tools and equipment|V2-492]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-493 - Consumables and medical supplies|V2-493]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-498 - Equipment conditions|V2-498]] |
| M08 / P1 | One terminal with a door/bridge, manual route and enemy response | INT attempts, freezes, denied access, actions saved, counterplay | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-162 - Interact and stat examples|V2-162]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-165 - Hacking, terminals and repair|V2-165]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-176 - Shared terrain operations and hazards|V2-176]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-496 - Interactive terrain catalogue|V2-496]] |
| M09 / P1 | One operator/device per side; then contested deployment and shutdown | Operator/device actions, uptime, reactions, control failures, responses | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-202 - Deploying, revealing, disarming and damaging devices|V2-202]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-218 - Sentry turret operations|V2-218]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-220 - Drone operations|V2-220]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-497 - Deployable equipment catalogue|V2-497]] |
| M10 / P2 | Intended-use fixture for each skill; risk-based legal pairs/triples | Opportunity/use, effect, counters, rules exceptions and loops | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-305 - Choosing and using skills|V2-305]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-487 - STR skills|V2-487]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-488 - DEX skills|V2-488]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-489 - AGI skills|V2-489]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-490 - INT skills|V2-490]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-491 - NRV skills|V2-491]] |
| M11 / P2 | Later legal roster construction and equal-Credit matches | Build errors, dominant packages, omissions and trade-offs | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-029 - Recruitment and training grades|V2-029]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-034 - Crew composition and item limits|V2-034]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-037 - Equipping fighters and handling weapons|V2-037]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-025 - Credits and Crew Rating|V2-025]] |
| M12 / later | Linked battles, advancement and campaign incentives after costs | Progression, injury/replacement and runaway advantage | [[Settlements/Rules System/Master Rules System/Rule Cards/V2-153 - Ending a battle and recovering the crew|V2-153]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-386 - Battle rewards|V2-386]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-389 - Experience and deeds|V2-389]], [[Settlements/Rules System/Master Rules System/Rule Cards/V2-392 - Advancement and promotion|V2-392]] |

## Coverage is evidence, not a tick for having printed a card

For every rule/item intended for release, distinguish **documented, exercised, understood, measured, integrated and retested**. Use the owner-level CSV in Data to attach session IDs and evidence. A procedure can share evidence with several cards; a catalogue wrapper is not a new mechanic requiring an artificial separate battle.

The first pack tests only five selected skills and a small loadout set. All 60 skills and all approved battle profiles need an eventual disposition before a game-wide claim. Prioritise shared foundations and high-risk interactions; do not exhaustively demand every theoretical permutation in human play.

High-risk examples to rotate later: Rage/Implode; sword/shield and extra defence; Gun-fu/Gunslinger; repeated reactions and turret control; operator/device activation advantage; armour/Wounds/revival; terrain displacement/fall damage; chem stacking; slots/actions/resource loops. These are hypotheses to examine, not predetermined nerfs.

## Links

- [[Settlements/Testing/START HERE - Settlements Testing|Testing workspace]]
- [[Settlements/Rules System/Master Rules System/Master Rules System|Approved Master Rules System]]
