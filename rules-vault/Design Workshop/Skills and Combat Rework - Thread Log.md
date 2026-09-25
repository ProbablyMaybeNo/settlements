---
type: working-discussion
status: historical discussion; skill catalogue integrated 2026-09-25
created: 2026-09-20
updated: 2026-09-25
tags:
  - settlements/workshop
  - settlements/skills
  - settlements/combat
---

# Skills and Combat Rework — Thread Log

> [!important] Design history — current skills now integrated
> On 2026-09-25 Ross authorised replacing the live skill system. The canonical list is [[Rules System/Skills]]; this log preserves prior discussion and superseded proposals. Acquisition is explicitly undecided. The broader core mechanics remain subject to the integration decisions note.

> Earlier boundary, retained for history:
> This note tracks the discussion in this Codex task. It is outside `Rules System/` and does not amend the master, rules records, ledger, or roadmap. Decisions here are workshop directions until Ross explicitly authorises integration. The vault's scheduled mirror may copy this file into the repository; that does not make it authoritative.

## How to use this log

- Add subsequent discussion to the dated journal and update the current direction and open questions.
- Distinguish **Ross's direction**, **assistant proposal**, **unresolved**, and **superseded**. Do not turn an assistant suggestion into an adopted rule through repetition.
- Preserve prior wording when a substantial change needs comparison. Keep the current direction prominent.
- Keep skill effects concise; put shared rules and edge cases outside the effect text where possible.
- This is a structured discussion record, not a verbatim transcript. The earlier 60-skill draft is preserved below. Ross's newer 75-skill Sheet is captured separately in [[Skills Table Snapshot - 2026-09-22]], with review in [[75 Skills - Archetype and Combo Review]].
- Maintain this note as this task continues. No background automation or automatic capture has been configured.

## Current direction at a glance

| Topic | Current workshop direction | Status |
| --- | --- | --- |
| Skill count | 15 skills per stat, 75 total, all in one tier. Latest first-pass Sheet reviewed 2026-09-22. | Ross increased count; supersedes 12 per stat |
| Skill purpose | Define tactical approaches and unit archetypes. Combat and defensive benefits are allowed. Avoid universally useful numerical upgrades with no interesting decision. | Ross directed |
| Combinations | Support combinations within a stat and across stats. Players should discover interactions rather than receive mandatory build recipes. | Ross directed |
| Signature themes | STR Grapple; DEX Spotted/Marked; INT Hacking; AGI Ambush; NRV local buffs/debuffs rather than one signature state. | Ross proposed; structure still exploratory |
| Avoid mandatory builds | Signature mechanics should support some skills without making the other choices unattractive. Follow-ups should normally work independently. | Shared design direction; exact implementation untested |
| Dice | The working system uses d20s. The older master text used in earlier answers still said d10. | Ross corrected; full d20 specification not supplied here |
| Positive skill bonuses | Increase the drafted +1 bonuses to +2. | Ross directed; not yet applied to the preserved catalogue below |
| Positive modifier cap | Combined positive modifiers cap at +6 on d20, replacing +3. | Ross confirmed; negative cap not specified |
| Hidden and Marked | Hidden gives -4 to be hit and prevents targeting beyond 12 inches. Marked or any successful hit removes Hidden; a complete miss leaves it intact. Check exposure at start/end of the Hidden unit's activation: enemy within 12 inches with LOS removes Hidden. Enemy movement into LOS alone does not reveal. | Ross clarified activation timing and hit-based reveal; master unchanged |
| Ordinary attack outcomes | Every successful ranged or melee hit gives 1 Stress, whether or not it wounds, capped at 5 total Stress. | Ross clarified; working direction, not master integration |
| Suppressed | Remove the separate condition. | Ross directed |
| Pinned | A qualifying skill or weapon may Pin on a ranged hit that does not wound. Self or friendly spends an action point to Recover. No additional Stress for Pinning. | Ross clarified; previous friendly range was 3 inches; detailed restrictions pending |
| Stress | Each point gives -1 to rolls, maximum 5 Stress / -5. The flat Shaken -2 proposal is superseded. | Ross clarified; general modifier-cap interaction and NRV procedure pending |
| Master integration | Keep everything separate until ideas are fleshed out and reviewed. | Ross explicitly directed |

## 1. Design intent and category boundaries

### Original brief

Ross wanted tangible, consistent categories explaining how units gain capabilities, become stronger, and suffer lasting consequences:

- **Weapons:** primary source of offensive output: Damage, attack count, accuracy, range, penetration, cover interaction, blasts, and payloads.
- **Armour:** primary source of protection; no offensive benefits.
- **Skills:** initially restricted toward movement, handling, actions, and non-combat tests rather than direct offence or defence.
- **Equipment:** temporary or limited-use benefits that may cross the other categories, with clear consumption and replenishment.
- **Advancements:** permanent positive changes to stats, Wounds, and movement, plus character development.
- **Injuries:** lasting penalties and narrative consequences, with explicit recovery where relevant.

The separate existing [[Rules System/Modifier Design Framework|Modifier Design Framework]] records an earlier version of those boundaries. It has not been changed by this discussion.

### Revised skill identity — supersedes the strict original restriction

Ross found the strict approach made skills too weak and peripheral. Skills should be a primary part of a unit's function. Direct combat and defensive effects are permitted when they support a distinctive tactical approach.

> **Working definition:** Skills represent distinctive fighting techniques, training, and behaviours. Each should change tactical decisions or reward a particular approach. Skills may affect attacks, defence, movement, control, or support, while avoiding unconditional improvements that suit almost every unit equally.

The other category identities remain useful, but the old ban on skills affecting lethality or survivability no longer describes this workshop's direction. Whether skills may permanently change characteristics or Wounds was not separately settled by lifting that ban.

### Combination principles

- Each skill should have an independent use; another skill can improve its opportunities or payoff.
- Shared triggers can include Grappled, Marked, Hidden, movement, Ready, Stress, and defending melee.
- Permit cross-stat combinations, including stat substitution interacting with applicable test bonuses.
- Do not publish compulsory paths or hand players all the combinations as recipes.
- Keep powerful interactions, but constrain infinite attacks, repeated activation denial, and contradictory targeting demands.
- Evaluate actual action costs and counterplay, not merely whether a rule sounds like utility or damage.

Ross illustrated the goal with a Barons War defensive/counterattack interaction, an AGI-in-melee plus AGI-bonus pairing, and forced-targeting interactions with defensive or intimidating skills. These were illustrative design examples, not adopted Settlements mechanics.

## 2. Stat identities and signature mechanics

| Stat | Broad identity | Signature theme | Alternative approaches to support |
| --- | --- | --- | --- |
| STR | Physical dominance | Grappling and displacement | Charging aggression; protecting allies and holding space |
| DEX | Control of a firefight | Marking and exploiting targets | Mobile gunfighting; suppression/control; overwatch |
| INT | Preparation and battlefield manipulation | Hacking | Engineering/demolition; medicine; combat analysis |
| AGI | Choosing where and when to engage | Ambush | Evasive duelling; traversal; objective running |
| NRV | Influencing behaviour under pressure | Local buffs and debuffs | Resolve; aggressive momentum; leadership |

Assistant design suggestion, not a locked quota: roughly three overlapping groups of four skills per stat, with three or four interacting with the signature theme. The groups should be invisible as prerequisites to players.

Useful review test: can a player build two compelling units from a stat without its signature skill, and another centred on it?

Ordinary hacking should remain available through core actions; the Hacker skill improves it rather than being required to participate. Similarly, ordinary concealment should not require Ambush.

## 3. Grapple discussion

Grapple went through several proposals:

1. An opposed STR Action temporarily preventing both units moving, expiring at the grappler's next activation. Rejected as weak and awkward: it expired before the grappler could exploit it on the next activation.
2. A melee-win replacement that also prevented two-handed weapon use. Still did not provide a clear enough primary purpose.
3. **Grab and drag:** opposed STR Action; hold the enemy and move both at half MOV. This is the latest catalogue basis.

Current draft purpose: move an enemy off an objective, out of cover, away from a doorway, or toward allies. Throw and Heavy Hands benefit without requiring Grapple as a prerequisite.

Open details: opposed escape timing, who counts as defender, attacks while held, size/carrier restrictions, environmental hazards, and repeated holds. The latest draft prohibits dragging across drops but lets Throw resolve falls; that difference needs deliberate review.

## 4. Latest complete skill catalogue — preserved snapshot

> [!warning] Baseline snapshot, not a reconciled current rules list
> These are the 60 skills formatted in the conversation before the subsequent d20 bonus and condition changes. **+1 bonuses are intentionally preserved here for traceability.** Ross subsequently directed +1 bonuses to become +2. Suppressed and references to Shaken also need reconciliation. Notes below identify affected areas; no revised balance is implied.

No additional selection prerequisites were assigned. Equipment and use conditions belong in Effect/Notes. Stat eligibility and skill-count rules remain unresolved. Repetition of `None` in the prerequisite column is not a ruling that recruits or every stat value gain unrestricted skill access.

### Shared rules proposed alongside this snapshot

- Action/Move spends that activation slot.
- Normal tests, movement, reaction rules, and weapon requirements apply unless overridden.
- Maximum one skill-granted bonus attack per unit per round; no bonus-attack chains.
- Auras require LOS; stop while their source is Down, Out, or Broken; identical effects do not stack.
- Until next activation means until its start, unless the text says through/end of that activation.
- Attack replacement effects replace all Injury rolls and surplus-hit effects from that attack.
- One received Order per unit per round; Orders cannot chain.
- The old +/-3 modifier cap was assumed in the draft; its compatibility with d20 bonuses and cumulative Stress is now open.

### Type labels

**Action:** spends Action. **Move:** spends Move. **Passive:** ongoing permission or conditional modifier. **Triggered:** effect used when an event occurs. **Reaction:** uses Ready and reaction. **Attack option:** modifies a normal attack rather than being a separate activation Action.

### STR

| Skill | Stat | Type | Effect | Prerequisites | Notes |
| --- | --- | --- | --- | --- | --- |
| Grapple | STR | Action | Opposed STR against an adjacent enemy. Success locks both in contact; you may drag both at half MOV using Move. Neither attacks outsiders. Enemy escapes with an Action and opposed STR, or by wounding you. | None | Release freely; separation, Down, or Out ends it. No dragging across drops. |
| Throw | STR | Action | Opposed STR against an adjacent enemy; +1 if Grappled. Throw it 3 inches and Pin it, ending your hold. Collision Pins both units. | None | Stop at obstructions; falls resolve normally, otherwise no Injury. |
| Knockback | STR | Triggered | On winning melee, replace Injury with a 2-inch push. You may follow without a disengagement attack from that target. | None | Stop at obstructions; falls resolve normally. |
| Heavy Hands | STR | Passive | +1 melee against Grappled, Pinned, or Prone enemies. | None | Multiple qualifying conditions do not stack. |
| The Bull | STR | Passive | +1 Injury on a Charge whose final 3 inches follow a straight, unobstructed path. | None | Declare route before moving. |
| Rampage | STR | Triggered | Once per round, after taking an enemy Out in melee during your activation, move 2 inches and make a bonus Fight against another enemy. | None | Must be unengaged before moving. |
| Come Get Some | STR | Action | Opposed STR against enemy NRV within 6 inches and LOS. Its attacks next activation must target you if legal. | None | Other actions remain allowed. |
| Weather the Storm | STR | Passive | After one enemy completes an attack against you, Injury rolls from other enemies suffer -1 against you that round. | None | Not additional dice from the first attack. Negative modifier has not been authorised to double. |
| Bodyguard | STR | Triggered | Once per round, redirect an adjacent ally's incoming ranged attack to yourself before rolling, if legal. | None | Use your protection; no further redirection. |
| Rooted | STR | Triggered | Pass STR to resist an enemy push, pull, drag, or throw. Other effects remain. | None | Cannot prevent falling when support disappears. |
| Breakthrough | STR | Triggered | During Move or Charge, test STR to breach one Breachable obstacle without an Action. Success opens it and movement continues; failure stops you. | None | Normal movement allowance. |
| Strong Back | STR | Passive | Ignore movement penalties for casualties or cumbersome objectives; may Sprint carrying either. | None | No Charge carrying casualties; capacity/carrier requirements remain. |

### DEX

| Skill | Stat | Type | Effect | Prerequisites | Notes |
| --- | --- | --- | --- | --- | --- |
| Mark Target | DEX | Action | Pass DEX against an enemy within 18 inches and LOS to Mark it this round. Friendly ranged attacks reduce its cover penalty by 1, including Hidden. | None | No Stress, no removal of Hidden, no shots through blocked LOS. Whether this benefit becomes 2 is unresolved. |
| Run N' Gun | DEX | Passive | Split Move around Shoot. | None | Total remains MOV; reactions after each qualifying segment. |
| Gunslinger | DEX | Triggered | After shooting a sidearm during your activation, bonus shot with another sidearm at a different target: one Attack Die, -1 hit. | None | Both spend ammunition; bonus-attack cap applies. |
| Deadeye | DEX | Passive | +1 ranged hit against open or Marked targets if you have not moved this activation. | None | Taking bonus prevents later movement that activation. |
| Sniper | DEX | Move | Reduce Light/Heavy cover penalty by 1 for your next Shoot this activation. | None | Not Hidden. Whether this becomes 2 is unresolved. |
| Crossfire | DEX | Passive | +1 Injury against Marked enemies or enemies hit by another friendly's ranged attack earlier this round. | None | Either condition qualifies; no double bonus. |
| Pin Them Down | DEX | Attack option | Declare before shooting. Any hit replaces damage with Suppressed: no movement/reactions until Move is spent to clear it. | None | OBSOLETE CONDITION: rewrite after removing Suppressed. Previously replaced all Injury/surplus effects. |
| Called Shot | DEX | Attack option | Nominate a weapon before shooting. Any hit may replace damage by disabling it through the target's next activation. | None | Replaces all Injury/surplus effects; Action restores weapon early. |
| Ready to React | DEX | Reaction | Spend Ready/reaction to Snap Shot a charger before it moves. | None | Charger must already be a legal shooting target. |
| Calm Under Fire | DEX | Triggered | Once per round, retain Ready after an attack hits without wounding you. | None | Conditions and Stress still apply. |
| Speed Loader | DEX | Move | Reload one weapon using Move instead of Action. | None | Ammunition requirements remain. |
| Eagle Eye | DEX | Passive | +6-inch range against Marked targets, or if stationary this activation. | None | Maximum 36 inches; existing beyond-24 restrictions retained provisionally. Not a +1 bonus to double. |

