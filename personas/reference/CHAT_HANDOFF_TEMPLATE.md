<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-REFERENCE-HANDOFF-001 |
| Version（バージョン） | 0.3 |
| Status（ステータス） | Draft |
| Created Date（作成日） | 2026-09-23 |
| Last Updated（最終更新日） | 2026-09-23 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | [`PERSONA_OPERATION_CASE_STUDY.md`](PERSONA_OPERATION_CASE_STUDY.md) |

<!-- Decision history: ../../project-notes/2026-09-23-persona-operation-case-study-decisions.md -->

---

# Chat Handoff Template（チャット引き継ぎテンプレート）

> **読む順：** [AI運用全体のCase Study](PERSONA_OPERATION_CASE_STUDY.md) → [Prompt Template](PERSONA_PROMPT_TEMPLATE.md) → **本Handoff Template**
>
> AIへ通常の依頼を出すだけであれば、先に [`PERSONA_PROMPT_TEMPLATE.md`](PERSONA_PROMPT_TEMPLATE.md) を使用します。本テンプレートは、チャットやAIを切り替えて継続作業するときに使用します。

## 1. Purpose（目的）

このテンプレートは、作業中にチャットやAIを切り替える場合に、次のAIへ必要な状態を明示的に引き継ぐために使用します。

過去の会話全体をそのまま移送することが目的ではありません。

**次のAIが、正本を再確認したうえで、迷わず安全に作業を再開できる状態を渡すこと**が目的です。

---

## 2. Core Principles（基本原則）

- Handoffは正本ではありません。
- GitHub等で管理されている仕様、設計、Decision、HEAD、現在状態は、再開時に正本を確認します。
- 会話履歴、Memory、Handoffだけを根拠に現行仕様を確定しません。
- 既存の `AGENTS.md`、`CURRENT.md`、対象成果物等にルールがある場合、新しいAIが独自に再設計しません。
- 確定事項と未確定事項を分離します。
- 未確認の内容を事実として扱いません。
- AI側で確認可能な内容を不要な質問として利用者へ戻しません。

---

## 3. Status Labels（確認状態）

Handoff内の事実には、必要に応じて次の状態を使用します。

| Status | Meaning |
|---|---|
| **VERIFIED** | 実物、GitHub、Git、ファイル、実行結果等で確認済み |
| **UNVERIFIED** | 報告・引き継ぎ情報はあるが、再開時点で未確認 |
| **ASSUMPTION** | 作業継続のために明示的に置いた仮定 |

`VERIFIED` は、実際に確認した事項だけに使用します。

---

## 4. Copy Template（コピー用テンプレート）

