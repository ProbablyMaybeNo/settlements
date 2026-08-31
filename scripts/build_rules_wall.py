"""Render every table in the rules system onto ONE pan-and-zoom wall.

    py -3.13 scripts/build_rules_wall.py <out.html> [--repo]

Everything visible at once, nothing collapsed, nothing filtered. A vertical
document was the wrong shape for this — you cannot compare Deployables against
Weapons by scrolling past one to reach the other — so the wall is a wide 2D
tiling you pan and zoom, with related catalogues banded together by colour.

Pulls tables AND bullet-list catalogues (Skills, Conditions, Infrastructure are
written as bullets, not tables, and a table-only sweep misses them entirely).
"""
import html
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.join(os.path.expanduser("~"), "Documents", "Obsidian Vault",
                     "Settlements", "Rules System")
MIRROR = os.path.normpath(os.path.join(HERE, "..", "rules-vault", "Rules System"))
ROOT = MIRROR if "--repo" in sys.argv else VAULT
# Wall width in px. Bands wrap inside it, so this is what sets the overall
# aspect ratio. Unbounded it came out ~2.8:1; 6400 over-corrected to 1.1:1 and
# left the width empty. 11000 lands near 2.1:1, which is roughly a monitor.
WALL_W = 11000

OUT = next((a for a in sys.argv[1:] if not a.startswith("--")),
           os.path.join(HERE, "rules-wall.html"))

# Which notes sit in which band, in reading order. Anything not listed is
# skipped: sim findings, guides, roadmaps and the master doc all duplicate or
# discuss the phase notes rather than holding catalogue content.
BANDS = [
    ("Core engine", "eng", ["Rules Engine", "Core Game Format", "Initiative & Activation"]),
    ("Combat", "cbt", ["Shooting", "Melee", "Damage", "Morale", "Conditions"]),
    ("Gear", "ger", ["Weapons", "Deployables"]),
    ("Movement · terrain · machines", "ter",
     ["Movement", "Terrain", "Terrain Interaction", "Infrastructure", "Hacking"]),
    ("Crew", "crw", ["Unit Design", "List Building", "Progression", "Skill Paths"]),
    ("Campaign & settlement", "cmp",
     ["Campaign", "Downtime", "Economy", "Settlement", "Structures", "Territory",
      "Events", "Scenarios", "Factions"]),
    ("Physical", "phy", ["Board Representation", "Components"]),
]


def read(note):
    path = os.path.join(ROOT, note + ".md")
    if not os.path.exists(path):
        return None
    return io.open(path, encoding="utf-8").read()


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\[\[[^\]|]*\|([^\]]+)\]\]", r"<i>\1</i>", t)
    t = re.sub(r"\[\[([^\]#|]+)(?:#[^\]]*)?\]\]", r"<i>\1</i>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![*\w])\*(?!\s)([^*\n]+?)\*(?!\w)", r"<em>\1</em>", t)
    return t


def split_row(line):
    """Split on cell pipes only — a wikilink alias puts a pipe inside a cell."""
    sent = chr(1)
    masked = re.sub(r"\[\[[^\]]*\]\]|`[^`]*`",
                    lambda m: m.group(0).replace("|", sent), line)
    return [c.strip().replace(sent, "|") for c in masked.strip("|").split("|")]


def harvest(note):
    """Every table and bullet-catalogue in a note, tagged with its section."""
    text = read(note)
    if not text:
        return []
    lines = text.splitlines()
    out, section, i = [], "", 0
    while i < len(lines):
        raw = lines[i]
        bare = re.sub(r"^>\s?", "", raw)

        h = re.match(r"^#{2,4}\s+(.*)", bare)
        if h:
            section = re.sub(r"[*`]|\[\[|\]\]", "", h.group(1)).strip()
            i += 1
            continue

        nxt = re.sub(r"^>\s?", "", lines[i + 1]) if i + 1 < len(lines) else ""
        if bare.startswith("|") and re.match(r"^\|[\s:|-]+\|?$", nxt):
            head = split_row(bare)
            aligns = ["center" if c.strip().startswith(":") and c.strip().endswith(":")
                      else "right" if c.strip().endswith(":") else "left"
                      for c in nxt.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines):
                b = re.sub(r"^>\s?", "", lines[i])
                if not b.startswith("|"):
                    break
                rows.append(split_row(b))
                i += 1
            if rows:
                out.append(("table", section, head, aligns, rows))
            continue

        # bullet catalogue: four or more consecutive "- **Name** — ..." lines
        if re.match(r"^\s*-\s+\*\*", bare):
            j, items = i, []
            while j < len(lines):
                b = re.sub(r"^>\s?", "", lines[j])
                m = re.match(r"^\s*-\s+\*\*([^*]+)\*\*\s*[—:-]?\s*(.*)", b)
                if not m:
                    break
                items.append((m.group(1).strip(), m.group(2).strip()))
                j += 1
            if len(items) >= 4:
                out.append(("list", section, None, None, items))
                i = j
                continue
        i += 1
    return out


