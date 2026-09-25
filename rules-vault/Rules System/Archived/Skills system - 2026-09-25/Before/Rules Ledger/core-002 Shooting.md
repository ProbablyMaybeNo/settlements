---
type: rule
rule_id: core-002
category: core
status: draft
version: v0.3
parent_phase: "[[Shooting]]"
tags: [settlements/rule, settlements/cat/core]
---
# core-002 · Shooting
> **core** · status **draft** · v0.3

**Parent phase:** [[Shooting]]

## Text
1. Declare a target in **range**, **true LOS**, and **forward 180°** facing.
2. **Attack roll:** `1d10 + DEX + mods` vs **7+**.
3. On a hit → **Injury roll** ([[core-007 Casualties]] / [[Damage]]): a wound costs a **WND**; a **non-wounding** hit instead **Pins** the target (**+1 Stress**, [[Morale]]).
4. A clean **miss** does nothing — every hit does exactly one thing (wound *or* Pin), never both.

**Attack Dice** ([[Full Rules System v1]] §15, ruled 2026-08-29). A weapon's **Attack Dice** value is **1** unless its card says otherwise. Attack Dice 2 or 3 fires that many shots for **one Action**: roll every die's attack-and-Injury chain at once, then apply **one** Injury result of the attacker's choice. **A burst inflicts at most 1 WND however many dice pass** — wounds never stack. **Every other die that hit becomes +1 Stress**, whether it passed the Injury roll or failed it, and that Stress lands even on a model the Action put Down. The one-thing-per-hit contract in step 4 runs **per die**, not per Action. Cost **+40** for die 2, **+25** for die 3 (65 cumulative). *Gates (rank, one-AD-3-per-crew, manufactured-only) are **proposed, not law** — §29.*

**Modifiers:** Cover Light −1 · Heavy −2 · Hidden −3. Outside arc / no LOS / out of range = illegal. Weapons rarely add to hit ([[Weapons]]).

**Target may react:** a **Ready** target may **Dodge** — opposed `1d10 + AGI` vs the shooter's `1d10 + DEX` *replaces* this to-hit (win = miss + dive out of LOS, then Pinned); see [[core-005 Activation order]].

**Engaged:** most ranged cannot fire. **Sidearm** may fire at the Engaged enemy only (still needs facing).

**Facing** does not affect melee.

*Graduated from [[Shooting]]. See [[Rules System MOC]].*
