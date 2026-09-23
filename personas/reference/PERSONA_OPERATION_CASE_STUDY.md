<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-REFERENCE-OPERATION-001 |
| Version（バージョン） | 0.1 |
| Status（ステータス） | Draft |
| Created Date（作成日） | 2026-09-23 |
| Last Updated（最終更新日） | 2026-09-23 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | [`README.md`](README.md)<br>[`CHAT_HANDOFF_TEMPLATE.md`](CHAT_HANDOFF_TEMPLATE.md)<br>[`PERSONA_PROMPT_TEMPLATE.md`](PERSONA_PROMPT_TEMPLATE.md)<br>[`../../README.md`](../../README.md) |

<!-- Decision history: ../../project-notes/2026-09-23-persona-operation-case-study-decisions.md -->

---

# AI Operation Environment Case Study（AI運用環境実例）

## 1. Purpose（目的）

本資料は、Personaそのものを主題とするものではありません。

本資料では、職業訓練校でIT教育を担当する **O講師** が、生成AIの回答精度および利用品質の向上を目的として、日常的に検証・改善している実際の利用環境、設定構成、情報管理方法、運用方法を、一つの実践事例として公開します。

O講師は、生成AIの実用上の回答品質について、利用するモデルだけではなく、与えるContext、設定、参照情報、役割分担、情報管理方法、運用手順など、複数の要因が影響し得るという前提で継続的に検証しています。

本資料では、これらの要素をどのように構成し、どのような考え方に基づいて採用・不採用を判断しているかを、実際の運用例を通して示します。

ここで示す構成を唯一の正解として提示することを目的とはしていません。各利用者が自身の目的、利用するAIサービス、作業内容、環境に応じて設定や運用方法を検討し、より安定した、再現性のある、扱いやすいAI利用環境を構築するための参考事例として活用されることを意図しています。

---

## 2. Positioning（位置付け）

この文書はEducation用4Gem＋1の必須手順ではありません。

O講師が実際に採用しているAI利用環境・設定・情報管理・運用方法を、Reference Case Studyとして公開するものです。

重要なのは、利用できる機能をすべて有効にすることではありません。

**どの情報を、誰が、どこで管理し、どの場面でAIへ与えるのかを明確にすること**を重視します。

---

## 3. Responsibility Model（情報の責務分離）

O講師の運用では、主に次のように情報を分けています。

| Layer（層） | Responsibility（責務） | 主な情報 |
|---|---|---|
| Personal Profile | O講師自身の恒常情報 | 回答スタイル、職種、普段のPC・開発環境など |
| Persona | AIの役割と行動を定義 | Role、Responsibility、Boundary、Decision Criteria、禁止事項、Output |
| Project / Gem | 案件・用途ごとのContext分離 | プロジェクトの目的、対象となる作業領域 |
| Prompt | 今回AIへ依頼する内容 | 背景、依頼、入力、成果物、制約、完了条件 |
| Knowledge | AIから参照可能にする資料 | 仕様書、設計書、参考資料、用語集など |
| GitHub | 正確な仕様・状態・履歴の正本 | 現行仕様、設計、Decision、CURRENT.md、履歴 |
| Handoff | チャット間で必要な状態を移送 | 完了事項、確定事項、未決事項、次作業 |
| Memory等 | AIサービス側による情報再利用 | 過去会話、利用者情報など |

これらは似た情報を扱う場合がありますが、責務は同じではありません。

---

## 4. Personal Profile（恒常情報）

Personal Profileには、案件が変わっても比較的変化しにくいO講師自身の情報を置きます。

例：

- 回答スタイル
- 職種
- 普段使用するPCやOS
- 開発環境
- 恒常的な出力上の希望

一方、次のような変化しやすい情報は置きません。

- 現在のGitHub HEAD
- 現在の開発工程
- 今回だけ使用する仕様
- 一時的な未決事項

---

## 5. Persona（AIの役割と責務）

Personaでは、AIについて主に次を定義します。

- Role（役割）
- Responsibility（責務）
- Boundary（責務境界）
- Decision Criteria（判断基準）
- 禁止事項
- 回答方針
- Output（出力）

Personaの目的は、AIへ大量の情報を格納することではありません。

**このAIは何を担当し、何を担当しないのか**を継続的に明確にすることです。

そのため、プロジェクトの全資料、現在の進捗、GitHub HEAD、過去会話などをPersonaへ無制限に混在させません。

---

## 6. Project / Gem（案件・用途の分離）

ProjectやGemは、案件や用途ごとにContextを分離するために使用します。

例えば、

```text
対面指導レクチャ資料作成
PF基礎判定
SCAO設計
Repository Governance
```

など、目的や作業領域が異なる案件を同じContextへ無制限に混在させず、必要に応じて分離します。

これにより、別案件の仕様、条件、過去の判断が現在の回答へ不用意に混入することを防ぎやすくなります。

---

## 7. Prompt（今回の依頼）

