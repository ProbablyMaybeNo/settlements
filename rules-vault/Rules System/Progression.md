---
type: rule-phase
phase: "21"
stage: S4 Settlement & Campaign
status: Drafted
build_order: 19
depends_on: ["Campaign"]
feeds_into: []
tags: [settlements/phase, settlements/stage/s4]
---
# 21 · Progression
> **S4 Settlement & Campaign** · status **Drafted** · build order **19**

**Depends on:** [[Campaign]]
**Feeds into:** —
**Raw dependency (from Notion):** Campaign

## Focus
How crews grow over a campaign — XP, leveling, injuries, veterans.

The Rules column should nail down:
- XP sources and how units earn and spend it.
- Advancement tables: new skills, stat increases, unlocked equipment.
- The injury / permanent-scar system: debilitating injuries, death, and survivors becoming powerful veterans.
- How leader/elite progression differs from non-elite.
- Grudges, bonds, and character traits that build the narrative attachment the vision promises.

## Working rules / decisions

> [!info] Superseded — [[Full Rules System v1]] is the ruling
> **§26.1 is canonical.** The freeform Advance spend is dead. Note the 2026-08-07
> revision: **Primary is derived and never changes, and there is no declared
> Secondary** — levels 1/4/8 float to *any* stat, chosen when earned — while a
> **skill slot's tier is gated by the stat**, +2/+4/+6 unlocking T1/T2/T3.

### Levels — the fixed advancement track
*Replaces the freeform Advance spend, 2026-08-05 ([[Full Rules System v1]] §26.1). Revised 2026-08-07: the track's stat levels float and skill tiers ride the stat.*

Surviving units earn a **Level** after a battle — from kills, [[Full Rules System v1|Glorious Deeds]], surviving, and objectives held. One qualifying trigger = one Level, with a soft cap of **6 distinct sources per fighter per battle**.

**Primary is derived, not declared** — it is the stat carrying the fighter's highest investment at creation (player's choice on ties). It never changes, and it names their Primary skill path. **There is no declared Secondary.** Every other stat is a secondary stat.

| Level | Grants | Credits |
|:--:|---|:--:|
| **1** | +1 **any stat** (floating) | *ladder* |
| **2** | +1 **Primary** stat | *ladder* |
| **3** | **Skill slot** | **10** |
| **4** | +1 **any stat** (floating) | *ladder* |
| **5** | +1 **Primary** stat | *ladder* |
| **6** | **Skill slot** | **20** |
| **7** | **+1 WND** | **20** |
| **8** | +1 **any stat** (floating) | *ladder* |
| **9** | +1 **Primary** stat | *ladder* |
| **10** | **Skill slot** — the capstone | **30** |

^tbl-level-track

At the **floating** levels (1, 4, 8) add +1 to **any** stat, chosen when the level is earned — a fighter's direction emerges from play, not from a box ticked at hire. Levels 2, 5 and 9 are forced **+1 Primary**, so identity keeps growing regardless of direction. Only the campaign stat cap (+6) limits track growth; **rank tier caps are creation-time caps and do not constrain levelling.**

**Skill slots (3, 6, 10):** declare **any path**, and roll on any tier that path's stat has **unlocked** — +2 → T1, +4 → T2, +6 → T3. The Level no longer fixes the tier; **the stat does.** A fighter's Primary path always counts as unlocked at T1, so a slot is never dead. Roll **three times** on that tier's chart (reroll duplicates), then **choose one of the three.** Cross-path picks are legal and cost you your own path's capstone — a genuine trade.

**A stat level is priced off the measured ladder, not a flat rate:**

| Rung | One-sided *(DEX, INT, NRV)* | Opposed *(STR, AGI)* |
|:--:|:--:|:--:|
| 0→1 | **20** | 15 |
| 1→2 | **15** | 15 |
| 2→3 | **15** | 15 |
| 3→4 | **10** | 15 |
| 4→5 | **10** | 15 |
| 5→6 | **5** | 15 |

^levels-the-fixed-advancement-track

A fully-levelled fighter carries roughly **+140 Credits** over their rank body (it depends which stats they grew), **6 lifetime stat points**, **4 skills** (1 starting + 3 levelled) and **one wound**. **A fighter caps at Level 10** — further kills and Deeds still bank Resources, but no longer advance them. Reaching Level 10 should be rare.

### Caps (anti-snowball)
- Campaign cap is **+6** (Tier 3). Start caps (+2 / +4) lift as a unit levels — most plateau around +4–5, a rare few reach +6.
- **MOV never rises from Levels** — only from **Fleet** (T2 AGI, see [[Skill Paths]]). **WND** rises exactly once, at Level 7.
- Growth makes a unit *better*, not higher-*ranked*.
- **Scar-healing is not on the track.** It lives in the **Med-bay's T2 structure tier**, and in the **once-per-career Special Treatment** option on a third Scar ([[Campaign#The third Scar — forced retirement]]). *(Worker benefits have no tiers — the Proficiency track was cut 2026-08-05 — so the T2 that heals scars is the **structure's**, per [[Full Rules System v1]] §21 and [[Structures#Recover — people come back]].)*

> [!warning] One price on this track is derived, and one stat is unmeasured entirely
> **+1 WND is 20 Credits**, derived from the measured value of **heavy armour** (−2 on the injury roll, the same 20 Cr) — both buy the same thing, the model staying on the table longer. It was 45 by pure judgement. Still **C-tier** — an analogy is not a measurement, but unlike the 45 it is correctable from table data, because the derivation is written down.
>
> **The flat 15-per-stat-point is gone**; the ladder above is measured. *(The old "16–34 Credits" underprice figure quoted here was **contaminated** — measured before the 2026-08-13 policy fix and averaged across scenarios since dropped. It is retired, not carried forward.)*
>
> **The real residual: AGI has never been measured at all.** The engine reads it only inside the Dodge reaction and `DODGE_ON` is False, so it measures exactly **zero by construction**. It currently rides the opposed ladder at ×0.8 by analogy. One of five stats is unpriced. Full derivation in `docs/POINTS-CATALOGUE.md`.
>
> A fighter who takes **Tough** (T3 STR) at Level 6 or 10 stacks it with the Level 7 wound for **WND 3** at the ceiling. That was walked through deliberately and accepted — recorded here so the stack is visible in the rules, not just in the conversation that produced it.

### Promotion
- **Rank never rises automatically.** You may **promote** a veteran into an **open** rank slot between battles (e.g. a fallen Leader's seat), gaining that rank's Orders + skill slot.
- Multiple veterans can be *leader-calibre* — a deep bench for a brutal game — but [[List Building]] caps decide how many hold rank at once. A promoted Leader still **fights**.

## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
