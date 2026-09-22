---
type: design-review
status: discussion-not-adopted
created: 2026-09-22
source_spreadsheet: 1l7hMrpLqTqCJfIHnmESnVUWRgYR9NCoj5tbjcnTiU6I
source_sheet: Skills
source_sheet_id: 964457579
---
# 75 Skills — Archetype and Combo Review

> Review only. The source Sheet and live rules were not edited. Groupings and replacement concepts below are assistant proposals for discussion, not new rules or assigned prerequisites.

[Live Skills table](https://docs.google.com/spreadsheets/d/1l7hMrpLqTqCJfIHnmESnVUWRgYR9NCoj5tbjcnTiU6I/edit#gid=964457579)

## Coverage and limits

Read Skills A1:G85: 75 populated skill entries in rows 2–76, exactly 15 per stat. Also read bounded reference ranges in Conditions (A1:G40), Weapon Characteristics (A1:F35), Weapon Drawbacks (A1:F15), and Reactions (A1:F15). Those reference tabs contain older and newer wording together. This is a design/wording review, not mathematical balance testing, playtesting, or an audit of the entire workbook.

The exact readback of the Skills values is preserved in [[Skills Table Snapshot - 2026-09-22]]. No spreadsheet formulas/formatting/comments audit was performed.

## Overall assessment

The new list is substantially more archetype-driven. STR shows the clearest deliberate groups. DEX has a strong reaction-fire package. AGI has strong identity but too many damage/attack-economy effects risk converging on one dominant melee build. INT invests nine of fifteen slots in hacking or terminal effects, while medicine has only one. NRV contains a promising aggressive stress-management build as well as leadership and terror.

Do not confuse shared flavour with an interaction: two damage bonuses merely add; a skill that changes position/target eligibility/condition and another that exploits that result create a sequence the player can pursue and the opponent can disrupt.

Keep archetypes as designer labels, not restricted paths or required bundles. A skill may have a primary home and secondary synergies. Four rough archetypes plus flex is a useful budget, not a demand that every group receive exactly three entries.

## Provisional grouping of all 75 current entries

Every current skill appears once as its primary home below. This is a map of existing content, not a final allocation of slots.

| Stat | Primary home | Existing skills | Assessment |
| --- | --- | --- | --- |
| STR | Tank / protector | Come Get Some; Weather the Storm; Tough | Clear taunt-to-protection relationship. Tough is broadly useful, not inherently tank-exclusive. |
| STR | Grappler | Grapple; Throw; Meat sheild | Strong control identity; wording currently makes the grappler/payoffs relationship uncertain. |
| STR | Charger | The Bull; Breakthrough; Cannonball | Clear approach and charge payoff, but Cannonball overlaps Rampage and can chain as written. |
| STR | Bruiser (rather than generic DPS) | Knockback; Heavy Hands; Rampage | Potential for positioning/condition setup into close-combat payoff. Needs distinction from charge-chain build. |
| STR | Flex / equipment handling | Strong Back; Double Strength; Goliath | Can change loadouts sharply; not automatically small benefits. |
| DEX | Marksman | Mark Target; Deadeye; Sniper; Eagle Eye | Good ranged target-selection identity; clarify Mark versus Hidden and cover. |
| DEX | Mobile shooter | Run N’ Gun; Gunslinger; Double shot | Includes alternate sidearm and two-handed routes. Gunslinger and Double shot are loadout branches, not one unit's compulsory package. |
| DEX | Overwatch specialist | Bullet Time; Ready to React; Ready and Waiting | Clear preparation/timing/payoff. Needs a shared reaction budget and costs. |
| DEX | Suppressor / fire support | Pin Them Down; Pray and Spray; Crossfire | Split fire creates multiple control opportunities and hits for allies. Wound-per-target rules need deciding. |
| DEX | Flex | Calm Under Fire; Speed Loader | Keep effects precise; Calm Under Fire is presently ambiguous. |
| INT | Network controller | Hacker; Counter-Hacker; Remote Operator; Systems Operator; Neural enhancment | Strong group, heavily subsidised by automatic successes/free operations. |
| INT | Saboteur | Mind melter; Mind tricks; Terminal overload; Surprise hack | Strong active disruption identity, but several effects depend on undefined technology and sequencing. |
| INT | Engineer | Quick build; Dump n go | Good deployment sequence potential, but resource expenditure/recovery is missing. |
| INT | Medic | Medic! | One skill is a specialist ability, not yet a supported archetype. |
| INT | Flex / logistics | Surveyor; Salvager; Gadgets n gizmos | Useful broad support; extra equipment particularly supports engineering and medicine. |
| AGI | Infiltrator / ambusher | Ambush; Low Profile; Vanish | Clear concealment loop; carefully bound re-hiding and hit-based reveal exceptions. |
| AGI | Duelist | Finesse; Riposte; Surprise shot | Stat substitution, response, and unusual weapon handling. Surprise shot needs legal hand/weapon handling and pool rules. |
| AGI | Mobile skirmisher | Hit and Run; Dodge; Action on the Run; Blade flurry | Strong but overloaded with movement/extra attacks; two movement rules overlap. |
| AGI | Acrobat / aerial raider | Parkour; Dive bomber; Wall Runner | Strong route identity. Wall Runner forbids climb-and-charge, so aerial setup generally spans activations unless a later rule changes it. |
| AGI | Throwing specialist package | Up my sleeve; And another | Potential fifth archetype, but only two slots; decide if a full identity or optional loadout branch. |
| NRV | Commander | Pep talk; Advance!; Good Aura; Boss man | Accuracy, movement, and objective influence. Define aura limit and control-counting rules before valuing two entries. |
| NRV | Rallying leader | Rally; On Your Feet; Commanding Presence | Existing condition/Stress wording prevents a clean comparison. |
| NRV | Terror leader | Dread Presence; Intimidating | Clear enemy-facing pressure. Room for a skill that establishes the initial Stress or a positional trigger. |
| NRV | Fanatic | Take It on Me; Red Mist; Bloodlust; Beta blocker | Promising shared resource loop: absorb/accept pressure, manage its penalties, remove it through aggression. |
| NRV | Flex | Inspiring Example; Iron man | Inspiring Example bridges aggressive/support builds; Iron man duplicates STR Tough. |

## Most promising interactions to preserve

1. **Come Get Some + Weather the Storm:** encourage attacks from several enemies, then resist later attackers. Enemy choosing not to attack is meaningful counterplay.
2. **Knockback/Throw + Heavy Hands:** create a disadvantageous position/condition, then exploit it. Pinned-from-melee is an explicit change from the ranged-only workshop boundary and must be decided.
3. **Ready and Waiting + Bullet Time:** establish overwatch and choose the point in the opponent's movement when it fires. Powerful but recognisable; Ready to React must not accidentally add another unlimited response.
4. **Mark Target + Crossfire/Deadeye:** spending an Action setting up a target increases later attack quality. Allies can provide the setup. Latest Marked-reveals-Hidden direction needs propagation.
5. **Gadgets n gizmos + Quick build + Dump n go:** carry more, deploy efficiently, deploy during movement. Preserve meaningful consumable/Action costs so the whole build does not place free hardware at no opportunity cost.
6. **Take It on Me + Beta blocker + Red Mist/Bloodlust:** accept friendly Stress, tolerate it, fight under pressure, then shed it. At the Stress cap, prohibit transferring more than the receiver can actually gain unless deliberate deletion is intended.
7. **Ambush + Wall Runner/Dive bomber:** vertical positioning creates future approach opportunities, but current no-climb-and-charge and Charge-only Ambush wording mean this is not an automatic same-activation combination.

These recipes are designer review examples, not suggested player-facing prescribed builds.

## Resolve mechanics before judging power

### Major action-economy effects
Cannonball has no explicit chain limit; Rampage is once per round. Blade flurry explicitly grants up to two extra attacks, unlike the earlier provisional one-bonus-attack cap. Gunslinger grants a free full Shoot on a successful Shoot; define whether success means hit or wound and whether the second Shoot can trigger it. Double shot grants a kill-triggered full Shoot, potentially alongside other attack grants. Systems Operator's free second operation could recursively qualify itself. Ready and Waiting gives a free Ready every activation. Dodge has no printed use cost or frequency.

A normal shared attack budget with clearly printed exceptions is preferable to treating each missing limit as unlimited or silently forcing the old cap onto new deliberate effects.

### Opposed melee and loadouts
Unwieldy says Fights Last in Weapon Drawbacks, but this workshop rejected straightforward first/last ordering for single head-to-head exchanges. Goliath cannot be evaluated until Unwieldy has a working effect. Double Strength plus Goliath may erase the key costs of two heavy melee weapons. Surprise shot refers to three weapons in one pool; define carried versus wielded weapons and stat selection. Down-triggered melee skills (Cannonball, Blade flurry) require a decision on whether melee still goes directly Out at zero Wounds.

### Control wording
Grapple's effect uses "unit" and "enemy" ambiguously: does the no-Attack restriction apply to the holder or the held target? If the holder cannot attack, Throw and weapon payoffs need explicit permissions. Throw uses an ordinary STR test, not opposed STR: intentional or omitted defence? Meat sheild is a hard prerequisite payoff rather than independent utility. That can be allowed deliberately, but the core Grapple purchase must not become compulsory for every STR build.

### New direction versus reference-tab drift
- Mark Target Notes say Marked does not remove Hidden, conflicting with the latest conversation.
- Conditions retains Suppressed, Pinned cleared using Move, and flat Shaken -1, conflicting with the latest workshop.
- Pin Them Down says any ranged hit Pins, while Weapon Characteristics/Suppression says non-wounding hits. Confirm rather than assume.
- On Your Feet clears Shaken but Notes say it removes no Stress. Under cumulative Stress, define whether it actually removes Stress or temporarily ignores the penalty.
- Red Mist still says ignore Shaken; define whether this ignores the full current Stress penalty or an obsolete flat penalty.
- Vanish's old Notes require no enemy within 6 inches with LOS. Its new reactive effect needs range/LOS and timing defined without secretly inheriting unintended old restrictions.
- Calm Under Fire says ignore first non-wounding hit while Notes say conditions and Stress still apply. What is left to ignore? Choose cancelled hit, cancelled Stress, cancelled Pin, or some named effect.
- Tough has Rooted's falling note; Mind melter has Jury-Rig's repair note; Surveyor has Demolitionist's Blast note; Blade flurry retains Scramble's no-Engagement note. These are incompatible carryovers, not reliable balancing restrictions.
- Type labels also need correction after rules: Tough is Passive, Quick build looks Action, Mind melter looks an Interrupt/Triggered ability, Bullet Time modifies a reaction, Systems Operator grants a triggered extra operation.

### Literal omissions / user-owned unresolved cells
Neural enhancment Requirements contains "Increase " and is incomplete. Do not infer the intended requirement. Some new skills have no Type/Notes yet. Pep talk lacks an explicit duration in Effect (Notes end on movement); Good Aura assumes a one-active-aura rule not established by the read entries. Boss man counts models twice but reviewed older scenario control is uncontested presence, not majority counting.

## Recommended cuts, merges, and additions for discussion

- Merge **Cannonball/Rampage** into one clearly limited continuation attack, or differentiate them by outcome: one charge-route momentum skill and one ongoing-melee response. Do not keep two slightly different kill-chain engines just to fill two archetypes.
- Rework one of **Action on the Run/Hit and Run**. Current Action on the Run no longer helps interactions; it splits movement around melee and overlaps Hit and Run. Restoring the objective/Interact role would support an AGI runner without weakening the other melee skill.
- Decide whether **Tough/Iron man** should be the same non-stackable skill accessible from either stat or separate effects. Generic +1 WND is extremely broadly useful in a mostly WND-1 system and should not be called harmless flex. The current sheet does not define cross-stat stacking.
- Replace **Mind tricks** unless a clear technological explanation supports compulsory movement toward a terminal. An equipment/communications deception or local device-control effect fits the grounded setting better than unexplained mind control. Mind melter likewise needs a physical path for damaging a human through hacking.
- Rework **Hacker** from blanket automatic success if hacking reliability is meant to be a build dimension. Automatic success bypasses Stress and makes some future hack-test bonuses irrelevant. Retaining it would require a narrow domain or meaningful cost.
- Add a second/third **Medic** interaction if Medic is to be a real archetype. Candidate roles: move a casualty into treatment position; spend Ready to Stabilize; clear a limited amount of Stress after successful treatment. These are design slots, not approved effect values.
- Add an **Engineer retrieval/reposition** option if hardware relocation is intended; it creates another tactical decision without adding more free attacks.
- Add a **Terror setup** option if NRV terror needs a third skill: a short-range action that establishes Stress or rewards isolating an enemy, rather than another passive penalty aura.
- For **Boss man**, first define objective control. If presence-based, consider an objective-interaction/timing benefit instead of meaningless double counting.

## Proposed next design pass

1. Agree intended stat identities/archetypes using this map; do not require all groups to be equally sized.
2. Clean conflicting Notes/Types and settle the few common mechanics that determine whether combinations work.
3. Give each supported archetype an independent entry skill, a compatible payoff, and a way to position/recover; share flex skills across them.
4. Replace overlap and unsupported isolated entries before increasing counts further.
5. Compare 1-, 2-, and 3-skill packages, then cross-stat combinations. Compare full Actions, denied enemy Actions, objective contribution, exposure, and failure risk; not just raw damage.
6. Test normal scenarios and interactive terrain. No sim or full balance claim has been made in this review.

