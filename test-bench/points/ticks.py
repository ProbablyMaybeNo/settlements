"""Atomic tick table — 1000-Credit scale. Players never see these atoms.

WRITE-BACK LANDED 2026-08-13. Until today no measured price had ever reached this
file: it carried the legacy x10 scale, a 1D-board primitive table, and an armour
level citing `balance/armourprice.py` — a file that has never existed in any
commit on any branch. Every headline number below now comes from the 2.5D harness
and names the artefact it came from.

THE CONFIDENCE TIER travels with every price. No number ships untagged.

    A   measured, current, significant. Trust it for play.
    B   measured, but wide CI or single-scenario coverage only. Usable; expect
        movement as scenario coverage lands.
    C   DERIVED BY RULE from an A/B atom and never measured directly. A
        placeholder that is correctable — the first thing table data fixes.

A C price is fine. An UNTAGGED price is not, which is the defect this rebuild
existed to eliminate. Every C entry states its derivation inline; if you cannot
read how a number was reached, it is a bug in this file.

CATALOGUE-WIDE LIMITATIONS. Stated once here rather than repeated per row; the
full statement is the front matter of docs/POINTS-CATALOGUE.md.

  1. THE LIST-CONTEXT CEILING. An 18" gun measures ~39% more valuable in an
     all-melee crew than the decomposition through a gun-carrying crew predicts
     (3.060 +- 1.460 wp, significant). No flat per-item catalogue is accurate past
     that bound. This is a property of points systems, not a defect in this one.
  2. SINGLE-SCENARIO COVERAGE. Everything is priced on `hold_claim` — Take a
     Hold, 1 of 5 shipped scenarios and the most static. Expect static and
     defensive atoms (range, damage, armour) to read HIGH and mobility, tempo,
     stealth and objective-running to read LOW.
  3. POLICY RESIDUALS. The AI sprints across open ground where a slower advance
     would shoot (costs ~40-46% head-to-head in 3 of 9 cells); no model ever
     defends anything; Orders carry a standing AI-limitation caveat.
  4. THE ANCHOR IS PROVISIONAL. Five values so far, each error invisible from
     inside the one before it. Corroborated once, within the same instrument.

Sources: test-bench/balance/results/, engine e2b861d61 / harness hf20a47e3.
"""

from __future__ import annotations

SCALE = 1000
TICK = 10  # Points per generic unconditional +1 test tick (legacy abstraction)

# Confidence tiers, as data so `points.verify` can assert nothing ships untagged.
TIER_A = "A"  # measured, current, significant
TIER_B = "B"  # measured; wide CI or single-scenario only
TIER_C = "C"  # derived by rule from an A/B atom, never measured directly

# ---------------------------------------------------------------------------
# THE ANCHOR                                    [B] gear-anchor-objective-n4000
#
# +1 on the Injury roll = 0.606 win-points per model buffed, CI [0.436, 0.776].
# Pegging it at 15 Credits fixes the whole scale. THE PEG IS A CHOICE, NOT A
# MEASUREMENT — the measured part is the 0.606, and everything else in this file
# is that number in different clothes.
#
# FLAT, AND THAT IS NOW SETTLED. The density sweep (n2000, 9/11/12 features,
# nested boards) moved the anchor by +0.176 +- 0.184 — stable within noise. The
# 5.0x cell spread that once argued for a non-linear anchor turned out to be the
# hold/hold_claim gap, i.e. two different games being averaged, and priced on
# hold_claim alone the spread is 1.46x. Flat-vs-curve is CLOSED: ship flat.
# ---------------------------------------------------------------------------
ANCHOR_WP = 0.606              # win-points per model, +1 Damage
ANCHOR_CI = (0.436, 0.776)
CREDITS_PER_WINPOINT = 24.77   # = 15 / 0.606


def cr(wp: float) -> int:
    """Win-points -> Credits at the pegged scale. Every price below traces here."""
    return round(wp * CREDITS_PER_WINPOINT)

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
# Anchoring +1 Damage = 15 Credits gives 22.15 / 15.00 / 15.13 / 6.77.
#
# CAVEAT ON PROVENANCE: realistic.py runs on crew_sim.py, which documents itself
# as a 1D board, and it does not swap sides. The 2.5D engine (engine2d/) has not
# reproduced these exchange rates. M2 of the completion plan records that a 1D
# armour result was later shown to be an artefact, so the 1D provenance of these
# four numbers is a live risk, not a settled fact.
# ---------------------------------------------------------------------------
CREDITS_DAMAGE = 15  # [A] the anchor: +1 on the Injury roll. 0.606 wp, the peg.

