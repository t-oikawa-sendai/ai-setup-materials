# AGENTS 判断履歴アーカイブ

- 移動元：`AGENTS.md` の `Decision & Rationale`。
- D-080に基づき原文を移動。新しい判断は `DECISIONS.md` に記録する。
- 本文中の旧保存先・「本ファイル」等は記録当時の表現である。
- 未上書きの判断は有効。現行作業規則は [AGENTS.md](../AGENTS.md) を参照する。

## Decision & Rationale

### 2026-08-23

#### 文書管理ルール（正本・決定反映・CURRENT.mdの役割）

Decision:
決定事項は会話や別管理ログへ残さず、対象成果物MDへ即時反映する。成果物MD自身を最新仕様・最新構成・最新手順の正本とする。記録基準に該当する判断理由は、同じ成果物MDの `Decision & Rationale` に残す。`CURRENT.md` は現在地点（完了事項・作業中・次工程）のみを記載し、詳細設計や判断理由は記載しない。User決定の反映後にGitHubへ保存してから次工程へ進む。2026-08-23より前の `project-notes/YYYY-MM-DD-*.md` は削除せず履歴として保持するが、新規の設計決定の代替正本としては使用しない。

Reason:
最新状態の正本性を維持する。設計判断の過程を失わない。新チャット移行時でもGitHub上の成果物MDだけで過去判断を復元できるようにする。AIが記録要否を自己判断して決定事項を会話空間へ残すばらつきを防ぐ。

Rejected:
- 会話 → AI判断 → 必要と思われた事項のみ記録 → GitHub という流れ
- 決定事項を別管理ログへ集約し、正本更新を後回しにする方式
- AIの曖昧な「重要判断」による記録要否判断
- `CURRENT.md` に確定事項の全文を集約し、成果物MDと二重に正本化する方式

### 2026-09-01

#### User承認範囲の厳守と決定事項の即時記録

Decision:
Userが明示的に承認した変更だけを正本へ反映する。AIは、Userが明示的に決定した要求・設計・責務境界・運用方針を、既存の記録基準と正本管理ルールに従って対象成果物MDへ即時反映し、GitHubへ保存する。Userが承認していない内容、文書構造、章、運用方式をAI判断だけで正本へ追加しない。今回の `GEM_SOLUTION_PARTNER.md` では、Userが承認したPersona改善本文のみを保持し、AIが未承認で追加した `Decision & Rationale` は除去する。

Reason:
既存の `AGENTS.md` で、User決定後の即時反映、AI判断による未承認事項の確定禁止、対象外変更の禁止が既に定められていたにもかかわらず、AIがこれを遵守せず、`GEM_SOLUTION_PARTNER.md` へ未承認の `Decision & Rationale` を追加し、さらにUser決定事項の記録を `AGENTS.md` へ反映しなかった。既存ルールそのものを変更するのではなく、今回のUser決定と適用結果を正本へ記録し、承認範囲と記録責務を明確に残す。

Rejected:
- AIが必要と判断した内容をUser承認なしで正本へ追加する方式
- User決定事項を会話内だけに残し、正本への反映を後回しにする方式
- 未承認の文書構造変更を既存運用ルールの解釈だけで実施する方式

### 2026-09-01

#### Education Solution Partnerの設計回答精度を強化

**Decision:**

Education用Solution Partnerについて、職業訓練校のIT初学者が学習・演習・ポートフォリオ制作で利用する前提を維持しつつ、設計回答の精度を高める。

既存の「確定済み仕様を勝手に変更しない」「事実・未確認事項・仮定を区別する」「不要な機能や抽象化を追加しない」という原則は維持する。

その上で、次を追加する。

- Userが明示していない仕様を、一般論や実務慣行だけを理由に確定しない。
- 実装判断に必要な未確定事項は「要確認」または「仮定」として区別する。
- Userの目的、対象者、学習レベル、対象範囲に合わせ、学習に不要な実務レベルの厳格さや過剰設計を持ち込まない。
- User指定の出力形式、項目、順序を既定の出力形式より優先する。
- 回答前に、要求反映、仕様外追加、未確定事項、出力形式、回答内整合性を確認する。

**Reason:**

同一のWebアプリ仕様書生成プロンプトをPersonaあり／なしで比較した結果、Personaありでは仕様外追加の抑制や責務分離などに改善が見られた一方、未確定事項の補完、出力形式の完全遵守、回答内の整合性には改善余地が残った。

