# 新加坡（Singapore）— 對抗式查核報告（WP6）

| 項目 | 內容 |
|---|---|
| 查核日期 | 2026-10-09 |
| 查核者 | Claude 子代理（SG-verification，懷疑立場） |
| 查核對象 | `countries/SG-A-market.md`（視角 A：市場）、`countries/SG-B-rules.md`（視角 B：法規） |
| 方法 | 15 次獨立 WebSearch（3 次以華文重新措辭、12 次英文，均避開分析師原查詢字串）；WebFetch／curl 被封鎖，證據為搜尋引擎回傳之頁面摘要與引文。另以人工算術複核兩份筆記全部匯率／面積換算。預設立場：主張在證據支持前視為錯誤 |
| 結果 | 查核 28 項：**確認 15、修正 5、駁斥 0、無法查證 8**；另列 15 項內部矛盾／定義問題 |
| 保留額度 | 2 次搜尋未使用（依任務規定保留） |

---

## (a) 逐項查核表

| # | 項目 | 原報告值 | 查核結果 | 修正值 | 證據 URL | 說明 |
|---|---|---|---|---|---|---|
| 1 | HDB 轉售交易量 2025（A §1.3、§3.1、§8） | 26,169 筆（−9.7%；2024：28,986） | **確認** | 同左（HDB 4Q2025 正式數；初估為 26,042、−9.8%） | https://www.hdb.gov.sg/about-us/news-and-publications/press-releases/Upcoming-flat-supply-4Q2025-rpi ；https://www.era.com.sg/research-articles/4q-2025-hdb-quarterly-report ；https://www.99.co/singapore/insider/hdb-ura-q42025-statistics/ | 華文獨立搜尋回傳相同數字。A §10 已正確處理 26,042（初估）與 26,169（正式）之差。另查得 **2025 年達 MOP 之組屋僅 6,973 戶（11 年新低）**，可補強 B §5.1「2026 年 13,480 戶達 MOP≈2025 年 2 倍」之說法 |
| 2 | HDB 轉售價格指數 2025（A §3.1、§6） | 全年 +2.9%（2024：+9.7%）；Q4 5,256 筆（−27.2% q-o-q、−18.2% y-o-y） | **確認** | 同左；Q4 指數 203.6（Q3 203.7），為 2020 Q1 以來首次無季增 | https://edgeprop.sg/property-news/hdb-resale-price-growth-slows-million-dollar-flats-prices-gain-23-4q2025 ；https://www.99.co/singapore/insider/hdb-ura-q42025-statistics/ | 全部數字一致。注意「9.7%」同時是 2024 年價格漲幅與 2025 年交易量跌幅，撰寫時勿混用 |
| 3 | 私宅新售（developer sales）2025（A §1.3、§3.1、§8） | 10,611 戶（2024：6,469） | **修正** | **10,815 戶（不含 EC；2024：6,469）**，URA 4Q2025 正式統計（2026-01-23） | https://www.ura.gov.sg/news/media/pr26-05/ | A 的 10,611 應為 ERA 以 caveat 計之數，非 URA 官方；差 1.9%。最終報告採 URA 10,815。URA 另載 2025 全年推出 11,482 戶、Q4 新售 2,940 戶 |
| 4 | 私宅完工 2025（A §1.3、§2.5、§8） | 6,123 戶（不含 EC；2024：8,460） | **修正（口徑）** | **URA：7,996 戶（含 EC，Q4 2,018）**；ERA：6,123 戶（不含 EC） | https://www.ura.gov.sg/news/media/pr26-05/ ；https://www.era.com.sg/research-articles/4q-2025-ura-private-quarterly-report | 6,123 為 ERA 窄口徑，數字本身可用，但 A 把它與 2024 的 8,460 直接比較，而 8,460 疑為 URA 含 EC 口徑（本輪未能確認），**兩年口徑須統一後才可比**。A §2.5 推估若改用 7,996 戶，新完工裝修產值由 S$1.9 億升至約 S$2.5 億（影響微小） |
| 5 | 私宅未售庫存、2025 價格（A §3.1、§6） | 未售 16,193 戶（−5.2% q-o-q） | **確認（並補充）** | 未售 16,193 戶（有規劃許可 39,746 戶，含 EC）；**2025 年私宅價格 +3.3%**（2024：+3.9%）、租金 +1.9% | https://www.ura.gov.sg/news/media/pr26-05/ | A 未載 2025 私宅價格年增，建議補入 |
| 6 | 私宅全年交易總量 2025（A §1.3、§7） | 26,492 戶 | **無法查證** | — | （URA pr26-05 僅載新售 10,815；轉售／轉手合計未在摘要出現） | ERA 口徑數字；與 URA 新售 10,815 相加後之轉售＋轉手約 15,700 戶，量級合理。採用時標「ERA 整理」 |
| 7 | CASE 2024 裝修投訴與預付款損失（A §1.7、§4.3；B §1.2、§3.2） | 962 件（2023：1,168）；97% 非 CaseTrust；全行業預付款損失 S$193 萬；裝修 S$728,814 | **確認** | 同左；另補 **2022 年裝修投訴 1,469 件**；認證業者投訴全數解決 | https://singaporelawwatch.sg/Headlines/consumers-lost-almost-2m-in-prepayments-in-2024-highest-losses-from-home-renovations-case ；https://case.org.sg/wp-content/uploads/2025/02/Media-Release-CASE-sees-prepayment-losses-more-than-quadruple-in-2024-entertainment-related-complaints-nearly-triple.pdf ；https://vulcanpost.com/880908/singaporean-customers-prepayment-losses-2024-skyrocket | 華文獨立搜尋回傳相同數字（二手來源寫「約 S$72.8 萬」，精確值 728,814 來自 CASE 原 PDF，B 引用正確） |
| 8 | CASE 2025 全年裝修統計（A §11.15、B §3.2 皆列為「未找到」） | 缺口；B 並將商業部落格「2025 預付款損失 −73.8%」判為「無法溯源，不採用」 | **修正（補齊缺口；B 誤判）** | **CASE 2026-02 新聞稿：2025 年總投訴 13,786 件（−3.2%）；裝修承包商居投訴第 4 位（美容、電器、汽車之後）；全行業預付款損失 S$2,710,000（+40.4%）；裝修業預付款損失 S$190,667（第 2 位，較 2024 年 S$728,814 減 73.8%）**；CASE 將裝修投訴下降歸因於 CaseTrust 認證擴大 | https://www.case.org.sg/wp-content/uploads/2026/02/Media-Release——76.2-per-cent-surge-in-beauty-complaints-in-2025-with-consumers-losing-over-2.1m.pdf | 該新聞稿 2026-02 即公布，兩位分析師（2026-10-08）均未找到。部落格之「−73.8%」實為 190,667÷728,814 之正確計算，B 的否定錯誤。2025 年裝修投訴**件數**未在摘要出現，整合時應開啟 PDF 補齊 |
| 9 | CaseTrust 認證裝修業者家數（A §1.6、§4.1、§8） | 約 183 家（Aman Engineering 轉述，低信心） | **修正** | **逾 140 家（CASE 2025-02 自述）**；2025-03 起目標再認證 500 家 | https://singaporelawwatch.sg/Headlines/consumers-lost-almost-2m-in-prepayments-in-2024-highest-losses-from-home-renovations-case | 183 可能是 2026 年之商業目錄計數，但無官方佐證；最終報告採 CASE 自述「>140（2025-02）」並註明 500 家目標 |
| 10 | CaseTrust 認證條件（A §4.4、§9；B §3.1、§5.4、§9） | 首期訂金 ≤20%；訂金履約保證（Deposit Performance Bond）；標準裝修契約、分期付款；12 個月工藝保固 | **確認** | 同左；保證範圍現版強調「歇業、清算、破產」，2023 版另含「不履約」；須先為 RCMA 會員方可申請 CaseTrust-RCMA 聯合認證 | https://case.org.sg/casetrust/casetrust-accreditation-for-renovation-businesses/ ；https://www.case.org.sg/casetrust/wp-content/uploads/2025/08/Info-Kit-CaseTrust-for-Renovation-Businesses-Silver.pdf ；https://www.case.org.sg/casetrust/info-kit-casetrust-accreditation-for-renovation-businesses-silver-subsidy-framework-june-2025 | B 將「≤20%」標為「承接前版、中信心」，本輪由 CASE 官方頁確認，可升為「高」。12 個月保固亦見於 CASE 官方資料，不必依賴第三方代管 PDF |
| 11 | HDB DRC 申請人資格（B §1.3、§2.2、§4.1、§9、§11.1；A §4.4） | 第三方稱：申請人須公民／PR；Pte Ltd 實收資本 ≥S$50,000；3 年經驗（CaseTrust 1 年）；ACRA 登記 ≥1 年、有獲利（B 標「低信心、驗證必查」） | **確認（主要項目；HDB 官方頁）** | **HDB 官方頁明載：申請人須為新加坡公民或永久居民；完成 BCA 學院「Renovation for Public Housing」課程；公司 ACRA 登記；過去一年有獲利；至少 1 名全職員工；Pte Ltd 實收資本 ≥S$50,000；合夥人／董事非未解除破產人、無詐欺／不誠實前科；申請費 S$100；21 個工作天內通知結果**。「3 年經驗」與「ACRA 登記滿 1 年」**未見於官方頁，無法查證** | https://www.hdb.gov.sg/business/renovation-contractors/windows ；https://www.hdb.gov.sg/business/renovation-contractors/renovation ；https://www.hdb.gov.sg/cs/infoweb/business/renovation-contractors/renovation/directory-of-renovation-contractors-drc | 上述條件列於 HDB「窗戶承包商列名」頁（同屬 DRC 體系，另要求 BCA CRS RW01 工種），一般 DRC 頁僅稱「須符合申請標準」；兩頁條件高度可能相同，但整合時仍應以一般 DRC 申請頁逐條核對。**對外資的結論不變：須有公民／PR 身分之申請人（獨資東主／合夥人／董事）**，B 的「低信心」可升為「中高」 |
| 12 | BCA 建築商執照（BLS）門檻（B §1.1、§2.3、§9） | GB1 不限金額；GB2 專案 ≤S$600 萬；實收資本 GB1 ≥S$300,000、GB2 ≥S$25,000；執照費 S$1,800／S$1,200；效期最長 3 年 | **確認** | 同左 | https://www1.bca.gov.sg/regulatory-info/building-control/builder-licensing ；https://www1.bca.gov.sg/procurement/pre-tender-stage/builders-licensing-scheme-bls ；https://www1.bca.gov.sg/bca-directory/company/Details/200202016R ；https://lawplayer.com/sg/act/BCA1989/29C | BCA 公司名錄之執照條件明載「不得承接估計最終價格逾 S$600 萬之合約」。注意《Building Control Act》第 29C 條條文本文仍寫 S$300 萬，但授權部長以公告調整，現行操作值為 S$600 萬；B 引 S$600 萬正確。執照費由 BCA 官方頁確認，B 原標「第三方、中」可升為「高」 |
| 13 | EP 最低月薪現行與 2027 調整（B §1.3、§2.5、§4.3、§9） | 2025 起 S$5,600（金融 S$6,200）；2027-01-01 起新申請 S$6,000（金融 S$6,600）；續期 2028-01-01 起適用 | **確認** | 同左（Budget 2026／2026-03 COS 宣布） | https://www.forvismazars.com/sg/en/insights/latest-insights-updates/outsourcing/work-pass-requirements ；https://terraadvisoryservices.com/singapore-ep-changes-2027/ | 多個獨立顧問來源一致；宣布日期（2026-02-17 預算案 vs 2026-03 COS）各源不一，整合時引 MOM 官方頁 |
| 14 | EP 45 歲以上門檻 2027（B §1.3、§4.3、§9） | 2027 起 S$11,500（金融 S$12,700）；現行 S$10,700 | **無法查證** | 現行 S$10,700 可由第三方確認；**S$11,500／12,700 僅為顧問公司「預期約值」，MOM 尚未公布 2027 年齡級距表** | https://transformborders.com/employment-pass-salary-singapore/ ；https://terraadvisoryservices.com/singapore-ep-changes-2027/ | B 標「高（多來源一致）」過於樂觀；應改為「推估、待 MOM 公布」。對台籍資深主管派駐成本之推論（≈NT$28 萬／月）須加註 |
| 15 | 建築業外勞 DRC 與 MYE（B §1.5、§2.5、§4.3、§6.5、§9） | 2024-01-01 起 DRC 由 1:7（87.5%）降至 1:5（83.3%）；MYE 廢除（來源矛盾） | **確認** | 同左：2022-02 聯合新聞稿宣布、2024-01-01 生效；**MYE 自 2024-01-01 起廢除**（levy 結構同步調整，非「以新框架取代」）；超額業者可留用既有工人至准證到期；MND 2024-02 稱多數建築業 SME 本已在 1:5 內 | https://www.mom.gov.sg/newsroom/press-releases/2022/0218-supporting-transformation-in-the-process-and-construction-sectors ；https://www.mnd.gov.sg/newsroom/speeches/view/written-answer-by-ministry-of-national-development-on-the-number-of-local-smes-impacted-by-the-reduced-dependency-ratio-ceiling-(drc)-for-the-construction-sector ；https://www.edgeprop.sg/property-news/contractors-and-developers-face-skilled-labour-crunch-and-high-costs-2024 | B 所列「2026 商業指南仍載 87.5%」為過時資料，可逕採 83.3%；信心升為「高」 |
| 16 | 辦公室 fit-out 單價 C&W 2026（A §1.5、§3.6、§7、§8） | 新加坡 USD 140/ft²（SGD 180）；東京 215、香港 160；2025-12 市況 | **確認** | 同左；另確認雪梨 USD 161、印度 65–73；C&W 自述為「指標性基準」 | https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office/ ；https://ianslive.in/india-remains-asia-pacifics-most-cost-competitive-office-fit-out-market-report--20260326105534 ；https://fitoutawards.ie/news/hong-kong-office-fit-out-costs-hold-firm-at-160-per-square-foot-as-greater-china-peers-record-declines | 換算 USD 140/ft² ≈ USD 1,507/m²（本查核換算），A 的 SGD 180/ft²、NT$15.8 萬/坪換算正確。大阪 210、基本／高規 USD 102／212 未在本輪摘要出現（未否定） |
| 17 | 辦公室 fit-out Knight Frank 2026（A §1.5、§3.6、§7、§8，標「高」信心、繼承） | 新加坡 USD 2,029/m²，亞太 23 城最高（東京 1,994、台北 1,593） | **無法查證** | 指南存在且確為 23 城（澳紐、東亞、東南亞）；本輪僅見印度城市數字（中規格 USD 449/m²、高規 838/m²），**新加坡／東京／台北數字未見** | https://realtynmore.com/asia-pacific-knight-frank-report | A 在 §7、§8 標「高」信心不當：該數字為第 1 回合繼承、未開頁、本輪亦未能驗證，應降為「低」。且 KF 的 USD 2,029/m² 與 C&W 的 USD 1,507/m² 規格口徑不同，不可互比（見 (b)-8） |
| 18 | Qanvast 2025 組屋每案裝修費（A §1.4、§3.3、§8；B §1.4、§5.2、§9） | 4 房轉售 S$64,300–80,300；4 房 BTO S$51,000–61,800（A 稱「平台實際合約中位數」） | **確認（定義修正）** | 數字確認；但其性質為 **Qanvast 以 2024 年平台專案中位數 +1–5% 推估之 2025「平均區間」**，非 2025 年實際合約中位數。交叉：MoneySmart 2026 版 4 房轉售 S$55,000–85,000、BTO S$51,000–70,000；HomeJourney 轉售 S$55,700–80,400（含 10% 預備金）；2024 年中階 S$58,000–72,200 | https://dollarsandsense.sg/how-much-does-it-cost-to-renovate-your-hdb-resale-flat/ ；https://www.moneysmart.sg/personal-loan/3-4-and-5-room-hdb-renovation-cost-ms ；https://uchify.com/renovation-cost-4-room-bto-2025/ ；https://www.homejourney.sg/blog/homejourney-renovation-budget-planning-complete-guide-singapore-202512301900 | 華文獨立搜尋回傳相同區間。B 的描述（「2024 中位數＋1–5% 推算」）正確，A §1.4 的「平台實際合約中位數」應改寫 |
| 19 | Qanvast 2025 公寓每案（A §3.3；B §5.2） | 新公寓 S$40,400–51,500；轉售公寓 S$80,800–105,000（2024 年 315 案） | **無法查證** | — | （本輪搜尋未回傳公寓數字） | 僅 Qanvast 單一來源；採用時標「中」並註明 315 案樣本 |
| 20 | DeepMarket Insights 室內設計服務市場（A §1.2、§2.1、§2.3、§8；經 designbureau.sg 轉引） | USD 7.7 億（2024）→ 12.2 億（2033），隱含 CAGR ≈5.3% | **修正** | **DMI 官方頁：USD 0.7 Billion（2025）→ 1.1 Billion（2034），CAGR 5.14%（2026–2034）** | https://deepmarketinsights.com/vista/insights/interior-design-services-market/singapore | 轉引值疑為舊版或四捨五入前數字；最終報告直接引 DMI 官方頁，並把 A 的「研究機構一致落在 5.3–5.9%」改為 **5.1–5.9%** |
| 21 | Cognitive Market Research 室內設計市場（A §1.2、§2.1、§7、§8） | USD 7.16 億（2024）→ 8.62 億（2025）→ 13.27 億（2033），CAGR 5.54% | **無法查證（且內部不一致）** | — | （本輪搜尋未回傳 CMR 新加坡頁） | 7.16→8.62 隱含單年 +20.4%，與 CAGR 5.54% 矛盾；8.62×1.0554^8≈13.27 僅對 2025→2033 成立，故 7.16（2024）極可能來自不同版本／口徑。**不可當時間序列並列**；若採用僅引 8.62 億（2025）並標「低」 |
| 22 | Ken Research 傢俱＋家飾（A §1.2、§2.1、§8） | USD 11.3 億（2025）→ 15.5 億（2031），CAGR 5.43% | **確認** | USD 1,130 百萬（2025）→ 1,552 百萬（2031），5.43% | https://www.kenresearch.com/industry-reports/singapore-furniture-home-decor-market | 零售口徑，與設計服務不可相加（A 已註明） |
| 23 | Astute Analytica interior fit-out furniture（A §2.1） | USD 49 億（2030E，CAGR 7%，2021 基準） | **確認（不可比）** | USD 2,728.6 百萬（2021）→ 4,909.1 百萬（2030），7.0% | https://www.barchart.com/story/news/15079089/singapore-interior-fit-out-furniture-market-share-key-players-revenue-report-and-forecast-by-2030 | 含固定傢俱之窄口徑且基準過舊，A 標「極低」正確；建議最終報告不採 |
| 24 | Statista 家飾零售（A §2.1、§8） | USD 3.66 億（2025），CAGR 3.15%（2025–29） | **確認（版本差異）** | Statista 另一版本：2024 年 €328m、CAGR 3.43%（2024–29） | https://es-statista-com.ezproxy.canberra.edu.au/outlook/cmo/furniture/home-decor/singapore | 兩版相容（€328m≈USD 3.5 億，2025 年約 3.66 億）；Statista Market Insights 為模型推估，標「低」 |
| 25 | Frost & Sullivan fitting-out 市場（A §1.2、§2.1、§2.5、§7、§8；繼承、未開頁） | SGD 48.75 億（2022E，2020 港交所招股書） | **無法查證** | — | （搜尋未回傳任何 HKEX 招股書或 F&S 數字；僅見 Astute 之傢俱口徑 USD 27.3 億／49 億） | 這是 A 唯一的「承攬口徑」錨點，用以校準住宅推估 S$27–35 億，但兩輪皆未開頁、本輪亦無法獨立找到；最終報告若採用須標「繼承、未驗證、2020 年預估」，並以 A §2.5 推估為主、F&S 為輔 |
| 26 | HIP 2025 批次與 HDB 存量（A §3.2、§7、§8、§9） | 29,000 戶、371 棟、S$4.07 億；累計 494,000 戶獲選；推論組屋總數約 110 萬戶、約半數屋齡 ≥28 年 | **無法查證** | — | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf | HDB《Key Statistics FY2024/25》PDF 已存在（含「Properties Under Management」節），但摘要未含數字；整合時應開啟該 PDF 取得官方存量與 HIP 累計數，取代 A 的 110 萬戶推算 |
| 27 | 室內設計師無法定證照；政府不強制資格（B §1.1、§2.1；A §4.4） | IDCS 自述無規管；MTI 2024-05 國會答覆不強制主要人員資格；SIDAS 為自願 | **確認（間接）** | 同左 | https://www.mti.gov.sg/newsroom/written-reply-to-pqs-on-disputes-arising-from-interior-design-and-renovation-firms ；https://www.mnd.gov.sg/newsroom/speeches/view/written-answer-by-ministry-of-national-development-on-accountability-framework-for-renovation-contractors | MTI 答覆頁於兩次獨立搜尋中出現（新舊網址各一），內容未開頁；與新加坡僅規管建築師（Architects Act）與專業工程師之既知架構一致。**另發現 MND「裝修承包商問責框架（accountability framework for renovation contractors）」書面答覆**，兩份筆記皆未引用，內容本輪未能取得，整合階段必讀（可能涉及 DRC／CaseTrust 之後續政策） |
| 28 | 小額索償法庭上限、裝修貸款上限（B §1.4、§3.3、§5.5、§9；A §3.7） | SCT S$20,000（同意可至 S$30,000）；裝修貸款 S$30,000 或 6 倍月薪取低者 | **無法查證（本輪未搜尋）** | — | （B 引司法院、DBS／MoneySmart） | 與現行《Small Claims Tribunals Act》及銀行裝修貸款慣例一致，為節省配額未獨立搜尋；可視為高信心 |

