---
ai: claude
mode: research（Claude Code 雲端會話；以 r1 筆記為基底＋補搜）
date: 2026-10-10
scope: country:MY
prompt_version: v1
notes: 單一市場深潛（country-module-template v1）。來源僅經搜尋結果內容讀取，未直接開頁；與 V1 獨立。補搜 30 次（其中在地語言 15 次）。
---

# 馬來西亞（Malaysia）室內裝修設計市場深潛：中古屋撐需求、法規切分設計與施工（以台灣為基準）r1

## 0. 中繼資料

| 項目 | 內容 |
|---|---|
| AI | Claude |
| 模式 | Claude Code 雲端會話 Research（以 r1 筆記為基底＋補搜） |
| 日期 | 2026-10-10 |
| 範圍 | 單一市場：馬來西亞（代碼 MY）；比較基準：台灣 |
| 委託方情境 | 璞石集團（CEO Banson；室內裝修設計＋不動產＋家居零售；基地宜蘭、台北信義） |
| 搜尋語言 | 本輪補搜 30 次：英文 15、馬來文 8、馬來西亞華文 7（其中 5 次限定星洲日報、南洋商報、中國報、東方日報網域）。底稿 r1 兩輪另有 26 次成功搜尋（馬來文 7、華文 4） |
| 來源數 | 186 條：沿用 r1 編號 85 條（MY-xx）＋本輪新增 92 條（MY-D01～MY-D92）＋台灣／總體錨點 9 條（TW-xx、TF-xx）。其中在地語言（馬來文、馬來西亞華文）56 條（本輪新增 43 條） |
| 匯率 | 聯準會 G.5A 2025 年平均（TF-01）：1 USD＝4.2809 MYR＝31.1663 TWD；1 MYR＝7.2803 TWD。為了可比，所有年份的金額都用 2025 年平均換算 |
| 面積 | 1 m²＝10.7639 sq ft；1 坪＝3.3058 m²；每 sq ft 單價 × 35.58＝每坪單價 |
| 標示 | 【實際】＝來源直接報告的數字；【示意】＝本報告計算、加總或推估的數字，以及業者行銷頁、市調公司口徑 |
| 限制 | (1) 所有來源都只透過搜尋結果內容（工具摘要）讀取，沒有直接開啟原頁；本環境無法使用 WebFetch／curl。(2) 部分數字無法精確對應到單一 URL，已標「對應不確定」並降低信心。(3) 本報告與 V1（04-research-notes、05-report）獨立，未讀取 V1。(4) TF 筆記沒有馬來西亞的人口與名目 GDP 總額，因此人均與占 GDP 比兩個錨點改用替代分母。(5) 所有法規結論都需專業人士最終確認。 |

---

## 1. 摘要

1. **室內裝修市場第一次有了業界口徑**：依 IPO 招股書引用的 Smith Zanders 研究，「室內裝修服務＋安裝工程＋專業建築活動」完成工程值從 2019 年 RM25 億增加到 **2024 年 RM48 億**（約 11.2 億 USD／349 億 TWD）。這是住宅與商業的混合口徑〔MY-D04、MY-D05〕【實際（IMR 口徑），中】。
2. **需求以中古屋為主**：2025 年住宅交易中，中古屋占 **84.5%**〔MY-06〕。住宅存量 **620 萬單位**（2023），其中排屋（terrace）占 41.3%〔MY-D27〕【實際，中／高】。
3. **「室內設計師」是法定登記頭銜，但人數極少**：依 LAM 登記資料，室內設計師 **606 人**，室內設計執業體 72 家（2021-08）〔MY-D22〕；另有一說只有 165 人〔MY-60〕（見矛盾表）【實際，中】。
4. **施工端高度分散**：CIDB 最高等級 G7 的本地承包商中，登記 B07（室內裝飾）類別的有 **907 家**（2025-12-01）〔MY-D14 群〕。業界龍頭 Signature Alliance 自稱市占約 **8.1%**〔MY-D04〕【實際（公司說法），低中】。
5. **信任赤字很大**：CIDB 在 2018–2025 年共接獲 **3,201 宗**房屋建造與裝修承包商投訴〔MY-D43〕。消費者索償仲裁庭（TTPM）求償上限 RM50,000（約 11,680 USD）〔MY-49〕【實際，中】。
6. **外資門檻決定進入模式**：CIDB 規定「本地承包商」本地股權須 **≥70%**〔MY-65、MY-66〕；室內設計顧問執業體的董事須全部是 LAM 登記室內設計師〔MY-32〕。因此台資 100% 持股設立設計或施工公司，實務上不可行（需專業人士最終確認）。
7. **成本溫和上升、缺工持續**：2026 年 7 月鋼筋年增 0.5–8.4%、OPC 水泥年增 0.9–7.5%，每包 **RM25.70**〔MY-D75〕。熟練印尼籍工人日薪 RM120–160（2025）〔MY-D64〕。營建業外勞稅每年 RM1,850（半島）〔MY-D62〕【實際，中】。
8. **新零售者擴張，平台退場傳聞未證實**：宜得利（Nitori）2026-03-31 在馬有 **14 家店**，計畫增至 21 家〔MY-D31〕；HomePro 在馬 7 家（2025 年底）〔MY-D34〕。「Livspace 退出馬來西亞」**沒有任何來源證實**〔MY-D17、MY-D18〕【實際，中】。

---

## 2. 十節正文

### 2.1 市場規模與成長

**結論**：馬來西亞**沒有官方的住宅翻修或室內設計服務市場規模**。本輪新增的最佳口徑是 IPO 招股書引用的 Smith Zanders 數字：2024 年 RM48 億，為「室內裝修服務＋安裝工程＋專業建築活動」的完成工程值，住宅與商業混合。廣義「家居改善」（含產品）為 RM477 億（2024）。兩者相差 10 倍，屬定義差異，不可平均。住宅與商業、新屋與存量的拆分：**無資料**。

| 來源# | 數值（原幣／USD／TWD） | 年份 | 原始定義 | 歸桶 | 現況／預測 | 標示 | 信心 |
|---|---|---|---|---|---|---|---|
| MY-D04、MY-D05 | RM48 億（11.2 億 USD／349 億 TWD）；2019 年為 RM25 億（年化約 13.9%，本報告計算） | 2024 | Smith Zanders（SAG 招股書 IMR）：室內裝修服務、安裝工程與專業建築活動的完成工程值，合併口徑 | 商業裝修＋住宅翻修（混合） | 現況 | 【實際】 | 中 |
| MY-D04、MY-D05 | 單獨的室內裝修（interior fit-out）RM12 億（2.8 億 USD／87 億 TWD）；2020 年 RM7.911 億 | 2023 | 同一報告的 fit-out 單獨口徑 | 商業＋住宅 fit-out | 現況 | 【實際】 | 中低（數字與 URL 對應不確定） |
| MY-D10、MY-D13、MY-D14 群 | 2024 年 RM48 億；2024–2027 年 CAGR 10.5%；2027 年 RM27 億 | 2024／2027 | 南洋商報引「獨立市場研究」；RM27 億與 RM48 億口徑不同，報導未說明 | 混合 | 現況＋預測 | 【示意】 | 低 |
| MY-D12 | 室內裝修行業 RM44.3 億（10.3 億 USD／323 億 TWD）；2029 年 RM56.5 億 | 2024／2029 | 南洋地產引述；定義未說明 | 混合 | 現況＋預測 | 【示意】 | 低（對應不確定） |
| MY-D01、MY-D11 | 家居改善 RM477 億（111.4 億 USD／3,473 億 TWD）；2029 年 RM592 億（年化約 4.4%，本報告計算） | 2024／2029 | Topmix 執行長與南洋地產引述的市場報告；含產品，屬廣義口徑 | 家居零售＋住宅翻修（混合） | 現況＋預測 | 【示意】 | 中低（兩源一致，可能同一出處） |
| MY-D02 | home improvement 10 億 USD（約 RM42.8 億／312 億 TWD）；至 2032 年 CAGR 7.0% | 2025 | Ken Research；含產品與服務 | 混合 | 估計＋預測 | 【示意】 | 低 |
| MY-D03 | 營建市場中新建工程占 75.4%；翻修工程至 2031 年 CAGR 8.10% | 2025 | Mordor Intelligence；全營建業口徑 | 其他 | 估計＋預測 | 【示意】 | 低 |
| MY-16～19 | 專業工程完成值四季合計約 RM214 億（50.0 億 USD／1,558 億 TWD） | 2025 | DOSM 季度營建統計。依 AES 2022 指南，「專業工程」含建築完工與裝修（building completion and finishing）等 8 類〔MY-D90〕 | 上限型代理 | 現況 | 【示意】（四季加總） | 中 |
| MY-26／27 | 家具＋室內設計 24.3 億／54.2 億 USD（兩個版本） | 2025 | Ken Research | 混合 | 估計 | 【示意】 | 低 |
| MY-28、MY-29 | 家飾 32.87 億 USD（IMARC）／8.459 億 USD（Statista） | 2024 | 市調區隔 | 家居零售 | 估計 | 【示意】 | 低 |
| MY-95 | Signature International 室內裝修工程分部 RM4.784 億（1.12 億 USD／34.8 億 TWD），年增 23.4% | FY2025 | 上市公司分部營收 | 公司層級 | 現況 | 【實際】 | 中 |

**合理性檢查（全部為【示意】）**
- RM48 億 ÷ 2025 年住宅交易 256,512 筆〔MY-06〕≈ 每筆 RM18,700。這遠低於 800 sq ft 公寓中階翻修 RM56,000–120,000〔MY-21〕，因此 RM48 億不可能涵蓋全部住宅翻修。研判它主要是有組織承包商的 B2B／商業 fit-out（推論）。
- RM477 億 ÷ 256,512 筆 ≈ 每筆 RM186,000，已接近一般住宅裝修預算上限 RM200,000〔MY-24〕。這個數字含產品零售、維修與全部存量住宅，是上限值。
- Signature International 的 fit-out 營收 RM4.784 億約等於 RM48 億的 10%，與子公司 SAG 自稱的 8.1% 市占量級一致。
- **結論**：住宅翻修的實際規模應介於 RM48 億與 RM477 億之間。本報告不取中值。

**預測（與現況分開，全部【示意】、低信心）**：2027 年 RM27 億（南洋，口徑不明）；2029 年 RM56.5 億〔MY-D12〕；2029 年家居改善 RM592 億〔MY-D01、MY-D11〕；home improvement 至 2032 年 CAGR 7.0%〔MY-D02〕；翻修工程至 2031 年 CAGR 8.10%〔MY-D03〕；家具＋室內設計 2032 年 39.79 億 USD〔MY-26〕。

### 2.2 需求結構

**結論**：交易端以中古屋為主（84.5%），存量 620 萬單位。建商已完工未售的庫存在 2026 年第 1 季升到 32,800 單位。30 年以上屋齡占比**無資料**。公寓全屋裝修的工期，施工本身約 6–10 週，計入延誤後常見 3–6 個月（低信心）。

| 指標 | 數值 | 年份 | 來源# | 定義 | 標示 | 信心 |
|---|---|---|---|---|---|---|
| 住宅交易 | 256,512 筆（−1.5%）／RM1,082.7 億（253 億 USD／7,882 億 TWD） | 2025 | MY-06 | NAPIC 住宅次產業（二手轉述） | 【實際】 | 中 |
| 中古屋占住宅交易 | 84.5%（2024 年 83.0%） | 2025 | MY-06、MY-105 | NAPIC secondary market | 【實際】 | 中／高 |
| 住宅存量 | 620 萬單位（2022 年 608 萬，+2.0%）；排屋占 41.3% | 2023 | MY-D27 | DOSM 引 NAPIC existing stock | 【實際】 | 高 |
| 30 年以上屋齡占比 | **無資料**。《都市更新法案》以 30 年為同意門檻分界〔MY-127〕，2026-01 內閣同意撤回再修〔MY-126〕 | — | — | — | — | — |
| 已完工未售住宅 | 30,471 單位／RM177.3 億 | 2025 | MY-09、MY-10 | NAPIC overhang | 【實際】 | 高／中 |
| 同上（上半年） | 26,911 單位／RM186 億（+16.3%） | 1H2025 | MY-D30 | 同上 | 【實際】 | 中（對應不確定） |
| 同上（最新） | 32,800 單位／RM163 億（38.1 億 USD） | 2026Q1 | MY-D28 | KPKT 國會答詢引 NAPIC | 【實際】 | 中 |
| 未售分州 | 霹靂 3,943（12.9%）、柔佛 3,705（12.1%）、雪蘭莪 3,547（11.6%） | 2025 | MY-D29 | NAPIC 2025 | 【實際】 | 中 |
| 新推案 | 64,487 單位（−14.9%）；1H2025 為 23,380 單位（−46%） | 2025 | MY-06、MY-D30 | 開發商新推出單位 | 【實際】 | 中 |
| 平均房價 | RM502,922（11.7 萬 USD／366 萬 TWD） | 2025 暫定 | MY-06 | MHPI 平均價 | 【實際】 | 中 |

**住宅裝修單價（Loanstreet 全屋均攤，MY-21，2025，【示意】，中）**

| 等級 | RM／sq ft | RM／m² | USD／m² | TWD／坪 |
|---|---|---|---|---|
| 基本（油漆、小修） | 20–60 | 215–646 | 50–151 | 5,181–15,543 |
| 中階（廚衛升級、鋪磚） | 70–150 | 754–1,615 | 176–377 | 18,134–38,859 |
| 高階（拆牆、結構、高檔飾面） | 160–300+ | 1,722–3,229+ | 402–754+ | 41,449–77,717+ |

**每案均價（【示意】，低）**：公寓標準翻修 RM25,000–45,000、全面翻修 RM50,000–80,000（巴生谷與新山，2026）〔MY-23〕；ID 公司全包的公寓約 RM150,000，排屋 RM220,000 起，半獨立式約 RM300,000，獨立洋房約 RM400,000（年份未標示）〔MY-22〕；800 sq ft 中階 RM56,000–120,000（1.31–2.80 萬 USD），約為平均房價的 11–24%〔MY-21、MY-06〕。

**設計費（2026，設計公司指南群 MY-83～91，【示意】，中）**：全包設計約占工程費 8–15%（成熟工作室 8–12%）。純設計每 sq ft RM3–10，換算每 m² RM32–108（7.5–25.1 USD）。包價 RM15,000–80,000。以 1,200 sq ft 公寓試算，純設計費 RM3,600–12,000（841–2,803 USD／2.6–8.7 萬 TWD）。

**工期（本輪新增，全部為業者或平台指南，【示意】，低）**

