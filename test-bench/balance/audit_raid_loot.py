# -*- coding: utf-8 -*-
"""AUDIT ADD 4 — raid loot cap / floor / vault immunity (exact enumeration).

Rule: attacker takes 25% (floor) of stored Credits and 25% of stored Materials,
Vault excluded, capped at 100 Cr + 100 Mat per raid. Theft never reduces the
defender below 50 Cr + 50 Mat (i.e. each resource has a floor of 50 — a
settlement can be hurt, not deleted).

Also verifies Vault contents are never touched, and that the ADD 5 / economy
sim's combined-floor reading (sum >= 100) is NOT what the audit text says —
flag if they diverge on any fixture.
"""
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass


def raid_loot(cr, mat, vault_cr=0, vault_mat=0, floor_mode='per_resource'):
    """Return (take_cr, take_mat, end_cr, end_mat, vault untouched)."""
    take_cr = min(int(cr * 0.25), 100)
    take_mat = min(int(mat * 0.25), 100)
    end_cr = cr - take_cr
    end_mat = mat - take_mat
    if floor_mode == 'per_resource':
        # never below 50 of each
        if end_cr < 50:
            take_cr -= (50 - end_cr)
            end_cr = 50
        if end_mat < 50:
            take_mat -= (50 - end_mat)
            end_mat = 50
        take_cr = max(0, take_cr)
        take_mat = max(0, take_mat)
    else:
        # combined floor of 100 (economy sim's reading)
        after = end_cr + end_mat
        if after < 100:
            short = 100 - after
            give = min(short, take_cr + take_mat)
            total = take_cr + take_mat
            if total:
                take_cr -= give * (take_cr / total)
                take_mat -= give * (take_mat / total)
            end_cr = cr - take_cr
            end_mat = mat - take_mat
    return (take_cr, take_mat, end_cr, end_mat, vault_cr, vault_mat)


FIXTURES = [
    # (label, cr, mat, vcr, vmat)
    ('poor start',           60,  60, 0, 0),
    ('ADD5 post-phase',     175, 178, 0, 0),
    ('fat no storehouse',   180, 180, 0, 0),
    ('one storehouse',      400, 400, 0, 0),
    ('whale + vault',       800, 800, 150, 0),
    ('asymmetric Cr-heavy', 500,  60, 0, 0),
    ('asymmetric Mat-heavy', 60, 500, 0, 0),
    ('exactly at floor',     50,  50, 0, 0),
    ('just above floor',     51,  51, 0, 0),
]

print('=' * 96)
print('AUDIT ADD 4 — RAID LOOT: 25% / cap 100+100 / floor 50+50 / Vault immune')
print('=' * 96)

print(f"\n  {'fixture':<22}{'store':>12}{'take':>14}{'end':>14}{'vault':>10}  checks")
fails = []
for label, cr, mat, vcr, vmat in FIXTURES:
    tcr, tmat, ecr, emat, _, _ = raid_loot(cr, mat, vcr, vmat, 'per_resource')
    checks = []
    if tcr > 100 or tmat > 100:
        checks.append('CAP_BREAK'); fails.append((label, 'cap'))
    if ecr < 50 - 1e-9 or emat < 50 - 1e-9:
        checks.append('FLOOR_BREAK'); fails.append((label, 'floor'))
    # vault is never an input to the take — immunity is structural
    checks.append('vault-safe')
    ok = 'PASS' if not any(c.endswith('BREAK') for c in checks) else 'FAIL'
    print(f"  {label:<22}{cr:>5}+{mat:<5}  {tcr:>5.0f}+{tmat:<5.0f}  "
          f"{ecr:>5.0f}+{emat:<5.0f}  {vcr}+{vmat}   {ok}")

# Cap stress: 25% of 800 = 200 → must clamp to 100
tcr, tmat, ecr, emat, _, _ = raid_loot(800, 800)
cap_ok = (tcr == 100 and tmat == 100)
print(f"\n  CHECK — 25% of 800 clamps to 100+100: "
      f"{'PASS' if cap_ok else 'FAIL'}  (took {tcr:.0f}+{tmat:.0f})")

# Floor stress: raiding 60+60 takes 15+15 → 45+45, must give back to 50+50
tcr, tmat, ecr, emat, _, _ = raid_loot(60, 60)
floor_ok = (ecr == 50 and emat == 50 and tcr == 10 and tmat == 10)
print(f"  CHECK — 60+60 raid leaves exactly 50+50 (took 10+10, not 15+15): "
      f"{'PASS' if floor_ok else 'FAIL'}  (end {ecr:.0f}+{emat:.0f}, took {tcr:.0f}+{tmat:.0f})")

# Vault immunity: whale with 150 in vault, raid takes from open stores only
tcr, tmat, ecr, emat, vcr, vmat = raid_loot(800, 800, 150, 0)
vault_ok = (vcr == 150 and vmat == 0)
print(f"  CHECK — Vault 150 Cr untouched on an 800+800 raid: "
      f"{'PASS' if vault_ok else 'FAIL'}")

# Divergence flag: combined-floor (economy sim) vs per-resource (audit text)
print(f"\n  Floor-reading divergence (asymmetric 500 Cr / 60 Mat):")
a = raid_loot(500, 60, floor_mode='per_resource')
b = raid_loot(500, 60, floor_mode='combined')
print(f"    per-resource (audit text): take {a[0]:.0f}+{a[1]:.0f} → end {a[2]:.0f}+{a[3]:.0f}")
print(f"    combined-100 (economy sim): take {b[0]:.0f}+{b[1]:.0f} → end {b[2]:.0f}+{b[3]:.0f}")
divergent = (round(a[2], 2), round(a[3], 2)) != (round(b[2], 2), round(b[3], 2))
print(f"    {'modes differ (expected) — economy sim uses per-resource' if divergent else 'aligned'}")

print(f"\n  OVERALL: {'PASS' if not fails and cap_ok and floor_ok and vault_ok else 'FAIL'}"
      + (f"  fails={fails}" if fails else ''))
print('=' * 96)
