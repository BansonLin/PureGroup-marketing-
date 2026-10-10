#!/usr/bin/env bash
# Build the PDF version of the report (V1 by default; pass report path and version for V2+).
# Requires: pandoc, node + playwright (Chromium), npm package @fontsource/noto-sans-tc (for CJK webfonts).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
# Usage: build.sh [work_dir] [report_md] [version]   e.g. build.sh /tmp/b ../../05-report/asia-interior-design-market-report-v2.md V2
WORK="${1:-$HERE/build}"
REPORT="$(cd "$(dirname "${2:-$HERE/../../05-report/asia-interior-design-market-report-v1.md}")" && pwd)/$(basename "${2:-asia-interior-design-market-report-v1.md}")"
VER="${3:-V1}"
export REPORT_VERSION="$VER"
export NODE_PATH="${NODE_PATH:-/opt/node22/lib/node_modules}"
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
LANG=C.UTF-8 LC_ALL=C.UTF-8 pandoc report-for-pdf.md -f gfm-tex_math_dollars -t html5 --standalone --columns=100000 \
  --toc --toc-depth=2 --metadata title="亞洲室內裝修設計市場研究報告 $VER" --metadata lang=zh-TW \
  --css style.css -o report.html
python3 postprocess.py   # cover page, wide-table classes, removes separators before headings -> report2.html
node topdf.js            # report2.html -> report.pdf (A4, header/footer, outline)
echo "built: $WORK/report.pdf"
