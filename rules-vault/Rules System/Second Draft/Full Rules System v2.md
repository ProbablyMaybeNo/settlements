---
type: master
status: Active second draft — incomplete
created: 2026-09-27
---
# Settlements — Full Rules System v2

> [!important] Active working draft
> Only recorded discussion decisions are carried forward. Blank systems have NOT been adopted. Earlier master/satellite rules are legacy reference, not fallbacks. This draft is not a complete playable ruleset or a balance claim.

[[Rules System/Second Draft/Draft 2 - Sources and Status|Sources and Status]] · [[Rules System/Second Draft/Draft 2 - Progress and Decisions|Progress and Decisions]]

**Status legend:**

- <span style="color:#2e7d32"><strong>RECORDED · GREEN</strong></span> — selected direction, with any listed follow-ups.
- <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span> — some mechanics recorded; important work remains.
- <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span> — no rules adopted yet.
- <span style="color:#c62828"><strong>OUTDATED · RED</strong></span> — superseded and retained only for history.

The colour is a reading aid, not a second rules layer. Blank sections remain undecided.

**TEST** is reserved for simulation-only material and remains explicitly labelled where it appears.

## 0 · The one rule everything else answers to

**Status: <span style="color:#2e7d32"><strong>RECORDED · GREEN</strong></span>.**

Weapons provide offensive capabilities; Armour provides protection; Equipment supplies temporary or limited-use options; Advancements and Injuries record lasting development and consequences.

Skills define tactical choices and discoverable combinations within and across stats. Offensive and defensive effects are allowed. Archetypes guide design; they are not compulsory player-facing paths. Explicit skills such as Tough and Quick may change characteristics.

**Still to write:** a concise second-draft design statement and final category boundaries.

---

# PART I — CORE GAME & COMBAT

## 1 · Core Game Format

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** board size, crew size, deployment, game length, victory and end conditions. The discussion supports scenario-guided interactive boards; it does not re-adopt Draft 1's exact formats.

---

## 2 · The Core Test

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Ordinary tests and shooting use **1d20 + relevant stat + modifiers vs 15+**. Natural 1 fails; natural 20 succeeds. Charge distance explicitly uses d6.

| Source | Cap |
| --- | --- |
| Skills | ±4 |
| Weapons | ±3 |
| Stats | ±6 |
| Armour | ±6 |

Skill modifiers stack within their cap; different sources combine. Other modifiers stack. These replace the previous global +6/±3 caps.

**Cap arithmetic (2026-09-29):** cap positive and negative contributions separately within each source, then combine. Printed weapon Damage is separate from the weapon modifier cap. Skill-granted Damage remains a skill-source roll modifier. Caps apply to roll modifiers, not Attack Dice, inches or Wounds. Stress and terrain are separate sources. Hidden and applicable cover stack. The +3 skill-cap proposal was not adopted.

**Next-pass working rulings:** opposed natural results and other bounded implementation choices are specified in [[Draft 2 - Simulation Assumptions]]. These are explicit test choices, not permission to guess or fill unrelated blank systems.

**Opposed tests:** the earlier single-test direction gave ties to the defender. Latest melee pool ties cause no hits; do not silently extend melee's rule to every single-test contest.

---

## 3 · Turn Structure & Activation

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Players alternate activating units. An activation supplies **one Move and one Core Action**; skills can grant alternatives or additional actions. Dash and Charge spend both. A reaction is one permitted action outside activation, not an activation refresh.

**READY:** gained using an Action, Order, skill or ability, including after activation. It carries between rounds until used, cancelled by movement/another regular action, hit by an attack, or explicitly removed. A permitted READY reaction spends the token. Maximum one READY token per unit. Pinned units cannot use reactions except movement permitted by the Pinned rule; retaining READY does not override action restrictions.

**Triggers:** an enemy starts or finishes an action within LOS and applicable range, or a skill/ability grants a reaction. Permitted choices: ranged/melee Attack, Charge, Interact, Hack, Deploy, Skill action, Move, Hide, Dodge. Reactions cannot trigger other reactions unless explicitly permitted. The discussed pre-action reaction resolves before the declared action; if it Pins/Downs the actor, the declared action is lost.

