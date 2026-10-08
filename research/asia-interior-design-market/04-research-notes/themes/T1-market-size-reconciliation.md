# T1：市場規模數據彙整與可比性校準（Market-size data reconciliation）

研究日期：2026-10-08｜涵蓋市場：日本、南韓、新加坡、香港、台灣、中國大陸、馬來西亞、泰國、越南、印尼、菲律賓、印度（12 市場）＋亞太整體

> 研究方法備註：本輪共執行約 36 次網路搜尋（含中、日、韓、英文），之後搜尋額度用罄；對 IMF、矢野經済研究所、HK C&SD、Mordor、Grand View 等原始頁面的直接抓取被代理伺服器阻擋（DNS/403），因此部分數字來自搜尋引擎摘要而非原始頁面，已在「信心」欄位降級標示。所有換算匯率採用日本財務省關稅局公告週匯率（2026-08-23～08-29，見 §4.3），USD/TWD ≈ 32.2。

## 1. 摘要

1. 亞太「室內裝修設計市場」沒有任何一個單一、可被引用的官方總量；研究機構給出的亞太數字從 Mordor 的 DIY 居家修繕 USD 64 億（2025）到 Market Data Forecast 的居家修繕 USD 943 億（2025）、Deep Market Insights 的住宅翻修 USD 1,111 億（2025），再到 GlobalData 的居家修繕與園藝零售 USD 2,830 億（2021），差距超過 40 倍，完全取決於定義口徑。
2. 真正具有統計基礎的國家級數字只有五個：日本矢野經済研究所的住宅リフォーム市場 7 兆 5,119 億円（2025）、南韓建設產業研究院（건산연）的建築物리모델링市場 37 兆韓元（2025 年預測值，2020 年發布）、馬來西亞 DOSM 承包商口徑的室內裝潢工程產值 RM 20 億（2024）、香港統計處「工地以外地點」建造工程總值每季約 HK$ 205–225 億（2025）、以及中國建築裝飾協會的產業產值（但 2024 年正式數字本輪未能找到，僅有 2022 年 5.1 兆／6.03 兆人民幣兩個互相矛盾的轉述）。
3. 台灣目前唯一公開的「裝修年產值 5,500 億元（2025）」來自民營媒合平台（100 室內設計／數字科技）「據財政部數據推估」，並非官方統計；本輪未能找到財政部或經濟部對「室內裝潢業」營業額的直接公開數字。
4. 印度是研究機構數字最膨脹的市場：Mordor（USD 314 億，2025）、IMARC（USD 369 億，2025）與本地 Magicbricks Research（₹1.27 lakh crore ≈ USD 133 億，2024，住宅室內）、Redseer（家居與傢俱 ₹2.8–3.0 兆 ≈ USD 340–360 億，2024）之間，商用與住宅的比重甚至互相顛倒（Mordor 稱商用 74%，IMARC 稱住宅 60%）。
5. 東南亞四國（泰、越、印尼、菲）幾乎沒有「室內設計服務」的獨立估計，只有傢俱、家飾、地板等產品市場的研究機構數字；泰國唯一可用的總量是 Mr. DIY 上市文件引用的居家修繕零售市場 1,826 億泰銖（2024）。
6. 研究機構數字有明顯的「回收」痕跡：Grand View 與 Mordor 的全球室內設計市場 2024 年值完全相同（USD 1,379.3 億）；Ken Research 同一國家同一主題在不同頁面給出 USD 24.3 億與 54.2 億兩個 2025 年值；Deep Market Insights 的室內設計服務報告把「訴訟（litigation）」列為最大服務類別，顯示為範本套用錯誤。
7. 建議最終報告以「口徑分層的可比區間」而非單一數字呈現：(a) 住宅翻修支出、(b) 室內設計服務費、(c) 商用裝修（fit-out），並以 IMF WEO 的 GDP 與人口做人均／占 GDP 比率正規化；本輪因 IMF API 被阻擋，僅取得日、韓、台、港、星五地的人均 GDP（經二手轉載），其餘 7 國的正規化留待整合階段補齊。

## 2. 關鍵問題一：亞太整體估計值彙整

### 2.1 彙整表（含定義與地理範圍）

