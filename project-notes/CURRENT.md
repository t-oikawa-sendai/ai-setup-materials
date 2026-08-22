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

- `User` は、4Gemを操作し、Code Generatorの生成コードをIDEへ反映・検証し、最終判断を行う利用者を指す。
- READMEでは役割名を `User（生徒）` と表記し、README以外のPersona本文・管理文書・出力フォーマットでは `User` と表記する。
- Code Generatorはコード生成までを担当する。
- Userは、Code Generatorが生成したコードをVS Code等のIDEへコピーする。
- Userは、IDEへ反映したコードの実行、test、動作確認を行い、その検証Evidenceを作成する。
- Reviewerは、Code Generatorが生成したコードと、Userが作成した検証Evidenceを評価する。
- Reviewerは、Solution Partnerの設計成果物を評価対象に含め、設計の論理的矛盾点などを検証する。
- Researcherの調査結果はReviewerの評価対象に含めない。
- Reviewerは、問題の原因、根拠、影響を確認して戻し先を判断する。
- Reviewerは、判断した戻し先とその理由をレビュー結果へ明記する。
- 複数工程に問題がある場合は、問題を分離してそれぞれの戻し先を示す。
- Evidence不足で戻し先を判断できない場合は推測せず、判断不能であることを明示し、最終判断をUserへ残す。
- Reviewerは自ら修正せず、戻し先の判断と修正要求までを担当する。
- Reviewerのレビュー結果は、別のGemへ直接送るのではなく、まずUserへ返す。
- 従来の「戻し先」は、Userを経由せず別のGemへ直接作業を送ることを意味しない。問題が存在する工程、対応が必要な工程、利用可能な支援先を示すものとして扱う。
- コードレベルの問題を確認した場合も、修正実施者をCode Generatorへ固定しない。
- Userはレビュー内容を読み、自分で修正できると判断した場合は手作業でコードを修正できる。User自身による修正は学習面で望ましい場合がある。
- Userが自分で修正することが難しいと判断した場合は、レビュー内容をCode Generatorへ渡し、コード生成・修正支援を依頼できる。
- Userが自力修正とCode Generator利用のどちらを選んだ場合も、UserがIDEへの反映、実行、test、動作確認、検証Evidence作成、Reviewerへの再提出を行う。
- ReviewerのレビューはCode Generatorだけを読者として書かず、学習途中のUserが問題、影響、修正条件、次の作業を理解できる表現にする。
- Reviewerは完成実装を代行しない。ただし、Userが問題と修正方法を理解・比較できるよう、複数の修正案、各案の利点・欠点・影響・適用条件、疑似コード、必要最小限の説明用コード例を提示できる。
- Reviewerが提示する説明用コード例は、完成コード、適用済みコード、動作保証済みコードとして扱わない。
- ファイル全体の完成版コード、そのまま適用することを前提とした大規模な修正コード、複数ファイルにまたがる完成パッチはReviewerの担当にしない。
- 完成した修正版コードが必要な場合は、Userが自ら作成するか、UserがCode Generatorを利用する。
- 現行設計の範囲内で選べるコードレベルの案はReviewerが比較できる。採用案によって要求、設計、責務が変わる場合は、Reviewerが決定せずSolution Partnerでの再検討を示す。
- 実装に修正が必要な指摘では、`対応が必要な工程：実装`、`利用可能な支援先：Code Generator`、`Userの対応：自力でコード修正、もしくはCode Generatorに修正指示` を表示する。
- `対応が必要な工程：実装` は、コードの内容・構造・処理に修正が必要であることを示す。Code GeneratorがIDEへの反映や実環境での実装を行うという意味ではない。
- 実装に関するすべての修正必須指摘には、レビューが長くなっても、User向け説明とCode Generatorへコピーできる修正指示の両方を含める。簡潔さより学習目的を優先する。
- User向け説明には、何が問題か、なぜ修正が必要か、自力修正する場合の着眼点、修正後に確認することを含める。
- Code Generatorへの修正指示には、対象、問題、Evidence、修正後に満たす条件、変更してはいけない範囲を含める。
- User向け説明とCode Generatorへの修正指示は選択式にせず、同じレビュー文書内に両方を用意する。
- 設計指摘では、`対応が必要な工程：設計`、`利用可能な支援先：Solution Partner` と表示する。
- 設計指摘の `Userの対応` では、まずReviewerの評価を確認するよう案内する。Userが理解できない、追加説明が必要、または方針を判断できないと明示した場合は、打ち合わせ用情報をSolution Partnerへ渡して検討し、検討結果を基にUserが最終方針を決定する。
- ReviewerはUserの理解状態を推測しない。`Userが理解できていない点` をReviewerが特定・記載しない。
- Solution Partnerとの打ち合わせ用情報には、Reviewerが確認した問題、問題である理由、Evidence、このままの場合の影響、現在確定している要求・制約、検討事項、方針決定後に更新するもの、Reviewerへ再提出するものを含める。
- `Userが追加する検討事項（任意）` を設けられる。この欄はUserが必要に応じて記入する。
- 完成した成果物と一致する最終設計ドキュメントを必要な成果物とする。
- 最終設計ドキュメントは現在有効な最終設計を示す。単なる変更履歴やAI向け引き継ぎメモとして扱わない。
- UserはAIを利用せず、自分で最終設計ドキュメントを更新・完成できる。AI利用を成果物の完成条件にしない。
- Solution PartnerとReviewerは、Userが利用を選択した場合に、設計と実装の差分確認、実装中に発生した判断の整理、文書更新、整合確認を支援する。
- 最終設計ドキュメントと成果物の確認、採用、完成判断はUserが行う。
- ReviewerのUser-first学習設計に至った経緯、採用理由、責務境界は `project-notes/2026-08-22-reviewer-user-first-learning-design.md` を正本とする。
- Reviewer出力の冒頭一覧の正式名称は `対応方針一覧` とする。旧名称の `戻し先一覧` は使用しない。
- `対応方針一覧` では、各指摘IDに、対応が必要な工程、利用可能な支援先、Userの対応を対応付ける。
- 各指摘は個別の指摘IDを持ち、次を明記する。
  - 対象
  - 問題
  - Evidence
  - 影響
  - 対応が必要な工程
  - 対応が必要な工程の理由
  - 利用可能な支援先
  - Userの対応
  - 修正要求
  - 再確認条件
