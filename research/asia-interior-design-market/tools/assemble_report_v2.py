#!/usr/bin/env python3
"""Assemble the V2 report from _frontmatter-v2 + chapters-v2 (fallback to V1 chapter), plus merged changelog and adjudication log."""
import os, re, sys
BASE = '/home/user/PureGroup-marketing-/research/asia-interior-design-market/05-report'
INT = '/home/user/PureGroup-marketing-/research/asia-interior-design-market/04-research-notes/integration'
CH2, CH1 = os.path.join(BASE, 'chapters-v2'), os.path.join(BASE, 'chapters')
OUT = os.path.join(BASE, 'asia-interior-design-market-report-v2.md')
ORDER = [
  ('第一部 總覽', ['01-overview.md']),
  ('第二部 台灣基準線', ['10-TW.md']),
  ('第三部 第一層：成熟市場', ['11-JP.md', '12-KR.md', '13-SG.md', '14-HK.md']),
  ('第四部 第二層：中高所得成長市場', ['21-CN.md', '22-MY.md', '23-TH.md']),
  ('第五部 第三層：新興市場', ['31-VN.md', '32-ID.md', '33-PH.md', '34-IN.md']),
  ('第六部 跨國主題', ['41-T8.md', '42-T2.md', '43-T3.md', '44-T4.md', '45-T5.md', '46-T6.md', '47-T7.md']),
  ('第七部 對璞石集團的策略意涵', ['90-strategy.md']),
  ('附錄', ['48-T1.md']),
]
def h1(path):
    for line in open(path, encoding='utf-8'):
        if line.startswith('# '): return line[2:].strip()
    return os.path.basename(path)
parts, toc, fallback = [], [], []
front = open(os.path.join(BASE, '_frontmatter-v2.md'), encoding='utf-8').read().rstrip() + '\n'
for part, files in ORDER:
    toc.append(f'- **{part}**')
    body = [f'\n\n---\n\n# {part}\n']
    for f in files:
        p = os.path.join(CH2, f)
        if not os.path.exists(p):
            p = os.path.join(CH1, f); fallback.append(f)
        title = h1(p)
        anchor = re.sub(r'[^\w一-鿿]+', '-', title).strip('-')
        toc.append(f'  - [{title}](#{anchor})')
        body.append('\n\n' + open(p, encoding='utf-8').read().rstrip() + '\n')
    parts.append(''.join(body))
# merged changelog
CL = os.path.join(BASE, 'changelog-parts')
order_codes = ['TW','JP','KR','SG','HK','CN','MY','TH','VN','ID','PH','IN','T8','T2','T3','T4','T5','T6','T7','T1','OV','ST']
cl = ['# V1 → V2 變更紀錄（合併）', '', '整合日期：2026-10-10｜依 `02-integration-protocol.md` §5、§11。各市場對照表見 `04-research-notes/integration/`。', '']
n_rows = 0
for c in order_codes:
    p = os.path.join(CL, c + '.md')
    if not os.path.exists(p): continue
    txt = open(p, encoding='utf-8').read().strip()
    n_rows += len([l for l in txt.split('\n') if re.match(r'\|\s*V2-', l)])
    cl.append('\n' + txt.replace('\n# ', '\n## ', 1) if not txt.startswith('# ') else '\n## ' + txt[2:])
open(os.path.join(BASE, 'v1-to-v2-changelog.md'), 'w', encoding='utf-8').write('\n'.join(cl) + '\n')
# merged adjudication log
adj = ['# 矛盾裁決紀錄 V2（合併自各市場對照表 B 節）', '', '| 編號 | 指標 | 來源 1（值、等級） | 來源 2（值、等級） | 差異原因 | 裁決 | 裁決理由 | 信心 |', '|---|---|---|---|---|---|---|---|']
n_adj = 0
for c in order_codes[:12]:
    p = os.path.join(INT, c + '-reconciliation.md')
    if not os.path.exists(p): continue
    s = open(p, encoding='utf-8').read()
    m = re.search(r'\n## B\. .*?(?=\n## [A-Z]\. |\Z)', s, flags=re.S)
    if not m: continue
    for l in m.group(0).split('\n'):
        if re.match(r'\|\s*V2-', l): adj.append(l); n_adj += 1
open('/home/user/PureGroup-marketing-/research/asia-interior-design-market/04-research-notes/verification/adjudication-log-v2.md', 'w', encoding='utf-8').write('\n'.join(adj) + '\n')
# merged QA log
QA = os.path.join(BASE, 'qa-v2')
if os.path.isdir(QA):
    qa = ['# V2 一致性審查紀錄（合併）', '']
    for f in sorted(os.listdir(QA)):
        qa.append('\n' + open(os.path.join(QA, f), encoding='utf-8').read().strip() + '\n')
    open(os.path.join(BASE, '_qa-log-v2.md'), 'w', encoding='utf-8').write('\n'.join(qa))
doc = front + '\n## 目錄\n\n' + '\n'.join(toc) + '\n' + ''.join(parts)
doc += f'\n\n---\n\n# 附錄 B：V1 → V2 變更摘要\n\n完整變更紀錄（{n_rows} 項）見 `05-report/v1-to-v2-changelog.md`；矛盾裁決（{n_adj} 項）見 `04-research-notes/verification/adjudication-log-v2.md`；各市場指標對照表（A–F 節為 ChatGPT 整合、G 節為 Claude r1 增補）見 `04-research-notes/integration/`；Claude 會話自做的 V1 對 r1 逐格裁決（215 列）見 `03-inbox/claude/verification/adjudication-log-v1-vs-claude-r1.md`；一致性審查紀錄見 `05-report/_qa-log-v2.md`。\n'
open(OUT, 'w', encoding='utf-8').write(doc)
print('written', OUT, len(doc), 'chars; V1 fallback chapters:', fallback, '; changelog rows', n_rows, '; adjudications', n_adj)