### INT

| Skill | Stat | Type | Effect | Prerequisites | Notes |
| --- | --- | --- | --- | --- | --- |
| Hacker | INT | Passive | +1 hacking; access terminals within 3 inches and LOS instead of contact. | None | Normal equipment and hacking restrictions. |
| Counter-Hacker | INT | Triggered | Once per round, successful Interrupt does not Overload your terminal. | None | Normal Interrupt requirements. |
| Remote Operator | INT | Action | Operate a friendly Linked deployable within 12 inches using its normal actions/profile. | None | Attack consumes your attack allowance and respects device firing limits. |
| Systems Operator | INT | Move | After operating infrastructure physically or by hacking, spend unused Move to Ready. May delay the change until activation ends. | None | Conditional Move expenditure. |
| Jury-Rig | INT | Action | Touch an Overloaded terminal or disabled repairable friendly device; pass INT to clear Overloaded or complete normal repair. | None | No ammunition, charge, or destroyed-equipment restoration. |
| Combat Engineer | INT | Passive | Deploy devices using Action instead of both slots. | None | No device attack during that activation. |
| Demolitionist | INT | Passive | Use INT for grenade throws and charge placement. On grenade hit, shift blast centre 1 inch while keeping original target inside. | None | Does not grant Blast. |
| Predictive Fire | INT | Passive | Use INT instead of DEX for ranged Snap Shots using Ready. | None | Normal weapon rules/modifiers. |
| Exploit Weakness | INT | Action | Pass INT against enemy within 12 inches and LOS. Next friendly attack against it this round ignores 1 Armour, minimum 0. | None | Miss consumes effect. Whether magnitude becomes 2 is unresolved. |
| Medic | INT | Passive | +1 Stabilize; ignore missing Med-Kit penalty. | None | Normal Action and recovery. |
| Triage | INT | Reaction | Spend Ready/reaction to Stabilize adjacent ally after the attack that Downs it finishes. | None | Cannot rescue directly Out units. |
| Salvager | INT | Triggered | After successful Search, roll twice for discovery and choose one result. | None | Resolve only chosen result and consequences. |

### AGI

| Skill | Stat | Type | Effect | Prerequisites | Notes |
| --- | --- | --- | --- | --- | --- |
| Ambush | AGI | Passive | Start activation Hidden: first attack gains +1 hit/melee against enemy within 6 inches that could not see you at activation start. | None | Moving/attacking remove Hidden normally. |
| Low Profile | AGI | Passive | Move up to 3 inches Hidden without revealing, entirely in Concealing terrain and outside Engagement. | None | Other actions break Hidden normally. |
| Vanish | AGI | Move | Hide using Move instead of Action. | None | Suitable terrain; no enemy within 6 inches with LOS. |
| Finesse | AGI | Passive | Use AGI instead of STR in melee with Unarmed or one-handed melee weapons. | None | Applicable AGI modifiers; Damage unchanged. |
| Footwork | AGI | Passive | After voluntarily moving 3 inches during your activation, +1 AGI tests and AGI-based melee for that activation. | None | Underlying AGI unchanged. |
| Riposte | AGI | Triggered | Once per round, after losing enemy-initiated melee without a wound, bonus Fight if still Engaged. | None | Incoming effects resolve first. |
| Hit and Run | AGI | Triggered | Once during your activation, move 2 inches after a Fight you initiated. That opponent gets no disengagement attack. | None | Others still do; must be able to move. |
| Rolling Dodge | AGI | Passive | Winning Dodge does not give you Pinned. | None | Normal Dodge movement/reaction cost. |
| Parkour | AGI | Passive | Each Move/Charge ignores first low obstacle's 2-inch cost. One AGI test at first climb/jump/vault covers remaining maneuvers. | None | Failure at first maneuver; distances still cost movement. |
| Action on the Run | AGI | Passive | Split Move around Interact, including objectives. | None | Spend Action/test at interaction point; total remains MOV. |
| Scramble | AGI | Triggered | Once per round, when enemy attack Pins you, move 2 inches despite Pinned. | None | Remain Pinned; cannot enter Engagement. |
| Sidestep | AGI | Reaction | When charged, spend Ready/reaction to move 2 inches before charger moves. It pursues; if unreachable, moves toward you without attack or retarget. | None | Must be unengaged and able to move. |

### NRV

| Skill | Stat | Type | Effect | Prerequisites | Notes |
| --- | --- | --- | --- | --- | --- |
| Rally | NRV | Action | Pass NRV: remove 1 Stress from self and up to two allies within 3 inches, or end Bolt/Broken on one ally within 6 inches. | None | LOS; cannot reverse BugOut. Stress removal is not a +1 roll bonus. |
| Hold the Line | NRV | Move | 3-inch aura until your next activation: self/allies +1 defending melee. | None | Ends if you move. |
| Fire Discipline | NRV | Move | 6-inch aura until your next activation: self/allies +1 ranged hit against open targets when stationary throughout shooting activation. | None | Re-evaluate aura strength after +2 conversion. |
| Advance! | NRV | Action | Up to two unengaged allies within 3 inches and LOS each move 2 inches without entering Engagement. | None | Resolve separately; each is a received Order. |
| On Your Feet | NRV | Action | Clear Pinned from self and up to two allies within 3 inches and LOS. | None | Does not remove Stress or other conditions. |
| Inspiring Example | NRV | Triggered | Once per round, after your attack wounds an enemy, one ally within 6 inches and LOS removes 1 Stress. | None | Not yourself. |
| Dread Presence | NRV | Passive | Enemies within 6 inches that see you suffer -1 Break tests. | None | Identical effects do not stack; negative magnitude unchanged pending decision. |
| Intimidating | NRV | Passive | Charging you/allies in your 3-inch aura requires NRV. Failure bars charging anyone protected by you that activation. | None | Once per charger activation; alternatives remain without spending slots. |
| Take It on Me | NRV | Action | Transfer up to 2 total Stress from allies within 3 inches and LOS to yourself. | None | New Stress applies immediately. |
| Red Mist | NRV | Attack option | Once during activation, gain 1 Stress for +1 on one melee roll. If now at 2+ Stress, ignore Shaken's penalty for that roll. | None | NEEDS REWRITE: cumulative Stress replaces separate Shaken penalty. Take Stress even on failure. |
| Bloodlust | NRV | Triggered | Once per round, taking an enemy Out in melee removes 2 Stress from you, including when defending. | None | Re-evaluate with cumulative Stress. |
| Commanding Presence | NRV | Triggered | Once per round, ally within 6 inches and LOS may use your NRV for its Break test. | None | Its own Stress and modifiers apply. |

### Formatting preferences

- Requested player-facing columns: **SKILL | STAT | EFFECT | PREREQUISITES | Notes**. A separate Type column was subsequently requested.
- Ross prefers very concise effects, with shared rules/edge cases elsewhere.
- For Google Sheets paste, use plain text in a code block: one physical line per cell, no header or blank lines unless requested, preserving row order STR/DEX/INT/AGI/NRV.
- Ross requested an apostrophe before plus signs to avoid formula interpretation. Treat this as export formatting, not game notation. Use `2 or more Stress` instead of corrupting `2+` to `2'+`.

## 5. Dice and modifier discussion

### Correction

The assistant initially used the older d10 master and calculated +1 as a 10-percentage-point change. Ross corrected that this system now uses **d20s**. Those earlier numerical examples are not current-system evidence.

For a flat d20 threshold, away from automatic-result limits and modifier caps:

- +1 changes a single roll by **5 percentage points**.
- +2 changes a single roll by **10 percentage points**.
- An illustrative attack with 50% hit and 50% Injury has 25% wound chance. A +1 to either stage gives 27.5%; +1 to both gives 30.25%.
- These are illustrative calculations, not measured balance or confirmed current thresholds. Reactions, opposed melee, Attack Dice, armour, and cover change the result.

Ross's response: **"I'll just hike +1 bonuses to +2."**

Record this as a direction for drafted positive skill bonuses. Do not silently double Stress gains, penalties, base Damage, Armour, stat values, or all numerical effects. Cover reduction and Armour-ignore effects need an explicit scope decision.

The assistant suggested that capabilities and action interactions should carry identity, with numerical bonuses rewarding their use. +2 is a starting baseline, not evidence that all skills now have equal value.

## 6. Pinned, Suppressed, and attack outcomes

### Original written distinction used in the conversation

- Pinned: no Move/Charge/Sprint/Disengage; spend Move to clear; Shoot/Interact remain possible.
- Suppressed: Pinned plus no reactions.
- A ranged hit that failed Injury applied Pinned and 1 Stress; a melee hit that failed Injury applied Stress without Pinned.
- Being hit normally cancelled Ready separately, making the extra reaction prohibition feel less distinctive.

### Proposals considered, then superseded

1. Ross proposed Suppressed also prohibit Shoot and Interact.
2. The assistant noted that clearing it with Move would still leave an Action, and proposed spending both slots to clear it. This was a proposal, not a final adopted rule.
3. When Ross asked to unify ranged/melee results, the assistant briefly proposed ordinary failed Injury giving Stress only, with Pinned/Suppressed reserved for control attacks.
4. Ross instead chose to **remove Suppressed and apply Pinned as the additional consequence of a hit that fails to wound**. This supersedes the previous branches.

### Latest workshop attack outcome

| Result | Effect |
| --- | --- |
| Miss | Nothing |
| Hit, successful Injury | Lose 1 Wound |
| Hit, failed Injury | Gain 1 Stress and become Pinned |

Use the same result for ranged and melee. The discussion did not explicitly change ranged Down versus melee Out at zero Wounds.

Latest concise Pinned wording proposed:

> **Pinned:** Cannot Move, Charge, Sprint, or Disengage. Spend Move to clear. May still Shoot, Fight, Interact, or React normally.

- Clearing Pinned does not remove Stress.
- Further qualifying non-wounding hits add Stress; Pinned does not stack.
- Do not count one Stress for the failed Injury and a second for Pinned: they are one attack result.
- Explicit movement exceptions, such as Scramble, still require review under the new shared melee/ranged application.
- Skills that formerly applied Suppressed cannot simply retain the retired word. Pin Them Down is particularly affected because ordinary failed Injury now already Pins.

## 7. Earlier cumulative Stress proposal — now under reconsideration

The old Shaken explanation was: any Stress gives a flat -1 to rolls; extra points increase morale risk rather than worsening every roll.

Ross then directed:

> **Each point of Stress should subtract an additional -1 on all rolls now that the game uses d20s.**

Working wording:

> **Stress:** Subtract your current Stress from every roll you make. Clearing Pinned does not remove Stress.

The assistant proposed replacing the separate Shaken penalty rather than stacking both. This avoids counting the same Stress twice.

| Stress | Penalty before any cap |
| --- | --- |
| 1 | -1 |
| 2 | -2 |
| 3 | -3 |
| 4 | -4 |

### Open implications — not silently settled

- **Cap:** The old +/-3 combined modifier cap prevents unrestricted scaling. Extra Stress could still cancel positive bonuses, but a net penalty would bottom out at -3. Decide whether to change the cap, exempt Stress, or accept that behaviour.
- **Roll scope:** Literal "all rolls" includes Injury, which reduces both accuracy and the chance to wound, and could include Search discovery or other outcome-table rolls if not defined carefully. Specify tests versus resolution/outcome-table rolls, opposed defence, reactions, and campaign rolls.
- **Break formula:** Assistant proposed `d20 + NRV - Stress + other modifiers`, replacing the older `-(Stress-1)` adjustment and applying Stress once. Ross has not separately confirmed this formula, its target number, or its failure bands.
- **Shaken:** Decide whether the name remains descriptive or is retired. Do not retain its old additional -1 on top of cumulative Stress.
- **Recovery:** Thresholds, passive recovery, Stress retention through Down, and Rally interactions have not been redesigned yet.
- **Compounding penalties:** Stress on both hit and Injury can make recovery and aggressive Stress-clearing much stronger. Evaluate before costing skills.

## 7a. Superseded proposal: flat Shaken and ranged-only Pinned (2026-09-20)

> Historical proposal. Ross's clarification in section 7b replaces the flat -2 penalty and the not-Down pinning trigger. Do not use this section as current wording.

### Ross's proposal — not yet adopted

- Every successful ranged or melee hit adds 1 Stress, independently of whether it wounds.
- At 1+ Stress the unit is **Shaken: -2 to all rolls**. This is flat, not an additional penalty per point.
- At 2+ Stress, take an NRV test and roll on the NRV table if failed. Timing/frequency and table contents were not specified.
- **Pinned** is separate, ranged-only, normally granted by a skill but potentially inherent to some weapons.
- Example skill trigger: a successful ranged attack that does not Down its target Pins it. This can include a wounded multi-Wound target that remains standing; confirm whether that is intended.
- The unit or a friendly within 3 inches may spend an Action to Recover from Pinned. This replaces the earlier proposed Move-slot clearing cost if adopted.
- Further hits add Stress normally.
- Ross's example: three Attack Dice, two hits, both fail Injury, attacker has Pin Them Down. Result: Pinned and 2 total Stress (one associated with the pinning hit, one from the additional hit).

