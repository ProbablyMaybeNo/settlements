---
type: research-note
title: Infinity
game: Infinity N3-N5
publisher: Corvus Belli
depth: official N5.2 wiki + N3 rulebook figures
tags: [settlements/research]
---
# 🎲 Infinity

> [!abstract] In one breath
> The **dual-currency reference implementation**. Every profile carries two prices — **Army Points** and **SWC** — and the second budget is *derived from the first* (`1 SWC per 50 points`). It has survived four editions essentially unchanged, which is the strongest evidence any mechanic in this vault has.

| | |
|---|---|
| **Publisher** | Corvus Belli |
| **Currencies** | **Army Points** (abundant, integers) + **SWC** (scarce, 0.5 granularity) |
| **Depth of read** | Official N5.2 wiki + N3 rulebook cost figures |
| **Long-form** | `docs/POINTS-RESEARCH.md` §7.2 |

---
## SWC — the derived second budget

**Type:** List · **Take:** ⭐ steal

> *"Support Weapons are the weapons or Special Equipment not included in the basic or standard equipment. These Support Weapons have a specific cost named Support Weapons Cost (SWC)… **In game terms, each 50 Army Points will provide 1 point of SWC** to spend on Troopers with Support Weapons. For example, in a standard 300 Point game, players will have 6 SWC points available."* **[FACT — official N5.2 wiki]**

- Every profile row carries **both** costs: `SWC` and `C`.
- **SWC granularity is 0.5**; values run 0, 0.5, 1 … 3.5, plus `+1`/`+2`.
- **Both Cost and SWC are Private Information** — your opponent may not ask what anything costs.
- Stacked alongside: **AVA** (per-unit availability caps), **Combat Groups** (max 10 order-generating troopers each), exactly one Lieutenant, and in N5 a hard **15-trooper cap**.
- N5 Reinforcements **splits the budget in both currencies** — *"assign a total of 100 points and 2 SWC to build their Reinforcements Section."*

**Why two currencies?** **[INFERENCE, well-supported]** Points alone cannot prevent the degenerate list, because Infinity's **order economy** makes cheap bodies individually mandatory. A single currency would force the designer to price HMGs so high nobody takes them. SWC lets them price the gun **cheaply in points** (a Fusilier HMG is only +8 points over a Combi) while **hard-capping how many exist**. **Points buy bodies and order count; SWC buys the right to have force-multipliers at all.** Two independent knobs on two independent failure modes.

**And the derived budget is the elegant part.** Because SWC is a function of points, it **auto-scales with game size** — no separate table per format. Half-point granularity on the scarce currency and integers on the abundant one is exactly right: the scarce currency needs resolution because you only get six of them.

**The load-bearing discovery — the same weapon costs more SWC on a better platform** **[FACT — N3 rulebook]**:

| HMG carrier | SWC | Points |
|---|:--:|---:|
| Fusilier (PanO line infantry) | 1 | 18 |
| Moblot / Govad | 1.5 | 29 |
| Janissary (Heavy Infantry) | 2 | 40 |
| Hsien (HI) | 2 | 61 |
| Squalo (TAG), MULTI HMG | 2 | 93 |

*Honest counter-example: the Missile Launcher is a flat 1.5 on both a 15-point Fusilier and a 49-point Father-Knight, rising to 2 only on top-tier HI. **Platform-scaling is a strong designer habit, not a stated rule.***

**For Settlements — the finding that matters.** Settlements has **already built an SWC equivalent**, but implemented it as **rank gates** rather than a second currency **[INFERENCE]**:

| SWC-like capability | How we gate it |
|---|---|
| **Orders** | Leader/Specialist only — the rank pyramid |
| **Extra-action skills** (Quick Shot, Dual Wield) | Tier gate |
| **24" range** | Heavy Ranged at Specialist rank |

That is a **legitimate and arguably better choice** for a game this size — rank gating needs no extra bookkeeping and reads off the model. **The recommendation is to keep it and state it as an explicit design principle, not to add a second battle currency on top of it.** See [[List Building]]. Note this is separate from the locked one-economy tenet: **Credits are the only currency the player ever sees**, and that isn't up for renegotiation.

---
## Profiles that pay you

**Type:** List · **Take:** ⭐ steal

Some profiles **grant** SWC rather than costing it **[FACT]**:

> *"Troopers whose SWC value has the + symbol will provide the player that many extra SWC points… it will not cost the player any SWC to field these Troopers."*

Typically gated behind fielding that model as **Lieutenant**. And Lieutenant options are priced **in SWC, not points**: a Ghulam HMG is SWC 1; the Ghulam *Lieutenant* HMG is SWC 0.5. **Joan of Arc as Lieutenant is +1 SWC — she pays you.**

**Why it works.** Corvus Belli uses the second currency as the dial for the **leader tax** rather than touching points at all. A negative price in a *scarce* currency is a strong incentive that costs the main budget nothing, and it steers list-building toward thematic leaders without a single restriction.

**For Settlements.** The transferable half is the shape: **a cost expressed in the constrained resource, not the abundant one, is a much sharper lever.** Our constrained resource is rank slots in the pyramid — so a "this Leader choice buys you back a Fighter slot"-style incentive is the analogue worth exploring in [[List Building]] and [[Factions]].

---
## What isn't published

**[NOT FOUND]** No formula, no spreadsheet, no credible community reverse-engineering of Infinity costs. Designer Gutier Lusquiños' published reasoning is qualitative and in-fiction: *"The Red Fury is designed as a light machine gun which is why it costs less SWC. It's more of an anti-personnel weapon than the Spitfire."* Costs are hand-set per profile row and iterated on playtesting.

**Verdict** **[CONSENSUS]**: four editions essentially unchanged. N4 rebalanced individual values; N5 kept the mechanic verbatim and extended it. The one recurring complaint is that **SWC value is table-dependent** — long-ranged support weapons are worth less on dense terrain. That is our own measured result too: `Crew Sim — Findings` put a **66-point swing** on terrain density alone. See [[Terrain]].

---
## Source

- Primary: official Infinity N5.2 wiki; N3 rulebook PDF for the cost figures
- Long-form: `docs/POINTS-RESEARCH.md` §7.2, §2
- Related: [[Wargaming Research]] · [[Gaslands]] · [[Kill Team]] · [[List Building]]
