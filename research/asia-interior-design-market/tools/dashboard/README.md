# 圖表頁「亞洲裝修市場圖解 V2」

Claude Dashboard 型 Artifact：https://claude.ai/artifact/QJsmtK3MLHGvnrX3Bh1wja

- `index.html`：頁面（存在 Artifact 的 `files/index.html`）。
- `data/*.json`：9 個資料集（含 `countries.json` 十二市場摘要，供「聚焦市場」篩選卡使用）；原 8 個（台灣需求訊號、八面向比較、住宅單價區間、商辦裝修單價、商業模式評分、跨境評分、行動路線圖、停損規則），全部摘自 V2 報告，每列附數字標籤。
- 改版：更新 JSON 後重新上傳為 Artifact 資產，再更新對應 `datasets/<id>` 的 `url` 與 `updated`；頁面不含任何寫死的數字。
- 篩選：頁面參數 `market`（`dash/params` 預設 null）；點選頂端市場鈕、色塊表欄位或任一長條即聚焦該市場，其他市場淡出。
- 同一份資料也以 Miro 原生圖形畫在看板第 07 章（`../miro/miro_ch7.py`）。
