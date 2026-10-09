# 印尼（Indonesia）— 事實查核報告（ID-verification，第二輪：含獨立搜尋）

| 項目 | 內容 |
|---|---|
| 查核日期 | 2026-10-09（取代 2026-10-08 之零搜尋版本） |
| 查核者 | Claude 子代理（懷疑型事實查核；預設立場：原報告主張在證據支持前視為錯誤） |
| 查核對象 | `countries/ID-A-market.md`（LENS A：市場結構／規模／價格／玩家）、`countries/ID-B-rules.md`（LENS B：法規／證照／消保／外資／人才／材料） |
| 方法 | 本輪成功執行 **16 次獨立 WebSearch**（15 次驗證＋1 次動用保留額度處理外資上限爭議；另 1 次保留未用）。查詢全部以印尼文或英文**重新措辭**、避開分析師原查詢；WebFetch／curl 依環境政策封鎖，故所有證據來自搜尋結果摘要中可辨識之原文，逐項附 URL。未納入本輪搜尋之項目另列於 (a) 末段，不計入查核統計。 |
| 結果 | 查核 **20 項**：✅ 確認 **11**、✏️ 修正 **2**、❌ 駁斥 **1**、❓ 無法查證 **6**。另列 12 項內部矛盾／定義問題。整體品質：**中**。 |

> **整合者務必先讀的三件事**
> 1. **「室內設計子部門 Rp 104.6 兆」是誤植級錯誤，必須刪除。** 7.44% 是「創意經濟占全國 GDP」的比率（2019 年；2016 年亦約 7.44%），OSS-RBA 部落格把它誤套到「室內設計占創意經濟」上，再乘上創意經濟 GDP 得出 Rp 104.6 兆。室內設計是小型子部門，官方前三大子部門（餐飲、時尚、工藝）合占約 75%，其餘 14 個子部門合占 25%。LENS A 由此衍生的「占 GDP 0.47%」「人均 Rp 37 萬」「設計施工服務與家具商品同量級」全部失效。
> 2. **住房缺口 990 萬戶是 2023 年（Susenas 2023）數字，不是 2025 年。** BPS 2026-08-22 首版《Statistik Perumahan 2026》：2025 年 964 萬戶（13.00%）、2026 年 929 萬戶（12.39%）。
> 3. **BUJK PMA 外資上限 67%/70% 不得寫成現行規定。** PP 5/2021 附錄確有此數；PP 28/2025（2025 年 6 月）取代 PP 5/2021 後，2026 年法律顧問指南稱上限已取消、ASEAN Briefing 稱過渡期仍實質適用，兩說相反；須以 PP 28/2025 附錄 I 與 Permen PU 6/2025 原文裁定。

---

## (a) 逐項查核表

