"""Every catalogue as note records, plus a Base per catalogue — and back again.

    py -3.13 scripts/records.py explode      # tables -> record notes + .base files
    py -3.13 scripts/records.py verify       # round-trip every catalogue, byte-for-byte
    py -3.13 scripts/records.py rebuild NAME # print the regenerated table for one

Generalises the weapon-characteristics prototype. Rather than a bespoke script
per catalogue, the COLUMN CONVENTION IS DERIVED FROM THE DATA: for each column
we look at every cell and work out whether the whole column is bold-wrapped,
bold-plus-a-suffix, or free markdown. That wrapper is stored in the catalogue's
_schema.json, so a rebuild is deterministic from the stored VALUE alone — which
is what lets frontmatter be the source of truth without the raw markdown having
to be carried alongside it and go stale.

`verify` is the gate. A catalogue only converts if its records regenerate its
table byte-for-byte; anything that fails is reported and left alone rather than
silently losing formatting.
"""
import io
import json
import os
import re
import sys

VAULT = os.path.join(os.path.expanduser("~"), "Documents", "Obsidian Vault", "Settlements")
RULES = os.path.join(VAULT, "Rules System")
ROOT = os.path.join(VAULT, "Records")

# (folder, note, section-heading regex, table index within that section, tag)
# Table index matters where a section holds several tables — Deployables' mine
# family carries a chassis table and a payload table under one heading.
CATALOGUES = [
    ("Weapon Classes",        "Weapons", r"1 · Weapon classes", 0, "gear/class"),
    ("Weapon Characteristics", "Weapons", r"2 · Characteristics", None, "gear/characteristic"),
    ("Armour",                "Weapons", r"3 · Armor", 0, "gear/armour"),
    ("Hacking Gear",          "Weapons", r"4 · Hacking gear", 0, "gear/hack"),
    ("Sample Armoury",        "Weapons", r"5 · Sample armoury", None, "gear/weapon"),
    ("Turrets",               "Deployables", r"Family A", 0, "gear/deployable"),
    ("Mines",                 "Deployables", r"Family B", None, "gear/deployable"),
    ("Traps",                 "Deployables", r"Family C", 0, "gear/deployable"),
    ("Beacons",               "Deployables", r"Family D", 0, "gear/deployable"),
    ("Structures",            "Structures", r"The catalogue", None, "settlement/structure"),
    ("Worker Benefits",       "Structures", r"Worker benefits", 0, "settlement/worker"),
    ("Conditions",            "Conditions", r"Working rules", None, "combat/condition"),
    ("Reactions",             "Initiative & Activation", r"Reaction options", 0, "core/reaction"),
    ("Terrain",               "Terrain", r"Working rules", None, "terrain/type"),
    ("Terrain Verbs",         "Terrain Interaction", r"Interaction verbs", 0, "terrain/verb"),
    ("Infrastructure",        "Infrastructure", r"Feature catalogue", None, "terrain/feature"),
    ("Loot Table",            "Territory", r"Working rules", None, "campaign/loot"),
    ("Events",                "Events", r"Working rules", None, "campaign/event"),
    ("Factions",              "Factions", r"Working rules", None, "campaign/faction"),
    ("Skills",                "Skill Paths", r"^## (Combat|Shooting|Movement|Expertise|Bravery)", None, "crew/skill"),
]

SENT = chr(1)


def uncallout(line):
    """Strip a callout prefix so "> | a | b |" reads as a table row."""
    return re.sub(r"^>\s?", "", line)


def lines_of(note):
    # Some notes are CRLF. records.py only READS the notes, so normalising for
    # comparison is safe; wall_server.py, which writes, preserves the endings.
    raw = io.open(os.path.join(RULES, note + ".md"), encoding="utf-8", newline="").read()
    return raw.replace(chr(13) + chr(10), chr(10)).split(chr(10))


def split_row(line):
    masked = re.sub(r"\[\[[^\]]*\]\]|`[^`]*`",
                    lambda m: m.group(0).replace("|", SENT), line)
    return [c.strip().replace(SENT, "|") for c in masked.strip().strip("|").split("|")]


