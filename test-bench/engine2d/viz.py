"""Render one recorded game to a self-contained HTML replay.

    py -3.13 viz.py            # turret crew vs plain -> replay.html
    py -3.13 viz.py 42         # pick a seed

Open replay.html in a browser: an SVG tactical map you step round-by-round —
unit positions, casualties, the turret, and who holds each objective each End Phase.
This is the visualization layer that turns the sim from a number-printer into a
watchable game (and the seed of the product demo — see the note to Ross).
"""
import json
import random
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

from board import take_a_hold
from crews import redline, redline_turret
from engine import Game


TEMPLATE = r"""<!doctype html>
<meta charset="utf-8">
<title>Settlements — Battle Replay</title>
<style>
  :root{ --bg:#191c15; --panel:#23271d; --ink:#e9e5d6; --a:#8fb43a; --b:#e07a3a;
         --obj:#e7c14a; --line:#4a4f3c; }
  body{ margin:0; background:var(--bg); color:var(--ink);
        font-family:"Segoe UI",Arial,sans-serif; display:flex; flex-direction:column;
        align-items:center; padding:16px; }
  h1{ font-family:"Arial Narrow",Impact,sans-serif; letter-spacing:2px; text-transform:uppercase;
      font-size:20px; margin:0 0 2px; }
  .sub{ font-size:12px; color:#9a9a86; margin-bottom:10px; }
  .wrap{ display:flex; gap:16px; align-items:flex-start; flex-wrap:wrap; justify-content:center; }
  svg{ background:var(--panel); border:2px solid var(--line); }
  .side{ width:220px; }
  .card{ background:var(--panel); border:1px solid var(--line); padding:10px 12px; margin-bottom:10px; }
  .card h2{ font-size:12px; letter-spacing:1px; text-transform:uppercase; margin:0 0 6px; color:#c9c4b0; }
  .vp{ display:flex; justify-content:space-between; font-size:26px; font-weight:800;
       font-family:"Arial Narrow",sans-serif; }
  .vp .a{ color:var(--a); } .vp .b{ color:var(--b); }
  .leg{ font-size:12px; line-height:1.7; }
  .dot{ display:inline-block; width:11px; height:11px; border-radius:50%; margin-right:6px; vertical-align:-1px; }
  .controls{ margin-top:12px; display:flex; gap:8px; align-items:center; }
  button{ background:#3a4030; color:var(--ink); border:1px solid var(--line); padding:6px 12px;
          cursor:pointer; letter-spacing:1px; font-size:12px; }
  button:hover{ background:#4a5140; }
  input[type=range]{ width:300px; }
  #rlabel{ font-family:"Arial Narrow",sans-serif; font-size:15px; min-width:120px; }
  .banner{ font-family:"Arial Narrow",sans-serif; font-size:15px; letter-spacing:1px; }
</style>

<h1>Settlements — Battle Replay</h1>
<div class="sub">Take a Hold · roof crew (A) vs ground crew (B) · white ring = on a rooftop · step the End Phases</div>

<div class="wrap">
  <svg id="map" width="580" height="580" viewBox="0 0 580 580"></svg>
  <div class="side">
    <div class="card"><h2>Score</h2>
      <div class="vp"><span class="a" id="vpa">0</span><span style="color:#666">VP</span><span class="b" id="vpb">0</span></div>
      <div class="banner" id="banner"></div>
    </div>
    <div class="card"><h2>Legend</h2>
      <div class="leg">
        <span class="dot" style="background:var(--a)"></span>Crew A (roof)<br>
        <span class="dot" style="background:var(--b)"></span>Crew B (ground)<br>
        <span class="dot" style="background:#777"></span>down / out<br>
        <span style="display:inline-block;width:11px;height:11px;border:2px solid #fff;border-radius:50%;margin-right:6px;vertical-align:-1px"></span>on a rooftop (elevated)<br>
        <span style="display:inline-block;width:11px;height:11px;background:var(--a);margin-right:6px;vertical-align:-1px"></span>turret<br>
        <span style="display:inline-block;width:11px;height:11px;border:2px solid var(--obj);border-radius:50%;margin-right:6px;vertical-align:-1px"></span>objective (glows for the holder)
      </div>
    </div>
  </div>
</div>

<div class="controls">
  <button id="prev">◀ Prev</button>
  <button id="play">▶ Play</button>
  <button id="next">Next ▶</button>
  <input type="range" id="slider" min="0" value="0">
  <span id="rlabel"></span>
</div>

<script>
const D = /*DATA*/;
const S = 15, M = 20, SZ = D.size;
const NS = "http://www.w3.org/2000/svg";
const svg = document.getElementById('map');
const px = x => M + x * S;
const py = y => M + (SZ - y) * S;   // board y=0 at bottom
function el(tag, attrs){ const e=document.createElementNS(NS,tag); for(const k in attrs) e.setAttribute(k,attrs[k]); return e; }

// --- static layer: terrain, deploy bands, objective rings ---
const A_COL='#8fb43a', B_COL='#e07a3a', OBJ='#e7c14a';
// deploy bands
D.frames && [ [0,6,'#8fb43a'], [30,36,'#e07a3a'] ].forEach(([y0,y1,c])=>{
  svg.appendChild(el('rect',{x:px(0),y:py(y1),width:SZ*S,height:(y1-y0)*S,fill:c,opacity:0.08}));
});
// terrain
D.terrain.forEach(t=>{
  const fill = t.blocks ? '#3c4230' : (t.cover>=2 ? '#565c44' : '#727659');
  svg.appendChild(el('rect',{x:px(t.x1),y:py(t.y2),width:(t.x2-t.x1)*S,height:(t.y2-t.y1)*S,
    fill:fill, stroke:'#20241a', 'stroke-width':1}));
});
// centreline
svg.appendChild(el('line',{x1:px(0),y1:py(18),x2:px(SZ),y2:py(18),stroke:'#5a4030','stroke-dasharray':'5 5','stroke-width':1}));
// dynamic layer group
const objRings = D.objectives.map(o=>{
  const r = el('circle',{cx:px(o[0]),cy:py(o[1]),r:3*S,fill:'none',stroke:OBJ,'stroke-width':2,opacity:0.5});
  svg.appendChild(r); return r;
});
const dyn = el('g',{}); svg.appendChild(dyn);

function holder(o, f){
  const a = f.units.some(u=>u.side===0 && u.st==='ok' && Math.hypot(u.x-o[0],u.y-o[1])<=3);
  const b = f.units.some(u=>u.side===1 && u.st==='ok' && Math.hypot(u.x-o[0],u.y-o[1])<=3);
  return a&&!b ? 0 : b&&!a ? 1 : -1;
}
function draw(i){
  const f = D.frames[i];
  while(dyn.firstChild) dyn.removeChild(dyn.firstChild);
  // objective glow by holder
  D.objectives.forEach((o,j)=>{
    const h = holder(o,f);
    objRings[j].setAttribute('stroke', h===0?A_COL:h===1?B_COL:OBJ);
    objRings[j].setAttribute('opacity', h<0?0.4:0.95);
    objRings[j].setAttribute('stroke-width', h<0?2:4);
  });
  // turrets
  f.turrets.forEach(t=>{
    const c = t.side===0?A_COL:B_COL;
    const g = el('rect',{x:px(t.x)-7,y:py(t.y)-7,width:14,height:14,
      fill:t.state==='online'?c:'#555', stroke:'#111','stroke-width':1.5});
    dyn.appendChild(g);
    dyn.appendChild(el('text',{x:px(t.x),y:py(t.y)+4,'text-anchor':'middle','font-size':9,fill:'#111','font-weight':'bold'},'T'));
  });
  // units
  f.units.forEach(u=>{
    const c = u.side===0?A_COL:B_COL;
    if(u.st==='out'){
      ['-1 1','1 1'].forEach(()=>{});
      const g=el('g',{opacity:0.5});
      g.appendChild(el('line',{x1:px(u.x)-5,y1:py(u.y)-5,x2:px(u.x)+5,y2:py(u.y)+5,stroke:'#888','stroke-width':2}));
      g.appendChild(el('line',{x1:px(u.x)-5,y1:py(u.y)+5,x2:px(u.x)+5,y2:py(u.y)-5,stroke:'#888','stroke-width':2}));
      dyn.appendChild(g);
    } else {
      if(u.z>0){ dyn.appendChild(el('circle',{cx:px(u.x),cy:py(u.y),r:9.5,fill:'none',stroke:'#fff','stroke-width':1.5,opacity:0.9})); }
      dyn.appendChild(el('circle',{cx:px(u.x),cy:py(u.y),r:6,
        fill:u.st==='down'?'#777':c, stroke:'#111','stroke-width':1.5}));
    }
  });
  document.getElementById('vpa').textContent=f.vp[0];
  document.getElementById('vpb').textContent=f.vp[1];
  document.getElementById('rlabel').textContent = i===0?'Deployment':('End of Round '+f.round);
  if(i===D.frames.length-1){
    const w=D.result;
    document.getElementById('banner').textContent = w==='draw'?'Draw':('Crew '+w+' wins '+D.vp[0]+'–'+D.vp[1]);
  } else document.getElementById('banner').textContent='';
}
const slider=document.getElementById('slider');
slider.max=D.frames.length-1;
slider.oninput=()=>draw(+slider.value);
document.getElementById('prev').onclick=()=>{slider.value=Math.max(0,+slider.value-1);draw(+slider.value);};
document.getElementById('next').onclick=()=>{slider.value=Math.min(D.frames.length-1,+slider.value+1);draw(+slider.value);};
let timer=null;
document.getElementById('play').onclick=()=>{
  if(timer){clearInterval(timer);timer=null;return;}
  if(+slider.value>=D.frames.length-1) slider.value=0;
  timer=setInterval(()=>{ if(+slider.value>=D.frames.length-1){clearInterval(timer);timer=null;return;}
    slider.value=+slider.value+1; draw(+slider.value); }, 900);
};
draw(0);
</script>
"""


def build(seed, out='replay.html'):
    random.seed(seed)
    board = take_a_hold()
    g = Game(redline(0, 'roof'), redline(1, 'balanced'), board, record=True)
    res = g.play()
    terrain = [dict(x1=p.x1, y1=p.y1, x2=p.x2, y2=p.y2, cover=p.cover, blocks=p.blocks)
               for p in board['terrain']]
    data = dict(size=board['size'], terrain=terrain, objectives=board['objectives'],
                deploy={str(k): v for k, v in board['deploy'].items()},
                frames=g.frames, result=res['winner'], vp=res['vp'])
    html = TEMPLATE.replace('/*DATA*/', json.dumps(data))
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"wrote {out}  ({len(g.frames)} frames · result {res['winner']} {res['vp']})")


if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 20260717
    build(seed)
