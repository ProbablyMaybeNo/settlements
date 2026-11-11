<!-- settlements-simulation:generated -->
# Settlements simulation checklist

Updated **2026-11-11** from recorded evidence in **v4**, with the earlier ground-battle batches retained under **v2**.

**The full simulation plan is unfinished. Pricing readiness is not established.**

Use this page to follow the work in plan order. Every entry has recorded results, findings and notes. Checked means the **named subtask ran**, not that a whole mechanic is balanced. An unchecked **Partial** entry has some evidence but still needs the stated work. **Not run** means the required evidence has not been produced. Nothing is marked as running without an active recorded run.

[Original simulation plan](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/docs/balance-pass-2026-11-10/PLAN.md>) · [Current execution review](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/EXECUTION-REVIEW.md>) · [[Settlements/Simulations/Tracking/Rule and Item Coverage|Every rule, skill and item]] · [[Settlements/Simulations/Results/Simulation Results Log|Detailed results log]]

**Balance decision:** [[Settlements/Simulations/Analysis/Balance Verdicts|Read the balance verdicts first]]. Smoke has a provisional local pass; several mechanics need targeted confirmation. No game-rule change is currently justified. “Executed” is a work-status checkbox, not a balance pass.

**Current recorded totals:** 88 primary checks; 28 additional clause checks; 190,000 single-attack weapon trials; 480,000 mixed-weapon trials; 9,000 tactical screening pairs plus 2,000 confirmation pairs; 12,000 exploratory and 2,400 held-out ground-subset battles; 96 old/new engine comparisons.

**Area addition:** 600,000 trials in 60 contexts; 4,000 paired watched-lane tasks. Earlier evidence retains its producing v2/v3 manifests.

**Flashbang balance follow-up (v5 task supplement):** 12,000 paired first-cycle objective tasks across 12 timing/spacing/counter contexts. Verdict: **Watch / confirm — high-priority control concern; not passed.**

The 248 source owners include catalogue pages and definitions: they are **not 248 independent mechanics**. Zero tagged events does not prove that an option is weak or that its effect never appeared indirectly. No overall completion percentage is inferred from those counts.

**Scope:** no approved vault content or prices have been changed. All battle scenarios here are simulation fixtures; crews are mechanically controlled but their deferred Credit costs are unverified. No human play or complete campaign balance has been validated.

**Updating:** rerun `py -3.13 docs/balance-pass-2026-11-10/build_simulation_checklist.py --obsidian` after publishing a new evidence checkpoint. Ross’s notes inside the labelled comment blocks are preserved, with live Obsidian annotations taking precedence. This command refreshes documentation and the authorized simulation notes; it runs no simulations.

## 1. Sources, contract and engine foundation — plan §§1–3

<a id="F01"></a>

### F01 — Verify and freeze the current approved owners

- [x] **Executed** — Verify and freeze the current approved owners

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** All 248 owner files matched the prepared snapshot; inventory and extracted blocks were checked.

**Findings:** The recorded batches have a named source version.

**Notes / remaining work:** Recheck hashes before a new rule revision; preserve prior snapshots.

**Evidence:** [source-manifest.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/source-manifest.json>) · [source-snapshot.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/source-snapshot.json>)

**Ross’s notes:**

<!-- ross-notes:F01 -->

<!-- /ross-notes -->

<a id="F02"></a>

### F02 — Audit historical engines before reuse

- [x] **Executed** — Audit historical engines before reuse

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** TN10/TN15/d10 engines were audited; the current adapter is isolated.

**Findings:** Historical tests and prices do not validate the current rules.

**Notes / remaining work:** Historical engines and runs remain preserved.

**Evidence:** [ENGINE-REUSE-AUDIT.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/ENGINE-REUSE-AUDIT.md>)

**Ross’s notes:**

<!-- ross-notes:F02 -->

<!-- /ross-notes -->

<a id="F03"></a>

### F03 — Document the complete simulation contract

- [ ] **Partial** — Document the complete simulation contract

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Current core procedures, anchors, examples and abstractions are documented.

**Findings:** The contract separates approved rules from geometry/policy approximations.

**Notes / remaining work:** Complete conformance for all tech, terrain, timing and resources remains outstanding.

**Evidence:** [RULES-CONTRACT.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/RULES-CONTRACT.md>) · [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:F03 -->

<!-- /ross-notes -->

<a id="F04"></a>

### F04 — Resolve mixed-weapon cancellation ownership

- [x] **Executed** — Resolve mixed-weapon cancellation ownership

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Ross ruled: defender chooses attacker dice to cancel within normal/critical groups. Recorded in v3.

**Findings:** Mixed pools retain weapon identity; defender choice now has targeted checks.

**Notes / remaining work:** Default policy minimizes expected Injury; positional cancellation priorities need separate policy tests.

**Evidence:** [decision-addendum.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/decision-addendum.json>) · [mixed-summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/decision-validation/mixed-summary.json>)

**Ross’s notes:**

<!-- ross-notes:F04 -->

<!-- /ross-notes -->

<a id="F05"></a>

### F05 — Run primary deterministic and independent-oracle checks

- [x] **Executed** — Run primary deterministic and independent-oracle checks

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 88 named checks passed; every check is listed in the results log.

**Findings:** Covered clauses agree with their hand-worked/exact expectations.

**Notes / remaining work:** This is clause conformance, not certification of every owning rule.

**Evidence:** [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>) · [[Settlements/Simulations/Results/Simulation Results Log|SIMULATION-RESULTS-LOG.md]]

**Ross’s notes:**

<!-- ross-notes:F05 -->

<!-- /ross-notes -->

<a id="F06"></a>

### F06 — Run additional owner-clause fixtures

- [x] **Executed** — Run additional owner-clause fixtures

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 28 additional fixtures passed, including support, auras, chems, deployment assignment and condition timing.

**Findings:** Selected transitions work in their explicit fixtures.

**Notes / remaining work:** Some probes are analytical; deployment-only checks do not certify full device abilities.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/clause-fixtures/assertions.csv>)

**Ross’s notes:**

<!-- ross-notes:F06 -->

<!-- /ross-notes -->

<a id="F07"></a>

### F07 — Preserve implementation failures and regression seeds

- [x] **Executed** — Preserve implementation failures and regression seeds

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Engagement, flight-route and Charge-route failures were retained, corrected and regression-tested.

**Findings:** These were engine/policy defects, not balance findings.

**Notes / remaining work:** Superseded pilots and v1 are excluded from the interpreted battle total.

