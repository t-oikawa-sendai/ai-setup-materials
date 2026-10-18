<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-EDU-INDEX-001 |
| Version（バージョン） | 1.1（提案） |
| Status（ステータス） | Draft |
| Created Date（作成日） | 2026-08-19 |
| Last Updated（最終更新日） | 2026-10-18 |
| Owner（管理者） | Takashi Oikawa |
| Related Documents（関連文書） | [`../../README.md`](../../README.md)<br>[`../PERSONA_IDENTIFICATION_AND_SETUP.md`](../PERSONA_IDENTIFICATION_AND_SETUP.md)<br>[`GEM_RESEARCHER_FULL.md`](GEM_RESEARCHER_FULL.md)<br>[`GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`](GEM_RESEARCHER_LEARNING_DEVELOPMENT.md)<br>[`GEM_RESEARCHER_DEVELOPMENT.md`](GEM_RESEARCHER_DEVELOPMENT.md)<br>[`GEM_SOLUTION_PARTNER.md`](GEM_SOLUTION_PARTNER.md)<br>[`GEM_CODE_GENERATOR.md`](GEM_CODE_GENERATOR.md)<br>[`GEM_REVIEWER.md`](GEM_REVIEWER.md)<br>[`SKILLS/RESEARCHER_LEARNING.md`](SKILLS/RESEARCHER_LEARNING.md)<br>[`SKILLS/RESEARCHER_DEVELOPMENT.md`](SKILLS/RESEARCHER_DEVELOPMENT.md)<br>[`SKILLS/RESEARCHER_CAREER.md`](SKILLS/RESEARCHER_CAREER.md)<br>[`SKILLS/SOLUTION_PARTNER.md`](SKILLS/SOLUTION_PARTNER.md)<br>[`SKILLS/CODE_GENERATOR.md`](SKILLS/CODE_GENERATOR.md)<br>[`SKILLS/REVIEWER.md`](SKILLS/REVIEWER.md) |

前版の承認履歴は Version 1.0 / Status Approved である。この改訂は Version 1.1（提案）/ Status Draft である。Skillsの実登録と実動検証は未実施であり、この Draft の正式な Approved ではない。

---

# Education Personas（教育用Persona）

## 1. Purpose（目的）

このディレクトリは、職業訓練校の `User（生徒）` が調査、設計、コード生成、レビューをAIに役割分担させるためのPersona正本を管理します。

Education用の基本体系は4役割です。

`User（生徒）` が各役割のAIを操作し、各出力を確認して、次の工程に必要な確定情報を手動で渡します。各役割のAIが自動的に作業を転送したり、最終判断を行ったりする運用ではありません。

### Gemini Skillsと本教材の運用方針

本教材は、自己正当化バイアス（誤りの連鎖）と自己選好バイアスへの対策として、調査・設計・コード生成・レビューの役割を分け、評価の独立性を高めることを重視します。

Gemini Skillsの再利用性を活用したい場合は、各Education Personaを対応するSkillとして用意し、使い分けることもできます。ただし、同一アカウント内でSkillsを使い分ける運用では、本教材が求める評価の独立性を満たせないと判断します。役割別のSkillを設けても、自己正当化バイアス（誤りの連鎖）と自己選好バイアスという二つの懸念は残ります。同一アカウント内のReviewer Skillによる判定を、独立したレビューが成立した根拠とは扱いません。

Gemini Skillsで本設計思想に沿った役割分離を図る場合は、役割ごとにアカウントを分け、`User（生徒）` が各工程で確定した成果物とEvidenceを選んで引き渡すことを必要条件とします。アカウントを分けるだけでバイアスの解消が保証されるわけではありません。Evidenceの確認と最終判断は `User（生徒）` が行います。

筆者の見解では、ChatGPTまたはClaudeのProjectを役割ごとに分けて運用する方法が、本設計思想により適合します。その場合も、会話・参照資料・記憶の扱いを確認し、工程間の引き継ぎを `User（生徒）` が管理します。

この節は運用方針です。Skillの登録完了、動作確認、評価独立性の実証を示すものではありません。

Personaそのものがなぜ重要なのか、サービス全体のカスタム指示・共通設定やその都度のプロンプトと何が違うのかは、Repository共通の説明として [`../../README.md`](../../README.md) の `Why Persona Matters（なぜPersonaが重要なのか）` を参照してください。

Personaの識別と検証の共通仕様は [`../PERSONA_IDENTIFICATION_AND_SETUP.md`](../PERSONA_IDENTIFICATION_AND_SETUP.md) にあります。Education用の基本4役割と各Personaの責務は変更していません。サービスごとの設定方法は本Repositoryの範囲外です。

