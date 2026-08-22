# Reviewer User-First Learning Design

Last Updated: 2026-08-22
Status: CONFIRMED DECISION RECORD

## Purpose

Education用Reviewerが、なぜレビュー結果を単純にCode Generatorへ戻す設計ではなく、Userの理解・判断・学習を中心に置く設計になったのかを記録する。

この記録は、将来このReviewerの構成に疑問が生じたときに判断理由を確認できるようにするためのものである。また、利用者が独自のAI Personaを作成するときに、役割分担だけでなく、利用者の学習機会、判断権、出力の読者、AI間の受け渡しをどのように設計するかを考えるための教材として使用できる形にする。

## Context Before This Decision

Reviewer再構築では、次が先にユーザー確認済みであった。

- `User` はEducation用4Gemを操作する利用者である。
- Code Generatorはコード生成を担当する。
- Userは生成コードをIDEへ反映し、実行、test、動作確認を行い、検証Evidenceを作成する。
- ReviewerはCode Generatorが生成したコード、Userが作成した検証Evidence、Solution Partnerの設計成果物を評価する。
- Researcherの調査結果はReviewerの評価対象に含めない。
- Reviewerは自ら修正せず、問題、根拠、影響、戻し先、修正要求、再確認条件を示す。
- 最終判断はUserが行う。

一方、コードレベルの問題を確認した場合に、Reviewerの指摘を誰が最初に受け取り、UserとCode Generatorのどちらが修正するかは十分に整理されていなかった。

## Decision History

### 1. Initial routing proposal

AIは当初、Reviewerの戻し先を次の3分類として提案した。

1. 要求・要件・設計の問題はSolution Partnerへ戻す。
2. 生成コード、コード解析、コードレベルの修正はCode Generatorへ戻す。
3. IDEへの反映、実行、test、動作確認、検証Evidenceの不足はUserへ戻す。

この分類を説明する際、AIは「Userをコード修正担当にはしない」と付け加えた。

### 2. User correction

ユーザーは、「Userをコード修正担当にはしない」という前提を決めつけてはならないと訂正した。

理由は次のとおりである。

- 生徒が自分でコードを修正する場合がある。
- 学習面では、生徒が自分で修正することが望ましい場合がある。
- レビューはCode Generatorだけに向けた指示ではなく、学習途中の生徒にも理解できる表現である必要がある。

これにより、「コードの問題だからCode Generatorへ直接戻す」という固定分岐では、Userの学習機会と判断権を失わせることが確認された。

### 3. User-first flow proposed by the user

ユーザーは、Code Generatorへ戻す基準に該当するコードレベルの指摘についても、次の流れを提案した。

1. Reviewerのレビュー結果を、まずUserが読む。
2. Userが、自分で修正できそうか判断する。
3. 自分でできそうな場合、Userが手作業でコードを修正する。
4. 自分では難しいと判断した場合、Userがレビュー内容をCode Generatorへコピーしてコード生成・修正支援を依頼する。
5. どちらの方法を選んだ場合も、UserがコードをIDEへ反映する。
6. Userが実行、test、動作確認を行い、検証Evidenceを作成する。
7. Userが修正結果と検証EvidenceをReviewerへ再提出する。

この流れでは、ReviewerからCode Generatorへ自動的・直接的に作業を移さない。レビュー結果の最初の受領者、修正方法の判断者、検証者、再提出者はUserである。

### 4. Review document feasibility

上記のUser-firstフローは、1つのレビュー文書で実現可能と判断した。

レビュー文書は、Userが問題を理解し、自力修正とCode Generator利用のどちらにも使える必要がある。そのため、コードレベルの各指摘は、少なくとも次の情報を持つ。

- 指摘ID
- 対象
- User向けの問題説明
- 問題のEvidence
- 影響
- 修正後に満たす条件
- Userが自分で修正する場合の着眼点
- Code Generatorを利用する場合に渡せる情報
- 修正後の確認手順
- Reviewerへ再提出するもの

Code Generatorへ渡す情報は、対象、問題、Evidence、現在有効な要求・設計、修正後に満たす条件、変更してはいけない範囲を含められる形にする。

