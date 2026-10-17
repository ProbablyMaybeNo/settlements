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

Each player needs 5–10 human miniatures for a starting crew, a roster, several d20s, one d6, an inch measure, and markers. Use a 36 × 36-inch battlefield, terrain, and a round counter numbered 1–6. Larger crews are legal by agreement but increase play time.

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

For any roll, use only the **largest positive and largest negative modifier from skills**, and likewise the largest positive and negative modifier from equipment characteristics. A skill modifier cannot exceed 4; an equipment characteristic modifier cannot exceed 3. Add these to the stat and applicable position modifiers. Cover is either 0, −1, or −2, never both cover grades. Hidden, rear attacks, Aim, and Stress have their own stated effects and apply once each. Identical effects still never stack.

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

Nominate one fielded fighter as the crew leader for tie-breaking and narrative records. They need not have the Leader training grade; acting leadership grants no stat or action bonus. A crew may include at most one fighter with the Leader grade and one Specialist for every two fielded Recruits or Fighters. Advancement does not change training grade or this ratio unless you promote the fighter.

For each complete five human fighters in the Battle Roster, you may field one Heavy weapon and one powered combat device in total; a sentry turret is a powered combat device. You may also field one utility drone per complete five fighters. A crew below five may field one utility drone but no Heavy weapon or powered combat device. These limits count carried, deployed, and reserve items together. Mines and smoke emitters are not combat devices for this limit.

Use 5–10 fighters for the first games. More are allowed when the agreed limit and terrain support them. The rules do not grant a bonus for spending the limit exactly.

### Carrying equipment

A fighter has **four weapon slots**, **two equipment slots**, and may wear **one armour item**. A one-handed weapon uses one weapon slot; a two-handed weapon uses two; a Heavy weapon uses three. The included knife uses no slot. A grenade uses one equipment slot rather than a weapon slot. Other equipment lists its slots. A fighter may use only two hands at a time.

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

An action costing **Both** spends the fighter's unused Move and Core together. If either is already spent, it cannot perform that action. An unused Move cannot normally become a Core Action. There is no limit on which fighter you choose except its slots and state.

You may spend a Pass instead. Without a Pass, you may only pass if you have no legal action you wish to retain: mark all your remaining slots spent. If one crew has finished, the other completes its actions, still allowing reactions. Once both have finished, resolve the End Phase.

### Action reference

| Action | Cost | Main effect |
| --- | --- | --- |
| Move | Move | Travel up to MOVE and choose facing |
| Aim | Move | Gain +2 on your next Shoot this round; lost if you move first |
| Dash | Both | Move up to twice MOVE; no attack |
| Charge | Both | MOVE + d6, then one melee exchange if successful |
| Shoot or Fight | Core | One attack using Chapter 8 |
| Ready | Core | Gain one READY token |
| Recover | Core | Remove your own Pinned, or help a friendly within 3 inches and LOS remove Pinned |
| Rally | Core | Test NRV to clear Stress and a morale condition on yourself or one friendly within 3 inches and LOS |
| Hide or Observe | Core | Use the stealth rules in Chapter 11 |
| Interact or Hack | Core | Operate one control, objective, or device |
| Deploy or Repair | Core | Place or restore one carried device |
| Treat or Use Item | Core | Use a medkit or another printed equipment effect |
| Loot or Secure | Core | Take an item or capture an incapacitated enemy in contact |
| Reload | Core | Ready a weapon with Reload to fire again |
| Disengage | Both | Leave engagement by the procedure in Chapter 7 |

A fighter may perform at most **one own-turn attack action** each round: Shoot, Fight, or Charge. A reaction attack is separate. Defensive melee participation is not an attack action. A skill may change an action's cost or timing but cannot create an extra own-turn attack. A printed second non-attack Core Action is legal if an ability supplies its cost.

### READY

Ready grants one token, never a second. It can be gained after spending Move and can remain into later rounds. A fighter loses READY when it moves voluntarily, performs any regular action other than Ready, is hit by an attack, becomes Down or Unconscious, is captured, or gains a morale condition. A stationary free facing change made as part of another action does not save READY from that action's cancellation.

