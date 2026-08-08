# -*- coding: utf-8 -*-
"""Build a terrain PALETTE from subscribed Workshop mods, for hand-building boards.

The mods hold ~1,300 assets scattered across their own tables at coordinates like
(-60, 0.8, 14) — findable only by flying the camera around someone else's map. This
curates the ones that are useful as Settlements terrain, groups them by the ROLE
they play in the rules, and drops them next to your board as labelled bags you can
drag from.

TWO CURATION RULES THAT MATTER:

1. PREFER "(improved collider)" VARIANTS. Several pieces ship twice — `city ruin 1`
   and `city ruin 1 (improved collider)`. The collider is what decides whether a
   model blocks movement and line of sight correctly, and LOS is load-bearing in
   this game, so the improved one always wins.

2. GROUP BY RULES ROLE, NOT BY LOOKS. A building and a ruin are the same category
   to a player picking scenery, but they are different rows in the terrain table:
   one blocks LOS, one gives Heavy cover you can shoot through. The bag names say
   what each group DOES.

    py -3.13 make_palette.py            # list what it would spawn
    py -3.13 make_palette.py --spawn    # push the bags to the live table
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WORKSHOP = os.path.join(os.path.expanduser('~'), 'Documents', 'My Games',
                        'Tabletop Simulator', 'Mods', 'Workshop')

MODS = {
    '1940563574': 'Ultimate Modern Map Toolkit',
    '1932528870': 'Modern Items',
    '2416214524': 'Modern City Buildings',
    '3346010681': 'Suburb Map & Assets',
    '1210066713': 'Modern Army Infantry',
}

# name -> (bag, suggested cover, suggested height", suggested tags)
# Cover: 0 open · 1 light · 2 heavy.  These are SUGGESTIONS printed on the piece;
# you set the real profile with !terrain when you place it.
CURATED = {
    # --- LOS-blocking buildings: the backbone of a legal board -------------
    'Office Building 2':   ('Buildings', 2, 6, 'Openable, Climbable, Searchable'),
    'Office Building 3':   ('Buildings', 2, 6, 'Openable, Climbable, Searchable'),
    'Office Tower 1':      ('Buildings', 2, 8, 'Openable, Climbable, Searchable'),
    'Skyscraper':          ('Buildings', 2, 10, 'Climbable'),
    'Skyscraper 2':        ('Buildings', 2, 10, 'Climbable'),
    'Hospital':            ('Buildings', 2, 6, 'Openable, Lockable, Searchable'),
    'Bunker':              ('Buildings', 2, 4, 'Openable, Lockable, Breachable'),
    'Barn, Burnt':         ('Buildings', 2, 5, 'Openable, Searchable, Unstable'),
    'House':               ('Buildings', 2, 5, 'Openable, Climbable, Searchable'),
    'Church':              ('Buildings', 2, 6, 'Openable, Searchable'),
    'Garage':              ('Buildings', 2, 4, 'Openable, Breachable, Searchable'),
    'Windmill':            ('Buildings', 2, 8, 'Climbable'),
    'Gazebo':              ('Buildings', 1, 3, 'Climbable'),

    # --- ruins: heavy cover you can fight THROUGH, and the 2.5D layer ------
    'city ruin 1':         ('Ruins', 2, 6, 'Climbable, Searchable, Unstable'),
    'city ruin 2':         ('Ruins', 2, 6, 'Climbable, Searchable, Unstable'),
    'ruin large':          ('Ruins', 2, 7, 'Climbable, Searchable, Unstable'),
    'Ruin Small':          ('Ruins', 2, 3, 'Climbable, Searchable'),
    'Ruins Tall':          ('Ruins', 2, 7, 'Climbable, Unstable'),
    'gothic ruin':         ('Ruins', 2, 6, 'Climbable, Unstable'),
    'Rubble Wall':         ('Ruins', 2, 2, 'Climbable'),
    'wh_dead_civ_1':       ('Ruins', 1, 1, ''),

    # --- scatter: what fills the gaps until no lane crosses the board ------
    'Barricades':          ('Scatter & cover', 1, 1, 'Movable, Barricadable'),
    'Sandbags':            ('Scatter & cover', 2, 1, 'Barricadable'),
    'Tank Trap':           ('Scatter & cover', 1, 2, ''),
    'Dragonteeth':         ('Scatter & cover', 1, 2, ''),
    'Crate 2':             ('Scatter & cover', 1, 1, 'Movable, Searchable'),
    'Military Crate':      ('Scatter & cover', 1, 1, 'Movable, Searchable, Lockable'),
    'Wood Pile':           ('Scatter & cover', 1, 1, 'Movable'),
    'Wood Stack':          ('Scatter & cover', 1, 2, 'Movable'),
    'Burnt Junk':          ('Scatter & cover', 1, 1, 'Movable, Searchable'),
    'Craters':             ('Scatter & cover', 0, 0, ''),
    'ModularRock_01':      ('Scatter & cover', 2, 2, 'Climbable'),
    'Shrubs 1':            ('Scatter & cover', 1, 1, ''),
    'Shrubs 2':            ('Scatter & cover', 1, 1, ''),
    'Woods 1':             ('Scatter & cover', 1, 4, ''),
    'Woods 5':             ('Scatter & cover', 1, 4, ''),
    'Woods 6':             ('Scatter & cover', 1, 4, ''),
    'TreeTrunk':           ('Scatter & cover', 1, 1, 'Movable'),
    'Fence':               ('Scatter & cover', 1, 1, 'Breachable, Climbable'),
    'Newsstands':          ('Scatter & cover', 1, 2, 'Searchable'),
    'Kiosk':               ('Scatter & cover', 1, 2, 'Openable, Searchable'),
    'Rusty Old Locker':    ('Scatter & cover', 1, 2, 'Openable, Searchable'),
    'Discard Bin':         ('Scatter & cover', 1, 1, 'Searchable'),

    # --- vehicles: hard cover, and thematically right for 2051 ------------
    'Groundcar':           ('Vehicles', 2, 2, 'Openable, Searchable, Explosive'),
    'Motorcycle':          ('Vehicles', 1, 1, 'Movable'),
    'Quadbike':            ('Vehicles', 1, 1, 'Movable'),
    'Trailer':             ('Vehicles', 2, 3, 'Openable, Searchable'),
    'Opel Blitz':          ('Vehicles', 2, 3, 'Openable, Searchable, Explosive'),
    'Killer Cart':         ('Vehicles', 1, 2, 'Movable'),

    # --- VERTICALITY: the engine is 2.5D, so every roof needs a way up ----
    'Wood scaffold x1':    ('Verticality', 1, 4, 'Climbable'),
    'Wood stairs x1':      ('Verticality', 0, 3, 'Climbable'),
    'Stairs stone 1x':     ('Verticality', 0, 2, 'Climbable'),
    'Stairs stone 2x':     ('Verticality', 0, 4, 'Climbable'),
    'Steps, Wooden':       ('Verticality', 0, 2, 'Climbable'),
    'Ramp or bridge':      ('Verticality', 0, 2, 'Climbable'),
    'Bridge':              ('Verticality', 1, 4, 'Climbable'),
    'Rope Bridge':         ('Verticality', 0, 4, 'Climbable, Unstable'),
    'stone bridge floor':  ('Verticality', 0, 3, 'Climbable'),
    'stone bridge stairs': ('Verticality', 0, 3, 'Climbable'),
    'Platform, Dungeon':   ('Verticality', 1, 3, 'Climbable'),
    'metal thin floor board': ('Verticality', 0, 3, 'Climbable'),
    'Stage':               ('Verticality', 1, 2, 'Climbable'),
    'Wood stair spiral 1x1': ('Verticality', 0, 4, 'Climbable'),

    # --- Infrastructure: things a terminal can actually operate ------------
    'Power Generator':     ('Infrastructure', 2, 2, 'Powered, Hackable, Explosive'),
    'Power Unit':          ('Infrastructure', 1, 2, 'Powered, Hackable'),
    'Power box':           ('Infrastructure', 0, 1, 'Powered, Hackable'),
    'Switch 2':            ('Infrastructure', 0, 1, 'Powered, Hackable'),
    'door':                ('Infrastructure', 2, 3, 'Openable, Lockable, Breachable'),
    'Vent':                ('Infrastructure', 0, 1, 'Openable'),
    'Vending machine':     ('Infrastructure', 2, 2, 'Powered, Searchable'),
    'Nuka Cola Machine':   ('Infrastructure', 2, 2, 'Powered, Searchable'),
    'Security Camera':     ('Infrastructure', 0, 1, 'Powered, Hackable'),
    'Pumpjack':            ('Infrastructure', 1, 3, 'Powered, Explosive'),

    # --- objective and loot props ----------------------------------------
    'Laptop':              ('Objectives & loot', 0, 0, 'Hackable, Searchable'),
    'Tablet':              ('Objectives & loot', 0, 0, 'Hackable'),
    'Server Blade':        ('Objectives & loot', 0, 0, 'Hackable, Searchable'),
    'Ammo Box':            ('Objectives & loot', 0, 0, 'Searchable'),
    'First Aid Kit':       ('Objectives & loot', 0, 0, 'Searchable'),
    'Money Briefcase':     ('Objectives & loot', 0, 0, 'Lockable, Searchable'),
    'Jerry Can':           ('Objectives & loot', 0, 0, 'Explosive, Searchable'),
    'Toolbox':             ('Objectives & loot', 0, 0, 'Searchable'),
    'Gun Case':            ('Objectives & loot', 0, 0, 'Lockable, Searchable'),
    'Duffle':              ('Objectives & loot', 0, 0, 'Searchable'),
    'Military Helmet':     ('Objectives & loot', 0, 0, 'Searchable'),
    'Documents':           ('Objectives & loot', 0, 0, 'Searchable'),
    'Flash drive':         ('Objectives & loot', 0, 0, 'Hackable'),
}

BAG_ORDER = ['Buildings', 'Ruins', 'Scatter & cover', 'Vehicles', 'Verticality',
             'Infrastructure', 'Objectives & loot']

BAG_BLURB = {
    'Buildings': 'LOS-BLOCKING. The backbone of a legal board — you need at least '
                 'two, and every floor needs a no-test way up.',
    'Ruins': 'HEAVY COVER you can fight through, and the 2.5D layer. Prefer these '
             'over solid buildings if you want firefights instead of a stalemate.',
    'Scatter & cover': 'Fills the gaps. Keep adding until NO CLEAR FIRING LANE '
                       'crosses the board — that is the real test, not the count.',
    'Vehicles': 'Hard cover at the right scale for 2051. Several are Explosive.',
    'Verticality': 'The engine is 2.5D: a rooftop shooter sees over what blocks a '
                   'ground shooter. EVERY elevated area needs one of these.',
    'Infrastructure': 'Things a terminal can operate (§12.5). Reshapes the board; '
                      'it is not there to hurt people — that is Deployables.',
    'Objectives & loot': 'Objective markers, Searchable caches, hackable devices.',
}


def load_assets():
    found = {}
    for mid, label in MODS.items():
        p = os.path.join(WORKSHOP, f'{mid}.json')
        if not os.path.isfile(p):
            continue
        try:
            with open(p, encoding='utf-8', errors='replace') as fh:
                mod = json.load(fh)
        except Exception:
            continue
        stack = list(mod.get('ObjectStates') or [])
        while stack:
            o = stack.pop()
            if not isinstance(o, dict):
                continue
            stack.extend(o.get('ContainedObjects') or [])
            cm = o.get('CustomMesh') or {}
            if not cm.get('MeshURL'):
                continue
            nick = (o.get('Nickname') or '').strip()
            base = nick.replace(' (improved collider)', '').strip()
            if base not in CURATED:
                continue
            t = o.get('Transform') or {}
            rec = dict(nick=nick, base=base, mod=label,
                       mesh=cm.get('MeshURL', ''), diffuse=cm.get('DiffuseURL', '') or '',
                       collider=cm.get('ColliderURL', '') or '',
                       convex=bool(cm.get('Convex', False)),
                       mat=cm.get('MaterialIndex', 1), typ=cm.get('TypeIndex', 0),
                       scale=float(t.get('scaleX', 1) or 1),
                       improved='improved collider' in nick.lower())
            prev = found.get(base)
            # improved collider always wins; otherwise first one found
            if prev is None or (rec['improved'] and not prev['improved']):
                found[base] = rec
    return found




def rewrite_url(u):
    """Repair retired Steam CDN hosts.

    Verified from this machine: http://cloud-N.steamusercontent.com/ugc/... returns
    403 on HEAD, ranged GET and plain GET, while the identical path on
    https://steamusercontent-a.akamaihd.net/ugc/... returns 200. Steam moved its
    UGC hosting and left the old hostnames dead, which is why a lot of otherwise
    fine Workshop mods now nag you with Custom Model popups."""
    import re
    if not u:
        return u
    return re.sub(r'https?://cloud-\d+\.steamusercontent\.com',
                  'https://steamusercontent-a.akamaihd.net', u)


def verify(found):
    """HEAD-check every asset URL and DROP anything unreachable.

    This is the whole point of the palette. TTS pops its "Custom Model" config
    dialog every single time it cannot fetch a mesh, so one dead link nags you
    forever. Several big Workshop mods host on infrastructure that is simply gone
    - classic Google Sites hosting is shut down, Google Drive blocks hotlinking,
    personal domains lapse. Better to ship 40 pieces that load than 90 that
    mostly do not."""
    import concurrent.futures
    import urllib.request
    from urllib.parse import urlparse

    def reachable(url):
        if not url:
            return False
        for headers, method in (({}, 'HEAD'), ({'Range': 'bytes=0-0'}, 'GET')):
            try:
                req = urllib.request.Request(url, method=method)
                req.add_header('User-Agent', 'Mozilla/5.0')
                for k, v in headers.items():
                    req.add_header(k, v)
                with urllib.request.urlopen(req, timeout=8) as r:
                    if 200 <= r.status < 400:
                        return True
            except Exception:
                continue
        return False

    # repair the retired-host URLs BEFORE testing, so we do not throw away
    # assets that are perfectly alive under their new hostname
    rewritten = 0
    for rec in found.values():
        for k in ('mesh', 'diffuse', 'collider'):
            nu = rewrite_url(rec[k])
            if nu != rec[k]:
                rec[k] = nu
                rewritten += 1
    if rewritten:
        print(f'rewrote {rewritten} retired Steam CDN URL(s) -> Akamai')
    print(f'verifying {len(found)} asset(s) are actually reachable...')
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
        ok = dict(zip(found, ex.map(reachable, (r['mesh'] for r in found.values()))))
    good = {b: r for b, r in found.items() if ok.get(b)}
    dead = [(b, r['mesh']) for b, r in found.items() if not ok.get(b)]
    if dead:
        print(f'  DROPPED {len(dead)} unreachable - these are exactly what cause '
              f'the endless "Custom Model" popups:')
        by_host = {}
        for b, url in dead:
            by_host.setdefault(urlparse(url).netloc or '(no url)', []).append(b)
        for host, names in sorted(by_host.items(), key=lambda kv: -len(kv[1])):
            print(f'    {host:<34} {len(names):>3}  {", ".join(sorted(names)[:5])}'
                  + (' ...' if len(names) > 5 else ''))
    print(f'  {len(good)} reachable\n')
    return good


def build_bags(found):
    bags = {}
    for base, rec in found.items():
        bag, cover, height, tags = CURATED[base]
        bags.setdefault(bag, []).append((base, rec, cover, height, tags))
    for b in bags:
        bags[b].sort(key=lambda r: r[0])
    return bags


def model_json(rec, nickname, desc, pos, scale):
    return {
        'Name': 'Custom_Model', 'Nickname': nickname, 'Description': desc,
        'Transform': {'posX': pos[0], 'posY': pos[1], 'posZ': pos[2],
                      'rotX': 0, 'rotY': 0, 'rotZ': 0,
                      'scaleX': scale, 'scaleY': scale, 'scaleZ': scale},
        'ColorDiffuse': {'r': 1, 'g': 1, 'b': 1}, 'Locked': False,
        'Grid': True, 'Snap': False, 'Autoraise': True, 'Sticky': True,
        'CustomMesh': {
            'MeshURL': rec['mesh'], 'DiffuseURL': rec['diffuse'], 'NormalURL': '',
            'ColliderURL': rec['collider'],
            'Convex': rec['convex'] or not rec['collider'],
            'MaterialIndex': rec['mat'], 'TypeIndex': rec['typ'],
            'CustomShader': {'SpecularColor': {'r': 0.9, 'g': 0.9, 'b': 0.9},
                             'SpecularIntensity': 0.1, 'SpecularSharpness': 4.0,
                             'FresnelStrength': 0.1},
            'CastShadows': True,
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--spawn', action='store_true', help='push the bags to live TTS')
    ap.add_argument('--no-verify', action='store_true',
                    help='skip the reachability check (not recommended)')
    args = ap.parse_args()

    found = load_assets()
    if not args.no_verify:
        found = verify(found)
    bags = build_bags(found)
    missing = [k for k in CURATED if k not in found]

    total = sum(len(v) for v in bags.values())
    print(f'curated {total} of {len(CURATED)} wanted pieces\n')
    for b in BAG_ORDER:
        if b not in bags:
            continue
        print(f'[{b}]  {len(bags[b])} pieces')
        for base, rec, cover, height, tags in bags[b]:
            imp = '  (improved collider)' if rec['improved'] else ''
            print(f'   {base[:30]:<30} cover {cover} · {height:g}" tall{imp}')
        print()
    if missing:
        print(f'not found in the subscribed mods ({len(missing)}): '
              f'{", ".join(sorted(missing)[:18])}'
              + (' ...' if len(missing) > 18 else ''))

    if not args.spawn:
        print('\n(run with --spawn to push these bags onto the live table)')
        return 0

    sys.path.insert(0, HERE)
    import tts_api
    if not tts_api.is_up():
        print('\nTTS is not listening — load a table first.', file=sys.stderr)
        return 1

    lines = []
    for i, b in enumerate([x for x in BAG_ORDER if x in bags]):
        rows = bags[b]
        contained = []
        for base, rec, cover, height, tags in rows:
            cw = {0: 'Open (0)', 1: 'Light (-1)', 2: 'Heavy (-2)'}[cover]
            desc = (f'{base}\nSuggested: {cw} · {height:g}" tall'
                    + (f'\nTags: {tags}' if tags else '')
                    + f'\n\nPlace it, then: !terrain {cover} {height:g}'
                    + (f' {tags.replace(", ", ",")}' if tags else ''))
            contained.append(model_json(rec, base, desc, (0, 3, 0), rec['scale']))
        # a column down the left of the board, clear of the 36" playing area
        bag = {
            'Name': 'Bag', 'Nickname': f'{b} ({len(rows)})',
            'Description': BAG_BLURB.get(b, ''),
            'Transform': {'posX': -24.0, 'posY': 3.6, 'posZ': -18.0 + i * 5.5,
                          'rotX': 0, 'rotY': 0, 'rotZ': 0,
                          'scaleX': 1.4, 'scaleY': 1.4, 'scaleZ': 1.4},
            'ColorDiffuse': {'r': 0.30, 'g': 0.34, 'b': 0.30},
            'Locked': False, 'Grid': True, 'Snap': False,
            'ContainedObjects': contained,
        }
        lines.append(f'spawnObjectJSON({{json = [==[{json.dumps(bag)}]==]}})')
        lines.append(f'print("[palette] {b}: {len(rows)} pieces")')

    print(f'\nspawning {len(lines) // 2} bags...')
    for k in range(0, len(lines), 2):
        tts_api.send({'messageID': tts_api.MSG_EXEC, 'guid': '-1',
                      'script': '\n'.join(lines[k:k + 2])})
        tts_api.listen(2.0)
    print('\ndone. The bags sit off the left edge of the board. Drag a piece out,')
    print('place it, then tag it with !terrain so the density check counts it.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
