<details>
<summary>Document Info（文書情報）</summary>

| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-INDEX-001 |
| Version（バージョン） | 1.5（提案） |
| Status（ステータス） | Draft |
| Created Date（作成日） | 2026-08-17 |
| Last Updated（最終更新日） | 2026-10-18 |
| Owner（管理者） | Takashi Oikawa |
| Related Documents（関連文書） | [`personas/education/README.md`](personas/education/README.md)<br>[`personas/WHY_PERSONA_MATTERS.md`](personas/WHY_PERSONA_MATTERS.md)<br>[`personas/AI_ISSUES_EVIDENCE.md`](personas/AI_ISSUES_EVIDENCE.md)<br>[`personas/reference/README.md`](personas/reference/README.md)<br>[`personas/reference/PERSONA_OPERATION_CASE_STUDY.md`](personas/reference/PERSONA_OPERATION_CASE_STUDY.md)<br>[`personas/PERSONA_IDENTIFICATION_AND_SETUP.md`](personas/PERSONA_IDENTIFICATION_AND_SETUP.md)<br>[`project-notes/2026-09-11-code-generator-5-pattern-comparison-reference.md`](project-notes/2026-09-11-code-generator-5-pattern-comparison-reference.md) |

</details>

前版の承認履歴は Version 1.4 / Status Approved（D-052）である。この改訂は Version 1.5（提案）/ Status Draft である。修正方針の承認は、この Draft の正式な Approved、または研究結果の検証合格ではない。

---

# AI Setup Materials — Personaの意義・効果と役割分離

このRepositoryは、AIに「調査・設計・コード生成・レビュー」の役割を分ける理由、期待できる効果と限界を説明し、Persona本文と検証Evidenceを公開します。AIサービス別の設定方法は扱いません。

*本ドキュメントは入門的ガイダンス（Primer）であり、実運用レベルの標準仕様ではありません。*

---

## この資料で扱う2つの時間軸

この表は、本教材の中での構成の変遷を示します。全Googleアカウントが2026年10月までにSkillsへ移行したという意味ではありません。

| 時間軸 | 内容 | この教材での扱い |
|---|---|---|
| 従来構成 | GeminiのGemを使った4Gem＋1構成 | 過去の設計・関連検証記録。現行の新規導入手順ではない |
| SKILLS構成 | 基本4役割・合計6 Skills | Persona定義はDraft。実登録・自動選択の実動検証は未実施 |

