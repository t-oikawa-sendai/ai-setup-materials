# Portfolio Reviewer適合性分析

Date: 2026-08-27
Status: REVIEW EVIDENCE / NO SPEC CHANGE

## 1. 目的

Reference用 `CLAUDE_PERSONA.md` Version 1.3 を、職業訓練校でこれからIT系企業・業種への転職を目指す生徒のポートフォリオレビューに利用する観点から精査した結果を記録する。

本記録は分析Evidenceであり、Persona仕様の変更決定ではない。Persona本体の再作成・変更はまだ実施しない。

## 2. VERIFIED: Repository上の現行構成

- `personas/reference/CLAUDE_PERSONA.md`
  - Version: 1.3
  - Status: Approved
  - Role: `Strict Code Reviewer and Security Engineer`
  - ソフトウェアレビュー、正本文書レビュー、AI制御資産レビューを対象とするReference用Reviewer。
- `personas/education/GEM_REVIEWER.md`
  - Version: 1.0
  - Status: Approved
  - 学習途中のUserを対象とし、Solution Partnerの設計成果物、Code Generator生成コード、Userのtest・検証Evidenceを独立評価するEducation用Reviewer。
- Repositoryでは `personas/reference/` と `personas/education/` の責務が既に分離されている。

## 3. 分析結論

Reference用 `CLAUDE_PERSONA.md` Version 1.3 を、そのまま生徒のポートフォリオレビューに使用するのは適切ではない。

理由は、Reference版の中心目的が「実務システムを品質・セキュリティ・統制の観点から監査し、品質ゲートを判定すること」であり、生徒PFで中心にすべき「作品としての完成度、本人理解、説明可能性、採用担当者への伝達性」と評価目的が異なるためである。

これはReference版の品質不足ではなく、用途不一致である。

## 4. Reference版で生徒PF用途には重すぎる要素

### 4.1 全体レビュー前段の実務監査

Reference版は全体レビューで、データ主体、アカウント入口、ロール別データ露出表を必須とする。

業務システム監査では有効だが、一般的な学習用CRUD、Todo、予約、検索、学習管理等のPFで常時必須にすると、作品評価より監査作業が前面に出る。

### 4.2 個人情報・セキュリティ確認の深さ

Reference版は収集目的、保持期間、削除・匿名化経路、入力ラベル・表示箇所・設計文書の突合まで要求する。

PF標準レビューでは、秘密情報のGit混入、基本的な認証・認可、入力値検証、代表的なInjection、個人情報の不用意な公開等を中心とし、高度な確認は作品の性質に応じた条件付き評価とする方が目的に合う。

### 4.3 Code Headers

Reference固有のコードヘッダ検査は、一般的な生徒PFの価値評価とは直接関係しない。

### 4.4 Lifecycle Verification

削除→再投入、複数値での同一性、運用との整合などは、DB・更新ロジックを持つ作品では有効だが、全PFの固定必須項目にすると重い。

### 4.5 AI Control Assets Review

AI制御資産のインベントリ、ロード条件、強制力、適用範囲、Conflict、Enforcement、Driftの監査は、Agent型AIやAI開発環境を本格運用するRepositoryには有用である。

一方、一般的な生徒PFレビューの標準評価軸ではない。

### 4.6 本番投入中心の出力

Reference版の `本番投入可否`、CRITICAL/HIGH等の重大度体系は実務監査向けであり、PFレビューでは提出準備・改善優先度を理解しやすい表現の方が適合する可能性が高い。

## 5. Reference版から継承価値が高い要素

次はEducation用Reviewerでも維持する価値が高い。

- VERIFIED / UNVERIFIED / ASSUMPTIONによるEvidence分離
- Evidenceのない指摘を確定しない
- 仕様・設計・実装・test結果の整合性確認
- 不要な全面改修、過度な抽象化、共通化、リファクタリング、機能追加を要求しない
- 問題のない範囲へ改善提案を広げない
- 最小修正を優先する
- 実装担当とReviewerを分離する
- 自身の指摘を反証する姿勢
- Userへ迎合して結論を変更しない
- AIが未実行のtest結果や成功Evidenceを生成しない

## 6. 生徒PFレビューで中心にすべき評価軸

### 6.1 作品目的

- 誰のための作品か
- 何を解決する作品か
- なぜ作ったか
- 何を完成とするか

### 6.2 Scope

- PFとして完成させる範囲が明確か
- 機能を広げすぎていないか
- 主要機能が完成しているか
- 機能数より完成度を優先できているか

### 6.3 要求・要件・設計整合

- 要求 → 要件 → 設計 → 実装が矛盾していないか
- 実装だけが先行し、目的や設計と乖離していないか

### 6.4 Functionality