| 情境 | 工期 | 來源# |
|---|---|---|
| 公寓全屋標準翻修 | 6–10 週，另加 2–4 週緩衝；其中管理處核准 1–2 週 | MY-23、MY-D87～D89 群 |
| 依等級（公寓） | 基本 2–4 週（RM30,000–50,000）；中階 6–10 週（RM50,000–100,000）；高階 10–16 週（RM100,000–200,000+） | 同上 |
| 計入延誤（工班排程、磁磚到貨、追加工程） | 常見 3–6 個月 | MY-D89 群 |
| 公寓附則限制 | 多數公寓限制裝修期 1–3 個月；打鑿、鑽孔等噪音工程限平日上班時段 | MY-123 |
| 中國籍業者 | 約 2 個月，甚至 30 天完工（業界提醒可能流程不規範） | MY-81（2025） |
| 排屋／有地住宅 | **無資料**（結構變更須另申請 PBT 許可，時間另計） | — |

翻修週期：**無資料**。預算超支常見 30–50%〔MY-24，低〕。

### 2.3 產業結構與主要玩家

**結論**：設計端是「法定登記的小圈子」：LAM 登記室內設計師約 606 人、執業體 72 家（2021）。施工端是「大量分散的承包商」：G7 等級中 B07 類別就有 907 家。2025–2026 年出現**室內裝修業者 IPO 潮**（SAG 上市；Adnex、EGH 擬上市），資本開始集中。零售端則由 MR DIY、IKEA 主導，日系 Nitori 快速展店。

**家數**

| 指標 | 數值 | 年份 | 來源# | 定義 | 標示 | 信心 |
|---|---|---|---|---|---|---|
| LAM 全部登記人員 | 6,171 人 | 2022-12 | MY-D20 | 含建築師、見習、室內設計師、繪圖員等全部類別 | 【實際】 | 中 |
| LAM 登記建築與室內設計顧問事務所 | 1,891 家 → 1,981 家 | 2022 → 約 2024 | MY-D20、MY-D21 | 國會文件（LAM 年報） | 【實際】 | 中 |
| LAM 登記室內設計師 | 606 人；ID 法人 26、合夥 2、獨資 44（執業體合計 72） | 2021-08 | MY-D22 | MIID 供稿文章引 LAM | 【實際】 | 中 |
| 同上（另一說） | 165 人 | 約 2024 | MY-60 | Bernama；定義未明 | 【實際】 | 低（與上列矛盾） |
| G7 本地承包商中登記 B07（室內裝飾）者 | 907 家 | 2025-12-01 | MY-D14 群 | 華文財經報導引招股資料 | 【實際】 | 低中（對應不確定） |
| 集中度 | Signature Alliance 自稱市占約 8.1% | 2025-05 | MY-D04 | 執行長說法，非獨立來源 | 【示意】 | 低 |

**主要玩家**

| 業者 | 類型 | 關鍵數字 | 年份 | 來源# | 信心 |
|---|---|---|---|---|---|
| Signature Alliance Group（SAG，胜利者联盟） | 設計施工一體、fit-out（Signature International 子公司） | 2025-06-05 在 ACE 市場上市；發行 2.6 億股、每股 RM0.62、募資 RM1.61 億、上市市值約 RM6.2 億（1.45 億 USD）；認購 1.12 倍。2026-03 底有 87 個在建案、未入帳訂單 RM2.276 億 | 2025–2026 | MY-D06～D09、MY-D16 | 中 |
| Signature International Berhad | 廚櫃／衣櫃系統＋fit-out | FY2025 營收 RM9.674 億，fit-out RM4.784 億（+23.4%），在手訂單 RM12.8 億 | 2025 | MY-95 | 中 |
| Adnex 集團、EGH 國際 | 室內裝修服務／工程商 | 分別於 2025-07、2026-01 傳出擬上市 ACE（創業板） | 2025–2026 | MY-D13、MY-D14 | 中（僅標題與摘要） |
| 產業概況 | — | 南洋商報專題：「疫後迎來黃金爆發期，室內裝修業者排隊上市」 | 2025-10 | MY-D10 | 中 |
| MR DIY | 居家修繕零售 | 1,528 家店（2025-09-30）；營收約 RM50 億 | 2025 | MY-93、MY-94 | 中 |
| IKEA（Ikano 經營） | 家居零售 | FY2024 營業額 RM14.6 億；4 家大型店；FY2025 新開 8 家快閃店 | 2024–2025 | MY-98、MY-99 | 中 |
| 宜得利（Nitori） | 日系家居零售 | 11 家（2024-10）→ 14 家（2026-03-31），計畫 2027-03 前增至 21 家（約 +27%，本報告計算）；2022-12 在新山 Mid Valley Southkey 開設馬國最大店 | 2022–2026 | MY-D31、MY-D32、MY-D33 | 中 |
| HomePro Malaysia | 泰系居家修繕零售 | 7 家（2025 年底；2025Q2 無新店）；早年目標 8–10 年內開 40 家 | 2025 | MY-D34；MY-D35（對應不確定） | 中／低 |
| Courts | 家電家具 | 46 家（2025-02） | 2025 | MY-102 | 中 |
| Livspace | 印度系設計平台 | 「退出馬國」**未獲證實**：一份 profile 仍列新加坡與馬來西亞為服務市場（未標日期），另有報導指其在印度、東南亞、中東營運並裁員逾 1,000 人 | 2025–2026 | MY-D17、MY-D18、MY-D19 | 中（「退出」屬無資料） |
| 中國籍設計／裝修公司 | 低價進入者 | 報價為本地 40–50% | 2025 | MY-81 | 中 |

2023–2026 年的併購、募資與倒閉：IPO（SAG）與擬上市（Adnex、EGH）如上；Recommend.my 募資見 2.4 節；倒閉潮的統計：**無資料**（僅有個案，如老闆失蹤、訂金蒸發〔MY-D46〕）。

### 2.4 通路與獲客

**結論**：獲客分四路：平台、展會、零售，以及熟人／社群；其中熟人／社群風險最高。2026 年監管方（LAM 1/2026、CIDB「Jom Bina Sempurna」）開始把「查核登記」推向平台與消費者，**合規將成為通路門檻**（推論）。

| 通路 | 數字與事實 | 年份 | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|
| Qanvast（新加坡起家） | 2016 年進入馬國；屋主免費使用；Trust Programme 保障訂金，上限 RM50,000；累計逾 10 萬屋主使用（地區未拆分） | 2016／約 2021 | MY-D79、MY-D80 | 【實際】 | 中／低 |
| Recommend.my | A 輪 400 萬 USD（約 RM1,600 萬），Morning Crest Capital 領投；印尼品牌 Sejasa.com；MDV 提供 RM400 萬定期貸款 | 年份不明／2021 | MY-D81、MY-D82 | 【實際】 | 中（Craft.co 稱總募資 100 萬 USD〔MY-D83〕，矛盾） |
| Atap.co | **無資料**（搜尋無結果） | — | — | — | — |
| 房產入口網 | PropertyGuru、iProperty 以 ID 名單與交屋瑕疵（DLP）指南導流 | — | MY-54、MY-114 | — | 低 |
| 展會 ARCHIDEX | 2025 年參觀 50,668 人次、參展商 850 家以上、36,700 m²（主辦方自報；MITEC＋KLCC 雙場館；PAM 與 C.I.S Network 合辦）。2024 年 40,336 人次、商機 RM11.5 億（2.69 億 USD／83.7 億 TWD） | 2024–2025 | MY-D84、MY-D85、MY-D86 | 【實際】 | 中 |
| 熟人／社群 | 馬六甲 12 名苦主經「口傳口」介紹，被承包商捲走逾 RM23 萬；多數受害屋主經熟人或 Facebook 找到未登記承包商 | 2024／不明 | MY-D50、MY-47 | 【實際】 | 中／低 |
| 監管導流 | LAM《一般通告 1/2026》要求平台在刊登前查核登記；MIID 呼籲到 LAM 網站查名；CIDB 推「Jom Bina Sempurna」 | 2026 | MY-59、MY-D23、MY-D43、MY-D51 | 【實際】 | 中 |
| 零售導流 | IKEA 快閃店、MR DIY 每年新開 150–190 家、Nitori 展店 | 2025–2026 | MY-99、MY-92、MY-D31 | 【實際】 | 中 |

平台 GMV、抽成、滲透率：**無資料**。

### 2.5 法規與證照（需專業人士最終確認）

**結論**：設計與施工分屬兩套法定登記：設計歸 LAM（Act 117），施工歸 CIDB（Act 520）。住宅裝修另受三層規範：地方政府許可（DBKL、MBPJ、MBJB）、分層管理附則（by-law 27），以及變更用途時的消防（JBPM）。MIID 只是協會，不發執照。

| 項目 | 法規／機關（原文） | 內容 | 來源# | 信心 |
|---|---|---|---|---|
| 室內設計師登記 | Architects Act 1967（Act 117）；Lembaga Arkitek Malaysia（LAM） | 2007 年修法新增「Interior Designer」；只有登記者可提供室內設計顧問服務；第 7A 條罰款調高（金額無資料） | MY-30、MY-58、MY-61 | 高 |
| 執業體 | Act 117 第 27E(1) 條 | 獨資者、全部合夥人或董事會須為登記室內設計師 | MY-32 | 高（存在）／中（細節） |
| 持續進修 | LAM 通告 | 室內設計師與見習室內設計師須符合 CPD 要求 | MY-D26 | 中 |
| 平台查核 | LAM General Circular No. 1/2026 | 平台刊登前須查核登記狀態 | MY-59 | 中 |
| 協會 | Malaysian Institute of Interior Designers（MIID） | 協會會員名冊與 LAM 登記是兩回事；會長由 Norshafina Ibrahim 擔任（資料未標日期；2020–2021 年為 Lai Siew Hong） | MY-D22～D24、MY-37 | 中低 |
| 承包商 | Lembaga Pembangunan Industri Pembinaan Malaysia（CIDB）；Act 520 | G1–G7 分級（G1 承攬上限 RM20 萬；G7 無上限；第三方彙整）；B07 室內裝飾專業類別 | MY-38～42、MY-D14 群 | 中 |
| 吉隆坡小型工程 | Garis Panduan Permit Kerja Kecil WPKL（2021）；DBKL | 小型工程許可；2026-08 起換磁磚、天花板等只需填表通知 | MY-43～45 | 高／中 |
| 八打靈再也 | Majlis Bandaraya Petaling Jaya（MBPJ）；Akta 133、Akta Pengurusan Strata 2013 | 改建或加建既有建物，須事先取得地方政府書面核准；MBPJ 對未核准改建採取執法 | MY-D58 | 中 |
| 新山小型工程 | Majlis Bandaraya Johor Bahru（MBJB）小型工程指引 | 已取得入住證（Sijil Kelayakan Menduduki）的住宅，小型工程許可效期通常 1 年 | MY-D59 | 中 |
| 建築規範 | UBBL 1984 | 加隔間牆、雨遮、坡道等小型改造一般須 PBT 核准；未核准可罰款或令拆除 | MY-46 | 中 |
| 分層住宅 | Strata Management (Maintenance and Management) Regulations 2015 第三附表 | by-law 27(1)：事先取得管理法團（MC）書面核准，必要時另需主管機關核准；核准後可收押金；暗管與電線管 300 mm 內禁止打鑿鑽孔；by-law 7(1)：罰款由大會議定；17(1)：MC 可拒絕承包商進入；16(3)：業主自費修復公共區域損害 | MY-D60、MY-D61（律師／業界評論，非憲報原文） | 中 |
| 押金慣例 | JMB／MC 附則 | 多數社區收 RM2,000–5,000（467–1,168 USD） | MY-123 | 低 |
| 消防 | Jabatan Bomba dan Penyelamat Malaysia（JBPM）；Akta Perkhidmatan Bomba 1988 | 店屋改作宿舍等變更用途的裝修，須取得 JBPM 與地方政府圖則核准；違規逐項發通知，逾期未改可起訴（新山一次對 11 處發出 45 張通知）；持消防證書（Fire Certificate）的處所每年換證，並須申報結構或圖面變更 | MY-D54～D57 | 中 |
| 消防（商業 fit-out） | — | 標準送審流程與規費：**無資料** | — | — |

**2023–2026 年變動**：CIDB 外國承包商新制（2023）；最低工資 RM1,700（2025）；就業准證新門檻（2026-06-01）；外勞多層級徵收機制（MTLM，2026）；LAM 1/2026；DBKL 簡化（2026-08）；《都市更新法案》撤回再修（2026-01）。

### 2.6 消費者保護與糾紛

**結論**：裝修是消費糾紛高發領域：CIDB 7 年接獲 3,201 宗投訴；檳城 TTPM 的服務類索償以裝修居首。主要救濟管道是 TTPM（上限 RM50,000，立案費 RM5）。典型風險是**高比例預付後停工**。裝修工程沒有法定瑕疵責任期的證據，合約範本與訂金慣例：**無資料**。

| 項目 | 內容 | 年份 | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|
| TTPM | 上限 RM50,000（11,680 USD／36.4 萬 TWD，2019-10-01 起）；立案費 RM5；3 年內提出；通常不得由律師代理 | 2019 起 | MY-49、MY-50、MY-52、MY-119 | 【實際】 | 高／中 |
| CIDB 投訴 | 房屋建造與裝修承包商投訴 3,201 宗；工程部提出 4 項策略打擊承包商詐騙 | 2018–2025 | MY-D43 | 【實際】 | 中 |
| 國會議員轉述 | 約 30 宗裝修詐騙投訴，損失數百萬令吉 | 不明 | MY-D52 | 【實際】 | 低 |
| 檳城 TTPM | 至 9 月 10 日，住家裝修服務索償 68 件，為服務類最高 | 年份不明 | MY-48 | 【實際】 | 低 |
| 判決個案 | 新山屋主付 RM36,750，TTPM 判賠 RM15,000、分兩期；櫥櫃突加價 RM1 萬，判兩週內退 RM1,500；[2021] MLJU 1365 判退 RM22,375 | 2024／2021 | MY-D48、MY-D49、MY-113 | 【實際】 | 中 |
| 詐騙型態 | 預付最高 80% 後停工，每戶 RM10–40 萬（承諾 3 個月完工，進度不到 50%）；雪州 12 名屋主損失逾 RM30 萬；同一人開 3 家公司，18 名屋主付 RM181 萬後爛尾；設計師收近 RM15 萬未開工；警方有時視為商業糾紛，不構成詐騙 | 2022–2025 | MY-D44、MY-D47、MY-D92、MY-D45 | 【實際】 | 中 |
| 國貿局觀察 | 馬六甲國內貿易局：許多屋主沒查證承包商是否合法，也沒簽書面合約 | 2024 | MY-D50 | 【實際】 | 中 |
| 保固 | 裝修工程沒有法定瑕疵期的證據；向建商買的新屋有 24 個月 DLP | — | MY-114、MY-118 | — | 中 |
| 市場型保障 | Qanvast Trust 訂金保障上限 RM50,000 | — | MY-D79 | 【實際】 | 中 |
| 合約範本、訂金比例、履約保證 | **無資料**；CIDB 宣導先查登記、簽約、監督進度、依進度付款 | 2026 | MY-D43、MY-D51 | — | — |
| KPDN 全國裝修投訴統計 | **無資料**；KPDN 典藏有個別 TTPM 裁決紀錄 | 2024–2025 | MY-D53 | — | — |

