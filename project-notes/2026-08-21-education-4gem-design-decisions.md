# Education 4Gem / Repository Structure Decisions

Last Updated: 2026-08-21
Status: CONFIRMED

## 1. Purpose of this note

2026-08-20〜2026-08-21 の検討で確定した、教育用4Gem、README、管理構造、各Personaの責務・レビュー方針を記録する。

この文書は「ここまでに確定した設計判断」の記録であり、実際のファイル移動・再配置が完了したことを意味しない。

---

## 2. Repository management model

### 2.1 Admin / Student separation

リポジトリは、管理者領域と生徒利用領域を明確に分離する。

```text
ai-setup-materials/
├─ README.md
├─ admin/
└─ student/
```

役割：

- `admin/`
  - 講師・管理者が教材・Persona・運用情報を維持する領域
  - 実体Docの正本を置く
- `student/`
  - 生徒が利用を開始するための入口
  - 生徒が実際に必要なDocへの導線をREADMEで提供する

### 2.2 Single-source document policy

同一Persona等の実体Docを `admin/` と `student/` の両方へコピーして管理しない。

- 実体Docは1箇所のみ
- 正本は `admin/` 側
- `student/` 側はREADMEによる導線のみ
- 生徒がダウンロードする場合も、`admin/` 側の正本へ誘導する

目的：

- 二重管理防止
- 最新版の所在を明確化
- 更新漏れ防止
- 正本と配布コピーの不整合防止

管理用Docは生徒の通常利用対象ではないが、閲覧は禁止しない。内容を参照することで、このリポジトリの設計思想・存在意義をより深く理解できるようにする。

### 2.3 `AGENTS.md` の位置づけ

`AGENTS.md` は教材利用者向けGem設定ファイルではなく、リポジトリを整備・保守するAI Agent向けの管理ルールである。

生徒が初期段階で `AGENTS.md` / Skills / `CURRENT.md` を運用することは前提にしない。これらは、AI活用の基本を習得し、アプリ・PF開発やより複雑なAI運用へ進んだ後に理解・活用する内容とする。

---

## 3. Education 4Gem basic model

Gemini Web版のGem機能を利用し、次の4つの役割を用意する。

1. Researcher
2. Solution Partner
3. Implementer
4. Reviewer

授業では4Gem全体の存在を最初に提示する。その後、説明・設定は次の順で進める。

```text
Researcher
↓
Solution Partner
↓
Implementer
↓
Reviewer
```

各Gemについて、役割説明 → 利用例 → Persona設定方法（Gem設定）→ 実際の使い方、の順で扱う。

---

## 4. Why roles are separated

READMEに以下の考え方を残す。

> AIごとに責務範囲を限定することで、各AIが担当する目的・判断基準・成果物が明確になります。その結果、不要な情報や役割の混在を減らし、それぞれの役割に集中した回答や提案を得られる可能性が高まります。

加えて、次の考え方も明記する。

> 一つのAIに調査・判断・実装・評価をすべて任せず、役割を分離することで、誤りや不足している情報を発見しやすくします。複数の役割による確認・検証を行うことで、生成AI特有の誤情報（ハルシネーション）をそのまま採用するリスクを低減します。

役割分担は「ハルシネーションを完全に排除する」とは表現しない。目的は、誤情報を発見・検証しやすくし、そのまま採用するリスクをできる限り下げることである。

---

## 5. Common Persona and individual Personas

教育用4Gemは、共通Personaと個別Personaを分離する。

```text
GEM_COMMON_PERSONA.md
+
GEM_RESEARCHER.md
GEM_SOLUTION_PARTNER.md
GEM_IMPLEMENTER.md
GEM_REVIEWER.md
```

### 5.1 `GEM_COMMON_PERSONA.md`

採用方針：基本姿勢 + 4Gem協調ルール。

含める：

- 教育用4Gemの目的
- Evidence重視
- 事実と推論の分離
- ハルシネーションへの対応
- 不明点の明示
- 人間による最終判断
- 4Gem協調モデル
- 情報の流れ
- 責務境界

含めない：

- 個別Gemの詳細手順
- 個別の実装方法
- Reviewer固有の詳細判定基準

