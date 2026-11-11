<!-- settlements-simulation:generated -->
# Settlements simulation results log

Recorded evidence as of **2026-11-11**. [[Settlements/Simulations/Tracking/Simulation Plan Checklist|Back to the plan checklist]] · [[Settlements/Simulations/Tracking/Rule and Item Coverage|Individual owners]]

This log inventories existing runs; generating it launches no simulations. **Executed** means the named batch/check finished. It does not mean that all mechanics mentioned in its name are fully validated. Raw metrics retain their producing version; current v3 carries v2 homogeneous battle strata explicitly. All rates are conditional on their listed setup.

## A. Exact tables and Monte Carlo checks

<a id="A01"></a>

### A01 — Conditional weapon probability atlas

- [x] **Executed** — Conditional weapon probability atlas

#### Results

**Recorded result:** 72,840 exact rows.

**Findings:** The file distinguishes the probabilities/expectations appropriate to its declared contexts.

**Notes / remaining work:** Conditional dice math excludes complete movement, timing, AI utility and human play.

**Evidence:** [probability-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/probability-atlas.csv>) · [METRIC-DEFINITIONS.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/METRIC-DEFINITIONS.md>)

**Ross’s notes:**

<!-- ross-notes:A01 -->

<!-- /ross-notes -->

<a id="A02"></a>

### A02 — Raw Stat/Stress threshold atlas

- [x] **Executed** — Raw Stat/Stress threshold atlas

#### Results

**Recorded result:** 56 exact rows.

**Findings:** The file distinguishes the probabilities/expectations appropriate to its declared contexts.

**Notes / remaining work:** Conditional dice math excludes complete movement, timing, AI utility and human play.

**Evidence:** [stat-threshold-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/stat-threshold-atlas.csv>) · [METRIC-DEFINITIONS.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/METRIC-DEFINITIONS.md>)

**Ross’s notes:**

<!-- ross-notes:A02 -->

<!-- /ross-notes -->

<a id="A03"></a>

### A03 — Single opposed-test atlas

- [x] **Executed** — Single opposed-test atlas

#### Results

**Recorded result:** 441 exact rows.

**Findings:** The file distinguishes the probabilities/expectations appropriate to its declared contexts.

**Notes / remaining work:** Conditional dice math excludes complete movement, timing, AI utility and human play.

**Evidence:** [opposed-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/opposed-atlas.csv>) · [METRIC-DEFINITIONS.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/METRIC-DEFINITIONS.md>)

**Ross’s notes:**

<!-- ross-notes:A03 -->

<!-- /ross-notes -->

<a id="A04"></a>

### A04 — Homogeneous melee pool/defence atlas

- [x] **Executed** — Homogeneous melee pool/defence atlas

#### Results

**Recorded result:** 96 exact rows.

**Findings:** The file distinguishes the probabilities/expectations appropriate to its declared contexts.

**Notes / remaining work:** Conditional dice math excludes complete movement, timing, AI utility and human play.

**Evidence:** [melee-pool-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/melee-pool-atlas.csv>) · [METRIC-DEFINITIONS.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/METRIC-DEFINITIONS.md>)

**Ross’s notes:**

<!-- ross-notes:A04 -->

<!-- /ross-notes -->

<a id="A05"></a>

### A05 — One-hit-ignore conditional atlas

- [x] **Executed** — One-hit-ignore conditional atlas

#### Results

**Recorded result:** 72 exact rows.

**Findings:** The file distinguishes the probabilities/expectations appropriate to its declared contexts.

**Notes / remaining work:** Conditional dice math excludes complete movement, timing, AI utility and human play.

**Evidence:** [shield-drone-atlas.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/shield-drone-atlas.csv>) · [METRIC-DEFINITIONS.md](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/METRIC-DEFINITIONS.md>)

**Ross’s notes:**

<!-- ross-notes:A05 -->

<!-- /ross-notes -->

<a id="A06"></a>

### A06 — Individual weapon Monte Carlo results

- [x] **Executed** — Individual weapon Monte Carlo results

#### Results

**Recorded result:** 190,000 trials across 19 weapons; three area-weapon geometry batches remain unrun.

**Findings:** All recorded ordinary-weapon oracle checks passed.

**Notes / remaining work:** Stat 3, Armour 4, target Wounds 3, fresh target per action. Zero Down for a one-die profile against three Wounds is not evidence of uselessness.

**Evidence:** [combat-micro.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/combat-micro.csv>)

| Weapon | Trials | Any hit | Any Wound (95% interval) | Down | Oracle |
| --- | --- | --- | --- | --- | --- |
| Unarmed | 10000 | 37.02% | 7.46% (6.96%–7.99%) | 0.00% | True |
| Dagger / Shiv | 10000 | 64.18% | 15.91% (15.21%–16.64%) | 0.00% | True |
| Sword / Machete | 10000 | 64.18% | 19.79% (19.02%–20.58%) | 0.00% | True |
| Crowbar | 10000 | 37.02% | 9.30% (8.75%–9.88%) | 0.00% | True |
| Spear | 10000 | 37.02% | 12.83% (12.19%–13.50%) | 0.00% | True |
| Two-handed axe | 10000 | 37.02% | 21.33% (20.54%–22.14%) | 0.00% | True |
| Pistol | 10000 | 54.66% | 13.84% (13.18%–14.53%) | 0.00% | True |
| Revolver | 10000 | 79.09% | 23.70% (22.88%–24.54%) | 0.00% | True |
| Magnum | 10000 | 54.66% | 19.15% (18.39%–19.93%) | 0.00% | True |
| Carbine | 10000 | 79.09% | 23.70% (22.88%–24.54%) | 0.00% | True |
| Assault rifle | 10000 | 79.42% | 30.00% (29.11%–30.91%) | 0.00% | True |
| Submachine gun | 10000 | 79.42% | 25.48% (24.64%–26.34%) | 0.00% | True |
| Shotgun | 10000 | 54.66% | 19.15% (18.39%–19.93%) | 0.00% | True |
| Suppressed carbine | 10000 | 54.66% | 16.56% (15.84%–17.30%) | 0.00% | True |
| Sniper rifle | 10000 | 79.09% | 45.93% (44.96%–46.91%) | 0.00% | True |
| Machine gun | 10000 | 90.50% | 52.63% (51.65%–53.61%) | 1.07% | True |
| Grenade launcher | 0 | — | Not measured | — | Geometry outstanding |
| Flamethrower | 0 | — | Not measured | — | Geometry outstanding |
| Rocket launcher | 0 | — | Not measured | — | Geometry outstanding |
| Throwing knife | 10000 | 54.66% | 13.84% (13.18%–14.53%) | 0.00% | True |
| Javelin | 10000 | 54.66% | 27.87% (27.00%–28.76%) | 0.00% | True |
| Club / Hammer / Steel pipe | 10000 | 37.02% | 16.64% (15.92%–17.38%) | 0.00% | True |

**Ross’s notes:**

<!-- ross-notes:A06 -->

<!-- /ross-notes -->

<a id="A07"></a>

### A07 — Mixed-weapon defender-choice validation

- [x] **Executed** — Mixed-weapon defender-choice validation

#### Results

**Recorded result:** 48 contexts × 10,000 trials = 480,000; no declared oracle failures.

**Findings:** Defender-selected normal/critical cancellation matches the independent grouped-count calculation in these contexts.

**Notes / remaining work:** Pairs: sword/dagger and spear/axe. The policy minimizes Injury; it does not explore every positional/keyword priority.

**Evidence:** [mixed-cancellation.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/decision-validation/mixed-cancellation.csv>)

| Pair | Stress | Armour | Defence dice | Observed any Wound | Exact | 95% interval | Check |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Sword / Machete + Dagger / Shiv | 0 | 0 | 1 | 57.86% | 58.39% | 56.89%–58.82% | True |
| Sword / Machete + Dagger / Shiv | 0 | 0 | 5 | 21.15% | 21.36% | 20.36%–21.96% | True |
| Sword / Machete + Dagger / Shiv | 0 | 2 | 1 | 47.41% | 48.03% | 46.43%–48.39% | True |
| Sword / Machete + Dagger / Shiv | 0 | 2 | 5 | 16.79% | 16.77% | 16.07%–17.54% | True |
| Sword / Machete + Dagger / Shiv | 0 | 4 | 1 | 35.99% | 35.67% | 35.05%–36.94% | True |
| Sword / Machete + Dagger / Shiv | 0 | 4 | 5 | 11.77% | 11.83% | 11.15%–12.42% | True |
| Sword / Machete + Dagger / Shiv | 0 | 6 | 1 | 21.46% | 21.06% | 20.67%–22.28% | True |
| Sword / Machete + Dagger / Shiv | 0 | 6 | 5 | 6.60% | 6.51% | 6.13%–7.10% | True |
| Sword / Machete + Dagger / Shiv | 3 | 0 | 1 | 45.00% | 44.96% | 44.03%–45.98% | True |
| Sword / Machete + Dagger / Shiv | 3 | 0 | 5 | 14.81% | 14.73% | 14.13%–15.52% | True |
| Sword / Machete + Dagger / Shiv | 3 | 2 | 1 | 36.58% | 36.28% | 35.64%–37.53% | True |
| Sword / Machete + Dagger / Shiv | 3 | 2 | 5 | 11.72% | 11.47% | 11.10%–12.37% | True |
| Sword / Machete + Dagger / Shiv | 3 | 4 | 1 | 26.29% | 26.44% | 25.44%–27.16% | True |
| Sword / Machete + Dagger / Shiv | 3 | 4 | 5 | 7.90% | 8.05% | 7.39%–8.44% | True |
| Sword / Machete + Dagger / Shiv | 3 | 6 | 1 | 15.32% | 15.33% | 14.63%–16.04% | True |
| Sword / Machete + Dagger / Shiv | 3 | 6 | 5 | 4.47% | 4.44% | 4.08%–4.89% | True |
| Sword / Machete + Dagger / Shiv | 5 | 0 | 1 | 34.87% | 35.42% | 33.94%–35.81% | True |
| Sword / Machete + Dagger / Shiv | 5 | 0 | 5 | 11.37% | 11.42% | 10.76%–12.01% | True |
| Sword / Machete + Dagger / Shiv | 5 | 2 | 1 | 28.66% | 28.23% | 27.78%–29.55% | True |
| Sword / Machete + Dagger / Shiv | 5 | 2 | 5 | 8.97% | 8.86% | 8.43%–9.55% | True |
| Sword / Machete + Dagger / Shiv | 5 | 4 | 1 | 20.14% | 20.33% | 19.37%–20.94% | True |
| Sword / Machete + Dagger / Shiv | 5 | 4 | 5 | 5.89% | 6.19% | 5.45%–6.37% | True |
| Sword / Machete + Dagger / Shiv | 5 | 6 | 1 | 11.66% | 11.67% | 11.05%–12.30% | True |
| Sword / Machete + Dagger / Shiv | 5 | 6 | 5 | 3.61% | 3.43% | 3.26%–3.99% | True |
| Spear + Two-handed axe | 0 | 0 | 1 | 42.19% | 41.86% | 41.23%–43.16% | True |
| Spear + Two-handed axe | 0 | 0 | 5 | 8.98% | 9.29% | 8.44%–9.56% | True |
| Spear + Two-handed axe | 0 | 2 | 1 | 36.24% | 36.32% | 35.30%–37.19% | True |
| Spear + Two-handed axe | 0 | 2 | 5 | 7.77% | 7.90% | 7.26%–8.31% | True |
| Spear + Two-handed axe | 0 | 4 | 1 | 29.73% | 29.98% | 28.84%–30.63% | True |
| Spear + Two-handed axe | 0 | 4 | 5 | 6.35% | 6.38% | 5.89%–6.84% | True |
| Spear + Two-handed axe | 0 | 6 | 1 | 22.69% | 22.73% | 21.88%–23.52% | True |
| Spear + Two-handed axe | 0 | 6 | 5 | 5.01% | 4.73% | 4.60%–5.46% | True |
| Spear + Two-handed axe | 3 | 0 | 1 | 31.41% | 31.30% | 30.51%–32.33% | True |
| Spear + Two-handed axe | 3 | 0 | 5 | 7.84% | 7.70% | 7.33%–8.38% | True |
| Spear + Two-handed axe | 3 | 2 | 1 | 27.31% | 27.01% | 26.45%–28.19% | True |
| Spear + Two-handed axe | 3 | 2 | 5 | 6.26% | 6.55% | 5.80%–6.75% | True |
| Spear + Two-handed axe | 3 | 4 | 1 | 22.72% | 22.16% | 21.91%–23.55% | True |
| Spear + Two-handed axe | 3 | 4 | 5 | 5.17% | 5.30% | 4.75%–5.62% | True |
| Spear + Two-handed axe | 3 | 6 | 1 | 16.79% | 16.70% | 16.07%–17.54% | True |
| Spear + Two-handed axe | 3 | 6 | 5 | 3.84% | 3.93% | 3.48%–4.23% | True |
| Spear + Two-handed axe | 5 | 0 | 1 | 24.87% | 24.40% | 24.03%–25.73% | True |
| Spear + Two-handed axe | 5 | 0 | 5 | 7.07% | 6.81% | 6.58%–7.59% | True |
| Spear + Two-handed axe | 5 | 2 | 1 | 20.80% | 20.97% | 20.02%–21.61% | True |
| Spear + Two-handed axe | 5 | 2 | 5 | 5.60% | 5.81% | 5.17%–6.07% | True |
| Spear + Two-handed axe | 5 | 4 | 1 | 16.61% | 17.14% | 15.89%–17.35% | True |
| Spear + Two-handed axe | 5 | 4 | 5 | 4.79% | 4.70% | 4.39%–5.23% | True |
| Spear + Two-handed axe | 5 | 6 | 1 | 12.82% | 12.85% | 12.18%–13.49% | True |
| Spear + Two-handed axe | 5 | 6 | 5 | 3.68% | 3.49% | 3.33%–4.07% | True |

