# Education 4Gem and README Alignment Instructions

Last Updated: 2026-08-22
Status: READY FOR IMPLEMENTATION

## 1. Purpose

完成済みResearcher / Reviewerと、現行のSolution Partner / Code Generator、Education README、root READMEの名称、責務境界、User導線、配布ファイル導線を整合させる。

旧Education資産は、完成後に削除せずArchiveへ移動する既定方針に従う。

## 2. Authoritative Sources

1. `AGENTS.md`
2. `project-notes/CURRENT.md`
3. `project-notes/2026-08-21-researcher-completion.md`
4. `project-notes/2026-08-22-reviewer-user-first-learning-design.md`
5. `project-notes/2026-08-22-reviewer-completion.md`
6. `personas/education/GEM_REVIEWER.md`
7. `personas/education/GEM_CODE_GENERATOR.md`

## 3. Current 4Gem Names

```text
Researcher
Solution Partner
Code Generator
Reviewer
```

Education用4Gemに `Implementer` とCursorを含めない。

## 4. Files to Modify

- `personas/education/GEM_SOLUTION_PARTNER.md`
- `personas/education/GEM_CODE_GENERATOR.md`
- `personas/education/GEM_RESEARCHER_FULL.md`
- `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
- `personas/education/GEM_RESEARCHER_DEVELOPMENT.md`
- `personas/education/README.md`
- root `README.md`

## 5. Files to Move to Archive

次を削除せず、Git履歴を維持したまま移動する。

- `personas/education/GEM_IMPLEMENTER.md`
  - 移動先：`personas/education/archive/GEM_IMPLEMENTER.md`
- `personas/education/GEMINI_PERSONA_DEFINITION-4Gem.md`
  - 移動先：`personas/education/archive/GEMINI_PERSONA_DEFINITION-4Gem.md`

Archive版の冒頭に、次を明確に記載する。

- Status: `SUPERSEDED`
- 現行Education Personaとして使用しないこと
- `GEM_IMPLEMENTER.md` の置換先は `../GEM_CODE_GENERATOR.md` だが、責務を単純置換してはならないこと
- 旧一体型定義書の置換先は `../README.md` と現行の個別Persona群であること

Archive本文は履歴資料として保持し、現行仕様へ書き換えない。

## 6. User Terminology

- READMEでは `User（生徒）` と表記する。
- README以外のPersona本文では `User` と表記する。
- 現行Persona本文の役割主体として使われている `ユーザー`、`利用者`、`生徒` は、意味を変えず `User` へ統一する。
- Archive本文は履歴資料のため、この用語統一対象にしない。

## 7. Solution Partner Alignment

`GEM_SOLUTION_PARTNER.md` では次を反映する。

- すべての現行役割表記を `User` に統一する。
- `Implementer` への引き渡しを `Code Generator` へのコード生成用引き渡しへ変更する。
- Code Generatorが迷わずコードを生成できる粒度まで、設計・指示を具体化する。
- Code Generatorが実環境への適用、IDE操作、実行、test結果確認、動作確認、Evidence作成を担当するように書かない。
- Reviewerの設計指摘について、Userが理解不能、追加説明の必要、または方針判断不能を明示した場合に、Userとの打ち合わせ・検討を支援する。
- ReviewerからSolution Partnerへ作業が直接送られる設計にしない。
- コードだけで解決できる指摘をSolution PartnerからCode Generatorへ直接送らない。レビューの受領者と修正方法の判断者はUserである。
- Userが選択した場合、設計と実装の差分整理、実装中に生じた判断の整理、最終設計ドキュメント更新、整合確認を支援する。
- 最終設計ドキュメントと成果物の採用・完成判断はUserが行う。

現行の要求整理、設計、比較、Evidence、非迎合、過剰設計防止の中核責務は維持する。

## 8. Code Generator Alignment

`GEM_CODE_GENERATOR.md` では次を反映する。

- Role名は `Code Generator` のまま維持する。
- Userが利用するコード生成・解析・修正支援Personaであることを明記する。
- testコード生成を支援可能な責務として明記する。
- Userから渡された現行設計、仕様、対象、変更禁止範囲に従う。
- Userが自力修正ではなくCode Generator利用を選択した場合、Reviewerの修正指示を入力として扱えるようにする。
- 実環境への適用、IDE操作、Git操作、コード実行、test実行、結果確認、動作確認、検証Evidence作成、品質保証判定を担当しない。
- 生成したコードまたはtestコードを、適用済み、実行済み、成功済みとして扱わない。
- 出力はUserがIDEへ反映し、実行、test、動作確認、Evidence作成を行える形にする。
- 事実、仮定、未確認事項を分離する。

要求定義、システムアーキテクチャ決定、技術選定の最終判断を担当しない既存境界は維持する。

## 9. Researcher Terminology Alignment

現行Researcher 3ファイルでは、Persona本文中の役割主体 `ユーザー` を `User` へ統一する。

次を変更してはならない。

- Researcher本体の責務
- Active Modules
- Module構成
- Module検索範囲
- 3ファイルの配布方式

変更後も次を確認する。

- 3ファイルのResearcher本体が完全に同一である。
- 同名Module本文がファイル間で同一である。
- 各ファイルのActive Modulesだけが構成に応じて異なる。

## 10. Education README Alignment

`personas/education/README.md` は現行配布導線として再構築する。

必須内容：

- 役割名を `User（生徒）` とする。
- User（生徒）が4Gemを操作し、各出力を確認し、必要な情報を手動で渡すことを明記する。
- 現行4Gemの名称と責務を記載する。
- Researcherの配布ファイルを次の3本として案内する。
  - `GEM_RESEARCHER_FULL.md`
  - `GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
  - `GEM_RESEARCHER_DEVELOPMENT.md`