```markdown
# AI専用・新チャット文脈移行プロトコル

**Last Updated：YYYY-MM-DD**

---

## [REPOSITORY_RULES]

### Repository（対象）

- REPOSITORY_URI：
- Repository Name：
- Branch：
- Local Workspace：

### Existing Rules（既存ルール）

対象Repositoryに存在する管理文書：

- `AGENTS.md`：
- `project-notes/CURRENT.md`：
- その他の正本：

役割：

- `AGENTS.md`：AIが守る恒久ルール
- `CURRENT.md`：現在地点、完了事項、作業中、次工程
- 対象成果物：現行仕様・現行設計の正本

### Operation Policy（運用方針）

- 既存ルールを新しいAIが追加・再設計しない。
- 会話履歴、Memory、Handoffだけを正本として扱わない。
- Repository内で確認できる事項は、正本を確認してから判断する。
- 確定済み事項をEvidenceなしに再検討しない。

---

## [PROJECT_METADATA]

- Project：
- Repository：
- Branch：
- Local Workspace：
- GitHub main HEAD：
- Local HEAD：
- origin/main：
- Worktree：
- Current Target：
- Current Status：

※ 未確認の値は推測せず `UNVERIFIED` とする。

---

## [INITIALIZATION]

作業開始前に次を実施する。

### 1. Repository確認

1. 実作業用Local Workspaceを特定する。
2. Repository / remote / branchを確認する。
3. Local HEADを確認する。
4. 未commit変更の有無を確認する。
5. remoteの最新状態を取得する。
6. origin/main等の対象remote HEADを確認する。
7. Local HEADとremote HEADを比較する。
8. worktree状態を確認する。

### 2. 同期

- worktreeがcleanで、安全にfast-forwardできる場合だけ同期する。
- 未commit変更を破棄、上書き、resetして同期しない。
- localとremoteが分岐している場合は自動解消しない。
- 同期後、Local HEADとremote HEADが一致することを確認する。

### 3. 正本確認

次の順で読む。

1. `project-notes/CURRENT.md`
2. `AGENTS.md`
3. 今回の対象成果物
4. 必要なDecision / Evidence
5. 必要時のみ履歴資料

### 4. Initialization Evidence

本作業開始前に少なくとも次を確認・報告する。

- Repository
- Branch
- Local Workspace
- Local HEAD
- Remote HEAD
- HEAD一致
- 未commit変更
- Worktree状態
- 正本確認結果

GitHubやRepositoryへアクセスできないと事前に決めつけない。
実際に確認を試み、失敗した場合だけ失敗内容を報告する。

---

# 1. Background（背景）

## Purpose（目的）

-

## Problem（解決したい問題）

-

## Reason（この方法を採用した理由）

-

---

# 2. Current Status（現状）

## Repository Status

| Item | Status | Evidence |
|---|---|---|
| Repository | VERIFIED / UNVERIFIED | |
| Branch | VERIFIED / UNVERIFIED | |
| Local Workspace | VERIFIED / UNVERIFIED | |
| GitHub HEAD | VERIFIED / UNVERIFIED | |
| Local HEAD | VERIFIED / UNVERIFIED | |
| origin/main | VERIFIED / UNVERIFIED | |
| Worktree | VERIFIED / UNVERIFIED | |

## Completed（完了事項）

-

## In Progress（作業中）

-

## Not Completed（未完了）

-

---

# 3. Confirmed Facts（確定事項）

| ID | Fact | Status | Evidence |
|---|---|---|---|
| F-001 | | VERIFIED / UNVERIFIED | |
| F-002 | | VERIFIED / UNVERIFIED | |

- VERIFIEDで確認済みの確定事項をEvidenceなしに変更しない。
- UNVERIFIEDを事実として扱わない。
- 仮定を使用する場合はASSUMPTIONと明示する。

---

# 4. Decisions（決定事項）

## Adopted Decisions（採用事項）

| Decision | Reason |
|---|---|
| | |

## Rejected Decisions（却下事項）

| Decision | Reason |
|---|---|
| | |

却下済み事項を、後続Evidenceまたは利用者の新しい決定なしに復活させない。

---

# 5. Current Target（現在対象）

## Target

-

## Target Files

-

## Out of Scope（対象外）

-

## Must Not Change（変更禁止）

-

---

# 6. Unresolved Items（未決事項）

| Item | Required Decision | Decision Maker | Status |
|---|---|---|---|
| | | | UNRESOLVED |

- 未決事項をAIが推測で確定しない。
- 既に決定済みの事項を再度ASKMEしない。
- AI側で確認できる事項をASKMEへ転嫁しない。
- 判断事項がなければ停止せず次工程へ進む。

---

# 7. Rules / Prohibitions（必須ルール・禁止事項）

## Must Follow

-

## Do Not Do

-

## Stop Conditions（停止条件）

次の場合だけ作業を停止し、状態を報告する。

- 実作業用Repositoryを特定できない
- 未commit変更があり、安全な継続方法を正本から判断できない
- Localとremoteが分岐している
- 正本同士に解消できない矛盾がある
- 利用者判断が必須の未決事項がある
- 権限、network、tool等により必須Evidenceを確認できない

「念のため確認」だけを理由に停止しない。

---

# 8. Next Action（次の作業）

1.
2.
3.

## Completion Criteria（完了条件）

-

---

# 9. Validation（検証）

今回必要な検証だけを記載する。

| Validation | Result | Evidence |
|---|---|---|
| 対象差分確認 | PASS / FAIL / NOT RUN | |
| 既存validator | PASS / FAIL / N/A | |
| `git diff --check` | PASS / FAIL / NOT RUN | |
| build / test | PASS / FAIL / N/A / NOT RUN | |
| 実機・画面確認 | PASS / FAIL / N/A / NOT RUN | |

実行していない検証をPASSと記載しない。

---

# 10. Commit / Push Status（Git保存状態）

- Commit：実施 / 未実施
- Commit SHA：
- Commit Message：
- Push：SUCCESS / FAILED / 未実施
- GitHub main HEAD：
- Local HEAD：
- origin/main：
- HEAD一致：
- Worktree：

commit / pushを実施していない場合は、その旨を明示する。

---

# 11. References（確認すべき正本）

-
-
-

---

# 12. Completion Report（完了報告）

- 対象：
- 変更ファイル：
- 変更内容：
- 検証結果：
- Commit：
- Push：
- HEAD：
- Worktree：
- 想定外変更：
- 未完了事項：

---

# 13. Handoff Summary（引き継ぎ要約）

## Current State

-

## Next Step

-

## Important Notes

-
```

---

## 5. Usage（使い方）

すべての欄を必ず埋めることが目的ではありません。

案件に存在しない項目は `N/A` とし、未確認事項は `UNVERIFIED` とします。

重要なのは、次のAIが以下を区別できる状態にすることです。

- 何が確認済みか
- 何が未確認か
- 何が決定済みか
- 何が却下済みか
- 何が未決か
- 何を変更してよいか
- 何を変更してはいけないか
- 次に何を行うか
- どの正本を確認するか

---

## 6. Handoff and SSOT（Handoffと正本）

```text
GitHub / Repository Documents
→ 正確な現行仕様・状態・Decision・履歴を保持

Handoff
→ 次のAIが作業を再開するための現在地点と確認順を伝える
```

HandoffはGitHubや対象成果物の代替正本ではありません。

新しいAIはHandoffを入口として利用し、必要な正本を確認してから作業を継続します。


---

## 7. Navigation（導線）

- AI運用全体を確認する：[`PERSONA_OPERATION_CASE_STUDY.md`](PERSONA_OPERATION_CASE_STUDY.md)
- 今回の依頼を整理する：[`PERSONA_PROMPT_TEMPLATE.md`](PERSONA_PROMPT_TEMPLATE.md)
- Reference資料一覧へ戻る：[`README.md`](README.md)
- Repository全体へ戻る：[`../../README.md`](../../README.md)
