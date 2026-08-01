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

# +1 Armour measured at 1.0089x damage (1D) and 0.9756x (2.5D) — both engines
# agree armour is worth about the same as damage per point. The ABSOLUTE level is
# still unresolved: the primitive method implies ~15/point, while the body-trade
# method (paying for armour by dropping models) breaks even nearer 60/point. That
# gap is the body-vs-damage scale problem, not an armour problem — the weapon
# CLASS costs are still legacy and unmeasured, so any cross-comparison between a
# measured characteristic and an inherited class price gives a nonsense ratio.
# ARMOUR_GOODS holds the 60 level pending measurement of the classes.

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
    "thrown": 40,
    "sidearm": 40,
    "standard_ranged": 100,
    "heavy_ranged": 160,
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

# ---------------------------------------------------------------------------
# PAYLOADS & CHARACTERISTICS                         [measured 2026-08-01, M4]
#
# Source: test-bench/balance/conditions2d.py, 1200 games/cell, sides swapped,
# on the 2.5D engine with the condition layer implemented (engine2d/engine.py;
# behaviour verified by engine2d/test_conditions.py, 21/21).
#
# METHOD. Two passes were run and they disagree, so read the second:
#   (a) ASYMMETRIC — buffed list vs a fixed opponent, as balance/primitives2d.py
#       does it. DISCARDED as the primary: the Hold baselines sit at 8% (Gunline)
#       and 92% (Squad), so a buff has almost no room to move the number and every
#       delta is compressed toward zero.
#   (b) MIRROR — identical crews, one side buffed. Baseline is exactly 50% by
#       symmetry: maximum sensitivity, no clipping, and deployment/activation
#       asymmetries cancel exactly. THIS is the number used below.
# Every low-value trait rose between (a) and (b), which is the signature of the
# clipping the mirror pass was built to remove.
#
#   characteristic     mirror   asym   was   ratio to +1 Damage
#   +1 Damage             15      15    15   1.000x  (anchor)
#   Blast                 43      46    40   2.893x
#   Bleeding              46      54    40   3.050x
#   Incendiary            22      24    30   1.484x
#   Suppressive           17       5    40   1.107x
#   Heavy Impact          15      22    30   0.988x
#   Shocking              13       1    30   0.838x
#   Armour Piercing        9       1    15   0.594x  (conditional — see below)
#   Toxic                  9       2    30   0.583x
#   Blinding               7      -1    30   0.433x
#   Concussive             1      -4    30   0.036x  <-- measures nothing
#   Crippling             -2      -0    30  -0.120x  <-- measures nothing
# ---------------------------------------------------------------------------
CHAR_GOODS = {
    "brutal": GOODS_INJURY,  # [measured] 15 — the anchor, unchanged
    # AP is worth EXACTLY +1 Damage against an armoured target and EXACTLY ZERO
    # against a bare one — confirmed in test_conditions.py. In the armoured mirror
    # it measured 1.21/1.50 per model against +1 Damage's own 1.21/1.50: identical.
    # So its true form is 15 x f(target wears armour). 9 is the blend measured over
    # two bare lists and one armoured one. In an armoured meta it is worth 15.
    "armour_piercing": 9,  # [measured, conditional on armour prevalence]
    "accurate": GOODS_TO_HIT_CONDITIONAL,  # [measured, provisional f] 18 — was 30
    "spread": GOODS_TO_HIT_CONDITIONAL,  # [measured, provisional f] 18 — was 30
    "rate_of_fire_2": 50,  # [measured] balance/rof_cost.py — see note below
    # --- payloads, each measured on its own. The old flat 30 was a grouping, and
    # the spread below is 46:1. Bleed and Blind cannot share a price.
    "bleeding": 46,  # [measured] the death clock at WND 1 — the deadliest payload
    "incendiary": 22,  # [measured]
    "shocking": 16,  # [measured, re-measured after the duration change: 13 -> 16]
    "toxic": 9,  # [measured] -1 all rolls until a STR test clears it
    "blinding": 4,  # [measured] -2 on sight rolls only — small either way, see below
    "heavy_impact": 15,  # [measured] push 2"
    "suppressive": 17,  # [measured] the Pin costs the whole activation — was 40
    "blast": 43,  # [measured] resolve against everything within 2"
    # CONCUSSIVE (Off-Balance) and CRIPPLING (Hobbled) MEASURE AT ZERO — 1 and -2
    # Goods, i.e. inside the noise floor. They are DELIBERATELY LEFT AT 30 and
    # flagged, not repriced to nothing: selling a player a trait that does nothing
    # is worse than selling it at the wrong price. This is a DESIGN defect to fix
    # in the rules (the effects are too small, or expire too fast to matter), not
    # a price to set. See POINTS-TABLE.md §5.5.
    "concussive": 30,  # !! measures -1 AFTER being strengthened — see the note below
    "crippling": 30,  # !! measures  1 AFTER being strengthened — see the note below
    # --- not yet measured; still legacy x10, not derived from anything
    "hook": 20,
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

# ---------------------------------------------------------------------------
# THE DURATION EXPERIMENT — run 2026-08-01, and it mostly FAILED. Recorded so it
# is not repeated.
#
# All four low-measuring conditions had their rules strengthened in the vault and
# the measurement was repeated on the same harness:
#   Blind / Shocked : End Phase clear  ->  ends at the end of its NEXT activation
#   Off-Balance     : one activation   ->  persists until cleared with the Move
#   Hobbled         : one activation   ->  persists until cleared with the Move
#
#   trait         before   after
#   Shocking        13      16     helped
#   Blinding         7       4     no better (both inside noise, ~+/-2)
#   Concussive       1      -1     still zero
#   Crippling       -2       1     still zero
#
# Note how strong the Hobbled test actually was: nothing in the sim ever spends a
# Move to clear it, so the measurement is of a PERMANENT -2" MOV for the rest of
# the game — and it is still worth nothing. Movement debuffs do not pay on a 36"
# board over 6 rounds. Two caveats keep this a lower bound: the AI does not kite
# or focus slowed targets, and it never chooses to shed the condition.
#
# THE DEEPER CAUSE, which applies to every payload. A payload only lands on a hit
# that FAILS to wound. A rifle (+3) into no armour wounds ~70% of the time, so
# only ~30% of hits deliver their payload at all. Payload value therefore rises
# with target armour — visible in the Armoured column of conditions2d.py, where
# almost every payload measures higher. Pricing a payload against bare targets
# understates it in an armoured meta and overstates it in a naked one.
#
# The duration changes were KEPT regardless of the numbers: the activation clock
# removes an invisible coin-flip (a payload used to do nothing at all if the
# target had already activated), which is a readability win the player can see.
# ---------------------------------------------------------------------------

# Characteristics whose measurement came back inside the noise floor EVEN AFTER
# their rules were strengthened. The remaining options are to strengthen much
# harder or to cut them; they are deliberately not repriced to ~0, because a
# near-free trait in a player-built weapon system gets taken on everything.
# Reported by points.verify.
UNPRICEABLE_MEASURED_ZERO = ("concussive", "crippling")

# Rate of Fire 2 = 50  [measured 2026-07-30, balance/rof_cost.py reproduced]
# Method: grant RoF 2 to both rifles in the 100-pt Cadre, then rebuild the list to
# pay for it. Dropping a 12-pt model returned the crew to baseline: -3 / -2 / -6
# vs Pyramid / Horde / Standard at medium. 12 at the 100-scale, slightly under,
# so ~50 at the 1000-scale.
#
# RATE OF FIRE 3 IS UNPRICED. Do not infer it from RoF 2 — the third die is
# superlinear (hit chance 84%->94%, but extra Stress 0.36->0.86 per attack).
# Run the same rebuild test before it ships. There is deliberately no entry.

# ---------------------------------------------------------------------------
# RANGE BANDS — range is priced by which threshold a weapon clears, never per
# inch. Two thresholds structure the ladder. Neither is itself a priced feature;
# both are costing PRECONDITIONS that make the band values mean anything.
#
#   12"  the turn-one firing threshold. Deployment zones sit 24" apart and MOV
#        is 6". A rifle at 18" closes 6" and fires on turn one (24 - 6 = 18).
#        A pistol at 8" must cross 16" and cannot. 12" is where that flips.
#   24"  the deployment distance itself — fire on turn one without moving.
#        Nothing is priced above it; 24" is a hard ceiling (POINTS-TABLE §11).
#
# Value accelerates toward the ceiling. This is why a linear per-inch rate is
# wrong: the same 6" is worth far more at the top of the ladder than the bottom.
# ---------------------------------------------------------------------------
RANGE_BAND = {
    "melee": 0,
    "thrown": 6,  # below both thresholds
    "close": 8,  # below both thresholds
    "effective": 18,  # clears the 12" turn-one threshold
    "deployment": 24,  # the 24" ceiling
}

CLASS_RANGE_BAND = {
    "unarmed": "melee",
    "light_melee": "melee",
    "one_handed_melee": "melee",
    "heavy_melee": "melee",
    "thrown": "thrown",
    "sidearm": "close",
    "standard_ranged": "effective",
    "heavy_ranged": "deployment",
}

# Priced steps between adjacent bands.
RANGE_STEP_GOODS = {
    # [derived twice, independently, from this file]
    #   (a) CHAR_GOODS["long_range"] == 60
    #   (b) CLASS_GOODS["heavy_ranged"] 160
    #       == CLASS_GOODS["standard_ranged"] 100 + long_range 60
    # Cumbersome is no longer welded onto Heavy Ranged (decision 2026-07-30), so
    # the -20 refund is gone and the class costs the clean 160. Its real cost is
    # the SLOT count: 4 against Standard Ranged's 3 — opportunity, not penalty.
    # Cumbersome remains available as an OPT-IN drawback in DRAWBACK_GOODS.
    # verify.verify_structural() checks (b) still holds.
    ("effective", "deployment"): 60,
}

# The lower steps are UNPRICED, not zero and not estimated. They cannot be read
# off the class table without also splitting out Damage and Hands from the same
# figure. Worked example of why:
#   sidearm 40 (Damage +2, 8") -> standard_ranged 100 (Damage +3, 18") = a gap
#   of 60, containing one Damage step and one range step. With the M1 measured
#   Damage atom of 15 that leaves 45 for range-plus-Hands. The completion plan's
#   "8\" -> 18\" is worth ~20" was computed when Damage cost 40; M1 invalidates
#   that arithmetic. Do not carry the 20 forward.
RANGE_STEP_UNPRICED = (
    ("melee", "thrown"),
    ("thrown", "close"),
    ("close", "effective"),
)

# Short Range halves a weapon's range, so its refund must scale with what is
# actually lost — a flat -30 handed back a 24"->12" collapse for the same money
# as an 18"->9" one. Banded by class:
SHORT_RANGE_REFUND = {
    "thrown": -20,  # 6" -> 3"; was below both thresholds already
    "sidearm": -20,  # 8" -> 4"; was below both thresholds already
    "standard_ranged": -30,  # 18" -> 9"; loses the turn-one threshold
    "heavy_ranged": -70,  # 24" -> 12"; loses the deployment threshold entirely
}

# Drawbacks — legacy ×10 (negative = refund).
# short_range is NOT here: it is banded by class, see SHORT_RANGE_REFUND.
DRAWBACK_GOODS = {
    "slow": -30,
    "unstable": -20,
    "cumbersome": -20,
    "single_use": -20,  # renamed from "limited" 2026-07-31
}

BANDED_DRAWBACKS = frozenset({"short_range"})

# Armour carries NO penalties (decision 2026-07-30). A drawback you opt into for
# a discount is a deal; a drawback welded to something you want is a tax. The old
# table taxed armour twice — Improvised -1 AGI, Heavy -1 MOV / -1 AGI / Loud — and
# neither sim modelled AGI meaningfully (1D never reads it; 2.5D uses it only for
# the Dodge reaction), so every armour measurement priced those penalties at zero.
#
# The ladder is now linear in what it actually does. The injury roll is
# 1d10 + Damage - Armour vs 7+, so each armour point is a flat -10% on the injury
# probability: -2 is worth exactly twice -1, and Heavy must cost twice Light.
#
# Improvised was CUT (2026-07-30). Once its -1 AGI penalty was removed it had an
# identical profile to Light at an identical price — a redundant catalogue row.
# Crafted-vs-bought is a settlement-layer distinction, not a second armour type.
#
# LEVEL [measured]: balance/armourprice.py swept the price with every crew rebuilt
# to 100 pts. The three melee builds cluster tightest between 20 and 30 per point;
# at 60 they fan out (bare 73% / light 51% / heavy 42%). Parity sits near 25.
# 30 is taken as the integral value inside that bracket.
ARMOUR_GOODS = {
    "none": 0,
    "thick_clothing": 0,
    "light": 30,   # -1  [measured 2026-07-30, balance/armourprice.py]
    "heavy": 60,   # -2  exactly 2x, no refunds
}

ARMOUR_INJURY = {
    "none": 0,
    "thick_clothing": 0,
    "light": -1,
    "heavy": -2,
}

HACK_GEAR_GOODS = {
    "bare": 0,
    "breach_kit": 40,
    "exploit_suite": 80,
}

EQUIPMENT_GOODS = {
    "med_kit": 40,
}
