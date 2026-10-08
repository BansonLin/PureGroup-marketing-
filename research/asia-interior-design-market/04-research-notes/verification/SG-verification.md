# 新加坡（Singapore）— 事實查核報告（SG-verification）

| 項目 | 內容 |
|---|---|
| 查核日期 | 2026-10-08 |
| 查核者 | Claude 子代理（SG-verification，懷疑立場） |
| 查核對象 | `countries/SG-A-market.md`（LENS A：市場規模／需求／玩家／價格）、`countries/SG-B-rules.md`（視角 B：法規／證照／消保／外資） |
| 原定方法 | 15 次獨立 WebSearch（英、華文重新措辭，避開分析師查詢），保留 2 次；WebFetch／curl 依環境政策封鎖 |
| **實際執行** | **0 次搜尋成功。** 本回合所有代理共用的 200 次 WebSearch 額度在本子代理啟動前已用罄；本人送出的 10 次查核搜尋全數被系統拒絕，之後停止送出。依指示未以 curl／第三方代理／快取服務繞過。本檔因此**沒有任何一項是以本回合獨立網路證據證實**。查核改以三種手段：(1) 與同一工作階段其他筆記（T1、T2、T3、T8、IN-A、MY-A/B、HK-A、VN-B、05-report/42-T2）交叉比對；(2) 全部匯率換算與衍生比率的算術重算；(3) 查核者背景知識作為方向性訊號（一律標 **D 級**、不得當作引用）。 |
| 結果 | 查核 27 項：確認 5（皆為法條／官方頁面與知識庫高度一致，非網路證據）、修正 10、推翻 1、無法驗證 11。另列 11 項內部矛盾／定義問題。整體品質：**低**（兩份筆記自承 0 次搜尋、58 條 URL 全部未開頁；本次查核亦無法補上獨立證據）。 |

> **整合者務必先讀**
> 1. 本檔「查核結果」欄的 ❓ 代表「本回合無獨立證據」，不代表原主張為假；括號內「先驗一致／先驗存疑」只是查核者記憶的方向性訊號，**不得據此把任何數字升級為【實際】**。
> 2. 本檔唯一能以本地證據裁定的，是兩份筆記之間、以及與 T1／T2／T3／T8 之間的矛盾與定義問題（見 (b) 節）。
> 3. 兩份筆記的算術（匯率換算、比率）**全部重算無誤**；問題不在算錯，而在 (i) 同一數字在不同筆記用了三套 USD/TWD（31.0／31.5／32.0），(ii) USD/SGD 1.33 為 2023–2024 年水準，可能偏弱，(iii) 2020 年預測、2017 年營收被當成現況量級。
> 4. 下一回合（使用者再送一則訊息即重置額度）請直接執行本檔「附一」的 15 條查核搜尋；屆時本檔可原地覆寫。

判定符號：✅ 確認｜✏️ 修正｜❌ 推翻｜❓ 無法驗證

---

## (a) 逐項查核表

匯率註記：本表「修正值」欄統一採 T1 慣例 **USD/SGD 1.33、USD/TWD 31.5（S$1 ≈ NT$23.68）**，與 SG-A 相同、與 SG-B（32.0，S$1 ≈ NT$24.06）不同；最終報告應以 MAS 或台銀當日中間價覆寫（https://www.mas.gov.sg/statistics/exchange-rates ，官方入口，本輪未開啟）。

