<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-EDU-GEMINI-GEM-SETUP-001 |
| Version（バージョン） | 0.1 |
| Status（ステータス） | Review |
| Created Date（作成日） | 2026-08-23 |
| Last Updated（最終更新日） | 2026-08-23 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | [`../README.md`](../README.md) |

---

# Gemini Gem Setup（Gemini Gem設定）

## 1. Purpose（目的）

この文書は、Education用4GemをGeminiのカスタムGemとして設定するための手順を説明します。

対象はGemの作成と設定です。Personaの役割説明、4Gemの利用Workflow、各Gemの使い方そのものは [`../README.md`](../README.md) と各Persona文書を参照してください。

Education用4Gemは次の4つです。

- Researcher
- Solution Partner
- Code Generator
- Reviewer

各GemのPersona本体は、Gem編集画面の `カスタム指示` 欄に貼り付けます。`知識` は、必要に応じてGemへ追加のContextを与えるための資料を追加する領域として扱います。

## 2. Gemini Gem Overview（Gemini Gem概要）

2026-08-23時点のGeminiウェブアプリのGem編集画面では、次の設定項目を確認できます。

- `名前`
- `説明`
- `カスタム指示`
- `デフォルト ツール`
- `知識`

本教材では、各項目を次の方針で設定します。

| Geminiの画面項目 | 本教材での設定方針 |
|---|---|
| `名前` | Gem表示名を設定する |
| `説明` | Gemの役割を短く説明する文を設定する |
| `カスタム指示` | Document Info等の文書管理情報を除いたPersona本体を貼り付ける |
| `デフォルト ツール` | 全4Gemで一律に固定しない。用途に応じて、未設定のまま使うか必要なツールを設定する |
| `知識` | 初期状態では空でもよい。追加Contextが必要になった場合だけ資料を追加する |

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

| Gem Display Name（Gem表示名） | Persona File（Personaファイル） |
|---|---|
| Researcher | `GEM_RESEARCHER_FULL.md` / `GEM_RESEARCHER_LEARNING_DEVELOPMENT.md` / `GEM_RESEARCHER_DEVELOPMENT.md` のうち利用する1本 |
| Solution Partner | `GEM_SOLUTION_PARTNER.md` |
| Code Generator | `GEM_CODE_GENERATOR.md` |
| Reviewer | `GEM_REVIEWER.md` |

Researcherは3完成版を同時に設定しません。その時点で必要な検索範囲を含む1本だけを選びます。

基本手順：

1. `名前` にGem表示名を入力します。
2. `説明` にGemの役割を短く記入します。
3. 対応するPersona本体を `カスタム指示` 欄に貼り付けます。
4. `デフォルト ツール` は用途に応じて判断します。必要がなければ未設定のまま使用し、必要な場合だけ設定します。
5. `知識` は初期状態では空でも構いません。追加Contextが必要な場合だけ資料を追加します。
6. 右側の `プレビュー` で応答を確認します。
7. 設定内容を保存します。

Google公式ヘルプでは、プレビューを使用しただけではGemは自動保存されないと案内されています。設定確認後に保存操作を行います。

### 3.3 `説明` の記入例

`説明` は、Gem一覧や編集画面で「このGemは何を担当するのか」を人がすぐ識別できるようにするために設定します。

長いPersona本文を転載する場所ではありません。役割を1文程度で簡潔に表します。

記入例：

| Gem | `説明` の記入例 |
|---|---|
| Researcher | 必要な外部情報を一次情報中心に調査し、Evidence付きで整理する |
| Solution Partner | 目的・要求・制約を整理し、設計とコード生成用指示を具体化する |
| Code Generator | 現行設計と仕様に従い、コード・testコードの生成や修正を支援する |
| Reviewer | 設計・コード・検証Evidenceを独立して評価する |

これらは記入例です。Personaの責務を変えない範囲で、利用者が識別しやすい短い説明へ調整できます。

### 3.4 `デフォルト ツール` の考え方

`デフォルト ツール` は、Education用4Gemすべてに同じ設定を強制しません。

用途によって必要性が変わるため、次のどちらも許容します。

- 特定のデフォルト ツールを設定せずに利用する
- そのGemの用途で必要なデフォルト ツールを設定して利用する

「4Gemだから必ず同じツールを設定する」「初期設定では必ず空にする」といった固定ルールにはしません。利用目的と必要な機能に応じて判断します。

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

選択したPersona本体をResearcher Gemの `カスタム指示` 欄に貼り付けます。

検索範囲を変更するときは、現在のResearcher Personaを別の完成版へ入れ替えます。複数のResearcher完成版を1つのGemへ同時に設定しません。

### 4.3 Solution Partner / Code Generator / Reviewer

それぞれ次のPersona本体を、対応するGemの `カスタム指示` 欄に貼り付けます。

- Solution Partner：`../GEM_SOLUTION_PARTNER.md`
- Code Generator：`../GEM_CODE_GENERATOR.md`
- Reviewer：`../GEM_REVIEWER.md`

Persona本文を変更する場合は、Repository上の現行Personaを正本として更新し、その後Gem側の `カスタム指示` 欄へ反映します。Gem側だけを変更してRepository上の正本と不一致にしないでください。

## 5. Knowledge Registration（知識への資料追加方法）

`知識` への資料追加は必須ではありません。**初期状態は空でも構いません。**

Gemへ、Personaだけでは持っていない追加のContextや参照資料を継続的に参照させたい場合に使用します。

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

`知識` に資料を追加すると、そのGemは回答を作る際に、Personaだけでなく追加された資料の内容もContextとして参照できるようになります。

