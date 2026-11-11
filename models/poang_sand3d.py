"""POANG-style cantilever armchair: two bent-wood side frames (one flat band each, floor runner
rising into the arm and back), a seat-and-back cushion lofted along its own centre line, two
cross rails. Millimetres, Z up, the chair's front towards -Y; width/depth/height are the listed size."""
import json
import math
import sys

import sand3d as s3d


def poang(width=680, depth=830, height=1000):
    D2 = depth / 2
    sx = width / 2 - 45                                      # side frame centre line, from the middle
    # side frame centre line (y, z): rear foot, floor runner to the front, up to the seat edge, back and up the back
    runner = [(D2 - 60, 12), (D2 - 200, 12), (-(D2 - 130), 12), (-(D2 - 45), 95), (-(D2 - 60), 230),
              (-(D2 - 140), 330), (-60, 345), (D2 * 0.45, 520), (D2 - 150, 760), (D2 - 135, height - 70)]
    arm = [(-(D2 - 140), 330), (-(D2 - 150), 520), (-60, 560), (D2 * 0.35, 580), (D2 * 0.5, 640)]
    band = 58                                                # flat band, 58 mm across x, 18 mm thick
    sides = []
    for s in (-1, 1):
        for name, pts in (("runner", runner), ("arm", arm)):
            path = s3d.spline([(s * sx, y, z) for y, z in pts])
            sides.append(s3d.sweep(f"frame_{name}", s3d.rect(band, 18, r=5), path))
    # cushion: one loft, sections square to the centre line (y, z, thickness)
    centre = [(-(D2 - 90), 440, 85), (-D2 * 0.3, 410, 100), (D2 * 0.12, 420, 100), (D2 * 0.45, 560, 85), (D2 - 140, 780, 70), (D2 - 125, height - 60, 55)]
    cw = width - 150
    secs = []
    for i, (y, z, t) in enumerate(centre):
        a, b = centre[max(i - 1, 0)], centre[min(i + 1, len(centre) - 1)]
        ty, tz = b[0] - a[0], b[1] - a[1]
        n = math.hypot(ty, tz); ty, tz = ty / n, tz / n
        secs.append(s3d.at(s3d.superellipse(cw, t, 4), y=y, z=z, rx=math.degrees(math.atan2(-ty, tz))))
    cushion = s3d.loft("cushion", *secs)
    s3d.material(cushion, "fabric", color="#9fb08f")
    for o in sides:
        s3d.material(o, "birch")
    rails = []
    for y in (D2 - 60, -(D2 - 130)):
        r = s3d.extrude("rail", s3d.rect(2 * sx, 40, r=6), 18)
        rails.append(s3d.at(r, y=y, z=0))
    for r in rails:
        s3d.material(r, "birch")
    return s3d.assembly("poang", cushion, *sides, *rails)


if __name__ == "__main__":
    s3d.empty_scene()
    kw = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    root = s3d.group("poang_chair", poang(**kw))
    s3d.export(root, sys.argv[1])
