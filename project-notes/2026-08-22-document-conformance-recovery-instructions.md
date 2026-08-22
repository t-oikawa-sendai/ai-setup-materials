# Document Conformance Recovery Instructions

Last Updated: 2026-08-22
Status: APPROVED IMPLEMENTATION INSTRUCTIONS

## Purpose

確定済みの設計文書標準適用境界に従い、現行配布文書のヘッダー、`English（日本語）` 表記、文書間導線、Reference索引、Archive Noticeを復旧する。

Personaの機能設計、責務、固定出力契約、旧本文を変更しない。

## Authoritative Sources

次の順で正本として扱う。

1. `project-notes/CURRENT.md`
2. `project-notes/2026-08-22-design-document-standard-application-scope.md`
3. 本指示書

競合または一意に判断できない箇所を確認した場合は、推測して修正せず停止する。

## Exact Change Scope

変更対象は次の16文書に限定する。

### Current Distribution Documents

1. `README.md`
2. `personas/education/README.md`
3. `personas/education/GEM_RESEARCHER_FULL.md`
4. `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
5. `personas/education/GEM_RESEARCHER_DEVELOPMENT.md`
6. `personas/education/GEM_SOLUTION_PARTNER.md`
7. `personas/education/GEM_CODE_GENERATOR.md`
8. `personas/education/GEM_REVIEWER.md`
9. `personas/reference/README.md`（新規）
10. `personas/reference/CHATGPT_PERSONA.md`
11. `personas/reference/CLAUDE_PERSONA.md`
12. `personas/reference/CURSOR_PERSONA.md`
13. `personas/reference/GEMINI_PERSONA.md`

### Archive Notices

14. `personas/education/archive/GEM_RESEARCHER.md`
15. `personas/education/archive/GEM_IMPLEMENTER.md`
16. `personas/education/archive/GEMINI_PERSONA_DEFINITION-4Gem.md`

他のファイルを変更しない。実装担当はcommit・pushを行わない。

## Standard Header

13件の現行配布文書の先頭へ、次の形式で標準ヘッダーを配置する。

```markdown
<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | ... |
| Version（バージョン） | 0.1 |
| Status（ステータス） | Review |
| Created Date（作成日） | YYYY-MM-DD |
| Last Updated（最終更新日） | 2026-08-22 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | ... |

---
```

既存のroot READMEとReference PersonaのDocument ID・Created Dateは変更しない。Statusは `Review`、Last Updatedは `2026-08-22`、Related Documentsは本指示書の規則へ更新する。

## Document ID and Created Date Matrix

| File（ファイル） | Document ID（文書ID） | Created Date（作成日） |
|---|---|---|
| `README.md` | `STD-PERSONA-INDEX-001` | `2026-08-17` |
| `personas/education/README.md` | `STD-PERSONA-EDU-INDEX-001` | `2026-08-19` |
| `personas/education/GEM_RESEARCHER_FULL.md` | `STD-PERSONA-EDU-RESEARCHER-FULL-001` | `2026-08-21` |
| `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md` | `STD-PERSONA-EDU-RESEARCHER-LEARNING-DEVELOPMENT-001` | `2026-08-21` |
| `personas/education/GEM_RESEARCHER_DEVELOPMENT.md` | `STD-PERSONA-EDU-RESEARCHER-DEVELOPMENT-001` | `2026-08-21` |
| `personas/education/GEM_SOLUTION_PARTNER.md` | `STD-PERSONA-EDU-SOLUTION-PARTNER-001` | `2026-08-19` |
| `personas/education/GEM_CODE_GENERATOR.md` | `STD-PERSONA-EDU-CODE-GENERATOR-001` | `2026-08-20` |
| `personas/education/GEM_REVIEWER.md` | `STD-PERSONA-EDU-REVIEWER-001` | `2026-08-19` |
| `personas/reference/README.md` | `STD-PERSONA-REFERENCE-INDEX-001` | `2026-08-22` |
| `personas/reference/CHATGPT_PERSONA.md` | `STD-PERSONA-CHATGPT-001` | `2026-08-17` |
| `personas/reference/CLAUDE_PERSONA.md` | `STD-PERSONA-CLAUDE-001` | `2026-08-17` |
| `personas/reference/CURSOR_PERSONA.md` | `STD-PERSONA-CURSOR-001` | `2026-08-17` |
| `personas/reference/GEMINI_PERSONA.md` | `STD-PERSONA-GEMINI-001` | `2026-08-17` |

## Related Documents

次の階層導線を適用する。

- root `README.md`：Education READMEとReference README
- Education README：root READMEと現行Education Persona 6文書
- 各Education Persona：Education READMEだけ
- Reference README：root README、Education README、現行Reference Persona 4文書
- 各Reference Persona：Reference READMEだけ

リンクは各ファイルから解決できる正しい相対パスとする。複数リンクはMarkdown表の同一セル内で `<br>` により分ける。Persona同士をヘッダーから総当たりリンクしない。

## Reference README

`personas/reference/README.md` を新規作成する。タイトルは `# Reference Personas（参考用Persona）` とする。

