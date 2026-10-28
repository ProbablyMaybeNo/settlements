---
type: settlements-design-audit
date: 2026-10-27
status: Research and recommendations; no rule changes adopted
scope: Live Draft 2 consolidated rules and individual item cards
tags:
  - settlements/research
  - settlements/draft2-audit
---

# Settlements Draft 2 — Realism, Originality, Fast Play and Bloody Battles

**Audit date: October 27, 2026.** Read this as a design assessment and a proposed order of work. All experiments below are unadopted. Existing rule text, approvals, semantic dates, IDs and anchors were left unchanged.

## 1. The design direction I recommend

**Keep the present foundation. Make exposure, suppression and the physical battlefield more consequential; remove overlapping exceptions before adding another subsystem.** Settlements already has enough material to become distinctive. Its strongest identity is ordinary, vulnerable people changing the battlefield to get something done, then living with the consequences at home.

The present draft is **dangerous to remain effective in, but relatively forgiving to survive permanently**. One Wound does not by itself make every exchange lethal. Hit chances, the separate Injury roll, Pinned recovery, revival, withdrawal and aftermath recovery all determine how bloody a battle feels.

The biggest obstacle to believable combat is currently **timing and incentives**, rather than missing ballistic detail. A prepared fighter cannot Reaction Shoot somebody crossing an exposed lane when both movement endpoints are unseen. Conversely, a fighter who is hit may spend its Move standing and still fire its Core, if the timing and remaining reactions permit. These two interactions deserve more attention than ammunition counts, hit locations or new morale tracks.

| Goal | Assessment of the current design | Most valuable improvement |
| --- | --- | --- |
| Realism | Strong vulnerability, physical routes and support decisions; conspicuous abstractions around exposure, awareness and casualty recovery | Make crossing watched ground dangerous; test whether suppression actually buys a useful movement opportunity |
| Originality | Familiar individual mechanisms; a promising combination of interactive terrain, vulnerable persistent people and settlement choices | Make manipulating the battlefield a recurring route to success, with a small shared vocabulary |
| Fast play | Bounded activations and small pools help; reaction eligibility, conditions and lookup still carry substantial load | Resolve timing once, reduce overlapping skills, present only fielded rules |
| Bloody battles | Attacks can disable quickly, especially automatic weapons; death is deliberately deferred and limited | Establish the desired casualty experience before changing Injury or permanent mortality |
| Low rules overhead | Several good exclusions already exist; breadth and exceptions remain expensive | Demand a concrete recurring decision from every retained rule |

These are qualitative design judgments, not measured scores or playtest results.

**A useful design sentence:** “You win by making an opening, moving through it, and getting your people and prize home.” It gives shooting, fear, machinery, rescue and persistence a common purpose.

## 2. What was audited and what counts as evidence

I read the owning Rule text of **all 82 official rule/catalogue cards and all 193 item cards across 16 folders**, the complete index, workspace instructions, assembled-rulebook structure, current four-part battle reference and the explicitly unadopted reaction-chain note. I also inspected the 18 deferred objective/scenario records to identify dependencies; they were not treated as active rules. Appendix A accounts for every official card. Appendix B accounts for every item category.

The snapshot contains 22,781 whitespace-delimited words under official card Rule text and 9,653 under item Rule text. **Do not add those figures as unique rules prose:** generated catalogue tables repeat item-owned text and contain long links. Nor are 275 owners equivalent to 275 distinct mechanics. Consolidation has reduced document fragmentation; it has not automatically reduced the number of decisions or exceptions players must administer.

The official-card metadata currently reads **79 Drafted, 2 Partial, 1 Confirmed**. That describes authoring/review state, not validation. The two Partial catalogue owners roll up unresolved area-weapon entries. The current contract verified in the cards is:

- Ordinary tests: d20 + stat + modifiers − Stress, **13+**; normal natural 1/20 rules.
- Injury: d20 + Damage − Armour + applicable Injury modifiers, **15+**, without Stress.
- All human fighters: **one Wound maximum**, including veterans.
- Whole-fighter alternating activation, one Move and one Core in either order; bounded reactions.
- Credits purchase and value the fielded roster; current suggested starting battle limit **750 Credits**.
- Scenario specifics remain Ross’s responsibility. Confirmed objective circles do not supply complete scoring procedures.

The older d10/7+, 15+ ordinary tests, multi-Wound advancement, old rank prices and historical simulation results do not govern this audit. Relevant owners: [[Settlements/Rules System/Second Draft/Rule Cards/V2-015 - Reading a fighter profile|V2-015 - Reading a fighter profile]], [[Settlements/Rules System/Second Draft/Rule Cards/V2-017 - Ordinary tests and modifiers|V2-017 - Ordinary tests and modifiers]], [[Settlements/Rules System/Second Draft/Rule Cards/V2-025 - Credits and Crew Rating|V2-025 - Credits and Crew Rating]], [[Settlements/Rules System/Second Draft/Rule Cards/V2-055 - Activations, action costs and attack limit|V2-055 - Activations, action costs and attack limit]], [[Settlements/Rules System/Second Draft/Rule Cards/V2-114 - Injury and attack outcomes|V2-114 - Injury and attack outcomes]], [[Settlements/Rules System/Second Draft/Rule Cards/V2-392 - Advancement and retraining|V2-392 - Advancement and retraining]], [[Settlements/Rules System/Second Draft/Rule Cards/V2-454 - Objective limits and control areas|V2-454 - Objective limits and control areas]].

Evidence is separated throughout:

| Label | Meaning |
| --- | --- |
| **Observed rule** | Directly present in a current owning card |
| **Derived result** | Arithmetic or a worked rules interaction using stated assumptions |
| **Design risk** | A plausible consequence requiring observation at the table |
| **Proposal** | An unadopted change or experiment |
| **Precedent** | A verified published example, not permission to import its rules |

Fresh external checks used official Infinity rules, publisher material for Spectre and BLKOUT, and Army movement/suppression references. Local research notes supplied historical context; their older “our rules” comparisons were not accepted as current facts. This was not a fresh cover-to-cover read of every commercial source book, an exhaustive originality search, or a new battle simulation.

## 3. Realism: reward believable decisions with simple consequences

### 3.1 What is already working

**Human vulnerability is well protected.** Veteran experience adds capability without extra Wounds or extra normal activations. Damage resolves without a separate armour save, so one successful Injury matters. Injury ignoring Stress avoids the odd implication that a frightened attacker’s bullets hit less hard. Keep these choices. [[Settlements/Rules System/Second Draft/Rule Cards/V2-029 - Recruitment and training grades|V2-029 - Recruitment and training grades]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-055 - Activations, action costs and attack limit|V2-055 - Activations, action costs and attack limit]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-114 - Injury and attack outcomes|V2-114 - Injury and attack outcomes]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-392 - Advancement and retraining|V2-392 - Advancement and retraining]]

**Position changes the available actions.** Opaque terrain blocks shots outright; elevation changes actual sight instead of awarding a generic bonus. Carrying occupies a hand and slows movement. Wounded people, extraction and door controls compete with shooting for the same scarce Core. These are useful abstractions because they create physical tradeoffs without detailed weight or anatomy tables. [[Settlements/Rules System/Second Draft/Rule Cards/V2-049 - Cover and elevation|V2-049 - Cover and elevation]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-074 - Facing, visibility and rear attacks|V2-074 - Facing, visibility and rear attacks]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-090 - Carrying and releasing loads|V2-090 - Carrying and releasing loads]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-134 - Securing, rescuing and extracting captives|V2-134 - Securing, rescuing and extracting captives]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-162 - Interact and stat examples|V2-162 - Interact and stat examples]]

