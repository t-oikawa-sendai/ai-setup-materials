# DECISIONS（判断履歴）

<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | ASM-DECISIONS-001 |
| Version（バージョン） | 1.0 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-10-13 |
| Last Updated（最終更新日） | 2026-10-14 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | AGENTS.md / project-notes/CURRENT.md |

## Purpose（目的）

本規則の適用後に発生する新たな判断を記録する。
既存判断履歴は従来の保存場所で保全する。
本書はPersona・README等の本文の正本を代替しない。

## D-001 Preserve Existing Decisions and Record New Decisions Centrally（既存判断の保全と新規判断の共通記録）

Date（日付）: 2026-10-13
Related Documents（関連文書）: AGENTS.md / project-notes/CURRENT.md / Repository全体

Decision（決定）:
- 既存判断履歴は原文と保存場所を維持する。移行を義務化しない。
- 新たに§5.5に該当する判断のみ、本ファイルへ記録する。
- 過去の記録と新規記録の併存を認める。過去記録は必要時のみ参照する。
- 既存判断は、後続の有効なDecisionで明示的に上書きされた部分を除き、引き続き有効とする。
- 判断履歴の保全と追跡可能性を優先し、無関係な通常業務を妨げない。
- commit は、Userが commit を明示したときだけ行う。push は、Userが push を明示したときだけ行う。各操作の実施条件は、その操作に対する明示指示があることである。対象成果物MDと本ファイルへのローカル反映は、commit と push を含まない。
- 本改訂は、中央Governanceの正式導入に先行する User 決定である。
- 中央統制の基本原則、既存判断の効力、Repository の分類値は変更しない。
- 正式導入は別工程とし、本改訂を導入完了としない。
- 本改訂の正本反映が完了した事実は `project-notes/CURRENT.md` の完了事項に記録する。同じ完了を作業中へ重複記載しない。

Rationale（理由）:
既存記録の移動による影響・欠落・混乱を避け、今後の判断を確実に追跡できるようにするため。
過去の判断履歴の検索頻度は低く、現時点で全面移行の費用対効果は低いとのUserの運用実態による。

Supersedes（上書き対象・範囲）:
- AGENTS.md / 2026-08-23 / 「文書管理ルール（正本・決定反映・CURRENT.mdの役割）」：判断を同じ成果物MDへ追記する運用部分、およびUserの明示指示なしにGitHubへ保存してから次工程へ進む義務の部分のみ
- AGENTS.md / 2026-09-01 / 「User承認範囲の厳守と決定事項の即時記録」：Userの明示指示なしにGitHubへ保存する義務の部分のみ。User承認範囲の厳守と対象成果物MDへの即時反映は維持する
- AGENTS.md / 2026-09-11 / 「Root READMEのDecision & Rationale分離」：新判断の文書別管理方式部分
- AGENTS.md / 2026-09-11 / 「生徒・利用者向け公開文書のDecision & Rationale分離」：新判断の文書別管理方式部分
- AGENTS.md §5.4：同一ファイル追記と、公開・教材向け文書の分離例外として新判断の記録先を分ける現行規則部分
- AGENTS.md / 2026-09-11の各Rejected：「一律分離を禁止する」として新規判断の共通記録まで禁止する解釈部分のみ。過去のRejected記録自体は保持する
- AGENTS.md / 2026-09-13 / 「Education Solution Partnerを Version 1.5へ正式改版」：「判断履歴は本ファイルへ記録する」の新規記録先部分のみ
- AGENTS.md / 2026-09-13 / 「Education Code Generatorを Version 2.2へ更新し、Solution Partner v1.5の補足A 3区分へ整合」：同上の新規記録先部分のみ
- AGENTS.md / 2026-10-06 / 「決定の保留と仮定の実装利用許可を分離」：判断履歴の記録先を定める部分のみ
- AGENTS.md / 2026-10-07 / 「対象Repository省略の是正対象を記録」：「既定の判断履歴」の記録先部分のみ
- AGENTS.md §2.2・§3・§3.2・§3.3・§4・§5.1・§5.2・§5.7・§6・§7・§8：判断履歴の記録先・参照先を定める部分のみ
- AGENTS.md §3.1 第9項：明示指示なしに GitHub へ保存する義務だけ
- AGENTS.md §5.1：流れの GitHub保存段にある、明示指示なしに GitHub へ保存する義務だけ

Non-Changes（非変更範囲）:
既存の判断履歴原文・保存先、個々のPersona・README本文、§5.5、§5.6、外部AIサービスへの登録内容。
上記で上書き範囲を明示していない既存判断の効力。
2026-10-12の ReadOK / ReadNG / ReadUndefine 報告規則の全範囲。
2026-10-07の是正対象、予定範囲、適用条件。是正作業は未完了のまま維持する。
2026-09-13の Solution Partner 1.5 と Code Generator 2.2 の機能上の決定。
2026-10-06の、保留と実装利用許可を分離する機能上の決定。
本Repositoryの Purpose、Governance Status、その他の分類値。
中央統制の基本原則。中央Governanceの正式導入は未了であり、本改訂は導入完了ではない。

Rejected（不採用案）:
- 既存判断を含む全件を本ファイルへ移し、移動元を削除する方式
- 旧保存先と新規記録の併存を禁止する方式
- AGENTS.md 末尾の旧履歴を全件移行する方式
- CHANGELOG の不存在を、本判断の是正へ抱き合わせる方式

## D-002 Limit the Git Sync Gate to Local Changes（Git同期ゲートをローカル変更へ限定）

Date（日付）: 2026-10-13
Related Documents（関連文書）: AGENTS.md / project-notes/CURRENT.md / Repository全体

