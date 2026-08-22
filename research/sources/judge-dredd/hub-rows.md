# Hub rows — Judge Dredd Miniatures Game (Warlord Games, 2020)

Copy-paste ready. Source vault note: `Judge Dredd Miniatures Game.md` (Research/Notes/).
Capture: `research/sources/judge-dredd/` (source.md, meta.json, block-war-meta.json).

Target file: `Research\Wargaming Research Hub.md`

---

## Target section: `## 🎯 Combat, damage & injury`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Judge Dredd Miniatures Game** | Stun/Injury fork — capturability as a weapon property | Combat | A knockout is tagged Stun or Injury by the weapon that caused it, not by range or melee — only an Injury tag risks a death roll after the game; Stun-only always risks arrest instead. | [[Judge Dredd Miniatures Game#The Stun/Injury fork — capturability as a weapon property, not a coin-flip]] |

---

## Target section: `## 🏁 Scenarios, objectives & victory`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Judge Dredd Miniatures Game** | The Crime Ledger — sentences built from actions taken | Scenario | Post-game sentencing reads off an itemised in-game crime code (shots fired, Injury vs Stun markers caused, weapons used) rather than one flat post-game roll. | [[Judge Dredd Miniatures Game#The Crime Ledger — sentences are built from actions taken, not from a single post-game roll]] |
| ⚙️ | **Judge Dredd Miniatures Game** | Informers — pay to bias scenario role assignment | Scenario | A Notoriety-bought upgrade adds +1 per Informer spent to a simultaneous-reveal roll-off deciding which side attacks and which defends. | [[Judge Dredd Miniatures Game#Informers — paying a campaign resource to bias which scenario role you get]] |

---

## Target section: `## 📈 Campaign, progression & snowball control`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⚙️ | **Judge Dredd Miniatures Game** | Sentencing, Iso-Cubes, and the jailbreak loop | Campaign | A captured model serves time with its own passive death/escape risk each missed game, and jailbreak is floated by the book itself as a Raid/Heist variant with prisoners standing in for the cache. | [[Judge Dredd Miniatures Game#Sentencing, Iso-Cubes, and the jailbreak loop]] |
| ⚙️ | **Judge Dredd Miniatures Game** | Deeds — the losing side still earns advancement | Campaign | A heavily-sentenced perp earns their owner a Deed scaled to sentence length — being captured isn't a pure write-off for the promotion track. | [[Judge Dredd Miniatures Game#Deeds — the losing side still earns advancement currency]] |
| 📎 | **Judge Dredd Miniatures Game** | Underdog Big Meg Cards — bonus resource scales with the gap | Campaign | +1 wildcard card per full 10 points of Notoriety deficit, rounding up — independent confirmation of rating-gap banding over win/loss banding ([[Necromunda and Mordheim#Underdog banding]]). | [[Judge Dredd Miniatures Game#Underdog Big Meg Cards — a bonus resource that scales with the gap, not the scoreboard]] |
| 📎 | **Judge Dredd Miniatures Game** | Notoriety phase ceiling — fixed schedule, catch-up top-up | Campaign | Budget ceilings escalate on a printed Early/Mid/Late schedule regardless of performance; under-cap rosters get free top-up Notoriety to match. Second data point for [[Trench Crusade#The published threshold ladder]]. | [[Judge Dredd Miniatures Game#The Notoriety phase ceiling — fixed schedule, catch-up top-up, never performance-tied]] |
| 📎 | **Judge Dredd Miniatures Game** | Grudge Points — a two-faction nemesis track | Campaign | Two rival gang Leaders accrue points against each other specifically (from Deeds the rival earned, wounds their own crew took, defending a Raid) cashed in the next time those two factions meet. | [[Judge Dredd Miniatures Game#Grudge Points — a two-faction nemesis track]] |

---

## Target section: `## 💰 Costing & points derivation`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⚙️ | **Judge Dredd Miniatures Game** | Base Upgrades — fire-arc costs the field of fire | Costing | A Placed Gun's own weapon cost is surcharged by a percentage for its firing arc (+25%/+50%/+100%), rounded up — one currency prices units, base defences, and campaign resources alike. | [[Judge Dredd Miniatures Game#Base Upgrades — one currency buys crew, base defences, and one-off campaign resources alike]] |

---

## Target section: `## 🧱 List building & force construction`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| 📎 | **Judge Dredd Miniatures Game** | Robots — a keyword, not a subsystem | List | Every robot is a normally-costed roster entry carrying one repeated rule (no Star chips, immune to Psi) — the book's 110 "robot" word-count hits were mostly repeated flavour text, not mechanical density. | [[Judge Dredd Miniatures Game#Robots — a keyword, not a subsystem (and a lesson about probe counts)]] |

---
---

### index.json block

Add one entry to `sources[]`. `mechanics[].name` is copied **verbatim** from the Mechanic cell above.

```json
{
  "slug": "judge-dredd",
  "title": "Judge Dredd Miniatures Game",
  "game": "Judge Dredd Miniatures Game",
  "designer": "Dylan Owen",
  "publisher": "Warlord Games",
  "year": 2020,
  "depth": "primary",
  "note": "Research/Notes/Judge Dredd Miniatures Game.md",
  "capture": "research/sources/judge-dredd/",
  "mechanics": [
    { "name": "Stun/Injury fork — capturability as a weapon property", "type": "Combat", "verdict": "⭐" },
    { "name": "The Crime Ledger — sentences built from actions taken", "type": "Scenario", "verdict": "⭐" },
    { "name": "Sentencing, Iso-Cubes, and the jailbreak loop", "type": "Campaign", "verdict": "⚙️" },
    { "name": "Deeds — the losing side still earns advancement", "type": "Campaign", "verdict": "⚙️" },
    { "name": "Underdog Big Meg Cards — bonus resource scales with the gap", "type": "Campaign", "verdict": "📎" },
    { "name": "Informers — pay to bias scenario role assignment", "type": "Scenario", "verdict": "⚙️" },
    { "name": "Notoriety phase ceiling — fixed schedule, catch-up top-up", "type": "Campaign", "verdict": "📎" },
    { "name": "Base Upgrades — fire-arc costs the field of fire", "type": "Costing", "verdict": "⚙️" },
    { "name": "Robots — a keyword, not a subsystem", "type": "List", "verdict": "📎" },
    { "name": "Grudge Points — a two-faction nemesis track", "type": "Campaign", "verdict": "📎" }
  ]
}
```

---

### Proposed Source-index row (`## 📚 Source index`)

| Note | Game / subject | Designer · Publisher | Depth | Long-form source |
|---|---|---|---|---|
| [[Judge Dredd Miniatures Game]] | Judge Dredd Miniatures Game — Judges-vs-perps urban law-enforcement skirmish with a campaign layer | Dylan Owen · Warlord Games | **Primary** — full 164-page rulebook read in full | `research/sources/judge-dredd/` |

---

### To-read-next changes (`## 🔭 To read next`)

Add these three new entries — nothing existing needs ticking off (Judge Dredd wasn't already listed):

- [ ] **Strontium Dog Miniatures Game** (Warlord Games, 2019), primary PDF sitting uncaptured alongside this one in `G:\My Drive\Wargaming\Judge dredd\Miniatures Games (Judge Dredd, Strontium Dog, Slaine)\`. Same publisher/era as [[Judge Dredd Miniatures Game]] — likely the same Notoriety/Action-chip/Combat-dice chassis, sci-fi bounty-hunter setting. **Flagged as the stronger candidate of the two Warlord siblings for Settlements** (closer tonally than Slaine).
- [ ] **Slaine Miniatures Game** (Warlord Games, 2022), primary PDF, same folder as above. Same engine family, Celtic-fantasy setting — thematically distant from Settlements, lower priority than Strontium Dog.
- [ ] **Judge Dredd Miniatures Game (Mongoose Publishing, c.2009–2013)** — a completely different, older Judge Dredd miniatures game discovered mid-capture: `research/sources/judge-dredd/block-war.pdf` (assumed to be a Warlord supplement) turned out to be *this* game's "Block War" expansion instead (Credits/Rep/Minions/Heroes engine, Matthew Sprange). Its own core rulebook was not found in the library — needed before a real capture. Partial skim surfaced one citable idea for the Settlement/Territory want: a 2D6 Territory table (flat income + a unique special ability per site) capped at 10 held but gated to fewer "managed" (income-generating) by a crew-headcount table. **Not verified in depth — see `research/sources/judge-dredd/block-war-meta.json` for the full write-up.** Needs its own slug and vault note once the core rulebook is located (different publisher, different system — not a supplement to [[Judge Dredd Miniatures Game]]).
