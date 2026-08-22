# Infected! — raw capture

Three files, all Immersion Studios / Oliver R. Shead. See `meta.json` for hashes, library paths and full provenance. **This is a limited capture — a sampler, a GM-screen reference card, and one adventure module. There is no core rulebook in this capture.** Quotes below are verbatim from the extracted PDF text (PyMuPDF `get_text("text")`, embedded text layer, no OCR needed).

---

## Game-type determination (from `original.pdf`, p.4)

> *"Role Playing Game — Welcome to Infected!, a tabletop role playing game — also called an RPG."*

> *"A role playing game puts your group of friends in command of the story and the outcome... In an RPG one person, called the Narrator, sets the scene and directs the story... Meanwhile, the other people in the gaming group, called the Players, take on the role of the protagonists, which are called Player Characters or PCs."*

This is unambiguous. There is no miniatures/basing/measured-movement layer anywhere in the 66 pages read.

---

## Core dice mechanic (`original.pdf`, pp.8-11)

> *"Most Actions Roll 2D10 — 1D10 + Attribute/1D10 + Skill — Target Number is 11. Almost every action in the Immersion RPG system uses 2D10 to determine its resolution."*

> *"One die rolls for the Attribute, the other one rolls for the Skill... the player must specify before rolling which die is for which statistic."*

> *"10 or below is a failure, 11 is 1 success, 12 is 2 successes, 13 is 3 successes and so on."*

**Gradients of Success** (p.10, matches the Narrator Screen table exactly):

| Successes | Result |
|---|---|
| Epic Bungle (0 successes, two natural 1s) | Catastrophe |
| Bungle (0 successes, one natural 1) | Failure With Complication |
| 0 | Fail |
| 1-4 | Fair Success |
| 5-9 | Good Success |
| 10-14 | Great Success |
| 15-19 | Incredible Success |
| 20+ | Perfection |

Natural 1 on a die = automatic failure for that die, no matter the bonus. Natural 10 = +1 extra success on top of the normal total.

**Bungles**: 0 successes + a natural 1 on any die = Potential Bungle; spend 1 point of Luck to downgrade it to a plain failure. 0 successes + two natural 1s = Potential Epic Bungle; costs 2 Luck to downgrade.

**Spiritual Attributes** (p.24, repeated verbatim on the Narrator Screen):
> *"Resolve — Spend a point to gain +2/+2 to one roll. Spend a point to remove damage, pain or exhaustion penalties for a scene. Spend a point to be able to function during a scene while dying (−4 on all rolls). Luck — Spend a point to prevent a Bungle. Spend a point to reroll of a non-Bungled roll."* Both recover at 1/day.

---

## Statistics (`original.pdf`, pp.8, 12-18)

- **Attributes** (1-10, ×2 Exp): Brawn, Dexterity, Presence, Tact, Awareness, Intelligence, Resolve (+ Luck as a spend-economy stat).
- **Skills** (0-10, ×1 Exp): Animal Handling, Athletics, Command, Construction, Deception, Deduction, Diplomacy, Dodge, Domestic, Hand to Hand, Intimidation, Knowledge, Language, Medical, Melee, Military, Observation, Ranged, Stealth, etc.
- **Circumstances** (0-10, ×1 Exp): Allies, Equipment, Minions, Pets, Reputation, Status, Team Mate, Wealth, Weapons — situational resources, occasionally rolled as an Extra Die.
- **Advantages & Disadvantages** (1-10): character quirks; Advantages cost Exp, Disadvantages grant bonus Exp at creation only.
- **Vital Statistics**: Health (2-40, = Brawn + Luck + purchased Extra Health, capped at 2x Base) and Morality (1-10, sanity/ethics).

Level bands used throughout (Attributes/Skills/Circumstances/A&D all share this): 1-2 Poor, 3-4 Average/Fair, 5-6 Proficient/Enviable, 7-8 Expert/Impressive, 9-10 Masterful/Legendary.

