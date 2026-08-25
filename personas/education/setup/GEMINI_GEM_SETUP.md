<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-EDU-GEMINI-GEM-SETUP-001 |
| Version（バージョン） | 1.0 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-08-23 |
| Last Updated（最終更新日） | 2026-08-25 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | [`../README.md`](../README.md) |

---

# Gemini Gem Setup（Gemini Gem設定）

## 1. Purpose（目的）

この文書は、Education用4Gem＋1をGeminiのカスタムGemとして設定するための手順を説明します。

また、Personaを設定する理由を理解するために、Geminiのパーソナル インテリジェンスにあるカスタム指示、Gem内のPersona・指示、その都度のプロンプトの違いを最初に整理します。パーソナル インテリジェンスのカスタム指示については、効果・制約・設定方法まで扱います。

基本4Gemの利用Workflowや各Gemの使い方そのものは [`../README.md`](../README.md) と各Persona文書を参照してください。

Education用の基本4Gemは次の4つです。

- Researcher
- Solution Partner
- Code Generator
- Reviewer

これに、Researcherの詳細調査用Gemとして `Researcher Deep Research` を1つ追加します。本教材では、この構成を **Education用4Gem＋1** と呼びます。

`Researcher Deep Research` は新しいPersonaではありません。Researcher Personaを使用し、`デフォルト ツール` に Deep Research を設定した追加Gemです。

PersonaとGemini上のGem実体の関係は次のとおりです。

```text
4 Persona
├─ Researcher
│  ├─ Researcher
│  └─ Researcher Deep Research
├─ Solution Partner
├─ Code Generator
└─ Reviewer

Gemini上の実体：5 Gem
```

各GemのPersona本体は、Gem編集画面の `カスタム指示` 欄に貼り付けます。初期作成時に最低限設定する項目は `名前`、`説明`、`カスタム指示` の3項目です。`知識` へのファイル追加は必須ではなく、必要になった時点で追加します。

### 1.1 Geminiに指示を与える3つの方法

Geminiへ「どのように答えてほしいか」「どの役割で動いてほしいか」「今回何をしてほしいか」を伝える方法は、同じものではありません。

本教材では、次のように整理します。

| 観点 | パーソナル インテリジェンスのカスタム指示 | Gem内のPersona・指示 | その都度のプロンプト |
|---|---:|---:|---:|
| 継続性 | ★★★★★ | ★★★★★ | ★☆☆☆☆ |
| 適用範囲 | 通常のGemini利用 | そのGem | その質問・会話 |
| 回答スタイルへの影響 | ★★★★★ | ★★★★★ | ★★★★☆ |
| AIの役割への影響 | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| 専門的な責務の固定 | ★★☆☆☆ | ★★★★★ | ★★★☆☆ |
| 具体的タスクへの影響 | ★★☆☆☆ | ★★★★☆ | ★★★★★ |
| 回答形式への影響 | ★★★★☆ | ★★★★★ | ★★★★★ |
| 毎回入力する必要 | 不要 | 不要 | 必要 |
| 主な用途 | 普段どう答えてほしいか | **このAIは何者で、何を担当するか** | 今回何をしてほしいか |
| Gem利用時 | 原則として適用されない | 適用される | 適用される |

> **注意：** 星の数はGoogleが公開している内部的な優先順位ではありません。本教材で、各設定が回答へどの程度・どのような種類の影響を与えるかを理解するための目安です。

3つを一言で表すと、次のようになります。

```text
パーソナル インテリジェンスのカスタム指示
「私は、普段こう答えてほしい」

Gem内のPersona・指示
「あなたは、こういう役割のAIである」

その都度のプロンプト
「今回は、これをしてほしい」
```

### 1.2 なぜPersonaが重要なのか

パーソナル インテリジェンスのカスタム指示は、結論から説明する、長い説明を箇条書きにするなど、普段の回答方法を自分に合わせるために有効です。

その都度のプロンプトは、今回の質問や作業内容を具体的に指定するために有効です。

一方、Personaは、そのAIの **Role（役割）・Responsibility（責務）・Boundary（責務境界）・Decision Criteria（判断基準）・Output（出力）** を継続的に定義します。

