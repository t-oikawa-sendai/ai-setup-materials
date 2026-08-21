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
- この「Researcher本体の責務は維持したまま、検索範囲・対象をModuleで変更し、不要になったModuleを外せること」が、Researcher Personaの他Personaと異なる特徴である。

### Researcher Module 構成方針

- Moduleを複数のKnowledgeファイルとして同時登録する方式は採用しない。
- Researcherは、その時点で必要な本体・Moduleを含む完成済みファイルを1本だけGemへ登録して利用する。
- 複数のResearcher候補ファイルは入替候補であり、Gemへ同時登録するものではない。
- したがって、Gemの実運用上Researcher本体が重複して読み込まれることはない。
- 判断基準は着脱の簡単さより、Gemが必要な指示を確実に参照できることを優先する。
- Moduleを外した場合、その分野を「検索禁止」とするのではなく、Researcherの担当検索範囲から外す。
- Researcher本体には調査方法・品質基準を置き、Moduleには「何について調査するか」という検索対象・範囲を置く。
- Researcher本体に置く内容の例：Evidence、一次情報優先、事実と推論の分離、比較、根拠付き推論、結論提示、未確認事項の明示。
- Moduleごとに調査方法・品質基準を変える設計にはしない。
- Moduleの着脱・構成変更時もResearcher本体の責務・調査方法・品質基準は変更しない。

### Module 正式名称

1. `Learning Module` — 学習関連
2. `Career Module` — 就職活動関連
3. `Development Module` — PFなどの設計・開発関連

### 教材として提供する範囲

- このRepositoryが提供するのは完全な運用サービスではなく学習教材である。
- 教材側で、利用者が将来取り得るすべての状態・組み合わせを網羅する必要はない。
- 「学習は終了したが、まだ就職していない」状態は、教材としてあらかじめ提供するパターンには含めない。
- その状態に対応する `Career Module + Development Module` の組み合わせが必要になった場合は、利用者が学習した内容をもとに自己判断で作成させる。

### Researcher 3完成版ファイル方式

教材として次の3つの完成済みResearcherファイルを提供する方式を正式採用する。

1. `GEM_RESEARCHER_FULL.md`
   - Researcher本体 + `Learning Module` + `Career Module` + `Development Module`
2. `GEM_RESEARCHER_LEARNING_DEVELOPMENT.md`
   - Researcher本体 + `Learning Module` + `Development Module`
3. `GEM_RESEARCHER_DEVELOPMENT.md`
   - Researcher本体 + `Development Module`

- 各ファイルは、それ単体でResearcher Personaとして成立する完全な独立ファイルとする。
- Gemには常に上記のうち必要な1ファイルだけを登録する。
- ユーザーはPersona本文やModule本文を削除・編集して切り替えるのではなく、必要な完成済みファイルへ入れ替えて利用する。
- 3パターンは教材として用意する代表的な構成である。
- どのタイミングでどのファイルへ切り替えるかはユーザーの任意とし、教材側で強制的な切替条件にはしない。
- 代表例としては、訓練中・就職活動中は `FULL`、就職活動支援が不要になった後は `LEARNING_DEVELOPMENT`、学習支援も不要になった後は `DEVELOPMENT` を利用できる。

### Reviewer Persona

- Reviewer Personaは未完成。

---

## Not Yet Confirmed

次の事項は、ユーザーからまだ具体的に確定されていないため、この文書では推論しない。

- 3分野それぞれの詳細な検索対象・検索範囲
- Researcher Persona本文内でのModule配置・記法
- 3つの配布候補ファイルを改訂するときの保守方法
- 旧 `personas/education/GEM_RESEARCHER.md` の最終的な扱い
- Reviewer Personaの未完成部分の具体的内容

これらは既存資料の再監査で確認し、資料だけで一意に決まらない場合のみユーザーへ確認する。
