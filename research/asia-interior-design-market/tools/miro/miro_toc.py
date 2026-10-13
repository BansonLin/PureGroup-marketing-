import json, glob, os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from miro_gen import shape, ta, B1, B3, B4, N4

SP = os.path.dirname(os.path.abspath(__file__)) + '/'
BOARD = 'https://miro.com/app/board/uXjVEaC0s_I=/'
frames = {
    '01-1 三個決策問題與 V2 結論': '3458764687102514022',
    '01-2 V1 到 V2 改變了哪些判斷': '3458764687102514023',
    '01-3 研究方法與資料可信度': '3458764687102514024',
    '02-1 台灣基準線：關鍵數字': '3458764687102711295',
    '02-2 台灣在亞洲的位置': '3458764687102711296',
}
for f in sorted(glob.glob(SP + 'out/miro-out-b*.json')):
    d = json.load(open(f))
    frames.update(d.get('frames', {}))
chapters = [('01 決策總覽', '01-'), ('02 台灣基準線', '02-'), ('03 十二市場比較', '03-'),
            ('04 跨國主題與標竿學習', '04-'), ('05 策略：模式、跨境與行動', '05-'), ('06 風險、數據缺口與待確認事項', '06-')]
els = [ta(3720, -40, 2900, '目錄｜點擊連結直接跳到該區塊', 22, B4, True)]
W, G, H = 960, 20, 196
missing = []
for i, (name, pre) in enumerate(chapters):
    col, row = i % 3, i // 3
    x, y = 3720 + col * (W + G), 0 + row * (H + 16)
    items = sorted((t, fid) for t, fid in frames.items() if t.startswith(pre))
    if not items:
        missing.append(name)
    html = f'<b>{name}</b>' + ''.join(f'<br>・<a href="{BOARD}?moveToWidget={fid}">{t}</a>' for t, fid in items)
    els.append(shape(x, y, W, H, B1, html, N4, 18, 'left', 'top'))
print('missing', missing, 'frames', len(frames))
open(SP + 'out/toc-els.txt', 'w').write('\n'.join(els))
