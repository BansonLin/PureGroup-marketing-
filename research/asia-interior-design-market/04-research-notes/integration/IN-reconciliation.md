# 印度 V1 × ChatGPT r2 × Gemini 指標對照（V2 整合）
整合日期：2026-10-10｜整合者：Claude V2 整合代理

> 輸入：V1 章節 `05-report/chapters/34-IN.md`（13 節、180 條來源）、`IN-verification.md`（23 項查核：確認 9／修正 8／駁斥 0／無法查證 6）、ChatGPT r2 `20261009_chatgpt_country-IN_r2.md`（18 條國別來源 #IN01–IN18＋#X01／X02／X11／MIN；32 列指標查核：29 pass、3 partial 僅年份未確認、0 fail；20 條 URL 全部可開）、`gpt-excluded.csv`（空：本市場無不採用項）、Gemini 資料包（無 URL）。
> 匯率：V1 以 1 USD ≈ INR 88 ≈ NT$31.4 換算；V2 統一參照表 1 USD＝INR 87.1468＝NT$31.1663。差 0.98%（INR）／0.75%（TWD），皆 <3%，依規則 7 V1 既有換算不重算；本表新增值以 V1 章節匯率換算（與統一表差 <1%），並附 ChatGPT 固定匯率值供對照。
> 依使用者指示：ChatGPT 將 Livspace FY25 調整 EBITDA 保留為 −13.1 億 INR（虧損記負值，＝ −131 crore，與 V1 同值）；#IN02 Magicbricks 二線「中古來源 82%／平均花費 Rs 3.9 lakh」為「2025 發布／觀察期未明」（partial）；BIS 傢俱 QCO 2026 修正頁開啟失敗列為缺口。Gemini「314.3 億美元、CAGR 12.87%（Mordor）、2031 年 650 億、Asian Paints Beautiful Homes」均無 URL；Mordor 已由 V1 [#5] 與 ChatGPT #IN01 引用，Gemini 同值不增加來源數，**Mordor 全程只算 1 個機構**。

## A. 指標逐項對照

（關係：一致／定義不同分桶／矛盾／僅 V1／僅 ChatGPT／ChatGPT 不採用）

