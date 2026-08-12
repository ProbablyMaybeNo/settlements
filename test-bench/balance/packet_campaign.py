# -*- coding: utf-8 -*-
"""PACKET TESTS T9, T11, T12 — the campaign / economy questions.

  T11  §5.2 + §5.7 + §9   THE REVIEW'S #1 UNRESOLVED BET.
       The packet cuts every per-head upkeep resource and leans entirely on
       structural limits (housing, footprint, Power, storage). The review's
       objection: structural limits are ONE-TIME costs. Once you have built past
       them they stop applying pressure, whereas a per-head cost scales
       continuously with success, forever. Is Crew Rating alone a sufficient brake?

  T9   §4.3  the "special treatment" scar-removal option — how often does it get
       used if it is not hard-capped?

  T12  §5.6  the economy pacing ratios only mean something checked against a
       costed catalogue.

METHOD — two stages.

  STAGE 1 (calibration, measured on the 2.5D engine): what does a Crew Rating
  deficit actually cost you? Crews are built down from 100 points and played
  against the full-strength crew. This produces the rating->win% curve the
  campaign model needs, so the campaign is not resting on a guessed number.

  STAGE 2 (campaign Monte-Carlo): two settlements play a season. Income, hiring,
  building, casualties and Fate are modelled; the fielded crew is capped by Crew
  Rating exactly as the rules require. Upkeep is toggled.

Every economic constant is declared at the top and labelled with its source.
Where the packet gives a ratio rather than a number, the ratio is used and the
absolute is derived from the costed catalogue in test-bench/points/.
"""
import sys, os, random, statistics

ENG = r"D:\AI-Workstation\Antigravity\apps\Settlements\test-bench\engine2d"
sys.path.insert(0, ENG)
os.chdir(ENG)

import engine
# HISTORICAL NOTE, 2026-08-12. This file used to set engine.BALANCED_GOALS = True
# here, on the reasoning that the default nearest-objective assignment made
# coverage depend on crew-size parity and swamped the Rating effect. The premise
# was wrong and the flag has been deleted:
#
#   - The default assignment is OPTIMALLY balanced at every crew size 2..12. The
#     gap between the busiest and emptiest objective never exceeds one model,
#     which is the best achievable when the count is not divisible by three.
#   - BALANCED_GOALS was never better at any size and often far worse - it sent
#     ALL THREE models of a 3-model crew to one objective - because it indexed a
#     per-model sorted list, so the picks collided instead of spreading.
#   - The real cause of the non-monotonicity is that Take-a-Hold does not score
#     under symmetric play: every even-sized crew drew 100% of games at 0.00 VP
#     against a 15-VP ceiling, because holding needs no enemy within 3" and both
#     crews contest the same objectives every round.
#
# So T9 / T11 / T12 / T14 in docs/PACKET-TEST-RESULTS.md were measured with the
# collision-clustering assignment ACTIVE, on campaign crews small enough (a
# Campaign Start crew fields three models) to hit its worst case. Those findings
# need re-running before they are relied on. Full write-up:
# docs/POINTS-REBUILD-EXPLANATIONS.txt

from engine import Game, Unit
from board import take_a_hold
from policies import BALANCED

try: sys.stdout.reconfigure(encoding='utf-8')
except Exception: pass

N_CAL = int(sys.argv[1]) if len(sys.argv) > 1 else 600
N_CAMP = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
SEASON = 20          # battles per campaign

# ---------------------------------------------------------------------------
# ECONOMIC CONSTANTS — every one labelled with where it comes from.
# ---------------------------------------------------------------------------
RECRUIT_CR   = 65     # [points/ticks.py] body cost, 1000-Credit scale
FIGHTER_CR   = 135    # [POINTS-TABLE.md §3]
SPECIALIST_CR = 240   # [POINTS-TABLE.md §3]
LEADER_CR    = 375    # [POINTS-TABLE.md §3]
RATING_CAP   = 1000   # [POINTS-DECISIONS.md D1]
HQ_SLOTS     = 12     # [D10] (the vault's Structures.md says 10 — unreconciled)
BUNK_SLOTS   = 6      # [D10]
TIER1_MAT    = 100    # [GLOBAL-POINTS-SYSTEM.md structure table, ~75-135 band]

