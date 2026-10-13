"""Chapter 07 of the Miro board: the dashboard's charts drawn as native Miro shapes.
Reads the dashboard datasets in ../dashboard/data and writes out/b10.svg, out/b11.svg, out/b12.svg."""
import json, os, sys, datetime as dt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from miro_gen import (shape, ta, frame, frame_head, svg, chapter_head, write, nlines, lh,
                      B1, B2, B3, B4, G1, G2, G3, G4, R1, R2, R3, R4, N1, N2, N3, N4, WHITE, SP)

DATA = os.path.join(SP, '..', 'dashboard', 'data') + '/'
L = lambda n: json.load(open(DATA + n))
DASH_URL = 'https://claude.ai/artifact/QJsmtK3MLHGvnrX3Bh1wja'
CH7_Y, ROW1 = 13460, 13590
POS = {}


def num(v):
    return f'{v:,}'


def signed(v):
    return ('+' if v > 0 else '') + f'{v:.1f}'.replace('-', '−')


def rule(x, y, w, h, fill):
    return shape(x, y, w, h, fill, rx=0)


# ---------------- 07-1 Taiwan signals (diverging bars) ----------------
def f_signals(x0, y0):
    rows = sorted([r for r in L('tw.json') if r['kind'] == 'change'], key=lambda r: -r['value'])
    W = 2000
    cx0, cx1 = 64, W - 64
    zero = (cx0 + cx1) / 2
    max_abs = max(abs(r['value']) for r in rows) * 1.3
    px = lambda v: zero + v / max_abs * (cx1 - cx0) / 2
    rowH, top = 132, 200
    H = top + len(rows) * rowH + 40
    e = frame_head(W, '需求訊號：新屋還在、換手斷了', '年增率；右邊增加、左邊減少。數字後為標籤。')
    e.append(rule(zero - 1, top - 10, 2, len(rows) * rowH + 10, N3))
    for i, r in enumerate(rows):
        y = top + i * rowH
        up = r['value'] >= 0
        e.append(ta(cx0, y, cx1 - cx0, f"<b>{r['metric']}</b>（{r['period']}）【{r['label']}】", 18, N4))
        bx, bw = (zero, px(r['value']) - zero) if up else (px(r['value']), zero - px(r['value']))
        e.append(shape(bx, y + 38, bw, 32, B3 if up else R3, rx=6))
        vx = bx + bw + 12 if up else bx - 172
        e.append(ta(vx, y + 40, 160, f"<b>{signed(r['value'])}%</b>", 22, N4, align='left' if up else 'right'))
        e.append(ta(cx0, y + 80, cx1 - cx0, r['note'], 18, N3))
    t = '07-1 需求訊號：新屋還在、換手斷了'
    POS['f20'] = dict(x=x0, y=y0, w=W, h=H, title=t)
    return frame('f20', x0, y0, W, H, t, e), W, H


# ---------------- 07-2 pricing ranges ----------------
def f_pricing(x0, y0):
    rows = sorted(L('pricing.json'), key=lambda r: -(r['low'] + r['high']))
    W = 2400
    cx0, cx1 = 64, W - 64
    vmax = max(r['high'] for r in rows) * 1.04
    px = lambda v: cx0 + v / vmax * (cx1 - cx0)
    rowH, top = 78, 250
    gh = len(rows) * rowH
    H = top + gh + 160
    base = next(r for r in rows if r['code'] == 'TW')
    e = frame_head(W, '住宅中階單價區間（美元／m²）', '淺藍帶＝台灣新成屋中階區間。長條在帶子左邊＝當地比台灣便宜，台灣報價在該市場是負債。C 級行情、口徑各異，全部示意。')
    e.append(shape(64, 180, 30, 30, B4, rx=6))
    e.append(ta(104, 182, 300, '台灣（比較基準）', 18, N3))
    e.append(shape(420, 180, 30, 30, B2, rx=6))
    e.append(ta(460, 182, 200, '其他市場', 18, N3))
    e.append(shape(640, 180, 30, 30, B1, stroke=B2, rx=6))
    e.append(ta(680, 182, 400, '台灣新成屋中階區間', 18, N3))
    e.append(shape(px(base['low']), top - 10, px(base['high']) - px(base['low']), gh + 10, B1, rx=0))
    for t in range(0, int(vmax) + 1, 250):
        e.append(rule(px(t) - 1, top - 10, 2, gh + 10, N2))
        e.append(ta(px(t) - 60, top + gh + 10, 120, num(t), 18, N3, align='center'))
    for i, r in enumerate(rows):
        y = top + i * rowH
        rng = f"{num(r['low'])}–{num(r['high'])}"
        tail = {'低於台灣': f"　台灣為其 {r['multiple']} 倍", '同級': '　與台灣同級', '高於台灣': '　高於台灣'}.get(r['group'], '')
        tw = r['group'] == '台灣'
        e.append(ta(cx0, y, cx1 - cx0, (f"<b>{r['market']}</b>" if tw else r['market']) + f"　{rng}{tail}", 18, N4))
        e.append(shape(px(r['low']), y + 36, max(8, px(r['high']) - px(r['low'])), 26, B4 if tw else B2, rx=6))
    e.append(ta(64, top + gh + 60, W - 128, '口徑：香港為中階私樓、日本為全面翻新（C／D 級來源）、新加坡為轉售組屋（面積以 90 m² 假設），其餘為業者行情；只比區間、不排名次，待璞石內部案件校準。', 18, N3))
    t = '07-2 住宅中階單價區間（美元／m²）'
    POS['f21'] = dict(x=x0, y=y0, w=W, h=H, title=t)
    return frame('f21', x0, y0, W, H, t, e), W, H