A conscious fighter with READY, no morale condition, and no Reacted marker may react. It must see the triggering enemy in its forward arc at the moment of the trigger, within the relevant action's range. Pinned fighters can only use the Dive reaction, and only if they somehow retained READY through a specific skill.

### Reaction windows

After an enemy declares an action, the non-active player may declare **one reaction by one model**. Alternatively, they may wait for a visible point along a declared movement path or the end of the action. Announce the precise point before the model moves past it. The entire action, including a Charge's movement and attack, allows only one reacting model, even if several are eligible.

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
4. Score objectives due this round. Clear temporary effects whose duration is “this round,” including unused Aim and Passes. Resolve smoke, fire, and gas expiry.
5. Check the scenario's end condition. A standard battle ends after round 6.

## 7 Movement facing and visibility

### Facing and LOS

A fighter sees through the **forward 180 degrees** of its base. Draw the dividing line through the base centre; a target whose centre lies exactly on that line counts as in the forward arc. The rear half is outside LOS. A fighter may change facing freely during its own movement and once at the start of its own Core Action. Facing does not change for free during an enemy turn or after an attack is declared.

Agree a normal human silhouette as a cylinder above its base, approximately 2 inches tall. Check LOS from the acting fighter's eye point to the target's head or torso volume; ignore decorative parts. A sliver of weapon, scenic base, or clothing is not enough. Solid walls block sight. Other standing fighters' base-width body volumes block sight, including friendly fighters. For shooting into engagement, use Chapter 8.

Pinned, Down, and Unconscious models use their **base footprint** as the visible target instead of the standing figure. If the attacker cannot see any of that base footprint, it cannot shoot the prone fighter. Area hazards can still reach it. A Pinned fighter checks sight from ground level when it needs LOS for a permitted action. This convention also applies while crawling.

An attack declared from wholly behind the target's dividing line is a **rear attack**. It gains +2 to hit. The target cannot react to that attacker through its rear arc. Close-combat defence and rear charges are resolved in Chapter 8.

### Ordinary movement

Move up to MOVE along a legal path. You may stop early. A normal Move cannot enter within 1 inch of a standing enemy; use Charge instead. You may pass within 1 inch of Down or Unconscious enemies and enter contact to rescue, loot, or capture them.

Cross an unlocked ordinary door as part of movement; opening it is automatic. Closing it deliberately is an Interact. A low obstacle up to 1 inch high costs 2 inches of movement to cross. Difficult ground costs twice the distance travelled. Movement penalties do not multiply: half-speed movement and difficult ground together still halve available movement once. Heavy carrying also uses this rule.

### Dash and Charge

Dash spends Both slots and moves up to twice MOVE. Hidden fighters cannot Dash without first removing Hidden.

Declare a Charge against one visible enemy within **MOVE + 6 inches**, along a plausible route. Spend Both slots, roll one d6, and move up to MOVE plus that result. Reach within 1 inch of the target to succeed; resolve one melee exchange with +1 die on the dominant weapon, within the three-die pool ceiling. On failure, move up to MOVE toward the target along the declared route, stop outside engagement, and end the action. Stress does not alter distance, but applies to any traversal tests and the attack.

You may attempt a risky route as part of a Charge. Resolve its tests at the relevant point. A failed traversal ends the Charge, even if its distance roll was sufficient. A reaction can likewise stop it. Charge does not let a fighter pass through other standing fighters.

### Climbing jumping and falling

Stairs, ladders, and stable ramps use measured movement without a test. Free climbing needs handholds or climbing gear, costs double the vertical distance, and requires one AGI test per action. A failed climb stops at the starting level; natural 1 causes a fall from halfway up the attempted climb. You cannot free-climb a smooth wall without appropriate equipment.

Step across a gap up to 1 inch as normal movement. A gap over 1 and up to 3 inches requires enough movement to reach the other side and an AGI test. Failure means falling into the gap. Wider gaps need a bridge, equipment explicitly permitting the crossing, or a different route. No skill increases the maximum unsupported jump beyond 3 inches.

