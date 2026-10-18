<details>
<summary>Document Info（文書情報）</summary>

| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-INDEX-001 |
| Version（バージョン） | 1.4 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-08-17 |
| Last Updated（最終更新日） | 2026-10-18 |
| Owner（管理者） | Takashi Oikawa |
| Related Documents（関連文書） | [`personas/education/README.md`](personas/education/README.md)<br>[`personas/WHY_PERSONA_MATTERS.md`](personas/WHY_PERSONA_MATTERS.md)<br>[`personas/reference/README.md`](personas/reference/README.md)<br>[`personas/reference/PERSONA_OPERATION_CASE_STUDY.md`](personas/reference/PERSONA_OPERATION_CASE_STUDY.md)<br>[`personas/PERSONA_IDENTIFICATION_AND_SETUP.md`](personas/PERSONA_IDENTIFICATION_AND_SETUP.md)<br>[`project-notes/2026-09-11-code-generator-5-pattern-comparison-reference.md`](project-notes/2026-09-11-code-generator-5-pattern-comparison-reference.md) |

</details>

---

# AI Setup Materials — Personaの意義・効果と役割分離

このRepositoryは、AIに「調査・設計・コード生成・レビュー」の役割を分ける理由、期待できる効果と限界を説明し、Persona本文と検証Evidenceを公開します。AIサービス別の設定方法は扱いません。

*本ドキュメントは入門的ガイダンス（Primer）であり、実運用レベルの標準仕様ではありません。*

---

## この資料で扱う2つの時間軸

| 時間軸 | 内容 | 現在の意味 |
|-------|------|-----------|
| 過去（〜2026年10月） | Geminiの「Gem」機能を使った4Gem＋1構成 | 承認済みの従来構成・関連記録 |
| 現在（2026年10月〜） | Geminiの「Skills」機能への移行と4Skills構成案 | 未検証の構成案。新規導入先は未決 |

2026-10-18のUser実機確認ではGemの表示がなくSkillsへ変更されていました。2026-10-16には対象の講師・生徒アカウントでGemを新規作成できないことも確認されています。**4Gem＋1は現在の新規導入手順ではありません。**

---

<a id="start-here"></a>
## Start Here（目的別入口）