Decision（決定）:
- Repositoryに関する作業は、読取専用とローカル変更に分ける。ファイルの追加、編集、削除、commit、pushを行わない作業を読取専用とする。これらを行う作業をローカル変更とする。
- 読取専用の作業では、ローカルGit同期ゲートを要求しない。作業報告には、読み取ったRepository、branch、commit SHAを含める。SHAを確認できない場合は未確認と報告し、確認済みと偽らない。
- ローカル変更作業には、従来の同期ゲートの手順と停止条件を適用する。未commit変更を破棄・退避・上書きして同期を強行しない。
- 読取専用の作業からローカル変更へ移行する場合は、変更前に同期ゲートを実施する。
- この決定は、リモート読取、ローカル読取、ローカル変更の3分類へ拡張しない。
- D-001は改変しない。GOV-01その他の未承認是正は、この決定に含めない。

Rationale（理由）:
ローカルRepositoryを持たない読取にローカル同期ゲートを要求すると、読取が毎回停止するか、停止条件を無視する運用になるため。Userが承認したASKME-01のA案を、ローカル変更の既存ゲートを維持したまま反映する。

Supersedes（上書き対象・範囲）:
- AGENTS.md §2.1：Repositoryに関する作業のすべてにローカルGit同期ゲートを要求する部分のみ。ローカル変更作業の手順、停止条件、未commit変更を破棄・退避・上書きしない規定は維持する
- AGENTS.md §2.2：文書確認を「Git同期ゲート通過後」に限るという、読取専用作業への適用部分のみ
- AGENTS.md §8：「Git同期ゲートを通過せずにRepository作業を開始しない」のうち、読取専用作業へ適用する部分のみ

Non-Changes（非変更範囲）:
ローカル変更作業の5手順と停止条件。未commit変更の破棄・退避・上書き禁止。2026-10-12の ReadOK / ReadNG / ReadUndefine 報告規則。D-001の全文。Persona、README、設定資料。GOV-01その他の未承認是正。

Rejected（不採用案）:
- 読取専用の作業にもローカルGit同期ゲートを要求し、満たせなければ作業を開始しない方式
- リモート読取、ローカル読取、ローカル変更の3分類へ拡張する方式

## D-003 Record Claude Reference Persona as Version 1.4（Claude Reference Personaを Version 1.4 として記録）

Date（日付）: 2026-10-13
Related Documents（関連文書）: personas/reference/CLAUDE_PERSONA.md / project-notes/CURRENT.md

Decision（決定）:
- `personas/reference/CLAUDE_PERSONA.md` の Document Info を、Version 1.4、Status Approved、Last Updated 2026-10-13 とする。
- Persona本文は変更しない。
- GOV-07その他の未承認変更は、この決定に含めない。
- D-001とD-002は改変しない。
- この反映はローカルのみとし、commit と push を含まない。

Rationale（理由）:
2026-10-12に本文へ読込状態の一行報告を追加した後も、Document Info は Version 1.3、Last Updated 2026-08-27 のままだった。Userは本文を変えず、Document Info を Version 1.4 / Approved / Last Updated 2026-10-13 とすることを決定した。

Supersedes（上書き対象・範囲）:
- project-notes/CURRENT.md の作業中にある、Claude の現行版を Version 1.3 / Approved とし、2026-10-12の追加は Approved へ昇格していないとする現在地点のみ。2026-10-12の ReadOK / ReadNG / ReadUndefine 報告規則は維持する

Non-Changes（非変更範囲）:
Persona本文。Created Date。ChatGPT と Cursor の Version と Status。2026-10-12の報告規則、責務、動作、報告構成。GOV-07。D-001。D-002。既存の `Decision & Rationale`。

Rejected（不採用案）:
- Version 1.3 のままにする方式
- Version 1.4 を Draft とする方式

## D-004 Align Reference Operation Materials with D-001 and D-002（Reference運用資料のD-001・D-002整合是正）

Date（日付）: 2026-10-13
Related Documents（関連文書）: AGENTS.md / personas/reference/CHAT_HANDOFF_TEMPLATE.md / personas/reference/PERSONA_OPERATION_CASE_STUDY.md / project-notes/CURRENT.md / project-notes/2026-09-23-persona-operation-case-study-decisions.md

Decision（決定）:
- GOV-09で確認されたD-002の適用漏れを、Reference AI運用資料3文書の既定レビュー工程と統合して是正する。
- ローカル変更作業を別端末で再開する場合は、`AGENTS.md` §2.1のGit同期ゲートを適用する。読取専用作業にローカルpullを要求しない。未commit変更の破棄・退避・上書きは禁止する。§2.1の手順と停止条件は変更しない。
- Handoffの初期化は作業種別で分ける。読取専用はRepository、branch、取得したcommit SHAを確認する。SHAを確認できない場合は未確認と報告する。読取専用ではLocal Workspace、Local HEAD、worktreeの確認を必須とせず、ローカルGit状態が未確認であることだけを理由に停止しない。ローカル変更は、対象Repositoryの作業規則に定義されたGit同期ゲートを実施する。Initialization Evidenceの必須項目は作業種別で分ける。ローカル状態に関する停止条件はローカル変更作業に限定する。VERIFIED / UNVERIFIED / ASSUMPTIONは維持する。
- Case Studyの成果管理は、O講師が成果内容を判断し、確定内容を対象成果物MDへローカル反映し、記録基準に該当する新しい判断を `project-notes/DECISIONS.md` へ記録し、`CURRENT.md` の現在地点を更新し、commit は User が commit を明示したときだけ行い、push は User が push を明示したときだけ行い、必要に応じてHandoffを作成する順序とする。
- 現行版は、Case Study Version 0.2 / Draft、Handoff Template Version 0.3 / Draft、Prompt Template Version 0.2 / Draft とする。VersionとStatusは昇格しない。
- `PERSONA_PROMPT_TEMPLATE.md` は変更しない。BRIDGE、簡易版、文書間導線は維持する。
- D-001、D-002、D-003は改変しない。GOV-01は再検討しない。2026-10-07の対象Repository省略是正は未完了のまま維持し、この決定をもって是正完了としない。
- この反映はローカルのみとし、commit と push を含まない。