A deliberate drop of up to 2 inches is safe and costs its vertical distance. For a greater drop or an involuntary fall of more than 2 inches, test AGI: pass and land Pinned; fail and suffer one Damage 3 Injury roll ignoring Armour, then become Pinned if still conscious. Falls over 6 inches automatically fail that AGI test. A fall never kills a fighter on the battlefield. Place a Down casualty at the reachable bottom; if inaccessible, mark its position at the rim and treat it as Unconscious until recovered after the battle.

### Forced movement and carrying

Pushes and pulls follow the shortest stated direction. Stop at an immovable obstruction or another standing base; excess distance is lost. A ledge or open pit is a hazard, not a wall: use the fall rules. A move cannot end with overlapping bases. If terrain closes on a model, use the feature's Displace or Crush rule.

Dragging a casualty, escorting a captive, or carrying a Heavy objective halves movement, prohibits Dash and Charge, and occupies one hand. Two unengaged friendlies in contact can jointly carry one casualty: one spends Move, both use their Move slots, and both move together up to the slower fighter's normal MOVE. A carrier may drop a load without a test at any time during its own action.

### Engagement and withdrawal

Engaged fighters may Fight, Grapple, use a Sidearm in that melee exchange, Recover, Rally themselves, or Disengage. They cannot shoot someone outside the engagement, operate a terminal, Treat, or manipulate an objective. A Pinned fighter is still engaged if an enemy is within 1 inch.

Disengage normally spends Both slots. Test AGI opposed by one engaging enemy's AGI, chosen by the opponent. Pass: move up to MOVE and leave engagement. Fail: move up to half MOVE after that enemy makes one Unanswered melee exchange against you; cancel movement if you become Down. The free exchange is not a reaction and cannot trigger follow-up attacks. Pinned fighters may attempt Disengage, but halve the resulting movement and retain Pinned. Any forced Bolt or Bugging Out movement also allows one such Unanswered exchange, then the survivor moves without an escape test.

Within engagement, a fighter may spend Move to shift up to 1 inch around an enemy, remaining engaged and not entering another enemy's engagement. It cannot cross the enemy base. Both may face each other after a completed melee exchange.

## 8 Shooting and close combat

### Shooting

Choose held weapons and one legal target in the shooter's forward arc, within weapon range and LOS. Declare dice and any optional effects. Roll **1d20 + DEX + modifiers − Stress** for each Attack Die; each 15+ is a hit. Natural 1 misses and natural 20 hits. Apply −1 or −2 for cover, −4 for Hidden when the target is legally visible, +2 for a rear attack, and +2 for a retained Aim. Each hit then makes an Injury roll.

There is no long-range penalty within a weapon's printed range. There is no generic penalty for moving. You cannot shoot beyond range or through solid terrain. Premeasure before spending the action.

A normal Shoot targets one fighter. Split Fire permits allocation to several targets as described in its skill; declare every die's target first. A firearm with three dice does not attack three targets automatically.

### Two weapons and pool limits

Using two one-handed weapons gives the dominant weapon's full dice and **one off-hand die**. Identify that die separately and use its own range, Damage, and traits. Both weapons must be eligible for the attack. A shooting pair must contain two firearms; a melee pair may contain melee weapons or Sidearms. Skill exceptions never raise a combined attack pool above **three dice**, including a Charge die. Remove excess dice of your choice before rolling.

A fighter with only its included knife makes one melee die at Damage 1. Unarmed attacks make one die at Damage 0. A Sidearm may contribute one melee die, using STR to hit and its printed Damage. It does not use DEX in melee.

### Shooting into an engagement

You may shoot an enemy engaged with your friendly fighter, but each natural 1 in that attack pool hits one friendly involved instead, chosen by the opponent. Resolve its Injury roll normally. Other misses remain misses. A blast affects all models in its area, including friendlies; do not add this natural-1 rule to blast attacks.

### Melee exchange

The acting fighter chooses one engaged enemy. Both roll their held melee pools, normally adding STR and their own modifiers to every die; Agile allows AGI instead. An outnumbered fighter suffers −1 to its melee totals for each **additional** conscious, unpinned enemy engaging it, maximum −2.

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