**Support has a purpose beyond adding accuracy.** Smoke changes sight, terrain changes routes, READY threatens interruption, and Rally restores agency. Army doctrine treats suppression as a way to reduce enemy interference so another element can act; movement guidance also distinguishes speed from caution. That supports testing whether these decisions work together, rather than equating realism with a higher casualty percentage. [Army breaching fundamentals](https://www.benning.army.mil/Infantry/DoctrineSupplement/ATP3-21.8/appendix_h/ObstacleReduction/BreachingFundamentals/index.html), [TC 3-21.75, Chapter 7](https://rdl.train.army.mil/catalog-ws/view/100.ATSC/C6763F0D-4346-4DA6-BC8C-4EBFF5B34997-1377112048566/tc_3-21x75.pdf).

Compress the waiting, searching and administration around a clash. Let an exposed clash resolve sharply. Realism does not require every battle to be an uninterrupted charge into gunfire.

### 3.2 Highest-priority mismatch: moving through watched ground

**Observed rule:** Reaction Shoot checks only an action’s start or end, never an intermediate movement point. Other reactions can retain intermediate windows. [[Settlements/Rules System/Second Draft/Rule Cards/V2-065 - Reactions and interruption|V2-065 - Reactions and interruption]]

**Worked interaction:** A READY rifleman watches a road. An enemy begins behind one solid building, crosses the visible road, and ends behind another within its legal Move. Neither endpoint is in LOS. The rifleman cannot Reaction Shoot despite seeing the road crossing represented by that movement. This is a direct consequence of the text, not a claim that every approach is safe.

**Why it matters:** Crossing the actual dangerous space can become safer than stopping just inside it. Smoke, supporting fire and route changes lose some of their value. Run and Gun compounds the question by permitting a shot from partway along a route: its relationship to Reaction Shoot endpoints and the incoming Return Fire window needs explicit treatment. [[Settlements/Rules System/Second Draft/Item Cards/Skill Cards/V2-320 - Run and Gun|V2-320 - Run and Gun]]

**Recommendation:** First test one declared, legal exposure point along a movement route, keeping the existing one-reactor and one-reaction limits. Proposal P1 below defines a bounded version. Do not add an area overwatch template or another readiness state.

### 3.3 Suppression needs to create an opening, not merely a marker

**Observed rule:** Hits either Down or Pin; failed Injury also adds Stress. Pinned loses READY and voluntary attacks. A fighter can later spend Move to stand automatically, retaining an unused Core to shoot. End Phase Break at 2+ Stress may clear all Stress on success, or cause a morale condition on failure. [[Settlements/Rules System/Second Draft/Rule Cards/V2-114 - Injury and attack outcomes|V2-114 - Injury and attack outcomes]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-117 - Pinned and recovery|V2-117 - Pinned and recovery]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-139 - Stress, Break and forced flight|V2-139 - Stress, Break and forced flight]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-150 - Rally|V2-150 - Rally]]

This is already meaningful suppression: lost movement, lost readiness, impaired accuracy, possible morale failure and a change in the target’s visibility. **It is not an automatic immediate stand-up loop.** The owner chooses activation timing; prone LOS, unused enemy reactions and remaining friendly activations matter. Standing itself creates an action window.

The risk is subtler: a target that has not activated may stand and shoot before the suppressing player can exploit the loss of movement. A target already activated may instead remain neutralised for the rest of the round. The same hit therefore buys different opportunities according to sequence. That may be good tactical play, but it needs a deliberate test.

Measure “did the hit enable a teammate to cross, work or extract?” before imposing an extra recovery cost. Taking away the target’s Core as well would be a substantial loss of agency and could create prolonged inactivity.

True attack misses have no suppressive effect. Some near misses are already abstracted into hits with failed Injury; the concern is whether the resulting distribution feels right. Avoid adding Stress for every shot on top of current outcomes.

### 3.4 Awareness is useful but unusually exact

Forward 180-degree LOS rewards flanks and makes facing legible. It also means a nearby shot from just behind a dividing line cannot provoke an ordinary reaction, while sight on the boundary counts as front. Public Hidden positions simplify play but give players information their fighters fictionally lack. [[Settlements/Rules System/Second Draft/Rule Cards/V2-074 - Facing, visibility and rear attacks|V2-074 - Facing, visibility and rear attacks]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-154 - Hidden and Observe|V2-154 - Hidden and Observe]]

Keep these playable conventions initially. Distinguish **surprise** from literal blindness in the explanation. Do not add separate hearing radii, alert levels and visual/thermal awareness tracks. Test close rear approaches and physical screening by friendly bodies; change arcs only if those cases repeatedly feel implausible or dominate positioning.

Quiet and Ghost preserve Hidden after certain shots. They should represent difficulty locating a concealed firing position, not silent or consequence-free gunfire. Existing proximity/exposure reveals must remain visible on the reference. [[Settlements/Rules System/Second Draft/Item Cards/Weapon Characteristic Cards/V2-240 - Quiet|V2-240 - Quiet]] [[Settlements/Rules System/Second Draft/Item Cards/Skill Cards/V2-326 - Ghost|V2-326 - Ghost]]

### 3.5 Cover, armour, range and weapons favour playability

Light and heavy cover give −1/−2 to hit; armour ordinarily reduces Injury chance by five percentage points per point. At close tabletop distances the flat maximum-range rule avoids repeated range-band arithmetic. Those are defensible abstractions, but masonry and protective clothing are not physically interchangeable with a modest accuracy or Injury adjustment. A visibly protective wall must actually block LOS where appropriate. [[Settlements/Rules System/Second Draft/Rule Cards/V2-049 - Cover and elevation|V2-049 - Cover and elevation]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-097 - Shooting and target allocation|V2-097 - Shooting and target allocation]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-494 - Armour and shields|V2-494 - Armour and shields]]

Do not solve this by adding penetration by material, weapon calibre, armour location and ricochet tables. Start with clear scenery declarations: what can be seen, what blocks the shot, and what merely obscures it. The two cover modifiers cannot carry the whole burden of battlefield protection.

The armoury contains cinematic elements: dual firearms can generate multiple attack dice, a magnum has Reload after each firing action, and a suppressed carbine can keep Hidden under stated conditions. Explain Attack Dice as useful fire opportunities and Reload as the weapon’s abstract recovery burden. If those explanations still feel wrong in play, adjust individual profiles. There is no evidence here that the whole armoury needs replacing. [[Settlements/Rules System/Second Draft/Rule Cards/V2-102 - Weapon pools, dual wielding and unarmed attacks|V2-102 - Weapon pools, dual wielding and unarmed attacks]] [[Settlements/Rules System/Second Draft/Item Cards/Weapon Characteristic Cards/V2-243 - Reload|V2-243 - Reload]] [[Settlements/Rules System/Second Draft/Item Cards/Weapon Cards/V2-292 - Magnum|V2-292 - Magnum]] [[Settlements/Rules System/Second Draft/Item Cards/Skill Cards/V2-318 - Gunslinger|V2-318 - Gunslinger]]

### 3.6 Casualty rules are humane campaign protection, not literal trauma modelling

Down fighters can crawl and self-treat; successful treatment restores a battle-capable person, Pinned with Stress 2. A conscious revived finisher avoids a lasting-injury roll. Unconscious fighters cannot die from further battlefield attacks. Casualties and much unclaimed equipment return at battle end; evacuation prevents capture but does not improve the ordinary lasting-injury roll. [[Settlements/Rules System/Second Draft/Rule Cards/V2-122 - Down and Unconscious casualties|V2-122 - Down and Unconscious casualties]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-126 - Treatment and revival|V2-126 - Treatment and revival]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-134 - Securing, rescuing and extracting captives|V2-134 - Securing, rescuing and extracting captives]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-153 - Ending a battle and recovering the crew|V2-153 - Ending a battle and recovering the crew]]

