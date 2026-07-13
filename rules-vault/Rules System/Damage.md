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
# 15 · Damage
> **S2 Core Combat** · status **Drafted** · build order **9**

**Depends on:** [[Shooting]], [[Melee]]
**Feeds into:** [[Conditions]], [[Morale]], [[Scenarios]]
**Raw dependency (from Notion):** Shooting, Melee

## Focus
The output of every attack — wounds, injury states, and criticals.

The Rules column should nail down:
- How a hit converts to a wound: armour/save roll, AP/rend modifier, then wounds dealt.
- The wound model: most units have 1 wound (down on a successful hit); multi-wound leaders/champions.
- Down/injury states in-battle: knocked down, out of action, bleeding out.
- Criticals: what triggers one and what it does (extra damage / roll on an injury table).
- The armour profile and how it modifies the save.
- The hook into the persistent roster: post-battle survival vs death vs lasting injury (brutal-realism pillar).

## Inherits from the engine
> [!info] Recall — saves / wound rolls should reuse the [[Rules Engine#Universal Resolution Mechanic|core test]] (armour as a modifier, AP as a negative to it), and criticals hook off the **natural 10** rule. Don't introduce a new dice type here — set the lethality dial by *how a hit converts*, not by changing the roll.

## Working rules / decisions

### Two-roll combat
After an attack lands ([[Shooting]] / [[Melee]]), the **attacker** makes one **Injury roll**:

`1d10 + Weapon Damage − Armor` vs **7+**

- **Pass →** the target loses **1 WND**. Reduced to **0 WND** → **Down** if the wound was **ranged / hazard**, or straight to **Out of Action** if it was **melee** (see below).
- **Fail →** no wound, but the hit still tells:
    - **Ranged** → the target is **Pinned** (+1 Stress) — head down, can't advance.
    - **Melee** → the target gains **+1 Stress** (**Shaken**, −1 next round) but stays engaged. No Pinned — you can't pin someone you're locked toe-to-toe with.

Every hit does *something* — it wounds or it pins. No wasted hits.

### Weapon Damage & Armor
- **Damage** is a small class, not a bespoke number: **+0** unarmed · **+1** light · **+2** medium · **+3** heavy. See [[Weapons]].
- **Armor** reduces the Injury roll only, never the hit: **0** none · **−1** light · **−2** heavy. Armor carries drawbacks — see [[Weapons#Armor]].
- *Example:* pistol (**+2**) into heavy armor (**−2**) = net 0 → `1d10 vs 7+` = 40% to wound.

### Pinned
- Pinned is **suppression, not injury**, and it's the **ranged** non-wound result — the shot landed but didn't wound. (A non-wounding **melee** blow instead piles Stress → **Shaken**; you can't pin someone you're toe-to-toe with.)
- A Pinned unit **cannot Move, Charge, Sprint or Disengage**; it must spend its **Move** to shake Pinned off before it can reposition. It may still **Shoot or Interact** from where it stands.
- Pinned **persists until cleared**, and applying it is **+1 Stress** — so a unit that keeps getting Pinned climbs the [[Morale|Stress]] ladder toward **Shaken** and a **Break test**. That accumulation, not the Pin itself, is what wears down a dug-in shooter.
- Full status entry in [[Conditions]].

### Down & bleeding out
- **Melee is decisive.** A unit reduced to **0 WND by a melee attack** goes **straight to Out of Action** — removed (→ Fate). No finisher, no bleed-out clock: put someone down in a brawl and they're done.
- **Ranged / hazard leaves them Down.** A unit reduced to 0 by **ranged fire or a hazard** goes **Down** — prone and out of the fight, but still alive on the table. It counts as **Heavy cover vs ranged unless in the open**; a **melee / engaged attack auto-hits** to finish it (Injury roll still made, a **pass = Out**), but **ranged attacks resolve normally** — so a downed fighter has a chance to be reached and Stabilized instead of shot for free.
- A Down unit must be **Stabilized** by the end of its **next** activation or it **bleeds out** and is removed (→ [[Campaign#Post-battle — the Fate table|Fate roll]]).
- **Stabilize** = 1 Action + an **INT test (7+)**, by the Down unit itself or an adjacent friendly. **−2 without a Med-Kit**; a **Med-Kit** cancels the penalty; a **Medic** ([[Skill Paths]]) auto-stabilizes.

### Wounds
**Every unit has WND 1** — one injury pass drops it (**Down** from ranged, **Out** from melee). The *only* way to have more is a specific **skill** that grants +1 WND ([[Skill Paths]]); a multi-wound unit takes each pass as **−1 WND**, going Down at 0.

## Rule ledger
- [[core-007 Casualties]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