## 基本4役割（サービス非依存）

| 役割 | 主な責務 |
|---|---|
| Researcher | 外部情報を調査し、確認済み事実とEvidenceを提示する |
| Solution Partner | 目的・要求・制約を整理し、設計する |
| Code Generator | 確定した設計に基づき、コード・testコードの生成を支援する |
| Reviewer | 設計・コード・検証Evidenceを独立して評価する |

これらの4役割は、GeminiのGemやSkillsだけに限定されません。`GEM_` で始まるPersonaファイル名は従来の開発・運用経緯による名称であり、利用可能なAIサービスを制限するものではありません。

従来の4Gem＋1構成と、SKILLSの基本4役割・合計6 Skillsは、基本4役割を利用する方式の違いです。構成の違いだけで評価の独立性が実証されたとは扱いません。6つのSkill定義は Draft であり、実登録と実動検証は未実施です。

## 2. SKILLS Configuration（基本4役割・合計6 Skills）

> [!IMPORTANT]
> **重要：GEM版とSKILLS版のPersona機能本文は同一です。**
>
> 役割・責務・判断基準・Evidence規則・回答規則は変更しません。
>
> 違いは利用方式です。GEM固有の手動切替案内などは、Persona機能本文の一致判定に含めません。
>
> Researcherは既存の共通本文とModuleを、Learning・Development・Careerの3用途に再編しています。

対象は職業訓練校の生徒です。設計目的は、Skillの自動適用を使い、生徒が毎回Researcher Personaを明示選択する負担を減らすことです。

`SKILLS/` はPersona定義の管理場所です。Geminiの画面操作手順やサービス設定資料は作成しません。

Skillsの実登録、自動選択精度の実動検証、Deep Research連携は未実施です。講師本人がGemini Skillsを利用して実動検証したことは、前提にしません。

同一Geminiアカウント内で、設計・コード生成・レビューのSkillsを使い分けるだけでは、本教材が要求する評価の独立性は成立しません。実運用で独立レビューを成立させる場合は、役割ごとにアカウントを分け、`User（生徒）` が各工程で確定した成果物とEvidenceを選んで引き渡します。アカウントを分けるだけでバイアスの解消は保証しません。

| Skill | ファイル | 役割 |
|---|---|---|
| Researcher（学習調査） | [`RESEARCHER_LEARNING.md`](SKILLS/RESEARCHER_LEARNING.md) | 学習調査 |
| Researcher（設計・開発調査） | [`RESEARCHER_DEVELOPMENT.md`](SKILLS/RESEARCHER_DEVELOPMENT.md) | 設計・開発調査 |
| Researcher（就職活動調査） | [`RESEARCHER_CAREER.md`](SKILLS/RESEARCHER_CAREER.md) | 就職活動調査 |
| Solution Partner | [`SOLUTION_PARTNER.md`](SKILLS/SOLUTION_PARTNER.md) | 要求整理・設計 |
| Code Generator | [`CODE_GENERATOR.md`](SKILLS/CODE_GENERATOR.md) | コード生成 |
| Reviewer | [`REVIEWER.md`](SKILLS/REVIEWER.md) | 評価・レビュー |

### GEM／SKILLS対応表

| GEM側のPersona | SKILLS側のPersona | 対応関係 |
|---|---|---|
| [`GEM_RESEARCHER_FULL.md`](GEM_RESEARCHER_FULL.md) | [`RESEARCHER_LEARNING.md`](SKILLS/RESEARCHER_LEARNING.md) / [`RESEARCHER_CAREER.md`](SKILLS/RESEARCHER_CAREER.md) / [`RESEARCHER_DEVELOPMENT.md`](SKILLS/RESEARCHER_DEVELOPMENT.md) | 共通本文と用途別Moduleを継承 |
| [`GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`](GEM_RESEARCHER_LEARNING_DEVELOPMENT.md) | [`RESEARCHER_LEARNING.md`](SKILLS/RESEARCHER_LEARNING.md) / [`RESEARCHER_DEVELOPMENT.md`](SKILLS/RESEARCHER_DEVELOPMENT.md) | 2用途を分離 |
| [`GEM_RESEARCHER_DEVELOPMENT.md`](GEM_RESEARCHER_DEVELOPMENT.md) | [`RESEARCHER_DEVELOPMENT.md`](SKILLS/RESEARCHER_DEVELOPMENT.md) | Persona本文を継承 |
| [`GEM_SOLUTION_PARTNER.md`](GEM_SOLUTION_PARTNER.md) | [`SOLUTION_PARTNER.md`](SKILLS/SOLUTION_PARTNER.md) | Persona本文は同一 |
| [`GEM_CODE_GENERATOR.md`](GEM_CODE_GENERATOR.md) | [`CODE_GENERATOR.md`](SKILLS/CODE_GENERATOR.md) | Persona本文は同一 |
| [`GEM_REVIEWER.md`](GEM_REVIEWER.md) | [`REVIEWER.md`](SKILLS/REVIEWER.md) | Persona本文は同一 |

