# Rules Design Guide

**A working bench reference for drafting rules and diagnosing systems.**

Distilled from *The Fundamentals of Tabletop Miniatures Game Design: A Designer's Handbook* — Glenn Ford & Mike Hutchinson, CRC Press, 2025 (433pp). Hutchinson designed *Gaslands*, which is already in this project's research corpus, so this is partly the theory behind a game we've already mined.

Page citations are **PDF page numbers** of `Webscraper/data/books/fundamentals_tabletop_miniatures_glenn_ford.pdf`. Full chapter notes: `Webscraper/data/books/FUNDAMENTALS_CLIFF_NOTES.md`.

---

## 0 · How to use this

**This is not a summary of the book.** It is reorganised around the questions we actually ask mid-draft. If you know which question you're on, go straight to that part:

| If you're asking… | Go to |
|---|---|
| Should this be a rule at all? | **§2 — Does this belong?** |
| What is this rule *for*? | **§3 — Focus and drama** |
| How do I make this decision interesting? | **§4 — Decisions and resources** |
| How do I resolve it mechanically? | **§5 — Dice and probability** |
| What does this cost? | **§6 — Pricing** |
| Why is this breaking? | **§7 — The failure catalogue** ← *the diagnostic half* |
| How do I write it down? | **§8 — Rules-writing craft** |
| Scenario / campaign / list question | **§9** |
| We're stuck | **§10 — Provocations** |
| What's the word for…? | **§11 — Vocabulary** |

**Two conventions used throughout:**

- **`→ Settlements:`** flags where we already have a standing answer. These are **pointers, not copies** — `Rules System/Full Rules System v1.md` and `AGENTS.md` are the authorities. If this guide and the master note disagree, the master note wins and this file is owed an edit.
- **⚠** marks a place the book's default is *wrong for us*, with the reason.

**A warning the book puts on itself,** worth putting on this guide too (pp.420–421): a design that *"simply reorganises common mechanical tropes into a new order… is unlikely to be an effective design. Effective game design tightly integrates its core ideas with mechanics to shape the players' experiences."* None of what follows generates a good rule. It stops you writing a bad one.

---

## 1 · The ten laws

The load-bearing principles. Everything else in this guide is downstream of these.

---

### 1. A game is about whatever its mechanics cause players to focus on.
**(p.120)**

Mechanical detail is a camera. **Detail slows the action and zooms in; abstraction speeds it up and widens the shot.** Adding rules to a moment tells players that moment matters. Simplifying or automating a moment tells them it doesn't.

So the question for any new rule is never "is this realistic?" — it is *"do I want the player's attention here?"* If the answer is no, abstract it or delete it.

> The book's worked case (p.119): *Harpoon* is arguably the best public naval simulation, and it has **no rules for adjusting sonar frequency** — because a fleet commander is disconnected from that activity. Larry Bond: *"A game must show the players the **significant** details, and ignore the rest."*

---

### 2. Whatever loop players run most often must be the most fun part.
**(p.75)**

> *"Our games are not about what we believe, intend or say they are about; they are about what our players spend their time doing and thinking about while playing them."*

Diagnostic, not aspirational: count what the players actually do most. If the most-repeated action is bookkeeping, arithmetic, or looking things up, the game is about bookkeeping.

---

### 3. Victory conditions are a signpost, not a scoreboard.
**(p.89)**

They are the main way you tell players what you want them to do. If your rules point one way and your victory conditions point another, **the fault is yours, not the player's**:

> *"you cannot abdicate responsibility to the player for playing your game 'wrong': you must align the victory conditions with the actions in the game you wish players to take."*

The four-step method (p.90): find the fun → identify what engaging with it achieves → playtest for what a *skilled* level of that achievement looks like → make that the victory condition.

`→ Settlements:` objective-primary, never kills; scoring every End Phase from Round 2. Locked and endorsed by the book (§9.1 below).

---

### 4. Write rules against what is no fun but advantageous. Never against what is no fun and disadvantageous.
**(p.95)**

The single best filter for whether a restriction earns its rules text. If a behaviour is boring *and* bad for the player, they will stop doing it without your help — a rule against it is pure overhead.

---

### 5. Make undesired play weak, not illegal.
**(p.90)**

> *"make such things weak. This can be as simple as withholding extrinsic rewards for undesired behaviour."*

And weakness is a **safe error**: if you mistakenly weaken something that turns out to be fun, that's fine — *"Many systems have legendarily enjoyable non-optimal choices that players are not only happy to engage with but they also take doing so as a mark of pride."* A prohibition has no such safety margin.

---

### 6. If a resource never runs out, delete it.
**(p.213)**

> *"If the resource never stops a player from triggering its action, it should be removed."*

Test: if a player takes the gated action every time it's available and the gate rarely bites, you have added bookkeeping and nothing else.

---

### 7. Control removal must not require player choice — but must be bracketed by player choices.
**(pp.272–273, 340)**

Two halves that seem contradictory and aren't:

- **During** the uncontrolled action, no choice: *"set a target point, usually the closest edge of the playing area, and demand that movement be directed towards this point."* Otherwise players agonise over whether to act in their own interest or in the spirit of the simulation.
- **Around** it, choices: let a player spend a resource to avoid it, make it conditional on a positional decision, and *"require an intentional choice by one player to inflict the control removal effect on the other player rather than having it be a natural side-effect."*

> *"Players like to be in control. A game is a series of interesting choices, and the removal of control means the removal of choices."* (p.340)

---

### 8. Reduce effectiveness as range increases.
**(p.35)**

> *"When a rule allows force projection over a great distance, its average effect on the game should be less than force projection over a short distance. Close combat should be more reliably able to remove units than ranged attacks, and close combat from slow-moving units should be more reliable than that of fast-moving units."*