# ---------------- 07-3 office fit-out ----------------
def f_fitout(x0, y0):
    rows = sorted(L('fitout.json'), key=lambda r: -r['high'])
    W = 1800
    lx, cx0, cx1 = 64, 300, W - 220
    vmax = max(r['high'] for r in rows)
    px = lambda v: cx0 + v / vmax * (cx1 - cx0)
    rowH, top = 66, 200
    H = top + len(rows) * rowH + 140
    e = frame_head(W, '商辦裝修單價（美元／ft²，2026）', '台北已高於所有東南亞城市，輸出純施工沒有價格優勢。單一顧問估計，示意。')
    for i, r in enumerate(rows):
        y = top + i * rowH
        tp = r['city'] == '台北'
        e.append(ta(lx, y + 12, cx0 - lx - 16, f"<b>{r['city']}</b>" if tp else r['city'], 18, N4, align='right'))
        e.append(shape(cx0, y + 10, px(r['low']) - cx0, 34, B4 if tp else B2, rx=6))
        if r['high'] > r['low']:
            e.append(shape(px(r['low']) + 2, y + 10, px(r['high']) - px(r['low']) - 2, 34, B1, stroke=B2, rx=6))
        v = f"{r['low']}–{r['high']}" if r['high'] > r['low'] else f"{r['high']}"
        e.append(ta(px(r['high']) + 12, y + 12, 180, f'<b>{v}</b>' if tp else v, 18, N4))
    e.append(ta(64, top + len(rows) * rowH + 20, W - 128, '台北 2025 年為 110，一年 +32%（原因未明）；胡志明市約 61，與台北 2025 基本級同價，是越南台商廠辦專案的報價基礎。', 18, N3))
    t = '07-3 商辦裝修單價（美元／ft²）'
    POS['f22'] = dict(x=x0, y=y0, w=W, h=H, title=t)
    return frame('f22', x0, y0, W, H, t, e), W, H


# ---------------- 07-4 cross-border stacked ----------------
SEG = [('T', '台灣優勢可移植性', 0.40, B4), ('M', '市場吸引力', 0.25, B3), ('X', '執行風險', 0.20, G3), ('R', '法規可進入性', 0.15, G2)]
PILL = {'試點': (G2, G4), '有條件': (B1, B4), '不進': (R1, R4)}


