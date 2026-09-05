# The McCullough Combat Engine — verbatim capture

Combat-resolution chapters only, from three Joseph A. McCullough (Osprey Games) rulebooks that
share one engine: **Frostgrave 2.0** (2020), **Stargrave** (2021), and **Rangers of Shadow Deep,
Standard Edition** (2021 update). Costing/list-building content for these games is **already
captured** in `Research/Notes/Frostgrave and Stargrave.md` and `Research/Notes/Rangers of Shadow
Deep.md` — this capture is combat only, extracted to answer whether/how a single-roll
hit-and-wound mechanic ("back the damage into the initial roll") could inform a Settlements
engine change.

All page numbers below are the PDF's **printed page number** (footer), not the PDF page index,
except where noted. Extracted with PyMuPDF (`fitz`), `page.get_text("text")` — all three PDFs
have clean embedded text layers (1,400–2,200 chars/page average), no OCR needed. Ligature/curly-
quote mis-decodes (`�`) are a PyMuPDF/font artifact in the source PDF, not a capture error —
confirmed by `repr()` inspection; read as apostrophes/em-dashes in context.

---

## 1. FROSTGRAVE 2.0 — dice statement (p.14)

> "Whenever a figure is required to test its skill in some way, whether trying to move through
> difficult terrain or attempting to hit an enemy in a fight, require the player to roll a die in
> order to determine success or failure. Frostgrave uses a twenty-sided die (often just referred
> to as a d20) for all rolls. At a minimum, each player will need one d20 to play."

## 1a. FROSTGRAVE 2.0 — Automatic Success/Failure & Maximum Bonuses (p.44)

> "Whenever a figure makes a Stat Roll, including Will Rolls to resist spells, an unmodified roll
> of 20 is always a success. This is true even if the roll, after modifiers, still falls short of
> the Target Number. Conversely, an unmodified roll of 1 is always a failure... When a warband
> member makes a die roll of any type, including Stat Rolls, Combat Rolls, Shooting Rolls, Casting
> Rolls, etc., the figure may never have a total bonus greater than +10. If any combination of a
> figure's stats and modifiers results in a bonus above +10, treat the total as +10 instead."
>
> Worked example given: Fight +5 base, +1 magic sword, +2 Strength spell, +4 from two supporting
> figures = +12 raw, **capped to +10**.

## 1b. FROSTGRAVE 2.0 — COMBAT (melee), p.52–56

> "Once a figure is in combat with an enemy figure, it may spend one of its actions to fight...
> In a fight, each figure makes a Combat Roll by rolling a die and adding its Fight stat and any
> relevant modifiers. The figure with the higher score wins the fight and may inflict damage on
> its opponent. To determine damage, the winning figure takes its Combat Roll, adds any damage
> modifiers granted by its weaponry, and subtracts the loser's Armour stat. If the result is a
> positive number, this is the amount of damage inflicted. This damage is then subtracted from
> the Health of the loser... In the event that the Combat Rolls are tied, the two figures land
> their strikes simultaneously — both are considered to be the winner and both might take damage."

Worked example (p.52): knight (Fight +4, Armour 13) vs thug (Fight +2, Armour 10), both with hand
weapons. Knight rolls 13+4=17, thug rolls 7+2=9. Knight wins. Damage = 17 − 10 (thug's Armour) =
**7 damage**, subtracted from thug's Health.

**Combat Summary (p.55, verbatim numbered list):**
> 1. Both figures make a Combat Roll — roll a die and add the figure's Fight stat and any other
>    relevant modifiers (e.g. bonuses from magic or supporting figures).
> 2. Determine the winner by comparing Combat Rolls — highest wins.
> 3. Add any damage modifiers (such as +2 for a two-handed weapon or -1 for a dagger) to the
>    winner's Combat Roll.
> 4. Subtract the opponent's Armour stat from this total.
> 5. Apply any damage multipliers.
> 6. **If the final total is greater than 0, subtract that many points from the loser's Health.
>    If it is 0 or negative, no damage is done.**
> 7. The winner now has the choice to remain in combat or push either themselves or their
>    opponent back by 1".

**Optional Rule: Critical Hits (p.55):**
> "When a figure making a Combat Roll rolls a natural 20 (i.e. the number that comes up on the
> die, irrespective of modifiers or stats), then it has scored a critical hit. It automatically
> wins the combat, even if its opponent Combat Roll is higher. Furthermore, it does an additional
> +5 damage... Critical hits also apply to Shooting Rolls in the same way. In the rare case that
> both the shooter and the target roll natural 20s, however, the shot misses."