That combination supports attachment and a continuing two-player game. It also creates a broad range of injuries with the same battlefield recovery potential. Treat Down as “unable to continue without help,” rather than claiming every Down is a penetrating gunshot that a medkit reverses.

The present incentives often favour **reviving in place over hauling somebody out**, provided it is tactically safe: revival may restore actions and remove aftermath exposure, while evacuation costs a carrier and still requires the injury roll. This is a design consequence, not proof that rescue is useless; extraction still protects against capture and can satisfy an authored objective.

If medical realism becomes a priority, change the revival/aftermath relationship deliberately. A detailed bleeding or anatomical system would add work at the very point the battle already slows down. My initial recommendation is to retain the bounded one-revival rule and test the decisions it produces before replacing it.

Falls reveal a sharper mismatch: above six inches the AGI test automatically fails, but the consequence is still one Damage 3 Injury roll. Without special modifiers that gives a **45% chance of Down**, whether the fall is just over six inches or much higher. Proposal P4 uses the existing threshold to make a major fall decisive with fewer rolls. [[Settlements/Rules System/Second Draft/Rule Cards/V2-084 - Climbing, jumping and falling|V2-084 - Climbing, jumping and falling]]

## 4. How bloody is it mathematically?

These are exact single-action probabilities, **not battle casualty predictions**. Assumptions: DEX 2, Stress 0, one legal target, no Aim, skills, rear bonus, reaction or interruption; listed weapon pools and traits; initially standing unless stated. The machine gun has not moved. “Down” means disabled in this exchange, not dead.

| Attack and target | At least one hit | Target goes Down | Hit but no Down |
| --- | ---: | ---: | ---: |
| Pistol, open/unarmoured | 50.00% | 17.50% | 32.50% |
| Carbine, open/unarmoured | 50.00% | 20.00% | 30.00% |
| Assault rifle, open/unarmoured | 75.00% | 36.00% | 39.00% |
| Assault rifle, open/light armour | 75.00% | 31.94% | 43.06% |
| Assault rifle, heavy cover/light armour | 64.00% | 26.04% | 37.96% |
| Assault rifle, heavy cover/light armour, already Pinned | 51.00% | 19.90% | 31.10% |
| Shotgun with Brutal, open/unarmoured | 50.00% | 34.88% | 15.13% |
| Machine gun, open/unarmoured | 87.50% | 57.81% | 29.69% |
| Machine gun, heavy cover/light armour | 78.40% | 44.86% | 33.54% |

“Hit but no Down” causes Pinned and the appropriate Stress; for an already Pinned target it leaves that state in place. The machine gun’s Suppression adds Stress in this category, not extra Wounds. Sources: [[Settlements/Rules System/Second Draft/Rule Cards/V2-097 - Shooting and target allocation|V2-097 - Shooting and target allocation]], [[Settlements/Rules System/Second Draft/Rule Cards/V2-114 - Injury and attack outcomes|V2-114 - Injury and attack outcomes]], [[Settlements/Rules System/Second Draft/Item Cards/Weapon Characteristic Cards/V2-237 - Brutal|V2-237 - Brutal]], [[Settlements/Rules System/Second Draft/Item Cards/Weapon Characteristic Cards/V2-242 - Suppression|V2-242 - Suppression]], [[Settlements/Rules System/Second Draft/Rule Cards/V2-486 - Standard weapons|V2-486 - Standard weapons]], [[Settlements/Rules System/Second Draft/Rule Cards/V2-494 - Armour and shields|V2-494 - Armour and shields]].

For identical dice, `P(Down) = 1 − (1 − P(hit) × P(Injury))^dice`. Brutal changes Injury success to `1 − (1 − p)^2`. Natural extremes are included. The reproducible calculation is saved with this audit’s repository evidence.

**Interpretation:** Basic rifles create a substantial chance of disabling a person and a larger combined chance of disrupting them. They do not guarantee a casualty. The stationary machine gun is considerably more dangerous, even against cover. Casualty tempo will depend strongly on access to firing opportunities and recovery, not just the Wound count.

Melee’s pool size matters too. With equal stats/modifiers, three Damage 2 dice against one Damage 1 die produce approximately **43.62% defender Down**, **7.90% attacker Down**, and **5% exchanges with no hits**. These figures enumerate all 160,000 attack-dice combinations and then apply Injury probabilities. They do not include Charge bonuses beyond the stated pool, Pinned, rear attacks or Unanswered. More dice improve both offence and defence through the opposing maximum; an extra melee die is more than a simple extra independent attack. [[Settlements/Rules System/Second Draft/Rule Cards/V2-106 - Melee exchanges, Unanswered and Shove|V2-106 - Melee exchanges, Unanswered and Shove]]

### Disabling, death and persistent loss are separate dials

Eligible unresolved casualties die on lasting-injury results 1–2: **10% per roll**. Four independent eligible casualties would have a **34.39% chance of at least one death**. That is not a per-battle death forecast: the actual number eligible, revival, Subdued exceptions and battle ending all matter. [[Settlements/Rules System/Second Draft/Rule Cards/V2-153 - Ending a battle and recovering the crew|V2-153 - Ending a battle and recovering the crew]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-370 - Lasting injuries, scars and retirement|V2-370 - Lasting injuries, scars and retirement]]

This means a bloody-looking board can coexist with a mostly surviving roster. There is no reason to raise permanent death merely to make the firefight feel decisive. Faster disabling, fewer revival resets and harsher long-term losses are different design decisions with different costs.

If testing shows prolonged ineffective shooting, a single-variable Injury comparison is available: changing Injury from 15+ to 13+ would raise the open/unarmoured assault-rifle example from **36% to 43.75% Down**. **I am not recommending adoption now.** It would affect melee, armour, hazards and the balance between Stress and wounds across the whole game. First repair exposure timing and observe the current baseline.

## 5. Fast play: the main cost is administering exceptions

### 5.1 The core already has useful bounds

Keep whole-fighter activations, Move/Core, the three-die ceiling, one own attack, one reaction per fighter, one reactor per action, no ordinary reaction chains, no extra armour save, and no repeated movement halving. These are strong protections against runaway procedure. [[Settlements/Rules System/Second Draft/Rule Cards/V2-007 - Measuring and shared conventions|V2-007 - Measuring and shared conventions]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-055 - Activations, action costs and attack limit|V2-055 - Activations, action costs and attack limit]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-061 - READY and reaction eligibility|V2-061 - READY and reaction eligibility]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-102 - Weapon pools, dual wielding and unarmed attacks|V2-102 - Weapon pools, dual wielding and unarmed attacks]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-114 - Injury and attack outcomes|V2-114 - Injury and attack outcomes]]

Six rounds do not establish a sixty-minute game. With no casualties or early exit:

| Crew size | Potential fighter activations over six rounds | Potential Move/Core slot uses | Fighter-reaction ceiling over six rounds |
| --- | ---: | ---: | ---: |
| 5 vs 5 | 60 | 120 | 60 |
| 6 vs 6 | 72 | 144 | 72 |
| 10 vs 10 | 120 | 240 | 120 |

These are workload bounds, not expected activity. Both-cost actions combine two slots; incapacitation, conditions, forfeits and unused READY reduce use. Turrets can add reactions within their separate limits. Defensive melee, Orders and End Phase procedures add work outside those columns.

A sixty-minute 10-v-10 game allows only thirty seconds per potential activation before allocating time to setup, End Phases or the settlement. The rules should therefore make a modest crew the normal fast-play entry point. Treat larger crews as a longer format until measured otherwise.

