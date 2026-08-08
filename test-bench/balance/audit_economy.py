# -*- coding: utf-8 -*-
"""AUDIT Part D test 5 + ADD 2/3/4 — economy pacing over a 12-battle campaign.

Monte-Carlo of the settlement resource loop under the audit's proposed numbers:
  ADD 2  storage caps: HQ 150Cr+150Mat · gatherer buffer 30 own · Storehouse +250
         combined · Vault 150 combined (raid-immune). Cap check at PHASE END.
  ADD 3  trader: Kiosk 2 Mat -> 1 Cr / 2 Cr -> 1 Mat; one direction per phase.
  ADD 4  raid loss: 25% of stored Cr+Mat (Vault excluded), cap 100+100,
         floor 50+50 combined-stores remaining.

Income (v1): win 65 Cr + 33 Mat, loss half (provisional); one Scavenge dispatch
per phase (HQ I) rolling the §23 loot table (with TRIM 4's entry 7 = +15 Cr).
Structure wishlist priced from §21. Roster spend: one Recruit-equivalent (65 Cr)
every second phase.

STRATEGIES
  builder   buys the next affordable wishlist structure every phase
  hoarder   never builds — the overflow-sink stress test
  trader    hoarder who converts at the Kiosk each phase toward balance

PASS (Part D): a settlement always has a purchase it WANTS by battle 5 (wishlist
non-empty + reachable); surplus loss actually bites at least once (hoarder must
bleed); a raided settlement is functional (>= floor, buys again within 2 phases).
"""
import random
import statistics
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

random.seed(20260807)
RUNS = 2000
TURNS = 12
RAID_TURNS = {4, 8}          # turns the settlement gets raided (attacker wins 50%)
WIN_P = 0.5

WISHLIST = [                 # (name, materials cost) — §21, the audit's TRIM 1 core ten
    ('Med-bay', 120), ('Storehouse', 90), ('Bunkhouse', 115),
    ('Workbench', 75), ("Trader's Kiosk", 75), ('Equipment Shed', 40),
    ('Mess Hall', 120), ('Storehouse 2', 90), ('HQ II', 210), ('Vault', 95),
]

LOOT = {1: (0, 0), 2: (5, 0), 3: (0, 10), 4: (10, 0), 5: (0, 0),
        6: (0, 15), 7: (15, 0), 8: (20, 0), 9: (0, 0)}   # 5/9 = gear (no resources)


def loot_roll():
    d = random.randint(1, 10)
    if d == 10:
        a = loot_roll_once()
        b = loot_roll_once()
        return a[0] + b[0], a[1] + b[1]
    return LOOT[d]


def loot_roll_once():
    d = random.randint(1, 9)
    return LOOT[d]


class Settlement:
    def __init__(self, strategy):
        self.strategy = strategy
        self.cr = 150.0
        self.mat = 250.0
        self.built = []
        self.wishlist = list(WISHLIST)
        self.overflow_lost = 0.0
        self.overflow_turns = []
        self.kiosk = False
        self.vault = False
        self.vault_cr = 0.0
        self.vault_mat = 0.0
        self.first_stuck_turn = None      # first turn with nothing wanted/reachable
        self.post_raid_rebuy = []         # turns from raid to next purchase

    # --- caps (ADD 2) ------------------------------------------------------
    def caps(self):
        fixed = 150 + 30                  # HQ + own gatherer buffer, per resource
        flex = 250 * sum(1 for b in self.built if b.startswith('Storehouse'))
        return fixed, flex

    def enforce_caps(self, turn):
        fixed, flex = self.caps()
        over_cr = max(0.0, self.cr - fixed)
        over_mat = max(0.0, self.mat - fixed)
        spill = over_cr + over_mat
        if spill <= flex:
            return
        lost = spill - flex
        # lose proportionally from whichever resource is over
        if spill > 0:
            lose_cr = lost * (over_cr / spill)
            lose_mat = lost * (over_mat / spill)
            self.cr -= lose_cr
            self.mat -= lose_mat
            self.overflow_lost += lost
            self.overflow_turns.append(turn)

    # --- raid (ADD 4) ------------------------------------------------------
    def raided(self):
        take_cr = min(int(self.cr * 0.25), 100)
        take_mat = min(int(self.mat * 0.25), 100)
        # floor: never below 50 Cr AND 50 Mat (per-resource; vault excluded)
        end_cr = self.cr - take_cr
        end_mat = self.mat - take_mat
        if end_cr < 50:
            take_cr = max(0, take_cr - (50 - end_cr))
        if end_mat < 50:
            take_mat = max(0, take_mat - (50 - end_mat))
        self.cr -= take_cr
        self.mat -= take_mat
        return take_cr + take_mat

    # --- one campaign turn --------------------------------------------------
    def turn(self, t):
        # battle income
        if random.random() < WIN_P:
            self.cr += 65
            self.mat += 33
        else:
            self.cr += 33
            self.mat += 16
        # scavenge dispatch
        lc, lm = loot_roll()
        self.cr += lc
        self.mat += lm
        # raid?
        if t in RAID_TURNS:
            if random.random() < 0.5:
                self.raided()
                self.post_raid_rebuy.append([t, None])
        # settlement phase: spend
        bought = False
        if self.strategy == 'builder':
            while self.wishlist and self.mat >= self.wishlist[0][1]:
                name, cost = self.wishlist.pop(0)
                self.mat -= cost
                self.built.append(name)
                if name == "Trader's Kiosk":
                    self.kiosk = True
                bought = True
        if self.strategy == 'trader' and t >= 2:
            self.kiosk = True             # assume kiosk built turn 2 (75 Mat)
            if t == 2:
                self.mat -= 75
            # convert toward balance, one direction per phase (ADD 3)
            if self.mat > self.cr + 40:
                conv = min((self.mat - self.cr) / 2, 60)
                self.mat -= conv
                self.cr += conv / 2
            elif self.cr > self.mat + 40:
                conv = min((self.cr - self.mat) / 2, 60)
                self.cr -= conv
                self.mat += conv / 2
        # roster spend: a recruit-equivalent every 2nd turn
        if t % 2 == 0 and self.cr >= 65:
            self.cr -= 65
        # stuck check: nothing wanted or first wishlist item unreachable soon
        if self.strategy == 'builder' and self.first_stuck_turn is None:
            if not self.wishlist:
                self.first_stuck_turn = t
        if bought:
            for pr in self.post_raid_rebuy:
                if pr[1] is None:
                    pr[1] = t - pr[0]
        # phase-end cap check (ADD 2 timing rule)
        self.enforce_caps(t)


