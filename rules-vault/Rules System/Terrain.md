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

^tbl-the-three-properties

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

^tbl-cover

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

^tbl-terrain-types

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

^tbl-hazards-the-dangerous-overlay

Forced movement (Knockback, Slam & Throw, etc.) into a Dangerous area triggers it immediately. Steadying yourself in a hazard is an NRV Interact ([[Terrain Interaction]]).

### Verticality

- Height advantage: a ranged attacker 2"+ above its target ignores Light cover from pieces at the target's level (Heavy still counts). _(single, simple bonus — no melee height mods at launch)_
- Engagement across levels: you can only be Engaged by an enemy on your own level, or within 1" including the vertical distance.
- **Falling.** A fall under **3"** has no effect. **3"+** lands the fighter **Prone**. **6"+** also forces an **Injury roll** at **+1 Damage per full 2" fallen**, ignoring Armor. A **voluntary** drop may test **AGI 7+** to land clean (avoid Prone); a 6"+ fall still rolls Injury on a fail. Like a Cat ([[Skill Paths]]) modifies as written.
- Fall _risk_ moments (failed climbs, Knockback off a ledge) come from [[Movement]] and skills; this section only owns what a fall _does_.

### Setup procedure

Any collection — DIY, 3D-printed, bought — plugs in the same way:

1. **Density first — 9 to 12 large features.** Divide the 3'×3' into nine **12"×12"** squares. Place **at least one large feature per square** (Building, Ruin, or a substantial Scatter cluster), then fill the gaps with smaller scatter until no clear firing lane crosses the board. **Twelve is the ceiling.**
2. Pick Type for each significant piece.
3. Accept or adjust defaults for Movement and Cover (one axis may be overridden per piece; say it out loud at setup).
4. Add Tags for anything interactive; mark Dangerous areas and name their hazard.
5. Check the board has at least 2 Buildings/Ruins and real interactive pieces (Searchable, a terminal or Feature) — a bare board is not a Settlements board.
6. Check access: every elevated area has its no-test route (stairs/ladder).

#### Settlement boards — the same procedure, one square-set pre-filled
When a battle is fought at someone's settlement, the defender's layout supplies part of the board and **the density band is unchanged**.

1. The settlement is a **12" × 36"** strip on the defender's board edge — exactly the **back three 12"×12" squares** of the nine above ([[Structures#The settlement canvas]]).
2. Those three squares are already filled: the defender's placed structures **are** their large features. Each declares its one-line profile from the settlement sheet.
3. Fill the attacker's remaining **six** squares with neutral terrain as normal, until the board totals **9–12** large features.
4. Over-filled? Bench structures down to the ceiling exactly as you would neutral scatter. **The band wins over the layout, always.**

Because the settlement fits inside one board there is **no window to pick** — a raid uses all of it, and the attacker crosses ~24" of neutral ground to reach it.

> [!info] A settlement never buys board advantage
> A developed settlement changes *what* fills those three squares, never *how many* features the board has. Structures granting deploy-rights (turret hardpoints and the like) still cost crew-points and still sit inside the band — see [[Structures#Design contract — the five rules that keep this honest|the structure contract]] and [[Deployables]].

One line per piece is enough: `Ruin · Difficult · Light · Unstable, Climbable, Searchable`.

> [!danger] Density is a **band**, not a floor — the most powerful dial in the game
> [[Crew Sim — Findings|The crew sim]] measured a **66-point swing** in win rate from terrain density alone — bigger than any points cost could ever produce. A 4-model elite crew beats a 14-model horde **81%** of the time on a sparse board and **15%** of the time on a very crowded one. **Parity sits at 9–12 large features** — exactly the band above, and every list in [[List Building]] is costed against it.
>
> Density is chosen *after* lists are locked, so it **must not be open-ended.** "Nine minimum, as crowded as you like" hands the game to whoever pushes the dial: a swarm player wants a jungle, a gunline wants a car park. **9–12.** A scenario may fix an exact number.

### Interact

A unit spends its Action to Interact with adjacent terrain; the stat used depends on the interaction:

| Interaction                          | Stat |
| ------------------------------------ | ---- |
| Kick door · drag object · Lift       | STR  |
| Pick lock · disarm trap              | DEX  |
| Hack · build/repair feature · lay/deploy trap · Search | INT  |
| Steady yourself in a hazard          | NRV  |

^tbl-interact

Routine Interacts auto-pass; test (7+) only when failure has a consequence. Terminals and digital control → [[Hacking]]. Full verb table → [[Terrain Interaction]].

Climb · vault · leap · swim are not Interacts — they are Move-slot maneuvers ([[Movement#Terrain movement]]):

- Obstacles under 2" — low leap: no test, −2" Move cost (flat).
- Gaps, 2"+ obstacles, climbs, and swim — AGI test vs 7+.

> [!question] Playtest dials
> 
> - Ladder cost: free vs −2" Move.
> - Fall damage: RESOLVED - under 3" nothing, 3"+ Prone, 6"+ Injury (+1 per 2", round up). First injuring fall (6") = +3 = 70% vs WND1; drop to +2 if it plays too hot.
> - Height advantage: ignoring Light cover from above may make roofs dominant — watch for camping.
> - Interior Building floors defaulting Open vs Difficult.

## Rule ledger
- [[core-004 Cover and line of sight]]
- [[adv-004 Weather and climate]]

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
