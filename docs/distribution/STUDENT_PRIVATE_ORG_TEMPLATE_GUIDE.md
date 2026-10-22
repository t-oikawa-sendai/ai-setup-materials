# 生徒用｜Private教材テンプレートから自分のGitHub Repositoryを作る手順書

- 対象：IT職業訓練校の受講生
- 費用：GitHub Freeを使用
- 準備するもの：自分のGitHubアカウント、Webブラウザ、講師から届く招待
- 作業方法：GitHubの画面操作だけ。ZIPのダウンロードやGitコマンドは不要
- この手順書を含む配布版では、教材テンプレートのRoot READMEからこの手順書を開ける

## 1. この作業で作るもの

```text
講師のOrganization：OSLIB21-materials
  └── ai-setup-materials-student（Private・教材テンプレート）
        │ Use this template
        ▼
あなたの個人GitHubアカウント
  └── 自分のRepository（Private・独立した教材コピー）
```

講師から閲覧を許可されたテンプレートを、自分のGitHubにコピーして学習を始めます。自分のRepositoryを編集しても、講師の教材は変更されません。講師がテンプレートを後から更新しても、**あなたのRepositoryには自動反映されません**。

この手順書を含む版のテンプレートでは、手順書は `docs/distribution/STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md` にあります。テンプレートのRoot READMEから開けます。作成した自分のRepositoryにも同じ場所へコピーされるので、後から読み直せます。講師用の管理手順書は、あなたのRepositoryには配布されません。

講師が管理する元のRepositoryは、生徒向けの取得先ではありません。生徒は以下のPrivate Templateだけを開きます。

## 2. GitHubにサインインする

