# research/ — wargaming rules & mechanics research

Raw material and machine-readable output for the **[[Wargaming Research Hub]]** hub. The
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

## The source library — every rulebook is filed in two places

When a rules source arrives (a download, a path, an attachment), it is filed **twice**,
before anything is extracted from it:

| Copy | Path | Purpose |
|---|---|---|
| **Library master** | `G:\My Drive\Wargaming\<Game Name>\<Readable Name>.pdf` | The permanent, synced, browsable library. **One folder per game** — match the existing convention. Readable filename, not the download slug |
| **Working copy** | `research/sources/<slug>/original.pdf` | What we extract from. Gitignored |

Both are `sha256`-checked against the source and the hash goes in `meta.json` along with
the library path. If a file is already sitting loose in `G:\My Drive\Wargaming\`, it gets
**moved** into its game folder rather than duplicated.

Everything already in that library is a capture candidate — as of the first pipeline run
it holds BLKOUT, Frostgrave, Stargrave, Last Days, Mordheim, Necromunda, Oathmark, Rangers
of Shadow Deep, Trench Crusade, The Walking Dead, Fallout, Barons' War, Konflikt '47,
Kill Team, 40k and AoS. Several already have vault notes written from *other* sources;
those are upgrade candidates from second-hand to primary.

## Large binaries

Rulebook PDFs are **not committed** — they're third-party copyrighted material and they're
big. `sources/**/original.pdf` is gitignored; `source.md` (our extracted, quoted-in-fair-use
notes) and `meta.json` are committed so the trail is reproducible. The G Drive library
master is the durable copy; `meta.json` records its path.

## Existing research already in the repo

These predate this folder and are still the canonical long-form for their subject. The vault
notes cite them rather than duplicating them:

| Doc | What it is |
|---|---|
| `docs/POINTS-RESEARCH.md` | 2,050 lines — how ~25 wargames derive costs, with a `[FACT]/[CONSENSUS]/[INFERENCE]/[NOT FOUND]` evidence tag on every claim. The single richest source in the project. |
| `docs/BLKOUT-RULES-ANALYSIS.md` | Full read-through of BLKOUT 2e + its supplement, framed against the Settlements taxonomy. |
| `docs/SETTING-TECH-2051.md` | Near-future mil-tech research for the setting. |

## Adding a source — the standard pipeline

Hand it to the **`wargaming-researcher`** agent; this is the sequence it runs, and the one
to follow by hand if you're doing it yourself.

1. **File it twice** — G Drive library master + `sources/<slug>/original.pdf`. Verify the
   `sha256` of both against the source before going further.
2. **Extract** — `fitz` for a text layer, render + `pytesseract` only if there isn't one.
   Rebuild tables with `get_text("dict")` if the plain pass mangles them; **the tables are
   usually where the value is.** Clean the encoding — Osprey PDFs in particular emit
   replacement characters for apostrophes and dashes. Write `source.md` + `meta.json`.
3. **Analyse** — pull out *mechanics*, not a summary, and tag every load-bearing claim
   `[FACT]` / `[CONSENSUS]` / `[INFERENCE]` / `[NOT FOUND]`. Extract the *mechanism*: "their
   campaign doesn't snowball" is useless; "everyone's ceiling rises on the same printed
   schedule regardless of who's winning" is the finding.
4. **Write the vault note** — one per source, named for the game, one `##` heading per
   mechanic. **Those headings are an API** — the hub links to them, so make them durable.
   Template: `Research/_Research Entry Template.md`. Cross-link to the Settlements rules
   notes the mechanic would touch and to sibling research notes that agree or disagree.
5. **Populate the hub** — rows in `Research/Wargaming Research Hub.md` (Take · Game ·
   Mechanic · Type · Description · link to the note heading), a Source-index row with an
   honest depth rating, and a matching entry in `index.json`.
6. **Verify and sync** — run the anchor link-check, then `scripts/sync-rules.ps1` and commit.

The two rules that matter most: **never inflate the depth rating**, and **never invent a
number** — a recorded `[NOT FOUND]` is a real result and stops the next person re-searching
it.
