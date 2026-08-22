# Hub rows — Necromunda homebrew capture

For the merging agent. Vault note: `Research/Notes/Necromunda Homebrew Campaigns.md`
(already written and link-checked — 0 broken anchors against the vault as of this capture).

## ⚠️ Proposed new mechanic type: Diplomacy

No existing row in "🏷️ Mechanic types" covers alliance/negotiation/betrayal mechanics — the closest
is Campaign or Faction, neither of which fits. Three rows below use `Diplomacy` as their Type. Suggest
adding to the legend table:

| Type | Covers | Our note |
|---|---|---|
| **Diplomacy** | alliances, truces, negotiation, betrayal, reputation-as-standing | [[Diplomacy]] |

...and a new hub section **`## 🤝 Diplomacy & negotiation`** (no section currently exists for it — it
would need to be inserted, e.g. after "🎭 Faction identity" and before "🏰 Settlement, base &
territory," matching the type-legend ordering). If you'd rather fold these into an existing section
instead of adding a new one, `Campaign` is the least-bad fallback for all three — your call.

Also add `"Diplomacy"` to `mechanic_types` in `research/index.json` if the new type is adopted.

---

## Hub rows

### → new section `🤝 Diplomacy & negotiation` (or fold into `📈 Campaign, progression & snowball control`)

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Necromunda (homebrew)** | Striking a Deal — a one-roll table with a hidden hedge for betrayal | Diplomacy | A single open D6 decides refused/one-scenario/long-term, but the **break check on a struck deal is rolled in secret and hidden by an impartial party** — the only source in this vault that gives alliance-breaking actual dice teeth instead of table talk. | [[Necromunda Homebrew Campaigns#Striking a Deal — a one-roll table with a hidden hedge for betrayal]] |
| ⭐ | **Necromunda (homebrew)** | The Meet and the Double-Cross — betrayal staged as a scenario | Diplomacy | A hidden third-party Ambusher gang (or a hidden traitor half of your own "ally") turns "you've been betrayed" into an actual firefight with a real chance both duped gangs shoot each other by mistake, instead of a GM narrating it. | [[Necromunda Homebrew Campaigns#The Meet and the Double-Cross — betrayal staged as a scenario, not a narrated event]] |
| ⚠️ | **Necromunda (homebrew)** | Alliances without teeth — the modern homebrew default | Diplomacy | Three independent, more-recent hex-map campaigns (Under the Dome, Underside Campaign, Frontier Campaign) all quietly dropped mechanical betrayal risk in favour of an unenforced, table-talk-only pact — the opposite choice from the older Striking a Deal mechanic above. | [[Necromunda Homebrew Campaigns#Alliances without teeth — the modern homebrew default]] |

### → `🎭 Faction identity`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Necromunda (homebrew)** | Hard-blocked pairings — some factions never get to roll | Faction | A short, absolute exclusion list (Escher/Goliath, Redemptionist-only-with-Cawdor, Spyrers/Ratskins-with-anybody) vetoes a deal before any dice are thrown — one line of text doing all the thematic work of a reputation system. | [[Necromunda Homebrew Campaigns#Hard-blocked pairings — some factions never get to roll]] |

### → `📈 Campaign, progression & snowball control`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Necromunda (homebrew)** | The Arbitrator's Special — a costed, GM-adjudicated wildcard slot | Campaign | Reputation-as-currency's fourth spend option is a named, budgeted "the referee rules on it, cost varies" line — bounds GM fiat with a price tag instead of leaving it free and unbounded. | [[Necromunda Homebrew Campaigns#The Arbitrator's Special — a costed, GM-adjudicated wildcard slot]] |
| ⭐ | **Necromunda (homebrew)** | Arbitrator-curated rotating NPC pools — the same fix, invented twice | Campaign | Two unrelated documents (Lost Zone's Trading Post Generator/Unemployment Office; Expanded Campaign's Heroes-of-Might-and-Magic-inspired Tavern Mechanic) independently built a weekly Arbitrator-curated, scarcity-capped hire/buy list — with cheapest-item-to-lowest-rated-gang as a free catch-up rule riding along. | [[Necromunda Homebrew Campaigns#Arbitrator-curated rotating NPC pools — the same fix, invented twice]] |
| ⚠️ | **Necromunda (homebrew)** | Reputation, admitted broken, rebuilt as a second currency | Economy | Lost Zone's designer states official Reputation is *"pretty much meaningless after a point"* and fixes it by making it a second spendable currency — a real diagnosis of a real problem, cured the one way Settlements has already locked against (one economy only). | [[Necromunda Homebrew Campaigns#Reputation, admitted broken, rebuilt as a second currency]] |
| ⭐ | **Necromunda (homebrew)** | Six-category Triumphs instead of one winner | Campaign | Spire of Babel's six simultaneous "best at X" awards (Dominator/Slaughterer/Creditor/Warmonger/Powerbroker/Achiever, explicitly citing official N18 Dominion Campaign as precedent) let a campaign end without crowning one winner — echoed independently at scenario scale by Desperation Campaign's Saviour/Looter/Hunter. | [[Necromunda Homebrew Campaigns#Six-category Triumphs instead of one winner]] |
| ⭐ | **Necromunda (homebrew)** | Achievements with zero mechanical payout | Campaign | ~28 one-time checkboxes that feed only the Achiever Triumph category, never claimed exclusively and never worth in-game power — the cheap end of the same dial Trench Crusade's Glory sits at the expensive end of. | [[Necromunda Homebrew Campaigns#Achievements with zero mechanical payout]] |
| ⭐ | **Necromunda (homebrew)** | The Campaign Events Table — catch-up baked into the randomness itself | Campaign | A D66 random-event table whose entries deliberately skew toward penalizing the highest-rated gang and boosting the lowest (a free veteran attaches to the last-place gang "until they no longer have the lowest rating") — balance work done inside the flavour table itself, at zero extra tracked numbers. | [[Necromunda Homebrew Campaigns#The Campaign Events Table — catch-up baked into the randomness itself]] |
| ⭐ | **Necromunda (homebrew)** | The post-battle action — one downtime action per surviving fighter | Campaign | Every surviving fighter gets exactly one downtime action to spend on ONE of injury-mitigation/income/rare-item-search/skill-training — forces a real per-model trade-off instead of doing every downtime task for every fighter automatically. | [[Necromunda Homebrew Campaigns#The post-battle action — one downtime action per surviving fighter]] |

### → `🎲 Solo & co-op`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Necromunda (homebrew)** | Arbitrator's Monster — a dual-mode PvE stat block | Solo | Creature profiles explicitly tagged to run either under a human Arbitrator or by a printed simplified-AI ruleset shared across every tagged monster — one stat block serves both refereed and unrefereed play for free. | [[Necromunda Homebrew Campaigns#Arbitrator's Monster — a dual-mode PvE stat block]] |

### → `🏰 Settlement, base & territory`

| Take | Game | Mechanic | Type | Description | Full write-up |
|:--:|---|---|---|---|---|
| ⭐ | **Necromunda (homebrew)** | Settlement visit as an encounter roll, not just a shop | Settlement | A capped number of locations per visit (D3) plus one shared D66 random-event roll for the whole travelling party turns "go shopping" into something that can happen *to* you — two self-contained push-your-luck mini-games (Gambling, Pit-Fighting) share one clean "when to quit" streak-gate. | [[Necromunda Homebrew Campaigns#Settlement visit as an encounter roll, not just a shop]] |
| 📎 | **Necromunda (homebrew)** | The settlement-nominee template — identity as reweighted odds, not a new system | Settlement | A community design-contest's shared (if thin) schema: worldbuilding + one signature rule + a reweighted territory table — cheapest-possible way to differentiate a named location without a new subsystem. One of three entries checked was pure flavour with no mechanics at all. | [[Necromunda Homebrew Campaigns#The settlement-nominee template — identity as reweighted odds, not a new system]] |

---

## index.json — mechanics array (name / type / verdict)

Use exactly these `name` strings (kept identical to the hub-row Mechanic cells, per house rule) —
verdict mapped ⭐=steal, ⚙️=adapt, ⚠️=avoid, 📎=reference:

```
{
  "slug": "necromunda-homebrew",
  "game": "Necromunda — homebrew and community campaign layer",
  "note": "Research/Notes/Necromunda Homebrew Campaigns.md",
  "publisher": "Community / fan-authored",
  "depth": "community reconstruction",
  "capture": "research/sources/necromunda-homebrew/",
  "long_form": null,
  "retrieved": "2026-08-22",
  "mechanics": [
    { "name": "Striking a Deal — a one-roll table with a hidden hedge for betrayal", "type": "Diplomacy", "verdict": "steal" },
    { "name": "The Meet and the Double-Cross — betrayal staged as a scenario", "type": "Diplomacy", "verdict": "steal" },
    { "name": "Alliances without teeth — the modern homebrew default", "type": "Diplomacy", "verdict": "avoid" },
    { "name": "Hard-blocked pairings — some factions never get to roll", "type": "Faction", "verdict": "steal" },
    { "name": "The Arbitrator's Special — a costed, GM-adjudicated wildcard slot", "type": "Campaign", "verdict": "steal" },
    { "name": "Arbitrator-curated rotating NPC pools — the same fix, invented twice", "type": "Campaign", "verdict": "steal" },
    { "name": "Reputation, admitted broken, rebuilt as a second currency", "type": "Economy", "verdict": "avoid" },
    { "name": "Six-category Triumphs instead of one winner", "type": "Campaign", "verdict": "steal" },
    { "name": "Achievements with zero mechanical payout", "type": "Campaign", "verdict": "steal" },
    { "name": "The Campaign Events Table — catch-up baked into the randomness itself", "type": "Campaign", "verdict": "steal" },
    { "name": "The post-battle action — one downtime action per surviving fighter", "type": "Campaign", "verdict": "steal" },
    { "name": "Arbitrator's Monster — a dual-mode PvE stat block", "type": "Solo", "verdict": "steal" },
    { "name": "Settlement visit as an encounter roll, not just a shop", "type": "Settlement", "verdict": "steal" },
    { "name": "The settlement-nominee template — identity as reweighted odds, not a new system", "type": "Settlement", "verdict": "reference" }
  ]
}
```

Note: the vault note has 15 `##` mechanic headings total; the table above covers all 14 hub-row-worthy
ones (the 15th, "What it gets wrong," is a wrap-up section, not a mechanic, and isn't linked from a hub
row — matching house style elsewhere in the vault).

---

## Source index row

| Note | Game / subject | Designer · Publisher | Depth | Long-form source |
|---|---|---|---|---|
| [[Necromunda Homebrew Campaigns]] | Necromunda — homebrew/community campaign layer (deals, Arbitrator role, Triumphs, settlement events) | Multiple community authors; one source (`arbitrator-campaign.pdf`) reads as GW studio-authored, flagged in the note | **Community reconstruction** — 5 of 17 curated PDFs read closely, remainder grepped/spot-checked for convergence (94-file library, 17 curated, ~77 uncaptured) | `research/sources/necromunda-homebrew/` |

---

## To read next — additions/ticks

**Add to the list** (found but not captured this run):
- `ExpandedCampaignRules_V2.pdf` (library: same folder as Expanded Campaign) — a different-hashed, likely later-versioned document than the one captured; not read.
- `Book-of-the-Sump 2/` and `PRINT_Book of the Sump.pdf` — duplicate/print variants of Book of the Sump; not read (content believed identical, see meta.json note).
- `gw_05_settlement_events P1.pdf` — a third, differently-hashed scan of Settlement Events Part 1; not read.
- The remaining ~77 files in `G:\My Drive\Wargaming\NECROMUNDA\Campaigns and Homebrews\` are entirely uncaptured — this run was scoped to the 17 files staged in `research/sources/necromunda-homebrew/`.

**Nothing to tick off** on the existing "To read next" list from this run — this capture was assigned
directly rather than pulled from that list (confirm/ignore if the necromunda-official agents' rows
already covered any overlapping entries).