def slug(s):
    s = re.sub(r"[*`\[\]]", "", s).strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s or "col"


def find_tables(note, section_re, want_index):
    """Tables under the matching heading(s), with header, rows and line numbers."""
    lines = lines_of(note)
    out, inside, idx = [], False, 0
    for i, raw_l in enumerate(lines):
        l = uncallout(raw_l)
        if re.match(r"^#{2,4}\s", l):
            hit = bool(re.search(section_re, l))
            if section_re.startswith("^##"):
                hit = bool(re.match(section_re, l))
            if hit:
                inside, idx = True, 0
            elif re.match(r"^##\s", l):
                inside = False
            continue
        if not inside:
            continue
        nxt = uncallout(lines[i + 1]) if i + 1 < len(lines) else ""
        if l.startswith("|") and re.match(r"^\|[\s:|-]+\|?$", nxt):
            head = split_row(l)
            j, rows, nos = i + 2, [], []
            while j < len(lines) and uncallout(lines[j]).startswith("|"):
                rows.append(split_row(uncallout(lines[j])))
                nos.append(j)
                j += 1
            callout = [bool(re.match(r"^>\s?", lines[n])) for n in nos]
            if rows and (want_index is None or idx == want_index):
                # Some tables are written tight ("|a|b|"), others padded
                # ("| a | b |"). Rebuilding in the wrong style is a byte
                # difference on every row, so record which one this table uses.
                pad = lines[nos[0]].startswith("| ")
                widths = [len(split_row(lines[n])) for n in nos]
                # A few tables are hand-aligned into columns with padding spaces.
                # Rebuilding them unpadded differs on every row, so measure the
                # column widths from the source and re-apply them.
                rowpad = [[len(c) for c in uncallout(lines[n]).strip().strip("|").split("|")]
                          for n in nos]
                rowspaced = [uncallout(lines[n]).strip().startswith("| ") for n in nos]
                out.append({"head": head, "rows": rows, "lines": nos, "pad": pad,
                            "widths": widths, "rowpad": rowpad,
                            "rowspaced": rowspaced, "callout": callout,
                            "sep_line": i + 1})
            idx += 1
    return out


def find_bullets(note, section_re):
    """Bullet catalogues: runs of "- **Name** - description" under a heading.

    Conditions, Infrastructure and Skills are written as bullets rather than
    tables, so a table-only sweep scores them at zero. Each run becomes a
    two-column pseudo-table so the same record/rebuild machinery applies.
    """
    lines = lines_of(note)
    out, inside = [], False
    i = 0
    while i < len(lines):
        l = uncallout(lines[i])
        if re.match(r"^#{2,4}\s", l):
            hit = bool(re.match(section_re, l)) if section_re.startswith("^##")                 else bool(re.search(section_re, l))
            if hit:
                inside = True
            elif re.match(r"^##\s", l):
                inside = False
            i += 1
            continue
        if inside and re.match(r"^\s*-\s+\*\*", l):
            j, rows, nos, seps, leads = i, [], [], [], []
            while j < len(lines):
                b = uncallout(lines[j])
                m = re.match(r"^(\s*-\s+)\*\*([^*]+)\*\*(\s*[—:-]?\s*)(.*)$", b)
                if not m:
                    break
                leads.append(m.group(1)); rows.append([m.group(2), m.group(4)])
                seps.append(m.group(3)); nos.append(j)
                j += 1
            if len(rows) >= 3:
                out.append({"head": ["name", "description"], "rows": rows,
                            "lines": nos, "seps": seps, "leads": leads,
                            "bullet": True})
            i = j
            continue
        i += 1
    return out


def column_pattern(cells):
    """How this whole column is formatted, so a rebuild can re-apply it.

    Derived, never assumed: a column is only treated as bold-wrapped if EVERY
    non-empty cell in it is bold. Mixed columns fall back to raw, which is
    always safe because the value is then stored verbatim.
    """
    vals = [c for c in cells if c.strip()]
    if not vals:
        return {"kind": "raw"}
    if all(re.fullmatch(r"\*\*.+\*\*", c) for c in vals):
        return {"kind": "bold"}
    if all(re.match(r"^\*\*[^*]+\*\*.*$", c) for c in vals):
        return {"kind": "bold_suffix"}
    return {"kind": "raw"}