**Return Fire — test variant:** when a READY unit is targeted by a ranged attack, it can spend READY to make a legal shot back. Both roll opposed attack pools using §8's highest-total comparison with DEX. Resolve both attacks once; ties cause no hits. Against movement or other non-shooting actions, reaction shooting remains a normal 15+ test. See [[Draft 2 - Simulation Assumptions]].

**Sequencing:** start-trigger reactions resolve before the declared action; end-trigger reactions resolve after it. A start-trigger shot that Pins or Downs the actor cancels the declared action and spends its cost, even if that action was movement. Do not cancel participation retrospectively in the simultaneous exchange that caused Pinned. Resolve an attack pool completely before its after-attack/after-Down effects. No automatic attack-back follows an exchange; explicit skill attacks retain their printed permissions and limits. [[Draft 2 - Simulation Assumptions]] specifies simultaneous-trigger and recursion handling for the next pass.

**Still to decide:** full round sequence/initiative, Orders' costs/range/counts, remaining action definitions and core Dodge. Next-pass timing choices are explicit in the linked test contract.

---

## 4 · Movement

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Move uses the unit's MOVE value. Ordinary movement cannot end within 1 inch of an enemy to initiate engagement unless Charging or resolving an explicit movement-into-combat effect. Already-engaged units can remain engaged; Blade Fury and Rampage retain their movement-and-fight permissions.

Charge spends Move and Core Action; roll **MOVE + 1d6**. Reach within 1 inch of the declared enemy to succeed and gain the free melee exchange and charge die. Human Bullet changes the roll to MOVE + 2d6. Dash moves up to **2 × MOVE** and spends both actions; Sprinter permits Dash using only Move. On a failed Charge, move up to MOVE toward the target by the most direct legal route, stopping outside engagement range; the activation ends.

**Still to decide:** normal MOVE baseline and Charge declaration limits (earlier 12-inch gate versus extended skills), general traversal, disengage attacks, forced-movement placement, and movement during engagement. Do not inherit Draft 1's 2×MOVE Charge.

---

## 5 · Terrain

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Scenarios can guide key terrain placement, with players filling the rest. Additional interactive features should be mandatory so INT has relevant choices. Ordinary doors/windows do not satisfy that additional-feature requirement. Tokens/templates can represent features where matching models are unavailable.

**Cover:** Hidden gives -4 to hit and stacks with cover; -2 cover plus Hidden is -6. The next-pass terrain fixture uses light cover -1 and heavy cover -2, explicitly recorded in [[Draft 2 - Simulation Assumptions]].

**Still to decide:** feature counts/selection, terrain density, full cover qualification, LOS/facing, traversal, height and falls. No old terrain-density balance claim is adopted.

---

## 6 · Terrain Interaction

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Interactive features provide stated operations and consequences. Tokens can be interacted with in base contact, spending an action where specified. The discussed crane moves scatter/obstacles; the pit opens/closes a template and threatens units above it or pushed into it.

**Still to write:** the shared Interact procedure and actual feature rules. Crane damage and pit death/escape examples remain exploratory; they are not automatically general terrain rules.

---

## 7 · Shooting

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Roll one **d20 + DEX + applicable modifiers vs 15+** per Attack Die, then one Injury die per successful hit (§9). Natural 1 fails; natural 20 succeeds. Use each weapon's range and characteristics; LOS is required unless explicitly overridden.

Dual wielding uses full dominant-weapon dice plus one off-hand die, retaining each weapon's Damage/traits/range. Gunslinger permits full off-hand ranged dice. Combined shooting is one action; split fire requires permission such as Bullet Time. Return Fire is the separate opposed test variant in §3.

**Still to decide:** full targeting/facing and cover procedure, special templates, reroll scope and allocation details. No d10 shooting survives into this draft.

---

## 8 · Melee

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

**Latest thread direction: highest opposing total**, superseding the September 26 hit-cancellation method.