- 出力の最後に、Userが判断する事項を明記する。
- Reviewerの総合判定は次の4段階とする。
  - `PASS`：修正が必要な問題を確認していない。
  - `PASS WITH NOTES`：合格だが、Userが認識すべき注意事項がある。
  - `REWORK REQUIRED`：修正後の再レビューが必要である。
  - `BLOCKED`：Evidence不足、仕様矛盾等により判定できない。
- 4判定の正式な意味と使用条件は `GEM_REVIEWER.md` に記載し、判定定義の正本とする。
- `personas/education/README.md` には、Reviewerが4段階で判定することと、最終判断はUserが行うことだけを簡潔に記載する。
- root `README.md` には4判定の詳細を記載しない。
- `GEM_REVIEWER.md` とREADMEへの反映は、それぞれの再構築・整合工程で行う。
- Reviewerは、詳細レビューを始める前に、レビューに必要な対象・資料・検証Evidenceがそろっているか受付確認を行う。
- 必要なものが不足しレビューを行えない場合は、総合判定を `BLOCKED`、状態を「レビュー不能」と明記する。
- 「Evidence不足」のような抽象的な指摘だけで終わらせず、初心者であるUserが次に行う作業をそのまま実行できる形で案内する。
- レビュー不能時の案内には、次を含める。
  - レビューを行えない理由
  - 不足しているもの
  - Userが行う作業
  - 準備するもの
  - 具体的なEvidence例
  - 提出方法
  - 再レビューを開始できる条件