そのため、本教材では「毎回うまいプロンプトを書くこと」だけに依存しません。役割ごとのPersonaをGemへ設定し、AIが何者で、何を担当し、どこまでを担当しないのかを先に明確にします。そのうえで、その都度のプロンプトから具体的な作業を依頼します。

GoogleのGem作成ガイドでも、Gemの指示を作成する主な観点として `Persona`、`Task`、`Context`、`Format` が示されており、PersonaはGemが担う役割と回答方法を伝える要素として案内されています。

### 1.3 パーソナル インテリジェンスのカスタム指示

#### 1.3.1 何ができるか

パーソナル インテリジェンスのカスタム指示は、Geminiへ毎回同じ指示を書かなくても、普段の回答方法を自分に合わせるための設定です。

例：

- 回答の最初に結論を示す
- 長い説明では箇条書きを使用する
- IT初心者にも理解できる言葉で説明する
- 専門用語を使用する場合は簡単な説明を付ける

Google公式ヘルプでは、追加したカスタム指示をすべてのチャットへ適用できると案内されています。

#### 1.3.2 効果と制約

カスタム指示は、回答スタイルや説明方法を継続的に調整する用途では有効です。一方で、AIの動作を完全に拘束する絶対命令としては扱いません。

Google公式ヘルプでも、特定のトピックを忘れる、または避けるよう指示しても、必ずしも完全に機能するとは限らないと案内されています。

したがって、本教材では次のように理解します。

```text
カスタム指示
＝ 普段の回答傾向を継続的に調整する

≠ AIの動作を完全に制御する
```

また、現在のGoogle公式案内では、パーソナル インテリジェンスのカスタム指示は **Gemなど一部の機能では利用できません**。

そのため、Education用4Gem＋1で使用するRole、Responsibility、Boundary、Decision Criteria等は、パーソナル インテリジェンス側ではなく、各Gem自身の `カスタム指示` 欄へPersonaとして登録します。

#### 1.3.3 利用条件

2026-08-25時点のGoogle公式案内では、パーソナル インテリジェンスのカスタム指示を追加するには個人のGoogleアカウントでGeminiへログインしている必要があります。

仕事用、学校用、または管理対象のGoogleアカウントでは利用できません。

#### 1.3.4 設定方法（パソコン）

2026-08-25時点のGoogle公式案内に基づく設定手順：

1. ウェブブラウザで `https://gemini.google.com/` を開きます。
2. 画面下部の `設定とヘルプ` を開きます。
3. `パーソナル インテリジェンス` を開きます。
4. `Gemini へのカスタム指示` を開きます。
5. `+ 追加` を選択します。
6. すべてのチャットに適用したいカスタム指示を入力します。
7. `送信` を選択します。

ここで設定するのは、通常のGemini利用に対する共通的な回答方法です。GemのPersona登録とは別の設定です。

## 2. Gemini Gem Overview（Gemini Gem概要）

2026-08-23時点のGeminiウェブアプリのGem編集画面では、次の設定項目を確認できます。

- `名前`
- `説明`
- `カスタム指示`
- `デフォルト ツール`
- `知識`

本教材では、各項目を次の方針で設定します。

| Geminiの画面項目 | 初期作成時 | 本教材での設定方針 |
|---|---|---|
| `名前` | 必須 | Gem表示名を設定する |
| `説明` | 必須 | 何のGemか人が分かりやすいように、本教材で定めた標準値をそのまま設定する |
| `カスタム指示` | 必須 | Gem側の指示欄。Document Info等の文書管理情報を除いたPersona本体を貼り付ける |
| `デフォルト ツール` | 任意 | `Researcher Deep Research` だけ Deep Research を設定する。通常用Researcher / Solution Partner / Code Generator / Reviewerは初期状態では設定しない。必要になった場合だけ追加する |
| `知識` | 任意 | 初期状態は空でよい。必要になった時点で、追加Contextとして参照させたいファイルを追加する |

