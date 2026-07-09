# Art Assets

## Layout

```
art/
├── references/    Mood boards, photo references, concept art (input)
└── final/         Finished pieces (output)
```

## Naming

`<subject>__<variant>__<status>.<ext>`

Examples:
- `fcf-trooper__front__ref.jpg`
- `patriot-front-banner__v3__final.png`
- `urban-core__mood__ref.png`

## Tracking

Don't duplicate metadata in filenames beyond what's useful for sorting.
The structured tracking lives in `TRACKERS/art-assets.csv` — each entry
points to the file path and tags it (faction, unit, location, etc.).

Run `py -3.13 scripts/notion_sync.py sync-art` to push to the Art Assets DB.

## What goes where

- **References:** anything that's input to your design thinking — Pinterest
  saves, screenshots, photo refs, mood collages.
- **Final:** anything you'd show off — finished concept art, faction
  insignia, rulebook illustrations.

Work-in-progress files can live anywhere; tag them `wip` in the tracker.
