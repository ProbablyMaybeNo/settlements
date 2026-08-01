"""Pluggable AI policies. A policy decides a unit's activation; the engine owns
the mechanics (shoot / fight / move / orders). Swap policies to ask design
questions — the headline one being the lone-runner degeneracy test.

  balanced  — fight for the objectives: hold yours, shoot/charge what threatens it.
  runner    — the degenerate: sprint onto the freest objective, NEVER attack, flee melee.
  hunter    — pure aggression: ignore objectives, hunt and kill the enemy crew.
"""
from board import dist


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
        # 1) shoot a threat if there is one — clears contesters off objectives
        if u.has_gun():
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
            if dist(u.pos, u.goal) > 2.5:
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
                goal = u.goal if dist(u.pos, u.goal) > 2.5 else u.pos
                g.move_to(u, goal, u.mov)
            else:
                goal = u.goal if dist(u.pos, u.goal) > 2.5 else (foe.pos if foe else u.goal)
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


BALANCED = BalancedPolicy()
RUNNER = RunnerPolicy()
HUNTER = HunterPolicy()
ROOF = RoofPolicy()
POLICIES = {'balanced': BALANCED, 'runner': RUNNER, 'hunter': HUNTER, 'roof': ROOF}
