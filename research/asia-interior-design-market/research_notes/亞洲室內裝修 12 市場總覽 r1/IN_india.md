# 印度（India）住宅室內裝修與翻修市場：r1 獨立三角驗證筆記

- 市場層級：第三層（新興市場），以台灣為基準線
- 研究日期：2026-10-09（現況以 2024–2026 為準；印度會計年度 FY 為 4 月至隔年 3 月，例如 FY25 = 2024-04-01～2025-03-31）
- 撰寫語言：繁體中文（台灣用語）；機構、公司與法規名稱以括號保留原文
- 單位換算（只換算數量級，不換算幣別）：1 lakh = 100,000（10 萬）；1 crore = 10,000,000（1,000 萬）；1 lakh crore = 10^12（1 兆）。例如 ₹1,460 crore = ₹146 億盧比；₹6 lakh crore = ₹6 兆盧比；₹12 lakh = ₹120 萬盧比
- 幣別與面積單位都保留來源原樣（INR、USD、₹/sq ft），不換算成其他幣別，也不把 sq ft 換算成 m²（統一由中央處理）
- 所有來源的讀取方式都是「搜尋結果內容」：WebFetch 在本環境被網路政策封鎖，因此沒有開啟任何原始頁面全文
- 獨立性：本輪沒有讀取 04-research-notes/ 或 05-report/ 下的任何檔案

---

## 0. 搜尋紀錄摘要

| 項目 | 數值 |
|---|---|
| 嘗試的 WebSearch 次數 | 20 次 |
| 成功執行的次數 | 16 次（其中 4 次用 extended 模式） |
| 未執行的次數 | 4 次。原因是整輪共用的 WebSearch 額度（每輪 200 次，所有代理共用）已用完。依工具指示，沒有用其他方式繞過 |
| 印地語（Hindi）搜尋 | 嘗試 3 次；成功 1 次（但回傳的都是英文頁面），另 2 次因額度用完未執行 |
| 列入清單的來源數 | 65 條（IN-01～IN-65） |
| 印度在地來源 | 政府來源 2 條（IN-49 India Code、IN-60 Bihar RERA）；印度媒體與印度業者來源 30 條以上（Entrackr、Inc42、Outlook Business、Business Today、Free Press Journal、IANS、The Week、Deccan Herald、Housing.com、Ply Reporter 等） |
| 印地語來源 | **0 條**（未達「至少 2 條」的要求，見缺口表） |

**成功執行的查詢（16 次）**

1. India home interiors market size Redseer Livspace organised share
2. Livspace FY25 revenue loss
3. HomeLane DesignCafe merger FY25 revenue
4. India interior design market size IMARC Mordor Intelligence USD billion
5. Indian home interiors market $20 billion organised players share percent Livspace HomeLane（extended）
6. ANAROCK housing sales top 7 cities 2025 units value
7. Knight Frank India residential sales 2025 top 8 cities
8. इंटीरियर डिजाइन बाजार भारत करोड़（印地語，extended；結果都是英文市調頁）
9. Redseer India home interiors market report organised segment growth（extended）
10. home interior cost per sq ft India 2025 basic premium luxury modular kitchen 2BHK package
11. Livspace exit Singapore Malaysia layoffs 2025
12. Urban Company IPO 2025 listing revenue FY25 profit
13. Architects Act 1972 interior designers Council of Architecture title "architect" protected interior design not regulated（extended）
14. BIS quality control order plywood wood based panels implementation date 2025
15. RERA section 14(3) structural defect five years builder liability interior
16. FDI policy construction development 100% automatic route DPIIT Press Note 3 2020 land border

**因額度用完而未執行的查詢（4 次）**

17. होम इंटीरियर कंपनी लिवस्पेस घाटा राजस्व（印地語）
18. बढ़ई मिस्त्री दिहाड़ी मजदूरी 2025 रुपये प्रति दिन（印地語）
19. IKEA India FY25 revenue loss stores
20. Asian Paints Beautiful Homes revenue home decor segment FY25 Godrej Interio revenue

> **本輪最大限制**：額度用完時，人才與工資、材料品牌與 WPI、消費者保護與投訴、簽證、IKEA 與其他玩家營收等題目都還沒開始搜尋，因此這幾節多為「無資料」，請見第 6 節的缺口表。

---

## 1. 市場關鍵結論

1. **「印度室內設計市場」的規模說法差距很大。** 2024–2025 年的市調推估介於 USD 23.6B（Credence，2024）與 USD 36.89B（IMARC，2025）之間。主流兩家 Mordor 與 IMARC 的 2025 年值分別是 USD 31.43B 與 USD 36.89B，相差約 17%（來源 IN-01、IN-03、IN-05、IN-06）。這些都是市調公司推估，不是官方統計，而且沒有一家能清楚區分「設計服務」與「裝修工程」。
2. **住宅與商業的占比互相矛盾。** IMARC 稱 2025 年住宅占 60%（IN-03），Mordor 卻稱 2025 年商業專案占營收 74.44%（IN-01）。兩者口徑不同，不可混用。
3. **組織化（品牌）業者占比低。** 一則行銷式個案稱組織化占比已從 2–3% 升到約 15%（IN-11，低信心）；Verified Market Research 稱逾 90% 為非組織化業者（IN-09，低信心）。市場仍以小包商與工匠為主。
4. **龍頭平台仍在虧損，但虧損在收斂。** Livspace FY25 營收 ₹1,460 crore（年增約 23%），淨損約 ₹242 crore（年減約 42%）（IN-15、IN-17）。HomeLane 在 2024 年 9 月以換股方式併購 DesignCafe，FY25 合併營業收入 ₹747.8 crore、淨損 ₹111 crore，未達原訂 ₹1,000 crore 的目標，該目標已延到 FY27（IN-25、IN-27）。
5. **需求面：新屋銷量下滑，但金額上升、產品高端化。** ANAROCK 統計前 7 大城市 2025 年住宅銷售 395,625 戶（年減 14%），金額卻增至逾 ₹6 lakh crore（年增 6%）（IN-34）。Knight Frank 統計前 8 大城市 2025 年銷售 348,207 戶，其中 ₹1 crore 以上住宅占 50%（IN-39）。
6. **住宅裝修單價（業者與金融業部落格的行情，非官方）：** 基本 ₹1,500–2,000/sq ft、中階 ₹2,000–3,000/sq ft、高階 ₹3,000–4,000+/sq ft（IN-43，低至中信心）。
7. **法規：室內設計師沒有法定證照。** 《建築師法》（Architects Act, 1972）只保護「architect」這個頭銜，不保護設計業務本身（IN-49、IN-50）。另外，合板的 BIS 品質管制命令（QCO）自 2025-02-28 起強制實施（IN-54）；RERA 第 14(3) 條規定開發商自交屋起負 5 年瑕疵責任（IN-58、IN-60）。
8. **平台開始轉向 AI，大規模裁員。** Livspace 在 2026 年 2 月裁員約 1,000 人，約占員工 12%，公司稱要轉型為「AI-native」組織（IN-19、IN-20）。

---

## 2. 十節

### Q1 市場規模與成長

**結論**：本輪找不到任何官方的「住宅室內裝修／翻修市場」統計。可取得的都是市調公司的「India interior design market」推估。這些推估把設計與施工混在一起，並包含住宅與商業，2025 年的區間約為 USD 31–37B。Redseer 另有一個「家居與家飾」口徑（屬家居零售），2024 年為 ₹2.8–3.0 trillion。FICCI、Grand View、6Wresearch、HomeLane 自述數字，以及 Livspace 與 Redseer 合作的「home interiors」數字，本輪都沒有找到。

#### Q1 表：所有找到的規模說法