# [B] +1 to-hit. The 1D figure was 22 and is SUPERSEDED — to-hit is a DEX rung,
# and the measured DEX ladder is not flat (37 Cr at the first rung, 10 at the
# last, a 3.6x spread). A single number for "+1 to-hit" is therefore wrong by
# construction; 22 survives only as the ladder's mid value and is kept for the
# legacy callers that still want a scalar. Price from STAT_LADDER instead.
CREDITS_TO_HIT = 22

# [C] +1 Stress inflicted on a hit. DERIVATION: no 2.5D measurement isolates
# Stress. Its nearest measured neighbour is Pinned (value-of-pinned-n4000,
# +0.510 wp = 13 Cr), which is "+1 Stress AND the pin" — so Stress alone is
# strictly less than 13. Held at the legacy 7, which sits inside that bound.
# Correct this first if Stress ever matters at the table.
CREDITS_STRESS = 7

# Provisional conditional ladder: L = (1 - f)/f, net multiplier = f.
# f = 0.8 ("most activations") is a judgement band, NOT measured. Measuring f per
# trait is Milestone 4's job; until then every conditional to-hit trait sits here.
CONDITIONAL_F_PROVISIONAL = 0.8
CREDITS_TO_HIT_CONDITIONAL = 18  # round(22 * 0.8) = 17.6 -> 18  [provisional]

# +1 Armour measured at 1.0089x damage (1D) and 0.9756x (2.5D) — both engines
# agree armour is worth about the same as damage per point. The ABSOLUTE level is
# still unresolved: the primitive method implies ~15/point, while the body-trade
# method (paying for armour by dropping models) breaks even nearer 60/point. That
# gap is the body-vs-damage scale problem, not an armour problem — the weapon
# CLASS costs are still legacy and unmeasured, so any cross-comparison between a
# measured characteristic and an inherited class price gives a nonsense ratio.
# ARMOUR_CREDITS holds the 60 level pending measurement of the classes.

# Injury-side atom (Brutal / AP). Legacy was 4 ticks x 10 = 40; measurement
# replaces it. The tick abstraction no longer divides evenly, which is expected:
# measurement supersedes the hand-set ladder.
CREDITS_INJURY = CREDITS_DAMAGE  # [measured] 15

# ---------------------------------------------------------------------------
# THE STAT LADDER                                     [B] stat-ladder-n3000
#
# THE FLAT 15 PER POINT IS WRONG IN BOTH DIRECTIONS, and this is the single
# largest correction in the write-back. Measured per rung, on hold_claim:
#
#   DEX (one-sided, vs a fixed TN 7+)   STR (opposed, vs another model's stat)
#     0->1  +1.514 wp   37 Cr             every rung  +1.011 wp   25 Cr
#     1->2  +1.044 wp   26 Cr
#     2->3  +1.108 wp   27 Cr           An opposed same-stat roll CANNOT
#     3->4  +0.739 wp   18 Cr           saturate: P(X+a > Y+b) depends only on
#     4->5  +0.619 wp   15 Cr           b-a, so every rung is identical. The
#     5->6  +0.422 wp   10 Cr           structure predicted this before it was
#                                       measured and the sim reproduced it flat
#   Every rung significant.             to four decimals.
#
# A one-sided stat SATURATES against the fixed TN — the sixth point buys far less
# than the first because the roll it improves is already passing. An opposed stat
# does not. So the ladder shape is a property of WHICH KIND of test the stat
# drives, and that is the placement rule for every unmeasured stat below.
# ---------------------------------------------------------------------------
STAT_LADDER = {
    # rung -> Credits, for a stat tested against a fixed target number
    "one_sided": {1: 37, 2: 26, 3: 27, 4: 18, 5: 15, 6: 10},   # [B] measured, DEX
    # rung -> Credits, for a stat opposed by another model's stat
    "opposed": {1: 25, 2: 25, 3: 25, 4: 25, 5: 25, 6: 25},     # [B] measured, STR
}