1. Both units roll their melee Attack Dice; add each die's applicable stat and modifiers. STR is normal; AGILE weapons allow AGI.
2. Each die that **exceeds the opponent's highest total** scores a hit. Do not use a 15+ hit threshold, subtract enemy stats, pair individual dice, or cancel successes one-for-one.
3. Equal highest totals cause no hits. Units remain engaged ("locked in combat"); no extra condition or automatic attack is created.
4. Resolve Injury rolls for successful hits. No automatic second attack-back follows.

**Charge:** a successful Charge grants this exchange with **+1 Attack Die on the dominant weapon**. Already-engaged units use their Core Action to Fight.

**Dual wielding:** full dominant pool plus one off-hand die, retaining weapon identities; Ambidextrous supplies its printed exception. Goliath alone does not give full off-hand dice.

**UNANSWERED:** use the same opposing-pool comparison, but only the initiating unit can score hits. The defender provides defence only; no automatic reply.

Example totals: 22/19/16/10 versus 18/13 yields two hits for the first unit, none for the second.

**Next-pass working rulings:** natural 1/20 handling, empty defensive pools and skill-counterattack ordering are defined in [[Draft 2 - Simulation Assumptions]]. General multiple-enemy engagement remains unfinished; do not manufacture a full melee subsystem for isolated tests.

---

## 9 · Damage

**Status: <span style="color:#2e7d32"><strong>RECORDED · GREEN</strong></span>.**

Roll **1d20 + the hit's weapon Damage − target Armour + applicable modifiers vs 15+** per successful hit. Natural 1 fails; natural 20 succeeds.

- Each success removes **1 Wound**.
- Each failure adds **1 Stress**.
- A hit target with Wounds remaining becomes **Pinned**; pinning adds no extra Stress.
- At **0 Wounds**, it becomes **Downed**, including melee.

No one-Wound-per-attack cap: three successful Injury dice remove three Wounds. A four-Wound target retains one Wound and is Pinned; a three-Wound target is Downed. Resolve pools together. Surplus successful Injury dice do not automatically convert to Stress or execute a Downed target in that same attack.

**Still to write:** treatment, restored Wounds/state, bleed-out, finishing attacks and special payload interaction. Those older procedures were not re-selected for this second draft.

---

## 10 · Conditions

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

**Pinned:** hit survivors are Pinned under §9. A Pinned unit cannot resolve actions except MOVE and RECOVER. MOVE is at half speed. Spend one Core Action to RECOVER and remove Pinned. It may Recover first and then move at normal speed, or move at half speed and then Recover. Recover does not clear Stress or a break condition. Pinning adds no Stress. Suppressed is not a separate condition. Friendly recovery uses the explicit next-pass ruling in [[Draft 2 - Simulation Assumptions]].

Forced Bolt/Bugging Out movement overrides Pinned: spend both actions to Dash at normal speed. Other movement restrictions still apply unless explicitly overridden.

**Downed:** zero Wounds; precise activity/recovery/removal rules remain unfinished.

**Hidden:** −4 to hit and normally untargetable beyond 12 inches. Enemy movement into LOS alone does not reveal it; check exposure at the start/end of the Hidden unit's own activation against enemies within 12 inches and LOS. A successful hit reveals; a complete miss does not. Skill exceptions apply. See §25.

Other skill definitions: [[Draft 2 - Keywords]]. **Still to decide:** Hidden acquisition/movement penalty, Marked conflict, and the full condition list. Do not import old Fire/Poison/Break tables by default.

---

## 11 · Morale

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Stress normally caps at **5**, applying **−1 per point to all unit rolls**, including hit, Injury and ordinary skill tests. **BREAK and RALLY are exceptions: ignore Stress penalties.** Apply Stress once per roll; the unit rolling uses its own Stress. Implode extends its holder's maximum by two; other skills apply their stated exceptions. Shaken describes Stress rather than adding a second flat penalty. Injury failures generate Stress; successful wounds do not also generate it under the latest procedure.

**BREAK:** At the end of each round, a unit without a break condition and with 2+ Stress rolls **1d20 + NRV + applicable non-Stress modifiers vs 15+**. Natural 1 fails; natural 20 succeeds. Pass: clear all Stress. Fail: keep Stress and use its current amount, not the die total, to assign one break condition:

