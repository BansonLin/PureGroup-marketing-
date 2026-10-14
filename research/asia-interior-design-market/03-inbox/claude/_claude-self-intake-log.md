# 收件匣回收登記表（Intake Log）

依 `02-integration-protocol.md` §1 建立。每份進收件匣的報告登記一列；格式檢查依 `01-prompts/output-format-spec.md`（總覽／分層）與 `01-prompts/country-module-template.md`（單一市場）。

最後更新：2026-10-10（Claude）

## 1. 登記表

| # | 檔名 | AI | 模式 | 範圍 | 日期 | 字數（中日韓字元，含表格） | 來源數 | 在地語言來源數 | CSV 指標列 | 格式檢查 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `claude/20261009_claude_12market-overview_r1.md` | Claude | Claude Code 雲端會話多代理 Research（非 Claude.ai） | 12 市場總覽 | 2026-10-09 | 102,956（第 1–6 章約 4.1 萬） | 1,733 | 1,043（報告自報；腳本計 1,048） | 1,050 | 通過：0–8 章骨架、12×13 比較表無空白、每市場 10 節、附錄每市場 ≥15 列。缺項：菲律賓在地語言來源 3 條（<5）；越南搜尋 13 次（<15） |
| 2 | `claude/20261010_claude_country-TW_r1.md` | Claude | Claude Code 雲端會話 Research（以 r1 筆記為基底＋補搜 30 次） | 單一市場：台灣 | 2026-10-10 | 10,795 | 135 | 123 | 38 | 通過：範本 0–7 節、10 題、台灣錨點、CSV ≥15 |
| 3 | `claude/20261010_claude_country-JP_r1.md` | Claude | 同上（補搜 30 次） | 單一市場：日本 | 2026-10-10 | 12,812 | 124 | 106 | 38 | 通過 |
| 4 | `claude/20261010_claude_country-SG_r1.md` | Claude | 同上（補搜 30 次） | 單一市場：新加坡 | 2026-10-10 | 11,248 | 182 | 8（簡中；另 gov.sg 41、在地機構 11） | 41 | 通過（新加坡官方語言含英文，在地語言只計中文） |
| 5 | `claude/20261010_claude_country-MY_r1.md` | Claude | 同上（補搜 30 次） | 單一市場：馬來西亞 | 2026-10-10 | 11,812 | 186 | 56（馬來文、華文） | 33 | 通過 |
| 6 | `claude/20261010_claude_country-VN_r1.md` | Claude | 同上（補搜 30 次） | 單一市場：越南 | 2026-10-10 | 10,403 | 136 | 108（越南文） | 31 | 通過 |

計數方式：字數＝檔案中的中日韓字元數（含表格與來源清單，正文字數見各報告第 0 章）；來源數＝來源清單中含 URL 的列；在地語言來源以各報告第 0 章自報為準，腳本以來源清單「語言」欄非英文者交叉檢查。

## 2. 共同限制（所有 Claude 報告）

| 項目 | 狀態 | 對整合的影響 |
|---|---|---|
| URL 是否實際開啟 | **否**。本環境網路政策封鎖直接開頁（WebFetch／curl 全部失敗），所有來源只經搜尋結果內容讀取，標「讀取方式：搜尋結果內容」 | §3 逐條驗證尚未執行；在驗證前，這些報告的數字不得因「已開頁」而加權；見 `04-research-notes/verification/inbox-20261009_claude_12market-overview_r1-check.md` |
| 與 V1 的獨立性 | 研究與撰寫都未讀取 `04-research-notes/`、`05-report/` | 可作為 V1 的獨立比對來源；但 V1 與本批報告都出自 Claude，若引用同一原始來源，依 §4 只算 1 個來源 |
| 單一市場深潛與 r1 總覽的關係 | 深潛以 r1 筆記為基底再補搜，**不是**獨立於 r1 的第二個來源 | 三角驗證時，同一市場的 r1 總覽與深潛視為同一來源群 |
| 搜尋配額 | 每回合 200 次全體共用；r1 合計 397 次成功搜尋，深潛每市場 30 次 | 缺口較多的市場（越南、菲律賓）信心偏低 |

## 3. V2 觸發條件

| 條件（§9） | 目前 | 狀態 |
|---|---|---|
| 收件匣 ≥ 3 份 r1（12 市場總覽） | 1 份（Claude） | **未達**：待 ChatGPT r1、Gemini r1 |
| 璞石內部數據（§8，CONFIDENTIAL） | 0 份 | 待提供；清單見 `04-research-notes/verification/v2-integration-prep.md` |

## 4. 待收清單

| 檔名（建議） | 來源 | 優先序 |
|---|---|---|
| `chatgpt/<YYYYMMDD>_chatgpt_12market-overview_r1.md` | ChatGPT Deep research，貼 `01-prompts/chatgpt-prompt.md` | 1 |
| `gemini/<YYYYMMDD>_gemini_12market-overview_r1.md` | Gemini Deep Research，貼 `01-prompts/gemini-prompt.md` | 1 |
| `other/<YYYYMMDD>_other_puregroup-internal-pricing.md` | 璞石內部數據（CONFIDENTIAL） | 1 |
| `chatgpt|gemini/<YYYYMMDD>_<ai>_country-<代碼>_r1.md` | 各 AI 單一市場深潛（台、日、新、馬、越優先） | 2 |
