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

各GemのPersona本文は、Gem編集画面の `カスタム指示` 欄に貼り付けます。`知識` は、必要に応じてGemへ追加のContextを与えるための資料を追加する領域として扱います。

## 2. Gemini Gem Overview（Gemini Gem概要）

2026-08-23時点のGeminiウェブアプリのGem編集画面では、次の設定項目を確認できます。

- `名前`
- `説明`
- `カスタム指示`
- `デフォルト ツール`
- `知識`

本教材で現時点の設定方針が確定している項目は次のとおりです。

| Geminiの画面項目 | 本教材で設定する内容 |
|---|---|
| `名前` | Gem表示名 |
| `カスタム指示` | 対応するPersona本文 |
| `知識` | 必要に応じて追加する仕様・設計・参考資料などのContext |

`説明` と `デフォルト ツール` のEducation用4Gemとしての設定方針は、本資料の現時点では未確定です。推測で値を決めません。

Gemの新規作成はGeminiウェブアプリで行います。

## 3. Gem Creation Procedure（Gem作成手順）

### 3.1 Geminiを開く

1. ウェブブラウザで `https://gemini.google.com/` を開きます。
2. GoogleアカウントでGeminiへログインします。
3. 左側の `Gem` を開き、`Gemを作成` を選択します。

Google公式ヘルプでは、Gemの新規作成時にGemの名前とカスタム指示を入力し、必要に応じて `知識` へファイルを追加する手順が案内されています。

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
2. 対応するPersona本文を `カスタム指示` 欄に貼り付けます。
3. 必要な場合だけ `知識` に資料を追加します。
4. 右側の `プレビュー` で応答を確認します。
5. 設定内容を保存します。

Google公式ヘルプでは、プレビューを使用しただけではGemは自動保存されないと案内されています。設定確認後に保存操作を行います。

## 4. Persona Registration（Persona登録方法）

### 4.1 貼り付け先

Persona本文を、Gem編集画面の `カスタム指示` 欄に貼り付けます。

Personaファイルには、そのGemが担当する役割、責務、行動原則、責務境界、出力方針などが定義されています。Gemの振る舞いを定義する情報として使用します。

### 4.2 Researcher

Researcherは次の3完成版から1本を選択します。

- `../GEM_RESEARCHER_FULL.md`
- `../GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
- `../GEM_RESEARCHER_DEVELOPMENT.md`

選択したPersona本文をResearcher Gemの `カスタム指示` 欄に貼り付けます。

検索範囲を変更するときは、現在のResearcher Personaを別の完成版へ入れ替えます。複数のResearcher完成版を1つのGemへ同時に設定しません。

### 4.3 Solution Partner / Code Generator / Reviewer

それぞれ次のPersona本文を、対応するGemの `カスタム指示` 欄に貼り付けます。

- Solution Partner：`../GEM_SOLUTION_PARTNER.md`
- Code Generator：`../GEM_CODE_GENERATOR.md`
- Reviewer：`../GEM_REVIEWER.md`

Persona本文を変更する場合は、Repository上の現行Personaを正本として更新し、その後Gem側の `カスタム指示` 欄へ反映します。Gem側だけを変更してRepository上の正本と不一致にしないでください。

## 5. Knowledge Registration（知識への資料追加方法）

`知識` への資料追加は必須ではありません。Gemへ追加のContextや参照資料が必要な場合に使用します。

### 5.1 ファイルを追加する

1. Gem編集画面の `知識` を確認します。
2. `+` からファイル追加を開始します。
3. 利用する資料を追加します。
4. 追加したファイルが意図した資料であることを確認します。
5. 設定内容を保存します。

Google公式ヘルプでは、`知識` にファイルを追加することでGemへ追加のContextを提供できると案内されています。

### 5.2 本教材での使い分け

- `カスタム指示`：Gemの役割・責務・行動を定義するPersona本文
- `知識`：必要に応じて追加する仕様、設計、参考資料などのContext

Personaの正本は `../` 配下のPersonaファイルです。`知識` をPersona正本の代替保管場所として扱いません。

## 6. Update and Change（更新・変更方法）

### 6.1 Personaを更新する場合

1. Repository上の対象Personaが現行正本であることを確認します。
2. Geminiウェブアプリで対象Gemを開きます。
3. `カスタム指示` 欄を現行Personaの内容へ更新します。
4. `プレビュー` で設定内容を確認します。
5. 変更内容を保存します。

### 6.2 Researcherの完成版を切り替える場合

1. 利用するResearcher完成版を1本選びます。
2. Researcher Gemの `カスタム指示` 欄を、選択した完成版の内容へ入れ替えます。
3. 旧完成版の内容と新完成版の内容を同時に残しません。
4. 変更内容を保存します。

### 6.3 知識を変更する場合

Gem編集画面の `知識` から、必要な資料を追加・削除します。

## 7. Notes（注意事項）

- カスタムGemの新規作成・編集はGeminiウェブアプリで行います。
- `プレビュー` は保存ではありません。設定変更後は保存操作を確認します。
- Personaの現行正本は本Repository内のPersonaファイルです。Gem側だけで独自変更しないでください。
- Researcherは3完成版のうち1本だけを有効にします。
- `知識` は必要な場合だけ使用します。不要な資料を機械的に追加しません。
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
本資料はGemの設定に限定し、4Gemの利用方法・Workflow説明は含めない。Persona本文はGem編集画面の `カスタム指示` 欄に貼り付け、`知識` は必要に応じた追加Context・参照資料の追加に使用する。

Reason:
設定資料の責務をGemの作成・設定・更新に限定し、Personaの機能仕様や利用Workflowとの責務混在を防ぐため。Gemini公式ヘルプでも、Gemの `カスタム指示` と追加Context用ファイルは別の設定として案内されている。

Rejected:
- Gemの利用方法・Workflowを本設定資料へ含める方式