"""Render every table in the rules system onto ONE pan-and-zoom wall.

    py -3.13 scripts/build_rules_wall.py <out.html> [--repo] [--editable]

Everything visible at once, nothing collapsed, nothing filtered. A vertical
document was the wrong shape — you cannot compare Deployables against Weapons by
scrolling past one to reach the other — so the wall is a wide 2D tiling you pan
and zoom, with related catalogues banded by colour.

Pulls tables AND bullet-list catalogues: Skills, Conditions and Infrastructure
are written as bullets, and a table-only sweep misses Infrastructure's 12 board
features entirely.

Every cell carries its source note and LINE NUMBER, which is what makes the wall
writable — `wall_server.py` serves it with --editable and posts each change back
into the vault note the cell came from. Import `build()` rather than shelling
out to this file.
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

# Wall width in px. Bands wrap inside it, so this sets the overall aspect ratio.
# Unbounded it came out ~2.8:1; 6400 over-corrected to 1.1:1 and left the width
# empty. 11000 lands near 2.1:1, roughly a monitor.
WALL_W = 11000

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

SENT = chr(1)


def read(root, note):
    path = os.path.join(root, note + ".md")
    return io.open(path, encoding="utf-8").read() if os.path.exists(path) else None


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
    masked = re.sub(r"\[\[[^\]]*\]\]|`[^`]*`",
                    lambda m: m.group(0).replace("|", SENT), line)
    return [c.strip().replace(SENT, "|") for c in masked.strip("|").split("|")]


def harvest(root, note):
    """Tables and bullet-catalogues in a note, each row tagged with its line no.

    The line number is what makes the wall writable: an edit knows exactly which
    line of which note produced it, so write-back never has to guess.
    """
    text = read(root, note)
    if not text:
        return []
    lines = text.splitlines()
    out, section, i = [], "", 0
    while i < len(lines):
        bare = re.sub(r"^>\s?", "", lines[i])

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
            rows, nos = [], []
            while i < len(lines):
                b = re.sub(r"^>\s?", "", lines[i])
                if not b.startswith("|"):
                    break
                rows.append(split_row(b))
                nos.append(i)
                i += 1
            if rows:
                out.append(("table", section, head, aligns, rows, nos))
            continue

        if re.match(r"^\s*-\s+\*\*", bare):
            j, items, nos = i, [], []
            while j < len(lines):
                b = re.sub(r"^>\s?", "", lines[j])
                m = re.match(r"^\s*-\s+\*\*([^*]+)\*\*\s*[—:-]?\s*(.*)", b)
                if not m:
                    break
                items.append([m.group(1).strip(), m.group(2).strip()])
                nos.append(j)
                j += 1
            if len(items) >= 4:
                out.append(("list", section, None, None, items, nos))
                i = j
                continue
        i += 1
    return out


def _cell(note, lineno, col, raw, align, tag, editable):
    """One cell, carrying enough provenance for the server to write it back."""
    if not editable:
        return "<{t} style='text-align:{a}'>{v}</{t}>".format(
            t=tag, a=align, v=inline(raw))
    return ("<{t} style='text-align:{a}' class='ed' contenteditable='plaintext-only' "
            "spellcheck='false' data-note=\"{n}\" data-line='{l}' data-col='{c}' "
            "data-raw=\"{r}\">{v}</{t}>").format(
        t=tag, a=align, n=html.escape(note, quote=True), l=lineno, c=col,
        r=html.escape(raw, quote=True), v=inline(raw))


def build(root=None, editable=False):
    """Return the whole wall as one self-contained HTML string."""
    root = root or VAULT
    cards, stats = [], {"tables": 0, "lists": 0, "rows": 0}

    for band, cls, notes in BANDS:
        band_cards = []
        for note in notes:
            for kind, section, head, aligns, rows, nos in harvest(root, note):
                stats["rows"] += len(rows)
                stats["tables" if kind == "table" else "lists"] += 1
                title = section or note

                def al(k):
                    return aligns[k] if aligns and k < len(aligns) else "left"

                if kind == "table":
                    th = "".join("<th style='text-align:{}'>{}</th>".format(al(k), inline(c))
                                 for k, c in enumerate(head))
                    tb = ""
                    for r, ln in zip(rows, nos):
                        tb += "<tr>" + "".join(
                            _cell(note, ln, k, c, al(k), "td", editable)
                            for k, c in enumerate(r)) + "</tr>"
                    body = ("<table><thead><tr>" + th + "</tr></thead><tbody>"
                            + tb + "</tbody></table>")
                else:
                    body = "<dl>"
                    for (name, desc), ln in zip(rows, nos):
                        body += _cell(note, ln, 0, name, "left", "dt", editable)
                        body += _cell(note, ln, 1, desc, "left", "dd", editable)
                    body += "</dl>"

                band_cards.append(
                    "<article class='card'><header><span class='src'>{}</span>"
                    "<h3>{}</h3></header>{}<footer>{} {}</footer></article>".format(
                        html.escape(note), inline(title), body, len(rows),
                        "rows" if kind == "table" else "entries"))
        if band_cards:
            cards.append(
                "<section class='band {}'><h2><span>{}</span><small>{} tables</small></h2>"
                "<div class='tiles'>{}</div></section>".format(
                    cls, html.escape(band), len(band_cards), "".join(band_cards)))

    total = stats["tables"] + stats["lists"]
    legend = "".join("<i style='--bc:var(--{})'>{}</i>".format(c, html.escape(n.split(" ")[0]))
                     for n, c, _ in BANDS)
    mode = ("<span class='mode live' title='Edits save straight into the Obsidian vault'>&#9679; live</span>"
            if editable else "<span class='mode'>read-only</span>")

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
        '  <span class="meta">' + str(total) + " tables &middot; " + str(stats["rows"])
        + " entries</span>\n  " + mode + "\n"
        '  <div id="legend">' + legend + "</div>\n"
        '  <span class="sp"></span>\n'
        '  <span id="toast"></span>\n'
        '  <input id="find" type="search" placeholder="highlight&hellip;  ( / )" '
        'aria-label="Highlight tables">\n'
        '  <button id="zout" title="Zoom out">&minus;</button>\n'
        '  <span id="zl">100%</span>\n'
        '  <button id="zin" title="Zoom in">+</button>\n'
        '  <button id="zfit" title="Fit everything (0)">Fit</button>\n'
        '  <button id="z100" title="Actual size">1:1</button>\n'
        "</div>\n"
        '<div id="vp"><div id="wall">' + "".join(cards) + "</div></div>\n"
        "<script>var EDITABLE=" + ("true" if editable else "false") + ";"
        + SCRIPT + "</script>\n"
    )
    return page, stats, total


STYLE = """
:root{
 --ground:#EFF1F0;--surface:#FFFFFF;--sunk:#E6EAE8;--ink:#14181C;--muted:#5A636B;
 --faint:#828B92;--rule:#D0D5D3;--soft:#E4E8E6;--accent:#2E5C7A;
 --ok:#2F6E55;--bad:#AC3327;
 --eng:#2E5C7A;--cbt:#AC3327;--ger:#B06D10;--ter:#2F6E55;--crw:#6B4C8A;--cmp:#7B7222;--phy:#4A5D68;
 --disp:"Barlow Condensed","Arial Narrow",Helvetica,sans-serif;
 --body:"Source Serif 4",Georgia,serif;
 --mono:"IBM Plex Mono",ui-monospace,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --ground:#0F1216;--surface:#171B21;--sunk:#1E242B;--ink:#E6E9E7;--muted:#9AA4AC;
 --faint:#79838B;--rule:#2A313A;--soft:#222932;--accent:#79ACCB;
 --ok:#6BB394;--bad:#E07364;
 --eng:#79ACCB;--cbt:#E07364;--ger:#DCA245;--ter:#6BB394;--crw:#B394D4;--cmp:#BDB055;--phy:#8FA4B0;}}
:root[data-theme="dark"]{
 --ground:#0F1216;--surface:#171B21;--sunk:#1E242B;--ink:#E6E9E7;--muted:#9AA4AC;
 --faint:#79838B;--rule:#2A313A;--soft:#222932;--accent:#79ACCB;
 --ok:#6BB394;--bad:#E07364;
 --eng:#79ACCB;--cbt:#E07364;--ger:#DCA245;--ter:#6BB394;--crw:#B394D4;--cmp:#BDB055;--phy:#8FA4B0;}
*{box-sizing:border-box}
html,body{margin:0;height:100%;overflow:hidden;background:var(--ground);color:var(--ink);
 font-family:var(--body);-webkit-font-smoothing:antialiased}

#bar{position:fixed;inset:0 0 auto 0;height:46px;z-index:20;display:flex;align-items:center;
 gap:.55rem;padding:0 .8rem;background:var(--surface);border-bottom:1px solid var(--rule)}
#bar .ttl{font-family:var(--disp);font-weight:700;font-size:1.12rem;white-space:nowrap}
#bar .meta,.mode{font-family:var(--mono);font-size:.6rem;letter-spacing:.11em;
 text-transform:uppercase;color:var(--faint);white-space:nowrap}