この章以降で `カスタム指示` と記載する場合は、特記がない限り **Gem編集画面の `カスタム指示`** を指します。パーソナル インテリジェンスのカスタム指示とは別の設定です。

Gemの新規作成はGeminiウェブアプリで行います。

## 3. Gem Creation Procedure（Gem作成手順）

### 3.1 Geminiを開く

1. ウェブブラウザで `https://gemini.google.com/` を開きます。
2. GoogleアカウントでGeminiへログインします。
3. 左側の `Gem` を開き、`Gemを作成` を選択します。

Gemの作成・編集に関するGoogle公式の案内は、次を参照してください。

`https://support.google.com/gemini/answer/15235603?visit_id=639230794998661777-729048722&p=custom_gems&rd=1`

### 3.2 Gemを作成する

作成するGemごとに次のPersonaを使用します。

| Gem Display Name（Gem表示名） | Persona File（Personaファイル） | `デフォルト ツール` |
|---|---|---|
| Researcher | `GEM_RESEARCHER_FULL.md` / `GEM_RESEARCHER_LEARNING_DEVELOPMENT.md` / `GEM_RESEARCHER_DEVELOPMENT.md` のうち利用する1本 | 設定しない |
| Researcher Deep Research | 通常用Researcherと同じResearcher Persona | Deep Research |
| Solution Partner | `GEM_SOLUTION_PARTNER.md` | 初期状態では設定しない。必要時のみ追加 |
| Code Generator | `GEM_CODE_GENERATOR.md` | 初期状態では設定しない。必要時のみ追加 |
| Reviewer | `GEM_REVIEWER.md` | 初期状態では設定しない。必要時のみ追加 |

Researcherは3完成版を同時に設定しません。その時点で必要な検索範囲を含む1本だけを選び、通常用ResearcherとResearcher Deep Researchの両方に同じ完成版を使用します。

初期作成時の最低限の設定手順：

1. `名前` にGem表示名を入力します。
2. `説明` に、3.3で定めた教材標準値をそのまま入力します。
3. 対応するPersona本体を `カスタム指示` 欄に貼り付けます。
4. `Researcher Deep Research` を作成する場合だけ、`デフォルト ツール` に Deep Research を設定します。
5. 右側の `プレビュー` で応答を確認します。
6. 設定内容を保存します。

通常用Researcher / Solution Partner / Code Generator / Reviewerでは、初期状態の `デフォルト ツール` は設定しません。利用上必要になった場合だけ追加します。`知識` も初期作成時には空で構いません。必要になった時点で、参照させたいファイルを追加します。

Google公式ヘルプでは、プレビューを使用しただけではGemは自動保存されないと案内されています。設定確認後に保存操作を行います。

### 3.3 `説明` の教材標準値

`説明` は、Gem一覧や編集画面で「このGemは何を担当するのか」を人がすぐ識別できるようにするために設定します。

長いPersona本文を転載する場所ではありません。本教材では次の内容を教材標準値として固定し、初期設定時はそのまま入力します。

| Gem | `説明` の教材標準値 |
|---|---|
| Researcher | 通常の調査・学習・情報確認を、一次情報とEvidenceを重視して支援する |
| Researcher Deep Research | 企業研究・業界研究・比較調査など、複数の情報源を横断する詳細調査を支援する |
| Solution Partner | 目的・要求・制約を整理し、設計とコード生成用指示を具体化する |
| Code Generator | 現行設計と仕様に従い、コード・testコードの生成や修正を支援する |
| Reviewer | 設計・コード・検証Evidenceを独立して評価する |

### 3.4 `デフォルト ツール` の考え方

`デフォルト ツール` は、Education用Gemすべてに同じ設定を強制しません。

Researcherでは、Deep Researchの使用有無を毎回設定変更するのではなく、次の2つのGemを作成して使い分けます。

- `Researcher`：`デフォルト ツール` は設定しない。通常の調査、学習、簡単な事実確認などに使用する。
- `Researcher Deep Research`：`デフォルト ツール` に Deep Research を設定する。企業研究、業界研究、比較調査など、複数の情報源を横断する詳細調査に使用する。

