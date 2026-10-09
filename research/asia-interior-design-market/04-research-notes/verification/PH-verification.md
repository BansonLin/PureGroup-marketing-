# 菲律賓（Philippines）— 對抗式查核報告（WP6）

| 項目 | 內容 |
|---|---|
| 查核日期 | 2026-10-09 |
| 查核者 | Claude 子代理（PH-verification，懷疑立場） |
| 查核對象 | `countries/PH-A-market.md`（LENS A：市場）、`countries/PH-B-rules.md`（LENS B：法規） |
| 方法 | 15 次獨立 WebSearch（英文為主；菲律賓商業、統計與法規資訊幾乎全以英文發布，分析師自承菲律賓語搜尋無效）；查詢措辭刻意避開分析師原查詢（改用判例字號、命令編號、報告正式名稱等）。WebFetch／curl 被封鎖，證據為搜尋引擎回傳之頁面摘要與引文，未能開啟原文。預設立場：主張在證據支持前視為錯誤 |
| 結果 | 查核 20 項：**確認 10、修正 4、駁斥 1、無法查證 5**；另列 6 項未分配配額之關鍵數字、14 項內部矛盾／定義問題 |

---

## (a) 逐項查核表

| # | 項目 | 原報告值 | 查核結果 | 修正值 | 證據 URL | 說明 |
|---|---|---|---|---|---|---|
| 1 | Ken Research 家居改善零售市場（A §2(b)、§8） | USD 31.27 億（2025）、CAGR 7.5%、2032 年 USD 51.87 億 | **確認（廠商估值）** | USD 3,127M（2025）→ 5,187M（2032），CAGR 7.50%；2020–25 歷史 CAGR 5.8%；交易筆數 2.084 億→2.936 億 | https://www.kenresearch.com/industry-reports/philippines-home-improvement-market.md | 獨立搜尋回傳相同數字。但同主題他家口徑差異極大：Statista「DIY & Hardware Store」2024 年 USD 213.3 億（https://statista.com/outlook/cmo/diy-hardware-store/philippines ，模型估計）、Nexdigm 五金零售 CAGR 8.2%（2025–31）。Ken 的 31 億只能作「量級」參考，不可作為產業總量 |
| 2 | Ken Research 另一版本（A §2(b)、§8） | USD 9 億（2025–2030 版） | **無法查證** | — | （本輪搜尋僅回傳 31.27 億版本） | 獨立搜尋未見 9 億版本的任何露出；可能為舊基期（2019–24）或不同細分口徑。建議最終報告**不要並列兩值**，只註明「同機構曾有較低估值，口徑不明」 |
| 3 | PSA ASPBI 建築業總營收（A §2(e)、§8） | ₱7,131.9 億，標為「2024 年最終結果」 | **無法查證（年份標示存疑）** | — | https://psa.gov.ph/statistics/construction/aspbi ；https://psa.gov.ph/statistics/construction/aspbi/node/1684060220 | PSA 網站獨立搜尋僅見 **2021 年** ASPBI 建築業最終結果（正式部門 2,293 家事業體、就業 270,311 人）與 2022 年初步結果；未見任何標示 2024 參考年的版本（ASPBI 通常落後約 2 年發布）。₱7,131.9 億很可能是 2022 或 2023 參考年，A 的「2024 年」疑為**發布年**。另 ASPBI 僅涵蓋正式部門事業體，₱7,132 億僅約建築業 GVA 的三分之一（A 自引季 GVA ₱3,835–5,036 億），A 稱其「可當上限／錨點」方向相反——它是下限 |
| 4 | PSA 2025 年 10 月住宅平均造價（A §3、§8） | ₱12,078.24/m² | **無法查證（量級合理）** | — | https://rssonir.psa.gov.ph/sites/default/files/attachment-dir/2025-SR61-021.pdf ；https://rsso08.psa.gov.ph/system/files/attachment-dir/SR%20-Construction%20Statistics%20Eastern%20Samar-%201st%20quarter%202025.pdf ；https://rsso02.psa.gov.ph/content/march-2025-construction-statistics-approved-building-permits-nueva-vizcaya | 全國 2025-10 釋出頁未在搜尋露出。PSA 區域辦公室同期數字：Siquijor Q1 2025 ₱10,112/m²、Eastern Samar Q1 2025 ₱14,510/m²、Nueva Vizcaya 2025-03 ₱14,565/m²，支持 ₱10,000–15,000/m² 量級。另查得 **2025 年 10 月全國核准建照件數年減 22.6%（12,705 件 vs 16,405 件）**（轉載來源 https://www.mexc.com/news/318891 ，需核 PSA 原文），A 未提及此大幅下滑，與 GDP Q4 +3.0% 的營建疲弱一致 |
| 5 | C&W 2026 馬尼拉辦公室裝修單價（A §2(c)、§7、§8） | USD 105/ft²（≈ USD 1,130/m²），標「高信心」 | **無法查證** | — | https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office/2-3/ ；https://www.cushmanwakefield.com/en/singapore/insights/apac-office-fit-out-cost-guide | 2026 年指南確實存在（33 個亞太城市、以 2025 年 12 月為價格基準、以 **USD/m²** 列示而非 ft²），但搜尋摘要未露出馬尼拉數值；A 亦自承「馬尼拉頁面數值未親自核對」。「高信心」標示過高，建議降為中信心，並與 JLL 2023/24 USD 1,006/m² 並列為區間 |
| 6 | Colliers Q4 2025 馬尼拉公寓庫存（A §3、§8） | 未售 79,200 戶；去化 7.9 年（Q2 峰值 13.4 年）；2025 年售 10,100 戶（+8%）；近 30,000 戶未售 RFO | **確認（二手）** | 同左（Gulf News 引 Colliers：去化「約 8 年」）；補充：Colliers 預期 2026 年交屋 13,000 戶（+74%）；獨立追蹤者 2026-08 另稱 82,900 戶 | https://gulfnews.com/business/property/beyond-supply-glut-manila-condo-market-faces-repricing-what-it-means-1.500630690 ；https://malaya.com.ph/weekly-features/property/over-75k-units-unsold-hefty-discounts-to-capture-condo-demand | 各數字與 A 一致，但全為媒體轉述，Colliers 原報告未能開啟。82,900 戶為非 Colliers 口徑，與 LPC 80,300／82,900 戶相近，A 已區分口徑 |
| 7 | DHSUD 住房積壓／需求（A 摘要 7、§3、§6、§8） | 積壓 220 萬戶（2022-12）；「**2028 年前需求 370 萬戶**」；650 萬為 2016–22 需求 | **修正（370 萬定義錯置）** | 220 萬戶積壓確認；**370 萬為「非正規住戶家庭（informal settler families）」數**，非需求量——Ejercito 參議員引 RA 11201 框架：2040 年前需 2,200 萬戶、現有積壓 220 萬、ISF 370 萬；另一官方口徑（Acuzar，2022）：650 萬需求若不作為將於 2028 年增至 1,090 萬 | https://www.abs-cbn.com/news/2024/9/17/solon-calls-dhsud-s-flagship-housing-program-a-failure-2311 ；https://newsinfo.inquirer.net/1683502/housing-backlog-to-hit11m-units-sans-funding ；https://verafiles.org/articles/fact-check-dhsud-officials-flip-flop-on-housing-targets | DHSUD 口徑多次變動（VERA Files 事實查核：興建目標 600 萬→550 萬→300 萬→320 萬→120 萬）。最終報告應寫「積壓 220 萬戶（DHSUD，2022 年底）；另有 370 萬非正規住戶；650 萬／1,090 萬為較舊的需求推估」，**不可寫「2028 年前需求 370 萬」**。A 摘要、§3、§6、§8 多處使用此句，須一併改 |
| 8 | RA 10350 罰則（B 摘要 1、§2.1、§9） | ₱300,000–1,000,000 及／或 6 個月–3 年徒刑 | **確認（二手摘要＋參院新聞稿）** | 同左 | https://www.digest.ph/laws/philippine-interior-design-act-of-2012 ；https://legacy.senate.gov.ph/press_release/2012/0910_prib1.asp | 兩個獨立來源一致（參院 2012 年法案新聞稿即載此金額）。條號未能確認（digest 將罰則歸於 §34–42「最終條款」）；B 原文未標條號，無矛盾。原文請以 LawPhil／Official Gazette 核對 |
| 9 | PRC 室內設計師證照考試結果（B 摘要 2、§2.1、§6.1、§9） | 2025-07：414 考／226 及格（54.59%）；2024-07：400／119（29.75%） | **確認（PRC 官方）** | 同左；**新增 2026-07：432 考／381 及格（88.2%）**，2026-07 已放榜（13 個工作日） | https://prc.gov.ph/node/8125 ；https://davao.prc.gov.ph/node/6770 ；https://www.prc.gov.ph/article/july-2026-licensure-examination-interior-designers-results-released-thirteen-13-working | PRC 原始公告確認 2025 與 2024 數字。2026 年 7 月結果在 B 研究日之前已公布，B 未納入（時效問題） |
| 10 | 「每年新增持照設計師僅約 100–250 人」（B 摘要 2、§10.3） | 100–250 人／年 | **修正** | **119–381 人／年**（2024：119；2025：226；2026：381；三年平均約 242） | https://www.prc.gov.ph/article/july-2026-licensure-examination-interior-designers-results-released-thirteen-13-working | 2026 年及格人數躍升至 381（及格率 88%），B 的供給上限須上修；「供給極為有限」的結論仍成立，但措辭應改為「每年新增 120–380 人」 |
| 11 | PCAB 外資規則（A §4、§8；B 摘要 3、§2.2、§4.2、§10.2） | A：Regular ≥60% 菲資；AAAA 淨值 ≥₱10 億可核外資 Regular。B：2020 年最高法院廢除外資 40% 上限，PCAB 迄今未發布細則 | **確認（措辭須合併修正）** | 最高法院 **G.R. No. 217590（PCAB v. Manila Water，2020-03-10）** 宣告 RA 4566 IRR Rule 3 §3.1 及 Rule 12 之「Regular 執照限 ≥60% 菲資」條款無效；PCAB 聲請再議遭駁回，但因介入人另提再議，**PCAB 公開表示「維持現狀（status quo）」**；PCAB 於訴訟中主張 2015 年 CIAP 決議已允許**實收資本（paid-up capital）≥₱10 億**之外資企業取得 Regular 執照（即 AAAA 類） | https://lawphil.net/judjuris/juri2020/mar2020/gr_217590_leonen.html ；https://insightplus.bakermckenzie.com/bm/dispute-resolution/philippines-supreme-court-affirms-ruling-that-allows-foreign-construction-firms-to-obtain-regular-licenses-to-engage-in-construction-in-the-philippines ；https://batas.org/?p=69347 | 兩筆記各對一半：法律上 60/40 限制已被判無效（B 對），實務上 PCAB 仍以舊規運作（A 的「≥60%」是實務現狀）。外資主要路徑仍是 Special License（逐案）或 AAAA。A 寫 AAAA 門檻為「淨值」、Baker McKenzie 寫「實收資本」，須向 PCAB 確認。另一來源（ndvlaw）將判決日期誤記為 2020-02-05，應以 2020-03-10 為準 |
| 12 | 外資負面清單現行版本（B §2.4、§4.1、§9 vs A §4） | B：現行為第 12 版 EO 175（2022），「本次搜尋未見第 13 版發布」；A：第 13 版 EO 113 於 2026-05-02 生效 | **駁斥（B）／確認（A）** | **第 13 版 RFINL 已由 EO 113 於 2026-04-13 簽署、2026-04-17 公告，2026-05-02 生效**（另有法律事務所稱 05-01）；「專業執業」仍保留菲籍（互惠例外）、建築等專業之法人執業仍列保留；國防相關工程承攬外資上限 25%；電信可 100% 外資（互惠） | https://lawphil.net/executive/execord/eo2026/eo_113_2026.html ；https://tribune.net.ph/2026/04/16/pbbm-updates-foreign-investment-ownership ；https://governance.depdev.gov.ph/marcos-unveils-new-foreign-investment-limits-under-eo-113/ ；https://ndvlaw.com/how-to-navigate-the-2026-foreign-investment-negative-list-why-structuring-your-philippine-subsidiary-correctly-is-crucial/ | B 研究日為 2026-10-09 卻稱第 13 版未發布，屬事實錯誤。最終報告所有 FINL 引用應改為 **EO 113（第 13 版，2026）**，並以 EO 113 附件重新核對室內設計（RA 10350 §15、§29）條目（本輪搜尋摘要未露出附件逐項，但「專業執業保留菲籍」之總則未變） |
| 13 | NCR 最低日薪 Wage Order NCR-26（A §6、§8；B §6.3、§9） | ₱695，2025-07-18 起（+₱50） | **確認（間接）** | 同左（NCR-27 新聞稿載明「自 ₱695 調升至 ₱755」） | https://www.dzrh.com.ph/post/peso60-ncr-minimum-wage-increase-takes-effect-daily-pay-now-at-peso755 ；https://www.sunstar.com.ph/manila/dole-reminds-ncr-firms-to-implement-new-wage-hike | 以新命令之基期間接確認 ₱695；但 ₱695 **已非現行值**（見 #14） |
| 14 | Wage Order NCR-27（B §6.3、§11.13，B 標「未經官方核實」） | ₱755（2026-07-19）、₱780（2027-01-20） | **修正（生效日）** | **₱755 自 2026-07-25 生效**（DOLE／NWPC；Context.ph 稱 07-19 為少數說法）；第二階段 +₱25 → **₱780 於 2027-01-20**；合計 +₱85 為 NCR 史上最大調幅；農業／小型零售製造 ₱658→₱718→₱743；命令 2026-06-23 核定、07-09 公告；全為基本工資、無 COLA；影響約 110 萬人 | https://www.dzrh.com.ph/post/peso60-ncr-minimum-wage-increase-takes-effect-daily-pay-now-at-peso755 ；https://sweldoph.com/guides/minimum-wage-ncr ；https://context.ph/2026/06/30/metro-manila-minimum-wage-jumps-by-record-p85/ | A 筆記（研究日 2026-10-09）全文仍以 ₱695 為現行值，已過時。最終報告應以 **₱755（≈ USD 13.0 ≈ NT$403／日）** 為 2026 年現行 NCR 最低日薪，並註明 2027-01-20 起 ₱780 |
| 15 | BSP 政策利率 2026 年時間軸（A §6、§8、§10.12，A 標低信心） | 2026-02 降至 4.25% → 2026-08-27 升至 5.00%（另說 7 月 4.75%、8 月 1 日維持不變） | **確認（矛盾已解）** | **2026-02 降息至 4.25%；04 升至 4.50%；06-18 升至 4.75%；08-27 升至 5.00%**（年內第三次升息；ODF 4.50%、OLF 5.50%）；7 月通膨 6.2%（6 月 6.4%）、核心 4.2%；BSP 預期 2026、2027 年均通膨皆突破 4% 上限；下次會議 10-22、12-17 | https://tradingeconomics.com/philippines/interest-rate/news/578549 ；https://interaksyon.philstar.com/sports/2026/08/27/318360/bsp-raises-policy-rate-as-expected/amp/ ；https://www.philstar.com/starweek-magazine/2026/06/18/2536130/bsp-raises-key-interest-rate-25-basis-points-475-june-2026 | A 的「一說」（UPropertyPH）正確；「8 月 1 日維持不變」之說（Ziggurat）錯誤。撰寫時標註「截至 2026-08-27」，10-22 會議後需更新 |
| 16 | Wilcon Depot 2025 年業績（A §4、§8；B 摘要 7、§7.2、§9） | 淨銷售 ₱354.44 億（+3.7%）；淨利 ₱24.46 億（−3.3%）；104 店；同店 −0.3% | **確認** | 同左；補充：毛利 ₱136.8 億（+2.5%）、毛利率 38.6%（2024：39.1%）、EBITDA 率 13.5%、淨利率 6.9%；Depot ₱341.36 億（96.3%）、DIW 約 ₱11.2 億；**專案銷售（project sales）−46.8%**；下半年淨利 +26%、Q4 同店轉正 | https://tribune.net.ph/2026/03/30/wilcon-income-slips-3-despite-higher-sales ；https://plus.inquirer.net/business/wilcon-income-dips-on-cost-pressures/ ；https://quartr.com/events/wilcon-depot-inc-wlcon-q4-2025_FtvIy3IS | 多來源一致。專案銷售（B2B 裝修）2025 年再減 46.8%（2024 年僅 ₱3.47 億 → 約 ₱1.85 億【推算】），強化 A「零售整合裝修尚未成形」的推論。B 的「2026-06-30 增至 109 店」本輪未查 |
| 17 | 2025 年 GDP 成長（A §2(e)、§6、§8） | +4.4%（低於 5.5–6.5% 目標） | **確認** | 2025 全年 **+4.4%**（2024：5.7%）；**Q4 2025 +3.0%**（季增 0.6%）；工業僅 +1.5%、服務 +5.9%、農業 +3.1%；內需 +3.7%；為疫後最低 | https://www.sunstar.com.ph/manila/ph-economy-grows-44-in-2025-misses-government-target ；https://www.dzrh.com.ph/post/philippine-gdp-growth-slows-to-30percent-in-q4-2025-full-year-expansion-at-44percentpsa ；https://context.ph/2026/01/29/philippine-gdp-growth-slows-services-carry-economy/ | PSA 2026-01-29 公布。Balisacan 點名防洪工程貪腐案拖累公共營建與信心——與 #4 的建照件數 −22.6% 互相印證，是建築業需求端的重要背景 |
| 18 | 飯店管線 2026 年報告（A 摘要 7、§6、§8、§9） | 45,884 間客房／213 案／₱3,870 億（較 2024 版 +55%）；2024 版 158 案、40,084 間 | **修正（客房數不一致）** | 213 案、₱3,870 億、期間 2026–2032 確認；客房數 **Context.ph 引 PHOA–LPC 報告為 45,213 間**，Manila Times 為 45,884 間（皆為媒體轉述；後者與報告所稱「客房 +14%」較吻合）；2024 基期 158 案／40,084 間／₱2,500 億確認；2028 年單年開出約 12,000 間；約 70% 位於國際門戶周邊；可支撐 64,000 個飯店直接就業 | https://context.ph/2026/09/16/philippine-hotel-pipeline-hits-p387b-45000-rooms-through-2032/ ；https://context.ph/2026/09/14/philippine-hotel-pipeline-to-exceed-40000-rooms/ ；https://hospitalitynews.ph/dot-phoa-releases-phisap-hoping-to-meet-the-projected-456055-room-keys-by-2028/ | 建議寫「約 4.5 萬間（45,213–45,884）、213 案、₱3,870 億」。報告為 PHOA（飯店業主協會）與 Leechiu（LPC）聯合發布，**非 DOT 官方統計**。另 PHOA 稱兩年來飯店營建成本上漲約 30%，與 CMWPI（2025 年 +0.1%、2026-07 +3.5%）落差極大，口徑不同（總造價含人工、機電、傢俱 vs 躉售材料指數），最終報告不可混用 |
| 19 | 建築業占 GDP（A §2(e)、§7、§8） | ≈5% | **無法查證（與筆記自身數據矛盾）** | 建議改為「約 7–8%（PSA 國民所得帳，待核）」或刪除 | https://tradingeconomics.com/philippines/gdp-from-construction | A 自引建築業 GVA（2018 年固定價格）季值 ₱3,835–5,036 億，年化約 ₱1.7–1.8 兆；對比 2025 年實質 GDP 約 ₱23 兆，占比應為 **7–8%**【推算】，非 5%。本輪未分配配額核對 PSA 原表，但 5% 幾可確定偏低，不建議引用 |
| 20 | 民法第 1723 條責任期（B 摘要 5、§3.1、§9、§10.5） | 15 年（另有來源稱 10 年，以 15 年為準） | **確認（法條）** | 建物完工後 **15 年內**倒塌：建築師／工程師（圖說、地基缺陷）與承包商（施工、劣質材料、違約）負責；監造者與承包商**連帶**；驗收不視為放棄；**訴訟須於倒塌後 10 年內提起**（此即「10 年」之由來） | https://lawphil.net/statutes/repacts/ra1949/ra_386_1949.html | 以 RA 386（Civil Code）條文確認；B 所稱「另有來源稱 10 年」是**訴訟時效**，非責任期，兩者並存不矛盾。注意第 1723 條僅適用「倒塌（collapse）」之重大結構事故；一般裝修瑕疵適用第 1713–1715 條與契約約定（B 已正確區分） |