| # | 項目 | 原報告值 | 查核結果 | 修正值 | 證據 URL | 說明 |
|---|---|---|---|---|---|---|
| 1 | 室內設計子部門產值（A §1、§2、§7、§8） | Rp 104.6 兆（2023）、占創意經濟 GDP 7.44%（OSS-RBA 引 BEKRAF）；A 據此推算占全國 GDP 0.47%、人均 Rp 37 萬 | ❌ **駁斥** | **不採用。** 7.44% 為創意經濟占全國 GDP 之比率，非室內設計占創意經濟之比率。量級推估：前三大子部門餐飲 41.69%、時尚 18.15%、工藝 15.70% 合占約 75%；其餘 14 個子部門合占 25%，其中 9 個各僅 0.1–0.5%。室內設計若落在 0.1–0.5% 帶，以 2024 年創意經濟 GDP Rp 1,611.2 兆計約 **Rp 1.6–8 兆**（本人推算，信心低，僅供量級） | https://ekon.go.id/publikasi/detail/3874/ekonomi-berbasis-kreativitas-dan-inovasi-sebagai-kekuatan-baru-ekonomi-indonesia ；https://jurnal.isei.or.id/index.php/isei/article/view/344/101 ；https://ekonomi.bisnis.com/read/20200830/12/1284797/tiga-subsektor-ekonomi-kreatif-jadi-penyumbang-terbesar-pdb ；https://www.kompas.id/artikel/majukah-industri-kreatif-indonesia ；https://databoks.katadata.co.id/infografik/2024/04/29/nilai-pdb-ekonomi-kreatif-indonesia-meningkat-usai-pandemi | 算術證據：7.44% × 2023 年創意經濟 GDP（舊系列約 Rp 1,400 兆）≈ Rp 104 兆，與 OSS-RBA 數字吻合，證明其為「比率誤套」。Databoks（2024-04）亦指 Kemenparekraf 尚未發布各子部門最新 PDB，故 2023 年「室內設計 Rp 104.6 兆」不可能有官方來源。兩輪獨立搜尋均未找到室內設計子部門的國家級 PDB 數字。 |
| 2 | 創意經濟 GDP（A §2） | 2024 年 Rp 1,611.2 兆、占 GDP 7.28%、+6.57%（Databoks 引 BPS／Kemenekraf） | ❓ 無法查證（序列不可串接） | 可引用，但須註明「Kemenekraf／BPS 2026 年發布之新系列」；**不可**與舊系列串接：2020 Rp 1,134.9 兆、2021 Rp 1,191 兆、2022 Rp 1,280 兆（占 6.54%，十年最低） | https://databoks.katadata.co.id/infografik/2024/04/29/nilai-pdb-ekonomi-kreatif-indonesia-meningkat-usai-pandemi ；https://journal.unpar.ac.id/index.php/PEDR/article/download/6996/4258 ；https://www.kompasiana.com/diahyunipurwati9478/6858319234777c52ae1658d2/menguat-ekonomi-kreatif-catat-kontribusi-dalam-pdb-ri ；https://pelakubisnis.com/2024/01/ekonomi-kreatif-sumbang-rp-1300-triliun-terhadap-pdb/ | 獨立搜尋只找到舊系列。若 2024 年 1,611.2 兆且年增 6.57%，隱含 2023 年約 1,512 兆，遠高於舊系列 2023 年「約 Rp 1,300 兆」，顯示 2026 年版本經過重估（子部門由 17 擴為 21 亦佐證）。A 以 1,611.2 ÷ 7.28% 反推全國 GDP ≈ Rp 22,132 兆，算術正確。 |
| 3 | 住房自有缺口 backlog（A §1、§3、§8） | 約 990 萬戶（**2025**）；2020 年 1,275 萬戶（Ken Research 引 BPS） | ✏️ **修正** | 990 萬 ＝ **Susenas 2023**；**2025 年 964 萬戶（13.00%）；2026 年 929 萬戶（12.39%）**（BPS《Statistik Perumahan 2026》首版，2026-08-22）。2020 年 1,275 萬維持 | https://www.bps.go.id/en/news/2026/08/22/937/bps-rilis-perdana-statistik-perumahan-2026--akses-rumah-layak-huni-meningkat.html ；https://pasardana.id/news/2026/8/14/bps-sebut-backlog-kepemilikan-rumah-tunjukkan-perkembangan-positif ；https://www.gebrak.id/2026/06/krisis-hunian-masih-membayangi-964-juta.html ；https://www.kabarbursa.com/makro/danantara-tawarkan-dp-1-persen-di-housing-expo-2026-mampukah-tekan-backlog-99-juta-unit.md ；https://investortrust.id/business/63933/kepala-bps-tepis-isu-backlog-hunian-capai-15-juta-tahun-ini | 2025-04 住宅部副部長 Fahri Hamzah 稱缺口「約 1,500 萬」，BPS 局長否認並維持 990 萬（當時仍為 2023 數據）；其後 BPS 正式發布 2025 年 964 萬。另有 backlog-2（居住品質不達標）2026 年 24.03%、2025 年 25.33%，可作「翻修需求」代理指標。 |
| 4 | 自有住宅戶比（A §3） | 82.38%（2025，Ken Research 引 BPS） | ✏️ **修正**（定義不符） | BPS backlog-1（未擁有自宅）2025 年 13.00% → 擁有自宅戶比約 **87.0%**（本人以 100 − 13.00 計算）；2026 年 12.39% → 約 87.6% | 同 #3（BPS 2026-08-22；pasardana 2026-08-14） | Ken Research 的 82.38% 無法對應 BPS 任一口徑；最終報告以 BPS 為準。 |
| 5 | FLPP 2025 補貼房貸放款（A §1、§3、§8） | 278,868 戶、Rp 34.64 兆、達 35 萬戶目標 79.68%、2010 年以來最高 | ✅ **確認** | 維持。補充歷年：2024 年 200,300 戶／Rp 24.6 兆；2023 年 229,000 戶／Rp 26.32 兆；2025-12-19 中途數 263,017 戶／Rp 32.67 兆 | https://keuangan.kontan.co.id/news/bp-tapera-salurkan-dana-flpp-senilai-rp-3464-triliun-sepanjang-tahun-2025 ；https://nasional.kontan.co.id/news/bp-tapera-realisasi-flpp-rumah-subsidi-capai-263017-rumah ；https://ekonomi.bisnis.com/read/20251111/47/1927945/penyaluran-rumah-subsidi-flpp-capai-rp2734-triliun-hingga-awal-november-2025 | BP Tapera 2025-12-31 結算數，Kontan 獨立報導與 A 的 Media Indonesia 來源一致；2025 年戶數較 2024 年 +39%。A 的換算 USD 21 億／TWD 661 億重算正確。 |
| 6 | BI 一級市場住宅價格調查 SHPR（A §3、§6、§8） | IHPR 2025 Q4 +0.83%、2026 Q1 +0.62%；銷量 2025 Q4 +7.83%、2026 Q1 −25.67%；KPR 占 69.87%；開發商自有資金 80.66% | ✅ **確認**（並有更新） | 維持；**補充 2026 Q2**（BI 2026-08-07 發布）：IHPR +0.69% yoy；銷量 **−2.36% yoy**（跌幅自 −25.67% 大幅收斂） | https://www.bi.go.id/id/publikasi/laporan/Documents/SHPR_Tw_I_2026.pdf ；https://www.bi.go.id/id/edukasi/Documents/Infografis-Survei-Harga-properti-Residensial-di-Pasar-Primer-Triwulan-I-2026.pdf ；https://ekonomi.bisnis.com/read/20260509/47/1972565/survei-harga-bi-properti-masih-naik-meski-pasar-perumahan-kian-lesu ；https://bcasekuritas.co.id/en/latest-news/news/survei-bi-harga-properti-residensal-naik-terbatas-di-triwulan-ii-2026 ；https://www.industry.co.id/read/154227/harga-rumah-di-pasar-primer-naik-terbatas-pada-kuartal-ii-2026-penjualan-mulai-pulih | 2026 Q1 數字全部與 BI 原始報告一致（18 城市樣本、2026-05-08 新聞稿 No. 28/97/DKom）。A 以「2026 Q1 −25.67%」推論新成屋裝修需求承壓，須補上 Q2 回穩，否則過度悲觀。 |
| 7 | 住宅翻修主流單價（A §1、§3、§7、§8） | Rp 250–400 萬/m²（含工帶料、不含家具；Mitra10 等承包商） | ✅ **確認** | 維持；補充兩軸拆解：**純工資包工（jasa saja）Rp 100–150 萬/m²；含料包工（borongan penuh）Rp 250–400 萬/m²** | https://momsmoney.kontan.co.id/news/berikut-ini-estimasi-biaya-renovasi-rumah ；https://mamikos.com/info/cara-menghitung-biaya-renovasi-rumah-1-lantai-menjadi-2-lantai-gnr/ | Kontan（MomsMoney）與 2026-04 Mamikos 兩個獨立來源給出相同區間（type-45 以 Rp 300 萬/m² 估約 Rp 2.7 億）。A 的 TWD 4,800–7,600/m²、1.58–2.52 萬/坪重算正確。 |
| 8 | 雅加達高階整屋翻修（A §1、§7） | Rp 700–1,000 萬/m²（Heris Kontraktor，2026） | ❓ 無法查證 | 降級為「單一承包商報價、信心低」；標題改用 Heris 的標準～中階帶 Rp 450–700 萬/m²，並註明來源 | 筆記既有：https://heriskontraktor.id/artikel/biaya-renovasi-rumah/ | 獨立搜尋未找到任何第二來源支持住宅翻修 Rp 700 萬/m² 以上行情；Kontan 的「大型翻修」上限僅 Rp 400 萬/m²。 |
| 9 | 純室內設計費（A §1、§3、§7、§8、§9） | Rp 15–100 萬/m²；或總造價 2–5%（Arsitag）／2–10%（Cariproperti） | ✅ **確認**（核心帶收窄） | **核心帶 Rp 20–70 萬/m²**（Archify）；全距 Rp 15–100 萬/m²；百分比法 2–5%，且業界「較少採用」；「至 10%」僅單一來源，降級 | https://www.archify.com/id/archifynow/perkirakan-biaya-membangun-interior-impian-anda-ini-caranya ；https://www.archify.com/id/archifynow/berapa-biaya-jasa-arsitek-begini-cara-hitungnya | Archify 獨立指出 per-m² 為主流計費法、2–5% 法 kurang lazim（因 RAB 前期不確定）。A 的 TWD 290–1,900/m² 換算正確；A §9「約為台灣 1/5–1/10」取決於 TW 筆記數字，本輪未核。 |
| 10 | 雅加達辦公室裝修成本（A §1、§3、§7、§8） | C&W 2025：USD 58/sqft、亞太最便宜、本幣 −16%、排名 24→33、東京 USD 195 最貴 | ✅ **確認** | 維持（USD 624/m² ≈ Rp 1,030 萬/m² ≈ TWD 19,700/m² 重算正確） | https://www.cushmanwakefield.com/en/singapore/news/2025/03/contractor-sentiment-generally-positive-as-the-worst-of-price-pressures-ease ；https://cfotech.asia/story/fit-out-costs-rise-in-asia-pacific-tokyo-remains-priciest ；https://realestateasia.com/indonesian/node/514574986 | C&W 官方新聞稿證實全部細節（雅加達取代胡志明市成最便宜、租戶轉向低規格）。A 所引 2026 年版「復原成本 USD 9–12/sqft」本輪未查。 |
| 11 | HDII 會員與持證人數（A §1、§4、§7、§8、§9；B §10） | 會員 2,225 人／23 省（2024）；持證 1,897 人、未持證約 6,000 人（Arsitag，未標年份） | ❓ 無法查證（與較早資料衝突） | 會員數：「約 2,200 人（2024，單一媒體來源）」可保留；**持證數改為「不明；2018 年 HDII 秘書長稱從業 1,700 人、持證僅約 200 人」，刪除「1,897 持證」** | https://wartaekonomi.co.id/read187183/minim-ri-hanya-punya-200- ；https://www.suarasurabaya.net/?p=231683 | 2018 年 Sekjen Rohadi：持證 200 人、當年目標 300–400 人；Suara Surabaya 引另一秘書長：1,200 餘家會員公司僅 100 餘家取得認證（頁面日期不明）。「1,897 持證」與上述相差近 10 倍，疑為「會員數」誤植為「持證數」。A §9 以「持證設計師約 1,900 人」立論須改寫。 |
| 12 | HDII 雅加達分會會員（A §4 vs B §6.3、§8.1） | A：會員 950+、持證 90+；B：會員 90+、持證 40+（**同一 URL** hdiidki.org/tentang-kami） | ❓ 無法查證（內部矛盾） | 兩者皆不採用；寫「HDII DKI 分會數字兩位分析師自同一頁面讀出不同值（950+/90+ vs 90+/40+），待向 HDII 確認」 | 筆記既有：https://hdiidki.org/tentang-kami/ | 搜尋摘要無法開啟原頁。以全國 2,225 人分布 23 分會計，平均約 97 人/分會，B 的 90+ 較合理；A 的 950+ 疑為誤讀（若雅加達占全國 43% 亦不合常理）。 |
| 13 | UU 2/2017 第 70 條：營造從業人員（含設計顧問）須持 SKK（B §1、§2.1、§2.2） | 所有營造從業人員須持 SKK；由 LSP 執行能力測驗；HDII 受 PUPR 委託核發 | ✅ **確認**（主張）；「HDII 核發」部分未驗證 | 維持；改寫為「SKK 經能力測驗取得，由 BNSP 授權、在 LPJK 登錄之 LSP 核發（HDII 相關 LSP 為其一）」 | https://pasal.id/peraturan/uu/uu-no-2-tahun-2017 ；https://www.industry.co.id/read/45797/sertifikasi-konstruksi-bukan-hanya-soal-kompetensi ；https://jurnal.tau.ac.id/index.php/snartek/article/download/774/517/3285 ；https://berkas.dpr.go.id/puspanlakuu/resume/resume-public-466.pdf | 獨立法學期刊與產業媒體均確認第 70 條 SKK 強制。MK 判決 70/PUU-XVI/2018 僅涉第 68(4) 條，未動搖第 65、70 條。 |
| 14 | UU 2/2017 第 65 條：建築失效（Kegagalan Bangunan）責任最長 10 年（B §2.1、§3.3，B 自標「既有知識、未驗證」） | 最長 10 年 | ✅ **確認** | 維持；條文要旨：服務提供者依「規劃使用年限」負責；若使用年限逾 10 年，自最終交付日起**最長 10 年**；期限須載明於營造契約；PP 22/2020 為施行細則（其序言引第 65(5) 條） | https://www.hukumonline.com/klinik/a/tanggung-jawab-kontraktor-lt4c692c9f31e6b/ ；https://business-law.binus.ac.id/2017/03/26/kegagalan-bangunan-tiada-lagi-pidana-bagi-pelaku-jasa-konstruksi ；https://klinikkonstruksi.jogjaprov.go.id/storage/images/peraturan/0ae8a_PP%20No%2022%20Th%202020%20ttg%20Peraturan%20Pelaks%20UU%20No%202%20Th%202017%20ttg%20JasKontr.pdf | 「建築失效」定義（第 1 條第 10 款）為交付後倒塌或喪失功能，**不等於一般裝修瑕疵保固**；印尼無法定裝修保固期，B 既有「5% 保留款、3–6 個月保養期」仍屬未驗證慣例。 |
| 15 | 住宅裝修許可 PBG（B §1、§2.3） | PP 16/2021 廢 IMB 改 PBG；結構／面積／用途／立面變更需 PBG；油漆換磚免辦；罰則「行政制裁乃至資產查封」 | ✅ **確認**（罰則用語修正） | 第 11(2) 條：功能或分類變更須申請「PBG perubahan」；第 253(3) 條：PBG 涵蓋新建、變更、擴建、縮建、維護；**第 45(1) 條行政制裁序列：書面警告→暫停或永久停工→查封（penyegelan）→拆除（pembongkaran）**；第 347 條：2021 年前之 IMB 仍有效，無 PBG 之既有建物須先辦 SLF；線上經 SIMBG 申辦 | https://www.detik.com/properti/tips-dan-panduan/d-7047030/pbg-adalah-persetujuan-bangunan-gedung-ketahui-perbedaannya-dengan-imb ；https://www.hukumonline.com/klinik/a/apakah-renovasi-rumah-akan-menaikkan-besar-pbb-lt5407f0d9ba6d6/ ；https://ekonomi.bisnis.com/read/20210225/47/1360852/jokowi-hapus-imb-diganti-pbg-apa-itu ；https://www.brighton.co.id/about/articles-all/cara-mengurus-imb-menjadi-pbg-dan-syaratnya | B 的「資產查封」應改為「建物查封與拆除」。「小型裝修免 PBG」為實務解讀，法條以「有無變更建築」為準，地方規費（retribusi）各地不同。 |
| 16 | BUJK PMA 外資持股上限（B §1、§2.1、§4.2、§9、§11） | 非東協 67%／東協 70%（PP 5/2021 附錄；B 自標「法源已被取代、現況未驗證」） | ❓ 無法查證（**現況有爭議**） | 改寫為：「PP 5/2021 附錄時期為 67%/70%（已確認）。PP 28/2025（2025 年 6 月取代 PP 5/2021）後：Emerhub 2026 指南稱該上限已取消、多數營造業別可 100% 外資；ASEAN Briefing（2025 年中）稱過渡期內仍實質適用 67%/70%；Dentons HPRP 2026-05 評述 PP 28/2025 與 Permen PU 6/2025 之 BUJK 許可新制。**須以 PP 28/2025 附錄 I 矩陣原文裁定**」 | https://emerhub.com/indonesia/foreign-construction-company-indonesia-2026/ ；https://www.aseanbriefing.com/news/indonesias-construction-boom-and-opportunity-for-foreign-contractors/ ；https://dentons.hprplawyers.com/en/insights/articles/2026/may/5/updates-to-indonesias-construction-services-business-licensing-regime ；https://peraturan.bpk.go.id/Download/381375/PP%20Nomor%2028%20Tahun%202025.pdf ；https://lsbu.center/gkb/uploads/produk_hukum/f0ae773a8ddecf315f1036356b0aa68d_2026-01-20.pdf ；https://lib.ui.ac.id/detail?id=9999920519556&lokasi=lokal | 三次搜尋（含 1 次保留額度）均無法自摘要讀出 PP 28/2025 附錄 I 的持股欄位。Permen PU 6/2025 原文確認「各 KBLI 之 BUJK 義務依 PP 28/2025 附錄 I 矩陣」，並對 BUJK PMA 要求大型資格 SBU 與母國法人身分，但未見持股百分比。最終報告**不得**把 67%/70% 寫成現行規定，亦不得寫成「已 100% 開放」。 |
| 17 | 室內設計 KBLI 代碼改碼（B §1、§4.1） | KBLI 2020 代碼 74120 → KBLI 2025 代碼 74191 | ✅ **確認** | 維持；補充：OSS 已建 74191 頁面；代辦網站稱 OSS 自 2026-06-16 起新登記採 KBLI 2025、既有 2020 代碼登記仍有效（待官方確認） | https://dpb.unpad.ac.id/kbli2025/74191/ ；https://oss.go.id/kbli/detail/6eba6cb7-518d-4a04-a7d1-41a602c0f763 ；https://kbli.co.id/74191 | 74191 範圍含室內設計之調查、可行性研究、繪圖、意象圖、監造、估價／QS、專案管理；不含建築設計（71101）。 |
| 18 | KBLI 74191 可 100% 外資（B §1、§4.1、§9） | 顧問網站稱可 100% 外資、Balizero 自評信心 MEDIUM | ❓ 無法查證 | 寫「顧問網站稱無外資上限、PT PMA 須登記為大型企業（投資額 > Rp 100 億）；**未見 Perpres 投資清單或 PP 28/2025 附錄明文**」 | https://kbli.co.id/id/74191 ；https://balizero.com/business/kbli-2025-foreign-ownership-pma-guide?lang=id | kbli.co.id 未引用任何法源；Balizero 另稱 PP 28/2025 依 KBLI 2025 更新持股比例並列有 49%／67%／95% 等有條件開放類別，與「無上限」說法未能互證。 |
| 19 | 室內設計公司須取得 SBU（B §2.2「重要觀察」、§4.1、§10） | OSS 要求「營造服務企業能力認定標準」即 SBU；方案代碼 AR003 | ✅ **確認**（子分類代碼待核） | SBU 要求確認（法源 Permen PUPR 8/2022）；子分類代碼兩來源不同：P3SM 方案文件標 **AR003**「建築物與土木建築之室內設計服務」，另一法務網站列 AR001、AR002、AL001–AL004；申請流程 OSS → LSBU → PUPR 入口 | https://prolegal.id/?p=32491 ；https://prolegal.id/?p=33828 ；https://news.sah.co.id/kode-kbli-74120-aktivitas-desain-interior-seperti-apa-tahap-mendapatkannya/?amp=1 ；筆記既有 https://p3sm.or.id/skema_files/AR003.pdf | 舊制（PP 5/2021）將 74120 列「中高風險」、需 NIB＋標準證書；PP 28/2025 下之風險等級須於 OSS 重新確認。 |
| 20 | BPS 建材／營造批發價指數 IHPB（A §1、§6、§8；B §1、§7） | 2026-06 指數 110.28（+1.32% mom、+8.68% yoy）；2026-08 +9.52% yoy；2026-09 +9.63% yoy（101.83→111.64） | ✅ **確認** | 維持；補充 2026-08 指數 111.43（+0.41% mom）；2026-09 IHPB 總指數 +6.76% yoy（+0.62% mom），推升項目為瀝青、鋼筋、水泥、碎石、砂 | https://goodstats.id/publication/perkembangan-indeks-harga-perdagangan-besar-september-2026-C2D3U ；https://bcasekuritas.co.id/latest-news/news/ihpb-september-2026-naik-676-harga-bijih-besi-dan-mineral-melonjak ；https://databoks.katadata.co.id/ekonomi-makro/statistik/3a6719d2aa29da8/indeks-harga-perdagangan-besar-ihpb-bahan-bangunan | A 與 B 的三個月份數字互相一致且與獨立來源相符；基期 2023=100（2025-01 起），跨基期只能比百分比。 |