# Which ladder each stat reads, and why. The two measured ones anchor the rest.
STAT_KIND = {
    "dex": ("one_sided", TIER_B, "MEASURED. Shooting, vs a fixed TN."),
    "str": ("opposed", TIER_B, "MEASURED. Melee, opposed by the target's STR."),
    # [C] INT drives the objective Interact — 1d10+INT vs 7+, a fixed TN, so it
    # reads the one-sided ladder. DISCOUNTED by CONDITIONAL_F: DEX is tested on
    # essentially every activation, INT only on activations spent interacting.
    # All five shipped scenarios score through an Interact, so it is never dead.
    "int": ("one_sided", TIER_C, "DERIVED: one-sided like DEX, x CONDITIONAL_F "
                                 "because it fires on Interact activations only."),
    # [C] NRV is tested against a fixed TN (morale/Stress), so one-sided again,
    # and conditional on being under pressure at all.
    "nrv": ("one_sided", TIER_C, "DERIVED: one-sided vs a fixed TN, x CONDITIONAL_F "
                                 "because it fires only under Stress."),
    # [C] AGI is ENGINE-BLOCKED: read only inside the Dodge reaction, and
    # DODGE_ON defaults False, so it measures exactly zero by construction — a
    # property of the harness, not the game. Priced by analogy to the nearest
    # measured neighbour: Dodge is an OPPOSED reaction, so it takes the opposed
    # ladder, x CONDITIONAL_F because it only fires when someone shoots you.
    "agi": ("opposed", TIER_C, "DERIVED BY ANALOGY: opposed like STR (Dodge is a "
                               "reaction against an attack), x CONDITIONAL_F. "
                               "Cannot be measured while DODGE_ON is False."),
}


def stat_rung_credits(stat: str, rung: int) -> int:
    """Credits for taking `stat` from rung-1 to rung. The one entry point."""
    kind, tier, _ = STAT_KIND[stat]
    base = STAT_LADDER[kind][rung]
    return round(base * (CONDITIONAL_F_PROVISIONAL if tier == TIER_C else 1.0))


# [C] Kept as the scalar fallback for callers that have not moved to the ladder.
# DERIVATION: the mid value of the measured one-sided ladder. Anything costing a
# fighter's stat line should call stat_rung_credits() and get the real shape.
TICK_STAT = 15

# [C] +1 WND. DERIVATION: the nearest measured survivability atom is heavy
# armour (-2 on the injury roll) at 41 Cr, armour-level-n2500. Both buy the same
# thing — the model stays on the table longer — so +1 WND takes heavy armour's
# measured value.
#
# THIS REPLACES 45 Cr, WHICH HAD NO DERIVATION AT ALL. The ruleset says so
# itself, in three separate places: "no sim data behind it at all... a judgment
# call, not a measurement" (Full Rules System v1 sec 991), "the one number in
# this whole area with zero validation behind it" (sec 1140), and Economy.md:129.
# It was priced by POSITION — above a T2 skill, below a T3 — and it sits inside
# the +245 Cr full Level track, so it propagates into every levelled fighter.
#
# Still C: an analogy is not a measurement. But a C with a stated derivation is
# correctable from table data, which 45 never was.
#
# !! NOT YET PROPAGATED TO THE VAULT. Full Rules System v1 sec 26.1,
# Progression.md:51, List Building.md:136 and Economy.md:108 all still say 45.
# Changing those is Ross's call, not this file's.
WND_CREDITS = 41

# [C] Bare body. DERIVATION: unchanged from the legacy table — no measurement
# isolates "a model with no gear and no stats" because every roster in the
# harness is built from equipped models. It is a floor, not a priced atom, and
# the crew-size work that would measure it needs crews rebuilt to equal cost.
BODY_BASE = 20

# [C] Orders. DERIVATION: none available — Orders have never been measured as an
# Order on any engine, and there is no measured neighbour close enough to derive
# from (the nearest, an extra activation, is not isolatable in this harness).
# RETAINED at the legacy values, and this is the WEAKEST NUMBER IN THIS FILE.
# It is rank-gated and never sold a la carte, so it cannot be arbitraged by a
# list-builder, which is the only reason it is tolerable to ship.
ORDER_PREMIUM = {0: 0, 1: 40, 2: 90}