# --------------------------------------------------------------------------
cards, stats = [], {"tables": 0, "lists": 0, "rows": 0}
for band, cls, notes in BANDS:
    band_cards = []
    for note in notes:
        for kind, section, head, aligns, rows in harvest(note):
            stats["rows"] += len(rows)
            stats["tables" if kind == "table" else "lists"] += 1
            title = section or note
            if kind == "table":
                th = "".join(
                    f"<th style='text-align:{aligns[k] if k < len(aligns) else 'left'}'>{inline(c)}</th>"
                    for k, c in enumerate(head))
                tb = "".join(
                    "<tr>" + "".join(
                        f"<td style='text-align:{aligns[k] if k < len(aligns) else 'left'}'>{inline(c)}</td>"
                        for k, c in enumerate(r)) + "</tr>"
                    for r in rows)
                body = f"<table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table>"
            else:
                body = "<dl>" + "".join(
                    f"<dt>{inline(n)}</dt><dd>{inline(d)}</dd>" for n, d in rows) + "</dl>"
            band_cards.append(
                f"<article class='card'><header><span class='src'>{html.escape(note)}</span>"
                f"<h3>{inline(title)}</h3></header>{body}"
                f"<footer>{len(rows)} {'rows' if kind == 'table' else 'entries'}</footer></article>")
    if band_cards:
        cards.append(
            f"<section class='band {cls}'><h2><span>{html.escape(band)}</span>"
            f"<small>{len(band_cards)} tables</small></h2>"
            f"<div class='tiles'>{''.join(band_cards)}</div></section>")

TOTAL = stats["tables"] + stats["lists"]

