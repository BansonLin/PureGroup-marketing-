# 馬來西亞（Malaysia）— 事實查核報告（MY-verification）

| 項目 | 內容 |
|---|---|
| 查核日期 | 2026-10-08 |
| 查核者 | Claude 子代理（MY-verification，懷疑立場） |
| 查核對象 | `countries/MY-A-market.md`（LENS A：市場結構／規模／價格）、`countries/MY-B-rules.md`（視角 B：法規／證照／消保／外資） |
| 原定方法 | 15 次獨立 WebSearch（以馬來文重新措辭，避開分析師查詢），WebFetch／curl 依環境政策封鎖 |
| **實際執行** | **0 次搜尋成功。** 本回合所有代理共用的 200 次 WebSearch 額度在本子代理啟動前已用罄（與兩位分析師遭遇相同）。依指示不得以 curl／第三方代理／快取服務繞過。本檔因此**沒有任何獨立網路證據**；查核改以三種可用手段進行：(1) 以同一工作階段其他筆記（T1、T2、T3、T8、SG-A、TW-B、VN-B）中與馬來西亞相關、兩位分析師未引用或與其矛盾的內容做交叉比對；(2) 算術、匯率與定義一致性審計；(3) 查核者背景知識作為「存疑／一致」的方向性訊號（一律標 D 級、無 URL、不得當作引用）。 |
| 結果 | 查核 22 項：確認 0、修正 3、推翻 1、無法驗證 18。另列 12 項內部矛盾／定義問題。整體品質：**低**（兩份筆記自承零次搜尋、所有 URL 未開頁；本次查核亦無法補上獨立證據）。 |

> **整合者務必先讀**：
> 1. 本檔所有「查核結果」欄中的 ❓ 代表「本次無獨立證據」，不代表原主張為假；括號內「先驗一致／先驗存疑」只是查核者記憶的方向性訊號，**不得升級任何數字為【實際】**。
> 2. 本檔唯一能以「本地證據」裁定的項目，是兩份筆記與 T1 §3.7、T2、T8 之間的矛盾（見 #1、#20–#22）。
> 3. 下一回合（使用者再送一則訊息即重置額度）請直接執行本檔「附一」的 15 條查核搜尋與兩份筆記附錄 B 的 20 條研究搜尋；屆時本檔可原地覆寫。

判定符號：✅ 確認｜✏️ 修正｜❌ 推翻｜❓ 無法驗證

---

## (a) 逐項查核表

匯率註記：本表「修正值」欄的美元／新台幣換算統一採本工作階段 T1／T8 慣例 **USD/MYR 4.40、USD/TWD 31.5（RM1 ≈ NT$7.16）**，與 MY-A（4.20／31.5，RM1 ≈ NT$7.50）、MY-B（4.40／32.0，RM1 ≈ NT$7.27）皆不同；最終報告應以 BNM 當日中間價覆寫（https://www.bnm.gov.my/exchange-rates ，官方入口，本輪未開啟）。

