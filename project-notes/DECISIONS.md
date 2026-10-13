# DECISIONS（判断履歴）

<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | ASM-DECISIONS-001 |
| Version（バージョン） | 1.0 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-10-13 |
| Last Updated（最終更新日） | 2026-10-13 |
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
