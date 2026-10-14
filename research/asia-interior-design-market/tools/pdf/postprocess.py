import re, os, html as h
src = open('report.html', encoding='utf-8').read()

# Version-specific cover text; override with environment variables when building other versions.
VER = os.environ.get('REPORT_VERSION', 'V1')
TITLE = f'亞洲室內裝修設計市場研究報告 {VER}'
VERSION_LINE = os.environ.get('REPORT_VERSION_LINE', 'V1（2026-10-09）')
AUTHOR_LINE = os.environ.get('REPORT_AUTHOR_LINE', 'Claude（總指揮）＋ 44 個研究／查核／審查代理')
COVER_NOTE = os.environ.get('REPORT_COVER_NOTE', '本報告為 V1 版：研究環境僅能使用搜尋摘要、無法開啟原始網頁，所有數字請依第 0 章「方法論與已知限制」判讀；法規與稅務結論需專業人士最終確認。')
# fix <title>
src = re.sub(r'<title>.*?</title>', f'<title>{TITLE}</title>', src, count=1, flags=re.S)

cover = f'''<section id="cover">
<div class="cover-kicker">璞石集團 PureGroup ｜ 策略研究</div>
<h1 class="cover-title">亞洲室內裝修設計市場研究報告</h1>
<div class="cover-sub">12 市場 × 3 層級：市場規模、商業模式、法規、消費者、人才、供應鏈與跨境進入評估</div>
<div class="cover-meta">
<div><span>版本</span>{VERSION_LINE}</div>
<div><span>委託人</span>Banson，璞石集團 CEO</div>
<div><span>作者</span>{AUTHOR_LINE}</div>
<div><span>涵蓋市場</span>台灣｜日本、韓國、新加坡、香港｜中國大陸、馬來西亞、泰國｜越南、印尼、菲律賓、印度</div>
<div><span>數字標註</span>【實際】＝有來源可查核 ／【示意】＝假設模型或估算（附假設）</div>
</div>
<div class="cover-note">{COVER_NOTE}</div>
</section>
'''
src = re.sub(r'<header id="title-block-header">.*?</header>\n', cover, src, count=1, flags=re.S)

# TOC heading
src = src.replace('<nav id="TOC" role="doc-toc">', '<nav id="TOC" role="doc-toc">\n<div class="toc-title">目錄</div>', 1)

# classify tables
def classify(m):
    t = m.group(0)
    head = re.search(r'<thead>(.*?)</thead>', t, flags=re.S)
    n = len(re.findall(r'<th', head.group(1))) if head else 0
    cls = []
    if n >= 11: cls.append('wide xwide')
    elif n >= 8: cls.append('wide')
    # first column short?
    firsts = re.findall(r'<tr[^>]*>\s*<t[dh][^>]*>(.*?)</t[dh]>', t, flags=re.S)
    plain = [re.sub(r'<[^>]+>', '', h.unescape(x)).strip() for x in firsts]
    if plain and max(len(x) for x in plain) <= 6:
        cls.append('nf')
    if cls:
        return '<table class="%s">' % ' '.join(cls) + t[len('<table>'):]
    return t
src = re.sub(r'<table>.*?</table>', classify, src, flags=re.S)
# drop horizontal rules that sit directly before a chapter heading (they produced blank pages)
src = re.sub(r'(?:<hr />\s*)+(?=<h1)', '', src)
open('report2.html', 'w', encoding='utf-8').write(src)
print('ok', src.count('class="wide'), src.count('xwide'), src.count(' nf"'), src.count('class="nf"'))