def decompose(cell, pat):
    if pat["kind"] == "bold":
        return {"v": cell[2:-2], "s": ""}
    if pat["kind"] == "bold_suffix":
        m = re.match(r"^\*\*([^*]+)\*\*(.*)$", cell)
        return {"v": m.group(1), "s": m.group(2)} if m else {"v": cell, "s": ""}
    return {"v": cell, "s": ""}


def compose(d, pat):
    if pat["kind"] == "bold":
        return "**%s**" % d["v"]
    if pat["kind"] == "bold_suffix":
        return "**%s**%s" % (d["v"], d.get("s", ""))
    return d["v"]


def yq(s):
    return '"%s"' % str(s).replace("\\", "\\\\").replace('"', '\\"')


def catalogue_folder(name):
    return os.path.join(ROOT, name)


def write_record(out, folder, note, tag, t_i, r_i, ncols, props, parts, label, seen):
    """One record note. Shared by the table and bullet paths."""
    label = re.sub(r"[*`\[\]]", "", label).strip() or ("row %d" % r_i)
    key = re.sub(r'[\/:*?"<>|#^]', "-", label)[:60]
    seen[key] = seen.get(key, 0) + 1
    if seen[key] > 1:
        key = "%s (%d)" % (key, seen[key])

    fm = ["---", "type: " + slug(folder).replace("_", "-"),
          "catalogue: " + yq(folder), "table: %d" % t_i, "row: %d" % r_i,
          "cols: %d" % ncols]
    for pr, part in zip(props, parts):
        fm.append("%s: %s" % (pr, yq(part["v"])))
        if part.get("s"):
            fm.append("%s_suffix: %s" % (pr, yq(part["s"])))
    fm += ["source: " + yq("%s.md" % note),
           "tags: [settlements/record, settlements/%s]" % tag,
           "---", "", "# " + label, ""]
    body = next((pt["v"] for pt, n in zip(parts, props)
                 if n in ("effect", "notes", "what_it_does", "result", "payload",
                          "trigger_effect", "description")), "")
    fm += [body, "",
           "*Record. These properties are the source of truth — "
           "`records.py` regenerates the table in [[%s]] from them.*" % note, ""]
    io.open(os.path.join(out, key + ".md"), "w",
            encoding="utf-8", newline="").write(chr(10).join(fm))
    return key



def explode_one(folder, note, section_re, want_index, tag):
    tables = find_tables(note, section_re, want_index)
    if not tables:
        tables = find_bullets(note, section_re)
    if not tables:
        return None
    out = catalogue_folder(folder)
    os.makedirs(out, exist_ok=True)

    schema = {"note": note, "section": section_re, "index": want_index,
              "tag": tag, "tables": []}
    written, seen = 0, {}

    for t_i, t in enumerate(tables):
        props = [slug(h) for h in t["head"]]
        pats = []
        for c in range(len(t["head"])):
            col = [r[c] if c < len(r) else "" for r in t["rows"]]
            pats.append(column_pattern(col))
        if t.get("bullet"):
            schema["tables"].append({"head": t["head"], "props": props,
                                     "patterns": [{"kind": "raw"}] * len(props),
                                     "lines": t["lines"], "bullet": True,
                                     "seps": t["seps"], "leads": t["leads"]})
            for r_i, (row, ln) in enumerate(zip(t["rows"], t["lines"])):
                write_record(out, folder, note, tag, t_i, r_i, len(row),
                             props, [{"v": row[0], "s": ""}, {"v": row[1], "s": ""}],
                             row[0], seen)
                written += 1
            continue
        schema["tables"].append({"head": t["head"], "props": props,
                                 "patterns": pats, "lines": t["lines"],
                                 "pad": t["pad"], "widths": t["widths"],
                                 "rowpad": t["rowpad"],
                                 "rowspaced": t["rowspaced"],
                                 "callout": t["callout"]})

        for r_i, (row, ln) in enumerate(zip(t["rows"], t["lines"])):
            parts = [decompose(row[c], pats[c]) for c in range(len(row))]
            write_record(out, folder, note, tag, t_i, r_i, len(row), props, parts,
                         parts[0]["v"], seen)
            written += 1

    io.open(os.path.join(out, "_schema.json"), "w", encoding="utf-8",
            newline="").write(json.dumps(schema, indent=1, ensure_ascii=False))
    io.open(os.path.join(ROOT, folder + ".base"), "w", encoding="utf-8",
            newline="").write(make_base(folder, schema))
    return written


