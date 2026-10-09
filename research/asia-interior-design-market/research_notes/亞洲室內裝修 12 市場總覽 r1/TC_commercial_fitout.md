# 跨國主題 C：商業空間（辦公／飯店／零售／餐飲）裝修需求與城市級裝修成本基準 — 12 市場（r1 獨立三角驗證）

> 研究日期：2026-10-09｜研究者：子代理（TC）｜語言：繁體中文（台灣用語），機構與公司原名置於括號
> 獨立性：未開啟 `04-research-notes/`、`05-report/` 任何檔案；未參考其他 AI 產出。
> 幣別／單位：**一律照原文記錄，未做匯率或面積換算**（由中央統一處理）。第 6 章矛盾診斷中為判斷差距大小所做的「面積」換算（1 m² = 10.7639 sq ft）僅用於診斷，不作為紀錄值。
> 讀取方式：WebFetch／curl 受組織網路政策封鎖，本輪所有來源皆為「搜尋結果內容」（搜尋引擎回傳的摘錄與摘要），**未開啟任何原始 PDF 全文**。

---

## 0. 搜尋紀錄摘要

**重要限制（請報告撰寫者務必知悉）**：本輪在完成 12 次搜尋後，系統回報「本回合 WebSearch 額度（200 次，所有子代理共用）已用盡」，其後 3 次搜尋（1 韓文、2 日文）未執行。因此**未達**委託要求的「≥25 次搜尋、≥6 次在地語言」。依系統指示未以其他方式繞過。以下缺口（日本／中國上市公司營收、飯店管線、各市場辦公空置率等）主要源於此限制，而非「資料不存在」。

| # | 查詢字串 | 語言 | 模式 | 結果 |
|---|---|---|---|---|
| Q1 | Cushman & Wakefield Asia Pacific Office Fit Out Cost Guide 2025 | 英 | extended | 成功：2025 版區間（東京 195／雅加達 58 USD psf）、2026 版 33 城市 |
| Q2 | JLL fit-out cost guide Asia Pacific 2025 per square foot | 英 | extended | 成功：JLL 2025／2026 亞太平均 USD/m² |
| Q3 | AECOM Asia Construction Cost Handbook 2025 fit-out office hotel per m2 | 英 | extended | **未找到 AECOM 手冊**；帶出 T&T 2025 東京／香港高規格數字、Arcadis 中港手冊（無裝修單價摘錄） |
| Q4 | Cushman Wakefield fit out cost guide 2026 Tokyo Singapore Hong Kong per square foot USD | 英 | extended | 成功：東京 215、香港 160、新加坡 140、台北 145 |
| Q5 | Turner & Townsend office fit-out cost guide 2025 Singapore Shanghai Mumbai per m2 | 英 | extended | 部分：T&T 方法論、班加羅爾低規格 531 USD/m²；新／滬／孟買城市數字未取得 |
| Q6 | Cushman Wakefield fit out cost India Mumbai Bengaluru 2026 per sq ft | 英 | standard | 成功：印度 65–73 USD psf、孟買 INR 6,567 psf；Knight Frank 449 USD/m² |
| Q7 | Cushman Wakefield 2026 fit out cost Taipei US$145 per square foot | 英 | extended | 成功：台北 110→145；2019 年 70 |
| Q8 | Cushman Wakefield fit out cost guide Kuala Lumpur Bangkok Manila Ho Chi Minh Jakarta 2026 | 英 | extended | 成功：馬尼拉 105、曼谷 91、吉隆坡 80、胡志明市 61；復原費 |
| Q9 | 戴德梁行 办公楼装修成本指南 2026 上海 北京 深圳 每平方英尺 | 簡中 | extended | 部分：中文版發布、滬京領跑內地（無數字）；本地裝修公司行情（低信心） |
| Q10 | 쿠시먼앤드웨이크필드 오피스 인테리어 비용 가이드 2026 서울 평당 | 韓 | extended | 部分：C&W 韓國 2026 版存在、90% 承包商預期漲價；第三方每坪行情（低信心） |
| Q11 | Cushman Wakefield 2025 fit out cost guide Seoul Shanghai Beijing Kuala Lumpur Bangkok USD psf | 英 | extended | 部分：2026 表格（首爾約 130、上海約 96、北京約 95，表格擷取錯亂，低信心） |
| Q12 | Turner & Townsend fit-out cost guide 2026 Asia-Pacific Tokyo Hong Kong Singapore high specification US$ per m2 | 英 | extended | 部分：T&T 2026 香港 HK$31,231/m²；東京／新加坡未取得 |
| Q13 | 쿠시먼 2025 오피스 인테리어 비용 보고서 서울 원 평당 핏아웃 | 韓 | standard | **未執行（額度用盡）** |
| Q14 | 乃村工藝社 2026年2月期 決算 売上高 営業利益 | 日 | standard | **未執行（額度用盡）** |
| Q15 | 丹青社 2026年1月期 決算 売上高 営業利益率 | 日 | standard | **未執行（額度用盡）** |

統計：嘗試 15 次；成功 12 次（在地語言成功 2 次：簡中 1、韓文 1）；被擋 3 次（韓 1、日 2）。引用來源 54 條（TC-01～TC-54），其中在地語言 13 條（簡中 7、韓文 6）；日文來源 0 條。

---

## 1. 關鍵結論（每點含數字＋來源#）

1. **辦公 fit-out 成本亞太最高仍是東京**：Cushman & Wakefield（戴德梁行，C&W）《2026 亞太辦公室裝修成本指南》（33 城市、價格基準 2025 年 12 月）東京 **USD 215／sq ft**（2025 版為 195），日本與澳洲為最高成本市場，印度最低 [TC-04][TC-07][TC-01]。【實際】信心：高
2. **台北是 2026 版漲幅最大城市之一**：台北由 **USD 110／sq ft（2025）升至 USD 145／sq ft（2026）**，約 +32%，已高於新加坡（140）、低於香港（160）[TC-04][TC-05][TC-19]。漲幅原因（實際工料上漲 vs 匯率 vs 計價口徑調整）搜尋結果未說明，見矛盾表。【實際】信心：高（數字）／低（原因）
3. **大中華區**：香港 **USD 160／sq ft** 為大中華區最貴、亞太第 8；上海、北京領跑內地（擷取表格中約 96、95，信心低），廣州、深圳「成本表現穩健」[TC-04][TC-19][TC-02]。
4. **東南亞是低價帶**：2026 版馬尼拉 **105**、曼谷 **91**、吉隆坡 **80**、胡志明市 **61**（USD／sq ft）[TC-06]；雅加達 2025 版 **58**，為 2025 版全區最低 [TC-11][TC-12]。
5. **印度最具成本競爭力**：C&W 2026 印度主要城市 **USD 65–73／sq ft**，孟買最高約 **USD 73（約 INR 6,567）／sq ft**，德里首都圈、班加羅爾、海德拉巴、清奈、浦那集中在 **USD 65–69**（情境：協作式混合辦公）[TC-07][TC-08][TC-09]；Knight Frank 2026 中規格平均 **USD 449／m²**（班加羅爾、孟買、德里首都圈）[TC-33]。
6. **等級／口徑差距可達 2 倍以上**：Turner & Townsend（T&T）2025 東京高規格 **USD 4,619／m²**、香港頂級 **USD 4,575／m²**、班加羅爾低規格 **USD 531／m²** [TC-27]；T&T 含 CAT A＋CAT B 與家具、AV、專業費 [TC-28]，與 C&W 平均值不可直接比（第 6 章）。
7. **JLL 區域平均**：亞太辦公 fit-out 平均 2025 年 **USD 1,460／m²**（全球指南）或 **USD 1,524／m²**（亞太指南，中等品質、適中風格），2026 年 **USD 1,550／m²**，為全球成本最低區域（全球平均 2025 年 USD 1,830–1,949／m²、2026 年 USD 2,150／m²）[TC-22][TC-23][TC-24][TC-26]。
8. **成本動能溫和上行**：JLL 2026 亞太以當地幣計年增 **2–5%** [TC-24]；T&T 2026 全球年增約 **3%** [TC-30]；C&W 2026 承包商調查 **70%** 預期 2026 市況改善 [TC-17]；C&W 韓國版 **90%** 受訪業者預期未來 6 個月小幅漲價（人工＋關稅）[TC-35]。
9. **飯店、零售、餐飲 fit-out 單價、AECOM／Arcadis／RLB 城市費率、主要裝修業者營收** 本輪皆**無資料**（搜尋額度用盡；AECOM 手冊於 Q3 未被搜尋引擎索引到）。C&W 的零售 fit-out 成本指南僅見美國版 [TC-47]。

