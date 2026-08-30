"""Render docs/CATALOGUE-MASTER.md into a standalone Artifact page.

    py -3.13 scripts/catalogue_to_html.py <out.html>

Deliberately a small hand-rolled converter rather than a dependency: the source
is generated markdown with a known, narrow feature set (tables, callouts, lists,
inline emphasis, wikilinks), and pinning the output shape matters more than
covering the whole CommonMark surface.
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "catalogue.html")
# optional second arg selects a different source doc; defaults to the master catalogue
SRC = (sys.argv[2] if len(sys.argv) > 2
       else os.path.normpath(os.path.join(HERE, "..", "docs", "CATALOGUE-MASTER.md")))
TITLE = os.path.splitext(os.path.basename(SRC))[0].replace("-", " ").title()

CALLOUT = {"success": ("ok", "Ruled"), "warning": ("warn", "Watch"),
           "danger": ("bad", "Superseded"), "info": ("info", "Note"),
           "tip": ("tip", "Proposed"), "note": ("info", "Note")}


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"<span class='wl'>\2</span>", t)
    t = re.sub(r"\[\[([^\]]+)\]\]", r"<span class='wl'>\1</span>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    return t


def split_row(line):
    """Split a table row on cell pipes only.

    A pipe inside a wikilink alias ([[Note#Head|Label]]) or inline code is not a
    cell boundary, so mask those spans before splitting and restore afterwards.
    """
    sent = chr(1)
    masked = re.sub(r"\[\[[^\]]*\]\]|`[^`]*`",
                    lambda m: m.group(0).replace("|", sent), line)
    masked = masked.replace(chr(92) + "|", sent)
    return [c.strip().replace(sent, "|") for c in masked.strip("|").split("|")]


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def convert(md):
    lines = md.splitlines()
    out, i, toc = [], 0, []
    while i < len(lines):
        ln = lines[i]

        if re.match(r"^\^tbl-", ln) or ln.strip() == "---":
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)", ln)
        if m:
            lvl, txt = len(m.group(1)), m.group(2).strip()
            if lvl == 1:
                i += 1
                continue
            sid = slug(txt)
            if lvl == 2:
                toc.append((sid, txt))
            out.append(f"<h{lvl} id='{sid}'>{inline(txt)}</h{lvl}>")
            i += 1
            continue

        # callout
        m = re.match(r"^>\s*\[!(\w+)\]\s*(.*)", ln)
        if m:
            kind, title = m.group(1).lower(), m.group(2).strip()
            cls, dflt = CALLOUT.get(kind, ("info", "Note"))
            i += 1
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(re.sub(r"^>\s?", "", lines[i]))
                i += 1
            inner = convert_block("\n".join(buf))
            lbl = inline(title) if title else dflt
            out.append(f"<aside class='co co-{cls}'><p class='co-t'>{lbl}</p>{inner}</aside>")
            continue

        # blockquote
        if ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(re.sub(r"^>\s?", "", lines[i]))
                i += 1
            out.append(f"<blockquote>{convert_block(chr(10).join(buf))}</blockquote>")
            continue

        # table
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1]):
            head = split_row(ln)
            aligns = []
            for c in lines[i + 1].strip("|").split("|"):
                c = c.strip()
                aligns.append("center" if c.startswith(":") and c.endswith(":")
                              else "right" if c.endswith(":") else "left")
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            th = "".join(f"<th style='text-align:{aligns[k] if k < len(aligns) else 'left'}'>{inline(c)}</th>"
                         for k, c in enumerate(head))
            tb = ""
            for r in rows:
                tds = "".join(f"<td style='text-align:{aligns[k] if k < len(aligns) else 'left'}'>{inline(c)}</td>"
                              for k, c in enumerate(r))
                tb += f"<tr>{tds}</tr>"
            out.append(f"<div class='tw'><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>")
            continue

        # lists
        if re.match(r"^\s*[-*]\s+", ln) or re.match(r"^\s*\d+\.\s+", ln):
            ordered = bool(re.match(r"^\s*\d+\.\s+", ln))
            items = []
            while i < len(lines) and (re.match(r"^\s*[-*]\s+", lines[i])
                                      or re.match(r"^\s*\d+\.\s+", lines[i])
                                      or (lines[i].strip() and lines[i].startswith("  ")
                                          and items)):
                cur = lines[i]
                if re.match(r"^\s*[-*]\s+", cur) or re.match(r"^\s*\d+\.\s+", cur):
                    items.append(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", cur))
                else:
                    items[-1] += " " + cur.strip()
                i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue

        if not ln.strip():
            i += 1
            continue

        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^(#{1,4}\s|>|\||\s*[-*]\s|\s*\d+\.\s|\^tbl-)", lines[i]) and lines[i].strip() != "---":
            buf.append(lines[i])
            i += 1
        if buf:
            out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n".join(out), toc


def convert_block(md):
    return convert(md)[0]


md = open(SRC, encoding="utf-8").read()
bodyhtml, toc = convert(md)

nav = "".join(f"<a href='#{sid}'>{html.escape(t)}</a>" for sid, t in toc)

STYLE = """
:root{
 --ground:#F1F3F2;--surface:#FFFFFF;--sunk:#E7EAE9;--ink:#14181C;--muted:#5A636B;
 --faint:#7C858C;--rule:#D2D7D6;--rule-soft:#E2E6E5;--accent:#2E5C7A;
 --ok:#2F6E55;--warn:#B06D10;--bad:#AC3327;--tip:#7B7222;
 --f-disp:"Barlow Condensed","Arial Narrow",Helvetica,sans-serif;
 --f-body:"Source Serif 4",Georgia,serif;
 --f-mono:"IBM Plex Mono",ui-monospace,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --ground:#11151A;--surface:#181D24;--sunk:#1F252D;--ink:#E5E9E7;--muted:#9BA5AD;
 --faint:#7D878F;--rule:#2B323A;--rule-soft:#232A32;--accent:#79ACCB;
 --ok:#6BB394;--warn:#DCA245;--bad:#E07364;--tip:#BDB055;}}
:root[data-theme="dark"]{
 --ground:#11151A;--surface:#181D24;--sunk:#1F252D;--ink:#E5E9E7;--muted:#9BA5AD;
 --faint:#7D878F;--rule:#2B323A;--rule-soft:#232A32;--accent:#79ACCB;
 --ok:#6BB394;--warn:#DCA245;--bad:#E07364;--tip:#BDB055;}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--f-body);
 font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.shell{display:grid;grid-template-columns:15.5rem minmax(0,1fr);gap:2.6rem;
 max-width:82rem;margin:0 auto;padding:2.6rem 1.4rem 5rem}
nav{position:sticky;top:1.4rem;align-self:start;max-height:calc(100vh - 3rem);
 overflow-y:auto;border-right:1px solid var(--rule);padding-right:1rem}
nav .nt{font-family:var(--f-mono);font-size:.62rem;letter-spacing:.15em;
 text-transform:uppercase;color:var(--faint);margin-bottom:.75rem;font-weight:600}
nav a{display:block;font-family:var(--f-disp);font-size:.97rem;color:var(--muted);
 text-decoration:none;padding:.2rem 0;line-height:1.25;border-left:2px solid transparent;
 padding-left:.6rem;margin-left:-.6rem}
nav a:hover,nav a:focus-visible{color:var(--accent);border-left-color:var(--accent)}
main{min-width:0}
h1{font-family:var(--f-disp);font-weight:700;font-size:clamp(2.3rem,6vw,3.4rem);
 line-height:.96;margin:0 0 .5rem;letter-spacing:-.012em}
h2{font-family:var(--f-disp);font-weight:700;font-size:clamp(1.5rem,3.6vw,2rem);
 line-height:1.08;margin:3.2rem 0 .5rem;padding-top:1.4rem;border-top:2px solid var(--ink);
 text-wrap:balance;scroll-margin-top:1.4rem}
h3{font-family:var(--f-disp);font-weight:600;font-size:1.24rem;margin:2rem 0 .4rem;
 color:var(--ink);scroll-margin-top:1.4rem}
h4{font-family:var(--f-mono);font-weight:600;font-size:.72rem;letter-spacing:.12em;
 text-transform:uppercase;color:var(--faint);margin:1.5rem 0 .4rem}
p{margin:0 0 .95rem;max-width:74ch}
ul,ol{margin:0 0 1rem;padding-left:1.15rem;max-width:74ch}
li{margin-bottom:.35rem}
a{color:var(--accent)}
code{font-family:var(--f-mono);font-size:.855em;background:var(--sunk);
 padding:.08em .34em;border-radius:2px}
.wl{font-family:var(--f-disp);font-size:1.04em;color:var(--accent);
 border-bottom:1px dotted currentColor}
strong{font-weight:600}
.tw{overflow-x:auto;margin:.9rem 0 1.5rem;border:1px solid var(--rule);background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:.855rem;font-variant-numeric:tabular-nums}
th,td{padding:.52rem .72rem;border-bottom:1px solid var(--rule-soft);vertical-align:top}
thead th{font-family:var(--f-mono);font-size:.6rem;letter-spacing:.11em;text-transform:uppercase;
 color:var(--faint);font-weight:600;background:var(--sunk);border-bottom:1px solid var(--rule);
 white-space:nowrap;position:sticky;top:0}
tbody tr:last-child td{border-bottom:0}
tbody tr:hover{background:var(--sunk)}
blockquote{margin:0 0 1.1rem;padding-left:1rem;border-left:2px solid var(--rule);
 color:var(--muted);max-width:74ch}
blockquote p:last-child{margin-bottom:0}
.co{background:var(--surface);border:1px solid var(--rule);border-left:3px solid var(--cc,var(--accent));
 padding:.85rem 1rem .1rem;margin:0 0 1.2rem;max-width:74ch;font-size:.93rem}
.co-t{font-family:var(--f-mono);font-size:.62rem;letter-spacing:.13em;text-transform:uppercase;
 color:var(--cc,var(--accent));font-weight:600;margin-bottom:.45rem}
.co-t strong{font-weight:600}
.co-ok{--cc:var(--ok)}.co-warn{--cc:var(--warn)}.co-bad{--cc:var(--bad)}
.co-tip{--cc:var(--tip)}.co-info{--cc:var(--accent)}
.co table{font-size:.8rem}
header.mast{border-bottom:2px solid var(--ink);padding-bottom:1.1rem;margin-bottom:1.6rem}
.eyebrow{font-family:var(--f-mono);font-size:.645rem;letter-spacing:.16em;text-transform:uppercase;
 color:var(--faint);display:flex;flex-wrap:wrap;gap:.4rem 1.1rem;margin-bottom:.7rem}
.lede{color:var(--muted);font-size:.97rem;max-width:70ch;margin:0}
@media (max-width:900px){
 .shell{grid-template-columns:1fr;gap:1.4rem}
 nav{position:static;max-height:none;border-right:0;border-bottom:1px solid var(--rule);
  padding-right:0;padding-bottom:1rem;display:flex;flex-wrap:wrap;gap:.15rem .9rem}
 nav .nt{width:100%}
 nav a{border-left:0;padding-left:0;margin-left:0;font-size:.9rem}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

page = f"""<title>{TITLE}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">
<style>{STYLE}</style>
<div class="shell">
<nav><div class="nt">Catalogues</div>{nav}</nav>
<main>
<header class="mast">
  <div class="eyebrow"><span>Settlements</span><span>Pre-alpha</span><span>Generated from the rules vault</span><span>2026-08-29</span></div>
  <h1>{TITLE}</h1>
  <p class="lede">Every catalogue in the game with its stats, costs and rules, pulled straight out of the Obsidian vault by <code>build_catalogue_master.py</code>. Nothing here is retyped, so it cannot drift from source — regenerate after any catalogue change.</p>
</header>
{bodyhtml}
</main>
</div>
"""

with open(OUT, "w", encoding="utf-8", newline="") as f:
    f.write(page)
print(f"wrote {OUT}  ({len(page):,} bytes, {len(toc)} sections)")
