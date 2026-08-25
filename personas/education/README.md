<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-EDU-INDEX-001 |
| Version（バージョン） | 1.0 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-08-19 |
| Last Updated（最終更新日） | 2026-08-25 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | [`../../README.md`](../../README.md)<br>[`GEM_RESEARCHER_FULL.md`](GEM_RESEARCHER_FULL.md)<br>[`GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`](GEM_RESEARCHER_LEARNING_DEVELOPMENT.md)<br>[`GEM_RESEARCHER_DEVELOPMENT.md`](GEM_RESEARCHER_DEVELOPMENT.md)<br>[`GEM_SOLUTION_PARTNER.md`](GEM_SOLUTION_PARTNER.md)<br>[`GEM_CODE_GENERATOR.md`](GEM_CODE_GENERATOR.md)<br>[`GEM_REVIEWER.md`](GEM_REVIEWER.md)<br>[`setup/GEMINI_GEM_SETUP.md`](setup/GEMINI_GEM_SETUP.md) |

---

# Education Personas（教育用Persona）

## 1. Purpose（目的）

このディレクトリは、職業訓練校の `User（生徒）` がGeminiのGemを使って、調査、設計、コード生成、レビューを役割分担しながら進めるためのPersona正本を管理します。

Education用の基本体系は4Gemです。Gemini上では、詳細調査用としてResearcher Personaを使う `Researcher Deep Research` を1つ追加し、**4Gem＋1** として運用します。

User（生徒）が各Gemを操作し、各出力を確認して、次の工程に必要な確定情報を手動で渡します。Gem同士が自動的に作業を転送したり、最終判断を行ったりする運用ではありません。

## 2. Why Persona Matters（なぜPersonaが重要なのか）

Geminiへ「どのように答えてほしいか」「どの役割で動いてほしいか」「今回何をしてほしいか」を伝える方法は、同じものではありません。

本教材では、違いを次のように整理します。

| 観点 | パーソナル インテリジェンスのカスタム指示 | Gem内のPersona・指示 | その都度のプロンプト |
|---|---:|---:|---:|
| 継続性 | ★★★★★ | ★★★★★ | ★☆☆☆☆ |
| 適用範囲 | 通常のGemini利用 | そのGem | その質問・会話 |
| 回答スタイルへの影響 | ★★★★★ | ★★★★★ | ★★★★☆ |
| AIの役割への影響 | ★★★☆☆ | ★★★★★ | ★★★★☆ |
| 専門的な責務の固定 | ★★☆☆☆ | ★★★★★ | ★★★☆☆ |
| 具体的タスクへの影響 | ★★☆☆☆ | ★★★★☆ | ★★★★★ |
| 回答形式への影響 | ★★★★☆ | ★★★★★ | ★★★★★ |
| 毎回入力する必要 | 不要 | 不要 | 必要 |
| 主な用途 | 普段どう答えてほしいか | **このAIは何者で、何を担当するか** | 今回何をしてほしいか |
| Gem利用時 | 原則として適用されない | 適用される | 適用される |

> **注意：** 星の数はGoogleが公開している内部的な優先順位ではありません。本教材で、各設定が回答へどの程度・どのような種類の影響を与えるかを理解するための目安です。

3つを一言で表すと、次のようになります。

```text
パーソナル インテリジェンスのカスタム指示
「私は、普段こう答えてほしい」

Gem内のPersona・指示
「あなたは、こういう役割のAIである」

その都度のプロンプト
「今回は、これをしてほしい」
```

パーソナル インテリジェンスのカスタム指示は、結論から説明する、長い説明を箇条書きにするなど、普段の回答方法を自分に合わせるために有効です。

一方、Personaは、そのAIの **Role（役割）・Responsibility（責務）・Boundary（責務境界）・Decision Criteria（判断基準）・Output（出力）** を定義します。

そのため、本教材では「毎回うまいプロンプトを書くこと」だけに依存せず、役割ごとのPersonaをGemへ設定します。PersonaによってAIの担当範囲をあらかじめ明確にし、そのうえで毎回のプロンプトから具体的な作業を依頼します。

なお、Googleの現行案内では、パーソナル インテリジェンスのカスタム指示はGemなど一部機能では利用できません。したがって、Gemで使用する役割・責務はGem自身の `カスタム指示` にPersonaとして設定します。

パーソナル インテリジェンスのカスタム指示の有効性、制約、設定方法、およびGemへのPersona登録方法は [`setup/GEMINI_GEM_SETUP.md`](setup/GEMINI_GEM_SETUP.md) を参照してください。