1. [GitHub](https://github.com/) にアクセスします。
2. 自分のGitHubアカウントでサインインします。アカウントを持っていない場合は、先に無料アカウントを作ります。
3. 画面右上のアイコンなどで、使用中のアカウントが自分のものか確認します。

## 3. 講師からの招待を受ける

1. GitHubから届く招待メール、またはGitHubの通知を開きます。
2. 招待元が **OSLIB21-materials** であることを確認します。
3. **Join organization** などの承諾ボタンを押します。
4. 招待を受け入れたことを確認します。

招待が見当たらない、期限切れ、追加の認証が求められる場合は、講師に知らせてください。招待を受け入れるだけでPrivate教材を開けるとは限りません。講師が教材RepositoryへのRead権限も設定します。

## 4. 教材テンプレートを開く

次のURLを開きます。

**[https://github.com/OSLIB21-materials/ai-setup-materials-student](https://github.com/OSLIB21-materials/ai-setup-materials-student)**

`404` と表示されたり、教材が見えなかったりする場合は、自分のアカウントでログインしているか、招待を受け入れたか確認します。そのうえで講師に教材へのRead権限を確認してもらいます。URLを変更したり、講師用の元Repositoryを探したりする必要はありません。

## 5. 自分のPrivate Repositoryを作る

1. 教材ページの **Use this template** を押します。
2. **Create a new repository** を選びます。
3. **Owner** は、**自分自身の個人GitHubアカウント**を選びます。講師のOrganizationは選びません。
4. **Repository name** に、講師が指定した名前、または自分で決めた名前を入れます。
5. **Visibility** で必ず **Private** を選びます。
6. **Include all branches** は、講師から特別な指示がなければ選びません。
7. **Create repository from template** を押します。

新しいRepositoryには、教材テンプレートの `main` にある選定ファイルがコピーされます。元Repositoryの過去のCommit履歴がそのまま移る仕組みではありません。

## 6. 作成直後に確認する

自分のRepositoryのページで確認します。

- [ ] URLが `https://github.com/＜自分のユーザー名＞/＜自分のRepository名＞` になっている
- [ ] Repository名のそばに **Private** と表示される
- [ ] `README.md`、`LICENSE`、`personas/` が表示される
- [ ] この手順書を含む版では、`README.md` から `docs/distribution/STUDENT_PRIVATE_ORG_TEMPLATE_GUIDE.md` を開ける
- [ ] 講師のPrivate Templateではなく、**自分のRepository**を開いている

教材の構成と設計方針は、自分のRepositoryにある `README.md` から確認できます。講師が以前に配布した30パス版には、この手順書が含まれていません。この手順書を含む新版は31パスです。文書に **Draft** とあれば提案中、**Approved** とあればその文書の状態表示です。コピーされたことだけを理由にDraftがApprovedへ変わることはありません。

## 7. S-SETUPを使う場合：自分のファイルURLを設定する

`personas/reference/PERSONA_SETUP_ADVISOR.md` は、Personaの選び方や設定を案内する教材です。配布時点では、冒頭の `URL` 欄が**未設定**になっています。使うときは、講師用Repositoryではなく、**自分のPrivate Repository内にあるこのファイルのURL**を記入します。GitHubプロフィールのURLや、RepositoryのトップページのURLではありません。

1. **自分のRepository**の `main` で、`personas/reference/PERSONA_SETUP_ADVISOR.md` を開きます。
2. ブラウザのアドレス欄から、そのファイルのURLをコピーします。形は `https://github.com/＜自分のユーザー名＞/＜自分のRepository名＞/blob/main/personas/reference/PERSONA_SETUP_ADVISOR.md` です。
3. ファイルの編集ボタンから、冒頭の `- URL：【各自のRepositoryの ...（未設定）】` の行を、コピーした**実際のファイルURL**へ置き換え、自分のRepositoryに保存します。講師のテンプレートを編集する操作ではありません。
4. URLが正しく入ったことを自分のRepositoryで確認します。

**URLを書くだけでは、AIがPrivate Repositoryを読めるようにはなりません。** 使用するAIサービスがあなたのRepositoryへ認証・接続できるかは別の確認が必要です。取得できなければ「GitHubから取得済み（G）」と扱わず、講師に利用方法を確認してください。公開設定をPublicへ変更して解決しようとしないでください。

S-SETUPを使わない授業では、このURL欄をすぐに編集する必要はありません。講師用の元Repositoryは今後Privateへ変更される予定です。あなたが利用するのは、自分に配布されたコピーです。

## 8. よくある問題

| 現象 | 確認・対応 |
|---|---|
| 教材のURLを開くと `404` | 自分のアカウントでのログイン、Organization招待の受諾、教材へのRead権限を確認。解決しなければ講師へ連絡 |
| **Use this template** がない | 上の正しい教材URLを開いているか確認し、講師にTemplate設定を確認してもらう |
| **Owner** に自分が表示されない | 自分のGitHubアカウントでログインしているか確認し、講師へ連絡 |
| Repository名が使用できない | 同じ名前のRepositoryがないか確認し、別の名前を使う |
| 誤って **Public** にした | ほかの作業を止め、すぐ講師へ連絡する。公開されていた期間に閲覧・取得された可能性は、Privateへ戻しても取り消せない |
| S-SETUPのURLを入れてもAIが読めない | ファイルURLが自分のRepository内のものか、AIがPrivate Repositoryへ接続・認証できるか確認。取得不能ならG取得成功と扱わない |

## 9. 知っておくこと

- **Organization**：講師が教材へのアクセスを管理するGitHubの組織。
- **Private**：許可された人だけが閲覧できる設定。
- **Repository**：ファイルと変更履歴を保存するGitHub上の場所。
- **Template**：ファイル構成を使って、新しい独立したRepositoryを作る仕組み。
- **Read権限**：講師の教材を閲覧できるが、講師の教材そのものへ変更を保存できない権限。

自分のRepositoryは自分が管理します。公開や外部への再配布については、教材の `LICENSE` と講師の案内を確認してください。講師がPrivate Templateへのアクセスを後で解除しても、あなたが既に作成した個人Repositoryは自動で消えません。

## 10. GitHub公式資料

- [テンプレートからRepositoryを作成する](https://docs.github.com/ja/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
- [Organizationへの招待について](https://docs.github.com/ja/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization)
