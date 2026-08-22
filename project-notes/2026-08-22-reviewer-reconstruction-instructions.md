# Reviewer Persona Reconstruction Instructions

Last Updated: 2026-08-22
Status: INVALID / DO NOT IMPLEMENT

## 1. 状態

この文書は、Education用4GemとCursor等のAIサービス別実務向け運用をAIが混同して作成した。

この文書を `GEM_REVIEWER.md` の実装へ使用しない。

## 2. 誤り

- Education用4GemへCursor等の外部実装担当を混入させた。
- 生徒がCode Generatorの生成コードをIDEへコピーし、実行・test・動作確認する前提を見落とした。
- 不明確な質問への回答を、Reviewerの詳細仕様が確定したものとして扱った。
- 確認されていない詳細な戻し先とReviewer責務を実装要件へ含めた。

## 3. 2026-08-22 corrected confirmed premise

- Code Generatorはコード生成までを担当する。
- 生徒は、Code Generatorが生成したコードをVS Code等のIDEへコピーする。
- 生徒は、IDEへ反映したコードの実行、test、動作確認を行い、その検証Evidenceを作成する。
- Reviewerは、Code Generatorが生成したコードと、生徒が作成した検証Evidenceを評価する。
- 最終判断は生徒が行う。
- CursorはEducation用4Gemのこの運用には含めない。
- Cursorが実装・testを担当するAIサービス別の実務向け運用と、Education用4Gemを混同しない。

## 4. 現在地点

- `personas/education/GEM_REVIEWER.md` は未変更である。
- Reviewer Personaの再構築仕様と実装は未完成である。
- この文書の旧内容から実装を開始しない。
- 確認済み事実と推論を分離して既存資料を再確認し、確認済み事項だけで新しい実装指示書を作成する。
