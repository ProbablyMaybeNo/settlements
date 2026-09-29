> [!important] Rules changed — 2026-09-29
> Reports below describe earlier rules. The next pass must use [[Draft 2 - Simulation Assumptions]]: Stress-free Break/Rally with Stress-based severity, Stress on Injury rolls, half-speed Pinned movement and the updated Rage/Implode cycle. In particular, the historical Rage FAILED verdict does not evaluate the new cycle. No rerun results are implied.


## REPORT FORMAT
### Title and Number

Use a sequential number and a short title.

### Overview

Briefly list what was tested and assign each item a status:

- **PASSED** — Works as intended.
    
- **FAILED** — Needs major revision or removal.
    
- **PENDING** — Promising but needs clarification or small changes.
    
- **BLOCKED** — Cannot be tested yet.
    
- **INCONCLUSIVE** — Results depend on unresolved assumptions.
    

### Report

Summarize the main findings in plain language. State what worked, what did not, and what needs further testing.

### Findings

| Mechanic / System | Status | Brief Finding |
| ----------------- | ------ | ------------- |

Add a short explanation for each result.

### Assumptions and Next Steps

Record important assumptions, limitations, and recommended follow-up tests.

### Files

List the result files, scripts, and instructions needed to reproduce the simulation.

---

## 001 · Skill Second Pass — corrected Stress model

*Run 2026-09-27. Second pass over the skills flagged by the first pass. Scope: 22 skills plus 2 rule checks.*

### Overview

- **PASSED** (works as intended): Quick; cumulative Stress penalty (simulator model).
- **FAILED** (needs major revision or removal): Rage; Pin Them Down.
- **PENDING** (promising but needs clarification or small changes):
  - **Movement:** Sprinter.
  - **NRV support:** Hold Fast, Menacing, Lean On Me, Big Aura, Rally, Motivate, Inspire, Sin Eater, Commanding Presence.
  - **Other:** Come On Then.
- **BLOCKED** (cannot be tested yet): Gunslinger, Ambidextrous, Big Fella, On Your Feet, Stabilize.
- **INCONCLUSIVE** (results depend on unresolved assumptions): Roar, Unflinching, Steady Breathing; the provisional Break formula.

### Report

**The main result: switching from flat Shaken −1 to cumulative −1 per Stress changed nothing in the battle results.** All 41 first-pass battle comparisons moved by 1 point or less. The reason is that 93% of attack rolls happen at 0–1 Stress, where the two models give the same penalty. The End-Phase Break test keeps Stress low. So none of the first-pass signals came from the old Stress rules. Where the first pass was wrong, the cause was the battle AI's behaviour or the scenario.

**What worked:**
- **Quick** is healthy. Its first-pass "overpowered" result (+9) came from the AI dashing to objectives in Sabotage. With a shoot-first AI it drops to +1.6. On randomised objectives it's about as valuable as +2 DEX.
- **Sprinter** holds up in every test on a gunner. It's positive across every layout, both AI styles and both crew policies (+1.5 to +11.3). In the AI-free kite duel (gunner retreating from a Brawler) it adds +18.7 points at 12". It's strong, possibly too strong, and it's the one skill to watch.

**What did not work:**
- **Rage** hurts whoever carries it: −1.5 to −5.5 on a Brawler at every NRV tested. In the AI-free duels it's only useful as a +1/+2 finisher against 1-Wound targets. The corrected Stress model makes it worse against tougher targets (+3 vs 2 Wounds: −2.8 → −10.1).
- **Pin Them Down** does nothing. Universal Pinned already covers it.

**What needs work:**
- **NRV support skills** have real effects, but paying an Action for them costs more than they return. Hold Fast is worth about +2 if it's free. Once it costs the Leader an Action and tempo it goes negative, and making the AI turn it on in its first activation made it worse (−5 to −11). The NRV 15+ activation test is the second-largest cost; the test alone is what holds Rally back.
- **Several skills can't do anything yet** because of missing rules or weapons.

**Retracted from the first pass:**
- **Steady Breathing is not useless.** On a 36" board, 17–28% of shooting positions gain a new target between 24" and 36"; the battle AI just never stands in them.
- **Unflinching now has a trigger** under v2 §3 (READY is cancelled when the unit is hit).
- **Come On Then's −13.7** was the AI taunting when it should have charged.

### Findings

