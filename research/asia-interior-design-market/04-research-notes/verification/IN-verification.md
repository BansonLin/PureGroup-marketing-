# 印度（India）— 對抗式查核報告（WP6）

| 項目 | 內容 |
|---|---|
| 查核日期 | 2026-10-09 |
| 查核者 | Claude 子代理（IN-verification，懷疑立場） |
| 查核對象 | `countries/IN-A-market.md`（視角 A：市場）、`countries/IN-B-rules.md`（視角 B：法規） |
| 方法 | 14 次獨立 WebSearch（均避開分析師附錄所列查詢字串；其中 2 次以 allowed_domains 鎖定研究機構官網與印度內政部／移民局官網）；第 15 次搜尋（C&W 2026 商辦裝修成本）因本回合共享搜尋額度耗盡而未執行。WebFetch／curl 被封鎖，證據為搜尋引擎回傳之頁面摘要與引文。另以人工算術複核兩份筆記之匯率／面積換算與占比計算。預設立場：主張在證據支持前視為錯誤 |
| 結果 | 查核 23 項：**確認 9、修正 8、駁斥 0、無法查證 6**；另列 14 項內部矛盾／定義問題 |
| 保留額度 | 依任務規定保留 2 次；實際因共享額度耗盡，第 15 次亦未執行 |

---

## (a) 逐項查核表

