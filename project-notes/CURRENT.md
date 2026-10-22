# CURRENT

Last Updated: 2026-10-22
Status: CURRENT

## PURPOSE

Personaの意義・効果・限界と役割分離を説明する `ai-setup-materials` を整える。Persona本文・検証Evidence・識別と検証の仕様を保持し、サービス別の固定的な設定方法は対象外とする。S-SETUPのPersona定義本文だけを例外とする。責務範囲と作業規則は `AGENTS.md` および `README.md` を正本とする。

本ファイルは現在地点だけを記す。Version と Status の正本は各ファイルの Document Info である。詳細仕様・判断理由は、対象成果物、`project-notes/DECISIONS.md`、既存の判断履歴、検証Evidenceを参照する。

## 現在地点

チャット移行で旧状態を現行と誤認しないため、現行値はこの節に一度だけ書く。完了事項・作業中・次工程・正本の所在へ同じ現行値を繰り返さない。

この整理の前の GitHub `main` の HEAD は `4045694c50d3d299b4d900a245ceeac3dc8665e8` である。以下、この SHA を「上記 HEAD」と呼ぶ。この整理を含む commit は `76d254acbae538f10c108c2cf3b73b900588f5df` であり、上記 HEAD の次の `main` の HEAD として GitHub に保存済みである。D-054 を含む、この commit より後のローカル修正は、D-055 と D-056 を記録する commit に含まれる。その commit の SHA は、この文を含む commit 自身であるため、本文には書かない。