## 3. Current 4Gem＋1（現行4Gem＋1）

基本4Gemは次の4つです。

| Gem Display Name（Gem表示名） | Persona File（Personaファイル） | Primary Responsibility（主な責務） |
|---|---|---|
| Researcher | 下記3完成版から1本を選択 | 必要な外部情報を一次情報中心に調査し、確認済み事実とEvidenceを渡す |
| Solution Partner | [`GEM_SOLUTION_PARTNER.md`](GEM_SOLUTION_PARTNER.md) | 目的、要求、制約を整理し、設計とコード生成用指示を具体化する |
| Code Generator | [`GEM_CODE_GENERATOR.md`](GEM_CODE_GENERATOR.md) | 現行設計と仕様に従い、コード・testコードの生成、解析、修正を支援する |
| Reviewer | [`GEM_REVIEWER.md`](GEM_REVIEWER.md) | 設計、コード、User（生徒）が作成した検証Evidenceを独立して評価する |

これに、詳細調査用として次の1Gemを追加します。

| Additional Gem（追加Gem） | Persona | Purpose（用途） |
|---|---|---|
| Researcher Deep Research | Researcherと同じ選択済みPersona | Deep Researchを使う企業研究・業界研究・比較調査などの詳細調査 |

`Researcher Deep Research` は新しいPersonaではありません。Researcher Personaを使用する追加Gemです。Gemini上の設定方法は [`setup/GEMINI_GEM_SETUP.md`](setup/GEMINI_GEM_SETUP.md) を参照してください。

## 4. Selecting a Researcher Edition（Researcher完成版の選択）

Researcherは、利用する検索範囲に応じて次の完成版から1本を選びます。

- [`GEM_RESEARCHER_FULL.md`](GEM_RESEARCHER_FULL.md)：Learning / Career / Development
- [`GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`](GEM_RESEARCHER_LEARNING_DEVELOPMENT.md)：Learning / Development
- [`GEM_RESEARCHER_DEVELOPMENT.md`](GEM_RESEARCHER_DEVELOPMENT.md)：Development

その時点で必要なModule構成を含む完成版を1本だけ選び、通常用 `Researcher` と `Researcher Deep Research` の両方に同じPersona本体を登録します。複数のResearcher完成版を同時に混在させません。検索範囲を変えたいときは、両Gemを同じ新完成版へ入れ替えます。

## 5. User-first Basic Flow（User-firstの基本フロー）

```text
User（生徒）が目的・要求を整理する
  ↓
必要に応じてResearcherで外部情報を調査する
  ↓ User（生徒）が確認済み事実とEvidenceを確認して渡す
Solution Partnerで要求・制約・設計を具体化する
  ↓ User（生徒）が現行設計とコード生成用指示を確認して渡す
Code Generatorでコードまたはtestコードの生成支援を受ける
  ↓
User（生徒）がコードをIDEへ反映し、実行、test、動作確認を行う
  ↓ User（生徒）が検証Evidenceを作成して提出する
Reviewerが設計、コード、検証Evidenceを評価する
  ↓ レビュー結果は最初にUser（生徒）へ返る
User（生徒）が修正方法、再提出、採用、完成を最終判断する
```

Researcherは必要な場面で利用し、常に直列で呼び出す必要はありません。通常の調査には `Researcher`、企業研究・業界研究・比較調査など複数情報源を横断する詳細調査には `Researcher Deep Research` を使い分けます。

各Gemへ過去の会話を丸ごと渡すのではなく、その工程に必要な現行の要求、仕様、設計、EvidenceだけをUser（生徒）が選んで渡します。

## 6. Responsibility Boundaries（責務境界）

- Solution Partnerは設計を具体化しますが、完成コードの生成や最終判断は行いません。
- Code Generatorはコード・testコードの生成までを支援します。IDE操作、実環境への適用、実行、test結果確認、動作確認、検証Evidence作成、品質保証判定は行いません。
- User（生徒）が、生成コードをIDEへ反映し、実行、test、動作確認、Evidence作成を行います。
- Reviewerは、Solution Partnerの設計成果物、Code Generatorが生成したコード、User（生徒）が作成したEvidenceを評価し、結果を最初にUser（生徒）へ返します。
- コードに修正が必要な場合、User（生徒）が自力で修正するか、Code Generatorの支援を使うかを選びます。
- 設計に再検討が必要な場合、User（生徒）は必要に応じてSolution Partnerの支援を利用できます。
- 各Gemの出力を確認し、次の作業、採用、完成を最終判断するのはUser（生徒）です。