| 來源# | 數值 | 年份 | 原始定義 | 歸桶 | 現況或預測 | 信心 |
|---|---|---|---|---|---|---|
| IN-01 Mordor Intelligence | USD 31.43B | 2025 | 「India Interior Design Market」，含住宅與商業；商業專案占 2025 年營收 74.44%；Mordor 自有推估架構 | 其他（設計＋住宅＋商業裝修混合） | 現況推估 | 中（市調推估，非官方） |
| IN-01 Mordor | USD 35.48B | 2026 | 同上 | 同上 | 推估 | 中 |
| IN-01 Mordor | USD 65.01B；CAGR 12.87%（2026–2031） | 2031 | 同上 | 同上 | **預測** | 中 |
| IN-03 IMARC（2026–2034 版） | USD 36.89B | 2025 | 「India Interior Design Market」，按裝飾類型、終端用戶、區域分類；住宅占 60%（2025） | 其他（混合） | 現況推估 | 中 |
| IN-03 IMARC | USD 74.73B；CAGR 8.16%（2026–2034） | 2034 | 同上 | 同上 | **預測** | 中 |
| IN-04 IMARC（舊版 2024–2032） | USD 31.5B | 2023 | 同一系列的舊版。搜尋摘要沒有明確對應到哪一個 URL，推定是 IN-04 頁面 | 其他（混合） | 推估 | 低（URL 對應不確定） |
| IN-04 IMARC（舊版） | USD 67.4B；CAGR 8.81%（2024–2032） | 2032 | 同上 | 同上 | **預測** | 低 |
| IN-05 Credence Research | USD 23,609.97 million | 2024 | 「India Interior Design Market」；區域占比：南印 30%、西印 28%、北印 27% | 其他（混合） | 推估 | 中 |
| IN-05 Credence | USD 66,163.37 million | 2032 | 同上 | 同上 | **預測** | 中 |
| IN-06 P&S Intelligence（PS Market Research，日文頁） | USD 36.4B | 2024 | 「India Interior Design Market」 | 其他（混合） | 推估 | 中 |
| IN-06 P&S | USD 81.2B；CAGR 14.3% | 2030 | 同上 | 同上 | **預測** | 中 |
| IN-07 Ken Research | USD 30.75B | 2023 | 「India Interior Design Market」 | 其他（混合） | 推估 | 中 |
| IN-08 Material360（部落格，標題「₹7 Lakh Crore Interior Design Industry」） | ₹2.74 lakh crore（₹2.74 兆） | 2023 | 「interior design industry」，定義不明 | 其他（混合） | 推估 | 低（二手部落格） |
| IN-08 Material360 | ₹7.07 lakh crore | 2032 | 同上 | 同上 | **預測** | 低 |
| IN-10 Analytics India Magazine | 約 USD 20B | 年份不明（舊文，推測在 2023 年前） | 「interior design market」，高度破碎 | 其他（混合） | 推估 | 低（年份不明；只因為是 Livspace 早期常被引用的說法而列出） |
| IN-11 OrangeOwl（行銷個案） | USD 22B+；組織化占比由 2–3% 升至約 15% | 年份不明 | 「interior design market」 | 其他（混合） | 推估 | 低 |
| IN-12 Redseer（Wakefit IPO DRHP 個案頁） | ₹2.8–3.0 trillion（Redseer 自註 US$34–36B） | 2024 | 「India's home & furnishings market」，含家具與家飾，偏零售口徑 | 家居零售 | 現況推估 | 中（Redseer 為 IPO 招股書撰寫產業報告的顧問；本輪只看到頁面摘要） |
| IN-13 MediaNews4U（引 Redseer） | 家具產業 USD 40B | 2026 | 「furniture industry」，含線上滲透率預測 | 家居零售 | **預測**（舊報告，發布年份推測約 2020–2021） | 低 |
| IN-14 Indian Retailer | USD 29.5B（標題）；約 USD 48.1B（2028）；家飾 CAGR 11.4%（2023–2028） | 2023 前後（不明） | 「home and interiors market」，含家飾 | 其他（家居零售＋裝修混合） | 現況與**預測**並列 | 低 |
| IN-09 Verified Market Research | 規模數字在搜尋結果中無法辨識；稱非組織化占比逾 90% | 2025–2033 報告 | 「interior design ecosystem」 | 其他 | — | 低（摘要稱原文數字有亂碼） |
| TechSci、ResearchAndMarkets（2020–2030F）、Ken Research Outlook 2028、IMARC Luxury Interior Design、Credence Luxury | 搜尋結果沒有揭露數值 | — | — | — | — | 無資料 |
| FICCI、Grand View Research、6Wresearch、HomeLane 自述、Livspace × Redseer「home interiors」 | **無資料** | — | — | — | — | 試過的查詢：#1、#5、#9 |
| 商業 fit-out 專門報告（Cushman & Wakefield、JLL、Colliers） | **無資料** | — | — | — | — | 預算用完，未搜尋 |

**住宅與商業的拆分**

- IMARC：住宅占 60%（2025）（IN-03）。
- Mordor：商業占 74.44%（2025），即住宅約 25.6%（IN-01，由反推得出）。
- 兩者互相矛盾，見第 6 節。
- 新屋與存量（翻修）的拆分：**無資料**。

**組織化占比**

- 約 15%（IN-11，低信心）。
- 逾 90% 為非組織化（IN-09，低信心）。
- Mordor 的質性描述：消費偏好正從「無品牌木工（unbranded carpentry）」轉向有保固、服務水準協議（SLA）與品牌系統櫃的模式（IN-02）。

**合理性檢查（推論，【示意】）**

- Material360 的 ₹2.74 兆（2023）約等於 ANAROCK 前 7 大城市新屋銷售金額 ₹5.68 兆（2024）的 48%。
- 這個比例看似偏高，但 Material360 的口徑是全國，且包含商業空間，因此未必不合理。
- 相對地，若只看住宅新屋：裝修單價 ₹1,500–4,000/sq ft，約為前 7 大城市新屋房價 ₹5,016–8,856/sq ft 的 17%–80%（IN-43、IN-40）。
- 結論：市調的全國總額與新屋流量規模大致同一數量級，但無法驗證細部結構。
- 人均翻修支出與占 GDP 比：因為人口與 GDP 都沒有在本輪取得來源，**無資料**。

### Q2 需求結構

**結論**：需求引擎是大都會的新成屋與預售屋交屋。2025 年前 7 大城市銷量下滑 14%，但銷售金額上升，而且產品結構明顯往高端移動，₹1 crore 以上住宅占 Knight Frank 前 8 大城市銷量的 50%。中古屋（resale）占比、屋齡結構與 PMAY-U 2.0 本輪都沒有取得。

#### 新屋銷售與推案（一手市場）

| 指標 | 數值 | 年份 | 來源 | 定義 | 信心 |
|---|---|---|---|---|---|
| 前 7 大城市住宅銷售戶數 | 約 395,625 戶（2024 年 459,645 戶，年減 14%） | 2025（曆年） | IN-34、IN-35、IN-36、IN-37 | ANAROCK 前 7 大城市：MMR、NCR、Bengaluru、Pune、Hyderabad、Chennai、Kolkata | 高（多源一致）【實際】 |
| 前 7 大城市銷售金額 | 逾 ₹6 lakh crore（2024 年約 ₹5.68 lakh crore，年增 6%） | 2025 | IN-34、IN-35、IN-36 | ANAROCK | 高【實際】 |
| 前 7 大城市新推案 | 約 419,170 戶（2024 年約 412,520 戶，年增約 2%） | 2025 | IN-34 | ANAROCK；MMR 與 Bengaluru 合占新供給約 48% | 中【實際】 |
| 新供給中 ₹2.5 crore 以上的占比 | 逾 21% | 2025 | IN-34 | ANAROCK | 中 |
| 平均房價漲幅 | 前 7 大城市 +8%；NCR +23% | 2025 | IN-34 | ANAROCK | 中 |
| 未售庫存 | +4% | 2025 年底 | IN-34 | ANAROCK | 中 |
| 2025 Q3 前 7 大城市 | 銷量年減 9%，金額年增 14% | 2025 Q3 | IN-38（標題） | ANAROCK | 中 |
| 城市銷量（ANAROCK） | MMR 127,875（−18%）；Pune 65,135（−20%）；Bengaluru 62,205（−5%）；NCR 57,220（−8%）；Chennai 約 22,180（+15%）；Hyderabad、Kolkata 數值無資料 | 2025 | IN-34 | ANAROCK | 中 |
| 前 8 大城市住宅銷售 | 348,207 戶（另一報導為 348,247）；年增率一說 −1%、一說 +1% | 2025 | IN-39、IN-40、IN-41、IN-42 | Knight Frank，**僅一手市場** | 中 |
| ₹1 crore 以上 | 175,091 戶，占 50%（年增 14%） | 2025 | IN-39、IN-41 | Knight Frank | 中高 |
| ₹50 lakh–1 crore | 99,422 戶（年減 8%） | 2025 | IN-39 | Knight Frank | 中 |
| ₹50 lakh 以下 | 73,694 戶（年減 17%） | 2025 | IN-39 | Knight Frank | 中 |
| 城市均價（₹/sq ft） | Mumbai 8,856（+7%）、Bengaluru 7,388（+12%）、Hyderabad 6,721（+13%）、NCR 6,028（+19%）、Pune 5,016（+5%）、Ahmedabad 3,197（+3%）；Chennai、Kolkata 無資料 | 2025 | IN-40 | Knight Frank，一手市場 | 中 |
| NRI（海外印度人）占住宅銷售 | 12–15%（十年前為個位數） | 2025 前後 | IN-40 | Knight Frank 評論 | 中 |

**本輪無資料的需求項目**

- 現屋（RTM）與預售（UC）的比例
- 中古屋交易占比
- 屋齡分布與 30 年以上占比（簡報已提示 Census 2011 過舊，本輪也沒有找到替代資料）
- 翻修週期
- PMAY-U 2.0 的戶數與預算

#### 住宅室內裝修單價

以下都是業者或金融業部落格的行情，屬【示意】。

