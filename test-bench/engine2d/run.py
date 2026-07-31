"""Run the 2D Take-a-Hold engine.

    py -3.13 run.py                 # one verbose game (balanced mirror) + VP timeline
    py -3.13 run.py 3000            # aggregate balanced mirror (symmetry check)
    py -3.13 run.py matrix 2000     # policy matrix: balanced / runner / hunter
    py -3.13 run.py lonerunner 3000 # THE degeneracy test — does rushing objectives beat fighting?

Every matchup SWAPS SIDES each game (half with policy-A deploying bottom, half
top) so board/first-move bias cancels and only the policy difference shows.
"""
import random
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

from board import take_a_hold
from crews import redline, redline_turret, redline_v2, redline_v2_stacked, redline_v2_gentle
from engine import Game


def series(n, pa, pb, lone_a=False, lone_b=False, seed=20260717):
    """Return dict with policy-A's win/loss/draw + avg VP + avg survivors,
    aggregated over n games with sides swapped every other game."""
    random.seed(seed)
    w = {'a': 0, 'b': 0, 'draw': 0}
    vp = [0, 0]      # [policy-A total, policy-B total]
    al = [0, 0]
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:                                  # policy-A on side 0
            g = Game(redline(0, pa, lone_a), redline(1, pb, lone_b), board)
            r = g.play()
            a_side, b_side = 0, 1
            aw = r['winner'] == 'A'
            bw = r['winner'] == 'B'
        else:                                           # policy-A on side 1
            g = Game(redline(0, pb, lone_b), redline(1, pa, lone_a), board)
            r = g.play()
            a_side, b_side = 1, 0
            aw = r['winner'] == 'B'
            bw = r['winner'] == 'A'
        w['a' if aw else 'b' if bw else 'draw'] += 1
        vp[0] += r['vp'][a_side]; vp[1] += r['vp'][b_side]
        al[0] += r['alive'][a_side]; al[1] += r['alive'][b_side]
    return dict(w=w, vp=[vp[0] / n, vp[1] / n], al=[al[0] / n, al[1] / n], n=n)


def winpct(s):
    return (s['w']['a'] + 0.5 * s['w']['draw']) / s['n']


def line(s, na, nb):
    print(f"    {na} win {winpct(s):5.1%}   {nb} win {1-winpct(s)-s['w']['draw']/s['n']:5.1%}"
          f"   draw {s['w']['draw']/s['n']:5.1%}")
    print(f"    avg VP {na} {s['vp'][0]:4.1f}   {nb} {s['vp'][1]:4.1f}      "
          f"survivors {na} {s['al'][0]:4.1f}   {nb} {s['al'][1]:4.1f}")


def one_game(seed=20260717):
    random.seed(seed)
    board = take_a_hold()
    g = Game(redline(0, 'balanced'), redline(1, 'balanced'), board, log=True)
    res = g.play()
    cost = sum(u.cost for u in g.sides[0])
    print("=" * 62)
    print(f"SETTLEMENTS 2D ENGINE — Take a Hold  (balanced mirror, {cost}/100 pts)")
    print("=" * 62)
    print("VP timeline (scored each End Phase, no scoring in R1):")
    print(f"    {'round':>5}{'A vp':>7}{'B vp':>7}   leader")
    prev = (0, 0)
    for rnd, a, b in res['timeline']:
        lead = 'A' if a > b else 'B' if b > a else '='
        print(f"    {rnd:>5}{a:>7}{b:>7}   {lead}   (+{a-prev[0]}/{b-prev[1]})")
        prev = (a, b)
    print(f"\nRESULT {res['winner']}   final VP {res['vp']}   survivors A/B {res['alive']}")


def aggregate(n):
    s = series(n, 'balanced', 'balanced')
    print("=" * 62)
    print(f"BALANCED MIRROR — {n} games, sides swapped (symmetry check)")
    print("=" * 62)
    line(s, 'A', 'B')
    print("\n  Symmetric board + side-swap -> this MUST be ~50/50. Any gap is an engine bug.")


def matrix(n):
    pols = ['balanced', 'runner', 'hunter']
    print("=" * 62)
    print(f"POLICY MATRIX — row's win% vs column   ({n} games/cell, sides swapped)")
    print("=" * 62)
    print(f"    {'row \\ col':<12}" + "".join(f"{p:>11}" for p in pols))
    for pa in pols:
        cells = []
        for pb in pols:
            cells.append(f"{winpct(series(n, pa, pb))*100:9.0f} ")
        print(f"    {pa:<12}" + "".join(cells))
    print("\n  If 'runner' beats 'balanced', rushing objectives without fighting is degenerate.")


