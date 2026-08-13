# Points Rebuild — Phase Tracking

**Live status board for the Credits-side rebuild.** Sim results live in
`test-bench/balance/results/` with a provenance envelope each; the reasoning behind
the two hardest findings is in `POINTS-REBUILD-EXPLANATIONS.txt`.

> ## The test this audit keeps applying
>
> **A number that looks precise, carries a tag or a confidence interval, and is
> denominated in something nobody has measured.**
>
> Every finding so far has been an instance of it. A confidence interval bounds
> sampling noise; it says nothing about whether the units mean anything. Apply it
> before trusting anything below.

---

## 0 · Standing invariants

| Invariant | Enforced by |
|---|---|
| The unit of account is **raw win-points per model**. Nothing stores Credits. | `harness/measure.py`, `Envelope` |
| The Credits peg (+1 Damage = 15 Cr) is a **choice**, not a measurement. | `harness/anchor.py` |
| Every result carries engine + cost-table + git fingerprints. | `harness/provenance.py` |
| A result whose scenario cannot resolve is **excluded, never averaged**. | `measure.degenerate` guard |
| A dial that does not exist is **refused, never created**. | `measure.set_dials` |
| Body and Gear scales never borrow each other's atoms. | design rule, checked in review |
| Every price carries an SE and a computed significance flag. | `measure.Result` |

---

## 1 · Atom status

Legend — **MEASURED**: current, post-policy-fix. **VOID**: measured under a defect,
must be re-run. **BLOCKED**: cannot be measured on this engine as built.
**JUDGMENT**: chosen, never measured. **OPEN**: Ross's call.

### Gear scale

> **THE OBJECTIVE-ONLY CUT (2026-08-12, commit `09c4462`) VOIDED MORE THAN IT FIXED.**
> `PRICING_SCENARIOS` became `(hold, hold_claim)` — Annihilate is a diagnostic and
> never enters a price. That policy landed **after** every measurement below except
> the sign-split run, so anything priced across `hold+annihilate` is now void by
> construction. Verified per script, not assumed: `measure_anchor.py:45`,
> `measure_payloads.py:65`, `measure_pinned.py:60` each carried
> `SCEN = ('hold','annihilate')`; the stat-ladder and weapon-class result files
> record `scenarios_used: ['hold','annihilate']`. Only `measure_signsplit.py` went
> through `price_atom()` and therefore ran on the new policy.

| Atom | Status | Value | Notes |
|---|---|---|---|
| +1 Damage (the anchor) | **MEASURED — PROVISIONAL** | **0.786** wp/model, CI [0.679, 0.894] | Objective-only, N=4000 × 9 cells. **REJECTS ALL FOUR PREDECESSORS** — 1.332, 1.12, 1.1183, 0.90385 all outside the CI. `CREDITS_PER_WINPOINT` 11.26 → **19.08**. **Carries the heaviest provisional marking in the project — see the box below §1.** Spread 0.292–1.471; the structure inside it is §4a, not §4.2. |
| Payload table (12 traits) | **MEASURED** | bleeding 34 · blast 27 · suppressive 21 · fire 20 · shocking 17 · heavy_impact 12 · AP 10 · toxic 6 · blinding 6 Cr | Canonical run, `payload-table-objective-n2500`. **Concussive, Crippling, Hook are indistinguishable from zero** (+0.018 / +0.012 / +0.020) — no price; they have a rules problem. Values still move when armour is priced. |
| value(Pinned) | **VOID** | — | Mixed-scenario. The sign-split finding that motivated the whole policy change came from here and survives; the *number* does not. |
| Range bands | **MEASURED** | 8″ 169 Cr · 12″ 175 · 18″ 194 · 24″ 230 | Value of upgrading **one** model off a 6″ baseline. **The 12″ threshold is not visible** — see below. |
| Weapon classes | **MEASURED** (damage + range only) | damage +1 → 1.300 wp *(hold-only)* | Objective-only, `weapon-class-atoms-objective-n2500`. Unblocks armour. Hands/slots, rank gate, Loud/Quiet, fire-while-Engaged remain unmeasurable, so a class price from this is damage + range and a flagged judgment for the rest. |
| Armour level | **UNBLOCKED — next** | — | Weapon classes are now real, so rebuild-to-pay has a currency. Measure with **zero prior** — 30/60 cites a file that has never existed. Then re-run payloads, which move with armour prevalence. |
| Hands / slots | **BLOCKED** | — | `Unit` carries one weapon string; `two_handed` is inert. |
| Rank-as-weapon-gate | **BLOCKED** | — | `CLASS_META.min_rank` is read by nothing. |
| Loud / Quiet | **BLOCKED** | — | No noise or alarm system. |
| Fire-while-Engaged | **BLOCKED** | — | `take_action()` forces melee for any engaged unit. |