---

## Health thirds (`original.pdf`, pp.17, 25-27)

> *"Health is divided as evenly as possible into three categories: Battered, Injured and Wounded. When damage is received, it is first subtracted from Battered Health, then Injured Health, and finally Wounded Health. Battered Health has a chance to heal once per day, Injured once per week and Wounded once per month."*

Injured Health lost = −1 to all rolls. Wounded Health lost = an *additional* −1 (so −2 total). At 0 Health: dying. Negative Health beyond the character's Brawn score: dead.

Healing: `Brawn (+Medical)` check, 2 successes = 1 Health recovered, gated by the same daily/weekly/monthly cadence as above.

---

## Morality (`original.pdf`, p.28)

> *"Morality measures a character's ethical level. His humanity, empathy and sanity too... A character's starting Morality sits wherever the player wishes."*

| Level | Description |
|---|---|
| 1-2 | Brutal |
| 3-4 | Selfish |
| 5-6 | Moral |
| 7-8 | Honourable |
| 9-10 | Saint-Like |

"If a character ends up acting worse than their Morality level indicates, they must make a Morality check." (Text cuts off mid-sentence on the sampler's consequence rules — **[NOT FOUND]** what a failed Morality check actually does; not present in this partial capture.)

---

## Hardness Rating — the armour/weapon tier system (`original.pdf` pp.29-30, 34, 36; `narrator-screen.pdf`)

> *"All objects, including humans, have a Hardness Rating. This ranges from 0 to 5, and represents how capable something is of dealing or withstanding damage... Whenever damage is dealt, you should compare HR to see if the target can absorb the damage or if the weapon can actually harm the target."*

| HR | Absorbs this damage | Deals this damage |
|---|---|---|
| 0 Soft | Humans, animals | Unarmed strikes |
| 1 Blunt | Sport armour, wooden doors, plaster walls | Bats, bricks, sticks, clubs, low-speed impacts |
| 2 Sharp | Light ballistic armour, metal doors, vehicles | Light firearms, knives, axes, bows, hammers |
| 3 Fatal | Military armour, sandbags, armoured cars | Armour-piercing weapons, assault rifles, shotguns |
| 4 Destructive | APCs, light tanks, bunkers | Heavy machineguns, grenades, napalm |
| 5 Annihilating | Main battle tanks, heavy bunkers | Artillery, missiles, large bombs |

**Comparison rule** (verbatim from the Narrator Screen, matches `original.pdf` p.30 exactly):

| Comparison | Result |
|---|---|
| Defender 2+ HR above attacker | Attacker cannot deal damage |
| Defender 1 HR above | Attacker deals half damage |
| Equal HR | Deal damage and absorb as normal |
| Attacker 1 HR above | Defender absorbs half |
| Attacker 2+ HR above | Defender cannot absorb |

Worked examples given in the text: *"Handgun (HR 2) vs Humvee (HR 4) — The handgun can shoot at the humvee all day, but it's not going to do anything but make a few scratches. No damage is possible."* / *"Assault Rifle (HR 3) vs Humvee (HR 4) — the humvee is heavily armoured and 1 HR level higher... the damage would be halved."*

---

## Combat sequence (`narrator-screen.pdf`, full text; matches `original.pdf` pp.31-36 prose)

1. Roll for Initiative — `1d10 + Base Initiative`, highest first.
2. Roll to Strike — Hand to Hand: Brawn/Hand to Hand. Melee: Brawn/Melee. Ranged: Dexterity/Ranged.
3. Roll to Defend — Dodge: Dexterity/Dodge. Running: Dexterity/Athletics. Block: Dexterity/Hand to Hand. Parry: Dexterity/Melee.
4. Add weapon damage to net successes to Strike.
5. Roll to Absorb (compare HR) — Brawn(+Athletics), or Armour/Armour, or Brawn/Armour/Armour.
6. Damage is dealt — defender subtracts Health.

**Multiple Actions** penalty (both files agree): 2 actions = −2/−3, 3 = −3/−4/−5, 4 = −4/−5/−6/−7, 5 = −5/−6/−7/−8/−9. First action penalised by the total number of actions; each subsequent action one worse.

**Firing Bursts**: Short Burst +1 Ranged die/−2 Strike. Long Burst +2 dice/−4 Strike. Full Clip +3 dice/−6 Strike. Machineguns get +1 die to any burst free. Spraying a Group: −2 Strike, 1 target hit per success. Shooting Multiple Close Targets: roll once, −1 Strike per target (max targets = Ranged skill level).

**Targeted Strikes** (`narrator-screen.pdf`): Head −2 Strike/Knockout/Can't Absorb. Throat −4/Chokes/Can't Absorb/Bleeding. Limb −1/Cripples. Hand or Foot −2/Cripples. Groin −2/Stuns. Eyes −5/Blinds.

**Random NPC Generation** (`narrator-screen.pdf`, d10 table): 1 Cannibal, 2 Reaver, 3 Merchant, 4 Informant, 5 Farmer, 6 Soldier, 7 Delver, 8 Zealot, 9 Villager, 10 Innocent.

---

## The one infection/contagion rule found (`original.pdf`, p.46)

Full context — this is inside the sample adventure's stat block for Infected creatures (Claws/Bite attacks), not a general rules chapter:

> *"To determine the result of this, the victim must make a Brawn/Luck check, opposed by the amount of damage received, or the successes gained from the spray. If they fail, they're infected, and only rapid medical attention will give them any chance of survival (unless they somehow become immune)."*
>
> *"Claws — Strike: Dexterity/Hand to Hand. Damage: +1, HR 0. Special: Infection."*
> *"Bite — Strike: Dexterity/Hand to Hand −1. Damage: +2, HR 1. Special: Infection."*
>
> *"If the Narrator is not sure how many successes the character needs, they can apply a rule of thumb of 4 successes minimum."*

That is the **entire** infection mechanic present in this capture: a single opposed `Brawn/Luck` roll triggered as a Special property on a Claws/Bite attack, pass/fail, no stages, no visible symptom track, no incubation clock given. **[NOT FOUND]** — anything past "infected" (what happens next, whether/how it can be treated, what "immune" means mechanically) is not in the sampler, the screen, or the adventure. The adventure explicitly defers to *"page 188 of the Infected Rulebook"* for setting/faction detail the sampler doesn't cover, confirming a substantially larger core book exists that this capture does not include.

---

## Noise/detection — searched, thin

`lobster-problems.pdf` (the adventure) was searched for `noise`, `detect`, `scaveng`, `stealth`, `scent`, `smell`, `sound`, `attract`: zero hits on `noise`/`detect`/`scaveng`/`stealth`/`scent`/`smell`; 2 hits on `sound`, 1 on `attract`, both flavour text with no mechanical content:

> *"In the early morning, PCs will attract little attention, with all nearby buildings securely shut up in case of Infected attacks. Here and there will be a few lonely individuals, and sometimes the sound of movement."*

The sampler does note, in the encounter on p.46: *"if they happen to kill all the Infected, let them know that loud noises are a bad idea, and that they know others will hear it and come investigating"* — a GM-prompt, not a codified noise mechanic (no range, no roll, no table).

---

## Source

- Immersion Studios, Oliver R. Shead (writer/designer). Sampler funded via 2015 Kickstarter, printed mid-2016; this is the *second edition* of the sampler.
- Full book: *"Infected Zombie RPG"* on DriveThruRPG (per sampler p.3); www.immersion-rpg.com.
- Working copies: `research/sources/infected/{original,narrator-screen,lobster-problems}.pdf` (gitignored).
- Library masters: `G:\My Drive\Wargaming\Infected!\`.