---

## 2. 城市級裝修成本基準總表

> 欄位：城市｜類型｜等級／情境｜數值｜幣別與單位（照原文）｜版本年｜來源#｜範圍說明｜信心｜標示
> C&W 2026 版範圍：成本拆分涵蓋家具、機電、營建工程、AV／IT 與雜項 [TC-19][TC-01]；印度頁明示情境為「協作式混合辦公（collaborative hybrid workplace）」[TC-09]；價格基準 2025 年 12 月 [TC-01][TC-19]。**C&W 美洲 2026 版明示其營建數字「不含」弱電、AV、保全、FF&E 與軟成本** [TC-54]；亞太版另有「all-in」拆分（專業費、家具、機電、營建、科技、復原）[TC-01]，但城市標題值（如東京 215）究竟是 all-in 或僅營建**未確認**——報告撰寫者引用時請註明此不確定性。

### 2.1 辦公（Office）— 城市級

| 城市 | 類型 | 等級／情境 | 數值 | 幣別與單位 | 版本年 | 來源# | 範圍說明 | 信心 | 標示 |
|---|---|---|---|---|---|---|---|---|---|
| 台北 Taipei | 辦公 | C&W 平均 | 145 | USD／sq ft | 2026 版（基準 2025-12） | TC-04, TC-05, TC-19 | C&W 2026 亞太版城市平均 | 高 | 【實際】 |
| 台北 Taipei | 辦公 | C&W 平均 | 110 | USD／sq ft | 2025 版 | TC-04, TC-05 | 同上，前一版 | 高 | 【實際】 |
| 台北 Taipei | 辦公 | C&W 調查 | 70 | USD／sq ft | 2019 | TC-15 | 2019 年 C&W 調查（Taipei Times 報導）；口徑可能與 2026 不同 | 中 | 【示意】 |
| 東京 Tokyo | 辦公 | C&W 平均 | 215 | USD／sq ft | 2026 版 | TC-04, TC-07 | C&W 2026；亞太最高 | 高 | 【實際】 |
| 東京 Tokyo | 辦公 | C&W 平均 | 195 | USD／sq ft | 2025 版 | TC-11, TC-12, TC-04 | C&W 2025；2025 版全區最高 | 高 | 【實際】 |
| 東京 Tokyo | 辦公 | T&T 高規格（high specification） | 4,619 | USD／m² | 2025 版（基準 2025 Q1） | TC-27 | T&T：CAT A＋CAT B，含保全、結構化布線、活動家具、AV、專業費；約 4,215 m² 兩層試配 | 中 | 【示意】 |
| 大阪 Osaka | 辦公 | — | 無資料 | — | — | — | Q1/Q4/Q11 未見大阪數值（C&W 稱「日本城市」整體最高 [TC-11]） | — | — |
| 首爾 Seoul | 辦公 | C&W 平均 | 約 130 | USD／sq ft | 2026 版 | TC-02 | 表格擷取錯亂，欄位未確認 | 低 | 【示意】 |
| 首爾 Seoul | 辦公 | 第三方：基本／中階／高階 | 120–160／160–200／200 以上 | 萬韓元（만원）／坪 | 2026 | TC-36 | 平台業者行情文章，含稅與否未明 | 低 | 【示意】 |
| 首爾 Seoul | 辦公 | 第三方：輕度／中度改裝／含全機電 | 80–150／150–220／220–350 | 萬韓元／坪 | 2026 | TC-37 | 不含 VAT、家具、IT、設計費 | 低 | 【示意】 |
| 首爾 Seoul | 辦公 | 第三方：全區間 | 80–200 | 萬韓元／坪 | 2026 | TC-38 | 行情文章，口徑未明 | 低 | 【示意】 |
| 新加坡 Singapore | 辦公 | C&W 平均 | 140 | USD／sq ft | 2026 版 | TC-04, TC-07 | C&W 2026；與 2025 版「大致持平」 | 高 | 【實際】 |
| 新加坡 Singapore | 辦公 | C&W 表格列（欄位未確認） | 102／140／212／63 | USD／sq ft | 2026 版 | TC-01 | 原表列「SINGAPORE 102 140 212 63」，推測可能為低／平均／高／復原，但**未確認** | 低 | 【示意】 |
| 香港 Hong Kong | 辦公 | C&W 平均 | 160 | USD／sq ft | 2026 版 | TC-04 | 大中華區最貴、亞太第 8；與 2025 大致持平 | 高 | 【實際】 |
| 香港 Hong Kong | 辦公 | T&T 頂級（premium） | 4,575 | USD／m² | 2025 版 | TC-27 | T&T 口徑同上 | 中 | 【示意】 |
| 香港 Hong Kong | 辦公 | T&T 頂級（premium）平均 | 31,231 | HKD／m² | 2026 版 | TC-32 | T&T 2026；與 Charlotte、Melbourne 等次級市場同級（URL 對應由搜尋摘要推定） | 中 | 【示意】 |
| 上海 Shanghai | 辦公 | C&W 平均 | 約 96 | USD／sq ft | 2026 版 | TC-02 | 表格擷取錯亂；C&W 中文稿確認「滬京領跑內地」[TC-19] | 低 | 【示意】 |
| 上海 Shanghai | 辦公 | 本地裝修公司全包 | 800–1,500 | RMB／m² | 2026 | TC-39 | 裝修公司行銷文章，口徑不明 | 低 | 【示意】 |
| 北京 Beijing | 辦公 | C&W 平均 | 約 95 | USD／sq ft | 2026 版 | TC-02 | 表格擷取錯亂 | 低 | 【示意】 |
| 北京 Beijing | 辦公 | 本地裝修公司：主流／高端 | 1,000–1,200／1,200–1,800 | RMB／m² | 2026 | TC-40 | 裝修公司行銷文章 | 低 | 【示意】 |
| 深圳 Shenzhen | 辦公 | — | 無資料 | — | — | TC-19 | 僅文字「廣深成本表現穩健」，無數值 | — | — |
| 吉隆坡 Kuala Lumpur | 辦公 | C&W 平均 | 80 | USD／sq ft | 2026 版 | TC-06 | C&W 泰國頁 2026 城市排名 | 中 | 【示意】 |
| 吉隆坡 Kuala Lumpur | 辦公 | C&W 復原（reinstatement）平均 | 約 10 | USD／sq ft | 2026 版 | TC-01 | 表格擷取錯亂 | 低 | 【示意】 |
| 曼谷 Bangkok | 辦公 | C&W 平均 | 91 | USD／sq ft | 2026 版 | TC-06 | C&W 泰國頁 | 中 | 【示意】 |
| 胡志明市 Ho Chi Minh City | 辦公 | C&W 平均 | 61 | USD／sq ft | 2026 版（年份標示不明確） | TC-06 | 搜尋摘要提醒此值未明確標為 2026 | 中 | 【示意】 |
| 河內 Hanoi | 辦公 | — | 無資料 | — | — | — | 未見 | — | — |
| 雅加達 Jakarta | 辦公 | C&W 平均 | 58 | USD／sq ft | 2025 版 | TC-11, TC-12 | 2025 版全區最低 | 高 | 【實際】 |
| 雅加達 Jakarta | 辦公 | C&W 復原平均 | 約 10 | USD／sq ft | 2026 版 | TC-01 | 表格擷取錯亂 | 低 | 【示意】 |
| 馬尼拉 Manila | 辦公 | C&W 平均 | 105 | USD／sq ft | 2026 版 | TC-06 | 東南亞僅次於新加坡 | 中 | 【示意】 |
| 馬尼拉 Manila | 辦公 | C&W 復原：平均（區間） | 約 20（15–25） | USD／sq ft | 2026 版 | TC-01 | 表格擷取錯亂 | 低 | 【示意】 |
| 孟買 Mumbai | 辦公 | C&W 協作式混合辦公 | 約 73 | USD／sq ft | 2026 版 | TC-07, TC-08, TC-09 | 印度最高 | 高 | 【實際】 |
| 孟買 Mumbai | 辦公 | 同上 | 約 6,567 | INR／sq ft | 2026 版 | TC-09 | C&W 印度頁 | 中 | 【示意】 |
| 孟買 Mumbai | 辦公 | C&W 前一版 | 73（6,303） | USD／sq ft（INR／sq ft） | 2024（摘要標示「前一版」，版本年不確定） | TC-10 | NAREDCO 轉載 | 中 | 【示意】 |
| 德里首都圈 Delhi NCR | 辦公 | C&W 協作式混合辦公 | 65–69（區間，與班加羅爾等合併） | USD／sq ft | 2026 版 | TC-07, TC-08 | 未單列 | 中 | 【示意】 |
| 德里首都圈 Delhi NCR | 辦公 | C&W 前一版 | 69 | USD／sq ft | 2024（同上） | TC-10 | — | 中 | 【示意】 |
| 班加羅爾 Bengaluru | 辦公 | C&W 協作式混合辦公 | 65–69（區間） | USD／sq ft | 2026 版 | TC-07, TC-08 | 未單列 | 中 | 【示意】 |
| 班加羅爾 Bengaluru | 辦公 | C&W 前一版 | 67（5,786） | USD／sq ft（INR／sq ft） | 2024（同上） | TC-10 | — | 中 | 【示意】 |
| 班加羅爾 Bangalore | 辦公 | T&T 低規格（low specification） | 531 | USD／m² | 2025 版 | TC-27 | T&T 口徑 | 中 | 【示意】 |
| 印度三城（班加羅爾、孟買、德里首都圈）平均 | 辦公 | Knight Frank 中規格（mid-spec） | 449 | USD／m² | 2026 | TC-33 | Knight Frank 方法，與 C&W 不同 | 中 | 【示意】 |

