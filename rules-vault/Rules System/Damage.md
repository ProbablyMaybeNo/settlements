---
type: rule-phase
phase: "15"
stage: S2 Core Combat
status: Drafted
build_order: 9
depends_on: ["Shooting", "Melee"]
feeds_into: ["Conditions", "Morale", "Scenarios"]
tags: [settlements/phase, settlements/stage/s2]
---

> [!warning] Legacy reference — not the active Second Draft
> This note retains Draft 1 or prior discussion material. Use [[Rules System/Second Draft/Full Rules System v2|Second Draft master]] and [[Rules System/Second Draft/Draft 2 - Progress and Decisions|Progress and Decisions]]. Its content does not fill blank Draft 2 sections.

# 15 · Damage
> **S2 Core Combat** · status **Drafted** · build order **9**

**Depends on:** [[Shooting]], [[Melee]]
**Feeds into:** [[Conditions]], [[Morale]], [[Scenarios]]
**Raw dependency (from Notion):** Shooting, Melee

## Current damage rules — 2026-09-26

After a successful ranged hit or an **uncancelled melee hit**, roll one Injury die using that hit's weapon:

**1d20 + Weapon Damage − Armour + applicable modifiers vs 15+.** Natural 1 fails; natural 20 succeeds.

- Each success removes **1 Wound**.
- Each failure adds **1 Stress**.
- A hit target with Wounds remaining becomes **Pinned**. Applying Pinned adds no further Stress by itself.
- At **0 Wounds**, the target becomes **Downed**, including in melee.

Resolve the pool together. There is **no one-wound-per-attack cap**: three successful Injury dice remove three Wounds. A three-Wound target is Downed; a four-Wound target retains one Wound and becomes Pinned. Surplus successes do not convert to Stress or automatically finish a Downed target during the same pool. Explicit special attacks that replace normal injury resolution retain their printed effects.

Damage and Armour come from the equipment profiles in [[Basic Weapon System]] and the armour catalogue; Armour affects injury, not accuracy. Wounds normally start at 1; explicit skills and campaign advancement may increase them under the existing Wound ceiling.

### Down and treatment
A Downed unit remains on the board rather than being removed automatically by a melee wound. It retains its Stress and takes no Break tests while Downed. A separate melee attack against an already-Downed target auto-hits; a successful Injury roll finishes it. Ranged attacks against Downed targets resolve normally. These are separate attacks, not surplus dice from the attack that Downed it.

Retain the existing stabilization deadline: by the end of the unit's next activation or it bleeds out. Stabilize costs an Action and an INT test against **15+**, with the existing −2 without a Med-Kit; the Stabilize skill applies its printed +4 and Stress recovery. Detailed recovery state and the revised Pinned restrictions remain in [[Skill Integration Decisions]]; this melee revision does not invent them.

## Rule ledger
- [[core-007 Casualties]]
