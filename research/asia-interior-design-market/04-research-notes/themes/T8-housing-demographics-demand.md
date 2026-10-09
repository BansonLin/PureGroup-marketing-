# T8：住宅存量、人口結構與不動產連動（需求引擎）（Housing stock, demographics and real-estate linkage: the renovation demand engine）

研究日期：2026-10-08 首稿（§1–§2）／2026-10-09 續寫完稿（§3–§12）｜涵蓋市場：日本、南韓、新加坡、香港、台灣、中國大陸、馬來西亞、泰國、越南、印尼、菲律賓、印度（12 市場）

> **研究方法備註（務必先讀）**
> - 本檔分兩輪完成：第一輪（2026-10-08）執行 20 次 WebSearch 寫成 §1–§2；第二輪（2026-10-09）再執行 **21 次 WebSearch**（英、日、韓、中、泰、越、印尼文）完成 §3–§12。環境禁止 WebFetch／curl，所有數字皆取自搜尋結果摘要中可辨識的原文引述，每個數字均附 URL。另沿用本專案既有筆記（`countries/*`、`themes/T1`、`verification/*`）中已附 URL 的數字，以「（既有筆記）」標示。
> - 第一輪摘要中若干數字（日本首都圈 2025 年中古成約 49,114 件、南韓 2026 年入住量 17.2–18.3 萬戶、中國 5 年期 LPR 3.5% 與宏觀槓桿率 302.4%、台灣家庭負債／GDP 94.3%、泰國 2025 年中古占比 60%、印度 2025 年七大城銷售 395,625 戶）在第二輪無法重新取得 URL，**已自本文移除並列入 §11 缺口**，不以無來源數字呈現。
> - 標示：**【官方】**＝統計局／央行／部會／立法機關原始發布或其直接轉載；**【業界／媒體】**＝研究機構、仲介、銀行、媒體整理（口徑一律記錄）；**【示意】**＝本人以已引用數字推算或假設，非來源數字；**無資料**＝本輪未找到，列入 §11 缺口，不以估計填補。
> - 匯率：沿用 T1 檔之「2025–2026 概略參考匯率」，整合時以當日官方匯率覆寫：USD/TWD 31.5；USD/JPY 150；USD/KRW 1,400；USD/CNY 7.20；USD/SGD 1.33；USD/HKD 7.80；USD/MYR 4.40；USD/THB 33；USD/VND 26,000；USD/IDR 16,000；USD/PHP 57；USD/INR 86。所有 USD／TWD 換算皆為本人計算。
> - 信心等級：高＝官方原始值或 ≥2 獨立來源一致；中＝單一官方轉載或單一研究機構；低＝部落格／聚合站／本人推算。

---

## 1. 摘要

1. 十二市場的翻修需求引擎可分三型。**「老化存量型」**（台灣、香港、南韓、日本、新加坡）：人均 GDP（IMF WEO 2026-04，2026 年名目）USD 35,703–107,758、65 歲以上占 20–30%，且存量明顯老化——台灣房屋稅籍住宅平均屋齡 34.1 年、30 年以上 554.6 萬宅（59%，2025Q2）；南韓 2025 年人口住宅總普查 2,018 萬戶中 30 年以上 618 萬戶（30.6%）；香港私樓 48–64% 樓齡滿 30 年；日本 1980 年以前（築 43 年以上）住宅 1,181 萬戶（約 21%）。中古交易已是主流：香港 2025 年二手私人住宅 39,821 宗、占私宅買賣 66%；日本首都圈 2024 年中古公寓成約 37,222 件、超過新建供給約 2.3 萬戶；泰國 2026Q1 中古占移轉 67%。
2. **「新建交屋型」**（越南、印尼、菲律賓、印度、馬來西亞）：65 歲以上僅 6–10%，需求由住房缺口與新案交屋驅動——印尼 2026 年 3 月住房所有權缺口 929 萬戶（12.39%）、FLPP 補貼房貸 2025 年放款 278,868 戶；菲律賓 Pag-IBIG 2025 年房貸放款 PHP 1,405.4 億（90,727 戶）；印度七大城 2026Q3 推案 114,320 戶（+18%）但未售升至約 63.1 萬戶；越南 2025 年成交 579,718 筆（土地 441,693、公寓＋獨立屋 138,025）；馬來西亞 2025 年完工 99,877 戶但滯銷（overhang）2026Q1 升至 32,801 戶。
3. **「過渡型」**（中國大陸、泰國）：中國 2026 上半年二手房占新房＋二手交易 50.4%（住建部，半年度首次過半，18 省二手面積超新房；1–8 月 52.4%），同期新建商品房銷售面積 4.01 億 m²（−11.6%）；泰國 2025 年移轉 316,214 戶（−9.1%）後，央行 LTV 100% 與移轉／抵押費 0.01% 優惠延至 2027-06-30，2026 上半年移轉反彈 +17.6%。
4. 台灣是全區「存量最老、交易最冷、新屋完工創高」的罕見組合：2025 年建物買賣移轉 261,308 棟（−25.5%）、住宅使照約 14.3 萬宅（1997 年以來新高）、低度使用住宅 914,196 宅（9.79%，2024 下半年，歷年新高；5 年內新屋空屋率 22.91%）、住宅自有率 2025 年降至 83.95%（16 年新低）；央行第二戶貸款成數 2026-03-20 由 5 成升至 6 成、2026 年第三季再升至 7 成；五大銀行新承做房貸利率 2026-07 約 2.29%；青安 3.0 自 2026-08-01 實施（前 3 年 1.775%）。
5. 東北亞進入「新建創低、利率反轉」：日本 2025 年新設住宅著工 740,667 戶（−6.5%、3 年連減、62 年來最低），日銀 2026-09-18 升息至 1.25%（1995 年以來最高）；南韓 2025 年完工約 30 萬戶（2024 年 44.9 萬）、買賣 726,111 件（+13.0%），韓銀 2026-08-27 升至 3.00%，8 月銀行新承做房貸利率 4.66%（3 年 9 個月最高），10·15 對策將首都圈房貸上限壓至 6 億／4 億／2 億韓元；未售（미분양）2026-08 末 69,134 戶。
6. 家庭負債／GDP（BIS，2025-12）：南韓 88.6%、香港 87.8%、泰國 87.5%、馬來西亞 69.8%、日本 61.1%、中國 58.0%；高槓桿市場與老化存量市場高度重疊，翻修支出對利率循環（日、韓升息；台、馬、泰持平或寬鬆；印尼、印度升息）極為敏感。
7. 本檔以「30 年以上存量占比 × 中古交易占比 × 所得」建構翻修需求指標 R（§5，方法公開、分項可追溯）：香港 0.80、台灣 0.74、新加坡 0.72（存量屋齡為代理值）、南韓 0.58、馬來西亞 0.55（低信心）、日本 0.53–0.69（區間）、中國 0.53、泰國 0.51、越南 0.29；印尼、菲律賓、印度因中古交易占比無資料而無法計算，改以「新屋交屋量」衡量。R 排序與 T1 校準之住宅翻修支出占 GDP（香港 2.5–2.6%、中國 1.95–2.67%、南韓 1.23–1.41%、日本 1.10–1.13%）方向一致，但台灣（0.69–1.89%，低信心）與新加坡（0.61%）偏低，顯示台灣翻修市場規模估計可能被低估或存量翻修轉化率低於結構所暗示。
8. 宜蘭（集團所在地）：2025 年建物買賣移轉約 5,270 棟（−23.6%）、房價指數 178.63（−0.81%，東台灣最抗跌）、2025 年實價中位數單價約 29.83 萬／坪；2025 年 5 月合法民宿 2,177 家、8,085 房（全台第一，超越花蓮 1,748 家）；電梯大樓交易占比 43.5% 首度超越透天 38.6%；宜蘭成交屋齡分布與外地買家占比官方統計本輪未取得。

---

## 2. 總體經濟與人口（Q1：Macro & demographics）

### 2.1 Takeaway
IMF WEO 2026 年 4 月（經 Worldometer／T1 轉載）之 2026 年名目人均 GDP：新加坡 107,758、香港 59,640、台灣 42,103、南韓 37,412、日本 35,703、馬來西亞 15,085、中國 14,874、泰國 8,105、印尼 5,362、越南 5,115、菲律賓 4,443、印度 2,813 美元；PPP（僅高所得五市場）：新加坡 173,708、台灣 98,051、香港 84,212、南韓 68,624、日本 59,207。65 歲以上占比：日本 29.5%（2026-04，總務省）、香港 25.0%（2025）、南韓 21.4%（2026）、台灣約 20%（2025）、泰國 16.0%（2025）、越南 9.5%（2025）、馬來西亞 8.1%（2024）、印尼 7.3%（2024）、印度 6.8%、菲律賓 5.8%（2021 估）。「高所得 × 高齡 × 高都市化 × 小家戶」四者同時成立者只有日本、南韓、台灣、香港、新加坡。

### 2.2 十二市場總經與人口表