### Body scale

| Atom | Status | Value | Notes |
|---|---|---|---|
| Stat rung (DEX, one-sided) | **re-running** | — | Prior shape: decays across rungs, saturating against the fixed TN. |
| Stat rung (STR, opposed) | **MEASURED (structural)** | flat, all rungs | `P(X+a > Y+b)` depends only on `b−a`; verified at 0.5606 for every base. An opposed same-stat roll **cannot** saturate. |
| Stat rung (AGI) | **BLOCKED** | — | Read only inside Dodge; `DODGE_ON` defaults False, so it measures zero by construction. |
| Stat rung (INT) | **conditional** | — | Worth zero without a claim step. Books against the **scenario mix**, not the fighter. |
| Stat rung (NRV) | **not started** | — | Never isolated per point by anything. |
| Orders (1 and 2) | **not started** | — | Never measured as an Order on any engine. See §2. |
| Bare body | **not started** | — | Unblocked now that Hold resolves. |
| +1 WND | **not started — LIVE AND UNVALIDATED** | 45 Cr charged | See §7. Not merely unmeasured: it is **shipping in the Level track right now** and the ruleset itself calls it unvalidated in three separate notes. |
| Skills (~150) | **BLOCKED, mostly** | — | 9 of ~150 are wired. The rest need engine work per subsystem. |

> ### The 12″ turn-one firing threshold does not appear in the data
>
> The banding argument rests on 12″ being the turn-one threshold — deploy zones 24″ apart,
> MOV 6″, so 18″ fires on turn one and 8″ cannot. `measure_weapon_classes.py` was written
> specifically to test that, because nothing ever had. Measured, off a 6″ baseline:
>
> | step | Δ wp | per inch |
> |---|---|---|
> | 6″ → 8″ | **+8.880** | 4.44 |
> | 8″ → 12″ | **+0.270** | 0.07 |
> | 12″ → 18″ | +1.040 | 0.17 |
> | 18″ → 24″ | +1.880 | 0.31 |
>
> **There is no step at 12″.** The 8→12 move is the *smallest* in the whole curve and about
> a quarter of an SE (0.270 against SEs of ~0.77). Above 12″ the curve **accelerates** —
> value per inch rises 0.07 → 0.17 → 0.31 — which is the opposite of a threshold and the
> opposite of diminishing returns.
>
> What dominates instead is the **6″ → 8″ jump: +8.88, thirty times the 8→12 step.** Nearly
> all the value is in "has usable reach at all" rather than in how much. That likely says
> more about the 6″ baseline being pathological on this board than about 8″ being good, so
> the *level* of these Credits figures should be treated with suspicion even though the
> *shape* is clear.
>
> **Caveat on the test, stated because it cuts toward the finding, not away:** all four
> variants were measured against the same `probe_r6` baseline on a shared seed, so their
> errors are correlated and a direct paired 8-vs-12 comparison would be *more* sensitive than
> the naive SEs above. That test has not been run. It could only tighten a difference already
> sitting at a quarter of an SE — but "not significant" here means "no evidence of a
> threshold", not "proof the threshold is absent".

