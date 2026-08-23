<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-INDEX-001 |
| Version（バージョン） | 1.0 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-08-17 |
| Last Updated（最終更新日） | 2026-08-23 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | [`personas/education/README.md`](personas/education/README.md)<br>[`personas/education/setup/GEMINI_GEM_SETUP.md`](personas/education/setup/GEMINI_GEM_SETUP.md)<br>[`personas/reference/README.md`](personas/reference/README.md) |

---

# AI Setup Materials — Persona and Configuration Repository（Persona・設定資料リポジトリ）

本リポジトリは、生成AIへ明確な役割、責務境界、禁止事項、入出力方針を与えるためのPersonaと関連資料を配布・管理します。

曖昧な依頼による推測、指示範囲外の変更、未検証の完了報告を減らし、User（生徒）がEvidenceを確認して最終判断できる運用を目的とします。

## 1. Structure（構成）

```text
personas/
├── education/   学習用：基本4Gem＋Researcher Deep Researchの追加1GemをGeminiで操作する構成
└── reference/   参考用：Education用4Gem＋1とは異なる前提の実務構成例
```

Education用の主要導線は [`personas/education/README.md`](personas/education/README.md) です。Personaの選び方、役割分担、User-firstの作業フローは、このREADMEから確認してください。

Gemini上での4Gem＋1の具体的な設定方法は [`personas/education/setup/GEMINI_GEM_SETUP.md`](personas/education/setup/GEMINI_GEM_SETUP.md) を参照してください。

Reference領域の入口は [`personas/reference/README.md`](personas/reference/README.md) です。`personas/reference/` は、Education用4Gem＋1とは役割、利用サービス、実装・検証方法の前提が異なる参考資料です。Education用の現行手順としてそのまま流用せず、設計思想や運用パターンの参考として扱ってください。

## 2. Education 4Gem＋1（Education用4Gem＋1）

基本4Gemは次のとおりです。

- `Researcher`：外部情報を一次情報中心に調査し、確認済み事実とEvidenceを示す
- `Solution Partner`：目的、要求、制約を整理し、設計とコード生成用指示を具体化する
- `Code Generator`：現行設計と仕様に従い、コード・testコードの生成、解析、修正を支援する
- `Reviewer`：設計、コード、User（生徒）が作成した検証Evidenceを独立して評価する

Gemini上では、詳細調査用としてResearcher Personaを使う `Researcher Deep Research` を1Gem追加します。これは独立した5番目のPersonaではなく、Researcherの追加Gemです。

Researcherは検索範囲が異なる3つの完成版を提供しています。

- [`GEM_RESEARCHER_FULL.md`](personas/education/GEM_RESEARCHER_FULL.md)
- [`GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`](personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md)
- [`GEM_RESEARCHER_DEVELOPMENT.md`](personas/education/GEM_RESEARCHER_DEVELOPMENT.md)

その時点で必要なModule構成を含むResearcher完成版を1本だけ選び、通常用 `Researcher` と `Researcher Deep Research` の両方へ同じPersona本体を登録します。検索範囲を変更するときは両Gemを同じ完成版へ入れ替えます。

## 3. Role of User（User（生徒）の役割）

User（生徒）が各Gemを操作し、出力を確認して、次の工程に必要な確定情報を手動で渡します。

Code Generatorが生成したコードまたはtestコードは、User（生徒）がIDEへ反映します。コードの実行、test、動作確認、検証Evidenceの作成もUser（生徒）が行います。

Reviewerの結果は最初にUser（生徒）へ返されます。修正方法、AI支援の利用、再提出、成果物と最終設計の採用・完成を最終判断するのはUser（生徒）です。

詳細な運用方法とPersonaへのリンクは [`personas/education/README.md`](personas/education/README.md) を参照してください。

## 4. Prerequisites and Notes（前提と注意事項）

- Personaは、すべての環境や用途で自動的に最適な結果を保証するものではありません。対象の要求、制約、正本を入力し、出力を確認してください。
- パスワード、APIキー、接続情報などの秘密情報を、AIへの入力、AIの出力、コード、ログ、画面、公開物へ含めないでください。
- AIが出力する「完了しました」「test成功」「問題なし」などの報告は、それだけでは検証Evidenceになりません。User（生徒）が自身の環境で実行・動作確認し、実際の結果を確認してください。
- 会話履歴やAIの記憶だけを正本として扱わず、現在有効な要求、仕様、設計、判断、検証結果を追跡できる文書や成果物へ反映してください。

## 5. License（ライセンス）

本リポジトリの文書は **Creative Commons Attribution-NonCommercial 4.0 International（CC BY-NC 4.0）** のもとで公開します。

出典を明示する限り、非営利目的における利用、改変、再配布が可能です。詳細は [`LICENSE`](LICENSE) を参照してください。

---

*本ドキュメントは入門的ガイダンス（Primer）として位置づけられており、実運用レベルの標準仕様ではありません。*

## Decision & Rationale（決定・判断理由）

### 2026-08-23

#### Education用4Gem＋1のRepository入口表現

Decision:
Repository入口ではEducation用の基本体系を4Gemとして維持し、Gemini上ではResearcher Personaを使う `Researcher Deep Research` を追加した `4Gem＋1` として案内する。設定詳細は `personas/education/setup/GEMINI_GEM_SETUP.md` へ導く。Reference領域との対比でEducationの現行構成を指す場合も `4Gem＋1` と表記する。

Reason:
基本4役割を維持しつつ、Gemini上で作成するGem実体が5つであることを入口から誤解なく案内するため。`Researcher Deep Research` を独立Personaとして扱わず、サービス固有設定の詳細を専用資料へ分離するため。

Rejected:
- Education体系を5つの独立Personaとして表現する方式
- ルートREADMEへGemini設定手順を重複記載する方式