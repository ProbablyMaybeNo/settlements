---
type: settlements-battle-catalogue-working-reference
created: 2026-11-01
tags:
  - settlements/battle-catalogue-review
---

# Battle Rules Reference

Battle procedures copied from the current ChatGPT working list on 1 November 2026, for use beside these editable catalogues. Catalogue entries remain under review.

[[Settlements/Design Workshop/Battle Catalogue Review/00 Battle Catalogue Review|All battle catalogues]] · [ChatGPT working list](https://chatgpt.com/space/page_ffc1cec57d808191a3e04ad1edeb1c8e)

## 1 Ordinary tests and modifiers

**Testing rule:** Roll **1d20 + Stat + modifiers − Stress against 13+**. Natural 1 fails; natural 20 succeeds. Trivial tasks are automatic; impossible tasks cannot be attempted with the available tools and position. For skills and equipment separately, use the largest positive and negative modifiers. Modifier categories stack, but each category is capped at ±4; Stats and Stress are exempt. Cover and the target's Pinned/Down/Unconscious condition are separate categories, so heavy cover −4 and the condition penalty −2 combine to −6. Injury, initiative and distance ignore Stress; Break and Rally use NRV − Stress as printed.

## 9 Equipping fighters and handling weapons

**Proposed testing rule:**

Each fighter has **3 weapon slots shared between melee and ranged weapons**. A one-handed weapon uses 1 slot and a two-handed weapon uses 2. This allows one two-handed weapon plus one one-handed weapon, or three one-handed weapons. Two two-handed weapons cannot be carried unless a skill or item explicitly changes that limit. The included utility knife is free but uses 1 weapon slot if carried; Unarmed uses none.

**When declaring any attack, nominate either one carried weapon (one-handed or two-handed), or two carried one-handed weapons**, including for Return Fire. Resolve a two-weapon attack using card 29's off-hand rule: the primary weapon contributes its normal Attack Dice and the off-hand weapon contributes only 1 die, regardless of its printed Attacks, unless a skill explicitly overrides this. An attack cannot use all three carried weapons or combine a two-handed weapon with another weapon unless a skill explicitly permits it. Holstering and drawing are included in the attack and cost no separate action. There is no per-round weapon-change limit. Meet each chosen weapon's profile requirements, including any required Stats; looted weapons follow the same requirements.

Each fighter also has **1 armour slot and 2 equipment slots**. Equipment slots hold equipment, grenades and other active items according to their profiles. **A pair of grenades occupies 1 equipment slot.** Each use consumes one grenade; a remaining grenade continues occupying that slot. Other consumables retain their own listed quantities and slot costs. Deployed devices continue reserving the operator's equipment slots unless their rules say otherwise.

## 14 Unit activations and actions

**Proposed testing rule:**

Players alternate unit activations. Each unit has two actions, **one Move and one Core**, which can be spent in either order before the opponent's next activation. Once a unit has completed both actions, its activation ends and the opposing player selects a unit to activate. A unit may forgo unused actions and end its activation early.

Units with an **ALERT** token may react outside their own activation, following the **Reactions** rules. Choose actions from the list below. Some skills and equipment provide additional action choices.

| Action cost | Choices |
| --- | --- |
| **Move** | Move, Climb, Jump, Sneak; Recover from Pinned. |
| **Core** | Attack (melee or ranged), Interact (including Hack, Repair, Loot or Secure), Hide, Deploy, Revive, ALERT, Aim, Observe, Reload, Rally, Use Item, Disengage, Carry. |
| **Move + Core** | Sprint, Charge, Aerial Assault. |

An action costing **Move + Core** spends both actions and requires both to be unused. Each action follows its own procedure and eligibility rules. Orders follow card 16.

## 17 Reactions and interruption

**Proposed testing rule:** Multiple eligible units may react to the same enemy unit. Each may react once per round. Spend an ALERT token to perform one Move or Core action, following its normal requirements. Actions that cost both actions cannot be reactions. Reactions trigger when the enemy starts or ends its activation within LOS; there is no separate reaction range. Shooting uses the chosen weapon's range. Reaction Shoot occurs at either activation boundary, not partway through movement. When an enemy declares a Charge against this unit, it may instead spend its ALERT token to Shoot before the charger moves, using normal LOS, forward arc and weapon range requirements. Return Fire against a shot targeting you requires the attacker to be within LOS, forward arc and weapon range. Declare it before dice and resolve simultaneous independent normal shooting against 13+, completing both attacks before applying either attack's results. Dive tests AGI before an incoming shot or Charge, moving up to 3 inches on success and becoming Pinned either way. Pinning or Downing cancels an unfinished action without refund; completed actions are not undone. Return Fire follows its simultaneous resolution rule. No reactions to reactions.

## 19 Facing visibility and rear attacks

**Current rule:** Units can see through their front arc at any vertical angle. Change facing during own movement and once at the start of own Core; no free enemy-turn pivot. Use an agreed normal human body volume, roughly 2 inches tall; walls and standing body volumes block sight. Pinned, Down and Unconscious targets use their base footprint. An attack declared wholly behind the target cannot be reacted to through its rear arc; it grants no bonus to hit.

## 20 Cover and elevation

**Current rule:** A model has cover when terrain or an object blocks part of it from the attacker's view. If less than 50% of the model is blocked, it has Light cover: −2 to hit. If 50% or more is blocked, it has Heavy cover: −4 to hit. Use the strongest cover grade only. A Pinned, Down or Unconscious unit in cover imposes an additional −2 modifier on the attacker's hit roll. Cover and this condition are separate modifier categories: heavy cover plus this condition gives −6 total. The attacker must still have LOS to the target; a completely hidden model cannot be targeted. Ignore a low obstacle within 1 inch of the shooter when firing over it. Height gives a better view, with no automatic accuracy bonus.

## 21 Move obstacles and Sprint

**Current rule:** A model may pivot as many times as it wishes during movement. Move up to MOVE along a legal path; a normal Move cancels Hidden. Sneak is a Move action allowing movement up to half MOVE while retaining Hidden. Do not enter within 1 inch of an enemy unit that is not a casualty except by Charge; casualties permit approach. Unlocked doors open during movement; deliberately closing one uses Interact. An obstacle up to 1 inch high costs 2 inches to cross. Difficult ground and half-speed effects halve movement only once rather than multiplying. Sprint costs Both for up to twice MOVE with no attack; remove Hidden first.

## 22 Charge

**Current rule:** Spend Both against one visible conscious enemy within MOVE + 6 by a plausible route. Roll d6 and travel up to MOVE + result; reaching within 1 inch gives one melee exchange and +1 dominant-weapon die. There is no three-dice maximum for Charge or Aerial Assault. Failure moves up to MOVE toward the target and stops outside engagement. Failed traversal or an interrupting reaction can end the Charge with no attack. Stress affects tests and the attack, not distance. Aerial Assault costs Both and may be attempted against an enemy within LOS and Charge range when the attacker is more than 3 inches above the target. Move the attacker to the edge of its platform or terrain closest to the target, then make an AGI test. On success, place the attacker within engagement range of the target and resolve a melee exchange with +2 additional attack dice instead of the normal Charge's +1. On failure, the attacker falls; resolve the existing falling rules as written.

## 23 Climbing jumping and falling

**Current rule:** Stairs, ladders and ramps use measured movement. To begin a climb or use a ladder, a unit must have enough movement to reach the top or a ledge where it can stand. It cannot end movement partway up a wall or ladder. Climbing requires no gear and is performed at half movement, with one AGI test per action; failure stays at the starting level and natural 1 falls from halfway. A unit may jump gaps up to 3 inches without a test. Gaps over 3 inches and up to 6 inches require an AGI test; failure causes a fall. A unit must have enough remaining movement to cross the gap. No unit may jump a gap wider than 6 inches, regardless of its MOVE. Deliberate drops up to 2 inches are safe. To jump down from a height greater than 2 inches, make an AGI test: on success, land safely; on failure, fall. A fall automatically hits, with no hit roll. Resolve Injury against the standard 13+ target number using 1 Injury die for a fall up to 3 inches, 2 dice for over 3 and up to 6 inches, 3 dice for over 6 and up to 9 inches, and 4 dice for over 9 and up to 12 inches. A fall from over 12 inches causes immediate Out of Action, with no Injury roll. Each falling Injury die is a flat d20 against 13+, with no Damage bonus and ignoring Armour; after resolving it, the unit becomes Pinned if conscious. 

## 25 Carrying and releasing loads

**Testing rule — 10 November 2026:** Spend Core and test STR while in base contact with a structure no larger than 3 inches or a Down unit. Success makes you Carrying it; failure spends Core and leaves it in place. No Grapple skill is required. Move at half speed and Fight or Shoot with only one one-handed weapon. During your activation you may freely Drop the load into an open position within 2 inches. One unit carries one load; there is no joint two-carrier action. Existing Sprint/Charge restrictions remain. Hauler and the load-bearing harness ignore their stated movement penalties, not the one-handed Carrying restriction. Carrying an enemy does not itself Secure it or make it a captured prisoner; use Secure and extraction for capture. Mission cargo still follows its scenario-specific handling rules.

## 26 Engagement and Disengage

**Current rule:** Engagement permits melee, Grapple, melee Sidearm use, Recover, self-Rally and Disengage, while blocking outside shooting and ordinary interaction. Disengage is a Core action requiring an AGI test. On success, move up to full MOVE. On failure, the opponent gets a free hit before the unit moves. Resolve the hit first: if it leaves the unit Pinned, Down, Unconscious or Out of Action, it stays in its current position and does not move; otherwise, it may still move up to full MOVE. Forced flight permits the same free enemy exchange without an escape test. A Move can instead reposition up to 1 inch within the existing engagement.

## 27 Shooting and target allocation

**Current rule:** Core Shoot chooses a legal forward-arc target within LOS and range. Roll a number of d20s equal to the weapon's Attack Dice; resolve each die with ± modifiers against 13+. Natural 1 misses and natural 20 hits. Each hit rolls Injury. There is no generic movement or long-range penalty. Normal shooting selects one target; Split Fire is an exception. Shooting into friendly engagement sends each natural 1 into an involved friendly chosen by the opponent; blasts instead affect everyone in their area.

## 28 Aim

**Testing rule:** Spend a Core action to gain **+2 to hit on the unit's next attack**, including a shooting reaction. The bonus applies to that attack's hit dice and is then spent. Repeated Aim does not stack.

## 29 Weapon pools dual wielding and unarmed attacks

**Current rule:** When dual wielding two one-handed weapons, use the main weapon's full Attack Dice plus one identifiable off-hand die using the off-hand weapon's profile. Ranged weapons with the Pistol keyword can be used in melee.

## 31 Melee exchanges Unanswered and Shove

**Testing rule:** Choose one engaged enemy. Both roll held melee pools using STR, or AGI with Agile, and normal relevant modifiers. Resolve each Attack Die against the standard 13+ target number using the normal attack rules. Cancel opposing normal successes one for one. Critical successes (natural 20s) cancel only opposing critical successes, also one for one; normal and critical successes cannot cancel each other. Each uncancelled success causes an Injury roll against the opposing fighter. Add +2 against Pinned. Defensive pools remain even when Pinned or Unanswered, but Down, Unconscious and Captured targets have none. Unanswered lets only the initiator hit; it is not automatic damage. Attacking from behind prevents reactions but does not by itself make an attack Unanswered. Core Shove replaces injury with an opposed STR test. On success, push the target directly backwards 2 inches, away from the shoving unit, stopping on contact with a solid structure or another unit. The pushed unit becomes Pinned only if it collides with a solid structure or another unit; a collision with another unit Pins both units. Resolve normal hazards.

## 32 Injury and attack outcomes

**Testing rule:** During the hit-roll phase, each successful hit adds **1 Stress** to the target. Then, for each successful hit, roll **1d20 + DMG − Armour ± applicable Injury modifiers against 13+**. Apply the modifiers to each die separately. Stress does not affect Injury rolls. Natural 1 fails; natural 20 succeeds. Armour supplies no separate save.

Each successful Injury roll removes **1 Wound**. At zero Wounds, the target is **Down**; if it still has a Wound after being hit, it becomes **Pinned**. Injury rolls add no further Stress, whether they succeed or fail. Resolve the attack's Injury dice together. Stress remains on the unit but is **ignored while Down or Unconscious**.

Every human has one Wound. Surplus Injury successes do not automatically execute the target or cause additional lasting injuries.

## 33 Pinned and recovery

**Current rule:** A Pinned unit spends a Move action to stand.

## 34 Down and Unconscious casualties

**Current rule:** At zero Wounds mark Down and its round, remove ALERT, Hidden, Marked, Aim and sustained skill effects, retain existing Stress and drop mission objects. Stress is ignored while Down or Unconscious; it is not removed by going Down. Down cannot control or contest. A Down unit cannot crawl or revive itself. Revival requires a teammate. It becomes Unconscious at the End Phase two rounds after going Down; Unconscious cannot act or be revived that battle. Ranged attacks against a visible Down unit suffer −2 to hit. This is the same condition penalty used by card 20, applied once: with heavy cover the total is −6. Contact melee attacks against a Down unit cause one automatic hit; an Injury success makes it Unconscious, never dead. Down and Unconscious bodies do not block movement or LOS. Further attacks on Unconscious have no extra effect.

## 35 Treatment and revival

**Current rule:** A conscious unpinned unengaged fighter in contact spends Core and one medkit to test INT on a Down friendly. Success restores one Wound, clears morale and leaves the patient Pinned at 2 Stress; failure spends the Core action and medkit and makes the patient Unconscious. Down fighters cannot revive themselves; revival requires a teammate. One successful revival per fighter per battle. Revival never restores spent slots or removes an old lasting injury; unused Move can stand and unused Core remains usable after recovery.

## 38 Stress Break and forced flight

**Current rule:** Stress is 0–5. Each successful hit adds 1 Stress during the hit-roll phase, before Injury is resolved. Injury rolls add no further Stress. Stress remains on the unit but is ignored while Down or Unconscious. The first visible friendly Down within 6 inches each round adds one witness Stress to eligible conscious fighters. Subtract Stress from ordinary stat tests and attack totals, not fixed MOVE, Injury, initiative or distance. End Phase fighters at 2+ Stress without a morale condition test d20 + NRV − Stress against 13+. Success clears Stress. Failure at 1–2 gives Broken and Pinned; at 3–4 Bolting; at 5 Bugging Out. A Broken unit drops to the ground and cannot take actions until its Stress reaches 0, except its Core self-Rally under card 39. On its next activation, a Bolting unit spends that activation's actions moving up to twice MOVE toward safety outside enemy LOS; Bugging Out instead moves toward the nearest reachable board edge. A condition gained in the End Phase grants no immediate movement or extra actions. Conditions stop reactions, assistance, scoring and contesting. Forced movement occurs at most once per round and gives no fresh activation. Fleeing is withdrawal, not injury.

## 39 Rally

**Current rule:** A fighter already under a morale condition at End Phase start makes Rally instead of Break. A test of d20 + NRV − Stress against 13+ clears morale and all Stress on success, leaving the rallied unit Pinned; failure retains the condition. A fresh Break failure does not immediately Rally again. Core Rally targets self or a friendly within 3 inches and LOS; an assisting fighter must be conscious, unpinned and unengaged. Pinned or Broken fighters may self-Rally; Bolting and Bugging Out need help or End Phase Rally.

## 40 Hidden and Observe

**Current rule:** Hide is a Core action. A unit may Hide only while unengaged and outside every enemy's LOS. No test is required. Position remains public. Sneak permits movement up to half MOVE while retaining Hidden. Normal Move, Sprint, Charge, shooting, loud interaction, engagement or a hit removes Hidden unless a stated exception applies. At own action start and end, exposed LOS within 12 inches reveals; enemy proximity within 3 inches and LOS reveals immediately. Beyond 12 inches Hidden normally cannot be targeted; within 12, legal shots take −4 plus cover. Core Observe tests INT against one Hidden enemy or concealed device within 12 inches and forward LOS. Success reveals the target but grants no accuracy bonus. Mark Target is a separate skill and follows its own duration and effects.

## 41 Interact and stat examples

**Current rule:** Core Interact normally needs base contact and no engagement. Trivial operations are automatic. Difficult, contested or dangerous work uses the appropriate ordinary stat test. An operation threatening an occupied space requires an operator test, followed by the feature's stated escape chance. STR forces, DEX manipulates and disarms, INT hacks and repairs, AGI traverses and evades, NRV handles composure. Failures use the printed consequence; no variable difficulty scale.

## 42 Hacking terminals and repair

**Current rule:** Anyone can use a terminal; every feature also has a physical control. A terminal links up to three features within 18 inches, without chaining. Shared links define Interrupt networks. Contact Core Hack tests INT to operate one linked feature; failure changes nothing, natural 1 Freezes that terminal until round end. A hacking kit also enables visible device hacking within 8 inches, disabling the target until Repair; kit natural 1 prevents further kit use that round. Trojan hijacks and Interrupt opposes. Contact Core INT Repair restores Offline or disabled electronics, not Destroyed devices. Critical terrain and objective terminals cannot simply be shot away.

## 43 Improvised actions

**Current rule:** Before committing, agree the object, intended effect, cost, stat and failure. Movement costs Move, another task Core, a combined movement and task Both. Prefer existing operations and plausible ordinary human capabilities. If agreement stalls, use the nearest printed action for that battle.

## 44 Shared terrain operations and hazards

**Current rule:** Each feature identifies footprint, controls, terminal link, states, operation and hazard area. Displace moves a model by the shortest safe distance up to 2 inches; without a safe position the operation stops unless Crush applies. Crush lets conscious targets test AGI to escape; failure or no safe destination causes one Damage 4 Injury ignoring Armour, then Pinned if conscious. Move casualties to an accessible edge; Down can become Unconscious, never battlefield dead. After resolving Crush, automatically push the affected model clear of the crushing terrain or machinery. Smoke uses a 5-inch-diameter template extending upward to unlimited height. It blocks LOS through the smoke between units outside it. When a unit inside the smoke shoots a target outside, treat the target as in Heavy cover. A unit inside the smoke is treated as in Heavy cover when shot at. Fall and Difficult use their shared rules.

## 46 Deploying revealing disarming and damaging devices

**Current rule:** Core Deploy places in contact with no base overlap and away from occupied objective markers. Barricades and ladders are automatic; mines, traps and electronics test INT. Failure leaves an inert visible device and allows later retry. Armed devices do not trigger on models already in their trigger area, but later movement can trigger them. No action on the deployment turn except passive smoke or cover; turrets first gain ALERT next Start Phase. Concealed payload type is secret, marker location public. Observe, triggering or approach within 2 inches and LOS reveals. Declare a disarm attempt before entering the device's trigger area; approaching for that attempt does not trigger it before the test. In contact, spend Core and test INT to Disarm: success makes the device inert; natural 1 triggers it. One hit makes standing equipment Offline, a second Destroyed; armed mines and traps are ruined without explosion, drones destroyed by the first hit. Both crews trigger devices.

## 47 Sentry turret

**Current rule:** A turret has no normal slots. It follows card 17's reaction rules using its own LOS, including Return Fire if targeted. Other eligible units may also react to the same enemy. Core operation from contact or a hacking kit within 8 inches turns facing. The turret fires only through ALERT reactions; firing spends turret ALERT and marks Reacted. It cannot fire without ALERT or attack twice in the round. Friendly operation is automatic; enemy use needs Trojan.

## 49 Utility drone

**Current rule:** Deploy automatically with operator Core. On a later activation one Core moves it up to 8 inches; a separate Core in another activation performs an operation. Stay within 12 inches of the operator and up to 6 inches above the surface below. The drone has a 360-degree camera and real-height LOS. It can use a contacted terminal, Observe within 12 inches or operate a contacted terrain control with the operator's INT and Stress. Operator must be conscious, unpinned, unengaged and without morale conditions. It cannot replace human objective, loot, capture or mission-cargo actions. Remote commands offer one reaction window against operator or drone. The drone is destroyed if it leaves the operator's control range or the operator becomes Down. Other loss of control leaves it inert. Friendly contact Core can transfer control with two free equipment slots; spend a Core action to remove the drone. One hit destroys it, leaving a recoverable wreck.

## 50 Equipment profiles and provisional prices

**Current rule:** Dice sets the attack pool, Damage changes Injury, Range sets reach, Slots determine carried capacity under card 9, and Access governs purchasing or crafting. Ignore all existing Credit costs during catalogue review. Rebuild costs for the entire game after the updated rules and catalogue profiles are settled; old prices are historical reference only. Reload costs Core and readies one unloaded Reload weapon. Prior simulations do not establish these profiles' balance.

## 51 Area attacks smoke and fire

**Current testing rule — updated 26 October 2026:** Choose a visible Blast impact point within weapon range, on a flat surface or a model, including a friendly model. Roll one normal shooting test for the shot. On a hit, leave the template at the chosen point; on a miss, scatter it a random direction by d6 inches. Blast normally uses a 3-inch-diameter circle, or 5 inches when the source specifies it. Affected models within the template's footprint and 3 inches above or below it are automatically hit, including friendlies. Solid obstacles and intervening floors block the blast; it cannot wrap around corners. Roll Injury for affected fighters using the source's Damage and applicable effects; devices use their hit-based damage rule. Do not roll a separate hit test for each affected model. Damaging thrown grenades cost Core Shoot and use the attack allowance. Smoke instead costs non-attack Core Use Item and a DEX test within 8 inches: success places a 5-inch-diameter circle, failure places it 2 inches nearer along the line, stopping at obstruction. Smoke expires at the end of the round. Fire bottle also leaves a 3-inch fire zone regardless of hit rolls; entry or action-start exposure gives Damage 2 Injury, once per round including its initial attack, through next round's End Phase. Fire is cleared by contact-edge Core INT Interact or automatically by extinguisher.

### Cone

Place the narrow end of an **8-inch teardrop template** against the firing fighter's forward base edge. Aim it in the direction of the attack; it may be angled up or down. Hold it above the models to check coverage: any model wholly or partly beneath its footprint along the direction aimed is **automatically hit**. The flame does not pass through walls or other solid terrain. Resolve Injury with the source's Damage and applicable effects; devices use their hit-based damage rules. Cone does not roll to hit or Scatter. A source leaves a persistent fire zone only if its profile explicitly says so.

## 57 Choosing and using skills

**Current rule:** The catalogue contains 39 skills. Card 7 supplies the agreed skill-allocation rule: each complete two points in a Stat grants one associated skill, up to three in that Stat at +6; Recruits and Fighters start with none. Count each Stat separately, using allocated Stats before lasting injuries. There is no overall three-skills-per-fighter cap, no skill tiers, and no duplicate copies of a skill. If a skill requires an action, its description states the cost. Passive skills require no action.

<!-- conditions-reference:start -->
## Conditions referenced

[[Settlements/Rules System/Second Draft/Conditions Reference#^condition-hidden|Hidden]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-marked|Marked]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-pinned|Pinned]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-down|Down]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-unconscious|Unconscious]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-stress|Stress]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-broken|Broken]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-bolting|Bolting]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-bugging-out|Bugging Out]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-engaged|Engaged]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-captured|Captured]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-alert|ALERT]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-aim|Aim]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-reacted|Reacted]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-out-of-action|Out of Action]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-concealed|Concealed]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-armed|Armed]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-disarmed-or-inert|Disarmed or Inert]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-offline-or-disabled|Offline or Disabled]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-frozen|Frozen]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-destroyed|Destroyed]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-loaded-or-unloaded|Loaded or Unloaded]] · [[Settlements/Rules System/Second Draft/Conditions Reference#^condition-retired-or-dead|Retired or Dead]]
<!-- conditions-reference:end -->

## Grapple family update — 10 November 2026

[[Settlements/Design Workshop/Skill Compatibility Review - 2026-11-09/STR - Grapple Hauler Carrying Throw - 2026-11-10|10 November Grapple, Hauler, Carrying and Throw decisions]] supersedes the earlier Grapple, Strong Arm and Throw recommendations. Strong Arm is now Hauler. Grappling permits the stated one-handed weapon use; Hauler permits non-Heavy two-handed weapons while Grappling.
