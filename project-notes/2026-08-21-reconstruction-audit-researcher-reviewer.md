# Reconstruction Audit: Researcher / Reviewer

Last Updated: 2026-08-21
Status: RECOVERY / VERIFIED-HISTORY

## Purpose

Education用4Gemの情報資産再構築にあたり、Researcher / ReviewerについてGitHub上で確認できた現物・commit履歴を記録する。

この文書は「最新仕様の確定記録」ではない。

ここにはGitHubで確認できた履歴事実だけを記載し、ユーザーが再確認した最新事項は `2026-08-21-reconstruction-confirmed-facts.md` と分離する。

---

## Researcher

### VERIFIED

- `personas/education/GEM_RESEARCHER.md` は commit `653db32aa879733fcb86e62228be674c01a82808`（2026-08-19）で追加された。
- 当時のResearcherは、外部情報調査、一次情報優先、確認済み事実と未確認情報の分離、Evidence表示、Solution Partnerへの引き渡しを主責務としていた。
- 当時の本文にはModule構想は含まれていない。
- Repository内のコード検索およびcommit検索で `Module` を確認したが、2026-08-21の監査時点では該当記録を検出できなかった。

### IMPORTANT

ユーザーが2026-08-21に明示した最新事項では、Researcher Personaは未完成であり、Moduleを導入してサーチ範囲の責務を変更できる機能を追加する前提で設計途中である。

したがって、2026-08-19版 `GEM_RESEARCHER.md` を最新完成仕様として扱わない。

Module構想の具体仕様は、GitHub上で確認できない限り推論で補完しない。

---

## Code Generator transition

### VERIFIED

- `personas/education/GEM_CODE_GENERATOR.md` は commit `85d024538830bea9cbd61a710148068786c3b4cd`（2026-08-20）で追加された。
- Code Generatorは、設計内容に基づくコード生成、既存コード解析、エラー原因分析、修正版コード生成等を担当する。
- 実環境への適用、IDE操作、Git操作、品質保証判定は担当しないと記載されている。

### IMPORTANT

この追加は、2026-08-19に作成されたEducation用 `GEM_IMPLEMENTER.md` より後の履歴である。

旧Implementerの責務をCode Generatorへ機械的に移植・置換してはならない。

---

## Reviewer

### VERIFIED

- `personas/education/GEM_REVIEWER.md` は commit `6e673d557a813ca34b16e44be0735772e47ed617`（2026-08-19）で追加された。
- 当時のReviewerは、要求・設計整合性、品質、保守性、セキュリティ、Evidence、修正先判定等を扱っていた。
- 当時の本文には、修正先として `Implementer` または `Solution Partner` が記載されている。
- リファクタリング実施担当も `Implementer` と記載されている。

### IMPORTANT

ユーザーが2026-08-21に明示した最新事項ではReviewer Personaは未完成である。

また、現行Education 4Gemでは `Implementer` ではなく `Code Generator` が採用されているため、2026-08-19版Reviewerの戻し先・責務連携をそのまま現行仕様として扱わない。

Code Generator化後のReviewerの戻し先・連携ルールは再構築対象とする。

---

## Current / Superseded / Unresolved classification

### CURRENT / USER-CONFIRMED

- Researcher Personaは未完成。
- Reviewer Personaは未完成。
- ResearcherはModule導入によってサーチ範囲の責務を変更できる機能を追加する前提で設計途中。
- Education 4Gemのコード生成担当はCode Generatorであり、Implementerではない。

### VERIFIED-HISTORY / NOT SAFE AS CURRENT

- 2026-08-19版Researcher Persona本文。
- 2026-08-19版Reviewer Persona本文。
- ReviewerからImplementerへ戻す旧記載。
- ImplementerをEducation 4Gemのコード実装担当として扱う旧記載。

### UNRESOLVED

- Researcher Moduleの具体的な構成。
- Moduleの命名。
- Moduleの選択・切替方法。
- Moduleごとのサーチ範囲。
- Researcher本体とModuleの責務境界。
- Reviewer Personaの最新完成要件。
- Code Generator化後のReviewerの戻し先・連携ルール。

上記UNRESOLVEDは、追加資料・履歴で一意に確認できない限り、AIが推論で確定しない。