.mode.live{color:var(--ok)}
#bar .sp{flex:1;min-width:.4rem}
#bar .meta,#legend{overflow:hidden;flex:0 1 auto}
@media (max-width:1100px){#legend{display:none}}
@media (max-width:820px){#bar .meta{display:none}}
button,#find{font-family:var(--mono);font-size:.66rem;letter-spacing:.06em;text-transform:uppercase;
 background:var(--sunk);color:var(--ink);border:1px solid var(--rule);border-radius:3px;
 padding:.32rem .55rem;cursor:pointer}
button:hover{border-color:var(--accent);color:var(--accent)}
button:focus-visible,#find:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
#find{text-transform:none;letter-spacing:0;width:11rem;cursor:text}
#zl{font-family:var(--mono);font-size:.62rem;color:var(--faint);min-width:3.1rem;text-align:right}
#toast{font-family:var(--mono);font-size:.6rem;letter-spacing:.08em;text-transform:uppercase;
 color:var(--ok);white-space:nowrap;opacity:0;transition:opacity .18s}
#toast.show{opacity:1}
#toast.err{color:var(--bad)}
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

/* ---- editing ---- */
.ed:hover{background:color-mix(in srgb,var(--accent) 9%,transparent);cursor:text}
.ed:focus{outline:2px solid var(--accent);outline-offset:-1px;background:var(--surface);
 white-space:pre-wrap;position:relative;z-index:5}
