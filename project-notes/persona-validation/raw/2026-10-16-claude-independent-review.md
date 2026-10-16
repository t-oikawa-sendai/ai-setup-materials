<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | なし（レビュー結果。Repository正本ではない） |
| Title（表題） | Claude Project GitHub取得方式（G方式）独立レビュー結果 |
| Status（ステータス） | Draft |
| Created Date（作成日） | 2026-10-16 |
| From（作成） | Claude（レビュー担当。Persona：M-CL@1.5（提案）、Project指示欄の本文を使用） |
| To（宛先） | ChatGPT（設計担当） |
| Owner（管理者） | t-oikawa-sendai |

---

# Claude Project GitHub取得方式（G方式）独立レビュー結果

## 0. この文書の性格

- レビュー担当（Claude）から設計担当（ChatGPT）への、レビュー結果と設計見直し要請である。
- Cursor向けの実装指示ではない。Persona本文の完成稿、指示欄用完成文章は含まない。
- 修正の採否はUserが判断する。設計担当は、User判断の後に設計を確定する（`AGENTS.md:113`、`:120`）。

## 1. 対象

| 項目 | 値 |
|---|---|
| Repository | `t-oikawa-sendai/ai-setup-materials` |
| URL | https://github.com/t-oikawa-sendai/ai-setup-materials |
| branch | `main` |
| 確認HEAD | `a908abaf46b0a4bbd8b37c16cf0efdb2ab69fe62`（GitHub main と一致を確認） |
| 作業種別 | 読取専用（変更、commit、pushは行っていない） |
| レビュー種別 | AI制御資産レビュー |
| 適用範囲 | 差分（G方式に関わる範囲。Gemini Gemは対象外） |
| AGENTS.md | ReadOK |

確認した正本：

1. `AGENTS.md`
2. `personas/reference/CLAUDE_PERSONA.md`
3. `personas/PERSONA_IDENTIFICATION_AND_SETUP.md`
4. `project-notes/DECISIONS.md` の D-005、D-011、D-021、D-022、D-033、D-034、D-035

## 2. 結論

| 項目 | 判定 |
|---|---|
| 総合判定 | **条件付き合格** |
| 最優先問題 | GOV-01 |
| 本番投入可否 | 条件付き（GOV-01の解消後） |
| Approvedへの昇格 | 対象外（PASSは昇格を意味しない。`PERSONA_IDENTIFICATION_AND_SETUP.md:382`） |

### 2.1 レビュー対象2点の扱い

| 対象 | 状態 |
|---|---|
| Claude Project用GitHub読込指示文 | User報告：別Projectのチャットで確認完了、PASS。本レビューでは原文未確認（UNVERIFIED） |
| 「ペルソナ検証」の回答 | 同上 |
| 検証時に使用した本文 | User報告：GitHub `a908aba` の本文 |

本レビューは、上記2点の原文を独自に再判定していない。判定の根拠は、正本4点の照合と、User報告のPASSである。

### 2.2 重点確認事項の判定

| # | 重点確認事項 | 判定 | 根拠 |
|---|---|---|---|
| 1 | 確定仕様と矛盾しないか | 正本側に矛盾なし。指示文の原文は未確認 | `PERSONA_IDENTIFICATION_AND_SETUP.md:324`、`:385` |
| 2 | 未確定の取得方式を確定扱いしていないか | 正本では「GitHub取得の具体的な実装方式」はUNRESOLVED。指示文の原文は未確認 | 同 `:324`、`AGENTS.md:29` |
| 3 | G/P/N/? の分類 | 正本は4旗のみで一貫している | 同 `:142-149`、`CLAUDE_PERSONA.md:341-344` |
| 4 | 取得と適用の区別 | 正本は区別している。ただしP本文とG本文が併存するときの適用規則がない（GOV-02） | 同 `:152`、`:384`、`CLAUDE_PERSONA.md:331` |
| 5 | 取得失敗時の誤報告防止 | 正本は禁止を明記している | 同 `:153-154`、`CLAUDE_PERSONA.md:327`、`:346` |
| 6 | 新チャットでの再取得 | 正本は規定している | `CLAUDE_PERSONA.md:331-333` |
| 7 | 取得成功を客観的に確認できるか | **現行仕様では不可**。Gは自己申告であり、Verification Codeは未確定 | 同 `:151`、D-011、`CLAUDE_PERSONA.md:322` |
| 8 | 既存Personaの責務を損なわないか | 正本側に損傷なし（D-033、D-034、D-035の非変更範囲） | `project-notes/DECISIONS.md` |

重点7について：客観的な取得確認の手段を追加するかは、User判断事項である。現行仕様の不備としては扱わない。

## 3. 問題点

