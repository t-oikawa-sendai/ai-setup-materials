# Core Persona SSOT Verification（中核4種PersonaのSSOT検証記録）

Date: 2026-09-29
Status: VERIFIED DOCUMENT CHANGES / RUNTIME UNVERIFIED

## 1. Scope and Baseline（対象と監査基準）

本記録は、2026-09-29に設計担当が実ファイル・Git差分・GitHub保存内容を独立照合した結果を、User承認に従って記録担当が今回まとめた内部監査Evidenceである。監査対象は中核4種Reference PersonaのSSOT参照化と、その文書・設定変更の保存結果とする。実機確認は未実施であり、本記録を新しい運用方針やPersona正本の代替として扱わない。

- 対象PR：[solacom_main PR #21](https://github.com/t-oikawa-sendai/solacom_main/pull/21)。User承認によりmainへ反映済み。
- 変更前main：[18f5ed1c06999796f165d121a513afac5d6347a3](https://github.com/t-oikawa-sendai/solacom_main/commit/18f5ed1c06999796f165d121a513afac5d6347a3)。
- レビュー済み候補：[c2fe54408e3767ec99fcfa60380a549c1131d790](https://github.com/t-oikawa-sendai/solacom_main/commit/c2fe54408e3767ec99fcfa60380a549c1131d790)。
- 反映後main／merge commit：[16c44976638b48c53ef16399b1d51217c540be0a](https://github.com/t-oikawa-sendai/solacom_main/commit/16c44976638b48c53ef16399b1d51217c540be0a)。PRの実結果はmerged、headはレビュー済み候補、変更ファイル数は9件。
- SSOT方針を保存した正本commit：[2fcf030f4743c75e3619cf9e8fd04f485745d408](https://github.com/t-oikawa-sendai/ai-setup-materials/commit/2fcf030f4743c75e3619cf9e8fd04f485745d408)。
- main反映後の正本側CURRENT保存commit：[1860db2c8c5313a582a0d97146397811a41f1b66](https://github.com/t-oikawa-sendai/ai-setup-materials/commit/1860db2c8c5313a582a0d97146397811a41f1b66)。[保存済みCURRENT](https://github.com/t-oikawa-sendai/ai-setup-materials/blob/1860db2c8c5313a582a0d97146397811a41f1b66/project-notes/CURRENT.md)にmain反映、元checkoutへの導入未実施、実機未確認を記録している。

既存の正本方針・判断履歴は、[AGENTS.md](https://github.com/t-oikawa-sendai/ai-setup-materials/blob/2fcf030f4743c75e3619cf9e8fd04f485745d408/AGENTS.md)と[Reference README](https://github.com/t-oikawa-sendai/ai-setup-materials/blob/2fcf030f4743c75e3619cf9e8fd04f485745d408/personas/reference/README.md)を参照する。

## 2. Merged Files（反映済み9ファイル）

反映後mainの次の9ファイルは、レビュー済み候補とGit blobが9/9一致した。以下は反映後commitに固定した参照と、照合済みGit blob SHAである。

- [.cursor/rules/00-cursor-persona.mdc](https://github.com/t-oikawa-sendai/solacom_main/blob/16c44976638b48c53ef16399b1d51217c540be0a/.cursor/rules/00-cursor-persona.mdc)：`54eabff29a604381a6a5bff34b4faebf4c2b8340`
- [.cursorrules](https://github.com/t-oikawa-sendai/solacom_main/blob/16c44976638b48c53ef16399b1d51217c540be0a/.cursorrules)：`25b70b31a72509947526e437afbe7fe7852ab812`
- [.gitignore](https://github.com/t-oikawa-sendai/solacom_main/blob/16c44976638b48c53ef16399b1d51217c540be0a/.gitignore)：`4ca4792def2931658594a381036faac32fd7cf18`
- [CHANGELOG.md](https://github.com/t-oikawa-sendai/solacom_main/blob/16c44976638b48c53ef16399b1d51217c540be0a/CHANGELOG.md)：`f23e24d7a8ecaf73c457f1c16a9c994a6d654607`
- [docs/standards/ai-personas/CHATGPT_PERSONA.md](https://github.com/t-oikawa-sendai/solacom_main/blob/16c44976638b48c53ef16399b1d51217c540be0a/docs/standards/ai-personas/CHATGPT_PERSONA.md)：`68742cbfd4aac650567279a4d1a4315c21dfdd44`
- [docs/standards/ai-personas/CLAUDE_PERSONA.md](https://github.com/t-oikawa-sendai/solacom_main/blob/16c44976638b48c53ef16399b1d51217c540be0a/docs/standards/ai-personas/CLAUDE_PERSONA.md)：`3101396836883bdfae19cdddd119b282c9a939b6`
- [docs/standards/ai-personas/CURSOR_PERSONA.md](https://github.com/t-oikawa-sendai/solacom_main/blob/16c44976638b48c53ef16399b1d51217c540be0a/docs/standards/ai-personas/CURSOR_PERSONA.md)：`3a233250832463f60434286e936d7246db1fee0a`
- [docs/standards/ai-personas/GEMINI_PERSONA.md](https://github.com/t-oikawa-sendai/solacom_main/blob/16c44976638b48c53ef16399b1d51217c540be0a/docs/standards/ai-personas/GEMINI_PERSONA.md)：`2dc05d9b575fa61590cb4d409568d4eed44b4155`
- [docs/standards/ai-personas/README.md](https://github.com/t-oikawa-sendai/solacom_main/blob/16c44976638b48c53ef16399b1d51217c540be0a/docs/standards/ai-personas/README.md)：`cfeb09bae3fe09de6b4c5947f3a784b61e7a8c86`

## 3. Canonical Body Preservation（正本4本文の不変確認）

`ai-setup-materials/personas/reference/` の中核4種本文は変更していない。設計担当はローカル保存内容とGitHub保存内容を照合し、次のSHA-256が移行前後で不変であることを確認した。

- [CHATGPT_PERSONA.md](https://github.com/t-oikawa-sendai/ai-setup-materials/blob/2fcf030f4743c75e3619cf9e8fd04f485745d408/personas/reference/CHATGPT_PERSONA.md)：`5decd4491e5def24bcdefcc26b8dede2ba1449910eb2a11dfa21e933625bd4b4`
- [CLAUDE_PERSONA.md](https://github.com/t-oikawa-sendai/ai-setup-materials/blob/2fcf030f4743c75e3619cf9e8fd04f485745d408/personas/reference/CLAUDE_PERSONA.md)：`7796985d6afb540fb7e3eb187a4a72a7aab5effe8b7a08c8d2a42efdd100a179`
- [CURSOR_PERSONA.md](https://github.com/t-oikawa-sendai/ai-setup-materials/blob/2fcf030f4743c75e3619cf9e8fd04f485745d408/personas/reference/CURSOR_PERSONA.md)：`3594c8892459f6ff19288b5a567cdb150733c6876af3945a897cc028beea210d`
- [GEMINI_PERSONA.md](https://github.com/t-oikawa-sendai/ai-setup-materials/blob/2fcf030f4743c75e3619cf9e8fd04f485745d408/personas/reference/GEMINI_PERSONA.md)：`5a666212b476a2ab48b44364d5d52ba7c275b724f3c1428092175eb6fa52e24f`

## 4. Static Verification（文書・設定の静的検証）

- 4つの参照入口と新規READMEのDocument Info、相対リンクを確認し、旧本文の規則・Role・Code Headersの複製がないことを確認した。
- 個人の実パスを共有ルールへ埋め込まず、`UserName / Author / DevRoot / BackupRoot / TestRoot / PersonaSourceRepository` の6キーと元の環境値を、独立検証環境の `.local-ops/persona-environment.md` に保持した。
- `.gitignore` への追加は `.local-ops/persona-environment.md` の単一パスであり、当該ファイルのignoreを確認した。個人実パス・生の環境値は本記録に含めない。
- Cursorの実行入口では `alwaysApply: true` を保持し、既存Verification追加段落が原文と一字一句一致することを確認した。
- 対象差分の `git diff --check` は成功した。

## 5. Checkout Preservation（元checkoutと正本の保全）

元の `solacom_main` Devcheckoutは既存未commit変更を保持している。設計担当は開始時の指紋と比較し、main反映後もGit状態、HEAD、対象18ファイルの内容、submoduleのHEAD・状態・差分が一致したことを確認した。元checkoutの強制同期、既存変更の破棄・退避・上書きは行っていない。

正本 `ai-setup-materials` は、CURRENT保存時点のHEAD／origin/main／GitHub mainが `1860db2c8c5313a582a0d97146397811a41f1b66` で一致し、作業領域はcleanであった。正本の同期・保存完了と、元 `solacom_main` のローカル導入未実施を区別する。

## 6. Governance and CI Evidence（文書検査とCIのEvidence）

[既存文書validator](https://github.com/t-oikawa-sendai/solacom_main/blob/16c44976638b48c53ef16399b1d51217c540be0a/docs/standards/project-bootstrap/scripts/validate-docs.py)をRepository全体へ適用した。validatorソース自体は変更せず、読み込み時に `repository_root` を監査対象のRepositoryルートへ切り替え、変更前後を同じvalidator・検査条件で比較した。

- 変更前：67文書、PASS 32件、FAIL 35件。
- 変更後：68文書、PASS 37件、FAIL 31件。
- 今回の4参照入口と新規README：5文書すべてPASS（5/5）。
- 今回差分による新規FAIL：0件。既存FAILは31件残存し、Repository全体の検査結果はFAILのままである。

監査時点のGitHub commit statusesとPR workflowの実行記録は各0件であった。これはCI合格のEvidenceではない。

## 7. Runtime Status and Exclusions（実機確認状況と対象外）

- 元 `solacom_main` Devcheckoutへの移行設定導入と、導入先でのローカル環境設定作成・確認は未実施。
- Cursor実機での正本取得、取得した正本パス・commitの確認、環境値解決は未確認。
- 外部AIサービスへの登録は未確認。登録する場合に、その登録内容を別途確認する。
- ignored環境ファイルはGitHub配布に含まれない。導入先での作成・確認手順は、反映済みの[参照入口README](https://github.com/t-oikawa-sendai/solacom_main/blob/16c44976638b48c53ef16399b1d51217c540be0a/docs/standards/ai-personas/README.md)に保持されている。
- Education・Lovable・Copilot、および既存31件の文書FAILは今回の変更対象外。

## 8. Decision & Rationale（決定・判断理由）

### 2026-09-29

#### Internal Audit Record（内部監査記録の保存）

Decision:
Userは「検証結果の要点を1文書にまとめ、`ai-setup-materials/project-notes/` に内部監査記録としてGitHubへ保存する」というASKME推奨を「OK」と承認した。

Reason:
文書変更の検証結果と実機未確認の範囲を、GitHub上で追跡可能な記録として残すため。
