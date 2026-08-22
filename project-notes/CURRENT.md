# CURRENT

Last Updated: 2026-08-22
Status: CURRENT / DOCUMENT CONFORMANCE RECOVERY

## PURPOSE

生徒へ配布可能な `ai-setup-materials` を完成させる。

単なるAI利用方法ではなく、AIの役割分担・責務分離・Evidence・検証を重視したAI活用設計を学べる教材とする。

## RECOVERY HISTORY

2026-08-21、AIによる決定事項統合で、Education用4Gemの旧名称 `Implementer` を現行情報として再混入させる誤りが確認された。

そのため、復旧中は次の統合記録を現行設計の正本として扱わなかった。

- `project-notes/2026-08-21-education-4gem-design-decisions.md`

原因説明だけで復旧扱いにせず、一次資料・既存決定記録・Persona現物・ユーザーの明示決定を再照合して、Researcher、Reviewer、4Gem間の責務境界、README導線を再構築した。

2026-08-22、Education用4Gem Personaの機能設計と、名称・責務境界・当時確認したREADME導線の整合化を一度完了と記録した。その後の現物監査により、文書標準・表記・文書間導線への適合性評価は未完了であり、復旧が必要であることを確認した。過去の完了宣言はPersonaの機能設計と当時確認した範囲の完了記録として扱い、文書適合性を含む全体完了のEvidenceとして扱わない。上記の統合記録には旧決定・失効情報が含まれるため、単独で現行完成仕様として使用しない。

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
- 旧 `Implementer` の責務を機械的にすべて `Code Generator` へ置換してはならない。役割変更後の責務境界、User-firstフロー、Persona・README導線は再構築・整合済みであり、今後も単純置換へ戻さない。

### Persona完成状態