# Packet §5.6 pacing targets, used as RATIOS not absolutes:
#   a normal battle reward funds ~1 Recruit, or ~1/3 of a Tier I structure
BATTLE_CREDITS = RECRUIT_CR          # ~1 Recruit per battle
BATTLE_MATERIALS = TIER1_MAT // 3    # ~1/3 of a Tier I structure per battle
WIN_BONUS = 0.5                      # winner earns 1.5x, loser 1.0x (equal-base + bonus)


# =========================== STAGE 1 — CALIBRATION ==========================
def crew_at(points, side):
    """Build the best legal crew for a Crew Rating budget, cheapest-body-first.
    Mirrors how a player short of Rating actually fields: fewer/worse bodies."""
    roster = []
    budget = points
    if budget >= LEADER_CR:
        roster.append(('Leader', 'rifle', dict(dex=4, nrv=2))); budget -= LEADER_CR
    while budget >= FIGHTER_CR:
        roster.append(('Fighter', 'pistol', dict(dex=2))); budget -= FIGHTER_CR
    while budget >= RECRUIT_CR:
        roster.append(('Recruit', 'bat', dict(str=1))); budget -= RECRUIT_CR
    out = []
    for i, (rank, wpn, st) in enumerate(roster):
        u = Unit(f'U{i}', side, rank, wpn, 'none', **st)
        u.policy = BALANCED
        out.append(u)
    return out


def play_pair(ptsA, ptsB, n, seed=20260802):
    random.seed(seed)
    a = dr = 0
    for i in range(n):
        board = take_a_hold()
        if i % 2 == 0:
            r = Game(crew_at(ptsA, 0), crew_at(ptsB, 1), board).play()
            aw, bw = r['winner'] == 'A', r['winner'] == 'B'
        else:
            r = Game(crew_at(ptsB, 0), crew_at(ptsA, 1), board).play()
            aw, bw = r['winner'] == 'B', r['winner'] == 'A'
        a += aw
        dr += (not aw and not bw)
    return (a + 0.5 * dr) / n


print("=" * 100)
print(f"STAGE 1 - CALIBRATION: what does a Crew Rating deficit cost?  ({N_CAL} games/cell)")
print("=" * 100)
print("Both crews built by the same rule; the weaker one simply has less Rating to")
print("spend. This is the curve the campaign model needs and it is MEASURED, not assumed.\n")
print(f"  {'deficit':<12}{'A rating':>10}{'B rating':>10}{'A win%':>10}")

CURVE = {}
for frac in (1.00, 0.90, 0.80, 0.70, 0.60, 0.50):
    b = int(RATING_CAP * frac)
    w = play_pair(RATING_CAP, b, N_CAL)
    CURVE[frac] = w
    print(f"  {(1-frac)*100:>6.0f}%     {RATING_CAP:>10}{b:>10}{w*100:>9.1f}%")


def win_prob(rating_a, rating_b):
    """Interpolate the measured curve. Symmetric in the two ratings."""
    if rating_a <= 0: return 0.0
    if rating_b <= 0: return 1.0
    if rating_a >= rating_b:
        frac = max(0.5, min(1.0, rating_b / rating_a))
        lo = max(f for f in CURVE if f <= frac + 1e-9)
        hi = min(f for f in CURVE if f >= frac - 1e-9)
        if lo == hi:
            return CURVE[lo]
        t = (frac - lo) / (hi - lo)
        return CURVE[lo] + t * (CURVE[hi] - CURVE[lo])
    return 1.0 - win_prob(rating_b, rating_a)


