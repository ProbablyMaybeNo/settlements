# -*- coding: utf-8 -*-
"""PACKET TESTS T5, T6, T8, T10, T13 — the battle-layer questions.

  T5   §2.2  is "one payload per weapon, no exceptions" load-bearing?
  T6   §3.2  is a third, NON-COMBAT-primary worked archetype (INT / NRV) viable?
  T8   §4.1  uncapped XP — find the soft ceiling N that never binds in normal play
              but still closes the degenerate tail
  T10  §4.4  the Level Surcharge — the review has "no opinion pending sim data"
  T13  §9.3  extra activations are super-linear and therefore un-priceable —
              verify the claim the Bandwidth cap rests on

METHOD — the same paired mirror as stealth2d.py: every measurement is reported as
(test - control) so any residual harness bias subtracts out. Sides swapped.

Prices are quoted against the anchor conditions2d.py established on this engine:
+1 Damage = 1.12 win-points per model = 15 Credits.
"""
import sys, os, random
from collections import Counter

ENG = r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench\engine2d"
sys.path.insert(0, ENG)
os.chdir(ENG)

import engine
from engine import Game, Unit
from board import take_a_hold
from policies import BALANCED
from data import WEAPONS

try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

N = int(sys.argv[1]) if len(sys.argv) > 1 else 800
DMG_ANCHOR = 1.12
CREDITS_PER_WINPOINT = 15.0 / DMG_ANCHOR


class Annihilate(Game):
    def score_objectives(self, rnd):
        self.vp[0] = sum(1 for u in self.sides[1] if u.out)
        self.vp[1] = sum(1 for u in self.sides[0] if u.out)
        self.timeline.append((rnd, self.vp[0], self.vp[1]))


# ---- weapon variants for T5 -------------------------------------------------
for base in ('rifle', 'pistol', 'crowbar', 'bat'):
    one = dict(WEAPONS[base]); one['traits'] = tuple(one['traits']) + ('bleeding',)
    WEAPONS[base + '+1load'] = one
    two = dict(WEAPONS[base]); two['traits'] = tuple(two['traits']) + ('bleeding', 'shocking')
    WEAPONS[base + '+2load'] = two
    three = dict(WEAPONS[base]); three['traits'] = tuple(three['traits']) + ('bleeding', 'shocking', 'crippling')
    WEAPONS[base + '+3load'] = three

DEX6 = [('Boss', 'Leader', 'rifle', 'none', dict(dex=4, str=2)),
        ('Marks', 'Specialist', 'rifle', 'none', dict(dex=4)),
        ('Gun1', 'Fighter', 'pistol', 'none', dict(dex=2)),
        ('Gun2', 'Fighter', 'pistol', 'none', dict(dex=2)),
        ('R1', 'Recruit', 'pistol', 'none', dict(dex=1)),
        ('R2', 'Recruit', 'bat', 'none', dict(str=1))]

STR6 = [('Boss', 'Leader', 'sledge', 'none', dict(str=4, nrv=2)),
        ('B1', 'Specialist', 'crowbar', 'none', dict(str=4)),
        ('B2', 'Fighter', 'crowbar', 'none', dict(str=2)),
        ('B3', 'Fighter', 'bat', 'none', dict(str=2)),
        ('R1', 'Recruit', 'bat', 'none', dict(str=1)),
        ('R2', 'Recruit', 'bat', 'none', dict(str=1))]

INT6 = [('Boss', 'Leader', 'rifle', 'none', dict(int=4, dex=2)),
        ('Tech', 'Specialist', 'pistol', 'none', dict(int=4)),
        ('T2', 'Fighter', 'pistol', 'none', dict(int=2)),
        ('T3', 'Fighter', 'bat', 'none', dict(int=2)),
        ('R1', 'Recruit', 'pistol', 'none', dict(int=1)),
        ('R2', 'Recruit', 'bat', 'none', dict(int=1))]

NRV6 = [('Boss', 'Leader', 'rifle', 'none', dict(nrv=4, dex=2)),
        ('N1', 'Specialist', 'pistol', 'none', dict(nrv=4)),
        ('N2', 'Fighter', 'pistol', 'none', dict(nrv=2)),
        ('N3', 'Fighter', 'bat', 'none', dict(nrv=2)),
        ('R1', 'Recruit', 'pistol', 'none', dict(nrv=1)),
        ('R2', 'Recruit', 'bat', 'none', dict(nrv=1))]


def crew(spec, bump=None, weapon_suffix=None, skills=(), only_first=False):
    """bump: (stat, amount) applied to every fighter. weapon_suffix: swap weapons."""
    def build(side):
        out = []
        for i, (nm, rank, wpn, arm, st) in enumerate(spec):
            st = dict(st)
            if bump and (not only_first or i == 0):
                stat, amt = bump
                st[stat] = st.get(stat, 0) + amt
            w = wpn
            if weapon_suffix and (w + weapon_suffix) in WEAPONS:
                w = w + weapon_suffix
            sk = tuple(skills) if (not only_first or i == 0) else ()
            u = Unit(nm, side, rank, w, arm, skills=sk, **st)
            u.policy = BALANCED
            out.append(u)
        return out
    return build


