---
type: reference
title: Skill Sim — Findings
tags: [settlements/reference, settlements/analysis]
---
# 🧠 Skill Sim — Findings

First quantified pass over the **dice-testable** skills in [[Skill Paths]]. Engine mirrors the locked core + nerve rules exactly; 10,000 samples per duel, seed `20260710`. Run: `test-bench/skills_sim.py`.

> [!warning] Scope — most skills are NOT dice questions
> Only ~40 of the ~150 skills resolve to a probability. **Hacking, terrain, spotting, objective-running, positioning, and most control skills** are worth what the **scenario and points cost** make them — you can't Monte-Carlo them without a board. This note covers the flat modifiers, multi-attack, grapple, and the whole Bravery path. Everything else is a **playtest / points** question.

> [!success] Headline — the "spend Stress for aggression" skills were broken by Shaken; now fixed
> **Feed the Anger, Red Mist and Fanatic were traps under the new nerve math**, because **Shaken-at-1** cancelled the bonus on the same activation you spent the Stress (Feed the Anger netted *exactly zero* on a clean turn — the −1 Shaken and +1 melee washed). **Fixed** by the *"ignore Shaken while raging"* clause, now written into all three in [[Skill Paths]]. Post-fix: Feed the Anger used well is **break-even** (a fair T1); Red Mist and Fanatic read as **situational** rather than trap — see §5.

## 1 · Flat combat modifiers — raw % bought (exact)
| Skill | Effect | Base | With | Δ |
|---|---|:--:|:--:|:--:|
| **Dead Eye** | +1 hit (no move / no cover) | 60% | 70% | +10% |
| **The Muscle** | +2 injury (1st charge hit) | 60% | 80% | +20% |
| **Heavy Hands** | +1 melee vs Pinned/Grappled | 45% | 55% | +10% |
| **Feint** | +2 melee (hidden approach) | 45% | 64% | +19% |
| **Ghost Blade** | AGI 4 melee vs STR 2 | 45% | 64% | +19% |

Clean **+10%/point**, capped 90% by the nat-1 rule — exactly as priced. A +2 conditional (Feint/Ghost Blade/The Muscle) is a ~+20% swing *when its condition is met*; that condition is the balancer.

## 2 · Multi-attack — expected wounds / activation
| Skill | Wounds/act | vs single | Cost |
|---|:--:|:--:|---|
| Single shot (DEX+2, med+2) | 0.36 | — | — |
| **Quick Shot** (2 shots, 2nd −2) | 0.60 | **+67%** | no Reactions this round |
| Single melee (even STR, +1 wpn) | 0.23 | — | — |
| **Dual Wield** (2 swings, 2nd −2) | 0.37 | **+62%** | no Charge |
| **Gunslinger** (2 targets) | — | **0 in a 1v1** | only pays vs multiple foes |

A second attack even at −2 is a **~+60–67% output** spike — the biggest raw DPS jump in the game. The "no Reactions / no Charge" riders are load-bearing; without them these are auto-includes.

## 3 · Grapple chain
| Step | Odds |
|---|:--:|
| Grapple lands (even STR) | 45% |
| Grapple lands (STR +2 grappler) | 64% |
| Victim escapes next activation (even) | 45% |
| …escapes vs a STR +2 grappler | 28% |
| Squeeze auto-hit injures (unarmed vs arm 0) | 40% / use |
| Heavy Hands on the Grappled target | 45% → 55% |

A **STR-heavy grappler is a hard lock**: 64% to land it, victim only 28% to break free each turn, ~40% to injure every Squeeze in between. Grapple + Squeeze/Crushing Hold is a genuine control engine — watch that a high-STR grappler doesn't trivialise single elite targets.

## 4 · Bravery path — break-rate impact (NRV+2)
| Build | Stress 2 | 3 | 4 |
|---|:--:|:--:|:--:|
| Baseline NRV+2 | 50% | 60% | 70% |
| **Rattle-Proof** (effective −1 Stress) | 40% | 50% | 60% |
| **Cowed** on you (−1 that test) | 60% | 70% | 80% |
| **Braced** (+1 that test) | 40% | 50% | 60% |

Rattle-Proof/Braced each shave **~10%** off breaking. **Steady / Count Breaths don't change per-test odds** — they win by cutting how *often* you test (shedding Stress before it hits 2), which is why they post huge duel numbers below.

## 5 · Marquee duel — "is it worth a point?"
Each skill given to **side A** in a WND-3 mirror; B is plain. Baseline **50%**; the edge is the skill's raw value in straight attrition (10k fights).