### 2.2 區域平均（非城市級，作為校準錨點）

| 範圍 | 指標 | 數值 | 單位 | 版本年 | 來源# | 範圍說明 | 信心 |
|---|---|---|---|---|---|---|---|
| 亞太 | JLL 辦公 fit-out 平均 | 1,460（135.66） | USD／m²（USD／sq ft） | 2025（全球指南，2025-04） | TC-22, TC-21 | JLL Global Office Fit-Out Cost Guide 2025 | 中 |
| 全球 | JLL 平均 | 1,830（170） | USD／m²（USD／sq ft） | 2025 | TC-22, TC-21 | 同上 | 中 |
| 北美 | JLL 平均 | 3,070（285.29） | USD／m²（USD／sq ft） | 2025 | TC-22 | 最高成本區域 | 中 |
| 亞太 | JLL「適中風格、中等品質」辦公平均 | 1,524 | USD／m² | 2025（基準 2025 Q1） | TC-23 | JLL APAC Fit-Out Cost Guide 2025；JLL 提醒貿易環境變動可能使報價偏離 | 中 |
| 全球 | JLL 同口徑平均 | 1,949 | USD／m² | 2025 Q1 | TC-23 | 同上 | 中 |
| 亞太 | JLL 平均 | 1,550 | USD／m² | 2026 | TC-24, TC-25 | 27 城市；競爭性招標使行情大致持平；當地幣年增 2–5% | 中 |
| 全球 | JLL 平均 | 2,150 | USD／m² | 2026 | TC-26 | 仲量聯行中文版 | 中 |
| 亞太 | JLL 復原（reinstatement）平均 | 235（區間：大中華 245 至東北亞 425） | USD／m² | 2026 | TC-25 | **內部不一致**：平均值低於所列區間下限，疑為摘要錯誤 | 低 |
| 全球前 6 大市場 | T&T 高規格平均 | >5,000 | USD／m² | 2026（58 市場） | TC-30 | 固定匯率比較 | 中 |
| 全球 | T&T 年度成本漲幅 | 約 3 | % | 2026 | TC-30 | — | 中 |

### 2.3 飯店／零售／餐飲（Hotel／Retail／F&B）

| 城市 | 類型 | 數值 | 說明 |
|---|---|---|---|
| 全部 18 城市 | 飯店 | **無資料** | Q3 嘗試 AECOM 手冊未果；Arcadis《2025 中國與香港建築成本手冊》[TC-34] 有飯店章節，但摘錄僅見飯店 CFA:GFA 比 1.30–1.45:1 與通風率，無裝修單價 |
| 全部 18 城市 | 零售 | **無資料** | C&W 零售 fit-out 成本指南僅見美國版（2026 U.S. Retail Fit Out Cost Guide）[TC-47] |
| 全部 18 城市 | 餐飲 | **無資料** | 未搜尋到（額度用盡） |

---

## 3. 各市場商業空間需求脈絡（2024–2026）

> 本章因搜尋額度用盡，絕大多數市場的辦公空置率、新供給、飯店管線、零售／餐飲開店數為**無資料**。以下僅列搜尋結果中可查證的內容。

### 3.1 區域整體
- C&W 2026 新聞稿標題為「亞太辦公需求走強，承包商信心上升」（Contractor Confidence Rises Amid Strengthening Office Demand Across Asia Pacific），新加坡、吉隆坡、韓國、大中華區均發布同稿 [TC-04][TC-05][TC-17][TC-18]；承包商調查中 **70%** 受訪者預期 2026 年市況改善 [TC-17]。信心：中（質化＋單一調查數字）
- C&W 2026：共識為未來 6 個月工料成本僅「小幅」上升 [TC-01]；2025 版標題為「最壞的價格壓力已過、承包商情緒大致正面」[TC-13]；2024 版標題為「亞太辦公 fit-out 成本續漲但漲速明顯放緩」[TC-41]。→ 2024–2026 為「漲幅收斂」週期。
- JLL：辦公室重回商用不動產核心角色、但代價升高（McMorrow 報導 JLL 全球指南）[TC-52]；JLL 東南亞稿標題指出亞太「永續 fit-out 需求成長」[TC-53]。信心：低（僅標題）
- 混合辦公影響：C&W 印度頁之成本情境即設定為「協作式混合辦公」[TC-09]，顯示主流顧問已以混合辦公配置作為標準試配；但 **fit-out 量（m²）受混合辦公影響之量化數字：無資料**。

### 3.2 分市場

