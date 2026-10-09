# 跨國主題 F：總體、住宅存量與匯率基準（TF）— 12 市場一致性資料集（r1，獨立三角驗證輪）

> 研究日期：2026-10-09｜研究者：Claude（子代理）｜讀取方式：全部為「搜尋結果內容」（WebFetch／curl 在本環境不可用；未開啟任何 04-research-notes／05-report 檔案）
>
> **重要執行限制（請報告撰寫者先讀）**：本輪在完成 **5 次成功搜尋** 後，觸發「本回合全體代理共用的 WebSearch 上限（200 次／回合）」，之後 3 次搜尋（菲律賓 BSP、印尼 BI、越南 SBV 匯率）被系統拒絕，並明示不得以其他方式繞過。因此：
> - **匯率（第 1 章）**：12 種貨幣中 **9 種已完成**（TWD、JPY、KRW、SGD、HKD、CNY、MYR、THB、INR；來源為美國聯準會 G.5A／G.5）；**VND、IDR、PHP 無資料**。
> - **總體（第 2 章）與住宅（第 3 章）**：本輪 **未能執行任何搜尋**，全部標「無資料」，並列出需執行的查詢（含在地語言）與目標原始資料表，供下一輪補齊。
> - 任務要求的「≥30 次搜尋、≥8 次在地語言住宅搜尋」**未達成**（實際 5 次成功，其中在地語言 1 次）。
> - 我刻意**不以訓練記憶填數**：所有數字皆來自本輪搜尋結果中具體 URL 的內容；未經搜尋的知識一律標為「未驗證」，且不給數字。

---

## 0. 搜尋紀錄摘要

| # | 查詢字串 | 模式 | 語言 | 結果 | 取得內容 |
|---|---|---|---|---|---|
| S1 | Federal Reserve G.5A foreign exchange rates annual 2025 | standard | 英 | 成功 | G.5A（2026-01-05 發布）2025／2024 年平均：JPY、CNY、INR；Broad 美元指數；FRED 方法註記（年平均＝日資料平均、紐約中午買入匯率） |
| S2 | 中央銀行 新台幣 美元 2025年 年平均匯率 | standard | 繁中 | 部分成功 | **未找到央行公布的 2025 年平均匯率**；取得 2025 全年升值 4.27%、央行全年淨買匯 76.9 億美元、2025-06-27 盤中 28.757 |
| S3 | G.5A 2025 annual average Korean won Taiwan dollar Singapore dollar Hong Kong dollar Malaysian ringgit Thai baht per US dollar | extended | 英 | 成功 | G.5A 2025／2024 年平均：KRW、TWD、SGD、HKD、MYR、THB |
| S4 | Federal Reserve G.5 foreign exchange rates monthly September 2026 | extended | 英 | 成功 | G.5（2026-09-01 發布）2026 年 8 月、7 月月平均：JPY、CNY；FRED「Sep 2026」暫定表（CNY 6.7084） |
| S5 | G.5 September 1 2026 August 2026 monthly average Korea won Taiwan dollar Thailand baht India rupee Malaysia ringgit Singapore dollar Hong Kong | extended | 英 | 成功 | 2026 年 8／7／6 月及 2025 年 8 月月平均：HKD、INR、MYR、SGD、KRW、TWD、THB |
| S6 | BSP peso dollar exchange rate 2025 average full year | standard | 英 | **被拒（共用搜尋額度用盡）** | — |
| S7 | rata-rata kurs rupiah 2025 JISDOR Bank Indonesia setahun | extended | 印尼文 | **被拒** | — |
| S8 | tỷ giá trung tâm bình quân năm 2025 VND USD Ngân hàng Nhà nước | extended | 越南文 | **被拒** | — |

- 成功搜尋：5 次（英 4、繁中 1）；被拒：3 次（英 1、印尼文 1、越南文 1）。
- 來源：7 個（TF-01～TF-07），其中在地語言 2 個（繁中）。
- 標示規則：官方統計機構發布的匯率（聯準會為原始發布者，非推估）標【實際】；由兩個官方匯率以公式導出的交叉匯率標【實際】並註明「導出」；搜尋摘要未明確對應到單一 URL 的數字標信心「低」。

---

## 1. 匯率表

### 1.1 主表（每 1 美元可兌換之本幣單位；數值越大＝本幣越弱）