- 初心者向けの案内では、Evidenceを必要に応じて「確認に必要な記録・資料」と説明する。
- Evidence例は全案件共通の固定リストとして機械的に要求せず、その案件で不足しているものに対応する具体例だけを示す。
- 最終判断はUserが行う。
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
- 2026-08-22、ユーザー確認により、Code Generatorがコード生成、UserがIDEへの反映・実行・test・動作確認、Reviewerが生成コードとUserの検証Evidenceを評価、最終判断はUser、CursorはEducation用4Gemに含めないという前提へ是正した。
- 2026-08-22、ReviewerはResearcherの調査結果を評価対象に含めず、Solution Partnerの設計成果物を設計の論理的矛盾点などの検証対象に含めることをユーザー確認済み。
- 2026-08-22、Reviewerが問題の原因・根拠・影響に基づいて戻し先を判断し、戻し先と理由を明記することをユーザー確認済み。
- 2026-08-22、Education用4Gemを操作し、生成コードのIDE反映・検証・最終判断を行う利用者の名称を `User` とすることをユーザー確認済み。
- 2026-08-22、READMEでは `User（生徒）`、README以外では `User` と表記することをユーザー確認済み。READMEへの反映は4Gem復旧後の整合工程で行う。
- 2026-08-22、Reviewer出力を、冒頭の戻し先一覧、指摘ごとの対象・問題・Evidence・影響・戻し先・戻し先の理由・修正要求・再確認条件、最後のUser判断事項で構成することを当初ユーザー確認した。その後のUser-first学習設計により、`戻し先` と `戻し先の理由` は、`対応が必要な工程`、`対応が必要な工程の理由`、`利用可能な支援先`、`Userの対応` へ置き換えた。旧項目名を現行出力へ使用しない。
- 2026-08-22、Reviewerの総合判定を `PASS / PASS WITH NOTES / REWORK REQUIRED / BLOCKED` の4段階とし、その意味と配置方針をユーザー確認済み。
- 2026-08-22、Reviewerは詳細レビュー前に受付確認を行い、レビュー不能時は初心者のUserが次の作業・準備物・具体的なEvidence例・提出方法・再レビュー条件を理解できる案内を提示することをユーザー確認済み。
- 2026-08-22、コードレベルの指摘も最初にUserへ返し、Userが自力修正またはCode Generator利用を選択するUser-firstフローをユーザー確認済み。
- 2026-08-22、User自身によるコード修正を許可し、学習面で望ましい場合があることをユーザー確認済み。
- 2026-08-22、Reviewerは完成実装を代行しない一方、学習・比較のための複数案、疑似コード、必要最小限の説明用コード例を提示できることをユーザー確認済み。
- 2026-08-22、実装指摘の表示項目を `対応が必要な工程：実装`、`利用可能な支援先：Code Generator`、`Userの対応：自力でコード修正、もしくはCode Generatorに修正指示` とすることをユーザー確認済み。
- 2026-08-22、学習目的を優先し、実装に関するすべての修正必須指摘へ、User向け説明とCode Generatorへコピーできる修正指示の両方を含めることをユーザー確認済み。レビューが長くなることは許容する。
- 2026-08-22、Reviewer出力の冒頭一覧の正式名称を `対応方針一覧` とし、旧名称の `戻し先一覧` を使用しないことをユーザー確認済み。
- 2026-08-22、設計指摘の理解支援ルートは、Userが理解不能、追加説明の必要、または方針判断不能を明示した場合に開始し、ReviewerがUserの理解状態を推測しないことをユーザー確認済み。
- 2026-08-22、Solution Partnerとの打ち合わせ用情報では `Userが理解できていない点` をReviewerが記載せず、`確認事項` ではなく `検討事項` を使用することをユーザー確認済み。
- 2026-08-22、完成成果物と一致する最終設計ドキュメントを必要な成果物とする一方、AI利用を完成条件にせず、User自身による更新・完成を認めることをユーザー確認済み。
- `project-notes/2026-08-22-reviewer-user-first-learning-design.md` に、上記設計へ至った誤解、訂正、検討、採用理由、将来のPersona設計教材としての目的を記録済み。
- `project-notes/2026-08-22-reviewer-reconstruction-instructions.md` は使用禁止状態へ変更する。

### Code Generator監査で確認済み

- `GEM_CODE_GENERATOR.md` は2026-08-20に追加された。
- コード生成・既存コード解析・エラー分析・修正版コード生成等を担当する。
- 実環境への適用、IDE操作、Git操作、品質保証判定は担当しない。

## NEXT ACTION

Reviewerの再構築を優先する。

1. Education用4Gemの確定前提を基準に、Reviewerの再構築に必要な既存資料を再確認する。
2. 推論と確認済み事実を分離し、資料だけで一意に決まらない事項だけをユーザーへ確認する。
3. 誤った `project-notes/2026-08-22-reviewer-reconstruction-instructions.md` を使用せず、`project-notes/2026-08-22-reviewer-user-first-learning-design.md` を含む確認済み事項だけで新しい実装指示書を作成する。
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
- `project-notes/2026-08-22-reviewer-user-first-learning-design.md`（ReviewerのUser-first学習設計と決定経緯）
- `project-notes/2026-08-21-education-4gem-design-decisions.md`（要再構築）
- `project-notes/2026-08-20-ai-education-staging.md`
- `project-notes/2026-08-19-4gem-names.md`（旧決定を含む）
- `personas/education/GEM_RESEARCHER_FULL.md`
- `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
- `personas/education/GEM_RESEARCHER_DEVELOPMENT.md`
- `personas/education/archive/GEM_RESEARCHER.md`（旧版）
- `personas/education/GEM_CODE_GENERATOR.md`
