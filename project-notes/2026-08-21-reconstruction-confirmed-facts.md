# Reconstruction Confirmed Facts

Last Updated: 2026-08-21
Status: RECOVERY / USER-CONFIRMED

## Purpose

AIによる誤統合で毀損したEducation用4Gemの情報資産を再構築するため、ユーザーが明示的に再確認した最新事項を小刻みに記録する。

この文書には、ユーザーが明示した事項のみを記載する。AIによる推論・補完は加えない。

---

## 2026-08-21 Confirmed Facts

### Researcher Persona

- Researcher Personaは未完成。
- Researcher本体の責務自体はModule導入によって変更しない。
- Moduleで変更するのはResearcherの検索範囲・検索対象である。
- 検索対象は大きく次の3分野に分ける。
  1. 学習関連
  2. 就職活動関連
  3. PFなどの設計・開発関連
- これら3分野は訓練期間中には有効だが、将来すべてが常に必要とは限らない。
- 学習終了後は「学習関連」が不要になる。
- 就職決定後は「就職活動関連」が不要になる。
- 不要になったModuleをResearcherから外せる構成にする。
- Moduleを外す方法は、できる限り簡単な方法を採用することを重視する。
- この「Researcher本体の責務は維持したまま、検索範囲・対象をModuleで変更し、不要になったModuleを外せること」が、Researcher Personaの他Personaと異なる特徴である。

### Researcher Module 構成方針

- Moduleを複数のKnowledgeファイルへ分割する方式は採用しない。
- Researcher Personaは1本のファイル内に本体とModuleを持たせる方向とする。
- 判断基準は着脱の簡単さより、Gemが必要な指示を確実に参照できることを優先する。
- Google Geminiの公式ヘルプではGemへ複数Knowledgeファイルを追加できることは確認できるが、毎回すべてのKnowledgeファイルが必ず同じ強さで参照されることまでは保証されていない。このため、安全側として1ファイル構成を採用する。
- 訓練期間中は3Moduleを同時に有効にすることを基本とする。
- Moduleを外した場合、その分野を「検索禁止」とするのではなく、Researcherの担当検索範囲から外す。
- Researcher本体には調査方法・品質基準を置き、Moduleには「何について調査するか」という検索対象・範囲を置く。
- Researcher本体に置く内容の例：Evidence、一次情報優先、事実と推論の分離、比較、根拠付き推論、結論提示、未確認事項の明示。
- Moduleごとに調査方法・品質基準を変える設計にはしない。
- Moduleの着脱・構成変更時もResearcher本体の責務・調査方法・品質基準は変更しない。

### Module 正式名称

1. `Learning Module` — 学習関連
2. `Career Module` — 就職活動関連
3. `Development Module` — PFなどの設計・開発関連

### Reviewer Persona

- Reviewer Personaは未完成。

---

## Not Yet Confirmed

次の事項は、ユーザーからまだ具体的に確定されていないため、この文書では推論しない。

- 1ファイル内で不要Moduleを外す具体的な操作方法
- 3分野それぞれの詳細な検索対象・検索範囲
- Researcher Persona本文内でのModule配置・記法
- Reviewer Personaの未完成部分の具体的内容

これらは既存資料の再監査で確認し、資料だけで一意に決まらない場合のみユーザーへ確認する。