def lonerunner(n):
    print("=" * 62)
    print(f"LONE-RUNNER DEGENERACY TEST — {n} games each, sides swapped")
    print("=" * 62)
    print("\n[1] Balanced (fights)  vs  Runner (pure objective-rush, never attacks)")
    line(series(n, 'balanced', 'runner'), 'Balanced', 'Runner')
    print("\n[2] Balanced  vs  Balanced + one lone runner (5 fight, 1 only rushes objectives)")
    line(series(n, 'balanced', 'balanced', lone_b=True), 'Plain', 'Lone-runner crew')
    print("\n  Verdict: if the fighting crew wins clearly, objective-primary is ROBUST —")
    print("  you must fight to hold, so combat stays the tool and the objective stays the point.")


def deployables_test(n):
    """Crew-integration: does adding an Autoturret break Take-a-Hold? Turret crew
    (policy-A) vs the plain crew, sides swapped."""
    random.seed(20260717)
    w = {'turret': 0, 'plain': 0, 'draw': 0}
    vp = [0, 0]; al = [0, 0]
    tc = sum(u.cost for u in redline_turret(0))
    pc = sum(u.cost for u in redline(0, 'balanced'))
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            g = Game(redline_turret(0), redline(1, 'balanced'), board)
            r = g.play(); ts, ps = 0, 1
            tw, pw = r['winner'] == 'A', r['winner'] == 'B'
        else:
            g = Game(redline(0, 'balanced'), redline_turret(1), board)
            r = g.play(); ts, ps = 1, 0
            tw, pw = r['winner'] == 'B', r['winner'] == 'A'
        w['turret' if tw else 'plain' if pw else 'draw'] += 1
        vp[0] += r['vp'][ts]; vp[1] += r['vp'][ps]
        al[0] += r['alive'][ts]; al[1] += r['alive'][ps]
    print("=" * 62)
    print(f"CREW-INTEGRATION — Autoturret crew ({tc}pt) vs plain crew ({pc}pt)")
    print(f"  {n} games, sides swapped")
    print("=" * 62)
    tw = (w['turret'] + 0.5 * w['draw']) / n
    print(f"    Turret crew win {tw:5.1%}   plain win {1-tw-w['draw']/n:5.1%}   draw {w['draw']/n:5.1%}")
    print(f"    avg VP turret {vp[0]/n:4.1f}   plain {vp[1]/n:4.1f}      "
          f"survivors turret {al[0]/n:4.1f}   plain {al[1]/n:4.1f}")
    print("\n  ~50-60% = a strong-but-fair addition. >70% = the turret is oppressive (nerf).")


def _versus(n, buildA, buildB, claim=False, seed=20260718):
    """A vs B, sides swapped every other game, aggregated for A. Optional claim mode."""
    random.seed(seed)
    w = {'a': 0, 'b': 0, 'draw': 0}
    vp = [0, 0]; al = [0, 0]
    for i in range(n):
        b = take_a_hold()
        if i % 2 == 0:
            r = Game(buildA(0), buildB(1), b, claim=claim).play(); asd, bsd = 0, 1
            aw, bw = r['winner'] == 'A', r['winner'] == 'B'
        else:
            r = Game(buildB(0), buildA(1), b, claim=claim).play(); asd, bsd = 1, 0
            aw, bw = r['winner'] == 'B', r['winner'] == 'A'
        w['a' if aw else 'b' if bw else 'draw'] += 1
        vp[0] += r['vp'][asd]; vp[1] += r['vp'][bsd]; al[0] += r['alive'][asd]; al[1] += r['alive'][bsd]
    return dict(w=w, vp=[vp[0] / n, vp[1] / n], al=[al[0] / n, al[1] / n], n=n)