| # | 項目 | 原報告值（出處） | 查核結果 | 修正值 | 證據 URL | 說明 |
|---|---|---|---|---|---|---|
| 1 | 「本工作階段沒有任何附 URL 的馬來西亞市場規模來源；唯一出現過的國家級數字是 DOSM RM 20 億」 | MY-A §2 Takeaway、§2 Cited Findings、§1.1 | ❌ 推翻（本地證據） | 刪除此句。T1 §3.7 已載有 7 條附 URL 的馬來西亞數字：Ken Research 傢俱＋室內設計 USD 24.3 億（2025）；Ken Research 居家修繕 ≈USD 10 億（2025）；Ken 引用住宅交易總值 RM 1,082.7 億（2025）；6Wresearch 室內設計成長率 5.8%；Houz／zacharykhaw 單價與設計費；Turner & Townsend 吉隆坡高階辦公室 fit-out RM 6,908/m²（2026）；DOSM Construction Statistics Q4 2025 頁面 | T1 §3.7：https://www.kenresearch.com/industry-reports/malaysia-furniture-and-interior-design-market ；https://www.kenresearch.com/industry-reports/malaysia-home-improvement-market ；https://www.6wresearch.com/industry-report/malaysia-interior-design-market-outlook ；https://www.houz.com.my/interior-design-cost-malaysia/ ；https://zacharykhaw.com/2025/09/05/interior-design-cost-malaysia/ ；https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026/asia-pacific ；https://www.dosm.gov.my/portal-main/release-content/construction-statistics-fourth-quarter-2025 | T1 檔案於 17:13 更新、MY-A 於 17:10 存檔，MY-A 當時可能未見 T1 最終版，屬流程問題而非分析師失誤；但最終報告必須以 T1 §3.7 取代 MY-A §2 的「無資料」。這些 URL 同樣未開頁，等級 C（市調公司）／B（T&T）。 |
| 2 | 室內設計市場規模 | MY-A：無資料；T1 §3.7：Ken Research「傢俱＋室內設計」USD 24.3 億（2025）；T1 另註「前稿同機構 USD 54.2 億，矛盾」 | ❓ 無法驗證（先驗存疑） | 不給單一 headline。若引用，寫「Ken Research 傢俱＋室內設計（含家飾）USD 24.3 億（2025）【示意】，同機構另一版本 USD 54.2 億，差逾 100%，口徑含傢俱零售，不等於裝修市場」 | https://www.kenresearch.com/industry-reports/malaysia-furniture-and-interior-design-market | 同一機構兩版本差 >100%，依整合協議 §4 進矛盾表。查核者記憶中沒有任何馬來西亞官方「室內設計服務」產值統計；DOSM 服務業普查 MSIC 7410「專門設計」是唯一可能的 A 級來源，待查。 |
| 3 | 居家修繕市場規模 | T1 §3.7：Ken Research ≈USD 10 億（2025，材料／工具／塗料／五金／專業施工） | ❓ 無法驗證 | 維持為【示意】區間參考；與 #2 口徑不同不可相加 | https://www.kenresearch.com/industry-reports/malaysia-home-improvement-market | MR DIY Group（Bursa：MRDIY）年報引用的獨立市場研究是較可信的替代來源（泰國 Mr. DIY 上市文件已有先例，見 TH-A），下一輪優先查。 |
| 4 | DOSM 承包商口徑「室內裝潢工程產值」RM 20 億（2024） | MY-A §1.8、§2、§8（轉述 T1 前稿，**無 URL**） | ❓ 無法驗證（無 URL） | **不採用**，直到在 DOSM《Quarterly Construction Statistics》或《Annual Economic Statistics: Construction》找到原表。RM 20 億 ≈ USD 4.5 億 ≈ NT$143 億（4.40／7.16） | 候選入口：https://www.dosm.gov.my/portal-main/release-content/construction-statistics-fourth-quarter-2025 （T1）；https://www.dosm.gov.my/ | 查核者記憶：DOSM 季度建築統計依「sub-sector」拆分（residential／non-residential／civil engineering／**special trades**），「special trades」含機電、裝修等所有專業工程，年產值量級遠大於 RM 20 億；RM 20 億若存在，應是其下更細的「室內裝潢」分項或 MSIC 4330（建築物完工與裝修）普查值。定義未確認前不可與 #2、#3 比較。 |
| 5 | 住宅裝修單價 | MY-A §3：無資料；T1 §3.7：Houz「公寓全屋 RM 120–450+/ft²」（2026） | ❓ 無法驗證（先驗存疑：偏高） | 建議以區間呈現並標【示意】：一般全屋翻修 **RM 50–150/ft²**（≈RM 540–1,615/m² ≈ NT$3,900–11,600/m² ≈ NT$1.3–3.8 萬/坪）；高階／含傢俱軟裝 **RM 150–450/ft²**（≈NT$3.8–11.5 萬/坪）。Houz 的 120–450 疑為「設計＋施工＋傢俱」的高階口徑 | https://www.houz.com.my/interior-design-cost-malaysia/ ；https://zacharykhaw.com/2025/09/05/interior-design-cost-malaysia/ | 查核者記憶（D 級）：Qanvast MY、Recommend.my、iProperty 2024–2025 費用指南常見口徑為 1,000 ft² 公寓全屋 RM 40,000–100,000（即 RM 40–100/ft²）、排屋 RM 100,000–300,000；Houz 為設計公司行銷頁，下限 RM 120/ft² 已高於多數平台的中階值。單位：馬來西亞慣用 ft²，1 m² = 10.764 ft²，1 坪 = 35.58 ft²。 |
| 6 | 設計費行情 | MY-A §3：無資料；T1 §3.7：設計費占預算 5–15%（Houz） | ❓ 無法驗證 | 「設計費占工程預算 5–15%；design-and-build 公司常以『免設計費』綁施工」【示意】 | https://www.houz.com.my/interior-design-cost-malaysia/ | 查核者記憶（D 級）：LAM／MIID 對註冊室內設計師有建議收費表（百分比制），市場上多數裝修公司採設計施工合一、設計費內含於施工報價。單一行銷來源，低信心。 |
| 7 | 吉隆坡辦公室裝修成本 | MY-A §6、§7：C&W 2025／2026 吉隆坡值「未取得」；T1 §2.3、§3.7：Turner & Townsend 2026 吉隆坡 RM 6,908/m²（高階規格） | ❓ 無法驗證（T&T 值已有 URL） | 採 T&T 2026：RM 6,908/m² ≈ RM 642/ft² ≈ USD 1,570/m² ≈ USD 146/ft² ≈ NT$4.9 萬/m² ≈ NT$16.4 萬/坪（**高階規格**）；C&W 吉隆坡值仍須補 | https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026/asia-pacific （經 T1） | **定義不可比**：T&T 為高階規格、C&W 分基本／協作／高階三級、JLL 區域平均 USD 1,550/m²、Knight Frank 另一套；不可把 T&T 高階值與 TW-A 的 C&W 台北 USD 61／110／202 psf 直接對比。查核者記憶（D 級）：C&W 2024–2025 版吉隆坡在亞太屬最低成本群（約 USD 60–75/ft²），遠低於 T&T 高階值，更說明口徑差異。 |
| 8 | 住宅交易量、完工、存量、屋齡、滯銷 | MY-A §3、T8：全部無資料；T1 §3.7（Ken 引用）：住宅交易總值 RM 1,082.7 億（2025） | ❓ 無法驗證 | 以 NAPIC《Property Market Report 2024》《H1 2025》為唯一 A 級來源；Ken 的 RM 1,082.7 億僅作【示意】。查核者記憶（D 級，須核對）：2024 年住宅交易約 27 萬宗、總值約 RM 1,100–1,200 億；住宅存量約 630–640 萬單位；滯銷約 2.3 萬單位（2024 年底，連續下降） | https://napic2.jpph.gov.my/ （NAPIC 官方入口，本輪未開啟）；https://www.kenresearch.com/industry-reports/malaysia-home-improvement-market | 若 Ken 的 2025 年 RM 1,082.7 億低於查核者記憶的 2024 年值，可能是口徑（僅次級市場？僅住宅分層？）或年份差異，需以 NAPIC 原表裁決。屋齡分布：DOSM Banci 2020 住屋特徵表是否含建成年份，查核者亦不確定，列結構性缺口。 |
| 9 | LAM 註冊人數：730 名 Registered ID、278 名 Graduate ID、17 家法人執業體 | MY-A §1.2、§4、§8；MY-B §1.2、§2.1、§9（皆經 T3，單源、未標日期） | ❓ 無法驗證（先驗：量級合理） | 維持，但降為「單一官方來源、未標日期、未開頁」；引用時註明擷取日期 | https://www.lam.gov.my/ （官方入口）；原引 https://www.lam.gov.my/welcome ；https://www.lam.gov.my/practices | 查核者記憶（D 級）：LAM 註冊建築師約 2,000–3,000 名，室內設計師數百名，730 的量級合理；但「17 家法人執業體」可能只計 body corporate，未含獨資／合夥的 ID 執業體，若是則「正式供給僅 17 家」的推論（MY-A §4、§7）會嚴重低估。 |
| 10 | 《建築師法 1967》（Act 117）「2015 年修正後將室內設計師納入 LAM 註冊體系」 | MY-A §1.2；MY-B §1.1、§2.1、§9（「納入年 2015」中信心） | ❓ 無法驗證（**先驗存疑**） | 建議改寫為：「室內設計師早於 2015 年即為 LAM 註冊類別；2015 年修正（Architects (Amendment) Act 2015）主要新增 Graduate Interior Designer 類別、LAM Part III（室內設計）專業考試，並明文允許註冊室內設計師設立獨資／合夥／法人執業體」——**此改寫本身亦為 D 級，須以 Act 117 原文核對** | 法規原文入口：https://lom.agc.gov.my/ （總檢察署 e-LOM，本輪未開啟）；原引 https://www.starproperty.my/news/registered-interior-designers-gain-greater-industry-recognition-and-credibility-/121482 | 查核者記憶：LAM 自 1990 年代中期（Architects (Amendment) Act 1995／1996）即登錄 Interior Designer；MIID 成立於 1992 年。StarProperty 報導標題談「獲得更高認可」，較符合「2015 年提升為完整專業註冊（含執業體）」而非「首次納入」。年份若寫錯，會影響報告對「馬來西亞管制歷史長度」的判斷。 |
| 11 | 僅 LAM 註冊室內設計師可設立室內設計顧問執業體；建築執業體允許 30% 非建築師持股，是否適用 ID 執業體未確認 | MY-B §2.1、§4.1；MY-A §9.1 | ❓ 無法驗證（先驗一致） | 維持；補充「持股限制須以 Act 117 第 7B／7C 條（室內設計執業體）及 Architects Rules 原文確認」 | https://lom.agc.gov.my/ ；原引 http://www.miid.org.my/Downloads/Practice-Notes/MIID-Practice-Notes-02-Special-Provisions-Part-I.pdf ；https://www.pam.org.my/images/notes/2019/Architect_s_Practice_16March2019.pdf | 查核者記憶（D 級）：Act 117 對建築法人執業體規定「至少 70% 股權及董事會由註冊建築師持有」，2015 年修正為室內設計執業體訂了平行條款；若屬實，台灣集團在 ID 執業體的持股上限即為 30%，與 MY-A §9.1「品牌授權＋在地 LAM 註冊事務所」的結論一致，但「30%」必須查原文。 |
| 12 | 「LAM 稱未註冊者所簽契約在法院不具效力」；Act 117 s.33(e) 冒充罪 | MY-B §2.1、§11.2；T3 | ❓ 無法驗證（**先驗存疑**） | 建議改為「未註冊者不得向法院請求室內設計／建築顧問服務之報酬（Act 117 對未註冊執業者的『不得追索費用』條款）；契約本身是否無效須以判例確認」；條號 s.33(e) 待核 | https://lom.agc.gov.my/ ；原引 https://x.com/LembagaArkitek/status/2065266904147939778 | 「契約不具效力」是 X 貼文摘要的轉述，法律上「不得追索費用」與「契約無效」是兩回事，前者對屋主有利、後者對屋主亦有風險（已付款難追回）。MY-B §11.2 已自行標註需確認，此處強化為「不可照抄」。 |
| 13 | CIDB Act 520 §25：所有承包商施工前須註冊；等級 G1–G7；室內裝潢為 B07；G7 最低實收資本 RM750,000；住宅小額工程無豁免 | MY-A §1.4、§4、§8；MY-B §1.3、§2.2、§9 | ❓ 無法驗證（先驗一致） | 維持；RM750,000 ≈ USD 170,455 ≈ NT$537 萬（4.40／7.16）。補充：**Act 520 的 RM500,000 門檻是 §34 建築業徵費（levy，0.125%）的適用下限，不是註冊豁免**；§25 註冊義務不分金額 | https://www.cidb.gov.my/ （官方入口）；https://lom.agc.gov.my/ ；原引 https://onekeybiz.com/insights/cidb-licence-foreign-contractors-malaysia-2026.html ；https://mishu.my/blog/business-licenses/cidb-category/ | 查核者記憶（D 級）：CIDB 各級最低實收資本 G1 RM5,000／G2 25,000／G3 50,000／G4 150,000／G5 250,000／G6 500,000／G7 750,000；合約上限 G1 ≤RM200,000、G2 ≤500,000、G3 ≤1,000,000、G4 ≤3,000,000、G5 ≤5,000,000、G6 ≤10,000,000、G7 無上限。對散戶住宅裝修業者而言，G1–G3 才是常態門檻，報告只提 G7 會誤導「進入門檻 RM750,000」。MY-B §2.2 對「RM500,000 以下」的疑問應以 levy 條款解釋。 |
| 14 | 外資 >30% 即「外國承包商」須逐案註冊；本地承包商本地持股 ≥70%；2023-02-01 新制 | MY-A §1.4、§8（高信心）；MY-B §1.4、§2.2、§4.2 | ❓ 無法驗證（先驗一致） | 維持；補充「外國承包商逐案註冊之證書（Perakuan Pendaftaran Sementara）效期以專案為限；本地註冊公司若外資 ≤30% 可申請一般 G 級註冊」 | https://www.cidb.gov.my/ ；原引 https://conventuslaw.com/report/participation-of-foreign-contractors-in/ ；https://wmlaw.com.my/2023/05/15/new-cidb-regimes-for-foreign-contractors/ | 查核者記憶與主張一致，但「2023-02-01」生效日僅來自 WM Law 一篇律所文章，CIDB 原始通函未見；兩筆記給「高信心」偏樂觀，建議中信心。土著（Bumiputera）持股：查核者記憶（D 級）私人工程無土著持股要求，政府工程須另向 PKK／UPKJ 登記取得土著地位——MY-B §4.2 列為缺口，方向正確。 |
| 15 | CIDB 住宅建造／裝修投訴：年均約 600 件；2024 年 564 件（違約 130、品質不良 86） | MY-A §1.5、§3、§8；MY-B §1.5、§3、§9（皆引 Malay Mail 2025-11-20，單源） | ❓ 無法驗證 | 維持，標「單一媒體來源（CIDB 發言）、含自建住宅」 | 原引 https://malaymail.com/news/malaysia/2025/11/20/cidb-logs-average-600-complaints-yearly-on-house-construction-renovation-issues/199136 | 兩筆記「高信心」實為單源；依整合協議 §4 應為低信心【示意】，除非找到 CIDB 年報或 BERNAMA 同一記者會的第二來源。130＋86 = 216，其餘 348 件類別未說明，不可把 564 全算作裝修糾紛。 |
| 16 | LAM 2024 年警告未註冊事務所激增；2026 年 General Circular No. 1/2026；稽查「數百則廣告僅 1 家確認註冊」 | MY-A §1.3、§4、§8（中信心）；MY-B §1.6、§2.4、§9（低信心） | ❓ 無法驗證 | 維持事件，但「僅 1 家」改標「LAM 於社群平台之說法，低信心」；兩筆記信心等級應統一為低 | 原引 https://www.bernama.com/en/news.php?id=2325910 ；https://x.com/LembagaArkitek/status/2065266904147939778 | X 貼文 ID（2065266904147939778）量級對應 2026 年，年份合理。「數百則廣告僅 1 家註冊」是稽查抽樣，不是市場統計，MY-A §4 Inferences 以此推論「絕大多數 ID 公司未註冊」屬合理但仍需 SSM／LAM 名錄比對。 |
| 17 | 消費者保護：無法定裝修保固、無訂金上限、無標準契約；救濟為 CIDB 投訴與消費者申訴仲裁庭 | MY-B §1.5、§3、§10.4；MY-A §3 | ❓ 無法驗證（先驗一致） | 維持「無裝修專法」；補充（D 級待核）：消費者申訴仲裁庭（Tribunal Tuntutan Pengguna Malaysia, TTPM）依《消費者保護法 1999》（Act 599）設立，**管轄金額上限 RM50,000**（≈USD 11,400 ≈ NT$36 萬），申請費 RM5，適用於個人／家庭用途之服務（住宅裝修屬之）；Act 599 Part IX 對服務有「合理注意與技能」之默示保證，可作為無專法下的保固依據 | https://ttpm.kpdn.gov.my/ （TTPM 官方入口，本輪未開啟）；https://lom.agc.gov.my/ ；原引 https://nglaw.com.my/renovation-nightmare-a-homeowners-guide-to-legal-claims-against-contractors-panduan-undang-undang-pemilik-rumah-terhadap-kontraktor/ | MY-B §10.4「消費者保護真空」說法過強：Act 599 的默示保證與 TTPM 低成本救濟是實質存在的消費者保護，只是沒有「裝修專用」規範。報告措辭應改為「無裝修專法，但一般消保法適用」。 |
| 18 | 住宅裝修許可：地方政府（PBT）許可、分層地契 JMB／MC 同意——細節全空 | MY-B §2.3、§11.1、§11.3 | ❓ 無法驗證（缺口確認） | 補法源（D 級待核）：(1) 《街道、排水與建築法 1974》（Act 133）§70 及《統一建築附例 1984》（UBBL）——涉結構／外觀之改建須由 Principal Submitting Person 提交圖說經 PBT 核准；非結構之室內改裝向 PBT 申請小型工程許可（DBKL：Permit Kerja Kecil／Permit Ubah Suai）；(2) 《分層管理法 2013》（Act 757）§32 附則與《分層管理（維護與管理）條例 2015》第三附表：裝修須事先取得 JMB／MC 書面同意並繳交可退還裝修押金，金額由各管理機構訂定；(3) 《消防法 1988》（Act 341）——商業空間涉消防系統須經 Bomba 核准 | https://lom.agc.gov.my/ ；https://www.dbkl.gov.my/ ；https://www.kpkt.gov.my/ （皆官方入口，本輪未開啟） | 與 MY-B §11.3 的 D 級線索一致；本次仍無法升級。對台灣業者的實務意義：公寓裝修的「JMB／MC 押金＋工時限制」是最常見的進場摩擦，應列為報告法規要點。 |
| 19 | Livspace × IKEA 馬來西亞店中店（Damansara、Cheras）；Livspace FY25 營收 Rs 1,460 crore（+23%）、淨損 Rs 242 crore；印度 85%／新加坡 15%；「退出馬來西亞」未證實 | MY-A §1.6、§4、§8；MY-B §4.3；T2 | ❓ 無法驗證（算術確認） | 維持；算術複核：Rs 1,460 crore ÷ 86 = USD 1.698 億 ✓；Rs 242 crore ÷ 86 = USD 2,814 萬 ✓；淨損率 242/1,460 = 16.6% ✓；新加坡 15% ≈ Rs 219 crore ≈ USD 2,550 萬 ✓（T2）；FY24→FY25 淨損 416→242 = −41.8% ✓（Entrackr「42%」）。Inc42 的「−43% 至 243 crore」隱含 FY24 基期 ≈426 crore，與 T2 所列 461.7 crore 不符，T2 §矛盾表已註記 | 原引 https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863 ；https://inc42.com/buzz/livspaces-fy25-loss-declines-43-to-inr-243-cr/ ；https://edgeprop.sg/property-news/ikea-and-livspace-offer-interior-design-solutions-kuala-lumpur-outlets | 查核者對 Livspace 馬來西亞現況同樣無可靠記憶；EdgeProp 報導未標年份，查核者記憶 Livspace 於 2021 年前後隨 Qanvast 併購進入馬來西亞（D 級）。最終報告應只寫「曾設店中店、現況不明」，不得暗示仍在營運或已退出。 |
| 20 | 匯率假設 | MY-A：USD/MYR 4.20、USD/TWD 31.5（RM1 ≈ NT$7.50）；MY-B：4.40、32.0（RM1 ≈ NT$7.27）；T1／T8：4.40、31.5（RM1 ≈ NT$7.16） | ✏️ 修正（內部矛盾） | 同一工作階段對 RM→NT$ 出現 **7.50／7.27／7.16 三個換算值（極差 4.7%）**；V1 整合統一採 T1 慣例 4.40／31.5，並於定稿以 BNM 當日中間價覆寫 | https://www.bnm.gov.my/exchange-rates （官方入口） | 查核者記憶（D 級）：令吉 2025 年已升值至約 4.2 水準，4.40 可能偏弱；但統一性優先於精確性，覆寫時全檔一次處理。 |
| 21 | CIDB G7 實收資本的美元值 | MY-A：USD 178,600／NT$563 萬；MY-B／T3：USD 170,455／NT$545 萬 | ✏️ 修正（同一 RM 數字兩個美元值） | 統一為 RM750,000 ≈ USD 170,455 ≈ NT$537 萬（4.40／7.16）；兩筆記算術各自正確（750,000/4.20 = 178,571；/4.40 = 170,455），差異純由匯率造成 | — | 若報告同時引用兩筆記的美元值，讀者會以為是兩個不同門檻。 |
| 22 | Livspace FY25 營收的新台幣值 | MY-A：NT$53.6 億（31.5）；T2：NT$52.6 億（31.0）；MY-B 未換算 | ✏️ 修正 | 統一為 USD 1.698 億 × 31.5 ≈ **NT$53.5 億**；淨損 ≈ NT$8.9 億 | — | T2 用 USD/TWD 31.0、MY-A 用 31.5、MY-B 用 32.0，同一公司三個台幣值。 |