| # | 項目 | 原報告值 | 查核結果 | 修正值 | 證據 URL | 說明 |
|---|---|---|---|---|---|---|
| 1 | 室內設計市場數值：Mordor／IMARC／Grand View（A §1、§2、§8） | Mordor USD 314.3 億（2025）→650.1 億（2031），CAGR ≈12.9%（分析師反推）；IMARC USD 368.9 億（2025）、CAGR 8.16%；Grand View USD 15.6 億（2024）、CAGR 5.9% | **確認** | Mordor USD 314.3 億（2025）→354.8 億（2026）→650.1 億（2031），**CAGR 12.87%（Mordor 公布值，非反推）**；IMARC USD 368.9 億（2025）→747.3 億（2034），8.16%（2026–2034）；Grand View USD 15.603 億（2024），5.9%（2025–2030） | https://www.mordorintelligence.com/industry-reports/india-interior-design-market ；https://www.imarcgroup.com/india-interior-design-market ；https://www.grandviewresearch.com/horizon/outlook/interior-design-market/india | 數字轉錄正確。IMARC 同一頁另載「CAGR 24.30%（2025–2033）」，與 8.16% 自相矛盾（見 (b)）；TechSci／P&S／VMR 本輪未重查 |
| 2 | 口徑標籤「D+FU+施工＝設計＋傢俱家飾＋施工」（A §2 對照表、§7、§9 啟示 1） | A 判讀 USD 300 億級數字為「設計＋櫃體傢俱＋施工」整體產值，「家居零售＋裝修工程鄰接總量」 | **修正（定義）** | Mordor 自述方法論：**僅計「在印度交付之室內設計服務價值」，排除傢俱、家飾、建材之獨立銷售**（stand-alone sale） | https://www.mordorintelligence.com/industry-reports/india-interior-design-market | 「含傢俱零售」為分析師推論，與 Mordor 聲明相反。Grand View 與 Mordor 的 20 倍差距無法用「含傢俱零售」解釋，較可能是 Mordor 計入施工／fit-out 執行工程費；TechSci／IMARC 範圍未知。最終報告應改稱「研究機構廣義口徑（各家定義不一、疑含執行工程）」，刪除「含傢俱家飾零售」之敘述 |
| 3 | 商用占室內設計市場 74.44%（Mordor FY25）／≈75%（IBEF 引 P&S 2023）（A §1、§2、§8、§9；B §5） | 商用 74–75%、住宅僅約 25% 但成長最快（住宅 CAGR 16.47%） | **修正（無共識）** | 三組互相矛盾之數字：(1) Mordor 主報告商用 74.44%（2025）、住宅 CAGR 16.47%；(2) **IMARC 2026–2034 版：住宅領先、占 60%（2025）**（IMARC 前一版 2025–2033 則稱商用占多數）；(3) **Mordor《Interior Design Services》印度頁：住宅 57.39%（2025），且稱商用為成長最快區隔（CAGR 12.26%）**——與主報告相反 | https://www.mordorintelligence.com/industry-reports/india-interior-design-market ；https://www.imarcgroup.com/india-interior-design-market ；https://www.mordorintelligence.com/industry-reports/interior-design-services-market | 商用占比不應以單一值寫入報告；A §9 啟示 1「真正有量的是商辦」以 74% 為前提，須改寫為「研究機構對住宅／商用占比無共識（商用 40–74%）」。Mordor 兩份報告中 57.39% 同時出現為「住宅占比」與「新建占比」，疑為標籤錯誤 |
| 4 | 新建 vs 翻修（A §2：Grand View 新建最大／翻修最快；Mordor 住宅營建新建 81.2%／翻修 18.8%） | 如左 | **確認（並補充）** | Grand View：翻修為成長最快區隔（確認）。**補充 IMARC 室內設計口徑：2025 年新裝（new decoration）56%／翻修（renovation）44%**。Mordor 住宅營建 81.2%／18.8% 本輪未獨立查核 | https://www.grandviewresearch.com/horizon/outlook/interior-design-market/india ；https://www.imarcgroup.com/india-interior-design-market | IMARC 翻修 44% 遠高於 Mordor 住宅營建口徑之 18.8%，因前者含商用翻修且不含新建結構工程；A §2 推論「存量翻修在統計上仍是小眾」須加註「僅就住宅營建口徑而言」 |
| 5 | IMARC「home improvement services」USD 126 億（2025）→176 億（2034），CAGR 3.59%（A §2、§7、§8） | 如左 | **確認（版本差）** | 獨立搜得 IMARC 前一版：**USD 121.0 億（2024）→170.8 億（2033），CAGR 3.90%（2025–2033）**；121.0×1.039≈125.7，與 A 之 2025 值 126 億相容 | https://www.imarcgroup.com/india-home-improvement-services-market | 兩版皆為 IMARC 自家估計，非獨立來源；量級可採用，年份須標明版本 |
| 6 | Global Market Insights 印度 remodeling 市場 ≈USD 380 億（2025），CAGR 9.5%（A §1、§2、§7、§8） | 如左（A 標低信心） | **無法查證** | — | （獨立搜尋未回傳 GMI 印度分項；另得 Deep Market Insights「India Home Services」USD 74.7 億（2025）→207 億（2034）、CAGR 12.03%，為又一不相容口徑：https://deepmarketinsights.com/vista/insights/home-services-market/india ） | GMI 為全球報告之印度分項，摘要無法核對；不建議作主值，僅可作「廣義口徑上限」註腳 |
| 7 | 住宅全屋單價分級 Rs 800–1,200／1,200–2,000／2,000–3,500+ per ft²（2025）；2026 版 1,200–1,800／1,800–3,000／3,000–5,500／5,500–10,000+（A §1、§3、§7、§8） | 如左（全部來自業者報價頁） | **確認（區間；補獨立中階錨點）** | 獨立 2026 估算：**1,000 ft² 2BHK 中階全屋（設計＋施工）Rs 14–25 lakh ≈ Rs 1,400–2,500/ft²；1,500 ft² 3BHK Rs 21–37 lakh ≈ Rs 1,400–2,470/ft²**；另一指南 2BHK 全國平均 Rs 8–15 lakh（≈Rs 800–1,500/ft² 以 1,000 ft² 計） | https://constructionestimatorindia.com/?p=17098 ；https://constructionestimatorindia.com/?p=11246 ；https://housiey.com/blogs/?p=8016 | A 之中階帶（2025：1,200–2,000；2026：1,800–3,000）與獨立錨點 1,400–2,500 相容。「豪宅 5,500–10,000+」僅 nearmeinteriors 單一來源，未獲獨立證實。注意同一網站「基本」級由 2025 版 800–1,200 升至 2026 版 1,200–1,800（+50%），屬分級重新定義而非通膨，報告不可將兩版並列為時間序列 |
| 8 | 每案均價：2BHK Rs 4–18 lakh、3BHK Rs 6–35 lakh（A §1、§3、§7、§8）；2BHK Rs 2.5–28 lakh、3BHK Rs 7–35 lakh（B §1、§5、§9） | 兩筆記區間不一致 | **修正（下限與上限）** | **HomeLane 官方（浦那）起價：2BHK 基本 Rs 3.4／舒適 4.8／豪華 5.8 lakh；3BHK 4.5／6.1／7.3 lakh（僅含廚房＋各房衣櫃＋電視櫃）**；全屋中階 2BHK Rs 14–25 lakh、3BHK Rs 21–37 lakh；2BHK 平均 Rs 8–15 lakh（2026） | https://www.homelane.com/design-ideas/buying-guides/interior-design-cost-in-pune-for-2bhk-home/ ；https://constructionestimatorindia.com/?p=17098 ；https://housiey.com/blogs/?p=8016 | B 的 2BHK 下限 Rs 2.5 lakh 無獨立佐證（組織化連鎖最低起價 3.4 lakh）；3BHK 中階全屋獨立上限達 Rs 37 lakh，高於兩筆記之 35 lakh。建議改以「模組化套裝起價／典型／都會全屋中階」三段呈現（見 (d)），並註明「起價」口徑僅含櫃體 |
| 9 | 設計費 Rs 50–500/ft² 或工程款 5–15%（豪宅至 25%）（A §3、§7、§8）；總價 7–15%（B §1、§5、§9） | 如左 | **確認（區間；典型帶較窄）** | 獨立來源：印度費用計算器室內設計 **Rs 100–250/ft²**；商業來源室內設計費 **4–15%** 工程費；CoA 2020《Conditions of Engagement and Scale of Charges》建築設計費率表（第三方轉載，標「指示性」）約 8–10%（工程 ≤Rs 50 lakh）遞減至 4.5–6%（>Rs 50 crore）；**無室內設計專用之 CoA 官方費率** | https://aecord.com/tools/architect-fee-calculator ；https://www.studiomatrx.org/guides/architect-fee-structures-india ；https://www.houseyog.com/blog/architect-fees-charges-for-house-designing-in-india | A「豪宅至 25%」僅見業者頁，未獨立證實，應標「單一來源」。A §3 推論「台灣設計費 NT$3,000–8,000/坪 ≈ Rs 240–640/ft² 落在印度頂級帶」算術正確。A §10 缺口「IIID／CoA 官方收費指引」：本輪確認 CoA 僅有建築費率表，無室內設計版本 |
| 10 | 商辦裝修成本 C&W 2026：INR 5,847–6,567/ft²（USD 65–73/ft²），孟買最高、亞太最低（A §1、§3、§6、§7、§8，標「高信心」；B §7、§9） | 如左 | **無法查證（搜尋額度於此項耗盡）** | 間接證據：JLL《APAC Fit-Out Cost Guide 2025》確認印度城市位於亞太指數最低端、以美元計最便宜；媒體轉述 JLL：**孟買高於全國均值 7%、班加羅爾低於均值 5%**；APAC 中規格均值 USD 1,524/m²（≈142/ft²）、全球 1,949/m²。另一第三方引 C&W「班加羅爾中規格辦公室 USD 449/m²（≈42/ft²）」 | https://www.jll.com/en-jp/insights/apac-fit-out-cost-guide-2025 ；https://www.dtnext.in/lifestyle/technology/indias-tech-hubs-offer-5-10-pc-lower-office-fit-out-costs-in-asia-pacific-834649 ；https://beaconfiling.com/blog/office-interior-fitout-india-cost | C&W 不同規格數字相差 1.6–1.9 倍（USD 449 vs 700–786/m²），A 的 USD 65–73/ft² 對應「協作式混合辦公」規格；建議信心由「高」降為「中」，並在與台北 NT$16.6 萬/坪比較時註明規格須一致。JLL 2025 印度絕對值僅在正文表格，摘要未載 |
| 11 | 辦公室總租賃 2025：83.3（JLL）／86.4（KF）／≈89（C&W）百萬 ft²；2026Q1 21.5 百萬 ft²（A §1、§6、§8） | 如左 | **無法查證（本輪未搜）** | — | — | 三家城市覆蓋與定義不同，A 已註明；保留但標「未獨立查核」。A §2 以租賃量 × 單位成本推算商辦裝修產值已自標「不得引用」，正確 |
| 12 | Anarock 前 7 大城市 2025：銷售 395,625 戶（−14%）、新推案 419,170（+2%）、未售 576,617（+4%）（A §1、§3、§6、§7、§8） | 如左 | **確認（補其他機構）** | Storyboard18 轉述 Anarock：7 城銷售 **−14%**、成交金額 +6% 至 Rs 6 lakh crore；**Knight Frank 8 城 2025 銷售 348,207 戶**（高價位占 50%）；**PropEquity 9 城：Q1 105,791（−23%）、Q2 94,864（−19%）、Q3 100,370（−4%）、Q4 推案 88,427（−10%）**；Square Yards 9 城登記 5.45 lakh（−5%，至 2025-12-25） | https://www.storyboard18.com/amp/how-it-works/top-7-cities-see-14-drop-in-housing-sales-in-2025-but-deal-value-rises-6-to-%e2%82%b96-lakh-crore-88119.htm ；https://realtynmore.com/premium-housing-captures-50-of-indias-348207-residential-sales-in-2025-knight-frank-india/ ；https://therealtytoday.com/news/housing-sales-decline-by-19-across-nine-cities-mumbai-thane-see-sharpest-fall-propequity-report ；https://realtynmore.com/housing-sales-drop-23-supply-falls-34-top-9-cities-in-q1-2025-says-propequity/ ；https://www.outlookmoney.com/real-estate/housing-sales-slip-4-in-q3-2025-across-top-cities-new-launches-stay-flat ；https://www.outlookbusiness.com/news/registration-of-homes-dips-5-to-545-lakh-units-till-dec-25-this-year-across-9-cities-square-yards | 方向與量級獲三家獨立機構佐證；絕對數因城市覆蓋不同不可互換。成交**金額**反升 6%，顯示高價位占比上升，與 A §3「付費裝修集中於都市中高收入層」推論一致 |
| 13 | PMAY-U 累計完工 99.07 lakh（2026-07）；CRISIL 全國住房短缺 6,150 萬戶（2025）（A §1、§3、§8） | 如左 | **無法查證（本輪未搜）** | — | — | 官方儀表板數字，與 2025-01 之 90.25 lakh 連貫；CRISIL 數字為 HomeFirst 部落格轉述，A 已標中信心。保留 |
| 14 | 住宅中古 vs 新屋交易占比「無資料」（A §1、§3、§7、§10；B §5） | 兩位分析師均列為缺口 | **修正（缺口可補）** | **Square Yards／Grant Thornton Bharat：FY2025（2024-04～2025-03）全國登記住宅交易中二手（resale）占 43%（FY2019 為 38%），一手（在建）57%**；孟買二手約 69,000 戶 vs 一手約 71,000 戶（≈49%，本人計算）；諾伊達／大諾伊達二手占 40%（原 29%） | https://www.squareyards.com/research-reports/fy2025-residential-registrations-rise ；https://www.outlookmoney.com/real-estate/residential-registrations-skyrocket-since-fy2019-primary-sales-lead-but-secondary-gains-ground | 一次搜尋即得，兩位分析師未嘗試。住宅存量屋齡仍無資料。A §2 推論「存量翻修是小眾」與「二手交易占 43%」並不衝突（二手交易不必然裝修），但報告應補入此數並改寫「無資料」 |
| 15 | 室內設計師無執照：Architects Act 1972 §37 僅保護「architect」名稱；最高法院 2020 *Council of Architecture v. Mukesh Goyal*（B §1、§2.1、§2.2、§9；A §1、§4） | 如左 | **確認** | 最高法院 2020-03-17（Chandrachud、Rastogi 二人庭）：§37 **不禁止未註冊者從事建築業務及相關活動**，僅禁止使用「architect」名稱與樣式；僱用自稱建築師者應確認其具資格與註冊；NOIDA 不得將無認可學位者任用於冠「architect」之職位 | https://api.sci.gov.in/supremecourt/2014/21001/21001_2014_3_1501_21539_Judgement_17-Mar-2020.pdf ；https://www.scconline.com/blog/post/2020/03/18/unregistered-individuals-can-practice-architecture-but-cant-designate-themselves-as-architects/ ；https://barandbench.com/news/litigation/registration-of-architects-under-the-architects-act-and-bar-on-using-the-title-what-the-supreme-court-said | 補充：德里高院其後於 *Council of Architecture v. Manohar Krishnaji Ranade* 對該判決作出區分（https://law.asia/unregistered-architects-build-name/ ），B 未提及；對「室內設計師無執照」之結論無影響，但「Interior Architect」名稱風險應維持 |
| 16 | 孟買裝修許可：BMC Act §342 結構變更須「事前書面許可」；非結構工程僅需社區 NOC（B §1、§2.1、§2.4、§9、§10） | 如左（來源為業者指南） | **修正（機制與清單）** | §342 區分 **「可耐住修繕（tenantable repairs）」**（抹灰、油漆、勾縫、換地磚、廁浴修繕、排水管更換、同材質換屋面、露台防水）——**不需市政許可但需社區 NOC**；其餘拆除／變更／重建須依 §342 **向市政專員送交通知**（§344 規定表格：位置、性質與範圍、監工人姓名），由建管（Executive Engineer, Building Proposal）處理；**禁止降低基座、基礎或樓板**；砌磚牆需 BMC 許可，玻璃／木質／板材輕隔間不需（不得動柱梁）；MHADA 2026-07 核准 Borivali 兩戶合併即依 §342 通知程序 | https://housing.com/news/beware-of-illegal-renovations-bmc-guidelines-for-house-repairs ；https://www.kaanoon.com/274607/partition-wall ；https://mhada.gov.in/sites/default/files/BPC_Mumbai-1_dtd-09-07-2026.pdf ；https://ghar.tv/blog/bmc-changes-rules-for-renovating-your-homes/artid36 | B 的「事前書面許可」應改為「依 §342／§344 送交通知並經建管核可」；B 列出的「需 BMC 許可」項目（承重牆、合併兩戶、移廚衛、封陽台、夾層）與獨立來源相容。另一報導稱 BMC 曾放寬「調整格局不必再向 BMC 申請」，日期不明，列為待查 |
| 17 | 未經許可施工罰款 Rs 10,000–1 lakh＋拆除（B §1、§2.4(c)、§9、§10） | 如左（AMS Civil Work，條文出處未註） | **無法查證** | — | （獨立來源僅載「拆除通知、法律後果」，無金額） | 金額應標「業者指南，未經條文核對」；拆除令與社區訴訟風險之敘述可保留 |
| 18 | Press Note 3 (2020) 陸鄰國審查不適用台灣（B §1、§4、§9；T3 台商進入評分 4/4） | 「台灣不適用」，標「中–高信心」 | **修正（信心下調）** | PN3 未點名任何國家，**亦未澄清台灣／香港／澳門之適用**；2020 年 Tribune 報導：印度政治上視台灣為中國一部分、曾研議台資是否須審查，而香港被視為獨立、走自動路徑；律師事務所意見分歧（law.asia：「需官方澄清」；另一所主張不適用）；實務上台商多以自動路徑設 100% 子公司，台灣對印 FDI 2019–2023 累計逾 USD 6.65 億 | https://law.asia/press-note-3-restriction-investment/ ；https://www.tribuneindia.com/news/business/taiwan-may-be-treated-as-separate-entity-for-fdi-94367 ；https://touchstonepartners.com/press-note-3-of-2020-a-first-anniversary-edition/ ；https://www.vjmglobal.com/zh/blog/business-setup-india-taiwan-bsic ；https://www.taiwannews.com.tw/en/news/5903318 | B 的「中–高信心」過高，應改「中／低；無官方澄清，實務多走自動路徑」，並加註「若股東含中國大陸之受益所有人則須政府核准；建議取得印度律師書面意見」。T3 之「設計 4／承攬 4」評分應加此但書 |
| 19 | Employment Visa 年薪下限 USD 25,000（≈Rs 16.25–20 lakh，各源不一）（B §1、§4、§8、§9、§10） | 如左 | **確認（補官方盧比值）** | **MHA 工作簽證 FAQ：年薪須逾 USD 25,000**，未達者可被駐外館處拒簽；豁免：民族廚師、非英語語言教師／翻譯、使領館人員。**MHA／BOI 另以盧比表述：Rs 16.25 lakh／年**（中央高教機構教師 Rs 9.10 lakh；BPO／ITES 不得豁免；停留 <1 年按比例計） | https://www.mha.gov.in/sites/default/files/2022-08/work_visa_faq[1].pdf ；https://boi.gov.in/boi/contents/travelling-to-india/foreigners/work-in-india ；https://www.mha.gov.in/PDF_Other/AnnexIII_01022018.pdf | Rs 16.25 lakh 是官方門檻之盧比版本（源自舊匯率），非匯率換算；B「各來源換算不一」之疑可解。以 B 自身匯率 86 計，USD 25,000 ＝ Rs 21.5 lakh，Wisemonk「Rs 20 lakh+」非官方。B §10 已正確提醒需移民專業確認 |
| 20 | 消保救濟條號：CPA 2019 §2(11)／§2(47)；「§35 允許在消費者住所地、付款地或營業地提告，並可 e-Daakhil 線上立案」；時效 2 年（B §1、§3、§9） | 如左 | **修正（條號）** | 地域管轄為 **§34(2)**：(a) 對造居住／營業／分支機構／工作地，(b) 對造實際自願居住或營業地（須委員會許可），(c) 訴因全部或部分發生地，(d) **申訴人居住或工作地**；**§35** 規範「誰可提告」（消費者、消費者團體、共同利益之多數消費者、中央／邦政府）及**電子提告**但書；**時效 2 年為 §69(1)**，§69(2) 得以正當理由寬限但須載明理由；地區委員會金額管轄 ≤Rs 1 crore（§34(1)，中央可另定） | https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/34.php ；https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/35.php ；https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/69.php ；https://www.casemine.com/in/column/territorial-jurisdiction-of-consumer-fora-in-india/view | 實質結論（可在住所地提告、2 年時效、可線上立案）正確，但條號錯置：報告應寫「§34(2)(d)／§35／§69」。「付款地」非法條用語，應改為「訴因發生地」。Consumer Protection (Jurisdiction) Rules 2021 已將地區委員會門檻改為 ≤Rs 50 lakh（本輪未查，B §11 已列缺口）。報價單中「專屬管轄其他城市」條款不能排除消費者住所地管轄（上訴判例） |
| 21 | IKEA India FY25：營收 Rs 1,749.5 crore（−3.33%）或 Rs 1,860 crore（+6%）兩源不一；淨損 Rs 1,325.2 crore（A §1、§4、§8、§10） | 兩源矛盾未解 | **修正（採申報值）** | **Tofler 申報（2026-02 報導）：營業收入 Rs 1,749.50 crore（FY24 1,809.80，−3.33%）；總收入 Rs 1,780.10 crore（−3.9%）；虧損 Rs 1,325.2 crore（FY24 1,299.40）**；廣告費 Rs 223.9 crore（+14.06%）；借款 Rs 8,335.2 crore（FY24 7,060）；Ingka Holding Overseas BV 持股 99.9%；目標 FY28 獲利、4–5 年開 25 家中小型店；NCR 投資約 Rs 7,000 crore | https://ianslive.in/ikea-indias-loss-widens-to-rs-1325-crore-in-fy25-revenue-dips--20260204142638 ；https://www.indianretailer.com/news/retail-india-news-ikea-india-loss-widens-rs-13252-cr-fy25 ；https://www.outlookbusiness.com/corporate/ikea-aims-to-be-profitable-by-fy28-to-open-25-new-small-medium-size-stores-in-next-4-5-years | Business Standard 2025-11 之 Rs 1,860 crore（+6%）與 ROC 申報值衝突，疑為初步數或不同口徑，**採申報值 1,749.5**。部分媒體誤將 FY24 虧損 1,299.4 寫成 FY25，整合時勿混用。A §10 缺口 7「IKEA 兩源矛盾原因」可結案 |
| 22 | BIS《合板與木質平板門品質管制令 2024》2025-02-28 生效；小型企業 2025-05-28、微型 2025-08-28；進口品亦適用（B §1、§2.5、§7、§9、§10） | 如左 | **確認** | 公報 **S.O. 1377(E)（商工部 2024-03-15）**，取代 2023 年同名命令；生效 **2025-02-28**；小型企業 2025-05-28、微型企業 2025-08-28；適用既有執照持有人、新申請人、製造商、**進口商**與銷售者；**出口用製品除外**；一般用途合板 IS 303:1989、裝飾合板 IS 1328:1996、防火合板 IS 5509:2021、模板合板 IS 4990:2011、平板門 IS 2202(Part 1):1999；違者依 BIS Act 2016 處罰 | https://alephindia.in/pdf/bis-qco-for-polywood-and-wooden-flush-door-shutters.pdf ；https://alephindia.in/bis-qco-for-the-Plywood-for-general-purposes.php | 《木質板材 QCO 2024》2025-02-11 生效一節本輪未另行查核；B 所引「一來源稱曾延後」為 2023 版舊訊，2024 版公報已取代，可結案 |
| 23 | 公司稅：印度子公司 22% 優惠→有效 25.17%；外國公司分公司 35%＋附加費＋4% 捐 ＝ 36.40–38.22%（Finance Act 2024 由 40% 調降）（B §1、§4、§9、§10） | 如左 | **無法查證（本輪未搜）** | — | — | 與 Finance Act 2024 之法定結構算術一致（22%×1.10×1.04＝25.168%；35%×1.04＝36.4%；35%×1.05×1.04＝38.22%）；保留並維持 B「需稅務專業確認」之標註 |