def statsystem(n):
    """V2 rank system: prove the stat lines are legal, then test whether forced
    SPREAD beats STACKING when the game rewards multi-tasking (hack-to-claim)."""
    from data import validate_statline

    from data import RANKS_V2 as _R
    from data import RANKS_V2_GENTLE as _G

    def show(label, crew, ranks=_R):
        print(f"\n{label}:")
        for u in crew:
            ok, detail = validate_statline(u.rank, u.stats, ranks)
            sl = " ".join(f"{k.upper()}{v:+d}" for k, v in u.stats.items())
            print(f"  [{'ok ' if ok else 'ILLEGAL'}] {u.name:<8}{u.rank:<9}{sl:<40}{detail}")

    def report(tag, s, na, nb):
        awr = (s['w']['a'] + 0.5 * s['w']['draw']) / s['n']
        print(f"\n{tag}")
        print(f"  {na} {awr:5.1%}   {nb} {1-awr-s['w']['draw']/s['n']:5.1%}   draw {s['w']['draw']/s['n']:5.1%}")
        print(f"  avg VP {na} {s['vp'][0]:.1f} / {nb} {s['vp'][1]:.1f}"
              f"      survivors {na} {s['al'][0]:.1f} / {nb} {s['al'][1]:.1f}")

    print("=" * 66)
    print("V2 STAT SYSTEM — where does the tier cap belong? (softened hack-to-claim)")
    print("=" * 66)
    show("GENTLE — loose caps: strong primary + one REAL secondary", redline_v2_gentle(0), _G)
    show("SPREAD — strict caps: one spike, rest +1 dabbles", redline_v2(0))
    show("STACKED — uncapped: all-in one stat (what any cap forbids)", redline_v2_stacked(0))

    print("\n" + "-" * 66)
    print("Scenario: Take a Hold + hack-to-claim (claim = sticky ownership; keep a")
    print("body on it to score; enemy must re-claim to flip). {} games/row.".format(n))
    print("-" * 66)
    report("[1] GENTLE vs STACKED (the specialists):",
           _versus(n, redline_v2_gentle, redline_v2_stacked, claim=True), "gentle", "stacked")
    report("[2] GENTLE vs SPREAD (the thin generalists):",
           _versus(n, redline_v2_gentle, redline_v2, claim=True), "gentle", "spread")
    report("[3] SPREAD vs STACKED (the two ends):",
           _versus(n, redline_v2, redline_v2_stacked, claim=True), "spread", "stacked")
    print("\n  GENTLE winning both = the sweet spot is a strong primary + one real")
    print("  secondary — not maximal forced spread, and not pure stacking.")


def sweep(n):
    """Sensitivity: at what height-advantage strength does roof-camping tip to dominant?"""
    import board
    print("=" * 62)
    print(f"HEIGHT-ADVANTAGE SENSITIVITY SWEEP — {n} games/row, sides swapped")
    print("=" * 62)
    print(f"    {'height rule':<26}{'roof win%':>10}   VP r/g   surv r/g")
    for mode, label in [('off', 'none'), ('light', 'ignore Light (RAW)'),
                        ('minus1', '−1 any cover'), ('minus2', '−2 any cover')]:
        board.HEIGHT_MODE = mode
        s = series(n, 'roof', 'balanced')
        print(f"    {label:<26}{winpct(s)*100:8.1f}%   {s['vp'][0]:.1f}/{s['vp'][1]:.1f}   {s['al'][0]:.1f}/{s['al'][1]:.1f}")
    board.HEIGHT_MODE = 'light'
    print("\n  Roof matchups at the RAW rule (ignore Light):")
    line(series(n, 'roof', 'runner'), 'Roof', 'Runner')
    line(series(n, 'roof', 'hunter'), 'Roof', 'Hunter')
    print("\n  The rule where roof win% crosses ~60% is where camping tips to dominant.")


def roofs_test(n):
    """2.5D verticality: do units that seize the objective rooftops (height advantage
    + see-over LOS) dominate ground play? Sides swapped."""
    print("=" * 62)
    print(f"ROOF DOMINANCE TEST — {n} games each, sides swapped")
    print("=" * 62)
    print("\n[1] Roof crew (ranged take the objective rooftops)  vs  ground crew")
    line(series(n, 'roof', 'balanced'), 'Roof', 'Ground')
    print("\n  ~50-55% = height is a fair edge. >65% = roofs dominate — the terrain note's")
    print("  'watch for roof-camping' dial is real; consider capping the height bonus.")


if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == 'statsys':
        statsystem(int(args[1]) if len(args) > 1 else 3000)
    elif args and args[0] == 'sweep':
        sweep(int(args[1]) if len(args) > 1 else 3000)
    elif args and args[0] == 'roofs':
        roofs_test(int(args[1]) if len(args) > 1 else 3000)
    elif args and args[0] == 'matrix':
        matrix(int(args[1]) if len(args) > 1 else 2000)
    elif args and args[0] == 'deployables':
        deployables_test(int(args[1]) if len(args) > 1 else 3000)
    elif args and args[0] == 'lonerunner':
        lonerunner(int(args[1]) if len(args) > 1 else 3000)
    elif args and args[0].isdigit():
        aggregate(int(args[0]))
    else:
        one_game()