**統計**：查核 20 項｜✅ 確認 11（#5、6、7、9、10、13、14、15、17、19、20）｜✏️ 修正 2（#3、#4）｜❌ 駁斥 1（#1）｜❓ 無法查證 6（#2、8、11、12、16、18）。

**未納入本輪獨立查核之項目**（搜尋配額用於上列更具決定性之項目；下列維持原報告值並標「未獨立查核」）：
- YLKI 2025 年申訴 1,977 件（住宅團體 919 件）、2024 年住宅申訴 49 件（B §3.1）。
- 外籍人員 RPTKA／DKP-TKA USD 100/月（PP 34/2021、Permenaker 8/2021；B §4.3 自標未驗證）。
- 雅加達營建工人日薪 Rp 165,000、全國 Rp 140,000（BPS 2025 Q2；A §3）；木工日薪 Rp 130,750；設計師月薪中位 Rp 575 萬（B §6）。
- CSAP 2025 營收 Rp 17.5 兆；AZKO 前三季 Rp 6.33 兆；HERO 2024 Rp 4.54 兆；Dekoruma 收購價 Rp 1.16 兆；Gravel／Kanggo／Fabelio（A §4）。
- 營造業占 GDP 9.82%（2025 Q3）；三百萬住宅計畫累計 324,213 戶；雅加達飯店 48,500 房（A §2、§3、§6）。
- C&W 2026 年版雅加達復原成本 USD 9–12/sqft（A §3）。
- 研究機構家具／家飾估值（IMARC、Mordor、Ken Research、Statista；A §2）：未查原始頁面，僅做定義審計（見 (b) B-6）。
- 住宅存量屋齡分布、新建／中古交易比、翻修頻率：兩份筆記均列缺口，本輪未搜尋；建議以 BPS《Statistik Perumahan 2026》（2026-08 首版，含 backlog-2 居住品質指標）補充。

