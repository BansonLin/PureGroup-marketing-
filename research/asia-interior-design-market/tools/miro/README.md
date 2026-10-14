# Miro 視覺化看板產生器（V2）

把 V2 報告轉成 Miro 看板「亞洲室內裝修設計市場研究 V2｜璞石集團」：https://miro.com/app/board/uXjVEaC0s_I=/

## 看板結構

| 章 | 框 | 內容來源 |
|---|---|---|
| 01 決策總覽 | 01-1～01-3 | 一頁決策、V1 到 V2 變更、研究方法 |
| 02 台灣基準線 | 02-1～02-3 | 10-TW、heatmap、台灣市場卡 |
| 03 十二市場比較 | 03-1 一覽、03-2～03-4 分層國別卡 | `miro-countries.json`（由 01-overview 與各國章濃縮） |
| 04 跨國主題與標竿 | 04-1 八大主題、04-2 標竿 | `miro-themes.json`（由 41～48 主題章與策略章第 1 節濃縮） |
| 05 策略 | 05-1 做／試／不做、05-2 跨境評分、05-3 30／60／90 天、05-4 停損 | 90-strategy 第 2、3、6 節 |
| 06 風險與待確認 | 06-1 風險登錄、06-2 D1–D11、06-3 專家名單、06-4 待確認與連結 | 90-strategy 第 4、5、6 節 |
| 07 圖解 | 07-1 需求訊號、07-2 單價區間、07-3 商辦單價、07-4 跨境分數拆解、07-5 模式色階表、07-6 路線圖 | `../dashboard/data/*.json`（與互動圖表頁同一份資料），`miro_ch7.py` 產生 |

框的 Miro id 在 `board-ids.json`；看板頂端目錄的每個連結都用 `?moveToWidget=<id>` 跳轉。

## 重建或改版（V2.1）

1. 更新 `miro-countries.json`、`miro-themes.json` 或 `05-report/chapters-v2/90-strategy.md`。
2. `python3 -I miro_build.py`：在 `out/` 產生 b1～b9 九批 Canvas Composer SVG 與 `miro-pos.json`（座標）。第 1、2 章是手寫 SVG，未納入本產生器。
3. 以 Miro MCP `canvas_create_from_svg` 逐批上傳；更新既有看板時，改用 `canvas_read_as_svg` 取得基準後用 `canvas_update_from_svg`，避免重複建立。
4. 上傳結果存成 SVG 後跑 `python3 -I miro_qa.py <result.svg>`，檢查文字與文字、文字與卡片是否重疊。
5. 第 07 章：`python3 -I miro_ch7.py` 產生 b10～b12（以 Miro 原生圖形畫圖表）。
6. `python3 -I miro_toc.py` 依新 id 產生目錄卡片。

## 版面規則（踩過的坑）

- 文字一律用 `<textArea>` 並給明確寬度；`<text>` 會被估成過窄寬度而換行，壓到下一行。
- 原文的「→」在區間用「至」，在門檻判斷（D1–D11）用「則」。
- 字型 Noto Sans；字級 90／67／33／22／18／13；色系：藍（結構）、綠（實際、做、進入路徑）、紅（風險、不做、觀察重點）加中性灰。
- 內部數據（D1–D11）只列「需要什麼」，看板上不放任何集團實際數字。
