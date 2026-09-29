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

---

## 002 · Skill Third Pass — 2026-09-29 contract

*Run 2026-09-29 against the next-pass contract in `Draft 2 - Simulation Assumptions`. The four suites run scripted situations only; there is no whole-game AI. They cover 29 skills plus 7 rule checks. All suites read one identical snapshot of the live notes; the hashes are in the `meta-*.json` files. Suites 1–3 reproduced byte-for-byte on a rerun.*

### Overview

- **PASSED** (works as intended): the contract hand-checks (23/23); signed per-source caps and Hidden-plus-cover stacking; Stress-free Break/Rally with Stress-based severity; the Rage → Implode cycle; Tough as Nails; Parry; Last Laugh; Commanding Presence.
- **FAILED** (needs major revision or removal): Rage alone; Menacing; Lean On Me.
- **PENDING** (promising but needs clarification or small changes):
  - **Morale and support:** Implode alone; Blowing Off Steam; Sin Eater; Inspire; Rally; On Your Feet; Motivate; Hold Fast; Big Aura.
  - **Movement and reactions:** Sprinter; Unflinching; Watch Out!.
  - **Rule under test:** Return Fire.
- **BLOCKED** (cannot be tested yet): Gunslinger, Big Fella, the Grapple family, Stabilize, hacking, deployables, chems, Hide/Sneak, Cover Me damage, Phantom Shot. None were retested; they are unsupported, not worthless.
- **INCONCLUSIVE** (results depend on unresolved assumptions): Beta Blocker; Roar.

### Report

**The biggest finding is structural. Under the new End Phase, Stress almost never reaches a roll.** Every hit Pins its survivor, so Stress and Pinned arrive together. The unit spends its next activation Recovering, and by then the End Phase has already cleared the Stress (Break pass) or turned it into a condition. In the firing line, **0%** of shots were rolled at 2+ Stress; in the melee gauntlet, **0%** of carrier attacks were. Stress on Injury rolls is a large penalty when it applies: Stress 3 cuts a rifle's expected Wounds by 62%. It just rarely applies. As a result:

- Beta Blocker has nothing to act on.
- Implode's melee bonus is never used on Stress taken from enemy hits: 0.83 Implodes per game, and a used bonus of exactly 0. The Pinned unit spends that activation Recovering.
- Implode still gives **complete Break immunity**. It replaces every Break test, so no unit carrying it ever failed Break.

**Rage alone still fails, and now for a clear reason.** Rage Stress is self-inflicted and arrives *without* Pinned. It therefore goes straight into the End-Phase Break test. Rage +3 at NRV1–3 made the carrier flee while still engaged in 72–91% of gauntlets, and win rate fell from 0.26 to 0.03 (Tough ×2 opponents, NRV3). Rage +1 and +2 were also worse than taking no skill.

**Rage + Implode works as designed and is strong.** The Rage Stress becomes next activation's +hit/+Injury, and the carrier never breaks.

| Opponents | No skill | Rage+3 + Implode | Best other 2-pick |
|---|---|---|---|
| Line ×3 | 0.52 | 0.66 | 0.64 (Tough + Implode / Tough + Parry) |
| Tough ×2 | 0.26 | 0.45 | 0.36 (Tough + Parry) |
| Heavy ×1 | 0.37 | 0.50 | 0.55 (Tough + Parry) |

- The value comes through Implode's +hit. Rage's own +3 Injury is partly or wholly capped away whenever Implode is at +2 or more, because skills cap at +4.
- **Blowing Off Steam works against Implode:** it removes the Stress that Implode would convert. Adding it lowers Rage+3 + Implode by up to 7 win points (Line −7.4, Tough −4.8, Heavy 0).

**NRV support at printed cost is mostly net-negative. The NRV test is the main obstacle, more than the Action.**

- **Motivate:** printed −0.07 to −0.15 net casualties; with no test (Action still paid) +0.20 to +0.28; completely free about +1.0.
- **Hold Fast:** printed −0.05 to +0.10 (positive when outgunned or at NRV5); with no test +0.12 to +0.32. It turns prevented Wounds into Stress, which raises friendly Break failures from 0.88 to 1.10 per game.
- **Rally skill:** no better than the generic friendly Rally action in this geometry. There were only about 0.5 opportunities per game.
- **Menacing and Lean On Me:** negative even with no test. Lean On Me stays about 0 even when free, and its absorber breaks 0.64 times per game.
- **Sin Eater:** its absorber breaks 0.54–0.69 times per game. Adding Implode removes those failures, but the pair is still net-negative (−0.05 to −0.09) because of the Action it costs.

For comparison, the equal pick **Tough** on the Leader is worth +0.13 to +0.30, and on three squad members +0.37 to +0.83.