| # | 項目 | 原報告值（出處） | 查核結果 | 修正值 | 證據 URL | 說明 |
|---|---|---|---|---|---|---|
| 1 | Interior fitting-out 市場規模（Frost & Sullivan） | SGD 48.751 億（2022E）≈ USD 36.7 億 ≈ NT$1,155 億；占 GDP ≈0.61%（A §1.2、§2.1、§8；B §5.1、§9；T1 §3.6） | ❓ 無法驗證（先驗一致：URL 日期 2020-05-07 符合新加坡裝修承包商 Raffles Interior Ltd 在港交所上市之招股書；2020 年預測值） | 維持為**唯一承攬口徑量級錨點**，但標題寫法改為「F&S 2020 年對 2022 年之預測 SGD 48.8 億（承攬口徑，含商用；2023–2026 無更新）【示意】」。算術重算：4,875.1 ÷ 1.33 = USD 36.66 億 ✓；× 31.5 = NT$1,155 億 ✓ | https://www1.hkexnews.hk/listedco/listconews/sehk/2020/0507/9270144/sehk19101000768.pdf （筆記既有，未開頁） | 這是 **COVID 前後做的預測**，不是觀測值；2022 實際值不明。依整合協議 §7「引用 2019–2021 數字當 2025 現況」為幻覺檢查項，報告中不得寫成「2025 年市場規模」。候補 A 級來源（D 級線索）：2023–2025 年其他新加坡裝修承包商在港交所／新交所 Catalist 的招股書行業章節（F&S／Ipsos／CIC 撰寫）。 |
| 2 | 設計服務口徑 USD 7.7 億（2024）→12.2 億（2033）；6Wresearch CAGR 5.9%；Ken Research 傢俱＋家飾 USD 11.3 億（2025） | A §1.3、§2.1、§2.3；T1 §3.6 | ❓ 無法驗證 | 三者皆 C 級、口徑互異、不可相加（兩筆記已正確標示）。0.13% GDP 之算術 ✓（770M ÷ 596bn）。建議報告只保留「設計服務口徑 USD 7–8 億【示意】、CAGR 5–6%【示意】」 | https://designbureau.sg/insights/commercial-interior-design-trends-statistics-singapore-2026-pQ5n8w/ ；https://www.6wresearch.com/industry-report/singapore-interior-design-market-outlook ；https://www.kenresearch.com/industry-reports/singapore-furniture-home-decor-market | DMI 數字經 designbureau.sg（設計公司行銷頁）二手轉引，依協議 §2 應為 D 級而非 C 級；6Wresearch 無基準年金額。「設計費占承攬 21%」（A §2.2、§7）是用 2024 年 C 級數除以 2022 年預測值，**不應出現在報告正文**。 |
| 3 | 辦公室 fit-out 單位成本（Knight Frank 2026） | USD 2,029/m²，亞太 23 城最高；東京 1,994、台北 1,593（A §1.4、§2.1、§7、§8；B §1.6、§5.1） | ❓ 無法驗證（先驗一致：KF 2025 版新加坡與東京即已並列亞太最貴，2026 版因日圓偏弱而新加坡居首屬合理） | 維持；換算重算：2,029 × 3.3058 = USD 6,707/坪 ✓；× 1.33 = SGD 8,921/坪 ✓；× 31.5 = NT$211,285/坪 ✓；SG/台北 = 1.274 ✓ | https://irei.com/publications/article/asia-pacific-office-fit-out-costs/ （轉載）；KF 原始入口 https://www.knightfrank.com/research （待開頁） | 兩筆記引用的是 irei 轉載而非 KF 原報告；KF 指南分 basic／medium／high 規格，2,029 為哪一級（或平均）未標。報告應註明「中階規格或三級平均，待核」。 |
| 4 | 辦公室 fit-out 單位成本（Cushman & Wakefield 2026） | USD 140/ft² ≈ 1,507/m²（A §2.1；B §5.1；T1 §2.3） | ❓ 無法驗證 | 維持；140 × 10.764 = 1,507/m² ✓；KF 與 C&W 差 34.6%，兩筆記「不取平均」正確 | https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office | IN-A §201 引 VN-A 註：C&W **2026 版改為「全含」口徑**（顧問、科技、傢俱、MEP、復原），與 2025 版及 KF 不可直接比較；SG-A §7 把 C&W 2026 新加坡 140 psf 對比 TW-A 的 C&W **2025** 台北 61／110／202 psf，是跨版本口徑錯配，TW-verification #14 已指出台北 2026 版升至 145 psf——**同版本對比應為新加坡 140 vs 台北 145 psf（2026）**，兩城幾乎相同，與 KF 的「新加坡為台北 1.27 倍」結論衝突，報告必須並列說明而非擇一。 |
| 5 | HDB／公寓全屋裝修每案價格帶 | S$30,000–60,000 ≈ NT$71–142 萬（A §1.5、§3、§7、§8；B §1.6、§5.1、§9；單一設計公司部落格） | ✏️ 修正（D 級，待核） | 改為分級區間【示意】：**新 BTO 4 房（≈90 m²／≈1,000 ft²）全屋 S$35,000–55,000；轉售組屋（含拆除、重做水電、磁磚）S$55,000–90,000；私人公寓 S$50,000–100,000+**。換算每單位面積：約 **S$35–90/ft² ≈ S$380–970/m² ≈ S$1,250–3,200/坪 ≈ NT$3–7.5 萬/坪**（不含傢俱家電；多數報價含木作訂製櫃）。ovon-d 的 30k–60k 大致對應「新屋」而低估轉售組屋 | 原引 https://www.ovon-d.com/2025/06/18/interior-design-in-singapore-costs-in-2025-and-whats-actually-worth-it/ ；候補 B／C 級來源（本輪未開啟）：Qanvast 年度 Renovation Cost Guide https://qanvast.com/sg ；Renopedia；HDB 無官方單價 | 查核者記憶（D 級）：Qanvast 2023–2025 各版成本指南的平均值約為 BTO 4 房 S$4–5 萬、轉售 4 房 S$6.5–7.5 萬、公寓 S$5–9 萬。**對台灣比較的關鍵含意**：新加坡住宅每坪約 NT$3–7.5 萬，**低於**台北新成屋 6–10 萬／中古屋 10–15 萬（TW-verification #9），與 A §9.1「新加坡價格最高」的印象相反——商辦單價高、住宅每坪不高，兩者必須分開陳述。單位：新加坡慣用 ft²，1 坪 = 35.58 ft²。 |
| 6 | 純設計費 | S$1,500–15,000／案（A §3、§8；B §5.1、§9） | ❓ 無法驗證（先驗一致） | 維持為【示意】；補充慣例（D 級）：新加坡多數「ID firm」為設計施工合一（design & build），設計費常「免收」或內含於施工報價；純設計顧問（不承攬）約收工程款 8–15% 或按 ft² 計 S$3–10/ft² | 原引 ovon-d（同上） | B §11 缺口「SIDS 設計費指引」：查核者記憶中新加坡設計師協會**沒有**公開的建議收費表（與馬來西亞 LAM 不同），此缺口可能無解。 |
| 7 | Livspace FY25：營收 Rs 1,460 crore（+23%）、淨損 Rs 242 crore、新加坡占 15% | A §1.6、§4.2、§8；B §1.7、§4.5、§9；T2、IN-A、MY-A | ❓ 無法驗證（算術確認） | 維持；重算：1,460 crore ÷ 86 = USD 1.698 億 ✓；15% = Rs 219 crore = USD 2,547 萬 = SGD 3,388 萬 ✓；淨損率 16.6% ✓；FY24 416→242 = −41.8%（Entrackr「42%」✓）；Inc42「−43% 至 243 crore」隱含 FY24 基期 ≈426 crore，與 461.7 不符（T2 已列矛盾表） | https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863 ；https://inc42.com/buzz/livspaces-fy25-loss-declines-43-to-inr-243-cr/ | 「新加坡 15%」若來自 Entrackr 對 Tofler／MCA 申報的解讀，屬 B 級；但新加坡實體（Livspace Pte Ltd／Interiortech Pte Ltd）ACRA 財報才是 A 級。A §4 推論「單一最大全包連鎖市占不到 1%」把 FY25 營收除以 2022E 預測值，僅能作量級。裁員「逾 1,000 人（2026）」與「約 100 人（2025）」為不同時點的累計 vs 單次，不是矛盾。 |
| 8 | Space Matrix 營收與股權 | 2017 年 >S$1.15 億；「≈USD 4,600 萬」與「Rs 1,200 crore」互相矛盾；CB Insights 載 2022-03 被 CapitaLand 收購（A §4.2、§4.3、§10；B §4.5） | ✏️ 修正 | (1) 三個營收數字**年份不同，不構成矛盾**：S$1.15 億為 2017 年（≈USD 8,650 萬）；「Rs 1,200 crore」（≈USD 1.4 億）若為 2023–2025 年集團營收，與 2017 年值相比年增率約 7–9%，量級合理；USD 4,600 萬為第三方目錄估值，不採。(2) 「被 CapitaLand 收購」查核者記憶中**無任何 CapitaLand 公告**，單源且與常識不符（CapitaLand 非設計施工業者），報告**不得引用**，改寫為「股權結構不明」 | 原引 https://www.aol.com/news/singapore-office-design-firm-space-093000697.html ；https://www.cbinsights.com/company/space-matrix | A §10 矛盾表把「不同年份」當「互相矛盾」，是定義問題而非來源衝突。 |
| 9 | CASE 2024 投訴統計：總 14,236 件（+2%）；裝修承包商 962 件（2023：1,168）；97% 針對非 CaseTrust 業者；認證業者 100% 解決 | A §1.7、§4.4、§8；B §1.4、§3.2、§9；T3 | ❓ 無法驗證（先驗一致：CASE 每年 2 月發布，裝修連年居投訴前三類，2023 年逾千件、2024 年回落之方向與記憶一致） | 維持；重算：962/1,168 = −17.6% ✓；14,236/13,991 = +1.75%（CASE 四捨五入為 +2%）✓ | https://www.case.org.sg/wp-content/uploads/2025/02/Media-Release-CASE-sees-prepayment-losses-more-than-quadruple-in-2024-entertainment-related-complaints-nearly-triple.pdf ；https://www.asiaone.com/singapore/home-renovations-make-bulk-consumers-losses-2024-case | CASE PDF 為 A／B 級原始來源，AsiaOne 為轉載，**兩者算 1 個來源**，兩筆記給「高信心」應降為「單源、中信心」直到 PDF 開頁。2025 年統計（2026-02 新聞稿）超出查核者可靠知識範圍，仍為缺口。 |
| 10 | 裝修預付款損失 S$728,000（2024）vs「CASE 另稱裝修約占預付損失 1/3」 | A §4.3、§8（「未對帳」）；B §3.2、§9；T3 | ✏️ 修正（說明） | 兩句**可同時成立**：CASE 2024 年預付款損失總額「逾四倍成長」，查核者記憶（D 級）總額約 S$2.0–2.3 百萬，則 728k ≈ 32–36% ≈「約三分之一」。報告改寫為「裝修為 2024 年預付款損失最大來源（約 S$728,000，約占三分之一）」，刪除「未對帳」 | 同 #9 | 換算：728,000 ÷ 1.33 = USD 547,368 ✓；× 31.5 = NT$1,724 萬（A）／× 32.0 = NT$1,752 萬（B）——同一數字兩個台幣值（見 #23）。 |
| 11 | CaseTrust 裝修認證：首期訂金 ≤20% 合約額＋Deposit Performance Bond；標準契約；配合 CASE 調解 | A §1.7、§4.4、§8；B §1.3、§3.1、§9；T3 | ✅ 確認（知識庫：與 CaseTrust 裝修業者認證要件一致） | 維持；補充：(1) 正式名稱為 **CaseTrust–RCMA Joint Accreditation Scheme for Renovation Businesses**（CASE 與新加坡裝修承包商及材料供應商公會 RCMA 聯合認證）；(2) 訂金保障以履約保證金（bond）為限，**非無上限**，保額與保費須向 CASE 查明；(3) HDB 對 CaseTrust 認證之 DRC 業者給 3 年名錄效期即源於此制 | https://www.case.org.sg/casetrust/renovate-your-home-with-peace-of-mind/ ；CaseTrust 官方入口 https://www.casetrust.org.sg/ （本輪未開啟） | sageshield 為第三方顧問頁，不應與 CaseTrust 官方頁並列為兩個來源。保固期：查核者記憶中 CaseTrust 標準契約含瑕疵責任條款，但年限（通常由業者填寫，市場慣例 12 個月）**非法定**，B §3.1「保固為契約約定、無法定保固」正確。 |
| 12 | HDB 組屋裝修強制由 DRC 名錄承包商承作並代申請許可；名錄效期 2 年（CaseTrust 認證 3 年）、到期前 3 個月續期 | A §1.7、§4.4、§8；B §1.2、§2.2、§9；T3 | ✅ 確認（官方頁面 URL＋知識庫一致） | 維持；補充（D 級，待核）：(1) 並非所有工程都需許可——拆牆、更換地磚、浴室防水、窗戶、冷氣穿牆等須經 DRC 承包商線上申請（HDB APEX／e-services），油漆、不拆除之櫃體安裝等免許可；(2) 許可後施工期限：**新交屋組屋 3 個月、轉售組屋 1 個月**（可申請展延）；(3) 施工時段：一般工程週一至六 09:00–18:00、噪音工程週一至五 09:00–17:00，週日與公假禁工；(4) DRC 承包商違規採**記點制**，累計達門檻即暫停或除名 | https://www.hdb.gov.sg/residential/living-in-an-hdb-flat/renovation/applying-for-approval ；https://www.hdb.gov.sg/business/renovation-contractors/renovation ；https://www.hdb.gov.sg/business/renovation-contractors/renovation/renewal-of-application-to-be-listed-in-the-drc | 對台灣業者的實務含意：**沒有 DRC 列名就連報價施工都違規**，不是「可做但不建議」；A §9.2、B §10.1 的「JV／分包持 DRC 業者」結論正確。 |
| 13 | DRC 列名年資要件：ACRA 註冊 ≥1 年＋3 年裝修經驗（CaseTrust 認證者 1 年） | A §4.4；B §2.2、§4.2、§9（fixfirst 第三方） | ❓ 無法驗證 | 不採用具體年數，改寫為「HDB 要求負責人完成『Renovation for Public Housing』課程並通過測驗、公司具 ACRA 登記、負責人無破產與詐欺紀錄；**經驗年資門檻以 HDB 官網條文為準**」 | 原引 https://fixfirst.sg/service-blog/hdb-directory-of-renovation-contractors/ ；官方 https://www.hdb.gov.sg/business/renovation-contractors/renovation | 查核者記憶中 HDB 曾要求「至少 3 年裝修經驗」但不確定現行版本；對外資公司而言，這是進入時程的關鍵變數（新設公司可能需先累積年資），必須開官方頁。 |
| 14a | 違反 HDB 裝修規定罰款 S$5,000 | A §4.4；B §2.2、§9（structures.com.sg，「未經官方驗證」） | ✅ 確認（知識庫：HDB 官網裝修頁明載屋主未經許可施工依 Renovation Control Rules 可處**最高 S$5,000** 罰款） | 「最高 S$5,000（≈USD 3,759 ≈ NT$11.8 萬）」；主體為**屋主**（flat owner），DRC 承包商則受記點／除名處分 | https://www.hdb.gov.sg/residential/living-in-an-hdb-flat/renovation （HDB 官方入口）；法源 Housing and Development (Renovation Control) Rules（Singapore Statutes Online https://sso.agc.gov.sg/ ，條文編號待核） | 兩筆記「低信心」可升為中；但 B §9 的 NT$120,301 用 32.0 匯率，A 未換算，報告統一。 |
| 14b | HDB 裝修管制規則 2025-12 以 S 725/2025 更新；BCA「CRS」2025-06-01 擴大 | A §4.4；B §2.2、§2.3、§2.5（商業來源） | ❓ 無法驗證（**先驗存疑**） | **不採用**。S 725/2025 之法規編號與內容在查核者知識庫中無對應；「CRS」在 BCA 語境指 **Contractors Registry System（承包商登記系統，用於政府工程投標，含 CR06 室內裝修工作類別）**，與 Builders Licensing Scheme 是兩套制度，第三方文章可能混用 | 原引 https://structures.com.sg/hdb-renovation-permit-guide-2026-what-every-flat-owner-must-know/ ；https://renovationcontractorsingapore.com/blogs/news/hdb-licensed-contractors-singapore-2026-complete-guide | 兩條來源皆為裝修公司 SEO 內容（D 級）。若 2025-12 確有修訂，Singapore Statutes Online 的 Subsidiary Legislation 頁可直接核對（下一回合搜尋 #4）。 |
| 15 | BCA Builders Licensing Scheme：GB Class 1／2、Specialist Builder；要件「財務與技術門檻」（數字未取得）；私宅純裝修是否需執照為缺口 | A §4.4；B §1.2、§2.3、§4.2、§11 | ✏️ 修正（補缺口，D 級待核） | (1) 法源：Building Control Act 1989 Part VA（2008-12-16 起）；**只有「需提交圖說核准的建築工程（building works requiring plan approval）」才須持照建築商**，不涉結構、外牆、消防分隔的室內裝修**不需** BCA 建築商執照；(2) **GB2 承攬金額上限 S$6 百萬（≈NT$1.4 億）、最低實收資本 S$25,000；GB1 無上限、實收資本 S$300,000**，兩級皆須指定 Approved Person（AP，管理層）與 Technical Controller（TC，具認可學歷與年資）；(3) Specialist Builder 六類（打樁、地基支撐、地質調查、鋼結構、預鑄混凝土、現場後拉預力）與室內裝修無關；(4) 涉結構變更須由 QP（註冊建築師／專業工程師）送件 | https://www1.bca.gov.sg/regulatory-info/building-control/builder-licensing （官方入口）；Building Control Act 1989 https://sso.agc.gov.sg/Act/BCA1989 （SSO，本輪未開啟） | 這解答了 T3 缺口 #4 與 B §2.3「是否一律要求 licensed builder」：**答案是否**，住宅室內裝修的實質門檻在 HDB DRC（組屋）與 MCST 附則（公寓），BCA 執照只在涉及 building works 時觸發。數字（S$6M、S$25k、S$300k）為查核者記憶，必須開 BCA 頁核對。 |
| 16 | 室內設計師無法定證照；「SIDS 與其認證室內設計師制度（IDCS）」為自願性 | A §1.7、§4.4；B §1.1、§2.1；T3 | ✏️ 修正（D 級，待核） | 「無法定證照、無名稱保護」維持 ✅（知識庫一致：新加坡無室內設計師專法）。但機構名稱有誤：**IDCS = Interior Design Confederation (Singapore)，是 SIDS（Society of Interior Designers Singapore，1985 年成立）2010 年代更名後的名稱，不是「SIDS 之下的認證制度」**；自願性設計師認證由 IDCS 推動、名稱約為 Singapore Interior Design Accreditation Council（SIDAC）之「Accredited Interior Designer」制度（2017 年前後成立，DesignSingapore Council 支持） | IDCS 官方入口（網址待核，本輪未開啟）；原引 https://www.hka.com/news/lexology-getting-the-deal-through-construction-2021-singapore-chapter/ | 對報告的意義：有自願認證可作行銷訊號（類似台灣乙級技術士），但**不影響執業合法性**。SIDAC 名稱與成立年為查核者記憶，須核對。 |
| 17 | 外資可 100% 持有新加坡公司、無本地股東要求、需 1 名常住董事 | A §1.7、§4.4；B §1.5、§4.1、§9；T3 | ✅ 確認（法條：Companies Act 1967 第 145 條要求至少一名通常居住於新加坡之董事；無外資持股上限、無室內設計業別限制） | 維持；補充（D 級）：最低實收資本 S$1；須於 6 個月內委任公司秘書；外籍負責人若欲常駐須持 EP／EntrePass，否則以名義董事（nominee director，年費約 S$2,000–3,000）滿足；公司稅 17%（新創部分免稅）、GST 9%（2024-01-01 起） | Companies Act 1967 https://sso.agc.gov.sg/Act/CoA1967 ；ACRA https://www.acra.gov.sg/ ；IRAS https://www.iras.gov.sg/ （官方入口，本輪未開啟）；原引 https://terraadvisoryservices.com/can-a-foreigner-own-100-of-a-singapore-company/ | terraadvisory 為商業顧問頁，兩筆記「中信心」合理；法條層級的事實可升為高。台星租稅協定（避免雙重課稅）存在，但細節未查，稅務仍須顧問確認（B §4.6 處理正確）。 |
| 18 | Employment Pass 薪資門檻 S$5,600（2026）；2027-01-01 起 S$6,000；「另見 S$5,000 不一致」 | A §4.4、§8；B §1.5、§4.3、§6.1、§9；T3 | ✏️ 修正 | (1) **S$5,600 是 MOM 自 2025-01-01 起對新申請的門檻（續簽自 2026-01-01 適用）**，不是「2026 年值」；金融業為 S$6,200；且門檻**隨年齡遞增**，45 歲以上約需 S$10,700；(2) **S$5,000 是 2022-09 至 2024-12 的舊門檻**，「不一致」實為新舊版本，不是來源矛盾；(3) 「2027-01-01 起 S$6,000」**僅見於一家人力仲介部落格**，查核者知識庫（至 2026 年中）無 MOM 公告，**不採用**，改寫為「MOM 約每 2–3 年上調，下次調整時點與金額待 MOM 公告」；(4) COMPASS 評分（2023-09 起）與 MyCareersFuture 刊登 14 日（公平考量框架）正確 | MOM EP 資格頁 https://www.mom.gov.sg/passes-and-permits/employment-pass/eligibility （官方入口，本輪未開啟）；原引 https://singaporeemploymentagency.com/hiring-foreign-interior-designer-singapore-employment-pass/ | 對台灣業者：外派 30 歲上下設計師月薪成本 ≥S$5,600 ≈ NT$13.3 萬（31.5）是硬門檻；資深者門檻更高，B §10.3 的「至少 NT$13.5–14.4 萬起跳」方向正確但低估資深人員。 |
| 19 | ASTEP：2014-04-19 生效；服務業負面表列；台灣後續自由化自動適用；**2028-01-01 全面實施** | A §1.7、§4.4、§8；B §1.5、§4.4、§9；T3 | ✏️ 修正（定義） | (1) 2013-11-07 簽署、**2014-04-19 生效** ✅（知識庫一致）；(2) 服務貿易採負面表列 ✅（台灣首個負面表列 FTA）；(3) **「2028-01-01 全面實施」指的是台灣對新加坡貨品關稅分 15 年降至零的最後期限（新加坡對台灣貨品自生效即零關稅），與服務業無關**；設計／裝修服務的國民待遇與市場進入承諾**自 2014 年生效起即適用**，報告不得暗示 2028 年前服務業有限制；(4) 附件 8B 新加坡保留清單是否涵蓋建築／室內設計仍待核，但因新加坡對室內設計無執業管制，實務上無可保留之措施（D 級推論） | https://www.enterprisesg.gov.sg/industries/wholesale-trade/astep ；協定全文 https://www.enterprisesg.gov.sg/-/media/esg/files/industries/wholesale-trade/ASTEP/astep_30_04_2014_v8_final.pdf ；https://www.ey.gov.tw/File/872DE9FBD9B635ED ；經濟部國際貿易署 ASTEP 專區（入口 https://www.trade.gov.tw/ ，本輪未開啟） | 兩筆記與 T3 把「2028 全面實施」寫在法規摘要首段，容易被讀成「協定 2028 年才完全生效」；建議整合時改寫為「貨品關稅 2028 年前全數歸零；服務承諾已生效」。 |
| 20 | 人均 GDP USD 99,365（2025）；人口 6.0 百萬；名目 GDP ≈USD 6,000 億 | A §1.2、§2 Inferences、§7、§8；B §5.1、§9；T1 §5 | ✏️ 修正（小幅） | (1) 人口：SingStat《Population in Brief 2025》總人口 **611 萬（2025-06）**，居民 420 萬、公民 366 萬（D 級，數量級確定）；以 6.11 重算名目 GDP ≈ USD 6,070 億、F&S 占 GDP **0.60%**（原 0.61%）、人均承攬 **USD 600**（原 608）、設計服務占 0.127%——結論不變；(2) 人均 GDP：SingStat 2024 年實際值 ≈ S$121,000 ≈ USD 90,700；IMF 2025 估計值落在 USD 95,000–100,000 之間，99,365 可用但應標「IMF WEO 估計」而非實際 | SingStat Population in Brief https://www.singstat.gov.sg/publications/population/population-trends ；SingStat 國民所得 https://www.singstat.gov.sg/find-data/search-by-theme/economy/national-accounts/latest-data ；IMF WEO https://www.imf.org/en/Publications/WEO （官方入口，本輪未開啟）；原引 Worldometers 轉載 | A §8 以「人口 6.0 百萬未驗證」自我標註正確；T8 §3.7 用同一 F&S 數字算出「≈0.7% GDP」，與 A 的 0.61% 不一致（分母不同），見 (b)-7。 |
| 21 | 住宅存量、屋齡、HDB 完工／轉售、URA 交易：「本輪無資料」 | A §3 Gaps、§11；B §5.2、§11 | ❌ 推翻（本地證據）＋補值 | 「本工作階段無資料」不成立：**T8 §2.4、§4、§6 已載有附 HDB／URA／SingStat URL 的未驗證值**（HDB 轉售 28,986 戶 2024 +8.4%；BTO 2025 推出 >2.5 萬戶；HDB 組屋約 110 萬＋私宅約 44 萬戶；裝修貸款上限；SSD 2025-07 加碼），兩份筆記應引用 T8 而非寫「無資料」。查核者補充（D 級【示意】，與 T8 方向一致）：HDB 管理組屋 **≈110–112 萬戶**，約 77–80% 居民家戶住組屋、自有率 ≈90%；私人住宅存量 ≈42–44 萬戶；**屋齡 ≥30 年組屋（1995 年前建成）約占組屋存量 45–55%**（T8 以 30% 示意，偏低）；HIP 適用 1997 年前建成組屋，累計涵蓋約 55 萬戶；HDB 年完工 ≈2 萬戶（2021–2025 累計約 10 萬戶）；HDB 轉售 2024 年 28,986 戶（+8.4%）、2025 年約 2.6–2.9 萬戶；轉售價格指數 2024 +9.7%、2025 約 +5–7%；私宅新售 2024 ≈6,500 戶（16 年低點）、2025 回升至 ≈1.1–1.3 萬戶；私宅轉售每年 ≈1.3–1.5 萬戶。→ **二手（轉售）交易占住宅交易約 70–75%**，與 T8「0.75」示意一致 | HDB 轉售統計 https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-statistics ；HDB 年報 https://www.hdb.gov.sg/cs/infoweb/about-us/news-and-publications/annual-reports ；URA 房地產統計 https://www.ura.gov.sg/Corporate/Property/Property-Data ；HIP https://www.hdb.gov.sg/residential/living-in-an-hdb-flat/sers-and-upgrading-programmes/upgrading-programmes/types/home-improvement-programme-hip （皆官方入口，T8 既有，本輪未開啟） | 與 MY-verification #1 同類的流程問題：T8 與 SG-A／B 同日產出，彼此未互引。所有數字仍為【示意】，但「無資料」的敘述必須刪除，否則報告會低估新加坡的翻修需求引擎（存量老化＋轉售為主）。 |
| 22 | 銀行裝修貸款上限 S$30,000 或 6 倍月薪（取低者）、最長 5 年 | A §3 Gaps（「無來源」）；T8 §6（「研究者既有知識」） | ✅ 確認（知識庫：MAS 對銀行無擔保裝修貸款的監管上限，DBS／OCBC／UOB 產品頁均載「依 MAS 規定」） | 「裝修貸款：S$30,000 或 6 倍月薪取低者，期限 ≤5 年，利率約 3–6%；可與 HDB 貸款並行」【示意，待開 MAS／銀行頁】 | MAS https://www.mas.gov.sg/ ；DBS renovation loan https://www.dbs.com.sg/personal/loans/renovation-loan （官方入口，本輪未開啟） | 對定價的含意：S$30,000 上限正好落在 BTO 全屋裝修預算帶下緣，是新加坡「新屋裝修預算常態 S$3–5 萬」的制度性原因之一（D 級推論）。 |
| 23 | 匯率假設與台幣換算 | SG-A：USD/SGD 1.33、USD/TWD 31.5（S$1 ≈ NT$23.68）；SG-B：1.33、32.0（S$1 ≈ NT$24.06）；T2：31.0；42-T2 章節：31.0 | ✏️ 修正（內部矛盾） | 同一工作階段對 S$→NT$ 出現 **23.3／23.68／24.06 三個換算值**，同一數字在不同筆記差 1.6–3.2%：Livspace 新加坡營收 NT$7.9（42-T2）／8.0（A）／8.2 億（B）；Space Matrix NT$26.8（B，實為 T2 的 31.0）／27.2（A）／27.7 億（B 自身假設應得值）；CASE 損失 NT$1,724／1,752 萬；EP 門檻 NT$13.3／13.5 萬。**B 註明採 32.0 卻直接抄 T2 的 31.0 換算值（Space Matrix NT$26.8 億），自身不一致。** V1 統一採 T1 的 1.33／31.5，定稿以 MAS 中間價覆寫 | https://www.mas.gov.sg/statistics/exchange-rates | 查核者記憶（D 級）：新元 2025 年對美元升值，USD/SGD 年末約 1.28–1.30；若實際為 1.29，F&S 的 USD 值應為 37.8 億（+3%）、所有 S$ 計價數字的 USD／NT$ 值同步上修 3%。 |
| 24 | 2026-08 室內設計師因「直接付款」侵吞客戶款項被捕 | A §4.3、§6；B §1.4、§3.4（The Star 2026-08-15，經 VN-B） | ❓ 無法驗證（超出查核者知識截止） | 維持為單一事件，標「單一媒體報導」；不得據以推論案件數趨勢 | https://www.thestar.com.my/aseanplus/aseanplus-news/2026/08/15/interior-designer-arrested-in-singapore-for-allegedly-pocketing-clients-money-in-direct-payment-scheme | The Star 為馬來西亞媒體轉載新加坡新聞，原始來源應為 Straits Times／CNA／警方新聞稿。 |
| 25 | MTI 2024-05、2025-02 國會書面答覆：維持 CaseTrust 自願制、不強制裝修業執照 | A §4.4；B §1.3、§2.5、§8.1；T3 | ❓ 無法驗證（先驗一致：新加坡政府對裝修業一貫採「DRC 登記＋自願認證＋CPFTA 執法」立場） | 維持；補充法源：不公平交易依 **Consumer Protection (Fair Trading) Act 2003（CPFTA）**，2018 年起由 CCCS 執法；CPFTA 的「檸檬法」條款僅適用於商品，不適用裝修服務 | https://mti.gov.sg/Newsroom/Parliamentary-Replies/2024/05/Written-reply-to-PQs-on-disputes-arising-from-Interior-Design-and-Renovation-firms ；https://www.mti.gov.sg/Newsroom/Parliamentary-Replies/2025/02/Written-reply-to-PQ-on-consumer-protection-for-customers-of-non-accredited-renovation-contractors ；CPFTA https://sso.agc.gov.sg/Act/CPFTA2003 | 兩條 MTI URL 格式與 MTI 網站一致，可信度高；CCCS 指引年份仍缺。 |
| 26 | Small Claims Tribunals 金額上限（B 列為缺口） | B §3.3、§11 | ✏️ 補缺口（D 級法條） | **S$20,000；雙方書面同意可提高至 S$30,000**（Small Claims Tribunals Act 1984，2019 年修正後）；裝修契約屬「服務契約」可受理；申訴費低、不得委任律師；提告時效 2 年 | Small Claims Tribunals Act 1984 https://sso.agc.gov.sg/Act/SCTA1984 ；State Courts https://www.judiciary.gov.sg/civil/small-claims （官方入口，本輪未開啟） | 對比：多數 HDB 全屋裝修合約 S$3–9 萬超過 SCT 上限，大額糾紛須走 CASE 調解或地方法院，這是 CaseTrust 履約保證的價值所在。 |