def f_xborder(x0, y0):
    rows = sorted(L('xborder.json'), key=lambda r: (-r['score'], r['market']))
    W = 3200
    lx, cx0, cx1 = 64, 260, 1960
    px = lambda v: cx0 + v / 5 * (cx1 - cx0)
    ex = 2300
    rowH, top = 88, 260
    gh = len(rows) * rowH
    H = top + gh + 160
    e = frame_head(W, '跨境分數拆解：四個維度各貢獻多少', '各維度 1–5 分乘上權重，四段加總即綜合分（全部示意）。2026–2027 不設海外法人、不開海外門市，只做輕資產試點。')
    lxx = 64
    for k, name, w, c in SEG:
        e.append(shape(lxx, 180, 30, 30, c, rx=6))
        e.append(ta(lxx + 40, 182, 360, f'{name}（權重 {int(w * 100)}%）', 18, N3))
        lxx += 440
    for t in range(6):
        e.append(rule(px(t) - 1, top - 10, 2, gh + 10, N2))
        e.append(ta(px(t) - 40, top + gh + 10, 80, str(t), 18, N3, align='center'))
    e.append(ta(ex, top - 50, W - ex - 64, '<b>V2 進入路徑</b>', 18, N3))
    for i, r in enumerate(rows):
        y = top + i * rowH
        e.append(ta(lx, y + 22, cx0 - lx - 16, f"<b>{r['market']}</b>", 18, N4, align='right'))
        acc = 0
        for j, (k, name, w, c) in enumerate(SEG):
            v = r[k] * w
            x1, x2 = px(acc), px(acc + v)
            e.append(shape(x1 + (1 if j else 0), y + 18, max(2, x2 - x1 - 2), 36, c, rx=4 if j in (0, 3) else 0))
            acc += v
        e.append(ta(px(acc) + 14, y + 20, 80, f"<b>{r['score']:.1f}</b>", 22, N4))
        f, tc = PILL[r['decision']]
        e.append(shape(px(acc) + 100, y + 20, 110, 34, f, r['decision'], tc, 13, 'center', 'middle', bold=True, rx=17))
        e.append(ta(ex, y + 8, W - ex - 64, r['entry'], 18, N4))
    e.append(ta(64, top + gh + 70, W - 128, '判定：試點＝列入四個具體打法；有條件＝只做設計顧問、授權或供應鏈；不進＝2027 年後再觀察。法律結論需專業人士最終確認。', 18, N3))
    t = '07-4 跨境分數拆解'
    POS['f23'] = dict(x=x0, y=y0, w=W, h=H, title=t)
    return frame('f23', x0, y0, W, H, t, e), W, H


# ---------------- 07-5 business model heat table ----------------
GREEN = {1: (N1, N3), 2: (G1, G4), 3: (G2, G4), 4: (G3, WHITE), 5: (G4, WHITE)}
RED = {1: (N1, N3), 2: (R1, R4), 3: (R2, R4), 4: (R3, WHITE), 5: (R4, WHITE)}
VERD = {'做': (G2, G4), '試': (B1, B4), '不做': (R1, R4)}


def f_models(x0, y0):
    rows = sorted(L('models.json'), key=lambda r: -r['綜合'])
    cols = [('模式', 700), ('契合', 150), ('資本輕', 150), ('SOP', 150), ('毛利', 150), ('L4 難度', 150), ('綜合', 330), ('建議', 150), ('條件', 520)]
    W = 128 + sum(w for _, w in cols)
    top = 200
    rowH = 76
    H = top + 60 + len(rows) * (rowH + 4) + 120
    e = frame_head(W, '商業模式評分色階表（1–5，示意）', '綠色越深越有利；L4 難度紅色越深越依賴創辦人。綜合＝（契合＋資本輕＋SOP＋毛利＋（6 − L4 難度））÷ 5。')
    x = 64
    for t, w in cols:
        e.append(shape(x, top, w - 4, 56, B4, f'<b>{t}</b>', WHITE, 18, 'left' if t in ('模式', '條件') else 'center', 'middle', rx=6))
        x += w
    for i, r in enumerate(rows):
        y = top + 60 + i * (rowH + 4)
        x = 64
        for t, w in cols:
            key = 'L4難度' if t == 'L4 難度' else t
            v = r[key]
            if t == '模式':
                e.append(shape(x, y, w - 4, rowH, N1 if i % 2 == 0 else WHITE, f'<b>{v}</b>', N4, 18, 'left', 'middle', rx=6))
            elif t in ('契合', '資本輕', 'SOP', '毛利'):
                f, tc = GREEN[int(v)]
                e.append(shape(x, y, w - 4, rowH, f, f'<b>{v}</b>', tc, 22, 'center', 'middle', rx=6))
            elif t == 'L4 難度':
                f, tc = RED[int(v)]
                e.append(shape(x, y, w - 4, rowH, f, f'<b>{v}</b>', tc, 22, 'center', 'middle', rx=6))
            elif t == '綜合':
                e.append(shape(x, y, w - 4, rowH, N1 if i % 2 == 0 else WHITE, rx=6))
                e.append(ta(x + 16, y + 22, 70, f'<b>{v:.1f}</b>', 22, N4))
                e.append(shape(x + 90, y + 28, (w - 120) * v / 5, 20, B3, rx=4))
            elif t == '建議':
                f, tc = VERD[v]
                e.append(shape(x + 20, y + 20, w - 44, 36, f, f'<b>{v}</b>', tc, 18, 'center', 'middle', rx=18))
            else:
                e.append(shape(x, y, w - 4, rowH, N1 if i % 2 == 0 else WHITE, v, N4, 18, 'left', 'middle', rx=6))
            x += w
    e.append(ta(64, H - 100, W - 128, '三方共同優先的還有信任產品化與產品化整案含家具搭售（兩者無完整評分，判定「做」，見 05-1）。', 18, N3))
    t = '07-5 商業模式評分色階表'
    POS['f24'] = dict(x=x0, y=y0, w=W, h=H, title=t)
    return frame('f24', x0, y0, W, H, t, e), W, H


