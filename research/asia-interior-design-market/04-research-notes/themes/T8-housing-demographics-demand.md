# T8：住宅存量、人口結構與不動產連動（需求引擎）（Housing stock, demographics and real-estate linkage: the renovation demand engine）

研究日期：2026-10-08（本版為「已執行網路搜尋」之覆寫版，取代同路徑之純繼承資料草稿）｜涵蓋市場：日本、南韓、新加坡、香港、台灣、中國大陸、馬來西亞、泰國、越南、印尼、菲律賓、印度（12 市場）

> **研究方法備註（務必先讀）**
> - 本輪共執行 **20 次 WebSearch**（英、日、韓、中、泰、越、印尼文各若干），環境禁止 WebFetch／curl，所有數字皆取自搜尋結果摘要中可辨識的原文引述；每個數字均附 URL。另沿用本專案既有筆記（`countries/*`、`themes/T1`、`verification/*`）中已附 URL 的數字，以「（既有筆記）」標示。
> - 標示：**【官方】**＝統計局／央行／部會／立法機關原始發布或其直接轉載；**【業界／媒體】**＝研究機構、仲介、銀行、媒體整理（口徑一律記錄）；**【示意】**＝本人以已引用數字推算或假設，非來源數字；**無資料**＝本輪未找到，列入 §11 缺口，不以估計填補。
> - 匯率：沿用 T1 檔之「2025–2026 概略參考匯率」，整合時以當日官方匯率覆寫：USD/TWD 31.5；USD/JPY 150；USD/KRW 1,400；USD/CNY 7.20；USD/SGD 1.33；USD/HKD 7.80；USD/MYR 4.40；USD/THB 33；USD/VND 26,000；USD/IDR 16,000；USD/PHP 57；USD/INR 86。所有 USD／TWD 換算皆為本人計算。
> - 信心等級：高＝官方原始值或 ≥2 獨立來源一致；中＝單一官方轉載或單一研究機構；低＝部落格／聚合站／本人推算。

---

## 1. 摘要