| Skill | A win% | Edge | Read |
|---|:--:|:--:|---|
| **Quick Shot** | 74% | **+24** | biggest single-skill swing |
| **Dual Wield** | 73% | **+23** | melee equivalent |
| **Rattle-Proof** | 73% | **+23** | composure dominates long fights |
| **Steady** | 73% | **+23** | ″ (shed before you test) |
| **Feint** | 71% | **+20** | clean +2 when set up |
| **Ghost Blade** | 70% | **+20** | AGI 4 duelist |
| **Tough** (WND+1) | 65% | **+15** | more health = more attrition |
| **Dodge** | 63% | **+13** | −1 to be meleed |
| **Dead Eye** | 60% | **+10** | flat +1 ranged |
| **Iron Will** | 56% | **+6** | one free pass = insurance |
| **The Muscle** | 54% | **+3** | burst, not attrition (see note) |
| **Feed the Anger** *(once, fixed)* | 49% | **−1** | now break-even; value is the key hit |
| **Fanatic** *(fixed)* | 43% | **−7** | value is *not routing* — board presence, unmeasured in 1v1 |
| **Red Mist** *(once, fixed)* | 36% | **−14** | situational nuke — a bad even-fight pick by design |

*Post-fix numbers (the "ignore Shaken while raging" clause is applied). **Never spam the fury skills:** Red Mist spammed every activation = **1.7%**, Feed the Anger spammed = **36%** — one use, at the right moment.*

> [!note] "Low" scores that aren't actually weak
> **The Muscle (+3%)** and **Iron Will (+6%)** look mild because a pure attrition duel doesn't reward them — The Muscle is a **charge alpha-strike** (its value is the opening kill, not the grind), and Iron Will is **one-per-game insurance**. Both do their job outside the metric. Don't buff them off this number.
> **Steady / Rattle-Proof (+23%)** are only that strong because WND-3 fights *last*. In a fast **WND-1** fight — the common case — Stress rarely reaches 2, so they're worth close to nothing. Their power **scales with fight length**, so T1 is defensible; revisit if WND-2+ units become normal.

## The self-Stress fix — APPLIED
Feed the Anger, Red Mist and Fanatic are meant to be **high-risk aggression**, but pre-fix the rules made them *self-defeating*, not risky:
1. **Shaken cancelled the bonus.** Gaining Stress → −1 to all rolls → the +1/+2 melee washed out on the very attack it was meant to boost.
2. **BugOut-at-4 punished the cost twice.** Red Mist's +3 Stress lands you at the break-4 threshold in one use; Fanatic's +2 rushes you to a *rout* (removed) instead of a survivable skip.

> [!success] Fix (now in [[Skill Paths]]) — "ignore Shaken while raging"
> While using **Feed the Anger / Red Mist** (and while **Fight**-driven via **Fanatic**), the fighter **ignores Shaken's −1** for that activation. The bonus is now real and the *only* cost is the break risk — the intended gamble.

| Skill | Before | After (used once) |
|---|:--:|:--:|
| Feed the Anger | −30% (net-zero trap) | **−1% — break-even** |
| Fanatic | −10% | **−7% — Fight turns now land** |
| Red Mist | −49% | **−14% — real +2, still a nuke** |

Red Mist stays a **one-shot nuke** by design (one use ≈ Broken-risk that round, two = BugOut) — correct for a "Berserker, high-risk" T3; it's a finisher, not an even-fight tool.

## Takeaways
1. ✅ **Flat modifiers, multi-attack, grapple and composure are all correctly priced** — the +10%/point spine holds and the conditional +2s are strong-but-gated.
2. 💥 **A second attack (Quick Shot / Dual Wield) is the biggest DPS lever** — keep the no-Reaction / no-Charge riders.
3. 🧊 **Composure scales with fight length** — huge in WND-3, near-nil in WND-1. Fine at T1 while WND-1 is the norm; watch it.
4. 🔒 **STR grapplers are a hard lock** — points-cost or scenario counters needed so they don't neutralise single elites for free.
5. ✅ **Self-Stress cluster fixed** (Feed the Anger / Red Mist / Fanatic) with the "ignore Shaken while raging" clause — Feed the Anger is now break-even, Red Mist a correct situational nuke. The only balance casualty of Shaken-at-1, now closed.

---
*Not covered (needs board/scenario/points, not dice): all INT/hacking, terrain & positioning, spotting, objective, and team-support skills (Rally, Talk Them Down, Bodyguard, etc.). Next pass worth running: multi-model fights so team-support and Grapple-vs-focus-fire actually register.*

See [[Skill Paths]] · [[Conditions]] · [[Morale]] · [[Dice Mechanic — Sim Findings]].