- GemにはResearcher完成版を1本だけ登録し、必要に応じて入れ替えることを明記する。
- Code Generatorはコード・testコード生成までを支援する。
- User（生徒）がIDE反映、実行、test、動作確認、Evidence作成を行う。
- Reviewerは設計、コード、User（生徒）のEvidenceを評価し、結果を最初にUser（生徒）へ返す。
- Reviewerの判定が `PASS / PASS WITH NOTES / REWORK REQUIRED / BLOCKED` の4段階であることだけを簡潔に記載する。
- 最終判断はUser（生徒）が行う。
- READMEへ4判定の詳細定義を記載しない。
- `Implementer`、旧Researcher単一ファイル、旧一体型定義書を現行導線として案内しない。
- Evidence、正本、責務分離、User-firstの基本フローを初心者が理解できる日本語で説明する。

Reviewerの詳細出力仕様は `GEM_REVIEWER.md` を参照させ、READMEへ重複させない。

## 11. Root README Alignment

root `README.md` はRepository全体の入口として更新する。

必須内容：

- `personas/education/README.md` をEducation用の主要導線とする。
- 現行4Gem名を簡潔に記載する。
- Researcherが3完成版方式であることを簡潔に案内する。
- `User（生徒）` がCode Generatorの生成コードをIDEへ反映・検証し、最終判断することを簡潔に記載する。
- Reviewerの4判定の詳細は記載しない。
- `GEMINI_PERSONA_DEFINITION-4Gem.md` を現行主要導線として案内しない。
- `Implementer` をEducation用4Gemとして記載しない。
- `personas/reference/` はEducation用4Gemとは前提が異なる参考資料であることを維持する。
- 秘密情報、AIの未検証完了報告に関する既存注意事項を維持する。

root READMEをPersona詳細仕様の重複先にしない。

## 12. Out of Scope

- `personas/education/GEM_REVIEWER.md` の再変更
- Reviewer設計の再検討
- Researcher Module設計の変更
- `ASKME 迎合禁止` の検討
- 7文書の配置・管理方法の決定
- `personas/reference/` の変更
- project-notes内の旧決定記録の改変

## 13. Required Verification

### 13.1 Active Education files

Archiveを除く `personas/education/` とroot READMEで次を確認する。

- Education用4Gemとして `Implementer` が残っていない。
- `GEM_IMPLEMENTER.md` への現行導線がない。
- `GEMINI_PERSONA_DEFINITION-4Gem.md` への現行導線がない。
- 旧 `GEM_RESEARCHER.md` への現行導線がない。
- 現行4Gem名が一致している。
- User責務、Code Generator境界、Reviewer入力・返却先が一致している。

### 13.2 Archive

- 旧2ファイルが `personas/education/archive/` に存在する。
- 旧パスから削除されている。
- Archive冒頭に `SUPERSEDED` と置換先がある。
- Archive本文を現行仕様として書き換えていない。

### 13.3 Researcher invariants

- 3ファイルのResearcher本体が同一である。
- 同名Module本文が一致する。
- Active Modulesが各構成どおりである。

### 13.4 Repository

- 対象外ファイルを変更していない。
- `git diff --check` が成功する。
- 現行導線のリンク先が実在する。
- 旧決定を現行仕様として復活させていない。

## 14. Completion Report

実装担当は次を報告する。

- 変更・移動ファイル
- Archive移動結果
- Solution PartnerとCode Generatorの責務境界修正
- Researcher不変条件の検証
- README導線の更新
- 禁止語・旧リンク確認
- `git diff --check` 結果
- 未解決事項または実装不能事項

資料だけで一意に決まらない新しい事項が見つかった場合は推測せず停止する。
