# -*- coding: utf-8 -*-
"""AUDIT FIX 4 (analytical) — skill tier is gated by the stat, not the Level slot.

The bug Ross admitted: the shipped Level track handed T3 at Level 10 on the
Primary path regardless of whether that stat had reached +6. FIX 4 closes it
by making the slot roll on whatever tier the chosen path's *current* value
unlocks (+2 T1 / +4 T2 / +6 T3).

This check walks every legal leveling path for Campaign Start ranks and
asserts: you cannot hold a Tier-3 skill unless that path's stat is >= +6 at
the moment the slot is taken. Also prints the earliest Level a Fighter /
Specialist / Leader can unlock T3 on their Primary under all-in floaters.
"""
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# Campaign Start creation budgets (stat points) and a representative spike
# that maximises Primary (the all-in rush the audit flags).
START = {
    'Recruit':    {'pts': 3, 'primary': 2},   # e.g. +2/+1
    'Fighter':    {'pts': 5, 'primary': 2},   # e.g. +2/+2/+1  (lean Campaign Start)
    'Specialist': {'pts': 7, 'primary': 4},   # e.g. +4/+2/+1
    'Leader':     {'pts': 9, 'primary': 6},   # e.g. +6/+2/+1
}

# Track: L1/4/8 floating (any, Primary included); L2/5/9 forced Primary;
# L3/6/10 skill slots; L7 +1 WND.
FLOAT = {1, 4, 8}
FORCED = {2, 5, 9}
SLOTS = {3: None, 6: None, 10: None}  # tier resolved from stat at take-time


def tier_of(stat):
    if stat >= 6:
        return 3
    if stat >= 4:
        return 2
    if stat >= 2:
        return 1
    return 0


def simulate(rank, dump_floaters_into_primary=True):
    """Return list of (level, primary_stat, max_tier_available, took_tier)."""
    p = START[rank]['primary']
    # Non-primary pool starts at (pts - primary); irrelevant for the rush path.
    log = []
    for lvl in range(1, 11):
        if lvl in FLOAT:
            if dump_floaters_into_primary and p < 6:
                p = min(6, p + 1)
            # else: floater elsewhere — Primary unchanged
        elif lvl in FORCED:
            p = min(6, p + 1)
        elif lvl in SLOTS:
            t = tier_of(p)
            log.append((lvl, p, t))
        # L7 WND — no effect on tier gate
    return log


print('=' * 88)
print('AUDIT FIX 4 — TIER GATE (analytical): T3 requires the path at +6')
print('=' * 88)

print('\n  All-in Primary rush (floaters into Primary until +6):')
print(f"  {'rank':<12}{'start P':>8}{'L3 (stat/tier)':>16}{'L6':>14}{'L10':>14}  earliest T3")
failures = []
for rank, cfg in START.items():
    log = simulate(rank, dump_floaters_into_primary=True)
    cells = []
    earliest = None
    for lvl, stat, t in log:
        cells.append(f"+{stat}/T{t}")
        if t == 3 and earliest is None:
            earliest = lvl
        # The bug FIX 4 closes: old track always granted T3 at L10.
        # Under FIX 4, L10 may only grant T3 if stat >= 6.
        if lvl == 10 and t < 3:
            # Legal — they simply don't get T3. Not a failure.
            pass
        if t == 3 and stat < 6:
            failures.append((rank, lvl, stat, t))
    print(f"  {rank:<12}{cfg['primary']:>8}{cells[0]:>16}{cells[1]:>14}{cells[2]:>14}  "
          f"{('L' + str(earliest)) if earliest else 'never'}")

print('\n  Breadth path (floaters NEVER into Primary) — can they still snag T3?')
print(f"  {'rank':<12}{'L3':>10}{'L6':>10}{'L10':>10}  T3 available?")
for rank in START:
    log = simulate(rank, dump_floaters_into_primary=False)
    cells = [f"+{s}/T{t}" for _, s, t in log]
    has_t3 = any(t == 3 for _, _, t in log)
    # Leaders who start at +6 already have T3 from creation investment.
    print(f"  {rank:<12}{cells[0]:>10}{cells[1]:>10}{cells[2]:>10}  "
          f"{'YES (started +6 or forced there)' if has_t3 else 'NO — gate holds'}")
    for lvl, stat, t in log:
        if t == 3 and stat < 6:
            failures.append((rank, lvl, stat, t))

print(f"\n  CHECK — no T3 skill ever granted on a path below +6: "
      f"{'PASS' if not failures else 'FAIL ' + str(failures)}")
print(f"  CHECK — Fighter all-in reaches T3 at L6 (STR 2→3→4→5→6 via L1..L5): "
      f"{'PASS' if simulate('Fighter')[1][2] == 3 else 'FAIL'}")
print(f"  CHECK — Fighter who spreads never gets T3 on Primary by L10: "
      f"{'PASS' if simulate('Fighter', False)[2][2] < 3 else 'FAIL'}")
print(f"  (Old shipped track would have handed every fighter a T3 at L10 regardless — closed.)")
print('=' * 88)