Deep Researchは詳細調査に有効ですが、通常の調査より処理時間が長くなり、利用量（Usage）が増え、利用上限にも影響します。そのため、Researcherのすべての調査をDeep Researchへ固定せず、用途に応じて2つのGemを選択します。

本教材では、AIサービスをどの程度使用したかを表す共通用語を **`利用量（Usage）`** に統一します。各サービス固有の説明で別の正式名称を引用する必要がある場合を除き、`クレジット` や `ポイント` を共通用語として使用しません。

Solution Partner / Code Generator / Reviewerは、初期状態では `デフォルト ツール` を設定しません。利用上必要なツールが明確になった場合だけ追加します。

## 4. Persona Registration（Persona登録方法）

### 4.1 貼り付け先

Persona本体を、Gem編集画面の `カスタム指示` 欄に貼り付けます。

**Persona MDファイルの全文をそのまま貼り付けるのではありません。**

貼り付ける対象は、Gemの振る舞いを定義するPersona本体です。次のような文書管理情報は除外します。

- `Document Info（文書情報）`
- Version / Status / Created Date / Last Updated / Owner / Related Documents
- 将来Personaファイルに追加された場合の `Decision & Rationale（決定・判断理由）`

理由：これらはRepository上で文書を管理し、設計判断の経緯を追跡するための情報であり、Gemの役割・責務・行動を定義する指示そのものではないためです。文書管理情報まで `カスタム指示` に含めると、Gemに不要なContextを与え、文書管理ルールをPersonaの行動指示として誤って扱わせる可能性があります。

#### 記入例：Solution Partner

`GEM_SOLUTION_PARTNER.md` を使う場合：

**貼り付けない部分**

```text
Document Info（文書情報）
Version
Status
Created Date
Last Updated
Owner
Related Documents
```

**貼り付ける部分**

```text
# Solution Partner Persona（Solution Partnerペルソナ）

## 1. Role（役割）
...

## 2. Primary Responsibilities（主な責務）
...

## 3. Operating Principles（行動原則）
...
```

以降も、そのPersonaの役割・責務・判断基準・責務境界・出力等を定義する本文を最後まで貼り付けます。`Decision & Rationale` が存在する場合は、その直前までをPersona本体として扱います。

### 4.2 Researcher

Researcherは次の3完成版から1本を選択します。

