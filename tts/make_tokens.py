# -*- coding: utf-8 -*-
"""Generate Settlements condition/Stress/objective token images for TTS.

WHY GENERATE RATHER THAN DOWNLOAD. Settlements' condition list is specific to
Settlements — Pinned, Suppressed, Off-Balance, Hobbled, Snared, Bleed, and a
Stress count that drives Break tests. No asset pack has those, and a token whose
label does not match the rule it represents is how rules get misplayed at a table.
These are also generated FROM the rules, so if a condition is renamed in the
vault, the tokens follow.

Design is for a TOP-DOWN camera, which is how a TTS table is actually read:
fat ring, high contrast, short word, and colour that groups by rule family.
Colour never carries meaning alone — the word is always there too.

    py -3.13 make_tokens.py
    py -3.13 make_tokens.py --size 512 --out ../tts/assets/tokens

Then in TTS: right-click -> Objects -> Components -> Custom -> Token, and give it
the PNG. Token shape follows the image's alpha, so these come out round.
"""
import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'assets', 'tokens')

# Families, so the table reads at a glance:
#   red      = you are losing wounds / dying
#   orange   = suppression, the ranged non-wound result
#   purple   = control: cannot move / cannot act properly
#   blue     = your own state you chose (Hidden, Ready)
#   yellow   = Stress and nerve
#   green    = markers and devices, which are not conditions at all
FAMILY = {
    'wound':   ((0.78, 0.16, 0.20), 'Losing wounds — the death clocks'),
    'pin':     ((0.87, 0.45, 0.13), 'The ranged non-wound result'),
    'control': ((0.45, 0.30, 0.62), 'Cannot move or cannot act properly'),
    'chosen':  ((0.19, 0.44, 0.66), 'A state you put yourself in'),
    'nerve':   ((0.85, 0.68, 0.14), 'Stress and the nerve states'),
    'marker':  ((0.24, 0.55, 0.40), 'Device/marker states — no Stress, no cap'),
}

# (label, family, sub-caption). Straight from Conditions.md / §10.
TOKENS = [
    ('PINNED',    'pin',     "can't Move · may Shoot"),
    ('SUPPRESSED', 'pin',    'Pinned + no Reactions'),
    ('DOWN',      'wound',   'Stabilize or bleed out'),
    ('PRONE',     'control', 'stand = whole activation'),
    ('HIDDEN',    'chosen',  '-3 to be hit'),
    ('READY',     'chosen',  'one Reaction held'),
    ('GRAPPLED',  'control', 'opposed STR to escape'),
    ('SNARED',    'control', 'Action + STR 7+'),
    ('OFF-BAL',   'control', 'no Sprint/Charge'),
    ('HOBBLED',   'control', '-2" MOV'),
    ('BLIND',     'control', '-2 sight rolls'),
    ('SHOCKED',   'control', '-2 all · no React'),
    ('PROVOKED',  'control', '-1 vs others'),
    ('FIRE',      'wound',   'End Phase: +1 dmg, no armour'),
    ('BLEED',     'wound',   'End Phase: -1 WND'),
    ('POISON',    'wound',   '-1 all · STR 7+ to end'),
    ('BOLT',      'nerve',   'flees to nearest edge'),
    ('BROKEN',    'nerve',   'frozen, cannot act'),
    ('SPOTTED',   'marker',  'identified for skills'),
    ('JAMMED',    'marker',  'remote control fails'),
    ('OVERLOAD',  'marker',  'terminal down till next turn'),
    ('LINKED',    'marker',  'shares a terminal'),
]


# ---------------------------------------------------------------------------
# SHAPE ENCODES CATEGORY. Conditions are ROUND and sit beside a model. Terrain,
# devices and deployables are HEXAGONAL and sit on the board. That way a Pinned
# marker on a fighter can never be misread as an Offline turret, which matters
# because both are the same colour family in any sane palette.
# ---------------------------------------------------------------------------