**Evidence:** [failing-engagement-replay.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/pilot/failing-engagement-replay.json>) · [failing-flight-replay.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/pilot/failing-flight-replay.json>) · [failing-charge-replay.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v1/failing-charge-replay.json>)

**Ross’s notes:**

<!-- ross-notes:F07 -->

<!-- /ross-notes -->

<a id="F08"></a>

### F08 — Establish complete action/event replay reconstruction

- [ ] **Partial** — Establish complete action/event replay reconstruction

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Seed reproduction passes; v3 adds a final checkpoint including secondary VP.

**Findings:** The earlier v2 outcome totals were correct; the last displayed checkpoint omitted the secondary award.

**Notes / remaining work:** Complete action-by-action event reconstruction is not established.

**Evidence:** [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>) · [replay-checkpoint-audit.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/replay-checkpoint-audit.json>) · [replay-review.html](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/replay-review.html>)

**Ross’s notes:**

<!-- ross-notes:F08 -->

<!-- /ross-notes -->

## 2. CORE — dice, Stats and thresholds

<a id="C01"></a>

### C01 — Generate exact ordinary, Injury and opposed probability tables

- [x] **Executed** — Generate exact ordinary, Injury and opposed probability tables

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 72,840 weapon contexts; 56 Stat/Stress rows; 441 opposed rows.

**Findings:** Ordinary and opposed tests use different resolution procedures; natural extremes are preserved.

**Notes / remaining work:** Raw Stat accuracy is measured separately from the utility of its skill unlock.

**Evidence:** [probability-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/probability-atlas.csv>) · [stat-threshold-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/stat-threshold-atlas.csv>) · [opposed-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/opposed-atlas.csv>)

**Ross’s notes:**

<!-- ross-notes:C01 -->

<!-- /ross-notes -->

<a id="C02"></a>

### C02 — Cross-check large melee pools with an independent oracle

- [x] **Executed** — Cross-check large melee pools with an independent oracle

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Dynamic-programming distributions agree with small-pool brute force and named fixtures.

**Findings:** Normal successes cancel normal; criticals cancel only criticals; defender surplus causes no hits.

**Notes / remaining work:** This does not measure every mixed keyword or tactical circumstance.

**Evidence:** [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>) · [melee-pool-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/melee-pool-atlas.csv>)

**Ross’s notes:**

<!-- ross-notes:C02 -->

<!-- /ross-notes -->

<a id="C03"></a>

### C03 — Measure each Stat step including its skill unlock

- [ ] **Partial** — Measure each Stat step including its skill unlock

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Raw threshold tables and selected unlock/promotion fixtures exist.

**Findings:** A raw accuracy increment is not the full value of an associated skill.

**Notes / remaining work:** Complete INT/AGI/STR/NRV task utility, skill-choice effects and crew-level comparisons remain.

**Evidence:** [stat-threshold-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/stat-threshold-atlas.csv>) · [skill-scorecards.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/skill-scorecards.csv>)

**Ross’s notes:**

<!-- ross-notes:C03 -->

<!-- /ross-notes -->

<a id="C04"></a>

### C04 — Measure all legal maximum modifier and pool combinations

- [ ] **Partial** — Measure all legal maximum modifier and pool combinations

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Category caps, Stress exemptions, pool additions, Parry/shield and selected bonuses are checked.

**Findings:** Pool additions must not be mistaken for roll-total modifiers.

**Notes / remaining work:** Every exceptional skill, equipment stack and advanced boundary still needs complete coverage.

**Evidence:** [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>) · [legal-high-risk-builds.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/legal-high-risk-builds.csv>)

**Ross’s notes:**

<!-- ross-notes:C04 -->

<!-- /ross-notes -->

## 3. RANGED and MELEE — weapons and defence

<a id="W01"></a>

### W01 — Run conditional single-attack Monte Carlo across ordinary weapons

- [x] **Executed** — Run conditional single-attack Monte Carlo across ordinary weapons

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 19 weapons × 10,000 trials = 190,000 trials, with no declared oracle-check failures.

**Findings:** Recorded hit/Wound rates match the independent expectations within the declared check tolerance.

**Notes / remaining work:** Fresh-target, analytical combat probes exclude range, movement, Reload downtime and whole-crew value.

**Evidence:** [combat-micro.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/combat-micro.csv>) · [combat-micro-summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/combat-micro-summary.json>)

**Ross’s notes:**

<!-- ross-notes:W01 -->

<!-- /ross-notes -->

<a id="W02"></a>

### W02 — Complete all 22 weapon profiles and all 21 keywords

- [ ] **Partial** — Complete all 22 weapon profiles and all 21 keywords

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** All 22 weapons have conditional atlas entries; 19 ordinary weapons have single-attack Monte Carlo. The three area weapons now have declared v4 geometry/micro contexts.

**Findings:** Direct conditional combat evidence does not establish range, downtime, full keyword interactions or crew value.

**Notes / remaining work:** Complete oblique Blast/cone/device cases, multi-round range, Retrieve, Reach, casualties, consumption and keyword combinations; see every profile below.

**Evidence:** [[Settlements/Simulations/Tracking/Rule and Item Coverage|SIMULATION-OWNER-CHECKLIST.md]] · [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:W02 -->

<!-- /ross-notes -->

<a id="W03"></a>

### W03 — Measure defender-selected mixed-weapon cancellation

- [x] **Executed** — Measure defender-selected mixed-weapon cancellation

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** The success/cancellation math and conditional attack/defence differences are verified. Powerful defence and asymmetric initiating pools alone do not establish oppression; movement, alternate targets and objective counterplay are incomplete.

**Recommended action:** Keep Ross’s settled mechanics. No cancellation or dual-weapon rule change is indicated by an implementation-oracle pass alone.

**Verdict scope:** Exact pool distributions, mixed-weapon Monte Carlo and selected paired melee exchanges. Complete legal crew counterbuilds have not run.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 48 contexts × 10,000 trials = 480,000 trials; no declared independent-oracle failures.

**Findings:** Sword/dagger and spear/axe outcomes agree with grouped-count math under defender choice.

**Notes / remaining work:** This completes the named conditional batch, not all mixed weapons or defender priorities.

**Evidence:** [mixed-cancellation.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/decision-validation/mixed-cancellation.csv>)

**Ross’s notes:**

<!-- ross-notes:W03 -->

<!-- /ross-notes -->

<a id="W04"></a>

### W04 — Compare dual Agile weapons with sword/shield

- [ ] **Partial** — Compare dual Agile weapons with sword/shield

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** The success/cancellation math and conditional attack/defence differences are verified. Powerful defence and asymmetric initiating pools alone do not establish oppression; movement, alternate targets and objective counterplay are incomplete.

**Recommended action:** Keep Ross’s settled mechanics. No cancellation or dual-weapon rule change is indicated by an implementation-oracle pass alone.

**Verdict scope:** Exact pool distributions, mixed-weapon Monte Carlo and selected paired melee exchanges. Complete legal crew counterbuilds have not run.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Conditional paired melee comparisons cover Stress, Armour and successful-Charge bonuses.

**Findings:** Initiating, defending and the chance of no remaining attacker successes must be separated.

**Notes / remaining work:** Movement-to-engagement, alternate targets, objective effects and broader counterbuilds remain.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>) · [melee-pool-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/melee-pool-atlas.csv>)