## 1c. FROSTGRAVE 2.0 — SHOOTING, p.57–59

> "Once range and line of sight have been confirmed, a shooting attack is resolved in a similar
> way to melee combat. The shooter makes a Shooting Roll, rolling a die and adding their Shoot
> stat. The target makes a Combat Roll, much as for melee combat, by adding its Fight stat and
> any relevant shooting defence modifiers (see below) to the roll of a die. Once both figures have
> a final score, the two are compared. If the Shooting Roll is higher, then the target is hit and
> damage is determined. If the target's Combat Roll is higher score, or the scores are equal,
> then the shot has missed — either the shooter's aim was off, or the target was able to duck out
> of the way in the nick of time.
>
> Damage is determined in the same way as for melee combat. The shooter takes their final
> Shooting Roll, adds any relevant damage modifiers and subtracts the target's Armour stat. If
> the result is a positive number, that is the amount of damage inflicted."

Worked example (p.57): archer (Shoot +2) vs thug (Fight +2, Armour 10), no modifiers. Archer
rolls 8+2=10. Thug rolls 2+2=4. Archer wins (hit). Damage = 10 − 10 (thug's Armour) = **0. Quoted
verbatim: "the archer's total of 10 is the same as the thug's Armour, so no damage is caused. The
arrow apparently just nicked their sleeve."** — this is the book's own on-page example of a hit
that deals zero damage, and the stated consequence is *narrative flavour text only*; no game-state
change of any kind follows.

**Shooting Defence Modifier Table (p.58):** Intervening Terrain +1 (cumulative per piece), Light
Cover +2, Heavy Cover +4, Hasty Shot +1 (shooter moved this activation), Large Target −2. "All
modifiers to shooting are expressed as bonuses to the target's Combat Roll."

**Shooting Summary (p.59, verbatim numbered list):**
> 1. The shooter checks range and line of sight, then declares their target.
> 2. The shooter makes a Shooting Roll — roll a die and add the figure's Shoot stat.
> 3. The target makes a Combat Roll — roll a die and add its Fight stat and any relevant shooting
>    defence modifiers.
> 4. Determine the winner by comparing the shooter's Shooting Roll to the target's Combat Roll —
>    highest wins.
> 5. If the target is the winner, or the scores are equal, the attack misses.
> 6. If the shooter is the winner, add any damage modifiers (such as +2 for a crossbow) to the
>    Shooting Roll.
> 7. Subtract the opponent's Armour stat from this total.
> 8. Apply any damage multipliers.
> 9. **If the final total is greater than 0, subtract that many points from the target's Health.
>    If it is 0 or negative, no damage is done.**

## 1d. FROSTGRAVE 2.0 — DAMAGE / Wounded, p.60

> "Whenever a figure takes damage, whether from combat, shooting, or any other source, the amount
> of damage is subtracted from the figure's current Health total. If this takes a figure to 0
> Health or less, that figure has been killed and should be removed from the table."

**OPTIONAL RULE: WOUNDED (p.60)** — the only state-threshold effect in the chapter, and it is
**Health-total-based, not hit-based**:
> "When any figure is reduced to 4 Health or less, regardless of their starting Health, they are
> considered wounded. Wounded figures are reduced to a single action per activation instead of
> the normal two... Wounded figures also suffer a -2 to all die rolls."

No rule anywhere in this chapter attaches a consequence to a hit that rolls 0 or negative
damage, beyond the flavour text in the worked example above.

---

## 2. STARGRAVE — dice statement (p.8)

> "Stargrave uses a twenty-sided die (often just referred to as a d20) for all rolls. Each player
> will need one d20 to play."

## 2a. STARGRAVE — COMBAT (melee), p.49–53

> "Once a figure is in combat with an enemy figure, it may spend one of its actions to fight...
> In a fight, both figures roll a die and add their Fight stat, plus any additional modifiers
> (to a maximum of +10). The figure with the higher score wins the fight and may inflict Damage
> on their opponent. To determine Damage, compare the total Fight score of the winning figure,
> including all modifiers, to the Armour stat of the loser. If the Fight score is greater,
> subtract the Armour score from it, and the resulting number is the Damage inflicted... In the
> event that the Fight scores are tied, the two figures land their strikes simultaneously — both
> are considered to be the winner and may inflict Damage on their opponent."

**MAXIMUM ARMOUR (sidebar, p.49):**
> "The maximum Armour Stat that any crewman can reach is 14. If any combination of gear, bonuses,
> or modifiers would take Armour over 14, treat it as 14."

Worked example (p.49): commando (Fight +4, Armour 11) vs recruit (Fight +2, Armour 10, knife).
Commando rolls 13+4=17, recruit rolls 7+2=9. Commando wins. Damage = 17 − 10 = **7 damage**.

**Combat resolution steps, verbatim (p.50):**
> 1. Both figures roll a die.
> 2. Both figures add their Fight stat and any other Fight bonuses (e.g. Power bonuses or
>    friendly figures also in combat).
> 3. Determine the winner of the combat by comparing Fight scores.
> 4. Apply Damage modifiers (such as -1 for knives) to the winner's final Fight score.
> 5. Subtract the opponent's Armour from this total.
> 6. Apply any Damage multipliers (some rare creatures do x2 or even x3 Damage; occasionally
>    damaged is halved).
> 7. **If the final total is greater than 0, subtract that many points from the loser's Health.
>    If it is 0 or negative, no Damage is done.**
> 8. The winner now has the choice to remain in combat or push either itself or its opponent
>    back by 1".

## 2b. STARGRAVE — SHOOTING, p.55–58

> "Once range and line of sight have been confirmed, a Shooting attack is resolved in a similar
> way to melee combat. Both the shooter and the target figure roll a die. The shooter adds its
> Shoot stat to the roll, while the target adds its Fight stat. Any additional modifiers are then
> added. Once both figures have a final score, the two are compared. If the shooter has the
> higher score, then the shot hits the target and Damage is determined... Damage is determined in
> exactly the same way as it is in melee combat. The shooter takes its final Shoot score and
> subtracts the target's Armour stat. If the result is a positive number, that is the amount of
> Damage inflicted. **If the target takes 4 or more points of Damage, it is also Stunned** (see
> page 59)."

Worked example (p.55): commando (Shoot +3) vs recruit (Fight +2, Armour 10). Commando rolls
8+3=11. Recruit rolls 2+2=4. Commando wins. Damage = 11 − 10 = **1 point** (explicit low-damage
example — no additional state change beyond the 1 Health lost; Stun threshold of 4 is not met).

**Shooting Modifier Table (p.56):** Intervening Terrain +1 (cumulative), Hasty Shot +1, Cleared
Jam +1, Light Cover +2, Stunned (target) +2, Heavy Cover +4, Large Target −2.

## 2c. STARGRAVE — EXTREME RESULTS: Critical Hits & Weapon Jams (p.59)

> "Whenever a figure rolls a natural '20' on its combat or shooting die... it has scored a
> critical hit. This figure automatically wins the combat or hits its target, and does an
> additional +5 Damage... If a target in a shooting attack rolls a natural 20, then the shot
> misses, even if the firer also rolls a natural 20."
>
> "If a figure making a shooting attack rolls a natural 1, then they have either run out of
> ammunition or their weapon has jammed. Either way, they must spend an action servicing their
> weapon before they can make another shooting attack with it."

## 2d. STARGRAVE — DAMAGE, STUN, WOUNDED, TOXINS (p.59–60)

> "Whenever a figure takes Damage, whether from combat, shooting, or any other source, the amount
> of Damage is subtracted from the figure's current Health total. If this takes a figure to 0
> Health or less, that figure has been killed and should be removed from the table."

**STUN (p.59) — the one state genuinely tied to a shooting hit, but gated on a Damage floor, not
on a zero/negative-damage hit:**
> "Whenever a figure takes 4 or more points of Damage from a single shooting attack — including
> flamethrower and grenade attacks — it becomes Stunned... Since a stunned figure is devoting all
> its effort to maximizing its use of cover, it receives a +2 bonus to Fight Rolls against
> shooting attacks. The next time this figure activates... it receives a maximum of one action
> during this activation."
>
> Note explicitly: Stun requires **4+ actual Damage points delivered**. A hit that deals 0 or
> negative Damage cannot trigger Stun — there is no separate "grazed but shaken" state below that
> threshold.

**WOUNDED (p.60)** — identical Health-threshold rule to Frostgrave (≤4 Health, one action, −2 to
all rolls), **not** hit-triggered.

No mechanic in Stargrave attaches any consequence — morale, positional, or otherwise — to a
shooting or melee hit whose final damage total is 0 or negative, beyond "no Damage is done."

---

## 3. RANGERS OF SHADOW DEEP (Standard Edition, 2021 update) — dice statement (p.8)

> "Rangers of Shadow Deep uses twenty-sided dice exclusively. These dice, which are numbered
> 1–20, are available at most game stores..."

## 3a. ROSD — character baseline stats (p.11), relevant to Q5 (Health as a pool)

**Ranger Base Stat-line:** Move 6 / Fight +2 / Shoot +1 / Armour 10 / Will +4 / **Health 18.**
Build Points may raise Fight, Shoot, Will, Move, or Health — **never Armour** — by 1 per BP, up
to 3 BP spent on stats total.

## 3b. ROSD — Hand-to-Hand Combat, p.27–29

> "Whenever a figure is in combat with an enemy figure, it may spend one of its actions to fight.
> During a fight, both figures have the chance to wound, and possibly kill, their opponent. To
> resolve a fight, the player should roll two dice — one for his figure, and one for the enemy
> figure. These are called Fight Rolls... Both figures should take their die roll and add their
> Fight Stat, plus any other modifiers, to determine their Combat Score. Whichever figure has the
> highest Combat Score has won the fight.
>
> To see if the figure that has won the fight has wounded its opponent, simply take its final
> Combat Score, apply any relevant damage modifiers (e.g. for using a two-handed weapon or
> dagger) and subtract its opponent's Armour Stat. If the result is greater than 0 then this is
> the amount of damage that the winning figure inflicts on its opponent."

Worked example (p.28): ranger (Fight +4, Armour 12) vs gnoll (Fight +2, Armour 11). Ranger rolls
16+4=20, gnoll rolls 8+2=10. Ranger wins. Damage = 20 − 11 = **9 damage** (11 with a two-handed
weapon's +2 modifier, per the text).

**Fight resolution steps, verbatim (p.28–29):**
> 1. Both figures roll a die.
> 2. Both figures add their Fight Stat and any other Fight bonuses (e.g. from magic bonuses or
>    friendly figures also in combat) to get their Combat Score.
> 3. Determine the winner based on which figure has the highest Combat Score.
> 4. Apply any damage modifiers (such as the +2 damage for a two-handed weapon or the -1 for a
>    dagger) to the winner's Combat Score.
> 5. Subtract the opponent's Armour from this total.
> 6. Apply any damage multipliers (rare and powerful weapons and creatures can do x2 or even x3
>    damage).
> 7. **If this final total is greater than 0, subtract that many points from the loser's Health.
>    If it is 0 or negative, no damage is done.**
> 8. The winner decides whether to remain in combat, to push his opponent back, or to step back.

**Critical Hits (p.29):**
> "Whenever a player rolls a natural 20 during a fight, he has scored a Critical Hit. This figure
> automatically wins the fight, regardless of its opponent's Combat Score. Furthermore, the hit
> does +5 damage. This rule applies to shooting attacks as well. **Evil creatures never score
> Critical Hits.**" (This last clause has no equivalent in Frostgrave/Stargrave, where any figure
> — including monsters — can crit.)

## 3c. ROSD — Shooting, p.29–31

> "A shooting attack is resolved in a very similar way to hand-to-hand combat. Both figures
> should roll a die. The shooter should add his Shoot Stat, plus any modifiers to determine his
> Combat Score. The target, however, should add its Fight Stat, plus any modifiers to determine
> its Combat Score. The scores are then compared. If the shooter has the higher score, then the
> shot has hit, and damage is determined in the same way as for hand-to-hand combat. If the
> target has the higher score, then the shot has missed."

Worked example (p.31): ranger (Shoot +2) vs gnoll (Fight +2, Armour 11). Ranger rolls 12+2=14.
Gnoll rolls 15+2=17. Gnoll wins — **the shot missed** (this example is a miss, not a 0-damage
hit; the book does not give a 0-damage shooting example for RoSD the way it does for Frostgrave).

**Shooting Modifiers Table (p.31):** Intervening Terrain +1 (cumulative), Light Cover +2, Heavy
Cover +4, Hurried Shot +1 (shooter moved this activation), Large Target −2. Identical shape to
Frostgrave/Stargrave, no Stun-equivalent line item.

## 3d. ROSD — Damage, p.31–32

> "Whenever a figure takes damage, whether from combat, shooting, or any other source, the amount
> of damage is subtracted from the figure's current Health total. If this takes a figure to 0
> Health or less, that figure is out of the game."

No Wounded/Stun-equivalent threshold state is defined in the RoSD core rulebook's Damage section
at all (unlike Frostgrave's Wounded and Stargrave's Wounded+Stun) — RoSD's only Health-threshold
mechanics found are **Poison** (any nonzero damage from a Poison-tagged creature → 1 action/turn)
and **Disease** (a Health Roll on being damaged by a Disease-tagged creature). Neither is tied to
a hit that deals 0 damage; both require actual damage to have been dealt.

## 3e. ROSD — no printed overall modifier cap found

Unlike Frostgrave (p.44, "+10" hard cap on any roll) and Stargrave (p.49, "to a maximum of +10"
stated inline in the Combat rule itself), **no equivalent overall modifier cap was found anywhere
in the RoSD Standard Edition core rulebook** — searched full text for "maximum bonus", "+10" in
context, "cannot exceed". The closest related rule is **Maximum Armour** does not appear in RoSD
either (that's Stargrave-only). RoSD's Heroic Abilities routinely hand out large single-roll
bonuses with no stated ceiling on how they stack: **Dive for Cover +10 Fight** (vs. a shooting
attack), **Parry +10** (to the Fight Roll, but does no damage if it wins), **Focus +8** (to a
Skill Roll), **Steady Aim +5 Shoot**, **Inner Strength +5** (Will), **Frenzied Attack +5** (Fight).
**[NOT FOUND]** — this is reported as a genuine absence, not a gap in the capture; the full text
was searched.

---

## 4. Cross-game modifier-stacking example (from Frostgrave, directly transferable pattern)

Frostgrave's own worked example of the +10 cap firing (p.44): a wizard with Fight +5, wielding a
magic sword (+1 Fight), under a Strength spell (+2 Fight), supported by two other figures in the
Multiple Combat rule (+4 Fight) — raw total +12, **capped to +10**. That is **four separate
modifier sources stacking on one roll** before the cap engages — base stat, item, spell, and
tactical/positional bonus. The Multiple Combat Modifier Table (Frostgrave p.53, Stargrave p.50,
RoSD p.29, near-identical text in all three) caps supporting-figure bonus at +6 on its own
(3 supporters × +2, "never more than +6 from supporting figures").

---

## 5. What none of the three rulebooks contain (searched, not found)

- **No "hit but no wound" state of any kind** — no push, no stagger, no forced Will/Nerve test,
  no positional consequence, no marker placed — tied specifically to a hit whose final damage
  total after Armour is 0 or negative. All three books use the identical formula: *"If it is 0
  or negative, no damage is done."* Full stop, no follow-on clause, in the numbered
  Combat/Shooting Summary of all three rulebooks.
- Stargrave's **Stun** is the closest thing to a fear/suppression-adjacent mechanic tied to
  ranged combat, but it requires **actual delivered Damage ≥4**, not a bare hit. It is a damage-
  magnitude threshold, not a hit/wound decoupling.
- No morale, Break, or Nerve system of any kind appears in the combat-resolution chapters of any
  of the three books (Frostgrave/Stargrave/RoSD do not have a morale mechanic — warbands/crews
  fight to the death or flee the table voluntarily; this is a known genre trait of the McCullough
  "one-page-ish" solo-friendly design line, not something this capture searched separately since
  it falls outside the combat-resolution chapters specifically requested).
