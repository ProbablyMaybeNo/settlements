"""Give every rules table a ^block anchor, so it can be embedded on its own.

    py -3.13 scripts/anchor_tables.py --dry-run
    py -3.13 scripts/anchor_tables.py

A heading embed drags in the whole section — for these notes that is 54% prose,
and some sections are 19% table. A BLOCK embed (`![[Note#^tbl-x]]`) pulls the
table and nothing else, which is what a table lens actually wants.

That needs every table to carry an anchor. This adds the missing ones: a single
`^tbl-slug` line immediately after the table, which is standard Obsidian, is
invisible in reading view, and changes no rule text. Existing anchors are left
exactly as they are.
"""
import io
import os
import re
import sys

RULES = os.path.join(os.path.expanduser("~"), "Documents", "Obsidian Vault",
                     "Settlements", "Rules System")
DRY = "--dry-run" in sys.argv

# Only the notes the lens actually shows. Deliberately excludes
# Full Rules System v1 (the source of truth — 38 anchors of churn for no gain,
# it is not a lens source) and the guide/roadmap docs.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_lens import BANDS  # noqa: E402
TARGETS = {n for _, notes in BANDS for n in notes}


def slugify(s, used):
    s = re.sub(r"[*`]", "", s).lower()
    s = re.sub(r"\[\[([^\]|]*\|)?([^\]]+)\]\]", r"\2", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:44] or "table"
    base, n = s, 2
    while s in used:
        s = "%s-%d" % (base, n)
        n += 1
    used.add(s)
    return s


def process(path):
    raw = io.open(path, encoding="utf-8", newline="").read()
    nl = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.replace("\r\n", "\n").split("\n")
    used = set(re.findall(r"^\^([a-z0-9-]+)\s*$", "\n".join(lines), re.M))

    inserts, heading, i = [], "table", 0
    while i < len(lines):
        bare = re.sub(r"^>\s?", "", lines[i])
        h = re.match(r"^#{1,6}\s+(.*)", lines[i])
        if h:
            heading = h.group(1)
            i += 1
            continue
        nxt = re.sub(r"^>\s?", "", lines[i + 1]) if i + 1 < len(lines) else ""
        if bare.startswith("|") and re.match(r"^\|[\s:|-]+\|?$", nxt):
            j = i + 2
            while j < len(lines) and re.sub(r"^>\s?", "", lines[j]).startswith("|"):
                j += 1
            # already anchored within the next two non-blank lines?
            k, seen = j, 0
            anchored = False
            while k < len(lines) and seen < 2:
                t = lines[k].strip()
                if t:
                    seen += 1
                    if re.match(r"^\^[a-z0-9-]+$", t):
                        anchored = True
                        break
                    break
                k += 1
            # a table inside a callout cannot take a bare anchor line
            if not anchored and not lines[i].lstrip().startswith(">"):
                inserts.append((j, "^" + slugify(heading, used)))
            i = j
            continue
        i += 1

    if not inserts:
        return 0, []
    if not DRY:
        for pos, anc in reversed(inserts):
            # blank line, anchor, blank line — Obsidian binds it to the block above
            lines[pos:pos] = ["", anc]
        tmp = path + ".anc-tmp"
        io.open(tmp, "w", encoding="utf-8", newline="").write(nl.join(lines))
        os.replace(tmp, path)
    return len(inserts), [a for _, a in inserts]


if __name__ == "__main__":
    total, touched = 0, 0
    for f in sorted(os.listdir(RULES)):
        if not f.endswith(".md") or f.startswith("_") or f[:-3] not in TARGETS:
            continue
        n, anchors = process(os.path.join(RULES, f))
        if n:
            touched += 1
            total += n
            print("  %-42s +%d  %s" % (f[:-3], n, ", ".join(anchors[:3])
                                       + (" ..." if len(anchors) > 3 else "")))
    print("\n%s %d anchors across %d notes."
          % ("would add" if DRY else "added", total, touched))
