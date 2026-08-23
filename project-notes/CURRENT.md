# CURRENT

Last Updated: 2026-08-23
Status: CURRENT

## PURPOSE

生徒へ配布可能な `ai-setup-materials` を完成させる。責務範囲と作業規則は `AGENTS.md` および `README.md` を正本とする。

## 完了事項

- Education用4Gem Persona本体の機能設計
- 文書適合性復旧、現行配布文書13件の `Version 1.0 / Status Approved` 昇格
- Repository責務の確定（Persona + Persona利用に直接必要な設定・運用資料。7文書は別Repository。`ASKME 迎合禁止` は独立事項としない）
- Persona本文と設定・運用資料の責務分離、AIサービス単位管理、Education Geminiは共通1資料
- 文書管理ルールの変更（成果物MDを正本とし、`Decision & Rationale` を同ファイルへ記録。`CURRENT.md` は現在地点のみ）
- Education用Gemini設定資料の対象、ファイル名、基本構成を確定
  - 対象：Education用Gemini Gem
  - ファイル：`personas/education/setup/GEMINI_GEM_SETUP.md`
  - 4Gem共通1資料
  - 利用方法・Workflow説明は設定資料へ含めない

## 作業中

- `personas/education/setup/GEMINI_GEM_SETUP.md`
  - Version：0.1
  - Status：Review
  - 確定済み方針と2026-08-23時点のGoogle公式Gemini Apps Helpを基に初版を作成済み
  - Gem作成、PersonaのInstructions設定、Knowledge設定、更新・変更方法、注意事項を記載
  - `Decision & Rationale` に管理単位と責務範囲の判断理由を記録済み

## 次工程

1. `GEMINI_GEM_SETUP.md` の内容をUserが確認する。
2. 修正判断が発生した場合は、対象成果物である `GEMINI_GEM_SETUP.md` へ即時反映し、記録基準に該当する場合は同ファイルの `Decision & Rationale` へ追記する。
3. User承認後、文書状態を完成版へ昇格する。
4. 完成版昇格後、`personas/education/README.md` から設定資料への導線を追加する。

Reviewerを含むPersonaの機能設計はEvidenceなしに再検討しない。完了済みの文書適合性復旧を、Evidenceなしに再作業対象へ戻さない。`ASKME 迎合禁止` と7文書配置を未決事項へ戻さない。

## 正本の所在

- 作業規則：`AGENTS.md`
- Repository入口：`README.md`
- Education Persona：`personas/education/`
- Education入口：`personas/education/README.md`
- Education Gemini設定資料：`personas/education/setup/GEMINI_GEM_SETUP.md`
- Reference Persona：`personas/reference/`
- Reference入口：`personas/reference/README.md`
- 現行仕様の判断理由：各成果物MDの `Decision & Rationale`
- 2026-08-23より前の判断経緯・復旧・監査Evidence：`project-notes/YYYY-MM-DD-*.md`（履歴。現行仕様の代替正本ではない）

## 現行として使用しない文書

次の文書には旧決定・失効情報が含まれるため、単独で現行の完成仕様として扱わない。

- `project-notes/2026-08-21-education-4gem-design-decisions.md`
- `project-notes/2026-08-19-4gem-names.md`
- `project-notes/2026-08-22-reviewer-reconstruction-instructions.md`

`personas/education/archive/` 配下は `Deprecated` の履歴資料であり、現行Education Personaまたは現行運用導線として使用しない。

## 再開時の読み順

1. 本ファイル（現在地点）
2. `AGENTS.md`（作業規則）
3. 対象成果物MDの本文（現行仕様）
4. 対象成果物MDの `Decision & Rationale`（判断理由）
5. 必要時のみ `project-notes/YYYY-MM-DD-*.md`（2026-08-23より前の履歴）

## REFERENCES

- `AGENTS.md`
- `personas/education/setup/GEMINI_GEM_SETUP.md`
- `project-notes/2026-08-21-ai-information-asset-safety.md`
- `project-notes/2026-08-22-persona-and-setup-scope.md`
- `project-notes/2026-08-22-design-document-standard-application-scope.md`
- `project-notes/2026-08-22-document-conformance-recovery-completion.md`
- `project-notes/2026-08-22-reviewer-user-first-learning-design.md`
- `project-notes/2026-08-21-researcher-completion.md`
- `project-notes/2026-08-22-reviewer-completion.md`
- `personas/education/README.md`
- `personas/reference/README.md`
- `README.md`
