# GEM_REVIEWER Decisions

この文書は \`personas/education/GEM_REVIEWER.md\` の判断履歴を管理する。
Reviewer Persona本体には運用指示のみを保持し、判断履歴は表示しない。

## 2026-08-27

### Education Reviewerを職業訓練校生のポートフォリオレビューへ最適化

**Decision:**

Education用Reviewerの中心用途を、職業訓練校でITを学び、IT系企業・職種への就職・転職を目指すUserのポートフォリオレビューとして明確化する。

既存のEvidence重視、User-firstフロー、Solution Partner / Code Generatorとの責務境界、不要な改善要求を避ける原則は維持する。

その上で、作品目的、Scope、要求・設計・実装整合、機能、必要十分なコード品質、基本セキュリティ、test Evidence、README・伝達性、本人理解・説明可能性、採用・面接視点を中心評価軸とする。

実務向けの高度なセキュリティ・運用・AI制御資産監査は、作品の性質上必要な場合だけ条件付きで適用する。

**Reason:**

Reference用 \`CLAUDE_PERSONA.md\` Version 1.3 は、実務システムの品質・セキュリティ・AI統制を監査する用途には適しているが、生徒PFでは監査項目が前面に出すぎる。

一方、既存Education Reviewerは初心者向け説明、User自身による検証、AI間の責務分離など教育用途に適した基盤を既に持つため、新しいReviewer体系を増やすより、Education ReviewerをPF用途へ最適化する方が責務分離と保守性に優れる。

分析Evidence：\`project-notes/2026-08-27-portfolio-reviewer-fit-analysis.md\`

**Rejected:**

- Reference用Claude Personaをそのまま生徒PFレビューに使用する方式
- Reference版を単純に短縮・コピーする方式
- Education用4Gem体系へ新しいPortfolio Reviewerを追加してReviewerを二重管理する方式
- 実務最高水準の設計・運用・セキュリティ基準を全PFへ固定適用する方式

## 2026-09-23

### Reviewer Personaを7,000文字以内へ簡潔化し、判断履歴を分離

**Decision:**

\`personas/education/GEM_REVIEWER.md\` を Version 1.2 / Status Approved へ更新する。

- Persona全体を7,000文字以内にする。
- 既存の評価思想・責務境界・判定方式は維持する。
- 重複していた責務境界、評価観点、修正フロー、説明可能性、禁止事項を統合する。
- Persona本文から \`Decision & Rationale\` を削除する。
- Reviewerに関する判断履歴は本ファイルへ分離し、Persona本文からHTMLコメントで参照する。

**Reason:**

PersonaはAIへ与える実行指示であり、判断履歴を本文へ混在させると文字数を消費し、役割・評価基準・責務境界など実行時に必要な指示が埋もれるため。

既存のReviewerは内容の重複と判断履歴の混在により長大化していたため、機能を削らず構造を整理し、Personaとして必要な情報へ集中させる。

**Rejected:**

- 7,000文字を超えたまま運用する方式
- 判断履歴をPersona本文へ残す方式
- 文字数削減のため評価軸やEvidence原則そのものを削除する方式
