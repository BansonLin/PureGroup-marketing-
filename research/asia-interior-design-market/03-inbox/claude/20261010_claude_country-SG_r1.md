---
ai: claude
mode: research（Claude Code 雲端會話；以 r1 筆記為基底＋補搜）
date: 2026-10-10
scope: country:SG
prompt_version: v1
notes: 單一市場深潛（country-module-template v1）。來源僅經搜尋結果內容讀取，未直接開頁；與 V1 獨立。補搜 30 次（其中在地語言 7 次）。
---

# 新加坡：交易驅動、信任稀缺、單價不貴的小市場——室內裝修設計單一市場深潛（r1）

> 讀法：每個數字都附年份、來源編號、定義與信心，並標【實際】（來源直接給出的數字）或【示意】（市調、平台估算、本研究推算）。金額依序列原幣 SGD（S$）、美元、新台幣，匯率一律用聯準會 G.5A 2025 年平均：1 USD＝1.3065 SGD＝31.1663 TWD，也就是 1 SGD＝23.8548 TWD（TF-01）。面積換算：1 坪＝3.3058 m²，1 m²＝10.7639 sq ft。法規結論一律「需專業人士最終確認」。

---

## 0. 中繼資料

| 項目 | 內容 |
|---|---|
| AI | Claude |
| 模式 | Claude Code 雲端會話 Research（以 r1 筆記為基底＋補搜） |
| 日期 | 2026-10-10 |
| 範圍 | 單一市場：新加坡（Singapore, SG）；比較基準：台灣 |
| 委託人 | 璞石集團（CEO Banson；室內裝修設計＋不動產＋家居零售；基地宜蘭、台北信義） |
| 基底證據 | r1 筆記 `SG_singapore.md`（SG-01～SG-99）、`TF_macro_housing_fx.md`（匯率、人均 GDP）、`TW_taiwan.md`（台灣錨點）；另引用 r1 主題筆記中與新加坡相關的編號（TC、TD、TE、TA2）。未讀取 04-research-notes／05-report（V1），本報告與 V1 獨立 |
| 補搜次數 | 30 次（WebSearch；硬上限 30 次，已用完）：英文 23 次、簡體中文 7 次（新加坡華文媒體用語，如「消协」「组屋」「预购组屋」「乐龄易」「最低居住年限」） |
| 搜尋語言 | 英文、簡體中文。新加坡的在地語言含英文，本報告的「在地語言」專指簡體中文 |
| 來源數 | 列入第 6 章 182 個：沿用 r1 編號 92 個（SG 系列 67、TW 10、TF 3、TC 1、TD 2、TE 8、TA2 1），本輪新增 SG-D01～SG-D90 共 90 個。其中在地語言（簡中）8 個（SG-D13、SG-D14、SG-D37、SG-D40、SG-66、SG-67、SG-68、SG-70）；新加坡政府網域（gov.sg）來源 41 個，另有 CASE、BCA 學院、DesignSingapore、SGX 等在地機構來源 11 個 |
| 限制 | (1) 所有來源都只透過搜尋結果內容讀取，未直接開啟網頁（本環境無法使用 WebFetch／curl）。搜尋工具會把多個網頁彙整成一段文字，因此部分數字無法精確對應單一 URL，這類數字一律標「對應推定」並降低信心。(2)《聯合早報》網域在 r1 已確認無法存取，本輪中文搜尋也沒有回傳早報頁面。(3) 本報告與 V1（04-research-notes／05-report）獨立，未讀取 V1。(4) 2025 全年 CASE 投訴、HDB DRC 家數、CaseTrust 認證家數、ACRA 室內設計公司家數，本輪仍查不到 |

---

## 1. 摘要

1. **新加坡沒有官方的住宅翻修市場規模；本研究以交易量×每戶單價推估，每年約 S$28.1 億～49.3 億（＝21.5 億～37.7 億 USD＝670 億～1,176 億 TWD），約占 2025 年 GDP 的 0.36%～0.62%**。這是上限式推估，假設每戶新入住者都翻修（2025 年量×2026 年價；本研究依 SG-20、SG-71、SG-13 推算，GDP 取自 SG-D82）【示意】，信心低。
2. **需求幾乎完全由「交屋與轉手」觸發，2026–2028 年將迎來組屋屆滿最低居住年限（MOP）的高峰**。2025 年 HDB 轉售 26,169 筆（−9.7%，SG-20）；2026 年達 MOP 的組屋 13,480 戶，比 2025 年多 93%（SG-D41），2026–2028 年合計 53,816 戶（SG-D42，對應推定）。
3. **以所得衡量，新加坡的裝修單價遠比台灣便宜**。4 房式轉售組屋翻修每 m² 約 S$778～907（＝595～694 USD），只占人均 GDP 的 0.60%～0.70%；台灣中古屋同一比值是 2.46%～3.69%（2026 年價，SG-13、TW-C2，【示意】）。
4. **糾紛集中在未經認證的業者**。2024 年 CASE 收到裝修承包商投訴 962 件，約 97% 針對非 CaseTrust 業者，裝修業預付款損失 S$72.8 萬（SG-01、SG-02）。2025 年 3 月起，CASE 以最高 80% 的補貼，目標在三年內認證 500 家業者（SG-D01、SG-D04）。
5. **詐騙手法已轉向「付給我個人可打折」**。2026 年 8 月，一名 51 歲的室內設計師被捕，損失逾 S$10 萬（SG-D16、SG-D18）；2019–2021 年警方調查 100 宗不良裝修承包商案件，其中 72% 已起訴（SG-D20）。
6. **設計師沒有法定執照，法定管制只落在組屋施工端**。HDB 的承包商名錄（DRC）規定 24 個月內累計 24 點即除名（SG-D28）；SIDS 的設計師認證（SIDAS，2021 年起）屬自願性質（SG-D25）。需專業人士最終確認。
7. **工班成本由外勞制度決定**。營建業馬來西亞／北亞來源的基本技術工，每月外勞稅 S$700（＝536 USD＝16,698 TWD）（MOM，SG-D06）；S Pass 自 2025-09-01 起月薪門檻 S$3,300，外勞稅 S$650（SG-D09）。
8. **跨境沒有價格優勢**。C&W 2026 年辦公室 fit-out 新加坡為 140 USD／sq ft，低於台北的 145（TC-04）。外資可 100% 持股（SG-85），但 EP 月薪門檻 S$5,600（＝133,587 TWD，SG-87），在地人力很貴。

---

## 2. 十節正文

### Q1 市場規模與成長

**結論**：新加坡沒有「住宅翻修」或「室內設計服務」的官方或市調規模。可用的數字分成四類：(a) 營建業整體的需求與產值，(b) 家具與家飾零售市調，(c) 單一公司營收，(d) 政府翻修支出（HIP）。本研究以交易量推估的住宅翻修規模為 S$28.1 億～49.3 億／年【示意】。住宅與商業、新屋與存量的占比，都**無資料**。現況與預測分列如下。

**現況（2024–2026）**

| 來源# | 數值（原幣） | USD／TWD | 年份 | 原始定義 | 歸桶 | 標示／信心 |
|---|---|---|---|---|---|---|
| SG-D69、SG-D70（BCA） | 營建需求 S$470 億～530 億；2025 年初值 S$505 億 | 2026 年：360 億～406 億 USD＝1.12 兆～1.26 兆 TWD | 2026（預估）／2025 | BCA「construction demand」。公共住宅 S$62 億～68 億、私人住宅 S$50 億～55 億；搜尋結果未說明是否含 A&A 翻修，推論以新建為主 | 其他（整體營建） | 【實際】高（官方新聞稿） |
| SG-40（IMARC） | 392.1 億 USD | — | 2024 | 整體營建市場（含基建） | 其他 | 【示意】中 |
| SG-41（Linesight） | 2025 年成長 5.2% | — | 2025 | 營建業整體 | 其他 | 【示意】中 |
| SG-39（Ken Research） | 11.3 億 USD；家具占 61% | ＝S$14.8 億＝352 億 TWD | 2025 | 家具與家飾零售商品價值 | 家居零售 | 【示意】中 |
| SG-83（Ikano） | IKEA Singapore 營業額 S$3.842 億（−2.0%） | 2.94 億 USD＝91.7 億 TWD | FY2023 | 單一零售商；新加坡 FY2024–2025：無資料 | 家居零售 | 【實際】高 |
| SG-D65（Ikano Group） | Ikano Retail 集團 11.1 億 EUR | — | FY2025 | 涵蓋新加坡、馬來西亞、泰國、菲律賓、墨西哥 | 家居零售 | 【實際】中 |
| SG-37（Hafary，SGX） | 營收 S$2.870 億（+9.1%） | 2.20 億 USD＝68.5 億 TWD | FY2025 | 上市磁磚建材通路商 | 其他（建材） | 【實際】高 |
| SG-29；SG-D56、SG-D58 | HIP 2025 年一輪逾 S$4.07 億（約 29,000 戶）；2026 年一輪逾 S$2.53 億（逾 18,000 戶） | 3.12 億／1.94 億 USD | 2025／2026 | 政府老屋改善計畫撥款，為多年期專案金額，不是年度支出 | 住宅翻修（公部門） | 【實際】中 |
| 本研究 A | HDB 新入住翻修 S$28.1 億～33.1 億／年 | 21.5 億～25.3 億 USD＝670 億～790 億 TWD | 2025 年量×2026 年價 | BTO 交屋 19,600 戶（低信心）×S$5 萬～6 萬，加上轉售 26,169 筆×S$7 萬～8.16 萬 | 住宅翻修 | 【示意】低 |
| 本研究 B | A＋私宅轉售：S$40.1 億～45.1 億 | 30.7 億～34.5 億 USD | 同上 | 加上 14,622 筆×S$8.2 萬（SG-71、SG-60） | 住宅翻修 | 【示意】低 |
| 本研究 C | B＋私宅新售：S$44.3 億～49.3 億 | 33.9 億～37.7 億 USD＝1,057 億～1,176 億 TWD | 同上 | 再加上 10,815 筆×S$3.9 萬（新 condo，多為期房，翻修時點較晚） | 住宅翻修 | 【示意】低 |

**預測（與現況分開）**

| 來源# | 數值 | 期間 | 定義 | 標示／信心 |
|---|---|---|---|---|
| SG-D69 | 營建需求平均每年 S$390 億～460 億 | 2027–2030 | BCA 中期預測 | 【示意】高（官方預測） |
| SG-40 | 566.8 億 USD（CAGR 4.18%） | 2033 | IMARC 整體營建 | 【示意】中 |
| SG-41 | 每年 +4.2% | 2026–2029 | Linesight 營建業 | 【示意】中 |
| SG-D41、SG-D42 | 達 MOP 組屋：2026 年 13,480 戶；2026–2028 年 53,816 戶（2023–2025 年為 37,474 戶，+56.1%） | 2026–2028 | 可轉售的組屋供給，是翻修需求的領先指標 | 【實際】中（對應推定） |

**合理性檢查**：
- 以 SingStat 2025 年名目 GDP S$7,895 億（SG-D82、SG-D83）與人口 611.12 萬人（SG-D81）回推，人均 GDP 為 S$129,194＝98,885 USD，與 IMF 的 99,365 USD（TF-18）只差 0.5%，分母可信。
- 情境 C 的 S$49.3 億，約占 BCA 2026 年私人住宅營建需求（S$50 億～55 億）的九成，兩者量級相當。不過 BCA 的口徑以新建為主，兩者不能相加，也不能直接比較。
- IKEA SG 的營業額約占 Ken Research 家具家飾市場的 26%（換匯後），提示 Ken Research 的定義可能偏窄。
- **2030 年的翻修市場預測：無資料。**

### Q2 需求結構

**結論**：翻修的觸發點有三個：BTO 交屋、轉售成交、屋齡約 30 年時的 HIP。2025 年 HDB 轉售量降到五年新低，2026 上半年再年減 7%～8%；但 2026–2028 年將有一波 MOP 屆滿潮。每戶翻修價依「新屋 vs 轉售」明顯分層，轉售比 BTO 貴 20%～50%。4 房式組屋約 90 m²，以此換算，每 m² 的基本、中階、高階單價約為 S$444～622、S$778～907、S$889～1,556【示意】。設計費百分比：**無資料**。工期 8～16 週。

**新屋供給與交易量**

| 指標 | 數值 | 年份 | 來源# | 標示／信心 |
|---|---|---|---|---|
| HDB 新推組屋 | 29,975 戶（BTO 19,723＋SBF 10,252），為「推出」而非「完工」 | 2025 | SG-24 | 【實際】高 |
| BTO 計畫推出 | 約 19,600 戶，其中逾 4,000 戶等待期 <3 年；2 月一輪含 1,300 戶短等待組屋 | 2026 | SG-25、SG-26、SG-D51 | 【實際】中（計畫值） |
| BTO 完工／交屋戶數 | **無資料**（r1 的「2025 年完工 19,600 戶」疑與 2026 年推出量混淆，本輪查無官方數字） | 2025–2026 | — | — |
| HDB 轉售 | 26,169 筆（2024 年 28,986 筆，−9.7%） | 2025 | SG-20、SG-21 | 【實際】高 |
| HDB 轉售 1H | 12,533 筆（−8.3%，ERA 快報）／12,681 筆（−7.4%，ERA 季報） | 2026 上半年 | SG-D46、SG-D45 | 【實際】中 |
| HDB 轉售價格指數 | 1Q −0.1%（七年來首跌）、2Q −0.3% | 2026 | SG-D50、SG-D45 | 【實際】中 |
| 百萬新元組屋 | 1,594 筆（2025）；1H2026 共 902 筆（1H2025 為 763 筆），占轉售約 7.8% | 2025／2026 | SG-22；1H2026 對應推定 SG-D49 | 【實際】中／低 |
| 私宅成交 | 轉售 14,622 筆，占私宅全年 26,492 筆的 55.2% | 2025 | SG-71 | 【實際】中高 |
| 私宅 2Q 成交 | 6,148 筆（季增 13.6%，ERA）／約 5,420 筆（URA 快報） | 2026 | SG-D48；SG-D49（推定） | 【實際】中 |
| 轉售量預測 | 26,000～27,000 筆 | 2026 | SG-D41（ERA、SRI） | 【示意】中（預測） |