def versus(mkA, mkB, GameCls, n, seed=20260802, kw=None, collect=None):
    random.seed(seed)
    a = dr = 0
    acc = {}
    kw = kw or {}
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            ca, cb = mkA(0), mkB(1)
            g = GameCls(ca, cb, board, **kw); r = g.play()
            aw, bw = r['winner'] == 'A', r['winner'] == 'B'
        else:
            cb, ca = mkB(0), mkA(1)
            g = GameCls(cb, ca, board, **kw); r = g.play()
            aw, bw = r['winner'] == 'B', r['winner'] == 'A'
        a += aw
        dr += (not aw and not bw)
        if collect:
            for k, fn in collect.items():
                acc[k] = acc.get(k, 0.0) + fn(ca, g)
    out = (a + 0.5 * dr) / n
    return (out, {k: v / n for k, v in acc.items()}) if collect else out


def paired(spec, GameCls=Game, kw=None, **buff):
    ctrl = versus(crew(spec), crew(spec), GameCls, N, kw=kw)
    test = versus(crew(spec, **buff), crew(spec), GameCls, N, kw=kw)
    return (test - ctrl) * 100


def dials(**kw):
    for k, v in kw.items():
        setattr(engine, k, v)


def banner(t):
    print("\n" + "=" * 104)
    print(t)
    print("=" * 104)


def price(delta_pts, models):
    pm = delta_pts / models
    return pm, pm * CREDITS_PER_WINPOINT


# ================================ T10 =======================================
banner(f"T10 - WHAT IS A LEVEL WORTH?  (the Level Surcharge, §6.6)   {N} games/cell")
print("The review: 'no opinion on values pending testing'. A Level is a stat point")
print("(and, at a tier, a skill). Measure the stat point directly against the anchor.\n")
print(f"  {'buff':<34}{'d Hold':>9}{'d Annih':>9}{'d mean':>9}{'per model':>11}{'Credits':>9}")

for label, spec, bump in (
        ('+1 primary stat, whole crew', DEX6, ('dex', 1)),
        ('+2 primary stat, whole crew', DEX6, ('dex', 2)),
        ('+1 primary stat, ONE fighter', DEX6, ('dex', 1)),
        ('+1 STR, whole melee crew', STR6, ('str', 1)),
        ('+2 STR, whole melee crew', STR6, ('str', 2))):
    only1 = 'ONE fighter' in label
    dh = paired(spec, Game, bump=bump, only_first=only1)
    da = paired(spec, Annihilate, bump=bump, only_first=only1)
    m = (dh + da) / 2
    n_models = 1 if only1 else 6
    pm, cr = price(m, n_models)
    print(f"  {label:<34}{dh:>+8.1f} {da:>+8.1f} {m:>+8.1f} {pm:>10.2f}{cr:>9.0f}")

# ================================ T13 =======================================
banner(f"T13 - IS AN EXTRA ACTIVATION SUPER-LINEAR?   {N} games/cell")
print("The Bandwidth cap (§9.3) rests on the claim that an extra activation cannot")
print("be priced. Compare it against buying stat points on the same fighter.\n")
print(f"  {'buff (one fighter)':<34}{'d Hold':>9}{'d Annih':>9}{'d mean':>9}{'per model':>11}{'Credits':>9}")

dials(EXTRA_ACTIVATION=True)
dh = paired(DEX6, Game, skills=('extra_activation',), only_first=True)
da = paired(DEX6, Annihilate, skills=('extra_activation',), only_first=True)
m = (dh + da) / 2
pm, cr = price(m, 1)
print(f"  {'extra activation':<34}{dh:>+8.1f} {da:>+8.1f} {m:>+8.1f} {pm:>10.2f}{cr:>9.0f}")
dials(EXTRA_ACTIVATION=False)

for amt in (1, 2, 4):
    dh = paired(DEX6, Game, bump=('dex', amt), only_first=True)
    da = paired(DEX6, Annihilate, bump=('dex', amt), only_first=True)
    m = (dh + da) / 2
    pm, cr = price(m, 1)
    print(f"  {'+' + str(amt) + ' DEX (for comparison)':<34}{dh:>+8.1f} {da:>+8.1f} {m:>+8.1f}"
          f" {pm:>10.2f}{cr:>9.0f}")

