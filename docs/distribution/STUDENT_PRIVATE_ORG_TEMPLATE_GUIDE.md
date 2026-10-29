# 生徒用｜招待を承諾して限定公開のGitHub教材を読む手順書

- 改訂日：2026-10-29
- 対象：IT職業訓練校の受講生
- 費用：GitHub Freeを使用
- 準備するもの：自分のGitHubアカウント、Webブラウザ、講師から届く招待
- 作業方法：GitHubの画面操作だけ。ZIPのダウンロードやGitコマンドは不要
- 教材を読む手順は第2〜4章。自分用の教材コピーの作成は任意で、希望する人は第5〜6章を使う

## 1. はじめに：招待と教材の入口

**講師が許可した教材への招待を承諾すると、その教材を読めるようになります。承諾後に、講師の追加承認を待つ必要はありません。**

普段使う教材の入口は、次のページです。ブックマークしておきましょう。

**[教材の入口：https://github.com/t-oikawa-sendai](https://github.com/t-oikawa-sendai)**

入口のページは公開されていますが、受講生限定の教材本文には閲覧許可が必要です。教材名やリンクが見えても、すべての教材を読めるわけではありません。

| 入口にある教材名 | GitHub上の教材名 |
|---|---|
| AI活用入門 | `OSLIB21-materials/ai-setup-materials-student` |
| 設計文書管理入門 | `OSLIB21-materials/design-document-templates-student` |

たとえば「AI活用入門」だけを許可された場合、「設計文書管理入門」の教材本文は閲覧できません。

初回の招待メールのリンクは、招待を承諾するためのものです。普段使う上記の入口URLとは役割が異なります。この手順書は、招待承諾後に「AI活用入門」の教材トップにある **生徒用マニュアル** のリンクから読み直せます。

## 2. 自分のアカウントを準備する

1. [GitHub](https://github.com/) にアクセスします。
2. 自分のGitHubアカウントでサインインします。アカウントを持っていない場合は、先に無料アカウントを作ります。
3. 画面右上のアイコンなどで、使用中のアカウントが自分のものか確認します。
4. 講師に、自分の **GitHubユーザー名** を指定された連絡方法で伝えます。表示名やメールの宛名ではなく、プロフィールのURL `https://github.com/ユーザー名` に入る名前です。パスワードや認証コードは伝えません。

## 3. 教材への招待を承諾する

1. 講師に伝えたGitHubアカウントでログインしているブラウザを使います。
2. そのアカウントの登録メールアドレスに届いた、今回の教材への招待メールを開きます。
3. 招待先が **OSLIB21-materials** の許可された教材であることを確認します。「AI活用入門」なら **ai-setup-materials-student** です。
4. メール内の招待リンクを開き、GitHub上で招待を承諾します。ログインを求められた場合は、講師に伝えたアカウントでログインしてから承諾します。
5. 教材ページを開き、ファイル一覧と **README** の本文が表示されることを確認します。READMEは教材トップに表示される案内文です。

講師は招待時に **Read（閲覧）権限** を設定しています。承諾すると、その教材を閲覧できます。別の教材を受講する場合は、その教材についても講師の許可と必要な招待を受けます。

**招待の有効期限は、招待が作成されてから7日間です。期限内に承諾してください。期限切れの場合は、講師へ招待の再送を依頼してください。** この7日間は招待を承諾するまでの期限であり、承諾後の教材閲覧期間を7日間に制限するものではありません。

招待が見当たらない場合は迷惑メールも確認してください。期限切れや追加認証で進めない場合は、講師に知らせます。以前届いた組織への参加メールではなく、今回の教材への招待を使ってください。

## 4. 入口から教材を開く：毎回の使い方

1. 招待を承諾した自分のGitHubアカウントでログインします。
2. [教材の入口](https://github.com/t-oikawa-sendai)を開きます。
3. 講師から許可された教材名をクリックします。「AI活用入門」の場合は **AI活用入門（ai-setup-materials-student）** を選びます。
4. 教材トップの **README** を読み、案内されている教材リンクやファイル名をクリックして本文を開きます。

**教材の閲覧は、ここまででできます。自分のRepositoryを作ることは、閲覧の条件ではありません。**

許可されていない限定公開教材で `404`（ページが見つからない）と表示されるのは想定された動作です。許可された教材で `404` になる場合は、第7章を確認してください。

## 5. 任意：自分のPrivate Repositoryに教材をコピーする

自分用に教材を編集・保存したい人は、自由に個人用のPrivate Repositoryを作れます。作成は任意で、講師からの指示や承認を待つ必要はありません。「AI活用入門」の教材トップを開いて操作します。

1. 教材ページの **Use this template** を押します。
2. **Create a new repository** を選びます。
3. **Owner** は、**自分自身の個人GitHubアカウント**を選びます。講師のOrganizationは選びません。
4. **Repository name** に、自分で決めた名前を入れます。
5. **Visibility** で必ず **Private** を選びます。
6. **Include all branches** は選びません。教材の基本となる `main` だけをコピーします。
7. **Create repository from template** を押します。

新しいRepositoryには、教材テンプレートの `main` にある選定ファイルがコピーされます。元Repositoryの過去のCommit履歴がそのまま移る仕組みではありません。

自分のRepositoryを編集しても、講師の教材は変更されません。

**講師がPersonaを更新しても、生徒が個人Repositoryに作成したコピーには自動反映されません。最新のPersonaを使う場合は、教材の入口から最新の配布教材を開き、該当するPersonaを改めて取得して、自分のコピーを更新する必要があります。Persona以外の教材も同様です。**

## 6. 作成直後に確認する

自分のRepositoryのページで確認します。

- [ ] URLが `https://github.com/＜自分のユーザー名＞/＜自分のRepository名＞` になっている
- [ ] Repository名のそばに **Private** と表示される
- [ ] `README.md`、`LICENSE`、`personas/` が表示される
- [ ] この手順書を含む版では、`README.md` から `docs/distribution/STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md` を開ける
- [ ] 講師のPrivate Templateではなく、**自分のRepository**を開いている

教材の構成と設計方針は、自分のRepositoryにある `README.md` から確認できます。この手順書も同じ場所にコピーされ、後から読み直せます。講師用の管理手順書は配布されません。文書に **Draft** とあれば提案中、**Approved** とあれば承認済みという状態表示です。コピーしただけで文書の状態は変わりません。

## 7. よくある問題

| 現象 | 確認・対応 |
|---|---|
| 許可されていない教材で `404` になる | 教材ごとのアクセス制限による想定された動作。その教材を受講する必要がある場合は講師へ相談 |
| 許可された教材で `404` になる | 講師に伝えたアカウントでのログイン、今回の教材招待の承諾、入口から開いたURLを確認。解決しなければユーザー名・教材名・表示画面を講師へ連絡 |
| 招待メールが見当たらない・期限切れ | 有効期限は作成から7日間。登録メールアドレスと迷惑メールを確認し、見つからない場合や期限切れの場合は講師へ再送を依頼 |
| 招待リンクで別のアカウントが表示される | 講師に伝えたアカウントへ切り替えてから、招待リンクを開き直す |
| **Use this template** がない | 上の正しい教材URLを開いているか確認し、講師にTemplate設定を確認してもらう |
| **Owner** に自分が表示されない | 自分のGitHubアカウントでログインしているか確認し、講師へ連絡 |
| Repository名が使用できない | 同じ名前のRepositoryがないか確認し、別の名前を使う |
| 誤って **Public** にした | ほかの作業を止め、すぐ講師へ連絡する。公開されていた期間に閲覧・取得された可能性は、Privateへ戻しても取り消せない |

## 8. 知っておくこと

- **Organization**：講師が教材へのアクセスを管理するGitHubの組織。
- **Private**：許可された人だけが閲覧できる設定。
- **Repository**：ファイルと変更履歴を保存するGitHub上の場所。
- **Template**：ファイル構成を使って、新しい独立したRepositoryを作る仕組み。
- **Read権限**：講師の教材を閲覧できるが、講師の教材そのものへ変更を保存できない権限。
- **外部コラボレーター**：組織のメンバーにならず、指定されたRepositoryに参加する人。今回の教材への招待はこの方式です。

自分のRepositoryは自分が管理します。公開や外部への再配布については、教材の `LICENSE` と講師の案内を確認してください。講師がPrivate Templateへのアクセスを後で解除しても、あなたが既に作成した個人Repositoryは自動で消えません。

## 9. GitHub公式資料

- [テンプレートからRepositoryを作成する](https://docs.github.com/ja/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
- [特定のRepositoryに外部コラボレーターを招待する](https://docs.github.com/ja/organizations/managing-user-access-to-your-organizations-repositories/managing-outside-collaborators/adding-outside-collaborators-to-repositories-in-your-organization)
- [Repositoryごとの権限](https://docs.github.com/ja/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)
- [招待の有効期限は作成から7日間](https://github.blog/changelog/2020-02-05-self-expiring-repository-and-organization-invitations/)
