# 跨國主題 C：商業空間（辦公／飯店／零售／餐飲）裝修需求與城市級裝修成本基準 — 12 市場（r1 獨立三角驗證，含第 2 輪補缺）

> 研究日期：2026-10-09｜研究者：子代理（TC）｜語言：繁體中文（台灣用語），機構與公司原名置於括號
> 獨立性：未開啟 `04-research-notes/`、`05-report/` 任何檔案；未參考其他 AI 產出。
> 幣別／單位：**一律照原文記錄，未做匯率或面積換算**（由中央統一處理）。第 6 章矛盾診斷中為判斷差距大小所做的「面積」換算（1 m² = 10.7639 sq ft；1 坪 = 3.3058 m² ≈ 35.583 sq ft）僅用於診斷，不作為紀錄值。利潤率欄標「計算值」者，為以同一來源之營業利益÷營收算出（非換匯）。
> 讀取方式：WebFetch／curl 受組織網路政策封鎖，所有來源皆為「搜尋結果內容」（搜尋引擎回傳的摘錄與摘要），**未開啟任何原始 PDF 全文**。
> URL 對應原則：搜尋工具回傳「摘要＋連結清單」。凡能由標題或摘錄直接對應到特定 URL 的數字，信心最高為「中／高」；摘要中有數字但無法確定對應哪一個 URL 者，標「（推定）」或「搜尋摘要」並一律給「低」。

---

## 0. 搜尋紀錄摘要

**第 1 輪限制**：完成 12 次搜尋後，系統回報本回合 WebSearch 共用額度用盡，其後 3 次（1 韓、2 日）未執行。
**第 2 輪補缺**：協調者重置額度並設上限 14 次；本輪恰用 14 次，未再遭阻擋。

| # | 輪 | 查詢字串 | 語言 | 模式 | 結果 |
|---|---|---|---|---|---|
| Q1 | 1 | Cushman & Wakefield Asia Pacific Office Fit Out Cost Guide 2025 | 英 | extended | 成功：2025 版區間（東京 195／雅加達 58 USD psf）、2026 版 33 城市 |
| Q2 | 1 | JLL fit-out cost guide Asia Pacific 2025 per square foot | 英 | extended | 成功：JLL 2025／2026 亞太平均 USD/m² |
| Q3 | 1 | AECOM Asia Construction Cost Handbook 2025 fit-out office hotel per m2 | 英 | extended | 未找到 AECOM 手冊；帶出 T&T 2025 東京／香港、Arcadis 中港手冊 |
| Q4 | 1 | Cushman Wakefield fit out cost guide 2026 Tokyo Singapore Hong Kong per square foot USD | 英 | extended | 成功：東京 215、香港 160、新加坡 140、台北 145 |
| Q5 | 1 | Turner & Townsend office fit-out cost guide 2025 Singapore Shanghai Mumbai per m2 | 英 | extended | 部分：T&T 方法論、班加羅爾低規格 531 USD/m² |
| Q6 | 1 | Cushman Wakefield fit out cost India Mumbai Bengaluru 2026 per sq ft | 英 | standard | 成功：印度 65–73 USD psf；Knight Frank 449 USD/m² |
| Q7 | 1 | Cushman Wakefield 2026 fit out cost Taipei US$145 per square foot | 英 | extended | 成功：台北 110→145；2019 年 70 |
| Q8 | 1 | Cushman Wakefield fit out cost guide Kuala Lumpur Bangkok Manila Ho Chi Minh Jakarta 2026 | 英 | extended | 成功：馬尼拉 105、曼谷 91、吉隆坡 80、胡志明市 61 |
| Q9 | 1 | 戴德梁行 办公楼装修成本指南 2026 上海 北京 深圳 每平方英尺 | 簡中 | extended | 部分：滬京領跑內地（無數字）；本地行情（低） |
| Q10 | 1 | 쿠시먼앤드웨이크필드 오피스 인테리어 비용 가이드 2026 서울 평당 | 韓 | extended | 部分：C&W 韓國 2026 版；第三方每坪行情（低） |
| Q11 | 1 | Cushman Wakefield 2025 fit out cost guide Seoul Shanghai Beijing Kuala Lumpur Bangkok USD psf | 英 | extended | 部分：首爾約 130、上海約 96、北京約 95（低） |
| Q12 | 1 | Turner & Townsend fit-out cost guide 2026 Asia-Pacific Tokyo Hong Kong Singapore high specification US$ per m2 | 英 | extended | 部分：T&T 2026 香港 HK$31,231/m² |
| Q13 | 1 | 쿠시먼 2025 오피스 인테리어 비용 보고서 서울 원 평당 핏아웃 | 韓 | standard | 未執行（第 1 輪額度用盡） |
| Q14 | 1 | 乃村工藝社 2026年2月期 決算 売上高 営業利益 | 日 | standard | 未執行（第 1 輪額度用盡；第 2 輪 Q18 補做） |
| Q15 | 1 | 丹青社 2026年1月期 決算 売上高 営業利益率 | 日 | standard | 未執行（第 1 輪額度用盡；第 2 輪 Q18 補做） |
| Q16 | 2 | AECOM Asia Construction & Cost Handbook 2025 hotel fit-out retail shop fit-out cost per m2 | 英 | extended | AECOM 手冊仍未被索引；Arcadis 中港手冊零售／飯店表格擷取錯亂 |
| Q17 | 2 | Arcadis International Construction Costs 2025 Asia hotel fit-out per m2 Singapore Kuala Lumpur Bangkok | 英 | extended | 成功：香港飯店 fit-out HK$/m²（公共區／客房×星級）；QCC 2025 Q2；ICC 2025 標價漲幅 |
| Q18 | 2 | 乃村工藝社 丹青社 決算 2025 売上高 営業利益 過去最高 | 日 | extended | 成功：乃村 2026/2 期、丹青社 2025/1 期與「過去最高」列 |
| Q19 | 2 | 金螳螂 亚厦股份 2025年年报 营业收入 毛利率 公装 | 簡中 | extended | 成功：兩家 2025 營收、毛利率 |
| Q20 | 2 | Grade A office vacancy Q2 2026 Tokyo Singapore Hong Kong Shanghai Seoul new supply | 英 | extended | 成功：東京、新加坡、香港 |
| Q21 | 2 | 台北 A辦 空置率 2026 信義區 新供給 商辦 | 繁中 | extended | 成功：台北空置率、2026–2030 供給、信義南山案 |
| Q22 | 2 | Lodging Econometrics Asia Pacific hotel construction pipeline 2026 rooms projects | 英 | extended | 成功：APEC 管線 2026 Q1／Q2 |
| Q23 | 2 | Grade A office vacancy 2026 Kuala Lumpur Bangkok Jakarta Manila Ho Chi Minh City | 英 | extended | 部分：吉隆坡、雅加達 |
| Q24 | 2 | 서울 오피스 공실률 2026년 2분기 A급 오피스 신규 공급 | 韓 | extended | 成功：CBRE／C&W／알스퀘어 三家數字 |
| Q25 | 2 | 上海 甲级写字楼 空置率 2026年第二季度 新增供应 北京 深圳 | 簡中 | extended | 成功：上海、北京、深圳 |
| Q26 | 2 | 漢唐 帆宣 亞翔 2025年 營收 無塵室 廠務 統包 創新高 | 繁中 | extended | 成功：台灣無塵室／廠務統包商營收 |
| Q27 | 2 | 商業空間 室內設計費 工程費 百分比 每坪 行情 辦公室 餐廳 | 繁中 | extended | 成功（行銷來源，低信心）：台灣設計費 %、每坪行情 |
| Q28 | 2 | Rider Levett Bucknall Asia hotel fit-out retail fit-out cost per m2 2025 Singapore Kuala Lumpur Ho Chi Minh | 英 | extended | 部分：RLB Riders Digest 有飯店／零售章節，但數字未擷取 |
| Q29 | 2 | office vacancy Q2 2026 Bengaluru Mumbai Metro Manila Bangkok Ho Chi Minh City Grade A | 英 | extended | 成功：曼谷、馬尼拉、胡志明市；印度部分（低） |

**累計統計**：嘗試 29 次；成功 26 次；被擋 3 次。在地語言成功 9 次（簡中 3、繁中 3、韓 2、日 1）——已達「≥25 次、≥6 次在地語言」。第 2 輪 14 次中在地語言 7 次。
**來源**：TC-01～TC-117 共 117 條；在地語言 52 條（繁中 19、簡中 18、韓 10、日 5）。

---

## 1. 關鍵結論（每點含數字＋來源#）