> ### The anchor is 0 for 3. Cite 0.786 with this, every time.
>
> | Anchor | Rejected by | Cause, invisible from inside the number that carried it |
> |---|---|---|
> | 1.150 | 1.332 | `BalancedPolicy` shot instead of advancing |
> | 1.332 | 0.786 | Annihilate averaged into a price |
> | **0.786** | — | *unknown* |
>
> Every one of those runs was **internally clean** — paired estimator, tight CI, sane
> per-cell spread. 1.150 had *two independent confirmations* and they were wrong together.
> The defect was never visible from inside the measurement; it was always in an assumption
> the measurement could not see.
>
> **This is not a reason to doubt 0.786 specifically.** It is the best-founded anchor the
> project has had and the first measured on the scenarios the ruleset actually wins on. It
> is a reason it must never read as *settled* merely because two prior errors were caught.
> Finding two does not imply finding all.
>
> The marking travels in code, not just here: `anchor.PROVISIONAL` is embedded in
> `anchor.describe()`, which every measurement script prints, so a caller who wants only the
> number still gets the caveat.

### Materials axis

| Atom | Status | Notes |
|---|---|---|
| Base gatherer rate | **OPEN — Ross** | Not merely unmeasured: **not computable**. D23 prices structures by payback and the denominator is stated nowhere. Parked, not blocking. |
| Everything downstream | blocked on the above | Structures, workers, trader rates, loot, raid cap/floor. |

---

## 2 · Dependency chain

Read top-down; nothing below a blocked row can be trusted.

```
policy: advance before shooting        FIXED (5bdeafd)
    |
    +-- Take-a-Hold scoring            RESOLVED as a side effect - draws 100% -> 23%
    |       |
    |       +-- proposed tie-break     RE-EVALUATE: it was written for a contest
    |                                   failure, and the failure was non-arrival
    |
    +-- the anchor                     1.332 - itself later voided, see below
    |
    +-- weapon classes                 re-run, then voided again below

policy: objective-only pricing         FIXED (09c4462) - a SECOND root cause,
    |                                   independent of the first
    |
    +-- the anchor                     RE-DERIVED, 0.786 (was 1.332)
    |       |
    |       +-- every Credits figure   all derived through it; everything taken
    |       |                           at 1.332 is low by 1.694x
    |       |
    |       +-- payload table          re-priced by arithmetic, NOT re-run:
    |                                   numerators were already objective-only
    |
    +-- sign-split detector            FIXED - duplicate loose check removed
    |       |
    |       +-- Concussive/Crippling/  re-ran CLEAN: all three flat, no splits.
    |           Hook                    Ross's suspended ruling can resume.
    |
    +-- weapon classes                 VOID AGAIN - re-run on mixed scenarios
            |
            +-- armour level           blocked until classes are real
                    |
                    +-- payload table  moves AGAIN with the armour meta
                    +-- AP             worth 15 vs armour, 0 vs bare
```

**Two independent defects, found in sequence, each invisible from inside the number
the other produced.** The policy fix corrected *how models behave*; the pricing fix
corrected *which games count*. 1.332 was right about the first and wrong about the
second. The general lesson is in §0's one-line test: 1.332 looked precise, carried a
CI, and was denominated in a scenario mix nobody had justified.

**Bare-body pricing** additionally depended on the Take-a-Hold fix, not only on the
deleted `BALANCED_GOALS`. That dependency is now cleared.

---

## 3 · Contaminated prior findings

