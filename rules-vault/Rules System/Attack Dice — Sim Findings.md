---
type: reference
title: Attack Dice — Sim Findings
tags: [settlements/reference, settlements/analysis, settlements/mechanic/attack-dice]
---
# 🎲 Attack Dice — Sim Findings

Sim pass on [[15b · Attack Dice]], run 2026-08-29. Mirrors the [[core-000 Core Test]] / [[Dice Mechanic — Sim Findings]] harness exactly — same core test, same seed `20260708`, same 10,000-sample standard. Harness: `test-bench/attack_dice_sim.py`, stamped as `attack-dice-15b-n10000-e2b861d61-h326cd413`.

**Every headline figure here is exact**, by full enumeration of the 10-face space. The chain is analytically closed, so Monte-Carlo would only add sampling error; the 10k run is carried as a cross-check and agrees in every cell.

> [!success] Headline
> **The mechanic works and the brief's own arithmetic is right.** 36 / 59 / 74% P(≥1 wound) reproduces exactly. Three things do not survive contact:
> 1. **The linearity assumption breaks at WND 1** — which is everyone. E[wounds] is capped at 1.0 by construction.
> 2. **AD 3 is an auto-include**, beating the Heavy Gunner benchmark by **+51%** on identical fielded Credits — and **Attack Dice break the stat ceiling**: a DEX +0 Recruit with 3 dice out-shoots a DEX +6 marksman. Price cannot fix that; it needs a gate.
> 3. **The cost step runs the wrong way.** Fair is **+40 then +25** (65 cumulative), not +25 then +35. Die 2 is the expensive one.
>
> *(An earlier draft of this note said the table was "roughly half price". That was the uncapped-overkill reading and is corrected in §6.)*

> [!success] RULED 2026-08-29 — a burst inflicts at most ONE wound
> Ross ruled the resolution after this pass: **roll every die's chain at once, apply one Injury result of the attacker's choice, and every other hit that failed to wound still Pins.** That settles the blocking question below in favour of a hard **one-wound cap per Action**. The rule is now law in [[Full Rules System v1]] §15 and [[Weapons]] §1.5.
>
> Consequences measured in the follow-up pass (`test-bench/attack_dice_rules_compare.py`, stamped):
> - **The candidate rules were never an offence choice.** P(Down) is *identical* — 73.8% at AD 3 — under all four resolutions. The order you learn a wound in cannot change whether it happened.
> - **The one-wound cap is the load-bearing half.** A 3-die weapon now takes a WND-2 or WND-3 veteran from full to Down **0%** of the time, against **29.5%** / **4.7%** if surplus wounds stacked. Attack Dice shred rank-and-file and do not melt characters.
> - **Step 4 — surplus whiffs still Pin — is the one sub-decision still owed a tick.** It is the *only* thing separating the two candidates. Dropping it cuts effective suppression **14–40%** and caps a burst at one Stress, making a 3-die burst suppress exactly as hard as a pistol.
> - **The fair price is 40 / 65 and the step runs DOWNWARD** — see §6, rewritten.
>
> §§1–5 below stand as measured. §6's pre-ruling recommendation is superseded.

## The blocking ruling — now settled, see banner

The brief's sim ask assumes the dice are independent. That is only true if surplus dice have somewhere to go. **At WND 1, die 1 wounding means the target is already Down when dice 2 and 3 resolve.** So there are two engines, not one:

| Reading | What it means |
|---|---|
| **`resolve_all`** | Every die resolves regardless. Correct if surplus dice may be redirected, or against WND 2–3 campaign veterans. |
| **`stop_on_down`** | The sequence ends at Down; surplus dice are lost. Correct at WND 1 with dice locked to one target. |

This is **the same question as the brief's split-fire item**, and the draft answers neither. It is worth **21–32% of AD 3's output** and it changes the *shape* of the correct price, not just the level. Nothing can be finalised until it is ruled. Both columns are reported below rather than averaged.

## 1 · P(at least 1 wound) per Action — the brief's headline holds

Standard **DEX +2** shooter, medium weapon (**+2**). Identical under both readings — "at least one" cannot care what happens after the first.

| Cover | Armour | AD 1 | AD 2 | AD 3 |
|---|---|:--:|:--:|:--:|
| Open | Unarmoured | 36.0% | 59.0% | **73.8%** |
| Light | Unarmoured | 30.0% | 51.0% | 65.7% |
| Heavy | Unarmoured | 24.0% | 42.2% | 56.1% |
| Hidden | Unarmoured | 18.0% | 32.8% | 44.9% |
| Open | Light | 30.0% | 51.0% | 65.7% |
| Light | Light | 25.0% | 43.8% | 57.8% |
| Heavy | Light | 20.0% | 36.0% | 48.8% |
| Hidden | Light | 15.0% | 27.8% | 38.6% |
| Open | Heavy | 24.0% | 42.2% | 56.1% |
| Light | Heavy | 20.0% | 36.0% | 48.8% |
| Heavy | Heavy | 16.0% | 29.4% | 40.7% |
| Hidden | Heavy | 12.0% | 22.6% | 31.9% |