本文の責務は次に限定する。

1. `Purpose（目的）`
2. `Difference from Education 4Gem（Education用4Gemとの違い）`
3. `Current Reference Personas（現行Reference Persona）`
4. `Usage Notes（利用上の注意）`
5. `Navigation（導線）`

現行Reference Persona 4文書へのリンクを掲載する。ただし「4文書で固定」と記載しない。将来7文書に追加資料を加えた構成へ増える可能性を受け入れる索引とするが、未確定文書名や役割を推測して追加しない。

Education用4Gemとは役割、利用サービス、実装・検証方法の前提が異なること、Educationの現行手順としてそのまま流用しないことを明示する。新しいPersona機能仕様は追加しない。

root READMEの構成説明にReference READMEへのリンクを追加する。

## English-Japanese Notation

文書タイトル、通常の章・節見出し、文書管理項目、通常の表の列名を `English（日本語）` へ統一する。

- 日本語のみの見出し：既存日本語を一字も変えず、前に意味の等しい英語を追加する。
- 英語のみの見出し：既存英語を一字も変えず、後ろに意味の等しい日本語を追加する。
- 番号付き見出し：番号を維持し、番号の後を `English（日本語）` とする。
- 既に `English（日本語）` の見出し：変更しない。
- 通常本文：英語併記しない。
- fenced code / fenced Markdown内：変更しない。

文書タイトルは次の表記を使用する。

- root：`AI Setup Materials — Persona and Configuration Repository（Persona・設定資料リポジトリ）`
- Education README：`Education Personas（教育用Persona）`
- Researcher 3文書：`Researcher Persona（Researcherペルソナ）`
- Solution Partner：`Solution Partner Persona（Solution Partnerペルソナ）`
- Code Generator：`Code Generator Persona（Code Generatorペルソナ）`
- Reviewer：`Reviewer Persona（Reviewerペルソナ）`
- Reference README：`Reference Personas（参考用Persona）`
- ChatGPT：`ChatGPT Responsibility Definition（ChatGPT向け責務定義）`
- Claude：`Claude Persona（Claudeペルソナ）`
- Cursor：`Cursor Persona（Cursorペルソナ）`
- Gemini：`Gemini Persona（Geminiペルソナ）`

Education READMEの通常表の列名は、次へ変更する。

- `Gem Display Name（Gem表示名）`
- `Persona File（Personaファイル）`
- `Primary Responsibility（主な責務）`

## Temporary Notation Exceptions

次は固定出力・引き渡し契約であるため変更しない。

