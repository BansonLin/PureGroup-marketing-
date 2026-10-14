---
ai: claude
mode: research（Claude Code 雲端會話；以 r1 筆記為基底＋補搜）
date: 2026-10-10
scope: country:VN
prompt_version: v1
notes: 單一市場深潛（country-module-template v1）。來源僅經搜尋結果內容讀取，未直接開頁；與 V1 獨立。補搜 30 次（其中在地語言 28 次）。
---

# 越南（Việt Nam，VN）室內設計與裝修市場深潛 r1：交屋潮滯後兩三年、2026 法規換軌、供應端價值大於內需

## 0. 中繼資料

| 項目 | 內容 |
|---|---|
| AI | Claude |
| 模式 | Claude Code 雲端會話 Research（以 r1 筆記為基底＋補搜） |
| 日期 | 2026-10-10 |
| 範圍 | 單一市場：越南（以台灣為比較基準） |
| 基底證據 | `03-inbox/claude/20261009_claude_12market-overview_r1_notes/VN_vietnam.md`（來源 VN-01～VN-58，r1 已搜 13 次）；匯率與總體數字取自 `TF_macro_housing_fx.md`（TF-01、TF-14、TF-18、TF-20、TF-21）；台灣錨點取自 `TW_taiwan.md`（TW-xx）及總覽 r1 第 2 章 |
| 本輪補搜 | **30 次**（硬上限 30，已用完）：越南文 28、繁體中文 1、英文 1 |
| 搜尋語言 | 越南文（主）、繁體中文、英文 |
| 來源數 | 本報告引用 **136** 個（r1 沿用 VN 來源 34、本輪新增 VN-D01～VN-D88 共 88、TF 5、TW 9）；**其中在地語言（越南文）108 個**（另有繁中 11、英文 17） |
| 匯率 | 2025 年平均：1 USD ＝ **26,005.133 VND**（TF-14，CEIC 引用世界銀行系列；**第三方年平均，非越南國家銀行原始發布**，信心中）；1 USD ＝ **31.1663 TWD**（TF-01，美國聯準會 G.5A，信心高）。交叉：1,000 VND ＝ 1.198 TWD；1 TWD ＝ 834.40 VND。1 坪 ＝ 3.3058 m²。 |
| 限制 | (1) WebFetch／curl 不可用：**所有來源僅經搜尋結果內容讀取，未直接開頁**；數字與 URL 對應不確定者標「候選」，只有標題者標「僅標題」。(2) **與 V1 獨立**：未讀取 `04-research-notes/`、`05-report/`。(3) 單價多來自業者報價頁，一律【示意】。(4) 法規結論一律「需專業人士最終確認」。(5) 搜尋配額與其他 4 個代理共用。 |

標示說明：【實際】＝官方或財報等已發生的數字；【示意】＝市調估計、業者報價、或本報告推算。信心分高／中／低。

---

## 1. 摘要

1. **需求引擎是新屋交屋後的首次裝修，且落後銷售 2～3 年**：河內 2025 年售出公寓 34,760 戶（CBRE，VN-25，【實際】，高）。新開案通常 2～3 年後才交屋（VN-D01，低），因此 2025 年的銷售高峰會在 2027–2028 年轉成 fit-out 需求（推論）。
2. **交屋標準占比仍是空白**：毛胚、基本完工、全裝修三者的比例，兩輪共 4 次搜尋都**無資料**。間接訊號是毛胚屋「完成面」另有行情 2.6～5 百萬 VND/m²（＝100～192 USD；2025，VN-D07，【示意】，低）。
3. **住宅 fit-out 三級單價**：基本 3.5～4.5、中階 5～6.5、高階 7～10 百萬 VND/m²（＝135～173／192～250／269～385 USD/m²；2025，VN-D03，【示意】，低）。中階單價 ÷ 人均 GDP 為 4.0%～5.2%，約為台灣新成屋中階（1.5%～2.5%）的 2 倍。
4. **2026-07-01 法規全面換軌**：《Luật Xây dựng 2025》與《Nghị định 212/2026/NĐ-CP》同日施行，後者取代《Nghị định 175/2024》的能力條件與執業證照規定（VN-D08、VN-D16，中）。**r1 以 175/2024 與 2014 年建設法為基礎的結論須改寫**（需專業人士最終確認）。
5. **室內設計是否需要證照出現法律衝突**：建設法體系豁免「不影響承重結構」的工作，但《Luật Kiến trúc 2019》第 19 條把 thiết kế nội thất 列為建築服務，第 21 條要求主持人持建築執業證書（2019，VN-D19，中；需專業人士最終確認）。
6. **板材與系統櫃龍頭 An Cường（ACG）2025 年營收超過 4,600 十億 VND**（＝1.77 億 USD＝55.1 億 TWD，年增 16%），淨利 504 十億 VND（年增 20%）（VN-D42，【實際】，中）。2026 上半年營收再增 33.3%，內需是主要動能。
7. **越南對台灣業者的價值在供應端**：2025 年木材及木製品出口 **17.2 十億 USD**（年增約 6%），其中 55% 銷往美國（VN-D39，【實際】，中高）。同年台資新增登記 9.658 億 USD，累計 42.37 十億 USD（VN-D48、VN-D49，中）。
8. **商辦 fit-out 單價屬亞太最低一群**：Cushman & Wakefield 2026 年版為河內 678、胡志明市 657 USD/m²（≈ 69,854／67,690 TWD/坪；VN-D76，【示意】，中）。跟隨台商做廠辦裝修，必須面對這個價格天花板。

---

## 2. 10 節正文

### Q1 市場規模與成長

**結論**：本輪補搜後，「設計服務」「住宅翻修」「商業裝修」「建商精裝」四桶仍沒有任何官方或公會口徑的規模，皆為**無資料**。可用的只有兩類：家具市調（定義不一，彼此相差 10 倍），以及出口額（【實際】）。用「每筆住宅成交觸發一次 fit-out」做代理，全國約 33.8～96.6 兆 VND（＝13.0～37.2 億 USD），占 GDP 0.26%～0.75%（【示意】）。

**全部來源並列（不取平均）**

| 來源# | 數值（原幣／換算） | 年份 | 原始定義 | 歸桶 | 現況／預測 | 標示 | 信心 |
|---|---|---|---|---|---|---|---|
| VN-02 | 1.47 十億 USD（＝458 億 TWD） | 2024 | Mordor「越南家具市場」舊版，Dân trí 轉引 | 家居零售 | 現況估計 | 【示意】 | 低 |
| VN-02 | 1.92 十億 USD（CAGR 5.33%） | 2029 | 同上 | 家居零售 | **預測** | 【示意】 | 低 |
| VN-01 | 9.76 十億 USD（＝3,042 億 TWD） | 2025 | Mordor 現行版，定義未載明 | 家居零售（範圍可能較廣） | 現況估計 | 【示意】 | 低 |
| VN-01 | 14.87 十億 USD | 2031 | 同上 | 家居零售 | **預測** | 【示意】 | 低 |
| VN-10 | 15.00 十億 USD（＝4,675 億 TWD） | 2025 | Ken Research「家具＋室內設計」合併口徑 | 混合 | 現況估計 | 【示意】 | 低 |
| VN-10 | 21.82 十億 USD（CAGR 6.45%） | 2031 | 同上 | 混合 | **預測** | 【示意】 | 低 |
| VN-06 | 21.2 百萬 USD | 2024 | IMARC 室內設計**軟體**（不是設計服務） | 其他 | 現況估計 | 【示意】 | 中 |
| VN-07 | 1,278.4 百萬 USD | 2024 | IMARC 地板市場 | 其他（建材） | 現況估計 | 【示意】 | 中 |
| VN-03 | 16.25 十億 USD | 2024 | 木材及木製品出口（海關，經 VnExpress） | 其他（出口） | 現況 | 【實際】 | 高 |
| VN-D39 | **17.2 十億 USD**（＝447.3 兆 VND＝5,361 億 TWD），年增約 6% | 2025 | 木材及木製品出口（海關），首度突破 170 億 USD | 其他（出口） | 現況 | 【實際】 | 中高 |
| — | **無資料** | — | 室內設計服務、住宅翻修、商業裝修、建商精裝 | 四桶 | — | — | — |

**合理性檢查**（分母：2025 年 GDP 12,847.6 兆 VND，Cục Thống kê 經 VN-D66；按 TF 匯率約 4,940 億 USD）
- Ken Research 的 15.00 十億 USD 約占 GDP 3.0%。內需家具＋設計占到這個比例並不合理，研判混入了生產端或出口口徑（推論）。Mordor 現行版 9.76 十億 USD 約占 2.0%，同樣偏高。
- 2024→2025 出口 16.25→17.2 十億 USD，成長率約 5.8%，與「年增約 6%」一致，雙源互證。

**示意代理（不得當作市場規模）**

| 代理 | 算式 | 結果 | 假設與偏誤 |
|---|---|---|---|
| 全國「交易觸發型」fit-out | 138,025 筆公寓＋獨棟成交（2025，VN-38）× 70 m² × 3.5～10 百萬 VND/m²（VN-D03） | 33.8～96.6 兆 VND＝13.0～37.2 億 USD＝405～1,158 億 TWD | 假設每筆成交做一次 70 m² 全室裝修。中古屋成交會被高估，非交易型翻修與商空則未計入。【示意】 |
| 同上占 GDP | ÷ 12,847.6 兆 VND（VN-D66） | 0.26%～0.75% | 同上 |
| 河內新案（滯後交屋） | 34,760 戶（VN-25）× 70 m² × 3.5～10 百萬 VND/m² | 8.5～24.3 兆 VND＝3.3～9.4 億 USD | 這筆需求約在 2027–2028 年交屋時實現（推論，依 VN-D01） |

**住宅 vs 商業、新屋 vs 存量**：無資料。**成長**：只有市調預測 CAGR 5.33%～7.28%（VN-02、VN-06、VN-10，預測）。總體面上，2025 年 GDP 實質成長 8.02%（VN-D66，【實際】），IMF 預測 2026 年為 7.10%（TF-21，預測）。

---

### Q2 需求結構

**結論**：需求主要來自一手公寓交屋。2025 年河內創紀錄的銷售，會在 2–3 年後轉成交屋裝修。胡志明市供給受限，以高端案為主。交屋標準占比、全國屋齡分布、工期仍是**無資料**。單價三級化已相當明確，只是全部來自業者報價。

**2a. 新屋供給與成交**

| 指標 | 數值 | 年份 | 來源# | 定義 | 標示 | 信心 |
|---|---|---|---|---|---|---|
| 全國公寓＋獨棟成交 | 138,025 筆 | 2025 | VN-38 | Bộ Xây dựng 彙整，未區分新屋／中古 | 【實際】 | 中 |
| 2025Q2 公寓＋獨棟成交 | 34,461 筆（年增 33.1%） | 2025Q2 | VN-37 | Bộ Xây dựng 季報 | 【實際】 | 高 |
| 河內新推出／售出公寓 | 近 36,000／34,760 戶 | 2025 | VN-25、VN-26 | CBRE 一級市場 | 【實際】 | 高 |
| 河內單價 >120 百萬 VND/m² 新推案 | 近 4,000 戶 | 2025 | VN-26 | CBRE | 【示意】 | 中 |
| 胡志明市新推出公寓 | 約 1,400 戶（去化率 74%） | 2025H1 | VN-27 | CBRE | 【示意】 | 中 |
| 胡志明市高端公寓新推出 | 5,500～6,000 戶，另有 1,300 戶 RBL 物件 | 2025 | VN-D83 | JLL，經 Real Estate Asia | **預測** | 中 |
| 開案到交屋的時間差 | 新開案通常 2～3 年後交屋；想立即入住者偏好已完工或二手屋 | 2025–2026 | VN-D01 | Wiki BĐS 分析 | 【示意】 | 低 |
| 新屋 vs 中古成交占比 | **無資料** | — | — | — | — | — |

**2b. 房價（裝修預算的分母）**

| 指標 | VND/m² | USD/m² | TWD/坪 | 年份 | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|---|---|
| 河內一手公寓均價 | 100 百萬 | 3,845 | 396,189 | 2025 | VN-36 | 【實際】 | 中 |
| 胡志明市一手公寓均價 | 111 百萬 | 4,268 | 439,770 | 2025 | VN-36 | 【實際】 | 中 |
| 河內已交屋二手公寓 | 60～70 百萬 | 2,307～2,692 | 237,714～277,333 | 2025–2026 | VN-D02 | 【示意】 | 中低 |
| 河內 2025 新案最高價 | 270 百萬 | 10,383 | 1,069,711 | 2025 | VN-D87（僅標題） | 【示意】 | 低 |
| 河內 2025 新案下限 | 「已無低於 65 百萬 VND/m² 的公寓」 | — | — | 2025 | VN-D88（僅標題） | 【示意】 | 低 |

裝修單價與房價之比：3.5～10 百萬 ÷ 100～111 百萬 ≈ 3.2%～10%（推算，【示意】）。

**2c. 存量與屋齡**
- 全國 30 年以上屋齡占比：**無資料**。
- 舊公寓（chung cư cũ）數量只有零散數字：河內約 1,579 棟，興建於 1960–1994 年（2020 年資料，VN-D79，中低）；胡志明市 1975 年前的公寓 575 棟，已鑑定 462 棟，其中 15 棟須拆除重建（年份不明，VN-D80，低）；該文標題稱「約 10 萬戶住在舊公寓」（VN-D80）。全國舊公寓超過 2,500 棟（VN-D81，低）。2026 年 1 月河內決定對 48 個坊社的所有舊公寓做鑑定，胡志明市 2025 年 9 月宣布鑑定 156 棟（VN-D82，中）。
- 判讀：這批存量走的是**拆除重建**（cải tạo, xây dựng lại），不是台灣式的室內翻修；短期內不構成老屋翻修市場（推論）。