| Finding | Why | Action |
|---|---|---|
| Anchor 1.12 / 1.1183 / 0.90385 | All measured under the policy defect | **Rejected.** |
| Anchor 1.332 | Correct on policy, wrong on scenario mix — priced across hold+annihilate | **Rejected.** Superseded by **0.786**, which is outside 1.332's own CI. Every Credits figure taken at 1.332 is **low by 1.694×**. |
| "The payload table roughly HALVES" (commit `09c4462`) | Reported a **denominator mismatch**, not a finding: objective-only numerators divided by a mixed-scenario anchor | **Withdrawn.** Numerators were right; the conversion was wrong. True objective-only move is bleeding 44 → **33 Cr**, a ~25% cut, not a halving. |
| Concussive / Crippling "SIGN-SPLIT" verdicts | A second, untightened detector in `measure_signsplit.py` OR'd itself with the real one, so it could only add false positives | **Withdrawn.** Detector removed; re-run reports all three **flat - genuinely ~0**. |
| T9, T11, T12, T14 | `packet_campaign.py` set `BALANCED_GOALS = True`, and campaign crews are exactly the size where it sent every model to one objective | Re-run before use. T12 is **additionally circular** — it sets `BATTLE_CREDITS = RECRUIT_CR` then prints the ratio back as confirmation. |
| T13 | Published table has no harness in any branch; committed raw output is from a superseded implementation | Direction survives, exact values do not. |
| D21's model-count regression | Measured crews of different sizes on a scenario that did not score — **it was reading which crew sizes can deadlock, not which are stronger** | Re-run with crews rebuilt to equal `points/` cost. |
| Turret / roof / lone-runner headlines | `run.py` credits side A half the draws and side B none | Turret edge is ~1.6 pts, not the ~7.8 implied. |
| Every payload price pre-2026-08-12 | Melee never delivered a payload; divisor counted melee carriers anyway | Re-running. |

---

## 4 · Open decisions — Ross

1. **Base gatherer rate.** A scale choice like the 15. Materials is not computable without it.
2. **Does the anchor need non-linear treatment? — HELD, pending the density sweep.**
   The objective-cell spread is now **0.292–1.471, a 5.0× swing**, up from ~2× under mixed pricing — **widened twice**, once after the policy fix and once after the objective-only cut.
   **Ruling is withheld for sequencing, not caution.** Terrain density is a measured **66-point win-rate swing** (`Full Rules System v1` §187; `Crew Sim — Findings`; parity at 9–12 large features) — a bigger lever than any atom this rebuild has measured, and expected to move this spread. Ruling now would fix one variable while a larger untested one sits open. **Decide with both in hand.**
   *See §4a — the spread number is not the interesting part of this finding, and must not be the thing that gets carried forward.*

### 4a · The `hold` / `hold_claim` gap — a distinct finding, NOT "wide spread"

**Do not fold this into the spread narrative.** A wide spread and this are different objects,
and this one is the more troubling of the two.

| | `hold` | `hold_claim` | ratio |
|---|---|---|---|
| Fireteam (6) | +1.319 | +0.342 | 3.9× |
| Squad (8) | +0.898 | +0.292 | 3.1× |
| Armoured (6) | +1.471 | +0.396 | 3.7× |

A "5× spread" implies dispersion — cells scattered, some high, some low, the average a
reasonable summary of a noisy quantity. **That is not what this is.** This is a *systematic,
replicated, same-signed gap between two named scenarios, 3/3 across every list tested*, with
the ordering identical every time and the ratio stable at 3.1–3.9×. Dispersion would not
reproduce its own rank order three times out of three.

**Why it is worse than a wide spread.** Both scenarios are **inside the pricing set**. The
objective-only cut was justified on exactly this logic — that averaging across two families
which disagree describes neither, and Annihilate had to go. The same test, applied to what
remains, does not obviously pass: `hold` and `hold_claim` do not disagree in *sign*, so the
tightened detector correctly stays silent, but they disagree in *magnitude* by a stable
factor of ~3.5 in every single cell. The pricing set may therefore still straddle a boundary,
one detector-width below the threshold that would flag it.

**What it is not.** Not a sign-split — the detector is right not to fire. Not noise — 3/3
replication with stable ordering. Not an artefact of one list — it holds on Fireteam, Squad
and Armoured alike, across bare and armoured chassis.

**What would resolve it.** The gap has an obvious candidate mechanism: in claim mode
activations go to claiming rather than attacking, so a damage buff has fewer opportunities to
land. If that is the whole story, the correct price depends on **the expected scenario mix in
real play** — which is a Ross decision about what fraction of games are claim games, not a
measurement. That question is not currently on the open-decisions list and should be.

**This may end up mattering more than the density result.** Density moves the spread; this
asks whether averaging inside the pricing set is legitimate at all. Flagged here so it is not
absorbed into "the anchor has a wide spread" and quietly resolved by whatever the density
sweep happens to show.

