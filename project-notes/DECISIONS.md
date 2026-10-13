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
