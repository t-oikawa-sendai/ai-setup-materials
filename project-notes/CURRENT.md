# CURRENT

Last Updated: 2026-08-27
Status: CURRENT

## PURPOSE

生徒へ配布可能な `ai-setup-materials` を完成させる。責務範囲と作業規則は `AGENTS.md` および `README.md` を正本とする。

## 完了事項

- Education用4Gem Persona本体の機能設計
- 文書適合性復旧、当時の現行配布文書13件の `Version 1.0 / Status Approved` 昇格
- Repository責務の確定（Persona + Persona利用に直接必要な設定・運用資料。7文書は別Repository。`ASKME 迎合禁止` は独立事項としない）
- Persona本文と設定・運用資料の責務分離、AIサービス単位管理、Education Geminiは共通1資料
- 文書管理ルールの変更（成果物MDを正本とし、`Decision & Rationale` を同ファイルへ記録。`CURRENT.md` は現在地点のみ）
- Education用Gemini設定資料 `personas/education/setup/GEMINI_GEM_SETUP.md` 完成
  - Version：1.0
  - Status：Approved
  - Education用の基本体系は4Gem
  - Gemini上では `Researcher Deep Research` を追加した **4Gem＋1** として運用
  - `Researcher Deep Research` は独立PersonaではなくResearcher Personaを使う追加Gem
  - Gemini上の実体は5 Gem
  - 初期作成時の最低限必須項目：`名前`、`説明`、`カスタム指示`
  - `説明` は教材標準値を固定して使用
  - `Researcher Deep Research` の `デフォルト ツール` は Deep Research
  - 通常用Researcher / Solution Partner / Code Generator / Reviewerの `デフォルト ツール` は初期状態では設定しない
  - `知識` は必要になった時点でファイルを追加する任意設定
  - Contextと `知識` の関係を説明。Context Windowは本設定資料の対象外
  - AIサービス使用量の共通用語は `利用量（Usage）`
  - PersonaとGem実体の関係を示す `4 Persona / 5 Gem` 構成図を掲載
- `personas/education/README.md` を4Gem＋1へ整合し、Gemini設定資料への導線を追加
- 2026-08-26 Persona重要性の共通説明とGemini設定手順の責務を分離
  - ルート `README.md` の前半へ、サービス全体のカスタム指示・共通設定 / Persona / その都度のプロンプトの比較表を配置
  - 比較から「PersonaはAIの役割・責務・責務境界・判断基準・出力を継続的に定義するため重要」という導線を追加
  - Persona重要性の共通説明はEducationだけでなくReferenceにも適用するRepository共通の設計思想としてRootを正本化
  - 比較表の星は各AIサービスの内部優先順位ではなく教材上の影響度目安であることを明記
  - `personas/education/README.md` から共通比較表の重複を削除し、Root READMEへの導線に変更
  - 比較表はルート `README.md` の1か所だけに配置し、Education READMEとGemini設定資料にはRootへの導線だけを保持
  - `personas/education/setup/GEMINI_GEM_SETUP.md` はSetupマニュアルとして設定・操作手順へ限定
  - パーソナル インテリジェンスのカスタム指示は、パソコンでの設定手順だけをGemini設定資料の第2章に保持
  - Gem用Context説明の `カスタム指示` を `Gemのカスタム指示（Persona本体）` と明確化
- ルート `README.md` を4Gem＋1へ整合し、Gemini設定資料への導線を追加
- Repository配布前最終整合監査を完了
  - 2026-08-26時点の現行配布文書14件を確認し、14/14が `Version 1.0 / Status Approved`
  - Root / Education / Setup / Referenceの現行導線と実ファイルを照合し、内部リンク先の欠落なし
  - Education Persona名を Researcher / Solution Partner / Code Generator / Reviewer で確認
  - Geminiの現行構成を `4Gem＋1` としてRoot / Education / Setup / Referenceの対比表現まで整合
  - Root READMEとReference READMEに残っていた旧 `Education用4Gem` 対比表現を `Education用4Gem＋1` へ修正
  - 現行Education導線・設定資料に旧 `GEM_IMPLEMENTER`、旧 `Instructions（指示）`、`DeepSearch` 誤表記の残存なし
  - Gemini公式HelpでGem作成、`知識` による追加Context、Deep Research、利用上限の現行案内を再確認
- 2026-08-27 Reference Claude Personaを更新
  - `personas/reference/CLAUDE_PERSONA.md` を Version 1.3 / Status Approved へ更新
  - ソフトウェアレビューに加え、正本文書レビューとAI制御資産レビューを責務へ追加
  - AI制御資産のインベントリ先行、資産間評価、強制力・ロード条件・適用範囲の評価を追加
  - 責務変更の判断理由を同Personaの `Decision & Rationale` に記録
- 2026-08-27 Reference Claude Persona v1.3の生徒PFレビュー適合性分析を完了
  - 分析Evidence：`project-notes/2026-08-27-portfolio-reviewer-fit-analysis.md`
  - Reference版は実務監査向けとして品質上の問題ではなく、生徒PFレビューとは用途が異なると分析
  - 現行Education ReviewerにはUser-first・Evidence重視等の教育向け基盤が既に存在することを確認
  - PF用途では、作品目的、Scope、本人理解・説明可能性、README・成果物の伝達性、採用・面接視点が不足していると分析
  - Reference Claude PersonaおよびEducation ReviewerのPersona本体変更は未実施

## 作業中

- なし

## 次工程

1. `project-notes/2026-08-27-portfolio-reviewer-fit-analysis.md` を分析Evidenceとして、`personas/education/GEM_REVIEWER.md` の職業訓練校生向けPFレビューへの再設計を行う。
2. `personas/reference/CLAUDE_PERSONA.md` Version 1.3 は実務参考Reviewerとして維持し、本分析だけを理由に変更しない。
3. 再設計で新たなUser決定が発生した場合は、Education Reviewer本体へ即時反映し、必要に応じて同ファイルの `Decision & Rationale` へ記録する。
4. 現行成果物は配布可能な完成状態として維持し、対象外のPersona・設定資料へ変更を広げない。

Reviewerを含むPersonaの機能設計はEvidenceなしに再検討しない。完了済みの文書適合性復旧を、Evidenceなしに再作業対象へ戻さない。`ASKME 迎合禁止` と7文書配置を未決事項へ戻さない。Education用の基本体系は4Gemであり、`Researcher Deep Research` はResearcher Personaを使う追加Gemとして扱う。

## 正本の所在

- 作業規則：`AGENTS.md`
- Repository入口・Persona重要性の共通説明：`README.md`
- Education Persona：`personas/education/`
- Education入口：`personas/education/README.md`
- Education Gemini設定資料：`personas/education/setup/GEMINI_GEM_SETUP.md`
- Reference Persona：`personas/reference/`
- Reference入口：`personas/reference/README.md`
- 現行仕様の判断理由：各成果物MDの `Decision & Rationale`
- 2026-08-23より前の判断経緯・復旧・監査Evidence：`project-notes/YYYY-MM-DD-*.md`（履歴。現行仕様の代替正本ではない）
- 2026-08-27 PF Reviewer適合性分析Evidence：`project-notes/2026-08-27-portfolio-reviewer-fit-analysis.md`

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
- `project-notes/2026-08-27-portfolio-reviewer-fit-analysis.md`
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