| Stress | Condition | Effect during its next activation |
| --- | --- | --- |
| 1–2 | BROKEN | Become Pinned. Recover/movement then follow the Pinned rule. |
| 3–4 | BOLTING | Spend both actions to Dash toward the nearest reachable heavy cover outside every enemy's LOS, taking the most direct safe route. Stop on reaching safety; both actions are still spent. |
| 5+ | BUGGING OUT | Spend both actions to Dash toward the nearest board edge by the shortest route, including hazardous terrain. Resolve required movement tests. Reaching the edge removes the unit from play, but not as Out of Action. |

The 1-Stress band covers a skill-forced Break test below the normal threshold; 5+ also covers Implode's increased capacity.

**RALLY:** At the End Phase, units already carrying a break condition test to Rally instead of Break. Roll **1d20 + NRV + applicable non-Stress modifiers vs 15+**, ignoring Stress. Pass: clear the break condition and all Stress. Fail: retain both and repeat that condition's behaviour next activation; do not reselect the condition from current Stress. A newly failed Break does not grant an immediate Rally test in the same End Phase.

Friendly units can use an action or a skill to attempt a Rally. Next-pass range, Pinned removal, timing and edge cases are explicitly fixed in [[Draft 2 - Simulation Assumptions]]. Implode replaces an eligible End-Phase Break test, not a Rally test.

**Still to write:** Downed persistence and additional environmental/campaign Stress triggers. The older Stress-subtracted Break formula and die-total failure bands are superseded.

---

## 12 · Hacking

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Hacking operates interactive terrain through terminals. Neural Uplink improves hacking tests. Trojan temporarily uses an enemy ELECTRIC deployable for its stated action. Interrupt contests another terminal interaction and FREEZEs the enemy terminal. Use the current skill text for the selected effects.

**Still to decide:** base Hack action requirements, terminal links and operating range, failure results, device control duration and Interrupt frequency. Previous descriptions of the old system in the working log are context, not re-adoption of its range-band rules.

---

## 12.5 · Infrastructure

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Selected direction: cranes, elevators, retractable bridges and pits can make terrain tactically interactive; represent them with tokens/templates. Doors/windows are baseline terrain rather than the entire required feature selection.

**Rules:** —

**Still to write:** feature catalogue, setup counts, operating effects, hazards and token placement. Do not copy old CRUSH/FALL calculations without review.

---

## 12.6 · Deployables

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Deployables are carried items placed during battle. Skills selected: Molle expands carrying options, Technician improves placement tests, Quick Drop grants another placement, and Trojan can use ELECTRIC enemy devices. Single-use hacked devices are consumed when triggered or defused as stated.

**Rules:** —

**Still to write:** actual item profiles, capacity, placement range/tests/failures, activation/triggers, ownership, damage/repair and replenishment. Old deployable costs and chassis are not adopted.

---

## 12.7 · Scenarios

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Scenarios should suggest key terrain and include meaningful interactive features. Tagged is the selected remote-objective skill; UNCONTESTED will be a shared keyword.

**Rules:** —

**Still to decide:** scenario roster, objective control/contesting radius, scoring clocks, deployment, victory/ties and required feature mix. No old scenario is silently selected.

---

# PART II — BUILDING A FIGHTER

## 13 · Unit Design — the stat line

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Five skill stats: **STR, DEX, AGI, INT, NRV**. Units also use MOVE and Wounds. AGILE weapon handling permits AGI melee. Tough and Quick are explicit characteristic-changing skills.

**Rules:** —

**Still to decide:** base stat lines, rank budgets, Wound ceiling, costs, Orders and unit creation. Do not copy the old rank or level tables.

---

## 14 · Skills

**Status: <span style="color:#2e7d32"><strong>RECORDED · GREEN</strong></span>.**

**75 skills, 15 per stat, one tier.** Archetypes guide design but impose no compulsory packages. Acquisition, stat eligibility and progression are **undecided**.

![[Rules System/Second Draft/Draft 2 - Skills]]