STYLE = """
:root{
 --ground:#EFF1F0;--surface:#FFFFFF;--sunk:#E6EAE8;--ink:#14181C;--muted:#5A636B;
 --faint:#828B92;--rule:#D0D5D3;--soft:#E4E8E6;--accent:#2E5C7A;
 --eng:#2E5C7A;--cbt:#AC3327;--ger:#B06D10;--ter:#2F6E55;--crw:#6B4C8A;--cmp:#7B7222;--phy:#4A5D68;
 --disp:"Barlow Condensed","Arial Narrow",Helvetica,sans-serif;
 --body:"Source Serif 4",Georgia,serif;
 --mono:"IBM Plex Mono",ui-monospace,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --ground:#0F1216;--surface:#171B21;--sunk:#1E242B;--ink:#E6E9E7;--muted:#9AA4AC;
 --faint:#79838B;--rule:#2A313A;--soft:#222932;--accent:#79ACCB;
 --eng:#79ACCB;--cbt:#E07364;--ger:#DCA245;--ter:#6BB394;--crw:#B394D4;--cmp:#BDB055;--phy:#8FA4B0;}}
:root[data-theme="dark"]{
 --ground:#0F1216;--surface:#171B21;--sunk:#1E242B;--ink:#E6E9E7;--muted:#9AA4AC;
 --faint:#79838B;--rule:#2A313A;--soft:#222932;--accent:#79ACCB;
 --eng:#79ACCB;--cbt:#E07364;--ger:#DCA245;--ter:#6BB394;--crw:#B394D4;--cmp:#BDB055;--phy:#8FA4B0;}
*{box-sizing:border-box}
html,body{margin:0;height:100%;overflow:hidden;background:var(--ground);color:var(--ink);
 font-family:var(--body);-webkit-font-smoothing:antialiased}

#bar{position:fixed;inset:0 0 auto 0;height:46px;z-index:20;display:flex;align-items:center;
 gap:.55rem;padding:0 .8rem;background:var(--surface);border-bottom:1px solid var(--rule)}
#bar .ttl{font-family:var(--disp);font-weight:700;font-size:1.12rem;white-space:nowrap}
#bar .meta{font-family:var(--mono);font-size:.6rem;letter-spacing:.11em;text-transform:uppercase;
 color:var(--faint);white-space:nowrap}
#bar .sp{flex:1}
button,#find{font-family:var(--mono);font-size:.66rem;letter-spacing:.06em;text-transform:uppercase;
 background:var(--sunk);color:var(--ink);border:1px solid var(--rule);border-radius:3px;
 padding:.32rem .55rem;cursor:pointer}
button:hover{border-color:var(--accent);color:var(--accent)}
button:focus-visible,#find:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
#find{text-transform:none;letter-spacing:0;width:11rem;cursor:text}
#zl{font-family:var(--mono);font-size:.62rem;color:var(--faint);min-width:3.1rem;text-align:right}
#legend{display:flex;gap:.5rem;flex-wrap:nowrap}
#legend i{font-family:var(--mono);font-size:.57rem;letter-spacing:.08em;text-transform:uppercase;
 font-style:normal;color:var(--bc);border-bottom:2px solid var(--bc);padding-bottom:1px;white-space:nowrap}

#vp{position:fixed;inset:46px 0 0 0;overflow:hidden;cursor:grab;touch-action:none}
#vp.drag{cursor:grabbing}
#wall{transform-origin:0 0;width:__WALLW__px;padding:1.5rem 1.5rem 4rem}

.band{--bc:var(--eng);margin-bottom:1.6rem}
.band.cbt{--bc:var(--cbt)}.band.ger{--bc:var(--ger)}.band.ter{--bc:var(--ter)}
.band.crw{--bc:var(--crw)}.band.cmp{--bc:var(--cmp)}.band.phy{--bc:var(--phy)}
.band>h2{font-family:var(--disp);font-weight:700;font-size:1.28rem;margin:0 0 .55rem;
 color:var(--bc);border-bottom:2px solid var(--bc);padding-bottom:.25rem;
 display:flex;align-items:baseline;gap:.6rem}
.band>h2 small{font-family:var(--mono);font-size:.58rem;letter-spacing:.11em;
 text-transform:uppercase;color:var(--faint);font-weight:400}
.tiles{display:flex;flex-wrap:wrap;align-items:flex-start;gap:.7rem}

.card{background:var(--surface);border:1px solid var(--rule);border-top:3px solid var(--bc);
 width:392px;display:flex;flex-direction:column}
.card header{padding:.42rem .55rem .3rem;border-bottom:1px solid var(--soft)}
.card .src{display:block;font-family:var(--mono);font-size:.53rem;letter-spacing:.11em;
 text-transform:uppercase;color:var(--faint)}
.card h3{font-family:var(--disp);font-weight:600;font-size:.98rem;margin:.05rem 0 0;line-height:1.12}
.card footer{font-family:var(--mono);font-size:.53rem;letter-spacing:.09em;text-transform:uppercase;
 color:var(--faint);padding:.25rem .55rem;border-top:1px solid var(--soft);margin-top:auto}
table{border-collapse:collapse;width:100%;font-size:.665rem;line-height:1.32;
 font-variant-numeric:tabular-nums}
th,td{padding:.2rem .35rem;border-bottom:1px solid var(--soft);vertical-align:top}
thead th{font-family:var(--mono);font-size:.5rem;letter-spacing:.08em;text-transform:uppercase;
 color:var(--faint);font-weight:600;background:var(--sunk)}
tbody tr:last-child td{border-bottom:0}
dl{margin:0;font-size:.665rem;line-height:1.3}
dt{font-weight:600;padding:.2rem .55rem 0;font-size:.68rem}
dd{margin:0 0 .16rem;padding:0 .55rem .18rem;color:var(--muted);border-bottom:1px solid var(--soft)}
dd:last-child{border-bottom:0}
code{font-family:var(--mono);font-size:.9em;background:var(--sunk);padding:0 .18em;border-radius:2px}
b{font-weight:600}
i{font-style:normal;color:var(--accent)}
em{font-style:italic;color:var(--muted)}

.card.hit{outline:2px solid var(--accent);outline-offset:2px}
.card.dim{opacity:.28}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

SCRIPT = """
(function(){
 var vp=document.getElementById('vp'), wall=document.getElementById('wall'),
     zl=document.getElementById('zl'), find=document.getElementById('find');
 var s=1, x=0, y=0, MIN=0.06, MAX=2.4;
 function apply(){wall.style.transform='translate('+x+'px,'+y+'px) scale('+s+')';
                  zl.textContent=Math.round(s*100)+'%';}
 function zoomAt(cx,cy,ns){ns=Math.min(MAX,Math.max(MIN,ns));
   var r=vp.getBoundingClientRect(), px=cx-r.left, py=cy-r.top;
   x=px-(px-x)*(ns/s); y=py-(py-y)*(ns/s); s=ns; apply();}
 // Measure the real ink extent, not the declared wall width: bands wrap well
 // short of WALL_W, so scaling to the container fitted a lot of empty space.
 function extent(){var w=0,h=0,wr=wall.getBoundingClientRect();
   [].forEach.call(wall.querySelectorAll('.card,.band>h2'),function(el){
     var r=el.getBoundingClientRect();
     w=Math.max(w,(r.right-wr.left)/s); h=Math.max(h,(r.bottom-wr.top)/s);});
   return [w+24,h+24];}
 function fit(){var r=vp.getBoundingClientRect(), e=extent();
   s=Math.max(Math.min((r.width-24)/e[0],(r.height-24)/e[1],1),MIN); x=12; y=12; apply();}
 vp.addEventListener('wheel',function(e){e.preventDefault();
   if(e.shiftKey){x-=e.deltaY;apply();}
   else if(e.ctrlKey||e.metaKey){zoomAt(e.clientX,e.clientY,s*(e.deltaY<0?1.12:1/1.12));}
   else{zoomAt(e.clientX,e.clientY,s*(e.deltaY<0?1.12:1/1.12));}},{passive:false});
 var down=false,lx=0,ly=0;
 vp.addEventListener('pointerdown',function(e){
   if(e.target.closest('input'))return;
   down=true;lx=e.clientX;ly=e.clientY;vp.classList.add('drag');
   try{vp.setPointerCapture(e.pointerId);}catch(_){}});
 vp.addEventListener('pointermove',function(e){if(!down)return;
   x+=e.clientX-lx;y+=e.clientY-ly;lx=e.clientX;ly=e.clientY;apply();});
 function up(){down=false;vp.classList.remove('drag');}
 vp.addEventListener('pointerup',up); vp.addEventListener('pointercancel',up);
 function ctr(f){var r=vp.getBoundingClientRect();zoomAt(r.left+r.width/2,r.top+r.height/2,f);}
 document.getElementById('zin').onclick=function(){ctr(s*1.25);};
 document.getElementById('zout').onclick=function(){ctr(s/1.25);};
 document.getElementById('z100').onclick=function(){ctr(1);};
 document.getElementById('zfit').onclick=fit;

 var cards=[].slice.call(document.querySelectorAll('.card'));
 cards.forEach(function(c){c.dataset.t=c.textContent.toLowerCase();});
 var t=null;
 function clear(){cards.forEach(function(c){c.classList.remove('hit','dim');});}
 find.addEventListener('input',function(){clearTimeout(t);t=setTimeout(function(){
   var q=find.value.trim().toLowerCase();
   if(!q){clear();return;}
   cards.forEach(function(c){var h=c.dataset.t.indexOf(q)>-1;
     c.classList.toggle('hit',h);c.classList.toggle('dim',!h);});},140);});
 find.addEventListener('keydown',function(e){if(e.key==='Escape'){find.value='';clear();find.blur();}});
 window.addEventListener('keydown',function(e){
   if(e.key==='/'&&document.activeElement!==find){e.preventDefault();find.focus();}
   if(e.key==='0'&&document.activeElement!==find){fit();}});
 if(document.fonts&&document.fonts.ready){document.fonts.ready.then(function(){requestAnimationFrame(fit);});}else{requestAnimationFrame(fit);}
 window.addEventListener('load',function(){requestAnimationFrame(fit);});
})();
"""

legend = "".join(
    "<i style='--bc:var(--{})'>{}</i>".format(cls, html.escape(name.split(" ")[0]))
    for name, cls, _ in BANDS)

page = (
    '<meta charset="utf-8">\n'
    "<title>Rules Wall</title>\n"
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
    "family=Barlow+Condensed:wght@400;600;700&family=IBM+Plex+Mono:wght@400;600&"
    'family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">\n'
    "<style>" + STYLE.replace("__WALLW__", str(WALL_W)) + "</style>\n"
    '<div id="bar">\n'
    '  <span class="ttl">Rules Wall</span>\n'
    '  <span class="meta">' + str(TOTAL) + " tables &middot; " + str(stats["rows"]) + " entries</span>\n"
    '  <div id="legend">' + legend + "</div>\n"
    '  <span class="sp"></span>\n'
    '  <input id="find" type="search" placeholder="highlight&hellip;  ( / )" aria-label="Highlight tables">\n'
    '  <button id="zout" title="Zoom out">&minus;</button>\n'
    '  <span id="zl">100%</span>\n'
    '  <button id="zin" title="Zoom in">+</button>\n'
    '  <button id="zfit" title="Fit everything (0)">Fit</button>\n'
    '  <button id="z100" title="Actual size">1:1</button>\n'
    "</div>\n"
    '<div id="vp"><div id="wall">' + "".join(cards) + "</div></div>\n"
    "<script>" + SCRIPT + "</script>\n"
)

io.open(OUT, "w", encoding="utf-8", newline="").write(page)
print("wrote " + OUT + "  ({:,} bytes)".format(len(page)))
print("  {} tables + {} bullet catalogues = {} cards, {} entries".format(
    stats["tables"], stats["lists"], TOTAL, stats["rows"]))
