# MkDocsについて

[mkdocs.org](https://mkdocs.org).

## コマンド

- 新規プロジェクトの立ち上げ
```
mkdocs new [dir-name]
```
- ローカルサーバーで確認
自動的にビルドし直してくれる
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

## navigation

サイトの構成の記述

`mkdocs.yml` に記述する

```py
site_name: 雑記
nav:
    - Home: index.md
    - About: test.md
    - test:
        - test2: test_dir/test2.md
        - test3: test_dir/test3.md
```