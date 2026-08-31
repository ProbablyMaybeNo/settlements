"""Prototype: weapon characteristics as note records, and back again.

    py -3.13 scripts/records_weapon_chars.py explode   # table  -> 23 notes + a .base
    py -3.13 scripts/records_weapon_chars.py rebuild   # notes  -> the markdown table
    py -3.13 scripts/records_weapon_chars.py verify    # round-trip, byte-for-byte

The whole architecture rests on `verify`. If records regenerate the exact table
they came from, then frontmatter can safely become the source of truth and
`Full Rules System v1` keeps its tables as generated output — the rulebook still
builds, and Bases/Dashboard Hub get something they can actually edit.

If verify ever fails, STOP: it means a cell carries formatting the schema does
not model, and converting the rest of the catalogues would quietly lose it.
"""
import io
import os
import re
import sys

VAULT = os.path.join(os.path.expanduser("~"), "Documents", "Obsidian Vault", "Settlements")
RULES = os.path.join(VAULT, "Rules System")
SRC = os.path.join(RULES, "Weapons.md")
OUT = os.path.join(VAULT, "Records", "Weapon Characteristics")
BASE = os.path.join(VAULT, "Records", "Weapon Characteristics.base")

SECTION_START = "## 2 · Characteristics"
SECTION_END = "## 3 · Armor"


def source_lines():
    return io.open(SRC, encoding="utf-8", newline="").read().split("\n")


def parse():
    """Every characteristic row, with its group heading and source line number."""
    lines = source_lines()
    a = next(i for i, l in enumerate(lines) if l.startswith(SECTION_START))
    b = next(i for i in range(a + 1, len(lines)) if lines[i].startswith(SECTION_END))
    recs, group, kind, i = [], "", "characteristic", a
    while i < b:
        l = lines[i]
        h = re.match(r"^###\s+(.*)", l)
        if h:
            group = re.sub(r"[*]", "", h.group(1)).split("—")[0].strip()
            kind = "drawback" if "Drawback" in h.group(1) else "characteristic"
            i += 1
            continue
        if l.startswith("| **"):
            cells = [c.strip() for c in l.strip("|").split("|")]
            name = cells[0].strip("*").strip()

            # cost cell: "**10**", "**5**/step", "**−5** *(−10 on Heavy Ranged)*"
            m = re.match(r"^\*\*(−?-?\d+)\*\*(.*)$", cells[1])
            cr = int(m.group(1).replace("−", "-")) if m else None
            cr_suffix = (m.group(2) if m else "").strip()

            if kind == "drawback":                 # no tier column on drawbacks
                tier, tier_flag, effect = "", "", cells[2]
            else:
                t = cells[2]
                tm = re.match(r"^\*\*([^*]+)\*\*\s*(.*)$", t)
                tier = (tm.group(1) if tm else t).strip()
                tier_flag = (tm.group(2) if tm else "").strip()
                effect = cells[3]

            recs.append({"name": name, "group": group, "kind": kind, "cr": cr,
                         "cr_suffix": cr_suffix, "tier": tier, "tier_flag": tier_flag,
                         "effect": effect, "line": i})
        i += 1
    return recs


def row(r):
    """Rebuild one markdown row from a record. Inverse of parse()."""
    cr = "" if r["cr"] is None else "**%s**" % str(r["cr"]).replace("-", "−")
    if r["cr_suffix"]:
        cr += r["cr_suffix"] if r["cr_suffix"].startswith("/") else " " + r["cr_suffix"]
    if r["kind"] == "drawback":
        return "| **%s** | %s | %s |" % (r["name"], cr, r["effect"])
    tier = "**%s**" % r["tier"] + ((" " + r["tier_flag"]) if r["tier_flag"] else "")
    return "| **%s** | %s | %s | %s |" % (r["name"], cr, tier, r["effect"])


