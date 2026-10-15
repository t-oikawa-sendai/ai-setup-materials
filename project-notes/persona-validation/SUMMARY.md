# Persona検証の期間集計

集計の入口である。原文は `raw/`、日別の記録は `assessments/` に置く。このファイルへ原文を複製しない。

## 2026-10-14 の件数

この節は検証用Personaの記録である。2026-10-15の件数には含めない。

| 項目 | 値 |
|---|---|
| 検証日数 | 1日 |
| 質問 | 1種類（`Gemini4の性能は？`） |
| 回答 | 3件（Gemini、Claude、ChatGPT） |
| 対象期間 | 2026-10-14 |

2026-10-14の記録は `assessments/2026-10-14.md` を参照する。回答内容の正確性評価は未実施である。

## 2026-10-15 の件数

この節は ChatGPT Persona `M-CG` Version 1.2（提案）/ Draft に対する D-025 の記録である。2026-10-14の件数には含めない。保存された原文の件数と、正規比較の件数は別である。Decisionは `project-notes/DECISIONS.md` の D-032。

### 保存された原文

| 項目 | 値 |
|---|---|
| 旧18件 | ChatGPT従来Project 6、Claude Project 6、Gemini Gem 6。commit `86b3537dfb8c2eacca851763c00055500ee122bd` に保存済み |
| 再テスト | ChatGPT検証専用Project 6。原文は `raw/2026-10-15-chatgpt-retest-tc01-run1.md` から `raw/2026-10-15-chatgpt-retest-tc03-run2.md` |
| 累積原文 | 24件 |

### 参考履歴

従来ChatGPT Projectの回答内容評価は 6/6 PASS である。原文と当時の評価は維持する。正規比較には算入しない。

### 正規比較

| 対象 | PASS | FAIL |
|---|---|---|
| ChatGPT検証専用Project | 4/6 | 2 |
| Claude Project | 2/6 | 4 |
| Gemini Gem | 3/6 | 3 |
| 合計 | 9/18 | 9 |

```text
PASS（最大6回）                        FAIL
ChatGPT検証専用Project  ████░░  4/6     2
Claude Project         ██░░░░  2/6     4
Gemini Gem             ███░░░  3/6     3
```

正規比較の合計は 9 PASS / 9 FAIL（18回答）である。日別の判定理由は `assessments/2026-10-15.md` を参照する。順位とモデル間の優劣は記入しない。Persona適用状態は未確認である。Project間の結果差の原因は未確認である。

## 未集計

2026-10-14の回答内容の正確性評価は未実施である。いずれの日も、順位とモデル間の優劣は記入しない。

反復の回数、質問セット、実施頻度は未決定である。決まるまで、このファイルへ推測値を追加しない。