---

## (b) 內部矛盾與定義問題

1. **MY-A「零市場數字」與 T1 §3.7 的矛盾（最重要）**：MY-A §2 宣稱本工作階段沒有任何附 URL 的馬來西亞市場規模來源，但 T1 §3.7 載有 Ken Research 兩個市場數字、6Wresearch 成長率、Houz 單價與設計費、T&T 吉隆坡 fit-out 成本及 DOSM 頁面 URL。時間戳顯示 T1 在 MY-A 存檔後 3 分鐘才更新，屬流程時序問題；整合時必須以 T1 §3.7 覆蓋 MY-A §2、§3、§6 的「無資料」，並把 MY-A §10 缺口表對應項目改為「有 C 級示意值，待驗證」。
2. **三套匯率（RM1 = NT$7.50／7.27／7.16）**：MY-A、MY-B、T1 各自不同，導致 G7 資本額、Livspace 營收等同一數字在不同筆記出現 3–5% 的差異（#20–#22）。
3. **Ken Research 同一報告兩個數字（USD 24.3 億 vs 54.2 億）**：T1 已註記；差逾 100%，依協議 §4 不得取平均，應查兩版本的基準年與口徑（是否一版含出口傢俱製造）。
4. **市場規模口徑不可比／不可加**：Ken「傢俱＋室內設計」（含家飾零售）、Ken「居家修繕」（材料＋施工）、DOSM「室內裝潢工程產值」（承包商產值）、6Wresearch「室內設計」（僅成長率）是四個不同口徑；MY-A §7 的「住宅翻修市場規模 ÷ GDP」若用 Ken 的傢俱口徑計算，會與台灣的「裝修產值 NT$5,500 億」口徑錯配。
5. **商辦 fit-out 成本口徑**：T&T 2026 吉隆坡 RM 6,908/m² 是高階規格；MY-A §7 對台灣的錨點是 C&W 三級（USD 61／110／202 psf）。兩者不可直接相比；最終報告應等 C&W 吉隆坡值，或同時取 T&T 台北高階值作同口徑比較。
6. **「17 家法人執業體」的定義**：若 LAM Practices 頁只列 body corporate，則獨資／合夥的 ID 執業體未計入，MY-A §4、§7「執業體 17 vs 台灣 1.7 萬」的對比會誇大差距（台灣 1.7 萬家含所有登記形態）。需確認 LAM 頁面的分類。
7. **CIDB 投訴信心等級**：兩筆記與 T3 均給「高」，但只有 Malay Mail 一篇；且 564 件中僅 216 件有類別說明，其餘 348 件性質不明。應降為單源【示意】。
8. **LAM 稽查「僅 1 家註冊」信心等級不一**：MY-A 中、MY-B 低、T3 未標；應統一為低（社群貼文、抽樣說法）。
9. **Act 117「2015 年納入室內設計師」**：兩筆記與 T3 一致，但一致性來自同一搜尋摘要（StarProperty），不構成雙源；查核者先驗認為室內設計師註冊早於 2015（見 #10）。若最終報告據此寫「馬來西亞 2015 年才開始管制室內設計」，有錯誤風險。
10. **「RM500,000 以下是否豁免 CIDB 註冊」**：MY-B §2.2 列為未查證；查核者先驗認為 RM500,000 是 Act 520 §34 徵費門檻而非註冊豁免，兩者混淆會導致「小案不必註冊」的錯誤結論（見 #13）。
11. **「消費者保護真空」措辭**：MY-B §10.4 稱無法定保固／訂金上限／標準契約，推論為「真空」；但《消費者保護法 1999》的服務默示保證與 TTPM（RM50,000 上限）實際適用於住宅裝修，應改寫為「無裝修專法、一般消保法適用」（見 #17）。
12. **小型不一致**：Ng Law Firm 指南 MY-A 寫「雙語（英／馬）」、MY-B 寫「中英馬三語」；Livspace 裁員人數 Entrackr「逾 1,000 人」vs HRKatha「約 100 人、不到 2%」（T2 已列矛盾，兩筆記照抄未裁決）；MY-B §1.7 提到乃村工藝社馬來西亞據點來自日本 EDINET 沿革（TW-B S34），屬商業空間導向，與住宅裝修市場關聯弱，不宜作為「外資進入案例」的證據。