---

## (b) 內部矛盾與定義問題

1. **「無資料」與 T8 的矛盾（最重要）**：SG-A §3、§11 與 SG-B §5.2、§11 宣稱住宅完工、轉售、存量、屋齡、裝修貸款皆「無資料」，但 T8 §2.4、§4、§6 已有附官方 URL 的未驗證值（#21）。整合時以 T8 覆蓋，並把兩筆記的缺口表改為「有 D 級示意值，待驗證」。
2. **三套 USD/TWD 匯率（31.0／31.5／32.0）**：同一 S$ 或 Rs 數字在 SG-A、SG-B、T2、42-T2 章節出現最多三個台幣值；SG-B 自報 32.0 卻混用 T2 的 31.0 結果（#23）。
3. **2020 年預測被當成市場現況**：F&S SGD 48.8 億是 2020 年對 2022 年的預測，A §7、§8 與 T1 §5.2、T8 §3.7 均用它計算「占 GDP」「人均」「每戶」；其中 T8 更以**含商用**的 fit-out 總值除以住宅戶數得「每戶 USD 2,370」，是口徑錯配（#1、#20）。
4. **同一數字不同 GDP 占比**：F&S 48.8 億在 SG-A／T1 為 0.61% GDP，在 T8 §3.7 為 ≈0.7%，分母（GDP 基準年／人口）不同而未說明。
5. **商辦 fit-out 的跨版本比較**：SG-A §7 以 C&W **2026** 新加坡 140 psf 對比 C&W **2025** 台北 61／110／202 psf；TW-verification #14 已確認台北 2026 版為 145 psf。同版本對比下新加坡 ≈ 台北，與 Knight Frank 的 1.27 倍結論衝突，報告須並列兩家並說明規格口徑（#4）。
6. **「設計費占承攬 21%」為跨年份、跨等級的除法**（C 級 2024 ÷ 預測 2022E），A §2.2、§7 標「極低信心」仍列入比較表，建議移出正文。
7. **Space Matrix「矛盾」實為年份不同**（2017 vs 近年），A §10 矛盾表分類錯誤；CapitaLand 收購為單源且與常識不符（#8）。
8. **SIDS／IDCS 關係寫反**：B §2.1 把 IDCS 寫成 SIDS 的認證制度，實為更名後的協會名稱（#16）。
9. **EP「S$5,000 不一致」實為新舊門檻**，「2027 年 S$6,000」單源（#18）；B §10.3 以 2027 值計算外派成本，前提未證。
10. **ASTEP「2028-01-01 全面實施」語意錯置**：指貨品關稅分期，不影響服務業（#19）；三份筆記（A、B、T3）同句照抄，是「多個筆記引用同一來源不算三角驗證」的典型。
11. **CaseTrust 訂金上限與 DRC 效期的來源層級**：官方頁（CASE、HDB）與第三方指南（sageshield、fixfirst）並列為「兩個來源」給中信心，依協議 §4 應只算 1 個來源；反之 HDB 罰款 S$5,000 只引第三方而未引 HDB 官網，信心被低估（#11、#12、#14a）。

