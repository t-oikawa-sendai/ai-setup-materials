# CURRENT

Last Updated: 2026-10-18
Status: CURRENT

## PURPOSE

Personaの意義・効果・限界と役割分離を説明する `ai-setup-materials` を整える。Persona本文・検証Evidence・識別と検証の仕様を保持し、設定方法は対象外とする。責務範囲と作業規則は `AGENTS.md` および `README.md` を正本とする。

本ファイルは現在地点だけを記す。Version と Status の正本は各ファイルの Document Info である。詳細仕様・判断理由は、対象成果物、`project-notes/DECISIONS.md`、既存の判断履歴、検証Evidenceを参照する。

## 現在地点

チャット移行で旧状態を現行と誤認しないため、現行値はこの節に一度だけ書く。完了事項・作業中・次工程・正本の所在へ同じ現行値を繰り返さない。

この整理の前の GitHub `main` の HEAD は `4045694c50d3d299b4d900a245ceeac3dc8665e8` である。この整理を含む commit が、その次の `main` の HEAD である。

- Claude Persona `personas/reference/CLAUDE_PERSONA.md` の現行ファイルは Version 3.0 / Approved である。承認は D-037、版番号は D-038。この現行ファイルは `24609b0` で `main` に入り、Owner欄の訂正は `1e1a2b8` に含まれる。上記 HEAD でも Version 3.0 / Approved のままである。`a908abaf46b0a4bbd8b37c16cf0efdb2ab69fe62` が保存したのは、承認前の Version 1.5（提案）/ Draft である。D-003 の Version 1.4 / Approved は当時の承認履歴である。
- ChatGPT Persona `personas/reference/CHATGPT_PERSONA.md` の現行ファイルは Version 3.1（提案）/ Draft である（D-050）。`fb1d2e6` で `main` に入り、上記 HEAD でも同じである。D-037 と D-038 の Version 3.0 / Approved は、この改訂より前の承認履歴であり、現行ファイルではない。この改訂案の実動検証と User最終承認は未了である。
- 検証用Persona `personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md` の現行ファイルは Version 3.0 / Approved である（D-037、D-038）。Version 0.1 / Draft は 2026-10-13時点の検証前の状態である。区別は `personas/reference/README.md` 第4.1節に書く。
- 次の記録は GitHub `main` に保存済みである。各 Decision 本文にある「commit と push は行わない」は、その決定の時点で commit と push を行わなかったという記録である。現在の未保存を意味しない。Decision の原文は変更していない。
  - D-032 の再テスト記録: `9401cc1`
  - D-036: `24609b0`
  - D-047: `a9b83ad`
  - D-048: `b3a8f2b`
  - D-049: `9331e0d`
  - D-050: `fb1d2e6`
  - D-051: `4045694`（上記 HEAD）

変更直後の本ファイルに書いた「commit と push は未実施」は、その時点の記録である。後続 commit で `main` に入ったものの現在の保存先は、この節と完了事項に書く。整理前の本ファイル全文は、上記 HEAD の `project-notes/CURRENT.md` に残る。

## 完了事項

詳細は各正本と Decision を参照する。ここには、完了したことと、他の資料に本文が無い記録だけを残す。

