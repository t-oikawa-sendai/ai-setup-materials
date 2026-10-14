<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-IDENTIFICATION-SETUP-001 |
| Version（バージョン） | 1.0 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-10-14 |
| Last Updated（最終更新日） | 2026-10-14 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | [`../AGENTS.md`](../AGENTS.md)<br>[`../README.md`](../README.md)<br>[`education/README.md`](education/README.md)<br>[`reference/README.md`](reference/README.md)<br>[`../project-notes/DECISIONS.md`](../project-notes/DECISIONS.md)<br>[`../project-notes/CURRENT.md`](../project-notes/CURRENT.md) |

---

# Persona Identification and Setup（Persona識別と設定案内）

## 1. Purpose（目的）

この文書は、Personaの識別体系と、Project・Gem等への設定案内の共通仕様の正本である。

2026-10-14にUserが決定した内容を記録する。判断履歴は [`../project-notes/DECISIONS.md`](../project-notes/DECISIONS.md) の D-006〜D-018 に記録する。本書は判断履歴の代替ではない。

この文書の `Version 1.0 / Status Approved` は、本章から第12章の確定仕様を正本として記録したことを示す。次を意味しない。

- 全11 Personaの本文とDocument Infoを Version 3.0 へ更新したこと
- 既存の Draft または Approved を、Version変更だけで昇格したこと
- 設定案内専用Personaの本文を作成し、承認したこと
- 各AIサービスでの実動検証が完了したこと
- 指示欄用完成文のファイルを作成したこと

本書は education と reference の双方に適用する。Persona本文ではないため、区分ディレクトリのPersona本体へ置かない。AIサービス固有の手順ではないため、`personas/<区分>/setup/` へ置かない。新しいディレクトリは作らない。

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
- `Researcher Deep Research` は独立Personaではない。第4章の11件に含めない。Researcher Personaを使う追加Gemとして、既存のEducation運用を維持する。

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

`T-IT-ADVISOR` は確定Persona IDである。現行の [`reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md`](reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md) 本文には、移行前の識別子 `IT-GENERAL-ADVISOR-TEST` が残っている。本文は今回変更しない。現行本文の識別子を、確定Persona IDへ置き換わったものとして扱わない。

Researcher 3ファイルの現行見出しは、いずれも Researcher Persona である。Education README上の選択は、FULLが Learning / Career / Development、LEARNING_DEVELOPMENTが Learning / Development、DEVELOPMENTが Development である。この選択関係を、MainとSubsetの1対1対応表として扱わない。

## 5. CONFIRMED: Version 3.0 Migration（Version 3.0への移行方針）

- 全11 Personaを新共通基準のVersion `3.0` へ統一することを決定済みである。
- 共通基準としてVersion 2.0を採用せず、Version 3.0を新しい基点とする。
- 旧2.x系列は歴史的に存在するため、過去履歴を削除・書き換えしない。
- 既存のDraft・Approved状態を、Version変更だけで自動昇格させない。
- 今回記録するのは移行仕様である。実際の全Persona本文とDocument Infoの更新は別工程であり、未実施である。
- 移行前のVersionと移行後のVersionを混同しない。第4章の表は移行前である。移行後の共通Versionは `3.0` である。

[`../project-notes/DECISIONS.md`](../project-notes/DECISIONS.md) の D-005 は、検証用Personaを Version 0.1 / Draft として保全した時点の確定状態である。Version 3.0 は、その後に決めた移行先である。D-005を書き換えない。移行は未実施のため、当該Personaの現行Document Infoは Version 0.1 / Draft のままである。

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
- 現行の検証用Persona本文には旧形式の指示が残っている。本文は今回変更しない。新しい形式の適用は、本文更新の別工程である。検証原文の旧形式は履歴として維持する。

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

この基準は、Persona設定案内上の推奨である。GitHubの実際のアクセス制御を意味しない。利用経験や知識水準による本人認証を追加したと記録しない。M-Personaのアクセス禁止を技術的に保証したと記録しない。

第6章の独立性と矛盾しない。知識水準が不明な場合の標準案内は S- であり、使用するAIサービスでは決まらない。Userが M- を明示指定した場合は、どのAIサービスでも前提条件と注意点を案内し、知識水準だけを理由に拒否しない。AIサービスを理由に、その使用者へ案内できるPersonaを除外しない。

## 10. CONFIRMED: Instruction Text Management（指示欄用文章の管理）

従来のRepositoryは、Persona本文と設定方法の資料を中心に管理していた。

今後は、各AIサービスのProject・Gem等の指示欄に直接記載する完成済み文章も、必須の管理対象とする。

