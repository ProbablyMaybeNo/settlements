---
type: rule-phase
phase: "09"
stage: S3 Battle Layer
status: Drafted
build_order: 13
depends_on:
  - Terrain
feeds_into: []
tags:
  - settlements/phase
  - settlements/stage/s3
---
# 09 · Terrain Interaction
> **S3 Battle Layer** · status **Drafted** · build order **13**

**Depends on:** [[Terrain]]
**Feeds into:** —
**Raw dependency (from Notion):** Terrain

## Focus
Acting on the environment — doors, structures, loot/search, collapse/repair.

The Rules column should nail down:
- Interaction actions: opening/breaking doors, barricading, climbing, operating objects — gated by Strength / Dexterity / Intelligence.
- Searching and looting terrain: what's found, the rolls, and who can search.
- Structural integrity: damaging and destroying cover/buildings, and what collapse does to nearby units.
- In-battle repair/reinforce, which ties into settlement upgrades (turrets, reinforced doors).
- Traps and deployable defences: how they're placed, triggered, and disarmed.

## Working rules / decisions

### Resolution

Terrain Interacts use the core test.

- Auto-pass — trivial actions with no consequence (open an unlocked door, push a button, drop a carried object).
- Test — everything else: `1d10 + Stat + mods` vs 7+.
- No job-difficulty modifiers on ordinary Interacts. The only modifiers are ones the game already applies (skills, conditions, Shaken, etc.).
- Exception: hacking applies range modifiers (below).
- Natural 1 / Natural 10 still auto-fail / auto-succeed.
- Direct interaction needs base contact. Spends the unit's Action slot.

### Contested Interacts

Most Interacts are auto-pass or a solo 7+ test.  
When two units contest the same object or system at the same time, use an Opposed Test (`1d10 + Stat + mods`, highest wins, ties to the defender):

- Lift contest — opposed STR; defender = carrier / first claim.
- Hack contest — opposed INT; defender = current network controller.
- Skills may create other contests (e.g. Doorstop); they still use this pattern.

### Stat ownership

|Domain|Stat|Examples|
|---|---|---|
|Force / haul|STR|Force door, Smash, Lift|
|Mechanical precision|DEX|Lockpick, set/disarm mechanical trap|
|Digital / knowledge|INT|Hack, Search, Repair feature, electronic trap|
|Climb / vault / leap|AGI|Move-slot tests (see [[Movement]] / [[Terrain]]) — not an Interact|

### Interaction verbs

|Verb|Tag|Stat|Resolution|Notes|
|---|---|---|---|---|
|Open / close unlocked|Openable|—|Auto|—|
|Force door / Smash object|Breachable|STR|7+|Attempt is Loud|
|Lockpick|Lockable|DEX|7+|Quiet; skills may auto-succeed|
|Hack|Hackable / Powered|INT|7+ + range mod|See Hacking|
|Lift|Movable|STR|7+ (auto if light scatter)|Half MOV while carrying; drop within 1" free|
|Search|Searchable|INT|7+|See Searching|
|Repair feature|Powered / Hackable / etc.|INT|7+|See Feature damage|
|Climb / vault / leap|Climbable|AGI|Move slot|Per [[Movement]]|

There is no Barricade verb. Blocking openings is done with Lift.

### Lift → Blocked openings

- Lift a Movable object and drop it blocking an Openable opening.
- That opening becomes Blocked: it cannot be used until someone Lifts the object clear (STR, 7+), or opposed STR if contested.
- Skills (Deadlift, Power Position, Doorstop) override or contest as written.

### Searching and looting

- Who: any fighter in base contact with a Searchable piece, not Engaged, not Down.
- Roll: Interact, INT, 7+.
- Exhaust: place a Searched token after the attempt — pass or fail. That piece cannot be searched again this battle.
- Default find table (`1d10` on a pass; scenarios may override):