- 2026-08-19 から 2026-09-13 まで。Education の基本設計、当時の文書適合性復旧、Solution Partner 1.1〜1.5、Code Generator 2.1〜2.2、Reviewer 1.1。判断は `AGENTS.md` の `Decision & Rationale` と `project-notes/2026-09-01-solution-partner-unresolved-items-decisions.md`。Solution Partner の未承認 `Decision & Rationale` を除いた復旧 commit は `10da225e4117b3b7e88f43c42706347d154edc71`。Version 1.1〜1.3 の判断記録 commit は `34134536c95a9fff1a1a8930822474397daa38e0`。Version 1.4 の反映 commit は `6fbc12721553ce96840440b94ea82bccd849c710`。
- 2026-08-26時点の監査。当時の現行配布文書14件を確認し、14/14 が Version 1.0 / Status Approved だった。この監査は当時の確認であり、現在の Version と Status ではない。確認した内容は、Root / Education / Setup / Reference の当時の導線と実ファイル、内部リンク先の欠落なし、Education Persona 名が Researcher / Solution Partner / Code Generator / Reviewer であること、Gemini の当時の構成を `4Gem＋1` として対比表現まで揃えたこと、旧 `GEM_IMPLEMENTER`、旧 `Instructions（指示）`、`DeepSearch` 誤表記が当時の現行導線に残っていなかったこと、Gemini公式Helpで Gem作成、`知識`、Deep Research、利用上限の当時の案内を再確認したことである。
- 設定資料の作成と改訂は、当時の完了である。現行の資料所在を示さない。廃止と旧判断の保全は D-045。
- 2026-08-27。Reference Claude の責務追加、生徒ポートフォリオ向け適合性分析 `project-notes/2026-08-27-portfolio-reviewer-fit-analysis.md`、Education Reviewer の更新。
- 2026-09-23。Education Reviewer の判断履歴分離は `project-notes/GEM_REVIEWER_DECISIONS.md`。Reference AI運用資料の追加と判断は `project-notes/2026-09-23-persona-operation-case-study-decisions.md`。
- 2026-09-29。中核4種の本文編集元の一本化。`solacom_main` の反映と、元Devcheckoutへ導入していないことは `project-notes/2026-09-29-core-persona-ssot-verification.md`。
- 2026-10-05。Researcher系の更新。判断は `project-notes/RESEARCHER_PERSONA_DECISIONS.md`。内部記録は `project-notes/2026-10-05-researcher-persona-incident-record.md`。実動検証は完了事項に含めない。
- 2026-10-07。対象Repository省略の是正対象を記録した。本文是正の完了ではない。`AGENTS.md` の同日 `Decision & Rationale`。
- 2026-10-12。Repository作業時の `AGENTS.md` 確認と、`ReadOK` / `ReadNG` / `ReadUndefine` の一行報告。
- 2026-10-13。判断履歴の記録先を `project-notes/DECISIONS.md` とした。中央Governanceの正式導入は別工程のまま未了である。Git同期ゲートをローカル変更へ限定した記録は D-002、commit は `179cecc4cddd53308950d8a09a6ab5b4a142cc46`。Claude の当時の Document Info 更新は D-003、commit は `ad52f4b39a781b84a2d824d1c0ddb137c95eaa7b`。Reference運用資料の D-001・D-002 整合は D-004、commit は `eadc8a2ccb36706aac1e81c9b934904a942460fe`。この SHA の確認時点で GitHub Actions の実行履歴は 0件であり、SUCCESS とは記録しない。この 0件は確認時点の観察である。
- 2026-10-13。検証用Personaと Reference入口の検証専用導線を追加した commit は `ef77588d6c94bd50e0cc8c32c770f06c181a3bbb`。`personas/reference/setup/CHATGPT_PROJECT_PERSONA_TEST_SETUP.md` は、設定資料の本文が指示に含まれていなかったため未作成である。
- 2026-10-14。検証原文の保全は D-005。識別と検証の仕様記録は D-006〜D-016。M-Persona の利用方針は D-017、commit は `a72b6258e69977544bd269c9190d3d243d00c76d`。配布元の保護は D-018、commit は `a82ca1deb4ce7c0844c1f886ea4bc2894b007161`。
- 2026-10-15。D-019〜D-024 の反映 commit は `73b71b1dbf3dce8b99731a4207b9fa2924bfbb17`。ChatGPT Persona 第11章の是正 commit は `a627f4b2519b3750b7f3ea6f9cdd16898807ff15`。D-027 から D-031 と、先の18回答は `86b3537dfb8c2eacca851763c00055500ee122bd` に含まれる。D-032 の再テスト記録の保存先は現在地点に記載した。これらは Approved への昇格や D-025 の合格を含まない。
- 2026-10-16。Claude Persona の承認前ドラフトは `a908abaf46b0a4bbd8b37c16cf0efdb2ab69fe62`。G方式の独立レビュー原文は `c9b046c`。検証回答の原文は未取得である。現行11 Personaの User最終承認は D-037、Reference 5件の版番号統一は D-038。保存 commit は `24609b0`。
- 2026-10-17。D-039〜D-046 を含む変更は `1e1a2b822f521612e67b7c54d4d8a86a20c0ea0d`。D-047、D-048、D-049、D-050、D-051 の保存先は現在地点に記載した。
- 前回の本ファイルが記録した実測は、次のとおり残す。Claude Persona は、Project登録対象（`# Claude Persona` から本文末尾、末尾改行を含む）7,925、ファイル全体（末尾改行を含む）8,254。この整理で上記 HEAD のファイルを Unicode コードポイント数で確認し、同じ数値だった。ChatGPT Persona について、D-037 の承認表示後の記録はファイル全体が末尾改行を含めて 8,330、除いて 8,329。Owner欄訂正後の記録は、含めて 8,329、除いて 8,328。Project登録対象の記録は、含めて 7,999、除いて 7,998。上記 HEAD の現行ファイルは、ファイル全体が含めて 8,330、除いて 8,329、Project登録対象（`# ChatGPT向け責務定義` から本文末尾、Document Info を除く）が含めて 7,999、除いて 7,998 である。Owner欄訂正後として記録された 8,329 / 8,328 は、この HEAD の実測とは一致しない。当時の記録として残す。7,500文字は設計目標値であり、超過だけを不合格または作業停止としない（D-030）。