| # | 指標（定義／年份） | V1 值（標籤；來源） | ChatGPT r2 值（等級；查核結果；來源 id） | Gemini 值 | 關係 | V2 採用值 | V2 標籤／信心 | 理由 |
|---|---|---|---|---|---|---|---|---|
| 1 | 人均名目 GDP（曆年 2025） | USD 2,675（IMF WEO 轉載，Worldometers）【示意】[#1] | USD 2,702.48（World Bank WDI 2025；A；pass；#MIN） | — | 一致（差 1.0%） | USD 2,702（WDI）；IMF 2,675 作交叉 | 【實際｜高】 | 規則 1：A 級開頁 pass＋V1 以不同管道（IMF）給出差 ≤5% 之值 |
| 2 | 人均名目 GDP（財年 FY2024/25E） | — | USD 2,591.5（World Bank Selected Indicators；A；pass；#IN16） | — | 僅 ChatGPT（定義不同：財年估計） | 不採為主值，僅註記 | 【預測／示意】 | 財年估計值，不與曆年實績混排（ChatGPT 自標）；V2 僅在 §13 註記 |
| 3 | 人口（2025） | 14.6 億（T1 轉載，未查證）§11、§13 | 14.6 億（WDI 2025，頁面四捨五入；A；pass；#MIN） | — | 一致 | 14.6 億 | 【實際｜高】 | A 級開頁 pass＋V1 同值 |
| 4 | GDP（現價，2025） | — | USD 3.96 兆（WDI 2025；A；pass；#MIN） | — | 僅 ChatGPT | USD 3.96 兆 | 【實際｜中】 | A 級開頁 pass；V1 無值；寫入 §11 人均 GDP 列備註 |
| 5 | 廣義「室內設計市場」Mordor 單一值（2025；範圍段：含設計合約附隨供應、排除獨立傢俱建材交易；住宅＋商用、新建＋翻修） | USD 314.3 億【示意】[#5]；IN-verification #1 確認、#2 修正定義（排除傢俱獨立銷售） | USD 314.30 億（C；pass；#IN01；2026-01 模型表 31.43 bn） | 314.3 億美元（無 URL） | 一致（三方同值；同一機構） | USD 314.3 億（2025） | 【示意｜低｜單源（Mordor）】 | 規則 2：同一機構被三個 AI 引用只算 1 個來源；Gemini 同值（無 URL）不計 |
| 6 | 廣義「室內設計市場」多機構區間（2024–2025） | USD 314–369 億（Mordor 314.3／TechSci 358.4／IMARC 368.9；另 P&S 321（2023）、Ken 307.5（2023）、VMR 364（2024））【示意】[#5][#6][#7][#40][#41][#42] | 僅 Mordor（上列） | 僅 Mordor 同值 | 一致（量級） | **USD 310–370 億（2024–2025）** | 【實際｜中｜多源量級一致、定義未對齊】 | 五家機構落在 Mordor ±17% 內（P&S、Ken、TechSci 在 ±15% 內，IMARC 17.4%），形式上達規則 2「≥3 一致」；但僅 Mordor 經開頁核對、各家定義未對齊（IN-verification #2），依規則 4「定義不同」封頂為中、不升高。裁決 V2-IN-001 |
| 7 | Mordor 2026 模型值／2031 預測／CAGR | 650.1 億（2031）【示意】[#5]；IN-verification #1：354.8 億（2026）、CAGR 12.87%（公布值） | 2026 模型 USD 354.80 億（C；pass；#IN01）【預測／示意】 | 2031 年 650 億、CAGR 12.87%（無 URL） | 一致 | 354.8 億（2026）、650.1 億（2031）、CAGR 12.87% | 【預測／示意】 | 規則 5：預測一律【預測／示意】；V1 原標【示意】升為正確標籤；Gemini 同值（無 URL） |
| 8 | IMARC 室內設計市場 2025／CAGR | USD 368.9 億、8.16%（2026–2034；同頁另載 24.30% 自相矛盾）【示意】[#7] | — | — | 僅 V1 | 維持 | 【示意｜低｜單源】（CAGR【預測／示意】） | IN-verification #1 ✅；ChatGPT 未引用；納入第 6 列區間 |
| 9 | 純設計服務市場 Grand View（2024） | USD 15.6 億（→21.8 億／2030，CAGR 5.9%）【示意】[#4] | 「純服務無資料」（13 欄表） | — | 僅 V1 | USD 15.6 億（2024） | 【示意｜低｜單源】（2030 值【預測／示意】） | IN-verification #1 ✅；ChatGPT 未找到純服務口徑，維持單源 |
| 10 | 商用占比（Mordor 主報告，2025） | 「商用 40–74%、無共識」（Mordor 74.44%、IMARC 住宅 60%、Mordor services 住宅 57.39%）【示意】[#5][#8]；IN-verification #3 | 74.44%（C；pass；#IN01） | — | 一致（Mordor 值）；機構間矛盾未解 | 維持「無共識：商用 40–74%」；Mordor 主報告 74.44% | 【示意｜低｜單源】 | ChatGPT 開頁僅確認 Mordor 主報告之值，無法裁決 IMARC／Mordor services 之矛盾。裁決 V2-IN-005（未決） |
| 11 | 新建占比（室內設計口徑，2025） | IN-verification #3 疑 Mordor 兩報告之 57.39% 標籤錯置；#4 補 IMARC 新裝 56%／翻修 44%（V1 章節未寫入） | 新建 57.39%（Mordor 主報告 2026-01 模型表；C；pass；#IN01） | — | 一致（Mordor 57.39% 新建 vs IMARC 56% 新裝，差 2.5%） | **新建 56–57%／翻修 43–44%（室內設計口徑，2025）** | 【實際｜中｜雙源】 | 規則 2：兩個獨立機構（Mordor 開頁 pass、IMARC 經 IN-verification #4）差 ≤15%；ChatGPT 開頁確認主報告 57.39% 為「新建占比」，解除 IN-verification #3 之標籤疑慮（services 報告「住宅 57.39%」疑為沿用錯誤） |
| 12 | 住宅營建口徑新建／翻修（Mordor，2025） | 新建 81.2%／翻修 18.8%；翻修子集 ≈USD 496 億為本章推算【示意】[#44] | — | — | 僅 V1 | 維持；496 億明標「本章推算」 | 【示意｜低｜單源；推算值不得以 Mordor 名義引用】 | IN-verification (b)6；與第 11 列為不同口徑（營建 vs 室內設計），分桶。裁決 V2-IN-009 |
| 13 | 住宅翻修市場可比區間（2025） | USD 126 億（IMARC home improvement services）–380 億（GMI remodeling 含材料）【示意】[#2][#3] | 「無純住宅翻修值」（13 欄表） | — | 僅 V1 | 維持 USD 126–380 億 | 【示意｜低｜兩口徑上下限】 | IN-verification #5 ✅（IMARC 版本差）、#6 無法查證（GMI）；ChatGPT 亦無純翻修值 |
| 14 | 「Home Interiors」市場（Magicbricks，2024；住宅內裝含傢俱模組，平台研究樣本） | — | INR 1.27 lakh crore＝INR 1.27 兆＝USD 145.73 億（C；pass；#IN02） | — | 僅 ChatGPT | INR 1.27 lakh crore ≈ USD 144 億（本章匯率）≈ NT$4,534 億（2024） | 【示意｜低｜單源】 | 新口徑第三桶；與 Mordor 314.3 億差 54%、與 V1 翻修區間重疊但定義不同，不平均、不作上下限佐證。裁決 V2-IN-002／003；另一版本摘要「USD 12.33 bn」PDF 未能開啟（缺口） |
| 15 | Home Interiors 2030 目標（Magicbricks） | — | INR 2.75 lakh crore（C；pass；#IN02）【預測／示意】 | — | 僅 ChatGPT | INR 2.75 lakh crore ≈ USD 312 億（2030） | 【預測／示意】 | 規則 5 |
| 16 | 二線城市 Home Interiors（Magicbricks，2024→2030） | — | INR 23,074 crore（2024）→72,500 crore（2030）（C；pass；#IN02） | — | 僅 ChatGPT | INR 2,307 億 ≈ USD 26 億（2024）；2030 值【預測／示意】 | 【示意｜低｜單源】 | 子集合不得再加回全國總量（ChatGPT 自註） |
| 17 | 二線城市內裝案源中古住宅占比（Magicbricks） | — | 82%（C；**partial**：年份「2025 發布／觀察期未明」；#IN02） | — | 僅 ChatGPT（定義：內裝案源，非交易比） | 82%（二線內裝案源；2025 發布、觀察期未明） | 【示意｜低｜單源；觀察期未明】 | 與第 20 列「二手交易 43%」定義不同，分桶並列、互不否證。裁決 V2-IN-006 |
| 18 | 二線城市平均內裝花費（Magicbricks） | — | Rs 3.9 lakh／案（C；**partial**：觀察期未明；#IN02） | — | 僅 ChatGPT | Rs 3.9 lakh ≈ NT$13.9 萬／案 | 【示意｜低｜單源；觀察期未明】 | 非全國均價；與 V1 2BHK 典型 8–15 lakh 範圍、城市、樣本不同，不比較 |
| 19 | 中古（二手）交易占全國登記住宅交易（FY2025） | 43%（FY2019 38%；Square Yards／Grant Thornton Bharat）【實際，IN-verification #14】 | 「無全國占比」（13 欄表） | — | 僅 V1 | 43%（FY2025） | 【實際｜中】 | 規則 3 後段：V1 另有經 V1 查核 ✅ 之來源→維持；單一彙整機構、未開頁，信心中 |
| 20 | 30 年以上屋齡占比／存量屋齡／翻修週期 | 無資料 | 無資料 | — | 一致（缺口） | — | 缺口 | 雙方皆無 |
| 21 | 前 7 大城市住宅銷售／新推案／未售庫存（Anarock，2025） | 395,625 戶（−14%）／419,170（+2%）／576,617（+4%）【實際】[#24][#25]；IN-verification #12 ✅（KF、PropEquity、Square Yards 方向一致） | — | — | 僅 V1（年份不同於 ChatGPT 之 2024） | 維持 | 【實際｜高】 | B 級統計；V1 三家機構方向佐證＋ChatGPT 開頁之 2024 基期 459,600 × (1−14%)＝395,256，與 395,625 差 0.1%，算術交叉一致 |
| 22 | 前 7 大城市住宅銷售／新推案／年增（Anarock 原報告，2024） | — | 459,600 戶／412,500 戶／−4%（B；pass；#IN03；Pan India 僅七城） | — | 僅 ChatGPT（2025 之基期） | 459,600／412,500／−4%（2024） | 【實際｜中】 | B 級原報告開頁 pass；寫入 §2 表作 2025 年基期 |
| 23 | PMAY-U 累計完工（2026-07） | 99.07 lakh 戶【實際】[#26][#27] | — | — | 僅 V1 | 維持 | 【實際｜中】 | 官方儀表板；IN-verification #13 未搜；ChatGPT 未觸及 |
| 24 | 住宅全屋單價（基本／中階／高階，INR/ft²，2025 業者頁；2026 版分級） | 800–1,200／1,200–2,000／2,000–3,500+；2026 版 1,200–1,800／1,800–3,000／3,000–5,500／5,500–10,000+【示意】[#9][#10][#11][#57] | 「每 m² 無同面積比較」（13 欄表）；僅套餐總額 | — | 定義不同分桶（每 ft² vs 每案套餐） | 維持 | 【示意｜低｜業者行銷頁】 | ChatGPT 拒絕以假設面積換算；V1 區間維持 |
| 25 | 都會中階獨立錨點（2026） | Rs 1,400–2,500/ft²（constructionestimatorindia 2BHK／3BHK 全屋估算）【實際，IN-verification #7】 | — | — | 僅 V1 | 維持數值 | 【示意｜中｜單一估算頁、與多家業者頁相容】 | **降級**：規則 2 估計值單一機構（C 級估算頁）→【示意】；因與 [#9][#10][#11] 業者帶相容，信心中。V1「實際」係指「經獨立搜尋驗證」，與 V2 標籤定義不符 |
| 26 | Livspace 2BHK 套餐（2026 價格頁；基本／中階／高階） | — | INR 1,059,000／1,368,000／1,919,000（C；pass；#IN04；未給統一面積） | — | 僅 ChatGPT | Rs 10.59／13.68／19.19 lakh ≈ NT$37.8／48.8／68.5 萬 | 【示意｜低｜單源】 | 廠商示意非成交樣本；若以 1,000 ft² 計約 Rs 1,059–1,919/ft²，落在 V1 基本–中階帶（本章推算、不入正文表） |
| 27 | 每案均價 2BHK／3BHK（V1 三段：模組化起價／典型／都會全屋中階） | 2BHK 起價 3.4 lakh（HomeLane）、典型 8–15、都會中階 14–25 lakh；3BHK 7–35 lakh【示意；IN-verification #8】[#64][#131][#132][#133] | Livspace 套餐（第 26 列） | — | 一致（Livspace 10.59–19.19 lakh 落在典型／都會中階帶） | 維持，補 Livspace 套餐 | 【示意｜低】 | 組織化連鎖第二個價格點，相容但口徑（含項）不同 |
| 28 | 設計費市場行情 | Rs 50–500/ft²（典型 100–250）或工程款 5–15%（豪宅 25% 單源）【示意】[#12][#13][#63][#64] | 「COA 指引 7.5% 工程費，非普遍成交行情」 | — | 定義不同分桶（市場行情 vs 專業費率表） | 維持 | 【示意｜低】 | IN-verification #9 ✅ |
| 29 | CoA《Scale of Charges》室內建築服務費率／文件溝通附加費 | 「IIID 或 CoA 官方收費指引：無資料」（§2）；IN-verification #9：「無室內設計專用之 CoA 官方費率」 | 7.5% of works（第 3 項）；10% of professional fees（第 7 項）（A；pass；#IN14）；另 #IN13 Interior Design Conditions of Engagement（A；pass） | — | 僅 ChatGPT（**補缺口、修正 V1 查核結論**） | 7.5% 工程費；文件與溝通 10% 專業費 | 【實際｜中】 | 規則 1：A 級原文開頁 pass；V1 無值故為中。落在市場百分比制 5–15% 內。IN-verification #9「無室內設計版本」之結論被推翻 |
| 30 | 商辦 fit-out 單位成本（C&W 2026；價格基準 2025-12） | INR 5,847–6,567/ft²（USD 65–73/ft²）【示意，中；無法查證；IN-verification #10】[#19][#20] | 孟買 USD 73/ft²＝785.77 USD/m²，原幣 INR 6,567/ft²（B；pass；#X02 指南 pp.30–31＋#X11 方法頁） | — | 一致（孟買上限同值） | 維持區間；孟買 USD 73/ft²＝INR 6,567 已核對 | 【示意｜中｜單源（C&W）；孟買值已開頁核對】 | 規則 2：單一機構估計→【示意】；「無法查證」註記移除；下限 5,847（其他城市）ChatGPT 未逐一讀取 |
| 31 | 辦公室總租賃 2025（JLL／KF／C&W） | 83.3／86.4／≈89 百萬 ft²【實際】[#21][#22][#23] | — | — | 僅 V1 | 維持 | 【實際｜中】 | 三機構量級一致（差 6.8%）但覆蓋城市不同、未開頁；IN-verification #11 未搜 |
| 32 | Livspace FY25 營收 | Rs 1,460 crore（+23%）【實際】[#14][#15][#16] | INR 14.6 bn（B；pass；#IN06 Economic Times） | — | 一致 | Rs 1,460 crore ≈ NT$52 億 | 【實際｜中】 | 公司公告經多媒體轉載（同一來源不增計）；審計財報未取得→中，不升高 |
| 33 | Livspace FY25 毛利／毛利率 | 毛利率 51.5%【實際】[#14] | 毛利 INR 7.52 bn、51.5%（B；pass；#IN06） | — | 一致（毛利率）；毛利額僅 ChatGPT | 51.5%；毛利 Rs 752 crore ≈ NT$26.8 億 | 【實際｜中】 | 補毛利額 |
| 34 | Livspace FY25 調整 EBITDA（ESOP 前） | −131 crore【實際】[#15] | −1.31 INR bn（虧損記負值；B；pass；#IN06） | — | 一致（同值） | −Rs 131 crore | 【實際｜中】 | 依使用者指示保留負值表述；非淨損，不得混用 |
| 35 | Livspace FY25 淨損 | −242 crore（−42%）【實際】[#16] | —（ChatGPT 僅調整 EBITDA） | — | 僅 V1 | 維持 | 【實際｜中】 | ChatGPT 明示「不能把調整 EBITDA 虧損寫成淨損」，V1 已分列 |
| 36 | Livspace Series F（2022）／累計募資 | USD 1.8 億（KKR 領投，Business Wire）；累計約 4.5 億、估值 >10 億【示意】[#70] | USD 180 M（C；pass；#IN09 KKR 新聞稿；歷史事件） | — | 一致 | 維持 | 【實際｜中】（累計值【示意】） | 同一新聞稿兩管道；歷史背景 |
| 37 | HomeLane FY25 營收／淨損／廣告費 | Rs 747.8 crore（+22%）／−111.4 crore／廣告 84 crore（11%）【實際】[#17][#18] | —（缺口表：「管理層目標不可當實績」） | — | 僅 V1 | 維持 | 【實際｜中】 | ChatGPT 未取得 FY25 數字；V1 兩媒體（Inc42、Entrackr 依 MCA 申報） |
| 38 | HomeLane–DesignCafe 交易股權結構（2024） | 「2024-09 以 100% 換股併購 DesignCafe」[#75] | 取得多數股權＋未來全購承諾（C；pass；#IN08 交易律師 JSA 2024-12-18 公告；ChatGPT §5 裁決採 JSA、棄「官方訪談稱全購」） | — | **矛盾（定義：100% vs 多數股權）** | 多數股權並承諾後續全購 | 【實際｜中】 | 交易顧問公告（直接參與、開頁 pass）> 媒體「seeks buyout」報導；V1 修正。裁決 V2-IN-004 |
| 39 | HomeLane 同期募資 | Rs 225 crore [#75] | INR 2.25 bn（C；**partial**：LinkedIn 頁僅顯示「2y」，絕對日期未確認；#IN07） | — | 一致 | Rs 225 crore ≈ NT$8 億 | 【實際｜中】 | 公司官方公告＋媒體兩管道同值；日期以 JSA 2024-12 為準 |
| 40 | 合併估值 | 「曾談 USD 3.6 億估值」[#75] | 約 Rs 3,000 crore＝INR 30 bn（C；pass；#IN08） | — | 一致（Rs 3,000 crore ≈ USD 3.4 億@87／3.6 億@2024 匯率） | 約 Rs 3,000 crore ≈ USD 3.4–3.6 億 | 【示意｜低】 | 估值非對價、無計算底稿 |
| 41 | HomeLane 合約工期／延遲補償／保固（T&C 2025-11 版，2026 存取） | 「45–90 天」「保固 5–10 年」無 URL 不採用；缺口 | Type A 標準範圍 45 天（設計核准、合約、付款、現場前提後起算；土建拆除等排除）；延遲補償 Rs 1,000/日有上限；保固依木作／材種／OEM／服務分別（C；pass；#IN05） | — | 僅 ChatGPT（**補缺口**） | 如左 | 【實際｜中｜單一公司條款，非法定標準】 | 公司條款原文開頁 pass；屬「實際條款」而非估計；僅一家公司 |
| 42 | IKEA India FY25 營收／淨損 | 「Rs 1,749.5（−3.3%）或 1,860 crore（+6%）兩源矛盾」；淨損 1,325 crore【示意】[#80][#81]；IN-verification #21 裁決採 ROC 申報值 1,749.5 | — | — | 僅 V1（V1 內部矛盾，差 6%） | Rs 1,749.5 crore（−3.3%）；淨損 1,325.2 crore | 【實際｜中】 | 依 IN-verification #21（Tofler／ROC 申報）結案；1,860 疑為初步數棄用。V1 章節未完全套用查核結論，V2 套用 |
| 43 | 其他玩家營收（Godrej Interio 4,000 crore／Space Matrix 500–1,000／Cherry Hill 366／Asian Paints 33,797 crore） | 各【示意】[#76]–[#79][#84] | 僅列名（Asian Paints Beautiful Homes、Space Matrix、Godrej 等）無數字；「代表而非前三排名」 | Livspace、HomeLane；Asian Paints Beautiful Homes（無 URL） | 一致（名單）；數字僅 V1 | 維持 | 【示意】 | 三方玩家名單一致，無新數字 |
| 44 | 設計師執業管制（Architects Act 1972 §37；SC 2020 Mukesh Goyal） | 無執照、僅「architect」名稱受保護【實際】[#28][#29]；IN-verification #15 ✅ | 同結論（A；pass；#IN10 CoA 版法案 PDF、#IN11 CoA 2020 公告） | — | 一致 | 維持 | 【實際｜高】 | 規則 1：A 級原文開頁 pass＋V1 以不同管道（indiacode／SCI 判決）確認。仍註「需專業人士最終確認」 |
| 45 | CoA《Interior Design Conditions of Engagement》 | — | 區分概念、初步設計、核准圖、施工圖招標、承包商聘任、現場、完工；日常監督非當然含（A；pass；#IN13） | — | 僅 ChatGPT | 寫入 §5 | 【實際｜中】 | 專業委任範本、非強制消費者契約；與 V1 §6「無標準契約」不衝突 |
| 46 | 承包商執照 | 無全國執照【示意】[#96][#97] | 「在地承包施工不能單憑 FDI 公司設立即開工；地方登記、建管消防另查」 | — | 一致 | 維持 | 【示意】 | 雙方皆為推論＋二手指南 |
| 47 | 外資持股（設計服務／未列明行業） | 100% 自動路徑（DPIIT 2025-07 清單）【實際】[#30][#119] | 100% automatic（A；pass；#IN12 DPIIT Consolidated FDI Policy 2020 第 29 頁） | — | 一致 | 維持 | 【實際｜高】 | A 級原文 pass＋V1 不同文件同結論；零售／房地產交易另審 |
| 48 | Press Note 3（2020）對台適用／2026 修正 | 無官方澄清、律師分歧；有陸資受益人須核准；「2026 年放寬小額持股審查，與台灣無關」【示意，中/低；IN-verification #18】[#31] | 2026-05-01 修正：非控制之陸鄰國（LBC）權益 ≤10% 可依條件走自動路徑（A；pass；#IN17 PIB 2026-08-21）；「不宜只因台灣出資就跳過最終受益人審查」 | — | 一致（ChatGPT 補官方細節） | 維持 V1 結論＋補 ≤10%／2026-05-01 細節 | 【示意，信心中/低】（修正細節【實際｜中】） | 適用台灣與否仍無官方澄清；規則 8 需專業確認 |
| 49 | Employment Visa 年薪門檻 | USD 25,000（或 Rs 16.25 lakh 官方盧比版）【實際】[#32]–[#34]；IN-verification #19 ✅ MHA FAQ | 「派駐工作與稅務：本次未完成可直接採行的條件查核」 | — | 僅 V1 | 維持 | 【實際｜中】 | V1 查核 ✅ 官方 PDF（搜尋摘要）；未開頁 |
| 50 | GST（設計 18%／工程承攬 18%／傢俱 18%） | 【實際】[#122][#123][#105] | 缺口 | — | 僅 V1 | 維持 | 【實際｜中】 | 二手稅務指南一致；需專業確認 |
| 51 | 公司所得稅（子公司 25.17%／分公司 36.40–38.22%） | 【示意】[#124]–[#126]；IN-verification #23 算術一致 | 缺口 | — | 僅 V1 | 維持 | 【示意】 | 需稅務專業確認 |
| 52 | 消費者保護法 2019 條號（§2(11)、§2(47)、§34(2)(d)、§35、§69(1)） | 【實際，IN-verification #20】[#108][#109] | 法案原文（A；pass；#IN15 官方 PDF；已讀服務瑕疵定義） | — | 一致 | 維持；補官方 PDF 來源 | 【實際｜高】 | A 級原文 pass＋V1 查核 ✅ 條號修正 |
| 53 | 消費者投訴統計（NCH 2025） | 67,265 件、退款 Rs 45 crore；無裝修分項【實際】[#112][#113] | 「無可比全國室內裝修投訴量」 | — | 僅 V1 | 維持 | 【實際｜中】 | 缺裝修分項，雙方一致 |
| 54 | BIS 合板／木質板材 QCO（2025-02 生效，進口適用） | 【實際】[#35][#36]；IN-verification #22 ✅ S.O. 1377(E) | —（ChatGPT 讀的是傢俱 QCO） | — | 僅 V1 | 維持 | 【實際｜中】 | 公報編號經 V1 查核；未開頁 |
| 55 | 傢俱品質管制令 2025（Furniture (QC) Order；椅、桌、收納單元、床等） | 僅 [#156] 媒體提及「panels and furniture」 | 法令英文頁（A；pass；#IN18 BIS 2025-02-17）；2026 修正頁兩次 timeout | — | 僅 ChatGPT（**新事實**） | 寫入 §9、§12 | 【實際｜中】（現行時程【缺口】） | A 級原文 pass；2026 修正生效時程與例外待核 |
| 56 | 成品傢俱關稅（25–27.5%＋IGST 18%）、合板關稅、MDF 反傾銷 | 【示意】[#37][#38][#157][#158] | 「不同板材、電器、傢俱不可共用籠統關稅率」（缺口） | — | 僅 V1 | 維持 | 【示意】 | 二手關稅頁 |
| 57 | 技術工短缺（NAREDCO 200 萬；CSDCI 缺口 4,250 萬） | 【示意】[#39]；【實際】[#151] | 缺口 | — | 僅 V1 | 維持 | 【示意】／【實際｜中】 | — |
| 58 | 設計師年薪／監工月薪／木工日薪 | Rs 3.15–4.2 lakh；Rs 19,129–22,083／月；Rs 750–1,300／日【示意】[#143]–[#149] | 缺口（Labour Bureau 連結多次 502；農村工資不可當都市精裝成本） | — | 僅 V1 | 維持 | 【示意】 | 聚合平台估計 |
| 59 | 材料點價（合板 Rs 65–220/ft²、水泥 Rs 300–600／袋）、GST 改革 | 【示意】[#160][#161][#104] | 缺口（Kajaria 年報超上限） | — | 僅 V1 | 維持 | 【示意】 | — |
| 60 | 修繕貸款利率（HDFC 7.75–13.20%；SBI 7.25 vs 9.15%）、§24(b) | 【示意】矛盾未解 [#138]–[#142] | 「付款與融資無足夠全國調查」 | — | 僅 V1 | 維持（矛盾未解） | 【示意】 | ChatGPT 未觸及。裁決 V2-IN-010（未決） |
| 61 | 線上室內設計滲透 | <1%（Redseer FY19，已過時）【示意】[#91] | 「平台滲透率無資料；平台自報營收不作分子」 | — | 僅 V1 | 維持 | 【示意｜低｜過時】 | — |
| 62 | 人均翻修支出（本章推算） | USD 9–26（126–380 億 ÷ 14.6 億）【示意】 | 「不以混合額除全國人口」 | — | 僅 V1（ChatGPT 反對此類推算） | 維持，明標「本章推算、分子為住宅翻修兩口徑」 | 【示意｜低｜推算】 | 分子為住宅翻修口徑（非 Mordor 混合額），ChatGPT 之反對不直接適用，但保留其警示 |
| 63 | Livspace 裁員人數 | 100 vs >1,000 人兩源矛盾 [#71][#72] | — | — | 僅 V1（矛盾未解） | 維持矛盾 | 【示意】 | 裁決 V2-IN-010（未決） |
| 64 | 匯率參照 | 1 USD ≈ INR 88 ≈ NT$31.4 | USD1＝INR 87.1468＝NTD 31.1663（A；#X01 Fed G.5A） | — | 一致（差 <1%） | V1 換算不重算 | — | 規則 7 |
| 65 | 進入評分／優先度（管理判斷） | T3「設計 4／承攬 4（滿分 4）」＝法規可行性；§12「2026–2027 以觀察與小額 B2B 試水為限」 | 進入優先度 2／5（學模組、估價、合約；由既有企業客戶帶入） | 跨境可行性 2.5（無 URL、尺度未明） | 定義不同（可行性 vs 優先度） | 維持 V1 §12 結論；註 ChatGPT 2/5 方向一致 | 管理建議 | 三方均指向「先學習、後小額 B2B」 |

## B. 矛盾裁決（差 > 30% 或定義衝突）

| 編號 | 指標 | 來源 1（值、等級） | 來源 2（值、等級） | 差異原因 | 裁決 | 裁決理由 | 信心 |
|---|---|---|---|---|---|---|---|
| V2-IN-001 | 廣義「室內設計市場」區間之標籤 | Mordor USD 314.3 億（C，開頁 pass；範圍段：含設計合約附隨供應、排除獨立商品交易） | IMARC 368.9／TechSci 358.4／P&S 321／Ken 307.5／VMR 364 億（C，僅搜尋摘要；定義未揭露） | 五家量級一致（Mordor ±17%）但定義未對齊；Grand View 純服務 15.6 億另成一桶（20 倍差） | 區間 USD 310–370 億標【實際｜中｜多源量級一致、定義未對齊】；Mordor 單一值【示意｜低｜單源】；Grand View 15.6 億【示意｜低｜單源】；三桶並列不平均 | 形式上達規則 2「≥3 機構 ≤15%」，但規則 4 要求先比定義——僅 Mordor 定義已讀，其餘未知→封頂為中、不升高 | 中 |
| V2-IN-002 | Mordor 設計服務合約市場 vs Magicbricks Home Interiors | USD 314.3 億（2025，C） | INR 1.27 lakh crore ≈ USD 144 億（2024，C） | 差 54%；定義不同（住宅＋商用設計合約 vs 住宅內裝含傢俱模組）、年份不同 | 分桶並列，各自【示意｜低｜單源】；禁止平均或視為上下界（ChatGPT §5 同裁決） | 規則 4 定義不同→分桶 | 低 |
| V2-IN-003 | 住宅翻修規模 | IMARC HIS 126 億／GMI 380 億／Mordor 子集推算 496 億（V1） | Magicbricks 145.7 億（2024） | 四個口徑：僅服務／含材料施工／營建子集推算／內裝含傢俱模組 | V1 可比區間 126–380 億維持；496 億明標本章推算；Magicbricks 列為第三口徑、不作佐證 | 規則 4；IN-verification (b)6 | 低 |
| V2-IN-004 | HomeLane–DesignCafe 股權結構 | V1：100% 換股併購（Inc42 2024「seeks buyout at $360 Mn」，B／媒體） | ChatGPT：取得多數股權＋未來全購承諾（JSA 交易律師 2024-12-18 公告，C 但直接參與；開頁 pass） | 媒體以交易前「尋求全購」與公司訪談口語為據；交易顧問記載階段性結構 | **採 JSA**：V1 §3 改為「取得多數股權並承諾後續全購」；估值約 Rs 3,000 crore（≈ USD 3.4–3.6 億）與 V1「USD 3.6 億」相容 | 已開頁且為交易直接參與方 > 媒體轉述；ChatGPT §5 同裁決 | 中 |
| V2-IN-005 | 住宅／商用占比（室內設計市場） | Mordor 主報告商用 74.44%（2025，開頁 pass） | IMARC 住宅 60%（2025）；Mordor services 報告住宅 57.39% | 機構模型與分類不同；>30% | **未決**：維持 V1「無共識：商用 40–74%」；ChatGPT 開頁只確認 Mordor 主報告數值並釐清 57.39% 為「新建占比」，不能裁決機構間差異 | 規則 4：定義不同且無 A 級來源可為準 | 低 |
| V2-IN-006 | 「中古」比重 | Square Yards／GT Bharat：二手占全國登記住宅交易 43%（FY2025，B，V1 查核 ✅） | Magicbricks：二線城市內裝案源 82% 來自中古住宅（2025 發布／觀察期未明，C，partial） | 定義不同（交易比 vs 內裝案源比）、母體不同（全國 vs 二線） | 分桶並列：43% 入「中古交易占比」【實際｜中】；82% 入「二線內裝案源結構」【示意｜低；觀察期未明】；13 欄表「中古屋交易占比」填 43%，附 82% 註腳 | 規則 4；ChatGPT 13 欄表亦明示 82% ≠ 交易比 | 中／低 |
| V2-IN-007 | 人均 GDP 口徑 | World Bank WDI 曆年 2025 USD 2,702.48（A） | World Bank Selected Indicators FY2024/25E USD 2,591.5（A，財年估計）；IMF 轉載 2,675 | 差 4%；財年估計 vs 曆年實績 | 採曆年 WDI 2,702；財年值僅於 §13 註記不混排 | ChatGPT 自標財年值為【預測／示意】 | 高 |
| V2-IN-008 | IKEA India FY25 營收 | Rs 1,749.5 crore（Tofler／ROC 申報，IN-verification #21） | Rs 1,860 crore（Business Standard 2025-11 初步數） | 差 6%（<30%，列此僅因 V1 章節仍寫「兩源矛盾」） | 採 1,749.5 crore，1,860 棄用；V1 §3、§13 同步 | V1 查核已裁決而章節未套用 | 中 |
| V2-IN-009 | 翻修占比四口徑 | 室內設計口徑：Mordor 新建 57.39%→翻修 42.6%（開頁）／IMARC 翻修 44%（V1 查核） | 住宅營建口徑 Mordor 翻修 18.8%；Magicbricks 二線內裝案源中古 82% | 口徑：室內設計合約／住宅營建產值／二線內裝案源 | 室內設計口徑翻修 43–44%【實際｜中｜雙源】；營建口徑 18.8%【示意】；二線 82%【示意｜低】；V1「中古翻新為小眾」限縮為「就住宅營建口徑而言」 | 規則 2（雙源一致）＋規則 4（分桶） | 中／低 |
| V2-IN-010 | V1 內部矛盾未決（ChatGPT 未觸及） | Livspace 裁員 100 人（HRKatha） | >1,000 人（Entrackr） | 事件時點與口徑不同 | **未決**；另 SBI 修繕貸款 7.25% vs 9.15%、§24(b) 修繕利息扣除 Rs 30,000 vs 不適用，均維持矛盾標示 | 無新證據 | 低 |

## C. V1 被修正或降級的項目

1. **一頁摘要第 1 點、§11 表「人均 GDP」**：USD 2,675（IMF 轉載）【示意】→ USD 2,702（World Bank WDI 2025）【實際｜高】，IMF 2,675 保留作交叉；台灣倍數 1／14.8 → 1／14.6（§11）。原因：A 級開頁 pass＋V1 不同管道同值（規則 1）。
2. **一頁摘要第 2 點、§1 建議區間**：廣義口徑 USD 314–369 億【示意】→ USD 310–370 億【實際｜中｜多源量級一致、定義未對齊】（升級但封頂為中，V2-IN-001）；Mordor 範圍描述由「疑含執行工程、排除傢俱獨立銷售」補為「含設計合約附隨供應、排除獨立傢俱建材交易（ChatGPT 開頁讀取範圍段）」。
3. **§1 表、§1 成長展望**：Mordor 650.1 億（2031）、各機構 2030／2034 值與 CAGR 由【示意】→【預測／示意】（規則 5）；表下加註。
4. **一頁摘要第 3 點、§2 單價表中階列**：都會中階錨點 Rs 1,400–2,500/ft²「【實際，IN-verification #7】」→「【示意｜中｜單一估算頁、與多家業者頁相容】」。**降級**：單一 C 級估算頁之估計值依規則 2 不得標【實際】。
5. **§2 設計費段末、§13**：「IIID 或 CoA 官方收費指引：無資料」→ CoA《Scale of Charges》室內建築服務 7.5% 工程費、文件與溝通 10% 專業費【實際｜中】；IN-verification #9「無室內設計專用之 CoA 官方費率」之結論被 ChatGPT #IN14 推翻。
6. **§2 intro「台灣式的中古屋翻新在統計上仍是小眾」**：限縮為「在住宅營建口徑仍是小眾」，並補室內設計口徑翻修 43–44%【實際｜中｜雙源】與 Magicbricks 二線 82% 之對照（V2-IN-009）。
7. **§3 表 HomeLane 列、§3 資本事件段**：「2024-09 以 100% 換股併購 DesignCafe」→「2024 年取得 DesignCafe 多數股權並承諾後續全購（JSA 2024-12-18 公告）」；補合併估值約 Rs 3,000 crore（V2-IN-004）。
8. **§3 表 IKEA 列、§13**：「營收 Rs 1,749.5 或 1,860 crore 兩源矛盾【示意】」→「Rs 1,749.5 crore（ROC 申報值）【實際｜中】」，依 IN-verification #21 結案（V2-IN-008）。
9. **一頁摘要第 5 點、§2 商辦列、§11 商辦列**：C&W「【示意，中；無法查證、規格待註】」→「【示意｜中｜單源；孟買 USD 73/ft²＝INR 6,567 經 ChatGPT r2 開頁核對、價格基準 2025-12】」（查證狀態改善，標籤不變）。
10. **一頁摘要第 6 點**：Anarock 2025 銷售【實際】→【實際｜高】（ChatGPT 開頁之 2024 基期算術交叉一致）。
11. **一頁摘要第 7 點、§5、§7、§11**：Architects Act／SC 2020【實際】→【實際｜高】；外資 100% 自動路徑【實際】→【實際｜高】（A 級原文開頁 pass＋V1 同結論）。
12. **§6 首段**：CPA 2019 條號【實際，IN-verification #20】→【實際｜高】（法案原文開頁 pass）。
13. **一頁摘要第 4 點、§3、§11**：Livspace／HomeLane 財務【實際】→【實際｜中】（加註信心：公司公告多媒體轉載、審計財報未取得）。
14. **§6 表「付款節奏、保固、escrow：無可引用來源」**：拆為「工期、延遲補償、保固（HomeLane 合約條款）【實際｜中】」與「付款節奏、escrow：缺口」。
15. **§13 整體信心**：「低–中……本章未經任何獨立查核」→「中……法規、外資與公司財報已經 ChatGPT r2 開頁核對」。

## D. ChatGPT 帶來的新事實（V1 沒有、本次寫入 V2）

| 新事實 | 寫入位置 | 來源 id | URL |
|---|---|---|---|
| Magicbricks「Home Interiors」2024 INR 1.27 lakh crore（≈USD 144 億）、2030 目標 2.75 lakh crore；二線城市 23,074→72,500 crore | §1 表新列、一頁摘要第 2 點 | #IN02 | https://property.magicbricks.com/microsite/research-insights/src/pdf/sample/Interiors-Sample-Report.pdf |
| 二線城市內裝案源 82% 來自中古住宅、平均花費 Rs 3.9 lakh（2025 發布／觀察期未明） | §2 intro、§2 表、§8 表、§11 中古列 | #IN02 | 同上 |
| Anarock 2024 七城銷售 459,600／新推案 412,500／−4%（2025 年 −14% 之基期） | §2 表新列、一頁摘要第 6 點 | #IN03 | https://websitemedia.anarock.com/media/ANAROCK_Research_Indian_Residential_Market_Annual_Update_2024_3b5aa5b04d.pdf |
| Livspace 2026 兩房套餐 Rs 10.59／13.68／19.19 lakh（未給面積） | §2 每案均價段、§8 2BHK 列 | #IN04 | https://www.livspace.com/in/magazine/how-much-does-an-interior-designer-charge |
| HomeLane T&C：Type A 45 天（有前提）、延遲補償 Rs 1,000/日有上限、保固依材種／OEM 分級 | §2 表、§6 表、§12 第 5 點 | #IN05 | https://www.homelane.com/homelane-terms-conditions |
| Livspace FY25 毛利 Rs 752 crore（調整 EBITDA −131 crore 為「ESOP 前」口徑） | §3 表 | #IN06 | https://economictimes.indiatimes.com/tech/startups/homedecor-startup-livspaces-fy25-revenue-rises-23-to-rs-1460-crore/articleshow/124520597.cms?from=mdr |
| HomeLane–DesignCafe：多數股權＋後續全購承諾；合併估值約 Rs 3,000 crore（JSA 2024-12-18） | §3 表、§3 資本事件段 | #IN08（#IN07 LinkedIn 225 crore 佐證） | https://www.mondaq.com/pressrelease/154532/homelane-acquires-designcafe-raises-primary-funds-from-an-investor-club-consisting-of-hero-enterprise-claypond-capital-partners-westbridge-and-others ；https://www.linkedin.com/posts/homelane_growth-acquisition-homeinteriors-activity-7249658945546428416-Bt0D |
| CoA《Scale of Charges》：室內建築服務 7.5% 工程費；文件與溝通 10% 專業費 | §2 設計費段、§11 設計費列、§13 | #IN14 | https://coa.gov.in/index1.php?lang=1&level=2&lid=86&sublinkid=299 |
| CoA《Interior Design Conditions of Engagement》階段劃分（日常監督非當然含） | §5 | #IN13 | https://coa.gov.in/index1.php?lang=1&level=2&lid=82&sublinkid=295 |
| CoA 2020 公告：僅重申「Architect」稱謂保護、無室內設計全面禁令 | §5、§11 | #IN11 | https://coa.gov.in/show_img.php?fid=645 |
| 2026-05-01 FDI 修正：非控制之陸鄰國權益 ≤10% 可依條件走自動路徑（PIB 2026-08-21） | 一頁摘要第 7 點、§5 變動段、§7 表 | #IN17 | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2301992 |
| DPIIT 2020 綜合 FDI 政策原文（未列限制活動 100% 自動路徑） | §7 表來源補強 | #IN12 | https://www.dpiit.gov.in/static/uploads/2025/07/6457fc2703ee6082366c4a958b6473a8.pdf |
| 《傢俱品質管制令 2025》涵蓋椅、桌、收納單元、床、雙層床等（2026 修正頁開啟失敗） | 一頁摘要第 8 點、§9、§12 第 4 點、§13 | #IN18 | https://www.bis.gov.in/furniture-qco-17-02-2025/ |
| World Bank WDI 2025：人均 GDP USD 2,702.48、人口 14.6 億、GDP USD 3.96 兆 | 一頁摘要第 1 點、§11、§13 | #MIN | https://data.worldbank.org/country/india |
| 消費者保護法 2019 官方 PDF（來源補強） | §6 | #IN15 | https://consumeraffairs.gov.in/public/upload/files/CP%20Act%202019_1732700731.pdf |
| C&W 2026 APAC 指南 pp.30–31：孟買 USD 73/ft²＝INR 6,567/ft²、價格基準 2025-12 | 一頁摘要第 5 點、§2 商辦列、§11 | #X02／#X11 | https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office/30-31/ |
| Mordor 主報告：新建占比 57.39%（2025）、2026 模型 354.8 億（與 IMARC 新裝 56% 構成雙源） | §1 表 Mordor 列、§2 intro | #IN01 | https://www.mordorintelligence.com/industry-reports/india-interior-design-market |

## E. 仍未解決的缺口（含 ChatGPT 也查不到的；建議取得方式）

| 缺口 | 狀態 | 建議取得方式 |
|---|---|---|
| 純住宅翻修同口徑總量與 2030 預測 | V1 兩口徑上下限（126–380 億）、ChatGPT 兩口徑（Mordor 混合、Magicbricks 內裝）均非純住宅翻修 | 向 Mordor／IMARC／Magicbricks 索取分項與方法底稿；MoSPI 國民帳戶 repair & maintenance；NSSO HCES |
| 住宅／商用占比 | 三組機構數字矛盾（V2-IN-005 未決） | 採購 Mordor／IMARC 完整報告比對分類定義 |
| Magicbricks 另一版本（搜尋摘要 USD 12.33 bn）與已開啟盧比版（≈USD 14.6 bn）差 15% | ChatGPT：PDF 反覆開啟失敗 | 向 MB Research 索取原稿與版本變更說明 |
| 二線 82%／Rs 3.9 lakh 之觀察期 | partial（2025 發布、觀察期未註） | 同上 |
| 住宅完工戶數、存量屋齡、翻修週期、30 年以上屋齡 | 雙方皆無 | Anarock／PropEquity deliveries；各邦 RERA；Census 2011 H-series；NSS 76th round |
| 商辦裝修國家級總量；C&W 區間下限（5,847/ft²）所屬城市與規格 | ChatGPT 僅讀孟買頁 | C&W 指南其餘城市頁；JLL 印度 fit-out 正文 |
| 付款節奏、escrow、Livspace 條款 | HomeLane 單一公司條款已取得；Livspace T&C 未讀 | Livspace T&C 頁；兩家 DRHP |
| 傢俱 QCO 2026 修正版生效時程與例外 | BIS 2026 修正頁兩次 timeout | BIS 官網／egazette 原文；BIS 認證顧問 |
| 設計科系畢業人數、泥作／水電日薪、最低工資、WPI 建材指數 | ChatGPT：Labour Bureau 連結多次 502；農村工資不可代用 | AICTE／CoA；各邦勞工局；eaindustry.nic.in |
| 建材市占率、Kajaria 等年報分項、純設計事務所營收 | ChatGPT：Kajaria 年報超檔案上限 | BSE／NSE 年報；Tofler／Zauba |
| 平台 GMV／CAC／抽成、體驗中心家數、建商合作比例 | 雙方皆無 | DRHP；公司揭露 |
| 消防 NOC（單戶內裝）、NBC 2016 Part 4、德里／班加羅爾建管細則 | 雙方皆無；ChatGPT「未逐城市核驗」 | BIS NBC 頁；在地持照專業者法規矩陣 |
| Employment Visa 2025 年官方公告；「≥50 員工、1:1」說法 | ChatGPT 未查 | mha.gov.in；indianvisaonline.gov.in |
| 台印 DTAA（2011）、印台 BIA（2018）條文；GST／扣繳／常設機構 | 雙方皆無 | 財政部；經濟部投審司；法稅專業 |
| 修繕貸款利率（SBI 7.25 vs 9.15%）、§24(b) 修繕扣除；Livspace 裁員 100 vs >1,000 | V1 矛盾，ChatGPT 未觸及（V2-IN-010） | SBI 官網；incometax.gov.in；Entrackr 原文 |
| 印地語在地來源 | V1 不足；ChatGPT 未執行印地語檢索 | Navbharat Times、Dainik Bhaskar 財經版 |

## F. 本市場 V2 信心總評與 13 欄比較表的 V2 建議值

**總評**：ChatGPT r2 的 20 條 URL 全部可開、0 失敗，對 V1 的主要貢獻不在推翻數字（0 項推翻），而在（1）把法規、外資、消費者保護與人均 GDP 的 A 級原文開頁核對，使 V1 多數【實際】項目得以標高信心；（2）補入 V1 查核誤判為「無資料」的 CoA 收費指引、HomeLane 合約工期／補償／保固，以及 Magicbricks「Home Interiors」第三口徑與二線城市結構；（3）以交易律師公告修正 HomeLane–DesignCafe「100% 併購」之敘述。市場規模仍是三種不可平均的口徑（純設計 15.6 億／廣義 310–370 億／Home Interiors 144 億），住宅單價全為業者頁，商用占比與人均翻修支出仍為低信心；Gemini 僅提供 Mordor 同值而無 URL，對來源數無貢獻。本市場 V2 整體信心由「低–中」升為「中」：法規與財報中–高、市場規模與單價低–中；內部校準資料未收到。

**13 欄比較表 V2 建議值（印度列）**：

| 欄 | V2 建議值 | 標籤 |
|---|---|---|
| 人均 GDP（美元，年） | USD 2,702（2025，World Bank WDI；IMF 2,675） | 【實際｜高】 |
| 住宅翻修市場規模 | 無純住宅翻修值；可比區間 USD 126–380 億（2025，IMARC 服務／GMI 含材料）；另 Home Interiors INR 1.27 lakh crore ≈ USD 144 億（2024，Magicbricks，含傢俱模組） | 【示意｜低｜口徑並列】 |
| 室內設計服務市場 | 純設計服務 USD 15.6 億（2024，Grand View，單源）；廣義 USD 310–370 億（2024–2025，Mordor／IMARC／TechSci 等，定義未對齊） | 【示意｜低｜單源】／【實際｜中｜多源量級一致、定義未對齊】 |
| 住宅裝修單價（每 m²，基本／中階／高階） | Rs 8,611–12,917／12,917–21,528（錨點 15,070–26,910）／21,528–37,674 per m²（2025–2026 業者頁；≈NT$4,609–13,443/m²）；Livspace 2BHK 套餐 Rs 10.59／13.68／19.19 lakh（未給面積） | 【示意｜低｜業者頁】（錨點【示意｜中】） |
| 設計費行情 | 市場 Rs 50–500/ft²（典型 100–250）或工程款 5–15%；CoA 指引室內建築服務 7.5% 工程費（專業費率表） | 【示意｜低】／【實際｜中】 |
| 30 年以上屋齡占比 | 無資料 | 缺口 |
| 中古屋交易占比 | 二手占登記住宅交易 43%（FY2025，Square Yards／GT Bharat）；二線內裝案源中古 82%（Magicbricks，非交易比、觀察期未明） | 【實際｜中】／【示意｜低】 |
| 執業管制（設計師／承包商） | 設計師無執照，僅「Architect」稱謂受 CoA 註冊保護（Architects Act §37；SC 2020；CoA 2020 公告）／承包商無全國執照；地方建管、社區 NOC 另查 | 【實際｜高】／【示意】；需專業人士最終確認 |
| 外資可 100% 持股？ | 是：未列明服務 100% 自動路徑（DPIIT 2020 綜合政策／2025 清單）；Press Note 3 對台適用無官方澄清、陸資受益人須核准；2026-05-01 起非控制陸鄰國權益 ≤10% 可依條件自動路徑 | 【實際｜高】（PN3 部分【示意｜中/低】）；需專業人士最終確認 |
| 主要平台 | Livspace、HomeLane／DesignCafe、NoBroker Interiors、Magicbricks；線上室內設計滲透 <1%（FY19，過時）；平台 GMV／抽成無資料 | 【示意】 |
| 前 3 大玩家 | 代表而非排名：Livspace（FY25 Rs 1,460 crore）、HomeLane／DesignCafe（Rs 747.8 crore）、Asian Paints Beautiful Homes（分項未揭露）；家居零售 Godrej Interio ≈ Rs 4,000 crore（FY26） | 【實際｜中】（營收）／【示意】（排名） |
| 信心 | 中（法規、外資、財報中–高；市場規模、單價低–中） | — |