---

## (b) 內部矛盾與定義問題

**B-1 室內設計 Rp 104.6 兆 是「比率誤套」（決定性）**：7.44% × 創意經濟 GDP ＝ Rp 104.6 兆，而 7.44% 是創意經濟占全國 GDP 的比率。A 把此數放進摘要、§2、§7、§8 總表並據以推論「設計＋施工服務與家具商品（USD 82–91 億 ≈ Rp 136–150 兆）同一量級」「占 GDP 0.47%」「人均 Rp 37 萬／TWD 700」。全部刪除。正確的對照是：家具商品市場（研究機構 USD 80–91 億）遠大於室內設計服務（官方未公布；量級估 Rp 1.6–8 兆 ≈ USD 1–5 億），結構為「服務極小、商品較大」，與 A 的結論相反。

**B-2 住房缺口年份錯置**：A 把 Susenas 2023 的 990 萬標成 2025 年；BPS 2025 年為 964 萬、2026 年 929 萬。A 的「2020 年 1,275 萬→2025 年 990 萬」應改為「2020 年 1,275 萬→2023 年 990 萬→2025 年 964 萬→2026 年 929 萬」。

**B-3 自有住宅戶比 82.38% 與 BPS 口徑不合**：BPS backlog-1 為 13.00%（2025），隱含擁有率約 87%；Ken Research 的 82.38% 來源不明，與 A 引用的同一 BPS 體系矛盾。

