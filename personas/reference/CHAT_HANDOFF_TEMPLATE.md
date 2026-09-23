<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-REFERENCE-HANDOFF-001 |
| Version（バージョン） | 0.1 |
| Status（ステータス） | Draft |
| Created Date（作成日） | 2026-09-23 |
| Last Updated（最終更新日） | 2026-09-23 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | [`PERSONA_OPERATION_CASE_STUDY.md`](PERSONA_OPERATION_CASE_STUDY.md) |

<!-- Decision history: ../../project-notes/2026-09-23-persona-operation-case-study-decisions.md -->

---

# Chat Handoff Template（チャット引き継ぎテンプレート）

## 1. Purpose（目的）

このテンプレートは、作業中にチャットやAIを切り替える場合に、次のAIへ必要な状態だけを明示的に引き継ぐために使用します。

過去の会話全体をそのまま移すことが目的ではありません。

**次のAIが迷わず作業を再開するために必要な情報を整理して渡すこと**が目的です。

---

## 2. Important Rule（重要ルール）

このHandoffは正本ではありません。

仕様、設計、現在HEAD、Decision等について正確性が必要な場合、新しいAIはGitHubその他の正本を確認します。

Handoffの情報だけを根拠に、既存の正本を変更しません。

---

## 3. Copy Template（コピー用テンプレート）

```markdown
# AI専用・新チャット文脈移行プロトコル

**Last Updated：YYYY-MM-DD**

## [PROJECT_METADATA]

- Project：
- Repository：
- Branch：
- GitHub main HEAD：
- Current Target：
- Current Status：

---

## [INITIALIZATION]

新しいAIは、作業開始前に正本を確認する。

確認順：

1. Repositoryの現在状態
2. CURRENT.md
3. AGENTS.md
4. 今回の作業対象となる正本
5. 必要なDecision / Evidence

確認前に、確定仕様を推測して変更しない。

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

## Completed（完了事項）

-

## In Progress（作業中）

-

## Not Completed（未完了）

-

---

# 3. Confirmed Facts（確定事項）

- F-001：
- F-002：

確定事項はEvidenceなしに変更しない。

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

---

# 5. Unresolved Items（未決事項）

| Item | Required Decision | Decision Maker |
|---|---|---|
| | | |

未決事項をAIが推測で確定しない。

---

# 6. Current Target（現在対象）

-

---

# 7. Do Not Do（やらないこと）

-

---

# 8. Next Action（次の作業）

1.
2.
3.

---

# 9. References（確認すべき正本）

-
-
-

---

# 10. Handoff Summary（引き継ぎ要約）

## Current State

-

## Next Step

-

## Important Notes

-
```

---

## 4. Usage（使い方）

すべての欄を埋めることが目的ではありません。

次のAIが再開するために必要な情報だけを残します。

既に正本へ記録されている詳細をHandoffへ大量に複製する必要はありません。

Handoffには、**どこを確認すれば正しい情報が分かるか**を示すことを重視します。

---

## 5. HandoffとGitHubの関係

```text
GitHub
→ 正確な現行情報・仕様・Decisionを保持

Handoff
→ 次のAIが作業を再開するための現在地点を伝える
```

HandoffはGitHubの代替ではありません。

新しいAIはHandoffを入口として使用し、必要な正本を確認してから作業を継続します。
