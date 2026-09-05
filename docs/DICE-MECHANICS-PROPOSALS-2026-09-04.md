# Dice Mechanics Proposals — a fresh-mind pass

*2026-09-04. Written without reference to the current Settlements resolution rules, on request. Inputs: the 14 raw rulebook captures in `research/sources/`, the 33 curated notes in `rules-vault/Research/`, the audits and points research in `docs/`, the setting-tech research, and the cliff notes of Ford & Hutchinson's* The Fundamentals of Tabletop Miniatures Game Design *(2025). Every probability below was computed exactly (scripts in the session scratchpad), not estimated.*

---

## 0. What the brief asks for, turned into numbers

The brief: ultra-realistic, bloody fights between civilians in a near-future collapse. Average units die fast, shoot badly, carry scavenged kit, and crack under stress. Dense boards with graded cover and height. Short and long range matter. The mechanic must be simple, but must leave room for growth and customisation, and it must not run out of headroom the way a single d10 against a fixed 7+ does.

Design targets I held every candidate to:

| Target | Value | Where it comes from |
|---|---|---|
| Green civilian, short range, open ground, one shot: chance the target goes down | 25–50% | "Die quickly" plus Infinity's ">50% kill on hit" being the book's template for a gritty firefight (Fundamentals p.300) |
| Same shooter at long range or against light cover | 15–35% | Spectre Ops militia hit rates; the audits' finding that cover must matter most against bad shooters |
| Same shooter against heavy cover | 5–20%, never zero | A sliver of luck keeps civilians "unpredictable rather than useless" (Fundamentals p.160) |
| Veteran vs green, same situation | roughly 1.5× to 2× | Any wider and lists collapse into "one real build" (audit finding) |
| Rolls per shot | 1, at most 2 | Necromunda's four-roll chain is the research's canonical "avoid"; the audits reject extra mid-activation opposed rolls |
| A hit that fails to wound | must still do something (Stress) | Convergent across Zona Alfa, Spectre, Fistful of Lead, Last Days; the audits' "every hit does something" |
| Cover | two tiers, elevation demotes a tier | Zona Alfa's elevation rule was the single highest-rated steal in the research |
| Stress | bites within two volleys, before one-wound models die | Audit finding: a stress track that only fires at a threshold rarely reached is dead weight |
| Growth headroom | at least 8 meaningful steps per stat, ideally on two axes | The 7+ headroom problem; OPR/BattleTech/Rogue Trader all needed super-linear patches at the top of a single ladder |
| Modifiers | on one side of the roll only, capped | Fundamentals p.164; the audits' modifier-cap ruling |

The one design principle that answers the headroom question, straight from the book: **"opposed statistic tests keep every statistic value meaningful on low-granularity dice"** (p.169), and **"a bell curve creates a headwind for powerful characters"** (pp.160–161). A single flat die against a fixed number has neither property. Every system below uses at least one of the two.

A shared vocabulary so the four systems can be compared like-for-like:

- **Outcomes of any attack, in order:** Miss · **Pinned** (the target takes 1 Stress) · **Down** (out of the fight, bleeding; dies at end of game unless treated) · **Killed**.
- **Stress** is a token count on a model. Every Pinned result adds one. Stress degrades the model's own rolls. At Stress ≥ Nerve the model **Breaks** (must move to cover or away; may not attack until rallied). Cheap models break automatically; leaders test.
- **Cover** is Light (waist-high, soft) or Heavy (walls, vehicles, interiors). **Shooting from 2"+ above the target demotes its cover one tier** (Heavy→Light→none).
- **Range** is Short or Long per weapon, plus **Point Blank** (within 3").
- **Scavenged gear** carries the *Unreliable* trait: the weapon jams on the roll's fumble result and costs an action to clear. Crude armour is one step worse than the real thing. No ammo tracking anywhere.

---

## 1. System A — "Handful": d6 success pool with a success ladder

### The literal mechanic
Every stat is a number of six-sided dice: **Shoot, Fight, Nerve, Wits**, each 1–6. To do anything, pick up that many d6, add or remove dice for the situation (never below one die), and roll. **Each 5 or 6 is a success; a natural 6 counts as two.** Count successes and read the ladder:

| Successes | Attack result | Test result |
|---|---|---|
| 0 | Miss | Fail |
| 1 | Pinned | Pass (routine task) |
| 2 | Down | Pass (hard task) |
| 3+ | Killed | Pass (heroic task) |

The one rule of modifiers: **everything about the shooter changes dice; everything about the target changes the result.**

### Shooting
1. Take Shoot dice. Add the weapon's **Volume** (pistol 0, rifle +1, shotgun +2 at Short, machine gun +2). Add +1 for Aimed (spent the previous action). Remove 1 per Stress token. Remove 1 at Long range, 2 beyond Long. Remove 1 for Light cover, 2 for Heavy. Floor: one die.
2. Roll, count successes, read the ladder.
3. Armour downgrades the result one step (soft vest) or two (plates), never below Pinned. The weapon's **Pen** cancels downgrade steps (pistol 0, rifle 1, sniper/anti-materiel 2). So a rifle ignores a soft vest entirely and treats plates as a vest.
4. **Point Blank:** within 3" roll Nerve dice instead of Shoot dice. Untrained people hit at arm's length if they hold together (Spectre Ops' CQB rule, the research's "transferable one-liner").

Elevation demotes the target's cover a tier before you count dice removed.

### Melee
Both models roll **Fight + weapon Volume** (knife 0, bat +1, axe/machete +1 with Pen 1) simultaneously. Charging adds +1 die; each extra attacker on the same target adds +1 die to the group (max +2). The side with more successes applies the **difference** on the ladder to the loser. A tie is a scuffle: both take Pinned. Armour downgrades as in shooting.

### Tests
Wits or Nerve dice, need 1 success (routine), 2 (hard), 3 (heroic). Hacking, climbing, first aid, spotting all use this. **Rally** is a Nerve test at hard difficulty; success removes all Stress.

### Stress and morale
Every Pinned result is one Stress token; friendly Down/Killed within 3" is one Stress token. Each token removes one die from every pool. At Stress ≥ Nerve the model Breaks. A Broken model with Nerve 1–2 bolts automatically toward cover and out of line of sight; leaders may test Nerve to hold. This is how a civilian firefight actually ends: not with the bodies, with the people who stop shooting back.

### Damage
One wound. Down means bleeding out: it dies at game end unless a friendly spends an action in contact with a med kit (one use). Killed is killed. The *Tough* trait (campaign only) turns the first Down of the game into Pinned, once.

### Weapons and scavenged kit
A weapon is four numbers and a trait list: Short / Long range, Volume, Pen, traits. *Unreliable* (pipe shotgun, home-made SMG, nail gun): if any die shows a 1, the weapon jams after the shot; clearing it is an action. *Crude* armour is one step worse than the equivalent. Because Volume is dice and Pen is result steps, a scavenged weapon can be worse on either axis independently, which is the DIY-armoury customisation space.

### Growth and headroom
Two axes:
- **Dice** (the main ladder): 1 → 6 at creation, 8 in a long campaign. Each step is worth roughly the same absolute chance and never saturates because the ladder rewards *extra* successes with Kill instead of Down.
- **Training threshold** (rare, tier-gated): Elite models succeed on 4+ instead of 5+. This is the "feels elite" lever and should be gated, not sold.

Measured in the open, no armour, chance the target goes Down or worse: 1d 17% · 2d 33% · 3d 48% · 4d 60% · 5d 70% · 6d 78% · 7d 84% · 8d 88%. Chance of an outright Kill: 2d 8% · 4d 33% · 6d 57%. Nine steps before the curve flattens, with the top end still losing 30+ points to heavy cover.

### The numbers (chance the target goes Down or worse per shot)

| Shooter | Open, Short | Long | Light cover | Heavy cover | Heavy + Long |
|---|---|---|---|---|---|
| Green civilian, pistol (2 dice) | 33% | 17% | 17% | 17% | 17% |
| Green civilian, rifle (3 dice) | 48% | 33% | 33% | 17% | 17% |
| Trained, rifle (4 dice) | 60% | 48% | 48% | 33% | 17% |
| Veteran, rifle (5 dice) | 70% | 60% | 60% | 48% | 33% |
| Elite, rifle (6 dice) | 78% | 70% | 70% | 60% | 48% |
| Elite, aimed rifle (7 dice) | 84% | 78% | 78% | 70% | 60% |

Against a soft vest with a pistol (or plates with a rifle), subtract one result step: green rifle in the open drops to 20%, veteran to 46%, elite aimed to 66%.

Full split for a green rifle shot in the open: Miss 30% · Pinned 22% · Down 28% · Killed 20%. For one die (any civilian shooting into heavy cover): Miss 67% · Pinned 17% · Down 17%.

### Handling time
One roll per attack (two pools rolled at once in melee). Counting successes on 2–7 dice is instant; the ace rule is the only thing to remember.

### Strengths
- The most physical, legible engine: "cover takes dice out of your hand" reads from across the table (the BLKOUT lesson).
- Effectively unlimited granularity on the dice axis (Fundamentals p.159), and the ladder converts extra successes into extra lethality instead of wasting them, so top-end growth still means something.
- Zero arithmetic. Only d6s.
- Melee as a simultaneous pool comparison is fast and brutal, and doubles as the grapple/scuffle rule.

### Weaknesses
- Small pools are swingy by construction; the book's own rule is that a pool only smooths at six or more dice. A civilian's fight is a coin toss, which is thematically right but will feel random to some players.
- Dice removal for cover is worth a bigger *relative* chunk to bad shooters than good ones (a green rifle loses 31 points to heavy cover, an elite loses 18). That is arguably realistic, but the audits found cover value that depends on the enemy's skill is the hardest thing to price.
- Needs 8–10 d6 per player on the table; a 7-dice pool is the practical ceiling before counting slows.

---

## 2. System B — "Margin": 2d6 + Skill against a Difficulty, one roll decides everything

### The literal mechanic
Stats are small modifiers: **Shoot, Fight, Nerve, Wits**, from −1 (liability) through 0 (untrained adult) to +5 (the best in the campaign). Roll **2d6, add the stat and any shooter-side modifiers, and compare to a Difficulty set entirely by the target's situation.** The amount you beat the Difficulty by is the **margin**, and the margin *is* the result:

| Margin | Result |
|---|---|
| below 0 | Miss |
| 0–1 | Pinned |
| 2–3 | Down |
| 4+ | Killed |

Natural 2 (snake eyes) is always a miss and jams an Unreliable weapon. Natural 12 always at least Pins and counts as margin +2 whatever the Difficulty.

The one rule of modifiers: **what you are and what you did goes on your dice; where the target is sets the number.** Roll-side modifiers are capped at ±3.

### Shooting
1. **Difficulty starts at 8.** Long range +2, beyond Long +4. Light cover +1, Heavy +2, fortified/interior +3. Elevation demotes cover a tier first. Target that sprinted this turn +1.
2. **Your roll:** 2d6 + Shoot + weapon **Accuracy** at this band (rifle +1 Short / 0 Long; pistol +1 / −2; shotgun +2 / −2; hunting rifle 0 / +1; marksman rifle 0 / +2) + 1 if Aimed − 1 per Stress token.
3. Compute margin. **Armour subtracts from margin:** soft vest 1, plates 2, minus the weapon's Pen (rifle 1, heavy 2). Read the ladder.
4. **Point Blank:** within 3", use Nerve instead of Shoot.

That is the entire shooting rule. There is no second roll unless you decide the defender should roll armour (see the questions at the end).

### Melee
Opposed: each rolls 2d6 + Fight + weapon (knife 0, club/bat +1, machete +1 Pen 1, two-handed +2). Charging +1, each extra attacker +1 (max +2). The winner applies the difference on the ladder to the loser, minus armour. A tie: both Pinned. A defender behind an obstacle (fighting over a wall) adds +1.

### Tests
2d6 + stat vs 8 (routine), 10 (hard), 12 (heroic). Margin is ignored except that margin 4+ on a hack, search or climb is a "clean" result with a scenario-defined perk. Rally: 2d6 + Nerve vs 8, +1 per friendly model within 3".

### Stress and morale
Each Pinned result and each friendly casualty within 3" is one Stress token, −1 to every roll the model makes. Break at Stress ≥ Nerve + 2 (so a Nerve 0 civilian breaks on the second token). Cheap models bolt automatically; leaders test.

### Damage
One wound; Down bleeds out; Killed is killed. Tough as in System A.

### Weapons and scavenged kit
A weapon is Short / Long range, Accuracy at each band, Pen, traits. Unreliable jams on snake eyes. This system gives the cleanest weapon envelope of the four because Accuracy and Pen are the same unit as everything else (one point = one pip of margin).

### Growth and headroom
The bell curve does the work. Against Difficulty 8 in the open the ladder runs: +0 42% hit (28% Down or worse with a rifle) · +1 58% · +2 72% · +3 83% · +4 92% · +5 97%. Each +1 is worth 17 points in the middle and 5 points at the top, so a campaign veteran at +5 is superb in the open and still only 28% against a target in heavy cover at long range. That is the "headwind for powerful characters" the book describes, and it is what lets you sell +1s at a flat price without a hard cap: the curve prices the top of the ladder for you. Eight steps (−1 to +6) before anything saturates, times weapon Accuracy, times Aimed, times the two threshold skills below.

Second axis, gated not sold: **result-shifting skills** (Killer: Down on margin 1+ in melee; Marksman: Killed on margin 3+ with a rifle when Aimed; Cool Hand: ignore the first Stress token when shooting). These widen the ladder rather than the number, which is the book's "abilities as exceptions, not bigger numbers" (p.363).

### The numbers (chance the target goes Down or worse per shot, unarmoured)

| Shooter | Open, Short (Diff 8) | Long (10) | Light cover (9) | Heavy cover (10) | Heavy + Long (12) |
|---|---|---|---|---|---|
| Green civilian, pistol (+0) | 17% | 3% | 8% | 3% | 0% |
| Green civilian, rifle (+1) | 28% | 8% | 17% | 8% | 0% |
| Trained, rifle (+2) | 42% | 17% | 28% | 17% | 3% |
| Veteran, rifle (+3) | 58% | 28% | 42% | 28% | 8% |
| Elite, rifle (+4) | 72% | 42% | 58% | 42% | 17% |
| Elite, aimed rifle (+5) | 83% | 58% | 72% | 58% | 28% |

Against plates with a rifle (net Armour 1) every cell moves one row up the table; against plates with a pistol (net Armour 2), two rows.

Full split, green rifle in the open: Miss 42% · Pinned 31% · Down 19% · Killed 8%. Note the natural-12 rule keeps the "0%" cells at 3% in play; the table rounds them down.

The shape is gentler than System A on cover (a green rifle keeps 17% into light cover) and harsher on long range, which matches the setting research: distance is what untrained shooters cannot overcome.

### Handling time
One roll: add two dice and one small number, subtract one number you were told at the start of the shot. Four seconds. The Difficulty is the only thing the defender has to state, and it is the same three words every time: "eight, plus two, cover."

### Strengths
- One roll resolves hit, wound and stress. No chain, nothing to look up.
- Everyone owns d6s and everyone intuits 2d6 (Fundamentals p.152).
- Headroom is built into the curve; you can price +1 flat and let the maths taper it.
- Range and cover live on the Difficulty, skill and stress on the roll: one side each, never mixed.
- Prototypes trivially in the existing 2.5D engine.

### Weaknesses
- Attacker-only: the defender never rolls. The book argues players want to roll the die that decides their model's fate (p.280); the audits argue the opposite for pace. This is the first question at the end.
- A +1 is not worth the same everywhere, so the costing engine must price against a declared reference difficulty (BattleTech's un-revisited to-hit assumption mis-priced every modifier by ~37%).
- Arithmetic. Small, but present on every shot.

---

## 3. System C — "Step-Up": polyhedral step dice, one target number, exploding aces

### The literal mechanic
A stat *is* a die: **d4** (frightened civilian), **d6** (militia), **d8** (trained), **d10** (veteran), **d12** (elite). Roll your stat die. **A 4 or better succeeds.** If the die shows its maximum, roll it again and add (it "aces"). Beating the target by 4 or more is a **raise**: the result steps up one row. A natural 1 on the first die always fails and jams Unreliable weapons.

| Result | Attack | Test |
|---|---|---|
| below target | Miss | Fail |
| target met | Pinned | Pass |
| raise (target +4) | Down, ignores armour | Pass with a perk |
| two raises (target +8) | Killed | — |

The one rule of modifiers: **the target number is the situation; the die is the person.** Situation: Long range +2, Light cover +1, Heavy cover +2, elevation demotes cover. Person: weapon Accuracy ±1 to the roll, Aimed lets you roll a d6 alongside and keep the better (a "wild die"), each Stress token steps your die down one size (d10 → d8).

### Shooting
1. Set the target: 4, plus range and cover.
2. Roll Shoot die (+ Accuracy; + wild die if Aimed). Aces explode.
3. If you met the target but did not raise, the defender rolls their **Armour die** (none: no roll; soft vest d4; plates d8; crude armour one size smaller) against the weapon's **Damage** (pistol 3, rifle 4, shotgun 5 at Short, anti-materiel 6): equal or better deflects the hit to Pinned; otherwise Down.
4. A raise skips the armour roll: Down. Two raises: Killed.

### Melee
Both roll Fight die + weapon (knife +0, bat +1, machete +1 and Damage 4, sledgehammer +2). Higher total wins and applies raises against the loser's total as the ladder; a tie is a scuffle (both Pinned). Charging: +2. Each extra attacker: +1.

### Tests
Stat die vs 4 (routine), 6 (hard), 8 (heroic). Rally: Nerve die vs 4 + Stress.

### Stress and morale
Each Pinned result or nearby friendly casualty is a Stress token and **steps every die down one size**. Below d4 the model Breaks. Stress literally shrinks you. Rally removes all Stress on a success.

### Damage
One wound; Down bleeds out; Killed is killed. Armour is a defender's roll every time a hit is not a raise, which is a second roll on roughly half of hits.

### Weapons and scavenged kit
Short / Long, Accuracy, Damage, traits. Unreliable jams on a natural 1 (which a d4 shows one time in four: scavenged weapons in civilian hands jam constantly, which is the setting).

### Growth and headroom
The die ladder is five steps (d4 → d12), then **d12+1, d12+2** as campaign-only advances. That is seven steps, plus the wild die for leaders, plus Accuracy on weapons. Where this system wins is the *shape*: a d4 civilian has a 25% chance to ace on every roll, a d12 elite 8%. **The weak beat the strong at fateful moments** (Fundamentals p.166), which is the closest any engine gets to "a kid with a shotgun in a stairwell."

### The numbers (chance the target goes Down or worse per shot, unarmoured)

| Shooter | Open, Short (TN 4) | Long (6) | Light cover (5) | Heavy cover (6) | Heavy + Long (8) |
|---|---|---|---|---|---|
| Civilian, d4 | 25% | 19% | 25% | 19% | 6% |
| Militia, d6 | 50% | 17% | 33% | 17% | 14% |
| Trained, d8 | 62% | 38% | 50% | 38% | 12% |
| Veteran, d10 | 70% | 50% | 60% | 50% | 30% |
| Elite, d12 | 75% | 58% | 67% | 58% | 42% |

Against plates (d8 armour die vs rifle Damage 4): d6 militia 27% in the open, d10 veteran 45%, d12 elite 54%; raises still get through.

### Handling time
One roll on a miss or a raise, two on an ordinary hit. Reading "did it beat 4, 5, 6 or 8" is instant; exploding dice add a beat.

### Strengths
- The most characterful engine: the die in your hand is the man. Training, stress and armour are all die sizes, no numbers to add.
- Exploding aces give the drama without a critical table, and they are heaviest on the weakest models, which is exactly the setting's texture.
- The defender rolls last on ordinary hits (armour die), which the book argues matters emotionally.
- Stress-as-die-shrink is a one-line rule with real teeth.

### Weaknesses
- Five die types, plus a d6 wild die. The book is blunt that this raises the barrier to entry and that d4s are physically unpleasant (p.153). Everyone must bring a full polyhedral set.
- The ladder is lumpy: a d8 cannot roll a 9 without acing; step-die vs target-number maths produces the odd non-monotonic cell (d4 into light cover is the same 25% as open ground, because a d4's only route to 5 is acing). Playable, but it will surprise people.
- Two rolls on about half of hits.
- The research already logged the Fistful of Lead quality-die as "proof the alternative ships fine, at the cost of needing three sizes of die" and kept it as a contrast case rather than a candidate. This is that road, walked further.

---

## 4. System D — "Face-Off": opposed d10 + stat, result by margin

The minimum-change route if a single d10 is a fixed point. The headroom fix is opposition: any stat value is meaningful as long as the other side's number is close to it.

### The literal mechanic
Stats **Shoot, Fight, Nerve, Wits** run 0–10 (green 2, trained 4, veteran 6, elite 8, campaign legend 10). The attacker rolls **d10 + stat + weapon**; the target rolls **d10 + Guard**, where Guard is 3 plus the situation. **Ties go to the defender.** Margin minus armour is the result:

| Margin − Armour | Result |
|---|---|
| 0 or less | Miss |
| 1–2 | Pinned |
| 3–5 | Down |
| 6+ | Killed |

Attacker natural 1 is a miss (jams Unreliable); attacker natural 10 adds +2 margin. The defender's die is the whole "save."

### Shooting
Guard = 3, +2 Long range (+4 beyond), +2 Light cover, +4 Heavy cover, elevation demotes cover, +1 sprinted. Attacker adds Shoot + Accuracy (rifle +1 Short / 0 Long, pistol +1 / −2, shotgun +2 / −2) + 1 Aimed − Stress. Armour: soft 1, plates 2, minus Pen. Point Blank uses Nerve.

### Melee
Both roll d10 + Fight + weapon; margin ladder on the loser; tie = scuffle. Charging +2, extra attackers +1 each.

### Tests
d10 + stat vs a flat 7 for routine tasks; opposed d10 + stat vs d10 + difficulty (3 / 5 / 7) for anything an enemy or the environment is actively resisting (hacking a defended node, climbing under fire). Rally: d10 + Nerve vs 7.

### Stress, damage, weapons
As in System B: −1 per Stress token, Break at Stress ≥ 2 + half Nerve (rounded up), one wound, Down bleeds out, Unreliable jams on a natural 1.

### Growth and headroom
Because every roll is opposed, a Shoot of 8 against a Guard of 9 (heavy cover, long range) is exactly as tense as Shoot 2 against Guard 3. Effectively 10 steps per stat, all meaningful. The difference of two d10s is a triangle distribution, so the top and bottom of the ladder taper gently rather than cliffing.

### The numbers (chance the target goes Down or worse per shot, unarmoured)

| Shooter | Open, Short (Guard 3) | Long (5) | Light cover (5) | Heavy cover (7) | Heavy + Long (9) |
|---|---|---|---|---|---|
| Green civilian, pistol (2) | 21% | 10% | 10% | 3% | 0% |
| Green civilian, rifle (3) | 28% | 15% | 15% | 6% | 1% |
| Trained, rifle (5) | 45% | 28% | 28% | 15% | 6% |
| Veteran, rifle (7) | 62% | 45% | 45% | 28% | 15% |
| Elite, rifle (9) | 75% | 62% | 62% | 45% | 28% |

Against plates with a rifle: green 21%, veteran 54%, elite 69% in the open.

Full split, green rifle in the open: Miss 55% · Pinned 17% · Down 18% · Killed 10%.

### Handling time
Two dice, two players, on every shot. Fast in absolute terms, but it is the pattern the audits singled out as the clock-killer, and it means the defender is always engaged in the attacker's activation.

### Strengths
- Keeps the d10 and the additive habit; solves headroom without touching the die.
- The defender rolls, every time, which is the emotional argument from the book.
- Opposed tests are the natural shape for hacking, stealth, and anything contested.

### Weaknesses
- Two dice per shot, both players, every shot.
- Modified dice-offs with modifiers on both sides "can quickly become difficult to comprehend or predict" (Fundamentals p.169). The Guard ladder mitigates it, but the player is still doing two sums.
- It is the least distinctive of the four; it plays like a tidier version of several existing games.

---

## 5. Side by side

| | A · Handful (d6 pool) | B · Margin (2d6) | C · Step-Up (step dice) | D · Face-Off (opposed d10) |
|---|---|---|---|---|
| Dice needed | 8–10 d6 per player | 2 d6 | full polyhedral set | 2 d10 |
| Rolls per shot | 1 | 1 | 1–2 | 2 (both players) |
| Arithmetic | none (count) | one add, one subtract | none (compare) | two adds, one subtract |
| Where cover lives | dice removed | Difficulty | target number | Guard |
| Where armour lives | downgrades result | subtracts from margin | defender's die | subtracts from margin |
| Green civilian, rifle, open / heavy cover | 48% / 17% | 28% / 8% | 50% / 17% | 28% / 6% |
| Elite, rifle, open / heavy cover | 78% / 60% | 72% / 42% | 75% / 58% | 75% / 45% |
| Growth steps before saturation | 9 dice × 2 thresholds | 8 on a taper, × result skills | 7 sizes, × wild die | 10, all meaningful |
| "Every hit does something" | native (ladder) | native (margin) | native (raise ladder) | native (margin) |
| Stress hook | −1 die per token | −1 per token | die shrinks | −1 per token |
| Defender rolls? | melee only | no (optional armour die) | on ordinary hits | always |
| Costing friendliness | dice are linear, cover is not | curve tapers for you; declare a reference Difficulty | lumpy | opposed: price against a reference Guard |
| Variance | high in small pools | low (bell) | medium-high (aces) | medium (triangle) |
| Distinctiveness | high | medium | highest | low |

---

## 6. Recommendation

**Lead with System B (Margin).** It is the only one of the four that hits every target in section 0 with a single roll of two dice everyone owns, and its headroom is a property of the curve rather than a cap you have to police: a +1 costs the same to buy at every level and is worth less at the top *automatically*, which is the exact behaviour every points system in the research had to bolt on by hand (OPR's doubling at 2+, BattleTech's taper, Rogue Trader's multiplier bands). The margin ladder makes "every hit does something" free, the Difficulty makes cover and range a three-word sentence, and result-shifting skills give you a second growth axis that is exceptions rather than numbers. It also drops into the existing 2.5D engine in an afternoon.

**Keep System A (Handful) as the live alternative** and prototype both. If table feel matters more than smoothness, A is the better game: it is the most physical of the four, it never asks for arithmetic, and the dice axis has near-infinite granularity. Its cost is variance in small pools and a cover effect whose value depends on the enemy's skill. A two-hour side-by-side with the same scenario will settle it faster than more analysis.

**System C** is the most evocative and the most expensive. If you would happily ship a game that says "bring a full set of polyhedrals," it deserves a look, because "the die in your hand is the man" and "stress shrinks your die" are rules people remember. Otherwise park it.

**System D** is the fallback if the d10 and the additive roll are fixed points. It solves the headroom problem cleanly by opposition, at the cost of two players rolling on every shot.

Two things I would carry into whichever wins:
- **Point Blank uses Nerve, not Shoot.** One sentence, and it makes room-clearing a nerve problem instead of a marksmanship problem, which is what the setting research says it is.
- **Elevation demotes cover a tier.** One sentence, and dense vertical terrain starts paying for itself.

---

## 7. Questions for you

Numbered so you can answer inline.

1. **One die type: hard rule or preference?** It rules out C outright and decides whether A (many d6) or B (two d6) is "one type."
2. **Should the defender ever roll?** B is attacker-only by default. I can add an optional armour die (defender rolls d6, 5+ deflects to Pinned, Pen raises the number) for one extra roll on hits only. The book says players want it; your audits say no separate saves. Which instinct wins?
3. **Down as a state:** do you want the three-step Pinned / Down / Killed ladder, or binary alive/removed with Killed rolled post-game? Down-and-bleeding is where the medic, the drag-to-safety and the "leave him" decisions live.
4. **Stress per model with an automatic bolt for cheap models, or a crew-level break?** Every system above assumes per-model tokens and a Nerve threshold.
5. **Cover as default?** The book suggests that in a cover-heavy game you make cover assumed and give a bonus for shooting at someone in the open. I built all four with cover as a penalty. Want the inverted version costed too?
6. **Elevation:** demote cover a tier only, or also a small shooter bonus for height?
7. **Point Blank on Nerve:** keep it?
8. **Scavenged reliability:** jam on the fumble result, cleared with an action, no ammo tracking. Acceptable, or too fiddly?
9. **Growth caps:** campaign stat cap (say +5 in B, 8 dice in A) or uncapped with super-linear cost?
10. **Typical model count per side and target game length?** Under about eight models a side and 90 minutes, A and B are equal; above that B's single roll pulls ahead.
11. **Should I prototype A and B in the 2.5D engine next**, same scenario, same density, and report kill rates, stress-break rates and rounds-to-decision?
12. The cliff notes of the design book are now in scratch; do you want them filed under `research/sources/fundamentals-tabletop-design/` with a curated vault note, so the hub can cite it?

---

## 8. Addendum (2026-09-05) — reading the Idea Dump against the four engines

`rules-vault/Ross' Idea Dump.md` landed on main after this doc was written. Two things in it change what the engine has to carry.

### 8.1 Monsters

If the setting takes the alien invasion, the engine must express targets that are nothing like a civilian: Workers and Kings with heavy chitin, regeneration and mass; Stalkers that are fast and armoured. That means **multiple wounds and armour beyond plates**, and the four engines are not equal here.

| | A · Handful | B · Margin | C · Step-Up | D · Face-Off |
|---|---|---|---|---|
| Heavy armour | **Breaks.** Armour downgrades the result; a 2-step downgrade turns even a Kill into Pinned, so no pool size can wound a Worker. Would need monsters modelled as extra Wounds with armour capped at 2 steps, or *Crush* to ignore it. | Arithmetic. Worker Armour 3 vs a rifle (net 2): green 8%, veteran 28%, elite aimed 58% per shot. Stalker Armour 2: green 17%, veteran 42%. | Armour die d10 or d12 vs weapon Damage; raises still bypass. Works, but a d12 armour die stops rifles nearly always. | Arithmetic, same shape as B. |
| Multiple wounds | Track Wounds; each Down result removes one. Fine. | Same. | Same. | Same. |
| Regeneration | Remove a Stress or Wound token per round; engine-independent. | Same. | Same. | Same. |

Measured against monsters, B's lead widens: the same one-roll rule that resolves a civilian shot resolves a rifle against a King, with *Crush* as "ignore armour" and *Precise* as +1. A needs a second armour model for anything past plates.

### 8.2 The weapon keyword vocabulary

The Idea Dump's keyword list maps onto each engine as follows. Where an engine has no clean home for a keyword, that is a cost of the engine.

| Keyword (Idea Dump) | A · Handful | B · Margin | C · Step-Up | D · Face-Off |
|---|---|---|---|---|
| DMG +N | +N Volume dice, or +N steps on the ladder | +N to margin | +N Damage vs armour die | +N to margin |
| Multishot N | +N dice (native) | roll N times, or +1 margin per extra shot | roll N dice, keep best | roll N times |
| Precise | +1 die | +1 to roll | +1 to roll | +1 to roll |
| Crush (ignore armour) | skip the downgrade | ignore Armour | skip the armour die | ignore Armour |
| Smash (−1 enemy armour) | armour downgrades one step less | Armour −1 | armour die one size smaller | Armour −1 |
| Cleave / Hack | +2 / +1 successes-equivalent, or +1 die | +2 / +1 margin | +2 / +1 Damage | +2 / +1 margin |
| Parry | −1 die to the enemy's Fight pool | −1 to the enemy's roll | enemy's die one size smaller | −1 to the enemy's roll |
| Block | armour +1 step in melee | Armour +1 in melee | armour die one size larger | Armour +1 |
| Reach / Push / Pull / Hook / Skewer / Throw | positional; engine-independent | same | same | same |
| Reload / Stationary / Limit / Load | action economy; engine-independent | same | same | same |
| Silent | detection; engine-independent | same | same | same |
| Fire / Template / Blast / Indirect | one roll per model in the area; A's pool makes this many pools, B and D one roll each, C one die each | | | |

Reading the rows: A and C carry the keywords as dice and die sizes, which is legible but coarse (there is no "+1 margin" in a pool; every keyword becomes a whole die). B and D carry them as small integers on one roll, which is exactly what the Idea Dump already wrote them as: DMG +1, +2, +3. **The Idea Dump's own notation is a margin system.**

### 8.3 Shared Threats

The Threat Counter (start 10, roll 1d10 each round from Round 2, a Shared Threat arrives on a roll above the counter, Loud actions lower it, quiet rounds raise it) is independent of the combat engine and works unchanged under any of the four. It does mean a d10 stays on the table even if combat is d6-only, which touches question 1.

---

## Appendix — outcome splits used above

All figures exact. "Down+" is Down or Killed.

**A (pool, 5+, ace = 2, unarmoured):** 1d Miss 67 / Pin 17 / Down 17 / Kill 0 · 3d 30 / 22 / 28 / 20 · 4d 20 / 20 / 27 / 33 · 6d 9 / 13 / 21 / 57.

**B (2d6 vs 8, unarmoured, rifle +1):** Miss 42 / Pin 31 / Down 19 / Kill 8. Same shooter vs Difficulty 10: 72 / 20 / 6 / 2.

**C (step die vs 4, unarmoured, Damage 4):** d6 Miss 50 / Pin 0 / Down 36 / Kill 14. d10 vs TN 6 in plates: 50 / 25 / 15 / 10.

**D (opposed d10, unarmoured, rifle +1):** green Miss 55 / Pin 17 / Down 18 / Kill 10. Veteran vs Guard 7 in plates: 55 / 30 / 12 / 3.