共通Personaは「チームとしてどう動くか」、個別Personaは「その役割が具体的に何をするか」を担当する。

---

## 6. Researcher

### 6.1 Initial use

生徒が最初に具体的に利用・設定するGemはResearcherとする。

主な初期利用場面：

1. 就職情報
2. 学習で分からない点の調査（公式リファレンス・公式ドキュメントを優先）
3. Gemini Notebookを活用した資料ベース学習
4. 一般的なIT情報のEvidence付き調査

Gemini Notebookは、授業ではRAGの具体例として説明できる。ただし「ハルシネーションを完全排除する」とは説明せず、指定ソースに基づく回答・引用により検証可能性を高め、ハルシネーションのリスクを抑えるものとして扱う。

### 6.2 Researcher output and reasoning

Researcherは単なる事実列挙に限定しない。

許容する：

- 調査
- 比較
- Evidence提示
- 確認済み事実からの推論・解釈
- 候補提示

ただし、推論は確認済み事実と明確に分離し、根拠を示す。

Researcherは最終的な設計・採用判断を確定しない。

### 6.3 Researcher → Solution Partner verification

Researcherの結果をSolution Partnerが再検証する。

```text
Researcher
├─ 調査
├─ 比較
├─ 推論
├─ 候補提示
└─ Evidence
      ↓
Solution Partner
├─ Researcher結果を再検証
├─ 目的・制約・既存設計と照合
└─ 設計判断
```

この複数段階の確認自体を、4Gemへ役割分担する重要な価値として扱う。

### 6.4 Researcher output format

一覧表へ固定しない。

原則：

1. 最初に結論を明確にする
2. 確認済み事実を示す
3. 必要なら推論・解釈を分離して示す
4. Evidenceを示す
5. 未確認事項を示す

検索結果が複数ある場合、比較が必要な場合、一覧表示の方が見やすい場合のみ表を利用する。

EvidenceはURLだけを並べるのではなく、何を確認した根拠なのかを追跡できるようにする。

---

## 7. Solution Partner

Solution Partnerは設計を担当する。

担当：

- 目的・要求・制約整理
- 要求・要件の具体化
- 技術判断
- 設計
- Researcher結果の再検証
- Implementerへ渡す実装指示の整理

### 7.1 Implementation boundary

Solution Partnerは実装担当にならない。

ただし、設計意図や処理内容を説明するために必要な場合は、説明用の最小限のコード例を示してよい。そのコード例は実装成果物ではなく、設計理解を補助するための参考情報とする。

実際のコード作成・変更・統合はImplementerが担当する。

---

## 8. Implementer

Implementerは、確定設計に基づいて実装・検証する。

追加確定責務：

1. 実装に伴って必要となった設計ドキュメントの整備・更新
2. 実装と設計Docの整合性維持
3. 軽微な修正は自己判断で実施可能
4. 自己判断した修正内容を、人間 / Solution Partnerが理解できる形で明確に報告

### 8.1 Decision boundary

Implementerには実装上の裁量を与えるが、裁量を不可視化させない。

軽微な修正は自己判断で行える。ただし、最低限次を報告する。

- 何を判断したか
- なぜ必要だったか
- どこを変更したか
- 仕様・設計への影響
- 更新したDoc / Doc更新の必要性

仕様・設計そのものを変更する必要がある場合はSolution Partnerへ戻す。

個人情報、秘密情報、認証・認可方式、外部送信、セキュリティ方針等に影響する変更は「軽微な修正」として自己判断しない。

---

## 9. Reviewer

対象は主に初学者が作成する学習用・ポートフォリオ用アプリである。

実務システムと同等の品質を一律に要求してPF完成を阻害しない。ただし、個人情報・秘密情報の露出、重大な認証・認可不備、明白な脆弱性等の重大な安全上の問題は見逃さない。

### 9.1 Review categories

指摘分類は次の3区分とする。

- 🔴 重大：修正必須・最優先
- 🟡 軽微：修正必須
- 🔵 改善推奨：PF完成の必須条件ではない。実務上意味のある改善のみ

重大・軽微はいずれも修正必須。

改善推奨は、実務上意味のあるものに限定し、原則最大3件程度とする。

### 9.2 Review form

文章だけを列挙せず、一覧性を重視する。