### Assistant assessment / proposed clarification

This separates accumulated pressure from movement control and avoids the per-point penalty spiral. Ordinary hits have the same Stress rule in ranged and melee; Pinned is an explicit ranged specialty.

Recommend wording: **each hit adds 1 Stress; applying Pinned adds no additional Stress beyond that hit.** This expresses Ross's example without accidentally giving three Stress for two hits. If a non-hit source can Pin, specify its Stress separately; do not assume an extra universal condition bonus.

Proposed attack-level trigger: after resolving a ranged attack with at least one hit, if the target is not Down or Out, apply Pinned. This avoids unclear per-die ordering and double pinning. Wounds and Stress still follow their normal limits; the existing one-wound-per-attack cap is not changed merely by this proposal.

Recommend one NRV test in the End Phase for units at 2+ Stress, rather than after each hit. This is an assistant suggestion, not a user decision. Apply Shaken once on the test; do not silently retain an additional old Stress subtraction. Decide whether the subsequent NRV outcome-table roll is modified, especially given the phrase "all rolls".

Keep previous Pinned restrictions provisionally (cannot move, may act/react), pending confirmation. An Action to Recover then leaves Move available; this deliberately differs from clearing with Move and retaining an attack. Friendly recovery permits the pinned unit to keep its own slots. Recovery removes Pinned, not Stress, unless Ross chooses otherwise.

### Newly exposed questions

- Exact NRV-test timing, frequency, target number, and outcome table.
- Does more than 2 Stress affect test/table odds, or only the effort needed to recover below the threshold?
- Does "all rolls" include Injury and the NRV outcome table? Keep test and outcome-roll penalties distinct until ruled.
- Does not-Down deliberately include wounded survivors? How are already Down targets handled?
- Must a recovering helper be unengaged, have LOS, and be otherwise able to act?
- Are Pinned units allowed to Shoot/Fight/Interact/React as in the previous proposal?
- How does Stress recovery work, and does Stress persist through Down?
- Reconcile old surplus-hit Stress and negative-condition Stress rules so each hit is counted once.

## 7b. Current clarification: cumulative Stress capped at 5 (2026-09-20)

### Ross's explicit direction

1. Each successful hit from a ranged or melee attack adds **1 Stress**, whether or not it wounds.
2. Each Stress point gives **-1 to the unit's rolls**.
3. Stress is capped at **5**, producing a maximum Stress penalty of **-5**.
4. Some skills or weapons may apply **Pinned when a ranged hit does not wound**. Ordinary hits do not inherently Pin, and melee does not cause Pinned through this trigger.
5. A Pinned unit spends **an action point to Recover**. A friendly may also spend an action point to Recover it.
6. Pinning adds no extra Stress and does not replace the hit's Stress. Two non-wounding hits with a qualifying skill cause **Pinned and 2 Stress**, not 3 Stress.

Concise working wording:

> **Stress:** Each successful ranged or melee hit adds 1 Stress, up to 5. Each Stress gives -1 to the unit's rolls.
>
> **Pinned:** A skill or weapon may Pin a target on a ranged hit that fails to wound. The target or a friendly may spend an action point to Recover it. Pinning adds no additional Stress.

### Context retained / points not settled by this clarification

- The previous proposal allowed friendly recovery within **3 inches**. Ross did not revoke or restate that distance; retain it provisionally rather than claiming a newly confirmed range. LOS and helper eligibility remain unspecified.
- Previous Pinned wording prevented movement while allowing actions/reactions. No new restriction was stated here; confirm exact condition text before integration.
- Recovery clears Pinned; no Stress removal was newly granted. Stress recovery remains to be designed/confirmed.
- **Not wounded** replaces **not Down** as the pinning trigger. Do not Pin merely because a wounded multi-Wound target survives.
- Mixed multi-die results need a ruling: one hit wounds while another fails Injury. Do not silently choose whether that surviving target also becomes Pinned.
- A -5 Stress penalty must be possible under this direction; the old +/-3 general cap cannot truncate it to -3. How Stress interacts with other modifiers still needs wording.
- The earlier 2+ Stress NRV-test/table proposal was not restated or explicitly revoked. Keep it pending confirmation, including timing, target, table, and whether Stress modifies the outcome-table roll.
- No additional flat Shaken penalty should be stacked onto cumulative Stress. Whether Shaken remains a descriptive label is open.
- The term **action point** is Ross's wording. Do not infer a complete replacement of Move/Action slots with a new AP economy from this alone.
- Existing surplus-hit and condition Stress must not be added again on top of one Stress per hit. The one-wound-per-attack limit was not changed here.

## 8. Open decisions and next review

> Section 7b is the current working direction. Earlier flat-penalty, not-Down pinning, and automatic-Pinned proposals are history. Unresolved items below must be assessed against the 5-Stress cap and cumulative -1 penalty.

- [ ] Confirm current d20 target number(s), which rolls use d20, and natural-result rules.
- [ ] Confirm opposed-test procedure under d20; do not infer it from the old ambiguous wording.
- [ ] Resolve modifier cap with +2 skill bonuses and cumulative Stress.
- [ ] Define exactly which rolls Stress modifies.
- [ ] Confirm Break-test formula, trigger thresholds, outcomes, and recovery.
- [ ] Confirm final Pinned text and treatment of repeated applications.
- [ ] Reconcile multi-die attacks: wound limit, surplus-hit Stress, and whether an attack that wounds can also Pin from another die. Do not assume the single-hit table settles this.
- [ ] Reconcile control payloads, Stress, and the one-hit/one-result principle.
- [ ] Apply +2 conversion to a new catalogue revision, retaining this snapshot for comparison.
- [ ] Decide whether cover reduction / Armour-ignore benefits also increase.
- [ ] Replace Suppressed in skill designs, especially Pin Them Down.
- [ ] Rewrite Red Mist and any old Shaken-dependent effects.
- [ ] Review Grapple/Throw environmental control and one-handed/two-handed interactions.
- [ ] Review Ready cancellation, reaction timing, and retained-Ready skills.
- [ ] Confirm skill acquisition, stat access, and count limits. Assistant suggested retaining +2/+4/+6 selection milestones with one flat list; Ross has not adopted that.
- [ ] Test each signature skill's independent value and viable builds without it.
- [ ] Test action-saving effects, attack chains, movement after attacking, control loops, and overlapping NRV auras.
- [ ] Compare across objective, mobile, retrieval, sabotage, and infrastructure scenarios rather than only static firefights.
- [ ] Obtain explicit approval before integrating into the master and dependent records.

## 9. Discussion journal

### Thread discussion compiled 2026-09-20

1. Ross proposed reducing skills and supplied twelve STR/twelve DEX concepts, with empty lists for the other stats. Initial categories strongly separated offence, protection, capability, consumables, and permanent development.
2. Assistant reviewed the initial picks, identifying direct numerical buffs, Grapple dependencies, automatic takedowns, and extra-attack risks. Early replacements were too restrictive and utility-focused.
3. Ross confirmed **12 per stat** and explained that strong, discoverable combinations should make skills central to a unit's identity. Lifted the strict no-damage/no-survival boundary.
4. Assistant drafted 60 skills. Grapple was questioned repeatedly; its purpose evolved from movement lock to **grab and drag**.
5. Ross proposed signature themes for each stat and raised the risk of mandatory archetypes. Assistant suggested benefits rather than prerequisites, with alternative builds receiving equal support.
6. Assistant produced the revised 60-skill catalogue preserved above.
7. Ross requested much shorter wording, a five-column table, then a Sheets-friendly effect column and a matching Type column. Plain one-line-per-cell code blocks worked better than Markdown tables for copying.
8. Modifier discussion initially used stale d10 assumptions. Ross corrected to d20 and directed **+1 skill bonuses to become +2**.
9. Ross questioned Pinned versus Suppressed. Stronger Suppressed was explored, then superseded by removing it and making ranged/melee non-wounding hits both cause **Pinned and 1 Stress**.
10. Ross directed **cumulative -1 per Stress on all rolls**. Cap, roll scope, Break formula, and recovery remain open.
11. Ross requested this separate running Obsidian document before any master-system changes.
12. Ross clarified that the document should be viewable beside the conversation. The existing Markdown file was queued to open in the Codex right-hand panel; no ChatGPT Canvas was created.
13. Ross proposed replacing cumulative penalties with Shaken (-2 at any Stress), an NRV test/table at 2+ Stress, one Stress per successful hit in either combat mode, and ranged-only Pinned from skills/weapons with Action-based self/ally recovery. Historical proposal in section 7a, subsequently clarified.
14. Ross clarified: each ranged/melee hit gives 1 Stress; each Stress gives -1 to rolls, capped at 5 Stress/-5. Qualifying skills/weapons Pin on ranged hits that fail to wound. Self or friendly spends an action point to Recover. Two failed-Injury hits cause Pinned and 2 Stress. Section 7b is current; master remains untouched.

### Original supplied candidates — historical reference

- **STR:** Grapple, Throw, Knockback, Meat Shield, The Bull, Tough, Roar, Crush, Rampage, Just a Scratch, Come Get Some, Bullet Proof.
- **DEX:** Marked, Dead Shot, Quick Shot, Gunslinger, Run N' Gun, Sniper, Calm Under Fire, Pray and Spray, an unnamed +1 ranged Injury skill, I See You, Crossfire, Eagle Eye.
- Original high-impact concepts included extra Wounds, automatic takedowns of Grappled targets, redirecting attacks into held enemies, compulsory attacks, and extra shots. None should be treated as adopted merely because later discussion permitted combat skills.

## 10. Hacking review — 2026-09-21

**Request:** Ross asked for a reading of hacking in the master and design feedback. This section records analysis, not an adopted hacking redesign.

**Reading coverage:** master sections 12, 12.5, 12.6, hacking skill entries, hacking gear and loadout entries; the complete dedicated `Rules System/Hacking.md` note. Master references to activation, terrain interaction, and device states were also inspected. No simulation was run or independently verified.

### Written system

- Master: declare terminal and Linked feature, roll INT minus range against the written threshold, maximum 24 inches. Another terminal can Interrupt and Overload itself until next turn. No separate hacker-duel subsystem in v1.
- Dedicated Hacking note supplies details absent from the short master summary: base-contact terminal access, Action cost, one function per hack, scenario-defined Linked connections, range measured terminal to feature, and one access per unit per terminal per turn.
- Range bands: 0 through 6 inches, -1 through 12, -2 through 18, -3 through 24. Range alone never creates a Link.
- Interrupt is declared before access is rolled, needs an enemy at another live terminal on the network, ignores LOS/facing, and needs no Ready. In the dedicated note it has **no separate test**: a successful access is automatically cancelled and the interrupt terminal Overloads. Failed access does not spend the interrupt/Overload the terminal.
- Master summary says "Pass" without identifying the roll; the dedicated note clarifies the intended automatic interrupt procedure. Do not present the detail as if the master specifies it fully.
- Manual infrastructure operation requires contact and a DEX test (STR for heavy mechanisms) and cannot be Interrupted. Ready can allow operation as a reaction.
- Effects include doors, bridges, lights, shutters, vents, power, cameras, traps and turret functions. Damaging hacks count as the unit's attack; no extra personal attack.
- Turrets are deployables; hacking can deactivate/hijack/fire them under the dedicated description. Infrastructure otherwise focuses on board changes, with printed FALL/CRUSH hazards where appropriate.

### Assessment — assistant recommendations, not decisions

The strongest identity is environmental and device control. This enables meaningful combinations with concealment, movement, displacement, and fire lanes without creating a separate damage minigame. Manual operation as an uninterruptible alternative gives a useful positioning tradeoff.

The main concern is automatic Interrupt: one equipped defender at a live terminal can cancel a lone hacker's successful attempt regardless of the hacker's INT. More access bonuses cannot overcome a guaranteed veto. Multiple hackers can exhaust interrupt terminals, so the system rewards available bodies and access attempts more than specialist quality in this situation. Exact impact still depends on network layout and timing.

Hacker value also depends heavily on scenario terrain. Every relevant board needs useful, accessible Linked features, not just decorative terminals or ubiquitous uncontested toggles. Printed connections and functions are preferable to on-the-fly arguments about what can be hacked.

Suggested direction for discussion: retain one Action/one INT test/one printed device function; make network connections legible; define temporary override versus lasting control; reconsider automatic Interrupt through a paid/limited counterplay mechanic (for example a reaction-based opposed INT test), without introducing Program/Firewall tracks. Opposed defence would be an optional extra resolution only when contested; it is not yet adopted.

### Inconsistencies and questions to resolve

- Master hacking still uses d10/7+. Hacking note's introduction says d20/7+, but its step-by-step rules still say d10 and natural 10. This does not establish that the d20 target and natural-roll rules are settled.
- Dedicated note says terminals may be reusable access points or a one-shot Interrupt, "never both," but does not clearly explain whether accessing then Interrupting is forbidden mechanically. Define timing and when Overload ends (round versus unit activation/turn).
- Master lists Interruption among reaction options; dedicated note removes Ready cost. Clarify whether it still consumes the normal reaction allowance and how multiple interrupters resolve.
- Printed turrets may fire automatically once per round; does a hacked shot consume that existing allowance? Clarify rather than create extra attacks accidentally.
- Define who can hack without a skill. Core access and bare-handed gear imply broad availability; old skill text says Hacker grants basic terminal access.
- Hacking gear prices disagree inside the master (20/40 in hacking gear; 40/80 in loadout). Resolve later during integration; no price edits made.
- Old Counter-Hack skill removing Overload needs review: it removes the main cost from an automatic veto even if a reaction limit remains.
- Do not assume electronic hacks cause Stress merely because weapon hits do. Decide which effects count as attacks/hits; operating a door need not become a psychological attack.
- Full scope: only terminals/infrastructure/deployables, or also carried electronics? No new category of hackable targets authorised.