**Still to refine:** printed ambiguities and trigger/cost wording. Pin Them Down is redundant under universal pinning and remains flagged for replacement. Preserve it in the 75-skill selection until a replacement is chosen.

---

## 15 · Weapons — Basic Weapon System

**Status: <span style="color:#2e7d32"><strong>RECORDED · GREEN</strong></span>.**

The completed weapons-basics catalogue is carried forward as a design catalogue, with its own unresolved profile fields. It does not import historical prices or one-Wound attack caps.

![[Rules System/Second Draft/Draft 2 - Basic Weapon System]]

**Still to refine:** missing characteristic values, special payload interactions and final equipment/pricing. §9 governs ordinary injury outcomes.

---

## 16 · List Building

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** crew limits, costs, rank restrictions outside printed weapon access, equipment slots and skill acquisition. Fixed test loadouts are not roster-building rules.

---

# PART III — SETTLEMENT & CAMPAIGN

## 17 · Founding a settlement

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** location choice, starting structures and founding budget.

---

## 18 · The settlement canvas

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** settlement layout, space and connections.

---

## 19 · Power

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** power generation, demand and outages.

---

## 20 · Storage & caps

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** storage limits and excess resources.

---

## 21 · The structure catalogue

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** structure types, functions, costs and upgrades.

---

## 22 · Workers

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** worker assignment and benefits.

---

## 23 · Territory & the campaign map

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** territory, control and campaign map.

---

## 24 · Factions

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** faction identities and rules.

---

## 25 · Stealth & Ambush

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Ambush is an AGI skill triggered by a successful Charge begun Hidden. Its selected text supplies the AGI test, one-weapon +4 hit/injury and UNANSWERED effect, with its stated failure consequence. UNANSWERED now means the highest-opposing-roll method in §8.

Hidden grants −4 incoming accuracy and protection beyond 12 inches, with the activation-boundary and successful-hit reveal rules in §10. Ghost, Show Yourself and other skills provide exceptions.

**Still to decide:** Hide action/test, concealment requirements and movement penalty; whether Marked removes Hidden or only extends targeting; reveal on interaction/firing wording; Ambush/Parry/Aerial Assault sequence. Earlier FIGHTS FIRST/LAST ideas are superseded.

---

## 25.5 · The Campaign Turn

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** post-battle, settlement and battle-preparation sequence.

---

## 26 · Campaign persistence

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** advancement, lasting injuries, capture, promotion and retirement.

---

## 27 · Battlefield Events

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** event triggers and event table.

---

## 28 · Drones & Chems — advanced modules

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Chems are limited-use equipment. Doc expands Chem access and grants its printed application; Chemical Cocktail allows two Chem actions on one unit; Stims remains a selected skill.

**Rules:** —

**Still to write:** Chem profiles, application/consumption and whether Stims counts as a Chem. Drone rules remain blank; old Bandwidth and dependence tracks are not imported.

---

## 28.5 · Appendix — Board Representation & Tokens

**Status: <span style="color:#f9a825"><strong>PARTIAL · YELLOW</strong></span>.**

Tokens/templates can represent interactive features and their controls. Units use markers for tracked states such as READY, Pinned, Stress and skill-specific effects.

**Still to write:** complete component list, template sizes, marker conventions and physical placement. Examples in the workshop remain examples until selected.

---

## 28.6 · The Season — how a campaign ends

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** campaign length, victory and tiebreaks.

---

## 28.7 · Appendix — a worked founding and first campaign turn

**Status: <span style="color:#1565c0"><strong>OUTLINE · BLUE</strong></span>.**

**Rules:** —

**Still to decide:** a worked example after the relevant rules are drafted.

---

## 29 · What's still genuinely open

**Status: <span style="color:#1565c0"><strong>TRACKER · BLUE</strong></span>.**

Use [[Rules System/Second Draft/Draft 2 - Progress and Decisions|Progress and Decisions]] for per-section progress, outstanding questions and skill-specific gaps. Test assumptions are in [[Draft 2 - Simulation Assumptions]].

Blank sections are intentional. They must not be filled by inference from Draft 1. Adopt a section only after discussion, then record its source and update its status.

---
