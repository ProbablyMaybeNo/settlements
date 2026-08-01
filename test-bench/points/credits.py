"""Credits and Crew Rating — one number, two jobs.

THE RULE  (ruled 2026-08-01, POINTS-DECISIONS D24-D26)

    Credits      the currency. Everything in the game has a Credit cost. You
                 spend Credits to hire fighters, buy weapons, armour and kit.
    Crew Rating  the sum of the Credit costs of the crew you FIELD. The battle
                 gate; the scenario sets the cap (standard 1000).

    A unit's Credit cost IS its Crew Rating contribution. There is no second
    number, no conversion, and no separate fielding currency.

WHY THIS IS WRITTEN DOWN. A two-number design was floated (a Credit price for
acquisition, a separate Rating for the table, linked by an availability band) and
REJECTED: it means every unit has to be costed twice through two systems, which
is a headache at the table for no gain. The one-number rule is the older and
better answer, and it is what `POINTS-DECISIONS` D3/D5 always said.

    "Goods" was the old name for Credits, and it is retired — it read as cargo,
    not money. "points", "crew-points", "battle rating" and "fielding points"
    are all retired too; they were four names for this one number.

WHAT STASHED GEAR COSTS. Nothing, against Rating. You paid Credits to own it;
it only occupies Rating on a fighter you actually field (D4).
"""

from __future__ import annotations

from .units import fielded_cost


def crew_rating(fighters) -> int:
    """Crew Rating = the Credit cost of everything fielded.

    `fighters` is any iterable of things exposing a Credit cost — either an int,
    or an object the units module can cost.
    """
    total = 0
    for f in fighters:
        total += f if isinstance(f, int) else fielded_cost(f)
    return total


def legal(fighters, cap: int = 1000) -> bool:
    """A crew is legal when its Rating is inside the scenario's cap."""
    return crew_rating(fighters) <= cap


def headroom(fighters, cap: int = 1000) -> int:
    """Credits still spendable against the cap."""
    return cap - crew_rating(fighters)