def yaml_str(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def explode():
    os.makedirs(OUT, exist_ok=True)
    recs = parse()
    for r in recs:
        fm = [
            "---",
            "type: weapon-characteristic",
            "name: " + yaml_str(r["name"]),
            "group: " + yaml_str(r["group"]),
            "kind: " + r["kind"],
            "cr: " + ("" if r["cr"] is None else str(r["cr"])),
            "cr_suffix: " + yaml_str(r["cr_suffix"]),
            "tier: " + yaml_str(r["tier"]),
            "tier_flag: " + yaml_str(r["tier_flag"]),
            "effect: " + yaml_str(r["effect"]),
            "source: " + yaml_str("Weapons.md §2 · Characteristics"),
            "tags: [settlements/record, settlements/gear/characteristic]",
            "---",
            "",
            "# " + r["name"],
            "",
            r["effect"],
            "",
            "*Record note. The value of every property above is the source of truth —",
            "`records_weapon_chars.py rebuild` regenerates the markdown table in",
            "[[Weapons]] §2 from these. Edit here (or in the Base), not in the table.*",
            "",
        ]
        path = os.path.join(OUT, r["name"].replace("/", "-") + ".md")
        io.open(path, "w", encoding="utf-8", newline="").write("\n".join(fm))

    io.open(BASE, "w", encoding="utf-8", newline="").write(BASE_YAML)
    print("wrote %d record notes -> %s" % (len(recs), OUT))
    print("wrote the Base            -> %s" % BASE)


def load_records():
    recs = []
    for f in sorted(os.listdir(OUT)):
        if not f.endswith(".md"):
            continue
        txt = io.open(os.path.join(OUT, f), encoding="utf-8").read()
        fm = txt.split("---", 2)[1]
        d = {}
        for line in fm.strip().split("\n"):
            if ":" not in line:
                continue
            k, v = line.split(":", 1)
            v = v.strip()
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
            d[k.strip()] = v
        d["cr"] = int(d["cr"]) if d.get("cr") not in (None, "") else None
        recs.append(d)
    return recs


def rebuild():
    """Regenerate every row from the records, in the source's own order."""
    by_name = {r["name"]: r for r in load_records()}
    out = []
    for r in parse():                       # parse() supplies order + line numbers
        rec = by_name.get(r["name"])
        out.append((r["line"], row(rec) if rec else None))
    return out


def verify():
    lines = source_lines()
    bad = 0
    for ln, rebuilt in rebuild():
        if rebuilt is None:
            print("  MISSING record for line %d" % ln)
            bad += 1
            continue
        if rebuilt != lines[ln]:
            bad += 1
            print("  line %d DIFFERS" % ln)
            print("    original : %s" % lines[ln])
            print("    rebuilt  : %s" % rebuilt)
    n = len(list(rebuild()))
    if bad:
        print("\n%d of %d rows do not round-trip. DO NOT convert further." % (bad, n))
        return 1
    print("all %d rows round-trip byte-for-byte." % n)
    print("frontmatter can safely be the source of truth for this catalogue.")
    return 0


BASE_YAML = """views:
  - type: table
    name: All characteristics
    filters:
      and:
        - type == "weapon-characteristic"
    order:
      - file.name
      - cr
      - tier
      - group
      - effect
    sort:
      - property: cr
        direction: DESC
  - type: table
    name: By tier
    filters:
      and:
        - type == "weapon-characteristic"
    order:
      - file.name
      - tier
      - cr
      - effect
    sort:
      - property: tier
        direction: ASC
  - type: table
    name: Drawbacks - refunds
    filters:
      and:
        - type == "weapon-characteristic"
        - kind == "drawback"
    order:
      - file.name
      - cr
      - effect
  - type: table
    name: Untiered - the costing gap
    filters:
      and:
        - type == "weapon-characteristic"
        - tier == ""
    order:
      - file.name
      - cr
      - kind
      - effect
"""

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "verify"
    if cmd == "explode":
        explode()
    elif cmd == "rebuild":
        for ln, r in rebuild():
            print("%4d  %s" % (ln, r))
    else:
        sys.exit(verify())