Two axes, not one: reliability falls with **range**, and also falls with the attacker's **speed**.

---

### 9. Perfect balance is not the goal. Forgettable is the sin.
**(pp.404, 415)**

> *"If all options are exactly as good as all other options, there is no advantage to or meaning in a player's choices; they would do just as well to flip a coin as make a decision. Poorer options allow players to make good choices."*

> *"weak choices are not bad game design; forgettable choices are. It is far more interesting and beneficial to put in a piece of an engine that doesn't work but that looks like it could than another cog that does exactly the same job as five other perfectly good cogs."*

**But note the floor:** weak is fine, *negative* is not. An option that is strictly worse than the default it replaces isn't a choice at all.

---

### 10. Design the exchange of game state you want.
**(p.252)**

> *"as a player, I take actions to modify the game state, and then I hand control over to you, hopefully having created a game state that presents a tactical or strategic puzzle for you to overcome."*

**Big exchanges** feel strategic and premeditated, but passive for the inactive player. **Small exchanges** feel urgent and reactive, but resist complex puzzles. Neither is right; the choice determines whether your game reads as strategic or tactical.

---

## 2 · Does this belong in the game at all?

### The three affordances test
**(p.40)**

A non-discrete miniatures game earns its form only when it exploits all three:

1. **Spatial relationships** between markers are the primary interest.
2. **Diverse physical objects** can be accepted and expressed (the *shoe test*, p.21 — put a shoe on the table; a real miniatures game gives it cover, LOS-blocking and movement rules; *Monopoly* just breaks).
3. **Tolerance for complex and loose rules** — players accept far more complexity and far more ambiguity here than in a boxed game.

**The disqualifier (p.41):** *"if your desire is to create a game in which the rules remain precise and unambiguous at all times, miniatures games are a poor medium."*

**The drift warning (p.44):** *"each choice you make to abstract some part of the movement, position, orientation or perspective of the miniatures potentially pulls you away from leveraging the form to its fullest."*

### The complexity budget

- **Never ask a player to track more than nine units** — Miller's 7±2 (p.136). Past a dozen models in development, start grouping.
- **Fungible spending options:** cap at **3–4** if several option-sets appear per round; **6–10** if only a few do (p.211).
- **A genuinely tricky spend decision a couple of times each round** (p.212). More risks analysis paralysis; fewer means the resource is idle.
- **Component reasonableness ladder (p.50):** dice, tape measures and markers — fine. Printed reference cards and assorted markers — probably. Bespoke cards indistinguishable face-down, touch-identifiable pieces, specifically-shaped tokens — **publish a box instead.**

### The must-run-out test
See **Law 6**. Applies hardest to non-fungible resources: ammunition, charges, limited-use items.

### Prefer fungible to non-fungible
**(p.212)**

> *"it is always worth considering whether a non-fungible resource can be redesigned into a fungible one to increase the density of decisions and compromises available to the player."*

A non-fungible resource asks only *when* to spend. A fungible one asks *whether* to spend it here or there — a strictly richer question.

`→ Settlements:` the anti-bloat tenet is the local form of this whole section. Cut so far: Water upkeep, per-head upkeep, Heat/Attention, HP-based structure damage, worker Proficiency, the Seeker mine chassis. See `AGENTS.md`.

---

## 3 · Focus and drama — what is this rule *for*?

### The objective ↔ subjective axis
**(pp.114–115)**

- **Objective** — recreate the steps of causal reality, each link in the chain, equally weighted. *Harpoon*'s golden rule: *"Nothing may be done contrary to what could or would be done in actual war."*
- **Subjective** — hit the beats that tell the story; skip what doesn't matter, magnify what does. *Frostgrave*'s golden rule: ask *"What would happen in the movie?"*

Neither is better, they are not exclusive, and **you need not apply one uniformly** — one subsystem can be objective while another is subjective.

**Detail and objectivity are separate axes (p.117).** A subjective design can be *more* detailed than an objective one, if the moment looms large in the protagonist's experience.

### The input/output rule
**(p.118)**

> *"if the detail of output exceeds that of the input, it will create a sense in players that the game is 'playing itself' and that their input has relatively little weight."*

Do not generate a rich, graded outcome from a thin decision.

### Fail forward
**(pp.77–78)**

Failure that changes nothing is the weakest possible result. Make failure *do* something:

- *Rogue Planet* — a failed action gives the opponent a free move.
- *Gaslands* — failing to control your vehicle **forces** you to move, possibly into a collision.
- *Warhammer* — a stone thrower that misses scatters, possibly onto your own troops.

`→ Settlements:` **every hit does something** — a hit wounds *or* delivers its payload, and a failed wound becomes Stress. Locked, and this is the book's own principle.

### Make things behave as the fiction promises
**(pp.109–110)**

> *"Merely describing a given weapon as a grenade will not cause it to function as a narrative generator. It must carry with it a set of rules that cause results like grenades."*

If a name promises an effect the rules don't deliver, the name is doing no work and the dissonance costs you the diegetic pleasure entirely (p.77).

### Connect and correlate events
**(pp.107–108)**

- **Connect:** if a dying model just vanishes, the event is *"isolated and inert."* Let it panic neighbours, or leave ammo, or leave a stain — anything the next system can read.
- **Correlate:** players will invent causation from mere proximity in time and place. *SSO* has two entirely independent event sets — one drives players outside, one shuts the airlock — and players reliably invent an AI conspiracy connecting them. **You get narrative for free by co-locating unrelated systems.**

### Leave gaps, but shaped ones
**(p.110)**

