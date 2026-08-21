# CURRENT

Last Updated: 2026-08-21
Status: RECOVERY / RECONSTRUCTION

## PURPOSE

生徒へ配布可能な `ai-setup-materials` を完成させる。

単なるAI利用方法ではなく、AIの役割分担・責務分離・Evidence・検証を重視したAI活用設計を学べる教材とする。

## SAFETY HOLD

2026-08-21、AIによる決定事項統合で、Education用4Gemの旧名称 `Implementer` を現行情報として再混入させる誤りが確認された。

そのため、次の統合記録は再構築完了まで現行設計の正本として扱わない。

- `project-notes/2026-08-21-education-4gem-design-decisions.md`

原因説明だけで復旧扱いにしない。一次資料・既存決定記録・Persona現物・ユーザーの明示決定を再照合し、最新有効情報を再構築する。

## CONFIRMED SAFE

現時点で安全に確認できている事項のみ記載する。

### Education用4Gemの最新名称

```text
Researcher
Solution Partner
Code Generator
Reviewer
```

- Educationでは `Implementer` ではなく `Code Generator` を使用する。
- `GEM_CODE_GENERATOR.md` はGitHub上に実在する。
- `Code Generator` と、Cursor等で実装を担当する `Implementer` は別概念として扱う。
- 旧 `Implementer` の責務を機械的にすべて `Code Generator` へ置換してはならない。役割変更後の責務・戻し先・Doc連携は再構築対象とする。

### Persona完成状態

- Researcher Personaは未完成。
- Reviewer Personaは未完成。

### Researcher Module設計

- Researcher本体の責務自体はModule導入によって変更しない。
- Moduleで変更するのはResearcherの検索範囲・検索対象である。
- 検索対象は大きく次の3分野に分ける。
  1. 学習関連
  2. 就職活動関連
  3. PFなどの設計・開発関連
- Module正式名称は次の3つ。
  - `Learning Module`
  - `Career Module`
  - `Development Module`
- 訓練期間中は3Moduleを同時に有効にすることを基本とする。
- 学習終了後は `Learning Module` が不要になる。
- 就職決定後は `Career Module` が不要になる。
- 不要になったModuleをResearcherから外せる構成にする。
- Moduleを外した場合、その分野を検索禁止にするのではなく、Researcherの担当検索範囲から外す。
- Researcher本体には調査方法・品質基準を置き、Moduleには検索対象・検索範囲を置く。
- Researcher本体に置く内容の例：Evidence、一次情報優先、事実と推論の分離、比較、根拠付き推論、結論提示、未確認事項の明示。
- Moduleごとに調査方法・品質基準を変える設計にはしない。
- Moduleを複数Knowledgeファイルへ分割する方式は採用せず、Researcher Personaは1本のファイル内に本体とModuleを持たせる方向とする。
- 判断基準は着脱の簡単さより、Gemが必要な指示を確実に参照できることを優先する。
- Google Geminiの公式ヘルプでは複数Knowledgeファイルを追加できることは確認できるが、毎回すべてのKnowledgeファイルが必ず同じ強さで参照されることまでは保証されていないため、安全側として1ファイル構成を採用する。
- 1ファイル内で不要Moduleを外す具体的な操作方法はまだ未確定。

### 情報資産保全

- AIの能力を過信しない。
- AIは新旧決定の取り違え、旧情報復活、欠落、誤統合、推論混入を起こし得るものとして扱う。
- 重要情報資産の保全をAIの記憶・会話履歴・自己判断だけに依存しない。
- 重要決定はこまめにGitHubへ記録する。
- 名称変更・役割変更・採用・廃止・置換では、時系列と上書き関係を確認する。
- `CURRENT / SUPERSEDED / UNRESOLVED` を分離する。
- AI側で確認可能な事項をユーザーへの個別質問へ転嫁しない。
- 資料だけで一意に決まらない事項のみユーザーへ確認する。
- 「統合済み」「確定」「正本」とする前に、最新性・競合・欠落を検証する。
- 誤統合が発覚した場合、原因分析だけではなく再構築と検証を行う。

詳細：

- `project-notes/2026-08-21-ai-information-asset-safety.md`