| 市場 | 辦公（空置／去化／新供給） | 飯店管線 | 零售／餐飲 | 資料中心／半導體外溢 | 來源 |
|---|---|---|---|---|---|
| 台灣 | 無資料；僅知 C&W 2026 台北 fit-out 成本年增最大之一（110→145 USD psf）[TC-04] | 無資料 | 無資料 | 無資料 | TC-04 |
| 日本 | 無資料；T&T 指東京承包商競爭有限推高成本 [TC-27] | 無資料 | 無資料 | 無資料 | TC-27 |
| 韓國 | C&W 韓國 2026 辦公市場研討會主題為「不確定性下的最適租賃策略」[TC-43]；C&W 2026 首爾租戶產業變化報告存在 [TC-48]，無數字 | 無資料 | 無資料 | 無資料 | TC-43, TC-48 |
| 新加坡 | T&T：2024 Q4 辦公去化與入住率改善，利於 2025 fit-out 市場 [TC-29] | 無資料 | 無資料 | 無資料 | TC-29 |
| 香港 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 中國大陸 | 戴德梁行稱下半年一線城市甲級寫字樓租金或繼續下降（**年份不明**）[TC-46]；C&W 2026 上半年深圳寫字樓及零售報告存在 [TC-45]，摘要無數字 | 無資料 | 無資料 | 無資料 | TC-46, TC-45 |
| 馬來西亞 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 泰國 | C&W：曼谷仍為東南亞最成熟辦公市場之一，fit-out 成本在亞太相對具競爭力 [TC-06] | 無資料 | 無資料 | 無資料 | TC-06 |
| 越南 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 印尼 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 菲律賓 | 無資料 | 無資料 | 無資料 | 無資料 | — |
| 印度 | C&W 2025-09 新聞標題「印度成為全球彈性辦公市場成熟度領先者」[TC-44]（僅標題）；T&T 指班加羅爾為印度辦公去化龍頭之一 [TC-27]（摘要語句歧義，未取占比） | 無資料 | 無資料 | 無資料 | TC-44, TC-27 |

- 資料中心：《Asia Pacific Data Construction Cost Guide 2025》存在（SlideShare 轉載，出版者未在搜尋結果中確認）[TC-50]，但搜尋結果無城市數字。信心：低

---

## 4. 主要玩家表

> **本輪無任何一家裝修承包商／設計施工公司的營收或利潤率被搜尋結果證實**（日文、中文上市公司財報搜尋未執行）。以下保留委託書指定的公司名稱作為待查清單，不填任何數字。

| 公司 | 市場 | 營收 | 利潤率 | 業務 | 年度 | 來源# |
|---|---|---|---|---|---|---|
| 乃村工藝社（Nomura Co., Ltd.） | 日本 | 無資料 | 無資料 | 商業空間展示、內裝（待查） | — | —（Q14 未執行） |
| 丹青社（Tanseisha） | 日本 | 無資料 | 無資料 | 商業／文化空間（待查） | — | —（Q15 未執行） |
| スペース（Space Co., Ltd.） | 日本 | 無資料 | 無資料 | 商業設施內裝（待查） | — | — |
| 船場（Semba） | 日本 | 無資料 | 無資料 | 商業設施內裝（待查） | — | — |
| 金螳螂（Suzhou Gold Mantis） | 中國大陸 | 無資料 | 無資料 | 公裝／建築裝飾（待查） | — | — |
| 亚厦股份（Zhejiang Yasha） | 中國大陸 | 無資料 | 無資料 | 公裝／建築裝飾（待查） | — | — |
| ISG | 亞太 | 無資料 | 無資料 | fit-out 承包（待查） | — | — |
| Space Matrix | 亞太／印度 | 無資料 | 無資料 | 設計施工（待查） | — | — |
| Unispace | 亞太 | 無資料 | 無資料 | 設計施工（待查） | — | — |
| Gammon（金門建築） | 香港／新加坡 | 無資料 | 無資料 | 營建與內裝（待查） | — | — |
| 台灣商空設計／施工業者 | 台灣 | 無資料 | 無資料 | — | — | — |
| 韓國、東南亞、印度在地業者 | 各市場 | 無資料 | 無資料 | — | — | — |

- 可確認的「成本基準發布者」（同時也是專案管理／成本顧問服務商）：Cushman & Wakefield（33 城市，2026）[TC-01]、JLL（27 城市，2026）[TC-24]、Turner & Townsend（58 市場，2026）[TC-30]、Knight Frank（印度，2026）[TC-33]、Arcadis（中國與香港成本手冊 2025）[TC-34]。AECOM、Rider Levett Bucknall、Linesight、Currie & Brown：**本輪未取得任何搜尋結果**。

### 設計費基準（% 或每 m²）
- **無資料**。唯一相關資訊：T&T 2025 的成本口徑將「專業費（professional fees）」列入業主直接項目 [TC-28]，C&W 2026 亞太版的「all-in」成本拆分亦包含專業費 [TC-01 之搜尋摘要]，但兩者皆未在搜尋結果揭露專業費占比。

---

## 5. 對璞石（宜蘭＋台北信義；裝修＋不動產＋家居零售）的啟示

> 以下為依第 1–2 章已引用數字所做之推論，非新事實。

1. **台北商辦 fit-out 單價已站上亞太中高段**：C&W 2026 台北 145 USD psf，高於新加坡 140、首爾約 130（低信心），僅低於東京 215 與香港 160 [TC-04][TC-02]。推論：台北信義區商辦案的「每坪工程款」已與新加坡同級，**以「台灣工程比較便宜」作為出海新加坡的價格優勢論述不成立**；出海應以設計品質、華語服務、跟隨台商客戶為賣點，而非價格。
2. **台北 +32% 的年增需拆解**：若主要來自工料上漲，璞石在台北的商空案毛利可能受擠壓（固定總價合約風險）；若來自 C&W 口徑或匯率變化，則對實際報價影響有限。建議以新台幣報價紀錄自行驗證（缺口表 G-03）。
3. **東南亞／印度是「低單價、高量」市場**：雅加達 58、胡志明市 61、吉隆坡 80、曼谷 91、印度 65–73 USD psf [TC-11][TC-06][TC-07]，約為台北的 40–73%。推論：同樣面積的案子在這些城市營收規模較小，若無在地低成本工班與供應鏈，台灣團隊外派成本難以吸收；較可行的是「設計輸出＋在地施工夥伴」或專攻台商廠辦／高端零售。
4. **等級差距大於城市差距**：T&T 高規格東京 4,619 USD/m²、香港 4,575 USD/m² vs 班加羅爾低規格 531 USD/m² [TC-27]。推論：璞石若定位中高端商空（飯店大廳、精品零售、總部辦公），應以「高規格」基準而非城市平均值評估標的市場的單案規模。
5. **成本走勢溫和**：JLL 亞太年增 2–5%（當地幣）[TC-24]、T&T 全球約 3% [TC-30]、70% 承包商看好 2026 [TC-17]。推論：2026–2027 的報價可按 3–5% 年調幅做敏感度分析；韓國受人工與關稅推升 [TC-35]，與台灣同屬「人工成本驅動」型市場，值得參考其轉嫁策略。
6. **與不動產業務的連動**：C&W／JLL 的「復原（reinstatement）」成本（如吉隆坡、雅加達約 10 USD psf、馬尼拉約 20 USD psf，低信心）[TC-01] 提示：商辦租約到期的拆除復原是另一個可承接的服務品項；璞石若持有或代管信義區商辦，可把「進場 fit-out＋退場復原」打包。
7. **資料不足的部分不可下結論**：飯店、零售、餐飲 fit-out 單價、各市場商空主要玩家營收與毛利、設計費占比本輪皆無資料，跨境評分不宜只依本筆記。