**Ross’s notes:**

<!-- ross-notes:W04 -->

<!-- /ross-notes -->

<a id="W05"></a>

### W05 — Measure all armour tiers in combat and objective play

- [ ] **Partial** — Measure all armour tiers in combat and objective play

#### Balance judgment

**Balance verdict: WATCH / CONFIRM.**

**Why:** The initial subset screen showed severe losses in some mobility-sensitive fixtures (14.25% and 17% match score). Improved held-out control-policy scores were 36.875%, 45.375% and 48.25%, with wide intervals. The extreme initial losses were not broadly confirmed; a universal armour buff is not supported.

**Recommended action:** Keep Armour 6 / −2 MOVE pending role-specific tests. Investigate whether escort/holding tasks repay the movement cost; do not use obsolete prices to declare it bad value.

**Verdict scope:** Reinforced-for-Light substitution on one controlled leader, v2 ground objective fixtures and limited held-out policy confirmation. These are not equal-Credit rosters.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Armour 0/2/4/6 appears in conditional math; Reinforced-for-Light substitutions appear in battle screens.

**Findings:** Reinforced armour’s MOVE penalty is costly in some tested objective contexts.

**Notes / remaining work:** These unpriced, setup-dependent outcomes do not establish a global armour ranking.

**Evidence:** [battle-matrix.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battle-matrix.csv>) · [matrix.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/matrix.csv>)

**Ross’s notes:**

<!-- ross-notes:W05 -->

<!-- /ross-notes -->

<a id="W06"></a>

### W06 — Complete Blast, cone, scatter, walls/floors and friendly-fire tests

- [ ] **Partial** — Complete Blast, cone, scatter, walls/floors and friendly-fire tests

#### Balance judgment

**Balance verdict: WATCH / CONFIRM.**

**Why:** Smoke has a provisional local utility/counterplay pass; flame, Flashbang and tear gas need further counterplay/tempo confirmation. Blast and fire still lack full balance evidence.

**Recommended action:** Keep the baseline. Prioritize activation denial, approach costs and legal counters; no area rule adjustment is justified yet.

**Verdict scope:** See the separate mechanic verdicts; W06 has no blanket pass.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 24 area fixtures plus 60 contexts / 600,000 trials; no declared independent-oracle failures. 4,000 paired smoke-lane tasks.

**Findings:** Scatter, clustering and printed payloads have conditional evidence. Smoke utility depends on the lane and the watcher’s Respirator.

**Notes / remaining work:** Horizontal flame only. Oblique placement and device-hit handling fail explicitly. Partial occlusion is sampled; full area battle policies, machinery interactions, falling fire victims and broad counterbuilds remain.

**Evidence:** [micro.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/area/micro.csv>) · [smoke-lane.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/area/smoke-lane.csv>) · [AREA-CONTRACT.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/AREA-CONTRACT.md>) · [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>)

**Ross’s notes:**

<!-- ross-notes:W06 -->

<!-- /ross-notes -->

<a id="W07"></a>

### W07 — Measure Flashbang activation denial and immediate counters

- [x] **Executed** — Measure Flashbang activation denial and immediate counters

#### Balance judgment

**Balance verdict: WATCH / CONFIRM.**

**Why:** The new 12,000-pair task shows high activation-denial impact. With clustered victims and attackers acting first, two Flashbang actions denied 1.686 of two victim activations on average (simultaneous 95% 1.429–1.943), plus 0.740 pending skips. ALERT counterfire reduced observed immediate denial to 1.200 and Downed 0.491 of two throwers on average. With victims acting first, immediate denial fell to 0.719 but 1.724 skips remained pending. Acting first delays some harm rather than cancelling it. Solid walls stopped this fixed-position delivery opportunity.

**Recommended action:** High-priority balance concern: do not pass Flashbang yet. Keep the baseline while testing sustained denial, routes and initiative-aware objective crews. Recommend an adjustment if repeated lockout remains efficient after those legal counters and resource costs; this one-round task alone does not justify a nerf.

**Verdict scope:** 12 cells × 1,000 paired seeds: two mechanically legal four-member crews, whole-unit alternating activations, clustered/spread victims, attacker/defender first, unready/ALERT/solid-wall counters. Same gear in both arms; control uses Aim. Task ends before End Phase; pending skips are not counted as already-lost future turns.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 12 cells × 1,000 paired seeds = 12,000 pairs / 24,000 task arms; 24 representative event/state replays reproduce. Whole-unit alternation and legal loadouts checked.

**Findings:** Strong first-cycle denial persists with ALERT counterfire; early victim activation can shift denial into pending next-activation skips. Solid walls remove this fixed-position delivery opportunity.

**Notes / remaining work:** First cycle only, before End Phase. Full repeated-use, movement/alternative objectives, morale and held-out competent crew responses remain; the mechanic is not passed and no change has been adopted.

**Evidence:** [[Settlements/Simulations/Results/Flashbang Activation Denial|FLASHBANG-RESULTS.md]] · [paired-summary.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v5/flash-denial/paired-summary.csv>) · [configs.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v5/flash-denial/configs.json>)

**Ross’s notes:**

<!-- ross-notes:W07 -->

<!-- /ross-notes -->

## 4. MOVE and TERRAIN — access, paths and displacement

<a id="M01"></a>

### M01 — Check basic paths, base clearance, arcs and movement boundaries

- [x] **Executed** — Check basic paths, base clearance, arcs and movement boundaries

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Named fixtures pass for detours, narrow gaps, corner clearance, body blocking, facing, Sprint, Charge, jumps and falls.

**Findings:** Basic movement cannot bypass walls or standing enemies; half-speed effects do not compound.

**Notes / remaining work:** These checks do not certify all vertical, door, obstacle or engagement procedures.

**Evidence:** [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>)