# The eleven interaction tags actually used across the vault. Every interactive
# point must be VISIBLY marked on the table (§28.5) — nothing interactive is
# invisible — so these exist to satisfy a rule, not as decoration.
TAGS = [
    ('POWERED',     'device',  'needs Power · Disabled without'),
    ('SEARCHABLE',  'terrain', 'INT 7+ · one attempt ever'),
    ('LOCKABLE',    'terrain', 'DEX lockpick / STR force'),
    ('HACKABLE',    'device',  'INT - range band'),
    ('CLIMBABLE',   'terrain', 'AGI test to ascend'),
    ('BREACHABLE',  'terrain', 'STR · Breaching +2'),
    ('OPENABLE',    'terrain', 'Interact to open/close'),
    ('MOVABLE',     'terrain', 'Deadlift / Power Position'),
    ('UNSTABLE',    'terrain', 'may collapse'),
    ('EXPLOSIVE',   'device',  'goes up when hit'),
    ('BARRICADABLE', 'terrain', 'can be blocked up'),
]

# Hacking + Infrastructure. A terminal controls its Linked features (§12); a
# feature starts Powered Down and either crew may flip it back — that
# back-and-forth IS the contest, so both states need a marker.
DEVICES = [
    ('TERMINAL',    'device',  'hack from here · max 24"'),
    ('POWERED DOWN', 'state',  'inert — the default state'),
    ('ACTIVE',      'state',   'flipped on · either crew may flip back'),
    ('OFFLINE',     'state',   'one hit · repair INT 7+ adjacent'),
    ('DESTROYED',   'state',   'second hit · gone for the battle'),
    ('SEARCHED',    'state',   'spent — cannot be searched again'),
    ('ARMED',       'state',   'charge live · 3 End Phases to detonate'),
    ('CONCEALED',   'state',   'passed deploy — enemy cannot see it'),
    ('EXPOSED',     'state',   'failed deploy — visible and inert'),
    ('CRUSH',       'hazard',  '1d10+3 vs 7+, ignores Armour → Down'),
    ('FALL',        'hazard',  '3"+ Prone · 6"+ Injury'),
]

# Deployables (§12.6). One marker per item; state comes from the state hexes
# above so a turret does not need five separate images.
DEPLOYABLES = [
    ('AUTOTURRET',   'turret', '18" · Dmg +3 · Complex -1'),
    ('SNIPER TURRET', 'turret', '24" · +1 hit · Intricate -2'),
    ('BURST TURRET', 'turret', '18" · 2 shots Dmg +2'),
    ('BLAST TURRET', 'turret', '12" · Blast 2"'),
    ('REINF TURRET', 'turret', 'always Heavy cover'),
    ('PROXIMITY',    'mine',   '3" template · on enemy Move'),
    ('REMOTE MINE',  'mine',   '6" radius · owner detonates'),
    ('SEEKER',       'mine',   'moves 4"/round to target'),
    ('TRIP WIRE',    'trap',   '1" → Prone'),
    ('SPIKE STRIP',  'trap',   '3" · Difficult + Hobbled'),
    ('COVERED PIT',  'trap',   '2" → FALL + Snared'),
    ('LEG CLAMP',    'trap',   '1" → Snared'),
    ('RAZOR BARRIER', 'trap',  '3" wall · STR 7+ to pass'),
    ('MUNITIONS',    'beacon', '+1 Injury for allies'),
    ('TARGETING',    'beacon', '+1 ranged hit for allies'),
    ('AEGIS',        'beacon', '-1 enemy Injury vs allies'),
    ('COVER',        'beacon', 'allies count as Light cover'),
    ('CLEANSING',    'beacon', 'clear 1 condition/round'),
    ('REVIVE',       'beacon', 'one Down → Prone/round'),
    ('DREAD',        'beacon', 'enemies +1 Stress on entry'),
]

HAZARDS = [
    ('FIRE ZONE',   'burning — Fire condition'),
    ('ACID',        'Poison on contact'),
    ('ICE',         'AGI test or Off-Balance'),
    ('ELECTRIFIED', 'Shocked'),
    ('DEEP WATER',  'Swim test · Pinned on fail'),
    ('DENSE SMOKE', 'Blind inside · Concealing'),
]