Education用Personaの目的は実務監査レベルの厳格さを導入することではなく、IT初学者が迷わず学習・設計・実装へ進める支援を行うことである。そのため、技術固有の詳細ルールや網羅的な監査項目を追加せず、設計回答に共通する最小限の確認ルールとして追加する。

**Rejected:**

- Spring FrameworkやDB設計など特定技術専用のチェック項目をPersonaへ固定する方式
- 実務監査レベルの網羅的な品質ゲートを導入する方式
- 現行Solution Partner Personaを全面的に再設計する方式
- 未確定事項を一般的なベストプラクティスで自動補完する方式

### 2026-09-01

#### 初学者向け成果物の導入説明と締めの説明を必須化

**Decision:**

Education用Solution Partnerが初学者向けの設計書・仕様書・説明資料を出力する場合、本文だけを提示せず、冒頭に資料の目的・何を示すかを簡潔に説明し、末尾にどこまで決まったか・未確定事項・次に行うことを簡潔に説明する。

これらは任意の親切説明ではなく、初学者が成果物の位置づけと次の行動を理解するための必須構成とする。

UserがMarkdown表など出力形式を指定している場合は、導入説明と締めの説明もその指定形式の中で表現し、形式遵守と教育上の説明を両立する。

**Reason:**

Version 1.1を適用したWebアプリ仕様書の再生成では、推測抑制や未確定事項の区別は改善した一方、冒頭の導入説明と末尾のまとめ・次工程案内が完全に欠落した。

職業訓練校のIT初学者向け教材では、設計情報そのものだけでなく、「何の資料か」「どこまで決まったか」「次に何をするか」を理解できることが学習上必要である。説明量を増やすことが目的ではなく、必要最小限の導入と締めを欠落させないことを目的とする。

**Rejected:**

- 導入説明・締めの説明を任意項目とする方式
- 初学者向けであっても設計情報だけを提示する方式
- 教育上の説明を理由に長い一般論や詳細解説を追加する方式
- User指定の出力形式を崩して導入説明・締めの説明を追加する方式

### 2026-09-01

#### 出力構造・未指定詳細・設計用語の安定性を強化

**Decision:**

Education用Solution Partnerの設計回答について、次を追加で必須化する。

- Userが指定した表・列・項目構造を途中で分割せず、必須内容を指定構造の外へ移動しない。
- Userが機能名や目的だけを示した場合、検索方式、画面遷移、権限、削除方式、データ項目、Framework機能などの未指定詳細を一般論から確定しない。
- 同じ作業内で既に確定した名称、クラス分割、責務、用語は、変更理由がない限り維持する。

**Reason:**

Version 1.2を適用したWebアプリ仕様書の再生成では、冒頭の導入説明と末尾のまとめ・次工程案内は改善した。一方で、Userが指定したプログラム一覧表がクラスごとに分割され、役割・担当処理・責務が表外へ出る問題が残った。

また、検索機能からLIKE検索を確定する、未指定の画面遷移やFramework機能を追加するなど、機能名から実装詳細を一般論で補完する傾向が残った。さらに、同じ用途のFormやViewの分割・名称が生成ごとに揺れる例も確認された。

これらは実務監査を強化する問題ではなく、初学者向け設計資料の分かりやすさ、再現性、プロンプト遵守に直接関係するため、技術固有ルールではなく汎用的な設計回答ルールとして追加する。

**Rejected:**

- Spring Framework専用のクラス構成・命名をPersonaへ固定する方式
- 特定の検索方式、削除方式、認証方式などを教材標準としてPersonaへ固定する方式
- 出力形式をAI側の読みやすさ判断で変更できるようにする方式
- 同じ作業内でもAIが毎回答で自由にクラス分割・命名を変更する方式

### 2026-09-11

#### Root READMEのDecision & Rationale分離

Decision:
ルート `README.md` は職業訓練校生徒向けの公開入口として可読性を優先し、READMEに関する `Decision & Rationale` は `project-notes/README_DECISIONS.md` へ分離する。README本文には判断履歴本文を置かず、管理上の対応先だけをHTMLコメントで保持する。`project-notes/README_DECISIONS.md` をルートREADMEの判断履歴の正本とする。