**B-4 翻修單價「輕／中／重」標籤跨筆記不可比**：A 的「輕度」Rp 250 萬/m²（Mitra10，含料包工）與 B 的「輕度」Rp 50–80 萬/m²（Medcom，接近純工資或表面工程）相差 3–5 倍；B §1 的「Rp 50 萬–1,000 萬/m²、差距逾 10 倍」是把「純工資包工」與「豪宅含料」混在同一軸上造成的人為放大。最終報告改用兩軸：純工資 Rp 100–150 萬/m²；含料 Rp 250–400 萬/m²；雅加達中高階 Rp 450–700 萬/m²（單一來源）。

**B-5 HDII DKI 分會數字同頁不同讀**：A 950+/90+ vs B 90+/40+（同 URL）。另 A 的「持證 1,897 人」與 2018 年官方口述「持證 200 人」相差近 10 倍（見 #11、#12）。

**B-6 研究機構家具估值定義互斥，不可並列成長率**：IMARC「家用家具 USD 96 億」大於其「家具全口徑 USD 91 億」（A 已標示）；Mordor「家用家具 USD 49.4 億」為 IMARC 的一半；Statista「營收」USD 33 億為零售端；B §4.4 引 Research and Markets（轉售 Mordor）2025 年 USD 79.7 億、CAGR 6.46%，與 A 引 Mordor 官網 USD 82.4 億、CAGR 6.10% 為**同一報告的不同版次**，兩筆記未對齊。建議標題只寫「家具商品市場 USD 80–91 億（2025，Mordor／IMARC 區間，定義各異）」，不列 CAGR 比較。

**B-7 創意經濟 GDP 新舊系列不可串接**：A 的 2024 年 Rp 1,611.2 兆（2026 年新系列）與公開舊系列（2022 年 Rp 1,280 兆、占 6.54%）若串接會得出兩年 +26% 的假成長；占 GDP 比率亦由舊系列 6.54%（2022）跳至新系列 7.07%（2023）／7.28%（2024）。引用時必須註明系列。

**B-8 匯率假設不一致**：A 用 1 USD = 31.5 TWD（1 TWD ≈ 524 IDR），B 用 32 TWD（1 TWD ≈ 516 IDR），同一印尼盾金額在兩筆記的台幣值相差約 1.6%（例：Rp 1,000 萬/m² → A 19,100 vs B 19,400）。A 註明與專案其他國家筆記一致，建議全案統一為 A 的 16,500／31.5；B 的 TWD 值乘以 0.984 重算。兩筆記的算式本身經逐項重算均正確（含 USD 58/sqft → 624/m²、Rp 34.64 兆 → USD 21 億、Rp 575 萬 → USD 348、1 坪 = 3.3058 m²）。