### (a2) 未分配配額、未獨立查核之關鍵數字（請最終報告標示「未獨立查核」）

| 項目 | 原報告值 | 查核者判斷 |
|---|---|---|
| 公寓翻修單價分級與設計費慣例（A §3、§8；B §5、§9） | A：基本 ₱6,000–15,000／中 15,000–25,000／高 25,000–60,000+/m²；設計費工程款 10–20%。B：整體 ₱20,000–60,000/m²；設計費 10–45% | 全部來自承包商／設計平台行銷頁面（DMCI、Mainline Power、Qaltik、Coohom、Homestyler、JMG Build），**無任何官方或協會統計**；兩筆記區間互異（見 (b) 4–6）。只能以「市場行情（非統計）」標示並呈現區間 |
| OFW 現金匯款 2025 年 USD 356.34 億（A §5、§8） | BSP 初值 | 未搜；與 BSP 公布的 2023（334.9 億）、2024（344.9 億）序列一致（年增 3.3%），可視為高信心 |
| Pag-IBIG 房貸利率 5.75%（1 年）／6.25%（3 年）（B §5.3、§9） | Inquirer／PhilStar 2025 | 未搜；與 Pag-IBIG 2024–2025 公告費率表一致，中高信心；但非裝修貸款利率，B 已註明 |
| 台灣是否為 RA 10350 §29 互惠國（B §4.1、§11.2） | 未找到 | 本質上無法以搜尋驗證，須向 PRC Board of Interior Design 正式函詢。補充觀點：台灣無國家級「室內設計師」證照（僅《建築物室內裝修管理辦法》之專業技術人員登記），「互惠」判定本身存在法律空白，宜以「菲籍持照設計師簽證＋台方合作」為基本假設 |
| 6Wresearch 室內設計市場 CAGR 6.4%（A §2(a)、§8） | 付費牆 | 未搜；無基準金額，僅可引用為「成長率級別」，低信心 |
| 持照室內設計師「約 2,000 人（2013）、執業約 200 人」（A §4、§7、§8） | Inquirer ≈2013 | 未搜；13 年前資料。僅 2024–2026 三年即新增 726 人（#9、#10），現行 PRC 登記人數應明顯高於 2,000；建議改寫為「2013 年逾 2,000 人；2024–26 年新增 726 人；現行總數待向 PRC 查詢」 |

