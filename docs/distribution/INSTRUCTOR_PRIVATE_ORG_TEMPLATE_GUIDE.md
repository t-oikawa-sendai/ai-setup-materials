# 講師用｜GitHub Free OrganizationのPrivate Templateで教材を配布する手順書

- 改訂日：2026-10-29
- 用途：講師が管理する正本から教材を配布し、生徒ごとに許可した教材だけを閲覧できるようにする
- 費用：GitHub Freeの個人アカウントとOrganizationを使用
- 生徒の操作：教材への招待を承諾し、共通の入口から教材を閲覧する。個人Private Repositoryへのコピーは生徒が自由に選べる任意の作業
- 日常の招待操作は第7章。第1〜6章は配布構成・更新・管理の説明
- この手順書は運用手順と確認済みの構成を記す。生徒の招待・個人Repositoryの作成・利用成功は、実施するまで完了扱いにしない
- 手順書の管理場所：講師用正本の `docs/distribution/`。同ディレクトリの2冊を編集正本とし、Downloads版はコピーとして扱う。生徒用手順書だけを配布対象とし、講師用手順書は配布しない

## 1. 現在の構成

```text
講師が管理する教材の正本
t-oikawa-sendai/ai-setup-materials の main
  │ mainへのPush、またはGitHub Actionsの手動起動
  ▼
選定した30パスだけを一方向に同期
OSLIB21-materials/ai-setup-materials-student
  ├── GitHub Free Organization所有
  ├── Private・Template repository
  └── 招待され、Read権限を持つ生徒が閲覧
        │ Use this template（生徒の任意）
        ▼
各生徒の個人アカウントに作るPrivate Repository
```

