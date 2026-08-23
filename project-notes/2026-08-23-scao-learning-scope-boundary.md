# SCAO Learning Scope Boundary

Last Updated: 2026-08-23
Status: CONFIRMED DECISION RECORD

## Purpose

`ai-setup-materials` と SCAO Learning側Repositoryの責務境界を明確化する。

## ai-setup-materialsで扱う範囲

`ai-setup-materials` は、AI Personaと、そのPersonaを実際に利用するために直接必要な設定・運用資料を扱う。

扱う内容：

- Personaの定義
- Personaの役割・責務境界
- Personaの利用方法
- AIサービスへのPersona設定方法
- Persona運用に必要な資料

## SCAO Learning側へ委譲する範囲

以下は一般的なAI学習・設計思想としてSCAO Learning側で扱う。

### AI基礎概念

- Promptの詳細説明
- Contextの詳細説明
- Context Window

### AI技術概念

- RAG
- Knowledgeの技術的仕組み
- Embedding
- Vector Database
- AI Agent
- Tool利用
- Memory
- Planning
- 自律実行

### Persona概念の発展説明

- UX Design Persona
- AI Personaとの違い
- Persona設計思想の詳細

### AI活用設計

- AIオーケストレーション
- 複数AI活用設計
- Human-in-the-loopの詳細
- AI活用プロセス設計

### 開発工程学習

- 要求整理
- 要件定義
- 設計
- 実装
- テスト
- レビュー
- Deploy

## ai-setup-materials内で扱う概要

上記概念は必要に応じて概要のみ扱い、詳細説明はSCAO Learning側へ導線を張る。

対象：

- Personaとは何か
- AIへ役割・責務を与える考え方
- 役割分担の効果
- Evidence確認の重要性
- Humanが最終判断する考え方
- Knowledgeとの関係（概要）
- Prompt / Contextとの関係（概要）

## README設計方針

`README.md` はAI Personaの入口として、一般概念とRepository内での利用方法を説明する。

詳細なAI技術説明はSCAO Learning側の責務とする。

## 運用方針

設計判断・責務境界が確定した時点で記録する。

後工程でまとめて記録することで、判断理由や委譲範囲が失われることを防ぐ。
