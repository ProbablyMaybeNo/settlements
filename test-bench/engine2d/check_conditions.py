# -*- coding: utf-8 -*-
"""Behavioural checks for the condition layer, against Conditions.md as written.

Not a balance harness — this asks 'does the rule do what the note says?' before
any price is derived from it. Run: py -3.13 check_conditions.py

RENAMED FROM test_conditions.py, 2026-08-13, and the name was the whole defect.
This is an executable script, not a pytest module: it runs its checks at import
and calls sys.exit at the end. Under the old name pytest COLLECTED it, the exit
fired during collection, and a collection error interrupts the entire run — so
`pytest` from the repo root or from test-bench/ reported `no tests ran` and the
harness suite silently did not execute. Same failure class as the sys.path
collection error fixed by harness/conftest.py, one directory further out.

The fix is the name, not an ignore rule: a file is only collected under the
convention its name advertises, so a script that is not a pytest module must
not be called test_*.py. The __main__ guard below is the second half — if
anything ever imports this file, it runs the checks and reports, but it does
not kill the importing process.
"""
import sys, os, random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import engine
from engine import Game, Unit, PAYLOAD_TRAITS
from board import take_a_hold
from policies import BALANCED
from data import WEAPONS

try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

FAILS = []


def check(name, cond, detail=""):
    print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"   {detail}" if detail else ""))
    if not cond:
        FAILS.append(name)


def fresh_game():
    a = [Unit('A1', 0, 'Fighter', 'rifle', dex=2)]
    b = [Unit('B1', 1, 'Fighter', 'rifle', dex=2)]
    for u in a + b:
        u.policy = BALANCED
    g = Game(a, b, take_a_hold())
    g._spawn()
    return g, a[0], b[0]


print("=" * 72)
print("CONDITION LAYER — behaviour vs Conditions.md")
print("=" * 72)

# --- Bleed: -1 WND each End Phase; at WND 1 that is a two-round death clock ---
g, a, b = fresh_game()
b.bleed = True
g.resolve_conditions(b)
check("Bleed drops a WND-1 fighter to Down on the first End Phase",
      b.down and not b.out, f"down={b.down} out={b.out}")
g.resolve_conditions(b)
check("Down + Bleed bleeds out on the second End Phase", b.out, f"out={b.out}")

# --- Poison: -1 all rolls, STR 7+ to clear ----------------------------------
g, a, b = fresh_game()
b.poison = True
check("Poison is -1 on tests", b.penalty() == 1, f"penalty={b.penalty()}")
random.seed(1)
cleared = 0
for _ in range(2000):
    u = Unit('t', 0, 'Fighter', 'bat', str=0)
    u.poison = True
    g.resolve_conditions(u)
    cleared += not u.poison
check("Poison clears on a STR 7+ test (~40% at STR 0)",
      0.35 < cleared / 2000 < 0.45, f"{cleared/2000:.1%}")

# --- Blind: -2 on SIGHT rolls only; clears in the End Phase ------------------
g, a, b = fresh_game()
b.blind = True
check("Blind is -2 on sight rolls only",
      b.penalty(sight=True) == 2 and b.penalty() == 0,
      f"sight={b.penalty(sight=True)} non-sight={b.penalty()}")
g.resolve_conditions(b)
check("Blind does NOT clear in the End Phase any more", b.blind)
b.blind = 2
g.activate(b); g.activate(b)
check("Blind ends at the end of its next activation", not b.blind)

# --- Shocked: -2 all rolls, cannot React ------------------------------------
g, a, b = fresh_game()
b.shocked = True
check("Shocked is -2 on all rolls", b.penalty() == 2, f"penalty={b.penalty()}")
check("Shocked cannot React", not b.can_react())
g.resolve_conditions(b)
check("Shocked does NOT clear in the End Phase any more", b.shocked)
b.shocked = 2
g.activate(b); g.activate(b)
check("Shocked ends at the end of its next activation", not b.shocked)

# --- the -3 cap -------------------------------------------------------------
g, a, b = fresh_game()
b.stress, b.poison, b.shocked, b.blind = 3, True, 2, 2
check("Modifier cap holds at -3 however many conditions stack",
      b.penalty(sight=True) == 3, f"penalty={b.penalty(sight=True)}")

# --- Hobbled: -2 MOV, expires at the end of its next activation --------------
g, a, b = fresh_game()
check("Base MOV is 6", b.mov == 6.0, f"mov={b.mov}")
b.hobbled = True
check("Hobbled is -2 MOV", b.mov == 4.0, f"mov={b.mov}")
g.activate(b); g.activate(b)
check("Hobbled PERSISTS across activations until cleared", b.hobbled and b.mov == 4.0)
check("Hobbled sheds for the Move slot, like Pinned",
      g.clear_movement_condition(b) is True and not b.hobbled and b.mov == 6.0)

