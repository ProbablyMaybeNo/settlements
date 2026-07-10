---
type: reference
title: Skill Sim — Findings
tags: [settlements/reference, settlements/analysis]
---
# 🧠 Skill Sim — Findings

First quantified pass over the **dice-testable** skills in [[Skill Paths]]. Engine mirrors the locked core + nerve rules exactly; 10,000 samples per duel, seed `20260710`. Run: `test-bench/skills_sim.py`.

> [!warning] Scope — most skills are NOT dice questions
> Only ~40 of the ~150 skills resolve to a probability. **Hacking, terrain, spotting, objective-running, positioning, and most control skills** are worth what the **scenario and points cost** make them — you can't Monte-Carlo them without a board. This note covers the flat modifiers, multi-attack, grapple, and the whole Bravery path. Everything else is a **playtest / points** question.

> [!danger] Headline — the "spend Stress for aggression" skills are broken by Shaken
> **Feed the Anger, Red Mist and Fanatic are traps under the new nerve math.** The culprit is **Shaken-at-1**: the moment a skill gives you Stress you're at −1 to all rolls, so *the bonus you just bought is cancelled on the same activation*. Feed the Anger (+1 melee for +1 Stress) nets **exactly zero** on a clean turn — you gain −1 Shaken and +1 melee, they wash — and then you carry the −1 and the break risk. Red Mist spammed wins **0.7%**. This needs a fix (below), it's the one real casualty of locking Shaken at 1.

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
| **Fanatic** | 40% | **−10** | ⚠ self-Stress trap |
| **Feed the Anger** | 20% | **−30** | ⚠ self-Stress trap |
| **Red Mist** | 1% | **−49** | ⚠ self-Stress trap |

> [!note] "Low" scores that aren't actually weak
> **The Muscle (+3%)** and **Iron Will (+6%)** look mild because a pure attrition duel doesn't reward them — The Muscle is a **charge alpha-strike** (its value is the opening kill, not the grind), and Iron Will is **one-per-game insurance**. Both do their job outside the metric. Don't buff them off this number.
> **Steady / Rattle-Proof (+23%)** are only that strong because WND-3 fights *last*. In a fast **WND-1** fight — the common case — Stress rarely reaches 2, so they're worth close to nothing. Their power **scales with fight length**, so T1 is defensible; revisit if WND-2+ units become normal.

## The self-Stress fix
Feed the Anger, Red Mist and Fanatic are meant to be **high-risk aggression**, but the current rules make them *self-defeating*, not risky:
1. **Shaken cancels the bonus.** Gaining Stress → −1 to all rolls → the +1/+2 melee washes out on the very attack it's meant to boost.
2. **BugOut-at-4 punishes the cost twice.** Red Mist's +3 Stress lands you at the break-4 threshold in one use; Fanatic's +2 rushes you to a *rout* (removed) instead of a survivable skip.

> [!success] Recommended fix — "ignore Shaken while raging"
> While a fighter is using **Feed the Anger / Red Mist** (and while **Fight**-driven via **Fanatic**), **ignore Shaken's −1** for that activation. Now the bonus is real (Feed the Anger = a true net +1, not 0) and the *only* cost is the break risk — which is the intended gamble. Red Mist stays a **one-shot nuke** (one use ≈ Broken-risk end of round, two = BugOut), which is correct for a "Berserker, high-risk" T3. This is a one-line clause on three skills, no system change.
> Alternative if you'd rather not touch the skills: **self-inflicted Stress doesn't impose Shaken on the activation it's spent** (a general rule) — cleaner conceptually, slightly wider blast radius.

## Takeaways
1. ✅ **Flat modifiers, multi-attack, grapple and composure are all correctly priced** — the +10%/point spine holds and the conditional +2s are strong-but-gated.
2. 💥 **A second attack (Quick Shot / Dual Wield) is the biggest DPS lever** — keep the no-Reaction / no-Charge riders.
3. 🧊 **Composure scales with fight length** — huge in WND-3, near-nil in WND-1. Fine at T1 while WND-1 is the norm; watch it.
4. 🔒 **STR grapplers are a hard lock** — points-cost or scenario counters needed so they don't neutralise single elites for free.
5. ⚠️ **Fix the self-Stress cluster** (Feed the Anger / Red Mist / Fanatic) with the "ignore Shaken while raging" clause — the only real balance casualty of Shaken-at-1.

---
*Not covered (needs board/scenario/points, not dice): all INT/hacking, terrain & positioning, spotting, objective, and team-support skills (Rally, Talk Them Down, Bodyguard, etc.). Next pass worth running: multi-model fights so team-support and Grapple-vs-focus-fire actually register.*

See [[Skill Paths]] · [[Conditions]] · [[Morale]] · [[Dice Mechanic — Sim Findings]].
