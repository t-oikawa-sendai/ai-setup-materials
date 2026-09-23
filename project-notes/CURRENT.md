# CURRENT

Last Updated: 2026-09-23
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
- 2026-08-27 Education Reviewerを職業訓練校生のポートフォリオレビュー向けに更新
  - `personas/education/GEM_REVIEWER.md` を Version 1.1 / Status Approved へ更新
  - 主対象を、IT系企業・職種への就職・転職を目指す職業訓練校生のポートフォリオと明確化
  - Evidence重視、User-firstフロー、Solution Partner / Code Generatorとの責務境界を維持
  - 作品目的、Scope、要求・設計・実装整合、機能、必要十分なコード品質、基本セキュリティ、test Evidenceを中心評価へ整理
  - README・成果物の伝達性、本人理解・説明可能性、採用・面接視点を追加
  - 実務向け高度監査は作品の性質に応じた条件付き評価へ変更
  - 総合判定 `PASS / PASS WITH NOTES / REWORK REQUIRED / BLOCKED` は維持し、PF向け修正優先度 `提出前必須 / 推奨修正 / 改善候補` を追加
  - 判断理由を同Personaの `Decision & Rationale` に記録
  - Reference `CLAUDE_PERSONA.md` Version 1.3 は実務参考Reviewerとして変更せず維持
- 2026-09-01 Education Solution Partnerを Version 1.3 / Status Approved へ更新
  - Version 1.1：仕様外追加・勝手な補完の抑制、未確定事項の区別、対象者・学習レベルへの適合、出力形式優先、Design Response Checkを追加
  - Version 1.2：初学者向け設計書・仕様書・説明資料で、冒頭の目的説明と末尾の決定範囲・未確定事項・次工程説明を必須化
  - Version 1.3：指定された表・列・項目構造の維持、機能名から未指定詳細を一般論で確定しないこと、継続設計で確定済み名称・クラス分割・責務・用語を理由なく変更しないことを追加
  - User承認済みのVersion 1.1〜1.3 Persona本文を保持
- 2026-09-01 Solution Partner Personaの記録配置を復旧
  - AIがUser未承認で `GEM_SOLUTION_PARTNER.md` 末尾へ追加した `Decision & Rationale` を削除
  - Persona本文のUser承認済みVersion 1.1〜1.3内容は変更せず保持
  - 復旧commit：`10da225e4117b3b7e88f43c42706347d154edc71`
- 2026-09-01 `AGENTS.md` の決定履歴を是正
  - Solution Partner Version 1.1 / 1.2 / 1.3 の承認済み変更に関する Decision / Reason / Rejected を `AGENTS.md` の `Decision & Rationale` へ記録
  - Persona本文には変更履歴を再追加していない
  - 履歴是正commit：`34134536c95a9fff1a1a8930822474397daa38e0`
- 2026-09-01 Education Solution Partnerを Version 1.4 / Status Approved へ更新
  - AIが未決事項を勝手に補完・確定しない基本路線を維持
  - 未決事項を `次工程開始前に決定必須` / `実装段階まで持ち越し可能` の2区分へ分類
  - 決定必須項目は理由を初学者向けに説明し、ASKMEで解消するまで次工程へ進めない
  - 持ち越し可能項目は全件・一部・保留を選択でき、後から何度でも設計段階へ戻って再検討可能
  - 設計文書完成時・次工程引渡し時に固定名称 `補足A：未決事項一覧` を付与
  - `補足A` は `ID / 未決事項 / 区分 / 理由` の最小構成とし、未決事項0件の場合も合計・2区分の件数を明示
  - 決定済み項目は設計本文へ反映し、`補足A` から削除して件数を更新
  - ASKMEは最初に簡潔な質問を提示し、Userが判断できない場合のみ判断材料を追加
  - 不必要なASKMEを行わない
  - Decision Evidence：`project-notes/2026-09-01-solution-partner-unresolved-items-decisions.md`
  - Persona反映commit：`6fbc12721553ce96840440b94ea82bccd849c710`
  - Persona本文へ `Decision & Rationale` は追加していない
