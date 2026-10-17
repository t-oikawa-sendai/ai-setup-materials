# CURRENT

Last Updated: 2026-10-17
Status: CURRENT

## PURPOSE

Personaの意義・効果・限界と役割分離を説明する `ai-setup-materials` を整える。Persona本文・検証Evidence・識別と検証の仕様を保持し、設定方法は対象外とする。責務範囲と作業規則は `AGENTS.md` および `README.md` を正本とする。

## 完了事項

- 2026-10-17 Education READMEの冒頭に、Gemini Skillsと本教材の運用方針を現行方針として記載した（D-048）。同一アカウント内のSkills使い分けは、評価の独立性を満たさない。自己正当化バイアスと自己選好バイアスは残る。Gemini Skillsで設計思想に沿う場合の必要条件は、役割別アカウントと、User（生徒）による成果物・Evidenceの引き渡しである。筆者の見解では、ChatGPTまたはClaudeのProjectを役割ごとに分ける方法がより適合する。この記載は、Skillの登録完了、動作確認、評価独立性の実証ではない。従来の4Gem＋1は履歴として維持する。Researcherの3完成版は、当面User（生徒）が調査範囲に応じて1版を明示選択する。Skillsによる完成版の自動選択は現行運用として案内しない。Deep ResearchをSkillsから利用できるとは記載しない。D-039、D-041、D-042、D-043、D-045の原文は変更していない。Root READMEの警告全文、Persona本文、既存の検証結果、Skill実体は変更・作成していない。commit と push は未実施。
- 2026-10-17 Userのcommit・push承認により、Root READMEの改稿と警告の強調、詳細比較資料への分離、Owner欄の統一、設定資料の廃止、D-039〜D-046を含む変更29ファイルをcommit `1e1a2b822f521612e67b7c54d4d8a86a20c0ea0d` として `main` へpushした。以下に残る「未commit・未push」は各変更直後の履歴であり、現時点のGit保存状況ではない。Persona Verificationの未達、適用状態 `UNVERIFIED`、未決事項は変更していない。
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

