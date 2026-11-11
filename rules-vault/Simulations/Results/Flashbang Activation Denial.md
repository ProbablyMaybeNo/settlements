<!-- settlements-simulation:generated -->
# Flashbang balance follow-up — 11 November 2026

**Balance verdict: WATCH / CONFIRM — high-priority control concern. Not passed.**

**Recommended action:** retain the approved rule while testing sustained lockout
and legal counterplay. A rule adjustment becomes warranted if repeated denial
remains oppressive after competent movement, initiative, resource and reaction
responses. This first-cycle task does not establish that result yet.

## Executed test

12 cells × 1,000 independent paired seeds = **12,000 pairs / 24,000 task arms**.
Two mechanically legal four-member starting crews; deferred Credit verification.
Both arms carry the same Flashbangs. Treatment uses one per capable thrower;
control spends Core on Aim. Each victim earns one fixture work point using Core
at its console. This is a simulation task, not an approved scenario or whole battle.

Whole-unit activations alternate. Cross attacker/defender acting first, 1.3/6-inch
victim spacing, and unready/ALERT/solid-wall defence. ALERT counterfire happens
at the start of an enemy activation, before throwing; setup requires two pre-existing
tokens and their earlier Core/Order investment. It is not assumed free.

## Results and balance meaning

| Setup | Mean immediate activations lost (of 2) | Mean pending victim skips | Meaning |
| --- | --- | --- | --- |
| Attackers first, cluster, unready | 1.686 (simultaneous 95% 1.429–1.943) | 0.740 | Strong immediate denial; two Cores and two grenades expended. |
| Attackers first, cluster, ALERT | 1.200 (0.943–1.457) | 0.692 | Observed counterfire reduces delivery; 0.491 throwers Down on average, but substantial denial remains. |
| Attackers first, spread, unready | 1.531 (1.274–1.788) | 0.057 | Spreading greatly reduces follow-on cross-target pending effects, but each thrower can still target its own victim. |
| Defenders first, cluster, unready | 0.719 (0.462–0.976) | 1.724 | Earlier action protects some current work; much of the effect shifts to the next activation. |
| Defenders first, spread, unready | 0.068 (−0.189–0.325) | 1.460 | Little immediate denial, but significant pending conditions remain. |
| Full solid wall, either first/spacing | 0 (nonzero uncertainty retained) | 0 | No legal fixed-position throw opportunity; moving around the wall is untested. |

Intervals are simultaneous Hoeffding bounds across 12 × 8 declared paired outcomes.
Bounds for a difference may extend below zero; that is uncertainty, not negative lost
activations. Between-cell counter comparisons are descriptive screening comparisons.
All 12 cells, per-seed arms, fixture checks and 24 exact reproducing event/packet/state
samples are linked below; unfavourable cells were not dropped.

**Finding:** the rule has a real tempo effect and timing matters beyond the application
round. It should not receive a balance pass simply because it deals no Injury or because
Stunned does not stack. ALERT and solid cover offer tested constraints; neither this
task nor the older area micro batch establishes adequate full-crew counterplay.

**Adjustment decision:** no immediate nerf/buff recommendation yet. The next evidence
gate is repeated-use objective play with legal grenade quantities, resource depletion,
movement, End-Phase morale/flight, alternate objectives and competent counterbuilds.
If practical repeated lockout survives that gate, bring Ross a concrete proposed change
to footprint, targeting or duration with measured alternatives. Nothing is adopted here.

## Important limits

The task stops after one activation cycle, before End Phase. Pending Stunned flags
are reported, not counted as already-lost future turns. Victims stay at declared work
positions; this does not prove that remaining there is optimal. No complete terrain
route search, physical-template validation, campaign balance or human-play claim.
Rules/owners/prices are unchanged. Current kernel hash equals v4; v5 is this new
task evidence, not a rerun or relabelling of the earlier 14,400 ground games.

## Evidence

- [paired-summary.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v5/flash-denial/paired-summary.csv>)
- [seed-pairs.csv](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v5/flash-denial/seed-pairs.csv>)
- [configs.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v5/flash-denial/configs.json>)
- [fixture-validation.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v5/flash-denial/fixture-validation.json>)
- [replay-verification.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v5/flash-denial/replay-verification.json>)
- [summary.json](<file:///D:/AI-Workstation/Antigravity/apps/Settlements/output/balance-pass-2026-11-11/v5/flash-denial/summary.json>)

## Reproduce

From the D-drive repository root:

```
py -3.13 docs/balance-pass-2026-11-10/run_flash_denial_current.py --out output/balance-pass-2026-11-11/v5 --pairs 1000
py -3.13 docs/balance-pass-2026-11-10/publish_flash_supplement.py
```

After later engine changes, use this batch's frozen engine and producer script.
<!-- /settlements-simulation:generated -->

## Additional notes