**2d. 交屋標準（bàn giao thô／hoàn thiện cơ bản／full nội thất）**
- 占比：**無資料**（r1 第 18 次查詢被擋；本輪越南文、英文各一次仍無資料）。
- 間接證據：(i) 業者有「毛胚屋完成面」的獨立報價 2.6～5 百萬 VND/m²（＝100～192 USD），且明言不含家具（VN-D07，低），表示毛胚交屋仍存在、需多一層工程；(ii) 外籍人士租屋指南稱出租物件多為 warm shell（含燈具、冷氣、天花、地板）（VN-D84，英文，候選，低），但這是租屋市場，不是建商交屋。
- 推論：主流是「基本完工交屋＋屋主自行做活動家具與木作」，毛胚與全裝修各占一端；比例待實地向建商查證。

**2e. 住宅裝修單價（三級）**

| 等級 | VND/m² | USD/m² | TWD/坪 | 70 m² 總價 | ÷ 人均 GDP | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|---|---|---|
| 基本 | 3.5～4.5 百萬 | 135～173 | 13,867～17,829 | 245～315 百萬 VND（＝9,421～12,113 USD） | 2.79%～3.59% | VN-D03 | 【示意】 | 低 |
| 中階 | 5～6.5 百萬 | 192～250 | 19,809～25,752 | 350～455 百萬 VND（＝13,459～17,497 USD） | 3.98%～5.18% | VN-D03 | 【示意】 | 低 |
| 高階（天然木） | 7～10 百萬 | 269～385 | 27,733～39,619 | 490～700 百萬 VND（＝18,842～26,918 USD） | 5.58%～7.97% | VN-D03 | 【示意】 | 低 |

（人均 GDP 用 125.5 百萬 VND，VN-D66；改用 IMF 的 4,829 USD〔TF-18〕結果相同至小數點後一位。）

其他報價並列，口徑不同，不合併：
- r1 的 70 m² 公寓 180～450 百萬 VND，推算 2.57～6.43 百萬 VND/m²（VN-11，低）。
- 60 m² 公寓：基本 80～120、標準 120～180、高階 180 百萬 VND 以上，推算 1.3～3.0 百萬 VND/m²（VN-D04，低）。研判以活動家具套餐為主（推論）。
- 1 房 40 m² 約 130 百萬到 3 房 100 m² 約 800 百萬 VND，推算 3.25～8.0 百萬 VND/m²（VN-D05，低）。
- 「7～11 百萬 VND/m²」（VN-D06，候選，低）。
- 台灣不動產業者經營的網站 vietnamtophouse 有一個 104 m² 三房實例，裝修加採購約 14,500 USD，約 139 USD/m²（≈3.63 百萬 VND/m²≈14,365 TWD/坪；2025，VN-D46，繁中，低），落在基本到中階之間，可作交叉驗證。
- **對比台灣**：越南中階約 19,809～25,752 TWD/坪，台灣新成屋中階為每坪 6～10 萬 TWD（TW-16）。以台幣計，越南約為台灣的 2～4 成（【示意】）。

**2f. 設計費**

| 指標 | 數值 | 換算 | 年份 | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|---|
| 設計費（r1） | 150,000～200,000 VND/m²；簽施工約常可全免 | 5.8～7.7 USD/m²；594～792 TWD/坪 | 2025 | VN-16 等 | 【示意】 | 低 |
| 設計費（另案） | 250,000～350,000 VND/m² | 9.6～13.5 USD/m²；990～1,387 TWD/坪 | 2025 | VN-D05 | 【示意】 | 低 |
| 設計費占工程費 | 3.1%～10.8% | 250k～350k ÷ 3.25～8.0 百萬 | 推算 | VN-D05 | 【示意】 | 低 |

工期、翻修週期、每案全國均價：**無資料**。

**2g. 商辦 fit-out 單價（商業裝修的唯一可比數字）**

| 指標 | 數值 | 換算 | 年份 | 來源# | 定義 | 標示 | 信心 |
|---|---|---|---|---|---|---|---|
| 新辦公室 fit-out（C&W 2026 年版） | 河內 678、胡志明市 657 USD/m² | 69,854／67,690 TWD/坪；17.6／17.1 百萬 VND/m² | 2026 | VN-D76 | 亞太 fit-out 成本指南，經媒體轉引；未註明辦公室等級 | 【示意】 | 中 |
| 新辦公室 fit-out（C&W 2025 年版） | 河內 17.2、胡志明市 16.7 百萬 VND/m²，同列亞太最便宜前三名 | 661／642 USD/m² | 2025 | VN-D75 | 同上，前一版 | 【示意】 | 中 |
| 新辦公室 vs 舊辦公室改造（C&W 2022 年版） | 新辦公室約 15、舊辦公室改造約 7.4 百萬 VND/m²（標題：約 61 USD/sq ft）；範圍含家具、設計費、施工、機電、IT 與影音 | 577／285 USD/m² | 2022 | VN-D77 | 同上 | 【示意】 | 中 |
| A 級商辦租金（JLL） | 市中心毛租金胡志明市 64.7、河內 40.6 USD/m²/月；全市空置率 18.8% | — | 2026Q1 | VN-D78（候選） | 租金不是裝修費，只用來看商空需求 | 【示意】 | 中低 |

讀法：2022→2026 年新辦公室 fit-out 從約 577 漲到 657～678 USD/m²，4 年約增加 14%～18%（推算，版本間口徑可能不同）。舊辦公室改造約只有新辦公室的一半。

---

### Q3 產業結構與主要玩家

**結論**：設計施工端高度分散，公司家數與集中度**無資料**。規模化、可查證的業者集中在「板材／系統櫃製造」（ACG）與「家具零售」（AA／Nhà Xinh、JYSK、Nitori、Uma）。IKEA 截至本輪搜尋**仍未見已開店的證據**。內需市場長期被出口導向的木業忽略（VN-D37，僅標題）。

| 玩家 | 類型 | 關鍵數字 | 年份 | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|---|
| An Cường（ACG，HOSE 上市） | 板材（MDF、美耐板）＋系統櫃＋室內木作 | 營收超過 4,600 十億 VND（＝1.769 億 USD＝55.1 億 TWD），年增 16%，達計畫 114%；淨利 504 十億 VND（＝1,938 萬 USD），年增 20% | 2025 | VN-D42（r1 候選 VN-20 至此取得綁定） | 【實際】 | 中 |
| 同上 | — | 2026 上半年營收 2,349.4 十億 VND（年增 33.3%），稅後淨利 241.66 十億 VND（年增 8.4%），毛利率從 29.8% 降到 28.1%（提列呆帳） | 2026H1 | VN-D42（候選） | 【實際】 | 中 |
| 同上 | — | 2026 年計畫：股東會通過營收 5,300、淨利 604 十億 VND；另一報導稱下修為 4,811.9／550.2 | 2026 | VN-D42、VN-D43 | 計畫（矛盾） | 低 |
| 同上 | — | 2025 前三季營收 2,940.6 十億 VND（年增 6.4%）；券商稱內需中高階是 2026–2027 年主要動能 | 2025 | VN-19；VN-D44 | 【實際】／觀點 | 中／低 |
| AA Corporation（Nhà Xinh、AKA） | 商空與飯店設計施工＋家具零售 | 約 3,000 名員工、13 家公司、7 個國家（2021，VN-D29）；全球近 200 個專案，承作 Landmark 81 室內，擬 3 年內建 50 公頃工廠（2023，VN-D30）；AKA 代理約 30 個品牌、20 家以上門市（同站另處寫 30 個展示間，VN-D31）。**營收無資料** | 2021–2023 | VN-D29～D31 | 【示意】 | 低 |
| Hòa Phát | 鋼鐵集團（家具為附屬） | 集團 2025 營收 158,332 十億 VND，鋼鐵占 94%、農業占 5%；**家具營收未單獨揭露，無資料** | 2025 | VN-D45 | 【實際】（集團） | 中 |
| JYSK | 丹麥家居零售（加盟） | 2015 年經加盟進入，1,500 項以上商品；門市數各來源不一（15 家 vs 河內 8＋胡志明市 5，均為舊文） | 2015～ | VN-D32、VN-D33 | 【示意】 | 低 |
| Uma | 瑞典人創立的平價家居 | 15 家門市＋2 個設計中心 vs 河內 8＋胡志明市 9（舊文） | 2019 前後 | VN-D36 | 【示意】 | 低 |
| Nitori | 日本家居 | 胡志明市同起街（Đồng Khởi）3,000 m² 以上旗艦店，為在越第 4 家；長期目標 70 家以上 | 約 2023–2025 | VN-D34、VN-D35 | 【示意】 | 中低 |
| IKEA | 瑞典 | 2019 年宣布在河內投資約 450 百萬（USD／EUR 說法不一）設零售與倉儲中心；本輪搜尋**未見開店或線上開賣的證據** | 2019 | VN-D38、VN-D36 | — | 低 |
| BAYA | 本土家居零售 | **無資料**（本輪未取得） | — | — | — | — |
| Index Living Mall、BoConcept、Phố Xinh、Nhà Đẹp | 中高端家具零售 | 2019 年報導列為 IKEA 的主要對手，規模無資料 | 2019 | VN-D36 | 【示意】 | 低 |
| Viettel Construction（CTR） | 電信國企系統跨入住宅裝修 | 推出室內裝修業務（年份待確認） | 約 2023 | VN-42 | 【示意】 | 低 |
| Happynest | 居家社群電商平台 | 見 Q4 | 2024 | VN-D60 | — | — |

**近 3 年資本動作**：ACG 擬把子公司 1,474 萬股賣給兩名個人，並對子公司增資逾千億 VND，另關閉平新（Bình Tân）分公司（VN-23、VN-24、VN-22，僅標題）；Happynest 完成 72 萬 USD 種子輪（2024，VN-D60）。併購、倒閉：**無資料**。

---

### Q4 通路與獲客

**結論**：獲客以社群與內容為主，大型撮合平台尚未成形。唯一可查證的平台是 Happynest（社群電商），規模仍小。建商指定裝修通路、平台 GMV 與抽成都是**無資料**。

| 通路 | 關鍵事實 | 年份 | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|
| Happynest | 居家裝修社群電商，2021 年底推出網站與 App。Facebook 社團超過 48 萬人（另一越文報導為近 40 萬）；公司自稱月活 50 萬～100 萬（自報）。種子輪 72 萬 USD（＝2,244 萬 TWD），由 Touchstone Partners 領投；合作品牌有 LG、Panasonic、Bosch、Viglacera-Saint-Gobain、Nippon Paint、TOTO | 2024 | VN-D60、VN-D61 | 【實際】（募資）／【示意】（用戶） | 中／低 |
| 論壇與 SEO | VOZ 論壇詢價；業者在第三方平台自建報價頁搶 SEO | 2024–2026 | VN-15、VN-16 | 【示意】 | 低 |
| 業者手法 | 「簽施工約免設計費」「工廠直營價」「依臥室數的套餐」 | 2025–2026 | VN-11～VN-15、VN-D05 | 【示意】 | 低 |
| 展會 VietBuild | 河內 2025 年 3 月約 1,500 個攤位、400 家廠商；5 月 630 個以上；9 月 1,000 個以上、近 300 家。峴港 2025 年 5 月近 900 個攤位，其中 46 家為室內外裝飾、55 家為建材。**各屆不可加總** | 2025 | VN-D62～VN-D65 | 【實際】 | 中 |
| 建商通路、仲介轉介 | **無資料** | — | — | — | — |

---

### Q5 法規與證照（需專業人士最終確認）

**結論**：截至 2026-10，法源已換軌為《Luật Xây dựng 2025》與《Nghị định 212/2026/NĐ-CP》，兩者皆自 2026-07-01 施行。不動承重結構、不改用途的室內修繕，**仍免建築許可**（新法第 43 條第 2 項 h 款）。個人執業證照的豁免清單移到 212/2026 第 27 條第 3 項，但「室內施工監造」是否仍列入豁免，**本輪未能確認**。另一條線是《Luật Kiến trúc 2019》，它把室內設計列為建築服務，要求主持人持建築執業證書，與建設法的豁免邏輯不一致。消防方面，改造若影響防火條件，須依 2024 年新消防法與《Nghị định 105/2025》做消防設計審定。

**r1 結論的更新**：r1 說「Nghị định 212/2026 可能修正 175/2024」，本輪**確認**：212/2026 存在，自 2026-07-01 施行，取代 175/2024 中「能力條件與執業證照」部分（VN-D08、VN-D09，中）。另有一份法令對照表稱 175/2024 整體自 2026-07-01 失效，改由 2026-06-19 頒布的《Nghị định 217/2026/NĐ-CP》取代（VN-D10，低）。合理解讀是兩部新法令分別承接 175/2024 的不同部分，待以政府公報確認。