---

## (b) 內部矛盾與定義問題

1. **匯率微差**：A 用 SGD/TWD 24.6（USD/SGD 1.28、USD/TWD 31.5），B 用 24.5（S$1≈USD 0.78、USD/TWD 31.4）。差 0.4%，造成同一數字 NT$ 值不同（4 房轉售上限 A 198 萬 vs B 197 萬；EP S$5,600 兩者皆 13.7 萬）。本查核逐項複算兩份筆記之 SGD→USD→TWD、ft²→m²→坪換算（含 C&W SGD 180/ft²＝S$1,938/m²＝S$6,405/坪≈NT$15.8 萬、KF USD 2,029/m²≈NT$21.1 萬/坪、Livspace ₹1,460 crore≈USD 1.70 億、GDP 比例等），**算術均正確**；整合時以 V2 統一匯率表覆寫即可。
2. **CaseTrust 認證家數**：A 三處寫「約 183 家」（商業指南轉述），CASE 2025-02 自述「逾 140 家」；兩者相差 30%，且 A 用 183 推論「DRC 2,700 家中僅 7% 認證」。應改用 CASE 自述並標時間點。
3. **CMR 數列自相矛盾**：7.16 億（2024）→8.62 億（2025）為單年 +20%，與其 CAGR 5.54% 不相容；A §10 矛盾表僅比較 CMR 與 DMI 的 2024 值，未發現此點。
4. **DMI 轉引值與官方頁不符**：A 引 designbureau.sg 轉引之 7.7 億（2024）／12.2 億（2033）／隱含 5.3%；DMI 官方頁為 0.7B（2025）／1.1B（2034）／5.14%。A §2.3「三者一致落在 5.3–5.9%」應改 5.1–5.9%。
5. **私宅完工口徑混用**：A 把 ERA「6,123（不含 EC）」與「2024：8,460」並列，但 8,460 疑為 URA 含 EC 數；URA 2025 含 EC 為 7,996。A §6「私宅完工大減（6,123 戶）」之跌幅可能被高估。
6. **私宅新售 10,611 vs URA 10,815**：A §10 已注意 Q4 交易量 URA／ERA 口徑差（6,699 vs 5,399），但全年新售仍採 ERA 值；應統一採 URA 官方。
7. **Qanvast「中位數」定義**：A §1.4、§3.3 稱「平台實際合約中位數」，B §5.2 稱「2024 年中位數 +1–5% 推算」；後者正確。另 **B §5.2 表「三房組屋轉售 51,000–61,800」與「四房 BTO 51,000–61,800」完全相同**，疑為抄錄錯誤（本輪摘要未含三房數字，無法判定），整合前須核對 Qanvast 原文。
8. **兩套辦公室 fit-out 單價不可互比**：KF USD 2,029/m²（≈USD 189/ft²）與 C&W USD 140/ft²（≈USD 1,507/m²）相差 35%，來自不同規格定義（KF 未驗證）。A §7 一面用 KF 說「新加坡＝台北 1.27 倍」，一面用 C&W 說「基本型高 67%、先進型僅高 5%」，讀者會得到互相衝突的「新加坡溢價」。建議最終報告只用 C&W（本輪已驗證、且有台北同版數字），KF 僅列附註。
9. **B 錯判正確資料**：B §3.2 將部落格「2025 預付款損失 −73.8%」判為「無法溯源、不採用」，但 CASE 2026-02 新聞稿證實裝修預付款損失由 S$728,814 降至 S$190,667（−73.8%）。同一部落格的「2024 有 1,247 件詐騙舉報／S$280 萬」仍無法溯源，維持不採。
10. **CASE 2025 全年資料缺口並不存在**：A §11.15、B §11.4 皆列為缺口，實際上 CASE 2026-02 已公布（總投訴 13,786、預付款損失 S$271 萬）。兩份筆記的「2025 消保趨勢」判讀（A §6「消保趨嚴」）應以此更新：**整體預付款損失上升 40%，但裝修業損失大減、投訴排名由前列降至第 4**。
11. **DRC 資格信心標示過低**：B 三處把「公民／PR、S$50,000」標為「低（商業來源）」並列為 §11 第 1 缺口；實際上 HDB 官方頁即有記載（窗戶承包商列名頁）。反之，B 轉述的「3 年經驗（CaseTrust 1 年）」與「ACRA 登記 ≥1 年」在官方頁未見，應降為「未證實」。
12. **EP 45 歲門檻信心標示過高**：B §4.3 將 2027 年「S$11,500／12,700」與 S$6,000 一併標「高（多來源一致）」，但前者僅為顧問公司推估，MOM 未公布年齡級距。
13. **KF 信心標示過高**：A §7、§8 將繼承且未開頁的 KF USD 2,029/m² 標「高」，與 A 自訂之信心定義（高＝官方或 ≥3 獨立來源）不符。
14. **研究機構口徑不可相加**（A 已註明，此處重申）：設計服務 USD 0.7–0.86 億級（研究機構模型）、fitting-out 承攬 S$48.75 億（F&S 2022E，未驗證）、住宅推估 S$27–35 億（A 自算）、傢俱／家飾／家居改善零售 USD 3.1–21.7 億（四家定義互異、差距 2 倍以上）。A §7 錨點表以「設計服務占 GDP 0.14%」對比台灣「0.07–0.28%」，兩地口徑未必相同，僅供量級參考。
15. **人均 GDP 繼承值未驗證**：A §2、§7 以 Worldometers 轉載之 IMF 2025 人均 GDP USD 99,365 × 人口 6.0 百萬推算 GDP 比例；本輪未搜尋，整合時應以 IMF WEO 最新版覆寫，所有「占 GDP %」同步重算。

