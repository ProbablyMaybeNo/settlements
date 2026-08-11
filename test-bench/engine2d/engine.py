"""Settlements 2D engine — plays a full Take-a-Hold game headlessly.

Mirrors the locked core engine (same maths as crew_sim.py): core 1d10+stat>=7
(nat1 fail / nat10 pass), opposed melee ties->defender, injury 1d10+dmg-armor>=7,
Shaken -1 at 1+ Stress (not on Break), Break at 2+: 1d10+NRV-(Stress-1)>=7 ->
Bolt(2)/Broken(3)/BugOut(4+). Ranged/hazard kill = Down; melee kill = Out.
Orders issued on the issuer's own activation. Ready persists across rounds.

New vs the 1D crew sim: real (x,y) positions, true LOS + geometric cover, the
Take-a-Hold objectives with hold/contest scoring, an objective-seeking AI, and
witnesses computed by actual line of sight. Molotov carries Fire + Blast to prove
the engine can hold conditions and AoE.

STUBBED (next modules, noted so it's honest): skills are stored but not applied;
hacking / terrain-interaction / infrastructure / deployables; movement collision
(models pass through pieces); voluntary bottling; Down->Stabilize/bleed-out.
"""
import math
import random
from board import (dist, toward, has_los, has_los_3d, cover_level_3d, building_at,
                   concealing_at)
from data import WEAPONS, ARMOUR, RANKS, DEPLOYABLES, unit_cost

SIGHT = 24.0   # a witness must be within this and have LOS to feel a friendly fall
EYE = 1.0      # eye height above a fighter's feet (for 2.5D line of sight)

# --- BLKOUT-import toggles (default off = pre-import behaviour) ---------------
DODGE_ON = False    # Ready target may Dodge a shot: opposed AGI vs DEX, win = miss + reposition + Pinned
DIST_GATE = False   # movement overwatch only triggers on a Move > half MOV (short shuffles are safe)
# FIX 5 audit dial (2026-08-07): what a WON dodge buys.
#   'full'  = v1 as written — reposition up to full MOV
#   'half'  = FIX 5 proposal — reposition up to half MOV (round down)
#   'prone' = fallback — no move; dive prone (heavy cover vs ranged until its next activation)
DODGE_MOVE = 'full'

# --- Packet stealth layer (default off = pre-packet behaviour) ----------------
# Hide / Sneak / Spot / Ambush, per Packet-Design-Review §2.6. Every parameter
# below is a DIAL because the review specifies the SHAPE of these rules and not
# their numbers; balance/stealth2d.py sweeps them rather than asserting one value.
STEALTH_ON = False      # master switch for the whole layer
SNEAK_FRACTION = 0.5    # Sneak moves this fraction of MOV and keeps Hidden
SPOT_BAND = 6.0         # Spot test takes -1 per this many inches of range
AMBUSH_PAYOFF = 0       # bonus on the Ambush Injury roll (0 / 1 / 2)
AMBUSH_LETHAL = False   # an Ambush wound sends the target straight to Out, not Down
ATTACK_BACK = True      # a FAILED Ambush grants the target a free attack (the review's core risk)
HIDDEN_COVER = 3        # to-hit modifier a Hidden target imposes (Terrain.md: -3)
# The pivotal fork. The VAULT says Hidden is a -3 to be hit (still a legal target).
# The PACKET's Spot action only earns its slot if Hidden means "not a legal target
# until Spotted" — which is also what makes the review's "effectively un-targetable
# for an entire game" worry coherent. Both are implemented; stealth2d.py tests both.
HIDDEN_MODE = 'modifier'    # 'modifier' (vault, -3) | 'untargetable' (packet)
HIDDEN_HOLDS = True         # may a Hidden fighter hold/score an objective? (unruled either way)
AMBUSH_RANGE = 8.0          # max reach of an Ambush ("at melee or short range" — review §2.6)

# --- Packet §2.2: is "one payload per weapon" load-bearing? (test T5) ---------
MULTI_PAYLOAD = False       # True = a weapon delivers EVERY payload trait it carries
# --- Packet §9.3: extra activations (test T13) -------------------------------
EXTRA_ACTIVATION = False    # True = units with the 'extra_activation' skill act twice a round

# --- Goal assignment ---------------------------------------------------------
# Default (False) assigns every model its NEAREST objective at spawn. That is a
# real artefact generator: because models are spread evenly across the deploy
# band, coverage depends on CREW-SIZE PARITY. A 3-model crew lands exactly one
# model on each of the 3 objectives (perfect coverage); a 6-model crew doubles up
# on the same three; a 2-model crew leaves the centre uncontested. Measured: a
# 6-model crew loses to 5- and 3-model crews but beats 4- and 2-model ones —
# non-monotonic in crew size, which is parity, not strength.
# BALANCED_GOALS spreads models round-robin over the objectives instead. Left OFF
# by default so no existing finding silently moves.
BALANCED_GOALS = False


def d10():
    return random.randint(1, 10)


def core(mod, target=7):
    d = d10()
    if d == 1:
        return False
    if d == 10:
        return True
    return d + mod >= target


def opposed(a, b):        # ties -> defender (b)
    return d10() + a > d10() + b


