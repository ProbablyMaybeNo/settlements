"""The 100-pt mirror crew "Redline" — the same list on the printed Crew Sheet.
A unit per stat, weapons chosen to exercise different mechanics.

Wired skills (affect play): Knockback (shove off a hold), Stare Down (morale),
Keep Moving (Leader repositions a stranded ally). Stubbed (no effect in the
simplified Take-a-Hold: no terminals / Hidden / objective-interaction Action):
Hacker, Sharp Eyes, Quick Hands, Ready to React (overwatch is already engine-wide).
"""
from engine import Unit
from policies import POLICIES, BALANCED, RUNNER


def redline(side, policy='balanced', lone_runner=False):
    crew = [
        Unit('Boss',    side, 'Leader',  'rifle',   dex=2, int=2, nrv=2,
             skills=('hacker', 'sharp_eyes', 'keep_moving')),
        Unit('Bruiser', side, 'Fighter', 'crowbar', str=2, skills=('knockback',)),
        Unit('Deadeye', side, 'Fighter', 'pistol',  dex=2, skills=('ready_to_react',)),
        Unit('Wire',    side, 'Fighter', 'bat',     int=2, equip=('breach_kit',), skills=('hacker',)),
        Unit('Runner',  side, 'Fighter', 'molotov', agi=2, skills=('quick_hands',)),
        Unit('Nerves',  side, 'Fighter', 'bat',     nrv=2, skills=('stare_down',)),
    ]
    pol = POLICIES[policy]
    for u in crew:
        u.policy = pol
    if lone_runner:                       # the AGI 'Runner' rushes objectives; the rest fight
        for u in crew:
            u.policy = BALANCED
        crew[4].policy = RUNNER
    return crew


def redline_v2(side):
    """Same 6 roles + weapons as Redline, but built under the V2 rank system:
    more stat points, capped by tier, so every unit spreads into a fuller line
    (a spike + real breadth) instead of one +2 in a field of zeros."""
    crew = [
        # Leader (9 pts): DEX+4 shooter, dabble hack + nerve + a little muscle
        Unit('Boss',    side, 'Leader',  'rifle',   dex=4, int=2, nrv=2, str=1,
             skills=('sharp_eyes', 'hacker', 'keep_moving')),
        # Fighters (5 pts each): one T1 spike + three +1 dabbles
        Unit('Bruiser', side, 'Fighter', 'crowbar', str=2, agi=1, dex=1, nrv=1, skills=('knockback',)),
        Unit('Deadeye', side, 'Fighter', 'pistol',  dex=2, agi=1, nrv=1, int=1, skills=('ready_to_react',)),
        Unit('Wire',    side, 'Fighter', 'bat',      int=2, dex=1, agi=1, nrv=1, equip=('breach_kit',), skills=('hacker',)),
        Unit('Runner',  side, 'Fighter', 'bat',      agi=2, str=1, dex=1, nrv=1, skills=('quick_hands',)),
        Unit('Nerves',  side, 'Fighter', 'bat',      nrv=2, str=1, agi=1, dex=1, skills=('stare_down',)),
    ]
    for u in crew:
        u.policy = BALANCED
    return crew


def redline_v2_gentle(side):
    """The middle path: looser caps let each unit keep a strong primary AND one real
    secondary (a +2, not a +1 dabble). Built for the dual demand of hack-to-claim —
    every unit can fight its role and claim (INT+2). The 'melee-hacker' made real."""
    crew = [
        Unit('Boss',    side, 'Leader',  'rifle',   dex=4, int=4, nrv=1, skills=('sharp_eyes', 'hacker', 'keep_moving')),
        Unit('Bruiser', side, 'Fighter', 'crowbar', str=2, int=2, agi=1, skills=('knockback',)),
        Unit('Deadeye', side, 'Fighter', 'pistol',  dex=2, int=2, nrv=1, skills=('ready_to_react',)),
        Unit('Wire',    side, 'Fighter', 'bat',      int=2, dex=2, agi=1, equip=('breach_kit',), skills=('hacker',)),
        Unit('Runner',  side, 'Fighter', 'bat',      agi=2, int=2, str=1, skills=('quick_hands',)),
        Unit('Nerves',  side, 'Fighter', 'bat',      nrv=2, str=2, agi=1, skills=('stare_down',)),
    ]
    for u in crew:
        u.policy = BALANCED
    return crew


def redline_v2_stacked(side):
    """Same V2 point budgets as redline_v2, but STACKED into one stat each — the
    builds the tier caps forbid. Great at one thing, zero breadth. The control for
    'do the caps (forced spread) help or hurt when the game rewards multi-tasking?'"""
    crew = [
        Unit('Boss',    side, 'Leader',  'rifle',   dex=6, int=2, nrv=1, skills=('sharp_eyes', 'hacker', 'keep_moving')),
        Unit('Bruiser', side, 'Fighter', 'crowbar', str=4, nrv=1, skills=('knockback',)),
        Unit('Deadeye', side, 'Fighter', 'pistol',  dex=4, agi=1, skills=('ready_to_react',)),
        Unit('Wire',    side, 'Fighter', 'bat',      int=4, dex=1, equip=('breach_kit',), skills=('hacker',)),
        Unit('Runner',  side, 'Fighter', 'bat',      agi=4, str=1, skills=('quick_hands',)),
        Unit('Nerves',  side, 'Fighter', 'bat',      nrv=4, str=1, skills=('stare_down',)),
    ]
    for u in crew:
        u.policy = BALANCED
    return crew


def redline_turret(side):
    """Same crew, but Wire carries an Autoturret (drops his Breach Kit) and the
    Runner drops the Molotov to fund it. 97 pts vs the plain crew's 98."""
    crew = [
        Unit('Boss',    side, 'Leader',  'rifle',   dex=2, int=2, nrv=2,
             skills=('hacker', 'sharp_eyes', 'keep_moving')),
        Unit('Bruiser', side, 'Fighter', 'crowbar', str=2, skills=('knockback',)),
        Unit('Deadeye', side, 'Fighter', 'pistol',  dex=2, skills=('ready_to_react',)),
        Unit('Wire',    side, 'Fighter', 'bat',     int=2, deployable='autoturret', skills=('hacker',)),
        Unit('Runner',  side, 'Fighter', 'bat',     agi=2, skills=('quick_hands',)),
        Unit('Nerves',  side, 'Fighter', 'bat',     nrv=2, skills=('stare_down',)),
    ]
    for u in crew:
        u.policy = BALANCED
    return crew
