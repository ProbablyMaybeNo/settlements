# Settlements

A tabletop wargame in development. Modern-day second American civil war —
skirmish-scale, irregular crews, contested neighbourhoods, base-building campaign.

**Status:** Pre-alpha. Vision + pillars set, foundation rules drafted, no playtests yet.

---

## Where the design lives

- **Rules (live):** the **Obsidian vault** at `Documents/Obsidian Vault/Settlements/`, edited in Obsidian (synced across devices by Obsidian Sync). A mirror is committed here under **`rules-vault/`** so this repo is self-contained. It's refreshed **automatically every 15 min** by the **“Settlements Rules Sync”** scheduled task (`scripts/sync-and-push.ps1` → mirror + commit + push); `scripts/sync-rules.ps1` does a manual mirror only. **Don't hand-edit `rules-vault/`** — it's overwritten on sync. (An Obsidian git plugin can't do this — it would sync the *whole* vault, so it's intentionally not used here.)
- **Roadmap & trackers:** **Notion** (Build Roadmap + the project DBs).
- **Sim & tooling:** this repo — `test-bench/` (browser rules calculator), `scripts/`, `TRACKERS/`.

**Canonical Notion pages** (under THE HUB → Wargaming → 🏚️ Settlements):

| What | Page |
|---|---|
| 🗺️ Build Roadmap (the plan + all rules drafts) | `notion: d99342c0810e4386916f80af58ee65f7` |
| 📐 Design Pillars | `notion: 37cc577077718140badde5fe44a2b715` |
| 📚 Design Reference (wargame-design craft notes) | `notion: 37cc577077718129b7dbfe4e03c28ce3` |
| 🌎 Setting Notes (factions & geography) | `notion: 37cc5770777181d08eabe9bfbd9a724b` |
| 🏚️ Settlements hub (all DBs) | `notion: 364c57707771816cb3fcf524acc11aa1` |

Rules are written and tracked per phase in the Build Roadmap's **Rules** column.

## What's still in this repo

```
Settlements/
├── TRACKERS/        CSV data that syncs to the Notion DBs (units, weapons,
│                    factions, scenarios, locations, etc.)
├── art/             references/ and final/ image assets
├── 3d/              source/ (.blend) and stl/ (printable)
├── factions/        _template.md only (long-form writeups now live in Notion)
├── scenarios/       _template.md only
├── playtests/       _template.md only — per-session writeups go here
└── scripts/
    └── notion_sync.py
```

## Sync

| Task | Command |
|---|---|
| Sync everything to Notion | `py -3.13 scripts/notion_sync.py sync-all` |
| Pull playtest status back | `py -3.13 scripts/notion_sync.py pull-status` |
| Show sync state | `py -3.13 scripts/notion_sync.py status` |

See `scripts/notion_sync.py --help` for the full list.
