# T4 數位平台、AI 設計工具與科技應用（Digital platforms, AI design tools and technology adoption）

> **版本與方法說明（請整合者先讀）**
> 1. 本版（2026-10-09）以 22 次 WebSearch 重寫前一版（2026-10-08，該版因搜尋額度被用罄而完全依賴既有筆記的「繼承資料」）。本版**保留前版結構**，並將來源分為兩類：「本輪搜得」＝本回合搜尋結果摘要所列的 URL；「繼承」＝沿用前版（經由 T1／T2／T3／CN／KR／JP／TW／VN／ID／MY 筆記）的 URL。WebFetch／curl 在本環境被封鎖，**所有 URL 均未逐頁開啟核對原文**，引用層級為搜尋結果摘要，整合時請由查核代理開頁驗證。
> 2. 任務指定但本輪仍無資料者（例：집닥 2025 累計交易額、Hometrust、Renopedia、Decor8、幸福空間／設計家 2025 數據、Homestyler／Planner 5D／D5 Render 用戶數、三翼鳥 2025 全年、台灣系統櫃市占、各市場 CPL 基準、Samsung SmartThings／LIXIL／Panasonic 綁裝修率）一律列入 §12 資料缺口，**本筆記沒有任何估計值**；少數「本人推算」皆標明算式。
> 3. 匯率（統一採用）：USD 1 = TWD 31.5 = CNY 7.2 = KRW 1,400 = JPY 150 = INR 86 = SGD 1.35 = HKD 7.8 = MYR 4.4 = THB 33 = VND 25,500 = IDR 16,200 = PHP 57（2025–2026 概略水準；整合時以 V2 統一匯率表覆寫）。
> 4. 信心等級：高＝上市公司財報／招股書／政府／法規；中高／中＝券商首次覆蓋、協會、主流財經媒體引用原始數據；中低／低＝平台自報、市調機構新聞稿、比較網站、未附方法論之估計。

---

## 1. 摘要

1. **亞洲室內裝修數位化呈三種成熟度**：中國與韓國已走完「內容社群→電商→施工媒合→履約保障」循環，並各自出現可公開比較財務的標竿——群核科技／酷家樂（Manycore／Kujiale，00068.HK，2026-04 港交所上市；2025 年營收 8.20–8.29 億元人民幣、企業付費客戶 47,416 家、MAU 約 250 萬、毛利率 82.2%、經調整淨利 5,712.7 萬元）與 오늘의집（Bucketplace；2025 年營收 3,215 億韓元、施工累計交易額 2024 年破 1 兆韓元、但 2025 年營業損失 147 億韓元）；台灣、新加坡、印度、印尼、香港處於「媒合平台＋全包連鎖」階段（100室內設計月訪 200 萬、1,400 家設計公司；Qanvast 自報累計服務 7 萬屋主、訂閱制不抽佣；HomeLane FY25 營收 Rs 747.8 crore、Livspace Rs 1,460 crore；Dekoruma 2024 年以 Rp 1.16 兆售予 Blibli；裝修佬 DecoMan 估值 HK$1.5 億）；日本、越南、泰國、馬來西亞、菲律賓的平台公開數據最薄，且泰國 SCG 系 NocNoc 於 2020–2024 連年虧損後宣布結束服務。
2. **設計 SaaS 是本主題唯一被證明「可上市、高毛利」的科技層**：酷家樂每家企業年均訂閱 1.41 萬元人民幣（≈USD 1,958／TWD 6.2 萬）、大客戶 ARPU 85.6 萬元，45.4% 新企業客戶先用免費／個人版再轉企業訂閱（PLG 模式）；但收入成長已放緩至 8.6%，空間智能新業務僅占 0.6%。全球性調查顯示設計師 AI 使用率落在 31%（Houzz 美國，722 家）到 82%（Mattoboard，328 人／70 國）之間，主要用途是「加速」而非「創意」，生產力數字皆為自報；**12 市場中仍無任何一國的本地設計師 AI 採用率調查**。印度 HomeLane 稱 AI 把設計方案產出由數日縮至數分鐘、設計成本降約 25%；Livspace 2026-02 以「AI 導入」為由裁員約 1,000 人（12%）。
3. **BIM 強制令正在到達但尚未觸及室內裝修**：新加坡 CORENET X 依 2025-01 修訂時程於 2025-10-01 起對 GFA ≥30,000 ㎡ 新案強制、2026-10-01 擴及所有新案、2027-10-01 納入進行中案件，BIM（IFC-SG）要求適用新建或新增 GFA ≥5,000 ㎡ 之重大增改建；香港 2025-04-01 起公共工程招標文件強制 BIM（DEVB TC(W) 1/2025），私人圖則 BIM 路線圖仍在諮詢、業界提及 2029 年目標；日本施工管理 SaaS ANDPAD 依比較網站達 23 萬社／68 萬用戶、連續 8 年市占第一（Deloitte Tohmatsu MIC 2025-12），但官方 2025 導入社数未取得。**沒有任何市場的 BIM 規定明文涵蓋室內裝修工程**。
4. **預製／模組化內裝只有中國有政策推力但無滲透率**：住建部 2025 年底《關於提升住房品質的意見》明列「積極發展裝配式裝修」、國務院 2026-05《城市更新「十五五」規劃》提「提升裝配式裝修應用比例」、住建部《促進裝配式裝修發展的指導意見（徵求意見稿）》擬 2030 年顯著提高並要求保障性租賃住房全面採用；市場規模各機構口徑矛盾（智研 2025 年 3,431.5 億元 vs 同機構另頁 6,390 億元預測），全國滲透率無官方數字；台灣系統櫃市占、日本ユニットバス、韓國빌트인、新加坡 DfMA 室內規定本輪仍無資料。
5. **智慧家庭×裝修只在中國被規模化**：海爾三翼鳥 2024 年零售額破百億元、2024-03 首批 260 家門店入駐天貓喵店、2025-12 稱近千家品牌店「變身」；亞太智慧家庭市場規模各研究機構矛盾（USD 302 億 vs 502 億），GMI 稱 2025 年海爾、三星、LG、Amazon、小米五家合計 47% 份額；各國「翻修案綁售率」全部無資料。
6. **數位獲客的可引用證據集中在中國與韓國**：小紅書 2024 年家居家裝 GMV 年增 2.5 倍、#我的裝修記錄 183.3 億次瀏覽、2025 年 1–5 月家居種草內容月均互動逾 3 億、商業筆記 +45%、用戶「需求帖」年增 175%、逾 30 位博主單月漲粉 10 萬+、軟裝設計師單場直播 GMV 2,000 萬元；齊屹科技 2024 年每條線索 527 元人民幣且線索量年減 20%；土巴兔 COO 2025 年 12 月坦言「下半年全行業流量持續下滑」；韓國三份調查顯示 SNS／YouTube 與入口搜尋各約四成、平台約三成。新加坡／馬來西亞 Meta 廣告 CPL 基準：未找到。
7. **對台灣業者**：現在可部署且有海外 ROI 證據的是 (1) 低價 3D／AI 設計 SaaS 作簽單工具（酷家樂 USD 9.9／月起、Planner 5D USD 4.99／月起、Spacely AI 等）；(2) 在既有流量母體（100室內設計、小紅書／Instagram／YouTube）經營案例與創作者內容；(3) 履約保證／節點付款／第三方託管（오늘의집導入施工責任保障後施工交易額近倍增）。自建平台（土巴兔、齊屹、NocNoc、Dekoruma、Livspace 皆虧損或退出）與 BIM／裝配式／智慧家庭綁售（無滲透率證據）不宜作為策略投資。

---

## 2. 平台版圖：各市場主要消費者平台（用戶、GMV、募資、收入模式、2024–2026 狀態）

### 結論
12 市場中只有中國（群核、齊屹、貝殼）與韓國（오늘의집）的平台有審計財務；新加坡 Qanvast、香港裝修佬、台灣 100室內設計與 PULO、越南 Happynest 僅有自報營運數；印度以 Livspace／HomeLane 全包連鎖取代平台；區域平台正被收編或退出（Qanvast→Livspace 2022、Dekoruma→Blibli 2024、NocNoc 宣布結束服務、Fabelio 2022 破產）。日本（ホームプロ／リショップナビ／SUUMO）只有比較網站的加盟數；집닥、Hometrust、Renopedia、Decor8、Recommend.my、Atap、幸福空間、設計家、好好住 2025 年數據仍無資料。

### 引用發現