---

## (c) 整體評估

- **數字可靠度：中高。** 28 項中 15 項確認、5 項修正、0 項駁斥；修正均屬口徑／版本／更新問題（新售 10,611→10,815、完工口徑、DMI 轉引、CaseTrust 家數、CASE 2025 補齊），無一為量級錯誤。住房交易、CASE 2024、Qanvast 區間、BCA／CaseTrust／DRC 門檻、C&W 單價、建築業外勞 DRC 等最關鍵數字全部通過獨立（含華文）搜尋。
- **主要弱點**：(1) 市場規模全靠研究機構模型（USD 7–8.6 億級，低信心）與一個 2020 年發布、兩輪皆未開頁的 F&S 承攬數字（S$48.75 億），後者本輪亦找不到；A 的住宅推估 S$27–35 億仍是最可用的量級，但須標明為自算。(2) KF USD 2,029/m² 被標「高」卻無法驗證。(3) 兩位分析師都漏掉 CASE 2026-02 已公布的 2025 年統計，並誤判了一個其實正確的部落格數字。(4) HDB 存量／HIP 官方數字雖有 PDF 存在，但未被開啟，A 的「約 110 萬戶、半數 ≥28 年」仍是推算。
- **法規面：可靠。** 設計端無證照、HDB DRC 強制且申請人須公民／PR、BCA BLS 門檻、CaseTrust 條件、EP 2027 調整、建築業外勞 DRC 1:5 均獲官方或多方獨立來源確認；B 的信心標示有兩處偏低（DRC 資格）、一處偏高（EP 45 歲門檻）。
- **建議整合策略**：以 URA／HDB／CASE／BCA／MOM 官方值為主幹，Qanvast 為每案價格，C&W 為商辦單價；研究機構市場規模僅作附註並統一改引官方頁；所有「繼承」數字（F&S、KF、人均 GDP）降為「低」並在表中加註「未驗證」。