### 2.7 外資／台資進入規則（需專業人士最終確認）

**結論**：設計公司與裝修承包商**都不能由台資 100% 持股**（前者受 LAM 董事資格限制，後者受 CIDB 70% 本地股權限制）。可行路徑是：與 LAM 登記設計師合作、在本地承包商中少數持股（≤30%），或以外國承包商身分個案登記。外派人員須達就業准證（EP）第 II 類以上門檻（RM10,000／月）。柔新經濟特區（JS-SEZ）帶來新山辦公 fit-out 機會，但規模**無資料**。

| 項目 | 內容 | 來源# | 信心 |
|---|---|---|---|
| 設計顧問公司 | 執業體董事會須全部由 LAM 登記室內設計師組成 → 外資 100% 持股的設計顧問公司，若董事不是登記者即不符資格（推論）。外籍人士能否登記為 LAM 室內設計師：**無資料**。登記路徑要求至少 1 年在馬國 LAM 登記事務所實習 | MY-32、MY-35 | 中 |
| 裝修承包商 | 本地承包商須本地股權 ≥70%，外資 >30% 歸類為外國承包商；東協來源股權可到 51%；JV 中外國承包商股權 ≤30%；2023 年起外國承包商可在得標前先登記，首次效期 2 年 | MY-65、MY-66、MY-68、MY-63 | 中 |
| 家居零售外資規則 | **無資料**（本輪未搜尋） | — | — |
| 就業准證（2026-06-01 起） | 第 I 類月基本薪 ≥RM20,000（4,672 USD／14.6 萬 TWD）；第 II 類 RM10,000–19,999（2,336 USD 起）；第 III 類 RM5,000–9,999（1,168 USD 起）。2025 年舊制：第 I 類 ≥RM10,000、第 II 類 RM5,000–9,999、第 III 類 RM3,000–4,999 | MY-69～72 | 高 |
| 外勞稅 | 營建業每年 RM1,850（半島，432 USD／13,469 TWD）、RM1,010（沙巴／砂拉越）；頁面未標更新日期 | MY-D62 | 中 |
| 外勞政策 | MTLM 2026 年實施，營建業分層費率：**無資料**；新外勞引進自 2024-05 起凍結，業者轉向 IBS 與 BIM | MY-73～80、MY-D63（對應不確定） | 中 |
| 稅務 | **無資料**（未搜尋） | — | — |
| 已進入的外商 | Qanvast（新加坡，2016）；Nitori（日本，14 家）；HomePro（泰國，7 家）；IKEA（Ikano）；中國籍裝修公司；Livspace（現況未證實） | MY-D79、MY-D31、MY-D34、MY-98、MY-81、MY-D18 | 中 |
| 台資設計公司案例 | **無資料** | — | — |

**JS-SEZ 對柔佛裝修／fit-out 需求（本輪新增，直接證據不足）**

| 指標 | 內容 | 年份 | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|
| 特區範圍 | 柔佛南部 3,505 km²；重點為製造、高科技、綠能、資料中心 | 2025 | MY-D38 | 【實際】 | 中 |
| 新投資 | 柔佛 2025Q1 新投資約 RM274 億（64 億 USD）；RTS Link 預計 2026-12 通車 | 2025 | MY-D37 | 【實際】 | 中 |
| 辦公市場 | 新山特建辦公租金指數 2024 年只成長 0.1%，市場偏向租戶；舊 CBD 空置率高；Medini、Nusajaya 現代辦公需求上升 | 2024–2025 | MY-D36 | 【實際】 | 中 |
| 入駐率與租金 | 私有特建辦公平均入駐率約 57.5%；新樓每 sq ft RM3–3.5、舊樓 RM2–3（月租） | 2025 前後 | MY-D39 | 【實際】 | 中低 |
| 政策意圖 | 交通部長表示要吸引新加坡中小企業到新山設辦公室 | 2023 | MY-D40 | 【實際】 | 中 |
| 摩擦 | 長堤每日塞車；技術人員薪資可能需接近新加坡水準 | 2025 | MY-D91 | 【實際】 | 中 |
| 住宅 | 柔佛 2025 年住宅交易 42,566 筆（全國第二）；未售 3,705 單位 | 2025 | MY-06、MY-D29 | 【實際】 | 中 |
| fit-out 規模／單價 | **無資料** | — | — | — | — |

推論：JS-SEZ 的裝修需求主要會來自三類案源：新遷入中小企業的辦公室、共享辦公空間，以及為留住租戶而升級的舊辦公樓。但入駐率只有 57.5%，需求是「結構性、分段式」，不會一次爆發（【示意】）。

### 2.8 消費者行為

**結論**：裝修主力是中古屋買家與排屋自住者。主流預算 RM5–20 萬，價格敏感，中國業者以 40–50% 價格切入。決策高度依賴熟人與社群，但這也是糾紛來源。付款習慣上常見高比例預付。翻修融資與補助：**無資料**。

| 面向 | 內容 | 年份 | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|
| 誰在裝修 | 中古屋買家為主（84.5%）；存量中排屋占 41.3% | 2023–2025 | MY-06、MY-D27 | 【示意】推論 | 中 |
| 預算分級 | 一般住宅 RM50,000–200,000（1.17–4.67 萬 USD）；公寓基本 RM30,000–50,000、中階 RM50,000–100,000、高階 RM100,000–200,000+ | 2026 | MY-24、MY-D87～D89 群 | 【示意】 | 低 |
| 決策歷程 | 熟人、Facebook 介紹常見；建議至少 3 份明細報價；查 LAM／CIDB 登記 | — | MY-47、MY-24、MY-D23 | 【實際】 | 低中 |
| 付款階段 | 個案顯示預付 80% 後停工；CIDB 建議依進度付款；慣例比例：**無資料** | 2024、2026 | MY-D44、MY-D43 | 【實際】 | 中 |
| 價格敏感 | 中國業者報價為本地 40–50%、最快 30 天完工 | 2025 | MY-81 | 【實際】 | 中 |
| 高齡需求 | 南洋地產有「室內設計關懷年長者需求」專題（僅標題） | — | MY-D12 | — | 低 |
| 風格 | **無資料** | — | — | — | — |
| 融資與補助 | **無資料**（EPF 提領、銀行翻修貸款本輪未搜尋） | — | — | — | — |

### 2.9 人才與工班

**結論**：設計師供給的瓶頸在「登記」而不在人：一般室內設計師月薪約 RM3,761，但 LAM 登記者只有數百人。工班的瓶頸在熟練泥作與砌磚工：本地人老化、不願入行，印尼籍熟練工人減少，新外勞引進凍結。熟練工日薪 RM120–160，有時到 RM180。

| 項目 | 內容 | 年份 | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|
| 室內設計師月薪 | 全國平均 RM3,761（878 USD／27,381 TWD；1,600 筆回報）；吉隆坡 RM4,255；初級 RM2,912 | 2026-05 資料 | MY-D69 | 【實際】（平台自報） | 中 |
| 同上（另一平台） | 吉隆坡 RM4,500；資深吉隆坡 RM7,500（1,752 USD） | 2025–2026 | MY-D70、MY-D71 | 【實際】（平台自報） | 低中 |
| 監工薪資 | **無資料** | — | — | — | — |
| 設計科系畢業人數 | **無資料** | — | — | — | — |
| 印尼籍工人日薪 | 一般 RM100（23 USD／728 TWD）；較熟練 RM120；熟練維修 RM150–160；繁重工作有人要求 RM180（42 USD／1,310 TWD） | 2025 | MY-D64 | 【實際】 | 中 |
| 營建業日薪 | 約 RM120 | 2023 研究 | MY-108 | 【實際】 | 低 |
| 柔佛抹灰工 | 本地熟練 RM120.50、外勞熟練 RM109 | 2023 | MY-110 | 【實際】 | 低 |
| 缺工型態 | 外勞總數已足，缺的是熟練砌磚與泥作工；熟練工多為印尼籍，很多人轉為自行承包 | 2024 | MY-D65 | 【實際】 | 中 |
| 缺工規模 | 每家承包商平均缺工 30%；一般裝修業者需 8–10 名工人 | 2022 | MY-D66 | 【實際】 | 低中 |
| 最低工資 | RM1,700／月（397 USD／12,377 TWD），2025-02-01 起；員工少於 5 人的雇主自 2025-08-01 起，並涵蓋外勞；以每週 6 天計，約合日薪 RM65.38（本報告計算） | 2025 | MY-D67、MY-D68、MY-111 | 【實際】／【示意】 | 中 |
| 外勞稅／凍結 | 營建業每年 RM1,850；新引進自 2024-05 起凍結；2027 年預算若調升最低工資，勞力密集的固定價工程最受衝擊 | 2024–2026 | MY-D62、MY-D63、MY-79 | 【實際】 | 中 |

### 2.10 材料供應鏈與價格

**結論**：2022 年鋼材急漲（年增約 16–20%），2023–2025 年回落並趨穩。2026 年再溫和上升：7 月鋼筋年增 0.5–8.4%、水泥年增 0.9–7.5%，砂價單月急漲近 15%。2022–2026 年累計：鋼筋均價約 −10%，水泥自 2025 年 12 月起約 +4.7%（皆【示意】）。在地品牌與進口依賴：**無資料**。

| 時點 | 指標 | 數值 | 來源# | 標示 | 信心 |
|---|---|---|---|---|---|
| 2022-05 | 單價指數年增 | 鋼材 +19.9%、鋼構與金屬 +18.1%、水泥 +12.4% | MY-D72～D74 群 | 【實際】 | 中（對應不確定） |
| 2022-06 | 鋼筋（besi bar＋mycon）均價 | RM3,897.11／公噸（2021-06 為 RM3,362，+15.9%） | 同上 | 【實際】 | 中 |
| 2023-02 | 月增 | 水泥 +1.9%、鋼材 +1.5%；5–6 月鋼材隨國際價格下跌 | 同上 | 【實際】 | 中 |
| 2024-05 | 水泥年增 | 多數地區 +0.4–3.0% | 同上 | 【實際】 | 中 |
| 2025-02 | 年增 | 鋼材 −3.0～−15.3%；水泥 +0.2–4.0% | MY-121 | 【實際】 | 高 |
| 2025-12 | 均價 | OPC RM24.55／50 kg；鋼筋 RM3,512.10／公噸；水泥年增 +2.0–6.1% | MY-120 | 【實際】 | 高 |
| 2026-04 | 均價 | 鋼筋 RM3,504.20（月增 +2.3%）；水泥 RM25.90（+1.3%） | MY-D78 | 【實際】 | 中（對應不確定） |
| 2026-07 | 年增與均價 | 鋼材 +0.5–8.4%、水泥 +0.9–7.5%（霹靂最高）；鋼筋 RM3,499.50（817 USD／25,477 TWD）；OPC RM25.70（6.0 USD）；砂價急漲近 15% | MY-D75、MY-D76 | 【實際】 | 中 |
| 2026-08 | 建築成本指數（含鋼筋） | 半島月減 0.1–1.1%；沙巴、砂拉越上升 | MY-D77 | 【實際】 | 中 |
| 累計 | 鋼筋 2022-06 → 2026-07 | −10.2%（兩序列產品組合可能不同） | 本報告計算 | 【示意】 | 低 |
| 地區差 | 東馬材料運費使造價高 10–20% | 2026 | MY-23 | 【示意】 | 低 |
| 在地品牌 | 系統櫃 Signature、Corten（FY2025 營收 RM2.114 億、RM2.775 億）；磁磚、衛浴、塗料品牌：**無資料** | 2025 | MY-95 | 【實際】 | 中 |
| CIDB 官方指數序列、進口依賴、關稅與標準 | **無資料**（CIDB CONVINCE 價格未標日期） | — | MY-122 | — | — |

---

## 3. 對台灣業者（璞石）的啟示

1. **進入結構採「三層分離＋少數持股」，不要設 100% 子公司（需律師最終確認）。**
   - **設計層**：由馬國 LAM 登記室內設計師擔任董事，組成本地 ID 執業體〔MY-32〕。璞石不擔任執業體股東或董事，改以「設計系統授權＋技術服務合約」參與（如 3D 視覺、選材庫、標準圖庫、品牌）。這類服務是否構成 Act 117 所稱的「室內設計顧問」，必須先確認。
   - **施工層**：與本地 CIDB 登記承包商合資，璞石持股 ≤30%、本地 ≥70%〔MY-65、MY-66〕。住宅案多落在 G1（RM20 萬以下），應選擇已登記 B07 類別的夥伴。商業大案可另以外國承包商個案登記（首次效期 2 年），與本地 G7 業者組 JV〔MY-66、MY-68〕。
   - **零售層**：系統櫃與家具以供貨或品牌授權方式，進入 HomePro、Nitori 已在競爭的通路；零售公司的外資規則**無資料**，需另查。
   - **外派**：只派 1–2 名達 EP 第 II 類（≥RM10,000／月）的總經理或技術主管〔MY-69～72〕。初級設計師的市場月薪（約 RM2,912–3,761〔MY-D69〕）低於 EP 第 III 類下限 RM5,000，無法外派。
2. **先打「新山跨境 B2B」，再打「巴生谷中古屋」。** JS-SEZ 第 1 季就有 RM274 億新投資〔MY-D37〕，新山現代辦公需求上升〔MY-D36〕，RTS Link 預計 2026-12 通車；但辦公入駐率只有 57.5%〔MY-D39〕。建議以台商與新加坡中小企業的辦公室、宿舍 fit-out 先做 3–5 個驗證案，再進入住宅。住宅端要瞄準中古屋（84.5%）與排屋（存量 41.3%），這和璞石在台灣做中古屋翻修的能力最接近〔MY-06、MY-D27〕。
3. **把「信任」做成產品。** CIDB 7 年 3,201 宗投訴、預付 80% 後停工的個案、TTPM 上限只有 RM50,000〔MY-D43、MY-D44、MY-49〕，說明馬國屋主最缺的是保障。做法有四：LAM 登記設計師署名、CIDB 登記承包商施工、依里程碑付款並交由第三方保管訂金（Qanvast Trust 已提供 RM50,000 保障〔MY-D79〕）、書面保固。這也剛好符合 2026 年 LAM 與 CIDB 的監管方向〔MY-59、MY-D51〕。
4. **價格帶低、設計費占比與台灣接近：用「台馬分工」守住毛利。** 中階單價 176–377 USD／m²，約為台灣新成屋中階（582–971 USD／m²）的三分之一；但除以人均 GDP 後，比例與台灣接近（1.26–2.70% 對 1.47–2.46%）。設計費占工程費 8–15%，與台灣 13–15% 同一量級〔MY-83～91、TW-21〕。可行做法是台灣團隊遠端出圖與選材，由本地登記設計師簽署、本地監工執行，以對抗中國業者 40–50% 價格、30 天工期的低價競爭〔MY-81〕。
5. **不動產部門可接「建商去化包」與「資本市場捷徑」。** 已完工未售 32,800 單位（2026Q1），以霹靂、柔佛、雪蘭莪最多〔MY-D28、MY-D29〕，適合提供「精裝＋家具」去化方案，與 Signature 集團「fit-out＋系統櫃」的路徑相同〔MY-95〕。資本市場給 fit-out 公司估值（SAG 上市市值約 RM6.2 億〔MY-D06〕），也可考慮少數入股擬上市的本地 fit-out 公司（如 Adnex、EGH）作為進入捷徑。CIDB 30% 規則如何適用於上市公司股東，需確認。