**Ross’s notes:**

<!-- ross-notes:M01 -->

<!-- /ross-notes -->

<a id="M02"></a>

### M02 — Complete climbing, ladders, doors, ledges and disengagement

- [ ] **Partial** — Complete climbing, ladders, doors, ledges and disengagement

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Selected traversal/fall and engagement checks pass.

**Findings:** Ground-board reachability does not establish multi-level tactical access.

**Notes / remaining work:** Complete vertical pathfinding, door costs, obstacle crossing, Reach and Disengage.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:M02 -->

<!-- /ross-notes -->

<a id="M03"></a>

### M03 — Complete Grapple, Carry, Hauler, Throw, release and extraction

- [ ] **Partial** — Complete Grapple, Carry, Hauler, Throw, release and extraction

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Partial handlers, selected allowances and feasibility checks exist.

**Findings:** No complete interception, structure sweep or escape/counterplay finding is supported.

**Notes / remaining work:** Test the whole-attack interception d6, collisions, ledges, loss triggers, cargo/captive routes and load restrictions.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:M03 -->

<!-- /ross-notes -->

<a id="M04"></a>

### M04 — Prove every interactive terrain profile and contested use

- [ ] **Partial** — Prove every interactive terrain profile and contested use

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** A door operation/repeated-XP fixture and selected terminal/light/alarm clauses exist.

**Findings:** A board named “contested machinery” does not mean all 17 features were operated.

**Notes / remaining work:** Each of the 17 profiles still needs complete occupied-space effects, counterplay and tactical measurement.

**Evidence:** [[Settlements/Simulations/Tracking/Rule and Item Coverage|SIMULATION-OWNER-CHECKLIST.md]] · [UNSUPPORTED-MECHANICS.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/UNSUPPORTED-MECHANICS.md>)

**Ross’s notes:**

<!-- ross-notes:M04 -->

<!-- /ross-notes -->

## 5. REACTION — ALERT, Orders, initiative and tempo

<a id="R01"></a>

### R01 — Check ALERT persistence, ordinary limits, Orders, Dive and Return Fire

- [x] **Executed** — Check ALERT persistence, ordinary limits, Orders, Dive and Return Fire

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Named token, per-round, per-battle, facing, Dive and simultaneous-shooting assertions pass.

**Findings:** Return Fire completes both ordinary attacks; Orders do not refresh between rounds.

**Notes / remaining work:** Only the named cases are checked; general reaction-action coverage remains partial.

**Evidence:** [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>)

**Ross’s notes:**

<!-- ross-notes:R01 -->

<!-- /ross-notes -->

<a id="R02"></a>

### R02 — Measure initiative, reaction tempo and final-activation effects

- [ ] **Partial** — Measure initiative, reaction tempo and final-activation effects

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Battle blocks cross side and forced first activation; first/second scores are recorded per cell.

**Findings:** First-activation effects vary by tested environment and matchup.

**Notes / remaining work:** A separate all-natural-first-round stratum, waiting incentives and complete action-cost decomposition remain.

**Evidence:** [battle-matrix.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battle-matrix.csv>)

**Ross’s notes:**

<!-- ross-notes:R02 -->

<!-- /ross-notes -->

<a id="R03"></a>

### R03 — Complete turret, Interrupt, counterattack and extra-action exceptions

- [ ] **Partial** — Complete turret, Interrupt, counterattack and extra-action exceptions

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Riposte termination and selected extra-action/Interrupt clauses have evidence.

**Findings:** Passing ordinary shooting reactions does not validate persistent turret or network exception timing.

**Notes / remaining work:** Complete exception chains, competing reactors, termination, legal resources and crew policies.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:R03 -->

<!-- /ross-notes -->

## 6. STRESS and CASUALTY — morale, suppression and recovery

<a id="S01"></a>

### S01 — Check hit Stress, Injury independence, Pinning, Break/Rally and timers

- [x] **Executed** — Check hit Stress, Injury independence, Pinning, Break/Rally and timers

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Named fixtures pass for Stress-before-Injury, uncapped Injury successes, morale bands, Rally, Down timers and revival history.

**Findings:** Non-wounding hits do not universally Pin; Injury ignores Stress; revival preserves spent activation history.

**Notes / remaining work:** Potential Injury successes differ from actual Wounds removed; read the metric definitions.

**Evidence:** [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>) · [METRIC-DEFINITIONS.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/METRIC-DEFINITIONS.md>)

**Ross’s notes:**

<!-- ross-notes:S01 -->

<!-- /ross-notes -->

<a id="S02"></a>

### S02 — Measure Stress cascades, recovery delay, denial and support across crews

- [ ] **Partial** — Measure Stress cascades, recovery delay, denial and support across crews

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Ground battles record final Stress and selected events; some support and witness clauses are checked.

**Findings:** Complete round-by-round Stress/action-denial and recovery comparisons are not delivered.

**Notes / remaining work:** Include low/high NRV, rookies versus elites, multiple attackers, auras, flight routes and objective exclusion.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:S02 -->

<!-- /ross-notes -->

<a id="S03"></a>

### S03 — Complete casualties, revival, Secure/Rescue, extraction and withdrawal

- [ ] **Partial** — Complete casualties, revival, Secure/Rescue, extraction and withdrawal

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Down/revival clauses, a promotion boundary and separate cargo/breakthrough fixtures exist.

**Findings:** Mission cargo extraction is not complete captive/escort validation.

**Notes / remaining work:** Complete physical withdrawal, escort release, casualty evacuation, device casualties and all Wound boundaries.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:S03 -->

<!-- /ross-notes -->

<a id="S04"></a>

### S04 — Test a once-per-Attack Stress diagnostic variant if baseline warrants it

- [ ] **Not run** — Test a once-per-Attack Stress diagnostic variant if baseline warrants it

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** No such variant was adopted or measured in this pass.

**Findings:** The current baseline remains per successful hit.

**Notes / remaining work:** Only run a labelled sensitivity variant if baseline evidence justifies that question.

**Evidence:** [RULES-CONTRACT.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/RULES-CONTRACT.md>)

**Ross’s notes:**

<!-- ross-notes:S04 -->

<!-- /ross-notes -->

## 7. STEALTH, TECH and GEAR — non-damage value

<a id="T01"></a>

### T01 — Complete Hidden, reveal, Observe, Marked, smoke and lighting

- [ ] **Partial** — Complete Hidden, reveal, Observe, Marked, smoke and lighting

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Mark expiry, Ghost/Phantom Shot and selected exposure/light clauses have checks.

