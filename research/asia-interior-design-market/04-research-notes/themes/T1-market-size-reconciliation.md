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
