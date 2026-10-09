# 越南（Vietnam，市場代碼 VN）室內設計與住宅裝修市場 — 研究筆記 r1（獨立三角驗證輪）

- 研究日期：2026-10-09
- 範圍：單一市場：越南（第三層新興市場；以台灣為基準）
- 搜尋語言：越南文、英文
- 幣別：一律保留來源原幣（VND、USD）與原面積單位；**未做匯率換算**（由中央統一處理）。每坪換算用 1 坪 = 3.3058 m²，僅在標示「推算」處使用。
- 獨立性：本輪未開啟 `04-research-notes/`、`05-report/` 下任何檔案。
- 架構前提（委託方提供）：越南需求仍以**新屋（bàn giao thô／hoàn thiện cơ bản）交屋後的首次裝修（fit-out）**為主，而非老屋翻修。本輪**沒有找到**交屋標準占比、屋齡分布的直接數據，因此這個前提在本筆記中屬於「間接佐證＋推論」，見 Q2。

---

## 0. 搜尋紀錄摘要（搜尋次數、在地語言搜尋次數、來源數）

| 項目 | 數值 |
|---|---|
| 嘗試搜尋次數 | 12 |
| 實際執行搜尋次數 | **10**（越南文 8、英文 2） |
| 未執行 | 2 次（IKEA、Nitori）：工具回覆「本回合全體代理共用的 WebSearch 配額（200 次）已用盡」。依指示未以 curl／第三方代理等方式繞過 |
| 是否達 brief 要求（≥15 次搜尋） | **未達**（10／15）。在地語言搜尋 ≥5 次：**已達**（8 次） |
| 來源數（列入第 8 節） | 43 筆；越南文 34 筆、英文 9 筆（在地語言來源 ≥5：**已達**） |
| 讀取方式 | WebFetch 不可用；全部為「搜尋結果內容」。只有標題能支撐的來源，標為「搜尋結果內容（僅標題）」 |
| 主要影響 | Q3 的零售與外資玩家、Q4、Q6、Q7、Q8、Q9、Q10 多數為「無資料」。缺口表附建議查詢與**待查證線索**（研究員背景知識，未經本輪驗證，**不得引用**） |

已執行的查詢（原文照列）：
1. `quy mô thị trường nội thất Việt Nam 2024 tỷ USD`（越，extended）
2. `Vietnam interior design market size Mordor IMARC 2024`（英）
3. `đơn giá thi công nội thất trọn gói chung cư 2025 triệu/m2`（越）
4. `chi phí làm nội thất căn hộ chung cư bao nhiêu tiền VnExpress`（越，extended）
5. `An Cường ACG doanh thu lợi nhuận 2024 2025`（越）
6. `CBRE Vietnam 2025 Hanoi HCMC new apartment launches absorption full year`（英，extended）
7. `thiết kế nội thất có cần chứng chỉ hành nghề Nghị định 175/2024`（越，extended）
8. `sửa chữa cải tạo bên trong công trình miễn giấy phép xây dựng Luật Xây dựng 2020 điều 89`（越）
9. `đơn giá thiết kế nội thất 2025 đồng/m2 chung cư nhà phố`（越）
10. `Bộ Xây dựng năm 2025 giao dịch căn hộ chung cư nhà ở riêng lẻ tổng lượng giao dịch`（越，extended）
11. `IKEA Vietnam store opening 2025 2026 online`（未執行：配額耗盡）
12. `Nitori Vietnam stores 2025 Ho Chi Minh Hanoi`（未執行：配額耗盡）

---

## 1. 市場關鍵結論（5–8 點）

1. **新屋是裝修需求的主要來源（推論＋間接佐證）**：2025 年全國「公寓＋獨棟住宅（căn hộ chung cư và nhà ở riêng lẻ）」成交 **138,025 筆**；另有土地（đất nền）成交 441,693 筆。全部不動產成交約 579,718 筆，年增約 7.7%〔VN-38〕。河內 2025 年新推出公寓**近 36,000 戶**，為史上第二高，僅次於 2019 年；全年售出 **34,760 戶**〔VN-25、VN-26〕。交屋標準（毛胚／基本完工）的占比與屋齡數據為「無資料」。
2. **南北供給失衡**：胡志明市 2025 上半年新推出公寓僅 **約 1,400 戶**（CBRE），上半年去化率 74%，前一年同期為 86%〔VN-27〕。Savills 統計 2025 年第三季成交 2,700 戶，去化率 51%〔VN-28〕。fit-out 需求在 2025 年明顯偏向北部，包含河內周邊的興安省文江（Văn Giang, Hưng Yên）大型案〔VN-26〕。
3. **房價高、裝修單價低**：2025 年一手公寓均價河內 **100 百萬 VND/m²**、胡志明市 **111 百萬 VND/m²**（Bộ Xây dựng，經 VnEconomy 轉引）〔VN-36〕。業者報價推算的公寓統包裝修約 **2.57–6.43 百萬 VND/m²**（70 m² 總價 180–450 百萬 VND）〔VN-11〕，約為一手房價每 m² 的 2.3%–6.4%（推算，【示意】，信心低）。
4. **市場規模沒有官方口徑，市調數字相差約 10 倍**：越南「家具」市場估計從 **14.7 億美元（2024，Mordor 舊版）**〔VN-02〕、**97.6 億美元（2025，Mordor 現行版）**〔VN-01〕，到 **150 億美元（2025，Ken Research「家具與室內設計」）**〔VN-10〕。本輪未找到「室內設計服務」「住宅翻修」「商業裝修」任何一桶的可靠規模，皆為「無資料」。
5. **產業重心在出口而非內需**：2024 年木材及木製品出口 **162.5 億美元**，年增超過 20%（海關數據，經 VnExpress）〔VN-03〕，遠大於任何內需估計。
6. **最大上市內裝材料／系統櫃業者 An Cường（ACG）轉向內需**：2024 年前三季稅後淨利 329.9 十億 VND，年增 32.3%（出口回溫帶動）〔VN-18〕；2025 年前三季營收 2,940.6 十億 VND，年增 6.4%〔VN-19〕。2025 全年營收超過 4,600 十億 VND、淨利 504 十億 VND 的說法未能綁定單一 URL（信心低）〔候選 VN-20〕。2025 年第三季出口營收年減 16%（美國關稅），內需成為主要動能〔候選 VN-20，信心低〕。
7. **室內設計本身幾乎不受執業證照管制（需專業人士最終確認）**：依《Nghị định 175/2024/NĐ-CP》第 73 條第 3 項 c 款，「不影響承重結構的裝修完成工作之設計、審查、監造」及「工程室內施工監造」，個人**不需**持執業證書（chứng chỉ hành nghề）〔VN-29、VN-31〕。依《Luật Xây dựng 2014》（2020 年修正）第 89 條第 2 項 g 款，不改變承重結構、使用功能、環境與安全的室內修繕可**免建築許可**〔VN-33、VN-34、VN-35〕。
8. **設計費低，且常與施工綁約**：業者公開報價約 **150,000–200,000 VND/m²**，有業者宣稱簽施工合約即「免 100% 設計費」（信心低）〔VN-16 等〕。推算設計費約占施工費 2.3%–7.8%（【示意】）。

---

## 2. 十節

### Q1 市場規模與成長

**結論**：越南沒有室內設計或住宅翻修的官方或公會口徑規模數字。現有數字都來自市調公司或媒體轉引，定義從「家具」「家具＋室內設計」「室內設計軟體」到「出口」都有，彼此不可比。在四桶之中，只有「家居零售」有（低信心）估計；「設計服務」「住宅翻修」「商業裝修」「建商精裝」皆為**無資料**。

**所有找到的來源（並列，不取平均）**

