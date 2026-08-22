# Design Document Standard Application Scope

Last Updated: 2026-08-22
Status: CONFIRMED DECISION RECORD

## Purpose

`DESIGN_DOCUMENT_STANDARD.md` を全プロジェクト共通の設計文書統治原則として扱いながら、アプリプロジェクトとは性質が異なる `ai-setup-materials` へ適用する境界を記録する。

## Constitutional Position

`/Users/takashioikawa/Dev/solacom_main/docs/standards/DESIGN_DOCUMENT_STANDARD.md` は、ユーザーが作成する全プロジェクトの設計文書統治における憲法として扱う。

ただし、同標準はアプリプロジェクトを主な適用対象として想定している。教材、Persona、標準資料を管理するRepositoryである `ai-setup-materials` へ、アプリ用の文書構成やテンプレートを100%機械的に適用しない。

## Mandatory Governance Principles

`ai-setup-materials` では、次の統治原則を必須適用する。

- SSOTを明確にする。
- 文書ごとの責務を分離する。
- 命名・表記の一貫性を保つ。
- ヘッダー、状態、版管理を追跡可能にする。
- 文書間の導線を明確にする。
- 履歴を管理し、現行情報と旧情報を区別する。
- AIによる無秩序な文書の追加、変更、統合、削除を禁止する。
- 正本、適用関係、上書き関係を確認できない場合は停止する。
- 重複と更新不整合を防止する。

適用対象外のアプリ用構成があることを理由に、これらの統治原則まで免除してはならない。

## Application-Specific Requirements Not Mechanically Applied

次は、`ai-setup-materials` へ固定要件として機械的に適用しない。

- READMEと6文書を必ず作成する固定構成
- アプリプロジェクト固有の文書名
- UI、データ、API、アーキテクチャ、スクリーンショット等、`ai-setup-materials` に該当しない必須構成

適用対象だけを使用する。固定7文書を `ai-setup-materials` 内へ作成することは、今回の確定事項ではない。

## Notation Normalization Boundary

`English（日本語）` 等の表記統一は、意味、責務、契約、入出力仕様を変えない範囲に限って適用する。

表記変更が確定済みの仕様変更になる箇所は修正せず、例外適用として現行の正式名称・表記を維持する。例外候補には、User確認済みの正式出力名、役割名、判定名、状態名、項目名、列名、固定文言等を含む。ただし、これらを機械的にすべて例外とせず、正本で確定したものに限る。

この例外適用は、現在の確定仕様を表記修正だけで壊さないための一時的な互換性保留であり、永久固定ではない。将来、仕様変更として別途検討し、Userが承認した段階で、`English（日本語）` 表記への統合対象になり得る。

例外は表記の「統一漏れ」と混同せず、例外箇所、根拠、維持理由、再検討条件または解除条件を追跡可能にする。例外を理由に、未期限・無条件で不統一を固定化しない。例外解除をAIが自動決定しない。表記統一を理由にPersonaの機能仕様を再設計しない。

## English-Japanese Notation Scope

`English（日本語）` 表記は、次の構造上の項目名へ適用する。

- 文書タイトル
- 章・節見出し
- 文書管理項目
- 表の列名

通常の本文・説明文には、英語併記を機械的に適用しない。

Personaの正式な出力項目名、判定名、状態名、固定文言等は、表記変更によって確定済みの機能仕様または出力契約が変わる場合、修正せず一時例外として記録する。例外ではない日本語のみ、または英語のみの構造上の項目名は、`English（日本語）` への統一対象とする。

英語名と日本語名の対応は、既存の意味、責務、利用条件を変えないものに限る。翻訳を理由に、説明、要件、必須項目、処理、責務を追加または削除しない。

### Temporary Notation Exceptions Confirmed by Audit

現行Personaの出力形式を監査し、次を表記統一の一時例外として維持する。例外対象は記載した固定項目名・固定テンプレートに限定し、その周囲の通常の文書タイトル・章節見出しまで例外へ広げない。

1. Education Researcher 3文書
   - 例外箇所：`Active Modules`、`Solution Partnerへの引き渡し` 内の引き渡し項目名、`出力` 内の出力項目名
   - 根拠：現行Researcherの有効Module表示、引き渡し内容、出力順を構成する機能仕様である。
   - 維持理由：表記変更がGemの固定出力・引き渡し契約を変更し得るため。
2. `personas/education/GEM_CODE_GENERATOR.md`
   - 例外箇所：`Code Generation Report` と、その配下の固定出力項目名
   - 根拠：Code GeneratorがUserへ返す出力形式を定義している。
   - 維持理由：項目名の変更がCode Generatorの出力契約変更になるため。