# Weapon characteristic -> the condition its payload delivers (Weapons.md §2).
# A payload REPLACES the non-wounding result; it never stacks with Pinned.
PAYLOAD_TRAITS = {
    'fire': 'fire',                  # Incendiary
    'bleeding': 'bleed',             # Bleeding
    'toxic': 'poison',               # Toxic
    'blinding': 'blind',             # Blinding
    'shocking': 'shocked',           # Shocking
    'concussive': 'off_balance',     # Concussive
    'crippling': 'hobbled',          # Crippling
    'heavy_impact': 'heavy_impact',  # Heavy Impact — push 2"
    'hook': 'hook',                  # Hook — pull 1", melee only
}


class Unit:
    def __init__(self, name, side, rank, weapon, armour='none', skills=(), equip=(),
                 deployable=None, **stat):
        self.name = name
        self.tag = 'AB'[side] + '-' + name
        self.side = side
        self.rank = rank
        self.weapon = weapon
        self.armour = armour
        self.skills = tuple(skills)
        self.equip = tuple(equip)
        self.deployable = deployable
        self.stats = {k: stat.get(k, 0) for k in ('str', 'dex', 'agi', 'int', 'nrv')}
        self.base_mov = stat.get('mov', 6.0)
        self.wnd = stat.get('wnd', 1)
        self.orders = RANKS[rank]['orders']
        self.cost = unit_cost(rank, weapon, armour, equip, deployable)
        self.goal = None      # assigned objective point
        self.policy = None    # set by the crew builder (see policies.py)
        self.reset()

    def reset(self):
        self.pos = (0.0, 0.0)
        self.z = 0.0
        self.w = self.wnd
        self.stress = 0
        self.gained = 0
        self.pinned = False
        self.down = False
        self.out = False
        self.fire = False
        self.ready = False
        self.skip = False
        self.acted = False
        self.ordered = False
        self.cowed = False
        self.deployed = False
        self.prone = False          # FIX 5 'prone' dodge variant: heavy cover vs ranged until next activation
        # --- conditions (Conditions.md). No stacking: each is a flag, not a count.
        self.bleed = False          # persistent: -1 WND each End Phase
        self.poison = False         # persistent: -1 all rolls; STR 7+ each End Phase to end
        self.blind = 0              # -2 on sight rolls;  ends at the end of its next activation
        self.shocked = 0            # -2 all rolls + no React; ends at the end of its next activation
        self.off_balance = False    # no Sprint/Charge;   persists until cleared with the Move slot
        self.hobbled = False        # -2" MOV;            persists until cleared with the Move slot
        self.suppressed = False     # counts as Pinned and cannot React until the Pin clears
        # --- stealth layer (STEALTH_ON) -------------------------------------
        self.hidden = False         # -3 to be hit; lost on shooting / being spotted / ordinary Move
        self.spotted = False        # revealed this battle by an enemy Spot test
        self.ambushes = 0           # Ambush attacks made (instrumentation)
        self.ambush_fails = 0       # Ambushes that missed and drew an Attack Back
        self.rounds_hidden = 0      # rounds finished while Hidden (the un-targetable metric)
        self.times_targeted = 0     # how often an enemy actually shot at this unit
        # --- Deed / XP instrumentation (Packet §6.3-6.4, test T8) ------------
        self.kills = 0              # enemies put Out or Down by this fighter
        self.melee_kills = 0
        self.ambush_kills = 0
        self.fall_kills = 0         # killed by a shove off a ledge (terrain kill)
        self.first_blood = False
        self.odds_kills = 0         # kills made while your side was outnumbered
        self.objective_rounds = 0   # End Phases spent holding an objective
        self.claims = 0             # objectives INT-claimed (claim mode)
        self.stress_inflicted = 0

    # --- status helpers ------------------------------------------------------
    @property
    def mov(self):
        return max(1.0, self.base_mov - (2.0 if self.hobbled else 0.0))

    def shaken(self):
        return 1 if self.stress >= 1 else 0

    def penalty(self, sight=False):
        """Total negative modifier on a test. Conditions.md caps the sum at -3
        however many conditions a unit carries."""
        p = self.shaken() + (1 if self.poison else 0) + (2 if self.shocked else 0)
        if sight and self.blind:
            p += 2
        return min(p, 3)

    def can_react(self):
        return not self.shocked and not self.suppressed

    def standing(self):
        return not self.out and not self.down

    def has_gun(self):
        return WEAPONS[self.weapon]['rng'] > 0


class Deployable:
    def __init__(self, owner, spec, pos):
        self.owner = owner
        self.spec = spec
        self.pos = pos
        self.state = 'online'      # online / offline / destroyed
        self.fired = False         # reset each round

    def standing(self):
        return self.state == 'online'


