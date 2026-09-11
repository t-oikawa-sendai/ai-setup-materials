# README Decision & Rationale

対象成果物：`/README.md`

本ファイルは、ルート `README.md` に関する判断履歴の正本である。

ルート `README.md` は職業訓練校生徒向けの公開入口として可読性を優先し、判断履歴本文は本ファイルで管理する。

## Decision & Rationale（決定・判断理由）

### 2026-09-11

#### Personaあり／なしのA/B検証例をRoot READMEへ掲載

Decision:

ルート `README.md` の `Why Persona Matters（なぜPersonaが重要なのか）` に、同一モデル `Gemini 3.1 Pro`・同一実装プロンプトによる Code Generator Personaなし／ありの静的比較結果を掲載する。

比較はモデルランキングではなく、Personaが出力へ与えた影響を理解する教材として扱う。比較表の直下には、各評価項目を初学者が理解できるように1行で説明する `評価項目の見方` を置く。

比較結果は、Personaありで改善した項目だけでなく、明示制約遵守やLombok明示指定のように悪化した項目、および改善しなかった純JDBC制約・SQLのDAO集約も含める。

また、同一モデル・同一実装プロンプトによる2パターンの静的比較であり、Mavenによる実ビルドと実行時動作は未検証であること、モデル一般の性能を示すベンチマークではないことを明記する。

Reason:

Personaの有効性を説明するには、異なるモデル同士のランキングより、モデルを固定したA/B比較の方がモデル能力差とPersonaによる制御差を分離しやすいため。

また、Personaありを常に優位と見せるのではなく、改善・悪化・改善なしを同時に示すことで、PersonaがAIの能力そのものを増やすものではなく、判断基準や出力傾向へ影響することを教材として説明できるため。

評価項目の短い説明を併記することで、認可、XSS、HTTP更新系、純JDBC制約などの用語を知らない初学者でも比較表を読めるようにするため。

Rejected:

- GPT-5.6 Sol、Claude Opus 5 High、Gemini各パターンを同一順位表としてRoot READMEへ掲載する方式
- Personaありで改善した項目だけを抜き出す方式
- 5段階点数だけを掲載し、評価基準や検証条件を説明しない方式
- 実ビルド未実施の静的比較を一般的なモデル性能ベンチマークとして扱う方式

### 2026-09-11

#### Root READMEのDecision & Rationale分離

Decision:

ルート `README.md` に掲載していた `Decision & Rationale` を本ファイルへ分離する。

README本文には判断履歴本文を置かず、管理上の対応先だけをHTMLコメントで保持する。

本ファイルをルートREADMEの判断履歴の正本とする。

Reason:

ルートREADMEは生徒・利用者が最初に読む教材入口であり、内部の設計判断履歴が長く続くと利用導線の可読性を損なうため。

判断履歴自体は情報資産として必要なため削除せず、管理用 `project-notes/` へ分離する。

Rejected:

- READMEの `Decision & Rationale` を単純削除して履歴を失う方式
- すべての成果物MDの `Decision & Rationale` を一律に別管理へ移す方式
- `CURRENT.md` へREADME判断履歴を移す方式

### 2026-08-26

#### 比較表の正本一元化とSetupマニュアルの責務限定

Decision:

比較表はルート `README.md` の1か所だけに置く。Education READMEとGemini設定資料には比較表を重複掲載せず、ルート `README.md` への導線を置く。

Gemini設定資料は設定・操作手順に限定し、Personaの重要性やカスタム指示の効果・制約・利用条件などの説明は含めない。パーソナル インテリジェンスのカスタム指示は、パソコンで設定する操作手順だけをGemini設定資料に置く。

この決定により、2026-08-25の「Gemini固有の機能名称・制約・設定手順をGemini設定資料へ委譲する」という委譲範囲を更新する。

Reason:

Repository共通の概念説明とサービス固有の設定手順を分離し、比較表の重複と新旧不整合を防ぐため。

Rejected:

- 比較表をルート `README.md` とGemini設定資料へ重複掲載する方式
- Gemini設定資料へAIの概念・効果・制約を説明する章を置く方式

### 2026-08-25

#### Persona重要性のRepository共通化

Decision:

`Why Persona Matters（なぜPersonaが重要なのか）` はEducation固有の説明ではなく、Repository全体に共通する設計思想としてルート `README.md` に置く。

比較表はAIサービス共通の概念として、サービス全体のカスタム指示・共通設定、Persona、その都度のプロンプトの3つを比較する。

Gemini固有の機能名称・制約・設定手順は `personas/education/setup/GEMINI_GEM_SETUP.md` に委譲する。

Reason:

PersonaはEducation用Gemだけでなく `personas/reference/` のPersonaでも利用するため、Personaの必要性をEducation固有の前提として説明するとRepository全体の設計思想と一致しない。

入口で共通概念を理解してからEducation / Referenceへ進むことで、Personaの役割を利用サービスに依存せず理解できるため。

Rejected:

- `Why Persona Matters` をEducation READMEだけに置く方式
- ルートREADMEでGemini固有のパーソナル インテリジェンスの設定手順まで説明する方式

### 2026-08-23

#### Education用4Gem＋1のRepository入口表現

Decision:

Repository入口ではEducation用の基本体系を4Gemとして維持し、Gemini上ではResearcher Personaを使う `Researcher Deep Research` を追加した `4Gem＋1` として案内する。

設定詳細は `personas/education/setup/GEMINI_GEM_SETUP.md` へ導く。

Reference領域との対比でEducationの現行構成を指す場合も `4Gem＋1` と表記する。

Reason:

基本4役割を維持しつつ、Gemini上で作成するGem実体が5つであることを入口から誤解なく案内するため。

`Researcher Deep Research` を独立Personaとして扱わず、サービス固有設定の詳細を専用資料へ分離するため。

Rejected:

- Education体系を5つの独立Personaとして表現する方式
- ルートREADMEへGemini設定手順を重複記載する方式
