# 單一市場深潛提示詞範本（Country Module）v1

> **用法**：(1) 把 `{{市場}}` 換成市場名稱；(2) 把「在地搜尋線索」段落換成下方對照表中該市場的那一列；(3) 貼到 ChatGPT／Gemini／Claude.ai 任一個（模式同主提示詞）。每個 AI 每市場 1 次，12 市場 × 3 AI ＝ 36 次，屬加分項，優先跑台灣、日本、新加坡、馬來西亞、越南五個。
> **存檔**：`03-inbox/<ai>/<YYYYMMDD>_<ai>_country-<代碼>_r1.md`

=== 提示詞開始 ===

【範圍】：單一市場：{{市場}}

你是一位資深亞洲市場研究顧問，專長是室內裝修設計產業、住宅翻修與不動產。委託人是台灣一家中型集團（室內裝修設計＋不動產＋家居零售，基地在宜蘭與台北信義）的 CEO。請用多步驟網頁研究，針對 **{{市場}}** 的室內裝修設計市場完成一份 6,000–12,000 字、可查證的深潛報告，供與台灣比較及評估跨境可行性。

### 必答的 10 個問題（每題一節，先結論後證據，每個數字附年份、來源編號、URL、定義備註、信心）
1. 市場規模與成長：設計服務／住宅翻修／商業裝修／家居零售；列出**所有**來源與其定義（表格並列）；住宅 vs 商業、新屋 vs 存量占比；2024–2026 現況與 2030 預測分開。
2. 需求結構：新屋完工、交易量（新屋 vs 中古）、屋齡分布（30 年以上占比）、翻修週期、每案均價、每 m²（換算每坪 = 3.3058 m²）基本／中階／高階單價、設計費行情、工期。
3. 產業結構與主要玩家：家數與集中度；前 10–20 名（純設計、設計施工連鎖、零售整合、建商精裝、平台）營收、模式、股權、近 3 年併購／募資／倒閉。
4. 通路與獲客：平台（用戶數、GMV、抽成）、仲介、零售、建商、社群。
5. 法規與證照：誰能執業設計、誰能施工；法規名稱、主管機關、登記／證照／考試；裝修許可流程（建管、消防、公寓／公宅規約）；罰則；2023–2026 修法。引用法條或主管機關 URL。
6. 消費者保護與糾紛：合約範本、訂金、保固期、保險／履約保證、投訴統計、詐騙型態。
7. 外資／台資進入規則：100% 持股可否（設計公司／裝修承包商分開答）、外籍設計師執業限制、承包商登記、工作簽證、稅務提示、已進入的外商案例與結果。
8. 消費者行為：誰在裝修、預算分級、決策歷程、風格、付款階段、融資與補助。
9. 人才與工班：設計科系畢業人數、執業人數、設計師／監工薪資、師傅日薪、缺工、移工政策。
10. 材料供應鏈與價格：在地品牌、進口依賴、關稅／標準、2022–2026 漲幅。

### 在地搜尋線索（請用這些機構名、法規名、在地語言關鍵字查詢）
{{在地搜尋線索：貼上對照表中該市場那一列}}

### 輸出格式
0. 中繼資料（AI、模式、日期、範圍、搜尋語言、來源數）
1. 摘要（8 點內，每點一句結論＋一個關鍵數字）
2. 10 節正文
3. 本市場對台灣業者的 3–5 點啟示
4. 與台灣比較的錨點：人均翻修支出、翻修市場占 GDP 比、每 m² 單價 ÷ 人均 GDP、設計費占工程費比、設計公司家數 ÷ 人口、平台滲透率
5. 矛盾資料與資料缺口（表格）
6. 來源清單（#編號｜標題｜機構｜年份｜語言｜URL；只列實際開啟過的）
7. 附錄：關鍵指標表（CSV 風格：market,metric,value,unit,year,source_id,source_url,definition,confidence；≥ 15 列）

### 紀律
- 繁體中文（台灣用語）；機構、法規、公司名保留原文於括號。
- 幣別：原幣＋美元＋新台幣，註明匯率。
- 找不到寫「無資料」；禁止不標示的估計；禁止虛構 URL。
- 市調公司數字必註明定義；預測與現況分開。
- 法規結論標「需專業人士最終確認」。

=== 提示詞結束 ===

---

## 在地搜尋線索對照表

