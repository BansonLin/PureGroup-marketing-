import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from miro_gen import *

POS = {}


def reg(key, x, y, w, h, title):
    POS[key] = dict(x=x, y=y, w=w, h=h, title=title)


# =====================================================================
# Batch 1: TW card (02-3) + chapter 3 header + 03-1 overview grid
# =====================================================================
tw = next(c for c in C if c['code'] == 'TW')
plan, H = card_layout(tw, 1100, False)
fw, fh = 1228, 1320
t53 = '02-3 台灣市場卡：法規、業者與啟示'
ch = frame_head(fw, '台灣市場卡：法規、業者與啟示', '與 12 市場卡同一格式；關鍵數字見 02-1。')
ch += card(tw, 64, 180, 1100, H, plan)
f5b = frame('f5b', 5540, 2110, fw, fh, t53, ch)
reg('f5b', 5540, 2110, fw, fh, t53)

CH3_Y = 3600
FY3 = 3730
order = ['TW', 'SG', 'HK', 'JP', 'KR', 'MY', 'TH', 'CN', 'VN', 'IN', 'PH', 'ID']
cols = [('市場', 240), ('跨境分數', 220), ('人均 GDP（2025）', 320), ('住宅翻修市場', 600), ('中階單價（每坪）', 560), ('一句話定位', 760)]
rows = []
for code in order:
    c = next(x for x in C if x['code'] == code)
    k = {kk['label']: kk for kk in c['kpis']}

    def v(lbl):
        it = k[lbl]
        s = clean(it['value'])
        return s + (f"【{it['tag']}】" if it['tag'] else '')
    tier = c['tier'].split('：')[0]
    score = '比較基準' if c['score'] == '基準線' else f"<b>{c['score']}</b>／5"
    rows.append([f"<b>{c['name']} {code}</b><br>{tier}", score, v('人均 GDP（2025）'), v('住宅翻修市場'), v('中階單價（每坪）'), clean(c['headline'])])
gw = sum(w for _, w in cols)
fw6 = gw + 128
els, gh = grid(64, 180, cols, rows, 18, first_bold=False, min_h=72)
fh6 = 180 + gh + 120
t61 = '03-1 十二市場一覽'
ch = frame_head(fw6, '十二市場一覽：規模、單價與定位', '依分層與跨境分數排序。跨境分數為 V2 單一評分規則（5 分制，全部示意）；數字後的標籤沿用報告：實際＝已核對官方或公司資料，示意＝推估或業者行情。')
ch += els
ch.append(ta(64, 180 + gh + 30, gw, '分層說明：第一層＝人均 GDP 高、存量老化、法規成熟；第二層＝過渡型；第三層＝低所得、新建交屋型。各市場詳細卡片見 03-2 至 03-4。', 18, N3))
f6 = frame('f6', 0, FY3, fw6, fh6, t61, ch)
reg('f6', 0, FY3, fw6, fh6, t61)

# =====================================================================
# Batch 2-4: tier frames
# =====================================================================
x7 = fw6 + 320
t7 = '03-2 第一層：成熟市場（星、港、日、韓）'
f7, fw7, fh7 = tier_frame('f7', x7, FY3, t7, '人均 GDP 高、存量老化、法規成熟。依跨境分數由高至低排列；每張卡：關鍵數字、法規與准入、主要業者、對璞石的啟示、進入路徑與觀察重點。', ['SG', 'HK', 'JP', 'KR'])
reg('f7', x7, FY3, fw7, fh7, t7)
row3b = FY3 + max(fh6, fh7) + 160
t8 = '03-3 第二層：過渡市場（馬、泰、中）'
f8, fw8, fh8 = tier_frame('f8', 0, row3b, t8, '中所得、二手換手比重上升、外資執業限制多。依跨境分數由高至低排列。', ['MY', 'TH', 'CN'])
reg('f8', 0, row3b, fw8, fh8, t8)
x9 = fw8 + 320
t9 = '03-4 第三層：新興市場（越、印、菲、印尼）'
f9, fw9, fh9 = tier_frame('f9', x9, row3b, t9, '低所得、新建交屋為主、單價遠低於台灣。依跨境分數由高至低排列。', ['VN', 'IN', 'PH', 'ID'])
reg('f9', x9, row3b, fw9, fh9, t9)
END3 = row3b + max(fh8, fh9)