- Researcher Persona再構築は完了。
- Reviewer Persona再構築は完了。
- Solution PartnerとCode Generatorの現行責務境界への整合は完了。
- Education用4Gem Persona本体の機能設計と現行責務境界の実装は完了。
- 文書標準・表記・文書間導線への適合性評価と復旧は未完了。
- 現行Researcher Personaは次の3ファイル。
  - `personas/education/GEM_RESEARCHER_FULL.md`
  - `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
  - `personas/education/GEM_RESEARCHER_DEVELOPMENT.md`
- 旧 `personas/education/GEM_RESEARCHER.md` は3パターン完成後に旧版化し、`personas/education/archive/GEM_RESEARCHER.md` へ退避済み。
- 旧 `personas/education/GEM_IMPLEMENTER.md` は `personas/education/archive/GEM_IMPLEMENTER.md` へ退避し、`SUPERSEDED` と置換先を明記済み。
- 旧 `personas/education/GEMINI_PERSONA_DEFINITION-4Gem.md` は `personas/education/archive/GEMINI_PERSONA_DEFINITION-4Gem.md` へ退避し、`SUPERSEDED` と置換先を明記済み。
- Reviewerの機能設計は完成済みであり、機能設計の再検討対象ではない。ただし、文書標準・表記・導線への適合性は、他の現行文書と同じく再評価対象に含める。

### 設計文書標準の適用境界

- `/Users/takashioikawa/Dev/solacom_main/docs/standards/DESIGN_DOCUMENT_STANDARD.md` は、ユーザーが作成する全プロジェクトの設計文書統治における憲法として扱う。
- 同標準はアプリプロジェクトを主な適用対象としているため、教材・Persona・標準資料Repositoryである `ai-setup-materials` へ、アプリ用の文書構成やテンプレートを100%機械的に適用しない。
- `ai-setup-materials` では、SSOT、文書責務分離、命名・表記の一貫性、ヘッダー・状態・版管理の追跡可能性、文書間導線、履歴管理、AIによる無秩序な文書追加・変更・統合・削除の禁止、確認不能時の停止、重複・更新不整合防止を必須の統治原則として適用する。
- READMEと6文書の固定作成、アプリ固有の文書名、UI・データ・API・アーキテクチャ・スクリーンショット等の該当しない必須構成は、`ai-setup-materials` へ機械的に適用しない。
- アプリ固有の構成を適用対象外とすることは、統治原則まで免除することを意味しない。
- `ai-setup-materials` 向けの具体的な文書体系、配置、既存文書の修正方法は未決であり、推測しない。
- 固定7文書を `ai-setup-materials` 内へ機械的に作成することは確定事項ではない。
- `English（日本語）` 等の表記統一は、意味・責務・契約・入出力仕様を変えない範囲に限って適用する。
- 表記変更が確定済みの仕様変更になる箇所は修正せず、例外として現行の正式名称・表記を維持する。User確認済みの正式出力名、役割名、判定名、状態名、項目名、列名、固定文言等は例外候補だが、機械的にすべてを例外とせず、正本で確定したものに限る。
- 表記上の例外は、現在の確定仕様を表記修正だけで壊さないための一時的な互換性保留であり、永久固定ではない。将来、仕様変更として別途検討し、Userが承認した段階で `English（日本語）` 表記への統合対象になり得る。
- 例外は「統一漏れ」と混同せず、例外箇所、根拠、維持理由、再検討条件または解除条件を追跡可能にする。例外を理由に未期限・無条件で不統一を固定化せず、例外解除をAIが自動決定しない。表記統一を理由にPersonaの機能仕様を再設計しない。
- root `README.md`、`personas/education/README.md`、現行Education Persona、新設する `personas/reference/README.md`、`personas/reference/` の現行Personaを現行配布文書とし、統一した標準ヘッダーの適用対象とする。
- 現行配布文書の標準ヘッダーは、`Document ID（文書ID）`、`Version（バージョン）`、`Status（ステータス）`、`Created Date（作成日）`、`Last Updated（最終更新日）`、`Owner（管理者）`、`Related Documents（関連文書）` の7項目で統一する。ヘッダー表の列名は `Item（項目）` と `Value（値）` で統一する。
- 標準ヘッダーについて、項目名、列名、Status体系、Document ID体系、適合確認中と初回承認時のVersion・Status運用、Related Documentsの階層規則を確定した。作成日、最終更新日、管理者の具体値は未決であり、推測しない。
- 既にDocument IDを持つroot `README.md` と `personas/reference/` の現行Personaは、追跡性を維持するため既存IDを変更しない。
- 未採番のEducation文書には、`personas/education/README.md`：`STD-PERSONA-EDU-INDEX-001`、`GEM_RESEARCHER_FULL.md`：`STD-PERSONA-EDU-RESEARCHER-FULL-001`、`GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`：`STD-PERSONA-EDU-RESEARCHER-LEARNING-DEVELOPMENT-001`、`GEM_RESEARCHER_DEVELOPMENT.md`：`STD-PERSONA-EDU-RESEARCHER-DEVELOPMENT-001`、`GEM_SOLUTION_PARTNER.md`：`STD-PERSONA-EDU-SOLUTION-PARTNER-001`、`GEM_CODE_GENERATOR.md`：`STD-PERSONA-EDU-CODE-GENERATOR-001`、`GEM_REVIEWER.md`：`STD-PERSONA-EDU-REVIEWER-001` を付与する。
- 新設する `personas/reference/README.md` には `STD-PERSONA-REFERENCE-INDEX-001` を付与する。
- Document IDは固定識別子として扱い、配置変更、版更新、Status変更だけを理由に変更しない。
- `personas/reference/README.md` をReference領域の正式な入口・索引として配置し、Reference Personaの目的、Education用4Gemとの違い、Educationの現行手順として流用しない注意、現在利用可能なReference文書への索引、root `README.md` へ戻る導線、必要最小限のEducation READMEへの案内を記載する。
- Reference索引を現在の4文書専用として固定しない。将来7文書に追加資料を加えた構成へ増える可能性を受け入れ、承認された文書の追加時に索引を更新できる構成とする。ただし、将来数を推測して未確定文書を先に作成しない。
- root `README.md` はEducation領域とReference領域の入口を示し、Reference Personaは同一ディレクトリの `README.md` へ戻る導線を持つ。
- Persona文書の保存構造は、Repository全体の入口をroot `README.md`、区分別の入口を `personas/<区分>/README.md`、現行Personaを `personas/<区分>/`、旧版を `personas/<区分>/archive/`、内部の判断・作業記録を `project-notes/` とする共通規則で統一する。
- 現在のPersona区分は `education` と `reference` である。Referenceには旧版が存在しないため、空の `personas/reference/archive/` は作成せず、最初のReference旧版が発生した時点で作成する。
- 新設する `personas/reference/README.md` を除き、保存構造の統一だけを理由とする現行ファイルの移動は行わない。
- 7文書を本Repositoryへ配置するか別管理にするか、および現在の別Repositoryとの不整合解消は、Persona作成完了後に扱う最重要検討事項として分離し、Persona保存構造の決定だけで解決済みとしない。
- `Related Documents（関連文書）` は、root READMEから区分別README、区分別READMEから現行Personaへ進む階層規則で統一する。root READMEはEducation READMEとReference README、Education READMEはroot READMEと現行Education Persona、各Education PersonaはEducation README、Reference READMEはroot README・Education README・現行Reference文書、各Reference PersonaはReference READMEを関連文書とする。
- Persona同士をヘッダーから総当たりで相互リンクしない。区分内の文書追加・置換は区分別READMEの索引で管理し、個別Personaのヘッダー更新を必要最小限にする。
- Related Documents導線の背景意図は、root READMEから区分を選び、区分別READMEで適用境界と利用可能文書を確認してから個別Personaへ進める導線を維持しつつ、将来の文書増加に伴うリンク更新不整合を防ぐことである。
- 標準ヘッダーの `Status（ステータス）` は、`Draft`、`Review`、`Approved`、`Deprecated` の4状態で統一する。
- 文書適合性の確認中は、新設するReference READMEを含む全13件の現行配布文書を `Version（バージョン）: 0.1`、`Status（ステータス）: Review` とする。
- ヘッダー、表記、文書間導線、ディレクトリ構造の確認と必要な修正が完了しても、AIの判断だけで初回承認版へ変更しない。AIはUserへ `Version 1.0（Status: Approved）へ変更してよいか` と明示的に確認し、Userが承認した場合に限り `Version（バージョン）: 1.0`、`Status（ステータス）: Approved` へ変更する。
- `personas/education/GEM_REVIEWER.md` に記載する最終設計ドキュメントの `DRAFT`、`CURRENT`、`SUPERSEDED` は、標準ヘッダーの状態とは責務が異なるUser確認済みの機能仕様である。表記統一だけを理由に変更せず、一時例外として維持する。
- 上記例外は永久固定ではない。最終設計ドキュメントの状態仕様を変更対象として別途検討し、Userが仕様変更を明示承認した場合に限り表記統合を再検討する。解除条件を満たす前にAIが自動変更しない。
- `project-notes/` は作業状態・判断経緯・実装指示・監査Evidence等の内部記録であり、配布文書用の完全ヘッダーを機械適用せず、既存の簡易ヘッダーを維持する。
- `archive/` は履歴本文を保存する領域であり、旧本文・旧ヘッダーを書き換えず、冒頭のArchive Noticeだけを統一する。Archive Noticeでは、履歴資料であること、現行利用禁止、状態、置換先、旧本文を保存していることを追跡可能にする。
- 全Archive文書のArchive Noticeは、`# Archive Notice（アーカイブ通知）`、見出し直下の利用禁止警告、`Item（項目）` / `Value（値）` の管理表、区切り線、変更しない旧本文・旧ヘッダーの順で統一する。
- 見出し直下に `Do Not Use（利用禁止）` と「この文書は履歴資料です。現行仕様、現行Persona、現行運用の根拠として使用しないでください。」を独立表示する。
- Archive Noticeの管理表は、`Archive Type（アーカイブ種別）: Historical Material（履歴資料）`、`Status（ステータス）: Deprecated`、`Usage（利用可否）: Do Not Use（利用禁止）`、`Replaced By（置換先）`、`Preservation（保存方針）: Original Body Preserved（旧本文を変更せず保存）` の5項目とする。
- 利用禁止は見出し直下の警告と管理表の `Usage（利用可否）` の二重で表示し、Statusだけに利用禁止の意味を依存させない。
- 既存Noticeの `SUPERSEDED` はNotice内で `Deprecated` へ統一し、置換関係は `Replaced By（置換先）` で維持する。Noticeがない `personas/education/archive/GEM_RESEARCHER.md` にも同形式を旧本文の前へ追加する。
- Archive Noticeの置換・追加後も、区切り線より下の旧本文・旧ヘッダーは変更しない。
- この区分はヘッダー適用範囲の確定であり、作成日、最終更新日、管理者の具体値は未決である。
- ヘッダー適用範囲の背景意図は、配布文書の一貫性と追跡可能性を確保しつつ、内部記録への過剰適用とArchive本文の改変を防ぐことである。
- 背景意図は、標準の目的を維持しつつ、性質の異なるRepositoryへアプリ用テンプレートを機械適用して不要な文書を増やすことを防ぐことである。
- 表記統一に関する背景意図は、文書の一貫性を高めつつ、外見上の統一のために確定済み仕様を壊すことを防ぐことである。
- 詳細は `project-notes/2026-08-22-design-document-standard-application-scope.md` を正本とする。