**Findings:** No complete stealth policy or smoke/lighting counterplay measurement is established.

**Notes / remaining work:** Cover/Sneak/Quiet, proximity timing, Observe, flanks and enemy knowledge constraints still need full integration.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:T01 -->

<!-- /ross-notes -->

<a id="T02"></a>

### T02 — Check deployment assignment for all 11 deployables

- [x] **Executed** — Check deployment assignment for all 11 deployables

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** All 11 profiles passed a narrow deployment/assignment/slot-retention fixture.

**Findings:** An operator can deploy the assigned profile in the named setup.

**Notes / remaining work:** This explicitly does not certify its attacks, triggers, uptime or control/repair counterplay.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/clause-fixtures/assertions.csv>)

**Ross’s notes:**

<!-- ross-notes:T02 -->

<!-- /ross-notes -->

<a id="T03"></a>

### T03 — Complete six drones, five field deployables and hacking counterplay

- [ ] **Partial** — Complete six drones, five field deployables and hacking counterplay

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Deployment, selected control/shutdown, kit/terminal and shield-hit clauses exist.

**Findings:** One-hit ignore strongly affects one-die attacks in the conditional shield-drone atlas.

**Notes / remaining work:** Complete Flight/Hover, abilities, activation ordering, footprints, persistent fire, triggers, disarm/hijack and operator targeting.

