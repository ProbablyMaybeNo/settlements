# -*- coding: utf-8 -*-
"""Rules reference for the in-game TTS Notebook.

These become tabs in the notebook (top-left in TTS), so a player can read the rule
without leaving the table. Deliberately a QUICK REFERENCE, not the full ruleset:
the master note is ~1,100 lines and nobody reads that mid-turn. Each tab says
where the full version lives.

Sourced from the Obsidian vault as of 2026-08-07 — `Full Rules System v1` plus the
phase notes it rules over. If a rule changes there, change it here and re-run
build_table.py.
"""

TABS = [
    ("★ Start here", """
SETTLEMENTS — quick reference
=============================
ONE DICE MECHANIC, EVERYWHERE:

    1d10 + Stat + Modifiers  vs  7+
    Natural 1 ALWAYS fails.  Natural 10 ALWAYS succeeds.

There is no second die type anywhere in this game.

Each +1 on a stat is worth roughly +10% on that test, bounded 10-90% by the
natural-1/natural-10 floor and ceiling.

OPPOSED TESTS use the same roll for both sides. Highest total wins,
and TIES GO TO THE DEFENDER.

MODIFIER CAP: +/-3 on any single roll, however many conditions you carry.

THE THREE LEVERS, never blurred together:
  Stats   decide IF you land it.
  Weapons decide HOW BAD it is.
  Skills  decide WHAT ELSE happens.

YOU WIN ON OBJECTIVES, NEVER ON KILLS. A wiped crew cannot contest or score,
so combat is the tool and the objective is the win.

TYPE !help IN CHAT for the automated commands (tests, morale, End Phase,
terrain density, scoring).

House conventions: pre-measuring always allowed · measure base edge to base
edge · round down · every model has a 180 degree forward arc set by how you
physically placed it, no facing notches · melee ignores facing entirely ·
Engaged = within 1".
"""),

    ("Turn & activation", """
THE ROUND
=========
1. PRIORITY PHASE - both players roll 1d10, +1 if you have FEWER surviving
   models. Highest chooses to activate first or second. Ties re-roll.
   (In a RAID the defender simply takes every tie.)
2. ALTERNATING ACTIVATIONS - one unit at a time.
3. END PHASE - in this order, and the order matters:
      a. refresh Actions / Orders / Reactions
      b. resolve persistent conditions (Fire, Bleed, Poison)
      c. BREAK TESTS for every unit at 2+ Stress
      d. score objectives

THE ACTIVATION = one Move slot + one Action slot.
  MOVE    up to MOV" (baseline 6"), any direction. Never split around the
          Action. Never forced.
  ACTION  Shoot, Fight, Interact, Hide, Stabilize, Ready...  NOT a second Move.
          At most ONE ATTACK per activation.
  SPRINT  (both slots) up to 2x MOV", nothing else.
  CHARGE  (both slots) up to 2x MOV" into contact, then a free melee at +1.

ORDERS: Recruits and Fighters get none. Specialists 1, Leaders 2. An Order
grants a free Action or Reaction to the issuer or a friendly. Orders cannot
chain, are issued ONLY during the issuing unit's own activation, and each unit
may receive only ONE Order per round.

READY & REACTIONS
  Spend your Action on Ready, or receive it from an Order.
  At most ONE Ready token, persists across rounds until spent or cancelled.
  CANCELLED by taking any other Action, or by being hit by an attack, a hostile
  hack, or a terrain/hazard effect.
  A Ready unit may react ONCE, after an enemy finishes a Move or Action in the
  reactor's forward 180 degrees + true LOS.
  Triggers: a Move > half MOV ending in that arc · a finished Shoot · a
  finished Interact · a resolved Charge · a sprung visible trap.

  Snap Shot  normal ranged attack, no penalty. Resolves AFTER the enemy's
             action - so a shooter who Downs its target first denies the reply.
  Charge     Move up to MOV" into Engagement, free melee at NO bonus.
  Dodge      vs a ranged attack, any angle: opposed 1d10+AGI vs shooter's
             1d10+DEX, ties to you. Win = shot misses, move up to full MOV"
             ending out of LOS, then gain Pinned. Lose = shot hits.
  Throw · Interact/Operate · Trigger (your own Remote Detonation only)
"""),

    ("Shooting & melee", """
SHOOTING
========
1. Declare a target in range, true LOS, forward 180 degrees.
2. Measure range.
3. ATTACK ROLL: 1d10 + DEX + modifiers vs 7+.
4. Hit -> Injury roll. Miss -> nothing.

MODIFIERS: Cover Light -1 · Heavy -2 · Hidden -3.
Weapons rarely add to hit - only via a conditional trait like Accurate.

ARMOUR NEVER AFFECTS THE HIT. Cover protects against BEING HIT; armour
protects against BEING HURT.

Most ranged weapons cannot fire while Engaged. A Sidearm is the exception,
using DEX, targeting only the Engaged enemy.

MELEE
=====
Engage by moving into an enemy's 1" zone (no LOS needed), then Fight with your
Action at no bonus - or CHARGE (both slots, LOS required, 2x MOV") for a free
attack at +1.

MELEE IS OPPOSED: 1d10+STR attacker vs 1d10+STR defender.
Highest wins. TIES GO TO THE DEFENDER.
Some weapons/skills swap in AGI. Facing never applies.

The LOSER takes the Injury roll. A charged unit gets no charge bonus of its own.

DISENGAGING uses your Move slot (not the whole activation): move up to MOV"
out of the 1" zone. EVERY enemy you were Engaged with gets a free swing at -2.
You keep your Action but CANNOT CHARGE afterward.
"""),

    ("Damage & injury", """
THE INJURY ROLL
===============
    1d10 + Weapon Damage - Armour  vs  7+

PASS -> the target loses 1 WND. At 0 WND:
    DOWN            if the wound was ranged or a hazard
    OUT OF ACTION   if it was melee.  Melee is decisive - no bleed-out.

FAIL -> no wound, but the hit still tells:
    RANGED -> Pinned (+1 Stress)
    MELEE  -> +1 Stress (Shaken), stays Engaged, no Pinned

EVERY HIT DOES SOMETHING. There are no wasted hits.

WEAPON DAMAGE: +0 unarmed · +1 light · +2 medium · +3 heavy.  Cap +4.
ARMOUR: 0 none · -1 light · -2 heavy.  Reduces the Injury roll only.

EVERY UNIT HAS WND 1. Only the Tough skill (T3 STR) and Level 7 raise it.

DOWN
  Prone, alive, out of the fight. Counts as HEAVY COVER vs ranged unless in
  the open. A melee/engaged attack AUTO-HITS to finish it; ranged resolves
  normally. Must be STABILIZED by the end of its NEXT activation or it bleeds
  out.  Stabilize = Action + INT 7+ (-2 without a Med-Kit; a Medic auto-succeeds).
"""),

    ("Conditions", """
A condition is a status TOKEN. No condition is tracked in your head.

NO STACKING - reapplying refreshes duration, it never deepens the effect.
MODIFIER CAP +/-3 on any single roll, however many you carry.
Gaining a negative condition costs +1 STRESS the FIRST time only.
  EXCEPTION: Pinned and Shaken - their own +1 IS that Stress. Don't double it.

PAYLOAD RULE: a weapon characteristic that applies a condition does so INSTEAD
of the normal non-wound result, never in addition. A hit does exactly one thing.

CORE
  PINNED   ranged non-wound. No Move/Charge/Sprint/Disengage; spend Move to
           clear. May still Shoot or Interact.
  DOWN     see Damage tab. Ranged origin only.
  PRONE    knocked flat, not an injury. No Shoot/Charge/Sprint.
           Standing costs the WHOLE activation.
  HIDDEN   -3 to be hit. Earned by Hide in Concealing terrain, or gear/skill.
           LOST on moving, shooting, INTERACTING (claim/loot/hack/arm/defuse),
           or being revealed.
           You MAY hold an objective while Hidden. CLAIMING one breaks it.

CONTROL
  Suppressed (Pinned + cannot React) · Off-Balance (no Sprint/Charge, persists)
  Hobbled (-2" MOV, persists) · Blind (-2 sight rolls, ends end of next
  activation) · Shocked (-2 all rolls + cannot React) · Grappled · Snared ·
  Provoked (-1 on the first attack against anyone but the source)

PERSISTENT - resolve in the END PHASE
  FIRE    Injury roll at +1 Damage IGNORING ARMOUR each End Phase.
          An Action extinguishes it, automatically.
  BLEED   lose 1 WND each End Phase unless treated. AT WND 1 THIS IS A
          TWO-ROUND DEATH CLOCK - the harshest condition in the game.
  POISON  -1 all rolls. STR 7+ each End Phase to end it.

MARKER STATES - not conditions. No Stress, and they do NOT count toward the cap:
  Spotted · Jammed · Overloaded · Compromised · Linked
"""),

    ("Morale", """
Every hit that FAILS TO WOUND generates STRESS. That is the entire
fear/suppression system, running through one number.

1+ STRESS = SHAKEN
    Flat -1 to ALL rolls. Always on. Does not stack. No test.
    Carries into your next turn - Stress never clears on the round you gained it.

2+ STRESS = A BREAK TEST in the End Phase:

    1d10 + NRV - (Stress - 1)  vs  7+

    Shaken's -1 does NOT apply here. Do not double-count it.

FAIL MARGIN:
    by 2   BOLT     flees toward the nearest board edge, hugging cover
    by 3   BROKEN   freezes, cannot act
    by 4+  BUGOUT   routs off the board, removed from play

BugOut cannot be rallied - only PREVENTED at the moment of failure by a
specific skill.

SHEDDING: a unit at exactly 1 Stress sheds it in the End Phase, but only on a
round it took no new Stress.

BOTTLING (voluntary concession): Rounds 1-3, only a fighting withdrawal off
your own edge or an accepted surrender ends it early. ROUND 4+, a declared
bottle ends the game immediately as the opponent's win, whatever the score.
"""),

    ("Terrain (the dial)", """
TERRAIN IS THE PRIMARY WEAPON, and its density is the most powerful balance
dial in the game. Simulation measured a 66-POINT WIN-RATE SWING from density
alone - bigger than any points cost could ever produce.

    A 4-model elite crew beats a 14-model horde 81% of the time on a sparse
    board, and 15% on a crowded one. Parity sits at 9-12 features exactly.

SETUP PROCEDURE
1. DENSITY FIRST - 9 to 12 large features, at least one in EACH of the nine
   12"x12" board squares, filled in with smaller scatter until no clear firing
   lane crosses the board.  TWELVE IS A HARD CEILING.
2. Pick each piece's Type, accept/adjust its Movement and Cover, add Tags,
   mark hazards.
3. At least 2 Buildings/Ruins and real interactive pieces.
4. Check every elevated area has access.

Density is chosen AFTER lists are locked, and must never be open-ended.
Type !density in chat to check the board.

EVERY PIECE HAS THREE INDEPENDENT PROPERTIES
  MOVEMENT  Open · Difficult (double cost) · Impassable
  COVER     Open 0 · Light -1 · Heavy -2 · Hidden -3 (earned, not passive) ·
            Blocked (cannot be targeted)
  TAGS      Openable, Climbable, Searchable, Hackable, Lockable, Breachable,
            Movable, Powered, Unstable, Explosive, Barricadable
            EVERY TAG MUST BE VISIBLY MARKED. Nothing interactive is invisible.

VERTICALITY
  A ranged attacker 2"+ ABOVE the target ignores LIGHT cover from the target's
  level. Heavy still counts.
  FALLING: under 3" nothing · 3"+ Prone · 6"+ also an Injury roll at +1 Damage
  per full 2" fallen, ignoring Armour. A voluntary drop may test AGI 7+ to
  land clean.

MOVEMENT TESTS (AGI 7+, paid from the Move slot)
  Climb · Jump/Leap · Vault · Swim.  Low leap (under 2") needs no test and
  costs a flat -2" of Move. Difficult ground costs double.
"""),

    ("Scenario: Take a Hold", """
THE BOARD ON THIS TABLE
  3'x3'. Three terminals on the centreline, on heavy-cover buildings with 4"
  roofs you can perch on. Deployment in the 6" bands, about 24" apart.
  Terrain is MIRROR-SYMMETRIC about the centreline, so both deployments face
  identical ground.

  This is the exact board ~6 million simulated games were measured on.

HOW IT PLAYS
  Claim a terminal with INT 7+ (an Interact - it breaks Hidden).
  Score 1 VP per HELD terminal at each End Phase, Rounds 2-6. Ceiling 15 VP.
  Most VP after Round 6 wins.

HOLDING
  A standing friendly within 3" and NO enemy within 3".
  CONTESTED (both within 3") -> nobody holds it that round.
  A Down, Out or Broken unit cannot hold, claim or score.
  Shaken units act normally, at their -1.

  NO SCORING IN ROUND 1.

WIPE
  A crew at zero standing models can no longer contest or score; the opponent
  plays on to bank objectives. Both wiped in the same round -> whoever is ahead
  at that moment wins.

THE TWIST - roll 1d6 at setup
  1 Blackout       true LOS capped at 12" all game
  2 Live Board     one terrain hazard starts active, placed centrally
  3 Reinforcements Round 3 End Phase, each crew returns one Down model
  4 Scavengers     a neutral bonus objective dead-centre, either side may take
  5 Foul Weather   open ground is Difficult
  6 Clean          no twist

OBJECTIVES ARE INTERACTS - base contact, costs the Action, 1d10+Stat vs 7+.
  Claim/activate/connect -> INT.  Loot/search -> INT + a Searched token.
  Arm -> INT, defuse -> DEX.  Open a route -> STR/DEX/INT by lock type.
"""),

    ("Chat commands", """
Hover a model, then type in chat. These automate the bookkeeping that gets
fumbled - not the decisions.

  !help                        the command list
  !enrol <name> S A D I N [W]  make the hovered object a unit
  !sheet                       show the hovered unit's line

  !test <stat> [mods]          the core test, honouring nat 1 / nat 10
  !shoot [cover]               DEX test; cover 0/1/2/3 -> 0/-1/-2/-3
  !melee                       select TWO models: opposed STR, ties to defender
  !injury <dmg> [armour]       1d10 + Damage - Armour vs 7+

  !stress <+n|-n>              adjust Stress, auto-applies Shaken
  !cond <name> [off]           toggle a condition
  !break                       one Break test
  !endphase                    conditions -> Breaks -> shed -> score, IN ORDER

  !priority                    1d10 each, +1 to whoever has fewer models
  !round                       advance the round counter
  !density                     the 9-12 band AND the nine-square check
  !score                       objective hold/contest right now

WHY THESE AND NOT MORE: the engine automates the natural-1/natural-10 override
(which is not just d+mod>=7), Shaken NOT double-applying to Break tests, the
first-condition Stress NOT double-counting with Pinned's own, and End Phase
ordering. It does not move models, choose targets, or enforce legality.

Full rules: the Obsidian vault, `Rules System/Full Rules System v1`.
"""),
]