### Reviewer再構築仕様

- 旧Reviewerのうち、役割名・戻し先・実施担当に依存しない中核部分は現行Reviewerでも維持する。
- Reviewerは、設計ドキュメント、実装内容、test・検証結果を独立した立場から評価する。
- 基本評価観点は、要求・要件・設計との整合性、指示範囲外の変更、正常系・異常系、test・検証Evidenceの十分性、品質・保守性・セキュリティ、秘密情報・個人情報の不適切な露出とする。
- Evidenceのない指摘を確定事項として扱わない。
- 好みや「より綺麗になる」「将来役立つかもしれない」だけを理由に変更を要求しない。
- 問題がない範囲へ不要な改善提案を広げない。
- 全案件で全観点を機械的に列挙せず、対象に関係する観点だけを評価する。
- 旧Reviewerの `Implementer` への戻し方、リファクタリング実施担当を `Implementer` とする記述、旧出力形式は維持せず、後続のUser-first仕様へ置き換える。
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
- 検証Evidence不足の指摘では、`対応が必要な工程：検証` とし、利用可能な支援先を一つへ固定せず、不足原因に応じて記載する。
- 実行結果・画面表示・実機確認が不足する場合、利用可能な支援先は `なし` とし、Userが実環境で確認してEvidenceを作成する。
- testコード自体が不足する場合、利用可能な支援先は `Code Generator` とする。Code Generatorはtestコード生成までを支援し、実行、結果確認、Evidence作成はUserが行う。
- 検証基準となる要求・仕様が不明確な場合、検証問題のまま扱わず `対応が必要な工程：設計` とし、利用可能な支援先は `Solution Partner` とする。
- Evidenceの取得方法をUserが理解できず追加説明を求めた場合、Reviewerは初心者向けの具体的な取得手順を説明する。ReviewerはEvidenceを代わりに作成しない。
- AIが実行していないtest結果、推測した実行結果・成功画面をEvidenceとして生成しない。Code Generatorが生成したtestコードを実行済み・成功済みとして扱わない。
- Evidence不足の原因が要求・仕様の不明確さにある場合、設計工程へ戻さずUserへ検証だけを繰り返させない。
- Reviewerは修正後のサンプルコードを自動的に提示しない。Userから明示的な依頼があった場合に限り、理解のための必要最小限のサンプルコードを提示できる。
- 既存コードの問題箇所をEvidenceとして引用することは、サンプルコードの依頼を必要としない。完成した修正版コードはUserから依頼された場合もReviewerの担当外とする。
- サンプルコードを提示可能な指摘がある場合、Reviewerはレビューの最後に `必要であればサンプルコードの出力が可能です。必要ですか？` と表示する。Userが必要と回答するまでサンプルコードを出力しない。
- 数行程度の説明用コード断片はサンプルコードと区別する。問題箇所、構文、条件式、修正方針の一部分を説明するために必要で、単独で完成した処理として成立しない断片は、説明文の一部としてUserの依頼なしで提示できる。
- 説明用コード断片かサンプルコードかは行数だけで判断せず、問題説明の一部か、修正結果を完成させる実装例かで判断する。完成コードを複数の説明用断片に分割して提示しない。
- 問題説明に必要な短い疑似コードはUserの依頼なしで提示できる。修正後の処理全体を示す疑似コードはUserの明示依頼を必要とする。
- 同じ指摘に採用可能な修正案が2つ以上ある場合だけ、詳細説明より先に `修正案一覧表` を表示する。有効な修正案が一つの場合は表示しない。
- 複数の指摘があっても各指摘に一案しかない場合は `修正案一覧表` を表示しない。一部の指摘だけに複数案がある場合は、その指摘の案だけを掲載する。
- 二案以上にするために、仕様違反、危険、成立しない案を追加しない。
- `修正案一覧表` の列は、指摘ID、案ID、修正方針、変更範囲、主な利点、主な欠点、適する条件とする。
- Reviewerの出力順は、総合判定、`対応方針一覧`、`修正案一覧表`（同じ指摘に採用可能な修正案が2つ以上ある場合のみ）、各指摘・各案の詳細、Userが判断する事項、サンプルコード提示の案内（提示可能な場合のみ）とする。
- 完成した成果物と一致する最終設計ドキュメントを必要な成果物とする。
- 最終設計ドキュメントは現在有効な最終設計を示す。単なる変更履歴やAI向け引き継ぎメモとして扱わない。
- UserはAIを利用せず、自分で最終設計ドキュメントを更新・完成できる。AI利用を成果物の完成条件にしない。
- Solution PartnerとReviewerは、Userが利用を選択した場合に、設計と実装の差分確認、実装中に発生した判断の整理、文書更新、整合確認を支援する。
- 最終設計ドキュメントと成果物の確認、採用、完成判断はUserが行う。
- Reviewerを利用する場合、Reviewerは設計、実装、Evidenceを確認して `PASS` を判定した後、`最終設計ドキュメント更新情報` を出力する。
- `最終設計ドキュメント更新情報` には、完成した機能・動作、実装で変更された内容、現在の設計文書との差分、最終設計へ反映する事項、採用した方針、維持すべき要求・制約、test・動作確認Evidence、既知の制約・未対応事項を含める。
- Userは自分で最終設計ドキュメントを更新するか、Solution Partnerを利用して更新する。更新後のReviewer再確認はUserが選択できる任意の支援とし、完成の必須条件にしない。
- Reviewerの `PASS` は確認した設計・実装・Evidenceに対するレビュー判定である。最終設計ドキュメントと成果物の一致確認、採用、完成版としての最終判断はUserが行う。
- Education教材の最終設計ドキュメントでは、`DRAFT（作成・更新途中・現行設計の正本として使用しない）`、`CURRENT（現在有効な最終設計・User確認済み）`、`SUPERSEDED（後続文書に置換済み・現行設計として使用しない）` の表記を使用する。
- `SUPERSEDED` の場合は置換先も記載する。
- 日本語説明の併記は初心者向けEducation教材の標準とする。利用者が自分のPersona・成果物で英語のみの表記へ変更することは利用者の自由意思とし、日本語併記を利用者独自の成果物へ強制しない。
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
- `GEM_REVIEWER.md` の再構築仕様、Persona本文への反映、静的検証は完了している。

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
- `背景意図` は、要求・ルール・設計判断・文書構成・用語について、なぜ必要か、何を防ぎ、どの価値・制約・責務境界を守るかを示す重要情報資産として扱う。
- 重要事項を記録・変更・統合・簡略化・置換するときは、表面上の文言だけでなく、ユーザー明示またはEvidenceで確認済みの背景意図も保存・確認する。
- 背景意図をAIが推測して補完せず、一意に確認できない場合はユーザーへ確認する。
- 背景意図を理由に、明示されていない要求・必須工程・成果物を追加しない。
- 重要決定はこまめにGitHubへ記録する。
- 名称変更・役割変更・採用・廃止・置換では、時系列と上書き関係を確認する。
- `CURRENT / SUPERSEDED / UNRESOLVED` を分離する。
- AI側で確認可能な事項をユーザーへの個別質問へ転嫁しない。
- 資料だけで一意に決まらない事項のみユーザーへ確認する。
- 「統合済み」「確定」「正本」とする前に、最新性・競合・欠落を検証する。
- 誤統合が発覚した場合、原因分析だけではなく再構築と検証を行う。

