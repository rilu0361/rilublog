# Anacondaによる環境構築(Win)

2018/09/27

Windows10での環境構築をベースとします。
Linux系でも流れは同じはず…。

Anacondaのインストールからjupyter notebookでプログラムが書けるようになるまでの流れです。

## インストール

Anacondaのページにいってぽちっとする。

![install](./image/anaconda_install.png)

`Anaconda3-5.2.0-Windows-x86_64.exe`
をどこに保存されるか聞かれるのでわかるところに置いておく。

チートシートほしいならEメール登録してと言われるが無視。  
入力場所じゃないところをクリックすると消える。

`Anaconda3-5.2.0-Windows-x86_64.exe` を実行する。

![exe](./image/exe.png)

next ,I agree, next... と進めていく。

![setup](./image/setup.png)

待機。

ゲージがたまったらnext

![vscode](./image/vscode.png)

vsCodeが必要なければ、とりあえずskip

![finish](./image/finish.png)

そのままfinishすると  
http://docs.anaconda.com/anaconda/user-guide/getting-started/  
と、  
https://anaconda.org/  
に飛ばされる。

anacondaの使い方（英語）とAnacondaクラウドの登録っぽいあれなので無視してもよい。  
もしくはfinishする前にチェックを外しておく。

ここまででインストールは終了。

## 起動

スタートのアプリ覧を見ると、「最近追加されたもの」にAnaconda関連のものが加わっていることが分かる。  
検索してもよい

![ret](./image/ret.png)

Anaconda Navigaterを起動する。

しばらく待って起動すると以下がでてくる。

![start](./image/start.png)

`Ok, and don't show again` する。チェックを外しても良い。

起動画面はこれ

![navi](./image/navi.png)

jupyter notebookを `Launch` (起動)する。

ブラウザが立ち上がってjupyter notebookが起動する。

![jup1](./image/jup1.png)

## jupyterの基本

### フォルダの作成

![folder](./image/folder.png)

Folderをクリックすると、  
新しく、`Untitled Folder` が作成される。  
追加されたフォルダは一番上に追加されなるわけでもなく、追加しましたって通知がくるわけでもないので注意。  
アルファベット順に見ていくと追加されているのが分かる。「U」 なので結構下の方にある。

### フォルダのソート

右上のほうの `Name`  `LastModified` などでソート順を変えることも可能。

![add_folder](./image/add_folder.png)

### リネーム

フォルダ名の変更は左上の `Rename` から行える。

変更したいフォルダにチェックをうってから `Rename` をクリック。

![rename](./image/rename.png)

フォルダ名を入力し、右下の`Rename`

![rename2](./image/rename2.png)

## pythonファイルを書く

Pythonファイルをかき始めるには
右上の `new` から `python3` を選択する。

![add_py](./image/add_py.png)

以下の画面が出てくる。

![py](./image/py.png)

タイトルの変更はUntitledの場所をクリックすればよい。もしくはフォルダ名の変更と同様のやり方で行う。

![ch_ti](./image/ch_ti.png)

## 保存してあるpython notebook(.ipynb) を読み込む

右上のuploadをクリックする。

![upload](./image/upload.png)

読み込みたいファイルを探し、開く。

![up2](./image/up2.png)

名前の変更も行える。
右の青いボタン（``Upload`` ）をクリック。

![up3](./image/up3.png)

以上で追加される。

## markdownの書き方

jupyter notebook上ではコメントを書くことができる。

![mark](./image/mark.png)
