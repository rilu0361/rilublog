# MeCabを使用する

形態素解析。  
環境構築に関しては[mecabをpython上で利用する](mecab.md)を参照してください。  
ユーザー辞書の追加に関しては[mecabのユーザー辞書追加方法](mecab_add_userdic.md)を見てください。

## 分かち書き
単語ごとに分割する。
```py
import MeCab
mecab = MeCab.Tagger("-Owakati")

def wakati(text : str) -> list[str]:
    text = mecab.parse(str(text))
    return text.split()

print(wakati("今日の天気は雨です。"))
```

```sh
$ python test.py 
['今日', 'の', '天気', 'は', '雨', 'です', '。']
```

!!! WARNING
    neologdを使うときなどは、Mecab.Tagger("-d /usr/lib/mecab/dic/mecab-ipadic-neologd")
    などとする。pathはneologdのインストール先次第で変更する必要あり。

## 各単語の情報の出力

```py
import MeCab
mecab = MeCab.Tagger("-Ochasen")
mecab.parse("")
def node_feature(text: str) -> None:
    node = mecab.parseToNode(text)
    while node:
        print(node.feature)
        node = node.next

node_feature("今日も雨が降っています。")
```
実行結果
```sh
$ python test.py 
BOS/EOS,*,*,*,*,*,*,*,*
名詞,副詞可能,*,*,*,*,今日,キョウ,キョー
助詞,係助詞,*,*,*,*,も,モ,モ
名詞,一般,*,*,*,*,雨,アメ,アメ
助詞,格助詞,一般,*,*,*,が,ガ,ガ
動詞,自立,*,*,五段・ラ行,連用タ接続,降る,フッ,フッ
助詞,接続助詞,*,*,*,*,て,テ,テ
動詞,非自立,*,*,一段,連用形,いる,イ,イ
助動詞,*,*,*,特殊・マス,基本形,ます,マス,マス
記号,句点,*,*,*,*,。,。,。
BOS/EOS,*,*,*,*,*,*,*,*
```

## 特定の品詞のみを抜き出す.

名詞と動詞のみを**表層形**で抜き出す。  
基本形で抜き出したい場合はコメントアウトを抜けば良い。
```py
import MeCab
mecabTagger = MeCab.Tagger("-Ochasen")
def me_parse(text: str) -> list:
    word_list = []
    node = mecabTagger.parseToNode(text)
    while node:
        word = node.surface # 表層形
        # word = node.feature.split(",")[6] # 基本形
        hinshi = node.feature.split(",")[0] # 品詞
        if hinshi == '名詞' or hinshi == '動詞':
            word_list.append(word)
        node = node.next
    return word_list # リストにして返す 

print(me_parse("今日も雨が降っています。"))
```
実行結果
```sh
$ python test.py 
['今日', '雨', '降る', 'いる']
```




