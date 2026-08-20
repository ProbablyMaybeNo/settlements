---
type: reference
title: Skill Paths
tags: [settlements/reference]
---
# 🧠 Skill Paths

Skills are the **third lever**: stats decide *if* you hit, weapons decide *how bad*, **skills decide what else happens**. A skill is a **verb or a conditional exception** — a new option or situational effect, **not** a flat stat increase (those are the least interesting, so we avoid them — where a numeric edge is needed it's **conditional** (e.g. +1 to hit *in the open*) and kept **high-tier**).

## How it works — skills ride the stat line
Every point-stat (STR, DEX, AGI, INT, NRV) is also a **skill path**. There's no separate skill pool — **a stat hands you a skill every time it reaches a tier.**

- A path-stat at **+2 = Tier 1 · +4 = Tier 2 · +6 = Tier 3.** (**+1 is a dabble** — capable, no tier, no skill.)
- **Each tier a stat reaches grants one skill from that stat's path, at that tier.** So a stat at **+4** grants its **T1 *and* T2** skill; at **+6**, its **T1 + T2 + T3**.
- You **choose** the specific skill from that path at that tier — and may take a lower-tier skill from the same path if you prefer (the tier is a ceiling). It must match the stat's path: no Combat skill on your Intelligence.
- Pick at **crew-build** as you set the stat line, and again in a **campaign** whenever an Advance tips a stat into a new tier ([[Progression]]).

So the stat line *is* the skill loadout — **spread wide** (`STR+2 / INT+2` → one Combat + one Expertise skill, a melee-hacker) or **specialise deep** (`STR+4` → two Combat skills, a master). Same count, different shape. Rank sets how far you can push it:

| Rank | Stat pts | Tier caps | Skills *(Match Play)* | Skills *(Campaign Start)* |
|---|:---:|---|:---:|:---:|
| **Recruit** | 3 | no tiers | **0** | **0** |
| **Fighter** | 5 | 2× T1 | ~2 | **1× T1** |
| **Specialist** | 7 | 1× T2 · 2× T1 | ~3 | **1× T2** |
| **Leader** | 9 | 1× T3 · 2× T2 · 4× T1 | ~4 | **1× T3** |

^tbl-how-it-works-skills-ride-the-stat-line

> [!info] Two starting kits, one catalogue
> **Match Play** (one-off game, 850 Crew Rating) takes every skill the stat line earns — those fighters never get another chance to develop. A **Campaign Start** crew (425 Crew Rating) takes **exactly one skill, at its rank's tier**, and earns the rest through the Level track ([[Progression]]) — a fully-levelled fighter ends on **four** skills, all from their Primary path. Ruled 2026-08-05, [[Full Rules System v1]] §16 · §26.1.

Only a **Leader** gets a **T3** stat (the +6 elite). Full rank rules in [[Unit Design#Ranks (build budget)]] · fielding in [[List Building]].

## The five paths
Each path-stat has one path with three tiers. **WND and MOV have no path** — they're fixed (1 and 6"), raised only by a specific skill below. *Path names are WIP.*

| Stat | Path | Covers |
|---|---|---|
| **STR** | Combat / Muscle | melee, force, grappling, breaking, hauling |
| **DEX** | Shooting / Perception | ranged, aim, spotting, trick shots |
| **AGI** | Movement / Acrobatics | climbing, dodging, repositioning, escaping |
| **INT** | Expertise / Knowledge | hacking, traps, medicine, tech, terrain |
| **NRV** | Bravery / Morale | rallying, resisting fear, reckless aggression |

^tbl-the-five-paths

## Complete skill catalogue
Each skill fills **one tier-slot** off its stat's path — you don't pay for it separately; the stat reaching the tier *is* the payment. There are no skill prerequisites: reaching the tier unlocks its skills, and combinations emerge from the skills, equipment and terrain a fighter uses.

> [!info] Design contract
> - **Tier 1 — Good:** reliable options and narrow exceptions.
> - **Tier 2 — Great:** role-defining actions and stronger combinations.
> - **Tier 3 — Amazing:** campaign-earned, fight-swinging abilities.
> - A modifier from a skill is conditional and the final modifier on any roll cannot exceed **+3 or −3**.
> - **Difficulty is a modifier on the standard 7+ test, never a raised target number.** A harder job is **−1 / −2 / −3** (within the cap); a strong roll can grant a bonus (*"beat the target by 2+"*). No 9+/11+ targets.
> - Unless a skill explicitly says otherwise, a fighter still makes at most **one attack per activation**.
> - Every condition a skill applies is defined in **[[Conditions]]** — skills apply conditions, they never redefine them.

## Combat / Muscle (STR)
### Tier 1 — Good

- **Heavy Hands** — Gain +1 on a melee attack against a **Pinned** or **Grappled** defender. *(Melee DPS · Grappler)*
- **Knockback** — After winning a melee attack, push the defender 2" directly away before the Injury roll; you may follow up to 2". *(Melee DPS · Terrain controller)*
- **Breakdown** — As an Action, automatically open or destroy an adjacent ordinary Breachable door, window or light barricade. *(Breacher)*
- **Deadlift** — As an Action, pick up an adjacent Movable terrain piece. Move at half MOV while carrying it; dropping it within 1" is free. *(Hauler · Terrain controller)*
- **Strong Arm** — Double the printed range of thrown weapons. You may throw a carried Movable object up to 4" as an Action. *(Thrower · DEX combo)*
- **Grapple** — Replace a melee attack with an opposed STR test. On a win, apply **Grappled** instead of making an Injury roll. *(Grappler · Controller)*
- **Bodyguard** — Once per round, when an attack targets a friendly within 2", move up to 2" and become the target instead if you are a legal target. *(Tank · Protector)*
- **Rooted** — When an effect would forcibly move you, pass a STR test to ignore all forced movement from that effect. *(Tank · Terrain controller)*
- **Pack Mule** — Carrying an objective or friendly does not reduce your Move. You may Sprint while carrying, but cannot Charge. *(Hauler · Objective runner)*
- **Doorstop** — While adjacent to a closed Openable door, an enemy must spend an Action and beat you in an opposed STR test to open it. *(Tank · Terrain controller)*

### Tier 2 — Great
- **Muscle Override** — As an Action, force an adjacent powered or locked door open or closed without its terminal. This is Loud and cannot affect Reinforced barriers. *(Breacher · INT combo)*
- **Human Shield** — Ranged attacks tracing LOS through an enemy you have Grappled treat you and friendlies within 1" as having Heavy Cover. *(Tank · Grappler)*
- **Super Slam** — When your Charge attack hits but fails its Injury roll, the target becomes **Suppressed** instead of the usual Shaken. *(Melee DPS · Controller)*
- **Squeeze** — As an Action, make an opposed STR test against an enemy you have Grappled. On a win, it suffers an automatic unarmed hit; make only the Injury roll. *(Grappler · Melee DPS)*
- **Come Along** — You may move your full MOV while dragging a Grappled enemy and keeping it within 1". You still cannot Sprint or Charge. *(Grappler · Objective control)*
- **Disarm** — After winning a melee attack, forgo the Injury roll to make the defender drop one held weapon or carried item within 1". Recovering it requires an adjacent Action. *(Controller · Equipment denial)*
- **Breach and Clear** — After your Action opens or destroys a door, window or barricade, immediately move up to 3" through the opening. *(Breacher · Assault)*
- **Power Position** — As an Action, move and rotate an adjacent Movable terrain piece up to 3". It cannot overlap models or Impassable terrain. *(Tank · Terrain controller)*
- **Fireman's Carry** — Carry a Down friendly at full MOV. You may take the Stabilize Action while carrying that fighter without putting them down. *(Rescuer · INT combo)*
- **Clinch** — If your free swing against a Disengaging enemy hits, its Disengage ends before it moves. *(Tank · Grappler)*

### Tier 3 — Amazing
- **Tough** — Increase this fighter's WND by 1. This is a named exception to the normal fixed WND value. *(Tank)*
- **The Muscle** — Add +2 to the Injury roll for the first melee hit you land during a Charge. *(Melee DPS)*
- **Slam & Throw** — As an Action, make an opposed STR test against an enemy you have Grappled. On a win, place it anywhere within 5" and make it Pinned; falling and hazardous terrain resolve normally. *(Grappler · Terrain controller)*
- **Falcon Punch** — After your Charge attack hits, push the defender 4". If it contacts terrain or another fighter, stop it and make the defender Pinned. If it contacted another fighter, make that fighter Pinned too. *(Melee DPS · Terrain controller)*
- **Wrecking Crew** — If your Charge attack makes its defender Down, immediately make one melee attack at −2 against a different enemy within 1". This cannot trigger again that activation. *(Melee DPS)*
- **Juggernaut** — During a Charge, move through one ordinary closed door or light barricade, destroy it and continue moving. You must still reach a legal target. *(Breacher · Tank)*
- **Crushing Hold** — When an enemy you have Grappled fails its escape test, it becomes Pinned and gains **Bleed**. *(Grappler · Melee DPS)*
- **Living Barricade** — A friendly within 1" directly behind your base has Heavy Cover. If that cover changes a ranged hit into a miss, resolve the hit against you instead. *(Tank · Protector)*
- **Structural Collapse** — As an Action, pass a STR test to destroy up to a 4"-wide section of adjacent Breachable terrain. On success, every fighter within 2" becomes Pinned and gains the normal 1 Stress from Pinned; on failure, the terrain remains and you become Pinned. *(Breacher · Area controller)*
- **Too Angry to Drop** — Once per round when you would become Pinned, gain 1 Stress to ignore Pinned. *(Tank · NRV combo)*

## Shooting / Perception (DEX)
### Tier 1 — Good
- **Long Barrel** — If you do not Move, a rifle's maximum range increases by 5" for this activation. *(Sniper)*
- **Ready to React** — As an Action, Ready against one visible enemy. If it Charges before your next activation, make one reaction attack against it at −2 before it moves. *(Overwatch)*
- **Bank Shot** — When Heavy Cover causes your ranged attack to miss by exactly 1, a target touching that cover becomes Pinned; make no Injury roll. *(Trick shot · Suppressor)*
- **Sharp Eyes** — As an Action, choose one visible enemy within 18"; it is **Spotted** by you until the end of the round. *(Scout · Spotter)*
- **Muzzle Flash** — After a visible enemy makes a ranged attack within 24", it is Spotted by you until the end of the round. *(Counter-sniper · Spotter)*
- **Covering Fire** — As an Action, choose a visible 4"-wide lane within weapon range. The first enemy crossing it before your next activation becomes Pinned if you pass a DEX test at −2; make no Injury roll. *(Suppressor · Area control)*
- **Called Shot** — Make a ranged attack at −2. On a hit, you may forgo the Injury roll to make the target drop one carried item or become **Hobbled**. *(Controller · Equipment denial)*
- **Shoot and Shift** — After resolving your ranged attack, move up to 2" toward cover. You cannot use this after Sprinting or Charging. *(Skirmisher · Ranged DPS)*
- **Crossfire** — When your ranged attack hits an already Pinned target but fails to injure it, that target becomes Suppressed. *(Suppressor · Team combo)*
- **Tripwire Eye** — As an Action, shoot a visible terrain trigger within 12". Pass a DEX test to activate it from the impact point instead of making an Injury roll. *(Terrain shooter · Utility)*

### Tier 2 — Great
- **Sniper** — When a rifle attack against a target more than 12" away misses by exactly 1 and you did not Move, the target becomes Pinned; make no Injury roll. *(Sniper)*
- **I See You** — When attacking an enemy Spotted by you, reduce its Hidden hit modifier from −3 to −2. *(Scout · Anti-concealment)*
- **Lookout** — As an Action, choose one visible enemy within 24" and up to two allies within 6". That enemy is Spotted by those allies until the end of the round. *(Spotter · Support)*
- **One in a Million** — As an Action, shoot any visible terrain trigger within the weapon's maximum range at −2. On a hit, activate it from the impact point instead of making an Injury roll. *(Terrain shooter · Trick shot)*
- **Kill Lane** — As an Action, mark a straight 3"-wide lane within weapon range. Before your next activation, make one reaction attack at −2 against the first enemy that Moves within it. *(Overwatch · Area control)*
- **Relocation Drill** — After firing from cover, move up to 3" if you did not Move earlier this activation. You cannot become Hidden during this movement. *(Skirmisher · Sniper)*
- **Pin Them Down** — When your ranged attack hits but fails its Injury roll, the target becomes Suppressed instead of Pinned. *(Suppressor · Ranged DPS)*
- **Breach Window** — When an ally in your LOS destroys, opens or moves terrain, immediately Spot one newly revealed enemy within 18" until the end of the round. *(Spotter · STR/INT combo)*
- **Running Read** — After Moving at least 5", choose one enemy you crossed LOS to during that Move; it is Spotted by you until the end of the round. *(Scout · AGI combo)*
- **Calm Under Fire** — Pinned does not prevent you from taking Ready, Spot or terrain-trigger Actions. Ignore Shaken's −1 modifier on tests made for those Actions. *(Overwatch · NRV combo)*

### Tier 3 — Amazing
- **Dead Eye** — Gain +1 on one ranged attack if you did not Move and the target has no cover. *(Sniper · Ranged DPS)*
- **Quick Shot** — If you did not Move, attack the same target twice with a pistol, SMG or semi-automatic rifle within 12"; the second attack is at −2. You cannot make Reactions this round. *(Ranged DPS)*
- **Gunslinger** — If carrying two pistols and you did not Move, attack two different targets within 8", once each at −2. You cannot make Reactions this round. *(Ranged DPS · Gunslinger)*
- **Counter-Sniper** — Once per round, when a visible enemy attacks from more than 18" away, immediately Spot it and Ready against it without spending an Action. *(Counter-sniper · Overwatch)*
- **Patient Overwatch** — As an Action, Ready against a visible 6"-wide area within weapon range. Before your next activation, make one reaction attack at −1 against one enemy that attacks or Moves there. *(Overwatch · Area control)*
- **Thread the Gap** — When attacking through an opening no wider than 2", reduce the target's cover penalty by 1, to a minimum of −1. You must not have Moved. *(Sniper · Terrain shooter)*
- **Forward Observer** — As an Action, choose one visible enemy within 30". It is Spotted by every ally within 12" of you until the end of the round. *(Scout · Team support)*
- **Shoot the Supports** — As an Action, make a ranged attack at −2 against a visible Breachable terrain element within range. On a hit, make an Injury roll against Armor 0. On a pass, destroy it and Suppress every fighter within 2". *(Terrain shooter · Area control)*
- **Last Known Position** — Once per round, when an enemy Spotted by you becomes Hidden, mark its position. Your next attack against it before it Moves uses a −2 Hidden modifier instead of −3. *(Hunter · Anti-concealment)*
- **Controlled Burst** — When you hit a target within 12", forgo the Injury roll to make it Suppressed and push it up to 2" directly away from the attack, stopping at obstacles or fighters. *(Suppressor · Controller)*

## Movement / Acrobatics (AGI)
### Tier 1 — Good
- **Sure-Footed** — Automatically pass AGI tests caused solely by unstable, slippery or uneven ground. *(Terrain runner)*
- **Like a Cat** — Falls of 3" or less cause no Injury. For longer falls, reduce the measured distance by 3". *(Acrobat · Infiltrator)*
- **Weave** — After moving at least 3", melee attacks against you suffer −1 until your next activation. *(Evasive skirmisher)*
- **Leaper** — Cross horizontal gaps up to 3" without testing, counting the gap as movement. Gain +2 on AGI tests for longer jumps. *(Terrain runner)*
- **Vault** — Cross one waist-high obstacle during a Move without testing or paying additional movement; you cannot end on it. *(Mobile melee · Terrain runner)*
- **Low Profile** — While Hidden, move up to 3" without losing Hidden if you finish outside every enemy's LOS. *(Scout · Infiltrator)*
- **Quick Hands** — Once per activation, perform one simple pick-up, drop or objective interaction during your Move. You cannot attack that activation. *(Objective runner)*
- **Break Contact** — After resolving a Disengage, move an additional 3". This movement cannot enter contact with an enemy. *(Escape · Skirmisher)*
- **Rescue Grip** — Carrying one Down friendly does not reduce your normal Move. You still cannot Sprint, Charge or attack while carrying them. *(Rescuer)*
- **Scramble** — When you become Pinned, immediately move up to 2" toward the nearest cover you can reach. This is not a Disengage. *(Scout · Survival)*

### Tier 2 — Great
- **Houdini** — Once per round, when targeted by a ranged attack from more than 12", move up to 3" before the roll. If this breaks LOS, the attack fails and you become Hidden. *(Escape · Infiltrator)*
- **Sidestep** — Once per round, when Charged, move up to 3" before the attack. If the charger can no longer reach you with its remaining movement, the Charge ends without an attack. *(Evasive skirmisher)*
- **Water Walker** — Treat shallow water and similar liquid terrain as open ground. Cross designated swimmable deep water at half movement without testing. *(Terrain runner)*
- **Slide** — During a Move or Sprint, pass through one enemy's space if there is room beyond it. You cannot end there or use this during a Charge. *(Infiltrator · Escape)*
- **Double Dash** — Sprint may consume only your Action instead of both slots. You may still use your normal Move, but cannot attack or Interact that activation. *(Objective runner · Scout)*
- **Fleet** — Your MOV is 8" instead of 6". This is a named exception to the normal fixed MOV value. *(Objective runner · Mobile melee)*
- **Parkour Route** — During one Move, combine climbing, jumping and ordinary movement into one route. Measure it normally and make only one AGI test. *(Terrain runner · Infiltrator)*
- **Grab and Go** — After picking up an objective or Down friendly, immediately move up to 3". This movement cannot enter enemy contact. *(Objective runner · Extraction)*
- **Feint** — If you began your Move outside the target's LOS and moved at least 3" immediately before making a melee attack against it, gain +2 on that attack. *(Mobile melee DPS)*
- **Leg Sweep** — After winning a melee attack, forgo its Injury roll to make the target **Off-Balance**. *(Controller · Mobile melee)*

### Tier 3 — Amazing
- **Ghost Blade** — Use AGI instead of STR for your melee attack rolls. Defenders oppose normally. *(Mobile melee DPS · Duelist)*
- **Dual Wield** — After a normal Move, attack once with each of two one-handed melee weapons; the second attack suffers −2. This overrides the one-attack limit but cannot be used with Charge. *(Mobile melee DPS)*
- **Trading Spaces** — After winning a melee attack, before the Injury roll, exchange base positions with the defender if both bases fit. This does not trigger Disengage. *(Controller · Mobile melee)*
- **In-N-Out** — After your Charge attack hits, Disengage for free and move up to 3". You cannot enter contact with another enemy. *(Mobile melee DPS · Skirmisher)*
- **Vanishing Point** — If you finish a Sprint in cover and outside every enemy's LOS, become Hidden. *(Scout · Infiltrator)*
- **Extraction Drill** — While adjacent to a Down friendly, pick them up and Sprint while carrying them. This consumes both slots and permits no attack or Interact. *(Rescuer · Extraction)*
- **Wall Runner** — Once per activation, cross one wall, vehicle or similar obstacle up to 3" high without testing. Measure the route normally. *(Terrain runner · Infiltrator)*
- **Cornering Charge** — During a Charge, ignore Difficult Ground and cross one waist-high obstacle without testing or additional movement cost. You must still have LOS when declaring the Charge and reach a legal target. *(Mobile melee · Terrain runner)*
- **Reversal** — Once per round, after an enemy misses you in melee, move up to 3", including through that enemy's space. You cannot end in contact with an enemy. *(Evasive skirmisher · Escape)*
- **Action on the Run** — During a normal Move, pause to take one non-attack Action, then complete any unused movement. *(Objective runner · Infiltrator)*

## Expertise / Knowledge (INT)
### Tier 1 — Good
- **Hacker** — As an Action beside a Hackable device, pass an INT test to access data, loop a camera, silence an alarm or toggle an unlocked Powered system. Modifiers apply and an enemy may Interrupt ([[Hacking]]). *(Hacker · Objective specialist)*
- **Locksmith** — As an Action beside a Lockable door or container, pass an INT test to lock or unlock it without damage; hard security is **at −2**, military-grade **at −3** (still a 7+ test). *(Infiltrator · Objective specialist)*
- **Trapper** — As an Action, arm, disarm, conceal or reposition an adjacent carried trap or terrain trap with an INT test. Searching for your concealed trap is an opposed INT test. *(Trapper · Controller)*
- **Medic** — As an Action beside a casualty with medical supplies, pass an INT test to remove Bleed or Poison. You automatically Stabilize an adjacent Down fighter instead of making the normal Stabilize test. *(Medic · Support)*
- **Camouflage Drill** — When you take the Hide Action in Concealing terrain, one adjacent friendly touching the same terrain may also become Hidden. *(Infiltrator · Team support)*
- **Loop Camera** — As an Action, hack an adjacent camera. On success, it ignores you and one chosen ally until either attacks, enters contact with an enemy or the camera is reset. *(Hacker · Infiltrator)*
- **Jury-Rig** — As an Action beside a damaged Powered device, pass an INT test to restore one basic function until the encounter ends. Failure by 3+ disables it until repaired. *(Engineer · Tech support)*
- **Threat Scan** — As an Action, pass an INT test while observing a 6" area to reveal one Hidden trap, mine, camera, alarm or Powered hazard there; **beat the target by 2+** to also identify its trigger and a safe route. *(Intel support · Trapper)*
- **Jam Signals** — As an Action, pass an INT test against one electronic device or remote trap within 6". It becomes **Jammed** until your next activation. *(Hacker · Debuffer)*
- **Read the Objective** — As an Action beside an objective, pass an INT test to learn its active defences, required interaction and whether it is trapped, alarmed, Powered, Hackable or Lockable. *(Objective specialist · Intel support)*

### Tier 2 — Great
- **Computer Whiz** — As an Action at an accessed terminal, hack one **Linked** device on its local network ([[Hacking]] rules apply — modifiers, Interrupt). *(Hacker · Remote control)*
- **Turret Tamer** — As an Action, hack a Linked or adjacent turret to rotate, deactivate or fire it once. Firing uses the turret's profile and counts as your one attack. *(Hacker DPS · Controller)*
- **Lockdown** — As an Action at a terminal or control panel, pass an INT test to lock or unlock up to three Linked Lockable doors until your next activation. *(Hacker · Area controller)*
- **Field Surgeon** — As an Action beside a Down fighter with medical supplies, pass an INT test **at −2** to restore them to 1 WND, remove Down and leave them Pinned. Each casualty can benefit once per encounter. *(Medic · Recovery support)*
- **Counter-Hack** — When Readied at a device or terminal, **Interrupt** a hostile hack ([[Hacking]]) **without Overloading your own terminal**; the interrupted system is left **Compromised**. *(Hacker nerfer · Tech support)*
- **Trap Relay** — As an Action, pass an INT test to link up to three armed electronic traps within 6". Until your next activation, when one linked trap triggers normally, trigger one other linked trap whose normal conditions are met. A trap triggered by Trap Relay cannot trigger this skill, and each linked trap can trigger at most once. *(Trapper · Area control)*
- **Power Broker** — As an Action at a power control, pass an INT test to disable one Linked Powered system and activate, restore or use the printed overcharge effect of another until your next activation. *(Engineer · Hacker buffer)*
- **Forensic Sweep** — As an Action at a body, terminal, trap or objective, pass an INT test to identify the last interaction, its direction and one tool used; **beat the target by 2+** to also reveal deliberate tampering. *(Intel support · Objective specialist)*
- **Tactical Uplink** — As an Action at a camera, sensor or terminal, pass an INT test and choose two allies visible to it; each ignores Blind or Shaken for their next single Action. *(Hacker buffer · Intel support)*
- **Shepherd Alarm** — As an Action, hack an alarm or sensor to suppress its next trigger or redirect it to one Linked alarm zone. It cannot fabricate targets. *(Hacker debuffer · Controller)*

### Tier 3 — Amazing
- **Mastermind** — As an Action at an accessed terminal, make one INT test to operate two different Linked non-weapon device functions; failure operates neither. *(Hacker · Controller)*
- **Kaboom** — As an Action, hack or wire one visible Explosive or Powered hazard within 6". Detonate it now or set one specific trigger; its normal profile counts as your one attack. *(Hacker DPS · Trapper)*
- **Blackout Protocol** — As an Action at a power node, pass an INT test **at −2** to disable all Linked lights, cameras, alarms and unlocked doors in one defined zone until your next activation. *(Hacker nerfer · Area controller)*
- **Rewrite Killbox** — As an Action at a security terminal, pass an INT test to make up to two Linked turrets treat your allies as authorised and prevent the enemy firing them remotely until your next activation. *(Hacker buffer · Hacker nerfer)*
- **Trauma Reset** — As an Action beside a Down fighter with medical supplies, pass an INT test **at −3** to restore them to 1 WND, remove Down and remove one of Bleed, Poison, Blind or Shocked. Each casualty can benefit once per encounter. *(Medic · Recovery support)*
- **Ghost the Network** — As an Action at a terminal, pass an INT test so cameras, alarms and access logs on that network ignore your crew until your next activation or until an ally attacks through the network. *(Hacker · Infiltrator)*
- **Fortify Objective** — As an Action beside an objective, pass an INT test to arm its existing alarm, engage its lock, activate its cover mechanism or impose **−2 on any hack** to access it for the rest of the encounter. *(Engineer · Objective specialist)*
- **Minefield Conductor** — As an Action, pass an INT test to control up to three visible electronic mines within 9". Until your next activation, suppress their triggers or trigger one legal mine; it counts as your one attack. *(Hacker DPS · Area controller)*
- **Predictive Model** — As an Action after observing an enemy or monitored 6" zone, pass an INT test. Choose one: up to two allies within 6" each remove 2 Stress, or the first enemy entering that zone before your next activation becomes Pinned. *(Hacker buffer · Debuffer)*
- **Camo King** — As an Action in Concealing terrain, make yourself and up to two allies within 3" Hidden even if observed. Until your next activation, each may move 2" within connected Concealing terrain without losing Hidden; attacking still ends it. *(Infiltrator · Team support)*

## Bravery / Morale (NRV)
### Tier 1 — Good
- **Steady** — Once per activation, remove 1 Stress from yourself before or after taking an Action. *(Stress controller · Anchor)*
- **Rattle-Proof** — Ignore the first point of Stress you would gain each round. *(Tank · Composure)*
- **Battle Cry** — Once per activation after moving into melee, choose one Engaged enemy; it gains 1 Stress. *(Intimidator · Melee)*
- **Dig In** — If you do not Move during your activation, become **Braced** until your next activation. *(Tank · Anchor)*
- **Keep Moving** — As an Action, choose an ally within 6"; it immediately moves up to 3" without entering enemy contact. *(Leader · Reposition support)*
- **Stare Down** — As an Action, make an opposed NRV test against one visible enemy within 6". On a win, it gains 1 Stress and becomes **Cowed**. *(Intimidator · Debuffer)*
- **Feed the Anger** — Before a melee attack, gain 1 Stress to add +1 to that attack **and ignore Shaken's −1 for that activation**. Once per activation. *(Berserker · Melee DPS)*
- **Drag Clear** — When an ally within 3" becomes Down, move directly toward it up to 3". If you finish adjacent, other allies gain 1 less Stress from that Down event. *(Rescuer · Morale support)*
- **Count Breaths** — If you neither attacked nor issued an Order during your activation, remove 2 Stress at its end. *(Composure · Stress controller)*
- **Buddy Check** — If you end your activation adjacent to an ally and neither of you attacked this round, each removes 1 Stress. *(Morale support · Anchor)*

### Tier 2 — Great
- **Rally** — As an Action, choose yourself or an ally within 6"; remove 2 Stress, or end a Bolt or Broken state. *(Morale support)*
- **Fearless** — Gain no Stress from seeing an ally become Down, and reduce Stress caused by negative conditions by 1, minimum 0. *(Anchor · Tank)*
- **Bloodlust** — When your melee attack makes an enemy Down, remove 3 Stress; if the attack misses, gain 1 Stress. *(Berserker · Melee DPS)*
- **Talk Them Down** — Once per round, when an ally within 3" fails a Break test, reduce the resulting state one step (BugOut → Broken → Bolt → no state) and gain 2 Stress yourself. *(Morale support · Anchor)*
- **Snap Out of It** — As an Action, end one non-persistent negative condition on an ally within 3"; that ally gains 1 Stress. *(Condition support)*
- **Take It on Me** — Once per round, when an ally within 3" gains Stress, take up to 2 of that Stress instead. *(Tank · Protector)*
- **Dare Me** — As an Action, choose a visible enemy within 8"; it becomes **Provoked** until the end of its next activation. *(Intimidator · Tank)*
- **No One Left** — As an Action while adjacent to a Down ally, move up to half MOV while carrying them; this movement may leave an Engagement without a free swing. *(Rescuer · Extraction)*
- **Hard Case** — The first negative condition applied to you each round causes no Stress; the condition still applies. *(Tank · Condition control)*
- **Lead from the Front** — Once per round when you spend an Order on an ally within 6", that ally also removes 1 Stress before resolving it. *(Leader · Order support)*

### Tier 3 — Amazing
- **Iron Will** — Once per game, automatically pass one Break test. Natural 1 still fails. *(Anchor · Stress tank)*
- **Fanatic** — When a failed Break test would make you Bolt or Broken, become **Fight** instead (BugOut still applies); while Fighting this way you **ignore Shaken's −1**. After that activation, gain 2 Stress. *(Berserker · High-risk melee)*
- **Unbreakable** — Once per round, you and each friendly within 6" reduce the first Stress gained by 1, minimum 0. *(Anchor · Team support)*
- **Last Command** — When you become Down, immediately issue one Order to an ally within 6" before resolving Down. Once per game. *(Leader · Last stand)*
- **Stand Your Ground** — Once per game, when an ally within 3" fails a Break test, it takes no Break state (it stays merely Shaken) and you gain 3 Stress. *(Anchor · Rescuer)*
- **Terrify** — As an Action, make an opposed NRV test against an enemy within 3". On a win, it gains 2 Stress and becomes **Frightened**. *(Intimidator · Debuffer)*
- **Master the Moment** — Once per game when you issue an Order, apply it to two eligible allies instead of one. Neither granted Action or Reaction can issue an Order. *(Leader · Order specialist)*
- **Walk into Fire** — Once per round, when an ally within 3" is targeted by ranged fire, move adjacent and become the target if legal; gain 1 Stress after the attack. *(Tank · Protector)*
- **Red Mist** — At the start of your activation, gain 3 Stress to add +2 to melee attack rolls **and ignore Shaken's −1** until it ends. You cannot Rally or receive an Order that activation. *(Berserker · Melee DPS)*
- **Clear Heads** — When you roll a natural 10 on a Break test, each ally within 6" removes 2 Stress in addition to you clearing all Stress. *(Morale support · Stress controller)*

## Skill conditions
Every condition and marker state a skill applies — **Grappled, Suppressed, Off-Balance, Hobbled, Provoked, Braced, Cowed, Frightened, Fight, Spotted, Jammed, Compromised, Linked** — is fully defined in **[[Conditions]]**, alongside the core combat, persistent and Nerve states. Skills only *apply* conditions; they never redefine them.

## Example role combinations
- **Tank / bodyguard** — Bodyguard + Living Barricade + Take It on Me or Walk into Fire.
- **Grapple controller** — Grapple + Come Along + Squeeze or Slam & Throw.
- **Melee DPS** — The Muscle + In-N-Out + Feed the Anger or Red Mist.
- **Mobile melee DPS** — Ghost Blade + Feint + Dual Wield.
- **Ranged DPS / sniper** — Sniper + Dead Eye + Thread the Gap.
- **Suppressor** — Crossfire + Pin Them Down + Controlled Burst.
- **Scout / spotter** — Low Profile + Running Read + Lookout or Forward Observer.
- **Objective runner** — Quick Hands + Fleet + Grab and Go.
- **Hacker DPS** — Turret Tamer + Kaboom + Minefield Conductor.
- **Hacker buffer** — Power Broker + Tactical Uplink + Rewrite Killbox.
- **Hacker nerfer** — Jam Signals + Counter-Hack + Blackout Protocol.
- **Medic / extraction** — Field Surgeon + Rescue Grip + No One Left.
- **Terrain controller** — Deadlift or Power Position + One in a Million + Lockdown.
- **Morale anchor** — Rally + Talk Them Down + Unbreakable.

---
See [[Unit Design]] · [[Progression]] · [[Rules System MOC]].
