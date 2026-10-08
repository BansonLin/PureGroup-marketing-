# 泰國（Thailand／ประเทศไทย）室內裝修設計市場 — 視角 B：法規證照、消費者保護、外資進入、消費者行為、人才勞動、材料供應鏈、產業組織

- 研究者：Claude（子代理，TH-B）
- 日期：2026-10-08
- 範圍：法規與證照、消費者保護與糾紛、外資進入規則、消費者行為、人才與勞動、材料與供應鏈、產業組織與監測來源
- **執行紀錄（重要，請先讀）**：本輪規劃了 20 次 WebSearch（每個關鍵問題 2–4 次、泰英雙語），但第一批 6 次查詢全部回傳「本輪搜尋額度用罄（limit 200，所有代理共用）」而**未執行**；依環境政策 WebFetch／curl 本來就被封鎖，且規範禁止以其他方式繞過。因此本檔**沒有任何本輪新搜得的資料**。內容分成兩層，請嚴格區分：
  - **【A／B 級｜承襲】**：取自同一工作階段兄弟代理已附 URL 的主題筆記 `04-research-notes/themes/T3-regulation-licensing.md`、`T1-market-size-reconciliation.md`、`T2-business-models.md` 中與泰國相關的片段（T3 自己也註明「依搜尋摘要、未開頁核對」）。這些是本檔唯一可以標【實際】候選的內容。
  - **【D 級｜模型既有知識，未驗證】**：為了讓報告撰寫者看得到「規則的全貌」與正確的法規名稱，我補上以模型既有知識（訓練資料截至 2026-06）整理的法規架構、機構名稱與常見實務，每條都標 `【未驗證】`，URL 僅給**機構入口頁**（確定存在的網域），**不是**該條文或數字所在的頁面。依 `02-integration-protocol.md` 第 2 節，這一層屬 D 級，**不得作為任何【實際】數字的來源**，只能作下一輪搜尋的線索；凡涉及數字（面積門檻、罰金、工資、薪資、人數）者，我只在「有相當把握」時寫出，並一律標低信心；沒有把握的直接列入缺口。
- **資料狀態**：關鍵問題 4（消費者行為）、5（人才與勞動）、6（材料與供應鏈）、7（產業組織）幾乎沒有已附 URL 的數字；第 10 節列出完整缺口與可直接執行的 20 條搜尋計畫，建議使用者另開一輪（或提高 `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`）後重跑。
- 匯率假設（2025–2026 近似值，非官方牌告）：**USD/THB 33.0；USD/TWD 31.5；即 THB 1 ≈ USD 0.0303 ≈ NT$0.955**。T3 筆記換算時用的是約 USD/THB 34，故同一數字兩檔的美元值略有差異，以本檔口徑為準並在表中註明。

---

## 1. 摘要

1. 泰國是本研究 12 個市場中**少數把「室內建築」（สถาปัตยกรรมภายในและมัณฑนศิลป์, Interior Architecture）列為法定管制專業**的國家：依《建築師法 B.E. 2543（2000）》（พระราชบัญญัติสถาปนิก พ.ศ. 2543, Architect Act B.E. 2543）由泰國建築師委員會（สภาสถาปนิก, Architect Council of Thailand, ACT；2000-02-07 成立）管轄建築、室內建築與裝飾、景觀、都市設計四個分支；執照考試以泰文筆試，無照執業有罰金與監禁（T3 承襲，來源：Architect Expo 2023、Bangkok Post 2016、issacompass）。【A/B 級承襲】
2. **施工端沒有承包商執照制度**：泰籍公司承攬住宅裝修無專門執照要求；唯一針對住宅裝修業的消費者法規是消費者保護委員會辦公室（สคบ., OCPB）2023-02-13 公告「住宅裝修業須開立載明法定事項之收據」（公告後 90 日生效）（Tilleke & Gibbins 2023）。【A/B 級承襲】
3. **外資進入屬「實質受限」**：室內設計顧問屬《外國人經營事業法 B.E. 2542（1999）》（Foreign Business Act, FBA）附表三第 (21) 項「其他服務業」，外資持股 ≥50% 須取得外國人經營事業執照（Foreign Business Licence, FBL，法定審查 60 日）；施工承攬（construction）亦屬附表三（僅基礎建設且外資最低資本 ≥5 億泰銖（≈USD 15.2M／NT$4.77 億）例外）；常見替代是 BOI 投資促進或泰資 51% 合資；且提供受管制室內建築服務的公司須向 ACT 登記、董事須有泰籍持照人（BOI OSOS FAQ、UNCTAD、lexbangkok 2026、Tilleke）。T3 給泰國「設計公司 2／承包商 1」的進入可行性分數（1＝幾乎封閉，5＝完全開放）。【A/B 級承襲】
4. 需求面可用的錨點只有：居家修繕產業（含建材零售口徑）**THB 4,795 億（2023，≈USD 145 億／NT$4,580 億）**，2018–2023 CAGR 4.4%（Mr. DIY 泰國 SEC 上市文件）；二手房占住宅交易 **60%**（2025-10，Matichon）；屋齡 ≥10 年住宅逾 **2,340 萬戶**（約 2024，Bangkokbiznews）；但 2025 年為泰國房市 10 年來最艱困的一年，2026 年僅持平（SCB EIC／ttb，Nation）。【A/B 級承襲】
5. 零售整合裝修的參照：HomePro（HMPRO）2024 年總收入 **THB 726.4 億（≈USD 22.0 億／NT$693 億）**、淨利率約 9%，但「Home Service」不分項揭露；Index Living Mall 2024 年營收 THB 98.9 億、毛利率 45.9%（SET 上市公司快照）。【A/B 級承襲】
6. 糾紛面：泰國沒有裝修專屬的投訴統計，只有個案（一承包商詐騙 60 餘名受害人約 4,500 萬泰銖（≈USD 136 萬／NT$4,300 萬），Pattaya Mail、Bangkok Post）；救濟途徑為 OCPB 熱線 1166 與線上申訴。【A/B 級承襲】
7. 以下屬本檔以模型既有知識補充、**全部未驗證**的架構：住宅改建許可依《建築物管制法 B.E. 2522（1979）》（พระราชบัญญัติควบคุมอาคาร พ.ศ. 2522）向地方主管機關申請；瑕疵擔保依《民商法典》（ประมวลกฎหมายแพ่งและพาณิชย์）承攬（จ้างทำของ）章；外國人工作許可依《外國人工作管理敕令 B.E. 2560（2017）》，實務上 1 張工作證對應 4 名泰籍員工與 200 萬泰銖實收資本；2025 年最低工資 337–400 泰銖／日。這些都必須在下一輪重開 URL 核對。【D 級未驗證】

---

## 2. 法規與證照：誰可以合法執業室內設計與施工

### 2.1 室內設計執業管制 —《建築師法 B.E. 2543》與 ACT