另：SG-A 與 SG-B 之間**沒有**發現數字上的直接衝突（兩者繼承同一組 T1／T2／T3 數據），這代表「兩位分析師一致」在本案**不構成任何交叉驗證**。

---

## (c) 整體評估

- **品質：低。** 兩份筆記自承 0 次搜尋、58 條 URL 全部未開頁；本次查核也 0 次搜尋成功，無法補上獨立證據。所有「確認」皆為法條／官方頁面與查核者知識庫比對，非網路證據。
- **可用之處**：(1) 算術與換算全部正確；(2) 法規架構（無設計師證照、HDB DRC 強制、BCA 僅管 building works、CaseTrust 自願、外資 100%、ASTEP 負面表列）的**方向**與查核者知識一致，可作報告骨架；(3) 兩位分析師對來源等級與缺口的自我標註誠實且完整。
- **不可用之處**：(1) 市場規模只有 2020 年預測與 C 級市調，**沒有任何 2024–2026 的 A／B 級數字**；(2) 住宅單價只有一條行銷部落格，且其量級可能低估轉售組屋與公寓；(3) 住宅存量／交易「無資料」的敘述錯誤（T8 已有）；(4) 三處法規敘述有定義錯誤（ASTEP 2028、SIDS／IDCS、EP 2027）；(5) 2017 年營收（Space Matrix）與 2020 年預測（F&S）被用於 2025 年量級推論。
- **對最終報告的建議**：新加坡章節可用「法規最開放但承攬端強制 DRC、商辦單價亞太最高而住宅每坪不高、市場高度分散且全包連鎖尚未獲利」三句話定調，但**所有金額一律標【示意】**，直到附一的 15 條搜尋跑完並開頁。
- **本查核的限制**：所有 D 級補值（住宅分級單價、HDB 存量與交易、BCA 門檻金額、SCT 上限、EP 年齡級距、人口 611 萬）皆為查核者記憶，可能過時 1–2 年；2026 年 6 月以後的事件（The Star 2026-08、CASE 2026-02 新聞稿、S 725/2025）一律未核。