A Pinned fighter may Move at half speed, Recover, Rally itself, or attempt the specified Disengage. It cannot attack voluntarily, Hide, Ready, operate equipment, or use ordinary skill actions. It can still defend in melee. Spend a Core Action to Recover and remove Pinned. Move first and travel at half speed, or Recover first and use normal movement on a later turn. Recover does not remove Stress.

A conscious, unpinned, unengaged friendly within 3 inches and LOS may spend its Core to help the target Recover without a test. This removes Pinned only; it does not cure Down or a morale condition. The target keeps its own remaining slots.

### Down and Unconscious

Leave a Down fighter on the battlefield, mark its base, and record the **round it went Down**. Remove READY, Hidden, Marked, Aim, and any sustained skill effect. Retain Stress. It cannot control or contest objectives and drops carried mission objects into contact with its base. It retains its personal equipment until looted.

A Down fighter may only crawl up to half MOVE using its Move slot and attempt self-treatment with a carried medkit using its Core slot. Being Down neither refreshes slots already spent nor grants an immediate crawl. Crawling cannot engage an enemy, use equipment other than self-treatment, or interact with objectives. It provokes ordinary reactions when visible.

At the End Phase **two rounds after the round in which it went Down**, it becomes Unconscious. The partial round in which it fell does not count. A fighter Downed in round 2 therefore becomes Unconscious at the end of round 4. This gives it all of rounds 3 and 4 for rescue.

Unconscious fighters stay on the table but cannot act, react, or be revived during that battle. They may still be carried, looted, or captured. They have not been declared dead.

### Treat and self-treatment

A medkit is a single-use consumable. A conscious, unpinned, unengaged fighter in contact with a Down friendly may spend its Core and a medkit to test INT. Success restores one Wound, removes any morale condition, and leaves the patient Pinned at **2 Stress**. Failure spends the action and medkit but does not alter the Down timer. Natural 1 has no additional medical penalty.

A Down fighter carrying a medkit may use the same action on itself. For **self-treatment only**, ignore its Stress penalty: the attempt represents applying prepared emergency aid. An assisting fighter uses its own normal INT test and Stress. One fighter may be successfully revived **once per battle**. Record that use on its card. A later Down still allows crawling and capture but cannot be revived again that battle.

Treatment never restores spent action slots. A patient revived with a Core slot still available must spend it Recovering before doing other work, unless a friendly helps it. A revived fighter retains injuries from earlier battles. Medical aid in battle does not erase a lasting injury.

### Attacks against casualties

A Down or Unconscious fighter cannot be used as a shield for another model and does not block movement or LOS. Attacks may target a visible Down fighter using normal shooting or one automatic melee hit from contact. A successful Injury roll makes it Unconscious immediately. It does not kill it, roll lasting injuries early, or add further post-battle injury rolls. Further attacks on an Unconscious fighter have no additional rules effect. There are no battlefield execution rules.

### Loot

An unengaged fighter in contact with a Down or Unconscious model may spend Core to take **one carried item**, including an unused medkit, or one carried objective already on the ground. No test is needed. The looter must have space; it may drop an item into contact to make room. Removing armour requires a whole Both-slots action instead. The included utility knife and clothing have no resale value.

Mark ownership transfers immediately. A looted item exists in only one place. A weapon taken this way is not held until the looter next makes a permitted weapon choice. Carried loot is not added to the starting Crew Rating during the battle; it must be fully counted in later battles. A dropped item remains where it fell and can be picked up with Interact.

### Capture and evacuation

An unengaged fighter in contact with a Down or Unconscious enemy may spend Core to **Secure** it. This is automatic if no conscious, unpinned enemy is within 1 inch of either model. Mark Captured. The captive cannot act or self-treat. Its Down timer continues normally.

The captor may escort or drag one captive using the carrying rules. Move both bases together, keeping them in contact. Capture becomes a lasting capture only when the captive is escorted completely off the captor's deployment edge while the escort remains capable of moving. An Unconscious captive can be dragged in the same way.

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

A fighter with a morale condition cannot react, give assistance, score, or contest. Bolting and Bugging Out movement overrides Pinned and spends the fighter's remaining slots even if it reaches its destination early. Movement remains subject to physical obstacles and traversal tests. Bolting never deliberately takes a hazardous route when a safe one exists. Bugging Out may take one if it is the shortest legal way out. If no destination can be reached, move as far along a legal route toward it as possible; if no route exists, remain in place and spend the slots. The owner breaks equal-distance route ties.

