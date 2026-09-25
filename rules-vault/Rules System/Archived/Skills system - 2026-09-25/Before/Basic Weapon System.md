---
type: design-framework
title: Basic Weapon System
status: Drafted
version: v0.1
created: 2026-09-10
tags: [settlements/design, settlements/weapons, settlements/basic-weapons]
---
# Settlements — Basic Weapon System

> [!important] Design draft, pending integration
> This note defines the basic weapon construction system and the characteristics available to ordinary weapons. It records the current design decisions; it does not by itself replace the weapon rules in [[Full Rules System v1]]. Any adopted mechanical change must be propagated to the master note, weapon catalogue, costing engine, and relevant ledger cards.

## 1. Weapon construction

Every basic weapon is built in four steps:

1. Choose a **weapon class**. The class supplies the weapon's basic Damage envelope, range envelope, hands requirement, rank gate, and slot value.
2. Choose the weapon's **Damage** and **Range** within that class's envelope.
3. Add legal **characteristics**, conditions, and drawbacks to define how the weapon behaves.
4. Give the finished build a name and price it using the existing Credits system.

The class is an envelope, not a finished weapon. A pistol, revolver, and machine pistol may share a class while differing in Damage, Range, and characteristics. A sniper rifle, shotgun, and automatic rifle may likewise be different builds within the two-handed ranged envelope.

Weapons are the primary source of direct offensive improvement. They may improve how an attack hits, how much harm it causes, how many attack dice it rolls, what armour or cover it ignores, and what payload it delivers. Weapons do not grant Skills or permanent changes to a unit.

## 2. Basic weapon classes

| Class | Damage envelope | Range envelope | Hands | Rank gate | Slots | Identity |
|---|---:|---:|---:|---|---:|---|
| **Unarmed** | +0 | Melee | — | Any | 0 | Universal fallback when no weapon is available. |
| **1h Ranged / Sidearm** | +1 to +3 | 6"–12" | 1 | Recruit | 1 | Pistols and other one-handed firearms. Always a Sidearm and may fire while Engaged. |
| **2h Ranged** | +1 to +3 | 24" base | 2 | Fighter | 2 | Ordinary rifles, SMGs, shotguns, and other general-purpose firearms. |
| **Heavy 2h Ranged** | +3 to +5 | 24" base | 2 | Specialist | 3 | Heavy or support weapons, launchers, and other high-output systems. |
| **1h Melee** | +1 to +3 | Melee | 1 | Recruit | 1 | Knives, clubs, axes, machetes, and other one-handed weapons. |
| **2h Melee** | +3 to +5 | Melee | 2 | Fighter | 2 | Large, powerful, or two-handed melee weapons. |
| **Thrown** | +1 to +2 | 8" | 1 | Recruit | 1 | Weapons thrown at range; may also be used in melee. |

^tbl-1-weapon-classes

The class's Damage and Range values are selected when the weapon is built. They are not automatically the maximum shown in the envelope.

### Rank access

- **Recruit:** Unarmed, 1h Ranged / Sidearm, 1h Melee, Thrown.
- **Fighter:** all Recruit classes plus 2h Ranged and 2h Melee.
- **Specialist:** all Fighter classes plus Heavy 2h Ranged.
- **Leader:** all classes.

A weapon does not gain an additional rank requirement because of its name. A sniper rifle built inside the 2h Ranged class follows the ordinary gate for that class; it does not require a separate Specialist or Leader gate.

## 3. Basic weapon characteristics

Characteristics describe the finished weapon's behaviour. Each characteristic must state its exact value, trigger, and interaction with the core attack sequence before the weapon is priced.

### Accuracy and harm

| Characteristic | Effect |
|---|---|
| **Accurate** | Add +1 to the weapon's attack roll. |
| **Precision** | After making an attack roll with this weapon, re-roll it once and use the new result. |
| **Lethal** | Add the stated Damage value. |
| **Piercing** | Reduce the target's effective Armour by the stated value for the Injury roll, to a minimum of 0. |
| **Brutal** | Roll one additional Injury die and choose the highest result. The additional die does not create an additional Wound. |
| **Automatic** | Roll the stated number of Attack Dice for one Action. Resolve the burst using the normal Attack Dice rules. |
| **Ignore Cover** | Ignore the stated amount of cover penalty when making the attack. This does not permit attacks without line of sight. |

^tbl-damage-armour

Accurate and Precision are intentionally overlapping options. Accurate improves the attack roll directly; Precision replaces one result with a second attempt. They may be assigned to different weapons at different prices.

### Payloads and conditions

| Characteristic | Effect |
|---|---|
| **Suppression** | Apply the stated suppression effect when the weapon's defined trigger occurs. If it delivers a condition instead of a wound, use the existing condition and payload rules. |
| **Stress** | Add the stated amount of Stress when the weapon's defined trigger occurs. |
| **Blast** | Resolve the attack separately against every legal unit within the stated distance of the target or impact point. |
| **Knock Back** | Push the target directly away by the stated distance. Resolve falls and hazards normally. |
| **Pull** | Move the target directly toward the weapon or impact point by the stated distance, subject to the final weapon wording. |
| **Hook** | Apply the stated close-combat disengagement penalty. The exact modifier and duration must be printed on the weapon. |

^tbl-payload-replaces-the-non-wounding-result

Weapon payloads apply existing conditions; they do not redefine those conditions. A weapon attack still wounds or delivers its payload according to the core rules and may not stack a second result unless the rule expressly permits it.