---

## (b) 內部矛盾與定義問題

1. **外資負面清單版本（A vs B）**：A 引第 13 版 EO 113（2026），B 稱現行為第 12 版 EO 175（2022）且「未見第 13 版」。**已解決：第 13 版 EO 113 為現行**（#12）。B §2.4、§4.1、§9、§10.1 所有「EO 175／第 12 版」引用須改。
2. **PCAB 外資規則表述**：A「Regular ≥60% 菲資」描述的是 PCAB 實務現狀；B「2020 年最高法院已廢除」描述的是法律狀態。兩者都對，但各自單獨陳述會誤導；最終報告須合併為「法律上已無效、PCAB 維持現狀、外資實務走 Special License 或 AAAA（₱10 億）」（#11）。
3. **NCR 最低工資**：A 全文以 ₱695 為現行，B 已列 NCR-27 但生效日錯（07-19）。以 **₱755（2026-07-25 起）** 為準（#13、#14）；A §6、§7、§8 所有 ₱695 之 USD／NT$ 換算（USD 12.0／NT$371）須改為 USD 13.0／NT$403。
4. **公寓翻修單價區間不一致**：A 基本級 ₱6,000–15,000/m²（油漆、燈具、小修）vs B 整體 ₱20,000–60,000/m²、分級 ₱15–20K／25–40K／50K+。差異來自**工程範圍定義**（美容性小修 vs 全室翻修）與來源（DMCI vs Mainline Power／RenovationCalcPH），非數據矛盾；最終報告必須以「工程範圍」定義分級，不可取兩筆記平均。
5. **設計費百分比**：A「10–20% 為最多來源一致」vs B「10–45%，平均 15–30%」（單一來源 Qaltik）。建議採 10–20% 為主流、高端至 30%，並註明 PIID Doc 5 正式費率表未取得（Scribd 版本真偽未核）。
6. **每 m² 設計費**：A ₱1,500–5,000；B ₱600–2,500／₱5,000–10,000／USD 15–50（≈ ₱870–2,900）。範圍橫跨 16 倍，顯示此計費方式在菲律賓並非主流且各家定義不同，不可引用單一值。
7. **研究機構口徑不可比（A §2 對照表）**：Ken 家居改善零售 USD 31 億 vs Ken 另版 USD 9 億 vs Statista DIY/hardware USD 213 億（2024）；IMARC 傢俱 USD 43 億 vs Ken 傢俱＋生活室內 USD 25 億 vs Statista 傢俱零售 USD 7.86 億。各家定義（零售 vs 製造含出口、是否含電商、是否含建材）皆未公開；A 已標低信心，**但 A §7 以 Ken 31 億計算「占 GDP 0.64%、人均 USD 27」並與台灣 RR 口徑（0.69–1.89%）並列比較，屬跨口徑比較**，應刪除或加強警語。
8. **辦公室裝修跨機構比較（A §7）**：馬尼拉 USD 1,130/m²（C&W 2026，未核）vs 台北 USD 1,593/m²（Knight Frank 2026）。不同研究機構、內含項目不同（C&W 指南是否含傢俱、AV、專業費用未核），不可並列為同口徑；C&W 指南本身含台北值，應以同一機構比較。
9. **ASPBI 定位錯誤**：A 稱 ASPBI ₱7,132 億「可當上限／錨點」，但 ASPBI 僅正式部門事業體，數值約為建築業 GVA 的 1/3，實為**下限**；且年份標示疑誤（#3）。
10. **建築業占 GDP 5% vs 自引 GVA 數據**：A §2(e) 的 5% 與同段引用的季 GVA（₱3,835–5,036 億）推算之 7–8% 矛盾（#19）。
11. **飯店客房數**：45,884（Manila Times）vs 45,213（Context.ph 引 PHOA–LPC），同一報告兩個媒體數字（#18）。
12. **住房需求「370 萬戶」定義錯置**：A 摘要 7、§3、§6「驅動」、§8 皆寫「2028 年前需求 370 萬戶」，實為非正規住戶數（#7）；須全文統一改寫。
13. **匯率換算抽查**：抽查 12 組（₱10,000/m²→NT$17,670/坪；₱12,078/m²→NT$21,340/坪；USD 105/ft²→USD 1,130/m²→₱65,540→NT$115,800/坪；Ken USD 31.27 億→₱1,814 億→NT$969 億；Wilcon ₱354.4 億→USD 6.11 億→NT$189 億；OFW USD 356.3 億→₱2.07 兆→NT$1.10 兆；飯店 ₱3,870 億→USD 66.7 億→NT$2,070 億；罰金 ₱30–100 萬→USD 5,172–17,241／NT$16–53.4 萬；40 ㎡翻修 ₱80–180 萬→USD 13,800–31,000／NT$42.7–96.2 萬；₱695→USD 12.0／NT$371；Ken 占 GDP 0.64%；人均 USD 27）**全部正確**（誤差 <0.5%），兩筆記匯率假設一致（1 USD = ₱58 = NT$31；1 PHP = NT$0.534）。惟 B 自述 2026 年披索貶值推升進口成本，實際匯率可能已偏離 58；最終報告應統一標註「以 1 USD = ₱58 換算（2025–26 概略）」。
14. **時效問題（兩筆記共同）**：研究日皆為 2026-10-09，但 A 仍用 ₱695 工資、BSP 利率存疑；B 仍用第 12 版 FINL、未納入 2026 年 7 月考試結果（381 人）。2026 年 4–8 月的四項重大更新（EO 113、NCR-27、BSP 三次升息、IDLE 2026）均須補入。