---

## (d) 建議採用值

| 指標 | 建議值 | 年份 | 來源 URL | 信心 |
|---|---|---|---|---|
| HDB 轉售交易量 | 26,169 筆（−9.7%）；Q4 5,256 筆（五年低點） | 2025 | https://www.hdb.gov.sg/about-us/news-and-publications/press-releases/Upcoming-flat-supply-4Q2025-rpi | 高 |
| HDB 轉售價格年增 | +2.9%（2024：+9.7%）；Q4 季增 0% | 2025 | https://edgeprop.sg/property-news/hdb-resale-price-growth-slows-million-dollar-flats-prices-gain-23-4q2025 | 高 |
| 2025 年達 MOP 組屋數 | 6,973 戶（11 年新低）；2026 年第三方估約 13,480 戶 | 2025／2026E | https://www.99.co/singapore/insider/hdb-ura-q42025-statistics/ | 中（2026 值低） |
| 私宅新售（developer sales，不含 EC） | 10,815 戶（2024：6,469）；全年推出 11,482 戶 | 2025 | https://www.ura.gov.sg/news/media/pr26-05/ | 高 |
| 私宅完工 | 7,996 戶（含 EC，URA）；6,123 戶（不含 EC，ERA） | 2025 | https://www.ura.gov.sg/news/media/pr26-05/ | 高／中 |
| 私宅價格年增、未售庫存 | +3.3%；未售 16,193 戶（有規劃許可 39,746 戶） | 2025 | https://www.ura.gov.sg/news/media/pr26-05/ | 高 |
| 私宅全年交易總量 | 約 26,500 戶（ERA；新售 10,815＋轉售／轉手約 15,700） | 2025 | https://www.era.com.sg/research-articles/4q-2025-ura-private-quarterly-report | 中 |
| 住宅裝修年產值（承攬口徑） | S$27–35 億（≈USD 21–27 億）— A 自算，標「推估」；F&S S$48.75 億（2022E，含商用）僅作附註並標「未驗證」 | 2025 | SG-A §2.5；F&S 見 A 來源 4 | 低 |
| 室內設計服務市場（研究機構） | USD 7–8.6 億（DMI USD 0.7B；CMR 8.62 億）；CAGR 5.1–5.9% | 2025 | https://deepmarketinsights.com/vista/insights/interior-design-services-market/singapore | 低 |
| 傢俱＋家飾零售 | USD 11.3 億 → 15.5 億（2031），5.43% | 2025 | https://www.kenresearch.com/industry-reports/singapore-furniture-home-decor-market | 低 |
| 每案裝修費（組屋，Qanvast 2025 推估區間） | 4 房 BTO S$51,000–61,800；4 房轉售 S$64,300–80,300；交叉 MoneySmart 2026：BTO 51,000–70,000、轉售 55,000–85,000 | 2025–2026 | https://dollarsandsense.sg/how-much-does-it-cost-to-renovate-your-hdb-resale-flat/ ；https://www.moneysmart.sg/personal-loan/3-4-and-5-room-hdb-renovation-cost-ms | 中 |
| 每案裝修費（公寓） | 新公寓 S$40,400–51,500；轉售公寓 S$80,800–105,000（Qanvast 2025，315 案） | 2025 | https://qanvast.com/sg/articles/singapore-condo-renovation-costs-new-and-resale-in-2025-3389 | 中（未獨立驗證） |
| 每 m²／每坪（組屋，推算） | 4 房 ≈90 m²：BTO S$567–687/m²（≈NT$4.6–5.6 萬/坪）；轉售 S$714–892/m²（≈NT$5.8–7.3 萬/坪） | 2025 | 由上列 Qanvast 值換算（SG-A §3.4） | 低–中（面積為假設） |
| 設計費規範 | 主流為設計施工一體「免費設計」；獨立計費 5–15% 或每案 S$3,000–15,000（業者部落格，未驗證） | 2025–2026 | SG-A §3.5 | 低 |
| 辦公室 fit-out 單價 | **C&W 2026：新加坡 USD 140/ft²（≈USD 1,507/m²≈SGD 180/ft²≈NT$15.8 萬/坪）；東京 215、雪梨 161、香港 160**；KF USD 2,029/m² 僅附註「未驗證」 | 2026（2025-12 市況） | https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office/ | 高（C&W）／低（KF） |
| CASE 裝修投訴 | 2022：1,469；2023：1,168；2024：962（97% 非 CaseTrust）；2025：件數待開 PDF，排名第 4 | 2022–2025 | https://case.org.sg/wp-content/uploads/2025/02/Media-Release-CASE-sees-prepayment-losses-more-than-quadruple-in-2024-entertainment-related-complaints-nearly-triple.pdf ；https://www.case.org.sg/wp-content/uploads/2026/02/Media-Release——76.2-per-cent-surge-in-beauty-complaints-in-2025-with-consumers-losing-over-2.1m.pdf | 高 |
| 預付款損失 | 全行業 2024 S$193 萬 → 2025 S$271 萬（+40.4%）；裝修業 2024 S$728,814 → 2025 S$190,667（−73.8%） | 2024–2025 | 同上 | 高 |
| CaseTrust 認證裝修業者 | 逾 140 家（2025-02）；2025-03 起 80% 補貼、目標 500 家 | 2025 | https://singaporelawwatch.sg/Headlines/consumers-lost-almost-2m-in-prepayments-in-2024-highest-losses-from-home-renovations-case ；https://www.case.org.sg/casetrust/case-to-accredit-500-renovation-contractors-with-up-to-80-per-cent-in-subsidies-2/ | 高 |
| EP 最低月薪 | S$5,600（金融 6,200；45 歲以上 10,700）→ 2027-01-01 新申請 S$6,000（金融 6,600），續期 2028-01-01；45 歲以上 2027 值待 MOM 公布 | 2025–2027 | https://www.forvismazars.com/sg/en/insights/latest-insights-updates/outsourcing/work-pass-requirements | 高（底線）／低（年齡級距） |
| 建築業外勞 DRC | 83.3%（1:5），2024-01-01 起；MYE 同日廢除 | 2024– | https://www.mom.gov.sg/newsroom/press-releases/2022/0218-supporting-transformation-in-the-process-and-construction-sectors | 高 |
| BCA 標價指數 | 2025 約 +1%、2026 預估持平；顧問預測 2026 營建成本 +2–5% | 2025–2026 | SG-A §6（BCA 2026 簡報；未獨立搜尋） | 中 |
| HDB 存量／屋齡 | 以 HDB《Key Statistics FY2024/25》PDF 官方值取代 A 之「約 110 萬戶、半數 ≥28 年」推算 | FY2024/25 | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf | 待開頁 |