この決定はルート `README.md` に限る明示的例外であり、本ファイルにある「対象成果物MDと同じファイルに `Decision & Rationale` を保持する」「決定事項を別管理ログへ集約しない」という一般規定より優先する。他の成果物MDには適用しない。

Reason:
ルートREADMEは生徒・利用者が最初に読む教材入口であり、内部の設計判断履歴が長く続くと利用導線の可読性を損なう。一方、判断履歴自体は情報資産として保持する必要があるため、削除せず管理用 `project-notes/` へ分離する。

Rejected:
- READMEの `Decision & Rationale` を単純削除して履歴を失う方式
- すべての成果物MDの `Decision & Rationale` を一律に別管理へ移す方式
- `CURRENT.md` へREADME判断履歴を移す方式

### 2026-09-11

#### 生徒・利用者向け公開文書のDecision & Rationale分離

Decision:
Root READMEだけに限定していた `Decision & Rationale` 分離例外を、生徒・利用者が直接読むことを目的とする公開教材・公開参考資料へ拡張する。

公開・教材向け文書では、内部判断履歴が本文の可読性を損なう場合、対象成果物MDには利用者向け本文だけを保持し、判断履歴を `project-notes/` 配下の管理用Decisionファイルへ分離できる。対象成果物MDの本文・最新仕様はそのMD自身を正本とし、管理用Decisionファイルは判断履歴だけの正本とする。対象成果物MDには対応先をHTMLコメントで残す。

この分離はUser決定または既存の正本ルールで対象と明示された文書に限る。AIが独自判断で分離対象を増やしてはならない。Persona本体、`AGENTS.md`、内部管理文書は従来どおり同一ファイル内の `Decision & Rationale` を原則とする。

この決定は、2026-09-11の `Root READMEのDecision & Rationale分離` にある「ルートREADMEに限る」という適用範囲を更新し、§5.4の分離例外として一般化する。本ファイル内の同一ファイル保持規定と競合する場合は、この分離例外を優先する。

Reason:
生徒・利用者が直接読む教材・参考資料に内部の設計判断履歴を表示すると、教材本文の理解と利用導線を妨げる。一方で、判断履歴を削除すると情報資産と追跡可能性を失うため、公開本文と内部判断履歴を責務分離する。

Rejected:
- 公開教材・参考資料の `Decision & Rationale` を単純削除する方式
- すべての成果物MDから一律に `Decision & Rationale` を分離する方式
- AI判断だけで任意の文書を分離対象へ変更する方式
- 内部判断履歴を生徒向け本文へ表示し続ける方式

### 2026-09-13

#### Education Solution Partnerを Version 1.5へ正式改版

**Decision:**

Education用Solution Partnerを Version 1.5 / Status Approved へ正式改版する。既存Version 1.4への部分追記ではなく、Persona本文の整理と責務境界の明確化を含む改版とする。

- Solution Partnerは実装担当ではない。完成した実装コードの生成はCode Generatorの責務とする。
- 説明・比較・設計判断に必要な疑似コード、部分的なサンプルコード、SQL例、設定例、コマンド例、問題説明用の部分コード、差分例は禁止しない。
- コード可否の判断基準は分量ではなく、「そのまま提出・実行できる完成実装を生成しないこと」とする。
- 未決事項をAIが勝手に確定しない原則は維持する。
- UserがASKMEの決定を保留した場合は作業停止を続けず、暫定値を `仮定` と明示し、`補足A` に残し、後から変更可能であることを明示した上で次工程へ進む。
- `補足A` の管理対象に、従来の2分類に加えて `仮定を置いて進めた事項` を追加する。
- 冗長な重複規定（旧 `Design Response Check` を含む）を `Principles`、`ASKME`、`Output` 等へ統合し、Persona全体を簡潔化する。
- 学習用途・初学者向けという従来の背景意図は維持する。
- 現行どおり、Persona本文へ `Decision & Rationale` は追加しない。判断履歴は本ファイルへ記録する。

**Reason:**

完成実装の生成と設計説明用サンプルの混同を防ぐ。未決事項の勝手な確定は避けつつ、Userが決定を保留した場合に初学者が次工程へ進めなくなることを防ぐ。同じ確認規則の重複記載を解消し、適用漏れと解釈揺れを減らす。学習用途・初学者向けという従来の背景意図は維持し、実現方法だけを更新する。

**Rejected:**