---

## (d) 建議採用值（最終報告 headline；全部待下一回合開頁覆核）

| 指標 | 建議值 | 年份 | 來源 URL | 信心／等級 | 備註 |
|---|---|---|---|---|---|
| 裝修市場規模（承攬口徑，住宅＋商用） | **SGD 48.8 億 ≈ USD 36.7 億 ≈ NT$1,155 億**（僅作量級） | 2022E（2020 年預測） | https://www1.hkexnews.hk/listedco/listconews/sehk/2020/0507/9270144/sehk19101000768.pdf | 低–中／B（上市文件）但年份舊 →【示意】 | 寫明「2020 年 F&S 預測，無 2023–2026 更新」；不得寫成 2025 現況 |
| 室內設計服務口徑 | **USD 7–8 億**（0.12–0.13% GDP） | 2024 | https://designbureau.sg/insights/commercial-interior-design-trends-statistics-singapore-2026-pQ5n8w/ | 低／C–D →【示意】 | 僅用於跨國「設計服務／GDP 比」錨點 |
| 成長率 | **4–6%／年**（6Wresearch 5.9% CAGR 2025–2031；名目 GDP 4–5% 為合理性上限） | 2025–2031 | https://www.6wresearch.com/industry-report/singapore-interior-design-market-outlook | 低／C →【示意】 | 無官方數列 |
| 辦公室 fit-out 單位成本 | **Knight Frank USD 2,029/m²（≈NT$21.1 萬/坪，亞太最高）；Cushman & Wakefield USD 140/ft²（≈USD 1,507/m²，2026 全含口徑）** 並列 | 2026 版（Q4 2025 資料） | https://irei.com/publications/article/asia-pacific-office-fit-out-costs/ ；https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office | 中高／B | 與台北比較須同機構同版本（KF：1.27 倍；C&W 2026：140 vs 145 psf ≈ 持平） |
| 住宅全屋裝修每案 | **BTO 新組屋 S$3.5–5.5 萬；轉售組屋 S$5.5–9 萬；公寓 S$5–10 萬+**（≈NT$83–237 萬） | 2024–2025 | 候補：https://qanvast.com/sg （年度成本指南，待開）；原引 ovon-d | 低／D →【示意】 | 不含傢俱家電；以 Qanvast／Renopedia 指南覆寫 |
| 住宅每單位面積 | **S$35–90/ft² ≈ S$380–970/m² ≈ NT$3–7.5 萬/坪** | 2024–2025 | 同上 | 低／D →【示意】 | 低於台北新成屋 6–10 萬/坪；報告須點出「商辦貴、住宅每坪不貴」 |
| 設計費慣例 | **D&B 公司多免收或內含；純設計顧問 S$1,500–15,000／案或工程款 8–15%** | 2025 | 原引 ovon-d | 低／D →【示意】 | 協會無公開費率表 |
| 住宅存量 | **HDB ≈110 萬戶（居民家戶約 77–80% 住組屋）＋私宅 ≈43 萬戶；屋齡 ≥30 年組屋約占 45–55%** | 2024–2025 | https://www.hdb.gov.sg/cs/infoweb/about-us/news-and-publications/annual-reports ；https://www.ura.gov.sg/Corporate/Property/Property-Data | 低／D →【示意】（量級確定） | 以 HDB 年報、URA 覆寫 |
| 住宅交易 | **HDB 轉售 28,986 戶（2024，+8.4%）、2025 約 2.6–2.9 萬戶；私宅新售 2024 ≈6,500、2025 ≈1.1–1.3 萬戶；私宅轉售 ≈1.3–1.5 萬戶／年；二手占交易約 70–75%** | 2024–2025 | https://www.hdb.gov.sg/residential/buying-a-flat/buying-procedure-for-resale-flats/resale-statistics ；URA 同上 | 2024 HDB 轉售：中／D；其餘低 →【示意】 | T8 既有值，兩筆記應引用 |
| 住宅完工 | **HDB 年完工 ≈2 萬戶；BTO 2025 推出 >2.5 萬戶（含 SBF）** | 2024–2025 | HDB 年報（同上） | 低／D →【示意】 | — |
| 裝修貸款 | **≤S$30,000 或 6 倍月薪（取低）、≤5 年** | 現行 | https://www.mas.gov.sg/ ；https://www.dbs.com.sg/personal/loans/renovation-loan | 中／D（法規慣例） | — |
| 裝修投訴 | **CASE 962 件（2024；2023：1,168）；預付款損失 ≈S$728,000（約占總預付損失 1/3）** | 2024 | https://www.case.org.sg/wp-content/uploads/2025/02/Media-Release-CASE-sees-prepayment-losses-more-than-quadruple-in-2024-entertainment-related-complaints-nearly-triple.pdf | 中／A–B（單源未開頁） | 2025 年值待 2026-02 新聞稿 |
| 最大全包連鎖 | **Livspace 新加坡營收 ≈Rs 219 crore ≈ USD 2,550 萬 ≈ SGD 3,390 萬 ≈ NT$8.0 億（集團 15%）；集團淨損率 −16.6%** | FY25（2024-04～2025-03） | https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863 | 中／B | 台幣值統一用 31.5 |
| 人均 GDP／人口 | **USD ≈99,000（IMF 2025 估計；2024 實際 ≈USD 90,700）；人口 611 萬（2025-06）** | 2025 | https://www.imf.org/en/Publications/WEO ；https://www.singstat.gov.sg/publications/population/population-trends | 中／A（入口未開頁） | 以 6.11 百萬重算：F&S 占 GDP 0.60%、人均承攬 USD 600 |
| EP 薪資門檻 | **S$5,600（2025-01-01 起新申請；隨年齡遞增至 ≈S$10,700）** | 2025–2026 | https://www.mom.gov.sg/passes-and-permits/employment-pass/eligibility | 高／A（法規，入口未開頁） | 「2027 年 S$6,000」不採 |
| 匯率 | **USD/SGD 1.33、USD/TWD 31.5（S$1 ≈ NT$23.68）**，定稿以 MAS 中間價覆寫 | 2025–2026 假設 | https://www.mas.gov.sg/statistics/exchange-rates | — | 新元 2025 年升值，1.33 可能偏弱 3% |