> *"If a player's imagination needs to cross a gap, the player will own the gap."* — But: *"players proverbially filling in the frames between the panels of a comic book is good, and creating a story from a pile of randomly discovered pictures is bad. **There should be clarity and intention even in your gaps.**"*

---

## 4 · Decisions and resources

### The four axes of a resource
**(p.209)**

Classify every resource on all four before writing its rules:

| Axis | Meaning | Example |
|---|---|---|
| **Fungible / non-fungible** | Can it be exchanged for a range of outcomes? | Activation points / ammunition |
| **Positive / negative** | Does the player want it? | Command points / wounds |
| **Recoverable / not** | Does it come back, and how? | Actions (auto) / wounds (rarely) |
| **Scope** | Per-unit, or force-wide? | *Infinity*'s force-wide AP pool |

### Negative resources — the discipline
**(p.214)**

They work when they are **either the downside of an active beneficial choice, or inflicted by an opponent's choice**. And:

> *"They should alter a player's decision space by adding or changing options, not simply reduce that decision space."*

> *"We require players to suffer from having their toys removed from their game incrementally over a play session against their will; we should be careful about forcing them to have them exhausted, poisoned, burned and driven insane against their will as well."*

Model to copy: *Gaslands* hazard tokens — you accept them **voluntarily** to climb gears, and there are multiple ways to shed them.

### Recovery sets your tempo
**(p.215)**

> *"In many ways, a round is just the point at which activation point resources recover. You can create a rhythm in your game by dictating when resources recover and how."*

**Action-based recovery has three costs:** it drops tempo (an action spent on bookkeeping, not board change); it competes badly against high-value fungible resources (reloading on the second-to-last turn is hard to justify); and player behaviour varies wildly, which upsets balance.

### Loss aversion
**(p.216)**

People overvalue what they already hold, so a one-off pile of resources handed out at game start **will still be sitting there at the end** — even when it has no scoring value and no purpose but to be spent.

Two fixes: **give a little each round rather than a lot at the start**, and **clear unspent stock at end of round.**

### Catch-up: value curves, never handouts
**(pp.216–217)**

> *"It might be tempting to simply give the lagging player additional resources, but this runs the risk of feeling like unearned 'pity points' to the recipient and like an unfairness in the game to their opponent."*

The right shape: a **universally available** option whose value naturally rises for whoever is behind. *Gaslands*' audience votes let a vehicle change gear out of activation — near-worthless if you're doing well, the difference between one activation and five if you're struggling. **Same rule for everyone; different value by position.**

⚠ `→ Settlements:` the underdog's **+1 Priority** is a small handout rather than a value curve. It is defensible (it compensates for swarm output at fixed WND 1) but it is the handout shape, and it governs *who goes first* rather than *who has the last word* — which is where objective VP actually lands. Flagged in the assessment, not yet ruled.

### Keep the decision space wide
**(p.163)**

On rerolls: the standard rule (the new result stands) *"narrows the player's decision space, such that they will only reroll a result that is a definite failure."* Consider letting players return to the pre-reroll result.

And on whose dice (p.164): *"players have a strong proprietary relationship towards the rolls that they made"*, and *"players will likely react more strongly to losing a success than to their opponent averting a failure, even if the two have the same effect."*

---

## 5 · Dice and probability

### The four shaping mechanics
**(pp.156–162)**

| Mechanic | What it gives you | Watch for |
|---|---|---|
| **Cumulative odds** (roll N+) | Simplest control; D6 gives ⅙ ⅓ ½ ⅔ ⅚ and nothing between | Only five graduations of skill on a D6 (p.152) |
| **Dice pools** (count successes) | Near-infinite granularity, no extra table time, tactile | **Only smooths if the pool holds at least as many dice as the die has faces** — 12 or 18 D6 are stable; nobody owns 40 D20 (p.159) |
| **Dice combinations** (2D6) | A bell curve and a 2–12 range from two dice | A +1 is worth more near the middle target — a deliberate **headwind on strong characters** (pp.160–161) |
| **Nested rolls** (hit → wound → save) | Very predictable outputs from few stages | **Two or three stages is enough**; each stage is table friction |

### Choose for feel, not just probability
**(pp.155–156)**

Two systems, both averaging five damage:

- **20 D6 at 4+, then 4+ again** — feels like a scrum of individuals, strikes and parries; an average result is likelier; **but it can produce nothing at all.**
- **1 D10, rerolling 10s** — feels like a single decisive strike; **some damage always happens**; far greater variance.

> *"Mechanics are the medium by which the art of a game is created."*

### Roll-over-plus-stat
**(p.157)**

> *"If you wish for both high statistics and high rolls to be advantageous in your game, consider having players roll over a set target number, adding the statistic in question, rather than rolling under a statistic."*

`→ Settlements:` `1d10 + Stat + Modifiers vs 7+`. This is the book's own prescription.

### Modifier discipline
**(p.164)**

- **Apply modifiers to one side only.** *"If one modifier is added to a dice roll, another should not be subtracted from a target number."*
- **Cap them.** The book's two named taming methods are *"capping modifiers at +/−3"* and reserving natural rolls as automatic success/failure.
- **More than a couple, and players can't recall them** — plan how they're accessed at the table.
- Automatic success/failure **reduces granularity** by voiding any modifier stack large enough to flip the natural result (p.165).

`→ Settlements:` ±3 cap **and** natural 1/10. Both of the book's methods, verbatim.

### The "feels elite" trick
**(p.162)**

Give a model a large bonus on the **first** roll of a nested chain — they almost never miss, so they *feel* extraordinary — then claw it back with a modifier on a later stage so real output stays ordinary. Perception and power, decoupled.

### Criticals and fumbles
**(pp.165–166)**

