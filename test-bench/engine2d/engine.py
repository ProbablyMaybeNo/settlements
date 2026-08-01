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
from board import dist, toward, has_los, has_los_3d, cover_level_3d, building_at
from data import WEAPONS, ARMOUR, RANKS, DEPLOYABLES, unit_cost

SIGHT = 24.0   # a witness must be within this and have LOS to feel a friendly fall
EYE = 1.0      # eye height above a fighter's feet (for 2.5D line of sight)

# --- BLKOUT-import toggles (default off = pre-import behaviour) ---------------
DODGE_ON = False    # Ready target may Dodge a shot: opposed AGI vs DEX, win = miss + reposition + Pinned
DIST_GATE = False   # movement overwatch only triggers on a Move > half MOV (short shuffles are safe)


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
        # --- conditions (Conditions.md). No stacking: each is a flag, not a count.
        self.bleed = False          # persistent: -1 WND each End Phase
        self.poison = False         # persistent: -1 all rolls; STR 7+ each End Phase to end
        self.blind = 0              # -2 on sight rolls;  ends at the end of its next activation
        self.shocked = 0            # -2 all rolls + no React; ends at the end of its next activation
        self.off_balance = False    # no Sprint/Charge;   persists until cleared with the Move slot
        self.hobbled = False        # -2" MOV;            persists until cleared with the Move slot
        self.suppressed = False     # counts as Pinned and cannot React until the Pin clears

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
                self.note(f"  {att.tag} {'downs' if ranged else 'takes OUT'} {dfn.tag}")
            else:
                self.add_stress(dfn, 1)
            return True
        self.apply_payload(att, dfn, ranged, payload)
        return False

    def _resolve_hit(self, att, dfn):
        traits = WEAPONS[att.weapon]['traits']
        payload = next((PAYLOAD_TRAITS[t] for t in traits if t in PAYLOAD_TRAITS), None)
        targets = [dfn]
        if 'blast' in traits:
            targets += [e for e in self.foes_of(att)
                        if e is not dfn and not e.out and dist(e.pos, dfn.pos) <= 2.0]
        for t in targets:
            self.injure(att, t, True, payload=payload)

    def _wants_dodge(self, att, dfn):
        return self.cover(att, dfn) < 2       # dodge when exposed; keep Heavy cover (shot's already hard)

    def shoot(self, att, dfn):
        rng = WEAPONS[att.weapon]['rng']
        if rng == 0 or dist(att.pos, dfn.pos) > rng:
            return False
        if not self.sight(att, dfn):
            return False
        if DODGE_ON and dfn.ready and dfn.standing() and self._wants_dodge(att, dfn):
            dfn.ready = False
            self.stat['dodge_try'] += 1
            if opposed(att.stats['dex'] - att.penalty(sight=True), dfn.stats['agi'] - dfn.penalty()):
                self._resolve_hit(att, dfn)               # attacker wins opposed roll -> auto-hit
            else:
                self.stat['dodge_save'] += 1              # dodge beats the shot: miss + dive + Pinned
                self.move_away(dfn, att.pos, dfn.mov)
                dfn.pinned = True
                self.note(f"  {dfn.tag} dodges {att.tag}")
            return True
        cov = self.cover(att, dfn)
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
                self.push(dfn, att.pos, 2.0)
            self.injure(att, dfn, False)
        else:
            self.add_stress(att, 1)              # lost the clash: Shaken

    def push(self, u, from_pos, d):
        dx, dy = u.pos[0] - from_pos[0], u.pos[1] - from_pos[1]
        L = math.hypot(dx, dy) or 1.0
        u.pos = (min(max(u.pos[0] + dx / L * d, 0.0), self.size),
                 min(max(u.pos[1] + dy / L * d, 0.0), self.size))
        if u.z > 0 and building_at(u.pos, self.terrain) is None:   # shoved off a roof -> fall
            h = u.z
            u.z = 0.0
            self.note(f"  {u.tag} falls {h}\"")
            if h >= 6:                              # 6\"+ fall forces an Injury (ignoring armour)
                self.injure_dmg(3, u, True)

    def reactions(self, mover):
        for r in self._standing(1 - mover.side):
            if not r.ready or not r.has_gun() or not r.can_react():
                continue
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
        return cover_level_3d(att.pos, att.z, dfn.pos, dfn.z, self.terrain, target_down=dfn.down)

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
                self.note(f"  {u.tag} claims obj{i}")
            return True
        return False

    def score_objectives(self, rnd):
        if rnd >= 2:                             # no scoring in Round 1
            for i, o in enumerate(self.objectives):
                a = any(dist(u.pos, o) <= 3.0 for u in self._standing(0))
                b = any(dist(u.pos, o) <= 3.0 for u in self._standing(1))
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
            # End Phase: conditions -> break tests -> score
            for u in self.units:
                self.resolve_conditions(u)
            for u in self.units:
                self.break_test(u)
            self.score_objectives(rnd)
            if self.record:
                self._snapshot(rnd)
        return self.result()

    def result(self):
        a, b = self.vp
        winner = 'A' if a > b else 'B' if b > a else 'draw'
        return dict(winner=winner, vp=(a, b), timeline=self.timeline,
                    alive=(len(self._standing(0)), len(self._standing(1))))