| 主題 | 法規（原名） | 主管機關 | 內容摘要 | 狀態 | 來源# | 信心 |
|---|---|---|---|---|---|---|
| 建築許可豁免 | 《Luật Xây dựng 2025》第 43 條第 2 項 h 款（取代《Luật Xây dựng 2014》第 89 條） | 國會；Bộ Xây dựng；省級 Sở Xây dựng | 工程內部修繕改造，以及不臨接有建築管理要求之都市道路的外觀修繕，在不改用途功能、不影響承重結構、符合消防、環保、基礎設施連接要求下免許可。依工程類別，部分仍須「通知」或附技術文件。2026-07-01 施行，部分條款 2026-01-01 先行 | 現行 | VN-D16、VN-D17 | 中 |
| 罰則 | 同上 | — | 擅自施工最高罰 80 百萬 VND（＝3,076 USD＝95,877 TWD） | 現行 | VN-D18（僅標題） | 低 |
| 能力條件與執業證照 | 《Nghị định 212/2026/NĐ-CP》 | 政府；Bộ Xây dựng；**自 2026-07-01 由省級人民委員會核發**（標題） | 新證照效期 10 年；停發「專案管理」「建設定價」證照，已核發者用至到期；2026-07-01 前送件者仍依 175/2024 審理；免證照清單在第 27 條第 3 項，其中有「不影響承重結構的完成工作」一類，但搜尋摘要列出的例子與室內無關；監造證照規定在第 37 條。頒布日各來源記為 2026-06-15 或 06-17 | 現行 | VN-D08、VN-D09、VN-D11～VN-D15 | 中（存在、生效日）／低（室內豁免是否延續） |
| 舊法 | 《Nghị định 175/2024/NĐ-CP》第 73 條第 3 項 c 款（r1） | — | 「不影響承重結構的完成工作之設計、審查、監造」與「工程室內施工監造」免個人證照 | **已被取代**（至少證照部分） | VN-29、VN-31；VN-D08 | 中 |
| 建築服務與室內設計 | 《Luật Kiến trúc 2019》（Luật số 40/2019/QH14）＋《Nghị định 85/2020/NĐ-CP》 | Bộ Xây dựng；省級 Sở Quy hoạch – Kiến trúc／Sở Xây dựng 核發 | 第 19 條第 2 項：建築服務包含 thiết kế nội thất。第 21 條：主持建築設計者、建築執業組織的專業負責人、以個人身分執業的建築師，須持建築執業證書；無證者可在組織內參與。第 28 條：取證要件為建築本科以上、3 年經驗、通過考核。顧問稱室內設計公司須向省級建築主管機關申報資訊（第 33 條第 1 項 c 款） | 現行 | VN-D19、VN-D20、VN-D21、VN-D22 | 中（條文）／低（實務適用） |
| 消防：新法與細則 | 《Luật Phòng cháy, chữa cháy và cứu nạn, cứu hộ 2024》；《Nghị định 105/2025/NĐ-CP》（2025-05-15 頒布）；《Thông tư 36/2025/TT-BCA》 | Bộ Công an（消防警察） | 使用期間若調整設計、改變功能或改造，須做消防設計審定（法第 17 條第 2 項），審查範圍限於改造部分。觸發例：改變火警或滅火原理、更換消防泵規格。公安機關審定據稱自 2025-07-01 起適用 | 現行 | VN-D23～VN-D26 | 中低 |
| 消防：舊細則 | 《Nghị định 50/2024/NĐ-CP》（2024-05-10，修正《Nghị định 136/2020》） | Bộ Công an | 附錄 V 所列專案在改造或改變用途時須審定的情形：增加樓層或防火分區面積、改變逃生梯、減少出口、新設或更換火警／滅火系統。消防管理對象含公寓、集合宿舍、混合用途建築；附錄 II 自 2024-05-15 適用。過渡規定：已依 136/2020 審定但尚未驗收者，續用 136/2020 與 50/2024 | 過渡適用 | VN-D27、VN-D28、VN-D26 | 中 |
| 公寓管理規約 | 《Thông tư 05/2024/TT-BXD》附《Quy chế quản lý, sử dụng nhà chung cư》（2024-08-01；經 09/2025、32/2025、08/2026 修正；2026-03-24 合併文本 17/VBHN-BXD）；胡志明市《Quyết định 26/2025/QĐ-UBND》 | Bộ Xây dựng；省市 UBND | 有規約與內規架構。**裝修登記、施工時段、施工押金的具體條文無資料** | 現行 | VN-D73、VN-D74 | 中（存在）／無資料（細節） |
| 內裝材料防火等級 | 國家技術規範（QCVN 06 等） | Bộ Xây dựng | **無資料**（本輪未搜） | — | — | — |

**實務推論（信心低）**：一般公寓內部 fit-out 只要不動結構、不改消防系統，原則上免建築許可、免消防審定，但仍受公寓規約管理。商空（餐飲、辦公室）若改變用途或更動撒水、火警系統，須做消防審定。設計公司若以「建築服務」名義經營，須配置持建築執業證書的專業負責人（依 VN-D19、VN-D21）。

---

### Q6 消費者保護與糾紛

**結論**：主管機關沒有拆出「裝修」類申訴統計。業者合約範本的訂金偏高（50%），保固年限常留白，追加費用（phát sinh）是結構性爭議點。履約保證與保險：**無資料**。

| 主題 | 內容 | 年份 | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|
| 主管機關與申訴量 | 原 Cục Cạnh tranh và Bảo vệ người tiêu dùng 已改組為 **Ủy ban Cạnh tranh Quốc gia（國家競爭委員會）**；2025 年 1–9 月受理全國消費者申訴、陳情 642 件，未拆出裝修類 | 2025 | VN-D58 | 【實際】 | 中 |
| 申訴管道 | 專線 1800.6838、bvntd 網站（來自較舊報導） | 舊 | VN-D86 | 【示意】 | 低 |
| 業者合約範本 | 預付 50%，餘款於安裝完成後 3 日內付清；保固年限留白，接到通知後 7 日內開始維修；逾期罰款每週 2%；報價未含 10% 增值稅；追加項目另簽附約 | 年份不明 | VN-D71（候選） | 【示意】 | 低 |
| 建設合約預付上限 | 簽約時預付不得超過合約價值 30%（適用建設法規範的合約；民間室內合約是否適用待確認） | 2026 | VN-D72 | 【示意】 | 中低 |
| 消費者建議 | 修繕訂金不宜超過 30% | 年份不明 | VN-D59（候選） | 【示意】 | 低 |
| 詐騙型態、履約保證、保險、標準合約範本（官方） | **無資料** | — | — | — | — |

---

### Q7 外資／台資進入規則（需專業人士最終確認）

**結論**：施工端依 WTO 承諾可 100% 外資；「室內設計」不在 WTO 承諾內，國內法又把它歸為建築服務。因此外資設計公司除了要經主管部會個案同意，很可能還須配置持越南建築執業證書的負責人（推論）。外國承包商的個案許可，自 2026 年起改適用新法令的表單（VN-53）。台資在越製造業基礎深厚，北部電子業聚落持續擴大，是「跟隨客戶」型進入的需求來源。

| 主題 | 規則／事實 | 來源# | 標示 | 信心 |
|---|---|---|---|---|
| 建設服務（CPC 511–518） | WTO 承諾無持股上限，2009 年起可設 100% 外資企業 | VN-44、VN-48 | 【實際】 | 中 |
| 室內設計（CPC 87907） | 越南未作承諾；外資登記須經主管部會同意 | VN-46、VN-47 | 【實際】 | 中 |
| 國內法定性 | 《Luật Kiến trúc 2019》把 thiết kế nội thất 列為建築服務，主持人須持證 | VN-D19 | 【實際】（條文） | 中 |
| 外國承包商許可 | 175/2024 第 114、115 條：須得標或獲選，並與越方聯營或使用越南分包商。2026-05-13 起申請文件更新，2026-07-01 起適用 212/2026 新表單；許可程序是否改由 217/2026 規範，未確認 | VN-52、VN-53、VN-D10 | 【實際】／【示意】 | 中／低 |
| 外籍工作許可 | 《Nghị định 219/2025/NĐ-CP》自 2025-08-07 生效，審查期限 10 個工作日，由省級 UBND 核發 | VN-55、VN-56 | 【實際】 | 中 |
| 台資規模 | 2025 年新增登記 965.8 百萬 USD（＝301 億 TWD），居第 6、占 5.6%；累計 3,457 案、42.37 十億 USD（＝1.32 兆 TWD），居第 4（至 2026-04） | VN-D48、VN-D49（候選） | 【實際】 | 中 |
| 台資北部案例 | 鴻海北寧 PCB 383 百萬 USD；2024 年廣寧兩案合計 551 百萬 USD；廣達南定 120 百萬 USD | VN-D85（候選） | 【實際】 | 中低 |
| 台灣設計公司在越案例 | 頭頓 450 m² 商辦，設計團隊與建商從初步設計起整合建築與室內，土木、室內、機電分包（VN-D47）；台灣不動產業者經營越南住宅裝修資訊網站（VN-D46）。**台商廠辦宿舍統包業者名單：無資料** | VN-D46、VN-D47 | 【示意】 | 低 |
| 稅務 | 本輪未搜（不提供稅務建議） | — | — | — |

---

### Q8 消費者行為

**結論**：預購族（投資）與自住族分流明顯：自住者偏好已完工或二手屋，期房買家則在交屋時才集中裝修（VN-D01，低）。預算依臥室數套餐化，2 房標準方案約 120～180 百萬 VND（＝4,615～6,922 USD）。高端客群在河內擴大。融資、補助、決策歷程：**無資料**。

| 面向 | 觀察 | 來源# | 標示 | 信心 |
|---|---|---|---|---|
| 預算分級 | 60 m² 基本 80～120、標準 120～180 百萬 VND；70 m² 中階 350～455 百萬 VND | VN-D04、VN-D03 | 【示意】 | 低 |
| 高端區隔 | 河內單價 >120 百萬 VND/m² 新案近 4,000 戶（2025）；最高 270 百萬 VND/m² | VN-26、VN-D87 | 【示意】 | 中／低 |
| 資訊蒐集 | 社群（Happynest 社團 48 萬人）、論壇（VOZ） | VN-D60、VN-15 | 【示意】 | 低 |
| 付款 | 合約範本預付 50% | VN-D71 | 【示意】 | 低 |
| 風格 | 現代、北歐、極簡為報價頁常見分類（設計費 200,000 VND/m²） | VN-11～VN-15 | 【示意】 | 低 |
| 屋主年齡、所得層、決策者、融資與補助 | **無資料** | — | — | — |

---

### Q9 人才與工班

**結論**：設計師月薪約 8～14 百萬 VND（＝308～538 USD），約為台幣 1～1.7 萬元。官方工資單價河內最高 416,000 VND／日（＝16 USD＝499 TWD）。人力成本低，但缺持證主持人（見 Q5）。科系畢業人數、持證人數、缺工程度：**無資料**。

| 指標 | 數值 | 換算 | 年份 | 來源# | 定義 | 標示 | 信心 |
|---|---|---|---|---|---|---|---|
| 室內設計人員平均月薪 | 約 10 百萬 VND（常見 8～14 百萬） | 385（308～538）USD；11,985（9,588～16,779）TWD | 2026 | VN-D68 | 人力銀行估計 | 【示意】 | 中低 |
| 初階職缺（胡志明市） | 10～20 百萬 VND／月 | 385～769 USD | 2025–2026 | VN-D69 | 單一職缺 | 【示意】 | 低 |
| 資深概念／3D 設計 | 20～30 百萬 VND／月 | 769～1,154 USD；23,969～35,954 TWD | 年份不明 | VN-D70 | 部落格 | 【示意】 | 低 |
| 河內官方建設工資單價上限 | 416,000 VND／日 | 16.0 USD；499 TWD | 2025-12-22 起 | VN-D50 | 《QĐ 3461/QĐ-SXD》，屬估價用單價，不是市場實付；河內另有 2026-07-01 起的新單價（14502/SXD-KTXD），數字未取得 | 【實際】（官方單價） | 中 |
| 太原省一級技工單價 | 170,000～182,000 VND／日 | 6.5～7.0 USD | 2025 | VN-D51 | 省建設廳公告 | 【實際】 | 中 |
| 胡志明市木工職缺 | 10～18 百萬 VND／月 | 385～692 USD；11,985～21,572 TWD | 2025–2026 | VN-D52（候選） | 徵才廣告 | 【示意】 | 低 |
| 胡志明市泥作職缺 | 師傅 600,000 VND 起、助手 500,000 VND 起（計薪單位不明，推測為日薪） | 23.1／19.2 USD | 2025–2026 | VN-D53 | 徵才廣告 | 【示意】 | 低 |
| 設計科系畢業人數、持證人數、缺工 | **無資料**（建築證照由各省 Sở 以決定書核發，可見 2025 年河內核發紀錄） | — | — | VN-D22 | — | — | — |

---

### Q10 材料供應鏈與價格

**結論**：越南是全球主要木製家具出口國。2025 年美國關稅與 232 調查壓縮出口，龍頭轉向內需，國內板材與系統櫃的價格競爭可能加劇（推論）。2025 年建材價格指數僅漲 3.1%，但砂石大漲，推高土建與泥作成本。2022–2024 年的漲幅、進口依賴度、MDF 與磁磚價格：**無資料**。

| 指標 | 數值 | 年份 | 來源# | 定義 | 標示 | 信心 |
|---|---|---|---|---|---|---|
| 木材及木製品出口 | 17.2 十億 USD（年增約 6%）；未達 18 十億目標 | 2025 | VN-D39、VN-D40 | 海關 | 【實際】 | 中高 |
| 對美出口 | 9.46 十億 USD（年增 4.4%，占 55%） | 2025 | VN-D39 | 海關 | 【實際】 | 中 |
| 美國對等關稅 | 20%，2025-08-07 起（由 46% 談判降至此）；另有對木材的 232 調查，稅率可能最高 25% | 2025 | VN-D41（候選） | 摘要註明出自彙整來源 | 【示意】 | 低 |
| 建設用原物料價格指數 | 年增 3.1% | 2025 | VN-D55（候選） | Cục Thống kê | 【實際】 | 中 |
| 砂、石、礫、黏土 | 全年平均 +18.2%，第 4 季年增 29.57%；天然砂部分地區到第 2 季末年增最高 58.4%（建設經濟研究院） | 2025 | VN-D55（候選） | 統計＋研究院 | 【實際】 | 中 |
| 鋼筋、水泥 | 鋼筋 +7%～8%、水泥 +3%～5% | 2025 年中 | VN-D55（候選） | **預測** | — | 低 |
| 2026 年初 | 建材價格持續小漲 | 2026 | VN-D56 | 媒體 | 【示意】 | 中低 |
| 官方價格公告進度 | 截至 2026-01-31，34 個省市中 29 個已公告到 2025 年 12 月或第 4 季的材料價，23 個已公告價格指數 | 2026 | VN-D54 | 《Công văn 1966/BXD-KTQLXD》 | 【實際】 | 中 |
| 商業牌價 | 鋼筋 13,500～17,500 VND/kg；水泥每 50 kg 包 75,000～110,000 VND | 2026 | VN-D57（候選） | 業者牌價 | 【示意】 | 低 |
| 在地品牌 | ACG（板材）、Viglacera（衛浴、磁磚；與 Saint-Gobain 合作，見 VN-D60）；Đồng Tâm 等**無資料** | — | VN-D42、VN-D60 | — | — | — |
| 2022–2024 漲幅、進口依賴、關稅與標準 | **無資料** | — | — | — | — | — |

