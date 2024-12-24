## 使い方

クローンする

```
$ git clone https://github.com/kazukikanomata/kazukikanomata.github.io.git
```

### Gemfileインストール

そのまえにbundle使える？
```
$ bundle -v
```


実際にインストール

```
$ bundle install
```

ローカルサーバー立ち上げ

```
$ bundle exec jekyll s
// ディレクトリを指定する場合は-sオプション
// $ bundle exec jekyll s -s hoge
```






## rbenv利用する可能なコマンド
簡単に使いかたをまとめる。

```
$ rbenv help
```

主に使用するコマンドは以下の通りです

`$ rbenv install`: Ruby の新しいバージョンをインストールします。
`$ rbenv global`: システム全体で使用するデフォルトの Ruby バージョンを設定します。
`$ rbenv local`: 現在のディレクトリ専用の Ruby バージョンを設定します。
`$ rbenv versions`: インストール済みの Ruby バージョンを一覧表示します。
`$ rbenv version`: 現在使用中の Ruby バージョンを表示します。
`$ rbenv uninstall`: Ruby バージョンをアンインストールします。

## gemのインストールと管理
`rbenv`を使う場合、それぞれのRubyバージョンごとに独立したgem環境が構築される。`gem`を使った管理は次のように実施

```bash
$ gem install bundler
```

## Railsプロジェクトでの利用
`rbenv`を使ってプロジェクトに必要なRubyバージョンを設定。Railsをインストール

```bash
$ rbenv local 3.3.6
$ gem install rails
$ rails new my_app
```

