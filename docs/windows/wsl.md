# WSL(Windows Subsystem for Linux)の導入

2018/04/07

## 目的
Windows上でLinuxを動かしたい

## 概要
Windows上でLinuxを使おうと思ったとき、MinGWとか、Cygwinとか、仮想でやる方法が今までもあった。
しかし、2017/10/18のWindows 10 Fall Creators Updateで「Windows Subsystem for Linux（WSL）」が使えるようになったのでその導入方法を簡単に以下に示す。

詳しいことは省略。

## 導入方法

### 1.Windowsのバージョン確認
「設定」→「システム」→「バージョン情報」の 'Windowsの仕様' に書いてある バージョン が **1709** 以降であることを確認。

### 2.WSLの有効化

「設定」→「アプリ」→「アプリと機能」→関連設定「プログラムと機能」→「Windowsの機能の有効化または無効化」→「Windows Subsystem for Linux」にチェック→「OK」→ **PC再起動**

### 3.Microsoft StoreからUbuntuをインストール
Microsoft Storeを開く。
検索バーから「 **Ubuntu** 」を検索して「入手」

### 4.Ubuntuの起動
スタート画面に追加されるはずなので起動する。
ユーザー名とパスワードが聞かれるので適当に設定する。パスワードは覚えておくこと。

とりあえず以上で完了。

## 利用の際のヒント
コピーしたテキストは右クリックでペーストできる。

windows上からlinux環境の中身を弄るとlinuxが壊れることがあるそうなので注意する。

逆にlinux上からwindows上のファイルは見える。(`/mnt/`以下にcとdがある)
`mnt`はrootの下にある。（最初は `/home/ユーザー名` にいる）
```
cd /mnt/
```
でwindowsの中身が見える。

## オプション
やると便利なことなど。

### シンボリックリンクの作成
例えばwindows上によく見に行くファイルがあったとき、毎回`cd /mnt/d/hoge/fuga/piyo`と長い道順を書いていくのは面倒くさい。
そこで、ショートカット（近道）を作る。
そのために端末上で以下のコマンドを実行する。
```
ln -s 正式な道順(パス) 近道の名前(パス)
```
例えば、windows上のDドライブ下にある`home`の下にある`workspace`という名前のディレクトリへの道に`work`という名前の近道を作る場合、以下のコマンドになる。
近道を作りたいディレクトリの中で、以下を実行する。
```
ln -s /mnt/d/home/workspace work
```
以降は `cd /mnt/d/home/workspace` を `cd work` だけで中身を見にいくことができるようになるため便利。

```
ln -s /mnt/d/home/workspace ~/work
```
とすると、最初にいる場所(`/home/ユーザー名`)にシンボリックリンクが作られる。
また、場所を指定すれば、その場所にシンボリックリンクが作られる。
例えば以下のようにする。
```
ln -s /mnt/d/home/workspace /home/user/hoge/fuga
```
`hoge`の下に`fuga`という名前のシンボリックリンクが作られる。


### 日本時間(JST)に変更する
端末上で`date`と入力すると、日時が表示される。
以下を実行して日本時間に変更する。
```
sudo dpkg-reconfigure tzdata
```

### サーバーの変更
初期状態ではソフトウェアのパッケージのダウンロード元は海外にあるメインサーバーに設定されている。
それを日本サーバーに変更する。
```
sudo sed -i s%/archive%/jp.archive% /etc/apt/sources.list
```

パッケージ情報を最新の状態に更新。
```
sudo apt update
sudo apt upgrade -y
```
