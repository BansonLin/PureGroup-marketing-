"""Check a Miro result_svg for text overlaps. Usage: python3 -I miro_qa.py file.svg"""
import re, sys

s = open(sys.argv[1]).read()
items = []
frame_off = None
for line in s.split('\n'):
    m = re.match(r'<g [^>]*transform="translate\(([-\d.]+),([-\d.]+)\)"[^>]*data-frame="([^"]*)"', line)
    if m:
        frame_off = (float(m.group(1)), float(m.group(2)), m.group(3))
        continue
    if line.startswith('</g>'):
        frame_off = None
        continue
    m = re.match(r'<(textArea|rect) [^>]*?data-miro-id="(\d+)" x="([-\d.]+)" y="([-\d.]+)" width="([\d.]+)" height="([\d.]+)"', line)
    if not m or 'data-type="frame"' in line:
        continue
    kind, mid, x, y, w, h = m.group(1), m.group(2), *map(float, m.groups()[2:])
    fo = frame_off or (0, 0, '')
    txt = re.sub(r'<[^>]+>', '', line)[:40] if kind == 'textArea' else (re.search(r'data-content="([^"]{0,40})', line) or [None, ''])[1]
    items.append(dict(kind=kind, id=mid, x=x + fo[0], y=y + fo[1], w=w, h=h, frame=fo[2], txt=txt))


def inter(a, b):
    ix = min(a['x'] + a['w'], b['x'] + b['w']) - max(a['x'], b['x'])
    iy = min(a['y'] + a['h'], b['y'] + b['h']) - max(a['y'], b['y'])
    return ix > 2 and iy > 2, ix, iy


def contains(a, b):  # a contains b
    return a['x'] <= b['x'] + 1 and a['y'] <= b['y'] + 1 and a['x'] + a['w'] >= b['x'] + b['w'] - 1 and a['y'] + a['h'] >= b['y'] + b['h'] - 1


texts = [i for i in items if i['kind'] == 'textArea']
rects = [i for i in items if i['kind'] == 'rect']
bad = 0
for i, a in enumerate(texts):
    for b in texts[i + 1:]:
        ok, ix, iy = inter(a, b)
        if ok:
            bad += 1
            print(f"TEXT/TEXT {a['frame'][:14]} '{a['txt']}' y{a['y']:.0f}+{a['h']:.0f} vs '{b['txt']}' y{b['y']:.0f}+{b['h']:.0f} overlap {iy:.0f}")
    for r in rects:
        ok, ix, iy = inter(a, r)
        if ok and not contains(r, a):
            bad += 1
            print(f"TEXT/RECT {a['frame'][:14]} '{a['txt']}' y{a['y']:.0f}+{a['h']:.0f} x{a['x']:.0f}w{a['w']:.0f} vs rect '{r['txt'][:20]}' y{r['y']:.0f}+{r['h']:.0f} x{r['x']:.0f}w{r['w']:.0f} overlap {iy:.0f}")
print('items', len(items), 'texts', len(texts), 'issues', bad)
