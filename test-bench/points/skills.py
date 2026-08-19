"""Named skills, their tier, and what a skill costs on a model.

GENERATED FROM THE VAULT 2026-08-19 by parsing the tier blocks in
`Full Rules System v1.md` (`**T1 - Good:** Name (desc) - Name (desc) ...` under
each `### Path (STAT)` heading). Regenerate rather than hand-edit: the vault is
the source of truth for which skills exist and what tier they are.

WHY THIS FILE EXISTS. Skill TIERS have been priced since the write-back
(T1 20 / T2 35 / T3 55, derived from measured atoms of comparable effect size),
but `Fighter` had no skills field, so a named skill could not be put on a model
and costed. Skills existed only as campaign Advances. That made it impossible to
playtest the thing skills most affect - a specific fighter in a specific list.

The banding is deliberately COARSE and is not reopened here: 149 skills exist and
9 are wired into the engine, so individual measurement is not achievable on any
timeline. A skill costs its tier. What table data corrects is a skill's TIER
(cheap to change, one entry) rather than its price.
"""

from __future__ import annotations

from .ticks import SKILL_TIER_CREDITS

# name -> (tier, path, governing stat)
SKILLS: dict[str, tuple[int, str, str]] = {
    'Battle Cry': (1, 'Bravery / Morale', 'NRV'),
    'Buddy Check': (1, 'Bravery / Morale', 'NRV'),
    'Count Breaths': (1, 'Bravery / Morale', 'NRV'),
    'Dig In': (1, 'Bravery / Morale', 'NRV'),
    'Drag Clear': (1, 'Bravery / Morale', 'NRV'),
    'Feed the Anger': (1, 'Bravery / Morale', 'NRV'),
    'Keep Moving': (1, 'Bravery / Morale', 'NRV'),
    'Rattle-Proof': (1, 'Bravery / Morale', 'NRV'),
    'Stare Down': (1, 'Bravery / Morale', 'NRV'),
    'Steady': (1, 'Bravery / Morale', 'NRV'),
    'Bodyguard': (1, 'Combat / Muscle', 'STR'),
    'Breakdown': (1, 'Combat / Muscle', 'STR'),
    'Deadlift': (1, 'Combat / Muscle', 'STR'),
    'Doorstop': (1, 'Combat / Muscle', 'STR'),
    'Grapple': (1, 'Combat / Muscle', 'STR'),
    'Heavy Hands': (1, 'Combat / Muscle', 'STR'),
    'Knockback': (1, 'Combat / Muscle', 'STR'),
    'Pack Mule': (1, 'Combat / Muscle', 'STR'),
    'Rooted': (1, 'Combat / Muscle', 'STR'),
    'Strong Arm': (1, 'Combat / Muscle', 'STR'),
    'Camouflage Drill': (1, 'Expertise / Knowledge', 'INT'),
    'Hacker': (1, 'Expertise / Knowledge', 'INT'),
    'Jam Signals': (1, 'Expertise / Knowledge', 'INT'),
    'Jury-Rig': (1, 'Expertise / Knowledge', 'INT'),
    'Locksmith': (1, 'Expertise / Knowledge', 'INT'),
    'Loop Camera': (1, 'Expertise / Knowledge', 'INT'),
    'Medic': (1, 'Expertise / Knowledge', 'INT'),
    'Read the Objective': (1, 'Expertise / Knowledge', 'INT'),
    'Threat Scan': (1, 'Expertise / Knowledge', 'INT'),
    'Trapper': (1, 'Expertise / Knowledge', 'INT'),
    'Break Contact': (1, 'Movement / Acrobatics', 'AGI'),
    'Leaper': (1, 'Movement / Acrobatics', 'AGI'),
    'Like a Cat': (1, 'Movement / Acrobatics', 'AGI'),
    'Low Profile': (1, 'Movement / Acrobatics', 'AGI'),
    'Quick Hands': (1, 'Movement / Acrobatics', 'AGI'),
    'Rescue Grip': (1, 'Movement / Acrobatics', 'AGI'),
    'Scramble': (1, 'Movement / Acrobatics', 'AGI'),
    'Sure-Footed': (1, 'Movement / Acrobatics', 'AGI'),
    'Vault': (1, 'Movement / Acrobatics', 'AGI'),
    'Weave': (1, 'Movement / Acrobatics', 'AGI'),
    'Bank Shot': (1, 'Shooting / Perception', 'DEX'),
    'Called Shot': (1, 'Shooting / Perception', 'DEX'),
    'Covering Fire': (1, 'Shooting / Perception', 'DEX'),
    'Crossfire': (1, 'Shooting / Perception', 'DEX'),
    'Long Barrel': (1, 'Shooting / Perception', 'DEX'),
    'Muzzle Flash': (1, 'Shooting / Perception', 'DEX'),
    'Ready to React': (1, 'Shooting / Perception', 'DEX'),
    'Sharp Eyes': (1, 'Shooting / Perception', 'DEX'),
    'Shoot and Shift': (1, 'Shooting / Perception', 'DEX'),
    'Tripwire Eye': (1, 'Shooting / Perception', 'DEX'),
    'Bloodlust': (2, 'Bravery / Morale', 'NRV'),
    'Dare Me': (2, 'Bravery / Morale', 'NRV'),
    'Fearless': (2, 'Bravery / Morale', 'NRV'),
    'Hard Case': (2, 'Bravery / Morale', 'NRV'),
    'Lead from the Front': (2, 'Bravery / Morale', 'NRV'),
    'No One Left': (2, 'Bravery / Morale', 'NRV'),
    'Rally': (2, 'Bravery / Morale', 'NRV'),
    'Snap Out of It': (2, 'Bravery / Morale', 'NRV'),
    'Take It on Me': (2, 'Bravery / Morale', 'NRV'),
    'Talk Them Down': (2, 'Bravery / Morale', 'NRV'),
    'Breach and Clear': (2, 'Combat / Muscle', 'STR'),
    'Clinch': (2, 'Combat / Muscle', 'STR'),
    'Come Along': (2, 'Combat / Muscle', 'STR'),
    'Disarm': (2, 'Combat / Muscle', 'STR'),
    "Fireman's Carry": (2, 'Combat / Muscle', 'STR'),
    'Human Shield': (2, 'Combat / Muscle', 'STR'),
    'Muscle Override': (2, 'Combat / Muscle', 'STR'),
    'Power Position': (2, 'Combat / Muscle', 'STR'),
    'Squeeze': (2, 'Combat / Muscle', 'STR'),
    'Super Slam': (2, 'Combat / Muscle', 'STR'),
    'Computer Whiz': (2, 'Expertise / Knowledge', 'INT'),
    'Counter-Hack': (2, 'Expertise / Knowledge', 'INT'),
    'Field Surgeon': (2, 'Expertise / Knowledge', 'INT'),
    'Forensic Sweep': (2, 'Expertise / Knowledge', 'INT'),
    'Lockdown': (2, 'Expertise / Knowledge', 'INT'),
    'Power Broker': (2, 'Expertise / Knowledge', 'INT'),
    'Shepherd Alarm': (2, 'Expertise / Knowledge', 'INT'),
    'Tactical Uplink': (2, 'Expertise / Knowledge', 'INT'),
    'Trap Relay': (2, 'Expertise / Knowledge', 'INT'),
    'Turret Tamer': (2, 'Expertise / Knowledge', 'INT'),
    'Double Dash': (2, 'Movement / Acrobatics', 'AGI'),
    'Feint': (2, 'Movement / Acrobatics', 'AGI'),
    'Fleet': (2, 'Movement / Acrobatics', 'AGI'),
    'Grab and Go': (2, 'Movement / Acrobatics', 'AGI'),
    'Houdini': (2, 'Movement / Acrobatics', 'AGI'),
    'Leg Sweep': (2, 'Movement / Acrobatics', 'AGI'),
    'Parkour Route': (2, 'Movement / Acrobatics', 'AGI'),
    'Sidestep': (2, 'Movement / Acrobatics', 'AGI'),
    'Slide': (2, 'Movement / Acrobatics', 'AGI'),
    'Water Walker': (2, 'Movement / Acrobatics', 'AGI'),
    'Breach Window': (2, 'Shooting / Perception', 'DEX'),
    'Calm Under Fire': (2, 'Shooting / Perception', 'DEX'),
    'Controlled Burst': (2, 'Shooting / Perception', 'DEX'),
    'I See You': (2, 'Shooting / Perception', 'DEX'),
    'Kill Lane': (2, 'Shooting / Perception', 'DEX'),
    'Last Known Position': (2, 'Shooting / Perception', 'DEX'),
    'Lookout': (2, 'Shooting / Perception', 'DEX'),
    'One in a Million': (2, 'Shooting / Perception', 'DEX'),
    'Pin Them Down': (2, 'Shooting / Perception', 'DEX'),
    'Relocation Drill': (2, 'Shooting / Perception', 'DEX'),
    'Running Read': (2, 'Shooting / Perception', 'DEX'),
    'Sniper': (2, 'Shooting / Perception', 'DEX'),
    'Clear Heads': (3, 'Bravery / Morale', 'NRV'),
    'Fanatic': (3, 'Bravery / Morale', 'NRV'),
    'Iron Will': (3, 'Bravery / Morale', 'NRV'),
    'Last Command': (3, 'Bravery / Morale', 'NRV'),
    'Master the Moment': (3, 'Bravery / Morale', 'NRV'),
    'Red Mist': (3, 'Bravery / Morale', 'NRV'),
    'Stand Your Ground': (3, 'Bravery / Morale', 'NRV'),
    'Terrify': (3, 'Bravery / Morale', 'NRV'),
    'Unbreakable': (3, 'Bravery / Morale', 'NRV'),
    'Walk into Fire': (3, 'Bravery / Morale', 'NRV'),
    'Crushing Hold': (3, 'Combat / Muscle', 'STR'),
    'Falcon Punch': (3, 'Combat / Muscle', 'STR'),
    'Juggernaut': (3, 'Combat / Muscle', 'STR'),
    'Living Barricade': (3, 'Combat / Muscle', 'STR'),
    'Structural Collapse': (3, 'Combat / Muscle', 'STR'),
    'The Muscle': (3, 'Combat / Muscle', 'STR'),
    'Too Angry to Drop': (3, 'Combat / Muscle', 'STR'),
    'Tough': (3, 'Combat / Muscle', 'STR'),
    'Wrecking Crew': (3, 'Combat / Muscle', 'STR'),
    'Blackout Protocol': (3, 'Expertise / Knowledge', 'INT'),
    'Camo King': (3, 'Expertise / Knowledge', 'INT'),
    'Fortify Objective': (3, 'Expertise / Knowledge', 'INT'),
    'Ghost the Network': (3, 'Expertise / Knowledge', 'INT'),
    'Kaboom': (3, 'Expertise / Knowledge', 'INT'),
    'Mastermind': (3, 'Expertise / Knowledge', 'INT'),
    'Minefield Conductor': (3, 'Expertise / Knowledge', 'INT'),
    'Predictive Model': (3, 'Expertise / Knowledge', 'INT'),
    'Rewrite Killbox': (3, 'Expertise / Knowledge', 'INT'),
    'Trauma Reset': (3, 'Expertise / Knowledge', 'INT'),
    'Action on the Run': (3, 'Movement / Acrobatics', 'AGI'),
    'Cornering Charge': (3, 'Movement / Acrobatics', 'AGI'),
    'Dual Wield': (3, 'Movement / Acrobatics', 'AGI'),
    'Extraction Drill': (3, 'Movement / Acrobatics', 'AGI'),
    'Ghost Blade': (3, 'Movement / Acrobatics', 'AGI'),
    'In-N-Out': (3, 'Movement / Acrobatics', 'AGI'),
    'Reversal': (3, 'Movement / Acrobatics', 'AGI'),
    'Trading Spaces': (3, 'Movement / Acrobatics', 'AGI'),
    'Vanishing Point': (3, 'Movement / Acrobatics', 'AGI'),
    'Wall Runner': (3, 'Movement / Acrobatics', 'AGI'),
    'Counter-Sniper': (3, 'Shooting / Perception', 'DEX'),
    'Dead Eye': (3, 'Shooting / Perception', 'DEX'),
    'Forward Observer': (3, 'Shooting / Perception', 'DEX'),
    'Gunslinger': (3, 'Shooting / Perception', 'DEX'),
    'Patient Overwatch': (3, 'Shooting / Perception', 'DEX'),
    'Quick Shot': (3, 'Shooting / Perception', 'DEX'),
    'Shoot the Supports': (3, 'Shooting / Perception', 'DEX'),
    'Thread the Gap': (3, 'Shooting / Perception', 'DEX'),
}