## 作業中

- ChatGPT Persona の D-050 改訂案について、実動検証と User最終承認は未了である。現行の Version と Status、GitHub上の保存先は現在地点に記載した。

## 次工程

1. Reference AI運用資料3文書の残る内容を User がレビューする。Handoff Template の現行正本化は D-047 で完了している。3文書全体の内容確定と Status の昇格は未了である。内容確定後、昇格要否は User が判断する。
2. 新チャット開始時は、本ファイルの現在地点、完了事項、作業中、次工程を読み、その後 `AGENTS.md`、対象成果物MDの順に読む。読取専用ではローカルGit同期を要求しない。ローカル変更の前には `AGENTS.md` §2.1 の同期ゲートを実施する。
3. Solution Partner と Code Generator の確定事項を、Evidence なしに再検討しない。追加の検証または修正は、User の次指示、または実利用で具体的な問題が確認された場合のみ行う。当時の判断は `AGENTS.md` の 2026-09-13。現行の Document Info は各ファイル。D-037 の承認は、実動検証の合否を変えない。
4. Education Reviewer の実利用確認は未実施である。User の指示なく自動的に切り替えない。
5. 対象外の Persona へ変更を広げない。
6. Researcher系の実動検証計画は、内部記録 `project-notes/2026-10-05-researcher-persona-incident-record.md` 第6章を維持する。現行の講師・生徒アカウントで Gem を新規作成できないため、テスト用Gemの新規作成を前提とする実施は停止し、既存Gemの利用可否と代替検証方法の判断を待つ。合格と本番Gemへの反映は未実施である。
7. 2026-10-07に記録した対象Repository省略の是正は、ChatGPT Persona の D-019 §7 以外は未着手である。対象一覧と適用条件は `AGENTS.md` の同日 Decision を参照する。記録済みであることを是正完了と扱わない。
8. 検証用Personaの ChatGPT Project 上の取得検証は、2026-10-13時点で未実施である。D-037 と D-038 は、この未実施を実施済みに変えない。導線を含む commit は `ef77588d6c94bd50e0cc8c32c770f06c181a3bbb`。未作成の設定資料は完了事項に記した。設定資料は D-045 で対象外である。
9. 中央Governanceの正式導入は別工程である。今回の判断履歴管理規則の改訂では開始しない。導入完了、Purpose、Governance Status は確定しない。
10. 検証用Personaについて、反復検証、日別評価、期間集計を継続する。2026-10-14分の原文保全は完了している。回答内容の正確性評価は未実施である。
11. 保全した原文の独立バックアップを用意する。バックアップ先のパスと方式は未決定であり、この記録では確定しない（D-005）。
12. ChatGPT Persona の D-025 は未達のまま残す。条件は TC-01、TC-02、TC-03 を各2回、合計6回、6回すべてPASSである。再試験は D-037、D-038、D-050 では開始しない。適用状態が UNVERIFIED のまま、PASS としない。Cursor から ChatGPT Project を直接操作できないため、適用状態の確認と6回の実施は User の操作が必要である。第11章の是正、共通仕様第16章の復元、D-027 の重複整理、文字数は、この6回の実施とPASSを含まない。将来の検証対象範囲の詳細基準、質問セット、実施頻度は、この工程で確定しない。先の18回答は `86b3537dfb8c2eacca851763c00055500ee122bd` にある。正規比較は D-032、保存 commit は `9401cc1` である。内訳は ChatGPT検証専用Project 4/6、Claude Project 2/6、Gemini Gem 3/6、合計 9/18。従来ChatGPT Projectの 6/6 は参考履歴である。4/6 は6回すべてPASSを満たさない。D-037 の承認を D-025 の合格と混同しない。
13. Claude Persona の G方式用指示文は作成済みである。Claude による取得成功は自己申告であり、客観的な GitHub アクセスの確認ではない。User は指示文と検証回答を視認し、問題なしと評価した。独立レビューは条件付き合格である。原文は `project-notes/persona-validation/raw/2026-10-16-claude-independent-review.md` にあり、保存 commit は `c9b046c` である。検証回答の原文は未取得であり、保存済みとして扱わない。G方式は正式運用の前提条件ではない。未実施の検証を実施済みとして扱わない。将来の検証対象範囲の詳細基準は未承認である。D-037 と D-038 は、技術的検証結果の合否を変えない。Gemini Persona の機能の大改修は対象外である。共通仕様第16章の独立工程は移動・複製していない。Persona ID は `M-CL`。Verification Code は未確定である。2026-08-27の判断原文は D-034 の「保全する原文」にある。8,000文字以内への整理は D-035。
14. 識別表示インシデントの記録は D-049、保存 commit は `9331e0d` である。この記録は、原因特定、例外処理の確定、仮説の実証、是正完了を意味しない。画面の Work と内部 kind のどちらをサービス略号の層にするかは未決である。CG、Codex、? のいずれも正式値にしていない。
15. 既存Gemの利用・編集可否と、代替導入先は未確認・未決である（D-043、D-048）。
16. 元Devcheckoutへの移行設定導入は未実施である。自動ルール読込は UNVERIFIED である。根拠は `project-notes/2026-09-29-core-persona-ssot-verification.md`。
17. 作業中の ChatGPT Persona 改訂案について、実動検証と User最終承認は、User の次指示があるまで開始しない。