| 市場 | 貼入「在地搜尋線索」的內容 |
|---|---|
| 台灣 | 財政部 營利事業家數及銷售額（室內裝潢業）；內政部國土署 室內裝修業登記；建築物室內裝修管理辦法；建築法第 95 條之 1；內政部 不動產資訊平台（屋齡、買賣移轉棟數）；使用執照核發戶數；中華民國室內裝修商業同業公會全國聯合會（CNAID）、台北市室內設計裝修商業同業公會（TAID）、中華民國室內設計協會（CSID）；100室內設計、設計家 searchome、PULO、幸福空間、漂亮家居；特力集團年報（HOLA、特力屋）、IKEA 台灣、宜得利 NITORI、無印良品；營造業移工開放（2023–2025）；長照 2.0 居家無障礙環境改善補助；青年安心成家 修繕貸款；內政部「建築物室內裝修－工程承攬契約書範本」；消基會／消保處 裝修申訴；Cushman & Wakefield 台北 fit-out 成本；宜蘭縣 建物買賣移轉、民宿數量 |
| 日本 | 矢野経済研究所 住宅リフォーム市場規模（2025 約 7.5 兆円）；住宅リフォーム・紛争処理支援センター；国土交通省 住宅市場動向調査、住宅着工統計、住宅・土地統計調査 2023；リフォーム産業新聞 リフォーム売上ランキング；建築士法、建設業法（内装仕上工事業）；インテリアプランナー／インテリアコーディネーター（インテリア産業協会）；リフォーム瑕疵保険；住宅リフォーム事業者団体登録制度；国民生活センター リフォーム トラブル；住宅省エネ2025／2026キャンペーン；介護保険 住宅改修；SUUMO リフォーム、ホームプロ、リショップナビ；積水ハウスリフォーム、住友林業ホームテック、大和ハウスリフォーム、LIXIL リフォームショップ、Panasonic リフォーム、カチタス、リノベる、ニトリ；特定技能 建設 外国人；大工 高齢化；三幸エステート オフィス 内装 坪単価 |
| 韓國 | 한국건설산업연구원（KCERI）인테리어 리모델링 시장 규모；통계청 실내건축 및 건축마무리 공사업；건설산업기본법 실내건축공사업 등록；실내건축기사；한국소비자원 인테리어 피해구제；공정거래위원회 인테리어 표준계약서；그린리모델링；한샘 리하우스、LX하우시스 지인、KCC글라스 홈씨씨、현대리바트；오늘의집（버킷플레이스）거래액、집닥、아파트멘터리；인테리어 평당 비용 2025；노후 아파트 30년 이상 비율；주택 매매 거래량 국토교통부；건설근로자공제회 고령화；고용허가제 E-9 건설업；한국실내건축가협회 KOSID；코리아빌드 |
| 新加坡 | HDB Directory of Renovation Contractors（DRC）、HDB renovation permit；BCA licensed builders；CaseTrust-RCMA；Society of Interior Designers Singapore（SIDS）、IDCS accreditation；CASE renovation complaints；police renovation deposit scams；Qanvast renovation cost guide、Hometrust、Renopedia；Livspace Singapore；HDB BTO completions、HDB resale transactions、URA private transactions；HIP Home Improvement Programme；EASE 2.0、Age Well SG；Cushman & Wakefield fit-out cost Singapore；MOM Employment Pass salary threshold 2025；construction work permit quota／levy；ACRA number of interior design firms；DesignSingapore Council；IKEA Singapore、Courts、Castlery |
| 香港 | 屋宇署 小型工程監管制度、註冊小型工程承建商（第 I／II／III 級）、註冊一般建築承建商；建築物條例；香港室內設計協會（HKIDA）；消費者委員會 裝修投訴；裝修訂金騙案；政府統計處 裝修及維修工程總值；土地註冊處 住宅成交量；樓齡 30 年以上樓宇數；樓宇更新大行動 2.0；長者維修自住物業津貼；裝修佬 DecoMan、Decor8、好師傅、設計家；裝修費用 每呎 2025；Steve Leung Design Group 年報、AB Concept；建造業議會 CIC 技工短缺、輸入勞工計劃；高才通 設計師；IKEA 香港、Pricerite 實惠、日本城；Cushman & Wakefield／JLL 香港 寫字樓裝修成本 |
| 中國大陸 | 中国建筑装饰协会 行业发展报告（产值）；艾瑞咨询 家装行业报告；住建部 全装修／精装修 政策、装配式装修；奥维云网 精装房 渗透率；国家统计局 住宅销售面积、竣工面积；贝壳研究院 二手房成交；老旧小区改造、城市更新；以旧换新 家装 补贴 2024–2025；住宅室内装饰装修管理办法（建设部 110 号令）；建筑业企业资质（建筑装修装饰工程专业承包）；GB 50222 内部装修设计防火规范；中消协 家装投诉；家装合同示范文本；外商投资准入负面清单 2024；土巴兔、齐家网（齐屹科技）、被窝家装（贝壳）、圣都、爱空间、酷家乐（群核科技 招股书）、三翼鸟；金螳螂、东易日盛、红星美凯龙、居然之家、宜家中国；欧派、索菲亚、志邦、九牧、箭牌、东鹏、马可波罗；家装 每平米 价格 一线城市 2025；小红书／抖音 家装 流量；中国室内装饰协会 CIDA；广州建博会 |
| 馬來西亞 | Architects Act 1967（2015 修正）Interior Designer registration、Lembaga Arkitek Malaysia（LAM）；Malaysian Institute of Interior Designers（MIID）；CIDB contractor registration G1–G7、CIDB Act 520；Strata Management Act 2013 renovation by-laws；DBKL／MBPJ renovation permit；Bomba；KPDN consumer complaints、Tribunal for Consumer Claims；NAPIC property market report（transactions、overhang、completions）；DOSM specialised construction；SSM foreign equity services；Employment Pass 2025；foreign worker quota／levy construction；Qanvast Malaysia、Recommend.my、Atap.co；Livspace Malaysia exit；IKEA Malaysia（Ikano）、MR DIY、Nitori Malaysia、SSF、Courts、HomePro Malaysia、Signature International；renovation cost per sq ft 2025；Johor–Singapore SEZ；ARCHIDEX |
| 泰國 | พระราชบัญญัติสถาปนิก พ.ศ. 2543（สถาปัตยกรรมภายในและมัณฑนศิลป์ 為管制專業）、สภาสถาปนิก（ACT）；Foreign Business Act 1999 List 3（interior design 屬服務業需 FBL 或泰資 51%）；BOI；work permit 4:1 泰籍員工比；Building Control Act ดัดแปลงอาคาร；นิติบุคคลอาคารชุด 裝修規範；สคบ. 消費者投訴；ศูนย์วิจัยกสิกรไทย（Kasikorn）、Krungsri Research、SCB EIC 住宅翻修與建材零售；REIC 住宅移轉；曼谷公寓庫存（CBRE、Colliers）；HomePro、Index Living Mall、SB Design Square、Thai Watsadu、DoHome、IKEA Thailand、Nitori Thailand、Boonthavorn 年報；dwp、P49 Deesign、PIA Interior；TIDA；ค่าตกแต่งภายใน ต่อตารางเมตร 2568；ค่าแรงช่าง 2568；แรงงานต่างด้าว ก่อสร้าง；Architect Expo |
| 越南 | Luật Xây dựng 2014／2020、Nghị định 15/2021（năng lực hoạt động xây dựng）、Luật Kiến trúc 2019（chứng chỉ hành nghề）；Nghị định 175/2024 nhà thầu nước ngoài；WTO 服務承諾 CPC 8674；work permit 2025；Nghị định 50/2024 PCCC；Bộ Xây dựng 住宅供給；GSO 建築完成；CBRE／Savills 河內、胡志明公寓供給；bàn giao thô（毛胚交屋慣例）；chi phí hoàn thiện nội thất căn hộ 2025 triệu đồng/m²；báo giá thi công nội thất trọn gói；AA Corporation、Nhà Xinh（AKA）、Hòa Phát、An Cường、Viglacera、Đồng Tâm；JYSK、BAYA、Uma、Nitori Vietnam；HAWA／VIFOREST 家具出口；台商 越南 辦公室 宿舍 裝修；VietBuild；Happynest |
| 印尼 | UU 2/2017 Jasa Konstruksi、SKK Konstruksi（LPJK）、SBU；HDII（Himpunan Desainer Interior Indonesia）；PP 16/2021 PBG（建築許可）；P3SRS 公寓裝修；Perpres 10/2021 正面投資清單（建設顧問外資上限）、BUJKA；KBLI 74120 desain interior PMA；RPTKA／IMTA 外籍人力；YLKI／BPKN 消費者投訴；BPS 建築統計；REI 住宅完工、housing backlog；Colliers／JLL 雅加達辦公室裝修成本；IKN 新首都；Dekoruma、Fabelio（倒閉）；Informa（Kawan Lama）、IKEA Indonesia（Hero）、Mitra10（CSAP）、AZKO（Ace Hardware）；Hadiprana、Airmas Asri；biaya renovasi per meter 2025；upah tukang 2025；Mulia、Roman、Toto Indonesia、Propan、Taco；Indobuildtech |
| 菲律賓 | RA 10350 Philippine Interior Design Act of 2012（執業限持照菲籍設計師；外籍需互惠）；PRC Board of Interior Design 考照人數；Foreign Investments Act 專業執業保留；PCAB 承包商執照（Regular／Special、外資）；PD 1096 National Building Code 裝修許可；RA 9514 Fire Code；condominium corporation 裝修規定；DTI 消費者投訴；Civil Code Art. 1723 保固；PSA 建築許可／完工；Colliers 馬尼拉公寓供給；BPO 辦公室 fit-out；Cushman & Wakefield／JLL 馬尼拉 fit-out 成本；Wilcon Depot、AllHome、SM Home、IKEA Pasay、Mandaue Foam 年報；PIID；Pag-IBIG home improvement loan；TESDA 技工短缺；NCR 最低工資；Worldbex |
| 印度 | 無室內設計師法定證照（Council of Architecture Act 1972 僅管建築師）；IIID；National Building Code 2016；RERA；cooperative housing society renovation NOC（孟買）；Consumer Protection Act 2019 室內設計投訴案例；FDI policy 建設開發與服務業 100% 自動路徑；RedSeer／Livspace 市場規模（organized vs unorganized）；Livspace、HomeLane、Design Cafe 財報與募資；Pepperfry、Urban Ladder（Reliance）、IKEA India、Asian Paints Beautiful Homes、Godrej Interio、Sleek；Anarock／Knight Frank 住宅銷售；Cushman & Wakefield 孟買／班加羅爾 fit-out 成本；interior cost per sq ft 2025；carpenter wages 2025；Century Ply、Greenply、Kajaria、Somany、Hindware、Jaquar、Merino；NID／CEPT 畢業生；ACETECH、India Design ID |
