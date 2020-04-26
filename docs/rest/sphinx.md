# sphinxによるwebページの公開

2019/4/1

sphinxでドキュメントを生成し、github pagesを利用してwebページの公開までの流れです。  
sphinxはpython製のドキュメント生成ツール。基本的にreST(reStructuredText)で記述していく。

~~なお本サイトはsphinxを使用していない模様~~  
→ [mkdocsによるwebページの公開](../markdown/mkdocs.md)

## install

    conda install sphinx

## プロジェクト作成

プロジェクトフォルダの作成

    mkdir myweb
    cd myweb

`sphinx-quickstart` によりプロジェクトを作成する。

    sphinx-quickstart

以上を実行し各種質問に答えていく。
長いので割愛するが ~~基本何も考えずに~~ Enterしていく。
記述するのは以下

- > Separate source and build directories (y/n) [n]: y
- > Author name(s): <著者名>
- > Project language [en]: ja

github-pagesで公開する場合は `.nojekyll` ファイルが必要らしいので、そうする場合は

- > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: y

回答し終えると以下のファイルたちができている。

    $ tree
    .
    ├── Makefile
    ├── build
    ├── make.bat
    └── source
        ├── _static
        ├── _templates
        ├── conf.py
        └── index.rst


## コンテンツの作成

`source` 以下にある `.rst` を参照してHTMLが作成されるので、それを弄っていく。

reSTの記法については最低限まとめたつもりなので
[rest基本構文](fund.md) などに書いてあるので参考にどうぞ。

## 目次の書き方

最初のページは `index.rst` となる。
例えばこの中で、

    .. toctree::
        :maxdepth: 4
        :caption: Rest

        ./documents/doc

とすると `documents` フォルダ内にある `doc.rst` のリンクが作成される。

オプションとして

- maxdepth : 層をどこまで参照し表示するか
- numberes : セクションのナンバリング
- caption  : キャプション
- titlesonly : タイトルのみ
- glob : 例えば `./documents/*` とすれば `documents` フォルダ内の全てのファイルが参照できる
- reversed : 逆順にできる

## テーマの変更

デザインテーマは `source/conf.py` を書き換える。

基本的には

```py
    html_theme = 'classic'
```

の部分を変更すれば良い。いくつかテーマが用意されているのでその中から選ぶのが簡単。

- 組み込みのテーマを使う

以下を参考に変更  
[HTMLテーマのサポート — Sphinx 1.4.4 ドキュメント](https://docs.sphinx-users.jp/theming.html#using-a-theme)

- sphinx_rtd_themeを使用する場合

個人的にはkeras documentationでおなじみのテーマ

    $ conda install sphinx_rtd_theme

```py
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
```

[GitHub - rtfd/sphinx_rtd_theme: Sphinx theme for readthedocs.org](https://github.com/rtfd/sphinx_rtd_theme)


## HTMLファイルの作成

    $ make html

をすると、 `build/` 以下にたくさんのファイルができる。
htmlファイルを確認すればできているはず。

## github pagesを利用した公開

githubのアカウントを作成していることが前提。

1. リポジトリの作成

github上でweb公開用のリポジトリを作成する。  
作り方は公式のを見たほうが早そう。
https://pages.github.com/

2. githubへのpush

`build/html` に移動しておく。  
あとは細かいことはさておき、とりあえず以下のように。

    git init
    git add --all
    git commit -m "first commit"
    git remote add origin https://github.com/アカウント名/アカウント名.github.io.git
    git push -u origin master

修正・追加して更新したいときは同じように `build/html` で以下のコマンドを実行。

    git add --all
    git commit -m "<コミットメッセージ>"
    git push -u origin master

を繰り返せば良い。

!!! WARNING
    githubへのpushの仕方は本当に必要最低限のやり方です。ご注意を。


## 参考

[sphinx でドキュメント作成からWeb公開までをやってみた - Qiita](https://qiita.com/kinpira/items/505bccacb2fba89c0ff0)
