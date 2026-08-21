# research/ — wargaming rules & mechanics research

Raw material and machine-readable output for the **[[Wargaming Research]]** hub. The
curated, human-readable notes do **not** live here — they live in the Obsidian vault at
`Documents/Obsidian Vault/Settlements/Research/`, and arrive in this repo automatically
under `rules-vault/Research/` on the 15-minute sync.

## The split — which side does a file belong on?

| | `research/` (this folder) | vault `Research/` → `rules-vault/Research/` |
|---|---|---|
| **Holds** | raw captures: PDFs, scraped HTML/markdown, Reddit/forum threads, transcripts, the index JSON | curated notes: the hub table + one note per source |
| **Written by** | the `wargaming-researcher` agent, scrapers, manual downloads | the agent (and Ross), in Obsidian house style with `[[wikilinks]]` |
| **Edited by hand?** | rarely — it's evidence, kept verbatim | **yes — this is the live surface** |
| **Git** | committed, except large binaries (see below) | mirrored one-way, never hand-edited in `rules-vault/` |

Rule of thumb: **if it has a `[[wikilink]]` in it, it belongs in the vault.** If it's the
thing a wikilinked note is quoting, it belongs here.

## Layout

```
research/
├── sources/          one folder per source — the verbatim capture
│   └── <slug>/
│       ├── source.md         cleaned markdown of the original
│       ├── meta.json         url, title, author, retrieved date, sha256, licence note
│       └── original.pdf      (optional) the untouched original
├── captures/         scratch — in-flight scrapes not yet promoted to sources/
└── index.json        every source + every mechanic extracted from it, machine-readable
```

`index.json` is the join key between the two halves: each entry carries the source slug,
the vault note it produced, and the mechanics rows it contributed to the hub. Regenerate
or extend it whenever a source is added.

## Large binaries

Rulebook PDFs are **not committed** — they're third-party copyrighted material and they're
big. `sources/**/original.pdf` is gitignored; `source.md` (our extracted, quoted-in-fair-use
notes) and `meta.json` are committed so the trail is reproducible. Keep the original where
you downloaded it and record that path in `meta.json`.

## Existing research already in the repo

These predate this folder and are still the canonical long-form for their subject. The vault
notes cite them rather than duplicating them:

| Doc | What it is |
|---|---|
| `docs/POINTS-RESEARCH.md` | 2,050 lines — how ~25 wargames derive costs, with a `[FACT]/[CONSENSUS]/[INFERENCE]/[NOT FOUND]` evidence tag on every claim. The single richest source in the project. |
| `docs/BLKOUT-RULES-ANALYSIS.md` | Full read-through of BLKOUT 2e + its supplement, framed against the Settlements taxonomy. |
| `docs/SETTING-TECH-2051.md` | Near-future mil-tech research for the setting. |

## Adding a source

Ask the **`wargaming-researcher`** agent. It scrapes the source, writes `sources/<slug>/`,
creates the vault note, and adds the mechanic rows to the hub. Doing it by hand: follow the
same layout, then copy `Research/_Research Entry Template.md` in the vault for the note.