---

## (c) 整體評估

- **證據基礎**：兩份筆記自承 0 次搜尋、所有 URL 來自 T2／T3 搜尋摘要且未開頁；本次查核同樣 0 次搜尋。因此馬來西亞是目前 12 市場中**唯一完全沒有任何經獨立查核數字**的市場。依整合協議 §3，兩份筆記的所有數字在 V1 只能標【示意】；§2 分級上，LAM／CIDB／DOSM 來源雖屬 A 級機構，但「未開頁」使其實際可用等級不高於 C。
- **分析師自律良好**：兩位分析師沒有編造任何數字，缺口全部明示並附可執行搜尋計畫，附錄 A／B 與 §11.3 的 D 級線索方向與查核者先驗知識大致一致；這是本輪少數可稱讚之處。
- **主要風險**：(1) MY-A 未納入 T1 §3.7 已有的市場數字，整合者若只讀 MY-A 會誤以為全無資料；(2) 三套匯率；(3) 法規敘述中有兩處先驗存疑（室內設計師納入年份、「契約無效」說法）與一處易誤導（只提 G7 門檻、RM500,000 疑為豁免）；(4) 單源數字（LAM 註冊數、CIDB 投訴）被給予中高信心。
- **整體品質：低**（資料完整度低；法規骨架方向正確但未經核對；市場數字為零或 C 級）。
- **下一輪優先順序**：先跑附一的 15 條查核搜尋（法規原文與官方統計），再跑兩筆記附錄 B 的 20 條研究搜尋；兩輪合計約 35 次搜尋即可把馬來西亞提升到與日本、台灣相當的驗證水準。