### 5.2 READY is a useful resource with a costly explanation

Players track whether READY is held, whether it was lost or spent, whether a token was spent this round, whether the fighter already Reacted, and whether a replacement is legal. Orders can provide READY after activation. Normal actions usually remove it; Ready itself does not. [[Settlements/Rules System/Second Draft/Rule Cards/V2-061 - READY and reaction eligibility|V2-061 - READY and reaction eligibility]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-485 - Orders|V2-485 - Orders]]

This bookkeeping can be justified by interesting commitment decisions. It should be shown as one consistent physical convention: a readiness marker beside a visible activation/reaction indicator, with spent information on the roster. Avoid scattering several near-identical tokens around the base. Reducing reminders is interface work, not permission to delete separate mechanical facts without testing.

**Orders need clarification:** “leader” may mean recruitment grade or nominated crew role; the current Orders text does not explicitly state the issuer’s Pinned/engaged/morale restrictions. Recipient restrictions are detailed. A free order is not obviously governed by skill-action restrictions. Settle these meanings in the owning procedure before balance conclusions. Do not quietly assign two orders to both interpretations. [[Settlements/Rules System/Second Draft/Rule Cards/V2-034 - Crew composition and item limits|V2-034 - Crew composition and item limits]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-305 - Choosing and using skills|V2-305 - Choosing and using skills]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-485 - Orders|V2-485 - Orders]]

### 5.3 Modifiers are bounded by source, but still need source sorting

The player identifies the largest positive and negative skill modifiers, repeats that for equipment characteristics, then applies position and Stress. Ordinary, opposed and melee pools use different natural-extreme rules. The three-die cap keeps rolling short; it does not remove these distinctions. [[Settlements/Rules System/Second Draft/Rule Cards/V2-017 - Ordinary tests and modifiers|V2-017 - Ordinary tests and modifiers]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-023 - Single opposed tests|V2-023 - Single opposed tests]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-106 - Melee exchanges, Unanswered and Shove|V2-106 - Melee exchanges, Unanswered and Shove]]

First preprint the selected fighter’s common modifiers and show one worked ordinary/melee comparison. Do not introduce a new overall modifier cap or change to task difficulty just to shorten an explanation. If repeated calculation still dominates timed games, compare a replacement stacking rule in isolation; do not layer it on top of the current one.

### 5.4 Morale is the clearest place to remove overlap

The core has Pinned, Stress 0–5 and three morale conditions, with Break and Rally at different times. That is already a substantial account of fear. The NRV catalogue adds several ways to reduce Stress, stand people up or improve a recovery test.

**A concrete redundancy:** Rally Training can test without Stress for up to two friendlies within six inches, including self, clearing all Stress, Pinned and morale on success. Inspire uses a stressed NRV test, removes only up to two Stress from self and one nearby friendly, and clears neither Pinned nor morale. In ordinary eligible use, Rally Training offers the stronger version of the same support purpose. This is an internal comparison, not a numerical skill valuation. [[Settlements/Rules System/Second Draft/Item Cards/Skill Cards/V2-340 - Inspire|V2-340 - Inspire]] [[Settlements/Rules System/Second Draft/Item Cards/Skill Cards/V2-341 - Rally Training|V2-341 - Rally Training]]

Prioritise **merging or replacing Inspire**, rather than inventing another leadership bonus. Review Share the Burden for actual use: its automatic transfer is a real distinction, but moves Stress between records. Hold Fast and On Your Feet attach to ordinary recovery and have clearer physical effects. Preserve distinct support decisions; cut choices whose only value is remembering a worse variant. [[Settlements/Rules System/Second Draft/Item Cards/Skill Cards/V2-343 - Share the Burden|V2-343 - Share the Burden]] [[Settlements/Rules System/Second Draft/Item Cards/Skill Cards/V2-344 - Hold Fast|V2-344 - Hold Fast]] [[Settlements/Rules System/Second Draft/Item Cards/Skill Cards/V2-345 - On Your Feet|V2-345 - On Your Feet]]

If forced-flight route adjudication proves slow, the first simplification candidate is combining Bolting and Bugging Out into one flight procedure. That would remove a behaviour branch but change an explicit fear distinction. Test before recommending the merger as a final rule. No new morale state is needed.

### 5.5 Casualties and devices retain work after being disabled

A Down fighter retains slots, a timer, a revival record and possible capture/loot relevance. An Unconscious body remains an object. Devices have placed/inert/active/concealed/revealed/offline/destroyed distinctions, though not all apply to every device. Drones add an operator, range, flying position and separate command choices. [[Settlements/Rules System/Second Draft/Rule Cards/V2-122 - Down and Unconscious casualties|V2-122 - Down and Unconscious casualties]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-202 - Deploying, revealing, disarming and damaging devices|V2-202 - Deploying, revealing, disarming and damaging devices]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-220 - Utility drone|V2-220 - Utility drone]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-451 - Battle and settlement record sheets|V2-451 - Battle and settlement record sheets]]

These are justified when people actually rescue, steal, reroute and disable. If bodies and devices routinely stay untouched until cleanup, the game is paying for decisions it is not receiving. Record whether each retained marker changes a later choice. Do not equate the existence of a procedure with meaningful play.

## 6. Originality: build around the strongest combination

Reactive d20 combat and simultaneous exchanges already have published precedents. Infinity’s official rules document d20 resolution and opposing reactions, with a different resolution structure and reaction budget. Spectre explicitly uses Stress and suppression. BLKOUT markets fast small-force tactical games. None of those ingredients alone establishes originality. [Infinity rolls](https://infinitythewiki.com/Rolls), [Infinity ARO](https://infinitythewiki.com/ARO:_Automatic_Reaction_Order), [Spectre revised-edition notes](https://www.spectreminiatures.com/blogs/news/spectre-operations-revised-edition), [BLKOUT overview](https://www.blkoutgame.com/pages/the-game).

The promising identity lies in their **specific relationship** here:

1. A hit changes what an ordinary person can safely do.
2. A teammate or a physical machine changes the available route or sightline.
3. That opening permits an objective, rescue or extraction.
4. The aftermath changes which people, equipment and facilities are available next time.

That sequence can feel recognisably Settlements even when each rule is easy to explain.

### Terrain needs tactical value more often than it needs more entries

The current twenty terrain profiles already cover doors, lifts, bridges, movable cover, smoke, light, gas and power. They mostly share a small operation vocabulary. Keep that. A crane moving cargo to screen a lane is more distinctive than another +1 shooting perk. [[Settlements/Rules System/Second Draft/Rule Cards/V2-176 - Shared terrain operations and hazards|V2-176 - Shared terrain operations and hazards]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-496 - Interactive terrain catalogue|V2-496 - Interactive terrain catalogue]]

But mandatory four-feature setup does not guarantee four useful choices. Moving the machine, reaching its control or spending a Core must compare favourably with simply moving or firing. A feature with no effect on a contested route is scenery with administration attached.

For example, a dangerous operation requiring INT 2, followed by an AGI 2 victim’s escape test and a Damage 3 Crush roll, gives **11.25% Down** under ordinary unmodified conditions with a safe displacement available. That is three resolution stages. It may be worthwhile because it moves the victim, closes a route or acts from safety; it is often less attractive as a pure damage action than the rifle examples. Do not raise all hazard damage merely to make cranes popular. Place them where their spatial effect matters. [[Settlements/Rules System/Second Draft/Rule Cards/V2-162 - Interact and stat examples|V2-162 - Interact and stat examples]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-176 - Shared terrain operations and hazards|V2-176 - Shared terrain operations and hazards]]

