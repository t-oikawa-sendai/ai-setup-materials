<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-REFERENCE-INDEX-001 |
| Version（バージョン） | 1.2 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-08-22 |
| Last Updated（最終更新日） | 2026-09-23 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | [`../../README.md`](../../README.md)<br>[`../education/README.md`](../education/README.md)<br>[`CHATGPT_PERSONA.md`](CHATGPT_PERSONA.md)<br>[`CLAUDE_PERSONA.md`](CLAUDE_PERSONA.md)<br>[`CURSOR_PERSONA.md`](CURSOR_PERSONA.md)<br>[`GEMINI_PERSONA.md`](GEMINI_PERSONA.md)<br>[`PERSONA_OPERATION_CASE_STUDY.md`](PERSONA_OPERATION_CASE_STUDY.md)<br>[`CHAT_HANDOFF_TEMPLATE.md`](CHAT_HANDOFF_TEMPLATE.md)<br>[`PERSONA_PROMPT_TEMPLATE.md`](PERSONA_PROMPT_TEMPLATE.md) |

---

# Reference Personas（参考用Persona）

## 1. Purpose（目的）

このディレクトリは、Education用4Gem＋1とは異なる前提で、実務構成の参考Personaと、AI利用環境・設定・運用の実践例を管理します。現在利用可能なReference文書への入口・索引です。

## 2. Recommended Reading Order（推奨する読み順）

AI運用参考資料は、次の順で読むと全体像から実際の利用方法へスムースに進めます。

| Step | 文書 | 目的 |
|---|---|---|
| 1 | [`PERSONA_OPERATION_CASE_STUDY.md`](PERSONA_OPERATION_CASE_STUDY.md) | O講師の実環境・設定・情報管理・運用方法の全体像を理解する |
| 2 | [`PERSONA_PROMPT_TEMPLATE.md`](PERSONA_PROMPT_TEMPLATE.md) | AIへ今回の依頼を出すとき、BRIDGEで必要事項を整理する |
| 3 | [`CHAT_HANDOFF_TEMPLATE.md`](CHAT_HANDOFF_TEMPLATE.md) | 長い作業でチャットやAIを切り替えるとき、現在状態を安全に引き継ぐ |

Personaそのものを参照したい場合は、下記のReference Personaから対象AIを選びます。

## 3. Difference from Education 4Gem＋1（Education用4Gem＋1との違い）

Reference Personaは、Education用4Gem＋1と次の点が異なります。

- 役割
- 利用サービス
- 実装・検証方法の前提

Education用4Gem＋1の現行手順として、そのまま流用しないでください。設計思想や運用パターンの参考として扱ってください。

## 4. Current Reference Personas（現行Reference Persona）

現在利用可能なReference文書は次のとおりです。承認された文書が追加された場合は、この索引を更新します。

- [`CHATGPT_PERSONA.md`](CHATGPT_PERSONA.md)：ChatGPT Responsibility Definition（ChatGPT向け責務定義）
- [`CLAUDE_PERSONA.md`](CLAUDE_PERSONA.md)：Claude Persona（Claudeペルソナ）
- [`CURSOR_PERSONA.md`](CURSOR_PERSONA.md)：Cursor Persona（Cursorペルソナ）
- [`GEMINI_PERSONA.md`](GEMINI_PERSONA.md)：Gemini Persona（Geminiペルソナ）

## 5. Reference Operation Materials（AI運用参考資料）

O講師が実際に使用・検証しているAI利用環境、設定、情報管理、運用方法を、再現を強制しない実践例として公開します。

- [`PERSONA_OPERATION_CASE_STUDY.md`](PERSONA_OPERATION_CASE_STUDY.md)：AI利用環境・設定・情報管理・運用方法の実践例
- [`CHAT_HANDOFF_TEMPLATE.md`](CHAT_HANDOFF_TEMPLATE.md)：チャットやAIを切り替える際の状態移送テンプレート
- [`PERSONA_PROMPT_TEMPLATE.md`](PERSONA_PROMPT_TEMPLATE.md)：BRIDGEを使って今回の依頼を整理するプロンプトテンプレート

## 6. Usage Notes（利用上の注意）

- Education領域の現行手順、Gem操作、User-firstフローは [`../education/README.md`](../education/README.md) を正とします。
- 本ディレクトリの文書は参考資料であり、Education用4Gem＋1の代替ではありません。
- O講師の実運用例は唯一の正解ではありません。利用者自身の目的、AIサービス、作業内容、環境に合わせて採否を判断してください。

## 7. Navigation（導線）

- Repository全体の入口：[`../../README.md`](../../README.md)
- Education領域の入口：[`../education/README.md`](../education/README.md)
- AI運用資料の開始地点：[`PERSONA_OPERATION_CASE_STUDY.md`](PERSONA_OPERATION_CASE_STUDY.md)
- 今回の依頼整理：[`PERSONA_PROMPT_TEMPLATE.md`](PERSONA_PROMPT_TEMPLATE.md)
- チャット切替・作業引き継ぎ：[`CHAT_HANDOFF_TEMPLATE.md`](CHAT_HANDOFF_TEMPLATE.md)

## Decision & Rationale（決定・判断理由）

### 2026-09-23

#### Reference資料の推奨導線を明示

Decision:
Reference入口に `Case Study → Prompt Template → Handoff Template` の推奨する読み順を追加する。

各文書の用途を「全体像」「日常の依頼」「チャット切替・状態移送」と分け、利用者が目的に応じて直接移動できる導線も併記する。

Reason:
3文書へのリンクは存在していたが、読む順と利用場面が明示されておらず、初見の利用者がどこから開始すべきか判断しにくかったため。

Rejected:
- 3文書を同列リンクだけで案内し、利用者自身に読む順を判断させる方式
- Root READMEから各テンプレートへ直接大量にリンクし、Reference入口を経由しない方式

### 2026-09-23

#### AI運用の実践例と再利用テンプレートをReference領域へ追加

Decision:
Reference領域へ、O講師の実際のAI利用環境・設定・情報管理・運用方法を示すCase Studyと、チャット引き継ぎ・プロンプト整理の再利用テンプレートを追加する。

これらはEducation用4Gem＋1の必須手順ではなく、各利用者が自身の環境を改善する際の参考資料として扱う。

Reason:
Persona単体の説明だけでは、実際のAI利用においてProfile、Project / Gem、Prompt、Knowledge、GitHub、Handoff、Memory等をどのように責務分離しているかが伝わりにくいため。

また、実践者を `User` と表記すると、教材を読む利用者（生徒）との区別が曖昧になるため、Case Studyでは実践者を `O講師` と表記する。

Rejected:
- Case StudyをEducation用必須手順として扱う方式
- 実践者と教材利用者の双方を `User` と表記する方式
- HandoffとPrompt TemplateをCase Study本文へ全文埋め込みし、再利用性を下げる方式

### 2026-08-23

#### Education用4Gem＋1との対比表現

Decision:
Reference領域からEducationの現行Gemini構成を指す場合は `Education用4Gem＋1` と表記する。基本4Gemそのものの役割定義を変更するものではない。

Reason:
Gemini上では基本4Gemに `Researcher Deep Research` を追加して運用することが現行仕様であり、Reference入口だけ旧 `Education用4Gem` 表記を残すと、配布構成の実体数を誤解させるため。