**屋齡與翻修週期**
- 30 年以上組屋的占比：**無資料**。鄰近指標有兩個：約三分之一的組屋屋齡超過 35 年（SG-68，簡中，低）；約 9 萬戶超過 40 年，約占 9%（SG-65，低）。
- HIP 原則上在屋齡約 30 年時施作第一次（SG-28）。2025 年一輪選的是 1997 年或以前建成的組屋（SG-29）。
- 組屋 MOP 為 5 年。2025 年達 MOP 的組屋只有 6,973 戶，是十多年來最低（SG-22）；2026 年增為 13,480 戶，多集中在榜鵝、淡濱尼等組屋區（SG-D41，對應推定）；2027 年約 18,939 戶（SG-D43，推定，低）。ERA 1Q2026 季報的標題為「轉售需求持穩、價格放緩」（SG-D44）；簡中房產網站也以 2025 年轉售市場回顧作為 2026 年價格展望的主題（SG-D40，僅標題）。
- **租約遞減（lease decay）壓抑老屋的大翻修意願**：組屋都是 99 年租約，屋齡 40 年的組屋在 2026 年約剩 59 年（SG-66，簡中，中）。依新加坡土地管理局的 Bala 表，剩約 60 年租期的權益約值永久地契的 80%（SG-67，簡中，低）；老組屋能否保值，市場看法分歧（SG-70，簡中，中）。據此推論，老組屋屋主較傾向依賴 HIP 這類政府改善，而不是自費全翻；這與台灣老屋「全翻」的主流做法不同。

**每戶均價（住宅翻修，平台與媒體口徑）**

| 房型／分級 | S$／戶 | USD／戶 | TWD／戶 | 年份 | 來源# | 信心 |
|---|---|---|---|---|---|---|
| 4 房 BTO（Qanvast，2025 中位數＋1%～2%） | 50,000～60,000 | 38,270～45,924 | 119.3 萬～143.1 萬 | 2026 預估 | SG-13 | 中【示意】 |
| 4 房轉售（Qanvast） | 70,000～81,600 | 53,578～62,457 | 167.0 萬～194.7 萬 | 2026 預估 | SG-13 | 中【示意】 |
| 5 房轉售（Qanvast） | 80,800～98,900 | 61,845～75,698 | 192.7 萬～235.9 萬 | 2026 預估 | SG-13 | 中【示意】 |
| 4 房 BTO 標準（中位約 S$4.8 萬）／4 房轉售 | 40,000～56,000／55,000～83,000 | 30,616～42,863／42,097～63,529 | 95.4 萬～133.6 萬／131.2 萬～198.0 萬 | 2026 | SG-D38（對應推定） | 低【示意】 |
| 4 房 BTO 中階／4 房轉售／設計師主導 | 35,000～65,000／55,000～95,000／80,000～140,000 | — ／— ／61,232～107,157 | — ／— ／190.8 萬～334.0 萬 | 2026 | SG-D35 | 低【示意】 |
| 4 房 BTO／condo（簡中平台） | 45,000～65,000／60,000～120,000 以上 | — | — | 2026 | SG-D37 | 低【示意】 |
| Condo（依房間數：1／2／3／4 房） | 15,000～30,000／25,000～50,000／40,000～60,000／50,000～80,000 | — | — | 2026 | SG-D33（引 Hometrust） | 低【示意】 |
| Qanvast 計算器 2025 區間：BTO／轉售組屋／新 condo | 36,000～82,000／51,000～97,000／40,000～52,000 | — | — | 2025 | SG-17（對應推定） | 低【示意】 |
| 平均：轉售組屋／轉售 condo／新組屋／新 condo | 67,000／82,000／44,000／39,000 | 51,282／62,763／33,678／29,851 | — | 年份未標 | SG-60 | 中【示意】 |

- Qanvast 2026 年的文章指出，4 房與 5 房的價格趨於穩定，3 房在 2024–2025 年上漲；業者之間的價格戰可能壓低部分費用（SG-13，本輪中文搜尋再次命中）。
- 轉售屋比 BTO 貴，各來源的說法：20%～40%（SG-D38）、30%～50%（SG-D37）、36%～40%（依 Qanvast 4 房區間推算，SG-13）。原因是轉售屋要拆除前屋主的廚房、浴室、磁磚與線路。個案分布很寬：Qanvast 的 4 房轉售案例從 S$3.3 萬到 S$18 萬都有（SG-D39，僅標題）。

**每 m² 單價（基本／中階／高階）**——以 4 房約 90 m² 換算（90 m² 為搜尋彙整的常用基準，非 HDB 官方面積，低）

| 分級（定義） | S$／m² | S$／sq ft | USD／m² | TWD／坪 | ÷人均 GDP（99,365 USD） |
|---|---|---|---|---|---|
| 基本：4 房 BTO 標準（SG-D38） | 444～622 | 41～58 | 340～476 | 35,049～49,068 | 0.34%～0.48% |
| 中階 A：4 房 BTO（SG-13） | 556～667 | 52～62 | 425～510 | 43,811～52,573 | 0.43%～0.51% |
| 中階 B：4 房轉售（SG-13） | 778～907 | 72～84 | 595～694 | 61,335～71,499 | 0.60%～0.70% |
| 高階：設計師主導（SG-D35） | 889～1,556 | 83～145 | 680～1,191 | 70,097～122,670 | 0.68%～1.20% |

（全為【示意】、低信心。另有平台稱「基本 S$800～1,200／sq ft、高階 S$1,500 以上」（SG-D32）。照此計算，一戶 4 房的翻修費會高達 S$77 萬～116 萬，是 Qanvast 的 10 倍以上，不合理，不予採用，見第 5 章。）

**設計費行情**：設計費以百分比表示的費率：**無資料**。收費方式有三種：按工程總額的百分比、固定包價、或併入木作加價（SG-61、SG-D36）。另有一個間接指標：直接找木工比透過 ID 公司便宜 15%～30%（SG-97，低），但這不是設計費率。2018 年的歷史資料顯示，condo 設計案平均 S$4.05 萬或 S$10.6 萬（SG-62，低）。設計施工一體是主流，但這只是定性判斷，沒有量化證據。

**工期**：BTO 約 8～12 週，轉售 4／5 房約 10～12 週（SG-14，中）；全面翻修 12～16 週（SG-76，中）。以上都不含 HDB 許可的時間。

### Q3 產業結構與主要玩家

**結論**：產業極度分散。最新的官方家數是 2022 年 4 月 ACRA 登記的裝修承包商 6,697 家（SG-04）。室內設計公司（SSIC 74191「Interior design services」）的家數、HDB DRC 登錄家數、CaseTrust 認證家數，本輪都查不到（**無資料**）。可查證的大型玩家都在建材與家居零售端；前 10～20 大 ID 公司的營收：**無資料**。

| 類型 | 玩家 | 關鍵資訊 | 來源# | 信心 |
|---|---|---|---|---|
| 產業家數 | ACRA 裝修承包商 | 6,697 家（2022-04；定義為 ACRA 登記的裝修承包商，不專指 ID） | SG-04 | 中【實際】 |
| 行業代碼 | SSIC 74191 Interior design services | 單一公司登記頁顯示此代碼。SSIC 每 5 年修訂一次；據一份指南，SSIC 2025 版自 2026-05-09 起生效，修訂逾 1,500 個代碼，ID 代碼可能變動 | SG-D22、SG-D21、SG-D23（推定） | 低 |
| 建材通路 | Hafary（SGX: 5VS） | FY2025 營收 S$2.870 億，毛利率 41.1%；服務屋主與裝修公司的 General 部門 S$1.427 億（＝1.09 億 USD） | SG-37、SG-38 | 高 |
| 家居零售 | IKEA SG（Ikano Retail 加盟經營） | FY2023 S$3.842 億；集團 FY2025 為 11.1 億 EUR | SG-83、SG-D65 | 高／中 |
| 家居零售（DTC） | Castlery | 美國約占全球營收 70%，美國關稅增加成本壓力（2026-01）；國際訂單逾 80%（2022） | SG-D66、SG-D67、SG-79 | 中 |
| 家電家具 | Courts Asia（Nojima 收購） | 某年 9 個月虧損擴大至 S$540 萬，商品與服務收入 S$1.607 億（−2.5%）；Nojima 收購價每股 S$0.205（年份不明，推定 2023 年前） | SG-D68 | 低（歷史） |
| 平台（D2C 設計施工） | Livspace | 2019 年進入新加坡；2022-11 新開 3 家體驗中心；新加坡母公司 Livspace Pte Ltd 在 2025 年分兩筆注資印度實體 INR 427 crore 與 362 crore（合計約 789 crore），進行「回流註冊」（reverse flip），尚待印度央行（RBI）核准；2025 年 2 月共同創辦人轉任董事長，由 Ramakant Sharma 接任執行長；2026 年 2 月標題稱裁員 1,000 人。新加坡 2025–2026 年的營運規模：無資料 | TE-40、TE-73、TE-72、SG-D62、SG-D63、SG-D64 | 中（裁員：低） |
| 平台 | Qanvast、HomeMatch、Hometrust、HomeRenoGuru | 見 Q4 | — | — |
| 倒閉與退出 | 營建業整體 | 2025 年停業 2,737 家；2026 年 1–7 月 2,127 家（部分因 ACRA 清理失效公司） | SG-42、SG-43 | 中／低 |
| 判例 | Concept Werk | 合約 S$12.3 萬、訂金 20%；業者在糾紛期間關閉公司，屋主在高等法院勝訴（年份未顯示） | SG-D85 | 中 |

### Q4 通路與獲客

**結論**：屋主篩選業者靠兩份官方或半官方名錄（HDB DRC、CaseTrust）加上平台。平台的差異化在於「倒閉保障」與「價格透明」，收入模式是向設計公司收訂閱或點數，不抽佣。平台的用戶數、GMV 與滲透率：**無資料**。

- **Qanvast**：2013 年在新加坡創立，2016 年進入馬來西亞（TE-47、TE-48）。早期上架費最高 S$1,500，後來改為訂閱制，例如 S$10,000 換點數購買名單，不向設計公司抽佣（TA2-82，中）。對推薦 ID 的倒閉保障上限為 S$5 萬或總費用的 50%（SG-19）。三個市場合計服務逾 70,000 位屋主（官網，TE-47／48；累計數，不是年度滲透率）。
- **HomeRenoGuru**：ID 清盤時保障合約金額的 50%，上限 S$5 萬（SG-D88）。**HomeMatch**：主打訂金保證（SG-07）；CB Insights 的公司頁提到「三年內認證 500 家業者」的目標（SG-D04），與 CASE 的計畫一致。
- **價格透明當獲客工具**：Hometrust 公開個別業者的平均案價，例如 MET Interior 平均 S$82,523（SG-D89，單一業者）；Qanvast 業者頁也公開「新屋／轉售平均花費」（SG-63）。
- **官方名錄**：HDB DRC（SG-D28）與 CaseTrust 名單（SG-06）；部分 condo 管委會要求使用認證業者（SG-D87，推定，低）。
- **銀行**：裝修貸款直接撥付給承包商（SG-33），銀行因此成為間接通路。
- **實體**：Livspace 體驗中心（TE-73）、Castlery Liat Towers 旗艦店 24,000 sq ft（SG-99）。
- **平台滲透率**：**無資料**。若以 Qanvast 累計 7 萬屋主對照每年約 4～7 萬戶新入住來看，滲透率可能不低，但兩者口徑不同（累計對年度、三國對單國），不計算。

### Q5 法規與證照（需專業人士最終確認）

**結論**：室內設計師在新加坡**沒有法定執照**，只有協會的自願認證（SIDAS）。法定管制落在三處：(1) 組屋施工須列入 HDB 的 DRC 名錄並申請許可；(2) 影響結構的增建與改建（A&A）須由合格人員（QP）向 BCA 送審；(3) 水電燃氣須由持牌技師施作。私宅還要遵守管委會（MCST）的規約。2023–2026 年未見針對裝修業的修法；政策工具是 2025 年起的 CaseTrust 認證補貼。

| 項目 | 法規／制度 | 主管機關 | 性質 | 內容 | 來源# |
|---|---|---|---|---|---|
| 組屋施工資格 | Housing and Development (Renovation Control) Rules 2006 第 6 條；Directory of Renovation Contractors（DRC） | 建屋發展局（HDB） | 法定登錄 | 只有列入 DRC 的承包商可在組屋施工；申請前須修畢 BCA 學院課程（Renovation for Public Housing） | SG-09、SG-10、SG-D28 |
| DRC 記點與除名 | DRC 記點制度 | HDB | 法定 | 24 個月內累計 ≥24 點即除名；重大違規不論點數皆可取消資格；在公共區域亂丟廢料，罰 S$500 並記 6 點，可暫停或禁止承接新組屋工程 12 個月（2023） | SG-D28、SG-D29 |
| 執法規模 | — | HDB／MND | — | 2022 年答覆：過去三年處分約 200 家（對應推定）；2018–2022 年因廢料處置不當，平均每年處分 5 家 | SG-D30、SG-D31 |
| 組屋裝修許可 | Renovation permit；鄰居通知 | HDB | 法定許可 | 拆牆、換窗須申請；須提前 5 天通知鄰居（2024；較早為 3 天）；噪音工程限平日 9:00–17:00 | SG-09、SG-11、SG-12 |
| 結構 A&A | Building Control（建築管制） | 建設局（BCA） | 法定 | 只有影響結構安全的 A&A 須 BCA 批准；圖說須由 QP（註冊建築師或土木結構 PE）提交；部分輕微工程免審 | SG-D74、SG-D75 |
| 私宅 condo | MCST 規約（by-laws） | 管委會 | 規約 | 可能須取得 MCST 批准；BCA 免審不代表 MCST 免批（二手指南） | SG-D74、SG-D76、SG-D77 |
| 水電燃氣 | 持牌水喉匠／電工 | 公用事業局（PUB）／能源市場管理局（EMA） | 法定執照 | 須持牌者施作 | SG-09 |
| 室內設計師 | 無法定執照；SIDAS（Singapore Interior Design Accreditation Scheme） | SIDS 主辦，SIDAC 監督（委員含政府機關、公會、學校） | 自願認證 | 2021-11 推出；分 Interior Design Practitioner 第 1、2、3 級；評核專業實務、建築法規、專案與合約管理、設計與技術四項能力；公開認證名單 | SG-D25、SG-D26、SG-D27、SG-50、SG-03 |
| 設計團體 | IDCS（Interior Design Confederation Singapore） | — | 協會 | 由室內設計師協會與 SIDS 合組；2017 年推「合格專業室內設計師」登錄（registry）；現以獎項與專業發展計畫為主 | SG-D24、SG-D26 |
| 消保 | Consumer Protection (Fair Trading) Act | 貿工部（MTI）／競爭與消費者委員會（CCCS） | 法定 | 涵蓋裝修的不公平行為 | SG-48、SG-04 |
| 自律認證 | CaseTrust for Renovation Businesses；另有 CaseTrust-RCMA 聯合認證（RCMA 全名與現況，搜尋結果未載明） | 消費者協會（CASE） | 協會認證 | 訂金上限 20%，並須購買訂金履約保證 | SG-06、SG-D84 |
| 2023–2026 政策 | CaseTrust 認證補貼（2025–2028） | CASE | 補貼（非修法） | 2025-03-15 宣布：銀級首年認證費最高補貼 80%，申請費加顧問費合計最高補 S$5,280，其中顧問費補 80%、上限 S$1,200；銅級補 50%，限 10 家 | SG-D01、SG-D02、SG-D03 |
| 2023–2026 修法 | — | — | — | 未見；2024-05、2025-02 有國會質詢（SG-03、SG-05）；強制認證的提案：無資料 | SG-03、SG-05 |

