# -*- coding: utf-8 -*-
"""AUDIT FIX 1 (new check) — the Fate table under modifiers, old rule vs FIX 1.

Old rule: result = band(d10 + modifier). A staffed Med-bay (+2) makes the minimum
result 3 — Death (band 1) becomes unreachable.
FIX 1: a natural 1 is always Dead, a natural 10 is always Hardened, modifiers
shift everything else, and total Fate modifiers cap at +2.

Bands (v1 s26.3): 1 Dead · 2-3 Grievous · 4-5 Captured · 6-8 Scar ·
9 Recovery · 10 Hardened (results past 10 clamp to Hardened).

Exact enumeration — no sampling.
"""
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

BANDS = [(1, 1, 'Dead'), (2, 3, 'Grievous'), (4, 5, 'Captured'),
         (6, 8, 'Scar'), (9, 9, 'Recovery'), (10, 99, 'Hardened')]
ORDER = ['Dead', 'Grievous', 'Captured', 'Scar', 'Recovery', 'Hardened']


def band(v):
    v = max(1, v)
    for lo, hi, name in BANDS:
        if lo <= v <= hi:
            return name
    return 'Hardened'


def dist_old(mod):
    d = {k: 0 for k in ORDER}
    for die in range(1, 11):
        d[band(die + mod)] += 10
    return d


def dist_fix1(mod):
    mod = min(mod, 2)                     # FIX 1: total Fate modifiers cap at +2
    d = {k: 0 for k in ORDER}
    for die in range(1, 11):
        if die == 1:
            d['Dead'] += 10               # natural 1 is always Dead
        elif die == 10:
            d['Hardened'] += 10           # natural 10 is always Hardened
        else:
            d[band(die + mod)] += 10
    return d


print('=' * 84)
print('AUDIT FIX 1 — FATE TABLE, exact result distribution (%) by modifier')
print('=' * 84)
for label, fn in (('OLD RULE (v1 as written)', dist_old), ('FIX 1', dist_fix1)):
    print(f"\n  {label}")
    print(f"  {'mod':<14}" + ''.join(f"{k:>10}" for k in ORDER))
    for mod, note in ((0, 'no Med-bay'), (1, 'Med-bay'), (2, 'Med-bay+worker'),
                      (3, 'future stack')):
        d = fn(mod)
        print(f"  +{mod} {note:<11}" + ''.join(f"{d[k]:>10}" for k in ORDER))

print(f"\n  CHECK 1 — death risk is never zero under FIX 1: "
      f"{'PASS' if all(dist_fix1(m)['Dead'] == 10 for m in range(0, 4)) else 'FAIL'}"
      f"  (flat 10% at every modifier)")
print(f"  CHECK 2 — old rule kills Death at +2: "
      f"{'CONFIRMED BUG' if dist_old(2)['Dead'] == 0 else 'not reproduced'}")
print(f"  CHECK 3 — Med-bay still worth building under FIX 1 "
      f"(Grievous+Captured shrink, Recovery+Hardened grow):")
b0, b2 = dist_fix1(0), dist_fix1(2)
bad0 = b0['Grievous'] + b0['Captured']
bad2 = b2['Grievous'] + b2['Captured']
good0 = b0['Recovery'] + b0['Hardened']
good2 = b2['Recovery'] + b2['Hardened']
print(f"    bad outcomes {bad0}% -> {bad2}%   good outcomes {good0}% -> {good2}%   "
      f"{'PASS' if bad2 < bad0 and good2 > good0 else 'FAIL'}")
print('=' * 84)