A fighter that flees off-board is Withdrawn, not Down, and does not roll an injury merely for fleeing. Any casualty it was carrying is released at the point it started fleeing.

### Rally

A fighter already carrying Broken, Bolting, or Bugging Out at the beginning of the End Phase makes **Rally instead of Break**, using the same Stress-free NRV test. Success removes the morale condition, all Stress, and Pinned. Failure retains its current condition, even if Stress changed. It never immediately rerolls a new Break failure in that End Phase.

A Core Rally action may be attempted by the affected fighter if Broken, or by a conscious, unpinned, unengaged friendly within 3 inches and LOS. Test the acting fighter's NRV, ignoring Stress. Success removes all Stress, the morale condition, and Pinned from the target. Rally may also be used on a stressed fighter with no morale condition. Failed Rally has no additional effect beyond its action cost.

Bolting or Bugging Out fighters need friendly help or the End Phase to Rally. They cannot spend their forced action on self-Rally. Removing Pinned alone does not remove a morale condition.

### Voluntary withdrawal

At the start of any of your turns, you may withdraw the crew and end the battle. Resolve current casualties and post-battle procedures normally. The opponent wins, but you retain rewards already earned and evacuated loot. Remaining uncaptured fighters and casualties return to their own settlement; an on-board captive that was not extracted is released. There is no bonus round of unopposed killing or looting. Scenario-specific extraction rewards still require actual extraction before withdrawal.

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

Every interactive feature has a physical control in contact with it or at a marked nearby panel. Electronic features may also be linked to a **terminal**. A terminal may link up to three features within 12 inches; draw or label these links before play. Links ignore intervening walls but cannot chain through another terminal to reach farther. Either crew can use the same terminal.

An unengaged fighter in contact with an active terminal may spend Core and test INT to **Hack** one linked feature. Success performs one printed operation immediately. Failure changes nothing. A natural 1 **Freezes that terminal until this round ends**. Freeze affects remote electronic use through that terminal; it never disables local manual controls.

No specialist skill or hacking kit is required to use a terminal. Tools and training improve reliability. Any crew can instead reach the feature's direct control. A physically locked door can be forced or picked; hacking is another route, not the only route.

### Portable hacking and interference

A hacking kit also permits an INT Hack against one visible electronic deployable or drone within **8 inches**. Success disables it until someone Repairs it. Failure leaves it unchanged. Natural 1 also prevents that kit being used again this round. This does not hack human fighters, their firearms, or their ordinary armour.

Hijacking a device for an immediate operation requires Trojan. Opposing a terminal operation requires Interrupt and READY. There is no separate cybercombat phase, bandwidth resource, or list of attack programs.

### Repair and sabotage

Repair requires contact, Core, and an INT test. Success restores an Offline device or clears a disabled electronic state. A Destroyed device cannot be repaired during battle. Normal failure does not worsen it.

Critical terrain and objective terminals cannot be shot out of the game. They can be temporarily Frozen, or disabled by a scenario's sabotage objective. A sabotaged feature stays in its last safe position and can be repaired with the ordinary Repair action unless the scenario explicitly sets a different objective procedure. Do not invent hit points for whole buildings.

### Improvised actions

Players may propose an action that follows from the physical scene. Agree its **object, intended effect, Core or Both cost, relevant stat, and failure consequence before committing**. Use an existing operation such as Shove, Displace, Open, Close, Move Cover, or Create Smoke whenever possible. Ordinary people and the tools present must plausibly be able to do it.

One improvised action normally affects one target or one terrain piece. It cannot exceed the common move distance, create a free attack, erase a scenario objective, or destroy an entire building. Throwing a hand-carried box or tipping a cabinet is plausible; throwing a car is not. Dangerous and difficult attempts use a normal test, not an invented modifier table. If you cannot agree quickly, use the nearest printed action for this battle and discuss a future addition afterwards.

## 13 Interactive terrain catalogue

### Feature cards

