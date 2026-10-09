# 跨國主題 F：總體、住宅存量與匯率基準（TF）— 12 市場一致性資料集（r1，獨立三角驗證輪）

> 研究日期：2026-10-09｜研究者：Claude（子代理）｜讀取方式：全部為「搜尋結果內容」（WebFetch／curl 在本環境不可用；未開啟任何 04-research-notes／05-report 檔案）
>
> **重要執行限制（請報告撰寫者先讀）**：兩輪都撞上「本回合全體代理共用的 WebSearch 上限（200 次／回合）」，系統明示不得繞過。
> - **第 1 輪**：5 次成功後被拒 3 次。
> - **第 2 輪（補缺口）**：協調者給的上限是 30 次。實際 12 次成功後再次被拒 3 次（台灣、日本、韓國住宅屋齡），依指示立即停止。
> - **累計**：成功 17 次、被拒 6 次。
>
> 目前狀態：
> - **匯率（第 1 章）**：12 種貨幣 **全部有 2025 年平均**。
>   - 9 種用聯準會 G.5A，信心高。
>   - VND、IDR、PHP 改用第三方年平均，信心中，因為央行官方年平均沒找到。
>   - 2026 最新值：VND 和 IDR 仍無資料，PHP 只有 2026 年 5 月月平均。
> - **總體（第 2 章）**：已取得**IMF WEO 2026 年 4 月版**的 12 市場 2025 年名目人均 GDP（經 Worldometer 轉載，信心中），以及 11 市場的 2026 預測值（缺中國大陸）。
>   - 名目 GDP 總額只取得 5 市場。
>   - 人均 GDP 2024 仍無資料。
>   - 65+ 占比只取得 6 市場的 2024 值（世界銀行系列），另有日本、香港 2025 值。2035 預測無資料。
>   - 都市化率只取得 3 市場。
>   - 人口 2025 只有由 IMF 數據導出的 5 市場隱含人口。
> - **住宅（第 3 章）**：**仍全部無資料**，第 2 輪的在地語言住宅搜尋全部被拒。
> - 任務要求的「≥30 次搜尋、≥8 次在地語言住宅搜尋」**仍未達成**：累計成功 17 次，在地語言成功 3 次，住宅類在地語言 0 次。
> - 我刻意**不以訓練記憶填數**：所有數字都來自搜尋結果中具體 URL 的內容；未經搜尋的知識一律標為「未驗證」，且不給數字。

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
| **第 2 輪** | | | | | |
| R2-1 | BSP peso-dollar rate 2025 annual average 58 | standard | 英 | 部分成功 | 未找到 BSP 官方年平均；取得 BSP 參考匯率月平均（2025 年 5／6／7 月、2026 年 5 月） |
| R2-2 | rata-rata nilai tukar rupiah 2025 terhadap dolar AS Bank Indonesia | extended | 印尼文 | 部分成功 | 未找到 BI 官方年平均；取得非官方的 2025 年平均約 16,474／16,475，以及 BI 週報收盤價 |
| R2-3 | tỷ giá trung tâm VND/USD bình quân năm 2025 Ngân hàng Nhà nước | extended | 越南文 | 部分成功 | 未找到 SBV 中心匯率年平均；取得中心匯率高點 25,298（2025-08-22） |
| R2-4 | IRS yearly average currency exchange rates 2025 Philippines peso Indonesia rupiah Vietnam dong | extended | 英 | 部分成功 | PHP 57.509、IDR 16,478.44：第三方以日資料重算；IRS 表不含此二幣 |
| R2-5 | Vietnam dong 2025 average exchange rate per US dollar full year depreciation interbank | extended | 英 | 成功 | VND 2025 年平均 26,005.133（CEIC，世界銀行系列）、26,008、26,009；2024／2025 年底值 |
| R2-6 | IMF World Economic Outlook April 2026 GDP per capita Asia … | extended | 英 | 成功 | WEO 2026 年 4 月版，2026 年人均 GDP **預測**（11 市場，缺中國大陸）；確認 2026 年 4 月版統計附錄存在 |
| R2-7 | Worldometer GDP per capita Asia 2025 IMF nominal China Taiwan Japan Korea | extended | 英 | 成功 | 2025 年人均 GDP：台灣、韓國、日本、中國大陸 |
| R2-8 | Worldometer GDP by country Asia 2025 IMF nominal billions China Japan India Korea Taiwan | extended | 英 | 成功 | 2025 年名目 GDP 總額：中國大陸、日本、印度、韓國、台灣；印度人均 GDP |
| R2-9 | GDP per Capita in Asia (2025) IMF Worldometer Singapore Hong Kong Malaysia … | extended | 英 | 成功 | 2025 年人均 GDP：新加坡、香港、馬來西亞、泰國、印尼、越南、菲律賓 |
| R2-10 | UN World Population Prospects 2024 percentage population aged 65 and over 2025 2035 Asian countries | extended | 英 | 部分成功 | 僅有區域與全球數字，無個別國家的 2025／2035 值 |
| R2-11 | Worldometer Asian countries by population 2025 urban population percentage | extended | 英 | 部分成功 | 都市化率：日本、中國大陸、印尼（2025）；亞洲整體 53.6% |
| R2-12 | share of population aged 65+ 2025 Japan Korea Taiwan Hong Kong Singapore China Thailand … | extended | 英 | 部分成功 | 65+ 占比：6 市場 2024 年值；日本、香港 2025 年值；香港、台灣 2050 預測 |
| R2-13 | 內政部 住宅存量 平均屋齡 30年以上 占比 2025 | extended | 繁中 | **被拒（共用額度再度用盡）** | — |
| R2-14 | 令和5年住宅・土地統計調査 住宅総数 建築の時期 1980年以前 割合 | extended | 日文 | **被拒** | — |
| R2-15 | 주택총조사 2024 노후기간 30년 이상 주택 비율 통계청 | extended | 韓文 | **被拒** | — |

