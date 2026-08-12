"""Pluggable AI policies. A policy decides a unit's activation; the engine owns
the mechanics (shoot / fight / move / orders). Swap policies to ask design
questions — the headline one being the lone-runner degeneracy test.

  balanced  — fight for the objectives: hold yours, shoot/charge what threatens it.
  runner    — the degenerate: sprint onto the freest objective, NEVER attack, flee melee.
  hunter    — pure aggression: ignore objectives, hunt and kill the enemy crew.
"""
from board import dist

# The objective hold radius, from the scenario rules: a unit holds an objective
# when it is a standing friendly within 3" and no enemy is within 3". This was
# previously written as a bare 2.5 in five places here while every engine-side
# check used 3.0, so a model could believe it was out of position while already
# holding. One name, one value, matching the rule.
IN_POSITION = 3.0


class BalancedPolicy:
    name = 'balanced'

    def act(self, g, u):
        if u.deployable and not u.deployed:           # engineer stands up its turret first
            g.deploy_turret(u); g.issue_orders_attack(u); return
        if u.pinned:
            if g.clear_pin(u):
                g.take_action(u); g.issue_orders_attack(u)
            return
        eng = g.engaged(u)
        if eng:
            g.fight(u, eng[0]); g.issue_orders_attack(u); return
        # 1) shoot a threat — but ONLY once in position.
        #
        # This gate is the fix for a defect that made weapon range negatively
        # correlated with objective play. The shoot branch returns, so a model
        # that could see an enemy shot every activation and never walked; the
        # longer its weapon, the earlier it acquired a target and the sooner it
        # stopped advancing. Measured mean distance from its own goal at game
        # end: melee 2.49", 6" gun 1.60", 8" 3.29", 18" 7.37", 24" 9.30" —
        # against a 3" hold radius. A rifle crew scored 0.00 VP, never once
        # reaching an objective, which is why symmetric ranged mirrors drew
        # 100% of Take-a-Hold games at nil.
        #
        # AmbushPolicy already carried this fix locally ("TAKE THE GROUND
        # FIRST... without this a unit will stand at range plinking for six
        # rounds and never contest the objective"). It was found once and never
        # propagated here.
        #
        # Note the reposition branch below ALREADY moves and then shoots, so a
        # model that advances does not lose its shot — it only loses the right
        # to stand still while doing it.
        in_position = u.goal is None or dist(u.pos, u.goal) <= IN_POSITION
        if u.has_gun() and in_position:
            tgt = g.best_target(u)
            if tgt:
                g.shoot(u, tgt); g.issue_orders_attack(u); return
            et = g.enemy_turret_target(u)
            if et:
                g.shoot_turret(u, et); g.issue_orders_attack(u); return
        # 2) claim a safe, unclaimed objective in reach (claim-mode only — else a no-op)
        if g.try_claim(u):
            g.issue_orders_attack(u); return
        # 3) reposition
        if u.has_gun():
            if dist(u.pos, u.goal) > IN_POSITION:
                g.move_to(u, u.goal, u.mov)
            else:
                foe = g.nearest_foe(u)
                if foe:
                    g.move_to(u, foe.pos, u.mov)
            if u.standing():
                t2 = g.best_target(u)
                if t2:
                    g.shoot(u, t2)
                else:
                    u.ready = True
        else:
            foe = g.nearest_foe(u)
            if foe and dist(u.pos, foe.pos) <= 2 * u.mov and g.los(u.pos, foe.pos):
                g.move_to(u, foe.pos, dist(u.pos, foe.pos) - 0.9)
                if u.standing():
                    g.fight(u, foe, charge=1)
            elif 'stare_down' in u.skills and g.stare_down(u):
                goal = u.goal if dist(u.pos, u.goal) > IN_POSITION else u.pos
                g.move_to(u, goal, u.mov)
            else:
                goal = u.goal if dist(u.pos, u.goal) > IN_POSITION else (foe.pos if foe else u.goal)
                g.move_to(u, goal, 2 * u.mov)
        g.issue_orders_attack(u)


class RunnerPolicy:
    name = 'runner'

    def act(self, g, u):
        if u.pinned:
            g.clear_pin(u)                            # pinned can't reposition; lose the activation
            return
        if g.engaged(u):
            g.move_to(u, g.flee_point(u), u.mov)      # never fight — run from melee
            return
        u.goal = g.freest_objective(u)                # chase the least-contested objective
        g.move_to(u, u.goal, 2 * u.mov)               # Sprint onto it; never shoot or charge
        g.issue_orders_move(u)


class HunterPolicy:
    name = 'hunter'

    def act(self, g, u):
        if u.pinned:
            if g.clear_pin(u):
                g.take_action(u)
                g.issue_orders_attack(u)
            return
        eng = g.engaged(u)
        if eng:
            g.fight(u, eng[0])
            g.issue_orders_attack(u)
            return
        foe = g.nearest_foe(u)
        if foe is None:
            g.issue_orders_attack(u)
            return
        if u.has_gun():
            tgt = g.best_target(u)
            if tgt:
                g.shoot(u, tgt)
            else:
                g.move_to(u, foe.pos, u.mov)          # close on the enemy, ignore objectives
                if u.standing():
                    t2 = g.best_target(u)
                    if t2:
                        g.shoot(u, t2)
                    else:
                        u.ready = True
        else:
            if dist(u.pos, foe.pos) <= 2 * u.mov and g.los(u.pos, foe.pos):
                g.move_to(u, foe.pos, dist(u.pos, foe.pos) - 0.9)
                if u.standing():
                    g.fight(u, foe, charge=1)
            else:
                g.move_to(u, foe.pos, 2 * u.mov)
        g.issue_orders_attack(u)


