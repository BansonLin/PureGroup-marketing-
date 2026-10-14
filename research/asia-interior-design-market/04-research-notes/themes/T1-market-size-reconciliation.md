# T1：市場規模數據彙整與可比性校準（Market-size data reconciliation across research houses and official statistics）

研究日期：2026-10-08｜涵蓋市場：日本、南韓、新加坡、香港、台灣、中國大陸、馬來西亞、泰國、越南、印尼、菲律賓、印度（12 市場）＋亞太整體

> **研究方法備註**
> - 本檔為兩輪研究合併：前一輪（約 36 次搜尋，搜尋額度用罄後中斷於 §2）＋本輪（20 次 WebSearch，含中、日、韓、泰文查詢）。本環境**禁止網頁抓取（WebFetch／curl）**，所有數字均來自搜尋引擎對來源網頁的摘錄，**未逐頁開啟原文核對**，驗證階段（04-research-notes/verification）須逐一重開 URL。
> - 匯率：採「2025–2026 年概略參考匯率」，**驗證階段須以當日官方匯率覆寫**：USD/TWD 31.5；USD/JPY 150；USD/KRW 1,400；USD/CNY 7.20；USD/SGD 1.33；USD/HKD 7.80；USD/MYR 4.40；USD/THB 33；USD/VND 26,000；USD/IDR 16,000；USD/PHP 57；USD/INR 86。（T2 檔採 USD/TWD 31.0、前稿採 32.2，整合時請統一。）
> - 信心等級依 02-integration-protocol：高＝≥3 獨立來源一致；中＝2 來源一致或單一官方來源；低＝單一研究機構／轉載；極低＝來源品質可疑。

---

## 1. 摘要

1. 亞太「室內裝修設計市場」**不存在單一可引用的官方總量**。研究機構的亞太數字依口徑從 Mordor 的 DIY 居家修繕 USD 64 億（2025）、Grand View 的室內設計 USD 305 億（2024）、Research and Markets 的 DIY USD 923 億（2025）、Ken Research 的住宅翻修 USD 1,600 億（2025）到 Fortune Business Insights 的住宅翻修 USD 6,050 億（2025），差距近 100 倍，完全取決於定義（設計費／設計＋施工／住宅翻修／居家修繕零售／傢俱）。
2. 真正具統計基礎的國家級錨點只有：日本矢野経済研究所住宅リフォーム市場 **7 兆 5,119 億円（2025 推計，+2.5%）**；南韓建設產業研究院（건산연）리모델링市場 **37 兆韓元（2025，2020 年發布之預測）**；中國智研咨詢（經中裝協官網轉載）建築裝飾總產值 **5.78 兆人民幣（2023）**與艾瑞家裝市場 **3.78 兆人民幣（2025 預測）**；香港統計處「非地盤建造工程」（含樓房裝飾、修葺保養）**HK$873 億（2024）**；泰國 SEC 上市文件引用之居家修繕產業 **4,795 億泰銖（2023）**。
3. 台灣唯一流通的「裝修年產值 5,500 億元（2025）」來自民營媒合平台（100 室內設計／數字科技）「依財政部數據推估」，**非官方統計**；內政部建築研究所早期研究推估住宅裝修市場僅約 776 億～近 2,000 億元，兩者口徑與年代差距極大；財政部營利事業家數及銷售額統計（財政統計月報表 3-9～3-12）可取得「室內裝潢業」官方銷售額，但本輪未能開啟。
4. 「室內設計服務費」口徑在各國的研究機構估值大致為：中國 USD 270 億（Grand View，2025）／1,744 億人民幣（智研，2024）、日本 USD 61–65 億（2024–2025）、印度 USD 314–369 億（2025）、南韓 USD 40 億（2025）、新加坡 USD 7.7 億（2024）、印尼 USD 8.2 億（2023）；其中印度數字相對 GDP 明顯偏高（約 0.9%），疑含傢俱家飾。
5. 商用裝修（fit-out）缺乏可信的亞太總量（DataM 推算亞太約 USD 181 億、Dataintelo 商用室內設計亞太 USD 117 億，2024–2025，皆低信心）；較可靠的是 JLL／Cushman & Wakefield／Knight Frank／Turner & Townsend 2026 年版的**單位成本**：亞太辦公室平均 USD 1,550/m²（JLL），新加坡 USD 2,029/m²、東京 1,994、台北 1,593（Knight Frank）。
6. 研究機構數字有明確「回收／套版」證據：Grand View 與 Mordor 全球室內設計 2024 年值完全相同（USD 1,379.3 億）；Grand View 中國頁面同時出現「中國占全球 14.5%」與「52.1%」；Ken Research 同一國家在不同頁面給出 USD 82／86／100 億（印尼）三個 2025 年值；Mobility Foresights 泰國居家修繕 USD 3,104 億（2025）超過泰國 GDP 一半。
7. 建議最終報告以「口徑分層可比區間」呈現：(a) 住宅翻修支出、(b) 室內設計服務費、(c) 商用裝修；並以 IMF WEO 2026 年 4 月人均 GDP（經 Worldometers 轉載）正規化。以住宅翻修／GDP 比率看，日本 1.1%、南韓 1.2–1.4%、中國 2.7%（家裝）、香港 2.6%（含小型新建）、台灣 1.9%（5,500 億口徑，偏高）、泰國 2.5%（含建材零售）；東南亞其餘四國與印度 <1%。

---

## 2. 關鍵問題一：亞太整體估計值彙整（Asia-Pacific aggregates）

### 2.1 室內設計（Interior design / design services）口徑

