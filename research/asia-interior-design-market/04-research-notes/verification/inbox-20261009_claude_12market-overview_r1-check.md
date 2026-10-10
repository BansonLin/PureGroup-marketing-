# r1 回收檢查表：20261009_claude_12market-overview_r1

> 依 `02-integration-protocol.md` §1（回收與格式）、§2（來源分級）、§3（URL 驗證）、§7（幻覺與偏誤檢查）製作。受檢報告：`03-inbox/claude/20261009_claude_12market-overview_r1.md`（以下稱 r1），原始筆記在同目錄 `20261009_claude_12market-overview_r1_notes/`。製作日 2026-10-10。r1 與其筆記未做任何修改。
> **重要限制**：本次執行環境的網路政策封鎖開啟網頁（curl／WebFetch 都會失敗），所以本表**沒有開過任何 URL**。所有「可開啟？」欄一律寫「未驗證（環境網路政策封鎖開頁）」，「判定」欄一律寫「待驗證」。本表不假裝驗證；它的用途是把要驗的 URL、要核的數字、驗證失敗時的後果先整理好，讓能開網頁的會話直接接手。

## 結論先行

- **URL 驗證進度：0／625**（附錄 URL）與 0／49（抽驗樣本）。§3 失敗率無法計算，因此 r1 的整體等級暫時無法依 §3 判定；在驗證完成前，r1 的任何數字都只能當【示意】或搜尋線索使用。
- **r1 本身也沒有開過任何網頁**（r1 第 0 章限制 a），1,733 條來源全部是「搜尋結果內容」。依 §10，r1 不享有「實際開啟過原文」的加權，它與 V1 屬於同一種證據強度。
- **§2 類型分級（1,733 條）**：A 305（17.6%）、B 876（50.5%）、C 461（26.6%）、D 91（5.3%）。這是依來源類型給的「上限」等級；開頁失敗的來源依 §2 一律降為 D。
- **§7 檢查**：幣別換算（含日圓、韓元、越南盾、印尼盾千倍錯誤）、亞太總數拆國、協會認證寫成法定證照、太整齊的數字：未發現問題。**未通過或部分未通過**：URL 存在與內容相符（無法驗證）、在地語言（菲律賓只有 3 條）、2019–2021 及更舊數字當現況（2 處：台灣 2011 年業者家數、日本 2018 年中古占比）。另在裁決過程發現 4 項實質錯誤（菲律賓外資引用已被取代的 EO 175、越南設計費來源其實是辦公室、馬來西亞 LAM 人數取媒體值而非官方值、台灣業者家數停在 2011 年）。

## §1 回收登記與格式檢查

（§1 第 2 步要求的回收登記表 `03-inbox/_intake-log.md` 尚未另建檔；以下為應登錄的內容。）

| 檔名 | AI | 模式 | 範圍 | 日期 | 字數 | 來源數 | 在地語言來源數 |
|---|---|---|---|---|---|---|---|
| 20261009_claude_12market-overview_r1.md | Claude | Claude Code 雲端會話多代理 Research（**不是**提示詞預期的 Claude.ai Research 介面） | 12 市場總覽 | 2026-10-09 | 全檔約 59.9 萬字元（約 9.5 萬中文字）；第 0–6 章約 4.3 萬中文字 | 1,733（含台灣候選出處 4 條） | 約 1,043（r1 自報；本檢查依語言欄重算為 1,043–1,045） |

| 格式項目（§1 第 3 步） | 結果 | 說明 |
|---|---|---|
| 8 章骨架（0–8 章） | 通過 | 第 0–8 章齊全，章名與 `output-format-spec.md` 一致 |
| 12 市場比較表 | 通過 | 12 列 × 13 欄，以程式檢查無空白格（「無資料」43 格） |
| 附錄關鍵指標表 | 通過 | 1,050 列、9 欄 CSV 全部可解析；每市場 ≥15 列（最少為越南 51 列）；每列都有 URL 與 high／medium／low |
| 來源清單只列實際開啟過的 URL（規範 §7） | **不符規範（已揭露）** | r1 列出的全部是只讀過搜尋結果的 URL，並在每列註明「搜尋結果內容」；屬透明揭露，但與規範不符 |
| 搜尋量與在地語言下限 | 部分不符 | 越南只搜尋 13 次（下限 15）；菲律賓在地語言來源 3 條（下限 5） |
| 獨立性 | 註記 | r1 與 V1 都是 Claude，雖各自獨立執行，但同一模型、同一搜尋工具；兩份共用 242 個 URL。依 §4，兩者引用同一來源只算 1 個 |

## （a）分層抽驗樣本（§3：每份報告 ≥20 條）

共 49 條，涵蓋 12 市場與 6 個主題，優先抽支撐 12 市場比較表與摘要數字的來源。「預驗風險」取自 r1 第 7 章「讀取方式」欄的註記；「與 V1 同源」表示 V1 也引用了同一 URL（驗證一次可同時用於兩份報告）。

| URL | 可開啟？ | 數字相符？ | 年份相符？ | 定義相符？ | 判定 | 來源# | 市場／主題 | r1 用在哪裡 | 待核數字或主張 | 類型等級 | 預驗風險 | 與 V1 同源 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| https://udn.com/news/story/7241/9245511 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-23 | 台灣 | 比較表：住宅翻修規模；摘要 1 | 2025 年裝修產值近 5,500 億 TWD（平台推估） | B | — | 是 |
| https://money.udn.com/money/story/5621/9014283 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-13 | 台灣 | 比較表：30 年以上屋齡；摘要 2 | 30 年以上住宅 5,545,854 戶、約 59%；平均 34.1 年（2025Q2） | B | 對應或年份為推定 | 是 |
| https://finance.technews.tw/2026/06/25/taiwan-housing-market-more-houses-built-fewer-buyers-25-5-decline-nine-year-low/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-14 | 台灣 | 台灣 3.1.2；摘要 2 | 2025 年建物買賣移轉 261,308 棟（−25.5%）；第一次登記 176,690 棟（+8.4%） | B | — | 是 |
| https://www.moi.gov.tw/News_Content.aspx?n=2905&s=328048 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-41 | 台灣 | 台灣 3.1.2；摘要 2 | 2024 年住宅類使照 13.8 萬戶，近 10 年新高 | A | — | 否 |
| https://www.pro360.com.tw/price/old_house_renovation | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-19 | 台灣 | 比較表：單價（高階） | 老屋（30–40 年）翻新 10–18 萬 TWD／坪 | C | — | 否 |
| https://www.pro360.com.tw/price/20_ping_house_decoration | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-21 | 台灣 | 比較表：設計費 | 20 坪新成屋設計費 9–24 萬、工程費 60–180 萬（推得 13–15%） | C | — | 否 |
| https://w3.cpami.gov.tw/statisty/100/100_pdf/06_building/0c_building.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-30 | 台灣 | 台灣 3.1.3 | 2011 年底室內裝修業 4,969 家（設計施工 3,633、施工 1,299） | A | — | 否 |
| https://me.moe.edu.tw/license/view.php?lid=303&frm=1&cid=101 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-34 | 台灣 | 比較表：執業管制 | 建築物室內裝修專業技術人員登記證列於教育部政府核發證照一覽 | A | — | 否 |
| https://www.dreamnews.jp/press/0000356164 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-01 | 日本 | 比較表：規模 | 矢野：2025 年住宅翻修 7.51 兆 JPY，2026 年預測 7.7 兆 | B | — | 否 |
| https://www.chord.or.jp/assets/marketsize_2024.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-07 | 日本 | 比較表：規模；§2.1 | CHORD：2024 年狹義住宅翻修 7.0 兆 JPY | B | — | 否 |
| https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_fr2_000055.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-23 | 日本 | 比較表：中古屋交易占比 | 既存住宅流通シェア 14.5%（2018） | A | — | 否 |
| https://shuken-renovation.jp/yomimono/column/no427/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-34 | 日本 | 比較表：單價；摘要 3 | マンション全面翻修 15–20 萬 JPY／m²；戸建て 10–22 萬 | C | — | 否 |
| https://www.cerik.re.kr/board/press/589 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-01 | 韓國 | 比較表：規模 | CERIK：2020 年建築物리모델링 30조 KRW；2025 預測 37조 | B | — | 是 |
| https://www.korea.kr/news/policyNewsView.do?newsId=156721680 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-48 | 韓國 | 比較表：30 年以上屋齡；摘要 2 | 2024 年 30 年以上住宅 557 萬戶、28.0% | A | — | 否 |
| https://www.ajd.co.kr/contents/basic-tip/detail/%ED%98%84%EC%9E%A5_%EC%97%85%EC%9E%90%EA%B0%80_%EC%95%8C%EB%A0%A4%EB%93%9C%EB%A6%AC%EB%8A%94_%EC%95%84%ED%8C%8C%ED%8A%B8_%EB%A6%AC%EB%AA%A8%EB%8D%B8%EB%A7%81_%EB%B9%84%EC%9A%A9_%ED%8F%89%EB%8B%B9_%EA%B0%80%EA%B2%A9!-50541 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-61 | 韓國 | 比較表：單價 | 全面翻修每평 150–170／180–200／220+ 만원 | C | 對應或年份為推定 | 否 |
| https://www.law.go.kr/LSW/lumLsLinkPop.do?lspttninfSeq=105029&chrClsCd=010202 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-72 | 韓國 | 比較表：執業管制 | 實內建築工程 1,500 만원以上須登錄 | A | — | 否 |
| https://qanvast.com/sg/articles/what-are-the-expected-renovation-costs-for-hdb-flats-in-2026-3568 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-13 | 新加坡 | 比較表：單價 | HDB 翻修每戶 S$5–8.16 萬（2026） | C | — | 否 |
| https://www.era.com.sg/press-release/4q-2025-ura-real-estate-statistics-private-home-demand-momentum-carries-from-3q-2025-sets-firm-outlook-for-2026 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-71 | 新加坡 | 比較表：中古屋交易 | 2025 年私宅轉售占 55.2% | C | — | 否 |
| https://www.case.org.sg/wp-content/uploads/2025/02/Media-Release-CASE-sees-prepayment-losses-more-than-quadruple-in-2024-entertainment-related-complaints-nearly-triple.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-01 | 新加坡 | 摘要 7 | 2024 年裝修投訴 97% 針對非 CaseTrust 業者 | B | — | 是 |
| https://www.info.gov.hk/gia/general/202503/11/P2025031100233.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-01 | 香港 | 比較表：規模代理 | 2024 年地盤以外建造工程 873 億 HKD（年減 6.0%） | A | — | 是 |
| https://homejournal.com/2026-hong-kong-renovation-cost-guide-a-complete-breakdown-from-starter-homes-to-luxury-flats/128996/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-09 | 香港 | 比較表：單價 | 全屋裝修約 HK$1,000／呎實用（中階） | C | — | 是 |
| http://static.cninfo.com.cn/finalpage/2025-04-30/1223412858.PDF | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-03 | 中國大陸 | 比較表：規模；§2.1 | CBDA 2024 年住宅裝飾裝修約 2.2 萬億 CNY | A | — | 否 |
| https://www.sohu.com/a/859595741_116082 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-20 | 中國大陸 | 比較表：規模；§2.1 | 奧維 2024 年家裝銷售額 3.563 萬億 CNY | D | — | 是 |
| https://news.qq.com/rain/a/20220628A0BO3R00 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-90 | 中國大陸 | 比較表：30 年以上屋齡；摘要 2 | 1990 年前建成住房占 14.4%（2020 普查） | B | — | 是 |
| https://news.qq.com/rain/a/20260920A09ZUS00 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-16 | 中國大陸 | 比較表：中古屋交易 | 2025 年二手房占比 46% | B | — | 否 |
| https://dosm.gov.my/portal-main/release-content/construction-statistics-first-quarter-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-16 | 馬來西亞 | 比較表：規模代理 | DOSM 2025Q1 專業工程完成值（四季合計約 RM214 億之一） | A | — | 否 |
| https://www.propplace.my/guides/malaysia-residential-property-market-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-06 | 馬來西亞 | 比較表：中古屋交易 | 2025 年中古屋占住宅交易 84.5% | C | — | 否 |
| https://bernama.com/bm/news.php?id=2325906 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-60 | 馬來西亞 | 比較表：執業管制 | LAM 登記室內設計師約 165 人 | B | — | 否 |
| https://www.bernama.com/en/news.php?id=2479278 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-17 | 泰國 | 比較表：規模代理 | 2024 年家居修繕零售 1,826 億 THB | B | — | 是 |
| https://www.businesstoday.co/business/25/02/2026/126296/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-02 | 泰國 | 比較表：中古屋交易 | 2025 年中古屋占過戶 64%（REIC） | B | — | 是 |
| https://th.wikipedia.org/wiki/%E0%B8%AA%E0%B8%96%E0%B8%B2%E0%B8%9B%E0%B8%B1%E0%B8%95%E0%B8%A2%E0%B8%81%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-53 | 泰國 | 比較表：執業管制；摘要 4 | 公共建築室內 ≥500 m² 須持照 | D | — | 是 |
| https://takenli.vn/chi-phi-lam-noi-that-chung-cu-70m2-bao-gia-kinh-nghiem-thuc-te/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-11 | 越南 | 比較表：單價 | 70 m² 公寓室內裝修 180–450 百萬 VND（推得 257 萬／357–471 萬／643 萬 VND 每 m²） | C | 候選出處 | 否 |
| https://baochinhphu.vn/nguoi-nuoc-ngoai-co-duoc-dau-tu-hoat-dong-thiet-ke-noi-that-102272847.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-46 | 越南 | 比較表：外資；§5.3 | 室內設計外資登記須主管部會同意 | A | — | 否 |
| https://coda.io/@thietkenoithat/bao-gia-thiet-ke-van-phong | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-16 | 越南 | 比較表：設計費 | 設計費 150,000–200,000 VND／m²（附錄註明為辦公室） | D | — | 否 |
| https://www.credenceresearch.com/report/indonesia-interior-design-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-14 | 印尼 | 比較表：設計服務市場 | 2023 年室內設計市場 8.2478 億 USD（Credence） | C | — | 是 |
| https://pegadaian.co.id/artikel/keuangan/estimasi-biaya-renovasi-rumah | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-09 | 印尼 | 比較表：單價 | 翻修每 m² Rp150–250 萬／250–400 萬／400–600 萬 | C | — | 否 |
| https://psa.gov.ph/content/construction-statistics-approved-building-permits-philippines-2024 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-01 | 菲律賓 | 比較表：規模代理 | 2024 年核准建照「改建及修繕」造價 PhP 430.5 億 | A | — | 否 |
| https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/5/95421 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-53 | 菲律賓 | 比較表：外資；§5.3 | EO 175 把室內設計列在外資上限 40% | A | — | 是 |
| https://www.mordorintelligence.com/industry-reports/india-interior-design-market/market-size | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-01 | 印度 | 比較表：設計服務市場 | Mordor：印度 interior design 市場規模（2025） | C | — | 否 |
| https://www.imarcgroup.com/india-interior-design-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-03 | 印度 | 比較表：設計服務市場 | IMARC：印度 interior design 市場規模（2025） | C | — | 是 |
| https://poonawallafincorp.com/blogs/personal-loan/full-home-renovation-cost-in-india | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-43 | 印度 | 比較表：單價 | 全屋翻修 ₹1,500–2,000／2,000–3,000／3,000–4,000 每 sq ft | C | — | 否 |
| https://static.squareyards.com/PrimaryVsSecondary-UnpackingDemandTrendsinIndia'sResidentialMarket-SquareYards.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-88 | 印度 | 比較表：中古屋交易 | FY25 主要城市中古屋占 43% | C | — | 否 |
| https://www.federalreserve.gov/releases/g5a/current/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-01 | 總體（主題 F） | 全文匯率基準 | Fed G.5A 2025 年平均匯率（TWD 31.1663 等） | A | 多個候選 URL | 否 |
| https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-18 | 總體（主題 F） | 比較表：人均 GDP | IMF WEO 2026-04 之 2025 年人均 GDP（經 Worldometer） | B | — | 是 |
| https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-04 | 商空（主題 C） | 摘要 5；台灣 fit-out | C&W 2026：台北 145 USD／sq ft，新加坡 140 | B | — | 否 |
| https://daiwair.webcdn.stream.ne.jp/www11/daiwair/qlviewer/pdf/2605088919gCYthxZI.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-03 | 商業模式（主題 A） | 摘要 6 | カチタス 2026/3 期營業利益率約 12.0% | A | — | 否 |
| https://www.cna.com.tw/news/afe/201908050023.aspx | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-02 | 跨境（主題 E） | 摘要 9 | 特力 HOLA 2019 年關閉 13 店、提列約 3.78 億 TWD | B | — | 否 |
| https://smart.businessweekly.com.tw/Reading/IndepArticle.aspx?id=6015022 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-41 | 補助（主題 D） | 台灣基準線補充 | 長照 2.0 輔具及居家無障礙 4 萬元／3 年 | B | — | 否 |
| https://wowtale.net/2026/04/14/257037/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-30 | 平台（主題 B） | 摘要 5 | 오늘의집 2025 年營收 3,215 억 KRW | B | — | 是 |

## （b）附錄關鍵指標表（第 8 章）URL 全表（§3：100% 驗證）

第 8 章 1,050 列共引用 **625 個不重複 URL**（以完整字串去重；再以網域去 www／尾斜線正規化後仍為 625 個，沒有隱藏重複）。每個 URL 對應的來源編號、市場與列數一併列出，驗證時一次核對該 URL 支撐的所有列。依最高等級來源計：A 130、B 312、C 164、D 19。

附錄內 3 列（CSV 資料第 776、880、946 列，即越南、印尼、菲律賓的交叉匯率）來源編號寫「TF-01+TF-14」或「TF-01+TF-10」，URL 只放了第三方匯率站；驗證時兩個來源都要核。