| 確認したいこと | 最初に読む場所 |
|---|---|
| AIの問題点と、Personaによる役割分離の意義 | [AI利用時の課題](#challenges-in-ai-use) → [なぜPersonaが重要なのか](#why-persona-matters) |
| 現在のSkills環境で注意すべき評価の独立性 | [Gemini Skillsの警告](#gemini-skills-and-role-separation) ／ [`Education README`](personas/education/README.md) |
| Education Personaの4役割と従来の4Gem＋1構成 | [`Education README`](personas/education/README.md)（従来構成は新規導入手順ではない） |
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
- [6. Education 4Skills（4役割の構成案）](#education-4skills)
  - [6.1 4役割の概要](#education-4skills-overview)
  - [6.2 Researcherの統合案](#education-4skills-researcher)
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

- **自己正当化**：誤りを指摘されても認めず、理由を後付けして元の回答を守る
- **自己選好バイアス**：AI自身が生成した内容を、他の内容より高く評価しやすい

**指示遵守・作業実行・検証**

- **指示遵守の非保証**：Userの指示に対する遵守が毎回保証されないことは、現在のLLMの根本的な信頼性問題の一つである。AIが指示や規則を理解・説明できることと、それらを実際に安定して守れることは別である。
- **指示範囲外の変更**：頼んでいない箇所まで修正・追加する
- **未検証の完了報告**：実行していないのに「完了」「テスト成功」と報告する

本教材のPersonaは、これらの問題の影響を軽減することを目的として設計しています。AIの出力はUserが確認します。

<a id="why-persona-matters"></a>
## 3. Why Persona Matters（なぜPersonaが重要なのか）

AIは自分の成果物を過大評価しがちです（自己選好バイアス）。また、間違いを指摘されても認めず、言い訳を並べることがあります（自己正当化バイアス）。

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

**Gemini 3.1 Pro**で、同一実装プロンプトによるCode Generator Personaなし／ありのA/B静的比較を実施しました。比較結果・評価項目・条件・限界は[検証詳細](personas/WHY_PERSONA_MATTERS.md#persona-ab-code-generator)を参照してください。GPT-5.6 Solなどを含む[5パターン横断比較](project-notes/2026-09-11-code-generator-5-pattern-comparison-reference.md)は補助資料です。

<a id="role-of-user"></a>
## 4. Role of User（Userの役割）

従来の4Gem＋1ではUserが各Gemを操作し、確定した情報を次工程へ引き渡しました。現在のSkills等を利用する場合も、成果物とEvidenceの引き渡しと最終判断はUserが管理します。

### Education運用におけるUserの3つの役割

1. **受け取る**：各役割のAIからの出力を確認する
2. **検証する**：Educationの従来フローでは、UserがコードをIDEへ反映・実行し、test・動作確認を行ってEvidenceを作成する
3. **判断する**：修正方針・再提出・最終採用を自分で決める

AIの「完了」報告だけでは、実行・検証済みのEvidenceになりません。

**Userの最終判断によって、検証Evidenceの有無、真偽、合否は変わりません。**

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
│   ├── education/   Education用Personaと従来の4Gem＋1構成
│   └── reference/   実務参考Persona・運用資料
└── project-notes/   判断履歴・現在地点・検証記録
```

役割選択と責務境界は[`Education README`](personas/education/README.md)、実務事例と運用資料の案内は[`Reference README`](personas/reference/README.md)を参照してください。

<a id="education-4skills"></a>
## 6. Education 4Skills（4役割の構成案）

現在のUser実機環境ではGemの表示がなくSkillsへ移行しています。Education Personaの基本は、サービスの形態にかかわらず次の**4役割**です。これらをSkillとして使い分ける「4Skills」は構成案であり、4つのSkillの登録・実動検証が完了したことを意味しません。

<a id="education-4skills-overview"></a>
### 6.1 4役割の概要（Skillとして利用する候補）

| 役割（Skillとして利用する候補） | 主な責務 |
|---|---|
| Researcher | 学習・就職・開発などの調査を1つのSkillで扱い、確認済み事実とEvidenceを示す |
| Solution Partner | 目的・要求・制約を整理し、設計とコード生成用指示を具体化する |
| Code Generator | 現行設計と仕様に従い、コード・testコードの生成、解析、修正を支援する |
| Reviewer | 設計・コード・Userが作成した検証Evidenceを独立して評価する |

<a id="education-4skills-researcher"></a>
### 6.2 Researcherの統合案（利点と未決事項）

学習・就職・開発などの調査範囲ごとにSkillを分けず、Researcherを1つのSkillにまとめることで、切替・管理の手間を減らせる可能性があります。

ただし、使用するPersona本文（既存の3完成版の扱いを含む）や調査範囲の切替方法は未決で、動作検証も未実施です。現行のEducation運用では、Userが3完成版から1版を明示選択します。

<a id="education-4skills-deep-research"></a>
### 6.3 Deep Researchの制約（Skills非対応）

2026-10-18時点の[Google公式案内](https://support.google.com/gemini/answer/18560919?hl=ja)によれば、Gemini SkillsはDeep Researchに対応していません。従来の追加「Researcher Deep Research」Gemに相当する5つ目のSkillは設けず、SkillからDeep Researchを起動・切替できるとは案内しません。

<a id="education-4skills-independence"></a>
### 6.4 評価の独立性への注意

同一アカウント内で4つのSkillsを使い分けるだけでは、本教材が求める独立レビューの条件を満たしません。必要な責務分離は[Gemini Skillsの警告](#gemini-skills-and-role-separation)を参照してください。

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
