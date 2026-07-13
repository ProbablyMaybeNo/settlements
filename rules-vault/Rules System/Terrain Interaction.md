---
type: rule-phase
phase: "09"
stage: S3 Battle Layer
status: Drafted
build_order: 13
depends_on:
  - Terrain
feeds_into:
  - Hacking
tags:
  - settlements/phase
  - settlements/stage/s3
---
# 09 · Terrain Interaction
> **S3 Battle Layer** · status **Drafted** · build order **13**

**Depends on:** [[Terrain]]
**Feeds into:** [[Hacking]]
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

- **Auto-pass** — trivial actions with no consequence (open an unlocked door, push a button, drop a carried object).
- **Test** — everything else: `1d10 + Stat + mods` vs **7+**.
- No job-difficulty modifiers on ordinary Interacts. The only modifiers are ones the game already applies (skills, conditions, **Shaken**, etc.).
- Terminals / digital control → [[Hacking]] (range modifiers live there).
- **Natural 1** / **Natural 10** still auto-fail / auto-succeed.
- Direct interaction needs **base contact**. Spends the unit's **Action** slot.

### Contested Interacts

Most Interacts are auto-pass or a solo **7+** test.  
When two units contest the same object at the same time, use an **Opposed Test** (`1d10 + Stat + mods`, highest wins, **ties to the defender**):

- **Lift contest** — opposed **STR**; defender = carrier / first claim.
- Skills may create other contests (e.g. **Doorstop**); they still use this pattern.
- Digital contests (network control, shut-outs) → [[Hacking]].

### Stat ownership

|Domain|Stat|Examples|
|---|---|---|
|Force / haul|STR|Force door, Smash, Lift|
|Mechanical precision|DEX|Lockpick, **lay/disarm traps** (mechanical & electronic devices)|
|Digital / knowledge|INT|Hack, Search, **Build/Repair feature**, ID terrain|
|Climb / vault / leap|AGI|Move-slot tests (see [[Movement]] / [[Terrain]]) — not an Interact|

### Interaction verbs

| Verb                      | Tag                       | Stat | Resolution     | Notes                                        |
| ------------------------- | ------------------------- | ---- | -------------- | -------------------------------------------- |
| Open / close              | Openable                  | —    | Auto           | —                                            |
| Force door / Smash object | Breachable                | STR  | 7+             | Attempt is Loud                              |
| Lockpick                  | Lockable                  | DEX  | 7+             | Quiet                                        |
| Hack                      | Hackable / Powered        | INT  | see [[Hacking]] | Terminals, range, shut-outs                  |
| Lift                      | Movable                   | STR  | 7+             | Half MOV while carrying; drop within 1" free |
| Search                    | Searchable                | INT  | 7+             | See Searching                                |
| Repair feature            | Powered / Hackable / etc. | INT  | 7+             | See Feature damage                           |
|Climb / vault / leap / swim|Climbable / water|AGI|Move slot — see [[Movement]]|Under 2" = low leap, no test, −2" Move|

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
- Hit + successful Injury → feature goes **Offline** (non-functional; still on the board as terrain/LOS)
- Repair: adjacent Interact, INT, 7+ → restore to 1 WND and online (Jury-Rig may auto-succeed)
- If an **Offline** feature is Injured again → Destroyed, removed for the rest of the battle

Untriggered traps can be damaged this way. A trap that has already triggered is spent — don't use **Offline** to cancel a boom mid-trigger.

### Hacking
Operating terminals, Linked networks, range bands, and hacker-vs-hacker shut-outs live in **[[Hacking]]**. Feature **Offline** / **Destroyed** on terminals still uses the Feature damage rules above.

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

Disarm (either type) → **DEX** Interact, 7+ (nat 1 = boom). A trap wired into a **Linked** network can *alternatively* be neutralised by hacking the network (**INT** — Jam Signals / Linked terminal / related skills, see [[Hacking]]).

Deployables: Lifted scatter (Blocked openings), carried traps, settlement turrets/terminals.

### Locked design notes

1. **DEX** = mechanical · **INT** = digital
2. **Lift** replaces Barricade
3. **Searched** exhausts the *piece*
4. Turrets = controlled only (rules in [[Hacking]])
5. No building collapse; feature two-strike damage only
6. Ordinary Interacts = auto-pass **or** flat **7+**
7. Contested Lift = opposed STR; ties to defender
8. Full hacking system → [[Hacking]]

## Rule ledger
_none_

---
_Ported from Notion · Build Roadmap. See [[Rules System MOC]] and [[_Rules Map.canvas|the map]]._
