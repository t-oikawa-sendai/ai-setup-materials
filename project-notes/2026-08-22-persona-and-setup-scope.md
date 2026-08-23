# Persona and Setup Materials Repository Scope

Last Updated: 2026-08-23
Status: CONFIRMED DECISION RECORD

## 運用更新（2026-08-23）

本記録のRepository責務と設定・運用資料方針は現行である。

`CURRENT.md` は現在地点のみを保持する。確定仕様の正本は対象成果物MDとする。記録方法の正本は `AGENTS.md` とする。

## Purpose

2026-08-22にUserが確定した、`ai-setup-materials` のRepository責務と、設定・運用資料の管理方針を記録する。

本記録は、既存Personaの機能仕様を変更するものではない。Persona機能設計、固定出力契約、現行配布文書の `Version 1.0 / Status Approved` は本決定によって変更しない。

## Repository Scope（Repository責務）

`ai-setup-materials` は、AI Personaと、そのPersonaを実際に利用するために直接必要な設定・運用資料に特化する。

### 対象

- Persona定義
- Personaの選択・使い分け
- Persona間の責務境界
- Persona利用に必要なREADME
- AIサービスへのPersona設定方法
- Personaの導入・切替・利用手順
- Persona運用に直接必要な設定資料

### 対象外

- 一般的な生成AI学習教材
- 要求定義・要件定義・各種設計などの一般教材
- アプリ開発用7文書
- 他Repositoryを正本とする教材本文・設計文書

### 背景意図（Repository責務）

Personaとその利用に直接必要な資料へ範囲を絞ることで、性質の異なる教材本文や設計文書が混在し、正本の所在が曖昧になることを防ぐ。

この責務限定は、Personaが学習用途で使われることを否定しない。否定するのは、Persona利用に直接必要ではない一般教材本文や、他Repositoryを正本とする文書を本Repositoryへ持ち込むことである。

## Seven Documents（7文書）

設計ドキュメント標準で扱う7文書は、`ai-setup-materials` では管理しない。

- 別Repository管理とする。
- 本Repositoryへ複製しない。
- 本Repositoryへ機械的に生成しない。
- 本RepositoryのPersona領域へ混在させない。

これにより、従来「Persona作成完了後に扱う最重要検討事項」として未決に置いていた「7文書を本Repository内へ配置するか別管理にするか」は、`別Repository管理` で解決済みとする。

### 既存確定事項との関係

- 「最大7文書は作成数の強制ではなく、AIによる文書増殖の防止と、Humanが情報の所在・修正箇所に迷わない状態を作るための上限・配置ルールである」という背景意図は維持する。本決定はこの背景意図と矛盾せず、`ai-setup-materials` における配置先を「本Repository外」として確定するものである。
- 「固定7文書を `ai-setup-materials` 内へ機械的に作成することは確定事項ではない」という既存確定事項は、本決定によって「作成しない」として確定した。
- `DESIGN_DOCUMENT_STANDARD.md` を全プロジェクト共通の統治原則として扱うこと、および `ai-setup-materials` へアプリ用テンプレートを機械適用しないことは、従来どおり維持する。
- 現在の別Repositoryとの不整合解消は、7文書を管理する側のRepositoryで扱う。本Repositoryの未決事項として保持しない。

## ASKME 迎合禁止

`ASKME 迎合禁止` を、本Repositoryの独立した検討事項・実装事項として扱わない。

本Repositoryの未決事項に残さない。

代わりに、既存PersonaおよびRepositoryルールに存在する次を維持する。

- Evidence優先
- Userが最終判断
- 問題があれば根拠を示して指摘
- 推測禁止
- 必要な場合の停止

### 背景意図（ASKME 迎合禁止）

上記の観点は既にPersonaとRepositoryルールへ実装されている。同じ目的の項目を別名の独立事項として追加すると、規則が重複し、どれが正本かが分かりにくくなる。したがって、新しい独立事項を設けず、既存の確定済みルールの維持で対応する。

## Separation of Persona and Setup Materials（Personaと設定資料の責務分離）

- Persona本文には、AIサービス固有のセットアップ手順、配置方法、操作手順を混在させない。
- 設定・運用資料はPersonaとは別文書として管理する。

### 背景意図（責務分離）

Personaは役割、責務境界、禁止事項、入出力方針を定義する文書である。ここへAIサービス固有の操作手順を混在させると、AIサービス側の仕様変更のたびにPersona本文を変更することになり、Personaの機能仕様と操作手順の変更理由を分離できなくなる。

## Setup Material Unit（設定・運用資料の単位）

- AIサービスごとに設定方法・配置場所が異なるため、設定・運用資料はAIサービス単位で管理する。
- Personaを提供するAIサービスには、原則として対応する最低限の設定・運用資料も提供する。
- この原則は既存Reference Personaにも適用する。

現在対象となるReference Persona：

- ChatGPT
- Claude
- Cursor
- Gemini

今後追加されるAIサービスについても、Personaを提供する場合は同原則を適用する。

### 背景意図（AIサービス単位）

AIサービス単位とする理由は、設定方法と配置場所がAIサービスごとに異なるためである。Personaだけを配布して設定方法を示さない状態を避けるため、Personaを提供するAIサービスには最低限の設定・運用資料も併せて提供する。

## Placement（配置）

設定・運用資料は各Persona区分配下で管理する。

想定配置：

```text
personas/
├─ education/
│  ├─ Persona本体
│  └─ setup/
│
└─ reference/
   ├─ Persona本体
   └─ setup/
```

- Gitは空ディレクトリを管理しない。本記録だけを目的として、空の `setup/` ディレクトリやダミーファイル（`.gitkeep` 等）を作成しない。
- 実際の設定・運用文書を作成するときに配置する。

この方針は、既存の保存構造の確定事項（Repository全体の入口をroot `README.md`、区分別の入口を `personas/<区分>/README.md`、現行Personaを `personas/<区分>/`、旧版を `personas/<区分>/archive/`、内部記録を `project-notes/`）と併存する。既存の確定事項を置き換えるものではない。

## Education Gemini

Education用Geminiについては、Researcher、Solution Partner、Code Generator、Reviewerごとに設定資料を4文書へ分割しない。

Gemini Gemの設定・運用を説明する共通資料1つとする。

具体的なファイル名と本文構成は今回決定していない。推測して作成しない。

## Not Changed by This Decision（本決定で変更しないもの）

- 現行Persona本文の機能仕様。
- Personaの固定出力契約。
- 現行配布文書13件の `Version 1.0 / Status Approved`。
- 完了済みのResearcher、Reviewer、Education用4Gemの設計。
- 文書適合性復旧の完了記録。
- Git同期ゲート、AI能力に関する安全前提、背景意図の保全、情報資産保全の各ルール。

## Unresolved（未決）

- 設定・運用資料の具体的なファイル名と本文構成。
- 各AIサービスの設定・運用資料に記載する項目の詳細。

いずれも今回決定していないため、推測して作成しない。Userの確定後に作成する。

## References

- `AGENTS.md`（Repositoryの恒久ルールと目的）
- `project-notes/CURRENT.md`（現在地点。確定仕様の正本ではない）
- `project-notes/2026-08-22-design-document-standard-application-scope.md`（設計文書標準の適用境界）
- `project-notes/2026-08-22-document-conformance-recovery-completion.md`（文書適合性復旧の完了状態と検証Evidence）
- `project-notes/2026-08-21-ai-information-asset-safety.md`（情報資産保全方針）