---

## (d) 建議採用值（最終報告 headline numbers）

> 所有值在下一輪開頁核對前一律標【示意】；「信心」欄為查核者對「下一輪核對後大致成立」的主觀機率，不是來源等級。

| 指標 | 建議值 | 年份 | 來源／URL | 信心 | 備註 |
|---|---|---|---|---|---|
| 匯率 | USD/MYR 4.40；USD/TWD 31.5；RM1 ≈ NT$7.16 | 2025–2026 參考值 | T1 慣例；定稿以 https://www.bnm.gov.my/exchange-rates 覆寫 | 中（統一性） | 令吉 2025 年起升值，4.40 可能偏弱 |
| 室內設計＋傢俱市場（Ken 口徑） | USD 24.3 億 ≈ RM 107 億 ≈ NT$765 億（區間：同機構另版 54.2 億） | 2025 | https://www.kenresearch.com/industry-reports/malaysia-furniture-and-interior-design-market | 低 | 含傢俱／家飾零售，**非裝修市場**；只作上限參考 |
| 居家修繕市場（Ken 口徑） | ≈USD 10 億 ≈ RM 44 億 ≈ NT$315 億 | 2025 | https://www.kenresearch.com/industry-reports/malaysia-home-improvement-market | 低 | 材料＋工具＋專業施工；優先以 MR DIY 年報引用的市場研究取代 |
| 室內裝潢工程產值（DOSM 承包商口徑） | RM 20 億（≈USD 4.5 億）——**暫不採用** | 2024 | 無 URL；候選 https://www.dosm.gov.my/portal-main/release-content/construction-statistics-fourth-quarter-2025 | 極低 | 找到原表並確認定義前不得進入報告正文 |
| 室內設計市場成長率 | 5.8% | 2025（6Wresearch） | https://www.6wresearch.com/industry-report/malaysia-interior-design-market-outlook | 低 | 市調公司，無基期數值 |
| 住宅全屋翻修單價 | 一般 RM 50–150/ft²（≈NT$1.3–3.8 萬/坪）；高階／含軟裝 RM 150–450/ft²（≈NT$3.8–11.5 萬/坪） | 2025–2026 | https://www.houz.com.my/interior-design-cost-malaysia/ ；https://zacharykhaw.com/2025/09/05/interior-design-cost-malaysia/ ；下限區間為查核者 D 級補充 | 低 | 台灣新成屋 6–10 萬/坪 ≈ RM 235–393/ft²，馬來西亞中階約為台灣 1/3 |
| 設計費 | 工程預算 5–15%；design-and-build 常「免設計費」 | 2026 | https://www.houz.com.my/interior-design-cost-malaysia/ | 低 | 單一行銷來源 |
| 吉隆坡辦公室 fit-out（高階規格） | RM 6,908/m² ≈ USD 1,570/m² ≈ USD 146/ft² ≈ NT$16.4 萬/坪 | 2026 | https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026/asia-pacific | 中 | T&T 高階口徑；C&W 三級值待補 |
| 住宅交易總值 | RM 1,082.7 億（Ken 引用）；NAPIC 原值待補 | 2025 | https://www.kenresearch.com/industry-reports/malaysia-home-improvement-market ；https://napic2.jpph.gov.my/ | 低 | 查核者記憶 2024 年約 27 萬宗、RM 1,100–1,200 億（D 級） |
| 住宅存量／滯銷 | 存量 ≈630–640 萬單位；滯銷 ≈2.3 萬單位 | 2024 | https://napic2.jpph.gov.my/ （待開啟） | 極低（D 級記憶） | 僅供下一輪定位 |
| 人口 | ≈34.1 百萬 | 2025 | https://www.dosm.gov.my/ （T8） | 中 | T8 標未驗證 |
| LAM 註冊室內設計師／畢業室內設計師／法人執業體 | 730／278／17 | 擷取日未標（2026） | https://www.lam.gov.my/welcome ；https://www.lam.gov.my/practices | 中低 | 單源；「17 家」可能僅計 body corporate |
| CIDB 住宅建造／裝修投訴 | 年均 ≈600 件；2024 年 564 件（違約 130、品質 86） | 2024 | https://malaymail.com/news/malaysia/2025/11/20/cidb-logs-average-600-complaints-yearly-on-house-construction-renovation-issues/199136 | 中低 | 單源；含自建住宅 |
| CIDB G7 最低實收資本 | RM750,000 ≈ USD 170,455 ≈ NT$537 萬 | 現行 | https://www.cidb.gov.my/ ；原引 https://onekeybiz.com/insights/cidb-licence-foreign-contractors-malaysia-2026.html | 中 | 並列 G1–G3 門檻（RM5,000–50,000）以免誤導 |
| 消費者申訴仲裁庭管轄上限 | RM50,000 ≈ USD 11,400 ≈ NT$36 萬 | 現行 | https://ttpm.kpdn.gov.my/ （待開啟） | 中（D 級記憶） | Consumer Protection Act 1999（Act 599） |
| Livspace 集團（唯一跨國連鎖參照） | FY25 營收 Rs 1,460 crore ≈ USD 1.70 億 ≈ NT$53.5 億；淨損率 −16.6%；馬來西亞分項未揭露 | FY25 | https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863 | 中高（三源一致，但同為印度媒體轉述財報） | 馬來西亞現況不明 |