---

## 6. 矛盾表與缺口表

### 6.1 矛盾表（差異 >30%；不取平均）

> 診斷用面積換算：1 m² = 10.7639 sq ft，僅用於判斷差距，不作紀錄值。幣別不同者不做換算比較。

| # | 指標 | 來源 1 | 來源 2 | 差異 | 差異原因診斷 | 裁決 |
|---|---|---|---|---|---|---|
| C-01 | 東京辦公 fit-out | C&W 2025：195 USD/sq ft [TC-11]（診斷換算約 2,099 USD/m²） | T&T 2025 高規格：4,619 USD/m² [TC-27] | T&T 約為 C&W 的 2.2 倍 | **等級**（T&T 高規格 vs C&W 平均）＋**範圍**（T&T 含 CAT A＋CAT B、活動家具、AV、專業費 [TC-28]；C&W 範圍含家具、機電、營建、AV/IT [TC-19] 但未確認是否含專業費）＋試配面積不同 | 兩者並列；城市比較用 C&W，高端定位估算用 T&T 高規格 |
| C-02 | 香港辦公 fit-out | C&W 2026：160 USD/sq ft [TC-04]（診斷換算約 1,722 USD/m²） | T&T 2025 頂級：4,575 USD/m² [TC-27] | T&T 約為 C&W 的 2.7 倍 | 同 C-01（等級＋範圍）；另版本年不同 | 並列；不可平均 |
| C-03 | 香港 T&T 自身跨年 | T&T 2025 頂級：4,575 **USD**/m² [TC-27] | T&T 2026 頂級：31,231 **HKD**/m² [TC-32] | 幣別不同，不在此換算 | 計價幣別改變；須中央以統一匯率換算後再判斷是否跨年下修 | 待中央換算後判定 |
| C-04 | 孟買辦公 fit-out | C&W 2026：約 73 USD/sq ft [TC-07] | Knight Frank 2026 三城中規格平均：449 USD/m² [TC-33]（診斷換算約 41.7 USD/sq ft） | C&W 約為 KF 的 1.75 倍 | **城市**（KF 為三城平均，孟買為三城最貴）＋**等級**（KF 中規格）＋**範圍**（KF 是否含家具／AV 未知；C&W 為協作式混合辦公情境含家具、AV/IT） | 並列 |
| C-05 | 班加羅爾辦公 fit-out | C&W 2026：65–69 USD/sq ft [TC-07] | T&T 2025 低規格：531 USD/m² [TC-27]（診斷換算約 49.3 USD/sq ft） | C&W 高約 32–40% | **等級**（T&T 低規格）＋版本年 | 並列；T&T 低規格可作為印度「最低門檻」 |
| C-06 | 台北辦公 fit-out（同一出版者跨年） | C&W 2025：110 USD/sq ft [TC-04] | C&W 2026：145 USD/sq ft [TC-04] | +31.8% | 非來源衝突，而是單年跳升；可能原因：(a) 實際工料上漲、(b) 新台幣兌美元匯率變動、(c) 2026 版擴充「all-in」拆分導致口徑變動——搜尋結果**未提供當地幣變動**，無法裁定 | 兩值並列；標註「原因未明」 |
| C-07 | 台北長期 | C&W 2019：70 USD/sq ft [TC-15] | C&W 2026：145 USD/sq ft [TC-04] | 約 2.07 倍 | 7 年間方法論可能變動（2019 版範圍未知）＋通膨＋匯率 | 2019 值僅作歷史參考，不與 2026 直接比 |
| C-08 | 首爾辦公 fit-out（第三方之間） | spacelogin 基本型 120–160 萬韓元／坪 [TC-36] | interiorcnote 輕度 80–150 萬韓元／坪（不含 VAT、家具、IT、設計費）[TC-37] | 下限差 50% | **範圍**（含稅與否、家具與設計費）＋行銷文章口徑不一 | 皆低信心；以 C&W 韓國原版補正（G-02） |
| C-09 | JLL 亞太復原成本 | 平均 235 USD/m² [TC-25] | 區間下限 245（大中華）、上限 425（東北亞）[TC-25] | 平均低於區間下限 | 疑為搜尋摘要錯誤或區域加權方式不同 | 列低信心，不採用 |
| C-10（<30%，備註） | JLL 2025 亞太平均 | 全球指南 1,460 USD/m² [TC-22] | 亞太指南 1,524 USD/m² [TC-23] | 約 4% | 兩份報告樣本城市、基準期（2025-04 vs Q1 2025）與試配定義不同 | 差異小，並列即可 |

### 6.2 缺口表

| # | 找不到的項目 | 嘗試過的搜尋 | 建議取得方式 |
|---|---|---|---|
| G-01 | C&W 2026 亞太版完整城市表（大阪、深圳、河內、首爾／上海／北京之正確欄位、各城市 all-in 拆分、雅加達與胡志明市 2026 值） | Q1、Q4、Q8、Q9、Q11 | 下載 C&W 2026 亞太 PDF（TC-01）；或請 C&W 台灣研究部提供 |
| G-02 | 首爾 C&W 官方數字（韓元／坪或 USD psf） | Q10；Q13 未執行 | C&W 韓國 2025 報告 PDF（TC-16，搜尋摘要稱以韓元排名，但未取得數字）及 2026 韓國版 |
| G-03 | 台北 110→145 的當地幣（新台幣）變動與原因 | Q7 | C&W 台灣辦公室；比對璞石自身近 2 年商辦報價 |
| G-04 | AECOM《Asia Construction & Cost Handbook》各城市辦公／飯店／零售 fit-out 每 m² 費率 | Q3 | 向 AECOM 亞洲索取 PDF；本輪搜尋引擎未索引 |
| G-05 | Arcadis、RLB、Linesight、Currie & Brown 城市費率 | Q3（僅 Arcadis 中港手冊出現，無費率摘錄）；其餘未搜尋（額度） | 下載 Arcadis 2025 中港手冊（TC-34）全文；RLB Asia Pacific 季報 |
| G-06 | 飯店、零售、餐飲 fit-out 單價（全部城市） | Q3 | AECOM／Arcadis 手冊之 hotel fit-out 與 shop fit-out 列 |
| G-07 | 各城市甲級辦公空置率、新供給、去化（2024–2026） | 未搜尋（額度） | CBRE、JLL、Colliers、C&W 各城市季報 |
| G-08 | 亞太飯店管線（房數、開發中案量） | 未搜尋（額度） | Lodging Econometrics APAC 季報、STR |
| G-09 | 資料中心／半導體外溢 fit-out（台灣、日本、馬來西亞） | 未搜尋（額度）；僅見 C&W 資料中心成本指南存在 [TC-50] | C&W／T&T 資料中心成本指南全文 |
| G-10 | 乃村工藝社、丹青社、スペース、船場 營收與利潤率 | Q14、Q15 未執行 | 各社 IR 決算短信（乃村 2 月決算、丹青社 1 月決算，期別請再確認） |
| G-11 | 金螳螂、亚厦 營收與毛利 | 未搜尋（額度） | 深交所年報（2025 年報） |
| G-12 | 台灣、韓國、東南亞、印度商空設計施工業者營收；ISG、Space Matrix、Unispace、Gammon 亞洲營收 | 未搜尋（額度） | 公司年報、Companies House（ISG）、公開說明書 |
| G-13 | 商空設計費占工程費比例或每 m² 設計費 | 未搜尋（額度） | 各地設計師公會收費標準、RLB／AECOM 手冊之 professional fees 章節 |
| G-14 | 混合辦公對 fit-out 面積量的量化影響 | 未搜尋（額度） | JLL／CBRE 占用者調查 |

