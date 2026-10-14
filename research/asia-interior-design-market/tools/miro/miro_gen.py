"""Generate Canvas Composer SVG batches for chapters 2-3 to 6 of the Miro board."""
import json, re, math, os, sys

SP = os.path.dirname(os.path.abspath(__file__)) + '/'
REPO = os.path.join(SP, '..', '..', '05-report', 'chapters-v2') + '/'
C = json.load(open(SP + 'miro-countries.json'))
T = json.load(open(SP + 'miro-themes.json'))
STRAT = open(REPO + '90-strategy.md').read()

# ---------- palette ----------
B1, B2, B3, B4 = '#f0f5fd', '#c6dcff', '#659df2', '#305bab'
G1, G2, G3, G4 = '#eaf9ef', '#adf0c7', '#2dc75c', '#067429'
R1, R2, R3, R4 = '#fff0f0', '#ffc6c6', '#ff6464', '#bd0a0a'
N1, N2, N3, N4 = '#f7f7f7', '#e7e7e7', '#595959', '#1a1a1a'
WHITE = '#ffffff'


def clean(s):
    s = re.sub(r'\s*(\[#\d+\])+', '', s)
    s = s.replace('**', '')
    s = s.replace('結構評估→管委會→公設 3 項→戶內', '結構評估、管委會、公設 3 項、戶內')
    s = s.replace('→', ' 至 ')
    s = s.replace('——', '，').replace('—', '，').replace('──', '，')
    s = s.replace('<', '＜').replace('>', '＞').replace('&', '＆')
    s = s.replace('C＆W', '戴德梁行')
    s = re.sub(r'[  ]+', ' ', s)
    s = re.sub(r' ([，。；、）】])', r'\1', s)
    return s.strip()


