# Settlements Rules Vault — agent instructions

This repo is an **Obsidian vault**. The active project is the **Settlements** tabletop wargame rules system under `Settlements/Rules System/`. (A separate `The Huffles/` vault also lives here — leave it alone unless asked.)

## Canon (do not reinvent)
- **Only the 3 completed S1 notes are canon:** `Game Vision`, `Core Game Format`, `Rules Engine` — plus the `core-000 Core Test` ledger entry derived from them. Their text is authoritative.
- Everything else is a fresh stub to draft. Ross **started fresh** — do not resurrect old/pre-existing rules or tenets.
- **Core resolution engine:** `1d10 + Stat + mods, 7+` (natural 1 = auto-fail, natural 10 = auto-success; opposed tests: highest wins, ties to defender). Any uncertain outcome **cites** this (`[[Rules Engine]]` / `core-000 Core Test`) — it never restates it.

## The "done with [note]" pass
When Ross says **"done with [note name]"** (or pastes rough rule text), run this on that note:

1. **Structure** to house style: each distinct rule gets its own `###` heading; sub-parts `####`; the note's fixed sections stay `##`. Use tables for stat/modifier/probability data, code fences for dice/formulas, `> [!example]` for worked examples. Fix typos.
2. **Link & embed:** `[[ ]]` every rule/term it references; `![[ ]]`-embed anything that reuses canon instead of restating it. **One rule, one home — never restate a rule that lives elsewhere.**
3. **Wire dependencies:** update `depends_on` / `feeds_into` frontmatter and link the note from `Rules System MOC`.
4. **Flag** open decisions as `> [!question]` callouts (they surface on the Open Decisions board).
5. **Status:** set `status` on the ladder `Not Started → Designing → Drafted → Testing → Done`. When a rule is *locked*, **graduate it to a `core-xxx` ledger entry** (distilled, + probability table if mathy) and repoint citations to that ID.
6. **Commit** a restore point.

Full conventions live in `Settlements/Rules System/Quick Reference — Writing Rules.md` and `Obsidian Guide — Building Settlements.md`. Each S2 combat note already carries an **"Inherits from the engine"** panel that live-embeds the relevant S1 rule — read it, don't duplicate it.

## Sync caution (important — this vault has 3 sync layers)
Obsidian Sync (Ross's devices) + obsidian-git (auto-commit/push to this repo) + any cloud agent all touch these files. To avoid `.md` merge conflicts:
- **Pull before you start; commit + push when done.**
- **Never edit a note that Ross has open in Obsidian, or that another agent is editing, at the same time.** One editor per note.