- 2026-09-13 Education Solution Partnerを Version 1.5 / Status Approved へ正式改版
  - 既存Version 1.4への部分追記ではなく、Persona本文を整理して責務境界を明確化
  - コード責務：完成実装コードの生成はCode Generatorの責務。説明・比較・設計判断用の疑似コード、部分的なサンプルコード、SQL例、設定例、コマンド例、部分コード、差分例は許容
  - コード可否は行数ではなく、「そのまま提出・実行できる完成実装か」で判断
  - ASKME保留時は作業停止を続けず、暫定値を `仮定` と明示して次工程へ進む
  - `補足A` に `仮定を置いて進めた事項` を追加
  - 旧 `Design Response Check` を含む重複規定を `Principles`、`ASKME`、`Output` 等へ統合し、Personaを簡潔化
  - 学習用途・初学者向けという従来の背景意図は維持
  - Persona本文へ `Decision & Rationale` は追加していない
  - Decisionは `AGENTS.md` の `Decision & Rationale`（2026-09-13）へ記録
  - Code Generator v2.1との整合確認：`仮定を置いて進めた事項` の扱い、およびASKME保留後のコード生成開始条件が Code Generator 2.1 に未記載。`GEM_CODE_GENERATOR.md` は未変更
- 2026-09-01 Education Code Generatorを Version 2.1 / Status Approved へ更新
  - `補足A：未決事項一覧` をSolution Partnerからの未決事項引継ぎインターフェースとして扱う規定を追加
  - `次工程開始前に決定必須` が残る場合はコード生成を開始しない
  - `実装段階まで持ち越し可能` は該当処理で判断が必要になるまで未決として保持する
  - 影響しない持ち越し事項だけを理由に全生成は停止しない
  - Solution Partner確定仕様の再設計、未決事項の推測補完、ASKME・分類責務の複製は行わない
- 2026-09-13 Education Code Generatorを Version 2.2 / Status Approved へ更新
  - Solution Partner v1.5の `補足A` 3区分（`次工程開始前に決定必須` / `実装段階まで持ち越し可能` / `仮定を置いて進めた事項`）へ対応
  - `仮定を置いて進めた事項` をUser確定仕様ではなく暫定実装条件として受領
  - 明示された仮定があることだけを理由に生成停止しない
  - Code Generator自身による仮定生成は禁止
  - 仮定とMandatory Rulesの衝突時は実装せず停止
  - 既存v2.1の未決事項制御思想、中核責務、Mandatory Rules、Default Practices、責務境界は維持
  - Persona本文へ `Decision & Rationale` は追加していない
  - Decisionは `AGENTS.md` の `Decision & Rationale`（2026-09-13）へ記録
  - Solution Partner v1.5 / Code Generator v2.2間の引継ぎ整合完了


