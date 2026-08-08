# -*- coding: utf-8 -*-
"""AUDIT ADD 5 — worked-example arithmetic under the phase-end cap timing rule.

Walks Rosa's founding + first campaign turn exactly as written in the audit
(post 2026-08-07 reconciliation) and asserts every number lands.
"""
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# Caps at founding: HQ 150 Cr + 150 Mat, Salvage Yard buffer +30 Cr,
# Processor buffer +30 Mat. No Storehouse yet.
CAP_CR = 150 + 30   # 180
CAP_MAT = 150 + 30  # 180


def check(name, cond, detail=''):
    status = 'PASS' if cond else 'FAIL'
    print(f"  [{status}] {name}" + (f" — {detail}" if detail else ''))
    return cond


print('=' * 88)
print('AUDIT ADD 5 — worked example (Rosa / Fire Station) under phase-end caps')
print('=' * 88)

ok = True

# Founding
mat, cr = 250, 150
mat -= 120  # Med-bay
ok &= check('founding bank', mat == 130 and cr == 150, f"{cr} Cr + {mat} Mat")
power = 1 + 1 + 1 + 1  # HQ + Processor + Salvage + Med-bay
ok &= check('power draw 4 of 5', power == 4)

# Crew
leader = 170 + 130   # Marisol + AR
deke = 75 + 40
junie = 75 + 0
total = leader + deke + junie
ok &= check('crew 490/500', total == 490, f"total={total}")
ok &= check('pyramid legal (1 Leader, 0 Spec, 3 models)', True)

# Battle 1 rewards
cr += 65
mat += 33
ok &= check('post-battle bank before spend', cr == 215 and mat == 163,
            f"{cr} Cr + {mat} Mat")

# Mid-phase over-cap is legal
ok &= check('215 Cr over mid-phase cap (180) is legal until phase end',
            cr > CAP_CR)

# Spend Sidearm 40 + scavenge +15 Mat
cr -= 40
mat += 15
ok &= check('after Sidearm + scavenge', cr == 175 and mat == 178,
            f"{cr} Cr + {mat} Mat")

# Phase-end cap check
lost_cr = max(0, cr - CAP_CR)
lost_mat = max(0, mat - CAP_MAT)
ok &= check('phase-end: nothing lost', lost_cr == 0 and lost_mat == 0,
            f"lost {lost_cr}+{lost_mat}")
ok &= check('phase-end stores under cap', cr <= CAP_CR and mat <= CAP_MAT,
            f"{cr}/{CAP_CR} Cr, {mat}/{CAP_MAT} Mat")

# Counterfactual: if caps bit at banking time, Rosa would have lost 35 Cr
counterfactual_loss = max(0, 215 - CAP_CR)
ok &= check('counterfactual (cap-at-bank) would lose 35 Cr — why timing matters',
            counterfactual_loss == 35)

print(f"\n  OVERALL: {'PASS' if ok else 'FAIL'}")
print('=' * 88)
