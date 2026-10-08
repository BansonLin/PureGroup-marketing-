# T4 數位平台、AI 設計工具與科技應用（Digital platforms, AI design tools and technology adoption）

> **執行狀態與限制（請整合者先讀）**
> 1. 本回合（2026-10-08）WebSearch 額度在第一次查詢前即已被同一工作階段的其他代理用罄（系統回覆「web search budget is used up」），WebFetch／curl 亦被環境封鎖；因此**本筆記沒有任何一條由本代理新搜得的來源**。
> 2. 所有附 URL 的事實，皆重用本專案既有筆記（T1、T2、T3、CN-A／B、KR-A／B、JP-A／B、TW-A／B、VN-A／B、ID-A／B、MY-A／B）在其搜尋結果摘要中記錄的 URL；這些 URL 均**未曾被任何代理實際開啟核對原文**（整合協議 §10）。來源清單中標註「經由 XX 筆記」。
> 3. 任務指定的多項指標（Coohom 海外用戶、Homestyler／Planner 5D／Spacely／D5 Render 用戶數、設計師 AI 採用率調查、ANDPAD 導入社数、CORENET X 對室內工程的要求、裝配式裝修滲透率、系統櫃市占、Samsung SmartThings／Xiaomi／LIXIL／Panasonic 智慧家庭綁裝修比率、各國社群獲客占比與 CPL 基準）**本輪一律無資料**，全部列入 §6 資料缺口並附下一輪可直接續跑的 20 條查詢（附錄 A）。**本筆記沒有任何估計值**；少數「本人推算」皆標明算式與假設。
> 4. 匯率（本筆記統一採用，與各國筆記略有差異時以本表為準）：USD 1 = TWD 31.5 = CNY 7.2 = KRW 1,400 = JPY 150 = INR 86 = SGD 1.35 = HKD 7.8 = MYR 4.4 = THB 33 = VND 25,500 = IDR 16,200 = PHP 57（2025–2026 年概略水準，未經本輪搜尋驗證，整合時請以 V2 統一匯率表覆寫）。
> 5. 信心等級依整合協議：A 級（上市公司財報／招股書／政府）→ 高；B 級（協會、券商、主流財經媒體引用原始數據）→ 中高／中；C 級（平台自報、市調新聞稿、未附方法論）→ 中低／低，單獨出現時視為【示意】。

---

## 1. 摘要

1. 亞洲室內裝修的「數位化」在 12 市場中呈現三種成熟度：**中國與韓國**已跑完「內容社群→電商→施工媒合→履約保障」整個循環，並出現以設計工具為核心的上市公司（群核科技／酷家樂 Coohom，2026-04-17 港交所上市，2025 年營收 8.20 億元人民幣、MAU 250 萬、毛利率 82.2%）與年營收破 3,000 億韓元的平台（오늘의집 Ohouse，2025 年 3,215 億韓元、施工累計 GMV 破 1 兆韓元）；**台灣、新加坡、印度、印尼**處於「媒合平台＋全包連鎖」階段（100室內設計 2025 年促成逾 4,000 筆簽約；Livspace FY25 營收 Rs 1,460 crore 但淨損 16.6%；Dekoruma 2024 年售予 Blibli）；**日本、越南、泰國、菲律賓、馬來西亞、香港**的裝修數位化仍以「既有客戶網絡＋社群／搜尋」為主，專屬平台數據本輪未取得。
2. **AI／3D 設計工具已在中國成為簽單標配**：酷家樂付費企業客戶 4.7 萬家、個人付費 43.3 萬、每日數百萬次渲染，裝企與建材商以 3D 效果圖作為前置獲客工具；韓國（오늘의집「AI 端到端空間解決方案」、아파트멘터리×LG전자、Archisketch）、台灣（100室內設計免費 AI 設計工具）、越南（AiHouse、Homestyler 越南文版）皆有工具落地，但**沒有任何市場有可引用的設計師採用率調查或生產力量測數據**（缺口）。
3. **數位獲客的經濟學已被中國案例證偽「純買線索」模式**：土巴兔 2019–2021 年銷售費用占營收 56–61%、三年獲客費 6.6 億元；齊屹科技 2024 年每條線索均價 527 元人民幣（≈USD 73／TWD 2,306）且線索量年減 20%；存活者是「相鄰交易導流」（貝殼房產交易貢獻約 39% 家裝合同額）與「內容平台」（小紅書 2024 年家居家裝 GMV 年增 2.5 倍、#舊房改造 瀏覽 41.3 億次；線上觸點對家居決策影響率 >70%）。
4. **韓國是「平台信任機制」的標竿**：오늘의집 2023 年導入「施工責任保障（시공책임보장）」與公正委標準契約後施工 GMV 近倍增；2024-12-16 公正委、消費者院與 4 家平台（오늘의집、숨고、집닥、내드리오）簽訂自律協約；但平台本身 2025 年因投資施工、線下與 AI 再度轉虧（−147 億韓元），且 2025 年消費者院對「숨고」等媒合平台發布受害警示。
5. **BIM、專案管理 SaaS、預製／模組化內裝、智慧家庭的跨國可比數據極薄**：本輪僅取得貝殼「BIM 設計工具＋模組化產品」、亞廈股份（裝配式，2025 年毛利率 15.61%）、海爾三翼鳥（2024 年零售額破百億元、智家 APP MAU 1,000 萬、戶均消費 42 萬元）、奧維雲網「2025 年高端精裝房智能家居華為份額近 50%」、艾媒「49.45% 受訪者已購智能家居」、丹青社（Tanseisha）與台北若水國際 2024-07 簽 BIM 合作備忘錄等零星證據；新加坡 CORENET X、香港 BIM 規定、日本 ANDPAD 導入社数、韓國 BIM、裝配式裝修滲透率、系統櫃市占等**全部無資料**。
6. **數位履約／資金託管正在成為平台的核心價值而非附加功能**：土巴兔按節點付款託管（2022 年深圳裝企倒閉時為 200 多位業主保住 800 餘萬元）、聖都整裝銀行第三方存管、廈門三方託管案例、印尼 Sejasa「SejasaPay」、台灣住保會 2025 年履約保證 2,866 件／3.17 億元；這與 T3 指出的「跑路（먹튀／裝修蟑螂）」糾紛上升趨勢互為因果。
7. 對台灣業者的結論：**可立即部署且有海外 ROI 證據的是「3D／AI 設計 SaaS 作為簽單工具」「平台案例＋評價經營」「履約保證／第三方託管」三項**；「自建媒合平台」與「純線上買線索」在中、韓、印、印尼四地都已被驗證為燒錢且難獲利；BIM／預製／智慧家庭綁裝修則缺乏可量化 ROI，應以小規模試點而非策略投資處理。

---

## 2. 平台版圖：各市場主要消費者平台（用戶、GMV、募資、收入模式、2024–2026 狀態）

### 結論
12 市場中只有中國（齊家網、土巴兔、貝殼、酷家樂）與韓國（오늘의집）的平台有可公開比較的財務數據；台灣（100室內設計）有平台自報的媒合量；新加坡（Qanvast）、印尼（Dekoruma）兩個區域平台已分別被 Livspace 與 Blibli 收編；印度以 Livspace／HomeLane 全包連鎖取代平台；日本、越南、泰國、菲律賓、馬來西亞、香港的任務指定平台（ホームプロ、リショップナビ、SUUMO、Happynest、Recommend.my、Atap、裝修佬 DecoMan、Decor8）本輪僅有 Happynest 自報流量，其餘無資料。

### 引用發現