- `../GEM_RESEARCHER_FULL.md`
- `../GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
- `../GEM_RESEARCHER_DEVELOPMENT.md`

選択したPersona本体を、通常用の `Researcher` と `Researcher Deep Research` の両方の `カスタム指示` 欄に使用します。

検索範囲を変更するときは、現在のResearcher Personaを別の完成版へ入れ替えます。複数のResearcher完成版を1つのGemへ同時に設定しません。

### 4.3 Solution Partner / Code Generator / Reviewer

それぞれ次のPersona本体を、対応するGemの `カスタム指示` 欄に貼り付けます。

- Solution Partner：`../GEM_SOLUTION_PARTNER.md`
- Code Generator：`../GEM_CODE_GENERATOR.md`
- Reviewer：`../GEM_REVIEWER.md`

Persona本文を変更する場合は、Repository上の現行Personaを正本として更新し、その後Gem側の `カスタム指示` 欄へ反映します。Gem側だけを変更してRepository上の正本と不一致にしないでください。

## 5. Knowledge Registration（知識への資料追加方法）

`知識` への資料追加は必須ではありません。**初期状態は空で構いません。必要になった時点でファイルを追加します。**

Gemへ、Personaだけでは持っていない追加のContextや参照資料を継続的に参照させたい場合に使用します。

本教材では、Contextを「AIが回答するときに参照する情報のまとまり」として扱います。理解のため、主な構成要素は次のように整理します。

```text
Context
≒
Gemのカスタム指示（Persona本体）
＋
会話履歴
＋
今回のプロンプト
＋
「知識」から参照された情報
```

ここでいう `Gemのカスタム指示` は、パーソナル インテリジェンスのカスタム指示ではありません。

Context Windowの説明は本資料には含めません。本資料では、Gem設定に直接必要なContextと `知識` の関係だけを扱います。

### 5.1 ファイルを追加する

1. Gem編集画面の `知識` を確認します。
2. `+` からファイル追加を開始します。
3. 利用する資料を追加します。
4. 追加したファイルが意図した資料であることを確認します。
5. 設定内容を保存します。

Google公式ヘルプでは、`知識` にファイルを追加することでGemへ追加のContextを提供できると案内されています。

### 5.2 どのような資料を追加するか

例：

- 課題や制作物の要求・仕様をまとめた資料
- 現行の設計資料
- 授業で使用する参考資料
- 用語集やルール集
- そのGemが繰り返し参照する必要があるプロジェクト固有資料

毎回の会話で一時的に使うだけの情報まで、機械的に `知識` へ追加する必要はありません。

### 5.3 `知識` を追加すると何が変わるか

`知識` に資料を追加すると、そのGemは回答を作る際に、Personaだけでなく追加された資料から参照された情報もContextとして利用できるようになります。

例えば、設計資料を追加した場合、そのGemは一般論だけでなく、その設計資料に記載された現行仕様・用語・制約を踏まえて回答しやすくなります。

一方で、古い仕様、不要な資料、相互に矛盾する資料を追加すると、それらもContextとして参照される可能性があります。そのため、`知識` は「多いほど良い」ものではありません。現在の目的に必要で、内容が有効な資料だけを追加します。

### 5.4 本教材での使い分け

- `Gemのカスタム指示`：Gemの役割・責務・行動を定義するPersona本体
- `知識`：必要に応じて追加する仕様、設計、参考資料などのContext

Personaの正本は `../` 配下のPersonaファイルです。`知識` をPersona正本の代替保管場所として扱いません。

## 6. Update and Change（更新・変更方法）

### 6.1 Personaを更新する場合

1. Repository上の対象Personaが現行正本であることを確認します。
2. Geminiウェブアプリで対象Gemを開きます。
3. `カスタム指示` 欄を現行Persona本体の内容へ更新します。
4. `プレビュー` で設定内容を確認します。
5. 変更内容を保存します。

### 6.2 Researcherの完成版を切り替える場合

1. 利用するResearcher完成版を1本選びます。
2. 通常用 `Researcher` と `Researcher Deep Research` の `カスタム指示` 欄を、選択した完成版のPersona本体へ入れ替えます。
3. 旧完成版の内容と新完成版の内容を同時に残しません。
4. 変更内容を保存します。

### 6.3 `説明` を変更する場合

本教材では3.3の教材標準値を使用します。初期設定時に利用者判断で変更しません。

Personaの責務そのものを変更する場合は、Gem側の `説明` だけを変更せず、先にRepository上のPersona正本と本資料の教材標準値を見直します。

### 6.4 `デフォルト ツール` を変更する場合

ResearcherではDeep Researchの使用有無を都度切り替えず、通常用 `Researcher` と `Researcher Deep Research` を使い分けます。

Solution Partner / Code Generator / Reviewerは、初期状態では `デフォルト ツール` を設定しません。利用上必要になった場合だけ追加・変更します。

### 6.5 `知識` を変更する場合

Gem編集画面の `知識` から、必要な資料を追加・削除します。

追加資料が古くなった場合や、現行仕様と矛盾する場合は、不要なContextを残さないよう見直します。

## 7. Notes（注意事項）

- パーソナル インテリジェンスのカスタム指示と、Gem編集画面の `カスタム指示` は別の設定です。
- Googleの現行案内では、パーソナル インテリジェンスのカスタム指示はGemなど一部機能では利用できません。
- カスタムGemの新規作成・編集はGeminiウェブアプリで行います。
- Education用の構成は、基本4Gemに `Researcher Deep Research` を追加した **4Gem＋1** です。
- `Researcher Deep Research` は新しいPersonaではなく、Researcher Personaを使う詳細調査用の追加Gemです。
- 初期作成時の最低限必須項目は `名前`、`説明`、`カスタム指示` の3つです。
- `プレビュー` は保存ではありません。設定変更後は保存操作を確認します。
- Personaの現行正本は本Repository内のPersonaファイルです。Gem側だけで独自変更しないでください。
- Gemの `カスタム指示` にはPersona本体を貼り付け、Document Infoや `Decision & Rationale` 等の文書管理情報は含めません。
- `説明` は3.3の教材標準値をそのまま設定します。
- Researcherは、通常用 `Researcher` と Deep Research用 `Researcher Deep Research` の2つを作成して用途で使い分けます。
- `Researcher` の `デフォルト ツール` は設定せず、`Researcher Deep Research` には Deep Research を設定します。
- Solution Partner / Code Generator / Reviewerの `デフォルト ツール` は初期状態では設定せず、必要になった場合だけ追加します。
- Researcherは3完成版のうち1本だけを有効にします。
- AIサービスの使用量に関する共通用語は `利用量（Usage）` を使用します。
- `知識` は初期作成時の必須項目ではありません。必要になった時点で、現在有効な資料を追加します。
- `知識` へ不要・旧版・矛盾する資料を機械的に追加しません。
- Context Windowの説明は本資料の対象外です。
- パスワード、APIキー、接続情報などの秘密情報をパーソナル インテリジェンスのカスタム指示、Gemの `カスタム指示`、`知識` へ登録しません。
- Geminiの画面名称や配置はサービス更新で変更される可能性があります。操作表示が異なる場合は、実際の画面とGoogle公式ヘルプの現行案内を確認してください。

## References（参照情報）

確認日：2026-08-25

- Google Gemini Apps Help（カスタム指示でGeminiの回答をカスタマイズする）: `https://support.google.com/gemini/answer/16598625?co=GENIE.Platform%3DDesktop&hl=ja`
- Google Gemini Apps Help（Gemの作成・編集）: `https://support.google.com/gemini/answer/15235603?hl=ja`
- Google Gemini Apps Help: `https://support.google.com/gemini/answer/15146780?co=GENIE.Platform%3DDesktop&hl=ja`