> 以上法規結論皆需專業人士最終確認。另有第三方網站把組屋施工資格稱為「HDB Registered Renovation Contractors Scheme（RRCS）」（SG-D86，推定），與現行官方名稱 DRC 不同，以 HDB 官方頁為準。

### Q6 消費者保護與糾紛

**結論**：CASE 的裝修投訴量從 2022 年高點 1,454 件降到 2024 年 962 件，但預付款損失反而變大，CASE 因此改以「補貼認證」擴大履約保證的覆蓋率。警方案件顯示，詐騙已從「承包商收訂金後失聯」轉向「設計師個人要求私下付款」。保固期：**無資料**；2025 全年 CASE 裝修投訴：**無資料**。

**投訴與損失時序**

| 年份 | CASE 裝修承包商投訴 | 備註 | 來源# | 信心 |
|---|---|---|---|---|
| 2019–2021 | 年均約 1,100 件 | MTI 國會答覆 | SG-04 | 中【實際】 |
| 2021 | 1,300 件 | 媒體轉述 | SG-D84 | 中【實際】 |
| 2022 | 1,454 件 | 媒體轉述 | SG-D84 | 中【實際】 |
| 2023 | 1,168 件（排名第 3） | CASE 新聞稿表 1 | SG-01、SG-D84 | 高【實際】 |
| 2024 | 962 件（排名第 4；約 97% 針對非 CaseTrust 業者） | 全行業 14,236 件 | SG-01 | 高【實際】 |
| 2025 上半年 | 全行業 6,253 件；裝修列前五大，但未單列件數 | — | SG-74 | 高／無資料 |
| 2025 全年 | **無資料** | 本輪英文、中文各搜一次，都沒有命中 | — | — |

- **預付款損失**：2024 年全行業約 S$193 萬（＝148 萬 USD＝4,604 萬 TWD），是 2023 年的四倍以上；其中裝修約 S$72.8 萬（＝55.7 萬 USD＝1,737 萬 TWD，占 37.7%）（SG-01、SG-02、SG-D05）。
- **未完工預付款投訴**：2017–2023 年每年約 120 件，涉及合約平均約 S$7,400（＝5,664 USD）；約半數經協商追回款項（SG-03、SG-D13 簡中）。這個平均合約金額遠低於整戶翻修，推論這類投訴多為小型工程，或「合約金額」指的是損失部分；原文定義未見，低。
- **投訴率（示意）**：2024 年 962 件 ÷（HDB 轉售 28,986＋私宅轉售 14,053 筆）＝每 100 筆中古成交約 2.2 件【示意】，低。
- **警方案件（詐騙型態）**

| 時間 | 手法 | 金額 | 來源# |
|---|---|---|---|
| 2019–2021 | 警方調查 100 宗不良裝修承包商案件，其中 72% 已起訴；手法為收款後只做部分工程或完全不動工 | — | SG-D20（內政部 MHA 書面答覆）【實際】中 |
| 2020-07 | 上門推銷、收款後失聯 | 逾 S$13 萬 | SG-D19【實際】中 |
| 2023-10 | 55 歲男子上門推銷，全島 20 多宗 | 逾 S$19.8 萬（＝15.2 萬 USD） | SG-D15【實際】高 |
| 2026-07 | 冒稱裝修公司員工 | 逾 S$8.6 萬（單一被害人） | SG-D17【實際】中 |
| 2026-08 | 51 歲室內設計師以「直接付給我個人可打折」為誘餌，款項用於賭博；6 月 29 日報案 | 逾 S$10 萬（＝7.65 萬 USD＝239 萬 TWD） | SG-D16、SG-D18【實際】高 |
| 2022 | 一人實際控制 3 家公司，CASE 收到 21 宗投訴，18 位屋主付了大部分訂金後工程爛尾 | 合約約 S$58 萬 | SG-D14（簡中）、SG-48 中 |

  **2025 年**的警方裝修詐騙新聞稿：本輪未命中，**無資料**。
- **制度保障**：CaseTrust 訂金上限 20%，並以訂金履約保證涵蓋業者倒閉；但保證只涵蓋訂金，不涵蓋里程碑付款（SG-06、SG-08、SG-D87）。平台另有 S$5 萬或 50% 的倒閉保障（SG-19、SG-D88）。
- **爭議解決**：先由 CASE 調解，再到小額索償庭或法院（SG-05）；業者清盤時，消費者只能以判決申報債權（SG-47）。屋主勝訴的案例罕見（SG-D85）。
- **合約範本**：官方範本：**無資料**。

### Q7 外資／台資進入規則（需專業人士最終確認）

**結論**：法律上，設計公司與裝修承包商都可以 100% 外資持股，只須一名通常居住在新加坡的董事。真正的門檻有三：(1) 組屋施工須列入 DRC；(2) 工班依賴外勞配額與外勞稅；(3) 外派主管與設計師的 EP 與 S Pass 薪資門檻逐年調升。設計公司與承包商的持股規則，搜尋結果未區分；兩者都以《公司法》的一般規定處理（推論）。

| 項目 | 規定 | 金額換算 | 年份 | 來源# | 信心 |
|---|---|---|---|---|---|
| 外資持股 | 私人有限公司可 100% 外資；至少 1 名常駐董事（公民、PR 或 EP 持有人） | — | 現行 | SG-85、SG-86 | 中 |
| EP | 新申請者月薪門檻：非金融業 S$5,600、金融業 S$6,200；須通過 COMPASS 40 分 | S$5,600＝4,286 USD＝133,587 TWD | 2025-01-01 起 | SG-87、SG-88 | 高 |
| EP 2027 | 據報調至 S$6,000 | — | 2027（已公布的未來值） | SG-89 | 低中 |
| S Pass | 新申請者月薪門檻 S$3,300（金融業 S$3,800），隨年齡遞增，40 多歲中段為 S$4,800（金融業 S$5,650）；2026-09-01 起到期的續簽也適用 | S$3,300＝2,526 USD＝78,721 TWD | 2025-09-01 起 | SG-D09、SG-D10 | 高 |
| S Pass 外勞稅 | 基本級（Tier 1）由 S$550 調升至 S$650，Tier 2 維持 S$650 | S$650＝498 USD＝15,506 TWD | 2025-09-01 | SG-D09、SG-D10 | 高 |
| S Pass 2027 | 據報調至 S$3,600（金融業 S$4,000）；KPMG 表格有此欄，但數字未擷取到 | — | 2027-01-01（預告） | SG-D11（推定）、SG-D12 | 低 |
| 營建 Work Permit 外勞稅（月） | 馬來西亞／北亞來源（NAS）／中國：高技術 S$300、基本技術 S$700；非傳統來源國（NTS）基本技術 S$900；場外製造（off-site）S$250／S$370；未取得所需技能認證者一律 S$900 | S$700＝536 USD＝16,698 TWD；S$900＝21,469 TWD | 現行（2026 年檢視） | SG-D06（MOM 官方）；SG-D07、SG-D08 佐證 | 高 |
| 外勞依存比上限 | 營建業 83.3% | — | 現行 | SG-34 | 中高 |
| 本地合格薪資（LQS） | S$1,600 調升至 S$1,800 | — | 2026-07-01 | SG-35、SG-36 | 中 |
| 組屋施工 | 須列入 DRC（外資公司也一樣；外籍業者是否有額外限制：無資料） | — | 現行 | SG-09、SG-D28 | 中 |

- **外商案例**：IKEA 由瑞典 Ikano 集團加盟經營（SG-83、TE-66）；日本 Nitori 在 2022 年進入新加坡（TE-25，低）；印度 Livspace 在 2019 年進入，2022 年擴點，2025 年把控股架構遷回印度（見 Q3）。反向案例是新加坡業者出海：Castlery 營收以美國為主（SG-D66），Hafary 併購上海 MML（SG-37）。
- **台資案例**：**無資料**。2011 年有一則台灣家具廠主計畫到新加坡開店的報導，後續不明（TE-85，低）。
- **稅務提示**：IRAS 認為，若董事會不在新加坡開會、代名董事沒有實權，可能影響公司的稅務居民身分（SG-86）。這只是提示，不是稅務建議。

### Q8 消費者行為

**結論**：翻修主力是 BTO 首購族與轉售屋買家，預算依房型與新舊分層。付款採「訂金 ≤20%＋里程碑」。融資以無擔保裝修貸款為主，上限 S$3 萬。政府直接出錢改善老屋與高齡設施：HIP 每戶約 S$1.4 萬由政府負擔；EASE 2.0 讓長者只付 5%～12.5%。風格偏好與決策歷程：**無資料**。

- **誰在裝修**：BTO 交屋者、轉售買家（Q2）。高端需求：百萬新元組屋 2025 年 1,594 筆（SG-22），1H2026 占轉售約 7.8%（推定，低）。高齡化：公民中 65 歲以上占 20.7%（2025-06；2015 年為 13.1%）（SG-D80、SG-D81），HIP 與 EASE 的需求因此持續。
- **預算分級**：見 Q2。新屋約 S$3.9 萬～4.4 萬，轉售約 S$6.7 萬～8.2 萬（SG-60），設計師主導 S$8 萬～14 萬（SG-D35）。平台建議另留約 15% 預備金（SG-D38，推定）。
- **付款**：訂金 ≤20%（CaseTrust，SG-06）。各階段的比例：**無資料**。2026 年的詐騙案顯示，消費者被教育「只付款到公司帳戶」（SG-D16）。
- **融資**：裝修貸款上限為「月薪 6 倍或 S$3 萬，取較低者」（＝22,962 USD＝71.6 萬 TWD），由銀行直接撥給承包商（SG-32、SG-33，中）。
- **政府補助**

| 計畫 | 內容 | 金額 | 年份 | 來源# | 信心 |
|---|---|---|---|---|---|
| HIP 2025 輪 | 約 29,000 戶以上，1997 年或以前建成 | 逾 S$4.07 億；每戶約 S$14,034【示意】 | 2025 | SG-28、SG-29 | 中 |
| HIP 2026 輪 | 逾 18,000 戶、12 個市鎮、198 座組屋 | 逾 S$2.53 億（＝1.94 億 USD＝60.4 億 TWD）；每戶約 S$14,056【示意】 | 2026-05 | SG-D56、SG-D57、SG-D58、SG-D59 | 中 |
| HIP 自付 | 必要項目由政府全額負擔（公民）；選配項目最高補 95%。5 房自付 S$1,199（10%），Executive 自付 S$1,498.75（12.5%）；HIP 推出以來政府累計支出約 S$50 億 | — | 2026 | TD-74、SG-D60（推定） | 中／低 |
| EASE 2.0 | 2024-04 起，項目由 3 項增至 11 項（坐浴沖洗器、可折式 U 型扶手、降低浴室門檻、折疊淋浴椅、搖桿開關、住宅火警警報器等）；逾 11,000 戶已申請 | 公民自付 5%～12.5%（即政府最高補 95%）；基本套餐 S$125～312.50（＝2,982～7,455 TWD） | 2024– | SG-D52、SG-D53、SG-D54、SG-D55、TD-71 | 中 |
| EASE（私宅） | 2025 年預算案宣布，2026–2028 年試行；有長者的公民私宅家戶，可向預審合格名單上的承包商申請 | 補 75%，上限 S$1,200（＝28,626 TWD） | 2026–2028 | SG-31、SG-D52、SG-D61 | 中 |

### Q9 人才與工班

**結論**：設計人才的薪資有兩種口徑。全體設計師月薪中位數約 S$6,000（2022，NDIMS）；室內設計師的聚合站數據偏低，中期約年薪 S$41,196。施工端幾乎全靠外勞，人力成本由外勞稅與配額決定（Q7）。設計科系畢業人數、監工薪資、泥作與水電日薪：**無資料**。

| 指標 | 數值 | 換算 | 年份 | 來源# | 定義／信心 |
|---|---|---|---|---|---|
| 設計師月薪中位數（全體設計職類） | 約 S$6,000 | 4,592 USD＝143,129 TWD | 2022 | SG-D78 | DesignSingapore NDIMS，含所有設計職類，非室內專屬；中【實際】 |
| 設計勞動力 | 2021–2030 年成長 25%（需再增 17,000 人，CAGR 2.5%）；67% 在非設計產業任職 | — | 2021／預測 | SG-D78、SG-D79 | 調查逾 230 家企業；中 |
| 室內設計師年薪（入門／中期／資深） | S$26,729／41,196／49,503 | 中期＝31,532 USD＝98.3 萬 TWD | 2026 | SG-90～92 | Payscale 聚合；低中 |
| ID 招聘月薪 | S$2,800～4,500 | — | 2026 | SG-93 | 招聘廣告；中 |
| 木工日薪 | S$150～180 | 3,578～4,294 TWD | 約 2025 | SG-96 | 商業部落格；低 |
| 營建外勞稅 | S$300～900／月 | 7,156～21,469 TWD | 現行 | SG-D06 | MOM 官方；高 |
| 非居民人口 | 191 萬（+2.7%），成長主要來自 Work Permit 持有人 | — | 2025-06 | SG-D80 | 官方；高 |

- **缺工訊號**：2025 年營建業停業 2,737 家（SG-42）；2026 年有室內設計師受訪表示，同業因成本上升與外商競爭而結業（SG-43，低中）。
- **師傅**：泥作、水電日薪：**無資料**。新加坡施工的人力結構是「外籍師傅＋本地 ID 或監工」，與台灣「本地師傅＋移工輔助」不同（推論）。

### Q10 材料供應鏈與價格

**結論**：2025 年材料價格壓力緩和，Hafary 毛利率回升、T&T 估 2025 年營建成本只漲 1%。2026 年因中東衝突推升能源與運費，水泥與預拌混凝土再度上漲；T&T 預估 2026 年漲約 4%、2027 年漲 5%。在地品牌、進口依賴度與關稅：**無資料**。

| 指標 | 數值 | 年份 | 來源# | 標示／信心 |
|---|---|---|---|---|
| 散裝水泥 | S$115.90 → 120.00（初值）／噸（+3.5%） | 2025-12 → 2026-03 | SG-D71（統計局 PDF，對應推定） | 【實際】中 |
| 預拌混凝土 | S$129.50 → 140.00／m³（+8.1%） | 同上 | SG-D71 | 【實際】中 |
| 鋼筋 | 約 S$660～663／噸（持平；＝507 USD） | 同上 | SG-D71 | 【實際】中 |
| 營建成本通膨 | 2025 年 1%；預估 2026 年約 4%、2027 年 5% | 2025／預測 | SG-D72（Turner & Townsend） | 現況【實際】中；預測【示意】 |
| 材料價格 | 2026 年 7 月 CNA 報導：混凝土、水泥、鋼筋、瀝青價格仍居高 | 2026 | SG-D73（轉述） | 低 |
| Hafary 毛利率 | 41.1%（FY2024 40.3%），稱投入成本緩和 | FY2025 | SG-37、SG-38 | 【實際】高 |
| 木作占預算 | 28%～35% | 2026 | SG-97 | 【示意】低 |
| 木作單價 | S$150～450／sq ft（定義不明，可能為每呎長） | 2026 | SG-D34 | 低 |
| 住宅翻修價格 | Qanvast：4／5 房趨穩，3 房在 2024–2025 年上漲；以 1%～2% 通膨推估 2026 年 | 2026 | SG-13 | 【示意】中 |