**B-9 SBU 子分類代碼不一致**：B 採 AR003（P3SM 方案文件），獨立來源列 AR001、AR002、AL001–AL004。兩者可能都存在（AR003 為室內設計專屬方案，其餘為建築／景觀類），但 B 未說明設計公司只需 AR003 或需多項，待 LPJK／LSBU 確認。

**B-10 PBG 罰則措辭**：B 寫「資產查封」，法條（PP 16/2021 第 45(1) 條）是對**建物**的警告、停工、查封、拆除，不是對資產的扣押。

**B-11 「持證設計師」與「SKK」概念混用**：A §9 以 HDII「持證 1,900 人」推論人才供給；B 則指 SKK 由 LSP 核發、分 7–9 級。兩者未對齊：HDII 的「sertifikasi」（協會認證／KTA）與法定 SKK 不是同一件事，報告應以 SKK（LPJK 登錄可查驗）為準。

**B-12 BI 銷量數字時效**：A 以 2026 Q1 −25.67% 作「短期承壓」結論，而 2026 Q2（−2.36%）已於 2026-08-07 發布並顯著回穩；A 研究日期 2026-10-08 本可取得。最終報告應同時給 Q1 與 Q2。

---

## (c) 整體評估

- **整體品質：中。** 政府與央行統計（FLPP、BI SHPR、BPS IHPB、BPS 缺口）、C&W 辦公室裝修成本、翻修與設計費行情、UU 2/2017 核心條文、PBG 制度、KBLI 改碼等 **11 項經獨立來源確認**，顯示兩位分析師的官方／半官方引用大體可靠，且 LENS B 誠實標示「既有知識未驗證」的條文經本輪查核全部成立（第 65、70 條）。
- **但最醒目的市場規模數字是錯的。** 「室內設計 Rp 104.6 兆／占 GDP 0.47%」為比率誤套，連帶 LENS A 的量級比較與人均推算失效；這是整份印尼筆記唯一可能誤導決策的錯誤，必須在最終報告中移除並以「無官方數字、量級遠小於家具商品市場」取代。
- **年份與定義錯置是第二類問題**：缺口 990 萬標錯年份；自有率 82.38% 口徑不明；翻修單價標籤跨筆記不可比；HDII 數字同頁不同讀；創意經濟 GDP 新舊系列混用。這些不是捏造，而是二手來源未對齊，整合時以本報告 (d) 的建議值取代即可。
- **法規面最大缺口仍是外資持股上限現況**（PP 28/2025 附錄 I）與 KBLI 74191 純設計公司是否真可 100% 外資；本輪三次搜尋證實學界與法律顧問對此意見相反，必須由印尼律師以原文裁定後，台灣業者才能決定持股結構。消費者保護面，印尼**沒有裝修專屬的法定保固期或押金規範**，唯一法定責任是 UU 2/2017 第 65 條的「建築失效」10 年上限；公寓裝修押金屬管委會規則而非法律。
- **未獨立查核的項目**（上市公司財務、工資、YLKI、RPTKA、研究機構估值）多為可直接查公司公告或 BPS 表格的事實，風險低；但 C&W 2026 年版與 HDII 持證人數宜於下一輪補查。

---

## (d) 建議採用值（最終報告標題數字）

