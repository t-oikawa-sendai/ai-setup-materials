# 受講生用教材のプロフィール更新履歴連携

Status: User採用済み設計（変更なし通知の導通確認済み・新しい配布日の自動更新未検証）

Last Updated: 2026-10-23

Userは、**受講生用Private Repositoryへ実際に反映された更新だけを対象にすること**、以下の`repository_dispatch`・token・日付単位の集約方式、限定された自動Commit・Push例外を採用した。採用はGitHub設定、Secret登録、workflow実行、公開表示の成功を意味しない。

## 対象とデータ境界

講師正本 `t-oikawa-sendai/ai-setup-materials` の既存同期workflowが正常終了した後、Private配布先 `OSLIB21-materials/ai-setup-materials-student` の `origin/main` の現在のCommit日時を取得し、Asia/Tokyoでの日付だけを公開プロフィールへ送る。同期が変更なしでも同じ手順を実行するため、source workflowの手動再実行で通知を復旧できる。Private配布先の更新がない限り、プロフィールREADMEは変更しない。

公開イベントの `client_payload` は `date` だけとする。Private側のCommit SHA、メッセージ、変更ファイル名、本文、Credentialは送らない。公開READMEの文言は定型の「受講生向け教材の配布内容を更新しました。」だけを使用する。既存の2026-10-22の個別要約は、同日通知で上書きしない。

受信側はAI活用入門の教材更新日と「最近の更新（直近5件）」を同時に更新する。通知日が現在のAI教材更新日と同日またはそれ以前なら無変更。新しい日付だけを1日1行加え、日付降順の5行を維持する。非AI行を改変しない。表の形式・件数・日付が想定外の場合は失敗し、READMEを保存しない。

sourceで抽出した配布日と受信側で受け取った日付が、それぞれの実行時点のJST日付より未来なら失敗する。時計の不整合や異常なCommit日時を、そのまま公開履歴へ転記しない。

## 認証と起動

- source Actions secret `PROFILE_HISTORY_DISPATCH_TOKEN`: プロフィールRepository 1件だけを対象にしたfine-grained tokenで、Repository Contents:writeのみ。`repository_dispatch`送信専用に使う。既存の`STUDENT_TEMPLATE_TOKEN`と兼用しない。
- 受信側は自身の`GITHUB_TOKEN`にContents:writeだけを与え、READMEのみをCommit・Pushする。Private Repositoryを読むCredentialはプロフィール側に置かない。
- 手動復旧は**sourceの既存同期workflowの`workflow_dispatch`**を起動する。受信側単独の手動起動や日付入力欄は設けない。手動でも日付はsourceが配布先`main`から取得する。
- 配布先への同期が失敗したら通知しない。日付取得または通知が失敗したらsource workflow全体を失敗とし、再実行で復旧する。受信側で形式検証・更新・Commit・Pushのいずれかが失敗した場合も受信workflowを失敗とする。

## 承認範囲と稼働前の確認

Userはsource・profile両Repositoryのこの設定差分のCommit・Pushを承認し、以後の受信workflowによる自動Commit・PushをプロフィールREADMEの「AI活用入門の教材更新日・変更概要」と「最近の更新（直近5件）」に限って承認した。他の教材本文、別ファイル、Private教材本体、通常の人手作業への包括的なGit操作許可ではない。2026-10-23にsource Actions secret `PROFILE_HISTORY_DISPATCH_TOKEN` の名前と登録日時を確認した。値は取得していない。source側設定は`ce48dda7efcf3ce0ebb302def3be325cbff0dc69`でmainへ反映済み。

Push起動の[source実行](https://github.com/t-oikawa-sendai/ai-setup-materials/actions/runs/39927699348)は成功し、配布先31パスは変更なしだった。日付通知後の[profile受信実行](https://github.com/t-oikawa-sendai/t-oikawa-sendai/actions/runs/39927727246)も成功し、同日通知としてREADMEは無変更だった。新しい配布日での自動Commitと公開プロフィールの更新表示は未検証。プロフィールREADMEの「手動管理」コメントをAI活用入門のみ自動・他教材は手動という実状態へ更新するかは、別途判断する。