6ファイルはいずれも Draft です。Document ID は、2026-08-22の採番一覧から一意に決まらないため UNRESOLVED です。推測で採番していません。

## 3. 4Gem＋1 Configuration（従来の4Gem＋1構成・参考記録）

従来のGem構成では、詳細調査用としてResearcher Personaを使う `Researcher Deep Research` を1つ追加する **4Gem＋1** の設計です。

以下の4Gem＋1は従来の承認済み構成であり、現在の生徒向け新規導入手順ではありません。画面上の新しい導入手順は、本書では定めません。

2026-10-18時点の[Google公式案内](https://support.google.com/gemini/answer/18560919?hl=ja)では、Gemの提供終了予定はアカウント種別により異なります。個人のGoogleアカウントは2026年11月、Workspace Business・Enterprise・Non-Profitは2027年3月、Workspace Educationは2027年6月です。提供終了に伴い、GemはSkillとして自動的に再作成される予定も案内されています。本教材の対象アカウント種別は未確認です。この公式予定は、既存Gemを現に利用・編集できることの確認ではありません。

2026-10-16のUser実機確認では、本教材の講師・生徒アカウントでGemを新規作成できませんでした。2026-10-18のUser実機確認では、確認した環境でGemの表示がなく、Skillsへ変更されていました。これらは当該環境の観測であり、公式の提供終了予定とは別です。既存Gemの利用・編集可否は未確認のままです。

従来の基本4Gemは次の4つです。

| Gem Display Name（Gem表示名） | Persona File（Personaファイル） | Primary Responsibility（主な責務） |
|---|---|---|
| Researcher | 下記3完成版から1本を選択 | 必要な外部情報を一次情報中心に調査し、確認済み事実とEvidenceを渡す |
| Solution Partner | [`GEM_SOLUTION_PARTNER.md`](GEM_SOLUTION_PARTNER.md) | 目的、要求、制約を整理し、設計とコード生成用指示を具体化する |
| Code Generator | [`GEM_CODE_GENERATOR.md`](GEM_CODE_GENERATOR.md) | 現行設計と仕様に従い、コード・testコードの生成、解析、修正を支援する |
| Reviewer | [`GEM_REVIEWER.md`](GEM_REVIEWER.md) | 設計、コード、User（生徒）が作成した検証Evidenceを独立して評価する |

従来構成では、詳細調査用として次の1Gemを追加する設計でした。

| Additional Gem（追加Gem） | Persona | Purpose（用途） |
|---|---|---|
| Researcher Deep Research | Researcherと同じ選択済みPersona | Deep Researchを使う企業研究・業界研究・比較調査などの詳細調査 |

`Researcher Deep Research` は新しいPersonaではありません。Researcher Personaを使用する従来の追加Gemです。

## 4. Selecting a Researcher Edition（GEM側のResearcher完成版・参考記録）

従来のGem構成では、調査範囲の異なる完成版が3つあります。その運用では、`User（生徒）` が調査範囲に応じて、次の完成版から1版を明示選択します。これらのファイルは変更せず保全します。SKILLS側のResearcherは、第2節の3つのSkillです。

- [`GEM_RESEARCHER_FULL.md`](GEM_RESEARCHER_FULL.md)：Learning / Career / Development
- [`GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`](GEM_RESEARCHER_LEARNING_DEVELOPMENT.md)：Learning / Development
- [`GEM_RESEARCHER_DEVELOPMENT.md`](GEM_RESEARCHER_DEVELOPMENT.md)：Development

従来の4Gem＋1構成では、通常調査とDeep Researchに同じResearcher完成版を使う設計でした。複数の完成版を同時に混在させる設計ではありません。

Deep ResearchをSkillsから利用できるとは扱いません。2026-10-18時点の[Google公式案内](https://support.google.com/gemini/answer/18560919?hl=ja)では、SkillsはDeep Researchにはまだ対応していません。2026-10-16時点の同旨の記載は、その時点の記録として残します。当時の記載は、その作業で公式案内を改めて取得したものではありません。

## 5. User-first Basic Flow（User-firstの基本フロー）

```text
User（生徒）が目的・要求を整理する
  ↓
必要に応じてResearcherで外部情報を調査する
  ↓ User（生徒）が確認済み事実とEvidenceを確認して渡す
Solution Partnerで要求・制約・設計を具体化する
  ↓ User（生徒）が現行設計とコード生成用指示を確認して渡す
Code Generatorでコードまたはtestコードの生成支援を受ける
  ↓
User（生徒）がコードをIDEへ反映し、実行、test、動作確認を行う
  ↓ User（生徒）が検証Evidenceを作成して提出する
Reviewerが設計、コード、検証Evidenceを評価する
  ↓ レビュー結果は最初にUser（生徒）へ返る
User（生徒）が修正方法、再提出、採用、完成を最終判断する
```

Researcherは必要な場面で利用し、常に直列で呼び出す必要はありません。従来の4Gem＋1構成では、通常の調査に `Researcher`、企業研究・業界研究・比較調査など複数情報源を横断する詳細調査に `Researcher Deep Research` を使い分ける設計でした。

各役割のAIへ過去の会話を丸ごと渡すのではなく、その工程に必要な現行の要求、仕様、設計、Evidenceだけを `User（生徒）` が選んで渡します。

## 6. Responsibility Boundaries（責務境界）

- Solution Partnerは設計を具体化しますが、完成コードの生成や最終判断は行いません。
- Code Generatorはコード・testコードの生成までを支援します。IDE操作、実環境への適用、実行、test結果確認、動作確認、検証Evidence作成、品質保証判定は行いません。
- User（生徒）が、生成コードをIDEへ反映し、実行、test、動作確認、Evidence作成を行います。
- Reviewerは、Solution Partnerの設計成果物、Code Generatorが生成したコード、User（生徒）が作成したEvidenceを評価し、結果を最初にUser（生徒）へ返します。
- コードに修正が必要な場合、User（生徒）が自力で修正するか、Code Generatorの支援を使うかを選びます。
- 設計に再検討が必要な場合、User（生徒）は必要に応じてSolution Partnerの支援を利用できます。
- 各役割のAIの出力を確認し、次の作業、採用、完成を最終判断するのは `User（生徒）` です。

## 7. Reviewer Judgment（Reviewerの判定）

Reviewerは、次の4段階で判定します。

- `PASS`
- `PASS WITH NOTES`
- `REWORK REQUIRED`
- `BLOCKED`

判定の詳細、出力項目、修正案、Evidence不足時の案内は [`GEM_REVIEWER.md`](GEM_REVIEWER.md) と [`SKILLS/REVIEWER.md`](SKILLS/REVIEWER.md) を参照してください。Reviewerの判定はUser（生徒）の最終判断に代わるものではありません。

## 8. Evidence and Canonical Sources（Evidenceと正本）

Evidenceとは、判断、確認、検証結果を追跡できる根拠です。初心者向けには「確認に必要な記録・資料」と考えてください。

- Researcher：情報源、参照先、確認した内容
- Solution Partner：User（生徒）が示した要求、制約、確認済み事実、採用・不採用理由
- Code Generator：入力された設計・仕様、対象、変更範囲、コード解析の根拠、仮定、未確認事項
- User（生徒）：実行したtestの結果、ビルド結果、画面・実機・API等の動作確認結果
- Reviewer：対象箇所、仕様・設計との不一致、検証結果、指摘根拠

会話そのものを正本にせず、現在有効な要求、仕様、設計、判断、検証結果を追跡できる文書や成果物へ反映します。
Evidenceのない「確認済み」「完了」「問題なし」という断定は避けます。

## 9. Common Principles（共通原則）

- 確定事項、未確認事項、仮定を分離する。
- 各役割のAIは自分の責務を越えて、他工程の最終判断を行わない。
- 不要な機能追加、過剰な抽象化、根拠のない仕様補完を行わない。
- 問題を指摘する場合は、理由と影響を示す。
- パスワード、APIキー、接続情報などの秘密情報を、入力、出力、ログ、公開物へ含めない。

## 10. Scope（本書の範囲）

本書はPersonaの役割、効果、責務境界、現行の運用方針と、従来構成を説明します。AIサービスの設定方法は扱いません。Gemini Skillsと役割分離の現行運用方針は [`../../project-notes/DECISIONS.md`](../../project-notes/DECISIONS.md) の D-048 に記録します。GEMとSKILLSの構成は同ファイルの D-058 に記録します。旧Gemini設定資料の判断履歴は同ファイルの D-045 に保全します。
