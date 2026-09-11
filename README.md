<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-INDEX-001 |
| Version（バージョン） | 1.0 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-08-17 |
| Last Updated（最終更新日） | 2026-09-11 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | [`personas/education/README.md`](personas/education/README.md)<br>[`personas/education/setup/GEMINI_GEM_SETUP.md`](personas/education/setup/GEMINI_GEM_SETUP.md)<br>[`personas/reference/README.md`](personas/reference/README.md) |

---

# AI Setup Materials — AIに役割分担させる設定集

職業訓練校でプログラミングを学ぶ生徒が、GeminiのGem（役割を固定したカスタムAI）に登録し、「調査・設計・コード生成・レビュー」をAIに役割分担させるための設定文（Persona）集です。

*本ドキュメントは入門的ガイダンス（Primer）として位置づけられており、実運用レベルの標準仕様ではありません。*

## 1. Target Users（対象者）

初学者（職業訓練校生徒）を利用者として想定。

## 2. Challenges in AI Use（AI利用時の課題）

生成AIには、次のような問題があります。

- **ハルシネーション**：事実ではない内容を、もっともらしく断定する
- **迎合（Sycophancy）**：ユーザーの誤った主張や期待に合わせて、回答を曲げる
- **自己正当化**：誤りを指摘されても認めず、理由を後付けして元の回答を守る
- **自己選好バイアス**：AI自身が生成した内容を、他の内容より高く評価しやすい
- **LITM（Lost in the Middle）**：長い入力の中ほどにある情報を見落としやすい
- **知識の古さ**：学習時点より新しい情報を知らず、新しいバージョンを「存在しない」と断定することがある
- **推測による補完**：曖昧な依頼の不足部分を、確認せずに推測で埋める
- **指示範囲外の変更**：頼んでいない箇所まで修正・追加する
- **未検証の完了報告**：実行していないのに「完了」「テスト成功」と報告する

本教材のPersonaは、これらの問題を軽減することを目的に設計しています。

ただし、問題を完全になくすものではないため、AIの出力は利用者（生徒）が必ず確認してください。

## 3. Why Persona Matters（なぜPersonaが重要なのか）

生成AIへ「普段どのように答えてほしいか」「どの役割で動いてほしいか」「今回何をしてほしいか」を伝える方法は、同じものではありません。

本教材では、違いを次のように整理します。

| 観点 | パーソナルインテリジェンスのGemini へのカスタム指示 | Gemのカスタム指示 | Gem内のプロンプト |
|---|:---:|:---:|:---:|
| 継続性 | ★★★★★ | ★★★★★ | ★☆☆☆☆ |
| 適用範囲 | サービスやアカウントの設定範囲 | Personaを設定したAI・Agent | その質問・会話 |
| 回答スタイルへの影響 | ★★★★★ | ★★★★★ | ★★★★☆ |
| AIの役割への影響 | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| 専門的な責務の固定 | ★★☆☆☆ | ★★★★★ | ★★★☆☆ |
| 具体的タスクへの影響 | ★★☆☆☆ | ★★★★☆ | ★★★★★ |
| 回答形式への影響 | ★★★★☆ | ★★★★★ | ★★★★★ |
| 毎回入力する必要 | 不要 | 不要 | 必要 |
| 主な用途 | 普段どう答えてほしいか | **このAIは何者で、何を担当するか** | 今回何をしてほしいか |

> **注意：** 星の数は各AIサービスが公開している内部的な優先順位ではありません。
>
> 本教材で、各設定が回答へどの程度・どのような種類の影響を与えるかを理解するための目安です。
>
> また、カスタム指示・共通設定の名称、提供有無、適用範囲はAIサービスによって異なります。

3つを一言で表すと、次のようになります。

```text
パーソナルインテリジェンスのGemini へのカスタム指示
「私は、普段こう答えてほしい」

Gemのカスタム指示
「あなたは、こういう役割のAIである」

Gem内のプロンプト
「今回は、これをしてほしい」
```

パーソナルインテリジェンスのGemini へのカスタム指示は、結論から説明する、長い説明を箇条書きにするなど、普段の回答方法を自分に合わせる用途に適しています。

Gem内のプロンプトは、今回の質問や作業内容を具体的に指定するために使用します。

一方、Gemのカスタム指示は、そのAIの **Role（役割）・Responsibility（責務）・Boundary（責務境界）・Decision Criteria（判断基準）・Output（出力）** を継続的に定義します。

