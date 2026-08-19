# CURRENT

Last Updated: 2026-08-19
Status: ACTIVE

## PURPOSE

生徒へ配布可能な `ai-setup-materials` を完成させる。

## CONFIRMED

- Education用Gemは4つとする。
  - `Solution Partner`
  - `Implementer`
  - `Reviewer`
  - `Researcher`
- Gem表示名とMarkdownファイル名は対応関係で迷わないよう原則一致させる。
  - `Solution Partner` → `GEM_SOLUTION_PARTNER.md`
  - `Implementer` → `GEM_IMPLEMENTER.md`
  - `Reviewer` → `GEM_REVIEWER.md`
  - `Researcher` → `GEM_RESEARCHER.md`
- 本教材ではSDDを意識し、重要な入力・判断・成果・検証結果を文書として残して次工程へ引き渡す。
- 会話そのものを正本にしない。
- 生徒自身がオーケストレーターとして、どの情報を正本として残し、次のAIへ何を渡すかを管理する。
- `Solution Partner` は「何を作るか」「何のために作るか」「どう作るか」を人間と対話しながら整理・提案・設計する。
- `Implementer` は確定した設計ドキュメントに基づいて実装・検証し、その結果を文書として残す。
- `Reviewer` は設計・実装・検証結果を独立した立場から評価し、問題・根拠・修正先を文書化する。
- リファクタリングについて詳細な専用基準書は作成しない。
- Reviewerは、重複、過度な複雑化、責務混在など保守性に影響する具体的問題を根拠付きで指摘する。
- リファクタリングの実施担当は `Implementer` とする。
- 設計変更を伴う場合は `Solution Partner` に戻す。
- `Researcher` は一次情報・公式情報を優先し、確認済み事実にはEvidenceを必ず表示する。
- Evidenceを示せない情報は確認済み事実として扱わない。
- `CURRENT.md` の通常運用はローカルGitリポジトリを基本とし、GitHubはリアルタイム同期基盤とはしない。
- 作業終了・端末切替・ローカルを直接参照できないAIへの引き継ぎ・重要なチェックポイントで commit / push する。

## CURRENT TARGET

以下7文書の整備。

- `AGENTS.md`
- `project-notes/CURRENT.md`
- `personas/education/README.md`
- `personas/education/GEM_SOLUTION_PARTNER.md`
- `personas/education/GEM_IMPLEMENTER.md`
- `personas/education/GEM_REVIEWER.md`
- `personas/education/GEM_RESEARCHER.md`

## CURRENT STATE

上記7文書を初版として作成する段階。

既存の `personas/education/GEMINI_PERSONA_DEFINITION-4Gem.md` は旧統合Draftとして残し、勝手に削除しない。

## NEXT ACTION

7文書の内容を精査し、生徒配布用として過不足・矛盾・重複がないか確認する。

## DO NOT REOPEN

- 4Gemを採用するかどうか
- 4Gemの正式名称
- 4Gemの基本的な責務分担
- SDDを意識した文書連携方針
- ResearcherのEvidence必須方針
- Reviewerのリファクタリング評価方針

## REFERENCES

- `project-notes/2026-08-19-4gem-names.md`
