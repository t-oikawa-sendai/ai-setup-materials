<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-EDU-INDEX-001 |
| Version（バージョン） | 1.0 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-08-19 |
| Last Updated（最終更新日） | 2026-10-17 |
| Owner（管理者） | Takashi Oikawa |
| Related Documents（関連文書） | [`../../README.md`](../../README.md)<br>[`../PERSONA_IDENTIFICATION_AND_SETUP.md`](../PERSONA_IDENTIFICATION_AND_SETUP.md)<br>[`GEM_RESEARCHER_FULL.md`](GEM_RESEARCHER_FULL.md)<br>[`GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`](GEM_RESEARCHER_LEARNING_DEVELOPMENT.md)<br>[`GEM_RESEARCHER_DEVELOPMENT.md`](GEM_RESEARCHER_DEVELOPMENT.md)<br>[`GEM_SOLUTION_PARTNER.md`](GEM_SOLUTION_PARTNER.md)<br>[`GEM_CODE_GENERATOR.md`](GEM_CODE_GENERATOR.md)<br>[`GEM_REVIEWER.md`](GEM_REVIEWER.md) |

---

# Education Personas（教育用Persona）

## 1. Purpose（目的）

このディレクトリは、職業訓練校の `User（生徒）` が調査、設計、コード生成、レビューをAIに役割分担させるためのPersona正本を管理します。

Education用の基本体系は4役割です。従来のGem構成では、詳細調査用としてResearcher Personaを使う `Researcher Deep Research` を1つ追加する **4Gem＋1** の設計です。

2026-10-16時点で、本教材の講師・生徒アカウントではGemを新規作成できないことを確認しました。以下の4Gem＋1は従来の承認済み構成であり、現在の生徒向け新規導入手順ではありません。既存Gemの利用・編集可否と、新しい導入先は未確認・未決です。

User（生徒）が各Gemを操作し、各出力を確認して、次の工程に必要な確定情報を手動で渡します。Gem同士が自動的に作業を転送したり、最終判断を行ったりする運用ではありません。

Personaそのものがなぜ重要なのか、サービス全体のカスタム指示・共通設定やその都度のプロンプトと何が違うのかは、Repository共通の説明として [`../../README.md`](../../README.md) の `Why Persona Matters（なぜPersonaが重要なのか）` を参照してください。

Personaの識別と検証の共通仕様は [`../PERSONA_IDENTIFICATION_AND_SETUP.md`](../PERSONA_IDENTIFICATION_AND_SETUP.md) にあります。Education用の基本4役割と各Personaの責務は変更していません。サービスごとの設定方法は本Repositoryの範囲外です。

## 2. 4Gem＋1 Configuration（従来の4Gem＋1構成）

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

`Researcher Deep Research` は新しいPersonaではありません。Researcher Personaを使用する従来の追加Gemです。

## 3. Selecting a Researcher Edition（Researcher完成版の選択）

Researcherは、利用する検索範囲に応じて次の完成版から1本を選びます。

- [`GEM_RESEARCHER_FULL.md`](GEM_RESEARCHER_FULL.md)：Learning / Career / Development
- [`GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`](GEM_RESEARCHER_LEARNING_DEVELOPMENT.md)：Learning / Development
- [`GEM_RESEARCHER_DEVELOPMENT.md`](GEM_RESEARCHER_DEVELOPMENT.md)：Development

従来の4Gem＋1構成では、通常調査とDeep Researchに同じResearcher完成版を使う設計でした。複数の完成版を同時に混在させる設計ではありません。

Researcherの調査対象（Learning / Career / Development）を依頼に応じて切り替える用途では、Skillsの自動適用を活かす方法を検討します。ただし、適切な検索範囲を毎回選べるかは未検証であり、Skillの構成や選択条件も未決です。[Google公式案内](https://support.google.com/gemini/answer/18560919)では、2026-10-16時点でSkillsはDeep Researchに対応していません。Deep ResearchをSkillsから自動起動・切替できるとは扱いません。Skills運用の設計・登録・実動検証はまだ行っていません。

## 4. User-first Basic Flow（User-firstの基本フロー）

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

## 5. Responsibility Boundaries（責務境界）

- Solution Partnerは設計を具体化しますが、完成コードの生成や最終判断は行いません。
- Code Generatorはコード・testコードの生成までを支援します。IDE操作、実環境への適用、実行、test結果確認、動作確認、検証Evidence作成、品質保証判定は行いません。
- User（生徒）が、生成コードをIDEへ反映し、実行、test、動作確認、Evidence作成を行います。
- Reviewerは、Solution Partnerの設計成果物、Code Generatorが生成したコード、User（生徒）が作成したEvidenceを評価し、結果を最初にUser（生徒）へ返します。
- コードに修正が必要な場合、User（生徒）が自力で修正するか、Code Generatorの支援を使うかを選びます。
- 設計に再検討が必要な場合、User（生徒）は必要に応じてSolution Partnerの支援を利用できます。
- 各Gemの出力を確認し、次の作業、採用、完成を最終判断するのはUser（生徒）です。

## 6. Reviewer Judgment（Reviewerの判定）

Reviewerは、次の4段階で判定します。

- `PASS`
- `PASS WITH NOTES`
- `REWORK REQUIRED`
- `BLOCKED`

判定の詳細、出力項目、修正案、Evidence不足時の案内は [`GEM_REVIEWER.md`](GEM_REVIEWER.md) を参照してください。Reviewerの判定はUser（生徒）の最終判断に代わるものではありません。

## 7. Evidence and Canonical Sources（Evidenceと正本）

Evidenceとは、判断、確認、検証結果を追跡できる根拠です。初心者向けには「確認に必要な記録・資料」と考えてください。

- Researcher：情報源、参照先、確認した内容
- Solution Partner：User（生徒）が示した要求、制約、確認済み事実、採用・不採用理由
- Code Generator：入力された設計・仕様、対象、変更範囲、コード解析の根拠、仮定、未確認事項
- User（生徒）：実行したtestの結果、ビルド結果、画面・実機・API等の動作確認結果
- Reviewer：対象箇所、仕様・設計との不一致、検証結果、指摘根拠

会話そのものを正本にせず、現在有効な要求、仕様、設計、判断、検証結果を追跡できる文書や成果物へ反映します。
Evidenceのない「確認済み」「完了」「問題なし」という断定は避けます。

## 8. Common Principles（共通原則）

- 確定事項、未確認事項、仮定を分離する。
- 各Gemは自分の責務を越えて、他工程の最終判断を行わない。
- 不要な機能追加、過剰な抽象化、根拠のない仕様補完を行わない。
- 問題を指摘する場合は、理由と影響を示す。
- パスワード、APIキー、接続情報などの秘密情報を、入力、出力、ログ、公開物へ含めない。

## 9. Scope（本書の範囲）

本書はPersonaの役割、効果、責務境界と、従来構成を説明します。AIサービスの設定方法は扱いません。旧Gemini設定資料の判断履歴は [`../../project-notes/DECISIONS.md`](../../project-notes/DECISIONS.md) の D-045 に保全します。
