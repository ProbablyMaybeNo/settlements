# -*- coding: utf-8 -*-
"""Generate the Settlements board surface: cracked concrete with a 1" grid.

WHY BAKE THE GRID INTO THE TEXTURE. TTS's own grid overlay is a display setting —
it is global, it drifts if the board is nudged, and it does not travel with a save.
A grid painted into a 36"x36" image is exact BY CONSTRUCTION: 36 squares across a
36-unit board is 1" per square no matter what TTS's units or camera do. TTS grid
snapping is still set on top (build_table.py does it) so pieces click into place,
but the visible truth is in the image.

Line weights carry meaning, because a flat 1" grid is visual noise:
  * hairline  every 1"  — the measuring grid
  * medium    every 6"  — one Move. Also the deployment band depth.
  * heavy     every 12" — the nine density squares (§5), the balance dial
  * centreline           — the objective line, and the raid mirror axis

    py -3.13 make_board.py
    py -3.13 make_board.py --size 4096 --board 36
"""
import argparse
import os
import random
import sys

from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'assets', 'boards')


def concrete(px, board_in, seed=7):
    """Mottled concrete: value noise, aggregate speckle, stains, cracks."""
    rnd = random.Random(seed)

    # base value noise, built small and upscaled so it reads as broad mottling
    small = Image.new('L', (px // 24, px // 24))
    sd = small.load()
    for y in range(small.height):
        for x in range(small.width):
            sd[x, y] = rnd.randint(96, 140)
    base = small.resize((px, px), Image.BICUBIC).filter(ImageFilter.GaussianBlur(px / 400))

    # a second, finer layer of grain
    fine = Image.new('L', (px // 6, px // 6))
    fd = fine.load()
    for y in range(fine.height):
        for x in range(fine.width):
            fd[x, y] = rnd.randint(110, 145)
    fine = fine.resize((px, px), Image.BILINEAR)
    base = Image.blend(base, fine, 0.35)

    img = Image.merge('RGB', (
        base.point(lambda v: min(255, int(v * 1.02))),
        base.point(lambda v: min(255, int(v * 1.00))),
        base.point(lambda v: min(255, int(v * 0.96))),   # faintly warm grey
    ))
    d = ImageDraw.Draw(img, 'RGBA')

    # aggregate speckle — the chips of stone in the mix
    for _ in range(px * 6):
        x, y = rnd.randrange(px), rnd.randrange(px)
        r = rnd.choice((1, 1, 1, 2))
        v = rnd.randint(70, 175)
        d.ellipse([x, y, x + r, y + r], fill=(v, v, v, rnd.randint(40, 110)))

    # oil / damp stains
    for _ in range(26):
        cx, cy = rnd.randrange(px), rnd.randrange(px)
        rr = rnd.randint(px // 60, px // 14)
        dark = rnd.randint(12, 34)
        for k in range(5, 0, -1):
            f = rr * k / 5
            d.ellipse([cx - f, cy - f * 0.8, cx + f, cy + f * 0.8],
                      fill=(0, 0, 0, int(dark / k)))

    # cracks — a random walk, so they wander like real ones
    for _ in range(18):
        x, y = rnd.randrange(px), rnd.randrange(px)
        ang = rnd.uniform(0, 6.28)
        for _ in range(rnd.randint(40, 160)):
            ang += rnd.uniform(-0.35, 0.35)
            nx, ny = x + 6 * random.uniform(0.6, 1.4) * (ang and 1), y
            import math
            nx = x + 7 * math.cos(ang)
            ny = y + 7 * math.sin(ang)
            d.line([x, y, nx, ny], fill=(38, 36, 34, rnd.randint(70, 130)),
                   width=rnd.choice((1, 1, 2)))
            x, y = nx, ny
            if not (0 <= x < px and 0 <= y < px):
                break

    return img.filter(ImageFilter.SMOOTH)


def draw_grid(img, px, board_in, deploy=6):
    d = ImageDraw.Draw(img, 'RGBA')
    ppi = px / board_in                     # pixels per game inch

    def w(scale):
        return max(1, int(round(px / 2048 * scale)))

    # 1" hairlines
    for i in range(board_in + 1):
        p = i * ppi
        d.line([p, 0, p, px], fill=(255, 255, 255, 26), width=w(1))
        d.line([0, p, px, p], fill=(255, 255, 255, 26), width=w(1))
    # 6" — one Move
    for i in range(0, board_in + 1, 6):
        p = i * ppi
        d.line([p, 0, p, px], fill=(255, 255, 255, 54), width=w(2))
        d.line([0, p, px, p], fill=(255, 255, 255, 54), width=w(2))
    # 12" — the nine density squares
    for i in range(0, board_in + 1, 12):
        p = i * ppi
        d.line([p, 0, p, px], fill=(255, 236, 190, 92), width=w(3.5))
        d.line([0, p, px, p], fill=(255, 236, 190, 92), width=w(3.5))
    # the centreline: objectives sit on it, and a raid mirrors about it
    c = px / 2
    d.line([0, c, px, c], fill=(255, 210, 110, 120), width=w(4))

    # deployment bands, 6" from each edge
    for y0, tint in ((0, (150, 190, 235, 30)), (board_in - deploy, (235, 140, 130, 30))):
        d.rectangle([0, y0 * ppi, px, (y0 + deploy) * ppi], fill=tint)
        d.line([0, (y0 + deploy if y0 == 0 else y0) * ppi,
                px, (y0 + deploy if y0 == 0 else y0) * ppi],
               fill=(tint[0], tint[1], tint[2], 150), width=w(3))

    # corner ticks every 12", so you can read position without counting squares
    for i in range(0, board_in + 1, 12):
        for j in range(0, board_in + 1, 12):
            x, y = i * ppi, j * ppi
            s = ppi * 0.22
            d.line([x - s, y, x + s, y], fill=(255, 236, 190, 130), width=w(2))
            d.line([x, y - s, x, y + s], fill=(255, 236, 190, 130), width=w(2))
    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--size', type=int, default=2048, help='texture px (square)')
    ap.add_argument('--board', type=int, default=36, help='board inches per side')
    ap.add_argument('--deploy', type=int, default=6)
    ap.add_argument('--seed', type=int, default=7)
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)

    print(f'generating {args.board}"x{args.board}" concrete at {args.size}px '
          f'({args.size / args.board:.0f} px per inch)...')
    img = concrete(args.size, args.board, args.seed)
    img = draw_grid(img, args.size, args.board, args.deploy)
    path = os.path.join(OUT, f'concrete_{args.board}x{args.board}_grid1in.png')
    img.save(path, optimize=True)
    kb = os.path.getsize(path) / 1024
    print(f'wrote {path}  ({kb:.0f} KB)')
    print(f'\n  1"  hairline   the measuring grid')
    print(f'  6"  medium     one Move · deployment band depth')
    print(f'  12" heavy      the nine density squares (the balance dial)')
    print(f'  centreline     objectives · the raid mirror axis')
    print(f'\nbuild_table.py picks this up automatically as the board surface.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