| 來源# | 數值 | 年份 | 原始定義 | 歸桶 | 現況/預測 | 信心 | URL |
|---|---|---|---|---|---|---|---|
| VN-02 | 1.47 十億 USD | 2024 | Mordor Intelligence「越南家具市場」（Dân trí 轉引；細部定義未於搜尋內容載明） | 家居零售 | 現況（市調估計）【示意】 | 低 | https://dantri.com.vn/bat-dong-san/vi-sao-nganh-noi-that-viet-nam-chua-ghi-dau-an-tren-the-gioi-20250607213731069.htm |
| VN-02 | 1.92 十億 USD（CAGR 5.33%，2024–2029） | 2029 | 同上 | 家居零售 | **預測** | 低 | 同上 |
| VN-01 | 9.76 十億 USD | 2025 | Mordor「Quy mô thị trường nội thất Việt Nam（Vietnam Furniture Market）」現行版；定義未於搜尋內容載明 | 家居零售（範圍可能較廣，待確認） | 現況（市調估計）【示意】 | 低 | https://www.mordorintelligence.com/industry-reports/vietnam-furniture-market |
| VN-01 | 10.47 十億 USD（2026）；14.87 十億 USD（2031） | 2026／2031 | 同上 | 家居零售 | **預測** | 低 | 同上 |
| VN-10 | 15.00 十億 USD；2020–2025 歷史 CAGR 5.83% | 2025 | Ken Research「Vietnam Furniture and Interior Design Market」（家具＋室內設計合併口徑） | 家居零售＋設計服務（混合，無法拆分） | 現況（市調估計）【示意】 | 低 | https://www.kenresearch.com/industry-reports/vietnam-furniture-and-interior-design-market.md |
| VN-10 | 21.82 十億 USD（CAGR 6.45%） | 2031 | 同上 | 混合 | **預測** | 低 | 同上 |
| VN-04／VN-05（候選，數字未能明確綁定 URL） | 國內木製家具消費 4–5 十億 USD；人均超過 20 USD／年 | 年份不明（推測為 2023 年前的舊數字） | 「各木業協會」估算之國內木製家具消費 | 家居零售 | 現況（協會估算）【示意】 | 低（算式內部不一致，見矛盾表） | https://congthuong.vn/thi-truong-do-noi-that-trong-nuoc-manh-dat-hua-cho-cac-doanh-nghiep-276811.html ／ https://vneconomy.vn/thi-truong-noi-that-viet-nhieu-tiem-nang.htm |
| VN-06 | 21.20 百萬 USD | 2024 | IMARC「Vietnam Interior Design **Software** Market」 | 其他（設計軟體，**非設計服務**） | 現況（市調估計） | 中 | https://www.imarcgroup.com/vietnam-interior-design-software-market |
| VN-06 | 39.90 百萬 USD（CAGR 7.28%，2025–2033） | 2033 | 同上（IMARC 已有 2026–2034 新版，數字可能已修訂） | 其他 | **預測** | 中 | 同上 |
| VN-07 | 1,278.4 百萬 USD | 2024 | IMARC「Vietnam Flooring Market」 | 其他（建材） | 現況（市調估計） | 中 | https://www.imarcgroup.com/vietnam-flooring-market |
| VN-08 | CAGR 5.40%（2024–2032），無規模值 | 2024–2032 | IMARC「Vietnam Home Furniture Market」 | 家居零售 | **預測** | 低 | https://imarcgroup.com/vietnam-home-furniture-market |
| VN-09 | CAGR 6.38%（2024–2032），無規模值 | 2024–2032 | IMARC「Vietnam Home Decor Market」 | 家居零售 | **預測** | 低 | https://imarcgroup.com/vietnam-home-decor-market |
| VN-03 | 16.25 十億 USD（年增超過 20%） | 2024 | 木材及木製品出口（Tổng cục Hải quan，經 VnExpress） | 其他（**出口**，非內需） | 現況【實際】 | 高 | https://vnexpress.net/bai-toan-18-ty-usd-cua-xuat-khau-go-noi-that-4843845.html |
| VN-01 | 13.436 十億 USD（年增 24.5%） | 2024 | Mordor 頁面引用之家具出口額 | 其他（出口） | 現況 | 中 | https://www.mordorintelligence.com/industry-reports/vietnam-furniture-market |
| — | **無資料** | — | 室內設計服務市場（設計費） | 設計服務 | — | — | — |
| — | **無資料** | — | 住宅翻修／裝修工程市場 | 住宅翻修 | — | — | — |
| — | **無資料** | — | 商業空間 fit-out 市場 | 商業裝修 | — | — | — |
| — | **無資料** | — | 建商精裝交屋產值 | 建商精裝 | — | — | — |

**住宅 vs 商業、新屋 vs 存量占比**：無資料。

**合理性檢查**（人口、GDP 本輪未搜尋，下列所用的人口約 1 億為背景知識，未經驗證）
- Mordor 舊版 1.47 十億 USD 換算人均約 15 USD；現行版 9.76 十億 USD 換算人均約 97 USD。同一機構改版後差 6.6 倍，年份只差一年，**不可能是真實成長**，應為定義或方法改變。
- 協會說法「人均超過 20 USD × 約 1 億人」約 20 億 USD，與同句的「4–5 十億 USD」不符（後者隱含人均 40–50 USD）。這個數字年份不明、算式不一致，降為低信心、不採用。
- Ken Research 的 15 十億 USD 與出口額（13–16 十億 USD）同一量級。若為內需，約占 GDP 數個百分點，對低中所得國家的「家具＋設計」來說偏高。研判可能混入生產端或出口口徑（推論，無法以搜尋內容證實）。
- 小結：越南內需「家居零售」規模在 1.5–15 十億 USD 之間，區間取決於定義，**沒有可用的點估計**。報告中如需引用，請標明版次與定義，並以【示意】處理。

**成長**：只有市調公司的預測 CAGR，介於 5.33%–7.28%（不同口徑），**皆為預測**〔VN-02、VN-06、VN-08、VN-09、VN-10〕。

---

### Q2 需求結構

**結論**：需求引擎是一手公寓交屋，尤其是 2025 年河內的創紀錄供給，胡志明市則供給受限。屋齡、交屋標準、翻修週期、工期四項本輪皆「無資料」。裝修單價只有業者報價可推算，信心低。

#### 2a. 新屋供給、成交（新屋 vs 中古）

| 指標 | 數值 | 單位 | 年份 | 來源# | 原始定義 | 歸桶 | 標示 | 信心 |
|---|---|---|---|---|---|---|---|---|
| 全國公寓＋獨棟住宅成交 | 138,025 | 筆 | 2025 | VN-38 | Bộ Xây dựng 彙整各地 Sở Xây dựng 回報之「成功交易」（Báo Chính phủ 轉引）；**未區分新屋／中古** | 其他（需求驅動） | 【實際】 | 中 |
| 全國土地（đất nền）成交 | 441,693 | 筆 | 2025 | VN-38 | 同上 | 其他 | 【實際】 | 中 |
| 全國不動產成交合計 | 約 579,718（年增約 7.7%） | 筆 | 2025 | VN-38 | 同上 | 其他 | 【實際】 | 中 |
| 2025Q2 公寓＋獨棟成交 | 34,461（季增 2.61%、年增 33.1%） | 筆 | 2025Q2 | VN-37（官方）；VN-39 標題「年增 33%」佐證 | Bộ Xây dựng 季度公布 | 其他 | 【實際】（雙源） | 高 |
| 2025Q1 公寓＋獨棟成交 | 33,585（季增 32%） | 筆 | 2025Q1 | VN-41（候選，未能明確綁定） | 各地 Sở Xây dựng 資料 | 其他 | 【示意】 | 低 |
| 河內新推出公寓 | 近 36,000（史上第二高，僅次 2019） | 戶 | 2025 | VN-25；VN-26 | CBRE 河內公寓（condo）一級市場新推出 | 其他 | 【實際】 | 高 |
| 河內公寓售出 | 34,760 | 戶 | 2025 | VN-25；VN-26 | CBRE | 其他 | 【實際】（雙源，同出 CBRE） | 高 |
| 河內 Q4 新案平均去化率 | 79 | % | 2025Q4 | VN-26 | CBRE（經 Việt Nam News） | 其他 | 【示意】 | 中 |
| 興安文江（Văn Giang, Hưng Yên）占河內新供給 | Q4 超過 60%；全年近 40% | % | 2025 | VN-26 | CBRE 把行政上屬興安省的文江大型案計入「河內市場」 | 其他 | 【示意】 | 中 |
| 河內單價超過 120 百萬 VND/m² 新推案 | 近 4,000（創紀錄） | 戶 | 2025 | VN-26 | CBRE | 其他 | 【示意】 | 中 |
| 胡志明市新推出公寓 | 約 1,400（其中 Q2 約 1,000） | 戶 | 2025H1 | VN-27 | CBRE | 其他 | 【示意】 | 中 |
| 胡志明市一級去化率 | 74（2024H1 為 86） | % | 2025H1 | VN-27 | CBRE | 其他 | 【示意】 | 中 |
| 胡志明市成交 | 2,700；去化率 51% | 戶；% | 2025Q3 | VN-28 | Savills（經 The Investor） | 其他 | 【示意】 | 中 |
| 胡志明市（舊市界）下半年新供給 | 約 6,000 | 戶 | 2025H2 | VN-28（候選） | CBRE **預測**；「former HCMC」指 2025 年行政區合併前的舊市界（合併細節為背景知識，待確認） | 其他 | **預測** | 低 |
| 新屋 vs 中古成交占比 | **無資料** | — | — | — | — | — | — | — |

註：搜尋摘要另有一組「全年新供給超過 3,800 戶、較 2024 年減少 40%、全年成交 5,852 戶（成交大於新供給）」，但無法確認區域與產品類別，也無法綁定 URL，列入矛盾表、不採用。