| Mechanic / System | Status | Brief Finding |
| ----------------- | ------ | ------------- |
| Cumulative Stress penalty | PASSED | Implemented and verified. It changed no first-pass battle result by more than 1 point. |
| Provisional Break formula (d20 + NRV − Stress vs 15+) | INCONCLUSIVE | Uniformly 5% harder than the first-pass formula. v2 has no Break procedure yet. |
| Quick | PASSED | Worth about +2 DEX once AI policy and Sabotage tempo are separated out. |
| Sprinter | PENDING | Strong on gunners in every test; nothing on a Brawler. Watch for over-strength. |
| Rage | FAILED | Harmful in battle. Useful only as a +1/+2 finisher against 1-Wound targets. |
| Hold Fast | PENDING | The effect is real, but the Action and tempo cost more than it returns. |
| Menacing | PENDING | Same pattern as Hold Fast, with a smaller effect. |
| Lean On Me | PENDING | Close to worthless even when free. Probably needs a stronger effect. |
| Big Aura | PENDING | Inherits the auras' Action cost. Worth +1.7 only when the auras are free. |
| Rally | PENDING | Held back by the activation test; automatic activation lifts it to +1.0. |
| Motivate | PENDING | Spending an Action to grant Actions nets about zero. |
| Inspire | PENDING | Works, but the chance to use it rarely comes up. |
| Sin Eater | PENDING | Small effect, few opportunities. |
| Commanding Presence | PENDING | Prevents only 0.02–0.04 Breaks per game. |
| Come On Then | PENDING | Only pays off with a multi-Wound carrier under ranged fire. |
| Gunslinger | BLOCKED | No 1H weapon with more than one Attack Die. Healthy with a test weapon. |
| Ambidextrous | BLOCKED | No 1H multi-die AGILE weapon. Healthy with a test weapon. |
| Big Fella | BLOCKED | No weapon has UNWIELDY. |
| On Your Feet | BLOCKED | Pinned recovery rules are unfinished. |
| Stabilize | BLOCKED | Treatment rules are unwritten. Measured +0.5 to +0.7. |
| Pin Them Down | FAILED | Redundant under universal Pinned. |
| Roar | INCONCLUSIVE | Its trigger (an enemy charging into it) almost never occurs. |
| Unflinching | INCONCLUSIVE | Has a trigger under v2, but the AI rarely holds READY. |
| Steady Breathing | INCONCLUSIVE | The sight lines exist; the battle AI never uses them. |

**Cumulative Stress penalty.** −1 per Stress point on every relevant roll, maximum 5 (7 with Implode). Hand-checked tests confirm it's applied once per roll. The engine still reproduces all 84 first-pass tests exactly when the old settings are selected.

**Provisional Break formula.** Tested as instructed, with the first-pass trigger (End Phase, 2+ Stress) and outcomes (2 Bolt, 3 Broken, 4+ BugOut) kept. 69% of Break tests happen at exactly 2 Stress.

