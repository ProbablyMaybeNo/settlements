---
type: reference
title: Terrain · Hacking · Cover — Sim Findings
tags: [settlements/reference, settlements/analysis]
---
# 🧪 Terrain · Hacking · Cover — Sim Findings

Ran the **P1 dice battery** from [[Terrain Hacking Cover — Test Plan]] on the locked S3 rules. Exact math where closed-form, seeded Monte-Carlo (10k) for chains. Run: `test-bench/terrain_hacking_sim.py`, seed `20260713`.

> [!success] Headline
> The **cover / hacking / terrain math is sound**, and terrain does the balancing job it's supposed to (heavies pay ~10% on every climb). Three things need a dial before they hit a table: **hacker shut-outs are far too weak**, a **2" fall is a coin-flip kill**, and **Disengage is a dead option** (double-costed).

## 🔴 Fix before playtest

### T6 · Hacker shut-outs are too weak
Opposed INT (ties→def) → Effect roll (1d10≥7) → Shut-out table. Triple-gated:

| INT Δ | win opposed | payload lands | **real effect** | nothing |
|:--:|:--:|:--:|:--:|:--:|
| −2 | 28% | 11% | **9%** | 91% |
| 0 | 45% | 18% | **14%** | 86% |
| +2 | 64% | 26% | **20%** | 80% |

An even-INT shut-out does anything real **14% of the time — for a whole activation**. Nobody will take it.
> [!warning] Fix — cut the Effect roll
> Winning the opposed INT *is* the payload; go **straight to the Shut-out table**. That lifts even-INT to ~**36%** real, INT+2 to ~**51%** — worth an activation and still gated by needing a terminal + winning the duel. (The 20% Glitch band on the table already provides the "close but nothing" outcome.)

### T3 · A 2" fall is a coin-flip kill
`1d10 + (1 per full 2") ` ignoring Armor:

| Fall | +Dmg | P(wound) = P(Down) at WND 1 |
|:--:|:--:|:--:|
| 2–3" | +1 | **50%** |
| 4" | +2 | 60% |
| 6" | +3 | 70% |
| 8" | +4 | 80% |

A 2" curb downing half of WND-1 fighters is too swingy for involuntary falls (knockback off a low ledge).
> [!warning] Fix — floor the Injury
> **2–3" fall = Prone only, no Injury roll.** Injury rolls start at **4"+** (`+1 per full 2"` as now). Big drops stay lethal; a low ledge just knocks you flat. Voluntary 2–3" drops keep the AGI-7+ clean-landing option.

### T8 · Disengage is a dead option
Both slots (whole activation) **and** a −2 free swing from every engager:

| Leaving | P(Downed while fleeing) |
|:--:|:--:|
| 1 engager | 14% |
| 2 engagers | 26% |

Two costs stacked = nobody disengages; they just die in place.
> [!warning] Fix — one cost, not two
> Make Disengage a normal **Move** (not both slots) that **provokes the −2 swings.** The swing is the risk; you keep your Action. (Or keep both-slots and drop the swings — but the swing version is the more interesting play.)

## 🟡 Watch (working, flagged)
- **T4 · Height** — an attacker 2"+ up ignores Light cover, turning a Light target into an open one: **50%→60% to-hit, ~+20% lethality**, 3.3→2.8 shots-to-Down. **Heavy cover still counts from above**, so real cover defeats height — but watch roof-camping on maps that are mostly Light cover.
- **T10 · Brutal shotgun (close)** = +3 & Brutal(+1) = **+4 injury = 80% wound at Armor 0** — the top of the scale. Its gates (close range, Loud, Two-Handed, Spread) should hold it; **keep Brutal off any longer-ranged weapon.**

## ✅ Validated
| Test | Result |
|---|---|
| **T1 Cover ladder** | Clean −10%/step. Open 60%/2.8 shots → Hidden 30%/5.6 shots. Cover is *the* survival lever. |
| **T2 Cover vs ±3 cap** | Our **cover-separate** ruling holds: Shaken stays worth a real **−10%** even into Hidden (20% vs 30% under a shared cap). |
| **T5 Hacking curve** | Clean band ladder; Long unusable for low INT (INT+0 @ Long = 10%) → rewards the specialist. |
| **T7 Search** | Modest, fair: INT+2 attempt ≈ 0.24 Resource + 0.18 gear, 6% self-Pin. A real commitment (exhausts the piece). |
| **T9 Traversal + armour** | **Heavy armour = −10% on every terrain test**; a failed climb → fall → Prone. **This is the lever that makes terrain punish the Heavy Gunner** — confirms the [[Dice Mechanic — Sim Findings]] §6 thesis. |
| **T11 Overload** | Rare (shut-out 10 only) and modest (40% injury at Armor 0). Fine as a spike. |

## Interaction worth noting
**Climb → fall → death** compounds: at AGI+2 a climb fails **40%** of the time, and a fall from height then wounds 50–80%. So sending a mid-AGI fighter up high terrain is genuinely dangerous — good (verticality has teeth), but the T3 fall-floor fix keeps it from being *random* death on low features.

---
*Next: re-run T6 after cutting the Effect roll to confirm the ~36%/51% landing rates; and a multi-model pass so team-hacking (Computer Whiz, Turret Tamer) and focus-fire register.*

See [[Terrain Hacking Cover — Test Plan]] · [[Hacking]] · [[Terrain]] · [[Damage]] · [[Movement]] · [[Dice Mechanic — Sim Findings]].