|d10|Result|
|---|---|
|1|Hazard — trap/alarm/collapse; searcher is Pinned; search is Loud|
|2–4|Nothing|
|5–7|Supply cache — 1 Resource|
|8–9|Gear — one usable item (Med-Kit, Molotov, ammo, tool)|
|10|Jackpot — 1 Resource + one gear item|

### Structural integrity (buildings / cover)

Out of scope for launch (maybe forever). No damaging walls, cover sections, or building collapse.

Cover pieces stay as passive cover from [[Terrain]].

### Feature damage

Applies to interactive features (turrets, traps, vents, terminals, cameras, alarms) — not walls/cover.

- WND 1
- Armor −2 (heavy)
- Cover: Heavy (−2) to be hit, unless the attacker is within 6" → Open (0)
- Hit + successful Injury → feature goes Down (non-functional; still on the board as terrain/LOS)
- Repair: adjacent Interact, INT, 7+ → restore to 1 WND and online (Jury-Rig may auto-succeed)
- If a Down feature is Injured again → Destroyed, removed for the rest of the battle

Untriggered traps can be damaged this way. A trap that has already triggered is spent — don't use Down to cancel a boom mid-trigger.

### Hacking

1. Base contact with a terminal. Declare one Linked function.
2. Measure terminal → feature (max 24"). Apply range modifier:

|Band|Distance|Mod|
|---|---|---|
|Close|0–6"|0|
|Short|6–12"|−1|
|Medium|12–18"|−2|
|Long|18–24"|−3|

3. Uncontested → `1d10 + INT + mods` vs 7+.  
    Contested → opposed INT (same mods; ties to the current controller).
4. Pass/win → that one function resolves. Fail/lose → nothing.

Linked is required — range alone never makes a feature Linked.  
Firing a turret from a terminal counts as your attack for the activation.  
Turrets are controlled only (no auto-sentry).

Example functions (one per Action unless a skill says otherwise): lock/unlock/open/close doors · loop/reveal cameras · suppress/trip alarms · toggle power · rotate/deactivate/fire turret · arm/disarm/trigger Linked electronic traps.

### In-battle repair / settlement hook

- Repair = INT Interact, 7+, adjacent to a Down feature.
- No in-battle building reinforce at launch.
- Settlement upgrades show up as board state:

|Upgrade|Battle effect|
|---|---|
|Reinforced doors|Named doors start Lockable / Reinforced (skills/traits may be required to Force)|
|Turret emplacement|Turret: Powered · Hackable · Linked|
|Trap stockpile|X traps pre-placed, armed and concealed|
|Workshop / scrap|Materials / Build tokens if used|
|Generator / security net|Terminals, cameras, alarms — the Linked network|

### Traps and deployable defences

Trap = a waiting weapon card (trigger + effect + traits).

Place (DEX Interact, adjacent):

- Pass → armed and concealed
- Fail → armed but visible
- Nat 1 → triggers on the placer
- Pre-battle settlement traps skip the roll: deploy armed and concealed

Trigger: first enemy meeting the condition sets it off once, then spent. Fits Reaction Trigger and skills (Tripwire Eye, One in a Million).

Find: Threat Scan, or opposed INT vs the placer for a concealed trap.

Disarm:

- Mechanical → DEX Interact, 7+ (nat 1 = boom)
- Electronic → INT Interact, 7+, or via Jam Signals / Linked terminal / related skills

Deployables: Lifted scatter (Blocked openings), carried traps, settlement turrets/terminals.

### Locked design notes

1. DEX = mechanical · INT = digital
2. Lift replaces Barricade
3. Searched exhausts the _piece_
4. Turrets = controlled only
5. No building collapse; feature two-strike damage only
6. Ordinary Interacts = auto-pass or flat 7+
7. Hacking = 7+ with range mods (0 / −1 / −2 / −3), max 24"
8. Contested Lift / Hack = opposed tests; ties to defender

## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