管理上の要件：

1. Persona本文と指示欄用文章を区別する。
2. GitHub取得方式（G）と直接記載方式（P）に対応する。
3. Persona本文は既存正本を使用し、独立した編集元を増やさない。
4. 利用者に複数資料から指示文を組み立てさせない。
5. そのままコピーできる完成文を提供する。
6. 指示文の共通部分とサービス固有部分を識別できるようにする。
7. サービスの現行仕様で実現できない機能を保証しない。
8. 既存のPersona本文と、サービス固有セットアップ手順の責務分離を維持する。

過去に検討した「9パターン」「17パターン」は、確定文書数ではない。

完成文の生成・管理方式と必要ファイル数は、詳細設計の対象であり、UNRESOLVEDである。この記録では完成文ファイルを作成しない。

サービス固有のセットアップ手順の既存正本は、次のまま維持する。本書へ手順を移さない。

- [`education/setup/GEMINI_GEM_SETUP.md`](education/setup/GEMINI_GEM_SETUP.md)
- [`reference/setup/CLAUDE_CODE_SETUP.md`](reference/setup/CLAUDE_CODE_SETUP.md)

### 10.1 Distribution Source Protection（配布元の保護）

Owner自身のGitHubおよびAI利用の保護を、運用上の最優先とする。他のUserによるGitHub取得の制限または失敗は許容する。

この節は、G方式とP方式を継続したまま、取得先Repositoryの扱いを定める。GitHubのアクセス制御、認証機能、新しい配布システム、自動同期機構は追加しない。GitHub取得の具体的な実装方式は、第13章の未確定事項のままとする。

- OwnerのRepositoryは、Persona本文の唯一の編集元（SSOT）として維持する。UserによるForkやコピーは、正本の独立した編集元としない。
- G方式を継続して使いたいUserには、自分専用のGitHub Repositoryを作成することを強く推奨する。この推奨は必須条件ではない。
- Userは、自分のRepositoryにPersonaを配置し、自分のAIにはそのRepositoryのURLを設定する。
- 自分のRepositoryを参照する設定では、OwnerのRepositoryへの取得URLが残らないよう案内する。
- User側Repositoryの管理、更新、およびアクセス制限への対応は、各Userの責任とする。
- UserによるOwnerのPublic Repositoryへの直接アクセスは禁止しない。
- P方式も継続して提供する。
- GitHubの利用制限がOwnerへ絶対に影響しないという技術的保証はしない。

## 11. CONFIRMED: Setup Guidance（Persona設定案内の要求仕様）

利用者はPersona IDを知らなくてもよい。

自然文の依頼から、用途、Persona、AIサービス、取得方式を特定し、設定まで案内する。

### 11.1 Basic Flow（基本フロー）

1. Userの作成目的を理解する。
2. 目的に適したPersonaを、第9章の利用推奨基準に従って選定する。
3. 使用AIサービスを確認する。
4. G/P方式を確認する。G方式を継続して使う場合は、第10.1節に従い、User専用のGitHub Repositoryの作成を強く推奨する。この推奨は必須条件にしない。Userが自分のRepositoryを参照する設定を選んだ場合は、そのURLを設定し、OwnerのRepositoryへの取得URLが残らないよう案内する。OwnerのPublic Repositoryへの直接アクセスは禁止しない。P方式も継続して案内する。
5. 設定手順と指示欄用完成文を提示する。
6. 動作確認方法を案内する。

質問順序を機械的に固定せず、既に判明している事項は再質問しない。

### 11.2 ASKME

- 情報不足の場合のみASKMEを行う。
- 必要最小限の事項だけ質問する。
- 一意に判定できるPersonaを再選択させない。
- M/Sの選択を毎回質問しない。利用者の知識水準が不明な場合、標準案内は第9章に従い S- とする。Userが M- を明示指定した場合は、前提条件と注意点を案内し、知識水準だけを理由に拒否しない。
- 同じ質問を繰り返さない。
- 不明なPersona名は、ID対応表と現行Personaから確認する。
- AIサービスとPersonaの役割を結びつけて候補を制限しない。
- 第10.1節の専用Repository作成は強い推奨である。未作成であることだけを理由にG方式の案内を止めない。OwnerのPublic Repositoryへの直接アクセスを拒否しない。

### 11.3 Examples（会話による具体例）

例A：目的が明確な問い合わせ。

依頼の例：「GitHubで管理するペルソナを読み込む仕様のSolution Partnerのプロジェクトを作りたい」

判定：