詳細：

- `project-notes/2026-08-21-ai-information-asset-safety.md`

設計ドキュメント管理に関する確認済みの背景意図：

- 標準のREADMEと最大6種の設計ドキュメントは、全案件で7文書を作成させるための必須数ではない。
- 本来の目的は、原則として合計7文書以内という上限と配置先を定め、AIが文書を際限なく追加することを防ぐことである。
- 適用対象だけを作成する。例えばCLI成果物ではUI設計文書は不要であり、必要な文書が7文書以内であれば問題としない。
- Repository間で文書の置き場所を統一することで、Humanが情報の所在や修正箇所に迷わない状態を作ることが主な価値である。
- `DESIGN_DOCUMENT_STANDARD.md` の統治目的は全プロジェクトに適用するが、アプリ用テンプレートを `ai-setup-materials` へ100%機械適用しない。
- 最大7文書は上限と統制の考え方であり、`ai-setup-materials` に固定7文書を必ず作成することは確定事項ではない。
- アプリ固有の構成を適用しない場合も、SSOT、責務分離、表記、追跡可能性、導線、履歴、変更統制、重複・更新不整合防止は免除しない。
- `ai-setup-materials` 向けの具体的な文書体系、状態名、配置、既存文書修正は未決であり、推測しない。
- この考え方をAIが機械的に誤解しないための別運用文書は将来整備する予定だが、現時点では作成しない。