---

## (e) 法規要點確認

> 狀態欄：「待核」＝本次無獨立證據；「先驗一致」＝查核者記憶與分析師主張方向一致；「先驗存疑」＝查核者記憶與主張不同，必須以原文裁決。所有 URL 為官方入口或分析師原引，**本輪皆未開啟**。

| 要點 | 內容（最終報告建議措辭） | 法源／主管機關 | URL | 狀態 |
|---|---|---|---|---|
| 室內設計為法定管制專業 | 依《建築師法 1967》（Act 117），只有 LAM 註冊室內設計師（Interior Designer）可提供室內設計顧問服務並設立室內設計執業體；畢業室內設計師（Graduate ID）須通過 LAM Part III 考試方可成為註冊 ID | Architects Act 1967（Act 117）；Lembaga Arkitek Malaysia（LAM，工務部） | https://lom.agc.gov.my/ ；https://www.lam.gov.my/ ；https://www.lam.gov.my/menuRecognisedId | 先驗一致 |
| 室內設計師納入年份 | 建議寫「室內設計師自 1990 年代中期起即由 LAM 登錄；2015 年修正擴充為 Graduate ID／Part III／執業體制度」而非「2015 年納入」 | Architects (Amendment) Act 2015 | https://lom.agc.gov.my/ | **先驗存疑**（兩筆記寫 2015 納入） |
| 室內設計執業體外資／非專業持股 | 執業體須由註冊 ID 設立；建築執業體對非建築師持股上限 30%，室內設計執業體是否有平行條款待核；台灣集團最可能的合法結構為「本地註冊 ID 持股 ≥70% 的執業體＋品牌授權」 | Act 117 執業體條款；Architects Rules | https://lom.agc.gov.my/ ；https://www.pam.org.my/images/notes/2019/Architect_s_Practice_16March2019.pdf | 待核 |
| 未註冊執業之法律效果 | 未註冊者冒充註冊 ID 構成犯罪；未註冊者不得向法院請求顧問服務報酬；「契約無效」之說法未經條文或判例確認，不得照抄 | Act 117 罰則與費用追索條款 | https://lom.agc.gov.my/ ；https://x.com/LembagaArkitek/status/2065266904147939778 | **先驗存疑**（「契約無效」） |
| 施工承包商強制註冊 | 任何承包商（含外國）執行建築工程（含翻修、裝修）前須向 CIDB 註冊並持有效證書；分級 G1–G7（合約上限 RM20 萬至無上限）；室內裝潢專業類別 B07；**無小額豁免**，RM500,000 為徵費門檻（§34）而非註冊豁免 | Lembaga Pembangunan Industri Pembinaan Malaysia Act 1994（Act 520）§25、§34；CIDB | https://lom.agc.gov.my/ ；https://www.cidb.gov.my/ | 先驗一致（豁免問題為先驗補充） |
| 工地人員登記 | 所有工地人員須持 CIDB Green Card（Act 520 §33）；是否實際適用於室內裝修工班待核 | Act 520 §33 | https://www.cidb.gov.my/ | 待核 |
| 外國承包商 | 外資 >30% 之公司為「外國承包商」，採逐案（專案）註冊，證書效期以專案為限；本地註冊且外資 ≤30% 可申請一般 G 級註冊；私人工程無土著持股要求，政府工程須另向 PKK 登記 | CIDB 外國承包商註冊指引（2023-02-01 新制） | https://www.cidb.gov.my/ ；https://wmlaw.com.my/2023/05/15/new-cidb-regimes-for-foreign-contractors/ ；https://conventuslaw.com/report/participation-of-foreign-contractors-in/ | 先驗一致；生效日單源 |
| 公司設立 | 外資可 100% 持有 Sdn. Bhd.（SSM 登記），但從事室內設計顧問須另有 LAM 執業體登錄、從事施工須 CIDB 註冊——公司法層面的開放不等於專業法層面的開放 | Companies Act 2016；SSM | https://www.ssm.com.my/ ；https://accountingmalaysia.com/guides/set-up-company-malaysia-foreigner/ | 先驗一致 |
| 外籍專業人員簽證 | Employment Pass 由移民局 Expatriate Services Division（ESD）核發，分三類（查核者記憶：Cat I 月薪 ≥RM10,000；Cat II RM5,000–9,999；Cat III RM3,000–4,999，D 級） | Immigration Department／ESD | https://esd.imi.gov.my/ | 待核 |
| 住宅裝修許可（有地住宅） | 涉結構／外觀變更須經 PBT 核准圖說（Principal Submitting Person 提交）；非結構內裝向 PBT 申請小型工程／裝修許可（DBKL：Permit Kerja Kecil／Ubah Suai） | Street, Drainage and Building Act 1974（Act 133）§70；Uniform Building By-Laws 1984；各 PBT | https://lom.agc.gov.my/ ；https://www.dbkl.gov.my/ | 待核 |
| 住宅裝修許可（分層／公寓） | 裝修須事先取得 JMB／MC 書面同意、繳交可退還裝修押金並遵守工時與垃圾清運附則；押金金額由各管理機構依附則訂定 | Strata Management Act 2013（Act 757）§32；Strata Management (Maintenance and Management) Regulations 2015 第三附表；Commissioner of Buildings（各 PBT） | https://lom.agc.gov.my/ ；https://www.kpkt.gov.my/ | 待核 |
| 商業空間消防 | 涉消防系統或逃生路徑之商業裝修須經 Bomba 核准 | Fire Services Act 1988（Act 341）；UBBL 第七、八部 | https://www.bomba.gov.my/ | 待核 |
| 消費者保護 | 無裝修專法、無法定保固期、無訂金上限、無法定標準契約；但《消費者保護法 1999》對服務有默示保證，消費者可向消費者申訴仲裁庭（TTPM）提出 ≤RM50,000 之申訴（申請費 RM5），亦可向 CIDB 投訴承包商或提民事訴訟 | Consumer Protection Act 1999（Act 599）Part IX、Part XII；TTPM（KPDN） | https://ttpm.kpdn.gov.my/ ；https://lom.agc.gov.my/ ；https://nglaw.com.my/renovation-nightmare-a-homeowners-guide-to-legal-claims-against-contractors-panduan-undang-undang-pemilik-rumah-terhadap-kontraktor/ | 先驗一致（上限金額待核） |
| 稅務（商辦裝修） | 查核者記憶（D 級）：2025-07-01 起服務稅擴大至建築工程服務，稅率 6%，年營業額門檻 RM150 萬，住宅建築及其公共設施之工程豁免——對商業空間 fit-out 報價影響直接，對住宅裝修影響有限；須以關稅局 MySST 公告核對 | Service Tax Act 2018 及 2025 年修正條例；Royal Malaysian Customs Department | https://mysst.customs.gov.my/ | 待核（兩筆記列為缺口） |
| 2023–2026 執法趨勢 | LAM 2024 年公開警告未註冊事務所激增；2026 年 General Circular No. 1/2026 要求推廣平台配合稽查未註冊室內設計服務 | LAM | https://www.bernama.com/en/news.php?id=2325910 ；https://x.com/LembagaArkitek/status/2065266904147939778 | 待核（事件可信、「僅 1 家」為抽樣說法） |