# ---------------------------------------------------------------------------
# SKILLS — a three-band scheme, deliberately coarse            [C, derived]
#
# There are ~150 skills and 9 are wired into the engine. Individually pricing the
# rest is not achievable on any reasonable timeline, so they are BANDED, and each
# band is derived from a measured atom of comparable effect size:
#
#   T1 = 20   a CONDITIONAL +1 on one kind of test.
#             DERIVED: one mid-ladder DEX rung (18) x ~1. Rounded to 20.
#   T2 = 35   an UNCONDITIONAL +1 on one kind of test, or a conditional +2.
#             DERIVED: the first DEX rung (37), the value of a point that is
#             always live. Rounded to 35.
#   T3 = 55   changes what a model may DO, rather than what a roll scores.
#             DERIVED: the dearest measured payload (suppressive, 38) plus a
#             mid-ladder rung (18) = 56. Rounded to 55.
#
# The bands survive derivation unchanged from the legacy table, which is the one
# piece of good luck in this write-back — the numbers were right, they simply had
# nothing behind them.
#
# PLACEMENT RULE — how to band a skill you are adding:
#   T1  it improves one roll, in a named situation.
#   T2  it improves one roll always, or improves one roll by 2 in a situation.
#   T3  it removes a restriction, grants an action, or affects another model.
# When a skill straddles two bands, take the LOWER and note it: a cheap skill
# that turns out strong is a table-testing correction, an expensive one that
# turns out weak never gets taken and is never observed.
# ---------------------------------------------------------------------------
SKILL_TIER_CREDITS = {1: 20, 2: 35, 3: 55}

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
CLASS_CREDITS = {
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
# behaviour verified by engine2d/check_conditions.py, 21/21).
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
# PAYLOAD PRICES REWRITTEN FROM payload-table-objective-n2500, 2026-08-13.
# Every payload figure below is NET OF PINNED: a payload lands IN PLACE OF the
# ordinary non-wounding result, and on a ranged hit that result is Pinned
# (+0.510 wp = 13 Cr). So a payload's price is what it is worth MINUS what it
# displaces, and a trait can be a perfectly good condition and still price at or
# below zero purely because Pinned is strong.
CHAR_CREDITS = {
    "brutal": CREDITS_INJURY,  # [A] 15 — the anchor itself, unchanged
    # AP is worth EXACTLY +1 Damage against an armoured target and EXACTLY ZERO
    # against a bare one — confirmed in check_conditions.py. In the armoured mirror
    # it measured 1.21/1.50 per model against +1 Damage's own 1.21/1.50: identical.
    # So its true form is 15 x f(target wears armour). 9 is the blend measured over
    # two bare lists and one armoured one. In an armoured meta it is worth 15.
    "armour_piercing": 10,  # [B] +0.392 wp. Conditional on armour prevalence; the
                            # closest agreement between a measured atom and the
                            # price it replaces (was 9) anywhere in this rebuild.
    "accurate": CREDITS_TO_HIT_CONDITIONAL,  # [C] 18 — see CONDITIONAL_F note
    "spread": CREDITS_TO_HIT_CONDITIONAL,  # [C] 18 — see CONDITIONAL_F note
    "rate_of_fire_2": 50,  # [C] 1D rebuild test, never reproduced on the 2.5D
                           # engine. Retained; no measured neighbour.
    # --- payloads, each measured on its own, NET OF PINNED -------------------
    "bleeding": 35,  # [B] +1.410 wp. The death clock at WND 1. Was 46.
    "incendiary": 23,  # [B] +0.942 wp. Was 22 — effectively confirmed.
    "suppressive": 38,  # [B] +1.546 wp. NOW THE DEAREST PAYLOAD; was 17. The Pin
                        # costing the whole activation is worth far more than the
                        # old table thought.
    "blast": 31,  # [B] +1.256 wp. Resolves against everything within 2". Was 43.
    # --- measured POSITIVE but INSIDE THE NOISE FLOOR ------------------------
    # Shipped at measured value per the shipping standard, and flagged: a trait
    # this cheap gets taken on everything, so if table data shows either being
    # auto-included, the fix is mechanical rather than a reprice.
    "shocking": 5,  # [B] +0.217 wp, NOT significant. Was 16.
    "heavy_impact": 2,  # [B] +0.090 wp, NOT significant. Was 15.
    # --- NOT PRICED: measured at or below zero. See BLOCKED_REDESIGN below. ---
    # These keep their legacy numbers ONLY so existing catalogue rows still
    # resolve. `points.verify` refuses to let them ship. Do not read them as
    # prices — the traits are pulled pending a RULES decision.
    "concussive": 30,  # !! [BLOCKED] -0.592 wp, significantly NEGATIVE
    "crippling": 30,  # !! [BLOCKED] -0.613 wp, significantly NEGATIVE
    "blinding": 4,  # !! [BLOCKED] -0.317 wp, significantly NEGATIVE
    "hook": 20,  # !! [BLOCKED] -0.230 wp, negative point estimate (SE 0.858)
    "toxic": 9,  # !! [BLOCKED] -0.080 wp, negative point estimate
    # --- [C] not measured; derived or retained, each stating which ------------
    "smoke": 30,  # [C] retained. No LOS-denial atom is measured; nearest
                  # neighbour would be Blind, which is itself blocked.
    "long_range": 60,  # [C] RETAINED AGAINST THE MEASUREMENT, deliberately. The
                       # 8"-24" curve measures FLAT (spread 1.07 inside SE ~0.81),
                       # which would price this at ~0 — but that reading is
                       # bracketed by two opposite biases (single-scenario
                       # coverage overvalues reach, the sprint overcorrection
                       # undervalues it), and a free 24" is a KNOWN degenerate:
                       # the sim measured a 13-30 point edge for a list that can
                       # fire from its own deployment on turn one. Shipping 0 here
                       # would be following a number off a cliff.
    "balanced": 20,  # [C] retained; no measured neighbour.
    "defensive": 30,  # [C] retained; nearest measured neighbour is light armour
                      # (24), which is the same shape of effect. Within rounding.
    "cleaving": 50,  # [C] retained; nearest neighbour is blast (31) as a
                     # multi-target effect, plus a damage step (15) = 46.
    "breaching": 30,  # [C] retained; no measured neighbour.
    "concealable": 20,  # [C] retained; stealth is unmodelled (no noise system).
    "quiet": 20,  # [C] retained; Loud/Quiet is engine-blocked entirely.
    "compact": 20,  # [C] retained; hands/slots are inert in the engine.
}

# ---------------------------------------------------------------------------
# BLOCKED — REDESIGN. Escalated to Ross 2026-08-13; these do NOT ship.
#
# Five traits measure at or below zero NET of Pinned. The game currently sells
# five things that make an attack WORSE than not buying them, and no price fixes
# that: repricing a trait whose whole effect is to replace a good default with a
# worse one sells the player a downgrade at any number.
#
#   concussive  -0.592  significant   Off-Balance replaces Pinned
#   crippling   -0.613  significant   Hobbled replaces Pinned
#   blinding    -0.317  significant   Blind replaces Pinned
#   hook        -0.230  n.s. (SE 0.858, unmeasurably noisy)
#   toxic       -0.080  n.s.
#
# WHY, measured directly rather than assumed — condition-values-n3000:
#
#   value(Off-Balance) = +0.000   EXACTLY. Bit-identical games.
#   value(Hobbled)     = +0.078   not significant.
#   value(Blind)       = +0.369   SIGNIFICANT AND POSITIVE.
#
# So the three are NOT one problem. Off-Balance and Hobbled are worth nothing,
# for a mechanism that was counted rather than inferred: they are applied in
# quantity (89,498 times) but land on models that have ALREADY ARRIVED and will
# not move again. Afflicted models account for 0.8% of all movement, and the
# reduced cap actually binds in 0.8% of THOSE. A movement debuff that lands after
# movement has finished binds on nothing.
#
# Blind is the opposite: a genuinely valuable condition (+0.369) that still
# prices negative, because what it REPLACES is worth more.
#
# THE DESIGN QUESTION, which is Ross's and not a measurement:
# replace-not-stack was designed when Pinned was believed to be worth ~zero.
# Pinned measures +0.510 and significant. If the default result is strong, every
# trait that replaces it starts in a hole. That is one miscalibrated rule, not
# five broken traits.
#
# ONE FURTHER COMPLICATION, logged not chased: value(Pinned) is itself
# LIST-DEPENDENT — +0.510 on the mixed rosters, +0.086 (n.s.) on a uniform rifle
# chassis. Since every payload price is net of it, the subtrahend moves with the
# crew. That is THE CEILING operating on the payload table.
# ---------------------------------------------------------------------------
BLOCKED_REDESIGN = ("concussive", "crippling", "blinding", "hook", "toxic")

# Superseded by BLOCKED_REDESIGN, which is the same idea with the measurement
# behind it. Kept as an alias so older callers do not break.
UNPRICEABLE_MEASURED_ZERO = BLOCKED_REDESIGN

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

# (The old UNPRICEABLE_MEASURED_ZERO lived here and listed two traits. It is now
# BLOCKED_REDESIGN, defined beside CHAR_CREDITS, and lists five — the 2026-08-13
# re-measurement found that these do not merely measure at zero, three of them
# measure significantly NEGATIVE. The alias is kept there for older callers.)

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
RANGE_STEP_CREDITS = {
    # [derived twice, independently, from this file]
    #   (a) CHAR_CREDITS["long_range"] == 60
    #   (b) CLASS_CREDITS["heavy_ranged"] 160
    #       == CLASS_CREDITS["standard_ranged"] 100 + long_range 60
    # Cumbersome is no longer welded onto Heavy Ranged (decision 2026-07-30), so
    # the -20 refund is gone and the class costs the clean 160. Its real cost is
    # the SLOT count: 4 against Standard Ranged's 3 — opportunity, not penalty.
    # Cumbersome remains available as an OPT-IN drawback in DRAWBACK_CREDITS.
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
DRAWBACK_CREDITS = {
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
# [B] MEASURED 2026-08-13, armour-level-n2500, with ZERO PRIOR.
#
# The old 30/60 was tagged [measured] citing `balance/armourprice.py`, WHICH HAS
# NEVER EXISTED IN ANY COMMIT ON ANY BRANCH. That is why this was re-measured
# from nothing rather than checked against the old figure.
#
#   light  +0.953 wp  =  24 Cr      heavy  +1.663 wp  =  41 Cr
#
# CORROBORATED BY REBUILD-TO-PAY, which prices armour in weapons surrendered:
#   light + (rifle->pistol)   +0.140 +- 0.200   FAIR TRADE, parity
#   heavy + (rifle->pistol)   +1.110            armour worth MORE than the payment
#   heavy + (rifle->bat)      -3.400            armour worth LESS than the payment
# So Light is worth almost exactly one rifle->pistol downgrade, and Heavy is
# bracketed on BOTH sides. That is the first time an armour price in this project
# has been denominated in a measured quantity rather than a prior.
#
# THE LADDER IS NOT LINEAR, AND THE 2x RULE IS WITHDRAWN. It argued that each
# armour point is a flat -10% on the injury roll so -2 must cost exactly 2x -1.
# That is the WRONG QUANTITY: linear in injury PROBABILITY does not imply linear
# in WIN-POINTS, because the second point buys survival on a model that is
# already surviving more often. Measured ratio 1.745 +- 0.416.
#
# THE RATIO QUESTION IS CLOSED AS UNANSWERABLE, ruled 2026-08-13. Separating 2.0
# from the old 1.667 needs N~66,000 or N~194,000 respectively, and if the true
# ratio is near 1.75 no sample size ever separates them. The individual values are
# what get used; the ratio between them is not a number anyone plays with.
#
# KNOWN BIASES, both stated because they cut in opposite directions: armour's own
# drawbacks (Improvised -1 AGI, Heavy -1 MOV / -1 AGI / Loud) are priced at ZERO
# here, so these OVERSTATE armour; and light armour's value MOVES with terrain
# density (0.140 at 11 features, 0.508 at 9), so the level is board-dependent.
ARMOUR_CREDITS = {
    "none": 0,
    "thick_clothing": 0,
    "light": 24,   # -1  [B] measured +0.953 wp
    "heavy": 41,   # -2  [B] measured +1.663 wp — NOT 2x light, and deliberately so
}

ARMOUR_INJURY = {
    "none": 0,
    "thick_clothing": 0,
    "light": -1,
    "heavy": -2,
}

HACK_GEAR_CREDITS = {
    "bare": 0,
    "breach_kit": 40,
    "exploit_suite": 80,
}

EQUIPMENT_CREDITS = {
    "med_kit": 40,
}
