# Education 4Gem and README Alignment Completion

Last Updated: 2026-08-22
Status: COMPLETE / VERIFIED

## Purpose

Education用4GemのPersona本文、Education README、root READMEについて、現行名称、責務境界、User導線、配布ファイル導線の整合化が完了したことと、その検証Evidenceを記録する。

## Implemented Scope

次を現行仕様へ整合させた。

- `personas/education/GEM_SOLUTION_PARTNER.md`
- `personas/education/GEM_CODE_GENERATOR.md`
- `personas/education/GEM_RESEARCHER_FULL.md`
- `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
- `personas/education/GEM_RESEARCHER_DEVELOPMENT.md`
- `personas/education/README.md`
- root `README.md`

`personas/education/GEM_REVIEWER.md` は完成済みであり、本整合工程では変更・再検討していない。

## Archive Migration

次の旧ファイルを削除せず、履歴を維持したままArchiveへ移動した。

- `personas/education/GEM_IMPLEMENTER.md`
  - 移動先：`personas/education/archive/GEM_IMPLEMENTER.md`
- `personas/education/GEMINI_PERSONA_DEFINITION-4Gem.md`
  - 移動先：`personas/education/archive/GEMINI_PERSONA_DEFINITION-4Gem.md`

各Archive版の冒頭へ、次を追加した。

- Status: `SUPERSEDED`
- 現行Education Personaまたは現行運用導線として使用しないこと
- 現行の置換先
- 旧Implementerの責務をCode Generatorへ単純置換してはならないこと

Archive本文は現行仕様へ書き換えていない。各Archive本文を移動前のHEAD版と比較し、冒頭のArchive表示を除く旧本文が一致することを確認した。

一時indexを使用したGitのrename検出結果は次のとおりである。実Repositoryのstagingは変更していない。

- 旧一体型定義書：rename 94%
- 旧Implementer：rename 82%

## Current 4Gem and Responsibility Boundaries

現行4Gem名を次へ統一した。

```text
Researcher
Solution Partner
Code Generator
Reviewer
```

- Persona本文の役割主体は `User`、READMEでは `User（生徒）` とした。
- Solution Partnerは、要求・制約・設計を整理し、Code Generatorが迷わずコード生成できる粒度の指示を作成する。
- Code Generatorは、コード・testコードの生成、解析、修正支援までを担当する。
- Code Generatorは、IDE操作、実環境への適用、Git操作、コード・testの実行、結果確認、動作確認、検証Evidence作成、品質保証判定を担当しない。
- UserがコードをIDEへ反映し、実行、test、動作確認、Evidence作成、再提出、最終判断を行う。
- Reviewerは、Solution Partnerの設計成果物、Code Generatorが生成したコード、Userが作成した検証Evidenceを評価し、結果を最初にUserへ返す。
- Reviewerから別のGemへ作業を直接送らず、Userが自力修正または利用する支援先を選択する。
- Userが選択した場合、Solution Partnerは設計と実装の差分整理、実装中の判断整理、最終設計ドキュメント更新、整合確認を支援する。
- 最終採用・完成判断はUserが行う。

## README Alignment

`personas/education/README.md` をEducation用の主要導線として再構築した。

- 現行4Gemの名称と責務を記載した。
- User（生徒）が各Gemを操作し、必要な情報を手動で渡すUser-firstフローを記載した。
- Researcherの3完成版を案内し、Gemへ登録するのは1本だけであることを記載した。
- Code GeneratorとUser（生徒）のコード生成・適用・検証境界を記載した。
- Reviewerの4判定名だけを簡潔に記載し、詳細仕様は `GEM_REVIEWER.md` へリンクした。
- Evidence、正本、責務分離を初心者向けの日本語で説明した。

root `README.md` をRepository全体の入口として整合させた。

- `personas/education/README.md` をEducation用の主要導線とした。
- 現行4Gem名とResearcherの3完成版方式を簡潔に記載した。
- User（生徒）がIDE反映、検証、最終判断を行うことを記載した。
- `personas/reference/` はEducation用4Gemとは前提が異なる参考資料であることを維持した。
- 秘密情報とAIの未検証完了報告に関する既存注意事項を維持した。
- Persona詳細仕様やReviewerの4判定詳細は重複記載していない。

## Researcher Invariants

Researcher 3完成版では、役割主体の用語を `User` へ統一した。責務、Active Modules、Module構成、検索範囲、3ファイルの配布方式は変更していない。

検証結果：

- 3ファイルのResearcher本体 `1. 役割` から `9. Module運用ルール`：完全一致
- Full版とLearning + Development版のLearning Module本文：一致
- 3ファイルのDevelopment Module本文：完全一致
- Active Modules：各完成版の構成どおり

## Verification Evidence

### Current paths and links

- Archiveを除く `personas/education/` とroot READMEに、Education用4Gemとしての `Implementer` は存在しない。
- 現行READMEに `GEM_IMPLEMENTER.md` への導線は存在しない。
- 現行READMEに `GEMINI_PERSONA_DEFINITION-4Gem.md` への導線は存在しない。
- 現行READMEに旧 `GEM_RESEARCHER.md` への導線は存在しない。
- READMEとArchive冒頭に追加した現行リンクのリンク先はすべて実在する。
- 旧2ファイルは旧パスに存在せず、`personas/education/archive/` に存在する。

### Repository checks

- `git diff --check`: PASS
- 対象外の現行Persona、`personas/reference/`、旧決定記録は変更していない。
- 実Repositoryのstaging、commit、pushは実施していない。

## Unresolved Items

本整合工程に未解決事項または実装不能事項はない。

Persona作成・導線整合後の次の最重要検討事項は別工程として扱い、本工程では内容を検討していない。

1. `ASKME 迎合禁止` の利用
2. 7文書を配置するか別管理にするか、および現行の別Repositoryとの不整合