#### 2b. 房價（作為裝修預算分母）
- 一手公寓平均售價：河內 **100 百萬 VND/m²**、胡志明市 **111 百萬 VND/m²**（2025，Bộ Xây dựng 數據，經 VnEconomy）〔VN-36〕，【實際】，信心中。
- 推論：首購族把大部分預算用在房價與房貸，裝修預算受到擠壓（推論，無直接數據）。

#### 2c. 屋齡、交屋標準、翻修週期
- 30 年以上屋齡占比：**無資料**（未能搜尋；建議以 GSO 2019 人口與住宅普查／2024 年期中調查取得）。
- 交屋標準（bàn giao thô vs hoàn thiện cơ bản vs 全裝修）占比：**無資料**。
- 翻修週期、每案平均花費（全國）：**無資料**。
- 關於「需求以新屋 fit-out 為主」的委託方前提，本輪的**間接佐證**有：(i) 2025 年河內一年新推出、售出各約 3.5 萬戶〔VN-25〕；(ii) ACG 在出口受關稅衝擊時由內需撐起營收〔候選 VN-20〕；(iii) 業者報價頁一律以「公寓（chung cư）統包」與「臥室數套餐」為單位〔VN-11～VN-15〕。三者都不是直接占比數據，**屬推論**。

#### 2d. 住宅裝修單價（đơn giá thi công nội thất trọn gói）

| 指標 | 數值（原幣、原單位） | 推算每 m² | 推算每坪 | 年份 | 來源# | 原始定義 | 歸桶 | 標示 | 信心 |
|---|---|---|---|---|---|---|---|---|---|
| 70 m² 公寓室內裝修總價區間 | 180–450 百萬 VND／戶 | 2.57–6.43 百萬 VND/m² | 8.50–21.25 百萬 VND/坪 | 2025–2026（報價頁） | VN-11（標題為 70m² 成本頁，摘要歸屬「另一業者」；候選 VN-12） | 業者報價；未說明是淨面積（thông thủy）還是牆中心面積（tim tường） | 住宅翻修（新屋 fit-out） | 【示意】 | 低 |
| 70 m² 統包（工廠直營價） | 250–330 百萬 VND／戶 | 3.57–4.71 百萬 VND/m² | 11.81–15.58 百萬 VND/坪 | 2025–2026 | VN-11／VN-12（候選） | 同上 | 住宅翻修 | 【示意】 | 低 |
| 一房（1PN）套餐 | 「省錢」40–60；「標準」80–120 百萬 VND | — | — | 2024–2026 | VN-13／VN-14／VN-15（候選，未能綁定） | 業者報價套餐 | 住宅翻修 | 【示意】 | 低 |
| 兩房（2PN）套餐 | 「省錢」80–100；「標準」120–180 百萬 VND | — | — | 同上 | 同上 | 同上 | 住宅翻修 | 【示意】 | 低 |
| 三房（3PN）套餐 | 「省錢」90–120；「標準」150–220 百萬 VND | — | — | 同上 | 同上 | 同上 | 住宅翻修 | 【示意】 | 低 |
| 另一組「基本家具」報價 | 1PN 70–120；2PN 120–180；3PN 170–250 百萬 VND | — | — | 同上 | 同上 | 範圍可能含更多固定木作 | 住宅翻修 | 【示意】 | 低 |
| 換材料造成的價差 | 50–120 百萬 VND（同一設計） | — | — | 同上 | 同上 | — | 住宅翻修 | 【示意】 | 低 |
| 石膏板天花 | 180,000–250,000 VND/m² | — | — | 同上 | 同上 | 單項工料 | 住宅翻修 | 【示意】 | 低 |

- 基本／中階／高階分級：來源沒有正式分級。若以 70 m² 區間的下限、工廠統包、上限作為代理，分別約為 **2.57／3.57–4.71／6.43 百萬 VND/m²**（推算，【示意】，信心低）。
- 與房價比：2.57–6.43 ÷ 100（河內）＝ 2.6%–6.4%；÷ 111（胡志明市）＝ 2.3%–5.8%（推算）。
- **河內新案 fit-out 需求示意**：34,760 戶〔VN-25〕× 每戶 180–450 百萬 VND〔VN-11〕≈ **6.26–15.64 兆 VND／年**。假設所有售出戶在一年內完成裝修，且平均裝修規模約等於 70 m² 報價。**純示意**，不可作為市場規模。

#### 2e. 設計費行情（đơn giá thiết kế nội thất）

| 指標 | 數值 | 推算每坪 | 年份 | 來源# | 原始定義 | 標示 | 信心 |
|---|---|---|---|---|---|---|---|
| 公寓設計費（單一業者） | 150,000 VND/m²，不限修改次數；簽施工約可免 100% 設計費 | 495,870 VND/坪 | 2025 | 搜尋摘要（未能綁定 URL） | 業者自報；設計費＝單價 × 面積 | 【示意】 | 低 |
| 現代、北歐、極簡風格設計費 | 200,000 VND/m² | 661,160 VND/坪 | 2025–2026 | VN-11～VN-15 候選（未能綁定） | 業者報價 | 【示意】 | 低 |
| 辦公室設計費 | 150,000–200,000 VND/m²（面積越大單價越低） | — | 年份不明 | VN-16 | 自發布頁面（coda.io） | 【示意】 | 低 |
| 設計費占施工費比 | 約 2.3%–7.8% | — | 推算 | 由上兩表推算 | 150k–200k ÷ 2.57–6.43 百萬 | 【示意】 | 低 |

#### 2f. 典型工期
- **無資料**。

---

### Q3 產業結構與主要玩家

**結論**：本輪只對 An Cường（ACG）取得可查證數據。AA Corporation（Nhà Xinh）、Hòa Phát 家具、JYSK、IKEA、Index Living Mall、Nitori、Coteccons／Ricons／Unicons，以及台日韓業者，都因搜尋配額耗盡而為「無資料」。公司家數與集中度同為「無資料」。

#### An Cường（CTCP Gỗ An Cường，HOSE：ACG）— 木作板材（MDF／美耐板）、系統櫃、室內木作

| 指標 | 數值 | 單位 | 期間 | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|---|
| 淨營收 | 2,764（較 2023 年同期增加 154） | 十億 VND | 2024 年前三季 | VN-18 | 【實際】 | 高 |
| 稅後淨利 | 329.9（年增 32.3%，公司解釋為出口回溫） | 十億 VND | 2024 年前三季 | VN-18（標題含 32.3%） | 【實際】 | 高 |
| 營收 | 約 4,000（年增 6%）；超過計畫 5% | 十億 VND | 2024 全年 | 未能綁定（候選 VN-21） | 【示意】 | 低 |
| 淨利 | 420（年增 2%）；達成計畫 96% | 十億 VND | 2024 全年 | 同上 | 【示意】 | 低 |
| 淨營收 | 961（年減 6%） | 十億 VND | 2025Q2 | VN-17 | 【實際】 | 中 |
| 稅後淨利 | 137.94（年增 16.77%），含約 36 十億 VND 出售聯屬公司股權收益 | 十億 VND | 2025Q2 | VN-17（標題含 137.94／16.77%） | 【實際】 | 高 |
| 營收 | 2,940.6（年增 6.4%） | 十億 VND | 2025 年前三季 | VN-19 | 【實際】 | 中 |
| 稅後淨利 | 358.2（年增 8.6%）；約達年度計畫 80% | 十億 VND | 2025 年前三季 | VN-19（標題含 80%） | 【實際】 | 中 |
| 出口營收 | 年減 16%（美國關稅）；內需為主要動能（Vietcap 觀點） | % | 2025Q3 | 候選 VN-20 | 【示意】 | 低 |
| 營收 | 超過 4,600（年增 16%）；超過計畫 14% | 十億 VND | 2025 全年 | 候選 VN-20 | 【示意】 | 低 |
| 淨利 | 504（年增 20%）；超過計畫 12% | 十億 VND | 2025 全年 | 候選 VN-20 | 【示意】 | 低 |

- 內部一致性：2024 全年約 3,970（由 2025 年年增 16% 反推）減前三季 2,764，得 2024Q4 約 1,206 十億 VND。2025 全年 4,600 減前三季 2,940.6，得 2025Q4 約 1,660 十億 VND，等於第四季年增約 38%。數字之間可以對得上，但第四季增幅偏大，**需以 HOSE 經審計財報確認**。
- 近三年事件（僅有標題可用，細節待查）：關閉平新（Bình Tân）一個分公司〔VN-22〕；擬將子公司 1,474 萬股出售給兩名個人〔VN-23〕；擬對子公司投入「上千億 VND」〔VN-24〕；某年度「營收創新高，同時提列呆帳約 300 十億 VND」〔VN-21〕，推論為工程或建商通路的應收帳款風險（推論）；即將發放 196 十億 VND 股利〔VN-19〕。
- 歸桶：其他（建材／板材＋系統櫃製造），兼具建商精裝供應角色（推論）。