- Persona：S-SP
- 取得方式：G
- AIサービス：Project等の文脈から特定できる場合は追加質問不要。特定できなければ確認する。

例B：目的が不明な問い合わせ。

依頼の例：「プロジェクトを作りたい」

目的が不明なため、必要事項をASKMEする。

Userの回答例：「PFを作成する設計の相談相手」

この回答例では、利用者の知識水準は不明であり、M- の明示指定もない。第9章に従い、標準案内は S-SP とする。さらにUserが「Claude」を選択した場合、Claudeを利用環境として扱う。Claude用という理由で S-SP を除外しない。Userが M- を明示指定した場合は、第9章に従い前提条件と注意点を案内し、知識水準だけを理由に拒否しない。

例C：取得方式。

例Bの続きとして、Userが「G方式」を選択した場合、Claude向けに S-SP のGitHub取得用設定手順と指示欄用完成文を提示する。G方式を継続して使う場合は、第10.1節に従い、User専用のGitHub Repositoryの作成を強く推奨する。この推奨は必須条件ではない。Userが自分のRepositoryを参照する設定を選んだ場合は、そのRepositoryのURLを設定し、OwnerのRepositoryへの取得URLが残らないよう案内する。OwnerのPublic Repositoryへの直接アクセスは禁止しない。P方式へ切り替えることもできる。

例Cが求める完成文は、第10章のとおり未作成である。例示は案内の要求であり、完成文が既にRepositoryへ存在することを意味しない。

### 11.4 Completion（完了条件）

設定案内において、次を提供する。

- 選択したPersona IDと名称
- 使用するAIサービス
- 取得方式
- G方式でUser自身のRepositoryを参照する場合は、そのRepositoryのURL。この場合、OwnerのRepositoryへの取得URLは残さない
- Project等の作成手順
- 指示欄へコピーする完成文
- 動作確認用プロンプト

実際の適用成功は、別途検証する。本章の記録は、適用成功の検証完了を意味しない。

## 12. CONFIRMED: Dedicated Setup Persona（設定案内専用Personaの新設方針）

Userは、Personaの設定案内だけを担当する専用Personaの新設を指示した。この新設方針は確定事項である。

名称、Persona ID、本文、配置は第13章の未確定事項である。第4章の11 IDへ加えない。

### 12.1 Responsibilities（責務）

- プロジェクト・Gem等のPersona利用環境の設定案内
- Userの目的からのPersona選定
- 必要最小限のASKME
- Persona IDとGitHub正本の対応確認
- G/P方式の選択支援
- AIサービス固有の設定手順
- 指示欄へ貼る完成文
- 設定後の動作確認方法

### 12.2 Out of Scope（対象外）

- PFやアプリケーションそのものの設計
- プログラミング・コード生成
- ソフトウェア実装
- コードレビュー
- 一般的なIT相談
- Persona本文の無断変更
- Git操作の無断実行

## 13. PROPOSED / UNRESOLVED（未確定事項）

以下はChatGPTの初稿であり、Userの個別承認を受けていない。PROPOSED / UNRESOLVED として保持する。

- 名称案：Persona Setup Advisor
- Persona ID案：S-SETUP
- 新規PersonaのDocument Info
- 新規Persona本文の最終構成
- 正本ファイルの配置先
- GitHub取得の具体的な実装方式
- 共通指示文とサービス別派生文の最終構成
- 新Personaの実動検証条件
- 指示欄用完成文の生成・管理方式と必要ファイル数

`S-SETUP` を承認済みIDとして扱わない。Version 3.0 を新設Personaへ無条件に適用しない。Approvedへ昇格しない。新規Persona本文の正式実装は、今回の対象外であり未実施である。

## 14. Boundaries（既存Personaとの責務境界）

既存11 Personaの責務は、各本文のまま維持する。本書は、識別、利用推奨基準、設定案内、指示欄用文章の管理を定める。Researcher、Solution Partner、Code Generator、Reviewer、中核4種、検証用Personaの役割定義を変更しない。

設定案内専用Personaの対象外は、第12.2節のとおりである。対象外の作業を、本書で既存Personaへ割り当て直さない。既存本文の責務を維持する。

Education用4Gem＋1の構成と利用手順は変更しない。`Researcher Deep Research` は独立Personaのままにしない。

## 15. Not Done（この記録では未実施）

- 全11 Personaの本文、Version、Status、Document IDの変更
- 旧形式から新形式への、Persona本文上の置換
- 設定案内専用Personaの本文作成
- 指示欄用完成文ファイルの作成
- 各AIサービスへの登録と実動検証
- 「9パターン」「17パターン」の文書数としての採用
