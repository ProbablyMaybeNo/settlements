# Mordheim — capture (mordheimer.net + Living Rulebook cross-check)

Retrieved 2026-08-21. Primary: https://mordheimer.net ("The New Mordheimer," Docusaurus wiki).
Cross-check: `living-rulebook.pdf` (122pp, hash-verified against `G:\My Drive\Wargaming\Mordheim\Mordheim Living Rulebook.pdf`).
Full page list and provenance in `meta.json`. This file holds the load-bearing verbatim tables and text;
narrative/flavour text is condensed. Quote marks preserve exact wording where it matters.

---

## Core resolution (docs/rules — characteristics, the-turn, movement, shooting, close-combat, recovery)

**Characteristics:** M, WS, BS, S, T, W, I, A, Ld, each roughly 1–10. **Characteristic test:** roll D6, pass on
roll ≤ characteristic value; **a natural 6 always fails**, regardless of the characteristic's value.
**Leadership tests:** roll 2D6, pass on ≤ Leadership.

**Turn sequence** (IGO-UGO, four phases every turn): 1. Recovery — rally fleeing models, stunned→knocked-down,
knocked-down→stand. 2. Movement — charges declared first, then compulsory moves, then everything else.
3. Shooting. 4. Hand-to-hand combat — **both sides fight in this phase regardless of whose turn it is.**

**To hit (shooting):** table keyed on BS, `D6 roll needed` from 6 (BS1) down to 1 (BS6), with negative rolls-needed
(auto-hit) above BS6. Modifiers: cover −1, long range (>half max range) −1, moved-and-shot −1, Large Target +1
(cap ±… no explicit stated cap in the source — modifiers stack freely).

**To hit (close combat):** compare attacker WS to target WS on a chart (roughly need a 4+ at equal WS, easier
if attacker WS is higher, harder if lower).

**To wound:** compare Strength (weapon Strength for shooting; attacker's own Strength, modified by weapon, for
melee) against target Toughness on a S-vs-T chart (higher S needs a lower D6 roll; a dash means no chance).

**Critical hits:** rolling a natural 6 to wound causes a critical hit (unless the attacker needed a 6 to wound
in the first place — "his opponent is simply too tough"). Roll a D6:

| D6 | Result |
|---|---|
| 1-2 | Hits a vital part — wound doubled to 2, armour save taken **before** doubling |
| 3-4 | Hits an exposed spot — wound doubled to 2, **ignores all armour saves** |
| 5-6 | Master strike — wound doubled to 2, ignores all armour saves, **+2 to any Injury roll** |

One critical hit max per model per hand-to-hand combat phase.

**Armour saves:** D6 roll ≥ threshold. Light armour 6+, Heavy armour 5+, Gromril 4+, **shield adds +1**.
**Armour save modifier by attacker Strength:** S1-3 none, S4 −1, S5 −2, S6 −3, S7 −4, S8 −5, S9+ −6.

**Wound-to-injury roll** (when Wounds hit 0), D6 rolled by the attacker, worst-of-multiple-hits-that-turn:

