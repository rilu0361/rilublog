# mecabをpython上で利用する
環境:Ubuntu16.04(WSL)

## mecabのインストール

```sh
sudo apt install mecab
sudo apt install libmecab-dev
sudo apt install mecab-ipadic-utf8
```
python3 バインド
```sh
pip install mecab-python3
```

## neologdのインストール
```sh
git clone https://github.com/neologd/mecab-ipadic-neologd.git
cd mecab-ipadic-neologd
sudo bin/install-mecab-ipadic-neologd
```

```sh
$ cd mecab-ipadic-neologd/
$ sudo bin/install-mecab-ipadic-neologd
```

`/etc/mecabrc` を編集。`sudo` じゃないと書き込み不可。
```py
sudo vim mecabrc
```
書き換えるものは、`dicdir = ` の箇所。
```
dicdir = /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd
```
と参考サイト上にあったが、
```sh
dicdir = /usr/lib/mecab/dic/mecab-ipadic-neologd
```
に変更。


## 参考
[ubuntu 17.04 に mecab をインストール](https://qiita.com/ekzemplaro/items/c98c7f6698f130b55d53)