---

## 3. 本市場對台灣業者（璞石）的啟示

1. **把「交易量」當成裝修需求的主公式，並建立成交即報價的轉換漏斗**。新加坡的翻修需求，大致等於「交屋量＋轉售量」乘以每戶單價（第 2 章 Q1）。2026–2028 年 MOP 屆滿潮（53,816 戶，SG-D42）會直接轉為裝修訂單。台灣 2025 年買賣移轉年減 25.5%，但第一次登記年增 8.4%（TW-14），結構相同：交屋潮撐住需求。璞石的不動產線可以在交屋前 60 天，把客變、設計、軟裝與家具綁成一張報價單，並追蹤「成交→簽約」的轉換率。（推論）
2. **把信任做成可賣的產品，而不只是口號**。新加坡 97% 的投訴針對非認證業者（SG-01）；政府補貼 80% 認證費，目標認證 500 家（SG-D01）；警方案件集中在「私下付款可打折」（SG-D16）。璞石可以自行宣示四件事：訂金 ≤20%、價金信託或履約保證、只收公司帳戶、合約審閱期 7 日（對齊內政部草案，TW-37），並把這些印在報價單首頁。這在宜蘭與信義區都是對抗低價工班的差異化。（推論）
3. **台灣的裝修相對所得偏貴，「透明標準包」有空間**。新加坡 4 房轉售每 m² 只占人均 GDP 的 0.60%～0.70%，台灣中古屋是 2.46%～3.69%（第 4 章，【示意】）。新加坡平台公開各業者的中位案價（SG-63、SG-D89），並以分級標準包報價。璞石可推出「坪數×等級」的公開價目，作為集客入口；家居零售線同時提供系統櫃與建材，Hafary 服務屋主與裝修公司的部門毛利率為 41.1%（SG-37），可作參考。（推論）
4. **學新加坡把高齡改造做成「政府出錢、業者標準化施工」的量產單**。HIP 每戶政府約投入 S$1.4 萬（約 33.5 萬 TWD，【示意】），EASE 2.0 有 11 個標準項目，長者自付 5%～12.5%（SG-D52）。宜蘭高齡人口多，璞石可以把長照 2.0 的居家無障礙補助（4 萬元／3 年，TD 筆記）包成固定品項與價格的「高齡安全包」，向市府或社福單位爭取指定施工。（推論）
5. **新加坡適合當制度標竿與採購或品牌據點，不適合作為規模化的施工市場**。C&W 的 fit-out 單價台北（145 USD／sq ft）已高於新加坡（140）（TC-04），設計人力的 EP 門檻 S$5,600（SG-87）、工班外勞稅 S$700～900（SG-D06）。若要進入，建議路徑依序是：(a) 跟隨台商客戶承接辦公或展示空間的設計；(b) 與已列入 DRC 且有 CaseTrust 認證的在地公司合作，或少數持股；(c) 不要自建施工隊。（需專業人士最終確認）

---

## 4. 與台灣比較的錨點

> 共同分母：人均 GDP 新加坡 99,365 USD、台灣 39,489 USD（2025，IMF WEO 2026-04，TF-18）；新加坡名目 GDP S$7,895 億＝6,043 億 USD（SG-D82），人口 611.12 萬（2025-06，SG-D81）；台灣名目 GDP 9,200.5 億 USD（TF-20），人口約 2,330 萬（IMF 隱含值，TF 筆記導出，【示意】）。匯率見檔首。

| 錨點 | 新加坡 | 台灣 | 公式與註記 | 標示／信心 |
|---|---|---|---|---|
| 人均翻修支出 | 情境 A（只算 HDB）：352～415 USD／人（＝S$460～542＝10,969～12,920 TWD）；情境 C（含私宅）：555～617 USD／人 | 上限值 757 USD／人（5,500 億 TWD，含商業，TW-23）；歷史值 275 USD／人（2,000 億 TWD，2000 年代，TW-26，年代錯配） | 規模÷人口。新加坡只算交易觸發的住宅翻修，台灣上限值含商業與 B2B 重複計算，方向相反、不可直接比較 | 【示意】低 |
| 翻修市場占 GDP 比 | 情境 A 0.36%～0.42%；情境 C 0.56%～0.62% | 1.92%（上限值）；0.70%（歷史值） | 規模÷名目 GDP（新加坡 S$7,895 億；台灣 9,200.5 億 USD） | 【示意】低 |
| 每 m² 單價÷人均 GDP | 基本 0.34%～0.48%；中階（4 房 BTO）0.43%～0.51%；中階（4 房轉售）0.60%～0.70%；高階 0.68%～1.20% | 基本 0.74%～1.47%（3～6 萬／坪）；中階新成屋 1.47%～2.46%（6～10 萬）；中古屋 2.46%～3.69%（10～15 萬）；高階 3.69%～4.92%（15～20 萬） | （每戶價÷90 m²÷1.3065）÷99,365；台灣為（每坪價÷3.3058÷31.1663）÷39,489。新加坡含木作與設計（設計常併入木作加價），台灣不含設計費（TW-22、TW-C2、TW-19） | 【示意】低 |
| 每 m² 絕對值（USD） | 340～1,191 | 291～1,941 | 同上 | 【示意】低 |
| 設計費占工程費比 | **無資料**（收費方式為百分比、包價或併入木作；SG-61） | 約 13%～15%（20 坪新成屋，TW-21） | 設計費÷工程費 | 台灣【示意】低 |
| 設計公司家數÷人口 | 10.96 家／萬人（ACRA 裝修承包商 6,697 家〔2022-04，SG-04〕÷611.12 萬人〔2025〕） | 2.13 家／萬人（室內裝修業 4,969 家〔2011，TW-30〕÷約 2,330 萬人） | 家數÷人口×10,000。新加坡口徑為所有登記的裝修承包商，台灣只算特許的「室內裝修業」，且兩邊年份錯配。不可據此斷言新加坡業者密度是台灣的 5 倍 | 【示意】低 |
| 平台滲透率 | **無資料**（Qanvast 三國累計服務 >7 萬屋主，TE-47） | **無資料** | 平台成交戶÷年度裝修戶 | — |
| 補充：辦公 fit-out | 140 USD／sq ft（＝1,507 USD／m²＝155,260 TWD／坪） | 台北 145 USD／sq ft | C&W 2026 版，價格基準 2025-12（TC-04） | 【實際】高 |
| 補充：30 年以上屋齡占比 | **無資料**（約三分之一超過 35 年，SG-68，低） | 約 59%（2025 Q2，TW-13） | — | — |
| 補充：中古交易量 | HDB 轉售 26,169＋私宅轉售 14,622＝40,791 筆（2025） | 買賣移轉 261,308 棟（2025，TW-14） | 每千人：新加坡 6.7 筆、台灣 11.2 棟【示意】 | 【示意】中 |

**讀法**：新加坡人均所得是台灣的 2.5 倍，但裝修的絕對單價與台灣相近，甚至更低，翻修支出占 GDP 也較低。可能的原因（推論）有三：(1) 組屋交屋時已附地磚與部分衛浴，工程範圍較小；(2) 外勞使施工工資受到壓抑；(3) GDP 中金融與貿易的比重高，拉大了分母。

---

## 5. 矛盾資料與資料缺口

### 5.1 矛盾表

| 指標 | 來源 1 | 來源 2 | 差異與原因 | 裁決 |
|---|---|---|---|---|
| 每 sq ft 翻修單價 | S$800～1,200 psf（基本）、S$1,500+（高階）（SG-D32） | 依 Qanvast 推算 S$52～84 psf（SG-13） | >10 倍。推論前者混淆了房價 psf 或面積單位 | 不採用 SG-D32 |
| 營建業外勞稅 | r1：S$500／650（SG-36 等第三方） | MOM：高技術 S$300、基本 S$700、NTS 基本 S$900（SG-D06） | r1 的第三方說法過時或口徑錯誤 | 採 MOM 官方表（解決 r1 的矛盾） |
| 4 房 BTO 每戶價 | S$50,000～60,000（SG-13） | S$40,000～56,000（SG-D38）；S$35,000～65,000（SG-D35）；S$45,000～65,000（SG-D37） | 中點差 <30%；樣本與分級定義不同 | 並列，以 SG-13 為主 |
| 轉售比 BTO 貴多少 | 20%～40%（SG-D38） | 30%～50%（SG-D37）；Qanvast 推算 36%～40% | 定義（同房型或不同房型） | 並列，記錄為 20%～50% |
| HDB 2Q2026 轉售量 | 6,268 筆（ERA 快報，SG-D46） | 6,396 筆（ERA 季報，SG-D45）；6,203 筆（OrangeTee，依 caveat 計，SG-D47） | 差 3%；資料時點與方法不同 | 採 HDB 最終值（待取得）；暫列範圍 |
| 1H2026 HDB 轉售量 | 12,533 筆（SG-D46） | 12,681 筆（SG-D45） | 差 1.2%；同上 | 並列 |
| 2Q2026 私宅成交 | 約 5,420 筆（URA 快報，SG-D49 推定） | 6,148 筆（ERA，SG-D48） | 差 13%；快報與修正值不同 | 採 6,148（較新） |
| Castlery 美國營收占比 | 65%（SG-79） | 約 70%（SG-D66，2026）；78%（SG-78，最大線上商店） | 年份與口徑（全通路 vs 單一線上店） | 全公司採約 70%（較新） |
| Ikano Retail FY2024 營收 | 10.7 億 EUR（公司頁，SG-D65 群組） | 10.9 億 EUR（新聞，SG-D90） | 差 2%；匯率或口徑 | 採公司頁 |
| CASE 2021 裝修投訴 | 1,300 件（SG-D84） | 2019–2021 年均約 1,100 件（SG-04） | 一個是單年、一個是三年平均，兩者相容 | 不構成矛盾 |
| CASE 裝修投訴排名 | 2023 年第 3（SG-D84） | 2024 年第 4（SG-01） | 不同年份 | 不構成矛盾 |
| HIP 居民自付 | S$630～1,575（TD-74，舊指南） | 5 房 S$1,199、Executive S$1,498.75（SG-D60） | 一個是區間、一個是分房型；年份不同 | 採較新的 SG-D60（低） |
| 組屋施工登錄名稱 | RRCS（SG-D86，第三方） | DRC（SG-09、SG-D28，HDB 官方） | 第三方用了舊名稱 | 採 DRC |
| IDCS 與 SIDS 的關係 | IDCS 由室內設計師協會與 SIDS 合組（SG-D26） | SIDS 在 2021 年仍以自身名義推 SIDAS（SG-D25） | 組織層級（聯合會 vs 成員團體）不明 | 兩者並列，需向 SIDS 確認 |
| BCA 2026 規模 | 營建需求 S$470 億～530 億（SG-D69） | 某聚合頁稱 S$430 億～460 億（SG-D70 搜尋彙整） | 需求 vs 產出（output），口徑不同 | 採 BCA 需求值 |
| Livspace 新加坡現況 | 委託書假設「撤出新加坡」 | 2022 年新開 3 家；2025 年控股遷回印度；新加坡營運未見撤出報導（TE-73、SG-D62） | 「撤出」未獲證實 | 判定：控股回流，新加坡營運現況無資料 |
| 未完工預付款投訴的合約金額 | 平均約 S$7,400（SG-D13） | 整戶翻修 S$4 萬～8 萬（SG-13） | 差 5 倍以上；推論定義為小型工程或損失金額 | 只作投訴樣本特徵，不代表市場均價 |

### 5.2 缺口表

| 項目 | 本輪試過的搜尋 | 建議取得方式 |
|---|---|---|
| 住宅翻修／室內設計服務的官方規模 | r1 #1；本輪 BCA 搜尋只取得營建總需求 | SingStat 營建業產值中的 A&A 細項；BCA「construction demand」的 A&A 分項 |
| CASE 2025 全年裝修投訴、預付款損失 | 英文 #1、中文 #4 | case.org.sg 2026 年 2 月新聞稿；直接向 CASE 索取 |
| 2025 年警方裝修詐騙統計 | 英文 #6、中文 #7（只取得 2020、2023、2026 年個案與 2019–2021 年 100 宗） | SPF 年度詐騙統計（scam types）；國會答覆 |
| ACRA 室內設計公司家數（SSIC 74191 或 2025 版新代碼） | #8 | data.gov.sg 的 ACRA 實體資料集，依主要業務代碼篩選「Live」狀態 |
| HDB DRC 登錄家數、CaseTrust 認證裝修業者家數（含 500 家目標的進度） | #5、#10、#22 | HDB DRC 名錄頁計數；CASE 年報；CaseTrust 名單（renodots 等第三方列表） |
| SIDAS 認證人數、IDCS 會員數 | #9 | SIDS 公開名單 |
| BTO 完工與交屋戶數（2025、2026） | #12、#13 | HDB 年報、MND 國會答覆 |
| 30 年以上組屋占比（同口徑） | r1 #19、#22 | HDB Key Statistics「Age of HDB dwellings」 |
| 每 m² 單價的官方或大樣本口徑；HDB 各房型官方樓面面積 | #11、#29 | Qanvast 年度成本指南全文；HDB 房型面積表 |
| 設計費占工程費的百分比 | #20 | ID 公司報價單樣本；SIDS 收費指引 |
| 平台用戶數、GMV、滲透率 | 未專搜 | Qanvast 與 Hometrust 媒體專訪；ACRA 財報 |
| IKEA SG FY2024–2025、Courts SG 2025、Castlery 營收實數 | #18、#19 | Ikano 年報；Nojima 年報的海外分部；Castlery 媒體稿 |
| 監工薪資、泥作與水電日薪、設計科系畢業人數 | #26（NDIMS 只有全體設計師） | MOM Occupational Wage Survey；MOE 高教統計 |
| 進口依賴度、關稅、在地品牌 | #24（只取得水泥、混凝土、鋼筋價格） | SingStat 進口統計（HS 69、94）；BCA 材料價格表 |
| 保固期與官方合約範本 | 未專搜 | CASE 範本合約；CaseTrust 認證條款全文（SG-D03） |
| 台資進入新加坡的案例 | 未專搜（r1 TE 只有 2011 年一例） | 台灣駐新加坡代表處；新加坡台灣商會 |

---

## 6. 來源清單