#### 其他玩家
- **Viettel Construction（CTR）**：VnExpress 標題「Viettel Construction ra mắt mảng nội thất」（推出室內裝修業務）〔VN-42〕。年份依文章編號推斷約為 2023 年，**需確認**。歸桶：住宅翻修（設計施工）。電信國企系統跨入住宅裝修是值得追蹤的競爭者型態。
- AA Corporation／Nhà Xinh、Hòa Phát 家具、JYSK、IKEA、Index Living Mall、Nitori、Hanssem、Coteccons／Ricons／Unicons、台資室內裝修業者：**無資料**（見缺口表與待查證線索）。
- 平台：**無資料**。
- 公司家數與集中度：**無資料**。

---

### Q4 通路與獲客

**結論**：**無資料**（Facebook 社團、TikTok、平台用戶數、GMV、抽成皆未能搜尋）。
- 僅有的間接觀察：消費者會在論壇詢價，例如 VOZ 討論串「Chi phí làm Nội Thất 1 Căn Hộ Chung Cư là bao nhiêu?」〔VN-15〕；業者以「設計費全免＋簽施工約」「工廠直營價（giá tại xưởng）」「依臥室數的套餐價」作為獲客手法〔VN-12、VN-11～VN-15〕。以上皆為推論，信心低。
- 部分業者在 Behance、coda.io、GitLab 等第三方平台自建 SEO 頁面（見搜尋結果）〔VN-16〕，顯示 SEO 與內容行銷競爭激烈（推論）。

---

### Q5 法規與證照（需專業人士最終確認）

**結論**：只要不動到承重結構、不改變使用功能，室內設計與裝修監造**不需個人執業證書**，室內修繕也**免建築許可**。涉及結構、機電設計，或改變外觀（位於有建築管理要求的都市臨街面）時，需要相應證照或許可。

| 主題 | 法規（越南文原名） | 主管機關 | 內容摘要 | 來源# | 信心 |
|---|---|---|---|---|---|
| 個人執業證書（chứng chỉ hành nghề）豁免 | 《Nghị định 175/2024/NĐ-CP》（取代《Nghị định 15/2021/NĐ-CP》）第 73 條第 3 項 c 款 | 政府頒布；Bộ Xây dựng（Cục Quản lý hoạt động xây dựng 負責指引） | 以下工作個人**不需**執業證書：「不影響承重結構的工程完成工作（抹灰、貼磚、油漆、裝門及類似工作）之設計、設計審查、監造」，以及「**giám sát thi công nội thất công trình**（工程室內施工監造）」 | VN-29（法規全文）、VN-31（主管機關簡報）、VN-30（175 與 15 差異比較） | 中 |
| 需要證照的情形 | 同上，附錄 VII（Phụ lục VII）證照類別 | 同上 | 設計涉及承重結構（拆承重牆、改柱、樑、樓板）時需「結構設計」證照；涉及機電、給排水、空調系統可能需「機電設計」證照；擔任設計主持（chủ nhiệm／chủ trì）另有要求 | VN-29（摘要推論） | 低 |
| 組織能力（chứng chỉ năng lực） | 《Nghị định 175/2024/NĐ-CP》 | Bộ Xây dựng／Sở Xây dựng | 175 對組織的「建設活動能力」有新規定（細節未取得） | VN-32（僅標題） | 低 |
| 室內修繕的建築許可豁免 | 《Luật Xây dựng 2014》（Luật số 50/2014/QH13），2020 年修正（Luật số 62/2020/QH14）第 89 條第 2 項 g 款 | Bộ Xây dựng；地方 Sở Xây dựng／UBND | 「工程內部的修繕、改造、設備安裝，不改變承重結構、不改變使用功能、不影響環境與工程安全」者**免** giấy phép xây dựng。仍須符合已核定的建設規劃、**防火防爆（PCCC）**及環保要求。改變外觀且臨接有建築管理要求之都市道路者**不在**豁免之列 | VN-33、VN-34 | 中 |
| 主管機關函釋 | 《Công văn 6057/BXD-HĐXD》（2020） | Bộ Xây dựng | Bộ Xây dựng 針對修繕、改造是否需許可的答覆，方向同上 | VN-35 | 中 |
| 職業培訓證書（非法定證照） | — | 民間培訓機構 | 市場上有「室內設計職業證書（Chứng chỉ nghề thiết kế nội thất）」，屬**培訓結業證書，不是法定執業證照**（推論） | VN-43（僅標題） | 低 |
| 《Luật Nhà ở 2023》、《Luật Kinh doanh bất động sản 2023》 | — | — | **無資料**（本輪未能搜尋） | — | — |
| 消防：PCCC 法（2024）與施行細則 | — | — | **無資料**（僅知室內修繕免許可時仍須符合 PCCC，見 VN-33） | — | — |
| 公寓管理規約（Quy chế quản lý, sử dụng nhà chung cư）對裝修的限制 | — | — | **無資料** | — | — |
| 2023–2026 修法 | 《Nghị định 175/2024》取代《Nghị định 15/2021》 | — | 已確認〔VN-30〕；其他修法**無資料**（另見待查證線索：新《Luật Xây dựng》修訂） | VN-30 | 中 |

> 本節所有法規結論均**需專業人士最終確認**。條文款次依 2014 年版轉述；2020 年修正後款次是否變動，未能逐字核對（VN-33、VN-34 依 2014 年版引用）。
> 法定證照與協會認證的區分：本輪**未找到**越南室內設計的協會認證制度（如 VIDA 類組織），只見到培訓機構的結業證書〔VN-43〕。

---

### Q6 消費者保護與糾紛

**結論**：**無資料**（本輪未能搜尋）。合約範本、訂金慣例、保固期、履約保證、Cục Cạnh tranh và Bảo vệ người tiêu dùng／VICOPRO 投訴統計、常見詐騙型態，全部待補。
- 僅有的間接資訊：業者報價頁提醒「釐清是否含 3D 設計、施工、保固、水電；追加費用政策」〔VN-11～VN-15，候選〕，顯示**追加費（phát sinh）**與套餐範圍不清是常見爭議點（推論，信心低）。

---

### Q7 外資／台資進入規則

**結論**：**無資料**（本輪未能搜尋）。WTO 建設服務承諾、《Luật Đầu tư 2020》市場准入清單、外國承包商許可（giấy phép hoạt động xây dựng cho nhà thầu nước ngoài）、工作許可（《Nghị định 152/2020》及後續修正）、台日韓業者案例，全部待補（見缺口表待查證線索）。

---

### Q8 消費者行為

**結論**：**無資料**（首購族比例、各所得層預算、決策歷程、付款階段、融資，皆未能搜尋）。
- 間接資訊：業者以臥室數分的「省錢／標準」套餐，2PN 為 80–180 百萬 VND〔VN-13～VN-15，候選〕，推論是針對新屋首購族、年輕家庭的入門市場（信心低）。
- 河內 2025 年單價超過 120 百萬 VND/m² 的新推案近 4,000 戶〔VN-26〕，顯示高端客群在擴大，是設計附加價值較高的區隔（推論）。

---

### Q9 人才與工班

**結論**：**無資料**。設計科系畢業人數、設計師與監工薪資、木工、泥作、水電師傅 2025 年日薪、缺工情況，全部待補。

---

### Q10 材料供應鏈與價格

**結論**：本地板材與系統櫃龍頭為 An Cường（ACG，見 Q3）。其餘品牌、進口依賴（中國）、2022–2026 價格漲幅皆為「無資料」。
- 地板市場：1,278.4 百萬 USD（2024，IMARC 定義，市調估計）〔VN-07〕，歸桶「其他（建材）」，信心中。
- 越南是全球主要家具製造與出口國：木材及木製品出口 16.25 十億 USD（2024）〔VN-03〕。對台灣集團而言，**採購端（OEM／ODM）**的意義大於越南內需（推論）。
- ACG 2025Q3 出口營收年減 16%，起因為美國關稅〔候選 VN-20，信心低〕。出口受阻可能讓產能轉向內需，加劇內需板材與系統櫃的價格競爭（推論）。
- Viglacera、Prime、Đồng Tâm、INAX（LIXIL VN）、TOTO VN、Dulux、Jotun：**無資料**。

---

## 3. 橫向比較表一列