| 等級 | 數值 | 來源 | 範圍說明 | 信心 |
|---|---|---|---|---|
| 基本 | ₹1,500–2,000/sq ft | IN-43（Poonawalla Fincorp 個人貸款部落格） | 粉刷、標準地板、小幅水電 | 低至中 |
| 中階 | ₹2,000–3,000/sq ft | IN-43 | — | 低至中 |
| 高階 | ₹3,000–4,000/sq ft，大都會可達 ₹4,000+ | IN-43 | 高級飾面、訂製櫃體、智慧配件 | 低至中 |
| 另一組業者級距 | 基本 ₹1,200–1,800；中階 ₹1,800–2,800；高階 ₹2,800–4,000+（₹/sq ft） | 搜尋摘要稱「一家室內設計公司」，URL 對應不確定（候選為 IN-44） | — | 低 |

**2BHK（約 1,000 sq ft）整套包價**

- 「一家設計公司」2026 年的報價（URL 對應不確定，候選為 IN-45 Housiey）：
  - 經濟款 ₹3.5–6 lakh
  - 標準款 ₹7–12 lakh
  - 高級款 ₹13–20 lakh
  - 奢華款 ₹22–40 lakh+
  - 包含材料、工資與**設計費**，也就是設計費內含於統包。信心：低
- 2BHK 平均 ₹8–15 lakh（2026 指南，候選為 IN-46）。信心：低
- 另一業者的 2025 指南稱 2BHK 一般為 ₹12–28 lakh，基本款 ₹12–18 lakh（IN-44）。信心：低
- 這三組報價在基本款上相差超過 2 倍，見第 6 節矛盾表。

**系統廚具（modular kitchen）**

- 2BHK 廚房 ₹3–4.5 lakh；3BHK 起價 ₹5 lakh（Delhi；IN-47 DesignCafe 部落格，業者自述）。信心：低至中
- 平價廚房 ₹1.5–2 lakh（IN-48 Housing.com）。信心：低至中
- 檯面材料：花崗岩 ₹100–350/sq ft、石英 ₹250–800/sq ft、天然大理石 ₹300–3,000+/sq ft。搜尋摘要沒有標明是哪個 URL，信心：低

**設計費與工期**

- 設計費行情（占工程費 %、按 sq ft 計或包價）：**無資料**。只有 IN-45 的統包價明示包含設計費，可作為「常與施工綁定」的弱證據。
- 典型工期（例如「45 天交付」的說法）：**無資料**，本輪沒有搜到。

### Q3 產業結構與主要玩家

**結論**：產業極度破碎，組織化占比約一成多（低信心）。

- 兩大專業平台都還在虧損，但正在收斂：Livspace FY25 營收 ₹1,460 crore、淨損 ₹242 crore；HomeLane 加 DesignCafe FY25 營收 ₹747.8 crore、淨損 ₹111 crore。
- 2024–2026 年的主軸是整併、延後營收目標，以及以 AI 為名的裁員。
- 公司總家數與 CR5、CR10 集中度：**無資料**。

| 公司 | 模式 | 最新財務與事件 | 來源 | 信心 |
|---|---|---|---|---|
| **Livspace** | 設計施工平台，主打住宅；母公司在新加坡（Inc42 以 SGD 換算淨損，推論母公司以新加坡元報表） | **營收**：FY25 ₹1,460 crore，年增約 23%。FY24 基數有兩說：₹1,185 crore（Entrackr）或 ₹1,216.2 crore（Inc42，僅持續營運部門）。**淨損**：FY25 約 ₹242 crore（Inc42 為 ₹242.6 crore = SGD 38.42 Mn）。FY24 有兩說：₹416 crore（Entrackr）或 ₹461.7 crore（Inc42）。**調整後 EBITDA 虧損**：約 ₹131 crore，接近減半；EBITDA 率 −13.4%（Entrackr）或 −9%（Inc42，口徑不同）。**成長來源**：公司稱來自 premium 與 mass-premium 住宅 | IN-15、IN-16、IN-17、IN-18（PTI，2025-10-13） | 高（營收與 FY25 淨損多源一致）【實際】 |
| Livspace（組織） | — | 2026 年 2 月裁員約 1,000 人，約占員工 12%，公司稱為「AI-native」重組。Entrackr 認為長期缺乏新資金是主因。更早的裁員：2023 年 3 月約 2%，2020 年 5 月約 450 人。高層異動：2025 年 6 月 CFO 離職、共同創辦人 Saurabh Jain 離職、印度 CBO Lalit Mittal 離職 | IN-19、IN-20、IN-21、IN-22、IN-23 | 中至高（裁員人數）；低（2020 與 2023 的細節及 CFO 日期，URL 對應不確定） |
| Livspace（海外） | — | 近期報導稱業務橫跨印度、東南亞與中東。舊報導（約 2020 年，募資 USD 90M）曾稱考慮進入馬來西亞、印尼、澳洲與中東。**本輪找不到退出新加坡或馬來西亞的報導** | IN-19、IN-24 | 低 |
| Livspace（股東） | — | 一則行銷個案稱 2023 年與 IKEA 策略合作，Ingka Group 有投資 | IN-11 | 低（需以官方新聞稿驗證） |
| **HomeLane**（母公司 Homevista Decor） | 設計施工平台，以系統櫃為主 | 2024 年 9 月以 100% 換股併購 **DesignCafe**，同時募資 ₹225 crore。FY25 合併營業收入 ₹747.8 crore，FY24 為 ₹613.6 crore，年增 22%；加計利息收入約 ₹755.65 crore（公司新聞稿為 ₹756 crore）。FY25 淨損 ₹111 crore。Q4 FY25 首度 EBITDA 轉正（₹2.8 crore），全年 EBITDA 率由 −15% 改善為 −9.9%。原訂 FY25 合併營收 ₹1,000 crore（FY24 兩家合計為 ₹761 crore），沒有達成，目標已延到 FY27 | IN-25、IN-26、IN-27、IN-28、IN-29 | 高（營收）【實際】 |
| **Urban Company** | 到府服務平台（鄰接裝修與維修） | FY25 營業收入 ₹1,144.5 crore（年增 38.2%）；總收入約 ₹1,260.68 crore。FY25 淨利 ₹239.8 crore（FY24 淨損 ₹92.7 crore），其中含一次性遞延所得稅利益 ₹211 crore，稅前利益約 ₹28.6 crore。IPO 約 ₹1,900 crore（新股 ₹429 crore、舊股 OFS ₹1,471 crore），價格上限 ₹103，估值約 ₹15,000 crore，超額認購約 103 倍，以 ₹162.25 掛牌（溢價約 57%）。印度營收有兩說：₹997 crore 或 ₹881.4 crore | IN-30、IN-31、IN-32、IN-33 | 高（營收與淨利）；中（IPO 結構，URL 對應不完全確定） |
| Mordor 列名的主要業者 | — | HomeLane、Pepperfry Studio、Urban Ladder、IKEA India – Planning Studio、Godrej Interio；並稱 Livspace 與 HomeLane 正在擴張城市據點 | IN-02 | 中（僅名單，沒有營收） |

**本輪無資料的玩家**

- Bonito Designs、Asian Paints Beautiful Homes、Godrej Interio（營收）、Sleek、Pepperfry、NoBroker Interiors、Square Yards Interiors、IKEA India（營收與門市數）、Hettich India、Häfele India
- 試過的查詢：#19、#20，但都因額度用完未執行

### Q4 通路與獲客

**結論**：資料極少。

- 已知的通路型態：
  - 專業平台（Livspace、HomeLane）擴張城市據點，並以線上視覺化降低決策摩擦（IN-02，質性描述）
  - 家居零售附帶設計服務（IKEA Planning Studio、Pepperfry Studio；IN-02）
  - 到府服務平台（Urban Company；IN-30）
  - 金融業者以個人貸款部落格切入翻修預算（IN-43）
- 平台用戶數、GMV、抽成、實體體驗中心數、與建商的合作關係：**無資料**（預算用完，未搜尋）

### Q5 法規與證照

以下為重點整理，**需專業人士最終確認**。

