<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-INDEX-001 |
| Version（バージョン） | 1.3 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-08-17 |
| Last Updated（最終更新日） | 2026-10-17 |
| Owner（管理者） | Takashi Oikawa |
| Related Documents（関連文書） | [`personas/education/README.md`](personas/education/README.md)<br>[`personas/WHY_PERSONA_MATTERS.md`](personas/WHY_PERSONA_MATTERS.md)<br>[`personas/reference/README.md`](personas/reference/README.md)<br>[`personas/reference/PERSONA_OPERATION_CASE_STUDY.md`](personas/reference/PERSONA_OPERATION_CASE_STUDY.md)<br>[`personas/PERSONA_IDENTIFICATION_AND_SETUP.md`](personas/PERSONA_IDENTIFICATION_AND_SETUP.md)<br>[`project-notes/2026-09-11-code-generator-5-pattern-comparison-reference.md`](project-notes/2026-09-11-code-generator-5-pattern-comparison-reference.md) |

---

# AI Setup Materials — Personaの意義・効果と役割分離

このRepositoryは、AIに「調査・設計・コード生成・レビュー」の役割を分ける理由、期待できる効果と限界を説明し、その根拠となるPersona本文と検証結果を公開します。Education用PersonaはGeminiのGem向けに作成されました。AIサービスごとの設定方法は本Repositoryの範囲外です。

