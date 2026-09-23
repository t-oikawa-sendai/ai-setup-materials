# Persona Operation Reference Decision & Rationale

対象成果物：

- `personas/reference/PERSONA_OPERATION_CASE_STUDY.md`
- `personas/reference/CHAT_HANDOFF_TEMPLATE.md`
- `personas/reference/PERSONA_PROMPT_TEMPLATE.md`

本ファイルは、上記Reference公開資料の判断履歴を管理する。

## Decision & Rationale（決定・判断理由）

### 2026-09-23

#### O講師の実AI運用環境をReference Case Studyとして公開

Decision:

O講師が、生成AIの回答精度および利用品質の向上を目的として日常的に検証・改善している実際の利用環境、設定構成、情報管理方法、運用方法を、Reference Case Studyとして公開する。

Case StudyはPersonaそのものを主題とせず、Personal Profile、Persona、Project / Gem、Prompt、Knowledge、GitHub、Handoff、Memory等を含むAI利用環境全体を扱う。

Education用4Gem＋1の必須手順にはしない。

Reason:

Persona単体の説明だけでは、実際のAI利用において複数の情報源・設定・運用手段をどのように責務分離し、回答品質の安定化を図っているかを示せないため。

実運用を唯一の正解として提示せず、利用者自身が環境を改善する際の比較・検討材料として公開する。

Rejected:

- Personaだけを主題とする資料に限定する方式
- O講師の運用をEducation用必須手順として扱う方式
- 利用可能なAI機能を一律に有効化することを推奨する方式

### 2026-09-23

#### 実践者をO講師と表記

Decision:

Case Study内では、実環境・実設定を公開する実践者を `O講師` と表記する。

教材・参考資料を読む人は `利用者` とし、実践者と読者を区別する。

Reason:

既存Education資料では `User` が利用者（生徒）を意味するため、Case Studyの実践者まで `User` とすると、誰の環境・判断・運用を説明しているのかが曖昧になるため。

Rejected:

- 実践者と読者の双方を `User` と表記する方式

### 2026-09-23

#### Case Study / Handoff / Prompt Templateの3文書へ責務分離

Decision:

AI運用Reference資料を次の3文書へ分離する。

1. `PERSONA_OPERATION_CASE_STUDY.md`：実運用環境・設定・情報管理・運用方法を説明
2. `CHAT_HANDOFF_TEMPLATE.md`：チャットやAI間の状態移送に使用
3. `PERSONA_PROMPT_TEMPLATE.md`：今回の依頼条件をBRIDGEで整理

Handoffは正本の代替にせず、GitHub等の正本を確認するための現在地点・状態移送手段として扱う。

Reason:

説明資料と毎回再利用するテンプレートは利用目的が異なるため。1文書へ統合するとCase Study本文が長くなり、Handoff / Prompt Templateのコピー・再利用性も下がる。

Rejected:

- 3つの内容をCase Study 1文書へ全文統合する方式
- Handoffを仕様・Decision・HEAD等の正本として扱う方式

### 2026-09-23

#### Prompt整理にBRIDGEを採用

Decision:

Promptに必要な情報を整理する枠組みとして、次のBRIDGEを使用する。

- Background（背景）
- Request（依頼）
- Inputs（入力情報）
- Deliverables（成果物）
- Guardrails（制約）
- Evaluation（完了条件）

BRIDGEは6項目を毎回長文で埋めることを目的とせず、必要条件の不足を確認するための枠組みとして扱う。

Reason:

依頼条件が不足した状態でAIが不足部分を推測すると、利用者の意図と異なる回答、修正の往復、会話履歴の長大化につながり、重要情報が埋もれやすくなるため。

Rejected:

- 毎回6項目すべてを詳細記述することを義務化する方式
- BRIDGEをPersonaの代替として扱う方式


### 2026-09-23

#### Handoff TemplateへRepository再開手順とEvidence管理を復旧

Decision:

`CHAT_HANDOFF_TEMPLATE.md` を Version 0.2 / Draft へ更新し、以前から実運用で使用しているGitHub Project向け引き継ぎ要素を復旧する。

追加・復旧する主な要素：

- `REPOSITORY_RULES`
- Repository / Branch / Local Workspace / Local HEAD / remote HEAD / Worktree
- 作業開始前のGit同期・正本確認手順
- Initialization Evidence
- VERIFIED / UNVERIFIED / ASSUMPTION
- Current Target / Out of Scope / Must Not Change
- Stop Conditions
- Validation
- Commit / Push Status
- Completion Report

Reason:

Version 0.1は、背景・確定事項・Decision・未決事項等の状態移送は含んでいたが、O講師が従来使用している引き継ぎプロトコルに必要なRepository再開手順、Git同期Evidence、確認状態、停止条件、完了報告が欠落していたため。

Handoffの目的は要約だけではなく、新しいAIが正本を確認し、安全に作業を再開できる状態を渡すことである。

Rejected:

- Version 0.1の簡易テンプレートをそのまま正式利用する方式
- HEAD、worktree、同期状態等を会話記憶だけで引き継ぐ方式
- VERIFIED / UNVERIFIEDを区別せず、すべてを確定情報として扱う方式


### 2026-09-23

#### Reference AI運用3文書の導線を一本道化

Decision:

Reference AI運用資料の推奨導線を次に統一する。

```text
Reference README
  ↓
AI Operation Environment Case Study
  ↓
Persona Prompt Template
  ↓ 必要時
Chat Handoff Template
```

Case Studyには資料セットの使い方と次に読む文書を追加する。
Prompt / Handoff Templateには、Case Study・相互テンプレート・Reference README・Root READMEへの戻り導線を追加する。

Reason:

各文書へのリンク自体は存在していたが、開始地点、推奨読順、利用場面、戻り先が明確でなく、初見の利用者が文書間を移動するときに迷う可能性があったため。

Rejected:

- 3文書を同列の独立資料として扱い、前後関係を示さない方式
- 各文書から戻り先を示さず、ブラウザの戻る操作だけに依存する方式