3. `personas/education/GEM_SOLUTION_PARTNER.md`
   - 例外箇所：`Code Generatorへのコード生成用引き渡し` 内の固定項目名と、`出力` 内の固定出力項目名
   - 根拠：Code Generatorへの引き渡し内容とSolution Partnerの回答順を定義している。
   - 維持理由：項目名の変更が引き渡し・出力契約変更になるため。
4. `personas/education/GEM_REVIEWER.md`
   - 例外箇所：`総合判定`、`対応方針一覧`、`修正案一覧表`、各指摘の必須項目、`User向け説明`、`Code Generatorへの修正指示`、`Solution Partnerとの打ち合わせ用情報`、`Userが判断する事項`、`最終設計ドキュメント更新情報`、判定値、最終設計ドキュメントの状態値、固定案内文
   - 根拠：Reviewer再構築でUser確認済みの正式名称・出力契約であり、`project-notes/CURRENT.md` のReviewer再構築仕様に記録されている。
   - 維持理由：表記変更がReviewerの確定済み機能仕様を変更するため。
5. `personas/reference/CLAUDE_PERSONA.md`
   - 例外箇所：`本格レビュー` の fenced Markdownテンプレート内の固定見出し・項目名
   - 根拠：Claude Personaのレビュー出力形式を定義している。
   - 維持理由：テンプレート変更が出力契約変更になるため。
6. `personas/reference/CURSOR_PERSONA.md`
   - 例外箇所：fenced code内のコードヘッダー項目名と、`Report` の fenced Markdownテンプレート内の固定見出し・項目名
   - 根拠：Cursor Personaの生成コードヘッダーと作業報告形式を定義している。
   - 維持理由：テンプレート変更が生成物・報告契約変更になるため。
7. `personas/reference/GEMINI_PERSONA.md`
   - 例外箇所：`比較・技術選定調査` の fenced Markdownテンプレート内の固定見出し・項目名・表の列名
   - 根拠：Gemini Personaの比較調査出力形式を定義している。
   - 維持理由：テンプレート変更が出力契約変更になるため。

各例外の再検討・解除条件は共通とする。該当Personaの出力仕様または引き渡し仕様を変更対象として別途検討し、Userが仕様変更を明示承認した場合に限り、`English（日本語）` 表記への統合を再検討する。解除条件を満たす前にAIが自動変更しない。

## Header Application Scope

現行配布文書には、統一した標準ヘッダーを適用する。現行配布文書には、次を含む。

- root `README.md`
- `personas/education/README.md`
- 現行Education Persona
- `personas/reference/README.md`
- `personas/reference/` の現行Persona

`project-notes/` は、作業状態、判断経緯、実装指示、監査Evidence等を記録する内部領域である。配布文書用の完全ヘッダーを機械的に適用せず、既存の簡易ヘッダーを維持する。

`archive/` は履歴本文を保存する領域である。旧本文と旧ヘッダーを書き換えず、冒頭のArchive Noticeだけを統一する。Archive Noticeでは、少なくとも次を追跡可能にする。

- 履歴資料であること
- 現行利用禁止
- 状態
- 置換先
- 旧本文を保存していること

## Archive Notice Format

全Archive文書の冒頭に、次の順序で統一したArchive Noticeを配置する。

1. `# Archive Notice（アーカイブ通知）`
2. 見出し直下の利用禁止表示
3. `Item（項目）` / `Value（値）` の管理表
4. 区切り線
5. 変更しない旧本文・旧ヘッダー

見出し直下には、次を独立した引用表示として明記する。

```markdown
> **Do Not Use（利用禁止）**
>
> この文書は履歴資料です。現行仕様、現行Persona、現行運用の根拠として使用しないでください。
```

管理表には、次の5項目を記載する。

- `Archive Type（アーカイブ種別）`：`Historical Material（履歴資料）`
- `Status（ステータス）`：`Deprecated`
- `Usage（利用可否）`：`Do Not Use（利用禁止）`
- `Replaced By（置換先）`：現行文書へのリンク
- `Preservation（保存方針）`：`Original Body Preserved（旧本文を変更せず保存）`

利用禁止は、見出し直下の警告と管理表の `Usage（利用可否）` の二重で表示する。Statusだけに利用禁止の意味を依存させない。

既存Archive Noticeの `SUPERSEDED` はNotice内で `Deprecated` へ統一し、置換関係は `Replaced By（置換先）` で維持する。`personas/education/archive/GEM_RESEARCHER.md` にはArchive Noticeが存在しないため、同じ形式を旧本文の前へ追加する。

Archive Noticeの置換・追加後も、区切り線より下にある旧本文と旧ヘッダーは変更しない。

## Standard Header Fields