Give each feature a card showing its **footprint, control point, linked terminal, possible states, operation, and any hazard area**. Use two states whenever possible. A single card belongs beside the relevant terrain. Scenarios can choose from this catalogue; players may rename the same mechanics to suit their models.

**Displace:** move an affected fighter the shortest distance up to 2 inches to a safe legal position outside the changing area, chosen by its owner. If none exists, the operation stops before trapping it unless the feature explicitly has Crush.

**Crush:** each affected conscious fighter tests AGI. Pass: Displace it safely. Fail, or no safe destination: one Damage 3 Injury roll ignoring Armour, then Pinned if still conscious. Move a casualty to the nearest accessible edge of the hazard footprint. Down or Unconscious casualties cannot evade, but are never removed as dead. A feature cannot affect the same fighter with Crush more than once per round.

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
| Smoke emitter | 15 | 1 | Single-use, electronic. From a terminal linked during setup or a hacking kit within 8 inches, operate it to create ordinary smoke for this and the next round. |
| Remote clamp | 15 | 1 | Single-use, electronic. First human entering within 1 inch tests AGI. Failure Pins it and ends that movement; success continues. Consumed either way. |
| Sentry turret | 50 | 2 | Electronic. Stationary, 180-degree arc chosen at deployment, range 12 inches, DEX 2, one Attack Die, Damage 2. Gains one READY each Start Phase; it may react once that round. |
| Field supply case | 15 | 1 | Deploy an open cache containing one medkit and one smoke grenade. These two contents replace the case; they cannot be sold as extra profit because its total value equals their 15 Credits. Picking up each is an Interact. |

For mines and traps, **either crew can trigger them**. Placing one is a positional decision, not permission for your own fighters to walk through it safely. A flying drone does not trigger a ground-contact tripwire or clamp; it can trigger an electronic proximity mine if actually within its three-dimensional radius.

Turrets use the owner's one-reactor window, including Return Fire if targeted. They have no normal action slots. Operating a turret with a Core action can turn its facing or fire one shot, but expends its READY and marks it Reacted; this cannot give it a second attack that round. It may be operated only from contact or a portable hacking kit within 8 inches; friendly operation is automatic, enemy operation needs Trojan. It cannot fire without a READY token. A turret's reaction requires its own LOS, not its operator's.

### Utility drones

A utility drone costs **45 Credits**, occupies two equipment slots on its operator, and counts toward the crew's drone limit. Assign its operator on the Battle Roster. It has no weapon, no independent actions, no READY, and cannot score, contest, capture, carry mission cargo, or earn experience.

Deploy it from the operator's base with a Core Deploy action, automatically. On a later turn, spend the operator's **Move** to move the drone up to 8 inches, instead of moving the operator. It may fly over low obstacles but not through solid terrain. Keep it within 12 inches of the operator and no higher than 6 inches above the surface below it. Measure its real flying position; use a stand or height marker. It may finish hovering or on a stable surface. Its LOS uses its actual height and a 360-degree camera.

Spend the operator's **Core** to perform one of these through the drone:

- Operate a physical terrain control in contact with the drone, using the normal automatic operation or the operator's INT test for a dangerous operation.
- Hack through a terminal in contact with the drone, using that terminal's normal links and the operator's INT.
- Observe one Hidden fighter or concealed device within 12 inches and the drone's LOS, using the operator's INT.

The operator must be conscious, unpinned, unengaged, and free of a morale condition. Use the operator's Stress on its tests. Remote operation can change terrain, but **cannot Claim, Secure, loot, defuse a mission bomb, or complete an objective that requires a human interaction**. A scenario may expressly allow a drone operation as one step, not assume it can replace every human task.

If the operator becomes unavailable or moves out of control range, the drone stays inert at its position until control is restored. It remains targetable. Another friendly in contact with the drone may spend Core to become its operator, provided it has two equipment slots available; update both cards. Returning the drone to its operator's base and spending Interact packs it away.

A single successful hit destroys a drone; there is no armour or Injury roll. Place a wreck marker. It may be recovered like an item, including by an enemy. This makes remote access useful but exposed, and prevents a flying device becoming a second combatant for free.
