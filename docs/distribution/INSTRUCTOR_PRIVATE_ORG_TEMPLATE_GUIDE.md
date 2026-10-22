# 講師用｜GitHub Free OrganizationのPrivate Templateで教材を配布する手順書

- 改訂日：2026-10-22
- 用途：講師が管理する正本から、選んだ教材だけを生徒向けテンプレートへ配布する
- 費用：GitHub Freeの個人アカウントとOrganizationを使用
- 生徒の操作：WebブラウザでPrivate Templateから自分のPrivate Repositoryを作成する
- この手順書は運用手順と確認済みの構成を記す。生徒の招待・個人Repositoryの作成・利用成功は、実施するまで完了扱いにしない
- 手順書の管理場所：講師用正本の `docs/distribution/`。同ディレクトリの2冊を編集正本とし、Downloads版はコピーとして扱う。生徒用手順書だけを配布対象とし、講師用手順書は配布しない

## 1. 現在の構成

```text
講師が管理する教材の正本
t-oikawa-sendai/ai-setup-materials の main
  │ mainへのPush、またはGitHub Actionsの手動起動
  ▼
選定した31パスだけを一方向に同期
OSLIB21-materials/ai-setup-materials-student
  ├── GitHub Free Organization所有
  ├── Private・Template repository
  └── 招待され、Read権限を持つ生徒が閲覧
        │ Use this template
        ▼
各生徒の個人アカウントに作るPrivate Repository
```