- Researcher 3文書：`Active Modules`、引き渡し項目名、出力項目名
- Code Generator：`Code Generation Report` と配下の固定出力項目名
- Solution Partner：コード生成用引き渡し項目名、固定出力項目名
- Reviewer：`総合判定`、`対応方針一覧`、`修正案一覧表`、各指摘の必須項目、`User向け説明`、`Code Generatorへの修正指示`、`Solution Partnerとの打ち合わせ用情報`、`Userが判断する事項`、`最終設計ドキュメント更新情報`、判定値、最終設計ドキュメント状態値、固定案内文
- Claude：`本格レビュー` の fenced Markdownテンプレート
- Cursor：fenced codeのコードヘッダー、`Report` の fenced Markdownテンプレート
- Gemini：`比較・技術選定調査` の fenced Markdownテンプレート

Reviewerの `## 7. 総合判定`、`### 8.1 対応方針一覧`、`### 8.2 各指摘の必須項目`、`### 9.1 User向け説明`、`### 9.2 Code Generatorへの修正指示`、`## 14. PASS後の最終設計ドキュメント更新情報` は、正式名称を含む見出しとして現状維持する。判定値だけの小見出しも変更しない。

その他の通常見出しは、既存の意味を変えない範囲で英語を先頭へ追加する。翻訳に複数の意味があり一意に判断できない場合は、その見出しを変更せず報告する。

## Archive Notice

3件のArchive文書の先頭を、次のNoticeへ統一する。

```markdown
# Archive Notice（アーカイブ通知）

> **Do Not Use（利用禁止）**
>
> この文書は履歴資料です。現行仕様、現行Persona、現行運用の根拠として使用しないでください。

| Item（項目） | Value（値） |
|---|---|
| Archive Type（アーカイブ種別） | Historical Material（履歴資料） |
| Status（ステータス） | Deprecated |
| Usage（利用可否） | Do Not Use（利用禁止） |
| Replaced By（置換先） | ... |
| Preservation（保存方針） | Original Body Preserved（旧本文を変更せず保存） |

---
```

置換先は次のとおりとする。

- `GEM_RESEARCHER.md`：現行Researcher 3完成版
- `GEM_IMPLEMENTER.md`：`../GEM_CODE_GENERATOR.md`
- `GEMINI_PERSONA_DEFINITION-4Gem.md`：`../README.md` と現行Education Persona 6文書

既存Noticeは置換してよい。区切り線より下の旧本文・旧ヘッダーは一字も変更しない。Noticeがない `GEM_RESEARCHER.md` は、元の全内容を旧本文としてNoticeと区切り線の後ろへそのまま残す。

## Prohibited Changes

- Personaの責務、機能、出力順、判定、状態、固定文言を変更しない。
- 本文を要約、整理、追記、削除しない。
- fenced code / fenced Markdown内を変更しない。
- Archiveの旧本文・旧ヘッダーを変更しない。
- ファイルを移動・改名しない。
- 空の `personas/reference/archive/` を作成しない。
- 7文書または将来のReference文書を推測して作成しない。
- `project-notes/` を実装対象に含めない。

## Verification

実装後に次をすべて確認する。

1. 変更対象が指定16文書だけである。
2. 現行配布文書13件すべてに、7項目の標準ヘッダーが1つだけ存在する。
3. 13件すべてが `Version: 0.1`、`Status: Review`、`Owner: t-oikawa-sendai` である。
4. Document IDが全件一意で、指定値と一致する。
5. Created Dateが指定値と一致し、Last Updatedが `2026-08-22` である。
6. 全相対リンクのリンク先が存在する。
7. Reference READMEが、現在の4文書だけに固定しない索引として成立する。
8. 通常の文書タイトル・章節見出し・表列名が `English（日本語）` である。
9. 一時例外の固定出力項目・fenced内容が変更されていない。
10. Archive 3件に利用禁止が二重表示され、`Status: Deprecated`、`Usage: Do Not Use`、置換先、保存方針がある。
11. Archiveの旧本文・旧ヘッダーが変更前とbyte単位で一致する。
12. `git diff --check` が成功する。

一つでも確認不能または不一致がある場合は完了と報告せず、対象・Evidence・未確認理由を明示する。