- Version 1.4本文への部分追記で改版する方式
- Solution Partnerが完成実装コードを生成する方式
- サンプルコード等を行数や種類で全面禁止する方式
- UserがASKMEを保留した場合に作業停止を続ける方式
- 旧 `Design Response Check` を別章として残す方式
- Persona本文へ `Decision & Rationale` を追加する方式

### 2026-09-13

#### Education Code Generatorを Version 2.2へ更新し、Solution Partner v1.5の補足A 3区分へ整合

**Decision:**

Education用Code Generatorを Version 2.2 / Status Approved へ更新する。今回の目的はSolution Partner Version 1.5との引継ぎ整合に限定する。既存v2.1の未決事項制御思想は維持する。

- `補足A：未決事項一覧` の引継ぎインターフェースを、`次工程開始前に決定必須` / `実装段階まで持ち越し可能` / `仮定を置いて進めた事項` の3区分へ拡張する。
- `仮定` はUser確定仕様ではなく、Solution Partnerが明示した暫定実装条件として扱う。
- 明示された仮定があることだけを理由にコード生成を停止しない。
- Solution Partnerが具体的な暫定値・暫定方式を明示している場合は、その仮定に従って生成する。
- 仮定の内容が不明で実装条件を一意に決められない場合は、補完せずUserへ報告する。
- Code Generator自身による仮定作成は禁止する。
- 仮定を独自判断で変更・補完・確定しない。
- Mandatory Rulesと引き継いだ仮定が衝突する場合は、Mandatory Rulesを無視して実装せず、衝突内容をUserへ報告して停止する。
- 中核責務、Mandatory Rules 4-1〜4-5、Default Practices、実環境適用禁止、IDE / Git / test実行禁止、Evidence作成禁止、Reviewerとの責務境界、Solution Partner確定仕様を再設計しない原則は変更しない。
- 現行どおり、Persona本文へ `Decision & Rationale` は追加しない。判断履歴は本ファイルへ記録する。

**Reason:**

Solution Partner Version 1.5が `仮定を置いて進めた事項` を補足Aへ追加したため、Code Generatorが3区分を認識し、User確定仕様と暫定実装条件を混同せず受け取る必要がある。未決事項の勝手な補完禁止は維持しつつ、明示された仮定があることだけで初学者の実装工程を止めない。

**Rejected:**

- `仮定` があることだけを理由にコード生成を停止する方式
- `仮定` をUser確定仕様として扱う方式
- Code Generatorが新しい `仮定` を作成する方式
- Mandatory Rulesと衝突する仮定を、Mandatory Rulesを無視して実装する方式
- 未決事項制御思想を再設計する方式
- Persona本文へ `Decision & Rationale` を追加する方式

### 2026-09-29

#### 中核4種Reference Personaの本文編集元を一本化

Decision:
ChatGPT・Claude・Cursor・Geminiの本文の唯一の編集元（SSOT）を、本Repositoryの `personas/reference/CHATGPT_PERSONA.md`、`personas/reference/CLAUDE_PERSONA.md`、`personas/reference/CURSOR_PERSONA.md`、`personas/reference/GEMINI_PERSONA.md` とする。`solacom_main` の本文コピーは正本への参照へ置き換え、本文の独立編集元としない。個人パス等の実務固有の環境設定はPersona本文から分離し、利用環境側で保持する。

この決定の対象は中核4種の本文編集元であり、Education・Lovable・Copilotの正本配置変更や、AIサービス上の登録実体の移行完了を意味しない。

Reason:
同一Personaの独立編集による更新差分と更新漏れ、および本文コピー先の相対リンク切れを防ぐため。

Rejected:
- 実務版を `solacom_main`、教材版を `ai-setup-materials` に置き、それぞれを独立した本文編集元として維持する方式

### 2026-10-06

#### 決定の保留と仮定の実装利用許可を分離（Solution Partner 1.6（提案） / Code Generator 2.3（提案）、Draft）

**Decision:**

Education用Solution Partnerを Version 1.6（提案） / Status Draft、Code Generatorを Version 2.3（提案） / Status Draft とする。「判断を今は保留する」と「示された具体的な仮定を今回のコード生成・実装に使う」を別の選択として扱う。