# --- Off-Balance: no Sprint / no Charge -------------------------------------
g, a, b = fresh_game()
b.off_balance = True
start = b.pos
g.move_to(b, (start[0] + 30, start[1]), 2 * b.mov)
moved = abs(b.pos[0] - start[0])
check("Off-Balance denies the Sprint outright, and the denial sheds NOTHING",
      moved < 1e-6 and b.off_balance,
      f"moved {moved:.1f}\", off_balance={b.off_balance}")
b.off_balance = True
g.activate(b); g.activate(b)
check("Off-Balance PERSISTS until something sheds it", b.off_balance)

# --- Suppressive: clearing the pin costs the ENTIRE activation ---------------
g, a, b = fresh_game()
b.pinned = True
check("An ordinary Pin clears with the Move and keeps the Action",
      g.clear_pin(b) is True)
b.pinned = True; b.suppressed = True
check("A Suppressed pin costs the whole activation",
      g.clear_pin(b) is False and not b.suppressed)

# --- Payload replaces the non-wounding result, and gives exactly +1 Stress ---
g, a, b = fresh_game()
b.stress = 0
g.apply_payload(a, b, True, 'bleed')
check("A payload gives exactly +1 Stress, same as Pinned would",
      b.stress == 1 and b.bleed and not b.pinned,
      f"stress={b.stress} bleed={b.bleed} pinned={b.pinned}")
g, a, b = fresh_game()
g.apply_payload(a, b, True, None)
check("No payload -> the ordinary ranged result is Pinned +1 Stress",
      b.pinned and b.stress == 1)

# --- Armour Piercing bites only against armour ------------------------------
random.seed(7)
def wound_rate(weapon, armour, n=4000):
    hits = 0
    for _ in range(n):
        att = Unit('a', 0, 'Fighter', weapon, dex=2)
        dfn = Unit('d', 1, 'Fighter', 'bat', armour)
        gg, _, _ = fresh_game()
        hits += gg.injure(att, dfn, True)
    return hits / n

WEAPONS['rifle+ap'] = dict(WEAPONS['rifle'])
WEAPONS['rifle+ap']['traits'] = tuple(WEAPONS['rifle']['traits']) + ('armour_piercing',)
bare_plain, bare_ap = wound_rate('rifle', 'none'), wound_rate('rifle+ap', 'none')
hvy_plain, hvy_ap = wound_rate('rifle', 'heavy'), wound_rate('rifle+ap', 'heavy')
check("AP buys nothing against an unarmoured target",
      abs(bare_plain - bare_ap) < 0.03, f"{bare_plain:.1%} vs {bare_ap:.1%}")
check("AP is worth ~+10% against Heavy armour",
      0.05 < (hvy_ap - hvy_plain) < 0.16, f"{hvy_plain:.1%} -> {hvy_ap:.1%}")

# --- every payload trait maps to a real condition ---------------------------
g, a, b = fresh_game()
# 'null_payload' is a HARNESS INSTRUMENT, not a game trait: it exists to be inert
# so that a mirror against it measures exactly -value(Pinned) — the baseline every
# ranged payload price is quoted against, and which has never been measured. It is
# exempted here rather than removed, because the check below is the one that would
# catch a real trait going inert, and that check is worth keeping sharp.
INSTRUMENTS = {'null_payload'}

unmapped = []
for trait, payload in PAYLOAD_TRAITS.items():
    if trait in INSTRUMENTS:
        continue
    _, x, y = fresh_game()
    before = (y.fire, y.bleed, y.poison, y.blind, y.shocked, y.off_balance, y.hobbled, y.pos)
    _.apply_payload(x, y, True, payload)
    after = (y.fire, y.bleed, y.poison, y.blind, y.shocked, y.off_balance, y.hobbled, y.pos)
    if before == after:
        unmapped.append(trait)
check("Every payload trait changes the target's state",
      not unmapped, f"inert: {unmapped}" if unmapped else "")

# The instrument must be inert in the state channels AND must suppress Pinned —
# if it ever stopped suppressing Pinned it would silently measure zero instead of
# -value(Pinned), which is the one failure that would look like a real result.
_, x, y = fresh_game()
_.apply_payload(x, y, True, 'none')
check("null_payload instrument suppresses Pinned on a ranged hit",
      not y.pinned, "instrument applied Pinned — it would measure 0, not -value(Pinned)")

_, x, y = fresh_game()
_.apply_payload(x, y, True, None)
check("a ranged hit with NO payload still applies Pinned (the baseline itself)",
      y.pinned, "baseline lost Pinned — the instrument's comparison arm is broken")

print("=" * 72)
print(f"{'ALL CHECKS PASS' if not FAILS else str(len(FAILS)) + ' FAILURE(S): ' + ', '.join(FAILS)}")
print("=" * 72)
if __name__ == "__main__":
    sys.exit(1 if FAILS else 0)