| 市場 | 人均 GDP（美元，年） | 住宅翻修市場規模 | 室內設計服務市場 | 住宅裝修單價（每 m²，基本／中階／高階） | 設計費行情 | 30 年以上屋齡占比 | 中古屋交易占比 | 執業管制（設計師／承包商） | 外資可 100% 持股？ | 主要平台 | 前 3 大玩家 | 信心 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 越南 | 無資料（本輪未搜尋） | 無資料（僅有家具市場市調估計 1.47–15.00 十億 USD，2024–2025，定義不一，VN-01／VN-02／VN-10） | 無資料（IMARC「室內設計**軟體**」21.20 百萬 USD，2024，VN-06，不屬設計服務） | 公寓統包推算：約 2.57／3.57–4.71／6.43 百萬 VND/m²（70 m² 報價 180–450 百萬 VND，VN-11，【示意】） | 150,000–200,000 VND/m²；簽施工約常免設計費（VN-16 等，【示意】，低）；推算約占施工費 2.3%–7.8% | 無資料 | 無資料 | 設計師：不涉結構的室內設計與裝修監造免個人執業證（Nghị định 175/2024 Đ73.3，VN-29／VN-31；需專業人士最終確認）／承包商：無資料 | 無資料 | 無資料 | An Cường（ACG）；其餘無資料 | 低 |

---

## 4. 台灣比較錨點原始輸入

| 錨點 | 越南原始值 | 年份 | 來源# | 備註 |
|---|---|---|---|---|
| 住宅翻修市場規模 | 無資料 | — | — | 只有「家具」市調估計（1.47／9.76／15.00 十億 USD），不屬住宅翻修桶，不建議代用 |
| 人口 | 無資料（本輪未搜尋） | — | — | 待中央以 GSO 數據補入 |
| 名目 GDP | 無資料（本輪未搜尋） | — | — | 同上 |
| 住宅裝修單價（每 m²） | 2.57–6.43 百萬 VND/m²（工廠統包 3.57–4.71） | 2025–2026 | VN-11／VN-12 | 業者報價推算；面積口徑不明；【示意】，信心低 |
| 設計費占工程費比 | 約 2.3%–7.8%（推算） | 2025–2026 | VN-16、VN-11 等 | 設計費常因簽施工約而免收，實際有效費率可能趨近 0（推論） |
| 設計公司家數 | 無資料 | — | — | — |
| 平台滲透率 | 無資料 | — | — | — |
| （補充）一手公寓均價 | 河內 100／胡志明市 111 百萬 VND/m² | 2025 | VN-36 | 可作為「裝修單價 ÷ 房價」的錨點：約 2.3%–6.4% |

---

## 5. 對台灣中型集團（璞石：宜蘭＋台北信義；裝修＋不動產＋家居零售）的 3–5 點啟示

1. **越南是「新屋首次裝修」市場，不是老屋翻修市場**（推論，交屋標準與屋齡數據待補）。可參考的模式是「建商合作＋大型新案周邊樣品屋與展示門市」，而不是台灣式的老屋翻新。2025 年河內新推出近 36,000 戶，其中近 40% 集中在興安文江大型案〔VN-25、VN-26〕，需求在地理上高度集中，可以「跟案」方式切入。
2. **大眾市場單價與設計費都偏低，台灣設計溢價只適合高端區隔**。統包約 2.57–6.43 百萬 VND/m²，設計費 150,000–200,000 VND/m² 且常被免收〔VN-11、VN-16〕；入門市場是套餐化、工廠價競爭。較合適的目標是河內 2025 年近 4,000 戶、單價超過 120 百萬 VND/m² 的高端新案〔VN-26〕。
3. **越南更適合作為家居零售的供應基地，而非優先進入的市場**。木材及木製品出口 16.25 十億 USD（2024）〔VN-03〕，加上美國關稅壓力下 ACG 等業者轉向內需〔候選 VN-20〕，對璞石家居零售線而言，越南 OEM／ODM 採購的議價空間可能擴大（推論）。
4. **法規對非結構性室內設計相對寬鬆**（免個人執業證、免建築許可〔VN-29、VN-33〕），進入門檻低，但也代表在地競爭者眾多、品質參差。外資持股、外國承包商許可、工作許可本輪無資料，跨境前**必須取得在地法律意見**（需專業人士最終確認）。
5. **資料可得性極低，跨境決策前應先做實地調查**：拜訪河內、胡志明市的建商與 ACG 展示中心，蒐集 10–20 份真實報價與合約，以補足單價、工期、付款階段、糾紛型態的缺口。現有規模數字在不同來源間差到 10 倍，不宜用於商業計畫。

---

## 6. 矛盾表與缺口表

### 6a. 矛盾表（同指標差異 >30%）

| 指標 | 來源 1 | 來源 2 | 差異原因（定義／年份／方法） | 裁決 |
|---|---|---|---|---|
| 越南家具市場規模 | VN-02：1.47 十億 USD（2024，Mordor 舊版，Dân trí 轉引） | VN-01：9.76 十億 USD（2025，Mordor 現行版） | 同一機構改版，差 6.6 倍；年份只差一年，不足以解釋；應為**定義或方法改變**（可能納入更廣品類或生產端） | 兩者都不作點估計；引用時必須附版次；列為【示意】區間；**不取平均** |
| 越南家具（＋室內設計）市場 | VN-01：9.76 十億 USD（2025，家具） | VN-10：15.00 十億 USD（2025，家具＋室內設計） | **定義**不同：Ken Research 含室內設計，差 54% | 不可比；分桶並列，不合併 |
| 國內家具消費 | VN-04／VN-05（候選）：4–5 十億 USD，人均超過 20 USD（年份不明） | VN-02：1.47 十億 USD（2024） | **年份**不明（推測 2023 年前）；**定義**為木製家具國內消費 vs 市調零售口徑；且來源 1 內部算式不一致（20 USD × 約 1 億人約 20 億 USD） | 來源 1 降為低信心、不採用 |
| 胡志明市 2025H1 新推出公寓 | VN-27：約 1,400 戶（CBRE） | 另一報告：3,353 戶，全部為高端（搜尋摘要，無法綁定 URL） | **定義**：CBRE 只計新開盤；另一來源可能含既有專案新分期或不同市界 | 採 CBRE，以便與河內同口徑 |
| 2025Q2 住宅成交年增率 | VN-37：年增 33.1%（Bộ Xây dựng 官方；VN-39 佐證年增 33%） | VN-40：「年增超過 116%」（Tin nhanh Chứng khoán 標題） | **資料來源與口徑**不同（後者可能為協會或特定市場統計，僅有標題可用） | 採 Bộ Xây dựng 官方數據 |
| 2025 河內新供給 | VN-25：近 36,000 戶（CBRE 公寓） | 搜尋摘要：全年超過 3,800 戶、年減 40%、成交 5,852 戶（區域與類別不明） | **定義**：後者可能是別的城市或產品類別（如低層住宅、胡志明市） | 採 CBRE；後者不採用 |
| 一房裝修預算 | 「省錢」套餐 40–60 百萬 VND | 「基本家具」70–120 百萬 VND | **定義**：套餐範圍（活動家具 vs 含固定木作與完成面）不同 | 並列；都只是報價示意 |
| （差異 <30%，僅註記）2024 年出口 | VN-03：16.25 十億 USD（木材及木製品，海關） | VN-01：13.436 十億 USD（Mordor 引用的家具出口） | 定義：前者含木片、木粒、板材等；差約 21% | 不入正式矛盾；引用時須註明口徑 |

### 6b. 缺口表