---

## (b) 內部矛盾與定義問題

1. **匯率不一致（兩筆記）**：A 用 1 USD＝INR 88＝NT$31.0（1 INR＝NT$0.352）；B 用 INR 86＝NT$31.5（1 INR＝NT$0.366）。同一盧比數字之新台幣值相差 4%（例：Livspace Rs 1,460 crore＝NT$51.4 億（A）vs NT$53.5 億（B）；USD 1.66 億 vs 1.70 億）。兩筆記內部算術均正確（本輪複核 A §3 單價表、每案換算、C&W 每坪、設計費每坪、人均 GDP≈Rs 2.35 lakh、人均裝修支出 USD 21–25／GDP 0.8–0.9%、Grand View 人均 USD 1.1／GDP 0.04%、Mordor 翻修子集 USD 496 億、HomeLane 材料 43%／人事 32%／廣告 11%；B §6 日薪換算、§9 各換算），**整合時統一一組匯率並標註日期即可**。
2. **Employment Visa 盧比值**：B 稱 USD 25,000≈Rs 16.25–20 lakh「各來源換算不一」。以 B 自身匯率 86 計應為 Rs 21.5 lakh；Rs 16.25 lakh 實為 MHA／BOI 官方之盧比門檻（舊匯率時代訂定），非換算值。
3. **Mordor 口徑**：A 將 Mordor USD 314 億判讀為「設計＋傢俱家飾＋施工」，Mordor 自述排除傢俱／家飾／建材獨立銷售（見 (a)#2）。A §2「定義差異說明」(1) 與 §7「廣義『室內設計』人均支出 USD 21–25」之口徑註解須改寫。
4. **住宅／商用占比三組矛盾**：Mordor 主報告商用 74.44% vs IMARC 最新版住宅 60% vs Mordor services 報告住宅 57.39%；Mordor 兩報告對「哪個區隔成長最快」結論相反（見 (a)#3）。A §1、§2、§9 與 B §5 皆以「商用 74–75%」為定論，屬過度確定。
5. **IMARC 同頁雙 CAGR**：8.16%（2026–2034）與 24.30%（2025–2033）並存；A 僅引 8.16%，應加註。
6. **翻修占比四個不相容口徑**：Grand View「翻修成長最快」（設計服務）、IMARC 翻修 44%（室內設計）、Mordor 住宅營建翻修 18.8%（營建）、GMI remodeling USD 380 億 vs IMARC services USD 126 億 vs A 自算 Mordor 子集 USD 496 億（3 倍差距）。A §2 表已把「USD 496 億」標為本人計算，但 §8 關鍵數字總表仍列為 Mordor 行，**不得以 Mordor 名義引用**。
7. **住宅單價「基本級」一年內上調 50%**：nearmeinteriors 2025 版基本 Rs 800–1,200 → 2026 版 1,200–1,800，A §3 單價表將兩版並列，讀者易誤讀為通膨；實為同一網站重新分級。
8. **每案均價兩筆記不一致**：A 2BHK Rs 4–18 lakh／3BHK 6–35 lakh；B 2BHK Rs 2.5–28 lakh／3BHK 7–35 lakh。B §5 已指出原因（「僅模組化櫃體」與「全屋含假天花、油漆、電氣」口徑混用），但 B §1 摘要與 §9 總表仍以 2.5–28 lakh 呈現。
9. **設計費百分比**：A 5–15%（豪宅 25%）vs B 7–15%；獨立來源 4–15%。差異在來源取樣，非事實衝突；「25%」單一來源。
10. **CPA 2019 條號錯置**：B 將地域管轄歸於 §35，應為 §34(2)(d)；時效 2 年未註條號（§69）。
11. **BMC §342 性質**：B 寫「事前書面許可」，獨立來源顯示為「通知（§342／§344）＋可耐住修繕豁免清單」；B 列出的「需 BMC」項目本身正確。
12. **Press Note 3 信心**：B §4 標「中–高信心」且 T3 評分 4/4，但無任何官方澄清；2020 年政府曾研議對台資審查（見 (a)#18）。
13. **其他兩筆記已自標之矛盾（本輪未解）**：Livspace 裁員 100 vs >1,000 人；IIID 會員 6,800／8,000／10,000（不同年份快照）；飯店管線 LE 137,601 間 vs「品牌管線 >114,000 間」（口徑不同）；§24(b) 修繕利息扣除 Rs 30,000 vs 不適用；SBI 修繕貸款 7.25% vs 9.15%；CREDAI 缺工 1,000 萬未註年份。
14. **A 之內部推算混入關鍵數字總表**：§8 總表「Mordor 住宅營建翻修子集 ≈USD 496 億」與「商辦裝修潛在產值 USD 54–65 億（§2(c)，已自標不得引用）」均為分析師計算，整合時須與來源原數明確區隔。