讀取方式：全部為「搜尋結果內容」（未直接開啟網頁）。r1 編號的讀取方式均為「r1 筆記轉引（搜尋結果內容）」；本輪新增的 SG-D 編號為本輪搜尋取得。標「推定」者，表示數字與 URL 的對應是依搜尋彙整推斷的。

### 6.1 沿用 r1 編號

| # | 標題 | 機構 | 年份 | 語言 | URL | 讀取方式 |
|---|---|---|---|---|---|---|
| SG-01 | CASE sees prepayment losses more than quadruple in 2024（Media Release） | CASE | 2025 | 英 | https://www.case.org.sg/wp-content/uploads/2025/02/Media-Release-CASE-sees-prepayment-losses-more-than-quadruple-in-2024-entertainment-related-complaints-nearly-triple.pdf | r1 轉引；本輪再次命中 |
| SG-02 | Home renovations make up bulk of consumers' losses in 2024: Case | AsiaOne | 2025 | 英 | https://www.asiaone.com/singapore/home-renovations-make-bulk-consumers-losses-2024-case | r1 轉引；本輪再次命中 |
| SG-03 | Written reply to PQs on disputes arising from Interior Design and Renovation firms | MTI | 2024 | 英 | https://www.mti.gov.sg/newsroom/written-reply-to-pqs-on-disputes-arising-from-interior-design-and-renovation-firms/ | r1 轉引；本輪再次命中 |
| SG-04 | Written reply to PQ on renovation contractors | MTI | 2022 | 英 | https://www.mti.gov.sg/Newsroom/Parliamentary-Replies/2022/07/Written-reply-to-PQ-on-renovation-contractors | r1 轉引 |
| SG-05 | Written reply to PQ on consumer protection for customers of non-accredited renovation contractors | MTI | 2025 | 英 | https://www.mti.gov.sg/Newsroom/Parliamentary-Replies/2025/02/Written-reply-to-PQ-on-consumer-protection-for-customers-of-non-accredited-renovation-contractors | r1 轉引 |
| SG-06 | CaseTrust Accreditation for Renovation Businesses | CASE／CaseTrust | 現行 | 英 | https://www.case.org.sg/casetrust/casetrust-accreditation-for-renovation-businesses/ | r1 轉引 |
| SG-07 | Should you work with CaseTrust-accredited Renovators? | HomeMatch | 年份未明 | 英 | https://homematch.sg/ask/why-work-with-casetrust-accredited-renovators | r1 轉引 |
| SG-08 | Commercial Renovation Contracts & Quotations in Singapore | Adevo | 年份未明 | 英 | https://www.adevo.sg/commercial-renovation-contracts-quotations-singapore/ | r1 轉引 |
| SG-09 | Renovation（Renovation Contractors） | HDB | 現行 | 英 | https://www.hdb.gov.sg/business/renovation-contractors/renovation | r1 轉引 |
| SG-10 | Renovation for Public Housing（course） | BCA Academy | 現行 | 英 | https://www.bcaa.edu.sg/backend-pages/course/renovation-for-public-housing | r1 轉引 |
| SG-11 | Written answer by MND on reviewing renovation permits | MND | 推定 2024 | 英 | https://www.mnd.gov.sg/newsroom/speeches/view/written-answer-by-ministry-of-national-development-on-reviewing-renovation-permits | r1 轉引；本輪再次命中 |
| SG-12 | 8 HDB Renovation Rules and Restrictions | Renonation | 年份未明 | 英 | https://www.renonation.sg/hdb-renovation-rules-and-restrictions-that-homeowners-need-to-take-note-of | r1 轉引 |
| SG-13 | What are the expected renovation costs for HDB flats in 2026 | Qanvast | 2026 | 英 | https://qanvast.com/sg/articles/what-are-the-expected-renovation-costs-for-hdb-flats-in-2026-3568 | r1 轉引；本輪再次命中 |
| SG-14 | Qanvast 2025 成本／工期文章 | Qanvast | 推定 2025 | 英 | https://qanvast.com/sg/articles/-3384 | r1 轉引 |
| SG-17 | Renovation Calculator | Qanvast | 2025 更新 | 英 | https://qanvast.com/sg/renovation-calculator?variant=A | r1 轉引；本輪再次命中 |
| SG-19 | How To Protect Yourself From Renovation Scams | Qanvast | 年份未明 | 英 | https://qanvast.com/sg/articles/how-to-protect-yourself-from-renovation-scams-1163 | r1 轉引 |
| SG-20 | HDB resale price growth slows but million-dollar flats' prices gain 2.3% in 4Q2025 | EdgeProp SG | 2026 | 英 | https://edgeprop.sg/property-news/hdb-resale-price-growth-slows-million-dollar-flats-prices-gain-23-4q2025 | r1 轉引 |
| SG-21 | HDB & URA Q4 2025 statistics | 99.co | 2026 | 英 | https://www.99.co/singapore/insider/hdb-ura-q42025-statistics/ | r1 轉引 |
| SG-22 | 4Q 2025 HDB Quarterly Report（press release） | ERA Singapore | 2026 | 英 | https://www.era.com.sg/press-release/4q-2025-hdb-quarterly-report-hdb-resale-transactions-moderate-to-end-2025 | r1 轉引 |
| SG-24 | October 2025 BTO Sales Exercise | HDB | 2025 | 英 | https://www.hdb.gov.sg/about-us/news-and-publications/press-releases/october-2025-bto-sales-exercise | r1 轉引 |
| SG-25 | HDB plans 19,600 BTO flats in 2026 | 99.co | 2026 | 英 | https://www.99.co/singapore/insider/hdb-plans-19600-bto-flats-in-2026-over-4000-with-shorter-waits/ | r1 轉引 |
| SG-26 | 19,600 BTO flats in 2026: launch dates, shorter wait times | Stacked Homes | 2026 | 英 | https://stackedhomes.com/19600-bto-flats-2026-launch-dates-shorter-wait-times/ | r1 轉引；本輪再次命中 |
| SG-28 | HDB Home Improvement Programme 2025 | 99.co | 2025 | 英 | https://www.99.co/singapore/insider/hdb-home-improvement-programme-2025/ | r1 轉引 |
| SG-29 | Over 29,000 HDB flats selected for $407 mil upgrading | EdgeProp SG | 2025 | 英 | https://edgeprop.sg/amp/property-news/over-29000-hdb-flats-selected-407-mil-upgrading | r1 轉引 |
| SG-31 | Enhancement for Active Seniors (Private Housing) Programme | MND | 2025–2026 | 英 | https://www.mnd.gov.sg/newsroom/speeches/view/enhancement-for-active-seniors-(private-housing)-programme | r1 轉引；本輪取得內容 |
| SG-32 | How Much Renovation Loan Can I Get in Singapore? | SingSaver | 年份未明 | 英 | https://www.singsaver.com.sg/personal-loan/blog/how-much-renovation-loan-can-i-get | r1 轉引 |
| SG-33 | How Does A Renovation Loan Work In Singapore? | SingSaver | 年份未明 | 英 | https://www.singsaver.com.sg/personal-loan/blog/how-does-a-renovation-loan-work | r1 轉引 |
| SG-34 | What is the foreign worker levy | MOM | 現行 | 英 | https://www.mom.gov.sg/passes-and-permits/work-permit-for-foreign-worker/foreign-worker-levy/what-is-the-foreign-worker-levy | r1 轉引 |
| SG-35 | Singapore Work Permit 2026 guide | Raffles Corporate Services | 2026 | 英 | https://rafflescorporateservices.com/singapore-work-permit-2026-eligibility-quota-levy/ | r1 轉引 |
| SG-36 | Foreign worker levy Singapore 2026 guide | Singapore Employment Agency | 2026 | 英 | https://singaporeemploymentagency.com/foreign-worker-levy-singapore-2026-guide/ | r1 轉引 |
| SG-37 | HHL Interim FS – FY2025 Final | Hafary Holdings（SGX） | 2026 | 英 | https://links.sgx.com/1.0.0/corporate-announcements/0D6QYQB30LNU0IC8/874465_HHL%20Interim%20FS%20-%20FY2025%20Final.pdf | r1 轉引 |
| SG-38 | Hafary FY2025 revenue at S$287.0 million | Tiger Brokers | 2026 | 英 | https://www-web.itiger.com/news/1129153147 | r1 轉引 |
| SG-39 | Singapore Furniture & Home Decor Market | Ken Research | 2025 | 英 | https://www.kenresearch.com/industry-reports/singapore-furniture-home-decor-market | r1 轉引 |
| SG-40 | Singapore Construction Market 2025–2033 | IMARC | 2025 | 英 | https://www.imarcgroup.com/singapore-construction-market | r1 轉引 |
| SG-41 | Singapore construction industry to grow 4.2% annually 2026–2029: Linesight | EdgeProp SG | 2026 | 英 | https://www.edgeprop.sg/property-news/singapore-construction-industry-grow-42-annually-2026-2029-linesight | r1 轉引 |
| SG-42 | Singapore business closures 2025 | Vulcan Post | 2026 | 英 | https://vulcanpost.com/910484/singapore-business-closures-2025/ | r1 轉引 |
| SG-43 | Business closures in Singapore jump almost 13 percent | Asia News Network | 2026 | 英 | https://asianews.network/?p=297484 | r1 轉引（推定） |
| SG-47 | Written Answer by Minister for Law to PQ on claims against home renovation firms | MinLaw | 2021 | 英 | https://www.mlaw.gov.sg/news/parliamentary-speeches/2021-04-05-written-answer-by-minister-for-law-mr-k-shanmugam-to-pq-claims-made-against-home-renovation-firms-that-failed-to-deliver-after-accepting-a-deposit/ | r1 轉引 |
| SG-48 | Sense Construction（consumer alert） | CASE | 2022 | 英 | https://www.case.org.sg/list/sense-construction/ | r1 轉引；本輪再次命中 |
| SG-50 | Singapore's legally embattled renovation and interior design sector | FixFirst | 年份未明 | 英 | https://fixfirst.sg/home-repair/singapores-legally-embattled-renovation-and-interior-design-sector-an-explainer/ | r1 轉引 |
| SG-60 | Home renovations cost Singapore | Income Insurance | 年份未明 | 英 | https://www.income.com.sg/blog/home-renovations-cost-singapore | r1 轉引；本輪再次命中 |
| SG-61 | Renovation design cost Singapore | Megafurniture | 約 2025–2026 | 英 | https://megafurniture.sg/blogs/articles/renovation-design-cost-singapore | r1 轉引 |
| SG-62 | How much for interior designers in Singapore: Updated 2018 | Home & Decor SG | 2018 | 英 | https://www.homeanddecor.com.sg/renovation/how-much-for-interior-designers-in-singapore-updated-2018 | r1 轉引 |
| SG-63 | Ace Interior Design（業者頁） | Qanvast | 年份未明 | 英 | https://qanvast.com/sg/interior-designers-architects/ace-interior-design-2221 | r1 轉引 |
| SG-65 | Ageing HDB flats ideas Singapore | PropertyGuru | 年份未明 | 英 | https://www.propertyguru.com.sg/property-guides/ageing-hdb-flats-ideas-singapore-30624 | r1 轉引 |
| SG-66 | When to sell 40-year-old HDB flat（中文版） | PropertyNet.sg | 2026 | 簡中 | https://propertynet.sg/zh/when-to-sell-40-year-old-hdb-flat-lease-decay-timing-2026/ | r1 轉引（推定） |
| SG-67 | HDB lease decay: Bala curve（中文版） | PropertyNet.sg | 2026 | 簡中 | https://propertynet.sg/zh/hdb-lease-decay-balas-curve-flat-values-60-year-mark-2026/ | r1 轉引（推定） |
| SG-68 | Ageing HDB, 75 years lease（中文版） | PropertyNet.sg | 2026 | 簡中 | https://propertynet.sg/zh/ageing-hdb-75-years-lease-sell-now-or-wait-vers-2026/ | r1 轉引（推定） |
| SG-70 | Can older HDB flats really hold their value?（中文版） | Stacked Homes | 2024 | 簡中 | https://stackedhomes.com/zh/can-older-hdb-flats-really-hold-their-value-a-look-at-resale-price-trends-in-2024/ | r1 轉引 |
| SG-71 | 4Q 2025 URA Real Estate Statistics（press release） | ERA Singapore | 2026 | 英 | https://www.era.com.sg/press-release/4q-2025-ura-real-estate-statistics-private-home-demand-momentum-carries-from-3q-2025-sets-firm-outlook-for-2026 | r1 轉引 |
| SG-74 | CASE sees increase in prepayment losses for the beauty industry in 1H2025 | CASE | 2025 | 英 | https://www.case.org.sg/wp-content/uploads/2025/08/Media-Release-CASE-sees-increase-in-prepayment-losses-for-the-beauty-industry-in-the-first-half-of-2025.pdf | r1 轉引；本輪再次命中 |
| SG-76 | BTO vs resale HDB renovation cost | Ohmyhome | 年份未明 | 英 | https://ohmyhome.com/en-sg/blog/bto-vs-resale-hdb-renovation-how-much-does-it-cost | r1 轉引 |
| SG-78 | Castlery Company & Revenue | ECDB | 2025 | 英 | https://ecdb.com/resources/sample-data/retailer/castlery | r1 轉引 |
| SG-79 | Castlery first US store New York | Vulcan Post | 約 2025 | 英 | https://vulcanpost.com/910270/castlery-first-us-store-new-york/ | r1 轉引 |
| SG-83 | Ikano Retail, owner of IKEA Singapore, posts EUR 1.08 billion | IKEA SG Newsroom | 2023 | 英 | https://www.ikea.com/sg/en/newsroom/corporate-news/ikano-retail-owner-of-ikea-singapore-posts-eur-1-08-billion-in-total-turnover-pub3bd2f4e0 | r1 轉引；本輪再次命中 |
| SG-85 | Singapore foreign ownership rules | ASEAN Briefing | 年份未明 | 英 | https://www.aseanbriefing.com/doing-business-guide/singapore/company-establishment/singapore-foreign-ownership-rules | r1 轉引 |
| SG-86 | Can a foreigner own 100% of a Singapore company 2026? | Terra Advisory | 2026 | 英 | https://terraadvisoryservices.com/can-a-foreigner-own-100-of-a-singapore-company/ | r1 轉引 |
| SG-87 | Salary threshold for new EP applicants raised to $5,600 from 2025 | EDB | 2024–2025 | 英 | https://www.edb.gov.sg/en/business-insights/insights/salary-threshold-for-new-employment-pass-applicants-to-be-raised-to-5600-from-2025.html | r1 轉引 |
| SG-88 | New salary requirements for EP applicants from 1 Jan 2025 | EY | 2024–2025 | 英 | https://assets.ey.com/content/dam/ey-sites/ey-com/en_gl/topics/tax/tax-alerts-pdf/ey-singapore-announces-new-salary-requirements-for-employment-pass-applicants-starting-1-january-2025.pdf?download | r1 轉引 |
| SG-89 | Singapore: updated EP eligibility criteria for 2027 | Envoy Global | 2026 | 英 | https://www.envoyglobal.com/news-alert/singapore-updated-employment-pass-eligibility-criteria-for-2027/ | r1 轉引 |
| SG-90 | Average Entry-Level Interior Designer Salary in Singapore | Payscale | 2026 | 英 | https://www.payscale.com/research/SG/Job=Interior_Designer/Salary/5a5b320e/Entry-Level | r1 轉引 |
| SG-91 | Average Mid-Career Interior Designer Salary in Singapore | Payscale | 2026 | 英 | https://www.payscale.com/research/SG/Job=Interior_Designer/Salary/e86615f1/Mid-Career | r1 轉引 |
| SG-92 | Average Experienced Interior Designer Salary in Singapore | Payscale | 2026 | 英 | https://www.payscale.com/research/SG/Job=Interior_Designer/Salary/d834bde3/Experienced-Singapore | r1 轉引 |
| SG-93 | Interior Designer（job posting） | Fuku（Workable） | 約 2026 | 英 | https://apply.workable.com/fuku/jobs/view/6B072C4983.md | r1 轉引 |
| SG-96 | Carpenter project pricing | Dojo Business | 年份未明 | 英 | https://dojobusiness.com/blogs/news/carpenter-project-pricing | r1 轉引 |
| SG-97 | Carpentry Cost Calculator (2026) | SmartCalculator.sg | 2026 | 英 | https://www.smartcalculator.sg/housing/carpentry-cost-calculator | r1 轉引 |
| SG-99 | Castlery Liat Towers flagship store | Home & Decor SG | 年份未明 | 英 | https://www.homeanddecor.com.sg/gallery/accesible-luxury-at-castlerys-flagship-store-at-liat-towers/ | r1 轉引（僅標題） |
| TF-01 | Foreign Exchange Rates – G.5A（Annual） | Federal Reserve Board | 2026 | 英 | https://www.federalreserve.gov/releases/g5a/current/ | r1 轉引 |
| TF-18 | GDP per Capita in Asia (2025) - IMF | Worldometer | 2026 | 英 | https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal | r1 轉引 |
| TF-20 | GDP by Country in Asia (2025) - IMF | Worldometer | 2026 | 英 | https://www.worldometers.info/gdp/gdp-by-country/?region=asia&year=2025&metric=nominal | r1 轉引 |
| TW-13 | 全台住宅平均屋齡創新高 | 經濟日報 | 2025 | 繁中 | https://money.udn.com/money/story/5621/9014283 | r1 轉引 |
| TW-14 | Taiwan housing market: 25.5% decline, nine-year low | 科技新報 | 2026 | 繁中 | https://finance.technews.tw/2026/06/25/taiwan-housing-market-more-houses-built-fewer-buyers-25-5-decline-nine-year-low/ | r1 轉引 |
| TW-19 | 老屋翻新 價格 | PRO360 | 現行 | 繁中 | https://www.pro360.com.tw/price/old_house_renovation | r1 轉引 |
| TW-21 | 20坪 房屋裝潢 價格 | PRO360 | 現行 | 繁中 | https://www.pro360.com.tw/price/20_ping_house_decoration | r1 轉引 |
| TW-22 | 裝潢預算怎麼估？ | vocus 方格子 | 推定 2025 | 繁中 | https://vocus.cc/article/68429352fd897800016a223d | r1 轉引（推定） |
| TW-23 | 裝修市場熱！年產值上看5500億元 | 聯合新聞網 | 2025 | 繁中 | https://udn.com/news/story/7241/9245511 | r1 轉引 |
| TW-26 | 住宅裝修市場規模推估方法之研究 | 內政部建築研究所 | 2000 年代 | 繁中 | https://www.abri.gov.tw/News_Content_Table.aspx?n=807&s=38057 | r1 轉引 |
| TW-30 | 建築管理（100 年統計） | 內政部營建署 | 2011 | 繁中 | https://w3.cpami.gov.tw/statisty/100/100_pdf/06_building/0c_building.pdf | r1 轉引 |
| TW-37 | 內政部預告室內裝修定型化契約應記載事項草案 | 工商時報 | 2024 | 繁中 | https://www.ctee.com.tw/news/20240221701408-430103 | r1 轉引 |
| TW-C2 | 2025 裝潢每坪行情報導（候選出處 TW-16） | 工商時報 | 2025 | 繁中 | https://www.ctee.com.tw/news/20251119700015-431001 | r1 轉引（候選出處，低） |
| TC-04 | Contractor Confidence Rises Amid Strengthening Office Demand Across Asia Pacific | Cushman & Wakefield | 2026 | 英 | https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific | r1 轉引 |
| TD-71 | Enhancement for Active Seniors (EASE) | HDB | 年份未標 | 英 | https://www.hdb.gov.sg/cs/infoweb/residential/living-in-an-hdb-flat/for-our-seniors/ease | r1 轉引 |
| TD-74 | 5 things to know if your home is undergoing HIP | gov.sg | 年份未標 | 英 | https://www.gov.sg/article/5-things-to-know-if-your-home-is-undergoing-hip | r1 轉引 |
| TE-47 | Qanvast Malaysia FAQ | Qanvast | 現行 | 英 | https://qanvast.com/my/faq | r1 轉引 |
| TE-48 | Qanvast About Us（MY） | Qanvast | 現行 | 英 | https://qanvast.com/my/about-us | r1 轉引 |
| TE-25 | Nitori（Brand Wiki） | Lazada Singapore | 2026 | 英 | https://brandwiki.lazada.sg/nitori/ | r1 轉引（低） |
| TE-40 | Interior design startup Livspace cuts staff | Crunchbase News | 2020 | 英 | https://news.crunchbase.com/startups/interior-design-startup-livspace-cuts-staff | r1 轉引 |
| TE-66 | Ikano Retail | Ikano Group | 現行 | 英 | https://group.ikano/stories/ikano-retail/ | r1 轉引 |
| TE-85 | Factory owner Lu opens store prototype in Taiwan | Furniture Today | 2011 | 英 | https://www.furnituretoday.com/business-news/factory-owner-lu-opens-store-prototype-in-taiwan | r1 轉引（低） |
| TE-72 | With Reverse Flip In Cart, Livspace Nets INR 427 Cr From Singapore Parent | Inc42 | 2025 | 英 | https://inc42.com/buzz/exclusive-with-reverse-flip-in-cart-livspace-nets-inr-427-cr-from-singapore-parent/ | r1 轉引 |
| TE-73 | Livspace launches experience centres in Singapore | Inside Retail Asia | 2022 | 英 | https://insideretail.asia/2022/11/29/livspace-launches-experience-centres-in-singapore/ | r1 轉引 |
| TA2-82 | Qanvast（Daniel Lim 專訪） | Vulcan Post | 推測約 2020 | 英 | https://vulcanpost.com/721133/qanvast-match-homeowners-interior-designers-singapore | r1 轉引 |