**Ross’s notes:**

<!-- ross-notes:A07 -->

<!-- /ross-notes -->

## B. Every primary conformance check

<a id="Q01"></a>

### Q01 — Accurate one miss only

- [x] **Executed** — Accurate one miss only

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-231, V2-291. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_accurate_one_miss_only](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q01 -->

<!-- /ross-notes -->

<a id="Q02"></a>

### Q02 — Alert retention and once per round

- [x] **Executed** — Alert retention and once per round

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-061, V2-073. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_alert_retention_and_once_per_round](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q02 -->

<!-- /ross-notes -->

<a id="Q03"></a>

### Q03 — Atlas hand worked rifle

- [x] **Executed** — Atlas hand worked rifle

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-097, V2-114. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_atlas_hand_worked_rifle](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q03 -->

<!-- /ross-notes -->

<a id="Q04"></a>

### Q04 — Boundaries and independent oracle

- [x] **Executed** — Boundaries and independent oracle

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-017, V2-114. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_boundaries_and_independent_oracle](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q04 -->

<!-- /ross-notes -->

<a id="Q05"></a>

### Q05 — Break and rally subtract stress

- [x] **Executed** — Break and rally subtract stress

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-139, V2-150. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_break_and_rally_subtract_stress](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q05 -->

<!-- /ross-notes -->

<a id="Q06"></a>

### Q06 — Break no same phase rally and beta exception

- [x] **Executed** — Break no same phase rally and beta exception

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-139, V2-150, V2-540. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_break_no_same_phase_rally_and_beta_exception](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q06 -->

<!-- /ross-notes -->

<a id="Q07"></a>

### Q07 — Category largest not sum

- [x] **Executed** — Category largest not sum

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-017. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_category_largest_not_sum](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q07 -->

<!-- /ross-notes -->

<a id="Q08"></a>

### Q08 — Chem no unlock duplicate or extra wounds

- [x] **Executed** — Chem no unlock duplicate or extra wounds

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-270, V2-498, V2-504. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_chem_no_unlock_duplicate_or_extra_wounds](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q08 -->

<!-- /ross-notes -->

<a id="Q09"></a>

### Q09 — Critical cancellation hand case

- [x] **Executed** — Critical cancellation hand case

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-106, V2-114. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_critical_cancellation_hand_case](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q09 -->

<!-- /ross-notes -->

<a id="Q10"></a>

### Q10 — Defender choice values piercing and respects critical groups

- [x] **Executed** — Defender choice values piercing and respects critical groups

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-106, V2-238. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_defender_choice_values_piercing_and_respects_critical_groups](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q10 -->

<!-- /ross-notes -->

<a id="Q11"></a>

### Q11 — Defender chooses mixed success cancellation

- [x] **Executed** — Defender chooses mixed success cancellation

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-106, V2-102. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_defender_chooses_mixed_success_cancellation](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q11 -->

<!-- /ross-notes -->

<a id="Q12"></a>

### Q12 — Defender surplus has no hits or stress

- [x] **Executed** — Defender surplus has no hits or stress

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-106. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_defender_surplus_has_no_hits_or_stress](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q12 -->

<!-- /ross-notes -->

<a id="Q13"></a>

### Q13 — Down timer and no surplus execution

- [x] **Executed** — Down timer and no surplus execution

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-122, V2-114. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_down_timer_and_no_surplus_execution](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q13 -->

<!-- /ross-notes -->

<a id="Q14"></a>

### Q14 — Dual agile and parry shield stack

- [x] **Executed** — Dual agile and parry shield stack

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-102, V2-106, V2-256, V2-286, V2-543. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_dual_agile_and_parry_shield_stack](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q14 -->

<!-- /ross-notes -->

<a id="Q15"></a>

### Q15 — Event key streams do not shift other events

- [x] **Executed** — Event key streams do not shift other events

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-017. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_event_key_streams_do_not_shift_other_events](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q15 -->

<!-- /ross-notes -->

<a id="Q16"></a>

### Q16 — Every hit stress no universal pin

- [x] **Executed** — Every hit stress no universal pin

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-114, V2-139. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_every_hit_stress_no_universal_pin](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q16 -->

<!-- /ross-notes -->

<a id="Q17"></a>

### Q17 — Ground aerial shutdown distinct

- [x] **Executed** — Ground aerial shutdown distinct

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-220. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_ground_aerial_shutdown_distinct](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q17 -->

<!-- /ross-notes -->

<a id="Q18"></a>

### Q18 — Gunfu and gunslinger are separate permissions

- [x] **Executed** — Gunfu and gunslinger are separate permissions

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-102, V2-318, V2-554. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_gunfu_and_gunslinger_are_separate_permissions](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q18 -->

<!-- /ross-notes -->

<a id="Q19"></a>

### Q19 — Large pool dp against brute

- [x] **Executed** — Large pool dp against brute

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-106, V2-102. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_large_pool_dp_against_brute](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q19 -->

<!-- /ross-notes -->

<a id="Q20"></a>

### Q20 — Legal rosters and invalid skill

- [x] **Executed** — Legal rosters and invalid skill

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-029, V2-034, V2-037, V2-305, V2-030, V2-031, V2-032, V2-033. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_legal_rosters_and_invalid_skill](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q20 -->

<!-- /ross-notes -->

<a id="Q21"></a>

### Q21 — Mark expiry is source start not round end

- [x] **Executed** — Mark expiry is source start not round end

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-316. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_mark_expiry_is_source_start_not_round_end](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q21 -->

<!-- /ross-notes -->

<a id="Q22"></a>

### Q22 — Mixed cancellation blocks unruled baseline

- [x] **Executed** — Mixed cancellation blocks unruled baseline

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-106. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_mixed_cancellation_blocks_unruled_baseline](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q22 -->

<!-- /ross-notes -->

<a id="Q23"></a>

### Q23 — Multi wounds and injury ignores stress

- [x] **Executed** — Multi wounds and injury ignores stress

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-114, V2-139. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_multi_wounds_and_injury_ignores_stress](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q23 -->

<!-- /ross-notes -->

<a id="Q24"></a>

### Q24 — Opposed extremes and no target

- [x] **Executed** — Opposed extremes and no target

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-023. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_opposed_extremes_and_no_target](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q24 -->

<!-- /ross-notes -->

<a id="Q25"></a>

### Q25 — Orders do not refresh

- [x] **Executed** — Orders do not refresh

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-485. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_orders_do_not_refresh](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q25 -->

<!-- /ross-notes -->

<a id="Q26"></a>

### Q26 — Piercing is best of not extra wound

- [x] **Executed** — Piercing is best of not extra wound

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-238, V2-298. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_piercing_is_best_of_not_extra_wound](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q26 -->

<!-- /ross-notes -->

<a id="Q27"></a>

### Q27 — Promotion boundary and skill unlock

- [x] **Executed** — Promotion boundary and skill unlock

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-392, V2-305. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_promotion_boundary_and_skill_unlock](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q27 -->

<!-- /ross-notes -->

<a id="Q28"></a>

### Q28 — Rage implode post attack stress

- [x] **Executed** — Rage implode post attack stress

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-313, V2-538. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_rage_implode_post_attack_stress](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q28 -->

<!-- /ross-notes -->

<a id="Q29"></a>

### Q29 — Reload and recovery costs

- [x] **Executed** — Reload and recovery costs

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-243, V2-117, V2-292. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_reload_and_recovery_costs](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q29 -->

<!-- /ross-notes -->

<a id="Q30"></a>

### Q30 — Remaining wound pins

- [x] **Executed** — Remaining wound pins

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-114. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_remaining_wound_pins](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q30 -->

<!-- /ross-notes -->

<a id="Q31"></a>

### Q31 — Return fire is simultaneous independent

- [x] **Executed** — Return fire is simultaneous independent

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-065, V2-097. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_return_fire_is_simultaneous_independent](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q31 -->

<!-- /ross-notes -->

<a id="Q32"></a>

### Q32 — Revive once consumption and activation history

- [x] **Executed** — Revive once consumption and activation history

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-126, V2-257, V2-055. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_revive_once_consumption_and_activation_history](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q32 -->

<!-- /ross-notes -->

<a id="Q33"></a>

### Q33 — Riposte does not chain counterattacks

- [x] **Executed** — Riposte does not chain counterattacks

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-531. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_riposte_does_not_chain_counterattacks](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q33 -->

<!-- /ross-notes -->

<a id="Q34"></a>

### Q34 — Shield ignored hit adds no stress

- [x] **Executed** — Shield ignored hit adds no stress

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-547. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_shield_ignored_hit_adds_no_stress](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q34 -->

<!-- /ross-notes -->

<a id="Q35"></a>

### Q35 — Tough as nails does not leave transferred hit stress

- [x] **Executed** — Tough as nails does not leave transferred hit stress

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-517, V2-343. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_tough_as_nails_does_not_leave_transferred_hit_stress](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q35 -->

<!-- /ross-notes -->

<a id="Q36"></a>

### Q36 — Unused starting stat points are lost not illegal

- [x] **Executed** — Unused starting stat points are lost not illegal

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-029. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_kernel.ContractTests.test_unused_starting_stat_points_are_lost_not_illegal](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_kernel.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_kernel.py>)