The best imaginative improvements can therefore be **authored situations using existing rules**: a pallet becomes movable cover and the prize, a shutter changes a contested firing lane, or power to a smoke vent also determines which approach is observable. Scenario scoring remains Ross’s to write. These are candidate scene briefs, not newly adopted objective procedures.

### Preserve plausible technology without a second game

The current drone trades its operator’s Core for one movement or operation. Hacking changes a named linked feature or disables a nearby device; physical controls remain usable. That is a useful near-future constraint: technology changes access, but does not create a free extra fighter. [[Settlements/Rules System/Second Draft/Rule Cards/V2-165 - Hacking, terminals and repair|V2-165 - Hacking, terminals and repair]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-220 - Utility drone|V2-220 - Utility drone]]

Improve the presentation of **who controls what, from where, and what physical counterplay exists**. Avoid adding bandwidth, battery, radio-strength, cyberattack programs or electronic-health tracks. The setting’s 2051 date can support a scenario’s fiction; it is not evidence that every civilian machine must be network-accessible. Declare links and manual alternatives locally.

## 7. Four bounded experiments worth considering

These are alternatives to test separately. They are not a package, and none is claimed to be unprecedented across all games. The measure of success is whether they produce more believable, interesting choices for their cost.

### P1 — Shoot at one declared exposure point

**Priority: highest. Replace the movement-endpoint restriction; add no condition or token.**

Candidate: “Declare the full movement route before moving. One eligible READY reactor may nominate one point on that route where it will have legal LOS and range, before movement is carried out. Resolve its shot when the mover reaches that point, then apply interruption normally. If no legal point is reached, the shot is not made. The action still permits only one reacting model.”

Retain the once-per-round reaction budget and the ordinary prohibition on reaction chains. For a combined Run and Gun, declare its firing point with the route: a reaction before that point can cancel an unfinished shot; at the firing point, use the ordinary simultaneous Return Fire window if the reactor is the target, otherwise resolve the relevant shot after that firing segment. The action still gets one reactor in total. This combined-action timing must be printed and tested with the movement replacement, not improvised by players.

**Expected gain:** watched ground is dangerous during actual exposure, making smoke and suppression useful. **Risk:** defenders gain area control and geometry discussion increases. Test a crossing, a corner, a Charge and Run and Gun before a whole battle. Reject it if it turns every route into a prolonged negotiation.

### P2 — A suppressive burst gives the target a choice

**Priority: exploratory, only if the present suppression test fails. Replace the Suppression trait’s extra-Stress effect; do not add this to it.**

Candidate: A weapon with Suppression may declare a suppressive attack instead of its ordinary damaging attack, using its normal legal target and hit pool. It uses the own-turn attack allowance. On any hit, roll no Injury. The target chooses **become Pinned** or **remain standing and gain 2 Stress**. It loses READY either way. If already Pinned, it stays Pinned; the attack gives no extra benefit. Do not use this as a new reaction mode in the initial test.

**Expected gain:** fewer resolution stages, a visible decision between keeping position and absorbing fear, and an explicit “make an opening” role for a support weapon. **Cost:** this is a new attack choice, reduces actual wounding opportunities and may feel artificial. A player might accept Stress knowing an End Phase test can clear it. The present machine gun already hits frequently, so this experiment may earn no place at all. Keep ordinary shooting as the baseline.

The precise effect combination is a proposal for Settlements, not a claim that suppressive modes or defender choices are new inventions.

### P3 — One contested machine, several useful consequences

**Priority: high as encounter design; no new universal mechanic.**

Give an existing lift, crane or shutter a useful relationship to an objective and two approaches. Use the existing two-state card, printed reach, direct control and terminal links. Example brief: a crane can move a supply pallet into a lane to screen a rescue, or away from that lane to expose the route; both crews can reach a control. Do not let the crane score or extract cargo automatically. Ross supplies the objective’s handling and scoring rules.

**Expected gain:** the battlefield becomes something players manipulate, with decisions about timing, control and exposure. **Cost:** scenario preparation and the risk of an obviously superior control position. Measure whether operating it changes a subsequent choice. This is a better first investment in originality than another catalogue of skills.

### P4 — A major fall ends that fighter’s participation

**Priority: a small realism experiment if vertical hazards feature often. Replace the current over-six-inch outcome.**

Candidate: “A fall over six inches automatically puts a human Down; do not make the AGI or Injury roll. Use the existing accessible/inaccessible casualty placement procedure. Resolve lasting injury normally after battle.”

This reuses a threshold already in the rules and removes a roll. It creates no on-table execution or special death table. **Expected gain:** large falls are decisively dangerous. **Risk:** a 2-inch Shove near a high ledge becomes very strong, so fair terrain access and Unanswered/forced-movement interactions need testing. Do not add distance-by-distance damage bands.

## 8. What to cut, merge, clarify or preserve

| Area | Recommended disposition | Reason |
| --- | --- | --- |
| One Wound, no armour save, Injury without Stress | Preserve | Clear vulnerability without a damage ledger |
| Whole-fighter Move/Core and reaction ceilings | Preserve | Bounded procedure and meaningful sequencing |
| Inspire | First skill merger/replacement candidate | Rally Training largely covers the same support job more effectively |
| Automatic X | Consider showing as a profile label only | It repeats printed Dice; it need not be a separate rule to memorise |
| Bolting/Bugging Out | Conditional merger test | Two forced-route behaviours may cost more adjudication than their difference earns |
| Capture and loot | Preserve core, teach after basic combat | Gives casualties purpose; measure extraction feasibility |
| Custom weapons | Keep optional, out of first-battle preparation | Adds approval, calculation and combination work before the core is proven |
| Twenty terrain profiles | Keep reference breadth; teach shared verbs | Profiles are not twenty separate engines |
| Small settlement discounts | First settlement consolidation candidates | Holding Room changes ransom by 5 Credits; Community Hall saves 5 per Recruit; several worker benefits save tiny amounts |
| No wages/food/water/proficiency/building HP | Preserve exclusions | The core already has enough persistent accounting |
| Reaction-chain variant | Keep separate and unadopted | More replies compete directly with the speed goal; current rules prohibit them |
| New ammunition, fatigue, bleeding, hearing or alert tracks | Do not add for this pass | They multiply state before the existing choices are shown to work |

The settlement’s breadth should earn its place through identity or real choices. A worker on a Salvage Yard adds 5 Credits per cycle against a Recruit body cost of 60; the nominal payback is twelve cycles, ignoring the worker’s other possible uses and constraints. That can make sense for an existing spare person, but is a weak reason to recruit a dedicated worker. Small bonuses are not automatically deep strategy. [[Settlements/Rules System/Second Draft/Item Cards/Training Grade Cards/V2-030 - Recruit grade|V2-030 - Recruit grade]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-406 - Power and workers|V2-406 - Power and workers]] [[Settlements/Rules System/Second Draft/Item Cards/Structure Cards/V2-426 - Salvage Yard|V2-426 - Salvage Yard]]

The broader economy is already more restrained than historical descriptions: both crews get 125 Credits/20 Materials and the winner gets only another 25 Credits. Relief Volunteers and automatic prisoner return help keep a fixed opponent playing. Full-value fielding prevents discounted purchases bypassing the battle cap. These deserve preservation, although a mature settlement’s wider choice remains an advantage that equal Credits cannot completely remove. [[Settlements/Rules System/Second Draft/Rule Cards/V2-025 - Credits and Crew Rating|V2-025 - Credits and Crew Rating]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-042 - Relief Volunteers|V2-042 - Relief Volunteers]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-383 - Post-battle prisoners and release|V2-383 - Post-battle prisoners and release]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-386 - Battle rewards and qualifying battles|V2-386 - Battle rewards and qualifying battles]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-410 - Purchasing, selling and unlocks|V2-410 - Purchasing, selling and unlocks]]