# =========================== STAGE 2 — CAMPAIGN =============================
class Settlement:
    def __init__(self, rng):
        self.rng = rng
        self.credits = 400
        self.materials = 100
        self.structures = 4          # the four starters
        self.housing = HQ_SLOTS
        self.roster = [('Leader', 0)] + [('Fighter', 0)] * 3 + [('Recruit', 0)] * 4
        self.scars = 0
        self.treatments = 0
        self.starved_battles = 0     # battles fielded under the Rating cap

    def body_cr(self, rank, advances):
        base = {'Leader': LEADER_CR, 'Specialist': SPECIALIST_CR,
                'Fighter': FIGHTER_CR, 'Recruit': RECRUIT_CR}[rank]
        return base + 15 * advances          # [D13] veterans cost more as they Advance

    def fieldable(self):
        """Best Rating you can put on the table, capped. Sorted best-first."""
        vals = sorted((self.body_cr(r, a) for r, a in self.roster), reverse=True)
        total = 0
        for v in vals:
            if total + v > RATING_CAP:
                break
            total += v
        return total

    def upkeep_cost(self):
        return len(self.roster) * UPKEEP_PER_HEAD

    def cycle(self, won):
        mult = 1.0 + (WIN_BONUS if won else 0.0)
        self.credits += int(BATTLE_CREDITS * mult)
        self.materials += int(BATTLE_MATERIALS * mult)
        # production scales with built structures (the thing with no continuous brake)
        self.credits += 12 * max(0, self.structures - 4)
        self.materials += 8 * max(0, self.structures - 4)
        if UPKEEP_PER_HEAD:
            cost = self.upkeep_cost()
            if self.credits >= cost:
                self.credits -= cost
            else:                              # cannot feed them: they leave
                self.credits = 0
                while self.roster and self.upkeep_cost() > BATTLE_CREDITS:
                    self.roster.pop()
        # casualties -> Fate (Campaign.md table), then losses are replaced
        for _ in range(self.rng.randint(0, 2 if won else 3)):
            if len(self.roster) <= 4:
                break
            d = self.rng.randint(1, 10)
            if d == 1:
                self.roster.pop()
            elif d <= 3:
                self.scars += 1
            elif d <= 8:
                self.scars += 1
        # spend: build while there is room, else hire while there is housing
        while self.materials >= TIER1_MAT and self.structures < STRUCTURE_CAP:
            self.materials -= TIER1_MAT
            self.structures += 1
            if self.structures % 3 == 0:
                self.housing += BUNK_SLOTS
        while self.credits >= FIGHTER_CR and len(self.roster) < self.housing:
            self.credits -= FIGHTER_CR
            self.roster.append(('Fighter', 0))
        # veterans advance
        for i, (r, a) in enumerate(self.roster):
            if self.rng.random() < 0.15:
                self.roster[i] = (r, a + 1)
        # T9: scar treatment, if it is not capped, is bought whenever affordable
        if SCAR_TREATMENT and self.scars and self.credits >= SCAR_COST:
            if not TREATMENT_CAP or self.treatments < TREATMENT_CAP:
                self.credits -= SCAR_COST
                self.scars -= 1
                self.treatments += 1
        # "starved" = materially short of the cap, not merely unable to hit it
        # exactly (no legal roster sums to 1000 on the nose).
        if self.fieldable() < RATING_CAP * 0.90:
            self.starved_battles += 1


UPKEEP_PER_HEAD = 0
STRUCTURE_CAP = 10        # footprint limit: ~10 structures on a 12x36 lot [Structures.md]
SCAR_TREATMENT = True
SCAR_COST = 120
TREATMENT_CAP = 0         # 0 = uncapped (the packet's tension), else max per campaign


def run_campaign(seed):
    rng = random.Random(seed)
    a, b = Settlement(rng), Settlement(rng)
    for _ in range(SEASON):
        pa = win_prob(a.fieldable(), b.fieldable())
        won_a = rng.random() < pa
        a.cycle(won_a)
        b.cycle(not won_a)
    return a, b


