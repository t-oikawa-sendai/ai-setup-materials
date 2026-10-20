<details>
<summary>Document Info（文書情報）</summary>

| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-IDENTIFICATION-SETUP-001 |
| Version（バージョン） | 1.2 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-10-14 |
| Last Updated（最終更新日） | 2026-10-20 |
| Owner（管理者） | Takashi Oikawa |
| Related Documents（関連文書） | [`../AGENTS.md`](../AGENTS.md)<br>[`../README.md`](../README.md)<br>[`education/README.md`](education/README.md)<br>[`reference/README.md`](reference/README.md)<br>[`../project-notes/DECISIONS.md`](../project-notes/DECISIONS.md)<br>[`../project-notes/CURRENT.md`](../project-notes/CURRENT.md) |

</details>

---

# Persona Identification and Verification（Persona識別と検証）

## 1. Purpose（目的）

この文書は、Personaの分類・識別、利用推奨、および Persona Verification の共通仕様の正本である。AIサービス別の設定方法、画面操作、指示欄用完成文は扱わない。

2026-10-14〜15に確定した識別・検証仕様は維持する。設定案内と指示欄用文章を扱った旧第10章から第15章は、2026-10-17のUser決定（[`../project-notes/DECISIONS.md`](../project-notes/DECISIONS.md) の D-045）により現行本文から除外した。旧判断は同Decisionファイルに残す。

この文書の Version 1.2 / Approved は共通仕様の文書状態であり、個々のPersonaのApproved昇格や実動検証の完了を意味しない。今回、VersionとStatusは変更しない。ファイル名・Document IDの `SETUP` と第16章の番号は、既存参照との互換性のため維持する。設定方法が現行の対象範囲に含まれるという意味ではない。

本書は education と reference の双方に適用する。Persona本文や判断履歴を代替しない。

## 2. Record Status（記録の区別）

本書の各事項は、次のいずれかである。

| Status | Meaning |
|---|---|
| CONFIRMED | Userが承認した確定仕様 |
| PROPOSED | ChatGPTが提示し、Userの個別承認を受けていない案・初稿 |
| UNRESOLVED | 今後の詳細設計・検証を要する事項 |

PROPOSED と UNRESOLVED を確定仕様として扱わない。

## 3. CONFIRMED: Persona Classification（Persona分類）

| Prefix | 名称 | 意味 |
|---|---|---|
| M- | Main | 基本版 |
| S- | Subset | 機能限定版 |
| T- | Test | 検証版 |

確定事項：

- `S-` の正式な日本語名称は「機能限定版」である。
- 「教育用」は対象者・用途の説明であり、Persona分類名ではない。
- Subsetを厳密な機能包含関係で定義しない。
- MainとSubsetの1対1対応表を必須にしない。
- `education/` と `reference/` のディレクトリ構造を維持する。
- 既存Document IDを変更しない。Persona IDはDocument IDではない。
- `Researcher Deep Research` は独立Personaではない。第4章の11件に含めない。Researcher Personaを使う従来の追加Gemとして記録する。

## 4. CONFIRMED: Eleven Persona IDs（全11 Persona ID）

IDは確定済みである。再命名・再提案しない。

