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

### The three properties

Every piece is described by three independent properties. Never merge them — a piece is always all three:

|Property|Question|Values|
|---|---|---|
|Movement|How do I cross it?|Open · Difficult · Impassable|
|Cover|How hard am I to hit while using it?|Open · Light · Heavy (+ Concealing enables Hide)|
|Tags|What can I do to it?|Openable, Climbable, Searchable, Hackable… (see Terrain tags)|

- Difficult costs double movement.
- Impassable cannot be entered — unless Climbable (AGI climb) or a Breach makes a hole.
- Dangerous is an overlay, not a fourth Movement value (see Hazards).

### Cover

Cover is a negative modifier to the attacker's ranged hit roll (see [[Shooting]]):

|Cover|To-hit|
|---|---|
|Open|0|
|Light|−1|
|Heavy|−2|
|Hidden|−3|
|Blocked line of sight|cannot be targeted|

- Light / Heavy are passive properties of terrain.
- Hidden is _earned_, not passive: the Hide action while in Concealing terrain, or granted by gear/skill. Lost on moving, shooting, or being revealed.
- True line of sight, judged model's-eye: if the bulk of the target is behind solid material it's Heavy or blocked; partial obscurement by light material is Light.

### Terrain types

Type = defaults + setup duties. It tells you the usual answer for each axis when the piece hits the table — the scenario or owners may override any single axis.

|Type|What it is|Default Movement|Default Cover|Common tags|
|---|---|---|---|---|
|Building|Intact enclosed structure, 1–3 stories|Interior Open (mark cluttered rooms Difficult); walls Impassable|Light inside at windows/doorways; Heavy behind solid wall|Openable · Lockable · Searchable · Climbable (exterior) · Powered/Hackable if wired|
|Ruin|Broken structure, partial walls/floors|Difficult; gaps may need Leap|Light at stub walls; Heavy at solid remains; often Concealing|Climbable · Unstable · Searchable · Breachable|
|Scatter|Cars, dumpsters, crates, low walls|Open around; low leap over <2"|Light or Heavy by bulk|Movable · Searchable · sometimes Barricadable|
|Environmental|Water, mud, woods, slopes, pools|Difficult or Impassable|Usually Open; woods Concealing|Climbable · Dangerous overlay|
|Feature|Terminals, turrets, vents, cameras, alarms|Occupies its spot|Feature damage rules ([[Terrain Interaction#Feature damage]])|Hackable · Powered · Linked · Explosive|
|Deployed|Player-placed: barricades, traps, builds|As placed|As the piece|Barricadable · Movable · Buildable|

Building access rule (setup duty): every floor of a Building or multi-level Ruin must have at least one no-test route (stairs or ladder). Climbable walls are optional shortcuts, never the only way up — unless a scenario explicitly says so.

- Stairs — free, normal movement.
- Ladders — no test; _(optional playtest dial: −2" Move like a low leap)._
- Climb (no ladder) — AGI 7+ ([[Movement#Terrain movement]]).

### Hazards (the Dangerous overlay)

Dangerous marks any area that can hurt you. There is no separate Hazards type — Dangerous sits on top of any piece (usually Environmental, sometimes Feature or Ruin). Each Dangerous area names its hazard; effects reuse existing [[Conditions]] — never invent a new condition here.

Trigger: a fighter that ends its Move or activation inside the area suffers the hazard. (Crossing at full tilt doesn't trigger it — deep water is the exception, see Swim.)

|Hazard|Effect|
|---|---|
|Fire / burning ground|Gain Fire|
|Acid / chemical pool|Gain Poison|
|Ice / slick surface|AGI 7+ or gain Off-Balance|
|Electrified area|Gain Shocked|
|Deep water|Swim (AGI, on entering — [[Movement#Terrain movement]])|
|Dense smoke|Blind while inside; area counts as Concealing|

Forced movement (Knockback, Slam & Throw, etc.) into a Dangerous area triggers it immediately. Steadying yourself in a hazard is an NRV Interact ([[Terrain Interaction]]).

### Verticality

- Height advantage: a ranged attacker 2"+ above its target ignores Light cover from pieces at the target's level (Heavy still counts). _(single, simple bonus — no melee height mods at launch)_
- Engagement across levels: you can only be Engaged by an enemy on your own level, or within 1" including the vertical distance.
- Falling: a fighter that falls 2"+ suffers an Injury roll at +1 Damage per full 2" fallen, ignoring Armor, and lands Pinned. A voluntary drop of 2–3" may test AGI 7+ to land clean (no Injury, no Pinned). Like a Cat ([[Skill Paths]]) modifies as written.
- Fall _risk_ moments (failed climbs, Knockback off a ledge) come from [[Movement]] and skills; this section only owns what a fall _does_.

### Setup procedure

Any collection — DIY, 3D-printed, bought — plugs in the same way:

1. Pick Type for each significant piece.
2. Accept or adjust defaults for Movement and Cover (one axis may be overridden per piece; say it out loud at setup).
3. Add Tags for anything interactive; mark Dangerous areas and name their hazard.
4. Check density: the board should have multiple LOS blockers, at least 2 Buildings/Ruins, and interactive pieces (Searchable, a terminal or Feature) — a bare board is not a Settlements board.
5. Check access: every elevated area has its no-test route (stairs/ladder).

One line per piece is enough: `Ruin · Difficult · Light · Unstable, Climbable, Searchable`.

### Interact

A unit spends its Action to Interact with adjacent terrain; the stat used depends on the interaction:

| Interaction                    | Stat |
| ------------------------------ | ---- |
| Kick door · drag object · Lift | STR  |
| Pick lock · disarm · repair    | DEX  |
| Hack · Build/Deploy            | INT  |
| Scavenge                       | DEX  |
| Steady yourself in a hazard    | NRV  |

Routine Interacts auto-pass; test (7+) only when failure has a consequence. Terminals and digital control → [[Hacking]]. Full verb table → [[Terrain Interaction]].

Climb · vault · leap · swim are not Interacts — they are Move-slot maneuvers ([[Movement#Terrain movement]]):

- Obstacles under 2" — low leap: no test, −2" Move cost (flat).
- Gaps, 2"+ obstacles, climbs, and swim — AGI test vs 7+.

> [!question] Playtest dials
> 
> - Ladder cost: free vs −2" Move.
> - Fall damage: +1 Dmg per full 2" may be too soft/hard — check against 1-WND fighters.
> - Height advantage: ignoring Light cover from above may make roofs dominant — watch for camping.
> - Interior Building floors defaulting Open vs Difficult.

## Rule ledger
- [[core-004 Cover and line of sight]]
- [[adv-004 Weather and climate]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