専門用語を禁止するのではなく、学習途中のUserが次に何をすればよいか理解できる説明を添える。技術的なEvidenceと、User向けの説明を両立させる。

### 5. Question about prohibiting corrected code

次に、Reviewerによる修正コードの提示を完全に禁止すべきかが検討された。

完全禁止には、ReviewerとCode Generatorの責務境界を明確にし、Userが完成コードを受け取るだけになることを防ぐ利点がある。一方で、次の場合には修正案や小さなコード例がUserの理解を助ける。

- 複数の修正方法を比較する場合
- 修正前後の考え方の違いを説明する場合
- 抽象的な説明だけでは問題箇所を理解しにくい場合
- Userが自力修正できるか判断する材料を示す場合

したがって、コードそのものを一律禁止するのではなく、「完成実装の代行」と「学習・比較のための説明」を分離する方針を検討した。

### 6. Confirmed boundary

ユーザーは、次の境界に問題がないことを確認した。

- Reviewerは完成実装を代行しない。
- Reviewerは、問題と修正方法をUserが理解・比較できるよう、複数の修正案を提示できる。
- 各修正案について、利点、欠点、影響、適する条件を説明できる。
- 疑似コードを提示できる。
- 問題点や修正方針を説明するために必要な、最小限のコード例を提示できる。
- Reviewerが提示するコード例は、完成コード、適用済みコード、動作保証済みコードとして扱わない。
- ファイル全体の完成版コード、そのまま適用することを前提とした大規模な修正コード、複数ファイルにまたがる完成パッチはReviewerの担当にしない。
- 完成した修正版コードが必要な場合は、Userが自ら作成するか、UserがCode Generatorを利用する。
- 現行設計の範囲内で選べるコードレベルの案はReviewerが比較できる。
- 採用案によって要求、設計、責務が変わる場合、Reviewerは決定せず、Solution Partnerでの再検討が必要であることを示す。
- 最終的な修正方法の選択、IDEへの反映、実行、test、動作確認、検証Evidence作成、Reviewerへの再提出はUserが行う。

## Confirmed Current Design

### Review recipient and decision flow

- Reviewerのレビュー結果は、まずUserへ返す。
- Reviewerがコードレベルの問題を確認しても、Code Generatorを修正実施者として固定しない。
- Userはレビュー内容を読み、自分で修正するか、Code Generatorを利用するかを判断する。
- User自身によるコード修正を許可する。学習面ではUser自身による修正が望ましい場合がある。
- Code Generatorを利用する場合も、Userがレビュー内容を渡し、生成結果を受け取り、IDEへ反映し、検証する。
- どちらの修正方法でも、Reviewerへ再提出するときの再確認条件は同じである。

### Meaning of destination

従来の「戻し先」は、ReviewerがUserを経由せず別のGemへ直接作業を送ることを意味しない。

レビュー結果では、次を区別する必要がある。

- レビュー結果の受領者：User
- 問題が存在する工程または対応が必要な工程
- 利用可能な支援先：Solution PartnerまたはCode Generator
- 修正方法の判断者：User
- 修正・検証結果の再提出者：User

コードレベルの指摘については、`戻し先: Code Generator` だけで終わらせず、Userが自力修正とCode Generator利用を判断できる情報を示す。

### Output language

- レビューはCode Generatorだけを読者として書かない。
- 学習途中のUserが問題、影響、修正条件、次の作業を理解できる表現にする。
- 技術的な正確さを失わせる過度な単純化は行わない。
- 専門用語を使用する場合は、必要に応じて意味または具体的な作業との関係を説明する。
- User向けの説明と、Code Generatorへ渡せる技術情報を同じレビュー文書内で両立させる。

### Reviewer and code boundary

Reviewerは完成実装を代行しない。ただし、Userの理解・比較・自力修正の判断を支援するための複数案、疑似コード、必要最小限の説明用コード例は提示できる。

この境界の目的は、Reviewerを単なる合否判定役や、反対に完成コード生成役へ偏らせず、Userが問題を理解し、自分で次の行動を選択できるレビューを実現することである。

### Confirmed fields for implementation findings

実装に修正が必要な指摘では、従来の `戻し先: Code Generator` だけを表示する形式を使用しない。次の3項目を表示する。

