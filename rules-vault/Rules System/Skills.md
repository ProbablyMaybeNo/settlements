---
type: reference
status: Adopted catalogue; mechanics review pending
updated: 2026-09-25
tags: [settlements/reference, settlements/skills]
---
# Skills

The current catalogue contains **75 skills: 15 each for STR, DEX, AGI, INT and NRV, all in one tier**. Skills create tactical options, playstyles and combinations within and across stats. Offensive and defensive benefits are permitted. There are no player-facing archetype packages or archetype prerequisites.

## Acquisition

**UNDECIDED by Ross, 2026-09-25:** starting counts, stat requirements, selection milestones, campaign acquisition and selection costs. Do not grant skills automatically at +2/+4/+6, apply rank-based skill tiers, or use old tier-roll tables. Keeping the catalogue in one tier does not mean every unit receives every skill. No new acquisition system is implied.

## Using the catalogue

Use the named weapon's profile and ordinary action rules unless a skill explicitly changes them. A free action does not create free equipment or replenish consumables. Skill-specific exceptions permit the combinations written here; no blanket ban on bonus attacks cancels an explicit chain.

Type labels describe usage, not an extra action charge. Unspecified costs and frequencies remain unresolved, not automatically free or unlimited. See [[Skill Integration Decisions]] for the finite mechanics questions still requiring decisions. Values here are the approved design list, not simulation-validated balance.

Shared definitions live in [[Keywords]]. The skills were designed for the thread's d20 revision and positive modifier cap of +6. A complete core dice/Break-table conversion has **not** been approved by selecting these skills; remaining engine conflicts are listed in [[Skill Integration Decisions]], not silently resolved with invented thresholds.

## STR

| SKILL | STAT | TYPE | EFFECT |
| --- | --- | --- | --- |
| **GRAPPLE** | STR | Action | Make an opposed STR test against an enemy within 1 inch. On success, it becomes GRAPPLED; see Keywords for holding, escape and Meat Shield. |
| **STRONG ARM** | STR | Passive | Ignore HEAVY. While holding a GRAPPLED target, move at full MOVE, INTERACT and attack with 1 HANDED weapons. Cannot CHARGE, DASH, CLIMB or use 2 HANDED equipment while holding it. |
| **THROW** | STR | Action | Throw adjacent scatter or obstacle terrain no larger than 3 inches a distance in inches equal to STR. May instead throw a GRAPPLED target. Terrain hitting a unit causes PINNED. A thrown unit hitting a structure suffers an injury roll at +3 Damage; collision with another unit PINs both. |
| **BRACE** | STR | Action | BRACE until the end of the turn: incoming attacks suffer -4 to hit. This unit cannot move, act or react while BRACING. |
| **COME ON THEN** | STR | Action | Test STR. On success, enemies within 6 inches must target this unit with their ATTACK actions. Duration and legal-target exceptions require ruling. |
| **TOUGH AS NAILS** | STR | Triggered | Once per round, when attacked in melee without being wounded, ignore the hit's effects. Subsequent attacks against this unit suffer -4 to injure until the end of the turn. |
| **RAMPAGE** | STR | Triggered | After DOWNING an enemy with a CHARGE ATTACK, move the remaining charge distance. If this brings the unit within 1 inch of another enemy, make a free MELEE ATTACK against it. |
| **BULL** | STR | Attack modifier | When declaring a CHARGE, test STR. On success, pass through non-LOS-blocking scatter, obstacles and barricades. Enemies contacted test AGI; on failure, push them 2 inches in your chosen direction and PIN them. Cannot pass reinforced doors, buildings or LOS-blocking structures. |
| **HUMAN BULLET** | STR | Passive | Determine CHARGE distance using MOVE plus the total of 2d6 instead of 1d6. |
| **RAGE** | STR | Attack modifier | When making a MELEE ATTACK, add up to +3 Damage to its injury roll. Gain 1 STRESS per point added. |
| **I'M ABOUT TO BREAK** | STR | Triggered | Once per turn when CHARGED, use STRESS as positive modifiers instead of penalties for that combat. Afterwards gain 1 STRESS and immediately make a BREAK test, ignoring beneficial Stress modifiers from friendly units, skills or equipment. |
| **BLOWING OFF STEAM** | STR | Triggered | Whenever this unit DOWNS an enemy, remove 2 of its STRESS. |
| **GOLIATH** | STR | Passive | Wield two 2 HANDED melee weapons as if they were 1 HANDED. The off-hand still contributes only one attack die unless another rule explicitly overrides it. |
| **TOUGH** | STR | Passive | Gain +1 WOUND, subject to the unit's Wound ceiling. |
| **BIG FELLA** | STR | Passive | Ignore UNWIELDY on this unit's weapons. |

