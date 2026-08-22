# Reconstruction Confirmed Facts

Last Updated: 2026-08-21
Status: RECOVERY / USER-CONFIRMED

## Purpose

AIによる誤統合で毀損したEducation用4Gemの情報資産を再構築するため、ユーザーが明示的に再確認した最新事項を小刻みに記録する。

この文書には、ユーザーが明示した事項と、ユーザーが指定した資料から直接確認できる事項を記載する。AIによる推論・補完は加えない。

---

## 2026-08-21 Confirmed Facts

### Researcher Persona

- Researcher Personaは未完成。
- Researcher本体の責務自体はModule導入によって変更しない。
- Moduleで変更するのはResearcherの検索範囲・検索対象である。
- 検索対象は大きく次の3分野に分ける。
  1. 学習関連
  2. 就職活動関連
  3. PFなどの設計・開発関連
- これら3分野は訓練期間中には有効だが、将来すべてが常に必要とは限らない。
- 学習終了後は「学習関連」が不要になる。
- 就職決定後は「就職活動関連」が不要になる。
- 不要になったModuleをResearcherから外せる構成にする。
- この「Researcher本体の責務は維持したまま、検索範囲・対象をModuleで変更し、不要になったModuleを外せること」が、Researcher Personaの他Personaと異なる特徴である。

### Researcher Module 構成方針

- Moduleを複数のKnowledgeファイルとして同時登録する方式は採用しない。
- Researcherは、その時点で必要な本体・Moduleを含む完成済みファイルを1本だけGemへ登録して利用する。
- 複数のResearcher候補ファイルは入替候補であり、Gemへ同時登録するものではない。
- したがって、Gemの実運用上Researcher本体が重複して読み込まれることはない。
- 判断基準は着脱の簡単さより、Gemが必要な指示を確実に参照できることを優先する。
- Moduleを外した場合、その分野を「検索禁止」とするのではなく、Researcherの担当検索範囲から外す。
- Researcher本体には調査方法・品質基準を置き、Moduleには「何について調査するか」という検索対象・範囲を置く。
- Researcher本体に置く内容の例：Evidence、一次情報優先、事実と推論の分離、比較、根拠付き推論、結論提示、未確認事項の明示。
- Moduleごとに調査方法・品質基準を変える設計にはしない。
- Moduleの着脱・構成変更時もResearcher本体の責務・調査方法・品質基準は変更しない。

### Module 正式名称

1. `Learning Module` — 学習関連
2. `Career Module` — 就職活動関連
3. `Development Module` — PFなどの設計・開発関連

### 教材として提供する範囲

- このRepositoryが提供するのは完全な運用サービスではなく学習教材である。
- 教材側で、利用者が将来取り得るすべての状態・組み合わせを網羅する必要はない。
- 「学習は終了したが、まだ就職していない」状態は、教材としてあらかじめ提供するパターンには含めない。
- その状態に対応する `Career Module + Development Module` の組み合わせが必要になった場合は、利用者が学習した内容をもとに自己判断で作成させる。

### Researcher 3完成版ファイル方式

教材として次の3つの完成済みResearcherファイルを提供する方式を正式採用する。

1. `GEM_RESEARCHER_FULL.md`
   - Researcher本体 + `Learning Module` + `Career Module` + `Development Module`