1. **辦公 fit-out 成本階梯（C&W 2026，USD／sq ft，價格基準 2025-12）**：東京 **215** ＞ 香港 **160** ＞ 台北 **145** ＞ 新加坡 **140** ＞ 首爾約 130（低）＞ 馬尼拉 **105** ＞ 上海約 96／北京約 95（低）＞ 曼谷 **91** ＞ 吉隆坡 **80** ＞ 孟買約 **73** ＞ 印度其他城市 **65–69** ＞ 胡志明市 **61** ＞ 雅加達 **58**（2025 版）[TC-04][TC-06][TC-07][TC-02][TC-11]。【實際】（東京／香港／台北／新加坡／孟買），其餘【示意】
2. **台北 2026 年漲幅亞太最大之一**：**USD 110 → 145／sq ft（約 +32%）** [TC-04][TC-05]；原因未揭露。台北本地行銷行情為辦公 **5–8 萬／坪（台北，PRO360）**、設計型辦公 **8–15 萬／坪** [TC-61][TC-60]（低信心），與 C&W 口徑（含家具／機電／AV-IT）不同，須中央換匯後比對（矛盾表 C-13）。
3. **等級與口徑差距可達 2 倍以上**：T&T 2025 東京高規格 **USD 4,619／m²**、香港頂級 **USD 4,575／m²**、班加羅爾低規格 **USD 531／m²** [TC-27]，與 C&W 城市平均不可直接比（C-01、C-02）。
4. **飯店 fit-out（僅香港有可用數字）**：Arcadis 2025 手冊（4Q2024 價位）香港五星級公共區 **HK$24,000 以上／m²**、四星級 **HK$17,000–24,000**、三星級 **HK$11,500–17,000**；客房五星級 **HK$15,500 以上**、四星級 **HK$11,500–15,000**、三星級 **HK$9,500–11,200** [TC-55]。其他 17 城市飯店、零售 fit-out 單價：**無資料**（AECOM 手冊兩度搜尋未被索引；RLB 有章節但未擷取數字 [TC-58][TC-59]）。台北餐飲：咖啡廳 **10–20 萬／坪**、精品餐廳 **20–35 萬／坪**（行銷來源，低）[TC-60]。
5. **2026 Q2 甲級辦公空置率高度分化**：東京 Grade A **1.3%**（Colliers）[TC-67]；新加坡核心 CBD Grade A **3.3%**（CBRE）／CBD Grade A **5.6%**（JLL）[TC-69][TC-68]；首爾 **4.2%**（CBRE）／**5.8%**（C&W）／**6.5%**（알스퀘어，全體）[TC-78][TC-79][TC-81]；香港 **13.1%**（JLL）／**16.1%**（Colliers）[TC-71][TC-70]；吉隆坡 **14.8%** [TC-89]；北京 **14.7%**（JLL）[TC-84]；曼谷 CBD Grade A **21.9%** [TC-91]；深圳 **22.7%** [TC-88]；上海 **23.5%**（JLL）[TC-82]；雅加達 Grade A 出租率 **67%**（2026 Q1）[TC-90]。
6. **台北正進入商辦供給潮（璞石主場）**：高力預估 2026–2030 台北市中心新增商辦約 **39 萬坪**（搜尋摘要，低）；仲量統計 2021–2030 約 **44 萬坪** A 辦 [TC-73]；世邦魏理仕（CBRE）預測 A 辦空置率 **2028 年近 25%** [TC-72]；南山人壽信義 A26（2027）、A21（2028）四棟合計約 **12.2 萬坪**，租金衝每坪 **5,000 元** [TC-74]。→ 2026–2028 年信義區有大量新進場 fit-out 需求。
7. **飯店管線（亞太不含中國，Lodging Econometrics）**：2026 Q2 **2,506 案／452,972 房**（案數年增 17%），其中印度 **1,033 案**；Q1 越南 **258 案／87,077 房** 居第二、曼谷 **68 案** 居城市之首、奢華級 **404 案** 創紀錄 [TC-99][TC-100][TC-101]。
8. **主要玩家財務**：乃村工藝社 2026/2 期營收 **1,626 億 7,900 萬日圓**、營業利益 **128 億 1,800 萬日圓**（營業利益率計算值 **7.9%**）[TC-103]；丹青社 2025/1 期營收 **918 億 5,800 萬日圓**、營業利益 **51 億 4,700 萬日圓**（計算值 **5.6%**）[TC-104]；金螳螂 2025 年營收 **173.10 億元**、毛利率 **12.67%**（裝飾業毛利率 12.42%，2024 年 13.94%）[TC-108]；亚厦 2025 年營收 **91.18 億元（−24.87%）** [TC-110]。
9. **台灣半導體外溢的「廠務 fit-out」規模遠大於商空裝修**：亞翔 2025 營收約 **767.39 億元（+18.1%）**、漢唐約 **660.78 億元（+39.3%）**、帆宣約 **515.67 億元（−15%）**（搜尋摘要，低～中）；亞翔 2026 前 8 月 **679.04 億元（+63.4%）**、漢唐 **656.94 億元（+71.6%）**[TC-112]；金螳螂亦已將潔淨室列為培育業務 [TC-108]。
10. **成本動能溫和、設計費僅台灣有行情**：JLL 2026 亞太當地幣年增 **2–5%** [TC-24]、T&T 全球約 **3%** [TC-30]、Arcadis 2025 標價漲幅新加坡約 **3–6%**、吉隆坡 **2.5–3.5%**、香港 **0 至 −2%**（表格錯亂，低）[TC-57]；台灣設計費 **5–20% 工程款**、監工費 **5–10%**、商空設計費 **1,500–4,500 元／坪**（行銷來源，低）[TC-61][TC-63][TC-65]。其他 11 市場設計費：**無資料**。

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
| 台北 Taipei | 辦公 | 本地平台報價統計（連工帶料） | 50,000–80,000 | 元（新台幣）／坪 | 2026 | TC-61 | PRO360 達人網台北地區報價統計；含設計費 5–20%、監工 5–10%、工程 70–90% 之拆分 | 低 | 【示意】 |
| 台灣（未限城市） | 辦公 | 一般辦公／設計型辦公 | 3–8 萬／8–15 萬 | 元（新台幣，原文未標幣別）／坪 | 2026 | TC-60 | howroom 行銷文章 | 低 | 【示意】 |
| 台灣（未限城市） | 辦公 | 新商辦／屋齡 15 年以上舊商辦翻新 | 7–13 萬／10–16 萬 | 元（新台幣，原文未標幣別）／坪 | 2026 | TC-62（推定） | 行銷文章；URL 對應由搜尋摘要推定 | 低 | 【示意】 |
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

### 2.2 區域平均與成本動能（非城市級，作為校準錨點）

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
| 新加坡／吉隆坡／香港／德里 | Arcadis 標價漲幅（截至 4Q2025 的 12 個月） | 約 3–6／2.5–3.5／0 至 −2／約 4 | % | ICC 2025 | TC-57 | 表格擷取錯亂（如「Singapore 2 to 3 3 to 6」），欄位對應未確認 | 低 |

### 2.3 飯店／零售／餐飲（Hotel／Retail／F&B）