## 9. Concrete readiness and documentation findings

These issues affect evaluation even before choosing new mechanics.

| Finding | Current evidence | Effect and next action |
| --- | --- | --- |
| Area weapons remain incomplete | Frag grenade, fire bottle, grenade launcher, flamethrower and rocket launcher are Partial; profiles do not assign their approved template | Assign weapon-specific templates when Ross decides them. A physical 8-inch flame template also needs a complete placement/targeting procedure; do not invent a default. [[Settlements/Rules System/Second Draft/Rule Cards/V2-002 - Components, models and templates\|V2-002 - Components, models and templates]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-248 - Area attacks, smoke and fire\|V2-248 - Area attacks, smoke and fire]] [[Settlements/Rules System/Second Draft/Item Cards/Equipment Cards/V2-259 - Frag grenade\|V2-259 - Frag grenade]] [[Settlements/Rules System/Second Draft/Item Cards/Equipment Cards/V2-260 - Fire bottle\|V2-260 - Fire bottle]] [[Settlements/Rules System/Second Draft/Item Cards/Weapon Cards/V2-300 - Grenade launcher\|V2-300 - Grenade launcher]] [[Settlements/Rules System/Second Draft/Item Cards/Weapon Cards/V2-301 - Flamethrower\|V2-301 - Flamethrower]] [[Settlements/Rules System/Second Draft/Item Cards/Weapon Cards/V2-302 - Rocket launcher\|V2-302 - Rocket launcher]] |
| Orders issuer and terminology are unresolved | Recipient eligibility is explicit; issuer conditions and grade/role meaning are not equally explicit | Clarify the owning card before playtesting leadership power. [[Settlements/Rules System/Second Draft/Rule Cards/V2-485 - Orders\|V2-485 - Orders]] |
| Active text still directs readers to archived organisation | 18 archive-link occurrences across 17 active owners, including one duplicated in a generated skill catalogue | Redirect live procedure references to live owners in a later editorial pass. These are existing links, not missing-file errors; source/provenance archive links are legitimate and excluded from this count. |
| Unfinished editorial instruction remains inside a rule | Persistent-roster Rule text includes a request to make the passage concise | Finish prose later without treating the embedded request as another game rule. [[Settlements/Rules System/Second Draft/Rule Cards/V2-001 - Persistent crew and settlement\|V2-001 - Persistent crew and settlement]] |
| Component guidance mentions scatter equipment | Core Blast explicitly has no scatter | Reconcile component guidance; do not infer a missing scatter subsystem. [[Settlements/Rules System/Second Draft/Rule Cards/V2-002 - Components, models and templates\|V2-002 - Components, models and templates]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-248 - Area attacks, smoke and fire\|V2-248 - Area attacks, smoke and fire]] |
| Quick reference retains old navigation | Archived master reference and Chapters 18–21 wording remain despite thirteen-chapter assembly | Correct destinations during the editorial pass; keep current owner text authoritative. |
| Claim/Work appear in active skill/deed wording | Actual default Claim/Work procedures are among deferred scenario records | Require the selected authored mission to define those tasks. Do not silently reactivate the retired generator. [[Settlements/Rules System/Second Draft/Item Cards/Skill Cards/V2-339 - Smart\|V2-339 - Smart]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-389 - Experience and deeds\|V2-389 - Experience and deeds]] [[Settlements/Rules System/Second Draft/Rule Cards/V2-454 - Objective limits and control areas\|V2-454 - Objective limits and control areas]] |

In particular, an active instruction to use a deferred mission operation is a **dependency to state**, not authorization to write Ross’s scenario specifics.

## 10. A small test programme that answers the actual questions

Do not begin by changing Injury, recovery, reactions and skills together. The existing simulation code does not implement a validated contract for this exact draft.

### First: settle procedure, without balance changes

Resolve Orders wording and area-profile assignments, or exclude incomplete area weapons from the test roster explicitly. Use a Ross-supplied mission with exact scoring and handling. Rehearse the existing baseline for road crossing, Recover under remaining READY threats, Return Fire, Run and Gun, revival after slot spending, and End Phase fear. Record where the printed text cannot decide the outcome.

### Second: paired baseline and exposure test

Use the same six-person crews, terrain and mission; swap sides and first-player conditions across repeated games. Compare current timing with P1 only. A single pair can reveal procedure problems; it cannot establish balance. Repeat if results are inconsistent. Include an unequal-body-count matchup later, because 5 vs 10 creates activation-timing advantages even at equal Credits; Ross previously removed balancing passes, so do not reintroduce them by default.

Record a short log:

- Battle clock separately from setup and Settlement round; count rulings/lookups and their duration.
- Down events, people still incapacitated at the end, successful revivals, and actual post-battle deaths separately.
- Each useful suppression opening: who crossed, operated or extracted because an enemy was disrupted.
- Recovery followed by a useful Core; whether enemy reactions or LOS made standing a real risk.
- Terrain operations that changed the next decision, and machinery nobody used.
- Rescue/capture attempts and completions; meaningful reaction choices rather than merely available tokens.

Possible **design targets to agree**, not established standards: a familiar six-v-six battle around 45–60 minutes; ordinary decisions resolved from the table/roster without a lookup; fewer than five rule lookups after introductory play; terrain manipulation materially affecting at least a couple of decisions; exposed movement feeling dangerous without making all movement irrational. Do not set a required casualty quota until the mission and preferred tone are clear.

### Third: choose one remaining problem

If firing is still indecisive, test a single lethality adjustment. If fear rarely buys an opening, compare the smallest recovery/suppression replacement, possibly P2. If administration dominates, merge a redundant skill or a forced-flight branch. If terrain is ignored, first change placement and relevance through P3. If major falls look implausible, compare P4.

Stop an experiment when its new ruling burden outweighs its decisions. Keep a dated test contract and record the result as a test, not an adopted ruling. Only then propagate an accepted semantic change through its live owners and reading views.

## Appendix A — Official rule-card coverage

All entries below were inspected as current owners. “Preserve” means retain the design direction for testing, not confirm or lock the card. Catalogue judgments also use the individual item owners.

