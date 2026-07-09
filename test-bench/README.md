# Settlements — Test Bench

A self-contained probability + combat simulator for the Settlements core engine.
**No install, no server.** Double-click `index.html` (or drag it into any browser). Works offline.

## Tabs
- **Core Test** — the `1d10 + Stat ≥ 7` mechanic. Exact success % + a mod −1…+6 table.
- **Shooting** — two rolls (hit vs cover, then injury vs armor). Wound / Pin / Miss split + avg shots-to-Down.
- **Melee** — opposed STR, ties to defender, charge toggle. Attacker-wins % + injury.
- **Head-to-Head** — any contested opposed test (hacking duels, arm-wrestles). Configurable tie-winner.
- **Stat Check** — fixed-difficulty core test (hacking, lockpick, breakdown, climb). Routine auto-pass toggle.
- **Duel Sim** — Monte-Carlo attrition between two built fighters (2k–50k fights), with an optional Stress/Nerve layer. Pure combat — **no terrain/movement**, so it reads raw balance (terrain is the board's job).

Every button either **rolls once** (live dice, hands-on) or shows the **exact probability** (full enumeration — tabs 1–5). The Duel tab is Monte-Carlo.

## Keeping it honest
The dice math mirrors the rules in the Obsidian vault (`Settlements/Rules System`). Current dials baked in:
- weapon damage **+0 / +1 / +2 / +3** · armor **0 / −1 / −2** (injury only) · cover **0 / −1 / −2 / −3**
- stat cap **+6** · path tiers unlock at **+2 / +4 / +6**

If a number changes in the vault, change it in `index.html` (search the `DIALS` line / the relevant `<select>` options).