## CURRENT TARGET

Education用4Gem Persona本体の機能設計は完了している。

現在の最優先対象は、今回確定した設計文書標準の適用境界に基づき、既存文書・Persona・READMEの文書標準、表記、文書間導線への適合性を再評価し、必要な復旧を行うことである。機能設計と文書適合性を混同せず、Reviewerを含むPersonaの機能設計をEvidenceなしに再検討しない。

この再評価と復旧を、`ASKME 迎合禁止` の利用に関する検討より先に行う。具体的な文書体系、状態名、配置、既存文書の修正内容は現物監査で確認し、未決事項を推測しない。

## PERSONA FUNCTIONAL RECOVERY METHOD（完了）

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
- `背景意図` を重要情報資産として定義し、恒久ルール、情報資産保全方針、本ファイルへ記録済み。
- 設計ドキュメント標準の「最大7文書」は作成数の強制ではなく、AIによる文書増殖の防止とHumanが情報の所在・修正箇所を把握しやすくするための上限・配置ルールであることを記録済み。別運用文書の作成は未着手。
- `project-notes/2026-08-21-education-4gem-design-decisions.md` は旧決定・失効情報を含む履歴資料として保持し、単独で現行完成仕様として使用しない。
- README仮完成作業の一時停止後、Education READMEとroot READMEについて、現行名称・責務境界・当時確認した配布リンクへの更新を実施済み。ただし、文書標準・表記・文書間導線への適合性評価と復旧は未完了。
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
- `personas/education/README.md` が旧Researcher 1ファイル構成と `Implementer` を参照していたことは監査時点の過去事実である。現在はResearcher 3完成版と現行4Gemの導線へ整合済み。