# =====================================================================
# Batch 5: chapter 4 themes + benchmarks
# =====================================================================
CH4_Y = END3 + 170
FY4 = CH4_Y + 130


def theme_plan(t, W):
    y = 124 + nlines(clean(t['thesis']), W - 56, 22) * lh(22) + 20
    p = [('label', y)]
    y += 32
    fs = []
    for f in t['findings']:
        f = clean(f)
        rh = max(64, nlines('0　' + f, W - 32 - 48, 18) * lh(18) + 24)
        fs.append((f, y, rh))
        y += rh + 4
    p.append(('finds', fs))
    y += 12
    imp = clean(t['implication'])
    ph = (nlines(imp, W - 32 - 48, 18) + 1) * lh(18) + 36
    p.append(('imp', y, ph, imp))
    y += ph + 16
    return p, y


def theme_card(t, ox, oy, W, H, p):
    e = [shape(ox, oy, W, H, WHITE, stroke=N2, rx=16), shape(ox, oy, W, 104, B1, rx=16),
         shape(ox + 24, oy + 30, 84, 44, B4, f"<b>{t['code']}</b>", WHITE, 18, 'center', 'middle'),
         ta(ox + 128, oy + 28, W - 160, clean(t['title']), 33, N4, True),
         ta(ox + 28, oy + 124, W - 56, clean(t['thesis']), 22, N4, True)]
    for it in p:
        if it[0] == 'label':
            e.append(ta(ox + 28, oy + it[1], 400, '關鍵發現', 18, B4, True))
        elif it[0] == 'finds':
            for i, (f, y, rh) in enumerate(it[1]):
                e.append(shape(ox + 16, oy + y, W - 32, rh, N1 if i % 2 == 0 else WHITE, f'<b>{i + 1}</b>　{f}', N4, 18, 'left', 'middle', rx=8))
        elif it[0] == 'imp':
            e.append(shape(ox + 16, oy + it[1], W - 32, it[2], G1, f'<b>對璞石的意涵</b><br>{it[3]}', G4, 18))
    return e


W = 1100
th = T['themes']
plans = [theme_plan(t, W) for t in th]
rowH = [max(p[1] for p in plans[0:4]), max(p[1] for p in plans[4:8])]
fw10 = 128 + 4 * W + 3 * 40
fh10 = 180 + rowH[0] + 40 + rowH[1] + 64
t10 = '04-1 八大跨國主題：核心論點與發現'
ch = frame_head(fw10, '八大跨國主題：核心論點、關鍵發現與對璞石的意涵', '主題順序依決策關聯度排列：T8 存量與需求、T2 商業模式、T3 法規、T4 數位平台、T5 商業空間、T6 永續高齡補助、T7 跨國擴張、T1 規模可比性。')
for i, t in enumerate(th):
    r, cidx = divmod(i, 4)
    ox = 64 + cidx * (W + 40)
    oy = 180 + (0 if r == 0 else rowH[0] + 40)
    ch += theme_card(t, ox, oy, W, rowH[r], plans[i][0])
f10 = frame('f10', 0, FY4, fw10, fh10, t10, ch)
reg('f10', 0, FY4, fw10, fh10, t10)

BW = 860


def bench_plan(b):
    y = 76
    l1 = nlines('學什麼　' + clean(b['learn']), BW - 48, 18)
    y2 = y + l1 * lh(18) + 14
    l2 = nlines('證據　' + clean(b['evidence']), BW - 48, 18)
    return y, y2, y2 + l2 * lh(18) + 24


