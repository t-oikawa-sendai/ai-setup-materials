<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-REFERENCE-PROMPT-001 |
| Version（バージョン） | 0.1 |
| Status（ステータス） | Draft |
| Created Date（作成日） | 2026-09-23 |
| Last Updated（最終更新日） | 2026-09-23 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | [`PERSONA_OPERATION_CASE_STUDY.md`](PERSONA_OPERATION_CASE_STUDY.md) |

<!-- Decision history: ../../project-notes/2026-09-23-persona-operation-case-study-decisions.md -->

---

# Persona Prompt Template（Persona利用時プロンプトテンプレート）

## 1. Purpose（目的）

このテンプレートは、AIへ作業を依頼するときに、今回の作業に必要な情報を整理するために使用します。

Personaは、**このAIは何者で、何を担当するか**を定義します。

Promptは、**今回は何をしてほしいか**を伝えます。

両者の責務は異なります。

---

## 2. BRIDGE

本テンプレートでは、Promptに必要な情報を **BRIDGE** の6項目で整理します。

| 項目 | 意味 | 確認すること |
|---|---|---|
| **B — Background（背景）** | なぜこの作業をするのか | 現状、目的、問題 |
| **R — Request（依頼）** | AIに何をしてほしいのか | 調査、設計、生成、レビュー等 |
| **I — Inputs（入力情報）** | 何を材料として使うのか | 仕様、ファイル、URL、条件 |
| **D — Deliverables（成果物）** | 何を出力してほしいのか | Markdown、表、設計案、コード等 |
| **G — Guardrails（制約）** | 何をしてはいけないか | 変更禁止範囲、技術制約、推測禁止 |
| **E — Evaluation（完了条件）** | 何を満たせば終了か | 確認事項、品質条件、完了条件 |

---

## 3. Why BRIDGE Is Used（なぜBRIDGEを使うのか）

依頼内容に必要な条件が不足している場合、AIが不足部分を推測して補完することがあります。

その推測が利用者の意図と一致するとは限りません。

```text
必要な条件が不足
 ↓
AIが不足部分を推測
 ↓
意図と異なる回答が生成される
 ↓
利用者が修正を依頼
 ↓
AIとのやり取りが増える
 ↓
会話履歴・旧条件・修正指示が増える
 ↓
重要情報が埋もれやすくなる
 ↓
回答が迷走しやすくなる
```

BRIDGEは、長いPromptを書くための仕組みではありません。

**最初に必要な条件を整理し、不要な往復や推測による補完を減らすための確認枠組み**です。

---

## 4. Copy Template（コピー用テンプレート）

```markdown
## Background（背景）

- 現状：
- 目的：
- 解決したい問題：

## Request（依頼）

AIに実施してほしいこと：

-

## Inputs（入力情報）

使用する情報・資料：

-

確定している条件：

-

## Deliverables（成果物）

必要な成果物：

-

出力形式：

-

## Guardrails（制約）

必ず守ること：

-

変更・実施してはいけないこと：

-

推測してはいけない事項：

-

## Evaluation（完了条件）

次を満たせば完了：

-
```

---

## 5. Minimum Use（簡易版）

すべての依頼で6項目を詳細に書く必要はありません。

簡単な依頼では、必要な部分だけ使用します。

最低限、

```text
何をしたいか
何を使うか
何を出してほしいか
守る条件
何をもって完了とするか
```

が明確であれば、短いPromptでも構いません。

---

## 6. Relationship with Persona（Personaとの関係）

```text
Persona
「あなたは何者で、何を担当するAIか」

Prompt / BRIDGE
「今回は何を、どの条件でしてほしいか」
```

PromptのたびにPersonaの役割・責務・禁止事項を全文書き直す必要はありません。

逆に、今回だけの仕様、ファイル、成果物、完了条件をPersonaへ恒久的に追加する必要もありません。

---

## 7. Relationship with Other Information（他情報との関係）

```text
Personal Profile
→ 利用者自身の恒常情報

Persona
→ AIの役割・責務

Project / Gem
→ 案件・用途の分離

Prompt / BRIDGE
→ 今回の具体的依頼

Knowledge
→ 参照資料

GitHub
→ 正確な仕様・状態・履歴

Handoff
→ チャット間の状態移送
```

各情報を適切な場所へ分けることで、PersonaやPromptへ不要な情報を集中させないようにします。

---

## 8. Important Notes（注意事項）

BRIDGEは絶対的なPrompt記法ではありません。

6項目をすべて埋めればAIの回答が必ず正しくなるものでもありません。

目的は、**利用者の意図、入力、制約、完了条件をAIが判断できる状態にすること**です。

不足している重要情報がある場合は、AIへ推測させるのではなく、必要に応じて確認または未確定事項として扱います。