---

## 附一：本次規劃但未能執行的 15 條獨立查核搜尋（下一輪請直接續跑）

1. `Lembaga Arkitek Malaysia bilangan pereka dalaman berdaftar statistik pendaftaran 2025`（#9）
2. `Akta Arkitek 1967 pindaan 2015 pereka dalaman berdaftar badan korporat amalan pereka dalaman`（#10、#11）
3. `CIDB gred G7 modal berbayar RM750,000 syarat pendaftaran kontraktor B07 hiasan dalaman`（#13）
4. `kontraktor asing CIDB ekuiti tempatan 70% pendaftaran projek 1 Februari 2023 pekeliling`（#14）
5. `CIDB aduan pembinaan ubah suai rumah 2024 564 aduan pelanggaran kontrak kualiti`（#15）
6. `LAM pekeliling am 1/2026 platform pereka dalaman tidak berdaftar penguatkuasaan`（#16）
7. `Livspace Malaysia IKEA Cheras Damansara design studio closed 2024 2025`（#19）
8. `Malaysia interior design market size 2025 USD million CAGR Statista Mordor IMARC`（#2）
9. `kos renovasi rumah 2025 sekaki persegi kondominium teres Qanvast Recommend.my`（#5）
10. `yuran pereka dalaman Malaysia peratus kos projek LAM skala fi reka bentuk dalaman`（#6）
11. `NAPIC laporan pasaran harta 2024 transaksi kediaman unit nilai stok lebihan`（#8）
12. `Tribunal Tuntutan Pengguna had RM50,000 kontraktor ubah suai rumah tuntutan`（#17）
13. `permit ubah suai rumah DBKL deposit renovasi JMB MC peraturan pengurusan strata 2015 jadual ketiga`（#18）
14. `Kuala Lumpur office fit-out cost per sq ft 2025 2026 Cushman Wakefield guide`（#7）
15. `cukai perkhidmatan 6% kerja pembinaan 1 Julai 2025 pengecualian bangunan kediaman ambang RM1.5 juta`（稅務）

另保留 2 次額度給 DOSM「室內裝潢」分項（#4）與 Ken Research 兩版本矛盾（#2）。

## 附二：本次使用的本地交叉來源（非獨立證據）

- `themes/T1-market-size-reconciliation.md` §2.3、§3.7（馬來西亞市場數字與 T&T 吉隆坡值；17:13 更新）
- `themes/T2-business-models.md` §4、§8、§11（Livspace／Qanvast 數字與矛盾表）
- `themes/T3-regulation-licensing.md` 馬來西亞各列（兩筆記法規主張之共同上游）
- `themes/T8-housing-demographics-demand.md` 馬來西亞列（人口、家戶、高齡化，全標未驗證）
- `countries/SG-A-market.md`、`countries/TW-B-rules.md`、`countries/VN-B-rules.md`（Qanvast、乃村工藝社、木材／磁磚／玻璃片段）
- `02-integration-protocol.md`（分級與三角驗證規則）