---

## (c) 整體評估

- **整體品質：中。** 硬數據（Wilcon 財報、2025 GDP、BSP 利率路徑、PRC 考試人數、Colliers 庫存、飯店投資額與案數、Ken 數字本身、RA 10350 罰則、Civil Code 1723）多數經獨立查核成立；錯誤集中在**法規版本過時（FINL 第 12→13 版）**、**工資命令生效日**、**住房需求定義錯置（370 萬）**、**飯店客房數**與**建築業占 GDP 比例**。
- **市場規模是最弱環節。** 菲律賓沒有任何官方的室內設計或翻修市場統計，兩筆記皆誠實標註；但 A §7 把低信心的 Ken 零售數字拿去算 GDP 占比並做跨國比較，是最大的方法風險。建議最終報告以「無官方口徑」為前提，只給量級與成長率，並以官方建照產值（月 ₱180–200 億住宅）作為新建端錨點。
- **單價與設計費 100% 來自行銷頁面**，本輪未分配配額驗證（也無法驗證——不存在官方價目）；應以「市場行情（非統計）」標示、以區間呈現、按工程範圍分級。
- **法規部分核心架構正確**（RA 10350 執照制＋互惠條款、PCAB 執照制、PD 1096／RA 9514 許可流程、Civil Code 責任），但 B 對 FINL 的結論錯誤、對 PCAB 應補「維持現狀」之官方立場；A 對 PCAB 的「≥60%」應註明為實務而非法律。
- **A 的信心標示偏高**：C&W USD 105/ft²（未核卻標高信心）、建築業占 GDP 5%（標中信心）應下調。B 的信心標示整體較保守、較可靠。
- **須以 2026-10 時點更新**：EO 113（FINL 第 13 版）、NCR-27 ₱755、BSP 5.00%（08-27）、IDLE 2026 年 381 人、Wilcon 專案銷售 −46.8%、2025-10 建照件數 −22.6%。

