# 資料字典與使用規則

key-metrics.csv 固定九欄，與總覽第8章一致。market為ISO風格兩碼，GLOBAL為跨國企業。value為原單位數值；範圍保留文字，缺值不以0代替。unit須連同value閱讀，%的20.06即20.06%，不是0.2006。year保留實際曆年、季度、財年、發布年與未知觀察期。definition內標示預測／示意及來源級別。所有採用數值均僅一個獨立原始機構，因此confidence全部為低，不因官方來源自動改高。

source-register.csv含本輪全部查核URL，包括失敗和D級；報告第7章只列實際取得正文且可用來源。publisher_group可用來去除同一報告、轉載與同機構重複來源。不同AI或不同URL不等於不同方法。

metric-audit.csv保留原值、原年份、四項查核、原文定位、修正後值及是否採用。excluded-metrics.csv是不可直接用於決策的原稿數字存檔，不得與key-metrics相加。

currency-conversions.csv換算採用的單一數值金額；range-currency-conversions.csv另保留11個金額區間的上下界（含+的不封頂性質），不取中間值。original_value×unit_multiplier÷fx_local_per_usd＝usd_value；twd_value＝usd_value×31.1663。保留原分母（每平方米、每案、每人等）。商辦C&W美元值已依顧問自身匯率形成，本表不把其原幣欄再套本報告匯率冒充完全一致。1坪＝3.3058m²，1ft²＝0.09290304m²。

fixed-exchange-rates.csv是固定比較參照，不是2026-10-09即期。大多為2025年均；印尼為2025年末中間價16782，越南為2025中央匯率年均。歐元使用1EUR＝1.1306USD倒數。USD為恆等式。

查核紀錄中的web_ref僅是本次研究定位碼，跨會話不保證可開啟；長期追溯請以完整URL、機構、標題、頁數／段落及查核日期為準。未附付費全文或第三方報告副本。

【示意】在此遵守委託方的單源規則，並不表示數值被虛構；政府原文查核通過與獨立三角驗證是兩件事。【預測／示意】不能當事後已發生的實績。【研究建議／規劃假設】不進市場原始指標資料。