- Claude Persona `personas/reference/CLAUDE_PERSONA.md` の現行ファイルは Version 3.0 / Approved である。承認は D-037、版番号は D-038。この現行ファイルは `24609b0` で `main` に入り、Owner欄の訂正は `1e1a2b8` に含まれる。上記 HEAD でも Version 3.0 / Approved のままである。`a908abaf46b0a4bbd8b37c16cf0efdb2ab69fe62` が保存したのは、承認前の Version 1.5（提案）/ Draft である。D-003 の Version 1.4 / Approved は当時の承認履歴である。
- Root README `README.md` の現行ファイルは Version 1.5（提案）/ Draft である（D-056）。Version 1.4 / Approved は前版の承認履歴である（D-052）。第3章の警告と比較図の後の独立性の説明は D-053 に整合する。D-039 の重要警告原文は変更していない。D-040 の Version 1.3 / Approved、および D-051 が Version 1.3 / Approved を維持した状態は、Version 1.4 より前の記録である。
- AI利用時の課題の根拠は `personas/AI_ISSUES_EVIDENCE.md`、Hazare et al.（2026）の9種類の反論者Personaの解説は `personas/SYCOPHANCY_CHALLENGER_PERSONAS.md`、グラフは `personas/assets/sycophancy_frontier_models_2026.png` である。導線は Root README 第2章から Evidence 集へ、Evidence 集から解説へである。判断は D-056。いずれも Draft。Document ID は UNRESOLVED。この追加は、Personaによる改善効果の実証でも、研究結果の検証合格でもない。
- 教材上の標準表記は「自己正当化バイアス（誤りの連鎖）」である（D-057）。Root README 第2章の項目名、第3章冒頭、Evidence集 E-06、Education README の現行の運用方針がこの表記を用いる。D-039 の重要警告原文は変更していない。この表記は教材上の用語であり、学術的に確立した独立バイアスであるとは断定しない。
- Education README `personas/education/README.md` の現行ファイルは Version 1.1（提案）/ Draft である（D-058）。Version 1.0 / Approved は前版の承認履歴である。サービス非依存の基本4役割は維持する（D-053）。従来の4Gem＋1の承認は、評価の独立性の実証ではない。SKILLS構成は `personas/education/SKILLS/` の6ファイルで、いずれも Draft、Document ID は UNRESOLVED である。既存の `personas/education/GEM_*.md` は変更していない。Skillsの実登録、自動選択の実動検証、Deep Research連携、講師本人によるSkills実動検証は未実施である。D-058の「Skillsの手動切替操作ができない」の意味は D-059 が補足する。D-058の原文は変更しない。
- ChatGPT Persona `personas/reference/CHATGPT_PERSONA.md` の現行ファイルは Version 3.1 / Approved である。User確認と最終承認は完了している（D-052、経緯と検証ゲートは D-054）。§11.1 は Document Info の Version 3.1 / Approved と一致する。この一致は `76d254acbae538f10c108c2cf3b73b900588f5df` に含まれる。D-052 は当初、変更を Document Info のみと記録した。その原文は変更しない。`fb1d2e6` で `main` に入ったファイル、および上記 HEAD のファイルは Version 3.1（提案）/ Draft である（D-050）。D-037 と D-038 の Version 3.0 / Approved は、この改訂より前の承認履歴であり、現行ファイルではない。既存の実動検証は 4/6 である。D-025 の 6/6 PASS は未達である。新たな 6/6 PASS の Evidence は未確認である。共通仕様第16章の現行規則は維持する。User承認は技術検証を PASS に変えない。第16章への完全適合は確認していない。
- 検証用Persona `personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md` の現行ファイルは Version 3.0 / Approved である（D-064）。Persona ID は `T-IT-ADVISOR`、Verification Code は `ADVISOR-ALPHA` である。D-037 の承認と D-038 の版番号統一は、Version 3.0 / Approved の承認履歴である。D-062 が現行を Version 3.1（提案）/ Draft とした記録は、その決定時点の記録である。Version 0.1 / Draft は 2026-10-13時点の検証前の状態である。区別は `personas/reference/README.md` 第4.1節に書く。この Approved は User の版の確定であり、実動検証の完了や適用成功を意味しない。D-062 の「この反映はローカルのみであり、commit と push は行っていない」は、その文を書いた時点の記録である。保存 commit は `4511652ffa32c092e85f7fc785fdaf44a98ab0bc` であり、`main` へ push 済みである。2026-10-13 の `Decision & Rationale` は、Persona本文から削除し、原文を `project-notes/DECISIONS.md` の D-063 に保存した。この移設と D-064 の版の確定はローカルのみであり、commit と push は行っていない。Persona本文に履歴への参照は追加していない。
- 新規S-IECDは、講師向け教材制作Personaとして `personas/reference/IT_EDUCATION_CONTENT_DESIGNER.md` に置く提案である。Persona ID `S-IECD` と Version 0.1 は提案、Statusは Draft。GitHub `main` を本文正本とするG方式で設計し、D-065に判断を記録する。Reference READMEには中核4種と別のDraft節で案内する。Userの後続指示により、この変更と既存Root READMEの見出し4件を同じCommitでGitHub `main`へ反映する対象とした。保存の成否はGitHubの `main` HEADで判定する。各AIサービスでのPersona取得・適用・実動検証およびUserのApproved承認は未実施であり、取得成功・PASS・Approvedとは扱わない。Document ID は UNRESOLVED である。
- 新規S-SETUPは、Personaの選定とAIサービスへの設定案内を担当するPersonaとして `personas/reference/PERSONA_SETUP_ADVISOR.md` に置く提案である。Persona ID `S-SETUP` と Version 3.0 は提案、Statusは Draft、Document IDは UNRESOLVED。G方式の本文正本をGitHub `main` とする設計で、D-066にS-SETUP本文だけの対象範囲例外を記録する。Userの明示指示により、独立チェックアウトで作成した変更をCommit・Pushする対象とした。保存の成否はGitHub `main` のHEADと本文の再取得で判定する。取得・適用・実動検証とUserのApproved承認は未実施である。元Devチェックアウトの未commit変更には触れていない。
- 次の記録は GitHub `main` に保存済みである。各 Decision 本文にある「commit と push は行わない」は、その決定の時点で commit と push を行わなかったという記録である。現在の未保存を意味しない。Decision の原文は変更していない。
  - D-032 の再テスト記録: `9401cc1`
  - D-036: `24609b0`
  - D-047: `a9b83ad`
  - D-048: `b3a8f2b`
  - D-049: `9331e0d`
  - D-050: `fb1d2e6`
  - D-051: `4045694`（上記 HEAD）
  - D-052、D-053、および同 commit の5ファイル（`README.md`、`personas/education/README.md`、`personas/reference/CHATGPT_PERSONA.md`、`project-notes/CURRENT.md`、`project-notes/DECISIONS.md`）: `76d254acbae538f10c108c2cf3b73b900588f5df`
  - D-058、および同 commit の対象（`README.md`、`personas/education/README.md`、`personas/education/SKILLS/` の6ファイル、`project-notes/CURRENT.md`、`project-notes/DECISIONS.md`）: `9ddbc319b48d6b7bcb53254a830c6622af54d20f`
  - D-060（`AGENTS.md`、`personas/reference/CHATGPT_PERSONA.md`、`project-notes/CURRENT.md`、`project-notes/DECISIONS.md`）: `a00542eba524f341904ffcb208aae86a136ecee1`
  - D-062（`personas/PERSONA_IDENTIFICATION_AND_SETUP.md`、`personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md`、`personas/reference/README.md`、`project-notes/CURRENT.md`、`project-notes/DECISIONS.md`）: `4511652ffa32c092e85f7fc785fdaf44a98ab0bc`