配布先：[OSLIB21-materials/ai-setup-materials-student](https://github.com/OSLIB21-materials/ai-setup-materials-student)

**教材の正本は講師用Repositoryの `main` です。** 生徒向けTemplateは選定ファイルの配布コピーです。各生徒がTemplateから作るRepositoryはさらに独立したコピーであり、後続の教材更新は自動反映されません。GitHub Actionsは生徒の個人Repositoryを操作しません。

**31パス版の構成**：2冊を講師用正本の `docs/distribution/` で管理し、生徒用 `STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md` だけを31番目の同期対象にします。配布先用に生成するRoot READMEには、この生徒用手順書へのリンクを付けます。正本のRoot READMEは変更しません。講師用手順書は同期対象外で、自動削除の許可範囲も旧9パスのままです。31パス版の実行結果と配布先の内容は§6の確認手順で判定します。

講師用Repositoryは、この改訂時点では**Public**です。配布先の構築・内容確認後に講師用RepositoryをPrivateへ変更する予定ですが、その変更は別操作です。変更前は内部文書を含む講師用Repositoryを誰でも閲覧できます。Private化を実施した事実は、GitHubの表示で別途確認してください。

## 2. 構築済みの設定と未実施の授業準備

| 項目 | 現在の扱い |
|---|---|
| Organization | `OSLIB21-materials`、GitHub Freeで作成済み |
| 配布先 | `ai-setup-materials-student`、Private・Template repositoryとして作成済み。2026-10-22の30パス版Push後、認証済みGitHub画面で `Private template`、`Use this template`、当時の最新Commit `547d018dd66f815c9d3472a8bbd98cd63c7604c0` を再確認 |
| 同期 | 講師用 `main` へのPushと、GitHub Actionsの手動起動に対応 |
| 配布範囲 | 追加・上書きは従来の30パスと生徒用手順書の計31パス。自動削除の許可は当初の9パスのみ。31パス版の実測は§6に区別して記録 |
| 認証情報 | 講師用RepositoryのActions用Repository Secret `STUDENT_TEMPLATE_TOKEN` に登録済み。値は手順書に書かない |
| 生徒の招待とRead権限 | 実在する生徒について授業前に設定・確認する。構築済みとは扱わない |
| 生徒の個人Repository | 各生徒が自分で作成する。講師側の構築作業では作成・変更していない |

初回の9パス配布、その後の30パスへの拡張、S-SETUPの個人URL欄への改訂は、それぞれGitHub Actionsで成功を確認済みです。直近の実測済み実行URLとHEAD、確認できていない事項は§6に記録します。

## 3. 何を配るか

この版の同期処理は、講師用Repositoryの [`scripts/sync_student_template.py`](https://github.com/t-oikawa-sendai/ai-setup-materials/blob/main/scripts/sync_student_template.py) にある31パスの許可リストを使います。選ばれたパスだけを配布先の同じ位置へ追加・上書きします。正本側で消えたときに配布先から自動削除できるのは、最初に承認された9パスだけです。後から追加した22パス（生徒用手順書を含む）が正本から消えた場合は、勝手に削除せず同期を停止します。

| 配布するもの | パス数 | 扱い |
|---|---:|---|
| ルート `README.md` と `LICENSE` | 2 | READMEは配布先用の案内に調整。LICENSEは原文のまま |
| `personas/` 直下の文書4件と図1件 | 5 | 選定した設計説明・Evidence・共通仕様など |
| `personas/education/` | 14 | README、GEM 6件、SKILLS 6件、旧資料1件 |
| `personas/reference/` | 9 | README、Persona、S-SETUP、運用参考資料など |
| `docs/distribution/STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md` | 1 | 生徒用手順書。Root READMEの配布コピーから案内 |

従来の30パスに追加するのは、生徒用手順書の1件だけです。講師用の同名ディレクトリ内の手順書は配布しません。

Root README、Education README、Reference README、`WHY_PERSONA_MATTERS.md`、`PERSONA_IDENTIFICATION_AND_SETUP.md`、S-SETUPの**配布コピーだけ**は、配布しない資料へのリンクや取得先の案内を調整します。31パス版では、Root READMEの配布コピーに生徒用手順書へのリンクも付けます。講師用正本の本文は変更しません。それ以外の選定ファイルは原文のままです。Draft、Approved、Deprecatedの表示を配布時に昇格・偽装しません。選定した通常文書のDraftとApprovedの間の変更は同期を続けますが、その他の状態変化や不正なStatusは停止します。

`AGENTS.md`、`project-notes/`、`docs/` 内の選定外ファイル（講師用手順書を含む）、選定外のPersonaの本文、秘密情報は配布しません。選定文書中に内部文書の**ファイル名だけ**を記したコメントが残る場合がありますが、内部文書の本文は配布しません。配布先の許可リスト外のファイル、他branch、過去の履歴は書き換えず、force pushは使いません。

### 従来からの選定30パスの一覧

```text
README.md
LICENSE
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
personas/reference/PERSONA_SETUP_ADVISOR.md
personas/reference/PERSONA_OPERATION_CASE_STUDY.md
personas/reference/PERSONA_PROMPT_TEMPLATE.md
personas/reference/CHAT_HANDOFF_TEMPLATE.md
```

この一覧は現在の決定を読むための写しです。将来の変更は講師用 `main` の許可リストと判断記録を確認してください。新しいファイルを `personas/` に置いただけでは、自動で配布対象になりません。

31番目のパス：`docs/distribution/STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md`。従来30パス版の実測記録には含まれません。

## 4. 教材を更新するとき

1. 講師用Repositoryの `main` を正本として教材を編集します。既存の `AGENTS.md` と判断記録に従い、変更前の状態と差分を確認します。
2. 配布範囲を変えたい場合は、追加・削除する**具体的なパス**を決め、許可リストと判断記録を更新します。新しいパスを正本から消したときの扱いも個別に決めます。
3. 必要なレビューと明示承認を経て、講師用 `main` へ通常のCommit・Pushを行います。force pushは使いません。
4. PushによりGitHub Actionsの **Sync selected student materials** が起動します。講師用Repositoryの **Actions** タブで実行結果を開き、`success` と各stepの結果を確認します。
5. 配布先の `main` を開き、Private・Templateの設定、この版の許可リストに対応する31パス、変更した本文、対象外ファイルの非配布を確認します。Actionsが成功しただけで内容一致と判断しません。

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
| S-SETUP | 配布コピーに講師用URLが残らず、各自のURL記入欄があること |
| 生徒の利用 | 招待、Read権限、本人のPrivate Repository作成・取得成功をそれぞれ別に確認 |

**配布内容の実測（2026-10-22）**：S-SETUP配布コピーを改訂した講師用GitHub `main`、ローカルHEAD、`origin/main` は `defbc2a4bc675196409fe257b392227ab6f824c4` で一致しました。[Push起動のActions実行 39777787027](https://github.com/t-oikawa-sendai/ai-setup-materials/actions/runs/39777787027) は `success` で、同期jobの全stepも成功しました。配布先のPrivate Repositoryを取得して確認した `main` のHEADは `547d018dd66f815c9d3472a8bbd98cd63c7604c0` です。trackedファイルは選定30パスと完全に一致し、正本からの配布変換後の内容と、欠落・余剰・byte不一致がありませんでした。直前の配布先HEAD `c20a3ccb656ddb9157bc0b1b7126f66704f6b9e4` は履歴上の祖先として残っています。配布先checkoutはcleanでした。

**後続の変更なし同期（同日）**：`project-notes/CURRENT.md` の確認記録だけをnoreply Git identityでCommitし、講師用 `main` へforce pushを使わず通常Pushしました。講師用GitHub `main`、ローカルHEAD、`origin/main` は `edf7780908fd996b1e7441c21af9b91623cd7fbd` で一致しました。[Actions実行 39778533319](https://github.com/t-oikawa-sendai/ai-setup-materials/actions/runs/39778533319) は `success` で、同期jobの各stepも成功し、ログに `No managed changes to publish.` と表示されました。配布先のリモート `main` は `547d018dd66f815c9d3472a8bbd98cd63c7604c0` のままで、新しいCommitは作られていません。この後続実行を、上記30パスの内容照合の代わりにはしません。

30パス版のPush後、認証済みChromeの配布先画面で `Private template`、`Use this template`、当時の最新Commit `547d018dd66f815c9d3472a8bbd98cd63c7604c0` を再確認しました。講師用正本のGitHubメタデータは引き続きPublicです。生徒の実アカウントでの招待・テンプレート利用・S-SETUPの取得は未確認です。

**31パス版の実測待ち**：生徒用手順書の同期と配布コピーのRoot READMEからのリンク、講師用手順書の非配布、従来30パスの維持は、Actionsの完了後に配布先の実ファイルで確認します。確認が終わるまで、上記30パス版の実測結果を31パス版の合格と読み替えません。

## 7. 授業前：生徒へ閲覧権限を付ける

1. `OSLIB21-materials` の **People → Invite member** で、実在する生徒のGitHubユーザー名または登録メールアドレスを指定します。Organization roleは **Member** にします。
2. 生徒が招待を承諾したことを確認します。招待が見つからない・期限切れの場合は再送の要否を調べます。
3. 配布先Repositoryの **Settings → Collaborators & teams** で、その生徒へ **Read** 権限を付けます。OrganizationのMemberであることと、このPrivate Repositoryの閲覧権限は別に確認します。Organization全体のBase permissionsも確認します。
4. 本人のアカウントで配布先を開け、**Use this template** が表示されることを確認します。本人が自分の個人アカウントをOwnerにしてPrivate Repositoryを作る操作は、生徒用手順書に従ってもらいます。

生徒へ伝えるURLは [配布先のPrivate Template](https://github.com/OSLIB21-materials/ai-setup-materials-student) です。31パス版の配布を確認した後は、テンプレートのRoot READMEにある生徒用手順書のリンクも案内できます。講師用正本のURLを生徒の取得先として案内しません。生徒の個人Repositoryへ講師が直接同期・書き込みを行う運用ではありません。

## 8. 配布版S-SETUPと講師用正本のPrivate化

S-SETUPは従来からの30パスに含まれます。講師用の `personas/reference/PERSONA_SETUP_ADVISOR.md` は原文のまま保存し、配布先に置くコピーだけ、講師用RepositoryのURLを**各生徒の個人Repository内にある同ファイルのURLを記入する未設定欄**へ置き換えます。各生徒のURLは作成するRepository名によって異なるため、講師側の同期では埋められません。

未記入の欄は実際のURLではありません。生徒がPrivate RepositoryのURLを入れても、利用するAIがそのRepositoryへ認証・接続できなければ本文を取得できません。取得不能なのにG方式の取得成功と表示してはいけません。生徒の個人Repositoryは、講師用正本の更新を自動受信しません。

**講師用正本をPrivateにする前の確認**：新しいS-SETUP配布コピーがGitHub上で確認でき、講師用RepositoryへのURLが配布物に残っていないこと、Actionsの結果と配布先の内容が一致することを確認します。その後、講師用RepositoryのVisibilityをPrivateに変更するかを本人が判断・操作し、変更後の表示を確認します。Private化は過去にPublicだった期間の閲覧や取得を取り消す操作ではありません。

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
