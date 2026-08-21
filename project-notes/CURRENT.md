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
- `personas/education/GEM_RESEARCHER.md` は旧版・廃止版ではなく、現在のResearcher本体のベースである。
- `GEM_RESEARCHER.md` はModule追加を含む最終構成が未反映のため未完成であり、完成済み配布Personaとしてはまだ扱わない。
- 3パターンのResearcher Personaがすべて完成した時点で、`GEM_RESEARCHER.md` を旧版として扱う。それまでは旧版化しない。

### Researcher Module設計

- Researcher本体の責務自体はModule導入によって変更しない。
- Moduleで変更するのはResearcherの検索範囲・検索対象である。
- Module正式名称は次の3つ。
  - `Learning Module`
  - `Career Module`
  - `Development Module`
- Researcher本体には調査方法・品質基準を置き、Moduleには検索対象・検索範囲を置く。
- Moduleごとに調査方法・品質基準を変える設計にはしない。
- Module構成変更時もResearcher本体の責務・調査方法・品質基準は変更しない。
- Gemへ複数のResearcher Moduleファイルを同時登録する方式は採用しない。
- Gemには、その時点で必要なModule構成を含む完成済みResearcherファイルを1本だけ登録する。

### Researcher Persona本文構造

- Researcher本体を先に記載し、Module群はResearcher本体の後ろに配置する。
- 各完成版ファイルの冒頭に `Active Modules` を明示し、そのファイルで有効なModuleを列挙する。
- 有効Module外の質問への案内は、各Module固有ルールではなくResearcher本体の共通ルールとして明記する。
- 3完成版ファイルのResearcher本体は完全に同一内容とする。ファイル間で変わるのは有効なModule構成だけとする。
- Module見出しは正式英語名を維持し、日本語を併記する。
  - `Learning Module（学習）`
  - `Career Module（就職活動）`
  - `Development Module（設計・開発）`

### Researcher 配布ファイル

教材として次の3完成版ファイルを提供する方式を正式採用する。

1. `GEM_RESEARCHER_FULL.md`
   - Researcher本体 + Learning + Career + Development