# ---------------- 07-6 roadmap gantt ----------------
LANES = [('做', G3), ('試', B3), ('海外', B4), ('決策點', R4), ('外部時程', N3)]


def f_plan(x0, y0):
    rows = L('roadmap.json')
    d = lambda s: dt.date.fromisoformat(s)
    t0, t1 = dt.date(2026, 10, 1), dt.date(2029, 1, 1)
    W = 4200
    cx0, cx1 = 64, W - 64
    px = lambda day: cx0 + (day - t0).days / (t1 - t0).days * (cx1 - cx0)
    top = 260
    items = []
    y = top
    for lane, c in LANES:
        rs = [r for r in rows if r['lane'] == lane]
        if not rs:
            continue
        items.append(('head', lane, c, y))
        y += 48
        for r in rs:
            items.append(('row', r, c, y))
            y += 70
    H = y + 120
    e = frame_head(W, '行動路線圖：先做、再試、後出海', '以 2026 年 11 月啟動為假設（示意）。長條＝執行期間，菱形＝決策點或外部事件，頂端黑色短線＝今天（2026-10-13）。每條試點都有停損條件。')
    lxx = 64
    for lane, c in LANES:
        e.append(shape(lxx, 180, 30, 30, c, rx=6))
        e.append(ta(lxx + 40, 182, 200, '海外試點' if lane == '海外' else lane, 18, N3))
        lxx += 260
    m = t0
    while m <= t1:
        if m.month in (1, 4, 7, 10):
            if m > t0:
                e.append(rule(px(m) - 1, top - 10, 2, y - top + 10, N2))
            e.append(ta(max(cx0, px(m) - 70), top - 44, 140, f'{m.year}-{m.month:02d}', 18, N3, align='left' if m == t0 else 'center'))
        m = dt.date(m.year + (m.month // 12), m.month % 12 + 1, 1)
    today = dt.date(2026, 10, 13)
    e.append(rule(px(today) - 1, top - 84, 3, 40, N4))
    e.append(ta(px(today) + 8, top - 90, 120, '<b>今天</b>', 18, N4))
    for kind, r, c, yy in items:
        if kind == 'head':
            e.append(ta(cx0, yy + 10, 600, f'<b>{"海外試點" if r == "海外" else r}</b>', 18, N3))
            continue
        s, en = d(r['start']), d(r['end'])
        label = f"{r['item']}　｜{r['note']}"
        lw = min(cx1 - cx0, 18 * len(label) * 0.95)
        lx = max(cx0, min(px(s), cx1 - lw))
        e.append(ta(lx, yy, lw + 40, label, 18, N4))
        if r['shape'] == 'bar':
            e.append(shape(px(s), yy + 34, max(10, px(en) - px(s)), 24, c, rx=6))
        else:
            e.append(f'<rect x="{round(px(s) - 13)}" y="{yy + 33}" width="26" height="26" rx="3" fill="{c}" stroke="none" data-rotation="45" />')
    t = '07-6 行動路線圖（2026-11 至 2028-12）'
    POS['f25'] = dict(x=x0, y=y0, w=W, h=H, title=t)
    return frame('f25', x0, y0, W, H, t, e), W, H


# ---------------- assemble ----------------
link = shape(2520, CH7_Y - 4, 2200, 100, B1,
             f'<b>互動版</b>：<a href="{DASH_URL}">開啟「亞洲裝修市場圖解 V2」圖表頁</a>，點選任一市場即可篩選整頁、滑過看每個數字的來源與標籤。',
             N4, 18, 'left', 'middle')
s20, w20, h20 = f_signals(0, ROW1)
s21, w21, h21 = f_pricing(w20 + 320, ROW1)
s22, w22, h22 = f_fitout(w20 + w21 + 640, ROW1)
ROW2 = ROW1 + max(h20, h21, h22) + 160
s23, w23, h23 = f_xborder(0, ROW2)
s24, w24, h24 = f_models(w23 + 320, ROW2)
ROW3 = ROW2 + max(h23, h24) + 160
s25, w25, h25 = f_plan(0, ROW3)
write('b10.svg', svg([chapter_head(0, CH7_Y, '07 圖解：一眼看懂', 'ch7'), link, s20, s21, s22]))
write('b11.svg', svg([s23, s24]))
write('b12.svg', svg([s25]))
json.dump(POS, open(SP + 'out/miro-pos-ch7.json', 'w'), ensure_ascii=False, indent=1)
for k, v in POS.items():
    print(k, v)