| 指標 | 建議採用值 | 年份 | URL | 信心 |
|---|---|---|---|---|
| 室內設計服務產值 | **不給點值。** 寫「印尼無官方室內設計／裝修市場統計；室內設計為創意經濟小型子部門，量級估 Rp 1.6–8 兆（≈ USD 1–5 億，本查核推算），遠小於家具商品市場」 | 2024 | https://ekonomi.bisnis.com/read/20200830/12/1284797/tiga-subsektor-ekonomi-kreatif-jadi-penyumbang-terbesar-pdb ；https://www.kompas.id/artikel/majukah-industri-kreatif-indonesia | 低（量級） |
| 創意經濟 GDP | Rp 1,611.2 兆、占 GDP 7.28%（2026 年發布之新系列；不可與 2022 年 Rp 1,280 兆舊系列串接） | 2024 | 筆記既有 https://databoks.katadata.co.id/pdb/statistik/6a3893afd20b3/kontribusi-sektor-ekonomi-kreatif-terhadap-pdb-ri-terus-tumbuh-sampai-2024 ；舊系列 https://databoks.katadata.co.id/infografik/2024/04/29/nilai-pdb-ekonomi-kreatif-indonesia-meningkat-usai-pandemi | 中 |
| 家具商品市場（非裝修服務） | USD 80–91 億（Mordor／IMARC 區間；定義各異，不列 CAGR） | 2025 | 筆記既有 https://www.mordorintelligence.com/industry-reports/indonesia-furniture-market ；https://www.imarcgroup.com/indonesia-furniture-market | 中低 |
| 住房自有缺口（backlog-1） | **964 萬戶（13.00%）**；2026 年 929 萬戶（12.39%）；2023 年 990 萬戶；2020 年 1,275 萬戶 | 2025／2026 | https://www.bps.go.id/en/news/2026/08/22/937/bps-rilis-perdana-statistik-perumahan-2026--akses-rumah-layak-huni-meningkat.html ；https://pasardana.id/news/2026/8/14/bps-sebut-backlog-kepemilikan-rumah-tunjukkan-perkembangan-positif | 高 |
| 居住品質不達標（backlog-2，翻修需求代理） | 24.03%（2026）；25.33%（2025） | 2025–26 | 同上 BPS 2026-08-22 | 高 |
| 擁有自宅戶比 | 約 87%（= 100 − backlog-1 13.00%） | 2025 | 同上 | 中 |
| FLPP 補貼房貸放款 | 278,868 戶／Rp 34.64 兆（≈ USD 21 億）；2024 年 200,300 戶／Rp 24.6 兆 | 2025 | https://keuangan.kontan.co.id/news/bp-tapera-salurkan-dana-flpp-senilai-rp-3464-triliun-sepanjang-tahun-2025 | 高 |
| 一級市場房價指數 IHPR（yoy） | 2025 Q4 +0.83%；2026 Q1 +0.62%；**2026 Q2 +0.69%** | 2025–26 | https://www.bi.go.id/id/publikasi/laporan/Documents/SHPR_Tw_I_2026.pdf ；https://bcasekuritas.co.id/en/latest-news/news/survei-bi-harga-properti-residensal-naik-terbatas-di-triwulan-ii-2026 | 高 |
| 一級市場銷量（yoy） | 2025 Q4 +7.83%；2026 Q1 −25.67%；**2026 Q2 −2.36%** | 2025–26 | 同上 | 高 |
| 房貸使用比例（一級市場） | 69.87% | 2026 Q1 | https://www.bi.go.id/id/publikasi/laporan/Documents/SHPR_Tw_I_2026.pdf | 高 |
| 住宅翻修單價（含料包工） | **Rp 250–400 萬/m²**（≈ USD 152–242 ≈ TWD 4,800–7,600/m² ≈ 1.6–2.5 萬/坪）；純工資包工 Rp 100–150 萬/m² | 2025–26 | https://momsmoney.kontan.co.id/news/berikut-ini-estimasi-biaya-renovasi-rumah ；https://mamikos.com/info/cara-menghitung-biaya-renovasi-rumah-1-lantai-menjadi-2-lantai-gnr/ | 中高 |
| 雅加達中高階翻修 | Rp 450–700 萬/m²（單一承包商報價；Rp 700 萬以上僅該來源「豪華級」，不作標題） | 2026 | 筆記既有 https://heriskontraktor.id/artikel/biaya-renovasi-rumah/ | 低 |
| 純室內設計費 | **核心 Rp 20–70 萬/m²**（≈ TWD 380–1,340/m²）；全距 Rp 15–100 萬/m²；或造價 2–5%（較少用） | 2025–26 | https://www.archify.com/id/archifynow/perkirakan-biaya-membangun-interior-impian-anda-ini-caranya ；筆記既有 https://www.liputan6.com/hot/read/6024358/harga-jasa-desain-interior-2025-panduan-lengkap-amp-tips-memilih-desainer-profesional | 中 |
| 設計＋施工套裝 | Rp 350–1,000 萬/m²（單一來源 SPlusA） | 2025 | 筆記既有 https://splusa.id/biaya-interior-design-per-meter/ | 低 |
| 雅加達辦公室裝修（中等規格） | **USD 58/sqft ≈ USD 624/m²**（亞太最低；本幣 −16%） | 2025 | https://www.cushmanwakefield.com/en/singapore/news/2025/03/contractor-sentiment-generally-positive-as-the-worst-of-price-pressures-ease | 高 |
| 建材批發價通膨 IHPB（yoy） | **+9.63%（2026-09）**；+9.52%（2026-08）；+8.68%（2026-06）；2025 年多在 1–3% | 2026 | https://goodstats.id/publication/perkembangan-indeks-harga-perdagangan-besar-september-2026-C2D3U ；https://bcasekuritas.co.id/latest-news/news/ihpb-september-2026-naik-676-harga-bijih-besi-dan-mineral-melonjak | 高 |
| HDII 會員數 | 約 2,200 人／23 分會（單一媒體來源）；**持證人數不明**（2018 年僅約 200 人） | 2024／2018 | 筆記既有 https://konstruksimedia.com/hdii-siap-gelar-kongres-ke-16-momentum-regenerasi-dan-pengembangan-desain-interior-indonesia/ ；https://wartaekonomi.co.id/read187183/minim-ri-hanya-punya-200- | 低 |
| 匯率（全案統一） | 1 USD = 16,500 IDR；1 USD = 31.5 TWD；1 TWD ≈ 524 IDR | 2025–26 假設 | — | — |

---

## (e) 法規要點確認