bp = [bench_plan(b) for b in T['benchmarks']]
BH = max(p[2] for p in bp)
fw11 = 128 + 2 * BW + 40
fh11 = 180 + 4 * BH + 3 * 32 + 64
t11 = '04-2 標竿學習：8 個可借鏡做法'
ch = frame_head(fw11, '標竿學習：8 個可借鏡做法', '難度 1＝30 天內可導入，難度 4＝需 12 個月試點；證據標籤沿用報告。')
for i, b in enumerate(T['benchmarks']):
    r, cidx = divmod(i, 2)
    ox = 64 + cidx * (BW + 40)
    oy = 180 + r * (BH + 32)
    lv = int(re.search(r'難度 (\d)', b['difficulty']).group(1))
    f, tc = (G1, G4) if lv <= 2 else ((B1, B4) if lv == 3 else (R1, R4))
    y1, y2, _ = bp[i]
    ch += [shape(ox, oy, BW, BH, WHITE, stroke=N2, rx=16),
           ta(ox + 24, oy + 22, BW - 300, clean(b['who']), 22, N4, True),
           shape(ox + BW - 264, oy + 20, 240, 36, f, clean(b['difficulty']), tc, 13, 'center', 'middle', bold=True),
           ta(ox + 24, oy + y1, BW - 48, '<b>學什麼</b>　' + clean(b['learn']), 18, N4),
           ta(ox + 24, oy + y2, BW - 48, '<b>證據</b>　' + clean(b['evidence']), 18, N3)]
x11 = fw10 + 320
f11 = frame('f11', x11, FY4, fw11, fh11, t11, ch)
reg('f11', x11, FY4, fw11, fh11, t11)
END4 = FY4 + max(fh10, fh11)

# =====================================================================
# Batch 6: chapter 5 models + cross-border
# =====================================================================
CH5_Y = END4 + 170
FY5 = CH5_Y + 130
MW = 1000
groups = {'做': [], '試': [], '不做': []}
for m in T['models']:
    v = m['verdict']
    g = '不做' if v.startswith('不做') else ('試' if v.startswith('試') else '做')
    groups[g].append(m)
gstyle = {'做': (G4, G1, G4), '試': (B4, B1, B4), '不做': (R4, R1, R4)}
gsub = {'做': '先做與同步做', '試': '小批量試點', '不做': '永不做或只入駐、採購'}


def model_plan(m):
    n1 = nlines(clean(m['name']), MW - 380 - 80, 22)  # Miro 實際換行比估算早
    y = 20 + max(n1 * lh(22), 36) + 14
    n2 = nlines(clean(m['why']), MW - 48, 18)
    y2 = y + n2 * lh(18) + 14
    n3 = nlines('KPI　' + clean(m['kpi']), MW - 32 - 48, 18)
    kh = n3 * lh(18) + 26
    return y, y2, kh, y2 + kh + 18


colH = {}
for g, ms in groups.items():
    colH[g] = sum(model_plan(m)[3] for m in ms) + 24 * (len(ms) - 1)
fw12 = 128 + 3 * MW + 2 * 40
fh12 = 180 + 72 + 20 + max(colH.values()) + 64
t12 = '05-1 可複製商業模式：做、試、不做'
ch = frame_head(fw12, '可複製商業模式：做、試、不做', 'V2 判定沿用策略章第 2 節表格。共同原則：每條做或試的產品線都指定非創辦人負責人與書面 SOP（L4 承接）。')
for gi, g in enumerate(['做', '試', '不做']):
    ox = 64 + gi * (MW + 40)
    hf, cf, ct = gstyle[g]
    ch.append(shape(ox, 180, MW, 72, hf, f'<b>{g}</b>　{len(groups[g])} 項｜{gsub[g]}', WHITE, 22, 'left', 'middle'))
    oy = 180 + 72 + 20
    for m in groups[g]:
        y1, y2, kh, H = model_plan(m)
        kl = '依據' if m['kpi'].startswith(('反證', '校準')) else 'KPI'
        ch += [shape(ox, oy, MW, H, WHITE, stroke=N2, rx=16),
               ta(ox + 24, oy + 20, MW - 380, clean(m['name']), 22, N4, True),
               shape(ox + MW - 344, oy + 18, 320, 36, cf, clean(m['verdict']), ct, 13, 'center', 'middle', bold=True),
               ta(ox + 24, oy + y1, MW - 48, clean(m['why']), 18, N4),
               shape(ox + 16, oy + y2, MW - 32, kh, N1, f'<b>{kl}</b>　{clean(m["kpi"])}', N4, 18, 'left', 'middle', rx=8)]
        oy += H + 24