def make_base(folder, schema):
    t = schema["tables"][0]
    props = t["props"]
    typ = slug(folder).replace("_", "-")
    cols = [p for p in props[:6]]
    y = ["views:", "  - type: table", "    name: All", "    filters:", "      and:",
         '        - type == "%s"' % typ, "    order:", "      - file.name"]
    y += ["      - %s" % p for p in cols[1:]]
    # a second view grouped on the first short column that looks categorical
    cat = next((p for p in props[1:5]
                if p in ("tier", "class", "kind", "category", "role", "group",
                         "build", "type", "state", "stat")), None)
    if cat:
        y += ["  - type: table", "    name: By " + cat, "    filters:", "      and:",
              '        - type == "%s"' % typ, "    order:", "      - " + cat,
              "      - file.name"] + ["      - %s" % p for p in cols[1:] if p != cat]
        y += ["    sort:", "      - property: " + cat, "        direction: ASC"]
    return "\n".join(y) + "\n"


def rebuild_one(folder):
    """Regenerate every row of a catalogue from its records."""
    out = catalogue_folder(folder)
    sp = os.path.join(out, "_schema.json")
    if not os.path.exists(sp):
        return []
    schema = json.load(io.open(sp, encoding="utf-8"))
    recs = {}
    for f in os.listdir(out):
        if not f.endswith(".md"):
            continue
        txt = io.open(os.path.join(out, f), encoding="utf-8").read()
        if not txt.startswith("---"):
            continue
        d = {}
        for line in txt.split("---", 2)[1].strip().split("\n"):
            if ":" not in line:
                continue
            k, v = line.split(":", 1)
            v = v.strip()
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
            d[k.strip()] = v
        if "table" in d and "row" in d:
            recs[(int(d["table"]), int(d["row"]))] = d

    result = []
    for t_i, t in enumerate(schema["tables"]):
        for r_i, ln in enumerate(t["lines"]):
            d = recs.get((t_i, r_i))
            if d is None:
                result.append((ln, None))
                continue
            if t.get("bullet"):
                lead = t["leads"][r_i] if r_i < len(t["leads"]) else "- "
                sep = t["seps"][r_i] if r_i < len(t["seps"]) else " — "
                result.append((ln, "%s**%s**%s%s" % (lead, d.get("name", ""), sep,
                                                     d.get("description", ""))))
                continue
            n = int(d.get("cols", len(t["props"])))
            cells = []
            for p, pat in zip(t["props"][:n], t["patterns"][:n]):
                cells.append(compose({"v": d.get(p, ""), "s": d.get(p + "_suffix", "")}, pat))
            co = t.get("callout") or []
            pre = "> " if (r_i < len(co) and co[r_i]) else ""
            rs = t.get("rowspaced") or []
            spaced = rs[r_i] if r_i < len(rs) else t.get("pad", True)
            w = (t.get("rowpad") or [])[r_i] if r_i < len(t.get("rowpad") or []) else None
            if w and any(x > 2 for x in w):
                out_cells = []
                for k, c in enumerate(cells):
                    tgt = w[k] if k < len(w) else 0
                    cell = (" %s " % c) if spaced else c
                    out_cells.append(cell.ljust(tgt))
                result.append((ln, pre + "|" + "|".join(out_cells) + "|"))
            elif spaced:
                result.append((ln, pre + "| " + " | ".join(cells) + " |"))
            else:
                result.append((ln, pre + "|" + "|".join(cells) + "|"))
    return result


def verify_one(folder, note):
    src = lines_of(note)
    rows = rebuild_one(folder)
    bad = []
    for ln, got in rows:
        if got is None or got != src[ln]:
            bad.append((ln, src[ln], got))
    return len(rows), bad