- 主要機能が正常に動作するか
- 基本的な異常入力で致命的に破綻しないか
- CRUD等、作品の中心となる処理が成立するか

### 6.5 Code Quality

評価基準を「実務最高水準」にしない。

- User本人が読めるか
- User本人が説明できるか
- 責務が極端に混在していないか
- 不要な複雑化がないか
- 採用した構造や技術の理由を説明できるか

初心者だから品質を甘くするのではなく、「初心者PFとして必要十分な品質」を評価する。

### 6.6 Basic Security

- 秘密情報をGitHub等へ公開していないか
- 認証・認可を簡単に迂回できないか
- 基本的な入力値検証があるか
- SQL Injection、Command Injection、XSS等、作品に関係する代表的リスクが放置されていないか
- 個人情報を不用意に公開していないか

高度な実務セキュリティ監査は、作品の性質に応じて追加する。

### 6.7 Test / Evidence

- User自身が実行・確認したEvidenceがあるか
- AI生成testを実行済みと誤認していないか
- 主要機能の確認結果を説明できるか

### 6.8 README・成果物の伝達性

- READMEを見て何の作品か分かるか
- 使用技術、主要機能、実行方法等が整理されているか
- 作品の工夫点が伝わるか
- GitHubを開いた第三者が迷わないか

### 6.9 Explainability（本人理解・説明可能性）

生徒PFでは独立した重要評価軸とする価値が高い。

- 自分のコードを説明できるか
- なぜその技術を選んだか説明できるか
- なぜその設計にしたか説明できるか
- 問題が発生したとき、原因と対応を自分の言葉で説明できるか

AIを利用して作成したこと自体を問題としない。問題は「AI生成物が動作しているが、User本人が理解・説明できない状態」である。

### 6.10 採用・面接視点

- 採用担当者が短時間で作品の目的と主要機能を把握できるか
- Userが自分の担当・工夫・判断を説明できるか
- 苦労した点と解決方法を説明できるか
- 技術選定・設計判断について面接で質問されたときに説明できるか

## 7. 現行Education Reviewerへの適合性分析

現行 `personas/education/GEM_REVIEWER.md` は、Reference版とは異なり、既に次のEducation向け要素を持つ。

- 学習途中のUserを読者とする
- Evidence取得をUser自身の作業として扱う
- User-firstでReviewer結果を返す
- User自身のコード修正を学習機会として許容する
- Code Generator / Solution Partner利用を強制しない
- 専門用語を必要に応じて説明する
- 不要な改善要求を広げない

したがって、Repository構造を踏まえると、新たに「Professional Reviewer」を追加して二重管理する必要性は低い。

現行の責務分離は既に次の形で成立している。

```text
Reviewer
├─ personas/education/GEM_REVIEWER.md     ← 生徒向け
└─ personas/reference/CLAUDE_PERSONA.md  ← 実務参考
```

一方で、Education Reviewerには以下が明示的な中心評価軸として不足している。

- PFの目的・対象者・完成条件
- PFとしてのScope妥当性
- 本人理解・説明可能性
- README・成果物の伝達性
- 採用担当者・面接官から見た評価
- PF提出前の改善優先順位

## 8. Repository-aware Recommendation（未決定の推奨）

現時点の推奨は次のとおり。

1. `personas/reference/CLAUDE_PERSONA.md` Version 1.3 は実務参考Reviewerとして維持する。
2. 生徒PF用途は `personas/education/GEM_REVIEWER.md` を対象に再設計する。
3. Reference版を単純に短縮・コピーしない。
4. Education版では、Evidence・非迎合・整合性・最小修正という既存の強みを維持する。
5. その上で、PF完成度、本人理解、説明可能性、README、採用・面接視点を中心評価へ追加する。
6. 実務監査項目は、作品の性質に応じて必要な場合だけ適用する。
7. Education用4Gem体系を増やすことは、現時点では推奨しない。

この節は分析に基づく推奨であり、User決定ではない。Persona仕様へは未反映。

## 9. 再設計時に判断が必要な事項

次はPersona再作成時に確定する必要があるが、本記録では未決定とする。

- PFレビューの標準出力形式
- 提出準備度をどの表現で示すか
- `PASS / PASS WITH NOTES / REWORK REQUIRED / BLOCKED` を維持するか、初心者向け表現へ変更するか
- README・採用視点を常時評価とするか、対象がPFの場合だけの評価とするか
- PF提出可否の目安をReviewerが出すか、改善優先度のみを出して最終判断をUserに残すか
- 現行Education Reviewerのどの章を維持・統合・削除するか

## 10. 現時点の状態

- Reference Claude Persona変更: 未実施
- Education Reviewer変更: 未実施
- Persona再作成: 未実施
- 本記録: 分析Evidenceのみ