---

## (d) 建議採用值

| 指標 | 建議值 | 年份 | 證據 URL | 信心 |
|---|---|---|---|---|
| 室內設計／住宅翻修市場規模 | **無官方口徑；不給點值。** 量級參考：Ken Research 家居改善零售 USD 31.3 億（CAGR 7.5%，2025–32）；須註明 Statista DIY/hardware 口徑達 USD 213 億（2024），口徑差 7 倍 | 2025 | https://www.kenresearch.com/industry-reports/philippines-home-improvement-market.md ；https://statista.com/outlook/cmo/diy-hardware-store/philippines | 低 |
| 室內設計服務市場成長率 | CAGR 6.4%（6Wresearch，無基準金額） | 2025–31 | https://www.6wresearch.com/industry-report/philippines-interior-design-market-outlook | 低（未核） |
| 新建住宅端錨點 | 住宅建照月產值 ₱178.8 億（2025-03）／₱197.7 億（2025-07）；住宅平均造價 ₱12,078/m²（2025-10，待核；區域值 ₱10,100–14,600/m² 支持量級）；**2025-10 全國建照件數 −22.6% YoY**（需核 PSA 原文） | 2025 | https://psa.gov.ph/statistics/construction/pcs/node/1684081355 ；https://rssonir.psa.gov.ph/sites/default/files/attachment-dir/2025-SR61-021.pdf | 中 |
| 公寓翻修單價（馬尼拉，行情） | 基本（油漆、燈具、小修）₱6,000–15,000/m²；中階（地板、櫥櫃、照明）₱15,000–25,000/m²（馬尼拉上緣至 45,000）；高階 ₱25,000–60,000+/m²；省區低 20–40%；**須標「承包商行情，非統計」並按工程範圍分級** | 2025–26 | https://communities.dmcihomes.com/how-much-personalize-condo-unit ；https://www.mainlinepowerph.com/blogs/articles/condo-renovation-budget ；https://www.renovationcalcph.com/ | 低–中（未獨立核） |
| 設計費慣例 | 工程款 **10–20%**（主流；高端至 30%）；小型公寓包案 ₱5–10 萬、較大 ₱10–25 萬；每 m² 計費非主流、區間不可靠；PIID Doc 5 允許按時／每 m²／百分比三制，正式費率表待向 PIID 取得 | 2025 | https://jmgbuild.com/interior-design-rates-in-the-philippines-2025/ ；https://www.scribd.com/presentation/541749828/PIIDDoc5GuidelinesonContracts | 低–中（未獨立核） |
| 辦公室裝修單價（馬尼拉） | **USD 1,000–1,130/m²**（JLL 2023/24 USD 1,006；C&W 2026 USD 1,130 待開原文核對）；本地承包商工程款 ₱15,000–35,000/m²（不含傢俱／IT）；跨國比較須用同一機構指南 | 2024–26 | https://www.cushmanwakefield.com/en/singapore/insights/apac-office-fit-out-cost-guide ；https://alphabuild.ph/office-fit-out-costs-in-manila-what-to-budget-in-2026/ | 中 |
| 馬尼拉公寓未售庫存 | 79,200 戶；去化約 7.9–8 年（Q2 2025 峰值 13.4 年）；2025 年售出 10,100 戶（+8%）；未售 RFO 近 30,000 戶；2026 年預計交屋 13,000 戶 | Q4 2025 | https://gulfnews.com/business/property/beyond-supply-glut-manila-condo-market-faces-repricing-what-it-means-1.500630690 | 中高（二手） |
| 住房積壓／需求 | 積壓 220 萬戶（DHSUD，2022-12）；非正規住戶 370 萬家庭；2040 年前需求 2,200 萬戶（RA 11201 框架）；「650 萬」為舊需求口徑（不作為時 2028 年達 1,090 萬）；**刪除「2028 年前需求 370 萬戶」** | 2022–26 | https://www.abs-cbn.com/news/2024/9/17/solon-calls-dhsud-s-flagship-housing-program-a-failure-2311 ；https://verafiles.org/articles/fact-check-dhsud-officials-flip-flop-on-housing-targets | 中 |
| 飯店管線（商業裝修池） | 213 案、約 4.5 萬間客房（45,213–45,884）、承諾投資 ₱3,870 億（2026–2032；較 2024 版 ₱2,500 億 +55%）；2028 年單年約 12,000 間 | 2026-09 | https://context.ph/2026/09/16/philippine-hotel-pipeline-hits-p387b-45000-rooms-through-2032/ | 中高（PHOA–LPC 報告，媒體轉述） |
| GDP 成長 | 2025 全年 +4.4%（Q4 +3.0%；2024：5.7%） | 2025 | https://www.sunstar.com.ph/manila/ph-economy-grows-44-in-2025-misses-government-target | 高 |
| 建築業占 GDP | **不採用 5%**；改引 PSA 國民所得帳（推算約 7–8%，待核） | 2025 | https://tradingeconomics.com/philippines/gdp-from-construction | 低（推算） |
| BSP 政策利率 | 5.00%（2026-08-27；年內自 4.25% 三度升息）；7 月通膨 6.2% | 2026-08 | https://tradingeconomics.com/philippines/interest-rate/news/578549 | 高（10-22 會議後需更新） |
| NCR 最低日薪 | **₱755（2026-07-25 起，Wage Order NCR-27）≈ USD 13.0 ≈ NT$403**；2027-01-20 起 ₱780；歷史：₱695（2025-07-18）、₱645（2024-07） | 2026 | https://www.dzrh.com.ph/post/peso60-ncr-minimum-wage-increase-takes-effect-daily-pay-now-at-peso755 ；https://sweldoph.com/guides/minimum-wage-ncr | 高 |
| 技工市場日薪（馬尼拉） | 泥作／木工 ₱800–1,200；電工／水電 ₱850–1,200（承包商估計，非統計） | 2026 | https://aedoconstruction.com/blog/construction-labor-rates-philippines-2026/ | 低–中（未獨立核） |
| 建材躉售物價（CMWPI NCR） | 2025 年均 +0.1%；2026-04 +1.9%、05 +2.8%、06 +2.9%、07 +3.5%（初步） | 2025–26 | https://businessmirror.com.ph/2026/07/14/psa-reports-hike-in-price-of-construction-materials/ | 中高（未獨立核；A/B 序列一致） |
| 家居建材零售龍頭 | Wilcon 2025：淨銷售 ₱354.4 億（+3.7%）、淨利 ₱24.5 億（−3.3%）、104 店、同店 −0.3%、專案銷售 −46.8% | 2025 | https://tribune.net.ph/2026/03/30/wilcon-income-slips-3-despite-higher-sales | 高 |
| 持照設計師供給 | 年新增 119（2024）／226（2025）／381（2026）人；三年合計 726；2013 年存量逾 2,000 人（舊）；現行總數待向 PRC 查詢 | 2024–26 | https://prc.gov.ph/node/8125 ；https://www.prc.gov.ph/article/july-2026-licensure-examination-interior-designers-results-released-thirteen-13-working | 高（考試）／低（存量） |
| OFW 現金匯款 | USD 356.3 億（2025 初值；2024：344.9 億） | 2025 | https://www.bsp.gov.ph/statistics/external/ofw2.aspx | 高（未獨立核，序列一致） |
| 匯率 | 1 USD = ₱58 = NT$31；1 PHP = NT$0.534（統一標註） | 2025–26 | — | — |