| 城市 | 類型 | 等級／情境 | 數值 | 幣別與單位 | 版本年 | 來源# | 範圍說明 | 信心 | 標示 |
|---|---|---|---|---|---|---|---|---|---|
| 香港 | 飯店 fit-out | 公共區（前場）三星／四星／五星 | 11,500–17,000／17,000–24,000／24,000 以上 | HK$／m² | 2025 手冊（4Q2024 價位） | TC-55, TC-34 | Arcadis〈FIT-OUT COSTS FOR HONG KONG〉；面積量至外牆內緣 | 中 | 【示意】 |
| 香港 | 飯店 fit-out | 客房 三星／四星／五星 | 9,500–11,200／11,500–15,000／15,500 以上 | HK$／m² | 2025 手冊（4Q2024 價位） | TC-55, TC-34 | 同上 | 中 | 【示意】 |
| 香港 | 飯店（整棟建造，非純 fit-out） | 平價三星／商務四五星／奢華五星 | 31,600–33,400／32,600–37,300／37,900–42,100 | 推定 HK$／m² CFA（摘錄中幣別單位未完全確認） | 2Q2025 | TC-56 | Arcadis QCC：含公共區 fit-out 與機電，不含店鋪裝修 | 低 | 【示意】 |
| 新加坡 | 飯店客房 fit-out 與 FF&E | — | 無資料（章節存在，數字未擷取） | — | RLB 2026（1Q2026 價位） | TC-58 | RLB 新加坡飯店費率含 FF&E、不含營運物資（OS&E） | — | — |
| 吉隆坡、胡志明市（另含雅加達） | 飯店／零售 | — | 無資料（RLB Asia 表有 RM、VND('000) 列，欄位標題未擷取） | — | RLB 2026（4Q2025） | TC-59 | RLB 亞洲面積口徑：營建樓地板面積（CFA），量至外牆外緣，含地下室與地上停車 | — | — |
| 台灣（未限城市） | 餐飲 fit-out | 咖啡廳／精品餐廳（連工帶料） | 10–20 萬／20–35 萬 | 元（新台幣，原文未標幣別）／坪 | 2026 | TC-60 | 行銷文章；餐飲工程中廚房設備約 20–40%、機電 15–30%、木作天花＋隔間 20–30% | 低 | 【示意】 |
| 新加坡 | 零售 | — | 無資料 | — | RLB 2026 | TC-58 | RLB 註明零售營建成本**不含**租戶 fit-out | — | — |
| 其餘城市 | 飯店／零售／餐飲 | — | **無資料** | — | — | — | AECOM 手冊於 Q3、Q16 兩度搜尋未被索引；Arcadis 中港手冊零售列擷取錯亂（「Retail malls, high end … 1,579–2,324／2,125–2,415」無法對應類別）[TC-55] | — | — |

---

## 3. 各市場商業空間需求脈絡（2024–2026）

### 3.1 區域整體
- C&W 2026 新聞稿標題「亞太辦公需求走強，承包商信心上升」（Contractor Confidence Rises Amid Strengthening Office Demand Across Asia Pacific）[TC-04][TC-05][TC-17][TC-18]；承包商調查 **70%** 受訪者預期 2026 年市況改善 [TC-17]。信心：中
- C&W 2026：共識為未來 6 個月工料成本僅「小幅」上升 [TC-01]；2025 版標題「最壞的價格壓力已過」[TC-13]；2024 版標題「續漲但漲速明顯放緩」[TC-41]。→ 2024–2026 為「漲幅收斂」週期。
- JLL：辦公室重回商用不動產核心角色、但代價升高 [TC-52]；亞太「永續 fit-out 需求成長」[TC-53]。信心：低（僅標題）
- 混合辦公：C&W 印度頁成本情境即設定為「協作式混合辦公」[TC-09]；**fit-out 量（m²）受混合辦公影響之量化數字：無資料**。
- 「往優質遷移（flight-to-quality）」：C&W 越南 2026-09 新聞稿標題明言胡志明市需求由 flight-to-quality 主導 [TC-93]；首爾 CBRE 稱扣除新供給後既有大樓空置反而下降 [TC-78]；台北戴德梁行 2026 Q1 敦北次市場成交占 52%、信義 29%，租戶偏好新落成大樓（搜尋摘要，低）。
- 飯店管線（亞太不含中國，APEC，Lodging Econometrics）：
  - 2026 Q2：**2,506 案／452,972 房**（案數 +17%、房數 +11% YoY）；施工中 **989 案／199,362 房**；早期規劃 **1,119 案／181,397 房**（占 45%，創紀錄）；當季開工 **101 案／16,628 房**；印度 **1,033 案／137,601 房** 居首 [TC-99][TC-101]。信心：中
  - 2026 Q1：**2,387 案／442,973 房**（+15%／+9% YoY）；施工中 963 案／202,877 房；越南 **258 案／87,077 房** 第二；曼谷 **68 案／16,267 房** 城市第一；高檔（upscale）616 案／120,127 房、奢華（luxury）**404 案／75,803 房** 創紀錄 [TC-100]。信心：中～高（標題直接確認 2,387 案）
  - 全球：2025 年新開幕 **2,438 家／332,699 房**；預測 2026 年 **2,742 家／379,921 房** [TC-98]。信心：中
  - Skift：「中國、印度、越南領先亞太飯店管線」（2026-02）[TC-102]。中國管線數字：**無資料**（APEC 不含中國）。
- 零售／餐飲開店數：**無資料**（各市場皆未搜尋到；額度優先用於飯店與辦公）。

### 3.2 分市場（甲級辦公以 2026 Q2 為主）

| 市場 | 辦公：空置率／去化／新供給 | 飯店管線 | 零售／餐飲 | 資料中心／半導體外溢 | 來源 |
|---|---|---|---|---|---|
| 台灣（台北） | 仲量：2026 Q3 台北核心商業區空置 **5.8%**（+0.7pp，敦北國泰新案入市）；高力：2026 Q2 整體 **6.82%**、A 級 **7.17%**、頂級 **11.62%**，預估年底升至約 **8.96%**；戴德梁行：2026 Q1 A 辦 **9.0%**（+1.1pp）（以上三筆為搜尋摘要，URL 未能對應，低）。供給：仲量 2021–2030 約 **44 萬坪** A 辦、空置高峰 10–15% [TC-73]；CBRE 預測 2028 年近 **25%** [TC-72]（2025 年報導）；南山信義 A26（2027）、A21（2028），四棟約 **12.2 萬坪**，名目租金每坪逾 **5,000 元**、南山廣場出租率約 96% [TC-74] | 無資料 | 無資料 | 亞翔、漢唐、帆宣等廠務統包商 2025–2026 營收創高（見第 4 章）[TC-112][TC-113] | TC-72～77, TC-112～117 |
| 日本（東京） | Colliers：Grade A（都心五區）空置 **1.3%**、租金 **JPY 39,900／坪**、新供給 **31,300 坪**、淨去化 **35,400 坪**（需求＞供給）[TC-67]；另有 Savills C5W Grade A **0.6%**（搜尋摘要，URL 未對應，低）。T&T：東京承包商競爭有限推高成本 [TC-27] | 無資料 | 無資料 | 無資料 | TC-67, TC-27 |
| 韓國（首爾） | CBRE：A 級三大圈 **4.2%**（+1.4pp），新租賃面積 **143,881 m²** 為一年多來最大，名目租金 **41,496 韓元／m²／月**（+1.4%）[TC-78]；C&W：A 級 **5.8%**（+1.8pp，2021 Q3 以來最高），CBD **9.0%**、GBD **3.1%**，租金年增 5.0%，淨去化 8,251 m²；肇因乙支路 G1 Seoul、Le Nesquare 同時竣工 [TC-79][TC-80]；알스퀘어：全體 **6.5%**，新供給 11 棟約 **99,000 坪**，CBD **7.3%** [TC-81] | 無資料 | 無資料 | 無資料 | TC-78～81 |
| 新加坡 | JLL：CBD Grade A（不含新竣工）**5.6%**，九季新低；2026 年唯一主要 Grade A 竣工為 Shaw Tower，供給偏緊至 2028 [TC-68]；CBRE：核心 CBD Grade A **3.3%**（Q2）→ **2.6%**（Q3）[TC-69]；全島約 11.0%（搜尋摘要，低）。T&T：2024 Q4 去化與入住率改善 [TC-29] | 無資料 | 無資料 | 無資料 | TC-68, TC-69, TC-29 |
| 香港 | Colliers：Q2 淨承租 **864,000 sq ft**，Grade A 整體空置降 1pp 至 **16.1%**，CBD **10.2%**（−4.3pp YoY），下半年約 **120 萬 sq ft** 新供給 [TC-70]；JLL：6 月 Grade A **13.1%**，Q2 淨去化 **492,000 sq ft**，Q2 無新竣工 [TC-71] | 無資料 | 無資料 | 無資料 | TC-70, TC-71 |
| 中國大陸 | 上海：仲量 Q2 竣工 2 案 **13.5 萬 m²**、空置 **23.5%**（−0.7pp）[TC-82]（年份由摘要判為 2026，見矛盾表）；另一機構 3 案 **39.1 萬 m²**、空置 **24.3%**、淨吸納 **23.2 萬 m²** [TC-83]。北京：仲量 **14.7%**、Q2 新供給 0 [TC-84]；高力 淨吸納 **14.6 萬 m²**（近三年單季新高）、空置 **17.5%** [TC-85]；莱坊 **15.9%**、淨有效租金 **219.2 元／m²／月**、全年新供給約 **79.9 萬 m²** [TC-86]；下半年至 2027 約 18 個月高供應期 [TC-87]。深圳：莱坊 新供給 **4 萬 m²**、淨吸納 **102,492 m²**、空置 **22.7%**、有效租金 **139.7 元／m²／月**（−1.5%）[TC-88]。另：戴德梁行稱一線城市甲級租金或續降（年份不明）[TC-46] | 無資料（APEC 不含中國） | 無資料 | 金螳螂已有潔淨室業務覆蓋半導體 [TC-108] | TC-82～88, TC-46, TC-108 |
| 馬來西亞（吉隆坡） | JLL：Q2 淨去化 **250,000 sq ft**、空置 **14.8%**；年底前再增 **264 萬 sq ft**，空置恐升至 **16.4%**（是否限 Grade A 未明）[TC-89] | 無資料 | 無資料 | 無資料 | TC-89 |
| 泰國（曼谷） | C&W：CBD Grade A 空置 **21.9%**（前季 23.3%），2023 Q1 以來最低 [TC-91]；C&W 2024 年預測曼谷 2027 年空置將逾 25%（舊預測）[TC-94] | Bangkok 為 APEC 管線城市第一（68 案）[TC-100] | 無資料 | 無資料 | TC-91, TC-94, TC-100 |
| 越南（胡志明市） | C&W：核心區 Grade A 出租率 **89.8%**（+1.4pp），Q2 核心與擴大市場皆無新供給，「趨近平衡、flight-to-quality」[TC-93]；非 CBD Grade A 出租率 88.39%（maisonoffice.vn 搜尋摘錄，非顧問原稿，未列入來源、不採用）；C&W 2024 年預測 2024–2025 CBD（第一郡）3 案 **118,700 m²** [TC-94] | 越南 258 案／87,077 房（APEC 第二）[TC-100] | 無資料 | 無資料 | TC-93, TC-94, TC-100 |
| 印尼（雅加達） | JLL：2026 Q1 Grade A 出租率 **67%**（+0.5pp）；年初至今無竣工，2026 全年亦無；年底空置預測 31% 或 32%（同頁兩說）[TC-90] | 無資料 | 無資料 | 無資料 | TC-90 |
| 菲律賓（馬尼拉） | Q2 去化 **40,400 m²**、空置 **13.8%**（−80.9bp），無新竣工（是否 Grade A 未明）[TC-92] | 無資料 | 無資料 | 無資料 | TC-92 |
| 印度 | 全國前 7 城空置 **14.5%**（5 年新低，−160bp）、Grade A **15.2%**（8 季新低）、班加羅爾約占 Q2 全國需求 **27%**、孟買空置 **10.8%**（16 年新低）——皆為搜尋摘要，URL 對應未確認，**低** [TC-95][TC-96][TC-97（推定）]；C&W 2025-09 標題「印度成為全球彈性辦公成熟度領先者」[TC-44] | 印度 1,033 案／137,601 房（APEC 第一）[TC-99][TC-101] | 無資料 | 無資料 | TC-95～97, TC-44, TC-99 |

- 資料中心：《Asia Pacific Data Construction Cost Guide 2025》存在（SlideShare 轉載，出版者未確認）[TC-50]，無城市數字。

---

## 4. 主要玩家表

| 公司 | 市場 | 營收 | 利潤率 | 業務 | 年度 | 來源# | 信心 |
|---|---|---|---|---|---|---|---|
| 乃村工藝社（Nomura Co., Ltd.，9716） | 日本 | 1,626 億 7,900 萬日圓；營業利益 128 億 1,800 萬日圓；純益 91 億 3,400 萬日圓；2027/2 期預估營收 1,680 億、營業利益 134 億 | 營業利益率 **7.9%**（計算值） | 商業空間、展示、內裝（ディスプレイ業界二強之一）[TC-107] | 2026 年 2 月期（2026-04-14 公布） | TC-103 | 中 |
| 丹青社（Tanseisha，9743） | 日本 | 918 億 5,800 萬日圓；營業利益 51 億 4,700 萬日圓 | **5.6%**（計算值） | 商業／文化空間 | 2025 年 1 月期 | TC-104 | 中 |
| 丹青社（同上） | 日本 | 「過去最高」列：1,072 億 2,200 萬日圓；營業利益 83 億 5,800 萬日圓（推定為 2026 年 1 月期實績；同頁 2027/1 期預估營收 1,070 億） | **7.8%**（計算值） | 同上 | 推定 2026 年 1 月期（**期別未確認**） | TC-104 | 低 |
| 丹青社（補充） | 日本 | 2025 年 2–4 月期純益為前年同期 2.7 倍，上修通期預估 | — | — | 2025 | TC-105 | 中 |
| スペース（Space Co., Ltd.） | 日本 | 無資料 | 無資料 | 商業設施內裝 | — | —（SHO-CASE 稱上場 6 社彙整存在 [TC-106]，數字未擷取） | — |
| 船場（Semba） | 日本 | 無資料 | 無資料 | 商業設施內裝 | — | 同上 | — |
| 金螳螂（Suzhou Gold Mantis，002081） | 中國大陸 | 173.10 億元；淨利 4.44 億元（−18.42%）；建築裝飾業營收約 167.68 億元 | 綜合毛利率 **12.67%**；裝飾業毛利率 **12.42%**（2024：13.94%）；淨利率 2.6%（計算值） | 公裝為主；潔淨室（含半導體）為培育業務 | 2025（年報 2026-04-29 披露） | TC-108, TC-109 | 中 |
| 亚厦股份（Zhejiang Yasha，002375） | 中國大陸 | 91.18 億元（−24.87%）；歸母淨利 3.30 億元（+9.00%）；經營現金流 2.41 億元 | 淨利率 3.6%（計算值）；毛利率：前三季 14.63%／同花順 2025 年 15.61%／2025 中報裝飾業 11.39%（口徑不一，見矛盾表） | 建築裝飾＋幕牆；2025 前三季營收 68.73 億（行業第三）、裝飾工程 26.9 億（55.07%）、幕牆 18.89 億（38.67%） | 2025 | TC-110, TC-111 | 中（營收）／低（毛利率） |
| 亞翔（L&K Engineering，6139） | 台灣 | 2025：約 767.39 億元（+18.1%，新高；另一報導 774.85 億、+19%）；2026 前 8 月 679.04 億（+63.4%），8 月 110.19 億；在手訂單 4,400.73 億（新高） | 無資料 | 無塵室機電、公共工程 | 2025／2026 | TC-112（8 月數字）；2025 全年 TC-114～116（推定） | 中（2026）／低（2025） |
| 漢唐（United Integrated Services，2404） | 台灣 | 2025：約 660.78 億元（+39.3%，史上次高）；稅後純益 90.69 億（+46.5%），EPS 48.08 元；2026 前 8 月 656.94 億（+71.6%）；在手訂單估逾千億 | 淨利率約 13.7%（計算值，低） | 台積電無塵室系統統包 | 2025／2026 | TC-112, TC-113；2025 全年 TC-115, TC-117（推定） | 中（2026）／低（2025） |
| 帆宣（Marketech，6196） | 台灣 | 2025：約 515.67 億元（−15%，史上第三高），獲利創新高；現金股利 6.5 元、配息率 41.9% | 無資料 | 廠務、設備 | 2025 | TC-116（推定） | 低 |
| ISG、Space Matrix、Unispace、Gammon（金門建築） | 亞太 | 無資料 | 無資料 | fit-out／設計施工 | — | — | — |
| 台灣商空室內設計／裝修公司（非廠務） | 台灣 | 無資料 | 無資料 | — | — | — | — |
| 韓國、東南亞、印度在地商空業者 | 各市場 | 無資料 | 無資料 | — | — | — | — |

- 成本基準發布者（同時為專案管理／成本顧問服務商）：Cushman & Wakefield（33 城市，2026）[TC-01]、JLL（27 城市，2026）[TC-24]、Turner & Townsend（58 市場，2026）[TC-30]、Knight Frank（印度，2026）[TC-33]、Arcadis（中港手冊 2025、QCC、ICC 2025）[TC-55][TC-56][TC-57]、Rider Levett Bucknall（Riders Digest 2026 新加坡、菲律賓、澳洲版）[TC-58][TC-59]。AECOM、Linesight、Currie & Brown：搜尋未取得任何內容。

### 設計費基準（% 或每 m²／每坪）

| 市場 | 指標 | 數值 | 單位 | 年 | 來源# | 範圍說明 | 信心 |
|---|---|---|---|---|---|---|---|
| 台灣 | 設計費／監工費／工程費 占總預算 | 5–20／5–10／70–90 | % | 2026 | TC-61 | PRO360 辦公室裝潢估算（「僅供參考」） | 低 |
| 台灣 | 設計費（按總工程款） | 5–20 | % | 2026 | TC-63 | Dahuan 設計 FAQ；另監工費 5–10% | 低 |
| 台灣 | 設計費（按坪） | 3,000–10,000 | 元／坪 | 2026 | TC-63 | 同上（住宅為主） | 低 |
| 台灣 | 設計費（按坪） | 4,500–8,000 | 元／坪 | 2026 | TC-64 | 好感生活提案（住宅為主） | 低 |
| 台灣（台中） | 商業空間／辦公設計費 | 1,500–4,500 | 元／坪 | 2026 | TC-65 | 介入空間收費標準；面積大故單價較低 | 低 |
| 台灣（桃園） | 監工費（工程地點在桃園市外） | 10–12 | % 總工程費 | 2026 | TC-66 | 桃園優德收費標準；付款：開工 30%、中繼 30%、尾款 10% | 低 |
| T&T／C&W 指南 | 專業費 | 已計入總成本，但占比未揭露 | — | 2025／2026 | TC-28, TC-01 | — | — |
| 其他 11 市場 | 商空設計費 | **無資料** | — | — | — | 未搜尋（額度） | — |

---

## 5. 對璞石（宜蘭＋台北信義；裝修＋不動產＋家居零售）的啟示

> 以下為依第 1–4 章已引用數字所做之推論，非新事實。

1. **主場的近期需求最確定：信義區新商辦潮**。南山 A26（2027）、A21（2028）合計約 12.2 萬坪 [TC-74]，台北 2021–2030 年約 44 萬坪 A 辦 [TC-73]，CBRE 預測 2028 年空置近 25% [TC-72]。推論：空置上升期房東常以裝修補貼、交屋標準裝修（Cat A／Cat B）競爭租戶，璞石可同時扮演「房東端 Cat A／樣板層」與「租戶端 Cat B」承包者；而其不動產業務若持有或代管商辦，應預期租金議價力下降。
2. **台北 fit-out 單價已站上亞太中高段**：C&W 2026 台北 145 USD psf，高於新加坡 140 [TC-04]。推論：出海新加坡不能以「台灣較便宜」為主賣點；應以設計品質、華語服務、跟隨台商客戶為主。
3. **東南亞／印度是「低單價、高量、高空置」組合**：雅加達 58、胡志明市 61、吉隆坡 80、曼谷 91 USD psf [TC-11][TC-06]；同時曼谷 CBD Grade A 空置 21.9% [TC-91]、雅加達 Grade A 出租率僅 67% [TC-90]、吉隆坡 14.8% 且年底再增 264 萬 sq ft [TC-89]。推論：這些市場的 fit-out 機會多來自「遷移升級（flight-to-quality）」與新大樓招租，而非淨增量；台灣團隊外派成本難吸收，宜採「設計輸出＋在地施工夥伴」。
4. **飯店是較明確的跨境題材**：APEC 管線 2,506 案、奢華級 404 案創紀錄，越南 258 案、曼谷 68 案居前 [TC-99][TC-100]；香港五星級公共區 fit-out 達 HK$24,000 以上／m² [TC-55]。推論：飯店公共區與客房設計（設計費按 % 計）單案價值高，適合以設計服務切入越南、泰國，而非承攬施工。
5. **毛利基準**：日本商空展示雙雄營業利益率 5.6–7.9%（計算值）[TC-103][TC-104]；中國公裝龍頭毛利率約 12–13% 且下滑、營收雙雙衰退 [TC-108][TC-110]。推論：大型商空承包本質是低毛利、規模型生意；中型集團應以設計費（台灣行情 5–20% 工程款 [TC-61][TC-63]，低信心）＋家具零售（FF&E 配套）提高單案毛利，而非追求工程量。
6. **半導體外溢屬另一個量級、另一種能力**：亞翔、漢唐 2026 前 8 月營收各約 650–680 億元、年增 60–70% [TC-112]。推論：廠務無塵室 fit-out 需機電、潔淨室資格，與室內設計能力不重疊；璞石可切入的是其「周邊」——科技廠辦公區、員工宿舍、接待中心（宜蘭／北部科技聚落），而非無塵室本體。
7. **成本走勢溫和**：JLL 亞太 2–5%（當地幣）[TC-24]、T&T 全球 3% [TC-30]；可按 3–5% 年調幅做報價敏感度分析。台北單年 +32% [TC-04] 須以自身新台幣報價紀錄驗證是否為實際工料上漲（G-03）。
8. **資料不足不可下結論**：除香港外的飯店、零售 fit-out 單價；台灣非廠務商空公司營收；台灣以外市場設計費——皆無資料，跨境評分不宜只依本筆記。

---

## 6. 矛盾表與缺口表

### 6.1 矛盾表（差異 >30%；不取平均）

> 診斷用面積換算：1 m² = 10.7639 sq ft；1 坪 ≈ 35.583 sq ft，僅用於判斷差距，不作紀錄值。幣別不同者不做換匯比較。

| # | 指標 | 來源 1 | 來源 2 | 差異 | 差異原因診斷 | 裁決 |
|---|---|---|---|---|---|---|
| C-01 | 東京辦公 fit-out | C&W 2025：195 USD/sq ft [TC-11]（診斷換算約 2,099 USD/m²） | T&T 2025 高規格：4,619 USD/m² [TC-27] | T&T 約為 C&W 的 2.2 倍 | **等級**（高規格 vs 平均）＋**範圍**（T&T 含 CAT A＋CAT B、活動家具、AV、專業費 [TC-28]；C&W 範圍含家具、機電、營建、AV/IT [TC-19] 但未確認是否含專業費）＋試配面積不同 | 並列；城市比較用 C&W，高端定位用 T&T |
| C-02 | 香港辦公 fit-out | C&W 2026：160 USD/sq ft [TC-04]（約 1,722 USD/m²） | T&T 2025 頂級：4,575 USD/m² [TC-27] | 約 2.7 倍 | 同 C-01；版本年不同 | 並列 |
| C-03 | 香港 T&T 跨年 | T&T 2025：4,575 **USD**/m² [TC-27] | T&T 2026：31,231 **HKD**/m² [TC-32] | 幣別不同 | 計價幣別改變；須中央換匯後判定 | 待中央換算 |
| C-04 | 孟買辦公 fit-out | C&W 2026：約 73 USD/sq ft [TC-07] | Knight Frank 2026 三城中規格：449 USD/m² [TC-33]（約 41.7 USD/sq ft） | 約 1.75 倍 | 城市（KF 三城平均）＋等級（中規格）＋範圍（家具／AV 是否計入未知） | 並列 |
| C-05 | 班加羅爾辦公 fit-out | C&W 2026：65–69 USD/sq ft [TC-07] | T&T 2025 低規格：531 USD/m² [TC-27]（約 49.3 USD/sq ft） | C&W 高約 32–40% | 等級＋版本年 | 並列；T&T 低規格作「最低門檻」 |
| C-06 | 台北辦公 fit-out（同出版者跨年） | C&W 2025：110 USD/sq ft [TC-04] | C&W 2026：145 USD/sq ft [TC-04] | +31.8% | 可能：工料上漲／新台幣匯率／2026 版 all-in 口徑擴充；搜尋結果未揭露當地幣變動 | 並列；「原因未明」 |
| C-07 | 台北長期 | C&W 2019：70 USD/sq ft [TC-15] | C&W 2026：145 USD/sq ft [TC-04] | 約 2.07 倍 | 方法論變動＋通膨＋匯率 | 2019 值僅作歷史參考 |
| C-08 | 首爾辦公 fit-out（第三方） | spacelogin 基本型 120–160 萬韓元／坪 [TC-36] | interiorcnote 輕度 80–150 萬韓元／坪（不含 VAT、家具、IT、設計費）[TC-37] | 下限差 50% | 範圍（稅、家具、設計費）＋行銷口徑 | 皆低信心 |
| C-09 | JLL 亞太復原成本 | 平均 235 USD/m² [TC-25] | 區間 245–425 USD/m² [TC-25] | 平均低於下限 | 疑為摘要錯誤 | 不採用 |
| C-10（<30%，備註） | JLL 2025 亞太平均 | 1,460 USD/m² [TC-22] | 1,524 USD/m² [TC-23] | 約 4% | 樣本與基準期不同 | 並列 |
| C-11 | 東京 Grade A 空置率 2026 Q2 | Colliers 1.3%（都心五區）[TC-67] | Savills 0.6%（C5W）（搜尋摘要，URL 未對應） | Colliers 高約 117% | Grade A 定義與樣本不同；Savills 值信心低 | 採 Colliers（有 URL）；Savills 列參考 |
| C-12 | 新加坡 Grade A 空置率 2026 Q2 | JLL CBD Grade A（不含新竣工）5.6% [TC-68] | CBRE 核心 CBD Grade A 3.3% [TC-69] | 約 70% | 地理範圍（CBD vs 核心 CBD）、新竣工是否計入 | 並列；跨市場比較時統一用同一家 |
| C-13 | 台北辦公 fit-out：國際指南 vs 本地行情 | C&W 2026：145 USD/sq ft [TC-04]（面積換算約 5,160 USD/坪，診斷用） | PRO360 台北：50,000–80,000 元／坪 [TC-61] | 幣別不同，須中央換匯；預期差距 >30% | 範圍（C&W 含家具、機電、AV/IT、國際企業甲級辦公規格；本地統計多為中小企業室內工程、多不含家具與 AV）＋樣本（平台案件） | 並列；國際客戶用 C&W、本地中小客戶用本地行情 |
| C-14 | 首爾辦公空置率 2026 Q2 | CBRE A 級三大圈 4.2% [TC-78] | 알스퀘어 全體 6.5% [TC-81]；C&W A 級 5.8% [TC-79] | 4.2 vs 6.5 約 55% | 範圍（A 級三大圈 vs 全體）；CBD 數字亦不同（C&W 9.0% vs 알스퀘어 7.3%） | 並列；同機構看趨勢 |
| C-15 | 台北 A 辦空置率 | 仲量 2026 Q3 核心商業區 5.8% | 戴德梁行 2026 Q1 A 辦 9.0%；高力 Q2 A 級 7.17% | 9.0 vs 5.8 約 55% | 範圍（核心商業區 vs A 辦）＋時點（Q1 vs Q3）；三筆皆搜尋摘要（低） | 並列，皆低信心 |
| C-16 | 台北 A 辦空置率預測 | CBRE：2028 年近 25% [TC-72] | 仲量：高峰 10–15% [TC-73] | 約 1.7–2.5 倍 | 預測方法、市場範圍、去化假設不同；CBRE 為 2025 年報導 | 並列；屬預測非現況 |
| C-17 | 上海 2026 Q2 新供給 | 仲量：2 案 13.5 萬 m² [TC-82] | 另一機構：3 案 39.1 萬 m² [TC-83] | 約 2.9 倍 | 項目納入標準（是否含超甲級、自用、跨區）不同；另 TC-82 之年份由摘要判定（同批結果中另有 2025-07 中新社同主題報導），**存在年份誤植風險** | 並列；空置率（23.5% vs 24.3%）差距小 |
| C-18（<30%，備註） | 北京 2026 Q2 空置率 | 仲量 14.7% [TC-84] | 高力 17.5% [TC-85]；莱坊 15.9% [TC-86] | 最大約 19% | 是否含自用項目等口徑 | 並列 |
| C-19（<30%，備註） | 香港 Grade A 空置率 2026 Q2 | Colliers 16.1% [TC-70] | JLL 13.1% [TC-71] | 約 23% | 樣本定義 | 並列 |
| C-20 | 亚厦毛利率 | 前三季 14.63% | 同花順 2025 年 15.61%；2025 中報裝飾業 11.39% | 15.61 vs 11.39 約 37% | 範圍（綜合 vs 裝飾業別）＋期間（中報／前三季／年報） | 並列；以年報分行業表為準（G-11） |
| C-21 | 丹青社「過去最高」營收期別 | 2025/1 期 918.58 億日圓 [TC-104] | 「過去最高」列 1,072.22 億日圓 [TC-104] | 約 17% | 期別不同（推定後者為 2026/1 期）；note.com 稱 2024 年度 918 億為當時最高 [TC-107] | 2025/1 期採 918.58 億；1,072 億待決算短信確認 |
| C-22（內部不一致） | 雅加達年底空置率預測 | 31% [TC-90] | 32% [TC-90] | — | 同頁兩版本 | 皆列 |

### 6.2 缺口表

| # | 找不到的項目 | 嘗試過的搜尋 | 狀態 | 建議取得方式 |
|---|---|---|---|---|
| G-01 | C&W 2026 亞太版完整城市表（大阪、深圳、河內；首爾／上海／北京之正確欄位；雅加達、胡志明市 2026 值） | Q1、Q4、Q8、Q9、Q11 | 未解 | 下載 C&W 2026 亞太 PDF（TC-01） |
| G-02 | 首爾 C&W 官方 fit-out 數字 | Q10（Q13 未執行） | 未解 | C&W 韓國 2025 報告（TC-16）及 2026 韓國版 |
| G-03 | 台北 110→145 的新台幣變動與原因 | Q7 | 未解 | C&W 台灣；比對璞石自身報價 |
| G-04 | AECOM《Asia Construction & Cost Handbook》城市費率 | Q3、Q16 | 未解（兩度未被索引） | 向 AECOM 亞洲索取 |
| G-05 | Arcadis、RLB 城市飯店／零售 fit-out 費率（香港以外） | Q16、Q17、Q28 | 部分（香港飯店已補；RLB 有章節未擷取） | 下載 RLB Riders Digest 2026 新加坡版（TC-58）、2026 Asia 表（TC-59）；Arcadis 東南亞 QCC |
| G-06 | 零售、餐飲 fit-out 單價（台灣以外） | Q16、Q28 | 未解 | AECOM／Arcadis shop fit-out 列；C&W 零售 fit-out 指南（目前僅見美國版 TC-47） |
| G-07 | 甲級辦公空置率 | Q20、Q21、Q23、Q24、Q25、Q29 | **大致補齊**；缺大阪、河內；印度、孟買、班加羅爾為低信心 | JLL／CBRE India Q2 2026 原稿 |
| G-08 | 亞太飯店管線 | Q22 | **已補（APEC）**；缺中國管線、STR 開業數 | Lodging Econometrics China 季報 |
| G-09 | 資料中心外溢 fit-out | 未直接搜尋 | 部分（台灣廠務商營收代替） | C&W／T&T 資料中心成本指南全文 |
| G-10 | 乃村、丹青社營收與利潤 | Q18 | **已補**；スペース、船場仍缺 | 各社決算短信 |
| G-11 | 金螳螂、亚厦營收與毛利 | Q19 | **已補**；亚厦 2025 年報分行業毛利率仍缺 | 巨潮資訊網年報 |
| G-12 | 台灣非廠務商空設計施工業者營收；ISG、Space Matrix、Unispace、Gammon | Q26（僅取得廠務商） | 未解 | 公開資訊觀測站、Companies House（ISG） |
| G-13 | 商空設計費（台灣以外 11 市場） | Q27（僅台灣） | 部分 | 各地設計師公會收費標準、RLB／AECOM 專業費章節 |
| G-14 | 混合辦公對 fit-out 面積量的量化影響 | 未搜尋 | 未解 | JLL／CBRE 占用者調查 |
| G-15 | 零售／餐飲開店數（各市場） | 未搜尋 | 未解 | CBRE 零售季報、各國餐飲公會 |

---

## 7. 關鍵指標 CSV

```csv
market,metric,value,unit,year,source_id,source_url,definition,confidence
TW,辦公fit-out平均成本（台北）,145,USD/sq ft,2026,TC-04,https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific,C&W亞太2026版城市平均；價格基準2025-12,high
TW,辦公fit-out平均成本（台北）,110,USD/sq ft,2025,TC-05,https://www.cushmanwakefield.com/en/south-korea/news/2026/04/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific,C&W亞太2025版城市平均（2026新聞稿比較值）,high
TW,辦公fit-out成本（台北）,70,USD/sq ft,2019,TC-15,https://www.taipeitimes.com/News/biz/archives/2019/11/05/2003725245,2019年C&W調查；口徑可能與2026不同,medium
TW,辦公裝潢報價統計（台北）,50000-80000,元/坪,2026,TC-61,https://www.pro360.com.tw/price/office_design,PRO360平台報價統計；連工帶料,low
TW,餐飲裝修行情（咖啡廳／精品餐廳）,10-20／20-35,萬元/坪,2026,TC-60,https://howroom.ai/posts/a/commercial-space-renovation-guide,行銷文章；原文未標幣別,low
TW,設計費占工程款,5-20,%,2026,TC-63,https://www.dahuandesign.com/faq/interior-design-cost/,設計公司FAQ；監工費另計5-10%,low
TW,商業空間設計費,1500-4500,元/坪,2026,TC-65,https://into-atelier.com.tw/charge/,台中設計公司收費標準,low
TW,A辦空置率預測（2028）,近25,%,2025,TC-72,https://money.udn.com/money/story/5621/9196803,CBRE預測台北A辦空置率2028年高點；預測值,medium
TW,A辦新供給（2021-2030）,44,萬坪,2026,TC-73,https://house.ettoday.net/news/3238017,仲量聯行統計台北市A辦供給,medium
TW,南山信義四棟商辦面積,12.2,萬坪,2026,TC-74,https://www.businessinsider.tw/article/2424,A26（2027）與A21（2028）接力完工,medium
TW,亞翔營收（2026前8月）,679.04,億新台幣,2026,TC-112,https://money.udn.com/money/story/5607/9747158,年增63.4%；無塵室機電,medium
TW,漢唐營收（2026前8月）,656.94,億新台幣,2026,TC-112,https://money.udn.com/money/story/5607/9747158,年增71.6%；台積電無塵室統包,medium
JP,辦公fit-out平均成本（東京）,215,USD/sq ft,2026,TC-04,https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific,C&W亞太2026版；亞太最高,high
JP,辦公fit-out平均成本（東京）,195,USD/sq ft,2025,TC-11,https://www.retalkasia.com/news/2025/03/06/office-fit-out-costs-asia-pacific-continue-rise-cushman-wakefield/1741232445,C&W亞太2025版；2025版最高,high
JP,辦公fit-out高規格成本（東京）,4619,USD/m2,2025,TC-27,https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2025/global-office-fit-out-costs,T&T高規格；CAT A+CAT B含家具AV專業費；基準2025Q1,medium
JP,Grade A空置率（東京都心五區）,1.3,%,2026,TC-67,https://www.colliers.com/en-jp/research/tokyo-office-market-q2-2026,Colliers 2026Q2；新供給31300坪、淨去化35400坪,medium
JP,乃村工藝社營收,1626.79,億日圓,2026,TC-103,https://kabutan.jp/stock/finance?code=9716,2026年2月期；營業利益128.18億日圓,medium
JP,乃村工藝社營業利益率,7.9,%,2026,TC-103,https://kabutan.jp/stock/finance?code=9716,計算值＝營業利益÷營收；2026年2月期,medium
JP,丹青社營收,918.58,億日圓,2025,TC-104,https://kabutan.jp/stock/finance?code=9743,2025年1月期；營業利益51.47億日圓（計算值利益率5.6%）,medium
KR,辦公fit-out平均成本（首爾）,130,USD/sq ft,2026,TC-02,https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office/28-29/,C&W亞太2026版表格擷取（欄位未確認；約值）,low
KR,辦公裝修第三方行情基本型（首爾）,120-160,萬韓元/坪,2026,TC-36,https://spacelogin.co.kr/2026-%EC%82%AC%EB%AC%B4%EC%8B%A4-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4-%EC%97%85%EC%B2%B4-%EB%B9%84%EA%B5%90-%EA%B0%80%EC%9D%B4%EB%93%9C/,平台業者行情；中階160-200；高階200以上,low
KR,承包商預期6個月內小幅漲價比例,90,%,2026,TC-35,https://www.kjob.news/news/501752,C&W韓國2026版承包商調查；驅動：人工與關稅,medium
KR,A級辦公空置率（首爾三大圈）,4.2,%,2026,TC-78,https://view.asiae.co.kr/article/2026072717565427925,CBRE Korea 2026Q2；新租賃143881平方公尺,medium
KR,A級辦公空置率（首爾）,5.8,%,2026,TC-79,https://www.kcenews.kr/9000,C&W 2026Q2；2021Q3以來最高,medium
SG,辦公fit-out平均成本（新加坡）,140,USD/sq ft,2026,TC-04,https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific,C&W亞太2026版；與2025大致持平,high
SG,CBD Grade A空置率,5.6,%,2026,TC-68,https://realestateasia.com/commercial-office/news/singapore-cbd-office-vacancy-hits-nine-quarter-low,JLL 2026Q2；不含新竣工；九季新低,medium
SG,核心CBD Grade A空置率,3.3,%,2026,TC-69,https://ohsem.me/2026/10/singapore-grade-a-office-market-posts-strongest-quarterly-rental-growth-since-2022-as-supply-constraints-intensify/,CBRE 2026Q2（Q3降至2.6%）,medium
HK,辦公fit-out平均成本（香港）,160,USD/sq ft,2026,TC-04,https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific,C&W亞太2026版；大中華最高、亞太第8,high
HK,辦公fit-out頂級成本（香港）,4575,USD/m2,2025,TC-27,https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2025/global-office-fit-out-costs,T&T premium,medium
HK,辦公fit-out頂級平均成本（香港）,31231,HKD/m2,2026,TC-32,https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026-us/hong-kong,T&T 2026 premium平均,medium
HK,飯店公共區fit-out（五星）,24000以上,HKD/m2,2025,TC-55,https://www.arcadis.com/contentassets/934a2cbf81254a22b8d893e40f92c781/2025constructioncosthandbook_china_hongkong.pdf?rev=1b304935c6ec425db127792f5c3703b3,Arcadis 2025手冊4Q2024價位；四星17000-24000；三星11500-17000,medium
HK,飯店客房fit-out（五星）,15500以上,HKD/m2,2025,TC-55,https://www.arcadis.com/contentassets/934a2cbf81254a22b8d893e40f92c781/2025constructioncosthandbook_china_hongkong.pdf?rev=1b304935c6ec425db127792f5c3703b3,Arcadis 2025手冊；四星11500-15000；三星9500-11200,medium
HK,Grade A空置率,16.1,%,2026,TC-70,https://realestateasia.com/commercial-office/news/hong-kong-grade-office-vacancy-rate-falls-161-in-q2,Colliers 2026Q2；淨承租864000 sq ft；CBD 10.2%,medium
HK,Grade A空置率,13.1,%,2026,TC-71,https://research.jllapsites.com/appd-market-report/q2-2026-office-hong-kong/,JLL 2026年6月；Q2淨去化492000 sq ft,medium
CN,辦公fit-out平均成本（上海）,96,USD/sq ft,2026,TC-02,https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office/28-29/,C&W亞太2026版表格擷取（約值；欄位未確認）,low
CN,辦公fit-out平均成本（北京）,95,USD/sq ft,2026,TC-02,https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office/28-29/,C&W亞太2026版表格擷取（約值；欄位未確認）,low
CN,辦公裝修全包行情（上海）,800-1500,RMB/m2,2026,TC-39,http://lingqisj.com/gsxw/3761.html,本地裝修公司行銷文章,low
CN,甲級辦公空置率（上海）,23.5,%,2026,TC-82,https://www.sohu.com/a/1055935733_655634,仲量聯行Q2；年份由搜尋摘要判定,low
CN,甲級辦公空置率（北京）,14.7,%,2026,TC-84,https://www.guandian.cn/article/20260728/578007.html,仲量聯行2026Q2；不含自用項目；新供給0,medium
CN,甲級辦公空置率（深圳）,22.7,%,2026,TC-88,https://m.hibor.com.cn/wap_detail.aspx?id=f6ad484404e17061441e1ebf1d8e9530,莱坊2026Q2；淨吸納102492平方公尺,medium
CN,金螳螂營收,173.10,億人民幣,2025,TC-108,http://basic.10jqka.com.cn/002081/field.html,2025年；綜合毛利率12.67%；裝飾業毛利率12.42%,medium
CN,亚厦股份營收,91.18,億人民幣,2025,TC-110,https://static.weeklyonstock.com/26/0427/AB2622075859419.html,2025年報；年減24.87%；歸母淨利3.30億,medium
MY,辦公fit-out平均成本（吉隆坡）,80,USD/sq ft,2026,TC-06,https://www.cushmanwakefield.com/en/thailand/insights/office-fit-out-cost-guide?sort=latest_update,C&W 2026城市排名（泰國頁）,medium
MY,辦公空置率（吉隆坡）,14.8,%,2026,TC-89,https://realestateasia.com/commercial-office/news/kuala-lumpur-office-vacancy-falls-148-in-q2,JLL 2026Q2；是否限Grade A未明；年底恐升至16.4%,medium
TH,辦公fit-out平均成本（曼谷）,91,USD/sq ft,2026,TC-06,https://www.cushmanwakefield.com/en/thailand/insights/office-fit-out-cost-guide?sort=latest_update,C&W 2026城市排名（泰國頁）,medium
TH,CBD Grade A空置率（曼谷）,21.9,%,2026,TC-91,https://www.cushmanwakefield.com/en/thailand/insights/bangkok-office-market-overview,C&W 2026Q2；2023Q1以來最低,medium
TH,飯店管線城市第一（曼谷）,68,案,2026,TC-100,https://lodgingeconometrics.com/record-projects-apec-hotel-pipeline-q1-2026/,LE 2026Q1；16267房,medium
VN,辦公fit-out平均成本（胡志明市）,61,USD/sq ft,2026,TC-06,https://www.cushmanwakefield.com/en/thailand/insights/office-fit-out-cost-guide?sort=latest_update,C&W城市排名；年份標示不明確,medium
VN,核心區Grade A出租率（胡志明市）,89.8,%,2026,TC-93,https://www.cushmanwakefield.com/en/vietnam/news/2026/09/ho-chi-minh-city-office-market-approaches-balance-as-flight-to-quality-continues-to-shape-demand,C&W 2026Q2；Q2無新供給,medium
VN,飯店管線（越南）,258,案,2026,TC-100,https://lodgingeconometrics.com/record-projects-apec-hotel-pipeline-q1-2026/,LE 2026Q1；87077房；APEC第二,medium
ID,辦公fit-out平均成本（雅加達）,58,USD/sq ft,2025,TC-11,https://www.retalkasia.com/news/2025/03/06/office-fit-out-costs-asia-pacific-continue-rise-cushman-wakefield/1741232445,C&W亞太2025版；全區最低,high
ID,Grade A出租率（雅加達）,67,%,2026,TC-90,https://research.jllapsites.com/appd-market-report/q1-2026-office-jakarta/,JLL 2026Q1；2026無新竣工,medium
PH,辦公fit-out平均成本（馬尼拉）,105,USD/sq ft,2026,TC-06,https://www.cushmanwakefield.com/en/thailand/insights/office-fit-out-cost-guide?sort=latest_update,C&W 2026城市排名（泰國頁）,medium
PH,辦公復原成本平均（馬尼拉）,20,USD/sq ft,2026,TC-01,https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office,C&W reinstatement平均（區間15-25）；表格擷取,low
PH,辦公空置率（馬尼拉）,13.8,%,2026,TC-92,https://realestateasia.com/commercial-office/news/manila-q2-office-absorption-reaches-40400-sqm-vacancy-falls,2026Q2；去化40400平方公尺；是否Grade A未明,medium
IN,辦公fit-out成本（孟買）,73,USD/sq ft,2026,TC-07,https://realtynmore.com/competitive-fit-out-market-cushman-wakefield/,C&W 2026協作式混合辦公；印度最高,high
IN,辦公fit-out成本（孟買）,6567,INR/sq ft,2026,TC-09,https://cw-prod-apacgws-a-cd.cushwake.com/en/india/insights/office-fit-out-cost-guide,C&W印度頁；約值,medium
IN,辦公fit-out成本（德里首都圈/班加羅爾/海德拉巴/清奈/浦那）,65-69,USD/sq ft,2026,TC-08,https://ianslive.in/india-remains-asia-pacifics-most-cost-competitive-office-fit-out-market-report--20260326105534,C&W 2026；城市未單列,medium
IN,辦公fit-out低規格成本（班加羅爾）,531,USD/m2,2025,TC-27,https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2025/global-office-fit-out-costs,T&T low specification,medium
IN,辦公fit-out中規格平均（三城）,449,USD/m2,2026,TC-33,https://realtynmore.com/asia-pacific-knight-frank-report,Knight Frank；班加羅爾+孟買+德里首都圈平均,medium
IN,全國前7城辦公空置率,14.5,%,2026,TC-95,https://www.crematrix.com/blog/india-office-space-trends-2026-rents-up-vacancy-down/,2026Q2；5年新低；URL對應推定,low
IN,飯店管線（印度）,1033,案,2026,TC-99,https://lodgingeconometrics.com/global-insights/,LE 2026Q2；137601房；APEC第一,medium
APAC,JLL辦公fit-out平均,1460,USD/m2,2025,TC-22,https://irei.com/news/average-fit-out-costs-for-offices-lowest-in-asia-pacific-compared-to-other-regions-jll/,JLL全球指南2025（2025-04）；全球1830,medium
APAC,JLL適中風格中等品質辦公平均,1524,USD/m2,2025,TC-23,https://www.jll.com/en-in/insights/apac-fit-out-cost-guide-2025,JLL亞太指南基準2025Q1；全球1949,medium
APAC,JLL辦公fit-out平均,1550,USD/m2,2026,TC-24,https://www.jll.com/en-in/guides/apac-fit-out-costs-guide,JLL亞太2026；27城市；當地幣年增2-5%,medium
APAC,C&W承包商預期2026市況改善比例,70,%,2026,TC-17,https://www.malaymail.com/news/money/mediaoutreach/2026/03/26/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific/456444,C&W 2026 Contractor Sentiment Survey,medium
APAC,飯店建設管線（不含中國）,2506,案,2026,TC-99,https://lodgingeconometrics.com/global-insights/,LE 2026Q2；452972房；案數年增17%,medium
APAC,飯店建設管線（不含中國）,2387,案,2026,TC-100,https://lodgingeconometrics.com/record-projects-apec-hotel-pipeline-q1-2026/,LE 2026Q1；442973房；奢華級404案創紀錄,high
GLOBAL,T&T全球fit-out年度成本漲幅,3,%,2026,TC-30,https://www.turnerandtownsend.com/insights/global-office-fit-out-cost-guide-2026/,T&T 2026；58市場,medium
GLOBAL,JLL全球辦公fit-out平均,2150,USD/m2,2026,TC-26,https://www.joneslanglasalle.com.cn/zh-cn/guides/global-office-fit-out-costs-guide,仲量聯行2026全球指南中文版,medium
GLOBAL,全球新開幕飯店（2025）,2438,家,2025,TC-98,https://lodgingeconometrics.com/global-hotel-construction-pipeline-q2-2026/,LE；332699房；2026預測2742家,medium
```

（共 74 列資料。confidence 欄 high／medium／low 對應正文 高／中／低。）

---

## 8. 來源清單

> 讀取方式：全部為「搜尋結果內容」（WebFetch 不可用；未開啟原始全文）。語言：英＝英文、簡中、繁中、韓、日。標「（推定）」者：URL 出現於搜尋結果，但該數字與 URL 的對應由摘要推定，引用時信心一律「低」。

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
| TC-17 | Contractor confidence rises amid strengthening office demand across Asia Pacific（70% expect improved conditions） | Malay Mail／Media OutReach | 2026 | 英 | https://www.malaymail.com/news/money/mediaoutreach/2026/03/26/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific/456444 | 搜尋結果內容 |
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
| TC-34 | China & Hong Kong 2025 Construction Cost Handbook（media.arcadis.com 版） | Arcadis Hong Kong Limited | 2025 | 英 | https://media.arcadis.com/-/media/project/arcadiscom/com/perspectives/asia/publications/cch/2025/2025-cnhk-cost-handbookfinal-online.pdf?rev=1b304935c6ec425db127792f5c3703b3 | 搜尋結果內容 |
| TC-35 | 2026 사무실 인테리어 비용 상승 전망: 응답 시공사 90%가 가격 인상 예측 | 전국인력신문（kjob.news） | 2026 | 韓 | https://www.kjob.news/news/501752 | 搜尋結果內容 |
| TC-36 | 2026 사무실 인테리어 업체 비교 가이드 | 스페이스로그인（spacelogin） | 2026 | 韓 | https://spacelogin.co.kr/2026-%EC%82%AC%EB%AC%B4%EC%8B%A4-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4-%EC%97%85%EC%B2%B4-%EB%B9%84%EA%B5%90-%EA%B0%80%EC%9D%B4%EB%93%9C/ | 搜尋結果內容 |
| TC-37 | 사무실 인테리어 비용, 평당 얼마가 현실적인가 — 규모별 정리 | 오피스 인테리어 컨설팅 랩（interiorcnote） | 2026（推定） | 韓 | https://interiorcnote.com/%EC%82%AC%EB%AC%B4%EC%8B%A4-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4-%EB%B9%84%EC%9A%A9-%ED%8F%89%EB%8B%B9-%EC%96%BC%EB%A7%88%EA%B0%80-%ED%98%84%EC%8B%A4%EC%A0%81%EC%9D%B8%EA%B0%80-%EA%B7%9C/ | 搜尋結果內容 |
| TC-38 | 사무실 인테리어 비용 가이드 2026 | ssjum.com | 2026 | 韓 | https://ssjum.com/interior-office.html | 搜尋結果內容 |
| TC-39 | 上海办公室装修每平米多少钱?2026最新报价清单及优势全解析 | 领企装修公司 | 2026 | 簡中 | http://lingqisj.com/gsxw/3761.html | 搜尋結果內容 |
| TC-40 | 北京办公室装修公司｜办公室设计多少钱一平米，装修多少钱一平米 | 网易（163.com） | 2026（推定） | 簡中 | https://c.m.163.com/news/a/KPJJ424N0556AOIS.html | 搜尋結果內容 |
| TC-41 | Office Fit Out Costs Continue to Rise Across Asia Pacific Albeit at Much Slower Rate | Cushman & Wakefield Greater China | 2024 | 英 | https://www.cushmanwakefield.com/en/greater-china/news/2024/05/office-fit-out-costs-continue-to-rise-across-asia-pacific-albeit-at-much-slower-rate | 搜尋結果內容 |
| TC-42 | APAC Office Fit Out Cost Guide 2024 – Page 8-9 | Cushman & Wakefield | 2024 | 英 | https://cushwake.cld.bz/apac-office-fit-out-cost-guide-2024/8-9/ | 搜尋結果內容 |
| TC-43 | 쿠시먼앤드웨이크필드 코리아 '2026 오피스 시장 세미나' 성료 | 뉴스와이어（newswire.co.kr） | 2026 | 韓 | https://www.newswire.co.kr/newsRead.php?no=1032661&sourceType=rss | 搜尋結果內容 |
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
| TC-55 | China & Hong Kong 2025 Construction Cost Handbook（arcadis.com 版，含 FIT-OUT COSTS FOR HONG KONG） | Arcadis Hong Kong Limited | 2025 | 英 | https://www.arcadis.com/contentassets/934a2cbf81254a22b8d893e40f92c781/2025constructioncosthandbook_china_hongkong.pdf?rev=1b304935c6ec425db127792f5c3703b3 | 搜尋結果內容 |
| TC-56 | Quarterly Construction Cost Review China and Hong Kong（2025 Q2） | Arcadis | 2025 | 英 | https://media.arcadis.com/-/media/project/arcadiscom/com/perspectives/asia/publications/qcc/2025/cnhk-qcc-2025-q2.pdf?rev=8522078780d24e89a3915fc0a67c348e | 搜尋結果內容 |
| TC-57 | Navigating Uncertainty – International Construction Costs 2025 | Arcadis | 2025 | 英 | https://www.arcadis.com/contentassets/9c69333169054e2ba8bb8fabf1a80df9/international-construction-costs-2025.pdf | 搜尋結果內容 |
| TC-58 | 2026 Riders Digest Singapore Edition | Rider Levett Bucknall | 2026 | 英 | https://www.rlb.com/wp-content/uploads/sites/5/2026/07/RLB-Riders-Digest-2026_Singapore_ecopy-20260707_FINAL.pdf | 搜尋結果內容 |
| TC-59 | Melbourne, Australia Riders Digest 2026 54th Edition（含 Asia 表） | Rider Levett Bucknall | 2026 | 英 | https://www.rlb.com/wp-content/uploads/sites/1/2026/01/Riders-Digest-Melbourne-2026.pdf | 搜尋結果內容 |
| TC-60 | 商業空間裝潢全攻略 2026：設計流程、法規送審與費用行情 | howroom | 2026 | 繁中 | https://howroom.ai/posts/a/commercial-space-renovation-guide | 搜尋結果內容 |
| TC-61 | 辦公室裝潢費用一坪多少？2026最新行情與省錢妙招 | PRO360達人網 | 2026 | 繁中 | https://www.pro360.com.tw/price/office_design | 搜尋結果內容 |
| TC-62 | 辦公室設計怎麼規劃才不後悔？從風格到預算，2026 完整拆解（推定） | rinzh | 2026 | 繁中 | https://rinzh.com/interior-design/commercial-space/office-design/officecp/ | 搜尋結果內容 |
| TC-63 | 室內設計費用、裝潢費用、監造費怎麼計算？ | 大桓設計（Dahuan） | 2026（推定） | 繁中 | https://www.dahuandesign.com/faq/interior-design-cost/ | 搜尋結果內容 |
| TC-64 | 室內設計費用有哪 4 筆？行情與計算方式 | 好感生活提案 | 2026（推定） | 繁中 | https://goodlivingnotes.com/interior-design-price/ | 搜尋結果內容 |
| TC-65 | 台中室內設計費 – 介入空間設計收費 | 介入空間設計 | 2026（推定） | 繁中 | https://into-atelier.com.tw/charge/ | 搜尋結果內容 |
| TC-66 | 收費標準 – 桃園優德室內裝修設計 | 優德室內裝修設計 | 2026（推定） | 繁中 | https://ude-design.com.tw/fee | 搜尋結果內容 |
| TC-67 | Tokyo Office Market Review and Outlook Q2 2026 | Colliers Japan | 2026 | 英 | https://www.colliers.com/en-jp/research/tokyo-office-market-q2-2026 | 搜尋結果內容 |
| TC-68 | Singapore CBD office vacancy hits a nine-quarter low | Real Estate Asia | 2026 | 英 | https://realestateasia.com/commercial-office/news/singapore-cbd-office-vacancy-hits-nine-quarter-low | 搜尋結果內容 |
| TC-69 | Singapore Grade A Office Market Posts Strongest Quarterly Rental Growth Since 2022 As Supply Constraints Intensify | ohsem.me | 2026 | 英 | https://ohsem.me/2026/10/singapore-grade-a-office-market-posts-strongest-quarterly-rental-growth-since-2022-as-supply-constraints-intensify/ | 搜尋結果內容 |
| TC-70 | Hong Kong Grade A office vacancy rate falls to 16.1% in Q2 | Real Estate Asia | 2026 | 英 | https://realestateasia.com/commercial-office/news/hong-kong-grade-office-vacancy-rate-falls-161-in-q2 | 搜尋結果內容 |
| TC-71 | Hong Kong – Q2 2026 Office | JLL | 2026 | 英 | https://research.jllapsites.com/appd-market-report/q2-2026-office-hong-kong/ | 搜尋結果內容 |
| TC-72 | CBRE：明年底北市商辦新供給高峰 2028年 A 辦空置率攀近25%高點 | 經濟日報（money.udn.com） | 2025 | 繁中 | https://money.udn.com/money/story/5621/9196803 | 搜尋結果內容 |
| TC-73 | 昔日「黑鄉」領頭 北市將湧44萬坪A辦供給 | ETtoday 房產雲 | 2026 | 繁中 | https://house.ettoday.net/news/3238017 | 搜尋結果內容 |
| TC-74 | 搶當信義區A辦最大房東！南山A21、A26接力完工 租金衝每坪5000元 | Business Insider Taiwan | 2026 | 繁中 | https://www.businessinsider.tw/article/2424 | 搜尋結果內容 |
| TC-75 | AI趨勢下科技業撐盤 新商辦大樓有底氣（推定：台北空置率摘要候選來源） | 中時新聞網 | 2026 | 繁中 | https://www.chinatimes.com/realtimenews/20260502000003-260410 | 搜尋結果內容 |
| TC-76 | 7.5萬坪新商辦殺到！房東不讓利還漲租 市場能撐多久？（推定） | 自由時報地產天下 | 2026 | 繁中 | https://estate.ltn.com.tw/article/28255 | 搜尋結果內容 |
| TC-77 | 台北商辦供給大增 2026 轉為「房客市場」 專家：高價大樓恐面臨壓力測試（推定） | 富比士地產王 | 2026 | 繁中 | https://www.fbs168.com/news/8499 | 搜尋結果內容 |
| TC-78 | 서울 오피스 신규 임대차 규모, 1년여 만에 최대…공실률은 4.2%로 상승 | 아시아경제（asiae） | 2026 | 韓 | https://view.asiae.co.kr/article/2026072717565427925 | 搜尋結果內容 |
| TC-79 | 서울 A급 오피스 공실률 5.8%, 5년 만에 최고치…임대료는 견조한 상승세 | kcenews | 2026 | 韓 | https://www.kcenews.kr/9000 | 搜尋結果內容 |
| TC-80 | 서울 오피스 공실률 5.8%, 5년 만에 최고치… 강남은 '클로드' 앤트로픽 입주 예정으로 IT 위상 강화 | 뉴스와이어（newswire.co.kr） | 2026 | 韓 | https://www.newswire.co.kr/newsRead.php?no=1039472&sourceType=rss | 搜尋結果內容 |
| TC-81 | 공실률 6.5%로 올랐지만 거래액 6조원…서울 오피스 '우량자산 쏠림' | 벤처스퀘어（venturesquare） | 2026 | 韓 | https://www.venturesquare.net/1105438 | 搜尋結果內容 |
| TC-82 | 仲量联行：二季度上海甲级办公楼空置率降至23.5% | 搜狐 | 2026（年份由摘要判定） | 簡中 | https://www.sohu.com/a/1055935733_655634 | 搜尋結果內容 |
| TC-83 | 净吸纳量23.2万方背后：2026年Q2上海商业地产市场的六组关键数据 | 网易订阅（163.com） | 2026 | 簡中 | https://www.163.com/dy/article/L1QVV0QF05159OAM.html | 搜尋結果內容 |
| TC-84 | 仲量联行：第二季度北京商业地产市场延续结构性分化态势 | 观点网（guandian.cn） | 2026 | 簡中 | https://www.guandian.cn/article/20260728/578007.html | 搜尋結果內容 |
| TC-85 | 2026年第二季度北京写字楼办公楼出租租金市场分析报告与发展前景趋势展望 | 高力国际（Colliers China） | 2026 | 簡中 | https://www.colliers.com.cn/zh-cn/research/20260708beijingofficeq2 | 搜尋結果內容 |
| TC-86 | 北京写字楼市场报告 2026年第二季度 | 莱坊（Knight Frank China） | 2026 | 簡中 | https://content.knightfrank.com/research/1527/documents/zh-chs/bei-jing-xie-zi-lou-shi-chang-bao-gao-2026nian-q2-12918.pdf | 搜尋結果內容 |
| TC-87 | 北京写字楼市场将迎来高供应周期 子市场去化压力或显著上升 | 央广网（cnr.cn） | 2026 | 簡中 | https://house.cnr.cn/kcb/20260714/t20260714_527708879.shtml | 搜尋結果內容 |
| TC-88 | 莱坊-房地产行业：2026年第二季度深圳写字楼市场报告 | 慧博投研资讯（hibor） | 2026 | 簡中 | https://m.hibor.com.cn/wap_detail.aspx?id=f6ad484404e17061441e1ebf1d8e9530 | 搜尋結果內容 |
| TC-89 | Kuala Lumpur office vacancy falls to 14.8% in Q2 | Real Estate Asia | 2026 | 英 | https://realestateasia.com/commercial-office/news/kuala-lumpur-office-vacancy-falls-148-in-q2 | 搜尋結果內容 |
| TC-90 | Jakarta – Q1 2026 Office | JLL | 2026 | 英 | https://research.jllapsites.com/appd-market-report/q1-2026-office-jakarta/ | 搜尋結果內容 |
| TC-91 | Bangkok Office Market Overview | Cushman & Wakefield Thailand | 2026 | 英 | https://www.cushmanwakefield.com/en/thailand/insights/bangkok-office-market-overview | 搜尋結果內容 |
| TC-92 | Manila Q2 office absorption reaches 40,400 sqm as vacancy falls | Real Estate Asia | 2026 | 英 | https://realestateasia.com/commercial-office/news/manila-q2-office-absorption-reaches-40400-sqm-vacancy-falls | 搜尋結果內容 |
| TC-93 | Ho Chi Minh City Office Market Approaches Balance as "Flight-to-Quality" Continues to Shape Demand | Cushman & Wakefield Vietnam | 2026 | 英 | https://www.cushmanwakefield.com/en/vietnam/news/2026/09/ho-chi-minh-city-office-market-approaches-balance-as-flight-to-quality-continues-to-shape-demand | 搜尋結果內容 |
| TC-94 | Cushman & Wakefield forecasts that Ho Chi Minh City and Hanoi will welcome a large amount of new office supply in 2024 | Cushman & Wakefield Vietnam | 2024 | 英 | https://www.cushmanwakefield.com/en/vietnam/news/2024/03/cushman-and-wakefield-forecasts-that-ho-chi-minh-city-and-hanoi | 搜尋結果內容 |
| TC-95 | India Office Market Q2 CY'26 Trends（rents up, vacancy down）（推定） | CREmatrix | 2026 | 英 | https://www.crematrix.com/blog/india-office-space-trends-2026-rents-up-vacancy-down/ | 搜尋結果內容 |
| TC-96 | India Office Market Dynamics Q2 2026（推定） | JLL India | 2026 | 英 | https://www.jll.com/en-in/insights/market-dynamics/india-office | 搜尋結果內容 |
| TC-97 | Bengaluru Office Market Q2 2026（推定） | Meraqi Advisors | 2026 | 英 | https://meraqiadvisors.com/articles/bengaluru-office-market-overview-q2-2026 | 搜尋結果內容 |
| TC-98 | The Global Hotel Construction Pipeline Reaches a Record High Project Count… at Q2 2026 Close | Lodging Econometrics | 2026 | 英 | https://lodgingeconometrics.com/global-hotel-construction-pipeline-q2-2026/ | 搜尋結果內容 |
| TC-99 | Global Insights | Lodging Econometrics | 2026 | 英 | https://lodgingeconometrics.com/global-insights/ | 搜尋結果內容 |
| TC-100 | Record Projects: APEC Hotel Pipeline Climbs to 2,387 Projects at Q1 2026 Close | Lodging Econometrics | 2026 | 英 | https://lodgingeconometrics.com/record-projects-apec-hotel-pipeline-q1-2026/ | 搜尋結果內容 |
| TC-101 | Asia Pacific Hotel Construction Pipeline Hits Record High as India Leads Regional Growth | Hotel-Online（日期欄誤植為 2025-08-06） | 2026 | 英 | https://www.hotel-online.com/news/asia-pacific-hotel-construction-pipeline-hits-record-high-as-india-leads-regional-growth | 搜尋結果內容 |
| TC-102 | China, India, and Vietnam Lead APAC's Hotel Pipeline | Skift Daily Lodging Report | 2026 | 英 | https://dlr.skift.com/2026/02/19/china-india-and-vietnam-lead-apacs-hotel-pipeline/ | 搜尋結果內容 |
| TC-103 | 乃村工藝社（乃村工芸社）【9716】の業績・財務推移 | 株探（かぶたん） | 2026 | 日 | https://kabutan.jp/stock/finance?code=9716 | 搜尋結果內容 |
| TC-104 | 丹青社【9743】の業績・財務推移 | 株探（かぶたん） | 2026 | 日 | https://kabutan.jp/stock/finance?code=9743 | 搜尋結果內容 |
| TC-105 | 丹青社の25年2〜4月期、純利益2.7倍 通期予想を上方修正 | 日本経済新聞 | 2025 | 日 | https://www.nikkei.com/article/DGXZRST0586497Q5A610C2000000/ | 搜尋結果內容 |
| TC-106 | 2025年版ディスプレイ業界 上場企業6社の業績まとめ | SHO-CASE（note） | 2025 | 日 | https://note.com/shocase/n/nfc3192d196d7 | 搜尋結果內容 |
| TC-107 | 【2026年最新】ディスプレイ業界2強「乃村工藝社」と「丹青社」の違いを徹底比較 | SHO-CASE（note） | 2026 | 日 | https://note.com/shocase/n/naf8922811942 | 搜尋結果內容 |
| TC-108 | 金螳螂(002081) 行业对比_F10 | 同花顺 | 2026 | 簡中 | http://basic.10jqka.com.cn/002081/field.html | 搜尋結果內容 |
| TC-109 | 金螳螂(002081) 最新动态_F10 | 同花顺 | 2026 | 簡中 | https://basic.10jqka.com.cn/002081/ | 搜尋結果內容 |
| TC-110 | 亚厦股份：2025年归母净利润3.30亿元 | 证券市场周刊 | 2026 | 簡中 | https://static.weeklyonstock.com/26/0427/AB2622075859419.html | 搜尋結果內容 |
| TC-111 | 亚厦股份的前世今生：2025年三季度营收68.73亿行业第三 | 新浪财经 | 2025 | 簡中 | https://finance.sina.com.cn/stock/aiassist/agqsjs/2025-10-31/doc-infvsyzf9267229.shtml | 搜尋結果內容 |
| TC-112 | 亞翔、漢唐、洋基8月績優 | 經濟日報（money.udn.com） | 2026 | 繁中 | https://money.udn.com/money/story/5607/9747158 | 搜尋結果內容 |
| TC-113 | 漢唐、亞翔6月及上半年營收 雙雙續創歷史同期新高 | 聯合新聞網 | 2026 | 繁中 | https://udn.com/news/story/7253/9625240 | 搜尋結果內容 |
| TC-114 | 台積設備鏈接單熱到2026 漢唐、亞翔、天虹等大進補（推定） | 經濟日報 | 2025 | 繁中 | https://money.udn.com/money/story/12926/8515002 | 搜尋結果內容 |
| TC-115 | 漢唐(2404) 前三季EPS已超越去年全年！在手訂單創新高（推定） | 鉅亨網 | 2025 | 繁中 | https://news.cnyes.com/news/id/6293105 | 搜尋結果內容 |
| TC-116 | 帆宣亞翔 接單創高（推定） | 工研院產科國際所 IEK | 2025（推定） | 繁中 | https://ieknet.iek.org.tw/ieknews/news_open.aspx/news_more.aspx?actiontype=ieknews&indu_idno=1&nsl_id=fde645ea6352472f916f22913c37124a | 搜尋結果內容 |
| TC-117 | 挑戰年賺 4 個股本？漢唐 EPS 創紀錄，為何 AI 擴產潮讓「無塵室龍頭」訂單接不完？（推定） | 詠騰不動產 | 2026 | 繁中 | https://www.ytyut.com/modules/news/article.php?storyid=8054 | 搜尋結果內容 |

> 來源備註：TC-14、TC-20、TC-42、TC-49、TC-51 僅確認報告存在或作為同一數字之輔證。TC-53 僅以標題引用。TC-54 僅用於說明 C&W 美洲版成本口徑。TC-75～77、TC-95～97、TC-114～117 為「推定」來源：URL 出現在搜尋結果，但所掛數字與該 URL 的對應未能確認，相關數字一律低信心。TC-97 之胡志明市非 CBD 出租率 88.39% 來自 maisonoffice.vn 摘錄，該值未採用。