### 6.2 本輪新增（SG-D 系列）

| # | 標題 | 機構 | 年份 | 語言 | URL | 讀取方式 |
|---|---|---|---|---|---|---|
| SG-D01 | CASE to accredit 500 Renovation Contractors with up to 80 per cent in Subsidies | CASE／CaseTrust | 2025 | 英 | https://www.case.org.sg/casetrust/case-to-accredit-500-renovation-contractors-with-up-to-80-per-cent-in-subsidies-2/ | 搜尋結果內容 |
| SG-D02 | CaseTrust Subsidy Framework for Renovation（24 March 2025） | CASE | 2025 | 英 | https://www.case.org.sg/casetrust/wp-content/uploads/2025/03/CaseTrust-Subsidy-Framework-for-Renovation-24-March-2025.pdf | 搜尋結果內容 |
| SG-D03 | CaseTrust Accreditation for Renovation Businesses（Updated） | CASE | 2026 | 英 | https://www.case.org.sg/casetrust/wp-content/uploads/2026/03/CaseTrust-Accreditation-for-Renovation-Businesses-Updated.pdf | 搜尋結果內容 |
| SG-D04 | About HomeMatch | CB Insights | 年份未明 | 英 | https://www.cbinsights.com/company/homematch | 搜尋結果內容 |
| SG-D05 | Almost S$2 million lost in prepayments by S'pore customers | Mothership | 2025 | 英 | https://mothership.sg/2025/02/spore-customers-money-lost-businesses-closed/ | 搜尋結果內容（標題層級佐證） |
| SG-D06 | Construction sector requirements（levy table） | MOM | 現行（2026 檢視） | 英 | https://www.mom.gov.sg/maintenance/passes-and-permits/work-permit-for-foreign-worker/sector-specific-rules/construction-sector-requirements/ | 搜尋結果內容 |
| SG-D07 | Foreign Worker Levy in Singapore: Rates & How to Calculate | Singapore Business Owners（sbo.sg） | 2026 | 英 | https://sbo.sg/business/hr-payroll/foreign-worker-levy-singapore-rates-how-to-calculate/ | 搜尋結果內容（推定） |
| SG-D08 | Foreign Worker Levy (FWL) Singapore 2026 | Raffles Corporate Services | 2026 | 英 | https://rafflescorporateservices.com/foreign-worker-levy-fwl-singapore-2026-rates-calculation-employer-obligations/ | 搜尋結果內容（推定） |
| SG-D09 | Upcoming changes to S Pass eligibility | MOM | 2025 | 英 | https://www.mom.gov.sg/maintenance/passes-and-permits/s-pass/upcoming-changes-to-s-pass-eligibility | 搜尋結果內容 |
| SG-D10 | COS 2025 factsheet on foreign workforce policies | MOM | 2025 | 英 | https://www.iac.gov.sg/-/media/mom/documents/budget2025/cos-2025-factsheet-on-foreign-workforce-policies.pdf | 搜尋結果內容 |
| SG-D11 | Singapore: changes to S Pass eligibility and levy rates | Envoy Global | 2025 | 英 | https://www.envoyglobal.com/news-alert/singapore-changes-to-s-pass-eligibility-and-levy-rates | 搜尋結果內容（推定） |
| SG-D12 | Flash alert fa26-059 | KPMG | 2026 | 英 | https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2026/03/fa26-059.pdf.coredownload.pdf | 搜尋結果內容（表格截斷） |
| SG-D13 | 新加坡室内装修相关投诉每年有这么多！ | 網易號（轉述國會答覆） | 2024 | 簡中 | https://www.163.com/dy/article/J9O371G305148HD5.html | 搜尋結果內容 |
| SG-D14 | 3装修公司是同一人 18屋主付181万 工程烂尾 | 中國報（柔佛） | 2022 | 簡中 | https://johor.chinapress.com.my/20220414/3%E8%A3%85%E4%BF%AE%E5%85%AC%E5%8F%B8%E6%98%AF%E5%90%8C%E4%B8%80%E4%BA%BA-18%E5%B1%8B%E4%B8%BB%E4%BB%98181%E4%B8%87-%E5%B7%A5%E7%A8%8B%E7%83%82%E5%B0%BE/ | 搜尋結果內容 |
| SG-D15 | Man arrested for series of renovation scams（20231018） | Singapore Police Force | 2023 | 英 | https://www.police.gov.sg/Media-Hub/News/2023/20231018_man_arrested_for_series_of_renovation_scams | 搜尋結果內容 |
| SG-D16 | Man to be charged for cheating（20260814） | Singapore Police Force | 2026 | 英 | https://www.police.gov.sg/Media-Hub/News/2026/08/20260814_man_to_be_charged_for_cheating | 搜尋結果內容 |
| SG-D17 | Man to be charged for cheating（20260717） | Singapore Police Force | 2026 | 英 | https://www.police.gov.sg/Media-Hub/News/2026/07/20260717_man_to_be_charged_for_cheating | 搜尋結果內容 |
| SG-D18 | Interior designer arrested in Singapore for allegedly pocketing client's money in direct payment scheme | The Star | 2026 | 英 | https://www.thestar.com.my/aseanplus/aseanplus-news/2026/08/15/interior-designer-arrested-in-singapore-for-allegedly-pocketing-clients-money-in-direct-payment-scheme | 搜尋結果內容 |
| SG-D19 | Man Arrested For Series Of Renovation Scams（20200717） | Singapore Police Force | 2020 | 英 | https://www.police.gov.sg/Media-Room/News/20200717_Man-Arrested-For-Series-Of-Renovation-Scams | 搜尋結果內容 |
| SG-D20 | Written reply to PQ on whether there is an increase in renovation contractors who take deposits without intent to carry out renovation works | Ministry of Home Affairs | 約 2022 | 英 | https://www.mha.gov.sg/media-room/newsroom/written-reply-to-pq-on-whether-there-is-an-increase-in-renovation-contractors-who-take-deposits-without-intent-to-carry-out-renovation-works/ | 搜尋結果內容 |
| SG-D21 | Finding the right SSIC code | ACRA | 現行 | 英 | https://www.acra.gov.sg/register/business/choosing-reserving-a-business-name/finding-the-right-ssic-code/ | 搜尋結果內容 |
| SG-D22 | AN INTERIOR DESIGN SOLUTIONS（company record） | OpenGovSG | 現行 | 英 | https://opengovsg.com/corporate/53100921A | 搜尋結果內容 |
| SG-D23 | SSIC Codes Singapore: Full 2026 List & Guide | Sleek | 2026 | 英 | https://sleek.com/sg/resources/ssic-codes-guide/ | 搜尋結果內容（推定） |
| SG-D24 | Categories & Benefits（members） | IDCS | 現行 | 英 | https://idcs.sg/members | 搜尋結果內容 |
| SG-D25 | Speech by MOS Low Yen Ling at the Launch of the Singapore Interior Design Accreditation Programme | MTI | 2021 | 英 | https://www.mti.gov.sg/Newsroom/Speeches/2021/11/Speech-by-MOS-Low-Yen-Ling-at-the-Launch-of-the-Singapore-Interior-Design-Accreditation-Programme | 搜尋結果內容 |
| SG-D26 | Do we need accreditation for Singapore's IDs? The Society of Interior Designers says yes | Home & Decor SG | 約 2017–2021 | 英 | https://www.homeanddecor.com.sg/design/accreditation-initiative-interior-designers-society-of-interior-designers-singapore | 搜尋結果內容 |
| SG-D27 | Singapore Launches Accreditation Scheme for Interior Designers | ADD Directory | 2021 | 英 | https://add.directory/?p=5451 | 搜尋結果內容 |
| SG-D28 | Directory of Renovation Contractors (DRC) | HDB | 現行 | 英 | https://www.hdb.gov.sg/cs/infoweb/business/renovation-contractors/renovation/directory-of-renovation-contractors-drc | 搜尋結果內容 |
| SG-D29 | Written answer by MND on measures against errant contractors who dispose of renovation debris in new HDB BTO projects | MND | 2023 | 英 | https://mnd.gov.sg/newsroom/speeches/view/written-answer-by-ministry-of-national-development-on-measures-against-errant-contractors-who-dispose-of-renovation-debris-and-refuse-indiscriminately-in-new-hdb-bto-projects | 搜尋結果內容 |
| SG-D30 | Written answer by MND on complaints received against HDB accredited or registered renovation contractors | MND | 約 2022 | 英 | https://mnd.gov.sg/newsroom/speeches/view/written-answer-by-ministry-of-national-development-on-complaints-received-against-hdb-accredited-or-registered-renovation-contractors | 搜尋結果內容（推定） |
| SG-D31 | Written answer by MND on renovation contractors penalised for improper disposal of renovation debris in past five years | MND | 2023 | 英 | https://www.mnd.gov.sg/newsroom/speeches/view/written-answer-by-ministry-of-national-development-on-data-on-renovation-contractors-penalised-for-improper-disposal-of-renovation-debris-on-common-property-in-hdb-estate-in-past-five-years | 搜尋結果內容 |
| SG-D32 | Renovation budget planning complete guide Singapore | Homejourney | 2025 | 英 | https://www.homejourney.sg/blog/homejourney-renovation-budget-planning-complete-guide-singapore-202512301900 | 搜尋結果內容 |
| SG-D33 | Condo Renovation Cost & Financing Guide in Singapore (2026) | MoneySmart | 2026 | 英 | https://www.moneysmart.sg/personal-loan/condo-renovation-cost-loan-guide-singapore-ms | 搜尋結果內容 |
| SG-D34 | Cost Guide for Kitchen, Bathroom, Living Room Renovations (2026) | MoneySmart | 2026 | 英 | https://blog.moneysmart.sg/renovation-loans/kitchen-bathroom-living-room-renovation-cost-singapore/ | 搜尋結果內容 |
| SG-D35 | HDB renovation cost | ShopBack | 2026 | 英 | https://www.shopback.sg/blog/finance/hdb-renovation-cost | 搜尋結果內容 |
| SG-D36 | Renovation Design in Singapore: What It Should Cost, and Why | Megafurniture | 約 2026 | 英 | https://megafurniture.sg/apps/aeo/ai/md/default/articles/743086850163.md | 搜尋結果內容 |
| SG-D37 | 新加坡 8 大室内设计与装修公司 2026 | MissLobang | 2026 | 簡中 | https://www.misslobang.com/zh/article/best-interior-design-renovation-firms-singapore-2026 | 搜尋結果內容（推定） |
| SG-D38 | HDB Renovation Cost Singapore 2026: Full Breakdown by Flat Type | SmartCalculator.sg | 2026 | 英 | https://www.smartcalculator.sg/articles/hdb-renovation-cost-singapore-2026 | 搜尋結果內容（推定；另見 MoneySmart HDB 指南） |
| SG-D39 | 4-Room Resale HDB Flat Renovations: From $33K to $180K | Qanvast | 年份未明 | 英 | https://qanvast.com/amp/sg/articles/4-room-resale-hdb-flat-renovations-from-sgd33k-to-sgd180k-2661 | 搜尋結果內容（僅標題） |
| SG-D40 | 2025 年 HDB 转售市场表现如何，这对 2026 年价格意味着什么 | Stacked Homes（中文版） | 2026 | 簡中 | https://stackedhomes.com/zh/hdb-resale-market-review-outlook-2026/ | 搜尋結果內容（僅標題） |
| SG-D41 | Expanded housing supply drives a healthier reset in the HDB resale market | EdgeProp SG | 2026 | 英 | https://edgeprop.sg/property-news/expanded-housing-supply-drives-healthier-reset-hdb-resale-market | 搜尋結果內容（推定） |
| SG-D42 | HDB Market Outlook 2026 | OrangeTee | 2025 | 英 | https://www.orangetee.com/ResearchHubFiles/Items/582/20251120141338-7bea9593HDB Market Outlook 2026_final.pdf | 搜尋結果內容（推定） |
| SG-D43 | HDB Outlook 2026 | Huttons | 2025–2026 | 英 | https://www.huttonsgroup.com/wp-content/uploads/HDB-Outlook-2026-Generic.pdf | 搜尋結果內容（推定） |
| SG-D44 | 1Q 2026 HDB Quarterly Report | ERA Singapore | 2026 | 英 | https://www.era.com.sg/research-articles/1q-2026-hdb-quarterly-report | 搜尋結果內容 |
| SG-D45 | 2Q 2026 HDB Quarterly Report | ERA Singapore | 2026 | 英 | https://www.era.com.sg/research-articles/2q-2026-hdb-quarterly-report | 搜尋結果內容 |
| SG-D46 | Commentary on 2Q 2026 HDB Flash Estimates | ERA Singapore | 2026 | 英 | https://www.era.com.sg/press-release/commentary-on-2q-2026-hdb-flash-estimates | 搜尋結果內容 |
| SG-D47 | Q2 2026 HDB Quarter Report | OrangeTee | 2026 | 英 | https://www.orangetee.com/ResearchHubFiles/Items/783/20260706112727-4465dab4Q2 2026 HDB Quarter Report.pdf | 搜尋結果內容 |
| SG-D48 | 2Q 2026 URA Quarterly Report: Resale Transactions Rebound | ERA Singapore | 2026 | 英 | https://www.era.com.sg/press-release/2q-2026-ura-real-estate-statistics-resale-transactions-volume-rebound-increase-due-to-fewer-new-launches | 搜尋結果內容 |
| SG-D49 | HDB resale prices fall for second consecutive quarter（2Q2026） | EdgeProp SG | 2026 | 英 | https://www.edgeprop.sg/amp/property-news/hdb-resale-prices-fall-second-consecutive-quarter-down-03-2q2026 | 搜尋結果內容（推定） |
| SG-D50 | HDB resale price index drops by 0.1% q-o-q in 1Q2026 | EdgeProp SG | 2026 | 英 | https://www.edgeprop.sg/property-news/hdb-resale-price-index-drops-01-q-o-q-1q2026-first-time-seven-years-hdb-flash-estimates | 搜尋結果內容 |
| SG-D51 | Singapore's February BTO launch to feature 1,300 flats with faster completion times | Malay Mail | 2026 | 英 | https://www.malaymail.com/amp/news/singapore/2026/01/31/singapores-february-bto-launch-to-feature-1300-flats-with-faster-completion-times-under-three-years/207497 | 搜尋結果內容（標題） |
| SG-D52 | Making our Homes and Neighbourhoods Safer for Seniors | MND | 2024 | 英 | https://mnd.gov.sg/newsroom/speeches/view/making-our-homes-and-neighbourhoods-safer-for-seniors | 搜尋結果內容（推定） |
| SG-D53 | HDB EASE Programme: Upgrades for seniors from $125–$312 | Home & Decor SG | 約 2024 | 英 | https://www.homeanddecor.com.sg/property/hdb/ease-programme-upgrading | 搜尋結果內容 |
| SG-D54 | Guide to government subsidies under HDB EASE | Dollars and Sense | 年份未明 | 英 | https://dollarsandsense.sg/guide-government-subsidies-slip-resistant-tiles-grab-bars-ramps-hdb-enhancement-active-seniors-ease-programme/ | 搜尋結果內容 |
| SG-D55 | Written answer by MND on senior-friendly features in mature HDB estates and EASE 2.0 | MND | 2024–2025 | 英 | https://mnd.gov.sg/newsroom/speeches/view/written-answer-by-ministry-of-national-development-on-plans-to-build-more-senior-friendly-features-in-mature-hdb-estates-and-access-to-additional-benefits-under-ease-2.0 | 搜尋結果內容 |
| SG-D56 | 18,000 more homes to be upgraded under HDB Home Improvement Programme | HDB（HDB Pulse） | 2026 | 英 | https://www.hdb.gov.sg/hdb-pulse/news/2026/18000-more-homes-to-be-upgraded-under-hdb-home-improvement-programme | 搜尋結果內容（標題與日期） |
| SG-D57 | Annex C（HIP 2026） | HDB | 2026 | 英 | https://www.hdb.gov.sg/-/media/hdb-pulse/news/2026/18000-more-homes-to-be-upgraded-under-hdb-home-improvement-programme/Annex-C.pdf | 搜尋結果內容（標題） |
| SG-D58 | Over 18,000 HDB flats selected for upgrading under HIP with over S$253 million set aside | The Independent SG | 2026 | 英 | https://theindependent.sg/over-18-000-hdb-flats-are-selected-for-upgrading-under-hip-with-over-s-253-million-set-aside/ | 搜尋結果內容 |
| SG-D59 | 18000 flats in 12 neighbourhoods to be upgraded under HIP | cos.sg | 2026 | 英 | https://cos.sg/18000-flats-in-12-neighbourhoods-to-be-upgraded-under-home-improvement-programme/ | 搜尋結果內容（推定） |
| SG-D60 | HDB Home Improvement Programme (HIP): Cost and Subsidy Guide 2026 | The Money Bees | 2026 | 英 | https://themoneybees.co/blog/home-improvement-programme-hdb-hip | 搜尋結果內容（推定） |
| SG-D61 | Committee of Supply 2025 | MND | 2025 | 英 | https://www.mnd.gov.sg/cos-2025 | 搜尋結果內容（推定） |
| SG-D62 | Exclusive: Livspace Parent Infuses INR 362 Cr Into Indian Arm | Inc42 | 2025 | 英 | https://inc42.com/buzz/exclusive-livspace-parent-infuses-inr-362-cr-into-indian-arm/ | 搜尋結果內容 |
| SG-D63 | Livspace（company news page） | Inc42 | 2026 | 英 | https://inc42.com/company/livspace/latest/ | 搜尋結果內容（僅標題） |
| SG-D64 | Livspace CEO change, IPO plans announced | Techleap Finder | 2025 | 英 | https://finder.techleap.nl/news/feed/livspace-ceo-change-ipo-plans-announced | 搜尋結果內容（推定） |
| SG-D65 | Retail 2025 | Ikano Group | 2025 | 英 | https://group.ikano/stories/retail-2025/ | 搜尋結果內容 |
| SG-D66 | 11,700 firms supported by EnterpriseSG in 2025 amid tariffs and disruptions | Enterprise Singapore | 2026 | 英 | https://www.enterprisesg.gov.sg/resources/media-centre/news/2026/january/11700-firms-supported-by-enterprisesg-in-2025-amid-tariffs-and-disruptions | 搜尋結果內容 |
| SG-D67 | Speech by MOS Low Yen Ling at the Opening of Castlery's Flagship Store | MTI | 2022 | 英 | https://mti.gov.sg/Newsroom/Speeches/2022/10/Speech-by-MOS-Low-Yen-Ling-at-the-Castlery-and-Launch-of-the-Retail-ITM-2025 | 搜尋結果內容 |
| SG-D68 | Courts Asia 9M losses widen to $5.4 mil | The Edge Singapore | 年份未明 | 英 | https://alfi.dev.theedgesingapore.com/capital/results/courts-asia-9m-losses-widen-54-mil | 搜尋結果內容 |
| SG-D69 | Steady construction demand in 2026 as Singapore steps up support for built environment firms | BCA | 2026 | 英 | https://www1.bca.gov.sg/resources/newsroom/steady-construction-demand-in-2026-as-singapore-steps-up-support-for-built-environment-firms-through-collaboration-and-innovation/ | 搜尋結果內容 |
| SG-D70 | Commercial and infrastructure works to drive Singapore's $47 bil – $53 bil construction pipeline in 2026 | EdgeProp SG | 2026 | 英 | https://www.edgeprop.sg/property-news/commercial-and-infrastructure-works-drive-singapores-47-bil--53-bil-construction-pipeline-2026 | 搜尋結果內容 |
| SG-D71 | free_stats（building materials market prices） | Department of Statistics Singapore | 2026 | 英 | https://isomer-user-content.by.gov.sg/338/81b0abeb-5972-4324-823d-a5ee9516abdc/free_stats.pdf | 搜尋結果內容（推定） |
| SG-D72 | Singapore's stability hides a tightening market | Turner & Townsend | 2026 | 英 | https://www.turnerandtownsend.com/insights/singapores-stability-hides-a-tightening-market/ | 搜尋結果內容 |
| SG-D73 | Notizie dal mondo 305461（轉述 CNA） | ICE（義大利貿易推廣局） | 2026 | 義／英 | https://www.ice.it/it/news/notizie-dal-mondo/305461 | 搜尋結果內容（推定） |
| SG-D74 | Written answer by MND on approvals granted for renovation works and environmental impact measures | MND | 年份未明 | 英 | https://mnd.gov.sg/newsroom/speeches/view/written-answer-by-ministry-of-national-development-on-approvals-granted-for-renovation-works-and-environmental-impact-measures-introduced | 搜尋結果內容 |
| SG-D75 | Building works not requiring approval | BCA | 現行 | 英 | https://www1.bca.gov.sg/guidelines-and-requirements/building-works-not-requiring-approval/ | 搜尋結果內容 |
| SG-D76 | Condo Renovation Approvals: Owner, MCST or BCA? | Little Big Red Dot | 2026 | 英 | https://littlebigreddot.com/condo-renovation-approvals-singapore/ | 搜尋結果內容 |
| SG-D77 | Singapore Home Renovation Guide 2026 | Lovelyhomes | 2026 | 英 | https://lovelyhomes.com.sg/singapore-home-renovation-guide-2026/ | 搜尋結果內容 |
| SG-D78 | NDIMS 2021/2022 Summary Report | DesignSingapore Council | 2023（2025 上傳） | 英 | https://designsingapore.org/wp-content/uploads/2025/02/NDIMS-2021_2022-Summary-Report.pdf | 搜尋結果內容 |
| SG-D79 | Singapore's design workforce to grow 25% | DesignSingapore Council | 2023 | 英 | https://designsingapore.org/news/singapores-design-workforce-to-grow-25-demand-driven-by-non-design-sectors/ | 搜尋結果內容 |
| SG-D80 | Population in Brief 2025: Key Trends | 國家人口及人才署（population.gov.sg） | 2025 | 英 | https://www.population.gov.sg/population-in-brief-2025-key-trends/ | 搜尋結果內容 |
| SG-D81 | Population and Population Structure – Latest Data | SingStat | 2025 | 英 | https://www.singstat.gov.sg/find-data/explore-data-themes/population/population-and-population-structure/latest-news-data | 搜尋結果內容 |
| SG-D82 | National Accounts – Latest Data | SingStat | 2026 | 英 | https://www.singstat.gov.sg/find-data/explore-data-themes/economy-prices/national-accounts/latest-news-data | 搜尋結果內容 |
| SG-D83 | Annual Economic Survey of Singapore 2025（Full Report） | MTI | 2026 | 英 | https://isomer-user-content.by.gov.sg/166/16f78938-9d69-4df0-87a2-c6e6b0376da6/FullReport_AES2025.pdf | 搜尋結果內容 |
| SG-D84 | Singaporeans spending too much on home renovation and complaints against the industry increases | Home & Decor SG | 推定 2024 | 英 | https://www.homeanddecor.com.sg/design/news/singaporeans-spending-too-much-on-home-renovation-and-complaints-against-the-industry-increases | 搜尋結果內容 |
| SG-D85 | HDB flat owner wins High Court case against contractor that shuttered firm before resolving dispute | Singapore Law Watch | 年份未明 | 英 | https://singaporelawwatch.sg/Headlines/HDB-flat-owner-wins-High-Court-case-against-contractor-that-shuttered-firm-before-resolving-dispute | 搜尋結果內容 |
| SG-D86 | What Licenses Should A Renovation Contractor In Singapore Have? | CompanyFiler | 年份未明 | 英 | https://www.companyfiler.com/what-licenses-should-a-renovation-contractor-in-singapore-have/ | 搜尋結果內容（推定） |
| SG-D87 | CaseTrust Renovation Singapore: What It Means for Homeowners | Handshake Finance | 2026 | 英 | https://handshake.finance/casetrust-renovation-singapore/ | 搜尋結果內容（推定） |
| SG-D88 | Celebrating Excellence: HomeRenoGuru top interior design firms of 2023 | HomeRenoGuru | 2023 | 英 | https://www.homerenoguru.sg/articles/design-trends/celebrating-excellence-homerenoguru-sgs-top-interior-design-firms-of-2023 | 搜尋結果內容 |
| SG-D89 | MET Interior（業者頁） | Hometrust | 現行 | 英 | https://hometrust.sg/interior-designers/met-interior | 搜尋結果內容 |
| SG-D90 | Ikano Retail FY2024 turnover（新聞） | The Sun（馬來西亞） | 2024 | 英 | https://thesun.my/?p=204984 | 搜尋結果內容（推定） |