**Evidence:** [shield-drone-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/shield-drone-atlas.csv>) · [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:T03 -->

<!-- /ross-notes -->

<a id="T04"></a>

### T04 — Complete all 22 equipment profiles and consumable limits

- [ ] **Partial** — Complete all 22 equipment profiles and consumable limits

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Selected Medkit, chem, Doc/Cocktail, Stabilize, slot and Unwieldy clauses pass.

**Findings:** These probes are not a complete equipment-use or AI-value study.

**Notes / remaining work:** Complete all grenades, smoke/gas, tools, load handling, histories, contacts, expiry and actual AI use.

**Evidence:** [[Settlements/Simulations/Tracking/Rule and Item Coverage|SIMULATION-OWNER-CHECKLIST.md]]

**Ross’s notes:**

<!-- ross-notes:T04 -->

<!-- /ross-notes -->

<a id="T05"></a>

### T05 — Run all planned timed access/rescue/objective tasks

- [ ] **Partial** — Run all planned timed access/rescue/objective tasks

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Smoke watched-lane and Flashbang console-denial tasks now have paired evidence; the complete elevated-objective, revive-and-escape, doorway, casualty-carry and smoke-contest pack remains incomplete.

**Findings:** No complete actions/turns/resources-saved ranking is supported.

**Notes / remaining work:** Use role-appropriate policies and record success, time and consumption separately.

**Ross’s notes:**

<!-- ross-notes:T05 -->

<!-- /ross-notes -->

## 8. COMBO — skills, archetypes and exploit search

<a id="K01"></a>

### K01 — Complete the full evidence ladder for every one of the 60 skills

- [ ] **Partial** — Complete the full evidence ladder for every one of the 60 skills

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Selected fixtures and hooks exist; all 60 skills have individual checklist entries.

**Findings:** No skill has the whole intended-use + unfavourable/counterplay + competent legal-crew ladder completed.

**Notes / remaining work:** Do not interpret an unused or unsupported skill as weak. Complete each skill’s ladder.

**Evidence:** [[Settlements/Simulations/Tracking/Rule and Item Coverage|SIMULATION-OWNER-CHECKLIST.md]] · [skill-scorecards.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/skill-scorecards.csv>)

**Ross’s notes:**

<!-- ross-notes:K01 -->

<!-- /ross-notes -->

<a id="K02"></a>

### K02 — Run conditional Rage + Implode and dual-weapon screens

- [x] **Executed** — Run conditional Rage + Implode and dual-weapon screens

#### Balance judgment

**Balance verdict: WATCH / CONFIRM.**

**Why:** Fresh-seed checks increased mean Injury successes by 0.041–0.050 per exchange, but increased retained attacker Stress by 1.167 and attacker Down frequency by 3.8 percentage points in the sampled Riposte contexts. This does not demonstrate an unavoidable dominant combo or a need to nerf an intended interaction.

**Recommended action:** Keep the intended combination. Test sustained multi-round benefit and risk against realistic counters before recommending a change.

**Verdict scope:** Two 1,000-pair conditional initiating-exchange confirmations at initial Stress 4, Standard/Reinforced armour; target may Riposte. No movement or full crew integration.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 36 cells × 250 independent seed pairs; 9,000 paired comparisons.

**Findings:** Results separate target Down, potential Injury successes, hits and attacker Stress.

**Notes / remaining work:** This is an exchange diagnostic; it does not establish movement opportunity or crew dominance.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:K02 -->

<!-- /ross-notes -->

<a id="K03"></a>

### K03 — Confirm the predeclared Rage + Implode contexts with new seeds

- [x] **Executed** — Confirm the predeclared Rage + Implode contexts with new seeds

#### Balance judgment

**Balance verdict: WATCH / CONFIRM.**

**Why:** Fresh-seed checks increased mean Injury successes by 0.041–0.050 per exchange, but increased retained attacker Stress by 1.167 and attacker Down frequency by 3.8 percentage points in the sampled Riposte contexts. This does not demonstrate an unavoidable dominant combo or a need to nerf an intended interaction.

**Recommended action:** Keep the intended combination. Test sustained multi-round benefit and risk against realistic counters before recommending a change.

**Verdict scope:** Two 1,000-pair conditional initiating-exchange confirmations at initial Stress 4, Standard/Reinforced armour; target may Riposte. No movement or full crew integration.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Two Stress-4/Armour-4-or-6 contexts × 1,000 fresh seed pairs.

**Findings:** The recorded conditional differences and uncertainty are in the run log; no general combo-dominance conclusion follows.

**Notes / remaining work:** Confirmation is tactical, not a held-out full-battle counterbuild test.

**Evidence:** [fixed-confirmation.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/fixed-confirmation.csv>)

**Ross’s notes:**

<!-- ross-notes:K03 -->

<!-- /ross-notes -->

<a id="K04"></a>

### K04 — Build the interaction graph and high-risk stat/skill feasibility search

- [x] **Executed** — Build the interaction graph and high-risk stat/skill feasibility search

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 1,191 candidate lexical interaction edges; 180 high-risk sets examined, 171 feasible and 9 blocked by caps.

**Findings:** Some four-skill same-Stat packages cannot be legal under current Stat limits.

**Notes / remaining work:** A graph edge is a search aid, not proof of an interaction. Gear, hands, slots, operators and behavior still need validation.

**Evidence:** [legal-pair-search.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/legal-pair-search.csv>) · [legal-high-risk-builds.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/legal-high-risk-builds.csv>)

**Ross’s notes:**

<!-- ross-notes:K04 -->

<!-- /ross-notes -->

<a id="K05"></a>

### K05 — Complete high-risk group 1: dual Agile/Gun-fu/Gunslinger/defence/charge/counterattacks

- [ ] **Partial** — Complete high-risk group 1: dual Agile/Gun-fu/Gunslinger/defence/charge/counterattacks

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Selected pool, Riposte, mixed cancellation and conditional dual-weapon evidence exists.

**Findings:** No complete legal crew-level dominance or lack-of-counterplay finding is established.

**Notes / remaining work:** Finish the group’s intended-use, counterbuild and held-out cases from PLAN.md.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:K05 -->

<!-- /ross-notes -->

<a id="K06"></a>

### K06 — Complete high-risk group 2: Rage/Implode and other Stress engines

- [ ] **Partial** — Complete high-risk group 2: Rage/Implode and other Stress engines

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Conditional Rage/Implode screening and fresh-seed confirmation ran.

**Findings:** No complete legal crew-level dominance or lack-of-counterplay finding is established.

**Notes / remaining work:** Finish the group’s intended-use, counterbuild and held-out cases from PLAN.md.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:K06 -->

<!-- /ross-notes -->

<a id="K07"></a>

### K07 — Complete high-risk group 3: tank armour/Brace/Tough as Nails/taunt/support

- [ ] **Partial** — Complete high-risk group 3: tank armour/Brace/Tough as Nails/taunt/support

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Selected clauses and armour substitutions exist; complete supported tank counterbuilds do not.

**Findings:** No complete legal crew-level dominance or lack-of-counterplay finding is established.

**Notes / remaining work:** Finish the group’s intended-use, counterbuild and held-out cases from PLAN.md.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:K07 -->

<!-- /ross-notes -->

<a id="K08"></a>

### K08 — Complete high-risk group 4: Mark/Head Shot/range extension/drone support

- [ ] **Partial** — Complete high-risk group 4: Mark/Head Shot/range extension/drone support

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Selected marksman clauses exist; the complete combined drone package is unmeasured.

**Findings:** No complete legal crew-level dominance or lack-of-counterplay finding is established.

**Notes / remaining work:** Finish the group’s intended-use, counterbuild and held-out cases from PLAN.md.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:K08 -->

<!-- /ross-notes -->

<a id="K09"></a>

### K09 — Complete high-risk group 5: Hidden/Ghost/Phantom Shot/cover/smoke/reveal

- [ ] **Partial** — Complete high-risk group 5: Hidden/Ghost/Phantom Shot/cover/smoke/reveal

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Ghost/Phantom Shot clause evidence exists; the full counterplay package is unmeasured.

**Findings:** No complete legal crew-level dominance or lack-of-counterplay finding is established.

**Notes / remaining work:** Finish the group’s intended-use, counterbuild and held-out cases from PLAN.md.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:K09 -->

<!-- /ross-notes -->

<a id="K10"></a>

### K10 — Complete high-risk group 6: extra actions/auras/Orders/chems/reload

- [ ] **Partial** — Complete high-risk group 6: extra actions/auras/Orders/chems/reload

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Selected resource/tempo clauses pass; complete combination and loop searches are missing.

**Findings:** No complete legal crew-level dominance or lack-of-counterplay finding is established.

**Notes / remaining work:** Finish the group’s intended-use, counterbuild and held-out cases from PLAN.md.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:K10 -->

<!-- /ross-notes -->

<a id="K11"></a>

### K11 — Complete high-risk group 7: shield drone and its counters

- [ ] **Partial** — Complete high-risk group 7: shield drone and its counters

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** One-hit-ignore math exists; operator, disabling, Blast, flank and objective counters are missing.

**Findings:** No complete legal crew-level dominance or lack-of-counterplay finding is established.

**Notes / remaining work:** Finish the group’s intended-use, counterbuild and held-out cases from PLAN.md.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:K11 -->

<!-- /ross-notes -->

<a id="K12"></a>

### K12 — Complete high-risk group 8: turrets/mines/Cloaking/activation delay/hijack

- [ ] **Partial** — Complete high-risk group 8: turrets/mines/Cloaking/activation delay/hijack

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Deployment-only and shutdown clauses exist; the combined kill-zone/counterplay suite has not run.

**Findings:** No complete legal crew-level dominance or lack-of-counterplay finding is established.

**Notes / remaining work:** Finish the group’s intended-use, counterbuild and held-out cases from PLAN.md.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:K12 -->

<!-- /ross-notes -->

<a id="K13"></a>

### K13 — Complete high-risk group 9: slot expansion/replacement/resource loops

- [ ] **Partial** — Complete high-risk group 9: slot expansion/replacement/resource loops

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Selected capacity and identical-effect checks pass; full duplication/zero-cost-loop searches are missing.

**Findings:** No complete legal crew-level dominance or lack-of-counterplay finding is established.

**Notes / remaining work:** Finish the group’s intended-use, counterbuild and held-out cases from PLAN.md.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:K13 -->

<!-- /ross-notes -->

<a id="K14"></a>

### K14 — Complete high-risk group 10: crane/Throw/falls/compactor/extraction denial

- [ ] **Partial** — Complete high-risk group 10: crane/Throw/falls/compactor/extraction denial

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Fall and some partial handlers exist; full contested terrain/control combinations are unmeasured.

**Findings:** No complete legal crew-level dominance or lack-of-counterplay finding is established.

**Notes / remaining work:** Finish the group’s intended-use, counterbuild and held-out cases from PLAN.md.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:K14 -->

<!-- /ross-notes -->

<a id="K15"></a>

### K15 — Complete all fifteen archetype integrations and adversarial best responses

- [ ] **Not run** — Complete all fifteen archetype integrations and adversarial best responses

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** The complete archetype roster rotation, repeated best-response search and held-out exploit confirmation have not run.

**Findings:** The current small targeted search cannot establish that no dominant combination exists.

**Notes / remaining work:** Use legal starting/advanced builds and improve both opposing policies fairly.

**Evidence:** [archetype-scorecards.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/archetype-scorecards.csv>)

**Ross’s notes:**

<!-- ross-notes:K15 -->

<!-- /ross-notes -->

## 9. CREW, PROGRESSION, boards and policies — plan §§4–7

<a id="P01"></a>

### P01 — Verify current roster skeletons and advancement boundaries

- [ ] **Partial** — Verify current roster skeletons and advancement boundaries

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 4/6/9-actor skeletons, selected Stat/skill/equipment legality and promotion assertions exist.

**Findings:** Current budgets are 2/3/5/7, with unused starting points allowed and lost.

**Notes / remaining work:** Complete all rank thresholds, advanced histories, equipment packages and progression/reward boundaries.

**Evidence:** [crews.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/crews.json>) · [conformance.txt](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/conformance.txt>)

**Ross’s notes:**

<!-- ross-notes:P01 -->

<!-- /ross-notes -->

<a id="P02"></a>

### P02 — Check repeat terrain-interaction XP opportunities

- [x] **Executed** — Check repeat terrain-interaction XP opportunities

#### Balance judgment

**Balance verdict: WATCH / CONFIRM.**

**Why:** Repeated successful door interactions each create an XP opportunity under current text. This is a potential farming incentive. The test does not show an infinite action loop or prove that farming beats mission/reward play.

**Recommended action:** Flag the incentive for campaign-boundary review; do not add a cap yet. Recommend a change only if repeated operation produces a material exploit after action and battle-ending costs.

**Verdict scope:** Two successful door operations; reward/campaign incentives not fully integrated.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** The door fixture records two successful operations earning two XP opportunities.

**Findings:** The current rule has no once-per-terminal cap; no cap was invented.

**Notes / remaining work:** This is not proof of an infinite action loop or complete farming/withdrawal incentive analysis.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/clause-fixtures/assertions.csv>)

