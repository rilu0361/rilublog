# Ubuntu設定関連
更新:2019/04/27

## フォルダの日本語化
2018/11/21

端末を開いて
```sh
LANG=C xdg-user-dirs-gtk-update
```
すると、  
「Update standard folders to current language?」  
と書かれたホームディレクトリの名前を変更するための画面が表示される。

「Update Names」を選択すると英語のディレクトリ名に変更できる。

このとき、対象のフォルダの中に何らかのファイルが入っていると、
そのフォルダは残り、新しくフォルダができることに注意。

なので、起動した直後にやることをおすすめする。

## 時間をJSTに変更する
端末上で `date` をうつと、日時が表示されるが日本時間ではないので、
```
sudo dpkg-reconfigure tzdata
```
でなにか画面がでてくるので、AsiaからTokyoを選択。

## サーバーの変更
デフォルトではソフトウェアパッケージのダウンロード元が海外にあるメインサーバーに設定されているので日本サーバーに変更する。
```
sudo sed -i 's/\/archive\.ubuntu/\/jp\.archive\.ubuntu/' /etc/apt/sources.list

sudo sed -i -e 's%http://.*.ubuntu.com%http://ftp.jaist.ac.jp/pub/Linux%g' /etc/apt/sources.list
```
以下のコマンドででパッケージ情報を最新の状態に更新
```
sudo apt update
```
そして、以下のコマンドを実行すれば、バージョンの古いパッケージが新しいものに更新
```
sudo apt upgrade -y
```

## 日本語ロケールに設定
日本語ロケールにしていると、なんか色々上手くいかないという話も聞くので微妙という話もあるが…。

Ubuntuを日本語でPCにインストールした場合と同じように、コマンドの出力を日本語に変える。
以下のコマンドで「language-pack-ja」パッケージをインストール。
```
sudo apt install -y language-pack-ja
```
以下のコマンドで「locale」を更新
```
sudo update-locale LANG=ja_JP.UTF-8
```
英語に戻したいときは
```
sudo update-locale LANG=en_US.UTF8
```
Ubuntuを再起動するとできてるはず。`date`などで確認できる