2. `GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
   - Researcher本体 + `Learning Module` + `Development Module`
3. `GEM_RESEARCHER_DEVELOPMENT.md`
   - Researcher本体 + `Development Module`

- 各ファイルは、それ単体でResearcher Personaとして成立する完全な独立ファイルとする。
- Gemには常に上記のうち必要な1ファイルだけを登録する。
- ユーザーはPersona本文やModule本文を削除・編集して切り替えるのではなく、必要な完成済みファイルへ入れ替えて利用する。
- 3パターンは教材として用意する代表的な構成である。
- どのタイミングでどのファイルへ切り替えるかはユーザーの任意とし、教材側で強制的な切替条件にはしない。
- 代表例としては、訓練中・就職活動中は `FULL`、就職活動支援が不要になった後は `LEARNING_DEVELOPMENT`、学習支援も不要になった後は `DEVELOPMENT` を利用できる。

### `GEM_RESEARCHER.md` の切替条件

- `personas/education/GEM_RESEARCHER.md` は、3パターンのResearcher Personaが完成するまでは現行Researcher本体のベースとして扱う。
- 3パターンすべてが完成した時点で、`GEM_RESEARCHER.md` を旧版として扱う。
- 3パターン完成前に `GEM_RESEARCHER.md` を旧版・廃止版として扱わない。
- 旧版化後の物理的な保管場所・削除有無は、この決定とは別に扱う。

### Researcher Persona本文のModule配置・記法

- Researcher本体を先に記載し、Module群はResearcher本体の後ろに配置する。
- 各完成版ファイルの冒頭に `Active Modules` を明示し、そのファイルで有効なModuleを列挙する。
- 現在有効でないModuleに属する質問を受けた場合の案内ルールは、各Module内ではなくResearcher本体側の共通ルールとして明記する。
- 3完成版ファイル間でResearcher本体の内容は完全に同一とする。ファイル間で変わるのは有効なModule構成だけとする。
- Moduleの正式名称は英語名を維持し、Persona本文の見出しでは日本語を併記する。
  - `Learning Module（学習）`
  - `Career Module（就職活動）`
  - `Development Module（設計・開発）`

### Module検索範囲の確定事項

#### Learning Module

基準資料：`2606e宮城_日別計画表.pdf`

ユーザー確認事項：

- このPDFは6e宮城のスケジュールである。
- 全コースで異なるのは日付であり、訓練内容・日程構成は同じである。
- したがってLearning Moduleの検索範囲を決める際は、PDF内の日付ではなく科目・訓練内容を全コース共通の基準として扱う。

PDFから確認できる学習科目・訓練内容：

1. 安全衛生・IT基礎
2. Webデザイン演習
3. Javaプログラミング基礎①〜④
4. Javaプログラミング実践①〜④
5. Pythonプログラミング基礎①〜④
6. Pythonプログラミング実践①〜④
7. データベース基礎①〜②
8. ソフトウェア開発演習①〜④

Learning Moduleは、上記の科目・訓練内容に関する学習上の調査を基本検索範囲とする。

次の項目はPDFには含まれるが、Learning Moduleの学習科目としては扱わない。

- 開講式・オリエンテーション
- 対面指導そのもの
- 就職支援
- ハローワーク来所
- キャリアコンサルティング
- 修了式

就職支援・ハローワーク・キャリアコンサルティング等はCareer Module側の対象として扱う。

習熟度確認テスト・成績考査・修了考査は評価・進行上の項目であり、Learning Moduleの検索対象となる独立技術分野としては扱わない。

追加確定事項：

- PDFに科目名として明記されていない場合でも、現在の学習内容を理解・問題解決するために直接必要な周辺知識・前提知識はLearning Moduleの検索対象に含める。
- 検索範囲は無制限にIT全般へ広げず、カリキュラムを起点として、現在の学習・疑問解決に直接必要な範囲までとする。
- 生成AI・AI活用はLearning Moduleの検索対象に明示的に含める。
- カリキュラム外の技術であっても、現在の学習との関連を説明でき、学習目的で調査する場合はLearning Moduleの対象に含める。
- ただし、ポートフォリオ制作や具体的なシステム設計・技術選定として扱う場合はDevelopment Moduleの領域とする。

#### Career Module

- 基本対象はIT分野への就職活動とする。
- ただし、Career Moduleの対象職種・業界は固定しない。
- ユーザーのプロンプトによって対象を変更できるものとする。
- 例：事務職、営業職、製造業など。

#### Development Module

- 学習成果物、ポートフォリオ、小規模開発を中心とする。
- 技術・フレームワーク、API・ライブラリ・OSS、公式仕様、技術比較、ホスティング・DB、セキュリティ上の事実、実装判断のための技術情報、既存コードやOSS理解のための関連資料等を調査対象とする方向で確定する。

#### Module横断

- 質問が複数の有効Moduleにまたがる場合、最も近い1Moduleに限定せず、有効なModuleを横断して調査する。
- 横断した結果は、1つの調査結果として統合して提示する。

#### 有効Module外の質問

- 現在有効でないModuleに属する質問を受けた場合、その質問を通常どおり調査しない。
- 現在のResearcher Personaが担当している検索範囲・責務を明確にユーザーへ伝える。
- そのうえで、必要に応じて別の完成済みResearcher Personaファイルへ入れ替えるよう案内する。
- 「検索禁止」とだけ返すのではなく、なぜ現在のPersonaの担当外なのか、どのPersonaへ切り替えるべきかが利用者に分かる形にする。

### Reviewer Persona

- Reviewer Personaは未完成。

#### 2026-08-22 confirmed reconstruction requirements

- Reviewerは、次をレビュー対象とする。
  - Researcherの調査結果
  - Solution Partnerの設計成果物
  - Code Generatorのコード生成結果
  - HumanまたはCursor等の外部実装担当が作成した実環境の検証Evidence
- 問題の種類に応じて、戻し先を次のように分離する。
  - 事実・情報源・Evidenceの問題：Researcher
  - 要求・要件・設計の問題：Solution Partner
  - コード生成・コード解析の問題：Code Generator
  - 実環境への適用、build、test、IDE、実機確認の問題：HumanまたはCursor等の外部実装担当
- Code Generatorは、実環境への適用、build、test、IDE操作、Git操作を担当しない。
- 実行・build・test・IDE・実機確認等のEvidenceは、HumanまたはCursor等の外部実装担当が作成し、Reviewerへ渡す。
- Reviewerは判定、問題、根拠、影響、修正要求、戻し先を提示する。
- Reviewerは最終判断を行わない。最終判断はHumanが行う。
- Reviewerは自ら調査、設計変更、コード修正、実環境への適用を代行せず、必要な担当へ戻す。

---

## Not Yet Confirmed

次の事項は、ユーザーからまだ具体的に確定されていないため、この文書では推論しない。

- 3つの配布候補ファイルを改訂するときの保守方法
- 旧版化後の `personas/education/GEM_RESEARCHER.md` の物理的な保管場所・削除有無

Reviewer Personaの未完成部分は、2026-08-22のユーザー確認により上記の範囲で確定した。

これらは既存資料の再監査で確認し、資料だけで一意に決まらない場合のみユーザーへ確認する。
