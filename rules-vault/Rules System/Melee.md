---
type: rule-phase
phase: "14"
stage: S2 Core Combat
status: Drafted
build_order: 8
depends_on: ["Unit Design", "Movement"]
feeds_into: ["Damage"]
tags: [settlements/phase, settlements/stage/s2]
---

> [!warning] Legacy reference — not the active Second Draft
> This note retains Draft 1 or prior discussion material. Use [[Rules System/Second Draft/Full Rules System v2|Second Draft master]] and [[Rules System/Second Draft/Draft 2 - Progress and Decisions|Progress and Decisions]]. Its content does not fill blank Draft 2 sections.

# 14 · Melee
> **S2 Core Combat** · status **Drafted** · build order **8**

**Depends on:** [[Unit Design]], [[Movement]]
**Feeds into:** [[Damage]]
**Raw dependency (from Notion):** Unit Design, Movement

## Current melee rules — 2026-09-26

### Engagement
A unit is **Engaged** within **1 inch** of an enemy. Ordinary movement cannot initiate engagement: enter by **Charge**, or by a rule explicitly permitting movement into close combat, such as Blade Fury or Rampage. Already-engaged units may remain engaged and use their Core Action to Fight without charging again. Facing does not apply during melee.

### Charge
Charge costs both the **Move and Core Action**. Declare an enemy in LOS and roll **MOVE + 1d6** for maximum charge movement; Human Bullet uses **MOVE + 2d6**. Reach within **1 inch** of the declared target to succeed and resolve a **free melee exchange**. The charging unit adds **one Attack Die to its dominant weapon**; the defender gains no charge die. A failed charge grants no melee exchange.

### Melee exchange
1. Both units gather their melee Attack Dice. When dual wielding, use the dominant weapon's full dice and one off-hand die unless a skill overrides this. Retain each die's weapon identity.
2. Both roll **1d20 + melee stat + applicable modifiers vs 15+**, once per Attack Die. STR is normal; AGILE weapons permit AGI. Natural 1 fails and natural 20 succeeds. Do **not** subtract the opponent's stat.
3. Each successful hit cancels one opposing successful hit. Equal hit counts cancel completely. The side with more hits retains the difference. Each player chooses which opposing hits their successes cancel; remaining hits retain their weapon profiles.
4. Roll one Injury die for each uncancelled hit, using [[Damage]].

This is simultaneous **hit cancellation**, not paired opposed dice. Defender-wins-ties remains a rule for genuine opposed tests; it does not turn tied melee hit counts into defender hits. Cancelled hits cause neither injury, Stress nor Pinned. There is **no additional automatic attack-back** after the exchange; the defender already participated. Explicit skill counterattacks are separate exceptions.

### UNANSWERED
Resolve the same exchange, but only its initiating unit can inflict injuries. Defender hits cancel attacker hits normally; surplus defender hits cause no injury, Stress or Pinned. Do not add an automatic return attack. A Charge alone is not UNANSWERED; Ambush, Aerial Assault and other explicit effects grant it.

### Simulation choice
For automated basic tests, cancel the opponent's highest-Damage hits first. This is a simulator decision policy, **not a compulsory player rule**. Record the policy when reporting results.

## Rule ledger
- [[core-003 Melee]]
