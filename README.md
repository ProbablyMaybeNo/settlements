# Settlements

A tabletop wargame in development. Modern-day second American civil war —
skirmish-scale, irregular crews, contested neighbourhoods, base-building campaign.

**Status:** Pre-alpha. Vision + pillars set, foundation rules drafted, no playtests yet.

---

## ⚠️ Source of truth = Notion (changed 2026-06-10)

The design and rules now live in **Notion**, not in this repo. The old local
design/rules docs were superseded and removed. This repo keeps only the **sync
tooling, tracker data, and asset folders**.

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