| # | URL | 可開啟？ | 數字相符？ | 年份相符？ | 定義相符？ | 判定 | 來源# | 市場 | 附錄列數 | 類型等級 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | https://www.federalreserve.gov/releases/G5/current/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-02 | ALL、CN、HK、IN、JP、KR、MY、SG、TH、TW | 41 | A |
| 2 | https://www.federalreserve.gov/releases/g5a/current/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-01 | ALL、CN、HK、IN、JP、KR、MY、SG、TH、TW | 27 | A |
| 3 | https://population.un.org/wpp/assets/Files/WPP2024_Summary-of-Results.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-26 | ALL | 1 | A |
| 4 | https://www.worldometers.info/world-population/asia-population/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-27 | ALL | 1 | B |
| 5 | https://lodgingeconometrics.com/record-projects-apec-hotel-pipeline-q1-2026/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-100 | APAC、TH、VN | 3 | C |
| 6 | https://lodgingeconometrics.com/global-insights/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-99 | APAC、IN | 2 | C |
| 7 | https://irei.com/news/average-fit-out-costs-for-offices-lowest-in-asia-pacific-compared-to-other-regions-jll/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-22 | APAC | 1 | B |
| 8 | https://www.jll.com/en-in/guides/apac-fit-out-costs-guide | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-24 | APAC | 1 | B |
| 9 | https://www.jll.com/en-in/insights/apac-fit-out-cost-guide-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-23 | APAC | 1 | B |
| 10 | https://www.malaymail.com/news/money/mediaoutreach/2026/03/26/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific/456444 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-17 | APAC | 1 | B |
| 11 | https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-18 | CN、HK、ID、IN、JP、KR、MY、PH、SG、TH、TW、VN | 12 | B |
| 12 | https://www.worldometers.info/gdp/gdp-by-country/?region=asia&year=2025&metric=nominal | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-20 | CN、IN、JP、KR、TW | 10 | B |
| 13 | https://www.theglobaleconomy.com/rankings/elderly_population/Asia/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-24 | CN、HK、JP、KR、SG、TH | 6 | B |
| 14 | https://www.nbd.com.cn/articles/2026-02-24/4267391.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-16 | CN | 5 | B |
| 15 | http://static.cninfo.com.cn/finalpage/2026-04-18/1225117188.PDF | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-113 | CN | 4 | A |
| 16 | http://static.cninfo.com.cn/finalpage/2025-04-30/1223412858.PDF | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-03 | CN | 3 | A |
| 17 | http://www.fangchan.com/data/13/2026-09-28/7510233308522157027.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-18 | CN | 3 | B |
| 18 | https://36kr.jp/354289/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-16 | CN | 3 | B |
| 19 | https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office/28-29/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-02 | CN、KR | 3 | B |
| 20 | https://finance.eastmoney.com/a/202604273720900682.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-35 | CN | 3 | B |
| 21 | https://finance.sina.com.cn/wm/2026-04-29/doc-inhwcvfh7817283.shtml?cre=tianyi&mod=pcfinhkst&loc=9&r=0&rfunc=4&tj=cxvertical_pc_finhkst&tr=12 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-77 | CN | 3 | B |
| 22 | https://m.chinabgao.com/freereport/115875.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-22 | CN | 3 | C |
| 23 | https://m.thebell.co.kr/m/newsview.asp?svccode=&newskey=202111301137052080102465 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-06 | CN | 3 | B |
| 24 | https://pdf.dfcfw.com/pdf/H2_AN202207051575830711_1.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-34 | CN | 3 | B |
| 25 | https://www.cna.com.tw/news/afe/201908050023.aspx | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-02 | CN | 3 | B |
| 26 | https://www.gov.cn/zhengce/zhengceku/202501/content_7001494.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-56 | CN | 3 | A |
| 27 | https://www.oppein.com/upfile/2026/04/20260428134446_923.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-22 | CN | 3 | A |
| 28 | https://www.theglobaleconomy.com/rankings/Percent_urban_population/Asia/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-23 | CN、ID、JP | 3 | B |
| 29 | http://finance.ce.cn/stock/gsgdbd/202207/06/t20220706_37838347.shtml | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-35 | CN | 2 | B |
| 30 | https://finance.sina.cn/2024-07-24/detail-incfeqsk9610801.d.html?vt=4&cid=76524&node_id=76524 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-62 | CN | 2 | B |
| 31 | https://finance.sina.com.cn/roll/2026-04-15/doc-inhupqxi8541563.shtml | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-82 | CN | 2 | B |
| 32 | https://finance.sina.com.cn/stock/hkstock/hkzmt/2026-02-24/doc-inhnyyvp1282748.shtml | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-108 | CN | 2 | B |
| 33 | https://m.fz.bendibao.com/news/75548.shtm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-61 | CN | 2 | C |
| 34 | https://m.gelonghui.com/p/1702454 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-61 | CN | 2 | B |
| 35 | https://m.jiemian.com/article/14124429.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-10 | CN | 2 | B |
| 36 | https://m.rccaijing.com/news-7467096612750948211.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-79 | CN | 2 | B |
| 37 | https://news.qq.com/rain/a/20230329A02O8Q00 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-55 | CN | 2 | B |
| 38 | https://news.qq.com/rain/a/20260920A09ZUS00 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-16 | CN | 2 | B |
| 39 | https://www.focus.cn/a/992078021_116082?scm=10001.7320_13-116000-0_922.0-0.0-0-0-0-0.a2_5X190X1069 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-48 | CN | 2 | B |
| 40 | https://www.ryutsuu.biz/abroad/r20250514003.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-80 | CN、TW | 2 | B |
| 41 | https://www.sohu.com/a/859595741_116082 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-20 | CN | 2 | D |
| 42 | https://www.stats.gov.cn/xxgk/sjfb/zxfb2020/202601/t20260119_1962324.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-08 | CN | 2 | A |
| 43 | https://zhuanlan.zhihu.com/p/1941938450937939920 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-64 | CN | 2 | D |
| 44 | http://basic.10jqka.com.cn/002081/field.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-108 | CN | 1 | B |
| 45 | http://epaper.zqrb.cn/html/2026-04/29/content_1238242.htm?div=-1 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-119 | CN | 1 | B |
| 46 | http://finance.sina.com.cn/stock/yyyj/2026-04-29/doc-inhwewst0723689.shtml | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-117 | CN | 1 | B |
| 47 | http://lingqisj.com/gsxw/3761.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-39 | CN | 1 | C |
| 48 | http://www.cbda.cn/html/yj/20250312/141927.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-01 | CN | 1 | B |
| 49 | https://cs.com.cn/sylm/jsbd/201808/t20180829_5865640.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-13 | CN | 1 | B |
| 50 | https://finance.ifeng.com/c/8r1M16jzvLU | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-18 | CN | 1 | B |
| 51 | https://finance.sina.cn/2026-04-30/detail-inhwfays7425120.d.html?vt=4 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-114 | CN | 1 | B |
| 52 | https://finance.sina.cn/cj/2024-07-04/detail-incawrmz9244743.d.html?vt=4 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-92 | CN | 1 | B |
| 53 | https://finance.sina.com.cn/roll/2025-09-03/doc-infpftfy7581179.shtml | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-78 | CN | 1 | B |
| 54 | https://finance.sina.com.cn/roll/2026-03-30/doc-inhsuquw2693118.shtml | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-17 | CN | 1 | B |
| 55 | https://finance.sina.com.cn/stock/roll/2026-03-04/doc-inhpunaw4077005.shtml?cre=tianyi&mod=pchp&loc=31&r=0&rfunc=21&tj=cxvertical_pc_hp&tr=12 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-21 | CN | 1 | B |
| 56 | https://finance.sina.com.cn/tech/csj/2025-02-14/doc-ineknewy7187278.shtml | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-28 | CN | 1 | B |
| 57 | https://finance.sina.com.cn/tech/roll/2025-05-08/doc-inevswwk1483374.shtml | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-66 | CN | 1 | B |
| 58 | https://fred.stlouisfed.org/release/tables?eid=26693&rid=15 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-03 | CN | 1 | A |
| 59 | https://jingdaily.com/intels/2026-01/08/ikea-pivots-to-smaller-stores-shutting-7-china-sites | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-69 | CN | 1 | B |
| 60 | https://m.bjnews.com.cn/detail/1790671605169302.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-17 | CN | 1 | B |
| 61 | https://m.businesspost.co.kr/BP?command=mobile_view&num=180543 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-07 | CN | 1 | B |
| 62 | https://m.gelonghui.com/live/2147093 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-66 | CN | 1 | B |
| 63 | https://m.gelonghui.com/live/2193149 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-68 | CN | 1 | B |
| 64 | https://m.gelonghui.com/p/637059 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-54 | CN | 1 | B |
| 65 | https://m.hibor.com.cn/wap_detail.aspx?id=f6ad484404e17061441e1ebf1d8e9530 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-88 | CN | 1 | B |
| 66 | https://m.thepaper.cn/newsDetail_forward_18953836 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-14 | CN | 1 | B |
| 67 | https://news.10jqka.com.cn/20260427/c676320749.shtml | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-101 | CN | 1 | B |
| 68 | https://news.qq.com/rain/a/20220628A0BO3R00 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-90 | CN | 1 | B |
| 69 | https://news.qq.com/rain/a/20240221A090US00 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-95 | CN | 1 | B |
| 70 | https://news.qq.com/rain/a/20260409A07IQE00?id=20260409A07IQE00&path=a&app=news&suid=&redirect_pc=1 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-20 | CN | 1 | B |
| 71 | https://news.qq.com/rain/a/20260420A07B9200 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-32 | CN | 1 | B |
| 72 | https://news.qq.com/rain/a/20260429A042AL00?media_id=&suid= | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-25 | CN | 1 | B |
| 73 | https://news.qq.com/rain/a/20260920A08JHX00 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-39 | CN | 1 | B |
| 74 | https://pdf.dfcfw.com/pdf/H2_AN202107051501978291_1.pdf?1625513152000.pdf= | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-33 | CN | 1 | B |
| 75 | https://scjgj.beijing.gov.cn/zwxx/scjgdt/202312/t20231208_3493772.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-125 | CN | 1 | A |
| 76 | https://scjgj.sh.gov.cn/cmsres/01/013097b8259047ec9d54be645442d42a/5d118ce63ba013b56a648236cd096e63.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-126 | CN | 1 | A |
| 77 | https://static.cninfo.com.cn/finalpage/2026-04-28/1225219607.PDF | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-100 | CN | 1 | A |
| 78 | https://static.weeklyonstock.com/26/0427/AB2622075859419.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-110 | CN | 1 | B |
| 79 | https://www.163.com/dy/article/K7J9B3L30556EG2C.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-60 | CN | 1 | D |
| 80 | https://www.21jingji.com/article/20240916/herald/a447195ac38b84dfd1e6f3a1787f3783.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-80 | CN | 1 | B |
| 81 | https://www.beijing.gov.cn/zhengce/zcjd/202205/t20220512_2707837.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-140 | CN | 1 | A |
| 82 | https://www.ccn.com.cn/Content/2025/02-20/1731025533.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-30 | CN | 1 | B |
| 83 | https://www.chinep.net/newsss/show.php?itemid=10312 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-122 | CN | 1 | C |
| 84 | https://www.digitaling.com/articles/1243185.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-112 | CN | 1 | B |
| 85 | https://www.guandian.cn/article/20260728/578007.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-84 | CN | 1 | B |
| 86 | https://www.gz.gov.cn/zt/tddgmsbgxhxfpyjhx/gzxd/content/post_10132753.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-60 | CN | 1 | A |
| 87 | https://www.jfdaily.com/wx/detail.do?id=1082476 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-30 | CN | 1 | B |
| 88 | https://www.jiemian.com/article/2432262.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-45 | CN | 1 | B |
| 89 | https://www.lejucaijing.com/news-7307711954683623300.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-53 | CN | 1 | B |
| 90 | https://www.mirrormedia.mg/story/amp/20190803fin001 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-03 | CN | 1 | B |
| 91 | https://www.mofcom.gov.cn/xwfb/rcxwfb/art/2024/art_e7455eb501514b05bf90912336c62bd8.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-75 | CN | 1 | A |
| 92 | https://www.mofcom.gov.cn/zwgk/zcfb/art/2025/art_fca1a108eea64d0a858c6d6136455d45.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-62 | CN | 1 | A |
| 93 | https://www.ndrc.gov.cn/xwdt/ztzl/cjgyjjpwzz/dfjyhzf/202304/t20230428_1355207.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-96 | CN | 1 | A |
| 94 | https://www.news.cn/fortune/2022-11/21/c_1129146975.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-143 | CN | 1 | A |
| 95 | https://www.news.cn/fortune/20260205/175286b8aacb4f2ca2c4c2eadc418d20/c.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-45 | CN | 1 | A |
| 96 | https://www.news.cn/house/20250325/dbe5166639e74752b526e46288082ffe/c.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-26 | CN | 1 | A |
| 97 | https://www.ryutsuu.biz/accounts/q110674.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-13 | CN | 1 | B |
| 98 | https://www.sgpjbg.com/bgdown/187977.html?dtype=83039 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-63 | CN | 1 | B |
| 99 | https://www.shanghai.gov.cn/xbhygq/20241206/e1cd8f68109b48bf829ac6b2b1dfd2ce.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-34 | CN | 1 | A |
| 100 | https://www.sohu.com/a/1055935733_655634 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-82 | CN | 1 | D |
| 101 | https://www.stcn.com/article/detail/3679495.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-31 | CN | 1 | B |
| 102 | https://www.sz.gov.cn/cn/xxgk/zfxxgj/zwdt/content/post_12071085.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-32 | CN | 1 | A |
| 103 | https://www.thepaper.cn/newsDetail_forward_30371407 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-67 | CN | 1 | B |
| 104 | https://www.thepaper.cn/newsDetail_forward_32414370 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-09 | CN | 1 | B |
| 105 | https://www.to8to.com/yezhu/z320545.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-61 | CN | 1 | C |
| 106 | https://www.to8to.com/yezhu/z348860.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-67 | CN | 1 | C |
| 107 | https://www.to8to.com/yezhu/z353267.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-68 | CN | 1 | C |
| 108 | https://www.wenxuan.news/live/20326.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-19 | CN | 1 | B |
| 109 | https://www.xinminweekly.com.cn/shenghuo/2026/05/13/43236.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-62 | CN | 1 | B |
| 110 | https://www.yicai.com/news/101328408.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-142 | CN | 1 | B |
| 111 | https://www.zx123.cn/zxbk/2445401.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-69 | CN | 1 | C |
| 112 | https://www2.jpx.co.jp/disc/59380/140120161107432620.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-62 | CN | 1 | A |
| 113 | https://yicaiglobal.com/news/japanese-furniture-giant-nitori-plans-massive-china-expansion-vp-says | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-14 | CN | 1 | B |
| 114 | https://zhuanlan.zhihu.com/p/16237122723 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | CN-23 | CN | 1 | D |
| 115 | https://www.worldometers.info/gdp/gdp-by-country/?region=asia&year=2026&metric=nominal | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-21 | HK、ID、IN、JP、KR、MY、PH、SG、TH、TW、VN | 11 | B |
| 116 | https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2026&metric=nominal | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-19 | HK、ID、IN、JP、KR、MY、PH、SG、TH、TW、VN | 11 | B |
| 117 | https://cw-prod-gblgws-a-cm.cushwake.com/en/greater-china/news/2026/05/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-04 | HK、JP、SG、TW | 4 | B |
| 118 | https://gia.info.gov.hk/general/202603/25/P2026032500380_537189_1_1774417243800.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-77 | HK | 3 | A |
| 119 | https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2025/global-office-fit-out-costs | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-27 | HK、IN、JP | 3 | B |
| 120 | https://www.censtatd.gov.hk/en/data/stat_report/product/B1050013/att/B10500132024MM01B0100.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-81 | HK | 3 | A |
| 121 | https://www.info.gov.hk/gia/general/202603/12/P2026031200295.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-70 | HK | 3 | A |
| 122 | https://www.visualcapitalist.com/ranked-25-countries-most-seniors-in-2025-vs-2100/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-25 | HK、TW | 3 | C |
| 123 | https://hk.centanet.com/info/property-news/%E7%A0%94%E7%A9%B6%E5%A0%B1%E5%91%8A/%E6%A8%93%E5%AE%87%E8%B2%B7%E8%B3%A3%E5%90%88%E7%B4%84%E7%99%BB%E8%A8%98%E7%B5%B1%E8%A8%88%E5%88%86%E6%9E%90-2025%E5%B9%B41%E6%9C%88%E4%BB%BD-%E6%95%B4%E9%AB%94%E8%B2%B7%E8%B3%A3%E5%86%8D%E5%BA%A6%E8%B7%8C%E7%A0%B4%E4%BA%94%E5%8D%83%E5%AE%97-%E4%B8%80%E4%BA%8C%E6%89%8B%E7%A7%81%E4%BA%BA%E4%BD%8F%E5%AE%85%E5%AE%97%E6%95%B8-%E5%90%8C%E7%82%BA4%E5%80%8B%E6%9C%88%E4%BD%8E%E4%BD%8D/181106 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-22 | HK | 2 | C |
| 124 | https://www.arcadis.com/contentassets/934a2cbf81254a22b8d893e40f92c781/2025constructioncosthandbook_china_hongkong.pdf?rev=1b304935c6ec425db127792f5c3703b3 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-55 | HK | 2 | B |
| 125 | https://www.businesstimes.com.hk/articles/154163/%E6%B6%88%E5%A7%94%E6%9C%83-%E5%AE%B6%E5%B1%85%E8%A3%9D%E4%BF%AE-%E5%B9%B4%E5%9D%87%E6%8A%95%E8%A8%B4172%E5%AE%97-%E4%B8%8D%E5%AF%A6%E5%84%AA%E6%83%A0-%E6%94%B6%E8%B2%BB%E5%90%AB%E7%B3%8A-%E7%94%B1%E6%96%BD%E5%B7%A5%E5%89%8D%E5%BE%8C%E5%88%B0%E4%BA%A4%E6%94%B66%E5%80%8B%E4%BC%8F%E4%BD%8D/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-11 | HK | 2 | B |
| 126 | https://www.gotohui.com/gongzi/list/160535.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-82 | HK | 2 | D |
| 127 | https://www.info.gov.hk/gia/general/202503/11/P2025031100233.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-01 | HK | 2 | A |
| 128 | https://www.legco.gov.hk/yr19-20/chinese/panels/dev/papers/dev20191216cb1-230-7-c.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-80 | HK | 2 | A |
| 129 | https://www.moneyhero.com.hk/blog/zh/裝修貸款-私人貸款-比較 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-07 | HK | 2 | C |
| 130 | https://www.stheadline.com/society/3318766/%E6%B6%88%E5%A7%94%E6%9C%83%E5%AE%B6%E5%B1%85%E8%A3%9D%E4%BF%AE%E5%A0%B1%E5%83%B9%E6%AC%A0%E9%80%8F%E6%98%8E-7%E5%B9%B4%E9%96%93%E6%8E%A51205%E5%AE%97%E6%8A%95%E8%A8%B4-0%E5%85%83%E6%8C%89%E9%87%91%E5%AF%A6%E5%89%87%E5%A4%A7%E4%BC%8F | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-10 | HK | 2 | B |
| 131 | https://air-corporate.com/why-companies-register-hk/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-89 | HK | 1 | C |
| 132 | https://businessfocus.io/article/346344/%E4%B8%AD%E5%8E%9F%E5%8D%81%E5%A4%A7%E5%B1%8B%E8%8B%9112%E6%9C%88%E9%8C%84188%E5%AE%97%E6%88%90%E4%BA%A4 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-24 | HK | 1 | B |
| 133 | https://finance.mingpao.com/fin/instantp/20250825/1756112161916/%E7%BE%8E%E8%81%AF-%E4%BB%8A%E5%B9%B4%E4%B8%80%E6%89%8B%E6%96%991-9%E8%90%AC%E5%AE%97%E5%89%B5%E6%96%B0%E9%AB%98-%E3%80%8A%E6%96%BD%E6%94%BF%E5%A0%B1%E5%91%8A%E3%80%8B%E6%8E%AA%E6%96%BD%E6%88%96%E6%8E%A8%E5%8D%87%E6%B8%AF%E4%BA%BA%E8%B2%B7%E6%A8%93%E6%84%8F%E6%AC%B2 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-23 | HK | 1 | B |
| 134 | https://fitoutawards.ie/news/hong-kong-office-fit-out-costs-hold-firm-at-160-per-square-foot-as-greater-china-peers-record-declines | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-43 | HK | 1 | D |
| 135 | https://gia.info.gov.hk/general/201910/11/P2019101100570_324663_1_1570790231117.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-87 | HK | 1 | A |
| 136 | https://hkcna.hk/docDetail.jsp?id=100528765&channel=4371 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-27 | HK | 1 | B |
| 137 | https://hkcourtnews.com/%E5%AE%8F%E7%A6%8F%E8%8B%91%E4%BA%94%E7%B4%9A%E7%81%AB%EF%BD%9C%E5%B1%8B%E5%AE%87%E7%BD%B2%E5%90%91%E9%B4%BB%E6%AF%85%E3%80%81%E5%AE%8F%E6%A5%AD%E3%80%81%E7%9B%B8%E9%97%9C%E8%91%A3%E4%BA%8B%E5%8F%8A/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-57 | HK | 1 | B |
| 138 | https://homejournal.com/2026-hong-kong-renovation-cost-guide-a-complete-breakdown-from-starter-homes-to-luxury-flats/128996/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-09 | HK | 1 | C |
| 139 | https://news.qq.com/rain/a/20251127A063QK00 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-28 | HK | 1 | B |
| 140 | https://realestateasia.com/commercial-office/news/hong-kong-grade-office-vacancy-rate-falls-161-in-q2 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-70 | HK | 1 | C |
| 141 | https://reports.turnerandtownsend.com/office-fit-out-cost-guide-2026-us/hong-kong | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-32 | HK | 1 | B |
| 142 | https://research.jllapsites.com/appd-market-report/q2-2026-office-hong-kong/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-71 | HK | 1 | B |
| 143 | https://www.bd.gov.hk/doc/tc/resources/codes-and-references/code-and-design-manuals/MW/TG_c/TGc_ch02.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-17 | HK | 1 | A |
| 144 | https://www.bd.gov.hk/tc/safety-inspection/mbis/index.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-31 | HK | 1 | A |
| 145 | https://www.businesstimes.com.hk/articles/292656/%E7%BE%8E%E8%81%AF%E6%A8%93%E5%83%B9%E6%8C%87%E6%95%B8-2025%E5%B9%B4%E5%85%A8%E5%B9%B4%E5%8D%875-14-%E4%BF%A1%E5%BF%83%E6%8C%87%E6%95%B8%E5%8D%87%E7%B4%842%E6%88%90/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-26 | HK | 1 | B |
| 146 | https://www.censtatd.gov.hk/en/press_release_detail.html?id=5393 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-03 | HK | 1 | A |
| 147 | https://www.devb.gov.hk/filemanager/en/content_1345/Powerpoint_for_the_briefing_20231009.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-34 | HK | 1 | A |
| 148 | https://www.devb.gov.hk/filemanager/tc/content_1345/FAQ%20(C | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-33 | HK | 1 | A |
| 149 | https://www.edigest.hk/%E5%89%B5%E6%A5%AD/90%E5%BE%8C%E5%89%B5%E8%BE%A6hellotoby-%E5%A5%87%E9%9B%A3%E9%9B%9C%E7%97%87%E6%90%B5%E5%B0%88%E4%BA%BA%E4%BB%A3%E5%8B%9E-15025/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-116 | HK | 1 | B |
| 150 | https://www.info.gov.hk/gia/general/202503/11/P2025031100240.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-02 | HK | 1 | A |
| 151 | https://www.info.gov.hk/gia/general/202506/10/P2025061000355.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-04 | HK | 1 | A |
| 152 | https://www.info.gov.hk/gia/general/202509/11/P2025091100340.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-72 | HK | 1 | A |
| 153 | https://www.info.gov.hk/gia/general/202512/11/P2025121100293.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-71 | HK | 1 | A |
| 154 | https://www.info.gov.hk/gia/general/202606/11/P2026061100218.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-05 | HK | 1 | A |
| 155 | https://www.info.gov.hk/gia/general/202609/10/P2026091000332.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-06 | HK | 1 | A |
| 156 | https://www.legco.gov.hk/yr19-20/chinese/panels/dev/papers/dev20191216cb1-230-6-c.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-85 | HK | 1 | A |
| 157 | https://www.legco.gov.hk/yr2026/cn/panels/hg/papers/hgcb1-992-1-c.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-20 | HK | 1 | A |
| 158 | https://www.sc.com/hk/zh/stories/loan-tips/find-a-home/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-08 | HK | 1 | C |
| 159 | https://www.stheadline.com/lifetips/3562457/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-78 | HK | 1 | B |
| 160 | https://www.wenweipo.com/a/202407/05/AP668702d9e4b01166d97ad713.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | HK-66 | HK | 1 | B |
| 161 | https://exchangerate.dev/learn/irs-yearly-average-exchange-rates | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-01、TF-10 | ID、PH | 4 | AC |
| 162 | https://investortrust.id/business/112799/bps-catat-9-29-juta-keluarga-belum-miliki-hunian-dan-18-01-juta-menghuni-rumah-tak-layak | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-05 | ID | 3 | B |
| 163 | https://pegadaian.co.id/artikel/keuangan/estimasi-biaya-renovasi-rumah | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-09 | ID | 3 | C |
| 164 | https://www.idxchannel.com/market-news/laba-bersih-aces-turun-25-persen-pada-2025-penjualan-naik-tipis-jadi-rp864-triliun | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-94 | ID | 3 | B |
| 165 | https://www.kenresearch.com/industry-reports/indonesia-home-improvement-market.md | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-01 | ID | 3 | C |
| 166 | https://www.liputan6.com/hot/read/6024358/harga-jasa-desain-interior-2025-panduan-lengkap-amp-tips-memilih-desainer-profesional | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-44 | ID | 3 | B |
| 167 | https://iainkendari.ac.id/pojok-rektor/show/kaleidoskop-general-ekonomi-moneter-indonesia-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-11 | ID | 2 | B |
| 168 | https://investasi.kontan.co.id/news/penjualan-naik-tipis-laba-bersih-aces-merosot-25-di-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-17 | ID | 2 | B |
| 169 | https://investortrust.id/business/80487/38-ribu-rtlh-mulai-direnovasi-oktober-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-75 | ID | 2 | B |
| 170 | https://investortrust.id/business/91428/realisasi-anggaran-kementerian-pkp-2025-tembus-96 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-82 | ID | 2 | B |
| 171 | https://lib.ui.ac.id/detail?id=9999920519556&lokasi=lokal | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-35 | ID | 2 | B |
| 172 | https://siplawfirm.id/id/publikasi/pemerintah-berikan-bantuan-pembangunan-perumahan-dan-penyediaan-rumah-khusus | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-88 | ID | 2 | B |
| 173 | https://www.credenceresearch.com/report/indonesia-interior-design-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-14 | ID | 2 | C |
| 174 | https://www.imarcgroup.com/indonesia-home-decor-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-16 | ID | 2 | C |
| 175 | https://www.kompas.com/jawa-tengah/read/2025/10/07/130000488/upah-tukang-bangunan-di-seluruh-provinsi-indonesia-jakarta-rp-165 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-81 | ID | 2 | B |
| 176 | https://www.megasyariah.co.id/id/artikel/edukasi-tips/pembiayaan/estimasi-budget-renovasi-rumah-tips-biar-hemat | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-11 | ID | 2 | C |
| 177 | https://www.retalkasia.com/news/2025/03/06/office-fit-out-costs-asia-pacific-continue-rise-cushman-wakefield/1741232445 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-11 | ID、JP | 2 | C |
| 178 | https://databoks.katadata.co.id/ekonomi-makro/statistik/3a6719d2aa29da8/indeks-harga-perdagangan-besar-ihpb-bahan-bangunan | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-87 | ID | 1 | B |
| 179 | https://ecommercedb.com/store/dekoruma.com | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-61 | ID | 1 | C |
| 180 | https://economy.okezone.com/read/2025/04/21/470/3132646/tak-punya-rumah-jumlah-backlog-di-indonesia-naik-jadi-15-juta-di-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-07 | ID | 1 | B |
| 181 | https://ekonomi.bisnis.com/read/20250818/47/1903526/rapbn-2026-anggaran-kementerian-pkp-rp109-triliun-untuk-program-perumahan | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-83 | ID | 1 | B |
| 182 | https://hybrid.co.id/post/dekoruma-umumkan-pendanaan-2168-miliar-rupiah-segera-capai-ebitda-positif-dan-rencanakan-ipo/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-128 | ID | 1 | B |
| 183 | https://industri.kontan.co.id/news/ikea-jadi-motor-pemulihan-kinerja-dfi-retail-nusantara-hero-pada-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-53 | ID | 1 | B |
| 184 | https://industri.kontan.co.id/news/rups-setujui-dividen-catur-sentosa-adiprana-csap-rp-227-miliar | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-25 | ID | 1 | B |
| 185 | https://investortrust.id/business/63933/kepala-bps-tepis-isu-backlog-hunian-capai-15-juta-tahun-ini | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-06 | ID | 1 | B |
| 186 | https://market.bisnis.com/read/20260225/192/1955682/sinyal-pemulihan-kinerja-penjualan-azko-aces-mulai-terlihat | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-18 | ID | 1 | B |
| 187 | https://market.bisnis.com/read/20260411/192/1965806/siapkan-capex-hingga-rp450-miliar-azko-aces-bidik-ekspansi-80-toko-baru | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-19 | ID | 1 | B |
| 188 | https://market.bisnis.com/read/20260626/192/1983518/csap-tebar-dividen-rp227-miliar-percepat-ekspansi-mitra10 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-24 | ID | 1 | B |
| 189 | https://money.kompas.com/read/2025/03/03/133434726/bps-indeks-harga-perdagangan-besar-tumbuh-130-persen-februari-2025-didorong | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-89 | ID | 1 | B |
| 190 | https://pasardana.id/news/2026/6/26/kinerja-hero-melejit-guardian-dan-ikea-jadi-mesin-pertumbuhan-dfi-nusantara-di-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-54 | ID | 1 | B |
| 191 | https://profiles.crustdata.com/company/dekoruma | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-130 | ID | 1 | C |
| 192 | https://research.jllapsites.com/appd-market-report/q1-2026-office-jakarta/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-90 | ID | 1 | B |
| 193 | https://sibambostudio.com/harga-interior-design-rincian-biaya-lengkap/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-47 | ID | 1 | C |
| 194 | https://sn-studio.id/kisaran-biaya-jasa-desain-interior-per-m%C2%B2/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-46 | ID | 1 | C |
| 195 | https://wartaekonomi.co.id/read187183/minim-ri-hanya-punya-200- | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-41 | ID | 1 | B |
| 196 | https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_2715025.aspx | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-13 | ID | 1 | A |
| 197 | https://www.bi.go.id/id/publikasi/ruang-media/news-release/Pages/sp_2727925.aspx | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-12 | ID | 1 | A |
| 198 | https://www.brighton.co.id/about/articles-all/biaya-renovasi-rumah-2-lantai-2 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-10 | ID | 1 | C |
| 199 | https://www.cbinsights.com/company/dekoruma | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-57 | ID | 1 | C |
| 200 | https://www.cnbcindonesia.com/news/20260901204221-4-764160/harga-bahan-bangunan-naik-barang-grosir-inflasi-05-agustus-2026 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-88 | ID | 1 | B |
| 201 | https://www.credenceresearch.com/report/indonesia-luxury-interior-design-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-15 | ID | 1 | C |
| 202 | https://www.idxchannel.com/economics/kementerian-pkp-kebut-program-bedah-rumah-ditargetkan-selesai-november-2026/all | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-77 | ID | 1 | B |
| 203 | https://www.kenresearch.com/indonesia-home-improvement-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-50 | ID | 1 | C |
| 204 | https://www.liputan6.com/hot/read/6111136/estimasi-biaya-bangun-rumah-sederhana-sesuai-tipe-dan-modelnya-di-2025-ini-tips-hematnya | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-13 | ID | 1 | B |
| 205 | https://www.marketresearch.com/Ken-Research-v3771/Indonesia-DIY-Hardware-Store-Outlook-44312370/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-51 | ID | 1 | C |
| 206 | https://www.researchandmarkets.com/report/asia-pacific-home-improvement-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-48 | ID | 1 | C |
| 207 | https://www.suarasurabaya.net/?p=231683 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | ID-42 | ID | 1 | B |
| 208 | https://entrackr.com/fintrackr/livspace-posts-rs-1460-cr-revenue-in-fy25-losses-shrink-42-10559863 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-15、TA2-61 | IN | 5 | B |
| 209 | https://ianslive.in/ikea-indias-loss-widens-to-rs-1325-crore-in-fy25-revenue-dips--20260204142638 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-31 | IN | 5 | B |
| 210 | https://entrackr.com/fintrackr/homelane-records-rs-748-revenue-in-fy25-but-falls-short-of-projections-10586234 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-25、TA2-66 | IN | 4 | B |
| 211 | https://entrackr.com/fintrackr/urban-company-posts-rs-1144-cr-revenue-and-rs-285-cr-pbt-in-fy25-9373371 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-120 | IN | 4 | B |
| 212 | https://poonawallafincorp.com/blogs/personal-loan/full-home-renovation-cost-in-india | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-43 | IN | 3 | C |
| 213 | https://static.squareyards.com/PrimaryVsSecondary-UnpackingDemandTrendsinIndia'sResidentialMarket-SquareYards.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-88 | IN | 3 | C |
| 214 | https://www.businesstoday.in/amp/real-estate/story/housing-sales-fall-14-in-2025-amid-sky-high-prices-it-layoffs-anarock-research-508242-2025-12-26 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-34 | IN | 3 | B |
| 215 | https://www.imarcgroup.com/india-interior-design-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-03 | IN | 3 | C |
| 216 | https://www.mordorintelligence.com/industry-reports/india-interior-design-market/market-size | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-01 | IN | 3 | C |
| 217 | https://hdfcsky.com/news/urban-company-turns-profitable-in-fy25-ahead-of-ipo | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-119 | IN | 2 | B |
| 218 | https://realtynmore.com/competitive-fit-out-market-cushman-wakefield/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-106、TC-07 | IN | 2 | C |
| 219 | https://realtynmore.com/premium-housing-captures-50-of-indias-348207-residential-sales-in-2025-knight-frank-india/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-39 | IN | 2 | C |
| 220 | https://www.indianretailer.com/news/retail-india-news-ikea-india-loss-widens-rs-13252-cr-fy25 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-32 | IN | 2 | B |
| 221 | https://www.outlookbusiness.com/markets/housing-sales-dip-1-last-year-in-top-8-cities-avg-price-grows-up-to-19-knight-frank | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-40 | IN | 2 | B |
| 222 | https://alephindia.in/bis-qco-for-the-plywood-face-panels.php | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-54 | IN | 1 | C |
| 223 | https://blog.ipleaders.in/employment-visa-india-rules-procedure/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-100 | IN | 1 | C |
| 224 | https://constructionestimatorindia.com/?p=17098 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-85 | IN | 1 | C |
| 225 | https://cw-prod-apacgws-a-cd.cushwake.com/en/india/insights/office-fit-out-cost-guide | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-09 | IN | 1 | B |
| 226 | https://housing.com/news/compensation-for-defects-in-construction-after-possession-under-rera/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-58 | IN | 1 | C |
| 227 | https://ianslive.in/india-remains-asia-pacifics-most-cost-competitive-office-fit-out-market-report--20260326105534 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-08 | IN | 1 | B |
| 228 | https://india.entrepreneur.com/?p=93997 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-20 | IN | 1 | B |
| 229 | https://m.thewire.in/article/ptiprnews/homelane-reports-22-revenue-growth-in-fy25-and-turns-ebitda-positive-in-q4-fy25 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-67 | IN | 1 | B |
| 230 | https://material360.co/blog/interior-design-industry | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-08 | IN | 1 | C |
| 231 | https://morbitilehub.com/blog/morbi-tile-price-hike-june-2026 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-78 | IN | 1 | C |
| 232 | https://orangeowl.marketing/unicorn-chronicles/livspace-success-story/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-11 | IN | 1 | D |
| 233 | https://pmay-urban.gov.in/material/component4/Housing_in_India_Compendium_English_Version2.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-92 | IN | 1 | A |
| 234 | https://realtynmore.com/asia-pacific-knight-frank-report | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-33 | IN | 1 | C |
| 235 | https://realtynmore.com/office-fit-out-costs-rise-amid-demand-for-premium-tech-enabled-sustainable-workspaces | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-105 | IN | 1 | C |
| 236 | https://redseer.com/casestudies/how-redseer-helped-indias-largest-d2c-home-furnishings-brand-by-revenue-in-fiscal-2024-wakefit-file-its-drhp/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-12 | IN | 1 | B |
| 237 | https://simplehai.axisdirect.in/app/index.php/insights/reports/downloadReport/file/Initiating+Coverage+-+Building+Materials+-+16072025+(2 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-79 | IN | 1 | B |
| 238 | https://solve24.in/blog/mason-construction-worker-daily-wages-india-2026 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-70 | IN | 1 | C |
| 239 | https://us.fashionnetwork.com/news/Muji-to-open-in-india-in-2016,548388.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-30 | IN | 1 | B |
| 240 | https://www.credenceresearch.com/report/india-interior-design-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-05 | IN | 1 | C |
| 241 | https://www.crematrix.com/blog/india-office-space-trends-2026-rents-up-vacancy-down/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-95 | IN | 1 | B |
| 242 | https://www.designcafe.com/blog/modular-kitchen-interiors/modular-kitchen-cost-delhi/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-47 | IN | 1 | C |
| 243 | https://www.houseyog.com/blog/how-much-does-an-interior-designer-charge-in-india/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-82 | IN | 1 | C |
| 244 | https://www.iifl.com/hi/blogs/gold-loan/home-renovation-cost-india-2025-full-budget-guide-financing-options | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-75 | IN | 1 | C |
| 245 | https://www.inkl.com/news/interior-designer-takes-rs-4-9-lakh-full-payment-leaves-work-incomplete-consumer-court-orders-refund-after-family-is-forced-to-stay-on-rent-for-months | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-97 | IN | 1 | B |
| 246 | https://www.outlookbusiness.com/corporate/livspace-revenue-rises-23-to-1460-cr-in-fy25-losses-come-down | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-63 | IN | 1 | B |
| 247 | https://www.outlookbusiness.com/start-up/news/urban-company-swings-to-2398-cr-profit-in-fy25-ahead-of-ipo | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-30 | IN | 1 | B |
| 248 | https://www.patrika.com/national-news/vb-g-ram-g-rural-employment-guarantee-act-2025-new-wage-rates-125-days-work-20710556 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-67 | IN | 1 | B |
| 249 | https://www.psmarketresearch.com/ja/market-analysis/india-interior-design-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-06 | IN | 1 | C |
| 250 | https://www.storyboard18.com/amp/advertising/ikea-india-posts-rs-1299-crore-loss-in-fy24-ad-spend-rises-to-rs-196-crore-report-51943.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-33 | IN | 1 | B |
| 251 | https://yojoapp.com/hi/blog/labor-rates-construction-india-2026-complete-guide/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | IN-66 | IN | 1 | C |
| 252 | https://www.marketscreener.com/news/nitori-e-ae--ce7f5bddd88af42c | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-01 | JP | 6 | A |
| 253 | https://daiwair.webcdn.stream.ne.jp/www11/daiwair/qlviewer/pdf/2605088919gCYthxZI.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-03 | JP | 5 | A |
| 254 | https://www.yano.co.jp/press-release/show/press_id/4153 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-24 | JP | 4 | B |
| 255 | https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20250711/20250711512501.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-117 | JP | 3 | A |
| 256 | https://finboard.jp/companies/JP:9843/history | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-12 | JP | 3 | C |
| 257 | https://jutaku-shoene2026.mlit.go.jp/about/reform.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-01 | JP | 3 | A |
| 258 | https://www.homes.co.jp/cont/press/buy/buy_01909/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-10 | JP | 3 | C |
| 259 | https://www.nikkei.com/markets/ir/irftp/data/tdnr/tdnetg3/20260430/fwiqo2/140120260430514722.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-104 | JP | 3 | A |
| 260 | https://www.reform-online.jp/news/reform-shop/67245.php | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-25 | JP | 3 | B |
| 261 | https://www.stat.go.jp/data/jyutaku/2023/pdf/g_kekka.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-14 | JP | 3 | A |
| 262 | https://finance.biggo.jp/news/jpx_tdnet_140120260109531815 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-58 | JP | 2 | A |
| 263 | https://hojyokin-portal.jp/subsidies/55272 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-09 | JP | 2 | C |
| 264 | https://howroad.co.jp/column/?p=9142 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-66 | JP | 2 | C |
| 265 | https://jp.investing.com/news/company-news/article-93CH-1512876 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-47 | JP | 2 | B |
| 266 | https://kabutan.jp/stock/finance?code=9716 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-103 | JP | 2 | B |
| 267 | https://kabutan.jp/stock/news?code=8940&b=n202509010478 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-118 | JP | 2 | B |
| 268 | https://kyutou-shoene2026.meti.go.jp/about/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-03 | JP | 2 | A |
| 269 | https://shuken-renovation.jp/yomimono/column/no427/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-34 | JP | 2 | C |
| 270 | https://the-shashi.com/tse/7453/current/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-83 | JP | 2 | B |
| 271 | https://www.chord.or.jp/assets/marketsize_2024.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-07 | JP | 2 | B |
| 272 | https://www.city.yokohama.lg.jp/kenko-iryo-fukushi/fukushi-kaigo/koreisha-kaigo/kaigo-hoken/kaishuhi/juukai.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-19 | JP | 2 | A |
| 273 | https://www.dreamnews.jp/press/0000356164 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-01 | JP | 2 | B |
| 274 | https://www.fse.or.jp/files/lis_tkj/26043053327.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-103 | JP | 2 | A |
| 275 | https://www.kokusen.go.jp/soudan_topics/data/reformtenken.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-54 | JP | 2 | A |
| 276 | https://www.nikkei.com/markets/ir/irftp/data/tdnr/tdnetg3/20260113/fpx71a/140120260109531806.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-57 | JP | 2 | A |
| 277 | https://www.rbayakyu.jp/rbay-kodawari/item/8489-2025-49-114-3 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-21 | JP | 2 | D |
| 278 | https://www.s-housing.jp/archives/419068 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-46 | JP | 2 | B |
| 279 | https://www.zaimu.metro.tokyo.lg.jp/documents/d/zaimu/roumur080301 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-67 | JP | 2 | A |
| 280 | https://crexgroup.com/ja/reform/renovation/renovation-cost-guide-2/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-39 | JP | 1 | C |
| 281 | https://crexgroup.com/ja/reform/renovation/sumairu-reform-homepro-reviews/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-61 | JP | 1 | C |
| 282 | https://finance.recruit.co.jp/article/k117/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-11 | JP | 1 | C |
| 283 | https://finance.yahoo.co.jp/quote/2975.T/performance | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-59 | JP | 1 | B |
| 284 | https://furureno.jp/magazine/renovation-subsidy-guide-window | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-15 | JP | 1 | C |
| 285 | https://hojyokin-portal.jp/columns/senshintki_mado_renovation | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-13 | JP | 1 | C |
| 286 | https://htonline.sohjusha.co.jp/20251031-2/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-08 | JP | 1 | B |
| 287 | https://kabutan.jp/stock/finance?code=9743 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-104 | JP | 1 | B |
| 288 | https://kyutou-shoene2026.meti.go.jp/graph/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-04 | JP | 1 | A |
| 289 | https://note.com/katitas8919/n/n82c7f6f7efd2 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-04 | JP | 1 | D |
| 290 | https://onayami000.com/home-pro/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-94 | JP | 1 | D |
| 291 | https://reform-hojo.jp/subsidy/34 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-05 | JP | 1 | C |
| 292 | https://reform-site.net/homepro/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-99 | JP | 1 | D |
| 293 | https://shou-blog.com/homepro-reputation/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-96 | JP | 1 | C |
| 294 | https://www.arc-navi.shikaku.co.jp/column/details.php?column_id=3671 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-69 | JP | 1 | C |
| 295 | https://www.arc-navi.shikaku.co.jp/column/details.php?column_id=5887 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-12 | JP | 1 | C |
| 296 | https://www.city.mitsuke.niigata.jp/uploaded/attachment/19690.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-10 | JP | 1 | A |
| 297 | https://www.colliers.com/en-jp/research/tokyo-office-market-q2-2026 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-67 | JP | 1 | B |
| 298 | https://www.jiji.com/jc/article?k=2026040800679&g=eco | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-32 | JP | 1 | B |
| 299 | https://www.mlit.go.jp/jutakukentiku/build/content/001757621.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-149 | JP | 1 | A |
| 300 | https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_fr2_000055.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-23 | JP | 1 | A |
| 301 | https://www.mlit.go.jp/report/press/house04_hh_001323.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-02 | JP | 1 | A |
| 302 | https://www.mlit.go.jp/report/press/tochi_fudousan_kensetsugyo14_hh_000001_00337.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-63 | JP | 1 | A |
| 303 | https://www.muji.net/ie/corporate/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-85 | JP | 1 | C |
| 304 | https://www.nikkei.com/article/DGXZQOUA2785N0X20C26A1000000/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-68 | JP | 1 | A |
| 305 | https://www.nikkei.com/article/DGXZQOUC085E10Y6A400C2000000/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-33 | JP | 1 | A |
| 306 | https://www.pref.osaka.lg.jp/documents/12205/r5jutyou.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-42 | JP | 1 | A |
| 307 | https://www.pref.saitama.lg.jp/documents/240159/jyutyo_saitamakenbun.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-41 | JP | 1 | A |
| 308 | https://www.reform-online.jp/news/reform-shop/67571.php | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-26 | JP | 1 | B |
| 309 | https://www.reins.or.jp/pdf/trend/sf/sf_2025.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-20 | JP | 1 | B |
| 310 | https://www.ryutsuu.biz/company/nitorihd | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-78 | JP | 1 | B |
| 311 | https://www.s-housing.jp/archives/427008 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-02 | JP | 1 | B |
| 312 | https://www.seikatsu-do.com/information/jutaku-shoene2026/kyuto-shoene2026.php | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-16 | JP | 1 | C |
| 313 | https://www.stat.go.jp/data/jyutaku/2023/pdf/kihon_gaiyou.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-15 | JP | 1 | A |
| 314 | https://www.tsr-net.co.jp/data/detail/1201585_1527.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-30 | JP | 1 | B |
| 315 | https://www.yano.co.jp/press-release/show/press_id/3877 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-04 | JP | 1 | B |
| 316 | https://www1.mlit.go.jp:8088/common/001081906.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-19 | JP | 1 | A |
| 317 | https://www1.mlit.go.jp:8088/common/001132800.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | JP-43 | JP | 1 | A |
| 318 | http://www.srtimes.kr/news/articleView.html?idxno=214203 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-85 | KR | 4 | B |
| 319 | https://www.korea.kr/news/policyNewsView.do?newsId=156721680 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-48 | KR | 4 | A |
| 320 | http://www.ancnews.kr/news/articleView.html?idxno=10893 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-03 | KR | 3 | B |
| 321 | https://biz.heraldcorp.com/article/10668992 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-36、TA1-107 | KR | 3 | B |
| 322 | https://byline.network/2025/03/31_bucketplace/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-33、TA2-01 | KR | 3 | B |
| 323 | https://company.hanssem.com/ir/financials/highlights | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-13 | KR | 3 | A |
| 324 | https://dealsite.co.kr/articles/156654 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-41 | KR | 3 | B |
| 325 | https://m.catch.co.kr/Comp/CompSummary/HH4342 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-101 | KR | 3 | C |
| 326 | https://www.ajd.co.kr/contents/basic-tip/detail/%ED%98%84%EC%9E%A5_%EC%97%85%EC%9E%90%EA%B0%80_%EC%95%8C%EB%A0%A4%EB%93%9C%EB%A6%AC%EB%8A%94_%EC%95%84%ED%8C%8C%ED%8A%B8_%EB%A6%AC%EB%AA%A8%EB%8D%B8%EB%A7%81_%EB%B9%84%EC%9A%A9_%ED%8F%89%EB%8B%B9_%EA%B0%80%EA%B2%A9!-50541 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-61 | KR | 3 | C |
| 327 | https://www.ajunews.com/view/20250202110248372 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-32 | KR | 3 | B |
| 328 | https://www.asiae.co.kr/article/2025060317133786615 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-29 | KR | 3 | B |
| 329 | https://www.insightkorea.co.kr/news/articleView.html?idxno=241285 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-19、TA1-16 | KR | 3 | B |
| 330 | http://www.csr.co.kr/pds_data/noim2026.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-93 | KR | 2 | B |
| 331 | https://bravo.etoday.co.kr/view/atc_view/20009 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-35 | KR | 2 | B |
| 332 | https://demoday.co.kr/bm-analysis/104 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-107 | KR | 2 | C |
| 333 | https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=02915926642401144 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-57 | KR | 2 | B |
| 334 | https://m.news.nate.com/view/20260316n27780 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-28 | KR | 2 | B |
| 335 | https://newstomato.com/ReadNews.aspx?no=1301184 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-05 | KR | 2 | B |
| 336 | https://wowtale.net/2026/04/14/257037/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-30、TA2-04 | KR | 2 | B |
| 337 | https://www.ikld.kr/news/articleView.html?idxno=223589 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-02 | KR | 2 | C |
| 338 | https://www.koscaj.com/news/articleView.html?idxno=111927 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-08 | KR | 2 | B |
| 339 | https://consline.co.kr/523864 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-16 | KR | 1 | B |
| 340 | https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=1222&ccfNo=2&cciNo=1&cnpClsNo=1 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-75 | KR | 1 | A |
| 341 | https://eiec.kdi.re.kr/policy/materialView.do?num=275544 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-54 | KR | 1 | B |
| 342 | https://info.cak.or.kr/lay1/bbs/S1T9C12/A/2/view.do?article_seq=153489&condition=&cpage=1&keyword=&rows=10 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-90 | KR | 1 | B |
| 343 | https://kbthink.com/main/real-estate/real-estate-in-depth-analysis/real-estate-research-report/2025/real-estate-research-report-serise3-250213.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-52 | KR | 1 | B |
| 344 | https://kicc.or.kr/license | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-67 | KR | 1 | B |
| 345 | https://m.news.nate.com/view/20260203n36871 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-21 | KR | 1 | B |
| 346 | https://m.news.nate.com/view/20260212n44377 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-56 | KR | 1 | B |
| 347 | https://magazine.hankyung.com/business/article/202107285159b | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-12 | KR | 1 | B |
| 348 | https://news.tf.co.kr/read/ogmeta/2183540.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-36 | KR | 1 | B |
| 349 | https://ohstory.io/press/pressrelease/15242 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-08 | KR | 1 | C |
| 350 | https://prtimes.jp/main/html/rd/p/000000973.000073913.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-20 | KR | 1 | C |
| 351 | https://spacelogin.co.kr/2026-%EC%82%AC%EB%AC%B4%EC%8B%A4-%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4-%EC%97%85%EC%B2%B4-%EB%B9%84%EA%B5%90-%EA%B0%80%EC%9D%B4%EB%93%9C/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-36 | KR | 1 | C |
| 352 | https://thebell.co.kr/free/Content/ArticleView.asp?key=202507251542475720104532&svccode= | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-38 | KR | 1 | B |
| 353 | https://view.asiae.co.kr/article/2026031611295345516 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-26 | KR | 1 | B |
| 354 | https://view.asiae.co.kr/article/2026072717565427925 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-78 | KR | 1 | B |
| 355 | https://www.ajd.co.kr/contents/basic-tip/detail/28%ED%8F%89,_29%ED%8F%89,_30%ED%8F%89_%EC%95%84%ED%8C%8C%ED%8A%B8_%EB%A6%AC%EB%AA%A8%EB%8D%B8%EB%A7%81_%EB%B9%84%EC%9A%A9!_%EC%A0%84%EC%B2%B4_%EC%98%AC%EC%88%98%EB%A6%AC_%EA%B2%AC%EC%A0%81_%ED%99%95%EC%9D%B8-51013 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-63 | KR | 1 | C |
| 356 | https://www.businesspost.co.kr/BP?command=article_view&num=435686 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-32 | KR | 1 | B |
| 357 | https://www.cerik.re.kr/board/press/589 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-01 | KR | 1 | B |
| 358 | https://www.codil.or.kr/filebank/original/RK/OTKCRK240459/OTKCRK240459.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-13 | KR | 1 | B |
| 359 | https://www.dnews.co.kr/uhtml/view.jsp?idxno=202201272348519800829 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-09 | KR | 1 | B |
| 360 | https://www.ebn.co.kr/news/articleView.html?idxno=1698009 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-37 | KR | 1 | B |
| 361 | https://www.fnnews.com/news/202512311901236006 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-98 | KR | 1 | B |
| 362 | https://www.fntimes.com/html/view.php?ud=202107141629356481539a63f164_18 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-27 | KR | 1 | B |
| 363 | https://www.gg.go.kr/uploads/CONTENTS/site/gg/2025%EB%85%84%EB%8F%84+%EA%B2%BD%EA%B8%B0%EB%8F%84+%EC%A3%BC%EA%B1%B0%EC%A2%85%ED%95%A9%EA%B3%84%ED%9A%8D_v20250619.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-33 | KR | 1 | A |
| 364 | https://www.hankyung.com/realestate/article/202012146956e | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-75 | KR | 1 | B |
| 365 | https://www.heraldk.com/article/2026031601231333800 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-37 | KR | 1 | B |
| 366 | https://www.imaeil.com/page/view/2025060412375066298 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-31 | KR | 1 | B |
| 367 | https://www.incruit.com/company/1682546883/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-102 | KR | 1 | C |
| 368 | https://www.innoforest.co.kr/company/CP00000005/%EB%B2%84%ED%82%B7%ED%94%8C%EB%A0%88%EC%9D%B4%EC%8A%A4 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-11 | KR | 1 | C |
| 369 | https://www.kalis.or.kr/www/brd/m_57/view.do?seq=2513&srchFr=&srchTo=&srchWord=&srchTp=&itm_seq_1=0&itm_seq_2=0&multi_itm_seq=0&company_cd=&company_nm=&p_stat=&p_itmseq1= | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-30 | KR | 1 | B |
| 370 | https://www.kcenews.kr/9000 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-79 | KR | 1 | B |
| 371 | https://www.kharn.kr/news/article.html?no=30991 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-100 | KR | 1 | B |
| 372 | https://www.kjob.news/news/501752 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-35 | KR | 1 | B |
| 373 | https://www.korea.kr/briefing/policyBriefingView.do?newsId=156643294&pWise=sub&pWiseSub=J2 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-49 | KR | 1 | A |
| 374 | https://www.korea.kr/news/policyNewsView.do?newsId=148960908 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-27 | KR | 1 | A |
| 375 | https://www.koscaj.com/news/articleView.html?idxno=321280 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-14 | KR | 1 | B |
| 376 | https://www.law.go.kr/LSW/lumLsLinkPop.do?lspttninfSeq=105029&chrClsCd=010202 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-72 | KR | 1 | A |
| 377 | https://www.newsis.com/view/NISX20260203_0003500734 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | KR-20 | KR | 1 | B |
| 378 | https://www.nikkei.com/article/DGXZQOGM2313T0T21C23A1000000/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-19 | KR | 1 | A |
| 379 | https://www.saramin.co.kr/zf_user/company-info/view/csn/b1NWdXFrd1BWbm9CU0VzM0hjUzNzdz09/company_nm/(%EC%A3%BC | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-108 | KR | 1 | C |
| 380 | https://www.sedaily.com/article/20056998 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-72 | KR | 1 | B |
| 381 | https://www.thereport.co.kr/news/articleView.html?idxno=86670 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-07 | KR | 1 | B |
| 382 | https://www.topdaily.kr/articles/102282 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-02 | KR | 1 | B |
| 383 | https://zdnet.co.kr/view/?no=20260414142409 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-05 | KR | 1 | B |
| 384 | https://www.propplace.my/guides/malaysia-residential-property-market-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-06 | MY | 5 | C |
| 385 | https://quartr.com/events/mr-d-i-y-group-m-berhad-mrdiy-q4-2025_FMmZXo2l | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-93 | MY | 4 | B |
| 386 | https://www.cushmanwakefield.com/en/thailand/insights/office-fit-out-cost-guide?sort=latest_update | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-06 | MY、PH、TH、VN | 4 | B |
| 387 | https://loanstreet.com.my/learning-centre/how-much-will-home-renovation-cost | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-21 | MY | 3 | C |
| 388 | https://www.dosm.gov.my/portal-main/release-content/special-release-for-building-and-structural-works-december-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-120 | MY | 3 | A |
| 389 | https://bernama.com/lite/news.php?id=2396739 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-03 | MY | 2 | B |
| 390 | https://dosm.gov.my/portal-main/release-content/construction-statistics-first-quarter-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-16 | MY | 2 | A |
| 391 | https://focusmalaysia.my/?p=236235 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-95 | MY | 2 | B |
| 392 | https://iqiglobal.com/blog/seo-title-4/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-05 | MY | 2 | C |
| 393 | https://mrem.bernama.com/viewsm.php?idm=49229 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-89 | MY | 2 | B |
| 394 | https://www.getfoundation.com.my/blog/cidb-contractor-registration-malaysia-grades-spkk-guide | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-39 | MY | 2 | C |
| 395 | https://www.propplace.my/guides/malaysia-property-market-2025-overview | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-07 | MY | 2 | C |
| 396 | https://bernama.com/bm/news.php?id=2325906 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-60 | MY | 1 | B |
| 397 | https://eiglaw.com/malaysia-revises-minimum-salary-for-employment-pass-applications-effective-june-1-2026/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-71 | MY | 1 | B |
| 398 | https://estatemarketpulse.com/2026/03/01/malaysia-property-market-2025/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-08 | MY | 1 | C |
| 399 | https://napic.jpph.gov.my/storage/app/media//3-penerbitan/Shahrul/Bahagian%20Inventori%20Harta%20Tanah/Laporan%20Jadual%20Status%20Harta%20Tanah/Q4%202025/Laporan%20Status%20Harta%20Tanah%202025.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-09 | MY | 1 | A |
| 400 | https://napic.jpph.gov.my/storage/app/media//3-penerbitan/Shahrul/Bahagian%20Pasaran%20Harta%20Tanah/Central%20Region%20Wilayah%20Tengah/Q4%202025/Central%20Region%202025.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-12 | MY | 1 | A |
| 401 | https://propcashflow.my/blog/renovation-costs-malaysia/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-23 | MY | 1 | C |
| 402 | https://qanvast.com/my/articles/how-much-does-it-cost-to-renovate-in-malaysia-928 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-22 | MY | 1 | C |
| 403 | https://qanvast.com/my/faq | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-47 | MY | 1 | C |
| 404 | https://realestateasia.com/commercial-office/news/kuala-lumpur-office-vacancy-falls-148-in-q2 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-89 | MY | 1 | C |
| 405 | https://rehdainstitute.com/wp-content/uploads/2024/07/Summary_NAPIC-Property-Market-Report-2023.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-106 | MY | 1 | B |
| 406 | https://rehdainstitute.com/wp-content/uploads/2025/05/NAPIC-Property-Market-2024-v2-For-Website.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-105 | MY | 1 | B |
| 407 | https://repositori.kpdn.gov.my/bitstream/123456789/3490/1/METRO%2024.09.2019.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-49 | MY | 1 | A |
| 408 | https://rsisinternational.org/journals/ijriss/articles/navigating-policy-challenges-in-malaysias-construction-sector-the-governmental-dilemma-on-the-issue-of-foreign-labour-shortage-in-malaysia/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-108 | MY | 1 | B |
| 409 | https://says.com/my/lifestyle/home-and-living/condo-renovation-malaysia | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-123 | MY | 1 | B |
| 410 | https://thesun.my/business/ikano-retail-owner-of-ikea-malaysia-posts-109b-turnover-for-fy24-md13102394/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-98 | MY | 1 | B |
| 411 | https://wmlaw.com.my/2023/05/15/new-cidb-regimes-for-foreign-contractors/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-66 | MY | 1 | B |
| 412 | https://www.aseanbriefing.com/doing-business-guide/malaysia/human-resources-and-payroll/salaries-minimum-wages-malaysia | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-111 | MY | 1 | B |
| 413 | https://www.bakermckenzie.com/en/insight/publications/2026/01/malaysia-expatriate-services-division-increases-employment-pass-salary | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-69 | MY | 1 | B |
| 414 | https://www.cbinsights.com/company/recommendmy/financials | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-90 | MY | 1 | C |
| 415 | https://www.coohom.com/article/interior-design-pricing-trends-in-malaysia-for-modern-homeowners | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-83 | MY | 1 | C |
| 416 | https://www.dosm.gov.my/portal-main/release-content/construction-statistics-q42025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-19 | MY | 1 | A |
| 417 | https://www.dosm.gov.my/portal-main/release-content/construction-statistics-second-quarter-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-17 | MY | 1 | A |
| 418 | https://www.dosm.gov.my/portal-main/release-content/construction-statistics-third-quarter-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-18 | MY | 1 | A |
| 419 | https://www.edgeprop.my/content/1915472/green-new-spec-inside-malaysia’s-industrial-sustainability-race | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-90 | MY | 1 | C |
| 420 | https://www.imarcgroup.com/malaysia-home-decor-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-28 | MY | 1 | C |
| 421 | https://www.kenresearch.com/malaysia-furniture-and-interior-design-market-krab6623 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-26 | MY | 1 | C |
| 422 | https://www.nst.com.my/amp/business/corporate/2023/10/966041/ikea-franchisee-ikano-posts-rm158bil-revenue-malaysia | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-67 | MY | 1 | B |
| 423 | https://www.nst.com.my/amp/business/corporate/2025/11/1312184/new-store-openings-lift-mr-diys-3q-results | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-93 | MY | 1 | B |
| 424 | https://www.statista.com/outlook/cmo/furniture/home-decor/malaysia | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-29 | MY | 1 | C |
| 425 | https://www.theborneopost.com/2025/02/18/tradition-meets-innovation-in-courts-raya-2025-campaign/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-102 | MY | 1 | B |
| 426 | https://www.threads.com/@malaysiauncapped/post/DWWc8eDkT8b/according-to-napi-cs-property-market-report-malaysia-recorded-completed-unsold | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-10 | MY | 1 | D |
| 427 | https://www.utusan.com.my/nasional/2024/08/jemaah-ditipu-boleh-tuntut-ganti-rugi-di-tribunal/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-50 | MY | 1 | B |
| 428 | https://zacharykhaw.com/2025/09/05/interior-design-cost-malaysia/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | MY-87 | MY | 1 | C |
| 429 | https://psa.gov.ph/content/construction-statistics-approved-building-permits-philippines-2024 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-01 | PH | 8 | A |
| 430 | https://quartr.com/events/wilcon-depot-inc-wlcon-q4-2025_FtvIy3IS | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-11、TA1-56 | PH | 4 | B |
| 431 | https://aedoconstruction.com/blog/house-renovation-cost-philippines-2026/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-45 | PH | 3 | C |
| 432 | https://tribune.net.ph/2026/03/30/wilcon-income-slips-3-despite-higher-sales | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-08、TA1-54 | PH | 3 | B |
| 433 | https://context.ph/2025/08/23/allhome-1h-profit-plunges-on-weak-property-demand/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-13 | PH | 2 | B |
| 434 | https://gulfnews.com/business/markets/pesos-new-normal-dollar-could-stay-above-60-bsp-data-1.500591425 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-08 | PH | 2 | B |
| 435 | https://gulfnews.com/business/property/beyond-supply-glut-manila-condo-market-faces-repricing-what-it-means-1.500630690 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-20 | PH | 2 | B |
| 436 | https://malaya.com.ph/weekly-features/property/construction-activities-decline-9-6-in-april-on-yr | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-05 | PH | 2 | B |
| 437 | https://plus.inquirer.net/business/wilcon-income-dips-on-cost-pressures/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-09、TA1-55 | PH | 2 | B |
| 438 | https://www.philstar.com/headlines/2026/05/29/2531214/pag-ibig-fund-raises-limit-housing-loans-p10-million | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-35、TD-99 | PH | 2 | B |
| 439 | https://abs-cbn.com/news/business/2025/3/31/pag-ibig-to-keep-housing-loan-rates-low-until-june-1823 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-101 | PH | 1 | B |
| 440 | https://aedoconstruction.com/blog/construction-labor-rates-philippines-2026/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-48 | PH | 1 | C |
| 441 | https://aedoconstruction.com/blog/office-fit-out-cost-philippines/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-46 | PH | 1 | C |
| 442 | https://bworldonline.com/?p=552187 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-77 | PH | 1 | B |
| 443 | https://bworldonline.com/economy/2026/05/20/750957/approved-building-permits-rise-2-in-march/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-06 | PH | 1 | B |
| 444 | https://davao.prc.gov.ph/node/6770 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-28 | PH | 1 | A |
| 445 | https://digital.cushmanwakefield.com/fitoutcostguide-03-2026-apac-regional-en-content-pds-office | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-01 | PH | 1 | B |
| 446 | https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/70820 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-76 | PH | 1 | A |
| 447 | https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/5/95421 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-53 | PH | 1 | A |
| 448 | https://eurobel.com.ph/blogs/finding-an-interior-designer-in-the-philippines/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-40 | PH | 1 | C |
| 449 | https://galathome.com/2023/10/01/how-much-are-interior-design-services-in-the-philippines/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-43 | PH | 1 | C |
| 450 | https://kyodonewsprwire.jp/release/202403067602 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-22 | PH | 1 | C |
| 451 | https://malaya.com.ph/weekly-features/property/cost-to-fit-out-spaces-in-manila-among-lowest-in-the-region | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-50 | PH | 1 | B |
| 452 | https://prc.gov.ph/node/8125 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-27 | PH | 1 | A |
| 453 | https://qaltik.com/business/what-is-the-average-cost-of-interior-design-for-a-condo-in-manila/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-44 | PH | 1 | C |
| 454 | https://rcbc.com/how-much-to-renovate-a-house-in-the-philippines | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-37 | PH | 1 | C |
| 455 | https://realestateasia.com/commercial-office/news/manila-q2-office-absorption-reaches-40400-sqm-vacancy-falls | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-92 | PH | 1 | C |
| 456 | https://tribune.net.ph/2022/09/04/housing-projects-pinag-uusapan | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-16 | PH | 1 | B |
| 457 | https://tribune.net.ph/2025/04/15/isabela-joins-nhmfcs-berde-program | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-102 | PH | 1 | B |
| 458 | https://www.eccp.com/storage/app/media/Advocacy/Materials/2025/eccp-position-on-pcab-licensing.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-30 | PH | 1 | B |
| 459 | https://www.gmanetwork.com/news/money/economy/950986/ncr-board-grants-p50-minimum-wage-hike/story/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-65 | PH | 1 | B |
| 460 | https://www.imarcgroup.com/philippines-home-decor-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-60 | PH | 1 | C |
| 461 | https://www.kenresearch.com/industry-reports/philippines-furniture-interiors-market.md | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-58 | PH | 1 | C |
| 462 | https://www.kenresearch.com/industry-reports/philippines-home-improvement-market.md | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-62 | PH | 1 | C |
| 463 | https://www.mexc.com/news/489231 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-71 | PH | 1 | D |
| 464 | https://www.prc.gov.ph/article/july-2026-licensure-examination-interior-designers-results-released-thirteen-13-working | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-29 | PH | 1 | A |
| 465 | https://www.statista.com/outlook/cmo/furniture/home-decor/philippines | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-61 | PH | 1 | C |
| 466 | https://www.statista.com/statistics/1403704/philippines-retail-price-index-of-construction-materials-ncr | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | PH-70 | PH | 1 | C |
| 467 | https://www.sunstar.com.ph/cebu/pag-ibig-expands-affordable-housing-loans-with-lower-rates | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-100 | PH | 1 | B |
| 468 | https://qanvast.com/sg/articles/what-are-the-expected-renovation-costs-for-hdb-flats-in-2026-3568 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-13 | SG | 4 | C |
| 469 | https://www.hdb.gov.sg/cs/infoweb/residential/living-in-an-hdb-flat/for-our-seniors/ease | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-71 | SG | 4 | A |
| 470 | https://www.case.org.sg/wp-content/uploads/2025/02/Media-Release-CASE-sees-prepayment-losses-more-than-quadruple-in-2024-entertainment-related-complaints-nearly-triple.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-01 | SG | 3 | B |
| 471 | https://www.era.com.sg/press-release/4q-2025-ura-real-estate-statistics-private-home-demand-momentum-carries-from-3q-2025-sets-firm-outlook-for-2026 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-71 | SG | 3 | C |
| 472 | https://www.gov.sg/article/5-things-to-know-if-your-home-is-undergoing-hip | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-74 | SG | 3 | A |
| 473 | https://qanvast.com/sg/articles/-3384 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-14 | SG | 2 | C |
| 474 | https://qanvast.com/sg/articles/hdb-optional-component-scheme-ocs-is-it-worth-opting-in-1873 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-68 | SG | 2 | C |
| 475 | https://www-web.itiger.com/news/1129153147 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-38 | SG | 2 | B |
| 476 | https://www.imarcgroup.com/singapore-construction-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-40 | SG | 2 | C |
| 477 | https://www.mti.gov.sg/Newsroom/Parliamentary-Replies/2022/07/Written-reply-to-PQ-on-renovation-contractors | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-04 | SG | 2 | A |
| 478 | https://dojobusiness.com/blogs/news/carpenter-project-pricing | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-96 | SG | 1 | C |
| 479 | https://ecdb.com/resources/sample-data/retailer/castlery | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-78 | SG | 1 | C |
| 480 | https://edgeprop.sg/amp/property-news/over-29000-hdb-flats-selected-407-mil-upgrading | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-29 | SG | 1 | B |
| 481 | https://edgeprop.sg/property-news/hdb-resale-price-growth-slows-million-dollar-flats-prices-gain-23-4q2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-20 | SG | 1 | B |
| 482 | https://insideretail.asia/2022/11/29/livspace-launches-experience-centres-in-singapore/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-73 | SG | 1 | B |
| 483 | https://links.sgx.com/1.0.0/corporate-announcements/0D6QYQB30LNU0IC8/874465_HHL%20Interim%20FS%20-%20FY2025%20Final.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-37 | SG | 1 | A |
| 484 | https://ohsem.me/2026/10/singapore-grade-a-office-market-posts-strongest-quarterly-rental-growth-since-2022-as-supply-constraints-intensify/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-69 | SG | 1 | B |
| 485 | https://qanvast.com/sg/interior-designers | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-59 | SG | 1 | C |
| 486 | https://qanvast.com/sg/renovation-calculator?variant=A | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-17 | SG | 1 | C |
| 487 | https://rafflescorporateservices.com/singapore-work-permit-2026-eligibility-quota-levy/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-35 | SG | 1 | C |
| 488 | https://realestateasia.com/commercial-office/news/singapore-cbd-office-vacancy-hits-nine-quarter-low | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-68 | SG | 1 | C |
| 489 | https://vulcanpost.com/721133/qanvast-match-homeowners-interior-designers-singapore | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-82 | SG | 1 | B |
| 490 | https://vulcanpost.com/910484/singapore-business-closures-2025/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-42 | SG | 1 | B |
| 491 | https://www.99.co/singapore/insider/hdb-plans-19600-bto-flats-in-2026-over-4000-with-shorter-waits/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-25 | SG | 1 | C |
| 492 | https://www.99.co/singapore/insider/hdb-ura-q42025-statistics/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-21 | SG | 1 | C |
| 493 | https://www.aseanbriefing.com/doing-business-guide/singapore/company-establishment/singapore-foreign-ownership-rules | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-85 | SG | 1 | B |
| 494 | https://www.asiaone.com/singapore/home-renovations-make-bulk-consumers-losses-2024-case | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-02 | SG | 1 | B |
| 495 | https://www.case.org.sg/casetrust/casetrust-accreditation-for-renovation-businesses/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-06 | SG | 1 | B |
| 496 | https://www.case.org.sg/wp-content/uploads/2025/08/Media-Release-CASE-sees-increase-in-prepayment-losses-for-the-beauty-industry-in-the-first-half-of-2025.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-74 | SG | 1 | B |
| 497 | https://www.edb.gov.sg/en/business-insights/insights/salary-threshold-for-new-employment-pass-applicants-to-be-raised-to-5600-from-2025.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-87 | SG | 1 | A |
| 498 | https://www.edgeprop.sg/property-news/singapore-construction-industry-grow-42-annually-2026-2029-linesight | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-41 | SG | 1 | B |
| 499 | https://www.era.com.sg/press-release/4q-2025-hdb-quarterly-report-hdb-resale-transactions-moderate-to-end-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-22 | SG | 1 | C |
| 500 | https://www.hdb.gov.sg/about-us/news-and-publications/press-releases/october-2025-bto-sales-exercise | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-24 | SG | 1 | A |
| 501 | https://www.ikea.com/sg/en/newsroom/corporate-news/ikano-retail-owner-of-ikea-singapore-posts-eur-1-08-billion-in-total-turnover-pub3bd2f4e0 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-83 | SG | 1 | C |
| 502 | https://www.income.com.sg/blog/home-renovations-cost-singapore | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-60 | SG | 1 | C |
| 503 | https://www.kenresearch.com/industry-reports/singapore-furniture-home-decor-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-39 | SG | 1 | C |
| 504 | https://www.mom.gov.sg/passes-and-permits/work-permit-for-foreign-worker/foreign-worker-levy/what-is-the-foreign-worker-levy | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-34 | SG | 1 | A |
| 505 | https://www.mti.gov.sg/newsroom/written-reply-to-pqs-on-disputes-arising-from-interior-design-and-renovation-firms/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-03 | SG | 1 | A |
| 506 | https://www.payscale.com/research/SG/Job=Interior_Designer/Salary/e86615f1/Mid-Career | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-91 | SG | 1 | C |
| 507 | https://www.propertyguru.com.sg/property-guides/ageing-hdb-flats-ideas-singapore-30624 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-65 | SG | 1 | C |
| 508 | https://www.singsaver.com.sg/personal-loan/blog/how-much-renovation-loan-can-i-get | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | SG-32 | SG | 1 | C |
| 509 | https://investor.indexlivingmall.com/storage/download/company-snapshots/20260312-ilm-company-snapshots-4q2025-en.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-86、TH-92 | TH | 6 | A |
| 510 | https://insideretail.asia/2026/04/01/why-are-thailands-diy-giants-losing-momentum/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-22 | TH | 4 | B |
| 511 | https://lssmedia.setlink.set.or.th/2025/3M/HMPRO-3M68-ListedCompanySnapshot-EN.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-42 | TH | 3 | A |
| 512 | https://lssmedia.setlink.set.or.th/2025/9M/HMPRO-9M68-ListedCompanySnapshot-EN.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-41、TH-23 | TH | 3 | A |
| 513 | https://neodecordesign.com/%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%95%E0%B8%81%E0%B9%81%E0%B8%95%E0%B9%88%E0%B8%87%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99%E0%B8%95%E0%B9%88%E0%B8%AD%E0%B8%95%E0%B8%A3%E0%B8%A1/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-34 | TH | 3 | C |
| 514 | https://www.businesstoday.co/business/25/02/2026/126296/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-02 | TH | 3 | B |
| 515 | https://www.markallcompany.com/blog/interior-design-cost-pricing-guide | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-33 | TH | 3 | C |
| 516 | https://investor.globalhouse.co.th/wp-content/uploads/2026/03/ManagementDiscussionAndAnalysis2025_EN_20260210.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-26 | TH | 2 | A |
| 517 | https://www.bernama.com/en/news.php?id=2479278 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-17 | TH | 2 | B |
| 518 | https://api.prod.pi.financial/cms/assets/480bc33a-db26-4b9d-a96c-c4566f28f085 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-83 | TH | 1 | B |
| 519 | https://asa.or.th/laws/news20170824/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-35 | TH | 1 | B |
| 520 | https://brandwiki.lazada.sg/nitori/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-25 | TH | 1 | C |
| 521 | https://download.asa.or.th/03media/04law/aa/cr52-upd63.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-52 | TH | 1 | B |
| 522 | https://gcc.go.th/2025/10/21/%E0%B8%AA%E0%B8%B3%E0%B8%99%E0%B8%B1%E0%B8%81%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%93%E0%B8%B0%E0%B8%81%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%84%E0%B8%B8%E0%B9%89-197/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-61 | TH | 1 | A |
| 523 | https://group.ikano/stories/ikano-retail/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-66 | TH | 1 | C |
| 524 | https://investor.globalhouse.co.th/wp-content/uploads/2025/10/ManagementDiscussionAndAnalysisQ3_EN_20251029.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-27 | TH | 1 | A |
| 525 | https://investor.indexlivingmall.com/storage/download/company-snapshots/20251126-ilm-company-snapshots-3q2025-en.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-87 | TH | 1 | A |
| 526 | https://investor.indexlivingmall.com/storage/download/company-snapshots/20260514-ilm-company-snapshots-1q2026-en.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-88 | TH | 1 | A |
| 527 | https://investor.lh.co.th/en/updates/press-releases/477/land-and-houses-unveils-2026-business-plan-targeting-thb-15-billion-in-bookings-thb-17-billion-in-property-transfers-and-thb-99-billion-in-rental-property-revenue | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-15 | TH | 1 | A |
| 528 | https://policywatch.thaipbs.or.th/article/economy-172 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-69 | TH | 1 | B |
| 529 | https://primo.co.th/%E0%B8%9A%E0%B8%97%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1/%E0%B8%A3%E0%B8%B5%E0%B9%82%E0%B8%99%E0%B9%80%E0%B8%A7%E0%B8%97%E0%B8%9A%E0%B9%89%E0%B8%B2%E0%B8%99/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-30 | TH | 1 | C |
| 530 | https://th.wikipedia.org/wiki/%E0%B8%AA%E0%B8%96%E0%B8%B2%E0%B8%9B%E0%B8%B1%E0%B8%95%E0%B8%A2%E0%B8%81%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%A0%E0%B8%B2%E0%B8%A2%E0%B9%83%E0%B8%99 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-53 | TH | 1 | D |
| 531 | https://www.bangkokbiznews.com/property/1124831 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-12 | TH | 1 | B |
| 532 | https://www.clodura.ai/directory/company/q-chang | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-82 | TH | 1 | C |
| 533 | https://www.cushmanwakefield.com/en/thailand/insights/bangkok-office-market-overview | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-91 | TH | 1 | B |
| 534 | https://www.expattaxthailand.com/th/easy-e-2025-tax-return/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-94 | TH | 1 | C |
| 535 | https://www.globalpropertyguide.com/asia/thailand/price-history | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-14 | TH | 1 | C |
| 536 | https://www.hlbthai.com/attention-shoppers-easy-e-receipt-personal-tax-deduction-campaign-for-2024-new-year/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-93 | TH | 1 | B |
| 537 | https://www.kaohoon.com/news/806401 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-78 | TH | 1 | B |
| 538 | https://www.krungsri.com/th/research/industry/summary-outlook/thailand-industry-outlook-summary-2025-2027 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-46 | TH | 1 | B |
| 539 | https://www.matichon.co.th/economy/news_5437917 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-90 | TH | 1 | B |
| 540 | https://www.reic.or.th/Upload/REIC-PressRelease-250828_682_1756368798_92679.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-06 | TH | 1 | A |
| 541 | https://www.thairath.co.th/money/economics/asean_economics/2892296 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-73 | TH | 1 | B |
| 542 | https://www.tpso.go.th/news/2507-0000000006 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-77 | TH | 1 | A |
| 543 | https://www.yamada-spire-th.com/wp-content/uploads/2023/09/Home-Improvement-and-Furnishing-Retail-Market-in-Thailand.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-87 | TH | 1 | C |
| 544 | https://www.yotathai.com/yotanews/law-architect-2549 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TH-38 | TH | 1 | C |
| 545 | https://finance.technews.tw/2026/06/25/taiwan-housing-market-more-houses-built-fewer-buyers-25-5-decline-nine-year-low/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-14 | TW | 4 | B |
| 546 | https://money.udn.com/money/story/5621/9014283 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-13 | TW | 3 | B |
| 547 | https://n.yam.com/Article/20260604841255 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-53 | TW | 3 | B |
| 548 | https://www.pro360.com.tw/price/20_ping_house_decoration | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-21 | TW | 3 | C |
| 549 | https://money.udn.com/money/story/5607/9747158 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-112 | TW | 2 | B |
| 550 | https://tw.stock.yahoo.com/news/%E7%89%B9%E5%8A%9B%E5%B1%8B10-29%E6%8E%9B%E7%89%8C%E4%B8%8A%E5%B8%82-%E4%B8%8A%E5%8D%8A%E5%B9%B4%E8%B3%BA%E8%B4%8F%E5%8E%BB%E5%B9%B4-125859576.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-11 | TW | 2 | C |
| 551 | https://udn.com/news/story/7239/9407547 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-05 | TW | 2 | B |
| 552 | https://w3.cpami.gov.tw/statisty/100/100_pdf/06_building/0c_building.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-30 | TW | 2 | A |
| 553 | https://www.abri.gov.tw/News_Content_Table.aspx?n=807&s=38057 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-26 | TW | 2 | A |
| 554 | https://www.ctee.com.tw/news/20260112701274-430201 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-08 | TW | 2 | B |
| 555 | https://www.money101.com.tw/blog/%E5%85%A7%E6%94%BF%E9%83%A8-%E4%BF%AE%E7%B9%95%E4%BD%8F%E5%AE%85%E8%B2%B8%E6%AC%BE-%E6%A2%9D%E4%BB%B6%E5%88%A9%E6%81%AF%E7%94%B3%E8%AB%8B | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-45 | TW | 2 | C |
| 556 | https://www.moneydj.com/kmdj/wiki/wikiviewer.aspx?keyid=3ac77f98-a84b-44fa-ac70-bf4188eb3176 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA1-12 | TW | 2 | C |
| 557 | https://www.pro360.com.tw/price/old_house_renovation | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-19 | TW | 2 | C |
| 558 | https://banks.tw/unsafe-and-old-buildings/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-54 | TW | 1 | C |
| 559 | https://ec.ltn.com.tw/article/breakingnews/4753996 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-47 | TW | 1 | B |
| 560 | https://hcdesign.com.tw/%E5%8D%B1%E8%80%81%E9%87%8D%E5%BB%BA/%E5%8D%B1%E8%80%81%E6%A2%9D%E4%BE%8B/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-53 | TW | 1 | C |
| 561 | https://house.ettoday.net/news/3238017 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-73 | TW | 1 | B |
| 562 | https://howroom.ai/posts/a/commercial-space-renovation-guide | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-60 | TW | 1 | C |
| 563 | https://into-atelier.com.tw/charge/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-65 | TW | 1 | C |
| 564 | https://jhlanddev.com.tw/%E5%8D%B1%E8%80%81%E7%8D%8E%E5%8B%B5%E6%87%B6%E4%BA%BA%E5%8C%85%EF%BD%9C%E5%8D%B1%E8%80%81%E7%8D%8E%E5%8B%B5%E7%94%B3%E8%AB%8B%E6%A2%9D%E4%BB%B6%EF%BC%9F%E7%8D%8E%E5%8B%B5%E4%B8%8A%E9%99%90%EF%BC%9F/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-51 | TW | 1 | C |
| 565 | https://money.udn.com/money/story/5621/9196803 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-72 | TW | 1 | B |
| 566 | https://news.cnyes.com/news/id/628493 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-84 | TW | 1 | B |
| 567 | https://play.google.com/store/apps/details?id=net.searchome.designer&hl=en_US | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TA2-81 | TW | 1 | C |
| 568 | https://service.mof.gov.tw/public/Data/statistic/class/9th/112.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-01 | TW | 1 | A |
| 569 | https://smart.businessweekly.com.tw/Reading/IndepArticle.aspx?id=6015022 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-41 | TW | 1 | B |
| 570 | https://udn.com/news/story/7241/9245511 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-23 | TW | 1 | B |
| 571 | https://vocus.cc/article/6213ff6efd89780001b9699a | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-C9 | TW | 1 | D |
| 572 | https://vocus.cc/article/68429352fd897800016a223d | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-22 | TW | 1 | D |
| 573 | https://w3.cpami.gov.tw/statisty/95/95_pdf/06_building/0c_building.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-29 | TW | 1 | A |
| 574 | https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvNDAwL3JlbGZpbGUvMC8xNjA0Ni81OTM3M2M1OC04NGUwLTQwZmItYWRiOS1hMGJhNzhkZDUxYWIucGRm&n=NC01LnBkZg%3D%3D&icon=.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-31 | TW | 1 | A |
| 575 | https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvNDAwL3JlbGZpbGUvMC8xODk2Ni8wY2E0YjMxOC03ZjY2LTQ0MzUtYjUxNS04OWYyYTljNDQwODAucGRm&n=NC01LnBkZg%3D%3D&icon=.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-32 | TW | 1 | A |
| 576 | https://ws.moi.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvNDAwL3JlbGZpbGUvMC8yMTA2MC8xYmJlNGI2Zi1hNWZlLTRmNDYtODZiYS1mMzAwYTZlNDQ5ZGMucGRm&n=NC01LnBkZg%3D%3D&icon=.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-33 | TW | 1 | A |
| 577 | https://www-ws.gov.taipei/001/Upload/461/relfile/22721/3504162/512168571471.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-49 | TW | 1 | A |
| 578 | https://www.businessinsider.tw/article/2424 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-74 | TW | 1 | B |
| 579 | https://www.businesstoday.com.tw/article/category/192008/post/202408070065/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-C8 | TW | 1 | D |
| 580 | https://www.commonhealth.com.tw/blog/3901 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-42 | TW | 1 | B |
| 581 | https://www.cushmanwakefield.com/en/south-korea/news/2026/04/contractor-confidence-rises-amid-strengthening-office-demand-across-asia-pacific | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-05 | TW | 1 | B |
| 582 | https://www.dahuandesign.com/faq/interior-design-cost/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-63 | TW | 1 | C |
| 583 | https://www.edh.tw/article/14351 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-40 | TW | 1 | C |
| 584 | https://www.gvm.com.tw/article/117211 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-10 | TW | 1 | B |
| 585 | https://www.laws.taipei.gov.tw/Law/File/0000398330 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-43 | TW | 1 | A |
| 586 | https://www.moi.gov.tw/News_Content.aspx?n=2905&s=328048 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TW-41 | TW | 1 | A |
| 587 | https://www.nlma.gov.tw/uploads/files/d50c4414dcd40fba0a1c3db7b638a778.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-48 | TW | 1 | A |
| 588 | https://www.pro360.com.tw/price/office_design | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-61 | TW | 1 | C |
| 589 | https://www.taipeitimes.com/News/biz/archives/2019/11/05/2003725245 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-15 | TW | 1 | B |
| 590 | https://www.ur.org.tw/mynews/view/2946 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-49 | TW | 1 | B |
| 591 | https://therealdeal.com/international/2026/03/31/japanese-homebuilders-pouring-into-american-market/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-59 | US | 2 | B |
| 592 | https://www2.jpx.co.jp/disc/59380/140120240219539414.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-87 | US | 1 | A |
| 593 | https://www.focus-economics.com/country-indicator/vietnam/exchange-rate/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-16 | VN | 3 | C |
| 594 | https://www.mordorintelligence.com/industry-reports/vietnam-furniture-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-01 | VN | 3 | C |
| 595 | https://baochinhphu.vn/nguon-cung-tang-gia-nha-chua-giam-102260117005432583.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-38 | VN | 2 | A |
| 596 | https://dantri.com.vn/bat-dong-san/vi-sao-nganh-noi-that-viet-nam-chua-ghi-dau-an-tren-the-gioi-20250607213731069.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-02 | VN | 2 | B |
| 597 | https://takenli.vn/chi-phi-lam-noi-that-chung-cu-70m2-bao-gia-kinh-nghiem-thuc-te/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-11 | VN | 2 | C |
| 598 | https://vietnamnews.vn/economy/1763814/ha-noi-apartment-market-sees-record-supply-clear-price-difference.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-26 | VN | 2 | B |
| 599 | https://vneconomy.vn/2025-thi-truong-cong-trinh-xanh-viet-nam-but-pha-ky-luc.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-96 | VN | 2 | B |
| 600 | https://vneconomy.vn/gia-chung-cu-o-mot-so-khu-vuc-da-tang-hon-40.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-36 | VN | 2 | B |
| 601 | https://www.cbrevietnam.com/insights/figures/hanoi-figures-q4-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-25 | VN | 2 | B |
| 602 | https://www.ceicdata.com/en/indicator/vietnam/exchange-rate-against-usd | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-01、TF-14 | VN | 2 | AB |
| 603 | https://www.kenresearch.com/industry-reports/vietnam-furniture-and-interior-design-market.md | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-10 | VN | 2 | C |
| 604 | https://baochinhphu.vn/nguoi-nuoc-ngoai-co-duoc-dau-tu-hoat-dong-thiet-ke-noi-that-102272847.htm | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-46 | VN | 1 | A |
| 605 | https://coda.io/@thietkenoithat/bao-gia-thiet-ke-van-phong | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-16 | VN | 1 | D |
| 606 | https://dauthau.asia/news/tu-lieu-cho-nha-thau/nha-thau-nuoc-ngoai-1748.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-52 | VN | 1 | C |
| 607 | https://diendandoanhnghiep.vn/acg-tao-suc-bat-tu-noi-dia-10165333.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-20 | VN | 1 | B |
| 608 | https://doanhnhan.baophapluat.vn/go-an-cuong-acg-sap-rot-196-ty-dong-co-tuc-hoan-thanh-80-ke-hoach-loi-nhuan-nam-2025-88438.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-19 | VN | 1 | B |
| 609 | https://doanhnhan.baophapluat.vn/thi-truong-xuat-khau-khoi-sac-lai-sau-thue-9-thang-cua-go-an-cuong-acg-tang-323-78729.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-18 | VN | 1 | B |
| 610 | https://edgebuildings.com/wp-content/uploads/2026/02/Official.VNGB-Q4-2025.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-97 | VN | 1 | B |
| 611 | https://edgebuildings.com/wp-content/uploads/2026/07/Official.VNGB_.Q2-2026.pdf | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TD-98 | VN | 1 | B |
| 612 | https://fdvn.vn/huong-dan-thu-tuc-cap-giay-phep-lao-dong-cho-nguoi-nuoc-ngoai-tai-viet-nam-theo-nghi-dinh-219-2025-nd-cp/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-57 | VN | 1 | B |
| 613 | https://moc.gov.vn/vn/tin-tuc/1269/87076/bo-xay-dung-cong-bo-thong-tin-ve-nha-o-va-thi-truong-bat-dong-san-trong-quy-ii-nam-2025.aspx | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-37 | VN | 1 | A |
| 614 | https://nhandan.vn/nhung-noi-dung-co-ban-cac-cam-ket-gia-nhap-wto-cua-viet-nam-post589471.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-48 | VN | 1 | B |
| 615 | https://nief.mof.gov.vn/kinh-te-xa-hoi/bien-dong-ty-gia-nam-2025-va-du-bao-tinh-hinh-nam-2026-11839.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-17 | VN | 1 | A |
| 616 | https://phapluatdoanhnghiep.vn/10-diem-moi-ve-nguoi-lao-dong-nuoc-ngoai-tai-viet-nam-tu-ngay-07-8-2025-theo-nghi-dinh-219-2025-nd-cp/ | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-55 | VN | 1 | B |
| 617 | https://theinvestor.vn/hcmc-apartment-prices-continue-to-rise-as-supply-hits-10-year-low-in-h1-d16321.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-27 | VN | 1 | B |
| 618 | https://theinvestor.vn/hcmc-apartment-prices-keep-climbing-as-supply-shortfall-persists-d17469.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-28 | VN | 1 | B |
| 619 | https://vnexpress.net/bai-toan-18-ty-usd-cua-xuat-khau-go-noi-that-4843845.html | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-03 | VN | 1 | B |
| 620 | https://www.cushmanwakefield.com/en/vietnam/news/2026/09/ho-chi-minh-city-office-market-approaches-balance-as-flight-to-quality-continues-to-shape-demand | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TC-93 | VN | 1 | B |
| 621 | https://www.dnse.com.vn/senses/tin-tuc/bctc-quy-22025-acg-loi-nhuan-q22025-tang-1677-so-voi-cung-ky-lai-13794-ty-dong-35102318 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-17 | VN | 1 | B |
| 622 | https://www.exchange-rates.org/exchange-rate-history/usd-vnd-2025 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TF-15 | VN | 1 | C |
| 623 | https://www.housenews.jp/house/10847 | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | TE-57 | VN | 1 | B |
| 624 | https://www.imarcgroup.com/vietnam-flooring-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-07 | VN | 1 | C |
| 625 | https://www.imarcgroup.com/vietnam-interior-design-software-market | 未驗證（環境網路政策封鎖開頁） | 待驗證 | 待驗證 | 待驗證 | 待驗證 | VN-06 | VN | 1 | C |