Reviewerを含むPersonaの機能設計は Evidence なしに再検討しない。完了済みの文書適合性復旧を、Evidence なしに再作業対象へ戻さない。`ASKME 迎合禁止` と7文書配置を未決事項へ戻さない。Education用の基本体系は4役割である。従来の4Gem＋1と `Researcher Deep Research` は履歴として維持する。Researcherの3完成版は、当面 User（生徒）が調査範囲に応じて1版を明示選択する。

## 正本の所在

Version と Status は各ファイルの Document Info を見る。

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
- ChatGPT Persona の識別・取得・更新検証：`personas/reference/CHATGPT_PERSONA.md` 第11章。品質検証の独立工程は `personas/PERSONA_IDENTIFICATION_AND_SETUP.md` 第16章。未達の検証条件は次工程。
- Claude Persona の識別・取得・更新検証：`personas/reference/CLAUDE_PERSONA.md` 第15章。品質検証の独立工程は `personas/PERSONA_IDENTIFICATION_AND_SETUP.md` 第16章。G方式の未了は次工程。
- Reference入口：`personas/reference/README.md`
- 検証用Persona：`personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md`（中核4種のSSOTではない。現行版と過去版の区別は同ディレクトリ `README.md` 第4.1節）
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

1. 本ファイルの現在地点、完了事項、作業中、次工程
2. `AGENTS.md`（作業規則）
3. 対象成果物MDの本文（現行仕様。Version と Status は Document Info）
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