**Sprinter** is strong on gunners inside 12". It cuts the gunner's chance of being Downed by a charging Brawler from 0.65 to 0.57 at 8" and from 0.44 to 0.25 at 12", and adds about 40% more shots. The gain disappears at 18" because the gunner reaches the end of the 36" lane. It does nothing for a Brawler. It correctly does not bypass Pinned.

**Unflinching** is worth nothing on its own. A hit that it lets the unit survive also Pins the unit, and a Pinned unit cannot use READY. It only works if a friendly Recovers the unit. That raised charge cancellation from 0.28 to 0.48, at the cost of the helper's action 45% of the time.

**Return Fire** removes the READY unit's pre-emptive cancel. Ordinary reaction-first fire cancels the attacker's shot 40–70% of the time; under Return Fire the attacker always shoots, and the exchange becomes a contest of relative modifiers. **Cover counts only as the difference between the two units' cover.** Equal cover on both sides cancels out, and a READY unit in heavy cover gets exactly the same result as one in light cover when the attacker is one step worse off.

### Findings

| Mechanic / System | Status | Brief Finding |
| ----------------- | ------ | ------------- |
| Contract hand-checks | PASSED | 23/23: d20/15+, opposed naturals, ties, empty pools, Unanswered, mixed dual wield, multiple Wounds, signed caps, Break/Rally, Pinned movement, the Rage/BOS/Implode sequence, and finite Parry/Last Laugh/Return Fire. |
| Signed caps, Hidden + cover | PASSED | DEX6 + skill 4 + weapon 3 − Hidden 4 − heavy cover 2 = +7, needs 8+ (65%). Hold Fast −2 with Tough as Nails −4 caps at −4. Implode +4 with Rage +3 caps at +4 on Injury. |
| Stress on rolls (incl. Injury) | PASSED | Works as ruled. Stress 3 cuts a rifle's expected Wounds by 62%, but 0% of rolls in either scenario were made at 2+ Stress. |
| Break / Rally procedure | PASSED | Stress-free tests (45% at NRV3). Severity follows Stress. No same-phase Rally. A failed Rally keeps its severity. |
| Rage (alone) | FAILED | +3: flees while engaged in 72–91% of gauntlets; win rate 0.26 → 0.03. +1 and +2 also below no skill. |
| Rage + Implode cycle | PASSED | +13 to +18 win points. Zero Breaks. Leads every other two-pick except against a single Heavy (3 Wounds). Watch its strength. |
| Implode (alone) | PENDING | Guaranteed Break immunity. The melee bonus is never used unless the Stress was self-inflicted. |
| Blowing Off Steam | PENDING | +0 to +2 win points alone. Costs 0–7 points when added to Rage + Implode. |
| Sin Eater | PENDING | Duel: raises Rage-alone from 0.03 to 0.13 but its absorber breaks about 1.5 times per game; adds nothing to Rage + Implode. Firing line −0.09 to −0.12 (with Implode −0.05 to −0.09). |
| Inspire | PENDING | −0.04 to −0.06 printed; about 0 to +0.04 free. |
| Rally (skill) | PENDING | −0.01 to −0.03, the same as the generic Rally action. About 0.5 opportunities per game. |
| On Your Feet | PENDING | 1.2 opportunities per game, but only 0.09 per game with two or more targets. Using it on one target: −0.07 to −0.11. |
| Motivate | PENDING | The test blocks it: printed −0.07 to −0.15; no test +0.20 to +0.28; free about +1.0 (too strong). |
| Hold Fast | PENDING | Printed −0.05 to +0.10; no test +0.12 to +0.32. Converts Wounds into Stress. |
| Big Aura | PENDING | The second aura costs another Action and test: printed −0.15 to 0; free +0.29 to +0.61. Its range was not tested (a compact line). |
| Menacing | FAILED | −0.15 to −0.23 printed and still negative with no test. The extra Stress mostly lands on targets that are already Pinned. |
| Lean On Me | FAILED | −0.20 to −0.29 printed; about 0 when free. The absorber breaks 0.64 times per game. |
| Commanding Presence | PASSED | +0.005 to +0.018. Used 0.86 times per game, adding 0.09 expected Break passes. |
| Last Laugh | PASSED | +0.01 to +0.03 on the Leader, +0.02 to +0.09 on three squad members. The chain stays finite. |
| Tough as Nails | PASSED | Duel +0 to +2 win points. The carrier never flees. |
| Parry | PASSED | Duel +2 to +3.5 win points. Triggers 0.44 times per game. No recursion. |
| Beta Blocker | INCONCLUSIVE | Exactly 0 in every scenario, including on Stress absorbers. No rolls happen at 2+ Stress. |
| Sprinter | PENDING | Gunner Downed 0.65 → 0.57 at 8" and 0.44 → 0.25 at 12". Depends on lane length. Nothing for a Brawler. |
| Unflinching | PENDING | 0 on its own. Needs a friendly Recover or On Your Feet to have any effect. |
| Watch Out! | PENDING | Same as the reactor firing itself, unless the charged friendly has a multi-die weapon (SMG: 0.50 → 0.70). |
| Roar | INCONCLUSIVE | Exact: blocks 19–41% of charge attempts. How often charges occur was not measured. |
| Return Fire (test) | PENDING | No pre-emptive cancel. Cover works only as a relative difference. |