Beyond auto-pass/auto-fail, consider **success with a twist / failure with a perk**: a fumble that opens the door but alerts the guards. Named study: Powered by the Apocalypse, Fantasy Flight's Narrative Dice, Modiphius's 2D20.

**Consistency rule:** *"if each test comes with a different fumble and critical additional effect, the result can be difficult to recall for players."*

### Five sources of uncertainty
**(p.140)**

Performative (dexterity, distance estimation) · Social (concealed information, unknown intent) · Complexity · Process (things hidden by the game itself) · **Stochastic** (dice).

> *"The primary disadvantage of luck is that you can have too much of it. An excess of the other methods mentioned simply changes what game is being designed, but an excess of luck destroys a game."* (p.147)

Because luck is so cheap to insert, its presence must be *"a distinct and clear design decision"*, not a default. Recommended division of labour (p.148): **luck as the workhorse, a handful of key interactions on dexterity or concealed information.**

**Input vs output randomness (p.147):** input randomness hands you resources to plan with (feels strategic); output randomness makes you weigh a risk and then find out (feels dramatic). Pick per subsystem.

---

## 6 · Pricing

### Start arbitrary
**(pp.404–405)**

Set your average unit at **10** if it is a small particle (a warband minion with a couple of items) or **100** if it will carry more variation (a squad with members, commands, upgrades). Then: *"don't fall into the trap later in your design of thinking they hold some absolute truth."* If you need more room between options, **double every value.**

### Anchor on damage ratio
**(p.405)**

*"if an elite unit can kill two of your 100-point average units over the course of a game, the elite unit can have its point cost set at 200 points."* Rough, but a fast sanity check on any derived number.

### The over/under iteration rule
**(p.406)**

If a unit priced at 100 looks too expensive and you suspect it's worth 90, **price it at 80** on the next pass. Three reasons:

1. **Search space.** Learning it's still too dear at 90 only narrows "<100" to "<90" — 90 candidates left. Too cheap at 80 collapses the range instantly; too dear at 80 saved you a whole iteration.
2. **Test coverage.** *"making a choice more tempting to your playtesters will mean that it gets looked at more."*
3. **Fun signal.** *"If a given option isn't fun for the person using it when it's overpowered, it's unlikely to be fun when it's well-balanced."*

### Massed guessing
**(pp.406–407)**

Two harvesting methods, both cheap:

- Ask players to rate units **1 to 5** and average, producing an alternative multiplier to your computed one.
- Ask players to build **two opposing forces they consider fair, without knowing which side they will play.** Aggregate enough of these and *"highly accurate point ranges can be arrived at."*

`→ Settlements:` everything currently prices on `hold_claim`, one of five scenarios and the most static — a known bias in `AGENTS.md`. Blind two-force builds are an independent human cross-check on exactly that axis.

### Why the naive model fails
**(pp.403–404)**

1. **Statistics sit on a curve, not a line.** *"if each point an attacker's strength is greater than a defender's toughness modifies a roll by plus one, then the seventh point of excess strength is useless."* Therefore *"statistics used in opposed tests can never be said to be worth a set number of points."*
2. **Units synergise within an army.** A lone shooting unit in a melee force is worth less than the same unit in a shooting force.
3. **Player psychology.** A melee-minded player will not use a ranged option well no matter what it costs.

`→ Settlements:` the measured stat ladder (one-sided stats saturating 20/15/15/10/10/5; opposed stats flat at 15) is exactly point 1, measured rather than asserted.

### Price synergy components individually
**(p.411)**

> *"each skill is fairly priced on its own, so when they are bought together, the synergistic effect is an essentially free bonus ability that is given to a player as a reward for spotting the combination."*

Do **not** surcharge combinations. The combo is the payoff for list-building skill.

### Force organisation is extrinsic
**(pp.409–410)**

> *"while list-building restrictions are an effective tool for requiring mixed forces, they are an extrinsically imposed one, and it may be of interest to consider if our game designs can motivate the same player choices in a way that is more emergent from the rules mechanics or the game's victory conditions."*

Standing question for any new slot rule: *could a victory condition produce this force shape instead?*

---

## 7 · The failure catalogue

**The diagnostic half of this guide.** Symptom → cause → fix.