---

## 7. 關鍵指標 CSV

```csv
market,metric,value,unit,year,source_id,source_url,definition,confidence
TW,辦公fit-out平均成本（台北）,145,USD/sq ft,2026,TC-04,https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific,C&W亞太2026版城市平均；價格基準2025-12,high
TW,辦公fit-out平均成本（台北）,110,USD/sq ft,2025,TC-05,https://www.cushmanwakefield.com/en/south-korea/news/2026/04/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific,C&W亞太2025版城市平均（2026新聞稿比較值）,high
TW,辦公fit-out成本（台北）,70,USD/sq ft,2019,TC-15,https://www.taipeitimes.com/News/biz/archives/2019/11/05/2003725245,2019年C&W調查；口徑可能與2026不同,medium
JP,辦公fit-out平均成本（東京）,215,USD/sq ft,2026,TC-04,https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific,C&W亞太2026版；亞太最高,high
JP,辦公fit-out平均成本（東京）,195,USD/sq ft,2025,TC-11,https://www.retalkasia.com/news/2025/03/06/office-fit-out-costs-asia-pacific-continue-rise-cushman-wakefield/1741232445,C&W亞太2025版；2025版最高,high
JP,辦公fit-out高規格成本（東京）,4619,USD/m2,2025,TC-27,https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2025/global-office-fit-out-costs,T&T高規格；CAT A+CAT B含家具AV專業費；基準2025Q1,medium
KR,辦公fit-out平均成本（首爾）,130,USD/sq ft,2026,TC-02,https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office/28-29/,C&W亞太2026版表格擷取（欄位未確認；約值）,low
KR,辦公裝修第三方行情基本型（首爾）,120-160,萬韓元/坪,2026,TC-36,https://spacelogin.co.kr/2026-%EC%82%AC%EB%AC%B4%EC%8B%A4-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4-%EC%97%85%EC%B2%B4-%EB%B9%84%EA%B5%90-%EA%B0%80%EC%9D%B4%EB%93%9C/,平台業者行情；中階160-200；高階200以上,low
KR,承包商預期6個月內小幅漲價比例,90,%,2026,TC-35,https://www.kjob.news/news/501752,C&W韓國2026版承包商調查；驅動：人工與關稅,medium
SG,辦公fit-out平均成本（新加坡）,140,USD/sq ft,2026,TC-04,https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific,C&W亞太2026版；與2025大致持平,high
HK,辦公fit-out平均成本（香港）,160,USD/sq ft,2026,TC-04,https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific,C&W亞太2026版；大中華最高、亞太第8,high
HK,辦公fit-out頂級成本（香港）,4575,USD/m2,2025,TC-27,https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2025/global-office-fit-out-costs,T&T premium；口徑同T&T,medium
HK,辦公fit-out頂級平均成本（香港）,31231,HKD/m2,2026,TC-32,https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026-us/hong-kong,T&T 2026 premium平均,medium
CN,辦公fit-out平均成本（上海）,96,USD/sq ft,2026,TC-02,https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office/28-29/,C&W亞太2026版表格擷取（約值；欄位未確認）,low
CN,辦公fit-out平均成本（北京）,95,USD/sq ft,2026,TC-02,https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office/28-29/,C&W亞太2026版表格擷取（約值；欄位未確認）,low
CN,辦公裝修全包行情（上海）,800-1500,RMB/m2,2026,TC-39,http://lingqisj.com/gsxw/3761.html,本地裝修公司行銷文章,low
MY,辦公fit-out平均成本（吉隆坡）,80,USD/sq ft,2026,TC-06,https://www.cushmanwakefield.com/en/thailand/insights/office-fit-out-cost-guide?sort=latest_update,C&W 2026城市排名（泰國頁）,medium
TH,辦公fit-out平均成本（曼谷）,91,USD/sq ft,2026,TC-06,https://www.cushmanwakefield.com/en/thailand/insights/office-fit-out-cost-guide?sort=latest_update,C&W 2026城市排名（泰國頁）,medium
VN,辦公fit-out平均成本（胡志明市）,61,USD/sq ft,2026,TC-06,https://www.cushmanwakefield.com/en/thailand/insights/office-fit-out-cost-guide?sort=latest_update,C&W城市排名；年份標示不明確,medium
ID,辦公fit-out平均成本（雅加達）,58,USD/sq ft,2025,TC-11,https://www.retalkasia.com/news/2025/03/06/office-fit-out-costs-asia-pacific-continue-rise-cushman-wakefield/1741232445,C&W亞太2025版；全區最低,high
PH,辦公fit-out平均成本（馬尼拉）,105,USD/sq ft,2026,TC-06,https://www.cushmanwakefield.com/en/thailand/insights/office-fit-out-cost-guide?sort=latest_update,C&W 2026城市排名（泰國頁）,medium
PH,辦公復原成本平均（馬尼拉）,20,USD/sq ft,2026,TC-01,https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office,C&W reinstatement平均（區間15-25）；表格擷取,low
IN,辦公fit-out成本（孟買）,73,USD/sq ft,2026,TC-07,https://realtynmore.com/competitive-fit-out-market-cushman-wakefield/,C&W 2026協作式混合辦公；印度最高,high
IN,辦公fit-out成本（孟買）,6567,INR/sq ft,2026,TC-09,https://cw-prod-apacgws-a-cd.cushwake.com/en/india/insights/office-fit-out-cost-guide,C&W印度頁；約值,medium
IN,辦公fit-out成本（德里首都圈/班加羅爾/海德拉巴/清奈/浦那）,65-69,USD/sq ft,2026,TC-08,https://ianslive.in/india-remains-asia-pacifics-most-cost-competitive-office-fit-out-market-report--20260326105534,C&W 2026；城市未單列,medium
IN,辦公fit-out低規格成本（班加羅爾）,531,USD/m2,2025,TC-27,https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2025/global-office-fit-out-costs,T&T low specification,medium
IN,辦公fit-out中規格平均（三城）,449,USD/m2,2026,TC-33,https://realtynmore.com/asia-pacific-knight-frank-report,Knight Frank；班加羅爾+孟買+德里首都圈平均,medium
APAC,JLL辦公fit-out平均,1460,USD/m2,2025,TC-22,https://irei.com/news/average-fit-out-costs-for-offices-lowest-in-asia-pacific-compared-to-other-regions-jll/,JLL全球指南2025（2025-04）；全球1830,medium
APAC,JLL適中風格中等品質辦公平均,1524,USD/m2,2025,TC-23,https://www.jll.com/en-in/insights/apac-fit-out-cost-guide-2025,JLL亞太指南基準2025Q1；全球1949,medium
APAC,JLL辦公fit-out平均,1550,USD/m2,2026,TC-24,https://www.jll.com/en-in/guides/apac-fit-out-costs-guide,JLL亞太2026；27城市；當地幣年增2-5%,medium
APAC,C&W承包商預期2026市況改善比例,70,%,2026,TC-17,https://www.malaymail.com/news/money/mediaoutreach/2026/03/26/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific/456444,C&W 2026 Contractor Sentiment Survey,medium
GLOBAL,T&T全球fit-out年度成本漲幅,3,%,2026,TC-30,https://www.turnerandtownsend.com/insights/global-office-fit-out-cost-guide-2026/,T&T 2026；58市場,medium
GLOBAL,JLL全球辦公fit-out平均,2150,USD/m2,2026,TC-26,https://www.joneslanglasalle.com.cn/zh-cn/guides/global-office-fit-out-costs-guide,仲量聯行2026全球指南中文版,medium
```

