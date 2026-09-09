---
type: design-framework
title: Modifier Design Framework
status: Drafted
version: v0.1
created: 2026-09-09
tags: [settlements/design, settlements/modifiers]
---
# Settlements — Modifier Design Framework

> [!important] Design direction, pending integration
> This note records the framework developed with Ross, including the revised Equipment boundary. It guides future design; it does not automatically replace existing rules or grant the example effects below. [[Full Rules System v1]] remains the authority for play until specific changes are reviewed and propagated.

## Purpose and Category Identities

Every benefit or penalty must have a clear source, purpose, trigger, and duration. Players should understand what changes their unit, why it changes, and when that change ends.

Keep the categories connected to the actual entries players choose, acquire, or record on their units:

- **Weapons:** how the unit attacks and becomes more dangerous.
- **Armour:** what protects the unit against attacks and wounds.
- **Skills:** what the unit knows how to do.
- **Equipment:** limited-use resources that provide temporary benefits.
- **Advancements:** how the unit permanently develops.
- **Injuries:** the lasting consequences the unit carries.

Category boundaries govern an effect's direct purpose. A movement option can indirectly improve survival, and a permanent stat advancement can improve an attack. Those consequences still matter for balance; they do not change which category owns the original effect.

## 1. Weapons — Lethality

Weapons are the primary source of direct improvements to lethality. Their rules determine how attacks are delivered, what they affect, and what happens when they connect.

Weapon effects may change Damage, attack count, range, armour penetration, attack re-rolls, conditional accuracy, interaction with cover, blast or indirect attacks, Stress, and permitted attack payloads.

Accuracy bonuses must have a specific condition, such as attacking a target in the open. Avoid unconditional “+1 to hit” benefits.

Weapons must not provide unrelated protection, general stat increases, or bonuses to non-combat tasks. Attack payloads use the existing conditions and wound-or-payload rules; this framework does not authorise additional stacking.

**Identity:** A better weapon improves the attack available to its wielder.

## 2. Armour — Survivability

Armour is the primary source of sustained protection against attacks and wounds.

Armour effects may modify the chance of being wounded, reduce incoming attacks or their effects, resist specifically named harmful conditions, or provide protection equivalent to cover where the design justifies it.

Every benefit must serve a protective purpose. Armour must not increase accuracy, Damage, attack count, or other offensive output. It must not permanently increase the unit's underlying Wounds or stats.

Always name the threat being resisted. Protection against one condition does not imply protection against all conditions. Protection against a battlefield wound does not automatically modify campaign Injury or Fate outcomes.

**Identity:** Armour improves the protection worn by the unit.

## 3. Skills — Capability

Skills represent training, technique, and practical experience. Their primary purpose is to grant actions, options, permissions, and ways to interact with the battlefield.

Skills should fit their governing stat, provide broadly comparable benefits across stat paths at the same tier, support believable behaviour, and make units distinct through meaningful choices.

Suitable effects include additional carrying options, altered equipment-handling requirements, specialised interactions, new actions, and alternative ways to traverse terrain.

Skills may improve specifically named non-combat tests. For example, “+1 to INT tests to repair machinery” is suitable. A blanket INT-test bonus is too broad if it also improves direct combat effects.

Skills must not directly improve hit rolls, wound rolls, Damage, attack count, injury resistance, or Wounds. Permanent increases to underlying stats or movement distance belong to Advancements.

A movement Skill changes how a unit moves. An equipment-handling Skill changes what it can carry or wield. Neither should add an unrelated offensive or protective bonus. Permissions such as treating a two-handed melee weapon as one-handed must still be assessed for their full tactical benefit.

**Identity:** A skilled unit has more ways to solve a problem.

## 4. Equipment — Limited Benefits

Equipment may borrow modifiers, effects, or capabilities from any of the other categories. Its defining restrictions are **limited use** and **non-persistence between games**.

Every item must satisfy all of the following:

- **Limited uses:** State how many times it can be used and what is expended.
- **Defined timing:** State when it can be used and any activation cost.
- **Defined duration:** State when each benefit ends. No granted modifier or capability lasts beyond the current game.
- **No permanent improvement:** Equipment cannot permanently increase stats, Wounds, or movement, or grant lasting Skills or Advancements.
- **Normal limits:** Existing modifier caps, characteristic ceilings, and resolution rules still apply.
- **Explicit replenishment:** State whether the item is consumed, whether an underlying reusable item remains, and whether spent uses replenish or require another purchase using Credits.

Examples include temporary weapon enhancements, expendable attacks such as grenades or satchel charges, temporary protection, climbing aids, bypassing a specified test, temporary carrying capacity, and temporary stat changes from chems. These examples are design possibilities, not newly granted rules.

The non-persistence restriction applies to the granted benefit or capability. It does not reverse resolved actions at the end of the game: an expendable attack can still cause an Injury through the normal campaign rules.

**Identity:** Equipment provides temporary access to a benefit through a resource the player chooses when to spend.

## 5. Advancements — Lasting Growth

Advancements own permanent increases to a unit's underlying stats, Wounds, and movement distance.

They represent lasting development earned through the campaign. They may also unlock Skills, support rank progression, and record enduring milestones where the campaign rules permit.

Advancements must follow the existing progression structure and characteristic limits. This framework creates no extra advancement opportunities.

A Skill unlocked through an Advancement still follows the Skill boundaries. Any permanent characteristic increase belongs to the Advancement itself.

**Identity:** An Advancement records how the unit has grown, independently of its current loadout.

## 6. Injuries — Lasting Consequences

Injuries own permanent reductions to a unit's underlying stats, Wounds, and movement distance, and may impose specific enduring limitations.

Each Injury must state its effect, whether recovery is possible, and exactly what changes or removes it. “Permanent” means it persists between games until an explicit recovery rule removes it; it does not mean every Injury must be incurable.

Temporary battlefield penalties use existing conditions where applicable. Conditions remain shared mechanics used by these categories, not a replacement category for unit choices.

Advancements and Injuries should help tell the unit's story. Capture, promotion, recovery, and survival can become lasting parts of that history without every event needing another modifier or resource track.

**Identity:** An Injury records what happened to the unit and how it continues to affect them.

## 7. Shared Writing Rules

Every effect must state:

1. **Source:** The specific entry granting or applying it.
2. **Trigger:** Exactly when it applies.
3. **Effect and scope:** The named roll, characteristic, action, permission, or target it changes.
4. **Duration:** When it ends or how it persists.
5. **Limits:** Uses, costs, restrictions, replenishment, and interaction with other effects.

Reuse existing mechanics and named conditions. Do not introduce a slightly different version of a condition when the existing one serves the purpose.

Preserve binary 7+ tests, natural-roll rules, the ±3 roll-modifier cap, existing characteristic ceilings, and the single Credits economy. Trivial actions auto-pass; this framework does not introduce difficulty tiers.

Place an effect in the category that owns its direct purpose. Equipment is the explicit limited-use exception. Any other exception must be narrow and recorded rather than silently broadening the category.

## Integration and Open Decisions

- [x] Record the six tangible categories and their design boundaries.
- [x] Define Equipment as limited-use access to cross-category effects whose benefits do not persist between games.
- [ ] Audit existing Skills, Weapons, Armour, Equipment, and campaign rules against the framework before changing their live wording.
- [ ] Resolve existing exceptions, including Tough granting +1 WND in [[Full Rules System v1]]. This framework does not remove Tough or alter the current WND ceiling.
- [ ] Decide whether medical Equipment may permanently remove a campaign Injury. No such exception is adopted here.
- [ ] Confirm item-by-item replenishment and whether unspent items remain on the roster; expiry of benefits alone does not decide inventory retention.
- [ ] Propagate any subsequently adopted mechanical changes through the master, satellite notes, ledger, and relevant catalogues.

Related: [[Full Rules System v1]] · [[Weapons]] · [[Skill Paths]] · [[Unit Design]] · [[Progression]] · [[Conditions]] · [[Rules System — Master Roadmap]]