class Game:
    def __init__(self, crewA, crewB, board, rounds=6, log=False, record=False, claim=False):
        self.units = crewA + crewB
        self.sides = (crewA, crewB)
        self.terrain = board['terrain']
        self.objectives = board['objectives']
        self.deploy = board['deploy']
        self.size = board['size']
        self.rounds = rounds
        self.vp = [0, 0]
        self.timeline = []       # (round, vp_a, vp_b) after each End Phase
        self.log_on = log
        self.log = []
        self.first_log = []
        self.deployables = []
        self.record = record
        self.frames = []
        self.claim_mode = claim      # objectives must be INT-claimed to score (makes INT matter)
        self.claims = {i: None for i in range(len(self.objectives))}
        self.stat = {'snap': 0, 'dodge_try': 0, 'dodge_save': 0}   # BLKOUT-import instrumentation
        self.blooded = False        # has first blood been drawn? (Deed instrumentation)

    def _spawn(self):
        for side, crew in enumerate(self.sides):
            x0, y0, x1, y1 = self.deploy[side]
            n = len(crew)
            for i, u in enumerate(crew):
                u.reset()
                # spread across the band, then assign the nearest objective
                x = x0 + (i + 0.5) * (x1 - x0) / n
                y = (y0 + y1) / 2
                u.pos = (x, y)
                if BALANCED_GOALS:
                    # round-robin over objectives ordered by proximity to this model,
                    # so coverage does not depend on crew-size parity
                    u.goal = sorted(self.objectives,
                                    key=lambda o: dist(u.pos, o))[i % len(self.objectives)]
                else:
                    u.goal = min(self.objectives, key=lambda o: dist(u.pos, o))

    def _live(self, side):
        return [u for u in self.sides[side] if not u.out]

    def _standing(self, side):
        return [u for u in self.sides[side] if u.standing()]

    def foes_of(self, u):
        return self.sides[1 - u.side]

    def allies_of(self, u):
        return self.sides[u.side]

    def note(self, msg):
        if self.log_on:
            self.log.append(msg)

    # --- resolution ----------------------------------------------------------
    def add_stress(self, u, n=1):
        u.stress += n
        u.gained += n

    def go_down(self, dfn, ranged):
        if ranged:
            dfn.down = True
        else:
            dfn.out = True
        # real witnesses: standing allies with LOS to the casualty gain Stress
        for a in self._standing(dfn.side):
            if a is not dfn and dist(a.pos, dfn.pos) <= SIGHT and has_los(a.pos, dfn.pos, self.terrain):
                self.add_stress(a, 1)

    def credit_kill(self, att, dfn, melee=False, ambush=False, fall=False):
        """Attribute a casualty for the Deed / XP instrumentation (test T8)."""
        att.kills += 1
        if len(self._standing(att.side)) < len(self._standing(1 - att.side)):
            att.odds_kills += 1          # "Against the Odds" — killed while outnumbered
        if melee:
            att.melee_kills += 1
        if ambush:
            att.ambush_kills += 1
        if fall:
            att.fall_kills += 1
        if not self.blooded:
            self.blooded = True
            att.first_blood = True

    def apply_payload(self, att, dfn, ranged, payload):
        """A payload lands IN PLACE OF the non-wounding result (Pinned / Shaken).
        Its +1 Stress is the same +1 Pinned would have given — never both
        (Conditions.md 'General rules' · Weapons.md 'Payload')."""
        if payload == 'fire':
            dfn.fire = True
        elif payload == 'bleed':
            dfn.bleed = True
        elif payload == 'poison':
            dfn.poison = True
        elif payload == 'blind':
            dfn.blind = 2                # this activation + its next
        elif payload == 'shocked':
            dfn.shocked = 2
        elif payload == 'off_balance':
            dfn.off_balance = True       # persists until cleared
        elif payload == 'hobbled':
            dfn.hobbled = True
        elif payload == 'heavy_impact':
            self.push(dfn, att.pos, 2.0)
            if ranged:
                dfn.pinned = True
        elif payload == 'hook':
            self.push(dfn, att.pos, -1.0)
        elif ranged:                      # no payload: the ordinary ranged result
            dfn.pinned = True
            if 'suppressive' in WEAPONS[att.weapon]['traits']:
                dfn.suppressed = True
        self.add_stress(dfn, 1)

    def injure(self, att, dfn, ranged, payload=None):
        arm = ARMOUR[dfn.armour]['injury']
        if 'armour_piercing' in WEAPONS[att.weapon]['traits']:
            arm = min(arm + 1, 0)          # AP reduces ARMOUR by 1 — worth nothing vs none
        mod = WEAPONS[att.weapon]['dmg'] + arm - att.penalty()
        if core(mod):
            dfn.w -= 1
            if dfn.w <= 0:
                self.go_down(dfn, ranged)
                self.credit_kill(att, dfn, melee=not ranged)
                self.note(f"  {att.tag} {'downs' if ranged else 'takes OUT'} {dfn.tag}")
            else:
                self.add_stress(dfn, 1)
            return True
        self.apply_payload(att, dfn, ranged, payload)
        return False

    def _resolve_hit(self, att, dfn):
        traits = WEAPONS[att.weapon]['traits']
        loads = [PAYLOAD_TRAITS[t] for t in traits if t in PAYLOAD_TRAITS]
        payload = loads[0] if loads else None
        targets = [dfn]
        if 'blast' in traits:
            targets += [e for e in self.foes_of(att)
                        if e is not dfn and not e.out and dist(e.pos, dfn.pos) <= 2.0]
        for t in targets:
            wounded = self.injure(att, t, True, payload=payload)
            # Packet §2.2 asks whether the one-payload cap is load-bearing. With
            # MULTI_PAYLOAD the extra payloads also land on a non-wounding hit —
            # exactly the stacking the cap exists to forbid.
            if MULTI_PAYLOAD and not wounded and len(loads) > 1 and not t.out:
                for extra in loads[1:]:
                    self.apply_payload(att, t, True, extra)

    def _wants_dodge(self, att, dfn):
        """Dodge like a player would: only when the opposed roll is a better bet
        than eating the plain to-hit roll. Losing the opposed roll is an AUTO-HIT,
        so a low-AGI fighter dodging a marksman is worse than standing still."""
        cov = self.cover(att, dfn)
        hit_mod = att.stats['dex'] - cov - att.penalty(sight=True)
        p_plain = sum(1 for d in range(2, 10) if d + hit_mod >= 7) / 10 + 0.1   # nat10 always hits
        diff = (att.stats['dex'] - att.penalty(sight=True)) - (dfn.stats['agi'] - dfn.penalty())
        p_opposed = sum(1 for a in range(1, 11) for b in range(1, 11) if a + diff > b) / 100
        return p_opposed < p_plain

    def shoot(self, att, dfn):
        rng = WEAPONS[att.weapon]['rng']
        if rng == 0 or dist(att.pos, dfn.pos) > rng:
            return False
        if not self.sight(att, dfn):
            return False
        if STEALTH_ON:
            att.hidden = False               # shooting always reveals (Terrain.md)
            dfn.times_targeted += 1
        if DODGE_ON and dfn.ready and dfn.standing() and self._wants_dodge(att, dfn):
            dfn.ready = False
            self.stat['dodge_try'] += 1
            if opposed(att.stats['dex'] - att.penalty(sight=True), dfn.stats['agi'] - dfn.penalty()):
                self._resolve_hit(att, dfn)               # attacker wins opposed roll -> auto-hit
            else:
                self.stat['dodge_save'] += 1              # dodge beats the shot: miss + dive + Pinned
                if DODGE_MOVE in ('full', 'half'):
                    d = dfn.mov if DODGE_MOVE == 'full' else float(int(dfn.mov / 2))
                    holding = dfn.goal is not None and dist(dfn.pos, dfn.goal) <= 3.0
                    if holding:
                        # a player dives without abandoning the objective: shrink the
                        # reposition until the endpoint keeps the 3" hold
                        p0 = dfn.pos
                        for _ in range(4):
                            self.move_away(dfn, att.pos, d)
                            if dist(dfn.pos, dfn.goal) <= 3.0 or d < 0.5:
                                break
                            dfn.pos = p0
                            d /= 2.0
                    else:
                        self.move_away(dfn, att.pos, d)
                else:                                     # 'prone': dive where you stand
                    dfn.prone = True
                dfn.pinned = True
                self.note(f"  {dfn.tag} dodges {att.tag}")
            return True
        cov = self.cover(att, dfn)
        if dfn.prone:
            cov = max(cov, 2)
        if core(att.stats['dex'] - cov - att.penalty(sight=True)):
            self._resolve_hit(att, dfn)
        return True

    def move_away(self, u, from_pos, d):
        dx, dy = u.pos[0] - from_pos[0], u.pos[1] - from_pos[1]
        L = math.hypot(dx, dy) or 1.0
        u.pos = (min(max(u.pos[0] + dx / L * d, 0.0), self.size),
                 min(max(u.pos[1] + dy / L * d, 0.0), self.size))

    def fight(self, att, dfn, charge=0):
        if dfn.down:
            self.injure(att, dfn, False)         # melee auto-hits a Down fighter
            return
        if opposed(att.stats['str'] + charge - att.penalty(), dfn.stats['str'] - dfn.penalty()):
            if 'knockback' in att.skills:        # skill: shove the loser 2" (can break a hold)
                self.push(dfn, att.pos, 2.0, pusher=att)
            self.injure(att, dfn, False)
        else:
            self.add_stress(att, 1)              # lost the clash: Shaken

    def push(self, u, from_pos, d, pusher=None):
        dx, dy = u.pos[0] - from_pos[0], u.pos[1] - from_pos[1]
        L = math.hypot(dx, dy) or 1.0
        u.pos = (min(max(u.pos[0] + dx / L * d, 0.0), self.size),
                 min(max(u.pos[1] + dy / L * d, 0.0), self.size))
        if u.z > 0 and building_at(u.pos, self.terrain) is None:   # shoved off a roof -> fall
            h = u.z
            u.z = 0.0
            self.note(f"  {u.tag} falls {h}\"")
            if h >= 6:                              # 6\"+ fall forces an Injury (ignoring armour)
                before = u.standing()
                self.injure_dmg(3, u, True)
                if pusher is not None and before and not u.standing():
                    self.credit_kill(pusher, u, fall=True)   # a terrain kill (Deed instrumentation)

    def reactions(self, mover):
        if STEALTH_ON and mover.hidden and HIDDEN_MODE == 'untargetable':
            return                       # you cannot snap-shoot what you cannot see
        for r in self._standing(1 - mover.side):
            if not r.ready or not r.has_gun() or not r.can_react():
                continue
            if DODGE_ON and getattr(r, 'dodge_hold', False):
                continue                     # the Ready holder chooses: this one saves it to Dodge
            if dist(r.pos, mover.pos) > WEAPONS[r.weapon]['rng']:
                continue
            if not self.sight(r, mover):
                continue
            r.ready = False
            self.stat['snap'] += 1
            self.note(f"  {r.tag} snap-shots {mover.tag}")
            self.shoot(r, mover)
            if not mover.standing():
                return

    # --- targeting / AI ------------------------------------------------------
    def best_target(self, u):
        rng = WEAPONS[u.weapon]['rng']
        seen = [e for e in self.foes_of(u) if not e.out
                and dist(u.pos, e.pos) <= rng and self.sight(u, e)]
        if STEALTH_ON and HIDDEN_MODE == 'untargetable':
            seen = [e for e in seen if not e.hidden]
        if not seen:
            return None
        # prefer a standing enemy contesting my objective, else nearest
        contesting = [e for e in seen if e.standing() and dist(e.pos, u.goal) <= 3.0]
        pool = contesting or seen
        return min(pool, key=lambda e: dist(u.pos, e.pos))

    def engaged(self, u):
        return [e for e in self.foes_of(u) if not e.out and dist(u.pos, e.pos) <= 1.0]

    def nearest_foe(self, u):
        c = [e for e in self.foes_of(u) if e.standing()] or [e for e in self.foes_of(u) if not e.out]
        return min(c, key=lambda e: dist(u.pos, e.pos)) if c else None

    def move_to(self, u, point, max_dist):
        if u.off_balance and max_dist > u.mov:
            # Off-Balance denies Sprint and Charge outright. To do either you must
            # first shed it, and shedding costs the Move slot — so this activation
            # buys the clear instead of the distance.
            u.off_balance = False
            return
        p0 = u.pos
        u.pos = toward(u.pos, point, max_dist)
        if STEALTH_ON and u.hidden:
            # An ordinary Move breaks concealment. Vanishing Point is the named
            # exception the review flags as possibly too strong: it lets a Sneaking
            # fighter cross enemy line of sight without being revealed.
            if 'vanishing_point' in u.skills and concealing_at(u.pos, self.terrain):
                pass
            else:
                u.hidden = False
        if (not DIST_GATE) or dist(p0, u.pos) > u.mov / 2.0:
            self.reactions(u)
        if u.standing():
            self.turret_watch(u)

    # --- deployables (turrets) ----------------------------------------------
    def deploy_turret(self, u):
        u.deployed = True
        spec = DEPLOYABLES[u.deployable]
        dd = d10()
        if dd == 1:
            self.note(f"  {u.tag} backfires deploying — hardware destroyed")
            return
        ok = dd == 10 or dd + u.stats['int'] + spec['build'] - u.penalty() >= 7
        d = Deployable(u.side, spec, u.pos)
        d.state = 'online' if ok else 'offline'
        self.deployables.append(d)
        self.note(f"  {u.tag} deploys a turret ({d.state})")

    def turret_watch(self, mover):
        """A turret auto-fires once/round at the first enemy that moves in range + LOS."""
        for d in self.deployables:
            if d.owner == mover.side or d.state != 'online' or d.fired:
                continue
            if d.spec['kind'] != 'turret':
                continue
            if dist(d.pos, mover.pos) > d.spec['rng'] or not has_los_3d(
                    (d.pos[0], d.pos[1], EYE), (mover.pos[0], mover.pos[1], mover.z + EYE), self.terrain):
                continue
            d.fired = True
            self.note(f"  a turret auto-fires at {mover.tag}")
            for _ in range(d.spec['shots']):
                cov = cover_level_3d(d.pos, 0.0, mover.pos, mover.z, self.terrain, target_down=mover.down)
                if core(d.spec['hit'] - cov):
                    self.injure_dmg(d.spec['dmg'], mover, True)
            if not mover.standing():
                return

    def injure_dmg(self, dmg, dfn, ranged):
        if core(dmg + ARMOUR[dfn.armour]['injury']):
            dfn.w -= 1
            if dfn.w <= 0:
                self.go_down(dfn, ranged)
            else:
                self.add_stress(dfn, 1)
            return True
        if ranged:
            dfn.pinned = True
        self.add_stress(dfn, 1)
        return False

    def enemy_turret_target(self, u):
        rng = WEAPONS[u.weapon]['rng']
        cand = [d for d in self.deployables if d.owner != u.side and d.state == 'online'
                and dist(u.pos, d.pos) <= rng
                and has_los_3d((u.pos[0], u.pos[1], u.z + EYE), (d.pos[0], d.pos[1], EYE), self.terrain)]
        return min(cand, key=lambda d: dist(u.pos, d.pos)) if cand else None

    def shoot_turret(self, u, d):
        cov = 0 if dist(u.pos, d.pos) <= 6.0 else 2       # Heavy cover unless within 6"
        if core(u.stats['dex'] - cov - u.penalty(sight=True)):
            if core(WEAPONS[u.weapon]['dmg'] - 2 - u.penalty()):   # turret Armour -2
                d.state = 'offline' if d.state == 'online' else 'destroyed'
                self.note(f"  {u.tag} {'wrecks' if d.state == 'destroyed' else 'downs'} a turret")
        return True

    def clear_movement_condition(self, u):
        """Off-Balance / Hobbled persist until the unit spends its Move slot on
        them (Conditions.md). Returns True if it spent the Move this activation."""
        if u.off_balance or u.hobbled:
            u.off_balance = False
            u.hobbled = False
            return True
        return False

    def clear_pin(self, u):
        """Spend the Move slot to shake Pinned off. Returns True if the unit may
        still use its Action. Suppressive (Weapons.md) denies that: clearing a
        Suppressed pin costs the ENTIRE activation."""
        u.pinned = False
        if u.suppressed:
            u.suppressed = False
            return False
        return True

    def take_action(self, u):
        """One Action slot (also used by Orders). Shoot / fight what's reachable."""
        eng = self.engaged(u)
        if eng:
            self.fight(u, eng[0])
            return
        if u.has_gun():
            tgt = self.best_target(u)
            if tgt and self.shoot(u, tgt):
                return
            u.ready = True                       # nothing to shoot -> bank overwatch

    def activate(self, u):
        u.acted = True
        u.prone = False                          # standing back up is part of the activation
        if not u.standing():
            self.tick_activation_conditions(u)
            return
        if u.skip:                               # Bolt / Broken lose the activation
            u.skip = False
            self.tick_activation_conditions(u)
            return
        u.policy.act(self, u)
        self.tick_activation_conditions(u)                    # the decision is the policy's; primitives are the engine's

    # --- primitives the policies compose ------------------------------------
    def los(self, a, b):
        return has_los(a, b, self.terrain)      # 2D ground LOS (melee reachability)

    def sight(self, u, e):                       # 2.5D unit-to-unit line of sight
        return has_los_3d((u.pos[0], u.pos[1], u.z + EYE),
                          (e.pos[0], e.pos[1], e.z + EYE), self.terrain)

    def cover(self, att, dfn):
        lvl = cover_level_3d(att.pos, att.z, dfn.pos, dfn.z, self.terrain, target_down=dfn.down)
        if STEALTH_ON and dfn.hidden:
            lvl = max(lvl, HIDDEN_COVER)      # Hidden REPLACES passive cover — the best single state
        return lvl

    # --- stealth layer (STEALTH_ON) ------------------------------------------
    def hide(self, u):
        """Hide Action: become Hidden if standing in Concealing terrain and no
        enemy has line of sight from within 3" (you can't vanish in someone's face)."""
        if not concealing_at(u.pos, self.terrain):
            return False
        for e in self._standing(1 - u.side):
            if dist(e.pos, u.pos) <= 3.0 and self.sight(e, u):
                return False
        u.hidden = True
        self.note(f"  {u.tag} hides")
        return True

    def sneak(self, u, point):
        """Sneak: move SNEAK_FRACTION x MOV and KEEP Hidden. The strict default —
        an ordinary Move breaks concealment, only a Sneak preserves it."""
        u.pos = toward(u.pos, point, u.mov * SNEAK_FRACTION)
        if not concealing_at(u.pos, self.terrain) and 'ghost_step' not in u.skills:
            u.hidden = False              # Ghost Step: keep Hidden across open ground
        return True

    def spot(self, u):
        """Spot Action: a DEX test against one Hidden enemy, -1 per SPOT_BAND of
        range. Reveals it for the rest of the battle (the strict, readable default)."""
        cand = [e for e in self._standing(1 - u.side) if e.hidden and self.sight(u, e)]
        if not cand:
            return False
        tgt = min(cand, key=lambda e: dist(u.pos, e.pos))
        band = int(dist(u.pos, tgt.pos) // SPOT_BAND)
        bonus = 1 if 'sharp_eyes' in u.skills else 0
        if 'counter_watch' in u.skills:
            bonus += 1
        if core(u.stats['dex'] + bonus - band - u.penalty(sight=True)):
            tgt.hidden = False
            tgt.spotted = True
            self.note(f"  {u.tag} spots {tgt.tag}")
        return True

    def ambush(self, att, dfn):
        """Ambush (§2.6): an attack made from Hidden, resolved on AGI instead of
        STR/DEX. On a miss the target gets a FREE Attack Back even if it has
        already activated — the review's load-bearing risk clause."""
        att.ambushes += 1
        att.hidden = False                       # attacking always reveals you
        melee = dist(att.pos, dfn.pos) <= 1.0
        if core(att.stats['agi'] - att.penalty()):
            self.note(f"  {att.tag} AMBUSHES {dfn.tag}")
            arm = ARMOUR[dfn.armour]['injury']
            mod = WEAPONS[att.weapon]['dmg'] + arm + AMBUSH_PAYOFF - att.penalty()
            if core(mod):
                dfn.w -= 1
                if dfn.w <= 0:
                    self.go_down(dfn, ranged=not (melee or AMBUSH_LETHAL))
                    self.credit_kill(att, dfn, melee=melee, ambush=True)
                else:
                    self.add_stress(dfn, 1)
            else:
                self.apply_payload(att, dfn, not melee, None)
        else:
            att.ambush_fails += 1
            self.note(f"  {att.tag} botches an ambush on {dfn.tag}")
            if ATTACK_BACK and dfn.standing():
                if melee:
                    self.fight(dfn, att)
                elif dfn.has_gun():
                    self.shoot(dfn, att)
        if 'return_to_shadows' in att.skills and att.standing():
            # skill: slip straight back into concealment after the strike
            if concealing_at(att.pos, self.terrain):
                att.hidden = True

    def ambush_target(self, u):
        """The best victim for an Ambush: an enemy in reach that cannot see you.
        Reach is capped at AMBUSH_RANGE — the review describes the failed ambush as
        happening 'at melee or short range', so a rifleman cannot ambush at 18"."""
        if not u.hidden:
            return None
        rng = min(max(1.0, WEAPONS[u.weapon]['rng']), AMBUSH_RANGE)
        cand = [e for e in self._standing(1 - u.side)
                if dist(u.pos, e.pos) <= rng and self.sight(u, e)]
        return min(cand, key=lambda e: dist(u.pos, e.pos)) if cand else None

    def building_at(self, point):
        return building_at(point, self.terrain)

    def ascend(self, u, b):                       # take a roof via its no-test stair/ladder
        u.z = b.height
        u.pos = (min(max(u.pos[0], b.x1 + 0.5), b.x2 - 0.5),
                 min(max(u.pos[1], b.y1 + 0.5), b.y2 - 0.5))
        self.note(f"  {u.tag} takes the roof (z={b.height})")

    def flee_point(self, u):
        foe = self.nearest_foe(u)
        if not foe:
            return u.goal or u.pos
        dx, dy = u.pos[0] - foe.pos[0], u.pos[1] - foe.pos[1]
        L = math.hypot(dx, dy) or 1.0
        return (min(max(u.pos[0] + dx / L * u.mov, 0.0), self.size),
                min(max(u.pos[1] + dy / L * u.mov, 0.0), self.size))

    def freest_objective(self, u):
        def sc(o):
            enemies = sum(1 for e in self.foes_of(u) if e.standing() and dist(e.pos, o) <= 3.0)
            return (enemies, dist(u.pos, o))
        return min(self.objectives, key=sc)

    def stare_down(self, u):                     # skill: opposed NRV -> +1 Stress + Cowed
        seen = [e for e in self.foes_of(u) if e.standing()
                and dist(u.pos, e.pos) <= 6.0 and self.sight(u, e)]
        if not seen:
            return False
        tgt = min(seen, key=lambda e: dist(u.pos, e.pos))
        if opposed(u.stats['nrv'], tgt.stats['nrv']):
            self.add_stress(tgt, 1)
            tgt.cowed = True
            self.note(f"  {u.tag} stares down {tgt.tag}")
        return True

    def issue_orders_attack(self, u):
        for _ in range(u.orders):
            pool = [a for a in self._standing(u.side) if a is not u and not a.ordered]
            ready = [a for a in pool if (a.has_gun() and not a.pinned and self.best_target(a))
                     or self.engaged(a)]
            if ready:
                pick = ready[0]
                pick.ordered = True
                self.note(f"  {u.tag} orders {pick.tag} (act)")
                self.take_action(pick)
                continue
            if 'keep_moving' in u.skills:        # skill: order a stranded ally to reposition
                far = [a for a in pool if dist(a.pos, a.goal) > 3.0]
                if far:
                    pick = min(far, key=lambda a: dist(a.pos, a.goal))
                    pick.ordered = True
                    self.note(f"  {u.tag} keeps {pick.tag} moving")
                    self.move_to(pick, pick.goal, pick.mov)
                    continue
            break

    def issue_orders_move(self, u):
        for _ in range(u.orders):
            pool = [a for a in self._standing(u.side) if a is not u and not a.ordered]
            far = [a for a in pool if dist(a.pos, a.goal) > 3.0]
            if not far:
                break
            pick = min(far, key=lambda a: dist(a.pos, a.goal))
            pick.ordered = True
            self.move_to(pick, pick.goal, pick.mov)

    def break_test(self, u):
        if not u.standing():
            return
        if u.stress >= 2:
            d = d10()
            pen = u.stress - 1 + (1 if u.cowed else 0)   # Cowed: -1 on this Break test
            if d == 10 or (d != 1 and d + u.stats['nrv'] - pen >= 7):
                u.stress = 0
            else:
                if u.stress >= 4:
                    u.out = True                 # BugOut: removed
                    self.note(f"  {u.tag} BUGS OUT")
                else:
                    u.skip = True                # Bolt / Broken
                u.stress = max(0, u.stress - 1)
        elif u.stress == 1 and u.gained == 0:
            u.stress = 0                         # sheds on a clean round
        u.cowed = False                          # Cowed clears after the Break test

    def resolve_conditions(self, u):
        """End Phase step 2 — persistent conditions, then the timed ones tick down.
        Every effect here is as written in Conditions.md; nothing is invented."""
        if u.out:
            return
        # Fire — Injury roll at +1 Damage, IGNORING armour. Persists until put out.
        if u.fire:
            self.note(f"  {u.tag} burns")
            if core(1):
                u.w -= 1
                if u.w <= 0:
                    self.go_down(u, True)
            # an unengaged fighter beats the flames out with its Action next turn
            if u.standing() and d10() >= 5:
                u.fire = False
        # Bleed — lose 1 WND outright each End Phase unless treated. At WND 1 this
        # is a two-round death clock: Down at the first tick, dead at the second.
        if u.bleed and not u.out:
            if u.down:
                u.out = True                     # Down + Bleed = bleeds out
                self.note(f"  {u.tag} bleeds out")
            else:
                u.w -= 1
                if u.w <= 0:
                    self.go_down(u, True)
                    self.note(f"  {u.tag} drops from blood loss")
            if not u.out and 'med_kit' in u.equip and core(u.stats['int']):
                u.bleed = False                  # treated: Action + INT 7+, Med-Kit cancels the -2
        # Poison — STR 7+ to shake it off
        if u.poison and core(u.stats['str']):
            u.poison = False
        # Blind and Shocked no longer clear here — they run on the activation
        # clock now (Conditions.md, 2026-08-01), ticked in tick_activation_conditions.

    def tick_activation_conditions(self, u):
        """'Ends at the end of the unit's next activation' — counted down here so it
        expires even if the unit did nothing."""
        if u.blind:
            u.blind -= 1
        if u.shocked:
            u.shocked -= 1
        # Off-Balance and Hobbled do NOT tick down — they persist until the unit
        # spends its Move slot on them (see clear_movement_condition).

    # --- objective scoring ---------------------------------------------------
    def try_claim(self, u):
        """Claim-mode: a unit at a safe, unclaimed objective spends its Action on an
        INT test to flag it. Hacker skill / Breach Kit help. Returns True if it acted."""
        if not self.claim_mode:
            return False
        for i, o in enumerate(self.objectives):
            if dist(u.pos, o) > 3.0 or self.claims[i] == u.side:
                continue
            bonus = (1 if 'hacker' in u.skills else 0) + (1 if 'breach_kit' in u.equip else 0)
            if core(u.stats['int'] + bonus - u.penalty()):
                self.claims[i] = u.side
                u.claims += 1
                self.note(f"  {u.tag} claims obj{i}")
            return True
        return False

    def score_objectives(self, rnd):
        if rnd >= 2:                             # no scoring in Round 1
            for i, o in enumerate(self.objectives):
                for u in self._standing(0) + self._standing(1):
                    if dist(u.pos, o) <= 3.0:
                        u.objective_rounds += 1  # Deed instrumentation (Courier / holder)
                def holds(side):
                    return any(dist(u.pos, o) <= 3.0 and (HIDDEN_HOLDS or not u.hidden)
                               for u in self._standing(side))
                a, b = holds(0), holds(1)
                if self.claim_mode:              # ownership IS the claim; keep a body on it to score
                    own = self.claims[i]
                    if own == 0 and a:
                        self.vp[0] += 1
                    elif own == 1 and b:
                        self.vp[1] += 1
                else:                            # positional: bodies-in-area
                    if a and not b:
                        self.vp[0] += 1
                    elif b and not a:
                        self.vp[1] += 1
        self.timeline.append((rnd, self.vp[0], self.vp[1]))

    def _snapshot(self, rnd):
        self.frames.append(dict(
            round=rnd,
            vp=list(self.vp),
            units=[dict(tag=u.tag, side=u.side, x=round(u.pos[0], 2), y=round(u.pos[1], 2),
                        z=round(u.z, 1), st=('out' if u.out else 'down' if u.down else 'ok'))
                   for u in self.units],
            turrets=[dict(x=round(d.pos[0], 2), y=round(d.pos[1], 2), side=d.owner, state=d.state)
                     for d in self.deployables],
        ))

    # --- the game loop -------------------------------------------------------
    def play(self):
        self._spawn()
        if self.record:
            self._snapshot(0)
        for rnd in range(1, self.rounds + 1):
            if not self._standing(0) or not self._standing(1):
                break
            for u in self.units:
                u.acted = False
                u.ordered = False
                u.gained = 0
            for d in self.deployables:
                d.fired = False
            # Priority: 1d10 + underdog +1
            pa = d10() + (1 if len(self._live(0)) < len(self._live(1)) else 0)
            pb = d10() + (1 if len(self._live(1)) < len(self._live(0)) else 0)
            while pa == pb:
                pa, pb = d10(), d10()
            first = 0 if pa > pb else 1
            self.first_log.append(first)
            self.note(f"Round {rnd}: side {first} has priority")
            # alternating activation
            while True:
                qa = [u for u in self._standing(0) if not u.acted]
                qb = [u for u in self._standing(1) if not u.acted]
                if not qa and not qb:
                    break
                order = (first, 1 - first)
                queues = {0: qa, 1: qb}
                for s in order:
                    q = queues[s]
                    if q:
                        self.activate(q[0])
                        q[0].acted = True
                        # Packet §9.3 — the extra ACTION is the thing the packet caps
                        # rather than prices (one drone action per activation).
                        # Deliberately take_action and not a whole second activation:
                        # a second full activation also grants a second MOVE, which
                        # this AI spends over-extending into fire, so it measured
                        # NEGATIVE and was reading the policy, not the mechanic.
                        if EXTRA_ACTIVATION and 'extra_activation' in q[0].skills \
                                and q[0].standing():
                            self.take_action(q[0])
            # End Phase: conditions -> break tests -> score
            for u in self.units:
                self.resolve_conditions(u)
            for u in self.units:
                self.break_test(u)
            if STEALTH_ON:
                for u in self.units:
                    if u.hidden and u.standing():
                        u.rounds_hidden += 1
            self.score_objectives(rnd)
            if self.record:
                self._snapshot(rnd)
        return self.result()

    def result(self):
        a, b = self.vp
        winner = 'A' if a > b else 'B' if b > a else 'draw'
        return dict(winner=winner, vp=(a, b), timeline=self.timeline,
                    alive=(len(self._standing(0)), len(self._standing(1))))
