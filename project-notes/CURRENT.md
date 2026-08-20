# CURRENT

Last Updated: 2026-08-21
Status: ACTIVE

## PURPOSE

生徒へ配布可能な `ai-setup-materials` を完成させる。

単なるAI利用方法ではなく、AIの役割分担・責務分離・Evidence・検証を重視したAI活用設計を学べる教材とする。

## CONFIRMED

- Education用Gemは4つとする。
  - `Researcher`
  - `Solution Partner`
  - `Implementer`
  - `Reviewer`
- 授業では4Gem全体を最初に提示し、説明・設定は `Researcher → Solution Partner → Implementer → Reviewer` の順で進める。
- AIごとに責務範囲を限定し、目的・判断基準・成果物を明確化する。
- 一つのAIへ調査・判断・実装・評価を集約せず、複数役割で確認・検証することで、ハルシネーションをそのまま採用するリスクを低減する。
- ハルシネーション抑止はAI利用上の重要事項とするが、役割分担で完全排除できるとは表現しない。
- 教育用4Gemには `GEM_COMMON_PERSONA.md` を設け、共通基本姿勢 + 4Gem協調ルールを定義する。
- 各Gemは `GEM_COMMON_PERSONA.md` + 個別Personaで設定する。
- `GEM_WORKFLOW.md` のような並列共通文書は新設せず、共通事項は `GEM_COMMON_PERSONA.md` に集約する。
- `Researcher` は調査・比較・Evidence・推論・候補提示まで行える。推論は確認済み事実と明確に分離し、根拠を示す。最終設計判断は行わない。
- `Researcher` の結果は `Solution Partner` が再検証し、目的・制約・既存設計と照合して設計判断する。
- `Solution Partner` は要求・要件・技術選定・設計を担当し、実装担当にならない。設計説明に必要な最小限のコード例は参考情報として許容する。
- 最終的に何を採用するかは人間が判断する。
- `Implementer` は確定設計に基づき実装・検証し、実装と設計Docの整合性を維持する。
- `Implementer` は軽微な修正を自己判断できるが、判断・理由・変更箇所・設計影響・Doc影響を明確に報告する。仕様・設計変更が必要な場合は `Solution Partner` へ戻す。
- 個人情報・秘密情報・認証・認可・外部送信・セキュリティ方針に関わる変更は軽微扱いしない。
- `Reviewer` の指摘区分は次の3つ。
  - 🔴 重大：修正必須・最優先
  - 🟡 軽微：修正必須
  - 🔵 改善推奨：PF完成の必須条件ではない。原則最大3件程度
- Reviewerは、現行の要求・仕様・設計を変えず実装修正だけで明確に解決できる場合のみ `Implementer` へ戻す。それ以外は `Solution Partner` へ戻す。
- Reviewerの総合判定は、重大・軽微0件かつ改善推奨なし=`PASS`、改善推奨あり=`PASS WITH NOTES`、重大または軽微あり=`REWORK REQUIRED`。`BLOCKED` はレビュー不能状態に限定する。
- 個人情報・秘密情報・認証・認可・外部送信・明白な脆弱性等の重大な安全上の問題は、初学者のPFでも見逃さない。一方、実務システム同等の品質を一律に要求してPF完成を阻害しない。
- 本教材ではSDDを意識し、重要な入力・判断・成果・検証結果を文書へ残して次工程へ引き渡す。会話そのものを正本にしない。
- Repositoryは `admin/` と `student/` に分離する。
- 実体Docは `admin/` 側1箇所のみを正本として管理し、`student/` 側にはコピーを置かない。`student/README.md` から必要な正本Docへ誘導する。
- `admin/` 配下の最終サブディレクトリ構成、既存フォルダの最終移動先、`AGENTS.md` の最終配置は未確定。推論で決めない。
- `AGENTS.md` / Skills / `CURRENT.md` の高度な運用は段階的に導入し、初学者へ最初から一括して要求しない。
- Education用4Gemは `AGENTS.md` / Skills / `CURRENT.md` を理解していなくても利用できる設計とする。
- 生徒はGeminiだけを使う前提ではないため、ChatGPT / Claude / Cursor / Gemini等のAIサービス別Persona資産も参照可能な形で維持する。
- READMEは詳細仕様書にせず、リポジトリの目的・背景・AIを分ける理由・4Gem概要・admin/studentの役割・詳細Docへの導線を示す入口とする。
- 既存READMEの思想・表現は、ユーザーが十分検討した内容であるため不用意に再構成しない。READMEはまず仮完成でよい。
- 明示的に確定した要求・設計・責務境界・運用方針は、会話だけに残さず、適切な `project-notes/` へこまめにGitHub記録する。
- 決定記録を更新するときは既存CONFIRMED事項を全文確認し、過去の確定事項を欠落させない。
- 推論・一般論・AIの補完をCONFIRMEDへ混入させない。不明点・矛盾・複数解釈がある場合はユーザーへ確認する。

## CURRENT TARGET

既存 `README.md` を基準に、今回確定した設計思想・管理構造を必要最小限反映して仮完成させる。

## CURRENT STATE

2026-08-21 の統合決定記録を以下へ保存済み。

- `project-notes/2026-08-21-education-4gem-design-decisions.md`

2026-08-21 に、過去の確定メモ・旧決定記録・最新対話の確定事項を照合し、統合版へ更新した。

同時に `AGENTS.md` へ、次の再発防止ルールを追加済み。

- 重要な決定をこまめにGitHubへ記録する
- 既存決定記録を全文確認してから統合する
- 過去のCONFIRMED事項を欠落させない
- 推論をCONFIRMEDへ混入させない
- 不明点・矛盾はユーザーへ確認する

既存のEducation Persona初版は作成済みだが、今回の統合決定事項をまだ完全には反映していない。

`admin/` / `student/` への物理的な再配置も未実施。

## NEXT ACTION

1. 既存READMEを精読する。
2. 既存思想を維持し、必要な追加・導線整理のみ行って仮完成させる。
3. README仮完成後、このチャットから新チャットへ移行する。
4. 新チャットで `GEM_COMMON_PERSONA.md` と個別4Gem Personaを精査する。

## DO NOT REOPEN

詳細は `project-notes/2026-08-21-education-4gem-design-decisions.md` を正として参照する。

特に次は、ユーザーから明示的な再検討指示がない限り再検討対象にしない。

- 4Gem採用
- 説明順 `Researcher → Solution Partner → Implementer → Reviewer`
- AIの責務分離を教材の中核思想とすること
- ハルシネーション抑止を重要目的とすること
- Researcherの根拠付き推論を許容すること
- Researcher結果をSolution Partnerが再検証すること
- Solution Partnerは実装担当にならないこと
- ImplementerのDoc整合性維持・軽微修正報告責務
- Reviewer分類 `重大 / 軽微 / 改善推奨`
- Reviewerの戻し先判定方式
- `GEM_COMMON_PERSONA.md` の採用
- 各Gemを共通Persona + 個別Personaで設定すること
- `admin/` / `student/` 分離
- 実体Docをadmin側1箇所のみで管理すること
- READMEへ詳細を詰め込まないこと
- 既存READMEを不用意に全面再構成しないこと
- 確定事項をこまめにGitHubへ記録し、推論・誤解釈・欠落を持ち込まないこと

## REFERENCES

- `project-notes/2026-08-19-4gem-names.md`
- `project-notes/2026-08-20-ai-education-staging.md`
- `project-notes/2026-08-21-education-4gem-design-decisions.md`
