"""Atomic tick table — 1000 Goods scale. Players never see these atoms."""

from __future__ import annotations

SCALE = 1000
TICK = 10  # Goods per generic unconditional +1 test tick (legacy abstraction)

# ---------------------------------------------------------------------------
# MEASURED PRIMITIVE ATOMS                                   [measured 2026-07-30]
#
# Source: test-bench/balance/realistic.py, re-run and reproduced 2026-07-30.
# Method: a free +1 given to one side; win-rate delta divided by models buffed;
# averaged over the realistic all-armed lists (Gunline 4 / Fireteam 6 / Squad 8)
# at medium and dense terrain density.
#
#   primitive     medium    dense     mean    relative to +1 Damage
#   +1 to-hit     +1.4367   +1.8667   1.6517  1.4769x
#   +1 Damage     +1.1733   +1.0633   1.1183  1.0000x   <- the anchor
#   +1 Armour     +0.9833   +1.2733   1.1283  1.0089x
#   +1 Stress     +0.5700   +0.4400   0.5050  0.4516x
#
# Anchoring +1 Damage = 15 Goods gives 22.15 / 15.00 / 15.13 / 6.77.
#
# CAVEAT ON PROVENANCE: realistic.py runs on crew_sim.py, which documents itself
# as a 1D board, and it does not swap sides. The 2.5D engine (engine2d/) has not
# reproduced these exchange rates. M2 of the completion plan records that a 1D
# armour result was later shown to be an artefact, so the 1D provenance of these
# four numbers is a live risk, not a settled fact.
# ---------------------------------------------------------------------------
GOODS_DAMAGE = 15  # [measured] the anchor: +1 on the Injury roll
GOODS_TO_HIT = 22  # [measured] unconditional +1 on the hit roll (1.4769x damage)
GOODS_STRESS = 7  # [measured] +1 Stress inflicted on a hit (0.4516x damage)

# Provisional conditional ladder: L = (1 - f)/f, net multiplier = f.
# f = 0.8 ("most activations") is a judgement band, NOT measured. Measuring f per
# trait is Milestone 4's job; until then every conditional to-hit trait sits here.
CONDITIONAL_F_PROVISIONAL = 0.8
GOODS_TO_HIT_CONDITIONAL = 18  # round(22 * 0.8) = 17.6 -> 18  [provisional]

# +1 Armour measured at 1.0089x damage = 15.13 Goods per point. NOT wired into
# ARMOUR_GOODS below, which still carries the legacy 60/100. Resolving that 4x
# gap is Milestone 2 and is a decision gate — do not close it here.

# Injury-side atom (Brutal / AP). Legacy was 4 ticks x 10 = 40; measurement
# replaces it. The tick abstraction no longer divides evenly, which is expected:
# measurement supersedes the hand-set ladder.
GOODS_INJURY = GOODS_DAMAGE  # [measured] 15

# Per path-stat point inside a rank bundle (not sold à la carte to players).
TICK_STAT = 15  # Goods directly (not × TICK) — kept as Goods for clarity
BODY_BASE = 20
ORDER_PREMIUM = {0: 0, 1: 40, 2: 90}

# Skill unlock premiums when an Advance crosses a tier
SKILL_TIER_GOODS = {1: 20, 2: 35, 3: 55}

# Structure Materials derivation
POWER_MAT = 15
FOOTPRINT_BAND = {
    "station": 25,
    "plant": 40,
    "building": 75,
    "large": 100,
    "line": 25,
    "yard": 40,
}
ROLE_BAND = {
    "sustain": 0,
    "gatherer": 25,
    "convert": 35,
    "operate": 40,
    "recover": 30,
    "defend": 45,
}
UPGRADE_MULT = {2: 1.60, 3: 1.75}
GROUNDWORKS_MAT = {1: 120, 2: 200}

# Weapon classes — legacy ×10
CLASS_GOODS = {
    "unarmed": 0,
    "light_melee": 0,
    "one_handed_melee": 40,
    "heavy_melee": 80,
    "thrown": 20,
    "sidearm": 40,
    "standard_ranged": 100,
    "heavy_ranged": 140,
}

CLASS_META = {
    "unarmed": {"damage": 0, "range": 0, "slots": 0, "min_rank": "recruit"},
    "light_melee": {"damage": 1, "range": 0, "slots": 2, "min_rank": "recruit"},
    "one_handed_melee": {"damage": 2, "range": 0, "slots": 2, "min_rank": "fighter"},
    "heavy_melee": {"damage": 3, "range": 0, "slots": 3, "min_rank": "specialist"},
    "thrown": {"damage": 1, "range": 6, "slots": 2, "min_rank": "recruit"},
    "sidearm": {"damage": 2, "range": 8, "slots": 2, "min_rank": "recruit"},
    "standard_ranged": {"damage": 3, "range": 18, "slots": 3, "min_rank": "fighter"},
    "heavy_ranged": {"damage": 3, "range": 24, "slots": 4, "min_rank": "specialist"},
}

# Characteristics. Rows marked [measured] come from the atoms above; the rest are
# still legacy ×10 and are not derived from anything.
CHAR_GOODS = {
    "brutal": GOODS_INJURY,  # [measured] 15 — was 40
    "armour_piercing": GOODS_INJURY,  # [measured] 15 — was 40 (armour 1.0089x = damage)
    "accurate": GOODS_TO_HIT_CONDITIONAL,  # [measured, provisional f] 18 — was 30
    "spread": GOODS_TO_HIT_CONDITIONAL,  # [measured, provisional f] 18 — was 30
    "rate_of_fire_2": 50,  # [measured] balance/rof_cost.py — see note below
    "concussive": 30,
    "crippling": 30,
    "blinding": 30,
    "shocking": 30,
    "toxic": 30,
    "incendiary": 30,
    "bleeding": 40,
    "heavy_impact": 30,
    "hook": 20,
    "suppressive": 40,
    "blast": 40,
    "smoke": 30,
    "long_range": 60,
    "balanced": 20,
    "defensive": 30,
    "cleaving": 50,
    "breaching": 30,
    "concealable": 20,
    "quiet": 20,
    "compact": 20,
}

# Rate of Fire 2 = 50  [measured 2026-07-30, balance/rof_cost.py reproduced]
# Method: grant RoF 2 to both rifles in the 100-pt Cadre, then rebuild the list to
# pay for it. Dropping a 12-pt model returned the crew to baseline: -3 / -2 / -6
# vs Pyramid / Horde / Standard at medium. 12 at the 100-scale, slightly under,
# so ~50 at the 1000-scale.
#
# RATE OF FIRE 3 IS UNPRICED. Do not infer it from RoF 2 — the third die is
# superlinear (hit chance 84%->94%, but extra Stress 0.36->0.86 per attack).
# Run the same rebuild test before it ships. There is deliberately no entry.

# Drawbacks — legacy ×10 (negative = refund)
DRAWBACK_GOODS = {
    "short_range": -30,
    "slow": -30,
    "unstable": -20,
    "cumbersome": -20,
    "limited": -30,
}

ARMOUR_GOODS = {
    "none": 0,
    "thick_clothing": 0,
    "improvised": 30,
    "light": 60,
    "heavy": 100,
}

HACK_GEAR_GOODS = {
    "bare": 0,
    "breach_kit": 40,
    "exploit_suite": 80,
}

EQUIPMENT_GOODS = {
    "med_kit": 40,
}