| 主題 | 內容 | 法律名稱與主管機關 | 來源 | 法定或自願 |
|---|---|---|---|---|
| 建築師 | 《建築師法》只保護「architect」頭銜。立法理由書明言不把建築設計、監造與施工劃為建築師專屬業務。法定「architect」指登錄在建築師委員會名冊上的人。虛偽表示已登錄者，可處最高 ₹1,000 罰金（條次以 India Code 原文為準） | 《建築師法》（The Architects Act, 1972, Act No. 20 of 1972，India Code 版本截至 2025-12-03）；主管機關為建築師委員會（Council of Architecture, CoA） | IN-49（政府）、IN-50 | **法定**（僅限頭銜） |
| 判例 | Delhi 高等法院在 Sudhir Arora v. Registrar of Companies 一案中認定，立法意旨只限制使用「architect」頭銜，不限制提供建築服務 | 判例 | IN-50（Mondaq） | — |
| 室內設計師 | 沒有任何法律定義、登記或管理室內設計師，也沒有強制名冊，任何人都可自稱「Interior Designer」。印度室內設計師學會（IIID）會員屬自願加入。非建築師常用的頭銜：Interior Designer、Interior Decorator、Space Planner、Interior Consultant | 沒有法定制度；IIID 為協會 | IN-51、IN-53（皆為二手實務指南） | **協會認證（自願）**，非法定 |
| 修法動向 | CoA 曾公布《建築師法》修正建議 | CoA | IN-52（僅標題，年份與內容不明） | — |
| 營建勞工 | 搜尋結果標題提到《營建勞工法》（BOCW Act 1996）在住宅實務中的角色劃分，內容沒有展開 | Building and Other Construction Workers Act, 1996 | IN-51（僅標題） | 法定（細節無資料） |
| 板材 BIS QCO | 《合板與木質平面門扇（品質管制）命令》（Plywood and Wooden Flush Door Shutters (Quality Control) Order, 2024）自 **2025-02-28** 生效；小型企業延至 2025-05-28，微型企業延至 2025-08-28。涵蓋 IS 303（一般合板）、IS 710（船用合板）、IS 4990（模板合板）、IS 2202（Part 1）（實心門扇）。木質板材（MDF、粒片板、木心板）約自 2025-02-10 或 02-11 起須取得 BIS 認證與 ISI 標章。2024-12-19 的利害關係人會議決定不再延期 | 商工部（Ministry of Commerce and Industry）；DPIIT 公告；印度標準局（BIS）執行 | IN-54、IN-55、IN-56、IN-57 | **法定**（強制認證）。注意：來源是顧問公司與業界媒體，本輪沒有找到政府公報原文 |
| RERA 瑕疵責任 | 第 14(3) 條：自交屋起 5 年內通報的結構瑕疵，以及工藝、品質、服務等瑕疵，由開發商在 30 日內免費修復；未修復時買方可求償。二手指南稱契約中限縮 5 年責任的條款無效 | 《不動產（規範與發展）法》（Real Estate (Regulation and Development) Act, 2016）；主管機關為各邦 RERA | IN-58、IN-59、IN-60（Bihar RERA 裁定 491/2023，政府）、IN-64、IN-65 | **法定**。適用對象是開發商（promoter），不是室內裝修承包商；室內飾面是否涵蓋，要看各邦裁定 |

**本輪無資料的法規項目**

- 私人工程有沒有全國性的承包商執照
- 市政建築規則（bye-laws）對結構變更的許可程序
- 商業 fit-out 的消防許可（fire NOC）
- 住宅社區（housing society）的 NOC 慣例
- 2023–2026 年的修法（BIS QCO 以外）

### Q6 消費者保護與糾紛

**結論**：只找到 RERA 對開發商的 5 年瑕疵責任（IN-58、IN-60）。

- 這項責任不直接適用於室內裝修公司（推論）。
- 室內裝修糾紛應該走《消費者保護法》（Consumer Protection Act, 2019）的消費者委員會，或國家消費者熱線（National Consumer Helpline），但本輪**沒有搜到驗證來源**。
- 以下項目皆為**無資料**：
  - 國家消費者熱線的室內裝修投訴統計
  - 訂金慣例（例如訂金 10%）
  - 付款階段
  - 平台的「10 年保固」說法
  - 常見糾紛與詐騙型態
- Mordor 的質性描述：消費者愈來愈偏好有保固與 SLA 的品牌業者（IN-02）。這可間接說明「無品牌木工」的品質與糾紛問題是品牌業者的切入點。這是推論。

### Q7 外資與台資進入規則

以下為重點整理，**需專業人士最終確認**。

**Press Note 3（2020）**

- 來自與印度陸地接壤國家（land-border countries）的投資，不論產業與持股上限，一律需要政府事先核准。
- 2026 年 3 月放寬：陸地接壤國家的「非控制性實益持股」若在 10% 以內，可走自動核准路徑（IN-61，考試補習網站轉述 DPIIT 的說法，信心：低至中）。
- 推論：台灣不是與印度陸地接壤的國家，因此 PN3 原則上不適用於台灣資本。但若投資架構中含有中國大陸的實益持股，就會受影響。

**不動產相關 FDI**

- 「不動產業務」與「農舍興建」禁止外資，但排除「市鎮開發」與「商業不動產開發」（IN-62，信心：低）。
- 營建開發（construction development）100% 自動核准的條件（最低面積、資本、閉鎖期等）：本輪**沒有在搜尋結果中驗證**，請以 DPIIT 最新的 Consolidated FDI Policy 為準（IN-63 為 2026 年的二手指南）。

**本輪無資料的項目**

- 室內設計或裝修服務公司能否 100% 外資持股
- 承包商登記類別
- 就業簽證薪資門檻（簡報提到年薪 USD 25,000，本輪**未驗證**）
- 外籍設計師的執業限制

**外商案例**

- IKEA India 的 Planning Studio 被 Mordor 列為主要業者（IN-02）。
- 一則行銷個案稱 Livspace 與 IKEA 在 2023 年策略合作，且 Ingka 有投資（IN-11，低信心）。
- 日本、韓國與台灣業者的案例：**無資料**。

### Q8 消費者行為

**結論**：從間接證據看，以大都會首購或新屋交屋客為主，預算往高端移動。

**間接證據**

- ₹1 crore 以上住宅占前 8 大城市一手銷量 50%，且年增 14%；₹50 lakh 以下則年減 17%（IN-39）。
- NRI 占住宅銷售 12–15%（IN-40）。
- Livspace 稱成長來自 premium 與 mass-premium 住宅（IN-17）。
- 融資：翻修成本指南出現在 NBFC Poonawalla Fincorp 的「個人貸款」部落格（IN-43），可作為「用個人貸款支應翻修」的弱證據。

**本輪無資料的項目**

- 房貸增貸（top-up）的利率與條件
- 各城市層級的預算
- 決策歷程與資訊來源
- 風格偏好
- 付款階段
- 室內裝修分期（EMI）的實際滲透率

### Q9 人才與工班

**結論**：**幾乎全無資料**。人才相關搜尋排在預算用完之後，沒有執行。

- 室內設計系畢業人數：無資料
- 設計師薪資：無資料
- Bengaluru、Mumbai、Delhi 的木工與泥作日薪：無資料。試過印地語查詢 #18，因額度用完未執行
- 缺工與移工：無資料
- 唯一相關的推論：Livspace 裁員約 1,000 人、約占員工 12%（IN-20），反推總員工約 8,300 人（【示意】，假設 12% 的分母就是全體員工）

### Q10 材料供應鏈與價格

**結論**：只確認了板材的強制 BIS 認證（QCO）在 2025 年 2 月起生效（IN-54、IN-55）。

- 這會墊高進口與小型板材廠的合規門檻（推論）。
- 以下項目皆為**無資料**：
  - 在地品牌的營收與市占：Asian Paints、Berger、Kajaria、Somany、Jaquar、Hindware、Cera、Greenply、CenturyPly、Merino、Hettich
  - 五金對中國的進口依賴度
  - 2022–2026 年營建材料批發物價指數（WPI）的漲幅
- 檯面材料價格見 Q2（低信心）。

---

## 3. 橫向比較表一列（印度）

| 市場 | 人均 GDP | 住宅翻修市場規模 | 室內設計服務市場 | 住宅裝修單價（基本／中階／高階） | 設計費行情 | 30 年以上屋齡占比 | 中古屋交易占比 | 執業管制（設計師／承包商） | 外資可否 100% 持股 | 主要平台 | 前 3 大玩家 | 信心 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 印度（IN） | 無資料（本輪未搜尋） | 無官方或專門的住宅翻修數字。【示意】推估區間：IMARC USD 36.89B × 住宅 60% ≈ USD 22.1B（2025，IN-03）；Mordor USD 31.43B × 住宅約 25.6% ≈ USD 8.0B（2025，IN-01）。兩者口徑矛盾，且都含新屋裝修 | 「interior design market」（設計＋施工混合）：USD 31.43B（Mordor，2025，IN-01）至 USD 36.89B（IMARC，2025，IN-03）；純設計服務：無資料 | ₹1,500–2,000／₹2,000–3,000／₹3,000–4,000+ per sq ft（IN-43，業者與金融業行情） | 無資料（常與統包綁定，屬弱證據，IN-45） | 無資料 | 無資料（Knight Frank 只涵蓋一手市場） | 設計師：無法定證照，只保護「architect」頭銜（IN-49、IN-50）；承包商：無資料 | 無資料（室內設計或裝修服務未驗證；PN3 不適用台灣，為推論，IN-61） | Livspace、HomeLane（含 DesignCafe）、Urban Company（到府服務） | Livspace（FY25 ₹1,460 crore）、HomeLane＋DesignCafe（FY25 ₹747.8 crore）、第 3 名無資料 | 低至中 |