| # | Failure | Symptom at the table | Cause | Fix | Cite |
|---|---|---|---|---|---|
| 1 | **Alpha-strike** | One player's first turn makes the game unrecoverable | Full Force Activation lets a whole army act before any reply | Interrupt the turn on a failed action (*Blood Bowl*); or **defer all model removal to a phase after every activation** (*W40K Apocalypse*) | pp.241–243 |
| 2 | **Activation advantage** | The model-rich player sees everything and scores last | Single Unit Activation, unequal model counts | Allow **passing** so the outnumbered player banks activations; or order systems; or an equal activation allowance regardless of model count | pp.246–248 |
| 3 | **Points-removal snowball** | An early lead compounds; the game is decided by turn 2 | Troopers *are* victory points, so the leader has more means to score | **Decouple VP from wounds** so activations must be split between killing, scoring and resourcing | p.358 |
| 4 | **Campaign snowball** | The better player wins, gets more, wins more | Progression rewards the winner | **Headwinds** (escalating or maintenance costs) *"slow the problem down rather than fixing it"*; or detach winning from progress; or make advancement grant **choices, not power** | pp.391–393 |
| 5 | **Learned helplessness** | Players stop iterating their lists | No visible counter exists to an early dominant strategy | *"All a game designer needs to do is show once or twice that there are solutions within the system."* Seed a first layer of answers | p.412 |
| 6 | **Ability bloat** | Nobody knows what the opponent can do | *"when every unit has multiple special rules, they start to just be the rules"* | Cap the total; fold similar capabilities into a **central standardised list**; reuse terminology so related rules are named alike; cap combinatorial exposure structurally (*Gaslands*: two menus of six perks) | pp.367–368 |
| 7 | **Dead-zone terrain** | A terrain piece is never entered by anyone | Its effect is predictable and bad, so it may as well be impassable | **Randomise or hide** the effect; or invert — make the penalty baseline and add *accelerating* terrain instead | pp.317–318, 325 |
| 8 | **Miss-a-go** | A unit spends multiple activations mired in rough ground | Halving movement is convention, *"ubiquity doesn't equate with excellence"* | Randomise the reduction; use non-movement effects; or make slowing a **choice** with damage as the alternative | p.317 |
| 9 | **Un-terminating threshold** | The leader disengages and runs the clock | A success threshold that doesn't end the game | Make the threshold **end the game**, or pair it with an objective that's easy to take if the enemy disengages | pp.91–92 |
| 10 | **Default-win asymmetry** | One side's optimal play is to do nothing | *"the defender wins if the attacker fails to breach the walls"* | Give **both** sides asymmetric but **active** objectives | p.92 |
| 11 | **Defend-your-own-zone** | Both armies sit still | Symmetric objectives inside one's own deployment zone | A time limit forcing aggression, or a secondary objective that breaks the tie | p.92 |
| 12 | **Summon short-circuit** | A late summon steals a hold-the-point objective | Units not present all game can score it | Curtail summoned units' ability to hold; normally **give them no inherent VP value** | pp.92, 349–350 |
| 13 | **Walk-off** | A leader strolls off the table to dodge an assassinate condition | Voluntary exit unaccounted for | Write the off-table rules explicitly — multiplayer scoring, partial-unit exits, pursuit, re-entry, forced vs voluntary | pp.93, 223–224 |
| 14 | **Artificial end-game** | Units turn their backs and run to empty table quarters in the last round | A publicly known fixed round count | **Semi-random ending:** roll a D6 at end of round, add the round number, end on 10+ — then check the variance against your round length | p.354 |
| 15 | **Analysis paralysis** | Turns take forever | Too many simultaneous options, or perfect information | 3–4 options if many sets per round; a few judicious dice rolls make perfect calculation impossible | pp.144, 211–212 |
| 16 | **Loss-aversion hoarding** | Resources sit unspent at game end | A one-off allocation the player may choose not to spend | Give a little each round; clear excess at end of round | p.216 |
| 17 | **Locked sweetshop** | Players resent visible-but-unreachable content | Progression gates content players can read but not use | Let players **target** specific unlocks; marry them to narrative acts (a *duellist* ability for killing named characters) | p.394 |
| 18 | **Buried treasure** | The best synergy is never discovered | Combos are hidden rather than signposted | *"abilities that clearly reference each other, elements that become cheaper when bought together or parts that directly name other units"* | p.414 |
| 19 | **Campaign drop-out** | The losing player stops showing up | A ninety-minute session is a much bigger ask than a lost half-hour | Escalate late-campaign scoring so early losses matter less; avoid plain leagues; end on a climactic scenario with roles for lower places | pp.384–386 |
| 20 | **Degradation into chore** | A damaged unit is activated only out of duty | Degradation removed its options *and* its mobility | **Protect movement above all** — a mobile unit is still a distraction, speed bump and objective-claimer; keep degraded admin no heavier than healthy admin | p.347 |
| 21 | **Refusal frustration** | A unit does nothing, and the board doesn't change | Refusal removes an action without altering game state | *"possibly even more controversial than fleeing"* — offer avoidance options, or make the failure change the board | pp.335–336 |
| 22 | **Meaningless flight** | Fleeing is pure bookkeeping | Ongoing flight state with no rallying | Rallying is **mandatory** where flight persists; without it, *"units that begin to flee are potentially better simply removed from play"* | p.335 |
| 23 | **The balcony problem** | Abstract LOS breaks the moment anyone climbs stairs | A base-to-base line assumes a 2D plane | State **exactly where the line is drawn from**; expect to patch repeatedly; or accept model's-viewpoint LOS for vertical terrain | pp.293–295 |
| 24 | **Conga line of dice** | Models trail dice around the table | D6-based status tracking that exceeds six | Design the tracking explicitly; don't let a status exceed the die | p.170 |
| 25 | **Bag building** | Players game the activation bag | Pull systems let players control bag contents | Limit player control of the bag if you want even randomisation | p.171 |
| 26 | **Procedural blow-out** | A rare scenario combination is broken | *"testing each of even a hundred possible combinations is a huge task"* | Accept it, or reduce the combinatorial space; pre-written scenarios test far better | p.377 |
| 27 | **Forgotten mid-game rule** | A scenario special rule never fires | It triggers on nothing the players already check | **Trigger off a state change** (entering the terrain triggers the terrain check), or fix it to a set point in the round | p.379 |
| 28 | **Ludo-narrative disharmony** | Players win by doing the un-thematic thing | Rewards and fiction point different ways | Make unthematic actions *"expensive, ineffective or have undesirable consequences"* | pp.83–85 |

---

## 8 · Rules-writing craft

### Ship a golden rule
**(pp.124–125)**

A non-discrete game **must** supply a catch-all for disputes, because vagueness is structural — real-space measurement, LOS across dense terrain, homemade terrain boundaries.

Two forms, and the book has a preference:

- **Dice-off** (*Warhammer*: 1–3 player A, 4–6 player B) — fair, but *"will result in two different rule interpretations being correct in two different instances."*
- **A consistent principle** (*Gaslands*: *"choose whichever option results in the most carnage for all concerned"*) — **preferred**, because it resolves identically at every table **and declares design intent at the same time.**