変更直後の本ファイルに書いた「commit と push は未実施」は、その時点の記録である。後続 commit で `main` に入ったものの現在の保存先は、この節と完了事項に書く。整理前の本ファイル全文は、上記 HEAD の `project-notes/CURRENT.md` に残る。D-052、D-053、D-058 の本文にある「commit と push を含まない」も、その決定の時点の記録であり、上記の保存済み commit を未保存と読まない。D-059 は、D-058 の保存 commit には含まれない。

- AIサービス変更の参考記録は `docs/AI_SERVICE_UPDATES.md` に集約する（D-061）。Root README は教材の入口とし、日時依存の詳細は同文書を参照する。2026-10-19のOwner実機確認、2026-10-18のPC環境でのSkills表示、2026-10-16の講師・生徒アカウントでのGem新規作成不可、および2026-10-18時点のGoogle公式案内は同文書にある。2026-10-18のPC観測は、2026-10-19のWeb版観測とは別の事実として保持する。本教材の対象アカウント種別、Web版での新規Gemの保存完了、Desktop版の当日状態、既存Gemの編集可否、GemとSkillsの同時動作、Skillsの作成と実動検証は未確認である。公式案内は、各利用環境の実際の状態や移行完了を証明しない。Education README の既存の日時付き記載は、この作業では変更していない。
- Git操作の承認は D-060 である。Push の明示指示には、対象変更を Commit する許可を含む。反映先は `AGENTS.md` と `personas/reference/CHATGPT_PERSONA.md` の §5、§7 である。ChatGPT Persona の Version 3.1 / Approved は維持する。この文の時点では commit と push は行っていない。その後の保存 commit は `a00542eba524f341904ffcb208aae86a136ecee1` であり、`main` へ push 済みである。上記の「行っていない」は、その文を書いた時点の記録である。中央Governance正本は編集していない。
- READMEの変更情報分離は D-061 である。Root README は Version 1.5（提案）/ Draft のままである。この反映はローカルのみであり、commit と push は行っていない。

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
- 2026-10-18。Root README と ChatGPT Persona の User最終承認を反映した。判断は D-052。D-052 本文の「commit と push を含まない」は、その決定の時点の記録である。保存先は現在地点に書いた `76d254acbae538f10c108c2cf3b73b900588f5df` である。実動検証の合否は変えない。
- 2026-10-18。Root README 第3章の独立性の説明と、Education README のサービス非依存の基本4役割を反映した。判断は D-053。保存先は D-052 と同じ commit である。D-053 本文の「commit と push を含まない」は、その決定の時点の記録である。
- 2026-10-18。Root README の表現明確化3件と、Reviewer指摘 R-01、R-02、R-03、R-04、R-05、R-08 を反映した。R-01 と R-02 の判断は D-054。R-04 と R-05 は、既存の D-043、D-048、D-053 の範囲で本文を合わせた。新たな方針判断としての別 Decision は作っていない。R-06、R-07、R-09、R-10 は対象外である。この反映は、D-055 の今回限りの例外により保全したまま、D-056 と同じ commit に含まれる。保存先の SHA は、その commit 自身であるため本文には書かない。D-052 と D-053 の保存済み commit とは別である。
- 2026-10-18。同期ゲートの今回限りの例外は D-055。Evidence資料の追加と参照関係は D-056。状態は現在地点に書く。
- 2026-10-18。教材上の標準表記を定め、Root README、Evidence集、Education README の現行本文へ反映した。判断は D-057。報告済みの未commit変更2ファイルは保全した。この保全は今回の継続作業に限る。`AGENTS.md` §2.1 と D-055 の適用範囲は変更しない。保存先の SHA は、この文を含む commit 自身であるため本文には書かない。
- 2026-10-18。既存GEMを保全したまま、EducationのSKILLS 6ファイルを追加し、Root README と Education README を更新した。判断は D-058。D-058 本文の「commit と push を含まない」は、その決定の時点の記録である。保存 commit は `9ddbc319b48d6b7bcb53254a830c6622af54d20f` である。実動検証は未実施であり、Approved ではない。
- 2026-10-18。D-058の「Skillsの手動切替操作ができない」の意味を補足した。判断は D-059。D-058の原文は変更していない。同じ修正で、Hazare et al. の事例抽出条件と分類上の限界、Root README 第3章の用語の読まれ方、Education README 第7章の参照先を直した。Version と Status は変更していない。D-059 は、D-058 の保存 commit `9ddbc319b48d6b7bcb53254a830c6622af54d20f` には含まれない。
- 2026-10-18。Git操作の承認を、Push の明示指示に対象変更の Commit 許可を含める規則へ更新した。判断は D-060。反映先は `AGENTS.md` と ChatGPT Persona の §5、§7 である。この文の時点では commit と push は行っていない。保存 commit は `a00542eba524f341904ffcb208aae86a136ecee1` である。中央Governance正本は編集していない。
- 2026-10-19。Root README から日時依存のGemini詳細を分離し、`docs/AI_SERVICE_UPDATES.md` を新設した。判断は D-061。Root README の Version 1.5（提案）/ Draft は維持する。この文の時点では commit と push は行っていない。
- 2026-10-20。検証用Personaの識別・取得・更新検証を共通仕様へ揃えた。判断は D-062。第1章から第15章、既存Decision、検証原文、過去版は変更していない。この反映はローカルのみであり、commit と push は行っていない。実動検証、Approved、適用成功は含まない。現行の Version と Status は現在地点に書く。その後の保存 commit は `4511652ffa32c092e85f7fc785fdaf44a98ab0bc` である。上記の「行っていない」は、その文を書いた時点の記録である。
- 2026-10-20。検証用Persona末尾の 2026-10-13 `Decision & Rationale` を原文のまま D-063 へ移し、Persona本文から削除した。第1章から第16章、Version 3.1（提案）/ Draft、Verification Code `ADVISOR-ALPHA` は変更していない。この移設はローカルのみであり、commit と push は行っていない。実動検証、独立レビュー、Approvedへの昇格は含まない。
- 2026-10-20。Userは、検証用Personaの現行を Version 3.0 / Approved に確定した。判断は D-064。対象は `T-IT-ADVISOR` のみである。D-063 の移設原文と、Persona本文に履歴への参照を残さない決定は維持する。この Approved は User の版の確定であり、実動検証の合格ではない。実動検証は未実施のままである。この反映はローカルのみであり、commit と push は行っていない。
- 前回の本ファイルが記録した実測は、次のとおり残す。Claude Persona は、Project登録対象（`# Claude Persona` から本文末尾、末尾改行を含む）7,925、ファイル全体（末尾改行を含む）8,254。この整理で上記 HEAD のファイルを Unicode コードポイント数で確認し、同じ数値だった。ChatGPT Persona について、D-037 の承認表示後の記録はファイル全体が末尾改行を含めて 8,330、除いて 8,329。Owner欄訂正後の記録は、含めて 8,329、除いて 8,328。Project登録対象の記録は、含めて 7,999、除いて 7,998。上記 HEAD の現行ファイルは、ファイル全体が含めて 8,330、除いて 8,329、Project登録対象（`# ChatGPT向け責務定義` から本文末尾、Document Info を除く）が含めて 7,999、除いて 7,998 である。Owner欄訂正後として記録された 8,329 / 8,328 は、この HEAD の実測とは一致しない。当時の記録として残す。7,500文字は設計目標値であり、超過だけを不合格または作業停止としない（D-030）。

