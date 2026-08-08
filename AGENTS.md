# AGENTS.md — Settlements

## Learned User Preferences

- Keep all stat tests binary pass/fail against the flat TN 7+ mechanic. Do not add per-task difficulty modifiers — trivial actions (pushing a button) auto-pass, everything else is a straight 7+ test. Ross has pushed back on added test complexity repeatedly.
- Avoid flat unconditional "+1 to hit" bonuses when designing skills or rules; any to-hit bonus must be conditional (e.g. +1 vs units in the open).
- Core anti-bloat tenet: prefer cutting or merging subsystems over adding parallel ones (e.g. water upkeep was cut because housing already covers it). Don't propose new resource tracks or difficulty tiers without strong justification.
- Preferred design workflow: agent presents a numbered question list, Ross answers inline in chat, then the agent drafts the rules into the vault notes. Format questions so they're easy to answer in-chat.
- After drafting or changing rules, keep the Build Roadmap checkboxes and the rules ledger up to date.
- One economy only: a unit/equipment's goods cost IS its battle-roster points cost. Never introduce a second parallel points currency. The internal global points costing system (docs/GLOBAL-POINTS-SYSTEM.md) is a designer-side tool — players should never see it.

## Learned Workspace Facts

- Settlements is a pre-alpha tabletop skirmish wargame (modern second American civil war, base-building campaign). Rules are markdown notes, not code.
- Rules source of truth is Ross's Obsidian vault (`Documents/Obsidian Vault/Settlements/`). The repo's `rules-vault/` folder is a one-way mirror refreshed every 15 min by the "Settlements Rules Sync" scheduled task (`scripts/sync-and-push.ps1`). NEVER hand-edit `rules-vault/` — it gets overwritten on sync.
- Roadmap and trackers live in Notion (Build Roadmap page + Settlements hub DBs); `TRACKERS/` CSVs sync to Notion via `py -3.13 scripts/notion_sync.py sync-all`.
- Core resolution mechanic (locked): 1d10 + STAT − modifiers vs TN 7+ to pass; to-injure is 1d10 + DMG − Armor vs 7+.
- Five stats (locked): STR (melee/strength), DEX (ranged/perception/mechanical interactions), AGI (movement/climbing/leaping), INT (intelligence/hacking/digital interactions), NRV (nerve/bravery).
- Unit hierarchy at creation: Leaders start with 6 stat points, Champions 4, standard fighters 2; a unit gains a free skill per 2 stat points spent.
- Balance simulations live in `test-bench/` (includes `test-bench/balance/` Python sims run with `py -3.13`).