#### The weapon-class run turned this from a pattern into a quantity

Two independent confirmations arrived from `weapon-class-atoms-objective-n2500`, which was
not designed to test any of this:

**1. The gap replicates on an unrelated atom, harder.** Range probes read `hold` +15.42 to
+18.96 against `hold_claim` +2.26 to +5.18 — a **3.7–6.9× gap**, same direction, all four
rungs. Dispersion does not reproduce its own rank order across unrelated measurements on a
different chassis.

**2. It is worth 36% of the anchor, and the probe chassis proves the anchor is otherwise
right.** All four damage probes returned `hold_claim` **degenerate**, so the damage ladder
priced from `hold` alone. That accident is the cleanest evidence yet:

| | value | basis |
|---|---|---|
| `probe_d2` (= +1 Damage on probe chassis) | **1.300** ± 0.217 | hold only |
| anchor, `hold` cells only | **1.229** | hold only |
| anchor, as published | **0.786** | hold + hold_claim |

The probe chassis **independently reproduces the anchor** — 1.229 sits comfortably inside
`probe_d2`'s CI [0.875, 1.725] — and the entire apparent 1.65× discrepancy between 1.300 and
0.786 is *nothing but the claim-scenario dilution*. Two different crews, two different
chassis, same answer once compared like with like.

**So the scenario-mix question is not academic and is not small.** "+1 Damage" is worth
**1.23** if claim games do not count and **0.786** if they count equally — a **36% swing in
the constant every Credits figure in the project is divided by**. That is a larger lever than
most of the atoms this rebuild is measuring, and it is currently being set by an unexamined
default (`hold` and `hold_claim` weighted 50/50 because there are two of them).

**This is now the top open question, ahead of flat-vs-curve** — see §4.5. Flat-vs-curve asks
what shape the constant should be; this asks what the constant *means*, and it has to be
answered first.

**One comparability defect it leaves behind:** within a single result file, range rows are
priced from two objective scenarios and damage rows from one, because `hold_claim`
degenerated only for the latter. The degeneracy guard is doing the right thing — excluding
rather than averaging a scenario that cannot resolve — but the surviving rows are then
denominated differently from each other, and the file does not say so on its face. A row
priced from `hold` alone is systematically **higher** than one priced across both, by exactly
the §4a factor. Any catalogue built by reading rows off this table side by side inherits
that. `priced_from` is recorded per row; nothing yet *warns* when rows in one table disagree.
### 4.5 · TOP OPEN QUESTION — what is the scenario mix, and who decides it?

**Not a measurement. A design decision, currently being made by accident.**

`PRICING_SCENARIOS = ("hold", "hold_claim")` weights the two equally, because there are two
of them. Nothing chose that. And the choice moves the anchor **0.786 ↔ 1.229 — 36%** — which
multiplies through every Credits figure in the project (§4a).

The three candidate answers are all defensible and give different games:

| Weighting | Anchor | Means |
|---|---|---|
| `hold` only | 1.229 | claim is a variant, not a pricing scenario |
| 50/50 (current, unchosen) | 0.786 | both equally likely at the table |
| weighted by real play | between | requires knowing the actual scenario mix |

**This blocks nothing mechanically** — every atom can be measured in win-points and converted
later, which is exactly why the harness stores win-points and never Credits. But **no Credits
figure is final until it is settled**, and that includes every number already produced.

**Ross's call.** The honest framing: what fraction of real games are claim games? If the
published scenario pack is the answer, the mix is countable rather than arguable.

3. **The Take-a-Hold tie-break**, re-evaluated now that the scenario resolves on its own.
4. **`IN_POSITION` 2.5 → 3.0.** Folded into the policy fix as a fidelity correction, not required by the invariant. Can be isolated and measured separately on request.

---

## 5 · Known harness defects