Boundary (p.125): it covers *"the cracks where non-discrete theory meets practical miniatures and tabletops, never as an excuse to leave loopholes or create contradictory rulesets."*

⚠ `→ Settlements:` **we have no golden rule.** Grepped and confirmed — precedence rules exist for *which note wins*, nothing for which *player* wins at the table. Open decision.

### Define line of sight explicitly
**(pp.287–288)**

> *"It is surprisingly common to find systems in which the author fails to define what they intend the LoS rules of their game to be, leaving it to a kind of presumed folk wisdom. Do not do this."*

And never tautologically: *"'For a model to have line of sight to another it must be able to see it' does not tell your players how you expect them to adjudicate LoS."*

Also **tell players which fiction they inhabit** (p.290) — ground-level general with imperfect information, or omniscient commander with total battlefield visibility. This settles most LOS arguments before they start.

### Put in-world commentary *before* the rule
**(pp.100–101)**

Normally, avoid commentary in rules text — it buries the operative sentence and risks restating the rule with a variation. **Minor conceits are the exception**: where a rule's in-world logic isn't obvious, a line of framing placed *before* the mechanical description measurably aids comprehension and recall.

### Never reference a pre-movement position without requiring a marker
**(p.273)**

> *"referencing a unit's position prior to movement should only be made if reference is also made to marking the position prior to physically moving the unit. A safer option is to base the placement on other units and elements."*

### Stacking must be explicit and consistent
**(pp.368–369)**

> *"if a buff increases a dice roll by one, should having five of them on one unit make all six-sided dice results successful?"*

Recommended middle path: **allow stacking, but not from the same source.** Whatever you choose, apply it uniformly — *"Allowing some effects to be stacked but not others can lead to overly powerful edge-case combinations and moments of frustrated surprise in play."*

### Passive abilities need consistent check-points
**(p.370)**

Don't expect players to check every possible state change. Fix passive triggers to a small set of moments: *"at a certain range, when an opposing model activates, or when an opposing model attacks."*

### Special abilities: impossible actions, not bigger numbers
**(p.363)**

> *"Ideally, special abilities do not simply increase existing numbers (five goes to six), but offer access to otherwise impossible actions or options (flying in a game in which most things walk on the ground)."*

The worked test (p.371): for *"the greatest sniper in your universe"*, a higher accuracy stat *"leads to the sense that they are just on a sliding scale."* Multiple shots, or automatic hits in defined situations, makes them **unique**.

**Method for building the palette (p.367):** take each of the game's rules areas in turn and write abilities that break *that area* in an interesting way. Cluster the results into faction or "lore" menus.

### Name the reused chassis once, and keep the name
Reskinning one mechanism under new names per supplement forces every reader to independently notice the equivalence. *(Drawn from `EQUIPMENT-RESEARCH.md` §31 — Necromunda renamed one Territory chassis five times.)*

### Saves exist for emotional reasons
**(p.280)**

> *"a '5+ armour save' has the same probability as a '3+ to wound'. However… many players prefer to roll the final dice that decide their trooper's fate and will miss the chance if it is not present… games are often a power fantasy, and having your units taken off without being able to do anything makes people feel impotent."*

⚠ `→ Settlements:` the **attacker** rolls the Injury roll. Melee is opposed and Dodge is a resourced reaction, so those give the defender a die — but a **ranged kill is entirely attacker-rolled**. Deliberate (no second dice type, pace). Flagged as a table-test question, not a defect.

---

## 9 · Scenarios, campaigns and lists

### 9.1 Ending and winning

**Deriving preset game length (p.353):** estimate from average speed, range, damage output and starting distance how many rounds it takes for engagement to begin and resolve. **Take that number and subtract one.**

**Combine end conditions (p.356).** The canonical formulation: *"the game ends when one player has three victory points, or when only one player has units in play, or at the end of round five, whichever is sooner."* Pure player control risks a session that is problematically long or short.

**Score at intervals, not only at the end (p.356).** *"if scoring occurs at multiple points in your game, an ultimate loser can still potentially have the fun of having been the winner for a stretch."*

**Victory condition types:**

| Type | Strength | Weakness |
|---|---|---|
| **Points removal** | Instantly legible; builds on list-building knowledge | **Snowballs** (§7.3); tells only one story — a war of attrition; counting is fiddly; doesn't guide behaviour, since players kill anyway |
| **Interactive objectives** | Highly narrative, reversible, catch-up built in | Needs rules not inherent to the core loop |
| **Positional objectives** | Dynamic, simple, tells a story | Middle ground on both axes |
| **Hidden / asymmetric** | Bluff, counter-bluff, verisimilitude | **Risk: two players with no reason to interact.** Guarantee every generated combination forces contact |

**Don't ship a simplified tutorial victory condition (p.360)** — it produces a disappointing, unthematic first-touch experience.

`→ Settlements:` objective-primary; scoring each End Phase from Round 2; ends on round 6, objective completion, or wipe; Escort is asymmetric. All four endorsed above.

### 9.2 Scenarios

**Four standard parts (p.378):** set-up · special rules · game end · victory conditions.

**Rule of thumb for generating one (p.380):** *"start differently and end as usual, start as usual and end differently, or start and end as usual but have something unusual in between."*

**For pick-up play (p.376):** *"put a lot of the scenario's elements into its set-up conditions."* Set-up is public, co-operative, scrutinised jointly and done once; victory conditions are studied **privately** and so need exceptional clarity.

**For hobby projects (p.376):** you can be much bolder, because everyone read the scenario in advance and built for it — *"the aim is to offer the chance to engage in extra hobby projects, not to demand them."*