## 失敗率與 r1 等級（§3 門檻）

**門檻規則目前無法套用**：§3 的失敗率＝「無法開啟或內容不符」的 URL 占抽驗與附錄 URL 的比例；本次 0 條被開啟，分子與分母都不存在。這不是「失敗率 0%」，也不是「失敗率 100%」，而是「未測」。

| 驗證結果（未來） | §3 規則 | 對 r1 的意義 |
|---|---|---|
| ≤10% 無法開啟或不符 | 維持原等級 | 各來源依（c）的類型等級使用；A／B 級且雙源者可標【實際】；r1 可作為 V2 的正式來源之一 |
| 10–20% | 整體降一級；未驗證數字一律【示意】 | A→B、B→C、C→D；r1 中所有未逐條驗證的數字（包括比較表大部分格子）只能標【示意】，不能單獨支撐 V2 頭條 |
| >20% | r1 降為 C 級 | r1 只能當搜尋線索；V2 任何【實際】數字都不能以 r1 為來源，必須回到原始頁面或其他報告 |

**驗證前的風險訊號**（不是失敗率，只供排程參考）：r1 第 7 章 1,733 條來源中，203 條（11.7%）自己註記了風險：對應或年份為推定 98 條、僅讀到標題 84 條、候選出處 23 條、多個候選 URL 6 條。這些條目驗證失敗的機率較高；若全部失敗，失敗率約 12%，落在「降一級」區間。