---

## 4. 與台灣比較的錨點

| 錨點 | 馬來西亞 | 台灣 | 公式／備註 | 標示 |
|---|---|---|---|---|
| 人均翻修支出 | **無資料**（TF 無馬國人口）。替代指標「每存量住宅單位」：RM715–774（167–181 USD／5,202–5,636 TWD）；廣義家居改善 RM7,694（1,797 USD） | 人均 757 USD（上限值）；每存量住宅約 58,512 TWD（1,877 USD） | 馬：RM44.3 億～48 億（2024，MY-D12、MY-D04）÷ 620 萬單位（2023，MY-D27）；RM477 億 ÷ 620 萬。台：5,500 億 TWD（2025，TW-23）÷ IMF 隱含人口 2,330 萬（TF-20 ÷ TF-18）；存量 ＝ 5,545,854 ÷ 59%（TW-13）≈ 940 萬戶 | 【示意】（年份與定義不一） |
| 翻修市場占 GDP 比 | **無資料**（TF 無馬國名目 GDP 總額） | 1.92%（5,500 億，上限值）；0.70%（ABRI 2,000 億，年代錯配） | 市場規模 ÷ 名目 GDP（台：TF-20 9,200.5 億 USD） | 【示意】 |
| 每 m² 單價 ÷ 人均 GDP | 基本 0.36–1.08%；中階 1.26–2.70%；高階 2.88–5.41% | 基本 0.74–1.47%；中階 1.47–2.46%（新成屋）或 2.46–3.69%（中古屋）；高階 3.69–4.92% | 馬：RM／sq ft × 10.7639 ÷ 4.2809 ÷ 13,949（MY-21、TF-18）；台：TWD／坪 ÷ 3.3058 ÷ 31.1663 ÷ 39,489（TW-22、TW-19） | 【示意】 |
| 設計費占工程費比 | 8–15%（成熟工作室 8–12%） | 13–15% | 馬：設計公司指南群（MY-83～91）；台：20 坪新成屋同端點配對（TW-21） | 【示意】 |
| 設計公司家數 ÷ 人口 | **無資料**（無人口）。替代「每萬存量住宅」：ID 執業體 72 家 → 0.12；LAM 建築＋ID 顧問所 1,981 家 → 3.20；G7 B07 承包商 907 家 → 1.46 | 每萬人 2.13；每萬存量住宅 5.29 | 馬：MY-D22（2021）、MY-D21（約 2024）、MY-D14 群（2025）÷ 620 萬；台：4,969 家（2011，TW-30）÷ 2,330 萬人或 940 萬戶 | 【示意】（年份錯配） |
| 平台滲透率 | **無資料**（Qanvast 累計逾 10 萬屋主，約 2021，地區未拆分〔MY-D80〕） | **無資料** | 平台成交案數 ÷ 年度翻修案數 | — |

讀法：馬國的絕對單價約為台灣的三分之一，但除以人均 GDP 後的負擔比與台灣相近。設計費占比兩地同級。每萬戶的「法定登記設計執業體」，馬國（0.12）遠少於台灣室內裝修業（5.29，含施工業者），反映馬國把「設計」嚴格限定在 LAM 登記者（推論）。

---

## 5. 矛盾資料與資料缺口

### 5.1 矛盾表

| 指標 | 來源 1 | 來源 2 | 差異原因（研判） | 裁決 |
|---|---|---|---|---|
| LAM 登記室內設計師人數 | 606 人＋72 個執業體（2021-08，MY-D22） | 165 人（約 2024，MY-60） | 差 3.7 倍；登記人數 3 年內減少七成不合常理，可能是 165 屬不同口徑（如當年新增、特定類別），或年份推定錯誤 | 採 606 人（有分項、出處為 MIID 引 LAM）；165 人列為存疑，需查 LAM 年報 |
| 室內裝修市場 2024 | RM48 億（Smith Zanders 合併口徑，MY-D04） | RM44.3 億（南洋地產，MY-D12）；2027 年 RM27 億（南洋商報群） | 定義與範圍不同；RM27 億可能是純 fit-out 預測 | 以 RM48 億為主錨（定義最清楚）；其他並列，不取平均 |
| 專業工程規模 | Smith Zanders RM48 億（2024） | DOSM 專業工程 RM214 億（2025，MY-16～19） | 差 4.5 倍；DOSM 含水電、土木等全部專業工程 | 不矛盾，屬範圍差；DOSM 只作上限代理 |
| 家居改善市場 | RM477 億（2024，MY-D01、MY-D11） | 10 億 USD ≈ RM42.8 億（2025，Ken Research，MY-D02） | 差約 11 倍；定義（含零售產品與否）與方法不同 | 兩者皆列【示意】；不得當作住宅翻修市場 |
| Recommend.my 募資 | A 輪 400 萬 USD（MY-D81） | 總募資 100 萬 USD（Craft.co，MY-D83） | 第三方資料庫可能未更新 | 採媒體報導 400 萬 USD，信心中 |
| ARCHIDEX 2025 | 行前：預估 56,000 人、850 家參展商來自 110 國、34,000 m²（MY-D85） | 事後：50,668 人次、850 家以上參展商來自 12 國（110 為參觀者國家／地區）、36,700 m²（MY-D84） | 預估與實際之別；國家數的描述對象不同 | 採主辦方事後數字（仍屬自報） |
| 公寓翻修工期 | 6–10 週（MY-D87～D89） | 3–6 個月（MY-D89 群） | 前者只算施工期，後者計入延誤 | 並列；報價時以 3 個月為規劃基準（推論） |
| 已完工未售金額 | 1H2025 26,911 單位／RM186 億（MY-D30） | 2025 全年 30,471 單位／RM177.3 億（MY-09、MY-10）；2026Q1 32,800 單位／RM163 億（MY-D28） | 單位數增加但金額下降，研判是低價州份（霹靂、吉蘭丹）占比上升 | 非矛盾；單位數採 NAPIC 官方值 |
| Livspace 退出馬國 | 研究簡報前提：已退出 | 搜尋：無退出報導，profile 仍列馬國（MY-D18） | 簡報前提未經來源證實 | 列為「無資料／未證實」 |
| 鋼筋均價 | 2022-06 RM3,897.11（besi bar＋mycon，MY-D72 群） | 2026-07 RM3,499.50（MY-D75） | 產品組合可能不同 | 累計 −10.2% 只作【示意】 |
| HomePro 馬國首店 | IOI Mall（吉隆坡） | IOI City Mall（布城） | 來源描述不一 | 不影響店數 7 家 |
| 家具＋室內設計（r1 沿用） | Ken Research 24.3 億 USD | 同公司另版 54.2 億 USD（MY-26／27） | 版本與定義不同 | 不取平均，低信心 |
| 100% 外資能否登記 CIDB 本地等級（r1 沿用） | ONEKEY BIZ：可（MY-38） | 律師樓：外資 >30% 不得登記為本地承包商（MY-65、MY-66） | 來源性質不同 | 採律師樓說法；需專業確認 |

### 5.2 資料缺口表

| 缺口 | 本輪嘗試 | 建議取得方式 |
|---|---|---|
| 住宅與商業 fit-out 拆分；Smith Zanders 原始定義 | 第 1、28、29 次搜尋 | 至 Bursa 網站讀 SAG、Adnex、EGH 招股書的 IMR 章節 |
| 馬國人口、名目 GDP 總額（人均、占 GDP 比錨點） | 未搜尋（屬中央 TF） | IMF WEO（NGDPD、LP）、DOSM，由中央統一代入 |
| 30 年以上屋齡占比 | 第 7、22 次 | NAPIC Property Stock Report 屋齡表；DOSM 2020 年人口與住屋普查 |
| LAM 2025–2026 室內設計師人數 | 第 3、20 次 | LAM 年報完整版（國會 ST 文件）；直接洽詢 LAM |
| Livspace 馬國現況 | 第 2、25 次 | 公司官網國家頁；SSM 公司狀態查詢 |
| Atap.co 規模；平台 GMV、抽成、滲透率 | 第 12 次 | 平台新聞稿、e27、DealStreetAsia |
| JBPM 商業 fit-out 送審流程與規費 | 第 13 次 | JBPM 官網；UBBL 1984 消防條文 |
| MBPJ 許可費與流程 | 第 14 次 | MBPJ 官網、OSC 指引 |
| KPDN 全國裝修投訴統計 | 第 15 次 | KPDN 年報；國會答詢（Hansard） |
| MTLM 營建業分層費率 | 第 11 次 | KDN、MOHR 正式公告或憲報 |
| 水電、木工等分工種 2026 年日薪；監工薪資 | 第 17、19、27 次 | CIDB 工資調查；JobStreet 薪資報告 |
| CIDB 建材價格指數 2022–2026 完整序列 | 第 16、30 次（只取得 DOSM 片段） | DOSM 建材成本指數月報完整表；CIDB CONVINCE 歷史資料 |
| JS-SEZ fit-out 規模與單價 | 第 6、18 次 | JLL、Knight Frank 新山辦公報告；Turner & Townsend 成本手冊 |
| 磁磚、衛浴品牌；進口依賴；關稅與標準 | 未搜尋 | Bursa 上市建材商年報；SIRIM、MITI |
| 零售業外資規則（distributive trade）、稅務 | 未搜尋 | MIDA、MITI 指引；四大會計師事務所稅務手冊 |
| 翻修融資（EPF、銀行翻修貸款）、補助 | 未搜尋 | EPF、Bank Negara、KPKT |
| 設計科系畢業人數 | 未搜尋 | 高教部統計；MQA 認可課程名單 |
| 典型翻修週期 | 第 4、9、26 次 | 業者訪談；Qanvast、Recommend.my 指南 |

---

## 6. 來源清單

讀取方式一律為「搜尋結果內容」（未直接開頁）；標「僅標題」者，表示只取得標題或極少摘要。

### 6.1 沿用 r1 來源（編號不變）

