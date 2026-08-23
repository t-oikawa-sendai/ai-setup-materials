# Chat Transition Handoff

Last Updated: 2026-08-23

## Purpose

新チャット移行時の再開情報。会話履歴ではなく、本Repositoryの正本と本記録を基準にする。

## Repository Scope

`ai-setup-materials` は AI Persona と、そのPersonaを利用するために直接必要な設定・運用資料に特化する。

対象外：
- 一般的な生成AI学習教材
- 要求定義・要件定義・設計などの一般教材
- アプリ開発用7文書
- 他Repositoryを正本とする教材本文・設計文書

7文書は別Repository管理。
ASKME迎合禁止は独立事項として扱わない。

## Confirmed Persona Facts

Education用4Gemの確定名称：

- Researcher
- Solution Partner
- Code Generator
- Reviewer

`Implementer` はEducation用4Gem名称ではない。
Code Generator と Cursor等の実装担当は別概念として扱う。

## README設計方針（検討確定事項）

README：概念理解の入口

扱う内容：
- Personaとは
- Personaは人格ではなく役割・責務・行動方針の定義
- Prompt / Context / Persona の関係（概要）
- Knowledgeとの違い（概要）
- Evidenceの考え方
- Humanが最終判断すること
- 4Gem概要
- 利用Workflow概要
- 詳細資料への導線

詳細は別文書へ分離する。

## 用語方針

初心者向け説明を基本とするが、技術用語・専門用語は削除しない。

初出時：
正式用語 + 日本語説明

文書種別で調整する。

## SCAO Learning Kitへ委譲する内容

`ai-setup-materials` では詳細説明しない。

- Prompt Engineering詳細
- Context Window
- RAG
- AI Agent
- UX Persona等のPersona概念比較
- AI技術そのものの詳細

## 注意事項

このチャットで出た以下の分類は未確定であり、正本事項ではない。

- 開発領域Persona
- 就活領域Persona
- 学習領域Persona

今後の設計では、既存正本・決定記録・Persona現物を確認し、推測で分類体系を追加しない。

## Workflow検討状況

`PERSONA_WORKFLOW.md` の位置付けは未確定。

確定していること：
- WorkflowはPersonaを利用するためのプロセスとして検討する。
- 現在確定しているEducation用4Gemを基準に考える。
- 将来拡張については、確定事項と設計案を分離する。