**Quick.**
- The first-pass +9.0 came mainly from Sabotage (+16.8) under the AI's dash-to-objective behaviour.
- With a shoot-first AI it's +1.6. On random objectives it's +1.2 to +2.3; in combat layouts, 0 to +4.6.
- It wins an objective race only at distance breakpoints (67% at 24").
- On a Brawler it's a real pursuit tool in open ground, adding 9–14 points in duels.

**Sprinter.**
- On a gunner, positive in every layout, AI style and crew policy (+1.5 to +11.3); +4.4 to +5.5 on random objectives.
- Kite duel: +18.7 points at 12", because it Dashes with the Move slot and still shoots.
- On a Brawler it's exactly 0, because a Dash can't be followed by a Charge.

**Rage.**
- **Battles:** Brawler +1/+2/+3 score −2.2 / −2.8 / −5.5 (NRV 1). At +3 the Brawler bugs out 0.49 times per game, against 0.06 for the mirror. On a heavy-armour Leader it's neutral.
- **AI-free duel grid:** net value +1.8 / +3.8 / +3.1 against 1-Wound targets, but −0.5 to −12.3 against 2–3 Wounds.
- **Costs:** the carrier's chance of breaking rises 10 / 31 / 32 points at +1/+2/+3. NRV barely changes this.

**Hold Fast / Menacing / Lean On Me / Big Aura.** Four ways of activating them were compared: A (the current rule), B (automatic activation), C (test NRV when the effect applies) and D (a diagnostic only, not a proposal: no Action and no test).
- Hold Fast scores −0.3 to −1.1 under A, B and C. Under D it scores +1.6 to +2.1 and prevents 0.26–0.31 wounds per game.
- Forcing activation on the first turn gives full coverage but scores −5 to −11, because the Leader loses its round-1 Action and its Dash.
- The NRV activation test passes only 45% at NRV 3.

**Rally.** Cohesive crew: +0.3 under the current rule, +1.0 with automatic activation, +1.3 when free. Automatic activation doubles the units rallied.

**Motivate.** Negative under automatic activation and the effect-test variant; positive (+0.5) only when free.

**Inspire, Sin Eater, Commanding Presence.** Small effects that rarely come up: 0.09–0.12 Inspire uses per game; 0.02–0.04 Breaks prevented per game by Commanding Presence.

**Come On Then.** Controlled test with an enemy Brawler and two rifles within 6":
- A Tough Brawler under ranged fire cuts expected friendly downs from 0.32 to 0.19.
- A 1-Wound carrier mostly moves the casualty to itself.
- The STR test passes only 30–45% of the time.

**Gunslinger and Ambidextrous.** Both do exactly 0 with one-die off-hands, which is correct under the rules. With the labelled test weapons:
- Gunslinger: P(Down) 35% → 44%; battle +1.2.
- Ambidextrous: kill chance 35% → 43%; battle +2.2.
- Both results hold under every resolution method tested.

**Big Fella / Pin Them Down.** The vault check found 0 UNWIELDY weapons. Pin Them Down measured exactly 0.0 in both passes.

**On Your Feet.** 0.001–0.004 uses per game. The simulation clears Pinned with the Move slot; v2's Action-cost recovery would give the skill more to do and is not modelled.

**Roar.** Blocks 0.004–0.019 charges per game in every variant.

**Unflinching.** Fires 0.02–0.06 times per game with READY-lost-on-hit, and 0.001–0.003 with v2's full READY cancellation. Δ 0.0.

**Steady Breathing.** AI-free sight-line survey: on 36" boards, 17–28% of shooter positions gain a target and 3–4% gain their only target. Larger boards: 33–48%.

### Assumptions and Next Steps

**Assumptions:**
- **Dice:** ordinary tests, shooting and Injury are d20 vs 15+. Melee and Return Fire use highest-opposing pools.
- **Opposed-pool natural results (provisional):** a natural 1 can't hit or defend; a natural 20 beats any non-20; two opposing 20s tie.
- **Modifier caps:** skills ±4, weapons ±3, stats ±6, armour ±6.
- **Stress:** cumulative, maximum 5. The Break formula above is provisional.
- **Carried from the first pass because Draft 2 is undecided:**
  - 36" board at density 9/11/12; MOVE 6; Dash = 2 × MOVE; Charge = MOVE + 1d6;
  - cover −1/−2;
  - Pinned cleared by the Move slot;
  - READY kept until used;
  - Downed units bleed out after one round.
- **Test fixtures, not catalogue entries:** `machine_pistol_X`, `twin_blade_X`, and Brawler NRV 3/6 stat profiles.
- **The battle AI is a test policy, not a human player.** Confidence intervals cover sampling noise only.
- **No live rules or Credits costs were changed.**

**Next steps:**
- Draft the Break procedure, then rerun Rage and the NRV skills against it.
- Decide whether NRV support skills should cost an Action, need an activation test, or both. The data points at the Action cost first and the test second.
- Rule on Pinned recovery (the v2 Action cost), then retest On Your Feet.
- Decide whether to add a 1H multi-die weapon (unblocks Gunslinger and Ambidextrous) and an UNWIELDY weapon (unblocks Big Fella).
- Replace Pin Them Down.
- Playtest Sprinter on gunners at the table.
- Build a READY-aware and range-aware AI before judging Unflinching, Steady Breathing and Roar.
- Retest movement once v2 sets MOVE, Dash distance and board size.

### Files

**Repository:** `D:\AI-Workstation\Antigravity\apps\Settlements`

- **Report:** `docs/SKILLS-SIM-PASS2-2026-09-27.md`
- **Assumptions:** `test-bench/skills_lab/ASSUMPTIONS-PASS2.md`
- **Results:** `test-bench/skills_lab/results/pass2-2026-09-27/`
  - `battles/battles.csv` — the "early timing" rows are superseded by `battles-timing/`
  - `battles-timing/battles.csv`
  - `controlled/*.csv`
  - `controlled/audit.txt`
  - `comparison.csv` / `comparison.md`
  - `verdicts.csv`
- **Scripts:** `test-bench/skills_lab/` — `core.py`, `battle.py`, `pass2_battles.py`, `pass2_controlled.py`, `pass2_compare.py`
- **Tests:** `test_core.py`, `test_battle.py`, `test_pass2.py` (27 tests)

**To reproduce** (from the repository folder):

```
py -3.13 test-bench/skills_lab/test_core.py
py -3.13 test-bench/skills_lab/test_battle.py
py -3.13 test-bench/skills_lab/test_pass2.py
py -3.13 test-bench/skills_lab/pass2_battles.py --pairs 300 --out <new folder>
py -3.13 test-bench/skills_lab/pass2_battles.py --pairs 300 --group nrv-timing --out <new folder>
py -3.13 test-bench/skills_lab/pass2_controlled.py --n 100000 --out <new folder>
py -3.13 test-bench/skills_lab/pass2_compare.py
```

Seeds are fixed at 20260927. Each battle seed is played twice with sides swapped.