# MkDocsについて
2019/04/27

## 環境構築
```sh
pip install mkdocs
pip install mkdocs-material
pip install python-markdown-math
pip install fontawesome_markdown
pip install mdx_unimoji
```
上から

- mkdocsのインストール
- マテリアルデザインのインストール
- 数式の表示
- webアイコンフォント
- 絵文字

のためのものです。
必要なものはinstallしましょう。

## 最低限の流れ
1. 環境構築　→　[環境構築](#環境構築)
2. プロジェクトの立ち上げ
```sh
mkdocs new myweb
```
3. 移動
```sh
cd myweb
```
確認
```sh
tree
.
├── docs
│   └── index.md
└── mkdocs.yml

1 directory, 2 files
```
4. ビルド
```sh
mkdocs build
```
確認
```sh
$ tree
.
├── docs
│   └── index.md
├── mkdocs.yml
└── site
    ├── 404.html
    ├── css
    │   ├── base.css
    │   ├── bootstrap-custom.min.css
    │   └── font-awesome.min.css
    ├── fonts
    │   ├── fontawesome-webfont.eot
    │   ├── fontawesome-webfont.svg
    │   ├── fontawesome-webfont.ttf
    │   ├── fontawesome-webfont.woff
    │   ├── fontawesome-webfont.woff2
    │   ├── glyphicons-halflings-regular.eot
    │   ├── glyphicons-halflings-regular.svg
    │   ├── glyphicons-halflings-regular.ttf
    │   ├── glyphicons-halflings-regular.woff
    │   └── glyphicons-halflings-regular.woff2
    ├── img
    │   ├── favicon.ico
    │   └── grid.png
    ├── index.html
    ├── js
    │   ├── base.js
    │   ├── bootstrap-3.0.3.min.js
    │   └── jquery-1.10.2.min.js
    ├── search
    │   ├── lunr.js
    │   ├── main.js
    │   ├── search_index.json
    │   └── worker.js
    ├── sitemap.xml
    └── sitemap.xml.gz
```

5. ローカルサーバーでの確認
```sh
mkdocs serve
```
以下が表示される。
```sh
INFO    -  Building documentation... 
INFO    -  Cleaning site directory 
[I 190427 17:21:13 server:298] Serving on http://127.0.0.1:8000
[I 190427 17:21:13 handlers:59] Start watching changes
[I 190427 17:21:13 handlers:61] Start detecting changes
```
`http://127.0.0.1:8000` を開いてみる。  
**Welcome to MkDocs** のページが出てきたらOK。

6. カスタマイズ
webサイトのテーマの変更など。`mkdocs.yml` を編集する。

7. 記事の追加
`doc/` 以下に`.md` ファイルの記事を追加していく。  
追加した記事は`mkdocs.yml` にファイル名を記述していく。

以下4以降繰り返し…

## mkdocsのコマンド

- 新規プロジェクトの立ち上げ
```
mkdocs new [dir-name]
```
- ローカルサーバーで確認
ローカルサーバーを起動している間は、編集して保存すると自動的にビルドし直してくれる。
ここでwebページの見た目の確認を行う。
```
mkdocs serve
```
- ビルドする
```sh
mkdocs build
```
- ヘルプを見る
```sh
mkdocs help
```
- githubでのデプロイ

```sh
mkdocs gh-deploy
```

## サイトの構成

サイトの構成の記述

`mkdocs.yml` に記述する。  
`docs`以下の記事のパスを記述していく。

```py
site_name: webサイトの名前
nav:
    - Home: index.md
    - About: about.md
    - test:
        - test2: test_dir/test2.md
        - test3: test_dir/test3.md
```

## テーマ（デザイン）の決定
組み込みのテーマを使うと便利。
マテリアルデザインに変更する場合は以下。
```yml
theme:
  name: 'material'
```
Readthedocsを使う場合は
```yml
theme: readthedocs
```


## 参考
[MkDocsによるドキュメント作成](https://qiita.com/mebiusbox2/items/a61d42878266af969e3c)
