#!/usr/bin/env bash
# Build the PDF version of the V1 report.
# Requires: pandoc, node + playwright (Chromium), npm package @fontsource/noto-sans-tc (for CJK webfonts).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
REPORT="$HERE/../../05-report/asia-interior-design-market-report-v1.md"
WORK="${1:-$HERE/build}"
mkdir -p "$WORK" && cd "$WORK"
cp "$HERE/style.css" "$HERE/postprocess.py" "$HERE/topdf.js" .
[ -d node_modules/@fontsource/noto-sans-tc ] || npm install --no-save @fontsource/noto-sans-tc >/dev/null
# strip the hand-written 目錄 block (pandoc regenerates a linked TOC)
python3 - "$REPORT" <<'PY'
import re, sys
s = open(sys.argv[1], encoding='utf-8').read()
s = re.sub(r'\n## 目錄\n.*?\n(?=\n---\n)', '\n', s, count=1, flags=re.S)
open('report-for-pdf.md', 'w', encoding='utf-8').write(s)
PY
LANG=C.UTF-8 LC_ALL=C.UTF-8 pandoc report-for-pdf.md -f gfm -t html5 --standalone --columns=100000 \
  --toc --toc-depth=2 --metadata title="亞洲室內裝修設計市場研究報告 V1" --metadata lang=zh-TW \
  --css style.css -o report.html
python3 postprocess.py   # cover page, wide-table classes, removes separators before headings -> report2.html
node topdf.js            # report2.html -> report.pdf (A4, header/footer, outline)
echo "built: $WORK/report.pdf"
