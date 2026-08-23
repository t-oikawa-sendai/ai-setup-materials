<!-- Document Info（文書情報） -->
| Item（項目） | Value（値） |
|---|---|
| Document ID（文書ID） | STD-PERSONA-REFERENCE-INDEX-001 |
| Version（バージョン） | 1.0 |
| Status（ステータス） | Approved |
| Created Date（作成日） | 2026-08-22 |
| Last Updated（最終更新日） | 2026-08-23 |
| Owner（管理者） | t-oikawa-sendai |
| Related Documents（関連文書） | [`../../README.md`](../../README.md)<br>[`../education/README.md`](../education/README.md)<br>[`CHATGPT_PERSONA.md`](CHATGPT_PERSONA.md)<br>[`CLAUDE_PERSONA.md`](CLAUDE_PERSONA.md)<br>[`CURSOR_PERSONA.md`](CURSOR_PERSONA.md)<br>[`GEMINI_PERSONA.md`](GEMINI_PERSONA.md) |

---

# Reference Personas（参考用Persona）

## 1. Purpose（目的）

このディレクトリは、Education用4Gem＋1とは異なる前提で、実務構成の参考Personaを管理します。現在利用可能なReference文書への入口・索引です。

## 2. Difference from Education 4Gem＋1（Education用4Gem＋1との違い）

Reference Personaは、Education用4Gem＋1と次の点が異なります。

- 役割
- 利用サービス
- 実装・検証方法の前提

Education用4Gem＋1の現行手順として、そのまま流用しないでください。設計思想や運用パターンの参考として扱ってください。

## 3. Current Reference Personas（現行Reference Persona）

現在利用可能なReference文書は次のとおりです。承認された文書が追加された場合は、この索引を更新します。

- [`CHATGPT_PERSONA.md`](CHATGPT_PERSONA.md)：ChatGPT Responsibility Definition（ChatGPT向け責務定義）
- [`CLAUDE_PERSONA.md`](CLAUDE_PERSONA.md)：Claude Persona（Claudeペルソナ）
- [`CURSOR_PERSONA.md`](CURSOR_PERSONA.md)：Cursor Persona（Cursorペルソナ）
- [`GEMINI_PERSONA.md`](GEMINI_PERSONA.md)：Gemini Persona（Geminiペルソナ）

## 4. Usage Notes（利用上の注意）

- Education領域の現行手順、Gem操作、User-firstフローは [`../education/README.md`](../education/README.md) を正とします。
- 本ディレクトリの文書は参考資料であり、Education用4Gem＋1の代替ではありません。

## 5. Navigation（導線）

- Repository全体の入口：[`../../README.md`](../../README.md)
- Education領域の入口：[`../education/README.md`](../education/README.md)

## Decision & Rationale（決定・判断理由）

### 2026-08-23

#### Education用4Gem＋1との対比表現

Decision:
Reference領域からEducationの現行Gemini構成を指す場合は `Education用4Gem＋1` と表記する。基本4Gemそのものの役割定義を変更するものではない。

Reason:
Gemini上では基本4Gemに `Researcher Deep Research` を追加して運用することが現行仕様であり、Reference入口だけ旧 `Education用4Gem` 表記を残すと、配布構成の実体数を誤解させるため。