---

## (e) 法規要點確認

以下各項「確認」為法條／官方頁面與查核者知識庫（截至 2026 年中）比對結果，**非本回合網路搜尋**；URL 標「筆記既有」者為兩份筆記已附之官方網址，標「待核」者為查核者依法規名稱給出的 Singapore Statutes Online（SSO）／主管機關入口，需在下一回合開頁核對。

| # | 要點 | 內容（查核後） | 法源／主管機關 URL | 等級 |
|---|---|---|---|---|
| L1 | 室內設計師執業 | **無法定證照、無名稱保護、無執業考試**；IDCS（前身 SIDS）為自願性協會，SIDAC 認證為自願 | Building Control Act 1989（僅管 building works 與 QP）https://sso.agc.gov.sg/Act/BCA1989 （待核）；原引 https://www.hka.com/news/lexology-getting-the-deal-through-construction-2021-singapore-chapter/ | 確認（D 級法條）；協會名稱已修正（#16） |
| L2 | 涉結構／外牆／消防之工程 | 須由 **Qualified Person（註冊建築師或專業工程師）**送件並監督；建築工程需圖說核准者，施工方須為 **BCA 持照建築商**（GB1 無上限／GB2 ≤S$6M；Specialist Builder 六類） | BCA Builders Licensing https://www1.bca.gov.sg/regulatory-info/building-control/builder-licensing （筆記既有）；Building Control Act 1989 Part VA（待核） | 確認（架構）；金額門檻 D 級待核（#15） |
| L3 | 不涉 building works 之室內裝修 | **不需 BCA 建築商執照**；政府工程投標另有 BCA Contractors Registry System（CRS）工作類別 CR06「室內裝修」，屬登記非執照 | BCA CRS 頁（入口 https://www1.bca.gov.sg/ ，路徑待核） | 確認（D 級）；修正「CRS 擴大」之誤讀（#14b） |
| L4 | HDB 組屋裝修 | **強制由 HDB Directory of Renovation Contractors（DRC）列名承包商承作**並代屋主線上申請許可；名錄效期 2 年（CaseTrust 認證 3 年）；新屋 3 個月／轉售 1 個月施工期限；工時限制；屋主違規最高罰 **S$5,000**；承包商記點制 | HDB https://www.hdb.gov.sg/residential/living-in-an-hdb-flat/renovation/applying-for-approval ；https://www.hdb.gov.sg/business/renovation-contractors/renovation （筆記既有）；Housing and Development (Renovation Control) Rules（SSO https://sso.agc.gov.sg/ ，條號待核） | 確認（#12、#14a）；年資要件與 S 725/2025 待核（#13、#14b） |
| L5 | 專項工程執照 | 窗戶工程須 **BCA 核准窗戶承包商**；電氣工程須 **EMA 持照電工**；給排水須 **PUB 持照水管工**；瓦斯須 EMA 持照瓦斯工 | HDB 同上；BCA 窗戶承包商名錄、EMA https://www.ema.gov.sg/ 、PUB https://www.pub.gov.sg/ （入口，待核） | 確認（D 級） |
| L6 | 私人公寓裝修 | 依 **Building Maintenance and Strata Management Act 2004（BMSMA）** 下各 MCST 附則：事前書面申請、可退還裝修押金（市場慣例 S$1,000–5,000）、工時與電梯保護規定；涉結構仍回到 L2 | BMSMA https://sso.agc.gov.sg/Act/BMSMA2004 （待核）；BCA 分層管理 https://www1.bca.gov.sg/ | 補缺口（D 級） |
| L7 | 消防（商業空間） | 商業單位之室內裝修若涉消防分隔、灑水、逃生動線，須由 QP 向 **SCDF（Fire Safety and Shelter Department）**送審並取得 **Fire Safety Certificate** 後方可使用；住宅內部裝修一般不需 | Fire Safety Act 1993 https://sso.agc.gov.sg/Act/FSA1993 （待核）；SCDF https://www.scdf.gov.sg/ | 補缺口（D 級） |
| L8 | 用途變更 | 商業空間變更用途（如零售→餐飲）須向 **URA** 申請規劃許可 | URA https://www.ura.gov.sg/Corporate/Guidelines/Development-Control （待核） | 補缺口（D 級） |
| L9 | 消費者保護（自願認證） | **CaseTrust–RCMA 聯合認證**：首期訂金 ≤20%、訂金履約保證金、標準契約、接受 CASE 調解；非認證業者無法定訂金上限、無法定保固 | https://www.case.org.sg/casetrust/renovate-your-home-with-peace-of-mind/ （筆記既有）；https://www.casetrust.org.sg/ （待核） | 確認（#11） |
| L10 | 消費者保護（法定） | **Consumer Protection (Fair Trading) Act 2003**：不公平交易行為（CCCS 執法）；**Small Claims Tribunals**：上限 S$20,000（合意 S$30,000）；CASE 調解；Singapore Mediation Centre；侵占訂金可報警（刑事） | CPFTA https://sso.agc.gov.sg/Act/CPFTA2003 ；SCT https://sso.agc.gov.sg/Act/SCTA1984 ；CCCS 指引 https://www.ccs.gov.sg/media-and-events/newsroom/announcements-and-media-releases/cccs-publishes-guide-on-fair-trading-practices-for-renovation-industry/ （筆記既有） | 確認（#25、#26，D 級法條） |
| L11 | 政府立場 | MTI 2024-05、2025-02 國會答覆：**不另設強制執照**，以 DRC＋CaseTrust＋CPFTA 處理 | https://mti.gov.sg/Newsroom/Parliamentary-Replies/2024/05/Written-reply-to-PQs-on-disputes-arising-from-Interior-Design-and-Renovation-firms ；https://www.mti.gov.sg/Newsroom/Parliamentary-Replies/2025/02/Written-reply-to-PQ-on-consumer-protection-for-customers-of-non-accredited-renovation-contractors | 先驗一致（#25） |
| L12 | 外資設立 | **100% 外資、無本地股東要求**；至少 1 名常住董事（Companies Act s.145）；最低資本 S$1；公司稅 17%、GST 9%；室內設計業無特別限制 | Companies Act 1967 https://sso.agc.gov.sg/Act/CoA1967 ；ACRA https://www.acra.gov.sg/ ；IRAS https://www.iras.gov.sg/ | 確認（#17） |
| L13 | 外資承攬 | 外資公司**可**申請 DRC（須完成 HDB 課程、符合年資）與 BCA 執照（AP／TC 可為持 EP 之外籍人員，須符合認可資格）；建築業 Work Permit 受依賴比率上限（DRC）、人力稅（levy）與來源國限制，台灣工班**不可直接輸出** | HDB、BCA 同上；MOM Work Permit（建築業）https://www.mom.gov.sg/passes-and-permits/work-permit-for-foreign-worker/sector-specific-rules/construction-sector-requirements （待核） | 架構確認；配額與 levy 數字仍缺 |
| L14 | 外籍設計師簽證 | **EP 門檻 S$5,600（2025-01-01 起；年齡遞增）＋COMPASS 評分＋MyCareersFuture 刊登 14 日**；S Pass 門檻另定 | MOM https://www.mom.gov.sg/passes-and-permits/employment-pass/eligibility | 確認（#18）；「2027 年 S$6,000」不採 |
| L15 | 貿易協定 | **ASTEP 2014-04-19 生效、服務負面表列、承諾即時適用**；「2028-01-01」為台灣對星貨品關稅歸零期限，與服務無關；CPTPP 台灣 2021-09-22 申請、未啟動談判 | https://www.enterprisesg.gov.sg/industries/wholesale-trade/astep ；協定全文（筆記既有）；https://www.ey.gov.tw/File/872DE9FBD9B635ED | 確認＋語意修正（#19） |

