"""Board geometry — real 2D positions, true line-of-sight, and cover.

This is the whole point of the 2D engine: terrain is no longer a probability
knob. A shot is blocked if a solid piece sits on the sight line; cover is the
worst-cover piece the line crosses (or that the target is hugging).
"""
import math

# tunable height-advantage rule (sensitivity sweep): 'off' | 'light' (RAW: ignore Light)
# | 'minus1' (-1 any cover) | 'minus2' (-2 any cover)
HEIGHT_MODE = 'light'


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def toward(a, b, d):
    """Point d inches from a toward b (clamped to b if closer)."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy)
    if L <= d or L == 0:
        return (b[0], b[1])
    return (a[0] + dx / L * d, a[1] + dy / L * d)


class Piece:
    def __init__(self, x1, y1, x2, y2, cover=0, blocks=False, name='', height=0.0):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.cover = cover      # 0 open / 1 light / 2 heavy
        self.blocks = blocks    # True = blocks line of sight (a solid building)
        self.height = height    # top elevation in inches (0 = flat). Stand on its roof at z=height.
        self.name = name

    def contains(self, p, pad=0.0):
        return (self.x1 - pad <= p[0] <= self.x2 + pad and
                self.y1 - pad <= p[1] <= self.y2 + pad)


def _seg_box_interval(p, q, r):
    """Liang-Barsky: the [t0,t1] sub-interval of segment p->q inside box r, or None."""
    x0, y0 = p[0], p[1]
    x1, y1 = q[0], q[1]
    dx, dy = x1 - x0, y1 - y0
    P = (-dx, dx, -dy, dy)
    Q = (x0 - r.x1, r.x2 - x0, y0 - r.y1, r.y2 - y0)
    t0, t1 = 0.0, 1.0
    for pi, qi in zip(P, Q):
        if pi == 0:
            if qi < 0:
                return None
        else:
            t = qi / pi
            if pi < 0:
                if t > t1:
                    return None
                t0 = max(t0, t)
            else:
                if t < t0:
                    return None
                t1 = min(t1, t)
    return (t0, t1) if t0 <= t1 else None


def _seg_hits_box(p, q, r):
    return _seg_box_interval(p, q, r) is not None


def has_los(a, b, terrain):
    """2D ground LOS — kept for melee reachability checks."""
    for r in terrain:
        if not r.blocks:
            continue
        if r.contains(a) or r.contains(b):
            continue
        if _seg_hits_box(a, b, r):
            return False
    return True


def has_los_3d(a, b, terrain):
    """2.5D LOS: a,b are (x,y,z) eye points. A solid building blocks only where the
    sight line actually passes THROUGH it — so a rooftop shooter sees over it."""
    for r in terrain:
        if not r.blocks:
            continue
        if r.contains(a) or r.contains(b):     # standing on/in it doesn't block your own LOS
            continue
        iv = _seg_box_interval(a, b, r)
        if iv is None:
            continue
        t0, t1 = iv
        za, zb = a[2], b[2]
        z_lo = min(za + t0 * (zb - za), za + t1 * (zb - za))
        if z_lo < r.height:                     # the line dips into the solid volume
            return False
    return True


def cover_level_3d(a2, az, b2, bz, terrain, target_down=False):
    """Cover with elevation: a piece only covers a target it rises above, and a
    shooter 2"+ higher than the target ignores Light cover (height advantage)."""
    lvl = 0
    for r in terrain:
        if r.cover == 0 or r.height <= bz + 0.3:   # piece doesn't rise above the target
            continue
        if r.contains(a2, 0.5):                     # shooter's own piece
            continue
        if _seg_hits_box(a2, b2, r) or r.contains(b2, pad=1.0):
            lvl = max(lvl, r.cover)
    if target_down:
        lvl = max(lvl, 2)
    if az >= bz + 2:                                 # height advantage (tunable via HEIGHT_MODE)
        if HEIGHT_MODE == 'light':
            lvl = 0 if lvl == 1 else lvl             # RAW: ignore Light, Heavy still counts
        elif HEIGHT_MODE == 'minus1':
            lvl = max(0, lvl - 1)
        elif HEIGHT_MODE == 'minus2':
            lvl = max(0, lvl - 2)
    return lvl


def building_at(point, terrain):
    """The tallest standable piece whose footprint holds this point (a roof), or None."""
    cand = [r for r in terrain if r.height > 0 and r.contains(point, 0.5)]
    return max(cand, key=lambda r: r.height) if cand else None


def concealing_at(point, terrain):
    """Is this point in or against Concealing terrain? Hide requires it
    (Terrain.md: Hidden is earned via the Hide action in Concealing terrain).
    Any piece offering cover conceals — ruins, scatter, woods, smoke."""
    return any(r.cover >= 1 and r.contains(point, 1.0) for r in terrain)


def take_a_hold():
    """The simplified Take-a-Hold board: 3'x3', 3 centreline objectives on
    heavy-cover structures, LOS-blocking buildings + scatter, 6" deploy bands.

    Terrain is MIRROR-SYMMETRIC about the centreline (y=18): every piece in a
    player's half has a twin in the other's, so the two deployments face
    identical approaches. Without this, A vs B isn't a controlled test."""
    # centred objective structures — heavy cover you can also perch a roof on (4")
    terrain = [
        Piece(3, 15, 9, 21, cover=2, height=4, name='obj-bldg-L'),
        Piece(15, 15, 21, 21, cover=2, height=4, name='obj-bldg-C'),
        Piece(27, 15, 33, 21, cover=2, height=4, name='obj-bldg-R'),
    ]
    # define the lower half, then reflect each piece across y=18 into the upper half
    lower = [
        Piece(8, 6, 15, 11, cover=2, blocks=True, height=5, name='bldg'),
        Piece(28, 5, 34, 10, cover=2, blocks=True, height=5, name='bldg'),
        Piece(4, 9, 7, 12, cover=1, height=1, name='scatter'),
        Piece(21, 10, 24, 13, cover=1, height=1, name='scatter'),
    ]
    for p in lower:
        terrain.append(p)
        terrain.append(Piece(p.x1, 36 - p.y2, p.x2, 36 - p.y1,
                             cover=p.cover, blocks=p.blocks, height=p.height, name=p.name + "'"))
    return dict(
        size=36.0,
        terrain=terrain,
        objectives=[(6, 18), (18, 18), (30, 18)],
        deploy={0: (0, 0, 36, 6), 1: (0, 30, 36, 36)},   # A bottom band, B top band
    )