| # | 標題 | 機構 | 年份 | 語言 | URL | 讀取方式 |
|---|---|---|---|---|---|---|
| MY-06 | Malaysia Residential Property Market 2025 | Propplace | 2026 | 英文 | https://www.propplace.my/guides/malaysia-residential-property-market-2025 | 搜尋結果內容 |
| MY-09 | Laporan Status Pasaran Harta Tanah / Property Market Status Report 2025 | NAPIC（JPPH） | 2026 | 馬來文／英文 | https://napic.jpph.gov.my/storage/app/media//3-penerbitan/Shahrul/Bahagian%20Inventori%20Harta%20Tanah/Laporan%20Jadual%20Status%20Harta%20Tanah/Q4%202025/Laporan%20Status%20Harta%20Tanah%202025.pdf | 搜尋結果內容 |
| MY-10 | According to NAPIC's Property Market Report 2025… 30,471 completed, unsold residential units worth RM17.73 billion | @malaysiauncapped（Threads） | 2026 | 英文 | https://www.threads.com/@malaysiauncapped/post/DWWc8eDkT8b/according-to-napi-cs-property-market-report-malaysia-recorded-completed-unsold | 搜尋結果內容 |
| MY-16 | Construction Statistics First Quarter 2025 | 統計局（DOSM） | 2025 | 英文 | https://dosm.gov.my/portal-main/release-content/construction-statistics-first-quarter-2025 | 搜尋結果內容 |
| MY-17 | Construction Statistics Second Quarter 2025 | DOSM | 2025 | 英文 | https://www.dosm.gov.my/portal-main/release-content/construction-statistics-second-quarter-2025 | 搜尋結果內容 |
| MY-18 | Construction Statistics Third Quarter 2025 | DOSM | 2025 | 英文 | https://www.dosm.gov.my/portal-main/release-content/construction-statistics-third-quarter-2025 | 搜尋結果內容 |
| MY-19 | Construction Statistics Q4 2025 | DOSM | 2026 | 英文 | https://www.dosm.gov.my/portal-main/release-content/construction-statistics-q42025 | 搜尋結果內容 |
| MY-21 | How much will home renovation cost | Loanstreet | 2025 | 英文 | https://loanstreet.com.my/learning-centre/how-much-will-home-renovation-cost | 搜尋結果內容 |
| MY-22 | How Much Does It Cost To Renovate In Malaysia? | Qanvast | 年份未標示 | 英文 | https://qanvast.com/my/articles/how-much-does-it-cost-to-renovate-in-malaysia-928 | 搜尋結果內容 |
| MY-23 | Renovation costs Malaysia | PropCashflow | 2026 | 英文 | https://propcashflow.my/blog/renovation-costs-malaysia/ | 搜尋結果內容 |
| MY-24 | Home renovation guide | Malaysia4U | 2026 | 英文 | https://malaysia4u.com/home-renovation-guide | 搜尋結果內容 |
| MY-26 | Malaysia Furniture and Interior Design Market | Ken Research | 2025 | 英文 | https://www.kenresearch.com/malaysia-furniture-and-interior-design-market-krab6623 | 搜尋結果內容 |
| MY-27 | Malaysia Furniture and Interior Design Market（.md 版） | Ken Research | 2026 | 英文 | https://www.kenresearch.com/industry-reports/malaysia-furniture-and-interior-design-market.md | 搜尋結果內容 |
| MY-28 | Malaysia Home Decor Market Size, Share, Trends and Forecast 2025-2033 | IMARC Group | 2025 | 英文 | https://www.imarcgroup.com/malaysia-home-decor-market | 搜尋結果內容 |
| MY-29 | Home Décor – Malaysia（Market Insights） | Statista | 2024 | 英文 | https://www.statista.com/outlook/cmo/furniture/home-decor/malaysia | 搜尋結果內容 |
| MY-30 | General Circular No. 3/2007（Architects Act 1967 amendments） | Lembaga Arkitek Malaysia（LAM） | 2007 | 英文 | https://www.lam.gov.my/sites/default/files/form/no-3-2007.pdf | 搜尋結果內容 |
| MY-32 | Circular No. 1/2010 | LAM | 2010 | 英文 | https://www.lam.gov.my/sites/default/files/form/no-1-2010.pdf | 搜尋結果內容 |
| MY-35 | How To Be an Interior Designer in Malaysia | EduAdvisor | 2023 | 英文 | https://eduadvisor.my/articles/how-to-be-interior-designer-malaysia | 搜尋結果內容 |
| MY-37 | What is the Malaysian Institute of Interior Designers (MIID)? | Eduspiral | 2022 | 英文 | https://eduspiral.com/2022/04/15/what-is-the-malaysian-institute-of-interior-designers-miid/ | 搜尋結果內容（僅標題） |
| MY-38 | CIDB licence for foreign contractors in Malaysia (2026): grades, capital and the project-based rule | ONEKEY BIZ | 2026 | 英文 | https://onekeybiz.com/insights/cidb-licence-foreign-contractors-malaysia-2026.html | 搜尋結果內容 |
| MY-39 | CIDB Registration Malaysia 2026: G1-G7, SPKK & Capital | Get Foundation | 2026 | 英文 | https://www.getfoundation.com.my/blog/cidb-contractor-registration-malaysia-grades-spkk-guide | 搜尋結果內容 |
| MY-40 | A Complete Guide To CIDB Contractor Grades | MISHU | 不明 | 英文 | https://mishu.my/blog/business-licenses/guide-cidb-grades/ | 搜尋結果內容 |
| MY-41 | CIDB G5 Contractor Malaysia: Grades Explained (2026) | Waterproofing KL | 2026 | 英文 | https://waterproofingkl.com/en/resources/cidb-grades-explained/ | 搜尋結果內容 |
| MY-42 | Malaysia's Construction Industry: CIDB Contractor Grades G1–G7 & Registration | Negaraku | 不明 | 英文 | https://negaraku.md/en/industries/construction-industry/ | 搜尋結果內容 |
| MY-43 | Garis Panduan Permit Kerja Kecil WPKL (pindaan 15.9.2021) | Dewan Bandaraya Kuala Lumpur（DBKL） | 2021 | 馬來文 | https://www.dbkl.gov.my/wp-content/uploads/2023/08/GARIS-PANDUAN-PERMIT-KERJA-KECIL-WPKL-pindaan-15.9.2021.pdf | 搜尋結果內容 |
| MY-44 | DBKL cuts red tape for restaurants, food operators | New Straits Times | 2026 | 英文 | https://www.nst.com.my/amp/news/regional/2026/08/1508705/dbkl-cuts-red-tape-restaurants-food-operators | 搜尋結果內容 |
| MY-45 | Rules Eased For KL Businesses Carrying Out Small Renovation Works | SAYS | 2026 | 英文 | https://says.com/my/news/gomen/rules-eased-for-kl-businesses-carrying-out-small-renovation-works | 搜尋結果內容 |
| MY-46 | Mitos Bagi Kerja-Kerja Pengubahsuaian Di Bangunan Komersial | IPM | 2024 | 馬來文 | https://ipm.my/wp-content/uploads/2024/02/Mitos-Bagi-Kerja-Kerja-Pengubahsuaian-Di-Bangunan-Komersial.pdf | 搜尋結果內容（僅標題） |
| MY-47 | 12 kes tuntutan libatkan kontraktor rumah babitkan nilai lebih RM200,000 | Sinar Harian | 不明 | 馬來文 | https://www.sinarharian.com.my/article/703638/berita/semasa/12-kes-tuntutan-libatkan-kontraktor-rumah-babitkan-nilai-lebih-rm200000 | 搜尋結果內容 |
| MY-48 | Kes pengubahsuaian rumah catat aduan tertinggi TTPM Pulau Pinang | RTM Berita | 不明 | 馬來文 | https://berita.rtm.gov.my/?p=692611 | 搜尋結果內容 |
| MY-49 | （Harian Metro 2019-09-24 剪報：TTPM 上限提高至 RM50,000） | KPDN 機構典藏（Repositori KPDN） | 2019 | 馬來文 | https://repositori.kpdn.gov.my/bitstream/123456789/3490/1/METRO%2024.09.2019.pdf | 搜尋結果內容 |
| MY-50 | Jemaah ditipu boleh tuntut ganti rugi di tribunal | Utusan Malaysia | 2024 | 馬來文 | https://www.utusan.com.my/nasional/2024/08/jemaah-ditipu-boleh-tuntut-ganti-rugi-di-tribunal/ | 搜尋結果內容 |
| MY-52 | A practical guide to file a complaint at Tribunal for Consumer Claims Malaysia | Conventus Law | 不明 | 英文 | https://conventuslaw.com/report/a-practical-guide-to-file-a-complaint-at-tribunal-for-consumer-claims-malaysia/ | 搜尋結果內容 |
| MY-54 | 20 top interior design firms in Malaysia | PropertyGuru Malaysia | 不明 | 英文 | https://www.propertyguru.com.my/property-guides/20-top-interior-design-firms-in-malaysia-33650 | 搜尋結果內容（僅標題） |
| MY-58 | LAM reminds the public to engage only Registered Architects and Registered Interior Designers for interior design consultancy services under the Architects Act 1967 [Act 117] | Lembaga Arkitek Malaysia（官方 X 帳號） | 約 2026（依貼文 ID 推算） | 英文 | https://x.com/LembagaArkitek/status/2065266904147939778 | 搜尋結果內容 |
| MY-59 | General Circular No. 1/2026 | Lembaga Arkitek Malaysia | 2026 | 英文 | https://admin.lam.gov.my/report/circular/files//P310Eemy53kE.pdf | 搜尋結果內容 |
| MY-60 | Ulat Arkitek, Iklan Tawar Khidmat Seni Bina Secara Haram Makin Berleluasa – LAM | Bernama | 約 2024 | 馬來文 | https://bernama.com/bm/news.php?id=2325906 | 搜尋結果內容 |
| MY-61 | Laws of Malaysia Reprint – Act 117 Architects Act 1967 | TCC Law（上傳重印本） | 2025 | 英文 | https://tcclaw.com.my/wp-content/uploads/2025/07/Architects-Act-1967.pdf | 搜尋結果內容 |
| MY-63 | New CIDB Contractor Registration Requirements for Foreign Contractors | Lexology | 不明（約 2023） | 英文 | https://www.lexology.com/library/detail.aspx?g=42dd714e-3e05-44ae-8fb0-f8e457419c6f | 搜尋結果內容 |
| MY-65 | Construction Industry of Malaysia | Christopher & Lee Ong | 不明 | 英文 | https://www.christopherleeong.com/viewpoints/construction-industry-malaysia/ | 搜尋結果內容 |
| MY-66 | New CIDB Regimes for Foreign Contractors | WM Law | 2023 | 英文 | https://wmlaw.com.my/2023/05/15/new-cidb-regimes-for-foreign-contractors/ | 搜尋結果內容 |
| MY-68 | Contractor Registration with CIDB Malaysia for Consortium or Joint Venture Company | Bestar | 不明 | 英文 | https://www.bestar-my.com/post/contractor-registration-with-cidb-malaysia-for-consortium-or-joint-venture-company-1 | 搜尋結果內容 |
| MY-69 | Malaysia: Expatriate Services Division increases Employment Pass salary | Baker McKenzie | 2026 | 英文 | https://www.bakermckenzie.com/en/insight/publications/2026/01/malaysia-expatriate-services-division-increases-employment-pass-salary | 搜尋結果內容 |
| MY-70 | Malaysia – Immigration – Revision to the minimum salary requirements for Employment Pass from 1 June 2026 | Vialto Partners | 2026 | 英文 | https://vialtopartners.com/regional-alerts/malaysia-immigration-revision-to-the-minimum-salary-requirements-for-employment-pass-from-1-june-2026/ | 搜尋結果內容 |
| MY-71 | Malaysia Revises Minimum Salary for Employment Pass Applications Effective June 1, 2026 | EIG Law | 2026 | 英文 | https://eiglaw.com/malaysia-revises-minimum-salary-for-employment-pass-applications-effective-june-1-2026/ | 搜尋結果內容 |
| MY-72 | （EY Tax News 2026-06-11：Employment Pass 新門檻） | EY | 2026 | 英文 | https://taxnews.ey.com/news/2026-1256 | 搜尋結果內容 |
| MY-73 | Multi-tier levy mechanism implementation by January 2025, says HR minister | Malay Mail | 2024 | 英文 | https://www.malaymail.com/news/malaysia/2024/05/20/multi-tier-levy-mechanism-implementation-by-january-2025-says-hr-minister/135529 | 搜尋結果內容 |
| MY-74 | Multi-tiered levy mechanism to be carried out in January | New Straits Times | 2024 | 英文 | https://nst.com.my/amp/news/government-public-policy/2024/05/1053146/multi-tiered-levy-mechanism-be-carried-out-january | 搜尋結果內容 |
| MY-75 | Govt to hold stakeholder engagement sessions before implementing multi-tier levy mechanism | The Vibes | 不明 | 英文 | https://www.thevibes.com/articles/news/105709/govt-to-hold-stakeholder-engagement-sessions-before-implementing-multi-tier-levy-mechanism | 搜尋結果內容（僅標題） |
| MY-76 | （MTLM 實施相關報導） | The Edge Malaysia | 不明（2025–26） | 英文 | https://theedgemalaysia.com/node/764721 | 搜尋結果內容 |
| MY-77 | （MTLM 實施相關報導） | Bernama | 不明（2025–26） | 英文 | https://bernama.com/en/news.php?id=2400782 | 搜尋結果內容 |
| MY-78 | BPA Report, page 102（外勞稅分層設計） | 人力資源部（MOHR） | 不明 | 不明 | https://www.mohr.gov.my/images/BPAReport/files/basic-html/page102.html | 搜尋結果內容 |
| MY-79 | （營建業外勞成本與 2027 年預算最低工資） | Berita Harian | 2026 | 馬來文 | https://www.bharian.com.my/amp/berita/nasional/2026/10/1656474/bhplus | 搜尋結果內容 |
| MY-80 | Updates on the progress of Malaysia's upcoming multi-level levy mechanism for foreign workers | Human Resources Online | 不明 | 英文 | https://www.humanresourcesonline.net/updates-on-the-progress-of-malaysia-s-upcoming-multi-level-levy-mechanism-for-foreign-workers | 搜尋結果內容（僅標題） |
| MY-81 | 【独家】中国装修工比本地价低50% 非法施工材料问题或酿祸 | 南洋商報（e南洋） | 2025 | 華文（馬來西亞） | https://www.enanyang.my/news/20250515/Finance/681613 | 搜尋結果內容 |
| MY-83 | Interior Design Pricing Malaysia: Why Renovations Cost RM30k–RM250k | Coohom | 2026 | 英文 | https://www.coohom.com/article/interior-design-pricing-trends-in-malaysia-for-modern-homeowners | 搜尋結果內容 |
| MY-84 | Interior Design & Renovation Cost Malaysia 2026 (RM120k-RM1.8mil+) | Houz | 2026 | 英文 | https://www.houz.com.my/interior-design-cost-malaysia/ | 搜尋結果內容 |
| MY-85 | Interior Design Cost Malaysia 2026 | Blaine Robert Design | 2026 | 英文 | https://blainerobertdesign.com/home-reno/interior-design-cost-malaysia/ | 搜尋結果內容 |
| MY-86 | Renovation Cost in Malaysia (2026): Per Sq Ft and by Room | iHome.my | 2026 | 英文 | https://ihome.my/renovation/renovation-cost-malaysia/ | 搜尋結果內容 |
| MY-87 | Interior Design Cost Malaysia 2026: Affordable & Complete Renovation Guide | Zachary Khaw | 2025 | 英文 | https://zacharykhaw.com/2025/09/05/interior-design-cost-malaysia/ | 搜尋結果內容 |
| MY-88 | Office Interior Design KL Cost Guide 2026 | Goodwinds | 2026 | 英文 | https://goodwinds.com.my/office-interior-design-kl-cost-guide-2026/ | 搜尋結果內容 |
| MY-89 | Interior Design Cost Malaysia 2026: Complete Pricing Guide | interiordesignerkl.com | 2026 | 英文 | https://interiordesignerkl.com/guides/interior-design-cost-malaysia/ | 搜尋結果內容 |
| MY-90 | Home Renovation Malaysia: Complete Cost Guide 2026 | Mo-ane | 2026 | 英文 | https://mo-ane.com/blog/home-renovation-cost-malaysia-2026 | 搜尋結果內容 |
| MY-91 | Interior Design Cost in Malaysia: What to Expect in 2026 | Stuarts Design | 2026 | 英文 | https://stuartsdesign.com/interior-design-cost-in-malaysia-what-to-expect-in-2026/ | 搜尋結果內容 |
| MY-92 | MR DIY kicks off 2025 with RM174.15m net profit in 1Q, eyes 190 new stores | Malay Mail | 2025 | 英文 | https://www.malaymail.com/amp/news/money/2025/05/05/mr-diy-kicks-off-2025-with-rm17415m-net-profit-in-1q-eyes-190-new-stores/175687 | 搜尋結果內容 |
| MY-93 | New store openings lift MR DIY's 3Q results | New Straits Times | 2025 | 英文 | https://www.nst.com.my/amp/business/corporate/2025/11/1312184/new-store-openings-lift-mr-diys-3q-results | 搜尋結果內容 |
| MY-94 | MR DIY Group FY25 earnings hit target as margins and expansion drive growth | Focus Malaysia | 2026 | 英文 | https://focusmalaysia.my/?p=236095 | 搜尋結果內容 |
| MY-95 | Signature International nears RM1b revenue milestone, backed by RM1.28b order book | Focus Malaysia | 2026 | 英文 | https://focusmalaysia.my/?p=236235 | 搜尋結果內容 |
| MY-98 | Ikano Retail, owner of IKEA Malaysia, posts turnover for FY24 | The Sun | 2024 | 英文 | https://thesun.my/business/ikano-retail-owner-of-ikea-malaysia-posts-109b-turnover-for-fy24-md13102394/ | 搜尋結果內容 |
| MY-99 | Retail 2025 | Ikano Group | 2025 | 英文 | https://group.ikano/stories/retail-2025/ | 搜尋結果內容 |
| MY-102 | Tradition meets innovation in Courts Raya 2025 campaign | Borneo Post | 2025 | 英文 | https://www.theborneopost.com/2025/02/18/tradition-meets-innovation-in-courts-raya-2025-campaign/ | 搜尋結果內容 |
| MY-105 | Summary of NAPIC Property Market Report 2024 | REHDA Institute | 2025 | 英文 | https://rehdainstitute.com/wp-content/uploads/2025/05/NAPIC-Property-Market-2024-v2-For-Website.pdf | 搜尋結果內容 |
| MY-108 | Navigating Policy Challenges in Malaysia's Construction Sector: The Governmental Dilemma on the Issue of Foreign Labour Shortage in Malaysia | RSIS International（IJRISS） | 約 2023 | 英文 | https://rsisinternational.org/journals/ijriss/articles/navigating-policy-challenges-in-malaysias-construction-sector-the-governmental-dilemma-on-the-issue-of-foreign-labour-shortage-in-malaysia/ | 搜尋結果內容 |
| MY-110 | LABOUR WAGE RATES | Scribd（上傳者不明） | 2023 | 英文 | https://www.scribd.com/document/726139748/LABOUR-WAGE-RATES | 搜尋結果內容 |
| MY-111 | Salary and Wages in Malaysia – Malaysia Guide | ASEAN Briefing（Dezan Shira） | 2025 | 英文 | https://www.aseanbriefing.com/doing-business-guide/malaysia/human-resources-and-payroll/salaries-minimum-wages-malaysia | 搜尋結果內容 |
| MY-113 | 消费仲裁庭：装修的缺陷 [2021] MLJU 1365 | Kuekong（郭剛律師樓） | 不明 | 華文（馬來西亞） | https://www.kuekong.com/?p=24463 | 搜尋結果內容 |
| MY-114 | How to make sure your home defects are fixed properly during the DLP? | iProperty Malaysia | 不明 | 英文 | https://www.iproperty.com.my/guides/home-defects-dlp-71608 | 搜尋結果內容 |
| MY-118 | A Practical Guide to Filing a Claim at the Homebuyer's Tribunal | Richard Wee Chambers | 不明 | 英文 | https://www.richardweechambers.com/a-practical-guide-to-filing-a-claim-at-the-homebuyers-tribunal/ | 搜尋結果內容 |
| MY-119 | How to File a Consumer Claims Tribunal (TTPM) Claim in Malaysia (2026) | sorted-my（個人網站） | 2026 | 英文 | https://hlteoh37.github.io/sorted-my/guides/ttpm-consumer-tribunal/ | 搜尋結果內容 |
| MY-120 | Special Release for Building and Structural Works, December 2025 | DOSM | 2026 | 英文 | https://www.dosm.gov.my/portal-main/release-content/special-release-for-building-and-structural-works-december-2025 | 搜尋結果內容 |
| MY-121 | Special Release for Building and Structural Works, February 2025 | DOSM | 2025 | 英文 | https://www.dosm.gov.my/portal-main/release-content/special-release----for-building-and-structural-works-february-2025 | 搜尋結果內容 |
| MY-122 | CONVINCE（建材價格入口網站） | CIDB | 不明 | 英文 | https://convince.cidb.gov.my/ | 搜尋結果內容 |
| MY-123 | Here's What You Can & Cannot Do When Renovating Your Condo In Malaysia | SAYS | 不明 | 英文 | https://says.com/my/lifestyle/home-and-living/condo-renovation-malaysia | 搜尋結果內容 |
| MY-126 | Bangunan lebih 30 tahun tidak sesuai diduduki? | Utusan Malaysia | 2026 | 馬來文 | https://www.utusan.com.my/ekonomi/2026/01/bangunan-lebih-30-tahun-tidak-sesuai-diduduki/ | 搜尋結果內容 |
| MY-127 | Akta Pembaharuan Semula Bandar lindungi pemilik, tingkatkan kualiti kehidupan – Kor Ming | Malaysia Gazette | 2025 | 馬來文 | https://malaysiagazette.com/2025/04/29/akta-pembaharuan-semula-bandar-lindungi-pemilik-tingkatkan-kualiti-kehidupan-kor-ming/ | 搜尋結果內容 |

