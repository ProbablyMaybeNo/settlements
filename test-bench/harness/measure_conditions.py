# -*- coding: utf-8 -*-
"""What are Off-Balance, Hobbled and Blind actually WORTH, measured directly?

RULED 2026-08-13. Three payload traits price significantly NEGATIVE net of Pinned
- concussive -0.592, crippling -0.613, blinding -0.317 - and the tempting story
is that today's Off-Balance ruling caused it. That story does not fit: crippling
and blinding do not touch the Sprint code path and moved anyway. A tidy
explanation that fits some of the data is how this project has been burned
before, so the mechanism is measured rather than argued.

THE METHOD, and it is the one value(Pinned) already used, one level along.

A ranged payload lands IN PLACE OF the ordinary non-wound result, which is
Pinned. So every payload price on record is a DIFFERENCE:

    net(trait)  =  value(condition)  -  value(Pinned)

value(Pinned) was measured by suppressing it: a `null_payload` variant that
replaces the ordinary result with NOTHING. That same variant is the baseline this
script needs. Against a null-payload crew there is no Pinned term at all, so:

    baseline  = rifle+null_payload   -> non-wound does nothing
    buffed    = rifle+concussive     -> non-wound applies Off-Balance
    delta     = value(Off-Balance),  gross, with no subtrahend

Each condition is then also measured NET, against a plain rifle, and the two
routes are checked against each other on the SAME chassis:

    net(trait)  =?=  value(condition) - value(Pinned)

That check is the point of doing it this way. Every quantity here is measured on
one uniform chassis, so composing them is legitimate - unlike the range hops in
THE CEILING, which compose across DIFFERENT baseline crews and disagree by ~39%
precisely because the chassis is part of the price. If these three disagree
anyway, that is a finding about the estimator, not about crews.

CHASSIS. A uniform rifle crew, every model on the same rung. Until 2026-08-13
this configuration was believed unmeasurable on hold_claim - it drew 99.3% of
games at 0.00 VP - and that belief was a bug, not a property: the AI never
Sprinted and never took an objective Interact while it had a target. Post-fix it
resolves at 33.7% draws and gives the TIGHTEST cells of any roster, which is what
an isolate should do. Uniform also means one weapon name, so a single
`weapon_swap` can move the whole crew between variants without the trait-order
ambiguity that `payload_of` would otherwise introduce (it takes traits[0], so
stacking null_payload and concussive on one weapon would silently measure the
null).

    py -3.13 measure_conditions.py [N]
"""
from __future__ import annotations

# IMPORT GUARD. This file is a SCRIPT: it runs its whole measurement at module
# level. `import measure_conditions` would therefore execute a full sweep as a
# side effect - which happened TWICE in one session on other scripts, once
# silently writing an artefact from a known-broken board ladder that then passed
# every provenance check. Loud raise rather than a `__main__` wrapper: the
# failure being guarded is silent, so the guard must not be.
if __name__ != "__main__":
    raise RuntimeError(
        f"{__name__} is a script, not a module - importing it would run its entire "
        "measurement as a side effect. Run it with `py -3.13 <file>.py` instead, or "
        "move the helper you wanted into a module."
    )

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "engine2d"))

import anchor as A  # noqa: E402
import effects as E  # noqa: E402
import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from data import WEAPONS  # noqa: E402
from rosters import uniform  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
ANCHOR = A.VALUE

# Fingerprinted BEFORE the games run: Envelope's default_factory fields evaluate
# at CONSTRUCTION, which is after the run, so an edit landing mid-run would stamp
# a result with code that never executed.
ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()

BASE_WEAPON = "rifle"
NULL = E.register_trait_variant(WEAPONS, BASE_WEAPON, "null_payload")

# trait -> the condition it delivers, per engine.PAYLOAD_TRAITS
CONDITIONS = [
    ("concussive", "Off-Balance", "denies Sprint and Charge; persists"),
    ("crippling", "Hobbled", "-2 MOV; persists"),
    ("blinding", "Blind", "-2 on sight rolls, this activation + next"),
]
for trait, _, _ in CONDITIONS:
    E.register_trait_variant(WEAPONS, BASE_WEAPON, trait)


# WHY THE MECHANISM IS INSTRUMENTED AND NOT INFERRED.
#
# The first run of this script returned value(Off-Balance) = +0.000 and
# value(Hobbled) = +0.000 with SE 0.000 - bit-identical games, not small effects.
# A hard zero is exactly the shape of a broken instrument, and this project has
# already shipped one (the density ladder whose terrain never changed a LOS check,
# giving four-decimal-identical cells that looked like a clean null).
#
# So the zero is not reported on its own. These counters record WHERE the
# conditions land relative to when models actually move, which is the difference
# between "the harness did nothing" and "the condition binds on nothing".
# Pure counters: they always delegate and never alter a decision.
import engine as _engine  # noqa: E402

TRACE = {"applied": 0, "moves": 0, "moves_by_afflicted": 0, "capped_by_affliction": 0}
_orig_move, _orig_payload = _engine.Game.move_to, _engine.Game.apply_payload


