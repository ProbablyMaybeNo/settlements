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

# SPRINT THRESHOLD. Beyond one Move plus the hold radius, running beats standing.
#
# Sprint is "both slots, up to 2x MOV, nothing else - no Shoot, no Ready" (Full
# Rules System v1 sec 115). So it is a real trade, not free movement: a sprinting
# model gives up its attack AND its Interact for the turn.
#
# The threshold is `u.mov + IN_POSITION` rather than a constant, because Fleet
# raises MOV to 8" and the rule should follow the stat rather than a number that
# happens to match the baseline. Inside that distance an ordinary Move already
# puts the model in position with its Action still free - which is what you need,
# because you cannot Sprint and Interact in the same activation. Outside it, a
# 6" walk while the objective sits 20" away is how a crew never arrives.
def sprint_threshold(u):
    return u.mov + IN_POSITION


# A DENIED SPRINT SPENDS NOTHING — ruled 2026-08-13.
#
# Off-Balance denies Sprint and Charge outright. The ruling is that the denied
# action never legally occurs, so there is nothing to have spent: the condition
# does NOT shed. Pinned is not a counter-example — the rules say directly that
# clearing Pinned costs the Move slot, which is a deliberate stated cost, not a
# general principle that transfers to every denied action. Nothing grants a
# denied Sprint equivalent behaviour, and inferring it would let a condition
# shed itself via an action that was never legal in the first place.
#
# So the POLICY must not ask for a sprint it cannot have. Asking is the defect:
# `move_to(u, goal, 2 * u.mov)` on an Off-Balance model reaches engine.py's
# denial branch, which spends the Move and clears the condition. That branch is
# what the sprint fix accidentally started reaching, and it broke the standing
# invariant "Off-Balance PERSISTS until something sheds it".
#
# An Off-Balance model therefore falls through to an ordinary Move (<= MOV),
# which is legal, keeps its Action, and leaves the condition where it is.
def can_sprint(u):
    return not u.off_balance


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

        # 1) TAKE THE OBJECTIVE ACTION FIRST, ahead of shooting.
        #
        # This ordering was the other half of the arrival defect, and it hid
        # behind the first half: once models could actually REACH an objective,
        # they stood on it and shot instead of using it. A uniform rifle crew
        # arrived at 0.74" from the enemy building - well inside the 3" reach -
        # and recorded ZERO charges armed across every game, because the shoot
        # branch above returned before try_claim was ever consulted.
        #
        # The ruleset is unambiguous about which matters: you win on objectives
        # and never on kills (sec 1, sec 12.7). A model in base contact with the
        # thing it came for should use it. Shooting remains available on every
        # activation where there is nothing to interact with, which is most of
        # them - try_claim returns False unless an interaction is actually in
        # reach, so this reorders a rare branch ahead of a common one rather than
        # trading one away.
        if g.try_claim(u):
            g.issue_orders_attack(u); return

        # 2) shoot a threat — but ONLY once in position (see the note above).
        if u.has_gun() and in_position:
            tgt = g.best_target(u)
            if tgt:
                g.shoot(u, tgt); g.issue_orders_attack(u); return
            et = g.enemy_turret_target(u)
            if et:
                g.shoot_turret(u, et); g.issue_orders_attack(u); return
        # 3) reposition
        if u.has_gun():
            # 3a) SPRINT if the objective is genuinely far.
            #
            # This is the second half of the advance/shoot fix. That one stopped a
            # model shooting INSTEAD of advancing; this one stops it strolling.
            # BalancedPolicy moved a gunner 6" and spent the Action shooting, so a
            # crew closed ~3"/round net against objectives ~26" away and simply
            # never arrived: Sabotage drew 99.3% of games at 0.03 interactions.
            #
            # The ruleset's own scoring clock assumes Sprint ("earliest arm
            # ~Round 2-3 (cross + reach)" is only reachable at 12"/round), so this
            # is reaching a legal action the AI already had, NOT a new heuristic.
            # Measured: arrival 20.4% -> 72.3%, interactions 0.03 -> 6.07, draws
            # 99.3% -> 22.5%.
            #
            # Deliberately NOT an expected-value model comparing a shot against
            # ground gained. Every heuristic is new decision surface with its own
            # untested bias, and the defect being fixed is simply that a legal
            # action was never taken.
            #
            # It stops at sprint_threshold rather than running all the way in,
            # because Sprint consumes the Action slot: a model that sprints ONTO
            # an objective cannot claim, arm or loot it that turn. Arriving faster
            # and never interacting is the same bug wearing a different face.
            # A "...and only when there is nothing to shoot" condition was TRIED
            # AND REJECTED on measurement. It sounded right - Sprint's cost is the
            # attack, so pay it only when the attack is worthless - but it cost
            # the arrival the fix exists to deliver (Sabotage mean distance to
            # goal 2.50" -> 7.80", interactions 6.07 -> 0.02) WITHOUT removing the
            # overcorrection it was meant to remove (Raid/Armoured 40.4% -> 41.5%,
            # unchanged). It bought nothing and gave back everything.
            #
            # KNOWN RESIDUAL, measured and left in place rather than tuned away:
            # an Armoured crew on Raid wins ~41% against a non-sprinting mirror.
            # The mechanism is real - a crew that runs into open ground gets shot
            # by one that stands still - and the correct fix is an expected-value
            # comparison between ground gained and the shot forgone. That is new
            # decision surface with its own untested bias, which is precisely what
            # this fix was told not to build. All measurements use SYMMETRIC
            # mirrors where both sides carry the same policy, so the weakness
            # applies equally to both arms and does not create an A-vs-B skew.
            if can_sprint(u) and dist(u.pos, u.goal) > sprint_threshold(u):
                g.move_to(u, u.goal, 2 * u.mov)   # both slots; no shot this turn
                g.issue_orders_attack(u)          # Orders are a rank resource, not the Action slot
                return
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
            # Off-Balance denies Charge on the same terms it denies Sprint, so an
            # Off-Balance melee model reaches only one Move and never asks the
            # engine for the denial branch. Pre-existing, not part of the sprint
            # fix — but the same ruling covers it, so it is corrected here rather
            # than left as a second live instance of the defect just fixed.
            reach = 2 * u.mov if can_sprint(u) else u.mov
            foe = g.nearest_foe(u)
            if foe and dist(u.pos, foe.pos) <= reach and g.los(u.pos, foe.pos):
                g.move_to(u, foe.pos, dist(u.pos, foe.pos) - 0.9)
                if u.standing():
                    g.fight(u, foe, charge=1)
            elif 'stare_down' in u.skills and g.stare_down(u):
                goal = u.goal if dist(u.pos, u.goal) > IN_POSITION else u.pos
                g.move_to(u, goal, u.mov)
            else:
                goal = u.goal if dist(u.pos, u.goal) > IN_POSITION else (foe.pos if foe else u.goal)
                g.move_to(u, goal, reach)
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
        # Gated for the same reason BalancedPolicy is: a denied Sprint spends
        # nothing, so asking for one while Off-Balance now moves the model 0" and
        # it would sit there for the rest of the game — nothing in this engine
        # ever spends the Move to clear the condition. Unmeasured today, but an
        # unmeasured policy is exactly where a defect waits.
        g.move_to(u, u.goal, 2 * u.mov if can_sprint(u) else u.mov)
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