現行配布文書の標準ヘッダーは、次の7項目で統一する。

- `Document ID（文書ID）`
- `Version（バージョン）`
- `Status（ステータス）`
- `Created Date（作成日）`
- `Last Updated（最終更新日）`
- `Owner（管理者）`
- `Related Documents（関連文書）`

ヘッダー表の列名は、`Item（項目）` と `Value（値）` で統一する。

この決定は項目名と列名の統一を確定する。`Created Date（作成日）`、`Last Updated（最終更新日）`、`Owner（管理者）` の具体値は未決であり、本記録では推測・決定しない。

## Document ID Scheme

既にDocument IDを持つ次の現行配布文書は、追跡性を維持するため既存IDを変更しない。

- root `README.md`：`STD-PERSONA-INDEX-001`
- `personas/reference/CHATGPT_PERSONA.md`：`STD-PERSONA-CHATGPT-001`
- `personas/reference/CLAUDE_PERSONA.md`：`STD-PERSONA-CLAUDE-001`
- `personas/reference/CURSOR_PERSONA.md`：`STD-PERSONA-CURSOR-001`
- `personas/reference/GEMINI_PERSONA.md`：`STD-PERSONA-GEMINI-001`

未採番のEducation文書には、次のDocument IDを付与する。

- `personas/education/README.md`：`STD-PERSONA-EDU-INDEX-001`
- `personas/education/GEM_RESEARCHER_FULL.md`：`STD-PERSONA-EDU-RESEARCHER-FULL-001`
- `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`：`STD-PERSONA-EDU-RESEARCHER-LEARNING-DEVELOPMENT-001`
- `personas/education/GEM_RESEARCHER_DEVELOPMENT.md`：`STD-PERSONA-EDU-RESEARCHER-DEVELOPMENT-001`
- `personas/education/GEM_SOLUTION_PARTNER.md`：`STD-PERSONA-EDU-SOLUTION-PARTNER-001`
- `personas/education/GEM_CODE_GENERATOR.md`：`STD-PERSONA-EDU-CODE-GENERATOR-001`
- `personas/education/GEM_REVIEWER.md`：`STD-PERSONA-EDU-REVIEWER-001`

新設するReference索引には、次のDocument IDを付与する。

- `personas/reference/README.md`：`STD-PERSONA-REFERENCE-INDEX-001`

Document IDは文書の固定識別子として扱う。配置変更、版更新、Status変更だけを理由に変更しない。

## Header Value Facts and Rules

`Created Date（作成日）` は、既存文書ではGit履歴上の初回追加日を使用する。確認結果は次のとおりである。

- `README.md`：`2026-08-17`
- `personas/education/README.md`：`2026-08-19`
- `personas/education/GEM_RESEARCHER_FULL.md`：`2026-08-21`
- `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`：`2026-08-21`
- `personas/education/GEM_RESEARCHER_DEVELOPMENT.md`：`2026-08-21`
- `personas/education/GEM_SOLUTION_PARTNER.md`：`2026-08-19`
- `personas/education/GEM_CODE_GENERATOR.md`：`2026-08-20`
- `personas/education/GEM_REVIEWER.md`：`2026-08-19`
- `personas/reference/CHATGPT_PERSONA.md`：`2026-08-17`
- `personas/reference/CLAUDE_PERSONA.md`：`2026-08-17`
- `personas/reference/CURSOR_PERSONA.md`：`2026-08-17`
- `personas/reference/GEMINI_PERSONA.md`：`2026-08-17`
- 新設する `personas/reference/README.md`：実際の初回作成日

`Last Updated（最終更新日）` は、その文書を実際に更新した日をISO 8601形式で記載する。今回の文書適合性修正で変更する文書は `2026-08-22` とする。

`Owner（管理者）` は、既存ヘッダーとRepository所有者表記に合わせ、全現行配布文書で `t-oikawa-sendai` とする。

## Reference Index and Routing

`personas/reference/README.md` をReference領域の正式な入口・索引として配置する。このREADMEは、次の責務に限定する。

- Reference Personaの目的
- Education用4Gemとの違い
- Educationの現行手順としてそのまま流用しない注意
- 現在利用可能なReference文書への索引
- root `README.md` へ戻る導線
- 必要最小限の `personas/education/README.md` への案内

索引を現在の4文書専用として固定しない。Reference領域は将来7文書に追加資料を加えた構成へ増える可能性があるため、承認された文書が追加された時点で索引を更新できる構成にする。ただし、将来数を推測して未確定文書を先に作成しない。

root `README.md` はEducation領域とReference領域の入口を示す。Reference Personaは `Related Documents（関連文書）` から同一ディレクトリの `README.md` へ戻れるようにする。これにより、Reference領域内で適用境界と利用可能文書を確認できる導線を作る。

