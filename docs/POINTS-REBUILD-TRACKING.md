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

| Atom | Status | Value | Notes |
|---|---|---|---|
| +1 Damage (the anchor) | **MEASURED** | 1.332 wp/model, CI [1.202, 1.462] | Rejects all four historical candidates. Per-cell spread 0.898–1.879 travels with it. |
| Payload table (12 traits) | **re-running** | — | Melee delivery fixed; divisor honest. |
| value(Pinned) | **re-running** | — | Prior: ~0, which settled Concussive/Crippling as weak rather than redundant. |
| Range bands | **VOID** | — | Prior run measured the policy, not the rules. |
| Weapon classes | **VOID** | — | Legacy ×10, never measured. Blocking armour. |
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
| +1 WND | **not started** | — | Charged 45 Cr with, by the ruleset's own admission, no sim data. |
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
    +-- the anchor                     re-measured, 1.332
    |       |
    |       +-- every Credits figure   all derived through it
    |
    +-- weapon classes                 re-running
            |
            +-- armour level           blocked until classes are real
                    |
                    +-- payload table  moves with the armour meta
                    +-- AP             worth 15 vs armour, 0 vs bare
```

**Bare-body pricing** additionally depended on the Take-a-Hold fix, not only on the
deleted `BALANCED_GOALS`. That dependency is now cleared.

---

## 3 · Contaminated prior findings

| Finding | Why | Action |
|---|---|---|
| Anchor 1.12 / 1.1183 / 0.90385 | All measured under the policy defect | **Rejected.** Superseded by 1.332. |
| T9, T11, T12, T14 | `packet_campaign.py` set `BALANCED_GOALS = True`, and campaign crews are exactly the size where it sent every model to one objective | Re-run before use. T12 is **additionally circular** — it sets `BATTLE_CREDITS = RECRUIT_CR` then prints the ratio back as confirmation. |
| T13 | Published table has no harness in any branch; committed raw output is from a superseded implementation | Direction survives, exact values do not. |
| D21's model-count regression | Measured crews of different sizes on a scenario that did not score — **it was reading which crew sizes can deadlock, not which are stronger** | Re-run with crews rebuilt to equal `points/` cost. |
| Turret / roof / lone-runner headlines | `run.py` credits side A half the draws and side B none | Turret edge is ~1.6 pts, not the ~7.8 implied. |
| Every payload price pre-2026-08-12 | Melee never delivered a payload; divisor counted melee carriers anyway | Re-running. |

---

## 4 · Open decisions — Ross

1. **Base gatherer rate.** A scale choice like the 15. Materials is not computable without it.
2. **Does the anchor need non-linear treatment?** Its per-cell spread is 0.898–1.879 — roughly 2×, and it *widened* after the policy fix, so it is a real property rather than an artefact. The stat ladder just demonstrated that a constant hiding a 5× spread was the wrong shape.
3. **The Take-a-Hold tie-break**, re-evaluated now that the scenario resolves on its own.
4. **`IN_POSITION` 2.5 → 3.0.** Folded into the policy fix as a fidelity correction, not required by the invariant. Can be isolated and measured separately on request.

---

## 5 · Known harness defects, unfixed

- The `measure_*` scripts build their `Envelope` at the **end** of a run, so the fingerprints evaluate then. An edit landing mid-run would stamp a result with code it never executed. `run_stamped.py` already fingerprints up front; the measurement scripts must do the same.
- `policies.py` still carries fixed action priorities beyond the one fixed: no kiting, no focusing a slowed target, unconditional Pinned-clearing, and `issue_orders_attack` picks `ready[0]` by **list order**. So 1.332 is the best estimate under a *less wrong* AI, not a provably right one.
- `engine2d/data.py` keeps its own 100-scale cost table, separate from `points/ticks.py`. No price has ever been verified end to end.