def season(label, reps, **cfg):
    global UPKEEP_PER_HEAD, STRUCTURE_CAP, SCAR_TREATMENT, TREATMENT_CAP
    UPKEEP_PER_HEAD = cfg.get('upkeep', 0)
    STRUCTURE_CAP = cfg.get('struct_cap', 10)
    SCAR_TREATMENT = cfg.get('treat', True)
    TREATMENT_CAP = cfg.get('treat_cap', 0)
    gaps, rosters, wealth, starved, treats = [], [], [], [], []
    for s in range(reps):
        a, b = run_campaign(20260802 + s)
        rich, poor = (a, b) if a.fieldable() >= b.fieldable() else (b, a)
        gaps.append(rich.fieldable() - poor.fieldable())
        rosters.append(len(rich.roster) - len(poor.roster))
        wealth.append(rich.credits + rich.materials * 2)
        starved.append((a.starved_battles + b.starved_battles) / 2)
        treats.append((a.treatments + b.treatments) / 2)
    return dict(gap=statistics.mean(gaps), roster=statistics.mean(rosters),
                wealth=statistics.mean(wealth), starved=statistics.mean(starved),
                treat=statistics.mean(treats),
                gap_p90=sorted(gaps)[int(len(gaps) * 0.9)])


print("\n" + "=" * 100)
print(f"STAGE 2 - T11: DOES CUTTING PER-HEAD UPKEEP REMOVE THE ONLY CONTINUOUS BRAKE?")
print(f"({N_CAMP} campaigns x {SEASON} battles each)")
print("=" * 100)
print("'Rating gap' = how much more Crew Rating the stronger settlement can field at")
print("season end. The Crew Rating cap is 1000, so a gap of ~0 means the cap is doing")
print("the braking on its own and no upkeep is needed. 'Idle wealth' is unspendable")
print("surplus — the symptom of an economy with no sink.\n")
print(f"  {'configuration':<40}{'rating gap':>12}{'p90 gap':>10}{'roster gap':>12}"
      f"{'idle wealth':>13}{'under-cap':>11}")

for label, cfg in (
        ('packet as written (no upkeep)', dict(upkeep=0)),
        ('+ per-head upkeep 10/head', dict(upkeep=10)),
        ('+ per-head upkeep 25/head', dict(upkeep=25)),
        ('+ per-head upkeep 50/head', dict(upkeep=50)),
        ('no upkeep, tighter lot (6 structures)', dict(upkeep=0, struct_cap=6)),
        ('no upkeep, bigger lot (15 structures)', dict(upkeep=0, struct_cap=15))):
    r = season(label, N_CAMP // 10, **cfg)
    print(f"  {label:<40}{r['gap']:>12.0f}{r['gap_p90']:>10.0f}{r['roster']:>12.1f}"
          f"{r['wealth']:>13.0f}{r['starved']:>11.2f}")

print("\n" + "=" * 100)
print("T9 - HOW OFTEN IS AN UNCAPPED SCAR TREATMENT ACTUALLY BOUGHT?")
print("=" * 100)
print("§4.3 allows paying Credits/Materials to remove a Scar but the review warns it")
print("is in tension with 'scars are never bought back' unless hard-capped.\n")
print(f"  {'configuration':<40}{'treatments per campaign':>26}")
for label, cfg in (('uncapped (packet as written)', dict(treat_cap=0)),
                   ('capped at 1 per campaign', dict(treat_cap=1)),
                   ('capped at 2 per campaign', dict(treat_cap=2)),
                   ('treatment unavailable', dict(treat=False))):
    r = season(label, N_CAMP // 10, **cfg)
    print(f"  {label:<40}{r['treat']:>26.2f}")

print("\n" + "=" * 100)
print("T12 - ECONOMY PACING vs THE COSTED CATALOGUE")
print("=" * 100)
print(f"  battle reward           {BATTLE_CREDITS} Credits + {BATTLE_MATERIALS} Materials")
print(f"  Recruit body            {RECRUIT_CR} Credits   -> {BATTLE_CREDITS/RECRUIT_CR:.2f} Recruits/battle")
print(f"  Fighter body            {FIGHTER_CR} Credits   -> {FIGHTER_CR/BATTLE_CREDITS:.1f} battles/Fighter")
print(f"  Tier I structure        {TIER1_MAT} Materials -> {TIER1_MAT/BATTLE_MATERIALS:.1f} battles/structure")
print(f"  Leader body             {LEADER_CR} Credits   -> {LEADER_CR/BATTLE_CREDITS:.1f} battles/Leader")
print("\n  Packet §5.6 targets: ~1 Recruit or ~1/3 of a Tier I structure per battle;")
print("  a Tier I structure in 2-3 battles. Both hold at the catalogue's own prices.")
print("=" * 100)