| 幣別 | 2024 年平均 | **2025 年平均（本研究基準）** | **最新值：2026 年 8 月月平均**（G.5，2026-09-01 發布） | 2026 年 7 月 | 2026 年 6 月 | 2025 年 8 月 | 來源# | 信心 |
|---|---|---|---|---|---|---|---|---|
| TWD 新台幣 | 32.1064 | **31.1663** | **32.0229** | 32.2168 | 31.6195 | 30.1538 | TF-01（年）／TF-02（月） | 年：高；月：中 |
| JPY 日圓 | 151.4551 | **149.5686** | **158.8476** | 162.3295 | 無資料 | 無資料 | TF-01／TF-02 | 年：高；月：中 |
| KRW 韓元 | 1,363.4381 | **1,421.3963** | **1,403.2186** | 1,486.0132 | 1,529.4619 | 1,388.9990 | TF-01／TF-02 | 年：高；月：中 |
| SGD 新加坡幣 | 1.3363 | **1.3065** | **1.2763** | 1.2908 | 1.2878 | 1.2847 | TF-01／TF-02 | 年：高；月：中 |
| HKD 港幣 | 7.8030 | **7.7956** | **7.8425** | 7.8407 | 7.8377 | 7.8260 | TF-01／TF-02 | 年：高；月：中 |
| CNY 人民幣 | 7.1957 | **7.1875** | **6.7361** | 6.7757 | 無資料 | 無資料 | TF-01／TF-02 | 年：高；月：中 |
| MYR 馬來西亞令吉 | 4.5747 | **4.2809** | **4.0626** | 4.0813 | 4.0635 | 4.2250 | TF-01／TF-02 | 年：高；月：中 |
| THB 泰銖 | 35.2845 | **32.8619** | **33.0090** | 33.4927 | 32.8990 | 32.4129 | TF-01／TF-02 | 年：高；月：中 |
| INR 印度盧比 | 83.6566 | **87.1468** | **95.4443** | 95.8573 | 94.9600 | 87.5695 | TF-01／TF-02 | 年：高；月：中 |
| VND 越南盾 | 無資料 | **無資料** | **無資料** | — | — | — | — | — |
| IDR 印尼盾 | 無資料 | **無資料** | **無資料** | — | — | — | — | — |
| PHP 菲律賓披索 | 無資料 | **無資料** | **無資料** | — | — | — | — | — |