---

## (e) 法規要點確認

| 要點 | 確認內容 | 法源／監理機關 URL | 查核狀態 |
|---|---|---|---|
| 室內設計執業法 | **RA 10350《Philippine Interior Design Act of 2012》**（2012-12-17 公布，取代 RA 8534）：僅 PRC 室內設計委員會登記之設計師或持臨時／特別許可之外籍設計師可執業；§29 互惠條款；非法執業罰 ₱30–100 萬及／或 6 個月–3 年徒刑；聘用未經許可外籍人士者同責 | https://www.officialgazette.gov.ph/2012/12/17/republic-act-no-10350/ ；https://www.lawphil.net/statutes/repacts/ra2012/ra_10350_2012.html ；罰則：https://www.digest.ph/laws/philippine-interior-design-act-of-2012 ；https://legacy.senate.gov.ph/press_release/2012/0910_prib1.asp | 罰則金額經兩獨立來源確認；條號未確認 |
| 設計師證照考試 | PRC 每年 7 月舉辦（NCR、Cebu、Davao，2026 年增 Rosales）；2024：119/400；2025：226/414；2026：381/432 | https://prc.gov.ph/node/8125 ；https://davao.prc.gov.ph/node/6770 ；https://www.prc.gov.ph/article/july-2026-licensure-examination-interior-designers-results-released-thirteen-13-working | 確認（PRC 官方） |
| 外資進入—專業執業 | **第 13 版外資負面清單（EO 113，2026-04-13 簽署，2026-05-02 生效）**：「專業執業」保留菲籍（互惠例外）；建築等專業之法人執業列保留；室內設計條目（RA 10350 §15、§29）須以 EO 113 附件逐項核對；國防相關工程承攬外資 25%；私人國內營建不在清單上（受 PCAB 執照制而非 FINL 限制） | https://lawphil.net/executive/execord/eo2026/eo_113_2026.html ；https://governance.depdev.gov.ph/marcos-unveils-new-foreign-investment-limits-under-eo-113/ | 確認（B 筆記之第 12 版引用須全部更新） |
| 外資進入—承攬 | **RA 4566（Contractors' License Law）＋ PCAB（CIAP／DTI）**：承攬或投標皆須執照。最高法院 G.R. No. 217590（2020-03-10）宣告 IRR「Regular 執照限 ≥60% 菲資」無效，再議駁回；因介入人再議，**PCAB 維持現狀**。外資實務路徑：Special License（逐案；PCAB Res. 214-1997）或 AAAA 類（實收資本 ≥₱10 億，2015 年 CIAP 決議）；Regular 執照效期 7/1–次年 6/30 | https://lawphil.net/judjuris/juri2020/mar2020/gr_217590_leonen.html ；https://insightplus.bakermckenzie.com/bm/dispute-resolution/philippines-supreme-court-affirms-ruling-that-allows-foreign-construction-firms-to-obtain-regular-licenses-to-engage-in-construction-in-the-philippines ；https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/11/44534 ；https://ciap.dti.gov.ph/ | 判決與現狀經確認；AAAA 門檻「淨值 vs 實收資本」須向 PCAB 確認；效期未獨立核 |
| 建築許可 | **PD 1096《National Building Code》**：變更建物之工程原則須向地方建築官（OBO）申領建照；僅狹義小型工程（更換地板、門窗、非承重隔間）免許可；結構、格局、水電機械消防工程須持照建築師／工程師簽證 | https://lawphil.net/statutes/presdecs/pd1977/pd_1096_1977.html ；https://www.respicio.ph/commentaries/building-permit-requirements-for-interior-renovations-in-the-philippines | 法條架構確認；「免許可工程清單」為律師事務所解釋，未獨立核 |
| 消防許可 | **RA 9514《Revised Fire Code of 2008》**：FSEC 為建照前提、FSIC 於使用前核發；公寓公共區域由管委會負責、單位內由所有權人負責 | https://lawphil.net/statutes/repacts/ra2008/ra_9514_2008.html ；https://vizcodeph.com/code-library/ra-9514-fire-code-of-the-philippines/ | 法條架構確認（本輪未獨立搜尋） |
| 公寓管委會 | 施工保證金 ₱10,000–30,000+、工時與電梯限制、多數大樓禁結構修改——為各大樓內規，無統一法規 | https://www.mainlinepowerph.com/blogs/articles/condo-renovation-cost-in-the-philippines ；https://sbcorp.gov.ph/wp-content/uploads/2023/07/Annex_A_Building_Guidelines.pdf | 行情（未獨立核） |
| 消費者保護—民法 | **Civil Code（RA 386）Art. 1723**：完工後 15 年內倒塌，建築師／工程師與承包商負責、監造連帶、訴訟時效倒塌後 10 年；**Art. 1713–1715**：固定價承攬（含修繕）之完工前風險與依圖施工義務；隱蔽瑕疵「6 個月通知、4 年起訴」之說（B 引 Aedo）**未附法條依據，不建議引用** | https://lawphil.net/statutes/repacts/ra1949/ra_386_1949.html | Art. 1723 確認；其他條文架構確認 |
| 消費者保護—行政 | **RA 7394《Consumer Act》**＋ DTI 調解（退款、更換、修復、減價；和解可依 ADR 規則執行）；PCAB／CIAP 可對持照承包商行政處分；「DTI 調解成功率 60%」僅單一律師事務所說法，**不建議引用**；無官方裝修糾紛統計 | https://lawphil.net/statutes/repacts/ra1992/ra_7394_1992.html ；https://www.respicio.ph/commentaries/how-to-file-a-consumer-fraud-complaint-against-a-construction-contractor-in-the-philippines | 法條架構確認（本輪未獨立搜尋） |
| 契約慣例 | 缺陷責任期 3–12 個月、保留款 5–10%、無強制履約保證或代管制度 | https://www.whitecase.com/insight-our-thinking/managing-construction-risks-asia-pacific-philippines | 市場慣例（未獨立核） |
| 勞動 | Wage Order NCR-27：₱755（2026-07-25）、₱780（2027-01-20）；DOLE／RTWPB-NCR | https://www.dzrh.com.ph/post/peso60-ncr-minimum-wage-increase-takes-effect-daily-pay-now-at-peso755 ；https://www.sunstar.com.ph/manila/dole-reminds-ncr-firms-to-implement-new-wage-hike | 確認 |
| 台菲互惠 | RA 10350 §29 互惠；台灣是否被 PRC 認定為互惠國**無法以搜尋驗證**，須向 PRC Board of Interior Design 函詢；台灣無國家級室內設計師證照，互惠判定存在法律空白 | https://www.lawphil.net/statutes/repacts/ra2012/ra_10350_2012.html | 無法查證 |