- 第 1 輪：成功 5 次（英 4、繁中 1），被拒 3 次（英 1、印尼文 1、越南文 1）。
- 第 2 輪：成功 12 次（英 10、印尼文 1、越南文 1），被拒 3 次（繁中、日文、韓文）。
- **累計：成功 17 次（在地語言 3 次）、被拒 6 次**。在地語言的住宅搜尋成功 0 次。
- 來源：累計 27 個（TF-01～TF-27），其中在地語言 6 個（繁中 2：TF-05、TF-07；印尼文 3：TF-11～TF-13；越南文 1：TF-17）。詳見第 7 章。
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
| VND 越南盾 | 無資料（年底值 25,485，TF-16） | **26,005.133**（另 26,008，TF-16；26,009，TF-15） | **無資料** | — | — | — | TF-14（主）／TF-15／TF-16 | 中（三源差 <0.02%，但都不是 SBV 原始發布） |
| IDR 印尼盾 | 無資料 | **16,478.44**（另約 16,474～16,475，TF-11） | **無資料** | — | — | — | TF-10（主）／TF-11 | 中（兩源一致，但都不是 BI 原始發布） |
| PHP 菲律賓披索 | 無資料 | **57.509** | **61.44**（**2026 年 5 月**月平均，BSP 參考匯率，經媒體轉引） | — | — | 無資料（2025 年 6 月 56.36、7 月 56.70、5 月 55.625） | TF-10（年）／TF-08（2026-05）／TF-09（2025 月） | 年：中；2026-05：中；2025 月值：低 |