```text
対応が必要な工程：実装
利用可能な支援先：Code Generator
Userの対応：自力でコード修正、もしくはCode Generatorに修正指示
```

`対応が必要な工程：実装` は、コードの内容、構造、処理に修正が必要であることを示す。Code GeneratorがIDEへの反映や実環境での実装を行うという意味ではない。

`Userの対応` は、Userの判断だけでなく、選択後に行う作業も示す項目である。

### Confirmed summary heading

Reviewer出力の冒頭一覧の正式名称は `対応方針一覧` とする。旧名称の `戻し先一覧` は使用しない。

`対応方針一覧` では、各指摘IDに対して、少なくとも次を対応付ける。

- 対応が必要な工程
- 利用可能な支援先
- Userの対応

これにより、Userは詳細な各指摘を読む前に、問題がある工程、利用できる支援、User自身が行う対応を一覧で確認できる。

### Required dual-use content for implementation findings

実装に関するすべての修正必須指摘には、レビューが長くなっても、次の両方を含める。簡潔さより学習目的を優先する。

#### User向け説明

- 何が問題か
- なぜ修正が必要か
- Userが自力修正する場合の着眼点
- 修正後に確認すること

#### Code Generatorへの修正指示

- 対象
- 問題
- Evidence
- 修正後に満たす条件
- 変更してはいけない範囲

`Code Generatorへの修正指示` は、Userが自力修正を選択できないと判断した場合に、そのままコピーしてCode Generatorへ渡せる形にする。

この2つは選択式でどちらか一方を出すものではない。Userがレビューを読んだ時点で、自力修正とCode Generator利用のどちらでも次へ進めるよう、同じレビュー文書内に両方を用意する。

## Why This Design Was Chosen

### Preserve learning opportunities

コードの問題をすべてCode Generatorへ送ると、生徒が自分で原因を理解し、修正する機会を失う。Userが最初にレビューを読み、修正方法を選択することで、自力修正の学習機会を残す。

### Preserve User judgment

同じ指摘でも、Userの知識、経験、学習目的、時間によって、自分で修正するかAIを利用するかは変わる。Reviewerが一律に決めず、判断材料を示してUserに選択を残す。

### Keep Persona responsibilities distinct

Reviewerは問題、Evidence、影響、修正条件、選択肢を示す。Code Generatorは必要に応じて完成コードを生成する。Userは選択、適用、検証、再提出を行う。この分離により、各Personaの責務を維持する。

### Make one review useful in both paths

レビュー文書にUser向け説明、技術的Evidence、修正条件、Code Generatorへ渡せる情報を含めれば、Userが自力修正する場合とCode Generatorを利用する場合で別のレビューを作る必要がない。

レビューが長くなることよりも、Userが問題を理解して修正方法を選択できることを優先する。Code Generatorへ渡せる修正指示を最初から含めることで、Userが自力修正は難しいと判断した後に、別の指示書を作り直す必要もなくす。

### Support future Persona design

Persona設計では、AIの役割名や機能だけでなく、最初の読者、判断者、作業実施者、検証者、再提出者を分けて考える必要がある。この経緯は、利用者が将来自分の目的に合わせてPersonaを作成・調整するときの判断例となる。

## Superseded Interpretation

次の解釈は現行仕様として使用しない。

- Userはコードを修正しない。
- コードレベルの指摘は常にCode Generatorが修正する。
- Reviewerのレビュー結果はUserの判断を経ず、Code Generatorへ直接戻す。
- Reviewerはコード例を一切提示してはならない。
- Reviewerが完成修正版コードを生成して修正を完了する。

## Unresolved Implementation Details

次はReviewer Persona本文または新しい実装指示書を作成する工程で、既存の確定事項と整合させて決める。

- `対応が必要な工程`、`利用可能な支援先`、`Userの対応` を、設計・検証・Evidence不足の指摘へ展開するときの具体的な値と表現。
- 説明用コード例を「必要最小限」と判断するためのPersona本文上の表現。
- 複数の修正案を提示すべき条件と、省略してよい条件の最終表現。

これらは本文表現の未確定事項であり、本記録のCONFIRMED事項を変更してはならない。