**中國**
- 群核科技／酷家樂（Manycore Tech／Kujiale・Coohom，00068.HK）：營收 2023／2024／2025 = 6.64／7.55／8.20 億元人民幣（2025 ≈ USD 1.14 億／TWD 35.9 億）；會計淨損 6.46／5.13／4.28 億元；2025 年經調整淨利 5,712.7 萬元（首次轉正）；訂閱收入 7.95 億元（96.9%）；毛利率 82.2%；MAU 250 萬（2024 年 270 萬，月活訪客 8,630 萬）；付費企業客戶 4.7 萬家（年付 20 萬元以上大客戶 424 家）；個人付費客戶 43.3 萬；NRR 企業 100.7%、個人 86.4%；2026-04-17 港交所上市、基石認購 37%；上市 3 個月後跌回發行價 — [新浪港股 2026-02-24](https://finance.sina.com.cn/stock/hkstock/hkzmt/2026-02-24/doc-inhnyyvp1282748.shtml)；[21 經濟網 2026-04-09](https://www.21jingji.com/article/20260409/herald/4a8ab282072f3daa5bf46a36e81fe0cc.html)；[新浪科技 2026-08-07](https://finance.sina.com.cn/tech/roll/2026-08-07/doc-inimnenp3338147.shtml)；[財聯社](https://www.cls.cn/detail/2338659)（經由 CN-A）。
- 群核 2024 年毛利率有 80.9%（[中國基金報](https://www.chnfund.com/article/AR385fcc39-1859-5917-d2f8-3a1bed2fa95f)）與 80.2%（[澎湃](https://www.thepaper.cn/newsDetail_forward_32992074)）兩種轉載；訂閱收入占比另有 98.3%、海外收入 7.4%（2024 年前 9 月）的說法 — [36 氪招股書解讀](https://www.36kr.com/p/3169957639825921)；[格隆匯](https://m.gelonghui.com/news/5304964)（經由 T2）。Frost & Sullivan 稱其 2023 年按 MAU 為全球最大空間設計平台 — [藍鯨](https://www.lanjinger.com/d/1775735430884273852)（經由 CN-A）。
- 齊屹科技／齊家網（Qeeka Home，1739.HK）：2024 年營收 10.56 億元（−11.07%；≈USD 1.47 億／TWD 46.2 億）、毛利率 39.1%（2023：41.7%）、歸母淨損 1.27 億元；2024 年銷售線索 633,769 條（−20%）、每條均價 527 元（≈USD 73／TWD 2,306）；SaaS 及行銷服務收入 3.337 億元（−20.2%）；2025H1 營收 4.232 億（−27.1%）；2026H1 營收 3.622 億（−14.4%）；市值約 2.36 億港元 — [同花順 2025-04-27](https://stock.10jqka.com.cn/20250427/c667789677.shtml)；[港交所年報 PDF](https://www.hkexnews.hk/listedco/listconews/sehk/2025/0425/2025042501676_c.pdf)；[騰訊新聞 2026-08-26](https://news.qq.com/rain/a/20260826A0BMM200)（經由 T2、CN-A）。
- 土巴兔（Tubatu）：2018–2021 年營收 5.83／6.8／6.15／6.55 億元；2021 年淨利 7,033 萬元；銷售費用占營收 2019／2020／2021 = 57.9%／56.1%／61.1%；三年獲客費 6.6 億元（≈USD 9,170 萬／TWD 28.9 億）；2022 年撤回創業板 IPO；2024–2025 財務無公開資料 — [華爾街見聞](https://wallstreetcn.com/articles/3634603)；[界面](https://www.jiemian.com/article/7679144.html)；[中國證券報](https://cs.com.cn/ssgs/gsxw/202208/t20220804_6289142.html)；[建築之窗](https://www.jianzhuzhichuang.com/cms/jianzhushixun/5095.html)（經由 T2、CN-A）。土巴兔 2026 年報告稱平台上全屋整裝占比 82.40% — [大眾網](https://m.dzplus.dzng.com/share/general/0/NEWS3468079NBYNVQOGXEHST)（經由 CN-B；平台樣本）。
- 貝殼（KE Holdings）家裝家居（被窩、聖都）：淨收入 2023／2024／2025 = 109／148／154 億元（2025 ≈ USD 21.4 億／TWD 674 億）；貢獻利潤率 2024 年 30.7%→2025 年 31.4%；2024 年 GTV 169 億元；2025Q4 收入年減 12% — [新浪 2026-03-16](https://finance.sina.com.cn/stock/estate/integration/2026-03-16/doc-inhrequs9902543.shtml)；[第一財經](https://www.yicai.com/news/102524134.html)；[澎湃](https://www.thepaper.cn/newsDetail_forward_27482182)（經由 T2、CN-A）。
- 互聯網家裝規模 4,142 億元、滲透率 20.8%（2023；定義：經線上平台獲客／成交之家裝）— [前瞻產業研究院](https://www.qianzhan.com/analyst/detail/220/240428-25c71993.html)（經由 CN-A；中低信心）。
- 好好住、被窩（獨立數據）、小紅書家裝頻道用戶數：**無資料**。

**韓國**
- 버킷플레이스 오늘의집（Bucketplace／Ohouse）：2024 年營收 2,879 億韓元（+22.3%；≈USD 2.06 億／TWD 64.8 億）、營業利益 5.78 億韓元（創業 10 年首度年度獲利，營益率 0.2%）；2025 年營收 3,215 億韓元（+11.7%；≈USD 2.30 億／TWD 72.3 億）、營業損失約 147 億韓元（投資施工、線下據點、海外、AI）；施工累計交易額破 1 兆韓元（≈USD 7.1 億／TWD 225 億）；2025 年施工交易營收成長 3.5 倍；App 下載 3,000 萬；2022 年募資 2,300 億韓元（≈USD 1.64 億／TWD 51.8 億）、估值約 2 兆韓元；無借款、現金逾 2,400 億韓元；定位「AI 端到端空間解決方案」— [아시아경제 2025](https://core.asiae.co.kr/article/2025033115492450800)；[와우테일 2026-04-14](https://wowtale.net/2026/04/14/257037/)；[벤처스퀘어](https://www.venturesquare.net/1075994/)；[오늘의집 뉴스룸](https://ohstory.io/press/pressrelease/15242)；[데모데이](https://demoday.co.kr/bm-analysis/109)；[유니콘팩토리](https://www.unicornfactory.co.kr/article/2024041211050958876)；[MTN 2022](https://news.mtn.co.kr/news-detail/2022050915405282133)；[아웃스탠딩](https://outstanding.kr/press/1887/20260414)（經由 T2、KR-A）。
- 오늘의집 2024 年綜合施工申請量年增 200%；2025 年公布平均綜合施工報價 20 坪型 4,000–5,000 萬韓元、30 坪型 5,000–6,000 萬（≈USD 35,700–42,900／TWD 112–135 萬）、40 坪型 8,000–9,000 萬 — [뉴스핌 2025-05-30](https://www.newspim.com/news/view/20250530000207)（經由 KR-B）。
- 집닥（Zipdoc）：2015 年成立之 O2O 施工比價媒合，向業者收手續費；創投（Altos、Kakao Investment、KDB 等；Series B 194 億韓元以上）；投資方部落格稱累計交易額破 3,000 億韓元（≈USD 2.14 億／TWD 67.5 億）；財務未公開（thevc.kr 付費牆；wanted.co.kr 顯示營收 59 億韓元但未標年份）— [넥스트유니콘](https://www.nextunicorn.kr/company/d091a12a4081eb88)；[빅뱅엔젤스](https://blog.bigbangangels.com/zipdoc/)；[The VC](https://thevc.kr/zipdoc)；[원티드](https://www.wanted.co.kr/company/767)（經由 KR-A、T2；低信心）。
- 아파트멘터리（Apartmentary，法人名 파이브）：高端公寓標準化整裝 D2C；2025 年營收 521.7 億韓元（≈USD 3,730 萬／TWD 11.7 億；2024 年 411.9 億）；累計募資 580 億韓元；2025-10 獲 LG전자 策略投資 — [The VC](https://thevc.kr/apartmentary)；[테크42](https://www.tech42.co.kr/%EC%95%84%ED%8C%8C%ED%8A%B8%EB%A9%98%ED%84%B0%EB%A6%AC-lg%EC%A0%84%EC%9E%90-%EC%A0%84%EB%9E%B5%EC%A0%81-%ED%88%AC%EC%9E%90-%EC%9C%A0%EC%B9%98-ai%EC%9C%B5%ED%95%A9-%EB%AA%B0%EC%9E%85%ED%98%95/)（經由 KR-A）。
- 숨고（Soomgo，生活服務媒合含裝修）：2025-07 韓國消費者院對「숨고」等服務仲介平台發布受害警示，最多類型為「失聯」 — [경향신문](https://www.khan.co.kr/article/202507011523011)（經由 KR-A／B）。

**台灣**
- 100室內設計（數字科技 Addcn，5287）：App 下載破 158 萬次；2025 年累積近 15,000 筆有效裝修需求、促成逾 4,000 筆簽約；提供免費 AI 設計工具、主推模組化裝修 — [NOWnews](https://www.nownews.com/news/6770793)；另稱 1,400 家設計公司進駐、1.7 萬件案例、每年媒合 2 萬筆需求、月訪量破 200 萬；有「全平台啟動收費」報導但費率不明 — [鉅亨網（Yahoo）2026](https://tw.stock.yahoo.com/news/%E6%88%BF%E7%94%A2-%E6%95%B8%E5%AD%97%E7%A7%91%E6%8A%80%E6%8B%93%E5%AE%A4%E5%85%A7%E8%A8%AD%E8%A8%88%E7%89%88%E5%9C%96-%E5%B9%B3%E5%8F%B0%E6%9C%88%E8%A8%AA%E9%87%8F%E7%AA%81%E7%A0%B4200%E8%90%AC%E6%AC%A1-075452062.html)；[LINE TODAY 平台比較 2026](https://today.line.me/tw/v3/article/gzXWjgz)（經由 TW-A、T2；平台自報，中信心）。該平台亦是「2025 年裝修產值逼近 5,500 億元」的推估來源 — [經濟日報](https://udn.com/news/story/7241/9245511)（非官方統計）。
- PULO 裝潢平台：營運逾 10 年、逾 10,000 位屋主選用、設計師／統包 5 關審核；自述「絕無抽成、只收媒合費用、無論成交與否」，費率未公開；服務雙北、桃園、台中、高雄、台南、新竹、南投、彰化、宜蘭 — [App Store 屋主版](https://apps.apple.com/tw/app/pulo-%E8%A3%9D%E6%BD%A2%E5%B9%B3%E5%8F%B0-%E5%B1%8B%E4%B8%BB%E7%89%88/id1160638151)；[App Store 專家版](https://apps.apple.com/tw/app/pulo-%E8%A3%9D%E6%BD%A2%E5%B9%B3%E5%8F%B0-%E5%B0%88%E5%AE%B6%E7%89%88/id1266584276)（經由 TW-A、T2；自報，低–中信心）。
- 設計家 Searchome（城邦／麥浩斯）：2008 年成立、近千位設計師、自述「每年促成逾千件合作、創造數十億商機」；2025 年數據未找到 — [LINE TODAY](https://today.line.me/tw/v3/article/gzXWjgz)；[鉅亨雜誌頁](https://news.cnyes.com/magazines/41)（經由 T2、TW-A；低信心）。
- PRO360：依平台交易資料發布室內設計費與中古屋裝潢價格區間 — [PRO360](https://www.pro360.com.tw/price/interior_design)（經由 TW-A）。幸福空間：**無資料**。
- 平台 GMV 推算（本人，TW-A 已做）：4,000 筆簽約 × 平均 100–150 萬元／案 ≈ 年 GMV 40–60 億元（≈USD 1.3–1.9 億），占 5,500 億的 1% 以下 → 平台滲透率仍低（推算，低信心）。

**新加坡／馬來西亞**
- Qanvast：2021-12 宣布、2022-04 完成由 Livspace 子公司 Interiortech Pte Ltd 取得多數股權，對外稱維持中立平台；Qanvast 亦經營馬來西亞站；Livspace 稱「透過 Qanvast 服務新加坡」，新加坡占 Livspace FY25 營收 15%（≈Rs 219 crore ≈ USD 2,550 萬／TWD 8.0 億）— [Allen & Gledhill](https://www.allenandgledhill.com/perspectives/articles/21509/acquisition-of-a-majority-stake-in-qanvast-pte-ltd-by-interiortepte-ltd)；[Southeast Asia Building](https://seab.tradelinkmedia.biz/publications/6/news/3438)；[Entrackr](https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863)（經由 T2、MY-A）。Qanvast 用戶數、費率：無資料。Hometrust：T2 子代理「未找到任何來源」。Renopedia：無資料。
- 馬來西亞：LAM 2026 年第 1 號通函要求網路推廣平台配合稽查未註冊室內設計業者，稽查委員會稱數百則廣告中僅 1 家確認為註冊業者 — [LAM（X）2026](https://x.com/LembagaArkitek/status/2065266904147939778)；[BERNAMA 2024](https://www.bernama.com/en/news.php?id=2325910)（經由 MY-A／B）；意即線上廣告／媒合平台是馬來西亞「ID 公司」的主要獲客場域。Recommend.my、Atap.co、Kaodim：無資料（MY-A 列為缺口）。

**印度**
- Livspace：FY25（2024/4–2025/3）營收 Rs 1,460 crore（+23%；≈USD 1.70 億／TWD 53.5 億）、淨損 Rs 242 crore（≈−16.6%）；印度 85%／新加坡 15%；2022 年 Series F USD 1.8 億（KKR 領投，估值逾 USD 10 億）；2025–2026 年裁員（Entrackr 稱逾 1,000 人；HRKatha 稱約 100 人）、CBO 與共同創辦人離職 — [Entrackr 2025](https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863)；[Inc42](https://inc42.com/buzz/livspaces-fy25-loss-declines-43-to-inr-243-cr/)；[Outlook Business](https://www.outlookbusiness.com/corporate/livspace-revenue-rises-23-to-1460-cr-in-fy25-losses-come-down)；[Business Wire 2022](https://www.businesswire.com/news/home/20220207005993/en)；[Entrackr 2026](https://entrackr.com/news/livspace-cbo-lalit-mittal-exits-after-co-founder-departure-and-mass-layoffs-11150871)；[HRKatha](https://www.hrkatha.com/news/layoff/100-job-cuts-at-livspace/)（經由 T2）。Livspace AI 功能：無資料。
- HomeLane（含 DesignCafe）：FY25 營業收入 Rs 748 crore（+22%；≈USD 8,700 萬／TWD 27.4 億）、淨損 Rs 111 crore；總費用 Rs 867 crore 中廣告 Rs 84 crore（≈USD 980 萬／TWD 3.1 億；≈營收 11.2%，本人計算）、材料 Rs 320 crore、人事 Rs 239 crore；FY25Q4 EBITDA 轉正 — [Entrackr](https://entrackr.com/fintrackr/homelane-records-rs-748-revenue-in-fy25-but-falls-short-of-projections-10586234)；[Franchise India](https://www.franchiseindia.com/index.php/insights/en/news/homelane-reports-22-revenue-growth-in-fy25-achieves-ebitda-profitability-in-q4.57729)；[Motilal Oswal](https://www.motilaloswal.com/news/stocks/107588)（經由 T2）。HomeLane「SpaceCraft」AI 工具：無資料。
- 組織化平台滲透：Livspace＋HomeLane 合計營收約 Rs 2,000 crore（≈USD 2.3 億）對照 Mordor 印度室內設計市場 USD 314 億，滲透率 <1%，與 Redseer「線上 <1%」說法一致；Livspace／HomeLane 市占說法互相矛盾（80%／65–70%／28%／5–7%），不建議引用 — T1 筆記推算，引 [Mordor IN](https://www.mordorintelligence.com/industry-reports/india-interior-design-market)（低信心）。

**印尼**
- Dekoruma（PT Dekoruma Inovasi Lestari）：2024-06-24 Blibli（Global Digital Niaga，Djarum 集團）以 Rp 1.16 兆（≈USD 7,160 萬／TWD 22.6 億）收購 99.83%，Dealroom 估 EV／營收 4.0x；dekoruma.com 線上商店營收 USD 920 萬（2024）；Series C1 USD 1,500 萬（Nexter Ventures、KTB Network）；曾宣布 Rp 216.8bn 募資並規劃 IPO（後放棄）；併入 Blibli 後成為「設計＋家具＋房屋買賣」平台 — [Tracxn](https://tracxn.com/d/companies/dekoruma/__yMvml0YzAJGfBB4NClfEUERCnmtJO5TKRq4i0M8IZmI)；[Dealroom](https://app.dealroom.co/companies/dekoruma)；[1001startup](https://1001startup.id/company/dekoruma)；[ecommerceDB](https://ecommercedb.com/store/dekoruma.com)；[DealStreetAsia 2021](https://media.dealstreetasia.com/stories/indonesia-dekoruma-series-c1-funding-257304)；[DailySocial 2021](https://en.dailysocial.id/post/dekoruma-announces-funding-of-2168-billion-rupiah-to-achieve-positive-ebitda-soon-and-plans-an-IPO)；[CB Insights](https://www.cbinsights.com/investor/dekoruma)（經由 ID-A、T2）。
- Fabelio（D2C 家具＋設計）：2022-10-05 破產，累計募資約 Rp 300bn（≈USD 1,850 萬）— [CNBC Indonesia](https://www.cnbcindonesia.com/tech/20221012071341-37-379004/sudah-galang-rp-300-miliar-startup-fabelio-kini-pailit)；[Bisnis](https://teknologi.bisnis.com/read/20221010/266/1586117/startup-fabelio-resmi-diputus-pailit)（經由 T2、ID-A）。
- 工程／工人媒合：Gravel 2023-12 募資 USD 1,400 萬（NEA 領投）、6,000+ 專案、20 省 — [Katadata](https://katadata.co.id/digital/startup/656d6becb3021/investor-amerika-suntik-startup-konstruksi-gravel-rp-216-miliar)；Kanggo 2025 年中月活 36,000+、服務約 30,000 棟建物（僅 Jabodetabek）— [Investor.id](https://investor.id/business/409706/pengguna-kanggo-tembus-36-ribu-layanan-perawatan-bangunan-kian-diminati)；Sejasa 累計 750,000+ 客戶、設 SejasaPay 履約帳戶 — [Sejasa](https://www.sejasa.com/)（經由 ID-A；自報）。
- 電商套裝：Tokopedia 上 studio 全裝套裝 Rp 2,499 萬–3,799 萬、客製 HPL 版 Rp 7,500 萬 — [Tokopedia](https://www.tokopedia.com/find/interior-apartemen-studio)（經由 ID-A）。

**越南**
- Happynest（Happynest Media）：家居社群＋專家媒合＋社交電商；自報月訪 400 萬、Facebook 社團 40 萬人、粉絲頁 25 萬（≈2023）；App 上線時專家檔案 1,000 件以上（2021）；2025 年與 LG 合辦 LG Architect Club；無公開 GMV／成交數 — [Happynest 介紹](https://v2.happynest.vn/gioi-thieu)；[Bongdaplus 2023](https://bongdaplus.vn/ben-ngoai-duong-piste/happynest-giup-hanh-trinh-lam-nha-cua-nguoi-viet-tro-nen-de-dang-hon-3981922305.html)；[VnExpress 2021](https://vnexpress.net/happynest-ra-mat-ung-dung-chuyen-ve-nha-o-4393392.html)；[Dân trí](https://dantri.com.vn/kinh-doanh/ung-dung-happynest-giai-quyet-nhu-cau-tim-y-tuong-tim-chuyen-gia-va-sam-noi-that-20211128204409915.htm)；[Zing](https://tech.zingnews.vn/lg-architect-club-truyen-cam-hung-cong-nghe-vao-to-am-tuong-lai-post1558482.html)（經由 VN-A；自報，中低信心）。
- 2026 年出現「數位平台協助尋找營造承包商」報導 — [VnExpress 2026](https://vnexpress.net/nen-tang-so-ho-tro-tim-nha-thau-xay-dung-5059125.html)（經由 VN-A；僅標題層級）。

**日本**
- ホームプロ（リクルート系）、リショップナビ、SUUMO リフォーム：加盟店數、累計相談件數、成約件數、抽成率——JP-A 子代理搜尋排程於配額用盡後**未取得**（缺口）。
- 可比的「線上獲客型」業者：生活堂（seikatsu-do）在リフォーム産業新聞「業種別リフォーム売上ランキング 2025」總合リフォーム店部門第 3、網路專業第 1（金額未揭露）— [生活堂公告](https://www.seikatsu-do.com/information/20251224.php)（經由 JP-A）。
- 建材商加盟網絡作為「實體平台」：LIXILリフォームショップ 549 店（2024-03）、540 店時年約 12 萬件工程 — [LIXIL トータルサービス PDF](https://bqzr2f-lts.origin.lixil.com/news/docs/202409_lrs-LTSebisu-open.pdf)；[Digital PR Platform 2023](https://digitalpr.jp/r/56840)（經由 T2）。
- 一站式中古＋翻新：リノベる「適合R住宅」2025 年度發行 410 件、請負型業者全國第 1（連續 6 年）；2023 年平均翻新價 1,360 萬日圓（≈USD 9.1 萬／TWD 286 萬） — [リノベる 2026-01 PR](https://www.renoveru.jp/hubfs/%E3%80%90PRESS%20RELEASE%E3%80%91%E3%83%AA%E3%83%8E%E3%83%99%E3%82%8B%E3%80%816%E5%B9%B4%E9%80%A3%E7%B6%9A%E5%85%A8%E5%9B%BD%E3%83%BB%E9%A6%96%E9%83%BD%E5%9C%8F1%E4%BD%8D%E3%81%AE%E8%AB%8B%E8%B2%A0%E5%9E%8B%E4%BA%8B%E6%A5%AD%E8%80%85%E3%81%AB%20%E3%80%8C%E9%81%A9%E5%90%88R%E4%BD%8F%E5%AE%85%E3%80%8D%E7%99%BA%E8%A1%8C%E4%BB%B6%E6%95%B0%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0.pdf)；[ユーザーレポート 2024](https://www.renoveru.jp/hubfs/corporate2024/pdf/20240625%E3%80%90%E3%83%97%E3%83%AC%E3%82%B9%E3%83%AA%E3%83%AA%E3%83%BC%E3%82%B9%E3%80%91%E3%80%8C%E3%83%AA%E3%83%8E%E3%83%99%E3%82%8B%E3%80%82%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%80%8D%E3%82%92%E5%85%AC%E9%96%8B.pdf)（經由 JP-A、T2）。

**香港、泰國、菲律賓**
- 香港：裝修佬 DecoMan、Decor8 用戶數——T2 列「搜尋未執行」，本輪亦無資料。唯一可引用的數位相關上市公司為梁志天設計集團（2262.HK）2025 年收入 HK$4.227 億（≈USD 5,420 萬／TWD 17.1 億）— [HKEX 2026-03-19](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0319/2026031900292.pdf)（經由 CN-B；非平台）。
- 泰國：HomePro（HMPRO）將「商品銷售＋居家服務」合併列報，Home Service 不單獨揭露 — [SET snapshot](https://lssmedia.setlink.set.or.th/2025/3M/HMPRO-3M68-ListedCompanySnapshot-EN.html)（經由 T2）；BaanLaeSuan 等平台：無資料。
- 菲律賓：Wilcon Depot 2024 年專案銷售 ₱347M（≈USD 610 萬／TWD 1.9 億，占營收約 1%）；Do-It-Wilcon ₱996M — [Inquirer Plus](https://plus.inquirer.net/?p=256738)；[Quartr](https://quartr.com/events/wilcon-depot-inc-wlcon-q4-2024_FtvIy3pe)（經由 T2）；平台：無資料。

### 推論
- 平台原型的公開財務只存在於中、韓；其共通點是**「平台若不碰施工履約，毛利率可達 40%（齊屹）但獲客成本吃掉利潤；一旦自營施工（오늘의집、齊家網 2023 年自營裝修收入 7.3 億元）毛利率下滑、轉虧」**（T2 推論，本筆記沿用）。
- 區域平台的終局是被收編：Qanvast→Livspace（2022）、Dekoruma→Blibli（2024）、好好住與被窩→貝殼體系；台灣 100室內設計隸屬數字科技分類媒合集團，亦屬「附屬於流量母體」的型態。
- 台灣平台公開數據全為自報且無 GMV／費率，依整合協議屬 C 級，只能作區間。

### 缺口
- 好好住、被窩、小紅書家裝、SUUMO／ホームプロ／リショップナビ、Hometrust、Renopedia、Recommend.my、Atap、裝修佬 DecoMan、Decor8、幸福空間、設計家 2025 年用戶／案件／GMV／費率：全部無資料。
- 오늘의집、집닥、100室內設計、PULO 的抽成率（take rate）、年度 GMV、MAU：未公開。
- Livspace／HomeLane 的線上獲客占比、AI 工具（SpaceCraft 等）：無資料。

---

## 3. AI 與 3D 設計工具：Coohom／酷家樂、Homestyler、Planner 5D、Spacely、SketchUp／Enscape／D5 Render、生成式 AI、AI 報價

### 結論
唯一有完整公開數據的工具型公司是群核科技（酷家樂／Coohom）：MAU 250 萬、付費企業 4.7 萬家、訂閱占 97–98%、毛利率 82%，證明「設計工具 SaaS」在亞洲可達上市規模且毛利結構遠優於裝修本業；韓國、台灣、越南皆有 AI 工具落地的質性證據（오늘의집 AI 端到端、아파트멘터리×LG전자、Archisketch AI、100室內設計免費 AI 工具、AiHouse／Homestyler 越南文版），但**12 市場中沒有任何一個市場有可引用的「設計師 AI／3D 採用率調查」「生產力量測」「工具定價比較」**。Homestyler、Planner 5D、Spacely、SketchUp／Enscape／D5 Render 在亞洲的用戶數：無資料。

### 引用發現
- 群核科技定位「空間智能」，每日處理數百萬次渲染、數十億次 API 調用；MAU 250 萬（2024 年 270 萬，月活訪客 8,630 萬）；付費企業客戶 4.7 萬家、年付 20 萬元以上大客戶 424 家；個人付費客戶 43.3 萬；NRR 企業 100.7%／個人 86.4% — [新浪港股 2026-02-24](https://finance.sina.com.cn/stock/hkstock/hkzmt/2026-02-24/doc-inhnyyvp1282748.shtml)；[SCMP「China's answer to Autodesk」](https://www.scmp.com/tech/tech-trends/article/3309107/chinas-answer-autodesk-manycore-bets-ai-future-spatial-intelligence)（經由 CN-A）。
- 群核訂閱收入 7.95 億元（2025，96.9%）；海外收入約 7.4%（2024 年前 9 月，即 Coohom 海外版）— [21 經濟網](https://www.21jingji.com/article/20260409/herald/4a8ab282072f3daa5bf46a36e81fe0cc.html)；[36 氪](https://www.36kr.com/p/3169957639825921)（經由 CN-A、T2）。
- 群核 2022–2025 毛利率 72.7%／76.8%／80.9%（或 80.2%）／82.2%；仍有會計淨損（2025 年 4.28 億元），研發與行銷為主要費用 — [中國基金報](https://www.chnfund.com/article/AR385fcc39-1859-5917-d2f8-3a1bed2fa95f)；[格隆匯](https://m.gelonghui.com/news/5304964)（經由 T2）。
- 酷家樂早年自稱註冊用戶 2,500 萬、設計師 800 萬（年份不明，不建議引用）— [百度百科](https://baike.baidu.com/item/%E9%85%B7%E5%AE%B6%E4%B9%90/12914547)（經由 CN-A；D 級）。
- 中國裝企／建材商以 3D 效果圖作為簽單前置工具；貝殼以「模組化產品體系、產品化樣板間、BIM 設計工具」提升設計師效率 — [新浪 2026-03-16](https://finance.sina.com.cn/stock/estate/integration/2026-03-16/doc-inhrequs9902543.shtml)（經由 CN-A；無量化效率數據）。
- 上海家裝設計師招聘樣本（2026-03）：底薪 4,000–6,500 元、簽單提成 3–7%，要求 CAD／SU（SketchUp）／PS — [牛起招聘](https://campus.niuqizp.com/job-vwk5tnatn.html)（經由 CN-B；單一樣本，低信心；為本輪唯一提及 SketchUp 的來源）。
- 韓國：오늘의집 2025 年投資 AI 高度化，定位「AI 기반 엔드투엔드 공간 솔루션」 — [벤처스퀘어](https://www.venturesquare.net/1075994/)；아파트멘터리 與 LG전자 合作「AI 融合沉浸式居住解決方案」 — [테크42](https://www.tech42.co.kr/%EC%95%84%ED%8C%8C%ED%8A%B8%EB%A9%98%ED%84%B0%EB%A6%AC-lg%EC%A0%84%EC%9E%90-%EC%A0%84%EB%9E%B5%EC%A0%81-%ED%88%AC%EC%9E%90-%EC%9C%A0%EC%B9%98-ai%EC%9C%B5%ED%95%A9-%EB%AA%B0%EC%9E%85%ED%98%95/)；本土 3D 工具 아키스케치（Archisketch）推出 AI 功能 — [Archisketch Substack](https://archisketch.substack.com/p/ai-3b0)（經由 KR-A）。
- 韓國室內設計軟體市場：2024 年 USD 1.279 億（≈TWD 40.3 億）→2030 年 USD 2.674 億，CAGR 13.1%（Grand View Research「interior design software」定義，研究機構估值，非官方）— [GVR](https://www.grandviewresearch.com/horizon/outlook/interior-design-software-market/south-korea)（經由 KR-A；低信心）。
- 韓國 AI 報價網站案例：feeldesign.ai 發布「2026 年 30 坪公寓翻修估價」（每坪 100–180 萬韓元）— [feeldesign.ai](https://www.feeldesign.ai/ko/post/30-pyeong-apartment-remodeling-estimate-2026)（經由 KR-A；商業網站，僅作「AI 估價型內容行銷已出現」之證據）。
- 台灣：100室內設計推出免費 AI 設計工具並主推模組化裝修；2026 年趨勢預期含「AI 設計工具」 — [NOWnews](https://www.nownews.com/news/6770793)；[經濟日報](https://udn.com/news/story/7241/9245511)（經由 TW-A）；TW-A 子代理明確記錄「AI／3D 工具採用率：無量化數據」。TW 查核紀錄亦指出該報導同時推廣平台 AI 工具，行銷成分高 — TW-verification。
- 越南：AiHouse（AI＋可編輯 3D，自稱 8,000 萬模型）、Homestyler（越南文介面）等工具普及；HAWA 專文討論 AI 設計；AWE 整理 15 款 AI 室內設計軟體；**無產業採用率數據** — [AiHouse](https://www.aihouse.com/vi)；[HAWA](https://hawa.vn/khi-ai-thiet-ke-noi-that/)；[AWE](https://awe.edu.vn/phan-mem-ai-thiet-ke-noi-that)（經由 VN-A）。
- 印尼：2026 年趨勢文指建築師須掌握 BIM、VR／AR，工廠端 CNC、panel saw、封邊機；AI 感測排程等智慧家庭應用 — [Immortal MG 2025-12](https://immortal-mg.com/2025/12/31/tren-arsitektur-tahun-2026-di-indonesia/)；[IDN Times](https://www.idntimes.com/life/diy/tren-desain-interior-2026-c1c2-01-k7db6-fdyklf)（經由 ID-A；趨勢文，低信心）。
- 日本：AI／3D／BIM 工具滲透——JP-A／JP-B 子代理「搜尋排程於配額用盡後未取得」；JP-B 建議「台灣團隊提供設計與 BIM／3D 後台、以日本在地 IC／IP 為前端」（為推論非數據）。
- 新加坡、香港、馬來西亞、泰國、菲律賓、印度的 AI／3D 工具採用：全部無資料。

### 推論
- 以群核數據推算的單位經濟（本人計算，僅供量級參考）：訂閱收入 7.95 億元 ÷（4.7 萬企業＋43.3 萬個人）= 平均每付費帳戶約 1,656 元／年（≈USD 230／TWD 7,250）；若全部歸於企業客戶則上限約 1.69 萬元／家／年（≈USD 2,350／TWD 7.4 萬）。真實企業 ARPU 介於兩者之間，顯示其定價是「裝企每月數百到數千元人民幣」量級的低價 SaaS，而非專業 BIM 軟體定價。
- 「AI 工具」在 2025–2026 年的實際商業用途集中於三件事：生成效果圖加速簽單（中、台）、AI 估價內容做 SEO 獲客（韓）、平台端的 AI 推薦與端到端流程（오늘의집）。沒有證據顯示 AI 已顯著改變施工端生產力。
- 毛利率 82% 但仍會計虧損、上市後跌回發行價，顯示設計 SaaS 作為「投資標的」風險不低；作為「採購項目」則成本極低（T2 已下同樣結論）。

### 缺口
- Coohom 海外（含台灣）用戶數與定價；Homestyler（易家）、Planner 5D、Spacely、SketchUp、Enscape、D5 Render、Chaos／V-Ray 在亞洲各市場的用戶數與定價。
- 任何市場的設計師 AI 採用率／情緒調查（2025）；AI 工具對設計工時、簽單率、改圖次數的量測。
- AI 報價／估算工具（中國「AI 量房」、台灣 AI 估價）的準確度與使用量。

---

## 4. BIM、數位施工管理與供應鏈數位化

### 結論
本輪**未取得任何市場針對「室內裝修工程」的 BIM 強制規定原文**（新加坡 CORENET X、香港、日本、韓國皆無資料）；能引用的是「建築確認／許可流程」層級的制度（日本 2025-04 四號特例縮小、台灣室內裝修審查、新加坡 HDB DRC、韓國行為許可），以及少數企業端 BIM 應用（貝殼、丹青社×若水）。專案管理 SaaS（ANDPAD 等）導入數據無資料。供應鏈數位化與資金託管方面，中國（貝殼集採、土巴兔節點付款、聖都銀行存管）、印尼（SejasaPay、Mitra10 全通路）、台灣（住保會履約保證）有可引用案例。

### 引用發現

**BIM 與審查流程**
- 日本：建築基準法 2025-04-01 起「四號特例縮小」，階數 2 以上或總樓地板面積逾 200 ㎡之建物（含大規模修繕・模様替）須取得建築確認、由建築士設計監理；法定審查期由 7 日改為 35 日 — [国土交通省 PDF](https://www.mlit.go.jp/common/001500388.pdf)；[青森県](https://www.pref.aomori.lg.jp/soshiki/kendo/sh-seibi/shimokita_kijunhou_kaisei.html)；[藤岡市 PDF](https://www.city.fujioka.gunma.jp/material/files/group/26/foufg.pdf)；[ANDPAD 專欄](https://andpad.jp/columns/0086)（經由 T3、JP-B）。ANDPAD 在本專案中僅以法規解說專欄形式出現，其導入社数、用戶數：無資料。
- 日本×台灣 BIM：丹青社（Tanseisha）與台北「若水國際」2024-07 簽署 MOU 強化 BIM 生產體制 — [共同通信 PR Wire](https://kyodonewsprwire.jp/release/202407053219)（經由 TW-B）。
- 中國：貝殼以 BIM 設計工具、模組化產品體系提升設計師效率 — [新浪](https://finance.sina.com.cn/stock/estate/integration/2026-03-16/doc-inhrequs9902543.shtml)（經由 CN-A）；涉及主體／承重結構變動時須由原設計單位或具資質設計單位出具方案（建設部 110 號令）— [深圳法規庫](https://www.sz.gov.cn/cn/xxgk/zfxxgj/zcfg/content/post_8966865.html)（經由 CN-B）。
- 新加坡：HDB 屋主須透過 DRC 承包商申請裝修許可；私宅 building works 須 QP＋BCA；MTI 2024-05、2025-02 國會答覆維持 CaseTrust 自願制 — [HDB](https://www.hdb.gov.sg/residential/living-in-an-hdb-flat/renovation/applying-for-approval)；[MTI 2024](https://mti.gov.sg/Newsroom/Parliamentary-Replies/2024/05/Written-reply-to-PQs-on-disputes-arising-from-Interior-Design-and-Renovation-firms)；[MTI 2025](https://www.mti.gov.sg/Newsroom/Parliamentary-Replies/2025/02/Written-reply-to-PQ-on-consumer-protection-for-customers-of-non-accredited-renovation-contractors)（經由 T3）。**CORENET X 對室內工程的 BIM 提交要求：無資料**。
- 台灣：室內裝修圖說審核應於收件 7 日內完成；審查規費簡易案約 NT$5,000–7,500、建築師簽證約 NT$2–4 萬、代辦 NT$6–12 萬起；國土署 2026-04-14 澄清「2026 裝修新制須先申請才能開工」報導不實 — [全國法規資料庫](https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0070148)；[Searchome](https://www.searchome.net/article.aspx?id=76546)；[中央社 2026-04-14](https://www.cna.com.tw/news/ahel/202604140322.aspx)（經由 T3）。台灣裝修審查之 BIM 要求：無資料。
- 韓國：拆除非承重牆、陽台擴建須向區廳取得「行為許可／申報」並附建築師蓋章之結構安全確認書 — [법제처 easylaw](https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=1222&ccfNo=2&cciNo=1&cnpClsNo=1)（經由 KR-B）。韓國 BIM 義務化對室內工程之適用：無資料。
- 印尼：趨勢文提及 BIM、VR／AR 為建築師必備，但住宅施工仍以傳統工法為主 — [Immortal MG](https://immortal-mg.com/2025/12/31/tren-arsitektur-tahun-2026-di-indonesia/)（經由 ID-A；低信心）。

**數位履約、付款節點與資金託管**
- 中國：家裝公司常在簽約或開工前收取總價 6 成以上預付款；土巴兔平台採「按施工節點付款」託管，2022 年深圳大型裝企倒閉時為 200 多位業主保住 800 餘萬元（≈USD 111 萬／TWD 3,500 萬）— [澎湃 2024](https://www.thepaper.cn/newsDetail_forward_27769661)；聖都整裝 2025 年在成都／青島上線銀行第三方資金存管 — [四川在線（推廣）](https://cbgc.scol.com.cn/news/7838213)；廈門裝企停工案中簽三方託管協議之業主約 20 萬元託管款保住 — [揚子晚報 2025-12](https://www.yzwb.net/news/ch/202512/t20251222_303120.html)；住范兒 2025-06 資金鏈斷裂、京滬 800+ 工地停工 — [鈦媒體](https://www.tmtpost.com/7644935.html)（經由 CN-B）。
- 中國政府端數位平台：北京「京煥新」家裝一體化平台整合補貼政策、裝企方案與農行消費信貸 — [澎湃](https://m.thepaper.cn/detail/30044835)（經由 CN-B）。
- 韓國：오늘의집 2023 年導入「시공책임보장 서비스」與標準契約後施工交易額近倍增 — [데모데이](https://demoday.co.kr/bm-analysis/109)；2024-12-16 公正委＋소비자원＋4 平台（오늘의집、숨고、집닥、내드리오）簽「정보제공 강화 및 분쟁해결 자율협약」：平台標示「전문건설업」徽章、每季核對登記、推廣標準契約書、提示 ≥1,500 萬韓元委託無登記業者難獲法律保護 — [korea.kr](https://www.korea.kr/briefing/pressReleaseView.do?newsId=156665860&pWise=sub&pWiseSub=C2)；[뉴시스](https://www.newsis.com/view/NISX20241216_0002998493)（經由 T3）；KCA 2022 年調查 8 家品牌／平台，4 家平台中僅 1 家（오늘의집）引導使用公正委標準契約 — [파이낸셜뉴스](https://www.fnnews.com/news/202204261201348830)（經由 KR-B）。
- 台灣：住宅消費者保護協會 2025 年執行住保履約 2,866 件、金額 NT$317,301,028（≈USD 1,007 萬）— [理財周刊](https://www.moneyweekly.com.tw/_Article?AID=247503)（經由 TW-A）；國土署 2025-11 定型化契約草案：審閱期 ≥5 日、保固 1 年（尚未施行）— [國土署 PDF](https://www.nlma.gov.tw/uploads/files/4a4f5b6c19d35226adf133a9a2bde45d.pdf)（經由 T3）。
- 印尼：Sejasa 設 SejasaPay 履約帳戶 — [Sejasa](https://www.sejasa.com/)（經由 ID-A）。
- 日本：裝修瑕疵保險（リフォーム瑕疵保険）2025 年度 4,496 件（−3.6%）— [リフォーム産業新聞摘要](https://www.fujisan.co.jp/product/1281683407/b/2808733/)（經由 JP-B；非數位機制，但為履約保障基礎設施）。

**材料採購數位化**
- 貝殼家裝約 80% 主材、60% 輔材採全國或地方集採；職業化項目經理月均接單量年增逾 100% — [新浪](https://finance.sina.com.cn/stock/estate/integration/2026-03-16/doc-inhrequs9902543.shtml)；[瑞財經](https://www.rccaijing.com/news-7307953023459456534.html)（經由 T2、CN-A）。
- 印尼 CSAP（Mitra10）2026 年策略主軸「全通路（omnichannel）」、以部落格內容行銷翻修估價 — [Industry.co.id](https://www.industry.co.id/read/152024/csap-catat-pendapatan-rp175-t-di-2025-bagi-dividen-meski-daya-beli-lesu)；[Mitra10 Blog](https://www.mitra10.com/blog/biaya-renovasi-rumah-per-meter)（經由 ID-A）。
- 日本：建材・住設流通商渡辺パイプ 2025 年營收逾 4,000 億日圓（リフォーム産業新聞ランキング第 1）— [Fujisan 目錄](https://www.fujisan.co.jp/product/1281683407/b/2630241/)（經由 JP-A；非數位平台）。
- 台灣、韓國、新加坡、印度、越南、馬來西亞、泰國、菲律賓、香港之建材 B2B 採購平台：無資料。

### 推論
- 跨國共通的「數位化最先落地點」不是 BIM 而是**付款節點與資金託管**，因為它直接回應各市場最大的糾紛類型（韓國瑕疵修補 56.9%、中國預付 6 成、台灣裝修蟑螂）。
- 法規層面，日本 2025 年四號特例縮小與台灣室內裝修審查都在拉高「圖說」要求，為 BIM／3D 出圖創造合規需求，但本輪沒有任何量化證據顯示室內工程端的 BIM 採用率。

### 缺口
- CORENET X（新加坡）、香港 BIM 規定、韓國 BIM 義務化、日本 BIM 補助對室內裝修工程的適用範圍。
- ANDPAD、Photoruction、韓國／台灣工程管理 SaaS 的導入家數與定價。
- 各市場第三方資金託管的法定地位與普及率；中國 2025 年全國性家裝資金監管新規（CN-B 未找到）。

---

## 5. 預製與模組化內裝

### 結論
本輪在 12 市場中**沒有任何官方或協會的預製／模組化內裝滲透率數據**。可引用者僅：中國公裝龍頭亞廈股份主打裝配式（2025 年毛利率 15.61%，高於同業均值 13.28%）、貝殼模組化產品體系、土巴兔平台整裝占比 82.4%（平台樣本）、印度 Livspace／HomeLane 以模組化櫃體標準化交付、台灣 100室內設計主推「模組化裝修」、韓國新建公寓普遍含廚櫃衛浴地板之建商配套；日本ユニットバス、新加坡 PPVC／DfMA 對室內之影響、台灣系統櫃市占、韓國빌트인滲透率：全部無資料。

### 引用發現
- 中國：亞廈股份（002375.SZ）主打裝配式綠色建築，2025 年營收 91.18 億元（−24.87%）、毛利率 15.61%（行業 23 家均值 13.28%）— [新浪 2026-04-30](https://finance.sina.cn/2026-04-30/detail-inhwhene7094454.d.html)；[同花順](https://news.10jqka.com.cn/20260428/c676320986.shtml)（經由 CN-A）。CN-A 子代理明確記錄「裝配式裝修滲透率無官方數字」。
- 中國：貝殼「模組化產品體系、產品化樣板間」 — [新浪](https://finance.sina.com.cn/stock/estate/integration/2026-03-16/doc-inhrequs9902543.shtml)；土巴兔 2026 年報告全屋整裝占比 82.40%、局部改造小幅收縮 — [大眾網](https://m.dzplus.dzng.com/share/general/0/NEWS3468079NBYNVQOGXEHST)（經由 CN-A、CN-B；平台樣本偏差）。
- 中國政策面：2025 年 9 月工信部等 6 部門《建材行業穩增長工作方案（2025—2026 年）》支持綠色建材納入以舊換新 — [觀研天下轉述](https://www.chinabaogao.com/jingzheng/202604/790396.html)（經由 CN-B）；「裝配式裝修」專項政策 2025 年版原文：未取得。
- 中國定制家居（系統櫃對應品類）2025 年全面衰退：歐派約 172 億元（−9%，門店淨減 468 家）、志邦 43.57 億（−17.14%）、索菲亞 2025H1 45.51 億（−7.7%）、尚品宅配 36 億（−6%）；A 股定制家居 8 家營收下滑 — [新浪 2026-05-12](https://news.sina.cn/2026-05-12/detail-inhxrshc1334104.d.html)；[證券之星](https://stock.stockstar.com/SS2026062400022292.shtml)；[每經](https://www.nbd.com.cn/articles/2025-08-27/4034678.html)（經由 CN-B）。
- 印度：Livspace、HomeLane 以「自有展示中心＋模組化櫃體＋自有或協力工班」標準化交付，仍處虧損；HomeLane FY25 材料費 Rs 320 crore（占總費用 37%）— [Entrackr](https://entrackr.com/fintrackr/homelane-records-rs-748-revenue-in-fy25-but-falls-short-of-projections-10586234)（經由 T2）。
- 台灣：100室內設計主推模組化裝修；2026 年趨勢含「模組化裝修」 — [NOWnews](https://www.nownews.com/news/6770793)；[經濟日報](https://udn.com/news/story/7241/9245511)；三商美福（系統家具）提供一站式裝修＋最高 300 萬元七年期貸款 — [商周廣編](https://www.businessweekly.com.tw/business/indep/1005275)（經由 TW-A）。TW-A／TW-B 子代理記錄「系統櫃、廚具、衛浴市場規模與市占：未找到」「預製／模組化施工滲透率：未找到量化數據」。
- 韓國：新建公寓普遍含廚櫃、衛浴、地板、窗框等基本內裝，建商提供付費「옵션（選配）」；選配滲透率或金額統計：缺口 — KR-A §5（無獨立 URL）。四大建材／家具集團（한샘 리하우스、LX Z:IN、현대리바트 집테리어、KCC 홈씨씨）以標準化套裝＋經銷展示館為主軸；한샘 Rehaus 2026Q2 單季 1,660 億韓元（+12.8%）— [네이트 2026-08-10](https://m.news.nate.com/view/20260810n29818)（經由 KR-A）。
- 日本：ユニットバス／システムキッチン滲透率——JP-A／B 子代理「預鑄／模組化未取得」；住設三雄（LIXIL、TOTO、Panasonic→YKK）主導廚衛門窗，2024–2026 年連番調價 8–15%（LIXIL 2024-04 馬桶 +8%、磁磚 +13%；2026 年最高 +15%；TOTO 2026-12 衛生陶器 +13%）— [LIXIL 2023-11-09 PDF](https://newsroom.lixil.com/hubfs/newsroom/PDF/JapanComms/20231109_PriceRevision.pdf)；[LOGI-TODAY](https://www.logi-today.com/952073)；[交換できるくん](https://www.sunrefre.jp/sumutano/housing-equipment/17415/)（經由 JP-B）；YKK 2026-03-31 完成收購 Panasonic Housing Solutions 80%（PHS 2025/3 期營收 4,795 億日圓）— [Panasonic HD](https://holdings.panasonic/content/dam/holdings/jp/ja/corporate/investors/pdf/jn260331-2.pdf)（經由 JP-A）。
- 印尼：預製／模組化主要討論於建築結構（預製板、模組結構），住宅施工仍以傳統工法為主 — [Immortal MG](https://immortal-mg.com/2025/12/31/tren-arsitektur-tahun-2026-di-indonesia/)（經由 ID-A）；Tokopedia 上可購買 studio 全裝套裝 Rp 2,499 萬–7,500 萬 — [Tokopedia](https://www.tokopedia.com/find/interior-apartemen-studio)（經由 ID-A；模組化套裝商品化之證據）。
- 越南：VN-A 子代理「搜尋結果無越南裝修模組化的具體數據」；XHOME 自有工廠（河內東英 Nguyên Khê 工業區）自製櫃體一條龍 — [XHOME Profile 2025](https://xhomesg.com.vn/wp-content/uploads/2025/05/XHOME-Profile-2025.pdf)（經由 VN-A）。
- 新加坡（PPVC／DfMA 對室內之影響）、香港、馬來西亞（IBS）、泰國、菲律賓：無資料。

### 推論
- 「模組化」在亞洲裝修業的實際落點是**櫃體與廚衛套裝（系統櫃／定制家居／ユニットバス／빌트인）**，而非整體裝配式裝修；但中國定制家居龍頭 2025 年營收下滑 6–17%、利潤下滑 23–47%，顯示模組化本身不保證利潤，需靠通路（貝殼集採、한샘經銷館）支撐。
- 人力成本是各市場共同的模組化驅動力（日本勞務單價連 14 年上調、韓國技能人力平均 51.7 歲、中國農民工 50 歲以上 32%、台灣技術工日薪升至 4,000–5,000 元），但沒有市場提供「模組化降低現場工時 X%」的量化證據。

### 缺口
- 各市場預製／裝配式內裝滲透率（中國住建部口徑、日本ユニットバス出貨量、新加坡 BCA DfMA 對室內之規定、台灣系統櫃市占與市場規模、韓國빌트인／옵션滲透率、馬來西亞 IBS）。
- 模組化對成本／工期的量化影響。

---

## 6. 智慧家庭整合：Haier 三翼鳥、Xiaomi、Samsung SmartThings、LIXIL、Panasonic 與裝修綁售

### 結論
只有中國有可量化的「智慧家庭×整裝」證據：海爾三翼鳥（場景品牌）2024 年零售額破百億元、智家 APP MAU 1,000 萬、2024 年新增 1,556 家門店、戶均消費 42 萬元；奧維雲網指 2025 年高端精裝房智能家居華為份額近 50%；艾媒調查 49.45% 受訪者已購智能家居；2025 年家裝廚衛「煥新」國補把智能家居列為五大補貼類之一，2026 年國補保留「智能產品」但家裝類移出。韓國（아파트멘터리×LG전자）、越南（Happynest×LG Architect Club、Vietbuild 2025 智慧家居攤位最吸睛）、台灣（櫻花「AI 智能廚電」）有質性證據；Samsung SmartThings、Xiaomi、LIXIL、Panasonic 智慧家庭與裝修綁售之滲透率：全部無資料。

### 引用發現
- 海爾三翼鳥：2024 年零售額破百億元（≈USD 13.9 億／TWD 438 億）；智家 APP MAU 1,000 萬（+35%）；2024 年新增 1,556 家門店；2025H1 新增 185 家家電家居融合店；營收仍以電器銷售為主 — [新浪科技 2025-01-20](https://finance.sina.com.cn/tech/roll/2025-01-20/doc-inefrnxv9444188.shtml)；[中國日報](https://caijing.chinadaily.com.cn/a/202501/20/WS678e1416a310be53ce3f290f.html)；[騰訊 2024-07](https://news.qq.com/rain/a/20240718A02A6J00)（經由 CN-A；企業自報，中信心）。
- 三翼鳥「場景」整裝戶均消費 42 萬元（≈USD 5.8 萬／TWD 184 萬；高端家電家居融合口徑）— [界面](https://www.jiemian.com/article/6485853.html)（經由 CN-A）。
- 奧維雲網（AVC）：2025 年高端精裝房智能家居華為份額近 50% — [199IT](https://www.199it.com/archives/1812063.html)（經由 CN-A；精裝房＝建商交付口徑，2025 年 1–4 月精裝 11.39 萬套、年減 29.9%）。
- 艾媒諮詢《2025 年中國家居市場消費行為調查》：49.45% 受訪者已購買智能家居 — [艾媒](https://report.iimedia.cn/tag/家居家装)（經由 CN-B；市調，中信心）。
- 中國補貼：2025 年家裝廚衛「煥新」補貼五大類含「智能家居」與「居家適老化改造」，上限售價 15%、1 級能效 20%、適老化 30%（商辦消費函〔2025〕29 號）— [中國政府網](https://www.gov.cn/zhengce/zhengceku/202501/content_7001494.htm)；2026 年國補僅四類（汽車報廢、汽車置換、家電數碼、智能產品），家裝移出；黑龍江 2026-04-18 起對 7 類廚衛智能產品地方補貼 — [新華網 2026-01-02](https://www.news.cn/politics/20260102/8280c115602841078b65d8f5176b239c/c.html)；[中國家電網](https://news.cheaa.com/2026/0427/654595.shtml)（經由 CN-A）。
- 韓國：아파트멘터리 2025-10 獲 LG전자 策略投資、合作「AI 融合沉浸式居住解決方案」 — [테크42](https://www.tech42.co.kr/%EC%95%84%ED%8C%8C%ED%8A%B8%EB%A9%98%ED%84%B0%EB%A6%AC-lg%EC%A0%84%EC%9E%90-%EC%A0%84%EB%9E%B5%EC%A0%81-%ED%88%AC%EC%9E%90-%EC%9C%A0%EC%B9%98-ai%EC%9C%B5%ED%95%A9-%EB%AA%B0%EC%9E%85%ED%98%95/)（經由 KR-A）。Samsung SmartThings 與裝修綁售：無資料。
- 越南：Vietbuild 2025 河內展上智慧家居（nhà thông minh）攤位最吸引人潮，參展品牌含 Hunonic、Rangos、Homegy 等 — [Mekong ASEAN](https://mekongasean.vn/cac-gian-hang-giai-phap-nha-thong-minh-hut-khach-tai-vietbuild-2025-42065.html)；[Nhân Dân](https://nhandan.vn/ocop/nhung-xu-huong-cong-nghe-noi-bat-tai-trien-lam-quoc-te-vietbuild-ha-noi-2025-post866246.html)（經由 VN-B）；Happynest 2025 年與 LG 合辦 LG Architect Club（30 名以上建築師）— [Zing](https://tech.zingnews.vn/lg-architect-club-truyen-cam-hung-cong-nghe-vao-to-am-tuong-lai-post1558482.html)（經由 VN-A）。
- 台灣：櫻花以「AI 智能廚電」與節能產品為成長動能 — [優分析](https://uanalyze.com.tw/articles/8096948742)（經由 TW-A）；智慧家庭與裝修綁售滲透率：無資料。
- 印尼：2026 年趨勢文提及感測器自動調燈與空調、AI 排程植生牆 — [IDN Times](https://www.idntimes.com/life/diy/tren-desain-interior-2026-c1c2-01-k7db6-fdyklf)；[DGA Interior](https://www.dga-interior.com/blog/tren-desain-interior-2026)（經由 ID-A；趨勢文）。
- 日本：LIXIL、Panasonic（→YKK）智慧住設綁裝修：JP-A／B 未取得；僅有價格調整與併購資訊（見 §5）。
- 新加坡、香港、馬來西亞、泰國、菲律賓、印度：無資料。

### 推論
- 「智慧家庭×裝修」在亞洲唯一被證明可規模化的路徑是**家電品牌以自有門店導流整裝**（三翼鳥 1,556 家新店＋智家 APP 1,000 萬 MAU），本質是 T2 所稱「相鄰交易流量再利用」，而非裝修公司自行綁售 IoT。
- 補貼是中國智慧家庭滲透的關鍵外力；2026 年家裝類退出國補後，智慧家庭補貼轉由地方自辦，滲透動能可能放緩（推論）。

### 缺口
- Samsung SmartThings、Xiaomi、LIXIL、Panasonic、LG ThinQ 在裝修案中的綁售率；各市場智慧家庭在翻修案中的滲透率；三翼鳥 2025 全年數據。

---

## 7. 數位獲客：社群／平台 vs 轉介的占比、每線索成本、網紅／設計師創作者模式

### 結論
可量化的獲客數據集中在中國與韓國。中國：線上觸點對家居決策影響率 >70%、典型路徑「抖音看到→小紅書搜效果與避坑→論壇口碑→門店體驗談價」；小紅書 2024 年家居家裝 GMV 年增 2.5 倍、#舊房改造 瀏覽 41.3 億次；被窩抖音直播全年有效線索逾 300 萬（自報）；每線索成本唯一基準是齊屹科技 2024 年均價 527 元人民幣；土巴兔銷售費用率 56–61%。韓國：三份消費者調查顯示入口網站部落格 42.2–51.5%、SNS／YouTube 32.5–39.9%、裝修 App／平台 31.1–36.8% 為主要資訊來源，65.3% 用過線上裝修平台但僅 22.9% 透過平台實際發包。台灣、越南、馬來西亞、印尼、印度僅有質性或推算證據；日本、新加坡、香港、泰國、菲律賓無資料。沒有任何市場有 Instagram／YouTube／TikTok／LINE／Facebook 的「裝修線索占比」官方或協會統計。

### 引用發現

**中國**
- 《2025 中國家居消費者決策鏈路白皮書》：線上觸點對決策影響率 >70%，線下體驗為最後拍板；典型路徑「抖音看到→小紅書搜效果與避坑→論壇口碑→門店體驗談價」 — [36 氪](https://www.36kr.com/p/3785899311012873)（經由 CN-B）。
- 增長黑盒調研（約 5,000 名消費者）：超過半數決策週期 2 週以上；六成以上購買前比較 6 個以上品牌 — [數英](https://www.digitaling.com/articles/1441033.html)（經由 CN-B）。
- 小紅書：2024 年家居家裝賽道 GMV 年增 2.5 倍；2025 年前 5 個月超過 30 位家居家裝博主單月漲粉 10 萬+ — [騰訊新聞 2025-06-12](https://news.qq.com/rain/a/20250612A05SKV00)；#舊房改造 話題瀏覽量超 41.3 億次（2025-03），年輕用戶拿筆記截圖找設計師 — [搜狐](https://m.sohu.com/a/1037767125_406598/)（經由 CN-A、CN-B）。
- 被窩抖音直播獲客：服務商稱全年有效線索超 300 萬個（自報）— [數英](https://www.digitaling.com/projects/285641.html)；聖都整裝透過官網、抖音、今日頭條、微信、天貓多渠道觸達 — [網易](https://www.163.com/dy/article/JVUFR0GC05118O92.html)（經由 CN-A）。
- 裝企獲客兩類：抖音／小紅書發布工地實景與完工案例吸引自然流量；平台付費投放 — [網易](https://www.163.com/dy/article/KVGIUMCA0552XWVG.html)（經由 CN-A）。
- 每線索成本：齊屹科技 2024 年每條線索均價 527 元（≈USD 73／TWD 2,306）、線索 633,769 條（−20%）— [同花順](https://stock.10jqka.com.cn/20250427/c667789677.shtml)（經由 T2；A 級財報轉述）。
- 土巴兔：銷售費用占營收 2019／2020／2021 = 57.9%／56.1%／61.1%；三年獲客費 6.6 億元 — [華爾街見聞](https://wallstreetcn.com/articles/3634603)；[建築之窗](https://www.jianzhuzhichuang.com/cms/jianzhushixun/5095.html)（經由 T2、CN-A）。
- 貝殼：2022Q4 房產交易為家裝貢獻約 39% 合同額；截至 2022 年底活躍用戶 3,660 萬 — [21 經濟網 2023](https://www.21jingji.com/article/20230318/herald/e28a277c5184a40ee1804a3896d521ba.html)（經由 CN-A）。
- 低價引流套路：線上平台精準推送低價廣告、以「全包」「零增項」降低戒心，簽約後逐步加碼 — [澎湃轉法治日報](https://www.thepaper.cn/newsDetail_forward_32020018)（經由 CN-B）。
- 家居賣場導流式微：居然之家、紅星美凱龍 2025 年營收各減 14–16% — [新浪](https://finance.sina.com.cn/stock/relnews/hk/2026-04-07/doc-inhtrqch3735553.shtml)（經由 CN-A）。

**韓國**
- THE LIVING 自辦調查（樣本偏社群用戶）：2,680 名受訪者中 65.3% 使用過線上裝修平台／商城；42.4% 只用平台比價、22.9% 透過平台實際發包 — [더리빙 2680 명](https://www.theliving.co.kr/news/articleView.html?idxno=21707)；3,198 人：資訊來源入口網站部落格 42.2%、線上平台 31.1% — [더리빙 3198 명](https://www.theliving.co.kr/news/articleView.html?idxno=22216)；1,962 人：YouTube・Instagram 等 SNS 39.9%、Naver 等入口搜尋 38.7% — [더리빙 1962 명](https://www.theliving.co.kr/news/articleView.html?idxno=23807)；3,160 人：47.6% 偏好委託專業公司 — [더리빙 3160 명](https://www.theliving.co.kr/news/articleView.html?idxno=23071)（經由 KR-A、KR-B；線上社群樣本，中信心）。
- KiwiSurvey 2023：資訊蒐集管道入口網站搜尋 51.5%、裝修 App 36.8%、YouTube 32.5%、網站 19.3%，親友推薦居次 — [KiwiSurvey](https://kiwisurvey.kr/report/detail?id=85)（經由 KR-A）。
- 엠브레인 트렌드모니터 2025（1,000 人）：自助裝修（셀프 인테리어）關注度 68.9% — [트렌드모니터](https://www.trendmonitor.co.kr/tmweb/trend/allTrend/detail.do?bIdx=3303&code=0401&trendType=CKOREA)（經由 KR-B）。
- 오늘의집 2025 年搜尋關鍵字結算：「折扣活動」搜尋量大增 — [오늘의집 뉴스룸](https://ohstory.io/press/pressrelease/14717)（經由 KR-B）。
- 平台糾紛：KCA 2025-07 對「숨고」等平台發布受害警示，清潔與室內裝修約占平台糾紛一半 — [경향신문](https://www.khan.co.kr/article/202507011523011)（經由 KR-B）；律師整理詐騙三型含「SNS 假評價」 — [로톡](https://www.lawtalk.co.kr/posts/118955)（經由 KR-B）。

**台灣**
- 100室內設計 2025 年近 15,000 筆有效需求、逾 4,000 筆簽約；屋主預算分布 >50% 落在 50–200 萬元、35% 在 50 萬元以下 — [NOWnews](https://www.nownews.com/news/6770793)（經由 TW-A）。
- TW-A 推算：平台促成年 GMV 約 40–60 億元，占 5,500 億的 1% 以下；B2B 商業空間仍以建商、租戶代表與專業顧問（CBRE、C&W、Colliers、JLL）主導，平台滲透低。
- 零售一站式：三商美福設計＋家具＋貸款 — [商周廣編](https://www.businessweekly.com.tw/business/indep/1005275)；特力屋以安裝／裝修服務對抗電商 — [科技新報 2026-09](https://finance.technews.tw/2026/09/06/how-tlw-can-return-revenue-and-profit-to-growth/)；預售屋「客變」階段裝修已成獨立通路 — [工商時報 2025-11-19](https://www.ctee.com.tw/news/20251119700015-431001)（經由 TW-A）。
- 台灣屋主裝修決策歷程、資訊來源（平台／社群／仲介）調查：TW-B 子代理「未取得」（缺口）。

**越南**
- 社群規模：Facebook 7,900 萬用戶（Meta 廣告數據）、Zalo 月活 7,830 萬、TikTok 成長最快（+9.9% YoY）— [Elite Asia 2026](https://www.eliteasia.co/top-digital-and-social-media-trends-in-vietnam-in-2026/)；[Statista](https://www.statista.com/statistics/941843/vietnam-leading-social-media-platforms/)；TikTok 內容已催生室內裝飾新職種（內容創作者／帶貨）— [Diễn đàn Doanh nghiệp](https://diendandoanhnghiep.vn/tiktok-de-ra-viec-moi-cho-linh-vuc-trang-tri-noi-that-10051203.html)（經由 VN-A）。
- 業者獲客手法（行銷公司整理）：Facebook／Google 廣告、Zalo OA、TikTok 短影音、與建商／仲介合作、展廳體驗、舊客轉介 — [CleverAds](https://cleverads.vn/blog/10-cach-tiep-can-khach-hang-noi-that/)；[Giải pháp Web](https://giaiphapweb.vn/tim-kiem-khach-hang-noi-that/)（經由 VN-A；無占比）。
- 建商通路：毛胚／基本完成交屋制度使「交屋即裝修」成為必然，建商完成品比毛胚貴 10–30% — [Tuổi Trẻ／PLO](https://tuoitre.vn/plo/mua-chung-cu-nen-chon-nha-giao-tho-hay-hoan-thien-109586696.htm)（經由 VN-A）。

**印度、印尼、馬來西亞、日本**
- 印度 HomeLane FY25 廣告費 Rs 84 crore ≈ 營收 11.2%（本人計算）；Livspace 行銷費用分項：無資料 — [Entrackr](https://entrackr.com/fintrackr/homelane-records-rs-748-revenue-in-fy25-but-falls-short-of-projections-10586234)（經由 T2）。
- 印尼：ID-A 子代理推論「平台滲透率仍低（Kanggo 3.6 萬月活 vs 數千萬戶），獲客主力仍是口碑／工班」；社群媒體（Instagram、TikTok）獲客比例無量化資料。
- 馬來西亞：LAM 2026 年平台稽查顯示線上廣告平台是未註冊業者的主要獲客管道 — [LAM（X）](https://x.com/LembagaArkitek/status/2065266904147939778)（經由 MY-A）。
- 日本：住宅翻修獲客以「建商／住設品牌既有客戶（OB 顧客）網絡」「中古仲介＋翻新一站式」「網路見積平台」三路並行；積水ハウス、大和ハウス、住友林業翻修子公司營收主要來自自家建物既有屋主 — [リクルートエージェント 住友林業ホームテック](https://www.r-agent.com/company/12495/)；MLIT 令和 6 年度住宅市場動向調查顯示網路資訊蒐集比重持續上升，但細項未取得 — [MLIT](https://www.mlit.go.jp/report/press/house02_hh_000228.html)（經由 JP-A）；上門推銷（點檢商法）諮詢 2023／2024／2025 年度 11,879／9,839／5,544 件 — [国民生活センター](https://www.kokusen.go.jp/soudan_topics/data/reformtenken.html)（經由 JP-B；為「非數位獲客」之負面指標）。
- 新加坡、香港、泰國、菲律賓：無資料。

### 推論
- 可比的「每線索成本」只有齊屹 527 元人民幣；若以中國全國平均客單值 16.65 萬元（2023）與常見線索→簽約轉化率假設計算 CAC，需要未取得的轉化率數據，故本筆記不推算。
- 韓國三份調查一致顯示「搜尋／部落格」與「SNS／YouTube」各占約四成、平台約三成，且「用平台比價」遠多於「用平台發包」，意即平台的實際角色是**資訊與比價入口**，簽約仍回到業者。
- 中國「設計師創作者」模式（小紅書博主單月漲粉 10 萬+、用戶拿筆記找設計師）是 12 市場中唯一有流量數據的創作者經濟證據；台灣、韓國雖有 YouTube／Instagram 設計師頻道，但無量化資料。

### 缺口
- 各市場「首次接觸管道」調查（朋友推薦／平台／賣場／社群）2025 年版；Instagram／YouTube／TikTok／LINE／Facebook 裝修線索占比；CPL 基準（除齊屹外）；貝殼、三翼鳥投放占比與 CAC；台灣 100室內設計、PULO 的線索成本與轉化率。

---

## 8. 對台灣業者的啟示：現在可部署的工具／平台與 ROI 證據

### 結論
依 12 市場證據，台灣業者「現在就能部署且有海外 ROI 證據」的只有三類：(1) 3D／AI 設計 SaaS 作為簽單工具（酷家樂模式：低價訂閱、82% 毛利代表供應商有空間降價搶客）；(2) 在既有平台（100室內設計、PULO、設計家、社群）經營案例與評價，而非自建平台（中、韓、印、印尼皆證明自建平台燒錢）；(3) 履約保證／第三方託管／節點付款作為信任產品（오늘의집施工 GMV 近倍增、土巴兔託管保住 800 萬元、住保會 2025 年 2,866 件）。BIM、裝配式、智慧家庭綁售則缺乏可量化 ROI，建議以試點處理。詳細啟示見 §11。

### 引用發現（本節只彙整，證據 URL 見 §2–§7）
- 可部署工具的成本量級：酷家樂平均每付費帳戶約 1,656 元人民幣／年（本人以訂閱收入÷付費帳戶推算，見 §3）。
- 平台 ROI 的負面證據：土巴兔銷售費用率 61%、齊屹線索均價 527 元且線索量 −20%、오늘의집營益率 0.2%→−4.6%、Livspace 淨損率 −16.6%、HomeLane 廣告占營收 11%、Dekoruma 放棄 IPO 售予 Blibli。
- 履約機制 ROI 的正面證據：오늘의집 2023 年導入施工責任保障後施工 GMV 近倍增、累計破 1 兆韓元；土巴兔節點付款 2022 年保住 200 位業主 800 餘萬元；台灣住保會 2025 年履約 2,866 件／3.17 億元。
- 台灣現況數據：100室內設計 2025 年 4,000 筆簽約（推算 GMV 占市場 <1%）、PULO 逾 10,000 屋主、住保會 2,866 件、國土署登記室內裝修業約 1.7 萬家／專技人員 3.3 萬人 — [中央社 2026-04-27](https://www.cna.com.tw/news/ahel/202604270323.aspx)（經由 TW-A）。

### 推論
- 台灣平台滲透率（<1% GMV）遠低於韓國（65.3% 用過平台、22.9% 透過平台發包）與中國（互聯網家裝滲透率 20.8%），意味台灣仍有「平台化」空間，但依中韓經驗，此空間會被既有流量母體（數字科技、城邦、電商、仲介）而非新進者取得。

---

## 9. 12 市場橫向比較表

| 市場 | 主要消費者平台（公開數據） | AI／3D 設計工具 | BIM／施工管理 SaaS／履約託管 | 預製／模組化內裝 | 智慧家庭×裝修 | 數位獲客證據 | 資料信心 |
|---|---|---|---|---|---|---|---|
| 日本 | ホームプロ／リショップナビ／SUUMO 無資料；生活堂為網路專業第 1（金額未揭露）；LIXIL FC 549 店年 12 萬件；リノベる 適合R住宅 410 件（2025） | 無資料 | 建築確認 2025-04 起擴及 2 層以上／>200 ㎡大規模修繕（35 日審查）；ANDPAD 導入數無資料；瑕疵保險 4,496 件（2025 年度） | ユニットバス滲透無資料；住設三雄 2024–26 調價 8–15%；YKK 併 PHS | 無資料 | OB 顧客網絡＋仲介一站式＋網路見積；MLIT 稱網路蒐集比重上升（細項未取得） | 低 |
| 韓國 | 오늘의집 2025 營收 3,215 億韓元、施工累計 GMV >1 兆、App 下載 3,000 萬；집닥 累計 3,000 億（投資方）；아파트멘터리 521.7 億 | 오늘의집 AI 端到端；아파트멘터리×LG전자；Archisketch AI；GVR 軟體市場 USD 1.28 億（2024） | 施工責任保障（2023）；公正委 4 平台自律協約（2024-12）；KCA 對숨고等警示（2025-07）；BIM 無資料 | 建商 옵션／빌트인 普遍但滲透率無資料；四大集團套裝整裝 | 아파트멘터리×LG전자（質性） | 65.3% 用過平台、22.9% 平台發包；資訊來源部落格 42–52%、SNS／YouTube 33–40%、平台 31–37% | 中 |
| 新加坡 | Qanvast（Livspace 控股 2022；SG 占 Livspace FY25 15% ≈ Rs 219 crore）；Hometrust／Renopedia 無資料 | 無資料 | HDB DRC 許可制；CaseTrust 自願；CORENET X 室內要求無資料 | PPVC／DfMA 對室內影響無資料 | 無資料 | 無資料 | 低 |
| 香港 | 裝修佬 DecoMan／Decor8 無資料 | 無資料 | BIM 規定無資料 | 無資料 | 無資料 | 無資料 | 無 |
| 台灣 | 100室內設計 App 158 萬下載、2025 年 4,000+ 簽約、月訪 200 萬（自報）；PULO >10,000 屋主；設計家 近千設計師 | 100室內設計免費 AI 工具；採用率無資料 | 室內裝修審查 7 日／規費 NT$5,000–7,500；住保會履約 2,866 件／3.17 億（2025）；定型化契約草案（保固 1 年） | 系統櫃市占無資料；100室內設計主推模組化；三商美福一站式＋貸款 | 櫻花 AI 智能廚電（質性） | 平台 GMV 推算占市場 <1%；屋主資訊來源調查無資料 | 中低 |
| 中國大陸 | 酷家樂 MAU 250 萬／營收 8.20 億（2025）；齊屹 線索 527 元／條（2024）；土巴兔 銷售費用率 61%（2021）；貝殼家裝 154 億（2025）；互聯網家裝滲透 20.8%（2023） | 酷家樂付費企業 4.7 萬家、毛利率 82.2%、每日數百萬次渲染；3D 效果圖為簽單標配 | 貝殼 BIM＋模組化；土巴兔節點付款託管；聖都銀行存管；京煥新政府平台；預付款常達 6 成 | 亞廈裝配式毛利率 15.61%；土巴兔整裝 82.4%（平台樣本）；滲透率無官方數字；定制家居龍頭 2025 營收 −6～−17% | 三翼鳥零售額 >100 億、智家 APP MAU 1,000 萬、戶均 42 萬；華為高端精裝 ~50%；49.45% 已購智能家居；2025 補貼含智能家居 | 線上觸點影響 >70%；小紅書家裝 GMV +2.5×、#舊房改造 41.3 億次；被窩抖音線索 300 萬（自報）；貝殼交易導流 39% | 中高 |
| 馬來西亞 | Qanvast MY（Livspace）；Recommend.my／Atap／Kaodim 無資料 | 無資料 | LAM 2026 平台稽查通函；CIDB 外資 >30% 逐案註冊 | IBS 對室內影響無資料 | 無資料 | LAM 稽查：線上廣告為未註冊業者主要獲客管道（數百則廣告僅 1 家註冊） | 低 |
| 泰國 | HomePro Home Service 不分項；平台無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無 |
| 越南 | Happynest 月訪 400 萬、社團 40 萬（自報 ≈2023）；GMV 無 | AiHouse、Homestyler 越南文版；採用率無資料 | 無資料 | 無資料；XHOME 自有工廠櫃體 | Vietbuild 2025 智慧家居攤位最熱；Happynest×LG | Facebook 7,900 萬／Zalo 7,830 萬 MAU；TikTok 催生裝飾新職種；獲客靠 FB／Zalo／建商 | 低–中 |
| 印尼 | Dekoruma 2024 售予 Blibli Rp 1.16 兆（99.83%）；Fabelio 2022 破產；Kanggo 月活 3.6 萬；Gravel 募 USD 1,400 萬；Sejasa 75 萬客戶 | 趨勢文提 BIM／VR／AR；採用率無資料 | SejasaPay 履約帳戶；Mitra10 全通路 | 住宅仍傳統工法；Tokopedia 全裝套裝 Rp 2,499 萬–7,500 萬 | 趨勢文（AI 感測） | 平台滲透低（推論）；社群占比無資料 | 低–中 |
| 菲律賓 | 平台無資料；Wilcon 專案銷售 ₱347M（占 1%） | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | 無 |
| 印度 | Livspace FY25 Rs 1,460 crore（淨損 −16.6%）；HomeLane Rs 748 crore；組織化滲透 <1% | Livspace AI／HomeLane SpaceCraft 無資料 | 無資料 | Livspace／HomeLane 模組化櫃體標準交付 | 無資料 | HomeLane 廣告 Rs 84 crore ≈ 營收 11%（本人計算） | 中低 |

---

## 10. 關鍵數字總表

| 指標 | 數值 | 年份 | 來源 | 定義／備註 | 信心 |
|---|---|---|---|---|---|
| 群核科技（酷家樂）營收 | 8.20 億 CNY ≈ USD 1.14 億 ≈ TWD 35.9 億 | 2025 | [新浪港股](https://finance.sina.com.cn/stock/hkstock/hkzmt/2026-02-24/doc-inhnyyvp1282748.shtml) | 2023／2024：6.64／7.55 億 | 高 |
| 群核 MAU | 250 萬（2024：270 萬；月活訪客 8,630 萬） | 2025 | 同上 | 招股書口徑 | 高 |
| 群核 付費客戶 | 企業 4.7 萬家（年付 ≥20 萬元 424 家）；個人 43.3 萬 | 2025 | 同上 | — | 高 |
| 群核 毛利率／訂閱占比 | 82.2%／96.9%（另 98.3%） | 2025 | 同上；[格隆匯](https://m.gelonghui.com/news/5304964) | 2024：80.9% 或 80.2%（來源不一） | 中高 |
| 群核 經調整淨利／會計淨損 | +5,712.7 萬／−4.28 億 CNY | 2025 | [新浪港股](https://finance.sina.com.cn/stock/hkstock/hkzmt/2026-02-24/doc-inhnyyvp1282748.shtml) | 2026-04-17 上市 | 高 |
| 群核 海外收入占比 | 7.4% | 2024 前 9 月 | [36 氪](https://www.36kr.com/p/3169957639825921) | Coohom 海外 | 中 |
| 齊屹科技 每條線索均價 | 527 CNY ≈ USD 73 ≈ TWD 2,306 | 2024 | [同花順](https://stock.10jqka.com.cn/20250427/c667789677.shtml) | 線索 633,769 條（−20%） | 高 |
| 齊屹科技 營收／毛利率 | 10.56 億 CNY／39.1% | 2024 | 同上 | 2026H1 營收 3.622 億（−14.4%） | 高 |
| 土巴兔 銷售費用率 | 61.1%（2021）；57.9%／56.1%（2019／2020） | 2019–2021 | [華爾街見聞](https://wallstreetcn.com/articles/3634603) | 招股書；2022 撤回 IPO | 高（過時） |
| 土巴兔 三年獲客費 | 6.6 億 CNY ≈ USD 9,170 萬 | 2019–2021 | [建築之窗](https://www.jianzhuzhichuang.com/cms/jianzhushixun/5095.html) | — | 中 |
| 互聯網家裝滲透率／規模 | 20.8%／4,142 億 CNY | 2023 | [前瞻](https://www.qianzhan.com/analyst/detail/220/240428-25c71993.html) | 經線上平台獲客／成交 | 中低 |
| 貝殼 家裝家居淨收入／貢獻利潤率 | 154 億 CNY（≈USD 21.4 億）／31.4% | 2025 | [新浪](https://finance.sina.com.cn/stock/estate/integration/2026-03-16/doc-inhrequs9902543.shtml) | 2024：148 億／30.7% | 高 |
| 貝殼 房產交易貢獻家裝合同額 | 約 39% | 2022Q4 | [21 經濟網](https://www.21jingji.com/article/20230318/herald/e28a277c5184a40ee1804a3896d521ba.html) | — | 中 |
| 線上觸點對家居決策影響率 | >70% | 2025 | [36 氪](https://www.36kr.com/p/3785899311012873) | 白皮書 | 中 |
| 小紅書 家居家裝 GMV 成長 | 年增 2.5 倍 | 2024 | [騰訊新聞](https://news.qq.com/rain/a/20250612A05SKV00) | 平台口徑 | 中 |
| 小紅書 #舊房改造 瀏覽量 | 41.3 億次 | 2025-03 | [搜狐](https://m.sohu.com/a/1037767125_406598/) | — | 中 |
| 被窩 抖音直播有效線索 | >300 萬個／年 | 2024 | [數英](https://www.digitaling.com/projects/285641.html) | 服務商自報 | 低 |
| 三翼鳥 零售額／智家 APP MAU／新增門店 | >100 億 CNY／1,000 萬／1,556 家 | 2024 | [新浪科技](https://finance.sina.com.cn/tech/roll/2025-01-20/doc-inefrnxv9444188.shtml) | 企業自報 | 中 |
| 三翼鳥 戶均消費 | 42 萬 CNY ≈ USD 5.8 萬 ≈ TWD 184 萬 | — | [界面](https://www.jiemian.com/article/6485853.html) | 高端融合口徑 | 中低 |
| 高端精裝房智能家居 華為份額 | 近 50% | 2025 | [199IT／奧維雲網](https://www.199it.com/archives/1812063.html) | 精裝房口徑 | 中 |
| 已購買智能家居受訪者 | 49.45% | 2025 | [艾媒](https://report.iimedia.cn/tag/家居家装) | 市調 | 中 |
| 亞廈股份 毛利率（裝配式） | 15.61%（行業均值 13.28%） | 2025 | [新浪](https://finance.sina.cn/2026-04-30/detail-inhwhene7094454.d.html) | 公裝 | 高 |
| 土巴兔 託管保住款 | 800 餘萬 CNY／200+ 業主 | 2022 | [澎湃](https://www.thepaper.cn/newsDetail_forward_27769661) | 單一事件 | 中 |
| 오늘의집 營收／營業損益 | 3,215 億 KRW（≈USD 2.30 億）／−147 億 | 2025 | [와우테일](https://wowtale.net/2026/04/14/257037/) | 2024：2,879 億／+5.78 億 | 高 |
| 오늘의집 施工累計 GMV | >1 兆 KRW ≈ USD 7.1 億 ≈ TWD 225 億 | 至 2025-03 | [데모데이](https://demoday.co.kr/bm-analysis/109) | 2023 導入施工責任保障後近倍增 | 中 |
| 오늘의집 施工申請增幅 | +200% | 2024 | [뉴스핌](https://www.newspim.com/news/view/20250530000207) | — | 中 |
| 오늘의집 App 下載／募資／估值 | 3,000 萬／2,300 億 KRW／≈2 兆 KRW | 2024／2022 | [유니콘팩토리](https://www.unicornfactory.co.kr/article/2024041211050958876)；[MTN](https://news.mtn.co.kr/news-detail/2022050915405282133) | — | 中 |
| 집닥 累計交易額 | >3,000 億 KRW ≈ USD 2.14 億 | ≈2025 | [빅뱅엔젤스](https://blog.bigbangangels.com/zipdoc/) | 投資方資料 | 低 |
| 아파트멘터리 營收／累計募資 | 521.7 億／580 億 KRW | 2025 | [The VC](https://thevc.kr/apartmentary) | LG전자 2025-10 投資 | 中 |
| 韓國 室內設計軟體市場 | USD 1.279 億→2.674 億（2030） | 2024 | [GVR](https://www.grandviewresearch.com/horizon/outlook/interior-design-software-market/south-korea) | 研究機構定義 | 低 |
| 韓國 用過線上裝修平台／平台發包 | 65.3%／22.9% | ≈2024 | [더리빙](https://www.theliving.co.kr/news/articleView.html?idxno=21707) | n=2,680 社群樣本 | 中低 |
| 韓國 資訊來源 | 入口部落格 42.2%、平台 31.1%；SNS 39.9%、入口搜尋 38.7% | 2024–2025 | [더리빙 3198](https://www.theliving.co.kr/news/articleView.html?idxno=22216)；[더리빙 1962](https://www.theliving.co.kr/news/articleView.html?idxno=23807) | 社群樣本 | 中 |
| 韓國 資訊蒐集管道 | 入口搜尋 51.5%、App 36.8%、YouTube 32.5% | 2023 | [KiwiSurvey](https://kiwisurvey.kr/report/detail?id=85) | — | 中 |
| 韓國 4 平台自律協約 | 오늘의집、숨고、집닥、내드리오 | 2024-12-16 | [korea.kr](https://www.korea.kr/briefing/pressReleaseView.do?newsId=156665860&pWise=sub&pWiseSub=C2) | 無強制力 | 高 |
| LIXILリフォームショップ 店數／年件數 | 549 店／約 12 萬件 | 2024-03／2023-01 | [LIXIL PDF](https://bqzr2f-lts.origin.lixil.com/news/docs/202409_lrs-LTSebisu-open.pdf)；[digitalpr](https://digitalpr.jp/r/56840) | FC 體系 | 中高 |
| リノベる 適合R住宅 發行件數 | 410 件（全國第 1，連續 6 年） | 2025 年度 | [リノベる PR](https://www.renoveru.jp/hubfs/%E3%80%90PRESS%20RELEASE%E3%80%91%E3%83%AA%E3%83%8E%E3%83%99%E3%82%8B%E3%80%816%E5%B9%B4%E9%80%A3%E7%B6%9A%E5%85%A8%E5%9B%BD%E3%83%BB%E9%A6%96%E9%83%BD%E5%9C%8F1%E4%BD%8D%E3%81%AE%E8%AB%8B%E8%B2%A0%E5%9E%8B%E4%BA%8B%E6%A5%AD%E8%80%85%E3%81%AB%20%E3%80%8C%E9%81%A9%E5%90%88R%E4%BD%8F%E5%AE%85%E3%80%8D%E7%99%BA%E8%A1%8C%E4%BB%B6%E6%95%B0%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0.pdf) | — | 中 |
| 日本 建築確認審查期（新 2 號） | 7 日→35 日 | 2025-04 起 | [藤岡市](https://www.city.fujioka.gunma.jp/material/files/group/26/foufg.pdf) | 含大規模修繕 | 中 |
| 日本 リフォーム瑕疵保険 件數 | 4,496 件（−3.6%） | 2025 年度 | [リフォーム産業新聞](https://www.fujisan.co.jp/product/1281683407/b/2808733/) | 轉述 | 中 |
| 100室內設計 App 下載／需求／簽約 | 158 萬／近 15,000／>4,000 | 2025 | [NOWnews](https://www.nownews.com/news/6770793) | 平台自報 | 中 |
| 100室內設計 設計公司／月訪量 | 1,400 家／>200 萬 | 2025–26 | [鉅亨網](https://tw.stock.yahoo.com/news/%E6%88%BF%E7%94%A2-%E6%95%B8%E5%AD%97%E7%A7%91%E6%8A%80%E6%8B%93%E5%AE%A4%E5%85%A7%E8%A8%AD%E8%A8%88%E7%89%88%E5%9C%96-%E5%B9%B3%E5%8F%B0%E6%9C%88%E8%A8%AA%E9%87%8F%E7%AA%81%E7%A0%B4200%E8%90%AC%E6%AC%A1-075452062.html) | 費率不明 | 中 |
| 100室內設計 推算年 GMV | 40–60 億 TWD（占市場 <1%） | 2025 | TW-A 推算 | 4,000 筆×100–150 萬 | 低（推算） |
| PULO 屋主數 | >10,000 | 2025 | [App Store](https://apps.apple.com/tw/app/pulo-%E8%A3%9D%E6%BD%A2%E5%B9%B3%E5%8F%B0-%E5%B1%8B%E4%B8%BB%E7%89%88/id1160638151) | 自報 | 低–中 |
| 住保會 履約件數／金額 | 2,866 件／TWD 3.173 億（≈USD 1,007 萬） | 2025 | [理財周刊](https://www.moneyweekly.com.tw/_Article?AID=247503) | 民間協會 | 中 |
| 台灣 室內裝修業／專技人員 | 約 1.7 萬家／3.3 萬人 | 2026-04 | [中央社](https://www.cna.com.tw/news/ahel/202604270323.aspx) | 國土署 | 高 |
| Livspace 營收／淨損 | Rs 1,460 crore（≈USD 1.70 億）／Rs 242 crore | FY25 | [Entrackr](https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863) | 印度 85%／新加坡 15% | 高 |
| Livspace Series F | USD 1.8 億（估值 >USD 10 億） | 2022 | [Business Wire](https://www.businesswire.com/news/home/20220207005993/en) | KKR 領投 | 高 |
| HomeLane 營收／廣告費 | Rs 748 crore／Rs 84 crore（≈11.2%） | FY25 | [Entrackr](https://entrackr.com/fintrackr/homelane-records-rs-748-revenue-in-fy25-but-falls-short-of-projections-10586234) | 廣告占比為本人計算 | 高／中 |
| Qanvast 被控股 | 多數股權→Livspace（Interiortech） | 2022-04 | [Allen & Gledhill](https://www.allenandgledhill.com/perspectives/articles/21509/acquisition-of-a-majority-stake-in-qanvast-pte-ltd-by-interiortepte-ltd) | — | 高 |
| Dekoruma 出售 | Rp 1.16 兆（≈USD 7,160 萬）／99.83%→Blibli | 2024-06-24 | [Tracxn](https://tracxn.com/d/companies/dekoruma/__yMvml0YzAJGfBB4NClfEUERCnmtJO5TKRq4i0M8IZmI)；[1001startup](https://1001startup.id/company/dekoruma) | 線上營收 USD 920 萬（2024） | 中高 |
| Gravel 募資／Kanggo 月活／Sejasa 客戶 | USD 1,400 萬／36,000+／750,000+ | 2023／2025／2025 | [Katadata](https://katadata.co.id/digital/startup/656d6becb3021/investor-amerika-suntik-startup-konstruksi-gravel-rp-216-miliar)；[Investor.id](https://investor.id/business/409706/pengguna-kanggo-tembus-36-ribu-layanan-perawatan-bangunan-kian-diminati)；[Sejasa](https://www.sejasa.com/) | 後兩者自報 | 中／中低 |
| Happynest 月訪／社團 | 400 萬／40 萬人 | ≈2023 | [Bongdaplus](https://bongdaplus.vn/ben-ngoai-duong-piste/happynest-giup-hanh-trinh-lam-nha-cua-nguoi-viet-tro-nen-de-dang-hon-3981922305.html) | 自報 | 中低 |
| 越南 Facebook／Zalo 用戶 | 7,900 萬／7,830 萬 MAU | 2025 | [Elite Asia](https://www.eliteasia.co/top-digital-and-social-media-trends-in-vietnam-in-2026/) | 一般社群，非裝修專屬 | 中 |
| 馬來西亞 LAM 平台稽查 | 數百則廣告僅 1 家確認註冊 | 2026 | [LAM（X）](https://x.com/LembagaArkitek/status/2065266904147939778) | 社群貼文 | 低 |
| 梁志天設計集團 收入 | HK$4.227 億（≈USD 5,420 萬） | 2025 | [HKEX](https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0319/2026031900292.pdf) | 非平台 | 高 |
| Wilcon 專案銷售 | ₱347M（≈USD 610 萬，占 1%） | 2024 | [Inquirer Plus](https://plus.inquirer.net/?p=256738) | — | 高 |

---

## 11. 對台灣業者（室內裝修＋不動產＋家居零售集團）的啟示

1. **把 3D／AI 設計 SaaS 當「簽單工具採購」而非「科技投資」**：酷家樂以每帳戶平均約 1,656 元人民幣／年（本人推算）的低價訂閱做到 4.7 萬家企業客戶、82% 毛利率，證明工具供應商有極大降價空間；台灣集團應以訂閱方式（Coohom 海外版、Homestyler 或本土工具）統一設計部門出圖與報價格式，把「免費 3D 效果圖＋即時估價」變成與 100室內設計、PULO 競爭的前端武器。沒有任何市場證據支持集團自研 AI 設計工具（群核上市後仍會計虧損、股價跌回發行價）。
2. **不要自建媒合平台，把預算花在「既有流量母體上的案例與評價」**：中（土巴兔銷售費用率 61%、齊屹線索 527 元且年減 20%）、韓（오늘의집 10 年才獲利、2025 再轉虧）、印（Livspace 淨損 16.6%、HomeLane 廣告占營收 11%）、印尼（Dekoruma 放棄 IPO 售予 Blibli）四地都證明平台本身難獲利；台灣 100室內設計推算 GMV 占市場 <1%，意味平台只是補充通路。集團應在 100室內設計、PULO、設計家、Instagram／YouTube 建立案例庫，並以「仲介交易→裝修」（貝殼模式，交易導流 39%）與「家居零售門店→安裝／裝修」（特力屋、三翼鳥模式）作為主獲客引擎。
3. **把「履約保證＋節點付款＋第三方託管」做成可行銷的信任產品**：오늘의집 2023 年導入施工責任保障後施工 GMV 近倍增、累計破 1 兆韓元；土巴兔節點付款 2022 年保住 200 位業主 800 餘萬元；台灣住保會 2025 年履約 2,866 件／3.17 億元，國土署定型化契約草案（審閱期 5 日、保固 1 年）即將施行。對應台灣「裝修蟑螂」與韓國「먹튀」、中國「跑路」共通痛點，這是 12 市場中 ROI 證據最直接的數位化項目，且成本遠低於平台。
4. **內容獲客的對標是小紅書／YouTube「設計師創作者」而非投放**：中國線上觸點影響率 >70%、小紅書家裝 GMV 年增 2.5 倍、博主單月漲粉 10 萬+；韓國 SNS／YouTube 占資訊來源約四成。台灣集團可將設計師培養為內容創作者（工地實景、完工案例、避坑），以自然流量取代每線索數千元的付費線索；但須記錄韓國 KCA 已針對「SNS 假評價」與平台失聯發出警示，內容真實性將成監管焦點。
5. **BIM／裝配式／智慧家庭以「試點＋合規」處理，不作策略賭注**：12 市場均無室內工程 BIM 強制規定原文與裝配式內裝滲透率數據；唯一可量化的是日本 2025-04 建築確認擴大（35 日審查）與台灣室內裝修審查對圖說要求的提高，這是 BIM／3D 出圖的合規需求而非商業需求。智慧家庭只有中國「家電門店導流整裝」（三翼鳥 1,556 家新店、戶均 42 萬元）被證明可規模化，且依賴補貼；台灣可與櫻花、家電通路做「場景整裝」小規模合作，先量測綁售率再擴大。
6. **模組化的落點是系統櫃／廚衛套裝，且必須綁通路**：中國定制家居龍頭 2025 年營收下滑 6–17%、利潤下滑 23–47%，證明模組化本身不保證利潤，須靠貝殼集採（主材 80%）或 한샘 經銷展示館式的通路支撐。台灣集團家居零售線可仿 Tokopedia「studio 全裝套裝」與三商美福「設計＋家具＋貸款」把系統櫃做成可線上下單的標準品。
7. **出海數位化優先順序：韓國平台入駐 > 中國小紅書內容 > 東南亞 Facebook／Zalo 社團**：韓國 65.3% 消費者用過平台（KR-B 建議「오늘의집入駐＋Naver 部落格＋YouTube」）；中國獲客須掛在仲介／家電／定製家居的相鄰交易上並經營小紅書；越南無公開成交量的媒合平台，獲客靠 Facebook 7,900 萬／Zalo 7,830 萬 MAU 的社團與建商交屋合作；馬來西亞則須注意 LAM 2026 年起透過網路平台稽查未註冊業者，線上廣告合規是前提。
8. **補數據後再決策**：本輪缺乏 Coohom 海外定價、設計師 AI 採用率、ANDPAD 導入數、CORENET X 室內要求、系統櫃市占、CPL 基準等關鍵數字（見 §12），任何「科技投資」決策應等附錄 A 的 20 條查詢跑完再做。

---

## 12. 資料缺口

| 缺口項目 | 本輪狀態 | 建議取得方式 |
|---|---|---|
| 群核科技招股書原文（MAU、付費客戶、ARPU、海外／台灣用戶、定價） | 僅媒體轉述；毛利率 80.9% vs 80.2% 來源不一 | 港交所披露易 00068 招股書／2025 年報；Coohom 官網定價頁 |
| Homestyler、Planner 5D、Spacely、SketchUp／Enscape／D5 Render 在亞洲各市場用戶數與定價 | 無資料 | 各公司新聞稿、App 商店排名、Trimble／Chaos 年報 |
| 設計師 AI／3D 採用率與情緒調查（2025）、生產力量測 | 12 市場均無 | 各國設計師協會（CSID、KOSID、JID、HDII、MIID、SIDS）年度調查；Houzz／Coohom 使用者調查 |
| 오늘의집 年度 GMV、MAU、抽成率；집닥 財務；100室內設計／PULO／設計家 費率與 GMV | 未公開 | DART 감사보고서；數字科技（5287）年報分部資訊；thevc.kr Pro |
| ホームプロ／リショップナビ／SUUMO リフォーム 加盟店數、累計相談、成約、抽成 | 未取得 | リクルート決算說明、各平台加盟店募集頁 |
| ANDPAD、Photoruction 等施工管理 SaaS 導入社数、定價 | 無資料 | ANDPAD 新聞稿（導入社数）、IR |
| CORENET X（新加坡）、香港 BIM、韓國 BIM 義務化對室內裝修工程之適用 | 無資料 | BCA CORENET X 官網、HK 發展局 BIM 通函、국토부 BIM 로드맵 |
| 裝配式裝修滲透率（中國住建部口徑、2025 政策原文）、日本ユニットバス出貨、新加坡 DfMA 對室內之規定、台灣系統櫃市占與市場規模、韓國빌트인／옵션滲透率、馬來西亞 IBS | 全部無資料 | 住建部《裝配式裝修》政策文件；日本住宅設備システム協會出貨統計；BCA DfMA 指南；台灣系統櫃公會／上市櫃年報；KOSCA |
| Samsung SmartThings、Xiaomi、LIXIL、Panasonic、LG 智慧家庭與裝修綁售率；三翼鳥 2025 全年 | 無資料 | 各品牌 IR／新聞稿；奧維雲網智能家居報告 |
| 各市場「首次接觸管道」調查、社群（小紅書／Instagram／YouTube／TikTok／LINE／Facebook）線索占比、CPL 基準、轉化率 | 僅中（齊屹 527 元）、韓（資訊來源調查） | 各國消費者調查（더리빙、艾媒、100室內設計、Qanvast 年度報告）；Meta／Google 行業基準 |
| 貝殼、三翼鳥投放占比與 CAC；Livspace／HomeLane 線上獲客占比與 AI 工具（SpaceCraft） | 無資料 | 年報 MD&A、公司部落格 |
| 香港（裝修佬 DecoMan、Decor8）、泰國、菲律賓、新加坡（Hometrust、Renopedia）、馬來西亞（Recommend.my、Atap、Kaodim）平台數據 | 全部無資料 | 各平台官網／媒體；ACRA／SSM 年報 |
| 第三方資金託管的法定地位與普及率（各市場）；中國 2025 年全國性家裝資金監管新規 | 僅案例 | 住建部／市監總局公告；台灣國土署定型化契約定稿 |
| 所有引用 URL 均未開頁核對 | 整合協議 §10 | WP6 查核代理逐條開啟 |

---

## 13. 來源清單（標題｜機構｜年份｜URL；「經由」註明原始擷取筆記）

### 中國大陸
1. 群核科技 MAU／付費客戶／NRR／經調整淨利｜新浪港股｜2026-02-24｜https://finance.sina.com.cn/stock/hkstock/hkzmt/2026-02-24/doc-inhnyyvp1282748.shtml｜經由 CN-A
2. 群核科技上市（21 經濟網）｜2026-04-09｜https://www.21jingji.com/article/20260409/herald/4a8ab282072f3daa5bf46a36e81fe0cc.html｜經由 CN-A
3. 群核科技上市 3 個月跌回發行價｜新浪科技｜2026-08-07｜https://finance.sina.com.cn/tech/roll/2026-08-07/doc-inimnenp3338147.shtml｜經由 CN-A
4. 群核科技招股书更新（2024 收入 7.55 亿、毛利率 80.9%）｜中国基金报｜2025｜https://www.chnfund.com/article/AR385fcc39-1859-5917-d2f8-3a1bed2fa95f｜經由 T2
5. 群核科技港股上市｜澎湃新闻｜2026｜https://www.thepaper.cn/newsDetail_forward_32992074｜經由 T2
6. 群核科技招股书解读｜36氪｜2025｜https://www.36kr.com/p/3169957639825921｜經由 T2
7. 群核科技(00068.HK)：核心订阅业务稳健｜格隆汇｜2026｜https://m.gelonghui.com/news/5304964｜經由 T2
8. 群核科技 Frost & Sullivan 排名｜藍鯨｜2026｜https://www.lanjinger.com/d/1775735430884273852｜經由 CN-A
9. China's answer to Autodesk, Manycore bets on AI｜SCMP｜2025｜https://www.scmp.com/tech/tech-trends/article/3309107/chinas-answer-autodesk-manycore-bets-ai-future-spatial-intelligence｜經由 CN-A
10. 群核科技上市 基石 37%｜財聯社｜2026｜https://www.cls.cn/detail/2338659｜經由 CN-A
11. 酷家乐（註冊用戶，D 級）｜百度百科｜—｜https://baike.baidu.com/item/%E9%85%B7%E5%AE%B6%E4%B9%90/12914547｜經由 CN-A
12. 齐屹科技 2024 财年归母亏损 1.27 亿元｜同花顺｜2025｜https://stock.10jqka.com.cn/20250427/c667789677.shtml｜經由 T2
13. 齐屹科技 2024 年报｜香港交易所披露易｜2025｜https://www.hkexnews.hk/listedco/listconews/sehk/2025/0425/2025042501676_c.pdf｜經由 T2
14. 齊屹科技 2026H1｜騰訊新聞｜2026-08-26｜https://news.qq.com/rain/a/20260826A0BMM200｜經由 CN-A
15. 土巴兔冲刺A股（2021 財務）｜华尔街见闻｜2021｜https://wallstreetcn.com/articles/3634603｜經由 T2
16. 土巴兔撤回IPO｜界面新闻｜2022｜https://www.jiemian.com/article/7679144.html｜經由 T2
17. 土巴兔 IPO 问询｜中国证券报｜2022｜https://cs.com.cn/ssgs/gsxw/202208/t20220804_6289142.html｜經由 T2
18. 土巴兔三年獲客費 6.6 億｜建築之窗｜—｜https://www.jianzhuzhichuang.com/cms/jianzhushixun/5095.html｜經由 CN-A
19. 土巴兔 2026 報告 整裝占比 82.4%｜大眾網｜2026｜https://m.dzplus.dzng.com/share/general/0/NEWS3468079NBYNVQOGXEHST｜經由 CN-B
20. 家裝預付款與平台託管（土巴兔）｜澎湃新聞｜2024｜https://www.thepaper.cn/newsDetail_forward_27769661｜經由 CN-B
21. 互聯網家裝規模與滲透率｜前瞻產業研究院｜2024｜https://www.qianzhan.com/analyst/detail/220/240428-25c71993.html｜經由 CN-A
22. 貝殼 2025 全年業績（家裝 154 億、BIM、集採）｜新浪財經｜2026-03-16｜https://finance.sina.com.cn/stock/estate/integration/2026-03-16/doc-inhrequs9902543.shtml｜經由 CN-A
23. 贝壳 2024 年家装业务收入 148 亿元｜第一财经｜2025｜https://www.yicai.com/news/102524134.html｜經由 T2
24. 贝壳 2024 年第四季度及全年业绩｜澎湃新闻｜2025｜https://www.thepaper.cn/newsDetail_forward_27482182｜經由 T2
25. 貝殼 房產交易貢獻家裝 39%｜21 經濟網｜2023｜https://www.21jingji.com/article/20230318/herald/e28a277c5184a40ee1804a3896d521ba.html｜經由 CN-A
26. 貝殼家裝 項目經理產能｜瑞財經｜2025｜https://www.rccaijing.com/news-7307953023459456534.html｜經由 CN-A
27. 被窩抖音直播獲客 300 萬線索｜數英｜—｜https://www.digitaling.com/projects/285641.html｜經由 CN-A
28. 聖都整裝多渠道觸達｜網易｜2025｜https://www.163.com/dy/article/JVUFR0GC05118O92.html｜經由 CN-A
29. 小紅書家居家裝 GMV 年增 2.5 倍｜騰訊新聞｜2025-06-12｜https://news.qq.com/rain/a/20250612A05SKV00｜經由 CN-A
30. 小紅書 #舊房改造 41.3 億次｜搜狐｜2025｜https://m.sohu.com/a/1037767125_406598/｜經由 CN-B
31. 2025 中國家居消費者決策鏈路白皮書（線上觸點 >70%）｜36 氪｜2025｜https://www.36kr.com/p/3785899311012873｜經由 CN-B
32. 增長黑盒 家居決策調研｜數英｜2025｜https://www.digitaling.com/articles/1441033.html｜經由 CN-B
33. 裝企獲客兩類（抖音／小紅書 vs 付費投放）｜網易｜2026｜https://www.163.com/dy/article/KVGIUMCA0552XWVG.html｜經由 CN-A
34. 家裝低價引流與增項｜澎湃轉法治日報｜2025｜https://www.thepaper.cn/newsDetail_forward_32020018｜經由 CN-B
35. 家居賣場營收下滑｜新浪｜2026-04-07｜https://finance.sina.com.cn/stock/relnews/hk/2026-04-07/doc-inhtrqch3735553.shtml｜經由 CN-A
36. 海爾三翼鳥 2024 零售額破百億｜新浪科技｜2025-01-20｜https://finance.sina.com.cn/tech/roll/2025-01-20/doc-inefrnxv9444188.shtml｜經由 CN-A
37. 三翼鳥（中國日報）｜2025-01-20｜https://caijing.chinadaily.com.cn/a/202501/20/WS678e1416a310be53ce3f290f.html｜經由 CN-A
38. 三翼鳥 戶均消費 42 萬｜界面｜—｜https://www.jiemian.com/article/6485853.html｜經由 CN-A
39. 三翼鳥 門店｜騰訊新聞｜2024-07｜https://news.qq.com/rain/a/20240718A02A6J00｜經由 CN-A
40. 高端精裝房智能家居華為份額近 50%（奧維雲網）｜199IT｜2025｜https://www.199it.com/archives/1812063.html｜經由 CN-A
41. 2025 年中國家居市場消費行為調查（49.45% 已購智能家居）｜艾媒諮詢｜2025｜https://report.iimedia.cn/tag/家居家装｜經由 CN-B
42. 亞廈股份 2025 年報（裝配式）｜新浪財經｜2026-04-30｜https://finance.sina.cn/2026-04-30/detail-inhwhene7094454.d.html｜經由 CN-A
43. 亞廈股份 2025 營收｜同花順｜2026-04-28｜https://news.10jqka.com.cn/20260428/c676320986.shtml｜經由 CN-A
44. 商務部等 6 部門 2025 年家裝廚衛「煥新」通知｜中國政府網｜2025-01｜https://www.gov.cn/zhengce/zhengceku/202501/content_7001494.htm｜經由 CN-A
45. 2026「國補」繼續！幾類補貼有變化｜新華網｜2026-01-02｜https://www.news.cn/politics/20260102/8280c115602841078b65d8f5176b239c/c.html｜經由 CN-A
46. 兩省份率先擴圍以舊換新品類（黑龍江廚衛智能）｜中國家電網｜2026-04｜https://news.cheaa.com/2026/0427/654595.shtml｜經由 CN-A
47. 聖都整裝銀行資金存管（推廣）｜四川在線｜—｜https://cbgc.scol.com.cn/news/7838213｜經由 CN-B
48. 廈門裝企停工／三方託管｜揚子晚報｜2025-12-22｜https://www.yzwb.net/news/ch/202512/t20251222_303120.html｜經由 CN-B
49. 北京「京煥新」家裝一體化平台｜澎湃｜—｜https://m.thepaper.cn/detail/30044835｜經由 CN-B
50. 住范兒資金鏈斷裂｜鈦媒體｜2025｜https://www.tmtpost.com/7644935.html｜經由 CN-B
51. 住宅室內裝飾裝修管理辦法（結構變動設計要求）｜深圳法規庫｜—｜https://www.sz.gov.cn/cn/xxgk/zfxxgj/zcfg/content/post_8966865.html｜經由 CN-B
52. 2025 年定制家居龍頭業績（歐派等）｜新浪財經｜2026-05-12｜https://news.sina.cn/2026-05-12/detail-inhxrshc1334104.d.html｜經由 CN-B
53. 志邦家居 2025 年報｜證券之星｜2026｜https://stock.stockstar.com/SS2026062400022292.shtml｜經由 CN-B
54. 索菲亞 2025H1｜每經｜2025-08-27｜https://www.nbd.com.cn/articles/2025-08-27/4034678.html｜經由 CN-B
55. 建材行業穩增長工作方案（2025—2026）轉述｜觀研天下｜2026｜https://www.chinabaogao.com/jingzheng/202604/790396.html｜經由 CN-B
56. 上海家裝設計師招聘樣本（CAD／SU）｜牛起招聘｜2026｜https://campus.niuqizp.com/job-vwk5tnatn.html｜經由 CN-B
57. 梁志天設計集團 2025 年業績｜HKEX｜2026-03-19｜https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0319/2026031900292.pdf｜經由 CN-B

### 韓國
58. 버킷플레이스 2024년 감사보고서 실적｜아시아경제｜2025｜https://core.asiae.co.kr/article/2025033115492450800｜經由 T2
59. 오늘의집 25년 매출 3천215억｜와우테일｜2026-04-14｜https://wowtale.net/2026/04/14/257037/｜經由 KR-A
60. 오늘의집 AI 기반 엔드투엔드 공간 솔루션｜벤처스퀘어｜2026｜https://www.venturesquare.net/1075994/｜經由 KR-A
61. 오늘의집 2025년 실적발표｜오늘의집 뉴스룸｜2026｜https://ohstory.io/press/pressrelease/15242｜經由 KR-A
62. 오늘의집 매출 3000억 수익성 악화｜아웃스탠딩｜2026｜https://outstanding.kr/press/1887/20260414｜經由 KR-A
63. 시공 거래액 1조로 흑자 달성한 3C 전략｜데모데이｜2025｜https://demoday.co.kr/bm-analysis/109｜經由 KR-A
64. 3000만명 홀리더니…연매출 2400억｜유니콘팩토리｜2024｜https://www.unicornfactory.co.kr/article/2024041211050958876｜經由 T2
65. 오늘의집 2,300억원 투자 유치｜MTN｜2022｜https://news.mtn.co.kr/news-detail/2022050915405282133｜經由 T2
66. 오늘의집 인테리어 시공 신청 +200%／평균 시공비｜뉴스핌｜2025-05-30｜https://www.newspim.com/news/view/20250530000207｜經由 KR-B
67. 오늘의집 검색어로 본 2025년 키워드｜오늘의집 뉴스룸｜2025｜https://ohstory.io/press/pressrelease/14717｜經由 KR-B
68. 집닥 기업정보｜넥스트유니콘｜2025｜https://www.nextunicorn.kr/company/d091a12a4081eb88｜經由 KR-A
69. 집닥 누적 거래액｜빅뱅엔젤스 블로그｜—｜https://blog.bigbangangels.com/zipdoc/｜經由 KR-A
70. 집닥 재무｜The VC｜2025｜https://thevc.kr/zipdoc｜經由 T2
71. 집닥 기업정보｜원티드｜—｜https://www.wanted.co.kr/company/767｜經由 T2
72. 아파트멘터리 기업정보｜The VC｜2026｜https://thevc.kr/apartmentary｜經由 KR-A
73. 아파트멘터리, LG전자 전략적 투자 유치｜테크42｜2025｜https://www.tech42.co.kr/%EC%95%84%ED%8C%8C%ED%8A%B8%EB%A9%98%ED%84%B0%EB%A6%AC-lg%EC%A0%84%EC%9E%90-%EC%A0%84%EB%9E%B5%EC%A0%81-%ED%88%AC%EC%9E%90-%EC%9C%A0%EC%B9%98-ai%EC%9C%B5%ED%95%A9-%EB%AA%B0%EC%9E%85%ED%98%95/｜經由 KR-A
74. 아키스케치 AI｜Archisketch Substack｜2025｜https://archisketch.substack.com/p/ai-3b0｜經由 KR-A
75. South Korea Interior Design Software Market｜Grand View Research｜2025｜https://www.grandviewresearch.com/horizon/outlook/interior-design-software-market/south-korea｜經由 KR-A
76. 30평대 아파트 리모델링 견적 2026｜feeldesign.ai｜2026｜https://www.feeldesign.ai/ko/post/30-pyeong-apartment-remodeling-estimate-2026｜經由 KR-A
77. 2680명의 소비자가 바라본 인테리어 시장｜월간 THE LIVING｜—｜https://www.theliving.co.kr/news/articleView.html?idxno=21707｜經由 KR-A
78. 3198명의 소비자 인테리어 현황｜월간 THE LIVING｜2024｜https://www.theliving.co.kr/news/articleView.html?idxno=22216｜經由 KR-B
79. 1962명 조사（SNS 39.9%）｜월간 THE LIVING｜2025｜https://www.theliving.co.kr/news/articleView.html?idxno=23807｜經由 KR-B
80. 3160명 조사（47.6% 전문업체 선호）｜월간 THE LIVING｜2025｜https://www.theliving.co.kr/news/articleView.html?idxno=23071｜經由 KR-A
81. 키위서베이 2023 인테리어 제품 트렌드 리포트｜KiwiSurvey｜2023｜https://kiwisurvey.kr/report/detail?id=85｜經由 KR-A
82. 2025 홈인테리어 니즈 인식 조사｜엠브레인 트렌드모니터｜2025｜https://www.trendmonitor.co.kr/tmweb/trend/allTrend/detail.do?bIdx=3303&code=0401&trendType=CKOREA｜經由 KR-B
83. 공정위·소비자원·4개 플랫폼 자율협약｜korea.kr｜2024-12-16｜https://www.korea.kr/briefing/pressReleaseView.do?newsId=156665860&pWise=sub&pWiseSub=C2｜經由 T3
84. 인테리어 플랫폼 자율협약｜뉴시스｜2024｜https://www.newsis.com/view/NISX20241216_0002998493｜經由 T3
85. '숨고' 등 용역 중개플랫폼 피해주의보｜경향신문｜2025｜https://www.khan.co.kr/article/202507011523011｜經由 KR-A
86. KCA 2022 인테리어 8개 플랫폼 조사｜파이낸셜뉴스｜2022｜https://www.fnnews.com/news/202204261201348830｜經由 KR-B
87. 인테리어 사기의 3가지 유형｜로톡｜—｜https://www.lawtalk.co.kr/posts/118955｜經由 KR-B
88. 아파트 인테리어 공사 행위허가（생활법령）｜법제처 easylaw｜—｜https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=1222&ccfNo=2&cciNo=1&cnpClsNo=1｜經由 KR-B
89. 한샘 2분기 리하우스 1,660억｜네이트 뉴스｜2026-08-10｜https://m.news.nate.com/view/20260810n29818｜經由 KR-A

### 日本
90. LIXILリフォームショップ 549 店｜LIXILトータルサービス｜2024｜https://bqzr2f-lts.origin.lixil.com/news/docs/202409_lrs-LTSebisu-open.pdf｜經由 T2
91. LIXILリフォームショップ 540 店舗・年間約12万件｜Digital PR Platform｜2023｜https://digitalpr.jp/r/56840｜經由 T2
92. 生活堂 業種別リフォーム売上ランキング 2025｜生活堂｜2025｜https://www.seikatsu-do.com/information/20251224.php｜經由 JP-A
93. リノベる 適合R住宅 6年連続1位｜リノベる｜2026｜https://www.renoveru.jp/hubfs/%E3%80%90PRESS%20RELEASE%E3%80%91%E3%83%AA%E3%83%8E%E3%83%99%E3%82%8B%E3%80%816%E5%B9%B4%E9%80%A3%E7%B6%9A%E5%85%A8%E5%9B%BD%E3%83%BB%E9%A6%96%E9%83%BD%E5%9C%8F1%E4%BD%8D%E3%81%AE%E8%AB%8B%E8%B2%A0%E5%9E%8B%E4%BA%8B%E6%A5%AD%E8%80%85%E3%81%AB%20%E3%80%8C%E9%81%A9%E5%90%88R%E4%BD%8F%E5%AE%85%E3%80%8D%E7%99%BA%E8%A1%8C%E4%BB%B6%E6%95%B0%E3%83%A9%E3%83%B3%E3%82%AD%E3%83%B3%E3%82%B0.pdf｜經由 JP-A
94. リノベる。ユーザーレポート 2024｜リノベる｜2024｜https://www.renoveru.jp/hubfs/corporate2024/pdf/20240625%E3%80%90%E3%83%97%E3%83%AC%E3%82%B9%E3%83%AA%E3%83%AA%E3%83%BC%E3%82%B9%E3%80%91%E3%80%8C%E3%83%AA%E3%83%8E%E3%83%99%E3%82%8B%E3%80%82%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%80%8D%E3%82%92%E5%85%AC%E9%96%8B.pdf｜經由 T2
95. 住友林業ホームテック 企業情報｜リクルートエージェント｜—｜https://www.r-agent.com/company/12495/｜經由 JP-A
96. 令和 6 年度住宅市場動向調査｜国土交通省｜2025｜https://www.mlit.go.jp/report/press/house02_hh_000228.html｜經由 JP-A
97. 四號特例縮小｜国土交通省｜2025｜https://www.mlit.go.jp/common/001500388.pdf｜經由 T3
98. 4号特例縮小 解説｜ANDPAD｜2025｜https://andpad.jp/columns/0086｜經由 T3
99. 令和7年4月施行 建築基準法改正｜青森県｜2025｜https://www.pref.aomori.lg.jp/soshiki/kendo/sh-seibi/shimokita_kijunhou_kaisei.html｜經由 JP-B
100. 改正建築基準法 周知資料（審查 35 日）｜藤岡市｜2025｜https://www.city.fujioka.gunma.jp/material/files/group/26/foufg.pdf｜經由 JP-B
101. 丹青社與若水國際 BIM 合作備忘錄｜共同通信 PR Wire｜2024-07｜https://kyodonewsprwire.jp/release/202407053219｜經由 TW-B
102. 2025年度 リフォーム瑕疵保険件数｜リフォーム産業新聞（fujisan）｜2026｜https://www.fujisan.co.jp/product/1281683407/b/2808733/｜經由 JP-B
103. リフォーム産業新聞 売上高ランキング 2025（渡辺パイプ）｜fujisan｜2025｜https://www.fujisan.co.jp/product/1281683407/b/2630241/｜經由 JP-A
104. LIXIL 価格改定（2024/4/1）｜LIXIL Newsroom｜2023｜https://newsroom.lixil.com/hubfs/newsroom/PDF/JapanComms/20231109_PriceRevision.pdf｜經由 JP-B
105. LIXIL 最大15%値上げ 2026｜LOGI-TODAY｜2026｜https://www.logi-today.com/952073｜經由 JP-B
106. TOTO 2026/12 価格改定｜交換できるくん｜2026｜https://www.sunrefre.jp/sumutano/housing-equipment/17415/｜經由 JP-B
107. PHS 株式譲渡完了（YKK）｜パナソニック HD｜2026｜https://holdings.panasonic/content/dam/holdings/jp/ja/corporate/investors/pdf/jn260331-2.pdf｜經由 JP-A
108. 点検商法 相談件数｜国民生活センター｜2026｜https://www.kokusen.go.jp/soudan_topics/data/reformtenken.html｜經由 JP-B

### 台灣
109. 100室內設計 2025 年市場觀察（App 下載、需求、簽約、AI 工具）｜NOWnews｜2025｜https://www.nownews.com/news/6770793｜經由 TW-A
110. 裝修年產值上看 5500 億 2026 趨勢｜經濟日報｜2025｜https://udn.com/news/story/7241/9245511｜經由 TW-A
111. 2026有望持續成長!裝修年產值上看5500億｜經濟日報｜2025｜https://udn.com/news/story/7241/9242628｜經由 TW-A
112. 數字科技拓室內設計版圖 平台月訪量突破200萬次｜鉅亨網（Yahoo）｜2026｜https://tw.stock.yahoo.com/news/%E6%88%BF%E7%94%A2-%E6%95%B8%E5%AD%97%E7%A7%91%E6%8A%80%E6%8B%93%E5%AE%A4%E5%85%A7%E8%A8%AD%E8%A8%88%E7%89%88%E5%9C%96-%E5%B9%B3%E5%8F%B0%E6%9C%88%E8%A8%AA%E9%87%8F%E7%AA%81%E7%A0%B4200%E8%90%AC%E6%AC%A1-075452062.html｜經由 T2
113. 台灣裝潢平台體驗比較（100室內設計、設計家、PULO）｜LINE TODAY｜2026｜https://today.line.me/tw/v3/article/gzXWjgz｜經由 T2
114. PULO 裝潢平台 屋主版｜App Store｜2025｜https://apps.apple.com/tw/app/pulo-%E8%A3%9D%E6%BD%A2%E5%B9%B3%E5%8F%B0-%E5%B1%8B%E4%B8%BB%E7%89%88/id1160638151｜經由 TW-A
115. PULO 裝潢平台 專家版｜App Store｜2026｜https://apps.apple.com/tw/app/pulo-%E8%A3%9D%E6%BD%A2%E5%B9%B3%E5%8F%B0-%E5%B0%88%E5%AE%B6%E7%89%88/id1266584276｜經由 T2
116. 設計家 Searchome 平台介紹｜鉅亨網雜誌頁｜—｜https://news.cnyes.com/magazines/41｜經由 TW-A
117. PRO360 室內設計費行情｜PRO360｜2025｜https://www.pro360.com.tw/price/interior_design｜經由 TW-A
118. 住保會 2025 履約件數與詐騙案｜理財周刊｜2025｜https://www.moneyweekly.com.tw/_Article?AID=247503｜經由 TW-A
119. 三商美福 一站式裝修＋貸款｜商業周刊廣編｜2025｜https://www.businessweekly.com.tw/business/indep/1005275｜經由 TW-A
120. 特力屋如何讓營收、獲利重返正成長｜科技新報｜2026-09｜https://finance.technews.tw/2026/09/06/how-tlw-can-return-revenue-and-profit-to-growth/｜經由 TW-A
121. 2025 年裝修行情（客變／新成屋／中古屋）｜工商時報｜2025-11-19｜https://www.ctee.com.tw/news/20251119700015-431001｜經由 TW-A
122. 櫻花 AI 智能廚電｜優分析｜2025｜https://uanalyze.com.tw/articles/8096948742｜經由 TW-A
123. 國土署：室內裝修既有申請規定未變（1.7 萬家／3.3 萬人）｜中央社｜2026-04-27｜https://www.cna.com.tw/news/ahel/202604270323.aspx｜經由 TW-A
124. 國土署澄清 2026 裝修新制報導不實｜中央社｜2026-04-14｜https://www.cna.com.tw/news/ahel/202604140322.aspx｜經由 T3
125. 建築物室內裝修管理辦法｜全國法規資料庫｜現行｜https://law.moj.gov.tw/LawClass/LawAll.aspx?PCode=D0070148｜經由 T3
126. 室內裝修許可如何申請（規費）｜Searchome 設計家｜2026｜https://www.searchome.net/article.aspx?id=76546｜經由 T3
127. 室內裝修定型化契約草案｜內政部國土署｜2025-11｜https://www.nlma.gov.tw/uploads/files/4a4f5b6c19d35226adf133a9a2bde45d.pdf｜經由 T3

### 新加坡／馬來西亞
128. Acquisition of a majority stake in Qanvast Pte Ltd by Interiortech Pte Ltd｜Allen & Gledhill｜2022｜https://www.allenandgledhill.com/perspectives/articles/21509/acquisition-of-a-majority-stake-in-qanvast-pte-ltd-by-interiortepte-ltd｜經由 T2
129. Livspace invests in Qanvast｜Southeast Asia Building｜2021｜https://seab.tradelinkmedia.biz/publications/6/news/3438｜經由 T2
130. HDB Applying for approval（DRC）｜HDB｜現行｜https://www.hdb.gov.sg/residential/living-in-an-hdb-flat/renovation/applying-for-approval｜經由 T3
131. Written reply to PQs on disputes arising from ID and renovation firms｜MTI Singapore｜2024-05｜https://mti.gov.sg/Newsroom/Parliamentary-Replies/2024/05/Written-reply-to-PQs-on-disputes-arising-from-Interior-Design-and-Renovation-firms｜經由 T3
132. Written reply to PQ on consumer protection for customers of non-accredited renovation contractors｜MTI Singapore｜2025-02｜https://www.mti.gov.sg/Newsroom/Parliamentary-Replies/2025/02/Written-reply-to-PQ-on-consumer-protection-for-customers-of-non-accredited-renovation-contractors｜經由 T3
133. LAM General Circular No. 1/2026（平台稽查）｜Lembaga Arkitek Malaysia（X）｜2026｜https://x.com/LembagaArkitek/status/2065266904147939778｜經由 MY-A
134. Unregistered firms offering architectural, interior design services soar｜BERNAMA｜2024｜https://www.bernama.com/en/news.php?id=2325910｜經由 MY-A
135. IKEA and Livspace to offer interior design solutions at Kuala Lumpur outlets｜EdgeProp Singapore｜—｜https://edgeprop.sg/property-news/ikea-and-livspace-offer-interior-design-solutions-kuala-lumpur-outlets｜經由 T2

### 印度
136. Livspace posts Rs 1,460 Cr revenue in FY25｜Entrackr｜2025｜https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863｜經由 T2
137. Livspace's FY25 Loss Declines 43%｜Inc42｜2025｜https://inc42.com/buzz/livspaces-fy25-loss-declines-43-to-inr-243-cr/｜經由 T2
138. Livspace Revenue Rises 23% to ₹1,460 Cr｜Outlook Business｜2025｜https://www.outlookbusiness.com/corporate/livspace-revenue-rises-23-to-1460-cr-in-fy25-losses-come-down｜經由 T2
139. Livspace Series F US$180M led by KKR｜Business Wire｜2022｜https://www.businesswire.com/news/home/20220207005993/en｜經由 T2
140. Livspace CBO exits after mass layoffs｜Entrackr｜2026｜https://entrackr.com/news/livspace-cbo-lalit-mittal-exits-after-co-founder-departure-and-mass-layoffs-11150871｜經由 T2
141. 100 job cuts at Livspace｜HRKatha｜2025｜https://www.hrkatha.com/news/layoff/100-job-cuts-at-livspace/｜經由 T2
142. HomeLane records Rs 748 Cr revenue in FY25｜Entrackr｜2025｜https://entrackr.com/fintrackr/homelane-records-rs-748-revenue-in-fy25-but-falls-short-of-projections-10586234｜經由 T2
143. HomeLane reports 22% revenue growth, EBITDA profitability in Q4｜Franchise India｜2025｜https://www.franchiseindia.com/index.php/insights/en/news/homelane-reports-22-revenue-growth-in-fy25-achieves-ebitda-profitability-in-q4.57729｜經由 T2
144. HomeLane FY25 note｜Motilal Oswal｜2025｜https://www.motilaloswal.com/news/stocks/107588｜經由 T2
145. India Interior Design Market（Redseer 線上 <1% 轉述）｜Mordor Intelligence｜2025｜https://www.mordorintelligence.com/industry-reports/india-interior-design-market｜經由 T1

### 印尼
146. Dekoruma company profile｜Tracxn｜2026｜https://tracxn.com/d/companies/dekoruma/__yMvml0YzAJGfBB4NClfEUERCnmtJO5TKRq4i0M8IZmI｜經由 ID-A
147. Dekoruma｜Dealroom｜2026｜https://app.dealroom.co/companies/dekoruma｜經由 ID-A
148. Dekoruma｜1001startup.id｜2026｜https://1001startup.id/company/dekoruma｜經由 ID-A
149. dekoruma.com eCommerce revenue｜ecommerceDB｜2025｜https://ecommercedb.com/store/dekoruma.com｜經由 ID-A
150. Dekoruma snags $15m in Series C1｜DealStreetAsia｜2021｜https://media.dealstreetasia.com/stories/indonesia-dekoruma-series-c1-funding-257304｜經由 T2
151. Dekoruma Announces 216.8 Billion Rupiah Funding, Plans for IPO｜DailySocial｜2021｜https://en.dailysocial.id/post/dekoruma-announces-funding-of-2168-billion-rupiah-to-achieve-positive-ebitda-soon-and-plans-an-IPO｜經由 T2
152. Dekoruma（Blibli 收購）｜CB Insights｜2024｜https://www.cbinsights.com/investor/dekoruma｜經由 T2
153. Sudah Galang Rp 300 Miliar, Fabelio Kini Pailit｜CNBC Indonesia｜2022｜https://www.cnbcindonesia.com/tech/20221012071341-37-379004/sudah-galang-rp-300-miliar-startup-fabelio-kini-pailit｜經由 T2
154. Startup Fabelio Resmi Diputus Pailit｜Bisnis.com｜2022｜https://teknologi.bisnis.com/read/20221010/266/1586117/startup-fabelio-resmi-diputus-pailit｜經由 T2
155. Investor Amerika Suntik Gravel Rp 216 Miliar｜Katadata｜2023｜https://katadata.co.id/digital/startup/656d6becb3021/investor-amerika-suntik-startup-konstruksi-gravel-rp-216-miliar｜經由 ID-A
156. Pengguna Kanggo Tembus 36 Ribu｜Investor.id｜2025｜https://investor.id/business/409706/pengguna-kanggo-tembus-36-ribu-layanan-perawatan-bangunan-kian-diminati｜經由 ID-A
157. Sejasa（SejasaPay）｜Sejasa｜2025｜https://www.sejasa.com/｜經由 ID-A
158. Interior Apartemen Studio 價格頁｜Tokopedia｜2026｜https://www.tokopedia.com/find/interior-apartemen-studio｜經由 ID-A
159. Biaya renovasi rumah per meter｜Mitra10 Blog｜2025｜https://www.mitra10.com/blog/biaya-renovasi-rumah-per-meter｜經由 ID-A
160. CSAP catat pendapatan Rp17,5 T di 2025（omnichannel）｜Industry.co.id｜2026｜https://www.industry.co.id/read/152024/csap-catat-pendapatan-rp175-t-di-2025-bagi-dividen-meski-daya-beli-lesu｜經由 ID-A
161. Tren arsitektur tahun 2026 di Indonesia（BIM／VR／AR）｜Immortal MG｜2025-12｜https://immortal-mg.com/2025/12/31/tren-arsitektur-tahun-2026-di-indonesia/｜經由 ID-A
162. Tren desain interior 2026（AI／智慧家庭）｜IDN Times｜2026｜https://www.idntimes.com/life/diy/tren-desain-interior-2026-c1c2-01-k7db6-fdyklf｜經由 ID-A
163. Tren desain interior 2026｜DGA Interior｜2026｜https://www.dga-interior.com/blog/tren-desain-interior-2026｜經由 ID-A

### 越南
164. Về Happynest｜Happynest｜2025｜https://v2.happynest.vn/gioi-thieu｜經由 VN-A
165. Happynest giúp hành trình làm nhà dễ dàng hơn（流量）｜Bongdaplus｜2023｜https://bongdaplus.vn/ben-ngoai-duong-piste/happynest-giup-hanh-trinh-lam-nha-cua-nguoi-viet-tro-nen-de-dang-hon-3981922305.html｜經由 VN-A
166. Happynest ra mắt ứng dụng chuyên về nhà ở｜VnExpress｜2021｜https://vnexpress.net/happynest-ra-mat-ung-dung-chuyen-ve-nha-o-4393392.html｜經由 VN-A
167. Ứng dụng Happynest｜Dân trí｜2021｜https://dantri.com.vn/kinh-doanh/ung-dung-happynest-giai-quyet-nhu-cau-tim-y-tuong-tim-chuyen-gia-va-sam-noi-that-20211128204409915.htm｜經由 VN-A
168. LG Architect Club｜Zing News｜2025｜https://tech.zingnews.vn/lg-architect-club-truyen-cam-hung-cong-nghe-vao-to-am-tuong-lai-post1558482.html｜經由 VN-A
169. Nền tảng số hỗ trợ tìm nhà thầu xây dựng｜VnExpress｜2026｜https://vnexpress.net/nen-tang-so-ho-tro-tim-nha-thau-xay-dung-5059125.html｜經由 VN-A
170. Top digital and social media trends in Vietnam 2026｜Elite Asia｜2026｜https://www.eliteasia.co/top-digital-and-social-media-trends-in-vietnam-in-2026/｜經由 VN-A
171. Leading social media platforms in Vietnam｜Statista｜2025｜https://www.statista.com/statistics/941843/vietnam-leading-social-media-platforms/｜經由 VN-A
172. TikTok "đẻ" ra việc mới cho lĩnh vực trang trí nội thất｜Diễn đàn Doanh nghiệp｜2024｜https://diendandoanhnghiep.vn/tiktok-de-ra-viec-moi-cho-linh-vuc-trang-tri-noi-that-10051203.html｜經由 VN-A
173. 10 cách tiếp cận khách hàng nội thất｜CleverAds｜—｜https://cleverads.vn/blog/10-cach-tiep-can-khach-hang-noi-that/｜經由 VN-A
174. Tìm kiếm khách hàng nội thất｜Giải pháp Web｜—｜https://giaiphapweb.vn/tim-kiem-khach-hang-noi-that/｜經由 VN-A
175. Mua chung cư nên chọn nhà giao thô hay hoàn thiện｜Tuổi Trẻ／PLO｜2025｜https://tuoitre.vn/plo/mua-chung-cu-nen-chon-nha-giao-tho-hay-hoan-thien-109586696.htm｜經由 VN-A
176. AiHouse（越南版）｜AiHouse｜2025｜https://www.aihouse.com/vi｜經由 VN-A
177. Khi AI thiết kế nội thất｜HAWA｜2025｜https://hawa.vn/khi-ai-thiet-ke-noi-that/｜經由 VN-A
178. 15 phần mềm AI thiết kế nội thất｜AWE｜2025｜https://awe.edu.vn/phan-mem-ai-thiet-ke-noi-that｜經由 VN-A
179. Các gian hàng giải pháp nhà thông minh hút khách tại Vietbuild 2025｜Mekong ASEAN｜2025｜https://mekongasean.vn/cac-gian-hang-giai-phap-nha-thong-minh-hut-khach-tai-vietbuild-2025-42065.html｜經由 VN-B
180. Những xu hướng công nghệ nổi bật tại Vietbuild Hà Nội 2025｜Nhân Dân｜2025｜https://nhandan.vn/ocop/nhung-xu-huong-cong-nghe-noi-bat-tai-trien-lam-quoc-te-vietbuild-ha-noi-2025-post866246.html｜經由 VN-B
181. XHOME Profile 2025｜XHOME｜2025｜https://xhomesg.com.vn/wp-content/uploads/2025/05/XHOME-Profile-2025.pdf｜經由 VN-A

### 泰國／菲律賓
182. HMPRO Listed Company Snapshot 3M/2025｜SET｜2025｜https://lssmedia.setlink.set.or.th/2025/3M/HMPRO-3M68-ListedCompanySnapshot-EN.html｜經由 T2
183. Wilcon Depot FY2024 results｜Inquirer Plus｜2025｜https://plus.inquirer.net/?p=256738｜經由 T2
184. Wilcon Depot (WLCON) Q4 2024 earnings summary｜Quartr｜2025｜https://quartr.com/events/wilcon-depot-inc-wlcon-q4-2024_FtvIy3pe｜經由 T2

來源總數：184（其中在地語言來源：中文 57、韓文 32、日文 19、繁中 19、印尼文 10、越南文 16；英文其餘）。所有 URL 均未於本輪開啟核對，依整合協議 §3／§10 由 WP6 逐條驗證。

---

## 附錄 A：本輪已規劃但未能執行的 20 條搜尋（供下一回合直接續跑）

1. 群核科技 招股书 2025 酷家乐 月活 付费企业 ARPU 海外 Coohom 定价
2. Coohom users 2025 pricing Southeast Asia Taiwan interior design SaaS
3. 오늘의집 MAU 거래액 2025 수수료율 집닥 누적 거래액 2025 매출
4. Qanvast 2025 users GMV Hometrust Renopedia Singapore renovation platform
5. 土巴兔 2024 年报 用户 收入 齐家网 2025 年报 GMV 抽成 获客成本
6. 好好住 用户数 2025 被窝 线索 小红书 家装 内容 流量 2025 博主
7. SUUMO リフォーム 利用者数 ホームプロ 累計 相談件数 リショップナビ 成約 2025
8. ANDPAD 導入社数 2025 ユーザー数 Photoruction 施工管理 SaaS 導入
9. CORENET X BIM Singapore requirements interior fit-out submission 2025
10. 香港 BIM 室內裝修 規定 發展局 通函 2025 裝修佬 DecoMan 用戶 2025 Decor8
11. 装配式装修 政策 2025 渗透率 住建部 装配式内装 试点
12. Singapore DfMA interior PPVC fit-out 2025; 系統櫃 市占 台灣 2025 市場規模
13. 三翼鸟 2025 门店 零售额 智家 APP MAU; Samsung SmartThings 인테리어 연동 2025
14. smart home penetration Asia renovation 2025 Xiaomi LIXIL Panasonic HomeX bundle
15. AI interior design tools survey designers 2025 adoption productivity; D5 Render users 2025 Enscape SketchUp Asia
16. Homestyler users 2025 Planner 5D users Spacely 導入社数 2025
17. 100室內設計 流量 設計師數 2025 收費 PULO 媒合 件數 2025 設計家 searchome 流量
18. Dekoruma 2025 Blibli pengguna; Livspace AI 2025; HomeLane SpaceCraft AI
19. Recommend.my Atap.co 2025 users Malaysia renovation platform Kaodim; Happynest 2025 GMV
20. renovation lead cost per lead Asia 2025 benchmark Instagram YouTube TikTok LINE Facebook interior design leads share survey