f12 = frame('f12', 0, FY5, fw12, fh12, t12, ch)
reg('f12', 0, FY5, fw12, fh12, t12)

# cross-border bars
status = {'SG': '試點', 'VN': '試點', 'HK': '試點', 'JP': '試點', 'MY': '有條件', 'TH': '有條件', 'CN': '有條件', 'PH': '有條件', 'KR': '不進', 'IN': '不進', 'ID': '不進'}
sst = {'試點': (G2, G4), '有條件': (B1, B4), '不進': (R1, R4)}
mk = sorted([c for c in C if c['code'] != 'TW'], key=lambda c: (-float(c['score']), c['code']))
X_LB, X_BAR, BARW, X_SC, X_ST, X_EN, ENW = 64, 300, 600, 920, 1030, 1200, 1040
fw13 = X_EN + ENW + 64
y = 180
ch = frame_head(fw13, '跨境可行性評分與進入路徑', '綜合＝0.25×市場吸引力＋0.15×法規可進入性＋0.40×台灣優勢可移植性＋0.20×執行風險（各 1–5 分，全部示意）。2026–2027 不設海外法人、不開海外門市，只做輕資產試點。')
ch.append(shape(X_LB, y, X_BAR - X_LB - 16, 56, B4, '<b>市場</b>', WHITE, 18, 'left', 'middle', rx=6))
ch.append(shape(X_BAR, y, X_ST - X_BAR - 16, 56, B4, '<b>跨境分數（0–5）</b>', WHITE, 18, 'left', 'middle', rx=6))
ch.append(shape(X_ST, y, X_EN - X_ST - 16, 56, B4, '<b>判定</b>', WHITE, 18, 'center', 'middle', rx=6))
ch.append(shape(X_EN, y, ENW, 56, B4, '<b>V2 進入路徑</b>', WHITE, 18, 'left', 'middle', rx=6))
y += 72
for i, c in enumerate(mk):
    ent = clean(c['entry'])
    nl = nlines(ent, ENW - 40, 18)
    rh = max(76, nl * lh(18) + 28)
    fill = N1 if i % 2 == 0 else WHITE
    sc = float(c['score'])
    ch.append(shape(X_LB, y, fw13 - 128, rh, fill, rx=8))
    ch.append(ta(X_LB + 16, y + rh / 2 - 16, X_BAR - X_LB - 32, f"<b>{c['name']}</b>　{c['code']}", 22, N4))
    ch.append(shape(X_BAR, y + rh / 2 - 14, BARW, 28, N2, rx=6))
    ch.append(shape(X_BAR, y + rh / 2 - 14, BARW * sc / 5, 28, B4 if sc >= 3.0 else B3, rx=6))
    ch.append(ta(X_SC, y + rh / 2 - 16, 100, f'<b>{c["score"]}</b>', 22, N4))
    s = status[c['code']]
    ch.append(shape(X_ST + 10, y + rh / 2 - 18, 130, 36, sst[s][0], s, sst[s][1], 13, 'center', 'middle', bold=True))
    ch.append(shape(X_EN, y, ENW, rh, fill, ent, N4, 18, 'left', 'middle', rx=0))
    y += rh + 4
ch.append(ta(64, y + 24, fw13 - 128, '判定：試點＝列入四個具體打法（越南台商專案與採購、宜蘭旅宿、熊本顧問、星港轉介）；有條件＝只做設計顧問、授權或供應鏈；不進＝2027 年後再觀察。任何海外家居零售門市一律不做。需專業人士最終確認。', 18, N3))
fh13 = max(y + 120, fh12)
x13 = fw12 + 320
t13 = '05-2 跨境可行性評分與進入路徑'
f13 = frame('f13', x13, FY5, fw13, fh13, t13, ch)
reg('f13', x13, FY5, fw13, fh13, t13)
END5a = FY5 + max(fh12, fh13)