# Area templates at TRUE SCALE. These are the sizes the rules actually use, and
# eyeballing a 6" beacon aura is how a beacon quietly becomes a 9" beacon.
TEMPLATES = [
    (1, 'TRIGGER',   'Trip Wire / Leg Clamp · Engaged'),
    (2, 'BLAST',     'Blast · Covered Pit · Displace'),
    (3, 'AREA',      'mine template · Smoke · Poison · hold radius'),
    (4, 'SEEKER',    'Seeker move / round · Conveyor'),
    (6, 'AURA',      'beacon aura · Remote mine radius'),
    (8, 'LINE',      'Power Supply node range'),
]

EXTRA_FAMILY = {
    'terrain': ((0.36, 0.42, 0.30), 'Terrain interaction tags'),
    'device':  ((0.20, 0.48, 0.55), 'Powered / hackable devices'),
    'state':   ((0.42, 0.42, 0.46), 'Feature and charge states'),
    'hazard':  ((0.72, 0.34, 0.12), 'Board damage keywords'),
    'turret':  ((0.55, 0.22, 0.28), 'Standing hardware — auto-fires'),
    'mine':    ((0.62, 0.34, 0.16), 'Spent on trigger'),
    'trap':    ((0.50, 0.40, 0.18), 'Denies movement'),
    'beacon':  ((0.28, 0.44, 0.62), '6" aura — max two per model'),
}


def _hex_points(size, pad):
    import math
    cx = cy = size / 2.0
    r = size / 2.0 - pad
    return [(cx + r * math.cos(math.radians(a - 90)),
             cy + r * math.sin(math.radians(a - 90))) for a in range(0, 360, 60)]