## 7. Reviewer Judgment（Reviewerの判定）

Reviewerは、次の4段階で判定します。

- `PASS`
- `PASS WITH NOTES`
- `REWORK REQUIRED`
- `BLOCKED`

判定の詳細、出力項目、修正案、Evidence不足時の案内は [`GEM_REVIEWER.md`](GEM_REVIEWER.md) を参照してください。Reviewerの判定はUser（生徒）の最終判断に代わるものではありません。

## 8. Evidence and Canonical Sources（Evidenceと正本）

Evidenceとは、判断、確認、検証結果を追跡できる根拠です。初心者向けには「確認に必要な記録・資料」と考えてください。

- Researcher：情報源、参照先、確認した内容
- Solution Partner：User（生徒）が示した要求、制約、確認済み事実、採用・不採用理由
- Code Generator：入力された設計・仕様、対象、変更範囲、コード解析の根拠、仮定、未確認事項
- User（生徒）：実行したtestの結果、ビルド結果、画面・実機・API等の動作確認結果
- Reviewer：対象箇所、仕様・設計との不一致、検証結果、指摘根拠

会話そのものを正本にせず、現在有効な要求、仕様、設計、判断、検証結果を追跡できる文書や成果物へ反映します。
Evidenceのない「確認済み」「完了」「問題なし」という断定は避けます。

## 9. Common Principles（共通原則）

- 確定事項、未確認事項、仮定を分離する。
- 各Gemは自分の責務を越えて、他工程の最終判断を行わない。
- 不要な機能追加、過剰な抽象化、根拠のない仕様補完を行わない。
- 問題を指摘する場合は、理由と影響を示す。
- パスワード、APIキー、接続情報などの秘密情報を、入力、出力、ログ、公開物へ含めない。

## 10. Gemini Setup（Gemini設定）

Geminiのパーソナル インテリジェンスにあるカスタム指示の有効性・制約・設定方法と、Gemini上での `名前`、`説明`、Gemの `カスタム指示`、`デフォルト ツール`、`知識` の設定方法、および4Gem＋1の具体的な作成手順は [`setup/GEMINI_GEM_SETUP.md`](setup/GEMINI_GEM_SETUP.md) を参照してください。

## Decision & Rationale（決定・判断理由）

### 2026-08-25

#### Persona重要性を先に理解する導入構成

Decision:
Education READMEの前半に、パーソナル インテリジェンスのカスタム指示、Gem内のPersona・指示、その都度のプロンプトを比較する表を配置する。その比較から、PersonaがAIの役割・責務・責務境界・判断基準・出力を継続的に定義するため重要であることを説明してから、現行4Gem＋1の紹介へ進む。

Reason:
Personaの定義を先に説明するだけでは、初学者にとって「なぜPersonaを設定する必要があるのか」が理解しにくい。普段の回答方法を調整するカスタム指示、AIの役割を定義するPersona、その場の作業を依頼するプロンプトを比較することで、それぞれの責務とPersonaの必要性を先に理解できるため。

また、Googleの現行仕様ではパーソナル インテリジェンスのカスタム指示はGemなど一部機能では利用できないため、Gemで役割・責務を継続的に与えるにはGem自身の `カスタム指示` へPersonaを設定する必要がある。この仕様上の違いも初学者の誤解防止に必要である。

Rejected:
- Personaの定義・4Gem一覧を先に提示し、カスタム指示やプロンプトとの違いを後から説明する構成
- パーソナル インテリジェンスのカスタム指示とGemの `カスタム指示` を同じものとして説明する構成

### 2026-08-23

#### Education用4Gem＋1とGemini設定資料への導線

Decision:
Education用の基本体系は4Gemとして維持し、Gemini上ではResearcher Personaを使う `Researcher Deep Research` を追加した `4Gem＋1` として運用する。Education READMEにはこの関係を明記し、Gemini固有の設定詳細は `setup/GEMINI_GEM_SETUP.md` へ委譲する。

Reason:
`Researcher Deep Research` は独立した5番目のPersonaではなく、Researcherの詳細調査用追加Gemであるため。基本4役割を維持しながらGemini上の実体数が5Gemになることを明示し、Persona説明とサービス固有設定の責務を分離するため。

Rejected:
- Education体系そのものを5つの独立Personaとして扱う方式
- Gemini固有の設定手順をEducation README本文へ重複記載する方式