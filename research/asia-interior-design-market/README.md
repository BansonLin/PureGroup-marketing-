# 亞洲室內裝修設計市場研究專案（Asia Interior Design Market Study）

**委託人**：Banson（璞石集團 CEO）
**總指揮**：Claude（本 repo 內的研究整合者）
**研究對象**：亞洲 12 個市場（台灣基準線＋三層分級）
**版本**：**V2（2026-10-10）**— V1（Claude 多代理研究，2026-10-09）整合三份外部調研：ChatGPT r2（462 列指標開頁核對）、Claude r1（另一 Claude 會話的獨立研究，1,733 條來源）、Gemini（無 URL，僅作對照）；經 38 個整合／審查代理三角驗證與一致性審查。下一版 V2.1 待璞石內部數據校準台灣基準線。

## 目錄結構

| 路徑 | 內容 | 狀態 |
|---|---|---|
| `00-project-plan.md` | 專案計畫：研究問題、分層定義、WBS、多 AI 分工、時程、品質標準、風險 | V1 |
| `01-prompts/` | 給 Claude／ChatGPT／Gemini 的市場調研提示詞、各國模組範本、回報格式規範 | V1 |
| `02-integration-protocol.md` | 外部 AI 報告如何回收、分級、三角驗證、整合進 V2 的規則（§11、§11.1 為 V2 裁決規則） | V2 |
| `03-inbox/` | **收件匣**：ChatGPT r2、Gemini、Claude r1 三份外部調研原檔與其查核資料；回收登記 `_intake-log.md` | 已收 3 份；內部數據待收 |
| `04-research-notes/` | V1 原始筆記與對抗式查核；`integration/` 為 12 市場 V1 × ChatGPT × Claude × Gemini 指標對照表；`verification/adjudication-log-v2.md` 為 V2 矛盾裁決 | V2 |
| `05-report/` | **V2 全文** `asia-interior-design-market-report-v2.md`／`.pdf`（523 頁）、V2 各章 `chapters-v2/`、變更紀錄 `v1-to-v2-changelog.md`（1,783 項）、V2 審查紀錄 `_qa-log-v2.md`；V1 全文與各章保留供對照 | V2 |
| `tools/` | 報告組裝（`assemble_report_v2.py`）與 PDF 產製（`pdf/build.sh`） | V2 |

## 使用流程

1. 讀 `00-project-plan.md`，確認分層與研究問題。
2. 到 `01-prompts/` 複製對應提示詞，分別貼到 ChatGPT（Deep research 模式）、Gemini（Deep Research 模式）、Claude.ai（Research 模式）。
3. 把每份回傳報告依 `03-inbox/README.md` 的命名規則存入收件匣。
4. 通知 Claude（本 repo 會話）：「收件匣有新報告，請整合」→ 產出 V2（已完成）。
5. 提供璞石內部數據（`02-integration-protocol.md` §8；空白範本在 `03-inbox/chatgpt/data/templates/`）→ V2.1 校準台灣基準線。
6. V2.1 後做一頁決策＋簡報（V3）。

## 數字標示紀律（全專案通用）

- 【實際】＝有來源 URL、年份、定義明確，且經查核或多源一致。
- 【示意】＝假設模型、推估或單一來源未經交叉驗證；必附假設條件。
- 法規、稅務結論一律標註「需專業人士最終確認」。