### 6.2 本輪新增來源

| # | 標題 | 機構 | 年份 | 語言 | URL | 讀取方式 |
|---|---|---|---|---|---|---|
| MY-D01 | Malaysian home renovation demand rising post-pandemic on lifestyle shift, says Topmix CEO | KLSE Screener（轉載） | 不明（約 2025） | 英文 | https://www.klsescreener.com/v2/news/view/1748129/malaysian-home-renovation-demand-rising-post-pandemic-on-lifestyle-shift-says-topmix-ceo | 搜尋結果內容 |
| MY-D02 | Malaysia Home Improvement Market Share, Companies & Trends Report 2026-2032 | Ken Research | 2026 | 英文 | https://www.kenresearch.com/industry-reports/malaysia-home-improvement-market | 搜尋結果內容 |
| MY-D03 | Malaysia Construction Market Size, Industry Outlook 2031 | Mordor Intelligence | 2026 | 英文 | https://www.mordorintelligence.com/industry-reports/malaysia-construction-market | 搜尋結果內容 |
| MY-D04 | IPO Watch: Signature Alliance relies on diversified portfolio to counter market slowdown | The Edge Malaysia | 2025 | 英文 | https://theedgemalaysia.com/node/757654 | 搜尋結果內容 |
| MY-D05 | Malaysia IPO Note: Signature Alliance Group – A Trusted Interior Fitting-Out Specialist | RHB（i3investor 存檔） | 2025 | 英文 | https://cdn1.i3investor.com/my/files/st88k/0360_SAG/pt/RHB/0360_SAG_RHB_2025-05-19_BUY_0.67_SignatureAllianceGroupATrustedInteriorFittingOutSpecialist_-523745964.pdf | 搜尋結果內容 |
| MY-D06 | Signature Alliance targets RM161mil from IPO | The Star | 2025 | 英文 | https://www.thestar.com.my/business/business-news/2025/05/15/signature-alliance-targets-rm161mil-from-ipo | 搜尋結果內容 |
| MY-D07 | Signature Alliance Group's IPO sees muted demand, gets just enough applications to fill offering | The Edge Malaysia | 2025 | 英文 | https://theedgemalaysia.com/node/756461 | 搜尋結果內容 |
| MY-D08 | Signature Alliance sets FY2026 growth course as interior fit-out demand gains momentum | Focus Malaysia | 2026 | 英文 | https://focusmalaysia.my/signature-alliance-sets-fy2026-growth-course-as-interior-fit-out-demand-gains-momentum/ | 搜尋結果內容 |
| MY-D09 | Signature Alliance Group Berhad is a subsidiary of MAIN Market-listed Signature International Berhad… | Bursa Malaysia（官方 X 帳號） | 2025 | 英文 | https://x.com/BursaMalaysia/status/1925110469158965613 | 搜尋結果內容 |
| MY-D10 | 【独家】疫后迎来黄金爆发期 室内装修业者排队上市 | 南洋商報（e南洋） | 2025 | 華文（馬來西亞） | https://www.enanyang.my/news/20251004/Finance/1018839 | 搜尋結果內容 |
| MY-D11 | 家居改善市场迎来"连锁时代" | 南洋地產（Nanyang Property） | 不明 | 華文（馬來西亞） | https://property.enanyang.my/%E8%B6%8B%E5%8A%BF/%E5%AE%B6%E5%B1%85%E6%94%B9%E5%96%84%E5%B8%82%E5%9C%BA%E8%BF%8E%E6%9D%A5%E8%BF%9E%E9%94%81%E6%97%B6%E4%BB%A3/ | 搜尋結果內容 |
| MY-D12 | 室内设计关怀年长者需求 | 南洋地產（Nanyang Property） | 不明 | 華文（馬來西亞） | https://property.enanyang.my/%E8%B6%8B%E5%8A%BF/%E5%AE%A4%E5%86%85%E8%AE%BE%E8%AE%A1%E5%85%B3%E6%80%80%E5%B9%B4%E9%95%BF%E8%80%85%E9%9C%80%E6%B1%82/ | 搜尋結果內容（數字對應不確定） |
| MY-D13 | 室内装修服务商 Adnex集团拟上创业板 | 南洋商報（e南洋） | 2025 | 華文（馬來西亞） | https://www.enanyang.my/news/20250703/Finance/911781 | 搜尋結果內容 |
| MY-D14 | 室内装修工程商 EGH国际拟上市创业板 | 中國報 | 2026 | 華文（馬來西亞） | https://www.chinapress.com.my/20260108/%E5%AE%A4%E5%86%85%E8%A3%85%E4%BF%AE%E5%B7%A5%E7%A8%8B%E5%95%86-egh%E5%9B%BD%E9%99%85%E6%8B%9F%E4%B8%8A%E5%B8%82%E5%88%9B%E4%B8%9A%E6%9D%BF/ | 搜尋結果內容（907 家數字對應不確定） |
| MY-D15 | 【独家】金鹰冠军上市高飞 鼎时达凭优势开疆扩土 | 南洋商報（e南洋） | 2026 | 華文（馬來西亞） | https://www.enanyang.my/news/20260221/Finance/1172284?variant=zh-hant | 搜尋結果內容（僅標題） |
| MY-D16 | 企业故事｜胜利者联盟筹资逾亿 加速扩展室内装修业务 | 星洲日報（星洲人） | 2025 | 華文（馬來西亞） | https://www.sinchew.com.my/news/20250602/%E6%98%9F%E6%B4%B2%E4%BA%BA/6579076 | 搜尋結果內容 |
| MY-D17 | Livspace CBO Lalit Mittal exits after co-founder departure and mass layoffs | Entrackr | 2025–2026 | 英文 | https://entrackr.com/news/livspace-cbo-lalit-mittal-exits-after-co-founder-departure-and-mass-layoffs-11150871 | 搜尋結果內容 |
| MY-D18 | Livspace（公司頁） | Built In Singapore | 不明 | 英文 | https://builtinsingapore.com/company/livspace | 搜尋結果內容 |
| MY-D19 | Home renovation platform Livspace raises USD 90 million to expand in Southeast Asia, Australia | KR-Asia | 不明（較早） | 英文 | https://amp.kr-asia.com/home-renovation-platform-livspace-raises-usd-90-million-to-expand-in-southeast-asia-australia | 搜尋結果內容 |
| MY-D20 | ST.13.2024（LAM 年報，國會文件） | 國會典藏（Repositori Parlimen） | 2024 | 馬來文 | https://repositori.parlimen.gov.my/bitstream/123456789/1611/13/ST.13.2024 | 搜尋結果內容 |
| MY-D21 | ST.1.2025（LAM 年報，國會文件） | 國會典藏（Repositori Parlimen） | 2025 | 馬來文 | https://repositori.parlimen.gov.my/bitstream/123456789/3521/1/ST.1.2025 | 搜尋結果內容 |
| MY-D22 | Registered interior designers gain greater industry recognition and credibility（Contributed by MIID） | StarProperty | 約 2021 | 英文 | https://www.starproperty.my/news/registered-interior-designers-gain-greater-industry-recognition-and-credibility-/121482 | 搜尋結果內容 |
| MY-D23 | MIID: check legitimacy of interior designers, contractors before renovation | EdgeProp | 不明 | 英文 | https://www.edgeprop.my/content/1904835/miid-check-legitimacy-interior-designers-contractors-renovation | 搜尋結果內容 |
| MY-D24 | Adj. Prof. IDr Norshafina Ibrahim（profile） | Asia Property Awards | 不明 | 英文 | https://www.asiapropertyawards.com/en/?p=43925 | 搜尋結果內容 |
| MY-D25 | Scam in Renovation Works: The Role of Registered Interior Designers | StarProperty | 不明 | 英文 | https://www.starproperty.my/news/scam-in-renovation-works-the-role-of-registered-interior-designers/124270 | 搜尋結果內容（僅標題） |
| MY-D26 | Notis Pemberitahuan CPD（Perekabentuk Dalaman） | Lembaga Arkitek Malaysia | 不明 | 馬來文 | https://lam.gov.my/sites/default/files/article/Notis-Pemberitahuan-cpd-id.pdf | 搜尋結果內容 |
| MY-D27 | My Local Stats: Malaysia, State & Administrative District 2023 | 統計局（DOSM） | 2024 | 英文 | https://www.dosm.gov.my/portal-main/release-content/my-local-stats--malaysia-state--administrative-district-2023 | 搜尋結果內容 |
| MY-D28 | Housing mismatch persists as 32,800 unsold homes worth RM16.3b recorded in Q1 2026, Dewan Rakyat told | Malay Mail | 2026 | 英文 | https://www.malaymail.com/amp/news/malaysia/2026/06/29/housing-mismatch-persists-as-32800-unsold-homes-worth-rm163b-recorded-in-q1-2026-dewan-rakyat-told/225632 | 搜尋結果內容 |
| MY-D29 | What is driving Perak's rising stock of unsold homes（The Edge 轉載） | Rahim & Co | 2026 | 英文 | https://www.rahim-co.com/news/what-is-driving-peraks-rising-stock-of-unsold-homes | 搜尋結果內容（分州數字對應不確定） |
| MY-D30 | （1H2025 已完工未售住宅報導） | Berita Harian | 2025 | 馬來文 | https://www.bharian.com.my/amp/bisnes/hartanah/2025/10/1453698/bhplus | 搜尋結果內容（與同站 2025-09 報導對應不確定） |
| MY-D31 | Nitori Holdings FY2026 店舖計畫（決算資料） | MarketScreener（轉載 Nitori） | 2026 | 日文／英文 | https://in.marketscreener.com/news/nitori-e-ae--ce7f5bddd88af42c | 搜尋結果內容 |
| MY-D32 | Nitori to accelerate expansion in Southeast Asia, India amid China's slump — Nikkei Asia | The Edge Malaysia | 2024 | 英文 | https://theedgemalaysia.com/node/729850 | 搜尋結果內容 |
| MY-D33 | Nitori opens its largest Malaysian store at The Mall, Mid Valley Southkey on Dec 15 | Business Today | 2022 | 英文 | https://www.businesstoday.com.my/2022/12/07/nitori-opens-its-largest-malaysian-store-at-the-mall-mid-valley-southkey-on-dec-15/ | 搜尋結果內容 |
| MY-D34 | HMPRO: Listed Company Snapshot（YE 2025） | 泰國證交所（SET） | 2026 | 英文 | https://lssmedia.setlink.set.or.th/2025/YE/HMPRO-YE68-ListedCompanySnapshot-EN.html | 搜尋結果內容 |
| MY-D35 | Hectares of home improvement | StarProperty | 不明 | 英文 | https://www.starproperty.my/news/featured-news/hectares-of-home-improvement/71689 | 搜尋結果內容（對應不確定） |
| MY-D36 | Pitfalls & Pitch Calls: Johor's reawakening: How the JS-SEZ is powering a property revival | The Edge Malaysia | 2025 | 英文 | https://theedgemalaysia.com/node/753786 | 搜尋結果內容 |
| MY-D37 | Johor-Singapore Special Economic Zone: May 2025 update | Lexology | 2025 | 英文 | https://www.lexology.com/library/detail.aspx?g=8fcc98a6-ce00-424d-a8dd-78124e95b60a | 搜尋結果內容 |
| MY-D38 | 社论．柔新经济特区开创新局：以深圳为范例 | 星洲日報 | 2025 | 華文（馬來西亞） | https://www.sinchew.com.my/news/20250107/yl/6199598 | 搜尋結果內容 |
| MY-D39 | 大型项目提振柔佛产业市场 | 南洋地產（Nanyang Property） | 不明 | 華文（馬來西亞） | https://property.enanyang.my/%E8%B6%8B%E5%8A%BF/%E5%A4%A7%E5%9E%8B%E9%A1%B9%E7%9B%AE%E6%8F%90%E6%8C%AF%E6%9F%94%E4%BD%9B%E4%BA%A7%E4%B8%9A%E5%B8%82%E5%9C%BA/ | 搜尋結果內容 |
| MY-D40 | 陆兆福：2大重点项目 带动新山经济转型发展 | 中國報（柔佛） | 2023 | 華文（馬來西亞） | https://johor.chinapress.com.my/20230702/%E9%99%86%E5%85%86%E7%A6%8F%EF%BC%9A2%E5%A4%A7%E9%87%8D%E7%82%B9%E9%A1%B9%E7%9B%AE-%E5%B8%A6%E5%8A%A8%E6%96%B0%E5%B1%B1%E7%BB%8F%E6%B5%8E%E8%BD%AC%E5%9E%8B%E5%8F%91%E5%B1%95/ | 搜尋結果內容 |
| MY-D41 | 【柔新经济特区特辑】新山房价飙升 投资热潮来袭 | 南洋商報（e南洋） | 2025 | 華文（馬來西亞） | https://www.enanyang.my/news/20250411/Finance/677853 | 搜尋結果內容（僅標題） |
| MY-D42 | 柔新经济特区及元首效应加持 新山重现有地房产抢购潮 | 東方日報 | 2024 | 華文（馬來西亞） | https://www.orientaldaily.com.my/news/south/2024/12/22/701099 | 搜尋結果內容（僅標題） |
| MY-D43 | 亚历山大：受害者损失数十万 工程部4策略打击承包商诈骗 | 南洋商報（e南洋） | 2026 | 華文（馬來西亞） | https://www.enanyang.my/news/20260817/Nation/1351712 | 搜尋結果內容 |
| MY-D44 | 装修承包商工程停滞不前 无一完成 多名屋主合共损失上百万 | 東方日報 | 2024 | 華文（馬來西亞） | https://www.orientaldaily.com.my/news/society/2024/08/12/672237 | 搜尋結果內容 |
| MY-D45 | 付近15万装修费设计师没开工 屋主报警揭还有7苦主 | 星洲日報（柔佛） | 2025 | 華文（馬來西亞） | https://johor.sinchew.com.my/news/20251103/johor/6998753?variant=zh-hant | 搜尋結果內容（僅標題） |
| MY-D46 | 独家｜装修未动工老板失踪 定金 薪水 全蒸发 | 中國報 | 2025 | 華文（馬來西亞） | https://www.chinapress.com.my/20250905/%E7%8B%AC%E5%AE%B6%EF%BD%9C%E8%A3%85%E4%BF%AE%E6%9C%AA%E5%8A%A8%E5%B7%A5%E8%80%81%E6%9D%BF%E5%A4%B1%E8%B8%AA-%E5%AE%9A%E9%87%91-%E8%96%AA%E6%B0%B4-%E5%85%A8%E8%92%B8%E5%8F%91%E3%80%80/ | 搜尋結果內容（僅標題） |
| MY-D47 | 收订金没装修12屋主报警 申诉拒付尾账被承包商恐吓 | 星洲日報 | 2023 | 華文（馬來西亞） | https://www.sinchew.com.my/news/20231204/nation/5174324 | 搜尋結果內容 |
| MY-D48 | 装修工程漏洞百出 越堤族告上庭 获赔1.5万 | 中國報（柔佛） | 2024 | 華文（馬來西亞） | https://johor.chinapress.com.my/20240328/%E8%A3%85%E4%BF%AE%E5%B7%A5%E7%A8%8B%E6%BC%8F%E6%B4%9E%E7%99%BE%E5%87%BA-%E8%B6%8A%E5%A0%A4%E6%97%8F%E5%91%8A%E4%B8%8A%E5%BA%AD-%E8%8E%B7%E8%B5%941-5%E4%B8%87/ | 搜尋結果內容 |
| MY-D49 | 不满橱柜装修突加价一万 工程师入禀仲裁庭获判退款 | 中國報（柔佛） | 2024 | 華文（馬來西亞） | https://johor.chinapress.com.my/20240815/%E4%B8%8D%E6%BB%A1%E6%A9%B1%E6%9F%9C%E8%A3%85%E4%BF%AE%E7%AA%81%E5%8A%A0%E4%BB%B7%E4%B8%80%E4%B8%87-%E5%B7%A5%E7%A8%8B%E5%B8%88%E5%85%A5%E7%A6%80%E4%BB%B2%E8%A3%81%E5%BA%AD%E8%8E%B7%E5%88%A4/ | 搜尋結果內容 |
| MY-D50 | "口传口"介绍人装修陷骗局 承包商卷逾23万 12人跳脚 | 星洲日報（馬六甲） | 2024 | 華文（馬來西亞） | https://melaka.sinchew.com.my/news/20241223/melaka/6169690 | 搜尋結果內容 |
| MY-D51 | Ucapan KE CIDB – Jom Bina Sempurna | CIDB | 2026 | 馬來文 | https://www.cidb.gov.my/wp-content/uploads/2026/03/Ucapan-KE-CIDB_JomBinaSempurna.pdf | 搜尋結果內容 |
| MY-D52 | Fahami perjanjian ubah suai rumah elak jadi mangsa penipuan – CIDB | Sinar Harian | 不明 | 馬來文 | https://www.sinarharian.com.my/article/638789/berita/nasional/fahami-perjanjian-ubah-suai-rumah-elak-jadi-mangsa-penipuan---cidb | 搜尋結果內容 |
| MY-D53 | （TTPM 裁決紀錄，含 TTPM-M-(P)-270-2024） | KPDN 機構典藏 | 2025 | 馬來文 | https://repositori.kpdn.gov.my/handle/123456789/5258?mode=full | 搜尋結果內容（案號對應不確定） |
| MY-D54 | Bomba Johor mula gempur rumah kedai dijadikan bilik sewa haram | Utusan Malaysia | 2026 | 馬來文 | https://www.utusan.com.my/terkini/2026/07/bomba-johor-mula-gempur-rumah-kedai-dijadikan-bilik-sewa-haram/ | 搜尋結果內容 |
| MY-D55 | Bomba Johor Gempur Sembilan 'Rumah Sarang Burung', Elak Risiko Kebakaran | Bernama | 2026 | 馬來文 | https://www.bernama.com/bm/jenayah_mahkamah/news.php?id=2587937 | 搜尋結果內容 |
| MY-D56 | Bomba kerjasama dengan Tourism Perak tingkat kesedaran pengusaha inap desa | Sinar Harian | 不明 | 馬來文 | https://www.sinarharian.com.my/ampArticle/279785 | 搜尋結果內容 |
| MY-D57 | Ubah suai secara haram: 45 notis dikeluarkan kepada 11 premis sekitar JB | RTM Berita | 不明 | 馬來文 | https://berita.rtm.gov.my/?p=669982 | 搜尋結果內容 |
| MY-D58 | Ubah suai melampau: Pangsapuri sekitar Taman Datuk Harun jadi contoh negatif | Sinar Harian | 不明 | 馬來文 | https://www.sinarharian.com.my/article/267662/edisi/selangor-kl/ubah-suai-melampau-pangsapuri-sekitar-taman-datuk-harun-jadi-contoh-negatif | 搜尋結果內容 |
| MY-D59 | Garispanduan UBT Kecil | 新山市政廳（MBJB） | 2023 | 馬來文 | https://www.mbjb.gov.my/sites/default/files/2023-01/Garispanduan%20UBT%20kecil.pdf | 搜尋結果內容 |
| MY-D60 | Property management: Ask the experts — expenses and renovations | EdgeProp | 不明 | 英文 | https://edgeprop.my/content/1564006/property-management-ask-experts-%E2%80%94-expenses-and-renovations | 搜尋結果內容 |
| MY-D61 | （Strata 裝修附則評論） | HHQ 律師事務所 | 不明 | 英文 | https://hhq.com.my/?p=27033 | 搜尋結果內容 |
| MY-D62 | Pengambilan Pekerja Asing | 馬來西亞投資發展局（MIDA） | 不明 | 馬來文 | https://www.mida.gov.my/ms/setting-up-content/pengambilan-pekerja-asing/ | 搜尋結果內容 |
| MY-D63 | （MTLM 與外勞凍結報導） | Berita Harian | 2026 | 馬來文 | https://www.bharian.com.my/amp/bisnes/lain-lain/2026/01/1492693/bhplus | 搜尋結果內容（對應不確定） |
| MY-D64 | 法规严·取缔频 大马已非印尼外劳最爱 | 南洋商報（e南洋） | 2025 | 華文（馬來西亞） | https://www.enanyang.my/news/20250319/Finance/674217 | 搜尋結果內容 |
| MY-D65 | 外劳薪酸（二）｜魏献勤：影响工程进度 建业聘外劳程序冗长 | 星洲日報 | 2024 | 華文（馬來西亞） | https://www.sinchew.com.my/news/20240120/%E6%98%9F%E6%9C%9F%E5%A4%A9%E5%A4%B4%E6%9D%A1/5412426 | 搜尋結果內容 |
| MY-D66 | 梁乾强：建筑业严缺工人 引进100万外劳都不够 | 星洲日報（霹靂） | 2022 | 華文（馬來西亞） | https://perak.sinchew.com.my/news/20220716/perak/3946866 | 搜尋結果內容（對應不確定） |
| MY-D67 | 1700令吉最低薪金涵盖外劳 家庭佣人及合约学徒除外 | 東方日報 | 2024 | 華文（馬來西亞） | https://www.orientaldaily.com.my/news/nation/2024/10/19/687545 | 搜尋結果內容 |
| MY-D68 | Minimum wage throughout Malaysia aligned from 1 August 2025 | Skrine | 2025 | 英文 | https://www.skrine.com/insights/alerts/july-2025/minimum-wage-throughout-malaysia-aligned-from-1-au | 搜尋結果內容 |
| MY-D69 | Interior Designer salary in Malaysia | Indeed Malaysia | 2026 | 英文 | https://malaysia.indeed.com/salaries/interior-designer-Salaries | 搜尋結果內容 |
| MY-D70 | Interior designer salary in Kuala Lumpur | AJobThing | 2025–2026 | 英文 | https://www.ajobthing.com/resources/recruitment-tools/salary-comparison-tool/interior-designer-salary-in-kuala-lumpur | 搜尋結果內容 |
| MY-D71 | Senior interior designer salary in Kuala Lumpur | AJobThing | 2025–2026 | 英文 | https://www.ajobthing.com/resources/recruitment-tools/salary-comparison-tool/senior-interior-designer-salary-in-kuala-lumpur | 搜尋結果內容 |
| MY-D72 | （建材成本指數發布檔下載紀錄，2022–2024） | DOSM | 2022–2024 | 馬來文／英文 | https://www.dosm.gov.my/portal-main/downloads-log?id=3253 | 搜尋結果內容（個別月份對應不確定） |
| MY-D73 | （建材價格報導） | Berita Harian | 2023 | 馬來文 | https://www.bharian.com.my/amp/bisnes/lain-lain/2023/03/1074978/bhplus | 搜尋結果內容（對應不確定） |
| MY-D74 | （建材價格報導） | Bernama | 不明（約 2022–2024） | 馬來文 | https://www.bernama.com/bm/news.php?id=2306678 | 搜尋結果內容（對應不確定） |
| MY-D75 | Malaysia's construction material prices creep higher except sand which jumps nearly 15pc, DOSM says | Malay Mail | 2026 | 英文 | https://malaymail.com/news/money/2026/08/10/malaysias-construction-material-prices-creep-higher-except-sand-which-jumps-nearly-15pc-dosm-says/230799 | 搜尋結果內容 |
| MY-D76 | Building materials costs rise in June: DOSM | New Straits Times | 2026 | 英文 | https://www.nst.com.my/amp/business/economy/2026/07/1484256/building-materials-costs-rise-june-dosm | 搜尋結果內容 |
| MY-D77 | Building Cost Index falls in Peninsular Malaysia, rises in Sabah, Sarawak in August – DOSM | The Star | 2026 | 英文 | https://www.thestar.com.my/business/business-news/2026/09/10/building-cost-index-falls-in-peninsular-malaysia-rises-in-sabah-sarawak-in-august---dosm | 搜尋結果內容 |
| MY-D78 | （DOSM 建築與結構工程特別發布，2026 年 4 月資料） | DOSM | 2026 | 英文 | https://www.dosm.gov.my/uploads/release-content/file_20260512121517.pdf | 搜尋結果內容（對應不確定） |
| MY-D79 | Renovation planning, on the go（FAQ） | Qanvast | 現行頁 | 英文 | https://qanvast.com/my/faq | 搜尋結果內容 |
| MY-D80 | Looking To Renovate? This S'pore Startup Helps Match Homeowners To Interior Design Firms | Newswav（轉載） | 約 2021 | 英文 | https://newswav.com/article/A2011_lAcSLj | 搜尋結果內容 |
| MY-D81 | Recommend Group home improvement startup Series A funding | Vulcan Post | 不明 | 英文 | https://vulcanpost.com/767711/recommend-group-home-improvement-startup-series-a-funding | 搜尋結果內容 |
| MY-D82 | Recommend FA（融資公告） | Malaysia Debt Ventures（MDV） | 2021 | 英文 | https://www.mdv.com.my/v3/wp-content/uploads/2021/02/Recommend-FA.pdf | 搜尋結果內容 |
| MY-D83 | Recommend.my（公司資料） | Craft.co | 不明 | 英文 | https://craft.co/recommend-my | 搜尋結果內容 |
| MY-D84 | ARCHIDEX 2025: Where Innovation Met Impact, and a Region Came Together | ARCHIDEX（主辦方） | 2025 | 英文 | https://archidex.com.my/?p=34818 | 搜尋結果內容 |
| MY-D85 | ARCHIDEX 2025 to occupy two venues, MITEC and KLCC, next year | EdgeProp | 2024 | 英文 | https://edgeprop.my/content/1910893/archidex-2025-occupy-two-venues-mitec-and-klcc-next-year | 搜尋結果內容 |
| MY-D86 | （ARCHIDEX 相關報導） | Bernama | 2024–2025 | 英文 | https://www.bernama.com/en/news.php?id=2358978 | 搜尋結果內容（對應不確定） |
| MY-D87 | House renovation in Malaysia | PropCashflow | 2026 | 英文 | https://propcashflow.my/blog/house-renovation-in-malaysia/ | 搜尋結果內容 |
| MY-D88 | （房東翻新指南） | Speedhome | 不明 | 英文 | https://speedhome.com/blog/?p=57025 | 搜尋結果內容 |
| MY-D89 | Renovating Your Home In Malaysia: A Comprehensive Guide | Welcu（轉載） | 2026 | 英文 | https://lb1.welcu.com/core-stories/renovating-your-home-in-malaysia-a-comprehensive-guide-1767648344 | 搜尋結果內容（工期數字與 URL 對應不確定） |
| MY-D90 | Panduan Pembinaan AES 2022（英文版） | DOSM | 2022 | 英文 | https://v1.dosm.gov.my/v1/uploads/files/AES_2022/Panduan-Pembinaan-AES2022-BI.pdf | 搜尋結果內容 |
| MY-D91 | Johor-Singapore SEZ: What you need to know | DHL | 2025 | 英文 | https://www.dhl.com/discover/en-sg/logistics-advice/import-export-advice/johor-singapore-sez-what-you-need-to-know | 搜尋結果內容 |
| MY-D92 | 3装修公司是同一人 18屋主付181万 工程烂尾 | 中國報（柔佛） | 2022 | 華文（馬來西亞） | https://johor.chinapress.com.my/20220414/3%E8%A3%85%E4%BF%AE%E5%85%AC%E5%8F%B8%E6%98%AF%E5%90%8C%E4%B8%80%E4%BA%BA-18%E5%B1%8B%E4%B8%BB%E4%BB%98181%E4%B8%87-%E5%B7%A5%E7%A8%8B%E7%83%82%E5%B0%BE/ | 搜尋結果內容（僅標題） |