配布先：[OSLIB21-materials/ai-setup-materials-student](https://github.com/OSLIB21-materials/ai-setup-materials-student)

生徒共通の入口：[https://github.com/t-oikawa-sendai](https://github.com/t-oikawa-sendai)

入口のプロフィールページは公開されています。限定公開教材の本文は、各Private Repositoryの権限で制限します。生徒は教材ごとの **外部コラボレーター**（組織メンバーにならず、指定Repositoryに参加する人）として **Read** で招待します。招待時に講師側の許可が済み、生徒が承諾すると、その教材を閲覧できます。追加の講師承認はありません。

**教材の正本は講師用Repositoryの `main` です。** 生徒向けTemplateは選定ファイルの配布コピーです。各生徒がTemplateから作るRepositoryはさらに独立したコピーです。GitHub Actionsは生徒の個人Repositoryを操作しません。

**講師がPersonaを更新しても、生徒が個人Repositoryに作成したコピーには自動反映されません。最新のPersonaを使う場合は、教材の入口から最新の配布教材を開き、該当するPersonaを改めて取得して、自分のコピーを更新する必要があります。Persona以外の教材も同様です。**

**今回の30パス版の構成**：2冊を講師用正本の `docs/distribution/` で管理し、生徒用 `STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md` だけを同期します。従来31パスから `PERSONA_SETUP_ADVISOR.md` を除外した30パスです。配布先用に生成するRoot READMEには生徒用手順書へのリンクを付け、S-SETUPの案内を除きます。正本のREADME・Persona本文は変更しません。講師用手順書は同期対象外で、自動削除の許可範囲も旧9パスのままです。同期対象から外した既存ファイルの扱いは第8章、過去の配布記録は第6章を参照してください。

講師用Repositoryは、**2026-10-29のGitHubメタデータ確認時点でPublic**です。講師用RepositoryのPrivate化は別操作で、この手順書の改訂では実施していません。Private化前は内部文書を含む講師用Repositoryを誰でも閲覧できます。Private化を実施した事実は、GitHubの表示で別途確認してください。

## 2. 構築済みの設定と未実施の授業準備

| 項目 | 現在の扱い |
|---|---|
| Organization | `OSLIB21-materials`、GitHub Freeで作成済み |
| 配布先 | `ai-setup-materials-student`。2026-10-29のGitHubメタデータでPrivate・Templateを確認。改訂開始時の `main` は `61870641fa0e4c19be042db5fd9ad7b517b01da6`。過去の同期記録は第6章 |
| 同期 | 講師用 `main` へのPushと、GitHub Actionsの手動起動に対応 |
| 配布範囲 | 今回の改訂で追加・上書き対象を30パスへ変更。従来31パスからS-SETUPを除外し、生徒用手順書は含む。自動削除は当初の9パスのみ。改訂のGitHub反映は別途確認 |
| 認証情報 | 講師用RepositoryのActions用Repository Secret `STUDENT_TEMPLATE_TOKEN` に登録済み。値は手順書に書かない |
| Organizationの基本権限 | 2026-10-29に `OSLIB21-materials` の **Base permissions = No permission** への反映を画面で確認 |
| 教材別のアクセス制限テスト | 2026-10-29、テストアカウントでAI活用を閲覧でき、設計文書は404になることをUserが確認し、合格と判定 |
| 実生徒の招待とRead権限 | 2026-10-29時点で未実施。テスト合格後、第7章の手順で開始する |
| 生徒の個人Repository | 作成は生徒の任意。講師から指示する作業ではなく、講師側で作成・変更・自動更新しない |

初回の9パス配布、その後の30パスへの拡張、S-SETUPの個人URL欄への改訂、および生徒用手順書を加えた31パス版は、それぞれGitHub Actionsで成功を確認済みです。実測した実行URLとHEAD、確認できていない事項は§6に記録します。

## 3. 何を配るか

この版の同期処理は、講師用Repositoryの [`scripts/sync_student_template.py`](https://github.com/t-oikawa-sendai/ai-setup-materials/blob/main/scripts/sync_student_template.py) にある30パスの許可リストを使います。選ばれたパスだけを配布先の同じ位置へ追加・上書きします。正本側で消えたときに配布先から自動削除できるのは、最初に承認された9パスだけです。残る21パス（生徒用手順書を含む）が正本から消えた場合は、勝手に削除せず同期を停止します。

| 配布するもの | パス数 | 扱い |
|---|---:|---|
| ルート `README.md` と `LICENSE` | 2 | READMEは配布先用の案内に調整。LICENSEは原文のまま |
| `personas/` 直下の文書4件と図1件 | 5 | 選定した設計説明・Evidence・共通仕様など |
| `personas/education/` | 14 | README、GEM 6件、SKILLS 6件、旧資料1件 |
| `personas/reference/` | 8 | README、Persona、運用参考資料。S-SETUPは同期対象外 |
| `docs/distribution/STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md` | 1 | 生徒用手順書。Root READMEの配布コピーから案内 |

従来31パスからS-SETUPの1件を除外します。講師用手順書は配布しません。

Root README、Education README、Reference README、`WHY_PERSONA_MATTERS.md`、`PERSONA_IDENTIFICATION_AND_SETUP.md` の**配布コピーだけ**は、配布しない資料へのリンクや案内を調整します。Root READMEに生徒用手順書へのリンクを付け、Root READMEとReference READMEからS-SETUPの利用案内・リンクを除きます。これらの講師用正本本文は変更しません。それ以外の選定ファイルは原文のままです。Draft、Approved、Deprecatedの表示を配布時に昇格・偽装しません。選定した通常文書のDraftとApprovedの間の変更は同期を続けますが、その他の状態変化や不正なStatusは停止します。

`AGENTS.md`、`project-notes/`、`docs/` 内の選定外ファイル（講師用手順書を含む）、選定外のPersonaの本文、秘密情報は配布しません。選定文書中に内部文書の**ファイル名だけ**を記したコメントが残る場合がありますが、内部文書の本文は配布しません。配布先の許可リスト外のファイル、他branch、過去の履歴は書き換えず、force pushは使いません。

### 今回の同期対象30パスの一覧

```text
README.md
LICENSE
docs/distribution/STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md
personas/WHY_PERSONA_MATTERS.md
personas/AI_ISSUES_EVIDENCE.md
personas/SYCOPHANCY_CHALLENGER_PERSONAS.md
personas/assets/sycophancy_frontier_models_2026.png
personas/PERSONA_IDENTIFICATION_AND_SETUP.md
personas/education/README.md
personas/education/GEM_CODE_GENERATOR.md
personas/education/GEM_RESEARCHER_DEVELOPMENT.md
personas/education/GEM_RESEARCHER_FULL.md
personas/education/GEM_RESEARCHER_LEARNING_DEVELOPMENT.md
personas/education/GEM_REVIEWER.md
personas/education/GEM_SOLUTION_PARTNER.md
personas/education/SKILLS/CODE_GENERATOR.md
personas/education/SKILLS/RESEARCHER_CAREER.md
personas/education/SKILLS/RESEARCHER_DEVELOPMENT.md
personas/education/SKILLS/RESEARCHER_LEARNING.md
personas/education/SKILLS/REVIEWER.md
personas/education/SKILLS/SOLUTION_PARTNER.md
personas/education/archive/GEMINI_PERSONA_DEFINITION-4Gem.md
personas/reference/README.md
personas/reference/CHATGPT_PERSONA.md
personas/reference/CLAUDE_PERSONA.md
personas/reference/CURSOR_PERSONA.md
personas/reference/GEMINI_PERSONA.md
personas/reference/PERSONA_OPERATION_CASE_STUDY.md
personas/reference/PERSONA_PROMPT_TEMPLATE.md
personas/reference/CHAT_HANDOFF_TEMPLATE.md
```

この一覧は現在の決定を読むための写しです。将来の変更は講師用 `main` の許可リストと判断記録を確認してください。新しいファイルを `personas/` に置いただけでは、自動で配布対象になりません。

今回の30パスは、生徒用手順書を含みS-SETUPを含みません。第6章の2026-10-22時点の旧30パスとは内訳が異なります。

## 4. 教材を更新するとき

1. 講師用Repositoryの `main` を正本として教材を編集します。既存の `AGENTS.md` と判断記録に従い、変更前の状態と差分を確認します。
2. 配布範囲を変えたい場合は、追加・削除する**具体的なパス**を決め、許可リストと判断記録を更新します。新しいパスを正本から消したときの扱いも個別に決めます。
3. 必要なレビューと明示承認を経て、講師用 `main` へ通常のCommit・Pushを行います。force pushは使いません。
4. PushによりGitHub Actionsの **Sync selected student materials** が起動します。講師用Repositoryの **Actions** タブで実行結果を開き、`success` と各stepの結果を確認します。
5. 配布先の `main` を開き、Private・Templateの設定、この版の許可リストに対応する30パス、変更した本文、新しい対象外ファイルが追加されていないことを確認します。既存の対象外ファイルは保持するため、配布先全体のファイル数が必ず30件になるわけではありません。Actionsが成功しただけで内容一致と判断しません。

手動で再実行する場合は、講師用Repositoryの **Actions → Sync selected student materials → Run workflow** で `main` を選びます。変更がなければ新しいCommitを作らず正常終了します。手動起動には講師用Repositoryへの適切な権限が必要です。

同期が停止した場合は、Actionsの失敗したstepを確認します。選定ファイルの欠落、不正なStatus、新しい選外リンク、配布先の未整理変更、認証情報の期限切れなどを調べます。失敗を回避するために許可リストを無条件に広げたり、配布先をforce pushで上書きしたりしません。

## 5. 認証情報を維持する

講師用Repositoryの **Settings → Secrets and variables → Actions → Repository secrets** に、`STUDENT_TEMPLATE_TOKEN` を置きます。これは配布先Repositoryへ書き込むための鍵です。Organization用Secretや配布先のSecretではありません。GitHub FreeのPrivate RepositoryではOrganization-level Secretを使えないため、講師用RepositoryのRepository Secretとして管理します。

現在のFine-grained PATは、Resource ownerを `OSLIB21-materials`、対象を `ai-setup-materials-student` だけ、Repository permissionsを `Contents: Read and write` とし、Metadataは既定のReadです。期限前に更新し、Organizationの承認要件がある場合は承認状態を確認します。発行値を会話、教材、Commit、画面共有やログへ載せないでください。値を再発行した場合は同じSecret名に新しい値を登録し、Actionsで同期を再確認します。

## 6. 配布結果の確認記録

次の項目を**実際に確認したときだけ**記入します。確認中・未実施はそのまま区別します。

| 確認項目 | 記録する内容 |
|---|---|
| 講師用GitHub `main` | 確認日時、HEAD、対象のCommit |
| Actions | 実行URL、結果、失敗stepの有無 |
| 配布先GitHub `main` | HEAD、実行時の許可リストのパス数、欠落・余剰・内容不一致の有無 |
| Visibility / Template | Private表示とTemplate repository設定の確認結果 |
| S-SETUPの同期除外 | 追加・更新対象に含まれず、配布版READMEの利用案内・リンクがないこと。既存ファイルの残存と同期対象を区別する |
| 生徒の利用 | 招待・承諾、許可教材の本文閲覧、未許可教材の閲覧不可を確認。個人Repositoryの作成・利用は生徒の任意であり、閲覧テストの合格条件にしない |

**配布内容の実測（2026-10-22）**：S-SETUP配布コピーを改訂した講師用GitHub `main`、ローカルHEAD、`origin/main` は `defbc2a4bc675196409fe257b392227ab6f824c4` で一致しました。[Push起動のActions実行 39777787027](https://github.com/t-oikawa-sendai/ai-setup-materials/actions/runs/39777787027) は `success` で、同期jobの全stepも成功しました。配布先のPrivate Repositoryを取得して確認した `main` のHEADは `547d018dd66f815c9d3472a8bbd98cd63c7604c0` です。trackedファイルは選定30パスと完全に一致し、正本からの配布変換後の内容と、欠落・余剰・byte不一致がありませんでした。直前の配布先HEAD `c20a3ccb656ddb9157bc0b1b7126f66704f6b9e4` は履歴上の祖先として残っています。配布先checkoutはcleanでした。

**後続の変更なし同期（同日）**：`project-notes/CURRENT.md` の確認記録だけをnoreply Git identityでCommitし、講師用 `main` へforce pushを使わず通常Pushしました。講師用GitHub `main`、ローカルHEAD、`origin/main` は `edf7780908fd996b1e7441c21af9b91623cd7fbd` で一致しました。[Actions実行 39778533319](https://github.com/t-oikawa-sendai/ai-setup-materials/actions/runs/39778533319) は `success` で、同期jobの各stepも成功し、ログに `No managed changes to publish.` と表示されました。配布先のリモート `main` は `547d018dd66f815c9d3472a8bbd98cd63c7604c0` のままで、新しいCommitは作られていません。この後続実行を、上記30パスの内容照合の代わりにはしません。

30パス版のPush後、認証済みChromeの配布先画面で `Private template`、`Use this template`、当時の最新Commit `547d018dd66f815c9d3472a8bbd98cd63c7604c0` を再確認しました。講師用正本のGitHubメタデータは引き続きPublicです。生徒の実アカウントでの招待・テンプレート利用・S-SETUPの取得は未確認です。

**31パス版の実測（2026-10-22）**：講師用GitHub `main` の配布変更Commitは `7a3f93780f79f060c28d8e7599a8a4827d7db0fa` です。[Push起動のActions実行 39784304065](https://github.com/t-oikawa-sendai/ai-setup-materials/actions/runs/39784304065) は `completed/success` で、同期jobと全stepが成功しました。配布先Private Repositoryの `main` は `d884959264795d1b82f3bde74dab1e91f87959eb` です。SSHで取得したcleanな配布先のtrackedファイルは許可リスト31パスと完全に一致し、配布変換をdry-runで照合した31/31パスの内容もbyte単位で一致しました。前回の配布先HEAD `547d018dd66f815c9d3472a8bbd98cd63c7604c0` から変わったのはRoot READMEと生徒用手順書の2パスだけで、旧HEADは履歴上の祖先です。認証済みGitHub画面でも `Private template`、`Use this template`、最新Commit `d884959264795d1b82f3bde74dab1e91f87959eb`、Root READMEから生徒用手順書へのリンクを再確認しました。講師用正本は引き続きPublicです。生徒本人の招待・テンプレート利用・個人Repositoryでの取得は未確認です。

**31パス版の手動再実行（同日）**：講師用 `main` のCommit `6b25083e620bb5bbc09c67bb04b0d3f0631e9d2e` から[手動起動したActions実行 39785400184](https://github.com/t-oikawa-sendai/ai-setup-materials/actions/runs/39785400184) は `completed/success` で、同期jobの全stepが成功しました。ログで管理対象31パスが同一内容であることと、実際の出力 `No managed changes to publish.` を確認しました。配布先を新たにfetchした後も `origin/main` は `d884959264795d1b82f3bde74dab1e91f87959eb` のままで、新しいCommitは作られていません。生徒本人の招待・テンプレート利用・個人Repositoryでの取得は未確認です。

## 7. 授業前：許可する教材だけに生徒を招待する

### 7.1 初回の前提設定

講師アカウント **t-oikawa-sendai** で操作します。次の設定は初回の環境整備で確認し、生徒を招待するたびに設定し直す必要はありません。

| 教材・入口での表示名 | 対象Repository | 公開範囲 |
|---|---|---|
| AI活用入門 | [OSLIB21-materials/ai-setup-materials-student](https://github.com/OSLIB21-materials/ai-setup-materials-student) | Private |
| 設計文書管理入門 | [OSLIB21-materials/design-document-templates-student](https://github.com/OSLIB21-materials/design-document-templates-student) | Private |

両RepositoryのPrivate設定は2026-10-29にGitHubメタデータで確認しています。

組織メンバー全員へ教材の閲覧権限が付かないよう、[OSLIB21-materials](https://github.com/OSLIB21-materials) の **Settings → Member privileges → Base permissions** は **No permission** とします。今回、この設定への変更と反映は確認済みです。画面上の項目名は **No permission** です。

別環境でこの設定を変更する場合は、先に影響する組織メンバーとRepositoryを確認します。これは組織全体の基本権限であり、個別・Team経由で付けた権限を取り消す設定ではありません。また、外部コラボレーターにはこの基本権限は適用されません。今回の生徒のアクセス範囲は、次のRepository単位の招待で指定します。

### 7.2 講師の操作：教材にReadで招待する

1. 生徒本人から **GitHubユーザー名** を受け取り、許可する教材を決めます。表示名やメールの宛名と取り違えないようにします。パスワードや認証コードは収集しません。
2. 上の表から、許可する教材のRepositoryを開きます。AI活用だけを許可する場合は **ai-setup-materials-student** です。
3. そのRepositoryの **Settings → Collaborators & teams** を開き、**Add people** をクリックします。
4. 生徒のGitHubユーザー名を検索し、一致するアカウントを選びます。
5. **Choose a role** で **Read** を選び、アカウント名と対象Repository名が表示された **Add … to …** ボタンで招待します。
6. 生徒へ、招待メールの確認と承諾を案内します。**招待の有効期限は作成から7日間**です。見当たらない場合は登録メールアドレス・迷惑メールを確認し、期限切れの場合は招待状況を調べて再送します。期限切れの外部コラボレーター招待は、組織の **People → Failed invitations** からも確認・再試行できます。

**講師側の閲覧許可は手順5で済んでいます。生徒が承諾した後の、追加の講師承認はありません。** 両方の教材を許可する生徒には、それぞれのRepositoryで必要な招待・権限付与を行います。

この手順は、組織メンバーでない生徒を教材の外部コラボレーターとして招待する方式です。組織の **People → Invite member** から参加させる操作は含めません。既にメンバーやTeamの権限を持つ人については、既存の権限が残るため、その付与元も確認します。

**メールアドレスで招待する場合**

Repositoryへの招待は、GitHubユーザー名の代わりにメールアドレスでも指定できます。手順4で、生徒本人が受信できるメールアドレスを入力し、同じく許可する教材だけに **Read** で招待します。メールを探す際は、GitHubの登録メールではなく、実際に招待を送った宛先を確認します。

メール招待は、**GitHubに登録済みのメールアドレスだけに限定されません。** GitHub公式では、メールで送った招待は別のGitHubアカウントでも承諾できる仕様とされています。**許可する生徒のGitHubアカウントまで指定したい場合は、メールアドレスではなくGitHubユーザー名で招待します。** メール招待を使う場合は、生徒本人のアカウントで承諾し、招待リンクを他の人へ転送しないよう案内します。

この説明は、今回のRepositoryへの招待についてのものです。Organizationのメンバー招待に関するメールアドレスの条件とは区別します。

### 7.3 生徒への案内と承諾後の確認

生徒へ次の内容を案内します。

- 講師に伝えたGitHubアカウントでログインし、今回の教材への招待メールから承諾する。
- 招待が作成されてから7日以内に承諾する。期限切れの場合は講師に再送を依頼する。この期限は承諾前の招待のものであり、承諾後の閲覧期間ではない。
- 承諾すると、その教材を閲覧できる。講師の追加承認を待つ必要はない。
- 普段の入口は **[https://github.com/t-oikawa-sendai](https://github.com/t-oikawa-sendai)**。このページをブックマークし、許可された教材名を選ぶ。
- 「AI活用入門」の教材トップにある **生徒用マニュアル** から、生徒用手順書を読める。

GitHubの自動招待メールのリンクは招待承諾用であり、講師のプロフィールURLに差し替える設定はありません。共通の入口URLは、講師からの案内メールや普段の連絡方法で別途伝えます。生徒用手順書自体もPrivate教材内にあるため、承諾前の案内には上記の要点を直接記載します。

生徒本人のアカウントで、入口から許可された教材のREADMEや教材本文が開けることを確認します。講師アカウントでの閲覧や、教材名・リンクの表示だけを、生徒の閲覧確認にしません。許可した教材で404になる場合は、ログイン中のユーザー名、招待先、承諾状況、Repositoryの権限を確認します。

個人用の教材コピーの作成は生徒の任意です。講師から作成を指示する運用ではなく、希望する生徒が生徒用手順書の第5〜6章を使います。Templateから個人Repositoryを作る操作は、教材を閲覧するための条件ではありません。

### 7.4 今回合格したテストと実生徒への適用

2026-10-29、**oikawa-solacom-test**（表示名：oikawa@test）を生徒役として確認しました。

| 確認内容 | 結果・根拠 |
|---|---|
| 再試験の開始状態 | Userが既存の組織メンバー登録を削除。削除後の権限照会は両教材とも `none` |
| AI活用だけへの招待 | UserがAI活用のRepositoryにReadで招待し、テストアカウントで承諾 |
| 許可教材の閲覧 | 承諾直後の画面でAI活用のREADME本文を確認。Userからも「AI活用はOK」と報告 |
| 未許可教材の閲覧不可 | 共通入口からの確認を案内後、Userから「文書は404なのでOK」と報告 |
| 合否 | Userが「合格」と判定 |

これはテストアカウントでのアクセス制限・閲覧の合格です。実生徒への招待は未実施で、合格後に第7.2節の手順で開始します。個人Repositoryの作成やAIによるPrivate Repositoryの取得は、今回の合格範囲に含みません。

テストで行った既存メンバーの削除は、最初から試すための操作でした。実生徒を招待する通常手順には含めません。

## 8. 同期対象の除外と講師用正本のPrivate化

`personas/reference/PERSONA_SETUP_ADVISOR.md` は生徒向けの追加・更新対象から外します。講師正本のファイル本文は保持します。配布版のRoot README・Reference READMEから利用案内・リンクを除き、生徒用手順書のS-SETUPの章も削除します。

同期対象からの除外だけでは、既に配布済みのファイル本体は消えません。2026-10-29のUser指示により、`OSLIB21-materials/ai-setup-materials-student` の `main` にある `personas/reference/PERSONA_SETUP_ADVISOR.md` だけを個別削除する対象としました（D-083）。まず同期除外を講師正本のGitHub `main` に反映し、その後で配布先の当該ファイルを削除します。同期スクリプトによる自動削除の範囲は旧9パスのままです。講師正本・生徒個人コピー・過去のGit履歴は削除しません。実施状況は `project-notes/CURRENT.md` で管理します。

**講師用正本をPrivateにする前の確認**：同期対象の配布物に講師正本へのURLが混入していないこと、Actionsの結果と配布先の内容が一致することを確認します。その後、講師用RepositoryのVisibilityをPrivateに変更するかを本人が判断・操作し、変更後の表示を確認します。Private化は過去にPublicだった期間の閲覧や取得を取り消す操作ではありません。

## 9. 運用上の注意と用語

- Templateから作った個人Repositoryは独立したコピーです。配布先の更新や、後日のアクセス権解除では自動更新・自動削除されません。
- **Read** は配布元を閲覧できる権限です。生徒の個人Repositoryを講師が管理する権限ではありません。
- **Private** は閲覧可能な相手を制限する設定です。設定後も権限を持つ人は閲覧できます。
- 教材のライセンスや授業上の再配布条件は、アクセス権とは別に案内してください。

## 10. GitHub公式資料

- [Organizationの作成](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch)
- [Template repositoryの作成](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)
- [TemplateからRepositoryを作る](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
- [Actionsの手動起動](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow)
- [Actions Secretsの利用](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets)
- [Repositoryの可視性変更](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)
- [Repositoryへの招待と権限管理](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository)
- [外部コラボレーターの追加](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/adding-outside-collaborators-to-repositories-in-your-organization)
- [組織の基本権限](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/setting-base-permissions-for-an-organization)
- [招待の有効期限は作成から7日間](https://github.blog/changelog/2020-02-05-self-expiring-repository-and-organization-invitations/)
- [期限切れ招待の再試行](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization#retrying-or-canceling-expired-invitations)
- [メール招待とユーザー名指定の違い（Email Invitations）](https://bounty.github.com/ineligible.html)