## Decision & Rationale（決定・判断理由）

### 2026-08-25

#### カスタム指示比較を前半へ配置しPersonaの重要性を説明する

Decision:
本資料の前半に、パーソナル インテリジェンスのカスタム指示、Gem内のPersona・指示、その都度のプロンプトを比較する表を配置する。比較後に、PersonaがRole、Responsibility、Boundary、Decision Criteria、Outputを継続的に定義するため重要であることを説明してからGem設定手順へ進む。

Reason:
Personaの定義や設定手順を先に説明するだけでは、初学者が「なぜPersonaが必要なのか」を理解しにくい。普段の回答方法を調整する設定、AIの役割を定義する設定、その場の作業を指定する指示を比較することで、それぞれの責務とPersonaの必要性を理解してから設定作業へ進めるため。

比較表の星はGoogleが公開する内部優先順位ではなく、教材上の理解を助ける影響度の目安として扱う。

Rejected:
- Persona設定手順を先に説明し、カスタム指示やプロンプトとの違いを後から説明する構成
- 星の数をGemini内部の正式な優先順位として説明する方式

#### パーソナル インテリジェンスのカスタム指示を設定資料へ追加する

Decision:
パーソナル インテリジェンスのカスタム指示について、効果、完全な制御ではないという制約、利用条件、パソコンでの設定手順を本資料へ追加する。Gemの `カスタム指示` とは明確に区別する。

2026-08-23の「本資料はGemの設定に限定する」という責務範囲は、本決定によって「Persona利用に直接関係するGemini設定まで扱う」へ更新する。基本4Gemの利用Workflowや各Personaの機能仕様は引き続き本資料へ含めない。

Reason:
Personaの重要性を理解するには、通常利用へ継続的に作用するカスタム指示と、Gem自身の役割を定義するPersonaの違いを理解する必要があるため。また、Googleの現行仕様ではパーソナル インテリジェンスのカスタム指示はGemなど一部機能では利用できず、Gemの役割・責務を継続させるにはGem自身の `カスタム指示` にPersonaを設定する必要があるため。