1. 十二市場的翻修需求引擎可分三型：**「老化存量型」**（日本、台灣、香港、南韓、新加坡）——人均 GDP（IMF WEO 2026 年 4 月，2026 年名目）USD 35,703–107,758、65 歲以上占 20–30%、30 年以上住宅占比台灣 59%（2025Q2）、南韓 30.6%（2025 普查）、香港私樓樓宇 48–64% 樓齡滿 30 年，且中古交易占住宅交易比重已達 40–79%；**「新建交屋型」**（越南、印尼、菲律賓、印度、馬來西亞）——65 歲以上僅 6–10%、都市化 35–76%、住房缺口（印尼 929 萬戶、2026 年 3 月）與新案推案（印度七大城 2025 年 41.9 萬戶）主導，裝修需求來自毛胚／基本完成新屋；**「過渡型」**（中國大陸、泰國）——新房銷售連年負成長，二手房已占 50.4%（中國 2026 上半年）／約 60%（泰國，顧問估計），政策仍以去化新屋為主。
2. 台灣是全區「存量最老、交易最冷、新屋完工卻創高」的罕見組合：房屋稅籍住宅平均屋齡 34.1 年、30 年以上 554.6 萬宅（59%）；2025 年建物買賣移轉 261,308 棟（−25.5%）但住宅使照約 14.3 萬宅；央行第七波信用管制自 2026-03-19 起首次微鬆（第二戶 5→6 成），2026-09-18 再升至 7 成，五大銀行新承做房貸利率 2.29%（2026-07），青安 3.0 自 2026-08-01 實施（最高 1,500 萬、40 年、1.775%）。
3. 東北亞進入「新建創低、中古創高、利率反轉」：日本 2025 年新設住宅著工 740,667 戶（−6.5%，62 年來最低）、首都圈中古公寓成約 49,114 件（+31.9%，三年連增），但日銀 2026 年 6 月與 9 月連續升息至 1.25%，變動型房貸 10 月起調升 0.19–0.60 個百分點，2026 年 4–7 月中古成約連續四個月年減；南韓 2025 年住宅買賣 726,111 件（+13.0%）、2026 年入住量降至 17.2–18.3 萬戶（13 年最低）、未售（미분양）6.9 萬戶、韓銀基準利率 2026-08 升至 3.00%、五大銀行混合型房貸 4.89–7.29%；中國 5 年期 LPR 3.5% 已 16 個月未動、2026 上半年二手房占比 50.4% 首次過半、宏觀槓桿率 302.4%（2025）而房貸連續 11 季負成長。
4. 東南亞與印度的循環位置分歧：泰國 2025 年住宅移轉 316,214 戶（−9.1%）後，LTV 100% 與移轉費 0.01% 優惠延長至 2027-06-30，2026 上半年低層住宅移轉 +14.6%；馬來西亞 2025 年全物業交易 416,413 宗（RM 2,418.7 億，+4.1%）但住宅滯銷（overhang）升至 28,672 戶（2025Q3，+30.5%）、2026Q1 再升至 32,801 戶；越南 2025 年成交 579,718 筆（+7.7%，其中公寓＋獨立屋 138,025）、2025Q4 專案庫存 32,894 戶；印尼 BI 利率 2026 年第二季升 100bp 至 5.75%、2026Q1 一級市場銷售 −25.67%；菲律賓 Pag-IBIG 2025 年房貸放款 PHP 1,405.4 億（+8%，90,727 戶）、社會住宅利率 3%；印度七大城 2025 年銷售 395,625 戶（−14%）、未售 576,617 戶、2026Q3 升至 630,590 戶，房貸利率自 7.0–7.25% 起。
5. 家庭負債／GDP（BIS 口徑，2025 年底）最高的南韓 88.6%、香港 87.8%、泰國 87.5%、馬來西亞 69.8%、日本 61.1%、中國 58.0%，台灣 94.3%（CEIC，2024 年底）更高；這些高槓桿市場與翻修需求最強的市場高度重疊，意味翻修支出對利率循環（日本、南韓 2026 年升息；台灣、中國、泰國降息或持平）極為敏感。
6. 政策性修繕融資以台灣（修繕貸款利息補貼 NT$80 萬、2,000 戶、1.062%／1.762%；老宅延壽機能復新計畫）、日本（子育てグリーン住宅支援 ≤60 萬円、窓リノベ ≤200 萬円、リフォーム減税）、南韓（그린리모델링 이자지원 2026-03-17 重啟，補貼 4.5–5.5%）、新加坡（HIP 2026 年 18,000 戶／S$2.53 億；銀行裝修貸款上限 S$30,000 或 6 倍月薪取低者，源於 MAS Notice 635 之豁免條件）、越南（VBSP 4.8%）最完整；菲律賓 Pag-IBIG 房貸可含修繕（home improvement）。
7. 本檔以「30 年以上存量占比 × 中古交易占比 × 所得」建構翻修需求指標 R（§5），台灣 0.92、香港 0.90、新加坡 0.80、南韓 0.75、中國 0.74、日本 0.64–0.77（30 年以上存量占比缺口使其為區間）居前；泰國（0.66，受顧問估計之二手占比 60% 推升）次之；越南、印尼、菲律賓、印度 0.35–0.44 但新屋交屋量大，需改以「新屋交屋 × 毛胚比例」衡量。
8. 宜蘭（集團所在地）：2025 年建物買賣移轉約 5,270 棟（−23.6%）、房價指數 178.63（−0.81%，東台灣最抗跌）、合法民宿 2,207 家（2025，較 2021 年 1,703 家增 30%）、電梯大樓交易占比 43.5% 首度超越透天 38.6%；「新宜蘭人」（雙北移居之公教／醫師）集中於縣政特區。宜蘭成交屋齡分布與外地買家占比官方統計本輪未取得。

---

## 2. 總體經濟與人口（Q1：Macro & demographics）

### 2.1 Takeaway
IMF WEO 2026 年 4 月（經 Worldometer／Wikipedia 轉載）之 2026 年名目人均 GDP：新加坡 107,758、香港 59,640、台灣 42,103、南韓 37,412、日本 35,703 美元；PPP：新加坡 173,708、台灣 98,051、香港 84,212、南韓 68,624、日本 59,207。65 歲以上占比：日本 29.5%（2026-04，總務省）、香港 25.0%（2025）、南韓 21.4%（2026）、台灣約 20%（2025）、泰國 16.0%（2025）、越南 9.5%（2025）、馬來西亞 8.1%（2024）、印尼 7.3%（2024）、印度 6.8%、菲律賓 5.8%（2021 估）。「高所得 × 高齡 × 高都市化 × 小家戶」四者同時成立者只有日本、南韓、台灣、香港、新加坡。

### 2.2 十二市場總經與人口表

