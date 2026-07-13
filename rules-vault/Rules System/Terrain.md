---
type: rule-phase
phase: "08"
stage: S3 Battle Layer
status: Drafted
build_order: 12
depends_on: ["Movement"]
feeds_into: ["Terrain Interaction", "Hacking", "Scenarios", "Edge Cases"]
tags: [settlements/phase, settlements/stage/s3]
---
# 08 · Terrain
> **S3 Battle Layer** · status **Drafted** · build order **12**

**Depends on:** [[Movement]]
**Feeds into:** [[Terrain Interaction]], [[Hacking]], [[Scenarios]], [[Edge Cases]]
**Raw dependency (from Notion):** Movement

## Focus
Your core pillar — terrain categories, cover, LOS, hazards, verticality. This is the section that makes Settlements Settlements.

The Rules column should nail down:
- A terrain category system (light/heavy/impassable, cover levels) that classifies ANY piece a player owns — DIY, 3D-printed, or bought.
- Cover and line-of-sight rules: full vs partial cover, obscuring, how blocking is judged.
- Hazard terrain (fire, water, rubble, height) and its effects on units.
- Verticality/elevation: ranged and melee benefits of height, plus fall risk.
- A setup procedure so mixed terrain collections all plug into the same rules.
- The interactive-terrain hooks that deliver the headline promise: no two battles the same.

## Working rules / decisions

Terrain is the primary weapon — the core rules stay simple so the *battlefield* carries the depth.

### Cover
Cover is a negative modifier to the attacker's ranged hit roll (see [[Shooting]]):

| Cover | To-hit |
|---|:---:|
| Open | 0 |
| Light | −1 |
| Heavy | −2 |
| **Hidden** | **−3** |
| Blocked line of sight | cannot be targeted |

- **Light / Heavy** are passive properties of terrain.
- **Hidden** is *earned*, not passive: the **Hide** action while in **Concealing** terrain, or granted by gear/skill. Lost on moving, shooting, or being revealed.

### Terrain tags
Every significant piece carries tags that define what can be done to it:
`Openable · Lockable · Barricadable · Breachable · Hackable · Powered · Flammable · Searchable · Climbable · Unstable · Concealing · Explosive · Loud · Movable · Buildable`

### Interact
A unit spends its **Action** to **Interact** with adjacent terrain; the **stat used depends on the interaction**:

| Interaction | Stat |
|---|:---:|
| Kick door · drag object · Lift | STR |
| Pick lock · disarm mechanical trap | DEX |
| Hack keypad · power · camera | INT |
| Search | INT |
| Steady yourself in a hazard | NRV |

Routine Interacts auto-pass; **test (7+) only when failure has a consequence.** Terminals and digital control → [[Hacking]].

**Climb · vault · leap · swim** are **not** Interacts — they are **Move-slot** maneuvers. Full rules in [[Movement#Terrain movement]].

- Obstacles **under 2"** — **low leap**: no test, **−2"** Move cost (flat).
- Gaps, **2"+** obstacles, climbs, and swim — **AGI** test vs **7+**.
## Rule ledger
- [[core-004 Cover and line of sight]]
- [[adv-004 Weather and climate]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