そのため、本教材では「毎回うまいプロンプトを書くこと」だけに依存しません。

Personaによって、AIが何者で、何を担当し、どこまでを担当し、どこからは担当しないかを先に明確にします。

そのうえで、Gem内のプロンプトから具体的な作業を依頼します。

Personaの設定方法はAIサービスによって異なります。

Education領域ではGeminiのGemへPersonaを設定し、Reference領域では各AIサービスや開発支援環境の仕組みに合わせてPersonaを利用します。

## 4. Role of User（利用者（生徒）の役割）

利用者（生徒）が各Gemを操作し、出力を確認して、次の工程に必要な確定情報を手動で渡します。

Code Generatorが生成したコードまたはtestコードは、利用者（生徒）がIDEへ反映します。

コードの実行、test、動作確認、検証Evidenceの作成も利用者（生徒）が行います。

Reviewerの結果は最初に利用者（生徒）へ返されます。

修正方法、AI支援の利用、再提出、成果物と最終設計の採用・完成を最終判断するのは利用者（生徒）です。

詳細な運用方法とPersonaへのリンクは [`personas/education/README.md`](personas/education/README.md) を参照してください。

## 5. Structure（構成）

```text
.
├── README.md        本文書（Repositoryの入口）
├── AGENTS.md        AIがこのRepositoryで作業する際の規則
├── LICENSE          ライセンス
├── personas/
│   ├── education/   学習用：基本4Gem＋Researcher Deep Researchの追加1GemをGeminiで操作する構成
│   └── reference/   参考用：Education用4Gem＋1とは異なる前提の実務構成例
└── project-notes/   設計判断と作業状況の記録（管理用）
```

Education用の主要導線は [`personas/education/README.md`](personas/education/README.md) です。

Personaの選び方、役割分担、User-firstの作業フローは、このREADMEから確認してください。

Reference領域の入口は [`personas/reference/README.md`](personas/reference/README.md) です。

`personas/reference/` は、Education用4Gem＋1とは役割、利用サービス、実装・検証方法の前提が異なる参考資料です。

Education用の現行手順としてそのまま流用せず、設計思想や運用パターンの参考として扱ってください。

## 6. Education 4Gem＋1（Education用4Gem＋1）

基本4Gemは次のとおりです。

| Gem | 主な責務 |
|---|---|
| `Researcher` | 外部情報を一次情報中心に調査し、確認済み事実とEvidenceを示す |
| `Solution Partner` | 目的、要求、制約を整理し、設計とコード生成用指示を具体化する |
| `Code Generator` | 現行設計と仕様に従い、コード・testコードの生成、解析、修正を支援する |
| `Reviewer` | 設計、コード、利用者（生徒）が作成した検証Evidenceを独立して評価する |

Gemini上では、詳細調査用としてResearcher Personaを使う `Researcher Deep Research` を1Gem追加します。

これは独立した5番目のPersonaではなく、Researcherの追加Gemです。

Researcher完成版の選び方は [`personas/education/README.md`](personas/education/README.md) を参照してください。検索範囲を変更するときは、両Gemを同じ完成版へ入れ替えます。

## 7. Quick Start（クイックスタート）

Education用4Gem＋1の作成手順と使い方は、[`personas/education/README.md`](personas/education/README.md) を参照してください。

## 8. Prerequisites and Notes（前提と注意事項）

- Personaは、すべての環境や用途で自動的に最適な結果を保証するものではありません。対象の要求、制約、正本を入力し、出力を確認してください。
- パスワード、APIキー、接続情報などの秘密情報を、AIへの入力、AIの出力、コード、ログ、画面、公開物へ含めないでください。
- AIが出力する「完了しました」「test成功」「問題なし」などの報告は、それだけでは検証Evidenceになりません。利用者（生徒）が自身の環境で実行・動作確認し、実際の結果を確認してください。
- 会話履歴やAIの記憶だけを正本として扱わず、現在有効な要求、仕様、設計、判断、検証結果を追跡できる文書や成果物へ反映してください。

## 9. License（ライセンス）

本リポジトリの文書は **Creative Commons Attribution-NonCommercial 4.0 International（CC BY-NC 4.0）** のもとで公開します。

出典を明示する限り、非営利目的における利用、改変、再配布が可能です。

詳細は [`LICENSE`](LICENSE) を参照してください。

<!-- README Decision & Rationale: project-notes/README_DECISIONS.md -->