| D6 | Result |
|---|---|
| 1-2 | Knocked down (face up; can crawl 2", cannot fight/shoot/cast) |
| 3-4 | Stunned (face down; can do nothing; auto-taken-OOA if hit again in HTH) |
| 5-6 | Out of action — removed from the battle; roll on Serious Injuries post-battle if a Hero |

Knocked-down models auto-recover to standing at the start of their next Recovery phase (half-move only, no
charge, strikes last if still in combat). Stunned → knocked-down at the next Recovery phase. A knocked-down
model attacked in HTH is auto-hit and, if it fails its armour save, is automatically taken out of action.

**Fully WFB-derived** — this is the classic 5th/6th-edition Warhammer Fantasy Battle skirmish engine (roll-under
stat tests, opposed WS/BS-vs-target charts, S-vs-T wound charts, armour save thresholds). None of this ports
directly to Settlements' flat `1d10+Stat vs 7+`; the useful transferable content is downstream of it
(injury/campaign/psychology), not the dice engine itself.

---

## Serious Injuries chart (docs/campaigns#serious-injuries, verbatim; confirmed identical in living-rulebook.pdf p.79-80)

Henchmen out of action: D6, **1-2 removed permanently, 3-6 fight next battle as normal.**

Heroes out of action roll **D66** (first D6 = tens, second D6 = units):

| D66 | Result |
|---|---|
| 11-15 | **Dead.** Removed from roster, all gear lost. |
| 16-21 | **Multiple Injuries.** Roll D6 times more on this table; re-roll further Dead/Captured/Multiple Injuries. |
| 22 | **Leg Wound.** Permanent −1 Movement. |
| 23 | **Arm Wound.** Roll again: 1 = arm amputated, single one-handed weapon only from now on; 2-6 = miss next game. |
| 24 | **Madness.** Roll again: 1-3 = Stupidity from now on; 4-6 = Frenzy from now on. |
| 25 | **Smashed Leg.** Roll again: 1 = may not run (may still charge); 2-6 = miss next game. |
| 26 | **Chest Wound.** Permanent −1 Toughness. |
| 31 | **Blinded in One Eye.** Permanent −1 Ballistic Skill; blinded a second time and the warrior must retire. |
| 32 | **Old Battle Wound.** Roll D6 before every future battle; on a 1, cannot fight that battle. |
| 33 | **Nervous Condition.** Permanent −1 Initiative. |
| 34 | **Hand Injury.** Permanent −1 Weapon Skill. |
| 35 | **Deep Wound.** Miss next D3 games; does nothing while recovering. |
| 36 | **Robbed.** Survives, but all weapons/armour/equipment lost. |
| 41-55 | **Full Recovery.** No effect. |
| 56 | **Bitter Enmity.** Gains Hatred (D6: 1-3 individual who injured him / 4 their leader / 5 their whole warband / 6 all warbands of that type). |
| 61 | **Captured.** Held by the other warband — ransom, prisoner exchange, sold to slavers (D6×5 gc), or killed for a Zombie/sacrifice depending on captor faction. |
| 62-63 | **Hardened.** Immune to fear from now on. |
| 64 | **Horrible Scars.** Causes fear from now on. |
| 65 | **Sold to the Pits.** Fights a Pit Fighter; lose → maybe dead/injured (D66 11-35) and thrown out with no gear; win → 50gc, +2 XP, keeps gear. |
| 66 | **Survives Against the Odds.** +1 Experience. |

**Wiki and Living Rulebook agree word-for-word on every line of this chart.** No divergence found.

**Minor secondary-source divergence (not from the two primary/cross-check sources):** the community
`post-game-chart.pdf` cheat sheet prints "23 Arm Wound: 1 = amputated, **2-5** = miss next game" and
"25 Smashed Leg: 1 = may not run, **2-5** = miss next game" — both silently drop the "6" result present in
both the wiki and the Living Rulebook's "2-6." Also adds a 1-4/5-6 sub-roll on who holds a Captured prisoner
that appears in neither primary source. Treat the wiki/Living Rulebook pairing as authoritative; this
cheat sheet as an imperfect derivative.

---

## Experience and Advancement (docs/campaigns/experience, confirmed verbatim in living-rulebook.pdf p.81-82)

+1 XP for surviving any battle (even injured). Scenario-specific bonuses layered on top (per-kill, objective, etc).

**Underdog table** (XP bonus per surviving fighter, keyed to the *gap* in Warband Rating):

| Rating gap | XP bonus |
|---|---|
| 0-50 | None |
| 51-75 | +1 |
| 76-100 | +2 |
| 101-150 | +3 |
| 151-300 | +4 |
| 301+ | +5 |

**Advance rolls**, 2D6:

Heroes: 2-5 New Skill · 6 (roll again) +1 STR or +1 A · 7 choose +1 WS or +1 BS · 8 (roll again) +1 I or +1 Ld ·
9 (roll again) +1 W or +1 T · 10-12 New Skill.

Henchmen (whole group advances together; max +1 per characteristic ever): 2-4 +1 I · 5 +1 S · 6-7 choose +1 BS
or +1 WS · 8 +1 A · 9 +1 Ld · **10-12 "The Lad's Got Talent"** — one model in the group becomes a Hero, keeps
its accumulated XP and characteristic increases, gets 2 chosen skill-list access, and immediately rolls once
on the Heroes Advance table. Remaining henchmen in the group re-roll their own advance (re-rolling further
10-12s).

**Warband Rating** = (number of warriors × 5) + accumulated Experience. Large creatures (Rat Ogres etc.) are
worth 20 points + their Experience, instead of 5. **Confirmed byte-for-byte identical wording in
ultimate-reference-sheet.pdf** ("The warband rating is simply the number of warriors in it multiplied by 5,
plus their accumulated experience. Large creatures such as Rat Ogres are worth 20 points…").

---

## Income and Exploration (docs/campaigns/income)

Post-battle: roll 1D6 per surviving Hero (not Henchmen), +1 die if you won, max 6 dice picked even if more
are allowed. Sum → shard count:

| Dice total | Shards found |
|---|---|
| 1-5 | 1 |
| 6-11 | 2 |
| 12-17 | 3 |
| 18-24 | 4 |
| 25-30 | 5 |
| 31-35 | 6 |
| 36+ | 7 |

**Doubles/triples/etc. on the dice trigger a separate Exploration Chart entry** — 30 distinct named locations
across doubles (6 entries) through six-of-a-kind (6 entries), each with its own loot/effect table (full text
captured; see the Mordheim.md note for the mechanic-level takeaways — Catacombs infiltration, faction-gated
outcomes for Skaven/Undead/Possessed/Sisters, and eight increasingly rare magic-item results at six-of-a-kind).

**Wyrdstone sell table** — price per shard **falls** both with quantity sold at once and with warband size
(explicit anti-snowball/diminishing-returns table, reproduced in the Mordheim.md note in full).

---

## Encampments (docs/optional-rules/encampments/*) — Town Cryer optional rules, NOT in the core rulebook or Living Rulebook

Three settlements, each its own page: **Sigmarhaven** (safest, tithe of 2 wyrdstone shards/battle, restricted
warband list), **Brigandsburg** (rougher, hired swords at 75% cost but risk of ambush when Rare-item
searching), **Cutthroat's Den** (most lawless, goods at +2 to find but double cost, a slaver, an underground
pit-fighting arena). Each has its own D66-style Housing chart (Tavern/House/Tent/Ruins/Farm/Barracks/Graveyard/
Cellar variants) and its own set of visitable Locations (Surgeon/Smithy/Muleskinner/Merchant/gambling den),
each with its own small sub-tables. Full verbatim tables captured live in Mordheim.md under
"The encampment layer — two full settlement rulesets."

## Lustria settlements (docs/campaigns/campaign-settings/lustria/optional-rules/settlements) — a SECOND, separate settlement ruleset

Three coastal settlements — **Santa Magritta** (best-equipped, town watch shows up after 4 rounds and can be
bribed, 10% income tithe, several races banned), **Nuevo Luccini** (pirate den, +2 to find goods at standard
cost), **Skeggi** (Norse colony, discounted upkeep for 5 named Hired Sword types). No shared mechanical
framework with the Mordheim-proper encampments — a parallel, independently-written settlement system for a
different campaign setting.

---

## Psychology suite (docs/rules/leadership-psychology)

**Rout test:** 2D6 vs warband leader's Ld, triggered when ≥25% of the warband is OOA; failure ends the battle
immediately for that side. Voluntary rout allowed once the threshold is met.

**All Alone:** a lone model fighting 2+ enemies with no friendly model within 6" tests Ld (2D6) at the end of
combat; failure = flees 2D6", auto-hit once per enemy on the way out.

**Fear:** Ld test to charge a Fear-causing enemy, or to fight one who charged you (failure = need 6s to hit
that combat round).

**Frenzy:** must charge if any enemy in range; doubles Attacks characteristic in HTH; immune to other psychology
while in charge range; lost if knocked down/stunned.

**Hatred:** re-roll misses in the first round of combat against a hated target only.

**Stupidity:** Ld test each turn; on a fail, D6 — 1-3 shambles forward at half speed (no charge, no shoot),
4-6 stands and drools (does nothing).

**Animosity** (Orcs/Goblins only): D6 per Henchman each turn, 1-in-6 triggers a further roll that can force the
model to fight a friendly Orc/Goblin, shoot at one, hurl insults (do nothing), or charge off alone toward the
enemy.

**All of this is the "classic" WFB psychology suite** — six named states, several with their own sub-roll,
before any Insanity content is added.

## Insanity — "At the Mouth of Madness" (Town Cryer #8, explicitly a bolt-on, not core)

A second, parallel XP-style track ("Insanity Points," IP) marked from the *opposite* end of the same
Experience boxes. Gains: +1 IP for a failed Fear test, +1 for casting a Necromantic/Chaos spell, +1 for a
critical wound, +1 for poison, +1D3 (replacing the normal effect) for rolling Madness on the Serious Injury
chart, +1 (replacing the normal effect) for Nervous Condition. Reaching a new experience-track level forces
a Ld test; fail it and roll a D6 (duration: D6 turns / next battle / next 2 battles / indefinite) then a
**4D6 (range 4–24) table of 21 unique named conditions** — Amnesia, Temper temper!, I'm a chicken!, Paranoia,
hallucinations, six kinds of phobia, Heroic Idiocy, multiple personalities, and (at the extreme end, 24)
permanent removal from the roster ("Completely bonkers"). Orc/Beastmen/Undead/Possessed warbands are immune
by racial mindset; a handful of caster troop types accrue IP at half rate. **This more than doubles the
psychology bookkeeping** already present in the base game (a second D66-scale table layered on the first) —
directly relevant to how much table-time a "lean" Stress/Nerve system should cost by comparison.

## Random Happenings (Mordheim Annual 2002 — docs/optional-rules/random-happenings)

1-in-6 chance per player-turn of a random encounter; if triggered, roll D66 on a 36-entry table (Ogre
Mercenary, Swarm of Rats, Earthquake, a summoned Bloodletter daemon, Skeletons, a carnivorous tree, a
storm-of-chaos sub-table, booby traps, plague victims, etc). Each entry places a neutral/hostile actor or
environmental effect with its own short rule; capped at one random encounter per game.

---

## Weapons & Armour — core costs (living-rulebook.pdf p.52, Mercenary Equipment List; cross-checked against
docs/weapons-armour/armour)