- 2026-09-23 Education Reviewerを Version 1.2 / Status Approved へ更新
  - \`personas/education/GEM_REVIEWER.md\` を7,000文字以内へ簡潔化
  - 評価思想、Evidence重視、User-firstフロー、4段階判定、3段階優先度、説明可能性評価を維持
  - 重複していた責務境界・評価観点・修正フロー・禁止事項を統合
  - Persona本文から \`Decision & Rationale\` を削除
  - Reviewer判断履歴を \`project-notes/GEM_REVIEWER_DECISIONS.md\` へ分離

- 2026-09-23 Reference AI運用資料 Version 0.1 / Draft を追加
  - `personas/reference/PERSONA_OPERATION_CASE_STUDY.md`
  - `personas/reference/CHAT_HANDOFF_TEMPLATE.md` Version 0.2 / Draft
  - `personas/reference/PERSONA_PROMPT_TEMPLATE.md`
  - Case Studyの実践者表記を `O講師` に統一し、教材利用者との混同を防止
  - Handoffは正本ではなく状態移送手段として分離
  - Handoff Template v0.2でRepository Rules、Git同期Evidence、VERIFIED / UNVERIFIED / ASSUMPTION、停止条件、検証、完了報告を復旧
  - 導線監査を実施し、Root目的別入口、Reference推奨読順、3文書間の前後移動・戻り導線を追加
  - Navigation反映後：Case Study v0.2 / Prompt Template v0.2 / Handoff Template v0.3
  - PromptはBRIDGE（Background / Request / Inputs / Deliverables / Guardrails / Evaluation）で整理
  - Root README / Reference READMEへ最小導線を追加
  - 判断履歴：`project-notes/2026-09-23-persona-operation-case-study-decisions.md`

## 作業中

- Reference AI運用資料3文書 Version 0.1 / Draft の内容レビュー

## 次工程

1. Reference AI運用資料3文書 Version 0.1 / Draft をUserレビューし、必要な修正を反映する。
2. 3文書の内容確定後、Version / Statusの昇格要否をUser判断する。
3. 新チャット開始時はGitHubとの同期状態を確認し、`project-notes/CURRENT.md` → `AGENTS.md` → 対象成果物MDの順に読む。
4. `GEM_SOLUTION_PARTNER.md` Version 1.5 / Status Approved と、Version 1.1〜1.5の承認済み改善内容を確定事項として扱い、Evidenceなしに再検討しない。
5. `GEM_CODE_GENERATOR.md` Version 2.2 / Status Approved と、Solution Partner v1.5の `補足A` 3区分引継ぎ規定を確定事項として扱い、Evidenceなしに再検討しない。
6. Solution PartnerまたはCode Generatorの追加検証または修正は、Userの次指示または実利用で具体的な問題が確認された場合のみ行う。
7. Education Reviewerの実利用確認は未実施の次工程として保持するが、Userの指示なく自動的に切り替えない。
8. 対象外のPersona・設定資料へ変更を広げない。

Reviewerを含むPersonaの機能設計はEvidenceなしに再検討しない。完了済みの文書適合性復旧を、Evidenceなしに再作業対象へ戻さない。`ASKME 迎合禁止` と7文書配置を未決事項へ戻さない。Education用の基本体系は4Gemであり、`Researcher Deep Research` はResearcher Personaを使う追加Gemとして扱う。

## 正本の所在

- 作業規則：`AGENTS.md`
- Repository入口・Persona重要性の共通説明：`README.md`
- Education Persona：`personas/education/`
- Education Solution Partner正本：`personas/education/GEM_SOLUTION_PARTNER.md`
- Education Code Generator正本：`personas/education/GEM_CODE_GENERATOR.md`
- Education Reviewer正本：`personas/education/GEM_REVIEWER.md`
- Education入口：`personas/education/README.md`
- Education Gemini設定資料：`personas/education/setup/GEMINI_GEM_SETUP.md`
- Reference Persona：`personas/reference/`
- Reference入口：`personas/reference/README.md`
- Reference AI運用実践例：`personas/reference/PERSONA_OPERATION_CASE_STUDY.md`
- Reference Chat Handoff Template：`personas/reference/CHAT_HANDOFF_TEMPLATE.md`
- Reference Prompt Template：`personas/reference/PERSONA_PROMPT_TEMPLATE.md`
- Reference AI運用資料判断履歴：`project-notes/2026-09-23-persona-operation-case-study-decisions.md`
- 現行仕様の判断理由：原則として各成果物MDの `Decision & Rationale`。Education Reviewerは `project-notes/GEM_REVIEWER_DECISIONS.md`
- 2026-08-23より前の判断経緯・復旧・監査Evidence：`project-notes/YYYY-MM-DD-*.md`（履歴。現行仕様の代替正本ではない）
- 2026-08-27 PF Reviewer適合性分析Evidence：`project-notes/2026-08-27-portfolio-reviewer-fit-analysis.md`
- 2026-09-01 Solution Partner未決事項運用Decision Evidence：`project-notes/2026-09-01-solution-partner-unresolved-items-decisions.md`

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
4. `AGENTS.md` の `Decision & Rationale`（Solution Partner Version 1.1〜1.3および Version 1.5、Code Generator Version 2.2の判断履歴を含む）
5. `project-notes/2026-09-01-solution-partner-unresolved-items-decisions.md`（Solution Partner Version 1.4の未決事項運用Decision Evidence）
6. 必要時のみ `project-notes/YYYY-MM-DD-*.md`（2026-08-23より前の履歴）

## REFERENCES

- `AGENTS.md`
- `personas/education/GEM_SOLUTION_PARTNER.md`
- `personas/education/GEM_REVIEWER.md`
- `personas/education/setup/GEMINI_GEM_SETUP.md`
- `project-notes/2026-09-01-solution-partner-unresolved-items-decisions.md`
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
- `personas/reference/PERSONA_OPERATION_CASE_STUDY.md`
- `personas/reference/CHAT_HANDOFF_TEMPLATE.md`
- `personas/reference/PERSONA_PROMPT_TEMPLATE.md`
- `project-notes/2026-09-23-persona-operation-case-study-decisions.md`
- `README.md`