def _traced_move(self, u, point, max_dist):
    TRACE["moves"] += 1
    if u.off_balance or u.hobbled:
        TRACE["moves_by_afflicted"] += 1
        # Did the affliction actually BIND? A shorter cap changes nothing when the
        # model was travelling less than the cap anyway - `toward()` arrives either
        # way. This separates "was slowed" from "was slower on paper".
        from board import dist as _dist
        if _dist(u.pos, point) > max_dist:
            TRACE["capped_by_affliction"] += 1
    return _orig_move(self, u, point, max_dist)


def _traced_payload(self, att, dfn, ranged, payload):
    if payload in ("off_balance", "hobbled"):
        TRACE["applied"] += 1
    return _orig_payload(self, att, dfn, ranged, payload)


_engine.Game.move_to = _traced_move
_engine.Game.apply_payload = _traced_payload


def crew(weapon):
    return uniform("dex", 2, weapon, 6)


def swap_to(weapon, label):
    return E.Effect(kind="weapon_swap", weapon=weapon, name=label,
                    require_ranged=True)


print("=" * 108)
print(f"CONDITION VALUES — measured directly, not inferred. N={N}/cell, paired mirror")
print("=" * 108)
print(A.describe())
print()
print(f"chassis: uniform {BASE_WEAPON} (6), all models DEX+2")
print(f"baseline for GROSS rows: {NULL} — a non-wound applies nothing at all")
print()

rows = []


def run(label, spec, eff, note=""):
    res = M.price_atom(spec, eff, n=N)
    wp = res["price_wp"]
    if wp is None:
        print(f"  {label:<34}  ALL OBJECTIVE CELLS DEGENERATE — no value")
        rows.append({"row": label, "wp": None, "note": note, **res})
        return None, None
    se = res["price_se"]
    lo, hi = res["price_ci"]
    cr = wp / ANCHOR * 15
    print(f"  {label:<34}{wp:>+9.3f}{se:>7.3f}  [{lo:+.3f}, {hi:+.3f}]{cr:>7.0f}"
          f"  {'yes' if res['price_significant'] else ' no':>4}"
          f"{'  SIGN-SPLIT' if res['sign_split'] else ''}")
    rows.append({"row": label, "wp": wp, "se": se, "ci": [lo, hi],
                 "credits": round(cr, 1), "significant": res["price_significant"],
                 "sign_split": res["sign_split"], "note": note,
                 "cells": res["cells"], "priced_from": res["priced_from"],
                 "dropped_degenerate": res["dropped_degenerate"]})
    return wp, se


print(f"  {'row':<34}{'wp':>9}{'SE':>7}{'95% CI':>19}{'Cr':>7}   sig")
print("  " + "-" * 82)

# 1. value(Pinned) on THIS chassis. Re-measured here rather than imported from
#    value-of-pinned: that run is on FIRETEAM/SQUAD/ARMOURED, and THE CEILING
#    says a value measured on one chassis does not transfer to another. The
#    subtrahend has to come from the same crew as the thing it is subtracted from.
pin_wp, pin_se = run("suppress Pinned (= -value(Pinned))",
                     crew(BASE_WEAPON), swap_to(NULL, f"swap:{NULL}"),
                     note="negative of value(Pinned) on this chassis")

print()
print("  GROSS — each condition against a baseline that applies NOTHING")
print("  " + "-" * 82)
gross = {}
for trait, cond, mech in CONDITIONS:
    variant = f"{BASE_WEAPON}+{trait}"
    gross[trait] = run(f"value({cond})", crew(NULL), swap_to(variant, f"swap:{variant}"),
                       note=f"{trait} -> {cond}: {mech}")

print()
print("  NET — the same conditions against the ordinary result they replace")
print("  " + "-" * 82)
net = {}
for trait, cond, _ in CONDITIONS:
    variant = f"{BASE_WEAPON}+{trait}"
    net[trait] = run(f"net({trait}) = value({cond}) - value(Pinned)",
                     crew(BASE_WEAPON), swap_to(variant, f"swap:{variant}"),
                     note="what the payload table prices")

# --- the internal consistency check, which is why all of this is on one chassis
print()
print("=" * 108)
print("  CONSISTENCY — composed vs direct, all on ONE chassis so composition is legitimate")
print("=" * 108)
value_pinned = None if pin_wp is None else -pin_wp
checks = []
if value_pinned is not None:
    print(f"  value(Pinned) on this chassis = {value_pinned:+.3f}")
    print()
    print(f"  {'condition':<20}{'direct net':>12}{'composed':>11}{'gap':>10}{'gap SE':>9}  verdict")
    for trait, cond, _ in CONDITIONS:
        g_wp, g_se = gross[trait]
        n_wp, n_se = net[trait]
        if g_wp is None or n_wp is None:
            continue
        composed = g_wp - value_pinned
        gap = composed - n_wp
        gse = (g_se ** 2 + n_se ** 2 + (pin_se or 0) ** 2) ** 0.5
        ok = abs(gap) <= 1.96 * gse
        print(f"  {cond:<20}{n_wp:>+12.3f}{composed:>+11.3f}{gap:>+10.3f}{gse:>9.3f}"
              f"  {'consistent' if ok else 'INCONSISTENT'}")
        checks.append({"condition": cond, "direct_net": n_wp, "composed": round(composed, 4),
                       "gap": round(gap, 4), "gap_se": round(gse, 4), "consistent": ok})
    print()
    print("  A failure here would NOT be a claim about crews - every row shares one")
    print("  chassis, so THE CEILING's list-context effect cannot explain it. It would")
    print("  mean the replace-not-stack arithmetic itself does not hold.")

