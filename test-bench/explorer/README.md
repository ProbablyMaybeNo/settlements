# Sim Explorer

One queryable store for every simulation result, and a browser to search it.

Answers the question the sims exist to answer — *"what is the percentage chance
to injure a unit while firing weapon X with stat line Y, in cover Z, against
armour A?"* — without opening a script.

## Run it

```bash
powershell -File test-bench/explorer/serve.ps1
```

Rebuilds the database, then serves <http://127.0.0.1:8765/>. Nine ready-made
queries are on the front page with form boxes for the parameters; every result
exports as JSON or CSV from the link under the table.

To rebuild without serving:

```bash
py -3.13 test-bench/explorer/build_db.py
```

Rebuild after **any** change to `points/ticks.py`, the engine, or the catalogue —
costs and probabilities are read live at build time, never hardcoded.

The rebuild works **in place** and is safe to run while Datasette is serving and
while the `settlements-sims` MCP connector is attached. Both hold the file open
for their whole lifetime, and on Windows an open handle makes deleting it
impossible — so the build drops and recreates the objects through a connection
rather than replacing the file. Re-running is idempotent.

## The one thing to understand

Two kinds of number live here and they are not the same kind of number. Every
table carries a `provenance` column saying which it is.

| | `derived-exact` | `measured-monte-carlo` |
|---|---|---|
| Tables | `shot_matrix`, `weapon_shot` | `sim_runs`, `sim_values` |
| Where from | closed-form enumeration of the core engine | stamped envelopes in `balance/results/` |
| Sampling error | none | yes |
| Reproducible | recomputed every build | **no** — cannot be re-derived |
| Staleness | impossible by construction | tracked per row |

**Never average across the two.** A derived number is current because it was
just computed; a measured one is current only if nothing it depended on has
moved. That distinction is the whole point of `harness/provenance.py`, and
collapsing it here would reintroduce the false-freshness failure one layer up.

`sim_runs.stale` flags a run whose engine, cost-table or harness fingerprint no
longer matches today's. **Most stored runs are flagged, and that is healthy** —
the harness deliberately prefers false-stale to false-fresh, and editing any
measurement script marks every result stale on purpose.

## Tables

| Table | Rows | What it is |
|---|--:|---|
| `shot_matrix` | 12,096 | Every shot: stat × cover × extra to-hit mod × armour × damage × attack dice |
| `weapon_shot` | 5,760 | The same chain for each catalogue weapon at its real Credits cost |
| `weapons` | 20 | The shipped armoury, priced live from the points engine |
| `skills` | 149 | Path, tier, stat, unlock threshold |
| `bodies` / `armour_costs` / `characteristics` | — | Costing reference on the 850 scale |
| `sim_runs` | 79 | Every stamped envelope, with fingerprints and a stale flag |
| `sim_values` | 13,396 | Every measured value from those envelopes, flattened and searchable |
| `search` | 13,644 | FTS5 across findings, weapons, skills and run questions |

### Notes on the axes

- **`extra_to_hit`** covers everything that is not cover: Accurate (+1), Shaken
  (−1), elevation, a second condition. `over_mod_cap = 1` marks rows where the
  raw total exceeded the ±3 cap and was clamped — the clamped value is what was
  used.
- **Armour Piercing is not an axis.** AP 1 against heavy armour is arithmetically
  identical to light armour, which is already a row. Adding it would have
  duplicated a third of the table under a second name.
- **`e_wounds_stop_on_down` is now the live column.** Attack Dice were ruled on
  2026-08-29: a burst rolls every die at once, the attacker applies **one**
  Injury result, and a burst inflicts **at most 1 WND**. That makes the capped
  column correct and `e_wounds_resolve_all` a counterfactual — kept because it
  is what the uncapped reading would have given, and every pre-ruling figure in
  the notes was quoted from it.
- **`fielded_credits`** is the cheapest body legally able to carry the weapon
  plus the weapon. Per-Credit comparisons use it rather than weapon cost alone,
  because a weapon multiplies the output of a body and the body is the expensive
  part — a Fighter is 100 Cr against a 15 Cr rifle.

## Querying it from Claude Code

An MCP connector named `settlements-sims` is registered against this database,
so it can be queried conversationally without the web UI running:

> *"what's the chance a DEX+3 shooter with a +3 weapon injures a target in heavy
> cover wearing light armour?"*

Restart Claude Code after a `build_db.py` run that changes the schema.

## Other third-party front-ends

The file is a plain SQLite database with no extensions, so anything that reads
SQLite works against it: **DB Browser for SQLite**, **TablePlus**, **DBeaver**,
Excel/Power BI via an ODBC driver, or `pandas.read_sql`. Datasette is the one
wired up here because it needs no install per-user and gives faceted browsing
and CSV export out of the box.