- **Fingerprint-before-run: fixed in 3 of 6.** The `measure_*` scripts built their `Envelope` at the **end** of a run, so an edit landing mid-run would stamp a result with code it never executed. `measure_anchor.py`, `measure_payloads.py` and `measure_weapon_classes.py` now capture engine/cost/harness/git **before** the first game. `run_stamped.py` always did. **`measure_pinned.py`, `measure_stat_ladder.py` and `measure_signsplit.py` still do not.**
- **ARTEFACT FILENAMES NOW GUARANTEE UNIQUENESS — RULED, FIXED 2026-08-12.**
  The old stem was `name-engine8`, which is content-independent: re-running a script with the same name, N and engine **silently overwrote** the prior result. Not theoretical — it destroyed the sign-split artefact on 2026-08-12, recoverable only because a commit happened to be 26 minutes old. `git show` is not a durability guarantee for an uncommitted run.
  This was the **second** artefact-naming defect in two milestones (after the misleading-filename finding in §6), and both traced to the same root: **the filename carried no uniqueness guarantee**. So the fix is the class, not the instance.
  Stems are now `name-e<engine8>-h<harness8>-<YYYYmmdd-HHMMSS>`, which cannot collide even for a byte-identical re-run, and `write()` **raises `FileExistsError` rather than clobbering** if one ever somehow does. No CI check can catch a silent overwrite after the fact, because the evidence is precisely what got deleted — so the guarantee has to be structural.
  Unique names create their own findability problem — one measurement name, many files, only one live — so `staleness()` now groups by name and labels the newest `<- LIVE` and the rest `superseded by …`, and `provenance.latest(name)` returns the live path so nothing has to hand-pick a filename.
- `policies.py` still carries fixed action priorities beyond the one fixed: no kiting, no focusing a slowed target, unconditional Pinned-clearing, and `issue_orders_attack` picks `ready[0]` by **list order**. So 0.786 is the best estimate under a *less wrong* AI, not a provably right one.
- `engine2d/data.py` keeps its own 100-scale cost table, separate from `points/ticks.py`. No price has ever been verified end to end.
- **A second sign-split detector existed and was removed** (`measure_signsplit.py`). It tested raw sign with no significance requirement and was OR'd with the real one in `price_atom`, so it could only ever *add* false positives and silently defeated the tightening beside it. Lesson recorded because the shape generalises: **a duplicate check OR'd with the real one is strictly worse than no check** — it cannot be fixed by improving the real one.
- **The live anchor artefact reads STALE, correctly, and should be re-stamped.**
  `gear-anchor-objective-n4000` was measured *after* the objective-only cut but *before*
  `harness_fingerprint()` existed, so it reports `harness(unstamped)` — "cannot verify",
  not "known changed". The checker is right to flag it and the distinction is already in
  the output. But the project's most load-bearing artefact should not be the one file
  that reads unverifiable. A re-run reproduces it exactly (fixed seed, same engine, and
  `measure_anchor.py` derives the anchor rather than importing it) — it costs ~72,000
  games purely to earn a stamp. **Ross's call whether that is worth the time.**
- **THE STALENESS CHECKER CANNOT SEE THE DEFECT THAT VOIDED HALF THIS BOARD — RULED, FIXED 2026-08-12.**
  Before the fix, `weapon-class-atoms-n3000`, `stat-ladder-n3000` and `value-of-pinned-n4000` all reported **`ok` / CURRENT** despite being void: `staleness()` compared only the **engine** and **cost-table** fingerprints, and the pricing policy that voided them lives in `harness/measure.py`, which nothing covered. The module written to catch stale artefacts could not catch itself.
  **Fixed:** `harness_fingerprint()` now text-hashes `measure.py` (PRICING_SCENARIOS, estimator, guards, sign-split detector), `effects.py` (the divisor — a ~20% swing) and `anchor.py` (VALUE). Text-hashed rather than value-hashed, the opposite choice from the cost table, and deliberately: `ticks.py` is mostly commentary so rewording must not invalidate a result, whereas these three are logic and an estimator can change completely while its constants sit still. **False-stale is noise; false-fresh is the failure this module exists to prevent.**
  Every stored result went stale at once, which is the checker finally reporting accurately rather than a cost — everything measured pre-objective-only *is* stale. Results carrying no harness fingerprint report `harness(unstamped)`, distinguishing "cannot verify" from "known changed".

