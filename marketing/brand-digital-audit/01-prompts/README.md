# 提示詞包（Prompt Pack）v1 — 使用說明

## 檔案

| 檔案 | 給誰 | 用途 |
|---|---|---|
| `chatgpt-prompt.md` | ChatGPT（Deep research） | r1 五品牌全模組逐頁開啟；r2 競品數字列 |
| `gemini-prompt.md` | Gemini（Deep Research） | g1 Google 生態專題（商家檔案、關鍵字排名、PageSpeed、YouTube、Trends、論壇）；r1 基本數字 |
| `claude-prompt.md` | Claude.ai（Research） | c1 定位與訊息分析、跨品牌一致性、競品定位圖；r1 基本數字 |
| `output-format-spec.md` | 正本 | 回報格式規範（三套提示詞內已內嵌） |
| `_core-brief.md` | 正本 | 研究簡報共用段落（三套提示詞內已內嵌；修改時改這裡再重組） |

重組指令（改了正本後執行）：
```bash
cd marketing/brand-digital-audit/01-prompts
for ai in chatgpt gemini claude; do
  { sed -n '1,/^=== 提示詞開始 ===/p' ${ai}-prompt.md; sed -n '/^=== 提示詞開始 ===/,/^## 研究簡報/p' ${ai}-prompt.md | sed '1d;$d'; cat _core-brief.md; echo; echo '## 回報格式（必須遵守）'; echo; sed -n '/^## 1\. 報告骨架/,$p' output-format-spec.md; echo; echo '=== 提示詞結束 ==='; } > /tmp/${ai}.md && mv /tmp/${ai}.md ${ai}-prompt.md
done
```

## 建議執行矩陣

| 次序 | 範圍 | ChatGPT | Gemini | Claude.ai | 優先級 |
|---|---|---|---|---|---|
| 1 | ChatGPT r1 五品牌全模組 | ✓ | | | **必跑** |
| 2 | Gemini g1 Google 生態專題 | | ✓ | | **必跑** |
| 3 | Claude.ai c1 定位與訊息分析 | | | ✓ | **必跑** |
| 4 | ChatGPT r2 競品數字列 | ✓ | | | 高（第 3 步比對報告的主要輸入） |
| 5 | Gemini r1 基本數字 | | ✓ | | 中（三角驗證） |
| 6 | Claude.ai r1 基本數字 | | | ✓ | 中（三角驗證） |

最低交付：1 到 3。完整交付：1 到 6。

## 操作步驟（每一次）

1. 開對應檔案，複製「=== 提示詞開始 ===」到「=== 提示詞結束 ===」之間全文。
2. 改第一行【範圍】。
3. 貼上、執行。ChatGPT 若問澄清問題，回「依提示詞內的預設執行」。Gemini 會先出計畫，核對 7 步驟後開始。
4. 等待（Deep research 通常 10 到 40 分鐘）。
5. 完成後複製**含 URL 的全文**，存入 `03-inbox/<ai>/`，檔名與開頭中繼資料依 `03-inbox/README.md`。
6. 全部跑完後通知 Claude：「收件匣有新報告，請整合」。

## 注意事項

- 社群數字每天變，三個 AI 盡量在同一週內跑完。
- Gemini 匯出後務必確認 URL 存在；沒有就回對話要求補列。
- 不要為了省字數刪掉 AI 的來源清單與附錄 CSV；整合時要逐條驗證。
- 外部 AI 看不到內部數據（GA4、廣告後台、電商後台）；那些走 `../internal-data-checklist.md`。
- 若 AI 回報「Instagram 需登入看不到互動數」是正常的；整合時以內部 Meta 洞察補。
