<!-- settlements-simulation:generated -->
# Balance verdicts — 11 November 2026

**Current recommendation: keep the approved baseline. Smoke has a provisional local pass; several mechanics need targeted confirmation. No game-rule change is justified by the evidence yet. The full balance pass remains unfinished.**

These verdicts answer “does the mechanic appear to work in balance, and should it change?” A conformance test passing only says the code followed its rule. It does not answer that balance question. No equal-Credit or human-play claim is made.

**Priority finding:** Flashbang now has a measured high-impact activation-denial warning. It is not passed. Sustained lockout and capable counterplay are the next decision gate; the one-round signal alone does not justify changing the approved rule.

## Verdict key

- **PROVISIONAL PASS:** Useful intended effect and a demonstrated constraint/counter in the stated scope; keep the baseline there. Not full-game sign-off.

- **NEEDS ADJUSTMENT:** A replicated material problem survives relevant counters and implementation/policy checks; propose a concrete change for Ross. No current game-rule finding reaches this bar.

- **WATCH / CONFIRM:** Material effect or plausible weakness/abuse needs targeted confirmation; keep baseline and prioritize the named test.

- **INSUFFICIENT EVIDENCE:** Cannot judge balance. A correct formula, unused hook or missing policy is not a pass or failure.

- **NOT A BALANCE TEST:** Conformance/provenance/reproduction check only; no power judgment follows.

## Decision list

| Mechanic | Balance verdict | Recommended action |
| --- | --- | --- |
| Smoke grenade and Respirator counter | **PROVISIONAL PASS** | Keep the current rule for the next tests. No balance-driven smoke or Respirator adjustment is indicated in the tested lane task. |
| Flamethrower | **WATCH / CONFIRM** | Keep the baseline. Do not nerf Damage or automatic hits from this one-action result. Prioritize legal approach/counterbuild tests. |
| Blast, Frag grenade and launchers | **INSUFFICIENT EVIDENCE** | Keep the current rules; no adjustment is justified yet. Complete tactical value comparisons before calling these balanced. |
| Flashbang and Stunned | **WATCH / CONFIRM** | High-priority balance concern: do not pass Flashbang yet. Keep the baseline while testing sustained denial, routes and initiative-aware objective crews. Recommend an adjustment if repeated lockout remains efficient after those legal counters and resource costs; this one-round task alone does not justify a nerf. |
| Tear-gas grenade | **WATCH / CONFIRM** | Keep the current rule. Measure recovery/action denial and Respirator/spacing counterplay before a radius or effect adjustment. |
| Molotov and On Fire | **INSUFFICIENT EVIDENCE** | Do not sign off or rebalance the condition yet. Finish spatial consequences and then compare mission impact, rather than judging it by zero Injury. |
| Reinforced armour and its −2 MOVE trade-off | **WATCH / CONFIRM** | Keep Armour 6 / −2 MOVE pending role-specific tests. Investigate whether escort/holding tasks repay the movement cost; do not use obsolete prices to declare it bad value. |
| Rage + Implode | **WATCH / CONFIRM** | Keep the intended combination. Test sustained multi-round benefit and risk against realistic counters before recommending a change. |
| Dual Agile, Parry/shield and defender-selected cancellation | **INSUFFICIENT EVIDENCE** | Keep Ross’s settled mechanics. No cancellation or dual-weapon rule change is indicated by an implementation-oracle pass alone. |
| Shield drone: ignore one hit per attack | **WATCH / CONFIRM** | Keep the profile while prioritizing intended counters. Do not balance it by attacking only the protected target with one-die weapons. |
| Repeated terrain-interaction XP | **WATCH / CONFIRM** | Flag the incentive for campaign-boundary review; do not add a cap yet. Recommend a change only if repeated operation produces a material exploit after action and battle-ending costs. |
| Other measured ordinary weapons and keywords | **INSUFFICIENT EVIDENCE** | Keep the current profiles. Distinct unpriced weapons need useful roles and counters, not identical one-attack damage. |