Rejected:
- パーソナル インテリジェンスのカスタム指示とGemの `カスタム指示` を同一機能として説明する方式
- カスタム指示をAIへ絶対的に強制されるルールとして説明する方式

### 2026-08-23

#### Education用Gemini設定資料の管理単位

Decision:
Education用4Gem＋1の設定資料はPersonaごとに文書を分割せず、`GEMINI_GEM_SETUP.md` 1文書で管理する。配置先は `personas/education/setup/` とする。

Reason:
基本4Gemと追加Gemはいずれも同じGem作成・設定機構を利用するため、Gemごとに同じ操作説明を重複させない。Persona本文とAIサービス固有の設定手順を分離し、Gemini側の仕様変更時に設定資料だけを更新できるようにする。

Rejected:
- Researcher / Researcher Deep Research / Solution Partner / Code Generator / Reviewerごとに設定資料を分割する方式
- Persona本文へGemini固有の設定操作を混在させる方式

#### 設定資料の責務範囲

Decision:
本資料はGemの設定に限定し、基本4Gemの利用方法・Workflow説明は含めない。Persona本体はGem編集画面の `カスタム指示` 欄に貼り付け、`知識` は必要に応じた追加Context・参照資料の追加に使用する。

Reason:
設定資料の責務をGemの作成・設定・更新に限定し、Personaの機能仕様や利用Workflowとの責務混在を防ぐため。Gemini公式ヘルプでも、Gemの `カスタム指示` と追加Context用ファイルは別の設定として案内されている。

Rejected:
- Gemの利用方法・Workflowを本設定資料へ含める方式

#### Gem編集画面の各設定項目の運用方針

Decision:
- `カスタム指示` にはPersona MD全文ではなく、Document Info等の文書管理情報を除いたPersona本体だけを貼り付ける。
- `説明` は各Gemの役割を人が識別できる教材標準値を使用し、初期設定時はそのまま入力する。
- `デフォルト ツール` は `Researcher Deep Research` だけ Deep Research を設定する。通常用Researcher / Solution Partner / Code Generator / Reviewerは初期状態では設定せず、必要になった場合だけ追加する。
- `知識` は初期状態では空でもよく、必要な追加Contextがある場合だけ資料を追加する。何を追加するかと、追加によって回答時に参照されるContextが変わることを本資料で説明する。

Reason:
- Document InfoやDecision履歴はRepository管理のための情報であり、Gemの役割・責務・行動を定義する指示ではないため。
- `説明` は初学者が内容を考える作業を不要にし、各Gemの役割を同じ表現で識別できるようにするため。
- `デフォルト ツール` は初期設定を最小化し、必要性が明確な場合だけ追加する方が、各ツールの目的を理解しやすく不要な設定も避けられるため。Deep Researchは用途を明確に分離するため `Researcher Deep Research` にのみ設定する。
- `知識` は追加Contextとして作用するため、初期必須項目にせず、目的に必要な有効資料だけを追加する運用とするため。

Rejected:
- Persona MDのDocument InfoやDecision履歴まで `カスタム指示` へ貼り付ける方式
- `説明` を利用者ごとの自由記入にする方式
- Solution Partner / Code Generator / Reviewerへ初期状態から `デフォルト ツール` を設定する方式
- `知識` へ初期状態から機械的に資料を追加する方式

#### 初期作成時の最低限必須項目

Decision:
Education用Gemを初期作成する際の最低限必須項目は、`名前`、`説明`、`カスタム指示` の3項目とする。`知識` へのファイル追加は初期作成時には必須とせず、必要になった時点で追加する。`デフォルト ツール` も最低限必須項目には含めず、用途に応じて設定する。

Reason:
最初にGemを識別する情報とPersonaとしての振る舞いを確定させれば、Gemとして利用を開始できるため。追加資料やツールは利用目的によって必要性が変わるため、初期設定を過剰にせず、必要になった時点で拡張する方が生徒にとって設定意図を理解しやすい。

Rejected:
- 初期作成時から `知識` へのファイル追加を必須にする方式
- 初期作成時から `デフォルト ツール` の設定を必須にする方式

#### ResearcherのDeep Research運用