**Ross’s notes:**

<!-- ross-notes:Q36 -->

<!-- /ross-notes -->

<a id="Q37"></a>

### Q37 — Base to base range boundary

- [x] **Executed** — Base to base range boundary

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-007. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_base_to_base_range_boundary](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q37 -->

<!-- /ross-notes -->

<a id="Q38"></a>

### Q38 — Body and casualty los

- [x] **Executed** — Body and casualty los

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-074, V2-122. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_body_and_casualty_los](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q38 -->

<!-- /ross-notes -->

<a id="Q39"></a>

### Q39 — Charge stress not distance

- [x] **Executed** — Charge stress not distance

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-082. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_charge_stress_not_distance](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q39 -->

<!-- /ross-notes -->

<a id="Q40"></a>

### Q40 — Dive success and failure both pin

- [x] **Executed** — Dive success and failure both pin

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-065. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_dive_success_and_failure_both_pin](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q40 -->

<!-- /ross-notes -->

<a id="Q41"></a>

### Q41 — Drone operator deploy and control

- [x] **Executed** — Drone operator deploy and control

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-220, V2-544, V2-532. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_drone_operator_deploy_and_control](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q41 -->

<!-- /ross-notes -->

<a id="Q42"></a>

### Q42 — Fall ignores armour

- [x] **Executed** — Fall ignores armour

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-084. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_fall_ignores_armour](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q42 -->

<!-- /ross-notes -->

<a id="Q43"></a>

### Q43 — Fall over twelve no injury

- [x] **Executed** — Fall over twelve no injury

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-084. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_fall_over_twelve_no_injury](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q43 -->

<!-- /ross-notes -->

<a id="Q44"></a>

### Q44 — Forward arc and no free enemy turn pivot

- [x] **Executed** — Forward arc and no free enemy turn pivot

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-074, V2-061. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_forward_arc_and_no_free_enemy_turn_pivot](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q44 -->

<!-- /ross-notes -->

<a id="Q45"></a>

### Q45 — Friendly down witness requires facing and base range

- [x] **Executed** — Friendly down witness requires facing and base range

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-139, V2-074. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_friendly_down_witness_requires_facing_and_base_range](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q45 -->

<!-- /ross-notes -->

<a id="Q46"></a>

### Q46 — Half speed does not compound

- [x] **Executed** — Half speed does not compound

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-078, V2-090. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_half_speed_does_not_compound](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q46 -->

<!-- /ross-notes -->

<a id="Q47"></a>

### Q47 — Jump and safe drop boundaries

- [x] **Executed** — Jump and safe drop boundaries

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-084. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_jump_and_safe_drop_boundaries](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q47 -->

<!-- /ross-notes -->

<a id="Q48"></a>

### Q48 — Low cover and shooter hug exception

- [x] **Executed** — Low cover and shooter hug exception

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-049. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_low_cover_and_shooter_hug_exception](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q48 -->

<!-- /ross-notes -->

<a id="Q49"></a>

### Q49 — Narrow gap blocks base

- [x] **Executed** — Narrow gap blocks base

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-007, V2-078. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_narrow_gap_blocks_base](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q49 -->

<!-- /ross-notes -->

<a id="Q50"></a>

### Q50 — No corner cutting

- [x] **Executed** — No corner cutting

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-007, V2-078. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_no_corner_cutting](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q50 -->

<!-- /ross-notes -->

<a id="Q51"></a>

### Q51 — Ordinary move cannot engage

- [x] **Executed** — Ordinary move cannot engage

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-078, V2-093. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_ordinary_move_cannot_engage](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q51 -->

<!-- /ross-notes -->

<a id="Q52"></a>

### Q52 — Path detours and clearance

- [x] **Executed** — Path detours and clearance

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-007, V2-078. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_path_detours_and_clearance](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q52 -->

<!-- /ross-notes -->

<a id="Q53"></a>

### Q53 — Seeded path reachability all boards

- [x] **Executed** — Seeded path reachability all boards

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-044, V2-046. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_seeded_path_reachability_all_boards](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q53 -->

<!-- /ross-notes -->

<a id="Q54"></a>

### Q54 — Sprinter retains core

- [x] **Executed** — Sprinter retains core

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-331, V2-055. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_sprinter_retains_core](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q54 -->

<!-- /ross-notes -->

<a id="Q55"></a>

### Q55 — Terminal kit no los and neural uplink

- [x] **Executed** — Terminal kit no los and neural uplink

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-165, V2-261, V2-332, V2-190. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_terminal_kit_no_los_and_neural_uplink](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q55 -->

<!-- /ross-notes -->

<a id="Q56"></a>

### Q56 — Terminal nat one freeze

- [x] **Executed** — Terminal nat one freeze

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-165. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_terminal_nat_one_freeze](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q56 -->

<!-- /ross-notes -->

<a id="Q57"></a>

### Q57 — Terrain open close and repeated xp

- [x] **Executed** — Terrain open close and repeated xp

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-181, V2-389, V2-482. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_operations.SpatialTests.test_terrain_open_close_and_repeated_xp](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_operations.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_operations.py>)

**Ross’s notes:**

<!-- ross-notes:Q57 -->

<!-- /ross-notes -->

<a id="Q58"></a>

### Q58 — Controlled first assignment

- [x] **Executed** — Controlled first assignment

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-052. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_battle.BattleTests.test_controlled_first_assignment](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_battle.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_battle.py>)

**Ross’s notes:**

<!-- ross-notes:Q58 -->

<!-- /ross-notes -->

<a id="Q59"></a>

### Q59 — Every declared policy runs

- [x] **Executed** — Every declared policy runs

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-055. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_battle.BattleTests.test_every_declared_policy_runs](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_battle.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_battle.py>)

**Ross’s notes:**

<!-- ross-notes:Q59 -->

<!-- /ross-notes -->

<a id="Q60"></a>

### Q60 — Final checkpoint includes secondary vp

- [x] **Executed** — Final checkpoint includes secondary vp

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-073, V2-454. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_battle.BattleTests.test_final_checkpoint_includes_secondary_vp](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_battle.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_battle.py>)

**Ross’s notes:**

<!-- ross-notes:Q60 -->

<!-- /ross-notes -->

<a id="Q61"></a>

### Q61 — Four scenarios all families and sizes

- [x] **Executed** — Four scenarios all families and sizes

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-044, V2-454, V2-354. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_battle.BattleTests.test_four_scenarios_all_families_and_sizes](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_battle.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_battle.py>)

**Ross’s notes:**

<!-- ross-notes:Q61 -->

<!-- /ross-notes -->

<a id="Q62"></a>

### Q62 — Regression charge uses legal contact destination

- [x] **Executed** — Regression charge uses legal contact destination

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_battle.BattleTests.test_regression_charge_uses_legal_contact_destination](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_battle.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_battle.py>)

**Ross’s notes:**

<!-- ross-notes:Q62 -->

<!-- /ross-notes -->

<a id="Q63"></a>

### Q63 — Regression engaged actor does not shoot outside

- [x] **Executed** — Regression engaged actor does not shoot outside

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-093, V2-097. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_battle.BattleTests.test_regression_engaged_actor_does_not_shoot_outside](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_battle.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_battle.py>)

**Ross’s notes:**

<!-- ross-notes:Q63 -->

<!-- /ross-notes -->

<a id="Q64"></a>

### Q64 — Seed replay reproduction

- [x] **Executed** — Seed replay reproduction

#### Results

**Recorded result:** Passed the named assertions.

**Findings:** The specified boundary/transition/oracle comparison passed; no power or complete-owner conclusion is implied.

**Notes / remaining work:** Owners: V2-055, V2-052. This is one focused fixture. Exact inputs/assertions are in the corresponding test function.

**Evidence:** [master_rules_balance.test_battle.BattleTests.test_seed_replay_reproduction](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/conformance.txt>) · [test_battle.py](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/test-bench/master_rules_balance/test_battle.py>)

**Ross’s notes:**

<!-- ross-notes:Q64 -->

<!-- /ross-notes -->

## C. Every additional clause fixture

<a id="L01"></a>

### L01 — Inspire three targets

- [x] **Executed** — Inspire three targets

#### Results

**Recorded result:** Passed; {"stress": [2, 2, 2], "core": 0}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-340.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L01 -->

<!-- /ross-notes -->

<a id="L02"></a>

### L02 — Rally skill three broken

- [x] **Executed** — Rally skill three broken

#### Results

**Recorded result:** Passed; {"stress": [0, 0, 0], "core": 0}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-341;V2-150.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L02 -->

<!-- /ross-notes -->

<a id="L03"></a>

### L03 — Brace penalty lock and expiry

- [x] **Executed** — Brace penalty lock and expiry

#### Results

