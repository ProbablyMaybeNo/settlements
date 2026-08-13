"""Do atom values move with terrain density? Every number to date sits at one density.

WHY THIS IS IN SCOPE WHILE PRICING IS NOT
-----------------------------------------
The rebuild is blocked on SCENARIO coverage - one of five shipped scenarios is
modelled, so every price carries single-scenario bias. Density is a DIFFERENT
axis and is not gated by that: the question here is whether an atom's value is
stable across boards, and it can be answered on hold_claim alone because it is a
comparison of the atom against ITSELF at three densities, not a price.

WHY IT MATTERS. The ruleset makes density the single largest lever in the game:

  "Terrain density alone produced a 66-point swing in win rate - bigger than any
   points cost could ever produce. A 4-model elite crew beats a 14-model horde
   81% of the time on a sparse board and 15% on a crowded one. Parity sits at
   9-12 exactly."          - Full Rules System v1 sec 187 / Crew Sim - Findings

Every atom in this rebuild was measured on ONE board at ONE density. If atom
values move materially across the legal 9-12 band, then a single global price is
a statement about the centre of that band and its spread belongs in the number -
exactly the finding the stat ladder produced about rungs.

The legal band is 9-12 large features. This sweeps 9, 11 and 12: the floor, the
middle, and the ceiling.

    py -3.13 measure_density.py [N]
"""

from __future__ import annotations

# IMPORT GUARD. This file is a SCRIPT: it runs its whole measurement at module
# level. `import measure_x` therefore executes a full sweep as a side effect -
# which happened TWICE in one session, once silently writing an artefact from a
# known-broken board ladder that then passed every provenance check.
#
# Deliberately a loud raise rather than the usual `if __name__ == "__main__":`
# wrapper. The wrapper makes an accidental import a silent no-op; this says why
# nothing happened. The failure being guarded is a silent one, so the guard is
# not silent.
if __name__ != "__main__":
    raise RuntimeError(
        f"{__name__} is a script, not a module - importing it would run its entire "
        "measurement as a side effect. Run it with `py -3.13 <file>.py` instead, or "
        "move the helper you wanted into a module."
    )

import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import anchor as A  # noqa: E402
import effects as E  # noqa: E402
import measure as M  # noqa: E402
import provenance as P  # noqa: E402
from board import Piece  # noqa: E402
from rosters import ARMOURED6, FIRETEAM6, MIXED6  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000

ENGINE_AT_START = P.engine_fingerprint()
COST_AT_START = P.cost_table_fingerprint()
HARNESS_AT_START = P.harness_fingerprint()
GIT_AT_START = P.git_state()

DENSITIES = (9, 11, 12)