## CURRENT TARGET

README作成を一時停止し、Education用4Gemと関連管理文書の情報資産を再構築する。

現在はResearcher / Reviewerを優先して再構築する。

## RECOVERY METHOD

1. GitHub上の関連決定記録を時系列で収集する。
2. Education Personaの現物を確認する。
3. README、旧CURRENT、関連文書を照合する。
4. 各事項を `CURRENT / SUPERSEDED / UNRESOLVED` に分類する。
5. 後続決定によって失効した旧情報を現行情報から除外する。
6. 資料だけで一意に決まらない事項のみ、まとめてユーザーへ確認する。
7. 確認済み事項から順にGitHubへこまめに記録する。
8. 再構築後、決定記録・CURRENT・README・Persona間の整合性を確認する。

## CURRENT STATE

- `project-notes/2026-08-21-ai-information-asset-safety.md` を追加済み。
- `AGENTS.md` にAI能力を過信しない安全前提と復旧ガードを追加済み。
- `project-notes/2026-08-21-education-4gem-design-decisions.md` は再構築完了まで正本扱い停止。
- README仮完成作業は復旧完了まで一時停止。
- `project-notes/2026-08-21-reconstruction-confirmed-facts.md` に、ユーザーが再確認したResearcher / Reviewerの最新状態とResearcher Module設計の確定事項を記録済み。
- `project-notes/2026-08-21-reconstruction-audit-researcher-reviewer.md` に、GitHub現物・commit履歴から確認した履歴事実を記録済み。

### Researcher監査で確認済み

- 2026-08-19版 `GEM_RESEARCHER.md` はModule構想を含まない旧段階のPersona。
- GitHub Repository内およびcommit履歴を `Module` で検索したが、2026-08-21監査時点で該当記録は検出できなかった。
- よってModule仕様はGitHub現物から推論で復元しない。
- ただし、2026-08-21のユーザー再確認により、Researcher本体の責務は維持し、検索範囲・検索対象をModuleで変更する設計であることは確定した。

### Reviewer監査で確認済み

- 2026-08-19版 `GEM_REVIEWER.md` はCode Generator追加前のPersona。
- 戻し先・リファクタリング担当として `Implementer` を含むため、その箇所は現行Education仕様としてそのまま利用しない。

### Code Generator監査で確認済み

- `GEM_CODE_GENERATOR.md` は2026-08-20に追加された。
- コード生成・既存コード解析・エラー分析・修正版コード生成等を担当する。
- 実環境への適用、IDE操作、Git操作、品質保証判定は担当しない。

## NEXT ACTION

Researcherの再構築を優先する。

1. Researcher本体について、Module導入後も変わらない責務・Evidence・出力原則を既存資料から抽出する。
2. Moduleに分離すべき検索対象・検索範囲とResearcher本体に残す事項を切り分ける。
3. `Learning Module / Career Module / Development Module` の詳細検索範囲を確定する。
4. 1ファイル内で不要Moduleをできる限り簡単かつ誤読されにくく外す具体的方法を設計する。
5. Reviewerについても監査を継続し、Code Generator化で影響を受ける項目を分離する。
6. 資料だけで決まらない事項を最後にまとめてユーザーへ確認する。

## DO NOT USE AS CURRENT SOURCE

再構築完了まで、次の文書を単独で現行設計の正本として扱わない。

- `project-notes/2026-08-21-education-4gem-design-decisions.md`
- `project-notes/2026-08-19-4gem-names.md`
- `personas/education/GEM_RESEARCHER.md`
- `personas/education/GEM_REVIEWER.md`

これらは復旧のための履歴資料として使用する。

## REFERENCES

- `project-notes/2026-08-21-ai-information-asset-safety.md`
- `project-notes/2026-08-21-reconstruction-confirmed-facts.md`
- `project-notes/2026-08-21-reconstruction-audit-researcher-reviewer.md`
- `project-notes/2026-08-21-education-4gem-design-decisions.md`（要再構築）
- `project-notes/2026-08-20-ai-education-staging.md`
- `project-notes/2026-08-19-4gem-names.md`（旧決定を含む）
- `personas/education/GEM_CODE_GENERATOR.md`