**Recorded result:** Passed; {"incoming_modifier": -1, "expires": "source next activation start"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-311.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L03 -->

<!-- /ross-notes -->

<a id="L04"></a>

### L04 — Coordination extra move and delayed stress

- [x] **Executed** — Coordination extra move and delayed stress

#### Results

**Recorded result:** Passed; {"extra_move": 1, "stress_timing": "after recipient activation"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-536.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L04 -->

<!-- /ross-notes -->

<a id="L05"></a>

### L05 — Motivate two core attacks

- [x] **Executed** — Motivate two core attacks

#### Results

**Recorded result:** Passed; {"attacks": 2, "core_remaining": 0}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-342;V2-055.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L05 -->

<!-- /ross-notes -->

<a id="L06"></a>

### L06 — Big aura capacity radius transfer and down

- [x] **Executed** — Big aura capacity radius transfer and down

#### Results

**Recorded result:** Passed; {"maximum_active": 2, "diameter": 9, "transferred": 4, "down_clears": true, "legality": "ANALYTICAL four NRV skills exceeds normal per-Stat three; isolates aura-capacity mechanics only"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-343;V2-344;V2-539;V2-541.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L06 -->

<!-- /ross-notes -->

<a id="L07"></a>

### L07 — Legal big aura two aura loadout

- [x] **Executed** — Legal big aura two aura loadout

#### Results

**Recorded result:** Passed; {"legal_starting_actor": true, "active": 2}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-541;V2-305.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L07 -->

<!-- /ross-notes -->

<a id="L08"></a>

### L08 — Doc free dose and cocktail recipient limit

- [x] **Executed** — Doc free dose and cocktail recipient limit

#### Results

**Recorded result:** Passed; {"doses": 2, "core_spent": 1, "free_dose_consumed": true}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-337;V2-535;V2-270.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L08 -->

<!-- /ross-notes -->

<a id="L09"></a>

### L09 — Stabilize revival clears stress

- [x] **Executed** — Stabilize revival clears stress

#### Results

**Recorded result:** Passed; {"patient_stress": 0, "pinned": true}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-336;V2-126.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L09 -->

<!-- /ross-notes -->

<a id="L10"></a>

### L10 — Ghost phantom nonwound stress

- [x] **Executed** — Ghost phantom nonwound stress

#### Results

**Recorded result:** Passed; {"hidden": true, "target_stress": 2, "pinned": false}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-326;V2-527.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L10 -->

<!-- /ross-notes -->

<a id="L11"></a>

### L11 — Headshot single die mark bonus

- [x] **Executed** — Headshot single die mark bonus

#### Results

**Recorded result:** Passed; {"injury_modifier": 4, "requires_mark_and_no_move": true}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-317.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L11 -->

<!-- /ross-notes -->

<a id="L12"></a>

### L12 — Big fella removes unwieldy

- [x] **Executed** — Big fella removes unwieldy

#### Results

**Recorded result:** Passed; {"moved_modifier_before": 1, "after": 3}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-315;V2-245.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L12 -->

<!-- /ross-notes -->

<a id="L13"></a>

### L13 — Goliath full eligible twohanded pool

- [x] **Executed** — Goliath full eligible twohanded pool

#### Results

**Recorded result:** Passed; {"base_atk": 2, "charge_atk": 3}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-520;V2-102.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L13 -->

<!-- /ross-notes -->

<a id="L14"></a>

### L14 — Planning ahead uses one active profile

- [x] **Executed** — Planning ahead uses one active profile

#### Results

**Recorded result:** Passed; {"active": "Sniper rifle", "simultaneous": false}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-524.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L14 -->

<!-- /ross-notes -->

<a id="L15"></a>

### L15 — Inspector slots and identical vest effect

- [x] **Executed** — Inspector slots and identical vest effect

#### Results

**Recorded result:** Passed; {"three_items_allowed": true, "identical_vests_do_not_stack": true}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-338;V2-499;V2-007.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L15 -->

<!-- /ross-notes -->

<a id="L16"></a>

### L16 — Deploy assignment v2-212

- [x] **Executed** — Deploy assignment v2-212

#### Results

**Recorded result:** Passed; {"profile": "Seeker mine", "assigned_slot_retained": true, "ability_coverage": "DEPLOYMENT ONLY; full printed effects remain unverified"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-212;V2-202.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L16 -->

<!-- /ross-notes -->

<a id="L17"></a>

### L17 — Deploy assignment v2-213

- [x] **Executed** — Deploy assignment v2-213

#### Results

**Recorded result:** Passed; {"profile": "Smoke emitter", "assigned_slot_retained": true, "ability_coverage": "DEPLOYMENT ONLY; full printed effects remain unverified"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-213;V2-202.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L17 -->

<!-- /ross-notes -->

<a id="L18"></a>

### L18 — Deploy assignment v2-215

- [x] **Executed** — Deploy assignment v2-215

#### Results

**Recorded result:** Passed; {"profile": "Sentry turret", "assigned_slot_retained": true, "ability_coverage": "DEPLOYMENT ONLY; full printed effects remain unverified"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-215;V2-202.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L18 -->

<!-- /ross-notes -->

<a id="L19"></a>

### L19 — Deploy assignment v2-544

- [x] **Executed** — Deploy assignment v2-544

#### Results

**Recorded result:** Passed; {"profile": "Surveillance drone", "assigned_slot_retained": true, "ability_coverage": "DEPLOYMENT ONLY; full printed effects remain unverified"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-544;V2-220.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L19 -->

<!-- /ross-notes -->

<a id="L20"></a>

### L20 — Deploy assignment v2-545

- [x] **Executed** — Deploy assignment v2-545

#### Results

**Recorded result:** Passed; {"profile": "Bomber drone", "assigned_slot_retained": true, "ability_coverage": "DEPLOYMENT ONLY; full printed effects remain unverified"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-545;V2-220.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L20 -->

<!-- /ross-notes -->

<a id="L21"></a>

### L21 — Deploy assignment v2-546

- [x] **Executed** — Deploy assignment v2-546

#### Results

**Recorded result:** Passed; {"profile": "Gunner drone", "assigned_slot_retained": true, "ability_coverage": "DEPLOYMENT ONLY; full printed effects remain unverified"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-546;V2-220.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L21 -->

<!-- /ross-notes -->

<a id="L22"></a>

### L22 — Deploy assignment v2-547

- [x] **Executed** — Deploy assignment v2-547

#### Results

**Recorded result:** Passed; {"profile": "Shield drone", "assigned_slot_retained": true, "ability_coverage": "DEPLOYMENT ONLY; full printed effects remain unverified"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-547;V2-220.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L22 -->

<!-- /ross-notes -->

<a id="L23"></a>

### L23 — Deploy assignment v2-548

- [x] **Executed** — Deploy assignment v2-548

#### Results

**Recorded result:** Passed; {"profile": "Breacher drone", "assigned_slot_retained": true, "ability_coverage": "DEPLOYMENT ONLY; full printed effects remain unverified"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-548;V2-220.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L23 -->

<!-- /ross-notes -->

<a id="L24"></a>

### L24 — Deploy assignment v2-549

- [x] **Executed** — Deploy assignment v2-549

#### Results

**Recorded result:** Passed; {"profile": "Support drone", "assigned_slot_retained": true, "ability_coverage": "DEPLOYMENT ONLY; full printed effects remain unverified"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-549;V2-220.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L24 -->

<!-- /ross-notes -->

<a id="L25"></a>

### L25 — Deploy assignment v2-550

- [x] **Executed** — Deploy assignment v2-550

#### Results

**Recorded result:** Passed; {"profile": "Cloaking field", "assigned_slot_retained": true, "ability_coverage": "DEPLOYMENT ONLY; full printed effects remain unverified"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-550;V2-202.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L25 -->

<!-- /ross-notes -->

<a id="L26"></a>

### L26 — Deploy assignment v2-551

- [x] **Executed** — Deploy assignment v2-551

#### Results

**Recorded result:** Passed; {"profile": "Decoy mine", "assigned_slot_retained": true, "ability_coverage": "DEPLOYMENT ONLY; full printed effects remain unverified"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-551;V2-202.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L26 -->

<!-- /ross-notes -->

<a id="L27"></a>

### L27 — Fire failed check escalation

- [x] **Executed** — Fire failed check escalation

#### Results

**Recorded result:** Passed; {"failed_checks": 3, "states": "Pinned+skip, Down, Unconscious", "limitation": "Initial/random/water-directed fire movement not covered"}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-498.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L27 -->

<!-- /ross-notes -->

<a id="L28"></a>

### L28 — Poison application round and natural move threshold

- [x] **Executed** — Poison application round and natural move threshold

#### Results

**Recorded result:** Passed; {"application_round_no_extra_loss": true, "unconscious_round": 3}

**Findings:** Only the recorded owner clauses were checked.

**Notes / remaining work:** NAMED CLAUSE ONLY; not complete owner/tactical/crew conformance Owners: V2-498.

**Evidence:** [assertions.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/assertions.csv>) · [events.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/clause-fixtures/events.json>)

**Ross’s notes:**

<!-- ross-notes:L28 -->

<!-- /ross-notes -->

## D. Paired tactical contexts and fresh-seed confirmation

<a id="TS01"></a>

### TS01 — Rage implode; Stress 0; Armour 0; Charge bonus 0

- [x] **Executed** — Rage implode; Stress 0; Armour 0; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.80%, treatment 0.80%; difference +0.00 pp (95% -17.18 pp to +17.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0240; attacker retained Stress differs by +3.0920. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026150000–2026150249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS01 -->

<!-- /ross-notes -->

<a id="TS02"></a>

### TS02 — Rage implode; Stress 0; Armour 0; Charge bonus 1

- [x] **Executed** — Rage implode; Stress 0; Armour 0; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.80%, treatment 2.00%; difference +1.20 pp (95% -15.98 pp to +18.38 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0640; attacker retained Stress differs by +3.0600. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026160000–2026160249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS02 -->

<!-- /ross-notes -->

<a id="TS03"></a>

### TS03 — Rage implode; Stress 0; Standard armour; Charge bonus 0

- [x] **Executed** — Rage implode; Stress 0; Standard armour; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.40%; difference +0.40 pp (95% -16.78 pp to +17.58 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0160; attacker retained Stress differs by +3.0920. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026170000–2026170249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS03 -->

<!-- /ross-notes -->

<a id="TS04"></a>

### TS04 — Rage implode; Stress 0; Standard armour; Charge bonus 1

- [x] **Executed** — Rage implode; Stress 0; Standard armour; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.40%, treatment 0.80%; difference +0.40 pp (95% -16.78 pp to +17.58 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0400; attacker retained Stress differs by +3.1000. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026180000–2026180249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS04 -->

<!-- /ross-notes -->

<a id="TS05"></a>

### TS05 — Rage implode; Stress 0; Reinforced armour; Charge bonus 0

- [x] **Executed** — Rage implode; Stress 0; Reinforced armour; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.00%; difference +0.00 pp (95% -17.18 pp to +17.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0240; attacker retained Stress differs by +3.0760. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026190000–2026190249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS05 -->

<!-- /ross-notes -->

<a id="TS06"></a>

### TS06 — Rage implode; Stress 0; Reinforced armour; Charge bonus 1

- [x] **Executed** — Rage implode; Stress 0; Reinforced armour; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.00%; difference +0.00 pp (95% -17.18 pp to +17.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0480; attacker retained Stress differs by +3.0880. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026200000–2026200249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS06 -->

<!-- /ross-notes -->

<a id="TS07"></a>

### TS07 — Rage implode; Stress 2; Armour 0; Charge bonus 0

- [x] **Executed** — Rage implode; Stress 2; Armour 0; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.40%, treatment 0.40%; difference +0.00 pp (95% -17.18 pp to +17.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0200; attacker retained Stress differs by +2.1920. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026210000–2026210249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS07 -->

<!-- /ross-notes -->

<a id="TS08"></a>

### TS08 — Rage implode; Stress 2; Armour 0; Charge bonus 1

- [x] **Executed** — Rage implode; Stress 2; Armour 0; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 2.00%, treatment 2.80%; difference +0.80 pp (95% -16.38 pp to +17.98 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0840; attacker retained Stress differs by +2.1040. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026220000–2026220249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS08 -->

<!-- /ross-notes -->

<a id="TS09"></a>

### TS09 — Rage implode; Stress 2; Standard armour; Charge bonus 0

- [x] **Executed** — Rage implode; Stress 2; Standard armour; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.40%; difference +0.40 pp (95% -16.78 pp to +17.58 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0360; attacker retained Stress differs by +2.1160. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026230000–2026230249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS09 -->

<!-- /ross-notes -->

<a id="TS10"></a>

### TS10 — Rage implode; Stress 2; Standard armour; Charge bonus 1

- [x] **Executed** — Rage implode; Stress 2; Standard armour; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.40%; difference +0.40 pp (95% -16.78 pp to +17.58 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0600; attacker retained Stress differs by +2.1160. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026240000–2026240249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS10 -->

<!-- /ross-notes -->

<a id="TS11"></a>

### TS11 — Rage implode; Stress 2; Reinforced armour; Charge bonus 0

- [x] **Executed** — Rage implode; Stress 2; Reinforced armour; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.00%; difference +0.00 pp (95% -17.18 pp to +17.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0680; attacker retained Stress differs by +2.1280. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026250000–2026250249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS11 -->

<!-- /ross-notes -->

<a id="TS12"></a>

### TS12 — Rage implode; Stress 2; Reinforced armour; Charge bonus 1

- [x] **Executed** — Rage implode; Stress 2; Reinforced armour; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.40%; difference +0.40 pp (95% -16.78 pp to +17.58 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0760; attacker retained Stress differs by +2.1120. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026260000–2026260249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS12 -->

<!-- /ross-notes -->

<a id="TS13"></a>

### TS13 — Rage implode; Stress 4; Armour 0; Charge bonus 0

- [x] **Executed** — Rage implode; Stress 4; Armour 0; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.00%; difference +0.00 pp (95% -17.18 pp to +17.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0320; attacker retained Stress differs by +1.2000. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026270000–2026270249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS13 -->

<!-- /ross-notes -->

<a id="TS14"></a>

### TS14 — Rage implode; Stress 4; Armour 0; Charge bonus 1

- [x] **Executed** — Rage implode; Stress 4; Armour 0; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.40%, treatment 2.80%; difference +2.40 pp (95% -14.78 pp to +19.58 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0960; attacker retained Stress differs by +1.1440. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026280000–2026280249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS14 -->

<!-- /ross-notes -->

<a id="TS15"></a>

### TS15 — Rage implode; Stress 4; Standard armour; Charge bonus 0

- [x] **Executed** — Rage implode; Stress 4; Standard armour; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.00%; difference +0.00 pp (95% -17.18 pp to +17.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0360; attacker retained Stress differs by +1.2000. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026290000–2026290249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS15 -->

<!-- /ross-notes -->

<a id="TS16"></a>

### TS16 — Rage implode; Stress 4; Standard armour; Charge bonus 1

- [x] **Executed** — Rage implode; Stress 4; Standard armour; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.80%, treatment 2.00%; difference +1.20 pp (95% -15.98 pp to +18.38 pp).

**Findings:** Potential Injury successes per exchange differ by +0.1200; attacker retained Stress differs by +1.1720. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026300000–2026300249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS16 -->

<!-- /ross-notes -->

<a id="TS17"></a>

### TS17 — Rage implode; Stress 4; Reinforced armour; Charge bonus 0

- [x] **Executed** — Rage implode; Stress 4; Reinforced armour; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.40%, treatment 0.40%; difference +0.00 pp (95% -17.18 pp to +17.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0280; attacker retained Stress differs by +1.1760. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026310000–2026310249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS17 -->

<!-- /ross-notes -->

<a id="TS18"></a>

### TS18 — Rage implode; Stress 4; Reinforced armour; Charge bonus 1

- [x] **Executed** — Rage implode; Stress 4; Reinforced armour; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.00%; difference +0.00 pp (95% -17.18 pp to +17.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0920; attacker retained Stress differs by +1.1400. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026320000–2026320249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS18 -->

<!-- /ross-notes -->

<a id="TS19"></a>

### TS19 — Dual swords vs sword shield; Stress 0; Armour 0; Charge bonus 0

- [x] **Executed** — Dual swords vs sword shield; Stress 0; Armour 0; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 2.40%; difference +2.40 pp (95% -14.78 pp to +19.58 pp).

**Findings:** Potential Injury successes per exchange differ by +0.1600; attacker retained Stress differs by -0.0480. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026330000–2026330249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS19 -->

<!-- /ross-notes -->

<a id="TS20"></a>

### TS20 — Dual swords vs sword shield; Stress 0; Armour 0; Charge bonus 1

- [x] **Executed** — Dual swords vs sword shield; Stress 0; Armour 0; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 1.20%, treatment 9.20%; difference +8.00 pp (95% -9.18 pp to +25.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.2160; attacker retained Stress differs by -0.0400. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026340000–2026340249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS20 -->

<!-- /ross-notes -->

<a id="TS21"></a>

### TS21 — Dual swords vs sword shield; Stress 0; Standard armour; Charge bonus 0

- [x] **Executed** — Dual swords vs sword shield; Stress 0; Standard armour; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 1.60%; difference +1.60 pp (95% -15.58 pp to +18.78 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0880; attacker retained Stress differs by -0.0560. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026350000–2026350249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS21 -->

<!-- /ross-notes -->

<a id="TS22"></a>

### TS22 — Dual swords vs sword shield; Stress 0; Standard armour; Charge bonus 1

- [x] **Executed** — Dual swords vs sword shield; Stress 0; Standard armour; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.40%, treatment 1.20%; difference +0.80 pp (95% -16.38 pp to +17.98 pp).

**Findings:** Potential Injury successes per exchange differ by +0.1480; attacker retained Stress differs by -0.0600. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026360000–2026360249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS22 -->

<!-- /ross-notes -->

<a id="TS23"></a>

### TS23 — Dual swords vs sword shield; Stress 0; Reinforced armour; Charge bonus 0

- [x] **Executed** — Dual swords vs sword shield; Stress 0; Reinforced armour; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.40%; difference +0.40 pp (95% -16.78 pp to +17.58 pp).

**Findings:** Potential Injury successes per exchange differ by +0.1120; attacker retained Stress differs by -0.0560. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026370000–2026370249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS23 -->

<!-- /ross-notes -->

<a id="TS24"></a>

### TS24 — Dual swords vs sword shield; Stress 0; Reinforced armour; Charge bonus 1

- [x] **Executed** — Dual swords vs sword shield; Stress 0; Reinforced armour; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.40%, treatment 1.20%; difference +0.80 pp (95% -16.38 pp to +17.98 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0680; attacker retained Stress differs by -0.0440. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026380000–2026380249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS24 -->

<!-- /ross-notes -->

<a id="TS25"></a>

### TS25 — Dual swords vs sword shield; Stress 2; Armour 0; Charge bonus 0

- [x] **Executed** — Dual swords vs sword shield; Stress 2; Armour 0; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.80%, treatment 4.80%; difference +4.00 pp (95% -13.18 pp to +21.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.2120; attacker retained Stress differs by -0.0440. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026390000–2026390249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS25 -->

<!-- /ross-notes -->

<a id="TS26"></a>

### TS26 — Dual swords vs sword shield; Stress 2; Armour 0; Charge bonus 1

- [x] **Executed** — Dual swords vs sword shield; Stress 2; Armour 0; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 2.00%, treatment 8.00%; difference +6.00 pp (95% -11.18 pp to +23.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.2600; attacker retained Stress differs by -0.0400. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026400000–2026400249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS26 -->

<!-- /ross-notes -->

<a id="TS27"></a>

### TS27 — Dual swords vs sword shield; Stress 2; Standard armour; Charge bonus 0

- [x] **Executed** — Dual swords vs sword shield; Stress 2; Standard armour; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.80%; difference +0.80 pp (95% -16.38 pp to +17.98 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0800; attacker retained Stress differs by -0.0680. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026410000–2026410249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS27 -->

<!-- /ross-notes -->

<a id="TS28"></a>

### TS28 — Dual swords vs sword shield; Stress 2; Standard armour; Charge bonus 1

- [x] **Executed** — Dual swords vs sword shield; Stress 2; Standard armour; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 1.20%, treatment 3.20%; difference +2.00 pp (95% -15.18 pp to +19.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.1240; attacker retained Stress differs by -0.0600. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026420000–2026420249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS28 -->

<!-- /ross-notes -->

<a id="TS29"></a>

### TS29 — Dual swords vs sword shield; Stress 2; Reinforced armour; Charge bonus 0

- [x] **Executed** — Dual swords vs sword shield; Stress 2; Reinforced armour; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.40%; difference +0.40 pp (95% -16.78 pp to +17.58 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0560; attacker retained Stress differs by -0.0840. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026430000–2026430249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS29 -->

<!-- /ross-notes -->

<a id="TS30"></a>

### TS30 — Dual swords vs sword shield; Stress 2; Reinforced armour; Charge bonus 1

- [x] **Executed** — Dual swords vs sword shield; Stress 2; Reinforced armour; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.40%; difference +0.40 pp (95% -16.78 pp to +17.58 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0680; attacker retained Stress differs by -0.0680. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026440000–2026440249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS30 -->

<!-- /ross-notes -->

<a id="TS31"></a>

### TS31 — Dual swords vs sword shield; Stress 4; Armour 0; Charge bonus 0

- [x] **Executed** — Dual swords vs sword shield; Stress 4; Armour 0; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.40%, treatment 3.20%; difference +2.80 pp (95% -14.38 pp to +19.98 pp).

**Findings:** Potential Injury successes per exchange differ by +0.1440; attacker retained Stress differs by -0.0680. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026450000–2026450249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS31 -->

<!-- /ross-notes -->

<a id="TS32"></a>

### TS32 — Dual swords vs sword shield; Stress 4; Armour 0; Charge bonus 1

- [x] **Executed** — Dual swords vs sword shield; Stress 4; Armour 0; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 2.40%; difference +2.40 pp (95% -14.78 pp to +19.58 pp).

**Findings:** Potential Injury successes per exchange differ by +0.1880; attacker retained Stress differs by -0.0760. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026460000–2026460249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS32 -->

<!-- /ross-notes -->

<a id="TS33"></a>

### TS33 — Dual swords vs sword shield; Stress 4; Standard armour; Charge bonus 0

- [x] **Executed** — Dual swords vs sword shield; Stress 4; Standard armour; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.40%; difference +0.40 pp (95% -16.78 pp to +17.58 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0560; attacker retained Stress differs by -0.0720. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026470000–2026470249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS33 -->

<!-- /ross-notes -->

<a id="TS34"></a>

### TS34 — Dual swords vs sword shield; Stress 4; Standard armour; Charge bonus 1

- [x] **Executed** — Dual swords vs sword shield; Stress 4; Standard armour; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.80%, treatment 2.00%; difference +1.20 pp (95% -15.98 pp to +18.38 pp).

**Findings:** Potential Injury successes per exchange differ by +0.1320; attacker retained Stress differs by -0.0560. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026480000–2026480249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS34 -->

<!-- /ross-notes -->

<a id="TS35"></a>

### TS35 — Dual swords vs sword shield; Stress 4; Reinforced armour; Charge bonus 0

- [x] **Executed** — Dual swords vs sword shield; Stress 4; Reinforced armour; Charge bonus 0

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.00%; difference +0.00 pp (95% -17.18 pp to +17.18 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0560; attacker retained Stress differs by -0.0560. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026490000–2026490249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS35 -->

<!-- /ross-notes -->

<a id="TS36"></a>

### TS36 — Dual swords vs sword shield; Stress 4; Reinforced armour; Charge bonus 1

- [x] **Executed** — Dual swords vs sword shield; Stress 4; Reinforced armour; Charge bonus 1

#### Results

**Recorded result:** 250 independent seed pairs. Target Down: control 0.00%, treatment 0.80%; difference +0.80 pp (95% -16.38 pp to +17.98 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0440; attacker retained Stress differs by -0.0960. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026500000–2026500249. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [paired-screen.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/paired-screen.csv>)

**Ross’s notes:**

<!-- ross-notes:TS36 -->

<!-- /ross-notes -->

<a id="TC01"></a>

### TC01 — Rage implode; Stress 4; Standard armour; Charge bonus 0

- [x] **Executed** — Rage implode; Stress 4; Standard armour; Charge bonus 0

#### Results

**Recorded result:** 1000 independent seed pairs. Target Down: control 0.20%, treatment 0.20%; difference +0.00 pp (95% -8.59 pp to +8.59 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0410; attacker retained Stress differs by +1.1670. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026900000–2026900999. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [fixed-confirmation.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/fixed-confirmation.csv>)

**Ross’s notes:**

<!-- ross-notes:TC01 -->

<!-- /ross-notes -->

<a id="TC02"></a>

### TC02 — Rage implode; Stress 4; Reinforced armour; Charge bonus 0

- [x] **Executed** — Rage implode; Stress 4; Reinforced armour; Charge bonus 0

#### Results

**Recorded result:** 1000 independent seed pairs. Target Down: control 0.00%, treatment 0.20%; difference +0.20 pp (95% -8.39 pp to +8.79 pp).

**Findings:** Potential Injury successes per exchange differ by +0.0500; attacker retained Stress differs by +1.1670. No crew-dominance conclusion.

**Notes / remaining work:** Conditional initiating melee exchange; target may Riposte; movement, activation and crew contributions excluded. Seeds 2026910000–2026910999. Target may Riposte; price verification deferred. Paired differences, not arms, are the independent samples.

**Evidence:** [fixed-confirmation.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/fixed-confirmation.csv>)

**Ross’s notes:**

<!-- ross-notes:TC02 -->

<!-- /ross-notes -->

<a id="TS37"></a>

### TS37 — High-risk stat/skill feasibility search

- [x] **Executed** — High-risk stat/skill feasibility search

#### Results

**Recorded result:** 180 candidate sets; 171 stat/skill feasible; 9 blocked by caps.

**Findings:** Feasibility is separate from measured strength. More than three associated skills would require a Stat above 6.

**Notes / remaining work:** The search uses Unarmed/no-gear actors to isolate stat/skill legality. Full loadout/operator/action validation and best-response power search remain.

**Evidence:** [legal-high-risk-builds.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/targeted/legal-high-risk-builds.csv>)

**Ross’s notes:**

<!-- ross-notes:TS37 -->

<!-- /ross-notes -->

## E. Every full-battle comparison cell

<a id="BS01"></a>

### BS01 — mirror-chokepoints — matched mirror

- [x] **Executed** — mirror-chokepoints — matched mirror

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 54.37%, conservative 95% 40.79%–67.96%. Wins/draws/losses: 170/95/135.

**Findings:** Mirror diagnostic; deviation from 50% is not an asymmetric upgrade value. Focal first/second scores: 55.25%/53.50%.

**Notes / remaining work:** v2; board chokepoints-0; scenario recover; size 9; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-chokepoints/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-chokepoints/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-chokepoints/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| Occupied destination | 3469 |
| goal_unreachable_dynamic | 3762 |
| mark_has_fewer_than_two_ready_shooters | 948 |
| flight_no_safe_legal_destination | 209 |
| approach_requires_charge | 195 |

**Ross’s notes:**

<!-- ross-notes:BS01 -->

<!-- /ross-notes -->

<a id="BS02"></a>

### BS02 — mirror-contested_machinery — matched mirror

- [x] **Executed** — mirror-contested_machinery — matched mirror

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 46.50%, conservative 95% 32.92%–60.08%. Wins/draws/losses: 177/18/205.

**Findings:** Mirror diagnostic; deviation from 50% is not an asymmetric upgrade value. Focal first/second scores: 46.75%/46.25%.

**Notes / remaining work:** v2; board contested_machinery-0; scenario control; size 6; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-contested_machinery/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-contested_machinery/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-contested_machinery/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| goal_unreachable_dynamic | 4340 |
| Occupied destination | 1750 |
| mark_has_fewer_than_two_ready_shooters | 1061 |
| approach_requires_charge | 54 |
| flight_no_safe_legal_destination | 4 |

**Ross’s notes:**

<!-- ross-notes:BS02 -->

<!-- /ross-notes -->

<a id="BS03"></a>

### BS03 — mirror-dense_urban — matched mirror

- [x] **Executed** — mirror-dense_urban — matched mirror

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 50.12%, conservative 95% 36.54%–63.71%. Wins/draws/losses: 177/47/176.

**Findings:** Mirror diagnostic; deviation from 50% is not an asymmetric upgrade value. Focal first/second scores: 50.50%/49.75%.

**Notes / remaining work:** v2; board dense_urban-0; scenario control; size 4; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-dense_urban/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-dense_urban/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-dense_urban/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 2981 |
| Occupied destination | 1638 |
| goal_unreachable_dynamic | 338 |
| approach_requires_charge | 404 |

**Ross’s notes:**

<!-- ross-notes:BS03 -->

<!-- /ross-notes -->

<a id="BS04"></a>

### BS04 — mirror-industrial_vertical — matched mirror

- [x] **Executed** — mirror-industrial_vertical — matched mirror

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 49.75%, conservative 95% 36.17%–63.33%. Wins/draws/losses: 130/138/132.

**Findings:** Mirror diagnostic; deviation from 50% is not an asymmetric upgrade value. Focal first/second scores: 49.75%/49.75%.

**Notes / remaining work:** v2; board industrial_vertical-0; scenario recover; size 6; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-industrial_vertical/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-industrial_vertical/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-industrial_vertical/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| goal_unreachable_dynamic | 4428 |
| Occupied destination | 1922 |
| mark_has_fewer_than_two_ready_shooters | 1054 |
| approach_requires_charge | 172 |
| flight_no_safe_legal_destination | 6 |
| Only Charge can enter engagement | 2 |

**Ross’s notes:**

<!-- ross-notes:BS04 -->

<!-- /ross-notes -->

<a id="BS05"></a>

### BS05 — mirror-interior_compound — matched mirror

- [x] **Executed** — mirror-interior_compound — matched mirror

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 51.12%, conservative 95% 37.54%–64.71%. Wins/draws/losses: 172/65/163.

**Findings:** Mirror diagnostic; deviation from 50% is not an asymmetric upgrade value. Focal first/second scores: 50.25%/52.00%.

**Notes / remaining work:** v2; board interior_compound-0; scenario network; size 9; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-interior_compound/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-interior_compound/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-interior_compound/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| approach_requires_charge | 180 |
| mark_has_fewer_than_two_ready_shooters | 955 |
| goal_unreachable_dynamic | 5578 |
| Occupied destination | 6015 |
| flight_no_safe_legal_destination | 56 |

**Ross’s notes:**

<!-- ross-notes:BS05 -->

<!-- /ross-notes -->

<a id="BS06"></a>

### BS06 — mirror-long_lanes — matched mirror

- [x] **Executed** — mirror-long_lanes — matched mirror

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 46.38%, conservative 95% 32.79%–59.96%. Wins/draws/losses: 167/37/196.

**Findings:** Mirror diagnostic; deviation from 50% is not an asymmetric upgrade value. Focal first/second scores: 50.00%/42.75%.

**Notes / remaining work:** v2; board long_lanes-0; scenario breakthrough; size 4; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-long_lanes/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-long_lanes/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/mirror-long_lanes/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 1994 |
| approach_requires_charge | 655 |
| Occupied destination | 40 |
| flight_no_safe_legal_destination | 17 |

**Ross’s notes:**

<!-- ross-notes:BS06 -->

<!-- /ross-notes -->

<a id="BS07"></a>

### BS07 — screen-chokepoints-0 — Assault rifle

- [x] **Executed** — screen-chokepoints-0 — Assault rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 51.38%, conservative 95% 37.79%–64.96%. Wins/draws/losses: 199/13/188.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 53.00%/49.75%.

**Notes / remaining work:** v2; board chokepoints-0; scenario control; size 9; policy pressure. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-chokepoints-0/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-chokepoints-0/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-chokepoints-0/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| approach_requires_charge | 1215 |
| goal_unreachable_dynamic | 4707 |
| mark_has_fewer_than_two_ready_shooters | 2171 |
| Occupied destination | 5222 |
| flight_no_safe_legal_destination | 140 |

**Ross’s notes:**

<!-- ross-notes:BS07 -->

<!-- /ross-notes -->

<a id="BS08"></a>

### BS08 — screen-chokepoints-1 — Sniper rifle

- [x] **Executed** — screen-chokepoints-1 — Sniper rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 59.75%, conservative 95% 46.17%–73.33%. Wins/draws/losses: 116/246/38.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 59.75%/59.75%.

**Notes / remaining work:** v2; board chokepoints-1; scenario recover; size 4; policy cautious. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-chokepoints-1/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-chokepoints-1/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-chokepoints-1/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| cautious_holds_firing_position | 3646 |
| mark_has_fewer_than_two_ready_shooters | 1113 |
| Occupied destination | 292 |
| goal_unreachable_dynamic | 273 |
| flight_no_safe_legal_destination | 4 |
| approach_requires_charge | 2 |

**Ross’s notes:**

<!-- ross-notes:BS08 -->

<!-- /ross-notes -->

<a id="BS09"></a>

### BS09 — screen-chokepoints-2 — Reinforced armour

- [x] **Executed** — screen-chokepoints-2 — Reinforced armour

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 17.00%, conservative 95% 3.42%–30.58%. Wins/draws/losses: 38/60/302.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 17.00%/17.00%.

**Notes / remaining work:** v2; board chokepoints-2; scenario network; size 6; policy flank. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-chokepoints-2/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-chokepoints-2/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-chokepoints-2/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| goal_unreachable_dynamic | 7522 |
| mark_has_fewer_than_two_ready_shooters | 950 |
| Occupied destination | 2234 |

**Ross’s notes:**

<!-- ross-notes:BS09 -->

<!-- /ross-notes -->

<a id="BS10"></a>

### BS10 — screen-chokepoints-3 — Pin Them Down replacement

- [x] **Executed** — screen-chokepoints-3 — Pin Them Down replacement

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 51.25%, conservative 95% 37.67%–64.83%. Wins/draws/losses: 179/52/169.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 47.00%/55.50%.

**Notes / remaining work:** v2; board chokepoints-0; scenario breakthrough; size 9; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-chokepoints-3/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-chokepoints-3/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-chokepoints-3/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| Occupied destination | 1535 |
| approach_requires_charge | 4982 |
| mark_has_fewer_than_two_ready_shooters | 739 |
| flight_no_safe_legal_destination | 215 |
| Only Charge can enter engagement | 1 |

**Ross’s notes:**

<!-- ross-notes:BS10 -->

<!-- /ross-notes -->

<a id="BS11"></a>

### BS11 — screen-contested_machinery-0 — Assault rifle

- [x] **Executed** — screen-contested_machinery-0 — Assault rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 49.00%, conservative 95% 35.42%–62.58%. Wins/draws/losses: 186/20/194.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 49.00%/49.00%.

**Notes / remaining work:** v2; board contested_machinery-0; scenario control; size 6; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-contested_machinery-0/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-contested_machinery-0/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-contested_machinery-0/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| goal_unreachable_dynamic | 4072 |
| mark_has_fewer_than_two_ready_shooters | 1060 |
| Occupied destination | 1811 |
| approach_requires_charge | 24 |
| flight_no_safe_legal_destination | 6 |

**Ross’s notes:**

<!-- ross-notes:BS11 -->

<!-- /ross-notes -->

<a id="BS12"></a>

### BS12 — screen-contested_machinery-1 — Sniper rifle

- [x] **Executed** — screen-contested_machinery-1 — Sniper rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 58.50%, conservative 95% 44.92%–72.08%. Wins/draws/losses: 195/78/127.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 59.25%/57.75%.

**Notes / remaining work:** v2; board contested_machinery-1; scenario recover; size 9; policy pressure. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-contested_machinery-1/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-contested_machinery-1/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-contested_machinery-1/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| goal_unreachable_dynamic | 4789 |
| Occupied destination | 2587 |
| approach_requires_charge | 218 |
| flight_no_safe_legal_destination | 86 |
| mark_has_fewer_than_two_ready_shooters | 110 |

**Ross’s notes:**

<!-- ross-notes:BS12 -->

<!-- /ross-notes -->

<a id="BS13"></a>

### BS13 — screen-contested_machinery-2 — Reinforced armour

- [x] **Executed** — screen-contested_machinery-2 — Reinforced armour

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 47.00%, conservative 95% 33.42%–60.58%. Wins/draws/losses: 154/68/178.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 48.00%/46.00%.

**Notes / remaining work:** v2; board contested_machinery-2; scenario network; size 4; policy cautious. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-contested_machinery-2/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-contested_machinery-2/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-contested_machinery-2/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| cautious_holds_firing_position | 1266 |
| goal_unreachable_dynamic | 1326 |
| Occupied destination | 1448 |
| flight_no_safe_legal_destination | 1 |
| mark_has_fewer_than_two_ready_shooters | 6 |

**Ross’s notes:**

<!-- ross-notes:BS13 -->

<!-- /ross-notes -->

<a id="BS14"></a>

### BS14 — screen-contested_machinery-3 — Pin Them Down replacement

- [x] **Executed** — screen-contested_machinery-3 — Pin Them Down replacement

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 55.12%, conservative 95% 41.54%–68.71%. Wins/draws/losses: 205/31/164.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 55.50%/54.75%.

**Notes / remaining work:** v2; board contested_machinery-0; scenario breakthrough; size 6; policy flank. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-contested_machinery-3/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-contested_machinery-3/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-contested_machinery-3/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 559 |
| Occupied destination | 207 |
| flight_no_safe_legal_destination | 37 |

**Ross’s notes:**

<!-- ross-notes:BS14 -->

<!-- /ross-notes -->

<a id="BS15"></a>

### BS15 — screen-dense_urban-0 — Assault rifle

- [x] **Executed** — screen-dense_urban-0 — Assault rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 59.13%, conservative 95% 45.54%–72.71%. Wins/draws/losses: 219/35/146.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 59.25%/59.00%.

**Notes / remaining work:** v2; board dense_urban-0; scenario control; size 4; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-dense_urban-0/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-dense_urban-0/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-dense_urban-0/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 2974 |
| approach_requires_charge | 309 |
| goal_unreachable_dynamic | 269 |
| Occupied destination | 1613 |
| flight_no_safe_legal_destination | 14 |

**Ross’s notes:**

<!-- ross-notes:BS15 -->

<!-- /ross-notes -->

<a id="BS16"></a>

### BS16 — screen-dense_urban-1 — Sniper rifle

- [x] **Executed** — screen-dense_urban-1 — Sniper rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 58.50%, conservative 95% 44.92%–72.08%. Wins/draws/losses: 170/128/102.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 58.75%/58.25%.

**Notes / remaining work:** v2; board dense_urban-1; scenario recover; size 6; policy pressure. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-dense_urban-1/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-dense_urban-1/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-dense_urban-1/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| Occupied destination | 2294 |
| goal_unreachable_dynamic | 2642 |
| mark_has_fewer_than_two_ready_shooters | 865 |
| approach_requires_charge | 258 |
| flight_no_safe_legal_destination | 24 |

**Ross’s notes:**

<!-- ross-notes:BS16 -->

<!-- /ross-notes -->

<a id="BS17"></a>

### BS17 — screen-dense_urban-2 — Reinforced armour

- [x] **Executed** — screen-dense_urban-2 — Reinforced armour

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 40.00%, conservative 95% 26.42%–53.58%. Wins/draws/losses: 105/110/185.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 39.50%/40.50%.

**Notes / remaining work:** v2; board dense_urban-2; scenario network; size 9; policy cautious. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-dense_urban-2/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-dense_urban-2/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-dense_urban-2/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| goal_unreachable_dynamic | 4690 |
| cautious_holds_firing_position | 8197 |
| mark_has_fewer_than_two_ready_shooters | 736 |
| Occupied destination | 1001 |
| approach_requires_charge | 116 |
| flight_no_safe_legal_destination | 158 |

**Ross’s notes:**

<!-- ross-notes:BS17 -->

<!-- /ross-notes -->

<a id="BS18"></a>

### BS18 — screen-dense_urban-3 — Pin Them Down replacement

- [x] **Executed** — screen-dense_urban-3 — Pin Them Down replacement

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 52.88%, conservative 95% 39.29%–66.46%. Wins/draws/losses: 199/25/176.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 44.75%/61.00%.

**Notes / remaining work:** v2; board dense_urban-0; scenario breakthrough; size 4; policy flank. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-dense_urban-3/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-dense_urban-3/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-dense_urban-3/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| approach_requires_charge | 324 |
| mark_has_fewer_than_two_ready_shooters | 100 |
| flight_no_safe_legal_destination | 12 |
| Occupied destination | 5 |

**Ross’s notes:**

<!-- ross-notes:BS18 -->

<!-- /ross-notes -->

<a id="BS19"></a>

### BS19 — screen-industrial_vertical-0 — Assault rifle

- [x] **Executed** — screen-industrial_vertical-0 — Assault rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 57.88%, conservative 95% 44.29%–71.46%. Wins/draws/losses: 220/23/157.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 57.50%/58.25%.

**Notes / remaining work:** v2; board industrial_vertical-0; scenario control; size 6; policy pressure. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-industrial_vertical-0/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-industrial_vertical-0/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-industrial_vertical-0/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| Occupied destination | 4201 |
| goal_unreachable_dynamic | 4094 |
| mark_has_fewer_than_two_ready_shooters | 1521 |
| flight_no_safe_legal_destination | 24 |
| approach_requires_charge | 254 |

**Ross’s notes:**

<!-- ross-notes:BS19 -->

<!-- /ross-notes -->

<a id="BS20"></a>

### BS20 — screen-industrial_vertical-1 — Sniper rifle

- [x] **Executed** — screen-industrial_vertical-1 — Sniper rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 53.50%, conservative 95% 39.92%–67.08%. Wins/draws/losses: 127/174/99.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 54.25%/52.75%.

**Notes / remaining work:** v2; board industrial_vertical-1; scenario recover; size 9; policy cautious. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-industrial_vertical-1/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-industrial_vertical-1/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-industrial_vertical-1/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| Occupied destination | 2924 |
| goal_unreachable_dynamic | 5466 |
| cautious_holds_firing_position | 7181 |
| mark_has_fewer_than_two_ready_shooters | 837 |
| flight_no_safe_legal_destination | 100 |
| approach_requires_charge | 99 |

**Ross’s notes:**

<!-- ross-notes:BS20 -->

<!-- /ross-notes -->

<a id="BS21"></a>

### BS21 — screen-industrial_vertical-2 — Reinforced armour

- [x] **Executed** — screen-industrial_vertical-2 — Reinforced armour

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 14.25%, conservative 95% 0.67%–27.83%. Wins/draws/losses: 32/50/318.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 14.25%/14.25%.

**Notes / remaining work:** v2; board industrial_vertical-2; scenario network; size 4; policy flank. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-industrial_vertical-2/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-industrial_vertical-2/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-industrial_vertical-2/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| goal_unreachable_dynamic | 3503 |
| Occupied destination | 1771 |
| mark_has_fewer_than_two_ready_shooters | 694 |
| approach_requires_charge | 98 |
| flight_no_safe_legal_destination | 4 |

**Ross’s notes:**

<!-- ross-notes:BS21 -->

<!-- /ross-notes -->

<a id="BS22"></a>

### BS22 — screen-industrial_vertical-3 — Pin Them Down replacement

- [x] **Executed** — screen-industrial_vertical-3 — Pin Them Down replacement

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 52.00%, conservative 95% 38.42%–65.58%. Wins/draws/losses: 174/68/158.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 52.00%/52.00%.

**Notes / remaining work:** v2; board industrial_vertical-0; scenario breakthrough; size 6; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-industrial_vertical-3/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-industrial_vertical-3/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-industrial_vertical-3/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| approach_requires_charge | 1613 |
| mark_has_fewer_than_two_ready_shooters | 144 |
| Occupied destination | 1000 |
| flight_no_safe_legal_destination | 33 |

**Ross’s notes:**

<!-- ross-notes:BS22 -->

<!-- /ross-notes -->

<a id="BS23"></a>

### BS23 — screen-interior_compound-0 — Assault rifle

- [x] **Executed** — screen-interior_compound-0 — Assault rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 52.88%, conservative 95% 39.29%–66.46%. Wins/draws/losses: 202/19/179.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 52.00%/53.75%.

**Notes / remaining work:** v2; board interior_compound-0; scenario control; size 9; policy cautious. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-interior_compound-0/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-interior_compound-0/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-interior_compound-0/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| cautious_holds_firing_position | 6127 |
| goal_unreachable_dynamic | 5326 |
| Occupied destination | 2654 |
| mark_has_fewer_than_two_ready_shooters | 1324 |
| approach_requires_charge | 102 |
| flight_no_safe_legal_destination | 36 |

**Ross’s notes:**

<!-- ross-notes:BS23 -->

<!-- /ross-notes -->

<a id="BS24"></a>

### BS24 — screen-interior_compound-1 — Sniper rifle

- [x] **Executed** — screen-interior_compound-1 — Sniper rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 52.38%, conservative 95% 38.79%–65.96%. Wins/draws/losses: 101/217/82.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 52.25%/52.50%.

**Notes / remaining work:** v2; board interior_compound-1; scenario recover; size 4; policy flank. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-interior_compound-1/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-interior_compound-1/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-interior_compound-1/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 1763 |
| approach_requires_charge | 759 |
| goal_unreachable_dynamic | 177 |
| Occupied destination | 201 |
| flight_no_safe_legal_destination | 8 |

**Ross’s notes:**

<!-- ross-notes:BS24 -->

<!-- /ross-notes -->

<a id="BS25"></a>

### BS25 — screen-interior_compound-2 — Reinforced armour

- [x] **Executed** — screen-interior_compound-2 — Reinforced armour

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 44.25%, conservative 95% 30.67%–57.83%. Wins/draws/losses: 136/82/182.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 43.75%/44.75%.

**Notes / remaining work:** v2; board interior_compound-2; scenario network; size 6; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-interior_compound-2/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-interior_compound-2/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-interior_compound-2/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| Occupied destination | 4562 |
| goal_unreachable_dynamic | 5155 |
| mark_has_fewer_than_two_ready_shooters | 641 |
| approach_requires_charge | 65 |
| flight_no_safe_legal_destination | 4 |

**Ross’s notes:**

<!-- ross-notes:BS25 -->

<!-- /ross-notes -->

<a id="BS26"></a>

### BS26 — screen-interior_compound-3 — Pin Them Down replacement

- [x] **Executed** — screen-interior_compound-3 — Pin Them Down replacement

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 44.38%, conservative 95% 30.79%–57.96%. Wins/draws/losses: 161/33/206.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 49.00%/39.75%.

**Notes / remaining work:** v2; board interior_compound-0; scenario breakthrough; size 9; policy pressure. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-interior_compound-3/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-interior_compound-3/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-interior_compound-3/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| approach_requires_charge | 5466 |
| mark_has_fewer_than_two_ready_shooters | 542 |
| Occupied destination | 1318 |
| flight_no_safe_legal_destination | 119 |
| Only Charge can enter engagement | 10 |

**Ross’s notes:**

<!-- ross-notes:BS26 -->

<!-- /ross-notes -->

<a id="BS27"></a>

### BS27 — screen-long_lanes-0 — Assault rifle

- [x] **Executed** — screen-long_lanes-0 — Assault rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 56.50%, conservative 95% 42.92%–70.08%. Wins/draws/losses: 196/60/144.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 56.50%/56.50%.

**Notes / remaining work:** v2; board long_lanes-0; scenario control; size 4; policy flank. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-long_lanes-0/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-long_lanes-0/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-long_lanes-0/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 2128 |
| goal_unreachable_dynamic | 1690 |
| Occupied destination | 1722 |
| flight_no_safe_legal_destination | 4 |
| approach_requires_charge | 24 |

**Ross’s notes:**

<!-- ross-notes:BS27 -->

<!-- /ross-notes -->

<a id="BS28"></a>

### BS28 — screen-long_lanes-1 — Sniper rifle

- [x] **Executed** — screen-long_lanes-1 — Sniper rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 57.12%, conservative 95% 43.54%–70.71%. Wins/draws/losses: 179/99/122.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 57.00%/57.25%.

**Notes / remaining work:** v2; board long_lanes-1; scenario recover; size 6; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-long_lanes-1/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-long_lanes-1/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-long_lanes-1/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 2011 |
| Occupied destination | 1599 |
| goal_unreachable_dynamic | 2381 |
| approach_requires_charge | 272 |
| flight_no_safe_legal_destination | 4 |

**Ross’s notes:**

<!-- ross-notes:BS28 -->

<!-- /ross-notes -->

<a id="BS29"></a>

### BS29 — screen-long_lanes-2 — Reinforced armour

- [x] **Executed** — screen-long_lanes-2 — Reinforced armour

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 45.62%, conservative 95% 32.04%–59.21%. Wins/draws/losses: 158/49/193.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 45.00%/46.25%.

**Notes / remaining work:** v2; board long_lanes-2; scenario network; size 9; policy pressure. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-long_lanes-2/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-long_lanes-2/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-long_lanes-2/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 1308 |
| Occupied destination | 5613 |
| goal_unreachable_dynamic | 7289 |
| flight_no_safe_legal_destination | 54 |
| approach_requires_charge | 183 |

**Ross’s notes:**

<!-- ross-notes:BS29 -->

<!-- /ross-notes -->

<a id="BS30"></a>

### BS30 — screen-long_lanes-3 — Pin Them Down replacement

- [x] **Executed** — screen-long_lanes-3 — Pin Them Down replacement

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 52.88%, conservative 95% 39.29%–66.46%. Wins/draws/losses: 172/79/149.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 51.50%/54.25%.

**Notes / remaining work:** v2; board long_lanes-0; scenario breakthrough; size 4; policy cautious. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-long_lanes-3/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-long_lanes-3/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/battles/screen-long_lanes-3/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 1292 |
| cautious_holds_firing_position | 2735 |
| approach_requires_charge | 351 |
| Occupied destination | 22 |
| flight_no_safe_legal_destination | 24 |

**Ross’s notes:**

<!-- ross-notes:BS30 -->

<!-- /ross-notes -->

<a id="HC01"></a>

### HC01 — capacity-confirm-dense_urban-0 — Assault rifle

- [x] **Executed** — capacity-confirm-dense_urban-0 — Assault rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 57.25%, conservative 95% 43.67%–70.83%. Wins/draws/losses: 220/18/162.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 58.25%/56.25%.

**Notes / remaining work:** v2; board dense_urban-3; scenario control; size 6; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-dense_urban-0/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-dense_urban-0/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-dense_urban-0/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 2114 |
| holds_controlled_objective | 4404 |
| approach_requires_charge | 93 |
| flight_no_safe_legal_destination | 10 |

**Ross’s notes:**

<!-- ross-notes:HC01 -->

<!-- /ross-notes -->

<a id="HC02"></a>

### HC02 — capacity-confirm-dense_urban-1 — Reinforced armour

- [x] **Executed** — capacity-confirm-dense_urban-1 — Reinforced armour

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 45.38%, conservative 95% 31.79%–58.96%. Wins/draws/losses: 172/19/209.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 45.50%/45.25%.

**Notes / remaining work:** v2; board dense_urban-3; scenario control; size 6; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-dense_urban-1/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-dense_urban-1/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-dense_urban-1/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 2014 |
| holds_controlled_objective | 3972 |
| approach_requires_charge | 45 |
| flight_no_safe_legal_destination | 6 |

**Ross’s notes:**

<!-- ross-notes:HC02 -->

<!-- /ross-notes -->

<a id="HC03"></a>

### HC03 — capacity-confirm-interior_compound-0 — Assault rifle

- [x] **Executed** — capacity-confirm-interior_compound-0 — Assault rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 51.38%, conservative 95% 37.79%–64.96%. Wins/draws/losses: 191/29/180.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 51.50%/51.25%.

**Notes / remaining work:** v2; board interior_compound-3; scenario control; size 9; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-interior_compound-0/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-interior_compound-0/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-interior_compound-0/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| approach_requires_charge | 735 |
| Occupied destination | 2737 |
| mark_has_fewer_than_two_ready_shooters | 1406 |
| holds_controlled_objective | 5779 |
| flight_no_safe_legal_destination | 71 |

**Ross’s notes:**

<!-- ross-notes:HC03 -->

<!-- /ross-notes -->

<a id="HC04"></a>

### HC04 — capacity-confirm-interior_compound-1 — Reinforced armour

- [x] **Executed** — capacity-confirm-interior_compound-1 — Reinforced armour

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 36.88%, conservative 95% 23.29%–50.46%. Wins/draws/losses: 135/25/240.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 36.50%/37.25%.

**Notes / remaining work:** v2; board interior_compound-3; scenario control; size 9; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-interior_compound-1/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-interior_compound-1/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-interior_compound-1/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| Occupied destination | 2822 |
| mark_has_fewer_than_two_ready_shooters | 1161 |
| holds_controlled_objective | 5156 |
| approach_requires_charge | 775 |
| flight_no_safe_legal_destination | 78 |
| Only Charge can enter engagement | 2 |

**Ross’s notes:**

<!-- ross-notes:HC04 -->

<!-- /ross-notes -->

<a id="HC05"></a>

### HC05 — capacity-confirm-chokepoints-0 — Assault rifle

- [x] **Executed** — capacity-confirm-chokepoints-0 — Assault rifle

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 57.50%, conservative 95% 43.92%–71.08%. Wins/draws/losses: 220/20/160.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 58.00%/57.00%.

**Notes / remaining work:** v2; board chokepoints-3; scenario control; size 6; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-chokepoints-0/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-chokepoints-0/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-chokepoints-0/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 2049 |
| holds_controlled_objective | 3645 |
| approach_requires_charge | 167 |
| flight_no_safe_legal_destination | 10 |

**Ross’s notes:**

<!-- ross-notes:HC05 -->

<!-- /ross-notes -->

<a id="HC06"></a>

### HC06 — capacity-confirm-chokepoints-1 — Reinforced armour

- [x] **Executed** — capacity-confirm-chokepoints-1 — Reinforced armour

#### Results

**Recorded result:** 400 games / 100 independent four-game seed blocks. Focal match score 48.25%, conservative 95% 34.67%–61.83%. Wins/draws/losses: 181/24/195.

**Findings:** Conditional unpriced substitution; not proof of global superiority, weakness or a required rule change. Focal first/second scores: 50.00%/46.50%.

**Notes / remaining work:** v2; board chokepoints-3; scenario control; size 6; policy balanced. Ground subset only. Side and first assignment crossed; heuristic rejection counts are retained.

**Evidence:** [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-chokepoints-1/summary.json>) · [games.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-chokepoints-1/games.csv>) · [replays.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation-v2/battles/capacity-confirm-chokepoints-1/replays.json>)

| Policy limitation/rejection | Recorded count |
| --- | --- |
| mark_has_fewer_than_two_ready_shooters | 1862 |
| approach_requires_charge | 198 |
| holds_controlled_objective | 3605 |
| flight_no_safe_legal_destination | 14 |

**Ross’s notes:**

<!-- ross-notes:HC06 -->

<!-- /ross-notes -->

<a id="E37"></a>

### E37 — Post-decision frozen-v2/current-v3 regression

- [x] **Executed** — Post-decision frozen-v2/current-v3 regression

#### Results

**Recorded result:** 96 comparisons (192 engine executions) produced identical outcome records.

**Findings:** The selected homogeneous single-weapon outcomes are unchanged by the defender-choice clarification and the v3 bookkeeping fixes.

**Notes / remaining work:** This is a compact regression, not 96 new independent balance matchups. Full comparison rows retain seeds and side/first controls.

**Evidence:** [homogeneous-regression.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/decision-validation/homogeneous-regression.csv>) · [carry-forward-manifest.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v3/carry-forward-manifest.json>)

**Ross’s notes:**

<!-- ross-notes:E37 -->

<!-- /ross-notes -->

## F. Pilots, corrected defects and excluded runs

<a id="X01"></a>

### X01 — Engaged actor attempted an outside shot

- [x] **Executed** — Engaged actor attempted an outside shot

#### Results

**Recorded result:** Corrected. Seed 2026145101.

**Findings:** This entry records an implementation correction or excluded run, not gameplay balance evidence.

**Notes / remaining work:** An engaged actor now uses the melee procedure; the failing seed is retained.

**Evidence:** [failing-engagement-replay.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/pilot/failing-engagement-replay.json>)

**Ross’s notes:**

<!-- ross-notes:X01 -->

<!-- /ross-notes -->

<a id="X02"></a>

### X02 — Blocked forced-flight destination

- [x] **Executed** — Blocked forced-flight destination

#### Results

**Recorded result:** Corrected. Seed 121.

**Findings:** This entry records an implementation correction or excluded run, not gameplay balance evidence.

**Notes / remaining work:** Flight destination/path selection was corrected; this is a policy/engine defect, not a morale balance result.

**Evidence:** [failing-flight-replay.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/pilot/failing-flight-replay.json>)

**Ross’s notes:**

<!-- ross-notes:X02 -->

<!-- /ross-notes -->

<a id="X03"></a>

### X03 — No legal Charge contact route

- [x] **Executed** — No legal Charge contact route

#### Results

**Recorded result:** Corrected. Seed 2026113106.

**Findings:** This entry records an implementation correction or excluded run, not gameplay balance evidence.

**Notes / remaining work:** Charge now searches legal contact destinations before committing its actions.

**Evidence:** [failing-charge-replay.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v1/failing-charge-replay.json>)

**Ross’s notes:**

<!-- ross-notes:X03 -->

<!-- /ross-notes -->

<a id="X04"></a>

### X04 — Slow first occupancy-aware confirmation

- [x] **Executed** — Slow first occupancy-aware confirmation

#### Results

**Recorded result:** Aborted. Completed cells recorded: 0.

**Findings:** This entry records an implementation correction or excluded run, not gameplay balance evidence.

**Notes / remaining work:** Stopped for redundant path-search runtime; excluded from interpreted outcomes. The revised policy was piloted and confirmed separately.

**Evidence:** [ABORTED.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v2/policy-confirmation/ABORTED.json>)

**Ross’s notes:**

<!-- ross-notes:X04 -->

<!-- /ross-notes -->
<!-- /settlements-simulation:generated -->

## Additional notes