.ed.saving{background:color-mix(in srgb,var(--accent) 16%,transparent)}
.ed.saved{background:color-mix(in srgb,var(--ok) 20%,transparent)}
.ed.failed{background:color-mix(in srgb,var(--bad) 22%,transparent);outline:2px solid var(--bad)}

.card.hit{outline:2px solid var(--accent);outline-offset:2px}
.card.dim{opacity:.28}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

SCRIPT = """
(function(){
 var vp=document.getElementById('vp'), wall=document.getElementById('wall'),
     zl=document.getElementById('zl'), find=document.getElementById('find'),
     toast=document.getElementById('toast');
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
   else{zoomAt(e.clientX,e.clientY,s*(e.deltaY<0?1.12:1/1.12));}},{passive:false});
 var down=false,lx=0,ly=0;
 vp.addEventListener('pointerdown',function(e){
   if(e.target.closest('input,[contenteditable]'))return;
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
   if(e.target.isContentEditable||document.activeElement===find)return;
   if(e.key==='/'){e.preventDefault();find.focus();}
   if(e.key==='0'){fit();}});

 // Editing. Listeners go DIRECTLY on each cell rather than delegating from
 // #wall: focus events do not bubble reliably in every context, and a save
 // that silently never fires is the worst possible failure for this tool.
 if(EDITABLE){
  function say(m,bad){toast.textContent=m;toast.classList.toggle('err',!!bad);
    toast.classList.add('show');clearTimeout(say._t);
    say._t=setTimeout(function(){toast.classList.remove('show');},2600);}
  function save(c,prev,next){
    c.classList.add('saving');
    return fetch('/cell',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({note:c.dataset.note,line:+c.dataset.line,
                           col:+c.dataset.col,old:prev,text:next})})
    .then(function(r){return r.json().then(function(j){return {ok:r.ok,j:j};});})
    .then(function(res){
      c.classList.remove('saving');
      if(!res.ok){throw new Error(res.j.error||'save failed');}
      c.dataset.raw=next; c.innerHTML=res.j.html;
      c.classList.add('saved'); setTimeout(function(){c.classList.remove('saved');},1100);
      say('saved → '+c.dataset.note+':'+c.dataset.line);})
    .catch(function(err){
      c.classList.remove('saving'); c.classList.add('failed');
      c.innerHTML=c.dataset.html||c.dataset.raw;
      setTimeout(function(){c.classList.remove('failed');},2600);
      say(String(err.message||err),true);});}
  [].forEach.call(document.querySelectorAll('.ed'),function(c){
    c.dataset.html=c.innerHTML;
    c.addEventListener('focus',function(){c.textContent=c.dataset.raw;});
    c.addEventListener('blur',function(){
      var next=c.textContent.trim(), prev=c.dataset.raw;
      if(next===prev){c.innerHTML=c.dataset.html;return;}
      save(c,prev,next);});
    c.addEventListener('keydown',function(e){
      if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();c.blur();}
      if(e.key==='Escape'){e.preventDefault();c.textContent=c.dataset.raw;
        c.innerHTML=c.dataset.html;c.blur();}});});
  window.wallSave=save;   // exposed so the round-trip can be tested headlessly
 }

 if(document.fonts&&document.fonts.ready){document.fonts.ready.then(function(){
   requestAnimationFrame(fit);});}else{requestAnimationFrame(fit);}
 window.addEventListener('load',function(){requestAnimationFrame(fit);});
})();
"""


if __name__ == "__main__":
    root = MIRROR if "--repo" in sys.argv else VAULT
    out = next((a for a in sys.argv[1:] if not a.startswith("--")),
               os.path.join(HERE, "rules-wall.html"))
    page, stats, total = build(root, editable="--editable" in sys.argv)
    io.open(out, "w", encoding="utf-8", newline="").write(page)
    print("wrote {}  ({:,} bytes)".format(out, len(page)))
    print("  {} tables + {} bullet catalogues = {} cards, {} entries".format(
        stats["tables"], stats["lists"], total, stats["rows"]))