# Which tiers each rank may hold, from Full Rules System v1 sec 26 (the rank
# table). A Recruit has no tiered stat, so it can hold no skill at all.
RANK_TIER_CAPS: dict[str, dict[int, int]] = {
    "recruit": {},
    "fighter": {1: 2},
    "specialist": {1: 2, 2: 1},
    "leader": {1: 4, 2: 2, 3: 1},
}


def tier_of(skill: str) -> int:
    try:
        return SKILLS[skill][0]
    except KeyError:
        raise ValueError(f"unknown skill {skill!r}") from None


def skill_credits(skill: str) -> int:
    """A skill costs its tier band. See the module docstring for why banded."""
    return SKILL_TIER_CREDITS[tier_of(skill)]


def validate_skills(skills, rank: str) -> list[str]:
    """A rank may only hold the tiers its stat line unlocks.

    This is the gate that makes skills a RANK GATE rather than a purchase - the
    same shape as the weapon min_rank gate, and for the same reason: without it a
    Recruit could carry a T3 and the pyramid stops meaning anything.
    """
    errs = []
    caps = RANK_TIER_CAPS.get(rank)
    if caps is None:
        return [f"unknown rank {rank!r}"]
    held: dict[int, int] = {}
    for s in skills:
        if s not in SKILLS:
            errs.append(f"unknown skill {s!r}")
            continue
        t = tier_of(s)
        held[t] = held.get(t, 0) + 1
    for t, n in sorted(held.items()):
        allowed = caps.get(t, 0)
        if n > allowed:
            errs.append(
                f"{rank} holds {n}x T{t} skill(s), cap is {allowed}"
                + (" (a Recruit has no tiered stat and so no skills)"
                   if rank == "recruit" else ""))
    return errs