### Reviewer監査で確認済み（過去事実と復旧記録）

次のうち旧Reviewerの状態を示す記述は監査時点の過去事実であり、現在の `GEM_REVIEWER.md` の状態を示すものではない。Reviewer Personaの再構築、独立レビュー、静的検証は完了しており、Reviewerは再検討対象ではない。

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
- 2026-08-22、検証Evidence不足では利用可能な支援先を固定せず、不足原因に応じて `なし`、`Code Generator`、`Solution Partner` を使い分けることをユーザー確認済み。
- 2026-08-22、AIが未実行のtest結果・実行結果・成功画面をEvidenceとして生成せず、仕様不明確が原因の場合は検証を繰り返さず設計工程へ戻すことをユーザー確認済み。
- 2026-08-22、修正後のサンプルコードはUserの明示依頼がある場合だけ提示し、提示可能な場合はレビューの最後に必要か確認することをユーザー確認済み。
- 2026-08-22、修正案は詳細説明より先に `修正案一覧表` で表示し、指摘ID、案ID、修正方針、変更範囲、主な利点、主な欠点、適する条件を横並びで比較可能にすることをユーザー確認済み。
- 2026-08-22、数行程度の説明用コード断片はサンプルコードと区別し、問題説明の一部としてUserの依頼なしで提示可能とすることをユーザー確認済み。
- 2026-08-22、Reviewerは `PASS` 後に `最終設計ドキュメント更新情報` を出し、Userが自力更新またはSolution Partner利用を選択すること、更新後のReviewer再確認は任意とすることをユーザー確認済み。
- 2026-08-22、同じ指摘に採用可能な修正案が2つ以上ある場合だけ `修正案一覧表` を表示し、一案のみの場合は表示しないことをユーザー確認済み。
- 2026-08-22、最終設計ドキュメントの状態名へ初心者向け日本語説明を併記し、利用者が将来自分のPersona・成果物で英語のみに変更することは自由とすることをユーザー確認済み。
- `project-notes/2026-08-22-reviewer-user-first-learning-design.md` に、上記設計へ至った誤解、訂正、検討、採用理由、将来のPersona設計教材としての目的を記録済み。
- `project-notes/2026-08-22-reviewer-reconstruction-instructions.md` は使用禁止状態へ変更する。
- `project-notes/2026-08-22-reviewer-reconstruction-approved-implementation-instructions.md` を、確認済み事項だけを使用する新しいReviewer実装指示書として作成済み。
- `personas/education/GEM_REVIEWER.md` を現行仕様に基づいて再構築済み。
- `project-notes/2026-08-22-reviewer-completion.md` にReviewer完成状態と検証Evidenceを記録済み。
- Reviewer実装後の独立レビューでコード例境界の不足を修正し、禁止語、必須構造、9つの想定ケース、`git diff --check` を再確認済み。