| Owner | Assessment |
| --- | --- |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-001 - Persistent crew and settlement\|V2-001 - Persistent crew and settlement]] | Finish embedded editorial request; preserve the people/settlement loop. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-002 - Components, models and templates\|V2-002 - Components, models and templates]] | Reconcile component guidance with no-scatter Blast and incomplete template assignments. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-007 - Measuring and shared conventions\|V2-007 - Measuring and shared conventions]] | Preserve shared conventions and reaction ceilings; do not multiply exceptions. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-015 - Reading a fighter profile\|V2-015 - Reading a fighter profile]] | Preserve zero-base stats and one-Wound human ceiling. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-017 - Ordinary tests and modifiers\|V2-017 - Ordinary tests and modifiers]] | Preserve ordinary 13+ and binary tasks; preprint common modifier totals. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-023 - Single opposed tests\|V2-023 - Single opposed tests]] | Preserve; distinguish natural extremes from melee explicitly. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-025 - Credits and Crew Rating\|V2-025 - Credits and Crew Rating]] | Preserve one fielded-value budget; current 750 is a test default. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-029 - Recruitment and training grades\|V2-029 - Recruitment and training grades]] | Preserve capability progression without extra actions or Wounds. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-034 - Crew composition and item limits\|V2-034 - Crew composition and item limits]] | Preserve roster gates; distinguish nominated leader from training grade in Orders. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-037 - Equipping fighters and handling weapons\|V2-037 - Equipping fighters and handling weapons]] | Preserve two hands and capacity costs; keep held-choice timing visible. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-042 - Relief Volunteers\|V2-042 - Relief Volunteers]] | Preserve recovery floor; no evidence supports removing its budget restrictions. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-044 - Setup and deployment\|V2-044 - Setup and deployment]] | Preserve explicit setup; a complete authored mission is still required. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-046 - Battlefield setup and terrain agreement\|V2-046 - Battlefield setup and terrain agreement]] | Preserve route guidance; make mandatory interactive features worth operating. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-049 - Cover and elevation\|V2-049 - Cover and elevation]] | Preserve actual LOS; modest cover modifiers need honest terrain declarations. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-052 - Round refresh and initiative\|V2-052 - Round refresh and initiative]] | Preserve refresh/initiative; assess whether Broken counting earns its upkeep. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-055 - Activations, action costs and attack limit\|V2-055 - Activations, action costs and attack limit]] | Preserve whole-fighter Move/Core, attack limits and no saved slots. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-061 - READY and reaction eligibility\|V2-061 - READY and reaction eligibility]] | Preserve finite READY; simplify physical tracking and eligibility presentation. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-065 - Reactions and interruption\|V2-065 - Reactions and interruption]] | Highest-priority exposure-point experiment; clarify combined-action timing. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-073 - End Phase\|V2-073 - End Phase]] | Preserve one ordered End Phase; measure morale and expiry administration. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-074 - Facing, visibility and rear attacks\|V2-074 - Facing, visibility and rear attacks]] | Preserve playable silhouettes; test exact rear boundary and screening effects. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-078 - Move, obstacles and Dash\|V2-078 - Move, obstacles and Dash]] | Preserve fixed movement and single halving; examine watched-road crossings. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-082 - Charge\|V2-082 - Charge]] | Preserve bounded Charge initially; test randomness, interception and rear routes. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-084 - Climbing, jumping and falling\|V2-084 - Climbing, jumping and falling]] | Compare automatic Down above six inches with the current fall outcome. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-089 - Forced movement\|V2-089 - Forced movement]] | Preserve a shared forced-movement procedure; examine ledge combinations. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-090 - Carrying and releasing loads\|V2-090 - Carrying and releasing loads]] | Preserve one-carrier movement and hand cost; do not restore joint carrying. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-093 - Engagement and Disengage\|V2-093 - Engagement and Disengage]] | Preserve one escape attack; test cost and clarity of Pinned escape. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-097 - Shooting and target allocation\|V2-097 - Shooting and target allocation]] | Preserve lean shooting; evaluate exposure before changing accuracy or Injury. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-099 - Aim\|V2-099 - Aim]] | Test whether spending a whole Core for future Aim earns the delay and marker. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-102 - Weapon pools, dual wielding and unarmed attacks\|V2-102 - Weapon pools, dual wielding and unarmed attacks]] | Preserve three-die ceiling; extra melee dice improve defence as well as offence. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-106 - Melee exchanges, Unanswered and Shove\|V2-106 - Melee exchanges, Unanswered and Shove]] | Preserve distinctive maximum comparison; illustrate natural-20 difference and Unanswered. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-114 - Injury and attack outcomes\|V2-114 - Injury and attack outcomes]] | Preserve Injury without Stress or save; baseline probabilities are now documented. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-117 - Pinned and recovery\|V2-117 - Pinned and recovery]] | Test actual openings from Pinning, chosen recovery timing and remaining reactions. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-122 - Down and Unconscious casualties\|V2-122 - Down and Unconscious casualties]] | Preserve meaningful casualty objects only if rescue/theft decisions occur. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-126 - Treatment and revival\|V2-126 - Treatment and revival]] | Test revival incentive and aftermath exemption; avoid a new bleeding track. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-131 - Loot and item ownership\|V2-131 - Loot and item ownership]] | Preserve explicit item transfers; measure whether taking armour per Core fits tone. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-134 - Securing, rescuing and extracting captives\|V2-134 - Securing, rescuing and extracting captives]] | Preserve bounded capture; test whether extraction competes with easier revival. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-139 - Stress, Break and forced flight\|V2-139 - Stress, Break and forced flight]] | Preserve fear purpose; consider one flight behaviour only if route adjudication drags. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-150 - Rally\|V2-150 - Rally]] | Keep as the main recovery procedure; reduce overlapping skill versions. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-153 - Ending a battle and recovering the crew\|V2-153 - Ending a battle and recovering the crew]] | Preserve humane withdrawal; recognise that automatic recovery softens battlefield loss. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-154 - Hidden and Observe\|V2-154 - Hidden and Observe]] | Preserve public Hidden simplicity; teach reveal triggers and its information abstraction. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-162 - Interact and stat examples\|V2-162 - Interact and stat examples]] | Preserve automatic trivial tasks and one normal test for consequential operations. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-165 - Hacking, terminals and repair\|V2-165 - Hacking, terminals and repair]] | Preserve local links/manual counterplay; avoid a separate cybercombat engine. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-174 - Improvised actions\|V2-174 - Improvised actions]] | Preserve a bounded improvisation fallback; do not prewrite every stunt. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-176 - Shared terrain operations and hazards\|V2-176 - Shared terrain operations and hazards]] | Preserve shared operations; test three-stage dangerous-operation payoff. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-202 - Deploying, revealing, disarming and damaging devices\|V2-202 - Deploying, revealing, disarming and damaging devices]] | Preserve hit-based device damage; simplify fielded state presentation. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-218 - Sentry turret\|V2-218 - Sentry turret]] | Preserve turret action economy; no independent free extra attack. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-220 - Utility drone\|V2-220 - Utility drone]] | Preserve operator-bound drone; measure deployment/move/operate Core burden. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-228 - Equipment profiles and provisional prices\|V2-228 - Equipment profiles and provisional prices]] | Preserve explicit provisional prices; no historic simulation equivalence. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-248 - Area attacks, smoke and fire\|V2-248 - Area attacks, smoke and fire]] | Complete profile assignments and flame procedure; keep no-scatter core. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-270 - Chems and medical supplies\|V2-270 - Chems and medical supplies]] | Preserve chem limit; check if modest benefits justify extra dose/expiry handling. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-271 - Optional custom weapon construction\|V2-271 - Optional custom weapon construction]] | Retain as optional; keep custom building outside first-battle preparation. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-305 - Choosing and using skills\|V2-305 - Choosing and using skills]] | Preserve three-skill cap and action restrictions; prune weak overlaps first. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-354 - Non-killing victory routes\|V2-354 - Non-killing victory routes]] | Preserve non-kill victory; primary/secondary procedures require Ross's mission. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-370 - Lasting injuries, scars and retirement\|V2-370 - Lasting injuries, scars and retirement]] | Preserve one aftermath roll and scar cap; 10% death is a separate tone choice. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-383 - Post-battle prisoners and release\|V2-383 - Post-battle prisoners and release]] | Preserve fixed-opponent prisoner return; captivity is a bounded setback. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-386 - Battle rewards and qualifying battles\|V2-386 - Battle rewards and qualifying battles]] | Preserve small winner premium; current rewards differ from older notes. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-389 - Experience and deeds\|V2-389 - Experience and deeds]] | Preserve non-kill deeds; make mission-specific Claim/Work definitions explicit. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-392 - Advancement and retraining\|V2-392 - Advancement and retraining]] | Preserve flexible growth and repricing; values still need longitudinal tests. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-399 - Founding a settlement\|V2-399 - Founding a settlement]] | Preserve funded entry; repair archived worked-example navigation later. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-401 - Settlement round and availability timing\|V2-401 - Settlement round and availability timing]] | Preserve one cycle per battle; measure settlement management separately. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-406 - Power and workers\|V2-406 - Power and workers]] | Preserve no upkeep/proficiency; small worker benefits need to earn accounting. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-410 - Purchasing, selling and unlocks\|V2-410 - Purchasing, selling and unlocks]] | Preserve full-value fielding and clear ownership; no second battle currency. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-413 - Construction, housing, plots and storage\|V2-413 - Construction, housing, plots and storage]] | Preserve abstract plots and safe capacity rules; avoid a building-placement minigame. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-418 - Medical services and device rebuilding\|V2-418 - Medical services and device rebuilding]] | Preserve bounded services and rebuilds; separate medical fiction from literal trauma. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-422 - Structure catalogue conventions\|V2-422 - Structure catalogue conventions]] | Consolidate marginal discount services if choices do not justify twenty structures. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-443 - Crafting and access\|V2-443 - Crafting and access]] | Keep crafting between battles; consider a prepared price column to reduce rounding. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-448 - Preparations -  Signal Plan and Route Map\|V2-448 - Preparations -  Signal Plan and Route Map]] | Preserve paid limited preparations; assess whether separate unlocks are worthwhile. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-451 - Battle and settlement record sheets\|V2-451 - Battle and settlement record sheets]] | Use a compact roster interface; distinguish required facts from tabletop tokens. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-454 - Objective limits and control areas\|V2-454 - Objective limits and control areas]] | Preserve confirmed circles and six-objective limit; never infer scoring rules. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-485 - Orders\|V2-485 - Orders]] | Clarify issuer conditions and leader/specialist terminology before balancing. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-486 - Standard weapons\|V2-486 - Standard weapons]] | Preserve role variety; three area-weapon item owners remain Partial. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-487 - STR skills\|V2-487 - STR skills]] | Keep physical roles; review Brace and Throw cost/payoff on useful terrain. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-488 - DEX skills\|V2-488 - DEX skills]] | Prioritise Run and Gun timing; keep Split Fire and handling limits explicit. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-489 - AGI skills\|V2-489 - AGI skills]] | Keep bounded movement/stealth roles; test exceptions without adding awareness tracks. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-490 - INT skills\|V2-490 - INT skills]] | Keep distinct technical roles; do not add programs or extra drone actions. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-491 - NRV skills\|V2-491 - NRV skills]] | First catalogue to prune: Inspire overlaps strongly with Rally Training. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-492 - Tools and equipment\|V2-492 - Tools and equipment]] | Keep role-based tools; teach only carried items. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-493 - Consumables and medical supplies\|V2-493 - Consumables and medical supplies]] | Two incomplete area consumables; inspect medical/chem exception burden. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-494 - Armour and shields\|V2-494 - Armour and shields]] | Preserve no-save armour; evaluate small benefits against speed and cost. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-495 - Weapon characteristics\|V2-495 - Weapon characteristics]] | Keep shared traits; Automatic can be a profile label rather than memorised procedure. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-496 - Interactive terrain catalogue\|V2-496 - Interactive terrain catalogue]] | Invest here for identity: useful route, sight and cargo choices over new mechanics. |
| [[Settlements/Rules System/Second Draft/Rule Cards/V2-497 - Deployable equipment catalogue\|V2-497 - Deployable equipment catalogue]] | Preserve shared device operations; measure whether deployment investment pays off. |

