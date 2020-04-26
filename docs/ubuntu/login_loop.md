# Ubuntuでログインループにはまったときの対処
2018/07/26

## 状況
- Ubuntu18.04LTSをインストール
- NVIDIA GeForce 1080ti を搭載済み

ログイン画面までいって、パスワードを打ってログインしようとするがループしてしまう。

## 結論
たぶんグラフィックドライバーが悪い。

## 確認

```sh
dpkg -l | grep nvidia
```
インストール済みのnvidiaドライバのバージョンを調べる。

## 対処法
 
ログイン画面で ++ctrl+alt+f1++ を押すとCUIのログイン画面に移る。  
CUI画面からGUI画面に戻るときも同様のコマンド。

CUI画面で指示に従って、ユーザー名、パスワードを打ち込みログインする。

そこから以下を順に実行する。

```sh
sudo add-apt-repository ppa:xorg-edgers/ppa
sudo add-apt-repository ppa:graphics-drivers/ppa
```
PPA(パーソナル・パッケージ・アーカイブ)をダウンロードしてくる。  
~~よく分かっていないが、もしかしたら片方だけでいいのかも。~~

PPAについて知りたければ以下。
[PPA(Personal Package Archive)の概要](https://help.launchpad.net/Packaging/PPA)

```sh
sudo apt-get update
```
とりあえずupdateはしておく。

```sh
sudo apt-cache search 'nvidia-[0-9]+$'
```
```sh
・・・
nvidia-331 - Transitional package for nvidia-331
nvidia-340 - NVIDIA binary driver - version 340.96
nvidia-346 - Transitional package for nvidia-346
nvidia-352 - NVIDIA binary driver - version 352.63
nvidia-367 - NVIDIA binary driver - version 367.35
・・・
```
インストールできる一覧が表示されるので、最新のものの数字を覚えておく。  
(2018/07/26現在 nvidia-390)

```sh
sudo apt-get install nvidia-xxx
```
xxx の場所に390のようにインストールしたいバージョンの数字を入れる。

```sh
sudo apt-get install mesa-common-dev
sudo apt-get install freeglut3-dev
```
必要なのか不明。どっちもOpenGL関係っぽい?  
特に２つ目のはできなかったらスルーでいいらしいとか…

最後、再起動するか  
`sudo reboot`
で読み直して、GUIログイン画面からログインしてみる。