def density_board(n_features):
    """take_a_hold, rebuilt with n_features LARGE features, mirror-symmetric.

    The 3 objective buildings are fixed - they carry the objectives and moving
    them would change the scenario rather than the density. The remaining
    features are drawn from a fixed pool IN ORDER, so 9 is a strict subset of 11
    and 11 of 12: the boards are nested, and a difference between them is the
    added terrain rather than a different layout.

    Symmetry is preserved by adding features in mirrored PAIRS about y=18, so
    neither deployment ever faces a harder approach than the other.
    """
    terrain = [
        Piece(3, 15, 9, 21, cover=2, height=4, name='obj-bldg-L'),
        Piece(15, 15, 21, 21, cover=2, height=4, name='obj-bldg-C'),
        Piece(27, 15, 33, 21, cover=2, height=4, name='obj-bldg-R'),
    ]
    # POOL PIECES MUST SIT IN THE APPROACH LANES.
    #
    # The first version of this pool added small scatter (cover=1, height=1) out
    # in dead space, and the sweep returned values identical to FOUR DECIMALS at
    # every density. That was not a null result, it was a broken ladder: with the
    # paired estimator both arms run the same seed, so terrain that never changes
    # a LOS check, a cover roll or a move produces bit-identical games. A "no
    # effect" reading from that board would have been a measurement of nothing.
    #
    # These are LOS-blocking, heavy-cover buildings straddling the lanes between
    # the deployment bands and the centreline objectives - the ground models
    # actually walk and shoot through.
    pool = [
        Piece(8, 6, 15, 11, cover=2, blocks=True, height=5, name='bldg-lane-L'),
        Piece(28, 5, 34, 10, cover=2, blocks=True, height=5, name='bldg-lane-R'),
        Piece(16, 7, 21, 12, cover=2, blocks=True, height=5, name='bldg-lane-C'),
        Piece(2, 11, 7, 15, cover=2, blocks=True, height=4, name='bldg-flank-L'),
        Piece(29, 11, 34, 15, cover=2, blocks=True, height=4, name='bldg-flank-R'),
    ]
    # A CENTRELINE piece is its own mirror, so it adds ONE feature without
    # breaking symmetry. Without it only odd counts are reachable (3 fixed + 2k),
    # and 12 - the top of the legal band - would be unbuildable.
    centre = Piece(10, 16.5, 14, 19.5, cover=2, blocks=True, height=4, name='bldg-centre')

    pairs, add_centre = {9: (3, False), 11: (4, False), 12: (4, True)}[n_features]
    for p in pool[:pairs]:
        terrain.append(p)
        terrain.append(Piece(p.x1, 36 - p.y2, p.x2, 36 - p.y1,
                             cover=p.cover, blocks=p.blocks,
                             height=p.height, name=p.name + "'"))
    if add_centre:
        terrain.append(centre)
    return dict(size=36.0, terrain=terrain,
                objectives=[(6, 18), (18, 18), (30, 18)],
                deploy={0: (0, 0, 36, 6), 1: (0, 30, 36, 36)}), len(terrain)


# Patch the board factory measure.mirror uses, so the sweep changes the board and
# nothing else. Restored in a finally.
_real_board = M.take_a_hold

LISTS = {"Fireteam (6)": FIRETEAM6, "Mixed (6)": MIXED6, "Armoured (6)": ARMOURED6}
ATOMS = {
    "+1 Damage (anchor)": E.damage_anchor(),
    "armour:light": E.Effect(kind="armour", armour="light", name="armour:light"),
    "payload:bleeding": E.Effect(kind="weapon_trait", trait="bleeding", name="bleeding"),
}

print("=" * 112)
print(f"DENSITY SWEEP — do atom values move across the legal 9-12 band? N={N}/cell")
print("=" * 112)
print(A.describe())
print("Priced on hold_claim. This is an atom compared against ITSELF at three")
print("densities - a stability check, not a price.")
print()

rows = []
try:
    for atom_name, eff in ATOMS.items():
        print(f"  {atom_name}")
        print(f"    {'features':<10}{'wp/model':>10}{'SE':>7}{'95% CI':>18}"
              f"{'vs 11':>9}  sig")
        per_density = {}
        for d in DENSITIES:
            board, actual = density_board(d)
            M.take_a_hold = lambda b=board: {
                'size': b['size'], 'terrain': b['terrain'],
                'objectives': list(b['objectives']), 'deploy': dict(b['deploy'])}
            vals, ses = [], []
            for spec in LISTS.values():
                res = M.price_atom(spec, eff, n=N)
                if res["price_wp"] is not None:
                    vals.append(res["price_wp"])
                    ses.append(res["price_se"])
            if not vals:
                print(f"    {actual:<10}  ALL CELLS DEGENERATE")
                continue
            mean = statistics.fmean(vals)
            pooled = (sum(s * s for s in ses) ** 0.5) / len(ses)
            per_density[d] = {"features": actual, "wp": mean, "se": pooled,
                              "ci": [mean - 1.96 * pooled, mean + 1.96 * pooled],
                              "significant": abs(mean) > 1.96 * pooled}
        base = per_density.get(11, {}).get("wp")
        for d in DENSITIES:
            r = per_density.get(d)
            if not r:
                continue
            rel = f"{r['wp'] / base:.2f}x" if base else "   -"
            print(f"    {r['features']:<10}{r['wp']:>+10.3f}{r['se']:>7.3f}"
                  f"  [{r['ci'][0]:+.3f}, {r['ci'][1]:+.3f}]{rel:>9}"
                  f"  {'yes' if r['significant'] else ' no'}")
            rows.append({"atom": atom_name, "density_target": d, **r})
        # Does the spread across densities exceed what sampling noise explains?
        if len(per_density) >= 2:
            lo = min(per_density.values(), key=lambda r: r["wp"])
            hi = max(per_density.values(), key=lambda r: r["wp"])
            gap = hi["wp"] - lo["wp"]
            gap_se = (lo["se"] ** 2 + hi["se"] ** 2) ** 0.5
            moves = abs(gap) > 1.96 * gap_se
            print(f"    spread {lo['wp']:+.3f}..{hi['wp']:+.3f} = {gap:+.3f} "
                  f"+-{gap_se:.3f}  ->  {'MOVES with density' if moves else 'stable within noise'}")
        print()