Rationale（理由）:
D-002は読取専用にローカルGit同期を要求しないと定めた。一方、`AGENTS.md` §6の別端末再開、Handoffの初期化と停止条件、Case Studyの成果管理順序は、読取専用を含む作業へローカル同期、またはGitHub反映を先にする文面のままだった。3文書の既定レビュー工程の中で、その適用漏れを是正する。

Supersedes（上書き対象・範囲）:
- AGENTS.md §6：「別端末で再開する場合は、作業開始前に最新状態を pull する」のうち、読取専用作業を含む再開にローカルpullを要求する部分のみ。未commit変更の破棄・退避・上書き禁止は維持する
- project-notes/2026-09-23-persona-operation-case-study-decisions.md / 2026-09-23 / 「Handoff TemplateへRepository再開手順とEvidence管理を復旧」：作業開始前のGit同期、および Local Workspace / Local HEAD / Worktree の確認を、読取専用を含む再開全般の必須とする部分のみ。VERIFIED / UNVERIFIED / ASSUMPTION、正本確認、検証、完了報告は維持する
- personas/reference/PERSONA_OPERATION_CASE_STUDY.md §13：成果管理を「確定した成果をGitHubへ反映」の後にDecisionと現在地点の更新を置く順序のみ

Non-Changes（非変更範囲）:
D-001、D-002、D-003の全文。`AGENTS.md` §2.1のローカル変更手順と停止条件。VERIFIED / UNVERIFIED / ASSUMPTION。Handoffの既存引き継ぎ項目、正本確認、検証、完了報告。Case Studyの目的、O講師の表記、責務分離。BRIDGE、簡易版、文書間導線。`PERSONA_PROMPT_TEMPLATE.md` の全文。各文書の Version と Status Draft。GOV-01。2026-09-23の過去Decision本文。GOV-05に関連する過去の完了記録。2026-10-07の対象Repository省略是正の未完了。Persona本文。

Rejected（不採用案）:
- 読取専用作業にもローカルpullまたはローカルGit同期ゲートを要求し、ローカルGit状態が未確認なら停止する方式
- 未commit変更を破棄・退避・上書きして同期する方式
- 成果を先にGitHubへ反映してから、対象成果物MD、Decision、現在地点を更新する方式
- この是正に合わせてDraftをApprovedへ昇格し、またはVersionを上げる方式
- 2026-10-07の対象Repository省略是正を、この是正と一括で完了とする方式
- GOV-01を再検討する方式

## D-005 Preserve Persona Validation Records Separately（Persona検証記録の分離保全）

Date（日付）: 2026-10-14
Related Documents（関連文書）: project-notes/persona-validation/README.md / project-notes/persona-validation/SUMMARY.md / project-notes/persona-validation/assessments/2026-10-14.md / project-notes/persona-validation/raw/ / project-notes/CURRENT.md

Decision（決定）:
- 検証記録の保存先は `project-notes/persona-validation/` とする。
- 原文、評価、総合集計を分離する。原文は `raw/`、日別評価は `assessments/`、期間集計は `SUMMARY.md` とする。
- 原文は無改変で保全する。改行、空白、文字参照、表記、バックスラッシュを変更しない。SHA-256で照合する。
- GitHubの履歴管理と、それとは独立したバックアップを併用する。
- 検証は数日〜数週間継続する。1回の回答で優劣や順位を最終結論にしない。
- 未確定の実行条件やバックアップ先を推測して記録しない。バックアップ先のパスと方式、質問セット、実施頻度は未決定のままとする。
- 検証用Persona `personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md` は Version 0.1 / Draft のまま維持する。
- 各AIの「GitHub読込済／未読込」は自己申告として扱い、技術的な取得証跡がない実際のGitHubアクセスはUNVERIFIEDとする。
- D-001、D-002、D-003、D-004は改変しない。
- この反映はローカルのみとし、commit と push を含まない。

Rationale（理由）:
評価基準が後から変わっても提出された原文へ戻れるようにするため。応答の揺らぎを単回の比較で確定しないため。公開Repositoryの履歴だけに保全を依存しないため。

Supersedes（上書き対象・範囲）:
なし。`project-notes/CURRENT.md` にある2026-10-13時点の「ChatGPT Project上の取得検証は未実施」は、当時の状態の記録として維持する。この決定で削除しない。

Non-Changes（非変更範囲）:
D-001、D-002、D-003、D-004の全文。検証用Personaの本文、Version、Status。他案件の完了事項、作業中、次工程。バックアップ先の具体パス。質問セットと実施頻度。commit と push の実施。

## D-006 Unify Persona IDs and the Response Identification Format（Persona IDと識別表示形式の統一）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / Repository全体

Decision（決定）:
- 回答冒頭の識別表示を、`【サービス略号/モデル名｜Persona ID@Version｜状態】` の1行に統一する。
- 旧形式 `【Persona：GitHub読込済｜Version：0.1】` との二重表示はしない。
- モデル名は確認できた値のみ使う。確認できない値は `?` とする。
- Persona IDとVersionは、実際に使用するPersona本文と照合する。推測で補完しない。
- 形式例 `【CG/GPT-6｜M-CG@3.0｜G】` は記号の並びを示す。例示のモデル名と `@3.0` は、現行本文がすでにその値であることを意味しない。
- 正本は `personas/PERSONA_IDENTIFICATION_AND_SETUP.md` とする。
- D-001〜D-005は改変しない。この反映はローカルのみとし、commit と push を含まない。

