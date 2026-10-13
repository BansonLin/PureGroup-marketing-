# 回報格式規範（Output Format Spec）v1 — 品牌數位資產盤點

所有外部 AI 的報告必須符合本規範，Claude 才能在整合階段自動比對、逐條驗證。三套提示詞內都已內嵌；本檔為正本。

## 1. 報告骨架（章節名稱與順序固定）

```
0. 中繼資料
1. 摘要（Key Takeaways）
2. 五品牌橫向比較表
3. 各品牌章節（每品牌 8 個模組）
4. 競品數字列（依品牌分 5 張表）
5. 關鍵字排名表（M5）
6. 矛盾資料與資料缺口
7. 來源清單
8. 附錄：關鍵指標表（機器可讀 CSV）
```

## 2. 各節規格

### 0. 中繼資料
```
AI：ChatGPT / Gemini / Claude
模式：Deep research / Deep Research / Research
執行日期：YYYY-MM-DD（所有「擷取日期」預設等於此日）
範圍：r1 五品牌全模組 / r2 競品數字列 / g1 Google 生態專題 / c1 定位與訊息分析
開啟頁面數：N
來源總數：N（其中有 URL 者 M；M 必須等於 N，否則說明原因）
```

### 1. 摘要
- 10 點以內，每點一句事實＋一個關鍵數字（含擷取日與來源編號）。只寫事實，不寫建議。

### 2. 五品牌橫向比較表（固定欄位）

| 品牌 | 官網索引頁數 | PageSpeed 行動／桌機 | 官網最近更新日 | FB 追蹤 | IG 追蹤 | Threads 追蹤 | YouTube 訂閱／影片數 | TikTok 追蹤 | 近 90 天社群發文數（全平台合計） | Google 商家評分／評論數 | 進行中廣告數 | 關鍵字組前 10 名命中數／總數 | 擷取日 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

無資料的格子寫「無資料」或「無此資產」，不要留白、不要估。

### 3. 各品牌章節（每品牌都用同樣 8 節，先數字後說明）

M1 官網體檢 → M2 社群 → M3 影音 → M4 評論與口碑 → M5 搜尋能見度（只放該品牌命中情形，完整排名放第 5 章）→ M6 廣告跡象 → M7 電商 → M8 資產缺口
＋ 本品牌關鍵數字表（指標｜數值｜單位｜擷取日｜來源#｜方法｜信心）

### 4. 競品數字列（每品牌一張表，自家品牌放第一列作對照）

| 公司 | 官網 | 索引頁數 | PageSpeed 行動 | 案例或商品數 | 最近更新 | FB 追蹤 | IG 追蹤 | 近 90 天發文數 | Google 評分／評論數 | 進行中廣告數 | 價格帶（電商） | 擷取日 | 來源# |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

### 5. 關鍵字排名表

| 品牌 | 關鍵字 | 名次 1 | 名次 2 | … | 名次 10 | 我們的名次 | 搜尋日 |
|---|---|---|---|---|---|---|---|

每格寫「網域｜頁面類型」，頁面類型取：官網／平台（pro360、100、設計家等）／部落格／地圖／影片／廣告／新聞。

### 6. 矛盾資料與資料缺口
- 矛盾表：指標｜來源 1 數值（日期）｜來源 2 數值（日期）｜差異原因｜你的判斷。
- 缺口表：找不到的項目｜嘗試過的搜尋（逐字）｜建議取得方式。

### 7. 來源清單
`#編號｜標題｜網站｜擷取日｜URL`
- 只列實際開啟過的 URL。禁止虛構；不確定就不要列。

### 8. 附錄：關鍵指標表（機器可讀）
每品牌至少 25 列、每競品至少 8 列，CSV 風格，欄位固定：
```
brand,entity_type,platform,metric,value,unit,as_of_date,source_id,source_url,method,confidence,note
pure-design,own,instagram,followers,1234,人,2026-10-15,#4,https://www.instagram.com/pure.ingenious/,開頁直讀,high,
pure-design,own,website,pagespeed_mobile,41,分,2026-10-15,#9,https://pagespeed.web.dev/...,工具,high,
kuanyue,competitor,google_business,rating,4.8,星,2026-10-15,#21,https://www.google.com/maps/...,開頁直讀,high,評論數 57
```
- `brand` 取：pure-design、pure-house、pu-yu、wayhome-yilan、wayhome-brand（參照）、homatch，競品用英文或拼音代碼並在第 4 章表頭對照。
- `entity_type` 取：own／competitor／benchmark。
- `metric` 用英文小寫底線，常用：followers、posts_total、posts_90d、avg_likes_10、avg_comments_10、engagement_rate、last_post_date、subscribers、videos_total、views_total、rating、reviews、indexed_pages、pagespeed_mobile、pagespeed_desktop、last_update_date、active_ads、products_total、price_min、price_median、price_max、free_shipping_threshold、keyword_rank。
- `method` 取：開頁直讀／工具／站內搜尋／估計。

## 3. 數字與來源紀律
- 每個數字：數值、單位、擷取日、來源編號、方法、信心。
- 社群與評論數字為日期快照；同一指標在不同日期的差異 ≤ 5% 視為一致。
- 找不到就寫「無資料」；禁止用估計填空。
- 第三方估計工具數字 `method` 必填「估計」。
- 不給行銷建議；只給事實。

## 4. 語言與長度
- 繁體中文（台灣用語）；平台、工具、公司名保留原文。
- r1 建議 8,000 到 15,000 字；r2 與 g1 以表格為主，字數不限；c1 建議 5,000 到 8,000 字。證據優先於修辭。