---

## (c) 整體評估

- **數字轉錄品質高**：23 項中 9 項確認、0 項駁斥；研究機構數值（Mordor、IMARC、Grand View）、Anarock 住宅銷售、最高法院判決、MHA 簽證門檻、BIS QCO 日期、IKEA 申報值均與獨立來源一致。A 的 Mordor CAGR「≈12.9%（反推）」實為 Mordor 公布之 12.87%。
- **主要弱點在「解讀」而非「數字」**：(1) 研究機構口徑被分析師自行定義為「含傢俱零售」，與 Mordor 聲明相反；(2) 「商用占 74%」被當作定論並據以推導對台啟示，但三份報告互相矛盾；(3) 法規條號兩處錯置（CPA §34 vs §35；BMC §342「許可」vs「通知」），結論方向正確但引用時會被專業讀者挑出；(4) Press Note 3 對台灣之適用被標為中–高信心，實則無官方澄清。
- **缺口判斷有一處錯誤**：「中古交易占比無資料」一次搜尋即可補齊（FY2025 二手占 43%），兩位分析師共 40 次搜尋未嘗試。
- **無法查證的 6 項**（GMI 380 億、C&W 2026 單位成本、辦公室租賃、PMAY-U／CRISIL、罰款金額、公司稅）多因本輪搜尋額度限制而非證據不存在；其中 C&W 2026 為 A 唯一標「高信心」的商辦數字，建議降為「中」並註明規格。
- **總體品質：中（medium）**。市場數字可直接採用（附口徑註解），法規章節須依 (e) 修正條號與信心等級後採用。