### 6.3 台灣與總體錨點來源（引自 r1 TW／TF 筆記，編號不變）

| # | 標題 | 機構 | 年份 | 語言 | URL | 讀取方式 |
|---|---|---|---|---|---|---|
| TW-13 | 全台住宅平均屋齡創新高 澎湖、雲林、嘉義縣「破40年」居冠 | 經濟日報（udn） | 2025 | 中文 | https://money.udn.com/money/story/5621/9014283 | 搜尋結果內容（數字歸屬依標題比對推定，信心中） |
| TW-19 | 老屋翻新 價格 | PRO360 達人網 | 現行頁 | 中文 | https://www.pro360.com.tw/price/old_house_renovation | 搜尋結果內容 |
| TW-21 | 20坪 房屋裝潢 價格 | PRO360 達人網 | 現行頁 | 中文 | https://www.pro360.com.tw/price/20_ping_house_decoration | 搜尋結果內容 |
| TW-22 | 裝潢預算怎麼估？裝修費用怎麼算？ | vocus 方格子 | 2025（推定） | 中文 | https://vocus.cc/article/68429352fd897800016a223d | 搜尋結果內容（出處為推定） |
| TW-23 | 裝修市場熱！年產值上看5500億元 業者曝2026年裝修趨勢 | 聯合新聞網（udn） | 2025／2026 | 中文 | https://udn.com/news/story/7241/9245511 | 搜尋結果內容 |
| TW-30 | 建築管理（100 年統計） | 內政部營建署 | 2011 | 中文 | https://w3.cpami.gov.tw/statisty/100/100_pdf/06_building/0c_building.pdf | 搜尋結果內容 |
| TF-01 | Foreign Exchange Rates – G.5A（Annual），January 05, 2026 | 美國聯邦準備理事會（Board of Governors of the Federal Reserve System） | 2026 | 英 | https://www.federalreserve.gov/releases/g5a/current/ （同版亦見 https://www.federalreserve.gov/releases/g5a/20260105/ ） | 搜尋結果內容 |
| TF-18 | GDP per Capita in Asia (2025) - IMF | Worldometer（轉載 IMF WEO 2026 年 4 月版） | 2026 | 英 | https://www.worldometers.info/gdp/gdp-per-capita/?region=asia&year=2025&metric=nominal | 搜尋結果內容 |
| TF-20 | GDP by Country in Asia (2025) - IMF | Worldometer | 2026 | 英 | https://www.worldometers.info/gdp/gdp-by-country/?region=asia&year=2025&metric=nominal | 搜尋結果內容 |