**[⚠️ 重要：Gemini Skillsの利用と、AIの役割分離について](#gemini-skills-and-role-separation)**

*本ドキュメントは入門的ガイダンス（Primer）として位置づけられており、実運用レベルの標準仕様ではありません。*

<a id="start-here"></a>
## Start Here（目的別入口）

目的に応じて、最初に読む文書を選びます。

| やりたいこと | 最初に読む文書 |
|---|---|
| Education用Personaと従来の4Gem＋1構成を確認したい | [`personas/education/README.md`](personas/education/README.md) |
| Personaの識別と検証仕様を確認したい | [`PERSONA_IDENTIFICATION_AND_SETUP.md`](personas/PERSONA_IDENTIFICATION_AND_SETUP.md) |
| Reference Personaと役割分離の利用例を確認したい | [`personas/reference/README.md`](personas/reference/README.md) |
| Personaあり／なしの検証例を確認したい | [3.1 Personaあり／なしの検証例](#persona-ab-code-generator) |

ReferenceのAI運用資料は、Reference入口に示した **Case Study → Prompt Template → Handoff Template** の順で読むと全体像を把握しやすくなります。

## Contents（目次）

- [Start Here（目的別入口）](#start-here)
- [1. Target Users（対象者）](#target-users)
- [2. Challenges in AI Use（AI利用時の課題）](#challenges-in-ai-use)
- [3. Why Persona Matters（なぜPersonaが重要なのか）](#why-persona-matters)
  - [重要：Gemini Skillsの利用と、AIの役割分離について](#gemini-skills-and-role-separation)
  - [3.1 Personaあり／なしの検証例（Code Generator）](#persona-ab-code-generator)
- [4. Role of User（Userの役割）](#role-of-user)
- [5. Structure（構成）](#structure)
- [6. Education 4Gem＋1（Education用4Gem＋1）](#education-4gem-plus-1)
- [7. Quick Start（クイックスタート）](#quick-start)
- [8. Prerequisites and Notes（前提と注意事項）](#prerequisites-and-notes)
- [9. License（ライセンス）](#license)

<a id="target-users"></a>
## 1. Target Users（対象者）

本Repositoryは、職種やAIの利用経験を問わず、次のような目的を持つUserを対象とします。

- プロンプトエンジニアリングの一要素として、AIの役割・責務を設計する考え方を理解したい
- AIの応答を、自身の業務や学習の目的に合わせて使いやすくしたい
- AIの判断基準、回答形式、検証の観点を明確にし、出力を確認・評価しやすくしたい
- 事実誤認や根拠不足を見つけ、回答の質を高めたい
- 調査・設計・実装・レビューの責務を分け、評価の独立性を高めたい

EducationカテゴリのPersonaには職業訓練校での利用を想定した設計も含まれます。Repository全体の対象は教育用途に限定しません。

<a id="challenges-in-ai-use"></a>
## 2. Challenges in AI Use（AI利用時の課題）

生成AIには、次のような問題があります。

- **ハルシネーション**：事実ではない内容を、もっともらしく断定する
- **迎合（Sycophancy）**：ユーザーの誤った主張や期待に合わせて、回答を曲げる
- **自己正当化**：誤りを指摘されても認めず、理由を後付けして元の回答を守る
- **自己選好バイアス**：AI自身が生成した内容を、他の内容より高く評価しやすい
- **LITM（Lost in the Middle）**：長い入力の中ほどにある情報を見落としやすい
- **知識の古さ**：学習時点より新しい情報を知らず、新しいバージョンを「存在しない」と断定することがある
- **推測による補完**：曖昧な依頼の不足部分を、確認せずに推測で埋める
- **指示遵守の非保証**：Userの指示に対する遵守が毎回保証されないことは、現在のLLMの根本的な信頼性問題の一つである。AIが指示や規則を理解・説明できることと、それらを実際に安定して守れることは別である。
- **指示範囲外の変更**：頼んでいない箇所まで修正・追加する
- **未検証の完了報告**：実行していないのに「完了」「テスト成功」と報告する

本教材のPersonaは、これらの問題を軽減することを目的に設計しています。

ただし、問題を完全になくすものではないため、AIの出力はUserが必ず確認してください。

<a id="why-persona-matters"></a>
## 3. Why Persona Matters（なぜPersonaが重要なのか）

本Persona群は、AIの自己正当化や自己選好バイアスに対し、役割を分けて評価の独立性を高めるために設計しました。最初はChatGPTとClaudeのProjectで運用・改善し、費用負担と訓練校の推奨環境を考慮してGeminiのGemへ移植しました。PersonaはAIの判断を助けますが、同じAIが自分の成果物を評価する際の偏りを、Personaの指示だけでなくすことはできません。

<a id="gemini-skills-and-role-separation"></a>
> [!IMPORTANT]
> **重要：Gemini Skillsの利用と、AIの役割分離について**
>
> 本Education Personaは、AIの「自己正当化バイアス」（自分の回答を正当化しようとする傾向）や「自己選好バイアス」（自分の生成した内容を過大評価する傾向）の影響を抑制することを目的として設計されています。
>
> Gemini Skillsでは、個々のSkillに定義された責務・判断基準・回答形式を適用できます。しかし、SkillはAIの判断によって自動的に適用される場合があり、同一会話内で複数のSkillが同時に利用される可能性があります。
>
> このため、各Skillが個別には適切に機能していても、設計・実装・レビューといった役割の独立性が保証されるわけではありません。個々のSkillの適切な動作と、AIシステム全体としての評価の独立性は、別の問題です。
>
> 本教材が重視する役割分離を実現するには、ChatGPTのProject機能やClaudeのProject機能などで会話と記憶を適切に分離するか、Geminiでは役割ごとに異なるアカウントを利用するなど、別途の対策が必要です。
>
> なお、これらの対策もAIのバイアスを完全に排除するものではありません。AIの回答はあくまで参考情報として扱い、最終的な判断は人間が行うことをお忘れなく。

例えば、設計Skillが作った内容を同じ会話でレビューSkillが評価すると、設計時の文脈を引き継ぎ、問題を見落とす可能性があります。評価の独立性を高めるには、レビュー担当へ必要な成果物と評価基準を渡し、設計時の会話・記憶を分けて運用します。

GemとSkillsの構造を、会話の使い方に着目して比べると次のとおりです。

```text
Gemを別会話で使う場合
設計Gem（会話A） ── Userが成果物を渡す ──▶ レビューGem（会話B）

Skillsが同一会話で適用される場合
同じ会話・文脈 ──┬──▶ 設計Skill
                 └──▶ レビューSkill
```

Gemを選ぶだけで独立性が保証されるわけではありません。会話と記憶の分離を含めた運用が必要です。

生成AIへの設定には、普段の回答方法を指定する共通設定、役割・責務・判断基準を継続的に定義するPersona、今回の作業を指定するプロンプトがあります。詳細な比較表と説明は、[Personaの詳細比較](personas/WHY_PERSONA_MATTERS.md#comparison-details)を参照してください。

<a id="persona-ab-code-generator"></a>
### 3.1 Personaあり／なしの検証例（Code Generator）

同一モデル・同一実装プロンプトによる静的比較では、Personaありで改善した項目に加え、悪化した項目と改善しなかった項目もありました。Mavenによる実ビルドと実行時動作は未検証で、モデル一般の性能を示す結果ではありません。[検証結果、評価項目、条件・限界の全文](personas/WHY_PERSONA_MATTERS.md#persona-ab-code-generator)を確認してください。

<a id="role-of-user"></a>
## 4. Role of User（Userの役割）

従来の4Gem＋1構成では、Userが各Gemを操作し、出力を確認して、次の工程に必要な確定情報を手動で渡します。

Code Generatorが生成したコードまたはtestコードは、UserがIDEへ反映します。

コードの実行、test、動作確認、検証Evidenceの作成もUserが行います。

Reviewerの結果は最初にUserへ返されます。

修正方法、AI支援の利用、再提出、成果物と最終設計の採用・完成を最終判断するのはUserです。

Userの最終判断によって、検証Evidenceの有無、真偽、合否は変わりません。

詳細な運用方法とPersonaへのリンクは [`personas/education/README.md`](personas/education/README.md) を参照してください。

<a id="structure"></a>
## 5. Structure（構成）

```text
.
├── README.md        本文書（Repositoryの入口）
├── AGENTS.md        AIがこのRepositoryで作業する際の規則
├── LICENSE          ライセンス
├── personas/
│   ├── PERSONA_IDENTIFICATION_AND_SETUP.md  Persona識別と検証の共通仕様（ファイル名は旧名称）
│   ├── WHY_PERSONA_MATTERS.md  比較表とPersonaあり／なしの検証詳細
│   ├── education/   学習用：基本4Gem＋Researcher Deep Researchの追加1GemをGeminiで操作する構成
│   └── reference/   参考用：Education用4Gem＋1とは異なる前提の実務構成例
└── project-notes/   設計判断と作業状況の記録（管理用）
```

Education用の主要導線は [`personas/education/README.md`](personas/education/README.md) です。

Personaの選び方、役割分担、User-firstの作業フローは、このREADMEから確認してください。

Reference領域の入口は [`personas/reference/README.md`](personas/reference/README.md) です。

`personas/reference/` は、Education用4Gem＋1とは役割、利用サービス、実装・検証方法の前提が異なる参考資料です。

O講師が実際に検証・改善しているAI利用環境、設定構成、情報管理方法、運用方法の実践例は [`PERSONA_OPERATION_CASE_STUDY.md`](personas/reference/PERSONA_OPERATION_CASE_STUDY.md) を参照してください。チャット間の状態移送には [`CHAT_HANDOFF_TEMPLATE.md`](personas/reference/CHAT_HANDOFF_TEMPLATE.md)、今回の依頼整理には [`PERSONA_PROMPT_TEMPLATE.md`](personas/reference/PERSONA_PROMPT_TEMPLATE.md) を参考資料として用意しています。

Education用の現行手順としてそのまま流用せず、設計思想や運用パターンの参考として扱ってください。

<a id="education-4gem-plus-1"></a>
## 6. Education 4Gem＋1（Education用4Gem＋1）

2026-10-16のUser報告では、確認した講師と教育用途のアカウントでGemを新規作成できませんでした。以下は承認済みのPersonaと従来のGem構成の説明であり、現在の新規導入手順ではありません。新規導入先は未決です。

基本4Gemは次のとおりです。

| Gem | 主な責務 |
|---|---|
| `Researcher` | 外部情報を一次情報中心に調査し、確認済み事実とEvidenceを示す |
| `Solution Partner` | 目的、要求、制約を整理し、設計とコード生成用指示を具体化する |
| `Code Generator` | 現行設計と仕様に従い、コード・testコードの生成、解析、修正を支援する |
| `Reviewer` | 設計、コード、Userが作成した検証Evidenceを独立して評価する |

従来のGem構成では、詳細調査用としてResearcher Personaを使う `Researcher Deep Research` を1Gem追加する設計です。

これは独立した5番目のPersonaではなく、Researcherの追加Gemです。

Researcher完成版の選び方は [`personas/education/README.md`](personas/education/README.md) を参照してください。検索範囲を変更するときは、両Gemを同じ完成版へ入れ替えます。

<a id="quick-start"></a>
## 7. Quick Start（クイックスタート）

Education用Personaと従来の4Gem＋1構成は、[`personas/education/README.md`](personas/education/README.md) を参照してください。上記の報告対象アカウントではGemを新規作成できないため、従来の作成手順を新規導入に使用しないでください。

Project・Gem・Skills等の画面操作や登録方法は本Repositoryでは案内しません。利用時は各サービスの現行の公式案内と実画面を確認してください。

Gemini Skillsを利用する場合は、[役割分離の警告](#gemini-skills-and-role-separation)を確認し、設計とレビューの会話・記憶を適切に分けてください。

<a id="prerequisites-and-notes"></a>
## 8. Prerequisites and Notes（前提と注意事項）

- Personaは、すべての環境や用途で自動的に最適な結果を保証するものではありません。対象の要求、制約、正本を入力し、出力を確認してください。
- パスワード、APIキー、接続情報などの秘密情報を、AIへの入力、AIの出力、コード、ログ、画面、公開物へ含めないでください。
- AIが出力する「完了しました」「test成功」「問題なし」などの報告は、それだけでは検証Evidenceになりません。Userが自身の環境で実行・動作確認し、実際の結果を確認してください。
- 会話履歴やAIの記憶だけを正本として扱わず、現在有効な要求、仕様、設計、判断、検証結果を追跡できる文書や成果物へ反映してください。

<a id="license"></a>
## 9. License（ライセンス）

本リポジトリの文書は **Creative Commons Attribution-NonCommercial 4.0 International（CC BY-NC 4.0）** のもとで公開します。

出典を明示する限り、非営利目的における利用、改変、再配布が可能です。

詳細は [`LICENSE`](LICENSE) を参照してください。

<!-- README Decision & Rationale: project-notes/README_DECISIONS.md -->