Decision:
Researcherは、通常調査用の `Researcher` と、`デフォルト ツール` に Deep Research を設定した `Researcher Deep Research` の2つのGemを作成し、用途に応じて使い分ける。通常用Researcherでは `デフォルト ツール` を設定しない。Researcher Persona自体はEducation用基本4Gem体系上1つの役割として扱う。

Reason:
Deep Researchは企業研究・業界研究・比較調査など複数情報源を横断する詳細調査に適している一方、通常の調査より処理時間が長く、利用量（Usage）が増え、利用上限にも影響する。1つのGemでDeep Research設定を都度変更するより、通常用と詳細調査用を分けた方が、利用者が用途を判断しやすく、不要なDeep Research利用や設定戻し忘れも防げるため。

Rejected:
- ResearcherでDeep Researchを常時使用する方式
- 1つのResearcher Gemで、必要になるたびに `デフォルト ツール` のDeep Research設定を追加・解除する方式

#### `知識` 説明へのContext定義追加

Decision:
`知識` の説明では、Contextを「AIが回答するときに参照する情報のまとまり」と説明し、主な構成要素を `カスタム指示 + 会話履歴 + 今回のプロンプト + 「知識」から参照された情報` として示す。

Reason:
`知識` にファイルを追加すると何が変わるかを、初学者がContextとの関係から理解できるようにするため。

#### Solution Partner / Code Generator / Reviewerの初期デフォルトツール

Decision:
Solution Partner / Code Generator / Reviewerは、初期状態では `デフォルト ツール` を設定しない。利用上必要なツールが明確になった場合だけ追加する。

Reason:
初期設定を最小化し、用途が確定していないツールを先回りして設定しないことで、各設定項目の意味と必要性を生徒が理解しやすくするため。

#### AIサービス使用量の共通用語

Decision:
本教材では、AIサービスをどの程度使用したかを表す共通用語を `利用量（Usage）` に固定する。各サービス固有の正式名称を引用する必要がある場合を除き、`クレジット` や `ポイント` を共通用語として使用しない。

Reason:
Claude、Cursor、ChatGPT、Gemini、Grokでは利用枠・追加利用等の正式名称が統一されていないため、教材横断で誤解なく使用できる共通表現として `利用量（Usage）` を採用する。

#### `説明` の教材標準値

Decision:
各Gemの `説明` は記入例ではなく教材標準値として固定し、初期設定時は本資料に記載した内容をそのまま入力する。

Reason:
初学者が `説明` の文面を考える必要をなくし、教材利用者間でGemの識別表現を統一するため。

Rejected:
- `説明` を記入例として提示し、利用者が責務を変えない範囲で自由に調整する方式

#### Context Windowの扱い

Decision:
Context Windowの説明は `GEMINI_GEM_SETUP.md` には追加しない。本資料ではGem設定に直接必要なContextと `知識` の関係だけを説明する。

Reason:
Context Windowは重要な概念だが、Gemの設定操作に直接必要ではないため。本資料の責務をGem設定に限定し、概念説明を過剰に広げない。

Rejected:
- Contextの説明に加えてContext Windowの概念説明も本資料へ追加する方式

#### Education用4Gem＋1の呼称と構成図

Decision:
Education用の基本体系は4Gemとして維持し、`Researcher Deep Research` を追加した構成を `4Gem＋1` と呼ぶ。PersonaとGemini上の実体数の違いを明確にするため、本文に `4 Persona` と `Gemini上の実体：5 Gem` の構成図を記載する。

Reason:
基本の4役割を変更せず、Deep Research用GemがResearcherの追加実体であることを初学者にも明確に示せるため。単に `5Gem` と呼ぶと5つの異なるPersonaが存在するように誤解される可能性がある。

#### 完成版昇格

Decision:
User承認に基づき、本資料を `Version 1.0 / Status Approved` へ昇格する。

Reason:
Gemini上の4Gem＋1構成、標準入力値、Persona登録方法、Deep Research運用、`知識`、Context、`利用量（Usage）`、更新方法までの設定仕様についてUser判断が完了し、Education READMEとの整合も確認・反映したため。