**Deployment zone variants (pp.229–232)** — free variety, minimal rules text: different shapes (L-shaped enables flanking and enfilade; a spur enables vanguards) · split, contiguous or interleaved · asymmetric (*"one of the fastest methods of creating a tabletop narrative"*) · shared (a starting grid — but only where victory isn't destruction, else you get an immediate brawl) · unanchored (place a token, deploy within X of it).

**Compensating asymmetry (p.231):** the more widely spread player is favoured where flank/rear bonuses or heavy shooting exist. Even it with **defensive structures, a points advantage, or asymmetric victory conditions** — not by shrinking the zone.

### 9.3 Campaigns

**Three distinct things get called "campaign" (p.383):**

1. **Meta-scoring** — compare results across games (tournament, league).
2. **Structuring** — link games into a narrative (sequential, or map/node).
3. **Progression** — forces change and grow.

**Design against drop-out first (pp.384–385):**

> *"It's one thing to expect a player to engage with an additional half an hour of play once they know… that they've lost… It's quite another to expect a player to… play through ninety minutes knowing that they've lost the war no matter what they do, particularly when they have days or weeks to think about it."*

**Sequential campaign shapes (p.387):** branching (exponential scenario count) · contained (linear, cheap, but winning every game ends the same as winning one) · **converging** (branches re-merge, so *N* wins in any order lands the same) · **sprouting** (a contained spine with alternative lanes at pivot games). Converging and sprouting are the practical middle.

**Map campaigns (p.390):** *"skills within the meta-game of developing locations and controlling the map should not overrule the skills at the tabletop."* Let the map shape **who fights whom and under what conditions** — not army availability.

**Negative progression (p.393):** injuries add real weight to unit loss, but watch two things — the **double punishment** (a loser gets fewer rewards *and* takes scars), and **narrative dissonance** when a model described as pulped makes a full recovery on the injury roll.

### 9.4 List building

**Statistics come in eight types (pp.398–402):** physical · intangible · target number · indirect (formula/table) · **modifier** · dice-type · comparative · cost.

**The evolving meta (p.412).** After a loss a player either **routes around** the winning list or **copies** it. Both paths must stay interesting:

- Against routing: seed visible counters to the obvious openers (§7.5).
- Against copying: make the core system interesting to operate for its own sake, **and make maximisation fragile** — *"If each unit has a rock, paper, scissors effect and both players choose to maximise their rock units… it shouldn't be too long until someone brings an all-paper army."*

**Build-at-the-table lists** (*Malifaux*, *A Billion Suns*) push tactical play but cost you the away-from-table meta-game, the session time, and — for a game whose main strategic claim *is* list building — most of that claim (pp.413–414).

---

## 10 · Provocations

The book ends most chapters with **Experiments** — deliberate, uncomfortable changes to run against a design. Collected here as a "we're stuck" list. Most are cheap to try in sim.

**On the whole design**
- Remove anything that could be considered an act of violence. Identify what units could still be trying to do, and why they'd care to see each other. Gamify that.
- Classify every force-projection rule as beneficial or dangerous — then swap each to the other kind at the same power level.
- Play the game with miniatures from another genre. Play it with plain wooden blocks.

**On fun and victory**
- Find something players do even when it's against their interests. Make it in their interests.
- Identify a moment where a test result causes *nothing* to happen. Make it make something happen.
- Remove one mechanic that requires bookkeeping.
- Create a stage for partially scoring before the end.
- Remove your victory conditions altogether. Then borrow another game's.

**On resolution**
- Recreate one resolution sequence's probability with a dice mechanic the game doesn't use — and with each of the four shaping mechanics in turn.
- Replace one resolution step with a dexterity mechanic.
- Have players roll five dice at the start of a round, usable to replace any five dice by either player.

**On movement and space**
- Give charging units a *disadvantage*. Worsen it until players refuse to charge. (Reveals what actually motivates engagement.)
- Allow free disengagement; then require a test; then give free strikes.
- Make terrain that slows movement **speed it up** by the same degree.
- Double or halve the play area. Square → rectangle, or the reverse.

**On activation**
- Swap Full Force ↔ Single Unit activation.
- Static initiative → shifting, or the reverse. Give initiative to the player with the fewest points on the table; then to the last player to cause a wound.

**On lists and abilities**
- Give all players access to all units. Then only three, of their choosing. Then dictate exactly which three.
- Make buffs freely stackable; then not at all; then only from different sources.
- Make debuffs reduce options; then statistics; then susceptibility.

---

## 11 · Vocabulary

Terms worth adopting so we can talk precisely. The book's stated hope is that designers adopt and adapt them so the field can *"build on each other's work"* (p.18).

| Term | Meaning |
|---|---|
| **Non-discrete game** | Analogue positioning **and** an open component set. Passes the *shoe test* |
| **Force projection** | The zone a marker can interact with. **Active** (threat range, only while activated) · **Passive** (auras, reaction fire) |
| **Aura / pulse** | A 360° zone; permanent-inherent or temporary-activated. A *pulse* is a one-action version |
| **Relational conflict** | Resolution that cares about *relative orientation* — flanks, rears, head-on |
| **Laddering** | Players can do **more** on the last turn than the first (*Catan*) |
| **Zeroing** | Players can do **less** but it matters more — attrition toward a decisive few decisions. **The natural fit for this medium** |
| **Reach (R)** | ⅙–⅛ of table width. Standard move R · fast 2R · most ranged 2R–3R · deploy 3R–4R apart |
| **Game scale** | Deliberately abandoning true ground scale for playability |
| **Scope** | Size of the depicted conflict: character skirmish → skirmish → massed battle |
| **Diegetic / non-diegetic** | Inside the game world / outside it |
| **Intrinsic / extrinsic** | For its own sake / for a reward. Crossed with the above, gives four sources of fun |
| **Embedded / emergent narrative** | Placed by the designer / generated by play |
| **Overall conceit** | The *"you are…"* statement framing the player's role |
| **Minor conceit** | The in-fiction label that makes an abstract roll legible ("to hit", "toughness") |
| **Dramatic focus** | Where the mechanics point the player's attention |
| **Full Force Activation** | IGOUGO, renamed for precision |
| **Single Unit Activation** | "Alternating activations", renamed |
| **Partial Force Activation** | Activate a division or set number, then hand over |
| **Control removal** | Any mechanic taking a unit out of its player's control |
| **Plot armour** | Rules making key models the last to die |
| **Headwind** | A cost that rises with power, slowing snowball |
| **The golden rule** | The published catch-all for disputes |
| **The five personas** | Story-builder · Spectacle-maker · Fine-point competitor · Player-artist · Mechanic-connoisseur |

### The personas, and their cardinal sins
**(pp.68–72)**

Every real player is a blend. The sins are the useful half — they name what each type will not forgive:

| Persona | Plays for | Cardinal sin |
|---|---|---|
| **Story-builder** | Narrative; exploring the world | Waving off narrative concerns as secondary to gameplay |
| **Spectacle-maker** | Experience; pulling levers to see what happens | **Pulling a lever and nothing happening** |
| **Fine-point competitor** | Proving they can solve the puzzle | Unclear or unreliable feedback on why they lost |
| **Player-artist** | Self-expression through unusual choices | *"excessive freedom and balance"* — they need constraints to push against, and sub-optimal options are **catnip** |
| **Mechanic-connoisseur** | Appreciating craft | Recycled mechanics in new clothes. *"They would rather see a designer swing big and fail hard than modestly succeed"* |

---

## 12 · The pre-flight checks

Short lists to run before shipping. Each item links to the section that explains it.

### Before shipping a new rule
- [ ] Does it put the player's attention where I want it? *(Law 1)*
- [ ] Is the thing it governs one of the most-repeated loops? If so, is it fun? *(Law 2)*
- [ ] Am I writing against something that is no fun **but advantageous** — or wasting text on something already disadvantageous? *(Law 4)*
- [ ] Could I make the undesired behaviour *weak* instead of *illegal*? *(Law 5)*
- [ ] If it introduces a resource: does it actually run out? Is it fungible? *(Law 6, §4)*
- [ ] If it removes control: is the uncontrolled part choice-free, and is it bracketed by choices? *(Law 7)*
- [ ] Modifiers on one side only, inside the cap? *(§5)*
- [ ] If it can stack: have I said so explicitly, and consistently with everything else? *(§8)*
- [ ] Does it add a named state, token or track? If so, what am I cutting to pay for it? *(§2, anti-bloat)*
- [ ] Have I checked it against the failure catalogue? *(§7)*

### Before shipping a scenario
- [ ] Are all four parts specified — set-up, special rules, game end, victory? *(§9.2)*
- [ ] Is the weight in **set-up** (public, once) rather than in-play rules? *(§9.2)*
- [ ] Do any in-play special rules trigger off a **state change**, or are they forgettable? *(§7.27)*
- [ ] Can either player win by **disengaging**? Challenge a playtester to try. *(§7.9–11)*
- [ ] Does every generated objective combination still force the two crews to interact? *(§9.1)*
- [ ] Is there both a player-triggered and a preset end condition? *(§9.1)*

### Before shipping a price
- [ ] Did I anchor on a damage ratio or an equivalent measured quantity? *(§6)*
- [ ] Am I iterating on the **under** side of my guess? *(§6)*
- [ ] Is the stat I'm pricing **opposed**? If so, it has no fixed value — check the curve. *(§6)*
- [ ] Are synergy components priced **individually**, so the combo is a free reward? *(§6)*
- [ ] Is this option merely *weak*, or is it **negative** — strictly worse than the default it replaces? Weak ships; negative doesn't. *(Law 9)*
- [ ] Could a victory condition produce this force shape instead of a slot rule? *(§6)*

### Before shipping a campaign system
- [ ] Which of the three is it — meta-scoring, structuring, or progression? *(§9.3)*
- [ ] What stops a losing player dropping out? *(§7.19)*
- [ ] Does winning grant resources? If so, what's the headwind — and does it merely slow the snowball? *(§7.4)*
- [ ] Is gated content visible but unreachable? Can players **target** an unlock? *(§7.17)*
- [ ] Does the map/meta layer overrule tabletop skill? *(§9.3)*
- [ ] Do injuries punish the loser twice? *(§9.3)*

---

## Sources

- **Primary:** Ford, G. & Hutchinson, M. (2025) *The Fundamentals of Tabletop Miniatures Game Design: A Designer's Handbook*. Boca Raton: CRC Press / Taylor & Francis. ISBN 978-1-032-32402-9 (hbk) · DOI 10.1201/9781003314820
- **Full chapter notes:** `Webscraper/data/books/FUNDAMENTALS_CLIFF_NOTES.md` (5,394 lines, page-cited, all 31 chapters)
- **Source PDF:** `Webscraper/data/books/fundamentals_tabletop_miniatures_glenn_ford.pdf` (433pp)
- **Prototyping toolkit** (CC0 public domain, by the authors): `https://planetsmashergames.com/fundamentals/prototyping-toolkit`
- **Companion docs in this repo:** `EQUIPMENT-RESEARCH.md` (30 games' gear systems) · `POINTS-RESEARCH.md` (~25 games' costing) · `BLKOUT-RULES-ANALYSIS.md`
- **Authority for anything marked `→ Settlements`:** `Rules System/Full Rules System v1.md` and `AGENTS.md`. Where they disagree with this file, **they win** and this file is owed an edit.
