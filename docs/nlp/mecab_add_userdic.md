## mecabのユーザー辞書追加方法
環境はubuntu16.04(WSL)

## 参考

[単語の追加方法(公式)](https://taku910.github.io/mecab/dic.html)
公式のはたぶんwindowsでのやり方なので、下のサイトを見てファイルの場所の読み替えをする。
[Ubuntu 16.04 LTS での MeCab の辞書の場所と確認](https://obel.hatenablog.jp/entry/20170218/1487418388)
> 辞書の場所
ここです。
`/var/lib/mecab/dic`
実は以下の設定ファイルに書いてあります。これは Mroonga などでも使われます。
`/etc/mecabrc`

## やったこと

任意のフォルダに辞書を作成する。  
Excelで作るなら保存するときに **utf-8** の **csv** にする。  
作成方法は[単語の追加方法(公式)](https://taku910.github.io/mecab/dic.html)のエントリーがどうとか書いてあるところに。  
コストは小さいほど出現しやすいらしいので1とした。  
左文脈IDと右文脈IDに関しては空にしておけば勝手につけてくれるらしい。

```sh
$ /usr/lib/mecab/mecab-dict-index -d /usr/lib/mecab/dic/mecab-ipadic-neologd -u my_dic.dic -f UTF-8 -t UTF-8 my_dic.csv
reading my_dic.csv ... 40
emitting double-array: 100% |###########################################|

done!
```
辞書を変える際には `mecabrc` を編集し、`user_dic = ` に作成したユーザー辞書のパスを記載する。

`/etc/mecabrc` のオリジナル
```sh
;
; Configuration file of MeCab
;
; $Id: mecabrc.in,v 1.3 2006/05/29 15:36:08 taku-ku Exp $;
;
dicdir = /usr/lib/mecab/dic/mecab-ipadic-neologd

; userdic = /home/foo/bar/user.dic

; output-format-type = wakati
; input-buffer-size = 8192

; node-format = %m\n
; bos-format = %S\n
; eos-format = EOS\n
```

`/etc/mecabrc` の変更後
```sh
;
; Configuration file of MeCab
;
; $Id: mecabrc.in,v 1.3 2006/05/29 15:36:08 taku-ku Exp $;
;
dicdir = /usr/lib/mecab/dic/mecab-ipadic-neologd

userdic = /mnt/f/home/user_dict/my_dic.dic

; output-format-type = wakati
; input-buffer-size = 8192

; node-format = %m\n
; bos-format = %S\n
; eos-format = EOS\n
```

動作確認してできていればOK。