2026-10-18時点の[Google公式案内](https://support.google.com/gemini/answer/18560919?hl=ja)では、Gemの提供終了予定はアカウント種別により異なります。個人のGoogleアカウントは2026年11月、Workspace Business・Enterprise・Non-Profitは2027年3月、Workspace Educationは2027年6月です。提供終了に伴い、GemはSkillとして自動的に再作成される予定も案内されています。本教材の対象アカウント種別は未確認です。この公式予定から、既存Gemの利用・編集可否を確認済みとは扱いません。

2026-10-16のUser実機確認では、対象の講師・生徒アカウントでGemを新規作成できませんでした。2026-10-18のUser実機確認では、確認した環境でGemの表示がなくSkillsへ変更されていました。これらは当該環境の観測であり、公式の提供終了予定とは別です。**4Gem＋1は現在の新規導入手順ではありません。**

---

<a id="start-here"></a>
## Start Here（目的別入口）

| 確認したいこと | 最初に読む場所 |
|---|---|
| AIの問題点と、Personaによる役割分離の意義 | [AI利用時の課題](#challenges-in-ai-use) → [なぜPersonaが重要なのか](#why-persona-matters) |
| 現在のSkills環境で注意すべき評価の独立性 | [Gemini Skillsの警告](#gemini-skills-and-role-separation) ／ [`Education README`](personas/education/README.md) |
| Education Personaの4役割、6 Skills、従来の4Gem＋1構成 | [`Education README`](personas/education/README.md)（従来構成は新規導入手順ではない） |
| Reference Personaと実務の役割分担 | [`Reference README`](personas/reference/README.md) |
| Personaの識別・検証仕様 | [`PERSONA_IDENTIFICATION_AND_SETUP.md`](personas/PERSONA_IDENTIFICATION_AND_SETUP.md) |
| Personaあり／なしの比較資料 | [検証例の案内](#persona-ab-code-generator) |

ReferenceのAI運用資料は、**Case Study → Prompt Template → Handoff Template** の順で参照できます。

## Contents（目次）

- [Start Here（目的別入口）](#start-here)
- [1. Target Users（対象者）](#target-users)
- [2. Challenges in AI Use（AI利用時の課題）](#challenges-in-ai-use)
- [3. Why Persona Matters（なぜPersonaが重要なのか）](#why-persona-matters)
  - [Gemini Skillsの利用と、AIの役割分離について](#gemini-skills-and-role-separation)
  - [3.1 Personaあり／なしの検証例](#persona-ab-code-generator)
- [4. Role of User（Userの役割）](#role-of-user)
- [5. Structure（構成）](#structure)
- [6. Education Skills（基本4役割・合計6 Skills）](#education-4skills)
  - [6.1 基本4役割と6 Skills](#education-4skills-overview)
  - [6.2 Researcherの3 Skills](#education-4skills-researcher)
  - [6.3 Deep Researchの制約](#education-4skills-deep-research)
  - [6.4 評価の独立性への注意](#education-4skills-independence)
  - [6.5 従来の4Gem＋1構成（参考記録）](#education-4gem-plus-1)
- [7. Quick Start（利用の入口）](#quick-start)
- [8. Prerequisites and Notes（前提と注意事項）](#prerequisites-and-notes)
- [9. License（ライセンス）](#license)

<a id="target-users"></a>
## 1. Target Users（対象者）

職種・所属・AI経験を問わず、次の目的を持つUserを対象とします。

- プロンプトエンジニアリングの一要素として、AIの役割・責務を設計する考え方を理解したい
- AIの応答、自身の業務や学習の目的に合わせて使いやすくしたい
- AIの判断基準、回答形式、検証の観点を明確にし、出力を確認・評価しやすくしたい
- 事実誤認や根拠不足を見つけ、回答の質を高めたい
- 調査・設計・実装・レビューの責務を分け、評価の独立性を高めたい

Education Personaには職業訓練校向けの設計も含みますが、Repository全体を教育用途には限定しません。

<a id="challenges-in-ai-use"></a>
## 2. Challenges in AI Use（AI利用時の課題）

生成AIの問題を、本教材の設計目的に沿って4つに分けます。

**情報・回答の正確性**

- **ハルシネーション**：事実ではない内容を、もっともらしく断定する
- **LITM（Lost in the Middle）**：長い入力の中ほどにある情報を見落としやすい
- **知識の古さ**：学習時点より新しい情報を知らず、新しいバージョンを「存在しない」と断定することがある
- **推測による補完**：曖昧な依頼の不足部分を、確認せずに推測で埋める

**対話時の判断の偏り**

- **迎合（Sycophancy）**：ユーザーの誤った主張や期待に合わせて、回答を曲げる

**自己評価・レビューの独立性に関わる偏り**

- **自己正当化バイアス（誤りの連鎖）**：先の回答に誤りがあっても、その回答を前提に説明を続け、さらに誤った内容を重ねることがある
- **自己選好バイアス**：AI自身が生成した内容を、他の内容より高く評価しやすい

**指示遵守・作業実行・検証**

- **指示遵守の非保証**：Userの指示に対する遵守が毎回保証されないことは、現在のLLMの根本的な信頼性問題の一つである。AIが指示や規則を理解・説明できることと、それらを実際に安定して守れることは別である。
- **指示範囲外の変更**：頼んでいない箇所まで修正・追加する
- **未検証の完了報告**：実行していないのに「完了」「テスト成功」と報告する

本教材のPersonaは、これらの問題の影響を軽減することを目的として設計しています。AIの出力はUserが確認します。各項目の根拠・研究条件・限界は[AI利用時の課題：Evidence集](personas/AI_ISSUES_EVIDENCE.md)を参照してください。

<a id="why-persona-matters"></a>
## 3. Why Persona Matters（なぜPersonaが重要なのか）

研究では、誤った回答を前提に説明を重ねる現象（本教材では『自己正当化バイアス（誤りの連鎖）』と表記）や、Userの疑問に迎合して正しい回答まで変更する現象が観測されています。また、自分の生成物を他のものより高く評価する自己選好バイアスも確認されています。

そのため、設計とレビューを同じAIに任せるのではなく、調査・設計・コード生成・レビューの4つの役割を分けます。会話と記憶も分離することで、偏りの影響を軽減できる可能性があります。

この考え方をもとに、当初はChatGPTとClaudeそれぞれのProjectを対象にPersonaを設計し、両サービスで運用してきました。その後、訓練校の推奨環境（Gemini）とUserの費用負担を考慮して、GeminiのGem向けにも移植しました。

**Personaの指示と、評価の独立性の確保は別の問題です。**

<a id="gemini-skills-and-role-separation"></a>
> [!IMPORTANT]
> **重要：Gemini Skillsの利用と、AIの役割分離について**
>
> - **設計目的**
>
>   本Education Personaは、AIの「自己正当化バイアス」（自分の回答を正当化しようとする傾向）や「自己選好バイアス」（自分の生成した内容を過大評価する傾向）の影響を抑制することを目的として設計されています。
>
> - **Skillsで可能なこと・留意点**
>
>   Gemini Skillsでは、個々のSkillに定義された責務・判断基準・回答形式を適用できます。しかし、SkillはAIの判断によって自動的に適用される場合があり、同一会話内で複数のSkillが同時に利用される可能性があります。
>
> - **役割の独立性**
>
>   このため、各Skillが個別には適切に機能していても、設計・実装・レビューといった役割の独立性が保証されるわけではありません。個々のSkillの適切な動作と、AIシステム全体としての評価の独立性は、別の問題です。
>
> - **役割分離の方法**
>
>   本教材が重視する役割分離を実現するには、ChatGPTのProject機能やClaudeのProject機能などで会話と記憶を適切に分離するか、Geminiでは役割ごとに異なるアカウントを利用するなど、別途の対策が必要です。
>
> - **最終判断**
>
>   なお、これらの対策もAIのバイアスを完全に排除するものではありません。AIの回答はあくまで参考情報として扱い、最終的な判断は人間が行うことをお忘れなく。

上記の重要警告に残る「自己正当化バイアス」は、承認済みの原文です。現行の教材上の統一表記は「自己正当化バイアス（誤りの連鎖）」です。

```text
Gemを別会話で使う場合（従来構成）
設計Gem（会話A） ── Userが成果物を渡す ──▶ レビューGem（会話B）

Skillsが同一会話で適用される場合
同じ会話・文脈 ──┬──▶ 設計Skill
                 └──▶ レビューSkill
```

評価の独立性は、会話を分けたという事実だけでは認めません。設計・実装時の会話・記憶・参照情報から判断を分離し、Userが成果物とEvidenceを選んで引き渡すことが共通条件です。

Gemini SkillsのEducation運用では、これに加えて役割別アカウントの分離を必要条件とします。従来の4Gem＋1は承認済みの構成であり、評価の独立性が実証済みであることを意味しません。

共通設定は普段の回答方法、Personaは役割・責務・判断基準、個別プロンプトは今回の作業を指定します。詳細は[Personaの比較](personas/WHY_PERSONA_MATTERS.md#comparison-details)を参照してください。

<a id="persona-ab-code-generator"></a>
### 3.1 Personaあり／なしの検証例（Code Generator）

**Gemini 3.1 Pro**で、同一実装プロンプトによるCode Generator Personaなし／ありのA/B比較（実行検証なし、コードレビューによる静的評価）を実施しました。比較結果・評価項目・条件・限界は[検証詳細](personas/WHY_PERSONA_MATTERS.md#persona-ab-code-generator)を参照してください。GPT-5.6 Solなどを含む[5パターン横断比較](project-notes/2026-09-11-code-generator-5-pattern-comparison-reference.md)は補助資料です。

<a id="role-of-user"></a>
## 4. Role of User（Userの役割）

従来の4Gem＋1ではUserが各Gemを操作し、確定した情報を次工程へ引き渡しました。現在のSkills等を利用する場合も、成果物とEvidenceの引き渡しと最終判断はUserが管理します。

### Education運用におけるUserの3つの役割

1. **受け取る**：各役割のAIからの出力を確認する
2. **検証する**：Educationの従来フローでは、UserがコードをIDEへ反映・実行し、test・動作確認を行ってEvidenceを作成する
3. **判断する**：修正方針・再提出・最終採用を自分で決める

AIの「完了」報告だけでは、実行・検証済みのEvidenceになりません。

**Userは作業全体の最終決定者として、Evidenceを確認し、修正方針・再提出・成果物の採否を決定します。ただし、その判断によって検証Evidenceの有無・真偽・技術的な合否は変わりません。**

<a id="structure"></a>
## 5. Structure（構成）

```text
.
├── README.md        Repositoryの入口
├── AGENTS.md        Repository作業規則
├── LICENSE          ライセンス
├── personas/
│   ├── PERSONA_IDENTIFICATION_AND_SETUP.md  識別・検証の共通仕様（旧ファイル名を維持）
│   ├── WHY_PERSONA_MATTERS.md               詳細比較・検証Evidence
│   ├── AI_ISSUES_EVIDENCE.md                第2章10項目の外部研究Evidence
│   ├── SYCOPHANCY_CHALLENGER_PERSONAS.md    迎合研究の解説（Evidence集から参照）
│   ├── assets/                              Evidence図表
│   ├── education/   Education用Persona（GEMとSKILLS）。従来の4Gem＋1は参考記録
│   └── reference/   実務参考Persona・運用資料
└── project-notes/   判断履歴・現在地点・検証記録
```

役割選択と責務境界は[`Education README`](personas/education/README.md)、実務事例と運用資料の案内は[`Reference README`](personas/reference/README.md)を参照してください。

<a id="education-4skills"></a>
## 6. Education Skills（基本4役割・合計6 Skills）

> [!IMPORTANT]
> **重要：GEM版とSKILLS版のPersona機能本文は同一です。**
>
> 役割・責務・判断基準・Evidence規則・回答規則は変更しません。
>
> 違いは利用方式です。GEM固有の手動切替案内などは、Persona機能本文の一致判定に含めません。
>
> Researcherは既存の共通本文とModuleを、Learning・Development・Careerの3用途に再編しています。

2026-10-18のUser実機確認では、確認した環境でGemの表示がなくSkillsへ変更されていました。これは当該環境の観測であり、全Googleアカウントの移行完了ではありません。Education Personaの基本は、サービスの形態にかかわらず**4役割**です。SKILLSでは、この4役割を合計6つのSkill定義にします。定義ファイルは Draft です。実登録と、自動選択の実動検証は未実施です。対応関係は[`Education README`](personas/education/README.md)にあります。

<a id="education-4skills-overview"></a>
### 6.1 基本4役割と6 Skills

| 役割 | Skillの数 | 主な責務 |
|---|---|---|
| Researcher | 3（Learning / Development / Career） | 学習、設計・開発、就職活動の調査を用途別に行い、確認済み事実とEvidenceを示す |
| Solution Partner | 1 | 目的・要求・制約を整理し、設計とコード生成用指示を具体化する |
| Code Generator | 1 | 現行設計と仕様に従い、コード・testコードの生成、解析、修正を支援する |
| Reviewer | 1 | 設計・コード・Userが作成した検証Evidenceを独立して評価する |

<a id="education-4skills-researcher"></a>
### 6.2 Researcherの3 Skills

Researcherは、既存の共通本文とModuleを維持したまま、Learning、Development、Careerの3つのSkillです。ファイル構成と対応関係は[`Education README`](personas/education/README.md)を参照してください。

<a id="education-4skills-deep-research"></a>
### 6.3 Deep Researchの制約（Skills非対応）

2026-10-18時点の[Google公式案内](https://support.google.com/gemini/answer/18560919?hl=ja)によれば、Gemini SkillsはDeep Researchにはまだ対応していません。従来の追加「Researcher Deep Research」Gemに相当する5つ目のSkillは設けず、SkillからDeep Researchを起動・切替できるとは案内しません。

<a id="education-4skills-independence"></a>
### 6.4 評価の独立性への注意

同一アカウント内で、設計・コード生成・レビューのSkillsを使い分けるだけでは、本教材が求める独立レビューの条件を満たしません。必要な責務分離は[Gemini Skillsの警告](#gemini-skills-and-role-separation)を参照してください。

<a id="education-4gem-plus-1"></a>
### 6.5 従来の4Gem＋1構成（参考記録）

4Gem＋1は過去の承認済み構成です。追加の「Researcher Deep Research」は第5のPersonaではなくResearcher Personaを使う別Gemでした。現在の新規導入手順ではありません。詳細は[`Education README`](personas/education/README.md)を参照してください。

<a id="quick-start"></a>
## 7. Quick Start（利用の入口）

AIサービスは名称・画面・機能・利用条件が更新され、設定操作もリニューアルによって変わるため、**本Repositoryではサービス別の登録・設定手順を説明しません。**

Project・Skills等の利用方法は、各サービスの現行公式案内と実際の画面で確認してください。本Repositoryは、サービスの変更に左右されにくい**Personaの目的・役割分離・評価の考え方**を説明します。

<a id="prerequisites-and-notes"></a>
## 8. Prerequisites and Notes（前提と注意事項）

- Personaはすべての環境で最適な結果を保証しません。要求・制約・正本を提示し、出力を確認してください。
- パスワード、APIキー、接続情報などの秘密情報を入力・出力・コード・ログ・画面・公開物へ含めないでください。
- AIの「完了」「test成功」「問題なし」という報告だけでは検証Evidenceになりません。Userが実際の結果を確認してください。
- 会話履歴やAIの記憶だけを正本にせず、仕様・判断・検証結果を追跡可能な成果物へ残してください。

<a id="license"></a>
## 9. License（ライセンス）

本リポジトリの文書は **Creative Commons Attribution-NonCommercial 4.0 International（CC BY-NC 4.0）** のもとで公開します。出典を明示する限り、非営利目的で利用・改変・再配布できます。詳細は[`LICENSE`](LICENSE)を参照してください。

<!-- README Decision & Rationale: project-notes/README_DECISIONS.md -->