| Item | Cost |
|---|---|
| Dagger | 1st free / 2gc |
| Mace / Hammer / Club | 3gc |
| Axe | 5gc |
| Sword | 10gc |
| Spear | 10gc |
| Halberd | 10gc |
| Morning star | 15gc |
| Double-handed weapon | 15gc |
| Bow | 10gc |
| Long bow | 15gc |
| Crossbow | 25gc |
| Pistol | 15gc (30 brace) |
| Duelling pistol | 25gc (50 brace) |
| Blunderbuss | 30gc |
| Handgun | 35gc |
| Hunting rifle | 200gc |
| Shield | 5gc |
| Buckler | 5gc |
| Helmet | 10gc |
| Light armour | 20gc |
| Heavy armour | 50gc |
| Gromril armour | 150gc (4+ save) |
| Ithilmar armour | 90gc (5+ save) |

**Caution logged in meta.json:** a bulk regex scrape of the wiki's `/docs/weapons-armour/close-combat` page
(73k chars, every warband's weapon variants) produced clearly wrong numbers (Dagger "15gc", Kitchen Knife
"40gc") — the figures above come from the Living Rulebook's actual price list instead, cross-checked against
the wiki's dedicated armour page, which scraped cleanly.

---

## Source pages (URLs)

https://mordheimer.net/docs/rules · /docs/rules/characteristics · /docs/rules/the-turn · /docs/rules/recovery ·
/docs/rules/movement · /docs/rules/shooting · /docs/rules/close-combat · /docs/rules/wounds-and-injuries ·
/docs/rules/leadership-psychology · /docs/campaigns · /docs/campaigns/experience · /docs/campaigns/income ·
/docs/campaigns/skills · /docs/optional-rules/encampments · /docs/optional-rules/encampments/sigmarhaven ·
/docs/optional-rules/encampments/cutthroats-den · /docs/optional-rules/encampments/brigandsburg ·
/docs/campaigns/campaign-settings/lustria/optional-rules/settlements ·
/docs/optional-rules/at-the-mouth-of-madness · /docs/optional-rules/random-happenings · /docs/tools ·
/docs/faqs · /docs/weapons-armour/armour