Rationale（理由）:
使用中のサービス、モデル、Persona、Version、取得状態を、回答の冒頭で一つの形式に示すため。確認できない値を推測で埋めないため。

Supersedes（上書き対象・範囲）:
なし。今後の識別表示の正本は本決定の形式とする。`personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md` 本文に残る旧形式の指示、および `project-notes/persona-validation/raw/` の検証原文は、この決定では変更しない。

Non-Changes（非変更範囲）:
D-001〜D-005の全文。既存11 Personaの本文、Version、Status、Document ID。検証原文とSHA-256。サービス略号は D-010、取得状態の旗は D-011、Version 3.0 の移行方針は D-009。移行は未実施である。

Rejected（不採用案）:
- 旧形式と新形式を同じ回答に二重表示する方式
- モデル名またはVersionを推測で補完する方式

## D-007 Define M/S/T Classification and Official Names（M/S/T分類と正式名称）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / Repository全体

Decision（決定）:
- Prefix `M-` は Main、基本版とする。
- Prefix `S-` は Subset、機能限定版とする。`S-` の正式な日本語名称は「機能限定版」である。
- Prefix `T-` は Test、検証版とする。
- 「教育用」は対象者・用途の説明であり、Persona分類名ではない。
- Subsetを厳密な機能包含関係で定義しない。
- MainとSubsetの1対1対応表を必須にしない。
- M/S/T はPersona分類である。取得状態の G/P/N/? とは別の識別軸とする。
- D-001〜D-006は改変しない。

Rationale（理由）:
Personaの基本版、機能限定版、検証版をPrefixで区別し、対象者の説明を分類名と混同しないため。Subsetを包含関係や1対1対応に固定しないため。

Supersedes（上書き対象・範囲）:
なし。

Non-Changes（非変更範囲）:
D-001〜D-006の全文。既存Document ID。`education/` と `reference/` の配置。既存11 Personaの本文。利用者制限の詳細は D-012。

Rejected（不採用案）:
- `S-` の分類名を「教育用」とする方式
- Subsetを厳密な機能包含関係で定義する方式
- MainとSubsetの1対1対応表を必須とする方式

## D-008 Assign the Eleven Persona IDs（全11 Persona ID）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / personas/reference/CHATGPT_PERSONA.md / personas/reference/GEMINI_PERSONA.md / personas/reference/CLAUDE_PERSONA.md / personas/reference/CURSOR_PERSONA.md / personas/education/GEM_RESEARCHER_FULL.md / personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md / personas/education/GEM_RESEARCHER_DEVELOPMENT.md / personas/education/GEM_SOLUTION_PARTNER.md / personas/education/GEM_CODE_GENERATOR.md / personas/education/GEM_REVIEWER.md / personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md

Decision（決定）:
- 次の11 IDを確定し、再命名・再提案しない。
  - `personas/reference/CHATGPT_PERSONA.md`：M-CG
  - `personas/reference/GEMINI_PERSONA.md`：M-GM
  - `personas/reference/CLAUDE_PERSONA.md`：M-CL
  - `personas/reference/CURSOR_PERSONA.md`：M-CU
  - `personas/education/GEM_RESEARCHER_FULL.md`：S-R-FULL
  - `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`：S-R-LD
  - `personas/education/GEM_RESEARCHER_DEVELOPMENT.md`：S-R-DEV
  - `personas/education/GEM_SOLUTION_PARTNER.md`：S-SP
  - `personas/education/GEM_CODE_GENERATOR.md`：S-CG
  - `personas/education/GEM_REVIEWER.md`：S-RV
  - `personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md`：T-IT-ADVISOR
- `Researcher Deep Research` は独立Personaではなく、11件に含めない。
- 既存Document IDは変更しない。
- 検証用Persona本文に残る移行前の識別子 `IT-GENERAL-ADVISOR-TEST` は、今回の本文未変更により残す。確定ID `T-IT-ADVISOR` へ置き換わったものとして扱わない。
- D-001〜D-007は改変しない。Persona本文は変更しない。

Rationale（理由）:
全Personaを一意のIDで参照し、ファイルとの対応を固定するため。独立Personaではない追加GemをID対象へ混ぜないため。

Supersedes（上書き対象・範囲）:
なし。検証用Persona本文中の `IT-GENERAL-ADVISOR-TEST` は、本文更新の別工程まで現行本文上の識別子として残る。D-005が保全した Version 0.1 / Draft は変更しない。

Non-Changes（非変更範囲）:
D-001〜D-007の全文。既存11 Personaの本文、Version、Status、Document ID。`S-SETUP` は本決定のIDに含めない。

Rejected（不採用案）:
- 確定済みIDを再命名・再提案する方式
- `Researcher Deep Research` を12件目の独立Personaとする方式
- 既存Document IDをPersona IDへ置き換える方式

## D-009 Adopt Version 3.0 as the Migration Baseline Without Applying It（Version 3.0への移行方針）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / project-notes/DECISIONS.md / project-notes/CURRENT.md / Repository全体

Decision（決定）:
- 全11 Personaを、新共通基準のVersion 3.0 へ統一する。
- 共通基準としてVersion 2.0を採用しない。Version 3.0を新しい基点とする。
- 旧2.x系列の過去履歴を削除・書き換えしない。
- 既存のDraft・Approvedを、Version変更だけで自動昇格しない。
- 今回行うのは移行仕様の記録である。全Persona本文とDocument Infoの Version 3.0 への更新は別工程であり、未実施である。
- 移行前のVersionは、2026-10-14時点の各Document Infoである。移行後の共通Versionは 3.0 である。両者を混同しない。
- D-005が記録した検証用Persona Version 0.1 / Draft は、2026-10-14の保全決定時点の確定状態として維持する。Version 3.0 はその後の移行先であり、D-005を書き換えない。移行未実施のため、現行Document Infoは Version 0.1 / Draft のままである。
- D-001〜D-008は改変しない。

