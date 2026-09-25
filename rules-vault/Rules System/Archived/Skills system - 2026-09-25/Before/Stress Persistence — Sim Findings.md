---
type: reference
title: Stress Persistence — Sim Findings
tags: [settlements/reference, settlements/analysis, settlements/mechanic/morale]
---
# 😰 Stress Persistence — Sim Findings

Does **Stress survive being Downed?** Measured 2026-08-29. Harness `test-bench/attack_dice_stress_on_down.py`, stamped `attack-dice-15b-stress-on-down-e2b861d61-h326cd413`. Exact enumeration for the burst arithmetic; seeded Monte-Carlo (N=20,000, seed `20260708`) where a fight has to exist for the question to mean anything.

> [!success] Headline
> **This was never an Attack Dice question, and that is the finding.** The rules have never said what happens to a unit's Stress when it goes Down, and **in today's game — with no Attack Dice anywhere — a downed model already carries 0.66 Stress and sits in Break-test range 15.5% of the time.** [[15b · Attack Dice]] did not create this; it just made somebody look. The ruling lands on every fight the game has ever had.

## 1 · Where the Stress actually comes from

A **single shot that Downs you carries no Stress at all** — its one Injury pass *is* the wound, so there is nothing left over. All the Stress on a downed model comes from **everything that missed or failed first.**

| Source | Mean Stress at Down | P(2+, i.e. Break-test range) |
|---|:--:|:--:|
| One 3-die burst, in isolation | 1.04 | 27.4% |
| **Ordinary single-shot fire, no Attack Dice at all** | **0.66** | **15.5%** |

^tbl-1-where-stress-comes-from

The second row is the important one. It takes several attempts to put a fighter down, every failed one Pins, and the Stress just sits there. That is already true and already unruled.

## 2 · What the ruling costs, per revival

A Stabilised fighter re-enters the fight carrying its Stress, so it starts taking Break tests again. At **NRV +2**:

| Game state | Mean Stress | P(2+) | Fails first Break test | **BugOut on revival** |
|---|:--:|:--:|:--:|:--:|
| **Today (1 die, no surplus conversion)** | 0.66 | 15.5% | 8.8% | **1.9%** — ~1 in 53 |
| 3-die weapons, no surplus conversion | 0.97 | 22.7% | 12.8% | 2.7% — ~1 in 37 |
| **Both Attack Dice rules adopted** | **1.44** | **40.8%** | **22.5%** | **4.2%** — ~1 in 24 |

^tbl-2-cost-per-revival

**The sharp end** is a revived fighter at 4+ Stress: the crew spent an Action *and* an INT test to save him, he stands up, fails one roll and walks off the table. At today's rates that is **about one revival in fifty-three** — story frequency. Memorable when it lands, not a pattern anyone plays around.

Break-test failure odds by Stress, for reference ([[Morale]]'s `1d10 + NRV − (Stress−1)` vs 7+):

| Stress | Test? | NRV +1 | NRV +2 | NRV +3 | Failure means |
|:--:|:--:|:--:|:--:|:--:|---|
| 0–1 | no | — | — | — | Shaken only |
| 2 | yes | 60% | 50% | 40% | **Bolt** |
| 3 | yes | 70% | 60% | 50% | **Broken** |
| 4+ | yes | 80% | 70% | 60% | **BugOut — removed** |

^tbl-3-break-test-failure-odds

## 3 · Why persistence is also the cheapest option to write

It is the **absence** of a clearing rule. Ruling that Stress persists adds **no new test, no new track and no new token** — the existing End Phase Break test already does all the work. The only clause genuinely required is that a **Down** unit does not test while it is Down, which is really just saying out loud that a model out of the fight is out of the fight.

The two alternatives both cost more:
- *Stabilize clears Stress to 1* — one clause, removes the bad beat entirely, but also removes the whole beat: no test on standing up, ever.
- *Persists, but no BugOut on the first test back* — keeps the drama, removes only the walk-off, at the cost of a special case. Special cases are what this project cuts.

## 4 · One correction to how this was described

The rule was discussed as *"their next activation will begin with a nerve test."* **It does not need to, and it should not.** [[Morale]]'s Break test is an **End Phase** test. A revived fighter at 2+ Stress is picked up by that machinery automatically — no new trigger, no activation-start test, nothing to remember. The beat Ross wanted happens; it just resolves in the End Phase like every other Break test, which is the whole reason this rule is free.

The only difference is rhythm: depending on turn order a revived fighter may get one activation in before the test, rather than testing the instant it stands. **That is a feature, not a shortfall** — it means the rescue can still pay off, which is exactly what stops the double-punish being a pure waste.

## Design takeaways
1. 📌 **Rule it in.** Realistic, free to write, and it fixes a genuine gap rather than adding a mechanic.
2. 🎲 **The bad beat is rare enough to be a story** — ~1 revival in 53 walks off at today's rates.
3. 🔗 **Both were adopted together (2026-08-29), so the stacked case is what ships.** Stress-persistence *and* surplus-hits-to-Stress roughly **2.2×** the Stress on a downed model (0.66 → 1.44) and take wasted revivals from 1-in-11 to nearly 1-in-4. The recommendation had been to test them one at a time; Ross ruled both, and they interlock — surplus-to-Stress does **nothing at WND 1** without persistence, so splitting them would have made the second rule untestable anyway.
4. ⚠️ **Compounds the death-spiral risk** already flagged in [[Dice Mechanic — Sim Findings]] §7 — many triggers × a compounding −1. Worth watching at the table specifically.
5. 🩹 **Valve held in reserve, not pre-applied:** *"a Stabilised fighter returns Shaken, however much Stress it had."* One clause if it plays too punishing. The maths cannot tell you whether the bad beat feels brutal-good or brutal-bad — only the table can.

---
*Raw JSON at `test-bench/balance/results/attack-dice-15b-stress-on-down.json`; browsable in the Sim Explorer (`powershell -File test-bench/explorer/serve.ps1`).*

See [[Morale]] · [[Damage]] · [[Conditions]] · [[Attack Dice — Sim Findings]] · [[Dice Mechanic — Sim Findings]] · [[Crew Sim — Findings]].