**VND、IDR、PHP 的口徑說明（第 2 輪補充）**：
- **VND**：
  - 26,005.133 是 CEIC 引用的世界銀行系列。世界銀行官方匯率的定義是「國家當局決定之匯率，或合法外匯市場決定之匯率」，屬年平均 — [CEIC Vietnam Exchange Rate against USD](https://www.ceicdata.com/en/indicator/vietnam/exchange-rate-against-usd)。
  - FocusEconomics 列 2025 年平均 26,008、2024 年底 25,485、2025 年底 26,150 — [FocusEconomics Vietnam Exchange Rate](https://www.focus-economics.com/country-indicator/vietnam/exchange-rate/)。
  - exchange-rates.org 列 2025 年平均 26,009，並稱美元對越南盾 2025 年上漲 3.20% — [exchange-rates.org USD-VND 2025](https://www.exchange-rates.org/exchange-rate-history/usd-vnd-2025)。
  - **注意口徑差異**：越南國家銀行（Ngân hàng Nhà nước Việt Nam, SBV）的「中心匯率」（tỷ giá trung tâm）明顯較低。2025-08-22 的年內高點只有 25,298，且是「首次突破 25,000」— [Viện Kinh tế và Tài chính（Bộ Tài chính）](https://nief.mof.gov.vn/kinh-te-xa-hoi/bien-dong-ty-gia-nam-2025-va-du-bao-tinh-hinh-nam-2026-11839.html)（搜尋摘要歸屬於財政部，對應 URL 信心低～中）。中心匯率是官方參考價，市場／銀行間成交價約高 3～7%。**換算 GDP 或市場規模時應採市場平均約 26,005，不要用中心匯率。**
- **IDR**：
  - 16,478.44 是第三方網站以日資料自行重算的 2025 全年平均，並說明 IRS 2025 表不含印尼盾與菲律賓披索 — [exchangerate.dev](https://exchangerate.dev/learn/irs-yearly-average-exchange-rates)。
  - 印尼國立伊斯蘭學院（IAIN Kendari）的年度回顧稱 2025 年 1–5 月平均約 16,474、6–12 月平均約 16,475，與上值一致；但它不是 BI 數據，方法也未說明 — [IAIN Kendari Kaleidoskop 2025](https://iainkendari.ac.id/pojok-rektor/show/kaleidoskop-general-ekonomi-moneter-indonesia-2025)。
  - 同一回顧稱最弱為 2025-04-08 的 17,071，最強為 2025-06-24 的「14,701」。後者與 BI 週報 2025-07-10 收盤 16,215 相差約 10%，**疑為誤植，不採用**。
  - BI 官方週報收盤：2025-11-20 為 16,725 — [BI 21 November 2025](https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_2727925.aspx)；2025-07-10 為 16,215 — [BI 11 Juli 2025](https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_2715025.aspx)。
- **PHP**：
  - 57.509 同樣是 exchangerate.dev 的日資料重算值，並非 BSP 官方年平均（信心中）。
  - 依 BSP 參考匯率，月平均從 2025 年 6 月的 56.36 逐步升到 2026 年 5 月的 61.44，下半年走弱主因是美元轉強 — [Gulf News：Peso's new normal? Dollar could stay above ₱60 — BSP data](https://gulfnews.com/business/markets/pesos-new-normal-dollar-could-stay-above-60-bsp-data-1.500591425)。
  - 2025 年 5 月月平均 55.625（年內最強）、7 月 56.70 — 候選來源 [Gulf News：Peso weakening continues](https://gulfnews.com/business/markets/peso-weakening-continues-should-ofws-remit-or-hold-know-whats-behind-the-trend-1.500215098)（歸屬不確定，信心低）。
  - 2026 年 5 月 61.44 對 2025 年平均 57.509 為 ＋6.8%，也就是披索走弱。
- **混用來源風險**：VND、IDR、PHP 的年平均與 TWD 的 G.5A 年平均出自不同來源。交叉匯率因此可能有小幅口徑誤差（推論，未量化），預期對比較表影響不大，但仍應註明。

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
| VND | 0.001198（1,000 VND＝1.198） | 834.40 | 無資料 | 無資料 |
| IDR | 0.001891（1,000 IDR＝1.891） | 528.73 | 無資料 | 無資料 |
| PHP | 0.5419 | 1.8452 | 無資料（只有 PHP 2026 年 5 月值，與 TWD 8 月值不同期，不應相除） | 無資料 |

（以上由 TF-01、TF-02 數值以 Python 計算，四捨五入；信心同其輸入值：2025 年＝高，2026 年 8 月＝中。VND、IDR、PHP 三列為第 2 輪新增，用 TWD 31.1663（TF-01）分別除以 26,005.133（TF-14）、16,478.44（TF-10）、57.509（TF-10），屬跨來源導出，信心中。）

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
3. **VND、IDR、PHP**：聯準會 G.5／G.5A 不涵蓋這三種貨幣（S1、S3 搜尋結果列出的幣別中不含此三者；推論）。
   - **第 2 輪暫定基準**：VND 26,005.133（TF-14，世界銀行系列）、IDR 16,478.44（TF-10）、PHP 57.509（TF-10）。三者都是第三方年平均，信心中。
   - 正式報告前，建議以**越南國家銀行（SBV）的銀行間或市場年平均**（不要用中心匯率）、**印尼央行（BI）JISDOR 年平均**、**菲律賓央行（BSP）參考匯率年平均**覆核。也可以統一改用 IMF 國際金融統計（IFS）／IMF 月度匯率檔（[IMF Exchange Rate Archives by Month](https://www.imf.org/external/np/fin/data/param_rms_mth.aspx)，僅見於搜尋結果、未讀內容）。
   - 也可以用「名目 GDP 本幣 ÷ 名目 GDP 美元」求出 WEO 隱含的年平均匯率作為後備，但須標示為導出值。
   - 2026 最新值：PHP 用 2026 年 5 月月平均 61.44（TF-08）；**VND 和 IDR 的 2026 值仍無資料**。
4. **敏感度提醒**：INR 在 2025 年平均與 2026 年 8 月間相差 9.5%，JPY 與 CNY 各約 6%。同一數字用不同年度匯率換算，可能讓排名翻轉，所以報告應固定一套基準，並在比較表註明。

---

## 2. 總體表

> 第 2 輪補入的資料如下：
> - **GDP／人均 GDP**：統一用 **IMF 世界經濟展望 2026 年 4 月版（World Economic Outlook, April 2026）**。2025 為 IMF 估計值，2026 為 **IMF 預測值**。
>   - 數值經 Worldometer 轉載。它是聚合網站，但表頭標明「Source: IMF, World Economic Outlook (April 2026)」— [Worldometer GDP per Capita in Asia 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)。
>   - IMF 2026 年 4 月版統計附錄確實存在 — [IMF WEO April 2026 Statistical Appendix](https://www.imf.org/-/media/files/publications/weo/2026/april/english/statsappendix.pdf)（僅見於搜尋結果，未讀數值）。
>   - 搜尋結果出現了 2026 年 1 月更新版與 4 月版，沒有出現 10 月版，所以 **4 月版暫視為最新可用版本**（推論）。
>   - 名目值依市場匯率換成美元，未經購買力調整（TF-18）。
> - **65+ 占比與都市化率**：國家數據不齊，來源混雜，詳見各格。本輪**未能取得聯合國《世界人口展望 2024》（WPP 2024）的個別國家 2025／2035 數值**；WPP 個別國家數值只在其 Excel 檔中（TF-26）。
> - **人口 2025**：本輪未取得 WPP 或國家統計值。下表「IMF 隱含人口」是用「名目 GDP 美元 ÷ 人均 GDP 美元」導出的【示意】值，僅供合理性檢查。

| 市場 | 人口 2025 | 名目 GDP 2025（本幣、USD） | 人均 GDP（USD）：2024／**2025**／2026 預測 | 都市化率 2025 | 65+ 占比：2024（世界銀行系列）／2025／2035 | 來源# |
|---|---|---|---|---|---|---|
| 台灣 | 無資料（IMF 隱含約 23.30 百萬，導出） | 本幣：無資料；USD 920.05 十億 | 無資料／**39,489**／42,103 | 無資料 | 無資料／無資料／無資料（2050 預測 31.7%，TF-25） | TF-20、TF-18、TF-19、TF-25 |
| 日本 | 無資料（IMF 隱含約 123.37 百萬，導出） | 本幣：無資料；USD 4,435.16 十億 | 無資料／**35,973**（另表 35,951）／35,703 | 92.3% | 29.78%／30.0%（信心低，URL 不明確）／無資料 | TF-18、TF-20、TF-19、TF-23、TF-24 |
| 韓國 | 無資料（IMF 隱含約 51.6 百萬，以四捨五入的 GDP 導出，精度低） | 本幣：無資料；USD 約 1.87 兆 | 無資料／**36,227**／37,412 | 無資料 | 19.27%／無資料／無資料 | TF-18、TF-20、TF-19、TF-24 |
| 新加坡 | 無資料 | 無資料 | 無資料／**99,365**（另表 98,814）／107,758 | 無資料 | 13.66%／無資料／無資料 | TF-18、TF-19、TF-24 |
| 香港 | 無資料 | 無資料 | 無資料／**56,893**／59,640 | 無資料 | 22.67%／**23.7%**（聯合國資料，全球第 8）／無資料（2050 預測 46.3%） | TF-18、TF-19、TF-24、TF-25 |
| 中國大陸 | 無資料（IMF 隱含約 1,406.6 百萬，導出） | 本幣：無資料；USD 19,498.04 十億（另一說 19.63 兆，見矛盾表） | 無資料／**13,968**（另表 13,862）／無資料 | 66.34% | 14.67%／無資料／無資料 | TF-18、TF-20、TF-23、TF-24 |
| 馬來西亞 | 無資料 | 無資料 | 無資料／**13,949**／15,085 | 無資料 | 無資料 | TF-18、TF-19 |
| 泰國 | 無資料 | 無資料 | 無資料／**8,057**／8,105 | 無資料 | 15.36%／無資料／無資料 | TF-18、TF-19、TF-24 |
| 越南 | 無資料 | 無資料 | 無資料／**4,829**／5,115 | 無資料 | 無資料 | TF-18、TF-19 |
| 印尼 | 無資料 | 無資料 | 無資料／**5,082**／5,362 | 59.39% | 無資料 | TF-18、TF-19、TF-23 |
| 菲律賓 | 無資料 | 無資料 | 無資料／**4,270**／4,443 | 無資料 | 無資料 | TF-18、TF-19 |
| 印度 | 無資料（IMF 隱含約 1,465 百萬，導出，精度低） | 本幣：無資料；USD 約 3.92 兆（2026 頁另列 3.96 兆） | 無資料／**2,675**／2,813 | 無資料 | 無資料 | TF-20、TF-21、TF-19 |

**補充（第 2 輪）**：
- **人均 GDP 2025 排序**（IMF 2026 年 4 月版，經 Worldometer）：新加坡 99,365 ＞ 香港 56,893 ＞ **台灣 39,489** ＞ 韓國 36,227 ＞ 日本 35,973 ＞ 中國大陸 13,968 ＞ 馬來西亞 13,949 ＞ 泰國 8,057 ＞ 印尼 5,082 ＞ 越南 4,829 ＞ 菲律賓 4,270 ＞ 印度 2,675 — [Worldometer 2025](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal)。台灣在亞洲排第 8，名目人均已高於日本與韓國。
- **2026 年實質 GDP 成長預測**（IMF 2026 年 4 月版，經 Worldometer 2026 表）：台灣 5.18%、日本 0.72%、韓國 1.86%、新加坡 3.51%、香港 2.42%、馬來西亞 4.70%、泰國 1.50%、印尼 4.95%、越南 7.10%、菲律賓 4.07%、印度 6.48%。中國大陸未列 — TF-19（預測值，信心中）。
- **購買力平價人均 GDP 2025**（國際元，供參考）：新加坡 164,318、台灣 90,233、香港 80,323、韓國 65,405、日本 56,854、馬來西亞 44,119、中國大陸 29,352、泰國 26,260、越南 17,971、印尼 17,746、菲律賓 12,877 — [Worldometer PPP 2025](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=ppp)（TF-28；印度無資料）。
- **區域背景**：
  - 亞洲整體 2025 年都市化率 53.6%（人口 4,835,320,060）— [Worldometer Asia Population](https://www.worldometers.info/world-population/asia-population/)（TF-27）。
  - 全球 65+ 占比從 1974 年的 5.5% 升到 2024 年的 10.3%，預計 2074 年達 20.7%。亞洲預計在 2050 年代跨過 20% 的「超高齡」門檻。2054 年香港與韓國將是 65+ 占比最高的地區之一 — [UN WPP 2024 Summary of Results](https://population.un.org/wpp/assets/Files/WPP2024_Summary-of-Results.pdf)（TF-26）。
- **台灣在 IMF 資料中的名稱**：Worldometer 表上顯示「Taiwan」。IMF 原始資料庫是否列為「Taiwan Province of China」，**本輪仍未以搜尋驗證**（信心低）。報告引用時應以 IMF 原表名稱為準並加註。

**下一輪的版本建議**：
- GDP／人均 GDP：第 2 輪已統一採 **IMF WEO 2026 年 4 月版**。IMF 的 10 月版通常在 10 月中旬年會期間發布，若在報告定稿前出版，應**整批**替換，不要混用兩版。2026 年數值一律標「IMF 預測」。
- 仍需補：人均 GDP 2024、名目 GDP 本幣值（12 市場）、名目 GDP 美元值（新加坡、香港、馬來西亞、泰國、越南、印尼、菲律賓）。建議直接查 IMF WEO 資料庫（NGDPD、NGDPDPC、NGDP），以取代 Worldometer 轉載。
- 台灣在 IMF WEO 及聯合國《世界人口展望》（WPP）中，**慣例列為「Taiwan Province of China」**。這是已知慣例，但仍未以搜尋驗證，信心：低。報告中應保留原名稱並加註。
- 人口、65+ 占比 2025／2035、都市化率：建議統一用 **UN WPP 2024 中推計**，以及**聯合國《世界都市化展望》（WUP）**。另並列國家推計：台灣國發會、日本國立社會保障・人口問題研究所、韓國統計廳（통계청）。若國家推計與 WPP 的差距 >30%，列入矛盾表。

---

## 3. 住宅表

> 本章 **仍全部無資料**。第 2 輪原本要查台灣、日本、韓國的住宅屋齡（R2-13～R2-15），但都因共用搜尋額度用盡被拒；優先序 5–7（自有率、房貸利率、BIS 房價）因此也未能執行。下表列出每格應取用的**目標原始資料**（原文名稱），以免下一輪混用不可比口徑。
>
> **協調者告知、其他研究代理已取得的數據**（本筆記**未獨立驗證**，不列入本筆記 CSV；引用時請用原代理的來源與 URL）：
> - 新加坡 HDB 轉售成交 26,169 戶（2025）
> - 泰國 房產過戶 316,214 戶（2025），其中中古占 64%
> - 馬來西亞 住宅交易 256,512 宗（2025）
> - 日本 新設住宅着工 740,667 戶（2025）
> - 中國大陸 二手房占比 46%（2025）

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