Rationale（理由）:
共通のVersion基点を 3.0 に置き、2.0 をその基点にしないため。過去の版履歴を残したまま、本文更新を別工程に分けるため。Versionの数字だけを変えて承認状態を上げないため。

Supersedes（上書き対象・範囲）:
なし。D-005の Version 0.1 / Draft は当時の確定状態として有効なままである。本決定は、未実施の移行先を追加するものであり、D-005の時点のVersionを現行値へ書き換えない。

Non-Changes（非変更範囲）:
D-001〜D-008の全文。既存11 Personaの本文、現行Document InfoのVersionとStatus、Document ID。検証原文。新設Personaへの Version 3.0 の無条件適用とApproved昇格。

Rejected（不採用案）:
- Version 2.0を新共通基準とする方式
- 旧2.x系列の過去履歴を削除または書き換える方式
- Version変更だけでDraftまたはApprovedを自動昇格する方式
- 移行仕様の記録と、本文・Document Infoの更新完了を同じものとして扱う方式

## D-010 Keep AI Services and Personas Independent（AIサービスとPersonaの独立性）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / Repository全体

Decision（決定）:
- サービス略号を、Gemini＝GM、ChatGPT＝CG、Claude＝CL、Cursor＝CU、M365 Copilot＝MC とする。
- M365 Copilotは、現段階で専用Personaを追加しない。略号のみ定義する。
- AIサービスとPersonaは独立する。ClaudeのProjectで `S-SP` を使用できるよう案内する。`M-CG` はChatGPT専用の実行制限を意味しない。
- AIサービスの種類によってPersonaの役割を限定しない。
- D-001〜D-009は改変しない。

Rationale（理由）:
識別表示のサービス略号を固定しつつ、Personaの使用先を作成元のサービス名へ縛らないため。略号の定義と、専用Personaの追加を分けておくため。

Supersedes（上書き対象・範囲）:
なし。

Non-Changes（非変更範囲）:
D-001〜D-009の全文。既存11 Personaの本文と配置。M365 Copilot専用Personaの不存在。利用者区分による案内制限は D-012。

Rejected（不採用案）:
- AIサービスの種類でPersonaの役割を限定する方式
- `M-CG` をChatGPTだけで実行できるIDとして扱う方式
- 現段階でM365 Copilot専用Personaを追加する方式

## D-011 Use G/P/N/? as the Only Acquisition Status Flags（G/P/N/?状態表示への一本化）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / project-notes/DECISIONS.md / Repository全体

Decision（決定）:
- 取得状態は次の4旗だけとする。GはGitHubからPersona本文を取得した状態、PはProject等の指示欄に記載されたPersona本文を使用する状態、NはPersona未読込、`?` は取得元・状態が未確認である。
- 以前の提案 `G!` は採用しない。
- GitHub取得失敗と未実施の詳細は、必要に応じて検証記録で区別する。
- Gは取得成功の自己申告であり、客観的なアクセス証明ではない。
- Persona取得とPersona適用は別の事実として扱う。
- GitHub取得失敗時に、Memoryや過去の会話から本文を補完しない。
- 未取得を取得済みと報告しない。
- D-005の、技術的な取得証跡がない実際のGitHubアクセスはUNVERIFIEDとする扱いは維持する。
- D-001〜D-010は改変しない。検証原文は変更しない。

Rationale（理由）:
取得状態を一つの旗の集合にまとめ、取得成功の自己申告をアクセス証明と混同しないため。失敗時に記憶から本文を補完しないため。

Supersedes（上書き対象・範囲）:
なし。今後の状態表示は本決定の4旗とする。D-005の自己申告とUNVERIFIEDの扱いは維持する。検証原文の「GitHub読込済」という過去の表記は改変しない。

Non-Changes（非変更範囲）:
D-001〜D-010の全文。M/S/T分類。検証原文とSHA-256。既存11 Personaの本文。

Rejected（不採用案）:
- `G!` を採用する方式
- Gを客観的なアクセス証明として扱う方式
- GitHub取得失敗時にMemoryや過去の会話から本文を補完する方式
- 未取得を取得済みと報告する方式

## D-012 Limit Main to the Owner and Subset to General Users（MainのOwner専用とSubsetの一般利用）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / Repository全体

Decision（決定）:
- Main（M-）はOwner専用とする。
- 生徒およびその他の一般利用者には、Subset（S-）のみを通常の設定候補として案内する。
- 一般利用者にMainを選択肢として提示しない。
- Test（T-）は検証用途とし、通常の設定候補へ含めない。
- 使用者の権限を確認できない場合は、一般利用者扱いとする。
- この制限はPersona設定案内上の規則であり、GitHubの実際のアクセス制御ではない。M-Personaのアクセス禁止を技術的に保証したと記録しない。
- 案内してよいPersonaの範囲は使用者の区分で決まる。使用するAIサービスでは決まらない。
- D-001〜D-011は改変しない。

Rationale（理由）:
基本版の案内先をOwnerに限る一方、その制限をGitHub上のアクセス禁止の実装済み事実として記録しないため。権限を確認できない使用者を、Mainの案内対象へ広げないため。

Supersedes（上書き対象・範囲）:
なし。