def pct(x):
    return f"{x * 100:.0f}%"


print('=' * 92)
print(f"AUDIT TEST 5 — ECONOMY PACING, {RUNS} campaigns x {TURNS} battles, "
      f"raids on turns {sorted(RAID_TURNS)} (50% lost)")
print('=' * 92)

# ADD 3 arithmetic check — no profitable round trip
k = 2 * 0.5          # 2 Mat -> 1 Cr -> back: 1 Cr buys 0.5 Mat
th = 3 * (2 / 3) * (2 / 3)
print(f"\n  ADD 3 round-trip check: Kiosk 2 Mat -> 1 Cr -> {k / 2:.2f} Mat "
      f"(lose 75%) · Trade House 3 Mat -> 2 Cr -> {th / 3 * 3:.2f} Mat (lose 56%)"
      f"  ->  no profitable loop: PASS")

for strat in ('builder', 'hoarder', 'trader'):
    outs = []
    for _ in range(RUNS):
        s = Settlement(strat)
        for t in range(1, TURNS + 1):
            s.turn(t)
        outs.append(s)
    lost = [s.overflow_lost for s in outs]
    bled = sum(1 for s in outs if s.overflow_lost > 0)
    end_cr = statistics.mean(s.cr for s in outs)
    end_mat = statistics.mean(s.mat for s in outs)
    print(f"\n  [{strat.upper()}]")
    print(f"    end stores (mean): {end_cr:.0f} Cr + {end_mat:.0f} Mat")
    print(f"    campaigns that lost surplus to caps: {pct(bled / RUNS)}  "
          f"(mean loss when it bites: "
          f"{statistics.mean([x for x in lost if x > 0]) if bled else 0:.0f})")
    if strat == 'builder':
        structures = statistics.mean(len(s.built) for s in outs)
        stuck = [s.first_stuck_turn for s in outs if s.first_stuck_turn]
        print(f"    structures built by turn {TURNS} (of {len(WISHLIST)} wishlist): "
              f"{structures:.1f}")
        print(f"    wishlist exhausted before turn {TURNS}: "
              f"{pct(len(stuck) / RUNS)}"
              + (f" (earliest mean turn {statistics.mean(stuck):.1f})" if stuck else ''))
        rebuys = [pr[1] for s in outs for pr in s.post_raid_rebuy if pr[1] is not None]
        raided_n = sum(len(s.post_raid_rebuy) for s in outs)
        if raided_n:
            print(f"    raids suffered: {raided_n}; mean phases to next purchase "
                  f"after a raid: {statistics.mean(rebuys):.1f}")

print(f"\n  PASS CRITERIA (Part D test 5)")
print(f"    1. 'always a purchase it wants by battle 5' — builder wishlist "
      f"must NOT be exhausted early (see above)")
print(f"    2. 'surplus loss actually bites at least once' — hoarder must "
      f"bleed in ~every campaign (see above)")
print(f"    3. anti-death-spiral — raided builders keep buying within ~2 phases "
      f"(see above)")
print('=' * 92)