---

## 7. 附錄：關鍵指標表（CSV）

```csv
market,metric,value,unit,year,source_id,source_url,definition,confidence
MY,室內裝修服務＋安裝工程＋專業建築活動完成工程值,4.8,RM billion,2024,MY-D04,https://theedgemalaysia.com/node/757654,"Smith Zanders（SAG 招股書 IMR）合併口徑；2019 年 RM2.5b；住宅＋商業混合；【實際】",medium
MY,室內裝修（fit-out）單獨口徑,1.2,RM billion,2023,MY-D05,https://cdn1.i3investor.com/my/files/st88k/0360_SAG/pt/RHB/0360_SAG_RHB_2025-05-19_BUY_0.67_SignatureAllianceGroupATrustedInteriorFittingOutSpecialist_-523745964.pdf,"Smith Zanders fit-out 單獨口徑；2020 年 RM791.1m；數字與 URL 對應不確定；【實際】",low
MY,室內裝修行業規模,4.43,RM billion,2024,MY-D12,https://property.enanyang.my/%E8%B6%8B%E5%8A%BF/%E5%AE%A4%E5%86%85%E8%AE%BE%E8%AE%A1%E5%85%B3%E6%80%80%E5%B9%B4%E9%95%BF%E8%80%85%E9%9C%80%E6%B1%82/,"南洋地產引述；定義未說明；2029 年預測 RM5.65b；【示意】",low
MY,家居改善市場,47.7,RM billion,2024,MY-D01,https://www.klsescreener.com/v2/news/view/1748129/malaysian-home-renovation-demand-rising-post-pandemic-on-lifestyle-shift-says-topmix-ceo,"Topmix 執行長引述；含產品的廣義 home improvement；2029 年預測 RM59.2b；【示意】",low
MY,專業工程完成值（四季加總）,21.4,RM billion,2025,MY-16,https://dosm.gov.my/portal-main/release-content/construction-statistics-first-quarter-2025,"DOSM special trade activities 2025Q1–Q4 加總（另見 MY-17～19）；新建＋改建、住宅＋非住宅；上限型代理；【示意】",medium
MY,中古屋占住宅交易比,84.5,%,2025,MY-06,https://www.propplace.my/guides/malaysia-residential-property-market-2025,"NAPIC secondary market 占住宅交易筆數（二手轉述）；【實際】",medium
MY,住宅存量,6.20,million units,2023,MY-D27,https://www.dosm.gov.my/portal-main/release-content/my-local-stats--malaysia-state--administrative-district-2023,"DOSM 引 NAPIC existing residential stock；2022 年 6.08m；排屋占 41.3%；【實際】",high
MY,已完工未售住宅,32800,單位,2026Q1,MY-D28,https://www.malaymail.com/amp/news/malaysia/2026/06/29/housing-mismatch-persists-as-32800-unsold-homes-worth-rm163b-recorded-in-q1-2026-dewan-rakyat-told/225632,"KPKT 國會答詢引 NAPIC；價值 RM16.3b；【實際】",medium
MY,住宅翻修單價-中階,70-150,RM per sq ft,2025,MY-21,https://loanstreet.com.my/learning-centre/how-much-will-home-renovation-cost,"全屋均攤；換算 176–377 USD/m²；÷人均 GDP 1.26–2.70%；【示意】",medium
MY,設計費占工程費比,8-15,%,2026,MY-83,https://www.coohom.com/article/interior-design-pricing-trends-in-malaysia-for-modern-homeowners,"設計公司指南群（MY-83～91）共識區間；【示意】",medium
MY,公寓全屋標準翻修工期,6-10,weeks,2026,MY-D87,https://propcashflow.my/blog/house-renovation-in-malaysia/,"施工期，另加 2–4 週緩衝；計入延誤常見 3–6 個月；業者指南；【示意】",low
MY,LAM 登記室內設計師,606,人,2021-08,MY-D22,https://www.starproperty.my/news/registered-interior-designers-gain-greater-industry-recognition-and-credibility-/121482,"MIID 供稿引 LAM；另有 ID 法人 26、合夥 2、獨資 44；與 MY-60 的 165 人矛盾；【實際】",medium
MY,LAM 登記建築與室內設計顧問事務所,1981,家,約2024,MY-D21,https://repositori.parlimen.gov.my/bitstream/123456789/3521/1/ST.1.2025,"LAM 年報（國會文件）；2022 年 1,891 家；【實際】",medium
MY,G7 本地承包商中登記 B07 室內裝飾類別,907,家,2025-12-01,MY-D14,https://www.chinapress.com.my/20260108/%E5%AE%A4%E5%86%85%E8%A3%85%E4%BF%AE%E5%B7%A5%E7%A8%8B%E5%95%86-egh%E5%9B%BD%E9%99%85%E6%8B%9F%E4%B8%8A%E5%B8%82%E5%88%9B%E4%B8%9A%E6%9D%BF/,"華文財經報導引招股資料；數字與 URL 對應不確定；【實際】",low
MY,Signature Alliance 自稱市占,8.1,%,2025,MY-D04,https://theedgemalaysia.com/node/757654,"執行長說法，非獨立來源；【示意】",low
MY,SAG 上市市值,620,RM million,2025-06,MY-D06,https://www.thestar.com.my/business/business-news/2025/05/15/signature-alliance-targets-rm161mil-from-ipo,"ACE 市場；2.6 億股 × RM0.62；募資 RM161m；【實際】",medium
MY,CIDB 房屋建造與裝修承包商投訴,3201,宗,2018-2025,MY-D43,https://www.enanyang.my/news/20260817/Nation/1351712,"工程部長引 CIDB 累計投訴；【實際】",medium
MY,TTPM 求償上限,50000,RM,2019-10-01 起,MY-49,https://repositori.kpdn.gov.my/bitstream/123456789/3490/1/METRO%2024.09.2019.pdf,"消費者索償仲裁庭上限（由 RM25,000 提高）；【實際】",high
MY,Qanvast Trust 訂金保障上限,50000,RM,現行,MY-D79,https://qanvast.com/my/faq,"平台型訂金保障；Qanvast 2016 年進入馬國；【實際】",medium
MY,Nitori 馬國店數,14,家,2026-03-31,MY-D31,https://in.marketscreener.com/news/nitori-e-ae--ce7f5bddd88af42c,"FY2026 期初店數；計畫增至 21 家（2027-03）；【實際】",medium
MY,HomePro 馬國店數,7,家,2025-12-31,MY-D34,https://lssmedia.setlink.set.or.th/2025/YE/HMPRO-YE68-ListedCompanySnapshot-EN.html,"Home Product Center 年報快照；集團共 133 家；【實際】",high
MY,ARCHIDEX 參觀人次,50668,人次,2025,MY-D84,https://archidex.com.my/?p=34818,"主辦方自報；參展商 850 家以上；2024 年 40,336 人次；【實際】",medium
MY,柔佛新投資,27.4,RM billion,2025Q1,MY-D37,https://www.lexology.com/library/detail.aspx?g=8fcc98a6-ce00-424d-a8dd-78124e95b60a,"JS-SEZ 背景下的柔佛新投資；fit-out 規模無資料；【實際】",medium
MY,新山私有特建辦公入駐率,57.5,%,2025 前後,MY-D39,https://property.enanyang.my/%E8%B6%8B%E5%8A%BF/%E5%A4%A7%E5%9E%8B%E9%A1%B9%E7%9B%AE%E6%8F%90%E6%8C%AF%E6%9F%94%E4%BD%9B%E4%BA%A7%E4%B8%9A%E5%B8%82%E5%9C%BA/,"南洋地產引顧問報告；新樓租金每 sq ft RM3–3.5；【實際】",low
MY,室內設計師平均月薪,3761,RM per month,2026-05,MY-D69,https://malaysia.indeed.com/salaries/interior-designer-Salaries,"Indeed 自報 1,600 筆；吉隆坡 RM4,255；初級 RM2,912；【實際】",medium
MY,熟練印尼籍工人日薪,120-160,RM per day,2025,MY-D64,https://www.enanyang.my/news/20250319/Finance/674217,"一般 RM100；繁重工作有人要求 RM180；【實際】",medium
MY,營建業外勞稅（半島）,1850,RM per year,不明,MY-D62,https://www.mida.gov.my/ms/setting-up-content/pengambilan-pekerja-asing/,"MIDA 頁面；沙巴／砂拉越 RM1,010；未標日期；MTLM 2026 年費率無資料；【實際】",medium
MY,就業准證第 I 類最低月基本薪,20000,RM per month,2026-06-01 起,MY-69,https://www.bakermckenzie.com/en/insight/publications/2026/01/malaysia-expatriate-services-division-increases-employment-pass-salary,"ESD Employment Pass Category I（2025 年舊制 RM10,000）；【實際】",high
MY,鋼筋平均價,3499.50,RM per tonne,2026-07,MY-D75,https://malaymail.com/news/money/2026/08/10/malaysias-construction-material-prices-creep-higher-except-sand-which-jumps-nearly-15pc-dosm-says/230799,"DOSM；年增 0.5–8.4%（霹靂最高）；【實際】",medium
MY,OPC 水泥平均價,25.70,RM per 50kg bag,2026-07,MY-D75,https://malaymail.com/news/money/2026/08/10/malaysias-construction-material-prices-creep-higher-except-sand-which-jumps-nearly-15pc-dosm-says/230799,"DOSM；年增 0.9–7.5%；【實際】",medium
MY,鋼材單價指數年增率,19.9,%,2022-05,MY-D72,https://www.dosm.gov.my/portal-main/downloads-log?id=3253,"DOSM 建材成本指數（2022-05 對 2021-05）；水泥 +12.4%；月份對應不確定；【實際】",medium
MY,每存量住宅單位室內裝修支出（替代錨點）,714.5-774.2,RM per unit,2024,MY-D04,https://theedgemalaysia.com/node/757654,"(RM4.43b～RM4.8b)÷6.20m 單位（MY-D12、MY-D27）；人口無資料的替代分母；【示意】",low
MY,中階單價÷人均GDP,1.26-2.70,%,2025,MY-21,https://loanstreet.com.my/learning-centre/how-much-will-home-renovation-cost,"RM70–150/sq ft×10.7639÷4.2809÷13,949（TF-18）；台灣新成屋中階 1.47–2.46%；【示意】",low
```

> 來源紀律說明：本報告引用的 URL 全部原樣出現在 r1 筆記或本輪 WebSearch 結果中，未構造或修正任何 URL。「對應不確定」表示工具摘要中的數字無法逐字對應到單一結果 URL，已降低信心。所有法規與外資結論都需專業人士最終確認。