| File | 確定Persona ID | 移行前のDocument Info |
|---|---|---|
| [`reference/CHATGPT_PERSONA.md`](reference/CHATGPT_PERSONA.md) | M-CG | Version 1.2（提案） / Draft |
| [`reference/GEMINI_PERSONA.md`](reference/GEMINI_PERSONA.md) | M-GM | Version 1.1 / Approved |
| [`reference/CLAUDE_PERSONA.md`](reference/CLAUDE_PERSONA.md) | M-CL | Version 1.4 / Approved |
| [`reference/CURSOR_PERSONA.md`](reference/CURSOR_PERSONA.md) | M-CU | Version 1.1（提案） / Draft |
| [`education/GEM_RESEARCHER_FULL.md`](education/GEM_RESEARCHER_FULL.md) | S-R-FULL | Version 1.1 / Approved |
| [`education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`](education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md) | S-R-LD | Version 1.1 / Approved |
| [`education/GEM_RESEARCHER_DEVELOPMENT.md`](education/GEM_RESEARCHER_DEVELOPMENT.md) | S-R-DEV | Version 1.1 / Approved |
| [`education/GEM_SOLUTION_PARTNER.md`](education/GEM_SOLUTION_PARTNER.md) | S-SP | Version 1.6（提案） / Draft |
| [`education/GEM_CODE_GENERATOR.md`](education/GEM_CODE_GENERATOR.md) | S-CG | Version 2.3（提案） / Draft |
| [`education/GEM_REVIEWER.md`](education/GEM_REVIEWER.md) | S-RV | Version 1.2 / Approved |
| [`reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md`](reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md) | T-IT-ADVISOR | Version 0.1 / Draft |

移行前のDocument Infoは、2026-10-14に各ファイルから確認した現行値である。Version 3.0 へ更新した後の値ではない。この表の記録によって、本文もStatusも変更しない。

`T-IT-ADVISOR` は確定Persona IDである。現行の [`reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md`](reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md) 第16章の識別子は `T-IT-ADVISOR` である。移行前の識別子 `IT-GENERAL-ADVISOR-TEST` は、D-063 が保全した 2026-10-13 `Decision & Rationale` の原文と、検証原文に歴史として残る。それらの原文は書き換えない。Persona本文には、その履歴への参照を残さない。第4章の表は、2026-10-14時点の移行前の Document Info であり、現行の Version と Status ではない。

Researcher 3ファイルの現行見出しは、いずれも Researcher Persona である。Education README上の選択は、FULLが Learning / Career / Development、LEARNING_DEVELOPMENTが Learning / Development、DEVELOPMENTが Development である。この選択関係を、MainとSubsetの1対1対応表として扱わない。

## 5. CONFIRMED: Version 3.0 Migration（Version 3.0への移行方針）

- 共通基準としてVersion 2.0を採用せず、Version 3.0を新しい基点とする。Version 2.0 は欠番である。
- 旧2.x系列は歴史的に存在するため、過去履歴を削除・書き換えしない。
- 既存のDraft・Approved状態を、Version変更だけで自動昇格させない。
- 移行前のVersionと移行後のVersionを混同しない。第4章の表は、2026-10-14時点の移行前の歴史である。移行後の共通Versionは `3.0` である。
- 2026-10-16の D-038 で、`reference/` の5件の Document Info を Version 3.0 / Approved とした。対象は ChatGPT、Claude、Cursor、Gemini、検証用Personaである。これは版番号の統一である。共通仕様の全機能を各Persona本文へ移行した完了ではない。全11の User承認は D-037 のまま有効であり、この版番号統一を理由に再検証へ戻さない。
- `GEM_` で始まる Education 6件は、現在の数値 Version / Approved を維持する。大改修の完了後に Version 3.0 へ揃える。
- 本書はPersonaではない。本書の Version 1.2 / Approved は、この版番号統一の対象ではない。

[`../project-notes/DECISIONS.md`](../project-notes/DECISIONS.md) の D-005 は、検証用Personaを Version 0.1 / Draft として保全した時点の確定状態である。D-005を書き換えない。D-037 の承認と D-038 の版番号統一は、Version 3.0 / Approved の承認履歴である。D-062 が現行を Version 3.1（提案）/ Draft とした記録は、その決定時点の記録であり、原文は変更しない。現行の Document Info は Version 3.0 / Approved である。この Approved は User の版の確定であり、実動検証の完了や適用成功を意味しない。

## 6. CONFIRMED: Service Codes（サービス略号）

| Service | Code |
|---|---|
| Gemini | GM |
| ChatGPT | CG |
| Claude | CL |
| Cursor | CU |
| M365 Copilot | MC |