| 市場 | 人均 GDP 名目 USD（2026，IMF WEO 2026-04） | 人均 GDP 名目 USD（2025） | 人均 GDP PPP（2026） | 人口 | 家戶數／戶量 | 都市化 % | 中位數年齡 | 65+ 占比 2025 | 65+ 占比 2035 投影 | 來源 |
|---|---|---|---|---|---|---|---|---|---|---|
| 日本 | **35,703** | 35,973 | **59,207** | 1.224 億（2026，WPP 投影） | 居住世帯あり住宅 5,566.5 萬戸（2023）【官方，代理指標】 | 無資料 | 49.4（2024） | **29.5%（2026-04-01，總務省）**；30.0%（WPP 2025） | 無資料 | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Worldometer 2025](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal)；[Wikipedia PPP（IMF 2026）](https://en.wikipedia.org/wiki/List_of_Asian_countries_by_GDP_(PPP)_per_capita)；[demographer.org 引總務省](https://demographer.org/countries/japan-demographics/)；[populationpyramid.net JP 2025](https://www.populationpyramid.net/japan/2025/)；[populationpyramids.org JP](https://www.populationpyramids.org/japan)；[Wikipedia Demographics of Asia（WPP 2024 中位數）](https://en.wikipedia.org/wiki/Demographics_of_Asia)；[総務省 基本集計](https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf) |
| 南韓 | **37,412** | 36,227 | **68,624** | 5,172 萬（2024） | 無資料 | 無資料 | 45（2024）；46.2（2026）；**52.0（2035）** | **21.4%（2026，WPP）** | 無資料（中位數 2035 有） | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Worldometer KR 人口](https://www.worldometers.info/world-population/south-korea-population/)；[populationpyramids.org KR](https://www.populationpyramids.org/south-korea)；[populationpyramid.net 2035](https://www.populationpyramid.net/republic-of-korea/2050/) |
| 新加坡 | **107,758** | 無資料 | **173,708** | 無資料 | 無資料；HDB 組屋居住之居民家戶占 77.2%（DOS） | 100（城邦） | 無資料 | 無資料 | 無資料 | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Wikipedia PPP](https://en.wikipedia.org/wiki/List_of_Asian_countries_by_GDP_(PPP)_per_capita)；[smartwealth.sg 引 DOS](https://smartwealth.sg/housing-household-statistics-singapore/) |
| 香港 | **59,640** | 無資料 | **84,212** | 無資料 | 無資料 | 100（城邦） | 無資料 | **25.0%（2025，政府經濟分析）**；23.7%（UN 口徑） | 無資料；**36%（2046）** | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[HK Economy Box 6.1（2025 Economic Background and 2026 Prospects）](https://www.hkeconomy.gov.hk/en/pdf/box-25q4-6-1.pdf)；[Visual Capitalist（UN）](https://www.visualcapitalist.com/ranked-25-countries-most-seniors-in-2025-vs-2100/) |
| 台灣 | **42,103** | **39,489**（主計總處概估 39,477） | **98,051** | 無資料（本輪） | 無資料（本輪） | 無資料 | 無資料 | **≈20%（2025）** | 無資料；38.4%（2050，Statista）vs 31.7%（2050，UN 口徑） | [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Taipei Times（IMF）](https://www.taipeitimes.com/News/taiwan/archives/2025/12/24/2003849443)；[聯合新聞網（主計總處）](https://udn.com/news/story/7238/9299429)；[Statista TW 年齡結構](https://www.statista.com/statistics/321439/taiwan-population-distribution-by-age-group/) |
| 中國大陸 | 無資料（本輪摘要未列） | 無資料 | 無資料 | 無資料 | 無資料 | **66.4%（2024，UN）／67%（2024，國家統計口徑）** | 無資料 | 無資料 | 無資料 | [Worldometer CN](https://www.worldometers.info/world-population/china-population/)；[Statista CN 城鎮化](https://www.statista.com/statistics/270162/urbanization-in-china/) |
| 馬來西亞 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | **76.44%（2023，World Bank）** | 無資料 | **8.1%（2024，DOSM）** | **10.4%（2035，政府推估）**；14%（2048，高齡國家門檻） | [Wikipedia Urbanization（WB）](https://en.wikipedia.org/wiki/Urbanization_by_sovereign_state)；[The Star 2026-07-07](https://www.thestar.com.my/news/nation/2026/07/07/one-in-10-malaysians-will-be-aged-65-and-above-by-2035)；[MOF Malaysia](https://mof.gov.my/portal/en/news/press-citations/malaysia-to-become-aged-nation-by-2048-amir-hamzah) |
| 泰國 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | **54.3%（2024，NSO／WB）** | 41.1（2024） | **16.0%（2025）**；16.7%（2026） | 無資料 | [Helgi Library TH](https://www.helgilibrary.com/indicators/urban-population-as-of-total-population/thailand)；[populationpyramid.net TH 2025](https://www.populationpyramid.net/thailand/2025/)；[TH 2026](https://www.populationpyramid.net/thailand/2026/) |
| 越南 | 無資料（IMF）；**5,026（2025，統計局）** | 5,026 | 無資料 | **1.023 億（2025 平均，+0.99%）** | 無資料 | **38.6%（2025，統計局）** | 32.9（2024） | **9.5%（2025，WPP）**；9.9%（2026）；60+ 14.5%（2025，統計局） | 無資料 | [Báo Chính phủ](https://baochinhphu.vn/gdp-nam-2025-tang-truong-802-binh-quan-dau-nguoi-dat-5026-usd-102260105152509472.htm)；[Cục Thống kê](https://www.nso.gov.vn/tin-tuc-thong-ke/2026/01/thong-cao-bao-chi-ve-tinh-hinh-dan-so-lao-dong-viec-lam-quy-iv-va-nam-2025/)；[populationpyramid.net VN 2025](https://www.populationpyramid.net/viet-nam/2025/)；[populationpyramids.org VN](https://www.populationpyramids.org/vietnam) |
| 印尼 | 無資料 | 無資料 | 無資料 | 2.879 億（2026，WPP 投影） | 無資料；Jabodetabek 租屋家戶 124 萬（14.6%） | **59.2%（2024）**；58.12%（2023，WB） | 30.1（2024） | **7.3%（2024）**；7.8%（2026） | 無資料 | [populationpyramid.net ID 2024](https://www.populationpyramid.net/indonesia/2024/)；[populationpyramids.org ID](https://www.populationpyramids.org/indonesia)；[Kompas.id](https://www.kompas.id/artikel/harga-rumah-semakin-tak-tergapai) |
| 菲律賓 | 無資料 | 無資料 | 無資料 | **112,729,484（2024-07-01，POPCEN）** | 2020 普查家戶 26,376,522；每 100 個有人居住住宅單位有 105 戶 | **48.6%（2024，WB）** | 25.7（2024） | 5.80%（2021 估） | **7.9%（2035，WPP 轉載）** | [PSA 2024 POPCEN](https://psa.gov.ph/content/2024-census-population-popcen-population-counts-declared-official-president)；[PSA 2020 CPH 住宅特徵](https://psa.gov.ph/content/housing-characteristics-philippines-2020-census-population-and-housing)；[TradingEconomics（WB）](https://tradingeconomics.com/philippines/urban-population-percent-of-total-wb-data.html)；[Wikipedia Demographics of the Philippines](https://en.wikipedia.org/wiki/Demographics_of_the_Philippines)；[populationpyramid.net PH 2035](https://www.populationpyramid.net/philippines/2035/) |
| 印度 | 無資料 | 無資料 | 無資料 | 無資料 | 無資料 | **35.07%（2023，WB）** | 28.4（2024） | 6.83%（2021 估） | 無資料；14%（2050，UN）；60+ 約 15%（2036，政府推估） | [Wikipedia Urbanization（WB）](https://en.wikipedia.org/wiki/Urbanization_by_sovereign_state)；[Wikipedia Demographics of India](https://en.wikipedia.org/wiki/Demographics_of_India)；[UNFPA India](https://india.unfpa.org/en/news/india-ageing-elderly-make-20-population-2050-unfpa-report)；[PIB Elderly in India](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2183196&reg=48&lang=2) |

IMF 原始入口（本輪未能開啟）：[WEO 2026-04 Statistical Appendix](https://www.imf.org/-/media/files/publications/weo/2026/april/english/statsappendix.pdf)；UN WPP 2024：[population.un.org/wpp](https://population.un.org/wpp/)；World Bank 都市化：[data.worldbank.org](https://data.worldbank.org/?locations=TH-MY-ID-SG-PH-VN)。

### 2.3 Cited Findings
- IMF WEO 2026 年 4 月（Worldometer 轉載）2026 年名目人均 GDP：新加坡 107,758、香港 59,640、台灣 42,103、南韓 37,412、日本 35,703 美元；2025 年：台灣 39,489、南韓 36,227、日本 35,973 — [Worldometer 2026](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal)；[Worldometer 2025](https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal)。注意：Worldometer 2026 頁另有一張未標示年份的表（日本 35,951、新加坡 98,814），應為 2025 值，本檔不採。
- PPP（IMF 2026 估計）：新加坡 173,708、台灣 98,051、香港 84,212、南韓 68,624、日本 59,207 國際元 — [Wikipedia List of Asian countries by GDP (PPP) per capita](https://en.wikipedia.org/wiki/List_of_Asian_countries_by_GDP_(PPP)_per_capita)
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
- IMF WEO 2026-04 之中國、馬來西亞、泰國、印尼、菲律賓、印度名目與 PPP 人均 GDP（Worldometer 頁面有，但本輪摘要未列）；UN WPP 2024 之 2035 年 65+ 占比（12 市場皆缺，僅南韓中位數、馬來西亞政府推估、菲律賓轉載有 2035 值）；台灣、日本、南韓、中國之 World Bank 都市化比率；新加坡、中國、台灣 65+ 2025 精確值；家戶數與戶量（除日本居住世帯あり住宅、菲律賓 2020 普查外全缺）。