## Appendix B — Item-card coverage

| Item category | Owners read | Principal audit result |
| --- | ---: | --- |
| Advancement | 10 | Flexible stat/skill growth, full-value advances and no extra Wounds are good; fixed 10-Credit advances remain provisional |
| Armour | 3 | Simple Injury protection; shield has explicit directional/hands tradeoff; test value rather than add save layers |
| Characteristics | 8 | Five stats plus MOVE/Wounds/Armour are understandable; not eight independently rolled abilities |
| Deployables | 9 | Shared operations are useful; public locations reduce hidden administration; test setup cost and actual use |
| Equipment | 13 | Tools support real jobs; five medical/chem entries add exceptions; frag/fire-bottle procedures are incomplete |
| Experience deeds | 4 | Useful non-kill contribution earns XP; mission task names require a supplied scenario |
| Interactions | 5 | Examples help assign one ordinary test; avoid expanding them into a difficulty catalogue |
| Lasting injury | 10 | One roll/two-scar limit is bounded; permanent death remains 10% of eligible rolls |
| Preparations | 2 | Explicit costs and no extra activations protect the budget; check whether minor advantages earn separate structures |
| Skills | 39 | Several strong physical roles; NRV overlap and Run and Gun timing deserve priority |
| Structures | 20 | Settlement choices are coherent; tiny discounts and worker arithmetic are likely consolidation targets |
| Terrain | 20 | Most promising source of distinct play; learn shared operations and field only useful profiles |
| Training grades | 4 | Capability without extra durability/actions fits; clarify Orders grade/role terminology |
| Weapons | 22 | Small pools, role differences and provisional prices; three area profiles remain incomplete |
| Weapon characteristics | 18 | A compact shared vocabulary; Automatic repeats profile data, several traits add extra handling/rolls |
| Weapon classes | 6 | Optional builder limits are useful guardrails; do not treat designer prices as validated balance |
| **Total** | **193** | **All item Rule text read; no item semantics changed** |

## Appendix C — Sources and reproducibility

Current authority: [[Settlements/START HERE - Settlements Project]], [[Settlements/Rules System/Second Draft/AGENTS]], [[Settlements/Rules System/Second Draft/Rule Cards - Complete Index]], [[Settlements/Rules System/Second Draft/Settlements Rulebook - Assembled]], [[Settlements/Rules System/Second Draft/Draft 2 - Battle Quick Reference]]. Findings link to owning cards throughout this report.

Historical research consulted at relevant sections: [[Settlements/Research/Settlements - Design Requirements and Research Audit]], [[Settlements/Research/Notes/BLKOUT]], [[Settlements/Research/Notes/Infinity]], [[Settlements/Research/Notes/Spectre Operations]]. Their older Settlements comparisons are historical, not current authority. [[Settlements/Rules System/Second Draft/Draft 2 - Reaction Chains - For Testing]] remains expressly unadopted.

Fresh external precedent checks: [Infinity rolls](https://infinitythewiki.com/Rolls), [Infinity reactions](https://infinitythewiki.com/ARO:_Automatic_Reaction_Order), [Spectre’s revised-edition explanation](https://www.spectreminiatures.com/blogs/news/spectre-operations-revised-edition), [BLKOUT’s publisher overview](https://www.blkoutgame.com/pages/the-game). BLKOUT’s advertised duration is a publisher claim, not an independently measured Settlements target. Its current rule download is account-mediated; the saved research note was used for historical context rather than claiming a fresh full-book verification.

Realism lens: [Army suppression/breaching guidance](https://www.benning.army.mil/Infantry/DoctrineSupplement/ATP3-21.8/appendix_h/ObstacleReduction/BreachingFundamentals/index.html) and [TC 3-21.75 movement guidance](https://rdl.train.army.mil/catalog-ws/view/100.ATSC/C6763F0D-4346-4DA6-BC8C-4EBFF5B34997-1377112048566/tc_3-21x75.pdf). Search-indexed passages were accessible; direct fetches of these two Army resources timed out. These are bounded qualitative references, not empirical support for casualty percentages or predictions about 2051 technology.

Repository evidence: `docs/draft2-tenets-audit-2026-10-27/` contains the pre-audit owner snapshot and hashes, extracted reading corpus, exact-probability calculator and results, and final source-preservation/link checks. Hashes document the scope and unchanged source files; they do not prove balance or real-world validity. No historical battle engine was run, and no tabletop or blind-reader acceptance is claimed.