### GOV-01 指示欄版とGitHub版で、本文が違うのにVersion表示が同じ

| 項目 | 内容 |
|---|---|
| 重要度 | MEDIUM |
| 真因分類 | 統制欠陥 |
| 対象箇所 | `personas/reference/CLAUDE_PERSONA.md:5`、`:18`、`:176-189`。レビュー担当Projectの指示欄 |
| 問題 | レビュー担当Projectの指示欄（P方式）に登録された本文と、GitHub版 `a908aba` の本文が異なる。両方とも `Version 1.5（提案）` と表示する |
| 根拠 | GitHub版18行目は「本実装は作成・投入しない…他の提示は §11」である。指示欄は「本実装コードは作成・投入しない…その他に提示できるものは §11」である。GitHub版の§7は項目一覧（D-035で短縮）だが、指示欄の§7はMarkdownのひな形全文である。1.5を記録したcommitは `a908aba` の1件だけであり、指示欄の版はGitHub履歴にない、D-035適用前の中間版と判断できる |
| 影響 | 回答識別表示 `M-CL@1.5（提案）` では、どちらの本文が使われたかを区別できない。今回のPASSはGitHub版で得られたもの（User報告）であり、指示欄版は検証されていない |
| 最小安全修正 | P方式の登録内容を、`a908aba` の登録対象範囲（`# Claude Persona` から本文末尾まで。末尾改行を含めて7,926文字。D-035）で差し替える。Persona本文の変更は不要 |
| 再検証 | 指示欄の全文と、GitHub版の登録対象範囲を比較し、差分0件を確認する |

### GOV-02 P本文とG本文が併存するときの適用規則がない

| 項目 | 内容 |
|---|---|
| 重要度 | MEDIUM |
| 真因分類 | 設計欠陥 |
| 対象箇所 | `personas/reference/CLAUDE_PERSONA.md:331`、`:341-344`。`personas/PERSONA_IDENTIFICATION_AND_SETUP.md:152` |
| 問題 | 指示欄に本文があり、GitHubから別の本文を取得できた場合に、どちらの規則を適用するかが定義されていない |
| 根拠 | §15.3の「再取得できたときだけ更新後の値を使う」は、「値」が表示値（ID、Version）だけなのか、本文の規則の適用まで含むのかが不明である。取得状態はG/Pのどちらか1つしか表示できない。共通仕様は、取得と適用を別の事実として扱っている |
| 影響 | 「G@新Version」と表示しながら、指示欄の旧い規則で回答する状態が、規則上は許されてしまう |
| 最小安全修正 | G方式の指示文に、「G取得に成功した場合は、取得した本文を適用する（または指示欄の本文を適用する）」を1文で明記する。取得の実装方式はUNRESOLVED（`PERSONA_IDENTIFICATION_AND_SETUP.md:324`）のため、どちらにするかはUser判断事項とする |
| 再検証 | 指示欄とGitHubで本文が異なる状態で「ペルソナ検証」を行い、表示した状態と、実際に従った規則が一致するかを確認する |

### GOV-03 CURRENT.mdの作業中欄が、push済みを反映していない

| 項目 | 内容 |
|---|---|
| 重要度 | LOW |
| 真因分類 | 統制欠陥（古い記述の残存） |
| 対象箇所 | `project-notes/CURRENT.md:218`（作業中） |
| 問題 | 「commit と push は未実施である」とあるが、当該内容は `a908aba` として main へpush済みである |
| 最小安全修正 | 作業中の当該文だけを、現状に合わせて更新する |
| 再検証 | CURRENT.mdの作業中の記載と `git log` を照合する |

## 4. 設計担当への要請

1. GOV-01、GOV-02について、Userへの確認事項を整理する。GOV-02は、どちらの本文を適用するかのUser判断が必要である。
2. 今回のPASSの記録を、D-005に従い `project-notes/persona-validation/` へ保存する設計を作る。記録には次を含める。
   - 使用した本文：GitHub `a908abaf46b0a4bbd8b37c16cf0efdb2ab69fe62`
   - 実施場所：別のClaude Project（User報告）
   - 指示欄版（GOV-01）は今回の検証対象外であること
3. PASSを理由にApprovedへ昇格させない。最終Approvedは Version 1.4（D-003）のままである。

## 5. 未確認事項

| 項目 | 内容 |
|---|---|
| 指示文と検証回答の原文 | 本レビューでは未確認。PASSはUser報告に依拠する |
| Claude Projectのチャット内でGitHub本文を取得する手段 | Claudeの現行仕様は未確認。本レビューの取得は、会話環境のシェルによるものであり、G方式の実証ではない |
| 指示欄版の文字数 | 未実測。8,000文字以内（D-035）への適合は未確認 |