---

## (e) 法規要點確認

| 要點 | 確認內容 | 法源／主管機關 URL | 查核狀態 |
|---|---|---|---|
| 室內設計師執業 | 無法定執照、無名稱保護；MTI 2024-05 國會答覆明示不強制裝修／室內設計公司主要人員之最低資格；SIDAS（SIDS／SIDAC）為自願認證。台籍設計師持 EP 即可執業；涉及建築圖說、結構、消防須由本地 QP（註冊建築師／專業工程師）簽署 | https://www.mti.gov.sg/newsroom/written-reply-to-pqs-on-disputes-arising-from-interior-design-and-renovation-firms ；https://sidac.org.sg/wp-content/uploads/2025/07/SIDAS-Guidebook-Updated-as-of-22-July-2025.pdf | 確認（間接：答覆頁經獨立搜尋出現；內容未開頁） |
| HDB 組屋裝修許可與承包商 | 僅 DRC 列名承包商可承作並代申請許可；列名效期 2 年。**列名資格（HDB 官方頁）：申請人須為新加坡公民或永久居民；完成 BCA 學院「Renovation for Public Housing」課程；ACRA 登記；過去一年獲利；≥1 名全職員工；Pte Ltd 實收資本 ≥S$50,000；合夥人／董事無破產、無詐欺前科；申請費 S$100；21 工作天審核**。「3 年經驗」未見官方記載 | https://www.hdb.gov.sg/business/renovation-contractors/renovation ；https://www.hdb.gov.sg/business/renovation-contractors/windows ；https://www.hdb.gov.sg/cs/infoweb/business/renovation-contractors/renovation/directory-of-renovation-contractors-drc | 確認（條件取自 HDB 窗戶承包商列名頁；一般 DRC 頁逐條核對待開頁） |
| HDB 施工限制 | 新落成大樓 3 個月／既有大樓 1 個月／換窗 2 週；一般工程週一至六 09:00–18:00、噪音工程週一至五 09:00–17:00、週日與公假禁工；不得拆承重結構 | https://www.hdb.gov.sg/residential/living-in-an-hdb-flat/renovation/applying-for-approval | 未獨立搜尋（HDB 官方頁，B 已引） |
| BCA 建築商執照（BLS） | 法源《Building Control Act》第 29C 條等及 S 641/2008；GB1 不限金額、GB2 ≤S$600 萬（條文 S$300 萬已由部長公告上調）；實收資本 GB1 ≥S$300,000、GB2 ≥S$25,000；執照費 S$1,800／S$1,200；效期 ≤3 年；純裝飾工程是否構成「building works」仍須個案認定（B §2.3 矛盾未解） | https://www1.bca.gov.sg/regulatory-info/building-control/builder-licensing ；https://www1.bca.gov.sg/procurement/pre-tender-stage/builders-licensing-scheme-bls ；https://lawplayer.com/sg/act/BCA1989/29C | 確認 |
| CaseTrust 裝修認證（自願） | 首期訂金 ≤合約額 20%；須購買 Deposit Performance Bond（涵蓋歇業／清算／破產）；採 CaseTrust 標準裝修契約（分期付款、12 個月工藝保固、瑕疵由業者自費修復）；另有 CaseTrust-RCMA 聯合認證（須 RCMA 會員）；2025-03 起最高 80% 補貼、目標 500 家 | https://case.org.sg/casetrust/casetrust-accreditation-for-renovation-businesses/ ；https://www.case.org.sg/casetrust/wp-content/uploads/2025/08/Info-Kit-CaseTrust-for-Renovation-Businesses-Silver.pdf | 確認 |
| 非認證業者 | 無法定訂金上限、無法定標準契約、無強制保固；救濟途徑為 CASE 協商、小額索償法庭（S$20,000，雙方同意至 S$30,000）、刑事告訴 | https://www.judiciary.gov.sg/civil/cases-eligible-small-claim ；https://www.mti.gov.sg/newsroom/written-reply-to-pqs-on-disputes-arising-from-interior-design-and-renovation-firms | 未獨立搜尋（與現行法一致） |
| 外資設立 | 100% 外資可；至少 1 名常住董事、本地地址、公司秘書；最低資本 S$1（ACRA 一般規定） | SG-B §4.1（代辦來源） | 未獨立搜尋 |
| 外籍專業人員 | EP：2025 起 S$5,600／金融 6,200，45 歲以上 10,700；2027-01-01 新申請 S$6,000／金融 6,600（續期 2028-01-01）；COMPASS 40 分；45 歲以上 2027 值未公布 | https://www.forvismazars.com/sg/en/insights/latest-insights-updates/outsourcing/work-pass-requirements ；https://www.mom.gov.sg/ | 確認（底線）／待公布（年齡級距） |
| 外籍工人（建築業） | DRC 1:5（83.3%）自 2024-01-01；MYE 廢除、levy 結構調整；超額業者可留用至准證到期 | https://www.mom.gov.sg/newsroom/press-releases/2022/0218-supporting-transformation-in-the-process-and-construction-sectors ；https://www.mnd.gov.sg/newsroom/speeches/view/written-answer-by-ministry-of-national-development-on-the-number-of-local-smes-impacted-by-the-reduced-dependency-ratio-ceiling-(drc)-for-the-construction-sector | 確認 |
| 台星 ASTEP | 2014-04-19 生效；新加坡服務業保留清單是否涵蓋建築／室內設計未查（維持缺口） | https://www.enterprisesg.gov.sg/industries/wholesale-trade/astep | 未獨立搜尋 |
| 待讀官方文件（新發現） | MND「Written answer on accountability framework for renovation contractors」（兩份筆記皆未引）；CASE 2026-02 新聞稿全文；HDB Key Statistics FY2024/25 | https://www.mnd.gov.sg/newsroom/speeches/view/written-answer-by-ministry-of-national-development-on-accountability-framework-for-renovation-contractors | 整合階段必開 |