## Smoke grenade and Respirator counter

**Balance verdict: PROVISIONAL PASS.**

**Why:** It provides a useful, costly crossing tool and has a demonstrated direct counter. In the fixed open lane, survival rose from 56.6% to 89.6%; the watcher’s Respirator removed that benefit. A wall already blocking the shot also removed its marginal benefit.

**Recommended action:** Keep the current rule for the next tests. No balance-driven smoke or Respirator adjustment is indicated in the tested lane task.

**Tested scope / confidence:** 4,000 paired one-round lane tasks: open/blocked line crossed with watcher Respirator absent/present. One Core and consumable, current-End-Phase expiry. This is a local utility/counterplay pass, not whole-game approval. Moderate for this task; low for whole-game balance.

**Next test needed:** Confirm on held-out lanes with different distances, initiative/timing, alternative paths and a competent objective crew before final sign-off.

**Evidence:** [smoke-lane.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/area/smoke-lane.csv>) · [configs.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/area/configs.json>) · [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>)

## Flamethrower

**Balance verdict: WATCH / CONFIRM.**

**Why:** Automatic multi-target damage has a strong clustering payoff. Armour-0 any-Wound frequency was 49.99% against the spaced fixture and 87.81% against the three-target cluster. Spreading and solid walls reduce its reach; approach risk and complete crew counterplay have not been measured.

**Recommended action:** Keep the baseline. Do not nerf Damage or automatic hits from this one-action result. Prioritize legal approach/counterbuild tests.

**Tested scope / confidence:** Eight horizontal flame contexts, Armour 0/2/4/6, cluster/spread; rounded 8 × 1–3 inch authored outline. Oblique placement, device damage and full battle policy are not validated. Strong for the measured effect; insufficient for a global verdict.

**Next test needed:** Test approaching an ALERT ranged crew, lateral spread/alternate objectives, confined routes and Reload-independent action tempo; confirm on held-out boards.

**Evidence:** [micro.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/area/micro.csv>) · [AREA-CONTRACT.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/AREA-CONTRACT.md>)

## Blast, Frag grenade and launchers

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** Scatter, partial footprints, clustering and friendly/self exposure are measured and agree with independent math. That establishes delivery behavior, not whether the complete range/hand/slot/action package is too strong or weak.

**Recommended action:** Keep the current rules; no adjustment is justified yet. Complete tactical value comparisons before calling these balanced.

**Tested scope / confidence:** One fixed-aim attack against fresh targets; Armour 0/2/4/6 and source-specific Injury. Reload/Single-use have focused consumption checks, not complete multi-round value evidence. Limited.

**Next test needed:** Compare single- and multi-target opportunities over multiple activations, including Reload downtime, limited ammunition, operator targeting and alternative objectives.

**Evidence:** [micro.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/area/micro.csv>) · [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>)

## Flashbang and Stunned

**Balance verdict: WATCH / CONFIRM.**

**Why:** The new 12,000-pair task shows high activation-denial impact. With clustered victims and attackers acting first, two Flashbang actions denied 1.686 of two victim activations on average (simultaneous 95% 1.429–1.943), plus 0.740 pending skips. ALERT counterfire reduced observed immediate denial to 1.200 and Downed 0.491 of two throwers on average. With victims acting first, immediate denial fell to 0.719 but 1.724 skips remained pending. Acting first delays some harm rather than cancelling it. Solid walls stopped this fixed-position delivery opportunity.

**Recommended action:** High-priority balance concern: do not pass Flashbang yet. Keep the baseline while testing sustained denial, routes and initiative-aware objective crews. Recommend an adjustment if repeated lockout remains efficient after those legal counters and resource costs; this one-round task alone does not justify a nerf.