### Use and handling

| Characteristic | Effect |
|---|---|
| **Close Combat** | The weapon may be used to make its listed attack while the wielder is Engaged. |
| **Agile** | The weapon may use AGI instead of STR for its melee attack. |
| **Quiet** | The attack does not reveal a Hidden wielder and does not trigger noise or alarm consequences. |
| **Reload** | After firing, the weapon cannot be fired again until its wielder spends one Action reloading it. A unit may reload and fire in the same activation if it has enough Actions remaining. |
| **Long Range** | Increase the weapon's range to the next legal range band. Any additional restrictions on range beyond 24" still apply. |
| **Single-Use** | The weapon may be used once per battle and is then expended. |

^tbl-handling

“Agile” is a weapon handling rule. It does not improve the wielder's AGI stat. “Close Combat” describes where the weapon may be used; it does not add a separate attack.

## 4. Basic weapon examples

These examples show how classes and characteristics combine. They are construction examples until their final Credits costs are entered in the live catalogue.

| Name | Class | Characteristics / conditions | Damage | Range | Hands | Rank gate | Slots |
|---|---|---|---:|---:|---:|---|---:|
| Pistol | 1h Ranged / Sidearm | — | +1 | 8" | 1 | Recruit | 1 |
| Revolver | 1h Ranged / Sidearm | Accurate | +2 | 8" | 1 | Recruit | 1 |
| Magnum | 1h Ranged / Sidearm | Lethal, Reload | +3 | 10" | 1 | Recruit | 1 |
| Shiv | 1h Melee | Agile | +1 | Melee | 1 | Recruit | 1 |
| Machete | 1h Melee | — | +2 | Melee | 1 | Recruit | 1 |
| Crowbar | 1h Melee | Breaching | +2 | Melee | 1 | Recruit | 1 |
| Spear | 2h Melee | Agile | +3 | Melee | 2 | Fighter | 2 |
| Two-Handed Axe | 2h Melee | Brutal | +3 | Melee | 2 | Fighter | 2 |
| Submachine Gun | 2h Ranged | Automatic 2, Close Combat | +1 | 12" | 2 | Fighter | 2 |
| Assault Rifle | 2h Ranged | Accurate | +2 | 24" | 2 | Fighter | 2 |
| Shotgun | 2h Ranged | Blast, Short Range | +3 | 12" | 2 | Fighter | 2 |
| Sniper Rifle | 2h Ranged | Accurate, Precision, Long Range | +3 | 36" | 2 | Fighter | 2 |
| Machine Gun | Heavy 2h Ranged | Automatic 3, Suppression | +4 | 24" | 2 | Specialist | 3 |
| Grenade Launcher | Heavy 2h Ranged | Blast, Reload | +3 | 24" | 2 | Specialist | 3 |
| Flamethrower | Heavy 2h Ranged | Blast, Suppression, Short Range | +3 | 12" | 2 | Specialist | 3 |
| Rocket Launcher | Heavy 2h Ranged | Blast, Piercing, Single-Use | +5 | 24" | 2 | Specialist | 3 |
| Grenade | Thrown | Blast, Single-Use | +1 | 8" | 1 | Recruit | 1 |
| Smoke Grenade | Thrown | Single-Use, Smoke payload | — | 8" | 1 | Recruit | 1 |
| Molotov | Thrown | Blast, Suppression, Single-Use | +1 | 8" | 1 | Recruit | 1 |
| Javelin | Thrown | Piercing, Close Combat | +2 | 8" / Melee | 1 | Recruit | 1 |

^tbl-5-sample-armoury

## 5. Build restrictions

- A weapon may not exceed its class's Damage or Range envelope without an explicit, recorded exception.
- **Deadly / Automatic Down** is not a basic weapon characteristic. Basic weapons use the normal hit, Injury, Wound, and payload sequence.
- **Reach** is not a characteristic. A weapon's appearance does not create an extended engagement distance unless a future rule gives that distance a concrete effect.
- Characteristics may overlap in purpose. Overlap is controlled through each characteristic's exact effect, cost, legal class access, and any drawback; it is not a reason to create another class.
- Reload is an action-economy restriction, not a second ammunition system.
- Thrown weapons may be reusable or Single-Use. Grenades and similar expendables take Single-Use; javelins, throwing axes, and throwing knives do not automatically do so.
- Basic weapons must obey the core 1d10 resolution, natural-roll rules, modifier cap, Damage ceiling, and existing condition rules.

## 6. Finalisation checklist

- [x] Seven basic classes defined.
- [x] One shared class for all one-handed guns.
- [x] Heavy 2h Ranged gated to Specialist.
- [x] Sniper rifles receive no extra Specialist or Leader gate beyond their class.
- [x] Deadly / Automatic Down removed from the basic list.
- [x] Accurate and Precision retained as intentionally overlapping accuracy characteristics.
- [x] Reach removed.
- [x] Reload defined as one Action before the weapon can fire again.
- [ ] Confirm exact numeric values for every characteristic.
- [ ] Assemble the final named weapon catalogue and Credits costs.
- [ ] Propagate adopted values to [[Full Rules System v1]], [[Weapons]], the costing engine, and the Rules Ledger.

Related: [[Modifier Design Framework]] · [[Full Rules System v1]] · [[Weapons]] · [[Skill Paths]] · [[Damage]] · [[Conditions]] · [[Rules System — Master Roadmap]]