---

## 4. 台灣比較錨點原始輸入（印度端）

| 錨點 | 印度原始輸入 | 年份 | 來源 | 信心 | 備註 |
|---|---|---|---|---|---|
| 住宅翻修市場規模 | 無官方值；【示意】區間 USD 8.0B–22.1B（由市調總額乘以住宅占比反推，見第 3 節） | 2025 | IN-01、IN-03 | 低 | 含新屋裝修；兩個占比互相矛盾 |
| 人口 | 無資料 | — | — | — | 本輪未搜尋 |
| 名目 GDP | 無資料 | — | — | — | 本輪未搜尋 |
| 住宅裝修單價 | ₹1,500–2,000／₹2,000–3,000／₹3,000–4,000+ per sq ft（原單位，未換算 m²） | 2025–26 | IN-43 | 低至中 | 業者與金融業部落格行情 |
| 設計費占工程費比 | 無資料 | — | — | — | 常內含於統包（IN-45，低） |
| 設計公司家數 | 無資料 | — | — | — | 無法定登記制度，官方統計可能根本不存在（推論） |
| 平台滲透率 | 無直接數據；組織化占比約 15%（IN-11）或低於 10%（IN-09） | 年份不明 | IN-11、IN-09 | 低 | 組織化不等於平台 |
| 補充：房價基準 | Mumbai ₹8,856、Bengaluru ₹7,388、NCR ₹6,028 per sq ft（一手市場） | 2025 | IN-40 | 中 | 可算裝修單價占房價的比例 |

---

## 5. 對台灣中型集團（璞石：宜蘭＋台北信義；裝修＋不動產＋家居零售）的啟示

1. **規模大，但平台模式極度燒錢。** 即使是龍頭，Livspace FY25 營收 ₹1,460 crore 仍淨損 ₹242 crore（IN-15）；HomeLane 晚了兩年才把 ₹1,000 crore 目標延到 FY27（IN-27）。啟示：不要照搬重資本的設計施工平台。可複製的是 HomeLane 先追求單位經濟、再透過換股整併拉高規模的路線（Q4 FY25 EBITDA 轉正，IN-26）。【推論】
2. **新屋交屋綁定裝修是主要需求引擎。** 印度需求集中在大都會一手新屋，而且高端化（₹1 crore 以上占 50%，IN-39）。這和璞石「不動產＋裝修」的組合相同：在宜蘭推案時把系統櫃與裝修方案綁進交屋流程，最能直接借鏡印度 2BHK 包價的產品化做法（IN-45、IN-46）。【推論】
3. **標準化包價與系統櫃取代無品牌木工。** Mordor 指出消費者從無品牌木工轉向有保固、SLA 的品牌系統櫃（IN-02）。這和台灣系統櫃取代木作的趨勢同方向。璞石的家居零售線可以把「固定價格方案＋保固條款」做成主打商品。【推論】
4. **AI 會取代設計前端人力。** Livspace 以「AI-native」為名裁員約 12%（IN-20）。啟示：台灣中型業者應該先用 AI 3D 與報價工具壓低設計前端人力成本，而不是擴編設計師。【推論】
5. **跨境到印度的可行性偏低（評分 1/5）。** 綁定限制如下：
   - 單價低（₹1,500–4,000/sq ft）
   - 工班高度非組織化
   - 龍頭仍在虧損
   - 室內設計師雖無證照門檻，但材料受 BIS 強制認證管制（IN-54）
   - 反面因素：PN3 原則上不適用於台灣資本（推論），因此資本進入本身的阻礙不大，主要阻礙在市場面
   
   若要接觸印度市場，較可行的是材料或五金供應（需取得 BIS 認證），或技術與 SaaS 授權，而不是直接做裝修服務。【推論】

---

## 6. 矛盾表與缺口表

### 6.1 矛盾表（同一指標差距超過 30%，或方向相反）

| 指標 | 來源 1 | 來源 2 | 差異原因 | 裁決 |
|---|---|---|---|---|
| 「India interior design market」2024 年規模 | Credence：USD 23,609.97M（IN-05） | P&S：USD 36.4B（IN-06）；差約 54% | 定義與方法不同（各家自訂口徑，沒有公開是否含家具、軟裝或商業 fit-out） | 不取平均。兩者都只是市調推估。以 Mordor（USD 31.43B）與 IMARC（USD 36.89B）的 2025 年值作為主要參考區間，並標示「市調推估、非官方」 |
| 住宅與商業占比（2025） | IMARC：住宅 60%（IN-03） | Mordor：商業 74.44%（住宅約 25.6%）（IN-01） | 定義與方法不同（分類軸是終端用戶還是專案類型；商業 fit-out 的單案金額較大） | **無法裁決**。報告中不要用單一占比去推算住宅市場；若要用，必須同時列出兩者的區間並標示【示意】 |
| 市場規模的年代差 | 約 USD 20B（IN-10，年份不明，舊文） | USD 30.75B（2023，IN-07）至 USD 36.89B（2025，IN-03） | 年份不同，且口徑不同 | 以 2023–2025 年的數字為準；USD 20B 只當作歷史說法 |
| 組織化占比 | 約 15%（IN-11） | 非組織化逾 90%，即組織化低於 10%（IN-09） | 定義（組織化指品牌平台，還是含所有登記公司）與來源品質（行銷文、亂碼摘要） | 兩者都是低信心。只能說組織化占比「約 1 成上下」，屬【示意】 |
| 前 7 或 8 大城市住宅銷售的變化方向（2025） | ANAROCK：−14%，395,625 戶（IN-34） | Knight Frank：−1%（另一報導 +1%），348,207 戶（IN-39、IN-40） | 城市範圍不同（ANAROCK 含 Kolkata、不含 Ahmedabad；Knight Frank 含 Ahmedabad）、統計方法不同（追蹤的專案範圍、MMR 與 Mumbai region 的界定） | 兩者並列。量的下滑幅度以 ANAROCK 為準（多源一致）；Knight Frank 強調結構高端化。KF 內部的 −1% 與 +1% 以多數報導的 −1% 為準 |
| 2BHK 基本款統包價 | ₹3.5–6 lakh（IN-45 候選） | ₹12–18 lakh（IN-44） | 範圍不同（是否含泥作、水電與家具；業者定位）、行銷偏差 | 不取平均。報告只引用 IN-43 的每平方英尺級距，並註明低信心 |
| Livspace FY24 淨損 | ₹416 crore（IN-15） | ₹461.7 crore（IN-16）；差約 11%，未達 30% | 可能是持續營運部門重編（Inc42 的 FY24 營收也標明「持續營運」） | FY25 的 ₹242 crore 兩者一致，予以採用；FY24 兩說並列 |
| HomeLane FY25 營收 | ₹747.8 crore（營業收入，IN-25） | ₹756 crore（公司新聞稿，IN-26） | 定義不同（是否含利息收入 ₹7.86 crore） | 採用營業收入 ₹747.8 crore |
| Urban Company FY25 營收 | ₹1,144.5 crore（營業收入，IN-30） | ₹1,260.68 crore（總收入） | 定義不同（含利息與基金收益約 ₹117 crore） | 採用營業收入 ₹1,144.5 crore |
| Urban Company 印度營收 | ₹997 crore | ₹881.4 crore | 定義不明（分部口徑不同） | 無法裁決；以 DRHP 或 RHP 為準 |

### 6.2 缺口表