Non-Changes（非変更範囲）:
D-001〜D-011の全文。GitHubのアクセス制御設定。既存11 Personaの本文と公開範囲。AIサービスとPersonaの独立性。

Rejected（不採用案）:
- 一般利用者へMainを通常の選択肢として提示する方式
- Testを通常の設定候補へ含める方式
- 案内上の制限を、GitHubアクセス制御の技術的保証として記録する方式

## D-013 Keep the education and reference Directories（education/ と reference/ の維持）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / personas/education/ / personas/reference/ / Repository全体

Decision（決定）:
- `education/` と `reference/` のディレクトリ構造を維持する。
- 既存Document IDを変更しない。
- 識別と設定案内の共通仕様は、両区分に適用する成果物 `personas/PERSONA_IDENTIFICATION_AND_SETUP.md` に置く。
- このファイルはPersona本文ではないため、区分ディレクトリのPersona本体へ置かない。AIサービス固有の手順ではないため、`personas/<区分>/setup/` へ置かない。
- 新しいディレクトリは作らない。
- D-001〜D-012は改変しない。既存ファイルの移動・改名はしない。

Rationale（理由）:
既存の区分とDocument IDを維持したまま、両区分にまたがる共通仕様の正本を一か所に置くため。サービス別手順とPersona本文の配置規則を崩さないため。

Supersedes（上書き対象・範囲）:
なし。2026-08-22のディレクトリ構造と、設定・運用資料を `personas/<区分>/setup/` でAIサービス単位に置く既存規則は維持する。

Non-Changes（非変更範囲）:
D-001〜D-012の全文。既存ディレクトリ名。既存Document ID。既存11 Personaの本文と配置。サービス固有セットアップ手順の既存ファイル。

Rejected（不採用案）:
- 共通仕様のために新しいディレクトリを作る方式
- 共通仕様を education または reference の一方だけへ置き、同じ仕様を他方へ複製する方式
- 既存Document IDまたはディレクトリ名を変更する方式

## D-014 Require Management of Completed Instruction Texts（指示欄用完成文章の必須管理）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / AGENTS.md / Repository全体

Decision（決定）:
- 各AIサービスのProject・Gem等の指示欄に直接記載する完成済み文章を、Repositoryの必須管理対象に加える。
- Persona本文と指示欄用文章を区別する。
- GitHub取得方式（G）と直接記載方式（P）に対応する。
- Persona本文は既存正本を使い、独立した編集元を増やさない。
- 利用者に複数資料から指示文を組み立てさせない。そのままコピーできる完成文を提供する。
- 指示文の共通部分とサービス固有部分を識別できるようにする。
- サービスの現行仕様で実現できない機能を保証しない。
- 既存のPersona本文と、サービス固有セットアップ手順の責務分離を維持する。
- 過去に検討した「9パターン」「17パターン」は確定文書数ではない。
- 完成文の生成・管理方式と必要ファイル数は詳細設計の対象であり、未確定である。未確定のまま完成文ファイルを作成しない。
- `AGENTS.md` の対象と文書責務へ、上記の管理対象と区別だけを追記する。過去の `Decision & Rationale` は書き換えない。
- D-001〜D-013は改変しない。

Rationale（理由）:
指示欄へ貼る文章を、利用者の組み立てやPersona本文への混在に依存させないため。サービス固有のセットアップ手順との責務分離を維持したまま、完成文を管理対象へ加えるため。

Supersedes（上書き対象・範囲）:
なし。`AGENTS.md` の既存の対象一覧へ、指示欄用完成文章を追加する。Persona本文とサービス固有セットアップ手順を分ける既存規則は維持する。

Non-Changes（非変更範囲）:
D-001〜D-013の全文。`AGENTS.md` 末尾の既存 `Decision & Rationale`。既存11 Personaの本文。`personas/education/setup/GEMINI_GEM_SETUP.md` と `personas/reference/setup/CLAUDE_CODE_SETUP.md` の本文。完成文ファイルの未作成。

Rejected（不採用案）:
- 「9パターン」または「17パターン」を確定文書数とする方式
- 利用者に複数資料から指示文を組み立てさせる方式
- 指示欄用文章のためにPersona本文の独立した編集元を増やす方式
- サービスの現行仕様で実現できない機能を保証する方式

## D-015 Guide Persona Setup from Natural Language（自然文からのPersona設定案内）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / README.md / personas/education/README.md / personas/reference/README.md / Repository全体

Decision（決定）:
- 利用者はPersona IDを知らなくてもよい。自然文の依頼から、用途、Persona、AIサービス、取得方式を特定し、設定まで案内する。
- 基本順序は、作成目的の理解、利用可能なPersonaの選定、AIサービスの確認、G/P方式の確認、設定手順と指示欄用完成文の提示、動作確認方法の案内である。
- 質問順序を機械的に固定せず、判明している事項は再質問しない。情報不足の場合のみ、必要最小限をASKMEする。
- 一意に判定できるPersonaを再選択させない。一般利用者に M/S を選択させない。同じ質問を繰り返さない。
- 不明なPersona名は、ID対応表と現行Personaから確認する。AIサービスとPersonaの役割を結びつけて候補を制限しない。
- 目的が明確な「GitHubで管理するペルソナを読み込む仕様のSolution Partnerのプロジェクト」は、S-SP かつ取得方式 G と判定する。AIサービスは文脈から特定できる場合は追加質問せず、特定できなければ確認する。
- 目的が不明な「プロジェクトを作りたい」はASKMEする。Userが「PFを作成する設計の相談相手」と答えた場合、一般利用者向け候補は S-SP とする。Userが Claude を選んでも、Claudeを理由に S-SP を除外しない。
- その続きでUserが G方式を選んだ場合、Claude向けに S-SP のGitHub取得用設定手順と指示欄用完成文を提示する。この完成文は未作成であり、例は要求であってファイルの存在を意味しない。
- 設定案内の完了時に、Persona IDと名称、AIサービス、取得方式、作成手順、指示欄へコピーする完成文、動作確認用プロンプトを提供する。実際の適用成功は別途検証する。
- Root README、Education README、Reference READMEには、共通仕様への入口だけを追加する。同じ説明文を複数ファイルへ重複掲載しない。Education用4Gem＋1の構成と利用手順は変更しない。三つのREADMEの Version と Status は変更しない。
- D-001〜D-014は改変しない。