def cmd_explode():
    os.makedirs(ROOT, exist_ok=True)
    total = 0
    for folder, note, sec, idx, tag in CATALOGUES:
        n = explode_one(folder, note, sec, idx, tag)
        if n is None:
            print("  %-24s NO TABLE FOUND — check the section pattern" % folder)
            continue
        total += n
        print("  %-24s %3d records" % (folder, n))
    print("\n%d records across %d catalogues -> %s" % (total, len(CATALOGUES), ROOT))


def cmd_verify():
    ok = bad_total = 0
    failed = []
    for folder, note, sec, idx, tag in CATALOGUES:
        if not os.path.exists(os.path.join(catalogue_folder(folder), "_schema.json")):
            continue
        n, bad = verify_one(folder, note)
        if bad:
            failed.append((folder, note, n, bad))
            bad_total += len(bad)
        else:
            ok += n
        print("  %-24s %3d rows  %s" % (folder, n, "OK" if not bad else "%d FAIL" % len(bad)))
    print("\n%d rows round-trip byte-for-byte." % ok)
    if failed:
        print("%d rows do NOT. Those catalogues are not safe to make authoritative:\n" % bad_total)
        for folder, note, n, bad in failed:
            print("  %s (%s)" % (folder, note))
            for ln, want, got in bad[:3]:
                print("    line %d" % ln)
                print("      want: %s" % (want or "")[:150])
                print("      got : %s" % (got or "<missing record>")[:150])
        return 1
    return 0


# Bands mirror the Rules Wall so the two stay legible against each other.
CANVAS_BANDS = [
    ("Core engine", ["Reactions"]),
    ("Combat", ["Conditions"]),
    ("Gear", ["Weapon Classes", "Weapon Characteristics", "Armour", "Hacking Gear",
              "Sample Armoury", "Turrets", "Mines", "Traps", "Beacons"]),
    ("Terrain & machines", ["Terrain", "Terrain Verbs", "Infrastructure"]),
    ("Crew", ["Skills"]),
    ("Campaign & settlement", ["Structures", "Worker Benefits", "Loot Table",
                               "Events", "Factions"]),
]

CARD_W, CARD_H, GAP, PAD = 460, 560, 40, 60


def cmd_canvas():
    """One canvas holding every catalogue Base, grouped into bands."""
    nodes, y, n = [], 0, 0
    for band, cats in CANVAS_BANDS:
        cats = [c for c in cats
                if os.path.exists(os.path.join(ROOT, c + ".base"))]
        if not cats:
            continue
        cols = min(len(cats), 5)
        rows = (len(cats) + cols - 1) // cols
        gw = cols * CARD_W + (cols - 1) * GAP + PAD * 2
        gh = rows * CARD_H + (rows - 1) * GAP + PAD * 2 + 20
        n += 1
        nodes.append({"id": "g%d" % n, "type": "group", "label": band,
                      "x": 0, "y": y, "width": gw, "height": gh})
        for k, c in enumerate(cats):
            n += 1
            nodes.append({
                "id": "n%d" % n, "type": "file",
                "file": "Settlements/Records/%s.base" % c,
                "x": PAD + (k % cols) * (CARD_W + GAP),
                "y": y + PAD + 20 + (k // cols) * (CARD_H + GAP),
                "width": CARD_W, "height": CARD_H})
        y += gh + GAP * 2

    out = os.path.join(VAULT, "Records", "_All Catalogues.canvas")
    io.open(out, "w", encoding="utf-8", newline="").write(
        json.dumps({"nodes": nodes, "edges": []}, indent=1, ensure_ascii=False))
    bases = len([x for x in nodes if x["type"] == "file"])
    print("wrote %s" % out)
    print("  %d Base widgets in %d bands" % (bases, len(CANVAS_BANDS)))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "verify"
    if cmd == "explode":
        cmd_explode()
    elif cmd == "canvas":
        cmd_canvas()
    elif cmd == "rebuild":
        for ln, r in rebuild_one(sys.argv[2]):
            print("%5d  %s" % (ln, r))
    else:
        sys.exit(cmd_verify())