---

## (d) 建議採用值

（匯率統一建議：1 USD＝INR 88＝NT$31.0，1 INR＝NT$0.352，與 A 一致；換算面積 1 坪＝35.58 ft²。NT$ 值為本人換算，非來源原數。）

| 指標 | 建議值 | 年份 | 證據 URL | 信心 |
|---|---|---|---|---|
| 室內設計市場（研究機構廣義口徑；註明「Mordor 排除傢俱／家飾／建材獨立銷售，各家定義不一」） | **USD 310–370 億**（Mordor 314.3 億／IMARC 368.9 億）；CAGR **8–13%**（IMARC 8.16%、Mordor 12.87%）；2031 年 Mordor USD 650 億 | 2025 | https://www.mordorintelligence.com/industry-reports/india-interior-design-market ；https://www.imarcgroup.com/india-interior-design-market | 低–中 |
| 純設計服務市場 | **USD 15.6 億**（2024）→21.8 億（2030），CAGR 5.9%；≈人均 USD 1.1、GDP 0.04% | 2024 | https://www.grandviewresearch.com/horizon/outlook/interior-design-market/india | 中（單一來源） |
| 住宅／商用占比 | **不採單一值**：「商用 40–74%」（IMARC 住宅 60%；Mordor 商用 74.44%；Mordor services 住宅 57.39%） | 2025 | （同上三頁） | 低 |
| 新裝 vs 翻修（室內設計口徑） | **新裝 56%／翻修 44%**（IMARC）；住宅營建口徑新建 81%／翻修 19%（Mordor，未獨立查核） | 2025 | https://www.imarcgroup.com/india-interior-design-market | 低–中 |
| 住宅居家改善服務市場 | **USD 126 億**（2025）→176 億（2034），CAGR 3.6–3.9%；GMI「remodeling USD 380 億」僅作廣義上限註腳 | 2025 | https://www.imarcgroup.com/india-home-improvement-services-market | 低–中 |
| 住宅全屋單價（設計＋施工，carpet area 計） | **模組化套裝／基本 Rs 800–1,200/ft²**（≈NT$1.0–1.5 萬/坪）；**都會中階 Rs 1,400–2,500/ft²**（≈NT$1.75–3.1 萬/坪）；**高階 Rs 3,000–5,500/ft²**（≈NT$3.8–6.9 萬/坪，單一來源）；GST 18% 另計 | 2026 | https://constructionestimatorindia.com/?p=17098 ；https://nearmeinteriors.com/interior-design-cost-per-square-foot-in-india-2026-guide-what-youll-really-pay-for-home-interiors/ | 中（業者頁，多源相容） |
| 每案均價 2BHK（≈1,000 ft²） | **模組化起價 Rs 3.4 lakh（HomeLane 浦那）；典型 Rs 8–15 lakh（≈NT$28–53 萬）；都會全屋中階 Rs 14–25 lakh（≈NT$49–88 萬）** | 2026 | https://www.homelane.com/design-ideas/buying-guides/interior-design-cost-in-pune-for-2bhk-home/ ；https://housiey.com/blogs/?p=8016 ；https://constructionestimatorindia.com/?p=17098 | 中 |
| 每案均價 3BHK（≈1,500 ft²） | **模組化起價 Rs 4.5 lakh；都會全屋中階 Rs 21–37 lakh（≈NT$74–130 萬）；四大都會高端至 Rs 35 lakh+** | 2026 | 同上；https://www.skfcontractor.in/3bhk-interior-design-costs-2025 | 中 |
| 設計費 | **典型 Rs 100–250/ft²（≈NT$1,250–3,130/坪）；全區間 Rs 50–500/ft²；或工程款 5–15%**；「25%」標單一來源 | 2025–26 | https://aecord.com/tools/architect-fee-calculator ；https://interioratoz.com/interior-designer-fees-in-india/ | 中 |
| 商辦裝修單位成本 | **C&W 2026：INR 5,847–6,567/ft²（USD 65–73/ft²；≈NT$7.3–8.2 萬/坪），協作式混合辦公規格；JLL：孟買高於全國均值 7%、班加羅爾低 5%**；註明 C&W 中規格另有 USD 449/m²（≈42/ft²）之低值 | 2026／2025 | https://www.cushmanwakefield.com/en/india/insights/office-fit-out-cost-guide ；https://www.dtnext.in/lifestyle/technology/indias-tech-hubs-offer-5-10-pc-lower-office-fit-out-costs-in-asia-pacific-834649 | 中（未獨立核對 C&W 原頁） |
| 住宅銷售 2025 | **Anarock 7 城 395,625 戶（−14%）；Knight Frank 8 城 348,207 戶；PropEquity 9 城 Q1–Q3 ≈301,000 戶（−23%／−19%／−4%）**；成交金額 +6% | 2025 | https://www.storyboard18.com/amp/how-it-works/top-7-cities-see-14-drop-in-housing-sales-in-2025-but-deal-value-rises-6-to-%e2%82%b96-lakh-crore-88119.htm ；https://realtynmore.com/premium-housing-captures-50-of-indias-348207-residential-sales-in-2025-knight-frank-india/ | 中高 |
| 中古交易占比 | **二手占登記住宅交易 43%（FY2025；FY2019 38%）；孟買約 49%；諾伊達 40%** | FY2025 | https://www.squareyards.com/research-reports/fy2025-residential-registrations-rise ；https://www.outlookmoney.com/real-estate/residential-registrations-skyrocket-since-fy2019-primary-sales-lead-but-secondary-gains-ground | 中 |
| 住宅存量屋齡、翻修週期、工期、完工戶數 | **仍無資料**（維持缺口） | — | — | — |
| 組織化玩家 | Livspace FY25 Rs 1,460 crore（+23%）、淨損 Rs 242 crore；HomeLane Rs 747.8 crore（+22%）、淨損 Rs 111.4 crore（本輪未重查，多源一致）；**IKEA India FY25 營收 Rs 1,749.5 crore（−3.3%）、虧損 Rs 1,325.2 crore（採 ROC 申報值，棄 1,860 crore）** | FY25 | https://ianslive.in/ikea-indias-loss-widens-to-rs-1325-crore-in-fy25-revenue-dips--20260204142638 ；https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863 | 高／中高 |
| Employment Visa 門檻 | **年薪 >USD 25,000 或 Rs 16.25 lakh（MHA／BOI 兩種官方表述）** | 現行 | https://www.mha.gov.in/sites/default/files/2022-08/work_visa_faq[1].pdf ；https://boi.gov.in/boi/contents/travelling-to-india/foreigners/work-in-india | 高 |
| 名目人均 GDP | USD 2,675（2025，IMF 轉載；未重查） | 2025 | https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal | 中 |