| 項目 | 試過的搜尋 | 建議取得方式 | 待查證線索（研究員背景知識，**未經本輪驗證，不得引用**） |
|---|---|---|---|
| 設計服務、住宅翻修、商業裝修、建商精裝市場規模 | 查詢 #1、#2 | GSO 營建業產值細分；VIFOREST／HAWA 國內市場報告；Euromonitor；建議查詢 `quy mô thị trường thi công nội thất Việt Nam`、`Vietnam fit-out market size` | — |
| 交屋標準占比（bàn giao thô vs hoàn thiện cơ bản） | 無（配額耗盡） | 查詢 `bàn giao thô hoàn thiện cơ bản tỷ lệ dự án 2025`；CBRE／Savills／DKRA 季報 | — |
| 30 年以上屋齡占比、住宅存量 | 無 | GSO《Tổng điều tra dân số và nhà ở 2019》與 2024 年期中調查 | — |
| 工期、付款階段、訂金 | 查詢 #3、#4 僅取得報價 | 查詢 `tiến độ thanh toán hợp đồng thi công nội thất đặt cọc` | — |
| 胡志明市 2025 全年供給與去化 | 查詢 #6 | CBRE「HCMC Figures Q4 2025」、Savills、DKRA 2025 年報 | 2025-07-01 起省級合併，胡志明市與平陽、巴地頭頓合併，數據口徑分為「新／舊市界」（待驗證） |
| IKEA、Nitori、JYSK、Index Living Mall、AA／Nhà Xinh、Hòa Phát 家具 | 查詢 #11、#12（未執行） | 查詢 `IKEA Việt Nam 2025`、`Nitori Việt Nam cửa hàng`、`JYSK Việt Nam số cửa hàng`、`AA Corporation doanh thu` | IKEA 約於 2025 年前後宣布進入越南（線上先行？）；Nitori 已在越南展店；JYSK 已有數十家門市（皆待驗證） |
| Coteccons／Ricons／Unicons fit-out；台日韓業者；募資、併購、倒閉 | 無 | 查詢 `Coteccons fit-out nội thất doanh thu`、`台商 越南 室內裝修`、`Hanssem Vietnam` | — |
| ACG 經審計全年財報 | 查詢 #5（全年數字未綁定） | HOSE 公告與 ACG 投資人關係頁 2024、2025 年報 | — |
| 《Luật Nhà ở 2023》、《Luật KDBĐS 2023》對交屋與裝修的影響 | 無 | thuvienphapluat.vn 全文 | 兩法提前於 2024-08-01 施行（待驗證） |
| PCCC 法（2024）與施行細則對 fit-out 的要求 | 查詢 #8（只取得「免許可仍須符合 PCCC」） | 查詢 `Luật Phòng cháy chữa cháy và cứu nạn cứu hộ 2024 cải tạo nội thất` | 新 PCCC 法自 2025-07-01 施行，另有施行細則《Nghị định 105/2025》（待驗證） |
| 2025–2026 《Luật Xây dựng》修訂、許可豁免是否改變 | 無 | chinhphu.vn、quochoi.vn | 國會可能已於 2025 年通過新建設法、2026 年施行（待驗證） |
| 公寓裝修管理規約 | 無 | Bộ Xây dựng《Thông tư》關於公寓管理使用規則 | — |
| 消保：合約、保固、投訴統計 | 無 | 查詢 `khiếu nại thi công nội thất người tiêu dùng`；Bộ Công Thương 年報 | 《Luật Bảo vệ quyền lợi người tiêu dùng 2023》自 2024-07-01 施行；主管機關為 Bộ Công Thương 轄下 Cục Cạnh tranh và Bảo vệ người tiêu dùng（待驗證） |
| 外資持股、承包商許可、工作許可 | 無 | WTO 越南服務減讓表（建設服務 CPC 511–518）；《Luật Đầu tư 2020》＋《Nghị định 31/2021》；《Nghị định 175/2024》外國承包商章節 | 越南的 WTO 承諾自 2009 年起允許建設服務 100% 外資（待驗證）；工作許可規則由《Nghị định 152/2020》經《Nghị định 70/2023》修正，2025 年可能由新法令取代（待驗證） |
| 消費者行為（Facebook 社團、TikTok、融資） | 無 | 查詢 `group Facebook review nội thất chung cư`、`vay sửa nhà ngân hàng lãi suất 2025` | — |
| 設計師薪資、師傅日薪 | 無 | 查詢 `lương thiết kế nội thất 2025`、`giá nhân công thợ mộc thợ hồ 2025 ngày` | — |
| 材料品牌與 2022–2026 漲價 | 無 | 查詢 `giá vật liệu xây dựng hoàn thiện tăng 2025`；Viglacera、Đồng Tâm 年報 | — |
| 人均 GDP、人口、名目 GDP | 無 | GSO（gso.gov.vn／nso.gov.vn）2025 年社經報告 | 2025 年人均 GDP 約 5,000 USD 上下；人口約 1.01 億（待驗證） |

---

## 7. 關鍵指標 CSV

```
market,metric,value,unit,year,source_id,source_url,definition,confidence
VN,家具市場規模（Mordor 舊版）,1.47,十億USD,2024,VN-02,https://dantri.com.vn/bat-dong-san/vi-sao-nganh-noi-that-viet-nam-chua-ghi-dau-an-tren-the-gioi-20250607213731069.htm,Mordor越南家具市場經Dân trí轉引；定義未載；家居零售桶；市調估計,low
VN,家具市場規模預測（Mordor 舊版）,1.92,十億USD,2029F,VN-02,https://dantri.com.vn/bat-dong-san/vi-sao-nganh-noi-that-viet-nam-chua-ghi-dau-an-tren-the-gioi-20250607213731069.htm,預測；CAGR 5.33% 2024-2029,low
VN,家具市場規模（Mordor 現行版）,9.76,十億USD,2025,VN-01,https://www.mordorintelligence.com/industry-reports/vietnam-furniture-market,Mordor越南家具市場現行版；定義未載；與舊版差6.6倍,low
VN,家具市場規模預測（Mordor 現行版）,14.87,十億USD,2031F,VN-01,https://www.mordorintelligence.com/industry-reports/vietnam-furniture-market,預測；2026年為10.47,low
VN,家具與室內設計市場規模（Ken Research）,15.00,十億USD,2025,VN-10,https://www.kenresearch.com/industry-reports/vietnam-furniture-and-interior-design-market.md,家具＋室內設計合併口徑；市調估計,low
VN,家具與室內設計市場預測（Ken Research）,21.82,十億USD,2031F,VN-10,https://www.kenresearch.com/industry-reports/vietnam-furniture-and-interior-design-market.md,預測；CAGR 6.45%,low
VN,室內設計軟體市場,21.20,百萬USD,2024,VN-06,https://www.imarcgroup.com/vietnam-interior-design-software-market,IMARC室內設計軟體（非設計服務）,medium
VN,地板市場,1278.4,百萬USD,2024,VN-07,https://www.imarcgroup.com/vietnam-flooring-market,IMARC地板市場；建材,medium
VN,木材及木製品出口,16.25,十億USD,2024,VN-03,https://vnexpress.net/bai-toan-18-ty-usd-cua-xuat-khau-go-noi-that-4843845.html,海關總局經VnExpress；年增超過20%；出口非內需,high
VN,家具出口（Mordor 引用）,13.436,十億USD,2024,VN-01,https://www.mordorintelligence.com/industry-reports/vietnam-furniture-market,Mordor引用之家具出口；年增24.5%,medium
VN,全國公寓＋獨棟住宅成交,138025,筆,2025,VN-38,https://baochinhphu.vn/nguon-cung-tang-gia-nha-chua-giam-102260117005432583.htm,Bộ Xây dựng彙整成功交易；未分新屋與中古,medium
VN,全國不動產成交合計,579718,筆,2025,VN-38,https://baochinhphu.vn/nguon-cung-tang-gia-nha-chua-giam-102260117005432583.htm,含土地441693筆；年增約7.7%,medium
VN,Q2公寓＋獨棟成交,34461,筆,2025Q2,VN-37,https://moc.gov.vn/vn/tin-tuc/1269/87076/bo-xay-dung-cong-bo-thong-tin-ve-nha-o-va-thi-truong-bat-dong-san-trong-quy-ii-nam-2025.aspx,Bộ Xây dựng官方季報；年增33.1%；季增2.61%,high
VN,河內新推出公寓,36000,戶（近）,2025,VN-25,https://www.cbrevietnam.com/insights/figures/hanoi-figures-q4-2025,CBRE河內公寓一級市場；史上第二高,high
VN,河內公寓售出,34760,戶,2025,VN-25,https://www.cbrevietnam.com/insights/figures/hanoi-figures-q4-2025,CBRE；Việt Nam News同數,high
VN,河內Q4新案去化率,79,%,2025Q4,VN-26,https://vietnamnews.vn/economy/1763814/ha-noi-apartment-market-sees-record-supply-clear-price-difference.html,CBRE經Việt Nam News,medium
VN,河內單價超過120百萬VND/m²新推案,4000,戶（近）,2025,VN-26,https://vietnamnews.vn/economy/1763814/ha-noi-apartment-market-sees-record-supply-clear-price-difference.html,CBRE；創紀錄,medium
VN,胡志明市新推出公寓,1400,戶（約）,2025H1,VN-27,https://theinvestor.vn/hcmc-apartment-prices-continue-to-rise-as-supply-hits-10-year-low-in-h1-d16321.html,CBRE；上半年去化率74%（2024H1為86%）,medium
VN,胡志明市成交,2700,戶,2025Q3,VN-28,https://theinvestor.vn/hcmc-apartment-prices-keep-climbing-as-supply-shortfall-persists-d17469.html,Savills；去化率51%,medium
VN,河內一手公寓均價,100,百萬VND/m²,2025,VN-36,https://vneconomy.vn/gia-chung-cu-o-mot-so-khu-vuc-da-tang-hon-40.htm,Bộ Xây dựng經VnEconomy；一級市場平均售價,medium
VN,胡志明市一手公寓均價,111,百萬VND/m²,2025,VN-36,https://vneconomy.vn/gia-chung-cu-o-mot-so-khu-vuc-da-tang-hon-40.htm,Bộ Xây dựng經VnEconomy；一級市場平均售價,medium
VN,70m²公寓室內裝修總價,180-450,百萬VND/戶,2025-2026,VN-11,https://takenli.vn/chi-phi-lam-noi-that-chung-cu-70m2-bao-gia-kinh-nghiem-thuc-te/,業者報價；摘要未明確綁定；面積口徑不明,low
VN,公寓裝修單價（推算）,2.57-6.43,百萬VND/m²,2025-2026,VN-11,https://takenli.vn/chi-phi-lam-noi-that-chung-cu-70m2-bao-gia-kinh-nghiem-thuc-te/,由70m²總價推算；示意,low
VN,設計費（辦公室）,150000-200000,VND/m²,年份不明,VN-16,https://coda.io/@thietkenoithat/bao-gia-thiet-ke-van-phong,自發布報價頁；面積越大單價越低,low
VN,ACG 稅後淨利,329.9,十億VND,2024年前三季,VN-18,https://doanhnhan.baophapluat.vn/thi-truong-xuat-khau-khoi-sac-lai-sau-thue-9-thang-cua-go-an-cuong-acg-tang-323-78729.html,年增32.3%；營收2764十億VND,high
VN,ACG 稅後淨利,137.94,十億VND,2025Q2,VN-17,https://www.dnse.com.vn/senses/tin-tuc/bctc-quy-22025-acg-loi-nhuan-q22025-tang-1677-so-voi-cung-ky-lai-13794-ty-dong-35102318,年增16.77%；營收961十億VND（年減6%）,high
VN,ACG 營收,2940.6,十億VND,2025年前三季,VN-19,https://doanhnhan.baophapluat.vn/go-an-cuong-acg-sap-rot-196-ty-dong-co-tuc-hoan-thanh-80-ke-hoach-loi-nhuan-nam-2025-88438.html,年增6.4%；稅後淨利358.2（年增8.6%）,medium
VN,ACG 營收,4600（超過）,十億VND,2025,VN-20,https://diendandoanhnghiep.vn/acg-tao-suc-bat-tu-noi-dia-10165333.html,摘要未綁定URL（候選）；年增16%；淨利504,low
```