M365 Copilotは、現段階で専用Personaを追加しない。サービス略号だけを定義する。

AIサービスとPersonaは独立する。

ClaudeのProjectで `S-SP` を使用できるよう案内する。`M-CG` というIDは、ChatGPT専用の実行制限を意味しない。AIサービスの種類によってPersonaの役割を限定しない。

## 7. CONFIRMED: Response Identification（回答識別表示）

確定形式：

`【サービス略号/モデル名｜Persona ID@Version｜状態】`

形式の例：

`【CG/GPT-6｜M-CG@3.0｜G】`

この例は、記号の並びを示すものである。例示のモデル名と `@3.0` は、現行のPersona本文がすでにその値であることを意味しない。モデル名やVersionを推測で補完しない。

- 回答冒頭に1行表示する。
- 旧形式 `【Persona：GitHub読込済｜Version：0.1】` との二重表示はしない。
- モデル名は確認できた値のみ使用する。
- 確認できない値は `?` とする。
- Persona IDとVersionは、実際に使用するPersona本文と照合する。
- 検証用Personaの現行第16章は、本章の識別形式と第8章の取得状態を用いる。旧形式との併用はしない。検証原文の旧形式は履歴として維持し、原文は変更しない。

## 8. CONFIRMED: Acquisition Status（Persona取得状態）

第3章の M- / S- / T- はPersona分類である。本章の旗は取得状態である。二つの識別軸を混同しない。

| Flag | Meaning |
|---|---|
| G | GitHubからPersona本文を取得 |
| P | Project等の指示欄に記載されたPersona本文を使用 |
| N | Persona未読込 |
| ? | 取得元・状態が未確認 |

- 以前の提案 `G!` は採用しない。
- GitHub取得失敗と未実施の詳細は、必要に応じて検証記録で区別する。
- Gは取得成功の自己申告であり、客観的なアクセス証明ではない。
- Persona取得とPersona適用は別の事実として扱う。
- GitHub取得失敗時に、Memoryや過去の会話から本文を補完しない。
- 未取得を取得済みと報告しない。

D-005が定めた、技術的な取得証跡がない実際のGitHubアクセスはUNVERIFIEDとする扱いは維持する。本章は、その自己申告を今後の表示旗へ対応させるものであり、検証原文を改変しない。

OwnerのRepositoryはPersona本文の唯一の編集元（SSOT）として扱う。利用者のForkやコピーは独立した正本としない。G方式を使う利用者には自分専用のRepositoryの利用を強く推奨するが、必須条件にはしない。Ownerの公開Repositoryへの直接アクセスは禁止せず、P方式も選択できる。GitHubの利用制限がOwnerへ絶対に影響しないという保証はしない。Repositoryの作成や取得URLの設定方法は本書で案内しない。

## 9. CONFIRMED: Usage Recommendation（利用推奨基準）

- Main（M-）は、Ownerおよび同等の知識・運用能力を持つUserを主な対象とする。
- M-は管理・設定条件が厳しい。必要な設定ファイル等が存在しなければ、AIが停止する場合がある。
- Subset（S-）は、初心者へ推奨する機能限定版である。
- Owner以外によるM-の利用を禁止しない。
- 初心者が推奨に従わずM-を選ぶことも認める。
- 利用者は、必要な前提条件を満たさない場合に、機能制限、動作停止、操作性低下が起こり得ることを理解したうえで利用する。
- 利用経験による本人認証、およびアクセス権限制御は追加しない。
- 利用者の知識水準が不明な場合、標準案内は S- とする。Userが M- を明示指定した場合は、前提条件と注意点を案内する。知識水準だけを理由に拒否しない。
- 既存のASKME最小化原則は維持する。M/Sの選択を毎回質問しない。
- Persona設計側の不備まで、利用者の自己責任として免責する規則は設けない。
- Test（T-）は検証用途とし、通常の設定候補へ含めない。
- AIサービスの種類によってPersonaの役割を限定しない。