- Solution Partner：未指定の仕様は未決事項として扱い、必要なUser判断をASKMEで確認する。質問せずに `仮定` へ置き換えない。未確認の外部事実は未決の仕様と区別する。
- Solution Partner：Userが決定を保留した後も、仮定を明示して次工程へ進む既存規則（2026-09-13）は維持する。ただし保留はコード生成・実装への使用許可ではない。実装に使う場合は、具体的な暫定値・方式と影響範囲を示してUserの選択を確認する。
- Solution Partner：既存設計やAI作成文書に書かれていること自体をUser承認の証拠にしない。根拠資料と、仕様を確定したUser判断を区別する。AI側で確認できる事実を不要なASKMEに回さない方針は維持する。
- Solution Partner：`補足A` の3区分・件数表示・4列表は維持する。`仮定を置いて進めた事項` の行には、`理由` 欄に具体的な仮定、影響範囲、`実装利用：可／不可`、可の場合のUserの明示選択を追える箇所を記載する。確認できない場合の既定は `実装利用：不可` とする。Code Generator以外の実装担当へ渡す場合も補足Aを省略しない。
- Code Generator：補足Aで当該仮定について `実装利用：可` とUserの明示選択を確認できる場合だけ、その仮定に依存するコードを生成する。記載なし、`不可`、または選択の根拠を確認できない場合は依存部分を生成せず、対象IDと必要なUser判断を報告する。無関係な生成・解析は止めない。
- Code Generator：§5の出力前確認と停止時の報告へ同じ条件を反映し、不一致がある場合は影響する生成対象だけを保留する形へ整合する。
- Code Generator：補足Aの3区分、Code Generator自身による仮定作成禁止、Mandatory Rulesとの衝突時の停止、使用した仮定の出力明示、UserによるIDE反映・実行・検証の責務は変更しない。
- 現行どおり、Persona本文へ `Decision & Rationale` は追加しない。Reference Cursor Persona Version 1.1（提案）の判断履歴は同ファイル内に記録する。
- Approvedへの昇格と実動検証は行っていない。

この決定は、2026-09-13の「Userが決定を保留した場合は暫定値を仮定と明示して次工程へ進む」（Solution Partner 1.5）と「Solution Partnerが具体的な暫定値・暫定方式を明示している場合はその仮定に従って生成する」（Code Generator 2.2）を、実装利用の許可条件について絞り込む。保留時に初学者の進行を止めないという2026-09-13の背景意図は変更しない。

**Reason:**

初学者の進行を保ちつつ、保留と実装許可を分けるため。Userが決定を保留したことを、AIが選んだ具体的な仮定でコードを生成・実装してよいという許可に変換しないようにする。一方で、初学者が設計の検討を続けられること、独立した作業は進められること、Userが最終判断することは維持する。

**Rejected:**

- 仮定が明示されていること、文書に記載されていること、Userが保留したことだけを実装許可として扱う方式
- 保留時に設計検討そのものを停止する方式
- 未確認の仮定が1件でもあれば、独立した生成・作業まで停止する方式
- Persona本文へ `Decision & Rationale` を追加する方式

### 2026-10-07

#### 対象Repository省略の是正対象を記録（本文是正は未着手）

**Decision:**

Userの「OK これを修正対象として記録」に基づき、次の修正対象と予定範囲を記録する。今回の承認は修正対象の確定と記録に対するものであり、修正本文の承認、PersonaのApprovedへの昇格、実動検証の完了を意味しない。今回は本記録と `project-notes/CURRENT.md` の現在地点だけを更新する。

対象Repository：`t-oikawa-sendai/ai-setup-materials`（`https://github.com/t-oikawa-sendai/ai-setup-materials`）。確認したGitHub mainのHEAD：`a4ab5040ef06c249ca21fc4cc7bd534eabb4b529`。

修正対象Persona：

| 対象ファイル | 修正予定範囲 |
|---|---|
| `personas/reference/CHATGPT_PERSONA.md` | 実装・追加・修正指示で、対象Repositoryを毎回明記し、省略を禁止する規定 |
| `personas/education/GEM_SOLUTION_PARTNER.md` | 実装担当への引き渡しで、対象Repositoryを毎回明記し、省略を禁止する規定 |
| `personas/reference/CURSOR_PERSONA.md` | 指示された対象と実作業先の照合、および未記載・特定不能・不一致の場合の変更開始禁止 |
| `personas/education/GEM_CODE_GENERATOR.md` | Repositoryを対象とする生成・修正依頼での対象情報確認と、不足時の扱い |
| `personas/reference/CLAUDE_PERSONA.md` | 通常レビューから作る実装修正指示でも、対象Repositoryを明記する規定 |
| `personas/education/GEM_REVIEWER.md` | Userがコピーして渡す修正指示で、対象Repositoryを明記する規定 |
| `personas/reference/GEMINI_PERSONA.md` | Cursorへ実動確認事項を渡す場合に限り、対象Repositoryを明記する規定 |