---

## 3. 對台灣業者（璞石集團）的啟示

1. **先把越南當「供應基地」，再談市場進入（家居零售線）**。2025 年木製品出口 17.2 十億 USD，55% 依賴美國，又受 20% 對等關稅與 232 調查壓力（VN-D39、VN-D41）。ACG 等板材與系統櫃商正把產能轉向內需與非美客戶（VN-D42）。建議璞石以宜蘭、信義門市為出口端，試做「越南系統櫃板材＋活動家具」的 OEM／ODM 小批量採購，並利用 VietBuild（河內一年三屆、單屆最多約 1,500 個攤位，VN-D62）找供應商。議價空間擴大屬推論，須以實際報價驗證。
2. **跟著台商廠辦宿舍走，但用「台灣設計＋越南施工夥伴」的輕資產架構**。台資累計 42.37 十億 USD，2025 年仍新增 9.66 億 USD，北部電子業聚落是需求來源（VN-D48、VN-D49、VN-D85）。外國承包商必須與越方聯營或分包（VN-52），室內設計又須持證主持人（VN-D19）。較穩的做法是由台灣端負責設計、標準與監造，在地與持證的越南設計施工公司簽合作，不急著設 100% 外資施工主體。商辦 fit-out 只有 657～678 USD/m²（VN-D76），報價必須以越南成本結構計算。
3. **住宅端只鎖定高端，並對準 2027–2028 年的交屋潮**。河內 2025 年售出 34,760 戶，2～3 年後才交屋（VN-25、VN-D01）；單價超過 120 百萬 VND/m² 的高端新案近 4,000 戶（VN-26）。大眾市場中階約 2～2.6 萬 TWD/坪，只有台灣的 2～4 成，設計費常被免收（VN-D03、VN-D05）。台灣設計的溢價只適合高端。可考慮與河內大型案建商合作樣品屋與客變套餐，把「不動產＋裝修」一條龍的經驗複製過去（推論）。
4. **2026 年法規換軌，進入前先取得越南律師意見**。《Luật Xây dựng 2025》與《Nghị định 212/2026》2026-07-01 才施行，執業證照改由省級核發（VN-D15）。「室內設計需不需要建築執業證書」在兩套法律之間不一致（VN-D19 vs VN-29）。消防審定已移交公安體系（VN-D23）。以上任何一點判斷錯誤，都可能讓商空案無法驗收（需專業人士最終確認）。
5. **資料缺口大，決策前先做 2 週實地調查**。交屋標準占比、設計公司家數、平台滲透率仍是無資料，市場規模各來源相差 10 倍（Q1）。建議拜訪 3～5 家河內、胡志明市建商與 ACG 展示中心，蒐集 10～20 份真實報價與合約，補齊單價、工期與付款條件。

---

## 4. 與台灣比較的錨點

| 錨點 | 越南 | 台灣 | 算式與備註 | 標示 |
|---|---|---|---|---|
| 人均翻修支出 | **官方：無資料**。示意代理（交易觸發 fit-out）：**12.7～36.3 USD／人**（330,328～943,795 VND） | 757 USD／人（5,500 億 TWD 上限值，TW-23）；或 275 USD／人（ABRI 2,000 億 TWD，2000 年代分子，TW-26） | 越南：138,025 筆（VN-38）× 70 m² × 3.5～10 百萬 VND（VN-D03）÷ 人口 102.37 百萬（＝GDP 12,847.6 兆 ÷ 人均 125.5 百萬 VND，VN-D66 導出）。台灣：÷ 23.30 百萬人（TF 隱含）、÷ 31.1663 | 【示意】 |
| 翻修市場占 GDP 比 | **官方：無資料**。示意代理：**0.26%～0.75%** | 1.92%（上限值）／0.70%（ABRI 舊數） | 越南代理 ÷ 12,847.6 兆 VND；台灣 ÷ 9,200.5 億 USD（TF-20） | 【示意】 |
| 每 m² 單價 ÷ 人均 GDP | 基本 2.79%～3.59%；**中階 3.98%～5.18%**；高階 5.58%～7.97%（VN-D03）。r1 口徑：2.05%／2.84%～3.75%／5.12%（VN-11） | 基本 0.74%～1.47%；**中階（新成屋）1.47%～2.46%**；中古屋 2.46%～3.69%；高階 3.69%～4.92% | 越南：VND/m² ÷ 125.5 百萬 VND（用 IMF 4,829 USD〔TF-18〕結果相同）。台灣：每坪 3～20 萬 TWD ÷ 3.3058 ÷ 31.1663 ÷ 39,489 USD（TF-18；單價 TW-16、TW-19、TW-22） | 【示意】 |
| 設計費占工程費比 | **3.1%～10.8%**（VN-D05）；r1 口徑 2.3%～7.8%；常因簽施工約而全免，實際有效費率可能趨近 0 | 13%～15%（20 坪新成屋，TW-21） | 越南：250k～350k VND/m² ÷ 3.25～8.0 百萬 VND/m² | 【示意】 |
| 設計公司家數 ÷ 人口 | **無資料** | 21.3 家／10 萬人（4,969 家室內裝修業，2011，TW-30 ÷ 23.30 百萬人，年份錯配） | — | 【示意】 |
| 平台滲透率 | **無資料**。僅有社群規模代理：Happynest 社團 48 萬人＝人口 0.47%；自報月活 0.49%～0.98%（VN-D60） | **無資料** | 社群人數 ÷ 102.37 百萬人。這不是交易滲透率，不可與他國平台 GMV 比較 | 【示意】 |
| （補充）新屋需求量 | 河內售出公寓 34,760 戶（2025，VN-25） | 住宅類使用執照 13.8 萬戶（2024，TW-41） | 口徑不同：越南為單一城市銷售，台灣為全國完工 | 【實際】 |
| （補充）屋齡 | 全國 30 年以上占比無資料；舊公寓 >2,500 棟（VN-D81） | 30 年以上住宅約 59%（2025Q2，TW-13） | 越南存量以拆除重建處理 | 【實際】／【示意】 |

**讀法**：越南單價對所得的負擔約為台灣的 2 倍，但絕對金額只有台灣的 2～4 成。設計費率約為台灣的一半或更低。人均支出（代理）約為台灣上限值的 2%～5%。這三者共同指向：越南的機會在**採購**與**高端利基**，而非大眾裝修服務（推論）。

---

## 5. 矛盾資料與資料缺口

### 5a. 矛盾表

| 指標 | 來源 1 | 來源 2 | 差異原因 | 裁決 |
|---|---|---|---|---|
| 取代 175/2024 的法令 | VN-D08、VN-D09：《Nghị định 212/2026》取代能力與證照部分，2026-07-01 施行 | VN-D10：175/2024 整體自 2026-07-01 失效，由 2026-06-19 頒布的《Nghị định 217/2026》取代 | 兩部法令可能分別承接 175/2024 的不同章節；頒布日另有 06-15 與 06-17 兩說 | 以 212/2026 為證照依據；217/2026 的範圍待查政府公報 |
| 室內設計是否需證照 | VN-29、VN-31：175/2024 第 73.3c 豁免非結構完成工作的設計與室內監造 | VN-D19：《Luật Kiến trúc 2019》第 19、21 條，室內設計屬建築服務，主持人須持建築執業證書 | **法律體系不同**：建設法管「建設活動證照」，建築法管「建築服務證照」 | 兩者並存；實務上配置持證建築師最保守；需專業人士最終確認 |
| 人均 GDP 2025 | VN-D67：5,026 USD（Cục Thống kê） | TF-18：4,829 USD（IMF） | **匯率**：統計局隱含約 24,970 VND/USD；TF 採 26,005 | 以本幣 125.5 百萬 VND 為準，換算一律用 TF 匯率（＝4,826 USD，與 IMF 一致） |
| GDP 2025（USD） | VN-D66：514 十億 USD | 本報告以 TF 匯率換算：494.0 十億 USD | 同上（匯率口徑） | 採 TF 換算，註明差異 |
| 住宅 fit-out 單價 | VN-D03：3.5～10 百萬 VND/m² | VN-11：2.57～6.43；VN-D04：約 1.3～3.0；VN-D06：7～11 | **範圍**：活動家具套餐、固定木作、天然木、是否含家電 | 並列不平均；本報告以 VN-D03 三級為錨，其餘作區間 |
| ACG 2026 計畫 | VN-D42：營收 5,300、淨利 604 十億 VND（股東會通過） | VN-D43：下修為 4,811.9／550.2 | **時點**：股東會後再調整（同一報導內部也有矛盾） | 以 HOSE 公告為準，待查 |
| AKA 門市數 | VN-D31：20 家以上 | VN-D31 同站：30 個展示間 | 口徑（門市 vs 展示間／含加盟） | 低信心，不引用為單一數字 |
| JYSK／Uma 門市數 | 15 家；15＋2 | 8＋5；8＋9 | **年份**（皆為 2019 年前後舊文） | 皆過時，列為無資料（現況） |
| IKEA 投資額 | VN-D38：450 百萬 USD | 搜尋摘要另見「450 百萬 EUR」 | 幣別轉述差異；且為 2019 年計畫 | 不採用；現況無資料 |
| 建材漲幅 | VN-D55：建材指數 +3.1% | VN-D55：砂石 +18.2%（第 4 季 +29.57%） | **範圍**：總指數 vs 單一品類 | 並列；室內裝修材料（板材、磁磚）無資料 |
| 河內公寓價格 | VN-36：一手均價 100 百萬 VND/m² | VN-D02：已交屋二手 60～70 百萬 | **市場層級**不同（一手新案 vs 二手） | 不是矛盾；分母分別使用 |
| 商辦 fit-out | VN-D75：2025 年河內 17.2、胡志明市 16.7 百萬 VND/m²（＝661／642 USD） | VN-D76：2026 年版 678／657 USD/m² | **版次**；差異 <5% | 採 2026 年版，並列 2025 年版 |
| Happynest 社群規模 | VN-D60：48 萬人以上 | VN-D61：近 40 萬人 | **時點**不同（差約 20%） | 採 TechNode 2024 年數字，註明自報 |

### 5b. 資料缺口表

| 缺口 | 本輪嘗試 | 建議取得方式 |
|---|---|---|
| 交屋標準占比（毛胚／基本／全裝修） | 越南文 1 次、英文 1 次，皆無 | 向 CBRE、Savills、DKRA 索取專案層級資料；實地訪談河內文江大型案建商 |
| 設計服務、住宅翻修、商業裝修市場規模 | r1 已搜；本輪未再搜 | Cục Thống kê 營建業細分產值；VIFOREST／HAWA 內需報告 |
| 設計公司家數、集中度 | 未搜（配額） | 企業登記資料庫依 VSIC 7110／7410 篩選 |
| 平台用戶、GMV、抽成 | Happynest 只有募資與社群數 | 直接洽 Happynest；Facebook 社團規模盤點 |
| HAWA／VIFOREST 協會報告 | 搜尋結果未出現兩協會 | 協會官網年報（2025 出口與內需估計） |
| Hòa Phát 家具、BAYA、AA 營收 | 搜 2 次，無 | HPG 年報分部資訊；企業登記財報 |
| IKEA 越南現況 | 搜 1 次，只有 2019 年計畫 | Ingka 年報、越南工商部投資登記 |
| 《Nghị định 212/2026》第 27.3 條全文（室內監造豁免）、《Nghị định 217/2026》範圍 | 搜 2 次，只有二手摘要 | 政府公報或 thuvienphapluat 全文 |
| 公寓裝修登記、施工時段、押金 | 搜 1 次，只確認規約存在 | 17/VBHN-BXD 全文；各大樓內規 |
| 內裝材料防火規範（QCVN 06） | 未搜 | Bộ Xây dựng 規範文本 |
| 裝修類消費申訴拆分 | 搜 1 次，只有總數 642 件 | 向國家競爭委員會申請分類統計 |
| 2022–2024 建材與板材漲幅、MDF 與磁磚價 | 搜 2 次，只有 2025 年 | Cục Thống kê 季度建設價格指數；ACG 價目表 |
| 設計科系畢業人數、持證建築師數 | 未搜 | Bộ Giáo dục 統計；Bộ Xây dựng 證照資料庫 |
| 工期、付款階段的市場慣例 | 只有單一合約範本 | 蒐集 10～20 份真實合約 |
| 台商廠辦裝修業者名單 | 繁中 1 次，無 | 越南台灣商會聯合總會、各地台商會 |
| 台灣側：師傅日薪、平台滲透率、台北商辦 fit-out 成本 | TW 筆記亦無資料 | 勞動部職類薪資調查；C&W 台北 fit-out 指南 |

---

## 6. 來源清單

（讀取方式一律為「搜尋結果內容」，未直接開頁；「候選」＝數字與 URL 的對應未能逐字確認；「僅標題」＝只有標題可支撐。）

### 6a. 沿用 r1（VN-01～VN-58 中本報告引用者）