2. `GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
   - Researcher本体 + Learning + Development
3. `GEM_RESEARCHER_DEVELOPMENT.md`
   - Researcher本体 + Development

- 各ファイルは単独でResearcher Personaとして成立する完全な独立ファイルとする。
- ユーザーはPersona本文を編集してModuleを削除するのではなく、必要な完成済みファイルへ入れ替える。
- 3パターンは学習教材として用意する代表構成であり、利用者のあらゆる状態を完全網羅するサービスにはしない。
- `Career + Development` 等、教材にない組み合わせが必要な場合は、利用者が学習内容をもとに自己判断で作成できる位置づけとする。
- ファイル切替のタイミングはユーザーの任意とし、教材側で強制条件にはしない。

### Module検索範囲

#### Learning Module

基準資料：`2606e宮城_日別計画表.pdf`

- ユーザー確認により、このPDFは6e宮城のスケジュールであり、全コースで異なるのは日付だけで、訓練内容・日程構成は同じ。
- したがって、Learning ModuleではPDFの日付を検索範囲の判断材料にせず、科目・訓練内容を全コース共通の基準として扱う。
- PDFから確認できるLearning Moduleの基本検索範囲は次のとおり。
  1. 安全衛生・IT基礎
  2. Webデザイン演習
  3. Javaプログラミング基礎①〜④
  4. Javaプログラミング実践①〜④
  5. Pythonプログラミング基礎①〜④
  6. Pythonプログラミング実践①〜④
  7. データベース基礎①〜②
  8. ソフトウェア開発演習①〜④
- 開講式・オリエンテーション、対面指導そのもの、就職支援、ハローワーク来所、キャリアコンサルティング、修了式はLearning Moduleの技術学習範囲として扱わない。
- 就職支援・ハローワーク・キャリアコンサルティング等はCareer Module側で扱う。
- 習熟度確認テスト、成績考査、修了考査は独立した技術分野としては扱わない。
- PDFに科目名として明記されていなくても、現在の学習内容を理解・問題解決するために直接必要な周辺知識・前提知識は検索対象に含める。
- 検索範囲は無制限にIT全般へ広げず、カリキュラムを起点として、現在の学習・疑問解決に直接必要な範囲までとする。
- 生成AI・AI活用をLearning Moduleの検索対象に明示的に含める。
- カリキュラム外の技術でも、現在の学習との関連を説明でき、学習目的で調査する場合はLearning Moduleの対象に含める。
- ポートフォリオ制作や具体的なシステム設計・技術選定として扱う場合はDevelopment Moduleの領域とする。

#### Career Module

- 基本対象はIT分野への就職活動。
- ただし対象職種・業界は固定しない。
- ユーザーのプロンプトで対象を変更できる。
- 例：事務職、営業職、製造業など。

#### Development Module

- 学習成果物、ポートフォリオ、小規模開発を中心とする。
- 技術・フレームワーク、API・ライブラリ・OSS、公式仕様、技術比較、ホスティング・DB、セキュリティ上の事実、実装判断のための技術情報、既存コードやOSS理解のための関連資料等を調査対象とする。

#### Module横断

- 質問が複数の有効Moduleにまたがる場合、有効なModuleを横断して調査する。
- 調査結果は1つに統合して提示する。

#### 有効Module外の質問

- 現在有効でないModuleに属する質問を通常どおり調査しない。
- 現在のResearcher Personaの担当検索範囲・責務を明確に伝える。
- 必要に応じて適切な完成済みResearcher Personaファイルへ入れ替えるよう案内する。
- 単に「検索禁止」と返すのではなく、担当外の理由と切替先が利用者に分かる形にする。

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
- `project-notes/2026-08-21-reconstruction-confirmed-facts.md` に、Researcher 3完成版ファイル方式、Module検索範囲、Persona本文構造のユーザー再確認事項を記録済み。
- `project-notes/2026-08-21-reconstruction-audit-researcher-reviewer.md` に、GitHub現物・commit履歴から確認した履歴事実と現行位置づけを記録済み。

### Researcher監査で確認済み

- `personas/education/GEM_RESEARCHER.md` は旧版ではなく、現在のResearcher本体のベースである。
- 現在の `GEM_RESEARCHER.md` はModule構想をまだ本文に含まないため未完成である。
- Module導入によってResearcher本体の責務は変更せず、検索範囲・検索対象をModuleで変更する。
- したがって、`GEM_RESEARCHER.md` の本体責務・Evidence・調査原則は現行Researcher再構築の基礎として扱う。
- 3パターンのResearcher Personaがすべて完成した時点で、`GEM_RESEARCHER.md` を旧版へ切り替える。
- 3つの完成済み独立Personaファイルを用意し、Gemには常に1つだけ登録する方式を正式採用した。
- Researcher本体を先に置き、Module群を後ろに配置する構造を採用した。
- 各完成版ファイルの冒頭でActive Modulesを明示する。
- 有効Module外の質問への案内をResearcher本体の共通ルールとする。
- 3ファイルのResearcher本体は完全同一とし、有効Moduleだけを変える。
- Module見出しは正式英語名に日本語を併記する。
- Career / Development / Module横断 / 有効Module外の挙動は確定した。
- `2606e宮城_日別計画表.pdf` とユーザー確認により、Learning Moduleの基本検索範囲も確定した。
- Learning Moduleは直接関連する周辺知識・前提知識、生成AI・AI活用、学習目的で関連を説明できるカリキュラム外技術まで含める。

### Reviewer監査で確認済み

- 2026-08-19版 `GEM_REVIEWER.md` はCode Generator追加前のPersona。
- 戻し先・リファクタリング担当として `Implementer` を含むため、その箇所は現行Education仕様としてそのまま利用しない。

### Code Generator監査で確認済み

- `GEM_CODE_GENERATOR.md` は2026-08-20に追加された。
- コード生成・既存コード解析・エラー分析・修正版コード生成等を担当する。
- 実環境への適用、IDE操作、Git操作、品質保証判定は担当しない。

## NEXT ACTION

Researcherの再構築を優先する。

1. 現行ベース `GEM_RESEARCHER.md` の本体責務・Evidence・出力原則を維持したまま、確定した共通Moduleルールを組み込む。
2. 確定済みの検索範囲と本文構造に基づき、3完成版Researcher Personaを作成する。
3. 3ファイル間でResearcher本体が完全同一であること、有効Moduleだけが異なることを検証する。
4. 3完成版すべての完成を確認した後、`personas/education/GEM_RESEARCHER.md` を旧版へ切り替える。旧版化後の物理的な保管方法はその時点で決める。
5. Reviewerについて監査を継続し、Code Generator化で影響を受ける項目を分離する。

## DO NOT USE AS COMPLETED CURRENT SOURCE

再構築完了まで、次の文書を単独で現行の完成仕様として扱わない。

- `project-notes/2026-08-21-education-4gem-design-decisions.md`
- `project-notes/2026-08-19-4gem-names.md`
- `personas/education/GEM_REVIEWER.md`

`personas/education/GEM_RESEARCHER.md` はこの一覧から除外する。これは3パターン完成までは現行Researcher本体のベースとして使用するが、Module未反映のため完成済み配布Personaとは扱わない。3パターン完成後に旧版へ切り替える。

## REFERENCES

- `project-notes/2026-08-21-ai-information-asset-safety.md`
- `project-notes/2026-08-21-reconstruction-confirmed-facts.md`
- `project-notes/2026-08-21-reconstruction-audit-researcher-reviewer.md`
- `project-notes/2026-08-21-education-4gem-design-decisions.md`（要再構築）
- `project-notes/2026-08-20-ai-education-staging.md`
- `project-notes/2026-08-19-4gem-names.md`（旧決定を含む）
- `personas/education/GEM_RESEARCHER.md`（3パターン完成まで現行Researcher本体ベース）
- `personas/education/GEM_CODE_GENERATOR.md`