### Code Generator監査で確認済み

- `GEM_CODE_GENERATOR.md` は2026-08-20に追加された。
- コード生成・既存コード解析・エラー分析・修正版コード生成等を担当する。
- 実環境への適用、IDE操作、Git操作、品質保証判定は担当しない。
- 2026-08-22、testコード生成支援、Reviewer修正指示の受入れ、Userへの返却、実行・test・Evidence作成を担当しない境界をPersona本文へ整合済み。

### Education 4Gem Persona・README整合化の過去完了宣言と現在評価

次の事項は、名称・責務境界・配布リンク・Researcher不変条件について当時実施した整合化と検証のEvidenceである。文書標準・表記・文書間導線を含む全体適合性の完了を示すものではない。

- `personas/education/GEM_SOLUTION_PARTNER.md` を、User、Code Generator、Reviewer、最終設計ドキュメントの現行責務境界へ整合済み。
- `personas/education/GEM_CODE_GENERATOR.md` を、コード・testコード生成支援とUserによる適用・検証の境界へ整合済み。
- Researcher 3完成版の役割主体表記を `User` へ統一済み。
- Researcher 3完成版の本体一致、同名Module一致、Active Modulesを再検証済み。
- `personas/education/README.md` をEducation用の主要導線として再構築済み。
- root `README.md` をRepository全体の入口として整合し、Education用の主要導線を `personas/education/README.md` として明記済み。
- 現行READMEから、旧 `GEM_IMPLEMENTER.md`、旧一体型定義書、旧 `GEM_RESEARCHER.md` への導線を除外済み。
- 現行READMEとArchive冒頭に追加したリンクのリンク先が実在することを確認済み。
- 旧 `GEM_IMPLEMENTER.md` と旧 `GEMINI_PERSONA_DEFINITION-4Gem.md` はArchiveへ移動し、`SUPERSEDED`、現行利用禁止、置換先を明記済み。旧本文は保持している。
- 当時の対象差分について `git diff --check` は成功した。
- 詳細Evidenceは `project-notes/2026-08-22-education-4gem-readme-alignment-completion.md` に過去の完了宣言として記録した。同記録の「未解決なし」は当時の整合化対象内に限るものであり、現在の文書適合性全体について未解決事項がないことを示さない。
- 現在は、今回確定した適用境界に基づく文書標準・表記・文書間導線の再評価と復旧が必要である。

## CURRENT PRIORITIES / UNRESOLVED

Persona本体の機能設計は完了している。現在は次の順で扱う。

1. 設計文書標準・表記・文書間導線の再評価と復旧
   - 今回確定した適用境界に基づき、SSOT、文書責務、命名・表記、ヘッダー・状態・版管理、導線、履歴、変更統制、重複・更新不整合を現物で確認する。
   - 現行配布文書、`project-notes/`、`archive/` の区分を前提にヘッダーを監査し、配布文書への標準ヘッダー、内部記録の簡易ヘッダー、Archive Noticeの各適用範囲を混同しない。
   - 表記修正によって意味・責務・契約・入出力仕様が変わる場合は、統一対象ではなく確定仕様上の一時例外として扱い、例外箇所、正本の根拠、維持理由、再検討条件または解除条件を確認する。
   - 機能設計の完成と文書適合性の完了を分離し、適合、不適合、未決を区別する。
   - 具体的な修正は現物監査結果と確定事項に基づき、推測しない。
