"""Canonical game data — the single source of truth for the 2D engine.

Phase 0: hand-authored to match the Obsidian vault (Rules System) as of the
Recruit/Fighter rename + the reworked Weapons/Damage tables. Phase 0.5 will
GENERATE this file by parsing the vault's markdown tables so it can never drift.
Until then: if a number changes in the vault, change it here.
"""

# rank -> stat points / skill slots / Orders / points cost
RANKS = {
    'Recruit':    dict(stat_pts=0, skills=0, orders=0, cost=5),
    'Fighter':    dict(stat_pts=2, skills=1, orders=0, cost=8),
    'Champion':   dict(stat_pts=7, skills=0, orders=1, cost=16),
    'Specialist': dict(stat_pts=4, skills=2, orders=1, cost=16),
    'Leader':     dict(stat_pts=6, skills=3, orders=2, cost=24),
}

# --- proposed V2 stat system: more points, capped by tier -> forces spread ---
# a stat's tier: +2/+3 = T1, +4/+5 = T2, +6 = T3  (0/+1 = untrained / dabble, no skill)
def tier_of(v):
    return 3 if v >= 6 else 2 if v >= 4 else 1 if v >= 2 else 0


RANKS_V2 = {   # strict caps — forces maximal spread (one T1 spike, rest dabbles)
    'Recruit':  dict(points=3, caps={1: 0, 2: 0, 3: 0}, cost=5),    # no tiered stat -> no skill
    'Fighter':  dict(points=5, caps={1: 1, 2: 0, 3: 0}, cost=8),
    'Champion': dict(points=7, caps={1: 3, 2: 1, 3: 0}, cost=16),
    'Leader':   dict(points=9, caps={1: 4, 2: 2, 3: 1}, cost=24),
}

RANKS_V2_GENTLE = {   # looser caps — a strong primary + one REAL secondary (the flex-point idea)
    'Recruit':  dict(points=3, caps={1: 1, 2: 0, 3: 0}, cost=5),
    'Fighter':  dict(points=5, caps={1: 2, 2: 0, 3: 0}, cost=8),    # up to two T1 -> dual-role
    'Champion': dict(points=7, caps={1: 2, 2: 1, 3: 0}, cost=16),
    'Leader':   dict(points=9, caps={1: 3, 2: 2, 3: 1}, cost=24),
}


def validate_statline(rank, stats, ranks=RANKS_V2):
    """stats: {path-stat: value}. Legal under the ruleset's points + per-tier caps?"""
    spec = ranks[rank]
    total = sum(stats.values())
    counts = {1: 0, 2: 0, 3: 0}
    for v in stats.values():
        t = tier_of(v)
        if t:
            counts[t] += 1
    if total > spec['points']:
        return False, f'{total}/{spec["points"]} pts (over budget)'
    for t in (1, 2, 3):
        if counts[t] > spec['caps'][t]:
            return False, f'{counts[t]} stats at T{t} > cap {spec["caps"][t]}'
    skills = sum(1 for v in stats.values() if tier_of(v) >= 1)   # one skill per tiered stat
    shape = "/".join(f"T{tier_of(v)}" for v in sorted(stats.values(), reverse=True) if v)
    return True, f'{total}/{spec["points"]} pts · {shape or "no tiers"} · {skills} skills'

# armour -> injury modifier (added to the injury roll, i.e. negative), cost
# No drawbacks (2026-07-30). Linear: each armour point is a flat -10% on the
# injury roll, so -2 costs exactly twice -1. Improvised and Light share a profile
# and a price; they differ only in acquisition (crafted vs bought).
ARMOUR = {
    'none':   dict(injury=0,  cost=0),
    'light':  dict(injury=-1, cost=3),
    'heavy':  dict(injury=-2, cost=6),
}

# built weapon profiles (class + characteristics), from Weapons.md.
# rng: inches (0 = melee) · dmg: +Damage on the injury roll · kind: melee/ranged/thrown
WEAPONS = {
    'fists':   dict(rng=0,  dmg=0, kind='melee',  cost=0,  traits=()),
    'bat':     dict(rng=0,  dmg=1, kind='melee',  cost=0,  traits=()),
    'crowbar': dict(rng=0,  dmg=2, kind='melee',  cost=7,  traits=('breaching',)),
    'sledge':  dict(rng=0,  dmg=3, kind='melee',  cost=8,  traits=('two_handed',)),
    'pistol':  dict(rng=8,  dmg=2, kind='ranged', cost=4,  traits=('sidearm', 'loud')),
    'rifle':   dict(rng=18, dmg=3, kind='ranged', cost=10, traits=('loud', 'two_handed')),
    'molotov': dict(rng=6,  dmg=1, kind='thrown', cost=9,  traits=('fire', 'blast', 'single_use')),
}

EQUIPMENT = {
    'breach_kit':    dict(cost=4, hack_mod=1),
    'exploit_suite': dict(cost=8, hack_mod=2),
    'med_kit':       dict(cost=4),
}

# deployables (from Deployables.md). build = modifier on the deploy INT test;
# turrets are standing hardware: WND 1, Armour -2, auto-fire once/round.
DEPLOYABLES = {
    'autoturret': dict(cost=12, build=-1, kind='turret', rng=18, dmg=3, hit=0, shots=1),
    'sniper_turret': dict(cost=15, build=-2, kind='turret', rng=24, dmg=3, hit=1, shots=1),
    'burst_turret': dict(cost=18, build=-2, kind='turret', rng=18, dmg=2, hit=0, shots=2),
}

COVER_MOD = {0: 0, 1: -1, 2: -2, 3: -3}   # open / light / heavy / hidden


def unit_cost(rank, weapon='bat', armour='none', equip=(), deployable=None):
    c = RANKS[rank]['cost'] + WEAPONS[weapon]['cost'] + ARMOUR[armour]['cost']
    c += sum(EQUIPMENT[e]['cost'] for e in equip)
    if deployable:
        c += DEPLOYABLES[deployable]['cost']
    return c