| 項目 | 試過的搜尋 | 建議取得方式 |
|---|---|---|
| Livspace × Redseer、HomeLane、FICCI、Grand View、6Wresearch 的「home interiors」規模 | #1、#5、#9 | 下一輪補搜：「Redseer home interiors India USD billion 2024」「FICCI home interiors report」「Grand View India interior design」；或查 Livspace、HomeLane 的新聞稿 |
| 商業 fit-out 規模與每 sq ft 成本 | 未執行（預算用完） | Cushman & Wakefield、JLL、Colliers、CBRE 的 India Fit-out Cost Guide |
| 家居零售規模（IKEA India、Pepperfry、Godrej Interio 營收） | #19、#20 未執行 | Entrackr 或 The Ken 的 MCA 財報報導；IKEA India（Ikano／Ingka）年報 |
| 中古屋占比、RTM 與 UC 比例、屋齡（Census 2011 過舊）、PMAY-U 2.0 | 未執行 | MoHUA 的 PMAY-U 2.0 儀表板；PropEquity 或 PropTiger 的 resale 報告；NSO 第 76／78 輪住房狀況調查 |
| 設計費 %、「45 天交付」說法、10 年保固 | #10（只有間接結果） | 查 Livspace、HomeLane、DesignCafe 官網的 FAQ 與條款 |
| 承包商執照、市政建築規則、fire NOC、society NOC | 未執行 | 各市（BBMP、MCGM）的建築規則；國家建築規範（National Building Code 2016）；律師事務所解說 |
| Consumer Protection Act 2019 與 NCH 投訴統計 | 未執行 | consumerhelpline.gov.in 的年報（NCH Annual Report）；消費者事務部（Department of Consumer Affairs） |
| FDI：營建開發與服務業的 100% 自動核准條件；就業簽證 USD 25,000 門檻 | #16（部分） | DPIIT Consolidated FDI Policy（2020 年起適用版本，含 2026 年 3 月 PN3 修正）；MHA 簽證手冊 |
| 設計師與工班薪資、日薪、缺工 | #18 未執行 | 勞動部（Labour Bureau）的 Wage Rates in Rural/Urban India、各邦最低工資公告、Naukri 或 AmbitionBox 薪資資料；印地語媒體（Dainik Bhaskar、Amar Ujala） |
| 材料品牌、WPI、中國五金依賴 | 未執行 | 經濟顧問辦公室（Office of the Economic Adviser，eaindustry.nic.in）的 WPI；各上市公司年報（Asian Paints、Kajaria、Greenply、Century Plyboards） |
| 人均 GDP、人口、名目 GDP | 未執行 | IMF WEO、MoSPI |
| 印地語來源（至少 2 條） | #8 成功但結果為英文；#17、#18 未執行 | 下一輪優先補搜印地語媒體：「इंटीरियर डिजाइन कारोबार」「घर का इंटीरियर खर्च प्रति वर्ग फुट」 |
| Livspace 退出新加坡或馬來西亞 | #11（找不到退出報導） | 查 Livspace 新加坡實體在 ACRA 的公告；The Ken 或 DealStreetAsia |

---

## 7. 關鍵指標 CSV

```csv
market,metric,value,unit,year,source_id,source_url,definition,confidence
IN,室內設計市場規模(Mordor),31.43,十億美元,2025,IN-01,https://www.mordorintelligence.com/industry-reports/india-interior-design-market/market-size,Mordor「India Interior Design Market」含住宅與商業;市調推估非官方,中
IN,室內設計市場規模預測(Mordor),65.01,十億美元,2031(預測),IN-01,https://www.mordorintelligence.com/industry-reports/india-interior-design-market/market-size,同上;CAGR 12.87% 2026-2031,中
IN,室內設計市場商業占比(Mordor),74.44,%,2025,IN-01,https://www.mordorintelligence.com/industry-reports/india-interior-design-market/market-size,商業專案占營收比;與IMARC住宅60%矛盾,中
IN,室內設計市場規模(IMARC),36.89,十億美元,2025,IN-03,https://www.imarcgroup.com/india-interior-design-market,IMARC「India Interior Design Market」2026-2034版;市調推估,中
IN,室內設計市場規模預測(IMARC),74.73,十億美元,2034(預測),IN-03,https://www.imarcgroup.com/india-interior-design-market,同上;CAGR 8.16% 2026-2034,中
IN,室內設計市場住宅占比(IMARC),60,%,2025,IN-03,https://www.imarcgroup.com/india-interior-design-market,終端用戶住宅占比;與Mordor矛盾,中
IN,室內設計市場規模(Credence),23609.97,百萬美元,2024,IN-05,https://www.credenceresearch.com/report/india-interior-design-market,Credence「India Interior Design Market」;市調推估,中
IN,室內設計市場規模(P&S),36.4,十億美元,2024,IN-06,https://www.psmarketresearch.com/ja/market-analysis/india-interior-design-market,P&S「India Interior Design Market」;2030預測81.2B,中
IN,室內設計產業規模(Material360),2.74,lakh crore 盧比(=₹2.74兆),2023,IN-08,https://material360.co/blog/interior-design-industry,部落格;定義不明;2032預測₹7.07 lakh crore,低
IN,家居與家飾市場規模(Redseer),2.8-3.0,trillion 盧比(Redseer自註US$34-36B),2024,IN-12,https://redseer.com/casestudies/how-redseer-helped-indias-largest-d2c-home-furnishings-brand-by-revenue-in-fiscal-2024-wakefit-file-its-drhp/,Redseer「home & furnishings market」;家居零售口徑,中
IN,組織化業者占比,約15,%,年份不明,IN-11,https://orangeowl.marketing/unicorn-chronicles/livspace-success-story/,行銷個案稱由2-3%升至約15%,低
IN,Livspace營收,1460,crore 盧比,FY25,IN-15,https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863,營業收入;年增約23%;多源一致,高
IN,Livspace淨損,242,crore 盧比,FY25,IN-15,https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863,淨損;Inc42為242.6 crore,高
IN,HomeLane合併營業收入,747.8,crore 盧比,FY25,IN-25,https://entrackr.com/fintrackr/homelane-records-rs-748-revenue-in-fy25-but-falls-short-of-projections-10586234,含DesignCafe(2024年9月換股併購)之合併營業收入,高
IN,HomeLane淨損,111,crore 盧比,FY25,IN-25,https://entrackr.com/fintrackr/homelane-records-rs-748-revenue-in-fy25-but-falls-short-of-projections-10586234,合併淨損,中
IN,Urban Company營業收入,1144.5,crore 盧比,FY25,IN-30,https://www.outlookbusiness.com/start-up/news/urban-company-swings-to-2398-cr-profit-in-fy25-ahead-of-ipo,到府服務平台營業收入;年增38.2%,高
IN,前7大城市住宅銷售戶數(ANAROCK),395625,戶,2025,IN-34,https://www.businesstoday.in/amp/real-estate/story/housing-sales-fall-14-in-2025-amid-sky-high-prices-it-layoffs-anarock-research-508242-2025-12-26,ANAROCK前7大城市一手銷售;年減14%,高
IN,前7大城市住宅銷售金額(ANAROCK),6,lakh crore 盧比(=₹6兆),2025,IN-34,https://www.businesstoday.in/amp/real-estate/story/housing-sales-fall-14-in-2025-amid-sky-high-prices-it-layoffs-anarock-research-508242-2025-12-26,ANAROCK;2024年為5.68 lakh crore;年增6%,高
IN,前7大城市新推案戶數(ANAROCK),419170,戶,2025,IN-34,https://www.businesstoday.in/amp/real-estate/story/housing-sales-fall-14-in-2025-amid-sky-high-prices-it-layoffs-anarock-research-508242-2025-12-26,ANAROCK新供給;年增約2%,中
IN,前8大城市住宅銷售戶數(Knight Frank),348207,戶,2025,IN-39,https://realtynmore.com/premium-housing-captures-50-of-indias-348207-residential-sales-in-2025-knight-frank-india/,Knight Frank僅一手市場,中
IN,₹1 crore以上住宅銷售占比(Knight Frank),50,%,2025,IN-39,https://realtynmore.com/premium-housing-captures-50-of-indias-348207-residential-sales-in-2025-knight-frank-india/,175091戶;年增14%,中
IN,Mumbai一手住宅均價,8856,₹/sq ft,2025,IN-40,https://www.outlookbusiness.com/markets/housing-sales-dip-1-last-year-in-top-8-cities-avg-price-grows-up-to-19-knight-frank,Knight Frank Mumbai region;年增7%,中
IN,住宅裝修單價-基本,1500-2000,₹/sq ft,2025-26,IN-43,https://poonawallafincorp.com/blogs/personal-loan/full-home-renovation-cost-in-india,NBFC部落格行情;粉刷/標準地板/小幅水電,低
IN,住宅裝修單價-中階,2000-3000,₹/sq ft,2025-26,IN-43,https://poonawallafincorp.com/blogs/personal-loan/full-home-renovation-cost-in-india,NBFC部落格行情,低
IN,住宅裝修單價-高階,3000-4000+,₹/sq ft,2025-26,IN-43,https://poonawallafincorp.com/blogs/personal-loan/full-home-renovation-cost-in-india,NBFC部落格行情;大都會可逾4000,低
IN,2BHK系統廚具價格(Delhi),3-4.5,lakh 盧比,2025-26,IN-47,https://www.designcafe.com/blog/modular-kitchen-interiors/modular-kitchen-cost-delhi/,業者部落格自述;3BHK起價5 lakh,低
IN,合板BIS QCO生效日,2025-02-28,日期,2025,IN-54,https://alephindia.in/bis-qco-for-the-plywood-face-panels.php,Plywood and Wooden Flush Door Shutters (QC) Order 2024;小型2025-05-28/微型2025-08-28,中
IN,RERA開發商瑕疵責任期,5,年(自交屋起),2016法(現行),IN-58,https://housing.com/news/compensation-for-defects-in-construction-after-possession-under-rera/,RERA第14(3)條;30日內免費修復,中
IN,Livspace裁員人數,約1000,人(約占員工12%),2026-02,IN-20,https://india.entrepreneur.com/?p=93997,AI-native重組,中
IN,NRI占住宅銷售比,12-15,%,2025,IN-40,https://www.outlookbusiness.com/markets/housing-sales-dip-1-last-year-in-top-8-cities-avg-price-grows-up-to-19-knight-frank,Knight Frank評論,中
```

