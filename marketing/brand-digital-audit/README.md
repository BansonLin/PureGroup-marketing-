# 璞石集團品牌數位資產盤點與行銷計畫（Brand Digital Audit & Marketing Plan）

**委託人**：Banson（璞石集團 CEO）
**總指揮**：Claude（本 repo 會話）
**對象**：璞石創研、璞石好室、璞域國際企劃、Wayhome 宜蘭店、Homatch（排除璞遇投資、相乘創研）
**版本**：**V0.1（2026-10-13）**，範圍待 CEO 確認後凍結為 V1.0
**沿用框架**：`research/asia-interior-design-market/`（提示詞包、整合協議、收件匣）

## 四步驟與對應檔案

| 步驟 | 內容 | 檔案 | 狀態 |
|---|---|---|---|
| 第 0 步 | 範圍凍結：品牌、目標錨點、競品、數據權限、執行承接、品牌架構、網路政策 | `00-scope-confirmation.md`（CEO 勾選）、`00-project-plan.md`、`digital-asset-inventory.md`、`competitor-set.md` | 待 CEO 回傳 |
| 第 1A 步 | 外部盤點：三 AI 分工 | `01-prompts/`（ChatGPT r1/r2、Gemini g1/r1、Claude.ai c1/r1） | 提示詞已就緒 |
| 第 1B 步 | 內部數據匯出 | `internal-data-checklist.md` → `03-inbox/internal/` | 清單已就緒 |
| 第 1C 步 | Claude 自查（官網技術體檢、一致性） | `04-research-notes/claude-audit/` | 待網路政策放寬 |
| 第 2 步 | 整合 → 盤點報告＋快速修正清單 | `02-integration-protocol.md` → `05-report/01-digital-asset-audit-v1.md`、`05-report/00-quick-fixes.md` | 待收件 |
| 第 3 步 | 競品比對報告 | `05-report/02-competitor-benchmark-v1.md` | 待第 2 步 |
| 第 4 步 | 行銷計畫（集團 1＋BU 5）＋執行表 | `05-report/03-marketing-plan-v1.md` | 待第 3 步 |

## 目錄

| 路徑 | 內容 |
|---|---|
| `00-scope-confirmation.md` | **CEO 要填的一頁**：A 品牌、B 目標、C 競品、D 數據權限、E 執行承接、F 品牌架構、G 網路政策 |
| `00-project-plan.md` | 決策問題、範圍、WBS、多 AI 分工、時程、來源分級、風險、治理 |
| `digital-asset-inventory.md` | 五品牌全部已知網址（CEO 提供＋搜尋補查）與待確認資產 |
| `competitor-set.md` | 每 BU 競品草案（固定＋自動補足規則）與關鍵字組 |
| `internal-data-checklist.md` | 13 個系統的匯出步驟（逐字介面名稱）、檔名規則、回收率門檻 |
| `01-prompts/` | 三套可直接貼上的提示詞＋正本（核心簡報、格式規範） |
| `02-integration-protocol.md` | 與亞洲市場專案協議的差異：快照型指標驗證規則、對內對外版 |
| `03-inbox/` | 收件匣（外部三 AI＋內部 CONFIDENTIAL） |
| `04-research-notes/` | 單一事實表、裁決紀錄、Claude 自查筆記 |
| `05-report/` | 快速修正清單、盤點報告、比對報告、行銷計畫 |

## 數字標示紀律

- 【實際】＝ 內部匯出，或平台直讀且附 URL 與擷取日（快照）。
- 【示意】＝ 第三方估計、單一來源未驗證、或 mock 數字；必附假設。
- 【評估】＝ Claude 的判斷或推論。
- 內部數據只進 `03-inbox/internal/` 與對內版報告。