| 要點 | 本輪確認內容 | 法源／主管機關 URL |
|---|---|---|
| 設計師與工程人員證照 | **UU 2/2017《營造服務法》第 70 條**：所有營造服務從業人員（含設計顧問類）須持工作能力證書 SKK；SKK 經能力測驗取得、由 BNSP 授權並在 LPJK 登錄之 LSP 核發；業主與服務提供者須聘用持證人員。室內設計 SKK 分 Ahli Muda（7 級）／Madya（8 級）／Utama（9 級）（分級依 B 筆記代辦來源，本輪未再核）。 | https://pasal.id/peraturan/uu/uu-no-2-tahun-2017 ；筆記既有法條全文 https://bphn.go.id/data/documents/17uu002.pdf ；https://www.industry.co.id/read/45797/sertifikasi-konstruksi-bukan-hanya-soal-kompetensi |
| 承包商／設計公司資格 | 室內設計在 OSS 被歸為營造顧問服務，公司須取得 **SBU（Sertifikat Badan Usaha）**，法源 Permen PUPR 8/2022；子分類代碼（AR003 vs AR001/AR002/AL001–004）待 LPJK／LSBU 確認；申請路徑 OSS → LSBU → PUPR 入口。 | https://prolegal.id/?p=32491 ；https://prolegal.id/?p=33828 ；筆記既有 https://p3sm.or.id/skema_files/AR003.pdf |
| 工程責任（唯一法定「保固」） | **UU 2/2017 第 65 條**：服務提供者對「建築失效」依規劃使用年限負責，使用年限逾 10 年者，自最終交付日起最長 10 年；期限須載於契約；施行細則 PP 22/2020（經 PP 14/2021 修正）。印尼**無**裝修專屬法定保固期；公寓裝修押金為管委會（P3SRS）規則，非法律。 | https://www.hukumonline.com/klinik/a/tanggung-jawab-kontraktor-lt4c692c9f31e6b/ ；https://klinikkonstruksi.jogjaprov.go.id/storage/images/peraturan/0ae8a_PP%20No%2022%20Th%202020%20ttg%20Peraturan%20Pelaks%20UU%20No%202%20Th%202017%20ttg%20JasKontr.pdf ；筆記既有 https://peraturan.bpk.go.id/Details/161844/pp-no-14-tahun-2021 |
| 住宅裝修許可 | **PP 16/2021**（建築法施行細則）：IMB 廢止、改 PBG；第 11(2) 條功能／分類變更須申請 PBG perubahan；第 253(3) 條 PBG 涵蓋新建、變更、擴建、縮建、維護；第 45(1) 條行政制裁：書面警告→停工→查封→拆除；第 347 條舊 IMB 仍有效、無 PBG 之既有建物須先辦 SLF；線上申辦 SIMBG，規費由地方訂定、各地不同。油漆、換磚等不變更建築者實務上免辦。 | https://www.detik.com/properti/tips-dan-panduan/d-7047030/pbg-adalah-persetujuan-bangunan-gedung-ketahui-perbedaannya-dengan-imb ；https://www.hukumonline.com/klinik/a/apakah-renovasi-rumah-akan-menaikkan-besar-pbb-lt5407f0d9ba6d6/ ；https://ekonomi.bisnis.com/read/20210225/47/1360852/jokowi-hapus-imb-diganti-pbg-apa-itu |
| 外資進入：純設計公司 | KBLI 2020 **74120** → KBLI 2025 **74191**「室內設計活動」（OSS 已有 74191 頁面；代辦網站稱 2026-06-16 起新登記採 KBLI 2025）。可否 100% 外資：顧問網站稱可，但**無 Perpres 投資清單或 PP 28/2025 附錄明文**，列為待印尼律師確認。PT PMA 須登記為大型企業（投資額 > Rp 100 億）。 | https://dpb.unpad.ac.id/kbli2025/74191/ ；https://oss.go.id/kbli/detail/6eba6cb7-518d-4a04-a7d1-41a602c0f763 ；https://kbli.co.id/id/74191 |
| 外資進入：營造／裝修承包（BUJK PMA） | PP 5/2021 附錄時期：非東協 67%／東協 70%（已確認為歷史規定）。**PP 28/2025**（2025 年 6 月，風險導向經營許可新規）取代 PP 5/2021，配套 **Permen PU 6/2025**（各 KBLI 之 BUJK 義務依 PP 28/2025 附錄 I 矩陣；BUJK PMA 須持大型資格 SBU 並為母國法人）。持股上限是否取消：Emerhub 2026 稱已取消（多數業別可 100%）、ASEAN Briefing 稱過渡期仍適用 67%/70%、Dentons HPRP 2026-05 有專文——**現況有爭議，須以 PP 28/2025 附錄 I 原文裁定**。另可走 BUJKA 代表處路徑（B 筆記，未再核）。 | https://peraturan.bpk.go.id/Download/381375/PP%20Nomor%2028%20Tahun%202025.pdf ；https://lsbu.center/gkb/uploads/produk_hukum/f0ae773a8ddecf315f1036356b0aa68d_2026-01-20.pdf ；https://emerhub.com/indonesia/foreign-construction-company-indonesia-2026/ ；https://www.aseanbriefing.com/news/indonesias-construction-boom-and-opportunity-for-foreign-contractors/ ；https://dentons.hprplawyers.com/en/insights/articles/2026/may/5/updates-to-indonesias-construction-services-business-licensing-regime |
| 外籍設計師工作許可 | RPTKA／DKP-TKA（PP 34/2021、Permenaker 8/2021、USD 100/人/月）：**本輪未查核**，維持 B 筆記「既有知識、未驗證」標示；外籍人員是否須持印尼 SKK 亦未查。 | 待查（下一輪） |
| 消費者保護與申訴 | 住宅申訴管道以建商糾紛為主（YLKI、BPKN、住宅部 BENAR-PKP 2025-03-26），**無裝修承包商專屬統計或法定押金／保固規範**；本輪未重新核 YLKI 件數。 | 筆記既有 https://pkp.go.id/berita/detail/kementerian-pkp-luncurkan-kanal-pengaduan-konsumen-perumahan-terpadu-benar-pkp |

---

## 附錄：本輪執行之獨立搜尋（16 次）

1. kontribusi subsektor desain interior terhadap PDB ekonomi kreatif persen BEKRAF subsektor terkecil（extended）
2. PDB ekonomi kreatif menurut subsektor "desain interior" triliun persen BPS Kemenparekraf statistik 2020 2021 2022（extended）
3. backlog rumah 9,9 juta 2025 Susenas BPS kepemilikan rumah persen Kementerian PKP
4. BP Tapera realisasi penyaluran FLPP sepanjang tahun 2025 unit rumah Rp triliun
5. Bank Indonesia SHPR triwulan I 2026 indeks harga properti residensial primer penjualan rumah turun
6. harga borongan renovasi rumah per m2 2026 kontraktor Jakarta material dan jasa
7. tarif jasa desainer interior per meter persegi 2026 atau persen dari RAB biaya konstruksi
8. Cushman Wakefield Asia Pacific office fit out cost guide 2025 Jakarta cheapest market USD per square foot
9. HDII Himpunan Desainer Interior Indonesia jumlah anggota bersertifikat seluruh Indonesia cabang provinsi kongres 2024
10. UU 2 tahun 2017 jasa konstruksi pasal 70 sertifikat kompetensi kerja wajib pasal 65 kegagalan bangunan paling lama 10 tahun
11. renovasi rumah apakah wajib PBG PP 16 tahun 2021 ubah struktur fungsi bangunan sanksi
12. PP 28 tahun 2025 lampiran sektor PUPR BUJK PMA kepemilikan modal asing paling banyak 67 persen ASEAN 70 persen（extended）
13. KBLI 74120 aktivitas desain interior PT PMA 100 persen asing OSS persyaratan sektor PUPR SBU
14. BPS IHPB bangunan konstruksi September 2026 naik persen tahun ke tahun semen besi beton
15. PP 28/2025 construction services foreign ownership limit BUJK PMA 67% ASEAN 70% still apply 2025 2026 Indonesia（extended）
16. （保留額度）Permen PU 6 Tahun 2025 BUJK PMA komposisi saham asing 67 persen 70 persen dihapus 100 persen asing jasa konstruksi lampiran PP 28 2025（extended）

下一輪建議補查（依優先序）：PP 28/2025 附錄 I 營造業別持股欄位原文；Perpres 投資清單對 KBLI 74191 之規定；HDII 持證人數與 DKI 分會數字；RPTKA／DKP-TKA 現行費率與外籍人員 SKK 要求；C&W 2026 年版雅加達數字；BPS 2025 Q2 雅加達工人日薪 Rp 165,000；YLKI 2025 申訴 1,977 件；CSAP／AZKO／HERO 財報與 Dekoruma 交易金額。
