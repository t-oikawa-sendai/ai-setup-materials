# Persona正本のP方式適合性・横断点検

- 日付：2026-10-28
- 対象Repository：t-oikawa-sendai/ai-setup-materials
- branch：main（ローカル作業差分）
- 基準commit：40e1e9785a29b315849f85a5ab52780ad1461824
- 作業先：独立Clone。開始時HEADとorigin/mainが一致、未commit変更なし。
- 根拠となるUser決定：DECISIONS.md D-076。
- 判定範囲：本文の静的点検。利用環境での実動検証ではない。

## 判定基準

1. 正本を無改変で指示欄に置き、P方式として使用できる。
2. 自己初期化・新規チャット開始・更新確認が無条件のGitHub取得を要求しない。
3. G取得指示とPersona本文を別管理し、P用・G用の別本文を作らない。
4. 業務責務と既存の識別・検証境界を保持する。

## 全現行Personaの点検結果

| ファイル | 検出事項・処置 | 修正後Version / Status | 文字数 |
|---|---|---|---:|
| personas/reference/CHATGPT_PERSONA.md | §11.3の無条件GitHub更新取得 | 3.2 / Draft | 8729 |
| personas/reference/CLAUDE_PERSONA.md | §15.3の無条件GitHub更新取得 | 3.1 / Draft | 8517 |
| personas/reference/CURSOR_PERSONA.md | 衝突なし。本文を維持 | 3.0 / Approved | 7705 |
| personas/reference/GEMINI_PERSONA.md | 衝突なし。本文を維持 | 3.0 / Approved | 6488 |
| personas/reference/IT_GENERAL_ADVISOR_TEST_PERSONA.md | §16.3の無条件GitHub更新取得 | 3.1 / Draft | 6730 |
| personas/reference/IT_EDUCATION_CONTENT_DESIGNER.md | 冒頭G固定・§11のGitHub初期化 | 0.3（提案） / Draft | 8084 |
| personas/reference/PERSONA_SETUP_ADVISOR.md | 冒頭G固定・§5/6/10のG前提 | 3.1（提案） / Draft | 4516 |
| personas/reference/EMPLOYMENT_SUPPORT_ADVISOR.md | 衝突なし。本文を維持 | 0.3 / Draft | 6320 |
| personas/education/GEM_CODE_GENERATOR.md | 衝突なし。本文を維持 | 2.3 / Approved | 7788 |
| personas/education/GEM_RESEARCHER_DEVELOPMENT.md | 衝突なし。本文を維持 | 1.1 / Approved | 4243 |
| personas/education/GEM_RESEARCHER_FULL.md | 衝突なし。本文を維持 | 1.1 / Approved | 5063 |
| personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md | 衝突なし。本文を維持 | 1.1 / Approved | 4846 |
| personas/education/GEM_REVIEWER.md | 衝突なし。本文を維持 | 1.2 / Approved | 4985 |
| personas/education/GEM_SOLUTION_PARTNER.md | 衝突なし。本文を維持 | 1.6 / Approved | 4893 |

- 14件中5件を是正、9件は本文を変更していない。
- 補助点検：SKILLSの6ファイルとArchiveの3ファイルに無条件のGitHub初期化指示は見つからず、原文を保持した。Skillsの登録・自動選択・実動の適合性まで評価したものではない。
- Archive・旧配布案内・過去Decisionは現行Personaとして数えない。研究の反論者Persona解説も、本Repositoryの運用Personaではない。

## 実施した検査

- M-CG §1～10、M-CL §1～14、T-IT-ADVISOR §1～15、S-IECD §1～10：基準commitと文字列一致。
- S-SETUP §1～4・7～9：基準commitと文字列一致。§5・6・10はP/G案内・取得の責務に限って是正。
- 未変更9 Persona、6 Skills、3 Archive：基準commitと一致。
- 既存Decisionの全文と各成果物内の既存Decision & Rationale：保持。
- 現行14 Personaに「適用方式：G」「Advisor自身はG方式」「新規チャットで無条件のGitHub取得」を示す旧指示がないことを確認。
- 改訂5件のDocument Infoと本文内の版・状態表示を照合。
- 配布スクリプトのdry-run：成功。31パスの選択、相対リンク、状態表示、秘密情報検査を通過。
- git diff --check：成功。

## 限界・後工程

- 文字数はUnicodeコードポイント数。設計目標7,500文字を超えるものがあるが、無断で短縮しない。特定サービスの登録可否・入力上限への適合は未確認。
- G取得の実機失敗原因は未特定。今回の文書修正を原因特定や実動検証PASSとは扱わない。
- 元のMac実機側の同期、GitHubへの反映、実配布はこの点検の成功に含めない。