2. `ASKME 迎合禁止` の利用に関する検討
   - 適用目的、適用範囲、運用方法、既存ルールとの関係は未確定。
3. 7文書の配置・管理方法に関する検討
   - 7文書を本Repository内のどこかへ配置するか、別管理とするかは未確定。
   - 現在は別Repositoryに存在するが、整合性が取れていない。
   - 現在の別Repositoryをそのまま採用すること、または本Repositoryへ移すことを確定事項として扱わない。
   - 固定7文書を `ai-setup-materials` 内へ機械的に作成することも確定事項として扱わない。

## NEXT ACTION

Reviewerを含むEducation用4Gem Persona本体の機能設計は完了している。Reviewerの機能設計は再検討対象に戻さない。

次は、今回確定した適用境界に基づき、既存文書・Persona・READMEの文書標準・表記・文書間導線への適合性を現物で再評価し、必要な復旧範囲を確定する。現行配布文書、`project-notes/`、`archive/` の区分を前提にヘッダーを監査し、具体的な各ヘッダー値、状態名、Document ID体系は未決事項として分離する。表記不統一と、正本で確定した仕様上の一時例外も分離して監査し、例外箇所、根拠、維持理由、再検討条件または解除条件を追跡可能にする。例外解除はAIが自動決定せず、別途の仕様検討とUser承認を必要とする。これはPersonaの機能設計再構築とは分離して行う。

その完了後、次の順で検討する。

1. `ASKME 迎合禁止` の利用に関する検討
2. 7文書を本Repository内へ配置するか別管理にするか、および現行の別Repositoryとの不整合に関する検討

7文書の配置・別管理は未決のまま保持する。固定7文書を `ai-setup-materials` へ機械的に作成することは確定事項ではない。いずれも結論を推測しない。

## DO NOT USE AS COMPLETED CURRENT SOURCE

次の文書には旧決定・失効情報が含まれるため、単独で現行の完成仕様として扱わない。

- `project-notes/2026-08-21-education-4gem-design-decisions.md`
- `project-notes/2026-08-19-4gem-names.md`
- `project-notes/2026-08-22-reviewer-reconstruction-instructions.md`

`personas/education/archive/GEM_RESEARCHER.md`、`personas/education/archive/GEM_IMPLEMENTER.md`、`personas/education/archive/GEMINI_PERSONA_DEFINITION-4Gem.md` は `SUPERSEDED` の履歴資料であり、現行Education Personaまたは現行運用導線として使用しない。

## REFERENCES

- `project-notes/2026-08-21-ai-information-asset-safety.md`
- `project-notes/2026-08-21-reconstruction-confirmed-facts.md`（Researcher再構築途中の確定事項）
- `project-notes/2026-08-21-researcher-completion.md`（Researcher完成状態）
- `project-notes/2026-08-21-reconstruction-audit-researcher-reviewer.md`
- `project-notes/2026-08-22-reviewer-user-first-learning-design.md`（ReviewerのUser-first学習設計と決定経緯）
- `project-notes/2026-08-22-reviewer-reconstruction-approved-implementation-instructions.md`（Reviewer再構築の現行実装指示書）
- `project-notes/2026-08-22-reviewer-completion.md`（Reviewer完成状態と検証Evidence）
- `project-notes/2026-08-22-education-4gem-readme-alignment-instructions.md`（4Gem・README整合実装指示書）
- `project-notes/2026-08-22-education-4gem-readme-alignment-completion.md`（4Gem・README整合完了状態と検証Evidence）
- `project-notes/2026-08-22-design-document-standard-application-scope.md`（設計文書標準の適用境界）
- `project-notes/2026-08-21-education-4gem-design-decisions.md`（旧決定を含み、単独で現行完成仕様として使用しない）
- `project-notes/2026-08-20-ai-education-staging.md`
- `project-notes/2026-08-19-4gem-names.md`（旧決定を含み、単独で現行完成仕様として使用しない）
- `personas/education/GEM_RESEARCHER_FULL.md`
- `personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
- `personas/education/GEM_RESEARCHER_DEVELOPMENT.md`
- `personas/education/archive/GEM_RESEARCHER.md`（旧版）
- `personas/education/GEM_SOLUTION_PARTNER.md`
- `personas/education/GEM_CODE_GENERATOR.md`
- `personas/education/GEM_REVIEWER.md`
- `personas/education/README.md`
- root `README.md`