^tbl-skills-str

## DEX

| SKILL | STAT | TYPE | EFFECT |
| --- | --- | --- | --- |
| **MARK TARGET** | DEX | Move | Spend a MOVE action to MARK an enemy within 24 inches and LOS until the start of this unit's next activation. Friendly shooting gains +2 to hit it and may target it within 24 inches even while HIDDEN, subject to weapon range. |
| **HEAD SHOT** | DEX | Passive | Gain +4 to injure MARKED targets with RANGED ATTACKS if this unit has not moved this turn. |
| **STEADY BREATHING** | DEX | Passive | Increase the range of this unit's 2 HANDED RANGED weapons and MARK TARGET by 12 inches. |
| **GUNSLINGER** | DEX | Passive | When dual wielding 1 HANDED RANGED weapons, the off-hand contributes its full attack dice to the combined SHOOT action. |
| **BULLET TIME** | DEX | Attack modifier | Once per turn when resolving a SHOOT action, divide the combined attack dice between the initial target and additional enemies within 6 inches of it. Each target requires LOS and the contributing weapon's range. |
| **RUN + GUN** | DEX | Passive | Resolve a SHOOT action at any point during this unit's normal MOVE, then complete any remaining movement. Grants no additional movement or free attack. |
| **BREACH** | DEX | Action | Once per turn, select an enemy within 12 inches, even outside LOS. Move up to MOVE through doorways without spending actions or testing, then SHOOT. This unit cannot be targeted by reactions until the shot resolves. The shot requires normal LOS and weapon range. |
| **SPRAY AND PRAY** | DEX | Attack modifier | Once per turn when SHOOTING an initial target within 12 inches, divide attack dice between it and other enemies within 8 inches of it and LOS. Each enemy DOWNED adds one die to allocate to a remaining eligible target. |
| **ON ME** | DEX | Triggered | Nominate a friendly within 6 inches and LOS. Immediately after this unit finishes its activation, activate that friendly. Activation eligibility requires ruling. |
| **WATCH OUT!** | DEX | Reaction | When a friendly within 12 inches and LOS is CHARGED, spend this unit's action or reaction to give that friendly a free RANGED ATTACK before the charge completes. |
| **COVER ME** | DEX | Reaction | Once per turn, when an enemy in LOS SHOOTS a friendly, intervene with a free SHOOTING ATTACK resolved as an opposed DEX test. On success the enemy attack misses; on failure the friendly becomes PINNED and SHAKEN. Damage/Stress resolution requires ruling. |
| **EYES PEELED** | DEX | Triggered | When this unit DOWNS an enemy with a RANGED ATTACK, gain a READY token. Keep it or give it to a friendly within 12 inches and LOS. |
| **PLANNING AHEAD** | DEX | Passive | Equip two 2 HANDED RANGED weapons, or one 1 HANDED and one 2 HANDED RANGED weapon. Choose the active weapon at the start of each activation; it cannot change during that activation. |
| **SPEED LOADER** | DEX | Passive | Once per turn, RELOAD one RANGED weapon while resolving a MOVE action. |
| **PIN THEM DOWN** | DEX | Passive | RANGED hits that fail to wound also cause PINNED. Generate STRESS normally; pinning adds no extra Stress. |

^tbl-skills-dex

## AGI

