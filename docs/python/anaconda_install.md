# Anacondaによる環境構築(Win)

2018/09/27

Windows10での環境構築をベースとします。
Linux系でも流れは同じはず…。

Anacondaのインストールからjupyter notebookでプログラムが書けるようになるまでの流れです。

## インストール

Anacondaのページにいってぽちっとする。

.. image:: ./image/anaconda_install.png
    :align: center

``Anaconda3-5.2.0-Windows-x86_64.exe``
をどこに保存されるか聞かれるのでわかるところに置いておく。

| チートシートほしいならEメール登録してと言われるが無視。
| 入力場所じゃないところをクリックすると消える。

``Anaconda3-5.2.0-Windows-x86_64.exe`` を実行する。

.. image:: ./image/exe.png
    :align: center

next ,I agree, next... と進めていく。

.. image:: ./image/setup.png
    :align: center

待機。

ゲージがたまったらnext

.. image:: ./image/vscode.png
    :align: center

vsCodeが必要なければ、とりあえずskip

.. image:: ./image/finish.png
    :align: center

| そのままfinishすると
| `http://docs.anaconda.com/anaconda/user-guide/getting-started/ <http://docs.anaconda.com/anaconda/user-guide/getting-started/>`_
| と、
| `https://anaconda.org/ <https://anaconda.org/>`_
| に飛ばされる。

| anacondaの使い方（英語）とAnacondaクラウドの登録っぽいあれなので無視してもよい。
| もしくはfinishする前にチェックを外しておく。

| ここまででインストールは終了。

起動
=======

スタートのアプリ覧を見ると、「最近追加されたもの」にAnaconda関連のものが加わっていることが分かる。

検索してもよい

.. image:: ./image/ret.png
    :align: center

Anaconda Navigaterを起動する。

しばらく待って起動すると以下がでてくる。

.. image:: ./image/start.png
    :align: center

``Ok, and don't show again`` する。チェックを外しても良い。

起動画面はこれ

.. image:: ./image/navi.png
    :align: center

jupyter notebookを ``Launch`` (起動)する。

ブラウザが立ち上がってjupyter notebookが起動する。

.. image:: ./image/jup1.png
    :align: center

jupyterの基本
==============

フォルダの作成
------------------

.. image:: ./image/folder.png
    :align: center

| Folderをクリックすると、
| 新しく、``Untitled Folder`` が作成される。
| 追加されたフォルダは一番上に追加されなるわけでもなく、追加しましたって通知がくるわけでもないので注意。
| アルファベット順に見ていくと追加されているのが分かる。「U」 なので結構下の方にある。


フォルダのソート
-----------------

| 右上のほうの ``Name``  ``LastModified`` などでソート順を変えることも可能。

.. image:: ./image/add_folder.png
    :align: center

リネーム
----------

| フォルダ名の変更は左上の ``Rename`` から行える。

| 変更したいフォルダにチェックをうってから ``Rename`` をクリック。

.. image:: ./image/rename.png
    :align: center

フォルダ名を入力し、右下の`Rename`

.. image:: ./image/rename2.png
    :align: center

pythonファイルを書く
-----------------------

Pythonファイルをかき始めるには
右上の ``new`` から ``python3`` を選択する。

.. image:: ./image/add_py.png
    :align: center

以下の画面が出てくる。

.. image:: ./image/py.png
    :align: center

タイトルの変更はUntitledの場所をクリックすればよい。もしくはフォルダ名の変更と同様のやり方で行う。

.. image:: ./image/ch_ti.png
    :align: center

保存してあるpython notebook(.ipynb) を読み込む
====================================================

右上のuploadをクリックする。

.. image:: ./image/upload.png
    :align: center

読み込みたいファイルを探し、開く。

.. image:: ./image/up2.png
    :align: center

名前の変更も行える。
右の青いボタン（``Upload`` ）をクリック。

.. image:: ./image/up3.png
    :align: center

以上で追加される。

markdownの書き方
====================

jupyter notebook上ではコメントを書くことができる。

.. image:: ./image/mark.png
    :align: center