| # | 標題 | 機構 | 年份 | 語言 | URL | 讀取方式 |
|---|---|---|---|---|---|---|
| VN-01 | Quy mô thị trường nội thất Việt Nam（Vietnam Furniture Market） | Mordor Intelligence | 2025–2026 | 越 | https://www.mordorintelligence.com/industry-reports/vietnam-furniture-market | 搜尋結果內容 |
| VN-02 | Vì sao ngành nội thất Việt Nam chưa ghi dấu ấn trên thế giới? | Dân trí | 2025 | 越 | https://dantri.com.vn/bat-dong-san/vi-sao-nganh-noi-that-viet-nam-chua-ghi-dau-an-tren-the-gioi-20250607213731069.htm | 搜尋結果內容 |
| VN-03 | Bài toán 18 tỷ USD của xuất khẩu gỗ nội thất | VnExpress | 2025 | 越 | https://vnexpress.net/bai-toan-18-ty-usd-cua-xuat-khau-go-noi-that-4843845.html | 搜尋結果內容 |
| VN-06 | Vietnam Interior Design Software Market | IMARC Group | 2025 | 英 | https://www.imarcgroup.com/vietnam-interior-design-software-market | 搜尋結果內容 |
| VN-07 | Vietnam Flooring Market | IMARC Group | 2025 | 英 | https://www.imarcgroup.com/vietnam-flooring-market | 搜尋結果內容 |
| VN-10 | Vietnam Furniture and Interior Design Market | Ken Research | 2025–2026 | 英 | https://www.kenresearch.com/industry-reports/vietnam-furniture-and-interior-design-market.md | 搜尋結果內容 |
| VN-11 | Chi phí làm nội thất chung cư 70m2: Báo giá & kinh nghiệm thực tế | Takenli（業者） | 2025–2026 | 越 | https://takenli.vn/chi-phi-lam-noi-that-chung-cu-70m2-bao-gia-kinh-nghiem-thuc-te/ | 搜尋結果內容（候選） |
| VN-12 | [Báo giá] Thi công nội thất chung cư trọn gói giá tại xưởng 2026 | Lanha（業者） | 2026 | 越 | https://www.lanha.vn/thi-cong-noi-that-chung-cu/ | 搜尋結果內容（候選） |
| VN-13 | Báo Giá Thi Công Nội Thất Chung Cư HCM Trọn Gói T9/2025 | Nội thất Bến Thành（業者） | 2025 | 越 | https://noithatbenthanh.vn/thi-cong-noi-that-can-ho-tron-goi-tphcm/ | 搜尋結果內容（候選） |
| VN-14 | Báo giá thiết kế thi công nội thất chung cư trọn gói năm 2024-2025 | Đồ gỗ Lê Gia（業者） | 2024–2025 | 越 | https://dogolegia.vn/bao-gia-thiet-ke-thi-cong-noi-that-chung-cu-tron-goi-nam-2025/ | 搜尋結果內容（候選） |
| VN-15 | Chi phí làm Nội Thất 1 Căn Hộ Chung Cư là bao nhiêu? | VOZ 論壇 | 年份不明 | 越 | https://voz.vn/t/chi-phi-lam-noi-that-1-can-ho-chung-cu-la-bao-nhieu.530354/ | 搜尋結果內容（候選） |
| VN-16 | Báo giá thiết kế văn phòng | thietkenoithat（coda.io） | 年份不明 | 越 | https://coda.io/@thietkenoithat/bao-gia-thiet-ke-van-phong | 搜尋結果內容 |
| VN-19 | Gỗ An Cường (ACG) sắp rót 196 tỷ đồng cổ tức, hoàn thành 80% kế hoạch lợi nhuận năm 2025 | Báo Pháp luật VN – Doanh nhân | 2025 | 越 | https://doanhnhan.baophapluat.vn/go-an-cuong-acg-sap-rot-196-ty-dong-co-tuc-hoan-thanh-80-ke-hoach-loi-nhuan-nam-2025-88438.html | 搜尋結果內容 |
| VN-20 | ACG tạo sức bật từ nội địa | Diễn đàn Doanh nghiệp | 2025–2026 | 越 | https://diendandoanhnghiep.vn/acg-tao-suc-bat-tu-noi-dia-10165333.html | 搜尋結果內容（候選） |
| VN-22 | Đóng cửa 1 chi nhánh tại Bình Tân, Gỗ An Cường (ACG) kinh doanh ra sao? | Báo Pháp luật VN – Doanh nhân | 年份不明 | 越 | https://doanhnhan.baophapluat.vn/dong-cua-1-chi-nhanh-tai-binh-tan-go-an-cuong-acg-kinh-doanh-ra-sao-80761.html | 僅標題 |
| VN-23 | Gỗ An Cường (ACG) muốn bán 14,74 triệu cổ phiếu công ty con cho hai cá nhân | Báo Pháp luật VN – Doanh nhân | 年份不明 | 越 | https://doanhnhan.baophapluat.vn/go-an-cuong-acg-muon-ban-14-74-trieu-co-phieu-cong-ty-con-cho-hai-ca-nhan.html | 僅標題 |
| VN-24 | Gỗ An Cường (ACG) muốn rót nghìn tỷ đồng vào công ty con | Báo Pháp luật VN – Doanh nhân | 年份不明 | 越 | https://doanhnhan.baophapluat.vn/go-an-cuong-acg-muon-rot-nghin-ty-dong-vao-cong-ty-con-86302.html | 僅標題 |
| VN-25 | Hanoi Figures Q4 2025 | CBRE Vietnam | 2026 | 英 | https://www.cbrevietnam.com/insights/figures/hanoi-figures-q4-2025 | 搜尋結果內容 |
| VN-26 | Hà Nội apartment market sees record supply, clear price difference | Việt Nam News | 2026 | 英 | https://vietnamnews.vn/economy/1763814/ha-noi-apartment-market-sees-record-supply-clear-price-difference.html | 搜尋結果內容 |
| VN-27 | HCMC apartment prices continue to rise as supply hits 10-year low in H1 | The Investor | 2025 | 英 | https://theinvestor.vn/hcmc-apartment-prices-continue-to-rise-as-supply-hits-10-year-low-in-h1-d16321.html | 搜尋結果內容 |
| VN-29 | Nghị định 175/2024/NĐ-CP（法規全文頁） | GXD | 2024 | 越 | https://cchn.gxd.vn/van-ban/qlda/nghi-dinh-175-2024.html | 搜尋結果內容 |
| VN-31 | Cục Quản lý hoạt động xây dựng hướng dẫn pháp luật về chứng chỉ hành nghề（175/2024 簡報） | Cục Quản lý hoạt động xây dựng（Bộ Xây dựng） | 2025 | 越 | http://www.quangdaqs.vn/data/files/NGHI%CC%A3%20%C4%90I%CC%A3NH%20175_2024_N%C4%90CP%20-%20SLIDE%20VE%CC%82%CC%80%20CHU%CC%9B%CC%81NG%20CHI%CC%89%20HA%CC%80NH%20NGHE%CC%82%CC%80.pdf | 搜尋結果內容 |
| VN-36 | Giá chung cư ở một số khu vực đã tăng hơn 40% | VnEconomy | 2025–2026 | 越 | https://vneconomy.vn/gia-chung-cu-o-mot-so-khu-vuc-da-tang-hon-40.htm | 搜尋結果內容 |
| VN-37 | Bộ Xây dựng công bố thông tin về nhà ở và thị trường bất động sản trong Quý II năm 2025 | Bộ Xây dựng | 2025 | 越 | https://moc.gov.vn/vn/tin-tuc/1269/87076/bo-xay-dung-cong-bo-thong-tin-ve-nha-o-va-thi-truong-bat-dong-san-trong-quy-ii-nam-2025.aspx | 搜尋結果內容 |
| VN-38 | Nguồn cung tăng, giá nhà chưa giảm | Báo Chính phủ | 2026 | 越 | https://baochinhphu.vn/nguon-cung-tang-gia-nha-chua-giam-102260117005432583.htm | 搜尋結果內容 |
| VN-42 | Viettel Construction ra mắt mảng nội thất | VnExpress | 約 2023 | 越 | https://vnexpress.net/viettel-construction-ra-mat-mang-noi-that-4596449.html | 僅標題 |
| VN-44 | Cam Kết Chung Về Dịch Vụ Của Việt Nam Trong WTO | Trung tâm WTO và Hội nhập（VCCI） | 2007 | 越 | https://trungtamwto.vn/upload/files/wto/7-/25-van-kien/Cam%20ket%20chung%20ve%20Dich%20vu.pdf | 搜尋結果內容 |
| VN-46 | Người nước ngoài có được đầu tư hoạt động thiết kế nội thất? | Báo Chính phủ | 年份不明 | 越 | https://baochinhphu.vn/nguoi-nuoc-ngoai-co-duoc-dau-tu-hoat-dong-thiet-ke-noi-that-102272847.htm | 搜尋結果內容 |
| VN-47 | Hoạt động dịch vụ kiến trúc tại Việt Nam, nhà đầu tư cần biết | PLF | 年份不明 | 越 | https://plf.vn/vi/hoat-dong-dich-vu-kien-truc-tai-viet-nam-nha-dau-tu-can-biet/ | 搜尋結果內容 |
| VN-48 | Những nội dung cơ bản các cam kết gia nhập WTO của Việt Nam | Nhân Dân | 年份不明 | 越 | https://nhandan.vn/nhung-noi-dung-co-ban-cac-cam-ket-gia-nhap-wto-cua-viet-nam-post589471.html | 搜尋結果內容（候選） |
| VN-52 | Nhà thầu nước ngoài là gì? Quy định về nhà thầu nước ngoài | DauThau.asia | 2025–2026 | 越 | https://dauthau.asia/news/tu-lieu-cho-nha-thau/nha-thau-nuoc-ngoai-1748.html | 搜尋結果內容 |
| VN-53 | Tổng hợp thành phần hồ sơ cấp giấy phép hoạt động xây dựng cho nhà thầu nước ngoài từ 13/5/2026 | Thư viện Nhà đất | 2026 | 越 | https://thuviennhadat.vn/phap-ly-nha-dat/tong-hop-thanh-phan-ho-so-cap-giay-phep-hoat-dong-xay-dung-cho-nha-thau-nuoc-ngoai-tu-13-5-2026-739116.html | 搜尋結果內容 |
| VN-55 | 10 điểm mới về người lao động nước ngoài tại Việt Nam từ ngày 07/8/2025 theo nghị định 219/2025/NĐ-CP | Pháp luật Doanh nghiệp | 2025 | 越 | https://phapluatdoanhnghiep.vn/10-diem-moi-ve-nguoi-lao-dong-nuoc-ngoai-tai-viet-nam-tu-ngay-07-8-2025-theo-nghi-dinh-219-2025-nd-cp/ | 搜尋結果內容 |
| VN-56 | Decree 219 regulating foreign workers working in Vietnam（越文版） | KPMG Vietnam | 2025 | 越 | https://kpmg.com/vn/vi/home/phan-tich-chuyen-sau/2025/08/decree-219-regulating-foreign-workers-working-in-vietnam.html | 搜尋結果內容 |

### 6b. 本輪新增（VN-D01～VN-D88）