| SKILL | STAT | TYPE | EFFECT |
| --- | --- | --- | --- |
| **AMBUSH** | AGI | Attack modifier | After a successful CHARGE begun HIDDEN, test AGI. Pass: one melee weapon makes an UNANSWERED attack with +4 to hit and injure; the second weapon attacks normally. Fail: no bonuses; the target may spend an unused ACTION to make an UNANSWERED attack first, followed by your normal attack if still able. |
| **RETURN TO THE SHADOWS** | AGI | Triggered | Once per turn after CLOSE COMBAT, move up to 6 inches without disengage attacks. End behind or in heavy cover and outside LOS of READY enemies. Become HIDDEN if normal hiding requirements are met. |
| **INCAPACITATE** | AGI | Action | Once per turn, make a 6-inch RANGED ATTACK using AGI and one attack die. A hit causes STUNNED; do not roll for injury. |
| **GHOST** | AGI | Passive | Once per turn, resolve a ranged action without losing HIDDEN from firing. Other reveal triggers still apply. |
| **PHANTOM SHOT** | AGI | Passive | When SHOOTING while HIDDEN, hits that fail to wound inflict additional STRESS. Additional amount requires ruling. |
| **SHOW YOURSELF** | AGI | Passive | Enemies can only target this unit within 6 inches while it is HIDDEN, instead of 12 inches. |
| **AMBIDEXTROUS** | AGI | Passive | When dual wielding two 1 HANDED melee weapons that BOTH have AGILE, the off-hand contributes its full attack dice instead of one. |
| **BLADE FURY** | AGI | Triggered | Once per turn, after DOWNING an enemy in melee, make a free MOVE and ATTACK against another enemy within 6 inches. If that enemy is DOWNED, repeat once more against an enemy within 3 inches. |
| **PARRY** | AGI | Triggered | When an enemy fails to hit this unit in melee, make an UNANSWERED melee counterattack against that enemy. This may trigger BLADE FURY. Counterattack recursion requires ruling. |
| **ACROBATIC** | AGI | Passive | Climb scalable structures without climbing gear or access points. Climbing costs movement equal to half the structure's height. |
| **DODGE** | AGI | Reaction | When targeted by an enemy CHARGE or MELEE ATTACK, test AGI. On success move 3 inches. Resolve the charge, but omit its melee attack if this unit is no longer in engagement range. |
| **AERIAL ASSAULT** | AGI | Attack modifier | From a structure at least 3 inches high, select an enemy within charge range. Roll to charge, then test AGI. If both succeed, move into engagement and make an UNANSWERED attack with +1 to hit and injure per full 2 inches of starting height above ground, maximum +4/+4. |
| **QUICK** | AGI | Passive | Gain +2 MOVE. |
| **SNEAK** | AGI | Passive | Ignore the movement penalty while HIDDEN. |
| **SPRINTER** | AGI | Passive | DASH using only the MOVE action instead of spending both actions. |

^tbl-skills-agi

## INT

| SKILL | STAT | TYPE | EFFECT |
| --- | --- | --- | --- |
| **NEURAL UPLINK** | INT | Passive | Gain +4 INT when resolving HACKING tests. |
| **TROJAN** | INT | Action | Test INT to take control of an enemy DEPLOYABLE with ELECTRIC. Immediately resolve an action with it. SINGLE USE deployables may be triggered or defused; resolve their action if triggered, then remove them in either case. |
| **INTERRUPT** | INT | Reaction | While in base contact with an active terminal, when an enemy interacts with another terminal within 12 inches, make an opposed INT test. On success cancel the interaction and FREEZE that terminal until the end of the next turn. May be used after this unit has activated. |
| **TUNNELS** | INT | Setup | Before deployment place two tunnel tokens, 8 inches from enemy deployment or units, 12 inches apart and 6 inches from the board edge. Secretly hold back two crew units. During battle deploy each at a different tunnel, then activate it normally. Enemies may react to arrivals. Arrival timing and distance minima require ruling. |
| **STRATEGIST** | INT | Setup | Once per game, during a turn's initiative phase, decide who activates first. |
| **TAGGED** | INT | Action | Test INT within 12 inches and LOS of an UNCONTESTED objective. On success your crew controls it until an enemy captures it. Your crew may have only one TAGGED objective at a time. |
| **MOLLE** | INT | Passive | Equip up to three unique DEPLOYABLES for battle. |
| **TECHNICIAN** | INT | Passive | Gain +4 INT when testing to set up a DEPLOYABLE during battle. |
| **QUICK DROP** | INT | Triggered | Once per turn after successfully placing a DEPLOYABLE, place another for free within LOS and 8 inches of the first. Uses carried equipment; creates no free device. |
| **STABILIZE** | INT | Action modifier | Gain +4 INT for STABILIZE tests. Success also clears all target STRESS. May spend an ACTION to STABILIZE a non-DOWN unit and clear its STRESS. Once per turn. |
| **CHEMICAL COCKTAIL** | INT | Passive | May resolve two CHEM actions on the same unit. This permission does not make either action free. |
| **DOC** | INT | Passive | Equip up to three unique CHEMS. Once per turn, resolve a free CHEM action on a friendly within 6 inches. |
| **INSPECTOR GADGET** | INT | Passive | Equip up to three EQUIPMENT items for battle. |
| **STIMS** | INT | Action | Once per turn, give two friendly units within 6 inches an additional MOVE during their next activation. Each gains 1 STRESS at the end of that activation. |
| **SMART** | INT | Passive | Resolve one free INTERACT action per turn. Qualifying action categories require ruling. |