^tbl-1-p-at-least-one-wound

The draft's **36 / 59 / 74** is confirmed to the decimal. The baseline holds across every band — it degrades smoothly with cover and armour, no cliff anywhere.

> [!note] The front-loading is real but it is not a fact about die 2
> The draft justifies a stepped cost because "tempo-compression value is front-loaded on die 2". The Δ2/Δ3 ratio is exactly **1/(1−w)** in every cell — it runs **1.14 to 1.56** depending on band, and is highest where the target is softest. The draft's ~1.4× step sits inside that range, so **the stepped shape is defensible under `resolve_all`**. Under `stop_on_down` it inverts — see §6.

## 2 · E[wounds] per Action — linearity fails at WND 1

| Cover / Armour | `resolve_all` AD1/2/3 | `stop_on_down` AD1/2/3 | AD 3 overkill |
|---|:--:|:--:|:--:|
| Open / Unarmoured | 0.360 / 0.720 / **1.080** | 0.360 / 0.590 / **0.738** | **31.7%** |
| Light / Light | 0.250 / 0.500 / 0.750 | 0.250 / 0.438 / 0.578 | 22.9% |
| Heavy / Heavy | 0.160 / 0.320 / 0.480 | 0.160 / 0.294 / 0.407 | 15.1% |
| Hidden / Heavy | 0.120 / 0.240 / 0.360 | 0.120 / 0.226 / 0.319 | 11.5% |

^tbl-2-e-wounds-per-action

The brief predicts **~0.36 / 0.72 / 1.07**. That is the `resolve_all` column for open/unarmoured and it is exactly right *there*. Under `stop_on_down` the same cell reads **0.738** — die 3 adds 0.148, not 0.360.

**At WND 1, E[wounds] can never exceed 1.0.** Linearity is not merely unobserved, it is unreachable. A multi-die weapon locked to one WND-1 target wastes **11–32%** of its output, worst against the soft targets it is best against.

## 3 · E[Stress] per Action — the suppression identity is real

Stress accrues **only on a hit that fails to wound**. A wound gives no Stress ([[Conditions]] §Stress hook — Pinned's +1 *is* the non-wounding result, don't count it twice).

> [!danger] `sim_report.py` has this wrong, and it moves a published number
> `attack()` adds Stress on **both** branches — a wound *and* a failed wound. The rules say a hit does exactly one thing. At WND 1 the divergence is invisible, because a wound ends the fight, which is why it survived unnoticed. **At WND 3 it is not invisible.** Re-running that harness's own `duel_stats` both ways, 10k fights, same seed:
>
> | | WND 1 | WND 3 |
> |---|:--:|:--:|
> | `sim_report.py` as written | 0.087 | **1.763** |
> | Rules-correct (Pin only) | 0.090 | **0.744** |
> | Change | +4.2% (noise) | **−57.8%** |
>
> The **"~1.75 breaks per fight"** in [[Dice Mechanic — Sim Findings]] §7 — the evidence for "morale is now a **duration** mechanic", which "self-corrected the inert morale problem" — is **roughly double** what the written rules produce. The correct figure is **~0.74**. The qualitative conclusion may well survive (0.74 is still far above the WND-1 rate of 0.09, so morale does still wake up in grinds), but the headline number is wrong and the margin is smaller than the note claims.
>
> **This is a separate defect from Attack Dice and wants its own pass.** Nothing in this note depends on it — the Attack Dice harness applies the rules-correct version throughout.

| Cover / Armour | `resolve_all` AD3 | `stop_on_down` AD3 | P(Break test) AD3 |
|---|:--:|:--:|:--:|
| Open / **Heavy** | **1.080** | **0.842** | **23.3%** |
| Open / Light | 0.900 | 0.657 | 16.2% |
| Open / Unarmoured | 0.720 | 0.492 | 10.4% |
| Hidden / Heavy | 0.540 | 0.478 | 7.8% |
| Hidden / Unarmoured | 0.360 | 0.299 | 3.5% |

^tbl-3-e-stress-per-action

> [!note] Which Stress measure is this?
> The table above is the **raw** measure — every Pin the dice produced, including Pins landing on a target the same Action then put Down. The follow-up pass also computes the **live** measure: Stress on a target *still standing*. Pinned restricts Move/Charge/Sprint/Disengage and feeds a Break test, none of which a Down model can do or take, so **live is the number that measures suppression**. For open/unarmoured AD 3 the two read **0.492 raw / 0.295 live**. Both are carried in the stamped JSON; neither is hidden. The Break-test column is computed on the live basis and is unaffected.