**建議驗證順序**：(1) 支撐 12 市場比較表與摘要的約 60 個 URL（本表（a）已列 49 個）；(2) 與 V1 共用的 242 個 URL（驗一次、兩份報告同時受惠）；(3) 附錄其餘 URL。每條紀錄：頁面是否開啟、數字是否逐字出現、年份與定義是否相符；任一項不符即判「不符」。

## （c）§2 來源分級：r1 第 7 章全部 1,733 條

### 分級規則（依序套用，先命中者為準）

| 規則代碼 | 等級 | 內容 |
|---|---|---|
| A1／A1k／A1e | A | 政府、央行、統計機關、法院、國會與法規原文：政府網域（.gov.*、.go.jp、.go.kr、.go.th、.go.id、.gov.vn、.nic.in 等）、央行與統計機關、官方與常用法規全文資料庫（含 lawphil、thuvienphapluat、indiankanoon）；機構欄為政府機關者（A1k）；法規全文或主管機關文件經其他第三方網站轉載者（A1e） |
| A2／A2k／A2r | A | 上市公司申報：交易所揭露系統（巨潮、港交所、SET、SGX、JPX 等）、公司 IR 文件（年報、決算說明、MD&A）；經金融資訊站轉載的決算資料（A2r） |
| B2／B2k／B2o／B2l／B2s／B2r | B | 產業公會與協會、研究機構（含矢野、CERIK、艾瑞）、國際顧問公司（C&W、JLL、CBRE、Knight Frank、Arcadis、Turner & Townsend 等）、律師與會計師事務所的法規解讀、券商與銀行研究部、文件分享站轉載的顧問報告（依原文件分級） |
| B3k／B3m | B | 主流新聞與財經媒體（依網域與機構欄關鍵字判定，涵蓋繁中、簡中、日、韓、泰、越、印尼、英文媒體） |
| B4 | B | 官方數據彙整站（Worldometer、TradingEconomics、CEIC 等轉載 IMF、央行、統計局數據）與金融資訊站轉載公告 |
| B5 | B | 大學、學術期刊、大學圖書館 |
| C1 | C | 市調公司與產業研究網站（Mordor、IMARC、Ken、Grand View、Credence、Statista、Euromonitor、智研、前瞻等）及新聞稿發布平台 |
| C2／C2k | C | 平台自報、業者價格頁、設計與裝修公司收費頁、房產與比價內容網站 |
| C3 | C | 求職、薪資、公司資料聚合站（JobStreet、Glassdoor、Tracxn、Crunchbase 類） |
| C4 | C | 企業官網一般頁面（非申報文件）、代辦與顧問業者行銷頁 |
| D1 | D | 部落格、論壇、自媒體（知乎、搜狐號、網易訂閱、vocus、note、brunch、Threads 等）、維基、個人網站 |
| D2 | D | 無法辨識機構類型 |
| D3 | D | 台灣「候選出處」（r1 自己註明數字與 URL 對應未確認） |

判定方式：先看網域清單，再看機構欄關鍵字，最後對 299 條無法自動判定或自動判定有誤的來源逐條人工指定（附錄的「規則」欄可追溯每一條的依據）。

### 邊界案例與處理

- **媒體報導業者或平台自己的推估**（例：TW-23 經濟日報報導 100室內設計的 5,500 億）：來源記 B，但數字本身依原始發布者記 C；裁決紀錄以數字的等級為準。
- **媒體轉載官方統計**（例：經濟日報報導內政部屋齡統計）：記 B，並在裁決紀錄寫「B（原始 A）」；驗證時應改引原始機關頁面，成功後可升 A。
- **上市公司文件引用協會數字**（例：CN-03 山西科新年報引述 CBDA 住宅裝修 2.2 萬億）：文件本身記 A，但該數字的實際來源是協會（B），裁決時以 B 計。
- **第三方網站轉載法規全文**（例：thuvienphapluat、lawphil、casenote、LBOX、律所上傳的法規重印本）：記 A（A1e），但驗證時必須與官方公報版本比對，尤其是條文是否為現行版本（菲律賓 EO 175 已被 EO 113 取代即為一例）。
- **國營或官方背景機構的行銷內容**（例：印尼 Pegadaian、HDFC、Bank Mega Syariah 的裝修費用文章）：依內容性質記 C（業者價格指南），不因機構背景升級。
- **在地仲介的研究報告**（中原、美聯、ERA、Square Yards、PropertyGuru）：記 C（平台／仲介自報）；國際顧問公司（C&W、JLL、CBRE、Knight Frank、Colliers、Savills）記 B。
- **自媒體轉載研究機構數據**（例：CN-20 搜狐轉載奧維雲網）：依轉載者記 D；原始機構另註，驗證時應找原始報告。
- **入口網站新聞**（騰訊新聞、新浪財經、LINE TODAY、Yahoo 新聞）：記 B；但入口網站上的自媒體內容不易辨識，驗證時若作者非媒體機構應降為 D。
- **泰文維基**（TH-53，泰國 500 m² 門檻的唯一來源）：記 D，即使內容引用法規。
- **台灣候選出處**（TW-C1、C2、C8、C9）：URL 本身多為主流媒體，但 r1 註明「數字與 URL 對應未確認」，依 §2「AI 未附 URL 的數字」的精神記 D。
- **未開頁**：依 §2，「無法開啟的 URL」屬 D。本表的等級是「若驗證通過」的上限；驗證失敗者一律降 D。

### 分級結果：各市場／主題與全體

| 第 7 章分節 | A | B | C | D | 合計 | A＋B 占比 |
|---|---|---|---|---|---|---|
| 7.1 台灣（TW） | 24 | 18 | 11 | 5 | 58 | 72% |
| 7.2 日本（JP） | 22 | 20 | 22 | 5 | 69 | 61% |
| 7.3 韓國（KR） | 12 | 72 | 13 | 4 | 101 | 83% |
| 7.4 新加坡（SG） | 14 | 26 | 55 | 4 | 99 | 40% |
| 7.5 香港（HK） | 29 | 46 | 16 | 4 | 95 | 79% |
| 7.6 中國大陸（CN） | 37 | 61 | 19 | 16 | 133 | 74% |
| 7.7 馬來西亞（MY） | 26 | 57 | 38 | 8 | 129 | 64% |
| 7.8 泰國（TH） | 33 | 46 | 16 | 2 | 97 | 81% |
| 7.9 越南（VN） | 9 | 30 | 17 | 2 | 58 | 67% |
| 7.10 印尼（ID） | 6 | 49 | 39 | 0 | 94 | 59% |
| 7.11 菲律賓（PH） | 13 | 39 | 28 | 1 | 81 | 64% |
| 7.12 印度（IN） | 3 | 43 | 58 | 5 | 109 | 42% |
| 7.13 主題 A（一）：零售、建材商、設計施工、建商精裝、買翻賣（TA1） | 22 | 82 | 11 | 7 | 122 | 85% |
| 7.14 主題 A（二）＋主題 B：平台、數位與 AI（TA2） | 5 | 89 | 46 | 13 | 153 | 61% |
| 7.15 主題 C：商業空間 fit-out（TC） | 1 | 81 | 27 | 8 | 117 | 70% |
| 7.16 主題 D：永續、高齡化與補助（TD） | 31 | 43 | 27 | 1 | 102 | 73% |
| 7.17 主題 E：跨國擴張案例（TE） | 8 | 60 | 14 | 2 | 84 | 81% |
| 7.18 主題 F：總體、住宅與匯率（TF） | 10 | 14 | 4 | 0 | 28 | 86% |
| 7.19 台灣候選出處（數字與 URL 對應未確認；本報告引用時一律標「候選出處」與低信心） | 0 | 0 | 0 | 4 | 4 | 0% |
| **全體** | **305** | **876** | **461** | **91** | **1733** | **68%** |

各規則命中數：B3k 547、C2 257、A1 243、B2 176、B3m 90、D1 86、C4 79、C1 68、C3 41、A2 38、B2k 21、C2k 16、B4 15、A2r 11、A1e 8、B2l 7、B2o 5、B2s 5、B5 5、B2r 5、D3 4、A1k 3、A2k 2、D2 1。

讀法：A＋B 占比最低的是新加坡（40%）與印度（42%），主因是單價與設計費幾乎只有業者價格頁（C）；台灣候選出處 4 條全為 D。A 級（官方、法規、申報）比例最高的是台灣（41%）、主題 F（36%）、泰國（34%）、日本（32%）、香港（31%）。

## （d）§7 幻覺與偏誤檢查清單

| # | 檢查項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | 有沒有「太整齊」的數字且無來源？ | 通過 | 以程式掃描第 0–6 章所有「x.0%」與 CAGR 字樣（28 處），28 處前後 60 字內都有來源編號；附錄 12 列 CAGR 全部來自市調公司並註明定義與預測性質。未發現無來源的整齊數字。 |
| 2 | 有沒有把亞太總數當作某國數字？ | 通過 | 附錄把區域列獨立標為 APAC（6 列）、ALL（4 列）、US（3 列）；國家列中出現區域字樣者（如印尼列的「東協五國居家修繕 99.7 億 USD」、台灣列的全球市場 977.2 億／589.1 億 USD）都在定義欄標明是區域或全球，且 r1 第 6 章判定不採用。§2.1 只對 5 個有官方 GDP 分母的市場做人均檢查，沒有拆分亞太數字。 |
| 3 | 有沒有把協會認證寫成法定證照？ | 通過（附反向註記） | r1 把 CaseTrust、インテリアプランナー、インテリアコーディネーター、HKIDA、KICC 都明確標為「協會認證」；台灣、馬來西亞、菲律賓、泰國的法定性都附法源。反向問題：印尼把 UU 2/2017 第 70 條下強制的職能證書（SKK，經 LSP 核發）寫成「無執照，只有 LSP 職能認證」，低估了法定性（見裁決紀錄 ID-09）。 |
| 4 | 有沒有引用 2019–2021（或更舊）的數字當 2025 現況？ | 部分未通過 | 附錄有 63 列年份 ≤2021，全部標了年份。但正文有 2 處把舊值當現況使用：台灣「最新官方家數停在 2011 年底」（4,969 家；國土署 2026-04 已公布約 1.7 萬家，見 TWB-05）；日本比較表「中古屋交易占比 14.5%（2018）」，國交省另有 2023 年新系列 40.4%（見 JP-08）。韓國規模用 2020 推估（30조）有標年份，屬可接受；中國 14.4% 與印度 Census 2011 是最新一次普查，屬可接受。 |
| 5 | 幣別換算是否錯位（日圓／韓元／越南盾／印尼盾千倍錯誤）？ | 通過 | 以程式依 r1 第 0 章匯率表重算：(i) 第 0–6 章「原幣＝億 USD」金額換算（命中於第 2、4 章） 19 處，最大偏差 0.48%；(ii) 第 2 章 12 市場單價換算 64 個端點（含每坪、每평、每呎、每 sq ft 換每 m²），最大偏差 0.57%；(iii) §2.1 人均與占 GDP 8 組，最大偏差 0.9%（中國奧維人均 352 vs 重算 355）；(iv) 第 0 章交叉匯率（TWD 每 1 JPY 0.2084、每 1 KRW 0.02193、每 1 VND 0.001198、每 1 IDR 0.001891）重算相符；(v) 附錄中日圓、韓元、越南盾、印尼盾計價的 172 列換成 USD 後，每 m² 單價 22 列、日薪 6 列、每戶金額 11 列都落在合理區間（每 m² 5–20,000 USD、日薪 2–1,000 USD、每戶 50–2,000,000 USD），同一指標跨列沒有 50 倍以上落差。未發現千倍錯誤。 |
| 6 | 來源 URL 是否存在、內容是否對得上？ | 未驗證（無法執行） | 環境封鎖開頁，0 條驗證；r1 自己也未開頁。風險訊號：203 條來源自註「僅讀到標題」「推定」「候選」或多個候選 URL；附錄 3 列來源編號與 URL 只對應一半（交叉匯率列）；比較表印度人均 GDP 引 TF-20，應為 TF-18。 |
| 7 | 是否只用英文來源而缺在地語言？ | 部分未通過 | 全體 1,733 條中在地語言約 1,043 條（60%），日、韓、中、泰、越、印尼都以在地語言為主；但菲律賓只有 3 條在地語言來源（下限 5）、印度印地語約 7 條、越南只搜尋 13 次。新加坡、印度、菲律賓的在地英文來源不計入在地語言。 |
| 8 | 是否把預測（2030）寫成現況（2025）？ | 通過（附註） | 附錄 15 列未來年份（2027–2034）全部在指標或定義欄標「預測」「目標」或「計畫」；正文韓國「2025 預測 37조」、台灣「2026 有望持續成長」都標為預測。附註：台灣 5,500 億在 2026-01 發布時是「上看」的預估值，r1 標「2025 推估」，V2 應寫明發布時為預估。 |

**裁決過程中發現的其他實質問題**（不屬上列 8 項，但影響可用性，詳見 `adjudication-log.md`）：

1. 法規版本過時：菲律賓引用 EO 175（第 12 版外資負面清單，2022），但第 13 版 EO 113 已於 2026-05-02 生效；r1 據此提出「台方持股 ≤40% 合資」建議（PH-11）。
2. 定義錯置：越南設計費 150,000–200,000 VND／m² 的來源，r1 附錄自己註明是「辦公室」設計報價，但比較表放在住宅設計費欄（VN-06）。
3. 取媒體值而非官方值：馬來西亞 LAM 登記室內設計師「約 165 人」取自媒體，LAM 官方 2024-08 統計為 639 人（MY-09）。
4. 漏搜較新官方值：台灣室內裝修業家數停在 2011 年（TWB-05）；台灣持證人才以三年流量推論「很少」，未對照約 3.3 萬人的存量（TWB-06）。
5. 跨國排名的前提：r1 用單一 C 級業者媒體的日本每 m² 價格，得出「台灣低於日本」；結論方向可能正確，但只有一個 C 級來源（HL-03）。

## 附錄：r1 第 7 章逐條分級

欄位：來源#｜等級｜規則代碼｜網域｜機構／作者（截斷 40 字）｜預驗風險。規則代碼對照上方「分級規則」。