| 機構 | 市場名稱（原文） | 基準值 | 預測值 | CAGR | 定義／範圍 | 來源 | 信心 |
|---|---|---|---|---|---|---|---|
| Deep Market Insights | Asia-Pacific Home Remodeling Market | USD 111.08 億 ×10 = **USD 1,110.8 億（2025）** ≈ NT$3.58 兆 | USD 1,790.8 億（2034） | 5.39%（2026–2034） | 住宅翻修（remodeling）；國家表 2030 欄位為空白；同系列報告有範本錯誤 | [DMI](https://deepmarketinsights.com/vista/insights/home-remodeling-market/asia-pacific) | 低 |
| Market Data Forecast | Asia Pacific Home Improvement Market | **USD 943.5 億（2025）** ≈ NT$3.04 兆 | USD 1,492.8 億（2034） | 5.23%（2026–2034） | 居家修繕整體（產品＋服務，未明示） | [MDF](https://www.marketdataforecast.com/market-reports/asia-pacific-home-improvement-market) | 低–中 |
| Mordor Intelligence | Asia-Pacific DIY Home Improvement Market | **USD 64.2 億（2025）**；USD 67.7 億（2026）≈ NT$2,067 億 | USD 87.9 億（2031） | 5.38%（2026–2031） | 僅 DIY 自行修繕（消費者自購材料）；中國占 31.88%（2025）；印度 CAGR 最快 10.95% | [Mordor](https://www.mordorintelligence.com/industry-reports/asia-pacific-diy-home-improvement-market) | 中 |
| Mordor Intelligence | APAC Interior Design Software Market | **USD 15.3 億（2025）**；USD 17 億（2026）≈ NT$493 億 | USD 28.7 億（2031） | 11.08%（2026–2031） | 僅設計軟體；住宅用戶占 57.13%；雲端占 62.52%；前一版（2025/05）為 USD 13.1 億（2025）→ 22.2 億（2030），同一機構兩版相差 USD 2.2 億 | [Mordor](https://www.mordorintelligence.com/industry-reports/apac-interior-design-software-market)；[R&M 舊版](https://www.researchandmarkets.com/report/asia-pacific-interior-design-software-market) | 中 |
| GlobalData | Retail home improvement & gardening products, APAC | **USD 2,830 億（2021）** | 無 | 無 | 居家修繕＋園藝「零售產品」（非服務） | [GlobalData](https://www.globaldata.com/data-insights/retail-and-wholesale/market-size-of-retail-home-improvement-and-gardening-products-in-asia-pacific/) | 中（但年份舊） |
| Euromonitor | Home Improvement in Asia Pacific | 無公開數字；稱亞太已超越北美成為全球最大居家修繕零售區域 | — | — | 消費者零售通路購買之居家修繕產品，排除對專業承包商之銷售 | [Euromonitor via ResearchPool](https://app.researchpool.com/provider/euromonitor/home-improvement-in-asia-pacific) | 中 |
| Research Dive | APAC DIY Home Improvement Retailing | 無基準值 | — | 3.9%（2021–2028） | DIY 零售 | [PRNewswire](https://prnewswire.co.uk/news-releases/growing-insistence-on-environmental-friendly-diy-projects-and-increasing-urbanization-to-boost-asia-pacific-do-it-yourself-diy-home-improvement-retailing-market-by-2028-160-pages-research-dive-811279977.html) | 低 |
| Statista | APAC home improvement market size in selected countries | 付費統計（ID 1474530），無公開數字 | — | — | 不明 | [Statista](https://www.statista.com/statistics/1474530/apac-home-improvement-market-size-in-selected-countries) | 無資料 |

### 2.2 全球口徑中可推算亞太份額者

| 機構 | 市場 | 全球值 | 亞太資訊 | 來源 | 信心 |
|---|---|---|---|---|---|
| Mordor Intelligence | Interior Design Services（全球） | USD 1,379.3 億（2024）→ USD 1,771.3 億（2029），CAGR 5.13%（2024/02 發布） | 未揭露亞太比例 | [Mordor via DRI](https://dri.co.jp/auto/report/mordor/240217-interior-design-services-market-share.html) | 中 |
| Grand View Research | Interior Design Market（全球） | USD 1,379.3 億（2024），CAGR 4.3% 至 2030；商用占 54.99% | 一份未具名統計彙整稱亞太 21.82%（2023），無法歸屬 GVR | [轉載：Alibaba seller blog](https://seller.alibaba.com/blogs/2026/southeast-asia/design-services/residential-interior-design-guide-alibaba-b2b) | 低（與 Mordor 數字完全相同，疑回收） |
| Fortune Business Insights | Interior Design Market（全球） | USD 1,459.6 億（2025）→ USD 2,143.5 億（2034） | 第三方部落格稱亞太約 38%、中國占亞太 16%、日本 6%（未標年份） | [轉載：hackmd](https://hackmd.io/@anvitoshniwal09/S1J7QEOUfl) | 低（未驗證原始頁） |
| Technavio | Interior Design Services Market 2025–2029（全球） | 未取得基準值 | 亞太貢獻全球「增量成長」之 35%（非市占率）；中國為亞太最大（2024） | [Technavio](https://www.technavio.com/report/interior-design-services-market-industry-analysis) | 中 |
| pmarketresearch | Interior Design Market | 2025 年亞太占 40.17% | 頁面單位自相矛盾（百萬／十億混用） | [pmarketresearch](https://pmarketresearch.com/it/interior-design-market) | 極低 |
| Kings Research（轉載） | Home Renovation Market（全球） | USD 2.84 兆（2024）、2.94 兆（2025）、3.92 兆（2032），CAGR 4.19% | 無亞太拆分 | [轉載](https://connect.usama.dev/blogs/31152/Home-Renovation-Market-An-Examination-of-Major-Segments-from-Kitchens) | 極低 |

### 2.3 結論

- 「亞太室內設計市場」在 Mordor、Grand View、IMARC、Statista 均**沒有獨立報告**（只有軟體、DIY、傢俱等子市場），搜尋「Asia Pacific interior design market」只會得到軟體報告。
- 可用的亞太總量只有三個低–中信心估計（USD 943 億／1,111 億／DIY 64 億）加上一個 2021 年的零售產品數字（USD 2,830 億）。若以全球室內設計市場 USD 1,379–1,460 億 × 亞太 35–40% 推算，亞太「室內設計（含設計＋部分裝修）」約 USD 480–580 億（2024–2025），此為**本研究推算**，非任何機構原始數字。

### 2.4 缺口

- 未找到 Grand View、IMARC、Technavio、Research and Markets、Allied、Precedence、Expert Market Research、Ken Research、6Wresearch 任何一家的「亞太室內設計市場」獨立報告頁面（搜尋 3 次無結果）。
- Fortune Business Insights 的亞太 38% 份額只見於第三方轉載，原始頁面無法抓取。