Rationale（理由）:
Persona IDを知らない利用者でも、目的から設定まで案内できるようにするため。判明済みの事項を繰り返し問わず、サービス名で候補を狭めないため。

Supersedes（上書き対象・範囲）:
なし。

Non-Changes（非変更範囲）:
D-001〜D-014の全文。Education用4Gem＋1の構成と利用手順。三つのREADMEの Version、Status、Document ID。既存のサービス固有セットアップ手順の本文。指示欄用完成文ファイルの未作成。実動検証の未実施。

Rejected（不採用案）:
- 質問順序を機械的に固定し、判明済みの事項も再質問する方式
- 一般利用者に M/S を選択させる方式
- AIサービスを理由に、使用できるPersonaの役割を制限する方式
- 同じ説明文をRoot、Education、Referenceの各READMEへ重複掲載する方式

## D-016 Establish a Dedicated Persona for Setup Guidance（設定案内専用Personaの新設方針）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / project-notes/CURRENT.md / Repository全体

Decision（決定）:
- Personaの設定案内だけを担当する専用Personaを新設する。この新設方針は確定である。
- 責務は、Persona利用環境の設定案内、目的からのPersona選定、必要最小限のASKME、Persona IDとGitHub正本の対応確認、G/P方式の選択支援、AIサービス固有の設定手順、指示欄へ貼る完成文、設定後の動作確認方法とする。
- 対象外は、PFやアプリケーションそのものの設計、プログラミング、コード生成、ソフトウェア実装、コードレビュー、一般的なIT相談、Persona本文の無断変更、Git操作の無断実行とする。
- 次はChatGPTの初稿であり、Userの個別承認を受けていない。PROPOSED / UNRESOLVED として保持する。名称案 Persona Setup Advisor、Persona ID案 S-SETUP、新規PersonaのDocument Info、本文の最終構成、正本ファイルの配置先、GitHub取得の具体的な実装方式、共通指示文とサービス別派生文の最終構成、新Personaの実動検証条件。
- `S-SETUP` を承認済みIDとして扱わない。D-008の確定11 IDへ加えない。
- Version 3.0 を新設Personaへ無条件に適用しない。Approvedへ昇格しない。
- 新規Persona本文の正式実装は未実施である。
- 既存11 Personaの役割定義は変更しない。対象外の作業を、本決定で既存Personaへ割り当て直さない。
- D-001〜D-015は改変しない。

Rationale（理由）:
設定案内を、設計・実装・レビュー・一般的なIT相談から分けた専用Personaの責務とするため。未承認の名称とIDを、確定仕様へ混ぜないため。

Supersedes（上書き対象・範囲）:
なし。

Non-Changes（非変更範囲）:
D-001〜D-015の全文。既存11 Personaの本文、Version、Status、Document ID、責務。確定11 ID。`S-SETUP` の未承認。新設Persona本文の未作成。実動検証の未実施。

Rejected（不採用案）:
- 名称案または `S-SETUP` を承認済みとして記録する方式
- Version 3.0 を新設Personaへ無条件に適用し、Approvedへ昇格する方式
- 新設方針の記録と、本文の正式実装完了を同じものとして扱う方式

## D-017 Change the Main Usage Rule from Owner-only to a Recommendation by Capability（M-のOwner専用規則を能力に応じた推奨基準へ変更）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / project-notes/CURRENT.md / Repository全体

Decision（決定）:
- Main（M-）は、Ownerおよび同等の知識・運用能力を持つUserを主な対象とする。
- M-は管理・設定条件が厳しい。必要な設定ファイル等が存在しなければ、AIが停止する場合がある。
- Subset（S-）は、初心者へ推奨する機能限定版とする。
- Owner以外によるM-の利用を禁止しない。
- 初心者が推奨に従わずM-を選ぶことも認める。
- 利用者は、必要な前提条件を満たさない場合に、機能制限、動作停止、操作性低下が起こり得ることを理解したうえで利用する。
- 利用経験による本人認証、およびアクセス権限制御は追加しない。
- 利用者の知識水準が不明な場合、標準案内は S- とする。Userが M- を明示指定した場合は、前提条件と注意点を案内する。知識水準だけを理由に拒否しない。
- 既存のASKME最小化原則は維持する。M/Sの選択を毎回質問しない。
- Persona設計側の不備まで、利用者の自己責任として免責する規則は設けない。
- D-012とD-015の原文は変更しない。D-001〜D-016の原文は改変しない。
- M/S/Tの分類名称と既存11 Persona IDは変更しない。
- 設定案内専用Personaの名称、Persona ID、配置は確定しない。
- 既存Personaの本文とVersionは変更しない。

Rationale（理由）:
M-のOwner専用規則を廃止し、利用者の知識・経験・運用能力に応じた推奨基準へ変更するため。Owner以外の利用を禁止せず、前提を満たさない場合の機能制限・動作停止・操作性低下は利用者が理解したうえで利用する。利用経験による本人認証とアクセス権限制御は追加しない。Persona設計側の不備を利用者の自己責任として免責しない。