（共 33 列資料。confidence 欄 high／medium／low 對應正文 高／中／低。）

---

## 8. 來源清單

> 讀取方式：全部為「搜尋結果內容」（WebFetch 不可用；未開啟原始全文）。語言：英＝英文、簡中＝簡體中文、韓＝韓文。

| # | 標題 | 機構／作者 | 年份 | 語言 | URL | 讀取方式 |
|---|---|---|---|---|---|---|
| TC-01 | Office Fit Out Cost Guide Asia Pacific 2026 | Cushman & Wakefield | 2026 | 英 | https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office | 搜尋結果內容 |
| TC-02 | Office Fit Out Cost Guide Asia Pacific 2026 – Page 28-29 | Cushman & Wakefield | 2026 | 英 | https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office/28-29/ | 搜尋結果內容 |
| TC-03 | Global Office Fit Out Cost Guide 2026 | Cushman & Wakefield | 2026 | 英 | https://www.cushmanwakefield.com/en/insights/office-fit-out-cost-guide | 搜尋結果內容 |
| TC-04 | Contractor Confidence Rises Amid Strengthening Office Demand Across Asia Pacific（Greater China） | Cushman & Wakefield | 2026 | 英 | https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific | 搜尋結果內容 |
| TC-05 | Contractor Confidence Rises Amid Strengthening Office Demand Across Asia Pacific（South Korea） | Cushman & Wakefield | 2026 | 英 | https://www.cushmanwakefield.com/en/south-korea/news/2026/04/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific | 搜尋結果內容 |
| TC-06 | Thailand Office Fit Out Costs Trends 2026 | Cushman & Wakefield | 2026 | 英 | https://www.cushmanwakefield.com/en/thailand/insights/office-fit-out-cost-guide?sort=latest_update | 搜尋結果內容 |
| TC-07 | India Reinforces Its Position as Asia Pacific's Most Cost-Competitive Fit-Out Market: Cushman & Wakefield | Realty n More | 2026 | 英 | https://realtynmore.com/competitive-fit-out-market-cushman-wakefield/ | 搜尋結果內容 |
| TC-08 | India remains Asia Pacific's most cost-competitive office fit out market: Report | IANS | 2026 | 英 | https://ianslive.in/india-remains-asia-pacifics-most-cost-competitive-office-fit-out-market-report--20260326105534 | 搜尋結果內容 |
| TC-09 | Office Fit Out Cost Guide（India） | Cushman & Wakefield India | 2026 | 英 | https://cw-prod-apacgws-a-cd.cushwake.com/en/india/insights/office-fit-out-cost-guide | 搜尋結果內容 |
| TC-10 | NAREDCO 轉載 C&W 印度 fit-out 成本（node 2738） | NAREDCO | 2024（推定） | 英 | https://www.naredco.in/index.php/node/2738 | 搜尋結果內容 |
| TC-11 | Office fit out costs Asia Pacific continue to rise – Cushman & Wakefield | Real Estate Asia（retalkasia） | 2025 | 英 | https://www.retalkasia.com/news/2025/03/06/office-fit-out-costs-asia-pacific-continue-rise-cushman-wakefield/1741232445 | 搜尋結果內容 |
| TC-12 | Office fit out costs Asia Pacific continue to rise at slower pace – Cushman & Wakefield | The Commercial Real Estate（commo） | 2025 | 英 | https://www.commo.com.au/news/2025/03/06/office-fit-out-costs-asia-pacific-continue-rise-slower-pace-cushman-wakefield | 搜尋結果內容 |
| TC-13 | Contractor sentiment generally positive as the worst of price pressures ease | Cushman & Wakefield Australia | 2025 | 英 | https://www.cushmanwakefield.com/en/australia/news/2025/03/contractor-sentiment-generally-positive-as-the-worst-of-price-pressures-ease | 搜尋結果內容 |
| TC-14 | Asia Pacific Office Fit Out Cost Guide 2025 (Cushman & Wakefield) | APREA | 2025 | 英 | https://www.aprea.asia/knowledge-hub/asia-pacific-office-fit-out-cost-guide-2025-cushman-wakefield/ | 搜尋結果內容 |
| TC-15 | Taipei offers economical office fit-out costs: survey | Taipei Times | 2019 | 英 | https://www.taipeitimes.com/News/biz/archives/2019/11/05/2003725245 | 搜尋結果內容 |
| TC-16 | HEADLINE No.1 (2025) Market Overview – KR 2025 fit-out cost report | Cushman & Wakefield Korea | 2025 | 英／韓 | https://assets.cushmanwakefield.com/-/media/cw/apac/south-korea/insights/research/kr-2025-fit-out-cost-report_.pdf?rev=b053d7de3df84e7493844c5f898dfac3 | 搜尋結果內容 |
| TC-17 | Contractor confidence rises amid strengthening office demand across Asia Pacific（Contractor Sentiment Survey shows 70%…） | Malay Mail／Media OutReach | 2026 | 英 | https://www.malaymail.com/news/money/mediaoutreach/2026/03/26/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific/456444 | 搜尋結果內容 |
| TC-18 | Contractor Confidence Rises Amid Strengthening Office Demand Across Asia Pacific | Alvinology | 2026 | 英 | https://alvinology.com/2026/03/26/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific/ | 搜尋結果內容 |
| TC-19 | 亚太地区办公室需求持续走强，承包商信心随之不断提升 | 中国工业新闻网（cinn.cn） | 2026 | 簡中 | https://www.cinn.cn/hz/2026/05-07/Zr5z5N6D.html | 搜尋結果內容 |
| TC-20 | [戴德梁行]：2026亚太区办公室装修成本指南 | 发现报告（fxbaogao） | 2026 | 簡中 | https://www.fxbaogao.com/detail/5414206 | 搜尋結果內容 |
| TC-21 | Global Office Fit-Out Cost Guide 2025（JLL，April 2025） | JLL（ASHB 轉載 PDF） | 2025 | 英 | https://www.ashb.com/wp-content/uploads/2025/10/IS-2025-127.pdf | 搜尋結果內容 |
| TC-22 | Average fit-out costs for offices lowest in Asia Pacific compared to other regions: JLL | IREI | 2025 | 英 | https://irei.com/news/average-fit-out-costs-for-offices-lowest-in-asia-pacific-compared-to-other-regions-jll/ | 搜尋結果內容 |
| TC-23 | Asia Pacific Fit-Out Cost Guide 2025 | JLL India | 2025 | 英 | https://www.jll.com/en-in/insights/apac-fit-out-cost-guide-2025 | 搜尋結果內容 |
| TC-24 | Asia Pacific Office Fit-Out Cost Guide 2026 | JLL India | 2026 | 英 | https://www.jll.com/en-in/guides/apac-fit-out-costs-guide | 搜尋結果內容 |
| TC-25 | Global office fit-out costs guide 2026 | JLL | 2026 | 英 | https://www.jll.com/en-us/guides/global-office-fit-out-costs-guide | 搜尋結果內容 |
| TC-26 | 2026全球办公空间装修成本指南 | 仲量联行（JLL China） | 2026 | 簡中 | https://www.joneslanglasalle.com.cn/zh-cn/guides/global-office-fit-out-costs-guide | 搜尋結果內容 |
| TC-27 | Global office fit-out costs – Global office fit-out cost guide 2025 | Turner & Townsend | 2025 | 英 | https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2025/global-office-fit-out-costs | 搜尋結果內容 |
| TC-28 | Methodology – Global office fit-out cost guide 2025 | Turner & Townsend | 2025 | 英 | https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2025/methodology | 搜尋結果內容 |
| TC-29 | Singapore – Global office fit-out cost guide 2025 | Turner & Townsend | 2025 | 英 | https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2025/singapore | 搜尋結果內容 |
| TC-30 | Global office fit-out cost guide 2026 | Turner & Townsend | 2026 | 英 | https://www.turnerandtownsend.com/insights/global-office-fit-out-cost-guide-2026/ | 搜尋結果內容 |
| TC-31 | Asia-Pacific – Global office fit-out cost guide 2026 | Turner & Townsend | 2026 | 英 | https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026/asia-pacific | 搜尋結果內容 |
| TC-32 | Hong Kong – Global office fit-out cost guide 2026 (US) | Turner & Townsend | 2026 | 英 | https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026-us/hong-kong | 搜尋結果內容 |
| TC-33 | Asia Pacific Knight Frank report（印度 fit-out） | Realty n More | 2026 | 英 | https://realtynmore.com/asia-pacific-knight-frank-report | 搜尋結果內容 |
| TC-34 | China & Hong Kong 2025 Construction Cost Handbook | Arcadis Hong Kong Limited | 2025 | 英 | https://media.arcadis.com/-/media/project/arcadiscom/com/perspectives/asia/publications/cch/2025/2025-cnhk-cost-handbookfinal-online.pdf?rev=1b304935c6ec425db127792f5c3703b3 | 搜尋結果內容 |
| TC-35 | 2026 사무실 인테리어 비용 상승 전망: 응답 시공사 90%가 가격 인상 예측 | 전국인력신문（kjob.news） | 2026 | 韓 | https://www.kjob.news/news/501752 | 搜尋結果內容 |
| TC-36 | 2026 사무실 인테리어 업체 비교 가이드 | 스페이스로그인（spacelogin） | 2026 | 韓 | https://spacelogin.co.kr/2026-%EC%82%AC%EB%AC%B4%EC%8B%A4-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4-%EC%97%85%EC%B2%B4-%EB%B9%84%EA%B5%90-%EA%B0%80%EC%9D%B4%EB%93%9C/ | 搜尋結果內容 |
| TC-37 | 사무실 인테리어 비용, 평당 얼마가 현실적인가 — 규모별 정리 | 오피스 인테리어 컨설팅 랩（interiorcnote） | 2026（推定） | 韓 | https://interiorcnote.com/%EC%82%AC%EB%AC%B4%EC%8B%A4-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4-%EB%B9%84%EC%9A%A9-%ED%8F%89%EB%8B%B9-%EC%96%BC%EB%A7%88%EA%B0%80-%ED%98%84%EC%8B%A4%EC%A0%81%EC%9D%B8%EA%B0%80-%EA%B7%9C/ | 搜尋結果內容 |
| TC-38 | 사무실 인테리어 비용 가이드 2026 | ssjum.com | 2026 | 韓 | https://ssjum.com/interior-office.html | 搜尋結果內容 |
| TC-39 | 上海办公室装修每平米多少钱?2026最新报价清单及优势全解析 | 领企装修公司 | 2026 | 簡中 | http://lingqisj.com/gsxw/3761.html | 搜尋結果內容 |
| TC-40 | 北京办公室装修公司｜办公室设计多少钱一平米，装修多少钱一平米 | 网易（163.com） | 2026（推定） | 簡中 | https://c.m.163.com/news/a/KPJJ424N0556AOIS.html | 搜尋結果內容 |
| TC-41 | Office Fit Out Costs Continue to Rise Across Asia Pacific Albeit at Much Slower Rate | Cushman & Wakefield Greater China | 2024 | 英 | https://www.cushmanwakefield.com/en/greater-china/news/2024/05/office-fit-out-costs-continue-to-rise-across-asia-pacific-albeit-at-much-slower-rate | 搜尋結果內容 |
| TC-42 | APAC Office Fit Out Cost Guide 2024 – Page 8-9 | Cushman & Wakefield | 2024 | 英 | https://cushwake.cld.bz/apac-office-fit-out-cost-guide-2024/8-9/ | 搜尋結果內容 |
| TC-43 | 쿠시먼앤드웨이크필드 코리아 '2026 오피스 시장 세미나' 성료… 불확실성 속 최적의 임차 전략 제시 | 뉴스와이어（newswire.co.kr） | 2026 | 韓 | https://www.newswire.co.kr/newsRead.php?no=1032661&sourceType=rss | 搜尋結果內容 |
| TC-44 | India emerges as a global leader in flexible office market maturity | Cushman & Wakefield India | 2025 | 英 | https://cw-prod-apacgws-a-cd.cushwake.com/en/india/news/2025/09/india-emerges-as-a-global-leader-in-flexible-office-market-maturity | 搜尋結果內容 |
| TC-45 | 戴德梁行发布2026上半年深圳写字楼及零售市场报告 | 网易订阅（163.com） | 2026 | 簡中 | https://www.163.com/dy/article/L0PL670A0535A6CE.html | 搜尋結果內容 |
| TC-46 | 戴德梁行：下半年一线城市甲级写字楼租金或继续下降 | 证券时报网（stcn.com） | 年份不明 | 簡中 | https://www.stcn.com/article/detail/1249992.html | 搜尋結果內容 |
| TC-47 | 2026 U.S. Retail Fit Out Cost Guide | Cushman & Wakefield | 2026 | 英 | https://www.cushmanwakefield.com/en/united-states/insights/retail-fit-out-cost-guide | 搜尋結果內容 |
| TC-48 | 2026 서울 오피스 임차사 업종 변화 보고서 | Cushman & Wakefield Korea | 2026 | 韓 | https://www.cushmanwakefield.com/ko-kr/south-korea/insights/seoul-office-tenant-profile-report | 搜尋結果內容 |
| TC-49 | Office Fit-Out Costs Are Rising—Here's Why | Commercial Property Executive | 2025 | 英 | https://www.commercialsearch.com/news/office-fit-out-costs-are-rising-heres-why/ | 搜尋結果內容 |
| TC-50 | Asia Pacific Data Construction Cost Guide 2025.pdf | SlideShare（轉載） | 2025 | 英 | https://www.slideshare.net/slideshow/asia-pacific-data-construction-cost-guide-2025-pdf/277700237 | 搜尋結果內容 |
| TC-51 | Asia Pacific Fit-Out Cost Guide 2025（campaign page） | JLL Singapore | 2025 | 英 | https://www.jll.com.sg/en/campaign/cost-fit-out-guide | 搜尋結果內容 |
| TC-52 | Office sector is regaining its central role in commercial real estate, at a cost, finds JLL's Global Office Fit-Out Cost Guide | McMorrow Reports | 2025 | 英 | https://www.mcmorrowreports.com/office-sector-is-regaining-its-central-role-in-commercial-real-estate-at-a-cost-finds-jlls-global-office-fit-out-cost-guide/ | 搜尋結果內容 |
| TC-53 | APAC cost guide: growing demand for sustainable fit-outs | JLL Southeast Asia | 2025（推定） | 英 | https://www.jll.com/en-sea/insights/apac-cost-guide-growing-demand-for-sustainable-fit-outs | 搜尋結果內容 |

| TC-54 | Office Fit Out Cost Guide Americas 2026 | Cushman & Wakefield | 2026 | 英 | https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-amer-regional-en-content-pds-office | 搜尋結果內容 |

> 來源備註：TC-14、TC-20、TC-42、TC-49、TC-51 僅確認報告存在或作為同一數字之輔證，正文未單獨依賴其數字。TC-53 僅於第 3 章以標題形式引用。TC-54 僅用於說明 C&W 美洲版的成本口徑（不含弱電／AV／保全／FF&E／軟成本），非亞洲數字。