| 來源# | 等級 | 規則 | 網域 | 機構／作者 | 預驗風險 |
|---|---|---|---|---|---|
| TW-01 | A | A1 | service.mof.gov.tw | 財政部 | — |
| TW-02 | A | A1 | fia.gov.tw | 財政部財政資訊中心 | — |
| TW-03 | A | A1 | mof.gov.tw | 財政部全球資訊網 | — |
| TW-04 | A | A1 | segis.moi.gov.tw | 內政部統計地理資訊服務網（SEGIS） | — |
| TW-05 | A | A1 | stat.gov.tw | 行政院主計總處 | — |
| TW-06 | C | C2 | fh-accounting.com | fh-accounting.com（會計事務所） | — |
| TW-07 | C | C4 | yih-chyun.com.tw | 益群聯合會計師事務所 | — |
| TW-08 | C | C4 | wanchicpa.com.tw | wanchicpa.com.tw（會計師事務所） | — |
| TW-09 | C | C4 | twomoney.com.tw | 錢錢會計記帳士事務所 | — |
| TW-10 | B | B3k | gvm.com.tw | 遠見雜誌 | — |
| TW-11 | C | C1 | gii.tw | 360iResearch／GII | — |
| TW-12 | C | C1 | gii.tw | Coherent Market Insights／GII | — |
| TW-13 | B | B3k | money.udn.com | 經濟日報（udn） | 對應或年份為推定 |
| TW-14 | B | B3k | finance.technews.tw | 科技新報 TechNews 財經 | — |
| TW-15 | B | B3k | news.cnyes.com | 鉅亨網（記者張欽發） | 對應或年份為推定 |
| TW-16 | B | B3k | ctee.com.tw | 工商時報 | 對應或年份為推定 |
| TW-17 | B | B3k | today.line.me | LINE TODAY | 對應或年份為推定 |
| TW-18 | B | B3k | today.line.me | LINE TODAY | 對應或年份為推定 |
| TW-19 | C | C2 | pro360.com.tw | PRO360 達人網 | — |
| TW-20 | C | C2 | pro360.com.tw | PRO360 達人網 | 對應或年份為推定 |
| TW-21 | C | C2 | pro360.com.tw | PRO360 達人網 | — |
| TW-22 | D | D1 | vocus.cc | vocus 方格子 | 對應或年份為推定 |
| TW-23 | B | B3k | udn.com | 聯合新聞網（udn） | — |
| TW-24 | B | B3k | udn.com | 聯合新聞網／經濟日報（udn） | — |
| TW-25 | B | B3m | merit-times.com.tw | 人間福報 | — |
| TW-26 | A | A1 | abri.gov.tw | 內政部建築研究所 | — |
| TW-27 | A | A1 | data.gov.tw | 政府資料開放平臺（內政部） | — |
| TW-28 | A | A1 | nlma.gov.tw | 內政部國土管理署 | — |
| TW-29 | A | A1 | w3.cpami.gov.tw | 內政部營建署 | — |
| TW-30 | A | A1 | w3.cpami.gov.tw | 內政部營建署 | — |
| TW-31 | A | A1 | ws.moi.gov.tw | 內政部 | — |
| TW-32 | A | A1 | ws.moi.gov.tw | 內政部 | — |
| TW-33 | A | A1 | ws.moi.gov.tw | 內政部 | — |
| TW-34 | A | A1 | me.moe.edu.tw | 教育部 | — |
| TW-35 | A | A1 | glrs.moi.gov.tw | 內政部 | — |
| TW-36 | A | A1 | nlma.gov.tw | 內政部國土管理署 | — |
| TW-37 | B | B3k | ctee.com.tw | 工商時報 | 對應或年份為推定 |
| TW-38 | B | B3k | ctee.com.tw | 工商時報 | 對應或年份為推定 |
| TW-39 | B | B3k | money.udn.com | 經濟日報（udn） | 對應或年份為推定 |
| TW-40 | D | D1 | ljd5712.pixnet.net | 臻坊（痞客邦部落格） | — |
| TW-41 | A | A1 | moi.gov.tw | 內政部統計處 | — |
| TW-42 | A | A1 | nlma.gov.tw | 內政部國土管理署 | — |
| TW-43 | A | A1 | law.moj.gov.tw | 法務部全國法規資料庫 | 對應或年份為推定 |
| TW-44 | C | C4 | dreamincloud.com | 周泳成建築師事務所（dreamincloud.com） | — |
| TW-45 | B | B4 | opengovtw.com | opengovtw.com（民間彙整政府開放資料） | — |
| TW-46 | A | A1 | dgbas.gov.tw | 行政院主計總處 | — |
| TW-47 | A | A1 | ws.dgbas.gov.tw | 行政院主計總處 | — |
| TW-48 | A | A1 | stat.gov.tw | 行政院主計總處 | — |
| TW-49 | A | A1k | www-ws.gov.taipei | 臺北市政府（建築管理相關單位） | 對應或年份為推定 |
| TW-50 | D | D1 | roychiang.pixnet.net | 江榮裕建築師＋居逸室內設計（痞客邦） | 對應或年份為推定 |
| TW-51 | D | D1 | tchid.net | tchid.net | 對應或年份為推定 |
| TW-52 | B | B2k | ntcaa.org.tw | 新北市建築師公會 | 對應或年份為推定 |
| TW-53 | B | B3k | n.yam.com | 蕃薯藤 yam 新聞 | — |
| TW-54 | A | A1 | cpc.ey.gov.tw | 行政院消費者保護會 | — |
| TW-55 | B | B2k | dqpa.org | 台灣住宅品質消費者保護協會 | — |
| TW-56 | D | D1 | ezlawyer.tw | 易律網 | — |
| TW-57 | B | B2o | arch.org.tw | arch.org.tw | — |
| TW-58 | C | C2k | puloapp.com | PULO 裝潢平台 | — |
| JP-01 | B | B2k | dreamnews.jp | 矢野経済研究所（ドリームニュース轉載） | — |
| JP-02 | B | B2 | s-housing.jp | 新建ハウジング | — |
| JP-03 | B | B3k | online.ibnewsnet.com | 日刊産業新聞（ibnewsnet） | — |
| JP-04 | B | B2 | yano.co.jp | 矢野経済研究所 | — |
| JP-05 | A | A2r | nikkei.com | 日本経済新聞 | — |
| JP-06 | B | B2 | yano.co.jp | 矢野経済研究所 | — |
| JP-07 | B | B2 | chord.or.jp | 住宅リフォーム・紛争処理支援センター | — |
| JP-08 | B | B3m | htonline.sohjusha.co.jp | ハウジング・トリビューン（創樹社） | — |
| JP-09 | B | B2 | s-housing.jp | 新建ハウジング | — |
| JP-10 | C | C2 | homes.co.jp | LIFULL HOME'S（吉崎誠二） | — |
| JP-11 | C | C2 | arc-navi.shikaku.co.jp | 総合資格 arc-navi | — |
| JP-12 | C | C2 | arc-navi.shikaku.co.jp | 総合資格 arc-navi | — |
| JP-13 | B | B3k | xtech.nikkei.com | 日経クロステック | — |
| JP-14 | A | A1 | stat.go.jp | 総務省統計局 | — |
| JP-15 | A | A1 | stat.go.jp | 総務省統計局 | — |
| JP-16 | A | A1 | stat.go.jp | 総務省統計局 | — |
| JP-17 | B | B2 | murc.jp | 三菱UFJリサーチ&コンサルティング | — |
| JP-18 | B | B3m | nippon.com | nippon.com | — |
| JP-19 | A | A1 | www1.mlit.go.jp:8088 | 国土交通省 | — |
| JP-20 | B | B2 | reins.or.jp | 東日本不動産流通機構 | — |
| JP-21 | D | D1 | rbayakyu.jp | R.bay 夜久 | — |
| JP-23 | A | A1 | mlit.go.jp | 国土交通省 | — |
| JP-24 | A | A1 | www1.mlit.go.jp | 国土交通省 | — |
| JP-25 | B | B2 | reform-online.jp | リフォーム産業新聞 | — |
| JP-26 | B | B2 | reform-online.jp | リフォーム産業新聞 | — |
| JP-27 | B | B2 | reform-online.jp | リフォーム産業新聞 | — |
| JP-28 | C | C3 | onecareer.jp | ワンキャリア | — |
| JP-29 | D | D1 | atopico.com | atopico | — |
| JP-30 | B | B2 | tsr-net.co.jp | 東京商工リサーチ | — |
| JP-31 | B | B2 | tsr-net.co.jp | 東京商工リサーチ | — |
| JP-32 | B | B3k | jiji.com | 時事通信 | — |
| JP-33 | A | A2r | nikkei.com | 日本経済新聞 | — |
| JP-34 | C | C2 | shuken-renovation.jp | shuken-renovation（翻修業者媒體） | — |
| JP-35 | C | C2 | forest.toppan.com | TOPPAN リフォトル | — |
| JP-36 | C | C2 | journal.zerorenovation.co.jp | ゼロリノベ | — |
| JP-37 | C | C2 | furureno.jp | フルリノ（furureno） | — |
| JP-38 | C | C2 | rehome-navi.com | リショップナビ（rehome-navi） | — |
| JP-39 | C | C2 | crexgroup.com | CREX | — |
| JP-40 | C | C2 | crexgroup.com | CREX | — |
| JP-41 | A | A1 | pref.saitama.lg.jp | 埼玉県 | — |
| JP-42 | A | A1 | pref.osaka.lg.jp | 大阪府 | — |
| JP-43 | A | A1 | www1.mlit.go.jp:8088 | 国土交通省 | — |
| JP-44 | A | A1 | pref.aichi.jp | 愛知県 | — |
| JP-45 | A | A1 | pref.miyazaki.lg.jp | 宮崎県 | — |
| JP-46 | C | C4 | biz.moneyforward.com | マネーフォワード クラウド | — |
| JP-47 | C | C2k | office-tree.jp | office-tree（行政書士） | — |
| JP-48 | C | C2 | suumo.jp | SUUMO リフォームタイムズ | — |
| JP-49 | B | B2 | zennichi.or.jp | 全日本不動産協会（全日ラビー） | — |
| JP-50 | D | D1 | chuko-mikata.jp | 中古住宅のミカタ | — |
| JP-51 | C | C2 | smtrc.jp | 三井住友トラスト不動産 | — |
| JP-52 | C | C4 | mec-h.com | 三井不動産（mec-h） | — |
| JP-53 | C | C2 | allabout.co.jp | All About | — |
| JP-54 | A | A1 | kokusen.go.jp | 国民生活センター | — |
| JP-55 | A | A1 | kokusen.go.jp | 国民生活センター | — |
| JP-56 | A | A1 | kokusen.go.jp | 国民生活センター | — |
| JP-57 | A | A1 | mlit.go.jp | 国土交通省 | — |
| JP-58 | C | C2k | shigyo.co.jp | 行政書士事務所（shigyo.co.jp） | — |
| JP-59 | C | C2k | shigyo.co.jp | 行政書士事務所（shigyo.co.jp） | — |
| JP-60 | B | B2l | aplawjapan.com | 渥美坂井法律事務所（Atsumi & Sakai） | — |
| JP-61 | C | C2 | crexgroup.com | CREX | — |
| JP-62 | D | D1 | shopowner-support.net | ショップオーナーサポート | — |
| JP-63 | A | A1 | mlit.go.jp | 国土交通省 | — |
| JP-64 | A | A1 | mlit.go.jp | 国土交通省 | — |
| JP-65 | D | D1 | genba-media.jp | 現場メディア（genba-media） | — |
| JP-66 | C | C4 | howroad.co.jp | HOW ROAD TO 工事業 | — |
| JP-67 | A | A1 | zaimu.metro.tokyo.lg.jp | 東京都財務局 | — |
| JP-68 | A | A2r | nikkei.com | 日本経済新聞 | — |
| JP-69 | C | C2 | arc-navi.shikaku.co.jp | 総合資格 arc-navi | — |
| JP-70 | A | A1 | mlit.go.jp | 国土交通省 | — |
| KR-01 | B | B2 | cerik.re.kr | 한국건설산업연구원（CERIK）보도자료 | — |
| KR-02 | C | C2 | ikld.kr | 국토일보 | 對應或年份為推定 |
| KR-03 | B | B2k | ancnews.kr | 대한건축사협회 건축사신문 | 對應或年份為推定 |
| KR-04 | B | B3k | conslove.co.kr | 한국건설신문 | 對應或年份為推定 |
| KR-05 | B | B3k | seoulfn.com | 서울파이낸스 | 對應或年份為推定 |
| KR-06 | B | B2 | cerik.re.kr | 한국건설산업연구원 | — |
| KR-07 | B | B3k | m.dnews.co.kr | 대한경제 | — |
| KR-08 | B | B3k | koscaj.com | 대한전문건설신문（引신영증권） | 對應或年份為推定 |
| KR-09 | B | B3k | dnews.co.kr | 대한경제 | — |
| KR-10 | B | B3k | opinionnews.co.kr | 오피니언뉴스 | — |
| KR-11 | B | B3k | edaily.co.kr | 이데일리 | 對應或年份為推定 |
| KR-12 | B | B3m | magazine.hankyung.com | 한경매거진&북 | — |
| KR-13 | B | B2k | codil.or.kr | 대한건설정책연구원（RICON）／CODIL 收錄 | — |
| KR-14 | B | B3k | koscaj.com | 대한전문건설신문 | — |
| KR-15 | B | B2 | kosca.or.kr | 대한전문건설협회（KOSCA） | — |
| KR-16 | B | B3m | consline.co.kr | 건설라인（consline） | — |
| KR-17 | C | C2k | sankun.com | 산군（sankun）部落格 | — |
| KR-18 | B | B2 | eiec.kdi.re.kr | 국가데이터처（原 통계청）／KDI 경제정보센터轉載 | — |
| KR-19 | B | B3k | insightkorea.co.kr | 인사이트코리아 | — |
| KR-20 | B | B3k | newsis.com | 뉴시스 | — |
| KR-21 | B | B3k | m.news.nate.com | 네이트 뉴스 | — |
| KR-22 | B | B3k | m.news.nate.com | 네이트 뉴스 | — |
| KR-23 | B | B3m | g-enews.com | 글로벌이코노믹 | — |
| KR-24 | B | B3k | ftoday.co.kr | 파이낸셜투데이 | — |
| KR-25 | C | C2 | saramin.co.kr | 사람인 | — |
| KR-26 | B | B3k | smedaily.co.kr | 중소기업신문 | 對應或年份為推定 |
| KR-27 | B | B3k | fntimes.com | 한국금융신문 | — |
| KR-28 | B | B3m | bloter.net | 블로터 | 對應或年份為推定 |
| KR-29 | B | B3k | etoday.co.kr | 이투데이 | — |
| KR-30 | B | B3k | wowtale.net | 와우테일 | — |
| KR-31 | C | C2 | ohstory.io | 버킷플레이스（오늘의집）官方新聞稿 | — |
| KR-32 | B | B3k | businesspost.co.kr | 비즈니스포스트 | — |
| KR-33 | B | B3k | byline.network | 바이라인네트워크 | — |
| KR-34 | C | C4 | demoday.co.kr | 데모데이（demoday） | 僅讀到標題、對應或年份為推定 |
| KR-35 | B | B3k | daily.hankooki.com | 데일리한국 | — |
| KR-36 | B | B3k | biz.heraldcorp.com | 헤럴드경제 | — |
| KR-37 | B | B3k | ebn.co.kr | 이비엔（EBN） | — |
| KR-38 | B | B3k | thebell.co.kr | 더벨 | — |
| KR-39 | B | B3m | sisaweek.com | 시사위크 | — |
| KR-40 | C | C2 | jobkorea.co.kr | 잡코리아 | — |
| KR-41 | B | B3k | dealsite.co.kr | 딜사이트 | — |
| KR-42 | B | B3k | newstomato.com | 뉴스토마토 | — |
| KR-43 | B | B2s | stock.pstatic.net | 證券公司研究報告（네이버증권收錄） | — |
| KR-44 | B | B3k | datanews.co.kr | 데이터뉴스 | — |
| KR-45 | B | B2k | kosca24.or.kr | 대한전문건설협회 지부 | — |
| KR-46 | B | B2k | icms.or.kr | 대한전문건설협회等 | — |
| KR-47 | D | D1 | archisketch.substack.com | archisketch（Substack） | 對應或年份為推定 |
| KR-48 | A | A1 | korea.kr | 국가데이터처（原통계청）／대한민국 정책브리핑 | — |
| KR-49 | A | A1 | korea.kr | 통계청／정책브리핑 | — |
| KR-50 | B | B2 | eiec.kdi.re.kr | KDI 경제교육·정보센터轉載 | — |
| KR-51 | B | B3k | m.news.nate.com | 네이트 뉴스 | — |
| KR-52 | B | B2 | kbthink.com | KB국민은행（KB think） | — |
| KR-53 | A | A1 | reb.or.kr | 한국부동산원 | — |
| KR-54 | B | B2 | eiec.kdi.re.kr | 국토교통부（KDI 경제정보센터轉載） | — |
| KR-55 | B | B3k | m-economynews.com | M이코노미뉴스 | — |
| KR-56 | B | B3k | m.news.nate.com | 네이트 뉴스 | — |
| KR-57 | B | B3k | edaily.co.kr | 이데일리（引직방） | — |
| KR-58 | B | B3k | mt.co.kr | 머니투데이 | — |
| KR-59 | B | B3k | v.daum.net | 다음 뉴스 | 對應或年份為推定 |
| KR-60 | B | B3k | sedaily.com | 서울경제 | 對應或年份為推定 |
| KR-61 | C | C2 | ajd.co.kr | 아파트 인테리어 業者部落格（ajd.co.kr） | 對應或年份為推定 |
| KR-62 | C | C2 | ajd.co.kr | 同上 | — |
| KR-63 | C | C2 | ajd.co.kr | 同上 | — |
| KR-64 | C | C2 | jipbro.com | 집브로（jipbro） | 對應或年份為推定 |
| KR-65 | C | C2 | soomgo.com | 숨고（Soomgo） | — |
| KR-66 | D | D1 | qplace.kr | 큐플레이스（qplace）社群 | — |
| KR-67 | B | B2 | kicc.or.kr | 한국인테리어건설협회（KICC） | — |
| KR-68 | C | C2k | allvisakorea.com | 行政士部落格（allvisakorea） | — |
| KR-69 | B | B3m | magazine.hankyung.com | 한경매거진&북 | — |
| KR-70 | B | B3k | koscaj.com | 대한전문건설신문 | — |
| KR-71 | B | B2k | codil.or.kr | 한국건설산업연구원（CODIL 收錄） | — |
| KR-72 | A | A1 | law.go.kr | 국가법령정보센터（법제처） | — |
| KR-73 | A | A1 | moleg.go.kr | 법제처 법령해석 | — |
| KR-74 | A | A1 | law.go.kr | 국가법령정보센터（국토교통부告示） | — |
| KR-75 | A | A1 | easylaw.go.kr | 찾기쉬운 생활법령정보（법제처） | — |
| KR-76 | A | A1 | easylaw.go.kr | 찾기쉬운 생활법령정보（법제처） | — |
| KR-77 | B | B3k | aptn.co.kr | 아파트관리신문 | — |
| KR-78 | D | D1 | lawtalk.co.kr | 로톡（LawTalk）法律諮詢 | — |
| KR-79 | A | A1e | casenote.kr | 케이스노트（casenote） | — |
| KR-80 | B | B2 | eiec.kdi.re.kr | 공정거래위원회（KDI 경제정보센터轉載） | — |
| KR-81 | B | B2 | theliving.co.kr | 월간 THE LIVING | — |
| KR-82 | C | C2 | phmkorea.com | PHM ZINE | — |
| KR-83 | D | D1 | lawwizice.blogspot.com | 部落格（lawwizice） | — |
| KR-84 | B | B3k | newsclaim.co.kr | 뉴스클레임 | 對應或年份為推定 |
| KR-85 | B | B3k | srtimes.kr | SR타임스 | — |
| KR-86 | B | B3k | m.sedaily.com | 서울경제 | — |
| KR-87 | B | B3m | intn.co.kr | 일간NTN | — |
| KR-88 | B | B3k | jjan.kr | 전북일보 | — |
| KR-89 | B | B3k | khan.co.kr | 경향신문 | 僅讀到標題 |
| KR-90 | B | B2k | info.cak.or.kr | 대한건설협회（CAK） | — |
| KR-91 | B | B2k | cak.or.kr | 대한건설협회 | — |
| KR-92 | B | B3k | m.news.nate.com | 네이트 뉴스 | — |
| KR-93 | B | B2k | csr.co.kr | 건설계약연구원 | — |
| KR-94 | A | A1 | law.go.kr | 국가법령정보센터（법제처） | — |
| KR-95 | A | A1e | lbox.kr | 엘박스（LBOX） | — |
| KR-96 | B | B2k | cak.or.kr | 대한건설협회 | — |
| KR-97 | A | A1 | molit.go.kr | 국토교통부 | — |
| KR-98 | B | B3k | fnnews.com | 파이낸셜뉴스 | — |
| KR-99 | B | B3k | fnnews.com | 파이낸셜뉴스 | — |
| KR-100 | B | B3m | kharn.kr | KHARN | 對應或年份為推定 |
| KR-101 | B | B2k | ricon.re.kr | 대한건설정책연구원（RICON） | 僅讀到標題、對應或年份為推定 |
| SG-01 | B | B2 | case.org.sg | Consumers Association of Singapore (CASE | — |
| SG-02 | B | B3k | asiaone.com | AsiaOne | — |
| SG-03 | A | A1 | mti.gov.sg | Ministry of Trade and Industry (MTI) | — |
| SG-04 | A | A1 | mti.gov.sg | MTI | — |
| SG-05 | A | A1 | mti.gov.sg | MTI | — |
| SG-06 | B | B2 | case.org.sg | CASE／CaseTrust | — |
| SG-07 | C | C2 | homematch.sg | HomeMatch | — |
| SG-08 | C | C4 | adevo.sg | Adevo | — |
| SG-09 | A | A1 | hdb.gov.sg | Housing & Development Board (HDB) | — |
| SG-10 | A | A1k | bcaa.edu.sg | BCA Academy | — |
| SG-11 | A | A1 | mnd.gov.sg | Ministry of National Development (MND) | 對應或年份為推定 |
| SG-12 | C | C2 | renonation.sg | Renonation | — |
| SG-13 | C | C2 | qanvast.com | Qanvast | — |
| SG-14 | C | C2 | qanvast.com | Qanvast | 對應或年份為推定 |
| SG-15 | C | C2 | dollarsandsense.sg | Dollars and Sense | — |
| SG-16 | C | C2 | qanvast.com | Qanvast | — |
| SG-17 | C | C2 | qanvast.com | Qanvast | — |
| SG-18 | C | C2 | qanvast.com | Qanvast | — |
| SG-19 | C | C2 | qanvast.com | Qanvast | — |
| SG-20 | B | B3k | edgeprop.sg | EdgeProp Singapore | — |
| SG-21 | C | C2 | 99.co | 99.co | — |
| SG-22 | C | C2 | era.com.sg | ERA Singapore | — |
| SG-23 | C | C2 | era.com.sg | ERA Singapore | — |
| SG-24 | A | A1 | hdb.gov.sg | HDB | — |
| SG-25 | C | C2 | 99.co | 99.co | — |
| SG-26 | C | C2 | stackedhomes.com | Stacked Homes | — |
| SG-27 | B | B3k | edgeprop.sg | EdgeProp Singapore | — |
| SG-28 | C | C2 | 99.co | 99.co | — |
| SG-29 | B | B3k | edgeprop.sg | EdgeProp Singapore | — |
| SG-30 | C | C2 | propertyguru.com.sg | PropertyGuru | — |
| SG-31 | A | A1 | mnd.gov.sg | MND | 僅讀到標題 |
| SG-32 | C | C2 | singsaver.com.sg | SingSaver | — |
| SG-33 | C | C2 | singsaver.com.sg | SingSaver | — |
| SG-34 | A | A1 | mom.gov.sg | Ministry of Manpower (MOM) | — |
| SG-35 | C | C4 | rafflescorporateservices.com | Raffles Corporate Services | — |
| SG-36 | C | C4 | singaporeemploymentagency.com | Singapore Employment Agency | — |
| SG-37 | A | A2 | links.sgx.com | Hafary Holdings Ltd | — |
| SG-38 | B | B3k | www-web.itiger.com | Tiger Brokers News | — |
| SG-39 | C | C1 | kenresearch.com | Ken Research | — |
| SG-40 | C | C1 | imarcgroup.com | IMARC Group | — |
| SG-41 | B | B3k | edgeprop.sg | EdgeProp Singapore | — |
| SG-42 | B | B3k | vulcanpost.com | Vulcan Post | — |
| SG-43 | B | B3k | asianews.network | Asia News Network | 對應或年份為推定 |
| SG-44 | B | B3m | theindependent.sg | The Independent Singapore | — |
| SG-45 | B | B3k | malaymail.com | Malay Mail | — |
| SG-46 | B | B3k | mustsharenews.com | MustShareNews | — |
| SG-47 | A | A1 | mlaw.gov.sg | Ministry of Law (MinLaw) | — |
| SG-48 | B | B2 | case.org.sg | CASE | — |
| SG-49 | D | D1 | theonlinecitizen.com | The Online Citizen | 僅讀到標題 |
| SG-50 | D | D1 | fixfirst.sg | FixFirst | — |
| SG-51 | C | C2k | homejourney.sg | HomeJourney（blog） | — |
| SG-52 | C | C2 | stackedhomes.com | Stacked Homes（中文版） | 僅讀到標題 |
| SG-53 | C | C2 | propertynet.sg | PropertyNet.sg | 僅讀到標題 |
| SG-54 | B | B5 | bizbeat.nus.edu.sg | NUS BizBeat | 僅讀到標題 |
| SG-55 | D | D1 | thesingaporean.sg | The Singaporean | — |
| SG-56 | A | A1 | mnd.gov.sg | MND | 僅讀到標題 |
| SG-57 | C | C1 | astuteanalytica.com | Astute Analytica | 僅讀到標題 |
| SG-58 | D | D1 | sixides.com | Sixides | 對應或年份為推定 |
| SG-59 | C | C2 | qanvast.com | Qanvast | — |
| SG-60 | C | C2 | income.com.sg | Income Insurance（blog） | — |
| SG-61 | C | C2 | megafurniture.sg | Megafurniture（零售商部落格） | — |
| SG-62 | B | B3m | homeanddecor.com.sg | Home & Decor Singapore | — |
| SG-63 | C | C2 | qanvast.com | Qanvast | — |
| SG-64 | B | B3m | womensweekly.com.sg | Women's Weekly Singapore | 對應或年份為推定 |
| SG-65 | C | C2 | propertyguru.com.sg | PropertyGuru | — |
| SG-66 | C | C2 | propertynet.sg | PropertyNet.sg | 對應或年份為推定 |
| SG-67 | C | C2 | propertynet.sg | PropertyNet.sg | 對應或年份為推定 |
| SG-68 | C | C2 | propertynet.sg | PropertyNet.sg | 對應或年份為推定 |
| SG-69 | B | B3k | edgeprop.sg | EdgeProp Singapore | 僅讀到標題 |
| SG-70 | C | C2 | stackedhomes.com | Stacked Homes | — |
| SG-71 | C | C2 | era.com.sg | ERA Singapore | — |
| SG-72 | A | A1 | ura.gov.sg | Urban Redevelopment Authority (URA) | 僅讀到標題 |
| SG-73 | B | B3k | edgeprop.sg | EdgeProp Singapore | — |
| SG-74 | B | B2 | case.org.sg | CASE | — |
| SG-75 | C | C2 | qanvast.com | Qanvast | — |
| SG-76 | C | C2 | ohmyhome.com | Ohmyhome | — |
| SG-77 | C | C4 | homerenoguru.sg | HomeRenoGuru | — |
| SG-78 | C | C3 | ecdb.com | ECDB | — |
| SG-79 | B | B3k | vulcanpost.com | Vulcan Post | — |
| SG-80 | C | C3 | castlery-inc.careerplug.com | Castlery Inc.（CareerPlug） | — |
| SG-81 | C | C3 | accio.com | Accio | — |
| SG-82 | B | B3k | insideretail.asia | Inside Retail Asia | 對應或年份為推定 |
| SG-83 | C | C4 | ikea.com | IKEA Singapore Newsroom／Ikano Retail | — |
| SG-84 | B | B3k | insideretail.asia | Inside Retail Asia | 對應或年份為推定 |
| SG-85 | B | B2 | aseanbriefing.com | ASEAN Briefing（Dezan Shira） | — |
| SG-86 | C | C2 | terraadvisoryservices.com | Terra Advisory Services | — |
| SG-87 | A | A1 | edb.gov.sg | Economic Development Board (EDB) | — |
| SG-88 | B | B2 | assets.ey.com | EY | — |
| SG-89 | C | C2 | envoyglobal.com | Envoy Global | — |
| SG-90 | C | C2 | payscale.com | Payscale | — |
| SG-91 | C | C2 | payscale.com | Payscale | — |
| SG-92 | C | C2 | payscale.com | Payscale | — |
| SG-93 | C | C3 | apply.workable.com | Fuku（Workable） | — |
| SG-94 | C | C3 | sg.jobstreet.com | Jobstreet Singapore | — |
| SG-95 | C | C3 | skillup.sg | SkillUp.sg | — |
| SG-96 | C | C2k | dojobusiness.com | Dojo Business（blog） | — |
| SG-97 | C | C2 | smartcalculator.sg | SmartCalculator.sg | — |
| SG-98 | C | C2 | hometrust.sg | Hometrust.sg | — |
| SG-99 | B | B3m | homeanddecor.com.sg | Home & Decor Singapore | 僅讀到標題 |
| HK-01 | A | A1 | info.gov.hk | 政府統計處（政府新聞公報） | — |
| HK-02 | A | A1 | info.gov.hk | Census and Statistics Department (GovHK  | — |
| HK-03 | A | A1 | censtatd.gov.hk | Census and Statistics Department | — |
| HK-04 | A | A1 | info.gov.hk | Census and Statistics Department | — |
| HK-05 | A | A1 | info.gov.hk | Census and Statistics Department | — |
| HK-06 | A | A1 | info.gov.hk | Census and Statistics Department | — |
| HK-07 | C | C2 | moneyhero.com.hk | MoneyHero | — |
| HK-08 | C | C4 | sc.com | 渣打銀行（香港） | — |
| HK-09 | C | C2 | homejournal.com | HomeJournal | — |
| HK-10 | B | B3k | stheadline.com | 星島日報 | — |
| HK-11 | B | B3k | businesstimes.com.hk | 香港財經時報 HKBT | — |
| HK-12 | B | B3m | epochtimes.com | 大紀元 | — |
| HK-13 | C | C2 | hkdecoman.com | 裝修佬（hkdecoman） | — |
| HK-14 | C | C2 | decoration2.com | 裝修易（decoration2） | — |
| HK-15 | B | B3k | stheadline.com | 星島日報 | — |
| HK-16 | A | A1 | bd.gov.hk | 屋宇署 | — |
| HK-17 | A | A1 | bd.gov.hk | 屋宇署 | — |
| HK-18 | A | A1 | bd.gov.hk | 屋宇署 | — |
| HK-19 | A | A1 | landreg.gov.hk | 土地註冊處 | — |
| HK-20 | A | A1 | legco.gov.hk | 土地註冊處／立法會 | — |
| HK-21 | B | B3k | hk.epochtimes.com | 大紀元時報（香港） | — |
| HK-22 | C | C2 | hk.centanet.com | 中原地產 | — |
| HK-23 | B | B3k | finance.mingpao.com | 明報財經 | — |
| HK-24 | B | B3m | businessfocus.io | BusinessFocus | — |
| HK-25 | B | B3k | hkcd.com.hk | 香港商報 | — |
| HK-26 | B | B3k | businesstimes.com.hk | 香港財經時報 HKBT | — |
| HK-27 | B | B3k | hkcna.hk | 香港中通社（hkcna） | — |
| HK-28 | B | B3k | news.qq.com | 騰訊新聞 | — |
| HK-29 | A | A1 | info.gov.hk | 香港特區政府新聞公報 | — |
| HK-30 | B | B3k | hk01.com | 香港01（研數所） | 僅讀到標題 |
| HK-31 | A | A1 | bd.gov.hk | 屋宇署 | — |
| HK-32 | B | B3k | stheadline.com | 星島日報 | — |
| HK-33 | A | A1 | devb.gov.hk | 發展局 | — |
| HK-34 | A | A1 | devb.gov.hk | 發展局 | — |
| HK-35 | C | C1 | acnnewswire.com | ACN Newswire | — |
| HK-36 | C | C1 | acnnewswire.com | ACN Newswire | — |
| HK-37 | B | B3m | globalcapital.com | GlobalCapital | — |
| HK-38 | B | B4 | tipranks.com | TipRanks | — |
| HK-39 | D | D1 | stockn.xueqiu.com | 梁志天設計集團（雪球轉載） | — |
| HK-40 | B | B3k | stockopedia.com | Stockopedia（Reuters 簡訊） | — |
| HK-40b | C | C4 | jangho.com | 江河创建集团股份有限公司 | 僅讀到標題 |
| HK-41 | C | C1 | secure.businesswire.com | ResearchAndMarkets（BusinessWire） | — |
| HK-42 | C | C1 | businesswire.com | ResearchAndMarkets（BusinessWire） | — |
| HK-43 | D | D2 | fitoutawards.ie | Fit Out Awards（愛爾蘭） | 僅讀到標題 |
| HK-44 | B | B2 | jll.com | JLL | 僅讀到標題 |
| HK-45 | A | A1 | data.gov.hk | 政府統計處（資料一線通 data.gov.hk） | — |
| HK-46 | B | B3k | hk01.com | 香港01 | 僅讀到標題 |
| HK-47 | B | B3k | ps.hket.com | 香港經濟日報 | 僅讀到標題 |
| HK-48 | B | B3k | hk01.com | 香港01 | 僅讀到標題 |
| HK-49 | B | B3k | dotdotnews.com | 點新聞 | — |
| HK-50 | B | B3k | news.now.com | now 新聞 | — |
| HK-51 | B | B3k | global.udn.com | 轉角國際（聯合新聞網） | 僅讀到標題 |
| HK-52 | B | B3k | news.rthk.hk | 香港電台 RTHK | — |
| HK-53 | B | B3k | cna.com.tw | 中央社（CNA） | — |
| HK-54 | B | B3m | thewitnesshk.com | 法庭線 The Witness | — |
| HK-55 | B | B3m | thewitnesshk.com | 法庭線 The Witness | 僅讀到標題 |
| HK-56 | B | B3m | thewitnesshk.com | 法庭線 The Witness | — |
| HK-57 | B | B3k | hkcourtnews.com | 庭刊 hkcourtnews.com | — |
| HK-58 | B | B3k | stheadline.com | 星島日報 | — |
| HK-59 | B | B3k | hk01.com | 香港01 | — |
| HK-60 | A | A1 | info.gov.hk | 香港特區政府新聞公報 | 僅讀到標題 |
| HK-61 | B | B3k | stheadline.com | 星島日報 | — |
| HK-62 | D | D1 | spyan-jour.hkbu.edu.hk | 香港浸會大學新聞系實習平台 | — |
| HK-63 | B | B3k | hk01.com | 香港01 | — |
| HK-64 | B | B3k | stheadline.com | 星島日報 | — |
| HK-65 | B | B3k | stheadline.com | 星島日報 | — |
| HK-66 | B | B3k | wenweipo.com | 香港文匯報 | — |
| HK-67 | B | B3m | finance730.com.hk | Finance730 | — |
| HK-68 | B | B5 | hkapi.lib.cuhk.edu.hk | 香港中文大學圖書館（香港社團檔案） | — |
| HK-69 | B | B5 | dc.lib.polyu.edu.hk | 香港理工大學圖書館 | — |
| HK-70 | A | A1 | info.gov.hk | 政府統計處（政府新聞公報） | — |
| HK-71 | A | A1 | info.gov.hk | 政府統計處（政府新聞公報） | — |
| HK-72 | A | A1 | info.gov.hk | 政府統計處（政府新聞公報） | — |
| HK-73 | A | A1 | censtatd.gov.hk | 政府統計處 | — |
| HK-74 | B | B2 | media.arcadis.com | 凱諦思香港有限公司（Arcadis） | 僅讀到標題 |
| HK-75 | A | A1 | data.gov.hk | 政府統計處（資料一線通 data.gov.hk） | — |
| HK-76 | A | A1 | bd.gov.hk | 屋宇署 | — |
| HK-77 | C | C3 | www2.ctgoodjobs.hk | CTgoodjobs（課程轉載） | 僅讀到標題 |
| HK-78 | B | B3k | businesstimes.com.hk | 香港財經時報 HKBT | 僅讀到標題 |
| HK-79 | B | B3k | businesstimes.com.hk | 香港財經時報 HKBT | 僅讀到標題 |
| HK-80 | B | B3k | hk01.com | 香港01 | 僅讀到標題 |
| HK-81 | A | A1 | censtatd.gov.hk | 政府統計處 | — |
| HK-82 | D | D1 | gotohui.com | 聚汇数据（gotohui） | — |
| HK-83 | A | A1 | devb.gov.hk | 發展局 | 僅讀到標題 |
| HK-84 | C | C2 | acdesign.com.hk | 藝創室內設計 | 僅讀到標題 |
| HK-85 | A | A1 | legco.gov.hk | 立法會 | — |
| HK-86 | A | A1 | districtcouncils.gov.hk | 深水埗區議會 | — |
| HK-87 | A | A1 | gia.info.gov.hk | 香港特區政府 | — |
| HK-88 | A | A1 | districtcouncils.gov.hk | 九龍城區議會 | — |
| HK-89 | C | C2 | air-corporate.com | Air Corporate | 對應或年份為推定 |
| HK-90 | B | B2 | asiabriefing.com | Asia Briefing（Dezan Shira & Associates） | — |
| HK-91 | C | C4 | ayp-group.com | AYP Group | — |
| HK-92 | B | B2 | china-briefing.com | China Briefing | — |
| HK-93 | C | C4 | tetraconsultants.com | Tetra Consultants | — |
| HK-94 | B | B2l | lexmundi.com | Lex Mundi | — |
| CN-01 | B | B2 | cbda.cn | 中裝新網（中國建築裝飾協會官網）轉載 | — |
| CN-02 | B | B2 | cbda.cn | 中裝新網（CBDA） | — |
| CN-03 | A | A2 | static.cninfo.com.cn | 巨潮資訊 | — |
| CN-04 | C | C1 | m.chinabgao.com | 報告大廳 | — |
| CN-05 | C | C1 | chinabgao.com | 報告大廳 | — |
| CN-06 | B | B2 | cbda.cn | 中裝新網（CBDA） | — |
| CN-07 | B | B2 | cbda.cn | 中裝新網（CBDA） | — |
| CN-08 | A | A1 | stats.gov.cn | 國家統計局 | — |
| CN-09 | B | B3k | thepaper.cn | 澎湃新聞 | — |
| CN-10 | B | B3k | m.jiemian.com | 界面新聞 | — |
| CN-11 | B | B3m | tech.ifeng.com | 鳳凰網科技 | — |
| CN-12 | B | B3m | tmtpost.com | 鈦媒體 | — |
| CN-13 | B | B3m | cs.com.cn | 中證網 | — |
| CN-14 | B | B3k | m.thepaper.cn | 澎湃新聞／港灣商業觀察 | — |
| CN-15 | B | B3k | lanjinger.com | 藍鯨財經 | — |
| CN-16 | B | B3k | news.qq.com | 騰訊新聞 | — |
| CN-17 | B | B3k | m.bjnews.com.cn | 新京報 | — |
| CN-18 | B | B2k | fangchan.com | 中房網（中國房地產業協會） | — |
| CN-19 | B | B3k | m.haofangdp.com | 克而瑞好房點評網 | — |
| CN-20 | D | D1 | sohu.com | 搜狐（轉載奧維雲網） | — |
| CN-21 | B | B3k | donews.com | DoNews 專欄 | — |
| CN-22 | C | C1 | m.chinabgao.com | 報告大廳 | — |
| CN-23 | D | D1 | zhuanlan.zhihu.com | 知乎 | — |
| CN-24 | B | B3k | finance.sina.cn | 新浪財經 | — |
| CN-25 | B | B2 | zhongzhihui.oss-cn-beijing.aliyuncs.com | 艾瑞諮詢（iResearch） | — |
| CN-26 | A | A1 | news.cn | 新華網 | — |
| CN-27 | B | B3k | cn.chinadaily.com.cn | 中國日報中文網 | — |
| CN-28 | B | B3k | news.10jqka.com.cn | 同花順財經 | — |
| CN-29 | C | C1 | chinabaogao.com | 中國報告網 | — |
| CN-30 | B | B3m | ccn.com.cn | 中國消費網 | — |
| CN-31 | B | B3k | xhby.net | 新華日報（交匯點） | — |
| CN-32 | A | A1 | sz.gov.cn | 深圳市人民政府 | — |
| CN-33 | B | B3k | stcn.com | 證券時報 | — |
| CN-34 | A | A1 | shanghai.gov.cn | 上海市人民政府 | — |
| CN-35 | A | A1 | sww.sh.gov.cn | 上海市商務委員會 | — |
| CN-36 | A | A1 | sww.sh.gov.cn | 上海市商務委員會 | — |
| CN-37 | A | A1 | news.cn | 新華網 | — |
| CN-38 | A | A1 | sz.gov.cn | 深圳市人民政府 | — |
| CN-39 | A | A1e | fadada.com | 法大大 | — |
| CN-40 | A | A1 | gov.cn | 中國政府網政策庫 | — |
| CN-41 | A | A1 | img.yichang.gov.cn | 宜昌市人民政府 | — |
| CN-42 | D | D1 | zhuanlan.zhihu.com | 知乎 | — |
| CN-43 | A | A1e | cncccg.com | 中化學交通建設集團（轉載） | — |
| CN-44 | C | C4 | hjxy99.com | 華建信源 | — |
| CN-45 | A | A1 | news.cn | 新華網 | — |
| CN-46 | B | B3k | cqn.com.cn | 中國質量新聞網 | — |
| CN-47 | B | B3m | ccn.com.cn | 中國消費網 | — |
| CN-48 | B | B3m | focus.cn | 搜狐焦點 | — |
| CN-49 | B | B3m | cmrnn.com.cn | 中國市場監管新聞網 | — |
| CN-50 | D | D1 | m.sdlycyw.com | sdlycyw | — |
| CN-51 | B | B3k | yicai.com | 第一財經 | — |
| CN-52 | B | B3k | m.huxiu.com | 虎嗅 | — |
| CN-53 | C | C1 | bg.qianzhan.com | 前瞻產業研究院 | — |
| CN-54 | C | C1 | aigc.idigital.com.cn | 樹懶生活 | — |
| CN-55 | C | C2 | zjbhi.com | 深圳市中經百匯信息諮詢 | — |
| CN-56 | A | A1 | shanghai.gov.cn | 上海市人民政府 | — |
| CN-57 | D | D1 | post.smzdm.com | 什麼值得買 | — |
| CN-58 | D | D1 | baogaobox.com | 遠瞻慧庫 | — |
| CN-59 | D | D1 | zhuanlan.zhihu.com | 知乎 | — |
| CN-60 | D | D1 | 163.com | 網易訂閱 | — |
| CN-61 | C | C2 | to8to.com | 土巴兔裝修大學 | — |
| CN-62 | B | B3k | xinminweekly.com.cn | 新民週刊 | — |
| CN-63 | D | D1 | m.sohu.com | 搜狐 | — |
| CN-64 | D | D1 | zhuanlan.zhihu.com | 知乎 | — |
| CN-65 | D | D1 | zhuanlan.zhihu.com | 知乎 | — |
| CN-66 | C | C2 | to8to.com | 土巴兔裝修大學 | — |
| CN-67 | C | C2 | to8to.com | 土巴兔裝修網 | — |
| CN-68 | C | C2 | to8to.com | 土巴兔裝修大學 | — |
| CN-69 | C | C2 | zx123.cn | 裝信通網 | — |
| CN-70 | C | C2 | m.ikongjian.com | 愛空間裝修網 | — |
| CN-71 | D | D1 | zhuanlan.zhihu.com | 知乎 | — |
| CN-72 | D | D1 | sohu.com | 搜狐 | — |
| CN-73 | A | A1 | mofcom.gov.cn | 商務部 | — |
| CN-74 | A | A1 | mofcom.gov.cn | 商務部 | — |
| CN-75 | A | A1 | mofcom.gov.cn | 商務部 | — |
| CN-76 | A | A1 | app.www.gov.cn | 中國政府網 | — |
| CN-77 | A | A1 | mohrss.gov.cn | 人力資源和社會保障部 | — |
| CN-78 | A | A1 | zjt.fj.gov.cn | 福建省住房和城鄉建設廳 | — |
| CN-79 | B | B2 | tailian.org.cn | 全國台聯（台胞之家） | — |
| CN-80 | A | A1 | gov.cn | 中國政府網（住房和城鄉建設部） | — |
| CN-81 | A | A1 | gov.cn | 中國政府網（國務院公報 2015 年第 15 號） | — |
| CN-82 | B | B3k | jiaju.sina.com.cn | 新浪家居 | — |
| CN-83 | C | C2 | archcy.com | 建築暢言網 | — |
| CN-84 | A | A1k | osta.gpy.org.cn | 人力資源和社會保障部 | — |
| CN-85 | B | B3m | shxlaw.cn | 陝西法制網 | — |
| CN-86 | B | B3k | jiaju.sina.cn | 新浪家居 | — |
| CN-87 | A | A1 | mohurd.gov.cn | 住房和城鄉建設部 | — |
| CN-88 | B | B2l | zhonglun.com | 中倫律師事務所 | — |
| CN-89 | D | D1 | m.jiansheku.com | 建設庫 | — |
| CN-90 | B | B3k | news.qq.com | 騰訊新聞（第一財經） | — |
| CN-91 | B | B3k | finance.sina.cn | 新浪財經 | — |
| CN-92 | B | B3k | finance.sina.cn | 新浪財經 | — |
| CN-93 | B | B2 | pdf.dfcfw.com | 券商研報（東方財富轉載） | — |
| CN-94 | A | A1 | stats.gov.cn | 國家統計局 | — |
| CN-95 | B | B3k | news.qq.com | 騰訊新聞 | — |
| CN-96 | A | A1 | ndrc.gov.cn | 國家發展和改革委員會（轉載工人日報） | — |
| CN-97 | B | B3k | paper.people.com.cn | 人民日報海外版 | — |
| CN-98 | B | B3k | m.bjnews.com.cn | 新京報 | — |
| CN-99 | B | B3m | m.gmw.cn | 光明網 | — |
| CN-100 | A | A2 | static.cninfo.com.cn | 巨潮資訊 | — |
| CN-101 | B | B3k | news.10jqka.com.cn | 同花順財經 | — |
| CN-102 | A | A2 | static.cninfo.com.cn | 巨潮資訊 | — |
| CN-103 | B | B3k | finance.sina.com.cn | 新浪財經 | — |
| CN-104 | B | B3k | stcn.com | 證券時報 | — |
| CN-105 | B | B3k | news.qq.com | 騰訊新聞 | — |
| CN-106 | D | D1 | sohu.com | 搜狐 | — |
| CN-107 | B | B3m | chnfund.com | 中國基金報 | — |
| CN-108 | B | B3k | finance.sina.com.cn | 新浪財經 | — |
| CN-109 | B | B3k | zjnews.zjol.com.cn | 浙江新聞（浙江在線） | — |
| CN-110 | B | B3k | wenxuan.news | 文軒財經 | — |
| CN-111 | D | D1 | agent.ren | 愛力方（A³） | — |
| CN-112 | B | B2 | digitaling.com | 數英（科爾尼） | — |
| CN-113 | C | C1 | x.qianzhan.com | 前瞻產業研究院 | — |
| CN-114 | C | C1 | qianzhan.com | 前瞻網 | — |
| CN-115 | B | B3k | finance.sina.com.cn | 新浪財經 | — |
| CN-116 | B | B3m | iheima.com | i 黑馬 | — |
| CN-117 | B | B3k | finance.sina.com.cn | 新浪財經 | — |
| CN-118 | B | B3k | news.qq.com | 騰訊新聞 | — |
| CN-119 | B | B3k | epaper.zqrb.cn | 證券日報 | — |
| CN-120 | B | B3k | finance.sina.com.cn | 新浪財經 | — |
| CN-121 | B | B3k | finance.sina.com.cn | 新浪財經 | — |
| CN-122 | C | C2 | chinep.net | 工採網 | — |
| CN-123 | B | B3k | finance.sina.com.cn | 新浪財經 | — |
| CN-124 | B | B3m | ceramicschina.com | 中國陶瓷網 | — |
| CN-125 | A | A1 | scjgj.beijing.gov.cn | 北京市市場監督管理局 | — |
| CN-126 | A | A1 | scjgj.sh.gov.cn | 上海市市場監督管理局、上海市消費者權益保護委員會、上海市室內裝飾行業協會 | — |
| CN-127 | A | A1 | htsfwb.samr.gov.cn | 國家市場監督管理總局合同示範文本庫 | — |
| CN-128 | A | A1 | amr.qingdao.gov.cn | 青島市市場監督管理局 | — |
| CN-129 | A | A1 | htsfwb.samr.gov.cn | 國家市場監督管理總局合同示範文本庫 | — |
| CN-130 | A | A1e | m.jianshe99.com | 建設工程教育網 | — |
| CN-131 | A | A1 | htsfwb.samr.gov.cn | 國家市場監督管理總局 | — |
| CN-132 | A | A1 | htsfwb.samr.gov.cn | 國家市場監督管理總局合同示範文本庫 | — |
| CN-133 | C | C2 | to8to.com | 土巴兔裝修大學 | — |
| MY-01 | B | B3k | nst.com.my | New Straits Times | — |
| MY-02 | C | C2 | edgeprop.my | EdgeProp | — |
| MY-03 | B | B3k | bernama.com | Bernama | — |
| MY-04 | A | A1 | mof.gov.my | 財政部（Ministry of Finance）新聞摘錄 | — |
| MY-05 | C | C2 | iqiglobal.com | IQI Global | — |
| MY-06 | C | C2 | propplace.my | Propplace | — |
| MY-07 | C | C2 | propplace.my | Propplace | — |
| MY-08 | C | C2 | estatemarketpulse.com | Estate Market Pulse | — |
| MY-09 | A | A1 | napic.jpph.gov.my | NAPIC（JPPH） | — |
| MY-10 | D | D1 | threads.com | @malaysiauncapped（Threads） | — |
| MY-11 | A | A1 | mof.gov.my | 財政部（Kementerian Kewangan） | — |
| MY-12 | A | A1 | napic.jpph.gov.my | NAPIC（JPPH） | — |
| MY-13 | A | A1 | napic.jpph.gov.my | NAPIC（JPPH） | — |
| MY-14 | A | A1 | napic.jpph.gov.my | NAPIC（JPPH） | — |
| MY-15 | B | B3k | theedgemalaysia.com | The Edge Malaysia | 僅讀到標題 |
| MY-16 | A | A1 | dosm.gov.my | 統計局（DOSM） | — |
| MY-17 | A | A1 | dosm.gov.my | DOSM | — |
| MY-18 | A | A1 | dosm.gov.my | DOSM | — |
| MY-19 | A | A1 | dosm.gov.my | DOSM | — |
| MY-20 | B | B3k | malaymail.com | Malay Mail | — |
| MY-21 | C | C2 | loanstreet.com.my | Loanstreet | — |
| MY-22 | C | C2 | qanvast.com | Qanvast | — |
| MY-23 | C | C2 | propcashflow.my | PropCashflow | — |
| MY-24 | D | D1 | malaysia4u.com | Malaysia4U | — |
| MY-25 | B | B3k | fmtv5.freemalaysiatoday.com | Free Malaysia Today | — |
| MY-26 | C | C1 | kenresearch.com | Ken Research | — |
| MY-27 | C | C1 | kenresearch.com | Ken Research | — |
| MY-28 | C | C1 | imarcgroup.com | IMARC Group | — |
| MY-29 | C | C1 | statista.com | Statista | — |
| MY-30 | A | A1 | lam.gov.my | Lembaga Arkitek Malaysia（LAM） | — |
| MY-31 | A | A1 | lam.gov.my | LAM | — |
| MY-32 | A | A1 | lam.gov.my | LAM | — |
| MY-33 | A | A1 | lam.gov.my | LAM | — |
| MY-34 | A | A1 | lam.gov.my | LAM | — |
| MY-35 | C | C3 | eduadvisor.my | EduAdvisor | — |
| MY-36 | C | C3 | eduspiral.com | Eduspiral | — |
| MY-37 | C | C3 | eduspiral.com | Eduspiral | 僅讀到標題 |
| MY-38 | C | C2 | onekeybiz.com | ONEKEY BIZ | — |
| MY-39 | C | C2 | getfoundation.com.my | Get Foundation | — |
| MY-40 | C | C2 | mishu.my | MISHU | — |
| MY-41 | C | C4 | waterproofingkl.com | Waterproofing KL | — |
| MY-42 | D | D1 | negaraku.md | Negaraku | — |
| MY-43 | A | A1 | dbkl.gov.my | Dewan Bandaraya Kuala Lumpur（DBKL） | — |
| MY-44 | B | B3k | nst.com.my | New Straits Times | — |
| MY-45 | B | B3m | says.com | SAYS | — |
| MY-46 | C | C4 | ipm.my | IPM | 僅讀到標題 |
| MY-47 | B | B3k | sinarharian.com.my | Sinar Harian | — |
| MY-48 | A | A1 | berita.rtm.gov.my | RTM Berita | — |
| MY-49 | A | A1 | repositori.kpdn.gov.my | KPDN 機構典藏（Repositori KPDN） | — |
| MY-50 | B | B3k | utusan.com.my | Utusan Malaysia | — |
| MY-51 | D | D1 | siakapkeli.my | Siakap Keli | — |
| MY-52 | B | B2 | conventuslaw.com | Conventus Law | — |
| MY-53 | D | D1 | malaysia4u.com | Malaysia4U | — |
| MY-54 | C | C2 | propertyguru.com.my | PropertyGuru Malaysia | 僅讀到標題 |
| MY-55 | B | B2 | turnerandtownsend.com | Turner & Townsend | 僅讀到標題 |
| MY-56 | B | B3k | malaymail.com | Malay Mail | 僅讀到標題 |
| MY-57 | B | B3k | nst.com.my | New Straits Times | 僅讀到標題 |
| MY-58 | D | D1 | x.com | Lembaga Arkitek Malaysia（官方 X 帳號） | — |
| MY-59 | A | A1 | admin.lam.gov.my | Lembaga Arkitek Malaysia | — |
| MY-60 | B | B3k | bernama.com | Bernama | — |
| MY-61 | A | A1e | tcclaw.com.my | TCC Law（上傳重印本） | — |
| MY-62 | B | B2 | conventuslaw.com | Conventus Law | — |
| MY-63 | B | B2 | lexology.com | Lexology | — |
| MY-64 | B | B2 | en.zhonglun.com | 中倫律師事務所（Zhong Lun） | — |
| MY-65 | B | B2 | christopherleeong.com | Christopher & Lee Ong | — |
| MY-66 | B | B2 | wmlaw.com.my | WM Law | — |
| MY-67 | C | C4 | xpatmobi.com | XpatMobi | — |
| MY-68 | C | C4 | bestar-my.com | Bestar | — |
| MY-69 | B | B2 | bakermckenzie.com | Baker McKenzie | — |
| MY-70 | B | B2 | vialtopartners.com | Vialto Partners | — |
| MY-71 | B | B2 | eiglaw.com | EIG Law | — |
| MY-72 | B | B2 | taxnews.ey.com | EY | — |
| MY-73 | B | B3k | malaymail.com | Malay Mail | — |
| MY-74 | B | B3k | nst.com.my | New Straits Times | — |
| MY-75 | B | B3m | thevibes.com | The Vibes | 僅讀到標題 |
| MY-76 | B | B3k | theedgemalaysia.com | The Edge Malaysia | — |
| MY-77 | B | B3k | bernama.com | Bernama | — |
| MY-78 | A | A1 | mohr.gov.my | 人力資源部（MOHR） | — |
| MY-79 | B | B3k | bharian.com.my | Berita Harian | — |
| MY-80 | B | B3m | humanresourcesonline.net | Human Resources Online | 僅讀到標題 |
| MY-81 | B | B3k | enanyang.my | 南洋商報（e南洋） | — |
| MY-82 | B | B3k | buypropertynews.com | Buy Property News | — |
| MY-83 | C | C2 | coohom.com | Coohom | — |
| MY-84 | C | C2 | houz.com.my | Houz | — |
| MY-85 | C | C2 | blainerobertdesign.com | Blaine Robert Design | — |
| MY-86 | C | C2 | ihome.my | iHome.my | — |
| MY-87 | C | C4 | zacharykhaw.com | Zachary Khaw | — |
| MY-88 | C | C4 | goodwinds.com.my | Goodwinds | — |
| MY-89 | C | C2 | interiordesignerkl.com | interiordesignerkl.com | — |
| MY-90 | C | C4 | mo-ane.com | Mo-ane | — |
| MY-91 | C | C2 | stuartsdesign.com | Stuarts Design | — |
| MY-92 | B | B3k | malaymail.com | Malay Mail | — |
| MY-93 | B | B3k | nst.com.my | New Straits Times | — |
| MY-94 | B | B3k | focusmalaysia.my | Focus Malaysia | — |
| MY-95 | B | B3k | focusmalaysia.my | Focus Malaysia | — |
| MY-96 | B | B3m | thesun.my | The Sun | 僅讀到標題 |
| MY-97 | B | B3k | focusmalaysia.my | Focus Malaysia | 僅讀到標題 |
| MY-98 | B | B3m | thesun.my | The Sun | — |
| MY-99 | C | C4 | group.ikano | Ikano Group | — |
| MY-100 | B | B3k | nst.com.my | New Straits Times | — |
| MY-101 | B | B3m | scandasia.com | ScandAsia | — |
| MY-102 | B | B3k | theborneopost.com | Borneo Post | — |
| MY-103 | C | C3 | jobstreet.com.my | JobStreet | — |
| MY-104 | B | B3m | marketing-interactive.com | Marketing-Interactive | 僅讀到標題 |
| MY-105 | B | B2k | rehdainstitute.com | REHDA Institute | — |
| MY-106 | B | B2k | rehdainstitute.com | REHDA Institute | — |
| MY-107 | C | C2 | myrumahbaru.com | MyRumahBaru | — |
| MY-108 | B | B2 | rsisinternational.org | RSIS International（IJRISS） | — |
| MY-109 | B | B2 | archive.aessweb.com | AESS 期刊典藏 | — |
| MY-110 | D | D1 | scribd.com | Scribd（上傳者不明） | — |
| MY-111 | B | B2 | aseanbriefing.com | ASEAN Briefing（Dezan Shira） | — |
| MY-112 | B | B2 | frontiersin.org | Frontiers in Built Environment | — |
| MY-113 | B | B2 | kuekong.com | Kuekong（郭剛律師樓） | — |
| MY-114 | C | C2 | iproperty.com.my | iProperty Malaysia | — |
| MY-115 | C | C2 | clickbina.com | ClickBina | 僅讀到標題 |
| MY-116 | C | C2 | recommend.my | Recommend.my | 僅讀到標題 |
| MY-117 | B | B2 | nglaw.com.my | Ng Law Firm | — |
| MY-118 | B | B2k | richardweechambers.com | Richard Wee Chambers | — |
| MY-119 | D | D1 | hlteoh37.github.io | sorted-my（個人網站） | — |
| MY-120 | A | A1 | dosm.gov.my | DOSM | — |
| MY-121 | A | A1 | dosm.gov.my | DOSM | — |
| MY-122 | A | A1 | convince.cidb.gov.my | CIDB | — |
| MY-123 | B | B3m | says.com | SAYS | — |
| MY-124 | B | B3k | selangorjournal.my | Selangor Journal | — |
| MY-125 | A | A1 | jkptg.gov.my | 聯邦土地及礦務總署（JKPTG） | — |
| MY-126 | B | B3k | utusan.com.my | Utusan Malaysia | — |
| MY-127 | B | B3m | malaysiagazette.com | Malaysia Gazette | — |
| MY-128 | B | B3m | malaysiagazette.com | Malaysia Gazette | 僅讀到標題 |
| MY-129 | A | A1 | kpkt.gov.my | 房屋及地方政府部（KPKT） | 僅讀到標題 |
| TH-01 | A | A1 | reic.or.th | REIC | — |
| TH-02 | B | B3m | businesstoday.co | Businesstoday（引 REIC） | — |
| TH-03 | B | B3k | thaipost.net | Thai Post | — |
| TH-04 | B | B3k | bangkokfocusnews.com | Bangkok Focus News | — |
| TH-05 | A | A1 | reic.or.th | REIC 新聞轉載 | — |
| TH-06 | A | A1 | reic.or.th | REIC | — |
| TH-07 | A | A1 | reic.or.th | REIC | — |
| TH-08 | A | A1 | reic.or.th | REIC 新聞轉載 | — |
| TH-09 | A | A1 | reic.or.th | REIC 新聞轉載 | — |
| TH-10 | A | A1 | reic.or.th | REIC 新聞轉載 | — |
| TH-11 | A | A1 | reic.or.th | REIC 新聞轉載 | — |
| TH-12 | B | B3k | bangkokbiznews.com | กรุงเทพธุรกิจ | — |
| TH-13 | B | B3k | bangkok-today.com | Bangkok Today | — |
| TH-14 | C | C2k | globalpropertyguide.com | Global Property Guide | — |
| TH-15 | A | A2 | investor.lh.co.th | Land and Houses PCL | — |
| TH-16 | B | B3m | pattayamail.com | Pattaya Mail | — |
| TH-17 | B | B3k | bernama.com | Bernama | — |
| TH-18 | B | B3k | kaohooninternational.com | Kaohoon International | — |
| TH-19 | C | C1 | euromonitor.com | Euromonitor | — |
| TH-20 | C | C1 | researchandmarkets.com | Research and Markets（Euromonitor） | — |
| TH-21 | B | B3k | insideretail.asia | Inside Retail Asia | — |
| TH-22 | B | B3k | insideretail.asia | Inside Retail Asia | — |
| TH-23 | A | A2 | lssmedia.setlink.set.or.th | SET | — |
| TH-24 | A | A2 | lssmedia.setlink.set.or.th | SET | — |
| TH-25 | B | B4 | marketscreener.com | MarketScreener | — |
| TH-26 | A | A2 | investor.globalhouse.co.th | Siam Global House PCL | — |
| TH-27 | A | A2 | investor.globalhouse.co.th | Siam Global House PCL | — |
| TH-28 | A | A2 | investor.globalhouse.co.th | Siam Global House PCL | — |
| TH-29 | B | B3k | kaohooninternational.com | Kaohoon International | — |
| TH-30 | C | C2 | primo.co.th | Primo | — |
| TH-31 | C | C2 | blovkliving.com | Blovk Living | — |
| TH-32 | C | C2 | idecdesign.com | Idec Design | — |
| TH-33 | C | C2 | markallcompany.com | Markall Company | — |
| TH-34 | C | C2 | neodecordesign.com | Neo Decor Design | — |
| TH-35 | B | B2 | asa.or.th | สมาคมสถาปนิกสยามฯ（ASA） | — |
| TH-36 | C | C4 | selectcon.com | Selectcon | — |
| TH-37 | B | B2 | download.asa.or.th | สภาสถาปนิก（經 ASA 下載站） | — |
| TH-38 | C | C2 | yotathai.com | YOTATHAI | — |
| TH-39 | B | B2 | download.asa.or.th | ASA 下載站 | — |
| TH-40 | A | A1 | reic.or.th | REIC 上傳檔 | — |
| TH-41 | A | A1 | reic.or.th | REIC 新聞轉載 | — |
| TH-42 | B | B3m | dsignsomething.com | Dsignsomething | — |
| TH-43 | C | C2 | thaipropertymentor.com | Thai Property Mentor | — |
| TH-44 | A | A1 | reic.or.th | REIC 新聞轉載 | — |
| TH-45 | B | B2 | daolsecurities.co.th | DAOL Securities | — |
| TH-46 | B | B2 | krungsri.com | วิจัยกรุงศรี（Krungsri Research） | — |
| TH-47 | B | B2 | krungsri.com | วิจัยกรุงศรี | — |
| TH-48 | B | B2 | lhbank.co.th | LH Bank สายงานวิจัยธุรกิจ | — |
| TH-49 | B | B3k | kaohoon.com | ข่าวหุ้น（Kaohoon） | — |
| TH-50 | B | B2 | kasikornresearch.com | ศูนย์วิจัยกสิกรไทย（KResearch） | — |
| TH-51 | B | B2 | download.asa.or.th | ASA 下載站 | — |
| TH-52 | B | B2 | download.asa.or.th | ASA 下載站 | — |
| TH-53 | D | D1 | th.wikipedia.org | วิกิพีเดีย（泰文維基） | — |
| TH-54 | B | B2 | act.or.th | สภาสถาปนิก | — |
| TH-55 | B | B2 | tilleke.com | Tilleke & Gibbins | — |
| TH-56 | B | B2l | inhouselawyer.co.uk | In-House Lawyer | — |
| TH-57 | B | B3m | pattayamail.com | Pattaya Mail | — |
| TH-58 | A | A1 | thailand.go.th | thailand.go.th（泰國政府入口網） | — |
| TH-59 | B | B3k | nationthailand.com | The Nation | — |
| TH-60 | A | A1 | ocpb.go.th | สคบ.（OCPB） | — |
| TH-61 | A | A1 | gcc.go.th | gcc.go.th | — |
| TH-62 | B | B3k | khaosod.co.th | ข่าวสด（Khaosod） | — |
| TH-63 | A | A1 | ocpb.go.th | สคบ. | — |
| TH-64 | A | A1 | ocpb.go.th | สคบ. | — |
| TH-65 | A | A1 | reic.or.th | REIC 新聞轉載 | — |
| TH-66 | A | A1 | ocpb.go.th | สคบ. | — |
| TH-67 | B | B2 | tcc.or.th | สภาองค์กรของผู้บริโภค（TCC） | — |
| TH-68 | D | D1 | justhat.app | JusThat.app | — |
| TH-69 | B | B3k | policywatch.thaipbs.or.th | Thai PBS Policy Watch | — |
| TH-70 | B | B3k | policywatch.thaipbs.or.th | Thai PBS Policy Watch | — |
| TH-71 | C | C2 | passport.co.th | Passport | — |
| TH-72 | B | B3m | mgronline.com | MGR Online | — |
| TH-73 | B | B3k | thairath.co.th | ไทยรัฐ（Thairath） | — |
| TH-74 | B | B3k | thansettakij.com | ฐานเศรษฐกิจ（Thansettakij） | — |
| TH-75 | A | A1 | tpso.go.th | สนค.（TPSO，商業部） | — |
| TH-76 | A | A1 | tpso.go.th | สนค.（TPSO） | — |
| TH-77 | A | A1 | tpso.go.th | สนค.（TPSO） | — |
| TH-78 | B | B3k | kaohoon.com | ข่าวหุ้น（Kaohoon） | — |
| TH-79 | B | B3k | khaosod.co.th | ข่าวสด（Khaosod） | — |
| TH-80 | B | B2 | kasikornresearch.com | ศูนย์วิจัยกสิกรไทย | — |
| TH-81 | B | B3k | en.dailysocial.id | DailySocial.id | — |
| TH-82 | C | C3 | clodura.ai | Clodura.ai | — |
| TH-83 | B | B2 | api.prod.pi.financial | Pi Securities | 候選出處、多個候選 URL |
| TH-84 | B | B2 | minichart.com.sg | Minichart（轉載 Maybank） | — |
| TH-85 | B | B3k | bloombergquint.com | Bloomberg（BloombergQuint） | — |
| TH-86 | B | B2 | scbeic.com | SCB EIC | — |
| TH-87 | C | C4 | yamada-spire-th.com | Yamada-Spire (Thailand) | — |
| TH-88 | C | C1 | kenresearch.com | Ken Research | — |
| TH-89 | C | C1 | marketresearch.com | Euromonitor（經 MarketResearch.com） | — |
| TH-90 | B | B3k | matichon.co.th | มติชน（Matichon） | — |
| TH-91 | B | B3m | matichon.co.th | มติชน | — |
| TH-92 | A | A2 | investor.indexlivingmall.com | Index Living Mall PCL | — |
| TH-93 | A | A2 | investor.indexlivingmall.com | Index Living Mall PCL | — |
| TH-94 | A | A2 | lssmedia.setlink.set.or.th | SET | — |
| TH-95 | A | A2 | investor.indexlivingmall.com | Index Living Mall PCL | — |
| TH-96 | A | A2 | investor.indexlivingmall.com | Index Living Mall PCL | — |
| TH-97 | A | A2 | investor.indexlivingmall.com | Index Living Mall PCL | — |
| VN-01 | C | C1 | mordorintelligence.com | Mordor Intelligence | — |
| VN-02 | B | B3k | dantri.com.vn | Dân trí | — |
| VN-03 | B | B3k | vnexpress.net | VnExpress | — |
| VN-04 | B | B3k | congthuong.vn | Báo Công Thương | 候選出處 |
| VN-05 | B | B3k | vneconomy.vn | VnEconomy | 候選出處 |
| VN-06 | C | C1 | imarcgroup.com | IMARC Group | — |
| VN-07 | C | C1 | imarcgroup.com | IMARC Group | — |
| VN-08 | C | C1 | imarcgroup.com | IMARC Group | — |
| VN-09 | C | C1 | imarcgroup.com | IMARC Group | — |
| VN-10 | C | C1 | kenresearch.com | Ken Research | — |
| VN-11 | C | C2 | takenli.vn | Takenli（業者） | 候選出處 |
| VN-12 | C | C2k | lanha.vn | Lanha（業者） | 候選出處 |
| VN-13 | C | C2k | noithatbenthanh.vn | Nội thất Bến Thành（業者） | 候選出處 |
| VN-14 | C | C2k | dogolegia.vn | Đồ gỗ Lê Gia（業者） | 候選出處 |
| VN-15 | D | D1 | voz.vn | VOZ 論壇 | 候選出處 |
| VN-16 | D | D1 | coda.io | thietkenoithat（coda.io 自發布頁） | — |
| VN-17 | B | B2s | dnse.com.vn | DNSE | — |
| VN-18 | B | B3k | doanhnhan.baophapluat.vn | Báo Pháp luật Việt Nam – Doanh nhân | — |
| VN-19 | B | B3k | doanhnhan.baophapluat.vn | Báo Pháp luật Việt Nam – Doanh nhân | — |
| VN-20 | B | B3m | diendandoanhnghiep.vn | Diễn đàn Doanh nghiệp | 候選出處 |
| VN-21 | B | B3k | doanhnhan.baophapluat.vn | Báo Pháp luật Việt Nam – Doanh nhân | 僅讀到標題 |
| VN-22 | B | B3k | doanhnhan.baophapluat.vn | Báo Pháp luật Việt Nam – Doanh nhân | 僅讀到標題 |
| VN-23 | B | B3k | doanhnhan.baophapluat.vn | Báo Pháp luật Việt Nam – Doanh nhân | 僅讀到標題 |
| VN-24 | B | B3k | doanhnhan.baophapluat.vn | Báo Pháp luật Việt Nam – Doanh nhân | 僅讀到標題 |
| VN-25 | B | B2 | cbrevietnam.com | CBRE Vietnam | — |
| VN-26 | B | B3k | vietnamnews.vn | Việt Nam News | — |
| VN-27 | B | B3k | theinvestor.vn | The Investor | — |
| VN-28 | B | B3k | theinvestor.vn | The Investor | — |
| VN-29 | C | C2 | cchn.gxd.vn | GXD（cchn.gxd.vn） | — |
| VN-30 | A | A1 | luatvietnam.vn | LuatVietnam | — |
| VN-31 | A | A1e | quangdaqs.vn | Cục Quản lý hoạt động xây dựng（Bộ Xây dự | — |
| VN-32 | C | C2 | icci.vn | ICCI | 僅讀到標題 |
| VN-33 | A | A1 | thuvienphapluat.vn | Thư viện Pháp luật | — |
| VN-34 | B | B3m | lsvn.vn | LSVN（Tạp chí Luật sư Việt Nam） | — |
| VN-35 | A | A1e | hethongphapluat.com | Hệ thống pháp luật（轉載 Bộ Xây dựng 函） | — |
| VN-36 | B | B3k | vneconomy.vn | VnEconomy | — |
| VN-37 | A | A1 | moc.gov.vn | Bộ Xây dựng（moc.gov.vn） | — |
| VN-38 | A | A1 | baochinhphu.vn | Báo Chính phủ（baochinhphu.vn） | — |
| VN-39 | B | B3m | sggp.org.vn | SGGP | 僅讀到標題 |
| VN-40 | B | B3m | tinnhanhchungkhoan.vn | Tin nhanh Chứng khoán | 僅讀到標題 |
| VN-41 | B | B3k | baovephapluat.vn | Báo Bảo vệ Pháp luật | 候選出處 |
| VN-42 | B | B3k | vnexpress.net | VnExpress | 僅讀到標題 |
| VN-43 | C | C4 | awe.edu.vn | AWE（培訓機構） | 僅讀到標題 |
| VN-44 | B | B2 | trungtamwto.vn | Trung tâm WTO và Hội nhập（VCCI） | — |
| VN-45 | A | A1 | thuvienphapluat.vn | Thư viện Pháp luật | 僅讀到標題 |
| VN-46 | A | A1 | baochinhphu.vn | Báo Chính phủ（政策問答） | — |
| VN-47 | B | B2 | plf.vn | PLF（Doing Business in Vietnam） | — |
| VN-48 | B | B3k | nhandan.vn | Nhân Dân | 候選出處 |
| VN-49 | B | B2 | phamdolaw.com | Phạm Đỗ Law | 候選出處 |
| VN-50 | C | C4 | dichvuhanhchinhcong.vn | dichvuhanhchinhcong.vn | 候選出處 |
| VN-51 | B | B2 | fdvn.vn | FDVN（Luật sư Đà Nẵng） | 僅讀到標題 |
| VN-52 | C | C2 | dauthau.asia | DauThau.asia | — |
| VN-53 | C | C2 | thuviennhadat.vn | Thư viện Nhà đất | — |
| VN-54 | A | A1 | thuvienphapluat.vn | Thư viện Pháp luật | — |
| VN-55 | B | B3k | phapluatdoanhnghiep.vn | Pháp luật Doanh nghiệp | — |
| VN-56 | B | B2 | kpmg.com | KPMG Vietnam | — |
| VN-57 | B | B2 | fdvn.vn | FDVN（Luật sư Đà Nẵng） | 候選出處 |
| VN-58 | C | C4 | giacorp.vn | GIA CORP | 候選出處 |
| ID-01 | C | C1 | kenresearch.com | Ken Research | — |
| ID-02 | C | C1 | statista.com | Statista | — |
| ID-03 | C | C1 | app.researchpool.com | Euromonitor（ResearchPool 刊登） | — |
| ID-04 | B | B3k | insideretail.asia | Inside Retail Asia | — |
| ID-05 | B | B3m | investortrust.id | Investor Trust（引 BPS） | — |
| ID-06 | B | B3k | investortrust.id | Investor Trust | — |
| ID-07 | B | B3k | economy.okezone.com | Okezone | — |
| ID-08 | B | B3m | kabarbursa.com | Kabar Bursa | — |
| ID-09 | C | C2 | pegadaian.co.id | Pegadaian | — |
| ID-10 | C | C2 | brighton.co.id | Brighton Real Estate | — |
| ID-11 | C | C4 | megasyariah.co.id | Bank Mega Syariah | — |
| ID-12 | C | C2 | mamikos.com | Mamikos | — |
| ID-13 | B | B3k | liputan6.com | Liputan6 | — |
| ID-14 | C | C1 | credenceresearch.com | Credence Research | — |
| ID-15 | C | C1 | credenceresearch.com | Credence Research | — |
| ID-16 | C | C1 | imarcgroup.com | IMARC Group | — |
| ID-17 | B | B3k | investasi.kontan.co.id | Kontan | — |
| ID-18 | B | B3k | market.bisnis.com | Bisnis.com | — |
| ID-19 | B | B3k | market.bisnis.com | Bisnis.com | — |
| ID-20 | B | B3k | market.bisnis.com | Bisnis.com | — |
| ID-21 | B | B3k | industry.co.id | Industry.co.id | — |
| ID-22 | B | B3k | market.bisnis.com | Bisnis.com | — |
| ID-23 | B | B3k | market.bisnis.com | Bisnis.com | — |
| ID-24 | B | B3k | market.bisnis.com | Bisnis.com | — |
| ID-25 | B | B3k | industri.kontan.co.id | Kontan | — |
| ID-26 | B | B3k | industri.kontan.co.id | Kontan | — |
| ID-27 | B | B3k | market.bisnis.com | Bisnis.com | — |
| ID-28 | A | A1 | oss.go.id | OSS（Kementerian Investasi/BKPM） | — |
| ID-29 | C | C4 | badanperizinan.co.id | Badan Perizinan | — |
| ID-30 | B | B3k | news.sah.co.id | Sah News | — |
| ID-31 | C | C2 | kbli.co.id | kbli.co.id | — |
| ID-32 | A | A1 | oss.go.id | OSS（Kementerian Investasi/BKPM） | — |
| ID-33 | C | C4 | oss-rba.com | oss-rba.com | — |
| ID-34 | C | C2 | valprointertech.com | Valpro Intertech | — |
| ID-35 | B | B2 | lib.ui.ac.id | Universitas Indonesia（論文） | — |
| ID-36 | C | C2 | hukumproperti.com | Hukumproperti.com | — |
| ID-37 | B | B2 | muc.co.id | MUC Consulting | — |
| ID-38 | B | B2 | blog.lekslawyer.com | Leks&Co（Leks Blawg） | — |
| ID-39 | B | B2 | blog.lekslawyer.com | Leks&Co（Leks Blawg） | — |
| ID-40 | C | C4 | gramedia.com | Gramedia | — |
| ID-41 | B | B3k | wartaekonomi.co.id | Warta Ekonomi | — |
| ID-42 | B | B3k | suarasurabaya.net | Suara Surabaya | — |
| ID-43 | B | B2 | its.ac.id | LSP Institut Teknologi Sepuluh Nopember（ | — |
| ID-44 | B | B3k | liputan6.com | Liputan6 | — |
| ID-45 | C | C4 | kochiro.com | Kochiro Architect | — |
| ID-46 | C | C4 | sn-studio.id | SN Studio | — |
| ID-47 | C | C4 | sibambostudio.com | Sibambo Studio | — |
| ID-48 | C | C1 | researchandmarkets.com | ResearchAndMarkets | — |
| ID-49 | C | C1 | finance.yahoo.com | Yahoo Finance（新聞稿） | — |
| ID-50 | C | C1 | kenresearch.com | Ken Research | — |
| ID-51 | C | C1 | marketresearch.com | Ken Research（MarketResearch.com 刊登） | — |
| ID-52 | C | C1 | statista.com | Statista | — |
| ID-53 | B | B3k | industri.kontan.co.id | Kontan | — |
| ID-54 | B | B3m | pasardana.id | Pasardana | — |
| ID-55 | B | B3m | kabarbursa.com | Kabar Bursa | — |
| ID-56 | B | B3k | industri.kontan.co.id | Kontan | — |
| ID-57 | C | C2 | cbinsights.com | CB Insights | — |
| ID-58 | C | C3 | profiles.crustdata.com | Crustdata | — |
| ID-59 | C | C2 | tracxn.com | Tracxn | — |
| ID-60 | C | C3 | pitchbook.com | PitchBook | — |
| ID-61 | C | C2 | ecommercedb.com | ECDB | — |
| ID-62 | C | C2 | 1001startup.id | 1001startup.id | — |
| ID-63 | C | C3 | zoominfo.com | ZoomInfo | — |
| ID-64 | C | C2 | emerhub.com | Emerhub | — |
| ID-65 | B | B2 | pro.hukumonline.com | Hukumonline Pro | — |
| ID-66 | C | C4 | balizero.com | Bali Zero | — |
| ID-67 | B | B2 | lexmundus.com | Lex Mundus | — |
| ID-68 | C | C4 | sertifikasi.biz | sertifikasi.biz | — |
| ID-69 | C | C2 | mitrarenov.com | Mitrarenov | — |
| ID-70 | C | C2 | izingedung.id | Izin Gedung | — |
| ID-71 | C | C4 | kingspointresidence.com | Kingspoint Residence | — |
| ID-72 | A | A1 | peraturan.bpk.go.id | JDIH BPK RI | — |
| ID-73 | A | A1 | jdih.pu.go.id | JDIH Kementerian PUPR | — |
| ID-74 | C | C2 | hukumproperti.com | Hukumproperti.com（Leks&Co） | — |
| ID-75 | B | B3k | investortrust.id | Investor Trust | — |
| ID-76 | B | B3k | rri.co.id | RRI | — |
| ID-77 | B | B3m | idxchannel.com | IDX Channel | — |
| ID-78 | B | B3k | antaranews.com | Antara | 僅讀到標題 |
| ID-79 | B | B3k | cnnindonesia.com | CNN Indonesia | 僅讀到標題 |
| ID-80 | B | B3k | rri.co.id | RRI | 僅讀到標題 |
| ID-81 | B | B3m | kompas.com | Kompas（引 BPS） | — |
| ID-82 | B | B3k | kompas.com | Kompas Properti | — |
| ID-83 | B | B3m | balikpapantv.jawapos.com | JawaPos Balikpapan TV | — |
| ID-84 | B | B3k | medcom.id | Medcom | — |
| ID-85 | B | B3k | detik.com | Detik | — |
| ID-86 | C | C4 | ecatalog.sinarmasland.com | Sinar Mas Land | — |
| ID-87 | B | B4 | databoks.katadata.co.id | Databoks（Katadata，引 BPS） | — |
| ID-88 | B | B3k | cnbcindonesia.com | CNBC Indonesia | — |
| ID-89 | B | B3k | money.kompas.com | Kompas Money | — |
| ID-90 | A | A1 | bps.go.id | BPS-Statistics Indonesia | — |
| ID-91 | B | B3k | antaranews.com | Antara | — |
| ID-92 | B | B3k | kompas.com | Kompas Properti | — |
| ID-93 | B | B3k | ekonomi.bisnis.com | Bisnis.com | — |
| ID-94 | A | A1 | bps.go.id | BPS-Statistics Indonesia | — |
| PH-01 | A | A1 | psa.gov.ph | Philippine Statistics Authority (PSA) | — |
| PH-02 | A | A1 | psa.gov.ph | PSA | — |
| PH-03 | A | A1 | rssomimaropa.psa.gov.ph | PSA RSSO MIMAROPA | — |
| PH-04 | A | A1 | rssonir.psa.gov.ph | PSA RSSO NIR | — |
| PH-05 | B | B3k | malaya.com.ph | Malaya Business Insight | — |
| PH-06 | B | B3k | bworldonline.com | BusinessWorld | — |
| PH-07 | B | B3k | philstar.com | Philstar | — |
| PH-08 | B | B3k | tribune.net.ph | Daily Tribune | — |
| PH-09 | B | B3k | plus.inquirer.net | Philippine Daily Inquirer (Inquirer Plus | — |
| PH-10 | B | B3k | philstar.com | Philstar | — |
| PH-11 | B | B2 | quartr.com | Quartr | — |
| PH-12 | A | A2 | investor.wilcon.com.ph | Wilcon Depot, Inc.（SEC Form 17-Q） | — |
| PH-13 | B | B3k | context.ph | Context.ph | — |
| PH-14 | B | B3k | malaya.com.ph | Malaya Business Insight | — |
| PH-15 | B | B3k | bworldonline.com | BusinessWorld | — |
| PH-16 | B | B3k | tribune.net.ph | Daily Tribune | — |
| PH-17 | B | B3k | tribune.net.ph | Daily Tribune | — |
| PH-18 | B | B3k | newsinfo.inquirer.net | Philippine Daily Inquirer | — |
| PH-19 | B | B3k | abs-cbn.com | ABS-CBN News | — |
| PH-20 | B | B3k | gulfnews.com | Gulf News | — |
| PH-21 | B | B3k | malaya.com.ph | Malaya Business Insight | — |
| PH-22 | B | B3k | gulfnews.com | Gulf News | — |
| PH-23 | A | A1 | ldr.senate.gov.ph | Senate of the Philippines, Legislative D | — |
| PH-24 | C | C2 | jur.ph | jur.ph | — |
| PH-25 | A | A1 | prc.gov.ph | Professional Regulation Commission (PRC) | — |
| PH-26 | A | A1 | prc.gov.ph | PRC | — |
| PH-27 | A | A1 | prc.gov.ph | PRC | — |
| PH-28 | A | A1 | davao.prc.gov.ph | PRC Davao | — |
| PH-29 | A | A1 | prc.gov.ph | PRC | — |
| PH-30 | B | B2k | eccp.com | European Chamber of Commerce of the Phil | — |
| PH-31 | B | B2 | pwc.com | PwC Philippines（Taxwise or Otherwise） | — |
| PH-32 | B | B2 | foalawoffice.com | FOA Law Office | — |
| PH-33 | C | C2k | babylon2k.org | Babylon2k（部落格） | — |
| PH-34 | B | B2 | veralaw.com | Villaraza & Angangco (VeraLaw) | — |
| PH-35 | B | B3k | philstar.com | Philstar | — |
| PH-36 | B | B3k | mb.com.ph | Manila Bulletin | — |
| PH-37 | C | C4 | rcbc.com | RCBC | — |
| PH-38 | C | C2 | jur.ph | jur.ph | — |
| PH-39 | C | C2 | coohom.com | Coohom（設計軟體平台） | 多個候選 URL |
| PH-40 | C | C2 | eurobel.com.ph | Eurobel Rugs + Carpets | — |
| PH-41 | C | C2 | realliving.com.ph | RealLiving | — |
| PH-42 | C | C2 | realliving.com.ph | RealLiving | — |
| PH-43 | C | C4 | galathome.com | Gal at Home Design Studio | — |
| PH-44 | C | C2 | qaltik.com | Qaltik | — |
| PH-45 | C | C2 | aedoconstruction.com | AEDO Construction | — |
| PH-46 | C | C2 | aedoconstruction.com | AEDO Construction | — |
| PH-47 | C | C2 | aedoconstruction.com | AEDO Construction | — |
| PH-48 | C | C2 | aedoconstruction.com | AEDO Construction | — |
| PH-49 | C | C2 | communities.dmcihomes.com | DMCI Homes Communities | — |
| PH-50 | B | B3k | malaya.com.ph | Malaya Business Insight | — |
| PH-51 | C | C3 | bossjob.com | Bossjob | — |
| PH-52 | C | C3 | paylab.com | Paylab | — |
| PH-53 | A | A1 | elibrary.judiciary.gov.ph | Supreme Court E-Library（Office of the Pr | — |
| PH-54 | C | C2 | jur.ph | jur.ph | — |
| PH-55 | B | B2 | divinalaw.com | Divina Law（Dose of Law） | — |
| PH-56 | B | B2 | oneasia.legal | One Asia Lawyers | — |
| PH-57 | B | B2 | kittelsoncarpo.com | Kittelson & Carpo | — |
| PH-58 | C | C1 | kenresearch.com | Ken Research | — |
| PH-59 | C | C1 | kenresearch.com | Ken Research | — |
| PH-60 | C | C1 | imarcgroup.com | IMARC Group | — |
| PH-61 | C | C1 | statista.com | Statista | — |
| PH-62 | C | C1 | kenresearch.com | Ken Research | — |
| PH-63 | C | C1 | euromonitor.com | Euromonitor International | — |
| PH-64 | B | B3k | malaya.com.ph | Malaya Business Insight | — |
| PH-65 | B | B3k | gmanetwork.com | GMA News | — |
| PH-66 | B | B3k | gmanetwork.com | GMA News（Balitambayan） | — |
| PH-67 | B | B3m | sunstar.com.ph | SunStar Superbalita Cebu | — |
| PH-68 | B | B2 | grantthornton.com.ph | Grant Thornton Philippines | — |
| PH-69 | B | B2 | pmap.org.ph | PMAP | — |
| PH-70 | C | C1 | statista.com | Statista（依 PSA 資料） | — |
| PH-71 | D | D1 | mexc.com | MEXC News（加密貨幣交易所新聞頁，轉載） | — |
| PH-72 | B | B2 | respicio.ph | Respicio & Co. | — |
| PH-73 | B | B2 | respicio.ph | Respicio & Co. | — |
| PH-74 | B | B2 | respicio.ph | Respicio & Co. | — |
| PH-75 | C | C2 | moneymax.ph | Moneymax | — |
| PH-76 | A | A1 | elibrary.judiciary.gov.ph | Supreme Court E-Library | — |
| PH-77 | B | B3k | bworldonline.com | BusinessWorld | — |
| PH-78 | C | C4 | group.ikano | Ikano Group | — |
| PH-79 | B | B3k | scandasia.com | ScandAsia | — |
| PH-80 | B | B3k | malaya.com.ph | Malaya Business Insight | — |
| PH-81 | C | C4 | group.ikano | Ikano Group | — |
| IN-01 | C | C1 | mordorintelligence.com | Mordor Intelligence | — |
| IN-02 | C | C1 | mordorintelligence.com | Mordor Intelligence | — |
| IN-03 | C | C1 | imarcgroup.com | IMARC Group | — |
| IN-04 | C | C1 | imarcgroup.com | IMARC Group | 對應或年份為推定 |
| IN-05 | C | C1 | credenceresearch.com | Credence Research | — |
| IN-06 | C | C1 | psmarketresearch.com | P&S Intelligence | — |
| IN-07 | C | C1 | kenresearch.com | Ken Research | — |
| IN-08 | C | C2 | material360.co | Material360 | — |
| IN-09 | C | C1 | verifiedmarketresearch.com | Verified Market Research | — |
| IN-10 | B | B3m | analyticsindiamag.com | Analytics India Magazine | — |
| IN-11 | D | D1 | orangeowl.marketing | OrangeOwl | — |
| IN-12 | B | B2 | redseer.com | Redseer Strategy Consultants | — |
| IN-13 | B | B3k | medianews4u.com | MediaNews4U | — |
| IN-14 | B | B3k | indianretailer.com | Indian Retailer | — |
| IN-15 | B | B3k | entrackr.com | Entrackr | — |
| IN-16 | B | B3k | inc42.com | Inc42 | — |
| IN-17 | B | B3k | outlookbusiness.com | Outlook Business（PTI） | — |
| IN-18 | B | B3k | theweek.in | The Week（PTI wire） | — |
| IN-19 | B | B3k | entrackr.com | Entrackr | — |
| IN-20 | B | B3m | india.entrepreneur.com | Entrepreneur India | — |
| IN-21 | B | B3k | entrackr.com | Entrackr | — |
| IN-22 | B | B3k | inc42.com | Inc42 | — |
| IN-23 | B | B3m | hrkatha.com | HR Katha | — |
| IN-24 | B | B3k | deccanherald.com | Deccan Herald | — |
| IN-25 | B | B3k | entrackr.com | Entrackr | — |
| IN-26 | C | C2 | franchiseindia.com | Franchise India | — |
| IN-27 | B | B3k | inc42.com | Inc42 | — |
| IN-28 | B | B3k | indianretailer.com | Indian Retailer | — |
| IN-29 | B | B3k | indiaretailing.com | India Retailing | — |
| IN-30 | B | B3k | outlookbusiness.com | Outlook Business | — |
| IN-31 | C | C4 | angelone.in | Angel One | — |
| IN-32 | C | C4 | 5paisa.com | 5paisa | — |
| IN-33 | C | C4 | indmoney.com | INDmoney | — |
| IN-34 | B | B3m | businesstoday.in | Business Today | — |
| IN-35 | B | B3k | freepressjournal.in | Free Press Journal | — |
| IN-36 | B | B3k | ianslive.in | IANS | — |
| IN-37 | B | B3k | outlookbusiness.com | Outlook Business | — |
| IN-38 | B | B3m | storyboard18.com | Storyboard18 | — |
| IN-39 | C | C2 | realtynmore.com | Realty n More | — |
| IN-40 | B | B3k | outlookbusiness.com | Outlook Business | — |
| IN-41 | B | B3m | nbmcw.com | NBM&CW | — |
| IN-42 | B | B3k | asianews.network | Asia News Network | — |
| IN-43 | C | C2 | poonawallafincorp.com | Poonawalla Fincorp | — |
| IN-44 | C | C2 | tinttoneandshade.com | Tint Tone and Shade | — |
| IN-45 | C | C2 | housiey.com | Housiey | — |
| IN-46 | C | C2 | constructionestimatorindia.com | Construction Estimator India | — |
| IN-47 | C | C4 | designcafe.com | DesignCafe | — |
| IN-48 | C | C2 | housing.com | Housing.com | — |
| IN-49 | A | A1 | indiacode.nic.in | India Code（法務部，政府） | — |
| IN-50 | B | B2 | mondaq.com | Mondaq | — |
| IN-51 | C | C2 | studiomatrx.org | Studio Matrx | — |
| IN-52 | B | B3m | worldarchitecture.org | World Architecture | 僅讀到標題 |
| IN-53 | C | C2 | interioratoz.com | Interior A to Z | — |
| IN-54 | C | C4 | alephindia.in | Aleph India | — |
| IN-55 | B | B3m | plyreporter.com | Ply Reporter | — |
| IN-56 | C | C2 | certification-india.com | MPR Kontakt（certification-india.com） | — |
| IN-57 | B | B3m | sourcinghardware.net | Sourcing Hardware | 僅讀到標題 |
| IN-58 | C | C2 | housing.com | Housing.com | — |
| IN-59 | C | C2 | housing.com | Housing.com | — |
| IN-60 | A | A1 | rera.bihar.gov.in | Bihar Real Estate Regulatory Authority（政 | — |
| IN-61 | B | B3k | civilsdaily.com | Civilsdaily | 對應或年份為推定 |
| IN-62 | D | D1 | gktoday.in | GKToday | 對應或年份為推定 |
| IN-63 | C | C4 | altacit.com | Altacit | — |
| IN-64 | C | C2 | propnewz.com | PropNewz | — |
| IN-65 | C | C2 | righttoinformation.wiki | righttoinformation.wiki | — |
| IN-66 | C | C2 | yojoapp.com | Yojo | — |
| IN-67 | B | B3m | patrika.com | Patrika（Rajasthan Patrika） | — |
| IN-68 | C | C2 | tractorjunction.com | TractorJunction | — |
| IN-69 | D | D1 | dpiljipr.in | dpiljipr.in | 對應或年份為推定 |
| IN-70 | C | C2 | solve24.in | Solve24 | — |
| IN-71 | C | C2 | solve24.in | Solve24 | — |
| IN-72 | C | C4 | nirmansetu.in | Nirmaansetu Technologies LLP | 對應或年份為推定 |
| IN-73 | C | C2 | iscodehub.com | ISCodeHub | 對應或年份為推定 |
| IN-74 | C | C2 | aecord.com | Aecord | 對應或年份為推定 |
| IN-75 | C | C4 | iifl.com | IIFL Finance | — |
| IN-76 | C | C4 | bajajfinserv.in | Bajaj Finserv | — |
| IN-77 | C | C2 | yojoapp.com | Yojo | — |
| IN-78 | C | C4 | morbitilehub.com | Morbi Tile Hub | — |
| IN-79 | B | B2 | simplehai.axisdirect.in | Axis Direct（Axis Securities） | 對應或年份為推定 |
| IN-80 | C | C2 | infralens.in | Infralens | 對應或年份為推定 |
| IN-81 | C | C2 | nobroker.in | NoBroker Interiors | 對應或年份為推定 |
| IN-82 | C | C2 | houseyog.com | HouseYog | 對應或年份為推定 |
| IN-83 | C | C2 | tinttoneandshade.com | Tint Tone and Shade | — |
| IN-84 | D | D1 | homedecoration.beehiiv.com | homedecoration.beehiiv.com | — |
| IN-85 | C | C2 | constructionestimatorindia.com | Construction Estimator India | 對應或年份為推定 |
| IN-86 | C | C4 | mccoymart.com | McCoy Mart | — |
| IN-87 | B | B3k | tribuneindia.com | The Tribune | — |
| IN-88 | C | C2 | static.squareyards.com | Square Yards | — |
| IN-89 | B | B2l | grantthornton.in | Grant Thornton Bharat | — |
| IN-90 | C | C1 | mordorintelligence.com | Mordor Intelligence | — |
| IN-91 | C | C4 | aurumproptech.in | Aurum PropTech | — |
| IN-92 | A | A1 | pmay-urban.gov.in | 住宅與都市扶貧部（MoHUPA；pmay-urban.gov.in，政府） | 對應或年份為推定 |
| IN-93 | C | C2 | thepropertist.com | The Propertist | 對應或年份為推定 |
| IN-94 | B | B3k | pressreader.com | The Free Press Journal（PressReader） | — |
| IN-95 | C | C4 | lawcrustrealty.com | Lawcrust Realty | 對應或年份為推定 |
| IN-96 | C | C4 | arkade.in | Arkade Developers | 對應或年份為推定 |
| IN-97 | B | B3m | inkl.com | inkl（轉載） | — |
| IN-98 | C | C2 | righttoinformation.wiki | righttoinformation.wiki | — |
| IN-99 | D | D1 | kaanoon.com | Kaanoon（律師 Q&A） | — |
| IN-100 | C | C2 | blog.ipleaders.in | iPleaders | — |
| IN-101 | C | C2 | taxguru.in | TaxGuru | — |
| IN-102 | B | B2 | india-briefing.com | India Briefing（Dezan Shira） | — |
| IN-103 | B | B3m | businesstoday.in | Business Today | — |
| IN-104 | C | C3 | hyring.com | Hyring | — |
| IN-105 | C | C2 | realtynmore.com | Realty n More（引 Cushman & Wakefield） | — |
| IN-106 | C | C2 | realtynmore.com | Realty n More | — |
| IN-107 | B | B3k | ianslive.in | IANS | 對應或年份為推定 |
| IN-108 | B | B3k | ianslive.in | IANS | — |
| IN-109 | B | B2 | cushmanwakefield.com | Cushman & Wakefield | — |
| TA1-01 | A | A2r | marketscreener.com | Nitori Holdings／MarketScreener | — |
| TA1-02 | B | B4 | filingreader.com | FilingReader | 僅讀到標題 |
| TA1-03 | A | A2 | daiwair.webcdn.stream.ne.jp | 株式会社カチタス | — |
| TA1-04 | D | D1 | note.com | カチタス IR（note） | — |
| TA1-05 | A | A2 | www2.jpx.co.jp | 株式会社カチタス（JPX） | 僅讀到標題 |
| TA1-06 | B | B3m | gyokaidigest.com | 業界ダイジェスト | — |
| TA1-07 | C | C4 | katitas.co.jp | 株式会社カチタス | 僅讀到標題 |
| TA1-08 | B | B3k | ctee.com.tw | 工商時報 | — |
| TA1-09 | B | B3k | money.udn.com | 經濟日報 | — |
| TA1-10 | B | B3k | udn.com | 聯合新聞網 | — |
| TA1-11 | C | C2 | tw.stock.yahoo.com | Yahoo 股市（轉載） | — |
| TA1-12 | C | C2 | moneydj.com | MoneyDJ 理財網 | — |
| TA1-13 | A | A2 | company.hanssem.com | 한샘 IR | — |
| TA1-14 | C | C2 | saramin.co.kr | 사람인 | — |
| TA1-15 | B | B3k | news1.kr | 뉴스1 | — |
| TA1-16 | B | B3k | insightkorea.co.kr | 인사이트코리아 | — |
| TA1-17 | B | B3k | news1.kr | 뉴스1 | 僅讀到標題 |
| TA1-18 | B | B3k | view.asiae.co.kr | 아시아경제 | 僅讀到標題 |
| TA1-19 | B | B3m | g-enews.com | 글로벌이코노믹 | 僅讀到標題 |
| TA1-20 | B | B3k | psnews.co.kr | 퍼블릭뉴스 | 僅讀到標題 |
| TA1-21 | B | B3k | dealsite.co.kr | 딜사이트 | 僅讀到標題 |
| TA1-22 | A | A2 | oppein.com | 欧派家居 | — |
| TA1-23 | D | D1 | sohu.com | 搜狐 | — |
| TA1-24 | B | B3k | lejucaijing.com | 乐居财经 | — |
| TA1-25 | B | B3k | news.qq.com | 腾讯新闻 | — |
| TA1-26 | B | B3k | bbtnews.com.cn | 北京商报 | — |
| TA1-27 | B | B3k | wenshannet.com | 中访网 | — |
| TA1-28 | B | B3k | furnituretoday.cn | 今日家居 FurnitureToday | 僅讀到標題 |
| TA1-29 | B | B3k | static.weeklyonstock.com | 证券市场周刊 | — |
| TA1-30 | B | B3k | jfdaily.com | 解放日报 | — |
| TA1-31 | B | B2s | stcn.com | 证券时报 | — |
| TA1-32 | B | B3k | finance.sina.com.cn | 新浪财经 | — |
| TA1-33 | D | D1 | zhuanlan.zhihu.com | 知乎 | — |
| TA1-34 | B | B3k | donews.com | DoNews | 僅讀到標題、對應或年份為推定 |
| TA1-35 | B | B3k | finance.eastmoney.com | 东方财富网 | — |
| TA1-36 | B | B3k | finance.sina.com.cn | 新浪财经 | — |
| TA1-37 | B | B3k | 21jingji.com | 21 经济网 | — |
| TA1-38 | B | B2s | disc.static.szse.cn | 东易日盛／深圳证券交易所 | — |
| TA1-39 | B | B3k | news.qq.com | 腾讯新闻 | — |
| TA1-40 | B | B3k | stock.10jqka.com.cn | 同花顺 | 僅讀到標題 |
| TA1-41 | A | A2 | lssmedia.setlink.set.or.th | SET（泰國證交所） | — |
| TA1-42 | A | A2 | lssmedia.setlink.set.or.th | SET（泰國證交所） | — |
| TA1-43 | B | B2 | api.prod.pi.financial | Pi Financial | — |
| TA1-44 | B | B2 | daolsecurities.co.th | DAOL Securities | — |
| TA1-45 | C | C4 | newsroom.lixil.com | LIXIL Newsroom | — |
| TA1-46 | B | B2 | s-housing.jp | 新建ハウジング | — |
| TA1-47 | B | B3k | jp.investing.com | Investing.com 日本版 | — |
| TA1-48 | D | D1 | note.com | 企業観察ノート（note） | — |
| TA1-49 | A | A2 | lixil.com | LIXIL | 僅讀到標題 |
| TA1-50 | A | A2 | bsx.com | DFI Retail Group | — |
| TA1-51 | B | B2k | swedcham.com.hk | 香港瑞典商會 Swedcham HK | — |
| TA1-52 | B | B2o | aplus.hkicpa.org.hk | HKICPA A Plus | — |
| TA1-53 | B | B3k | theedgemalaysia.com | The Edge Malaysia | — |
| TA1-54 | B | B3k | tribune.net.ph | Daily Tribune | — |
| TA1-55 | B | B3k | plus.inquirer.net | Inquirer Plus | — |
| TA1-56 | B | B2 | quartr.com | Quartr | — |
| TA1-57 | A | A2r | nikkei.com | スター・マイカ HD（日経 IR 轉載） | — |
| TA1-58 | A | A2r | finance.biggo.jp | BigGo ファイナンス | — |
| TA1-59 | B | B3k | finance.yahoo.co.jp | Yahoo!ファイナンス | — |
| TA1-60 | B | B2o | tokyo-takken.or.jp | 東京都宅地建物取引業協会 | 僅讀到標題 |
| TA1-61 | B | B3k | m.gelonghui.com | 格隆汇 | — |
| TA1-62 | B | B3k | finance.sina.cn | 华泰证券／新浪 | 對應或年份為推定 |
| TA1-63 | B | B2r | sgpjbg.com | 三个皮匠报告（转载奥维云网） | — |
| TA1-64 | B | B3k | news.qq.com | 腾讯新闻（转载奥维云网） | — |
| TA1-65 | B | B3k | news.qq.com | 腾讯新闻（转载奥维云网） | — |
| TA1-66 | B | B3k | finance.sina.com.cn | 新浪科技（转载奥维云网） | — |
| TA1-67 | D | D1 | m.163.com | 网易（转载奥维云网） | — |
| TA1-68 | C | C2 | qanvast.com | Qanvast | — |
| TA1-69 | B | B3k | edgeprop.sg | EdgeProp Singapore | — |
| TA1-70 | C | C2 | dollarsandsense.sg | DollarsAndSense | 對應或年份為推定 |
| TA1-71 | C | C3 | uchify.com | Uchify | — |
| TA1-72 | B | B3k | sedaily.com | 서울경제 | — |
| TA1-73 | B | B3k | m.news.nate.com | 네이트 뉴스 | — |
| TA1-74 | B | B3k | kyeongin.com | 경인일보 | — |
| TA1-75 | B | B3k | hankyung.com | 한국경제 | 對應或年份為推定 |
| TA1-76 | B | B3k | ilyosisa.co.kr | 일요시사 | — |
| TA1-77 | B | B3k | sedaily.com | 서울경제 | 對應或年份為推定 |
| TA1-78 | B | B3k | ryutsuu.biz | 流通ニュース | — |
| TA1-79 | D | D1 | note.com | NNAカンパサール（note） | — |
| TA1-80 | B | B3k | ryutsuu.biz | 流通ニュース | — |
| TA1-81 | B | B3k | diamond-rm.net | ダイヤモンド・チェーンストアオンライン | 僅讀到標題 |
| TA1-82 | B | B3k | bizspa.jp | bizSPA! | 僅讀到標題 |
| TA1-83 | B | B3k | the-shashi.com | The社史 | 對應或年份為推定 |
| TA1-84 | B | B3k | wwdjapan.com | WWDJAPAN | 對應或年份為推定 |
| TA1-85 | C | C4 | muji.net | MUJI HOUSE | — |
| TA1-86 | A | A2 | investor.indexlivingmall.com | Index Living Mall | — |
| TA1-87 | A | A2 | investor.indexlivingmall.com | Index Living Mall | — |
| TA1-88 | A | A2 | investor.indexlivingmall.com | Index Living Mall | — |
| TA1-89 | A | A2 | investor.indexlivingmall.com | Index Living Mall | — |
| TA1-90 | A | A2 | investor.indexlivingmall.com | Index Living Mall | — |
| TA1-91 | B | B3k | focusmalaysia.my | Focus Malaysia | — |
| TA1-92 | B | B3k | theedgemalaysia.com | The Edge Malaysia | 對應或年份為推定 |
| TA1-93 | B | B2 | quartr.com | Quartr | — |
| TA1-94 | B | B3k | idxchannel.com | IDX Channel | — |
| TA1-95 | B | B3k | beritakini.co.id | Beritakini | — |
| TA1-96 | B | B3k | theiconomics.com | The Iconomics | — |
| TA1-97 | B | B3k | investasi.kontan.co.id | Kontan | 對應或年份為推定 |
| TA1-98 | B | B3k | receh.in | Receh.in | — |
| TA1-99 | B | B3k | market.bisnis.com | Bisnis.com | 僅讀到標題 |
| TA1-100 | B | B3k | testing.dev.theedgesingapore.com | The Edge Singapore | — |
| TA1-101 | B | B3k | ig.com | IG | — |
| TA1-102 | B | B3k | marketing-interactive.com | Marketing-Interactive | 對應或年份為推定 |
| TA1-103 | A | A2 | fse.or.jp | TOTO（福岡證券交易所） | — |
| TA1-104 | A | A2r | nikkei.com | TOTO（日経 IR 轉載） | — |
| TA1-105 | D | D1 | x.com | 官報決算データベース（X） | — |
| TA1-106 | B | B3k | gyokaidigest.com | 業界ダイジェスト | 僅讀到標題 |
| TA1-107 | B | B3k | biz.heraldcorp.com | 헤럴드경제 | — |
| TA1-108 | B | B3k | news.nate.com | 네이트 뉴스 | — |
| TA1-109 | B | B3k | newspim.com | 뉴스핌 | 對應或年份為推定 |
| TA1-110 | B | B3m | sisaweek.com | 시사위크 | — |
| TA1-111 | B | B3k | datanews.co.kr | 데이터뉴스 | — |
| TA1-112 | C | C2 | lxzin.com | LX Z:IN | 僅讀到標題 |
| TA1-113 | A | A2 | static.cninfo.com.cn | 索菲亚家居／巨潮资讯 | — |
| TA1-114 | B | B3k | finance.sina.cn | 新浪财经 | — |
| TA1-115 | B | B3k | furnituretoday.cn | 今日家居 FurnitureToday | — |
| TA1-116 | B | B3k | m.jiemian.com | 界面新闻 | 僅讀到標題 |
| TA1-117 | A | A2k | finance-frontend-pc-dist.west.edge.storage-yahoo.jp | 株式会社インテリックス | — |
| TA1-118 | B | B2 | kabutan.jp | Kabutan（FISCO） | — |
| TA1-119 | A | A2k | intellex-hd.co.jp | 株式会社インテリックス | — |
| TA1-120 | A | A2r | nikkei.com | 株式会社インテリックスHD（日経 IR 轉載） | — |
| TA1-121 | C | C4 | order.com.tw | Order 歐德傢俱集團 | — |
| TA1-122 | B | B3k | furnituretoday.cn | 今日家居 FurnitureToday | 僅讀到標題 |
| TA2-01 | B | B3k | byline.network | Byline Network | — |
| TA2-02 | B | B3k | topdaily.kr | 톱데일리 | — |
| TA2-03 | B | B3k | news.nate.com | 네이트 뉴스 | — |
| TA2-04 | B | B3k | wowtale.net | 와우테일 | — |
| TA2-05 | B | B3k | zdnet.co.kr | ZDNet Korea | — |
| TA2-06 | B | B3k | hankyung.com | 한국경제 | — |
| TA2-07 | B | B3k | thereport.co.kr | 더리포트 | — |
| TA2-08 | C | C2 | ohstory.io | 오늘의집 ohstory | — |
| TA2-09 | B | B3k | newstap.co.kr | 뉴스탭 | — |
| TA2-10 | B | B3k | venturesquare.net | 벤처스퀘어 | — |
| TA2-11 | C | C3 | innoforest.co.kr | 혁신의숲 innoforest | — |
| TA2-12 | C | C4 | demoday.co.kr | 데모데이 | — |
| TA2-13 | B | B3k | outstanding.kr | 아웃스탠딩 | — |
| TA2-14 | B | B3k | view.asiae.co.kr | 아시아경제 | — |
| TA2-15 | B | B3k | v.daum.net | Daum | — |
| TA2-16 | B | B3k | nbd.com.cn | 每日经济新闻 | — |
| TA2-17 | B | B3k | finance.sina.com.cn | 新浪财经 | — |
| TA2-18 | B | B3k | finance.ifeng.com | 凤凰网 | — |
| TA2-19 | B | B3k | wenxuan.news | 文轩财经 | — |
| TA2-20 | B | B3k | news.qq.com | 腾讯新闻 | — |
| TA2-21 | B | B3k | finance.sina.com.cn | 新浪财经 | — |
| TA2-22 | B | B3k | tfcaijing.com | 投资时报／tfcaijing | — |
| TA2-23 | B | B3k | 21jingji.com | 21经济网 | — |
| TA2-24 | B | B3k | hstong.com | 华盛通 | — |
| TA2-25 | B | B3k | m.huxiu.com | 虎嗅 | — |
| TA2-26 | B | B3k | m.thepaper.cn | 澎湃新闻 | — |
| TA2-27 | B | B3k | news.qq.com | 腾讯新闻 | — |
| TA2-28 | B | B3k | finance.sina.com.cn | 新浪科技 | — |
| TA2-29 | D | D1 | c.m.163.com | 网易 | — |
| TA2-30 | B | B3k | caifuhao.eastmoney.com | 东方财富财富号 | — |
| TA2-31 | A | A1 | news.cn | 新华网 | — |
| TA2-32 | B | B3k | news.qq.com | 腾讯新闻 | — |
| TA2-33 | B | B2 | pdf.dfcfw.com | 土巴兔集团（东方财富 PDF） | — |
| TA2-34 | B | B2 | pdf.dfcfw.com | 保荐人（东方财富 PDF） | — |
| TA2-35 | B | B3k | finance.ce.cn | 中国经济网 | — |
| TA2-36 | B | B3k | m.thepaper.cn | 澎湃新闻 | — |
| TA2-37 | B | B3k | ep.ycwb.com | 羊城晚报 | — |
| TA2-38 | B | B3k | finance.sina.cn | 新浪财经 | — |
| TA2-39 | B | B3k | guancha.cn | 观察者网 | — |
| TA2-40 | B | B3k | jiemian.com | 界面新闻 | — |
| TA2-41 | D | D1 | 163.com | 网易订阅 | — |
| TA2-42 | B | B3k | lanjinger.com | 蓝鲸财经 | — |
| TA2-43 | B | B3k | smarthome.ofweek.com | OFweek 智能家居网 | — |
| TA2-44 | D | D1 | zhuanlan.zhihu.com | 知乎专栏 | — |
| TA2-45 | B | B3k | jiemian.com | 界面新闻 | — |
| TA2-46 | B | B3k | jiemian.com | 界面新闻 | — |
| TA2-47 | B | B3k | gelonghui.com | 格隆汇 | — |
| TA2-48 | C | C4 | globalcapital.com | GlobalCapital | 對應或年份為推定 |
| TA2-49 | C | C4 | globalcapital.com | GlobalCapital | 對應或年份為推定 |
| TA2-50 | B | B3k | globalventuring.com | Global Venturing | — |
| TA2-51 | B | B3k | technode.com | TechNode | — |
| TA2-52 | B | B3k | yicaiglobal.com | Yicai Global | — |
| TA2-53 | B | B3k | lejucaijing.com | 乐居财经 | — |
| TA2-54 | B | B3k | m.gelonghui.com | 格隆汇 | — |
| TA2-55 | B | B3k | news.qq.com | 腾讯新闻 | — |
| TA2-56 | B | B3k | jiemian.com | 界面新闻 | — |
| TA2-57 | B | B3k | lanjinger.com | 蓝鲸财经 | — |
| TA2-58 | B | B3k | jiemian.com | 界面新闻 | — |
| TA2-59 | B | B3k | nbd.com.cn | 每日经济新闻 | — |
| TA2-60 | B | B3k | jiemian.com | 界面新闻 | — |
| TA2-61 | B | B3k | entrackr.com | Entrackr | — |
| TA2-62 | B | B3k | inc42.com | Inc42 | — |
| TA2-63 | B | B3k | outlookbusiness.com | Outlook Business（PTI） | — |
| TA2-64 | B | B3k | theweek.in | The Week（PTI） | — |
| TA2-65 | B | B3k | pulse.d2cinsider.com | D2C Insider Pulse | — |
| TA2-66 | B | B3k | entrackr.com | Entrackr | — |
| TA2-67 | B | B3k | m.thewire.in | The Wire（PTI PR） | — |
| TA2-68 | C | C2 | franchiseindia.com | Franchise India | — |
| TA2-69 | B | B3k | motilaloswal.com | Motilal Oswal News | — |
| TA2-70 | B | B3k | entrackr.com | Entrackr | — |
| TA2-71 | B | B3k | inc42.com | Inc42 | — |
| TA2-72 | B | B3k | pulse.d2cinsider.com | D2C Insider Pulse | — |
| TA2-73 | C | C2 | 100.com.tw | 100室內設計 | — |
| TA2-74 | C | C2 | 100.com.tw | 100室內設計 | — |
| TA2-75 | C | C2 | 100.com.tw | 100室內設計 | — |
| TA2-76 | C | C2 | 100.com.tw | 100室內設計 | — |
| TA2-77 | C | C2 | 100.com.tw | 100室內設計 | — |
| TA2-78 | C | C2 | 100.com.tw | 100室內設計 | — |
| TA2-79 | C | C2 | searchome.net | 設計家 Searchome | — |
| TA2-80 | C | C2 | searchome.net | 設計家 Searchome | — |
| TA2-81 | C | C2 | play.google.com | 設計家 Searchome | — |
| TA2-82 | B | B3k | vulcanpost.com | Vulcan Post | 對應或年份為推定 |
| TA2-83 | B | B3k | newswav.com | Newswav（轉載） | — |
| TA2-84 | C | C2 | qanvast.com | Qanvast | — |
| TA2-85 | C | C2 | qanvast.com | Qanvast | — |
| TA2-86 | C | C2 | redbrick.sg | Redbrick | — |
| TA2-87 | C | C3 | prospeo.io | Prospeo（聚合站） | — |
| TA2-88 | C | C3 | app.dealroom.co | Dealroom（聚合站） | — |
| TA2-89 | C | C2 | craft.co | Craft（聚合站） | — |
| TA2-90 | C | C2 | cbinsights.com | CB Insights（聚合站） | — |
| TA2-91 | C | C3 | mdv.com.my | Malaysia Debt Ventures | — |
| TA2-92 | D | D1 | my-painter.com | 南大阪ペイントセンター | — |
| TA2-93 | C | C2k | flowertea.hatenadiary.jp | リフォーム花茶（部落格） | — |
| TA2-94 | D | D1 | onayami000.com | onayami000 | — |
| TA2-95 | D | D1 | gaiheki-ichiba.jp | 外壁市場 | — |
| TA2-96 | C | C2k | shou-blog.com | shou-blog | — |
| TA2-97 | D | D1 | atopico.com | atopico | — |
| TA2-98 | D | D1 | t23m-navi.jp | t23m-navi | — |
| TA2-99 | D | D1 | reform-site.net | reform-site.net | — |
| TA2-100 | D | D1 | websv.info | Webfolio | — |
| TA2-101 | C | C3 | m.catch.co.kr | 캐치（CATCH） | — |
| TA2-102 | C | C3 | incruit.com | 인크루트 | — |
| TA2-103 | C | C3 | wanted.co.kr | 원티드 | — |
| TA2-104 | C | C3 | thevc.kr | THE VC | — |
| TA2-105 | D | D1 | medium.com | Medium（jong-park） | — |
| TA2-106 | C | C3 | thevc.kr | THE VC | — |
| TA2-107 | C | C4 | demoday.co.kr | 데모데이 | — |
| TA2-108 | C | C2 | saramin.co.kr | 사람인 | — |
| TA2-109 | D | D1 | brunch.co.kr | brunch（個人） | — |
| TA2-110 | C | C2 | soomgo.com | 숨고 커뮤니티（使用者發文） | — |
| TA2-111 | C | C3 | yourator.co | Yourator（Toby 企業網誌） | — |
| TA2-112 | B | B3k | pcmarket.com.hk | PCM 電腦廣場 | — |
| TA2-113 | B | B3k | unwire.pro | unwire.pro | — |
| TA2-114 | B | B3k | ejtech.ai | EJ Tech | — |
| TA2-115 | C | C2 | hellotoby.com | HelloToby | — |
| TA2-116 | B | B3k | edigest.hk | 經濟一週 eDigest | — |
| TA2-117 | B | B3k | hk01.com | 香港01 深度報道 | — |
| TA2-118 | C | C3 | freelance.com.hk | HKfreelance | — |
| TA2-119 | B | B3k | hdfcsky.com | HDFC Sky | — |
| TA2-120 | B | B3k | entrackr.com | Entrackr | — |
| TA2-121 | B | B3k | cxodigitalpulse.com | CXO Digital Pulse | — |
| TA2-122 | B | B3k | rupeezy.in | Rupeezy | — |
| TA2-123 | B | B3k | ticker.finology.in | Finology Ticker | — |
| TA2-124 | B | B3k | 5paisa.com | 5paisa | — |
| TA2-125 | B | B3k | inc42.com | Inc42 | — |
| TA2-126 | B | B3m | india.entrepreneur.com | Entrepreneur India | — |
| TA2-127 | B | B3k | dealstreetasia.com | DealStreetAsia | — |
| TA2-128 | B | B3k | hybrid.co.id | Hybrid.co.id | — |
| TA2-129 | C | C3 | app.dealroom.co | Dealroom（聚合站） | — |
| TA2-130 | C | C3 | profiles.crustdata.com | Crustdata（聚合站） | — |
| TA2-131 | C | C2 | 1001startup.id | 1001startup.id（聚合站） | — |
| TA2-132 | C | C3 | pitchbook.com | PitchBook（聚合站） | — |
| TA2-133 | C | C3 | owler.com | Owler（聚合站） | — |
| TA2-134 | C | C3 | zoominfo.com | ZoomInfo（聚合站） | — |
| TA2-135 | D | D1 | linkedin.com | LinkedIn Pulse | — |
| TA2-136 | C | C3 | growjo.com | Growjo（聚合站） | — |
| TA2-137 | C | C3 | pinterest.com | Pinterest（Dekoruma） | — |
| TA2-138 | B | B5 | entrepreneur.uai.ac.id | UAI Entrepreneur | — |
| TA2-139 | B | B3k | hybrid.co.id | Hybrid.co.id | — |
| TA2-140 | A | A1 | beijing.gov.cn | 北京市人民政府（首都之窗） | — |
| TA2-141 | A | A1 | natcm.gov.cn | 国家中医药管理局（转载国务院信息） | — |
| TA2-142 | B | B3k | yicai.com | 第一财经 | — |
| TA2-143 | A | A1 | news.cn | 新华网 | — |
| TA2-144 | B | B2 | pdf.dfcfw.com | 东方财富 PDF | — |
| TA2-145 | B | B2 | pdf.hanspub.org | 汉斯出版社 | — |
| TA2-146 | C | C2 | arc-navi.shikaku.co.jp | 建築資料研究社 arc-navi | — |
| TA2-147 | B | B3k | housing-news.build-app.jp | BuildApp News | — |
| TA2-148 | B | B3k | xtech.nikkei.com | 日経クロステック | — |
| TA2-149 | A | A1 | mlit.go.jp | 国土交通省 | — |
| TA2-150 | B | B2 | j-eri.co.jp | 日本ERI | — |
| TA2-151 | B | B3k | built.itmedia.co.jp | BUILT（ITmedia） | — |
| TA2-152 | C | C2 | arc-navi.shikaku.co.jp | 建築資料研究社 arc-navi | — |
| TA2-153 | B | B2 | pivot.co.jp | 構造システム | — |
| TC-01 | B | B2 | digital.cushmanwakefield.com | Cushman & Wakefield | — |
| TC-02 | B | B2 | digital.cushmanwakefield.com | Cushman & Wakefield | — |
| TC-03 | B | B2 | cushmanwakefield.com | Cushman & Wakefield | — |
| TC-04 | B | B2 | cw-prod-gblgws-a-cm.cushwake.com | Cushman & Wakefield | — |
| TC-05 | B | B2 | cushmanwakefield.com | Cushman & Wakefield | — |
| TC-06 | B | B2 | cushmanwakefield.com | Cushman & Wakefield | — |
| TC-07 | C | C2 | realtynmore.com | Realty n More | — |
| TC-08 | B | B3k | ianslive.in | IANS | — |
| TC-09 | B | B2 | cw-prod-apacgws-a-cd.cushwake.com | Cushman & Wakefield India | — |
| TC-10 | B | B2 | naredco.in | NAREDCO | 對應或年份為推定 |
| TC-11 | C | C2 | retalkasia.com | Real Estate Asia（retalkasia） | — |
| TC-12 | C | C2 | commo.com.au | The Commercial Real Estate（commo） | — |
| TC-13 | B | B2 | cushmanwakefield.com | Cushman & Wakefield Australia | — |
| TC-14 | B | B2 | aprea.asia | APREA | — |
| TC-15 | B | B3k | taipeitimes.com | Taipei Times | — |
| TC-16 | B | B2 | assets.cushmanwakefield.com | Cushman & Wakefield Korea | — |
| TC-17 | B | B3k | malaymail.com | Malay Mail／Media OutReach | — |
| TC-18 | B | B3k | alvinology.com | Alvinology | — |
| TC-19 | B | B3k | cinn.cn | 中国工业新闻网（cinn.cn） | — |
| TC-20 | B | B2r | fxbaogao.com | 发现报告（fxbaogao） | — |
| TC-21 | C | C2 | ashb.com | JLL（ASHB 轉載 PDF） | — |
| TC-22 | B | B2 | irei.com | IREI | — |
| TC-23 | B | B2 | jll.com | JLL India | — |
| TC-24 | B | B2 | jll.com | JLL India | — |
| TC-25 | B | B2 | jll.com | JLL | — |
| TC-26 | B | B2 | joneslanglasalle.com.cn | 仲量联行（JLL China） | — |
| TC-27 | B | B2 | reports.turnerandtownsend.com | Turner & Townsend | — |
| TC-28 | B | B2 | reports.turnerandtownsend.com | Turner & Townsend | — |
| TC-29 | B | B2 | reports.turnerandtownsend.com | Turner & Townsend | — |
| TC-30 | B | B2 | turnerandtownsend.com | Turner & Townsend | — |
| TC-31 | B | B2 | reports.turnerandtownsend.com | Turner & Townsend | — |
| TC-32 | B | B2 | reports.turnerandtownsend.com | Turner & Townsend | — |
| TC-33 | C | C2 | realtynmore.com | Realty n More | — |
| TC-34 | B | B2 | media.arcadis.com | Arcadis Hong Kong Limited | — |
| TC-35 | B | B3k | kjob.news | 전국인력신문（kjob.news） | — |
| TC-36 | C | C2 | spacelogin.co.kr | 스페이스로그인（spacelogin） | — |
| TC-37 | C | C2 | interiorcnote.com | 오피스 인테리어 컨설팅 랩（interiorcnote） | 對應或年份為推定 |
| TC-38 | C | C2 | ssjum.com | ssjum.com | — |
| TC-39 | C | C2 | lingqisj.com | 领企装修公司 | — |
| TC-40 | D | D1 | c.m.163.com | 网易（163.com） | 對應或年份為推定 |
| TC-41 | B | B2 | cushmanwakefield.com | Cushman & Wakefield Greater China | — |
| TC-42 | B | B2 | cushwake.cld.bz | Cushman & Wakefield | — |
| TC-43 | C | C1 | newswire.co.kr | 뉴스와이어（newswire.co.kr） | — |
| TC-44 | B | B2 | cw-prod-apacgws-a-cd.cushwake.com | Cushman & Wakefield India | — |
| TC-45 | D | D1 | 163.com | 网易订阅（163.com） | — |
| TC-46 | B | B2s | stcn.com | 证券时报网（stcn.com） | — |
| TC-47 | B | B2 | cushmanwakefield.com | Cushman & Wakefield | — |
| TC-48 | B | B2 | cushmanwakefield.com | Cushman & Wakefield Korea | — |
| TC-49 | B | B2 | commercialsearch.com | Commercial Property Executive | — |
| TC-50 | B | B2r | slideshare.net | SlideShare（轉載） | — |
| TC-51 | B | B2 | jll.com.sg | JLL Singapore | — |
| TC-52 | B | B2 | mcmorrowreports.com | McMorrow Reports | — |
| TC-53 | B | B2 | jll.com | JLL Southeast Asia | 對應或年份為推定 |
| TC-54 | B | B2 | digital.cushmanwakefield.com | Cushman & Wakefield | — |
| TC-55 | B | B2 | arcadis.com | Arcadis Hong Kong Limited | — |
| TC-56 | B | B2 | media.arcadis.com | Arcadis | — |
| TC-57 | B | B2 | arcadis.com | Arcadis | — |
| TC-58 | B | B2 | rlb.com | Rider Levett Bucknall | — |
| TC-59 | B | B2 | rlb.com | Rider Levett Bucknall | — |
| TC-60 | C | C2 | howroom.ai | howroom | — |
| TC-61 | C | C2 | pro360.com.tw | PRO360達人網 | — |
| TC-62 | D | D1 | rinzh.com | rinzh | 對應或年份為推定 |
| TC-63 | C | C2 | dahuandesign.com | 大桓設計（Dahuan） | 對應或年份為推定 |
| TC-64 | D | D1 | goodlivingnotes.com | 好感生活提案 | 對應或年份為推定 |
| TC-65 | C | C2 | into-atelier.com.tw | 介入空間設計 | 對應或年份為推定 |
| TC-66 | C | C2 | ude-design.com.tw | 優德室內裝修設計 | 對應或年份為推定 |
| TC-67 | B | B2 | colliers.com | Colliers Japan | — |
| TC-68 | C | C2 | realestateasia.com | Real Estate Asia | — |
| TC-69 | B | B3k | ohsem.me | ohsem.me | — |
| TC-70 | C | C2 | realestateasia.com | Real Estate Asia | — |
| TC-71 | B | B2 | research.jllapsites.com | JLL | — |
| TC-72 | B | B3k | money.udn.com | 經濟日報（money.udn.com） | — |
| TC-73 | B | B3k | house.ettoday.net | ETtoday 房產雲 | — |
| TC-74 | B | B3k | businessinsider.tw | Business Insider Taiwan | — |
| TC-75 | B | B3k | chinatimes.com | 中時新聞網 | 候選出處、對應或年份為推定 |
| TC-76 | B | B3k | estate.ltn.com.tw | 自由時報地產天下 | 對應或年份為推定 |
| TC-77 | B | B3k | fbs168.com | 富比士地產王 | 對應或年份為推定 |
| TC-78 | B | B3k | view.asiae.co.kr | 아시아경제（asiae） | — |
| TC-79 | B | B3k | kcenews.kr | kcenews | — |
| TC-80 | C | C1 | newswire.co.kr | 뉴스와이어（newswire.co.kr） | — |
| TC-81 | B | B3k | venturesquare.net | 벤처스퀘어（venturesquare） | — |
| TC-82 | D | D1 | sohu.com | 搜狐 | — |
| TC-83 | D | D1 | 163.com | 网易订阅（163.com） | — |
| TC-84 | B | B3k | guandian.cn | 观点网（guandian.cn） | — |
| TC-85 | B | B2 | colliers.com.cn | 高力国际（Colliers China） | — |
| TC-86 | B | B2 | content.knightfrank.com | 莱坊（Knight Frank China） | — |
| TC-87 | B | B3k | house.cnr.cn | 央广网（cnr.cn） | — |
| TC-88 | B | B2r | m.hibor.com.cn | 慧博投研资讯（hibor） | — |
| TC-89 | C | C2 | realestateasia.com | Real Estate Asia | — |
| TC-90 | B | B2 | research.jllapsites.com | JLL | — |
| TC-91 | B | B2 | cushmanwakefield.com | Cushman & Wakefield Thailand | — |
| TC-92 | C | C2 | realestateasia.com | Real Estate Asia | — |
| TC-93 | B | B2 | cushmanwakefield.com | Cushman & Wakefield Vietnam | — |
| TC-94 | B | B2 | cushmanwakefield.com | Cushman & Wakefield Vietnam | — |
| TC-95 | B | B2 | crematrix.com | CREmatrix | 對應或年份為推定 |
| TC-96 | B | B2 | jll.com | JLL India | 對應或年份為推定 |
| TC-97 | C | C3 | meraqiadvisors.com | Meraqi Advisors | 對應或年份為推定 |
| TC-98 | C | C2 | lodgingeconometrics.com | Lodging Econometrics | — |
| TC-99 | C | C2 | lodgingeconometrics.com | Lodging Econometrics | — |
| TC-100 | C | C2 | lodgingeconometrics.com | Lodging Econometrics | — |
| TC-101 | C | C2 | hotel-online.com | Hotel-Online（日期欄誤植為 2025-08-06） | — |
| TC-102 | C | C2 | dlr.skift.com | Skift Daily Lodging Report | — |
| TC-103 | B | B2 | kabutan.jp | 株探（かぶたん） | — |
| TC-104 | B | B2 | kabutan.jp | 株探（かぶたん） | — |
| TC-105 | A | A2r | nikkei.com | 日本経済新聞 | — |
| TC-106 | D | D1 | note.com | SHO-CASE（note） | — |
| TC-107 | D | D1 | note.com | SHO-CASE（note） | — |
| TC-108 | B | B2 | basic.10jqka.com.cn | 同花顺 | — |
| TC-109 | B | B2 | basic.10jqka.com.cn | 同花顺 | — |
| TC-110 | B | B3k | static.weeklyonstock.com | 证券市场周刊 | — |
| TC-111 | B | B3k | finance.sina.com.cn | 新浪财经 | — |
| TC-112 | B | B3k | money.udn.com | 經濟日報（money.udn.com） | — |
| TC-113 | B | B3k | udn.com | 聯合新聞網 | — |
| TC-114 | B | B3k | money.udn.com | 經濟日報 | 對應或年份為推定 |
| TC-115 | B | B3k | news.cnyes.com | 鉅亨網 | 對應或年份為推定 |
| TC-116 | B | B2o | ieknet.iek.org.tw | 工研院產科國際所 IEK | 對應或年份為推定 |
| TC-117 | C | C4 | ytyut.com | 詠騰不動產 | 對應或年份為推定 |
| TD-01 | A | A1 | jutaku-shoene2026.mlit.go.jp | 國土交通省・經濟產業省・環境省 | — |
| TD-02 | A | A1 | mlit.go.jp | 國土交通省 | — |
| TD-03 | A | A1 | kyutou-shoene2026.meti.go.jp | 經濟產業省 | — |
| TD-04 | A | A1 | kyutou-shoene2026.meti.go.jp | 經濟產業省 | — |
| TD-05 | C | C2 | reform-hojo.jp | reform-hojo.jp | — |
| TD-06 | C | C2 | hojyokin-portal.jp | 補助金ポータル | — |
| TD-07 | C | C2 | dannetsu-takumi.com | 断熱リフォームの匠 | — |
| TD-08 | C | C2 | rise-creation.com | Rise Creation | — |
| TD-09 | C | C2 | hojyokin-portal.jp | 補助金ポータル | — |
| TD-10 | A | A1 | city.mitsuke.niigata.jp | 見附市（新潟縣） | — |
| TD-11 | C | C2 | finance.recruit.co.jp | リクルート（finance.recruit.co.jp） | — |
| TD-12 | C | C4 | nojima.co.jp | ノジマ | — |
| TD-13 | C | C2 | hojyokin-portal.jp | 補助金ポータル | — |
| TD-14 | C | C4 | glass-wonderland.jp | 日本板硝子 | — |
| TD-15 | C | C2 | furureno.jp | furureno | — |
| TD-16 | C | C2 | seikatsu-do.com | 生活堂 | — |
| TD-17 | A | A1 | mlit.go.jp | 國土交通省 | — |
| TD-18 | A | A1 | r07.choki-reform.mlit.go.jp | 國土交通省（事業事務局） | — |
| TD-19 | A | A1 | city.yokohama.lg.jp | 橫濱市 | — |
| TD-20 | A | A1 | city.ota.tokyo.jp | 大田區（東京都） | — |
| TD-21 | A | A1 | mlit.go.jp | 國土交通省 | — |
| TD-22 | B | B2k | j-reform.com | 住宅リフォーム推進協議会（j-reform.com） | — |
| TD-23 | C | C2 | roomie.jp | roomie.jp | 候選出處 |
| TD-24 | B | B2 | yano.co.jp | 矢野経済研究所 | — |
| TD-25 | C | C2 | crex-data.com | CREX（crex-data.com） | — |
| TD-26 | B | B3k | view.asiae.co.kr | 아시아경제 | — |
| TD-27 | A | A1 | korea.kr | 대한민국 정책브리핑（korea.kr） | — |
| TD-28 | B | B3k | m.news.nate.com | 네이트 뉴스 | — |
| TD-29 | B | B3k | asiae.co.kr | 아시아경제 | — |
| TD-30 | B | B2o | kalis.or.kr | 국토안전관리원（KALIS） | — |
| TD-31 | B | B3k | imaeil.com | 매일신문 | — |
| TD-32 | B | B3k | ajunews.com | 아주경제 | — |
| TD-33 | A | A1 | gg.go.kr | 경기도 | — |
| TD-34 | C | C2 | welfarehello.com | 웰페어헬로（welfarehello） | — |
| TD-35 | B | B3k | bravo.etoday.co.kr | 브라보마이라이프（이투데이）；同文轉載 https://m.news.nate. | — |
| TD-36 | B | B3m | news.tf.co.kr | 더팩트 | — |
| TD-37 | B | B3k | heraldk.com | 헤럴드（heraldk） | — |
| TD-39 | A | A1 | tour.gunsan.go.kr | 군산시（附件） | — |
| TD-40 | C | C2 | edh.tw | 早安健康（edh.tw） | — |
| TD-41 | B | B3k | smart.businessweekly.com.tw | Smart 智富（商業周刊） | — |
| TD-42 | B | B3k | commonhealth.com.tw | 康健雜誌（commonhealth.com.tw） | — |
| TD-43 | A | A1 | laws.taipei.gov.tw | 臺北市政府（法規查詢系統） | — |
| TD-44 | A | A1 | wd.vghtpe.gov.tw | 臺北市政府社會局（經臺北榮總網站） | — |
| TD-45 | C | C2 | money101.com.tw | Money101 | — |
| TD-46 | B | B3k | ec.ltn.com.tw | 自由時報（經濟） | — |
| TD-47 | B | B3k | ec.ltn.com.tw | 自由時報（即時） | — |
| TD-48 | A | A1 | nlma.gov.tw | 內政部國土管理署 | — |
| TD-49 | B | B2k | ur.org.tw | 財團法人都市更新研究發展基金會 | — |
| TD-50 | B | B3k | chinatimes.com | 工商時報 | — |
| TD-51 | C | C4 | jhlanddev.com.tw | 佳泓開發（jhlanddev） | — |
| TD-52 | C | C4 | turfs.com.tw | 臺灣金融聯合都市更新服務股份有限公司 | — |
| TD-53 | C | C2k | hcdesign.com.tw | 黃巢設計工務店 | 對應或年份為推定 |
| TD-54 | C | C2 | banks.tw | banks.tw | 對應或年份為推定 |
| TD-55 | C | C2 | housefeel.com.tw | HouseFeel 房感 | — |
| TD-56 | A | A1 | gov.cn | 中国政府网（商务部等 6 部门） | — |
| TD-57 | A | A1 | news.cn | 新华网 | — |
| TD-58 | B | B3k | ce.cn | 中国经济网 | — |
| TD-59 | A | A1 | mofcom.gov.cn | 商务部 | — |
| TD-60 | A | A1 | gz.gov.cn | 广州市人民政府 | — |
| TD-61 | C | C2 | m.fz.bendibao.com | 福州本地宝 | — |
| TD-62 | A | A1 | mofcom.gov.cn | 商务部 | — |
| TD-63 | A | A1 | ndrc.gov.cn | 国家发展和改革委员会 | — |
| TD-64 | B | B3k | news.10jqka.com.cn | 同花顺财经（10jqka） | — |
| TD-65 | B | B3k | jiemian.com | 界面新闻 | — |
| TD-66 | B | B3k | m.gelonghui.com | 格隆汇 | — |
| TD-67 | B | B3k | thepaper.cn | 澎湃新闻 | — |
| TD-68 | B | B3k | m.gelonghui.com | 格隆汇 | — |
| TD-69 | B | B3k | cn.chinadaily.com.cn | 中国日报网 | — |
| TD-70 | D | D1 | c.m.163.com | 网易（163.com） | — |
| TD-71 | A | A1 | hdb.gov.sg | Housing & Development Board | — |
| TD-72 | A | A1 | hdb.gov.sg | Housing & Development Board | — |
| TD-73 | A | A1 | cpf.gov.sg | CPF Board | — |
| TD-74 | A | A1 | gov.sg | gov.sg | 對應或年份為推定 |
| TD-75 | C | C4 | healthhub.sg | HealthHub（衛生部） | — |
| TD-76 | C | C2 | dollarsandsense.sg | DollarsAndSense | — |
| TD-77 | A | A1 | gia.info.gov.hk | 香港特區政府（gia.info.gov.hk） | — |
| TD-78 | B | B3k | stheadline.com | 星島頭條 | — |
| TD-79 | B | B3k | hk01.com | 香港01 | — |
| TD-80 | A | A1 | legco.gov.hk | 香港立法會 | — |
| TD-81 | A | A1 | gia.info.gov.hk | 香港特區政府 | — |
| TD-82 | B | B3k | investortrust.id | Investortrust | — |
| TD-83 | B | B3k | ekonomi.bisnis.com | Bisnis.com | — |
| TD-84 | B | B3k | antaranews.com | Antara News | — |
| TD-85 | B | B3k | investortrust.id | Investortrust | — |
| TD-86 | B | B3k | ekonomi.bisnis.com | Bisnis.com | 僅讀到標題 |
| TD-87 | B | B3k | rri.co.id | RRI | 僅讀到標題 |
| TD-88 | B | B2l | siplawfirm.id | SIP Law Firm | 對應或年份為推定 |
| TD-89 | B | B3k | mrem.bernama.com | Bernama（MREM） | — |
| TD-90 | C | C2 | edgeprop.my | EdgeProp Malaysia | — |
| TD-91 | C | C1 | kenresearch.com | Ken Research | — |
| TD-92 | A | A1 | rd.go.th | กรมสรรพากร 地區分局（Saraburi） | — |
| TD-93 | B | B2l | hlbthai.com | HLB Thailand | — |
| TD-94 | C | C4 | expattaxthailand.com | Expat Tax Thailand | — |
| TD-95 | A | A1 | media.thaigov.go.th | 泰國政府（thaigov.go.th） | 對應或年份為推定 |
| TD-96 | B | B3k | vneconomy.vn | VnEconomy | — |
| TD-97 | B | B2 | edgebuildings.com | IFC（EDGE Buildings） | — |
| TD-98 | B | B2 | edgebuildings.com | IFC（EDGE Buildings） | — |
| TD-99 | B | B3m | philstar.com | The Philippine Star | — |
| TD-100 | B | B3m | sunstar.com.ph | SunStar Cebu | — |
| TD-101 | B | B3k | abs-cbn.com | ABS-CBN | — |
| TD-102 | B | B3k | tribune.net.ph | Daily Tribune | — |
| TD-103 | B | B2r | slideshare.net | SlideShare（上傳者不明） | — |
| TE-01 | B | B3k | bnext.com.tw | 數位時代 | — |
| TE-02 | B | B3k | cna.com.tw | 中央社 | — |
| TE-03 | B | B3k | mirrormedia.mg | 鏡週刊 | — |
| TE-05 | B | B3k | newstomato.com | 뉴스토마토 | — |
| TE-06 | B | B3k | m.thebell.co.kr | 더벨 | — |
| TE-07 | B | B3k | m.businesspost.co.kr | 비즈니스포스트 | — |
| TE-08 | B | B3k | topdaily.kr | 탑데일리 | — |
| TE-09 | B | B3k | newswave.kr | 뉴스웨이브 | — |
| TE-10 | B | B3k | edaily.co.kr | 이데일리 | — |
| TE-12 | C | C3 | finboard.jp | finboard | — |
| TE-13 | B | B3k | ryutsuu.biz | 流通ニュース | — |
| TE-14 | B | B3k | yicaiglobal.com | Yicai Global | — |
| TE-15 | B | B3m | gendai.media | 現代ビジネス | — |
| TE-16 | B | B3m | 36kr.jp | 36Kr Japan | — |
| TE-17 | B | B3k | zaikei.co.jp | 財経新聞 | — |
| TE-18 | B | B3k | hokkaido-np.co.jp | 北海道新聞 | — |
| TE-19 | A | A2r | nikkei.com | 日本経済新聞 | — |
| TE-20 | C | C1 | prtimes.jp | ニトリ（PR TIMES） | — |
| TE-21 | B | B3k | business.nikkei.com | 日経ビジネス | — |
| TE-22 | C | C1 | kyodonewsprwire.jp | Kyodo News PR Wire | — |
| TE-23 | C | C1 | kyodonewsprwire.jp | Kyodo News PR Wire | — |
| TE-24 | B | B3m | thuonghieucongluan.com.vn | Thương hiệu & Công luận | — |
| TE-25 | C | C2 | brandwiki.lazada.sg | Lazada Singapore | — |
| TE-26 | B | B3k | insideretail.asia | Inside Retail Asia | — |
| TE-27 | A | A2 | muji.com | 良品計画 MUJI | — |
| TE-28 | B | B3k | retail-insight-network.com | Retail Insight Network | — |
| TE-29 | B | B3k | indiaretailing.com | IndiaRetailing | — |
| TE-30 | B | B3m | us.fashionnetwork.com | FashionNetwork | — |
| TE-31 | B | B3k | ianslive.in | IANS | — |
| TE-32 | B | B3k | indianretailer.com | Indian Retailer | — |
| TE-33 | B | B3m | storyboard18.com | Storyboard18 | — |
| TE-34 | B | B3k | interiordaily.com | Interior Daily | — |
| TE-35 | B | B3k | propnewstime.com | PropNewsTime | — |
| TE-36 | B | B3k | interiordaily.com | Interior Daily | — |
| TE-37 | B | B3k | asia.nikkei.com | Nikkei Asia（DealStreetAsia） | — |
| TE-38 | B | B3m | peoplematters.in | People Matters | — |
| TE-39 | B | B3k | inc42.com | Inc42 | — |
| TE-40 | B | B3k | news.crunchbase.com | Crunchbase News | — |
| TE-41 | C | C1 | businesswire.com | Business Wire | — |
| TE-42 | B | B3k | edgeprop.sg | EdgeProp Singapore | — |
| TE-43 | B | B3k | testing.dev.theedgesingapore.com | The Edge Singapore | — |
| TE-45 | B | B3k | startupnews.fyi | Startupnews.fyi | — |
| TE-46 | D | D1 | en.wikipedia.org | Wikipedia | — |
| TE-47 | C | C2 | qanvast.com | Qanvast | — |
| TE-48 | C | C2 | qanvast.com | Qanvast | — |
| TE-49 | B | B3k | vulcanpost.com | Vulcan Post | — |
| TE-50 | C | C2 | qanvast.com | Qanvast MY | — |
| TE-51 | A | A2 | www1.hkexnews.hk | HKEXnews／梁志天設計集團 | — |
| TE-52 | A | A2 | www1.hkexnews.hk | HKEXnews／梁志天設計集團 | — |
| TE-53 | A | A2 | www1.hkexnews.hk | HKEXnews／梁志天設計集團 | — |
| TE-54 | B | B2 | il.tipranks.com | TipRanks | — |
| TE-55 | C | C1 | media-outreach.vn | Media OutReach | — |
| TE-56 | C | C4 | arezdesignconsultant.com | 亞俬設計顧問（Arez Design Consultant） | — |
| TE-57 | B | B2 | housenews.jp | 住宅新報 | — |
| TE-58 | B | B3k | data-max.co.jp | NetIB-News（データ・マックス） | — |
| TE-59 | B | B3m | therealdeal.com | The Real Deal | — |
| TE-60 | D | D1 | en.wikipedia.org | Wikipedia | — |
| TE-61 | A | A2r | nikkei.com | 日本経済新聞 | — |
| TE-62 | A | A2 | www2.jpx.co.jp | LIXIL／日本取引所グループ | — |
| TE-63 | B | B3k | dealstreetasia.com | DealStreetAsia | — |
| TE-64 | C | C4 | nihon-ma.co.jp | 日本M&Aセンター | — |
| TE-65 | B | B3k | business-standard.com | Business Standard／Reuters | — |
| TE-66 | C | C4 | group.ikano | Ikano Group | — |
| TE-67 | B | B3k | nst.com.my | New Straits Times | — |
| TE-68 | B | B3k | bworldonline.com | BusinessWorld | — |
| TE-69 | B | B3k | jingdaily.com | Jing Daily | — |
| TE-70 | B | B3k | news.tuoitre.vn | Tuổi Trẻ News | — |
| TE-71 | B | B3k | retail-insight-network.com | Retail Insight Network | — |
| TE-72 | B | B3k | inc42.com | Inc42 | — |
| TE-73 | B | B3k | insideretail.asia | Inside Retail Asia | — |
| TE-74 | C | C3 | sg.linkedin.com | LinkedIn | — |
| TE-75 | B | B2 | pdf.dfcfw.com | 梁志天設計集團／東方財富 | — |
| TE-76 | B | B4 | lixinger.com | 理杏仁 Lixinger | — |
| TE-77 | B | B3k | finance.sina.com.cn | 新浪財經 | — |
| TE-78 | B | B3k | finance.sina.com.cn | 新浪財經 | — |
| TE-79 | B | B3k | m.rccaijing.com | 瑞財經 | — |
| TE-80 | B | B3m | 21jingji.com | 21 經濟網 | — |
| TE-81 | B | B3k | finance.sina.com.cn | 新浪財經 | — |
| TE-82 | B | B3k | finance.sina.com.cn | 新浪財經 | — |
| TE-83 | B | B3k | wallstreetcn.com | 華爾街見聞 | — |
| TE-84 | B | B3k | news.cnyes.com | 鉅亨網 | — |
| TE-85 | B | B3m | furnituretoday.com | Furniture Today | — |
| TE-86 | B | B3k | cnbce.com | CNBC-e | — |
| TE-87 | A | A2 | www2.jpx.co.jp | LIXIL／日本取引所グループ | — |
| TF-01 | A | A1 | federalreserve.gov | 美國聯邦準備理事會（Board of Governors of the Fede | 多個候選 URL |
| TF-02 | A | A1 | federalreserve.gov | 美國聯邦準備理事會 | — |
| TF-03 | A | A1 | fred.stlouisfed.org | St. Louis Fed（FRED） | — |
| TF-04 | A | A1 | federalreserve.gov | 美國聯邦準備理事會 | — |
| TF-05 | B | B3k | udn.com | 聯合報（udn） | — |
| TF-06 | A | A1 | fred.stlouisfed.org | St. Louis Fed（FRED） | — |
| TF-07 | B | B3k | finance.technews.tw | TechNews 科技新報（整理中央社） | 候選出處 |
| TF-08 | B | B3k | gulfnews.com | Gulf News | — |
| TF-09 | B | B3k | gulfnews.com | Gulf News | 候選出處 |
| TF-10 | C | C1 | exchangerate.dev | exchangerate.dev | — |
| TF-11 | B | B5 | iainkendari.ac.id | IAIN Kendari（印尼國立伊斯蘭學院肯達里分校） | — |
| TF-12 | A | A1 | bi.go.id | Bank Indonesia | — |
| TF-13 | A | A1 | bi.go.id | Bank Indonesia | — |
| TF-14 | B | B4 | ceicdata.com | CEIC Data（引用世界銀行／SBV） | — |
| TF-15 | C | C2 | exchange-rates.org | exchange-rates.org | — |
| TF-16 | C | C1 | focus-economics.com | FocusEconomics | — |
| TF-17 | A | A1 | nief.mof.gov.vn | Viện Kinh tế và Tài chính（Bộ Tài chính，越 | — |
| TF-18 | B | B4 | worldometers.info | Worldometer（轉載 IMF WEO 2026 年 4 月版） | — |
| TF-19 | B | B4 | worldometers.info | Worldometer（表頭標「Source: IMF, World Econo | — |
| TF-20 | B | B4 | worldometers.info | Worldometer | — |
| TF-21 | B | B4 | worldometers.info | Worldometer | — |
| TF-22 | A | A1 | imf.org | IMF | — |
| TF-23 | B | B4 | theglobaleconomy.com | TheGlobalEconomy.com（UN 來源） | — |
| TF-24 | B | B4 | theglobaleconomy.com | TheGlobalEconomy.com（世界銀行系列） | — |
| TF-25 | C | C4 | visualcapitalist.com | Visual Capitalist（UN 資料） | — |
| TF-26 | A | A1 | population.un.org | 聯合國經濟和社會事務部人口司（UN DESA Population Divisi | — |
| TF-27 | B | B4 | worldometers.info | Worldometer（UN 資料） | — |
| TF-28 | B | B4 | worldometers.info | Worldometer | — |
| TW-C1 | D | D3 | taiwannews.com.tw | 多個媒體或平台（未確認單一出處） | 候選出處、多個候選 URL |
| TW-C2 | D | D3 | ctee.com.tw | 多個媒體或平台（未確認單一出處） | 候選出處、多個候選 URL |
| TW-C8 | D | D3 | businesstoday.com.tw | 多個媒體或平台（未確認單一出處） | 候選出處、多個候選 URL |
| TW-C9 | D | D3 | vocus.cc | 多個媒體或平台（未確認單一出處） | 候選出處 |