---

## (e) 法規要點確認

| 要點 | 確認內容 | 法源／主管機關 URL | 狀態 |
|---|---|---|---|
| 室內設計師執業 | 無執照、無主管委員會。《Architects Act 1972》§37 僅禁止未註冊者使用「architect」名稱；最高法院 2020-03-17 *Council of Architecture v. Mukesh Goyal* 確認不禁止未註冊者從事建築業務。「Interior Designer／Decorator」可自由使用；「Interior Architect」有風險。德里高院 *Ranade* 案曾作區分 | https://api.sci.gov.in/supremecourt/2014/21001/21001_2014_3_1501_21539_Judgement_17-Mar-2020.pdf ；https://www.indiacode.nic.in/bitstream/123456789/1690/1/A1972-20.pdf | 確認 |
| 裝修承包商執照 | 無全國制度（B 引 studiomatrx／CalcGuru；本輪未另查，與最高法院判決邏輯一致） | https://www.studiomatrx.org/guides/scope-boundaries-architect-designer-contractor-india | 維持（未重查） |
| 孟買住宅裝修許可 | 《Mumbai Municipal Corporation Act 1888》§342：可耐住修繕（抹灰、油漆、換地磚、廁浴修繕、排水管、同材質屋面、防水）免市政許可但需社區 NOC；其餘拆除／變更／重建須依 §342／§344 向市政專員送交通知（表格載位置、範圍、監工人）；禁止降低基座／基礎／樓板；砌磚牆需許可、輕隔間不需；社區規約可另設事前書面同意要求 | https://housing.com/news/beware-of-illegal-renovations-bmc-guidelines-for-house-repairs ；https://mhada.gov.in/sites/default/files/BPC_Mumbai-1_dtd-09-07-2026.pdf | 確認（機制修正） |
| 外資持股 | 設計服務／未列明行業 100% 自動路徑；建設發展 100% 自動、3 年鎖定（DPIIT，B 引；本輪未重查） | https://www.dpiit.gov.in/static/uploads/2025/07/1b12c69de7c2e698a7b68f7b8fcf4fe3.pdf | 維持（未重查） |
| Press Note 3 (2020) 對台灣 | **未獲官方澄清**；政府 2020 年曾研議台資是否審查，香港被明確視為自動路徑；律師意見分歧；實務多以自動路徑設 100% 子公司。若有中國大陸受益所有人則須政府核准 | https://law.asia/press-note-3-restriction-investment/ ；https://www.tribuneindia.com/news/business/taiwan-may-be-treated-as-separate-entity-for-fdi-94367 | 修正（信心降為中／低） |
| 外派人員 Employment Visa | 年薪 >USD 25,000（或 Rs 16.25 lakh）；由印度登記實體聘用；豁免：民族廚師、非英語語言教師／翻譯、使領館人員；教職 Rs 9.10 lakh；BPO／ITES 不得豁免；<1 年按比例 | https://www.mha.gov.in/sites/default/files/2022-08/work_visa_faq[1].pdf ；https://boi.gov.in/boi/contents/travelling-to-india/foreigners/work-in-india | 確認 |
| 消費者保護 | 《Consumer Protection Act 2019》：§2(11) 服務瑕疵、§2(47) 不公平交易；**§34(2)(d)** 可於申訴人居住或工作地之地區委員會提告（報價單專屬管轄條款不能排除）；**§35** 提告主體與電子提告；**§69** 時效 2 年（得以正當理由寬限）；§34(1) 地區委員會金額管轄 ≤Rs 1 crore（2021 年規則已改 ≤Rs 50 lakh，未查）。**無裝修專屬標準契約、訂金上限、法定保固**（B 引 studiomatrx；本輪未見反證） | https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/34.php ；https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/35.php ；https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/69.php | 確認（條號修正） |
| 裝修材料管制 | BIS《Plywood and Wooden Flush Door Shutters (QC) Order 2024》S.O. 1377(E)（2024-03-15）：2025-02-28 生效（小型 05-28、微型 08-28）；適用製造商、進口商、銷售者；出口用除外；IS 303:1989 等標準；違者依 BIS Act 2016 處罰 | https://alephindia.in/pdf/bis-qco-for-polywood-and-wooden-flush-door-shutters.pdf | 確認 |
| 稅務 | 子公司有效 25.17%／分公司 36.40–38.22%；GST 設計服務與工程承攬 18%（B 引；本輪未重查，算術與 Finance Act 2024 結構一致） | https://www.indiaconnected.co.uk/blog-articles/indian-tax-policy-2025-gst-cit-changes-foreign-companies/ | 維持（需稅務專業確認） |