## 11. Scenario terrain and token-based interactions — 2026-09-21

### Ross's design direction

- Board setup is not yet fully designed. A possible setup mechanic has players roll on a table and place tokens identifying interactive terrain.
- Physical scenery should ideally communicate the function, but players cannot be expected to own functioning lifts, shutters, or other specialised models.
- Scenarios can suggest terrain or specify key pieces, with players filling out the remainder of the battlefield.
- Tokens/templates can represent most interactive features, including larger machinery such as cranes without needing a crane model.

### Crane example supplied by Ross — exploratory wording

> Spend an Action while in base contact with the crane token. Move obstacles or scatter terrain within 12 inches of the token. Terrain placed on a unit causes an automatic Injury roll at +5 Damage unless the target succeeds on an AGI test.

This is an example of the desired physical interaction, not a validated damage value or completed placement rule. The example includes both rearranging terrain and damaging units with terrain; do not reject the latter solely because an older infrastructure rule discouraged direct harm.

### Assistant suggestions — not adopted

- Let scenarios guarantee the functional terrain their objectives require; random features add variety around that structure.
- Guarantee a useful number/distribution of interactions rather than randomising whether hackers have anything relevant to do.
- A feature token/card can define local access, operation, range/area, targets, state, and any avoidance roll. Scenery remains the physical obstacle where present.
- Previously suggested local control points and remote hacking without mandatory separate terminals remain proposals, not an adopted replacement of the network rules.
- For a first crane test, consider one eligible movable piece per Action, with both original and final positions wholly inside the crane's operating radius. Agree eligible pieces at setup; exclude fixed buildings and scenario objectives unless explicitly allowed.
- Separate movement of cover from the optional damaging placement. Keep Ross's +5 as a trial value, not a balanced recommendation.
- Define what happens to the target and obstacle after a successful/failed AGI test. Physical bases and scenery must finish in legal, non-overlapping positions; avoid inventing unresolved buried-unit states.
- Clarify maximum piece size, whether intervening terrain obstructs the lift, protection/Armour, occupied pieces, multiple targets, use limits, and whether dropping terrain counts as the operator's attack. These are design questions, not additional approved mechanics.
- Remote hacking should operate the same feature effect if permitted; avoid creating separate manual and electronic crane minigames.

## 12. Interactive feature candidates — 2026-09-21

### Ross's Bottomless Pit example

- Place a 3-inch circular pit template and a control token anywhere within 6 inches.
- A unit in base contact with the token spends an Action to open/close the pit doors.
- Units standing on the pit when opened must pass AGI or fall to their doom.
- Units pushed or thrown so any part of their base touches the open template must likewise pass AGI or fall to their doom.
- On success, place the unit anywhere around the template.
- This is a proposed environmental hazard, not a master-rule amendment. The campaign meaning of "doom" (Out for battle versus campaign death/Fate) is not specified.

### Assistant candidate examples — all provisional

Default suggestion for this candidate set: a control token within 6 inches of its associated template; base-contact Action to operate, unless the feature card states otherwise. Do not treat this as an adopted universal rule or allow it to silently override the crane's own layout.

| Feature | Representation | Candidate operation |
| --- | --- | --- |
| Retractable Bridge | Narrow bridge strip across a printed gap/pit | Extend/retract; retraction uses the pit's AGI/escape procedure for occupants. Supports access and isolation rather than requiring moving scenery. |
| Conveyor Belt | 2 x 8-inch strip with direction arrow | Each operation moves occupants/eligible movable scatter up to 3 inches along the belt, using one common chosen direction. Stops at obstructions; units crossing into hazards resolve their hazard. Deliberately one movement per Action, not an undefined ongoing round effect. |
| Hydraulic Barricade | 1 x 4-inch strip | Raise/lower a wall: raised blocks ground passage and LOS, lowered is passable. Raising places overlapping units at nearest legal edge without damage. |
| Ventilation Outlet | Outlet token plus 3-inch smoke circle | Toggle smoke at the outlet. Smoke blocks LOS through it; clear removes this feature's smoke. No unspecified general smoke subsystem required for the sketch. |
| Floodlights | Lamp/control marker and 6-inch-diameter light circle | Position light centre within 12 inches of lamp and toggle on/off. Units touching lit zone lose/cannot gain Hidden. Light does not allow seeing through solid terrain. |
| Cargo Lift | Matching 3-inch platform templates on two elevations | Move the platform and its occupants between marked stops. Occupants retain own activation resources; clear landing area required. |
| Floodgate | 2 x 8-inch channel strip | Flood/drain; flooded ground costs double movement, drained is normal. Does not add drowning unless separately designed. |
| Security Shutters | Markers for up to three openings on one building | Open/close the marked shutters together, allowing/blocking LOS through them. Avoids affecting unrelated windows. |

These illustrate different tactical jobs, not tested ranges, dimensions, or damage values. Review repeat operation, overlapping templates, reactions, eligible terrain, and normal objective access before finalising.

### Pit review notes — assistant suggestions, not edits to Ross's example

- Successful escape could use the nearest legal edge rather than any edge, avoiding free repositioning around the pit; Ross's original permits anywhere around it.
- Prefer define "doom" as Out of Action for the battle with ordinary campaign Fate, unless permanent death is explicitly intended.
- Instant removal plus displacement may dominate surrounding objectives; bound setup placement and test it. No prohibition on environmental kills is being reintroduced.
- Resolve opening occupancy and later forced-entry triggers once per relevant event, not repeatedly for mere continued template contact; exact trigger wording still pending.

## 13. AGI traversal and stealth review — 2026-09-21

### Traversal discussion

Ross observed that interactive terrain makes AGI and INT more important. Assistant noted that AGI should actively exploit routes as well as avoid hazards; INT controls features and STR can displace enemies into them.

Ross proposed an AGI skill allowing climbing without gear or access points. Assistant drafted **Free Climber**: may climb structures without gear/access point; make AGI test, counting vertical distance against movement; normal failure consequences and no passage through solid surfaces. This is a candidate, not an approved thirteenth AGI skill or a confirmed replacement for one of the twelve. Assistant suggested retaining a test because access itself is valuable.

### Readback of written stealth/ambush

Read master sections 10 and 25, relevant action/skill references, Conditions' stealth subsection and Spotted definition. These remain separate from our workshop skills.

- Hide is listed as an Action. Hidden is gained in Concealing terrain, or via permitted gear/skills.
- Hidden imposes -3 to be hit, not untargetability. LOS and other attack legality still apply.
- Moving, shooting, interacting, or being revealed removes Hidden, except explicit exceptions. Quiet weapon and movement skills may create such exceptions.
- Holding an objective without acting may retain Hidden; claiming/looting/arming/defusing Interacts break it. The broader phrase "claiming/scoring breaks Hidden" is not fully consistent with the surrounding explanation of passive holding; clarify later.
- Spotted identifies a target for named skills until the relevant expiry; does not itself remove Hidden. Workshop Marked's cover reduction is a different draft mechanic.
- Master Ambush uses AGI rather than STR/DEX and grants the target a free Attack Back when Ambush fails.
- Conditions explicitly flags that Ambush has no defined action/skill/gear card specifying trigger and cost. Its complete procedure cannot be reconstructed reliably from those two master statements alone. Do not invent range, timing, or melee/ranged eligibility.
- Hide-test references exist, but a complete core Hide/Spot procedure was not found in the reviewed sections. Avoid assuming an AGI Hide test or a universal Spot range/cost.
- Master quotes old simulation findings for Ambush and concealment; Conditions says the referenced packet file is unavailable in the repo. This review does not independently verify those findings or establish their validity for d20 and revised Stress.