---

## 附：本輪搜尋紀錄（15 次）

| # | 查詢（重新措辭） | 語言 | 目的 | 對應項目 |
|---|---|---|---|---|
| 1 | HDB "Directory of Renovation Contractors" apply listing criteria Singapore Citizen Permanent Resident paid-up capital $50,000 three years experience | 英 | DRC 國籍／資本要件 | 11 |
| 2 | 消协 2024年 装修承包商 投诉 962起 预付款损失 72万8814元 非CaseTrust 97% | 華 | CASE 2024 | 7、9 |
| 3 | 建屋局 2025年全年 转售组屋 交易量 下跌 9.7% 转售价格指数 全年上涨 2.9% 第四季 | 華 | HDB 轉售 2025 | 1、2 |
| 4 | URA release 4th quarter 2025 real estate statistics private residential new sale units 2025 whole year completed units 2025 | 英 | URA 2025 | 3、4、5、6 |
| 5 | MOM Employment Pass qualifying salary raised 1 January 2027 $6,000 $11,500 age 45 Budget 2026 Committee of Supply | 英 | EP 2027 | 13、14 |
| 6 | CASE media release February 2026 renovation contractors complaints 2025 prepayment losses renovation industry CaseTrust accredited | 英 | CASE 2025（缺口） | 8、9 |
| 7 | Singapore office fit-out cost per square foot 2026 Cushman Wakefield Knight Frank most expensive Asia Pacific USD psf psm Tokyo Hong Kong | 英 | 商辦單價 | 16、17 |
| 8 | 新加坡 2025年 四房式 转售组屋 装修 费用 中位数 6万4300 8万300 BTO 5万1000 Qanvast 公寓 转售 8万800 | 華 | Qanvast 2025 | 18、19 |
| 9 | BCA general builder licence class 1 class 2 difference contract value not exceeding $6 million minimum paid-up capital $300,000 $25,000 licence fee | 英 | BLS 門檻 | 12 |
| 10 | CaseTrust renovation businesses accreditation criteria deposit performance bond protects deposit up to 20% standard renovation contract workmanship warranty defects liability | 英 | CaseTrust 條件 | 10 |
| 11 | MOM construction sector dependency ratio ceiling reduced 87.5% to 83.3% 1 January 2024 Man-Year Entitlement MYE replaced new levy framework | 英 | 建築業外勞 | 15 |
| 12 | Singapore interior design market size report 2025 USD million CAGR forecast 2030 2033 Mordor IMARC Cognitive 6Wresearch | 英 | 研究機構市場規模 | 20–24 |
| 13 | HDB annual report 2024/2025 key statistics flats under management Home Improvement Programme 29,000 flats 371 blocks $407 million FY2025 | 英 | HIP／存量 | 26 |
| 14 | Frost & Sullivan Singapore interior fitting-out works market size S$4,875 million 2022 prospectus industry overview HKEX | 英 | F&S 承攬口徑 | 25 |
| 15 | MND written answer accountability framework renovation contractors parliament HDB Directory of Renovation Contractors CaseTrust licensing interior designers 2025 2026 | 英 | 政策動向 | 27 |

未使用保留額度：2 次。未搜尋而以法規常識判定者（SCT 上限、裝修貸款上限、外資設立、ASTEP、HDB 施工時段）均在表中標明。