**Opposed melee modifiers are weaker than the same modifier on a 15+ roll.** In an even exchange, +4 to hit raises P(any hit) only from 0.47 to 0.64. The Charge die adds about as much. A +3 stat difference (STR6 vs STR3) gives 0.60 against 0.36.

**The natural-roll rule (WR7) does not drive any finding.** Rerunning with modified totals only changed every result by 3 points or less. The pinned-defender choice (I1) shifts the level of results but not which loadouts come out on top.

### Assumptions and Next Steps

**Assumptions:**
- The contract's recorded rulings and working rulings WR1–WR14 were implemented as written.
- Eleven further implementation choices (I1–I11) are listed in `test-bench/skills_lab/pass3/ASSUMPTIONS-PASS3.md`. The main ones:
  - A Pinned defender still rolls and can score hits.
  - Rage applies only to attacks the carrier makes itself.
  - Fleeing while engaged is counted as its own outcome, not resolved as movement (WR5).
  - Motivate is read strictly (the second action must repeat the first).
- All stat lines, Wounds, Armour, MOVE 6, the gauntlet, the firing line and the kite lane are **fixtures**, not rules.
- Weapon traits without printed values (Suppression, Blast, Piercing, Lethal) were omitted.
- The one synthetic weapon, `synthetic_acc3_X`, was used only for the cap check.
- Leader policies are scripted. Opportunity, AI choice and effect are reported separately. The confidence interval is ±0.017 net casualties (unpaired).
- None of this measures whole-game balance or sets prices. No live rules were changed.

**Next steps:**
1. **Decide whether Stress is meant to reach rolls.** Right now Break/Rally clears it before the next roll. Possible directions: Stress that persists through a passed Break, Pinned that does not arrive with Stress, or accept it and cut Beta Blocker.
2. Decide whether Implode's **automatic Break pass** is intended. If not, add a cost such as losing the next activation's Move.
3. Make the Implode bonus usable while Pinned, or say so explicitly. Resolve the Blowing Off Steam / Implode conflict (for example, Blowing Off Steam could add to the Implode bank).
4. Remove the NRV test from action-cost support skills (Motivate, auras), or make it cheaper. Keep Motivate's Action: it is too strong when free.
5. Rework Menacing and Lean On Me.
6. Let Unflinching also keep the unit un-Pinned, or merge it into another skill.
7. Rule on Return Fire's relative-cover behaviour before adopting it.
8. Retest Sprinter on real boards once board size and MOVE are set.
9. Measure how often Roar's trigger (enemy charges) occurs once charge AI exists.

### Files

**Repository:** `D:\AI-Workstation\Antigravity\apps\Settlements`

- **Report:** `docs/SKILLS-SIM-PASS3-2026-09-29.md`
- **Assumptions:** `test-bench/skills_lab/pass3/ASSUMPTIONS-PASS3.md`
- **Instructions:** `test-bench/skills_lab/pass3/README.md`
- **Code:** `test-bench/skills_lab/pass3/`
  - `rules.py`
  - `test_contract.py`
  - `suite_rage.py`
  - `suite_stacks.py`
  - `suite_nrv.py`
  - `suite_ready_move.py`
  - `diag_stress_at_roll.py`
  - `common.py`
- **Results:** `test-bench/skills_lab/results/pass3-2026-09-29/`
  - `suite1_rage_gauntlet.csv` (252 cells × 40k)
  - `suite2_shooting_stacks_exact.csv` (12,600 exact rows)
  - `suite2_melee_opposed.csv` (180 cells × 200k)
  - `suite3_nrv_firefight.csv` (164 cells × 20k)
  - `suite4_*.csv` (kite 54 cells × 50k; Return Fire 178 × 100k; READY 12 × 100k; exact tables)
  - `diag_stress_at_roll.csv`
  - `meta-*.json` (source hashes, seeds, sample sizes)
- Pass 1 and pass 2 code and results are unchanged.

**To reproduce** (from the repository folder):

```
py -3.13 test-bench/skills_lab/pass3/test_contract.py -v
py -3.13 test-bench/skills_lab/pass3/suite_rage.py --n 40000
py -3.13 test-bench/skills_lab/pass3/suite_stacks.py --mc 200000
py -3.13 test-bench/skills_lab/pass3/suite_nrv.py --n 20000
py -3.13 test-bench/skills_lab/pass3/suite_ready_move.py --n 100000
py -3.13 test-bench/skills_lab/pass3/diag_stress_at_roll.py --n 5000
```

The base seed is 20260929; each cell and each firing-line trial uses a fixed derived seed.