# ================================ T5 ========================================
banner(f"T5 - IS THE ONE-PAYLOAD CAP LOAD-BEARING?   {N} games/cell")
print("§2.2 says cap payloads at one 'no exceptions'. Measure what the 2nd and 3rd")
print("payload on the same weapon are actually worth when the cap is lifted.\n")
print(f"  {'weapon':<34}{'d Hold':>9}{'d Annih':>9}{'d mean':>9}{'per model':>11}{'Credits':>9}")

dials(MULTI_PAYLOAD=True)
for label, suffix in (('1 payload  (Bleed)', '+1load'),
                      ('2 payloads (Bleed+Shock)', '+2load'),
                      ('3 payloads (Bleed+Shock+Hobble)', '+3load')):
    dh = paired(DEX6, Game, weapon_suffix=suffix)
    da = paired(DEX6, Annihilate, weapon_suffix=suffix)
    m = (dh + da) / 2
    pm, cr = price(m, 6)
    print(f"  {label:<34}{dh:>+8.1f} {da:>+8.1f} {m:>+8.1f} {pm:>10.2f}{cr:>9.0f}")
dials(MULTI_PAYLOAD=False)

# ================================ T6 ========================================
banner(f"T6 - IS A NON-COMBAT-PRIMARY ARCHETYPE VIABLE?   {N} games/cell")
print("§3.2 recommends a third worked example that is deliberately NOT combat-primary")
print("(INT or NRV). The vault's own finding is that INT and AGI price at ~zero in")
print("combat. Each crew below plays the same neutral DEX6 opponent.\n")
print(f"  {'crew (identical ranks/weapons/points)':<40}{'Hold':>9}{'Hold+Claim':>13}{'Annih':>9}{'mean':>9}")

for label, spec in (('STR6 (combat primary)', STR6), ('DEX6 (combat primary)', DEX6),
                    ('INT6 (technical primary)', INT6), ('NRV6 (morale primary)', NRV6)):
    h = versus(crew(spec), crew(DEX6), Game, N)
    c = versus(crew(spec), crew(DEX6), Game, N, kw=dict(claim=True))
    a = versus(crew(spec), crew(DEX6), Annihilate, N)
    print(f"  {label:<40}{h*100:>8.1f}%{c*100:>12.1f}%{a*100:>8.1f}%{(h+c+a)/3*100:>8.1f}%")

# ================================ T8 ========================================
banner(f"T8 - THE XP CEILING: HOW MANY DEED SOURCES CAN ONE FIGHTER HIT?   {N*4} battles")
print("§4.1 removes the XP cap; the review wants a generous soft ceiling that never")
print("binds in normal play but closes the unbounded tail. Below: the number of")
print("DISTINCT scoring sources a single fighter reached in one battle.\n")

SOURCES = ('kill', 'multi_kill', 'first_blood', 'melee_kill', 'terrain_kill',
           'against_odds', 'objective_holder', 'claimed', 'survivor', 'last_standing')


def deed_sources(u, game):
    s = set()
    if u.kills >= 1: s.add('kill')
    if u.kills >= 2: s.add('multi_kill')
    if u.first_blood: s.add('first_blood')
    if u.melee_kills >= 1: s.add('melee_kill')
    if u.fall_kills >= 1: s.add('terrain_kill')
    if u.odds_kills >= 1: s.add('against_odds')
    if u.objective_rounds >= 1: s.add('objective_holder')
    if u.claims >= 1: s.add('claimed')
    if u.standing(): s.add('survivor')
    if u.standing() and len(game._standing(u.side)) == 1: s.add('last_standing')
    return s


random.seed(20260802)
hist = Counter()
src_freq = Counter()
n_fighters = 0
best = 0
for i in range(N * 4):
    board = take_a_hold()
    ca, cb = crew(DEX6)(0), crew(STR6)(1)
    g = Game(ca, cb, board, claim=(i % 2 == 0))
    g.play()
    for u in ca + cb:
        s = deed_sources(u, g)
        hist[len(s)] += 1
        src_freq.update(s)
        n_fighters += 1
        best = max(best, len(s))

print(f"  {'distinct sources in one battle':<36}{'fighters':>10}{'share':>9}{'P(>= n)':>10}")
cum = n_fighters
for k in range(0, max(hist) + 1):
    cnt = hist.get(k, 0)
    print(f"  {k:<36}{cnt:>10}{cnt/n_fighters*100:>8.2f}%{cum/n_fighters*100:>9.2f}%")
    cum -= cnt
print(f"\n  max observed on any single fighter: {best} of {len(SOURCES)} possible sources")
print(f"  mean per fighter: {sum(k*v for k, v in hist.items())/n_fighters:.2f}")
print("\n  source frequency (share of all fighters achieving it):")
for s, c in src_freq.most_common():
    print(f"    {s:<22}{c/n_fighters*100:>7.2f}%")

print("\n" + "=" * 104)
print("Every row is a measurement on the 2.5D engine.")
print("=" * 104)