Supersedes（上書き対象・範囲）:
- project-notes/DECISIONS.md / 2026-10-14 / 「D-012 Limit Main to the Owner and Subset to General Users（MainのOwner専用とSubsetの一般利用）」：Owner専用規則、および一般利用者へのM-案内禁止。具体的には、Main（M-）をOwner専用とする決定、生徒およびその他の一般利用者には Subset（S-）のみを通常の設定候補として案内する決定、一般利用者に Main を選択肢として提示しない決定、使用者の権限を確認できない場合に一般利用者扱いとする決定、案内してよいPersonaの範囲が使用者の区分で決まるとする部分。
- D-015は上書きしない。D-015の「一般利用者に M/S を選択させない」は、M/Sの選択を毎回質問しないこととして維持する。知識水準が不明なときの標準案内を S- とすることは、D-015の例が S-SP を候補とする扱いと矛盾しない。Userが M- を明示指定した場合に前提条件と注意点を案内し、知識水準だけを理由に拒否しない扱いは、D-015が不採用とした「一般利用者に M/S を選択させる方式」には当たらない。

Non-Changes（非変更範囲）:
D-001〜D-016の全文。D-012のうち、Test（T-）を通常の設定候補へ含めない決定、案内上の規則を GitHub のアクセス制御として記録しない決定、使用するAIサービスでは案内範囲が決まらないとする決定。D-015の全文。M/S/Tの分類名称。既存11 Personaの本文、Version、Status、Document ID、確定11 ID。設定案内専用Personaの名称・ID・配置の未確定。利用経験による本人認証とアクセス権限制御を追加しないこと。Persona設計側の不備を利用者の自己責任として免責する規則を設けないこと。

Rejected（不採用案）:
- Owner以外のM-利用を禁止し、一般利用者へ M- を案内しない方式
- 知識水準が不明な利用者へ、M- を標準案内とする方式
- M/Sの選択を毎回質問する方式
- 利用経験による本人認証、またはアクセス権限制御を追加する方式
- Userが M- を明示指定した場合に、知識水準だけを理由に拒否する方式
- Persona設計側の不備まで、利用者の自己責任として免責する方式

## D-018 Protect the Owner Repository While Guiding User-owned Acquisition（配布元の保護とUser側取得の案内）

Date（日付）: 2026-10-14
Related Documents（関連文書）: personas/PERSONA_IDENTIFICATION_AND_SETUP.md / project-notes/CURRENT.md / Repository全体

Decision（決定）:
- Owner自身のGitHubおよびAI利用の保護を、運用上の最優先とする。
- 他のUserによるGitHub取得の制限または失敗は許容する。
- G方式を継続して使いたいUserには、自分専用のGitHub Repositoryを作成することを強く推奨する。この推奨は必須条件ではない。
- Userは、自分のRepositoryにPersonaを配置し、自分のAIにはそのRepositoryのURLを設定する。
- 自分のRepositoryを参照する設定では、OwnerのRepositoryへの取得URLが残らないよう案内する。
- User側Repositoryの管理、更新、およびアクセス制限への対応は、各Userの責任とする。
- OwnerのRepositoryは、Persona本文の唯一の編集元（SSOT）として維持する。UserによるForkやコピーは、正本の独立した編集元としない。
- P方式も継続して提供する。G方式も継続する。
- UserによるOwnerのPublic Repositoryへの直接アクセスは禁止しない。
- GitHubの利用制限がOwnerへ絶対に影響しないという技術的保証はしない。
- GitHubのアクセス制御、認証機能、新しい配布システム、自動同期機構は追加しない。
- 反映先は `personas/PERSONA_IDENTIFICATION_AND_SETUP.md` の第10.1節と、第11章の基本フロー、ASKME、例C、完了条件とする。判断履歴の参照範囲は D-006〜D-018 とする。
- D-015が定める、G方式を選んだ場合にGitHub取得用設定手順と指示欄用完成文を提示する扱いは維持する。取得先Repositoryの案内を追加する。
- D-001〜D-017の原文は改変しない。D-017の内容は変更しない。
- 既存Personaの本文とVersionは変更しない。

Rationale（理由）:
OwnerのGitHub利用に制限や障害が発生するリスクを、運用上の最優先で抑制するため。G方式を継続したいUserには本人専用Repositoryを強く推奨するが、その推奨を技術的な利用禁止や必須条件としないため。User側のコピーを正本の独立した編集元にしないため。GitHubの利用制限がOwnerへ絶対に影響しないとは技術的に保証しないため。

Supersedes（上書き対象・範囲）:
なし。D-014のG方式・P方式の維持、およびPersona本文の既存正本を独立した編集元へ増やさない決定は維持する。D-015の設定案内フローと例Cの提示要求は維持し、取得先Repositoryの案内を追加する。D-017は上書きしない。

Non-Changes（非変更範囲）:
D-001〜D-017の全文。D-017の内容。既存11 Personaの本文、Version、Status、Document ID、確定11 ID。第9章の利用推奨基準。第13章にあるGitHub取得の具体的な実装方式の未確定。指示欄用完成文ファイルの未作成。GitHubのアクセス制御、認証機能、新しい配布システム、自動同期機構を追加しないこと。GitHubの利用制限がOwnerへ絶対に影響しないという技術的保証をしないこと。

Rejected（不採用案）:
- UserによるOwnerのPublic Repositoryへの直接アクセスを禁止する方式
- User専用Repositoryの作成を、G方式の必須条件とする方式
- G方式またはP方式を廃止する方式
- User側のForkやコピーを、正本の独立した編集元とする方式
- GitHubの利用制限がOwnerへ絶対に影響しないと技術的に保証する方式
- アクセス制御、認証、新しい配布システム、または自動同期を追加する方式
