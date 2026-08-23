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

各GemのPersona本文は、Gemの `Instructions（指示）` に設定します。`Knowledge` は、必要に応じてGemへ追加のContextを与えるための資料を登録する領域として扱います。

## 2. Gemini Gem Overview（Gemini Gem概要）

Gemは、名前、指示、必要に応じたKnowledgeを設定して作成するカスタムGeminiです。

本教材では、Gemの設定項目を次のように使い分けます。

| Geminiの設定項目 | 本教材で設定する内容 |
|---|---|
| Name（名前） | Gem表示名 |
| Instructions（指示） | 対応するPersona本文 |
| Knowledge | 必要に応じて追加する仕様・設計・参考資料などのContext |

Gemの新規作成はGeminiウェブアプリで行います。

## 3. Gem Creation Procedure（Gem作成手順）

### 3.1 Geminiを開く

1. ウェブブラウザで `https://gemini.google.com/` を開きます。
2. GoogleアカウントでGeminiへログインします。
3. 左側のGem一覧を開き、Gemの新規作成を選択します。

Googleの現在のヘルプでは、画面上の操作は `[Gem を表示]` → `[Gem を作成]`、またはUI言語によって `Gems` → `New Gem` と案内されています。

### 3.2 Gemを作成する

作成するGemごとに次を設定します。

| Gem Display Name（Gem表示名） | Persona File（Personaファイル） |
|---|---|
| Researcher | `GEM_RESEARCHER_FULL.md` / `GEM_RESEARCHER_LEARNING_DEVELOPMENT.md` / `GEM_RESEARCHER_DEVELOPMENT.md` のうち利用する1本 |
| Solution Partner | `GEM_SOLUTION_PARTNER.md` |
| Code Generator | `GEM_CODE_GENERATOR.md` |
| Reviewer | `GEM_REVIEWER.md` |

Researcherは3完成版を同時に設定しません。その時点で必要な検索範囲を含む1本だけを選びます。

基本手順：

1. Gemの名前を入力します。
2. 対応するPersona本文を `Instructions（指示）` へ設定します。
3. 必要な場合だけ `Knowledge` を追加します。
4. 右側のプレビュー欄で応答を確認します。
5. `保存` を実行します。

プレビューを実行しただけではGemは保存されません。設定確認後に必ず保存します。

## 4. Persona Registration（Persona登録方法）

### 4.1 登録先

Persona本文は `Instructions（指示）` に設定します。

Personaファイルには、そのGemが担当する役割、責務、行動原則、責務境界、出力方針などが定義されています。Gemの振る舞いを決める情報として、Persona本文全体をInstructionsへ設定します。

### 4.2 Researcher

Researcherは次の3完成版から1本を選択します。

- `../GEM_RESEARCHER_FULL.md`
- `../GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
- `../GEM_RESEARCHER_DEVELOPMENT.md`

選択した1ファイルの本文をResearcher GemのInstructionsへ設定します。

検索範囲を変更するときは、現在のResearcher Personaを別の完成版へ入れ替えます。複数のResearcher完成版を1つのGemへ同時に設定しません。

### 4.3 Solution Partner / Code Generator / Reviewer

それぞれ次のPersona本文を対応するGemのInstructionsへ設定します。

- Solution Partner：`../GEM_SOLUTION_PARTNER.md`
- Code Generator：`../GEM_CODE_GENERATOR.md`
- Reviewer：`../GEM_REVIEWER.md`

Persona本文を変更する場合は、Repository上の現行Personaを正本として更新し、その後Gem側のInstructionsへ反映します。Gem側だけを変更してRepository上の正本と不一致にしないでください。

## 5. Knowledge Registration（Knowledge登録方法）

Knowledgeは必須ではありません。Gemへ追加のContextや参照資料が必要な場合に使用します。

### 5.1 ファイルを追加する

1. Gem編集画面の `Knowledge` を表示します。
2. `Add files（ファイルを追加）` を選択します。
3. 端末からアップロードするか、Google Driveから追加します。
4. 追加したファイルが意図した資料であることを確認します。
5. Gemの設定を保存します。

Google Driveからファイルを追加する場合、GeminiはDrive上の最新バージョンを使用し、Drive側の変更がGemへ反映されます。Google Driveから追加するには、Gemini Apps Activityの設定やGoogle Workspaceとの接続が必要になる場合があります。

### 5.2 本教材での使い分け

- `Instructions`：Gemの役割・責務・行動を定義するPersona本文
- `Knowledge`：必要に応じて追加する仕様、設計、参考資料などのContext

Personaの正本は `../` 配下のPersonaファイルです。KnowledgeをPersona正本の代替保管場所として扱いません。

## 6. Update and Change（更新・変更方法）

### 6.1 Personaを更新する場合

1. Repository上の対象Personaが現行正本であることを確認します。
2. Geminiウェブアプリで対象Gemを開きます。
3. `Instructions（指示）` を現行Personaの内容へ更新します。
4. プレビューで設定内容を確認します。
5. 変更を保存します。

### 6.2 Researcherの完成版を切り替える場合

1. 利用するResearcher完成版を1本選びます。
2. Researcher GemのInstructionsを選択した完成版へ入れ替えます。
3. 旧完成版の内容と新完成版の内容を同時に残しません。
4. 設定を保存します。

### 6.3 Knowledgeを変更する場合

Gem編集画面からKnowledgeのファイルを追加・削除できます。

Google Driveから追加したファイルは、Drive側で更新するとGemでも最新バージョンが使用されます。

## 7. Notes（注意事項）

- カスタムGemの新規作成・編集・削除はGeminiウェブアプリで行います。
- プレビューは保存ではありません。設定変更後は保存操作を確認します。
- Personaの現行正本は本Repository内のPersonaファイルです。Gem側だけで独自変更しないでください。
- Researcherは3完成版のうち1本だけを有効にします。
- `Knowledge` は必要な場合だけ追加します。不要な資料を機械的に追加しません。
- パスワード、APIキー、接続情報などの秘密情報をInstructionsやKnowledgeへ登録しません。
- Geminiの画面名称や配置はサービス更新で変更される可能性があります。操作表示が異なる場合はGoogle公式ヘルプの現行案内を確認してください。

## References（参照情報）

確認日：2026-08-23

- Google Gemini Apps Help: `https://support.google.com/gemini/answer/15235603?hl=ja`
- Google Gemini Apps Help: `https://support.google.com/gemini/answer/15146780?co=GENIE.Platform%3DDesktop&hl=en`

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
本資料はGemの設定に限定し、4Gemの利用方法・Workflow説明は含めない。Persona本文はInstructionsへ設定し、Knowledgeは必要に応じた追加Context・参照資料の登録に使用する。

Reason:
設定資料の責務をGemの作成・設定・更新に限定し、Personaの機能仕様や利用Workflowとの責務混在を防ぐため。Gemini公式仕様でも、Gemの指示とKnowledgeは別の設定項目として提供されている。

Rejected:
- Gemの利用方法・Workflowを本設定資料へ含める方式