^tbl-skills-int

## NRV

| SKILL | STAT | TYPE | EFFECT |
| --- | --- | --- | --- |
| **INSPIRE** | NRV | Action | Once per turn, spend an ACTION and test NRV. On success remove 2 STRESS from up to three friendlies within 8 inches. |
| **RALLY** | NRV | Action | Once per turn, spend an ACTION and test NRV. On success RALLY up to three BROKEN friendlies within 8 inches. |
| **MOTIVATE** | NRV | Action | Once per turn, spend an ACTION and test NRV. Choose two friendlies within 8 inches. During their next activation each may use its MOVE as an ACTION and repeat an action. |
| **SIN EATER** | NRV | Action | Once per turn, spend an ACTION to transfer up to 3 STRESS in total from friendlies within 6 inches to this unit, limited by its remaining Stress capacity. |
| **IMPLODE** | NRV | Attack modifier | Increase maximum STRESS by 2. Once per turn before a MELEE ATTACK, remove up to half this unit's STRESS, rounding down. Gain +1 to hit and injure for that attack per point removed. |
| **LAST LAUGH** | NRV | Triggered | Once per turn, when an enemy attack would DOWN this unit, first make one final SHOOT or MELEE ATTACK against that enemy if it is a legal target. Then resolve this unit becoming DOWNED. |
| **HOLD FAST** | NRV | Aura | Spend an ACTION and test NRV to activate a 6-inch AURA. Injury rolls against friendlies within the aura suffer -2, whether or not they are in cover. |
| **MENACING** | NRV | Aura | Spend an ACTION and test NRV to activate a 6-inch AURA. Friendly attacks made from within it inflict +1 additional STRESS if they score at least one hit. |
| **LEAN ON ME** | NRV | Aura | Spend an ACTION and test NRV to activate a 6-inch AURA. Transfer STRESS inflicted on other friendlies within it to this unit, up to its remaining Stress capacity; excess stays on its original recipient. |
| **ROAR** | NRV | Action | Once per turn, spend an ACTION and test NRV. Until this unit's next activation, enemies must pass NRV to CHARGE it or friendlies within 3 inches. |
| **ON YOUR FEET** | NRV | Action | Once per turn, spend an ACTION and test NRV. On success remove PINNED from up to three friendlies within 8 inches. |
| **COMMANDING PRESENCE** | NRV | Triggered | Once per turn, a friendly within 8 inches and LOS may use this unit's NRV for a BREAK test. |
| **BETA BLOCKER** | NRV | Passive | Halve STRESS penalties, rounding up. Full STRESS still applies to BREAK tests. |
| **UNFLINCHING** | NRV | Triggered | Once per turn, when a hit would remove this unit's READY token, it may retain it. Resolve all other effects normally. |
| **BIG AURA** | NRV | Passive | Increase this unit's AURA ranges by 3 inches. It may maintain two AURAS simultaneously. |

^tbl-skills-nrv