---

## 6 · Artefact hygiene — the payload table exists in three states

All three are **kept on disk deliberately**, none overwritten, on the same footing as
`packet_battle-n2000.txt`: a stale artefact preserved because the *way* it went stale is
the evidence. The staleness checker (`provenance.staleness()`) reads all of them.

| File | bleeding | State |
|---|---|---|
| `payload-table-meleefixed-n2500-3b61ae81.json` | 3.914 wp → **44 Cr** | Mixed numerator ÷ mixed denominator. Superseded. |
| `payload-signsplit-n3000-…SUPERSEDED-mixed-denominator.json` | 1.726 wp → **19 Cr** | Objective numerator ÷ **mixed** denominator. Superseded. Also carries the two false SIGN-SPLIT verdicts. |
| `payload-signsplit-n3000-3b61ae81.json` | 1.726 wp → **33 Cr** | Correct, but under the *diagnostic's* name. Superseded as the table. |
| **`payload-table-objective-n2500-e3b61ae81-h42615a70-…json`** | 1.765 wp → **34 Cr** | **CANONICAL.** Under the name a reader looks for, from `measure_payloads.py`. |

**The index defect is now closed, and the fix is checkable rather than trusted.** Both scripts
run through `price_atom()` and are required to agree; they do, on all 12 traits, with a max
divergence of 0.187 wp (hook, whose SE is 0.537 — i.e. inside noise) and 11 of 12 inside 0.04.
That agreement is the point: `measure_signsplit.py` keeps answering only the question its name
asks, `measure_payloads.py` owns the table, and if they ever diverge the divergence is itself
the finding.

**The file-hygiene finding, which is the point of keeping all three:** the correct payload
numbers landed in a file *named for a different question*. `measure_signsplit.py` was written
to answer "are these three traits sign-split?", and in doing so it became the only script on
the new pricing policy — so the whole 12-trait table's best values sat under a filename that
advertises a narrow diagnostic. Nothing was wrong with the numbers; the *index* was wrong.
That is the same class of failure as `packet_battle-n2000.txt`, and neither a confidence
interval nor a provenance fingerprint can catch it — both files were internally honest.
**A result is only findable under the question it appears to answer.** The canonical
`measure_payloads.py` must be moved to `price_atom()` so the authoritative table lives under
the name a reader would look for.

---

## 7 · Live ruleset numbers with no measurement behind them

Distinct from §1, which tracks atoms the rebuild is *working toward*. These are **shipping in
the rules right now** while carrying no derivation — the failure mode where an unvalidated
number sits looking settled because nothing flags it.

| Number | Where it is live | Provenance |
|---|---|---|
| **+1 WND = 45 Cr** | `Full Rules System v1` §26.1 (Level-7 rung, table line 972); `Progression.md:51`; `List Building.md:136`; `Economy.md:108`. Inside the **+245 Cr** full-track total, so it propagates into every levelled fighter. | **None.** The ruleset says so itself in three places: "no sim data behind it at all… a judgment call, not a measurement" (§991); "the one number in this whole area with zero validation behind it at all" (§1140); `Economy.md:129`. Priced by position — above a T2 skill, below a T3. |
| **Armour Light 30 / Heavy 60** | `points/ticks.py` `ARMOUR_CREDITS` | Tagged `[measured]` citing `balance/armourprice.py` — **a file that has never existed in any commit on any branch.** Measure with zero prior. |
| **Flat 15 / stat point** | `ticks.py:55 TICK_STAT`; ruled price throughout the Level track | The vault already flags it as a known underprice citing "16–34 Credits" (`Progression.md:69`) — **but that correction is itself contaminated**, being a pre-policy-fix figure. A live number corrected by a void number. |

**+1 WND does not jump the queue** — it sits behind the anchor, weapon classes and armour in
the dependency chain. It is recorded here so it does not read as settled while the rebuild
works toward it.