**Ross’s notes:**

<!-- ross-notes:P02 -->

<!-- /ross-notes -->

<a id="P03"></a>

### P03 — Complete rewards, XP deeds and battle-relevant progression incentives

- [ ] **Partial** — Complete rewards, XP deeds and battle-relevant progression incentives

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Selected XP/unlock/promotion clauses and legal advanced sets are recorded.

**Findings:** Campaign snowball and complete settlement economy remain outside this pass.

**Notes / remaining work:** Finish all deeds, survival/revival/Out-of-Action attribution, withdrawal rewards and repeated advance boundaries.

**Evidence:** [scope-audit.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/scope-audit.csv>)

**Ross’s notes:**

<!-- ross-notes:P03 -->

<!-- /ross-notes -->

<a id="B01"></a>

### B01 — Author and reachability-check the six board families

- [x] **Executed** — Author and reachability-check the six board families

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 24 layouts: three initial variants plus one held-out variant per family; ground objective reachability checks pass.

**Findings:** Two inaccessible placements were corrected before the measured screen.

**Notes / remaining work:** Geometry is rectangular and LOS is sampled; do not treat reachability as full vertical or tactical board validation.

**Evidence:** [boards.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/boards.json>) · [board-metrics.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/board-metrics.csv>)

**Ross’s notes:**

<!-- ross-notes:B01 -->

<!-- /ross-notes -->

<a id="B02"></a>

### B02 — Complete all planned board metrics and alternate/vertical access

- [ ] **Partial** — Complete all planned board metrics and alternate/vertical access

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Footprint fractions and route-length metrics are saved.

**Findings:** Terrain count alone is not used as a density guarantee.

**Notes / remaining work:** Longest useful lanes, protected routes, choke widths, full climb/flying/hover access and independent alternate approaches remain.

**Evidence:** [board-metrics.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/board-metrics.csv>)

**Ross’s notes:**

<!-- ross-notes:B02 -->

<!-- /ross-notes -->

<a id="B03"></a>

### B03 — Define the four non-adopted objective fixture families

- [x] **Executed** — Define the four non-adopted objective fixture families

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Distributed control, recover/extract, network operation and breakthrough fixtures are specified.

**Findings:** The fixtures allow objective success without casualty VP.

**Notes / remaining work:** Fixture definitions do not become approved scenarios; dedicated attack/defend role-swap coverage remains incomplete.

**Evidence:** [scenarios.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/scenarios.json>)

**Ross’s notes:**

<!-- ross-notes:B03 -->

<!-- /ross-notes -->

<a id="B04"></a>

### B04 — Complete policy competence for all roles and equipment

- [ ] **Partial** — Complete policy competence for all roles and equipment

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Balanced, pressure, cautious and flank ground heuristics exist; occupancy-aware confirmation improves both arms.

**Findings:** Crowding/occupied-objective requests limited the initial policy; the limitations are logged.

**Notes / remaining work:** Complete tech/support, stealth, vertical, equipment, resource planning and operator-targeting policies.

**Evidence:** [policies.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/policies.json>) · [manifest.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/manifest.json>)

**Ross’s notes:**

<!-- ross-notes:B04 -->

<!-- /ross-notes -->

<a id="B05"></a>

### B05 — Run unequal-headcount and cross-role counterbuild sensitivity

- [ ] **Not run** — Run unequal-headcount and cross-role counterbuild sensitivity

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Several crew sizes ran, but the required elite-versus-one/two-extra-basic-actors comparisons and complete role matrix did not.

**Findings:** Multiple crew sizes alone do not establish an unequal-count trade-off.

**Notes / remaining work:** Do not translate a provisional headcount exchange into a Credit price.

**Ross’s notes:**

<!-- ross-notes:B05 -->

<!-- /ross-notes -->

## 10. Full-battle screens, replication and integrity — plan §§8–9

<a id="G01"></a>

### G01 — Run the declared exploratory ground-subset battle matrix

- [x] **Executed** — Run the declared exploratory ground-subset battle matrix

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 30 cells × 100 four-game independent seed blocks = 12,000 games.

**Findings:** The six mirror cells range from 46.4% to 54.4% focal match score; uncertainty remains broad.

**Notes / remaining work:** Each cell’s full findings, intervals, W/D/L and notes appear in the results log. Ground subset only.

**Evidence:** [battle-matrix.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battle-matrix.csv>) · [[Settlements/Simulations/Results/Simulation Results Log|SIMULATION-RESULTS-LOG.md]]

**Ross’s notes:**

<!-- ross-notes:G01 -->

<!-- /ross-notes -->

<a id="G02"></a>

### G02 — Confirm selected substitutions with free objective approaches

- [x] **Executed** — Confirm selected substitutions with free objective approaches

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Six held-out board/policy cells × 100 four-game seed blocks = 2,400 games.

**Findings:** Conditional armour/movement losses persist in some improved-policy control fixtures.

**Notes / remaining work:** This is not complete catalogue best-response validation. The slow first implementation was aborted and excluded.