class RoofPolicy:
    """Ranged units seize the roof of their objective building (height advantage +
    see-over LOS) and hold it; melee fighters stay on the ground like Balanced.
    The control test for 'does roof-camping dominate?'."""
    name = 'roof'

    def act(self, g, u):
        if u.deployable and not u.deployed:
            g.deploy_turret(u); g.issue_orders_attack(u); return
        if u.pinned:
            if g.clear_pin(u):
                g.take_action(u); g.issue_orders_attack(u)
            return
        eng = g.engaged(u)
        if eng:
            g.fight(u, eng[0]); g.issue_orders_attack(u); return
        if u.has_gun():
            b = g.building_at(u.goal)
            if b and u.z == 0:                        # climb onto the objective's roof
                bc = ((b.x1 + b.x2) / 2, (b.y1 + b.y2) / 2)
                if dist(u.pos, bc) <= 2.0:
                    g.ascend(u, b)
                else:
                    g.move_to(u, bc, u.mov)
                    if u.standing() and dist(u.pos, bc) <= 2.0:
                        g.ascend(u, b)
            if u.standing():
                tgt = g.best_target(u)
                if tgt:
                    g.shoot(u, tgt)
                elif u.z == 0 and dist(u.pos, u.goal) > 2.5:
                    g.move_to(u, u.goal, u.mov)
                else:
                    u.ready = True
            g.issue_orders_attack(u)
            return
        # melee: ground, like Balanced
        foe = g.nearest_foe(u)
        if foe and dist(u.pos, foe.pos) <= 2 * u.mov and g.los(u.pos, foe.pos):
            g.move_to(u, foe.pos, dist(u.pos, foe.pos) - 0.9)
            if u.standing():
                g.fight(u, foe, charge=1)
        else:
            goal = u.goal if dist(u.pos, u.goal) > 2.5 else (foe.pos if foe else u.goal)
            g.move_to(u, goal, 2 * u.mov)
        g.issue_orders_attack(u)


class AmbushPolicy:
    """ONE policy for both sides of the stealth test (Packet §2.6).

    Every unit spots, fights and holds objectives identically. The ONLY behavioural
    difference is that a unit carrying the 'stealth' skill may Hide / Sneak / Ambush.
    That is what makes this a true mirror: give the skill to one side and the delta
    is the value of the MECHANIC, not of a different playstyle. An earlier version
    of this test used two different policies and measured 99% — it was reading the
    playstyle, not the rule.
    """
    name = 'ambush'

    def act(self, g, u):
        import engine as _e
        stealthy = _e.STEALTH_ON and 'stealth' in u.skills
        if u.deployable and not u.deployed:
            g.deploy_turret(u); g.issue_orders_attack(u); return
        if u.pinned:
            if g.clear_pin(u):
                g.take_action(u); g.issue_orders_attack(u)
            return
        eng = g.engaged(u)
        # TAKE THE GROUND FIRST. Applied identically to both sides. Without this a
        # unit will stand at range plinking at a -3 Hidden target for six rounds and
        # never contest the objective — which reads as "stealth wins 97% of Holds"
        # when what actually happened is that the AI forgot to walk forward.
        if not eng and dist(u.pos, u.goal) > 3.0:
            foe = g.nearest_foe(u)
            near = foe is not None and dist(u.pos, foe.pos) <= 12.0
            if stealthy and u.hidden and near:
                g.sneak(u, u.goal)          # creeping only pays once you are close
            else:
                g.move_to(u, u.goal, u.mov)  # crossing open ground: speed beats concealment
            if u.standing():
                if stealthy and not u.hidden and g.hide(u):
                    pass
                else:
                    tgt = g.best_target(u) if u.has_gun() else None
                    if tgt:
                        g.shoot(u, tgt)
                    elif u.has_gun():
                        u.ready = True
            g.issue_orders_attack(u)
            return
        # A stealthy fighter plays the ambush line: strike from concealment if
        # something is in reach, otherwise creep, otherwise disappear. Taking this
        # line COSTS the shot it could have taken — that trade is what is measured.
        if stealthy:
            if u.hidden:
                tgt = g.ambush_target(u)
                if tgt:
                    g.ambush(u, tgt); g.issue_orders_attack(u); return
                if dist(u.pos, u.goal) > 2.5:
                    g.sneak(u, u.goal)               # creep toward the objective, stay Hidden
                    g.issue_orders_attack(u); return
            elif not eng:
                if g.hide(u):                        # vanish now, strike next activation
                    g.issue_orders_attack(u); return
                if dist(u.pos, u.goal) > 2.5:        # no concealment here — move to some
                    g.move_to(u, u.goal, u.mov)
                    if u.standing() and g.hide(u):
                        g.issue_orders_attack(u); return
        if eng:
            g.fight(u, eng[0]); g.issue_orders_attack(u); return
        if u.has_gun():
            tgt = g.best_target(u)
            if tgt:
                g.shoot(u, tgt); g.issue_orders_attack(u); return
        # nothing to shoot: hunt for a ghost, else fall back to Balanced
        if _e.STEALTH_ON and g.spot(u):
            g.issue_orders_attack(u); return
        BALANCED.act(g, u)


BALANCED = BalancedPolicy()
RUNNER = RunnerPolicy()
HUNTER = HunterPolicy()
ROOF = RoofPolicy()
AMBUSH = AmbushPolicy()
POLICIES = {'balanced': BALANCED, 'runner': RUNNER, 'hunter': HUNTER, 'roof': ROOF,
            'ambush': AMBUSH}
