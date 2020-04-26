# Ubutnuコマンド
2019/04/27

## 頻出コマンド
最低限覚えきたいものたち。

### ls ディレクトリ・ファイルの情報の確認
```sh
ls
```
「list segments」の略らしい。知らなかった。  
オプションをつけると追加で情報が得られる。
`ls -la` は割とよく使っている。 

- 隠しファイルを確認する
```sh
ls -a
```
- 権限と最終更新日の確認
```sh
ls -l
```

### cd カレントディレクトリの移動
カレントディレクトリは現在作業しているディレクトリのこと。

```sh
cd 相対パスor絶対パス
```

- ホームディレクトリに戻る
```sh
cd
```

- 親ディレクトリに移動
```sh
cd ..
```

### pwd 現在のディレクトリの表示
```sh
pwd
```

### apt, apt-get

- パッケージのinstall
```sh
sudo apt install パッケージ名
```
- パッケージの削除
```sh
sudo apt remove パッケージ名
```
- 利用可能なパッケージ一覧の更新
```sh
sudo apt update
```
追加削除を行うときはにしておくとよい。
- パッケージの更新
```sh
sudo apt upgrade
```
- ヘルプ
```sh
apt -h
```
他にもできることはいっぱいあるので困ったらヘルプを見るのが無難。

##### apt -h の最終行
**この APT は Super Cow Powers 化されています。**  
スーパー牛さんパワーとは…
```sh
$ apt moo
                 (__) 
                 (oo) 
           /------\/ 
          / |    ||   
         *  /\---/\ 
            ~~   ~~   
..."Have you mooed today?"...
```

##### aptitude -h の最終行
**この aptitude にはスーパー牛さんパワーなどはありません。**

興味があれば
```sh
aptitude moo
aptitude -v moo
aptitude -vv moo
aptitude -vvv moo
aptitude -vvvv moo
aptitude -vvvvv moo
aptitude -vvvvvv moo
```
を上から順番にどうぞ。  
`aptitude` がない場合は`sudo apt install aptitude` でできるようになります。

#### apt-get か aptか
多くのサイトで`apt-get` コマンドが使われているのを見るが、`apt` と置き換えて良さそう。

[「apt-get」はもう古い？新しい「apt」コマンドを使ったUbuntuのパッケージ管理](https://linuxfan.info/package-management-ubuntu)

aptコマンドでやれることの説明も書かれているのでaptで困ったら見てみると良いかも。


## サーバー関連

### ssh
```sh
ssh aaa.bb.ccc.XX
```
リモートマシンにsshでログインする。
自分がやったときは何故か一度はじかれた。原因不明。もう一回やったらできたので謎。

- ユーザー名を指定する場合
```sh
ssh ユーザ名@aaa.bb.ccc.XX
```
### passwd
パスワードの変更。
現在のパスワードと，新しいパスワードx2回要求される

### scp
ファイルの転送(クライアント側で実行)
```sh
scp 転送するファイル 転送先(ユーザー名@aaa.bbb.cc.XX : 任意のディレクトリ)
```
ファイル受信(クライアント側で実行)
```sh
scp 転送するファイル(ユーザ名@aaa.bb.ccc.XX:~/(転送するファイル))  転送先
```

## NVIDIA関連
```sh
nvidia-smi
```
グラボの状況が見れる。