# =====================================================================
# Batch 7: 90-day plan + stop-loss
# =====================================================================
FY5b = END5a + 160
plan_rows = md_rows('## 6. Next Steps', r'^\| (30|60|90) 天')
PW = 1000
blocks = []
for r in plan_rows:
    acts = [a for a in re.split(r'；', r[1]) if a]
    body = '<b>行動</b><br/>' + '<br/>'.join('・' + a for a in acts)
    body += f'<br/><br/><b>負責</b><br/>{r[2]}<br/><br/><b>產出</b><br/>{r[3]}<br/><br/><b>需要的內部數據</b><br/>{r[4]}<br/><br/><b>決策點</b><br/>{r[5]}'
    plain = re.sub(r'<[^>]+>', '', body.replace('<br/>', '\n'))
    blocks.append((r[0], body, nlines(plain, PW - 64, 18)))
PH = max(b[2] for b in blocks) * lh(18) + 60
fw14 = 128 + 3 * PW + 2 * 40
i90 = STRAT.index('90 天決策會議只回答三個問題')
note = clean(STRAT[i90:STRAT.index('\n', i90)])
nnl = nlines(note, fw14 - 128, 18)
fh14 = 180 + 72 + 16 + PH + 40 + nnl * lh(18) + 80
t14 = '05-3 30／60／90 天行動計畫'
ch = frame_head(fw14, '30／60／90 天行動計畫', '四個低成本試點的共同設計：不新增資本、指定非創辦人負責人、60 天內有可量測結果。')
for i, (lbl, body, nl) in enumerate(blocks):
    ox = 64 + i * (PW + 40)
    ch.append(shape(ox, 180, PW, 72, B4, f'<b>{lbl}</b>', WHITE, 22, 'left', 'middle'))
    ch.append(shape(ox, 180 + 72 + 16, PW, PH, B1, rx=12))
    ch.append(ta(ox + 28, 180 + 72 + 16 + 24, PW - 56, body, 18, N4))
ch.append(ta(64, 180 + 72 + 16 + PH + 40, fw14 - 128, note, 18, N3))
f14 = frame('f14', 0, FY5b, fw14, fh14, t14, ch)
reg('f14', 0, FY5b, fw14, fh14, t14)

sl = md_rows('停損規則（V2）', r'^\| (買翻賣|交易連動|越南台商專案|越南採購線|熊本顧問|新加坡／香港轉介|海外總暴險) \|')
cols15 = [('項目', 280), ('停損條件', 1000), ('依據', 620)]
els, gh = grid(64, 180, cols15, sl, 18, min_h=72)
fw15 = 128 + sum(w for _, w in cols15)
fh15 = max(180 + gh + 64, fh14)
t15 = '05-4 停損規則'
ch = frame_head(fw15, '停損規則（V2）', '門檻全部示意，待內部數據 D1–D11 校準；達任一條件即停，不開放例外。') + els
x15 = fw14 + 320
f15 = frame('f15', x15, FY5b, fw15, fh15, t15, ch)
reg('f15', x15, FY5b, fw15, fh15, t15)
END5 = FY5b + max(fh14, fh15)

# =====================================================================
# Batch 8: chapter 6 risk register
# =====================================================================
CH6_Y = END5 + 170
FY6 = CH6_Y + 130
rk = md_rows('## 4. 風險與觸發條件', r'^\| (財務|法律勞動|組織單點|品牌稀釋) \d')
cols16 = [('優先序', 180), ('風險', 380), ('觸發條件', 860), ('具體後果', 560), ('緩解', 640), ('監測指標', 540)]
els, gh = grid(64, 180, cols16, rk, 18, min_h=72)
# recolor first column by category
cat = {'財務': (R1, R4), '法律勞動': (B1, B4), '組織單點': (N2, N4), '品牌稀釋': (G1, G4)}
fixed = []
for e in els:
    m = re.search(r'data-content="&lt;b&gt;(財務|法律勞動|組織單點|品牌稀釋) (\d)&lt;/b&gt;"', e)
    if m:
        f, t = cat[m.group(1)]
        e = re.sub(r'fill="[^"]*"', f'fill="{f}"', e, count=1).replace(f'data-text-color="{N4}"', f'data-text-color="{t}"')
    fixed.append(e)