**Cover and armour push Stress in opposite directions.** Stress is `p_hit × (1 − p_wound)`: cover cuts *both* wounds and Stress, while armour *converts* wounds into Stress. So the suppression payoff peaks on an **armoured target in the open**, not a dug-in one. A 3-die weapon into a dug-in target is simply weak.

The Break column is the real result: **one 3-die Action puts an armoured, exposed target into Break-test range 23.3% of the time on its own**, from a standing start of zero Stress. That is a genuine second identity, not a consolation prize — and it is the honest justification for the mechanic.

## 4 · Activations-to-Down, points-normalized — the costing table fails

Live prices from `points/ticks.py`: Standard Ranged +2 @18" = **15 Cr** · Sidearm +2 = **15 Cr** · Fighter = **100 Cr** · Recruit = **70 Cr**.

Target in **light cover / light armour** (the modal cell). Lower `Cr·acts` is better.

| Configuration | Cr | Dice/act | P(Down) | E[acts] | **Cr·acts** |
|---|--:|:--:|:--:|:--:|--:|
| 1× Fighter, rifle **AD 3** | 175 | 3 | 57.8% | 1.73 | **303** ⬅ best |
| 1× Fighter, rifle **AD 2** | 140 | 2 | 43.8% | 2.29 | 320 |
| 1× Fighter, rifle +4 dmg | 135 | 1 | 35.0% | 2.86 | 386 |
| 2× Recruit, pistol | 170 | 2 | 43.8% | 2.29 | 389 |
| 1× Fighter rifle + 1× Recruit pistol | 200 | 2 | 43.8% | 2.29 | 457 |
| 1× Fighter, rifle **AD 1** | 115 | 1 | 25.0% | 4.00 | **460** ⬅ worst |

^tbl-4-activations-to-down

**The stepped price does not close the tempo gap.** AD 3 at full draft cost is the *most* Credit-efficient way to put a body down, and AD 1 is the least. Every Attack Dice rung beats the two-cheap-bodies build the mechanic is supposed to lose to.

> [!important] The reason is the denominator
> Attack Dice are bought per **weapon** but they multiply the output of a **body**, and the body is the expensive part — a Fighter is **100 Cr** against a **15 Cr** rifle. A second die costs **25 Cr**; a second body to fire a second die costs **85 Cr**. **Any per-die price below the price of a body makes dice the efficient purchase**, and 25 is far below it.
>
> *Honest caveat:* two bodies also bring a second activation, a second objective-carrier and a second body to lose — real value this test does not price, because it measures shooting only. It does not close a 1.5× gap.

## 5 · Auto-include check — flag raised

Cost is **fielded** (body + weapon). Open target, unarmoured.

| Fielded purchase | Cr | Wounds/act | **per 100 Cr** |
|---|--:|:--:|--:|
| Fighter + Std Ranged +2 (baseline) | 115 | 0.360 | 0.313 |
| Fighter + Std Ranged +3 | 125 | 0.420 | 0.336 |
| Fighter + Std Ranged +4 | 135 | 0.480 | 0.356 |
| **Specialist + Heavy Ranged +3 (Heavy Gunner)** | 175 | 0.490 | **0.280** |
| Fighter + rifle **AD 2** (`stop`) | 140 | 0.590 | 0.422 |
| Fighter + rifle **AD 3** (`stop`) | 175 | 0.738 | **0.422** |
| Fighter + rifle AD 3 (`resolve_all`) | 175 | 1.080 | 0.617 |

^tbl-5-auto-include-check

> [!danger] AD 3 is an auto-include at the draft price
> Every Attack Dice rung outperforms every Damage step per Credit, and **AD 3 beats the Heavy Gunner benchmark by +51% on identical fielded Credits (175 vs 175)** — under the *pessimistic* `stop_on_down` reading. Under `resolve_all` it is worse again.
>
> [[Dice Mechanic — Sim Findings]] takeaway #6 asked for price-plus-terrain-gate on Heavy Gunner. This wants the same treatment: **the derived price below, AND a rarity/rank gate.**

## 6 · What it should cost — derived, not asserted

The catalogue's own offensive exchange rate is `CREDITS_DAMAGE` = **10 Cr per +1 Damage**. On the modal open target that buys **+0.060 wounds/Action**, so the shipped rate is **167 Cr per 1.0 wounds/Action**. Pricing the dice at the catalogue's own rate:

| Reading | Die 2 marginal | Die 3 marginal | Cumulative | Draft | Draft / fair |
|---|--:|--:|--:|--:|--:|
| `resolve_all` | 60 Cr | 60 Cr | **60 / 120** | 25 / 60 | 0.42× / 0.50× |
| `stop_on_down` | 38 Cr | 25 Cr | **38 / 63** | 25 / 60 | 0.65× / 0.95× |

^tbl-6-derived-fair-price

Both readings agree in direction: **the draft is underpriced**. The draft's own instinct — that a flat per-die price "would underprice die 2" — was right in direction and much too small in magnitude.

They **disagree on the shape**, and that disagreement is the whole ruling:

- `resolve_all` → dice are **linear** (60 / 60). A flat per-die price is correct; the stepped table is the wrong shape.
- `stop_on_down` → dice **decay** (38 / 25). Die 3 is worth *less* than die 2, so the step should run **downward**.

**The draft's stepped-upward table (+25 then +35) is the one shape that is wrong under both readings.** That finding does not depend on which way the WND-1 ruling goes.

> [!success] SUPERSEDED BY THE RULING — the price is 40 / 65, and all four rules agree
> The follow-up pass prices every candidate resolution and they come out **identical: +40 (AD 2) then +25 (AD 3), 65 cumulative.** They deliver the same wounds, and the catalogue's exchange rate prices wounds only — so the rule choice was free at the till and paid for in suppression and character durability instead.
>
> **This corrects the "roughly half price" line above.** That came from `resolve_all`'s *uncapped* E[wounds] (60/120 fair), which counts overkill on a WND-1 target as value. It is not value. Capped at the target's actual WND — which the ruling now makes universal — the honest figures are:
>
> | | Fair | Draft | Gap |
> |---|:--:|:--:|:--:|
> | **AD 2** | **40** | 25 | **−35%**, the underpriced rung |
> | **AD 3** | **65** | 60 | −5%, close to right |
>
> **The step runs downward: +40 then +25.** The draft's +25 then +35 is backwards. Because a burst caps at one wound, die 2 buys **+0.230** wounds/Action and die 3 only **+0.148** — die 2 is the expensive one.
>
> **The auto-include finding in §5 is unaffected and still stands.** It compares Attack Dice against *bodies*, not against the Damage ladder. Both are true at once: the price matches the damage-step rate, and the damage ladder is itself cheap next to a 100 Cr Fighter.

## Design takeaways
1. ✅ **The brief's probability arithmetic is exactly right** — 36 / 59 / 74 reproduces to the decimal, and the baseline holds across all twelve cover×armour bands.
2. ⚠️ **Linearity fails at WND 1** — E[wounds] is capped at 1.0 by construction; AD 3 wastes 11–32% of its output. The brief's ~1.07 figure is `resolve_all` only.
3. 🎯 **Suppression is a genuine second identity**, and it peaks on *armoured, exposed* targets — not dug-in ones. 23.3% chance of a Break test from one Action.
4. 💸 **The costing table is roughly half price.** AD 3 at +60 is the best Cr-per-outcome buy on the board and beats Heavy Gunner by 51%. **Auto-include flag raised.**
5. 🔁 **The stepped-upward shape is wrong under both readings** — flat under `resolve_all`, decaying under `stop_on_down`. Never increasing.
6. 🚧 **One ruling blocks the rest:** does a multi-die weapon keep rolling after the target goes Down? Same question as split fire. Worth 21–32%.

## Still open — rulings, not sim outputs
- [ ] **WND-1 down-rule** (`resolve_all` vs `stop_on_down`). **Blocking** — sets the fair price *and* its shape.
- [ ] **Split fire** — same question wearing a different hat. Split fire makes `resolve_all` the right model by giving surplus dice somewhere to go.
- [ ] **1 Action or both slots?** §4 measures 1 Action. Both-slots roughly halves the tempo value and would move the fair price down by about half.
- [ ] **Is 3 the ceiling?** Nothing in the maths breaks past 3, but overkill waste grows and the auto-include gap widens with it.

---
*Harness `test-bench/attack_dice_sim.py`; raw JSON at `test-bench/balance/results/attack-dice-15b.json`. Every figure is browsable in the Sim Explorer (`powershell -File test-bench/explorer/serve.ps1`) — query 4, "Attack Dice", carries the full grid, and query 1 answers any stat-line/weapon/cover/armour combination directly.*

> [!info] `[[15b · Attack Dice]]` is a deliberate dangling link
> The Phase 15b draft was handed over in chat and has never been filed to the vault. The link marks it as owed, not missing.

See [[15b · Attack Dice]] · [[Dice Mechanic — Sim Findings]] · [[Weapons]] · [[Shooting]] · [[Damage]] · [[Conditions]] · [[Morale]] · [[List Building]].