| # | 標題 | 機構 | 年份 | 語言 | URL | 讀取方式 |
|---|---|---|---|---|---|---|
| VN-D01 | Giá Chung Cư Hà Nội Tăng Cao, Tỉ Lệ Hấp Thụ Vẫn Tích Cực | Wiki BĐS（batdongsan.com.vn） | 2025–2026 | 越 | https://wiki.batdongsan.com.vn/phan-tich-danh-gia/gia-chung-cu-ha-noi-tang-cao-ti-le-hap-thu-van-tich-cuc-cd-hn-847929 | 搜尋結果內容 |
| VN-D02 | Hà Nội sẽ đón nguồn cung căn hộ lớn trong năm 2026 | Diễn đàn Doanh nghiệp | 2025–2026 | 越 | https://diendandoanhnghiep.vn/ha-noi-se-don-nguon-cung-can-ho-lon-trong-nam-2026-10165338.html | 搜尋結果內容 |
| VN-D03 | Chi phí thiết kế nội thất chung cư 2 phòng ngủ 2025 | TNT Home（業者） | 2025 | 越 | https://tnthome.com.vn/chi-phi-thiet-ke-noi-that-chung-cu-2-phong-ngu-2025/ | 搜尋結果內容 |
| VN-D04 | Chi Phí Làm Nội Thất Chung Cư? Cách Lên Dự Toán Chi Tiết 2025 | Apacons（業者） | 2025 | 越 | https://apacons.vn/chi-phi-lam-noi-that-chung-cu-chi-tiet-2025/ | 搜尋結果內容 |
| VN-D05 | Báo giá thiết kế & thi công nội thất chung cư 2025 (trọn gói) | FHome（業者） | 2025 | 越 | https://fhomesg.vn/gia-thiet-ke-thi-cong-noi-that-chung-cu/ | 搜尋結果內容 |
| VN-D06 | Báo Giá Thi Công Nội Thất Trọn Gói 2026 Theo M2, Md Tại Xưởng | Hometalk（業者） | 2026 | 越 | https://hometalk.com.vn/bao-gia-thi-cong-noi-that/ | 搜尋結果內容（候選） |
| VN-D07 | Đơn giá hoàn thiện nhà xây thô và căn hộ chung cư năm 2025 | Xây nhà Sài Gòn（業者） | 2025 | 越 | https://xaynhasaigon.vn/du-an-hoan-thanh/gia-hoan-thien-nha-xay-tho-chung-cu/ | 搜尋結果內容 |
| VN-D08 | Quy định mới về chứng chỉ hành nghề hoạt động xây dựng từ 01/7/2026 (Nghị định 212/2026/NĐ-CP) | Thư viện Pháp luật | 2026 | 越 | https://thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/ho-tro-phap-luat/chinh-sach-moi/115172/quy-dinh-moi-ve-chung-chi-hanh-nghe-hoat-dong-xay-dung-tu-01-7-2026-nghi-dinh-212-2026-nd-cp | 搜尋結果內容 |
| VN-D09 | Nghị định 212/2026/NĐ-CP: Điều kiện năng lực và hệ thống thông tin xây dựng | LuatVietnam | 2026 | 越 | https://luatvietnam.vn/xay-dung/nghi-dinh-212-2026-nd-cp-dieu-kien-nang-luc-va-he-thong-thong-tin-xay-dung-437901-d1.html | 搜尋結果內容 |
| VN-D10 | Nghị định xây dựng còn hiệu lực 2026: bảng tra thay thế | Đại học Xây dựng Hà Nội（IIC） | 2026 | 越 | https://iic.huce.edu.vn/bai-viet/nghi-dinh-xay-dung-con-hieu-luc.html | 搜尋結果內容 |
| VN-D11 | CHÍNH THỨC: Bãi bỏ chứng chỉ hành nghề Định giá xây dựng từ ngày 01/7/2026 theo Nghị định 212 2026 NĐ CP | Thư viện Pháp luật | 2026 | 越 | https://thuvienphapluat.vn/banan/tin-tuc/chinh-thuc-bai-bo-chung-chi-hanh-nghe-dinh-gia-xay-dung-tu-ngay-0172026-theo-nghi-dinh-212-2026-nd--50709.html | 搜尋結果內容 |
| VN-D12 | Hồ sơ cấp chứng chỉ hành nghề xây dựng nộp trước 01/7/2026 xử lý thế nào? | DH Tax & Law | 2026 | 越 | https://www.dhtaxlaw.com.vn/ho-so-cap-chung-chi-hanh-nghe-xay-dung-nop-truoc-01-7-2026xu-ly-the-nao | 搜尋結果內容 |
| VN-D13 | Trường hợp không cần chứng chỉ hành nghề xây dựng từ 01/7/2026 | DH Tax & Law | 2026 | 越 | https://dhtaxlaw.com.vn/truong-hop-khong-can-chung-chi-hanh-nghe-xay-dung-tu-01-7-2026 | 搜尋結果內容 |
| VN-D14 | Trả lời kiến nghị của cử tri tỉnh Vĩnh Long về việc cấp chứng chỉ hành nghề giám sát thi công xây dựng tương ứng với các hạng | Bộ Xây dựng | 2026 | 越 | https://moc.gov.vn/vn/tin-tuc/1179/96204/tra-loi-kien-nghi-cua-cu-tri-tinh-vinh-long-ve-viec-cap-chung-chi-hanh-nghe-giam-sat-thi-cong-xay-dung-tuong-ung-voi-cac-hang.aspx | 搜尋結果內容 |
| VN-D15 | Từ 1/7/2026 UBND tỉnh cấp chứng chỉ hành nghề hoạt động xây dựng đúng không? | Thư viện Pháp luật | 2026 | 越 | https://thuvienphapluat.vn/hoi-dap-phap-luat/tu-172026-ubnd-tinh-cap-chung-chi-hanh-nghe-hoat-dong-xay-dung-dung-khong-138095030.html | 僅標題 |
| VN-D16 | Những công trình nào được miễn giấy phép xây dựng theo luật mới? | Tuổi Trẻ | 2026 | 越 | https://tuoitre.vn/nhung-cong-trinh-nao-duoc-mien-giay-phep-xay-dung-theo-luat-moi-20260506165120069.htm | 搜尋結果內容 |
| VN-D17 | Mở rộng diện miễn giấy phép xây dựng từ ngày 1/7/2026 | Nhân Dân | 2026 | 越 | https://nhandan.vn/mo-rong-dien-mien-giay-phep-xay-dung-tu-ngay-172026-post962147.html | 搜尋結果內容 |
| VN-D18 | Có trường hợp sửa nhà được miễn giấy phép xây dựng, nhưng vẫn có trường hợp tự ý làm sẽ bị phạt đến 80 triệu đồng | Soha | 2026 | 越 | https://soha.vn/co-truong-hop-sua-nha-duoc-mien-giay-phep-xay-dung-nhung-van-co-truong-hop-tu-y-lam-se-bi-phat-den-80-trieu-dong-nguoi-dan-can-luu-y-198260916095404693.htm | 僅標題 |
| VN-D19 | Mục 1 Chương 3 Luật Kiến trúc 2019 | Hệ thống pháp luật | 2019（法條） | 越 | https://hethongphapluat.com/luat-kien-truc-2019/chuong-3/muc-1 | 搜尋結果內容 |
| VN-D20 | Luật Kiến trúc 2019（số 40/2019/QH14） | Thư viện Pháp luật | 2019（法條） | 越 | https://thuvienphapluat.vn/van-ban/Xay-dung-Do-thi/Luat-Kien-truc-2019-384114.aspx | 搜尋結果內容 |
| VN-D21 | Luật kiến trúc 2019 và thành lập công ty thiết kế nội thất | Luật Việt An | 年份不明 | 越 | https://luatvietan.vn/thanh-lap-cong-ty-thiet-ke-noi-that.html | 搜尋結果內容 |
| VN-D22 | Quyết định 5028/QĐ-QHKT ngày 14/10/2025（核發建築執業證書） | Sở Quy hoạch – Kiến trúc Hà Nội（置於 moc.gov.vn） | 2025 | 越 | https://moc.gov.vn/Images/editor/files/CCHN%20kien%20truc/2025/SQHKT%20Ha%20Noi_5028-QD-QHKT_14102025.pdf | 搜尋結果內容 |
| VN-D23 | Nghị định 105/2025/NĐ-CP | TC Toàn Cầu（顧問） | 2025 | 越 | https://tctoancau.com/nghi-dinh-105-2025-nd-cp-ban-hanh-ngay-15-05-2025/ | 搜尋結果內容 |
| VN-D24 | Tổng hợp 6 điểm mới Nghị định 105/2025/NĐ-CP về PCCC | PTC1 | 2025 | 越 | https://www.ptc1.com.vn/nd/tin-tuc-ptc1/tong-hop-6-diem-moi-nghi-dinh-105-2025-nd-cp-ve-pccc.html | 搜尋結果內容 |
| VN-D25 | Dịch Vụ Thẩm Định Thiết Kế, Nghiệm Thu PCCC Trọn Gói ANO | ANO Group | 2025–2026 | 越 | https://anogroup.vn/tham-dinh-thiet-ke-nghiem-thu-pccc-theo-nghi-dinh-105-2025-dich-vu-tron-goi-ano | 搜尋結果內容 |
| VN-D26 | Nghị định 105 thẩm duyệt PCCC: Những điểm mới cần biết | PCCC Phúc Bảo An | 2025 | 越 | https://pcccphucbaoan.com/nghi-dinh-105-tham-duyet-pccc/ | 搜尋結果內容 |
| VN-D27 | Sửa đổi đối tượng thuộc diện thẩm duyệt thiết kế về PCCC theo Nghị định 50 | Thư viện Pháp luật | 2024 | 越 | https://thuvienphapluat.vn/phap-luat/sua-doi-doi-tuong-thuoc-dien-tham-duyet-thiet-ke-ve-pccc-theo-nghi-dinh-50-ho-so-de-nghi-tham-duyet-41696-182116.html | 搜尋結果內容 |
| VN-D28 | Đã có Nghị định 50/2024/NĐ-CP hướng dẫn Luật Phòng cháy chữa cháy | LuatVietnam | 2024 | 越 | https://luatvietnam.vn/tin-van-ban-moi/da-co-nghi-dinh-50-2024-nd-cp-huong-dan-luat-phong-chay-chua-chay-186-97696-article.html | 搜尋結果內容 |
| VN-D29 | Ông chủ đứng sau chuỗi siêu thị nội thất Nhà Xinh: Khủng hoảng là cơ hội để bật lên… | CafeBiz | 2021 | 越 | https://cafebiz.vn/ong-chu-dung-sau-chuoi-sieu-thi-noi-that-nha-xinh-khung-hoang-la-co-hoi-de-bat-len-nen-co-bao-nhieu-tien-chung-toi-tat-tay-mang-ra-dau-tu-het-20210120173415814.chn | 搜尋結果內容 |
| VN-D30 | Chiến lược "Phù Đổng" của công ty đứng sau thương hiệu Nhà Xinh, làm nội thất cho Landmark 81… | CafeF | 2023 | 越 | https://cafef.vn/chien-luoc-phu-dong-cua-cong-ty-dung-sau-thuong-hieu-nha-xinh-lam-noi-that-cho-landmark-81-xay-nha-may-rong-50-ha-trong-3-nam-huong-den-chinh-phuc-thi-truong-the-gioi-188231025210934073.chn | 搜尋結果內容 |
| VN-D31 | AKA Furniture（官網） | CTCP Nội thất AKA | 現行頁 | 英 | https://www.akafurniture.com.vn/ | 搜尋結果內容 |
| VN-D32 | JYSK Việt Nam（官網） | JYSK Việt Nam | 現行頁 | 越 | https://jysk.vn/ | 搜尋結果內容 |
| VN-D33 | JYSK – thương hiệu đồ nội thất quy mô toàn cầu từ Đan Mạch khám phá thị trường Việt Nam | Gỗ Việt | 年份不明 | 越 | https://goviet.org.vn/bai-viet/jysk-thuong-hieu-do-noi-that-quy-mo-toan-cau-tu-dan-mach-kham-pha-thi-truong-viet-nam-8324/ | 搜尋結果內容（候選） |
| VN-D34 | Nội thất Nhật Bản Nitori ra mắt cửa hàng hơn 3.000 m2 tại Đồng Khởi | VnExpress | 約 2025（依編號推斷） | 越 | https://vnexpress.net/noi-that-nhat-ban-nitori-ra-mat-cua-hang-hon-3-000-m2-tai-dong-khoi-4871117.html | 搜尋結果內容 |
| VN-D35 | Hãng nội thất Nhật Bản nhắm tới thị trường Việt Nam, muốn đối đầu với IKEA | Fili | 2023 | 越 | https://fili.vn/2023/10/hang-noi-that-nhat-ban-nham-toi-thi-truong-viet-nam-muon-doi-dau-voi-ikea-768-1113561.htm | 搜尋結果內容 |
| VN-D36 | Đường vào Việt Nam của IKEA: Giáp mặt hàng loạt ông lớn nội thất trong và ngoài nước… | Soha | 2019 | 越 | https://soha.vn/duong-vao-viet-nam-cua-ikea-giap-mat-hang-loat-ong-lon-noi-that-trong-va-ngoai-nuoc-tu-pho-xinh-nha-dep-den-uma-jysk-2019012008093539.htm | 搜尋結果內容 |
| VN-D37 | Doanh nghiệp nội thất đang bỏ lỡ thị trường tỉ đô ở 'sân nhà'? | Tạp chí Kinh tế Sài Gòn | 年份不明 | 越 | https://thesaigontimes.vn/doanh-nghiep-noi-that-dang-bo-lo-thi-truong-ti-do-o-san-nha/ | 僅標題 |
| VN-D38 | IKEA sẽ đầu tư 450 triệu USD vào Hà Nội | VietnamFinance | 2019 | 越 | https://vietnamfinance.vn/ikea-se-dau-tu-450-trieu-usd-vao-ha-noi-d30586.html | 搜尋結果內容 |
| VN-D39 | Năm đầu tiên xuất khẩu gỗ và sản phẩm gỗ vượt mốc 17 tỷ USD | Thương hiệu & Công luận | 2026 | 越 | https://thuonghieucongluan.com.vn/nam-dau-tien-xuat-khau-go-va-san-pham-go-vuot-moc-17-ty-usd-a300063.html | 搜尋結果內容 |
| VN-D40 | Xuất khẩu gỗ và sản phẩm gỗ năm 2025: "Tự tin" với mục tiêu 18 tỷ USD | Trung tâm WTO（VCCI） | 2025 | 越 | https://trungtamwto.vn/chuyen-de/29133-xuat-khau-go-va-san-pham-go-nam-2025-tu-tin-voi-muc-tieu-18-ty-usd | 搜尋結果內容 |
| VN-D41 | Xuất khẩu gỗ trước áp lực thuế quan từ Mỹ | Báo Đầu tư | 2025 | 越 | https://baodautu.vn/xuat-khau-go-truoc-ap-luc-thue-quan-tu-my-d252518.html | 搜尋結果內容（候選） |
| VN-D42 | Gỗ An Cường (ACG) dự kiến chi 151 tỷ đồng trả cổ tức | Báo Pháp luật VN – Doanh nhân | 2026 | 越 | https://doanhnhan.baophapluat.vn/go-an-cuong-acg-du-kien-chi-151-ty-dong-tra-co-tuc.html | 搜尋結果內容（候選） |
| VN-D43 | Sát giờ về đích 2026, loạt doanh nghiệp rốt ráo điều chỉnh kế hoạch kinh doanh | Viettimes | 2026 | 越 | https://viettimes.vn/sat-gio-ve-dich-2026-loat-doanh-nghiep-rot-rao-dieu-chinh-ke-hoach-kinh-doanh-post206704.html | 搜尋結果內容 |
| VN-D44 | Cổ phiếu nổi bật phiên giao dịch ngày 22/9 | Thương hiệu & Công luận | 年份不明 | 越 | https://thuonghieucongluan.com.vn/co-phieu-noi-bat-phien-giao-dich-ngay-22-9-a281427.html | 搜尋結果內容（候選） |
| VN-D45 | Hòa Phát (HPG) lãi sau thuế năm 2025 vượt 15.500 tỷ đồng, sản lượng thép cán nóng lập kỷ lục | Báo Pháp luật VN – Doanh nhân | 2026 | 越 | https://doanhnhan.baophapluat.vn/hoa-phat-hpg-lai-sau-thue-nam-2025-vuot-15-500-ty-dong-san-luong-thep-can-nong-lap-ky-luc.html | 搜尋結果內容 |
| VN-D46 | 越南房屋裝修，實際模擬案例。2025更新 | vietnamtophouse（台灣不動產業者經營） | 2025 | 繁中 | https://vietnamtophouse.com/decoration/ | 搜尋結果內容 |
| VN-D47 | 越南商辦空間設計：整合建築與室內設計，重塑企業識別的辦公場域 | Gentour Studio | 年份不明 | 繁中 | https://gentourstudio.com/blogs/commercial-space-design/vietnam-vungtau | 搜尋結果內容 |
| VN-D48 | Năm 2025 vốn FDI thực hiện tại Việt Nam tăng 9%, cao nhất trong 5 năm qua | Tạp chí Kinh tế Tài chính | 2026 | 越 | https://tapchikinhtetaichinh.vn/nam-2025-von-fdi-thuc-hien-tai-viet-nam-tang-9-cao-nhat-trong-5-nam-qua-137749.html | 搜尋結果內容 |
| VN-D49 | FDI Đài Loan vào Việt Nam: Sự dịch chuyển của chuỗi giá trị | Nhà Đầu tư | 2026 | 越 | https://nhadautu.vn/fdi-dai-loan-vao-viet-nam-su-dich-chuyen-cua-chuoi-gia-tri-d105198.html | 搜尋結果內容（候選） |
| VN-D50 | Từ 22/12/2025, đơn giá nhân công xây dựng tại Hà Nội cao nhất 416.000 đồng/ngày | LuatVietnam | 2025 | 越 | https://luatvietnam.vn/tin-van-ban-moi/don-gia-nhan-cong-xay-dung-tren-dia-ban-tp-ha-noi-tu-22-12-2025-186-106465-article.html | 搜尋結果內容 |
| VN-D51 | QĐ Công bố đơn giá NCXD năm 2025（Thái Nguyên） | Sở Xây dựng Thái Nguyên | 2025 | 越 | https://storage-vnportal.vnpt.vn/gov-tnn/10286/FileVanBanChiDao/QĐ Công bố đơn giá NCXD năm 2025.signed.signed.signed.signed.signed.pdf | 搜尋結果內容 |
| VN-D52 | Thợ mộc, thợ phụ gỗ công nghiệp（Quận 12，徵才） | Muaban.net | 2025–2026 | 越 | https://muaban.net/viec-lam/tho-moc-quan-12-ho-chi-minh/tho-moc-tho-phu-go-cong-nghiep-id71128614 | 搜尋結果內容（候選） |
| VN-D53 | Tuyển nhiều thợ hồ, phụ hồ làm công trình nhà phố（Cần Giờ，徵才） | Muaban.net | 2025–2026 | 越 | https://muaban.net/viec-lam/tho-xay-dung-huyen-can-gio-ho-chi-minh/tuyen-nhieu-tho-ho-phu-ho-lam-cong-trinh-nha-pho-id70958202 | 搜尋結果內容 |
| VN-D54 | Công văn 1966/BXD-KTQLXD 2026 công bố giá vật liệu xây dựng, nhân công, máy thi công và chỉ số giá xây dựng | LuatVietnam | 2026 | 越 | https://luatvietnam.vn/xay-dung/cong-van-1966-bxd-ktqlxd-2026-cong-bo-gia-vat-lieu-xay-dung-nhan-cong-may-thi-cong-va-chi-so-gia-xay-dung-426978-d6.html | 搜尋結果內容 |
| VN-D55 | Từ biến động giá vật liệu xây dựng đến áp lực ổn định thị trường bất động sản | Tạp chí Kinh tế Tài chính | 2026 | 越 | https://tapchikinhtetaichinh.vn/tu-bien-dong-gia-vat-lieu-xay-dung-den-ap-luc-on-dinh-thi-truong-bat-dong-san-143113.html | 搜尋結果內容（候選） |
| VN-D56 | Giá vật liệu xây dựng đầu năm 2026 tiếp tục tăng nhẹ | Thời báo Tài chính Việt Nam | 2026 | 越 | https://thoibaotaichinhvietnam.vn/gia-vat-lieu-xay-dung-dau-nam-2026-tiep-tuc-tang-nhe-189707-189707.html | 搜尋結果內容 |
| VN-D57 | Bảng giá vật liệu xây dựng mới nhất 2026 (cập nhật thị trường) | Sany Global（業者） | 2026 | 越 | https://sanyglobal.vn/truyen-thong/bang-gia-vat-lieu-xay-dung-moi-nhat-2026-cap-nhat-thi-truong | 搜尋結果內容（候選） |
| VN-D58 | Báo cáo công tác tư vấn, hỗ trợ và tiếp nhận, giải quyết yêu cầu… của người tiêu dùng | Ủy ban Cạnh tranh Quốc gia | 2025 | 越 | https://vcc.gov.vn/default.aspx?page=news&do=detail&id=224bdde5-5e16-4748-be57-c49456a658fb | 搜尋結果內容 |
| VN-D59 | 7 lời khuyên dành cho bạn để tránh bị lừa khi sửa nhà | OneHousing | 年份不明 | 越 | https://onehousing.vn/blog/7-loi-khuyen-danh-cho-ban-de-tranh-bi-lua-khi-sua-nha-n17t | 搜尋結果內容（候選） |
| VN-D60 | Touchstone Partners leads $720,000 seed investment round in Vietnam's Happynest | TechNode Global | 2024 | 英 | https://technode.global/2024/05/02/touchstone-partners-leads-720000-seed-investment-round-in-vietnams-happynest/ | 搜尋結果內容 |
| VN-D61 | CEO Cao Minh Tuyết và hành trình khai mở thị trường nhà ở cùng lối sống dành cho người Việt | Báo Đầu tư（eMagazine） | 年份不明 | 越 | https://baodautu.vn/emagazine-ceo-cao-minh-tuyet-va-hanh-trinh-khai-mo-thi-truong-nha-o-cung-loi-song-danh-cho-nguoi-viet-m169039.html | 搜尋結果內容 |
| VN-D62 | Gần 1.500 gian hàng của 400 doanh nghiệp trong và ngoài nước tham gia VIETBUILD Hà Nội 2025 lần thứ nhất | Thị trường Tài chính Tiền tệ | 2025 | 越 | https://thitruongtaichinhtiente.vn/gan-1-500-gian-hang-cua-400-doanh-nghiep-trong-va-ngoai-nuoc-tham-gia-vietbuild-ha-noi-2025-lan-thu-nhat-66371.html | 搜尋結果內容 |
| VN-D63 | Gần 900 gian hàng tham gia Triển lãm quốc tế Vietbuild Đà Nẵng 2025 | Tạp chí Công Thương | 2025 | 越 | https://tapchicongthuong.vn/gan-900-gian-hang-tham-gia-trien-lam-quoc-te-vietbuild-da-nang-2025-140436.htm | 搜尋結果內容 |
| VN-D64 | Hơn 1.000 gian hàng tham gia Triển lãm quốc tế Vietbuild Hà Nội 2025 | Thị trường Tài chính Tiền tệ | 2025 | 越 | https://thitruongtaichinhtiente.vn/hon-1-000-gian-hang-tham-gia-trien-lam-quoc-te-vietbuild-ha-noi-2025-70664.html | 搜尋結果內容 |
| VN-D65 | Hơn 630 gian hàng giới thiệu sản phẩm mới ngành xây dựng tại triển lãm quốc tế Vietbuild | Tuổi Trẻ | 2025 | 越 | https://tuoitre.vn/hon-630-gian-hang-gioi-thieu-san-pham-moi-nganh-xay-dung-tai-trien-lam-quoc-te-vietbuild-20250529161008895.htm | 搜尋結果內容 |
| VN-D66 | GDP Việt Nam 2025 tăng 8,02%, bình quân mỗi người 125 triệu đồng | VietnamFinance（引 Cục Thống kê） | 2026 | 越 | https://vietnamfinance.vn/gdp-viet-nam-2025-tang-802-binh-quan-moi-nguoi-125-trieu-dong-d138312.html | 搜尋結果內容 |
| VN-D67 | GDP Việt Nam tăng 8,02% năm 2025, bình quân đầu người đạt 5.026 USD | Nhà Đầu tư | 2026 | 越 | https://nhadautu.vn/gdp-viet-nam-tang-802-nam-2025-binh-quan-dau-nguoi-dat-5026-usd-d102080.html | 搜尋結果內容 |
| VN-D68 | Tuyển dụng việc làm Nhân Viên Thiết Kế Nội Thất | JobsGO | 2026 | 越 | https://jobsgo.vn/viec-lam-nhan-vien-thiet-ke-noi-that.html | 搜尋結果內容 |
| VN-D69 | Việc làm Nhân Viên Thiết Kế Nội Thất / Interior Designer (Intern, Junior Level) | JobsGO（徵才） | 2025–2026 | 越 | https://jobsgo.vn/viec-lam/nhan-vien-thiet-ke-noi-that-interior-designer-intern-junior-level-28335502985.html | 搜尋結果內容 |
| VN-D70 | Lương kiến trúc sư bao nhiêu? Có cao không? | Joboko | 年份不明 | 越 | https://vn.joboko.com/blog/luong-cua-kien-truc-su-co-cao-khong-nwi3650 | 搜尋結果內容 |
| VN-D71 | （室內裝修合約範本，Google Docs 匯出 PDF） | 不明（業者範本） | 年份不明 | 越 | https://docs.google.com/document/d/1bjE4AlN6Y5ZWOnkjs4S3LU9TCp-GIBD7/export?format=pdf | 搜尋結果內容（候選：同批 5 份範本中的哪一份未能確認） |
| VN-D72 | Mức tạm ứng tối thiểu hợp đồng thi công xây dựng công trình 2026 bao nhiêu? | Thư viện Pháp luật | 2026 | 越 | https://thuvienphapluat.vn/hoi-dap-phap-luat/muc-tam-ung-toi-thieu-hop-dong-thi-cong-xay-dung-cong-trinh-2026-bao-nhieu-138090308.html | 搜尋結果內容 |
| VN-D73 | 17/VBHN-BXD ngày 24/03/2026（Thông tư 05/2024/TT-BXD 合併文本） | Bộ Xây dựng | 2026 | 越 | https://moc.gov.vn/Images/FileVanBan/BXD_17-VBHN-BXD_24032026(1).pdf | 搜尋結果內容 |
| VN-D74 | Quyết định 26/2025/QĐ-UBND quản lý sử dụng nhà chung cư Hồ Chí Minh | Thư viện Pháp luật（轉載 UBND TP.HCM） | 2025 | 越 | https://thuvienphapluat.vn/van-ban/Xay-dung-Do-thi/Quyet-dinh-26-2025-QD-UBND-quan-ly-su-dung-nha-chung-cu-Ho-Chi-Minh-645071.aspx | 搜尋結果內容 |
| VN-D75 | Ho Chi Minh City and Hanoi rank among top 3 least expensive Asia Pacific markets | Cushman & Wakefield Vietnam | 2025 | 英 | https://www.cushmanwakefield.com/vi-vn/vietnam/news/2025/03/ho-chi-minh-city-and-hanoi-rank-among-top-3-least-expensive-asia-pacific-markets | 搜尋結果內容 |
| VN-D76 | Việt Nam chiếm lợi thế cạnh tranh về chi phí hoàn thiện nội thất văn phòng khu vực châu Á – Thái Bình Dương | Thị trường Tài chính Tiền tệ（引 C&W） | 2026 | 越 | https://thitruongtaichinhtiente.vn/viet-nam-chiem-loi-the-canh-tranh-ve-chi-phi-hoan-thien-noi-that-van-phong-khu-vuc-chau-a-thai-binh-duong-80624.html | 搜尋結果內容 |
| VN-D77 | Office fit-out cost in HCMC and Hanoi reaches about USD61/sqft | Cushman & Wakefield Vietnam | 2022 | 英 | https://www.cushmanwakefield.com/vi-vn/vietnam/news/2022/02/office-fit-out-cost-in-hcmc-and-hanoi-reaches-about-usd61-sqft | 搜尋結果內容 |
| VN-D78 | Giá thuê văn phòng hạng A tại TP.HCM và Hà Nội duy trì mức cao, lọt top đắt đỏ khu vực | Báo Pháp luật VN – Doanh nhân | 2026 | 越 | https://doanhnhan.baophapluat.vn/gia-thue-van-phong-hang-a-tai-tp-hcm-va-ha-noi-duy-tri-muc-cao-lot-top-dat-do-khu-vuc.html | 搜尋結果內容（候選） |
| VN-D79 | Những chung cư cũ nào tại Hà Nội được cải tạo, xây dựng lại? | VnBusiness | 年份不明（引 2020 資料） | 越 | https://vnbusiness.vn/nhung-chung-cu-cu-nao-tai-ha-noi-duoc-cai-tao-xay-dung-lai.html | 搜尋結果內容 |
| VN-D80 | 100 nghìn hộ dân đang sống tại các chung cư cũ | Báo Pháp luật | 年份不明 | 越 | https://baophapluat.vn/100-nghin-ho-dan-dang-song-tai-cac-chung-cu-cu-post415015.html | 搜尋結果內容 |
| VN-D81 | Cải tạo chung cư cũ: Dân không chịu đi vì nghi doanh nghiệp trục lợi | Báo Đầu tư | 年份不明 | 越 | https://baodautu.vn/batdongsan/cai-tao-chung-cu-cu-dan-khong-chiu-di-vi-nghi-doanh-nghiep-truc-loi-d72729.html | 搜尋結果內容 |
| VN-D82 | Chung cư cũ（主題頁） | Nông nghiệp và Môi trường | 2025–2026 | 越 | https://nongnghiepmoitruong.vn/chung-cu-cu-tag134588/ | 搜尋結果內容 |
| VN-D83 | Ho Chi Minh City to see up to 6,000 new prime apartments this year | Real Estate Asia（引 JLL） | 2025 | 英 | https://realestateasia.com/residential/news/ho-chi-minh-city-see-6000-new-prime-apartments-year | 搜尋結果內容 |
| VN-D84 | Accommodation in Vietnam | Expat Arrivals | 年份不明 | 英 | https://www.expatarrivals.com/vietnam/accommodation-in-vietnam | 搜尋結果內容（候選） |
| VN-D85 | Thêm cơ hội để Việt Nam đón sóng đầu tư điện tử, bán dẫn từ doanh nghiệp Đài Loan | Nhà Đầu tư | 2025–2026 | 越 | https://nhadautu.vn/them-co-hoi-de-viet-nam-don-song-dau-tu-dien-tu-ban-dan-tu-doanh-nghiep-dai-loan-d102536.html | 搜尋結果內容（候選） |
| VN-D86 | 4 cách người tiêu dùng khiếu nại về quyền lợi của mình | Tuổi Trẻ | 年份不明（較舊） | 越 | https://tuoitre.vn/4-cach-nguoi-tieu-dung-khieu-nai-ve-quyen-loi-cua-minh-1148440.htm | 搜尋結果內容 |
| VN-D87 | Hà Nội: Những chung cư mới mở bán trong năm 2025, giá cao nhất lên tới 270 triệu đồng/m2 | Báo Đầu tư | 2025 | 越 | https://baodautu.vn/ha-noi-nhung-chung-cu-moi-mo-ban-trong-nam-2025-gia-cao-nhat-len-toi-270-trieu-dongm2-d237415.html | 僅標題 |
| VN-D88 | Những dự án chung cư sẽ mở bán trong năm 2025 tại Hà Nội, không còn căn hộ dưới 65 triệu đồng/m2 | CafeLand | 2025 | 越 | https://cafeland.vn/tin-tuc/nhung-du-an-chung-cu-se-mo-ban-trong-nam-2025-tai-ha-noi-khong-con-can-ho-duoi-65-trieu-dongm2-133387.html | 僅標題 |