fw16 = 128 + sum(w for _, w in cols16)
fh16 = 180 + gh + 120
t16 = '06-1 風險登錄：觸發條件與監測指標'
ch = frame_head(fw16, '風險登錄：觸發條件、後果、緩解與監測指標', '依集團挑戰優先序：財務＞法律勞動＞組織單點故障＞品牌稀釋。只列有證據的風險。法律與稅務結論需專業人士最終確認。') + fixed
ch.append(ta(64, 180 + gh + 30, fw16 - 128, '讀法：財務三項（交屋潮退場、預收款、買翻賣存貨）同時指向現金；法律勞動風險都有明確時點，可設行事曆提醒；組織單點故障是所有風險的放大器。', 18, N3))
f16 = frame('f16', 0, FY6, fw16, fh16, t16, ch)
reg('f16', 0, FY6, fw16, fh16, t16)

# =====================================================================
# Batch 9: data gaps, experts, open items
# =====================================================================
dg = md_rows('## 5. 內部數據缺口', r'^\| D\d+ \|')
# 改判門檻欄的箭頭是「則」不是區間
dg = [r[:3] + [r[3].replace(' 至 ', '，則').replace('戴德梁行 ', '戴德梁行')] for r in dg]
cols17 = [('代號', 120), ('內部數據', 760), ('校準哪個判斷', 620), ('改判門檻（示意）', 620)]
els, gh = grid(64, 180, cols17, dg, 18, min_h=72)
fw17 = 128 + sum(w for _, w in cols17)
fh17 = 180 + gh + 64
t17 = '06-2 需要璞石補的內部數據 D1–D11'
ch = frame_head(fw17, '需要璞石補的內部數據 D1–D11', '機密：內部數據只用於校準、不外流。優先序：內部數據＞查核值＞章節值；台灣基準線一旦被覆寫，所有台灣對海外倍數與定價力表都要重算。') + els
x17 = fw16 + 320
f17 = frame('f17', x17, FY6, fw17, fh17, t17, ch)
reg('f17', x17, FY6, fw17, fh17, t17)

i_ex = STRAT.index('專家訪談名單')
ex_txt = STRAT[i_ex:STRAT.index('## 來源')]
ex = []
for line in ex_txt.split('\n'):
    m = re.match(r'^\| (台灣|日本|韓國|新加坡|香港|中國大陸|馬來西亞|泰國|越南|印尼|菲律賓|印度) \|', line)
    if m:
        ex.append([clean(x) for x in line.strip().strip('|').split('|')])
cols18 = [('市場', 200), ('訪談對象類型', 1240)]
els, gh = grid(64, 180, cols18, ex, 18, min_h=64)
fw18 = 128 + sum(w for _, w in cols18)
fh18 = 180 + gh + 64
t18 = '06-3 專家訪談名單'
ch = frame_head(fw18, '專家訪談名單', '每市場 2–3 類人，用於內部校準與法規確認；30 天內確定名單，60 天內執行。') + els
x18 = x17 + fw17 + 320
f18 = frame('f18', x18, FY6, fw18, fh18, t18, ch)
reg('f18', x18, FY6, fw18, fh18, t18)

# open items frame below f17/f18
y19 = FY6 + max(fh17, fh18) + 160
fw19 = x18 + fw18 - x17
open_q = ['越南：室內設計 CPC 87907 是否須部會個案同意；外國承包商 212/2026 新制',
          '菲律賓：EO 113 附件對室內設計公司的外資持股上限',
          '印尼：PP 28/2025 之後 BUJK PMA 持股 67%／70% 規定',
          '印度：PN3 對台灣投資是否適用（無官方澄清）',
          '台灣：外資負面表列是否列入室內裝修業；陸資另制',
          '台灣：室內裝修定型化契約公告時點（2025-11 再預告，2026-10 仍未公告）',
          '香港：《建築物條例》修訂 2026 年底提交，落地前不設承建商實體',
          '新加坡：EP 2027 年門檻 S$6,000；DRC 申請人須公民或 PR']
