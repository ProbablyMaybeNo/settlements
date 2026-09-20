---
type: working-discussion
status: exploratory-not-adopted
created: 2026-09-20
updated: 2026-09-20
tags:
  - settlements/workshop
  - settlements/skills
  - settlements/combat
---

# Skills and Combat Rework — Thread Log

> [!important] Separate working document — not live rules
> This note tracks the discussion in this Codex task. It is outside `Rules System/` and does not amend the master, rules records, ledger, or roadmap. Decisions here are workshop directions until Ross explicitly authorises integration. The vault's scheduled mirror may copy this file into the repository; that does not make it authoritative.

## How to use this log

- Add subsequent discussion to the dated journal and update the current direction and open questions.
- Distinguish **Ross's direction**, **assistant proposal**, **unresolved**, and **superseded**. Do not turn an assistant suggestion into an adopted rule through repetition.
- Preserve prior wording when a substantial change needs comparison. Keep the current direction prominent.
- Keep skill effects concise; put shared rules and edge cases outside the effect text where possible.
- This is a structured discussion record, not a verbatim transcript. Earlier abandoned catalogues are summarised; the latest complete 60-skill draft is preserved below.
- Maintain this note as this task continues. No background automation or automatic capture has been configured.

## Current direction at a glance

| Topic | Current workshop direction | Status |
| --- | --- | --- |
| Skill count | 12 skills per stat, 60 total, all in one tier; replacing the proposed 30 per stat across three tiers. | Ross confirmed |
| Skill purpose | Define tactical approaches and unit archetypes. Combat and defensive benefits are allowed. Avoid universally useful numerical upgrades with no interesting decision. | Ross directed |
| Combinations | Support combinations within a stat and across stats. Players should discover interactions rather than receive mandatory build recipes. | Ross directed |
| Signature themes | STR Grapple; DEX Spotted/Marked; INT Hacking; AGI Ambush; NRV local buffs/debuffs rather than one signature state. | Ross proposed; structure still exploratory |
| Avoid mandatory builds | Signature mechanics should support some skills without making the other choices unattractive. Follow-ups should normally work independently. | Shared design direction; exact implementation untested |
| Dice | The working system uses d20s. The older master text used in earlier answers still said d10. | Ross corrected; full d20 specification not supplied here |
| Positive skill bonuses | Increase the drafted +1 bonuses to +2. | Ross directed; not yet applied to the preserved catalogue below |
| Ordinary attack outcomes | Miss: nothing. Hit and wound: lose 1 Wound. Hit without a wound: 1 Stress and Pinned, for both ranged and melee. | Direction agreed in discussion; multi-die details unresolved |
| Suppressed | Remove the separate condition. | Ross directed |
| Pinned | Stops movement; clear by spending Move, retaining Action. Does not inherently prevent Shoot, Fight, Interact, or React. | Latest assistant wording consistent with discussion; final text pending |
| Stress | Each point imposes a cumulative -1 on all the unit's rolls. Clearing Pinned leaves Stress. | Ross directed; roll scope and cap interaction need closure |
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

## 7. Cumulative Stress proposal

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

## 8. Open decisions and next review

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

### Original supplied candidates — historical reference

- **STR:** Grapple, Throw, Knockback, Meat Shield, The Bull, Tough, Roar, Crush, Rampage, Just a Scratch, Come Get Some, Bullet Proof.
- **DEX:** Marked, Dead Shot, Quick Shot, Gunslinger, Run N' Gun, Sniper, Calm Under Fire, Pray and Spray, an unnamed +1 ranged Injury skill, I See You, Crossfire, Eagle Eye.
- Original high-impact concepts included extra Wounds, automatic takedowns of Grappled targets, redirecting attacks into held enemies, compulsory attacks, and extra shots. None should be treated as adopted merely because later discussion permitted combat skills.

## 10. Eventual integration checklist — inactive until authorised

1. Produce a reviewed, internally consistent proposal from the current direction and close relevant open questions.
2. Reconcile d20 resolution, Stress, Pinned, attack outcomes, skills, and progression together.
3. Audit references in the live master, Conditions, Morale, skill records, weapons, unit creation, advancement, and relevant simulations.
4. Only with approval: update the live rules, ledger, roadmap, and satellite references; regenerate affected catalogues and validate consistency.
5. Preserve this discussion log as rationale and history. Do not use it as a competing source of live rulings.