## Directory Structure Rules

Persona文書の保存構造は、次の共通規則で統一する。

- Repository全体の入口：root `README.md`
- 区分別の入口：`personas/<区分>/README.md`
- 区分別の現行Persona：`personas/<区分>/`
- 区分別の旧版：`personas/<区分>/archive/`
- 内部の判断・作業記録：`project-notes/`

現在のPersona区分は `education` と `reference` である。現行Personaを区分ディレクトリ直下、旧版を同じ区分の `archive/` に置くことで、現行と履歴を分離する。

Referenceには現在旧版が存在しないため、空の `personas/reference/archive/` は作成しない。最初のReference旧版が発生した時点で作成する。新設する `personas/reference/README.md` を除き、この決定だけを理由とする現行ファイルの移動は行わない。

この共通規則はPersona文書の保存構造に関する決定である。7文書を本Repositoryへ配置するか別管理にするか、および現在の別Repositoryとの不整合解消は、Persona作成完了後に扱う最重要検討事項として分離し、本決定で解決済みとしない。

## Related Documents Routing

`Related Documents（関連文書）` は、区分別READMEを索引として経由する次の階層規則で統一する。

- root `README.md`：`personas/education/README.md` と `personas/reference/README.md`
- `personas/education/README.md`：root `README.md` と現行Education Persona
- 各現行Education Persona：`personas/education/README.md`
- `personas/reference/README.md`：root `README.md`、`personas/education/README.md`、現行Reference文書
- 各現行Reference Persona：`personas/reference/README.md`

Persona同士をヘッダーから総当たりで相互リンクしない。区分内の文書追加・置換は区分別READMEの索引で管理し、個別Personaのヘッダー更新を必要最小限にする。

この規則の背景意図は、利用者がroot READMEから区分を選び、区分別READMEで適用境界と利用可能文書を確認してから個別Personaへ進める導線を維持しつつ、将来の文書増加に伴うリンク更新不整合を防ぐことである。

## Standard Header Status Values

標準ヘッダーの `Status（ステータス）` は、次の4状態で統一する。

- `Draft`
- `Review`
- `Approved`
- `Deprecated`

文書適合性の確認中は、新設するReference READMEを含む全13件の現行配布文書を `Version（バージョン）: 0.1`、`Status（ステータス）: Review` とする。

ヘッダー、表記、文書間導線、ディレクトリ構造の確認と必要な修正が完了しても、AIの判断だけで初回承認版へ変更しない。AIはUserへ、`Version 1.0（Status: Approved）へ変更してよいか` と明示的に確認する。Userが承認した場合に限り、`Version（バージョン）: 1.0`、`Status（ステータス）: Approved` へ変更する。

### Temporary Status Notation Exception

- 例外箇所：`personas/education/GEM_REVIEWER.md` に記載する最終設計ドキュメントの状態表記
- 維持する表記：`DRAFT`、`CURRENT`、`SUPERSEDED`
- 根拠：Reviewer再構築でUser確認済みの最終設計ドキュメントに関する機能仕様であり、標準ヘッダーの状態表記とは責務が異なる。
- 維持理由：標準ヘッダーへの表記統一だけを理由に変更すると、Reviewerの確定済み出力契約とEducation教材の説明を変更するため。
- 再検討・解除条件：最終設計ドキュメントの状態仕様を変更対象として別途検討し、Userが仕様変更を明示承認した場合に限り、標準ヘッダーとの表記統合を再検討する。

この例外は永久固定ではない。解除条件を満たす前にAIが自動変更しない。

この区分はヘッダー適用範囲、各ヘッダー項目、Document ID、Version・Status運用、作成日、最終更新日、管理者、Related Documents導線の確定である。

## Unresolved Details

次は未決であり、本記録では推測・決定しない。

- `ai-setup-materials` 向けの具体的な文書体系
- 既存文書へ必要な修正
- 7文書を本Repository内へ配置するか、別管理にするか
- 現在の別Repositoryとの不整合をどのように解消するか

## Background Intent

全プロジェクトの設計文書統治に共通する標準の目的を維持しつつ、性質の異なるRepositoryへアプリ用テンプレートを機械適用して、不要な文書や該当しない構成を増やすことを防ぐ。

文書数やアプリ固有の構成を適用しない場合も、SSOT、責務分離、追跡可能性、導線、履歴、変更統制、重複・不整合防止という統治目的は維持する。

文書の一貫性を高めつつ、外見上の統一のために確定済み仕様を壊すことを防ぐ。

配布文書の一貫性と追跡可能性を確保しつつ、内部記録への過剰適用とArchive本文の改変を防ぐ。
