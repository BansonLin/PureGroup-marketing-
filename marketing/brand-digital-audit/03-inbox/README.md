# 收件匣（Inbox）使用說明

| 資料夾 | 放什麼 |
|---|---|
| `chatgpt/` | ChatGPT Deep research 回傳（r1、r2） |
| `gemini/` | Gemini Deep Research 回傳（g1、r1） |
| `claude/` | Claude.ai Research 回傳（c1、r1） |
| `internal/` | **CONFIDENTIAL** 內部匯出（GA4、GSC、Meta、廣告、電商、POS、CRM、LINE），依 `../internal-data-checklist.md` |

## 命名規則

外部：`<YYYYMMDD>_<AI>_<範圍>_r<n>.md`，例：`20261015_chatgpt_r1_r1.md`、`20261016_gemini_g1_r1.md`、`20261016_claude_c1_r1.md`
內部：`<品牌代碼>_<系統>_<期間>_<匯出日>.csv`，例：`pure-design_ga4_12m_20261015.csv`

## 外部報告開頭中繼資料

```
---
ai: chatgpt | gemini | claude
mode: deep-research | research
date: 2026-10-15
scope: r1 | r2 | g1 | c1
prompt_version: v1
notes: （例如「跑了 25 分鐘」「IG 互動數需登入看不到」）
---
```

## 內部匯出開頭中繼資料（另附 `<檔名>.meta.txt` 或在 `_intake-log.md` 填）

```
system: ga4 | gsc | gbp | meta | meta-ads | youtube | tiktok | threads | shop | shopee | pos | crm | line
account: （帳號或資源名稱，不含密碼）
exported_by: （職位即可）
exported_at: 2026-10-15
period: 2025-10-01..2026-09-30
timezone: Asia/Taipei
```

## 規則

- 不要刪除 AI 原始輸出中的來源 URL、引用編號與附錄 CSV。
- 內部匯出不含個資明細（姓名、電話、Email）。
- Gemini 匯出前確認 URL 有保留。