### 6c. 總體與台灣錨點（沿用 TF、TW 筆記）

| # | 標題 | 機構 | 年份 | 語言 | URL | 讀取方式 |
|---|---|---|---|---|---|---|
| TF-01 | Foreign Exchange Rates – G.5A (Annual) | 美國聯邦準備理事會 | 2026 | 英 | https://www.federalreserve.gov/releases/g5a/current/ | 搜尋結果內容（經 TF 筆記） |
| TF-14 | Vietnam Exchange Rate against USD | CEIC Data（引世界銀行） | 2026 | 英 | https://www.ceicdata.com/en/indicator/vietnam/exchange-rate-against-usd | 搜尋結果內容（經 TF 筆記） |
| TF-18 | GDP per Capita in Asia (2025) - IMF | Worldometer（轉載 IMF WEO 2026-04） | 2026 | 英 | https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal | 搜尋結果內容（經 TF 筆記） |
| TF-20 | GDP by Country in Asia (2025) - IMF | Worldometer | 2026 | 英 | https://www.worldometers.info/gdp/gdp-by-country/?region=asia&year=2025&metric=nominal | 搜尋結果內容（經 TF 筆記） |
| TF-21 | GDP by Country in Asia (2026) - IMF | Worldometer | 2026 | 英 | https://www.worldometers.info/gdp/gdp-by-country/?region=asia&year=2026&metric=nominal | 搜尋結果內容（經 TF 筆記；歸屬 TF-19／21 不確定） |
| TW-13 | 全台住宅平均屋齡創新高… | 經濟日報 | 2025 | 繁中 | https://money.udn.com/money/story/5621/9014283 | 搜尋結果內容（經 TW 筆記） |
| TW-16 | （工商時報：裝潢行情報導） | 工商時報 | 2025 | 繁中 | https://www.ctee.com.tw/news/20251119700015-431001 | 搜尋結果內容（經 TW 筆記） |
| TW-19 | 老屋翻新 價格 | PRO360 達人網 | 現行頁 | 繁中 | https://www.pro360.com.tw/price/old_house_renovation | 搜尋結果內容（經 TW 筆記） |
| TW-21 | 20坪 房屋裝潢 價格 | PRO360 達人網 | 現行頁 | 繁中 | https://www.pro360.com.tw/price/20_ping_house_decoration | 搜尋結果內容（經 TW 筆記） |
| TW-22 | 裝潢預算怎麼估？裝修費用怎麼算？ | vocus 方格子 | 2025 | 繁中 | https://vocus.cc/article/68429352fd897800016a223d | 搜尋結果內容（經 TW 筆記） |
| TW-23 | 裝修市場熱！年產值上看5500億元 業者曝2026年裝修趨勢 | 聯合新聞網 | 2025／2026 | 繁中 | https://udn.com/news/story/7241/9245511 | 搜尋結果內容（經 TW 筆記） |
| TW-26 | 住宅裝修市場規模推估方法之研究 | 內政部建築研究所 | 2000 年代 | 繁中 | https://www.abri.gov.tw/News_Content_Table.aspx?n=807&s=38057 | 搜尋結果內容（經 TW 筆記） |
| TW-30 | 建築管理（100 年統計） | 內政部營建署 | 2011 | 繁中 | https://w3.cpami.gov.tw/statisty/100/100_pdf/06_building/0c_building.pdf | 搜尋結果內容（經 TW 筆記） |
| TW-41 | 114年第20週內政統計通報 | 內政部統計處 | 2025 | 繁中 | https://www.moi.gov.tw/News_Content.aspx?n=2905&s=328048 | 搜尋結果內容（經 TW 筆記） |