---

## 附：本輪搜尋紀錄（15 次）

| # | 查詢（已避開分析師措辭） | 對應項目 | 結果 |
|---|---|---|---|
| 1 | Philippines home improvement retail market size USD billion 2032 forecast hardware tiles sanitaryware | #1、#2 | Ken 31.27 億確認；9 億版未露出；Statista DIY 213 億 |
| 2 | PSA Annual Survey of Philippine Business and Industry construction section total revenue billion pesos establishments final results | #3 | 僅見 2021 年最終結果；營收未露出 |
| 3 | PSA approved building permits October 2025 residential average cost per square meter | #4 | 全國值未露出；區域值 ₱10,112–14,565；10 月件數 −22.6% |
| 4 | Cushman Wakefield 2026 Asia Pacific fit out cost guide Manila US$ per sq ft | #5 | 指南存在，馬尼拉值未露出 |
| 5 | Colliers Metro Manila condominium remaining inventory fourth quarter 2025 years to sell unsold units | #6 | 79,200／13.4→約 8 年／10,100 戶確認 |
| 6 | DHSUD housing need 3.7 million 2028 backlog 2.2 million Senate hearing 6.5 million misconception | #7 | 370 萬＝非正規住戶；220 萬積壓確認 |
| 7 | Republic Act 10350 penal provisions "interior design" fine "not less than" imprisonment Section 32 OR Section 33 | #8 | ₱30–100 萬／6 月–3 年確認 |
| 8 | Licensure Examination for Interior Designers July 2025 results passers "out of" examinees PRC | #9、#10 | 226/414、119/400 確認；新增 2026 年 381/432 |
| 9 | PCAB v. Manila Water Supreme Court G.R. 217590 regular license foreign-owned contractors 60% Filipino IRR void | #11 | 判決確認；PCAB 維持現狀；₱10 億實收資本 |
| 10 | 13th Regular Foreign Investment Negative List executive order 2026 Marcos signed | #12 | EO 113，2026-04-13 簽署、05-02 生效 |
| 11 | Wage Order NCR-27 minimum wage Metro Manila 2026 new daily rate effective | #13、#14 | ₱755 自 2026-07-25；₱780 自 2027-01-20 |
| 12 | Bangko Sentral Monetary Board August 2026 policy rate decision target reverse repurchase rate percent | #15 | 4.25→4.50→4.75→5.00% |
| 13 | Wilcon Depot full year 2025 results net sales billion net income stores end-2025 | #16 | 全部確認；專案銷售 −46.8% |
| 14 | Philippines full-year 2025 GDP growth PSA fourth quarter 2025 percent announced January 2026 | #17 | +4.4%／Q4 +3.0% 確認 |
| 15 | Philippine Accommodation Pipeline Report 2026 hotel rooms projects billion pesos committed | #18 | 213 案／₱3,870 億確認；客房 45,213 vs 45,884 |