Our workshop **Ambush** (+1 first hit/melee from Hidden within 6 inches, subsequently subject to Ross's +2 bonus direction) is a proposed different design, not the master's existing AGI-substitution mechanic. Low Profile and Vanish likewise remain workshop candidates.

### Proposed AGI-exclusive Ambush access

Ross asked whether Ambush attacks should be reserved for an AGI skill and indicated that this felt appropriate. Assistant supports this as a proposed access rule, not a complete adopted attack procedure:

- Ordinary Hide and ordinary attacks remain available without Ambush.
- Selecting the AGI **Ambush** skill unlocks the special Ambush attack; high AGI alone does not grant it automatically.
- Other AGI skills must remain useful independently. Concealment/movement skills can support Ambush without requiring it or becoming mandatory prerequisites.
- An attack made from Hidden without the skill is an ordinary attack and gains no Ambush-specific benefits.
- Using AGI to resolve the special attack is the recommended starting point and aligns with the written master's concept. This does not settle trigger, cost, range, eligibility, extra payoff, or failed-attempt retaliation.
- The earlier workshop Ambush accuracy-bonus wording should not be silently combined with AGI substitution; decide the final package explicitly.

### Latest Ambush draft from Ross

Ross proposed a Hidden unit starting a successful Charge or Aerial Assault outside the target's LOS (described parenthetically as outside its forward 180-degree arc) may choose Ambush. Pass AGI for +4 hit and +4 Injury in melee; with two one-handed melee weapons, choose one to benefit. On failed AGI, target may spend its Action or Ready token to attack first, then the ambusher attacks normally without bonuses.

Assistant's concise working version, for review:

> **Ambush:** If you begin a Charge or Aerial Assault Hidden and outside the target's forward 180-degree arc, test AGI when you reach it. **Pass:** one melee weapon gains +4 to hit and Injury for this attack. **Fail:** the target may spend its unused Action or Ready token to attack you first; if still able, you then attack normally.

Interpretations to confirm rather than silently adopt:

- The concise version uses Ross's forward-arc parenthesis as the eligibility test. Blocked true LOS from within the forward arc is a different condition and is not automatically included.
- Hidden is checked at the start, before movement would normally reveal the attacker. Roll after a successful approach reaches the target; a failed Charge/Aerial Assault does not grant an Ambush attack.
- One weapon benefits for that attack; another one-handed weapon is resolved normally if the base dual-wield rules permit its attack. The skill itself does not grant another attack.
- This proposal gives an AGI setup test then normal melee resolution with bonuses. It supersedes the previous suggested AGI-for-STR attack substitution as the active draft; do not silently apply both.
- "Unused Action" clarifies expenditure and avoids creating extra Actions. Whether a target that already activated can retaliate without Ready remains a user decision; the concise proposal says no.
- Retaliation is optional, costs one stated resource, happens before the ambusher's attack on failure, and can prevent that attack if the ambusher is no longer able to fight. Define interaction with ordinary opposed melee counter-damage before integration to avoid duplicate retaliation.
- +4 bonuses require revisiting the old +/-3 cap; do not silently truncate or exempt them. On d20 a +4 changes an uncapped threshold roll by 20 percentage points, but opposed melee is not the same calculation. No balance claim has been verified.
- Aerial Assault and dual-wield baseline rules have not been read or finalised in this review.

### Positive modifier cap confirmed — 2026-09-21

Ross explicitly confirmed changing the old +3 modifier cap to **+6**, matching the d10-to-d20 scale change. This is the current workshop direction; master remains untouched.

- Interpret as the cap on the combined modifier for a roll, not a cap on each individual skill. Base stat values and weapon profiles are not automatically doubled or recapped by this change.
- Ambush's +4 hit and +4 Injury now fit under the positive cap, each on its own separate roll. Each roll has room for a further net +2 modifier before reaching +6.
- +3 on d10 and +6 on d20 both represent a 30-percentage-point change in an uncapped flat-threshold test, away from natural-result limits. This is a scale comparison, not proof of balance for opposed tests or full attack sequences.
- Ross specified **+6**, not explicitly **+/-6**. Keep the negative cap and exact netting procedure pending confirmation; do not silently change them. The confirmed Stress direction still requires penalties up to -5 to function.
- Earlier cap-related concerns above are historical where they concern the positive +3 limit. Remaining negative-cap/Stress questions still apply.

### Simplified Ambush proposal — latest wording, 2026-09-21

Ross removed the rear-arc/LOS gate: a successful Charge begun Hidden may trigger Ambush. Test AGI for +4 hit/+4 Injury. On failure the target may spend an Action to Attack Back; close combat resolves normally except the ambusher fights last without the bonuses.

Concise assistant wording for review:

> **Ambush:** After completing a Charge begun Hidden, test AGI. **Pass:** one melee weapon gains +4 to hit and +4 to injure for this combat. **Fail:** gain no bonuses; the target may spend an unused Action to Attack Back, resolving its attack before yours. Resolve the combat normally otherwise.

- Retains the AGI-skill access direction; ordinary Hidden units do not automatically gain Ambush.
- Hidden is checked at Charge start, so normal movement removing Hidden does not make the skill impossible.
- Rear arc and starting out of LOS are no longer required.
- Read retaliation as changing the order of this combat, not adding a separate preliminary combat followed by another complete exchange. This is the assistant's interpretation of "fights last" and needs compatible core melee wording.
- If the defender declines or cannot pay, no bonus still applies; there is no free retaliatory attack created by the failed test.
- "Unused Action" is proposed precision; confirm availability under the eventual action-point economy.
- Ready expenditure was not included in Ross's latest wording; do not automatically retain the previous Action-or-Ready alternative.
- Aerial Assault was not restated; whether it qualifies through Charge rules or needs explicit inclusion remains open.
- One-weapon limit is retained from Ross's earlier explicit dual-wield restriction, not a grant of additional attacks.
- Current written master melee uses one opposed exchange where the loser suffers Injury. Attacking first/last is not fully defined there. Resolve this as part of the working melee redesign rather than claiming the new sequence already works in that master.
- Positive +6 modifier cap accommodates +4 bonuses. No numerical balance test performed.

### Ambush success grants Fights First — latest proposal, 2026-09-21

Ross noted that normal melee is head-to-head and proposed: a successful Ambush grants **Fights First with one chosen weapon**; resolve the second weapon normally.

- Retain latest eligibility: skill-holder completes a Charge begun Hidden, then tests AGI.
- On success, chosen weapon gains Fights First. Existing +4 hit/+4 Injury bonuses remain provisionally because Ross did not remove them; this is not a decision that the whole package is balanced.
- If another weapon may attack under dual-wield rules, resolve it normally without Ambush bonuses or Fights First. Do not grant a new extra attack or use the chosen weapon a second time merely because it struck first.
- Previous failed-test proposal remains: no bonuses; defender may spend an unused Action to Attack Back first. Formal Fights First/Attack Back sequencing is still pending.
- In a single opposed exchange, merely rolling one participant's die first provides no advantage. Fights First needs an actual sequencing exception. Assistant suggests the chosen weapon resolves its hit and Injury before the remaining exchange, allowing removal/incapacitation to prevent a response.
- Whether that first strike is an unopposed ordinary hit test, and how the defender's normal melee contribution/second-weapon exchange works, remains explicitly unresolved. Do not silently present either as existing master procedure.
- Resolve the first-strike procedure before judging +4/+4: bypassing an opposed contest and potentially preventing retaliation is an additional benefit beyond those modifiers.

### Unanswered instead of attack-order keywords — active discussion

Ross initially requested official Fights First/Last keywords, then identified that normal head-to-head melee makes attack ordering problematic. Assistant proposed **Unanswered** instead. This is still a proposal; Fights First/Last were not adopted.

Proposed Unanswered resolution: normal opposed melee test; on attacker win, resolve the attack normally; on defender win (including ties), the exchange ends with no Injury or other hit effects on either participant. It protects against the defender's normal winning-exchange damage without guaranteeing a hit.

Ross asked whether the target then attacks again normally or whether Unanswered should be a separate situation. Assistant recommends:

- An Unanswered attack is a **complete, standalone exchange**, not a preliminary roll requiring another exchange to finish it.
- It grants no automatic return attack. The defender retains any later attacks its own activation, resources, or another explicit rule allow; defending has not spent its Action.
- Applying Unanswered to an existing attack changes that attack's resolution; it does not also grant another normal attack with the same weapon.
- Any permitted second-weapon attack is a separate normal exchange unless its own rule says otherwise.
- Latest Ambush proposal: successful AGI modifies one selected weapon's attack with Unanswered and +4 hit/+4 Injury; another permitted weapon resolves normally. These benefits remain untested.
- Failed Ambush's optional paid defender attack is an **explicit extra exchange**: defender spends its Action for an Unanswered attack, then the original ambusher attacks normally if still able. The keyword itself does not create that extra attack.
- Using Unanswered for failed-Ambush retaliation and retaining +4/+4 are assistant draft suggestions, not final user-approved text.

### Revised Hidden / Marked proposal — latest discussion

Ross proposes:

- Hidden gives **-4 to be hit**.
- A Hidden unit is **untargetable from beyond 12 inches**. At 12 inches or less, normal targeting requirements apply and attacks suffer the Hidden penalty.
- DEX skills may **Mark Hidden targets from greater distances**.
- **Marked removes Hidden**, removing both its penalty and distance-based targeting protection.
- A Hidden unit may move and retain Hidden if **both its starting and finishing positions are outside LOS of any enemy within 12 inches of those respective positions**.

Assistant concise wording:

> **Hidden:** Attacks against this unit suffer -4 to hit. Enemies beyond 12 inches cannot target it. It may move without losing Hidden if no enemy within 12 inches has LOS to its starting or finishing position. Becoming Marked removes Hidden.

### Interpretations / pending details

- Endpoint requirement is checked against all enemies, not one selected observer. Enemies beyond 12 inches do not prevent retained Hidden under this movement rule.
- Ross specifies start/end, not the whole route. Visible intermediate ground does not itself remove Hidden under that wording. Reaction checks during the movement still need a timing decision; do not silently require the entire path to be concealed.
- Long-range Mark skills need an explicit exception allowing selection of Hidden targets beyond 12 inches, otherwise untargetability would prevent using them. Recommend retaining true LOS for Marking unless a particular sensor effect explicitly changes it.
- Define whether an active Mark also prevents re-entering Hidden, its duration, and whether Hidden can be regained after it expires. Removing Hidden does not by itself settle these questions.
- Previous Hide acquisition (Action in Concealing terrain) and shooting/Interact reveal rules were not expressly changed here. Clarify them rather than treating the new movement permission as permission to shoot without revealing.
- Workshop Mark Target's previous cover-reduction effect should be reconciled with now removing Hidden; do not silently stack both or assume which effects remain against non-Hidden targets. Original master Spotted remains distinct until names/mechanics are deliberately consolidated.
- Review Low Profile, Vanish, Ambush, floodlights, and other concealment/reveal effects under this replacement. Low Profile's old movement permission may be redundant and needs redesign.
- Negative modifier-cap interaction remains unresolved: intended Hidden penalty is -4 and Stress can reach -5. Confirm combined treatment rather than applying the retired -3 limit.
- Direct untargetability does not settle incidental blast/hazard exposure, no-LOS weapons, or how attackers measure sight/forward arc. These remain edge cases, not adopted immunities.
- No master, records, or skill catalogue changes made by this proposal.

### Hidden exposure timing clarification — latest direction

Ross clarified that a nearby enemy gaining LOS during the enemy's activation does **not** automatically remove Hidden. That enemy may shoot the target within 12 inches, taking the Hidden -4 modifier.

Automatic exposure is checked at the **start and end of the Hidden unit's own activation**, not whenever another unit sees it, and not at the end of every movement segment. If an enemy within 12 inches has LOS at either activation checkpoint, remove Hidden. An enemy's proximity alone is insufficient without LOS.

- This supersedes the previous movement-start/end wording and the assistant suggestion to reveal before a movement-triggered reaction just because movement ended exposed.
- A revealed unit does not automatically regain Hidden by moving out of sight; it needs an eligible Hide action/effect.
- If the unit is exposed at activation start, remove Hidden before checking a Charge-begun-Hidden Ambush trigger. This follows the proposed timing; no exception has been granted.
- Hidden still prevents targeting beyond 12 inches; at 12 inches or less, a legal ranged attack can target it at -4 while it remains Hidden.
- Marked remains an explicit reveal effect. Existing shooting/Interact reveal rules have not expressly been removed by this clarification.
- Decide how the activation-end exposure check is ordered against a reaction to the final Move/Action. Do not silently import the discarded immediate movement-end reveal rule.
- The assistant's proposed Mark duration and ban on re-Hiding while Marked remain unconfirmed.

### Successful hits reveal Hidden units — latest clarification

Ross clarified: an enemy can legally target a Hidden unit within the permitted range at -4; if it hits, Hidden is removed because the target gains Stress/is Shaken or goes Down. If every attack die misses, Hidden remains.

- Record this directly as **a successful hit removes Hidden**, regardless of whether Injury succeeds. This covers wounded survivors as well as non-wounding hits, without requiring a separate Down check.
- Existing range restriction remains: enemies beyond 12 inches cannot normally target Hidden units. The statement about targeting does not revoke it.
- Every hit still adds 1 Stress, capped at 5; no second Stress point is created by losing Hidden. A hit at the Stress cap still reveals.
- "Shaken" here describes being affected by Stress; it does not reinstate the superseded flat -2 penalty. Current Stress remains -1 per point, maximum -5.
- A complete miss does not reveal by itself. Other reveal triggers, including Marked and the unit's activation checkpoints, still apply independently.
- For simultaneous Attack Dice, assistant recommends applying Hidden's -4 to every die in that attack, then removing Hidden if any hit. Subsequent attacks would use the target's revealed state. This timing is a proposal pending confirmation, not a new per-die recalculation rule.
- Does not imply that a unit already carrying Stress is permanently barred from Hiding; whether Stress restricts taking Hide remains unspecified.

## 14. Review of Ross's 75-skill first pass — 2026-09-22

Ross supplied [SETTLEMENTSCATALOGUES / Skills](https://docs.google.com/spreadsheets/d/1l7hMrpLqTqCJfIHnmESnVUWRgYR9NCoj5tbjcnTiU6I/edit#gid=964457579) and requested an archetype/combo review before further refinement. Desired STR identities: Tank, Charger, Grappler, DPS, plus flex choices such as Wounds and weapon handling. Wants similarly deliberate groups in the other stats, removing weak fits and adding supporting choices.

- Read all 75 skill rows (2–76), 15 per stat, plus bounded supporting Conditions, Weapon Characteristics, Weapon Drawbacks, and Reactions ranges.
- Source Sheet left unchanged. Preserved values in [[Skills Table Snapshot - 2026-09-22]].
- Proposed primary grouping for every current skill, combo examples, conflicts, merges and missing support in [[75 Skills - Archetype and Combo Review]].
- STR is the clearest grouping; DEX overwatch is coherent; INT is overconcentrated in hacking while Medic has one skill; AGI has strong mobility/stealth identity but overlapping extra attacks; NRV has promising leadership, terror, and Stress-management builds.
- Important undefined/conflicting mechanics: attack/reaction budgets, down versus Out triggers, Unwieldy/Fights Last under opposed melee, Grapple holder versus target restrictions, cumulative Stress versus Shaken text, Marked removing Hidden versus old Notes, aura limits, and model-count objective control.
- Carryover Notes and Type cells frequently contradict updated Effects; flagged as review issues, not automatically applied as intended restrictions.
- Review is qualitative design analysis, not tested balance. All groupings and new-role suggestions remain proposals for Ross's review.

### Review priority correction — archetypes and concepts first

Ross explicitly directed that exact wording, action economy, mechanical finesse, and detailed balance be deferred. Current work is to decide **which archetypes each stat supports and which skill concepts belong to them**. Only after that selection should the group work through wording and mechanics.

- The previous review's mechanical issues are parked, not current blockers or grounds for rejecting otherwise useful concepts.
- Evaluate whether each archetype offers a distinct player intention and whether the selected skills create useful thematic/tactical connections.
- Differentiate concepts before deciding costs, distances, tests, caps, timing, or numeric balance.
- Allow overlapping skill membership and shared flex. Designer groupings are not mandatory player paths.
- Do not edit the source Sheet or treat the assistant's grouping as approved without the user's selection.
- Proposed discussion slate: STR Tank/Charger/Grappler/Bruiser; DEX Marksman/Mobile Shooter/Overwatch/Gunner; INT Controller/Saboteur/Engineer/Medic; AGI Ambusher/Duelist/Acrobat/Skirmisher; NRV Commander/Rallying Leader/Terror Leader/Fanatic. These are proposals, not decisions.
- Next pass should map existing concepts to these roles, identify genuine gaps, and propose concepts for missing support. Do not resume detailed action-economy critique during this phase.

### Shared archetype outline — discussion

Ross asked whether each stat should roughly cover offence, defence, control, and movement, while avoiding forced symmetry (for example forcing direct DPS into INT).

Assistant recommendation: use these as overlapping **tactical contribution tags**, not compulsory archetypes or equal skill allocations. Archetypes remain thematic player identities (Grappler, Medic, Marksman); tags indicate what each contributes. A Grappler can be control/offence, a Medic support/defence, and a Controller control/access.

- Each stat needs multiple distinct, useful approaches, an active way to influence play, and value beyond simply increasing attack output.
- Offensive contribution can be enabling attacks, exposing targets, or manipulating hazards; it need not mean personal damage.
- Defence can be recovery, denial, positioning, or endurance; it need not mean a tank.
- Movement contribution can affect routes or allies rather than increase the unit's movement.
- Strong specialisation and gaps are acceptable. Do not force identical role coverage, counts, or effectiveness across stats.
- Use the outline to identify a whole list that only attacks or only reacts, then add a concept only if it fits the stat's identity and intended archetypes.

This is an assistant proposal for organising the concept pass; no archetype slate or skill rewrite is approved by this discussion alone.

## 15. Ross's revised STR archetypes — concept selection stage

Ross supplied a new, deliberately strong and thematic STR outline: **Grappler, Tank, Charger, Berserker**, three skills each, plus three flex skills. This supersedes the earlier Bruiser grouping as the latest proposed STR roster. Skill concepts are under discussion; no official wording, action-economy reconciliation, or balance approval yet.

### Grappler

1. **Grapple:** Opposed STR against an enemy within 1 inch; success makes it Grappled. Ross wants substantial standalone value, rather than a humorous but inferior alternative to attacking.
   - Held target cannot activate/react normally; at activation start gets an opposed STR escape test. Pass escapes; fail stays held.
   - Grappler moves at half speed.
   - Proposed built-in **Crush**: an Action to make opposed STR with +4 for the grappler. Ross also floated a free end-of-activation Crush; choice and actual successful result remain unresolved.
   - Proposed built-in **Meat Shield** protects holder and allies within 2 inches against incoming shooting. Shooter rolls an unmodified d20 versus 10+ (called Luck); success hits intended target, failure hits captive. Exact targeting/attack-roll order is not settled. No permanent Luck stat was proposed.
2. **Strong Arm:** With a held target, move full distance, Interact, and attack using one-handed melee/ranged weapons. No Charge, Dash, Climb, or two-handed equipment. Ross explicitly intends an interaction with a skill treating two-handed melee weapons as one-handed. **Subsequent addition:** also ignore the Heavy weapon keyword (normally halves movement), allowing normal movement with heavy two-handed guns or melee weapons even without Grapple. Ignoring Heavy does not itself waive the held-target two-handed restriction.
3. **Throw:** In base contact, throw scatter/obstacle terrain no bigger than 3 inches a distance equal to STR. Terrain hitting a unit Pins it. Also throw a Grappled target. A thrown target striking a structure suffers an Injury roll at +3 Damage; thrown units colliding with another unit Pin both. Further movement/fall details not settled here.

### Tank — defensive

4. **Brace:** Spend an Action to Brace. Cannot move, act, or react; incoming attacks suffer -4 hit until end of turn.
5. **Come on then:** Pass STR to require enemies within 6 inches to target this unit with their Attack actions.
6. **Tough as nails:** Once per round, if attacked in melee but not wounded, ignore the hit's effects. Subsequent attacks from any enemy suffer -4 Injury against this unit until end of turn.

### Charger — movement/offence

7. **Rampage:** Down an enemy with a Charge attack, then continue the remaining charge distance in any direction. Reaching within 1 inch of another enemy grants a free melee attack.
8. **Bull:** On declaring Charge, pass STR to move through non-LOS-blocking scatter, obstacles, and barricades. Enemies contacted during charge test AGI; failure pushes them 2 inches in charger-chosen direction and Pins them. Does not cross reinforced doors, buildings, or LOS-blocking structures.
9. **Human Bullet:** Charge distance becomes movement plus the sum of 2d6 instead of 1d6. This proposes/assumes a charge procedure different from the older master; record without silently importing it into live core rules or rejecting the concept during this stage.

### Berserker — offensive

10. **Rage:** When attacking in melee, choose up to +3 Injury Damage and gain 1 Stress for each point added.
11. **I'm about to break:** Once per turn when charged, turn Stress penalties into positive modifiers for that combat. After combat gain 1 Stress and immediately take a Break test regardless of outcome. Ignore beneficial Stress modifiers from friendly units/skills/equipment for this test. Exact coverage of modifiers is for later wording.
12. **Blowing off steam:** Downing an enemy removes 2 Stress. Ross's current wording does not limit this to melee.

### Flex

13. **Goliath:** Dual-wield two-handed melee weapons as if one-handed.
14. **Tough:** +1 Wound.
15. **Big Fella:** Ignore Unwieldy on weapons.

### Concept-level assistant assessment — not additional rules

- This is a coherent four-archetype roster with explicit identity and potential mixed builds. Recommend retaining all fifteen concepts for this stage rather than cutting them based on unfinished numbers.
- Grappler controls one enemy; Tank influences enemy target choices/attention; Charger exploits routes and momentum; Berserker manages aggression and Stress. Those distinctions prevent all four from becoming simply stronger melee attackers.
- Grapple needs **situational superiority** to attacking (capturing position, denying an important unit, protecting a group), not universal superiority. Bundling denial, damage, protection and free damage risks letting one skill perform most jobs without needing a tactical choice.
- Recommend keep Crush as an optional use of the held target rather than automatic free damage for now. This preserves the choice to hold, drag, shield, or hurt without deciding numeric costs yet.
- Preserve the Tank's offensive sacrifice while Braced; it differentiates a protector from the Berserker. Confirm compatible skill timing during the later mechanics pass, not as a concept blocker now.
- Charger sequence has clear complementary jobs: reach, path disruption, and continuation. Strong concept cohesion without needing a prescribed build for players.
- Berserker has a real resource loop: create Stress for offence, exploit it defensively when charged, release it by downing enemies. Recommend STR retain personal physical aggression while NRV retains wider resolve/leadership roles, without banning cross-stat combinations.
- Goliath and Big Fella now have different names/functions from earlier snapshots; use this latest naming in future discussion. Flex skills broaden equipment/endurance without belonging to mandatory packages.
- Leave d6 charge distance, Luck naming, damage caps, action availability, attack chains, Down/Out, and allocation of Stress modifiers for the scheduled mechanics phase. Their presence here is not silent confirmation of a complete core-rules change.

### STR standalone-use check and Strong Arm addition

Ross added ignoring **Heavy** to Strong Arm to make it valuable outside grappling, and asked whether any other STR skills require another archetype skill.

Assistant assessment at concept level:

- All fifteen proposed STR skills have standalone use, assuming their referenced core actions/keywords are available. None presently requires selecting another skill.
- Meat Shield and Crush are built into Grapple, so no separate dead-end follow-up purchase is required.
- Strong Arm supports heavy-weapon users without Grapple. Its grappling permissions remain additional benefits, not prerequisites for ignoring Heavy.
- Throw works on eligible scatter/obstacle terrain without Grapple; throwing a held enemy is its additional use.
- Brace, Come on then, and Tough as nails individually provide protection, target influence, and endurance. Synergy does not mean dependency.
- Rampage, Bull, and Human Bullet all work with normal Charge; no other Charger skill is required.
- Rage generates its own Stress; I'm about to break can use Stress gained from ordinary enemy hits; Blowing off steam removes Stress after ordinary takedowns. No prerequisite Rage purchase is needed.
- Goliath, Tough, and Big Fella rely on loadout or baseline durability rather than another skill. Equipment specificity is different from a skill prerequisite.
- Strong Arm, Goliath, and Big Fella can all support a heavy-weapon character. Keep each identity distinct: carrying/movement, wielding/hand requirements, and Unwieldy handling respectively. Whether all become practically compulsory together is a later build-review question, not a reason to rewrite their concepts now.
- This does not resolve which unit types may access skills, Heavy/Unwieldy pricing, core Charge rules, or detailed action economy.

## 16. Ross's revised DEX archetypes — concept selection stage

Ross supplied twelve skill concepts across four archetypes, leaving three flex slots open. This is the latest DEX proposal, superseding the earlier suggested grouping without editing the source Sheet or live rules. Concept selection remains the priority over action-economy and wording refinement.

### Marksman — long-range offence/support, two-handed ranged

1. **Mark Target:** Spend Move to Mark an enemy within 24 inches and LOS. Friendlies gain +2 shooting it; Hidden targets may be targeted from 24 inches. Lasts until the start of the marking unit's next activation. This wording may change the previous Marked-removes-Hidden direction; clarify later rather than combine both silently.
2. **Head Shot:** +4 Injury against Marked targets if this unit has not moved this turn.
3. **Steady Breathing:** +12-inch range for this unit's two-handed ranged weapons and Mark Target. Existing long-range caps/gates are not automatically reconciled by this concept proposal.

### Gunslinger — short-range offence/movement, dual one-handed ranged

4. **Gunslinger:** Equip two one-handed ranged weapons and attack with both. Ross asks whether to resolve separately or combine Attack Dice into one attack, favouring a combined attack that Bullet Time can split.
5. **Bullet Time:** Spend both actions on a ranged attack; distribute Attack Dice among extra enemies within 6 inches of the original target, resolving per target.
6. **Run + Gun:** After a ranged attack, move up to MOVE for free, even if normal Move was already spent.

### Unnamed short-range two-handed archetype

7. **Pump N Dump:** Once per turn, Down a target within 12 inches with a ranged attack to gain a free ranged attack against another enemy within 12 inches and LOS. After the second attack the same weapon requires Reload before firing again.
8. **Planning Ahead:** Equip two two-handed ranged weapons or one one-handed and one two-handed ranged weapon. Choose one at activation start; cannot switch until next activation starts.
9. **Speed Loader:** Once per turn reload one ranged weapon while resolving a Move.

### Watcher — two-handed heavy ranged, offence/protection

10. **Watch Out!:** When an ally within 12 inches and LOS is charged, spend this unit's Action or reaction to give the ally a free ranged attack before the Charge completes.
11. **Cover Me:** Once per turn, when an ally is targeted by an enemy in this unit's LOS, make a free shooting intervention resolved as opposed DEX against the enemy. Win cancels the enemy's shot; loss automatically Pins and Shakes the original target. Enemy finishes activation normally. Exact damage/Stress sequence remains unspecified; record concept rather than invent it.
12. **Eyes Peeled:** Down an enemy with a ranged attack to gain Ready; keep it or give it to an ally within 12 inches and LOS.

### Flex and assistant concept-level assessment

- Ross has not selected the remaining three skills. Specifically likes DEX heavy-weapon users buying STR **Strong Arm** to ignore Heavy; do not automatically duplicate that permission in DEX.
- Suggested name for short-range two-handed role: **Breacher**, with **Pointman** as an alternative. Its niche is close-range commitment plus weapon/reload preparation rather than sidearm mobility.
- Four distinct intentions: Marksman prepares precise shots; Gunslinger distributes fire and repositions; Breacher chooses the right weapon and exploits a close-range takedown; Watcher protects allied actions and movement.
- Watcher currently reads as support/control through fire, not merely offensive heavy-gun damage. That is a useful distinction. Watch Out! empowers the ally's weapon, while Cover Me uses the watcher's intervention; these are deliberate different functions to preserve or choose between later.
- Recommend combined dual-pistol attack as one Shoot action/attack pool while retaining the origin and profile of each die, e.g. different coloured dice for different weapons. Do not blend Damage, range, traits, or ammo into a new synthetic weapon. Bullet Time can distribute those dice, but every assigned die must still have a legal target for its source weapon.
- Bullet Time plus Run + Gun can offer a committed multi-target attack followed by repositioning. This is the requested playstyle concept, not proof of balance or an approved Action/attack budget.
- Head Shot depends on a Marked target but not necessarily on buying Mark Target personally: allies can provide it. Decide later whether it should also have another trigger; don't reject coordinated unit roles solely for relying on team setup.
- Strong Arm/Planning Ahead provide potential cross-stat heavy-weapon builds; do not assume bonus hands or firing all carried weapons from Planning Ahead.
- Candidate flex concepts, not adopted: **Pin Them Down** (trade/augment fire toward movement control; exact effect later), **Calm Under Fire** (preserve shooting/reaction effectiveness under pressure), **Field of Fire** (broaden the area a Ready unit can watch). They support control, resilience, and awareness rather than duplicating Marksman range or STR weight handling.
- Details parked for later: hidden/marked relationship, handling unmatched weapon profiles, additional-target wound limits, off-turn resource spending, Ready chains, Cover Me's miss/Pin/Stress consequences, ranged reload/ammo interactions, and long-range caps.

### DEX Gunslinger / Breacher overlap — under reconsideration

Ross questioned whether Gunslinger and Breacher serve the same purpose with different weapons. Also questioned Planning Ahead's placement: it is broadly useful, and the apparent Breacher payoff is using a backup while the primary requires Reload after Pump N Dump.

Assistant assessment at concept level:

- The overlap is real in the current concepts: both deliver close-range burst fire and maintain momentum. Weapon type alone does not establish a distinct tactical role.
- Planning Ahead has a genuine connection to Pump N Dump: it provides an alternative weapon during the reload cycle. However, the existing choice-at-activation-start restriction makes this chiefly a next-activation option, not an immediate swap after firing. No restriction is changed by this observation.
- Speed Loader and Planning Ahead mainly offer two solutions to the same reload problem rather than inherently forming a three-part combo. This is not necessarily bad, but weakens the case for a coherent dedicated archetype.
- Recommend move Planning Ahead to flex as a candidate, rather than requiring a unique archetype home for every broadly useful skill. Broad utility alone does not always require flex classification; classify by strongest thematic/tactical purpose.
- Two possible directions, neither adopted: (1) retain Breacher but make its core about entry, close-range displacement, and claiming rooms/objectives, supported by distinctive concepts; or (2) treat one-/two-handed close-range guns as branches of a mobile assault shooter and use the fourth archetype for Suppressor/Fire Support.
- Assistant prefers exploring Suppressor/Fire Support: establish Pinned/Stress, influence multiple enemies, and create openings for allies, differentiated from Watcher's reactive protection.
- Pump N Dump remains a candidate skill even if the Breacher group is removed; do not delete it or rewrite the Sheet automatically.

### DEX identities clarified by Ross — retain Breacher and Watcher

Ross rejected the proposed Fire Support replacement as overlapping Watcher's enemy-control/protection role and clarified the intended four:

- **Marksman:** long-range, high single-target damage, with a substantial crew-wide benefit.
- **Gunslinger:** dual pistols, primarily movement rather than pure offence; move between cover, pick off enemies, avoid return fire.
- **Breacher:** offensive tank; force entry, deliver a close-range blast, then dig in and withstand return fire.
- **Watcher:** support through buffs, debuffs, and reaction shots.

These identities resolve the conceptual overlap. Gunslinger avoids retaliation through movement; Breacher accepts exposure and survives while holding the ground gained. Watcher protects the crew rather than personally occupying the assault role. Retain these four as the user-stated direction; Fire Support remains a discarded assistant alternative.

Assistant concept recommendations, not yet selected skills:

- Marksman and Watcher current groups broadly express their intended roles.
- Gunslinger's Gunslinger and Run + Gun fit. Bullet Time's split-target damage emphasis is less aligned with movement-first identity; consider a third concept around evasive repositioning/using cover. Keep Bullet Time as a candidate, not automatically delete it.
- Breacher's Pump N Dump fits aggressive entry, but its other two current skills solve loadout/reload problems instead of entry and survival. Suggest a breach/assault-access concept and a defensive dig-in/brace-after-advancing concept.
- Planning Ahead is a proposed flex candidate; Speed Loader may also serve flex. No final fifteen-slot allocation made.
- Defensive Breacher skill should complement its offensive occupation role, while STR Tank Brace can retain its more complete sacrifice of activity. No exact action costs, bonuses, durations, or guaranteed denial of return fire specified at this concept stage.

### Breacher revised to explosive assault and immediate follow-up

Ross replaced the earlier weapon-switching/reload package and explored moving away from the defensive-tank concept. Latest Breacher skills:

1. **Spray and Pray:** Once per turn, when making a ranged attack against an initial target within 12 inches, distribute Attack Dice among different enemies within 8 inches of the initial target and LOS. Resolve per target; each Downed enemy adds an Attack Die to allocate to remaining targets.
2. **On me:** Nominate a friendly within 6 inches and LOS. Immediately after the user's activation ends, activate that friendly.
3. **Pump and Dump:** At activation start, add +2 Attack Dice to the next ranged attack. After that attack, the weapon must Reload before firing again.

Ross describes the resulting identity as committing to enough damage to clear the threat, with danger if enemies survive. These are conceptual selections/proposals, not mechanically validated final rules.

Assistant assessment:

- Clear pattern: prepare a heavy opening volley, distribute it through a group, immediately bring a teammate into the opening. The three skills provide ammunition volume, distribution/momentum, and crew follow-up.
- The updated identity is **assault/room-clearing leader**, rather than a shooter protected by a defensive buff. On me adds valuable teamwork and need not make the build pure personal damage.
- On me can let an ally occupy the cleared objective, cover the exhausted shooter, or continue the assault. This is meaningful cross-unit synergy, not an assurance of safety if the volley fails.
- All three have uses outside Breacher: burst on another gunner, spread fire on dual pistols, coordinate a marksman/spotter or escort pair. No prerequisite dependency introduced.
- Gunslinger retains movement/escape; Breacher commits to concentrated offensive momentum; Watcher supplies reactive support. Maintain this distinction while evaluating concepts.
- Current Gunslinger **Bullet Time** also splits Attack Dice. Now that Spray and Pray owns multi-target offensive momentum, consider replacing Bullet Time with a movement/cover concept, or differentiate them substantially. Do not remove it without choosing the replacement.
- **Pump and Dump** is now extra dice within one attack, not the prior conditional second Shoot. Preserve latest identity and name, rather than silently stacking both versions. Planning Ahead/Speed Loader remain potential flex concepts.
- Deferred wording questions: whether On me advances an unactivated ally's ordinary activation or grants a second activation; repeated bonus-die triggers/target order; per-target weapon legality; Heavy/Reload interactions; attack-dice wound and Stress accounting. No action-economy critique is a blocker at concept-selection stage.

### Breacher identity reconsidered — entry, clearing, and securing

Ross questioned whether the latest burst/split-fire/activation trio truly captures a Breacher and invited a better conceptual fit.

Assistant assessment: latest Spray and Pray plus Pump and Dump emphasises multiplying damage across a crowd, which can read as gunner/rampage rather than assaulting a defended position. Missing identity is overcoming the exposed entry into that position. Breacher should win access to occupied space and help the crew take it; strong damage is a means, not the entire identity.

Suggested conceptual alternative (not selected or written as rules):

- **Dynamic Entry:** help cross an opening or approach into defended close quarters and limit the defender's immediate reaction advantage. A timing/entry technique rather than another general damage multiplier or STR terrain-smashing skill. Must work with ordinary gaps/approaches as well as specialised door terrain.
- **Pump and Dump:** retain the committed close-range volley and reload consequence as the clearing tool; no extra numeric revision proposed here.
- **On Me:** retain the coordinated follow-up so a teammate can enter, hold, or cover the newly contested position. Provides the securing/support component without a mandatory personal defensive bonus.

Alternative if Ross prefers a lone offensive tank: replace On Me with a **Hold the Breach** concept that rewards staying in the position just assaulted with protection against retaliation. Pick the desired identity before costs, numbers, or exact triggering geometry. Spray and Pray may be parked/reassigned as a general multi-target skill rather than discarded outright.

### Latest Breacher trio — Breach / Spray and Pray / On Me (2026-09-23)

Ross proposed replacing the archetype's opening skill with **Breach**, retaining his earlier **Spray and Pray** and **On Me**. Pump and Dump is no longer in this proposed three; it is parked, not automatically reassigned to flex. Assistant's Dynamic Entry remains historical, not a fourth skill.

**Breach — user proposal:** Once per turn, declare Breach against an enemy within 12 inches; initial LOS is not required. Move up to maximum Move, then immediately make a Shoot attack. During the movement, passing through doorways requires no Action or test. The unit cannot be targeted by reactions until after its Shoot Action resolves.

**Spray and Pray — retained user version:** Once per turn, when shooting an initial target within 12 inches, distribute Attack Dice among different enemies within 8 inches of the initial target and LOS. Each Downed enemy adds an Attack Die to allocate to remaining targets.

**On Me — retained user version:** Nominate a friendly within 6 inches and LOS; immediately after this unit's activation, activate that friendly.

Concept assessment: this trio provides a distinct entry/clear/follow-up sequence. Breach gets the unit into a firing position before reactions, Spray and Pray spreads pressure through nearby defenders, and On Me brings a teammate into the opening. Gunslinger still avoids exposure through movement after shooting; Breacher commits forward before firing.

Assistant interpretations suggested for later wording, not additional user rulings:

- Lack of LOS applies when declaring the target. The actual shot should still require normal range and LOS after the movement unless explicitly intended as indirect fire.
- Decide which doors the free passage includes. An existing doorway is different from passing through a solid wall or indestructible/sealed scenario feature. No blanket wall passage inferred.
- Breach's reaction immunity ends after the shot; it does not itself grant enemies a new reaction opportunity beyond the normal trigger rules.
- Scope of action cost, meaning of maximum Move, failure to reach a legal shot, and On Me activation eligibility remain for the later mechanics phase.
- Breach remains usable alone as a close-range entry tool; Spray and Pray remains usable with ordinary shooting; On Me remains useful for other coordinated unit roles. Exact bonus-die chains and balance are untested.

### DEX completion and shared dual-wielding decision

Ross considers DEX's concept pass complete. Latest Gunslinger trio supersedes the earlier versions above:

| Skill | Type | Working effect |
| --- | --- | --- |
| Gunslinger | Passive | When dual wielding 1 HANDED RANGED weapons, the off-hand contributes its full attack dice to the combined SHOOT action. |
| Bullet Time | Action modifier | Once per turn, when resolving a SHOOT action, divide its combined attack dice between the initial target and additional enemies within 6 inches of it. Each target requires LOS and range from the weapon contributing that die. No additional action cost. |
| Run + Gun | Passive | Resolve a SHOOT action at any point during a normal MOVE, then complete the remaining movement. Grants neither extra movement nor a free attack. |

**Shared dual wielding:** No skill is required to attack with two eligible one-handed weapons. Choose a dominant weapon before rolling: it contributes normal attack dice, while the off-hand contributes one die without an accuracy penalty. Each die retains its weapon's damage, traits, and applicable range. Combined shooting is one attack and one SHOOT action, not two skill triggers; ordinary targeting is one enemy unless a rule permits splitting. Exact opposed-melee resolution remains to be settled. Gunslinger overrides the ranged off-hand die limit. AGI Ambidextrous supplies a narrower melee exception, below.

Other DEX groups remain Marksman (Mark Target / Head Shot / Steady Breathing), Breacher (Breach / Spray and Pray / On Me), Watcher (Watch Out! / Cover Me / Eyes Peeled). The full-list draft offered Planning Ahead / Speed Loader / Pin Them Down as flex; Ross subsequently called DEX done without individual further changes to those candidates. Preserve that completion context without inventing additional detailed rulings.

## 17. AGILITY — selected fifteen-skill concept draft

Status: Ross supplied four archetypes, accepted the conceptual revisions below, then selected Sprinter as the third flex skill and asked to record the result. Working draft only; exact timing, limits and balance remain for a later pass. These changes do not update the master rules.

### Stalker — offensive movement and stealth

| Skill | Working effect |
| --- | --- |
| Ambush | After a successful CHARGE begun HIDDEN, test AGI. Pass: one melee weapon makes an UNANSWERED attack with +4 to hit and +4 to injure; a defender win causes no damage. The second weapon attacks normally. Fail: no bonuses; the target may spend an unused Action to make an UNANSWERED attack first, followed by this unit's normal attack if still able. |
| Return to the Shadows | Once per turn after resolving CLOSE COMBAT, move up to 6 inches without disengage attacks. End behind or in heavy cover and outside LOS of READY enemies. Become HIDDEN if the destination also meets the normal hiding requirements. |
| Incapacitate | Once per turn, make a 6-inch RANGED ATTACK using AGI and one attack die. A hit causes STUNNED instead of an injury roll. |

**STUNNED — proposed condition:** The unit loses its action points and cannot Ready or react until the start of its next activation. The exact relationship to action-point refresh at that activation remains unresolved; do not silently treat it as losing the entire next activation. Add to the official Conditions section only when integration is authorised. Ordinary hit/Stress interaction also needs wording later.

### Ghost — ranged offence and stealth

| Skill | Working effect |
| --- | --- |
| Ghost | Once per turn, resolve a ranged action without losing HIDDEN from firing. Other normal reveal triggers still apply. |
| Phantom Shot | When shooting while HIDDEN, hits that fail to wound inflict additional Stress. |
| Show Yourself | Enemies can only target this unit within 6 inches while it is HIDDEN, instead of 12 inches. |

Phantom Shot's accepted direction replaces the original simultaneous +2 hit / +2 injury / +2 Stress package with extra Stress on non-wounding hits. The original Stress amount was +2, but the accepted replacement wording did not specify the amount or settle per-hit accounting; confirm during the mechanics pass.

### Duelist — melee offence and movement

| Skill | Working effect |
| --- | --- |
| Ambidextrous | When dual wielding two 1 HANDED melee weapons that BOTH have AGILE, the off-hand contributes its full attack dice instead of one. |
| Blade Fury | Once per turn, after downing an enemy in melee, make a free MOVE and ATTACK against another enemy within 6 inches. If that enemy is downed, repeat once more against an enemy within 3 inches. |
| Parry | When an enemy fails to hit this unit in melee, it may make an UNANSWERED melee counterattack against that enemy. This can trigger Blade Fury. |

Parry's failed-hit trigger replaces the original survives-a-melee-attack trigger. Normal opposed damage, repeated triggers, and counterattack loops still need an explicit resolution rule; none is assumed here.

**Weapon gate:** Ross clarified that AGI-based melee belongs to the weapon characteristic, called AGILE in this draft. Earlier live weapon text used BALANCED for AGI substitution; reconcile the name later. The universal STR-or-AGI melee suggestion was withdrawn. Remove the redundant Agile skill. Ambidextrous replaces it in the archetype, not in flex. It does not unlock full attacks for two sledgehammers merely because Goliath makes them count as one-handed; both weapons must independently have AGILE. Footwork was an alternative suggestion, not selected.

### Traceur — movement and elevation

| Skill | Working effect |
| --- | --- |
| Acrobatic | Climb scalable structures without climbing gear or access points. Climbing costs movement equal to half the structure's height. |
| Dodge | When targeted by an enemy CHARGE or MELEE ATTACK, test AGI. On success, move 3 inches. Resolve the enemy's charge, but omit its melee attack if this unit is outside engagement range. |
| Aerial Assault | From a structure at least 3 inches high, select an enemy within charge range. Roll to charge, then test AGI on success. If both succeed, move into engagement and make an UNANSWERED attack, gaining +1 to hit and injure per 2 inches of starting elevation above ground, up to +4/+4. |

Aerial Assault's failed-test consequences and interaction with Ambush remain for later. The suggested direction is that overlapping UNANSWERED effects do not create extra attacks; do not assume a new attack chain from duplicated keywords.

### Flex — selected

| Skill | Working effect |
| --- | --- |
| Quick | Passive: +2 MOVE. |
| Sneak | Ignore the movement penalty while HIDDEN. |
| Sprinter | DASH using only the MOVE action instead of spending both actions. |

Sprinter preserves the other action; it does not grant an additional action. Run + Gun refers to a normal MOVE, so Sprinter does not automatically permit shooting midway through a DASH. Escape Artist and Sure Footed were rejected/not selected as too situational or unnecessary alternatives. The earlier placement of Ambidextrous in flex is superseded by its conditional Duelist version.

### Next discussion: INTELLIGENCE

DEX and AGI concept passes are complete enough to move on. INT archetypes and skills are next; none has yet been selected in this pass. Continue prioritising playstyles, broadly usable skills and cross-stat combinations before exact action economy. Keep hacking and interactive terrain relevant without making INT useful only on boards with bespoke devices.

### INT Hacker proposal — Neural Uplink (2026-09-24)

Ross proposed the first skill for the Hacker archetype during voice discussion. Name is tentative; the other Hacker skills and INT archetype choices remain open.

| Skill | Archetype | Working effect | Status |
| --- | --- | --- | --- |
| Neural Uplink | Hacker | Gain +4 to hacking tests when resolving a HACKING action at a terminal. | Ross's proposal; name and balance provisional. |

This bonus applies to hacking, not all INT tests. It does not itself grant remote terminal access, new device functions, or a bonus to a separate counter-hacking procedure. Exact terminal-access requirements remain for the mechanics pass. Master rules unchanged.

### INT Hacker trio — Hijack and Counter-Hack added (2026-09-24)

Ross explored direct hacking against units to give hackers something to do without terminal-heavy terrain. Communications interference causing Stress was considered but not selected. False Orders removing Ready and Feedback were assistant alternatives, not adopted skills. Ross then favoured hacking terrain and enemy electronic deployables.

| Skill | Working effect | Status |
| --- | --- | --- |
| Neural Uplink | +4 to hacking tests when resolving a HACKING action at a terminal. | Retained proposal. |
| Hijack | Test INT to take control of an enemy deployable with the ELECTRONIC keyword and perform one of its normal actions. No terminal required. | Ross accepted this direction after the assistant proposed temporary control for one action. Name and keyword spelling provisional; range and costs unspecified. |
| Counter-Hack | While in base contact with a terminal, when an enemy attempts to hack using another terminal within 24 inches, test INT. On success, cancel the enemy hack and shut down the enemy's terminal until the end of the following turn, preventing its use next turn as well. | Ross's third-skill proposal; assistant working name. |

Counter-Hack uses an INT test, not an assumed opposed test. The working reading measures 24 inches between terminals and shuts down the enemy terminal; confirm precise range reference and shared-network eligibility during wording. Ross described interaction then specifically cancelling a hack: no blanket power to interrupt non-hacking manual interactions is inferred. Exact meaning of turn, reaction resources, frequency and whether Neural Uplink applies to the interruption remain open. This proposed shutdown affects the enemy terminal, unlike the older self-overload Interrupt mechanism; reconcile rather than stack those systems during eventual integration.

This trio offers reliable terminal access, exploitation of enemy devices, and denial of enemy terminal use. It still depends on available infrastructure or enemy electronic deployables; it does not establish universal communications equipment or unrestricted hacking of ordinary units.

### Interactive terrain required at setup — Ross's direction (2026-09-24)

Ross intends board/scenario setup to require a minimum quantity of additional interactive terrain features, ensuring hackers have meaningful targets on every board. The number and selection procedure are not yet decided. Examples include cranes, elevators, retractable bridges and opening pits; manipulating these may create damaging attacks or hazards as well as access and movement options.

Doors and windows belong to ordinary terrain and are separate from this required feature list. They do not fill the minimum by themselves. Ross considered requiring variety, then favoured excluding ordinary doors/windows from the additional-feature list; no specific category quotas were selected. The assistant's proposed one movement hazard / one objective-control piece / one damage threat remains an unadopted example.

This is a workshop setup requirement for eventual integration, not an edit to the live board/scenario rules.

### INT Medic archetype — first skill (2026-09-24)

Ross moved from Hacker to Medic and proposed its base skill:

| Skill | Archetype | Working effect | Status |
| --- | --- | --- | --- |
| Medic | Medic | Gain +4 to STABILIZE rolls. | Ross's proposed base skill. |

This bonus does not itself alter the outcome of Stabilize, restore Wounds, waive medical equipment requirements, or change its action cost. The other two Medic skills remain open.

## 18. INTELLIGENCE — Ross's full fifteen-skill proposal (2026-09-24)

Latest conceptual roster: Hacker / Tactician / Artificer / Medic, three skills each, plus three flex. This supersedes the earlier proposed Engineer/Saboteur grouping and the partial voice drafts where they differ. The table includes the subsequently confirmed TAGGED replacement and Chemical Cocktail / Stims grouping swap. Concept selection is complete; no live integration or final balance approval.

| Archetype | Skill | Proposed effect |
| --- | --- | --- |
| Hacker — control/offence | Neural Uplink | +4 INT when resolving HACKING tests. |
| Hacker | Trojan | Test INT to take control of an enemy DEPLOYABLE with ELECTRIC. Immediately resolve an action with it. SINGLE USE deployables may be triggered or defused; resolve their action if triggered, then remove them in either case. |
| Hacker | Interrupt | While in base contact with an active terminal, when an enemy interacts with another terminal within 12 inches, test INT head-to-head. On success cancel the interaction and FREEZE that terminal until the end of the next turn. May be used even after this unit has activated. |
| Tactician — support | Tunnels | After board setup, before deployment, place two tunnel tokens: 8 inches from enemy deployment or units, 12 inches from each other, 6 inches from the board edge. Secretly hold two crew units back during deployment. During battle, deploy one model at a tunnel; the same tunnel cannot serve both units. Activate the arriving unit normally; enemies may react to its arrival. |
| Tactician | Strategist | Once per game, during any turn's initiative phase, decide who activates first. |
| Tactician | Tagged | Test INT while within 12 inches and LOS of an UNCONTESTED objective. On success, your crew controls it until an enemy captures it. Your crew may have only one TAGGED objective at a time. |
| Artificer — defensive offence | MOLLE | Equip up to three unique DEPLOYABLES for battle. |
| Artificer | Technician | +4 INT when testing to set up a DEPLOYABLE during battle. |
| Artificer | Quick Drop | Once per turn, after successfully placing a DEPLOYABLE, place another for free within LOS and 8 inches of the first. |
| Medic — support/buffs | Stabilize | +4 INT for STABILIZE tests. A successful Stabilize also removes all target Stress. May spend an action to Stabilize a non-Down unit and reduce its Stress to zero. Once per turn. |
| Medic | Chemical Cocktail | Resolve two CHEM actions on the same unit. |
| Medic | Doc | Equip up to three unique CHEMS. Once per turn, resolve a free CHEM action on a friendly within 6 inches. |
| Flex | Inspector Gadget | Equip up to three EQUIPMENT items for battle. |
| Flex | Stims | Once per turn, give two units within 6 inches an additional MOVE action during their next activation. Each target gains 1 Stress at the end of that activation. |
| Flex | Smart | Resolve a free INTERACT action once per turn. |

### Changes from earlier discussion and deferred details

- Neural Uplink now names HACKING tests without the former explicit at-terminal restriction. Which other skills count as HACKING tests remains to be classified.
- Trojan replaces the Hijack name; ELECTRIC is Ross's latest keyword spelling. Immediate use is specified, but the duration of control over a reusable device and range remain open.
- Interrupt replaces Counter-Hack; its range is now 12 inches and it explicitly uses opposed INT. The latest trigger says terminal interaction, broader than the earlier hack-only interpretation; do not silently narrow it. Exact range origin, frequency, network rules and FREEZE recovery timing remain for later.
- Tunnels' placement distances are recorded as supplied; minimum/exact interpretation, arrival timing and declaration secrecy require wording later. No extra activation inferred from arrival.
- Medic was questioned as too narrow during voice discussion. Field Support, Reinforce Armour and Extraction were suggestions, not selected. This full proposal restores Medic as a broader medical/chem support archetype.
- Stabilize's non-Down use test requirement and scope of once-per-turn need clarification later. Preserve full Stress clearance and do not restore the earlier bonus-only effect.
- Capacity effects need a shared equipment taxonomy: equipment, deployables and chems may be overlapping categories. Do not infer additive slots, free purchases, replenishment, or waived consumable use from these skills.
- Quick Drop's free placement must later specify carried stock, setup tests and legal placement; no free creation of a device is assumed. Its 8-inch placement is a meaningful remote-placement benefit as well as an action saving.
- Chemical Cocktail supplies permission for two CHEM actions, not automatically two free actions. Stims does not yet specify whether it is itself a CHEM action.
- Smart's INTERACT scope must eventually be reconciled with terminal use, objectives, deployable setup and medical actions. Do not assume all named INT actions qualify.

### Concept review — assistant assessment, not adopted changes

Retain the four groups for discussion: environmental/device control; deployment and activation timing; deployable positioning; medical and chem support. Medic now has work before casualties occur. Tactician's Inspire overlaps NRV's intended rally/leadership identity more than its other two skills; consider a positioning/redeployment alternative if needed after NRV is designed. Chemical Cocktail is strongly chem-specific and might fit Medic better, with Stims a potential broader flex choice. Capacity skills must remain distinct from Inspector Gadget to avoid one subsuming another. Strong combinations are intentional; no balance or action-economy approval is implied by keeping the concepts.

### INT concept pass completed — subsequent decisions

- Ross explicitly swapped Chemical Cocktail into Medic and Stims into flex. Effects are unchanged. Medic is Stabilize / Chemical Cocktail / Doc; flex is Inspector Gadget / Stims / Smart.
- INSPIRE leaves INT and belongs in NRV. Retain its proposed once-per-turn automatic rally of a Broken unit within 12 inches and LOS as a candidate for the Nerve pass, not an automatically finalised NRV slot.
- TAGGED replaces INSPIRE in Tactician. UNCONTESTED will have a shared entry in the rulebook's KEYWORD section at integration time, rather than repeating its definition in the skill. Its exact definition and the handling of the previous tag when tagging another objective remain for the mechanics pass. The proposed meaning was no enemy within control range; do not silently equate this with every possible objective-control use of uncontested.
- STICKY was the earlier physical-presence version, superseded by TAGGED's remote INT test. Contingency, Decoy, Sabotaged Approach and Prepared Ground were assistant alternatives, not selected.
- NRV should own rallying and most Stress management. STABILIZE is retained as a deliberate medical exception. This does not automatically remove previously selected Stress effects from STR, AGI or other groups; reconcile boundaries in the final pass.
- The preceding concept-review paragraph records the earlier assessment; the current table and these decisions supersede its unadopted replacement/swap suggestions. Proceed to NRV; action costs, frequencies, interaction scopes and balance remain deferred.

## 19. NERVE — Ross's first complete concept proposal (2026-09-25)

Ross deliberately uses three designer-only archetypes plus extra flex; no player-facing archetype prerequisites. Four groups are not mandatory. This submitted list contains sixteen skills (nine grouped, seven flex), one above the target fifteen. Nothing is cut or adopted as final by recording it.

| Group | Skill | Proposed effect |
| --- | --- | --- |
| Commissar — support | Inspire | Once per turn, spend an ACTION and test NRV. On success remove 2 Stress from three friendly units within 8 inches. |
| Commissar | Rally | Once per turn, spend an ACTION and test NRV. On success automatically rally up to three units within 8 inches. |
| Commissar | Motivate | Test NRV; choose two friendlies within 8 inches. Each gains an additional ACTION point in its next activation and may repeat the same action in that activation. Alternative proposed by Ross: instead allow each to spend its MOVE as a normal ACTION and repeat actions, without an extra action point. Choice unresolved. |
| Berserker — melee/offence | Rage | Once per turn, add up to three dice to a MELEE ATTACK pool. After resolving it, gain 1 Stress per added die. |
| Berserker | Sin Eater | Once per turn, spend an ACTION to remove up to three Stress in total from friendlies within 6 inches, taking an equal amount onto this unit. |
| Berserker | Implode | Increase this unit's maximum Stress by two. Shift BREAK results up by two. Once per turn halve this unit's Stress; each point removed grants +1 hit and injury for its next MELEE ATTACK. |
| Anchor — defence | He's on Our Team | Spend an ACTION and pass NRV to activate a 6-inch aura granting friendlies within range +2 ARMOUR. |
| Anchor | Menacing | Spend an ACTION and pass NRV to activate a 6-inch aura: friendlies within range inflict +1 Stress on enemies. |
| Anchor | Big Aura | May maintain two AURA effects at once. |
| Flex | Roar | Pass NRV; enemies must pass NRV to charge this unit or friendlies within 3 inches. |
| Flex | On Your Feet | Choose two friendlies within 8 inches and test NRV; on success clear Stress from all three units (source plus selected allies). |
| Flex | Lean on Me | Pass NRV to activate a 6-inch aura transferring Stress inflicted on friendlies in range to this unit. |
| Flex | Not Time for a Nap | Pass NRV; units within 8 inches automatically clear PINNED or SHAKEN. Stress points remain. |
| Flex | Solid | +1 Wound. |
| Flex | Commanding Presence | Once per turn, a friendly within 8 inches and LOS may use this unit's NRV for a BREAK test. |
| Flex | Beta Blocker | Halve Stress penalties to rolls; e.g. 6 Stress imposes -3. Does not affect BREAK tests. |

**Proposed AURA shared rule:** A passive effect remains active until its source activates another aura or is DOWNED. Big Aura raises the simultaneous limit to two. Exact replacement with two slots, self-affecting eligibility, LOS and other incapacity endings remain for later wording.

### Supersession and open concepts

- Latest Inspire reduces Stress. Earlier INT-to-NRV Inspire auto-rally draft is superseded in this slate by the distinct Rally skill and its test/range/target wording.
- STR already has a Berserker group and a Rage skill with a different effect (+Damage for Stress). No relocation, deletion, or replacement of STR was requested. Resolve the overlap deliberately rather than silently merging the two Rage effects.
- On Your Feet overlaps Inspire and can clear more Stress from a comparable number of units. Recommend merge/cut one to reach fifteen; not yet approved.
- Big Aura has no effect without access to another aura, unlike the desired independently attractive skill choices. Consider a built-in modest effect or treat as a deliberate exception; neither adopted.
- Stress transfer must not destroy overflow at the recipient's cap. A possible later rule is transfer only what the source can actually receive, leaving excess with original targets. Implode introduces a proposed cap of seven for its user against the ordinary five; rounding and direction/meaning of shifting BREAK results remain unspecified.
- The workshop has no separate flat Shaken penalty beyond accumulated Stress. Clearing SHAKEN but retaining Stress does not have a defined lasting benefit; Not Time for a Nap may focus on Pinned instead.
- Solid duplicates STR Tough. Retaining both raises a deliberate duplicate-benefit/stacking question; no new Wound maximum authorised here.
- Motivate's MOVE conversion is the assistant's preferred direction: flexible action use with a movement sacrifice. It is not adopted merely by being recommended. Cost, repeat-action limits and recipient frequency remain deferred.
- He's on Our Team has a clear protective role but its literal armour increase needs thematic consideration. Menacing is offensive support within the Anchor group; designer labels need not be exclusive.
- This is a concept review, not a balance test. Preserve strong combinations such as Sin Eater / Implode, Lean on Me / Beta Blocker, and protective / offensive aura choice without assuming unbounded chains or new free-action permissions.

## 20. Eventual integration checklist — inactive until authorised

1. Produce a reviewed, internally consistent proposal from the current direction and close relevant open questions.
2. Reconcile d20 resolution, Stress, Pinned, attack outcomes, skills, and progression together.
3. Audit references in the live master, Conditions, Morale, skill records, weapons, unit creation, advancement, and relevant simulations.
4. Only with approval: update the live rules, ledger, roadmap, and satellite references; regenerate affected catalogues and validate consistency.
5. Preserve this discussion log as rationale and history. Do not use it as a competing source of live rulings.

## Integration authorised — 2026-09-25

Ross accepted the assistant's final NERVE roster with HOLD FAST changed to flat -2 incoming injury rolls, regardless of cover. The fifteen are Inspire, Rally, Motivate, Sin Eater, Implode, Last Laugh, Hold Fast, Menacing, Lean on Me, Roar, On Your Feet, Commanding Presence, Beta Blocker, Unflinching and Big Aura. They are recorded in [[Rules System/Skills#NRV]].

Ross authorised archiving all previous skill-system entries and integrating the 75-skill replacement. Old skill material is archived. Skill acquisition is explicitly undecided, following his answer during integration. [[Skill Integration Decisions]] records remaining mechanics; this is not a claim of completed balance testing or a finished playable engine.