その他の修正対象文書：

| 対象ファイル | 修正予定範囲・適用条件 |
|---|---|
| `AGENTS.md` | 指示された対象と実作業先の照合を、作業開始条件として明確化 |
| `personas/reference/PERSONA_PROMPT_TEMPLATE.md` | Repository作業用の対象欄を追加し、簡易版でも省略不可とする規定 |
| `personas/reference/CHAT_HANDOFF_TEMPLATE.md` | Repository作業では、既存の対象欄を省略不可とする規定 |
| `personas/reference/setup/CLAUDE_CODE_SETUP.md` | 条件付き対象。Claude Code運用にも適用する場合、呼び出し・引き渡し例へ対象指定を追加し、Persona保管先と今回の作業対象を区別 |

予定範囲の共通条件：

- 指示に明記する情報は、Repository名（`owner/name`）、URL、作業branch、作業先の絶対パスとする。今回の `ai-setup-materials` だけを恒久的な作業対象としてPersonaへ固定しない。
- 教育用Code Generatorへの規定は、Repositoryを対象とする生成・修正依頼に適用する。一般的な学習用サンプルの生成に、存在しないRepositoryを要求しない。Code GeneratorへGit操作・実環境照合の責務を追加しない。
- `GEM_RESEARCHER_*`、各README、`PERSONA_OPERATION_CASE_STUDY.md` は、本件による直接の本文修正対象としない。
- 各本文を改訂する際は、既定の判断履歴と `project-notes/CURRENT.md` も更新する。既存のDecisionを欠落させない。
- 添付の利用中 `ChatGPT-Persona.txt` は、正本改訂後に登録内容を更新する対象として扱う。独立した本文編集元を増やさない。今回、添付ファイル・外部AIへの登録内容は変更しない。

**Reason:**

Userから、設計者が実装者への指示で対象Repositoryを省略することに起因するインシデントが頻発しているとの申告があった。GitHub mainと添付Personaを照合した結果、設計側の「対象」欄だけではRepository名・URLの毎回明記を要求しておらず、Cursor側も指示の対象未記載時の扱いを明確にしていなかった。修正指示を作るReviewerと実動確認事項を渡すReference Geminiにも、同じ省略を防ぐ規定の整合が必要と判断した。Userが対象一覧を了承したため、会話だけに残さず、是正未着手の状態と適用条件を記録する。

**Rejected:**

- 修正対象を会話だけに残す方式
- 対象一覧の記録指示を、全Persona本文の変更・承認・外部登録変更の指示として扱う方式
- 条件付きのClaude Code設定資料を、無条件の修正対象へ変更する方式
- 教育用Code GeneratorにGit操作を追加し、一般的な学習用サンプルにもRepository指定を機械的に要求する方式

### 2026-10-12

#### Repository作業におけるAGENTS.mdの確認と読込状態の一行報告

**Decision:**

Repositoryを対象に作業する際は、対象Repositoryの `AGENTS.md` を確認する。存在する場合は本文を確認する。通常の作業報告に `AGENTS.md：ReadOK / ReadNG / ReadUndefine` のうち該当する状態を一行で記す。

- `ReadOK`：対象Repositoryの `AGENTS.md` 本文を確認した。
- `ReadNG`：本文を確認できなかった。存在の有無を推測で確定しない。
- `ReadUndefine`：対象Repositoryに `AGENTS.md` が存在しないことを確認した。

読込状態だけの別報告や追加ターンは設けない。理由や影響は作業判断に必要な場合だけ補足する。この表示だけで作業の完成とは判定しない。既存Personaの責務・動作・報告構成は維持する。

**Reason:**

UserはAIが `AGENTS.md` を読めたかを直接確認できない。一方、読了確認より設計・実装・レビューの品質を優先し、報告の増加や細かなターンによる作業停滞を避けるため。

**Rejected:**

- 毎回、適用規則の該当箇所や読了証跡を詳細に列挙する方式
- `AGENTS.md` の読込状態だけを作業の完成判定とする方式