**中國大陸**
- 群核科技（Manycore Tech，00068.HK）2023／2024／2025 年營收 6.64／7.55／8.20 億元人民幣（國泰海通首次覆蓋口徑；36 氪引 8.29 億）；2025 ≈ USD 1.14 億／TWD 35.9 億；營收增速由 13.7% 放緩至 8.6%；毛利率 76.8%／80.9%／82.2%；歸母淨損 −6.46／−5.13／−4.28 億元；2025 年經調整淨利 5,712.7 萬元；國泰海通 2026-05 首次覆蓋給「增持」、目標價 HK$24.90 — [同花順／國泰海通 2026-05-22](https://stock.10jqka.com.cn/20260522/c676897096.shtml)；[格隆匯 首次覆蓋報告](https://m.gelonghui.com/news/5239188)（本輪搜得；券商，高／中高信心）。
- 群核 96.9% 收入來自「酷家樂」訂閱；企業客戶收入 6.69 億元（≈USD 9,290 萬／TWD 29.3 億，占比 >80%）；企業客戶數 2023→2025 年 41,070→47,416 家（+15%），單家企業年訂閱收入 1.37 萬→1.41 萬元（≈USD 1,958／TWD 6.2 萬，+2%）；年貢獻 ≥20 萬元大客戶 353→424 家，其 ARPU 72.9 萬→85.6 萬元（≈USD 11.9 萬／TWD 374 萬）；2025 年平均 MAU 約 250 萬；新獲企業客戶中 45.4% 先使用免費／個人版；研發支出 3.9 億→2.9 億元（營收占比 58.9%→35.5%）、銷售行銷 3.56 億→2.74 億元；空間智能業務（SpatialVerse）2025 年收入僅 520 萬元（0.6%）、客戶 16 家 — [36 氪 2026](https://www.36kr.com/p/3705744943460485)；[鈦媒體](https://www.tmtpost.com/7960361.html)；[界面](https://www.jiemian.com/article/14341537.html)；[鳳凰科技](https://tech.ifeng.com/c/8rxjRnyVj0p)（本輪搜得；年報解讀，中高信心）。
- 繼承（未重新搜尋）：群核 2026-04-17 上市、基石 37%、上市 3 個月跌回發行價；MAU 2024 年 270 萬、月活訪客 8,630 萬；個人付費 43.3 萬；NRR 企業 100.7%／個人 86.4%；海外收入約 7.4%（2024 前 9 月）— [新浪港股 2026-02-24](https://finance.sina.com.cn/stock/hkstock/hkzmt/2026-02-24/doc-inhnyyvp1282748.shtml)；[21 經濟網](https://www.21jingji.com/article/20260409/herald/4a8ab282072f3daa5bf46a36e81fe0cc.html)；[新浪科技 2026-08-07](https://finance.sina.com.cn/tech/roll/2026-08-07/doc-inimnenp3338147.shtml)；[36 氪招股書解讀](https://www.36kr.com/p/3169957639825921)。
- 互聯網家裝平台 MAU（Fastdata 2021-03 榜，為最後一次有公開排名）：齊家網 460.0 萬、好好住 281.6 萬、酷家樂 221.5 萬、土巴兔 217.7 萬；互聯網家裝平台活躍用戶 2016→2020 年 1,617 萬→3,156 萬 — [前瞻 2022-01](https://bg.qianzhan.com/trends/detail/506/220129-cdb79966.html)；[前瞻 2021-08](https://www.qianzhan.com/analyst/detail/220/210818-a123bf72.html)（本輪搜得；第三方監測，中低信心，已過時）。**2025 年土巴兔／好好住 MAU：未找到公開數據**。
- 土巴兔 COO 方浩於 2025-12 第十一屆土巴兔生態大會復盤：「下半年全行業流量持續下滑」、年初地產風險引發產業鏈連鎖反應（未給平台用戶數）— [楚天都市報 2025-12](https://www.ctdsb.net/c1734_202512/2623176.html)（本輪搜得）。
- 繼承：齊屹科技 2024 年營收 10.56 億元、線索 633,769 條（−20%）、每條均價 527 元（≈USD 73／TWD 2,306）；土巴兔 2019–2021 年銷售費用率 56–61%、2022 年撤回 IPO；貝殼家裝家居 2025 年淨收入 154 億元、貢獻利潤率 31.4%；互聯網家裝滲透率 20.8%（2023，前瞻）— [同花順 2025-04-27](https://stock.10jqka.com.cn/20250427/c667789677.shtml)；[華爾街見聞](https://wallstreetcn.com/articles/3634603)；[新浪 2026-03-16](https://finance.sina.com.cn/stock/estate/integration/2026-03-16/doc-inhrequs9902543.shtml)；[前瞻](https://www.qianzhan.com/analyst/detail/220/240428-25c71993.html)。

**韓國**
- 오늘의집（버킷플레이스）2025 年營收 3,215 億韓元（+11.7%；≈USD 2.30 億／TWD 72.3 億），創業以來首次破 3,000 億、連續 11 年兩位數成長；2025 年營業損失 147 億韓元（≈USD 1,050 萬／TWD 3.3 億；公司稱為未來成長之積極投資）；室內裝修「施工交易」營收年增 3.5 倍以上；數據依 2026-04-14 公告之 2025 年監查報告 — [데일리안 2026-04](https://www.dailian.co.kr/news/view/1633470/)（本輪搜得；審計報告轉述，高信心）。
- 2024 年營收 2,879 億韓元（≈USD 2.06 億／TWD 64.8 億）、創業 10 年首度年度獲利；導入施工責任保障與標準契約後施工交易額近倍增、累計破 1 兆韓元（≈USD 7.1 億／TWD 225 億，2024 年）— [데모데이 BM 분석](https://demoday.co.kr/bm-analysis/109)；[디지털데일리 2025-03-31](https://www.ddaily.co.kr/page/view/2025033115305138841)；[뉴데일리 2025-03-31](https://biz.newdaily.co.kr/site/data/html/2025/03/31/2025033100342.amp.html)；[The VC（버킷플레이스）](https://thevc.kr/bucketplace)（本輪搜得；中高信心）。**2025 年累計施工交易額：未公布**。
- 집닥（Zipdoc）2025 年累計交易額：本輪搜尋**未找到**；혁신의숲「직방·오늘의집·집닥 프롭테크 비교」報告為付費牆 — [혁신의숲](https://innoforest.co.kr/report/NS00000030)（本輪搜得）。繼承（低信心）：投資方部落格稱累計交易額破 3,000 億韓元 — [빅뱅엔젤스](https://blog.bigbangangels.com/zipdoc/)；[The VC](https://thevc.kr/zipdoc)。
- 繼承：아파트멘터리 2025 年營收 521.7 億韓元、2025-10 獲 LG전자 策略投資 — [The VC](https://thevc.kr/apartmentary)；[테크42](https://www.tech42.co.kr/%EC%95%84%ED%8C%8C%ED%8A%B8%EB%A9%98%ED%84%B0%EB%A6%AC-lg%EC%A0%84%EC%9E%90-%EC%A0%84%EB%9E%B5%EC%A0%81-%ED%88%AC%EC%9E%90-%EC%9C%A0%EC%B9%98-ai%EC%9C%B5%ED%95%A9-%EB%AA%B0%EC%9E%85%ED%98%95/)；2024-12-16 公正委＋소비자원＋4 平台（오늘의집、숨고、집닥、내드리오）自律協約 — [korea.kr](https://www.korea.kr/briefing/pressReleaseView.do?newsId=156665860&pWise=sub&pWiseSub=C2)。

**新加坡／馬來西亞**
- Qanvast（2013 年成立）自報「已協助逾 70,000 位新加坡、馬來西亞、香港屋主」（未標年份）；收入模式為向上架設計公司收**訂閱費、不抽佣**；Qanvast Trust Programme 提供設計公司倒閉時最高 S$50,000（≈USD 37,000／TWD 117 萬）訂金保障與爭議處理 — [Qanvast About Us（SG）](https://qanvast.com/sg/about-us)；[Qanvast About Us（MY）](https://qanvast.com/my/about-us)；[G2 Qanvast 討論](https://www.g2.com/products/qanvast/discuss)；[TODAY／Malay Mail 2024-07](https://malaymail.com/news/life/2024/07/15/to-build-your-dream-home-must-you-endure-a-nightmare-what-new-homeowners-wish-theyd-known-before-starting-renovations/143750)（本輪搜得；自報，中低信心）。
- 新加坡平台生態（2024）：老牌 Qanvast、Renonation、Renopedia，新進 HomeMatch、Ezid；Renopedia 提供裝修計算器、免費電子雜誌與檢核表；均無用戶數 — [Malay Mail／TODAY 2024](https://malaymail.com/news/life/2024/07/15/to-build-your-dream-home-must-you-endure-a-nightmare-what-new-homeowners-wish-theyd-known-before-starting-renovations/143750)；[SingSaver 平台比較](https://www.singsaver.com.sg/blog/renovation-interior-design-comparison-platforms-singapore)；[Vulcan Post](https://vulcanpost.com/522341/the-only-interior-designing-app-in-singapore-you-need-for-an-easy-renovation-journey/)（本輪搜得）。**Hometrust：搜尋結果完全未出現**。
- 繼承：Livspace 子公司 2022-04 取得 Qanvast 多數股權；新加坡占 Livspace FY25 營收 15% — [Allen & Gledhill](https://www.allenandgledhill.com/perspectives/articles/21509/acquisition-of-a-majority-stake-in-qanvast-pte-ltd-by-interiortepte-ltd)；[Entrackr](https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863)。
- 馬來西亞 Recommend.my（前身 RecomN，2014 年成立，Petaling Jaya）：居家服務與活動服務媒合，可搜尋、雇用、評價裝修承包商與室內設計師；無 2025 數據 — [Craft.co](https://craft.co/recommend-my)；Atap.co（屋主瀏覽設計師作品集並索取免費報價）最新報導為 2017–2018 年 — [Digital News Asia](https://www.digitalnewsasia.com/startup-scaleups/atapco-solves-your-renovation-problems-clever-online-tools)（本輪搜得；均無 2025 狀態）。繼承：LAM 2026 年第 1 號通函要求網路平台配合稽查未註冊 ID 業者 — [LAM（X）](https://x.com/LembagaArkitek/status/2065266904147939778)。

**台灣**
- 100室內設計（數字科技 5287）：2024-04 報導月均造訪量突破 200 萬次、1,400 家設計公司進駐、全台 1.7 萬筆案例、每年媒合 2 萬筆業主需求 — [鉅亨網／Yahoo 2024-04](https://tw.stock.yahoo.com/news/%E6%88%BF%E7%94%A2-%E6%95%B8%E5%AD%97%E7%A7%91%E6%8A%80%E6%8B%93%E5%AE%A4%E5%85%A7%E8%A8%AD%E8%A8%88%E7%89%88%E5%9C%96-%E5%B9%B3%E5%8F%B0%E6%9C%88%E8%A8%AA%E9%87%8F%E7%AA%81%E7%A0%B4200%E8%90%AC%E6%AC%A1-075452062.html)；2026-01 報導稱平台研發「精準媒合系統」以演算法比對屋主需求與設計團隊專長，並推估 2025 年裝修產值達 5,500 億元（非官方統計）— [經濟日報 2026-01](https://udn.com/news/story/7241/9245511)（本輪搜得；平台自報，中低信心）。繼承：2025 年近 15,000 筆有效需求、逾 4,000 筆簽約、App 下載 158 萬 — [NOWnews](https://www.nownews.com/news/6770793)。
- PULO 裝潢平台：App Store 自述「每 10 筆案件有 9.5 筆是統包、設計需求」、只收媒合費不抽成；無年份、無設計師人數 — [App Store 專家版](https://apps.apple.com/tw/app/pulo-%E8%A3%9D%E6%BD%A2%E5%B9%B3%E5%8F%B0-%E5%B0%88%E5%AE%B6%E7%89%88/id1266584276)；[App Store 屋主版](https://apps.apple.com/app/id1163661219)（本輪搜得；自報，低信心）。
- 設計家（Searchome）、幸福空間（hhh.com.tw）2025 年流量／媒合量／設計師數：**本輪未找到** — [幸福空間設計師頁](https://hhh.com.tw/designers/detail/2)；[LINE TODAY 平台比較](https://today.line.me/tw/v3/article/gzXWjgz)（本輪搜得，僅確認平台存在）。
- 本人推算（沿用前版）：4,000 筆簽約 × 100–150 萬元／案 ≈ 年 GMV 40–60 億元（≈USD 1.3–1.9 億），占 5,500 億的 1% 以下（低信心）。

**香港**
- 裝修佬（HK Decoman Technology）：自稱一站式 O2O 裝修平台，提供「AI 智能配對＋顧問」、網上建材商城、裝修學院；2015 年創立、2018 年完成八位數港元 Pre-A 輪、估值 HK$1.5 億（≈USD 1,920 萬／TWD 6.1 億，理大校友頁 2023 更新）；合作師傅／設計公司逾 1,500 家並進軍台灣；另有「累計交易額 HK$2 億（≈USD 2,560 萬／TWD 8.1 億）」說法但來源未標日期 — [HKTDC 一帶一路](https://beltandroad.hktdc.com/en/node/62513)；[理大校友 Benny Liu](https://www.polyu.edu.hk/alumni/featured-alumni/young-achievers/benny-liu-pui-yin/?sc_lang=en)；[INSIDE 進軍台灣](https://www.inside.com.tw/article/27152-decoman)；[鉅亨號](https://hao.cnyes.com/post/229203)（本輪搜得；自報，中低信心）。**2025 年用戶數、訂單量：未找到**；Decor8：無資料。MoneyHero 2025 年有「裝修平台比較」文但未列用戶數 — [MoneyHero](https://www.moneyhero.com.hk/blog/zh/%e8%a3%9d%e4%bf%ae%e5%85%a8%e6%94%bb%e7%95%a5-%e5%85%a8%e5%b1%8b%e8%a3%9d%e4%bf%ae%e5%a0%b1%e5%83%b9-%e8%a3%9d%e4%bf%ae%e5%b9%b3%e5%8f%b0%e6%af%94%e8%bc%83)。

**日本**
- 比較網站（2025）稱リショップナビ 加盟約 4,000 社、ホームプロ 約 1,200 社（未區分加盟／提攜，出處不明）— [crexgroup 2025](https://crexgroup.com/ja/reform/?p=1966)（本輪搜得；低信心）。ホームプロ（リクルート系）與 SUUMO 合辦之加盟店表彰活動已持續 18 年，2026 年以「ホームプロ 25 週年」之名改版為『ホームプロ&SUUMO SUCCESS MEET 2026』，表彰 2025 年度實績優良加盟店 — [PR TIMES](https://prtimes.jp/main/html/rd/p/000000005.000136710.html)；[ニッカホーム 雙料得獎](https://koubo.jp/press-release/prtimes/c74598_r329)（本輪搜得）。SUUMO カウンター リフォーム：店舖對面＋電話＋線上諮詢 — [ダイヤモンド不動産](https://diamond-fudosan.jp/articles/-/1111670)。**累計相談件數、成約件數、抽成率：未找到**。
- 繼承：生活堂為リフォーム産業新聞 2025 年網路專業第 1；LIXIL リフォームショップ 549 店、年約 12 萬件；リノベる 2025 年度「適合R住宅」410 件 — [生活堂](https://www.seikatsu-do.com/information/20251224.php)；[LIXIL PDF](https://bqzr2f-lts.origin.lixil.com/news/docs/202409_lrs-LTSebisu-open.pdf)；[リノベる PR](https://www.renoveru.jp/hubfs/%E3%80%90PRESS%20RELEASE%E3%80%91%E3%83%AA%E3%83%8E%E3%83%99%E3%82%8B%E3%80%816%E5%B9%B4%E9%80%A3%E7%B6%9A%E5%85%A8%E5%9B%BD%E3%83%BB%E9%A6%96%E9%83%BD%E5%9C%8F1%E4%BD%8D%E3%81%AE%E8%AB%8B%E8%B2%A0%E5%9E%8B%E4%BA%8B%E6%A5%AD%E8%80%85%E3%81%AB%20%E3%80%8C%E9%81%A9%E5%90%88R%E4%BD%8F%E5%AE%85%E3%80%8D%E7%99%BA%E8%A1%8C%E4%BB%B6%E6%95%B0%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0.pdf)。

**印度**
- HomeLane FY25（2024/4–2025/3）營業收入 Rs 747.8 crore（+22%；≈USD 8,700 萬／TWD 27.4 億；另一來源 Rs 756 crore）、淨損縮至 Rs 111.38 crore（≈USD 1,295 萬／TWD 4.1 億）；目標本財年營收約 Rs 1,000 crore（原訂 FY25 達成，已延後）、FY31 達 Rs 3,000 crore（≈USD 3.5 億／TWD 110 億）、兩年內 IPO；自稱「AI 驅動的家居內裝品牌」 — [D2C Insider：HomeLane targets IPO](https://pulse.d2cinsider.com/homelane-targets-ipo-within-two-years-as-ai-powered-home-interiors-brand-accelerates-expansion-and-growth/)；[D2C Insider：Rs 1,000 crore](https://pulse.d2cinsider.com/homelane-eyes-e2-82-b91000-crore-revenue-as-ai-and-category-expansion-drive-growth/)；[Inc42 HomeLane 十年](https://inc42.com/?p=566464)（本輪搜得；媒體引公司，中信心）。
- Livspace FY25 營收 Rs 1,460 crore（≈USD 1.70 億／TWD 53.5 億）、經調整 EBITDA 損失縮至約 Rs 131 crore（2025-10 報導）；2026-02 報導其半年內裁員約 1,000 人（約 12%），公司稱因「AI 導入」重組，正將 AI 代理與自動化整合進銷售、設計、營運、行銷 — [CB Insights Livspace](https://www.cbinsights.com/company/livspace)；[AI Market Watch Livspace](https://www.ai-market-watch.com/company/livspace)（本輪搜得；中信心）。繼承：Entrackr／Inc42 FY25 淨損 Rs 242 crore — [Entrackr](https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863)。

**印尼**
- Blibli（PT Global Digital Niaga, BELI）2024 年中以 IDR 1.16 兆（≈USD 7,060–7,160 萬／TWD 22.6 億）收購 PT Dekoruma Inovasi Lestari 99.83% 之 C 輪股份（26,167 股；另一來源 26,217 股），目的為強化 home & living 品類；Dekoruma 為「線上優先＋體驗中心＋自有品牌製造」混合模式，並以自家設計平台媒合屋主與設計師、協力工坊與承包商 — [IDN Financials](https://www.idnfinancials.com/news/50131/blibli-com-to-acquire-dekoruma-for-idr-1-16-trillion?sl=en)；[Endeavor Indonesia](https://indonesia.endeavor.org/?p=400259)；[CB Insights Dekoruma](https://www.cbinsights.com/investor/dekoruma)；[Techleap feed](https://finder.techleap.nl/news/feed/blibli-acquires-dekoruma-for-rp-1-16t)（本輪搜得；高／中信心）。**2025 年 Dekoruma 營運數據：未找到**。
- 繼承：Fabelio 2022-10 破產；Kanggo 月活 3.6 萬；Gravel 募 USD 1,400 萬；Sejasa 75 萬客戶 — [CNBC Indonesia](https://www.cnbcindonesia.com/tech/20221012071341-37-379004/sudah-galang-rp-300-miliar-startup-fabelio-kini-pailit)；[Investor.id](https://investor.id/business/409706/pengguna-kanggo-tembus-36-ribu-layanan-perawatan-bangunan-kian-diminati)；[Katadata](https://katadata.co.id/digital/startup/656d6becb3021/investor-amerika-suntik-startup-konstruksi-gravel-rp-216-miliar)；[Sejasa](https://www.sejasa.com/)。

**泰國**
- NocNoc（SCG 子公司 Better Be Marketplace，2019 年上線，定位「一站式居家平台」）：SCG 與 Musby（Frasers Property × ThaiBev 50/50 合資）合計投資逾 39 億泰銖（≈USD 1.18 億／TWD 37.2 億）目標五年內成東協第一 home & living 平台；第 5 年時銷售額年增 100%、累計銷售 150 億泰銖（≈USD 4.55 億／TWD 143 億）；2026-01 報導 2020–2024 年無一年獲利；另有報導宣布於 2 月 9 日起結束服務（年份摘要未顯示，推定 2026） — [ไทยรัฐ](https://www.thairath.co.th/money/tech_innovation/tech_companies/2698864)；[Marketeer](https://marketeeronline.co/archives/339473)；[ประชาชาติ 2026-01](https://www.prachachat.net/?p=1948208)；[ฐานเศรษฐกิจ](https://www.thansettakij.com/technology/648571)；[Bangkok Post](https://www.bangkokpost.com/business/general/2677164)（本輪搜得；中信心，結束服務日期須核對）。繼承：HomePro Home Service 不單獨揭露 — [SET snapshot](https://lssmedia.setlink.set.or.th/2025/3M/HMPRO-3M68-ListedCompanySnapshot-EN.html)。

**越南、菲律賓**
- 繼承：Happynest 自報月訪 400 萬、Facebook 社團 40 萬（≈2023）— [Happynest](https://v2.happynest.vn/gioi-thieu)；[Bongdaplus 2023](https://bongdaplus.vn/ben-ngoai-duong-piste/happynest-giup-hanh-trinh-lam-nha-cua-nguoi-viet-tro-nen-de-dang-hon-3981922305.html)；菲律賓 Wilcon 專案銷售 ₱347M — [Inquirer Plus](https://plus.inquirer.net/?p=256738)。本輪未另行搜尋，2025 數據缺。

### 推論
- 平台原型的審計財務只存在於中、韓；兩地共同顯示「純媒合」毛利高但線索成本吃掉利潤（齊屹）、「自營施工」拉高營收卻壓低利潤（오늘의집 2025 轉虧、施工交易營收 +3.5 倍）。
- 2024–2026 年區域平台的終局是被收編或退出：Qanvast→Livspace、Dekoruma→Blibli、NocNoc 關閉、Livspace 裁員；存活者皆依附更大的流量母體（電商、仲介、設計 SaaS）。
- 台灣、香港、新加坡平台數據全為自報且無 GMV／費率，屬 C 級，只能作區間參考。

### 缺口
- 집닥 2025 累計交易額；Hometrust、Renopedia、Decor8、幸福空間、設計家、好好住、小紅書家裝頻道、SUUMO／ホームプロ／リショップナビ 2025 年用戶／案件／GMV／費率；오늘의집／100室內設計／PULO／Qanvast 抽成率或訂閱費率；NocNoc 結束服務之確切年份與 2025 年 GMV。

---

## 3. AI 與 3D 設計工具：Coohom／酷家樂、Homestyler、Planner 5D、Spacely、SketchUp／Enscape／D5 Render、生成式 AI、AI 報價

### 結論
群核科技（酷家樂／Coohom）是唯一有完整審計數據的設計工具公司：47,416 家企業客戶、單家年均訂閱 1.41 萬元人民幣、毛利率 82.2%、45.4% 企業客戶由免費版轉化，證明「低價訂閱＋PLG」的設計 SaaS 在亞洲可達上市規模；但其收入成長已降到 8.6%，空間智能（AI）新業務僅占 0.6%。泰國 Spacely AI 以生成式 AI 渲染於 2025-07 募得 USD 100 萬、自報服務 1,500+ 事務所／50+ 國、累計 200 萬張渲染。全球性設計師調查（Mattoboard 82%／Houzz 美國 31%）顯示 AI 已普及但主要是「提速」工具且生產力數字皆自報；印度 HomeLane 稱 AI 使設計成本降約 25%、Livspace 以 AI 為由裁員 12%。**12 市場仍無任何本地設計師 AI／3D 採用率調查，Homestyler／Planner 5D／D5 Render 在亞洲的用戶數亦無資料**；第三方比價網站的定價（Coohom USD 9.90／月起、Planner 5D USD 4.99／月起、D5 Render 需報價）互有出入。

### 引用發現

**群核科技／酷家樂（中國；Coohom 海外）**
- 2025 年企業客戶 47,416 家、單家年均訂閱收入 1.41 萬元（≈USD 1,958／TWD 6.2 萬）；大客戶（年 ≥20 萬元）424 家、ARPU 85.6 萬元；MAU 約 250 萬；新企業客戶 45.4% 先用免費／個人版（PLG）；96.9% 收入為酷家樂訂閱；研發占營收 35.5%；SpatialVerse 收入 520 萬元（0.6%）、16 家客戶 — [36 氪 2026](https://www.36kr.com/p/3705744943460485)；[鈦媒體](https://www.tmtpost.com/7960361.html)；[鈦媒體 ITValue 2026](https://www.tmtpost.com/7924100.html)；[界面 14236839](https://www.jiemian.com/article/14236839.html)；[數英](https://www.digitaling.com/articles/1318302.html)（本輪搜得；中高信心）。
- 國泰海通定位其為「雲原生空間設計軟體領導者，以專用 GPU 集群與海量數據驅動空間智能」，首次覆蓋給增持、目標價 HK$24.90 — [格隆匯](https://m.gelonghui.com/news/5239188)；[同花順](https://stock.10jqka.com.cn/20260522/c676897096.shtml)（本輪搜得）。
- 繼承：每日數百萬次渲染、數十億次 API 調用；SCMP 稱「中國版 Autodesk」 — [SCMP](https://www.scmp.com/tech/tech-trends/article/3309107/chinas-answer-autodesk-manycore-bets-ai-future-spatial-intelligence)；[新浪港股](https://finance.sina.com.cn/stock/hkstock/hkzmt/2026-02-24/doc-inhnyyvp1282748.shtml)。

**工具定價（第三方比價網站；非官方定價頁，互有出入）**
- Coohom：Capterra 列起價 USD 9.90／用戶／月（≈TWD 312）；另一整理稱 Basic 方案 3 個專案內免費、付費價於結帳時顯示 — [Capterra Coohom vs D5 Render](https://capterra.com/compare/192882-10005615/Coohom-vs-D5-Render)；[DesignFiles Coohom 替代品](https://blog.designfiles.co/coohom-alternative/)。
- Homestyler（易家）：Capterra 列 USD 9.9／月；另一整理稱約 USD 3.90／月（兩者矛盾）— [Capterra Homestyler](https://www.capterra.com/p/10016145/Homestyler/reviews)；[GetApp](https://www.getapp.com/all-software/a/homestyler/alternatives)。
- Planner 5D：免費版專案數不限但家具庫約一半；付費 Premium USD 4.99／月（年繳，≈TWD 157）、Professional USD 33.33／月（≈TWD 1,050）、Enterprise 客製；渲染為付費功能 — [Capterra Planner 5D](https://www.capterra.ie/software/164022/planner-5d)；[Wearify 免費 3D 工具整理](https://thewearify.com/3d-home-design-free/)。
- D5 Render：Capterra 標「Contact vendor」，無公開每席價格 — [Capterra](https://capterra.com/compare/192882-10005615/Coohom-vs-D5-Render)（本輪搜得；全部為第三方，低信心）。**四款工具 2025 年用戶數：未找到任何來源**。

**Spacely AI（泰國，曼谷）**
- 2024-03 獲 SCB 10X（SCBX 集團投資部門）Pre-seed 投資（金額未揭露），定位「生成式 AI 室內建築設計平台」並推出空間設計 API；2025-07 完成 USD 100 萬（≈TWD 3,150 萬）種子輪，由 PropTech Farm Fund III 領投；公司自報營收年增 10 倍、服務逾 1,500 家建築／室內設計事務所（50+ 國）、累計產出逾 200 萬張渲染；產品含 AI 渲染、影像編輯、AI 虛擬佈置、自動 3D 模型生成；資金用於 2D→3D 自動化引擎與美國市場 — [TechSauce 2025-07](https://techsauce.co/en/news/spacely-ai-raises-1m-generative-ai-architecture)；[Spacely AI Blog（Seed）](https://spacely.ai/blog/spacely-ai-secures-us-1-million-seed-round-to-super-charge-generative-ai-design-for-architects-worldwide)；[Spacely AI（SCB 10X）](https://resources.spacely.ai/spacely-ai-raises-pre-seed-funding-from-scb-10x-and-launches-revolutionary-spatial-design-apis)；[DealStreetAsia](https://dealstreetasia.com/?p=388186)；[Barchart](https://www.barchart.com/story/news/33532372/spacely-ai-secures-us-1-million-seed-round-to-supercharge-generative-ai-design-for-architects-worldwide)（本輪搜得；募資金額高信心，營運數據為自報）。

**設計師 AI 採用率與生產力調查（全球；非亞洲專屬）**
- Mattoboard《State of AI & Interior Design Report》（2025-11）：2025 年 7–9 月線上調查 328 位室內設計師／建築師（70 國、6 區）；82% 定期使用 AI、71% 認為可提升創意；85% 用 ChatGPT、38% Canva、33% Photoshop AI；57% 以「速度與效率」為最大效益、僅 21% 為創意發想；54% 擔心作品同質化、44% 提出抄襲／偏見等倫理疑慮；58% 滿意現有工具、42% 不滿意 — [officeinsight 2025-11](https://officeinsight.com/officenewswire/the-first-state-of-ai-interior-design-report-from-mattoboard-reveals-an-ai-paradox-adoption-is-widespread-but-creative-integrity-fears-persist/)；[Gifts & Decorative Accessories 2025-11-20](https://www.giftsanddec.com/research-and-analysis/help-or-hindrance-interior-designers-share-mixed-feelings-about-ai-use/)（本輪搜得；工具商贊助、小樣本，中低信心）。
- Houzz《State of AI in Construction and Design》（美國，2025-05 調查 722 家住宅導向之營建／設計公司）：31% 設計師使用 AI；使用 AI 之公司自報每週節省逾 3 小時、年化生產力效益每公司 USD 108,000（營建公司 USD 170,000、設計公司 USD 74,400 ≈ TWD 234 萬）；行政用途多於設計用途 — [Business of Home 2025-07-18](https://businessofhome.com/articles/a-new-houzz-report-says-ai-saves-designers-75k)；[Hiverlab 摘要](https://hiverlab.com/us-ai-adoption-in-construction-new-2025-highs-houzz/)；[Kitchen & Bath Design](https://www.kitchenbathdesign.com/?p=202951)；英國版 — [kbbfocus](https://kbbfocus.com/news/6084-new-houzz-report-ai-adoption-grows-across-uk-construction-and-design)（本輪搜得；自報，中信心）。
- 其他：AI × Architecture Lab 稱 100 家設計組織 AI 採用率 92%（含建築、景觀、室內；方法論未見）— [Forem 2025 報告轉載](https://scour.ing/@minezone/p/https://future.forem.com/futureform_lab/2025-industry-report-the-state-of-design-software-and-ai-integration-57k7)（低信心）；澳洲 Torrens 大學 2025 年學術研究探討室內設計社群對 AI 的接受度，結論強調須保護人類設計角色 — [Torrens University](https://research.torrens.edu.au/en/publications/the-acceptance-of-artificial-intelligence-ai-by-an-australian-int/)。
- **亞洲 12 市場本地設計師調查：未找到**。

**AI 在整裝連鎖的量測效果（印度）**
- HomeLane 稱 AI 使團隊「數分鐘而非數日」產出設計方案、設計成本降低約 25%；其 SpaceCraft 工具以 AI＋AR 提供即時設計渲染 — [D2C Insider](https://pulse.d2cinsider.com/homelane-eyes-e2-82-b91000-crore-revenue-as-ai-and-category-expansion-drive-growth/)；[KrASIA HomeLane](https://kr-asia.com/accel-backed-indian-interior-design-startup-homelane-raises-usd-30-million)；[Inc42](https://inc42.com/?p=185338)（本輪搜得；公司自報，中低信心）。
- Livspace 2026-02 半年內裁員約 1,000 人（12%），稱因 AI 代理與自動化整合至銷售、設計、營運與行銷 — [AI Market Watch](https://www.ai-market-watch.com/company/livspace)（本輪搜得；中信心）。

**其他市場（繼承，未重新搜尋）**
- 韓國：오늘의집「AI 端到端空間解決方案」、아파트멘터리×LG전자、Archisketch AI；GVR 韓國室內設計軟體市場 2024 年 USD 1.279 億 — [벤처스퀘어](https://www.venturesquare.net/1075994/)；[Archisketch](https://archisketch.substack.com/p/ai-3b0)；[GVR](https://www.grandviewresearch.com/horizon/outlook/interior-design-software-market/south-korea)。
- 台灣：100室內設計免費 AI 設計工具（行銷成分高）— [NOWnews](https://www.nownews.com/news/6770793)；越南：AiHouse（自稱 8,000 萬模型）、Homestyler 越南文版 — [AiHouse](https://www.aihouse.com/vi)；[HAWA](https://hawa.vn/khi-ai-thiet-ke-noi-that/)。
- 日本、新加坡、香港、馬來西亞、菲律賓：AI／3D 採用資料無。

### 推論
- 酷家樂單家企業年均 1.41 萬元人民幣（≈TWD 6.2 萬）的 ARPU 證實設計 SaaS 是「每月數百到一千多元人民幣」的低價採購項，而非 BIM 級投資；對台灣業者而言採購門檻極低。
- 工具商營收成長放緩（8.6%）、空間智能僅 0.6%，顯示「AI 設計」在 2025 年仍是既有 3D 訂閱的附加功能；AI 可量化效果（HomeLane −25% 設計成本、Houzz 每週 3 小時）全部來自自報。
- Livspace 裁員與 HomeLane 成本下降指向同一方向：AI 先取代「設計產出與銷售支援人力」，而非施工端。

### 缺口
- Coohom 海外（含台灣）用戶數與官方定價；Homestyler、Planner 5D、SketchUp／Enscape、D5 Render、Chaos 在亞洲各市場用戶數；任何亞洲市場設計師 AI 採用率／情緒調查；AI 報價／AI 量房工具的準確度與使用量。

---

## 4. BIM、數位施工管理與供應鏈數位化

### 結論
新加坡與香港的 BIM 強制令已有明確時程，但**均針對建築圖則／公共工程，無一明文涵蓋室內裝修工程**：CORENET X 依 2025-01 修訂時程分三階段強制（2025-10-01／2026-10-01／2027-10-01），BIM（IFC-SG）門檻為新建或新增 GFA ≥5,000 ㎡ 之重大增改建；香港 2025-04-01 起公共工程招標強制 BIM，私人圖則 BIM 路線圖仍在諮詢（業界提及 2029 年）。日本 ANDPAD 依比較網站達 23 萬社、68 萬用戶、連續 8 年市占第一，是亞洲最大的施工管理 SaaS 可引用數字（官方 2025 新聞稿未取得）。韓國 BIM 義務化對室內工程之適用、台灣 BIM 要求：無資料。資金託管與付款節點（繼承）仍是跨國最先落地的數位履約機制。

### 引用發現

**新加坡 CORENET X 與 DfMA**
- URA 通函 DC23-07「CORENET X 實施計畫」：原訂 2025-04-01 起新案強制使用 CORENET X 提交、進行中案件自 2026 上半年起納入 — [URA DC23-07](https://www.ura.gov.sg/guidelines/circulars/dc23-07/)；[URA DC23-01](https://www.ura.gov.sg/Corporate/Guidelines/Circulars/dc23-01)（本輪搜得；官方，高信心）。
- 2025-01 報導 BCA 修訂時程：2025-10-01 起 GFA ≥30,000 ㎡ 新案強制、2026-10-01 起所有新案、2027-10-01 起進行中案件；BCA 稱業界回饋有助改進流程與平台 — [Southeast Asia Construction 2025-01-24](https://bkt.tradelinkmedia.biz/publications/7/news/5701)；[99.co 2025](https://www.99.co/singapore/insider/from-october-2025-corenet-x-mandatory-for-building-submissions/)（本輪搜得；媒體轉述官方，中高信心；與 DC23-07 衝突，以 BCA 最新公告為準）。
- BIM 提交須採 openBIM／IFC-SG 格式並遵守 CORENET X Code of Practice；BIM 要求適用新建或新增 GFA ≥5,000 ㎡ 之重大增改建（A&A）— [BCA BIM 頁](https://www1.bca.gov.sg/safety-and-standards/lifts-escalators-and-mechanised-car-parking-systems/building-information-modelling-bim/)（本輪搜得；官方，高信心）。
- 可建性（Buildability）合規三途徑之一為達到最低預製／DfMA 技術水準，其餘為 B-Score／C-Score；BIM 提交須帶預製構件、預製鋼筋、標準尺寸等可建性屬性；QP 與承建商於各 gateway 提交 — [BCA Guide to BDAS for COP 2022（2026-03 版）](https://isomer-user-content.by.gov.sg/338/a3a927bf-f335-418d-9e96-ba76a3c9eb84/Guide%20to%20BDAS%20for%20COP%202022_Mar26%20version%20v1.pdf)（本輪搜得；官方）。**未找到 CORENET X 針對 PPVC 模組或室內裝修（fit-out）之條文**。
- 繼承：HDB 裝修須經 DRC 承包商申請；CaseTrust 自願制 — [HDB](https://www.hdb.gov.sg/residential/living-in-an-hdb-flat/renovation/applying-for-approval)；[MTI 2025](https://www.mti.gov.sg/Newsroom/Parliamentary-Replies/2025/02/Written-reply-to-PQ-on-consumer-protection-for-customers-of-non-accredited-renovation-contractors)。

**香港 BIM**
- 發展局工務技術通告 DEVB TC(W) No. 1/2025：2025-04-01 起所有公共工程招標資料須含 BIM 模型，與 2D 招標圖對應之模型元素具合約約束力，MEP 等系統暫為參考 — [FTI Consulting](https://www.fticonsulting.com/insights/articles/hksar-governments-directives-bim-development)；[Turner & Townsend](https://www.turnerandtownsend.com/insights/digital-built-environment-evolution-of-hong-kongs-bim-policy/)；[DEVB BIM Book PDF](https://www.devb.gov.hk:443/filemanager/en/content_2373/BIM-Book-content-en.pdf)（本輪搜得；顧問轉述官方通告，中高信心）。
- 私人圖則：發展局《Roadmap on Adoption of BIM for Building Plan Preparation and Submission》2023-12-29 至 2024-02-29 諮詢，終極目標為所有《建築物條例》圖則全程 BIM；屋宇署現行立場為「鼓勵」AP／RSE／RGE 採用 BIM，BIM 僅作補充參考資料、圖則與 BIM 不一致時以圖則為準 — [屋宇署 BIM 頁](https://bd.gov.hk/en/resources/online-tools/building-information-modelling/index.html)；[屋宇署 PL071e](https://www.bd.gov.hk/doc/en/resources/codes-and-references/notices-and-reports/SFCQ2023/PL071e.pdf)（本輪搜得；官方，高信心）。
- CIC 2024-07 委員會紀錄引述業界：發展局路線圖目標 2029 年強制以 BIM 模型及 BIM 生成圖則送審（會議發言，非確定政策）；HKIE 2025-11 對路線圖提交意見、指出技術人才短缺 — [CIC-BIM-M-002-24](https://cic.hk/files/committee_file/6/file/10700/en/CIC-BIM-M-002-24_e.pdf)；[HKIE 2025-11](https://hkie.org.hk/wp-content/uploads/hkie/20251119/65e6c27d1dc04.pdf)；[CIC BIM 政策頁](https://bim.cic.hk/en/bim_in_hk)（本輪搜得；中信心）。**室內裝修工程 BIM 要求：無**。

**日本：ANDPAD 與建築確認**
- ANDPAD（アンドパッド）：IT トレンド頁（2026-03-13 更新）稱利用社数 23 萬社、用戶 68 萬人、連續 8 年施工管理 App 市占第一（出處：デロイト トーマツ ミック経済研究所 2025-12 號）；App Store 舊版文案為 13 萬社／33 萬人；2017 年報導服務首年導入 350 社；用戶評論稱「リフォーム時現場・営業・管理連攜更容易」 — [IT トレンド ANDPAD](https://it-trend.jp/construction_management_system/15908)；[App Store ANDPAD](https://apps.apple.com/jp/app/andpad-%E3%82%AB%E3%83%B3%E3%82%BF%E3%83%B3%E6%96%BD%E5%B7%A5%E7%AE%A1%E7%90%86%E3%82%A2%E3%83%97%E3%83%AA/id1067643333)；[THE BRIDGE 2017](https://thebridge.jp/2017/01/andpad)；[IT トレンド 評論](https://it-trend.jp/construction_management_system/15908/review/155655)（本輪搜得；比較網站轉述，中低信心；**官方 2025 導入社数新聞稿未取得**）。ANDPAD AWARD 2025 設 DX カンパニー部門 — [koubo.jp](https://koubo.jp/press-release/prtimes/c18154_r143)。
- 繼承：建築基準法 2025-04-01「四號特例縮小」、審查期 7→35 日 — [国土交通省](https://www.mlit.go.jp/common/001500388.pdf)；[ANDPAD 專欄](https://andpad.jp/columns/0086)；丹青社×若水國際 BIM MOU — [共同通信 PR Wire](https://kyodonewsprwire.jp/release/202407053219)。

**韓國、台灣、中國、其他**
- 韓國 BIM 義務化對室內工程之適用：本輪未搜尋（缺口）。繼承：行為許可與結構安全確認 — [법제처](https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=1222&ccfNo=2&cciNo=1&cnpClsNo=1)。
- 台灣：繼承室內裝修審查 7 日、規費與國土署 2026-04-14 澄清 — [全國法規資料庫](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0070148)；[中央社](https://www.cna.com.tw/news/ahel/202604140322.aspx)；BIM 要求無。
- 中國：繼承貝殼 BIM＋模組化 — [新浪](https://finance.sina.com.cn/stock/estate/integration/2026-03-16/doc-inhrequs9902543.shtml)。

**數位履約、付款節點與資金託管（繼承，未重新搜尋）**
- 中國土巴兔節點付款 2022 年保住 200 多位業主 800 餘萬元；聖都銀行存管；住范兒 2025-06 資金鏈斷裂 — [澎湃](https://www.thepaper.cn/newsDetail_forward_27769661)；[四川在線](https://cbgc.scol.com.cn/news/7838213)；[鈦媒體](https://www.tmtpost.com/7644935.html)。
- 韓國 오늘의집 2023 施工責任保障後施工交易額近倍增 — [데모데이](https://demoday.co.kr/bm-analysis/109)；公正委 4 平台自律協約 — [뉴시스](https://www.newsis.com/view/NISX20241216_0002998493)。
- 新加坡 Qanvast Guarantee S$50,000 訂金保障（本輪搜得，見 §2）。
- 台灣住保會 2025 年履約 2,866 件／NT$3.17 億 — [理財周刊](https://www.moneyweekly.com.tw/_Article?AID=247503)；國土署定型化契約草案 — [國土署 PDF](https://www.nlma.gov.tw/uploads/files/4a4f5b6c19d35226adf133a9a2bde45d.pdf)。
- 印尼 SejasaPay — [Sejasa](https://www.sejasa.com/)；日本瑕疵保險 2025 年度 4,496 件 — [Fujisan](https://www.fujisan.co.jp/product/1281683407/b/2808733/)。

**材料採購數位化（繼承）**
- 貝殼主材 80%／輔材 60% 集採 — [瑞財經](https://www.rccaijing.com/news-7307953023459456534.html)；Mitra10 全通路 — [Industry.co.id](https://www.industry.co.id/read/152024/csap-catat-pendapatan-rp175-t-di-2025-bagi-dividen-meski-daya-beli-lesu)。

### 推論
- 新加坡（GFA ≥5,000 ㎡）與香港（公共工程）的 BIM 門檻都在「建築」層級，室內裝修業者的實質 BIM 需求來自甲方（大型商辦、公共案）而非法規；住宅翻修在三年內不會被強制。
- ANDPAD 23 萬社（若屬實）對比日本約 47 萬家建設業者，顯示施工管理 SaaS 在日本的滲透已過半，這是 12 市場中唯一「施工端數位化」可能已成主流的訊號；台灣無對應產品數據。

### 缺口
- CORENET X Code of Practice 對室內裝修（fit-out）與 PPVC 的具體條文；香港私人圖則 BIM 強制年份；韓國 BIM 義務化、台灣 BIM；ANDPAD 官方 2025 導入社数與定價；台灣／韓國／東南亞工程管理 SaaS 數據；第三方託管的法定地位與普及率。

---

## 5. 預製與模組化內裝

### 結論
中國是唯一有明確「裝配式裝修」政策鏈的市場：住建部 2025 年底《關於提升住房品質的意見》→國務院 2026-05《城市更新「十五五」規劃》→住建部《促進裝配式裝修發展的指導意見（徵求意見稿）》（2030 年顯著提高、保障性租賃住房全面採用），但**全國滲透率無官方數字**，且市場規模各機構口徑矛盾（智研 2025 年 3,431.5 億元 vs 同機構另頁預測 6,390 億元），應用仍以 B 端（保障房、長租、酒店）為主。新加坡 DfMA 為可建性合規途徑之一（見 §4），但對室內之規定未取得。日本ユニットバス、韓國빌트인、台灣系統櫃市占：**本輪搜尋未找到任何產業統計**（台灣「系統櫃」查詢結果全為無關的機櫃／PCB 資料）。

### 引用發現
- 中國政策：住建部 2025 年底《關於提升住房品質的意見》明確提出「積極發展裝配式裝修，推廣集成廚衛、架空地面、裝配式隔牆等」；國務院 2026-05 印發《城市更新「十五五」規劃》提出「推廣裝配式裝修」「提升裝配式裝修應用比例」 — [新華網 2026-09-01](https://www.news.cn/house/20260901/7f4f87117cd64456bbcfbce729c89b23/c.html)（本輪搜得；官方媒體，高信心）。
- 住建部公開徵求《關於促進裝配式裝修發展的指導意見（徵求意見稿）》：擬提出到 2030 年裝配式裝修應用比例顯著提高，支持保障性租賃住房、人才公寓等租賃型房屋全面採用；是否已正式發布未確認 — [格隆匯快訊](https://m.gelonghui.com/live/2658510)（本輪搜得；中信心）。
- 裝配式建築目標：2016 年國務院、2017 年住建部文件設定 2020 年 15%、2025 年 30% 新建建築占比；北京目標 2025 年 55% — [中國證券報 2022](https://cs.com.cn/xwzx/hg/202202/t20220224_6244541.html)；福建省開展裝配式裝修試點並公布部品部件生產基地名單 — [福建省住建廳 PDF](https://zjt.fujian.gov.cn/xxgk/zfxxgkzl/xxgkml/dfxfgzfgzhgfxwj/jzsc/202403/P020240311498323463954.pdf)；上海市住建委相關文件 — [上海住建委 PDF](https://zjw.sh.gov.cn/cmsres/de/de8050460b294f9e81f3f3198e8b0367/b80791aa8c389e36eb5f8dc5f0058ce6.pdf)（本輪搜得；官方）。
- 市場規模（矛盾，慎用）：智研諮詢稱裝配式裝修市場規模 2016 年 3.7 億元→2025 年 3,431.5 億元（≈USD 477 億／TWD 1.50 兆）；同機構另頁稱 2018 年 175 億、2022 年 3,440 億、2025 年預測 6,390 億元（≈USD 888 億／TWD 2.80 兆）— [智研 1274143](https://www.chyxx.com/cyzx/1274143.html)；[智研 1256864](https://www.chyxx.com/industry/1256864.html)；觀研天下 2025／2026 報告 — [觀研 202509](https://www.chinabaogao.com/baogao/202509/765872.html)；[觀研 202604](https://www.chinabaogao.com/baogao/202604/789870.html)（本輪搜得；研究機構，低信心；**非官方統計**）。
- 滲透率：鈦媒體分析指「從 To B 邁向 To C 的滲透率與認知度仍待突破」，即住宅 C 端應用仍低 — [鈦媒體](https://www.tmtpost.com/7451937.html)（本輪搜得；質性）。**全國裝配式裝修滲透率 2025 實際值：未找到**。
- 繼承：亞廈股份 2025 年毛利率 15.61%（裝配式龍頭）— [新浪 2026-04-30](https://finance.sina.cn/2026-04-30/detail-inhwhene7094454.d.html)；定制家居龍頭 2025 年營收 −6～−17% — [新浪 2026-05-12](https://news.sina.cn/2026-05-12/detail-inhxrshc1334104.d.html)；土巴兔平台整裝占比 82.4% — [大眾網](https://m.dzplus.dzng.com/share/general/0/NEWS3468079NBYNVQOGXEHST)。
- 新加坡：DfMA 最低預製水準為可建性合規三途徑之一；BIM 須帶預製構件屬性 — [BCA BDAS 指南](https://isomer-user-content.by.gov.sg/338/a3a927bf-f335-418d-9e96-ba76a3c9eb84/Guide%20to%20BDAS%20for%20COP%202022_Mar26%20version%20v1.pdf)（本輪搜得）；PPVC 室內規定：無。
- 台灣：系統櫃市場規模／市占搜尋無結果；僅有全球「模組化儲存系統」研究機構估值 2025 年 USD 43 億→2035 年 68 億（CAGR 4.6%，全球口徑，含模組化櫥櫃）— [GII 全球模組化儲存系統](https://www.gii.tw/report/gis2107936-modular-storage-system-market-analysis-forecast.html)（本輪搜得；低信心、非台灣）。繼承：100室內設計主推模組化裝修；三商美福一站式 — [NOWnews](https://www.nownews.com/news/6770793)；[商周](https://www.businessweekly.com.tw/business/indep/1005275)。
- 印度、印尼、越南（繼承）：Livspace／HomeLane 模組化櫃體標準交付（HomeLane FY25 材料費 Rs 320 crore）— [Entrackr](https://entrackr.com/fintrackr/homelane-records-rs-748-revenue-in-fy25-but-falls-short-of-projections-10586234)；Tokopedia studio 全裝套裝 Rp 2,499 萬–7,500 萬 — [Tokopedia](https://www.tokopedia.com/find/interior-apartemen-studio)。
- 日本ユニットバス、韓國빌트인／옵션、馬來西亞 IBS 對室內：無資料。

### 推論
- 中國政策把裝配式裝修綁在「保障性租賃住房」與「城市更新」上，意味 B 端採購（國企、地方平台公司）是滲透主力；C 端翻修市場的滲透短期仍靠定制家居（櫃體）而非全屋裝配。
- 台灣系統櫃雖是實務主流，但無任何公開產業統計，集團若要以系統櫃作標準品，須自行以上市櫃（如系統家具廠商）營收與公會資料建立基準。

### 缺口
- 中國裝配式裝修全國滲透率（住建部口徑）與指導意見定稿；日本ユニットバス出貨統計（住宅設備システム協會）；韓國빌트인滲透率；新加坡 PPVC／DfMA 對室內之規定；台灣系統櫃市場規模與市占；馬來西亞 IBS。

---

## 6. 智慧家庭整合：Haier 三翼鳥、Xiaomi、Samsung SmartThings、LIXIL、Panasonic 與裝修綁售

### 結論
中國海爾三翼鳥仍是亞洲唯一有「家電品牌→場景整裝」可量化證據的案例（2024 年零售額破百億元、2024-03 首批 260 家門店入駐天貓喵店、2022 年月活 675 萬、2025-12 稱近千家品牌店轉型），但**2025 全年零售額、門店數、滲透率本輪仍未找到**。亞太智慧家庭市場規模各研究機構互相矛盾（Ken Research USD 302 億／2025 vs USD 502 億／2024），僅 GMI 一項可引用的結構數據：2025 年海爾、三星、LG、Amazon、小米五大合計 47% 份額；研究機構假設 2024 年寬頻家庭自動化滲透率約 15%（模型輸入，非調查）。各國「翻修案綁售智慧家庭」比率：全部無資料。

### 引用發現
- 海爾三翼鳥：2024-03-15 門店轉型升級，首批 260 家線下店入駐天貓喵店 — [海爾 2024-03-15](https://www.haier.com/press-events/news/20240315_236326.shtml)；2022-03 稱平台自 2021-08 上線後月活 675 萬、App 上線 5 個月向 15,590 個家庭提供 15,747 套方案 — [海爾 2022-03-02](https://www.haier.com/press-events/news/20220302_176521.shtml)；2025-07 建博會展示基於物聯網與自研「三翼鳥 Uhome 大模型」的 AI 智慧家方案（聯動煙櫃廚房、一鍵切換健身陽台）— [海爾 2025-07-10](https://www.haier.com/about_haier/xinwen/20250710_268034.shtml)；2025-12 文章標題「海爾智家 2025 年近千家品牌店『變身』」，正文引奧維雲網 2025 上半年家電線上零售額 +14% — [海爾 2025-12-16](https://www.haier.com/about_haier/xinwen/20251216_284062.shtml)（本輪搜得；企業自報，中低信心）。早期批評指三翼鳥 16 款產品多數門店無售、App 下載量不多 — [界面](https://www.jiemian.com/article/9656862.html)；[界面 10683531](https://www.jiemian.com/article/10683531.html)（本輪搜得；較早期）。
- 繼承：三翼鳥 2024 年零售額破百億元、智家 APP MAU 1,000 萬、2024 年新增 1,556 家門店、戶均消費 42 萬元 — [新浪科技 2025-01-20](https://finance.sina.com.cn/tech/roll/2025-01-20/doc-inefrnxv9444188.shtml)；[界面 6485853](https://www.jiemian.com/article/6485853.html)；奧維雲網 2025 高端精裝房智能家居華為份額近 50% — [199IT](https://www.199it.com/archives/1812063.html)；艾媒 49.45% 已購智能家居 — [艾媒](https://report.iimedia.cn/tag/家居家装)；2025 家裝廚衛煥新補貼含智能家居（商辦消費函〔2025〕29 號）— [中國政府網](https://www.gov.cn/zhengce/zhengceku/202501/content_7001494.htm)；2026 國補家裝類移出 — [新華網 2026-01-02](https://www.news.cn/politics/20260102/8280c115602841078b65d8f5176b239c/c.html)。
- 亞太市場規模（矛盾）：Ken Research 稱亞太智慧家庭自動化市場 2025 年 USD 302 億、至 2032 年 CAGR 17.5%；另一 Ken Research 報告稱 2024 年 USD 502 億、至 2030 年 CAGR 24.2% — [Ken Research（automation）](https://www.kenresearch.com/asia-pacific-smart-home-automation-market)；[Ken Research（smart homes）](https://www.kenresearch.com/industry-reports/asia-pacific-smart-homes-market)；[Spherical Insights APAC](https://www.sphericalinsights.com/reports/asia-pacific-smart-home-market)（本輪搜得；研究機構，低信心，**非官方統計**）。
- 競爭結構：Global Market Insights（韓文頁）稱 2025 年海爾智家、三星電子、LG 電子、Amazon、小米五大合計 47% 份額；主要廠商另含美的 — [GMI（ko）](https://www.gminsights.com/ko/industry-analysis/smart-home-market)（本輪搜得；研究機構，中低信心）。
- 滲透率：研究報告假設 2024 年寬頻家庭中有意義之自動化滲透率 15%（模型假設非調查）；新建住宅區隔預期 2025–2030 年 CAGR 最高，因布線與牆面可預先規劃（翻修安裝較難） — [Ken Research](https://www.kenresearch.com/asia-pacific-smart-home-automation-market)；Braze／Marketing-Interactive 2026-05 亞太「connected homes」專題 — [Marketing-Interactive](https://www.marketing-interactive.com/connected-homes-apac-embraces-smart-home-living)（本輪搜得；低信心）。
- Samsung SmartThings 整合所有 IoT App、小米五年投資 USD 15 億於 IoT：均為 2019 年前後舊聞，2025 狀態未確認 — [Business Wire 2019](https://www.businesswire.com/news/home/20190110005268/en/)（本輪搜得；過時）。
- 繼承：韓國 아파트멘터리×LG전자 — [테크42](https://www.tech42.co.kr/%EC%95%84%ED%8C%8C%ED%8A%B8%EB%A9%98%ED%84%B0%EB%A6%AC-lg%EC%A0%84%EC%9E%90-%EC%A0%84%EB%9E%B5%EC%A0%81-%ED%88%AC%EC%9E%90-%EC%9C%A0%EC%B9%98-ai%EC%9C%B5%ED%95%A9-%EB%AA%B0%EC%9E%85%ED%98%95/)；越南 Vietbuild 2025 智慧家居攤位最熱 — [Mekong ASEAN](https://mekongasean.vn/cac-gian-hang-giai-phap-nha-thong-minh-hut-khach-tai-vietbuild-2025-42065.html)；台灣櫻花 AI 智能廚電 — [優分析](https://uanalyze.com.tw/articles/8096948742)。
- 日本 LIXIL／Panasonic、新加坡、香港、馬來西亞、泰國、菲律賓、印度：無資料。

### 推論
- 研究機構對亞太智慧家庭規模的分歧（USD 302 億 vs 502 億）大到無法作決策依據；可用的只有結構性結論：五大品牌寡占近半、新建比翻修容易導入。
- 三翼鳥模式本質是「家電門店導流整裝」；2025 年海爾自報僅剩「門店變身」等質性訊息、未再公布零售額，整合時應將「2024 破百億」標為最後一個可引用年份。

### 缺口
- 三翼鳥 2025 零售額／門店數；Samsung SmartThings、Xiaomi、LIXIL、Panasonic、LG ThinQ 於裝修案之綁售率；各市場翻修案智慧家庭滲透率（調查口徑）；奧維雲網 2025 全屋智能報告原文。

---

## 7. 數位獲客：社群／平台 vs 轉介的占比、每線索成本、網紅／設計師創作者模式

### 結論
中國小紅書是 12 市場中唯一有「內容→線索→成交」量化證據的社群：2024 年家居家裝 GMV 年增 2.5 倍、2025 年 1–5 月家居種草內容月均互動逾 3 億、商業筆記 +45%、用戶主動發布之「需求帖」年增 175%、#我的裝修記錄 183.3 億次瀏覽、逾 30 位博主單月漲粉 10 萬+、軟裝設計師單場直播 GMV 2,000 萬元；同時傳統線索平台衰退（齊屹 527 元／條且 −20%；土巴兔 COO 稱 2025 下半年全行業流量下滑）。韓國三份調查（繼承）顯示 SNS／YouTube 與入口搜尋各約四成、平台三成。**新加坡／馬來西亞 Meta 廣告 CPL 基準：搜尋未找到任何來源**；日本、台灣、越南、印尼、泰國、菲律賓、香港、印度的社群線索占比亦無量化資料。

### 引用發現

**中國：小紅書與線索平台**
- 2024 年小紅書家居家裝賽道 GMV 年增 2.5 倍；2025 年前 5 個月逾 30 位家居家裝博主單月漲粉逾 10 萬；軟裝設計師 @一顆KK 單場直播 GMV 達 2,000 萬元（≈USD 278 萬／TWD 8,750 萬，多為小眾家具品牌）；用戶在博主影片下求推薦裝修方案／公司，已有達人與商家以家居內容獲取線索再線下交付；家居家裝＋科技類 UGC「需求帖」2024 vs 2023 年增 175%；#我的裝修記錄 話題瀏覽量 183.3 億 — [36 氪 2025](https://www.36kr.com/p/3331683375458568)；[36 氪（海外站）](https://eu.36kr.com/zh/p/3081593117145480)（本輪搜得；媒體引平台／第三方數據，中信心）。
- 千瓜數據：2025 年 1–5 月小紅書家居行業種草內容月均預估互動量超 3 億、商業筆記數年增 45%+ — [人人都是產品經理 6243948](https://www.woshipm.com/share/6243948.html)；[人人都是產品經理 6283320](https://www.woshipm.com/ai/6283320.html)；[界面 13491969](https://www.jiemian.com/article/13491969.html)（本輪搜得；第三方監測，中低信心）。
- 小紅書官方未披露電商 GMV，業內估 2024 年約 4,000 億元（估算，低信心）；「紅貓計畫」（與淘天）打通種草到下單、廣告可掛鏈跳轉 — [界面 12790194](https://www.jiemian.com/article/12790194.html)（本輪搜得）。
- 投放成本：第三方 618 策略報告建議「5 月上旬信息流成本開始上漲，前置搶占 4 月流量紅利期」（家電／家具／家裝設計類目；無絕對 CPL 數字）— [發現報告：2025 小紅書 618 大家電&家具&家裝設計策略](https://www.fxbaogao.com/detail/5556825)（本輪搜得；低信心）。
- 土巴兔 COO 方浩（2025-12 生態大會）：下半年全行業流量持續下滑；地產風險引發產業鏈連鎖反應 — [楚天都市報](https://www.ctdsb.net/c1734_202512/2623176.html)（本輪搜得）。
- 繼承：齊屹 2024 年每條線索 527 元（≈USD 73／TWD 2,306）、線索量 −20% — [同花順](https://stock.10jqka.com.cn/20250427/c667789677.shtml)；貝殼房產交易貢獻家裝合同額約 39%（2022Q4）— [21 經濟網](https://www.21jingji.com/article/20230318/herald/e28a277c5184a40ee1804a3896d521ba.html)；線上觸點對家居決策影響率 >70%、被窩抖音線索 300 萬（自報）— 見前版 CN-A；低價引流套路 — [澎湃](https://www.thepaper.cn/newsDetail_forward_32020018)。

**韓國（繼承）**
- THE LIVING 調查：65.3% 用過線上裝修平台、22.9% 透過平台實際發包；資訊來源入口部落格 42.2%／線上平台 31.1%；SNS 39.9%／入口搜尋 38.7% — [더리빙 2680](https://www.theliving.co.kr/news/articleView.html?idxno=21707)；[더리빙 3198](https://www.theliving.co.kr/news/articleView.html?idxno=22216)；[더리빙 1962](https://www.theliving.co.kr/news/articleView.html?idxno=23807)；KiwiSurvey 2023：入口搜尋 51.5%、裝修 App 36.8%、YouTube 32.5% — [KiwiSurvey](https://kiwisurvey.kr/report/detail?id=85)；KCA 2025-07 對숨고等平台警示 — [경향신문](https://www.khan.co.kr/article/202507011523011)。

**新加坡／馬來西亞**
- Meta（Facebook／Instagram）裝修類 CPL 基準：**搜尋結果全為裝修價格資料，無任何廣告成本或轉化率來源**。可引用的成本輸入：Homees 2024 年估 4 房 BTO 裝修 S$33,000–58,000（≈USD 24,400–43,000／TWD 77–135 萬）、公寓 S$40,000–120,000；設計費常佔預算 5–10% — [Home & Decor（Homees）](https://www.homeanddecor.com.sg/renovation/interior-designer-or-contractor)；[SingSaver](https://www.singsaver.com.sg/blog/cost-of-interior-designer-singapore)；馬來西亞 2 房公寓基本套裝 RM35,000–60,000、全設計 RM70,000–120,000（2026 指南；其引述「產業 RM48 億」未能驗證）— [Shinjiru 2026](https://digital.shinjiru.com.my/?p=3976)（本輪搜得；低信心）。
- Qanvast 以訂閱制向設計公司收費（非 CPL）— [Qanvast About](https://qanvast.com/sg/about-us)（本輪搜得）。繼承：LAM 稽查顯示線上廣告為未註冊業者主要獲客管道 — [LAM（X）](https://x.com/LembagaArkitek/status/2065266904147939778)。

**台灣、日本、印度、越南、印尼（繼承）**
- 台灣 100室內設計 2025 年 15,000 筆需求→4,000 筆簽約（平台自報）— [NOWnews](https://www.nownews.com/news/6770793)；屋主資訊來源調查無。
- 日本：OB 顧客網絡＋仲介一站式＋網路見積三路並行；點檢商法諮詢 2023→2025 年度 11,879→5,544 件 — [国民生活センター](https://www.kokusen.go.jp/soudan_topics/data/reformtenken.html)。
- 印度 HomeLane FY25 廣告費 Rs 84 crore ≈ 營收 11.2%（本人計算）— [Entrackr](https://entrackr.com/fintrackr/homelane-records-rs-748-revenue-in-fy25-but-falls-short-of-projections-10586234)。
- 越南 Facebook 7,900 萬／Zalo 7,830 萬 MAU、TikTok 催生裝飾新職種 — [Elite Asia 2026](https://www.eliteasia.co/top-digital-and-social-media-trends-in-vietnam-in-2026/)；[Diễn đàn Doanh nghiệp](https://diendandoanhnghiep.vn/tiktok-de-ra-viec-moi-cho-linh-vuc-trang-tri-noi-that-10051203.html)。

### 推論
- 中國的證據鏈（線索平台單價上升且量減、小紅書內容互動與 GMV 暴增）支持「付費線索→創作者內容」的結構性轉移；2025 下半年全行業流量下滑則表示內容平台也進入存量競爭。
- 韓國「用平台比價 42.4% vs 用平台發包 22.9%」與新加坡 Qanvast「訂閱不抽佣」共同顯示平台的實際角色是資訊／比價入口，簽約仍回到業者，故平台費用應以「曝光訂閱」而非「線索買斷」計價。
- 沒有任何市場公布裝修類 CPL 基準，所有「每線索成本」只能以齊屹（527 元）與 HomeLane（廣告占營收 11%）兩個財報數字作上下界。

### 缺口
- 各市場 2025「首次接觸管道」調查；Instagram／YouTube／TikTok／LINE／Facebook 裝修線索占比；新加坡／馬來西亞／台灣 Meta／Google CPL 與轉化率；貝殼、三翼鳥 CAC；台灣 100室內設計／PULO 線索成本；小紅書家裝官方 GMV。

---

## 8. 對台灣業者的啟示：現在可部署的工具／平台與 ROI 證據

### 結論
依 12 市場證據，台灣業者「現在就能部署且有海外 ROI 證據」的只有三類：(1) 低價 3D／AI 設計 SaaS 作簽單工具——酷家樂單家企業年均 1.41 萬元人民幣、45.4% 客戶由免費版轉化、Coohom USD 9.90／月起、Planner 5D USD 4.99／月起、Spacely AI 等生成式渲染；HomeLane 自報設計成本 −25%、Houzz 自報每週省 3 小時；(2) 在既有流量母體經營案例與創作者內容（小紅書家裝 GMV +2.5×、需求帖 +175%；100室內設計月訪 200 萬）；(3) 履約保證／節點付款／第三方託管（오늘의집導入後施工交易額近倍增；Qanvast S$50,000 保障；住保會 2025 年 2,866 件）。自建平台（土巴兔 2022 撤 IPO、齊屹線索 −20%、NocNoc 連虧五年後關閉、Dekoruma 售出、Livspace 裁員）與 BIM／裝配式／智慧家庭綁售（無滲透率證據）不宜作策略投資。詳細啟示見 §11。

### 引用發現（彙整，URL 見 §2–§7）
- 可部署工具成本：酷家樂企業 ARPU 1.41 萬元／年（≈TWD 6.2 萬）；Coohom 起價 USD 9.90／月；Planner 5D USD 4.99–33.33／月；Spacely AI 自報 1,500+ 事務所採用。
- 平台 ROI 負面證據：土巴兔銷售費用率 61%（2021）；齊屹線索 527 元且 −20%（2024）；오늘의집 2025 營業損失 147 億韓元；Livspace FY25 淨損 Rs 242 crore、2026 裁員 12%；HomeLane 廣告占營收 11%；NocNoc 2020–2024 無一年獲利並宣布結束服務；Dekoruma 售予 Blibli。
- 履約機制正面證據：오늘의집 2023 施工責任保障後施工交易額近倍增、2024 累計破 1 兆韓元；Qanvast Trust Programme S$50,000；土巴兔節點付款保住 800 餘萬元；住保會 2025 年 2,866 件／3.17 億元。
- 台灣現況：100室內設計 2024 月訪 200 萬、1,400 家設計公司、年媒合 2 萬筆需求；2025 年 4,000 筆簽約（推算 GMV 占市場 <1%）；PULO 案件 95% 為統包／設計需求（自報）；裝修佬（香港）已進軍台灣。

### 推論
- 台灣平台滲透率（<1% GMV）遠低於韓國（65.3% 用過平台）與中國（互聯網家裝 20.8%），平台化空間存在，但依中韓經驗將由既有流量母體（數字科技、城邦、電商、仲介）而非新進者取得；集團應「入駐＋內容」而非「自建」。