---

## 8. 來源清單

| # | 標題 | 機構／作者 | 年份 | 語言 | URL | 讀取方式 |
|---|---|---|---|---|---|---|
| VN-01 | Quy mô thị trường nội thất Việt Nam（Vietnam Furniture Market） | Mordor Intelligence | 2025–2026 版 | 越 | https://www.mordorintelligence.com/industry-reports/vietnam-furniture-market | 搜尋結果內容 |
| VN-02 | Vì sao ngành nội thất Việt Nam chưa ghi dấu ấn trên thế giới? | Dân trí | 2025 | 越 | https://dantri.com.vn/bat-dong-san/vi-sao-nganh-noi-that-viet-nam-chua-ghi-dau-an-tren-the-gioi-20250607213731069.htm | 搜尋結果內容 |
| VN-03 | Bài toán 18 tỷ USD của xuất khẩu gỗ nội thất | VnExpress | 2025（依內容推斷） | 越 | https://vnexpress.net/bai-toan-18-ty-usd-cua-xuat-khau-go-noi-that-4843845.html | 搜尋結果內容 |
| VN-04 | Thị trường đồ nội thất trong nước: "Mảnh đất hứa" cho các doanh nghiệp | Báo Công Thương | 年份不明 | 越 | https://congthuong.vn/thi-truong-do-noi-that-trong-nuoc-manh-dat-hua-cho-cac-doanh-nghiep-276811.html | 搜尋結果內容（數字未能明確綁定，候選） |
| VN-05 | Thị trường nội thất Việt nhiều tiềm năng | VnEconomy | 年份不明 | 越 | https://vneconomy.vn/thi-truong-noi-that-viet-nhieu-tiem-nang.htm | 搜尋結果內容（數字未能明確綁定，候選） |
| VN-06 | Vietnam Interior Design Software Market Size, Share, Trends and Forecast…2025-2033 | IMARC Group | 2025 | 英 | https://www.imarcgroup.com/vietnam-interior-design-software-market | 搜尋結果內容 |
| VN-07 | Vietnam Flooring Market | IMARC Group | 2025 | 英 | https://www.imarcgroup.com/vietnam-flooring-market | 搜尋結果內容 |
| VN-08 | Vietnam Home Furniture Market | IMARC Group | 2024–2025 | 英 | https://imarcgroup.com/vietnam-home-furniture-market | 搜尋結果內容 |
| VN-09 | Vietnam Home Decor Market | IMARC Group | 2024–2025 | 英 | https://imarcgroup.com/vietnam-home-decor-market | 搜尋結果內容 |
| VN-10 | Vietnam Furniture and Interior Design Market | Ken Research | 2025–2026 | 英 | https://www.kenresearch.com/industry-reports/vietnam-furniture-and-interior-design-market.md | 搜尋結果內容 |
| VN-11 | Chi phí làm nội thất chung cư 70m2: Báo giá & kinh nghiệm thực tế | Takenli（業者） | 2025–2026 | 越 | https://takenli.vn/chi-phi-lam-noi-that-chung-cu-70m2-bao-gia-kinh-nghiem-thuc-te/ | 搜尋結果內容（數字歸屬為候選） |
| VN-12 | [Báo giá] Thi công nội thất chung cư trọn gói giá tại xưởng 2026 | Lanha（業者） | 2026 | 越 | https://www.lanha.vn/thi-cong-noi-that-chung-cu/ | 搜尋結果內容（數字歸屬為候選） |
| VN-13 | Báo Giá Thi Công Nội Thất Chung Cư HCM Trọn Gói T9/2025 | Nội thất Bến Thành（業者） | 2025 | 越 | https://noithatbenthanh.vn/thi-cong-noi-that-can-ho-tron-goi-tphcm/ | 搜尋結果內容（數字歸屬為候選） |
| VN-14 | Báo giá thiết kế thi công nội thất chung cư trọn gói năm 2024-2025 | Đồ gỗ Lê Gia（業者） | 2024–2025 | 越 | https://dogolegia.vn/bao-gia-thiet-ke-thi-cong-noi-that-chung-cu-tron-goi-nam-2025/ | 搜尋結果內容（數字歸屬為候選） |
| VN-15 | Chi phí làm Nội Thất 1 Căn Hộ Chung Cư là bao nhiêu? | VOZ 論壇 | 年份不明 | 越 | https://voz.vn/t/chi-phi-lam-noi-that-1-can-ho-chung-cu-la-bao-nhieu.530354/ | 搜尋結果內容（數字歸屬為候選） |
| VN-16 | Báo giá thiết kế văn phòng | thietkenoithat（coda.io 自發布頁） | 年份不明 | 越 | https://coda.io/@thietkenoithat/bao-gia-thiet-ke-van-phong | 搜尋結果內容 |
| VN-17 | BCTC quý 2/2025 ACG: lợi nhuận Q2/2025 tăng 16,77% so với cùng kỳ, lãi 137,94 tỷ đồng | DNSE | 2025 | 越 | https://www.dnse.com.vn/senses/tin-tuc/bctc-quy-22025-acg-loi-nhuan-q22025-tang-1677-so-voi-cung-ky-lai-13794-ty-dong-35102318 | 搜尋結果內容 |
| VN-18 | Thị trường xuất khẩu khởi sắc, lãi sau thuế 9 tháng của Gỗ An Cường (ACG) tăng 32,3% | Báo Pháp luật Việt Nam – Doanh nhân | 2024 | 越 | https://doanhnhan.baophapluat.vn/thi-truong-xuat-khau-khoi-sac-lai-sau-thue-9-thang-cua-go-an-cuong-acg-tang-323-78729.html | 搜尋結果內容 |
| VN-19 | Gỗ An Cường (ACG) sắp rót 196 tỷ đồng cổ tức, hoàn thành 80% kế hoạch lợi nhuận năm 2025 | Báo Pháp luật Việt Nam – Doanh nhân | 2025 | 越 | https://doanhnhan.baophapluat.vn/go-an-cuong-acg-sap-rot-196-ty-dong-co-tuc-hoan-thanh-80-ke-hoach-loi-nhuan-nam-2025-88438.html | 搜尋結果內容 |
| VN-20 | ACG tạo sức bật từ nội địa | Diễn đàn Doanh nghiệp | 2025–2026 | 越 | https://diendandoanhnghiep.vn/acg-tao-suc-bat-tu-noi-dia-10165333.html | 搜尋結果內容（全年數字歸屬為候選） |
| VN-21 | CTCP Gỗ An Cường (ACG) doanh thu lập kỷ lục mới, trích lập dự phòng nợ xấu xấp xỉ 300 tỷ đồng | Báo Pháp luật Việt Nam – Doanh nhân | 年份不明 | 越 | https://doanhnhan.baophapluat.vn/ctcp-go-an-cuong-acg-doanh-thu-lap-ky-luc-moi-trich-lap-du-phong-no-xau-xap-xi-300-ty-dong.html | 搜尋結果內容（僅標題） |
| VN-22 | Đóng cửa 1 chi nhánh tại Bình Tân, Gỗ An Cường (ACG) kinh doanh ra sao? | Báo Pháp luật Việt Nam – Doanh nhân | 年份不明 | 越 | https://doanhnhan.baophapluat.vn/dong-cua-1-chi-nhanh-tai-binh-tan-go-an-cuong-acg-kinh-doanh-ra-sao-80761.html | 搜尋結果內容（僅標題） |
| VN-23 | Gỗ An Cường (ACG) muốn bán 14,74 triệu cổ phiếu công ty con cho hai cá nhân | Báo Pháp luật Việt Nam – Doanh nhân | 年份不明 | 越 | https://doanhnhan.baophapluat.vn/go-an-cuong-acg-muon-ban-14-74-trieu-co-phieu-cong-ty-con-cho-hai-ca-nhan.html | 搜尋結果內容（僅標題） |
| VN-24 | Gỗ An Cường (ACG) muốn rót nghìn tỷ đồng vào công ty con | Báo Pháp luật Việt Nam – Doanh nhân | 年份不明 | 越 | https://doanhnhan.baophapluat.vn/go-an-cuong-acg-muon-rot-nghin-ty-dong-vao-cong-ty-con-86302.html | 搜尋結果內容（僅標題） |
| VN-25 | Hanoi Figures Q4 2025 | CBRE Vietnam | 2026 | 英 | https://www.cbrevietnam.com/insights/figures/hanoi-figures-q4-2025 | 搜尋結果內容 |
| VN-26 | Hà Nội apartment market sees record supply, clear price difference | Việt Nam News | 2026 | 英 | https://vietnamnews.vn/economy/1763814/ha-noi-apartment-market-sees-record-supply-clear-price-difference.html | 搜尋結果內容 |
| VN-27 | HCMC apartment prices continue to rise as supply hits 10-year low in H1 | The Investor | 2025 | 英 | https://theinvestor.vn/hcmc-apartment-prices-continue-to-rise-as-supply-hits-10-year-low-in-h1-d16321.html | 搜尋結果內容 |
| VN-28 | HCMC apartment prices keep climbing as supply shortfall persists | The Investor | 2025 | 英 | https://theinvestor.vn/hcmc-apartment-prices-keep-climbing-as-supply-shortfall-persists-d17469.html | 搜尋結果內容 |
| VN-29 | Nghị định 175/2024/NĐ-CP（法規全文頁） | GXD（cchn.gxd.vn） | 2024 | 越 | https://cchn.gxd.vn/van-ban/qlda/nghi-dinh-175-2024.html | 搜尋結果內容 |
| VN-30 | Điểm mới của Nghị định 175 về quản lý hoạt động xây dựng so với Nghị định 15 | LuatVietnam | 2025 | 越 | https://luatvietnam.vn/dat-dai-nha-o/diem-moi-cua-nghi-dinh-175-ve-quan-ly-hoat-dong-xay-dung-567-100623-article.html | 搜尋結果內容 |
| VN-31 | Cục Quản lý hoạt động xây dựng hướng dẫn pháp luật về chứng chỉ hành nghề（Nghị định 175/2024 簡報） | Cục Quản lý hoạt động xây dựng（Bộ Xây dựng）；檔案置於 quangdaqs.vn | 2025 | 越 | http://www.quangdaqs.vn/data/files/NGHI%CC%A3%20%C4%90I%CC%A3NH%20175_2024_N%C4%90CP%20-%20SLIDE%20VE%CC%82%CC%80%20CHU%CC%9B%CC%81NG%20CHI%CC%89%20HA%CC%80NH%20NGHE%CC%82%CC%80.pdf | 搜尋結果內容 |
| VN-32 | Phần 3 – Những điểm quy định mới của Nghị Định 175/2024/NĐ-CP về năng lực hoạt động xây dựng | ICCI | 2025 | 越 | https://icci.vn/tin-tuc/phan-3-nhung-diem-quy-dinh-moi-cua-nghi-dinh-175-2024-nd-cp-ve-nang-luc-hoat-dong-xay-dung.html | 搜尋結果內容（僅標題） |
| VN-33 | Thủ tục xin cấp giấy phép sửa chữa nhà ở mới nhất năm 2024? | Thư viện Pháp luật | 2024 | 越 | https://thuvienphapluat.vn/hoi-dap-phap-luat/thu-tuc-xin-cap-giay-phep-sua-chua-nha-o-moi-nhat-nam-2024-138023971.html | 搜尋結果內容 |
| VN-34 | Sửa chữa, cải tạo công trình có cần xin giấy phép xây dựng? | LSVN（Tạp chí Luật sư Việt Nam） | 年份不明 | 越 | https://lsvn.vn/sua-chua-cai-tao-cong-trinh-co-can-xin-giay-phep-xay-dung-a37692.html | 搜尋結果內容 |
| VN-35 | Công văn 6057/BXD-HĐXD năm 2020 về sửa chữa cải tạo công trình do Bộ Xây dựng ban hành | Hệ thống pháp luật（轉載 Bộ Xây dựng 函） | 2020（仍屬現行主管機關見解，故引用） | 越 | https://hethongphapluat.com/cong-van-6057-bxd-hdxd-nam-2020-ve-sua-chua-cai-tao-cong-trinh-do-bo-xay-dung-ban-hanh.html | 搜尋結果內容 |
| VN-36 | Giá chung cư ở một số khu vực đã tăng hơn 40% | VnEconomy | 2025–2026 | 越 | https://vneconomy.vn/gia-chung-cu-o-mot-so-khu-vuc-da-tang-hon-40.htm | 搜尋結果內容 |
| VN-37 | Bộ Xây dựng công bố thông tin về nhà ở và thị trường bất động sản trong Quý II năm 2025 | Bộ Xây dựng（moc.gov.vn） | 2025 | 越 | https://moc.gov.vn/vn/tin-tuc/1269/87076/bo-xay-dung-cong-bo-thong-tin-ve-nha-o-va-thi-truong-bat-dong-san-trong-quy-ii-nam-2025.aspx | 搜尋結果內容 |
| VN-38 | Nguồn cung tăng, giá nhà chưa giảm | Báo Chính phủ（baochinhphu.vn） | 2026 | 越 | https://baochinhphu.vn/nguon-cung-tang-gia-nha-chua-giam-102260117005432583.htm | 搜尋結果內容 |
| VN-39 | Lượng giao dịch căn hộ chung cư, nhà ở riêng lẻ tăng 33% | SGGP | 2025 | 越 | https://www.sggp.org.vn/luong-giao-dich-can-ho-chung-cu-nha-o-rieng-le-tang-33-post805811.html | 搜尋結果內容（僅標題） |
| VN-40 | Lượng giao dịch nhà quý II/2025 tăng hơn 116%, giá căn hộ chung cư Hà Nội và TP.HCM cao nhất gần một thập kỷ | Tin nhanh Chứng khoán | 2025 | 越 | https://www.tinnhanhchungkhoan.vn/luong-giao-dich-nha-quy-ii2025-tang-hon-116-gia-can-ho-chung-cu-ha-noi-va-tphcm-cao-nhat-gan-mot-thap-ky-post373866.html | 搜尋結果內容（僅標題） |
| VN-41 | Bất động sản Quý I 2025: Dự án được cấp phép mới tăng mạnh | Báo Bảo vệ Pháp luật | 2025 | 越 | https://baovephapluat.vn/kinh-te/do-thi-xay-dung/bat-dong-san-quy-i-2025-du-an-duoc-cap-phep-moi-tang-manh-178112.html | 搜尋結果內容（Q1 數字歸屬為候選） |
| VN-42 | Viettel Construction ra mắt mảng nội thất | VnExpress | 年份待確認（約 2023） | 越 | https://vnexpress.net/viettel-construction-ra-mat-mang-noi-that-4596449.html | 搜尋結果內容（僅標題） |
| VN-43 | Chứng Chỉ Nghề Thiết Kế Nội Thất Và Những Điều Cần Biết | AWE（培訓機構） | 年份不明 | 越 | https://awe.edu.vn/chung-chi-nghe-thiet-ke-noi-that-va-nhung-dieu-can-biet | 搜尋結果內容（僅標題） |

來源統計：43 筆。越南文 34 筆、英文 9 筆。官方或主管機關來源 4 筆（VN-31、VN-35、VN-37、VN-38）。其中 11 筆僅標題或數字歸屬為候選，已個別標示。