この基準は、Persona選択上の推奨である。GitHubの実際のアクセス制御を意味しない。利用経験や知識水準による本人認証を追加したと記録しない。M-Personaのアクセス禁止を技術的に保証したと記録しない。

第6章の独立性と矛盾しない。知識水準が不明な場合の標準案内は S- であり、使用するAIサービスでは決まらない。Userが M- を明示指定した場合は、どのAIサービスでも前提条件と注意点を案内し、知識水準だけを理由に拒否しない。AIサービスを理由に、その使用者へ案内できるPersonaを除外しない。

## 16. CONFIRMED: Persona Verification（Persona検証）

Persona Verification は、今回のPersona大改修における最優先要件である。注意書きや進捗記録では代替しない、独立した工程である。章番号は、既存のPersonaと判断履歴の参照を維持するため第16章のままとする。

Personaの識別、利用環境への適用、検証、User承認、正式運用を、次の順でつなぐ。利用環境への具体的な設定方法は本Repositoryの対象外である。

```text
Persona定義・改訂
  ↓
対象Persona・Versionの識別
  ↓
利用環境への適用（具体的な設定方法は本Repositoryの対象外）
  ↓
Persona Verification
  ├─ FAIL／検証未完了 → 修正・再検証
  └─ 検証条件を満たす → User承認判断
                              ├─ 不承認 → 修正・再検証
                              └─ 承認 → Approvedへの昇格 → 正式運用
```

FAIL、検証未完了、またはUserの不承認の戻り先は、原因に対応する修正と、Persona Verification の再実施である。

確定事項：

- 新規Personaと改訂Personaは、すべて検証対象とする。Version 3.0 への移行も検証対象に含める。
- 「重要な改訂か否か」をAIの裁量で判断して、検証工程を省略してはならない。
- 将来の対象範囲の詳細基準は UNRESOLVED として保持する。詳細基準がUser承認により確定するまでは、今回の全件対象規則を適用する。
- 検証対象であることと、検証完了であることを混同しない。
- 評価中の新規版・改訂版は Draft として扱う。
- 検証の PASS だけで Approved へ自動昇格させない。必要な実動検証とEvidence、およびUser承認を経ずに Approved へ昇格させない。
- 検証FAIL時は、原因に対応する修正と再検証を行う。変更のないEvidenceに対する無意味な再試験は要求しない。
- Persona本文の取得確認と、Personaが回答へ正しく適用されたことの検証は、別の事実である。第8章の取得状態は、適用の検証を代替しない。
- 取得成功および適用成功を、本工程の前提にしない。GitHub直接取得（G方式）は検証中であり、正式運用の前提条件としない。
- 検証には、対象Persona、Version、適用条件の特定、責務遵守、安全性、要求された動作、再現性、Evidence、合否判定を含める。
- 検証記録の保存は、[`../project-notes/DECISIONS.md`](../project-notes/DECISIONS.md) の D-005 に従う。保存先は `project-notes/persona-validation/` である。既存の検証原文は、D-044のOwner欄訂正を除き変更しない。
- この決定は、過去の Approved 版を遡及的に失効させない。既存Personaの Version と Status は、この記録では変更しない。
- 全11 Persona ID、Version 3.0 移行方針、G/P/N/?、AIサービスとPersonaの独立性は維持する。既存Personaの役割定義は変更しない。

UNRESOLVED：

次は未承認である。推測で確定しない。

- 具体的なテストケース
- 判定閾値
- 検証回数
- 将来の検証対象範囲の詳細基準
- [`../project-notes/DECISIONS.md`](../project-notes/DECISIONS.md) の D-005 で未確定の、独立したバックアップ先と方式、質問セット、実施頻度。本章では新たに決定しない。バックアップの作成と実行は、この記録の作業に含めない。

本章の記録は、検証設計の確定、実動検証の実施、Personaの Approved への昇格を意味しない。