- 定義（TF-01、TF-06）：聯準會 G.5A 年平均＝**日資料之平均**；匯率為**紐約中午買入匯率**（noon buying rates in New York City for cable transfers payable in foreign currencies）；單位為「每 1 美元之外幣單位」（標星號者除外，本表 9 幣皆非星號幣別）— [G.5A](https://www.federalreserve.gov/releases/g5a/current/)；方法註記見 [FRED AEXCAUS](https://fred.stlouisfed.org/series/AEXCAUS)。
- 最新月資料：G.5 於每月初發布上月月平均；2026-09-01 版（含 2026 年 8 月）為本輪能確認的最新版 — [G.5 2026-09-01](https://www.federalreserve.gov/releases/G5/current/)。依發布慣例，2026-10-01 版應含 9 月月平均，但**本輪搜尋未取得**（推論，非來源陳述）。
- 2026 年 9 月暫定值：FRED「Sep 2026」發布表列 CNY 6.7084（另 AUD 0.7115），但搜尋摘要無法確認其 9 月欄位之計算方式，**信心低、不建議採用** — [FRED Release Tables Sep 2026](https://fred.stlouisfed.org/release/tables?eid=26693&rid=15)。
- 週資料：聯準會 H.10（2026-09-21 版）含 9 月 14–18 日日資料，但搜尋結果僅給歐元，本輪未取得亞洲幣別日值 — [H.10 2026-09-21](https://www.federalreserve.gov/releases/h10/current/default.htm)。
- Broad 美元指數（2006 年 1 月＝100）：2025 年平均 123.0636（TF-01）；2026 年 8 月 118.8512（TF-02）→ 美元在 2026 年整體轉弱，但亞洲幣別分化（見 1.3）。

### 1.2 換算成 TWD 的公式與交叉匯率（導出值）

**公式（同一來源、同一期間的兩條美元匯率相除，不混用來源）**：
- 1 單位外幣 X 值多少新台幣：**TWD／X ＝（TWD per USD）÷（X per USD）**
- 1 新台幣值多少 X：**X／TWD ＝（X per USD）÷（TWD per USD）**
- 本幣金額換美元：**USD ＝ 本幣金額 ÷（本幣 per USD）**；再換台幣：**TWD ＝ USD × 31.1663**（2025 年基準）。
- 範例：2025 年 1 日圓 ＝ 31.1663 ÷ 149.5686 ＝ 0.2084 新台幣（100 日圓 ＝ 20.84 新台幣）。

| 幣別 | 2025 年平均：1 單位 ＝ ? TWD | 2025 年平均：1 TWD ＝ ? 單位 | 2026 年 8 月：1 單位 ＝ ? TWD | 2026 年 8 月：1 TWD ＝ ? 單位 |
|---|---|---|---|---|
| JPY | 0.2084（100 JPY＝20.84） | 4.7990 | 0.2016（100 JPY＝20.16） | 4.9604 |
| KRW | 0.02193（1,000 KRW＝21.93） | 45.6068 | 0.02282（1,000 KRW＝22.82） | 43.8192 |
| SGD | 23.8548 | 0.0419 | 25.0904 | 0.0399 |
| HKD | 3.9979 | 0.2501 | 4.0833 | 0.2449 |
| CNY | 4.3362 | 0.2306 | 4.7539 | 0.2104 |
| MYR | 7.2803 | 0.1374 | 7.8824 | 0.1269 |
| THB | 0.9484 | 1.0544 | 0.9701 | 1.0308 |
| INR | 0.3576 | 2.7962 | 0.3355 | 2.9805 |
| VND／IDR／PHP | 無資料（公式同上，待補美元匯率） | 無資料 | 無資料 | 無資料 |

（以上皆由 TF-01、TF-02 數值以 Python 計算，四捨五入；信心同其輸入值：2025 年＝高，2026 年 8 月＝中。）

### 1.3 匯率變動（對換算結果的影響）

以「每美元兌換單位」計算（＋＝本幣走弱）：

| 幣別 | 2024→2025 年平均 | 2025 年平均 → 2026 年 8 月 |
|---|---|---|
| TWD | −2.9%（台幣走強） | ＋2.7%（台幣走弱） |
| JPY | −1.2% | ＋6.2%（日圓走弱） |
| KRW | ＋4.3%（韓元走弱） | −1.3%；但 2026 年 6 月曾達 1,529.46，6→8 月單位數下降 8.3% |
| SGD | −2.2% | −2.3% |
| HKD | −0.1% | ＋0.6%（7.8425，接近聯繫匯率 7.85 弱方，推論） |
| CNY | −0.1% | −6.3%（人民幣明顯走強） |
| MYR | −6.4%（令吉走強） | −5.1%（續強） |
| THB | −6.9%（泰銖走強） | ＋0.4% |
| INR | ＋4.2%（盧比走弱） | ＋9.5%（盧比顯著走弱） |

### 1.4 台灣中央銀行端的補充（TWD 交叉驗證，未完成）

- 搜尋**未找到中央銀行公布的 2025 年新台幣對美元年平均匯率**（S2）；本研究因此以聯準會 G.5A 的 31.1663 為 TWD 基準。聯準會採紐約中午買入匯率，台北外匯市場收盤／加權平均可能有小幅差異（推論，未量化）。
- 央行 2025 年全年累計**淨買匯 76.9 億美元**（約當 GDP 0.8%），終止連三年淨賣匯 — [聯合報 央行去年砸76.9億美元進場穩匯](https://udn.com/news/story/7239/9407547)（信心：中）。
- 新台幣 2025 全年（年底對年初）對美元**升值 4.27%**（央行統計；此為期末對期初變動，非年平均）— 同上搜尋結果，但摘要未明確指出出自哪一 URL（信心：低）。
- 2025-06-27 新台幣盤中一度升至 **28.757**，創逾三年新高；2025 上半年新台幣對美元升值 9.63%（央行書面報告）— 搜尋摘要未明確對應 URL（候選：[technews 央行第二季理監事會](https://finance.technews.tw/2025/06/20/central-bank-rate-taiwan/)），信心：低。
- 一致性檢查（推論）：G.5 月資料顯示 2025 年 8 月 TWD 30.1538、2025 年平均 31.1663，與「上半年大幅升值、下半年維持在 30 左右」的敘事方向一致，無 >30% 矛盾。

### 1.5 本研究建議的匯率基準（給報告撰寫者）

1. **2025 年流量數據（GDP、市場規模、交易額）**：一律用 **聯準會 G.5A 2025 年平均**（TF-01）。2024 年數據用 G.5A 2024 年平均。同年同源，避免把匯率波動誤當成實質成長。
2. **2026 年價格／報價（每 m² 單價、設計費報價）**：用 **G.5 2026 年 8 月月平均**（TF-02）作「最新值」，並在報告開頭註明「截至 2026-09-01 發布」。
3. **VND、IDR、PHP**：聯準會 G.5／G.5A 不涵蓋（S1、S3 搜尋結果列出的幣別中不含此三者；推論）。下一輪應取 **越南國家銀行（SBV）中心匯率年平均、印尼央行 JISDOR 年平均、菲律賓央行（BSP）參考匯率年平均**，或統一取 **IMF 國際金融統計（IFS）／IMF 月度匯率檔**（[IMF Exchange Rate Archives by Month](https://www.imf.org/external/np/fin/data/param_rms_mth.aspx)，本輪僅見於搜尋結果、未讀內容）。若取得 IMF WEO 資料，也可用「名目 GDP 本幣 ÷ 名目 GDP 美元」得出 WEO 隱含年平均匯率作為後備，但須標示為導出值。
4. **敏感度提醒**：INR 在 2025 年平均與 2026 年 8 月間相差 9.5%，JPY 與 CNY 各約 6%。同一數字用不同年度匯率換算，可能讓排名翻轉，所以報告應固定一套基準，並在比較表註明。

---

## 2. 總體表

> 本章 **全部無資料**：共用搜尋額度用盡，本輪未能執行任何總體查詢。以下保留格位與指定來源版本，避免下一輪混用版本。

| 市場 | 人口 2025 | 名目 GDP 2025（本幣、USD） | 人均 GDP 2024／2025（USD） | 都市化率 | 65+ 占比 2025／2035 | 來源# |
|---|---|---|---|---|---|---|
| 台灣 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 日本 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 韓國 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 新加坡 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 香港 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 中國大陸 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 馬來西亞 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 泰國 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 越南 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 印尼 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 菲律賓 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 印度 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | — |

**下一輪的版本建議（未驗證，僅為方法）**：
- GDP／人均 GDP：12 市場統一用**同一版 IMF 世界經濟展望（WEO）**。今天是 2026-10-09，IMF 的 10 月版通常在 10 月中旬年會期間發布，所以目前最新可用的**可能是 2026 年 4 月版**。這是依發布慣例做的推論，本輪沒有驗證。2026 年數值一律標「IMF 預測」。
- 台灣在 IMF WEO 及聯合國《世界人口展望》（WPP）中，**慣例列為「Taiwan Province of China」**。這是已知慣例，但本輪沒有以搜尋驗證，信心：低。報告中應保留原名稱並加註。
- 人口、65+ 占比 2025／2035、都市化率：建議統一用 **UN WPP 2024 中推計**，以及**聯合國《世界都市化展望》（WUP）**。另並列國家推計：台灣國發會、日本國立社會保障・人口問題研究所、韓國統計廳（통계청）。若國家推計與 WPP 的差距 >30%，列入矛盾表。

---

## 3. 住宅表

> 本章 **全部無資料**（同上原因）。下表為每格應取用的**目標原始資料**（原文名稱），以免下一輪混用不可比口徑。

| 市場 | 住宅存量 | 30 年以上占比 | 自有率 | 年交易量與新屋／中古占比 | 新完工 | 房價趨勢 2022–2026 | 房貸利率 | 目標原始來源（待查） |
|---|---|---|---|---|---|---|---|---|
| 台灣 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 內政部不動產資訊平台（住宅存量、屋齡）；建物買賣移轉棟數；使用執照核發；主計總處家庭收支調查（自有率）；中央銀行五大銀行新承做房貸利率 |
| 日本 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 總務省統計局「令和5年住宅・土地統計調査」（建築の時期別）；國土交通省「建築着工統計」；REINS 中古成約；國交省不動產價格指數 |
| 韓國 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 통계청「주택총조사」（노후기간별 주택）；국토교통부 주택 거래량／준공；한국부동산원 지수；한국은행 주택담보대출 금리 |
| 新加坡 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | HDB Annual Report（組屋存量、屋齡）；SingStat 自有率；URA 私宅價格指數；HDB resale 交易量 |
| 香港 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 差餉物業估價署《香港物業報告》（落成量、存量）；屋宇署樓齡統計；土地註冊處成交；HKMA 按揭利率 |
| 中國大陸 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 第七次全國人口普查「住房建成年代」；國家統計局商品住宅銷售面積／竣工面積；70 城房價指數；LPR |
| 馬來西亞 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | NAPIC（Pusat Maklumat Harta Tanah Negara）住宅存量、交易、竣工；Malaysian House Price Index；BNM 房貸利率 |
| 泰國 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | REIC（ศูนย์ข้อมูลอสังหาริมทรัพย์）新落成登記；BOT 房價指數；NSO 住宅普查 |
| 越南 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | Bộ Xây dựng 住宅市場報告；GSO（Tổng cục Thống kê）人口與住宅普查 2019 |
| 印尼 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | BPS Susenas（kepemilikan rumah）；Bank Indonesia Survei Harga Properti Residensial |
| 菲律賓 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | PSA 2020 Census of Population and Housing；BSP Residential Real Estate Price Index |
| 印度 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | Census 2011 Houselisting；NSS 住宅調查；RBI House Price Index；NHB RESIDEX |
| 跨市場 | — | — | — | — | — | 無資料 | — | BIS Residential Property Price Statistics（統一房價口徑的首選） |

---

## 4. 需求引擎觀察

### 4.1 有證據支持的觀察（僅限匯率）
- **匯率選擇會影響「人均翻修支出」與「占 GDP 比」的跨國比較**：2025 年平均與 2026 年 8 月之間，INR 每美元單位數 ＋9.5%、JPY ＋6.2%、CNY −6.3%、MYR −5.1%（TF-01、TF-02）。若台灣市場規模用 2025 年匯率、印度或中國用 2026 年匯率換算，相對排名會產生 5–10% 的人為偏差。建議所有比較固定使用 2025 年平均（第 1.5 節）。
- **新台幣在 2025 年走強、2026 年回落**（31.1663 → 32.0229）。以台幣計價時，2026 年的海外報價（例如日本、新加坡的每 m² 單價）在帳面上的變化，部分只是匯率造成：日圓報價換成台幣約便宜 3.3%（0.2084 → 0.2016），新加坡幣報價約貴 5.2%（23.85 → 25.09）。這兩個數字由第 1.2 節導出。

### 4.2 分類框架（待驗證假說；本輪無數據支持，不得當作結論引用）
- 判定「存量老化驅動」的建議門檻：30 年以上屋齡占比高、新完工占存量比低（例如 <1%／年）、中古交易占比高、65+ 人口占比高且持續上升。
- 判定「新屋交付驅動」的建議門檻：新完工占存量比高、新屋交易占比高、都市化率仍在上升、人口結構年輕。
- 依一般認知，暫將日本、韓國、台灣、香港歸為偏「存量老化型」，越南、印尼、菲律賓、印度歸為偏「新屋交付型」，中國大陸、馬來西亞、泰國、新加坡歸為「轉換中」。**這只是假說，未經本輪數據驗證**，必須在下一輪取得第 2、3 章數據後才能確認或推翻。
- 對翻修需求的含義（假說）：存量老化型市場的翻修支出與屋齡分布、高齡化（無障礙改修）及中古交易量連動較高；新屋交付型市場的裝修需求則與新屋交付量、建商精裝比例連動較高，受房市循環影響較大。

---

## 5. 矛盾表與缺口表

### 5.1 矛盾表（差異 >30%）
| 指標 | 來源 1 | 來源 2 | 差異原因 | 裁決 |
|---|---|---|---|---|
| — | — | — | 本輪每個指標僅取得單一來源，**未發現 >30% 矛盾** | — |
| TWD／USD（參考，非矛盾） | G.5A 2025 年平均 31.1663（TF-01） | 2025-06-27 盤中 28.757（S2，信心低） | 不同指標：年平均 vs 單日盤中極值，差 7.7%，未達 30% | 不構成矛盾；報告基準採年平均 |

### 5.2 缺口表
| 缺口項目 | 嘗試過的搜尋 | 建議取得方式（下一輪查詢，含在地語言） |
|---|---|---|
| VND、IDR、PHP 的 2025 年平均與 2026 年最新匯率 | S6（BSP，英）、S7（JISDOR，印尼文）、S8（SBV，越南文），三者都因共用額度用盡被拒 | 「BSP reference rate annual average 2025」、「kurs JISDOR rata-rata 2025」、「tỷ giá trung tâm bình quân 2025」；或 IMF IFS 年平均 |
| 台灣央行官方 2025 年平均 TWD／USD | S2（未找到年平均） | 「中央銀行 統計 新台幣對美元 銀行間收盤匯率 年資料 2025」 |
| 2026 年 9 月月平均（G.5 2026-10-01 版） | S4（只取得 2026-09-01 版） | 「federalreserve.gov G.5 October 1 2026」 |
| 12 市場名目 GDP、人均 GDP 2024／2025（IMF WEO 同一版） | 未執行（額度用盡） | 「IMF WEO April 2026 GDP per capita Asia」、「WEO database Taiwan Province of China 2025」 |
| 人口 2025、65+ 占比 2025／2035、都市化率 | 未執行 | 「UN WPP 2024 aged 65+ 2035」；「國發會 人口推估 2025 65歲以上」；「将来推計人口 令和5年 65歳以上 割合 2035」；「장래인구추계 고령인구 비율 2035」 |
| 住宅存量、30 年以上占比、自有率 | 未執行 | 「令和5年住宅・土地統計調査 建築の時期」；「주택총조사 노후주택 30년 이상」；「內政部 住宅存量 屋齡 30年以上」；「七普 住房建成年代」；「NAPIC stok kediaman 2025」；「BPS rumah milik sendiri 2025」 |
| 交易量（新屋 vs 中古）、新完工 2024／2025 | 未執行 | 「建物買賣移轉棟數 2025」；「주택 매매거래량 2025 국토교통부」；「差餉物業估價署 落成量 2025」；「REIC ที่อยู่อาศัยสร้างเสร็จ 2568」；「nhà ở hoàn thành 2025 Bộ Xây dựng」 |
| 房價趨勢 2022–2026 | 未執行 | 「BIS residential property prices Asia 2026」 |
| 房貸利率 2025／2026、翻修貸款產品 | 未執行 | 各央行房貸利率統計；「리모델링 대출」、「リフォームローン 金利 2026」、「home improvement loan Malaysia」 |

---

## 6. 關鍵指標 CSV

```csv
market,metric,value,unit,year,source_id,source_url,definition,confidence
TW,TWD per USD 年平均,31.1663,TWD/USD,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均＝日資料平均；紐約中午買入匯率；【實際】,高
JP,JPY per USD 年平均,149.5686,JPY/USD,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
KR,KRW per USD 年平均,1421.3963,KRW/USD,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
SG,SGD per USD 年平均,1.3065,SGD/USD,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
HK,HKD per USD 年平均,7.7956,HKD/USD,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
CN,CNY per USD 年平均,7.1875,CNY/USD,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
MY,MYR per USD 年平均,4.2809,MYR/USD,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
TH,THB per USD 年平均,32.8619,THB/USD,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
IN,INR per USD 年平均,87.1468,INR/USD,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
TW,TWD per USD 年平均,32.1064,TWD/USD,2024,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
JP,JPY per USD 年平均,151.4551,JPY/USD,2024,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
KR,KRW per USD 年平均,1363.4381,KRW/USD,2024,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
SG,SGD per USD 年平均,1.3363,SGD/USD,2024,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
HK,HKD per USD 年平均,7.8030,HKD/USD,2024,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
CN,CNY per USD 年平均,7.1957,CNY/USD,2024,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
MY,MYR per USD 年平均,4.5747,MYR/USD,2024,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
TH,THB per USD 年平均,35.2845,THB/USD,2024,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
IN,INR per USD 年平均,83.6566,INR/USD,2024,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 G.5A 年平均；【實際】,高
TW,TWD per USD 月平均,32.0229,TWD/USD,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5（2026-09-01 發布）月平均；本輪最新值；【實際】,中
JP,JPY per USD 月平均,158.8476,JPY/USD,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5（2026-09-01 發布）月平均；【實際】,中
KR,KRW per USD 月平均,1403.2186,KRW/USD,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5（2026-09-01 發布）月平均；【實際】,中
SG,SGD per USD 月平均,1.2763,SGD/USD,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5（2026-09-01 發布）月平均；【實際】,中
HK,HKD per USD 月平均,7.8425,HKD/USD,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5（2026-09-01 發布）月平均；【實際】,中
CN,CNY per USD 月平均,6.7361,CNY/USD,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5（2026-09-01 發布）月平均；【實際】,中
MY,MYR per USD 月平均,4.0626,MYR/USD,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5（2026-09-01 發布）月平均；【實際】,中
TH,THB per USD 月平均,33.0090,THB/USD,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5（2026-09-01 發布）月平均；【實際】,中
IN,INR per USD 月平均,95.4443,INR/USD,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5（2026-09-01 發布）月平均；【實際】,中
TW,TWD per USD 月平均,32.2168,TWD/USD,2026-07,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
JP,JPY per USD 月平均,162.3295,JPY/USD,2026-07,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
KR,KRW per USD 月平均,1486.0132,KRW/USD,2026-07,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
SG,SGD per USD 月平均,1.2908,SGD/USD,2026-07,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
HK,HKD per USD 月平均,7.8407,HKD/USD,2026-07,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
CN,CNY per USD 月平均,6.7757,CNY/USD,2026-07,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
MY,MYR per USD 月平均,4.0813,MYR/USD,2026-07,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
TH,THB per USD 月平均,33.4927,THB/USD,2026-07,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
IN,INR per USD 月平均,95.8573,INR/USD,2026-07,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
TW,TWD per USD 月平均,31.6195,TWD/USD,2026-06,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
KR,KRW per USD 月平均,1529.4619,KRW/USD,2026-06,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；本表最弱韓元值，建議覆核；【實際】,中
SG,SGD per USD 月平均,1.2878,SGD/USD,2026-06,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
HK,HKD per USD 月平均,7.8377,HKD/USD,2026-06,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
MY,MYR per USD 月平均,4.0635,MYR/USD,2026-06,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
TH,THB per USD 月平均,32.8990,THB/USD,2026-06,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
IN,INR per USD 月平均,94.9600,INR/USD,2026-06,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均；【實際】,中
TW,TWD per USD 月平均,30.1538,TWD/USD,2025-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均（去年同期比較欄）；【實際】,中
KR,KRW per USD 月平均,1388.9990,KRW/USD,2025-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均（去年同期）；【實際】,中
SG,SGD per USD 月平均,1.2847,SGD/USD,2025-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均（去年同期）；【實際】,中
HK,HKD per USD 月平均,7.8260,HKD/USD,2025-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均（去年同期）；【實際】,中
MY,MYR per USD 月平均,4.2250,MYR/USD,2025-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均（去年同期）；【實際】,中
TH,THB per USD 月平均,32.4129,THB/USD,2025-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均（去年同期）；【實際】,中
IN,INR per USD 月平均,87.5695,INR/USD,2025-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 G.5 月平均（去年同期）；【實際】,中
JP,TWD per 1 JPY（交叉）,0.208375,TWD/JPY,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,導出：31.1663÷149.5686；【實際】導出值,高
KR,TWD per 1 KRW（交叉）,0.021927,TWD/KRW,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,導出：31.1663÷1421.3963；【實際】導出值,高
SG,TWD per 1 SGD（交叉）,23.854803,TWD/SGD,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,導出：31.1663÷1.3065；【實際】導出值,高
HK,TWD per 1 HKD（交叉）,3.997935,TWD/HKD,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,導出：31.1663÷7.7956；【實際】導出值,高
CN,TWD per 1 CNY（交叉）,4.336181,TWD/CNY,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,導出：31.1663÷7.1875；【實際】導出值,高
MY,TWD per 1 MYR（交叉）,7.280315,TWD/MYR,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,導出：31.1663÷4.2809；【實際】導出值,高
TH,TWD per 1 THB（交叉）,0.948402,TWD/THB,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,導出：31.1663÷32.8619；【實際】導出值,高
IN,TWD per 1 INR（交叉）,0.357630,TWD/INR,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,導出：31.1663÷87.1468；【實際】導出值,高
JP,TWD per 1 JPY（交叉）,0.201595,TWD/JPY,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,導出：32.0229÷158.8476；【實際】導出值,中
KR,TWD per 1 KRW（交叉）,0.022821,TWD/KRW,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,導出：32.0229÷1403.2186；【實際】導出值,中
SG,TWD per 1 SGD（交叉）,25.090418,TWD/SGD,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,導出：32.0229÷1.2763；【實際】導出值,中
HK,TWD per 1 HKD（交叉）,4.083252,TWD/HKD,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,導出：32.0229÷7.8425；【實際】導出值,中
CN,TWD per 1 CNY（交叉）,4.753923,TWD/CNY,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,導出：32.0229÷6.7361；【實際】導出值,中
MY,TWD per 1 MYR（交叉）,7.882366,TWD/MYR,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,導出：32.0229÷4.0626；【實際】導出值,中
TH,TWD per 1 THB（交叉）,0.970126,TWD/THB,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,導出：32.0229÷33.0090；【實際】導出值,中
IN,TWD per 1 INR（交叉）,0.335514,TWD/INR,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,導出：32.0229÷95.4443；【實際】導出值,中
CN,CNY per USD（FRED 暫定 9 月欄）,6.7084,CNY/USD,2026-09,TF-03,https://fred.stlouisfed.org/release/tables?eid=26693&rid=15,FRED 發布表「Sep 2026」欄；計算方式未確認；【示意】,低
ALL,Broad 美元指數 年平均,123.0636,指數（2006-01=100）,2025,TF-01,https://www.federalreserve.gov/releases/g5a/current/,聯準會 Broad 名目美元指數（對主要貿易夥伴加權）；【實際】,高
ALL,Broad 美元指數 月平均,118.8512,指數（2006-01=100）,2026-08,TF-02,https://www.federalreserve.gov/releases/G5/current/,聯準會 Broad 名目美元指數；【實際】,中
TW,央行全年淨買匯,76.9,億美元,2025,TF-05,https://udn.com/news/story/7239/9407547,央行全年累計淨買匯（約當 GDP 0.8%）；終止連三年淨賣匯；【示意】單一媒體來源,中
TW,新台幣全年對美元升值幅度,4.27,%,2025,TF-05,https://udn.com/news/story/7239/9407547,年底對年初變動（非年平均）；搜尋摘要未明確對應 URL；【示意】,低
```

（共 71 列資料，全部為匯率相關。總體與住宅指標因本輪無資料，**未列入 CSV**，以免出現空值列；缺口見第 5.2 節。）

---

## 7. 來源清單

| # | 標題 | 機構／作者 | 年份 | 語言 | URL | 讀取方式 |
|---|---|---|---|---|---|---|
| TF-01 | Foreign Exchange Rates – G.5A（Annual），January 05, 2026 | 美國聯邦準備理事會（Board of Governors of the Federal Reserve System） | 2026 | 英 | https://www.federalreserve.gov/releases/g5a/current/ （同版亦見 https://www.federalreserve.gov/releases/g5a/20260105/ ） | 搜尋結果內容 |
| TF-02 | Foreign Exchange Rates – G.5（Monthly），September 01, 2026 | 美國聯邦準備理事會 | 2026 | 英 | https://www.federalreserve.gov/releases/G5/current/ | 搜尋結果內容 |
| TF-03 | Sep 2026, Release Tables: Foreign Exchange Rates | St. Louis Fed（FRED） | 2026 | 英 | https://fred.stlouisfed.org/release/tables?eid=26693&rid=15 | 搜尋結果內容 |
| TF-04 | Foreign Exchange Rates – H.10，September 21, 2026 | 美國聯邦準備理事會 | 2026 | 英 | https://www.federalreserve.gov/releases/h10/current/default.htm | 搜尋結果內容（僅確認存在，未取亞洲幣別數值） |
| TF-05 | 央行去年砸76.9億美元進場穩匯 終止連三年淨賣匯 | 聯合報（udn） | 2026 | 繁中 | https://udn.com/news/story/7239/9407547 | 搜尋結果內容 |
| TF-06 | Canadian Dollars to U.S. Dollar（AEXCAUS）系列說明 | St. Louis Fed（FRED） | 2026 | 英 | https://fred.stlouisfed.org/series/AEXCAUS | 搜尋結果內容（僅用於方法註記：年平均＝日資料平均、紐約中午買入匯率） |
| TF-07 | 央行第二季理監事會關鍵問答 | TechNews 科技新報（整理中央社） | 2025 | 繁中 | https://finance.technews.tw/2025/06/20/central-bank-rate-taiwan/ | 搜尋結果內容（僅作為「上半年升值 9.63%、盤中 28.757」的候選來源，信心低） |
| （參考，未讀內容） | Exchange Rate Archives by Month | IMF | — | 英 | https://www.imf.org/external/np/fin/data/param_rms_mth.aspx | 僅見於搜尋結果標題；下一輪補 VND／IDR／PHP 之建議來源 |
