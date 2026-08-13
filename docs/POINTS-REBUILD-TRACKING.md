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
| +1 Damage (the anchor) | **MEASURED** | **0.786** wp/model, CI [0.679, 0.894] | Objective-only, N=4000 × 9 cells, `gear-anchor-objective-n4000`. **REJECTS ALL FOUR PREDECESSORS** — 1.332, 1.12, 1.1183, 0.90385 all outside the CI. `CREDITS_PER_WINPOINT` 11.26 → **19.08**. Objective-cell spread **0.292–1.471 (5.0×)** — see §4.2. |
| Payload table (12 traits) | **MEASURED** | bleeding 33 Cr → AP 10 Cr | Numerators were already objective-only and are unchanged; only the conversion was wrong. Re-priced at 0.786. Still moves when armour is priced. |
| value(Pinned) | **VOID** | — | Mixed-scenario. The sign-split finding that motivated the whole policy change came from here and survives; the *number* does not. |
| Range bands | **VOID** | — | Prior run measured the policy, not the rules. |
| Weapon classes | **VOID (twice)** | — | Legacy ×10 originally; the 2026-08-12 re-run is void again on mixed scenarios. Still blocking armour. |
| Armour level | **BLOCKED** | — | Needs weapon classes first. Measure with **zero prior** — 30/60 cites a file that has never existed. |
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
2. **Does the anchor need non-linear treatment? — HELD, deliberately, pending the density sweep.**
   The evidence keeps pointing at "curve": the objective-cell spread is now **0.292–1.471, a 5.0× swing**, up from ~2× under mixed pricing. It has therefore **widened twice** — once after the policy fix, once after the objective-only cut.
   And the structure is not cell noise. `hold_claim` reads 0.29–0.40 in **every** list while `hold` reads 0.90–1.47 in **every** list, 3/3 consistent. The gap sits *inside the pricing set*, between the two scenarios a price is now averaged over.
   **Ruling is withheld anyway, and the reason is not caution but sequencing.** Terrain density is a measured **66-point win-rate swing** (`Full Rules System v1` §187; `Crew Sim — Findings`; parity at 9–12 large features) — a bigger lever than any atom this rebuild has measured, and it is expected to move this spread. Ruling on scenario-spread evidence alone would fix one variable while a larger untested one sits open. **Decide with both in hand, after the density sweep.**
3. **The Take-a-Hold tie-break**, re-evaluated now that the scenario resolves on its own.
4. **`IN_POSITION` 2.5 → 3.0.** Folded into the policy fix as a fidelity correction, not required by the invariant. Can be isolated and measured separately on request.

---

## 5 · Known harness defects

- **FIXED for `measure_anchor.py` only.** The `measure_*` scripts build their `Envelope` at the **end** of a run, so the fingerprints evaluate then, and an edit landing mid-run would stamp a result with code it never executed. `measure_anchor.py` now captures engine/cost/git **before** the first game and passes them explicitly. `run_stamped.py` already did. **The other five `measure_*` scripts still do not.**
- `policies.py` still carries fixed action priorities beyond the one fixed: no kiting, no focusing a slowed target, unconditional Pinned-clearing, and `issue_orders_attack` picks `ready[0]` by **list order**. So 0.786 is the best estimate under a *less wrong* AI, not a provably right one.
- `engine2d/data.py` keeps its own 100-scale cost table, separate from `points/ticks.py`. No price has ever been verified end to end.
- **A second sign-split detector existed and was removed** (`measure_signsplit.py`). It tested raw sign with no significance requirement and was OR'd with the real one in `price_atom`, so it could only ever *add* false positives and silently defeated the tightening beside it. Lesson recorded because the shape generalises: **a duplicate check OR'd with the real one is strictly worse than no check** — it cannot be fixed by improving the real one.
- **THE STALENESS CHECKER CANNOT SEE THE DEFECT THAT VOIDED HALF THIS BOARD — OPEN, needs a ruling.**
  Run `provenance.py` today and `weapon-class-atoms-n3000`, `stat-ladder-n3000` and `value-of-pinned-n4000` all report **`ok` / CURRENT**, despite being void in §1. `staleness()` compares the **engine** and **cost-table** fingerprints, and neither moved — the pricing policy that voided them lives in `harness/measure.py`, which no fingerprint covers.
  `git_state()` already half-knows this: its own comment says "measure.py's estimator and effects.py's divisor both change what a number means", and it watches `test-bench/harness/` for dirtiness. But dirtiness is not a fingerprint — a *committed* harness change moves the meaning of every result and leaves no trace at all.
  This is the exact false-freshness failure `provenance.py` was written to prevent, reintroduced one layer up: the module that guards against stale artefacts does not guard against itself.
  **The fix is a `harness_fingerprint()` over `measure.py` / `effects.py` / `anchor.py`, and it is Ross's call**, because adding it immediately marks **every stored result stale** — correctly, but all at once. That is a deliberate reset, not a silent maintenance change.

---

## 6 · Artefact hygiene — the payload table exists in three states

All three are **kept on disk deliberately**, none overwritten, on the same footing as
`packet_battle-n2000.txt`: a stale artefact preserved because the *way* it went stale is
the evidence. The staleness checker (`provenance.staleness()`) reads all of them.

| File | bleeding | State |
|---|---|---|
| `payload-table-meleefixed-n2500-3b61ae81.json` | 3.914 wp → **44 Cr** | Mixed numerator ÷ mixed denominator. Superseded. |
| `payload-signsplit-n3000-…SUPERSEDED-mixed-denominator.json` | 1.726 wp → **19 Cr** | Objective numerator ÷ **mixed** denominator. Superseded. Also carries the two false SIGN-SPLIT verdicts. |
| `payload-signsplit-n3000-3b61ae81.json` | 1.726 wp → **33 Cr** | **AUTHORITATIVE.** Objective numerator ÷ objective denominator (0.786). |

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