| 市場 | 人均 GDP 名目 USD（2026，IMF WEO 2026-04） | 人均 GDP 名目 USD（2025） | 人均 GDP PPP（2026） | 人口 | 家戶數／戶量 | 都市化 % | 中位數年齡 | 65+ 占比 2025 | 65+ 占比 2035 投影 | 來源 |
|---|---|---|---|---|---|---|---|---|---|---|
| 日本 | **35,703** | 35,973 | **59,207** | 1.224 億（2026，WPP 投影）；123.4 百萬（T1） | 居住世帯あり住宅 5,566.5 萬戸（2023）【官方，代理指標】 | 無資料 | 49.4（2024） | **29.5%（2026-04-01，總務省）**；30.0%（WPP 2025） | 無資料 | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Worldometer 2025](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal)；[Wikipedia PPP（IMF 2026）](https://en.wikipedia.org/wiki/List_of_Asian_countries_by_GDP_(PPP)_per_capita)；[demographer.org 引總務省](https://demographer.org/countries/japan-demographics/)；[populationpyramid.net JP 2025](https://www.populationpyramid.net/japan/2025/)；[populationpyramids.org JP](https://www.populationpyramids.org/japan)；[Wikipedia Demographics of Asia（WPP 2024 中位數）](https://en.wikipedia.org/wiki/Demographics_of_Asia)；[総務省 基本集計](https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf) |
| 南韓 | **37,412** | 36,227 | **68,624** | 5,172 萬（2024） | 無資料 | 無資料 | 45（2024）；46.2（2026）；**52.0（2035）** | **21.4%（2026，WPP）** | 無資料（中位數 2035 有） | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Worldometer KR 人口](https://www.worldometers.info/world-population/south-korea-population/)；[populationpyramids.org KR](https://www.populationpyramids.org/south-korea)；[populationpyramid.net 2035](https://www.populationpyramid.net/republic-of-korea/2050/) |
| 新加坡 | **107,758** | 99,365（T1） | **173,708** | 6.0 百萬（T1，概略） | 無資料；HDB 組屋居住之居民家戶占 77.2%（DOS 轉述） | 100（城邦） | 無資料 | 無資料 | 無資料 | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Wikipedia PPP](https://en.wikipedia.org/wiki/List_of_Asian_countries_by_GDP_(PPP)_per_capita)；[smartwealth.sg 引 DOS](https://smartwealth.sg/housing-household-statistics-singapore/) |
| 香港 | **59,640** | 56,893（T1） | **84,212** | 7.5 百萬（T1，概略） | 無資料 | 100（城邦） | 無資料 | **25.0%（2025，政府經濟分析）**；23.7%（UN 口徑） | 無資料；**36%（2046）** | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[HK Economy Box 6.1](https://www.hkeconomy.gov.hk/en/pdf/box-25q4-6-1.pdf)；[Visual Capitalist（UN）](https://www.visualcapitalist.com/ranked-25-countries-most-seniors-in-2025-vs-2100/) |
| 台灣 | **42,103** | **39,489**（主計總處概估 39,477） | **98,051** | 23.4 百萬（T1，概略） | 無資料（本輪） | 無資料 | 無資料 | **≈20%（2025）** | 無資料；38.4%（2050，Statista）vs 31.7%（2050，UN 口徑） | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Taipei Times（IMF）](https://www.taipeitimes.com/News/taiwan/archives/2025/12/24/2003849443)；[聯合新聞網（主計總處）](https://udn.com/news/story/7238/9299429)；[Statista TW 年齡結構](https://www.statista.com/statistics/321439/taiwan-population-distribution-by-age-group/) |
| 中國大陸 | **14,874** | 13,968（T1） | 無資料 | 1,408 百萬（T1，概略） | 無資料 | **66.4%（2024，UN）／67%（2024，國家統計口徑）** | 無資料 | 無資料 | 無資料 | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Worldometer CN](https://www.worldometers.info/world-population/china-population/)；[Statista CN 城鎮化](https://www.statista.com/statistics/270162/urbanization-in-china/) |
| 馬來西亞 | **15,085** | 13,949（T1） | 無資料 | 34.1 百萬（T1，概略） | 無資料 | **76.44%（2023，World Bank）** | 無資料 | **8.1%（2024，DOSM）** | **10.4%（2035，政府推估）**；14%（2048，高齡國家門檻） | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Wikipedia Urbanization（WB）](https://en.wikipedia.org/wiki/Urbanization_by_sovereign_state)；[The Star 2026-07-07](https://www.thestar.com.my/news/nation/2026/07/07/one-in-10-malaysians-will-be-aged-65-and-above-by-2035)；[MOF Malaysia](https://mof.gov.my/portal/en/news/press-citations/malaysia-to-become-aged-nation-by-2048-amir-hamzah) |
| 泰國 | **8,105** | 8,057（T1） | 無資料 | 71.6 百萬（T1，概略） | 無資料 | **54.3%（2024，NSO／WB）** | 41.1（2024） | **16.0%（2025）**；16.7%（2026） | 無資料 | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Helgi Library TH](https://www.helgilibrary.com/indicators/urban-population-as-of-total-population/thailand)；[populationpyramid.net TH 2025](https://www.populationpyramid.net/thailand/2025/)；[TH 2026](https://www.populationpyramid.net/thailand/2026/) |
| 越南 | **5,115**（T1，IMF）；**5,026（2025，統計局）** | 4,829（T1）／5,026（統計局） | 無資料 | **1.023 億（2025 平均，+0.99%）** | 無資料 | **38.6%（2025，統計局）** | 32.9（2024） | **9.5%（2025，WPP）**；9.9%（2026）；60+ 14.5%（2025，統計局） | 無資料 | [Báo Chính phủ](https://baochinhphu.vn/gdp-nam-2025-tang-truong-802-binh-quan-dau-nguoi-dat-5026-usd-102260105152509472.htm)；[Cục Thống kê](https://www.nso.gov.vn/tin-tuc-thong-ke/2026/01/thong-cao-bao-chi-ve-tinh-hinh-dan-so-lao-dong-viec-lam-quy-iv-va-nam-2025/)；[populationpyramid.net VN 2025](https://www.populationpyramid.net/viet-nam/2025/)；[populationpyramids.org VN](https://www.populationpyramids.org/vietnam) |
| 印尼 | **5,362** | 5,082（T1） | 無資料 | 2.879 億（2026，WPP 投影） | 無資料；Jabodetabek 租屋家戶 124 萬（14.6%） | **59.2%（2024）**；58.12%（2023，WB） | 30.1（2024） | **7.3%（2024）**；7.8%（2026） | 無資料 | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[populationpyramid.net ID 2024](https://www.populationpyramid.net/indonesia/2024/)；[populationpyramids.org ID](https://www.populationpyramids.org/indonesia)；[Kompas.id](https://www.kompas.id/artikel/harga-rumah-semakin-tak-tergapai) |
| 菲律賓 | **4,443** | 4,270（T1） | 無資料 | **112,729,484（2024-07-01，POPCEN）** | 2020 普查家戶 26,376,522；每 100 個有人居住住宅單位有 105 戶 | **48.6%（2024，WB）** | 25.7（2024） | 5.80%（2021 估） | **7.9%（2035，WPP 轉載）** | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[PSA 2024 POPCEN](https://psa.gov.ph/content/2024-census-population-popcen-population-counts-declared-official-president)；[PSA 2020 CPH 住宅特徵](https://psa.gov.ph/content/housing-characteristics-philippines-2020-census-population-and-housing)；[TradingEconomics（WB）](https://tradingeconomics.com/philippines/urban-population-percent-of-total-wb-data.html)；[Wikipedia Demographics of the Philippines](https://en.wikipedia.org/wiki/Demographics_of_the_Philippines)；[populationpyramid.net PH 2035](https://www.populationpyramid.net/philippines/2035/) |
| 印度 | **2,813** | 2,675（T1） | 無資料 | 1,460 百萬（T1，概略） | 無資料 | **35.07%（2023，WB）** | 28.4（2024） | 6.83%（2021 估） | 無資料；14%（2050，UN）；60+ 約 15%（2036，政府推估） | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Wikipedia Urbanization（WB）](https://en.wikipedia.org/wiki/Urbanization_by_sovereign_state)；[Wikipedia Demographics of India](https://en.wikipedia.org/wiki/Demographics_of_India)；[UNFPA India](https://india.unfpa.org/en/news/india-ageing-elderly-make-20-population-2050-unfpa-report)；[PIB Elderly in India](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2183196&reg=48&lang=2) |

IMF 原始入口（本輪未能開啟）：[WEO 2026-04 Statistical Appendix](https://www.imf.org/-/media/files/publications/weo/2026/april/english/statsappendix.pdf)；[WEO 2026-04 全文](https://www.imf.org/-/media/files/publications/weo/2026/april/english/text.pdf)；UN WPP 2024：[population.un.org/wpp](https://population.un.org/wpp/)；World Bank 都市化：[data.worldbank.org](https://data.worldbank.org/?locations=TH-MY-ID-SG-PH-VN)。註：IMF 對印度採會計年度，2026 值與其他市場曆年值不完全對齊（[Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)）。

### 2.3 Cited Findings
- IMF WEO 2026 年 4 月（Worldometer 轉載）2026 年名目人均 GDP：新加坡 107,758、香港 59,640、台灣 42,103、南韓 37,412、日本 35,703、馬來西亞 15,085、中國 14,874、泰國 8,105、印尼 5,362、菲律賓 4,443、印度 2,813 美元；2025 年：台灣 39,489、南韓 36,227、日本 35,973 — [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Worldometer 2025](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal)；[Worldometer GDP by country 2026](https://www.worldometers.info/gdp/gdp-by-country/?region=asia&year=2026&metric=nominal)。注意：Worldometer 2026 頁另有一張未標示年份的表（日本 35,951、新加坡 98,814），應為 2025 值，本檔不採。
- PPP（IMF 2026 估計）：新加坡 173,708、台灣 98,051、香港 84,212、南韓 68,624、日本 59,207 國際元 — [Wikipedia List of Asian countries by GDP (PPP) per capita](https://en.wikipedia.org/wiki/List_of_Asian_countries_by_GDP_(PPP)_per_capita)；其餘七市場 PPP 本輪搜尋結果未列（缺口）。
- 台灣人均所得 2025 年 23 年來首次超越南韓並超越日本（IMF 2025-12 版：台灣 37,827、南韓 35,960、日本 34,720）— [Taipei Times](https://www.taipeitimes.com/News/taiwan/archives/2025/12/24/2003849443)
- 日本 65 歲以上 29.5%（2026-04-01，総務省統計局確定推計）— [demographer.org](https://demographer.org/countries/japan-demographics/)；WPP 口徑 2025 年 30.0% — [populationpyramid.net](https://www.populationpyramid.net/japan/2025/)
- 南韓 65+ 21.4%、中位數 46.2（2026）— [populationpyramids.org](https://www.populationpyramids.org/south-korea)；2035 年中位數 52.0 — [populationpyramid.net](https://www.populationpyramid.net/republic-of-korea/2050/)
- 香港 65+ 25.0%（2025）、推算 2046 年 36% — [HK Economy Box 6.1](https://www.hkeconomy.gov.hk/en/pdf/box-25q4-6-1.pdf)
- 馬來西亞 65+ 8.1%（2024）、2035 年 10.4%、2048 年達 14% — [The Star](https://www.thestar.com.my/news/nation/2026/07/07/one-in-10-malaysians-will-be-aged-65-and-above-by-2035)；[MOF](https://mof.gov.my/portal/en/news/press-citations/malaysia-to-become-aged-nation-by-2048-amir-hamzah)
- 菲律賓 2024 年普查人口 112,729,484；家戶人口 1.1233 億（99.6%）— [PSA](https://psa.gov.ph/content/2024-census-population-popcen-population-counts-declared-official-president)
- 越南 2025 年人均 GDP USD 5,026、人口 1.023 億、都市化 38.6%、60+ 14.5% — [Báo Chính phủ](https://baochinhphu.vn/gdp-nam-2025-tang-truong-802-binh-quan-dau-nguoi-dat-5026-usd-102260105152509472.htm)；[Cục Thống kê](https://www.nso.gov.vn/tin-tuc-thong-ke/2026/01/thong-cao-bao-chi-ve-tinh-hinh-dan-so-lao-dong-viec-lam-quy-iv-va-nam-2025/)

### 2.4 Inferences
- 以「人均 GDP ≥ USD 30,000 且 65+ ≥ 20%」篩選，只有日本、南韓、台灣、香港符合（新加坡 65+ 本輪無值），這四個市場加新加坡是「高齡友善翻修＋高單價全屋翻新」核心客群；中國一線城市（上海 2000 年前建成住房占 50.38%，見 §7）在城市層級符合同一條件。
- 南韓中位數年齡將在 2035 年達 52 歲（全球最高群），翻修需求將由「換屋裝修」轉向「原地老化改造」，與日本 2010 年代路徑相同。

### 2.5 Gaps
- IMF WEO 2026-04 之中國、馬來西亞、泰國、印尼、菲律賓、印度 PPP 人均 GDP；UN WPP 2024 之 2035 年 65+ 占比（12 市場皆缺，僅南韓中位數、馬來西亞政府推估、菲律賓轉載有 2035 值）；台灣、日本、南韓、中國之 World Bank 都市化比率；新加坡、中國、台灣 65+ 2025 精確值；家戶數與戶量（除日本居住世帯あり住宅、菲律賓 2020 普查外全缺）；人口欄之 T1 概略值未經 URL 驗證。

---

## 3. 住宅存量與屋齡（Q2：Housing stock & age）

### 3.1 Takeaway
官方普查／統計可直接給出「30 年以上存量占比」的只有台灣（59%，2025Q2 房屋稅籍）、南韓（30.6%，2025 普查）與香港（私樓 48–64%）；日本只能給「築 43 年以上 21%」（1980 年以前建成）、中國只能給「2000 年前建成約 35%（戶數，七普推算）」；新加坡以 HIP（1997 年以前建成組屋）累計獲選 49.4 萬戶作代理；東南亞五國與印度皆無屋齡分布統計。自有率呈「東南亞 ＞ 東亞」：印尼 85.07%、台灣 83.95%、馬來西亞 78.0%、日本 60.9%、南韓 58.4%（自有自住）、香港 50.9%。空屋率：日本 13.8%（900 萬戶）、台灣 9.79%（低度用電 91.4 萬宅）、新加坡私宅 6.4%（2026Q2）、香港私樓 4.3%。

### 3.2 十二市場住宅存量表

| 市場 | 住宅總數（年） | 30 年以上占比（或最接近代理） | 公寓 vs 透天／有地 | 平均樓地板面積 | 自有率 | 空屋率 | 來源 |
|---|---|---|---|---|---|---|---|
| 日本 | **6,505 萬戶（2023-10-01，含空屋）**；居住世帯あり 5,566.5 萬戶【官方】 | 1980 年以前建成（築 43 年以上）**1,181 萬戶，約 21%**，其中持ち家 866 萬戶；1981 年以後 4,386 萬戶（持ち家 2,665 萬）；**30 年以上占比無直接值** | 一戸建て 53%（2,933 萬）、共同住宅 45%（2,492 萬）（2023 概数）；東京都共同住宅 71.6% | 1 住宅當たり延べ面積 **90.86 m²**（一戸建て 126.32、共同住宅 50.31）（2023） | **持ち家住宅率 60.9%（2023）**；1993 年 59.8% | **13.8%（空屋 900 萬戶，歷史新高）**；「其他空屋」5.9% | [data-max](https://data-max.co.jp/article/70863)；[総務省 基本集計](https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf)；[国交省 データ集](https://www.mlit.go.jp/jutakukentiku/house/content/001857617.pdf)；[大和不動産鑑定 概数集計](https://daiwakantei.co.jp/wp/uploads/2024/05/2b82434b2bb8f09ae7298f31fddc5cfb.pdf)；[東京都 概要](https://www.toukei.metro.tokyo.lg.jp/jyutaku/2023/jt23tgaiyou.pdf)；[不動産流通推進センター 統計集](https://www.retpc.jp/wp-content/uploads/toukei/202303/202303_7jinko.pdf)；[money-bu-jpx](https://money-bu-jpx.com/news/article057251/) |
| 南韓 | **2,018 萬戶（2025 人口住宅總普查，2025-11-01 基準，2026-07 公布）**（+1.6%）【官方轉載】 | **30 年以上 618 萬戶（30.6%）**；公寓 30 年以上 295 萬戶（22.2%）、20 年以上 664 萬戶（49.9%）；R114：30 年以上公寓 2,606,823 戶（22%，2025-06） | 公寓 1,329 萬戶（**65.8%**） | 1 인당 주거면적 **36.0 m²**（2024 주거실태조사） | **자가보유율 61.4%、자가점유율 58.4%（2024）**；수도권 자가점유율 52.7%、고령가구 75.9% | 無資料（2025 普查빈집未取得） | [KDI 轉載 2025 普查](https://eiec.kdi.re.kr/policy/materialView.do?num=284799)；[KR-verification 重算](../verification/KR-verification.md)；[한국경제（R114）](https://www.hankyung.com/article/2025061796206)；[KDI 轉載 2024 주거실태조사](https://eiec.kdi.re.kr/policy/materialView.do?num=273475)；[파이낸셜뉴스](https://www.fnnews.com/news/202512110631344792)；[영남경제](https://www.ynenews.kr/news/articleView.html?idxno=71266) |
| 新加坡 | 無資料（HDB Key Statistics 2024/25 之「properties under management」表本輪無法讀取） | **代理：HIP 累計獲選 49.4 萬戶（1997 年以前建成組屋，占合資格九成）、已完成 38.1 萬戶**；2025 批次 29,000 戶／371 棟 | 居民人口住組屋 **76.0%**（FY2024/25）、住 HDB 售出組屋 73.0%；居民家戶住組屋 77.2%（DOS 轉述） | 無資料 | 組屋居民 **90% 自有**（HDB SR 2023/24）；全國自有率數值（DOS 2024）被鎖 | 私宅（不含 EC）**6.4%（2026Q2）**；CCR 10.3%（2025Q1） | [HDB Key Statistics 2024/25](https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf)；[HDB SR FY23](https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB-SR-FY23.pdf)；[99.co HIP](https://www.99.co/singapore/insider/hdb-home-improvement-programme-2025/)；[AsiaOne HIP 2025](https://www.asiaone.com/singapore/govt-allocates-over-407m-upgrading-works-29000-hdb-flats-home-improvement-programme)；[Global Property Guide SG](https://www.globalpropertyguide.com/asia/singapore/price-history)；[ERA 1Q2025 租務](https://www.era.com.sg/research-articles/1q-2025-rental-report)；[smartwealth（DOS）](https://smartwealth.sg/housing-household-statistics-singapore/) |
| 香港 | **3,047 千伙（2025-03：公營 1,328 千、私樓 1,719 千）**【官方】；2025 年底 3,106 千（公 1,344、私 1,762，+1.6%） | 私樓樓齡滿 30 年 **48%**（HK01 標題）／**64%**（HK-A 筆記引同文，2023）——同一來源兩數字，口徑待核 | 公營 43.6%：私樓 56.4%（2025-03，本人計算） | 無資料 | **自置居所住戶比率 50.9%（2025）**；2024 年 50.5%；歷史高 54.3%（2004） | 私樓 **4.3%（56,080 伙，2025 年底）**，其中 7,120 伙未獲滿意紙 | [Housing in Figures 2025](https://www.hb.gov.hk/eng/publications/housing/HIF2025.pdf)；[Global Property Guide HK（引 HK in Figures 2026）](https://www.globalpropertyguide.com/asia/hong-kong/price-history)；[TradingEconomics HK 自置率（C&SD）](https://tradingeconomics.com/hong-kong/home-ownership-rate)；[HK01 樓齡](https://www.hk01.com/%E7%A0%94%E6%95%B8%E6%89%80/1093926/%E5%85%A8%E6%B8%AF48-%E7%A7%81%E6%A8%93%E6%A8%93%E9%BD%A1%E6%BB%BF30%E5%B9%B4-%E9%9A%A8%E6%99%82%E8%A6%81%E5%BC%B7%E5%88%B6%E9%A9%97%E6%A8%93-%E6%96%B0%E4%BE%8B%E5%A2%9E%E6%B3%95%E5%9C%98%E6%8B%9B%E6%A8%99%E9%80%8F%E6%98%8E%E5%BA%A6)；[RVD 2026 初步統計](https://www.rvd.gov.hk/doc/tc/HKPR2026_Preliminary_Findings_TC.pdf) |
| 台灣 | 房屋稅籍住宅 **≈934–940 萬宅**【示意：914,196÷9.79%≈934 萬；5,545,854÷59%≈940 萬】 | **平均屋齡 34.1 年；30 年以上 5,545,854 宅（59%）（2025Q2）**；台北市 73.8%（39.1 年）；桃園 28.3 年最年輕；住宅買賣平均屋齡 31.7 年（2025Q4） | 無全國資料；宜蘭交易：電梯大樓 43.5% vs 透天 38.6% | 無資料 | **84.4%（2024）→ 83.95%（2025，16 年新低）**；租屋 7.62% | **9.79%（914,196 宅，2024 下半年，歷年新高）**；5 年內新屋 22.91%、50 年以上 12.54%、20 坪以下 18.16%；台北 7.09%、新北 7.45% 最低 | [Newtalk 2025-09-17](https://newtalk.tw/news/view/2025-09-17/994199)；[工商時報](https://www.ctee.com.tw/news/20250917701015-430604)；[Newtalk 台北](https://newtalk.tw/news/view/2025-09-23/995218)；[聯合 買賣屋齡](https://udn.com/news/story/7241/9542785)；[經濟日報 空屋](https://money.udn.com/money/story/5621/8909453)；[主計總處 113 年家庭收支調查](https://ws.dgbas.gov.tw/001/Upload/466/ebook/ebook_341889/pdf/full.pdf)；[經濟日報 自有率](https://money.udn.com/money/story/5621/9708202)；[myhousing 宜蘭](https://www.myhousing.com.tw/n/n02/n0203/n020301/269746/) |
| 中國大陸 | 城鎮住房 **3.74 億套**、城鎮存量 335.5 億 m²（2023，任澤平）；七普存量住宅建面 517.22 億 m²（城鎮 294.6） | **2000 年前建成約 35%（戶數，七普推算）**；上海 50.38%（全國最高）；另一口徑 28%（澎湃，口徑不明） | 無資料 | 無資料（本輪） | 無資料 | 無資料 | [搜狐《中國住房存量報告 2026》](https://www.sohu.com/a/1032443179_120179484)；[華泰 PDF](https://reportify-1252068037.cos.ap-beijing.myqcloud.com/media/production/s_2d023dd8_2d023dd8457c351583068e0e7510101b.pdf)；[騰訊（人口普查年鑑）](https://news.qq.com/rain/a/20220628A0BO3R00)；[CN-verification](../verification/CN-verification.md) |
| 馬來西亞 | **1,090 萬戶（2025，DOSM；2020 年 960 萬，年均 +2.5%）**；雪蘭莪 250 萬戶最多 | 無資料（無官方屋齡統計） | **有地／透天 73.1%、高樓 22.8%、其他 4.1%** | 無資料 | **78.0%（2024，Ken 引 DOSM）** | 無資料；代理：住宅 overhang 32,801 戶（2026Q1） | [FMT 轉述 DOSM](https://www.freemalaysiatoday.com/category/nation/2026/04/23/malaysian-housing-units-reached-10-9mil-in-2025-says-statistics-dept)；[Ken Research](https://www.kenresearch.com/industry-reports/malaysia-home-improvement-market)；[IQI NAPIC Q1 2026](https://iqiglobal.com/blog/napic-q1-2026/) |
| 泰國 | 無資料（全國總數） | 無資料；代理：屋齡 ≥10 年住宅 **>2,340 萬戶**（≈2024） | 無資料 | 無資料 | 無資料 | 全國空屋 **164 萬戶**（AREA）；大曼谷住宅 **639 萬戶**（AREA 2025 調查） | [Bangkokbiznews](https://www.bangkokbiznews.com/property/1124831)；[Thansettakij 空屋](https://www.thansettakij.com/real-estate/642986)；[TNews（AREA）](https://www.tnews.co.th/social/social-news/637990) |
| 越南 | 無資料 | 無資料（河內舊公寓重建同意門檻降至 51%，代理訊號） | 無資料 | 無資料 | 無資料 | 無資料 | [Người Quan Sát](https://nguoiquansat.vn/ha-noi-trao-quyen-cho-cac-chu-nha-duoc-tu-de-xuat-cai-tao-chung-cu-cu-298599.html) |
| 印尼 | 無資料（總數）；**住房所有權缺口（backlog 1）929 萬戶（12.39%，2026-03 Susenas；2025 年 964 萬／13%）**；不適居（backlog 2）1,801 萬戶（24.03%） | 無資料 | FLPP 2025 放款 99.99% 為透天（rumah tapak） | 無資料 | **85.07%（2025，Susenas）**；都市 79.63%、鄉村 92.97% | 無資料 | [Tirto（BPS）](https://tirto.id/bps-jumlah-backlog-perumahan-capai-929-juta-rumah-tangga-hBfe)；[Kompas](https://www.kompas.com/properti/read/2026/08/13/205642221/backlog-rumah-turun-350000-keluarga-dalam-setahun-tersisa-929-juta)；[Journalarta](https://journalarta.com/news/2026/08/14/sembilan-juta-keluarga-belum-punya-rumah-18-juta-belum-tinggal-di-rumah-layak/)；[BPS 自有住宅表](https://www.bps.go.id/id/statistics-table/2/ODQ5IzI=/persentase-rumah-tangga-menurut-provinsi-dan-status-kepemilikan-bangunan-tempat-tinggal-yang-ditempati-milik-sendiri.html)；[Media Indonesia FLPP](https://mediaindonesia.com/ekonomi/845538/penyaluran-flpp-2025-cetak-rekor-tertinggi-tembus-278868-unit-rumah) |
| 菲律賓 | **≈2,850 萬住宅單位，其中 2,520 萬有人居住（2020 普查）**；家戶 26,376,522、每 100 單位 105 戶 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料；住房缺口 650 萬戶（UN-Habitat 2022）vs DHSUD 220 萬戶 | [BusinessWorld（PSA）](https://www.bworldonline.com/special-features/2024/10/24/630972/building-better-affordable-housing-for-filipino-families/)；[PSA 2020 CPH](https://psa.gov.ph/content/housing-characteristics-philippines-2020-census-population-and-housing)；[BusinessMirror](https://businessmirror.com.ph/2025/11/04/phls-housing-crisis-6-5-million-reasons-for-radical-action-now/)；[UN-Habitat PH brief](https://www.habitat.org/sites/default/files/documents/Philippines%20policy%20brief_UPDATED_20231108_0.pdf) |
| 印度 | 無資料（2011 普查過舊，2021 普查未辦） | 無資料 | 無資料 | 無資料 | 無資料 | 無資料；代理：七大城未售 ≈63.1 萬戶（2026Q3） | [Storyboard18（Anarock）](https://www.storyboard18.com/amp/how-it-works/mmr-bengaluru-drive-q3-housing-sales-as-it-grows-10-qoq-3-yoy-anarock-ws-lo-111529.htm) |

### 3.3 Cited Findings
- 日本 2023 年住宅總數 6,505 萬戶、空屋 900 萬戶（13.8%，歷史新高）— [data-max](https://data-max.co.jp/article/70863)；1980 年以前建成且有人居住 1,181 萬戶（約 21%）、其中持ち家 866 萬戶 — [国交省 住宅のあるべき姿 データ集](https://www.mlit.go.jp/jutakukentiku/house/content/001857617.pdf)；持ち家住宅率 60.9% — [money-bu-jpx](https://money-bu-jpx.com/news/article057251/)；一戸建て 53%／共同住宅 45% — [大和不動産鑑定](https://daiwakantei.co.jp/wp/uploads/2024/05/2b82434b2bb8f09ae7298f31fddc5cfb.pdf)。
- 南韓 2025 普查：總住宅 2,018 萬、公寓 1,329 萬（65.8%）、30 年以上 618 萬（30.6%）— [KDI 轉載](https://eiec.kdi.re.kr/policy/materialView.do?num=284799)（KR-verification 逐項重算成立）；2024 주거실태조사：자가보유율 61.4%、자가점유율 58.4%、1 인당 36.0 m²；청년 자가점유율 12.2%、신혼 43.9% — [KDI 轉載](https://eiec.kdi.re.kr/policy/materialView.do?num=273475)；[파이낸셜뉴스](https://www.fnnews.com/news/202512110631344792)。
- 香港 2025-03 存量 3,047 千伙（公 1,328／私 1,719）— [Housing in Figures 2025](https://www.hb.gov.hk/eng/publications/housing/HIF2025.pdf)；自置居所比率 50.9%（2025）— [TradingEconomics（C&SD）](https://tradingeconomics.com/hong-kong/home-ownership-rate)；私樓空置 4.3% — [RVD 2026](https://www.rvd.gov.hk/doc/tc/HKPR2026_Preliminary_Findings_TC.pdf)。
- 台灣 30 年以上 5,545,854 宅（59%）、平均 34.1 年 — [Newtalk](https://newtalk.tw/news/view/2025-09-17/994199)；低度使用住宅 914,196 宅（9.79%）— [經濟日報](https://money.udn.com/money/story/5621/8909453)；自有率 84.4%（2024）— [主計總處](https://ws.dgbas.gov.tw/001/Upload/466/ebook/ebook_341889/pdf/full.pdf)；83.95%（2025）— [經濟日報](https://money.udn.com/money/story/5621/9708202)。
- 印尼 backlog 929 萬戶（12.39%）、backlog 2 1,801 萬戶 — [Tirto](https://tirto.id/bps-jumlah-backlog-perumahan-capai-929-juta-rumah-tangga-hBfe)；[Journalarta](https://journalarta.com/news/2026/08/14/sembilan-juta-keluarga-belum-punya-rumah-18-juta-belum-tinggal-di-rumah-layak/)；自有 85.07% — [BPS 表](https://www.bps.go.id/id/statistics-table/2/ODQ5IzI=/persentase-rumah-tangga-menurut-provinsi-dan-status-kepemilikan-bangunan-tempat-tinggal-yang-ditempati-milik-sendiri.html)（搜尋摘要引述，未開啟原表）。
- 菲律賓 2020 普查住宅單位約 2,850 萬、有人居住 2,520 萬 — [BusinessWorld](https://www.bworldonline.com/special-features/2024/10/24/630972/building-better-affordable-housing-for-filipino-families/)；住房缺口 650 萬（UN-Habitat）vs DHSUD 220 萬 — [BusinessMirror](https://businessmirror.com.ph/2025/11/04/phls-housing-crisis-6-5-million-reasons-for-radical-action-now/)。

### 3.4 Inferences
- 「屋齡 × 自有率」決定翻修的付費者：台灣（59% 老屋 × 84% 自有）與日本（21% 築 43 年以上且 73% 為自有）翻修決策者就是屋主本人；香港（自置率僅 50.9%、公營占 43.6%）與新加坡（組屋 76% 人口）則有近半需求由房東或政府（HIP）決定，B2G／B2B 比重高。
- 台灣「5 年內新屋空屋率 22.91%」與「30 年以上 59%」並存，意味交屋裝修（新屋）與老屋翻新兩條線同時存在，但新屋端有相當比例延後裝修。

### 3.5 Gaps
- 日本 30 年以上（1995 年以前建成）占比；南韓 2025 普查空屋；新加坡 HDB 組屋總數與全國自有率精確值、私宅平均面積；香港 48% vs 64% 口徑；台灣全國公寓 vs 透天比、平均坪數；中國自有率與空置率；馬來西亞、泰國、越南、印尼、菲律賓、印度之屋齡分布、平均面積；泰國、越南、菲律賓、印度自有率；越南住宅總數。

---

## 4. 交易與新供給（Q3：Transactions, new supply, price cycle, policy）

### 4.1 Takeaway
2025 年住宅交易量：中國 30 城二手 174 萬套（全國二手占比 2026H1 50.4%）、南韓 726,111 件（+13.0%）、越南 579,718 筆（+7.7%，含土地）、泰國 316,214 戶（−9.1%）、馬來西亞住宅約 25.6 萬宗（全物業 416,413 宗）、台灣 261,308 棟（−25.5%）、香港 62,832 宗（二手私宅 39,821）、新加坡 HDB 轉售 26,169 ＋私宅 26,492。新供給：日本著工 740,667 戶（62 年最低）、南韓完工約 30 萬戶（−33%）、台灣住宅使照約 14.3 萬宅（新高）、馬來西亞完工 99,877 戶、越南商品房完工 29,901＋社宅 102,633 戶、印度七大城 2026Q3 推案 114,320 戶。2026 年循環位置：香港、南韓（價格回升＋政策緊縮）、日本（升息）、中國（量縮價跌、二手主導）、台灣（量縮、管制微鬆）、泰國（政策刺激反彈）、馬來西亞（滯銷攀升）、印尼（降溫、升息）、印度（價升、庫存升）、越南（量升價漲、利率高）。

### 4.2 十二市場交易與新供給表

| 市場 | 住宅交易（新 vs 中古） | 新完工／推案 2023–2025 | 價格指數與 2026 循環位置 | 未售庫存 | 政策干預（2024–2026） | 來源 |
|---|---|---|---|---|---|---|
| 日本 | 首都圈 2024：中古公寓成約 **37,222 件（+3.4%）** vs 新建分讓供給約 2.3 萬戶（連 3 年 <3 萬），中古超越新建差距 14,219 戶創紀錄；2025Q1 中古 12,385 件（+25.5%） | 新設住宅著工 **740,667 戶（2025 曆年，−6.5%，3 年連減，1963 年以來最低）**；2025 年度 711,171 戶（−12.9%） | 新建價格高漲推升中古競爭力；**日銀 2026-09-18 升息至 1.25%**（1995 年以來最高，6 月後 3 個月再升），變動型房貸多在 2027-04 基準利率改定反映 | 無資料 | 無資料（住宅交易面無新管制；補助見 §6） | [DIME](https://dime.jp/genre/1990629/)；[arc-navi 2025 暦年](https://www.arc-navi.shikaku.co.jp/column/details.php?column_id=5205)；[BuildApp（国交省）](https://news.build-app.jp/article/39533/)；[arc-navi 2025 年度](https://www.arc-navi.shikaku.co.jp/column/details.php?column_id=5887)；[NHK 日銀](https://news.web.nhk/newsweb/na/nd-20260918de50968)；[第一生命経済研究所](https://www.dlri.co.jp/report/macro/665928.html)；[モゲチェック](https://mogecheck.jp/articles/show/pnl6ZzOV4BDR2k5Ra7PY) |
| 南韓 | 住宅買賣 **726,111 件（2025，+13.0%）**；12 月 62,893 件（+37.0%）；公寓實價登錄 503,562 件（+14.4%）；新／中古分拆無官方值 | 完工 **約 30 萬戶（2025 確定值；2024 年 44.9 萬）**；許可 −35.5%、開工約 27 萬戶 | 2025 年 6 月單月買賣逾 7 萬件（44 個月新高）；**韓銀 2026-07-16 2.50→2.75%、08-27 →3.00%**；銀行新承做房貸 **4.66%（2026-08，3 年 9 個月最高；固定 4.88%／變動 4.53%）** | 미분양 **69,134 戶（2026-08 末，+1.3% m/m；首都圈 19,136、地方 49,998）**；2025-09 66,762 | **6·27 대책（2025）**：規制地域無住宅者 LTV 70→40%；**10·15 대책（2025-10-15）**：房貸上限 ≤15 億 6 億、15–25 億 4 億、>25 億 2 億韓元（≈USD 43／29／14 萬）、壓力利率下限 3.0%、2 年實居義務；2025Q4 銀行房貸增幅由 10.9 兆降至 4.8 兆韓元 | [M이코노미（국토부）](https://www.m-economynews.com/news/article.html?no=64226)；[네이트（부동산플래닛）](https://m.news.nate.com/view/20260212n44377)；[헤럴드경제](https://biz.heraldcorp.com/article/10887737)；[한국금융신문 금통위](https://www.fntimes.com/html/view.php?ud=202608271107018117179ad43907_18)；[한국일보 주담대](https://www.hankookilbo.com/news/article/A2026093010490005879)；[뉴데일리 미분양](https://biz.newdaily.co.kr/site/data/html/2026/09/30/2026093000005.html)；[뉴스핌 10·15](https://www.newspim.com/news/view/20251015000279)；[경향 10·15](https://www.khan.co.kr/article/202510151656001)；[머니투데이](https://www.mt.co.kr/economy/2026/02/24/2026022411382531015) |
| 新加坡 | HDB 轉售 **26,169 筆（2025，−9.7%；Q4 5,256 筆為五年低）**；私宅全年交易 26,492 戶、新售 10,611（2024：6,469）；Q3／Q4 轉售（非有地）2,762／2,393 | BTO 推出 19,723（2025）、19,600（2026）；私宅完工 **6,123 戶（2025，不含 EC；2024：8,460）**；未來數年管線 5.56–5.7 萬戶 | HDB 轉售價 **+2.9%（2025；2024 +9.7%）**，2019 年以來最慢；私宅空置率升至 6.4%（2026Q2） | 私宅未售 **16,193 戶（2025Q4，−5.2% q/q）** | 無資料（2025 年降溫措施本輪未取得 URL，列缺口） | [EdgeProp HDB](https://www.edgeprop.sg/property-news/hdb-resale-prices-plateaued-4q2025-transactions-sink-five-year-low)；[EdgeProp BTO](https://www.edgeprop.sg/property-news/hdb-supplying-19600-bto-flats-2026-spread-over-three-sales-exercises)；[ERA 4Q2025](https://www.era.com.sg/research-articles/4q-2025-ura-private-quarterly-report)；[URA 2Q2025](https://www.ura.gov.sg/news/media/pr25-40/)；[Global Property Guide SG](https://www.globalpropertyguide.com/asia/singapore/price-history) |
| 香港 | 住宅買賣登記 **62,832 宗／HK$5,198.3 億（≈USD 666 億／NT$2.10 兆）（2025）**；**一手 20,525 宗（HK$2,255.5 億）、二手 39,821 宗（HK$2,919.3 億）→ 二手占 66%**；整體樓宇 80,702 宗（2024：67,979）；2026 年預測 8.8 萬宗（一手 1.9 萬、二手 4.6 萬） | 私樓落成 **19,370 伙（2025）** | **撤辣 2024-02-28**；CCL 2025 年 +4.7%、2026Q1 +5.59%；CCL **160.1（2026-10-02）**；差估署售價指數 2026-03 312.8（連漲 10 個月）；1M HIBOR 2.63–2.88%、H 按約 3.25%（2026-08／09） | 私樓空置 56,080 伙（4.3%） | 撤辣（2024-02）；無新管制 | [香港經濟日報（中原 9 月分析）](https://ps.hket.com/article/4204187/%E4%B8%AD%E5%8E%9F%EF%BC%9A9%E6%9C%88%E6%95%B4%E9%AB%94%E8%B2%B7%E8%B3%A3%E5%AE%97%E6%95%B8%E5%9B%9E%E5%8D%87%E9%80%BE1%E6%88%90%C2%A0%C2%A0%E4%B8%80%E6%89%8B%E7%A7%81%E6%A8%93%E9%87%8D%E4%B8%8A%E9%80%BE%E5%8D%83%E5%AE%97)；[中原 研究報告索引](https://hk.centanet.com/info/property-news/%E7%A0%94%E7%A9%B6%E5%A0%B1%E5%91%8A/land-registry)；[土地註冊處 一手及二手](https://www.landreg.gov.hk/tc/monthly/agt-primary.htm)；[中原 CCI](https://hk.centanet.com/CCI/index)；[am730 差估署](https://www.am730.com.hk/%E5%9C%B0%E7%94%A2/1027430/%E6%A8%93%E5%83%B9%E6%8C%87%E6%95%B8-%E9%80%A3%E6%BC%B210%E5%80%8B%E6%9C%88%E5%89%B5%E9%80%BE7%E5%B9%B4%E5%8D%8A%E6%9C%80%E9%95%B7%E5%8D%87%E6%B5%AA-%E4%B8%AD%E5%8E%9F-%E7%A7%9F%E9%87%91%E5%8F%8A%E6%A8%93%E5%83%B9%E6%96%BC%E6%AC%A1%E5%AD%A3%E5%8D%87%E5%8B%A2%E6%8C%81%E7%BA%8C)；[OneDegree 撤辣](https://www.onedegree.hk/zh-hk/blog/home-buyers-tips/hong-kong-property-market-trends)；[RVD 2026](https://www.rvd.gov.hk/doc/tc/HKPR2026_Preliminary_Findings_TC.pdf)；[wuchatprop HIBOR](https://www.wuchatprop.com.hk/hibor/) |
| 台灣 | 建物買賣移轉 **261,308 棟（2025，−25.5%，近 9 年新低）**；移轉登記總數 450,983 棟（買賣 57.9%、繼承 17.4%、贈與 11.7%）；預售 2025H1 約 2 萬件（−73%）；新／中古無官方分拆，代理：屋齡 3 年以下新屋房貸件數占 **50.3%（2025；2021 年 32.4%）** | 住宅使照 **≈143,000 宅（2025，1997 年以來新高；2024 年 138,180）**；建物第一次登記 177,000 棟（25 年新高）；預售完工待交屋約 54 萬戶（2025–2027，低信心） | 五大銀行新承做房貸利率 **≈2.29%（2026-07）**（另有 2.322%／2026-05、2.303% 之說）；2026Q1 五大銀行新增房貸年減逾 26% | 待售新成屋 2024Q4 首破 11 萬宅 | **第七波信用管制（2024-09）**後成屋 −30%、預售 −70%；**2026-03-20 第二戶成數 5→6 成**；**2026Q3 理監事會再升至 7 成**（會議日 17／19 日各說不一）；第三戶以上維持 3 成；**青安 3.0 2026-08-01 起（前 3 年 1.775%）** | [中央社（內政部）](https://www.cna.com.tw/news/aipl/202606200029.aspx)；[經濟日報 使照](https://money.udn.com/money/story/5621/9324984)；[科技新報](https://finance.technews.tw/2026/06/25/taiwan-housing-market-more-houses-built-fewer-buyers-25-5-decline-nine-year-low/)；[聯合（信義）](https://udn.com/news/story/7241/9288854)；[經濟日報 預售](https://money.udn.com/money/story/5621/9028566)；[經濟日報 新屋申貸](https://udn.com/news/story/7241/9431371)；[工商時報 信用管制](https://www.ctee.com.tw/news/20250725700833-430601)；[money101（央行統計）](https://www.money101.com.tw/blog/%E6%88%BF%E8%B2%B8%E5%88%A9%E7%8E%87)；[經濟日報 五大銀行](https://money.udn.com/money/story/122376/9518079)；[Yahoo Q1 房貸](https://tw.stock.yahoo.com/news/q1%E4%BA%94%E5%A4%A7%E9%8A%80%E8%A1%8C%E6%96%B0%E5%A2%9E%E6%88%BF%E8%B2%B8%E5%89%B5%E8%BF%913%E5%B9%B4%E5%90%8C%E6%9C%9F%E6%96%B0%E4%BD%8E-%E5%B9%B4%E6%B8%9B%E9%80%BE26-001600614.html)；[FWA 待售新成屋](https://fwnews.com.tw/%E5%85%A7%E6%94%BF%E9%83%A8%E6%9C%80%E6%96%B0%E7%B5%B1%E8%A8%88%E5%87%BA%E7%88%90%E5%8E%BB%E5%B9%B4%E7%AC%AC4%E5%AD%A3%E5%BE%85%E5%94%AE%E6%96%B0%E6%88%90%E5%B1%8B%E9%A6%96%E5%BA%A6%E7%AA%81%E7%A0%B41/)；[房感 青安 3.0](https://www.housefeel.com.tw/article/%E9%9D%92%E5%B9%B4-%E9%A6%96%E8%B3%BC-%E8%B2%B8%E6%AC%BE-%E8%B3%BC%E5%B1%8B%E8%B2%B8%E6%AC%BE-%E5%AE%89%E5%BF%83%E6%88%90%E5%AE%B6%E8%B2%B8%E6%AC%BE/) |
| 中國大陸 | **2026H1 二手房占新房＋二手交易 50.4%（住建部；18 省二手面積超新房）；1–8 月 52.4%**；30 城二手 2025 年約 174 萬套（占 65%）；北京 2026H1 二手網簽 93,583 套；廣州二手占比 >60%、成都近 80% | 2025 年住宅竣工 −20.2%；2026 年 1–6 月新建商品房銷售面積 **4.01 億 m²（−11.6%）**、銷售額 3.79 兆元（−13.6%） | 住建部 2026-09 定調「存量時代」；國家統計局 2026-09-15 首次公布二手房網簽面積 | 商品房待售 **7.63 億 m²（2026-06 末，−0.9%，連 4 個月年減）**；貝殼二手掛牌 650 萬套（2025-12） | 限購放鬆細節本輪未取得；2026 年國補將家裝移出 | [21 財經（住建部）](https://m.21jingji.com/article/20260729/herald/df3b446d915832c3dab62856c9bf0024.html)；[新京報](https://m.bjnews.com.cn/detail/1790671605169302.html)；[網易（統計局）](https://www.163.com/dy/article/L1SOIAQS05159A0N.html)；[深圳房地產信息網（中指）](http://news.szhome.com/394159.html)；[騰訊 北京](https://news.qq.com/rain/a/20260924A0ELOT00)；[騰訊 住建部](https://news.qq.com/rain/a/20260920A08VNC00)；[國家統計局 2025](https://www.stats.gov.cn/sj/zxfb/202601/t20260119_1962324.html)；[東方財富（中指）](https://finance.eastmoney.com/a/202601043607773770.html)；[新浪 掛牌](https://finance.sina.com.cn/roll/2025-12-16/doc-inhaymzi1128022.shtml)；[新華網 國補](https://www.news.cn/politics/20260102/8280c1156) |
| 馬來西亞 | 全物業 **416,413 宗（2025，−1%）／RM 2,418.7 億（+4.1%；≈USD 550 億／NT$1.73 兆）**；住宅占量 61.6%（≈25.6 萬宗【示意】）、占值 44.8%；住宅量 −1.5%、值 +1.3% | 住宅完工 **99,877 戶（2025）**、開工 82,097、規劃 75,370；柔佛 2025–26 新增 11.5 萬戶 | HPI **+2.6%（2025）**、均價 RM 502,922；2025Q3 指數 −1.46% q/q（2021 年以來首季減）；OPR 2.75%（2025-07 起） | 住宅 overhang **30,471 戶（2025Q4，+31.6%）→ 32,801 戶（2026Q1，+39.5%）**，連六季升 | 房貸核准率 39.2%（2026 年 1–4 月） | [Hartamas（NAPIC）](https://hartamas.com/malaysia-property-market-2025-what-the-napic-data-really-shows/)；[iProperty](https://www.iproperty.com.my/guides/2025-malaysia-property-market-what-buyers-and-sellers-really-pay-pjx-101924)；[Propplace](https://www.propplace.my/guides/malaysia-property-market-2025-overview)；[Global Property Guide MY](https://www.globalpropertyguide.com/asia/malaysia/price-history)；[IQI Q1 2026](https://iqiglobal.com/blog/napic-q1-2026/)；[Threads（PMR 2025）](https://www.threads.com/@malaysiauncapped/post/DWWc8eDkT8b/)；[EdgeProp 柔佛](https://www.edgeprop.my/content/1917690/johor-adds-115000-homes-meet-demand-fuelled-industrial-rts-js-sez)；[Paultan OPR](https://paultan.org/2026/09/04/bank-negara-opr-sept-2026-mpc-meeting/) |
| 泰國 | 住宅移轉 **316,214 戶（2025，−9.1%；新屋 −13.9%、中古 −6.2%）**；中古占 **64%（2025 底）／67%（2026Q1，48,446 戶）**；**2026H1 167,665 戶（+17.6%）／THB 4,298 億（≈USD 130 億／NT$4,103 億）** | 大曼谷新公寓推案 THB 772 億（2025，−41%）；新推案 23 年最低 | 2026H1 低層 +14.6%、公寓 +24.1%；建材價格指數 2026-04 +5.9% | 大曼谷未售公寓 **≈35 萬戶（需 5–6 年去化，Knight Frank）** | **LTV 100% 延至 2027-06-30**（<10M 第 2 戶起、≥10M 第 1 戶起）；**移轉／抵押費 0.01%（≤THB 7M）延至 2027-06-30** | [LINE Today（REIC）](https://today.line.me/th/v3/article/2D7qOkO)；[Bangkok Post 中古](https://www.bangkokpost.com/property/3266023/resale-homes-take-larger-market-share)；[REIC 277](https://reic.or.th/Activities/PressRelease/277)；[The Thai Press](https://www.thethaipress.com/2026/169482)；[Bangkok Post 推案](https://www.bangkokpost.com/property/3217494/cautious-developers-to-cut-bangkok-housing-launches)；[Amarin 23 年最低](https://www.amarintv.com/spotlight/economy/520502)；[The Nation（KF）](https://www.nationthailand.com/business/property/40067333)；[Thansettakij LTV](https://www.thansettakij.com/economy/659052)；[Thansettakij 條件](https://www.thansettakij.com/real-estate/662824)；[Khaosod](https://www.khaosod.co.th/economics/news_10244535) |
| 越南 | 成交 **579,718 筆（2025，+7.7%）：土地 441,693、公寓＋獨立屋 138,025**；2025Q4 151,382 筆（+35% y/y）；VARS：新推案約 12.8 萬戶（+88%）、成交約 8.8 萬戶；>75% 買家已有一戶 | 商品住宅完工 **88 案／29,901 戶**；社會住宅 **102,633 戶（2025）**、2026 目標 >11 萬 | 河內、胡志明公寓價 2025 年 +20–30%；房貸優惠 8–10% → 浮動 13–15%（2026） | 專案庫存 **32,894 戶／地（2025Q4，僅 24/34 省；公寓 10,952、獨立屋 9,810、土地 12,132）**，公寓庫存 q/q +24% | 《土地法》2024（Luật Đất đai 2024）生效日本輪未經搜尋確認（列缺口）；2026-07-01 起 35 歲以下社宅貸款 6.5% | [Tạp chí Kinh tế Tài chính（Bộ Xây dựng）](https://tapchikinhtetaichinh.vn/thi-truong-bat-dong-san-quy-iv-va-ca-nam-2025-nguon-cung-tang-giao-dich-soi-dong-140788.html)；[Báo Xây dựng](https://batdongsan.baoxaydung.vn/thi-truong-bat-dong-san-nam-2025-nguon-cung-cai-thien-gia-van-neo-cao-19226011619375156.htm)；[Vietstock 庫存](https://vietstock.vn/2026/02/ton-kho-bat-dong-san-vuot-500-ngan-ty-737-1403221.htm)；[Dân trí](https://dantri.com.vn/bat-dong-san/bo-xay-dung-thua-nhan-gia-chung-cu-tang-nhanh-va-cao-20260117235004079.htm)；[Báo Chính phủ 完工](https://baochinhphu.vn/nguon-cung-tang-gia-nha-chua-giam-102260117005432583.htm)；[Báo Phú Thọ 社宅](https://baophutho.vn/ca-nuoc-hoan-thanh-102-633-can-nha-o-xa-hoi-vuot-2-pha-ke-hoach-244359.htm)；[Vietstock VARS](https://vietstock.vn/2026/03/vars-ire-nhieu-nha-dau-tu-bat-dong-san-tang-gap-doi-tai-san-chi-trong-1-2-nam-4220-1415575.htm)；[Người Đô Thị](https://nguoidothi.net.vn/gia-chung-cu-tai-ha-noi-va-tp-hcm-tang-toi-hon-20-30-trong-nam-2025-51374.html)；[Smartland 利率](https://smartland.vn/lai-suat-vay-mua-nha-2026/)；[LuatVietnam 6.5%](https://luatvietnam.vn/tin-van-ban-moi/chinh-thuc-ap-dung-lai-suat-65-nam-cho-nguoi-duoi-35-tuoi-vay-mua-nha-o-xa-hoi-tu-01-7-2026-186-109829-article.html) |
| 印尼 | 無全國交易統計；一級市場銷售 **2026Q1 −25.67% y/y**；購屋者 69.87% 使用房貸 | FLPP 補貼房貸 **278,868 戶／Rp 34.64 兆（2025，≈USD 21.7 億／NT$682 億）**；「三百萬住宅」累計 324,213 戶（至 2026-06-13） | 一級市場房價指數 **+0.83%（2025Q4，2003 年調查以來最低）→ +0.62%（2026Q1）**；**BI Rate 2026-05／06 升至 5.75%，7–9 月維持** | 無資料 | 配額 FLPP 35 萬戶；無交易面管制 | [BI 2026Q1](https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_289726.aspx)；[BI 2025Q4](https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_283226.aspx)；[Media Indonesia](https://mediaindonesia.com/ekonomi/845538/penyaluran-flpp-2025-cetak-rekor-tertinggi-tembus-278868-unit-rumah)；[Periskop](https://periskop.id/ekonomi/20260617/realisasi-program-3-juta-rumah-capai-324213-unit-pengembang-jadi-motor-utama)；[Bisnis BI Rate](https://finansial.bisnis.com/read/20260923/11/2006538/alasan-bank-indonesia-tahan-bi-rate-september-2026-di-575)；[detik](https://finance.detik.com/moneter/d-8536995/bi-rate-naik-lagi-jadi-5-75) |
| 菲律賓 | 無全國交易統計；代理：Pag-IBIG 房貸 **PHP 1,405.4 億（2025，+8%；≈USD 24.7 億／NT$777 億）、90,727 戶**（目標 PHP 1,568.6 億／111,648 戶未達） | 4PH 社會住宅 7,056 戶（PHP 76.3 億，利率 3%）；4,811 戶 @4.5% | 無資料 | 無資料 | 4PH 計畫目標年 100 萬戶 | [Manila Standard](https://manilastandard.net/business/314693903/pag-ibig-housing-loans-rose-8-to-record-p140-54-billion-in-2025.html)；[PNA](https://www.pna.gov.ph/articles/1267430)；[PIA](https://pia.gov.ph/gender-and-development/pag-ibig-fund-releases-p64-34-b-dividends-finances-p140-54b-housing-loans/)；[Philstar 目標](https://www.philstar.com/business/2025/04/05/2433551/pag-ibig-release-p157-billion-housing-loans-year) |
| 印度 | 七大城銷售 **100,220 戶（2026Q3，+3% y/y；Q2 90,715）**；MMR 31,750、Bengaluru 16,670；2025 全年值本輪無 URL | 七大城推案 **114,320 戶（2026Q3，+18%）** | 七大城均價 **+7% y/y（2026Q3）**；房貸最低 7.00–7.35%（2026-10）；RBI 2026-10-07 據報升息 25bp 至 5.50%（單一來源，待核） | 未售 **≈6.31 lakh（63.1 萬戶，2026Q3，+12% y/y；Q2 616,500）** | 無交易面管制 | [Storyboard18](https://www.storyboard18.com/amp/how-it-works/mmr-bengaluru-drive-q3-housing-sales-as-it-grows-10-qoq-3-yoy-anarock-ws-lo-111529.htm)；[Outlook Money](https://www.outlookmoney.com/amp/story/invest/housing-market-sees-modest-sales-growth-in-q3-as-launches-jump-18-per-cent)；[Grihik](https://www.grihik.com/news/financial/india-housing-sales-rise-3-in-q3-2026-to-100-220-units)；[Upstox 房貸](https://upstox.com/news/personal-finance/latest-updates/cheapest-home-loan-rates-in-october-2026-12-lenders-offer-7-1-7-35-interest-emi-revisions-may-follow/article-201440/)；[UrbanMoney SBI](https://www.urbanmoney.com/home-loan/state-bank-of-india/interest-rate) |

### 4.3 Cited Findings（補充）
- 香港 2025 年住宅買賣 62,832 宗、一手 20,525、二手 39,821（中原引土地註冊處；2026 年首 9 個月住宅 54,052 宗已達 2025 全年 86%）— [hket](https://ps.hket.com/article/4204187/%E4%B8%AD%E5%8E%9F%EF%BC%9A9%E6%9C%88%E6%95%B4%E9%AB%94%E8%B2%B7%E8%B3%A3%E5%AE%97%E6%95%B8%E5%9B%9E%E5%8D%87%E9%80%BE1%E6%88%90%C2%A0%C2%A0%E4%B8%80%E6%89%8B%E7%A7%81%E6%A8%93%E9%87%8D%E4%B8%8A%E9%80%BE%E5%8D%83%E5%AE%97)。土地註冊處住宅統計不含居屋等資助房屋 — [Land Registry](https://www.landreg.gov.hk/tc/monthly/agt-primary.htm)。
- 中國 2026H1 二手占比 50.4% 之發布方為住建部，國家統計局同期僅引「有關部門數據」；一篇虎嗅文章誤標為 2024 年，不採 — [21 財經](https://m.21jingji.com/article/20260729/herald/df3b446d915832c3dab62856c9bf0024.html)；[網易](https://www.163.com/dy/article/L1SOIAQS05159A0N.html)。
- 馬來西亞 HPI 指數水準兩來源不一（233.1 vs 218.4），但 +2.6% 與均價 RM 502,922 一致 — [Global Property Guide](https://www.globalpropertyguide.com/asia/malaysia/price-history)；[Hartamas](https://hartamas.com/malaysia-property-market-2025-what-the-napic-data-really-shows/)。
- 越南庫存 32,894 僅涵蓋 24/34 省，實際更高 — [Vietstock](https://vietstock.vn/2026/02/ton-kho-bat-dong-san-vuot-500-ngan-ty-737-1403221.htm)。
- 台灣央行第二戶成數調整：2026-03-20 起 5→6 成；第三季理監事會再升至 7 成（報導會議日 17 日／19 日不一）— [money101](https://www.money101.com.tw/blog/%E6%88%BF%E8%B2%B8%E5%88%A9%E7%8E%87)；[經濟日報](https://money.udn.com/money/story/122376/9518079)；[旺得富（央行）](https://wantrich.chinatimes.com/news/20260422900804-420501)。

### 4.4 Inferences
- 「中古占比」已是東亞共同趨勢（香港 66%、泰國 64–67%、日本首都圈 >60%、中國 50.4%、台灣約 50%），翻修需求的觸發點從「交屋」轉為「換手」，裝修業者的獲客通路須與仲介／按揭端綁定（香港中原按揭 × 好師傅、馬來西亞 RHB × Makeover Guys 即為例證，見 §6）。
- 日、韓升息與 10·15／6·27 式信貸限額，會先壓抑換手量再壓抑翻修；台灣信用管制微鬆（第二戶 7 成）與青安 3.0 則偏向支撐首購新屋交屋裝修而非老屋翻新。

### 4.5 Gaps
- 南韓 2026 年入住量（입주물량）；新加坡 2025 降溫措施（SSD 延長）與私宅轉售全年量；台灣全國房價指數 2026 與新／中古分拆；中國全國二手成交套數 2025、限購放鬆細節、LPR；印度 2025 全年銷售；印尼、菲律賓全國交易與完工；越南《土地法》2024 生效細節；日本、中國、泰國、印尼、菲律賓未售庫存官方值（泰國僅顧問估）。

---

## 5. 翻修需求推估（Q4：Renovation-demand indicator）

### 5.1 Takeaway
以公開可追溯的三個變數——30 年以上存量占比（S）、中古交易占比（T）、所得（I）——建構指標 R，結果：香港 0.80 ＞ 台灣 0.74 ＞ 新加坡 0.72（S 為代理）＞ 南韓 0.58 ＞ 馬來西亞 0.55（低信心）＞ 日本 0.53–0.69 ＞ 中國 0.53 ＞ 泰國 0.51 ＞ 越南 0.29；印尼、菲律賓、印度因 T 無資料不計算，改以新屋交屋量衡量。與 T1 校準後的住宅翻修支出占 GDP 相比，排序方向一致（香港最高、韓＞日），但台灣與新加坡的 R 明顯高於其市場規模占 GDP 比重，顯示（a）台灣翻修市場的既有估計（NT$2,000–5,500 億，低信心）可能低估，或（b）台灣老屋翻修轉化率受都更／危老預期、高齡屋主不投資等因素壓抑；中國與泰國則相反（市場規模口徑含建材零售／新房精裝而偏高）。

### 5.2 方法（全部為本人設計，【示意】）
- **R = 0.4·S′ + 0.4·T′ + 0.2·I′**，三項皆正規化至 0–1。
- **S′ = min(S ÷ 60%, 1)**，S＝30 年以上住宅占存量比（台灣 59%、南韓 30.6%、香港 48–64% 取中值 56%）；無 30 年值者用最接近代理並標註：日本以「築 43 年以上 21%」為下限、另設 45% 為情境上限（1981–1995 年建成之占比本輪無資料）；新加坡以 HIP（1997 年前建成）獲選 49.4 萬戶 ÷ 假設組屋總數約 110 萬戶 ≈ 45%（分母未經驗證）；中國以「2000 年前建成 35%」代理（屋齡 ≥25 年）。
- **T′ = 中古占住宅交易比**：香港 39,821÷(20,525+39,821)=66%；日本首都圈 37,222÷(37,222+23,000)=62%（都會代理）；泰國 64%（2025 底）；中國 50.4%（2026H1）；台灣以「屋齡 3 年以下新屋房貸占 50.3%」反推中古 ≈50%；南韓以 1 − 完工 30 萬 ÷ 買賣 72.6 萬 ≈ 59%（代理）；新加坡以 (HDB 轉售 26,169 ＋ 私宅轉售假設 1.05 萬) ÷ (前者 ＋ 新售 10,611 ＋ BTO 19,723) ≈ 55%；馬來西亞以 1 − 完工 99,877 ÷ 住宅交易 ≈25.6 萬 ≈ 61%；越南以 1 − 一手成交 8.8 萬 ÷ 公寓＋獨立屋成交 138,025 ≈ 36%；印尼、菲律賓、印度無資料。
- **I′ = [ln(人均 GDP 2026) − ln(2,500)] ÷ [ln(110,000) − ln(2,500)]**（對數尺度，IMF 2026 名目）：新加坡 0.99、香港 0.84、台灣 0.75、南韓 0.72、日本 0.70、中國 0.47、馬來西亞 0.47、泰國 0.31、印尼 0.20、越南 0.18、菲律賓 0.15、印度 0.03。
- S 無資料者（泰、馬、越）改以 R = 0.6·T′ + 0.4·I′ 計算並以 ◇ 標示；T 無資料者不計算。

### 5.3 指標表

| 市場 | S（30 年以上占比） | S′ | T（中古占比） | T′ | I′ | **R** | 信心 | T1 校準之住宅翻修支出占 GDP（RR 口徑） | 一致性判讀 |
|---|---|---|---|---|---|---|---|---|---|
| 香港 | 48–64%（私樓，2023） | 0.80–1.00 | 66%（2025） | 0.66 | 0.84 | **0.80（0.75–0.83）** | 中 | 2.5–2.6%（C&SD 非地盤，含新建與機電，高估） | 一致（最高） |
| 台灣 | 59%（2025Q2） | 0.98 | ≈50%（代理） | 0.50 | 0.75 | **0.74** | 中 | 0.69–1.89%（低信心） | **R 高於市場規模**：既有估計偏低或轉化率受抑 |
| 新加坡 | ≈45%（HIP 代理，分母未驗證） | 0.75 | ≈55%（代理） | 0.55 | 0.99 | **0.72** | 低–中 | 0.61%（F&S fit-out 2022E） | R 高於市場規模：HIP 由政府出資、組屋翻修單價受 HDB 規範限制 |
| 南韓 | 30.6%（2025 普查） | 0.51 | ≈59%（代理） | 0.59 | 0.72 | **0.58** | 中 | 1.23–1.41% | 一致 |
| 馬來西亞 ◇ | 無資料 | — | ≈61%（代理） | 0.61 | 0.47 | **0.55** | 低 | 0.21–0.51% | R 高於市場規模：T 代理可能高估（住宅交易含土地／次級市場定義） |
| 日本 | ≥21%（築 43 年以上）；情境 45% | 0.35–0.75 | 62%（首都圈 2024） | 0.62 | 0.70 | **0.53–0.69** | 中 | 1.10–1.13%（矢野，含家具） | 一致（R 上限情境） |
| 中國大陸 | ≈35%（2000 年前建成，代理） | 0.58 | 50.4%（2026H1） | 0.50 | 0.47 | **0.53** | 中 | 1.95–2.67% | **市場規模高於 R**：口徑含新房精裝／整裝 |
| 泰國 ◇ | 無資料 | — | 64%（2025 底） | 0.64 | 0.31 | **0.51** | 中 | 2.5%（HI 含建材零售，高估 RR） | 市場規模高於 R：口徑偏高 |
| 越南 ◇ | 無資料 | — | ≈36%（代理） | 0.36 | 0.18 | **0.29** | 低 | 0.31–0.65% | 一致（低） |
| 印尼 | 無資料 | — | 無資料 | — | 0.20 | 不計算 | — | 0.58%（FU 口徑） | 改看新屋交屋：FLPP 278,868 戶（2025） |
| 菲律賓 | 無資料 | — | 無資料 | — | 0.15 | 不計算 | — | 0.53%（FU 口徑） | 改看新屋交屋：Pag-IBIG 90,727 戶（2025） |
| 印度 | 無資料 | — | 無資料 | — | 0.03 | 不計算 | — | 0.80–0.94%（D＋FU 混合） | 改看新屋交屋：七大城推案 114,320 戶（2026Q3） |

來源：S、T、I 各欄數字之 URL 見 §2–§4；T1 校準值見 [T1 §5.2](./T1-market-size-reconciliation.md)。

### 5.4 Cited Findings（支撐指標之關鍵引用）
- 台灣 30 年以上 59%、屋齡 3 年以下新屋申貸占 50.3% — [Newtalk](https://newtalk.tw/news/view/2025-09-17/994199)；[經濟日報](https://udn.com/news/story/7241/9431371)
- 香港一手 20,525／二手 39,821 宗 — [hket（中原）](https://ps.hket.com/article/4204187/%E4%B8%AD%E5%8E%9F%EF%BC%9A9%E6%9C%88%E6%95%B4%E9%AB%94%E8%B2%B7%E8%B3%A3%E5%AE%97%E6%95%B8%E5%9B%9E%E5%8D%87%E9%80%BE1%E6%88%90%C2%A0%C2%A0%E4%B8%80%E6%89%8B%E7%A7%81%E6%A8%93%E9%87%8D%E4%B8%8A%E9%80%BE%E5%8D%83%E5%AE%97)
- 日本首都圈中古 37,222 vs 新建 2.3 萬 — [DIME](https://dime.jp/genre/1990629/)；1980 年以前 21% — [国交省](https://www.mlit.go.jp/jutakukentiku/house/content/001857617.pdf)
- 南韓 30.6% — [KDI](https://eiec.kdi.re.kr/policy/materialView.do?num=284799)；完工 30 萬 vs 買賣 72.6 萬 — [헤럴드경제](https://biz.heraldcorp.com/article/10887737)；[M이코노미](https://www.m-economynews.com/news/article.html?no=64226)
- 中國 50.4% — [21 財經](https://m.21jingji.com/article/20260729/herald/df3b446d915832c3dab62856c9bf0024.html)；2000 年前 35% — [CN-verification](../verification/CN-verification.md)
- 泰國 64% — [Bangkok Post](https://www.bangkokpost.com/property/3266023/resale-homes-take-larger-market-share)
- 馬來西亞 完工 99,877、住宅交易占 61.6% — [IQI](https://iqiglobal.com/blog/napic-q1-2026/)；[Hartamas](https://hartamas.com/malaysia-property-market-2025-what-the-napic-data-really-shows/)
- 越南 138,025 vs 一手 8.8 萬 — [Tạp chí KTTC](https://tapchikinhtetaichinh.vn/thi-truong-bat-dong-san-quy-iv-va-ca-nam-2025-nguon-cung-tang-giao-dich-soi-dong-140788.html)；[Vietstock VARS](https://vietstock.vn/2026/03/vars-ire-nhieu-nha-dau-tu-bat-dong-san-tang-gap-doi-tai-san-chi-trong-1-2-nam-4220-1415575.htm)
- 中國華泰研究假設翻新週期 10–20 年、2024 年存量重裝占家裝 >50% — [華泰 PDF](https://reportify-1252068037.cos.ap-beijing.myqcloud.com/media/production/s_2d023dd8_2d023dd8457c351583068e0e7510101b.pdf)；泰國 SCB EIC 調查翻修主因為屋齡老化、預算 THB 11–30 萬 — [ThaiPublica](https://thaipublica.org/2024/08/scb-eic-residential-real-estate-survey-2567/)

### 5.5 Inferences
- 台灣 R 0.74 與市場規模 0.69–1.89% GDP 的落差，對集團而言是「結構上存在、尚未被充分貨幣化」的老屋翻修需求：59% 的 30 年以上存量 × 84% 自有率 × 人均 GDP USD 42,103，以日本單價（矢野 RR 1.1% GDP）套算，台灣 RR 合理區間應在 GDP 1.0–1.4%（NT$2,900–4,100 億）【示意】，與 T1 區間上半段相符。
- 越南、印尼、菲律賓、印度的翻修需求在 2026–2030 年仍以「毛胚／基本完成新屋 → 首次裝修」為主，指標 R 不適用；合適的 KPI 是「年交屋戶數 × 毛胚比例 × 單價」。

### 5.6 Gaps
- 指標所需但缺的原始值：日本 30 年以上占比；新加坡組屋總數與私宅轉售全年量；南韓新／中古分拆；台灣新／中古官方分拆；印尼、菲律賓、印度中古交易占比與屋齡；各市場「翻修週期」調查（除中國華泰、泰國 SCB EIC 外皆無）。

---

## 6. 融資與家庭資產負債（Q5：Mortgage, household debt, renovation finance）

### 6.1 Takeaway
2026 年房貸利率分三層：低利（台灣 2.29%、日本變動型升息後仍低、香港 H 按約 3.25%）、中利（南韓 4.66%、新加坡裝修貸 3.5–6%、馬來西亞 SBR 2.75%＋加碼、泰國 GHB 政策貸 1%）、高利（印度 7.0–8.45%、印尼 BI Rate 5.75%、越南優惠 8–10% 後浮動 13–15%）。家庭負債／GDP（BIS 2025-12）南韓 88.6%、香港 87.8%、泰國 87.5%、馬來西亞 69.8%、日本 61.1%、中國 58.0%。政策性修繕融資最完整者為台灣（修繕貸款利息補貼 ≤NT$80 萬＋老宅延壽補助）、新加坡（HIP 年撥 S$4.07 億）、泰國（GHB 1% 修繕貸 ≤THB 30 萬）、南韓（그린리모델링 利息補貼 4.5–5.5%，2026-03 重啟）、日本（子育てグリーン住宅支援 ≤60 萬円）、越南（VBSP 4.8%）；銀行裝修貸額度：新加坡 S$30,000 或 6 倍月薪、馬來西亞 Maybank ≤RM250,000、印尼 Gradana ≤Rp 20 億、菲律賓 Pag-IBIG 房貸（含修繕）≤PHP 600 萬。

### 6.2 十二市場融資表

| 市場 | 房貸利率 2026 | 政策利率 2026 | 家庭負債／GDP | 銀行裝修貸款（產品／上限／利率） | 政府修繕融資／補助 | 來源 |
|---|---|---|---|---|---|---|
| 日本 | 變動型：日銀 9 月升息多在 2027-04 基準利率改定反映（具體利率無資料） | **1.25%（2026-09-18；6 月 1.00%）** | **61.1%（BIS 2025-12）** | 無資料（リフォームローン本輪未查） | **子育てグリーン住宅支援事業（裝修）S 型 ≤60 萬円／戶（≈USD 4,000／NT$12.6 萬）、A 型 ≤40 萬円**，2025-12-31 公募結束；リフォーム減税等未查 | [NHK](https://news.web.nhk/newsweb/na/nd-20260918de50968)；[モゲチェック](https://mogecheck.jp/articles/show/pnl6ZzOV4BDR2k5Ra7PY)；[TradingEconomics 家庭負債表](https://tradingeconomics.com/country-list/households-debt-to-gdp?continent=asia)；[Yahoo Finance（BIS Q4 2025）](https://finance.yahoo.com/economy/articles/ranked-countries-highest-debt-gdp-120507169.html)；[三菱電機 解說](https://www.mitsubishielectric.co.jp/ldg/ja/information/subsidy/kosodate-green/index.html)；[国交省 PDF](https://www.mlit.go.jp/report/press/content/001846077.pdf) |
| 南韓 | **銀行新承做주담대 4.66%（2026-08；固定 4.88%、變動 4.53%）**，市場利率 9 月再 +0.20pp | **3.00%（2026-08-27；7 月 2.75%）**；下次 10-22 | **88.6%（BIS 2025-12；一年前 97.3%）** | 無資料（本輪未查） | **민간건축물 그린리모델링 이자지원 2026-03-17 重啟**：基本 4.5%、節能 ≥30%／多子女／高齡／新婚 5.5%；10·15 對策房貸上限 6／4／2 億韓元（≈USD 43／29／14 萬；NT$1,350／900／450 萬） | [한국일보](https://www.hankookilbo.com/news/article/A2026093010490005879)；[한국금융신문](https://www.fntimes.com/html/view.php?ud=202608271107018117179ad43907_18)；[TheGlobalEconomy KR](https://www.theglobaleconomy.com/rankings/household_debt_gdp/)；[korea.kr 그린리모델링](https://www.korea.kr/news/policyNewsView.do?newsId=148960908)；[머니투데이](https://www.mt.co.kr/estate/2026/03/16/2026031609173892550)；[뉴스핌 10·15](https://www.newspim.com/news/view/20251015000279) |
| 新加坡 | 無資料（本輪未查） | 無資料 | 無資料 | **裝修貸款上限 S$30,000（≈USD 22,556／NT$71 萬）或 6 倍月薪取低者**；最長 5 年；僅限固定裝置；利率 2026 年 3.5–6%（廣告 3.88%、EIR 7.05%）；DBS 手續費 2%＋保險 1% | **HIP 2025 批次 29,000 戶／371 棟／S$4.07 億（≈USD 3.06 億／NT$96 億）**；累計 49.4 萬戶獲選、S$40 億；**HIP II**（60–70 年屋齡）2025-08 宣布 | [MoneySmart](https://www.moneysmart.sg/personal-loan/how-much-can-you-borrow-for-a-renovation-loan-in-singapore-ms)；[DBS](https://www.dbs.com.sg/personal/loans/homeloans/renovation-loan)；[SingSaver](https://www.singsaver.com.sg/blog/best-renovation-loan-in-singapore)；[SmartCalculator 2026](https://www.smartcalculator.sg/housing/renovation-loan-calculator)；[AsiaOne HIP](https://www.asiaone.com/singapore/govt-allocates-over-407m-upgrading-works-29000-hdb-flats-home-improvement-programme)；[99.co](https://www.99.co/singapore/insider/hdb-home-improvement-programme-2025/) |
| 香港 | **H 按實際約 3.25%**；1M HIBOR 2.63%（2026-08-19）→2.88%（09-11） | 聯繫匯率隨美息 | **87.8%（BIS 2025-12）** | 無政府補貼之私人貸款：銀行實際年利率約 2.5–8%、財務公司 8–15%；2026-04 參考 HSBC 3.38%、Citi 3.58%、DBS 3.68% | **長者維修自住物業津貼 ≤HK$8 萬（≈USD 10,256／NT$32 萬，≥60 歲）**；政府免息裝修貸款已終止；中原按揭 × 好師傅 CoDECO 交叉導流 | [wuchatprop](https://www.wuchatprop.com.hk/hibor/)；[mReferral](https://www.mreferral.com/blog/%E6%8C%89%E6%8F%AD%E5%88%A9%E7%8E%87/)；[TradingEconomics](https://tradingeconomics.com/country-list/households-debt-to-gdp?continent=asia)；[MoneyHero](https://www.moneyhero.com.hk/zh/personal-loan/blog/%E8%A3%9D%E4%BF%AE%E8%B2%B8%E6%AC%BE-%E7%A7%81%E4%BA%BA%E8%B2%B8%E6%AC%BE-%E6%AF%94%E8%BC%83)；[Intermatch 2026](https://intermatch.com.hk/articles/renovation-loan-hk-2026)；[1880](https://www.1880.com.hk/loan/782/)；[中原按揭 × CoDECO](https://www.centamortgage.com/information/detail/%E4%B8%AD%E5%8E%9F%E6%8C%89%E6%8F%ADX%E5%A5%BD%E5%B8%AB%E5%82%85CoDECO%E8%A3%9D%E4%BF%AE%E9%85%8D%E5%B0%8D%E5%B9%B3%E5%8F%B0%E5%B1%95%E9%96%8B%E7%AD%96%E7%95%A5%E5%90%88%E4%BD%9C_181965) |
| 台灣 | **五大銀行新承做購屋貸款 ≈2.29%（2026-07）**；一般方案 2.45% 起；青安 3.0 前 3 年 **1.775%**（滿 3 年後逐年減補、回復約 2.275%） | 無資料（本輪未查央行重貼現率） | 無資料（CEIC 有台灣序列，本輪數值未開啟） | 無資料（銀行裝修貸本輪未查；三商美福等業者與銀行合作裝修貸，廣編） | **修繕住宅貸款利息補貼：優惠貸款最高 NT$80 萬（≈USD 25,397）**，115 年度（2026）9/1–9/30 受理，自購＋修繕合計 6,000 戶，自購第一類 1.187%／第二類 1.762%（修繕專屬利率未取得），可搭青安；**青安 3.0 2026-08-01～2029-07-31**（2.0 額度 1,000 萬／40 年）；**老宅延壽機能復新計畫**：屋齡 ≥30 年、補助 ≤65%、公共 ≤960 萬／棟、戶內 ≤20 萬（高齡弱勢 ≤30 萬），至 2027-12-31 | [money101](https://www.money101.com.tw/blog/%E6%88%BF%E8%B2%B8%E5%88%A9%E7%8E%87)；[Yahoo 2026-07 房貸整理](https://tw.stock.yahoo.com/news/2026%E5%B9%B47%E6%9C%88%E6%88%BF%E8%B2%B8%E5%88%A9%E7%8E%87%E7%B8%BD%E6%95%B4%E7%90%86%EF%BD%9C%E5%AE%98%E6%96%B9%E5%B9%B3%E5%9D%872322%EF%BC%85-%E5%85%AC%E8%82%A1%E3%80%81%E6%B0%91%E7%87%9F%E9%8A%80%E8%A1%8C%E8%88%87%E6%96%B0%E9%9D%92%E5%AE%8930%E4%B8%80%E6%AC%A1%E7%9C%8B-081600061.html)；[房感 青安 3.0](https://www.housefeel.com.tw/article/%E9%9D%92%E5%B9%B4-%E9%A6%96%E8%B3%BC-%E8%B2%B8%E6%AC%BE-%E8%B3%BC%E5%B1%8B%E8%B2%B8%E6%AC%BE-%E5%AE%89%E5%BF%83%E6%88%90%E5%AE%B6%E8%B2%B8%E6%AC%BE/)；[住商 青安 3.0](https://www.hbhousing.com.tw/news/detail.aspx?num=5278)；[市場先生](https://rich01.com/young-housing-loans/)；[今周刊 住宅補貼](https://www.businesstoday.com.tw/article/category/183030/post/202609150009/)；[數位時代](https://www.bnext.com.tw/article/92240/2026-housing-loan-interest-subsidy)；[東森 利率](https://fnc.ebc.net.tw/fncnews/house/219833)；[國土署 老宅延壽 PDF](https://www.nlma.gov.tw/uploads/files/a5d37b464dc02a5814200514847f5c1a.pdf)；[CEIC 家庭負債](https://www.ceicdata.com/en/indicator/household-debt--of-nominal-gdp)；[商業周刊 三商美福](https://www.businessweekly.com.tw/business/indep/1005275) |
| 中國大陸 | 無資料（LPR 本輪未取得 URL） | 無資料 | **58.0%（BIS 2025-12）** | 城商行「以舊換新」裝修貸 3.35–4.15%、額度 ≤50 萬元（≈USD 69,444／NT$219 萬）（2024） | 2026 年國補四類不含家裝（家電 15%、單件 ≤1,500 元） | [TradingEconomics](https://tradingeconomics.com/country-list/households-debt-to-gdp?continent=asia)；[中證網](https://cs.com.cn/yh/04/202407/t20240704_6422052.html)；[新華網](https://www.news.cn/politics/20260102/8280c1156) |
| 馬來西亞 | SBR 2.75%（2025-07-14 起）＋銀行加碼；BLR 6.60% | **OPR 2.75%（2025-07 至 2026-09）** | **69.8%（BIS 2025-12）**；CEIC 另列 84.7%（2025，口徑不同） | **Maybank MyDeco 4.40% p.a. 起、上限 RM250,000（≈USD 56,818／NT$179 萬）**、融資比例 20–30%；CIMB Renovation 5.5–6.88% flat、RM200,000、10 年；**RHB × The Makeover Guys「購屋＋裝修」≤房價 120%（2026-09-15）**；Maybank Home+Reno ≤120% | 無政府修繕補助（本輪未見）；房貸核准率 39.2%（2026 年 1–4 月） | [CIMB 基準利率](https://www.cimb.com.my/en/personal/help-support/rates-charges/cimb-base-rate.html)；[Paultan](https://paultan.org/2026/09/04/bank-negara-opr-sept-2026-mpc-meeting/)；[TradingEconomics](https://tradingeconomics.com/country-list/households-debt-to-gdp?continent=asia)；[CEIC](https://www.ceicdata.com/en/indicator/household-debt--of-nominal-gdp)；[Maybank MyDeco](https://www.maybank2u.com.my/maybank2u/malaysia/en/personal/loans/home/mydeco.page)；[PropCashflow](https://propcashflow.my/blog/loan-for-house-renovation-malaysia/)；[Malay Mail RHB](https://www.malaymail.com/news/money/mediaoutreach/2026/09/15/the-makeover-guys-and-rhb-bank-introduce-the-makeover-flexi-loan-with-up-to-120-financing-for-home-purchase-and-renovation/487671)；[Global Property Guide](https://www.globalpropertyguide.com/asia/malaysia/price-history) |
| 泰國 | 無資料（商業銀行房貸本輪未查） | 無資料（本輪未查） | **87.5%（BIS 2025-12）**；BoT 86.8%（2025Q2）；WB 86.9%（2026Q1）；SCB EIC 85.9%（2026Q1） | KTC、AP 等提供修繕貸款指南（額度未列） | **GHB（ธอส.）修繕／增建／設備貸款：利率 1.00% 起、最長 40 年、兩方案合計 ≤THB 300,000（≈USD 9,091／NT$28.6 萬）**（2026-04-09）；2025-06 版前 3 年 1.00%、≤THB 100,000；太陽能屋頂抵稅 ≤THB 20 萬（2026-03-03～2028-12-31）；LTV 100% 與 0.01% 規費延至 2027-06-30 | [TradingEconomics](https://tradingeconomics.com/country-list/households-debt-to-gdp?continent=asia)；[Thansettakij 家庭負債](https://www.thansettakij.com/economy/645297)；[Dailynews（WB）](https://dailynews.co.th/news/6252478)；[Positioning（SCB EIC）](https://positioningmag.com/insight/114547)；[GHB 2026-04](https://www.ghbank.co.th/news/detail/public-relations/press-09-04-2026)；[GHB 2025-06](https://www.ghbank.co.th/news/detail/public-relations/press-19-06-2025)；[Bangkokbiznews](https://www.bangkokbiznews.com/economics/1228967)；[Prudential 抵稅](https://www.prudential.co.th/th/knowledge-corner/growing-wealth/tips-to-reduce-personal-income-tax/)；[Thansettakij LTV](https://www.thansettakij.com/economy/659052) |
| 越南 | **優惠 8–10%（6–24 個月）→ 浮動 13–15%（2026-09）**；2026-02 多家升至 13–14%，61% 有需求者延後購屋 6–12 個月 | 無資料 | 無資料 | 無資料（商業銀行裝修貸本輪未查） | **VBSP 社會住宅購買／新建／翻修貸款 4.8%**（最長 25 年，限住宅法對象）；2026-07-01 起 35 歲以下社宅貸款 6.5% | [Smartland](https://smartland.vn/lai-suat-vay-mua-nha-2026/)；[Dân Việt](https://danviet.vn/thang-2-2026-lai-suat-vay-mua-nha-co-de-tho-khong-d1403524.html)；[VNBA（VBSP）](https://vnba.org.vn/vi/dieu-kien-lai-suat-vay-ngan-hang-chinh-sach-mua-nha-sua-nha-11963.htm)；[LSVN 4.8%](https://lsvn.vn/lai-suat-cho-vay-mua-nha-o-xa-hoi-la-4-8-nam-1683716533-a130259.html)；[LuatVietnam](https://luatvietnam.vn/tin-van-ban-moi/chinh-thuc-ap-dung-lai-suat-65-nam-cho-nguoi-duoi-35-tuoi-vay-mua-nha-o-xa-hoi-tu-01-7-2026-186-109829-article.html) |
| 印尼 | 無資料（KPR 利率本輪未查）；購屋者 69.87% 使用 KPR | **BI Rate 5.75%（2026-05／06 升、9 月維持；DF 4.75%、LF 6.50%）** | 無資料 | **Gradana（OJK 持牌 P2P）翻修貸款 ≤Rp 20 億（≈USD 125,000／NT$394 萬）**，依 RAB 核貸 | **FLPP 補貼房貸 2025 年 278,868 戶／Rp 34.64 兆**（配額 35 萬戶）；無獨立修繕補助 | [BI 2026Q1](https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_289726.aspx)；[Bisnis](https://finansial.bisnis.com/read/20260923/11/2006538/alasan-bank-indonesia-tahan-bi-rate-september-2026-di-575)；[Kompas BI](https://money.kompas.com/read/2026/08/19/144130626/bi-rate-tetap-575-persen-pada-agustus-2026)；[Gradana](https://gradana.co.id/grasewa-grarenov)；[Media Indonesia](https://mediaindonesia.com/ekonomi/845538/penyaluran-flpp-2025-cetak-rekor-tertinggi-tembus-278868-unit-rumah) |
| 菲律賓 | Pag-IBIG 房貸 5.75%（1 年固定）起；社會住宅 3%、促銷 4.5% | 無資料 | 無資料 | **Pag-IBIG 房貸用途含 home improvement，上限 PHP 600 萬（≈USD 105,263／NT$332 萬）、最長 30 年** | 4PH 社會住宅 3%（2025 年 7,056 戶／PHP 76.3 億） | [Pag-IBIG Housing Loan](https://www.pagibigfund.gov.ph/HousingLoan.html)；[Manila Standard](https://manilastandard.net/business/314693903/pag-ibig-housing-loans-rose-8-to-record-p140-54-billion-in-2025.html)；[Inquirer 3%](https://business.inquirer.net/582687/pag-ibig-keeps-3-housing-rate) |
| 印度 | **最低 7.00–7.35%（2026-10：Bank of Maharashtra 7.00%、SBI 7.25%）；SBI 區間 7.25–8.45%**；RBI 2026-10-07 據報 repo +25bp 至 5.50%（單一來源） | 5.25%（2025-12 起）→5.50%（待核） | 無資料 | SBI、HDFC 等 home improvement loan 以房貸利率計（未驗證，既有筆記） | PMAY-U 2.0 為新建／增建補助，無獨立修繕補助（未驗證） | [Upstox](https://upstox.com/news/personal-finance/latest-updates/cheapest-home-loan-rates-in-october-2026-12-lenders-offer-7-1-7-35-interest-emi-revisions-may-follow/article-201440/)；[UrbanMoney](https://www.urbanmoney.com/home-loan/state-bank-of-india/interest-rate)；[Daily Financial](https://dailyfinancial.in/home-loan-rates-in-october-2026-should-you-lock-your-interest-rate-now-or-wait-for-the-rbi-decision/)；[IN-B-rules §（未驗證）](../countries/IN-B-rules.md) |

### 6.3 Cited Findings（補充）
- BIS 口徑家庭負債／GDP（2025-12）：南韓 88.6（前值 89.4）、香港 87.8、泰國 87.5、馬來西亞 69.8、日本 61.1、中國 58.0 — [TradingEconomics 亞洲表](https://tradingeconomics.com/country-list/households-debt-to-gdp?continent=asia)；[Yahoo Finance（BIS Q4 2025）](https://finance.yahoo.com/economy/articles/ranked-countries-highest-debt-gdp-120507169.html)；南韓一年前 97.3% — [TheGlobalEconomy](https://www.theglobaleconomy.com/rankings/household_debt_gdp/)。台灣不在上述表中（缺口）。
- 南韓 10·15 對策後 2025Q4 銀行房貸增幅由 10.9 兆降至 4.8 兆韓元；主담대 4.66% 為 2022-11（4.74%）以來最高 — [머니투데이](https://www.mt.co.kr/economy/2026/02/24/2026022411382531015)；[한국일보](https://www.hankookilbo.com/news/article/A2026093010490005879)。
- 台灣 115 年度修繕貸款利息補貼：優惠貸款最高 80 萬、僅 1 戶老屋者可申請、同一家庭每年擇一（自購／修繕／租金） — [今周刊](https://www.businesstoday.com.tw/article/category/183030/post/202609150009/)；[數位時代](https://www.bnext.com.tw/article/92240/2026-housing-loan-interest-subsidy)。
- 泰國 GHB 2026-04-09「一站式」修繕貸：1.00% 起、最長 40 年、月付 300 泰銖起、合計 ≤30 萬泰銖（超出 20 萬屬 Plus 1.99%、≤5 年） — [GHB](https://www.ghbank.co.th/news/detail/public-relations/press-09-04-2026)；[Bangkokbiznews](https://www.bangkokbiznews.com/economics/1228967)。

### 6.4 Inferences
- 修繕專屬政策融資的「額度」排序：馬來西亞（RM25 萬 ≈ NT$179 萬）＞ 台灣（NT$80 萬）＞ 新加坡（S$3 萬 ≈ NT$71 萬）＞ 泰國（THB 30 萬 ≈ NT$28.6 萬）＞ 日本補助（≤60 萬円 ≈ NT$12.6 萬），與各市場老屋翻新單價（台灣每坪 10–15 萬、新加坡轉售四房 S$6.4–8 萬）相比，台灣與新加坡的政策融資只能覆蓋全屋翻新的 15–40%，其餘靠自有資金或信貸——高家庭負債市場（韓、港、泰）因此對利率更敏感。

### 6.5 Gaps
- 台灣、新加坡、越南、印尼、菲律賓、印度之 BIS 口徑家庭負債；中國 LPR 與房貸利率 2026；日本リフォームローン利率與規模；南韓、新加坡、泰國、越南、印尼之商業銀行裝修貸款平均金額與筆數（各市場皆未公開）；台灣修繕貸款利息補貼之專屬利率與核定戶數；印度 PMAY／home improvement loan 驗證。

---

## 7. 區域與城市聚焦（Q6：Metro areas concentrating renovation demand）

### 7.1 Takeaway
翻修需求在各市場高度集中於 2–3 個都會區：日本首都圈（中古成約 >新建）、南韓首爾／首都圈（30 年以上公寓 29%、房貸管制最嚴）與大田（35%）、台灣台北（30 年以上 73.8%）＋新北／桃園（交屋潮）、中國上海（2000 年前建成 50.38%）／北京（2026H1 二手 93,583 套）／廣州與成都（二手占 >60–80%）、泰國大曼谷（639 萬戶、未售公寓 35 萬）、馬來西亞雪蘭莪（250 萬戶）＋柔佛（JS-SEZ 新增 11.5 萬戶）、越南河內／胡志明（公寓價 +20–30%）、印尼 Jabodetabek、印度 MMR／Bengaluru／Hyderabad。宜蘭 2025 年移轉 5,270 棟（−23.6%）、房價指數最抗跌、民宿全台第一（2,177 家），是「新成屋輕裝修＋民宿商空改裝」雙引擎市場。

### 7.2 各市場重點都會區

| 市場 | 重點都會區（2–3） | 住宅／交易數據 | 來源 |
|---|---|---|---|
| 日本 | **首都圈（東京・神奈川・埼玉・千葉）**；近畿圈（大阪・兵庫）；中京（愛知） | 首都圈 2024 中古公寓成約 37,222 件 vs 新建供給約 2.3 萬戶；東京都居住住宅中共同住宅 71.6%；東京都區部持ち家中共同住宅 56%（2021–23 年竣工者 52%）；リノベる直營區（東京、神奈川、大阪、兵庫、愛知）2021–23 成約 65% 為築 31 年以上；ホームテック 2025 年營收 72.8 億円居東京翻修店第 1 | [DIME](https://dime.jp/genre/1990629/)；[東京都 概要](https://www.toukei.metro.tokyo.lg.jp/jyutaku/2023/jt23tgaiyou.pdf)；[大和不動産鑑定 東京都区部](https://daiwakantei.co.jp/wp/uploads/2025/09/01a50e7ab2d4f8134dd676e8728cb8eb.pdf)；[リノベる user report](https://www.renoveru.jp/hubfs/corporate2024/pdf/20240625%E3%80%90%E3%83%97%E3%83%AC%E3%82%B9%E3%83%AA%E3%83%AA%E3%83%BC%E3%82%B9%E3%80%91%E3%80%8C%E3%83%AA%E3%83%8E%E3%83%99%E3%82%8B%E3%80%82%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%80%8D%E3%82%92%E5%85%AC%E9%96%8B.pdf)；[t23m-navi](https://t23m-navi.jp/magazine/?p=42901)；[大阪府 公表](https://www.pref.osaka.lg.jp/hodo/fumin/o040090/prs_51163.html) |
| 南韓 | **首爾／首都圈**；大田；釜山等五大廣域市 | 30 年以上公寓占比：大田 35%、首爾 29%、仁川／蔚山 25%、首都圈 21%、五大廣域市 25%（2025-06）；首都圈自有自住 52.7%（2024）；未售首都圈 19,136 戶（2026-08）；10·15 對策針對首都圈全域；首例垂直增建翻修 송파 성지（2025-03 完工）、松坡另 13 社區推動、옥수극동 900 戶 2025-02 通過首爾市審議 | [한국경제（R114）](https://www.hankyung.com/article/2025061796206)；[메트로서울](https://www.metroseoul.co.kr/article/20250617500101)；[KDI 주거실태](https://eiec.kdi.re.kr/policy/materialView.do?num=273475)；[뉴데일리 미분양](https://biz.newdaily.co.kr/site/data/html/2026/09/30/2026093000005.html)；[머니투데이 성지](https://www.mt.co.kr/estate/2025/03/09/2025030909032388302)；[뉴데일리 옥수](https://biz.newdaily.co.kr/site/data/html/2025/02/26/2025022600180.html) |
| 新加坡 | **中央區（Central）**、東部（較老轉售組屋）；Bidadari 等新 BTO 區 | Qanvast 2026 預算報告：中央區高預算比例最高、東部次之，歸因較老轉售存量；CCR 私宅空置 10.3%（2025Q1）；2025 年 Bidadari 四個 BTO 項目完工；2026-02 BTO 約 1,300 戶等候 <3 年 | [Qanvast 2026](https://qanvast.com/sg/articles/2026-qanvast-renovation-budgeting-report-insights-from-300-homeowners-3573)；[ERA 1Q2025](https://www.era.com.sg/research-articles/1q-2025-rental-report)；[EdgeProp BTO](https://www.edgeprop.sg/property-news/hdb-supplying-19600-bto-flats-2026-spread-over-three-sales-exercises)；[Malay Mail](https://www.malaymail.com/amp/news/singapore/2026/01/31/singapores-february-bto-launch-to-feature-1300-flats-with-faster-completion-times-under-three-years/207497) |
| 香港 | 全港（分區統計本輪未取得） | 住宅買賣 62,832 宗（2025）；私樓空置 56,080 伙；普通話拼音登記買家私樓交易近 1.4 萬宗、HK$1,410 億（2025，+20%，「雙破頂」） | [hket](https://ps.hket.com/article/4204187/%E4%B8%AD%E5%8E%9F%EF%BC%9A9%E6%9C%88%E6%95%B4%E9%AB%94%E8%B2%B7%E8%B3%A3%E5%AE%97%E6%95%B8%E5%9B%9E%E5%8D%87%E9%80%BE1%E6%88%90%C2%A0%C2%A0%E4%B8%80%E6%89%8B%E7%A7%81%E6%A8%93%E9%87%8D%E4%B8%8A%E9%80%BE%E5%8D%83%E5%AE%97)；[RVD](https://www.rvd.gov.hk/doc/tc/HKPR2026_Preliminary_Findings_TC.pdf)；[Yahoo 財經（中原）](https://hk.finance.yahoo.com/news/%E6%B8%AF%E6%A8%93-%E4%B8%AD%E5%8E%9F-%E5%8E%BB%E5%B9%B4%E6%B6%89%E6%99%AE%E9%80%9A%E8%A9%B1%E6%8B%BC%E9%9F%B3%E7%99%BB%E8%A8%98%E8%B2%B7%E5%AE%B6%E7%A7%81%E6%A8%93%E4%BA%A4%E6%98%93%E8%BF%911-4%E8%90%AC%E5%AE%97%E5%A2%9E%E5%85%A9%E6%88%90-%E6%B6%891-061239279.html) |
| 台灣 | **台北市（老屋翻新）**；**新北／桃園／台中（交屋潮）**；宜蘭（集團所在地，見 7.3） | 台北市 30 年以上 673,357 戶（73.8%，全台最高）、平均屋齡 39.1 年、買賣屋齡約 37 年（最老）；桃園 27.4–28.3 年最年輕；六都 2025 買賣移轉 205,000 棟（−24.6%）；2025H1 桃園、台中使照創新高；台中千萬以下成交 成屋 91.4%；台北／新北空屋率 7.09%／7.45% 全台最低 | [Newtalk 台北](https://newtalk.tw/news/view/2025-09-23/995218)；[聯合 買賣屋齡](https://udn.com/news/story/7241/9542785)；[理財周刊 六都](https://www.moneyweekly.com.tw/_Article?AID=206963)；[經濟日報 使照](https://udn.com/news/story/7241/8934080)；[工商時報 台中](https://www.ctee.com.tw/news/20260116701456-430601)；[經濟日報 空屋](https://money.udn.com/money/story/5621/8909453) |
| 中國大陸 | **上海**；**北京**；廣州／成都（二手主導） | 上海 2000 年前建成住房 50.38%（全國最高）、2025 年每 97 人有 1 人買二手房、存量房裝修需求占比「突破 72%」（業者分析，低信心）、2025H1 裝修報價 +8.3%；北京 2026H1 二手網簽 93,583 套；廣州二手占比 >60%；成都逼近 80%；一二線核心城市普遍 >60% | [騰訊（普查年鑑）](https://news.qq.com/rain/a/20220628A0BO3R00)；[第一財經](https://www.yicai.com/news/102986289.html)；[搜狐 上海](https://m.sohu.com/a/947081319_122493552)；[網易 上海](https://www.163.com/dy/article/K7J9B3L30556EG2C.html)；[騰訊 北京](https://news.qq.com/rain/a/20260924A0ELOT00)；[21 財經 廣州](https://m.21jingji.com/article/20260729/herald/df3b446d915832c3dab62856c9bf0024.html)；[新浪](https://www.sina.cn/news/detail/5321584597273666.html) |
| 馬來西亞 | **雪蘭莪／吉隆坡（巴生谷）**；**柔佛（新山，JS-SEZ）**；檳城 | 雪蘭莪住宅 250 萬戶全國最多；柔佛 2025–26 新增 11.5 萬戶、JS-SEZ 房價 +7–9%、RTS 2027-01-01 通車；overhang 中公寓／大樓占 47.1%（2025Q4） | [FMT](https://www.freemalaysiatoday.com/category/nation/2026/04/23/malaysian-housing-units-reached-10-9mil-in-2025-says-statistics-dept)；[EdgeProp 柔佛](https://www.edgeprop.my/content/1917690/johor-adds-115000-homes-meet-demand-fuelled-industrial-rts-js-sez)；[StackedHomes](https://stackedhomes.com/johor-sez-rental-yields-oversupply/)；[Threads NAPIC](https://www.threads.com/@malaysiauncapped/post/DWWc8eDkT8b/) |
| 泰國 | **大曼谷（BMR）**；東部經濟走廊（EEC）；普吉／清邁（度假） | BMR 住宅 639 萬戶（AREA 2025）；未售公寓約 35 萬戶（5–6 年去化）；2025 新公寓推案 THB 772 億（−41%）；2026H1 全國低層 111,624 戶（+14.6%）、公寓 56,041（+24.1%）；中古公寓掛牌 49,199 戶（+25.2%，2026Q2） | [TNews（AREA）](https://www.tnews.co.th/social/social-news/637990)；[The Nation](https://www.nationthailand.com/business/property/40067333)；[Bangkok Post](https://www.bangkokpost.com/property/3217494/cautious-developers-to-cut-bangkok-housing-launches)；[Thai Press](https://www.thethaipress.com/2026/169482)；[Retail News Asia](https://retailnews.asia/thailand-resale-condo-transfers-surge-39-percent-in-second-quarter) |
| 越南 | **河內**；**胡志明市**；峴港 | 河內、胡志明公寓價 2025 年 +20–30%；2026Q1 河內新案達 128 百萬 VND/m²；既成區二手公寓約 50 百萬 VND/m²（2025Q1）；河內舊公寓重建同意門檻降至 51% | [Người Đô Thị](https://nguoidothi.net.vn/gia-chung-cu-tai-ha-noi-va-tp-hcm-tang-toi-hon-20-30-trong-nam-2025-51374.html)；[Vietstock 2026Q1](https://vietstock.vn/2026/05/vars-ire-gia-ban-bat-dong-san-tiep-tuc-leo-thang-ha-noi-cham-128-trieum2-4220-1436994.htm)；[VARS Q1 2025](https://vars.com.vn/tin-tuc/tcbc-bao-cao-thi-truong-bat-dong-san-viet-nam-quy-1-nam-2025-kich-hoat-chu-ky-moi-n1937)；[Người Quan Sát](https://nguoiquansat.vn/ha-noi-trao-quyen-cho-cac-chu-nha-duoc-tu-de-xuat-cai-tao-chung-cu-cu-298599.html) |
| 印尼 | **Jabodetabek（大雅加達）**；泗水；萬隆 | Jabodetabek 租屋家戶 124 萬（14.6%）；雅加達 2025 新增公寓約 2,200 戶（−50%）、存量約 232,000（低信心）；雅加達工人日薪 Rp 165,000 全國最高；維修平台 Kanggo／Gravel 僅服務 Jabodetabek、泗水 | [Kompas.id](https://www.kompas.id/artikel/harga-rumah-semakin-tak-tergapai)；[Mordor（低信心）](https://www.mordorintelligence.com/industry-reports/real-estate-market-in-indonesia)；[Kompas（BPS）](https://www.kompas.com/properti/read/2025/10/07/103000621/upah-tukang-per-hari-di-jakarta-termahal-se-indonesia)；[Investor.id Kanggo](https://investor.id/business/409706/pengguna-kanggo-tembus-36-ribu-layanan-perawatan-bangunan-kian-diminati) |
| 菲律賓 | **Metro Manila**；宿霧；Davao | 無都會層級住宅統計（缺口）；全國：2020 普查住宅 2,850 萬、有人居住 2,520 萬 | [BusinessWorld](https://www.bworldonline.com/special-features/2024/10/24/630972/building-better-affordable-housing-for-filipino-families/) |
| 印度 | **MMR（孟買都會區）**；**Bengaluru**；Hyderabad（Delhi-NCR、Pune、Chennai、Kolkata 2026Q3 下滑） | 2026Q3 銷售 MMR 31,750 戶、Bengaluru 16,670 戶；七大城未售 63.1 萬戶、均價 +7% | [Storyboard18](https://www.storyboard18.com/amp/how-it-works/mmr-bengaluru-drive-q3-housing-sales-as-it-grows-10-qoq-3-yoy-anarock-ws-lo-111529.htm)；[Outlook Money](https://www.outlookmoney.com/amp/story/invest/housing-market-sees-modest-sales-growth-in-q3-as-launches-jump-18-per-cent) |

### 7.3 宜蘭（集團所在地）專節

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| 建物買賣移轉棟數 | **約 5,270 棟（−23.6%）**；宜蘭為北台灣 2025 年推案量逆勢成長縣市但交易未同步 | 2025 | [94m 房市報告（引內政部）](https://94m.com.tw/articles/c049ff) | 中 |
| 房價指數 | **178.63（−0.81%）**，東台灣相對抗跌 | 2025 | [94m](https://94m.com.tw/articles/c049ff) | 中 |
| 實價登錄中位數單價 | **約 29.83 萬／坪（2025 全年）**；8 月 36.29 萬最高、2 月 27.01 萬最低；新建案樣本 956 筆／96.01 億元 | 2025 | [myhousing 宜蘭報告](https://www.myhousing.com.tw/n/n02/n0203/n020301/269746/) | 中 |
| 成屋實價均價 | 每坪 23.6 萬（2024 年 23.5 萬，+0.2%） | 2025 | [工商時報](https://wantrich.chinatimes.com/news/20251011900027-420101)（既有筆記） | 中 |
| 近一年成交單價（仲介平台） | 宜蘭縣約 27 萬／坪；宜蘭市約 30 萬／坪 | 2025–26 | [樂居 宜蘭縣](https://www.leju.com.tw/map/region?mode=price&city=G)；[樂居 宜蘭市](https://www.leju.com.tw/map/region?city=G&area=G260) | 低（平台） |
| 交易結構（大廈 vs 透天） | **電梯大樓 43.5% 首度超越透天 38.6%**（聯徵）；2024 年 43% vs 38%，2015 年透天 50%、大廈 17% | 2024–25 | [myhousing](https://www.myhousing.com.tw/n/n02/n0203/n020301/269746/)；[NOWnews](https://www.nownews.com/news/6561997) | 中 |
| 新成屋占比 | 屋齡 5 年以下新成屋買賣占 19.5%，高於全台 | 年份待核 | [理財周刊](https://www.moneyweekly.com.tw/_Article?AID=156359) | 低 |
| 預售解約 | 2026Q1 預售屋解約 29 件，全國第五、超過雙北 | 2026Q1 | [經濟日報](https://money.udn.com/money/amp/story/5621/9514871) | 中 |
| 成交屋齡分布 | **無資料**（僅單筆實價登錄屋齡） | — | — | — |
| 外地買家占比 | **無資料**；全國外國人取得建物 857 棟（2005 年以來最低，非宜蘭專屬）；質性：移居宜蘭買房者增加（「幸福指數」報導） | 2025 | [myhousing](https://www.myhousing.com.tw/n/n02/n0203/n020301/269746/)；[聯合 房產](https://house.udn.com/house/story/123589/9206196) | 低 |
| 合法民宿家數 | **2,177 家、8,085 房（2025-05，全台第一；花蓮 1,748、台東 1,563）**；全國 114 年合法民宿 12,551 家（+407）；非法民宿 566 家，宜蘭 71 家（第 3）、裁罰金額宜蘭 651 萬元居首 | 2025 | [公視](https://news.pts.org.tw/article/803305)；[工商時報 2026-01-11](https://www.ctee.com.tw/news/20260111700312-431401)；[經濟日報 非法旅館](https://money.udn.com/money/amp/story/5621/9257993)（搜尋摘要引述，各數字之確切網址待核） | 中 |
| 宜蘭 2025 年底民宿家數、裝修市場規模 | **無資料** | — | 建議查觀光署臺灣旅宿網縣市統計 | — |

### 7.4 Inferences
- 宜蘭「大廈交易占比 43.5% ＞ 透天 38.6%」＋「5 年內新屋占 19.5%」＋「民宿全台第一」三者，指出集團在地的三條產品線：新成屋（大廈）輕裝修套餐、透天／老屋全室翻新、民宿與餐飲商空改裝；2026Q1 預售解約居全國第五則提示交屋裝修訂單有遞延風險。
- 民宿非法家數 566 家（全國）、宜蘭裁罰金額居首，意味「合法化改裝」（消防、無障礙、建築用途變更）是可被政策推動的裝修需求。

### 7.5 Gaps
- 香港分區、菲律賓都會、印尼全國交易等都會統計；宜蘭成交屋齡分布、外地（非宜蘭籍）買家占比、2025 年底民宿家數、宜蘭裝修市場規模；台北市信義區層級數據（本輪未搜尋）。

---

## 8. 12 市場橫向比較表

（各數字之 URL 見 §2–§7 對應列；「無資料」＝本輪未找到；R 指標見 §5）

| 市場 | 人均 GDP 2026（USD） | 65+（2025） | 住宅存量 | 30 年以上占比 | 自有率 | 空屋率 | 2025 住宅交易 | 中古占比 | 新完工／推案 2025 | 2026 循環位置 | 房貸利率 2026 | 家庭負債／GDP | 政策修繕融資 | R |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 日本 | 35,703 | 29.5%（2026） | 6,505 萬戶（2023） | ≥21%（築 43 年以上） | 60.9% | 13.8% | 首都圈中古公寓 37,222（2024） | ≈62%（首都圈） | 著工 740,667（−6.5%） | 升息（1.25%）、新建創低 | 變動型待 2027-04 反映 | 61.1% | 子育てグリーン ≤60 萬円 | 0.53–0.69 |
| 南韓 | 37,412 | 21.4%（2026） | 2,018 萬戶（2025） | 30.6% | 61.4%（保有）／58.4%（自住） | 無資料 | 726,111（+13.0%） | ≈59%（代理） | 完工 ≈30 萬（−33%） | 升息（3.00%）、信貸限額、未售 6.9 萬 | 4.66% | 88.6% | 그린리모델링 利息補貼 4.5–5.5% | 0.58 |
| 新加坡 | 107,758 | 無資料 | 無資料（組屋居民 76%） | ≈45%（HIP 代理） | 組屋居民 90% | 私宅 6.4%（2026Q2） | HDB 轉售 26,169＋私宅 26,492 | ≈55%（代理） | BTO 19,723；私宅完工 6,123 | HDB 價 +2.9%、量五年低 | 裝修貸 3.5–6% | 無資料 | HIP S$4.07 億／年；銀行裝修貸 ≤S$3 萬 | 0.72 |
| 香港 | 59,640 | 25.0% | 3,047 千伙（2025-03） | 私樓 48–64% | 50.9% | 私樓 4.3% | 62,832 宗 | 66% | 落成 19,370 | 撤辣後回升，CCL 160.1 | H 按 ≈3.25% | 87.8% | 長者維修津貼 ≤HK$8 萬 | 0.80 |
| 台灣 | 42,103 | ≈20% | ≈934–940 萬宅【示意】 | 59% | 83.95%（2025） | 9.79%（低度用電） | 261,308 棟（−25.5%） | ≈50%（代理） | 使照 ≈143,000 宅（新高） | 量縮、管制微鬆（第二戶 7 成） | ≈2.29%；青安 1.775% | 無資料 | 修繕貸款補貼 ≤NT$80 萬；老宅延壽 | 0.74 |
| 中國大陸 | 14,874 | 無資料 | 城鎮 3.74 億套（2023） | ≈35%（2000 年前） | 無資料 | 無資料 | 30 城二手 174 萬套 | 50.4%（2026H1） | 住宅竣工 −20.2% | 新房 −11.6%（2026H1）、二手過半 | 無資料 | 58.0% | 以舊換新貸 ≤50 萬元（城商行） | 0.53 |
| 馬來西亞 | 15,085 | 8.1%（2024） | 1,090 萬戶（2025） | 無資料 | 78.0% | 無資料 | 住宅 ≈25.6 萬宗（全物業 416,413） | ≈61%（代理） | 完工 99,877 | HPI +2.6%、overhang 32,801 | SBR 2.75%＋加碼 | 69.8% | Maybank MyDeco ≤RM25 萬 | 0.55 ◇ |
| 泰國 | 8,105 | 16.0% | 無資料（≥10 年 >2,340 萬戶） | 無資料 | 無資料 | 全國空屋 164 萬 | 316,214（−9.1%） | 64–67% | BKK 公寓推案 THB 772 億（−41%） | 刺激反彈（2026H1 +17.6%） | GHB 政策貸 1% | 87.5% | GHB 修繕貸 ≤THB 30 萬 | 0.51 ◇ |
| 越南 | 5,115 | 9.5% | 無資料 | 無資料 | 無資料 | 無資料 | 579,718（含土地） | ≈36%（代理） | 商品房 29,901＋社宅 102,633 | 量升價漲、利率高 | 優惠 8–10%→13–15% | 無資料 | VBSP 4.8% | 0.29 ◇ |
| 印尼 | 5,362 | 7.3%（2024） | 無資料（backlog 929 萬戶） | 無資料 | 85.07% | 無資料 | 無資料（2026Q1 一級 −25.67%） | 無資料 | FLPP 278,868 戶 | 降溫、升息（5.75%） | 無資料 | 無資料 | FLPP；Gradana ≤Rp 20 億 | 不計算 |
| 菲律賓 | 4,443 | 5.8%（2021 估） | 2,850 萬單位（2020） | 無資料 | 無資料 | 無資料 | 無資料（Pag-IBIG 90,727 戶） | 無資料 | 4PH 7,056 戶 | 無資料 | Pag-IBIG 5.75% 起／3% | 無資料 | Pag-IBIG ≤PHP 600 萬（含修繕） | 不計算 |
| 印度 | 2,813 | 6.8%（2021 估） | 無資料 | 無資料 | 無資料 | 無資料 | 七大城 2026Q3 100,220 | 無資料 | 七大城推案 114,320（2026Q3） | 價升 +7%、庫存 63.1 萬 | 7.00–8.45% | 無資料 | 無獨立修繕補助（未驗證） | 不計算 |

---

## 9. 關鍵數字總表

| 指標 | 數值 | 年份 | 來源 | 定義／備註 | 信心 |
|---|---|---|---|---|---|
| 人均 GDP 名目（12 市場） | SG 107,758／HK 59,640／TW 42,103／KR 37,412／JP 35,703／MY 15,085／CN 14,874／TH 8,105／ID 5,362／VN 5,115／PH 4,443／IN 2,813 USD | 2026F | [Worldometer（IMF WEO 2026-04）](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal) | IMF 投影；印度為會計年度 | 高 |
| 65+ 占比 | JP 29.5%（2026-04）；HK 25.0%（2025）；KR 21.4%（2026）；TH 16.0%（2025）；VN 9.5%；MY 8.1%（2024）；ID 7.3%（2024） | 2024–26 | [demographer.org](https://demographer.org/countries/japan-demographics/)；[HK Economy](https://www.hkeconomy.gov.hk/en/pdf/box-25q4-6-1.pdf)；[populationpyramids.org](https://www.populationpyramids.org/south-korea)；[The Star](https://www.thestar.com.my/news/nation/2026/07/07/one-in-10-malaysians-will-be-aged-65-and-above-by-2035) | 混合官方與 WPP 口徑 | 中–高 |
| 日本住宅總數／空屋 | 6,505 萬戶／900 萬戶／13.8% | 2023-10 | [data-max](https://data-max.co.jp/article/70863) | 住宅・土地統計調査 | 高 |
| 日本 1980 年以前住宅 | 1,181 萬戶（約 21%），持ち家 866 萬 | 2023 | [国交省](https://www.mlit.go.jp/jutakukentiku/house/content/001857617.pdf) | 居住世帯あり | 高 |
| 日本持ち家率／1 住宅面積 | 60.9%／90.86 m² | 2023 | [money-bu-jpx](https://money-bu-jpx.com/news/article057251/)；[総務省](https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf) | — | 中–高 |
| 日本新設住宅著工 | 740,667 戶（−6.5%） | 2025 | [arc-navi](https://www.arc-navi.shikaku.co.jp/column/details.php?column_id=5205) | 国交省 建築着工統計 | 高 |
| 日銀政策金利 | 1.25% | 2026-09-18 | [NHK](https://news.web.nhk/newsweb/na/nd-20260918de50968) | 1995 年以來最高 | 高 |
| 南韓總住宅／30 年以上 | 2,018 萬戶／618 萬戶（30.6%）；公寓 65.8% | 2025 | [KDI 轉載](https://eiec.kdi.re.kr/policy/materialView.do?num=284799) | 人口住宅總普查 | 中–高 |
| 南韓自有率 | 保有 61.4%／自住 58.4%；1 人 36.0 m² | 2024 | [KDI 轉載](https://eiec.kdi.re.kr/policy/materialView.do?num=273475) | 주거실태조사 | 高 |
| 南韓住宅買賣／完工 | 726,111 件（+13.0%）／約 30 萬戶 | 2025 | [M이코노미](https://www.m-economynews.com/news/article.html?no=64226)；[헤럴드경제](https://biz.heraldcorp.com/article/10887737) | 국토부 | 高 |
| 南韓未售 | 69,134 戶 | 2026-08 | [뉴데일리](https://biz.newdaily.co.kr/site/data/html/2026/09/30/2026093000005.html) | 미분양 | 高 |
| 韓銀基準利率／房貸 | 3.00%／4.66% | 2026-08 | [한국금융신문](https://www.fntimes.com/html/view.php?ud=202608271107018117179ad43907_18)；[한국일보](https://www.hankookilbo.com/news/article/A2026093010490005879) | 新承做加權 | 高 |
| 新加坡 HDB 轉售／價格 | 26,169 筆（−9.7%）／+2.9% | 2025 | [EdgeProp](https://www.edgeprop.sg/property-news/hdb-resale-prices-plateaued-4q2025-transactions-sink-five-year-low) | HDB | 高 |
| 新加坡私宅 | 交易 26,492、新售 10,611、完工 6,123、未售 16,193 | 2025 | [ERA（URA）](https://www.era.com.sg/research-articles/4q-2025-ura-private-quarterly-report) | 不含 EC | 高 |
| 新加坡 HIP | 2025 批次 29,000 戶／S$4.07 億；累計 49.4 萬戶 | 2025 | [AsiaOne](https://www.asiaone.com/singapore/govt-allocates-over-407m-upgrading-works-29000-hdb-flats-home-improvement-programme)；[99.co](https://www.99.co/singapore/insider/hdb-home-improvement-programme-2025/) | 1997 年前建成 | 高 |
| 新加坡裝修貸上限 | S$30,000 或 6 倍月薪 | 2026 | [MoneySmart](https://www.moneysmart.sg/personal-loan/how-much-can-you-borrow-for-a-renovation-loan-in-singapore-ms) | 銀行政策 | 高 |
| 香港住宅存量 | 3,047 千伙（公 1,328／私 1,719） | 2025-03 | [HIF2025](https://www.hb.gov.hk/eng/publications/housing/HIF2025.pdf) | 房屋局 | 高 |
| 香港自置居所比率 | 50.9% | 2025 | [TradingEconomics（C&SD）](https://tradingeconomics.com/hong-kong/home-ownership-rate) | 住戶比 | 中 |
| 香港住宅買賣 | 62,832 宗；一手 20,525／二手 39,821 | 2025 | [hket（中原）](https://ps.hket.com/article/4204187/%E4%B8%AD%E5%8E%9F%EF%BC%9A9%E6%9C%88%E6%95%B4%E9%AB%94%E8%B2%B7%E8%B3%A3%E5%AE%97%E6%95%B8%E5%9B%9E%E5%8D%87%E9%80%BE1%E6%88%90%C2%A0%C2%A0%E4%B8%80%E6%89%8B%E7%A7%81%E6%A8%93%E9%87%8D%E4%B8%8A%E9%80%BE%E5%8D%83%E5%AE%97) | 土地註冊處登記 | 中–高 |
| 香港私樓空置 | 56,080 伙（4.3%） | 2025 末 | [RVD](https://www.rvd.gov.hk/doc/tc/HKPR2026_Preliminary_Findings_TC.pdf) | 差估署 | 高 |
| 台灣 30 年以上住宅 | 5,545,854 宅（59%）；平均 34.1 年 | 2025Q2 | [Newtalk](https://newtalk.tw/news/view/2025-09-17/994199) | 房屋稅籍 | 高 |
| 台灣低度使用住宅 | 914,196 宅（9.79%） | 2024H2 | [經濟日報](https://money.udn.com/money/story/5621/8909453) | 用電 ≤60 度 | 高 |
| 台灣自有率 | 84.4%（2024）→83.95%（2025） | 2024–25 | [主計總處](https://ws.dgbas.gov.tw/001/Upload/466/ebook/ebook_341889/pdf/full.pdf)；[經濟日報](https://money.udn.com/money/story/5621/9708202) | 家庭收支調查 | 高 |
| 台灣買賣移轉 | 261,308 棟（−25.5%） | 2025 | [中央社](https://www.cna.com.tw/news/aipl/202606200029.aspx) | 內政部 | 高 |
| 台灣住宅使照 | ≈143,000 宅 | 2025 | [經濟日報](https://money.udn.com/money/story/5621/9324984) | 1997 年以來新高 | 中 |
| 台灣五大銀行房貸利率 | ≈2.29% | 2026-07 | [money101](https://www.money101.com.tw/blog/%E6%88%BF%E8%B2%B8%E5%88%A9%E7%8E%87) | 央行統計轉引 | 中 |
| 台灣第二戶貸款成數 | 5→6 成（2026-03-20）→7 成（2026Q3） | 2026 | [money101](https://www.money101.com.tw/blog/%E6%88%BF%E8%B2%B8%E5%88%A9%E7%8E%87)；[經濟日報](https://money.udn.com/money/story/122376/9518079) | 央行選擇性信用管制 | 中 |
| 台灣修繕貸款補貼 | ≤NT$80 萬；自購＋修繕 6,000 戶 | 2026（115 年度） | [今周刊](https://www.businesstoday.com.tw/article/category/183030/post/202609150009/) | 內政部 | 高 |
| 青安 3.0 | 2026-08-01 起；前 3 年 1.775% | 2026 | [房感](https://www.housefeel.com.tw/article/%E9%9D%92%E5%B9%B4-%E9%A6%96%E8%B3%BC-%E8%B2%B8%E6%AC%BE-%E8%B3%BC%E5%B1%8B%E8%B2%B8%E6%AC%BE-%E5%AE%89%E5%BF%83%E6%88%90%E5%AE%B6%E8%B2%B8%E6%AC%BE/) | 一段式機動 | 中 |
| 宜蘭買賣移轉／房價指數 | 約 5,270 棟（−23.6%）／178.63（−0.81%） | 2025 | [94m](https://94m.com.tw/articles/c049ff) | 引內政部 | 中 |
| 宜蘭民宿 | 2,177 家／8,085 房（全台第一） | 2025-05 | [公視](https://news.pts.org.tw/article/803305) | 觀光署統計 | 中 |
| 中國二手房占比 | 50.4%（2026H1）；52.4%（1–8 月） | 2026 | [21 財經](https://m.21jingji.com/article/20260729/herald/df3b446d915832c3dab62856c9bf0024.html)；[szhome（中指）](http://news.szhome.com/394159.html) | 住建部 | 高 |
| 中國新建商品房銷售 | 4.01 億 m²（−11.6%）；待售 7.63 億 m² | 2026H1 | [網易（統計局）](https://www.163.com/dy/article/L1SOIAQS05159A0N.html) | 國家統計局 | 高 |
| 中國 2000 年前建成住房 | 約 35%（全國，推算）；上海 50.38% | 2020 | [騰訊](https://news.qq.com/rain/a/20220628A0BO3R00) | 七普年鑑 | 中 |
| 馬來西亞交易 | 416,413 宗／RM 2,418.7 億（+4.1%） | 2025 | [Hartamas](https://hartamas.com/malaysia-property-market-2025-what-the-napic-data-really-shows/) | NAPIC PMR 2025 | 高 |
| 馬來西亞住宅存量 | 1,090 萬戶；有地 73.1% | 2025 | [FMT（DOSM）](https://www.freemalaysiatoday.com/category/nation/2026/04/23/malaysian-housing-units-reached-10-9mil-in-2025-says-statistics-dept) | DOSM | 高 |
| 馬來西亞 overhang | 32,801 戶 | 2026Q1 | [IQI](https://iqiglobal.com/blog/napic-q1-2026/) | NAPIC | 中–高 |
| 泰國住宅移轉 | 316,214 戶（−9.1%）；2026H1 167,665（+17.6%） | 2025–26 | [LINE（REIC）](https://today.line.me/th/v3/article/2D7qOkO)；[Thai Press](https://www.thethaipress.com/2026/169482) | REIC | 高 |
| 泰國中古占比 | 64%（2025 底）／67%（2026Q1） | 2025–26 | [Bangkok Post](https://www.bangkokpost.com/property/3266023/resale-homes-take-larger-market-share)；[REIC 277](https://reic.or.th/Activities/PressRelease/277) | 移轉戶數 | 高 |
| 泰國 LTV／規費優惠 | LTV 100%、規費 0.01% 延至 2027-06-30 | 2026 | [Thansettakij](https://www.thansettakij.com/economy/659052)；[Khaosod](https://www.khaosod.co.th/economics/news_10244535) | BoT／內閣 | 高 |
| 越南成交 | 579,718 筆（+7.7%）；公寓＋獨立屋 138,025 | 2025 | [Tạp chí KTTC](https://tapchikinhtetaichinh.vn/thi-truong-bat-dong-san-quy-iv-va-ca-nam-2025-nguon-cung-tang-giao-dich-soi-dong-140788.html) | Bộ Xây dựng | 高 |
| 越南庫存 | 32,894 戶／地（24/34 省） | 2025Q4 | [Vietstock](https://vietstock.vn/2026/02/ton-kho-bat-dong-san-vuot-500-ngan-ty-737-1403221.htm) | 不完整涵蓋 | 中 |
| 印尼住房缺口 | 929 萬戶（12.39%） | 2026-03 | [Tirto（BPS）](https://tirto.id/bps-jumlah-backlog-perumahan-capai-929-juta-rumah-tangga-hBfe) | Susenas backlog 1 | 高 |
| 印尼自有率 | 85.07% | 2025 | [BPS 表](https://www.bps.go.id/id/statistics-table/2/ODQ5IzI=/persentase-rumah-tangga-menurut-provinsi-dan-status-kepemilikan-bangunan-tempat-tinggal-yang-ditempati-milik-sendiri.html) | Susenas | 中 |
| 印尼 BI Rate | 5.75% | 2026-09 | [Bisnis](https://finansial.bisnis.com/read/20260923/11/2006538/alasan-bank-indonesia-tahan-bi-rate-september-2026-di-575) | — | 高 |
| 菲律賓 Pag-IBIG 房貸 | PHP 1,405.4 億／90,727 戶 | 2025 | [Manila Standard](https://manilastandard.net/business/314693903/pag-ibig-housing-loans-rose-8-to-record-p140-54-billion-in-2025.html) | 含修繕用途 | 高 |
| 印度七大城未售／銷售 | 63.1 萬戶／100,220 戶（Q3） | 2026Q3 | [Storyboard18（Anarock）](https://www.storyboard18.com/amp/how-it-works/mmr-bengaluru-drive-q3-housing-sales-as-it-grows-10-qoq-3-yoy-anarock-ws-lo-111529.htm) | 顧問統計 | 中 |
| 家庭負債／GDP（BIS） | KR 88.6／HK 87.8／TH 87.5／MY 69.8／JP 61.1／CN 58.0 | 2025-12 | [TradingEconomics](https://tradingeconomics.com/country-list/households-debt-to-gdp?continent=asia) | BIS 非金融部門 | 高 |

---

## 10. 對台灣業者（室內裝修＋不動產＋家居零售集團）的啟示

1. **台灣是全區「翻修結構最成熟、貨幣化最不足」的市場**：R 指標 0.74 僅次於香港，但 T1 校準之翻修支出占 GDP（0.69–1.89%）低於日、韓（1.1–1.4%）。以日本單價套算，台灣老屋翻修的「應有」規模約 GDP 1.0–1.4%（NT$2,900–4,100 億）【示意】，集團應把 59% 的 30 年以上存量（554.6 萬宅）視為主戰場，而非只追逐 14.3 萬宅的新屋交屋。
2. **獲客通路要綁定「換手」而非「交屋」**：香港二手占 66%、泰國 64–67%、中國 50.4%、台灣約 50%，各市場的成功案例（中原按揭 × 好師傅、RHB × The Makeover Guys 120% 購屋＋裝修貸、日本リノベる一站式中古＋翻新）都是把裝修嵌入仲介／按揭流程；集團旗下不動產事業可直接複製「成交即裝修」的交叉銷售。
3. **政策融資是台灣相對優勢，但額度偏小**：修繕貸款利息補貼 ≤NT$80 萬（6,000 戶）＋老宅延壽（戶內 ≤20 萬）只能覆蓋全室翻新的 15–40%；可設計「補貼＋銀行裝修貸＋分期」的套裝並代辦申請（新加坡 S$3 萬上限、馬來西亞 RM25 萬的產品設計可參考），把 9/1–9/30 的申請季變成年度行銷節點。
4. **高齡化改造是日、韓、港、台共同的下一波**：日本 65+ 29.5%、南韓 2035 年中位數 52 歲、香港 2046 年 36%、台灣約 20%；南韓 2026-03 重啟 그린리모델링 利息補貼（高齡者加碼至 5.5%）、新加坡 HIP 含長者友善選項、香港長者維修津貼 8 萬港元，台灣「老宅延壽」戶內補助對高齡弱勢加碼至 30 萬——集團可把「無障礙＋節能」做成標準化套餐，對接補助。
5. **利率循環決定 2026–2027 的訂單節奏**：日、韓、印尼、印度升息，台灣房貸 2.29% 仍屬全區最低且管制微鬆（第二戶 7 成、青安 3.0），但 2026Q1 五大銀行新增房貸年減 26%、預售解約升溫（宜蘭全國第五），新屋交屋裝修有遞延風險；老屋翻新（自有率 84%、多無貸款）反而是利率免疫的現金流。
6. **宜蘭本地的三條線**：（a）電梯大樓交易占比 43.5% 首度超越透天——新成屋輕裝修套餐；（b）透天與老屋——全室翻新；（c）民宿 2,177 家全台第一、非法民宿裁罰金額居首——「合法化改裝」（消防、無障礙、用途變更）與民宿翻新是可被政策推動的 B2B 需求。宜蘭成交屋齡與外地買家數據缺口建議以集團自有成交資料補足。
7. **東南亞／印度的進入點是「交屋裝修」而非「翻修」**：越南 2025 年公寓＋獨立屋成交 138,025（>75% 買家已有一戶、投資客延後裝修）、印尼 FLPP 27.9 萬戶（99.99% 透天）、菲律賓 Pag-IBIG 9 萬戶、印度七大城年推案 >40 萬戶；若集團家居零售／模組化產品要出海，應以建商 B2B（毛胚交屋 → 基礎裝修包）為主，且注意越南 13–15% 房貸、印尼 5.75% 政策利率對買氣的壓抑。
8. **資料治理**：各市場「新／中古分拆」「屋齡分布」「翻修週期」多數無官方統計（§11），集團若能以自有成交與裝修案件建立「屋齡 × 交易 × 裝修單價」資料庫，本身就是不動產與裝修事業的決策資產，也可對外發布成為業界指標（如中原 CCL、REIC 之於裝修）。

---

## 11. 資料缺口

1. **第一輪摘要中無法重新取得 URL 而移除的數字**：日本首都圈 2025 年中古成約 49,114 件（+31.9%）；南韓 2026 年入住量 17.2–18.3 萬戶；中國 5 年期 LPR 3.5%、宏觀槓桿率 302.4%、房貸餘額連續 11 季負成長；台灣家庭負債／GDP 94.3%（CEIC 2024）；泰國中古占比 60%（顧問估）；印度 2025 年七大城銷售 395,625 戶、未售 576,617 戶；香港 2026-03 樓價、日本變動型房貸 10 月調升 0.19–0.60pp。
2. **總經與人口**：中、馬、泰、印尼、菲、印之 IMF PPP 人均 GDP；UN WPP 2024 之 2035 年 65+ 占比（12 市場）；台、日、韓、中 World Bank 都市化率；新加坡、中國、台灣 65+ 精確值；家戶數與戶量（10 市場）。
3. **存量與屋齡**：日本 30 年以上占比；南韓 2025 普查空屋；新加坡 HDB 組屋總數、全國自有率、平均面積；香港 48% vs 64% 口徑；台灣公寓 vs 透天、平均坪數；中國自有率、空置率、人均面積；馬、泰、越、印尼、菲、印屋齡分布與平均面積；泰、越、菲、印自有率。
4. **交易與供給**：南韓新／中古分拆與 2026 入住量；新加坡 2025 降溫措施（SSD）與私宅轉售全年量；台灣全國房價指數 2026、新／中古官方分拆；中國全國二手套數、限購放鬆細節、LPR；印度 2025 全年；印尼、菲律賓全國交易與完工；越南《土地法》2024 生效細節；日、中、泰、印尼、菲官方未售庫存。
5. **融資**：台、星、越、印尼、菲、印 BIS 家庭負債；中國房貸利率 2026；日本リフォームローン；各市場銀行裝修貸平均金額與筆數；台灣修繕補貼專屬利率與核定戶數；印度 home improvement loan 與 PMAY 驗證。
6. **都會與宜蘭**：香港分區、菲律賓都會、印尼全國交易；宜蘭成交屋齡分布、外地買家占比、2025 年底民宿家數、裝修市場規模；台北市信義區層級數據。
7. **翻修週期與轉化率**：除中國（華泰 10–20 年）與泰國（SCB EIC 調查）外，各市場皆無「屋齡 → 翻修」轉化率調查，指標 R 無法校準為金額。

---

## 12. 來源清單（標題｜機構｜年份｜URL）

| # | 標題 | 機構 | 年份 | URL |
|---|---|---|---|---|
| 1 | GDP per Capita in Asia (2026) – IMF | Worldometer | 2026 | https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal |
| 2 | GDP per Capita in Asia (2025) – IMF | Worldometer | 2025 | https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal |
| 3 | World Economic Outlook, April 2026 – Statistical Appendix | IMF | 2026 | https://www.imf.org/-/media/files/publications/weo/2026/april/english/statsappendix.pdf |
| 4 | List of Asian countries by GDP (PPP) per capita | Wikipedia（IMF） | 2026 | https://en.wikipedia.org/wiki/List_of_Asian_countries_by_GDP_(PPP)_per_capita |
| 5 | Japan Demographics（総務省推計） | demographer.org | 2026 | https://demographer.org/countries/japan-demographics/ |
| 6 | Box 6.1 Population ageing（2025 Economic Background） | HK Economy | 2026 | https://www.hkeconomy.gov.hk/en/pdf/box-25q4-6-1.pdf |
| 7 | One in 10 Malaysians will be aged 65+ by 2035 | The Star | 2026 | https://www.thestar.com.my/news/nation/2026/07/07/one-in-10-malaysians-will-be-aged-65-and-above-by-2035 |
| 8 | 2024 POPCEN population counts | PSA | 2025 | https://psa.gov.ph/content/2024-census-population-popcen-population-counts-declared-official-president |
| 9 | GDP năm 2025 tăng 8,02%, bình quân đầu người 5.026 USD | Báo Chính phủ | 2026 | https://baochinhphu.vn/gdp-nam-2025-tang-truong-802-binh-quan-dau-nguoi-dat-5026-usd-102260105152509472.htm |
| 10 | 空き家数が過去最高の 900 万戸 | データ・マックス | 2024 | https://data-max.co.jp/article/70863 |
| 11 | 令和５年住宅・土地統計調査 住宅及び世帯に関する基本集計 | 総務省統計局 | 2024 | https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf |
| 12 | 住宅のあるべき姿に関する論点（データ集） | 国土交通省 | 2025 | https://www.mlit.go.jp/jutakukentiku/house/content/001857617.pdf |
| 13 | 2023 年住宅・土地統計調査 住宅数概数集計結果 | 大和不動産鑑定 | 2024 | https://daiwakantei.co.jp/wp/uploads/2024/05/2b82434b2bb8f09ae7298f31fddc5cfb.pdf |
| 14 | 東京都 住宅・土地統計調査 結果の概要 | 東京都 | 2024 | https://www.toukei.metro.tokyo.lg.jp/jyutaku/2023/jt23tgaiyou.pdf |
| 15 | 世間の持ち家比率は？ | money-bu-jpx | 2025 | https://money-bu-jpx.com/news/article057251/ |
| 16 | 2025年新設住宅着工戸数74万戸、62年ぶり過去最低水準 | arc-navi（資格の大原） | 2026 | https://www.arc-navi.shikaku.co.jp/column/details.php?column_id=5205 |
| 17 | 国土交通省、2025年住宅着工74万戸 | BuildApp News | 2026 | https://news.build-app.jp/article/39533/ |
| 18 | 日銀 利上げ決定 政策金利1.25％程度へ | NHK | 2026 | https://news.web.nhk/newsweb/na/nd-20260918de50968 |
| 19 | 日銀追加利上げで住宅ローンはいつ上がる？ | モゲチェック | 2026 | https://mogecheck.jp/articles/show/pnl6ZzOV4BDR2k5Ra7PY |
| 20 | 首都圏中古マンション成約 vs 新築供給 | DIME | 2025 | https://dime.jp/genre/1990629/ |
| 21 | 2025년 인구주택총조사 결과 | 국가데이터처（KDI 轉載） | 2026 | https://eiec.kdi.re.kr/policy/materialView.do?num=284799 |
| 22 | 2024년도 주거실태조사 결과 | 국토교통부（KDI 轉載） | 2025 | https://eiec.kdi.re.kr/policy/materialView.do?num=273475 |
| 23 | 전국 아파트 5채 중 1채 30년 초과 | 한국경제（부동산R114） | 2025 | https://www.hankyung.com/article/2025061796206 |
| 24 | 국토부 12월 주택통계（거래 726,111건） | M이코노미뉴스 | 2026 | https://www.m-economynews.com/news/article.html?no=64226 |
| 25 | 2025년 주택 준공 확정치 | 헤럴드경제 | 2026 | https://biz.heraldcorp.com/article/10887737 |
| 26 | 한은 금통위, 기준금리 연 3%로 연속 인상 | 한국금융신문 | 2026 | https://www.fntimes.com/html/view.php?ud=202608271107018117179ad43907_18 |
| 27 | 주담대 금리 4.66% 3년 9개월 만에 최고 | 한국일보 | 2026 | https://www.hankookilbo.com/news/article/A2026093010490005879 |
| 28 | 전국 미분양 주택 6만9134가구 | 뉴데일리 | 2026 | https://biz.newdaily.co.kr/site/data/html/2026/09/30/2026093000005.html |
| 29 | [10·15 부동산대책] 규제지역 늘리고 대출한도 줄이다 | 뉴스핌 | 2025 | https://www.newspim.com/news/view/20251015000279 |
| 30 | 10·15 부동산 대책 Q&A | 경향신문 | 2025 | https://www.khan.co.kr/article/202510151656001 |
| 31 | 30대·수도권 주담대 꺾였다 | 머니투데이 | 2026 | https://www.mt.co.kr/economy/2026/02/24/2026022411382531015 |
| 32 | 민간건축물 그린리모델링 이자지원 재개 | 대한민국 정책브리핑 | 2026 | https://www.korea.kr/news/policyNewsView.do?newsId=148960908 |
| 33 | HDB Annual Report 2024/2025 Key Statistics | HDB | 2025 | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB_Key-Statistics-2025.pdf |
| 34 | HDB Sustainability Report 2023/2024 | HDB | 2024 | https://www.hdb.gov.sg/-/media/hdb-pulse/reports/annual-reports-and-financial-statements/HDB-SR-FY23.pdf |
| 35 | HDB resale prices plateaued in 4Q2025 | EdgeProp | 2026 | https://www.edgeprop.sg/property-news/hdb-resale-prices-plateaued-4q2025-transactions-sink-five-year-low |
| 36 | 4Q 2025 URA Private Quarterly Report | ERA | 2026 | https://www.era.com.sg/research-articles/4q-2025-ura-private-quarterly-report |
| 37 | Singapore Residential Property Market Analysis 2026 | Global Property Guide | 2026 | https://www.globalpropertyguide.com/asia/singapore/price-history |
| 38 | Govt allocates over $407m to HIP for 29,000 flats | AsiaOne | 2025 | https://www.asiaone.com/singapore/govt-allocates-over-407m-upgrading-works-29000-hdb-flats-home-improvement-programme |
| 39 | HDB Home Improvement Programme 2025 | 99.co | 2025 | https://www.99.co/singapore/insider/hdb-home-improvement-programme-2025/ |
| 40 | How much can you borrow for a renovation loan | MoneySmart | n.d. | https://www.moneysmart.sg/personal-loan/how-much-can-you-borrow-for-a-renovation-loan-in-singapore-ms |
| 41 | Housing in Figures 2025 | 香港房屋局 | 2025 | https://www.hb.gov.hk/eng/publications/housing/HIF2025.pdf |
| 42 | Hong Kong Home Ownership Rate | TradingEconomics（C&SD） | 2026 | https://tradingeconomics.com/hong-kong/home-ownership-rate |
| 43 | 香港物業報告 2026 初步統計 | 差餉物業估價署 | 2026 | https://www.rvd.gov.hk/doc/tc/HKPR2026_Preliminary_Findings_TC.pdf |
| 44 | 中原：9月整體買賣宗數回升逾1成（含 2025 全年數） | 香港經濟日報 | 2026 | https://ps.hket.com/article/4204187/ |
| 45 | 住宅樓宇買賣合約統計數字：一手及二手 | 土地註冊處 | 2026 | https://www.landreg.gov.hk/tc/monthly/agt-primary.htm |
| 46 | 中原城市領先指數 CCL | 中原地產 | 2026 | https://hk.centanet.com/CCI/index |
| 47 | 全港48%私樓樓齡滿30年 | HK01 | 2024 | https://www.hk01.com/%E7%A0%94%E6%95%B8%E6%89%80/1093926/ |
| 48 | 全台住宅平均屋齡 34.1 年、30 年以上 554.6 萬宅 | Newtalk | 2025 | https://newtalk.tw/news/view/2025-09-17/994199 |
| 49 | 空屋飆破91萬戶創高 | 經濟日報 | 2025 | https://money.udn.com/money/story/5621/8909453 |
| 50 | 113 年家庭收支調查報告 | 主計總處 | 2025 | https://ws.dgbas.gov.tw/001/Upload/466/ebook/ebook_341889/pdf/full.pdf |
| 51 | 住宅自有率探低 83.95% | 經濟日報 | 2026 | https://money.udn.com/money/story/5621/9708202 |
| 52 | 2025 年建物買賣移轉 261,308 棟 | 中央社（內政部） | 2026 | https://www.cna.com.tw/news/aipl/202606200029.aspx |
| 53 | 2025 全年住宅使照約 14.3 萬宅 | 經濟日報 | 2026 | https://money.udn.com/money/story/5621/9324984 |
| 54 | 2026 房貸利率比較（央行統計 2.29%） | Money101 | 2026 | https://www.money101.com.tw/blog/%E6%88%BF%E8%B2%B8%E5%88%A9%E7%8E%87 |
| 55 | 五大銀行房貸動能降溫 | 經濟日報 | 2026 | https://money.udn.com/money/story/122376/9518079 |
| 56 | 2026 住宅補貼限時申請（修繕貸款 80 萬） | 今周刊 | 2026 | https://www.businesstoday.com.tw/article/category/183030/post/202609150009/ |
| 57 | 青安 3.0 正式上路 | HouseFeel 房感 | 2026 | https://www.housefeel.com.tw/article/ |
| 58 | 老宅延壽機能復新計畫 | 內政部國土署 | 2025 | https://www.nlma.gov.tw/uploads/files/a5d37b464dc02a5814200514847f5c1a.pdf |
| 59 | 宜蘭、花蓮、台東 2025-2026 年房市 | 94m | 2026 | https://94m.com.tw/articles/c049ff |
| 60 | 宜蘭縣房價分析 2025 年實價登錄完整報告 | myhousing | 2026 | https://www.myhousing.com.tw/n/n02/n0203/n020301/269746/ |
| 61 | 宜蘭民宿 2,177 家、房間數破 8,000（觀光署） | 公視新聞 | 2025 | https://news.pts.org.tw/article/803305 |
| 62 | 114 年合法旅宿統計 | 工商時報 | 2026 | https://www.ctee.com.tw/news/20260111700312-431401 |
| 63 | 上半年二手房交易量超新房（住建部 50.4%） | 21 財經 | 2026 | https://m.21jingji.com/article/20260729/herald/df3b446d915832c3dab62856c9bf0024.html |
| 64 | 2026 年 1-6 月房地產數據解讀 | 網易（國家統計局） | 2026 | https://www.163.com/dy/article/L1SOIAQS05159A0N.html |
| 65 | 2026 年三季度中國房地產市場總結（中指） | 深圳房地產信息網 | 2026 | http://news.szhome.com/394159.html |
| 66 | 中國房齡大數據（人口普查年鑑） | 騰訊新聞 | 2022 | https://news.qq.com/rain/a/20220628A0BO3R00 |
| 67 | 《中國住房存量報告 2026》 | 搜狐（澤平宏觀） | 2026 | https://www.sohu.com/a/1032443179_120179484 |
| 68 | Malaysia Property Market 2025: NAPIC data | Hartamas | 2026 | https://hartamas.com/malaysia-property-market-2025-what-the-napic-data-really-shows/ |
| 69 | Malaysia Residential Property Market Analysis 2026 | Global Property Guide | 2026 | https://www.globalpropertyguide.com/asia/malaysia/price-history |
| 70 | NAPIC Q1 2026 | IQI Global | 2026 | https://iqiglobal.com/blog/napic-q1-2026/ |
| 71 | Malaysian housing units reached 10.9 mil in 2025 | FMT（DOSM） | 2026 | https://www.freemalaysiatoday.com/category/nation/2026/04/23/malaysian-housing-units-reached-10-9mil-in-2025-says-statistics-dept |
| 72 | Maybank MyDeco | Maybank | 2026 | https://www.maybank2u.com.my/maybank2u/malaysia/en/personal/loans/home/mydeco.page |
| 73 | The Makeover Guys × RHB Flexi Loan 120% | Malay Mail | 2026 | https://www.malaymail.com/news/money/mediaoutreach/2026/09/15/the-makeover-guys-and-rhb-bank-introduce-the-makeover-flexi-loan-with-up-to-120-financing-for-home-purchase-and-renovation/487671 |
| 74 | REIC 2025 住宅移轉 316,214 戶 | LINE Today（REIC） | 2026 | https://today.line.me/th/v3/article/2D7qOkO |
| 75 | Resale homes take larger market share | Bangkok Post | 2026 | https://www.bangkokpost.com/property/3266023/resale-homes-take-larger-market-share |
| 76 | 2026 上半年移轉 167,665 戶 | The Thai Press | 2026 | https://www.thethaipress.com/2026/169482 |
| 77 | แบงก์ชาติต่ออายุผ่อนเกณฑ์ LTV ถึง มิ.ย. 70 | Thansettakij | 2026 | https://www.thansettakij.com/economy/659052 |
| 78 | ธอส. สินเชื่อซ่อม-แต่ง 2026 | GH Bank | 2026 | https://www.ghbank.co.th/news/detail/public-relations/press-09-04-2026 |
| 79 | โจทย์ใหญ่หนี้ครัวเรือน | Thansettakij | 2025 | https://www.thansettakij.com/economy/645297 |
| 80 | Thị trường BĐS quý IV và cả năm 2025 | Tạp chí Kinh tế Tài chính | 2026 | https://tapchikinhtetaichinh.vn/thi-truong-bat-dong-san-quy-iv-va-ca-nam-2025-nguon-cung-tang-giao-dich-soi-dong-140788.html |
| 81 | Tồn kho bất động sản vượt 500 ngàn tỷ | Vietstock | 2026 | https://vietstock.vn/2026/02/ton-kho-bat-dong-san-vuot-500-ngan-ty-737-1403221.htm |
| 82 | Nguồn cung tăng, giá nhà chưa giảm | Báo Chính phủ | 2026 | https://baochinhphu.vn/nguon-cung-tang-gia-nha-chua-giam-102260117005432583.htm |
| 83 | Lãi suất vay mua nhà 2026 | Smartland | 2026 | https://smartland.vn/lai-suat-vay-mua-nha-2026/ |
| 84 | Điều kiện lãi suất vay VBSP mua nhà, sửa nhà | VNBA | 2026 | https://vnba.org.vn/vi/dieu-kien-lai-suat-vay-ngan-hang-chinh-sach-mua-nha-sua-nha-11963.htm |
| 85 | BPS: Backlog perumahan 9,29 juta | Tirto | 2026 | https://tirto.id/bps-jumlah-backlog-perumahan-capai-929-juta-rumah-tangga-hBfe |
| 86 | Persentase rumah tangga milik sendiri | BPS | 2025 | https://www.bps.go.id/id/statistics-table/2/ODQ5IzI=/ |
| 87 | Alasan BI tahan BI Rate September 2026 di 5,75% | Bisnis | 2026 | https://finansial.bisnis.com/read/20260923/11/2006538/alasan-bank-indonesia-tahan-bi-rate-september-2026-di-575 |
| 88 | Survei Harga Properti Residensial Q1 2026 | Bank Indonesia | 2026 | https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_289726.aspx |
| 89 | Penyaluran FLPP 2025 cetak rekor 278.868 unit | Media Indonesia | 2025 | https://mediaindonesia.com/ekonomi/845538/penyaluran-flpp-2025-cetak-rekor-tertinggi-tembus-278868-unit-rumah |
| 90 | Pag-IBIG housing loans rose 8% to P140.54B | Manila Standard | 2026 | https://manilastandard.net/business/314693903/pag-ibig-housing-loans-rose-8-to-record-p140-54-billion-in-2025.html |
| 91 | Pag-IBIG Housing Loan | Pag-IBIG Fund | 2025 | https://www.pagibigfund.gov.ph/HousingLoan.html |
| 92 | PHL housing crisis: 6.5 million reasons | BusinessMirror | 2025 | https://businessmirror.com.ph/2025/11/04/phls-housing-crisis-6-5-million-reasons-for-radical-action-now/ |
| 93 | Building better, affordable housing（PSA 2020） | BusinessWorld | 2024 | https://www.bworldonline.com/special-features/2024/10/24/630972/building-better-affordable-housing-for-filipino-families/ |
| 94 | MMR, Bengaluru drive Q3 housing sales（Anarock） | Storyboard18 | 2026 | https://www.storyboard18.com/amp/how-it-works/mmr-bengaluru-drive-q3-housing-sales-as-it-grows-10-qoq-3-yoy-anarock-ws-lo-111529.htm |
| 95 | Cheapest home loan rates October 2026 | Upstox | 2026 | https://upstox.com/news/personal-finance/latest-updates/cheapest-home-loan-rates-in-october-2026-12-lenders-offer-7-1-7-35-interest-emi-revisions-may-follow/article-201440/ |
| 96 | Households Debt to GDP – Asia | TradingEconomics（BIS） | 2026 | https://tradingeconomics.com/country-list/households-debt-to-gdp?continent=asia |
| 97 | Ranked: Countries with the highest debt-to-GDP（BIS Q4 2025） | Yahoo Finance | 2026 | https://finance.yahoo.com/economy/articles/ranked-countries-highest-debt-gdp-120507169.html |
| 98 | 重識建材之六：存量重裝崛起元年 | 華泰研究 | 2024 | https://reportify-1252068037.cos.ap-beijing.myqcloud.com/media/production/s_2d023dd8_2d023dd8457c351583068e0e7510101b.pdf |
| 99 | T1 市場規模校準（§5.2） | 本專案 | 2026 | ./T1-market-size-reconciliation.md |
| 100 | 各國驗證檔（CN／KR／TW） | 本專案 | 2026 | ../verification/ |

（其餘單次引用之 URL 已在各節內文附上，共約 140 個不重複網址。）
