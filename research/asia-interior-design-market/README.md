# 亞洲室內裝修設計市場研究專案（Asia Interior Design Market Study）

**委託人**：Banson（璞石集團 CEO）
**總指揮**：Claude（本 repo 內的研究整合者）
**研究對象**：亞洲 12 個市場（台灣基準線＋三層分級）
**版本**：V1（2026-10-08）— 由 Claude 自主多代理研究產出；待整合 ChatGPT／Gemini／Claude.ai 外部調研後升版為 V2

## 目錄結構

| 路徑 | 內容 | 狀態 |
|---|---|---|
| `00-project-plan.md` | 專案計畫：研究問題、分層定義、WBS、多 AI 分工、時程、品質標準、風險 | V1 |
| `01-prompts/` | 給 Claude／ChatGPT／Gemini 的市場調研提示詞、各國模組範本、回報格式規範 | V1 |
| `02-integration-protocol.md` | 外部 AI 報告如何回收、分級、三角驗證、整合進 V2 的規則 | V1 |
| `03-inbox/` | **收件匣**：請把 ChatGPT／Gemini／Claude.ai 產出的報告放這裡（見內部 README） | 待收 |
| `04-research-notes/` | Claude 多代理研究的原始筆記（各國 2 視角 × 12、跨國主題 × 8）與對抗式查核紀錄 | V1 |
| `05-report/` | 正式報告：`asia-interior-design-market-report-v1.md` | V1 |

## 使用流程

1. 讀 `00-project-plan.md`，確認分層與研究問題。
2. 到 `01-prompts/` 複製對應提示詞，分別貼到 ChatGPT（Deep research 模式）、Gemini（Deep Research 模式）、Claude.ai（Research 模式）。
3. 把每份回傳報告依 `03-inbox/README.md` 的命名規則存入收件匣。
4. 通知 Claude（本 repo 會話）：「收件匣有新報告，請整合」→ 產出 V2。
5. V2 定稿後，再做決策簡報（V3）。

## 數字標示紀律（全專案通用）

- 【實際】＝有來源 URL、年份、定義明確，且經查核或多源一致。
- 【示意】＝假設模型、推估或單一來源未經交叉驗證；必附假設條件。
- 法規、稅務結論一律標註「需專業人士最終確認」。
