# CURRENT

Last Updated: 2026-08-22
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

### Repository作業開始時のGit同期ゲート

- Repositoryに関する作業では、ユーザーから個別の同期指示がなくても、Git同期確認を最初の必須工程として実行する。
- 実作業用ローカルRepository、branch、remote、ローカルHEAD、リモートHEAD、未commit変更の有無を確認する。
- ローカルがcleanで安全に追従可能な場合のみ、fast-forwardでremoteの最新状態へ同期する。
- 同期後にローカルHEADとリモートHEADの一致を確認してから `AGENTS.md` と本ファイルを読む。
- 未commit変更、branch分岐、競合、Repository不在、remote取得失敗、権限・network問題等がある場合は、本作業を開始せず、状態と停止理由を報告する。
- 未commit変更の破棄・退避・上書きによって同期を強行しない。
- 作業報告には、対象Repository、branch、作業開始時のローカルHEAD、確認したリモートHEAD、未commit変更の有無、同期結果または停止理由をEvidenceとして含める。
- この同期確認はユーザーからの個別指示を待たずに行うが、実際の同期は安全条件を満たす場合に限る。

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

- Researcher Persona再構築は完了。
- Reviewer Personaは未完成。
- 現行Researcher Personaは次の3ファイル。
  - `personas/education/GEM_RESEARCHER_FULL.md`
  - `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
  - `personas/education/GEM_RESEARCHER_DEVELOPMENT.md`
- 旧 `personas/education/GEM_RESEARCHER.md` は3パターン完成後に旧版化し、`personas/education/archive/GEM_RESEARCHER.md` へ退避済み。

### Reviewer再構築仕様

- Code Generatorはコード生成までを担当する。
- 生徒は、Code Generatorが生成したコードをVS Code等のIDEへコピーする。
- 生徒は、IDEへ反映したコードの実行、test、動作確認を行い、その検証Evidenceを作成する。
- Reviewerは、Code Generatorが生成したコードと、生徒が作成した検証Evidenceを評価する。
- Reviewerは、Solution Partnerの設計成果物を評価対象に含め、設計の論理的矛盾点などを検証する。
- Researcherの調査結果はReviewerの評価対象に含めない。
- 最終判断は生徒が行う。
- CursorはEducation用4Gemのこの運用には含めない。
- Cursorが実装・testを担当するAIサービス別の実務向け運用と、Education用4Gemを混同しない。
- `project-notes/2026-08-22-reviewer-reconstruction-instructions.md` は誤った運用混同を前提に作成されたため、実装へ使用しない。
- `GEM_REVIEWER.md` の再構築仕様と実装は未完成である。

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

教材として次の3完成版ファイルを提供する。

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
- 3ファイルは生成元テンプレートを別途設けず、直接管理する。
- Researcher本体を改訂する場合は3ファイルの共通部分を同時に更新し、本体が一致していることを確認する。

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

Researcher再構築は完了。現在はReviewer再構築を優先する。

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

- `AGENTS.md` と本ファイルに、Repository作業開始時のGit同期ゲート、停止条件、同期Evidence要件を追加済み。
- `project-notes/2026-08-21-ai-information-asset-safety.md` を追加済み。
- `AGENTS.md` にAI能力を過信しない安全前提と復旧ガードを追加済み。
- `project-notes/2026-08-21-education-4gem-design-decisions.md` は再構築完了まで正本扱い停止。
- README仮完成作業は復旧完了まで一時停止。
- `project-notes/2026-08-21-reconstruction-confirmed-facts.md` はResearcher再構築途中の確定事項記録として保持する。
- `project-notes/2026-08-21-researcher-completion.md` をResearcher完成後の最新状態・検証記録として追加済み。
- `project-notes/2026-08-21-reconstruction-audit-researcher-reviewer.md` に、GitHub現物・commit履歴から確認した履歴事実と現行位置づけを記録済み。

### Researcher再構築完了

- `GEM_RESEARCHER_FULL.md` を作成済み。
- `GEM_RESEARCHER_LEARNING_DEVELOPMENT.md` を作成済み。
- `GEM_RESEARCHER_DEVELOPMENT.md` を作成済み。
- 3ファイルのResearcher本体 `1. 役割`〜`9. Module運用ルール` が同一であることをGitHub上で確認済み。
- `Active Modules` は各ファイルの構成に応じて異なる。
- 同名Moduleの本文はファイル間で同一。
- 旧 `GEM_RESEARCHER.md` は `personas/education/archive/GEM_RESEARCHER.md` へ退避し、旧パスから削除済み。
- `personas/education/README.md` は旧Researcher 1ファイル構成と `Implementer` を参照しており、4Gem復旧後にまとめて整合させる必要がある。

### Reviewer監査で確認済み

- 2026-08-19版 `GEM_REVIEWER.md` はCode Generator追加前のPersona。
- 戻し先・リファクタリング担当として `Implementer` を含むため、その箇所は現行Education仕様としてそのまま利用しない。
- 2026-08-19のReviewer方針・役割意図・Persona追加と、2026-08-20のCode Generator追加をcommit単位で時系列確認済み。
- `GEM_REVIEWER.md` はCode Generator追加後に改訂されていない。
- 旧Reviewerの名称非依存部分を再利用候補、Implementer依存部分を現行利用不可、Code Generator化後の連携を未解決として分離済み。
- AIがEducation用4GemとCursor等の実務向け運用を混同し、Reviewerの確定記録と実装指示書へ誤った外部実装担当を混入させた。
- 2026-08-22、ユーザー確認により、Code Generatorがコード生成、生徒がIDEへの反映・実行・test・動作確認、Reviewerが生成コードと生徒の検証Evidenceを評価、最終判断は生徒、CursorはEducation用4Gemに含めないという前提へ是正した。
- 2026-08-22、ReviewerはResearcherの調査結果を評価対象に含めず、Solution Partnerの設計成果物を設計の論理的矛盾点などの検証対象に含めることをユーザー確認済み。
- `project-notes/2026-08-22-reviewer-reconstruction-instructions.md` は使用禁止状態へ変更する。

### Code Generator監査で確認済み

- `GEM_CODE_GENERATOR.md` は2026-08-20に追加された。
- コード生成・既存コード解析・エラー分析・修正版コード生成等を担当する。
- 実環境への適用、IDE操作、Git操作、品質保証判定は担当しない。

## NEXT ACTION

Reviewerの再構築を優先する。

1. Education用4Gemの確定前提を基準に、Reviewerの再構築に必要な既存資料を再確認する。
2. 推論と確認済み事実を分離し、資料だけで一意に決まらない事項だけをユーザーへ確認する。
3. 誤った `project-notes/2026-08-22-reviewer-reconstruction-instructions.md` を使用せず、確認済み事項だけで新しい実装指示書を作成する。
4. Reviewer再構築完了後、4Gem全体・README・Persona導線の整合を行う。

## DO NOT USE AS COMPLETED CURRENT SOURCE

再構築完了まで、次の文書を単独で現行の完成仕様として扱わない。

- `project-notes/2026-08-21-education-4gem-design-decisions.md`
- `project-notes/2026-08-19-4gem-names.md`
- `personas/education/GEM_REVIEWER.md`
- `project-notes/2026-08-22-reviewer-reconstruction-instructions.md`

`personas/education/archive/GEM_RESEARCHER.md` は旧版の履歴資料であり、現行Researcher Personaとして使用しない。

## REFERENCES

- `project-notes/2026-08-21-ai-information-asset-safety.md`
- `project-notes/2026-08-21-reconstruction-confirmed-facts.md`（Researcher再構築途中の確定事項）
- `project-notes/2026-08-21-researcher-completion.md`（Researcher完成状態）
- `project-notes/2026-08-21-reconstruction-audit-researcher-reviewer.md`
- `project-notes/2026-08-21-education-4gem-design-decisions.md`（要再構築）
- `project-notes/2026-08-20-ai-education-staging.md`
- `project-notes/2026-08-19-4gem-names.md`（旧決定を含む）
- `personas/education/GEM_RESEARCHER_FULL.md`
- `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
- `personas/education/GEM_RESEARCHER_DEVELOPMENT.md`
- `personas/education/archive/GEM_RESEARCHER.md`（旧版）
- `personas/education/GEM_CODE_GENERATOR.md`