---

## 附一：下一回合應補跑的 15 條獨立查核搜尋（依重要性排序；與分析師附錄 B 的 20 條研究搜尋不重複）

1. `Qanvast renovation cost guide 2025 average 4-room BTO resale condo` — 覆寫 #5 住宅分級單價
2. `Knight Frank Asia-Pacific fit-out cost guide 2026 Singapore 2,029 specification basic medium high` — 確認 #3 規格層級
3. `Cushman Wakefield office fit out cost guide 2026 Singapore Taipei USD per sq ft` — 同版本對比 #4
4. `Singapore Statutes Online Housing and Development Renovation Control Rules 2025 amendment` — 裁決 #14b S 725/2025
5. `HDB Directory of Renovation Contractors listing criteria experience years training course` — 裁決 #13
6. `BCA general builder class 2 contract value limit paid-up capital approved person technical controller` — 核對 #15 數字
7. `MOM employment pass qualifying salary 2026 2027 increase announcement` — 裁決 #18 的 2027 說法
8. `CASE annual complaints statistics 2025 renovation contractors prepayment losses` — 補 2025 年值（#9、#10）
9. `HDB resale transactions 2025 full year resale price index 4Q2025` — 覆寫 #21
10. `URA private residential statistics 2025 new sale resale units full year` — 覆寫 #21
11. `HDB flats built before 1995 number HIP eligible flats 1997` — 屋齡 ≥30 年占比（#21）
12. `Singapore Statutes Online 臺星 ASTEP 關稅 分期 2028 服務貿易 附件 8B` — 裁決 #19
13. `Interior Design Confederation Singapore IDCS formerly SIDS accreditation SIDAC` — 裁決 #16
14. `Raffles Interior prospectus Frost Sullivan Singapore interior fitting-out market 2022 2024 update HKEX Catalist` — 尋找 #1 的更新版
15. `Space Matrix revenue 2024 ownership CapitaLand acquisition` — 裁決 #8

保留 2 次：`MAS renovation loan 30,000 six times monthly income regulation` 與 `SingStat Population in Brief 2025 total population 6.11 million`。