def hexagon(label, family, caption, size):
    """Hex token — used for anything that sits on the BOARD rather than on a model."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    base = (FAMILY.get(family) or EXTRA_FAMILY[family])[0]
    d.polygon(_hex_points(size, int(size * 0.03)), fill=rgb(base, 0.40))
    d.polygon(_hex_points(size, int(size * 0.10)), fill=rgb(base))
    d.polygon(_hex_points(size, int(size * 0.22)), fill=rgb(base, 0.55))

    lf = fit(d, label, FONT_BOLD, size * 0.66, int(size * 0.17))
    lw = d.textlength(label, font=lf)
    ly = size * (0.40 if caption else 0.44)
    for dx, dy in ((2, 2), (-2, 2), (2, -2), (-2, -2)):
        d.text(((size - lw) / 2 + dx, ly + dy), label, font=lf, fill=(0, 0, 0, 190))
    d.text(((size - lw) / 2, ly), label, font=lf, fill=(255, 255, 255, 255))
    if caption:
        cf = fit(d, caption, FONT_REG, size * 0.70, int(size * 0.078))
        cw = d.textlength(caption, font=cf)
        d.text(((size - cw) / 2, ly + lf.size * 1.08), caption, font=cf,
               fill=(255, 255, 255, 225))
    return img


def template(inches, label, caption, size):
    """A translucent measuring area, labelled with its own diameter.

    Deliberately see-through: it goes ON TOP of models and terrain, and an opaque
    template hides the very thing you are measuring."""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pad = int(size * 0.02)
    box = [pad, pad, size - pad, size - pad]
    d.ellipse(box, fill=(255, 214, 90, 46))                      # faint fill
    ring = max(3, int(size * 0.022))
    d.ellipse(box, outline=(255, 205, 70, 255), width=ring)      # hard edge
    inner = int(size * 0.5)
    d.ellipse([inner - ring, inner - ring, size - inner + ring, size - inner + ring],
              outline=(255, 205, 70, 160), width=max(2, ring // 2))
    # crosshair to centre it on a model
    c = size / 2
    for a, b in (((c, pad * 3), (c, size - pad * 3)), ((pad * 3, c), (size - pad * 3, c))):
        d.line([a, b], fill=(255, 205, 70, 110), width=max(1, ring // 3))

    txt = f'{inches}"'
    f = fit(d, txt, FONT_BOLD, size * 0.30, int(size * 0.20))
    w = d.textlength(txt, font=f)
    for dx, dy in ((3, 3), (-3, 3), (3, -3), (-3, -3)):
        d.text(((size - w) / 2 + dx, c - f.size * 0.72 + dy), txt, font=f, fill=(0, 0, 0, 210))
    d.text(((size - w) / 2, c - f.size * 0.72), txt, font=f, fill=(255, 255, 255, 255))
    lf = fit(d, label, FONT_BOLD, size * 0.34, int(size * 0.085))
    lw = d.textlength(label, font=lf)
    d.text(((size - lw) / 2, c + f.size * 0.30), label, font=lf, fill=(255, 240, 200, 240))
    cf = fit(d, caption, FONT_REG, size * 0.62, int(size * 0.055))
    cw = d.textlength(caption, font=cf)
    d.text(((size - cw) / 2, size * 0.72), caption, font=cf,
           fill=(255, 240, 200, 215))
    return img


def find_font(bold=True):
    """A real font or the labels are unreadable from a table camera."""
    names = (['arialbd.ttf', 'seguisb.ttf', 'segoeuib.ttf', 'calibrib.ttf', 'verdanab.ttf']
             if bold else ['arial.ttf', 'segoeui.ttf', 'calibri.ttf'])
    for n in names:
        p = os.path.join(r'C:\Windows\Fonts', n)
        if os.path.isfile(p):
            return p
    return None


FONT_BOLD = find_font(True)
FONT_REG = find_font(False) or FONT_BOLD


def fit(draw, text, path, max_w, start):
    """Largest size at which `text` fits `max_w`."""
    size = start
    while size > 8:
        f = ImageFont.truetype(path, size) if path else ImageFont.load_default()
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(path, 10) if path else ImageFont.load_default()


def rgb(t, mul=1.0):
    return tuple(int(max(0, min(255, c * 255 * mul))) for c in t)


def disc(label, family, caption, size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    base, _ = FAMILY[family]
    pad = int(size * 0.03)
    box = [pad, pad, size - pad, size - pad]

    # dark outer ring for contrast against light AND dark terrain
    d.ellipse(box, fill=rgb(base, 0.42))
    inner = int(size * 0.085)
    d.ellipse([inner, inner, size - inner, size - inner], fill=rgb(base))
    # a slightly darker plate behind the text so the word always wins
    plate = int(size * 0.20)
    d.ellipse([plate, plate, size - plate, size - plate], fill=rgb(base, 0.72))

    label_font = fit(d, label, FONT_BOLD, size * 0.62, int(size * 0.20))
    lw = d.textlength(label, font=label_font)
    ly = size * (0.40 if caption else 0.44)
    # shadow then fill — cheap outline that survives any background
    for dx, dy in ((2, 2), (-2, 2), (2, -2), (-2, -2)):
        d.text(((size - lw) / 2 + dx, ly + dy), label, font=label_font, fill=(0, 0, 0, 190))
    d.text(((size - lw) / 2, ly), label, font=label_font, fill=(255, 255, 255, 255))

    if caption:
        cf = fit(d, caption, FONT_REG, size * 0.66, int(size * 0.085))
        cw = d.textlength(caption, font=cf)
        cy = ly + label_font.size * 1.05
        d.text(((size - cw) / 2, cy), caption, font=cf, fill=(255, 255, 255, 225))
    return img


def numbered(n, size, base=(0.85, 0.68, 0.14), sub='STRESS'):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pad = int(size * 0.03)
    d.ellipse([pad, pad, size - pad, size - pad], fill=rgb(base, 0.42))
    inner = int(size * 0.085)
    d.ellipse([inner, inner, size - inner, size - inner], fill=rgb(base))
    txt = str(n)
    f = fit(d, txt, FONT_BOLD, size * 0.5, int(size * 0.62))
    w = d.textlength(txt, font=f)
    y = size * 0.14
    for dx, dy in ((3, 3), (-3, 3), (3, -3), (-3, -3)):
        d.text(((size - w) / 2 + dx, y + dy), txt, font=f, fill=(0, 0, 0, 190))
    d.text(((size - w) / 2, y), txt, font=f, fill=(255, 255, 255, 255))
    sf = fit(d, sub, FONT_BOLD, size * 0.6, int(size * 0.11))
    sw = d.textlength(sub, font=sf)
    d.text(((size - sw) / 2, size * 0.78), sub, font=sf, fill=(255, 255, 255, 230))
    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--size', type=int, default=512)
    ap.add_argument('--out', default=OUT)
    args = ap.parse_args()
    out = args.out if os.path.isabs(args.out) else os.path.join(HERE, args.out)
    os.makedirs(out, exist_ok=True)

    if not FONT_BOLD:
        print('WARNING: no TrueType font found in C:\\Windows\\Fonts — labels will be '
              'tiny and unreadable. Install/point at a font before using these.',
              file=sys.stderr)

    made = []
    for label, family, caption in TOKENS:
        img = disc(label, family, caption, args.size)
        fn = os.path.join(out, 'cond_' + label.lower().replace('-', '') + '.png')
        img.save(fn)
        made.append((label, fn))

    for n in range(1, 7):
        img = numbered(n, args.size)
        fn = os.path.join(out, f'stress_{n}.png')
        img.save(fn)
        made.append((f'Stress {n}', fn))

    for n in range(1, 4):
        img = numbered(n, args.size, base=(0.80, 0.66, 0.18), sub='OBJECTIVE')
        fn = os.path.join(out, f'objective_{n}.png')
        img.save(fn)
        made.append((f'Objective {n}', fn))

    def slug(s):
        return ''.join(c if c.isalnum() else '_' for c in s.lower()).strip('_')

    hexes = []
    for label, fam, cap in TAGS:
        hexes.append(('tag_' + slug(label), label, fam, cap))
    for label, fam, cap in DEVICES:
        hexes.append(('dev_' + slug(label), label, fam, cap))
    for label, fam, cap in DEPLOYABLES:
        hexes.append(('dep_' + slug(label), label, fam, cap))
    for label, cap in HAZARDS:
        hexes.append(('haz_' + slug(label), label, 'hazard', cap))
    for prefix, label, fam, cap in hexes:
        img = hexagon(label, fam, cap, args.size)
        fn = os.path.join(out, prefix + '.png')
        img.save(fn)
        made.append((label, fn))

    tpl = []
    for inches, label, cap in TEMPLATES:
        img = template(inches, label, cap, args.size)
        fn = os.path.join(out, f'template_{inches}in.png')
        img.save(fn)
        tpl.append((f'{inches}" {label}', fn))
    made.extend(tpl)

    # a contact sheet so you can eyeball legibility without opening 31 files
    cols = 8
    thumb = 160
    rows = (len(made) + cols - 1) // cols
    sheet = Image.new('RGBA', (cols * thumb, rows * thumb), (28, 28, 30, 255))
    for i, (_, fn) in enumerate(made):
        im = Image.open(fn).resize((thumb, thumb), Image.LANCZOS)
        sheet.alpha_composite(im, ((i % cols) * thumb, (i // cols) * thumb))
    sheet_p = os.path.join(out, '_contact_sheet.png')
    sheet.save(sheet_p)

    print(f'{len(made)} token images -> {out}')
    print('\n  ROUND = conditions, sit beside a MODEL:')
    for fam, (_, why) in FAMILY.items():
        print(f'    {fam:<9} {why}')
    print('\n  HEX = terrain / devices / deployables, sit on the BOARD:')
    for fam, (_, why) in EXTRA_FAMILY.items():
        print(f'    {fam:<9} {why}')
    print('\n  TRANSLUCENT RINGS = area templates at true scale:')
    for inches, label, cap in TEMPLATES:
        print(f'    {str(inches) + chr(34):<4} {label:<9} {cap}')
    print('\n  NOTE on the Remote mine bluff kit (§12.6): buying one gives 1 live +')
    print('  3 DUMMY markers, and they must be indistinguishable. Use the SAME')
    print('  dep_remote_mine.png for all four and put live/dummy in GM Notes only —')
    print('  visibly different dummies would break the mechanic.')
    print(f'\ncontact sheet (open this to check legibility): {sheet_p}')
    print('\nIn TTS: right-click -> Objects -> Components -> Custom -> Token, then')
    print('paste one of these as the Image. Token outline follows the alpha, so they')
    print('come out round. Thickness ~0.2, and tick Stackable for the Stress ones.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