Personaが **「このAIは何者か」** を定義するのに対し、Promptは **「今回は何をしてほしいか」** を伝えます。

O講師の運用では、Promptに必要な情報を整理するために **BRIDGE** を使用します。

| BRIDGE | 内容 |
|---|---|
| Background | 背景・目的 |
| Request | AIへの依頼 |
| Inputs | 使用する情報・前提 |
| Deliverables | 必要な成果物 |
| Guardrails | 制約・禁止事項 |
| Evaluation | 完了条件・評価条件 |

毎回6項目すべてを長文で書くことが目的ではありません。

不足している情報を確認し、AIが不要な推測で補完することを減らすための整理方法です。

実際に利用できる形式は [`PERSONA_PROMPT_TEMPLATE.md`](PERSONA_PROMPT_TEMPLATE.md) を参照してください。

---

## 8. Knowledge（参照資料）

Knowledgeは、AIから参照可能にしたい資料を登録するために使用します。

例：

- 現行仕様書
- 設計書
- 授業資料
- 用語集
- プロジェクト固有ルール

資料は多ければよいわけではありません。

古い資料、不要な資料、相互に矛盾する資料を追加すると、現在の回答に不要なContextが混入する可能性があります。

O講師の運用では、**現在の目的に必要で、内容が有効な資料だけを登録する**ことを基本とします。

Knowledgeそのものを正本とは扱いません。

---

## 9. GitHub as SSOT（GitHubを正本として使う）

正確性が必要な情報は、AIの記憶に依存せずGitHubで管理します。

例：

- 現行仕様
- 設計
- Persona
- 現在工程
- CURRENT.md
- Decision
- 変更履歴
- Commit

SSOT（Single Source of Truth）とは、**どの情報を正しいものとして確認するかを明確にする考え方**です。

例えば現在のHEADを確認する場合、過去の会話を頼りにせず、GitHubの現在状態を確認します。

---

## 10. Handoff（チャット間の引き継ぎ）

長い作業では、チャットやAIを切り替える場合があります。

その際、過去会話全体をそのまま移送するのではなく、次の作業に必要な状態を整理して渡します。

主な情報：

- 現在状態
- 完了事項
- 確定事項
- 採用事項
- 却下事項
- 未決事項
- 次の作業
- やらないこと
- 確認すべき正本

実際に利用できる形式は [`CHAT_HANDOFF_TEMPLATE.md`](CHAT_HANDOFF_TEMPLATE.md) を参照してください。

Handoffは正本そのものではありません。新しいAIは、必要に応じてGitHub等の正本を再確認します。

---

## 11. Memory and Automatic Context Reuse（自動情報再利用）

AIサービスには、過去会話や利用者に関する情報を後の回答へ再利用する機能が存在する場合があります。

O講師の運用では、仕様、進捗、Decision、HEADなど正確性が必要な状態情報の管理には依存しません。

利用できる機能だから採用するのではなく、**利用することで明確な効果が確認できるか**を採否判断の基準とします。

これはMemory等の機能そのものを否定するものではありません。利用目的や環境によって有効性は異なります。

---

## 12. Context Management（Context管理）

AIへ与える情報は、多ければ多いほど良いとは限りません。

例えば、

- 古い仕様
- 別案件の情報
- 矛盾する資料
- 不要なDecision
- 長すぎる会話履歴

が混在すると、現在の作業に必要な情報が埋もれやすくなります。

O講師の運用では情報量そのものより、

1. 正確性
2. 関連性
3. 最新性
4. 再現性
5. 統制性

を重視します。

基本方針は、**必要な情報を、正しい場所から、必要な範囲だけAIへ与える**ことです。

---

## 13. Actual Operation Flow（実際の運用フロー）

```text
準備
 ↓
適切なProject / Gemを選択
 ↓
Personaを確認
 ↓
GitHubの最新正本を確認
 ↓
必要なKnowledge・Handoffを確認
 ↓
BRIDGEで今回のPromptを整理

相談・作業
 ↓
AIへ依頼
 ↓
AIが担当する役割に従って処理
 ↓
O講師が内容を確認・判断

成果管理
 ↓
確定した成果をGitHubへ反映
 ↓
必要なDecisionを記録
 ↓
現在地点を更新
 ↓
必要ならHandoffを作成
```

---

## 14. Summary（まとめ）

O講師の実運用では、情報を次のように責務分離しています。

```text
O講師自身の恒常情報
→ Personal Profile

AIの役割・責務
→ Persona

案件・用途
→ Project / Gem

今回の依頼
→ Prompt / BRIDGE

参照資料
→ Knowledge

正確な仕様・状態・履歴
→ GitHub

チャット間の状態移送
→ Handoff
```

目的はAI機能を増やすことではありません。

**人間が明示的に管理できる情報は人間が管理し、AIには現在の作業に必要な正確な情報だけを渡す。**

本資料は、そのための一つの実践事例です。