---

## 附：本輪搜尋紀錄（14 次執行、1 次因共享額度耗盡未執行）

1. India interior design market size 2025 billion commercial segment share residential CAGR（allowed_domains：mordorintelligence／grandviewresearch／imarcgroup／techsciresearch）
2. India home renovation remodeling market size 2025 2034 USD billion CAGR report
3. Livspace HomeLane full home interiors 2BHK 3BHK package price per sq ft 2026 starting price
4. Council of Architecture conditions of engagement scale of charges interior architecture fee percentage of project cost
5. JLL fit-out cost guide 2025 India Mumbai Bengaluru average office fit-out cost per sq ft USD
6. PropEquity Knight Frank 2025 annual housing sales top cities units decline percent new launches
7. India resale homes share of total housing transactions secondary market registrations percent 2025 Mumbai Delhi
8. Architects Act 1972 section 37 Supreme Court 2020 unregistered persons can practise architecture only title protected Mukesh Goyal
9. Mumbai Municipal Corporation Act section 342 internal alterations flat permission structural changes notice BMC
10. Press Note 3 2020 Taiwan investors India government approval beneficial ownership Taiwanese companies treated land border
11. employment visa India minimum salary US$ 25,000 per annum guidelines exemptions（allowed_domains：mha.gov.in／boi.gov.in／indianvisaonline.gov.in／mea.gov.in）
12. Consumer Protection Act 2019 section 34 territorial jurisdiction where complainant resides section 69 limitation two years section 35 e-filing
13. IKEA India FY25 revenue net loss crore financial year 2024-25 Ingka Tofler
14. Plywood and Wooden Flush Door Shutters Quality Control Order 2024 effective date 28 February 2025 BIS gazette imports
15. （未執行）Cushman Wakefield India office fit-out cost guide 2026 Mumbai INR 6,567 per sq ft — 共享搜尋額度耗盡

印地語搜尋：未執行（兩位分析師之 8 次印地語查詢多回傳英文頁，本輪將額度集中於法規與定義查核）。
