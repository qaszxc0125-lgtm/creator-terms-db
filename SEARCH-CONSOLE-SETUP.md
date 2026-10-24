# Google Search Console 初回設定チェックリスト

対象サイト： https://qaszxc0125-lgtm.github.io/creator-terms-db/

この文書は運営者が初回設定を行うための手順書です。Googleアカウントへのログインや所有権確認は、サイト運営者本人が実施してください。認証トークンやHTML確認ファイルは、Googleが発行した実物を使用し、推測で作成しないでください。

## 1. URLプレフィックス プロパティを追加

1. [Google Search Console](https://search.google.com/search-console/) を開き、対象のGoogleアカウントでログインします。
2. プロパティ追加から「URLプレフィックス」を選びます。
3. 次のURLを末尾のスラッシュまで含めて入力します。

   `https://qaszxc0125-lgtm.github.io/creator-terms-db/`

4. Googleが提示する所有権確認方法を選びます。

## 2. 所有権を確認

Googleの画面に表示された手順に従います。HTMLファイル方式の場合は、Googleからダウンロードした確認ファイルをリポジトリの公開ルートに、ファイル名・内容を変更せず追加します。HTMLタグ方式の場合は、Googleが発行した実際の確認タグを共有してもらえれば、サイトの `<head>` への追加を支援できます。

- 確認ファイル名、トークン、メタタグの値を推測してはいけません。
- 確認に使うファイルやタグは削除しないでください。削除すると所有権確認が失われる場合があります。
- 設定後、公開サイトでファイルが表示できることを確認し、Search Consoleで「確認」を実行します。

## 3. サイトマップを送信

所有権確認後、Search Consoleの「サイトマップ」から次を送信します。

`sitemap.xml`

サイトマップの完全なURL：

https://qaszxc0125-lgtm.github.io/creator-terms-db/sitemap.xml

送信後、ステータスと検出されたURL数を確認します。送信しても、すべてのURLがインデックス登録される保証はありません。

## 4. インデックス登録を確認

「URL検査」にトップページと主要記事URLを1つずつ入力し、Googleが取得できるか、インデックス登録の状態に問題がないか確認します。必要に応じて「インデックス登録をリクエスト」を使います。連続して何度もリクエストする必要はありません。

- https://qaszxc0125-lgtm.github.io/creator-terms-db/
- https://qaszxc0125-lgtm.github.io/creator-terms-db/ai-commercial-use-guide.html
- https://qaszxc0125-lgtm.github.io/creator-terms-db/ai-stock-submission-guide.html
- https://qaszxc0125-lgtm.github.io/creator-terms-db/ai-tool-affiliate-programs.html
- https://qaszxc0125-lgtm.github.io/creator-terms-db/ai-tool-affiliate-start-guide.html
- https://qaszxc0125-lgtm.github.io/creator-terms-db/gemini-image-commercial-use.html

## 5. 定期的に見る指標

最初は週1回を目安に「検索パフォーマンス」で次を確認します。

- 表示回数：検索結果に表示された回数
- クリック数：検索結果から訪問された回数
- CTR：表示回数に対するクリック率
- 平均掲載順位：検索結果での平均的な掲載位置
- ページ／検索クエリ：どの記事が、どの検索語で表示されているか

初期データが少ない間は、短期間の上下だけで大幅な変更をしないでください。検索順位やアクセス数、収益は保証されません。

## 現在のサイト側の準備状況

- `sitemap.xml` を公開済み
- `robots.txt` にサイトマップを記載済み
- 主要ページにcanonical URLを設定済み
- 記事間の内部リンクを設定済み
- Search Consoleの所有権確認・サイトマップ送信は、運営者のアカウント操作待ち
- 独自アクセス解析やアフィリエイト成果計測は未設定

最終確認日：2026-10-24