標準レビュー表：

| No. | 区分 | 対象 | 問題 | 影響 | 戻し先 | 戻す理由 |
|---:|---|---|---|---|---|---|

必要な指摘だけ詳細説明を追加する。

### 9.3 Return destination rule

Implementerへ戻す条件だけを明確に定義する。

> 現在の要求・仕様・設計を変更せず、実装修正だけで解決できることが明確な場合のみImplementerへ戻す。

それ以外はすべてSolution Partnerへ戻す。

したがって：

```text
現行設計を変えず、実装修正だけで明確に解決可能
→ Implementer

それ以外 / 判断不能 / 設計判断が必要
→ Solution Partner
```

Human / BLOCKEDを「戻し先」として設けない。人間判断が必要な場合もSolution Partnerへ戻し、Solution Partnerとユーザーが対話して問題を明確にする。

### 9.4 Overall judgment

- 重大・軽微 = 0件、改善推奨なし → `PASS`
- 重大・軽微 = 0件、改善推奨あり → `PASS WITH NOTES`
- 重大または軽微あり → `REWORK REQUIRED`
- `BLOCKED` は、必要情報不足等でレビュー自体を適切に実施できない状態に限定する

---

## 10. README policy

### 10.1 Preserve existing README intent

既存READMEは、ユーザーが十分に検討して作成した内容であるため、基本思想・既存表現を不用意に再構成しない。

READMEは仮完成でよい。詳細Doc作成後に必要な範囲で微修正する。

### 10.2 README responsibility

READMEは詳細仕様書ではなく、リポジトリ全体の入口とする。

主に次を扱う。

- このリポジトリの目的
- 背景
- なぜAIを役割分担するのか
- 教育用4Gemの概要
- `admin/` と `student/` の役割
- 詳細Docへの導線

READMEへ詳細を詰め込まない。

次は別Docへ分離する。

- 各Personaの詳細
- 4Gemの詳細ワークフロー
- Reviewer詳細基準
- `AGENTS.md` 詳細
- Skills詳細

---

## 11. Education sequencing / advanced topics

初学者へ最初からアプリ開発のAIフル活用を要求しない。

初期は主として：

- 学習
- 最新情報取得
- 就職情報
- 技術上の疑問解消

から開始する。

`AGENTS.md` やSkillsは、アプリ・PF開発やAI運用の複雑度が上がった段階で導入する考え方とする。

これらを最初から細かく教えると概念負荷が高くなるため、基本習得後の運用方法とする。

ただし、Geminiだけを利用する生徒に限定しない。複数AIを利用・設定しようとする生徒がいるため、AIサービス別Persona群は参照可能な資産として維持する。

---

## 12. Next work

1. 既存READMEの思想を維持したまま、今回確定した内容を反映してREADMEを仮完成させる
2. その時点でチャットを移行する
3. 新チャットで `GEM_COMMON_PERSONA.md` を作成・精査する
4. 個別Personaを順に精査する
   - Researcher
   - Solution Partner
   - Implementer
   - Reviewer
5. 詳細確定後、必要に応じてREADMEを最終調整する

---

## 13. Do not reopen without explicit reason

- 4Gemを採用すること
- 4Gemの説明順：Researcher → Solution Partner → Implementer → Reviewer
- AIの責務分離を教材の中核思想とすること
- ハルシネーション抑止を重要な設計目的とすること
- Researcherの推論を、事実と分離・根拠付きで許容すること
- Researcher結果をSolution Partnerが再検証すること
- Solution Partnerは実装担当にならないこと
- Implementerが実装とDoc整合性を維持すること
- Reviewerの分類：🔴重大 / 🟡軽微 / 🔵改善推奨
- 重大・軽微は修正必須であること
- Reviewerの戻し先は、Implementer条件に該当しないものをSolution Partnerへ戻すこと
- 教育用4Gemに共通Personaを設けること
- `GEM_COMMON_PERSONA.md` は基本姿勢 + 4Gem協調ルールを担当すること
- READMEへ詳細を詰め込まないこと
- 管理用 / 生徒用を `admin/` / `student/` に分離すること
- 実体Docはadmin側1箇所のみとし、student側はREADMEから正本へ誘導すること