**Tested scope / confidence:** 12 cells × 1,000 paired seeds: two mechanically legal four-member crews, whole-unit alternating activations, clustered/spread victims, attacker/defender first, unready/ALERT/solid-wall counters. Same gear in both arms; control uses Aim. Task ends before End Phase; pending skips are not counted as already-lost future turns. Strong conditional control signal; final adjustment decision pending multi-round counterplay.

**Next test needed:** Confirm over multiple rounds with legal grenade quantities, End-Phase morale/flight, movement/alternate objectives and competent attacker/defender policies. Measure work denied per Core/item and practical escape opportunities; then decide whether footprint, targeting or duration needs a proposed change.

**Evidence:** [micro.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/area/micro.csv>) · [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>) · [paired-summary.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v5/flash-denial/paired-summary.csv>) · [configs.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v5/flash-denial/configs.json>) · [seed-pairs.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v5/flash-denial/seed-pairs.csv>)

## Tear-gas grenade

**Balance verdict: WATCH / CONFIRM.**

**Why:** The printed 5-inch radius gives broad Pinning coverage, including friendly exposure. Respirator blocks the effect in fixtures. Objective denial, recovery costs and whether this radius is oppressive remain unmeasured.

**Recommended action:** Keep the current rule. Measure recovery/action denial and Respirator/spacing counterplay before a radius or effect adjustment.

**Tested scope / confidence:** Three open one-action layouts and gas-protection fixtures; no Injury or invented hit Stress is applied. Limited.

**Next test needed:** Run timed objective contests with recovery, movement, legal slot costs and protected/unprotected opponents; include friendly exposure and repeated use.

**Evidence:** [micro.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/area/micro.csv>) · [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>)

## Molotov and On Fire

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** Initial displacement, water extinguishing and escalating condition states have tests. A multi-round balance judgment would be unreliable while ledges/falls, collisions, cure access and crew opportunity costs remain incomplete.

**Recommended action:** Do not sign off or rebalance the condition yet. Finish spatial consequences and then compare mission impact, rather than judging it by zero Injury.

**Tested scope / confidence:** Open placement/affected sets, central-ground fire movement and condition timing; no complete dynamic fire/casualty integration. Limited.

**Next test needed:** Measure activation loss, displacement, water access and casualty outcomes on several boards, including safe and dangerous elevation changes.

**Evidence:** [micro.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/area/micro.csv>) · [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>) · [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/clause-fixtures/assertions.csv>)

## Reinforced armour and its −2 MOVE trade-off

**Balance verdict: WATCH / CONFIRM.**

**Why:** The initial subset screen showed severe losses in some mobility-sensitive fixtures (14.25% and 17% match score). Improved held-out control-policy scores were 36.875%, 45.375% and 48.25%, with wide intervals. The extreme initial losses were not broadly confirmed; a universal armour buff is not supported.

**Recommended action:** Keep Armour 6 / −2 MOVE pending role-specific tests. Investigate whether escort/holding tasks repay the movement cost; do not use obsolete prices to declare it bad value.

**Tested scope / confidence:** Reinforced-for-Light substitution on one controlled leader, v2 ground objective fixtures and limited held-out policy confirmation. These are not equal-Credit rosters. Repeated conditional warning; insufficient for a universal change.

**Next test needed:** Run paired stationary defence/escort versus travel-heavy missions, improve slow-actor objective policy, and confirm against different damage/control counters.

**Evidence:** [battle-matrix.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battle-matrix.csv>) · [matrix.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/matrix.csv>)

## Rage + Implode

**Balance verdict: WATCH / CONFIRM.**

**Why:** Fresh-seed checks increased mean Injury successes by 0.041–0.050 per exchange, but increased retained attacker Stress by 1.167 and attacker Down frequency by 3.8 percentage points in the sampled Riposte contexts. This does not demonstrate an unavoidable dominant combo or a need to nerf an intended interaction.

**Recommended action:** Keep the intended combination. Test sustained multi-round benefit and risk against realistic counters before recommending a change.