---

## 7. 附錄：關鍵指標 CSV

```
market,metric,value,unit,year,source_id,source_url,definition,confidence
VN,住宅fit-out單價－基本,3.5-4.5,百萬VND/m²,2025,VN-D03,https://tnthome.com.vn/chi-phi-thiet-ke-noi-that-chung-cu-2-phong-ngu-2025/,業者報價；=135-173 USD/m²；=13867-17829 TWD/坪；示意,low
VN,住宅fit-out單價－中階,5-6.5,百萬VND/m²,2025,VN-D03,https://tnthome.com.vn/chi-phi-thiet-ke-noi-that-chung-cu-2-phong-ngu-2025/,業者報價；=192-250 USD/m²；=19809-25752 TWD/坪；示意,low
VN,住宅fit-out單價－高階,7-10,百萬VND/m²,2025,VN-D03,https://tnthome.com.vn/chi-phi-thiet-ke-noi-that-chung-cu-2-phong-ngu-2025/,天然木；=269-385 USD/m²；示意,low
VN,毛胚屋完成面單價,2.6-5,百萬VND/m²,2025,VN-D07,https://xaynhasaigon.vn/du-an-hoan-thanh/gia-hoan-thien-nha-xay-tho-chung-cu/,毛胚交屋後的完成面工程；不含家具；示意,low
VN,設計費,250000-350000,VND/m²,2025,VN-D05,https://fhomesg.vn/gia-thiet-ke-thi-cong-noi-that-chung-cu/,業者報價；=9.6-13.5 USD/m²；簽施工常免收；示意,low
VN,設計費占工程費比（推算）,3.1-10.8,%,2025,VN-D05,https://fhomesg.vn/gia-thiet-ke-thi-cong-noi-that-chung-cu/,設計費÷3.25-8.0百萬VND/m²工程費；示意,low
VN,中階單價÷人均GDP,3.98-5.18,%,2025,VN-D03;VN-D66,https://vietnamfinance.vn/gdp-viet-nam-2025-tang-802-binh-quan-moi-nguoi-125-trieu-dong-d138312.html,5-6.5百萬VND/m²÷125.5百萬VND；示意,low
VN,人均GDP,125.5,百萬VND,2025,VN-D66,https://vietnamfinance.vn/gdp-viet-nam-2025-tang-802-binh-quan-moi-nguoi-125-trieu-dong-d138312.html,Cục Thống kê估計；按TF匯率=4826 USD；統計局自報5026 USD,medium
VN,GDP（現價）,12847.6,兆VND,2025,VN-D66,https://vietnamfinance.vn/gdp-viet-nam-2025-tang-802-binh-quan-moi-nguoi-125-trieu-dong-d138312.html,Cục Thống kê估計；按TF匯率=494.0十億USD；實質成長8.02%,medium
VN,交易觸發型fit-out代理,33.8-96.6,兆VND,2025,VN-38;VN-D03,https://baochinhphu.vn/nguon-cung-tang-gia-nha-chua-giam-102260117005432583.htm,138025筆×70m²×3.5-10百萬VND；=13.0-37.2億USD；占GDP 0.26-0.75%；示意非市場規模,low
VN,河內公寓售出,34760,戶,2025,VN-25,https://www.cbrevietnam.com/insights/figures/hanoi-figures-q4-2025,CBRE一級市場；約2-3年後交屋,high
VN,開案至交屋時間,2-3,年,2025-2026,VN-D01,https://wiki.batdongsan.com.vn/phan-tich-danh-gia/gia-chung-cu-ha-noi-tang-cao-ti-le-hap-thu-van-tich-cuc-cd-hn-847929,河內新開案一般交屋時程；示意,low
VN,河內已交屋二手公寓價,60-70,百萬VND/m²,2025-2026,VN-D02,https://diendandoanhnghiep.vn/ha-noi-se-don-nguon-cung-can-ho-lon-trong-nam-2026-10165338.html,二級市場；=2307-2692 USD/m²,medium
VN,交屋標準占比（毛胚/基本/全裝修）,無資料,—,—,—,—,兩輪四次搜尋皆無,—
VN,An Cường ACG營收,4600（超過）,十億VND,2025,VN-D42,https://doanhnhan.baophapluat.vn/go-an-cuong-acg-du-kien-chi-151-ty-dong-tra-co-tuc.html,年增16%；=1.769億USD；淨利504十億VND（+20%）；URL歸屬候選,medium
VN,An Cường ACG營收,2349.4,十億VND,2026H1,VN-D42,https://doanhnhan.baophapluat.vn/go-an-cuong-acg-du-kien-chi-151-ty-dong-tra-co-tuc.html,年增33.3%；稅後淨利241.66（+8.4%）；URL歸屬候選,medium
VN,木材及木製品出口,17.2,十億USD,2025,VN-D39,https://thuonghieucongluan.com.vn/nam-dau-tien-xuat-khau-go-va-san-pham-go-vuot-moc-17-ty-usd-a300063.html,海關；年增約6%；對美9.46十億USD占55%,medium
VN,台資新增登記FDI,965.8,百萬USD,2025,VN-D48,https://tapchikinhtetaichinh.vn/nam-2025-von-fdi-thuc-hien-tai-viet-nam-tang-9-cao-nhat-trong-5-nam-qua-137749.html,新增登記（非實際到位）；排名第6、占5.6%,medium
VN,台資累計FDI,42.37,十億USD,2026-04,VN-D49,https://nhadautu.vn/fdi-dai-loan-vao-viet-nam-su-dich-chuyen-cua-chuoi-gia-tri-d105198.html,累計3457案；排名第4；URL歸屬候選,medium
VN,商辦fit-out成本（河內）,678,USD/m²,2026,VN-D76,https://thitruongtaichinhtiente.vn/viet-nam-chiem-loi-the-canh-tranh-ve-chi-phi-hoan-thien-noi-that-van-phong-khu-vuc-chau-a-thai-binh-duong-80624.html,C&W亞太fit-out指南經媒體轉引；=69854 TWD/坪,medium
VN,商辦fit-out成本（胡志明市）,657,USD/m²,2026,VN-D76,https://thitruongtaichinhtiente.vn/viet-nam-chiem-loi-the-canh-tranh-ve-chi-phi-hoan-thien-noi-that-van-phong-khu-vuc-chau-a-thai-binh-duong-80624.html,同上；=67690 TWD/坪,medium
VN,商辦fit-out成本（河內）,17.2,百萬VND/m²,2025,VN-D75,https://www.cushmanwakefield.com/vi-vn/vietnam/news/2025/03/ho-chi-minh-city-and-hanoi-rank-among-top-3-least-expensive-asia-pacific-markets,C&W 2025版；新辦公室平均；胡志明市16.7,medium
VN,室內設計人員平均月薪,10,百萬VND/月,2026,VN-D68,https://jobsgo.vn/viec-lam-nhan-vien-thiet-ke-noi-that.html,人力銀行估計；常見8-14百萬；=385 USD,low
VN,河內官方建設工資單價上限,416000,VND/日,2025-12-22起,VN-D50,https://luatvietnam.vn/tin-van-ban-moi/don-gia-nhan-cong-xay-dung-tren-dia-ban-tp-ha-noi-tu-22-12-2025-186-106465-article.html,QĐ 3461/QĐ-SXD；估價用非市場實付；=16.0 USD,medium
VN,建設用原物料價格指數,3.1,%年增,2025,VN-D55,https://tapchikinhtetaichinh.vn/tu-bien-dong-gia-vat-lieu-xay-dung-den-ap-luc-on-dinh-thi-truong-bat-dong-san-143113.html,Cục Thống kê；砂石類+18.2%；URL歸屬候選,medium
VN,消費者申訴受理量,642,件,2025年1-9月,VN-D58,https://vcc.gov.vn/default.aspx?page=news&do=detail&id=224bdde5-5e16-4748-be57-c49456a658fb,Ủy ban Cạnh tranh Quốc gia全國總數；未拆裝修類,medium
VN,Happynest社群規模,480000,人,2024,VN-D60,https://technode.global/2024/05/02/touchstone-partners-leads-720000-seed-investment-round-in-vietnams-happynest/,Facebook社團成員；種子輪72萬USD；非交易滲透率,low
VN,擅自施工罰款上限,80,百萬VND,2026,VN-D18,https://soha.vn/co-truong-hop-sua-nha-duoc-mien-giay-phep-xay-dung-nhung-van-co-truong-hop-tu-y-lam-se-bi-phat-den-80-trieu-dong-nguoi-dan-can-luu-y-198260916095404693.htm,僅標題；需專業人士最終確認,low
VN,Nghị định 212/2026施行日,2026-07-01,日期,2026,VN-D08,https://thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/ho-tro-phap-luat/chinh-sach-moi/115172/quy-dinh-moi-ve-chung-chi-hanh-nghe-hoat-dong-xay-dung-tu-01-7-2026-nghi-dinh-212-2026-nd-cp,取代175/2024能力與證照規定；新證照效期10年；需專業人士最終確認,medium
VN,河內舊公寓棟數,1579,棟,2020,VN-D79,https://vnbusiness.vn/nhung-chung-cu-cu-nao-tai-ha-noi-duoc-cai-tao-xay-dung-lai.html,1960-1994年興建；走拆除重建路徑,medium
TW,中階單價÷人均GDP（新成屋）,1.47-2.46,%,2025,TW-16;TF-18,https://www.ctee.com.tw/news/20251119700015-431001,每坪6-10萬TWD÷3.3058÷31.1663÷39489 USD；示意,low
TW,設計費占工程費比,13-15,%,約2025,TW-21,https://www.pro360.com.tw/price/20_ping_house_decoration,20坪新成屋同端點配對；示意,low
```