finally:
    M.take_a_hold = _real_board

print("  READING. 'Stable within noise' does NOT mean density is unimportant - the")
print("  ruleset's 66-point swing is about WIN RATE between asymmetric crews, which is")
print("  a different quantity from an atom's marginal value in a symmetric mirror.")
print("  These two can both be true: density decides who wins, while the marginal")
print("  value of +1 Damage stays put.")

env = P.Envelope(
    name=f"density-sweep-n{N}",
    question="Do atom values move across the legal 9-12 terrain band? Every number in the "
            "rebuild was taken at one density; if atoms move, a single global price is a "
            "statement about the centre of the band and the spread belongs in the number.",
    values={f"{r['atom']}@{r['features']}": r["wp"] for r in rows},
    raw_cells=rows,
    params={"N_per_cell": N, "densities_targeted": list(DENSITIES),
            "pricing_scenarios": list(M.PRICING_SCENARIOS),
            "lists": list(LISTS), "atoms": list(ATOMS),
            "anchor_wp_per_model": A.VALUE, "anchor_provisional": A.PROVISIONAL,
            "method": "paired mirror on nested, mirror-symmetric boards"},
    caveats=[
        "STABILITY CHECK, NOT A PRICE. Each atom is compared against ITSELF across "
        "densities. No Credits figure here is new.",
        "Boards are NESTED - 9 is a subset of 11 and 11 of 12 - so a difference is the "
        "ADDED terrain rather than a different layout. Mirrored pairs alone reach only odd "
        "counts (3 fixed + 2k), so 12 uses a CENTRELINE-straddling piece, which is its own "
        "mirror and adds one feature without making A and B face different approaches.",
        "The pool pieces are LOS-blocking heavy cover in the approach lanes, NOT scatter. "
        "An earlier pool of small scatter in dead space returned values identical to four "
        "decimals at every density - because the paired estimator runs both arms on one "
        "seed, terrain that never changes a LOS check or a move yields bit-identical games. "
        "That would have read as a clean null while measuring nothing.",
        "The ruleset's 66-point density swing is a WIN-RATE effect between asymmetric "
        "crews (4 elite vs 14 horde). This measures the marginal value of an atom in a "
        "SYMMETRIC mirror. Both can be true at once: density can decide who wins while an "
        "atom's marginal value stays put. A null here does not contradict the ruleset.",
        "Measured under single-scenario coverage (hold_claim only), so it inherits the "
        "static bias of control play like everything else in this rebuild.",
    ],
    engine=ENGINE_AT_START,
    cost_table=COST_AT_START,
    harness=HARNESS_AT_START,
    git=GIT_AT_START,
)
out = env.write()
print(f"\n[stamped] {out.name}")