| 項目 | 事實 | 等級 | 來源 |
|---|---|---|---|
| 法源 | 《建築師法 B.E. 2543（2000）》（พระราชบัญญัติสถาปนิก พ.ศ. 2543, Architect Act B.E. 2543），取代 1965 年舊法；設立泰國建築師委員會（สภาสถาปนิก, Architect Council of Thailand, ACT），ACT 於 2000-02-07 成立 | A/B 承襲 | [Architect Expo 2023](https://architectexpo.com/2023/en/20103/)；[issacompass](https://www.issacompass.com/insights/architects-and-civil-engineers-why-thai-professional-registration-gates-your-wor) |
| 受管制分支 | 四類受管制建築專業：建築（สถาปัตยกรรมหลัก）、**室內建築與裝飾（สถาปัตยกรรมภายในและมัณฑนศิลป์，對應專業協會 TIDA）**、景觀建築（ภูมิสถาปัตยกรรม，TALA）、都市設計／規劃（สถาปัตยกรรมผังเมือง，TUDA）；設計建築物須持 ACT 執照 | A/B 承襲（分支）；泰文名稱為 D 級補充 | [Architect Expo 2023](https://architectexpo.com/2023/en/20103/)；[ACT 官網入口](https://act.or.th)【未驗證】 |
| 執照取得 | ACT 執照考試（以泰文筆試）；2023 年（B.E. 2566）修法支援 ASEAN Architect 登錄 | A/B 承襲 | [Bangkok Post 2016](https://www.bangkokpost.com/thailand/general/1078432/labour-curbs-split-nations-architects)；[ResearchGate 2025](https://www.researchgate.net/publication/397335482_An_Assessment_of_Legal_Preparedness_for_the_Liberalization_of_Architectural_Services_within_ASEAN) |
| 執照等級 | 個人執照分三級：ภาคีสถาปนิก（Associate Architect，大學畢業後筆試取得）→ สามัญสถาปนิก（Professional Architect，需執業年資與作品審查）→ วุฒิสถาปนิก（Senior Architect）；另有 ภาคีสถาปนิกพิเศษ（Special Associate，針對特定工作範圍）。各分支（含室內建築）各自分級 | D 級【未驗證】 | [ACT 官網入口](https://act.or.th)【未驗證】 |
| 受管制範圍（關鍵） | 受管制的工作內容與建築物門檻由《指定受管制建築專業部令 B.E. 2549（2006）》（กฎกระทรวงกำหนดวิชาชีพสถาปัตยกรรมควบคุม พ.ศ. 2549）規定；室內建築分支依「建築物類型＋室內使用面積」界定（我的記憶是公共建築、大型建築等以室內面積 500 m² 為門檻，但**數字未核對**），一般私人住宅的純裝飾性室內設計是否落入管制，T3 已列為泰國第一缺口 | D 級【未驗證，面積門檻務必核對】 | [Royal Gazette 入口](https://www.ratchakitcha.soc.go.th)【未驗證】；[Council of State 法規庫入口](https://www.krisdika.go.th)【未驗證】 |
| 法人執業 | 提供受管制建築服務的公司須向 ACT 登記取得法人執照；實務上需泰籍持照建築師任董事／股東 | A/B 承襲 | [issacompass](https://www.issacompass.com/insights/architects-and-civil-engineers-why-thai-professional-registration-gates-your-wor) |
| 罰則 | 無照執業：罰金及監禁（T3 承襲）；我的記憶是《建築師法》第 45 條禁止無照執業、第 71 條處**最高 3 年監禁或最高 6 萬泰銖（≈USD 1,818／NT$57,300）罰金或併科**——條號與金額未核對 | A/B 承襲（有罰則）；D 級【金額未驗證】 | [Bangkok Post 2016](https://www.bangkokpost.com/thailand/general/1078432/labour-curbs-split-nations-architects)；[Council of State 法規庫入口](https://www.krisdika.go.th)【未驗證】 |
| 名稱保護 | 「สถาปนิก」（建築師）為受保護名稱；「นักออกแบบตกแต่งภายใน／มัณฑนากร」（室內設計師／裝飾師）一詞本身是否受名稱保護，我沒有把握，列為缺口 | D 級【未驗證】 | — |
| 工程端 | 結構、電機、機械等達一定規模的工程設計與監造屬《工程師法 B.E. 2542（1999）》（พระราชบัญญัติวิศวกร พ.ศ. 2542）下工程師委員會（สภาวิศวกร, Council of Engineers Thailand, COE）管制；住宅改建若涉及結構變更需持照工程師簽證 | D 級【未驗證】 | [COE 官網入口](https://coe.or.th)【未驗證】 |

**推論（Inferences）**
- 泰國與馬來西亞、菲律賓同屬「室內設計本身受專業法管制」的市場，但與馬來西亞不同的是：泰國的管制以「建築物規模門檻」而非「人人皆須註冊」運作，**小型私人住宅裝修很可能落在管制門檻之外**（待核對部令），這也是泰國住宅裝修市場由大量無照「ผู้รับเหมา」（承包商）承作的制度原因。
- 2023 年修法與 ASEAN MRA 僅對 ASEAN 會員國建築師開放登錄；台灣不是 ASEAN 成員，**台灣建築師／室內設計師沒有任何互惠登錄管道**，只能走「泰籍持照者掛名簽證」或 BOI／合資路徑。

### 2.2 施工承攬管制

| 項目 | 事實 | 等級 | 來源 |
|---|---|---|---|
| 承包商執照 | **泰國沒有承包商執照制度**（對比：日本建設業許可、韓國실내건축공사업、台灣室內裝修業登記）；泰籍公司承攬住宅裝修無專門執照要求 | A/B 承襲 | [UNCTAD FBA](https://investmentpolicy.unctad.org/investment-laws/laws/40/thailand-foreign-business-act)；[Tilleke EPC](https://www.tilleke.com/print-insight/?post_id=37170&print=1) |
| 外資承攬 | Construction 屬 FBA 附表三；外資承攬須 FBL，僅「基礎建設且外資最低資本 ≥5 億泰銖（≈USD 15.2M／NT$4.77 億）」例外 | A/B 承襲 | [UNCTAD FBA](https://investmentpolicy.unctad.org/investment-laws/laws/40/thailand-foreign-business-act) |
| 公司登記 | 一般承包商只需向商業發展廳（กรมพัฒนาธุรกิจการค้า, Department of Business Development, DBD）登記公司；DBD 以 TSIC 行業代碼（如 41002 住宅建築、43300 建築物完成與裝修、74100 專業設計）分類，可作企業數監測 | D 級【未驗證】 | [DBD 官網入口](https://www.dbd.go.th)【未驗證】 |
| 政府工程 | 政府採購承包商另有公共工程廳（กรมโยธาธิการและผังเมือง, DPT）等機關的承包商登錄制度，但不適用私人住宅裝修 | D 級【未驗證】 | [DPT 官網入口](https://www.dpt.go.th)【未驗證】 |

### 2.3 住宅改建許可程序 —《建築物管制法 B.E. 2522》【整段 D 級，未驗證】

| 項目 | 我的理解（待核對） | 來源 |
|---|---|---|
| 法源 | 《建築物管制法 B.E. 2522（1979）》（พระราชบัญญัติควบคุมอาคาร พ.ศ. 2522, Building Control Act）：建造（ก่อสร้าง）、**改建（ดัดแปลง）**、拆除（รื้อถอน）、移動建築物須向地方主管機關（เจ้าพนักงานท้องถิ่น；曼谷為各區公所 สำนักงานเขต，其他地區為市鎮／地方行政機構）申請許可 | [DPT 官網入口](https://www.dpt.go.th)【未驗證】 |
| 表單 | 申請書為 ข.1（คำขออนุญาตก่อสร้าง ดัดแปลง รื้อถอน），核發之許可證為 **อ.1**；另有第 39 條之二（มาตรา 39 ทวิ）「通報制」：由持照建築師與工程師簽證後向主管機關通報即可施工，不必等待許可 | 【未驗證】 |
| 何謂「改建」 | 法律定義為變更建築物的結構、重量、面積、形狀、外觀等；**第 11 號部令 B.E. 2528（1985）**列出不視為改建的工作，例如：以相同材料、尺寸更換非結構構件；增減樓地板面積不超過 5 m² 且不增減柱樑；增減屋頂面積不超過 5 m² 等——**換言之一般室內裝飾（油漆、貼磚、天花、櫥櫃、不動結構）通常不需 อ.1 許可**，但拆牆、增建夾層、改變開口與外觀則需要 | 【未驗證，5 m² 門檻務必核對】 |
| 消防 | 消防與逃生規定由《建築物管制法》下各號部令規定（高層與大型建築第 33 號部令 B.E. 2535、消防設備第 39 號部令 B.E. 2537、第 47 號部令 B.E. 2540 既有建築、第 55 號部令 B.E. 2543 建築標準）；室內裝修材料的防火要求以公共建築、娛樂場所為主，**是否有針對住宅室內裝飾材料的專門規定，本輪無法確認** | 【未驗證】 |
| 公寓大廈 | 《公寓大廈法 B.E. 2522（1979）》（พระราชบัญญัติอาคารชุด พ.ศ. 2522，2008 年第 4 次修正）：公寓法人（นิติบุคคลอาคารชุด）依管理規約（ข้อบังคับ）管理；區分所有權人不得變更共用部分；實務上單元內裝修須向法人登記、繳施工保證金、遵守施工時段與電梯使用規定，涉及結構或外觀者須經法人同意並另申請 อ.1 | 【未驗證】 |
| 國宅 | 國家住宅局（การเคหะแห่งชาติ, National Housing Authority, NHA）住宅與「บ้านเอื้ออาทร」等方案的裝修規定本輪未取得 | 缺口 |
| 2023–2026 變化 | 本輪只能確認（承襲）：2023 年 ACT 修法支援 ASEAN Architect；OCPB 2023 住宅裝修收據公告。其他（例如建築物管制法部令修正、EV 充電／太陽能相關改建簡化）**沒有來源** | 缺口 |

---

## 3. 消費者保護與糾紛

### 3.1 已附 URL 的事實【A/B 級承襲】

| 項目 | 事實 | 來源 |
|---|---|---|
| 裝修業受管制公告 | OCPB（สำนักงานคณะกรรมการคุ้มครองผู้บริโภค, สคบ.）2023-02-13 公告：住宅裝修業（residential building renovation business）為「須載明法定事項之收據」管制行業，公告後 90 日生效 | [Tilleke & Gibbins 2023](https://www.tilleke.com/insights/residential-building-renovation-business-in-thailand-to-be-controlled/4/) |
| 訂金上限／履約保證／保固 | 無法定訂金上限、無履約保證制度、無法定裝修保固期（T3 判定） | [Tilleke & Gibbins 2023](https://www.tilleke.com/insights/residential-building-renovation-business-in-thailand-to-be-controlled/4/) |
| 申訴管道 | OCPB 熱線 **1166**、線上申訴 | [Pattaya Mail](https://www.pattayamail.com/thailandnews/thai-consumer-protection-board-tightens-action-in-home-construction-fraud-cases-548874) |
| 投訴統計 | **無裝修分項統計**（T3 判定） | — |
| 詐騙個案 | 一承包商詐騙 60 餘名受害人約 **4,500 萬泰銖（≈USD 136 萬／NT$4,300 萬）**，OCPB 介入 | [Pattaya Mail](https://www.pattayamail.com/thailandnews/thai-consumer-protection-board-tightens-action-in-home-construction-fraud-cases-548874)；[Bangkok Post](https://www.bangkokpost.com/thailand/general/3253094/ocpb-looks-into-construction-scam) |

### 3.2 法律架構補充【D 級，未驗證】

| 項目 | 我的理解（待核對） | 來源 |
|---|---|---|
| 契約類型 | 裝修契約在泰國法上屬《民商法典》第三編第七章「承攬」（จ้างทำของ, Hire of Work，第 587–607 條） | [Council of State 法規庫入口](https://www.krisdika.go.th)【未驗證】 |
| 瑕疵擔保 | 民商法典第 600 條：承攬人對交付後 **1 年內**出現的瑕疵負責；若為建築物或其他土地上工作物則為 **5 年**；第 601 條：請求權自瑕疵出現起 1 年內行使。契約可另行約定（實務上裝修業者常給 1 年保固） | 【未驗證，條號請核對】 |
| 消費者法 | 《消費者保護法 B.E. 2522》（พระราชบัญญัติคุ้มครองผู้บริโภค พ.ศ. 2522）設 OCPB 與契約委員會（คณะกรรมการว่าด้วยสัญญา）、標示委員會（คณะกรรมการว่าด้วยฉลาก），得公告特定行業為「受管制契約」或「受管制收據」行業——2023 年裝修業公告即屬後者 | 【未驗證】 |
| 不公平契約 | 《不公平契約條款法 B.E. 2540（1997）》（พระราชบัญญัติว่าด้วยข้อสัญญาที่ไม่เป็นธรรม）：法院得宣告顯失公平之條款僅在合理範圍內有效 | 【未驗證】 |
| 消費訴訟 | 《消費者案件程序法 B.E. 2551（2008）》（พระราชบัญญัติวิธีพิจารณาคดีผู้บริโภค）：消費者對業者提告免裁判費、程序簡化、舉證責任轉換 | 【未驗證】 |
| 常見詐騙模式 | 泰文媒體常用語「ผู้รับเหมาทิ้งงาน」（承包商收訂金後棄工）、「ช่างทิ้งงาน」；典型型態：以低價報價吸引 → 收 30–50% 訂金 → 進場做部分拆除後消失；另有以臉書／LINE 社團攬客的無登記個人承包商。**比例與金額無來源** | 【未驗證，定性描述】 |
| 付款慣例 | 實務常見分期：簽約 30%（或 20–50%）→ 進場／材料 30% → 中期 30% → 完工驗收 10%（**無來源，僅業界常見說法**） | 【未驗證】 |
| 保險 | 泰國沒有類似日本「リフォーム瑕疵保險」的裝修瑕疵保險制度；大型承包商投保工程一切險（CAR）為自願 | 【未驗證】 |

**推論**
- 泰國消費者保護的「硬制度」幾乎只有 2023 年的收據公告，比新加坡（CaseTrust 訂金 ≤20%＋履約保證）、台灣（定型化契約草案）弱得多；這意味著**「可信賴的品牌＋透明合約＋分期付款」本身就是可差異化的賣點**，也是 HomePro 等零售商以「Home Service」切入的制度空隙。

---

## 4. 外資進入規則

### 4.1 已附 URL 的事實【A/B 級承襲】

| 項目 | 事實 | 來源 |
|---|---|---|
| 設計公司 | 室內設計顧問屬 FBA 附表三第 (21) 項「其他服務業」；外資持股 ≥50% 須向 DBD 申請外國人經營事業執照（FBL），法定審查 60 日；常見替代為 BOI 投資促進（取得 Foreign Business Certificate）或泰資 51% 合資 | [BOI OSOS FAQ](https://osos.boi.go.th/One-Stop/faq-group/24/To-open-a-branch-office-to-do-interior-design-consulting-in-Thailand/)；[UNCTAD FBA](https://investmentpolicy.unctad.org/investment-laws/laws/40/thailand-foreign-business-act)；[thailaws.org](https://www.thailaws.org/foreign-business-act/)；[lexbangkok 2026](https://lexbangkok.com/foreign-business-act-thailand-market-entry-guide-2026/) |
| 承包商 | Construction 屬附表三；僅基礎建設且外資最低資本 ≥5 億泰銖（≈USD 15.2M／NT$4.77 億）例外；實務需泰資多數合資 | [UNCTAD FBA](https://investmentpolicy.unctad.org/investment-laws/laws/40/thailand-foreign-business-act)；[Tilleke EPC](https://www.tilleke.com/print-insight/?post_id=37170&print=1) |
| 外國設計師 | 室內建築須 ACT 執照；外國人實務上極難取得（泰文考試）；公司向 ACT 登記需泰籍持照者任董事 | [issacompass](https://www.issacompass.com/insights/architects-and-civil-engineers-why-thai-professional-registration-gates-your-wor)；[Bangkok Post 2016](https://www.bangkokpost.com/thailand/general/1078432/labour-curbs-split-nations-architects) |
| 分公司 | BOI OSOS FAQ 針對「在泰國開設分公司做室內設計顧問」有專頁說明（內容未開頁核對） | [BOI OSOS FAQ](https://osos.boi.go.th/One-Stop/faq-group/24/To-open-a-branch-office-to-do-interior-design-consulting-in-Thailand/) |
| 貿易協定 | 泰國為 WTO 會員、非 CPTPP 成員；ASEAN 建築服務 MRA 僅對 ASEAN 會員國開放 | [ResearchGate 2025](https://www.researchgate.net/publication/397335482_An_Assessment_of_Legal_Preparedness_for_the_Liberalization_of_Architectural_Services_within_ASEAN) |
| T3 可行性評分 | 設計公司 2／承包商 1（1＝幾乎封閉，5＝完全開放） | T3 分析師判斷 |

### 4.2 架構補充【D 級，未驗證】

| 項目 | 我的理解（待核對） | 來源 |
|---|---|---|
| FBA 最低資本 | 外國人經營非附表事業最低資本 **200 萬泰銖（≈USD 60,606／NT$191 萬）**；經營附表二／三事業（需 FBL）最低資本 **300 萬泰銖（≈USD 90,909／NT$286 萬）** | [DBD 官網入口](https://www.dbd.go.th)【未驗證】 |
| 附表三其他相關項目 | 附表三另列「建築服務」（architectural services）、「工程服務」（engineering services）、「建設」（construction，含例外）；即使以泰資 51% 合資，若公司提供受管制建築服務仍須 ACT 法人登記 | 【未驗證】 |
| 人頭股東 | 以泰籍人頭（nominee）持 51% 規避 FBA 為違法，DBD 近年持續稽查（2024–2025 多次新聞）；對台商而言「真實合資＋股東協議／特別股設計」是合規路徑 | 【未驗證】 |
| 美泰友好條約 | Treaty of Amity 僅適用美國籍公司，與台灣無關 | 【未驗證】 |
| BOI | BOI 促進類別中與設計相關者偏向「工業設計／工程設計中心」與「區域總部／國際商業中心（IBC）」，一般室內設計顧問是否可促進，**T3 寫「BOI 可促進」但本輪未能核對類別** | [BOI 官網入口](https://www.boi.go.th)【未驗證】 |
| 工作許可 | 《外國人工作管理敕令 B.E. 2560（2017）》（พระราชกำหนดการบริหารจัดการการทำงานของคนต่างด้าว พ.ศ. 2560，2018 年修正）；就業廳（กรมการจัดหางาน, Department of Employment, DOE）實務比例：**每 1 張外國人工作證需 4 名泰籍全職員工＋200 萬泰銖實收資本**（BOI 促進公司可豁免比例） | [DOE 官網入口](https://www.doe.go.th)【未驗證】 |
| 外國人禁止從事職業 | 勞動部公告（B.E. 2563／2020）列 40 項職業分四類：絕對禁止、有條件開放（MOU 移工可做之體力工、泥作、木工等建築工）、僅依國際協定／MRA 開放（含**建築設計、繪圖、估價、監造**與土木工程）、…。意即**外籍室內設計師若從事「受管制建築工作」須依 MRA＋ACT 執照；台灣人沒有 MRA 管道**，實務上以「設計顧問／專案經理」職稱申請工作證，由泰籍持照者簽證 | [MOL 官網入口](https://www.mol.go.th)【未驗證，分類與項目務必核對】 |
| 工地主任 | 外籍工地主任（site manager）可申請一般工作證（非禁止職業），但需滿足 4:1 比例與資本要求；短期派駐可用「緊急工作通知（Urgent Work, ≤15 日）」 | 【未驗證】 |
| 稅務（僅提示，不構成建議） | 公司所得稅 20%；VAT 7%；境內服務費扣繳 3%；支付境外公司服務費扣繳 15%（可依租稅協定減免）；台泰有避免雙重課稅協定（我的記憶：1999 年簽署、2012 年生效，**請核對**）；設計費若由台灣母公司開立，需留意常設機構與移轉訂價 | [Revenue Department 入口](https://www.rd.go.th)【未驗證】 |

### 4.3 已進入泰國的外國業者【D 級，全部未驗證，僅供搜尋線索】

| 業者 | 國籍 | 我的理解 | 狀態 |
|---|---|---|---|
| 乃村工藝社（Nomura Co., Ltd.） | 日本 | 設有泰國子公司（Nomura Design & Engineering (Thailand)），承接日系零售、飯店、商業空間裝修 | 【未驗證】 |
| 丹青社（Tanseisha） | 日本 | 設有泰國子公司承接商業空間 | 【未驗證】 |
| Nitori（ニトリ） | 日本 | 2023 年在曼谷開泰國首店，走家具家飾零售 | 【未驗證】（VN-A 筆記引用 Nikkei 提及「泰國、越南新店」） |
| IKEA（Ikano Retail） | 瑞典／新加坡經營 | 2011 年曼谷 Bangna 首店；後有 Bang Yai 等店 | 【未驗證】 |
| Space Matrix | 新加坡 | 曼谷辦公室，商辦室內設計 | 【未驗證】 |
| HBA（Hirsch Bedner Associates） | 美國 | 曼谷辦公室，飯店室內設計 | 【未驗證】 |
| 台灣業者 | 台灣 | **沒有找到任何有來源的台灣室內設計／裝修公司進入泰國案例**；台商在泰以製造業與建材（如板材、五金）為主 | 缺口 |
| 韓國、中國業者 | 韓／中 | 中國定製家具品牌（如歐派、索菲亞）是否以經銷商形式進入曼谷，**無來源** | 缺口 |

**推論**
- 對台灣業者最現實的三條路：(1) **泰資 51% 真實合資**（設計＋施工各一家或一家兩業），以台方技術與供應鏈換取泰籍持照建築師與工班；(2) **BOI 促進**（需確認類別，可能需以「設計中心／IBC」包裝）；(3) **不做執業、改做供應鏈與零售**（系統櫃、衛浴、五金、板材的進口與展示中心）——零售與貿易受 FBA 附表三「零售（最低資本 1 億泰銖）」另一套規則管制，需另行研究。

---

## 5. 消費者行為

### 5.1 已附 URL 的事實【A/B 級承襲】

| 指標 | 數值 | 年份 | 來源 | 信心 |
|---|---|---|---|---|
| 居家修繕產業規模（含建材零售口徑） | THB 3,862 億（2018）→ **THB 4,795 億（2023）**，CAGR 4.4%；≈USD 145 億／NT$4,580 億 | 2023 | [泰國 SEC Mr. DIY 上市文件](https://market.sec.or.th/public/ipos/IPOSGetFile.aspx?TransID=646423&TransFileSeq=87) | 中（獨立顧問，HI 口徑） |
| 二手房占住宅交易 | **60%**，成長快於新屋（Modern Property Consultant） | 2025-10 | [Matichon](https://www.matichon.co.th/economy/news_5437496)；[REIC 轉載](https://www.reic.or.th/News/RealEstate/470359) | 中 |
| 屋齡 ≥10 年住宅 | **逾 2,340 萬戶**（翻修潛在存量） | 約 2024 | [Bangkokbiznews](https://www.bangkokbiznews.com/property/1124831) | 中 |
| 房市景氣 | 2025 年為 10 年來最艱困；2026 年持平或微增（SCB EIC／ttb analytics） | 2025–2026 | [Nation](https://www.nationthailand.com/business/property/40056158)；[Nation 2027](https://www.nationthailand.com/business/economy/40070934)；[SCB EIC](https://www.scbeic.com/en/detail/product/443) | 高 |
| REIC | 2025 Q4 住宅市場因政府措施觸底回穩 | 2025 | [REIC Q4（轉載）](https://www.bangkokfocusnews.com/2026/02/REIC-Q4-2568-Trends2569.html)；[REIC Q1](https://www.reic.or.th/Activities/PressRelease/260) | 高 |
| 零售通路 | HomePro 2024 總收入 THB 726.4 億（≈USD 22.0 億／NT$693 億），淨利約 THB 64–65 億（淨利率 ≈9%），Home Service 不分項 | 2024 | [SET HMPRO 快照](https://lssmedia.setlink.set.or.th/2025/3M/HMPRO-3M68-ListedCompanySnapshot-EN.html)；[Kaohoon](https://www.kaohooninternational.com/markets/537124) | 中高 |
| 零售通路 | Index Living Mall 2024 營收 THB 98.9 億（≈USD 3.0 億／NT$94 億），毛利率 45.9%，淨利率 7.5%，34 店 | 2024 | [SET ILM 快照](https://lssmedia.setlink.set.or.th/2024/YE/ILM-YE67-ListedCompanySnapshot-EN.html)；[ILM IR](https://investor.indexlivingmall.com/en/updates/press-releases/416/index-living-mall-reports-strong-2024-performance-with-recordhigh-profit-for-the-third-consecutive-year-proposes-thb-100-dividend-per-share) | 高 |

### 5.2 政策與融資補充【D 級，未驗證】

| 項目 | 我的理解（待核對） | 來源 |
|---|---|---|
| 翻修貸款 | 政府住宅銀行（ธนาคารอาคารสงเคราะห์, Government Housing Bank, GHB／ธอส.）長期提供「ต่อเติม／ซ่อมแซม」（增建／修繕）房貸與專案優惠利率；商業銀行（SCB、KBank、Krungsri、TTB）亦有「สินเชื่อตกแต่งบ้าน」（裝修貸款），多以房屋抵押加貸或個人信貸形式 | [GHB 官網入口](https://www.ghbank.co.th)【未驗證】 |
| 2025 年房市措施 | 2025-04 起過戶費與抵押登記費降至 0.01%（房價 ≤700 萬泰銖，≈USD 21.2 萬／NT$668 萬），至 2026-06-30；泰國央行（BOT）2025-05 起暫時放寬 LTV 至 100%（至 2026-06-30） | [BOT 官網入口](https://www.bot.or.th)【未驗證】 |
| 租稅誘因 | 「Easy E-Receipt 2.0」（2025-01-16～02-28）：持電子稅務發票之消費可扣除最高 5 萬泰銖（≈USD 1,515／NT$47,750），含向 VAT 登記業者購買的裝修服務；2024 年底曾有洪災房屋修繕支出扣除（最高 10 萬泰銖，≈USD 3,030／NT$95,500）——**是否延續至 2026 年未確認** | [Revenue Department 入口](https://www.rd.go.th)【未驗證】 |
| 誰在裝修 | 可推論的結構：二手房占六成＋2,340 萬戶 ≥10 年屋齡 → **二手房入住前翻修與高齡化住宅改修**為主力；曼谷公寓（คอนโด）租賃投資客的「แต่งคอนโดปล่อยเช่า」（裝修出租）為第二類；新建透天（บ้านจัดสรร）交屋後「ต่อเติมครัวหลังบ้าน」（增建後廚房）是泰國特有的高頻需求 | 推論＋【未驗證】 |
| 資訊來源 | บ้านและสวน（Baan Lae Suan，Amarin 集團）雜誌、網站與年度博覽會；Pantip（ห้องชายคา 版）；臉書社團；Pinterest；HomePro／Index 門市設計服務；房產平台 DDproperty、Baania、Think of Living | 【未驗證，定性】 |
| 風格偏好 | 曼谷主流為 Modern／Minimal、Muji-Japandi、Loft（工業風）；高端走 Modern Luxury、Thai-contemporary（泰式當代）——**無調查數據** | 缺口 |
| 預算分級 | **無來源**；泰國媒體常用「งบตกแต่ง 1 แสน／5 แสน／1 ล้าน」分級，無統計 | 缺口 |

---

## 6. 人才與勞動【整節 D 級，未驗證；無任何本輪 URL】

| 項目 | 我的理解（待核對） | 來源 |
|---|---|---|
| 教育管道 | 室內建築／室內設計學程集中在：朱拉隆功大學建築學院（室內建築系）、國立藝術大學（Silpakorn）裝飾藝術學院（คณะมัณฑนศิลป์，泰國歷史最久的室內設計／裝飾學院）、拉卡邦先皇技術學院（KMITL）建築學院、吞武里先皇科技大學（KMUTT）建築與設計學院、法政大學建築與規劃學院、清邁大學、孔敬大學、蘭實大學（Rangsit）、曼谷大學、易三倉大學（Assumption）、斯巴頓大學（Sripatum）、各拉差蒙坤科技大學（RMUT）體系等；ACT 對「可報考執照」之學程有認證名單 | [ACT 官網入口](https://act.or.th)【未驗證】 |
| 畢業人數 | **無來源** | 缺口 |
| 持照人數 | ACT 各分支持照人數（室內建築分支）**無來源**；ACT 網站有統計頁 | 缺口 |
| 設計師薪資 | 業界常見區間（求職網 JobsDB／Adecco 薪資指南）：初階室內設計師約 THB 18,000–25,000／月（≈USD 545–758／NT$17,200–23,900）、中階 30,000–50,000、資深／主管 60,000–100,000+；**數字為記憶區間，未核對** | 缺口（低信心） |
| 工地主任薪資 | **無來源** | 缺口 |
| 最低工資 | 2025-01-01 起全國日薪 **337–400 泰銖**（≈USD 10.2–12.1／NT$322–382）；曼谷及周邊 372 泰銖；普吉、春武里、羅勇、北柳、蘇美島 400 泰銖；2025-07-01 起曼谷等地提高至 400 泰銖（適用範圍待核對）；2026 年是否再調整**未確認** | [MOL 官網入口](https://www.mol.go.th)【未驗證】 |
| 技術工日薪 | 市場行情（曼谷）木工、泥作、貼磚、水電師傅約 THB 500–1,000／日（≈USD 15–30／NT$478–955），依技術等級差異大；勞動部另有「技能標準工資」（อัตราค่าจ้างตามมาตรฐานฝีมือ）對建築工種分級定價——**數字未核對** | 缺口（低信心） |
| 缺工與高齡化 | 泰國營建業長期依賴緬甸、柬埔寨、寮國（近年加越南）MOU 移工；泰籍工班高齡化、年輕人不願入行為業界共識；**缺工比例、工班平均年齡無來源** | 缺口 |
| 移工政策 | 依 2017 年敕令與內閣決議，營建工屬允許移工從事的職業；透過 MOU（緬、柬、寮、越）或登記核准；登記移工總數約 300 萬級（**數字未核對**）；2025 年緬甸情勢影響供給 | [DOE 官網入口](https://www.doe.go.th)【未驗證】 |
| 勞動統計 | 國家統計局（สำนักงานสถิติแห่งชาติ, NSO）勞動力調查（LFS）有營建業就業人數（我的記憶約 200–230 萬人，**未核對**） | [NSO 官網入口](https://www.nso.go.th)【未驗證】 |

---

## 7. 材料與供應鏈【整節 D 級，未驗證；零售商財報為 A/B 級承襲】

| 類別 | 主要本地品牌／通路（我的理解） | 備註 |
|---|---|---|
| 磁磚、衛浴 | **SCG Decor PCL**（SET: SCGD，2023 年底上市，旗下 COTTO、Sosuco、Campana，並持有越南 Prime、菲律賓 Mariwasa）；**Dynasty Ceramic**（SET: DCC，平價磁磚龍頭）；**RCI（Royal Ceramic）**；衛浴另有 American Standard（Lixil）、Karat（Kohler）、Nahm、Mogen | 【未驗證】 |
| 塗料 | **TOA Paint**（SET: TOA，市占第一）、Beger、Jotun、Nippon Paint、Captain | 【未驗證】 |
| 廚具、系統櫃 | **Starmark**（Index Living Mall 關係企業）、**Modernform**（SET: MODERN，辦公家具＋廚具）、Kitchen Form、SB Design Square（SB Furniture）、Koncept、Index Living Mall、IKEA；高端進口 Bulthaup、Poggenpohl | 【未驗證】 |
| 木材、板材 | 泰國橡膠木（ไม้ยางพารา）為主要本地實木；Vanachai（MDF／PB）、Metro-Ply、Panel Plus（Mitr Phol 集團）；美耐板 Formica Thailand、Wilsonart、TAK | 【未驗證】 |
| 照明 | **Lighting & Equipment PCL（L&E）**、Lamptan、Philips／Signify Thailand、Panasonic | 【未驗證】 |
| 家居建材零售 | HomePro（含 Mega Home）、Thai Watsadu（Central Retail）、Global House（SET: GLOBAL）、Dohome（SET: DOHOME）、Boonthavorn（บุญถาวร）、Mr. DIY Thailand、Index Living Mall、SB Design Square | 財報見第 5 節【A/B 承襲】 |
| 進口依賴 | 磁磚、衛浴、塗料、板材本地供應充足；高端五金、系統廚具、燈具、智能家居依賴進口（中國、歐洲、日本）；中國低價磁磚、燈具、家具進口壓力大（泰國曾對中國磁磚課反傾銷稅，**年份與稅率未核對**） | 【未驗證】 |
| 標準 | 泰國工業標準院（สำนักงานมาตรฐานผลิตภัณฑ์อุตสาหกรรม, TISI）TIS 標準，部分建材（如鋼筋、水泥、電線、衛浴陶瓷）為強制標準（มอก. บังคับ）；進口須符合 | [TISI 官網入口](https://www.tisi.go.th)【未驗證】 |
| 關稅 | 台灣建材進口泰國適用 MFN 稅率（多數建材 5–30%）；台泰無 FTA；中國、日本、韓國、ASEAN 產品享 FTA 優惠，**台灣產品在價格上處於結構劣勢** | 【未驗證】 |
| 價格指數 | 商務部貿易政策與戰略辦公室（สำนักงานนโยบายและยุทธศาสตร์การค้า, TPSO）每月發布**建材價格指數（ดัชนีราคาวัสดุก่อสร้าง, Construction Materials Price Index）**，分 11 大類（木材、水泥、鋼材、磁磚、衛浴、電器設備等）；2022 年因鋼材、能源大漲，2023–2025 趨於持平或微跌（**各年數字未核對**） | [TPSO 官網入口](https://www.tpso.go.th)；[價格指數入口](https://www.price.moc.go.th)【未驗證】 |
| 物流 | 曼谷都會區建材配送成熟；外府由 Global House、Dohome、Thai Watsadu 的大店覆蓋；公寓大廈搬運受法人時段與電梯限制 | 【未驗證】 |

---

## 8. 產業組織與監測來源【D 級為主；標註者為 A/B 承襲】

| 類型 | 名稱 | 說明 | 等級 |
|---|---|---|---|
| 法定機構 | 泰國建築師委員會（สภาสถาปนิก, ACT） | 執照、法人登記、紀律 | A/B（存在）；[act.or.th](https://act.or.th) 入口【未驗證】 |
| 專業協會 | 暹羅建築師協會（สมาคมสถาปนิกสยาม ในพระบรมราชูปถัมภ์, ASA）；**泰國室內設計師協會（สมาคมมัณฑนากรแห่งประเทศไทย, Thailand Interior Designers' Association, TIDA）**；泰國景觀建築師協會（TALA）；泰國都市設計師協會（TUDA） | 四協會與 ACT 共同主辦 Architect Expo；TIDA 辦 TIDA Awards 與學生競賽 | A/B（[Architect Expo 2023](https://architectexpo.com/2023/en/20103/)）；[asa.or.th](https://asa.or.th)【未驗證】 |
| 營建協會 | 泰國營造業協會（สมาคมอุตสาหกรรมก่อสร้างไทย ในพระบรมราชูปถัมภ์, Thai Contractors Association, TCA）；住宅建造業協會（สมาคมธุรกิจรับสร้างบ้าน, Home Builder Association, HBA）——HBA 每年公布「รับสร้างบ้าน」（委建住宅）市場規模與展會 | 【未驗證】 | D |
| 家具協會 | 泰國家具工業協會（สมาคมอุตสาหกรรมเครื่องเรือนไทย, TFA）；與 DITP 合辦 TIFF | 【未驗證】 | D |
| 展會 | **Architect Expo（งานสถาปนิก）**：每年 4–5 月，IMPACT Muang Thong Thani，ASA 主辦、TTF 承辦，東南亞最大建築建材展；**บ้านและสวนแฟร์（Baan Lae Suan Fair）**：Amarin 主辦，年底消費者家居展；**Thailand International Furniture Fair（TIFF）**與 **STYLE Bangkok**（DITP）；**HomePro Expo**；**Bangkok Design Week**（CEA，1–2 月）；BMAM／Thailand Building Fair | Architect Expo 為 A/B（網站存在）；其餘【未驗證】 | 混合 |
| 媒體 | บ้านและสวน（Baan Lae Suan）、room（Amarin）、art4d、Dsign Something、Wazzadu（建材平台）、ประชาชาติธุรกิจ（Prachachat）與ฐานเศรษฐกิจ（Thansettakij）房產版、Bangkok Post／Nation 房產版 | 【未驗證】 | D |
| 統計與研究 | REIC（ศูนย์ข้อมูลอสังหาริมทรัพย์，住宅市場季報；A/B 承襲）；SCB EIC、Krungsri Research、Kasikorn Research（KResearch）、ttb analytics（產業報告）；TPSO 建材價格指數；NSO 勞動力調查；BOT 房貸與 LTV；DBD DataWarehouse（企業登記數）；泰國 SEC 上市文件（HomePro、Index、SCGD、Mr. DIY） | REIC／SCB EIC／SET／SEC 為 A/B 承襲；其餘入口【未驗證】 | 混合 |

---

## 9. 關鍵數字總表

| 指標 | 數值 | 年份 | 來源 | 定義／備註 | 信心 |
|---|---|---|---|---|---|
| 居家修繕產業規模 | THB 4,795 億 ≈ USD 145 億 ≈ NT$4,580 億（2018：THB 3,862 億；CAGR 4.4%） | 2023 | [泰國 SEC Mr. DIY 上市文件](https://market.sec.or.th/public/ipos/IPOSGetFile.aspx?TransID=646423&TransFileSeq=87) | 獨立顧問 HI 口徑（含建材零售），高估純翻修；承襲 T1 | 中 |
| 二手房占住宅交易 | 60% | 2025-10 | [Matichon](https://www.matichon.co.th/economy/news_5437496) | Modern Property Consultant 說法；承襲 T1 | 中 |
| 屋齡 ≥10 年住宅 | >2,340 萬戶 | 約 2024 | [Bangkokbiznews](https://www.bangkokbiznews.com/property/1124831) | 翻修潛在存量；承襲 T1 | 中 |
| 房市景氣 | 2025 年 10 年最差；2026 持平 | 2025–26 | [Nation](https://www.nationthailand.com/business/property/40056158)；[SCB EIC](https://www.scbeic.com/en/detail/product/443) | 承襲 T1 | 高 |
| HomePro 總收入 | THB 726.4 億 ≈ USD 22.0 億 ≈ NT$693 億；淨利率 ≈9% | 2024 | [SET HMPRO](https://lssmedia.setlink.set.or.th/2025/3M/HMPRO-3M68-ListedCompanySnapshot-EN.html) | Home Service 不分項；承襲 T2（T2 以 USD/TWD 32 換算為 NT$682 億） | 中高 |
| Index Living Mall 營收／毛利率 | THB 98.9 億 ≈ USD 3.0 億 ≈ NT$94 億；毛利率 45.9%；淨利率 7.5% | 2024 | [SET ILM](https://lssmedia.setlink.set.or.th/2024/YE/ILM-YE67-ListedCompanySnapshot-EN.html) | 34 店；承襲 T2 | 高 |
| FBA 建設例外門檻 | 外資最低資本 ≥THB 5 億 ≈ USD 15.2M ≈ NT$4.77 億（基礎建設） | 現行 | [UNCTAD](https://investmentpolicy.unctad.org/investment-laws/laws/40/thailand-foreign-business-act) | 承襲 T3（T3 換算 USD 14.7M） | 高 |
| FBL 法定審查期 | 60 日 | 現行 | [thailaws.org](https://www.thailaws.org/foreign-business-act/) | 承襲 T3 | 高 |
| 室內設計顧問 FBA 歸類 | 附表三第 (21) 項其他服務業；外資 ≥50% 須 FBL | 現行 | [BOI OSOS FAQ](https://osos.boi.go.th/One-Stop/faq-group/24/To-open-a-branch-office-to-do-interior-design-consulting-in-Thailand/)；[lexbangkok 2026](https://lexbangkok.com/foreign-business-act-thailand-market-entry-guide-2026/) | 承襲 T3 | 高 |
| ACT 成立日 | 2000-02-07 | 2000 | [Architect Expo 2023](https://architectexpo.com/2023/en/20103/) | 承襲 T3 | 高 |
| ACT 修法支援 ASEAN Architect | B.E. 2566（2023） | 2023 | [ResearchGate 2025](https://www.researchgate.net/publication/397335482_An_Assessment_of_Legal_Preparedness_for_the_Liberalization_of_Architectural_Services_within_ASEAN) | 承襲 T3 | 中 |
| OCPB 裝修業收據公告 | 2023-02-13 公告，90 日後生效 | 2023 | [Tilleke 2023](https://www.tilleke.com/insights/residential-building-renovation-business-in-thailand-to-be-controlled/4/) | 承襲 T3 | 高 |
| 裝修詐騙個案 | 60 餘名受害人、約 THB 4,500 萬 ≈ USD 136 萬 ≈ NT$4,300 萬 | 約 2025 | [Pattaya Mail](https://www.pattayamail.com/thailandnews/thai-consumer-protection-board-tightens-action-in-home-construction-fraud-cases-548874) | 個案非統計；承襲 T3 | 中 |
| OCPB 熱線 | 1166 | 現行 | [Pattaya Mail](https://www.pattayamail.com/thailandnews/thai-consumer-protection-board-tightens-action-in-home-construction-fraud-cases-548874) | 承襲 T3 | 高 |
| T3 進入可行性評分 | 設計公司 2／承包商 1（1–5） | 2026 | T3 分析師判斷 | 非數據 | — |
| FBA 最低資本 | THB 200 萬（一般）／300 萬（附表二、三）≈ USD 60,606／90,909 ≈ NT$191 萬／286 萬 | 現行 | [DBD 入口](https://www.dbd.go.th)【未驗證】 | D 級記憶 | 低 |
| 工作證比例 | 1 工作證：4 泰籍員工＋THB 200 萬實收資本 | 現行 | [DOE 入口](https://www.doe.go.th)【未驗證】 | D 級記憶，DOE 實務 | 低 |
| 無照執業罰則 | 最高 3 年監禁或 THB 6 萬（≈USD 1,818／NT$57,300）罰金 | 現行 | [Krisdika 入口](https://www.krisdika.go.th)【未驗證】 | D 級記憶（建築師法 §45／§71） | 低 |
| 民商法典瑕疵擔保 | 1 年；建築物／土地上工作物 5 年（§600） | 現行 | [Krisdika 入口](https://www.krisdika.go.th)【未驗證】 | D 級記憶 | 低 |
| 最低工資 | THB 337–400／日 ≈ USD 10.2–12.1 ≈ NT$322–382；曼谷 372（2025-01）→ 400（2025-07，範圍待核） | 2025 | [MOL 入口](https://www.mol.go.th)【未驗證】 | D 級記憶 | 低 |
| 設計師月薪區間 | 初階 THB 18,000–25,000 ≈ USD 545–758 ≈ NT$17,200–23,900 | 2025 | 無 URL | D 級記憶，求職網區間 | 低 |
| 技術工日薪 | THB 500–1,000 ≈ USD 15–30 ≈ NT$478–955 | 2025 | 無 URL | D 級記憶 | 低 |
| 2025 房市措施 | 過戶費 0.01%（≤THB 700 萬 ≈ USD 21.2 萬／NT$668 萬）至 2026-06；LTV 100% 至 2026-06 | 2025–26 | [BOT 入口](https://www.bot.or.th)【未驗證】 | D 級記憶 | 低 |
| Easy E-Receipt 2.0 扣除額 | THB 50,000 ≈ USD 1,515 ≈ NT$47,750 | 2025 | [RD 入口](https://www.rd.go.th)【未驗證】 | D 級記憶 | 低 |

---

## 10. 對台灣業者的啟示

1. **泰國是「設計受管制、施工不受管制」的倒置市場**：與台灣（業者登記制）相反，泰國住宅裝修施工端沒有執照門檻，但「室內建築」設計在建築物規模門檻以上須 ACT 持照人簽證。對台灣業者而言，**施工與工班管理能力可以直接輸出，設計簽證必須借泰籍持照者**；合資夥伴的選擇應優先找「有 ACT 室內建築分支持照建築師的事務所」而非純施工承包商。
2. **外資結構要一開始就設計成合規的 51/49**：FBA 附表三同時涵蓋設計顧問與施工，FBL 審批不確定且 60 日起跳；人頭持股被 DBD 稽查。可行結構是泰方 51%（真實出資）＋台方 49%＋股東協議（董事席次、特別股、技術授權費）；或以 BOI 促進類別（須先確認室內設計是否符合）取得 Foreign Business Certificate。**在未確認 BOI 類別前，不要假設可 100% 持有。**
3. **消費者保護真空是品牌機會**：泰國只有 2023 年「收據載明事項」公告，沒有訂金上限、履約保證、法定保固或裝修瑕疵保險；「ผู้รับเหมาทิ้งงาน」是消費者最大的恐懼。台灣業者若把台灣的定型化契約、分期付款、1 年保固（甚至第三方履約保證）制度化並以中英泰三語呈現，可在曼谷中高端市場形成明確差異；HomePro 的 Home Service 已證明「可信賴通路」有需求但未分項揭露獲利。
4. **需求結構對台灣經驗友善但景氣正差**：二手房占六成、2,340 萬戶 ≥10 年屋齡、公寓投資客裝修出租，都與台灣「中古屋翻修為主」的經驗相近；但 2025 年是泰國房市 10 年最差、2026 僅持平，進入時點宜以「翻修需求不受新屋滯銷影響」為論述，並避開新建案配套裝修。
5. **供應鏈切入可能比執業切入更快**：泰國本地磁磚、衛浴、塗料、板材強勢（SCG Decor、Dynasty、TOA），但系統櫃五金、智能家居、精品燈具依賴進口；台灣產品因無 FTA 承受 MFN 關稅劣勢，須以設計整合與服務（丈量、安裝、售後）而非價格競爭；零售／貿易受 FBA 另一套規則（零售最低資本門檻）管制，須另行研究。
6. **人力策略必須以泰籍與 MOU 移工為主體**：外籍人員受 4:1 比例與 200 萬泰銖資本限制，台籍設計師與工地主任只能少量派駐；泰國工班結構（緬甸移工為主、泰籍師傅高齡化）與台灣相似，台灣的工班訓練與標準化 SOP 是可輸出的管理資產，但薪資與缺工數字本輪完全缺乏，須先補齊再估成本。

---

## 11. 資料缺口與下一輪搜尋計畫

### 11.1 缺口（依重要性）

1. **部令 B.E. 2549 室內建築分支的受管制面積／建築類型門檻原文**；私人住宅純裝飾設計是否受管制的 ACT 官方解釋（T3 第 8 項缺口，本輪仍未解）。
2. **ACT 室內建築分支持照人數**、ACT 認證學程名單與年度畢業人數；TIDA 會員數。
3. **《建築師法》罰則條文與金額原文**（§45／§71）；外國人取得 ACT 執照的正式途徑（是否有「外籍特許執照」）。
4. **《建築物管制法》改建許可實務**：第 11 號部令「不視為改建」項目原文（5 m² 門檻）；曼谷區公所 อ.1 申請文件與時程；第 39 條之二通報制適用範圍；住宅室內裝修材料防火規定。
5. **公寓法人裝修規範樣本**（保證金、時段、罰款）與國家住宅局規定。
6. **OCPB 2023 公告原文**（收據應載事項清單）；OCPB 年度投訴統計中「住宅建造／裝修」分項（2567、2568 年度）；民商法典 §600／§601 原文。
7. **FBA 附表三室內設計與建築服務的正式條號**；FBL 近年核准率；BOI 對設計服務的促進類別；DBD 人頭稽查案例。
8. **勞動部外國人禁止職業公告（B.E. 2563）**中建築設計、監造、木工、泥作的分類原文；DOE 4:1 比例的法源或公告。
9. **台泰租稅協定**生效年份與服務費扣繳稅率。
10. **消費者行為調查**：預算分級、決策旅程、風格偏好（Baan Lae Suan、DDproperty、SCB EIC、KResearch 消費者調查）；裝修貸款產品與利率（GHB、SCB、KBank 2568）。
11. **人才與勞動數字**：設計師與工地主任薪資（JobsDB／Adecco 2025 薪資指南）、技術工日薪（2568）、營建業就業人數與移工比例（NSO、DOE）、缺工調查（TCA、HBA）。
12. **材料**：TPSO 建材價格指數 2022–2025 各年變動；中國磁磚反傾銷稅年份稅率；SCG Decor／TOA／Dynasty 年報市占；台灣建材輸泰關稅。
13. **外國業者案例**：Nomura、Tanseisha 泰國子公司設立年份與營收；Nitori 泰國店數；是否有台灣、韓國、中國室內設計／定製家具業者進入泰國的案例與結果。
14. **2023–2026 法規變化**：建築物管制法、建築師法、FBA 是否有新修正；2026 年最低工資。

### 11.2 可直接執行的 20 條搜尋（泰英雙語，本輪原規劃）

| # | 問題 | 查詢 |
|---|---|---|
| 1 | Q1 | สภาสถาปนิก สถาปัตยกรรมภายใน วิชาชีพควบคุม กฎกระทรวง พื้นที่ ใบอนุญาต |
| 2 | Q1 | Thailand Architect Act B.E. 2543 interior architecture controlled profession foreign architect licence ASEAN MRA |
| 3 | Q1 | ดัดแปลงอาคาร ขออนุญาต อ.1 ตกแต่งภายใน กฎกระทรวง ฉบับที่ 11 ไม่ถือเป็นการดัดแปลง |
| 4 | Q1 | นิติบุคคลอาคารชุด ระเบียบ ตกแต่งห้อง เงินประกัน ผู้รับเหมา |
| 5 | Q2 | สคบ. ร้องเรียน ผู้รับเหมา ทิ้งงาน ตกแต่งภายใน 2568 สถิติ |
| 6 | Q2 | ประกาศคณะกรรมการว่าด้วยสัญญา ธุรกิจ ซ่อมแซม ต่อเติม อาคาร หลักฐานการรับเงิน 2566 |
| 7 | Q2 | สัญญา รับเหมา ตกแต่งภายใน มาตรฐาน รับประกัน 1 ปี มาตรา 600 |
| 8 | Q3 | Foreign Business Act List 3 interior design services foreign business licence Thailand 49% |
| 9 | Q3 | ประกาศกระทรวงแรงงาน งานที่ห้ามคนต่างด้าวทำ 2563 สถาปัตยกรรม ช่างไม้ |
| 10 | Q3 | work permit Thailand ratio 4 Thai employees 2 million capital interior designer |
| 11 | Q3 | Nomura Tanseisha Thailand subsidiary interior design Japanese firm Bangkok |
| 12 | Q4 | Thailand home renovation consumer survey 2025 budget style preference |
| 13 | Q4 | สินเชื่อ ตกแต่ง ต่อเติม บ้าน ธอส. 2568 ดอกเบี้ย |
| 14 | Q5 | เงินเดือน นักออกแบบตกแต่งภายใน 2568 มัณฑนากร JobsDB |
| 15 | Q5 | ค่าแรง ช่างไม้ ช่างปูกระเบื้อง ช่างไฟ 2568 ต่อวัน กรุงเทพ |
| 16 | Q5 | ขาดแคลน แรงงาน ก่อสร้าง 2568 ต่างด้าว เมียนมา สัดส่วน |
| 17 | Q6 | ดัชนีราคาวัสดุก่อสร้าง 2568 กระทรวงพาณิชย์ ทั้งปี เปลี่ยนแปลง |
| 18 | Q6 | SCG Decor COTTO Dynasty Ceramic market share tile Thailand 2025 anti-dumping China |
| 19 | Q7 | Architect Expo 2026 Thailand TIDA สมาคมมัณฑนากรแห่งประเทศไทย |
| 20 | Q7 | Home Builder Association Thailand รับสร้างบ้าน ตลาด 2568 มูลค่า |

---

## 12. 來源清單

### 12.1 本檔實際引用且已附 URL（承襲自 T1／T2／T3；均為搜尋摘要層級，驗證階段須重開）

| # | 標題 | 機構 | 年份 | URL |
|---|---|---|---|---|
| 1 | Architect Expo 2023: ASA/TIDA/TALA/TUDA and ACT | Architect Expo | 2023 | https://architectexpo.com/2023/en/20103/ |
| 2 | Labour curbs split nation's architects | Bangkok Post | 2016 | https://www.bangkokpost.com/thailand/general/1078432/labour-curbs-split-nations-architects |
| 3 | An Assessment of Legal Preparedness for the Liberalization of Architectural Services within ASEAN | ResearchGate | 2025 | https://www.researchgate.net/publication/397335482_An_Assessment_of_Legal_Preparedness_for_the_Liberalization_of_Architectural_Services_within_ASEAN |
| 4 | Architects and civil engineers: why Thai professional registration gates your work | issacompass | n.d. | https://www.issacompass.com/insights/architects-and-civil-engineers-why-thai-professional-registration-gates-your-wor |
| 5 | Residential Building Renovation Business in Thailand to Be Controlled | Tilleke & Gibbins | 2023 | https://www.tilleke.com/insights/residential-building-renovation-business-in-thailand-to-be-controlled/4/ |
| 6 | Engineering, Procurement, and Construction (Thailand) | Tilleke & Gibbins | n.d. | https://www.tilleke.com/print-insight/?post_id=37170&print=1 |
| 7 | Thailand – Foreign Business Act | UNCTAD Investment Policy Hub | n.d. | https://investmentpolicy.unctad.org/investment-laws/laws/40/thailand-foreign-business-act |
| 8 | Foreign Business Act (English translation) | thailaws.org | n.d. | https://www.thailaws.org/foreign-business-act/ |
| 9 | To open a branch office to do interior design consulting in Thailand (FAQ) | BOI One Start One Stop | n.d. | https://osos.boi.go.th/One-Stop/faq-group/24/To-open-a-branch-office-to-do-interior-design-consulting-in-Thailand/ |
| 10 | Foreign Business Act Thailand: Market Entry Guide 2026 | lexbangkok | 2026 | https://lexbangkok.com/foreign-business-act-thailand-market-entry-guide-2026/ |
| 11 | Thai Consumer Protection Board tightens action in home construction fraud cases | Pattaya Mail | 2025 | https://www.pattayamail.com/thailandnews/thai-consumer-protection-board-tightens-action-in-home-construction-fraud-cases-548874 |
| 12 | OCPB looks into construction scam | Bangkok Post | 2025 | https://www.bangkokpost.com/thailand/general/3253094/ocpb-looks-into-construction-scam |
| 13 | Independent Market Research on the Home Improvement Industry（Mr. DIY 泰國上市文件） | 泰國 SEC | 2024 | https://market.sec.or.th/public/ipos/IPOSGetFile.aspx?TransID=646423&TransFileSeq=87 |
| 14 | จับตาตลาดบ้านมือสอง ดิสรัปต์บ้านใหม่ | Matichon | 2025 | https://www.matichon.co.th/economy/news_5437496 |
| 15 | （REIC 轉載二手房報導） | REIC | 2025 | https://www.reic.or.th/News/RealEstate/470359 |
| 16 | （屋齡 ≥10 年住宅 2,340 萬戶報導） | Bangkokbiznews | 約 2024 | https://www.bangkokbiznews.com/property/1124831 |
| 17 | Thai property market faces toughest challenge in decades | Nation Thailand（SCB EIC／ttb） | 2025 | https://www.nationthailand.com/business/property/40056158 |
| 18 | （2026–2027 房市展望） | Nation Thailand | 2026 | https://www.nationthailand.com/business/economy/40070934 |
| 19 | （住宅市場展望） | SCB EIC | 2025 | https://www.scbeic.com/en/detail/product/443 |
| 20 | REIC Q4 2568 住宅市場與 2569 趨勢（轉載） | Bangkok Focus News | 2026 | https://www.bangkokfocusnews.com/2026/02/REIC-Q4-2568-Trends2569.html |
| 21 | REIC Press Release（Q1） | REIC | 2025 | https://www.reic.or.th/Activities/PressRelease/260 |
| 22 | HMPRO Listed Company Snapshot 3M/2025 | SET | 2025 | https://lssmedia.setlink.set.or.th/2025/3M/HMPRO-3M68-ListedCompanySnapshot-EN.html |
| 23 | HMPRO reports THB 6.4 billion net profit | Kaohoon International | 2025 | https://www.kaohooninternational.com/markets/537124 |
| 24 | ILM Listed Company Snapshot YE/2024 | SET | 2025 | https://lssmedia.setlink.set.or.th/2024/YE/ILM-YE67-ListedCompanySnapshot-EN.html |
| 25 | Index Living Mall reports strong 2024 performance | Index Living Mall IR | 2025 | https://investor.indexlivingmall.com/en/updates/press-releases/416/index-living-mall-reports-strong-2024-performance-with-recordhigh-profit-for-the-third-consecutive-year-proposes-thb-100-dividend-per-share |

### 12.2 機構入口頁（D 級，僅確認網域存在、本輪未開啟；用於下一輪定位原始條文與統計）

| # | 機構 | URL |
|---|---|---|
| 26 | 泰國建築師委員會（สภาสถาปนิก, ACT） | https://act.or.th |
| 27 | 工程師委員會（สภาวิศวกร, COE） | https://coe.or.th |
| 28 | 暹羅建築師協會（ASA） | https://asa.or.th |
| 29 | 商業發展廳（DBD） | https://www.dbd.go.th |
| 30 | 投資促進委員會（BOI） | https://www.boi.go.th |
| 31 | 就業廳（DOE） | https://www.doe.go.th |
| 32 | 勞動部（MOL） | https://www.mol.go.th |
| 33 | 消費者保護委員會辦公室（OCPB） | https://www.ocpb.go.th |
| 34 | 公共工程與城鄉規劃廳（DPT） | https://www.dpt.go.th |
| 35 | 國務院法制委員會法規庫（Krisdika） | https://www.krisdika.go.th |
| 36 | 政府公報（Royal Gazette） | https://www.ratchakitcha.soc.go.th |
| 37 | 貿易政策與戰略辦公室（TPSO） | https://www.tpso.go.th |
| 38 | 商務部價格指數 | https://www.price.moc.go.th |
| 39 | 國家統計局（NSO） | https://www.nso.go.th |
| 40 | 泰國央行（BOT） | https://www.bot.or.th |
| 41 | 稅務廳（Revenue Department） | https://www.rd.go.th |
| 42 | 政府住宅銀行（GHB） | https://www.ghbank.co.th |
| 43 | 泰國工業標準院（TISI） | https://www.tisi.go.th |