| 機構 | 市場名稱（原文） | 基準值 | 預測值 | CAGR | 定義／地理範圍 | 來源 | 信心 |
|---|---|---|---|---|---|---|---|
| Grand View Research | Asia Pacific Interior Design Market | **USD 305 億（2024）** ≈ NT$9,608 億 | USD 416 億（2030） | 5.5%（2025–2030）；新版 5.9%（2026–2033） | 室內設計（新建＋翻修；住宅＋商用）；new construction 最大、remodeling 成長最快；亞太區域頁 | [GVR APAC](https://www.grandviewresearch.com/horizon/outlook/interior-design-market/asia-pacific) | 中 |
| Grand View Research | Interior Design Market（全球） | USD 1,857 億（2025）；舊版 USD 1,379.3 億（2024），CAGR 4.3% | — | — | 全球；中國頁稱中國占 14.5%（2025）但另稱 52.1%，自相矛盾 | [GVR Global](https://www.grandviewresearch.com/industry-analysis/interior-design-market-report)；[GVR China](https://www.grandviewresearch.com/horizon/outlook/interior-design-market/china) | 低–中 |
| Mordor Intelligence | Interior Design Services Market（全球） | 亞太占 **38.39%（2025）**，為最大區域；全球 USD 1,379.3 億（2024）→ 1,771.3 億（2029），CAGR 5.13% | — | — | 設計服務；**無亞太獨立報告**；2024 全球值與 GVR 完全相同（疑回收） | [Mordor](https://www.mordorintelligence.com/industry-reports/interior-design-services-market) | 低–中 |
| Cognitive Market Research | Asia Pacific Interior Design Market | USD 246.9 億（2021）→ **USD 319.3 億（2025）** ≈ NT$1.006 兆 | USD 530.7 億（2033） | 6.558% | 室內設計（未明示是否含施工） | [CMR](https://www.cognitivemarketresearch.com/interior-design-market-report) | 低 |
| Transpire Insight | Asia Pacific Interior Design Market | **USD 523 億（2025）** | USD 845 億（2033） | 6.11%（2026–2033） | 未明示 | [Transpire](https://www.transpireinsight.com/report/asia-pacific-interior-design-market) | 極低 |
| Fortune Business Insights | Interior Design Market（全球） | USD 1,459.6 億（2025）→ 2,143.5 億（2034） | — | — | 第三方轉載稱亞太約 38%、中國占亞太 16% | [FBI](https://www.fortunebusinessinsights.com/interior-design-market-112750) | 低 |
| Technavio | Interior Design Services 2025–2029（全球） | 無基準值；亞太貢獻全球增量 35% | — | — | 中國為亞太最大（2024） | [Technavio](https://www.technavio.com/report/interior-design-services-market-industry-analysis) | 低 |
| Dataintelo | Commercial Interior Design（全球） | 亞太 **USD 117 億（2025）**，占 37.2% | — | — | 僅商用設計 | [Dataintelo](https://dataintelo.com/report/commercial-interior-design-market-report) | 低 |
| Mordor Intelligence | APAC Interior Design Software | USD 15.3 億（2025） | USD 28.7 億（2031） | 11.08% | **僅軟體**（常被誤當室內設計市場） | [Mordor SW](https://www.mordorintelligence.com/industry-reports/apac-interior-design-software-market) | 中 |

### 2.2 住宅翻修／居家修繕（Home renovation / remodeling / home improvement）口徑

| 機構 | 市場名稱 | 基準值 | 預測值 | CAGR | 定義／範圍 | 來源 | 信心 |
|---|---|---|---|---|---|---|---|
| Fortune Business Insights | Home Renovation Market（亞太） | **≈USD 6,050 億（2025）**（全球 29.5%）≈ NT$19.1 兆；USD 6,290 億（2026） | — | 亞太為最快 CAGR（2025–2032） | 住宅翻修（含施工＋材料） | [FBI Reno](https://www.fortunebusinessinsights.com/home-renovation-market-112345) | 低 |
| Fortune Business Insights | Home Improvement Market（全球） | USD 9,458.6 億（2025），亞太約 25% → ≈USD 2,360 億（本研究推算） | — | — | 居家修繕（產品＋服務） | [FBI HI](https://www.fortunebusinessinsights.com/home-improvement-market-113207) | 低 |
| Ken Research | Asia-Pacific Residential Remodeling | **USD 1,600 億（2025）** ≈ NT$5.04 兆 | USD 2,180 億（2032） | 4.5% | 廚衛、電氣、HVAC、隔熱、智慧家居、結構修復、無障礙改造 | [Ken APAC](https://www.kenresearch.com/industry-reports/asia-pacific-residential-remodeling-market) | 低–中 |
| Dataintelo | Home Remodeling（全球） | 全球 USD 1.14 兆（2025），亞太 24.1% → ≈USD 2,750 億（本研究推算） | — | — | 廚房、浴室、室內外增建 | [Dataintelo](https://dataintelo.com/report/global-home-remodeling-market) | 低 |
| Global Market Insights | Remodeling Market | 亞太占全球 16.0%（2025）；中國 ≈USD 1,000 億（2025） | — | 5.4%（2026–2035） | 翻修 | [GMI](https://www.gminsights.com/industry-analysis/remodeling-market) | 低 |
| Grand View Research | Residential Remodeling | 亞太占 33.6%（2025），最快成長 | — | — | 住宅翻修 | [GVR Remodel](https://www.grandviewresearch.com/industry-analysis/residential-remodeling-market-report) | 低 |
| Deep Market Insights（前稿） | APAC Home Remodeling | USD 1,110.8 億（2025） | USD 1,790.8 億（2034） | 5.39% | 住宅翻修；同系列報告有套版錯誤 | [DMI](https://deepmarketinsights.com/vista/insights/home-remodeling-market/asia-pacific) | 低 |
| Market Data Forecast（前稿） | APAC Home Improvement | USD 943.5 億（2025） | USD 1,492.8 億（2034） | 5.23% | 居家修繕整體 | [MDF](https://www.marketdataforecast.com/market-reports/asia-pacific-home-improvement-market) | 低 |
| IMARC | Home Improvement Services（全球） | USD 3,854 億（2025） | USD 5,384 億（2034） | 3.67% | 僅服務；無亞太拆分 | [IMARC](https://www.imarcgroup.com/home-improvement-services-market) | 低–中 |
| 未具名（EIN Presswire，疑 TBRC） | Home Improvement Services（亞太） | USD 1,170 億（2025） | USD 1,680 億（2030） | 7% | 服務 | [EIN](https://www.einnews.com/pr_news/948211131/) | 極低 |
| Research and Markets | APAC DIY Home Improvement | **USD 923.2 億（2025）** | USD 1,178.2 億（2030） | <5% | DIY 零售（含家居中心、五金） | [R&M DIY](https://www.researchandmarkets.com/report/asia-pacific-diy-home-improvement-market) | 低–中 |
| Verified Market Research | APAC DIY Home Improvement | USD 922 億（2024） | USD 1,470 億（2032） | — | DIY | [VMR](https://www.verifiedmarketresearch.com/product/asia-pacific-diy-home-improvement-market/) | 低（與 R&M 近似，疑同源） |
| Mordor Intelligence | APAC DIY Home Improvement | **USD 64.2 億（2025）**；中國占 31.88%；印度 CAGR 10.95% | USD 87.9 億（2031） | 5.38% | DIY 自購材料；與 R&M 同名市場差 14 倍 | [Mordor DIY](https://www.mordorintelligence.com/industry-reports/asia-pacific-diy-home-improvement-market) | 中 |
| GlobalData（前稿） | Retail home improvement & gardening products, APAC | USD 2,830 億（2021） | — | — | 零售產品 | [GlobalData](https://www.globaldata.com/data-insights/retail-and-wholesale/market-size-of-retail-home-improvement-and-gardening-products-in-asia-pacific/) | 中（年份舊） |
| Statista | APAC home improvement market size in selected countries | 2022 年、以歐元計、付費；中國最高；定義含 DIY 店、五金、建材、家飾店 | — | — | 零售 | [Statista](https://www.statista.com/statistics/1474530/apac-home-improvement-market-size-in-selected-countries) | 無公開數字 |

### 2.3 商用裝修（Commercial fit-out）口徑

| 機構 | 市場 | 數值 | 定義 | 來源 | 信心 |
|---|---|---|---|---|---|
| DataM Intelligence | Interior Fit Out（全球） | USD 644.7 億（2024）；亞太 28.1% → ≈USD 181 億（本研究推算） | 室內裝修工程 | [DataM](https://www.datamintelligence.com/research-report/interior-fit-out-market) | 低 |
| Coherent Market Insights | Interior Fit Out（全球） | USD 785.8 億（2026），CAGR 8.3% 至 2033 | 同上 | [Coherent](https://www.coherentmarketinsights.com/market-insight/interior-fit-out-market-6113) | 低 |
| Astute Analytica | Southeast Asia Interior Fit-Out Furniture | USD 89.3 億（2023）→ 133.3 億（2032） | 裝修用傢俱 | [Astute](https://www.astuteanalytica.com/industry-report/southeast-asia-interior-fit-out-furniture-market) | 低 |
| Credence Research | China Interior Fit Out | USD 73 億（2023）→ 154 億（2032） | 中國（含香港為華南重點城市） | [Credence CN](https://www.credenceresearch.com/report/china-interior-fit-out-market) | 低 |
| JLL | APAC Office Fit-Out Cost Guide 2026 | 區域平均 **USD 1,550/m²**；當地幣別年增 2–5%；27 城 14 國 | 辦公室單位成本（非市場總量） | [JLL](https://www.jll.com/en-in/guides/apac-fit-out-costs-guide)；[cfotech](https://cfotech.asia/story/jll-warns-asia-pacific-office-fit-out-costs-keep-rising) | 高 |
| Knight Frank | APAC fit-out 2026（Q4 2025 資料，23 城） | 新加坡 USD 2,029/m²、東京 1,994、台北 1,593、金邊 375 | 基本／中階／高階規格 | [irei](https://irei.com/publications/article/asia-pacific-office-fit-out-costs/) | 高 |
| Cushman & Wakefield | Office Fit Out Cost Guide APAC 2026 | 印度 USD 65–73/ft²；東京 215、雪梨 161、新加坡 140 | 含傢俱、機電、建築、AV/IT | [C&W](https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office)；[ConstructionWorld](https://www.constructionworld.in/latest-construction-news/real-estate-news/india-leads-asia-pacific-in-fit-out-cost-efficiency/88743) | 高 |
| Turner & Townsend | Global office fit-out cost guide 2026（APAC） | 雪梨 A$7,221/m²（最貴）；東京 ¥729,406/m²；大阪 ¥706,834；吉隆坡 RM6,908/m² | 高階規格 | [T&T](https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026/asia-pacific) | 高 |

### 2.4 結論

- Mordor、IMARC、Technavio、Statista、Research and Markets、Allied、Precedence、Expert Market Research、6Wresearch 皆**無**「亞太室內設計市場」獨立公開數字（6Wresearch 有 2021–2027 版頁面但無摘要數值）；只有 Grand View（USD 305 億，2024）與 Cognitive（USD 319 億，2025）兩個同量級估計，可作為「亞太室內設計（含設計＋部分施工）」的中信心區間 **USD 300–320 億（2024–2025）**。
- 住宅翻修口徑的亞太估計散布於 USD 1,100–6,050 億；**以各國官方錨點加總**（日本 USD 500 億＋南韓 260 億＋中國家裝 5,250 億＋香港 112 億＋台灣 175 億＋泰國 145 億）已達約 USD 6,400 億，顯示 Fortune 的 USD 6,050 億並非不可能，而 Ken 的 USD 1,600 億明顯低估（可能排除中國或僅計結構性翻修）。
- 商用裝修沒有可信總量；建議以成本指南的單位成本 × 各市場辦公／零售竣工面積自行推算（留待整合階段）。

---

## 3. 關鍵問題二：各國估計值與權威本地來源

### 3.1 日本（Japan）

**權威來源：矢野経済研究所（Yano Research Institute）「住宅リフォーム市場に関する調査」**

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| 住宅リフォーム市場規模（推計） | **7 兆 5,119 億円（+2.5%）** ≈ USD 500.8 億 ≈ NT$1.578 兆 | 2025 | [矢野 2026 年 7 月新聞稿（dreamnews）](https://www.dreamnews.jp/press/0000356164)；[ibnewsnet](https://online.ibnewsnet.com/sp/gy260717-01.html)；[s-housing](https://www.s-housing.jp/archives/427008) | 高（官方推計，三家媒體一致轉載） |
| 同上（前一年） | 7 兆 3,470 億円（−0.5%） | 2024 | [矢野 2025 年 8 月新聞稿](https://www.yano.co.jp/press-release/show/press_id/3877)；[BCI](https://online.bci.co.jp/article/detail/3587)；[日經](https://www.nikkei.com/article/DGXZRSP695565_Q5A820C2000000/) | 高 |
| 2025 年預測（2025 年 8 月版） | 7.3 兆円（−0.7%） | 2025F | 同上 | 高（已被實績 7.51 兆取代） |
| 2026 年預測 | **7.7 兆円（+1.9%）** ≈ USD 513 億 | 2026F | [矢野 2026 年版報告](https://www.yano.co.jp/market_reports/C68101800) | 高 |
| 推升因素 | 建材與人工成本上升推高工事單價；窗戶斷熱改修等政府補助帶動擴大工程範圍；部分需求因漲價預期提前下單 | 2025 | [s-housing](https://www.s-housing.jp/archives/427008) | 高 |
| 風險 | 中東情勢造成建材與住宅設備機器停止接單、交期延後 | 2026 | 同上 | 中 |

- 矢野「住宅リフォーム市場」定義（歷年新聞稿之標準口徑）：10 m² 超の増改築工事＋10 m² 以下の増改築工事＋設備修繕・維持関連＋家具・インテリア等；本輪摘錄未重述定義，列為待驗證（中信心）。

**研究機構（室內設計口徑）**

| 機構 | 數值 | CAGR | 來源 | 信心 |
|---|---|---|---|---|
| Grand View Research | **USD 64.9 億（2024）** → 89.7 億（2030）≈ NT$2,045 億 | 5.7%（2025–2030）；新建最大、翻修最快 | [GVR Japan](https://www.grandviewresearch.com/horizon/outlook/interior-design-market/japan) | 中 |
| Cognitive Market Research | USD 61.5 億（2025）→ 90.1 億（2033） | 4.879% | [CMR](https://www.cognitivemarketresearch.com/interior-design-market-report) | 低 |
| Renub Research | USD 63.9 億（2024）→ 90.6 億（2033） | 3.95%（2025–2033） | [Renub](https://www.renub.com/japan-interior-design-market-p.php)；[openPR](https://www.openpr.com/news/4294510/) | 低 |
| Spherical Insights | USD 63.8 億（2024） | 6.08%（2025–2035） | [Spherical](https://www.sphericalinsights.com/reports/japan-interior-design-market) | 低 |
| Credence Research | Japan Interior Fit Out（未取得數值） | — | [Credence JP](https://www.credenceresearch.com/report/japan-interior-fit-out-market) | 無資料 |

- 四家研究機構日本「室內設計」2024–2025 年值集中於 **USD 61–65 億**（≈ 住宅リフォーム市場的 12–13%），為少見的跨機構一致案例，但疑為互相抄錄而非獨立估計。
- 商用成本：東京高階辦公室 fit-out ¥729,406/m²（T&T 2026）、USD 1,994/m²（Knight Frank）、USD 215/ft²（C&W），為亞太最高群。

### 3.2 南韓（South Korea）

**權威來源：한국건설산업연구원（CERIK，建設產業研究院）**

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| 리모델링 시장（개수＋유지·보수） | 30 조원（2020）→ **37 조원（2025）**≈ USD 264 億 ≈ NT$8,325 億 → 44 조원（2030） | 2020 年發布之預測 | [CERIK 新聞稿](https://www.cerik.re.kr/board/press/589)；[국토일보](https://www.ikld.kr/news/articleView.html?idxno=223589)；[아시아경제](https://view.asiae.co.kr/article/2020091610320656635) | 中（官方研究院，但為 5 年前預測，無 2025 實績） |
| 其中 건축물 리모델링（改修） | 17 조 2,930 억（2020）→ 23 조 3,210 억（2025）→ 29 조 3,500 억（2030） | CAGR 5.4% | 同上 | 中 |
| 其中 유지·보수（維護） | 12 조 7,950 억（2020）→ 13 조 7,590 억（2025）→ 14 조 7,230 억（2030） | CAGR 1.4% | 同上 | 中 |
| 신영증권（Shinyoung Securities）인테리어 리모델링 | 25.4 조（2020）→ **32.4 조（2025）**≈ USD 231 億 → 46 조（2030） | 證券研究 | [대한전문건설신문](https://www.koscaj.com/news/articleView.html?idxno=111927) | 低–中 |

- 媒體常將「17.3 조（2020 建築物리모델링）」與「37 조（2025 含維護）」並列，造成口徑混淆（[서울파이낸스](https://www.seoulfn.com/news/articleView.html?idxno=395470)）。
- 統計廳（통계청）「건설업조사」未在本輪搜得實測數字（缺口）。

**研究機構**

| 機構 | 數值 | CAGR | 來源 | 信心 |
|---|---|---|---|---|
| Cognitive Market Research（室內設計） | **USD 39.9 億（2025）**→ 65.2 億（2033）≈ NT$1,257 億 | 6.343% | [CMR](https://www.cognitivemarketresearch.com/interior-design-market-report) | 低 |
| Ken Research（傢俱＋室內設計） | USD 126 億（2025）→ 165.5 億（2031）；另一頁 USD 172 億（2031），CAGR 5.6% | 4.65% | [Ken KR](https://www.kenresearch.com/industry-reports/south-korea-furniture-and-interior-design-market)；[Ken KR2](https://www.kenresearch.com/south-korea-furniture-interiors-market) | 低（同機構兩值矛盾） |
| Credence（豪宅設計） | USD 47.0 億（2023）→ 69.0 億（2032） | 4.35% | [Credence KR](https://www.credenceresearch.com/report/south-korea-luxury-interior-design-market) | 低 |
| Grand View（家居用品） | USD 141.1 億（2024） | 9.9% | [GVR HF](https://www.grandviewresearch.com/horizon/outlook/home-furnishing-market/south-korea) | 中（非裝修） |
| 6Wresearch（室內設計 2025–2031） | 頁面無數值 | — | [6W KR](https://www.6wresearch.com/industry-report/south-korea-interior-design-market-outlook) | 無資料 |

### 3.3 中國大陸（China）

**權威來源：中國建築裝飾協會（CBDA 中装协）、國家統計局、艾瑞咨詢（iResearch）、智研咨詢**

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| 建築裝飾行業完成工程總產值（智研，經中裝協官網轉載） | 4.49 萬億（2019）→ **5.78 萬億人民幣（2023）**≈ USD 8,028 億 ≈ NT$25.3 兆 | 2023 | [中裝新網 2025-06-30](http://www.cbda.cn/html/yj/20250630/142674.html)；[報告大廳](https://m.chinabgao.com/info/1248319.html) | 中（另一來源標為 2021 年值，年份有疑） |
| 中裝協「十四五」目標 | 2025 年產值 6.5 萬億 | 目標 | 同上 | 高（規劃文件） |
| 公共建築裝飾產值 | 2.2 萬億 | 2023 | [搜狐轉載](https://www.sohu.com/a/810449844_121388254) | 低 |
| 中裝協 2024 年度行業綜合數據統計 | 已於 2025-12 發布，**企業樣本口徑**，摘要無總產值 | 2024 | [中裝新網 2025-12-19](http://www.cbda.cn/html/hyyj/20251219/143631.html)；[知乎解讀](https://zhuanlan.zhihu.com/p/1986774932944873419) | 待驗證 |
| 艾瑞：家裝市場規模 | >3 萬億（2022，+7.8%）；預測 **3 兆 7,802 億（2025）**≈ USD 5,250 億 ≈ NT$16.5 兆 | 2025F | [艾瑞 2023 家裝報告 PDF](https://zhongzhihui.oss-cn-beijing.aliyuncs.com/industryPdf/%E8%89%BE%E7%91%9E%E5%92%A8%E8%AF%A2%EF%BC%9A2023%E5%B9%B4%E4%B8%AD%E5%9B%BD%E5%AE%B6%E8%A3%85%E8%A1%8C%E4%B8%9A%E7%A0%94%E7%A9%B6%E6%8A%A5%E5%91%8A.pdf)；[華聲](https://m.voc.com.cn/xhn/news/202401/19324088.html) | 中（2023 年預測，未見 2025 更新） |
| 報告大廳：家居家裝市場 | 2.76 萬億（2024）→ 3.28 萬億（2025E） | 2024 | [報告大廳](https://m.chinabgao.com/info/1274794.html) | 低（無原始出處） |
| 智研：建築室內設計行業規模 | 2,511.2 億（2021）→ **1,743.9 億（2024）**≈ USD 242 億；住宅 660.6 億、公建 1,083.3 億；預測 2,130.3 億（2029） | 2024 | [智研 1221629](https://www.chyxx.com/industry/1221629.html)；[智研 1213062](https://www.chyxx.com/industry/1213062.html) | 中 |
| 國家統計局：建築業增加值 | 89,949 億（+3.8%）；房地產開發投資 100,280 億（−10.6%） | 2024 | [中裝新網轉載](http://www.cbda.cn/html/yj/20250312/141927.html) | 高 |
| 中建協：建築業總產值 | 326,501.11 億（+3.85%） | 2024 | [陝西建協](https://www.sxjzy.org/h-nd-38035.html) | 高 |

**研究機構**

| 機構 | 數值 | CAGR | 來源 | 信心 |
|---|---|---|---|---|
| Grand View（室內設計） | **USD 269.5 億（2025）**→ 443 億（2033）≈ NT$8,489 億；占全球 14.5% | 6.5%（2026–2033） | [GVR China](https://www.grandviewresearch.com/horizon/outlook/interior-design-market/china) | 中（與智研 1,744 億人民幣≈USD 242 億接近） |
| Credence（室內設計） | USD 164.0 億（2023）→ 285 億（2032） | — | [Credence CN](https://www.credenceresearch.com/report/china-interior-design-market) | 低 |
| GMI（翻修） | ≈USD 1,000 億（2025） | — | [GMI](https://www.gminsights.com/industry-analysis/remodeling-market) | 低 |
| Mordor（家用傢俱） | USD 658.3 億（2025） | — | [Mordor CN furn](https://www.mordorintelligence.com/industry-reports/china-home-furniture-market) | 中（非裝修） |
| Mordor DIY（亞太）中國占比 | 31.88%（2025）→ ≈USD 20.5 億 | — | [Mordor DIY](https://www.mordorintelligence.com/industry-reports/asia-pacific-diy-home-improvement-market) | 中 |

### 3.4 台灣（Taiwan）

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| 「裝修年產值上看 5,500 億元」（100 室內設計／數字科技，稱依財政部數據推估） | **NT$5,500 億** ≈ USD 174.6 億 | 2025 | [聯合報 9245511](https://udn.com/news/story/7241/9245511)；[聯合報 9242628](https://udn.com/news/story/7241/9242628)；[PChome](https://news.pchome.com.tw/finance/idn/20251231/index-76714660650609224003.html)；[安傳媒](https://annewsmedia.com/2025/12/30/market-news/14836/) | 低（單一民營平台推估，計算方式未公開；多家媒體轉載同一新聞稿只算 1 源） |
| 內政部建築研究所「住宅裝修市場規模推估方法之研究」：室內裝修業＋土木包工業＋營造業之住宅裝修 | 約 NT$776 億／年；裝修材料約 153 億；另稱「近年接近 2,000 億」 | 依 84／90／91 年普查資料 | [ABRI](https://www.abri.gov.tw/News_Content_Table.aspx?n=807&s=38057)；[人間福報](https://www.merit-times.com.tw/NewsPage.aspx?unid=146493) | 中（官方委託研究，但資料年代久遠） |
| 經濟部產業發展署電子報：裝修產業年產值 | NT$1,100 億 | 十餘年前，年度未標 | [IDA 電子報](https://www.ida.gov.tw/ctlr?PRO=epaper.rwdEpaperView&id=2479) | 低 |
| 財政部營利事業家數及銷售額（可查「室內裝潢業」） | 財政統計月報表 3-9～3-12／財政統計資料庫；本輪未取得數字 | 2024–2025 | [財政部](https://www.mof.gov.tw/singlehtml/1412?cntId=63687)；[財政資訊中心 112 年營業稅統計表](https://www.fia.gov.tw/singlehtml/43?cntId=141a13f4f22c474886ffac80cfe5324e) | 缺口 |
| 小規模營業人起徵點：裝潢業等銷售勞務業自 114-1-1 起調至月銷售額 5 萬元 | 受惠約 12 萬家（跨業別）、減稅 10.68 億 | 2025 | [工商時報](https://www.ctee.com.tw/news/20241212702008-430503)；[財政部稅務入口網](https://www.etax.nat.gov.tw/etwmain/tax-info/network-transaction-taxtation-area/press/PEwQK1V) | 高（政策，非市場規模） |
| 商用成本：台北辦公室 fit-out | USD 1,593/m² | 2026 | [Knight Frank via irei](https://irei.com/publications/article/asia-pacific-office-fit-out-costs/) | 高 |

- 全國聯合會（中華民國室內設計裝修商業同業公會全國聯合會）、台北市（TAID）、新北市公會網站摘要均**無市場規模統計**（[idroc](https://www.idroc.org.tw/)；[taid](https://taid.org.tw/)；[tpdc](https://www.tpdc.org.tw/)）。
- 5,500 億口徑若對應 2025 年人均 GDP USD 39,489、人口約 2,340 萬，相當於 GDP 的 1.9%，**高於日本（1.1%）與南韓（1.2–1.4%）**，除非含新成屋交屋裝修＋商業空間＋傢俱家電，否則偏高；建議最終報告以「官方 2,000 億級（住宅）～民間推估 5,500 億（全口徑）」區間呈現。

### 3.5 香港（Hong Kong）

**權威來源：政府統計處（C&SD）「建造工程完成量按季統計調查」**

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| 主要承建商完成建造工程名義總值（全年，臨時） | **HK$2,866 億（−1.4%）**≈ USD 367 億 | 2025 | [政府新聞公報 2026-03-12](https://www.info.gov.hk/gia/general/202603/12/P2026031200295.htm) | 高 |
| 「非地盤」建造工程（小規模新建工程、樓房裝飾、樓宇修葺及保養、非地盤電器安裝及保養） | **HK$873 億（−6.0%）**≈ USD 112 億 ≈ NT$3,526 億 | 2024 全年 | [新聞公報 2025-03-11](https://www.info.gov.hk/gia/general/202503/11/P2025031100233.htm) | 高 |
| 非地盤：2025 Q1／Q2／Q4 | HK$206 億（−3.9%）／205 億（−0.7%）／222 億（−3.0%）；Q3 未取得 → 2025 全年推估約 HK$850 億 | 2025 | [Q1](https://www.censtatd.gov.hk/en/press_release_detail.html?id=5590)；[Q2](https://www.info.gov.hk/gia/general/202509/11/P2025091100340.htm)；[Q4](https://www.info.gov.hk/gia/general/202603/12/P2026031200295.htm) | 高（季度）／中（全年推估） |
| 2026 Q1 總值 | HK$727 億（+2.9%） | 2026 | [文匯網](https://www.wenweipo.com/a/202606/11/AP6a2a9131e4b0b49ad1bef21b.html) | 高 |
| 設計產業增加值（HKTDC，含產品、時裝等所有設計） | HK$41 億（−6%）；>7,000 家設計公司 | 2022 | [HKTDC](https://research.hktdc.com/en/article/MzEzOTE1MDI5) | 中（非裝修口徑） |
| 發展局統計：主要承建商建造工程總值（按工程類別） | 可按「裝修、修葺及保養」細分，本輪未開啟 | — | [DEVB](https://www.devb.gov.hk/tc/publications_and_press_releases/figures_and_statistics/gross_value/index.html) | 缺口 |
| 商用成本：辦公室 fit-out | HKD 400–1,200/ft²（承包商報價） | 2026 | [rokydesign](https://rokydesign.com/integrated-design-build-office-fit-out-hong-kong/) | 低 |

- 「非地盤」口徑**高估**裝修市場（含小型新建與機電保養），但為 12 市場中唯一按季公布、且涵蓋住宅＋商用翻修的官方數列；香港住宅裝修市場無獨立估計（研究機構報告多把香港併入中國）。

### 3.6 新加坡（Singapore）

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| Frost & Sullivan（港交所上市文件）：新加坡 interior fitting-out 市場 | **SGD 48.751 億（2022E）**≈ USD 36.7 億 ≈ NT$1,155 億 | 2022 預測 | [HKEX 2020 招股書行業概覽](https://www1.hkexnews.hk/listedco/listconews/sehk/2020/0507/9270144/sehk19101000768.pdf) | 中（第三方顧問、上市文件，但為 2020 年預測） |
| DeepMarket Insights／GrowthHQ：室內設計服務 | USD 7.7 億（2024）→ 12.2 億（2033） | 2024 | 轉引自 [designbureau.sg](https://designbureau.sg/insights/commercial-interior-design-trends-statistics-singapore-2026-pQ5n8w/) | 低 |
| 6Wresearch：室內設計 CAGR | 5.9%（2025–2031），住宅＋商用 | — | [6W SG](https://www.6wresearch.com/industry-report/singapore-interior-design-market-outlook) | 低 |
| Ken Research：傢俱＋家飾 | USD 11.3 億（2025）；排除家電、二手、獨立設計費、辦公傢俱、出口 | 2025 | [Ken SG](https://www.kenresearch.com/industry-reports/singapore-furniture-home-decor-market) | 低 |
| DOS 服務業調查：服務業營業收入總額 | S$6,087 億（全服務業；無室內設計細項摘要） | 2024 | [SingStat](https://www.singstat.gov.sg/-/media/files/visualising_data/infographics/industry/singapore-services-sector.ashx)；[SingStat services](https://www.singstat.gov.sg/find-data/explore-data-themes/industry/services/latest-news-data) | 高（但無細項） |
| 消費端單價：HDB／公寓全屋裝修 SGD 30,000–60,000；純設計 SGD 1,500–15,000 | 2025 | [ovon-d](https://www.ovon-d.com/2025/06/18/interior-design-in-singapore-costs-in-2025-and-whats-actually-worth-it/) | 低 |
| 商用成本：辦公室 fit-out | USD 2,029/m²（Knight Frank，亞太最高）；USD 140/ft²（C&W） | 2026 | [irei](https://irei.com/publications/article/asia-pacific-office-fit-out-costs/)；[C&W](https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office) | 高 |

- 新加坡無 2025 年官方裝修市場規模；SingStat Table Builder「Key Indicators by Detailed Industry in All Services Industries」可能含 SSIC 74 specialised design 細項（缺口）。

### 3.7 馬來西亞（Malaysia）

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| Ken Research：傢俱＋室內設計（含設計費、家飾） | **USD 24.3 億（2025）**≈ RM 107 億 ≈ NT$765 億 | 2025 | [Ken MY](https://www.kenresearch.com/industry-reports/malaysia-furniture-and-interior-design-market) | 低（前稿另見同機構 USD 54.2 億，矛盾） |
| Ken Research：居家修繕（材料、工具、塗料、五金、專業施工） | ≈USD 10 億（2025）≈ RM 44 億 | 2025 | [Ken MY HI](https://www.kenresearch.com/industry-reports/malaysia-home-improvement-market) | 低 |
| 同上引用：住宅交易總值 | RM 1,082.7 億（2025）（需求指標，非裝修） | 2025 | 同上 | 低 |
| 6Wresearch：室內設計成長率 | 5.8%（2025） | — | [6W MY](https://www.6wresearch.com/industry-report/malaysia-interior-design-market-outlook) | 低 |
| zenweb（行銷文）：室內設計市場 | >USD 14 億（2026） | 2026 | [zenweb](https://zenweb.my/industries/interior-design/digital-marketing/) | 極低 |
| 單價：公寓全屋 RM 120–450+/ft²；設計費占預算 5–15%；辦公室 fit-out RM 25 萬–150 萬／案 | 2026 | [Houz](https://www.houz.com.my/interior-design-cost-malaysia/)；[zacharykhaw](https://zacharykhaw.com/2025/09/05/interior-design-cost-malaysia/) | 低 |
| 商用成本：吉隆坡高階 fit-out | RM 6,908/m² | 2026 | [T&T](https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026/asia-pacific) | 高 |
| DOSM 建築統計（Construction Statistics Q4 2025） | 頁面存在，本輪未取得「室內裝潢」細項數字（前稿摘要提及 DOSM 承包商口徑室內裝潢工程產值 RM 20 億（2024），但無 URL，待驗證） | 2025 | [DOSM](https://www.dosm.gov.my/portal-main/release-content/construction-statistics-fourth-quarter-2025) | 缺口 |

### 3.8 泰國（Thailand）

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| 獨立市場研究（Mr. DIY 上市文件，泰國 SEC）：居家修繕產業 | THB 3,862 億（2018）→ **THB 4,795 億（2023）**，CAGR 4.4% ≈ USD 145 億 ≈ NT$4,577 億 | 2023 | [SEC 上市文件](https://market.sec.or.th/public/ipos/IPOSGetFile.aspx?TransID=646423&TransFileSeq=87) | 中（上市文件，獨立顧問；口徑為居家修繕含建材零售） |
| Ken Research：泰國居家修繕 | ≈USD 165 億（基準年不明；以 DIY／五金零售三角驗證） | — | [Ken TH](https://www.kenresearch.com/thailand-home-improvement-market) | 低 |
| Mobility Foresights：泰國居家修繕 | USD 3,104 億（2025）——**超過泰國 GDP 一半，顯然錯誤** | 2025 | [MF](https://mobilityforesights.com/product/thailand-home-improvement-market) | 極低（排除） |
| SCB EIC／ttb analytics：2025 年住宅市場為 10 年來最艱困；2026 年持平或微增 | 2025–2026 | [Nation](https://www.nationthailand.com/business/property/40056158)；[Nation 2027](https://www.nationthailand.com/business/economy/40070934)；[SCB EIC](https://www.scbeic.com/en/detail/product/443) | 高 |
| 二手房占市場 60%、成長快於新屋（Modern Property Consultant） | 2025-10 | [Matichon](https://www.matichon.co.th/economy/news_5437496)；[REIC 轉載](https://www.reic.or.th/News/RealEstate/470359) | 中 |
| 屋齡 ≥10 年住宅逾 2,340 萬戶（翻修潛在存量） | 約 2024 | [Bangkokbiznews](https://www.bangkokbiznews.com/property/1124831) | 中 |
| REIC：2025 Q4 住宅市場因政府措施觸底回穩 | 2025 | [REIC Q4](https://www.bangkokfocusnews.com/2026/02/REIC-Q4-2568-Trends2569.html)；[REIC Q1](https://www.reic.or.th/Activities/PressRelease/260) | 高 |

- Kasikorn Research、Krungsri Research 的翻修市場估計本輪未搜得（缺口）；泰國無「室內設計服務」獨立估計。

### 3.9 越南（Vietnam）

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| IMARC：居家修繕 | **USD 15.226 億（2025）**≈ VND 39.6 兆 ≈ NT$480 億 | 2025 | [IMARC VN HI](https://www.imarcgroup.com/vietnam-home-improvement-market) | 低 |
| Expert Market Research：居家修繕 | ≈USD 31.7 億（2025） | 2025 | [EMR VN HI](https://www.expertmarketresearch.com/reports/vietnam-home-improvement-market) | 低（與 IMARC 差 2 倍） |
| IMARC：建築服務（含 interior designing services 子項） | USD 16 億（2025） | 2025 | [IMARC VN Arch](https://www.imarcgroup.com/vietnam-architectural-services-market) | 低 |
| IMARC：家飾 | USD 40 億（2025）→ 54 億（2034） | 2025 | [IMARC VN decor](https://www.imarcgroup.com/vietnam-home-decor-market) | 低 |
| Mordor：傢俱（全） | USD 97.6 億（2025）→ 148.7 億（2031）；家用傢俱 USD 4.74 億（2025），前版 4.30 億 | 2025 | [Mordor VN furn](https://www.mordorintelligence.com/industry-reports/vietnam-furniture-market)；[Mordor VN HF](https://www.mordorintelligence.com/industry-reports/vietnam-home-furniture-market) | 中（含出口製造） |
| Ken Research／Research and Markets：傢俱＋室內 | ≈USD 150 億（以傢俱業 GDP 貢獻 top-down 推算；含出口） | — | [Ken VN](https://www.kenresearch.com/vietnam-furniture-and-interior-design-market)；[R&M VN](https://www.researchandmarkets.com/reports/6207252/vietnam-furniture-interiors-market) | 低（含出口製造，不可當內需裝修） |
| 6Wresearch：室內設計 CAGR | 7.1%（2026–2032） | — | [6W VN](https://www.6wresearch.com/industry-report/vietnam-interior-design-market-outlook) | 低 |
| GSO（統計總局）建築業產值 | 本輪未取得 | — | — | 缺口 |

### 3.10 印尼（Indonesia）

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| Ken Research：傢俱＋現代室內（domestic retail-equivalent） | **USD 84.0 億（2025）**→ 128.8 億（2032），CAGR 6.3% ≈ IDR 134 兆 ≈ NT$2,646 億 | 2025 | [Ken ID](https://www.kenresearch.com/indonesia-furniture-and-modern-interiors-market) | 低（同機構另有 USD 82 億、86 億、100 億三個版本） |
| Ken Research 其他版本 | USD 82 億（[furniture & interior solutions](https://www.kenresearch.com/indonesia-furniture-and-interior-design-market)）；USD 100 億（[2025-12 新聞稿](https://www.openpr.com/news/4320567/)） | 2025 | — | 低 |
| Credence：室內設計 | USD 8.25 億（2023）→ 11.58 億（2032），CAGR 3.82% ≈ NT$260 億 | 2023 | [Credence ID](https://www.credenceresearch.com/report/indonesia-interior-design-market) | 低 |
| Credence：Interior Fit Out | 報告存在，無摘要數值 | — | [Credence ID FO](https://www.credenceresearch.com/report/indonesia-interior-fit-out-market) | 無資料 |
| 6Wresearch：室內設計 CAGR | 7.5%（2026–2032），2026-02 更新 | — | [6W ID](https://www.6wresearch.com/industry-report/indonesia-interior-design-market-outlook) | 低 |
| BPS 建築業統計 | 本輪未取得 | — | — | 缺口 |

### 3.11 菲律賓（Philippines）

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| Ken Research：傢俱＋室內（區域比較表） | **USD 26.0 億（2025）**，CAGR 6.8% ≈ PHP 1,482 億 ≈ NT$819 億 | 2025 | [Ken ID 區域表](https://www.kenresearch.com/indonesia-furniture-and-modern-interiors-market) | 低 |
| Ken Research 其他版本 | USD 25 億（[lifestyle interiors](https://www.researchandmarkets.com/reports/6207740/philippines-furniture-lifestyle-interiors-market)）；USD 41 億（[furniture & interior design](https://www.kenresearch.com/philippines-furniture-and-interior-design-market)） | — | — | 低（矛盾） |
| 6Wresearch：室內設計 CAGR | 6.4%（2025–2031），住宅為主 | — | [6W PH](https://www.6wresearch.com/industry-report/philippines-interior-design-market-outlook) | 低 |
| IMARC：傢俱 | >USD 67 億（2034） | 2034F | [openPR](https://www.openpr.com/news/4519611/) | 低 |
| HKTDC：菲律賓室內設計公司尋求國際夥伴 | 質性 | — | [HKTDC PH](https://research.hktdc.com/en/article/MTk2OTMyNDExNA) | 中 |
| PSA 建築業統計 | 本輪未取得 | — | — | 缺口 |

### 3.12 印度（India）

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| IMARC：室內設計 | **USD 368.9 億（2025）**，CAGR 8.16% 至 2034 ≈ INR 3.17 兆 ≈ NT$1.162 兆 | 2025 | [IMARC IN](https://www.imarcgroup.com/india-interior-design-market) | 低–中 |
| Mordor：室內設計 | **USD 314.3 億（2025）**；指出 USD 369 億為「含家飾家具之廣義口徑」 | 2025 | [Mordor IN](https://www.mordorintelligence.com/industry-reports/india-interior-design-market) | 低–中 |
| Verified Market Research：室內設計 | USD 364 億（2024） | 2024 | [VMR IN](https://www.verifiedmarketresearch.com/product/india-interior-design-market/) | 低 |
| Indian Retailer：家居與室內市場 | USD 295 億 | 約 2024 | [Indian Retailer](https://www.indianretailer.com/article/retail-business/home/how-indias-home-and-interior-market-skyrocketed-295-billion-top-trends) | 低 |
| IMARC：家用傢俱／家飾／家紡 | USD 170.5 億／268.8 億／74.9 億（2025）；R&M 家用傢俱 USD 252 億；TechSci 家紡 USD 69.6 億 | 2025 | [IMARC furn](https://www.imarcgroup.com/india-home-furniture-market)；[IMARC decor](https://www.imarcgroup.com/india-home-decor-market)；[IMARC furnishings](https://www.imarcgroup.com/india-home-furnishings-market)；[R&M](https://www.researchandmarkets.com/report/india-home-furniture-market)；[TechSci](https://www.techsciresearch.com/report/india-home-furnishing-market/15229.html) | 低 |
| Redseer：線上居家修繕 | ≈USD 10 億（現值）→ USD 30–32 億（FY31） | 2025 | [Redseer instant home](https://redseer.com/articles/tapping-into-the-everyday-instant-home-services-and-the-next-habit-loop/) | 中 |
| Redseer：線上室內設計 ≈USD 1 億（FY19）、滲透 <1%；傢俱 86% 非組織化（2018）、組織化可達 20%（2022E）；傢俱產業 USD 400 億（2026E） | FY19／2018 | [Redseer online ID](https://redseer.com/articles/online-interior-design-market-updates/)；[Redseer 2018 PDF](https://redseer.com/wp-content/uploads/2018/09/Disruption-in-Indian-furniture-retailing-_-31-August-2018-v1.pdf)；[medianews4u](https://www.medianews4u.com/indias-furniture-industry-to-touch-40-billion-by-2026-redseer-report/) | 中（但年份舊） |
| Livspace 營收 ₹1,148 crore（FY23，≈USD 1.2 億）、淨損 ₹793 crore；FY25 成長 23% | FY23／FY25 | [Wikipedia Livspace](https://en.wikipedia.org/wiki/Livspace)；[Mordor IN](https://www.mordorintelligence.com/industry-reports/india-interior-design-market) | 中 |
| HomeLane 營收 ₹756 crore（FY25，+22%），併購 DesignCafe | FY25 | [franchisebazar](https://www.franchisebazar.com/blog/homelane-franchise-2026-indias-fastest-growing-home-interiors-opportunity) | 低 |
| 商用成本：印度主要城市 fit-out USD 65–73/ft²（亞太最低） | 2026 | [ConstructionWorld](https://www.constructionworld.in/latest-construction-news/real-estate-news/india-leads-asia-pacific-in-fit-out-cost-efficiency/88743) | 高 |

- 印度 Livspace／HomeLane 市占說法互相矛盾（80%／65–70%／28%／5–7%），皆無方法揭露，不建議引用。
- 以 Livspace＋HomeLane 合計營收約 ₹2,000 crore（≈USD 2.3 億）對照 Mordor USD 314 億市場，組織化平台滲透率 <1%，與 Redseer 的「線上 <1%」一致。

---

## 4. 關鍵問題三：定義矩陣（Definitions matrix）

### 4.1 口徑分類（bucket）定義

| 代號 | 口徑 | 內容 | 典型來源 |
|---|---|---|---|
| **D** | 室內設計服務費（design fees only） | 設計、繪圖、監造等專業服務收入，不含施工與材料 | Grand View／Mordor「interior design (services)」、智研「建築室內設計」、HKTDC 設計產業增加值 |
| **DB** | 設計＋施工（design & build / fit-out contracting） | 承包商口徑：設計＋工程＋材料；含住宅與商用 | Frost & Sullivan fitting-out（新加坡）、HK C&SD 非地盤工程、CBDA 建築裝飾產值、台灣「裝修年產值」 |
| **RR** | 住宅翻修支出（residential renovation / remodeling） | 既有住宅之增改建、設備更新、維護（屋主支出口徑） | 矢野リフォーム、CERIK 리모델링、艾瑞家裝、Ken/GVR/FBI remodeling |
| **HI** | 居家修繕零售（home improvement retail / DIY） | 消費者自購建材、五金、油漆、工具（零售通路口徑） | Mordor／R&M DIY、Statista、GlobalData、泰國 Mr. DIY 文件 |
| **FU** | 傢俱家飾（furniture & home décor） | 傢俱、家飾、家紡；常與「interiors」混稱 | Ken Research 各國 furniture & interiors、IMARC home decor、Mordor furniture |
| **CF** | 商用裝修（commercial fit-out） | 辦公、零售、酒店等非住宅室內工程 | Credence fit-out、DataM、Dataintelo commercial ID；JLL／C&W／KF／T&T 成本指南 |
| **DF** | 開發商交屋裝修（developer fit-out） | 新成屋精裝修／交屋標配（中國「全裝修」、台灣預售屋標配） | 中國家裝「新房裝修」子項、CBDA 住宅裝飾（本輪無獨立數字） |

### 4.2 各來源歸類

| 來源／市場名稱 | 範圍 | 含設計費 | 含施工 | 含材料 | 含傢俱家飾 | 含商用 | 含新建 | 歸類 |
|---|---|---|---|---|---|---|---|---|
| 矢野 住宅リフォーム市場（JP） | 住宅 | 是（併入工程） | 是 | 是 | 是（家具・インテリア） | 否 | 否（但含增改建） | **RR（廣）** |
| CERIK 리모델링（개수＋유지보수）（KR） | 建築物（含非住宅） | 是 | 是 | 是 | 否 | 是 | 否 | **RR＋CF** |
| 신영증권 인테리어 리모델링（KR） | 住宅為主 | 是 | 是 | 是 | 部分 | 部分 | 否 | **RR** |
| CBDA／智研 建築裝飾總產值（CN） | 全部 | 是 | 是 | 是 | 否 | 是（公裝 2.2 萬億） | 是（新建精裝） | **DB＋CF＋DF** |
| 艾瑞 家裝市場（CN） | 住宅 | 是 | 是 | 是 | 部分（主材） | 否 | 是（新房裝修） | **RR＋DF** |
| 智研 建築室內設計（CN） | 全部 | 是 | 否 | 否 | 否 | 是 | 是 | **D** |
| HK C&SD 非地盤建造工程 | 全部 | 併入 | 是 | 是 | 否 | 是 | 是（小型新建） | **DB＋CF（含雜項）** |
| F&S Singapore interior fitting-out | 全部 | 否（施工口徑） | 是 | 是 | 否 | 是 | 是 | **DB＋CF** |
| 100 室內設計「裝修年產值 5,500 億」（TW） | 不明 | 不明 | 是 | 是 | 不明 | 不明 | 不明 | **DB（口徑未公開）** |
| ABRI 住宅裝修市場（TW） | 住宅 | 是 | 是 | 是（另列材料 153 億） | 否 | 否 | 否 | **RR** |
| Grand View Interior Design（APAC／JP／CN） | 全部 | 是 | 不明（含 new construction／remodeling 類型） | 否 | 否 | 是 | 是 | **D（或 D＋部分 DB）** |
| Cognitive／Renub／Spherical Interior Design | 全部 | 是 | 不明 | 否 | 否 | 是 | 是 | **D** |
| IMARC／Mordor India Interior Design | 全部 | 是 | 部分 | 部分 | **是**（Mordor 自述） | 是（Mordor 稱商用 74%） | 是 | **D＋FU（混合）** |
| Ken Research Furniture & Interior Design（各國） | 全部 | 是（小部分） | 否 | 否 | **是（主體）** | 是（辦公傢俱） | 否 | **FU** |
| Ken Research APAC Residential Remodeling | 住宅 | 是 | 是 | 是 | 否 | 否 | 否 | **RR（結構性）** |
| Fortune BI Home Renovation | 住宅 | 是 | 是 | 是 | 部分 | 否 | 否 | **RR（廣）** |
| IMARC Home Improvement Services | 住宅 | 是 | 是 | 否 | 否 | 否 | 否 | **RR（服務）** |
| Mordor／R&M／VMR APAC DIY | 住宅 | 否 | 否 | 是 | 部分 | 否 | 否 | **HI** |
| Statista／GlobalData／Euromonitor home improvement | 住宅 | 否 | 否 | 是 | 是（家飾店） | 否 | 否 | **HI** |
| Mr. DIY 文件 Thailand home improvement industry | 住宅 | 否 | 部分 | 是 | 部分 | 否 | 否 | **HI** |
| IMARC Vietnam Home Improvement／EMR | 住宅 | 不明 | 部分 | 是 | 否 | 否 | 否 | **HI／RR** |
| Credence Interior Design（ID／CN／KR luxury） | 全部 | 是 | 不明 | 否 | 否 | 是 | 是 | **D** |
| DataM／Coherent／Credence Interior Fit Out | 非住宅為主 | 併入 | 是 | 是 | 部分 | 是 | 是 | **CF** |
| JLL／C&W／KF／T&T 成本指南 | 辦公 | 併入 | 是 | 是 | 是（傢俱） | 是 | 是 | **CF（單位成本）** |

### 4.3 歸類後的關鍵觀察

- 12 市場中僅日本（RR）、南韓（RR＋CF）、中國（RR＋DF／DB＋CF）、香港（DB＋CF）有**官方或半官方的 RR／DB 口徑**；新加坡（F&S）與泰國（Mr. DIY 文件）有上市文件級別的 DB／HI 口徑；台灣、馬、越、印尼、菲、印度**全部只有研究機構數字**。
- 研究機構的「interior design」在東北亞（JP／CN）約等於 D 口徑（占 RR 的 5–13%），但在印度明顯混入 FU（占 GDP 0.9%，與日本 D 口徑 0.15% 相差 6 倍），**不可跨國直接比較**。
- Ken Research 的「furniture & interior design」實為 FU 口徑，是東南亞四國唯一的「2025 年值」來源，引用時須改稱「傢俱與室內用品市場」。

---

## 5. 關鍵問題四：校準後的可比區間與正規化

### 5.1 正規化基礎（IMF WEO 2026 年 4 月，經 Worldometers／StatisticsTimes 轉載）

| 市場 | 人均 GDP 2025（USD，名目） | 人均 GDP 2026F | 人口（百萬，**未經本輪 URL 驗證之概略值，列入缺口**） | 推算名目 GDP 2025（USD 十億） |
|---|---|---|---|---|
| 新加坡 | 99,365 | 107,758 | 6.0 | 600 |
| 香港 | 56,893 | 59,640 | 7.5 | 428 |
| 台灣 | 39,489 | 42,103 | 23.4 | 924 |
| 南韓 | 36,227 | 37,412 | 51.7 | 1,873 |
| 日本 | 35,973 | 35,703 | 123.4 | 4,439 |
| 中國 | 13,968 | 14,874 | 1,408 | 19,667 |
| 馬來西亞 | 13,949 | 15,085 | 34.1 | 476 |
| 泰國 | 8,057 | 8,105 | 71.6 | 577 |
| 印尼 | 5,082 | 5,362 | 284 | 1,443 |
| 越南 | 4,829 | 5,115 | 101.3 | 489 |
| 菲律賓 | 4,270 | 4,443 | 114.1 | 487 |
| 印度 | 2,675 | 2,813 | 1,460 | 3,906 |

來源：[Worldometers GDP per capita Asia 2025](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal)；[Worldometers 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[StatisticsTimes](https://statisticstimes.com/economy/asian-countries-by-gdp-per-capita.php)；IMF 原始：[WEO April 2026 Statistical Appendix](https://www.imf.org/-/media/files/publications/weo/2026/april/english/statsappendix.pdf)（本輪無法開啟，數字為轉載，信心：中）。Worldometers 不同頁面 2025 值略有差異（如新加坡 99,365 vs 98,814），整合階段須以 IMF WEO 資料庫覆寫；人口為研究者依 IMF／UN 2025 概略值填入，**非本輪搜尋取得**。

### 5.2 (a) 住宅翻修支出（RR 口徑）可比區間

| 市場 | 可比區間（當地幣） | USD 十億 | NT$ 億 | 人均（USD） | 占 GDP | 錨點與口徑說明 | 信心 |
|---|---|---|---|---|---|---|---|
| 日本 | ¥7.35–7.51 兆（2024–2025） | 49.0–50.1 | 15,435–15,775 | 397–406 | 1.10–1.13% | 矢野 RR（廣，含家具） | 高 |
| 南韓 | ₩32.4–37 兆（2025，預測值） | 23.1–26.4 | 7,290–8,325 | 447–511 | 1.23–1.41% | 신영（RR）～CERIK（RR＋CF，含維護） | 中 |
| 中國 | ¥2.76–3.78 萬億（2024–2025） | 383–525 | 12,075–16,538 | 272–373 | 1.95–2.67% | 報告大廳（低信心）～艾瑞（RR＋DF） | 中 |
| 台灣 | NT$2,000–5,500 億 | 6.3–17.5 | 2,000–5,500 | 271–746 | 0.69–1.89% | ABRI 住宅（舊）～100 室內設計全口徑推估 | 低 |
| 香港 | HK$850–873 億（2024–2025） | 10.9–11.2 | 3,434–3,526 | 1,453–1,493 | 2.5–2.6% | C&SD 非地盤（DB＋CF，**含小型新建與機電保養，高估**） | 中 |
| 新加坡 | SGD 48.8 億（2022E） | 3.67 | 1,155 | 608 | 0.61% | F&S fitting-out（DB＋CF） | 中（年份舊） |
| 馬來西亞 | USD 10–24.3 億（2025） | 1.0–2.43 | 315–765 | 29–71 | 0.21–0.51% | Ken HI～Ken FU | 低 |
| 泰國 | THB 4,795 億（2023） | 14.5 | 4,577 | 203 | 2.5% | Mr. DIY 文件 HI（含建材零售，**高估 RR**） | 中 |
| 越南 | USD 15.2–31.7 億（2025） | 1.52–3.17 | 480–998 | 15–31 | 0.31–0.65% | IMARC～EMR HI／RR | 低 |
| 印尼 | USD 8.4 十億（2025） | 8.4 | 2,646 | 30 | 0.58% | Ken FU（**非 RR**） | 低 |
| 菲律賓 | USD 2.6 十億（2025） | 2.6 | 819 | 23 | 0.53% | Ken FU（**非 RR**） | 低 |
| 印度 | USD 31.4–36.9 十億（2025） | 31.4–36.9 | 9,891–11,624 | 22–25 | 0.80–0.94% | Mordor～IMARC（D＋FU 混合，**非純 RR**） | 低 |

註：人均與占 GDP 均為本研究以 §5.1 數字推算。

### 5.3 (b) 室內設計服務（D 口徑）可比區間

| 市場 | 可比區間 | USD 十億 | NT$ 億 | 人均（USD） | 占 GDP | D／RR 比 | 錨點 | 信心 |
|---|---|---|---|---|---|---|---|---|
| 日本 | USD 61.5–64.9 億（2024–2025） | 6.15–6.49 | 1,937–2,045 | 50–53 | 0.14–0.15% | 12–13% | Cognitive／GVR／Renub／Spherical | 中 |
| 南韓 | USD 39.9 億（2025） | 3.99 | 1,257 | 77 | 0.21% | 15–17% | Cognitive | 低 |
| 中國 | ¥1,744 億（2024）～USD 269.5 億（2025） | 24.2–26.95 | 7,623–8,489 | 17–19 | 0.12–0.14% | 4.6–5.1% | 智研／GVR | 中 |
| 台灣 | 無直接估計；若以 D／RR 比 10–15% 套用 2,000–5,500 億 → NT$200–825 億 | 0.6–2.6 | 200–825 | 27–112 | 0.07–0.28% | 假設 | **本研究推算** | 極低 |
| 香港 | 無；設計產業（全）增加值 HK$41 億（2022） | 0.53 | 166 | 70 | 0.12% | — | HKTDC | 低（口徑不符） |
| 新加坡 | USD 7.7 億（2024） | 0.77 | 243 | 127 | 0.13% | 21%（對 F&S fit-out） | DMI/GrowthHQ | 低 |
| 馬來西亞 | 無（含於 Ken FU） | — | — | — | — | — | — | 無資料 |
| 泰國 | 無 | — | — | — | — | — | — | 無資料 |
| 越南 | ≤USD 16 億（IMARC 建築服務含設計子項） | <1.6 | <504 | <16 | <0.33% | — | IMARC | 低 |
| 印尼 | USD 8.25 億（2023） | 0.82 | 260 | 2.9 | 0.06% | 10%（對 Ken FU） | Credence | 低 |
| 菲律賓 | 無 | — | — | — | — | — | — | 無資料 |
| 印度 | USD 314–369 億（含傢俱家飾）；若純設計費依日本 D／RR 比 12% 推估 → USD 38–44 億 | 3.8–4.4（推算） | 1,197–1,386 | 2.6–3.0 | 0.10–0.11% | 假設 | IMARC／Mordor 修正 | 極低 |

- 跨國一致性檢查：D 口徑占 GDP 在日、中、星、港集中於 **0.12–0.15%**，南韓 0.21% 略高；此可作為「設計服務費」的基準比率，用以檢驗任何偏離（例如印度 0.9%）為口徑混淆。

### 5.4 (c) 商用裝修（CF 口徑）：無可信總量，以單位成本呈現

| 市場（城市） | 辦公室 fit-out 單位成本 2026 | 來源 | 信心 |
|---|---|---|---|
| 亞太平均 | USD 1,550/m²（當地幣年增 2–5%） | [JLL via cfotech](https://cfotech.asia/story/jll-warns-asia-pacific-office-fit-out-costs-keep-rising) | 高 |
| 新加坡 | USD 2,029/m²（KF）；USD 140/ft²（C&W） | [irei](https://irei.com/publications/article/asia-pacific-office-fit-out-costs/)；[C&W](https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office) | 高 |
| 東京 | USD 1,994/m²（KF）；USD 215/ft²（C&W）；¥729,406/m² 高階（T&T） | 同上；[T&T](https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026/asia-pacific) | 高 |
| 台北 | USD 1,593/m²（KF） | [irei](https://irei.com/publications/article/asia-pacific-office-fit-out-costs/) | 高 |
| 吉隆坡 | RM 6,908/m² 高階（T&T） | [T&T](https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026/asia-pacific) | 高 |
| 印度主要城市 | USD 65–73/ft²（亞太最低） | [ConstructionWorld](https://www.constructionworld.in/latest-construction-news/real-estate-news/india-leads-asia-pacific-in-fit-out-cost-efficiency/88743) | 高 |
| 香港 | HKD 400–1,200/ft²（承包商） | [rokydesign](https://rokydesign.com/integrated-design-build-office-fit-out-hong-kong/) | 低 |
| 金邊（區域最低參考） | USD 375/m²（KF） | [irei](https://irei.com/publications/article/asia-pacific-office-fit-out-costs/) | 高 |

- 總量級參考（低信心）：DataM 亞太 fit-out ≈USD 181 億（2024）；Dataintelo 亞太商用室內設計 USD 117 億（2025）；中國公共建築裝飾 2.2 萬億人民幣（≈USD 3,056 億，2023，智研／搜狐轉載）——後者一國即遠超前兩者，再次顯示研究機構 CF 總量不可用。
- 建議整合階段以「單位成本 × 年度辦公／零售竣工面積（各地官方建築統計）」自建 CF 區間；香港可直接用 C&SD 非地盤數列扣除住宅比例。

---

## 6. 關鍵問題五：成長率與驅動因子比較

### 6.1 各市場 CAGR 區間與驅動因子

| 市場 | 官方／本地錨點成長 | 研究機構 CAGR 區間 | 各來源引述之驅動因子 | 住房市場對照與合理性 |
|---|---|---|---|---|
| 日本 | 矢野：2025 +2.5%、2026F +1.9%；2024 −0.5% | 3.95%（Renub）～6.08%（Spherical）；GVR 5.7% | 工事單價上升（資材・人件費）、斷熱補助、既存住宅活用；新建減少 | 研究機構 5–6% **高於**矢野近年 −0.5～+2.5% 之實績，屬高估；日本為負成長人口、新設住宅下滑，翻修以單價驅動為主 |
| 南韓 | CERIK：리모델링 5.4%／維護 1.4%（2020–2030）；신영：32.4→46 조（2025–2030，≈7.3%） | 4.35%（Credence 豪宅）～6.34%（Cognitive） | 老舊公寓（30 年以上）存量、重建管制下之리모델링替代、1 人家戶 | 2020 年預測未反映 2022–2024 高利率房市修正；5.4% 偏樂觀，建議採 3–5% |
| 中國 | 艾瑞：2022 +7.8%，2025F 3.78 萬億（隱含 ~8%）；智研室內設計 2021→2024 **−11%/年**；中裝協十四五目標 6.5 萬億（2025） | GVR 6.5%（2026–2033）；GMI 5.4% | 存量房翻新、舊改、適老化；但房地產投資 −10.6%（2024） | 艾瑞 2023 年預測顯然**未反映房市下行**；智研室內設計規模三年縮 30% 才是實況；GVR 6.5% 不可信，建議 0–3% |
| 台灣 | 100 室內設計：2025 「不減反增」至 5,500 億；2026 有望續增 | 無獨立 CAGR | 預售屋交屋潮（2024–2026）、寵物經濟、老屋翻新、商業空間 | 2024 年推案 6,000 億（十大建商）支撐交屋裝修；但 2025 年起房市限貸、交易量下滑，2026–2027 交屋後裝修需求可能轉弱 |
| 香港 | C&SD 非地盤：2024 −6.0%、2025 各季 −0.7～−3.9% | 無獨立 CAGR（併入中國） | 寫字樓空置高、零售弱；住宅翻修受樓價下行壓抑 | 官方數列**負成長**，任何正 CAGR 預測皆與實況不符 |
| 新加坡 | F&S（2020 預測）fit-out 至 2022 成長 | 6Wresearch 5.9%（2025–2031） | HDB 轉售量、BTO 交屋、辦公室升級 | 無官方數列可驗證；5.9% 與新加坡名目 GDP 成長（~4–5%）相當，尚屬合理 |
| 馬來西亞 | 無 | 6Wresearch 5.8%（2025）；Ken FU 2025–2032 未明 | 住宅交易 RM 1,083 億（2025）、柔佛—新加坡特區 | 合理區間 4–6% |
| 泰國 | Mr. DIY 文件：HI 2018–2023 CAGR 4.4% | Ken 未明 | 二手房占 60%、屋齡 ≥10 年 2,340 萬戶、新屋滯銷轉翻修 | SCB EIC：2025 房市 10 年最差、2026 持平；HI 4.4% 歷史值可接受，2025–2026 應下修至 0–3% |
| 越南 | 無 | 6Wresearch 7.1%（2026–2032）；Mordor 傢俱 2025–2031 ~7.3% | 都市化、公寓交付、中產擴張 | 越南名目 GDP 成長 ~8–10%，7% 合理 |
| 印尼 | 無 | Ken 6.3%（2025–2032）；6Wresearch 7.5%（2026–2032）；Credence 3.82% | 都市化、中產、IKN 新首都 | 三家差距 2 倍；6–7% 與名目 GDP 相當 |
| 菲律賓 | 無 | Ken 6.8%；6Wresearch 6.4%（2025–2031） | 住宅為主、OFW 匯款、公寓交付 | 合理 |
| 印度 | Livspace FY25 +23%、HomeLane FY25 +22%（公司層級） | IMARC 8.16%（2026–2034）；Mordor DIY 印度 10.95% | 住房需求、組織化平台、都市化 | 公司 20%+ 為低基期；市場 8% 與名目 GDP（~10%）相符，但基準值口徑含傢俱 |
| 亞太整體 | — | 室內設計 5.5–6.6%；住宅翻修 4.5–5.4%；DIY 5.4%；fit-out 8.3% | — | 研究機構亞太 CAGR 一律 4.5–8%，**與日本（+2%）、中國（負）、香港（負）之實況脫節**，實為把東南亞／印度高成長平均化 |

### 6.2 明顯不合理之預測（應排除或加註）

1. **Mobility Foresights 泰國居家修繕 USD 3,104 億（2025）**：超過泰國 GDP 的 50%，排除（[MF](https://mobilityforesights.com/product/thailand-home-improvement-market)）。
2. **Grand View 中國占全球 52.1% 同頁又稱 14.5%**：僅採 14.5%（與 USD 269.5／1,857 億相符）（[GVR China](https://www.grandviewresearch.com/horizon/outlook/interior-design-market/china)）。
3. **艾瑞 2025F 家裝 3.78 萬億**：2023 年預測，未反映 2024 房地產投資 −10.6%；引用時須標「2023 年預測」。
4. **CERIK 2025 37 조**：2020 年預測，引用須標「預測值」；本輪無 2025 實績。
5. **Ken Research 越南／印尼「furniture & interiors」USD 150／100 億**：以傢俱業 GDP 貢獻推算，含出口製造，不可當內需裝修。
6. **研究機構日本 5–6% CAGR**：與矢野 −0.5～+2.5% 實績矛盾。
7. **IMARC／Mordor 印度 USD 314–369 億**：占 GDP 0.9%，是日本 D 口徑 6 倍，必含傢俱家飾。

---

## 7. 關鍵問題六：方法論警示與建議引用政策

### 7.1 研究機構數字的已知問題（本輪實證）

| 問題類型 | 實例 | 證據 URL |
|---|---|---|
| **回收（recycling）**：不同機構同一數字 | Grand View 與 Mordor 全球室內設計 2024 年值皆 USD 1,379.3 億 | [GVR](https://www.grandviewresearch.com/industry-analysis/interior-design-market-report)；[Mordor via DRI](https://dri.co.jp/auto/report/mordor/240217-interior-design-services-market-share.html) |
| **自我矛盾**：同機構同市場多值 | Ken Research 印尼 USD 82／84／86／100 億（2025）；菲律賓 25／26／41 億；南韓 165.5 vs 172 億（2031）；Mordor 越南家用傢俱 4.30 vs 4.74 億（兩版） | §3.9–3.11 各 URL |
| **同名異量**：同名市場差 14 倍 | 「Asia-Pacific DIY Home Improvement」：Mordor USD 64 億 vs R&M USD 923 億（2025） | [Mordor](https://www.mordorintelligence.com/industry-reports/asia-pacific-diy-home-improvement-market)；[R&M](https://www.researchandmarkets.com/report/asia-pacific-diy-home-improvement-market) |
| **套版錯誤** | Deep Market Insights 室內設計服務報告把「litigation」列為最大服務類別（前稿）；Grand View 中國 52.1%／14.5% 並存 | [GVR China](https://www.grandviewresearch.com/horizon/outlook/interior-design-market/china) |
| **外推（extrapolation）未更新** | 艾瑞 2023 預測 2025；CERIK 2020 預測 2025；F&S 2020 預測 2022；ABRI 以 84–91 年普查推估 | §3 |
| **未定義口徑** | 台灣「5,500 億」計算方式未公開；Transpire、Cognitive 未說明是否含施工 | [udn](https://udn.com/news/story/7241/9245511) |
| **摘要／付費牆** | Statista 1474530、6Wresearch 各國 2025 值皆隱藏，只露 CAGR | [Statista](https://www.statista.com/statistics/1474530/apac-home-improvement-market-size-in-selected-countries) |
| **量級荒謬** | Mobility Foresights 泰國 USD 3,104 億 | 見 §6.2 |
| **新聞稿多重轉載被誤判為多源** | 台灣 5,500 億：聯合報×2、PChome、Yahoo、安傳媒皆同一新聞稿 | §3.4 |
| **軟體報告冒充市場報告** | 搜尋「Asia Pacific interior design market」首頁多為 Mordor／EMR 設計軟體報告 | [Mordor SW](https://www.mordorintelligence.com/industry-reports/apac-interior-design-software-market) |

### 7.2 建議引用政策（最終報告）

1. **分層標示**：每個市場數字必附口徑代號（D／DB／RR／HI／FU／CF／DF，§4.1）與年份；表格標題寫明「口徑」，禁止把不同口徑並列為同一欄。
2. **來源等級**：A 級＝官方統計（C&SD、NBS、DOS、財政部）；B 級＝產業研究院／協會／上市文件（矢野、CERIK、CBDA、艾瑞、F&S 招股書、Mr. DIY 文件）；C 級＝國際研究機構（GVR、Mordor、IMARC、Ken、6W）；D 級＝未具名轉載、行銷文。**C 級以下只能作為區間端點，不得單獨成為標題數字**；D 級不引用。
3. **研究機構數字一律標註「（研究機構估計，口徑：…）」**，並在同一句內給出 A／B 級錨點作對照；禁止寫成「市場規模為 USD X 億」的斷言句。
4. **預測值標「F」與發布年**：如「37 조원（2025F，CERIK 2020 發布）」。
5. **多重轉載只計一源**：同一新聞稿之媒體轉載視為單一來源；三角驗證需三家不同方法之機構。
6. **合理性檢核**：任何 RR 口徑 >GDP 3%、D 口徑 >GDP 0.3%、或 CAGR 與官方近三年實績差 >3 個百分點者，加註「疑口徑混淆／高估」。
7. **匯率**：以單一日期之央行／IMF 匯率統一換算，表格附匯率表；禁止混用研究機構自行換算的 USD 值與本地幣值。
8. **台灣數字特別規則**：「5,500 億」只能以「民營平台推估（口徑未公開）」引用，並與 ABRI 住宅 2,000 億級、財政部室內裝潢業銷售額（待補）並列。

---

## 8. 12 市場橫向比較表

（口徑代號見 §4.1；USD 換算見檔頭匯率；「無資料」＝本輪未找到）

| 市場 | 權威本地來源（A／B 級） | 住宅翻修 RR 錨點（USD 十億，年） | 室內設計 D 錨點（USD 十億，年） | 商用 CF（辦公 fit-out 單位成本 2026） | 研究機構主要數字（口徑） | RR 占 GDP | D 占 GDP | CAGR（官方 vs 機構） | 資料品質 |
|---|---|---|---|---|---|---|---|---|---|
| 日本 | 矢野経済研究所 住宅リフォーム市場 | 50.1（2025，¥7.51 兆） | 6.15–6.49（2024–25） | 東京 USD 1,994/m²（KF） | GVR 6.49（D）；Cognitive 6.15（D） | 1.13% | 0.14% | +2.5% vs 4–6% | 高 |
| 南韓 | 건설산업연구원（CERIK）；신영증권 | 23.1–26.4（2025F，₩32.4–37 조） | 3.99（2025） | 無資料 | Cognitive 3.99（D）；Ken 12.6（FU） | 1.2–1.4% | 0.21% | 5.4%（2020 預測）vs 4.4–6.3% | 中 |
| 中國 | 中裝協／智研；國家統計局；艾瑞 | 383–525（2024–25，¥2.76–3.78 萬億 家裝）；建築裝飾總產值 803（2023） | 24.2–26.95（2024–25） | 無資料（Credence CN fit-out 7.3，2023） | GVR 26.95（D）；GMI 100（RR）；Mordor 傢俱 65.8（FU） | 2.0–2.7% | 0.12–0.14% | 智研 D −11%/年（2021–24）vs GVR +6.5% | 中 |
| 台灣 | 內政部建研所（舊）；財政部（待補）；100 室內設計（民營推估） | 6.3–17.5（NT$2,000–5,500 億） | 無資料（推算 0.6–2.6） | 台北 USD 1,593/m²（KF） | 無國際機構獨立報告 | 0.7–1.9% | 無資料 | 「不減反增」vs 無 | 低 |
| 香港 | 政府統計處 C&SD（非地盤建造工程）；發展局 | 10.9–11.2（2024–25，HK$850–873 億；DB＋CF 含小型新建） | 無資料（設計產業全口徑 0.53，2022） | HKD 400–1,200/ft²（承包商） | 併入中國報告 | 2.5–2.6%（高估） | 0.12%（口徑不符） | −6.0%（2024）、−0.7～−3.9%（2025 各季） | 高（但口徑過寬） |
| 新加坡 | DOS（無細項）；Frost & Sullivan（招股書） | 3.67（2022E，SGD 48.8 億 fit-out，含商用） | 0.77（2024） | 新加坡 USD 2,029/m²（KF，亞太最高） | DMI 0.77（D）；Ken 1.13（FU）；6W CAGR 5.9% | 0.61% | 0.13% | 無 vs 5.9% | 中低 |
| 馬來西亞 | DOSM（細項待補） | 1.0–2.43（2025；Ken HI／FU） | 無資料 | 吉隆坡 RM 6,908/m²（T&T 高階） | Ken 2.43（FU）、1.0（HI）；6W 5.8% | 0.2–0.5% | 無資料 | 無 vs 5.8% | 低 |
| 泰國 | Mr. DIY 上市文件（SEC）；SCB EIC／REIC（房市） | 14.5（2023，THB 4,795 億 HI 含建材零售） | 無資料 | 無資料 | Ken 16.5（HI）；MF 310（排除） | 2.5%（HI 口徑高估） | 無資料 | HI 4.4%（2018–23）；2025 房市 10 年最差 | 中低 |
| 越南 | GSO（未取得） | 1.52–3.17（2025，IMARC／EMR HI） | <1.6（IMARC 建築服務含設計） | 無資料 | Mordor 傢俱 9.76（FU 含出口）；Ken 15（FU 含出口） | 0.3–0.65% | <0.33% | 無 vs 7.1% | 低 |
| 印尼 | BPS（未取得） | 8.4（2025，Ken FU，非 RR） | 0.82（2023） | 無資料 | Ken 8.2–10（FU）；Credence 0.82（D）；6W 7.5% | 0.58%（FU） | 0.06% | 無 vs 3.8–7.5% | 低 |
| 菲律賓 | PSA（未取得） | 2.6（2025，Ken FU，非 RR） | 無資料 | 無資料 | Ken 2.5–4.1（FU）；6W 6.4% | 0.53%（FU） | 無資料 | 無 vs 6.4–6.8% | 低 |
| 印度 | Redseer（線上／傢俱）；Livspace／HomeLane 財報 | 31.4–36.9（2025，Mordor／IMARC；D＋FU 混合） | 推算 3.8–4.4（以 D／RR 12%） | 印度 USD 65–73/ft²（C&W，亞太最低） | IMARC 36.9、Mordor 31.4（D＋FU）；Redseer 線上 HI 1.0 | 0.8–0.9%（混合） | ~0.1%（推算） | 公司 +22–23% vs 8.16% | 低 |
| 亞太整體 | 無官方 | 160（Ken）～605（FBI）（2025）；官方錨點加總 ≈640 | 30.5–31.9（GVR 2024／Cognitive 2025） | 區域平均 USD 1,550/m²（JLL） | DIY 6.4（Mordor）～92.3（R&M） | — | — | 4.5–6.6% | 低 |

---

## 9. 關鍵數字總表

| 指標 | 數值 | 年份 | 來源 | 定義／備註 | 信心 |
|---|---|---|---|---|---|
| 日本 住宅リフォーム市場 | ¥7 兆 5,119 億（+2.5%）≈ USD 500.8 億 ≈ NT$1.578 兆 | 2025 | [矢野／dreamnews](https://www.dreamnews.jp/press/0000356164) | RR（廣，含增改建、設備、家具） | 高 |
| 日本 住宅リフォーム市場 2026 預測 | ¥7.7 兆（+1.9%）≈ USD 513 億 | 2026F | [矢野 2026 年版](https://www.yano.co.jp/market_reports/C68101800) | 同上 | 高 |
| 日本 住宅リフォーム市場 | ¥7 兆 3,470 億（−0.5%） | 2024 | [矢野新聞稿 3877](https://www.yano.co.jp/press-release/show/press_id/3877) | 同上 | 高 |
| 日本 室內設計市場（GVR） | USD 64.9 億（2024）→ 89.7 億（2030），CAGR 5.7% | 2024 | [GVR Japan](https://www.grandviewresearch.com/horizon/outlook/interior-design-market/japan) | D | 中 |
| 南韓 리모델링 시장（개수＋유지보수） | ₩37 조 ≈ USD 264 億 ≈ NT$8,325 億 | 2025F（2020 發布） | [CERIK](https://www.cerik.re.kr/board/press/589) | RR＋CF；2030 44 조 | 中 |
| 南韓 건축물 리모델링 | ₩23 조 3,210 억，CAGR 5.4% | 2025F | [국토일보](https://www.ikld.kr/news/articleView.html?idxno=223589) | RR（改修） | 中 |
| 南韓 인테리어 리모델링（신영증권） | ₩32.4 조 ≈ USD 231 億 → 46 조（2030） | 2025F | [대한전문건설신문](https://www.koscaj.com/news/articleView.html?idxno=111927) | RR | 低–中 |
| 南韓 室內設計（Cognitive） | USD 39.9 億 → 65.2 億（2033），6.34% | 2025 | [CMR](https://www.cognitivemarketresearch.com/interior-design-market-report) | D | 低 |
| 中國 建築裝飾完成工程總產值 | ¥5.78 萬億 ≈ USD 8,028 億 ≈ NT$25.3 兆 | 2023 | [中裝新網／智研](http://www.cbda.cn/html/yj/20250630/142674.html) | DB＋CF＋DF | 中 |
| 中國 中裝協十四五目標 | ¥6.5 萬億 | 2025 目標 | 同上 | 規劃 | 高 |
| 中國 家裝市場（艾瑞） | >¥3 萬億（2022，+7.8%）；3 兆 7,802 億（2025F）≈ USD 5,250 億 | 2022／2025F | [艾瑞 PDF](https://zhongzhihui.oss-cn-beijing.aliyuncs.com/industryPdf/%E8%89%BE%E7%91%9E%E5%92%A8%E8%AF%A2%EF%BC%9A2023%E5%B9%B4%E4%B8%AD%E5%9B%BD%E5%AE%B6%E8%A3%85%E8%A1%8C%E4%B8%9A%E7%A0%94%E7%A9%B6%E6%8A%A5%E5%91%8A.pdf) | RR＋DF；2023 預測 | 中 |
| 中國 建築室內設計行業規模（智研） | ¥1,743.9 億（住宅 660.6、公建 1,083.3）≈ USD 242 億；2021 為 2,511.2 億 | 2024 | [智研](https://www.chyxx.com/industry/1221629.html) | D | 中 |
| 中國 室內設計（GVR） | USD 269.5 億 → 443 億（2033），6.5%；占全球 14.5% | 2025 | [GVR China](https://www.grandviewresearch.com/horizon/outlook/interior-design-market/china) | D | 中 |
| 中國 房地產開發投資 | ¥100,280 億（−10.6%）；建築業增加值 ¥89,949 億（+3.8%） | 2024 | [NBS via 中裝新網](http://www.cbda.cn/html/yj/20250312/141927.html) | 總體對照 | 高 |
| 台灣 裝修年產值（民營推估） | NT$5,500 億 ≈ USD 174.6 億 | 2025 | [聯合報](https://udn.com/news/story/7241/9245511) | DB（口徑未公開） | 低 |
| 台灣 住宅裝修市場（ABRI） | 約 NT$776 億／年（三業）；材料 153 億；「近 2,000 億」 | 84–91 年資料 | [ABRI](https://www.abri.gov.tw/News_Content_Table.aspx?n=807&s=38057) | RR | 中（舊） |
| 台灣 裝修產業年產值（經濟部 IDA 電子報） | NT$1,100 億 | 十餘年前 | [IDA](https://www.ida.gov.tw/ctlr?PRO=epaper.rwdEpaperView&id=2479) | DB | 低 |
| 香港 主要承建商建造工程總值 | HK$2,866 億（−1.4%）≈ USD 367 億 | 2025 | [新聞公報](https://www.info.gov.hk/gia/general/202603/12/P2026031200295.htm) | 全建造 | 高 |
| 香港 非地盤建造工程（裝飾、修葺保養等） | HK$873 億（−6.0%）≈ USD 112 億 ≈ NT$3,526 億 | 2024 | [新聞公報](https://www.info.gov.hk/gia/general/202503/11/P2025031100233.htm) | DB＋CF（含小型新建） | 高 |
| 香港 非地盤 2025 Q1／Q2／Q4 | HK$206／205／222 億 | 2025 | [Q1](https://www.censtatd.gov.hk/en/press_release_detail.html?id=5590)；[Q2](https://www.info.gov.hk/gia/general/202509/11/P2025091100340.htm) | 同上 | 高 |
| 香港 設計產業增加值 | HK$41 億（−6%）；>7,000 家 | 2022 | [HKTDC](https://research.hktdc.com/en/article/MzEzOTE1MDI5) | 全設計業 | 中 |
| 新加坡 interior fitting-out（F&S） | SGD 48.751 億 ≈ USD 36.7 億 ≈ NT$1,155 億 | 2022E | [HKEX 招股書](https://www1.hkexnews.hk/listedco/listconews/sehk/2020/0507/9270144/sehk19101000768.pdf) | DB＋CF | 中 |
| 新加坡 室內設計服務 | USD 7.7 億 → 12.2 億（2033） | 2024 | [designbureau.sg 轉引 DMI](https://designbureau.sg/insights/commercial-interior-design-trends-statistics-singapore-2026-pQ5n8w/) | D | 低 |
| 馬來西亞 傢俱＋室內設計（Ken） | USD 24.3 億 ≈ RM 107 億 | 2025 | [Ken MY](https://www.kenresearch.com/industry-reports/malaysia-furniture-and-interior-design-market) | FU | 低 |
| 馬來西亞 居家修繕（Ken） | ≈USD 10 億；住宅交易 RM 1,082.7 億 | 2025 | [Ken MY HI](https://www.kenresearch.com/industry-reports/malaysia-home-improvement-market) | HI | 低 |
| 泰國 居家修繕產業 | THB 4,795 億（2023）、3,862 億（2018），CAGR 4.4% ≈ USD 145 億 | 2023 | [SEC 上市文件](https://market.sec.or.th/public/ipos/IPOSGetFile.aspx?TransID=646423&TransFileSeq=87) | HI | 中 |
| 泰國 二手房占比 | 60% | 2025-10 | [Matichon](https://www.matichon.co.th/economy/news_5437496) | 需求指標 | 中 |
| 越南 居家修繕（IMARC） | USD 15.23 億 | 2025 | [IMARC VN](https://www.imarcgroup.com/vietnam-home-improvement-market) | HI | 低 |
| 越南 傢俱（Mordor） | USD 97.6 億 → 148.7 億（2031） | 2025 | [Mordor VN](https://www.mordorintelligence.com/industry-reports/vietnam-furniture-market) | FU（含出口） | 中 |
| 印尼 傢俱＋現代室內（Ken） | USD 84 億 → 128.8 億（2032），6.3% | 2025 | [Ken ID](https://www.kenresearch.com/indonesia-furniture-and-modern-interiors-market) | FU | 低 |
| 印尼 室內設計（Credence） | USD 8.25 億 → 11.58 億（2032），3.82% | 2023 | [Credence ID](https://www.credenceresearch.com/report/indonesia-interior-design-market) | D | 低 |
| 菲律賓 傢俱＋室內（Ken） | USD 26 億，6.8% | 2025 | [Ken 區域表](https://www.kenresearch.com/indonesia-furniture-and-modern-interiors-market) | FU | 低 |
| 印度 室內設計（IMARC） | USD 368.9 億，8.16% 至 2034 | 2025 | [IMARC IN](https://www.imarcgroup.com/india-interior-design-market) | D＋FU | 低–中 |
| 印度 室內設計（Mordor） | USD 314.3 億 | 2025 | [Mordor IN](https://www.mordorintelligence.com/industry-reports/india-interior-design-market) | D＋FU | 低–中 |
| 印度 線上居家修繕（Redseer） | ≈USD 10 億 → 30–32 億（FY31） | 2025 | [Redseer](https://redseer.com/articles/tapping-into-the-everyday-instant-home-services-and-the-next-habit-loop/) | HI 線上 | 中 |
| 印度 Livspace／HomeLane 營收 | ₹1,148 crore（FY23）／₹756 crore（FY25，+22%） | FY23／FY25 | [Wikipedia](https://en.wikipedia.org/wiki/Livspace)；[franchisebazar](https://www.franchisebazar.com/blog/homelane-franchise-2026-indias-fastest-growing-home-interiors-opportunity) | 公司 | 中／低 |
| 亞太 室內設計（GVR） | USD 305 億 → 416 億（2030），5.5% | 2024 | [GVR APAC](https://www.grandviewresearch.com/horizon/outlook/interior-design-market/asia-pacific) | D | 中 |
| 亞太 住宅翻修（Ken） | USD 1,600 億 → 2,180 億（2032），4.5% | 2025 | [Ken APAC](https://www.kenresearch.com/industry-reports/asia-pacific-residential-remodeling-market) | RR | 低–中 |
| 亞太 住宅翻修（FBI） | ≈USD 6,050 億（全球 29.5%） | 2025 | [FBI](https://www.fortunebusinessinsights.com/home-renovation-market-112345) | RR（廣） | 低 |
| 亞太 DIY（R&M／Mordor） | USD 923 億／64 億 | 2025 | [R&M](https://www.researchandmarkets.com/report/asia-pacific-diy-home-improvement-market)；[Mordor](https://www.mordorintelligence.com/industry-reports/asia-pacific-diy-home-improvement-market) | HI | 低–中／中 |
| 亞太 辦公 fit-out 平均成本 | USD 1,550/m²；新加坡 2,029、東京 1,994、台北 1,593、金邊 375 | 2026 | [JLL via cfotech](https://cfotech.asia/story/jll-warns-asia-pacific-office-fit-out-costs-keep-rising)；[KF via irei](https://irei.com/publications/article/asia-pacific-office-fit-out-costs/) | CF 單位成本 | 高 |
| 人均 GDP（IMF WEO 2026/04 轉載） | SG 99,365；HK 56,893；TW 39,489；KR 36,227；JP 35,973；MY 13,949；CN 13,968；TH 8,057；ID 5,082；VN 4,829；PH 4,270；IN 2,675（USD） | 2025 | [Worldometers](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal) | 名目 | 中（轉載） |

---

## 10. 對台灣業者（室內裝修＋不動產＋家居零售集團）的啟示

1. **台灣是 12 市場中唯一「連一個 A／B 級市場規模數字都沒有」的高所得市場**：日本有矢野、南韓有 CERIK、香港有 C&SD 季報、新加坡有招股書級 F&S 估計，而台灣只有民營平台推估的 5,500 億與 20 年前的 ABRI 研究。集團若要對外發布市場數據或向投資人／董事會說明 TAM，應**自行以財政部「營利事業家數及銷售額」（室內裝潢業、傢俱零售等細業別）建立官方口徑系列**（[財政部查詢說明](https://www.mof.gov.tw/singlehtml/1412?cntId=63687)），這本身即是可對外發布的產業話語權。
2. **5,500 億口徑相當於 GDP 的 1.9%，高於日本（1.1%）與南韓（1.2–1.4%）**：若集團內部規劃以此為 TAM，應假設其中含交屋裝修（DF）、商業空間（CF）與傢俱家電；純住宅翻修（RR）合理區間依東北亞比率（GDP 1.1–1.4%）推算約 **NT$3,200–4,100 億**，純設計費（D，GDP 0.12–0.15%）約 **NT$350–440 億**。
3. **日本模式顯示成熟市場的成長來自「單價」而非「件數」**：矢野 2025 +2.5% 全靠資材人工漲價與斷熱補助帶動加購；台灣 2026–2027 交屋潮退場後，業者應轉向節能／適老／補助導向的高單價翻修，而非追求案件量。
4. **中國與香港為負成長警訊**：智研室內設計規模三年縮 30%、香港非地盤工程連續負成長；集團若有大中華商業裝修業務，應以官方數列而非研究機構 +6% 預測做預算。
5. **東南亞四國的「USD 幾十億市場」多為傢俱口徑（FU）**：Ken 印尼 84 億、菲律賓 26 億、馬來西亞 24 億皆主要是傢俱家飾；對家居零售集團而言反而是正面訊號（零售可量化），但對裝修服務而言，真正的 RR／D 市場規模仍不明，進入前需自建估計（可用 fit-out 單位成本 × 竣工面積）。
6. **印度 USD 300 億級數字不可當 TAM**：Livspace＋HomeLane 合計營收不到 USD 3 億，組織化滲透 <1%；若評估合作或投資，用公司財報而非市場報告。
7. **商用裝修報價可直接對標亞太成本指南**：台北 USD 1,593/m²（KF 2026）介於新加坡／東京（~2,000）與吉隆坡（RM 6,908/m² ≈ USD 1,570 高階）之間；台灣業者赴東南亞承接商辦案，價格競爭力有限（印度、越南、金邊成本僅台北 1/4–1/2），應以設計與品質定位。
8. **對外引用政策**：集團任何對外文件引用亞太市場數字時，依 §7.2 標口徑與來源等級，避免 Mordor／GVR 同名異量（差 14 倍）造成的信譽風險。

---

## 11. 資料缺口

| 缺口 | 說明 | 建議補法 |
|---|---|---|
| 台灣財政部「室內裝潢業」銷售額與家數（2023–2025） | 財政統計月報表 3-9～3-12／財政統計資料庫存在但本輪無法開啟；113／114 年營業稅統計表未搜得 | 整合階段直接查詢財政統計資料庫（行業標準分類 4320 室內裝潢業、4700 傢俱零售等） |
| 台灣 100 室內設計「5,500 億」計算方式 | 新聞稿稱「依財政部數據推估」，未揭露細業別與加總方式 | 向數字科技／100 室內設計索取方法說明 |
| 中裝協 2024 年度行業綜合數據統計之總產值 | 2025-12-19 已發布，摘要無數字；僅有智研 2023 年 5.78 萬億（另一來源標 2021 年） | 開啟中裝新網原文核對年份與總產值 |
| 艾瑞 2024／2025 年家裝報告 | 僅有 2023 年版預測 3.78 萬億；未見房市下行後之更新 | 查艾瑞官網 2025 年發布 |
| CERIK 리모델링 2025 實績／更新預測；통계청 건설업조사 | 僅有 2020 年預測 | 查 CERIK 2024–2026 報告與 KOSIS |
| 矢野「住宅リフォーム市場」定義原文 | 摘錄未重述四大分類定義 | 開啟矢野新聞稿確認 |
| 香港 2025 Q3 非地盤數字與發展局「裝修、修葺及保養」細分 | 全年僅能推估 ≈HK$850 億 | 開啟 C&SD Q3 2025 新聞稿、DEVB 表 168 |
| 新加坡 DOS 細業別（SSIC 74 specialised design、43 fit-out） | 僅取得全服務業總額 | SingStat Table Builder「Key Indicators by Detailed Industry」 |
| 馬來西亞 DOSM 室內裝潢工程產值 | 前稿摘要提及 RM 20 億（2024）但無 URL | 開啟 DOSM Construction Statistics Q4 2025 原文 |
| 泰國 Kasikorn／Krungsri 翻修市場估計；Mr. DIY 文件 2024 更新（前稿提及 1,826 億泰銖零售口徑，無 URL） | 僅有 2023 年 HI 4,795 億 | 查 KResearch／Krungsri Research 2025–2026 |
| 越南 GSO、印尼 BPS、菲律賓 PSA 建築／裝修細項 | 本輪未搜得 | 查各國統計局建築業產值（specialised construction activities） |
| 6Wresearch 各國 2025 基準值（SG／MY／VN／ID／PH／KR） | 付費牆，只露 CAGR | 索取樣本報告 |
| Statista 1474530 亞太各國居家修繕規模 | 付費 | 集團 Statista 帳號 |
| Redseer 最新（2024–2025）印度家居室內總量與組織化占比 | 僅有 2018／FY19 與線上 HI | 查 Redseer 2025 reports |
| IMF WEO 2026/04 原始人均 GDP 與人口 | API／PDF 被阻擋，人均 GDP 為 Worldometers 轉載，人口為研究者概略值 | 以 IMF WEO 資料庫覆寫 §5.1 全表 |
| 商用裝修（CF）各國總量 | 無可信來源 | 以成本指南 × 官方竣工面積自建 |
| Grand View APAC 新版（2026–2033）基準值 | 僅取得 CAGR 5.9% | 開啟 GVR 頁面 |
| Mordor、IMARC、Technavio、Allied、Precedence、EMR 的「亞太室內設計」獨立報告 | 經兩輪共 4 次搜尋確認不存在公開頁面（僅軟體／DIY／傢俱） | 視為不存在 |

---

## 12. 來源清單

| # | 標題 | 機構 | 年份 | URL |
|---|---|---|---|---|
| 1 | 住宅リフォーム市場に関する調査を実施（2026 年）：2025 年 7.5 兆円、2026 年 7.7 兆円予測 | 矢野経済研究所（via DreamNews） | 2026 | https://www.dreamnews.jp/press/0000356164 |
| 2 | 2025 年住宅リフォーム市場規模は 7 兆 5119 億円 | ibnewsnet | 2026 | https://online.ibnewsnet.com/sp/gy260717-01.html |
| 3 | リフォーム市場、2026 年は 7.7 兆円へ拡大予測 | 新建ハウジング | 2026 | https://www.s-housing.jp/archives/427008 |
| 4 | 住宅リフォーム市場に関する調査を実施（2025 年） | 矢野経済研究所 | 2025 | https://www.yano.co.jp/press-release/show/press_id/3877 |
| 5 | 2026 年版 住宅リフォーム市場の展望と戦略 | 矢野経済研究所 | 2026 | https://www.yano.co.jp/market_reports/C68101800 |
| 6 | 矢野経済研究所、2024 年度は 7.3 兆円に | BCI | 2025 | https://online.bci.co.jp/article/detail/3587 |
| 7 | Japan Interior Design Market Size & Outlook, 2030 | Grand View Research | 2025 | https://www.grandviewresearch.com/horizon/outlook/interior-design-market/japan |
| 8 | 리모델링 시장, 2020 년 30 조원에서 2030 년 44 조원 | 한국건설산업연구원 | 2020 | https://www.cerik.re.kr/board/press/589 |
| 9 | 국내 리모델링 시장 지속성장, 올 30 조서 2030 년 44 조 전망 | 국토일보 | 2020 | https://www.ikld.kr/news/articleView.html?idxno=223589 |
| 10 | 리모델링 시장규모 2030 년 46 조원으로 2.5 배 급성장 전망 | 대한전문건설신문（신영증권） | 2021 | https://www.koscaj.com/news/articleView.html?idxno=111927 |
| 11 | 中国建筑装饰设计行业 2022-2024 发展状况分析 | 中裝新網（中國建築裝飾協會） | 2025 | http://www.cbda.cn/html/yj/20250630/142674.html |
| 12 | 2024 年度中国建筑装饰协会行业综合数据统计发布 | 中國建築裝飾協會 | 2025 | http://www.cbda.cn/html/hyyj/20251219/143631.html |
| 13 | 国家统计局：2024 年建筑业增加值 89949 亿元 | 中裝新網轉載國家統計局 | 2025 | http://www.cbda.cn/html/yj/20250312/141927.html |
| 14 | 2023 年中国家装行业研究报告 | 艾瑞咨詢 | 2023 | https://zhongzhihui.oss-cn-beijing.aliyuncs.com/industryPdf/艾瑞咨询：2023年中国家装行业研究报告.pdf |
| 15 | 预计 2025 年家装行业市场规模将达到 37802 亿元 | 華聲在線 | 2024 | https://m.voc.com.cn/xhn/news/202401/19324088.html |
| 16 | 研判 2025！中国室内设计行业产业链图谱、市场规模 | 智研咨詢 | 2025 | https://www.chyxx.com/industry/1221629.html |
| 17 | 2025 年中国建筑室内设计行业现状及趋势研判 | 智研咨詢 | 2025 | https://www.chyxx.com/industry/1213062.html |
| 18 | 中建协发布 2024 年建筑业发展统计分析 | 陝西省建築業協會 | 2025 | https://www.sxjzy.org/h-nd-38035.html |
| 19 | China Interior Design Market Size & Outlook | Grand View Research | 2025 | https://www.grandviewresearch.com/horizon/outlook/interior-design-market/china |
| 20 | 裝修市場熱！年產值上看 5500 億元 | 聯合報 | 2025 | https://udn.com/news/story/7241/9245511 |
| 21 | 2026 有望持續成長！裝修年產值上看 5500 億 | 聯合報 | 2025 | https://udn.com/news/story/7241/9242628 |
| 22 | 住宅裝修市場規模推估方法之研究 | 內政部建築研究所 | — | https://www.abri.gov.tw/News_Content_Table.aspx?n=807&s=38057 |
| 23 | 住宅裝修市場 年規模近兩千億 | 人間福報 | — | https://www.merit-times.com.tw/NewsPage.aspx?unid=146493 |
| 24 | 產業服務電子報（裝修產業年產值 1,100 億） | 經濟部產業發展署 | — | https://www.ida.gov.tw/ctlr?PRO=epaper.rwdEpaperView&id=2479 |
| 25 | 如何查詢營利事業家數及銷售額統計資料 | 財政部 | — | https://www.mof.gov.tw/singlehtml/1412?cntId=63687 |
| 26 | 起徵點上調 25％ 12 萬店家受惠 | 工商時報 | 2024 | https://www.ctee.com.tw/news/20241212702008-430503 |
| 27 | 二零二五年第四季及全年建造工程完成量統計數字 | 香港政府統計處 | 2026 | https://www.info.gov.hk/gia/general/202603/12/P2026031200295.htm |
| 28 | 二零二四年第四季及全年建造工程完成量統計數字 | 香港政府統計處 | 2025 | https://www.info.gov.hk/gia/general/202503/11/P2025031100233.htm |
| 29 | 二零二五年第二季建造工程完成量統計數字 | 香港政府統計處 | 2025 | https://www.info.gov.hk/gia/general/202509/11/P2025091100340.htm |
| 30 | Construction output for first quarter of 2025 | C&SD | 2025 | https://www.censtatd.gov.hk/en/press_release_detail.html?id=5590 |
| 31 | 主要承建商在地盤進行建造工程的總值（表 168） | 香港發展局 | — | https://www.devb.gov.hk/tc/publications_and_press_releases/figures_and_statistics/gross_value/index.html |
| 32 | Design Industry in Hong Kong | HKTDC Research | 2024 | https://research.hktdc.com/en/article/MzEzOTE1MDI5 |
| 33 | Industry Overview（Frost & Sullivan，Singapore interior fitting-out） | HKEX 招股書 | 2020 | https://www1.hkexnews.hk/listedco/listconews/sehk/2020/0507/9270144/sehk19101000768.pdf |
| 34 | Singapore Services Sector at a glance | SingStat | 2025 | https://www.singstat.gov.sg/-/media/files/visualising_data/infographics/industry/singapore-services-sector.ashx |
| 35 | Commercial Interior Design Trends & Statistics Singapore 2026 | designbureau.sg（轉引 DMI／6W） | 2026 | https://designbureau.sg/insights/commercial-interior-design-trends-statistics-singapore-2026-pQ5n8w/ |
| 36 | Singapore Interior Design Market | 6Wresearch | 2025 | https://www.6wresearch.com/industry-report/singapore-interior-design-market-outlook |
| 37 | Malaysia Furniture and Interior Design Market 2025-2032 | Ken Research | 2025 | https://www.kenresearch.com/industry-reports/malaysia-furniture-and-interior-design-market |
| 38 | Malaysia Home Improvement Market 2026-2032 | Ken Research | 2025 | https://www.kenresearch.com/industry-reports/malaysia-home-improvement-market |
| 39 | Construction Statistics, Fourth Quarter 2025 | DOSM | 2026 | https://www.dosm.gov.my/portal-main/release-content/construction-statistics-fourth-quarter-2025 |
| 40 | Independent Market Research on the Home Improvement Industry（Mr. DIY IPO） | 泰國 SEC | 2024 | https://market.sec.or.th/public/ipos/IPOSGetFile.aspx?TransID=646423&TransFileSeq=87 |
| 41 | Thailand Home Improvement Market | Ken Research | 2025 | https://www.kenresearch.com/thailand-home-improvement-market |
| 42 | Thai Property Market Faces Toughest Challenge in Decades | Nation Thailand（SCB EIC／ttb） | 2025 | https://www.nationthailand.com/business/property/40056158 |
| 43 | จับตาตลาดบ้านมือสอง ดิสรัปต์บ้านใหม่ | Matichon | 2025 | https://www.matichon.co.th/economy/news_5437496 |
| 44 | Vietnam Home Improvement Market | IMARC | 2025 | https://www.imarcgroup.com/vietnam-home-improvement-market |
| 45 | Vietnam Architectural Services Market | IMARC | 2025 | https://www.imarcgroup.com/vietnam-architectural-services-market |
| 46 | Vietnam Furniture Market | Mordor Intelligence | 2025 | https://www.mordorintelligence.com/industry-reports/vietnam-furniture-market |
| 47 | Vietnam Home Improvement Market | Expert Market Research | 2025 | https://www.expertmarketresearch.com/reports/vietnam-home-improvement-market |
| 48 | Indonesia Furniture and Modern Interiors Market | Ken Research | 2025 | https://www.kenresearch.com/indonesia-furniture-and-modern-interiors-market |
| 49 | Indonesia Interior Design Market 2032 | Credence Research | 2024 | https://www.credenceresearch.com/report/indonesia-interior-design-market |
| 50 | Indonesia Interior Design Market (2025-2031) | 6Wresearch | 2026 | https://www.6wresearch.com/industry-report/indonesia-interior-design-market-outlook |
| 51 | Philippines Interior Design Market | 6Wresearch | 2025 | https://www.6wresearch.com/industry-report/philippines-interior-design-market-outlook |
| 52 | Philippines Furniture and Interior Design Market | Ken Research | 2025 | https://www.kenresearch.com/philippines-furniture-and-interior-design-market |
| 53 | India Interior Design Market | IMARC | 2025 | https://www.imarcgroup.com/india-interior-design-market |
| 54 | India Interior Design Market Size & Share Analysis | Mordor Intelligence | 2025 | https://www.mordorintelligence.com/industry-reports/india-interior-design-market |
| 55 | Tapping into the everyday: instant home services | Redseer | 2025 | https://redseer.com/articles/tapping-into-the-everyday-instant-home-services-and-the-next-habit-loop/ |
| 56 | Online Interior Design Market Updates | Redseer | 2019 | https://redseer.com/articles/online-interior-design-market-updates/ |
| 57 | Disruption in Indian Furniture Retailing | Redseer | 2018 | https://redseer.com/wp-content/uploads/2018/09/Disruption-in-Indian-furniture-retailing-_-31-August-2018-v1.pdf |
| 58 | Livspace | Wikipedia | 2025 | https://en.wikipedia.org/wiki/Livspace |
| 59 | Asia Pacific Interior Design Market Size & Outlook, 2030 | Grand View Research | 2025 | https://www.grandviewresearch.com/horizon/outlook/interior-design-market/asia-pacific |
| 60 | Interior Design Market Size, Share & Growth Report, 2033 | Grand View Research | 2026 | https://www.grandviewresearch.com/industry-analysis/interior-design-market-report |
| 61 | Interior Design Services Market Size & Share Analysis | Mordor Intelligence | 2025 | https://www.mordorintelligence.com/industry-reports/interior-design-services-market |
| 62 | Interior Design Market Analysis 2026（APAC／JP／KR 國家表） | Cognitive Market Research | 2026 | https://www.cognitivemarketresearch.com/interior-design-market-report |
| 63 | Asia-Pacific Residential Remodeling Market 2025-2032 | Ken Research | 2025 | https://www.kenresearch.com/industry-reports/asia-pacific-residential-remodeling-market |
| 64 | Home Renovation Market Size, Share & Trends | Fortune Business Insights | 2025 | https://www.fortunebusinessinsights.com/home-renovation-market-112345 |
| 65 | Home Improvement Market Size, Share, Report, 2034 | Fortune Business Insights | 2025 | https://www.fortunebusinessinsights.com/home-improvement-market-113207 |
| 66 | Remodeling Market Size, 2025-2034 | Global Market Insights | 2025 | https://www.gminsights.com/industry-analysis/remodeling-market |
| 67 | Asia-Pacific DIY Home Improvement Market Size & Competitors | Research and Markets | 2025 | https://www.researchandmarkets.com/report/asia-pacific-diy-home-improvement-market |
| 68 | Asia-Pacific DIY Home Improvement Market | Mordor Intelligence | 2026 | https://www.mordorintelligence.com/industry-reports/asia-pacific-diy-home-improvement-market |
| 69 | Home Improvement Services Market | IMARC | 2025 | https://www.imarcgroup.com/home-improvement-services-market |
| 70 | APAC home improvement market size in selected countries | Statista | 2022 | https://www.statista.com/statistics/1474530/apac-home-improvement-market-size-in-selected-countries |
| 71 | Interior Fit Out Market Size | DataM Intelligence | 2025 | https://www.datamintelligence.com/research-report/interior-fit-out-market |
| 72 | Commercial Interior Design Market Report | Dataintelo | 2025 | https://dataintelo.com/report/commercial-interior-design-market-report |
| 73 | Asia Pacific Office Fit-Out Cost Guide 2026 | JLL | 2026 | https://www.jll.com/en-in/guides/apac-fit-out-costs-guide |
| 74 | JLL warns Asia Pacific office fit-out costs keep rising | cfotech.asia | 2026 | https://cfotech.asia/story/jll-warns-asia-pacific-office-fit-out-costs-keep-rising |
| 75 | Office Fit Out Cost Guide Asia Pacific 2026 | Cushman & Wakefield | 2026 | https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office |
| 76 | India Leads Asia Pacific in Fit-Out Cost Efficiency | Construction World（C&W） | 2026 | https://www.constructionworld.in/latest-construction-news/real-estate-news/india-leads-asia-pacific-in-fit-out-cost-efficiency/88743 |
| 77 | Asia Pacific office fit-out costs（Knight Frank） | IREI | 2026 | https://irei.com/publications/article/asia-pacific-office-fit-out-costs/ |
| 78 | Global office fit-out cost guide 2026 — Asia-Pacific | Turner & Townsend | 2026 | https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026/asia-pacific |
| 79 | GDP per Capita in Asia (2025) — IMF | Worldometers | 2026 | https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal |
| 80 | GDP per Capita in Asia (2026) — IMF | Worldometers | 2026 | https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal |
| 81 | World Economic Outlook, April 2026; Statistical Appendix | IMF | 2026 | https://www.imf.org/-/media/files/publications/weo/2026/april/english/statsappendix.pdf |
| 82 | Thailand Home Improvement Market（排除） | Mobility Foresights | 2025 | https://mobilityforesights.com/product/thailand-home-improvement-market |