def esc_attr(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def tw(s, size):
    w = 0.0
    for ch in s:
        o = ord(ch)
        if o < 128:
            w += 0.3 * size if ch in ' .,:;|()' else 0.6 * size
        else:
            w += size
    return w


def nlines(text, width, size):
    tot = 0
    for para in text.split('\n'):
        tot += max(1, math.ceil(tw(para, size) / max(1, width)))
    return tot


def lh(size):
    return {13: 19, 18: 25.5, 22: 31, 33: 47, 67: 94}.get(size, size * 1.42)


def shape(x, y, w, h, fill, html='', tc=N4, size=18, align='left', valign='top',
          stroke=None, sw=2, rx=12, bold=False, sid=None):
    a = '<rect'
    if sid:
        a += f' id="{sid}"'
    a += f' x="{round(x)}" y="{round(y)}" width="{round(w)}" height="{round(h)}" rx="{rx}" fill="{fill}"'
    a += f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ' stroke="none"'
    if html:
        a += f' data-content="{esc_attr(html)}"'
    a += (f' data-text-color="{tc}" data-font-family="noto_sans" data-font-size="{size}"'
          f' data-text-align="{align}" data-text-align-vertical="{valign}"')
    if bold:
        a += ' data-font-weight="bold"'
    return a + ' />'


def ta(x, y, w, body, size=18, color=N4, bold=False, align='left', sid=None):
    a = '<textArea'
    if sid:
        a += f' id="{sid}"'
    a += f' x="{round(x)}" y="{round(y)}" width="{round(w)}" font-family="noto_sans" font-size="{size}" fill="{color}"'
    if bold:
        a += ' font-weight="bold"'
    a += f' text-align="{align}">{body}</textArea>'
    return a


def frame(fid, x, y, w, h, title, children):
    t = esc_attr(title)
    out = [f'<g id="{fid}" transform="translate({round(x)},{round(y)})" data-frame="{t}">',
           f'<rect data-type="frame" x="0" y="0" width="{round(w)}" height="{round(h)}" fill="#ffffff" data-title="{t}" />']
    out += children
    out.append('</g>')
    return '\n'.join(out)


def frame_head(w, title, sub):
    return [ta(64, 56, w - 128, title, 33, N4, True), ta(64, 112, w - 128, sub, 18, N3)]


def svg(parts):
    return '<svg xmlns="http://www.w3.org/2000/svg">\n' + '\n'.join(parts) + '\n</svg>\n'


def chapter_head(x, y, text, sid):
    return ta(x, y, 2400, text, 67, N4, True, sid=sid)


def tagstyle(tag):
    if tag.startswith('實際｜高'):
        return G2, G4
    if tag.startswith('實際'):
        return G1, G4
    return N1, N3


# ---------- country card ----------
TIER_SHORT = {'基準線': '基準線', '第一層：成熟市場': '第一層：成熟市場',
              '第二層：過渡市場': '第二層：過渡市場', '第三層：新興市場': '第三層：新興市場'}


def card_layout(c, W, with_kpi):
    """Return (elements_fn, height). elements_fn(ox, oy) -> list."""
    tx = W - 56
    head_lines = nlines(c['headline'], tx, 22)
    y = 148 + head_lines * lh(22) + 20
    plan = []
    if with_kpi:
        plan.append(('kpi_label', y))
        y += 34
        rows = []
        for k in c['kpis']:
            vl = nlines(clean(k['value']), 680 - 40, 18)
            rh = max(60, vl * lh(18) + 18)
            rows.append((k, y, rh))
            y += rh + 4
        plan.append(('kpis', rows))
        y += 16
    reg = [clean(r) for r in c['regulation']]
    reg_l = sum(nlines('・' + r, tx - 10, 18) for r in reg)
    plan.append(('reg', y, reg_l))
    y += 30 + reg_l * lh(18) + 22
    pl = clean(c['players'])
    pl_l = nlines(pl, tx - 10, 18)
    plan.append(('players', y, pl_l))
    y += 30 + pl_l * lh(18) + 22
    ins = [clean(r) for r in c['insights']]
    ins_l = sum(nlines('・' + r, tx - 10, 18) for r in ins)
    plan.append(('ins', y, ins_l))
    y += 30 + ins_l * lh(18) + 24
    pw = (W - 48) / 2
    ent = clean(c['entry'])
    wat = clean(c['watch'])
    pan_l = max(nlines(ent, pw - 48, 18), nlines(wat, pw - 48, 18)) + 1
    ph = pan_l * lh(18) + 44
    plan.append(('panels', y, ph))
    y += ph + 16
    return plan, y


def card(c, ox, oy, W, H, plan):
    e = []
    e.append(shape(ox, oy, W, H, WHITE, stroke=N2, rx=16))
    e.append(shape(ox, oy, W, 128, B1, rx=16))
    e.append(ta(ox + 28, oy + 20, 640, f"{c['name']}　{c['code']}", 33, N4, True))
    e.append(shape(ox + 28, oy + 78, 260, 34, B2, c['tier'], B4, 13, 'center', 'middle', bold=True))
    e.append(shape(ox + 300, oy + 78, 220, 34, N1, f"資料可信度：{c['confidence']}", N3, 13, 'center', 'middle', bold=True))
    if c['score'] == '基準線':
        e.append(shape(ox + W - 228, oy + 20, 200, 88, B4, '<b>比較基準</b>', WHITE, 22, 'center', 'middle'))
    else:
        e.append(shape(ox + W - 228, oy + 20, 200, 88, B4, f"跨境分數<br><b>{c['score']}</b>／5", WHITE, 22, 'center', 'middle'))
    e.append(ta(ox + 28, oy + 148, W - 56, clean(c['headline']), 22, N4, True))
    for item in plan:
        kind = item[0]
        if kind == 'kpi_label':
            e.append(ta(ox + 28, oy + item[1], 400, '關鍵數字', 18, B4, True))
        elif kind == 'kpis':
            for i, (k, ry, rh) in enumerate(item[1]):
                fill = N1 if i % 2 == 0 else WHITE
                e.append(shape(ox + 16, oy + ry, W - 32, rh, fill, f"<b>{clean(k['label'])}</b>", N3, 18, 'left', 'middle', rx=8))
                e.append(shape(ox + 236, oy + ry, 680, rh, fill, clean(k['value']), N4, 18, 'left', 'middle', rx=0))
                if k['tag']:
                    f, t = tagstyle(k['tag'])
                    if fill == f:
                        f = WHITE if f == N1 else f
                    e.append(shape(ox + 926, oy + ry + (rh - 34) / 2, 158, 34, f, k['tag'], t, 13, 'center', 'middle', bold=True))
        elif kind == 'reg':
            y = item[1]
            e.append(ta(ox + 28, oy + y, 400, '法規與准入', 18, B4, True))
            body = '<br/>'.join('・' + clean(r) for r in c['regulation'])
            e.append(ta(ox + 28, oy + y + 30, W - 56, body, 18, N4))
        elif kind == 'players':
            y = item[1]
            e.append(ta(ox + 28, oy + y, 400, '主要業者', 18, B4, True))
            e.append(ta(ox + 28, oy + y + 30, W - 56, clean(c['players']), 18, N4))
        elif kind == 'ins':
            y = item[1]
            e.append(ta(ox + 28, oy + y, 400, '對璞石的啟示', 18, B4, True))
            body = '<br/>'.join('・' + clean(r) for r in c['insights'])
            e.append(ta(ox + 28, oy + y + 30, W - 56, body, 18, N4))
        elif kind == 'panels':
            y, ph = item[1], item[2]
            pw = (W - 48) / 2
            e.append(shape(ox + 16, oy + y, pw, ph, G1, f"<b>進入路徑</b><br>{clean(c['entry'])}", G4, 18))
            e.append(shape(ox + 32 + pw, oy + y, pw, ph, R1, f"<b>觀察重點</b><br>{clean(c['watch'])}", R4, 18))
    return e


def tier_frame(fid, x, y, title, sub, codes, W=1100, gap=40):
    cs = [next(c for c in C if c['code'] == k) for k in codes]
    plans = [card_layout(c, W, True) for c in cs]
    H = max(p[1] for p in plans)
    fw = 64 * 2 + len(cs) * W + (len(cs) - 1) * gap
    fh = 180 + H + 64
    ch = frame_head(fw, title, sub)
    for i, c in enumerate(cs):
        ch += card(c, 64 + i * (W + gap), 180, W, H, plans[i][0])
    return frame(fid, x, y, fw, fh, title, ch), fw, fh


# ---------- grid helper ----------
def grid(ox, oy, cols, rows, size=18, head_fill=B4, min_h=64, pad=40, row_fills=(N1, WHITE), first_bold=True):
    """cols: list of (title, width). rows: list of list of cell html/plain. returns elements, total height."""
    e = []
    x = ox
    for t, w in cols:
        e.append(shape(x, oy, w - 4, 56, head_fill, f'<b>{t}</b>', WHITE, 18, 'left', 'middle', rx=6))
        x += w
    y = oy + 60
    for ri, r in enumerate(rows):
        lines = 1
        for (t, w), cell in zip(cols, r):
            plain = re.sub(r'<[^>]+>', '', cell.replace('<br>', '\n'))
            lines = max(lines, nlines(plain, w - pad, size))
        rh = max(min_h, lines * lh(size) + 26)
        x = ox
        fill = row_fills[ri % len(row_fills)]
        for ci, ((t, w), cell) in enumerate(zip(cols, r)):
            html = f'<b>{cell}</b>' if (ci == 0 and first_bold) else cell
            e.append(shape(x, y, w - 4, rh, fill, html, N4, size, 'left', 'middle', rx=6))
            x += w
        y += rh + 4
    return e, y - oy


# ---------- markdown table parsing ----------
def md_rows(section_start, prefix_re):
    i = STRAT.index(section_start)
    out = []
    for line in STRAT[i:].split('\n'):
        if re.match(prefix_re, line):
            cells = [clean(x) for x in line.strip().strip('|').split('|')]
            out.append(cells)
    return out


def write(name, content):
    os.makedirs(SP + 'out', exist_ok=True)
    open(SP + 'out/' + name, 'w').write(content)
    print(name, len(content), 'chars', content.count('<rect') + content.count('<textArea'), 'widgets')
