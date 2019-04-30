# Gitについて
2018/04/07

## Gitとは？
バージョン管理システム。

## リポジトリとは？
ファイルとかディレクトリの状態を記録しておく場所のこと。

#### リモートリポジトリ
どっかのサーバで複数人で共有するためのリポジトリ。

#### ローカルリポジトリ
個人利用のリポジトリ。自分のPCにあるもの。

編集したりなど作業自体はローカルリポジトリで行い、公開するときはリモートリポジトリにアップする。これを **Push** という。

逆に、リモートリポジトリからファイルを取ってくることもできる。**Pull** という。

## コミットとは？
ファイルを変更したり、追加して、それをリポジトリに記録するための操作のことを**コミット**という。

コミットすると、前回と今回の情報の差分を記録したものが作成される。(**コミット または　リビジョン**)

それをたどっていくことで、過去の状態を知ることができるようになっている。

コミットには名前が付けられているため(英数字40桁)、名前を指定することでいつのコミットか指定できる。

コミット時にはメッセージを付与することが必須。

### リポジトリの作成
作業するディレクトリをGitの管理下に置く。
まずはそのディレクトリに移動して以下を実行。
```
git init
```

## ワークツリーとは？
Git管理下の、自分たちが作業するディレクトリのこと。

## インデックスとは？
ワークツリーとリポジトリの間にある場所。
ワークツリーで作業して、リポジトリに登録したものをリポジトリにコミットするという流れになる。

わざわざインデックスを通してしかリポジトリに登録できなくなっているのは、ワークツリー内の不必要のファイルをコミットしないため。

## gitのインストール
linuxなら
```
git install
```
で問題ないはず。

その後gitの設定を行う。
ユーザーのホームディレクトリに作成される`.gitconfig` ファイルに設定が書いてある。
vimかなにかで中身を直接書き換えてもいいが、コマンドラインから編集する。

```
git config --global user.name "<ユーザ名>"
git config --global user.email "<メールアドレス>"
```
gitの出力に色をつける。
```
git config --global color.ui auto
```
エイリアスの設定
例えば以下では`checkout`を`co`と省略して実行できるようにする。
```
git config --global alias.co checkout
```
Windowsで文字化けする(ファイル名が数字の羅列になる)とき
```
git config --global core.quotepath off
```

## 状態の確認
```
git status
```
によりワークツリーとディレクトリの状態を確認する。
`Untarack files`下にあるファイルは追跡対象になっていない、インデックスに登録されていないファイル。
このワークツリーにあるファイルを
```
git add <file>
```
することでインデックスに登録する。(追跡対象にする)

```
git add .
```
ですべてファイルをインデックスに登録することができる。

`Changes to be commited`に`new file`となっているものはインデックスに登録されたもの。
この状態になったところでコミットができるようになる。
コミットのコマンドは以下。
```
git commit -m "<コメント>"
```
`-m`のオプションはコメントを続けて書くためのもの。
コメントは上述した通り必須。

リポジトリの更新履歴を見るには
```
git log
```
これでコミットした情報が見れる。


## リポジトリの共有

### こちらが変更したことを反映させたい場合
ローカルリポジトリで作業したことをリモートリポジトリにPushする。
リモートリポジトリのアドレスに名前を付けて記憶できる。これは毎回長い名前を入力するのが面倒なため。
リモートリポジトリに追加するためには
```
git remote add <name> <url>
```
`<name>`は登録名、`<url>`はリモートリポジトリのURL。
プッシュ、プル時にリモートリポジトリ名を省略すると、デフォルトで`origin`を使う。
この名前はリモートリポジトリで一般的。

リモートリポジトリにプッシュする前の指定。
```
git push <repository> <refspec>
```
`<repository>`はプッシュ先のアドレス、`<refspec>`はプッシュするブランチ。

以下でリモートリポジトリにプッシュする。
```
git push -u origin master
```
`-u`をつけることで、次回以降ブランチ名を省略できる。
最初のときは省略できない。

ユーザー名とパスワードが聞かれるので答える。


### リモートリポジトリを複製して手元に欲しい場合
クローンする。

リモートリポジトリに変更があった場合はその変更内容を取り込む必要がある。
なのでPullをする。

```
git clone <repository> <directory>
```
`<repository>`はリモートリポジトリのURL、`<directory>`は服製作のディレクトリ名。
クローンしたリポジトリではpushの際の`origin master`は省略できる。