- 2026-09-29 中核4種Reference PersonaのSSOT方針を正本文書へ記録
  - `AGENTS.md` と `personas/reference/README.md` に記録
  - `solacom_main` の中核4種参照化の移行案を独立cloneで実装し、設計レビューを完了
  - [PR #21](https://github.com/t-oikawa-sendai/solacom_main/pull/21) はUser承認により `solacom_main` の `main` へ反映済み（merge commit：`16c44976638b48c53ef16399b1d51217c540be0a`）
  - 元Devcheckoutの既存未commit変更は保持。元Devcheckoutへの移行設定導入は未実施
  - 実機Cursorでの正本読込と外部AIサービスへの登録は未確認
  - 内部監査記録：[中核4種PersonaのSSOT検証記録](2026-09-29-core-persona-ssot-verification.md)
  - 独立cloneはmainへ合わせ、正本本文・6環境値・ignoreを確認済み。自動ルール読込はUNVERIFIED。元Devcheckoutへの導入は未実施

- 2026-10-03 Reference Claude Code設定資料を Version 1.0 / Status Approved へ昇格（User承認日：2026-10-03）
  - `personas/reference/setup/CLAUDE_CODE_SETUP.md`
  - Claude Desktop（Codeタブ）の `CLAUDE.md` 3層構成（全体共通、業務・開発領域、Repository）
  - 配置は `personas/reference/setup/`（AIサービス単位）
  - `CLAUDE_PERSONA.md` は変更していない
  - `Decision & Rationale` は同ファイルに記録（§5.4 の分離例外は適用していない）

- 2026-10-03 Reference Claude Code設定資料を Version 1.1 / Status Approved へ更新
  - `personas/reference/setup/CLAUDE_CODE_SETUP.md`
  - Reference中核4種を Claude Code のサブエージェントとして使う構成と作り方を追記
  - 定義ファイルへ正本の本文は複製せず、作業開始時に正本を読ませる
  - §4.1 と §4.2 の記載例を、現行の `~/.claude/CLAUDE.md` と `~/Dev/CLAUDE.md` から写し直した
  - 中核4種の Persona 本文は変更していない

- 2026-10-05 Researcher系Persona 4ファイルを Version 1.1 / Status Approved へ更新（User承認日：2026-10-05）
  - `personas/education/GEM_RESEARCHER_FULL.md`、`GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`、`GEM_RESEARCHER_DEVELOPMENT.md`、`personas/reference/GEMINI_PERSONA.md`
  - Researcher Gem（Version 1.0）が二次記事を要約しただけで確認済み事実として提示したインシデントへの対策
  - 提示資料の扱い（要約依頼と真偽確認の区別、資料性質の確認、主張ごとの振り分け、循環根拠の禁止）を追加。Education 3種は同一文
  - Reference版は9章の停止条件を限定し、11章の誤り時の原因を「確認できない場合は未特定」へ変更
  - Reference版冒頭の責務分担を「設計：ChatGPT、Gemini Gem、Owner」「実装：Cursor」「レビュー：Claude、ChatGPT、Owner」へ修正（User指示）
  - 判断履歴は `project-notes/RESEARCHER_PERSONA_DECISIONS.md` へ分離し、各PersonaからHTMLコメントで参照（§5.4 の分離例外をUser決定により適用）
  - 内部記録：`project-notes/2026-10-05-researcher-persona-incident-record.md`
  - テスト用Gemでの実動検証は未実施。本番Gemは実動検証の合格まで Version 1.0 を維持

- 2026-10-13 判断履歴の記録規則を改訂した。既存判断履歴は原文と保存場所を維持し、適用後の新判断は `project-notes/DECISIONS.md` に記録する。中央Governanceの正式導入は別工程のまま未了であり、この改訂は導入完了ではない。
- 2026-10-13 Git同期ゲートの適用をローカル変更へ限定した。読取専用ではローカルGit同期を要求せず、読み取ったRepository、branch、commit SHAを報告する。SHAを確認できない場合は未確認とする。ローカル変更は従来の同期ゲートと停止条件を維持し、読取から変更へ移行する前に同期ゲートを実施する。Decisionは `project-notes/DECISIONS.md` の D-002。main の `179cecc4cddd53308950d8a09a6ab5b4a142cc46` に反映済み。
- 2026-10-13 Reference Claude Persona の Document Info を Version 1.4 / Status Approved / Last Updated 2026-10-13 へ更新した。Persona本文は変更していない。Decisionは `project-notes/DECISIONS.md` の D-003。GitHub main の ad52f4b39a781b84a2d824d1c0ddb137c95eaa7b に反映済み。
- 2026-10-13 Reference運用資料のD-001・D-002整合是正をローカル反映した。Decisionは `project-notes/DECISIONS.md` の D-004。Version / Status は昇格していない。
  - Case Study：`personas/reference/PERSONA_OPERATION_CASE_STUDY.md` Version 0.2 / Draft
  - Handoff Template：`personas/reference/CHAT_HANDOFF_TEMPLATE.md` Version 0.3 / Draft
  - Prompt Template：`personas/reference/PERSONA_PROMPT_TEMPLATE.md` Version 0.2 / Draft（今回未変更）
- 2026-10-13 GOV-09のD-001・D-002整合是正はGitHub反映済み。反映commitは `eadc8a2ccb36706aac1e81c9b934904a942460fe`。変更対象5ファイルが一致し、対象外変更はない。D-004はGitHub保存済み。Reference運用資料3文書の Version / Status は変更していない。
  - 変更ファイル：`AGENTS.md`、`personas/reference/CHAT_HANDOFF_TEMPLATE.md`、`personas/reference/PERSONA_OPERATION_CASE_STUDY.md`、`project-notes/CURRENT.md`、`project-notes/DECISIONS.md`
  - Case Study Version 0.2 / Draft、Handoff Template Version 0.3 / Draft、Prompt Template Version 0.2 / Draft
  - 確認時点の Local HEAD、origin/main、GitHub main HEAD は `eadc8a2ccb36706aac1e81c9b934904a942460fe` で一致。worktree は clean
  - 当該SHAの GitHub Actions 実行履歴は確認時点で 0件。SUCCESS とは記録しない
- 2026-10-14 3モデル分のUser提出検証回答（Gemini、Claude、ChatGPT）と提出元全文、マニフェストを `project-notes/persona-validation/raw/` へ無改変で保全した。検証用Persona `personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md` は Version 0.1 / Draft のまま維持する。Decisionは `project-notes/DECISIONS.md` の D-005
- 2026-10-14 ChatGPTが今回の保全に先立ち示した GitHub main HEAD `85655023bcc6116dce4beb8b4f416d52840d8f5f` は、origin/main および GitHub main と一致した。この確認は、同日3回答の取得自己申告とは別である。3回答の実際のGitHubアクセスは UNVERIFIED
- 2026-10-14 Persona識別と設定案内の追加仕様を [`../personas/PERSONA_IDENTIFICATION_AND_SETUP.md`](../personas/PERSONA_IDENTIFICATION_AND_SETUP.md) へ記録した。判断は `project-notes/DECISIONS.md` の D-006〜D-016。この完了は仕様の記録である。全11 Persona本文の Version 3.0 への移行、設定案内専用Personaの本文の正式作成、各AIサービスの実動検証は、この完了に含まない
- 2026-10-14 M-Personaの利用方針を、Owner専用の禁止規則から、知識・経験・運用能力に応じた推奨基準へローカル反映した。正本は [`../personas/PERSONA_IDENTIFICATION_AND_SETUP.md`](../personas/PERSONA_IDENTIFICATION_AND_SETUP.md) 第9章。第11章の選定、ASKME、例Bを第9章へ整合した。同ファイルの判断履歴の参照範囲は D-006〜D-017 とし、第14章の境界表現は利用推奨基準へ合わせた。Decisionは `project-notes/DECISIONS.md` の D-017。D-017は D-012 の Owner専用規則と一般利用者への M- 案内禁止を上書きする。D-012 と D-015 の原文は変更していない。D-015 は上書きしていない。知識水準が不明な場合の標準案内は S- である。Owner以外の M- 利用は禁止しない。利用経験による本人認証とアクセス権限制御は追加していない。M/S/T の分類名称、既存11 Personaの本文と Version、確定11 ID、設定案内専用Personaの名称・ID・配置は変更していない。commit `a72b6258e69977544bd269c9190d3d243d00c76d` を `main` へpush済み。push後の Local HEAD、origin/main、GitHub main は同SHAで一致した
- 2026-10-14 Persona配布元の保護方針を [`../personas/PERSONA_IDENTIFICATION_AND_SETUP.md`](../personas/PERSONA_IDENTIFICATION_AND_SETUP.md) 第10.1節と第11章へローカル反映した。判断履歴の参照範囲は D-006〜D-018 とした。Decisionは `project-notes/DECISIONS.md` の D-018。D-001〜D-017の原文は変更していない。D-017の内容は変更していない。既存Personaの本文とVersionは変更していない。GitHubのアクセス制御、認証、新しい配布システム、自動同期は追加していない。反映commitは `a82ca1deb4ce7c0844c1f886ea4bc2894b007161`。2026-10-14の本作業開始時、Local HEAD と fetch 後の origin/main はこのSHAで一致した
- 2026-10-14 Reference ChatGPT Persona `personas/reference/CHATGPT_PERSONA.md` の §2、§4、§5、§7 を、ユーザー指定の正式修正案で置換した。Version 1.2（提案）/ Status Draft、Document Info、他節、既存 `Decision & Rationale` は変更していない。Decisionは `project-notes/DECISIONS.md` の D-019。commit と push は未実施。Approvedへの昇格と実動検証は未実施
- 2026-10-14 設計担当による一律のcommit前差分レビューを廃止し、実装担当の検証と、リスクに応じたClaude独立レビューへ切り替える規則を、`personas/reference/CHATGPT_PERSONA.md` の §5 と §7 へ反映した。Version 1.2（提案）/ Status Draft は維持した。Decisionは `project-notes/DECISIONS.md` の D-020。D-019のうち D-020 が上書きしない範囲は維持した。commit と push は未実施。Approvedへの昇格と実動検証は未実施
- 2026-10-15 Persona Verification を、今回のPersona大改修の最優先確定要件として記録した。正本は [`../personas/PERSONA_IDENTIFICATION_AND_SETUP.md`](../personas/PERSONA_IDENTIFICATION_AND_SETUP.md) の第16章。当時の Document Info は Version 1.1 / Approved である。起点は、変更していない第11.1節の動作確認方法の案内と、第11.4節の「適用成功は別途検証する」である。第3章から第12章の確定文、設定案内専用Personaの責務、既存Personaの Version と Status、既存の検証原文は変更していない。流れは、Persona定義・改訂、設定・適用、Persona Verification、User承認判断、正式運用である。Decisionは `project-notes/DECISIONS.md` の D-021。D-001〜D-021の原文は変更していない。この記録は、検証設計の確定、実動検証の完了、PersonaのApproved昇格を含まない。取得成功と適用成功は前提にしていない。このRepositoryに CHANGELOG はない
- 2026-10-15 Claude独立レビュー指摘の是正をローカル反映した。正本は [`../personas/PERSONA_IDENTIFICATION_AND_SETUP.md`](../personas/PERSONA_IDENTIFICATION_AND_SETUP.md) Version 1.2 / Approved。新規と改訂のすべて、および Version 3.0 移行を検証対象とし、FAILと不承認は修正・再検証へ戻る。ChatGPT Persona は Version 1.2（提案）/ Draft のまま、Last Updated は 2026-10-15 である。Decisionは `project-notes/DECISIONS.md` の D-022。D-001〜D-021の原文は変更していない。実動検証、PersonaのApproved昇格、commit、push は未実施である。同期ゲートについて、未commit差分を保護したまま編集する例外は、この是正作業に限るUser承認であり、`AGENTS.md` は変更していない
- 2026-10-15 必要性の根拠がない独立レビューを禁止し、真に必要な独立レビューを必須とする規則をローカル反映した。重大リスクの commit 前独立レビュー、実装担当の検証、Persona Verification の必須工程は維持した。Decisionは `project-notes/DECISIONS.md` の D-023。D-001〜D-022の原文は変更していない。commit と push は未実施である
- 2026-10-15 Userが明示した最優先目的を作業完了まで維持し、その達成に必要と説明できる追加作業だけを行い、不要な工程を自動生成しない規則をローカル反映した。重大リスクの必須レビュー、必要なPersona Verification、Userの承認権限、§6の停止条件は維持した。Decisionは `project-notes/DECISIONS.md` の D-024。D-001〜D-023の原文は変更していない。commit と push は未実施である
- 2026-10-15 D-019〜D-024 の反映は commit `73b71b1dbf3dce8b99731a4207b9fa2924bfbb17` として `main` へ push 済みである。同日の同期確認で Local HEAD、origin/main、GitHub main はこの SHA で一致した。直前の完了事項にある D-019〜D-024 の「commit と push は未実施」は、この commit より前の記録であり、その文は改変しない。この commit は Approved への昇格と実動検証を含まない。ChatGPT Persona は Version 1.2（提案）/ Draft のままである
- 2026-10-15 誤った配置是正を撤回した。`personas/reference/CHATGPT_PERSONA.md` 第11章は、検証用Persona第16章の識別・取得・更新検証の5機能を、共通仕様第7章・第8章の識別形式で実装する是正とした。Persona ID は `M-CG`、Version は 1.2（提案）、Status は Draft、Verification Code は未確定のままである。`personas/PERSONA_IDENTIFICATION_AND_SETUP.md` 第16章と、その削除に伴い変わっていた第1章、第14章、第15章は、基準 HEAD `73b71b1dbf3dce8b99731a4207b9fa2924bfbb17` の原文へ復元した。この Approved は共通仕様の文書状態であり、ChatGPT Persona の Approved 昇格ではない。Decisionは `project-notes/DECISIONS.md` の D-026 を正しい是正内容へ記録し直したものである。D-001〜D-025の原文は変更していない。D-025 の TC-01〜TC-03、各2回、合計6回、6回すべてPASSは維持している。実動検証6回、Approvedへの昇格、commit、push は未実施である
- 2026-10-15 ChatGPT Persona第1章から第11章の重複規則を整理し、末尾の `Decision & Rationale` を削除して `project-notes/DECISIONS.md` の D-027 に原文のまま保全した。Version は 1.2（提案）、Status は Draft のままである。文字数は Unicode のコードポイント数で、末尾改行は除く。整理前のファイル全体は 9,871、Document Info を除き末尾の `Decision & Rationale` を含む範囲は 9,539、第1章から第11章は 9,285 である。整理後のファイル全体は 8,230、Project登録対象は 7,898 である。登録対象は `# ChatGPT向け責務定義` から本文末尾までとし、Document Info は含めない。登録対象の末尾改行を含めると 7,899 である。実動検証6回は未実施である。Approvedへの昇格、commit、push は未実施である
- 2026-10-15 Personaの文字数上限を恒久ルールとして `AGENTS.md` §3.4 へ追加した。Decisionは `project-notes/DECISIONS.md` の D-028。新規Personaと今後の改訂に適用する。変更対象外の既存Personaは一括修正していない。D-001〜D-027の原文は変更していない。commit、push は未実施である
- 2026-10-15 ChatGPTとCursorの指示・報告順序を `AGENTS.md` §2.3 へ追加した。順序は、ChatGPTがCursor指示書を提示し、Cursorの完了・停止・未達報告を待ち、ChatGPTが報告内容とEvidenceを確認・評価し、必要な場合だけ次の指示を提示する。Cursor報告前の新規指示・追加指示・別工程の割り込みは禁止する。Decisionは `project-notes/DECISIONS.md` の D-029。§2.1の恒久規則は変更していない。今回の記録に限り、既知の未commit変更を保護するため §2.1 の停止条件を例外扱いとした。ChatGPT Personaのファイル全体は、末尾改行を含めて8,231文字であり、7,500文字を731文字超過した未達のままである。D-025の実動検証6回、Approved昇格、commit、push は未実施である
- 2026-10-15 7,500文字を必須上限から設計目標値へ変更した。正本は `AGENTS.md` §3.4。Decisionは `project-notes/DECISIONS.md` の D-030。D-028の必須上限を、7,500文字を設計目標値とし、超過だけを不合格または作業停止としない範囲で上書きする。D-028とD-029の原文は変更していない。直前の完了事項にある7,500文字超過の未達は、D-030より前の記録であり、その文は改変しない。AIサービスの実際の登録制限への適合は必須である。D-027のProject登録対象8,000文字以内は維持する。有効な規則は文字数削減を理由に削除・緩和していない。D-025の実動検証条件とD-029の指示・報告順序は変更していない。今回のD-030とD-031に限り、既知の未commit変更を保護するため `AGENTS.md` §2.1 の停止条件を例外扱いとした。§2.1の恒久規則は変更していない。commit、push、Approved昇格は未実施である
- 2026-10-15 ChatGPT Personaの実装担当の役割名を `CodingAI` とした。`Cursor` は現在の使用製品名として維持した。反映範囲は `personas/reference/CHATGPT_PERSONA.md` の §1、§2、§3.1、§3.2、§5、§7。Decisionは `project-notes/DECISIONS.md` の D-031。実装担当の責務、権限、指示形式、運用順序、検証、Git操作条件は変更していない。他Persona、製品名、ファイル名は変更していない。ファイル全体は末尾改行を含めて8,323文字、除いて8,322文字である。設計目標値7,500文字との差は823文字であり、この超過だけは不合格または作業停止としない。Project登録対象は `# ChatGPT向け責務定義` から本文末尾までで、末尾改行を含めて7,991文字、除いて7,990文字であり、8,000文字以内である。D-001〜D-030の原文は変更していない。commit、push、Approved昇格は未実施である
- 2026-10-15 ChatGPT Persona Version 1.2（提案）/ Draft の実動18回答を、`project-notes/persona-validation/` へローカル保存した。原文は `raw/`、評価は `assessments/2026-10-15.md`、集計は `SUMMARY.md` の2026-10-15の節である。サービスは ChatGPT Project、Claude Project、Gemini Gem。TC-01、TC-02、TC-03 を各2回。回答内容の評価は 11/18 PASS（ChatGPT Project 6/6、Claude Project 2/6、Gemini Gem 3/6）である。出典はUser転記であり、元画面との逐字一致は未検証である。Persona適用状態は UNVERIFIED である。この保存は Approved 昇格ではない。2026-10-14の検証用Personaの原文は変更していない。D-005 と D-025 の原文は変更していない。commit と push は未実施である
- 2026-10-15 ChatGPT検証専用Projectの再テスト6回答を、`project-notes/persona-validation/raw/` へ追加した。正規比較は ChatGPT検証専用Project 4/6、Claude Project 2/6、Gemini Gem 3/6、合計 9/18 である。従来ChatGPT Projectの 6/6 は参考履歴として残す。累積原文は24件である。Decisionは `project-notes/DECISIONS.md` の D-032。D-001〜D-031の原文、既存18回答の原文とSHA-256、先に記録した評価本文は変更していない。4/6 は D-025 の6回すべてPASSを満たさない。Persona適用状態は UNVERIFIED である。Approvedへの昇格はしていない。直前の完了事項にある18回答の「commit と push は未実施」は、この再テスト記録より前の文であり、その文は改変しない。18回答は commit `86b3537dfb8c2eacca851763c00055500ee122bd` にある。この再テスト記録の commit と push は未実施である
- 2026-10-15 Reference Claude Persona へ識別・取得・更新検証の第15章を追加した。`personas/reference/CLAUDE_PERSONA.md` の Document Info は Version 1.5（提案）/ Status Draft / Last Updated 2026-10-15 である。Persona ID は `M-CL`。Verification Code は未確定である。第0章から第14章のレビュー責務は維持した。第2章の `AGENTS.md` 本文確認は変更していない。第7章の通常確認は、読込状態の三定義の重複だけを第15.5節への参照へ整理した。既存の `Decision & Rationale` は原文のままである。最終 Approved は Version 1.4（D-003）である。Decisionは `project-notes/DECISIONS.md` の D-033。共通仕様第16章は変更していない。実動検証、Version 1.5 の正式承認、commit、push は未実施である
- 2026-10-15 Claude Persona 第0章から第15章の重複を整理した。第13章は、提出前の反証、反論への再検証、誤り確認後の訂正を残して短縮した。末尾の `Decision & Rationale` は削除し、2026-08-27の原文は `project-notes/DECISIONS.md` の D-034「保全する原文」へ移した。直前の完了事項にある「既存の `Decision & Rationale` は原文のままである」は、この移管より前の記録であり、その文は改変しない。Version は 1.5（提案）、Status は Draft のままである。最終 Approved は Version 1.4 である。第2章の `AGENTS.md` 確認文は §15.5 への参照へ置き換えた。確認規則は §15.5 に残している。Decisionは D-034。実動検証、正式承認、commit、push は未実施である
- 2026-10-15 Claude Persona のProject登録対象を8,000文字以内に収めた。登録対象は `# Claude Persona` から本文末尾までで、Document Infoを除き、末尾改行を含めて7,926文字である。ファイル全体は末尾改行を含めて8,257文字である。第7章の本格レビューは項目一覧にし、集約表の列、判定値、停止条件、第13章の3機能、第15章の5機能は残した。Decisionは `project-notes/DECISIONS.md` の D-035。D-001〜D-034の原文は変更していない。Version は 1.5（提案）、Status は Draft のままである。最終 Approved は Version 1.4 である。`AGENTS.md` の7,500文字は設計目標値のままである。実動検証、正式承認、commit、push は未実施である
- 2026-10-16 Claude Persona Version 1.5（提案）/ Draft は commit `a908abaf46b0a4bbd8b37c16cf0efdb2ab69fe62` として `main` へ push 済みである。作業開始時の同期で Local HEAD、origin/main、GitHub main はこの SHA で一致した。直前の完了事項にある D-033、D-034、D-035 の「commit、push は未実施」は、この commit より前の記録であり、その文は改変しない。この commit は Version 1.5 の Approved 昇格と、Persona全体の正式な Persona Verification を含まない。最終 Approved は Version 1.4（D-003）のままである。G方式用指示文は作成済みである。Claudeによる取得成功は自己申告であり、客観的なGitHubアクセスの確認ではない。Userは指示文と検証回答を視認し、問題なしと評価した。Claude独立レビューは条件付き合格である。独立レビューの原文は `project-notes/persona-validation/raw/2026-10-16-claude-independent-review.md` に保全した。検証回答の原文は未取得であり、保存していない。Gemini Personaの大改修は今回の対象外である
- 2026-10-16 ChatGPT Persona の §1、§4、§5、§7 を限定改善した。技術評価・完了条件確認とUserの最終受入を分け、目的単位の一括指示、根拠を示せない追加確認の禁止、FAILとUNVERIFIEDの表示保持、単純なGit操作での6項目を反映した。Version は 1.2（提案）、Status は Draft、Last Updated は 2026-10-16、Verification Code は未確定である。Decisionは `project-notes/DECISIONS.md` の D-036。D-025 の検証条件と D-032 の正規結果は維持した。4/6 は検証合格ではなく、適用状態は UNVERIFIED である。Approvedへの昇格、commit、push は未実施である
- 2026-10-16 Userは、現行11 Personaの現在版を正式承認した。Userは自ら実動検証を行い OK であると報告した。AIが実動検証を直接実施したとは記録しない。承認日は2026-10-16。Decisionは `project-notes/DECISIONS.md` の D-037。Education 6、Reference 4、検証用 1 である。既に Approved の5件は再編集していない。Draftだった6件は、数値 Version を維持し、提案表記を外し、Status を Approved、Last Updated を 2026-10-16 とした。D-025 の6回すべてPASS、D-032 の 4/6 と 9/18、UNVERIFIED、FAIL、原文、SHA-256 は変更していない。この承認は commit または push の承認ではない。commit と push は未実施である
- 2026-10-16 Userは、版番号を Version 3.0 に揃え、Version 2.0 は共通基点にせず欠番とすると決定し、`GEM_` で始まる6件は大改修の完了後に Version 3.0 へ揃えると限定した。Reference の5件（ChatGPT、Claude、Cursor、Gemini、検証用）の Document Info は Version 3.0 / Approved、Last Updated は 2026-10-16 である。`GEMINI_PERSONA.md` は `GEM_` 接頭辞ではないためこの5件に含む。`GEM_` 6件は現在の数値 Version / Approved を維持する。全11の User承認は D-037 のまま有効である。この版番号統一は、共通仕様の全機能移行の完了ではなく、再検証へ戻す理由ではない。4/6、9/18、UNVERIFIED、FAIL、原文、SHA-256 は変更していない。Decisionは `project-notes/DECISIONS.md` の D-038。commit と push は未実施である
- 2026-10-16 Root READMEへUser指定のGemini Skills警告全文を原文のまま掲載し、AIの問題から運用案内までの導線、具体例、構造比較図をローカル反映した。当時のREADMEは Version 1.3（提案）/ Draft、Decisionは D-039。その後、Userは改稿と詳細比較・A/B検証の別文書化を承認した。現行READMEは Version 1.3 / Approved、詳細の正本は `personas/WHY_PERSONA_MATTERS.md`、Decisionは D-040。Persona本文と旧Decision原文は変更していない。commit と push は未実施。
- 2026-10-16 Researcherの調査対象切替にはSkillsの自動適用が適するというUserの見解を受け、Learning / Career / Developmentの選択をSkillsの検討対象とし、Deep Researchは別運用とする範囲を `personas/education/README.md` と D-041 に記録した。Google公式案内では現時点でSkillsはDeep Researchに非対応。Skill構成・選択条件・実動検証は未決・未実施であり、現行のResearcher完成版選択と `Researcher Deep Research` Gemの手順、Persona本文は変更していない。commit と push は未実施。

- 2026-10-16 Userの個別承認により、Education README末尾の旧判断3件をD-042へ原文のまま移管し、本文から当該節を削除した。移管原文のSHA-256一致、現行手順とリンク、D-040による旧掲載先の上書き関係を確認した。Persona本文とGemini設定資料は変更せず、commit と push は未実施。
- 2026-10-16 Userは講師・生徒アカウントでGemを新規作成できないと報告した。D-043により、Root/Education READMEの新規作成導線を訂正し、Gem設定資料には現行対象アカウントで新規導入に使えない旨を明記した。既存Gemの利用・編集可否、代替導入先は未確認・未決。Google全アカウントでの作成不可とは断定せず、旧設定資料と判断履歴を保全した。Persona本文、commit、pushは変更・実施していない。
- 2026-10-17 User指定により、履歴・archive・検証原文を含む24文書のOwner欄を `Takashi Oikawa` に統一した（D-044）。GitHubアカウント名・URLと旧判断本文は維持した。commit、pushは未実施。
- 2026-10-17 User決定により、RepositoryはPersonaの意義・効果・限界の説明に集中し、サービス別の設定方法を対象外とした（D-045）。GeminiとClaude Codeの設定資料2件を廃止し、旧判断節を原文のままD-045へ移管した。識別・検証の共通仕様は維持する。過去に完了した設定資料の記録は当時の履歴であり、現行資料の所在を示さない。commit、pushは未実施。
- 2026-10-17 Root READMEの対象者を職業・所属やAI経験で限定せず、五つの関心・目的で示した。Root READMEの作業主体の呼称は `User` に統一した（D-046）。Education用Persona本文と既存検証結果は変更していない。commit、pushは未実施。
- 2026-10-17 Userが選んだ新VersionのChat Handoff Templateを、Version 0.4 / Draft の現行正本へローカル反映した（D-047）。同じAIの新規チャットを基本とし、GitHub管理中・ローカルGitのみ・Gitなしの保存方式、送受信時の正本照合、読取専用とローカル変更の区別を記載した。二つのチャットによる試験は「重要な事実を矛盾なく受け取れた」と評価したが、詳細な問題は実運用で確認する。commit、pushは未実施。

## 作業中

- 2026-10-17 Userは ASKME-01（GOV-01）B案を確定した。同一AIサービスでも、設計・実装時の会話・記憶・参照情報から判断を分離し、Userが成果物とEvidenceを選定・引き渡す場合は独立レビューを認める。異なるAIサービスや別Project・セッションだけでは認めない。この決定を `personas/reference/CHATGPT_PERSONA.md` Version 3.1（提案）/ Draft と D-050 へローカル反映した。実動検証とUser最終承認は未了である。commit と push は未実施である。
- 2026-10-17 Personaの回答識別表示インシデントとUserの根本仮説を、`project-notes/2026-10-17-persona-operation-incident-record.md`、`AGENTS.md`、D-049へローカル記録した。記録は原因特定、例外処理の確定、仮説の実証、是正完了を意味しない。画面のWorkと内部kindのどちらをサービス略号の層にするかは未決であり、CG、Codex、?のいずれも正式値にしていない。GitHub `main` への保存成否は、本文から推定せず、この記録を含む commit SHA と remote の `main` HEAD の一致で確認する。
- 2026-10-16 Claude Persona の現行ファイルは Version 3.0 / Approved（承認は D-037、版番号は D-038）である。現行の Version 3.0 / Approved はローカルの未commit・未pushである。commit `a908abaf46b0a4bbd8b37c16cf0efdb2ab69fe62` が `main` へ push 済みとして保存したのは、承認前の Version 1.5（提案）/ Draft である。Project登録対象は `# Claude Persona` から本文末尾まで、末尾改行を含めて7,925文字であり、8,000文字以内である。ファイル全体は末尾改行を含めて8,254文字である。第15章の5機能、レビューの確認項目、停止条件は維持している。2026-08-27の判断原文は D-034 の「保全する原文」にある。D-003 の Version 1.4 / Approved は当時の承認履歴である。現行版は Version 3.0 / Approved（承認は D-037、版番号は D-038）である。Persona ID は `M-CL`。Verification Code は未確定である。G方式用指示文は作成済みである。Claudeによる取得成功は自己申告であり、客観的なGitHubアクセスの確認ではない。Userは指示文と検証回答を視認し、問題なしと評価した。Claude独立レビューは条件付き合格である。独立レビュー原文は `project-notes/persona-validation/raw/2026-10-16-claude-independent-review.md` にある。検証回答の原文は未取得であり、保存していない。User最終承認は D-037 のまま有効である。版番号は D-038 で 3.0 とした。この版番号統一は、既存の技術的検証結果の合否を変えず、再検証へ戻さない。共通仕様第16章の独立工程は移動・複製していない。Gemini Personaの機能の大改修は今回の対象外である。Gemini の版番号は D-038 で 3.0 とした
- 2026-10-15 ChatGPT Persona の現行版は Version 3.0 / Approved（承認は D-037、版番号は D-038）である。D-025 の技術条件は、この承認とは別に未達のままである。検証条件は `project-notes/DECISIONS.md` の D-025。TC-01、TC-02、TC-03 を各2回、合計6回とし、6回すべてPASSを合格条件とする。第11章は自己識別・取得・更新検証であり、共通仕様第16章の独立検証工程は復元済みである。重複整理はローカル反映済みであり、この文書整理は6回の実動完了ではない。7,500文字は設計目標値である（D-030。Unicodeコードポイント数。Document Infoと末尾改行を含む）。超過だけを不合格または作業停止としない。D-037の承認表示後の実測は、末尾改行を含めて8,330、末尾改行を除いて8,329である。現在のOwner欄訂正後は、それぞれ8,329、8,328である。設計目標値との差は、承認表示後の実測では830文字、現在は829文字である。Project登録対象は `# ChatGPT向け責務定義` から本文末尾までで、末尾改行を含めて7,999、除いて7,998であり、D-027の8,000文字以内に適合する。D-036は6回の実動完了ではない。実装担当の役割名はCodingAI、現在の使用製品名はCursorである（D-031）。反映は §1、§2、§3.1、§3.2、§5、§7 に限る。責務、権限、指示形式、運用順序は変更していない。現行の Version は 3.0、Status は Approved（承認は D-037、版番号は D-038）である。正規比較は ChatGPT検証専用Project 4/6、Claude Project 2/6、Gemini Gem 3/6、合計 9/18 である。従来ChatGPT Projectの 6/6 は参考履歴である。D-025 の合格条件は6回すべてPASSのままであり、4/6 は検証合格ではない。Persona適用状態は UNVERIFIED のままである。4/6 と 9/18 は変更していない。現行版の User最終承認は D-037 であり、この承認は検証合格へ読み替えない
- 2026-10-15 将来の検証対象範囲の詳細基準は未承認である。G方式は検証中であり、正式運用の前提条件ではない。未実施の検証を実施済みとして扱わない
- 2026-10-13 ChatGPT ProjectでのGitHub Persona取得検証用の `personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md` Version 0.1 / Draft と、Reference入口の検証専用導線は、main の `ef77588d6c94bd50e0cc8c32c770f06c181a3bbb` に含まれている。ChatGPT Project上の取得検証は未実施。この「未実施」は2026-10-13時点の状態である。`personas/reference/setup/CHATGPT_PROJECT_PERSONA_TEST_SETUP.md` は、設定資料の本文が指示に含まれていなかったため未作成。現行 Document Info は Version 3.0 / Approved（承認は D-037、版番号は D-038）である。
- 2026-10-12 Repository作業時に対象の `AGENTS.md` を確認する規則と、通常報告の一行 `AGENTS.md：ReadOK / ReadNG / ReadUndefine` を、Reference の ChatGPT・Cursor・Claude の本文へ追加した。同じ User 決定を `AGENTS.md` の `Decision & Rationale` に記録した。ChatGPT の現行版は 3.0 / Approved、Cursor の現行版は 3.0 / Approved である（承認は D-037、版番号は D-038）。Claude の Document Info は、2026-10-13時点では Version 1.4 / Approved（D-003）であり、その改版では Persona本文を変更していない。現行ファイルは Version 3.0 / Approved（承認は D-037、版番号は D-038）である。
- 2026-10-07 対象Repository省略の是正対象をUser承認により記録。7 Persona・3文書・条件付き1文書。ChatGPT Personaの対象Repository明記は、2026-10-14の §7 置換（D-019）に含まれた。その他の本文是正は未着手。対象一覧と適用条件は `AGENTS.md` の `Decision & Rationale`（2026-10-07「対象Repository省略の是正対象を記録」）を参照
- Reference AI運用資料3文書全体の内容確定と Status 昇格は未了。現行版は Case Study Version 0.2 / Draft、Handoff Template Version 0.4 / Draft（D-047）、Prompt Template Version 0.2 / Draft
- Reference ChatGPT Persona `personas/reference/CHATGPT_PERSONA.md` は Version 3.0 / Status Approved（承認は D-037、版番号は D-038）、Last Updated 2026-10-16 である。2026-10-14に §2、§4、§5、§7 を正式修正案で置換済み（D-019）。同日、§5 と §7 に条件付き独立レビューの判定と依頼文の作成規則を追加した（D-020）。2026-10-15に §1 の受入・完了判定、§5 の例外のない重大リスクレビュー、GitHub反映後FAIL、未移行Repositoryの既存規則、§7 の依頼文の宛先を整合した（D-022）。同日、必要性の根拠がない独立レビューの禁止を §5 と §7 へ反映した（D-023）。同日、最優先目的の維持と不要な工程の自動生成禁止を §4、§7、§9 へ反映した（D-024）。D-019〜D-024 の文書反映は commit `73b71b1dbf3dce8b99731a4207b9fa2924bfbb17` として `main` へ push 済みである。2026-10-15に第11章を識別・取得・更新検証へ是正した（D-026）。その是正は commit `a627f4b2519b3750b7f3ea6f9cdd16898807ff15` に含まれている。同日、第1章から第11章の重複を整理し、末尾の Decision & Rationale を D-027 へ移した。この重複整理は commit `86b3537dfb8c2eacca851763c00055500ee122bd` に含まれている。2026-10-15に、7,500文字を設計目標値へ変更し（D-030）、実装担当の役割名をCodingAIとした（D-031）。Cursorは現在の使用製品名である。この呼称変更はD-027の整理結果に対する追加変更であり、責務、権限、指示形式、運用順序は変更していない。7,500文字の超過だけを不合格または作業停止としない。Verification Code は未確定である。D-027からD-031と先の18回答は commit `86b3537dfb8c2eacca851763c00055500ee122bd` に含まれている。正規比較は D-032 の 9/18 である。Persona適用状態は UNVERIFIED である。現行版の User最終承認は D-037 であり、4/6 と 9/18 は変更していない。2026-10-16の D-036 は §1、§4、§5、§7 の限定改善であり、その commit と push は未実施である
- 2026-10-06 決定の保留と仮定の実装利用許可を分離する規則（`実装利用：可／不可`）を、当時は Draft として3 Personaへ反映した。現行 Document Info は D-037 により Approved である。当時の最終 Approved は履歴である。この承認は実動検証の合否を変えない
  - `personas/education/GEM_SOLUTION_PARTNER.md` Version 1.6 / Approved（当時の最終 Approved は 1.5）
  - `personas/education/GEM_CODE_GENERATOR.md` Version 2.3 / Approved（当時の最終 Approved は 2.2）
  - `personas/reference/CURSOR_PERSONA.md` Version 3.0 / Approved（承認は D-037、版番号は D-038。当時の最終 Approved は 1.0）

## 次工程

1. Reference AI運用資料3文書（Case Study Version 0.2 / Draft、Handoff Template Version 0.4 / Draft、Prompt Template Version 0.2 / Draft）の残る内容をUserレビューし、必要な修正を反映する。Handoff Template v0.4の本文は反映済みである。GOV-09のGitHub保存は完了済みであり、3文書全体の内容確定または Status の昇格ではない。
2. 3文書の内容確定後、Version / Statusの昇格要否をUser判断する。
3. 新チャット開始時は `project-notes/CURRENT.md` → `AGENTS.md` → 対象成果物MDの順に読む。読取専用ではローカルGit同期を要求しない。ローカル変更の前には §2.1 の同期ゲートを実施する。
4. `GEM_SOLUTION_PARTNER.md` の最終Approved版 Version 1.5 と、Version 1.1〜1.5の承認済み改善内容を確定事項として扱い、Evidenceなしに再検討しない。現行版は Version 1.6 / Approved（D-037）である。当時の最終 Approved は Version 1.5 である。
5. `GEM_CODE_GENERATOR.md` の最終Approved版 Version 2.2 と、Solution Partner v1.5の `補足A` 3区分引継ぎ規定を確定事項として扱い、Evidenceなしに再検討しない。現行版は Version 2.3 / Approved（D-037）である。当時の最終 Approved は Version 2.2 である。
6. Solution PartnerまたはCode Generatorの追加検証または修正は、Userの次指示または実利用で具体的な問題が確認された場合のみ行う。
7. Education Reviewerの実利用確認は未実施の次工程として保持するが、Userの指示なく自動的に切り替えない。
8. 対象外のPersonaへ変更を広げない。
9. Researcher系Persona Version 1.1 の実動検証を、テスト用Gemで Version 1.0 と比較する計画は維持する（内部記録の第6章）。ただし現行の講師・生徒アカウントでGemを新規作成できないため、テスト用Gemの新規作成を前提とする実施は停止し、既存Gemの利用可否と代替検証方法の判断を待つ。合格と本番Gemへの反映は未実施。
10. 2026-10-07に記録した対象Repository省略の是正対象について、Userの次指示に従って本文を修正する。ChatGPT Personaの対象Repository明記は D-019 の §7 に含まれた。その他の対象は未着手である。対象一覧・適用条件は `AGENTS.md` の同日Decisionを参照し、記録済みであることを是正完了と扱わない。
11. `IT_GENERAL_ADVISOR_TEST_PERSONA.md` Version 0.1 / Draft と Reference入口の検証専用導線は、main の `ef77588d6c94bd50e0cc8c32c770f06c181a3bbb` に含まれている。ChatGPT Project上の取得検証は未実施。この「未実施」は2026-10-13時点の状態である。現行 Document Info は Version 3.0 / Approved（承認は D-037、版番号は D-038）である。この承認と版番号統一は、2026-10-13時点の取得検証未実施を実施済みへ変えない。
12. 中央Governanceの正式導入は別工程である。今回の判断履歴管理規則の改訂では開始しない。導入完了、Purpose、Governance Status は確定しない。
13. 検証用Personaについて、反復検証、日別評価、期間集計を継続する。2026-10-14分の原文保全は完了している。回答内容の正確性評価は未実施である。
14. 保全した原文の独立バックアップを用意する。バックアップ先のパスと方式は未決定であり、この記録では確定しない。
15. 共通仕様の Version 3.0 は移行先の基点である。2026-10-16の D-038 で、Reference の5件（ChatGPT、Claude、Cursor、Gemini、検証用）の Document Info を Version 3.0 / Approved とした。これは版番号の統一であり、共通仕様の全機能を本文へ移行した完了ではない。`GEM_` で始まる Education 6件は、現在の数値 Version / Approved を維持し、大改修の完了後に Version 3.0 へ揃える。Version 2.0 は共通基点として採用せず欠番とする。過去の 2.x 履歴は消さない。この版番号統一を理由に、D-037 の承認と既存Evidenceを再検証へ戻さない。D-005の検証用Persona Version 0.1 / Draft は、当時の確定状態として維持する。
16. ChatGPT Persona の現行版は Version 3.0 / Approved（承認は D-037、版番号は D-038）である。D-025 の TC-01〜TC-03、各2回、6回すべてPASSは、この承認および版番号統一とは別の技術条件として未達のまま残す。再試験は今回の承認と版番号統一では開始しない。適用状態が UNVERIFIED のまま PASS としない。Cursorから ChatGPT Project を直接操作できないため、適用状態の確認と6回の実施は User の操作が必要である。第11章の是正、共通仕様第16章の復元、および D-027 の重複整理は、この6回の実施とPASSを含まない。重複整理のローカル反映後は、追加の設計工程を作らず、この実動検証へ戻る。ファイル全体の7,500文字は設計目標値であり、超過だけを不合格または作業停止としない。有効な規則は削除していない。文字数の状態を、6回の実施またはPASSと扱わない。将来の検証対象範囲の詳細基準は、この工程では確定しない。D-005 で未確定の独立バックアップ先・方式、質問セット、実施頻度は、この工程で確定しない。条件の承認を、検証完了または Approved 昇格と扱わない。先の18回答は commit `86b3537dfb8c2eacca851763c00055500ee122bd` にある。従来ChatGPT Projectの 6/6 は参考履歴である。正規比較は、D-032 のとおり ChatGPT検証専用Project 4/6、Claude Project 2/6、Gemini Gem 3/6、合計 9/18 である。4/6 は6回すべてPASSを満たさない。適用状態は UNVERIFIED のままである。4/6 を検証合格へ変えず、D-037 の承認を D-025 の合格と混同しない。再テスト記録の commit と push は未実施である。
17. Claude Persona の現行ファイルは Version 3.0 / Approved（承認は D-037、版番号は D-038）である。現行の Version 3.0 / Approved はローカルの未commit・未pushである。commit `a908abaf46b0a4bbd8b37c16cf0efdb2ab69fe62` が `main` へ push 済みとして保存したのは、承認前の Version 1.5（提案）/ Draft である。D-003 の Version 1.4 / Approved は当時の履歴である。現行版は Version 3.0 / Approved（承認は D-037、版番号は D-038）である。第15章の追加、重複整理、第13章の短縮、`Decision & Rationale` の D-034 への移管、Project登録対象の8,000文字以内への整理（D-035）は、承認前の commit `a908abaf46b0a4bbd8b37c16cf0efdb2ab69fe62`（Version 1.5（提案）/ Draft）に含まれている。現行の Version 3.0 / Approved はその commit に含まれない。G方式用指示文は作成済みである。Claudeによる取得成功は自己申告であり、客観的なGitHubアクセスの確認ではない。Userによる指示文と検証回答の視認評価は問題なしである。独立レビューは条件付き合格である。検証回答の原文は未取得であり、保存済みとして扱わない。User最終承認は D-037 のまま有効である。版番号は D-038 で 3.0 とした。この承認と版番号統一は技術的検証結果の合否を変えない。Gemini Personaの機能の大改修は今回の対象外である。Gemini の版番号は D-038 で 3.0 とした。

Reviewerを含むPersonaの機能設計はEvidenceなしに再検討しない。完了済みの文書適合性復旧を、Evidenceなしに再作業対象へ戻さない。`ASKME 迎合禁止` と7文書配置を未決事項へ戻さない。Education用の基本体系は4役割である。従来の4Gem＋1と `Researcher Deep Research` は履歴として維持する。Researcherの3完成版は、当面User（生徒）が調査範囲に応じて1版を明示選択する。

## 正本の所在

- 作業規則：`AGENTS.md`
- Persona識別と検証：`personas/PERSONA_IDENTIFICATION_AND_SETUP.md`（旧ファイル名を維持）
- Repository入口・Persona重要性の共通説明：`README.md`
- カスタム指示・Persona・プロンプトの詳細比較とPersonaあり／なしの検証詳細：`personas/WHY_PERSONA_MATTERS.md`（文書ID・独立Versionは未決）
- Education Persona：`personas/education/`
- Education Solution Partner正本：`personas/education/GEM_SOLUTION_PARTNER.md`
- Education Code Generator正本：`personas/education/GEM_CODE_GENERATOR.md`
- Education Reviewer正本：`personas/education/GEM_REVIEWER.md`
- Education入口：`personas/education/README.md`
- Reference Persona：`personas/reference/`
- ChatGPT Persona の識別・取得・更新検証：`personas/reference/CHATGPT_PERSONA.md` 第11章（Version 3.0 / Approved（承認は D-037、版番号は D-038）。Verification Code は未確定。品質検証の独立工程は `personas/PERSONA_IDENTIFICATION_AND_SETUP.md` 第16章。正規比較は D-032 の 9/18。適用状態は UNVERIFIED。この承認は 9/18 と 4/6 を変えない）
- Claude Persona の識別・取得・更新検証：`personas/reference/CLAUDE_PERSONA.md` 第15章（Version 3.0 / Approved（承認は D-037、版番号は D-038）。現行の Version 3.0 / Approved はローカルの未commit・未pushである。commit `a908abaf46b0a4bbd8b37c16cf0efdb2ab69fe62` が `main` へ push 済みとして保存したのは、承認前の Version 1.5（提案）/ Draft である。Project登録対象は末尾改行を含めて7,925文字。D-003 の Version 1.4 / Approved は当時の履歴である。Persona ID は `M-CL`。Verification Code は未確定。2026-08-27の判断原文は `project-notes/DECISIONS.md` の D-034。8,000文字の整理は D-035。品質検証の独立工程は `personas/PERSONA_IDENTIFICATION_AND_SETUP.md` 第16章。G方式の取得成功は自己申告。Userの視認評価は問題なし。独立レビューは条件付き合格。この承認は技術的検証結果の合否を変えない）
- Reference入口：`personas/reference/README.md`
- 検証用Persona：`personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md`（Version 3.0 / Approved（承認は D-037、版番号は D-038）。中核4種のSSOTではない）
- 検証記録：`project-notes/persona-validation/`（原文は `raw/`、日別評価は `assessments/`、期間集計は `SUMMARY.md`。2026-10-14は検証用Persona、2026-10-15は ChatGPT Persona の D-025 記録。正規比較は D-032。2026-10-16は Claude Persona の独立レビュー原文1件。検証回答の原文は未取得）
- Reference AI運用実践例：`personas/reference/PERSONA_OPERATION_CASE_STUDY.md`
- Reference Chat Handoff Template：`personas/reference/CHAT_HANDOFF_TEMPLATE.md`
- Reference Prompt Template：`personas/reference/PERSONA_PROMPT_TEMPLATE.md`
- Reference AI運用資料判断履歴：`project-notes/2026-09-23-persona-operation-case-study-decisions.md`
- 判断履歴の所在：適用前の旧判断は、各成果物MDの `Decision & Rationale`、既存の判断履歴ファイル、`AGENTS.md` 末尾に残す。適用後の新判断は `project-notes/DECISIONS.md`。判断理由の本文は本ファイルに書かない。旧判断の所在の例は、Education Reviewer が `project-notes/GEM_REVIEWER_DECISIONS.md`、Researcher系が `project-notes/RESEARCHER_PERSONA_DECISIONS.md`、ルートREADMEが `project-notes/README_DECISIONS.md`。
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
4. 仕様・責務・構造・運用方針を変更する場合だけ、`project-notes/DECISIONS.md` の関連エントリを読む。全文は無条件に読まない。軽微な変更では判断履歴の確認を要求しない。
5. `AGENTS.md` の `Decision & Rationale`（Solution Partner Version 1.1〜1.3および Version 1.5、Code Generator Version 2.2の判断履歴を含む）
6. `project-notes/2026-09-01-solution-partner-unresolved-items-decisions.md`（Solution Partner Version 1.4の未決事項運用Decision Evidence）
7. 必要時のみ `project-notes/YYYY-MM-DD-*.md`（2026-08-23より前の履歴）

## REFERENCES

- `AGENTS.md`
- `personas/education/GEM_SOLUTION_PARTNER.md`
- `personas/education/GEM_REVIEWER.md`
- `personas/PERSONA_IDENTIFICATION_AND_SETUP.md`
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
