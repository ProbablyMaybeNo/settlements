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

### Levels — the fixed advancement track
*Replaces the freeform Advance spend, 2026-08-05 ([[Full Rules System v1]] §26.1). A player no longer chooses **what** an advance buys — only which stat carries it and which skill they take.*

Surviving units earn a **Level** after a battle — from kills, [[Full Rules System v1|Glorious Deeds]], surviving, and objectives held. One qualifying trigger = one Level, with a soft cap of **6 distinct sources per fighter per battle**.

**At creation, declare a Primary and a Secondary stat.** Primary is whichever stat carries the fighter's highest investment (player's choice if tied); Secondary is the next-highest. Both — and the skill path tied to the Primary — are **fixed for that fighter's whole career**.

| Level | Grants | Credits |
|:--:|---|:--:|
| **1** | +1 **Secondary** stat | 15 |
| **2** | +1 **Primary** stat | 15 |
| **3** | **Tier 1 skill** (Primary path) | 20 |
| **4** | +1 **Secondary** stat | 15 |
| **5** | +1 **Primary** stat | 15 |
| **6** | **Tier 2 skill** (Primary path) | 35 |
| **7** | **+1 WND** | 45 |
| **8** | +1 **Secondary** stat | 15 |
| **9** | +1 **Primary** stat | 15 |
| **10** | **Tier 3 skill** (Primary path) — the capstone | 55 |

^tbl-level-track

**Choosing the skill at Levels 3, 6 and 10:** roll **three times** on that tier's chart within the fighter's Primary path (reroll duplicates), then **choose one of the three**.

A fully-levelled fighter carries **+245 Credits** over their rank body, **6 lifetime stat points** (3 Primary + 3 Secondary), **4 skills** (1 starting + 3 levelled, all one path) and **one wound**. **A fighter caps at Level 10** — further kills and Deeds still bank Resources, but no longer advance them. Reaching Level 10 should be rare.

### Caps (anti-snowball)
- Campaign cap is **+6** (Tier 3). Start caps (+2 / +4) lift as a unit levels — most plateau around +4–5, a rare few reach +6.
- **MOV never rises from Levels** — only from **Fleet** (T2 AGI, see [[Skill Paths]]). **WND** rises exactly once, at Level 7.
- Growth makes a unit *better*, not higher-*ranked*.
- **Scar-healing is not on the track.** It lives in the **Med-bay's T2 structure tier**, and in the **once-per-career Special Treatment** option on a third Scar ([[Campaign#The third Scar — forced retirement]]). *([[Full Rules System v1]] §26.1 still words this as the Med-bay's "T2 **worker** benefit" — a leftover from the Proficiency track cut on 2026-08-05. Worker benefits have no tiers any more; the T2 that heals scars is the structure's, per §21 and [[Structures#Recover — people come back]].)*

> [!warning] Two prices on this track are unmeasured
> **+1 WND at 45 Credits has no sim data behind it at all** — it is priced above a T2 skill and below a T3 by judgement. And the flat **15 per stat point** is a known underprice: measurement puts a stat point at **16–34 Credits**, worst for STR/melee builds. Both are flagged in [[Full Rules System v1]] §26.1.
>
> A fighter who takes **Tough** (T3 STR) at Level 6 or 10 stacks it with the Level 7 wound for **WND 3** at the ceiling. That was walked through deliberately and accepted — recorded here so the stack is visible in the rules, not just in the conversation that produced it.

### Promotion
- **Rank never rises automatically.** You may **promote** a veteran into an **open** rank slot between battles (e.g. a fallen Leader's seat), gaining that rank's Orders + skill slot.
- Multiple veterans can be *leader-calibre* — a deep bench for a brutal game — but [[List Building]] caps decide how many hold rank at once. A promoted Leader still **fights**.

## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
