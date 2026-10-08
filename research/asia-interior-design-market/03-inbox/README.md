# 收件匣（Inbox）使用說明

把外部 AI 產出的市場調研報告放進對應子資料夾，Claude 會在整合階段讀取、分級、三角驗證。

## 資料夾

| 資料夾 | 放什麼 |
|---|---|
| `chatgpt/` | ChatGPT Deep research 回傳的報告 |
| `gemini/` | Gemini Deep Research 回傳的報告 |
| `claude/` | Claude.ai（Research 模式）回傳的報告 |
| `other/` | Perplexity、Grok、人工整理、購買的研究報告摘要、內部數據 |

## 命名規則

`<YYYYMMDD>_<AI>_<範圍>_<run序號>.md`

範例：
- `20261010_chatgpt_12market-overview_r1.md`
- `20261011_gemini_tier1-JP-KR-SG-HK_r1.md`
- `20261012_claude_theme-regulation_r1.md`
- `20261012_other_puregroup-internal-pricing.md`（內部數據，標 CONFIDENTIAL）

## 每份檔案開頭請加一段中繼資料（Claude 整合時會讀）

```
---
ai: chatgpt | gemini | claude | other
mode: deep-research | research | standard
date: 2026-10-10
scope: 12market-overview | tier1 | tier2 | tier3 | country:JP | theme:regulation ...
prompt_version: v1
notes: （使用者補充：例如「Deep research 跑了 22 分鐘」、「有被要求澄清問題，我回答了 XX」）
---
```

## 格式

- 優先 Markdown（.md）。PDF／Docx 也可以，但請同時存一份純文字版（.md 或 .txt），URL 才不會遺失。
- 不要刪除 AI 原始輸出中的來源 URL 與引用編號；整合時要逐條驗證。
- 內部數據（璞石自己的每坪單價、案量、毛利等）請獨立成檔、檔名含 `internal`，並在開頭標 `CONFIDENTIAL`。
