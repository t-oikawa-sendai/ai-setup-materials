# Code Generator 5パターン横断比較 Decision & Rationale

対象成果物：`project-notes/2026-09-11-code-generator-5-pattern-comparison-reference.md`

本ファイルは、上記の生徒・利用者向け参考資料に関する判断履歴の正本である。

参考資料本文は利用者向けの比較内容に限定し、内部の判断履歴は本ファイルで管理する。

## Decision & Rationale

### 2026-09-11

#### 公開参考資料からDecision & Rationaleを分離

Decision:

`project-notes/2026-09-11-code-generator-5-pattern-comparison-reference.md` は、Root READMEから生徒・利用者が直接参照する公開参考資料として扱う。

同資料の本文から内部管理用の `Decision & Rationale` を分離し、本ファイルを判断履歴の正本とする。参考資料本文には本ファイルへのHTMLコメントだけを残す。

Reason:

参考資料の目的は、5パターンの比較結果と読み方を生徒・利用者へ提示することであり、内部の文書変更理由を本文末尾へ表示すると教材としての可読性を損なうため。

一方で、判断履歴自体は情報資産として保持する必要があるため削除せず、`AGENTS.md` §5.4の公開・教材向け文書の分離例外に従って管理用文書へ分離する。

Rejected:

- `Decision & Rationale` を判断履歴ごと削除する方式
- 内部判断履歴を公開参考資料の末尾へ表示し続ける方式
- すべての文書へ無条件に同じ分離方式を適用する方式

### 2026-09-11

#### 総合比較表をCode Generator適性順位順に並べ替える

Decision:

総合比較表は、左から `GPT-5.6 Sol`、`Gemini 3.1 Pro Personaあり`、`Claude Opus 5 High`、`Gemini 3.1 Pro Personaなし`、`Gemini 3.5 Flash Lite` の順に並べる。

Reason:

最終行で示しているCode Generator適性順位と列順を一致させ、利用者が総合順位と各評価項目を対応付けて読みやすくするため。

Rejected:

- モデル名や作成順を基準に列順を維持する方式
- 最終行だけ順位を示し、列順は順位と一致させない方式
