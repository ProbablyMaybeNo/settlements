---
type: master
version: 2.0 working manuscript
status: Complete rules proposal for review and playtesting
created: 2026-10-17
authority: Ross core tenets and completion brief of 2026-10-17
---
# Settlements Rules System Version 2

Settlements is a skirmish game about ordinary people fighting over the things their community needs. Cover a friend's advance, open a route through a building, shut down an enemy device, recover someone who has fallen, and get the job done. Your settlement and its people continue from one battle to the next, whether or not you play a campaign.

> [!info] Working edition
> This is the complete proposed rules text for Version 2. New and revised mechanics, catalogue costs, and progression rates await playtesting. A familiar game of six rounds with 5–10 fighters per side aims for about 60 minutes; that duration has not yet been demonstrated. Design decisions and research evidence are kept in [[Draft 2 - Design Requirements and Research Audit]], outside the playing rules.

## Contents

1. [[#1 Introduction and the world]]
2. [[#2 What you need and how to read the rules]]
3. [[#3 Fighters and tests]]
4. [[#4 Building and equipping a crew]]
5. [[#5 Preparing the battlefield]]
6. [[#6 Rounds actions and reactions]]
7. [[#7 Movement facing and visibility]]
8. [[#8 Shooting and close combat]]
9. [[#9 Injury casualties and rescue]]
10. [[#10 Stress and morale]]
11. [[#11 Stealth and observation]]
12. [[#12 Interaction hacking and improvised actions]]
13. [[#13 Interactive terrain catalogue]]
14. [[#14 Deployables and drones]]
15. [[#15 Weapons armour and equipment]]
16. [[#16 Skills]]
17. [[#17 Objectives and building a mission]]
18. [[#18 Ending a battle and lasting injuries]]
19. [[#19 Experience and advancement]]
20. [[#20 Founding and running a settlement]]
21. [[#21 Settlement structures]]
22. [[#22 Worked examples]]
23. [[#23 Roster sheets and reference]]
24. [[#24 Campaign and scenario content]]

## 1 Introduction and the world

### The kind of game you are playing

The core rules are shared across the game. A difficult task uses the same test whether you are climbing a wall, treating a casualty, or hacking a terminal. The depth comes from where you stand, which action you spend, what the terrain can do, and what your opponent can threaten.

Every fighter is human. Training offers better judgment and useful techniques; it does not make someone bulletproof. A fighter has one Wound. One successful Injury roll puts them Down. They remain on the battlefield and may be rescued, looted, or captured.

Victory comes from the mission's primary and secondary objectives. Shooting helps secure a route, suppress a threat, or protect an interaction. Causing casualties earns no victory points by itself.

### Lore and setting

**[PLACEHOLDER — setting, history, locations, factions, illustrations, and introductory fiction.]** The rules assume near-future civilian crews, ordinary firearms, improvised equipment, electronic controls, and small utility drones. Faction identities do not change these rules until a later published module supplies an explicit rule.

### Persistent play

Keep a Settlement Roster containing everyone and everything you own. Before each battle, select a Battle Roster up to the Crew Rating agreed with your opponent. A large settlement gives you more choices; it never increases that agreed limit. Named fighters gain experience and injuries, while the settlement produces resources and unlocks equipment.

A campaign may connect battles through a story or map. It is not required for any of this progression.

## 2 What you need and how to read the rules

### Components

The standard game has two players. Each player needs 5–10 human miniatures for a starting crew, a roster, several d20s, one d6, an inch measure, and markers. Use a 36 × 36-inch battlefield, terrain, and a round counter numbered 1–6. Larger crews are legal by agreement but increase play time.

Use the same base size for comparable humans, normally 25–32 mm, and mark the front half of each base. Agree proxies and unusual sizes before deployment. A tall pose, banner, or weapon barrel does not make a fighter easier to see. Paper footprints can represent every interactive feature in this book.

Mark a fighter's unused **Move** and **Core** slots on its card. Useful table markers are READY, Reacted, Pinned, Hidden, Stress 1–5, Down with the round number, Unconscious, Captured, Marked, and a carried objective. Put spent item charges and once-per-battle abilities on the card. A single marker may show a fighter's current morale condition; do not add a second Shaken marker.

Use circular templates with **2-inch radius** for blasts and **3-inch diameter** for smoke, fire, and gas. Radius and diameter are deliberately different: label the templates. Use a 1-inch marker for a terminal, objective, or mine.

### Common conventions

- **Round:** both crews use their available actions, then resolve the End Phase. **Turn:** one player's opportunity to take one action. An action and its consequences finish before the other player's turn.
- **Within:** the shortest distance between bases is no greater than the stated distance. Base contact means touching; floors must also match unless a rule says otherwise. Engagement is within 1 inch on a reachable surface.
- Measure movement along the path actually travelled, using the same point on the base throughout. You may premeasure. A unit cannot move through a solid wall, another standing unit's base, or a gap its base cannot fit through.
- **Friendly** includes the acting fighter unless the rule says “another.” **Enemy** means the opposing crew. A **fighter** is a human model. A **device** is equipment, not a fighter.
- Fractions are rounded down unless the rule specifies otherwise. Never reduce an ordinary attack pool below one die. Reroll a die at most once and keep the new result.
- Identically named effects do not stack. Specific printed exceptions override the general procedure, but never the limits of one reaction per fighter per round, one reacting model per action, or the prohibition on reactions triggering reactions.
- Declare choices, targets, weapon allocation, and any conditional bonuses before rolling. If an action becomes impossible after a reaction, its slots and declared consumables are still spent.
- A displaced model returns to its agreed position. Reroll a cocked or off-table die. Agree the intended legal position before moving a model onto unstable scenery, then mark that position safely.

## 3 Fighters and tests

### The profile

| Characteristic | Meaning |
| --- | --- |
| STR | Strength, force, and ordinary melee attacks |
| DEX | Shooting, precise manipulation, and disarming |
| AGI | Climbing, jumping, balance, and Agile melee |
| INT | Hacking, repair, medicine, and technical work |
| NRV | Courage, recovery under pressure, and leadership |
| MOVE | Inches travelled with a Move; normally 6 |
| Wounds | Normally 1, with a maximum of 1 for human fighters |
| Armour | Protection supplied by equipment; normally 0–2 |

Stats range from 0 to +6. Zero represents no particular training under combat pressure, rather than an inability to perform ordinary daily tasks. A task without meaningful difficulty or danger succeeds without a test.

### Ordinary tests

Roll **1d20 + the relevant stat + modifiers − Stress**. A total of **15 or more succeeds**. Natural 1 always fails; natural 20 always succeeds. The action says what failure does. Do not add a difficulty scale: a task is automatic, a normal test, or impossible with the available tools and position.

For any roll, use only the **largest positive and largest negative modifier from skills**, and likewise the largest positive and negative modifier from equipment characteristics. A skill modifier cannot exceed 4; an equipment characteristic modifier cannot exceed 3. Add these to the stat and applicable position modifiers. Cover is either 0, −1, or −2, never both cover grades. Pinned, Hidden, rear attacks, Aim, and Stress have their own stated effects and apply once each. The Pinned target modifier stacks with applicable cover and rear modifiers; it changes hit rolls, not Injury rolls. Identical effects still never stack.

Printed weapon Damage and Armour are profile values, not equipment characteristic bonuses. Injury rolls have their own formula in Chapter 9 and **do not subtract Stress**. Break and Rally ignore Stress. Distance rolls, initiative, and post-battle tables are not stat tests and ignore Stress too.

**Example:** an INT 3 fighter at Stress 1 hacks using a +2 hacking tool and a +2 skill. Their total is d20 + 6. A second +2 hacking skill would not increase it again.

### Single opposed tests

Each side rolls one d20 with the specified stat and ordinary modifiers. The higher total succeeds; ties favour the defender. A natural 20 beats a non-20 and a natural 1 loses to a non-1. Two natural 20s or two natural 1s are ties. There is no additional 15+ requirement. Grapple and Interrupt use this procedure.

### Opposed attack pools

Melee compares attack pools rather than single tests. The complete procedure is in Chapter 8. Do not pair dice, subtract enemy stats, or count ordinary 15+ successes in a melee exchange.

## 4 Building and equipping a crew

### Credits and Crew Rating

Agree the scenario and maximum Crew Rating before choosing your Battle Rosters. **750 Credits** is the recommended starting limit. About **1,000 Credits** supports a broader starting crew. These are playtest defaults; either limit can be changed by agreement.

Your Crew Rating is the current Credits value of every fielded fighter, all carried weapons, armour, equipment, devices, and battle preparations. Count reserves and carried drones too. Gear in storage, workers left at home, Credits in the treasury, and settlement buildings do not count. A discount, gift, crafted item, or stolen item still counts at its **full listed value** when fielded.

Credits are the purchasing currency and the unit of Crew Rating. Materials build structures and are not a second battle budget. Experience earns improvements; it cannot buy equipment or be exchanged for Credits.

### Recruitment

Pay the listed Credits from your treasury. Allocate the stat points once at recruitment, starting all five stats at 0. Each +1 costs one point. Observe the starting maximum for any single stat. Unspent points are lost; they cannot be banked. Every fighter begins with MOVE 6, one Wound, Armour 0, ordinary clothing, and a utility knife included in the body cost.

| Training grade | Credits | Stat points | Starting stat maximum | Starting skills |
| --- | ---: | ---: | ---: | ---: |
| Recruit | 60 | 3 | +2 | 0 |
| Fighter | 80 | 5 | +3 | 1 |
| Specialist | 110 | 7 | +4 | 2 |
| Leader | 130 | 9 | +4 | 2 |

These grades describe experience and responsibility among civilians. They do not grant extra Wounds or extra actions. Choose skills from Chapter 16; each requires at least +2 in its listed stat. A fighter can know at most three skills. Skills included in a training grade do not cost additional Credits.

### Composition

Nominate one fielded fighter as the crew leader for tie-breaking and narrative records. They need not have the Leader training grade; acting leadership grants no stat or action bonus. A crew may include at most one fighter with the Leader grade and one Specialist for every two fielded Recruits or Fighters. Advancement does not change training grade or this ratio through experience; this edition has no grade-promotion purchase.

For each complete five human fighters in the Battle Roster, you may field one Heavy weapon and one powered combat device in total; a sentry turret is a powered combat device. You may also field one utility drone per complete five fighters. A crew below five may field one utility drone but no Heavy weapon or powered combat device. These limits count carried, deployed, and reserve items together. Mines and smoke emitters are not combat devices for this limit.

Use 5–10 fighters for the first games. More are allowed when the agreed limit and terrain support them. The rules do not grant a bonus for spending the limit exactly.

### Carrying equipment

A fighter has **four weapon slots**, **two equipment slots**, and may wear **one armour item**. A one-handed weapon uses one weapon slot; a two-handed weapon uses two; a Heavy weapon uses three. The included knife uses no slot. A grenade uses one equipment slot rather than a weapon slot. Other equipment lists its slots. A fighter may use only two hands at a time. Weapon slots hold weapons, equipment slots hold supplies/devices; worn armour uses neither. Carried devices continue to reserve their operator's equipment slots after deployment until lost, consumed, or transferred, so deployment does not create extra capacity.

Choose held weapons at the start of your fighter's first action or reaction each round. Once during a later own action that round, you may change held weapons before resolving it. You cannot switch in response to an enemy declaration after that round's choice. A carried but unheld weapon contributes no attack dice.

Any human can use a pistol, rifle, shotgun, or ordinary melee weapon. Heavy weapons require Specialist or Leader grade, or Level 6+. An item still needs its settlement unlock to be purchased or crafted. Loot may be used without the purchase unlock if the fighter meets the handling requirements.

### A recovery floor

If losses or recovery leave you unable to field five available owned fighters, you may borrow enough **Relief Volunteers** to reach five. Each uses the Recruit profile, has STR 0, DEX 1, AGI 1, INT 0, NRV 1, and carries an included knife and pistol. Each counts **75 Credits** toward the agreed limit. They cost no treasury Credits, gain no experience, work no structures, and return with their equipment after the battle. Loaned equipment cannot be traded, looted into permanent ownership, or sold. Volunteers may carry objectives and perform ordinary actions.

Relief is a way to keep playing after losses, not an addition above the battle limit. If even that roster exceeds the agreed limit, agree a higher limit or a smaller scenario before deployment.

## 5 Preparing the battlefield

### Setup sequence

1. Agree the scenario, Crew Rating, and any explicit changes to the six-round format.
2. Build the battlefield, identify terrain and controls, and place objectives.
3. Select and reveal Battle Rosters, including skills, carried devices, reserves, and preparations.
4. Roll a d20 each; the higher chooses a deployment zone, the other deploys the first fighter. Reroll ties. Alternate placing one fighter at a time.
5. Begin round 1. Unless a scenario says otherwise, deploy within 6 inches of opposite edges. Reserve entries must be stated by a rule; nothing may simply start off-board.

### A table that supports the game

Divide the board mentally into nine 12-inch squares. Place a substantial building, wall arrangement, or other LOS blocker in each square, then add scatter and cover. Start with **9–12 substantial features**, counting a connected building as one feature. This is a layout guide, not a fixed balance guarantee.

Provide at least two covered routes out of each deployment zone, at least two approaches to each primary objective, and a central LOS blocker. Neither deployment zone should have a direct ground-level firing lane into the other. Avoid both an empty killing ground and an unbroken maze of sealed rooms. Include useful gaps, flanks, and at least one elevated route with accessible stairs or ladders.

Add **four interactive features beyond ordinary doors**, using at least three different operations from Chapter 13. At least two must change routes or visibility around objectives. Provide at least two terminals, each linked to one or more of these features. Place controls so both crews can reasonably reach them. Mark all links openly. No hacking-only objective is required in the standard mission builder.

Agree what each piece represents: its footprint, height, cover grade, climbable faces, doors, controls, movable sections, and any hazard area. Declare moving terrain's allowed positions before deployment. Tokens and printed cards are sufficient; players do not need specialist scenery.

### Cover and solid terrain

Soft foliage, mesh, or thin scatter provides **light cover: −1 to shooting**. Masonry, substantial barricades, vehicle hulls, and thick machinery provide **heavy cover: −2**. Solid opaque terrain can block LOS entirely.

A target has cover when an intervening feature obscures part of its agreed body volume from the attacker's viewpoint. The target must be within 1 inch of the feature, or inside an agreed area of cover. Intervening distant clutter that does not block LOS gives no cover modifier. Ignore a low obstacle within 1 inch of the shooter when shooting over it. Use only the strongest applicable cover.

Height gives a better view, not an automatic accuracy bonus. If an elevated attacker can see over the actual protecting surface, that surface supplies no cover. A wall still blocking the target's body continues to protect it.

## 6 Rounds actions and reactions

### Start Phase

Advance the round counter. Restore each conscious, uncaptured fighter's Move and Core slots. Down fighters also receive those slots but can use only the limited actions in Chapter 9. Unconscious fighters receive neither. Clear Reacted markers and reset once-per-round abilities. READY tokens remain until used or cancelled.

Each player rolls a d20; higher chooses who takes the first turn this round, with ties favouring the player who did not take the first turn last round. Reroll a round-1 tie.

Count each crew's available action slots after deployment and conditions. The smaller total receives **Passes equal to half the difference, rounded up**. One Pass spends a turn without acting. Passes last only this round. They compensate for some timing advantage, not missing fighters or combat power.

### Alternating actions

On your turn, choose one fighter with a legal unused slot and perform one action. Mark the slot spent before resolving reactions. Play then passes to the opponent. You may return to that fighter on a later turn to spend its other slot. There are no consecutive full-unit activations.

An action costing **Both** spends the fighter's unused Move and Core together. If either is already spent, it cannot perform that action. Each fighter has one Move Action for its own movement and one Core Action for other tasks. Standing up from Pinned uses Move instead of travelling. Neither slot converts into the other, and skills do not grant a second Core Action. There is no limit on which fighter you choose except its slots and state.

You may spend a Pass instead. Without a Pass, you may only pass if you have no legal action you wish to retain: mark all your remaining slots spent. If one crew has finished, the other completes its actions, still allowing reactions. Once both have finished, resolve the End Phase.

### Action reference

| Action | Cost | Main effect |
| --- | --- | --- |
| Move | Move | Travel up to MOVE and choose facing |
| Recover (stand up) | Move | Remove your own Pinned instead of travelling; Core remains available if unused |
| Aim | Core | Prepare +2 on your next Shoot, lasting through the end of next round; lost if you move or become Pinned first |
| Dash | Both | Move up to twice MOVE; no attack |
| Charge | Both | MOVE + d6, then one melee exchange if successful |
| Shoot or Fight | Core | One attack using Chapter 8 |
| Ready | Core | Gain one READY token |
| Help Recover | Core | Help a friendly within 3 inches and LOS remove Pinned |
| Rally | Core | Test NRV to clear Stress and a morale condition on yourself or one friendly within 3 inches and LOS |
| Hide or Observe | Core | Use the stealth rules in Chapter 11 |
| Interact or Hack | Core | Operate one control, objective, or device |
| Deploy or Repair | Core | Place or restore one carried device |
| Treat or Use Item | Core | Use a medkit or another printed equipment effect |
| Loot or Secure | Core | Take an item or capture an incapacitated enemy in contact |
| Reload | Core | Ready a weapon with Reload to fire again |
| Disengage | Both | Leave engagement by the procedure in Chapter 7 |

A fighter may perform at most **one own-turn attack action** each round: Shoot, Fight, or Charge. A reaction attack is separate. Defensive melee participation is not an attack action. Skills may combine movement and a Core task by spending both slots, but cannot turn Move into another Core or create an extra own-turn attack. Any own action directly attacking a fighter—including Shove, Grapple, Throw, Incapacitate, or a damaging grenade—uses the own-turn attack allowance. Firing a turret through an operation or Trojan also uses the operator's allowance. Terrain operations and deploying devices remain interactions, even if their hazards threaten enemies; they do not grant a second direct attack.

### READY

Ready grants one token, never a second. It can be gained after spending Move and can remain into later rounds. A fighter loses READY when it moves voluntarily, performs any regular action other than Ready, is hit by an attack, becomes Down or Unconscious, is captured, or gains a morale condition. A stationary free facing change made as part of another action does not save READY from that action's cancellation.

A conscious, unengaged fighter with READY, no morale condition, and no Reacted marker may react. It must see the triggering enemy in its forward arc at the moment of the trigger, within the relevant action's range. Pinned fighters can only use the Dive reaction, and only if they somehow retained READY through a specific skill.

### Reaction windows

After an enemy declares an action, the non-active player may declare **one reaction by one model**. Alternatively, they may wait for a visible point along a declared movement path or the end of the action. Announce the precise point before the model moves past it. The entire action, including a Charge's movement and attack, allows only one reacting model, even if several are eligible.

For an incoming Shoot, Return Fire, Dive, or Cover Me must be declared before any attack dice are rolled. Waiting until its end does not permit retroactive fire or evasion. An ordinary reaction Shoot is available only against a non-shooting action; Cover Me supplies the exception for protecting another target.

Spend READY immediately and mark Reacted. No reaction triggers another reaction. Devices' automatic mine triggers are hazards, not reactions; a sentry turret's shot is a reaction and uses the same one-model limit.

| Reaction | Resolution |
| --- | --- |
| Shoot | Fire at the triggering enemy using the normal shooting rules. Resolve before the declared non-shooting action or at the chosen movement point. |
| Return Fire | If the triggering enemy is shooting you and is a legal target, both shoot using normal 15+ shooting tests. Resolve both attacks from the positions and states at declaration, then apply both sets of outcomes. |
| Dive | Before an incoming shot or Charge, test AGI. Pass: move up to 3 inches to a legal position and become Pinned; fail: stay and become Pinned. Recheck the declared attack's range and LOS. This is diving before the shot, not dodging a bullet already rolled. |
| Operate | Use a control or terminal you can currently reach. Resolve one legal terrain operation before the trigger completes. |
| Interrupt | Requires the Interrupt skill and uses its opposed test. |

A hit that Pins or Downs the acting fighter cancels its unfinished action and consumes the slots spent. If a moving fighter is interrupted, it stops at that point. A cancelled Charge has no attack. An operation that closes a route stops movement at the obstruction; it does not allow the remaining distance to pass through it. A simultaneous Return Fire exchange is completed even if one shooter is Downed by that exchange.

### End Phase

1. Finish any effects explicitly due at the end of the round; the first player resolves their crew's effects first if order matters.
2. Check Down timers and turn overdue casualties Unconscious.
3. Resolve one Break or Rally test per eligible fighter as described in Chapter 10.
4. Score objectives due this round. Clear temporary effects whose duration is “this round,” including Passes. Remove unused Aim when its stated duration ends. Resolve smoke, fire, and gas expiry.
5. Check the scenario's end condition. A standard battle ends after round 6.

## 7 Movement facing and visibility

### Facing and LOS

A fighter sees through the **forward 180 degrees** of its base. Draw the dividing line through the base centre; a target whose centre lies exactly on that line counts as in the forward arc. The rear half is outside LOS. A fighter may change facing freely during its own movement and once at the start of its own Core Action. Facing does not change for free during an enemy turn or after an attack is declared.

Agree a normal human silhouette as a cylinder above its base, approximately 2 inches tall. Check LOS from the acting fighter's eye point to the target's head or torso volume; ignore decorative parts. A sliver of weapon, scenic base, or clothing is not enough. Solid walls block sight. Other standing fighters' base-width body volumes block sight, including friendly fighters. For shooting into engagement, use Chapter 8.

Pinned, Down, and Unconscious models use their **base footprint** as the visible target instead of the standing figure. If the attacker cannot see any of that base footprint, it cannot shoot the prone fighter. Area hazards can still reach it. A Pinned fighter checks sight from ground level when it needs LOS for a permitted action. This convention also applies while crawling.

An attack declared from wholly behind the target's dividing line is a **rear attack**. It gains +2 to hit. The target cannot react to that attacker through its rear arc. Close-combat defence and rear charges are resolved in Chapter 8.

### Ordinary movement

Move up to MOVE along a legal path. You may stop early. A normal Move cannot enter within 1 inch of a conscious enemy, including a Pinned one; use Charge instead. You may pass within 1 inch of Down or Unconscious enemies and enter contact to rescue, loot, or capture them.

Cross an unlocked ordinary door as part of movement; opening it is automatic. Closing it deliberately is an Interact. A low obstacle up to 1 inch high costs 2 inches of movement to cross. Difficult ground costs twice the distance travelled. Movement penalties do not multiply: half-speed movement and difficult ground together still halve available movement once. Heavy carrying also uses this rule.

### Dash and Charge

Dash spends Both slots and moves up to twice MOVE. Hidden fighters cannot Dash without first removing Hidden.

Declare a Charge against one visible conscious enemy within **MOVE + 6 inches**, along a plausible route. Spend Both slots, roll one d6, and move up to MOVE plus that result. Reach within 1 inch of the target to succeed; resolve one melee exchange with +1 die on the dominant weapon, within the three-die pool ceiling. On failure, move up to MOVE toward the target along the declared route, stop outside engagement, and end the action. Stress does not alter distance, but applies to any traversal tests and the attack.

You may attempt a risky route as part of a Charge. Resolve its tests at the relevant point. A failed traversal ends the Charge, even if its distance roll was sufficient. A reaction can likewise stop it. Charge does not let a fighter pass through other standing fighters.

### Climbing jumping and falling

Stairs, ladders, and stable ramps use measured movement without a test. Free climbing needs handholds or climbing gear, costs double the vertical distance, and requires one AGI test per action. A failed climb stops at the starting level; natural 1 causes a fall from halfway up the attempted climb. You cannot free-climb a smooth wall without appropriate equipment.

Step across a gap up to 1 inch as normal movement. A gap over 1 and up to 3 inches requires enough movement to reach the other side and an AGI test. Failure means falling into the gap. Wider gaps need a bridge, equipment explicitly permitting the crossing, or a different route. No skill increases the maximum unsupported jump beyond 3 inches.

A deliberate drop of up to 2 inches is safe and costs its vertical distance. For a greater drop or an involuntary fall of more than 2 inches, test AGI: pass and land Pinned; fail and suffer one Damage 3 Injury roll ignoring Armour, then become Pinned if still conscious. Falls over 6 inches automatically fail that AGI test. A fall never kills a fighter on the battlefield. Place a Down casualty at the reachable bottom; if inaccessible, mark its position at the rim and treat it as Unconscious until recovered after the battle.

### Forced movement and carrying

Pushes and pulls follow the shortest stated direction. Stop at an immovable obstruction or another standing base; excess distance is lost. A ledge or open pit is a hazard, not a wall: use the fall rules. A move cannot end with overlapping bases. If terrain closes on a model, use the feature's Displace or Crush rule.

Dragging a casualty, escorting a captive, or carrying a Heavy objective halves movement, prohibits Dash and Charge, and occupies one hand. Two unengaged friendlies in contact can jointly carry one casualty: one spends Move, both use their Move slots, and both move together up to the slower fighter's normal MOVE. This is one combined action and one reaction window; either carrier may trigger it. If either is Pinned or Downed, the movement stops and they release the casualty. Taking hold of a friendly casualty in contact is part of the carrying Move, with no extra action. An enemy casualty must first be Secured. A carrier may drop a load without a test at any time during its own action.

### Engagement and withdrawal

Engaged fighters may Fight, Grapple, use a Sidearm in that melee exchange, Recover, Rally themselves, or Disengage. They cannot shoot someone outside the engagement, operate a terminal, Treat, or manipulate an objective. A Pinned fighter is still engaged if an enemy is within 1 inch.

Disengage normally spends Both slots. Test AGI opposed by one engaging enemy's AGI, chosen by the opponent. Pass: move up to MOVE and leave engagement. Fail: move up to half MOVE after that enemy makes one Unanswered melee exchange against you; cancel movement if you become Down. The free exchange is not a reaction and cannot trigger follow-up attacks. Pinned fighters may attempt Disengage and retain Pinned; their movement is at most half MOVE on either success or failure, without halving twice. Any forced Bolt or Bugging Out movement also allows one such Unanswered exchange, then the survivor moves without an escape test.

Within engagement, a fighter may spend Move to shift up to 1 inch around an enemy, remaining engaged and not entering another enemy's engagement. It cannot cross the enemy base. Both may face each other after a completed melee exchange.

## 8 Shooting and close combat

### Shooting

Choose held weapons and one legal target in the shooter's forward arc, within weapon range and LOS. Declare dice and any optional effects. Roll **1d20 + DEX + modifiers − Stress** for each Attack Die; each 15+ is a hit. Natural 1 misses and natural 20 hits. Apply −1 or −2 for cover, **−2 if the target is Pinned**, −4 for Hidden when the target is legally visible, +2 for a rear attack, and +2 for a retained Aim. Each hit then makes an Injury roll.

Aim costs Core and gives +2 to the next Shoot, including a shooting reaction. It lasts through the end of the following round, but is lost earlier if the fighter moves, stands up, becomes Pinned, or enters engagement. Apply it to the whole shot, then remove it. Repeated Aim does not stack.

There is no long-range penalty within a weapon's printed range. There is no generic penalty for moving. You cannot shoot beyond range or through solid terrain. Premeasure before spending the action.

A normal Shoot targets one fighter. Split Fire permits allocation to several targets as described in its skill; declare every die's target first. A firearm with three dice does not attack three targets automatically.

### Two weapons and pool limits

Using two one-handed weapons gives the dominant weapon's full dice and **one off-hand die**. Identify that die separately and use its own range, Damage, and traits. Both weapons must be eligible for the attack. A shooting pair must contain two firearms; a melee pair may contain melee weapons or Sidearms. Skill exceptions never raise a combined attack pool above **three dice**, including a Charge die. Remove excess dice of your choice before rolling.

A fighter with no eligible held melee weapon may always use one unarmed die at Damage 0. A fighter with only its included knife makes one melee die at Damage 1. Unarmed attacks make one die at Damage 0. A Sidearm may contribute one melee die, using STR to hit and its printed Damage. It does not use DEX in melee. Sidearm shots in melee still require a loaded weapon and use Reload normally; a two-handed gun without Close Combat cannot contribute its shooting pool.

### Shooting into an engagement

You may shoot an enemy engaged with your friendly fighter, but each natural 1 in that attack pool hits one friendly involved instead, chosen by the opponent. Resolve its Injury roll normally. Other misses remain misses. A blast affects all models in its area, including friendlies; do not add this natural-1 rule to blast attacks.

### Melee exchange

The acting fighter chooses one engaged enemy. Both roll their held melee pools, normally adding STR and their own modifiers to every die; Agile allows AGI instead. **Against a Pinned opponent, add +2 to every melee Attack Die total before comparing the pools.** This applies to melee hit rolls, including a Sidearm used in melee, not to Injury or opposed Shove/Grapple tests. An outnumbered fighter suffers −1 to its melee totals for each **additional** conscious, unpinned enemy engaging it, maximum −2.

Each die whose total **exceeds the opponent's highest total** scores a hit. Equal highest totals cause no hits. Only one side can score hits in an ordinary exchange. Roll Injury for those hits; there is no automatic second attack-back.

Natural 1s cannot hit and do not contribute to defence. Natural 20s are compared as modified totals in melee; they do not automatically defeat another pool. Against a pool containing only natural 1s, every non-1 die hits. A fighter always rolls at least one defensive die, even when Pinned or Unanswered; this is a struggle to avoid injury, not a voluntary action. Down, Unconscious, and Captured targets do not roll melee defence.

**Example:** totals 21, 18, and 12 against 17 and 11 produce two hits. Totals 21 and 14 against 21 and 8 produce none. A raw 20 with −3 totals 17 and loses to a raw 18 with +2, which totals 20.

### Rear charges and Unanswered attacks

A Charge that begins and ends in the target's rear arc is **Unanswered** and gains the ordinary +2 rear modifier. If the attacker crosses the target's forward arc along the route, it is no longer a rear Charge. The defender rolls normally to set the opposing maximum but cannot score hits. It may face the attacker after the exchange if still conscious.

Unanswered is also used by specified skills and escape attacks. Only the initiating fighter can hit. Do not omit the defensive pool or award automatic hits.

### Shove and Grapple

Any fighter may use its Fight action to **Shove** instead of injuring. Make one opposed STR test against an engaged enemy. On success push it 2 inches directly away and make it Pinned. On failure nothing moves. Resolve falls or other hazards caused by the push. Neither side inflicts ordinary melee hits during this test.

The Grapple skill offers a different use of the same opposed test. Its holding and escape rules appear with that skill. Neither action allows superhuman throws, attacks on several enemies, or free follow-up attacks.

## 9 Injury casualties and rescue

### Resolve a hit

For every hit, roll **1d20 + weapon Damage − target Armour + applicable injury modifiers vs 15+**. Natural 1 fails and natural 20 succeeds. Stress never changes an Injury roll. Armour does not grant another saving throw.

Each success removes one Wound. Each failure adds one Stress to the target. A hit fighter with a Wound remaining becomes Pinned, without additional Stress for pinning itself. At zero Wounds it becomes **Down**. Resolve all dice in the attack together before changing states; surplus successful Injury rolls do not execute a casualty or create additional post-battle injury rolls.

All humans have one Wound, including experienced Leaders. An Injury success represents a disabling hit; failures represent glancing impacts, protective equipment, and narrowly avoided serious harm.

### Pinned and Recover

A Pinned fighter stays low: **ranged hit rolls against it suffer −2; melee hit rolls against it gain +2**. Apply these alongside other applicable modifiers. It can still defend in melee. These modifiers end as soon as Pinned is removed; becoming Down or Unconscious replaces Pinned with that casualty's own rules.

On a chosen turn, spend its **Move Action to Recover: stand up and remove Pinned automatically, instead of travelling**. This uses the whole Move Action; it grants no travel and does not spend or restore Core. Standing counts as movement for Aim and Unwieldy. Recover does not remove Stress or a morale condition. With an unused Core and no other restriction, the fighter can Shoot or perform another Core Action on a later turn.

You may leave a fighter Pinned while using other fighters, then choose a useful moment to stand. If it instead spends Move crawling, it travels up to half MOVE and remains Pinned. While Pinned it may also Rally itself or attempt the specified Disengage, but cannot attack voluntarily, Hide, Ready, operate equipment, or use ordinary skill actions. It cannot exchange Core for an ordinary self-Recover.

A conscious, unpinned, unengaged friendly within 3 inches and LOS may spend its Core on Help Recover to help the target stand without a test. This removes Pinned only; it does not cure Down or a morale condition. The target keeps its own remaining slots.

### Down and Unconscious

Leave a Down fighter on the battlefield, mark its base, and record the **round it went Down**. Remove READY, Hidden, Marked, Aim, and any sustained skill effect. Retain Stress. It cannot control or contest objectives and drops carried mission objects into contact with its base. It retains its personal equipment until looted.

A Down fighter may only crawl up to half MOVE using its Move slot and attempt self-treatment with a carried medkit using its Core slot. Being Down neither refreshes slots already spent nor grants an immediate crawl. Crawling cannot engage an enemy, use equipment other than self-treatment, or interact with objectives. It provokes ordinary reactions when visible.

At the End Phase **two rounds after the round in which it went Down**, it becomes Unconscious. The partial round in which it fell does not count. A fighter Downed in round 2 therefore becomes Unconscious at the end of round 4. This gives it all of rounds 3 and 4 for rescue.

Unconscious fighters stay on the table but cannot act, react, or be revived during that battle. They may still be carried, looted, or captured. They have not been declared dead.

### Treat and self-treatment

A medkit is a single-use consumable. A conscious, unpinned, unengaged fighter in contact with a Down friendly may spend its Core and a medkit to test INT. Success restores one Wound, removes any morale condition, and leaves the patient Pinned at **2 Stress**. Failure spends the action and medkit but does not alter the Down timer. Natural 1 has no additional medical penalty.

A Down fighter carrying a medkit may use the same action on itself. For **self-treatment only**, ignore its Stress penalty: the attempt represents applying prepared emergency aid. An assisting fighter uses its own normal INT test and Stress. One fighter may be successfully revived **once per battle**. Record that use on its card. A later Down still allows crawling and capture but cannot be revived again that battle.

Treatment never restores spent action slots. A revived patient remains Pinned and can spend an unused Move to stand, leaving any unused Core available. If Move was already spent, ordinary self-Recover waits until its next Move becomes available; friendly help and Rally still work as stated. A revived fighter retains injuries from earlier battles. Medical aid in battle does not erase a lasting injury.

### Attacks against casualties

A Down or Unconscious fighter cannot be used as a shield for another model and does not block movement or LOS. Attacks may target a visible Down fighter using normal shooting or one automatic melee hit from contact. A successful Injury roll makes it Unconscious immediately. It does not kill it, roll lasting injuries early, or add further post-battle injury rolls. Further attacks on an Unconscious fighter have no additional rules effect. There are no battlefield execution rules.

### Loot

An unengaged fighter in contact with a Down or Unconscious model may spend Core to take **one carried item**, including an unused medkit, or one carried objective already on the ground. No test is needed. The looter must have space; it may drop an item into contact to make room. Armour counts as the one item taken with that Core Loot action. The included utility knife and clothing have no resale value.

Mark ownership transfers immediately. A looted item exists in only one place. A weapon taken this way is not held until the looter next makes a permitted weapon choice. Carried loot is not added to the starting Crew Rating during the battle; it must be fully counted in later battles. A dropped item remains where it fell and can be picked up with Interact.

### Capture and evacuation

An unengaged fighter in contact with a Down or Unconscious enemy may spend Core to **Secure** it. This is automatic if no conscious, unpinned enemy is within 1 inch of either model. Mark Captured. The captive cannot act or self-treat. Its Down timer continues normally.

The captor may escort or drag one captive using the carrying rules. Move both bases together, keeping them in contact. Capture becomes a lasting capture only when the captive is escorted completely off the captor's deployment edge while the escort remains capable of moving. The escort leaves with it and cannot return that battle. Carrying mission cargo off an exit or evacuating a friendly casualty likewise removes its carrier from play; surviving extracted carriers return to the settlement afterward. An Unconscious captive can be dragged in the same way.

If the escort becomes Down, Unconscious, Pinned, or gains a morale condition, it releases the captive immediately. Remove Captured; the captive retains its underlying Down or Unconscious state. An unengaged friendly may also free a captive from contact with a Core Interact, provided the escort is not a conscious unpinned enemy within 1 inch. A captor can release voluntarily at the start of its own action.

Friendly evacuation works the same way without Secure: take a casualty off your deployment edge to protect it from further battlefield interference. A casualty evacuated while Down or Unconscious still rolls lasting injury after battle. Evacuation is useful because it prevents capture; it is not an automatic cure.

## 10 Stress and morale

### Gaining Stress

Stress ranges from 0 to **5**. Gain one Stress for each failed Injury roll against you. You also gain one Stress the **first time each round** you see a friendly become Down within 6 inches. Use your forward LOS. Several casualties from one blast still give only one Stress through this witness trigger. Down and Unconscious fighters do not gain witness Stress.

Other sources must say how much they add. The same hit does not add a separate “under fire” Stress on top of its failed Injury result. Extra Stress beyond 5 is lost. A transfer cannot remove more Stress than its recipient can accept.

Subtract current Stress from stat tests, shooting, and melee totals. Do not subtract it from Injury, Break, Rally, initiative, distance, or post-battle rolls. Stress does not reduce fixed MOVE. There is no separate Shaken penalty.

### Break

At the End Phase, each conscious fighter without a morale condition and with **2+ Stress** makes a Break test: **d20 + NRV + applicable modifiers vs 15+**, ignoring Stress. Success removes all Stress. Failure retains Stress and gives the following condition, based on the Stress amount:

| Stress | Condition | What the fighter does |
| --- | --- | --- |
| 1–2 | Broken | Becomes Pinned. Until rallied it may only Move, Recover, Rally itself, or Disengage. |
| 3–4 | Bolting | On its next available turn, spend all remaining slots to move up to twice MOVE toward the nearest reachable place outside enemy LOS. Prefer heavy cover; take the shortest safe route. |
| 5 | Bugging Out | On its next available turn, spend all remaining slots to move up to twice MOVE toward the nearest reachable board edge. It leaves play if it reaches that edge. |

The 1-Stress entry is for effects that explicitly force a Break test. Never make a normal End Phase Break test at Stress 0 or 1. If a forced test fails at 0 Stress, use Broken.

A fighter with a morale condition cannot react, give assistance, score, or contest. Bolting and Bugging Out movement overrides Pinned and spends the fighter's remaining slots even if it reaches its destination early. Movement remains subject to physical obstacles and traversal tests. Bolting never deliberately takes a hazardous route when a safe one exists. Bugging Out may take one if it is the shortest legal way out. If no destination can be reached, move as far along a legal route toward it as possible; if no route exists, remain in place and spend the slots. The owner breaks equal-distance route ties. Choose this forced action on one of your turns before ending your crew's actions; it is taken once that round, even if only one slot remained. If no slots remain when the condition is gained, the forced movement waits until the next round.

A fighter that flees off-board is Withdrawn, not Down, and does not roll an injury merely for fleeing. Any casualty it was carrying is released at the point it started fleeing.

### Rally

A fighter already carrying Broken, Bolting, or Bugging Out at the beginning of the End Phase makes **Rally instead of Break**, using the same Stress-free NRV test. Success removes the morale condition, all Stress, and Pinned. Failure retains its current condition, even if Stress changed. It never immediately rerolls a new Break failure in that End Phase.

A Core Rally action may be attempted on itself by a conscious fighter, including while Pinned or Broken but not Bolting or Bugging Out, or by a conscious, unpinned, unengaged friendly within 3 inches and LOS. Test the acting fighter's NRV, ignoring Stress. Success removes all Stress, the morale condition, and Pinned from the target. Rally may also be used on a stressed fighter with no morale condition. Failed Rally has no additional effect beyond its action cost.

Bolting or Bugging Out fighters need friendly help or the End Phase to Rally. They cannot spend their forced action on self-Rally. Removing Pinned alone does not remove a morale condition.

### Voluntary withdrawal

At the start of any of your turns, you may withdraw the crew and end the battle. Resolve current casualties and post-battle procedures normally. The opponent wins, but you retain rewards already earned and evacuated loot. Remaining uncaptured fighters and casualties return to their own settlement with the equipment they currently carry, including looted gear; an on-board captive that was not extracted is released. There is no bonus round of unopposed killing or looting. Scenario-specific extraction rewards still require actual extraction before withdrawal.

## 11 Stealth and observation

### Hide

An unengaged fighter can spend Core to Hide if it is in cover or entirely outside every enemy's LOS. It cannot Hide within 3 inches and LOS of a conscious enemy. If entirely unseen, hiding is automatic. Otherwise test AGI; success gives Hidden, failure does nothing. Being behind an enemy is not enough when another enemy can clearly see you in the open.

Keep the miniature visible to both players and mark Hidden. Its location is public. Hidden represents uncertainty and concealment within that small area, not secret movement or an invisible person.

### Moving and revealing

A Hidden fighter moves at half MOVE and cannot Dash or Charge while retaining Hidden. A Charge can **begin Hidden** for Ambush, but removes Hidden when movement starts. Remove Hidden when the fighter shoots, makes a loud or forceful interaction, enters engagement, or is successfully hit. Quiet weapons and skills state specific exceptions.

At the start and end of the Hidden fighter's own actions, remove Hidden if a conscious enemy within 12 inches sees it without any intervening cover. Also remove Hidden immediately if a conscious enemy comes within 3 inches with LOS. Ordinary enemy movement into cover-obstructed LOS outside 3 inches does not reveal it automatically.

### Targeting and Observe

A Hidden fighter cannot normally be targeted beyond 12 inches. Within 12 inches, a shooter still needs forward LOS and suffers −4 in addition to cover. Use the starting Hidden modifier for the whole attack pool; reveal after resolving a successful hit. A complete miss does not reveal it. Blasts and hazards can affect Hidden fighters without selecting them as the attack's target.

An unengaged fighter may spend Core to **Observe** one Hidden enemy or one concealed device within 12 inches and forward LOS. Test INT. Success removes Hidden from that enemy or reveals the device's exact type. It does not mark every hidden thing nearby. A failed observation spends the action and does not reveal anything.

Marked is different from revealed. Mark Target requires a legally visible target; it cannot select an untargetable Hidden fighter beyond 12 inches. A marked target loses Hidden when the marking test succeeds and cannot Hide again until that mark expires. Marking never grants LOS through terrain.

## 12 Interaction hacking and improvised actions

### One shared interaction procedure

Choose what you want to change, identify the control or object, spend Core, and resolve the operation. Direct interaction normally requires base contact and no engagement. A trivial operation—pressing an unlocked button, opening an ordinary latch, picking up an accessible object—succeeds automatically.

Test only if the operation is difficult, contested, or dangerous:

| Task | Test | Failure |
| --- | --- | --- |
| Force a stuck door, shift heavy scatter, wrench a mechanism | STR | Nothing changes; the action is Loud |
| Pick a lock, disarm a device, make a delicate manual adjustment | DEX | Nothing changes; a device's natural-1 consequence applies if printed |
| Hack, repair electronics, or make a technical diagnosis | INT | Nothing changes; hacking's natural-1 lockout applies |
| Traverse a dangerous surface or escape a moving hazard | AGI | Use the named fall or hazard consequence |
| Keep composure or help a frightened person | NRV | No improvement; only a printed Break trigger causes a morale condition |

An operation that directly threatens an occupied space is dangerous and requires the operator's appropriate test even if its physical button would be simple to press. A successful operation then gives affected fighters the feature's stated chance to escape. Do not roll once for every empty shutter, lift stop, or door.

### Controls and terminals

Every interactive feature has a physical control in contact with it or at a marked nearby panel. Electronic features may also be linked to a **terminal**. A terminal may link up to three features within 12 inches; draw or label these links before play. Two terminals sharing a linked feature are on the same network for Interrupt; this never grants access to each other's other features. Links ignore intervening walls but cannot chain through another terminal to reach farther. Either crew can use the same terminal.

An unengaged fighter in contact with an active terminal may spend Core and test INT to **Hack** one linked feature. Success performs one printed operation immediately. Failure changes nothing. A natural 1 **Freezes that terminal until this round ends**. Freeze affects remote electronic use through that terminal; it never disables local manual controls.

No specialist skill or hacking kit is required to use a terminal. Tools and training improve reliability. Any crew can instead reach the feature's direct control. A physically locked door can be forced or picked; hacking is another route, not the only route.

### Portable hacking and interference

A hacking kit also permits an INT Hack against one visible electronic deployable or drone within **8 inches**. Success disables it until someone Repairs it. Failure leaves it unchanged. Natural 1 also prevents that kit being used again this round. This does not hack human fighters, their firearms, or their ordinary armour.

Hijacking a device for an immediate operation requires Trojan. Opposing a terminal operation requires Interrupt and READY. There is no separate cybercombat phase, bandwidth resource, or list of attack programs.

### Repair and sabotage

Repair requires contact, Core, and an INT test. Success restores an Offline device or clears a disabled electronic state. A Destroyed device cannot be repaired during battle. Normal failure does not worsen it.

Critical terrain and objective terminals cannot be shot out of the game. They can be temporarily Frozen, or disabled by a scenario's sabotage objective. A sabotaged feature stays in its last safe position and can be repaired with the ordinary Repair action unless the scenario explicitly sets a different objective procedure. Do not invent hit points for whole buildings.

### Improvised actions

Players may propose an action that follows from the physical scene. Agree its **object, intended effect, action cost, relevant stat, and failure consequence before committing**. Use Move for the fighter's movement, Core for another task, and Both only when combining movement with a Core task. Use an existing operation such as Shove, Displace, Open, Close, Move Cover, or Create Smoke whenever possible. Ordinary people and the tools present must plausibly be able to do it.

One improvised action normally affects one target or one terrain piece. It cannot exceed the common move distance, create a free attack, erase a scenario objective, or destroy an entire building. Throwing a hand-carried box or tipping a cabinet is plausible; throwing a car is not. Dangerous and difficult attempts use a normal test, not an invented modifier table. If you cannot agree quickly, use the nearest printed action for this battle and discuss a future addition afterwards.

## 13 Interactive terrain catalogue

### Feature cards

Give each feature a card showing its **footprint, control point, linked terminal, possible states, operation, and any hazard area**. Use two states whenever possible. A single card belongs beside the relevant terrain. Scenarios can choose from this catalogue; players may rename the same mechanics to suit their models.

**Displace:** move an affected fighter the shortest distance up to 2 inches to a safe legal position outside the changing area, chosen by its owner. If none exists, the operation stops before trapping it unless the feature explicitly has Crush.

**Crush:** each affected conscious fighter tests AGI. Pass: Displace it safely. Fail, or no safe destination: one Damage 3 Injury roll ignoring Armour, then Pinned if still conscious. Move a casualty to the nearest accessible edge of the hazard footprint. Down or Unconscious casualties cannot evade; an Injury success against Down makes it Unconscious, and Unconscious has no further injury effect. Neither is removed as dead. A feature cannot affect the same fighter with Crush more than once per round.

**Fall:** use Chapter 7. **Smoke:** blocks LOS through the template at any height up to 3 inches above its surface; fighters inside can see and be seen only within 1 inch. **Difficult:** movement costs double. Only the named state persists; do not add new conditions for individual machines.

### Routes and access

| Feature | Operation and states | Occupied space and counterplay |
| --- | --- | --- |
| Security door or roller gate | Open or Close a marked entrance. A closed gate blocks movement; its declared material determines LOS. | Displace a model caught in the opening. Local manual controls remain accessible from both sides. |
| Blast door | Open or Close a solid entrance up to 4 inches wide. | An occupied closing gap uses Crush. A failed operator test leaves it open. A manual release on each side needs STR, not hacking. |
| Lift or cargo elevator | Move one platform between two marked levels no more than 6 inches apart. Models and loose items on it travel with it. | No crushing under the lift. Someone standing beneath is Displaced; if there is no safe space, the lift stops. |
| Retractable bridge | Extend or Retract a bridge up to 6 inches long across a declared gap. | Retraction under a model is dangerous; AGI success reaches the nearest end within 2 inches, otherwise Fall. |
| Movable walkway | Rotate or slide a supported walkway between two marked connections within 4 inches of each other. | Riders travel with it. Displace anyone at a blocked connection; no movement through solid scenery. |
| Pit or vat cover | Open or Close a cover over a marked hole up to 3 inches across. | Opening beneath a model uses the bridge escape rule then Fall. The cover cannot crush someone beneath it; keep an accessible casualty marker. |

### Cover and visibility

| Feature | Operation and states | Occupied space and counterplay |
| --- | --- | --- |
| Cargo crane | Move one marked cargo piece up to 4 inches within its declared reach, placing or removing cover. | The cargo must fit its marked lifting capacity. Lowering into an occupied area uses Crush; otherwise Displace. Never lift a building. |
| Pulley or hoist | Raise or lower a marked crate or load by up to 4 inches between two positions. | A load can open a passage or screen a window. Dropping it into an occupied area uses Crush, once per round per target. |
| Window shutters | Open or Close one declared bank of windows up to 6 inches wide. | Closed shutters block LOS. Occupants are not injured. Either side can reach an interior manual control. |
| Sliding barricade | Shift one premarked barricade up to 4 inches along its track. | Displace models it touches. It stops at impassable terrain and cannot push a fighter off an edge. |
| Floodlights | Illuminate or darken a marked 6-inch-diameter zone. | While lit, remove Hidden in that zone and prevent Hide there. Light does not grant sight through cover or walls. |
| Ventilation fans | Clear one smoke or gas template linked to the vent, or turn ventilation Off. | Clearing is immediate. It cannot remove a solid obstacle or a fire template. |

### Hazards and utilities

| Feature | Operation and states | Occupied space and counterplay |
| --- | --- | --- |
| Smoke vent | On places one 3-inch-diameter smoke zone at its outlet; Off clears it. | While On it remains. A physical valve can close it. It never attacks through an entire room without a defined template. |
| Irritant gas vent | On places a 3-inch-diameter Difficult zone. A human entering or starting an action inside gains 1 Stress, at most once per round from gas. | Gas never causes direct Wounds. A respirator prevents its Stress. A fan or valve clears it. |
| Conveyor | On carries a model or loose objective up to 4 inches along its marked belt at the end of that model's action; Off stops it. | Each object moves once per round. A conscious rider may opt not to travel. At a dangerous end, an unwilling rider tests AGI to stop; failure uses Fall or Crush as marked. |
| Compactor | Cycle a marked 3-inch work area, then return to Open. | Uses Crush. It cannot enclose an unmarked room or permanently seal an objective. A safety control is accessible nearby. |
| Floodgate | Open makes a marked shallow channel Difficult; Close drains it. | Displace models caught at the gate. Flooding does not remove models or drown casualties. Deep water requires explicit scenario rules. |
| Junction box | Turn power On or Off to up to two linked electronic features within 12 inches. | Mechanical positions stay where they are; active smoke, gas, and lights stop while unpowered. Local manual route controls still work. |
| Service hatch | Open or Close a passage through a declared wall no more than 3 inches thick. | Move through at half speed. The two ends are marked; there is no off-table tunnel network unless a skill or scenario supplies one. |
| Emergency alarm | Sound or Silence an alarm. Sounding removes Hidden from fighters within 3 inches of its marked panel. | It adds no global alert track or automatic reinforcements. A scenario may give it a separate objective role. |

Choose normal, usable starting states during setup: lifts at a marked stop, doors reasonably mixed, bridges with an alternate route, smoke and gas Off. Do not begin a standard game with every route closed. Every mandatory objective must remain physically accessible without winning a hacking contest.

## 14 Deployables and drones

### Deploying equipment

Carried devices already count in Crew Rating. Spend Core to place one in base contact, outside other bases and away from an occupied objective marker. A barricade or ordinary ladder is automatic. Arming a mine, trap, or electronic device requires INT. Success arms it; failure leaves it placed but inert and visible. A natural 1 does not detonate it during deployment. A later Deploy action in contact can retry using the same item.

After deployment, turn its card to Active or Inert. It cannot trigger on models already in its trigger area at the moment it is armed; their subsequent movement can trigger it. Devices cannot act the turn they are deployed except passive smoke or physical cover. A sentry first gains READY at the next Start Phase.

### Visibility disarming and damage

All device locations are public. A concealed mine or trap is a face-down numbered marker: its type is written privately beside its number. Concealment hides the payload, not the location. It is revealed when triggered, successfully Observed, or approached within 2 inches and LOS by a conscious fighter. No dummy markers are required.

An unengaged fighter in contact may spend Core and test DEX to disarm a mine or trap. Success makes it inert; failure leaves it armed; natural 1 triggers it. An electronic device can instead be disabled with portable hacking. An inert device can be recovered with Interact into a free equipment slot.

A visible device can be shot or struck. Use normal shooting to hit; an adjacent unengaged fighter may spend Core to hit it automatically. There is **no Injury roll** against these small devices. One hit makes standing equipment Offline; a further hit makes it Destroyed. A mine or trap hit while armed is disarmed and ruined without an explosion. A utility drone is Destroyed by its first hit. Device cover follows its actual position. Devices have no Stress, morale, skills, or objective-control presence.

### Common deployables

| Item | Credits | Slots | Effect |
| --- | ---: | ---: | --- |
| Folding barricade | 15 | 1 | Place a line up to 3 inches long and 1 inch high; heavy cover. It is physical terrain, not an electronic device, and cannot be shot away. |
| Portable ladder | 10 | 1 | Place a ladder reaching up to 6 inches. It provides normal ladder movement to either crew. |
| Tripwire | 10 | 1 | Single-use. First human crossing its marked 2-inch line tests AGI; failure stops movement and Pins them. Success continues. Consumed either way. |
| Blast mine | 20 | 1 | Single-use, electronic. First model entering within 2 inches and LOS triggers a 2-inch-radius Crush hazard centred on the mine, using the shared AGI escape and Damage 3 procedure. Affects both crews. |
| Smoke emitter | 15 | 1 | Single-use, electronic. From contact, a terminal with a link reserved during setup, or a hacking kit within 8 inches, operate it to create ordinary smoke for this and the next round. |
| Remote clamp | 15 | 1 | Single-use, electronic. First human entering within 1 inch tests AGI. Failure Pins it and ends that movement; success continues. Consumed either way. |
| Sentry turret | 50 | 2 | Electronic. Stationary, 180-degree arc chosen at deployment, range 12 inches, DEX 2, one Attack Die, Damage 2. Gains one READY each Start Phase; it may react once that round. |
| Field supply case | 15 | 1 | Deploy an open cache containing one medkit and one smoke grenade. These two contents replace the case; they cannot be sold as extra profit because its total value equals their 15 Credits. Picking up each is an Interact. |

For mines and traps, **either crew can trigger them**. Placing one is a positional decision, not permission for your own fighters to walk through it safely. A flying drone does not trigger a ground-contact tripwire or clamp; it can trigger an electronic proximity mine if actually within its three-dimensional radius.

Turrets use the owner's one-reactor window, including Return Fire if targeted. They have no normal action slots. Operating a turret with a Core action can turn its facing or fire one shot, but expends its READY and marks it Reacted; this cannot give it a second attack that round. It may be operated only from contact or a portable hacking kit within 8 inches; friendly operation is automatic, enemy operation needs Trojan. It cannot fire without a READY token. A turret's reaction requires its own LOS, not its operator's.

### Utility drones

A utility drone costs **45 Credits**, occupies two equipment slots on its operator, and counts toward the crew's drone limit. Assign its operator on the Battle Roster. It has no weapon, no independent actions, no READY, and cannot score, contest, capture, carry mission cargo, or earn experience.

Deploy it from the operator's base with a Core Deploy action, automatically. On a later turn, spend the operator's **Core** to move the drone up to 8 inches. This is one remote command; performing an operation through it requires a separate Core Action. The operator's Move remains available for its own movement. It may fly over low obstacles but not through solid terrain. Keep it within 12 inches of the operator and no higher than 6 inches above the surface below it. Measure its real flying position; use a stand or height marker. It may finish hovering or on a stable surface. Its LOS uses its actual height and a 360-degree camera.

Spend the operator's **Core** to perform one of these through the drone:

- Operate a physical terrain control in contact with the drone, using the normal automatic operation or the operator's INT test for a dangerous operation.
- Hack through a terminal in contact with the drone, using that terminal's normal links and the operator's INT.
- Observe one Hidden fighter or concealed device within 12 inches and the drone's LOS, using the operator's INT.

The operator must be conscious, unpinned, unengaged, and free of a morale condition. Use the operator's Stress on its tests. Remote operation can change terrain, but **cannot Claim, Secure, loot, defuse a mission bomb, or complete an objective that requires a human interaction**. A scenario may expressly allow a drone operation as one step, not assume it can replace every human task.

If the operator becomes unavailable or moves out of control range, the drone stays inert at its position until control is restored. It remains targetable. Drone movement or operation offers the opponent the action's single reaction window against either the visible operator or visible drone, using the chosen target's position. Disabling the operator or drone stops the unfinished remote action. Another friendly in contact with the drone may spend Core to become its operator, provided it has two equipment slots available; update both cards. Returning the drone to its operator's base and spending Interact packs it away.

A single successful hit destroys a drone; there is no armour or Injury roll. Place a wreck marker. It may be recovered like an item, including by an enemy. This makes remote access useful but exposed, and prevents a flying device becoming a second combatant for free.

## 15 Weapons armour and equipment

### Reading a profile

**Dice** is the number rolled for one attack action, before dual-wielding and Charge. **Damage** modifies Injury. **Range** is the maximum shooting range; Melee means within engagement. **Hands** and **Slots** determine what can be used and carried. **Access** names the settlement structure required to buy or craft the item; it never increases the agreed Crew Rating.

All Credits in these catalogues are **provisional Version 2 prices**. Use the same published price sheet for both crews. No previous simulation result validates these new profiles or prices.

### Standard armoury

| Weapon | Credits | Dice | Damage | Range | Hands / slots | Characteristics | Access |
| --- | ---: | ---: | ---: | --- | --- | --- | --- |
| Unarmed | 0 | 1 | 0 | Melee | 1 / 0 | None | Always |
| Utility knife | Included | 1 | 1 | Melee | 1 / 0 | Agile | Included with fighter |
| Shiv or fighting knife | 10 | 1 | 2 | Melee | 1 / 1 | Agile | Basic |
| Club or machete | 15 | 2 | 2 | Melee | 1 / 1 | None | Basic |
| Crowbar | 15 | 1 | 2 | Melee | 1 / 1 | Breaching | Basic |
| Spear | 20 | 2 | 3 | Melee | 2 / 2 | Agile | Basic |
| Two-handed axe | 25 | 2 | 3 | Melee | 2 / 2 | Brutal | Workshop |
| Pistol | 15 | 1 | 1 | 8 inches | 1 / 1 | Sidearm | Basic |
| Revolver | 20 | 1 | 2 | 8 inches | 1 / 1 | Sidearm, Accurate | Basic |
| Magnum | 20 | 1 | 3 | 12 inches | 1 / 1 | Sidearm, Reload | Workshop |
| Carbine | 20 | 1 | 2 | 24 inches | 2 / 2 | None | Basic |
| Assault rifle | 35 | 2 | 2 | 24 inches | 2 / 2 | Automatic 2 | Basic |
| Submachine gun | 30 | 2 | 1 | 12 inches | 2 / 2 | Automatic 2, Close Combat | Workshop |
| Shotgun | 30 | 1 | 3 | 12 inches | 2 / 2 | Brutal | Basic |
| Suppressed carbine | 35 | 1 | 2 | 18 inches | 2 / 2 | Quiet | Armoury |
| Sniper rifle | 55 | 1 | 3 | 36 inches | 2 / 2 | Precision, Accurate | Armoury |
| Machine gun | 70 | 3 | 4 | 24 inches | 2 / 3 | Heavy, Automatic 3, Unwieldy, Suppression | Armoury |
| Grenade launcher | 65 | 1 per target | 3 | 24 inches | 2 / 3 | Heavy, Blast, Reload, Unwieldy | Armoury |
| Flamethrower | 65 | 1 per target | 2 | 8 inches | 2 / 3 | Heavy, Blast, Ignore Cover 2, Unwieldy | Armoury |
| Rocket launcher | 60 | 1 per target | 5 | 24 inches | 2 / 3 | Heavy, Blast, Piercing 2, Single-use, Unwieldy | Advanced Workshop |
| Throwing knife | 10 | 1 | 1 | 8 inches / Melee | 1 / 1 | Agile, Quiet, Thrown | Basic |
| Javelin | 15 | 1 | 2 | 8 inches / Melee | 1 / 1 | Piercing 1, Thrown | Basic |

The included utility knife cannot be duplicated for free to gain an off-hand die. Buy a second weapon if you want two weapons. A Heavy weapon is restricted by Chapter 4, even if its profile has no movement penalty beyond Unwieldy. A standard crew may field at most **one weapon with range over 24 inches per complete five human fighters**, minimum allowance one. Range-increasing effects count toward this limit.

### Characteristics

| Characteristic | Rule |
| --- | --- |
| Accurate | +1 to hit when the target is within half the weapon's printed range. No benefit in melee. |
| Precision | If the fighter has Aim, reroll one failed Attack Die with this weapon. |
| Automatic X | The printed ranged Dice value is X; do not add X again. |
| Agile | Use AGI instead of STR for melee hit totals. Damage is unchanged. |
| Sidearm | May contribute one die to a melee pool. Uses STR there. |
| Close Combat | May contribute one die to melee despite being two-handed. It occupies both hands. |
| Brutal | For each hit, roll two Injury dice and use the higher raw result as that hit's one Injury roll. It cannot cause two Wounds from one hit. |
| Piercing X | Reduce Armour by X, minimum 0. It never increases Damage against an unarmoured target. |
| Ignore Cover X | Reduce the shooting cover penalty by X, minimum 0. Does not remove Hidden or bypass blocked LOS. |
| Quiet | Firing does not itself remove Hidden if the shooter remains in cover. Other reveal rules still apply. |
| Breaching | +2 STR when forcing a physical door or simple obstruction with this tool. |
| Suppression | If this attack hits but causes no Wound, add one extra Stress to the target, once for the whole attack. |
| Reload | After firing, mark unloaded. Spend Core to Reload before firing again. A weapon begins the battle loaded. |
| Single-use | Expend the item after one declared use, even if it fails. It must be replaced between battles. |
| Unwieldy | −2 to hit if its wielder has moved earlier this round, including forced movement. Pivoting alone is not movement for this trait. |
| Thrown | A successful throw leaves the weapon at the target's position; a miss leaves it halfway along the line to the target. Recover it with Interact. It cannot be thrown again while lying on the table. |
| Blast | Use the area attack procedure below. It cannot be dual-wielded or gain extra dice from Charge, skills, or Automatic. |

### Blasts smoke and fire

For a Blast, choose a visible impact point within range. It must be a surface or a model's position, not an arbitrary point in the air. Each fighter or device whose base touches the **2-inch-radius** template and has an unobstructed line to its centre is a target, including the user's crew. This blast line ignores the target's facing. Targets must be on the impact point's level or within 2 inches vertically; intervening floors block it. Roll one normal ranged Attack Die against each, then Injury for hits on fighters; devices instead use their hit-based damage rule. Rear and Aim bonuses apply using the shooter's position and state, not the blast centre. Use cover from the impact point, apply −2 against a Pinned target, and ignore Hidden's −4. There is no separate shot at the centre, scatter roll, or extra attack on the original target. Solid walls contain the blast. A fighter can be hit only once by that blast.

Throwing a damaging grenade or fire bottle is a Core Shoot action and uses the own-turn attack allowance. It cannot be combined with another held weapon. A smoke grenade is a non-attack Core Use Item action and instead requires one DEX test to place a **3-inch-diameter** smoke template at a visible point within 8 inches. Pass: place it there. Fail: place it 2 inches closer to the thrower along the same line, stopping at the first obstruction. It produces no hits. Smoke lasts through the End Phase of the **next round**, then clears; mark its expiry round.

A fire bottle uses the grenade Blast profile, then leaves a 3-inch-diameter fire zone at the chosen point regardless of hit results. A human entering or starting an action inside fire suffers one Damage 2 Injury roll, at most once per round from fire zones. The initial bottle attack counts as that exposure. Fire blocks neither LOS nor movement. It lasts through the next round's End Phase. Core Interact in contact with the zone's edge extinguishes it on an INT test; a fire extinguisher does so automatically. Fire does not spread or add a separate Burning condition.

### Armour and supplies

| Item | Credits | Equipment slots | Rule | Access |
| --- | ---: | ---: | --- | --- |
| Light armour | 10 | Worn | Armour 1 | Basic |
| Heavy armour | 25 | Worn | Armour 2; MOVE reduced by 1 | Armoury |
| Protective shield | 15 | 1 | Occupies one hand. +1 Armour against attacks through the forward arc; total Armour maximum 3. No protection from falls or Crush. | Workshop |
| Medkit | 10 | 1 | Single-use; Treat or self-treatment | Basic |
| Smoke grenade | 5 | 1 | Single-use; smoke procedure | Basic |
| Frag grenade | 10 | 1 | Single-use; range 8, Damage 1, Blast | Workshop |
| Fire bottle | 10 | 1 | Single-use; range 8, Damage 1, Blast, fire zone | Basic |
| Hacking kit | 20 | 1 | +2 to Hack; enables portable hacking of devices within 8 inches | Basic |
| Climbing kit | 10 | 1 | +2 to a climb with usable anchor points; permits otherwise smooth climbs where a rope can be secured from an accessible top | Basic |
| Safety harness | 10 | 1 | Once per battle reroll a failed AGI test to avoid a fall; must be used with a climbing kit or a declared safety line | Workshop |
| Respirator | 10 | 1 | Ignore irritant gas Stress; does not ignore smoke LOS | Basic |
| Tool kit | 10 | 1 | +2 INT to Repair a device, not Deploy or Hack | Basic |
| Fire extinguisher | 10 | 1 | Core Interact automatically clears one adjacent fire template; reusable | Basic |
| Trauma dressings | 5 | 1 | Single-use; when treating another fighter, reroll one failed treatment test after spending the medkit. No effect on self-treatment. | Clinic |
| Stimulant | 5 | 1 | Single-use; Core in contact removes Pinned and 1 Stress from a conscious friendly. It gains 1 Stress at this End Phase. Cannot affect a Down fighter. | Clinic |
| Anti-anxiety dose | 5 | 1 | Single-use; Core on self or friendly in contact gives +2 to its next Break or Rally this battle. Only one dose may be pending per fighter. | Clinic |

A conscious fighter may administer a chem to itself only when otherwise permitted to Use Item. A Pinned fighter needs help; a chem does not silently override its action restrictions. A fighter may receive **one chem dose per round**. The bonus ends when used, and duplicates do not stack. Medkits and dressings are medical supplies, not chems. There is no addiction, toxicity, or drug-combination track in the core rules.

### Building and naming weapons

Use the armoury immediately, or agree a custom profile before either player selects a roster. A custom weapon must stay inside its class and use the characteristics above. An exact copy of a published profile always uses the published price, not a cheaper builder result. Its appearance does not grant unprinted capabilities. The following construction prices are a **provisional design tool**, not evidence of equivalence to the curated armoury. Both players must accept the complete profile and Credits value before it can enter persistent play; otherwise use the nearest published profile.

| Class | Starting profile | Base Credits | Limits |
| --- | --- | ---: | --- |
| One-handed ranged | 1 die, Damage 1, range 8, Sidearm | 10 | Damage 1–3; range at most 12; two dice maximum |
| Two-handed ranged | 1 die, Damage 1, range 24 | 15 | Damage 1–3; range at most 36; three dice maximum |
| Heavy ranged | 1 die, Damage 3, range 24, Heavy, Unwieldy | 35 | Damage 3–5; range at most 36; three dice maximum; three weapon slots |
| One-handed melee | 1 die, Damage 1 | 5 | Damage 1–3; two dice maximum |
| Two-handed melee | 2 dice, Damage 3 | 15 | Damage 3–5; three dice maximum |
| Thrown | 1 die, Damage 1, range 8, Thrown | 5 | Damage 1–2; one die; one weapon slot |

Add 5 Credits per extra Damage, 15 per extra Attack Die, 5 to extend a Sidearm from 8 to 12 inches, or 15 to extend a two-handed ranged weapon from 24 to 36. Shortening a two-handed ranged weapon to 12 inches reduces its price by 5. Each trait costs: Accurate 5; Precision 10; Agile 5; Close Combat 5; Brutal 10; Piercing 1 costs 5, Piercing 2 costs 10; Ignore Cover 1 costs 5, Ignore Cover 2 costs 10; Quiet 15; Breaching 5; Suppression 10; Blast 20. Blast restricts the profile to one die per target and cannot combine with Automatic or Quiet. Ordinary class traits are included, not purchased twice.

Reload reduces the result by 5; Single-use reduces it by 10. Use no more than one price-reducing drawback. Minimum weapon price is 5 Credits. At most **two optional traits** may be added to a custom weapon; class traits, Automatic's printed dice, and the one drawback do not count toward those two. No profile exceeds Damage 5, range 36, or the three-die ceiling. Consumable grenades use their printed profiles rather than this builder.

## 16 Skills

### Choosing and using skills

These **40 skills** are the Version 2 selection. Learn only skills whose stat is at least +2 before lasting injuries. Each fighter knows at most three; do not stack several copies. Starting skills are included in the training grade. Later skills come from advancement, not a separate purchase of powers.

“Once per round” means once across all of that fighter's turns and reactions combined. A skill never converts Move into Core or grants another Core Action. Movement included in a skill effect does not create another action or reaction. All skill tests use the core test unless explicitly opposed. A passive bonus has no action cost. A fighter must be conscious, unpinned, unengaged, and free of a morale condition to use a skill action unless its text explicitly permits otherwise. Melee skills can be used during their stated engagement.

### Strength skills

| Skill | Use | Effect |
| --- | --- | --- |
| Grapple | Core; engaged | Opposed STR against one engaged enemy. Pass: hold it. Neither can attack, react, or operate equipment while the hold remains. The holder may drag at half MOVE and release at the start of its own turn. The held fighter may spend Core to oppose STR and escape; success releases it and allows a free 1-inch separation. Down, Unconscious, Pinned, or a morale condition on the holder ends the hold. No human-shield or automatic takedown effect. |
| Strong Arm | Passive | Move at normal MOVE when dragging one casualty or carrying a Heavy mission object. Both still prohibit Dash and Charge and occupy one hand. Does not permit full-speed dragging of a resisting Grappled enemy. |
| Throw | Core | In contact, lift and throw a loose, plausibly hand-carried object no larger than a 1 × 2-inch footprint up to 3 inches. Test STR to hit one visible fighter at the destination; success Pins it and Displaces it 1 inch, with normal hazard consequences. Failure moves the object halfway without hitting. Cannot throw a person, anchored scenery, or mission-critical feature. |
| Brace | Core; in heavy cover | Ready and brace in place. Until you next move or take another Core Action, reduce Stress gained from each incoming attack by 1, minimum 0. Hits still Pin normally and may remove READY. This is not armour or injury resistance. |
| Bull | Charge modifier | You may replace the Charge's melee exchange with Shove, gaining +2 to that opposed STR test. There is no separate charge attack or charge die. |
| Rage | Melee modifier | Before rolling an own-turn Fight or Charge exchange, accept 1 Stress after the exchange to gain +2 Damage for its Injury rolls. You must have room for that Stress when declaring. No bonus in defensive exchanges or reaction attacks. |
| Tough | Once per battle | Reroll your failed self-treatment test using the same medkit. This is the same treatment attempt, not a second charge or an extra Wound. |
| Big Fella | Passive | An Unwieldy weapon suffers −1 instead of −2 after your movement. It still occupies its normal hands and slots. |

### Dexterity skills

| Skill | Use | Effect |
| --- | --- | --- |
| Mark Target | Core | Test DEX against one legally visible enemy within 24 inches. Pass: Mark it through this round's End Phase; friendly shooting gains +2 to hit it. Reveal it as described in Chapter 11. Only one enemy may be Marked by your crew at a time; a new mark replaces the old. |
| Head Shot | Shooting modifier | Gain +2 Damage against a Marked target when using a one-die ranged weapon. Does not apply to Blast or an Automatic weapon reduced to one die. |
| Gunslinger | Passive | When using two one-handed firearms, add one off-hand Attack Die beyond the normal allowance, to the shared maximum of three. Keep each die's weapon identity. |
| Split Fire | Shooting modifier | Divide your normal shooting pool between at most two enemies within 3 inches of each other. Each die needs its own weapon range and LOS. No extra dice or follow-up shots. |
| Run and Gun | Move plus Core | If both slots remain, combine normal Move and Shoot as one turn, firing at a declared point along the route. Spend both slots at declaration. This is your one own-turn attack and offers the opponent one reaction window for the combined action. |
| Breach | Move modifier; once per round | During your Move, attempt to force one closed ordinary door with an STR test without spending Core. Success opens it and movement continues; failure stops movement at the door. Reinforced blast doors are excluded. Reactions work normally. |
| Cover Me | Reaction | Spend READY when a visible enemy shoots another friendly within 6 inches of you. Shoot the attacker as a simultaneous Return Fire exchange; the attacker still targets the original friendly. Neither shot cancels the other. Counts as your one reaction and the action's one reacting model. |
| Speed Loader | Reload modifier | A Core Reload readies up to two held weapons with Reload instead of one. It does not include a shot or spend Move. |

### Agility skills

| Skill | Use | Effect |
| --- | --- | --- |
| Ambush | Charge modifier | If you begin a Charge Hidden, test AGI before moving. Success makes its exchange Unanswered and gives +2 to hit. Failure removes Hidden and gives no bonus; the Charge still proceeds normally. Rear and skill hit bonuses can both apply, but the attack pool is still capped. |
| Incapacitate | Core; engaged | Make a one-die Unanswered melee exchange using AGI and Damage 0. A successful Injury puts the target Down as normal; mark Subdued. If it suffers no other successful Injury or hazard before battle ends, its lasting-injury roll becomes Full Recovery instead. Capture still requires Secure and extraction. |
| Ghost | Once per round | Shooting a one-die weapon while in cover does not itself remove your Hidden. Other reveal triggers still apply. Cannot use with Blast or Automatic weapons. |
| Acrobatic | Passive | +2 to AGI for climbing or jumping. Climbing still costs double vertical distance and unsupported jumps remain limited to 3 inches. |
| Dodge | Reaction modifier | Reroll a failed Dive test. You still need READY, still become Pinned, and move no farther than 3 inches. |
| Quick | Passive | Increase MOVE by 1, to a maximum of 7 before armour and injuries. Does not alter Charge's d6 or the jump limit. |
| Sneak | Passive | Hidden no longer halves your normal Move. Other causes of half-speed movement still apply. |
| Sprinter | Both | Dash up to twice MOVE plus 2 inches. It still costs both slots and grants no attack. |

### Intelligence skills

| Skill | Use | Effect |
| --- | --- | --- |
| Terminal Training | Passive | +2 INT to Hack while your own fighter is physically in contact with the terminal. Does not apply through a drone or to portable device hacking. |
| Trojan | Core | With a hacking kit, test INT against one visible electronic enemy device within 8 inches. Success performs one legal operation with it, then control returns to its owner. A Single-use device is consumed if triggered. A turret needs unspent READY and cannot exceed its attack limit. A drone may move up to 4 inches but cannot perform an objective action. Failure changes nothing. |
| Interrupt | Reaction | While touching a terminal, spend READY when an enemy within 12 inches uses a terminal on the same network. This reaction needs the terminal link, not LOS to the hacker. Oppose INT. Success cancels that Hack and Freezes its terminal through this End Phase; failure permits the original Hack to succeed without another roll. A tied test favours the active hacker. |
| Technician | Passive | +2 INT when Deploying or arming a device. Does not improve its firing stat or create equipment. |
| Stabilize | Treatment modifier | +2 INT to Treat another fighter. On success set the patient's Stress to 0 instead of 2. It is still Pinned and has used its one revival. |
| Doc | Passive | Carry two medkits in one equipment slot. Pay for both. When Treating another fighter, you may spend its carried medkit instead of yours. Treatment still requires contact and Core. |
| Pack Rat | Passive | Gain one equipment slot, maximum three. Does not add hands or weapon slots. |
| Smart | Interact modifier; once per round | Reroll one failed test for a direct physical Interact, including a mission Work action. The action still costs Core. Does not apply to Hack, Treat, Capture, Deploy, attacks, or skill actions. Automatic interactions remain automatic. |

### Nerve skills

| Skill | Use | Effect |
| --- | --- | --- |
| Inspire | Core | Test NRV, applying your Stress. Success removes up to 2 Stress from you and from one friendly within 6 inches and LOS. Does not remove Pinned or a morale condition. |
| Rally Training | Core | Make the normal Stress-free Rally test for up to two friendlies within 6 inches and LOS instead of one within 3. One test determines both outcomes. You may include yourself. While Broken, you may use this skill only to Rally yourself, not to assist others. |
| Motivate | Core | Test NRV. Success lets one other conscious, unpinned friendly within 6 inches and LOS travel 2 inches farther during its next normal Move this round. It must spend its own unused Move; no slot is restored. Does not extend Dash, Charge, Disengage, forced flight, or standing up. |
| Share the Burden | Core | Transfer up to 2 Stress in total from friendlies within 3 inches and LOS to yourself, limited by your remaining capacity. No test. Does not remove their morale conditions. |
| Hold Fast | Help Recover modifier | When your Help Recover action helps another fighter in cover, also remove 1 of its Stress. It must actually have cover from at least one visible enemy. No injury-prevention aura is created. |
| On Your Feet | Core | Recover up to two friendlies within 6 inches and LOS instead of one within 3. No test. Neither may be Down or Unconscious; morale conditions remain. |
| Commanding Presence | Once per round | One friendly within 6 inches and LOS may use your NRV for its Break or Rally test. You must be conscious, unpinned, and without a morale condition. Other modifiers belong to the fighter taking the test. |
| Unflinching | Once per battle | After an attack hits you but causes no Wound, ignore Pinned from that attack and retain READY if you had it. Gain all Stress normally. This does not remove pre-existing Pinned or a morale condition. |

## 17 Objectives and building a mission

### Shared objective rules

A fighter controls an objective when it is within 2 inches, conscious, unpinned, unengaged, and free of a morale condition, and no eligible enemy is also within 2 inches. If both crews have eligible fighters there, it is contested. Extra bodies do not outweigh one enemy unless a scenario explicitly says so. Devices, drones, Down fighters, and captives never control or contest.

**Claim** is a Core Interact in base contact with an uncontested marker. It places your crew's token. For a Claim objective, that token remains when you move away and is replaced when an enemy Claims it. A contested marker scores for neither crew, even if it still bears a claim. Claim is always physical; there is no remote Tagged objective power.

**Retrieve** picks up a portable objective with a Core Interact in contact. A fighter may carry one; the scenario identifies it as normal or Heavy. Passing it to a friendly in contact takes the giver's Core. A Down fighter drops it. A drone cannot carry it.

**Work** is a Core Interact and an appropriate test to advance a marked objective, such as disabling a bomb or repairing a generator. Default: two successful INT or DEX tests in total, whichever the objective card names. Place a progress token for each success. A failure spends the action but does not remove progress. Opponents cannot erase progress unless the mission explicitly includes that operation.

### A mission must state

Record deployment, the primary objective, one secondary objective per crew, scoring times and values, the end condition, and any special terrain or loadout requirements. Both sides must know whether an objective is Control, Claim, Retrieve, Escort, or Work before selecting crews. Objectives that are secret must still use publicly agreed scoring procedures.

Every mission must offer a route to primary and secondary success without killing opponents. A requirement to loot an enemy casualty is suitable as an optional story objective, not the only available route to scoring. Do not award routine points for casualties in addition to the advantage of removing their actions.

### Generate a simple mission

This procedure supplies playable objectives when you have no authored scenario. It does not supply setting or campaign fiction.

1. Choose one primary type from the table below. Place its relevant markers in the middle 12-inch band, outside deployment zones, at least 6 inches apart and 3 inches from any edge. Alternate placing markers; each player must be able to reach them by two plausible routes.
2. Choose one secondary type for each crew, openly and simultaneously. Both players can choose the same one. Each secondary can score only once and is worth 2 points. An extracted carrier counts as having completed its recorded secondary before leaving play.
3. Link at least two of the four interactive terrain features to useful approaches to those objectives. Neither side may require a specific paid item or skill merely to participate.
4. Play six rounds. Highest total score wins; ties are draws. A withdrawn crew loses regardless of score.

| Primary type | Setup | Scoring |
| --- | --- | --- |
| Control | Three neutral markers | At each End Phase from round 2 onward, 1 point per marker controlled, maximum 2 points per crew per round. |
| Claim | Three neutral markers | Claim in contact. At each End Phase from round 2 onward, 1 point per uncontested friendly claim, maximum 2 per crew per round. |
| Retrieve | Three normal cargo markers | 2 points for each cargo taken off your deployment edge; 1 point for each still carried at battle end. Each cargo scores once, using the higher result. |
| Work | Two independent panels with separate progress for each crew | Completing both Work successes on a panel earns 2 points; each crew may complete each panel once. A human must finish the work in contact. |

| Secondary type | Completion |
| --- | --- |
| Open the route | Successfully operate two different interactive features while outside your deployment zone. Repeated toggling of one feature does not count twice. |
| Reconnoitre | End an action with a conscious eligible fighter in the opponent's deployment zone, outside engagement, and spend its Core to record the route. |
| Recover supplies | Place one additional neutral cargo at the centre before deployment. Retrieve and extract it; only one crew can score this secondary from that cargo. If both selected it, share that one marker. |
| Rescue | Revive or evacuate one of your own Down fighters. This is optional; never the sole secondary choice offered to someone learning the game. |

### Escort and sabotage conventions

An authored Escort objective must give the escorted figure a profile, who controls its movement, its exit, and how it behaves if its escort falls. The default is an unarmed Recruit profile, no independent action slots, moving with a friendly in contact at the escort's normal Move. It cannot attack, score other objectives, or be used to gain Passes. Harm uses the ordinary casualty rules.

For a sabotage objective, require Work at a marked charge or control point. The scenario must print the number of successes and the detonation time. In the absence of a special rule, two Work successes arm it; it triggers at the following End Phase, and one successful enemy DEX Work disarms it beforehand. Apply the feature's printed hazard or Disabled state rather than destroying an entire settlement by implication.

## 18 Ending a battle and lasting injuries

### Close the battlefield

End after round 6, an agreed scenario ending, or voluntary withdrawal. Finish the current action before a scenario ending; withdrawal follows Chapter 10. Score any end-of-battle objectives, then record the winner or draw.

Recover all your surviving fighters, including those Down or Unconscious, except captives already escorted off the enemy edge. Fighters who fled return home. Equipment still carried returns with its carrier. Unclaimed equipment and device wrecks are recovered by their original owner; a destroyed device returns as scrap with no sale value. Neither winning nor remaining on the table grants free extra Loot actions. Resolve actual ownership changes recorded during play once, with both players present.

Each fighter still Down or Unconscious at the end, including an evacuated or captured casualty, makes **one lasting-injury roll**. A revived fighter who finished conscious makes none unless put Down again. An Incapacitate-only Subdued casualty gets Full recovery without a roll. No fighter rolls twice because they were shot several times. Dead fighters are removed only at this post-battle step.

### Lasting-injury table

Roll a d20 and read its pair of results. There are ten outcomes; only the first is death. This is not a stat test: no natural-success rule, Stress, skill, or NRV modifier applies.

| d20 | Result | Effect |
| --- | --- | --- |
| 1–2 | Died of wounds | Remove the fighter from the Settlement Roster. Their recovered equipment goes into your stores; stolen equipment remains with its new owner. |
| 3–4 | Convalescence | Unavailable for your next battle and its Settlement round. After that round they return without a lasting penalty. |
| 5–6 | Damaged leg | Permanent MOVE −1, to a minimum of 4 before temporary movement effects. |
| 7–8 | Damaged arm | Permanent STR −1, to a minimum of 0. |
| 9–10 | Damaged eye | Permanent DEX −1, to a minimum of 0. |
| 11–12 | Shell shock | Begin each battle with 1 Stress. |
| 13–14 | Shaken confidence | Permanent NRV −1, to a minimum of 0. |
| 15–16 | Hatred | Record the opposing settlement. Once per battle against it, before one own melee attack, choose +1 Damage and gain 1 Stress after the exchange. You cannot choose this at Stress 5. This counts as a scar and adds 5 Credits to the fighter's value. |
| 17–18 | Full recovery | No lasting effect. |
| 19–20 | Hard-earned lesson | Full recovery and 1 extra XP, within the battle's XP cap. |

The five permanent penalties and Hatred are **scars**. A fighter can carry at most two scars; repeated instances of the same scar do not stack. If a new result would duplicate a scar or exceed two scars, apply Convalescence instead. A penalty at a stat's minimum still occupies its scar slot. Injury never reduces Crew Rating: deliberately injuring a fighter cannot buy a cheaper veteran. Hatred's value is removed if that scar is treated.

Convalescence prevents both deployment and work for one subsequent battle cycle. Mark it with the next battle number; clear it after that battle's Settlement round, not immediately after the injury. Other scars do not prevent deployment or work. A fighter can retire voluntarily; keep their equipment, receive no refund for their body or experience, and free their housing.

### Captives

Only a captive actually escorted off the enemy deployment edge is a post-battle prisoner. Resolve their lasting injury on their owner's roster first. Death cancels captivity. A surviving prisoner misses their owner's next battle and cannot work during that cycle; they return automatically after that battle's Settlement round. A prisoner is not converted to the captor's roster, sold, or held indefinitely.

Before that next battle, the owner may pay **25 Credits** to recover the prisoner immediately. If the captor has an operational Holding Room, the payment is **30 Credits**. This is paid to the captor; the captor cannot refuse a rules-defined release. Without payment, the one-battle return remains automatic. Temporary injury and captivity run concurrently, never consecutively. Immediate release does not cure Convalescence.

Captured equipment transfers only if actually taken with a Loot action during the battle. Otherwise it returns with the prisoner. Friendly evacuation, winning, or capturing a body does not grant an automatic inventory sweep. Captivity is a limited setback, not a route to removing the opponent from a two-player game.

### Battle rewards

Both crews receive **125 Credits and 20 Materials** for completing a battle. The winner gains another **25 Credits**; a draw gives no winner bonus. Both crews keep their legitimately extracted loot and scenario resource rewards. The default mission generator adds no extra resources for victory points, kills, or prisoners. A withdrawn crew receives the same participation reward but no winner bonus.

A battle counts for rewards, production, recovery, and experience after at least two complete rounds, or when its printed objective ends it earlier through normal play. A voluntary early concession is allowed but generates none of those benefits for either crew. Both players may instead void and replay a disrupted game; it then has no roster consequences. Do not manufacture empty games solely to generate income.

## 19 Experience and advancement

### Earning experience

Each surviving owned fighter deployed in a qualifying battle gains **1 XP**, including fighters who fled or were captured. Gain **1 additional XP** if that fighter completed at least one of these deeds:

- Made a successful Claim or Work action, or carried mission cargo off the table.
- Operated an interactive feature that opened or closed a useful route, moved a model or cargo, or affected an enemy; toggling an irrelevant switch does not qualify.
- Revived or evacuated a friendly casualty, or extracted an enemy captive.
- Put an enemy fighter Down through an attack, device, or terrain operation they personally resolved.

A fighter earns the deed bonus once per battle, however many deeds they perform. The injury-table lesson can add another XP, but **3 XP per battle is the absolute maximum**. Workers, reserves, Relief Volunteers, and fighters already dead gain none. Record a deed when it happens; use it to reward contribution rather than reconstructing every shot afterward.

### The ten-level track

New recruits start at **Level 0, XP 0**. Every **3 accumulated XP** grants the next level, to Level 10 at 30 XP. Apply each newly reached row after injuries. Keep total XP; do not spend it. Resolve multiple new levels in order. Level 10 fighters keep their history but gain no further numerical advances.

| Level | Total XP | Advance | Added Crew Rating |
| --- | ---: | --- | ---: |
| 1 | 3 | +1 to any one stat | 10 |
| 2 | 6 | +1 to any one stat | 10 |
| 3 | 9 | Learn a skill | 10 |
| 4 | 12 | +1 to any one stat | 10 |
| 5 | 15 | +1 to any one stat | 10 |
| 6 | 18 | Learn a skill; eligible to handle Heavy weapons | 10 |
| 7 | 21 | +1 to any one stat | 10 |
| 8 | 24 | +1 to any one stat | 10 |
| 9 | 27 | Learn a skill | 10 |
| 10 | 30 | +1 to any one stat | 10 |

Add each advance's value to the fighter's original body price. This is a valuation change, not a treasury payment. A stat can never exceed +6 before scars, and Wounds never increase. A learned skill requires an uninjured stat of at least +2 in its path. Keep at most three skills; when learning a fourth, replace one. At a skill level, you may instead replace one existing skill; if you neither learn nor replace, the advance is lost but its value still applies. At a stat level where you decline a legal increase, the value also applies.

Write uninjured stats and scars separately. A scar reducing a stat does not erase a learned skill or make future improvement exceed the uninjured +6 limit. Advancement does not change training grade. An experienced Recruit can become highly useful without replacing their profile or being charged for the same training twice.

### Retraining and promotion

An operational Training Yard lets one fighter replace one known skill for **20 Credits** per Settlement round, respecting the +2 prerequisite and three-skill maximum. It adds no skill or XP and changes no Crew Rating.

There is **no automatic promotion purchase** in this edition. Training grade stays the grade bought at recruitment. Recruit and Fighter veterans may handle Heavy weapons at Level 6, within the crew's item limit. If a fighter takes over as crew leader, that is the nominated role, not the Leader recruitment grade. This prevents a promotion from granting another starting allocation on top of earned advances.

## 20 Founding and running a settlement

### Founding package

Name your settlement and start with **1,000 Credits, 125 Materials, twelve building plots**, and these four free structures: **Headquarters, Generator, Materials Processor, and Salvage Yard**. Each occupies one plot, leaving eight free. Headquarters houses twelve people. Recruit a first crew, buy equipment, and optionally build additional available structures using the starting resources.

Founding is the one exception to construction timing: all structures bought during founding are operational for the first battle. Generate and allocate Power once before that battle. You receive no founding production or battle rewards. You may keep resources unspent. Buildings need no scale model; a named box on a settlement sheet is enough.

The founding package can buy a six-person 750-Credit Battle Roster, two basic workers, a Workshop, and a Clinic. The worked example in Chapter 22 shows the exact accounts. Persistent development does not require a campaign organiser, map, third player, or regular group.

### The Settlement round

Resolve one Settlement round after each qualifying battle, in this order:

1. **Record the battlefield:** score, ownership changes, prisoners, expended items, damaged devices, and which fighters need injury rolls. Clear battle Stress and conditions after recording them.
2. **Allocate workers and Power:** use structures already built before this round. A worker must be an available owned fighter who was not on the preceding Battle Roster, is not a prisoner or convalescent, and is not assigned elsewhere. Generate Power, then assign it to whole structures. No benefits apply until their required Power is assigned.
3. **Resolve injuries and medical services:** roll once per eligible casualty. Use an operational Clinic for treatment if desired. Resolve prisoner release payments. A newly injured or captured fighter cannot become a worker in this round.
4. **Collect resources:** receive battle rewards and each operational producer's output once. Buildings never generate extra rounds while you wait between games. Apply storage limits after purchases in step 6, not before you can spend the new income.
5. **Apply experience:** award XP and advances to survivors. Update their current Credits value.
6. **Manage the roster and buildings:** recruit, buy, sell, craft, repair, build, expand, and retrain. A service's per-round limit applies across all its uses. Each completed new structure becomes operational at the start of the next Settlement round; it grants no output, unlock, or Power now. Equipment bought or crafted now is ready for the next battle.
7. **Close records:** clear a previously due Convalescence or unpaid captivity after this cycle. Keep new ones marked for the next cycle. Discard Materials above storage capacity; record the next Battle Roster separately when a matchup is agreed.

For structures which unlock purchases or battle equipment, the last allocation of Power remains in force until the next Settlement round. Such access is available during pre-battle shopping too; a per-round production, service, or preparation limit does not refresh during shopping. Fielding someone previously assigned as a worker is legal: their completed production remains earned, but they cannot work in the Settlement round following that battle.

### Power and workers

Each Generator produces **10 Power** at allocation. Power is assigned, not spent as a stored currency: it expires at the next allocation and cannot be sold or saved. Pay a structure's entire listed requirement or leave it unpowered. No partially powered effects. A passive structure needs no Power. Multiple Generators add their output.

One eligible worker may occupy a structure's worker slot. A worker has no proficiency track and needs no particular stat. Worker benefits are printed in the structure table: roughly a tenth of normal production or a small service discount. Do not apply a generic extra 10% to everything. Structures marked “none” receive no worker benefit. Unpowered structures receive no worker benefit either. A worker assigned to a Generator adds its output before Power allocation.

No worker receives both a battle role and a production role for the same battle cycle. Workers still occupy housing and are paid for when recruited, but have no recurring wages, food, or water track. Every human body remains the same roster entry when reassigned.

### Buying selling and construction

Basic items are available without a special structure. An unlock marked Workshop, Armoury, Drone Bay, or Advanced Workshop requires that operational powered structure. Owned items remain usable if their unlock later loses Power. You may buy between rounds using your last valid unlocks, but cannot gain another round's income or manufacturing discount.

Buy **1 Material for 2 Credits**. Materials cannot be sold for Credits. Sell intact ordinary equipment for **half its listed Credits value, rounded down**. Consumed items, scrap, Relief gear, included knives, buildings, and fighter bodies cannot be sold. A crafted or stolen item sells at the same half value; the crafting rules never produce it for less than that value. Never count the same item in both a carrier's inventory and stores.

Construct a building by paying its Materials cost and reserving a vacant plot. Prerequisites must already be built; they need not be powered merely to permit construction. You cannot use a prerequisite still under construction to start its dependent structure in the same round. Unless a row says otherwise, only one of each structure may exist. You may build several independent structures in a round. Demolition frees the plot immediately but returns no resources, and removing a prerequisite disables its dependent structures until it is restored. Headquarters cannot be demolished.

Purchase **four additional plots for 40 Materials**, at most three times, for a maximum of twenty-four plots. A plot is an accounting slot, not a placement puzzle. Housing limits owned living people including workers, prisoners, and recovering fighters; Relief Volunteers do not occupy housing. Recruit only if there is space. Destroying or disabling a structure never deletes people or equipment you already own; excess residents may remain, but you cannot recruit until housing is sufficient.

Credits and equipment storage are unlimited. Headquarters stores **250 Materials**; each Storehouse adds 250. At the close of a Settlement round, excess Materials are discarded. You may spend them first. This cap never destroys items or removes Credits already earned.

### Medical treatment and device repair

An operational Clinic can treat one fighter per Settlement round. Pay **30 Credits** and nominate one scar. The fighter must sit out the next battle and cannot work in its following Settlement round; remove the scar after that recovery cycle. The treatment can run concurrently with Convalescence or captivity. It cannot reverse death. You can treat the same fighter again in a later round for a different scar. No Clinic is needed for the ordinary one-battle Convalescence recovery.

An Offline owned device is restored for free between battles. A Destroyed device can be rebuilt at a powered Workshop for **half its listed Credits value, rounded up**, once per device; remove its scrap entry and add the restored item. A utility drone or sentry also requires a powered Drone Bay. Without the required facilities, keep the scrap or discard it. Scrap has no battlefield use and cannot be repeatedly sold. Consumed mines, traps, grenades, rockets, and medical supplies must be replaced at their normal prices.

## 21 Settlement structures

### Structure catalogue

“Power” is the allocation each round. Every row occupies one plot. A prerequisite means the named structure must exist, in addition to any Power needed for that row's own benefit. A discount applies only to the named service, once to its final price, rounded down; it cannot create a negative cost or reduce an item's Crew Rating.

| Structure | Materials | Prerequisite | Power | Benefit | One worker |
| --- | ---: | --- | ---: | --- | --- |
| Headquarters | Free at founding; unique | — | 0 | Housing 12; storage 250 Materials; ordinary recruitment and basic shopping. | None |
| Generator | 40; one free | Headquarters | Produces 10 | Supply 10 Power. Up to three Generators. | +1 Power |
| Materials Processor | 50; one free | Headquarters | 2 | Produce 20 Materials each Settlement round. | +2 Materials |
| Salvage Yard | 50; one free | Headquarters | 2 | Produce 50 Credits each Settlement round. | +5 Credits |
| Bunkhouse | 30 | Headquarters | 0 | Housing +6. Up to three Bunkhouses. | None |
| Storehouse | 25 | Headquarters | 0 | Material storage +250. Up to two Storehouses. | None |
| Workshop | 60 | Headquarters | 2 | Unlock Workshop items, repair devices, and craft up to two eligible items each round. | Crafting price −10% |
| Armoury | 60 | Workshop | 2 | Unlock Armoury items and high-quality firearms. | None |
| Advanced Workshop | 80 | Armoury | 3 | Unlock rockets and approved custom Heavy profiles. | None |
| Clinic | 60 | Headquarters | 2 | Treat one fighter's scar per round; unlock dressings and medical drugs. | Treatment price −3 Credits |
| Drone Bay | 60 | Workshop | 2 | Unlock utility drones and sentries; repair their wrecks at a Workshop. | Their rebuild price −10% |
| Training Yard | 40 | Headquarters | 1 | Retrain one known skill for 20 Credits each round. | Retraining price −2 Credits |
| Comms Mast | 40 | Workshop | 1 | Prepare one Signal Plan per round for 10 Credits. | None |
| Scout Post | 35 | Headquarters | 1 | Prepare one Route Map per round for 10 Credits. | None |
| Smoke Shop | 35 | Workshop | 1 | Craft up to two smoke grenades each round for 3 Credits apiece. Separate from Workshop's two-item limit. | None |
| Medical Stores | 35 | Clinic | 1 | Craft up to two medkits each round for 6 Credits apiece. Separate from Workshop's limit. | None |
| Materials Exchange | 45 | Headquarters | 1 | Buy up to 20 Materials per round for 30 Credits as one batch, instead of the ordinary 40. | None |
| Holding Room | 25 | Headquarters | 0 | Immediate release price for a prisoner is 30 rather than 25 Credits. Does not extend captivity. | None |
| Repair Depot | 35 | Workshop | 1 | One eligible device rebuild per round costs 5 Credits less, minimum 1. Apply after any worker discount. | None |
| Community Hall | 30 | Headquarters | 0 | One Recruit per round costs 55 Credits to hire; their normal 60-Credit body value still counts in Crew Rating. | None |

There are no mandatory food, water, worker-proficiency, building-hit-point, or attention tracks. Settlement buildings provide production, capacity, access, or one named service. They do not add passive to-hit bonuses, extra Wounds, or free units to a Battle Roster.

### Crafting and availability

At a powered Workshop, craft up to two non-human items per Settlement round for **80% of listed Credits value, rounded up**, minimum 1 Credit. You must also have the item's normal unlock operational. A Workshop worker reduces that crafting price by 10%, rounded down, minimum 1. Use the finished item's full listed value when fielding or selling it. This process consumes Credits for parts and labour; Materials remain the construction resource. The Smoke Shop and Medical Stores prices cannot also receive the Workshop discount.

All weapons state their unlock in Chapter 15. Shields, climbing harnesses, frag grenades, and remote clamps need a Workshop. Heavy armour needs an Armoury. Blast mines, smoke emitters, hacking kits, and other ordinary equipment are Basic. Utility drones and sentries need a Drone Bay; its Workshop prerequisite must exist but need not also be powered just to purchase them. Rebuilding or Workshop crafting them requires both powered facilities. Clinic drugs and dressings need a Clinic. Custom weapon variants require at least a Workshop, plus Armoury for range over 24 inches or an Advanced Workshop for Heavy designs.

### Battle preparations

Preparations are single-use items assigned to one fighter before deployment. They use no inventory slot, but count at their **full 10 Credits** in Crew Rating even if prepared earlier. A Battle Roster may take at most one of each. Unused preparations remain in stores; a preparation lost with an unrecovered carrier is lost like other equipment.

- **Signal Plan:** after rolling your crew's initiative, expend it to reroll that die once. The carrier must be conscious, on the table, and not Broken, Bolting, or Bugging Out. Use the new result. It grants no extra turn or action.
- **Route Map:** after both crews deploy, expend it to move its carrier up to 3 inches wholly within its own deployment zone. It cannot interact, Hide, attack, or enter engagement. If both crews use a map, the player who deployed first moves first. It grants no objective progress.

These preparations are examples of settlement development affecting a battle through a paid, limited option. They never raise the agreed Crew Rating or create an automatic advantage for a larger settlement.

## 22 Worked examples

### A six-person founding crew

This example costs exactly **750 Credits** and uses six humans, including one Specialist, one Leader, two Fighters, and two Recruits. Each carries their included utility knife. Stat order below is STR / DEX / AGI / INT / NRV.

| Fighter | Stats | Skills | Equipment | Total |
| --- | --- | --- | --- | ---: |
| Leader | 1 / 2 / 1 / 2 / 3 | Inspire; Rally Training | Assault rifle 35, light armour 10, medkit 10 | 185 |
| Fighter A | 1 / 2 / 1 / 0 / 1 | Mark Target | Assault rifle 35, light armour 10 | 125 |
| Fighter B | 1 / 2 / 1 / 0 / 1 | Split Fire | Assault rifle 35, light armour 10 | 125 |
| Specialist | 0 / 1 / 1 / 4 / 1 | Terminal Training; Technician | Pistol 15, hacking kit 20, light armour 10 | 155 |
| Recruit A | 0 / 1 / 1 / 0 / 1 | — | Pistol 15, smoke grenade 5 | 80 |
| Recruit B | 0 / 1 / 1 / 0 / 1 | — | Pistol 15, smoke grenade 5 | 80 |

Starting with 1,000 Credits leaves 250. Hire two additional Recruits as workers for 120 Credits, leaving **130 Credits** and eight residents. Build a Workshop and Clinic for 60 Materials each, leaving **5 Materials**. Six buildings occupy six of twelve plots. Allocate the Generator's 10 Power: 2 each to the Processor, Salvage Yard, Workshop, and Clinic, leaving 2 unused.

Do not collect production during founding. After the first qualifying battle, the two non-deployed workers can staff the Processor and Salvage Yard, producing 22 Materials and 55 Credits. With a loss or draw, the settlement receives 125 Credits and 20 Materials from the battle as well: **180 Credits and 42 Materials** before other expenses. A win adds another 25 Credits. Injuries, used supplies, and construction still need to be paid for.

### Actions and a reaction

Mara spends her Move to advance into cover. The other player takes an action. Mara later spends her Core to Ready. On a later enemy Move, Mara sees a legal target cross her front arc at a declared point. She spends READY to Shoot there and marks Reacted. The shot hits but fails Injury: the enemy gains Stress and becomes Pinned, ending its unfinished movement. Mara cannot react again this round even if she somehow gains READY again.

A Pinned fighter can wait while its crew takes other actions. Once nearby enemies have spent their attacks and reactions, an exposed target may provide an opening: spend Move to stand, then use the fighter's unused Core to Shoot on a later friendly turn. Until it stands, incoming ranged hits suffer −2. An enemy able to reach it in melee instead gains +2 to hit. Choosing the recovery moment matters; standing immediately is not compulsory.

### Shooting and Injury

A DEX 2 rifle user at Stress 1 shoots a target in heavy cover with two attack dice. They have no other bonus, so each die adds 2 − 1 − 2 = **−1**. Rolls of 16 and 9 become 15 and 8: one hit. The rifle's Damage 2 attacks Armour 1. An Injury roll of 13 becomes 14, so it fails: the target gains 1 Stress and becomes Pinned. A 14 would total 15 and put the target Down instead. The shooter's Stress never modifies Injury.

### Opposed melee

A STR 2 attacker rolls 17 and 8, for totals **19 and 10**. A STR 1 defender rolls 14 and 6, for **15 and 7**. Only the attacker's 19 exceeds the defender's highest 15, so the attacker scores one hit. The defender has no die higher than 19 and scores none. Neither side counts 15+ successes here. If both highest totals were 19, neither would score a hit.

### A casualty's two full rounds

Nico goes Down during round 2. Record “Down 2.” The remaining part of round 2 does not count as a full round. Nico can crawl half MOVE or spend an available Core and medkit to try self-treatment. Friends can attempt treatment too. If still Down after complete rounds 3 and 4, Nico becomes Unconscious at the End Phase of round 4. No further battlefield revival is allowed. If evacuated earlier while still Down and never revived, Nico still makes one post-battle injury roll.

### Terrain as a weapon and a route

A fighter at a terminal successfully HACKS a linked pit cover. Opening the cover reveals a gap and triggers the printed fall procedure for its occupants. Closing a gate through an occupied doorway instead uses that gate's Crush procedure, including the operator test and the victims' escape tests. Both operations spend the same Core used for Shoot or Claim. A second reachable physical control means an opponent can restore the route without buying a hacking kit.

### An advance changes what you can field

A Fighter body originally worth 80 Credits reaches Level 1 and adds +1 INT. Their body is now worth 90 Credits; no treasury Credits are paid for the advance. With a 35-Credit rifle and 10-Credit armour they count as 135. Their settlement must find room for that extra 10 in the next agreed Battle Roster. An old injury does not discount it, and a discounted rifle still counts as 35.

## 23 Roster sheets and reference

### Battle Roster fields

Record the agreed limit, scenario, six-round counter, score, primary and secondary objectives, and crew Passes. For each fighter record:

| Name and grade | Current body value | STR | DEX | AGI | INT | NRV | MOVE | Armour | Weapons and equipment | Skills | Total value |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: |
|  |  |  |  |  |  |  |  |  |  |  |  |

Beside each entry, leave boxes for Move, Core, READY, Reacted, Stress, morale, Pinned, Hidden, Down round, revival used, consumables, and once-per-battle skills. You need only the weapon, skill, and device rules actually fielded; copy their short entries onto the roster or cards.

### Settlement record fields

Keep treasury Credits, stored Materials and capacity, plots, buildings, Power allocation, workers, and pending construction. For each person record training grade, original and current body value, uninjured stats, scars, skills, XP, level, equipment, availability, and any treatment, captivity, or recovery due after a numbered battle. Keep one shared inventory of stored items and device scrap.

At each battle's end, record the score, rewards, actual loot transfers, injuries, XP deeds, advances, production, purchases, construction, and the new balances. Both players should agree transferred items and prisoners before updating their separate records.

### Table reference

Use [[Draft 2 - Battle Quick Reference]] for the condensed battle procedures. The four-page A4 version is intended for two double-sided sheets. Keep fielded profiles, chosen skills, and the agreed terrain cards beside it; the reference does not replace those roster-specific details. Settlement bookkeeping belongs after the battle rather than on the battle reference.

## 24 Campaign and scenario content

### Campaign framework

**[PLACEHOLDER — linked stories, maps, territories, campaign events, organisers' guidance, and campaign endings.]** These may connect battles later. The persistent roster, injury, advancement, settlement, and Crew Rating rules already operate without a campaign.

### Authored scenarios

**[PLACEHOLDER — named missions, illustrated layouts, deployment diagrams, recommended interactive features, and narrative introductions.]** Each scenario must print the information required in Chapter 17. The mission generator is sufficient to play while these are written.

### Setting and presentation material

**[PLACEHOLDER — factions, character examples, artwork, terrain-building photographs, fiction, designer introduction, acknowledgements, and publication credits.]** Add these around the rules without silently creating equipment exceptions or changing the resolution system.
