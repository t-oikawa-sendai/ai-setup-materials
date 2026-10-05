# Researcher Persona Decisions

対象成果物：

- `personas/education/GEM_RESEARCHER_FULL.md`
- `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
- `personas/education/GEM_RESEARCHER_DEVELOPMENT.md`
- `personas/reference/GEMINI_PERSONA.md`

本ファイルは、上記Researcher系Personaの判断履歴を管理する。各Persona本体の最新仕様の正本は各Personaファイルであり、本ファイルはその代替ではない。

## Decision & Rationale（決定・判断理由）

### 2026-10-05

#### Researcher系Persona 4ファイルの判断履歴を分離

Decision:

上記4ファイルの判断履歴を本ファイルへ分離し、各Personaの Document Info の直後からHTMLコメントで参照する。Persona本文には判断履歴を表示しない。AGENTS.md §5.4 の分離例外を、User決定により適用する。

Reason:

2026-10-05 の改訂は4ファイル共通の判断であり、各Persona内へ記録するとEducation 3ファイルに同一の記録が重複するため。判断履歴を1か所で追跡できるようにする。

Rejected:

- 各Persona末尾へ、同一ファイル内の `Decision & Rationale` として記録する方式
- `AGENTS.md` の `Decision & Rationale` へ記録する方式

#### 提示資料の扱いを追加

Decision:

Education 3種の5章末尾に `User-provided Materials（User提示資料の扱い）`、Reference の3章末尾に `User-provided Materials（提示資料の扱い）` を追加する。Education 3種の追加節は同一文とする。

- 要約・説明だけの依頼と、真偽・現在の有効性の確認依頼を区別する。要約・説明だけの依頼には外部検索を必須とせず、資料の記述を確認済み事実として示さない。
- 確認依頼では、質問が短くても資料の要約だけで完了しない。資料の発行元・対象・版・公開日を確認し、公式発行元の一次情報で該当記述を確認できた場合は、その資料をEvidenceとして使える。
- 資料が二次情報の場合、または出所を確認できない場合は、資料の外で一次情報を確認し、主張ごとに振り分ける（Education：確認済み事実／二次情報のみ／未確認。Reference：`VERIFIED`／`SUPPORTED`／`UNVERIFIED`）。
- 二次情報の資料そのものを、その資料の主張の根拠にしない。話題が関連するだけの公式ページを根拠にしない。資料と一次情報の矛盾は調査結果として示す。
- 回答前に、Evidenceと主張の対応、作業メモ・思考過程の混入を確認し、確認の過程・結果は出力しない。

Reason:

Version 1.0 のEducation用Researcher Gemが、User提示の二次記事URLと短い真偽確認の質問に対し、記事の要約で調査を完了し、その記事を確認済み事実・Evidenceとして提示した。同じ失敗はReference版でも起こり得る。

Version 1.0 には同趣旨の禁止規則が既に存在しており、規則の欠落ではなく不遵守の事例であったため、禁止の追加ではなく手順として明示した。原因は未特定である。

一次情報が存在しない場合の扱いを、既存の「二次情報しか確認できない場合は明示する」と矛盾しない形で定めた。公式資料が提示された場合は根拠として使えるようにし、要約だけの依頼には外部検索を強制しない。

内部記録：`project-notes/2026-10-05-researcher-persona-incident-record.md`

Rejected:

- 「URL＋短い質問」の入力形式に限定して外部検索を義務付ける方式
- User提示の二次情報について、必ず公式発表をEvidenceとすることを義務付ける方式
- User提示資料をすべてEvidenceから除外する方式
- 出所を問わず、二次情報だけでは確認済みにしない方式
- 同趣旨の規則を3章・5章・8章へ分散して追加する方式

#### Reference：停止条件を限定

Decision:

`GEMINI_PERSONA.md` 9章の停止条件「調査依頼の前提そのものが一次情報と矛盾している」を、「調査依頼の前提が一次情報と矛盾し、調査対象または目的の変更判断が必要になる」へ限定する。前提や提示資料と一次情報の矛盾は、根拠を付けて調査結果として報告し、調査を継続する。

Reason:

真偽確認では、提示資料の誤りを見つけること自体が調査結果であり、従来の規則ではその時点で停止する解釈が可能だったため。

Rejected:

- 前提と一次情報の矛盾を一律に停止条件とする方式

#### Reference：誤り時の原因の扱いを変更

Decision:

`GEMINI_PERSONA.md` 11章の誤り時の対応で、原因は確認できた範囲だけを示し、確認できない場合は「未特定」とする。仮説を示す場合は `INFERENCE` として事実と分ける。

Reason:

原因の説明を必須とする規則では、裏付けのない原因説明を作る余地がある。本件のインシデントレポートでも、AIの自己申告による未検証の原因説明が示されたため。

Rejected:

- 誤り時に原因の説明を常に必須とする方式

#### Reference：責務分担の記載を修正

Decision:

`GEMINI_PERSONA.md` 冒頭の責務分担を、「設計：ChatGPT、Gemini Gem、Owner」「実装：Cursor」「レビュー：Claude、ChatGPT、Owner」へ修正する。Gemini（本Persona）が設計・実装の最終決定を行わない規定は変更しない。

Reason:

従来の記載（設計：ChatGPT、実装：Cursor、レビュー：Claude）が、Userが示した実際の責務分担と一致していなかったため。

Rejected:

- 従来の記載を維持する方式