例えば、設計資料を追加した場合、そのGemは一般論だけでなく、その設計資料に記載された現行仕様・用語・制約を踏まえて回答しやすくなります。

一方で、古い仕様、不要な資料、相互に矛盾する資料を追加すると、それらもContextとして参照される可能性があります。そのため、`知識` は「多いほど良い」ものではありません。現在の目的に必要で、内容が有効な資料だけを追加します。

### 5.4 本教材での使い分け

- `カスタム指示`：Gemの役割・責務・行動を定義するPersona本体
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
2. Researcher Gemの `カスタム指示` 欄を、選択した完成版のPersona本体へ入れ替えます。
3. 旧完成版の内容と新完成版の内容を同時に残しません。
4. 変更内容を保存します。

### 6.3 `説明` を変更する場合

Personaの役割が変わらない範囲で、利用者が識別しやすい短い説明へ変更できます。

Personaの責務そのものを変更する場合は、Gem側の `説明` だけを変更せず、先にRepository上のPersona正本を更新します。

### 6.4 `デフォルト ツール` を変更する場合

利用用途の変化に応じて、必要な場合のみ設定・変更します。全4Gemへ一律に同じ設定を適用する必要はありません。

### 6.5 `知識` を変更する場合

Gem編集画面の `知識` から、必要な資料を追加・削除します。

追加資料が古くなった場合や、現行仕様と矛盾する場合は、不要なContextを残さないよう見直します。

## 7. Notes（注意事項）

- カスタムGemの新規作成・編集はGeminiウェブアプリで行います。
- `プレビュー` は保存ではありません。設定変更後は保存操作を確認します。
- Personaの現行正本は本Repository内のPersonaファイルです。Gem側だけで独自変更しないでください。
- `カスタム指示` にはPersona本体を貼り付け、Document Infoや `Decision & Rationale` 等の文書管理情報は含めません。
- `説明` はGemの役割を人が識別するための短い説明として設定します。
- `デフォルト ツール` は用途に応じて判断し、全4Gemへ一律に固定しません。
- Researcherは3完成版のうち1本だけを有効にします。
- `知識` は初期状態では空でも構いません。必要な場合だけ、現在有効な資料を追加します。
- `知識` へ不要・旧版・矛盾する資料を機械的に追加しません。
- パスワード、APIキー、接続情報などの秘密情報を `カスタム指示` や `知識` へ登録しません。
- Geminiの画面名称や配置はサービス更新で変更される可能性があります。操作表示が異なる場合は、実際の画面とGoogle公式ヘルプの現行案内を確認してください。

## References（参照情報）

確認日：2026-08-23

- Google Gemini Apps Help（Gemの作成・編集）: `https://support.google.com/gemini/answer/15235603?visit_id=639230794998661777-729048722&p=custom_gems&rd=1`
- Google Gemini Apps Help: `https://support.google.com/gemini/answer/15146780?co=GENIE.Platform%3DDesktop&hl=ja`

## Decision & Rationale（決定・判断理由）

### 2026-08-23

#### Education用Gemini設定資料の管理単位

Decision:
Education用4Gemの設定資料はPersonaごとに4文書へ分割せず、`GEMINI_GEM_SETUP.md` 1文書で管理する。配置先は `personas/education/setup/` とする。

Reason:
Geminiでは4Gemとも同じGem作成・設定機構を利用するため、Personaごとに同じ操作説明を重複させない。Persona本文とAIサービス固有の設定手順を分離し、Gemini側の仕様変更時に設定資料だけを更新できるようにする。

Rejected:
- Researcher / Solution Partner / Code Generator / Reviewerごとに設定資料を4文書作成する方式
- Persona本文へGemini固有の設定操作を混在させる方式

#### 設定資料の責務範囲

Decision:
本資料はGemの設定に限定し、4Gemの利用方法・Workflow説明は含めない。Persona本体はGem編集画面の `カスタム指示` 欄に貼り付け、`知識` は必要に応じた追加Context・参照資料の追加に使用する。

Reason:
設定資料の責務をGemの作成・設定・更新に限定し、Personaの機能仕様や利用Workflowとの責務混在を防ぐため。Gemini公式ヘルプでも、Gemの `カスタム指示` と追加Context用ファイルは別の設定として案内されている。

Rejected:
- Gemの利用方法・Workflowを本設定資料へ含める方式

#### Gem編集画面の各設定項目の運用方針

Decision:
- `カスタム指示` にはPersona MD全文ではなく、Document Info等の文書管理情報を除いたPersona本体だけを貼り付ける。
- `説明` は各Gemの役割を人が識別できる短い説明を設定する。
- `デフォルト ツール` は未設定・設定済みのどちらか一方へ固定せず、用途に応じて判断する。
- `知識` は初期状態では空でもよく、必要な追加Contextがある場合だけ資料を追加する。何を追加するかと、追加によって回答時に参照されるContextが変わることを本資料で説明する。

Reason:
- Document InfoやDecision履歴はRepository管理のための情報であり、Gemの役割・責務・行動を定義する指示ではないため。
- `説明` はGemの役割を人が識別しやすくするため。
- `デフォルト ツール` の必要性はGemの用途によって異なり、一律設定では実利用に合わないため。
- `知識` は追加Contextとして作用するため、初期必須項目にせず、目的に必要な有効資料だけを追加する運用とするため。

Rejected:
- Persona MDのDocument InfoやDecision履歴まで `カスタム指示` へ貼り付ける方式
- `説明` を使用しない方式
- `デフォルト ツール` を全4Gemで一律に未設定、または一律に固定設定する方式
- `知識` へ初期状態から機械的に資料を追加する方式