## 作業中

- 生徒向けPrivate Template配布の構築Commit `2ab8587445549401e0d4af127fca580171743496` は講師正本 `main` に保存済みである。講師正本から `OSLIB21-materials/ai-setup-materials-student` への初回同期設計と9パスの配布範囲は D-067。GitHub画面で `OSLIB21-materials` のGitHub Free・請求表示 `$0`、配布先Private Repository、Template repositoryのチェック済み表示を確認した。User本人が正本RepositoryのActions Secret `STUDENT_TEMPLATE_TOKEN` を登録し、GitHub画面の `Repository secret added.`、Name、last updated表示を確認した。初回PushのActions実行 [39757830981](https://github.com/t-oikawa-sendai/ai-setup-materials/actions/runs/39757830981) はsuccessで、jobの各stepもsuccessだった。配布先 `main` は `ab8224c2a855084155c719ad03ce8119ed296528` で、初期HEAD `811b36da917c0f0509aefbcda8c2971d53f39c47` は履歴に残る。配布先のtrackedファイルは初回に許可された9パスだけで、9ファイルすべてが正本の対応ファイルとbyte一致した。初回実行ログのtoken入力は `***` 表示で、確認した資格情報形式の未マスク文字列は見つからなかった。生徒招待と実アカウントでの利用確認は未実施である。
- Userは一覧からPersona配下の22件とRoot READMEを追加配布対象に選択し、`AGENTS.md` と `project-notes/` の本文は不要とした。さらに、選択済み通常文書のDraft↔Approvedの変化では同期継続を選んだ。判断は D-069。配布先30パスの追加・上書き、旧9パスだけの自動削除、Root/Education READMEの正本由来コピーへの切替を実装した。一時Git Repositoryで30パスの初回同期・再実行の変更なし・対象外ファイルと別branchの保護・GEMのbyte一致を確認し、Draft↔Approvedの双方向と不正Status、旧資料の状態変更、READMEの必須文言欠落、講師正本への除外URLの拒否を確認した。Claudeの指摘GOV-01、BUG-01、ARCH-02を是正後、焦点を絞った独立再レビューはコード上PASS、GOV-02とBUG-02は非阻害のLOW指摘だった。Commit前にレビュー対象と実際のローカルパッチのSHA-256 `bbe1dd47183fffb8e1c5bd320fc88933349c0289e251c2dc48097473530efe3c` の一致を確認した。`.github/workflows/sync-student-template.yml`、`AGENTS.md`、`project-notes/CURRENT.md`、`project-notes/DECISIONS.md`、`scripts/sync_student_template.py` の5ファイルだけをnoreply Git identity `244720561+t-oikawa-sendai@users.noreply.github.com` でCommitし、force pushを使わない通常Pushを完了した。講師正本のGitHub `main`、ローカルHEAD、`origin/main` は `3745eba459f0b73651e23e27bfcea7134a6b187a` で一致した。Push起動のActions実行 [39771839798](https://github.com/t-oikawa-sendai/ai-setup-materials/actions/runs/39771839798) はsuccessで、同期jobの全stepもsuccessだった。GitHub APIで配布先がPrivate・Template repository・`main` であることを確認した。配布先 `main` のHEADは `c20a3ccb656ddb9157bc0b1b7126f66704f6b9e4`、trackedファイルは管理対象30パスと完全一致し、正本からの配布変換後の内容と欠落・余剰・不一致がなかった。旧HEAD `ab8224c2a855084155c719ad03ce8119ed296528` は履歴上の祖先として残る。生徒個人Repositoryは操作していない。生徒の実アカウントでの利用確認は未実施である。
- Claude独立レビューは初回BUG-01によりFAILだった。LICENSE末尾の空行で初回同期を止める差分チェック1行をローカルのワークフローから削除し、一時Git Repositoryで同期からCommitまで成功を確認した。提示パッチの再構成環境での再判定は、BUG-01がコード上PASS、GOV-01とUser判断D-068がPASS、SEC-01が非阻害の参考指摘だった。レビュー側は作業用checkoutの実ファイル一致を確認していない。初回のGitHub Actionsと配布内容は上記の実測結果で判定する。
- 講師正本 `t-oikawa-sendai/ai-setup-materials` のGitHub表示は現在Publicである。Userは配布先の構築・検証完了後に正本をPrivateへ変更する予定を示した。現時点で可視性は変更していない。D-070反映後の配布版S-SETUPには講師正本URLを含めず、各自のRepositoryのURLを記入する未設定欄がある。正本Private化の実施判断は残る。
- UserはD-070で、S-SETUPを30パスに残しつつ、配布コピーの講師正本URLを各自のRepositoryの正確なS-SETUP本文URLを記入する未設定欄へ置き換えると決めた。講師正本の `personas/reference/PERSONA_SETUP_ADVISOR.md` はbyte単位で変更していない。一時Git Repositoryで、旧30パス配布版からの更新ではRoot READMEとS-SETUPの2パスだけが変わり、30パスの追加・上書き範囲、旧9パスの削除範囲、再実行の変更なし、元URLの追加・変更時の停止を確認した。配布コピーでは講師管理のGitHub `main` を教材の正本、個人Repositoryを取得先のコピーとして区別する。URL未記入・Private Repositoryの認証または接続不足を取得成功とせず、個人Repositoryには後続更新が自動反映されないと案内する。D-070の変更はnoreply Git identity `244720561+t-oikawa-sendai@users.noreply.github.com` のcommit `defbc2a4bc675196409fe257b392227ab6f824c4` として通常Push済みで、講師正本のGitHub `main`、ローカルHEAD、`origin/main` が一致した。Push起動のActions実行 [39777787027](https://github.com/t-oikawa-sendai/ai-setup-materials/actions/runs/39777787027) はcompleted/successで、同期jobの全stepもsuccessだった。配布先Private RepositoryをSSHでcloneして確認した `main` HEADは `547d018dd66f815c9d3472a8bbd98cd63c7604c0`。trackedファイルは管理対象30パスだけで、正本からの配布変換後の内容と欠落・余剰・byte不一致がなく、cloneはcleanだった。旧HEAD `c20a3ccb656ddb9157bc0b1b7126f66704f6b9e4` は履歴上の祖先として残る。配布先のPrivate・Template設定は先のGitHub確認結果であり、この再検証では設定画面を再確認していない。生徒の招待・実アカウント利用と、Privateな個人RepositoryからのS-SETUPのG方式取得は未確認である。生徒個人Repositoryは操作していない。
- D-071の作業で、講師用・生徒用のGitHub配布手順書2冊を講師正本の作業用checkoutの `docs/distribution/` に反映した。2冊は改訂済み原本とbyte一致する。生徒用1パスだけをPrivate Templateへ追加・上書きする同期変更を実装した。旧30パスは維持し、追加・上書きは31パス、削除は旧9パスのままとする。講師用手順書と他の `docs/` は配布しない。配布先Root READMEのコピーに生徒用手順書へのリンクと構成表示を追加し、講師正本のRoot READMEは変更していない。ローカルの一時Git Repositoryで31パスの初回追加と再実行時の全件変更なしを確認した。実配布先の旧30パス版のローカル複製では、差分は配布先Root READMEと生徒用手順書の2パスだけだった。対象外ファイルと別branchを保持し、生徒用手順書内の講師正本URL、内部リンク、秘密情報の混入を同期前に拒否した。この作業前にGitHubで実測した配布先は30パスだった。31パス構成のGitHub実配布結果は、この記録時点では未取得であり、公開後の実測を別記する。
- D-063 の判断履歴移設と、D-064 の Version 3.0 / Approved への確定は、ローカル反映済みである。commit と push は未実施である。対象は `personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md`、`personas/PERSONA_IDENTIFICATION_AND_SETUP.md`、`personas/reference/README.md`、`project-notes/DECISIONS.md`、`project-notes/CURRENT.md` の5ファイルである。R-01 から R-05、R-08、および Evidence 資料の追加は、現在地点に書いた commit に含まれる。実動検証の未達は次工程に残す。

## 次工程

1. Reference AI運用資料3文書の残る内容を User がレビューする。Handoff Template の現行正本化は D-047 で完了している。3文書全体の内容確定と Status の昇格は未了である。内容確定後、昇格要否は User が判断する。
2. 新チャット開始時は、本ファイルの現在地点、完了事項、作業中、次工程を読み、その後 `AGENTS.md`、対象成果物MDの順に読む。読取専用ではローカルGit同期を要求しない。ローカル変更の前には `AGENTS.md` §2.1 の同期ゲートを実施する。
3. Solution Partner と Code Generator の確定事項を、Evidence なしに再検討しない。追加の検証または修正は、User の次指示、または実利用で具体的な問題が確認された場合のみ行う。当時の判断は `AGENTS.md` の 2026-09-13。現行の Document Info は各ファイル。D-037 の承認は、実動検証の合否を変えない。
4. Education Reviewer の実利用確認は未実施である。User の指示なく自動的に切り替えない。
5. 対象外の Persona へ変更を広げない。
6. Researcher系の実動検証計画は、内部記録 `project-notes/2026-10-05-researcher-persona-incident-record.md` 第6章を維持する。Gem新規作成を前提とする実施は、現在地点に書いた 2026-10-16 の User観測のため停止したままである。この観測は公式の提供終了予定とは別である。2026-10-19以降の環境別観測は `docs/AI_SERVICE_UPDATES.md` にあり、この停止を解除しない。既存Gemの利用可否と代替検証方法の判断を待つ。合格と本番Gemへの反映は未実施である。
7. 2026-10-07に記録した対象Repository省略の是正は、ChatGPT Persona の D-019 §7 以外は未着手である。対象一覧と適用条件は `AGENTS.md` の同日 Decision を参照する。記録済みであることを是正完了と扱わない。
8. 検証用Personaの ChatGPT Project 上の取得検証は、2026-10-13時点で未実施である。D-037、D-038、D-062、D-064 は、この未実施を実施済みに変えない。導線を含む commit は `ef77588d6c94bd50e0cc8c32c770f06c181a3bbb`。未作成の設定資料は完了事項に記した。設定資料は D-045 で対象外である。
9. 中央Governanceの正式導入は別工程である。今回の判断履歴管理規則の改訂では開始しない。導入完了、Purpose、Governance Status は確定しない。
10. 検証用Personaについて、反復検証、日別評価、期間集計を継続する。2026-10-14分の原文保全は完了している。回答内容の正確性評価は未実施である。
11. 保全した原文の独立バックアップを用意する。バックアップ先のパスと方式は未決定であり、この記録では確定しない（D-005）。
12. ChatGPT Persona の D-025 は未達のまま残す。条件は TC-01、TC-02、TC-03 を各2回、合計6回、6回すべてPASSである。再試験は D-037、D-038、D-050 では開始しない。適用状態が UNVERIFIED のまま、PASS としない。Cursor から ChatGPT Project を直接操作できないため、適用状態の確認と6回の実施は User の操作が必要である。第11章の是正、共通仕様第16章の復元、D-027 の重複整理、文字数は、この6回の実施とPASSを含まない。将来の検証対象範囲の詳細基準、質問セット、実施頻度は、この工程で確定しない。先の18回答は `86b3537dfb8c2eacca851763c00055500ee122bd` にある。正規比較は D-032、保存 commit は `9401cc1` である。内訳は ChatGPT検証専用Project 4/6、Claude Project 2/6、Gemini Gem 3/6、合計 9/18。従来ChatGPT Projectの 6/6 は参考履歴である。4/6 は6回すべてPASSを満たさない。D-037 の承認を D-025 の合格と混同しない。D-052 と D-054 の User最終承認も、4/6 の変更および D-025 の合格を含まない。共通仕様第16章の一般規則は変更しない。
13. Claude Persona の G方式用指示文は作成済みである。Claude による取得成功は自己申告であり、客観的な GitHub アクセスの確認ではない。User は指示文と検証回答を視認し、問題なしと評価した。独立レビューは条件付き合格である。原文は `project-notes/persona-validation/raw/2026-10-16-claude-independent-review.md` にあり、保存 commit は `c9b046c` である。検証回答の原文は未取得であり、保存済みとして扱わない。G方式は正式運用の前提条件ではない。未実施の検証を実施済みとして扱わない。将来の検証対象範囲の詳細基準は未承認である。D-037 と D-038 は、技術的検証結果の合否を変えない。Gemini Persona の機能の大改修は対象外である。共通仕様第16章の独立工程は移動・複製していない。Persona ID は `M-CL`。Verification Code は未確定である。2026-08-27の判断原文は D-034 の「保全する原文」にある。8,000文字以内への整理は D-035。
14. 識別表示インシデントの記録は D-049、保存 commit は `9331e0d` である。この記録は、原因特定、例外処理の確定、仮説の実証、是正完了を意味しない。画面の Work と内部 kind のどちらをサービス略号の層にするかは未決である。CG、Codex、? のいずれも正式値にしていない。
15. 既存Gemの編集可否と、代替導入先は未確認・未決である（D-043、D-048）。2026-10-19の環境別観測は `docs/AI_SERVICE_UPDATES.md` にあり、既存Gemの表示・実行を一部環境で確認した事実は、編集可否や全環境での利用可否を確認済みにしない。公式の自動再作成予定は、この未確認を確認済みに変えない。対象アカウント種別は未確認のままである。
16. 元Devcheckoutへの移行設定導入は未実施である。自動ルール読込は UNVERIFIED である。根拠は `project-notes/2026-09-29-core-persona-ssot-verification.md`。
17. ChatGPT Persona の User最終承認は完了している。実動検証の再試験は、User の次指示があるまで開始しない。
18. Evidence 2文書と Root README の今回改訂の正式な採否は、User の次の判断を待つ。Document ID の確定も、その判断まで行わない。
19. Education SKILLS の実登録、自動選択精度の実動検証、Deep Research連携は未実施である。講師本人がGemini Skillsを利用して実動検証することは、前提にしない。Userの次指示まで開始しない。
20. 中央Governance正本への D-060 の反映、および定義済み配布は未実施である。`solacom_main` は、対象ファイルに別件の未commit変更があるため、この作業では編集していない。配布と Migration は開始していない。

21. S-IECDはGitHub反映後に、取得、適用、共通仕様第16章に従うPersona Verificationを別々に確認する。検証条件の詳細は未承認事項として扱い、実施前にUserの判断を要する。実動検証の合格だけでApprovedへ昇格させず、Userの最終承認を待つ。

Reviewerを含むPersonaの機能設計は Evidence なしに再検討しない。完了済みの文書適合性復旧を、Evidence なしに再作業対象へ戻さない。`ASKME 迎合禁止` と7文書配置を未決事項へ戻さない。Education用の基本体系は4役割、SKILLSは合計6つである。従来の4Gem＋1と `Researcher Deep Research` は参考記録として維持する。ResearcherのSKILLSは Learning、Development、Career の3つである。

## 正本の所在

Version と Status は各ファイルの Document Info を見る。

- 作業規則：`AGENTS.md`
- 生徒向け配布同期：`.github/workflows/sync-student-template.yml` と `scripts/sync_student_template.py`。前回GitHubで実測した追加・上書き範囲は D-069 の30パスだった。D-071の追加・上書き設計は生徒用手順書1パスを加えた31パスである。自動削除範囲は D-067 の旧9パス。旧 `distribution/student/` は現行の配布元に使用しない。
- GitHub教材配布手順書：`docs/distribution/INSTRUCTOR_PRIVATE_ORG_TEMPLATE_GUIDE.md` と `docs/distribution/STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md`（D-071。生徒用だけが同期対象）。
- Persona識別と検証：`personas/PERSONA_IDENTIFICATION_AND_SETUP.md`（旧ファイル名を維持）
- Repository入口・Persona重要性の共通説明：`README.md`
- AIサービス変更情報：`docs/AI_SERVICE_UPDATES.md`（Persona教材や運用に関係する参考記録。網羅的な製品調査の正本ではない）
- AI利用時の課題の外部研究Evidence：`personas/AI_ISSUES_EVIDENCE.md`（Draft。第2章からの参照先。Document ID は UNRESOLVED）
- 迎合研究の9種類の反論者Persona解説：`personas/SYCOPHANCY_CHALLENGER_PERSONAS.md`（Draft。Evidence集から参照。本教材の4役割Personaとは別。Document ID は UNRESOLVED）
- カスタム指示・Persona・プロンプトの詳細比較とPersonaあり／なしの検証詳細：`personas/WHY_PERSONA_MATTERS.md`（文書ID・独立Versionは未決）
- Education Persona：`personas/education/`
- Education Solution Partner正本：`personas/education/GEM_SOLUTION_PARTNER.md`
- Education Code Generator正本：`personas/education/GEM_CODE_GENERATOR.md`
- Education Reviewer正本：`personas/education/GEM_REVIEWER.md`
- Education入口：`personas/education/README.md`
- Education SKILLS：`personas/education/SKILLS/`
- Reference Persona：`personas/reference/`
- ChatGPT Persona の識別・取得・更新検証：`personas/reference/CHATGPT_PERSONA.md` 第11章。品質検証の独立工程は `personas/PERSONA_IDENTIFICATION_AND_SETUP.md` 第16章。未達の検証条件は次工程。
- Claude Persona の識別・取得・更新検証：`personas/reference/CLAUDE_PERSONA.md` 第15章。品質検証の独立工程は `personas/PERSONA_IDENTIFICATION_AND_SETUP.md` 第16章。G方式の未了は次工程。
- Reference入口：`personas/reference/README.md`
- 講師向けS-IECD Draft：`personas/reference/IT_EDUCATION_CONTENT_DESIGNER.md`（G方式の本文正本候補。GitHub `main` 未反映時は取得対象外。品質・実動検証は共通仕様第16章）
- 検証用Persona：`personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md`（中核4種のSSOTではない。識別・取得・更新検証は同ファイル第16章。品質検証の独立工程は `personas/PERSONA_IDENTIFICATION_AND_SETUP.md` 第16章。現行版と過去版の区別は同ディレクトリ `README.md` 第4.1節）
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