---

## 7. 附錄：關鍵指標表（CSV）

```csv
market,metric,value,unit,year,source_id,source_url,definition,confidence
SG,名目 GDP,789529.2,SGD million,2025,SG-D82,https://www.singstat.gov.sg/find-data/explore-data-themes/economy-prices/national-accounts/latest-news-data,SingStat 當期市價 GDP；2024 年 765497.5；＝6043 億 USD【實際】,high
SG,總人口,6111.2,thousand persons,2025-06,SG-D81,https://www.singstat.gov.sg/find-data/explore-data-themes/population/population-and-population-structure/latest-news-data,含居民 420 萬與非居民 191 萬；年增 1.2%【實際】,high
SG,公民 65 歲以上占比,20.7,%,2025-06,SG-D80,https://www.population.gov.sg/population-in-brief-2025-key-trends/,公民口徑；2015 年 13.1%【實際】,high
SG,營建需求（預估）,47000-53000,SGD million,2026,SG-D69,https://www1.bca.gov.sg/resources/newsroom/steady-construction-demand-in-2026-as-singapore-steps-up-support-for-built-environment-firms-through-collaboration-and-innovation/,BCA construction demand；2025 初值 50500；私人住宅 5000-5500；公共住宅 6200-6800；以新建為主【實際】官方預估,high
SG,營建需求年均（預測）,39000-46000,SGD million per year,2027-2030,SG-D69,https://www1.bca.gov.sg/resources/newsroom/steady-construction-demand-in-2026-as-singapore-steps-up-support-for-built-environment-firms-through-collaboration-and-innovation/,BCA 中期預測【示意】,medium
SG,住宅翻修示意規模（僅 HDB 新入住）,2810-3310,SGD million per year,2025-2026,本研究,—,HDB 轉售 26169×S$70000-81600＋BTO 19600（低信心）×S$50000-60000；假設全數翻修【示意】,low
SG,住宅翻修示意規模（含私宅轉售與新售）,4430-4930,SGD million per year,2025-2026,本研究,—,情境 A 加私宅轉售 14622×S$82000 與新售 10815×S$39000【示意】上限式,low
SG,人均住宅翻修支出（示意）,352-617,USD per capita,2025-2026,本研究,—,情境 A 至 C÷611.12 萬人÷1.3065【示意】,low
SG,住宅翻修占 GDP（示意）,0.36-0.62,% of GDP,2025-2026,本研究,—,情境 A 至 C÷S$7895 億【示意】,low
SG,HDB 轉售成交量,26169,筆,2025,SG-20,https://edgeprop.sg/property-news/hdb-resale-price-growth-slows-million-dollar-flats-prices-gain-23-4q2025,HDB 全年轉售；2024 年 28986【實際】,high
SG,HDB 轉售成交量（上半年）,12533,筆,2026H1,SG-D46,https://www.era.com.sg/press-release/commentary-on-2q-2026-hdb-flash-estimates,ERA 依 HDB 快報；較 1H2025 的 13692 減 8.3%；ERA 季報另為 12681【實際】,medium
SG,達 MOP 組屋戶數,13480,戶,2026,SG-D41,https://edgeprop.sg/property-news/expanded-housing-supply-drives-healthier-reset-hdb-resale-market,屆滿 5 年最低居住年限；2025 年 6973；對應推定【實際】,medium
SG,達 MOP 組屋戶數（三年合計）,53816,戶,2026-2028,SG-D42,https://www.orangetee.com/ResearchHubFiles/Items/582/20251120141338-7bea9593HDB Market Outlook 2026_final.pdf,2023-2025 為 37474（+56.1%）；對應推定【示意】,medium
SG,私宅轉售成交量,14622,筆,2025,SG-71,https://www.era.com.sg/press-release/4q-2025-ura-real-estate-statistics-private-home-demand-momentum-carries-from-3q-2025-sets-firm-outlook-for-2026,URA 最終值；占私宅成交 26492 的 55.2%【實際】,high
SG,4 房 BTO 翻修費,50000-60000,SGD per flat,2026,SG-13,https://qanvast.com/sg/articles/what-are-the-expected-renovation-costs-for-hdb-flats-in-2026-3568,Qanvast 2025 中位數＋1-2%；＝38270-45924 USD【示意】,medium
SG,4 房轉售組屋翻修費,70000-81600,SGD per flat,2026,SG-13,https://qanvast.com/sg/articles/what-are-the-expected-renovation-costs-for-hdb-flats-in-2026-3568,Qanvast 預估；＝53578-62457 USD【示意】,medium
SG,設計師主導翻修費（4 房）,80000-140000,SGD per flat,2026,SG-D35,https://www.shopback.sg/blog/finance/hdb-renovation-cost,ID 主導、BTO 或轉售皆適用之高階區間【示意】,low
SG,4 房轉售每 m² 翻修單價（示意）,778-907,SGD per m2,2026,SG-13,https://qanvast.com/sg/articles/what-are-the-expected-renovation-costs-for-hdb-flats-in-2026-3568,每戶價÷90 m²（90 m² 為搜尋彙整基準）；＝595-694 USD/m²＝61335-71499 TWD/坪【示意】,low
SG,每 m² 單價÷人均 GDP（4 房轉售）,0.60-0.70,%,2026,SG-13;TF-18,https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal,USD/m²÷99365；台灣中古屋同口徑 2.46-3.69%【示意】,low
SG,CASE 裝修承包商投訴,962,件,2024,SG-01,https://www.case.org.sg/wp-content/uploads/2025/02/Media-Release-CASE-sees-prepayment-losses-more-than-quadruple-in-2024-entertainment-related-complaints-nearly-triple.pdf,約 97% 針對非 CaseTrust 業者；全行業第 4【實際】,high
SG,CASE 裝修承包商投訴,1454,件,2022,SG-D84,https://www.homeanddecor.com.sg/design/news/singaporeans-spending-too-much-on-home-renovation-and-complaints-against-the-industry-increases,媒體轉述 CASE；2021 年 1300、2023 年 1168【實際】,medium
SG,裝修業預付款損失,728000,SGD,2024,SG-02,https://www.asiaone.com/singapore/home-renovations-make-bulk-consumers-losses-2024-case,全行業 S$1.93m 中裝修部分（37.7%）【實際】,medium
SG,警方調查不良裝修承包商案件,100,宗,2019-2021,SG-D20,https://www.mha.gov.sg/media-room/newsroom/written-reply-to-pq-on-whether-there-is-an-increase-in-renovation-contractors-who-take-deposits-without-intent-to-carry-out-renovation-works/,MHA 書面答覆；72% 已起訴【實際】,medium
SG,單一裝修詐騙案損失,100000,SGD（逾）,2026,SG-D16,https://www.police.gov.sg/Media-Hub/News/2026/08/20260814_man_to_be_charged_for_cheating,51 歲室內設計師以私下付款折扣為誘餌；警方估計逾 S$10 萬【實際】,high
SG,CaseTrust 認證補貼目標家數,500,家,2025-2028,SG-D01,https://www.case.org.sg/casetrust/case-to-accredit-500-renovation-contractors-with-up-to-80-per-cent-in-subsidies-2/,CASE 計畫目標；銀級首年認證費最高補 80%；達成數無資料【實際】,medium
SG,CaseTrust 認證補貼上限,5280,SGD per business,2025-2028,SG-D02,https://www.case.org.sg/casetrust/wp-content/uploads/2025/03/CaseTrust-Subsidy-Framework-for-Renovation-24-March-2025.pdf,申請費＋顧問費；顧問費補 80% 上限 S$1200【實際】,medium
SG,CaseTrust 裝修訂金上限,20,% of contract,現行,SG-06,https://www.case.org.sg/casetrust/casetrust-accreditation-for-renovation-businesses/,協會認證（非法定）；另須訂金履約保證【實際】,high
SG,DRC 除名門檻,24,demerit points within 24 months,現行,SG-D28,https://www.hdb.gov.sg/cs/infoweb/business/renovation-contractors/renovation/directory-of-renovation-contractors-drc,HDB 承包商名錄記點；重大違規可直接取消資格【實際】,high
SG,ACRA 登記裝修承包商家數,6697,家,2022-04,SG-04,https://www.mti.gov.sg/Newsroom/Parliamentary-Replies/2022/07/Written-reply-to-PQ-on-renovation-contractors,最新官方家數；非專指 ID；÷2025 人口＝10.96 家/萬人【實際】,medium
SG,營建業基本技術工外勞稅,700,SGD per month,現行,SG-D06,https://www.mom.gov.sg/maintenance/passes-and-permits/work-permit-for-foreign-worker/sector-specific-rules/construction-sector-requirements/,馬來西亞/NAS/PRC 來源；高技術 300；NTS 基本 900；off-site 250/370【實際】,high
SG,S Pass 月薪門檻（新申請）,3300,SGD per month,2025-09-01起,SG-D09,https://www.mom.gov.sg/maintenance/passes-and-permits/s-pass/upcoming-changes-to-s-pass-eligibility,金融業 3800；隨年齡遞增至 4800；基本級外勞稅 S$650【實際】,high
SG,EP 月薪門檻（新申請，非金融業）,5600,SGD per month,2025-01-01起,SG-87,https://www.edb.gov.sg/en/business-insights/insights/salary-threshold-for-new-employment-pass-applicants-to-be-raised-to-5600-from-2025.html,另須 COMPASS 40 分；＝133587 TWD【實際】,high
SG,營建業外籍勞工依存比上限,83.3,%,現行,SG-34,https://www.mom.gov.sg/passes-and-permits/work-permit-for-foreign-worker/foreign-worker-levy/what-is-the-foreign-worker-levy,MOM 官方【實際】,medium
SG,設計師月薪中位數（全體設計職類）,6000,SGD per month,2022,SG-D78,https://designsingapore.org/wp-content/uploads/2025/02/NDIMS-2021_2022-Summary-Report.pdf,NDIMS 調查；非室內設計專屬【實際】,medium
SG,HIP 2026 輪撥款,253,SGD million,2026,SG-D58,https://theindependent.sg/over-18-000-hdb-flats-are-selected-for-upgrading-under-hip-with-over-s-253-million-set-aside/,逾 18000 戶、12 市鎮、198 座；每戶約 S$14056【實際】,medium
SG,HIP 2025 輪撥款,407,SGD million,2025,SG-29,https://edgeprop.sg/amp/property-news/over-29000-hdb-flats-selected-407-mil-upgrading,約 29000 戶以上；1997 年以前建成【實際】,medium
SG,EASE（私宅）補貼上限,1200,SGD per household,2026-2028,SG-31,https://www.mnd.gov.sg/newsroom/speeches/view/enhancement-for-active-seniors-(private-housing)-programme,補 75%；限有長者之公民私宅家戶【實際】,medium
SG,辦公 fit-out 平均成本,140,USD per sq ft,2026,TC-04,https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific,C&W 2026 版（價格基準 2025-12）；台北 145【實際】,high
SG,營建成本通膨,1,%,2025,SG-D72,https://www.turnerandtownsend.com/insights/singapores-stability-hides-a-tightening-market/,Turner & Townsend；預估 2026 約 4%、2027 5%【實際】,medium
SG,預拌混凝土價格,140.00,SGD per m3,2026-03,SG-D71,https://isomer-user-content.by.gov.sg/338/81b0abeb-5972-4324-823d-a5ee9516abdc/free_stats.pdf,統計局建材市價（初值）；2025-12 為 129.50；對應推定【實際】,medium
SG,Hafary 營收,286.991,SGD million,FY2025,SG-37,https://links.sgx.com/1.0.0/corporate-announcements/0D6QYQB30LNU0IC8/874465_HHL%20Interim%20FS%20-%20FY2025%20Final.pdf,SGX 公告；毛利率 41.1%【實際】,high
SG,IKEA Singapore 營業額,384.2,SGD million,FY2023,SG-83,https://www.ikea.com/sg/en/newsroom/corporate-news/ikano-retail-owner-of-ikea-singapore-posts-eur-1-08-billion-in-total-turnover-pub3bd2f4e0,Ikano 新聞稿；FY2024-25 新加坡無資料【實際】,high
SG,Castlery 美國營收占比,70,% of global revenue,2025-2026,SG-D66,https://www.enterprisesg.gov.sg/resources/media-centre/news/2026/january/11700-firms-supported-by-enterprisesg-in-2025-amid-tariffs-and-disruptions,EnterpriseSG 轉述；美國關稅增加成本壓力【實際】,medium
SG,Livspace 新加坡母公司對印度實體注資,362,INR crore,2025,SG-D62,https://inc42.com/buzz/exclusive-livspace-parent-infuses-inr-362-cr-into-indian-arm/,reverse flip 程序；前一筆 427 crore（TE-72）；新加坡營運現況無資料【實際】,medium
SG,設計費占工程費比,無資料,%,—,SG-61,https://megafurniture.sg/blogs/articles/renovation-design-cost-singapore,收費方式：百分比、固定包價、併入木作加價；百分比無資料,—
SG,平台滲透率,無資料,%,—,—,—,Qanvast 三國累計服務逾 7 萬屋主（TE-47）屬累計數不可換算,—
```