**Tested scope / confidence:** Two 1,000-pair conditional initiating-exchange confirmations at initial Stress 4, Standard/Reinforced armour; target may Riposte. No movement or full crew integration. Limited.

**Next test needed:** Test gaining/clearing Stress, attacking alternative defenders, support auras and mission pressure with legal progression/build histories.

**Evidence:** [fixed-confirmation.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/fixed-confirmation.csv>) · [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

## Dual Agile, Parry/shield and defender-selected cancellation

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** The success/cancellation math and conditional attack/defence differences are verified. Powerful defence and asymmetric initiating pools alone do not establish oppression; movement, alternate targets and objective counterplay are incomplete.

**Recommended action:** Keep Ross’s settled mechanics. No cancellation or dual-weapon rule change is indicated by an implementation-oracle pass alone.

**Tested scope / confidence:** Exact pool distributions, mixed-weapon Monte Carlo and selected paired melee exchanges. Complete legal crew counterbuilds have not run. Limited.

**Next test needed:** Compare initiation choices, disengagement, ranged pressure, multiple objectives and competent counterbuilds on held-out boards.

**Evidence:** [mixed-cancellation.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/decision-validation/mixed-cancellation.csv>) · [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>) · [melee-pool-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/melee-pool-atlas.csv>)

## Shield drone: ignore one hit per attack

**Balance verdict: WATCH / CONFIRM.**

**Why:** Ignoring one hit completely stops a one-die attack against the drone. Multi-die attacks retain possible hits, but operator attacks, disabling, flanks and objectives are not adequately measured. This is a concentrated matchup concern, not demonstrated whole-game dominance.

**Recommended action:** Keep the profile while prioritizing intended counters. Do not balance it by attacking only the protected target with one-die weapons.

**Tested scope / confidence:** Conditional hit-ignore atlas and fixtures; full shield geometry/device uptime/counterplay remain incomplete. Limited.

**Next test needed:** Compare multi-die fire, operator attack, disable/hack, flanking and objective bypass against a competent shield crew.

**Evidence:** [shield-drone-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/shield-drone-atlas.csv>) · [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>)

## Repeated terrain-interaction XP

**Balance verdict: WATCH / CONFIRM.**

**Why:** Repeated successful door interactions each create an XP opportunity under current text. This is a potential farming incentive. The test does not show an infinite action loop or prove that farming beats mission/reward play.

**Recommended action:** Flag the incentive for campaign-boundary review; do not add a cap yet. Recommend a change only if repeated operation produces a material exploit after action and battle-ending costs.

**Tested scope / confidence:** Two successful door operations; reward/campaign incentives not fully integrated. Limited.

**Next test needed:** Compare interaction farming with objectives/withdrawal over bounded battle rounds and legal extra-action support.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/clause-fixtures/assertions.csv>)

## Other measured ordinary weapons and keywords

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** Conditional per-action math agrees with the independent oracle. No full weapon balance pass follows while range, action economy, relevant roles and equal-policy counterbuilds are incomplete.

**Recommended action:** Keep the current profiles. Distinct unpriced weapons need useful roles and counters, not identical one-attack damage.

**Tested scope / confidence:** 19 weapon micro contexts and conditional atlas; selected unpriced substitutions in ground battles. Limited.

**Next test needed:** Complete intended-use and unfavourable tactical roles, legal combinations and capable crew comparisons before sign-off.

**Evidence:** [combat-micro.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/combat-micro.csv>) · [battle-matrix.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battle-matrix.csv>)

## Owner coverage and limits

All 248 active owners have an explicit balance disposition in [the owner verdict table](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/assessments-2026-11-11-v1/owner-verdicts.csv>). No owner is claimed to have completed the entire balance ladder.

A WATCH verdict is not an approved nerf/buff. An INSUFFICIENT verdict is not a declaration that the rule is weak. No new prices have been calculated. Review the listed strongest effects and their counters before a later trait-based Credits rebuild.
<!-- /settlements-simulation:generated -->

## Additional notes