path_v21 = ['收到 D1–D11 內部數據，覆寫台灣基準線（單價、設計費、三線毛利）',
            '重算台灣對海外倍數、定價力表與買翻賣門檻',
            '專家訪談與律師意見裁定左側未決法規問題',
            '90 天決策會議：Q1–Q3 定案、2027 年資本上限與停損點',
            '2027 年中複審：未達停損條件者續行']
PNW = (fw19 - 128 - 2 * 40) / 3
q_html = '<b>待確認法規問題（需專業人士最終確認）</b><br>' + '<br>'.join('・' + q for q in open_q)
p_html = '<b>V2.1 升級路徑</b><br>' + '<br>'.join(f'{i + 1}　{p}' for i, p in enumerate(path_v21))
links = [('V2 決策摘要（Claude 文件）', 'https://claude.ai/code/artifact/eadfc94f-bceb-45c7-a46a-8162955437df'),
         ('研究資料庫與審閱（GitHub PR #1）', 'https://github.com/BansonLin/PureGroup-marketing-/pull/1'),
         ('V2 報告全文（Markdown）', 'https://github.com/BansonLin/PureGroup-marketing-/blob/ccr-bedc4547-m6zdi5/research/asia-interior-design-market/05-report/asia-interior-design-market-report-v2.md'),
         ('V1 到 V2 變更紀錄', 'https://github.com/BansonLin/PureGroup-marketing-/blob/ccr-bedc4547-m6zdi5/research/asia-interior-design-market/05-report/v1-to-v2-changelog.md')]
l_html = '<b>延伸資料</b><br>' + '<br>'.join(f'・<a href="{u}">{t}</a>' for t, u in links) + '<br><br>PDF 全文（523 頁）已另傳；報告原始檔、查核紀錄與 1,783 列變更紀錄都在 PR #1。'
qh = max(nlines(re.sub(r'<[^>]+>', '', q_html.replace('<br>', '\n')), PNW - 48, 18),
         nlines(re.sub(r'<[^>]+>', '', p_html.replace('<br>', '\n')), PNW - 48, 18),
         nlines(re.sub(r'<[^>]+>', '', l_html.replace('<br>', '\n')), PNW - 48, 18)) * lh(18) + 60
fh19 = 180 + qh + 64
t19 = '06-4 待確認事項、V2.1 路徑與延伸資料'
ch = frame_head(fw19, '待確認事項、V2.1 路徑與延伸資料', '這些項目決定 V2 的結論能否升級為定案；資料位置與報告全文連結在右欄。')
ch.append(shape(64, 180, PNW, qh, R1, q_html, R4, 18))
ch.append(shape(64 + PNW + 40, 180, PNW, qh, B1, p_html, B4, 18))
ch.append(shape(64 + 2 * (PNW + 40), 180, PNW, qh, N1, l_html, N4, 18))
f19 = frame('f19', x17, y19, fw19, fh19, t19, ch)
reg('f19', x17, y19, fw19, fh19, t19)

# =====================================================================
# write batches
# =====================================================================
write('b1.svg', svg([f5b, chapter_head(0, CH3_Y, '03 十二市場比較', 'ch3'), f6]))
write('b2.svg', svg([f7]))
write('b3.svg', svg([f8]))
write('b4.svg', svg([f9]))
write('b5.svg', svg([chapter_head(0, CH4_Y, '04 八大跨國主題與標竿學習', 'ch4'), f10, f11]))
write('b6.svg', svg([chapter_head(0, CH5_Y, '05 策略：可複製模式、跨境評分與行動', 'ch5'), f12, f13]))
write('b7.svg', svg([f14, f15]))
write('b8.svg', svg([chapter_head(0, CH6_Y, '06 風險、數據缺口與待確認事項', 'ch6'), f16]))
write('b9.svg', svg([f17, f18, f19]))
POS['heads'] = dict(ch3=CH3_Y, ch4=CH4_Y, ch5=CH5_Y, ch6=CH6_Y)
json.dump(POS, open(SP + 'out/miro-pos.json', 'w'), ensure_ascii=False, indent=1)
for k, v in POS.items():
    print(k, v)