print()
print("=" * 108)
print("  WHY THE MOVEMENT CONDITIONS READ ZERO — the mechanism, counted not assumed")
print("=" * 108)
_afflicted_share = TRACE["moves_by_afflicted"] / max(1, TRACE["moves"])
_bind_share = TRACE["capped_by_affliction"] / max(1, TRACE["moves_by_afflicted"])
print(f"  Off-Balance / Hobbled applied            {TRACE['applied']:>8}")
print(f"  move_to calls, all models                {TRACE['moves']:>8}")
print(f"  move_to calls by an AFFLICTED model      {TRACE['moves_by_afflicted']:>8}"
      f"   ({_afflicted_share:.1%} of all movement)")
print(f"  ...where the shorter cap actually BOUND   {TRACE["capped_by_affliction"]:>8}"
      f"   ({_bind_share:.1%} of those)")
print()
print("  READING: the conditions land, in quantity. They land on models that have")
print("  ALREADY ARRIVED and will not move again — a gunner shoots from where it")
print("  stands once inside IN_POSITION, so its MOV is never read. Of the residue")
print("  that does move, the moves are shorter than the cap, so a reduced cap")
print("  changes no position. Hence bit-identical games and a hard zero.")
print()
print("  THIS IS AN AI LIMITATION, NOT A RULES FACT. A player repositions, falls")
print("  back, chases and breaks contact; this policy does none of those once in")
print("  position. So the zero is a LOWER bound on both conditions. What it does")
print("  establish is that the payload table's concussive/crippling rows are")
print("  measuring the LOSS OF PINNED and nothing else.")
print()
print("=" * 108)
print("  WHAT THIS DOES AND DOES NOT SETTLE")
print("=" * 108)
print("  Settled: what each condition is worth on its own, with no Pinned term.")
print("  NOT settled: whether the replace-not-stack RULE is calibrated. If Pinned")
print("  is strong, a trait can be a fine condition and still price negative purely")
print("  because of what it displaces. That is a design question and it is Ross's.")
print("  NOT settled: duration. No policy calls clear_movement_condition, so")
print("  Off-Balance and Hobbled run to the end of the game once applied. These")
print("  values are therefore an UPPER bound on both.")

env = P.Envelope(
    name=f"condition-values-n{N}",
    question="What are Off-Balance, Hobbled and Blind worth on their own, measured "
             "against a baseline that applies nothing - rather than inferred from the "
             "payload prices, which are all net of Pinned?",
    values={
        "value_pinned_this_chassis": None if value_pinned is None else round(value_pinned, 4),
        "gross": {c: (None if gross[t][0] is None else round(gross[t][0], 4))
                  for t, c, _ in CONDITIONS},
        "net": {t: (None if net[t][0] is None else round(net[t][0], 4))
                for t, _, _ in CONDITIONS},
        "consistency": checks,
        "anchor_used": ANCHOR,
        "anchor_provisional": A.PROVISIONAL,
    },
    raw_cells=rows,
    params={"N_per_cell": N, "chassis": f"uniform {BASE_WEAPON} (6), DEX+2",
            "null_baseline": NULL,
            "method": "paired mirror; weapon_swap between trait variants",
            "pricing_scenarios": list(M.PRICING_SCENARIOS),
            "diagnostic_scenarios": list(M.DIAGNOSTIC_SCENARIOS),
            # The zero is only interpretable with these beside it.
            "mechanism_trace": dict(TRACE),
            "afflicted_share_of_movement": round(_afflicted_share, 4),
            "share_of_those_where_cap_bound": round(_bind_share, 4)},
    caveats=[
        "UPPER BOUND on Off-Balance and Hobbled: no policy calls "
        "clear_movement_condition, so once applied they persist to the end of the "
        "game. A player would spend a Move to shed them. Blind is not affected - it "
        "expires on its own after the next activation.",
        "Ranged only. A melee non-wound is Shaken, not Pinned, so there is no "
        "equivalent baseline on the melee side and none of this transfers to it.",
        "Measured on a UNIFORM chassis. THE CEILING (tracking doc, head) measures a "
        "~39% list-context effect on weapon value, so these numbers belong to this "
        "crew and should not be assumed to carry to a mixed one. The consistency "
        "check above is valid precisely because it never leaves this chassis.",
        "value(Pinned) is re-measured here rather than imported from "
        "value-of-pinned-n4000 for the same reason - that run uses different rosters.",
        "Off-Balance's value depends on how often a model WANTS to sprint, which the "
        "policy fix changed. It is therefore coupled to the Sprint threshold and is "
        "not a pure property of the condition.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")