**Evidence:** [matrix.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/matrix.csv>)

**Ross’s notes:**

<!-- ross-notes:G02 -->

<!-- /ross-notes -->

<a id="G03"></a>

### G03 — Check unchanged outcomes after the defender-choice decision

- [x] **Executed** — Check unchanged outcomes after the defender-choice decision

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** 96 frozen-v2/current-v3 matched comparisons produced identical outcomes.

**Findings:** The earlier single-weapon homogeneous outcome strata are unaffected by the clarified mixed-pool choice.

**Notes / remaining work:** Keep the 14,400 earlier games under their v2 manifest; do not silently relabel them v3.

**Evidence:** [homogeneous-regression.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/decision-validation/homogeneous-regression.csv>) · [carry-forward-manifest.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/carry-forward-manifest.json>)

**Ross’s notes:**

<!-- ross-notes:G03 -->

<!-- /ross-notes -->

<a id="G04"></a>

### G04 — Finish representative full-system battles and precision escalation

- [ ] **Partial** — Finish representative full-system battles and precision escalation

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** The declared ground screen and limited held-out confirmation ran.

**Findings:** No whole-game balance conclusion follows while tech, support, terrain and other policies are incomplete.

**Notes / remaining work:** Complete the missing strata, ordinary-first-round initiative cases, relevant counters and 500–1,000-block escalation where justified.

**Evidence:** [COMPLETION-GATES.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/COMPLETION-GATES.md>)

**Ross’s notes:**

<!-- ross-notes:G04 -->

<!-- /ross-notes -->

<a id="G05"></a>

### G05 — Verify counts, provenance, seeds and independent-sample uncertainty

- [ ] **Partial** — Verify counts, provenance, seeds and independent-sample uncertainty

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Source/engine manifests, seeds, four-game blocks, counts and bounded-mean intervals are recorded.

**Findings:** Swapped games are correlated; all-draw samples do not receive zero-width certainty.

**Notes / remaining work:** Full event reconstruction and all required per-source positive-effect/utility metrics remain incomplete.

**Evidence:** [block-integrity.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/block-integrity.json>) · [publication-manifest.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/publication-manifest.json>) · [METRIC-DEFINITIONS.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/METRIC-DEFINITIONS.md>)

**Ross’s notes:**

<!-- ross-notes:G05 -->

<!-- /ross-notes -->

## 11. Review, completion gates and handoff — plan §§10–12

<a id="D01"></a>

### D01 — Publish findings, source coverage, manifests and reproducible outputs

- [x] **Executed** — Publish findings, source coverage, manifests and reproducible outputs

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Versioned reviews, coverage, source/engine manifests, configs, seeds, raw results, replay samples and current commands are available.

**Findings:** The reports explicitly state incomplete coverage and separate implementation failures from balance evidence.

**Notes / remaining work:** Publishing the reports does not close the unfulfilled simulation gates.

**Evidence:** [EXECUTION-REVIEW.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/EXECUTION-REVIEW.md>) · [FINDINGS.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/FINDINGS.md>) · [coverage.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/coverage.csv>)

**Ross’s notes:**

<!-- ross-notes:D01 -->

<!-- /ross-notes -->

<a id="D02"></a>

### D02 — Close all six completion gates

- [ ] **Partial** — Close all six completion gates

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Gates 1–5 remain incomplete/not established; the uncertainty/playtest packet is delivered.

**Findings:** The pass is not ready to begin pricing.

**Notes / remaining work:** See the exact gate-by-gate reasons; do not mark the overall pass complete.

**Evidence:** [COMPLETION-GATES.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/COMPLETION-GATES.md>)

**Ross’s notes:**

<!-- ross-notes:D02 -->

<!-- /ross-notes -->

<a id="D03"></a>

### D03 — Prepare the human-playtest follow-up

- [x] **Executed** — Prepare the human-playtest follow-up

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** A follow-up packet covers mirrors, melee/shields, Stress, terrain/hacking, stealth, deployables, support/revival and combinations.

**Findings:** Human pace, frustration, bookkeeping and decision quality are still untested.

**Notes / remaining work:** Conduct and record the sessions separately; preparation is not human-play validation.

**Evidence:** [HUMAN-PLAYTEST.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/HUMAN-PLAYTEST.md>)

**Ross’s notes:**

<!-- ross-notes:D03 -->

<!-- /ross-notes -->

<a id="D04"></a>

### D04 — Prepare the conditional trait-measurement handoff without prices

- [x] **Executed** — Prepare the conditional trait-measurement handoff without prices

#### Balance judgment

**Balance verdict: NOT A BALANCE TEST.**

**Why:** This entry checks implementation, math, provenance or test preparation. Passing it does not establish that a game mechanic is balanced.

**Recommended action:** Use the mechanic’s balance verdict and comparative tests before proposing a rule adjustment.

**Verdict scope:** The named check only.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** The handoff records interaction, restriction, uncertainty and double-counting requirements.

**Findings:** A universal flat trait value is not established by these diagnostics.

**Notes / remaining work:** Required utility/counterplay measurements are missing; no new Credit prices have been calculated or adopted.

**Evidence:** [PRICING-HANDOFF.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/PRICING-HANDOFF.md>)

**Ross’s notes:**

<!-- ross-notes:D04 -->

<!-- /ross-notes -->

<a id="D05"></a>

### D05 — Complete the measurement foundation required for a later Credits rebuild

- [ ] **Partial** — Complete the measurement foundation required for a later Credits rebuild

#### Balance judgment

**Balance verdict: INSUFFICIENT EVIDENCE.**

**Why:** This entry does not yet establish the comparative intended-use, constraint and counterplay evidence needed for a balance pass.

**Recommended action:** Keep the baseline and complete the remaining tests listed below. No evidence-backed adjustment is recommended yet.

**Verdict scope:** Only the explicitly recorded results; no global balance sign-off.

**Balance review:** [[Settlements/Simulations/Analysis/Balance Verdicts|Mechanic verdicts and next tests]]

#### Results

**Recorded result:** Conditional combat and limited objective evidence are available.

**Findings:** Pricing readiness remains blocked by the explicit completion gates.

**Notes / remaining work:** Finish missing mechanics/value-vector coverage and held-out testing before a separate pricing task.

**Evidence:** [COMPLETION-GATES.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v4/COMPLETION-GATES.md>)

**Ross’s notes:**

<!-- ross-notes:D05 -->

<!-- /ross-notes -->
<!-- /settlements-simulation:generated -->

## Additional notes