---

## 8. 來源清單

所有來源的讀取方式都是「搜尋結果內容」：WebFetch 被封鎖，沒有開啟原文。

| # | 標題 | 機構或作者 | 年份 | 語言 | URL | 讀取方式 |
|---|---|---|---|---|---|---|
| IN-01 | India Interior Design Market Analysis（market size） | Mordor Intelligence | 2025–26 | 英 | https://www.mordorintelligence.com/industry-reports/india-interior-design-market/market-size | 搜尋結果內容 |
| IN-02 | India Interior Design Market Size & Share Analysis | Mordor Intelligence | 2025–26 | 英 | https://www.mordorintelligence.com/industry-reports/india-interior-design-market | 搜尋結果內容 |
| IN-03 | India Interior Design Market Size, Share, Trends and Forecast 2026–2034 | IMARC Group | 2026 | 英 | https://www.imarcgroup.com/india-interior-design-market | 搜尋結果內容 |
| IN-04 | Interior Design Market India（舊版） | IMARC Group | 約 2024 | 英 | https://www.imarcgroup.com/interior-design-market-india | 搜尋結果內容（數值與 URL 的對應為推定） |
| IN-05 | India Interior Design Market Size, Growth and Forecast 2032 | Credence Research | 2025 | 英 | https://www.credenceresearch.com/report/india-interior-design-market | 搜尋結果內容 |
| IN-06 | India Interior Design Market（日文頁） | P&S Intelligence | 2024 | 日／英 | https://www.psmarketresearch.com/ja/market-analysis/india-interior-design-market | 搜尋結果內容 |
| IN-07 | India Interior Design Market, Strategic Roadmap 2030 | Ken Research | 2024 前後 | 英 | https://www.kenresearch.com/industry-reports/india-interior-design-market | 搜尋結果內容 |
| IN-08 | The ₹7 Lakh Crore Interior Design Industry Is Emerging | Material360 | 不明 | 英 | https://material360.co/blog/interior-design-industry | 搜尋結果內容 |
| IN-09 | India Interior Design Market Report 2025–2033 | Verified Market Research | 2025 | 英 | https://www.verifiedmarketresearch.com/product/india-interior-design-market/ | 搜尋結果內容 |
| IN-10 | Machine Learning Helps Livspace Corner The Biggest Share In The $20 Billion Interior Design Market | Analytics India Magazine | 不明（舊文） | 英 | https://analyticsindiamag.com/deep-tech/machine-learning-helps-livspace-corner-the-biggest-share-in-the-20-billion-interior-design-market | 搜尋結果內容 |
| IN-11 | LivSpace Success Story: 5 Actionable Lessons | OrangeOwl | 不明 | 英 | https://orangeowl.marketing/unicorn-chronicles/livspace-success-story/ | 搜尋結果內容 |
| IN-12 | How Redseer helped India's largest D2C home furnishings brand (Wakefit) file its DRHP | Redseer Strategy Consultants | 2025 | 英 | https://redseer.com/casestudies/how-redseer-helped-indias-largest-d2c-home-furnishings-brand-by-revenue-in-fiscal-2024-wakefit-file-its-drhp/ | 搜尋結果內容 |
| IN-13 | India's furniture industry to touch $40 billion by 2026: Redseer report | MediaNews4U | 約 2021 | 英 | https://www.medianews4u.com/indias-furniture-industry-to-touch-40-billion-by-2026-redseer-report/ | 搜尋結果內容 |
| IN-14 | How India's Home and Interior Market Skyrocketed to $29.5 Billion | Indian Retailer | 不明 | 英 | https://www.indianretailer.com/article/retail-business/home/how-indias-home-and-interior-market-skyrocketed-295-billion-top-trends | 搜尋結果內容 |
| IN-15 | Livspace posts Rs 1,460 Cr revenue in FY25, losses shrink 42% | Entrackr | 2025 | 英 | https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863 | 搜尋結果內容 |
| IN-16 | Livspace's FY25 Loss Declines 43% To INR 243 Cr | Inc42 | 2025 | 英 | https://inc42.com/buzz/livspaces-fy25-loss-declines-43-to-inr-243-cr/ | 搜尋結果內容 |
| IN-17 | Livspace Revenue Rises 23% to ₹1,460 Cr in FY'25; Losses Come Down | Outlook Business（PTI） | 2025 | 英 | https://www.outlookbusiness.com/corporate/livspace-revenue-rises-23-to-1460-cr-in-fy25-losses-come-down | 搜尋結果內容 |
| IN-18 | Livspace revenue rises 23 pc to Rs 1,460 cr in FY'25 | The Week（PTI wire） | 2025-10-13 | 英 | https://www.theweek.in/wire-updates/business/2025/10/13/dcm46-biz-realty-livspace.html | 搜尋結果內容 |
| IN-19 | Livspace lays off 1,000 employees amid co-founder exit and AI shift | Entrackr | 2026 | 英 | https://entrackr.com/news/livspace-lays-off-1000-employees-amid-co-founder-exit-and-ai-shift-11140571 | 搜尋結果內容 |
| IN-20 | Livspace Layoffs: Around 1,000 Employees Affected Amid AI-Driven Reorganisation | Entrepreneur India | 2026-02-21 | 英 | https://india.entrepreneur.com/?p=93997 | 搜尋結果內容 |
| IN-21 | Livspace CBO Lalit Mittal exits after co-founder departure and mass layoffs | Entrackr | 2026 | 英 | https://entrackr.com/news/livspace-cbo-lalit-mittal-exits-after-co-founder-departure-and-mass-layoffs-11150871 | 搜尋結果內容 |
| IN-22 | Another Exit At Livspace: India CBO Lalit Mittal Steps Down | Inc42 | 2026 | 英 | https://inc42.com/?p=550262 | 搜尋結果內容 |
| IN-23 | 100 job cuts at Livspace | HR Katha | 約 2023 | 英 | https://www.hrkatha.com/news/layoff/100-job-cuts-at-livspace/ | 搜尋結果內容 |
| IN-24 | Home renovation platform Livspace raises $90 million for expansion | Deccan Herald | 約 2020 | 英 | https://www.deccanherald.com/business/home-renovation-platform-livspace-raises-90-million-for-expansion-881765.html | 搜尋結果內容 |
| IN-25 | HomeLane records Rs 748 Cr revenue in FY25 but falls short of projections | Entrackr | 2025 | 英 | https://entrackr.com/fintrackr/homelane-records-rs-748-revenue-in-fy25-but-falls-short-of-projections-10586234 | 搜尋結果內容 |
| IN-26 | HomeLane reports 22% revenue growth in FY25, achieves EBITDA profitability in Q4 | Franchise India | 2025 | 英 | https://www.franchiseindia.com/index.php/insights/en/news/homelane-reports-22-revenue-growth-in-fy25-achieves-ebitda-profitability-in-q4.57729 | 搜尋結果內容 |
| IN-27 | Inside HomeLane's Decade-Long Quest To Organise Home Interiors And Build A ₹1,000 Cr Business | Inc42 | 2025–26 | 英 | https://inc42.com/?p=566464 | 搜尋結果內容 |
| IN-28 | Homevista Decor Acquires DesignCafe, Raises Rs 225 Cr to Drive Growth | Indian Retailer | 2024 | 英 | https://indianretailer.com/news/retail-india-news-homevista-decor-acquires-designcafe-raises-rs-225-cr-drive-growth | 搜尋結果內容 |
| IN-29 | Homevista Decor raises Rs 225cr fund | India Retailing | 2024-09-26 | 英 | https://www.indiaretailing.com/2024/09/26/homevista-decor-raises-rs-225cr-fund/ | 搜尋結果內容 |
| IN-30 | Urban Company Swings to ₹239.8 Cr Profit in FY25 Ahead of IPO | Outlook Business | 2025 | 英 | https://www.outlookbusiness.com/start-up/news/urban-company-swings-to-2398-cr-profit-in-fy25-ahead-of-ipo | 搜尋結果內容 |
| IN-31 | IPO-Bound Urban Company Posts Profit, Thanks to ₹211-Crore Deferred Tax Credit | Angel One | 2025 | 英 | https://www.angelone.in/news/ipos/ipo-bound-urban-company-posts-profit-thanks-to-211-crore-deferred-tax-credit | 搜尋結果內容 |
| IN-32 | Urban Company Makes Stellar Debut with 57% Premium, Lists at ₹162.25 | 5paisa | 2025 | 英 | https://www.5paisa.com/index.php/news/urban-company-ipo-listing | 搜尋結果內容 |
| IN-33 | Urban Company IPO: 57.5% Listing Gains After 103x Subscription | INDmoney | 2025 | 英 | https://www.indmoney.com/blog/ipo/urban-company-ipo-review | 搜尋結果內容 |
| IN-34 | Housing sales fall 14% in 2025 amid sky-high prices, IT layoffs: ANAROCK Research | Business Today | 2025-12-26 | 英 | https://www.businesstoday.in/amp/real-estate/story/housing-sales-fall-14-in-2025-amid-sky-high-prices-it-layoffs-anarock-research-508242-2025-12-26 | 搜尋結果內容 |
| IN-35 | Housing Sales Value In Top 7 Indian Cities Rises 6% To ₹6 Lakh Crore In 2025 | Free Press Journal | 2025-12 | 英 | https://www.freepressjournal.in/business/housing-sales-value-in-top-7-indian-cities-rises-6-to-6-lakh-crore-in-2025-despite-14-volume-drop | 搜尋結果內容 |
| IN-36 | Housing sales value in Indian cities jump 6 pc in 2025: Report | IANS | 2025-12-26 | 英 | https://ianslive.in/housing-sales-value-in-indian-cities-jump-6-pc-in-2025-report--20251226113519 | 搜尋結果內容 |
| IN-37 | Housing Sales Volume Down 14% in 2025 in 7 Cities: Anarock | Outlook Business | 2025-12 | 英 | https://www.outlookbusiness.com/corporate/housing-sales-volume-down-14-in-2025-in-7-cities-anarock | 搜尋結果內容 |
| IN-38 | Housing sales dip 9% across top-7 cities in Q3 2025, but sales value jumps 14%: Anarock | Storyboard18 | 2025 | 英 | https://www.storyboard18.com/special-coverage/housing-sales-dip-9-across-top-7-cities-in-q3-2025-but-sales-value-jumps-14-anarock-81520.htm | 搜尋結果內容 |
| IN-39 | Premium housing captures 50% of India's 348,207 residential sales in 2025: Knight Frank India | Realty n More | 2026-01 | 英 | https://realtynmore.com/premium-housing-captures-50-of-indias-348207-residential-sales-in-2025-knight-frank-india/ | 搜尋結果內容 |
| IN-40 | Housing Sales Dip 1% Last Year in Top-8 Cities, Avg Price Grows up to 19%: Knight Frank | Outlook Business | 2026-01 | 英 | https://www.outlookbusiness.com/markets/housing-sales-dip-1-last-year-in-top-8-cities-avg-price-grows-up-to-19-knight-frank | 搜尋結果內容 |
| IN-41 | Premium Homes Above Rs 1 Crore Account for 50% of India Housing Sales in 2025: Knight Frank | NBM&CW | 2026 | 英 | https://www.nbmcw.com/news/premium-homes-above-rs-1-crore-account-for-50-of-india-housing-sales-in-2025-knight-frank.html | 搜尋結果內容 |
| IN-42 | Residential sales in India dip slightly in 2025 despite softer home loan rates | Asia News Network | 2026 | 英 | https://asianews.network/residential-sales-in-india-dip-slightly-in-2025-despite-softer-home-loan-rates-report | 搜尋結果內容 |
| IN-43 | Full home renovation cost in India | Poonawalla Fincorp | 2025–26 | 英 | https://poonawallafincorp.com/blogs/personal-loan/full-home-renovation-cost-in-india | 搜尋結果內容 |
| IN-44 | 2 BHK Interior Design Cost Guide for Flats in India 2025 | Tint Tone and Shade | 2025 | 英 | https://tinttoneandshade.com/blog/interior-design-cost-2bhk-flats-guide | 搜尋結果內容 |
| IN-45 | Interior Budgeting 2026: 1BHK/2BHK/3BHK Cost Breakdowns | Housiey | 2026 | 英 | https://housiey.com/blogs/?p=8016 | 搜尋結果內容（數值與 URL 的對應不確定） |
| IN-46 | Interior Cost for 2BHK House in India 2026 | Construction Estimator India | 2026 | 英 | https://constructionestimatorindia.com/?p=11246 | 搜尋結果內容（數值與 URL 的對應不確定） |
| IN-47 | Modular Kitchen Cost in Delhi: Budget to Luxury | DesignCafe | 2025–26 | 英 | https://www.designcafe.com/blog/modular-kitchen-interiors/modular-kitchen-cost-delhi/ | 搜尋結果內容 |
| IN-48 | Modular kitchen price per sqft, design and installation tips | Housing.com | 2025–26 | 英 | https://housing.com/news/modular-kitchen/ | 搜尋結果內容 |
| IN-49 | The Architects Act, 1972 (Act No. 20 of 1972)（As on 3rd December 2025） | India Code（法務部，政府） | 2025 | 英 | https://www.indiacode.nic.in/bitstream/123456789/1690/1/A1972-20.pdf | 搜尋結果內容 |
| IN-50 | The Unique Position Of The Architects Act, 1972 | Mondaq | 約 2021 | 英 | https://www.mondaq.com/india/construction-planning/1077872/the-unique-position-of-the-architects-act-1972 | 搜尋結果內容 |
| IN-51 | Scope Boundaries: Architect, Interior Designer & Contractor（Architects Act 1972, IIID Code, BOCW 1996 & RERA 2016） | Studio Matrx | 2026 | 英 | https://www.studiomatrx.org/guides/scope-boundaries-architect-designer-contractor-india | 搜尋結果內容 |
| IN-52 | COA announces suggestive amendments to the Architect's Act, 1972 | World Architecture | 不明 | 英 | https://worldarchitecture.org/architecture-news/efcph/coa-announces-suggestive-amendments-to-the-architect-s-act-1972.html | 搜尋結果內容（僅標題） |
| IN-53 | Can I call myself an interior architect? | Interior A to Z | 不明 | 英 | https://interioratoz.com/can-i-call-myself-an-interior-architect/ | 搜尋結果內容 |
| IN-54 | BIS QCO for the Plywood and Wooden Flush Door Shutters（Plywood face panels） | Aleph India | 2025 | 英 | https://alephindia.in/bis-qco-for-the-plywood-face-panels.php | 搜尋結果內容 |
| IN-55 | QCO on Wood Based Panels; Countdown Begins | Ply Reporter | 2025 | 英 | https://plyreporter.com/article/154006/current-issue | 搜尋結果內容 |
| IN-56 | New BIS Quality Control Orders implementations next month (February 2025) | MPR Kontakt（certification-india.com） | 2025-01 | 英 | https://certification-india.com/en/new-bis-quality-control-orders-implementations-next-month-february-2025 | 搜尋結果內容 |
| IN-57 | Quality control orders will stay | Sourcing Hardware | 2025–26 | 英 | https://sourcinghardware.net/quality-control-orders-will-stay/ | 搜尋結果內容（僅標題） |
| IN-58 | Compensation for defects in construction after possession under RERA | Housing.com | 不明 | 英 | https://housing.com/news/compensation-for-defects-in-construction-after-possession-under-rera/ | 搜尋結果內容 |
| IN-59 | What is builder warranty under RERA? | Housing.com | 不明 | 英 | https://housing.com/news/what-is-builder-warranty-under-rera | 搜尋結果內容 |
| IN-60 | Order 491/2023 | Bihar Real Estate Regulatory Authority（政府） | 2023 起 | 英 | https://rera.bihar.gov.in/Order/order-491-2023.pdf | 搜尋結果內容 |
| IN-61 | FDI policy rejig for border nations spur Rs 5k cr investment: DPIIT | Civilsdaily | 2026 | 英 | https://www.civilsdaily.com/news/fdi-policy-rejig-for-border-nations-spur-rs-5k-cr-investment-dpiit/ | 搜尋結果內容（數值與 URL 的對應為推定） |
| IN-62 | FDI Policy in India: Sectoral Caps, Routes and Recent Changes | GKToday | 2025–26 | 英 | https://www.gktoday.in/fdi-policy-in-india-sectoral-caps-routes-and-recent-changes/ | 搜尋結果內容（數值與 URL 的對應為推定） |
| IN-63 | FDI in India: Rules, Routes, Sectors & Compliance Guide 2026 | Altacit | 2026 | 英 | https://www.altacit.com/fdi-in-india-rules-routes-sectors-compliance-guide-2026/ | 搜尋結果內容 |
| IN-64 | The Five Year Defect Liability Period Under RERA: What Bengaluru Buyers Can Demand | PropNewz | 2026-06-13 | 英 | https://www.propnewz.com/blog/rera-defect-liability-5-years-bengaluru-buyer-2026-06-13 | 搜尋結果內容 |
| IN-65 | RERA structural defect 5 year builder complaint India | righttoinformation.wiki | 2026 | 英 | https://righttoinformation.wiki/rera-structural-defect-5-year-builder-complaint-india | 搜尋結果內容 |

**來源統計**

- 共 65 條
- 印度政府來源 2 條：IN-49、IN-60
- 印度媒體與印度業者來源 30 條以上：IN-08、IN-10、IN-14～IN-48、IN-55、IN-57～IN-59 等
- 印地語來源 0 條
- 日文頁面 1 條（IN-06，市調公司的翻譯頁，不算在地語言來源）
