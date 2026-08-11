"""Crew specs, importable without side effects.

These lived in measure_anchor.py, which runs its campaign at module level — so
`from measure_anchor import FIRETEAM6` silently re-ran a 24,000-game measurement
as an import side effect. Twice, before it was noticed. Data belongs somewhere
importing it costs nothing.

A spec is a list of (name, rank, weapon, armour, stats-dict), consumed by
measure.build().
"""

from __future__ import annotations

# The three mirror lists conditions2d.py uses, reproduced exactly so any number
# taken here is comparable to the M4 table it supersedes.
FIRETEAM6 = [('Boss', 'Leader', 'rifle', 'none', dict(dex=4, str=2)),
             ('Marks', 'Specialist', 'rifle', 'none', dict(dex=4)),
             ('Gun1', 'Fighter', 'pistol', 'none', dict(dex=2)),
             ('Gun2', 'Fighter', 'pistol', 'none', dict(dex=2)),
             ('R1', 'Recruit', 'pistol', 'none', dict(dex=1)),
             ('R2', 'Recruit', 'bat', 'none', dict(str=1))]

SQUAD8 = [('Boss', 'Leader', 'rifle', 'none', dict(dex=2, str=2, nrv=2)),
          ('F1', 'Fighter', 'pistol', 'none', dict(dex=2)),
          ('F2', 'Fighter', 'pistol', 'none', dict(dex=2)),
          ('F3', 'Fighter', 'pistol', 'none', dict(dex=2)),
          ('R1', 'Recruit', 'pistol', 'none', dict(dex=1)),
          ('R2', 'Recruit', 'pistol', 'none', dict(dex=1)),
          ('R3', 'Recruit', 'bat', 'none', dict()),
          ('R4', 'Recruit', 'bat', 'none', dict())]

ARMOURED6 = [('Boss', 'Leader', 'rifle', 'heavy', dict(dex=4, str=2)),
             ('Marks', 'Specialist', 'rifle', 'heavy', dict(dex=4)),
             ('Gun1', 'Fighter', 'pistol', 'light', dict(dex=2)),
             ('Gun2', 'Fighter', 'pistol', 'light', dict(dex=2)),
             ('R1', 'Recruit', 'pistol', 'light', dict(dex=1)),
             ('R2', 'Recruit', 'bat', 'light', dict(str=1))]

# A MIXED crew, added because the pure lists each have a degenerate scenario:
# an all-rifle mirror draws 100% of Hold games (neither side can displace the
# other off its own objective), and a pure-melee crew cannot express a ranged
# trait at all. This one resolves in both scenarios and can carry either.
MIXED6 = [('Boss', 'Leader', 'rifle', 'none', dict(dex=4, str=2)),
          ('Spec', 'Specialist', 'sledge', 'none', dict(str=4)),
          ('F1', 'Fighter', 'rifle', 'none', dict(dex=2)),
          ('F2', 'Fighter', 'crowbar', 'none', dict(str=2)),
          ('R1', 'Recruit', 'pistol', 'none', dict(dex=1)),
          ('R2', 'Recruit', 'bat', 'none', dict(str=1))]


def uniform(stat: str, value: int, weapon: str, n: int = 6):
    """Every model on the SAME rung, so a measured delta belongs to that rung and
    is not an average over a mixed stat line."""
    ranks = ['Leader', 'Specialist', 'Fighter', 'Fighter', 'Recruit', 'Recruit'][:n]
    return [(f'U{i}', ranks[i], weapon, 'none', {stat: value}) for i in range(n)]


ALL = {"Fireteam (6)": FIRETEAM6, "Squad (8)": SQUAD8,
       "Armoured (6)": ARMOURED6, "Mixed (6)": MIXED6}
