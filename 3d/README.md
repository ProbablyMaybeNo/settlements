# 3D Assets

## Layout

```
3d/
├── source/    Editable source files (.blend, .obj working files, etc.)
└── stl/       Printable STLs (one folder per subject, optional)
```

## Naming

`<subject>__<variant>__<scale>.<ext>`

Examples:
- `fcf-trooper__rifleman__28mm.stl`
- `barricade__sandbag__terrain.stl`
- `objective-marker__settlement-flag.stl`

Scales used: `28mm`, `15mm`, `terrain`, `marker`.

## Tracking

Structured tracking lives in `TRACKERS/3d-models.csv`. Status options:
`concept`, `wip`, `printable`, `printed`, `cleaned`, `painted`. Each row
points to the source and/or STL path.

Run `py -3.13 scripts/notion_sync.py sync-3d` to push to the 3D Models DB.

## What goes where

- **Source:** the editable .blend / working file — what you'd open to
  revise the mesh.
- **STL:** the slicer-ready export. Keep these even if the .blend is
  here too — STLs are what gets printed.

Don't commit huge binaries to git. If a file is >50MB, consider git-lfs
or keeping it out of version control entirely. The CSV row + filename
should be enough to find it on disk.
