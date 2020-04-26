# janome
2019/07/12

## 概要
janomeを使って形態素解析を行うことができる。  
mecabより導入が簡単なので、ちょっと試してみるのにいいかもしれない。

## 導入

```sh
pip install janome
```
`conda install` はできなかった。

## 使い方

### 呼び出し

```py
from janome.tokenizer import Tokenizer
t = Tokenizer()
```

例文として以下を使う。

```py
s = "紅茶の飲んだ"
```

### 各情報の取得

```py
for token in t.tokenize(s):
    print(token)    
```

結果
```sh
紅茶    名詞,一般,*,*,*,*,紅茶,コウチャ,コーチャ
を      助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
飲ん    動詞,自立,*,*,五段・マ行,連用タ接続,飲む,ノン,ノン
だ      助動詞,*,*,*,特殊・タ,基本形,だ,ダ,ダ
```

以下でそれぞれ情報が取り出せる。

|情報|プログラム|
|:-:|:-:|
|表層形|token.surface|
|品詞|token.part_of_speech|
|活用型|token.infl_type|
|活用形|token.infl_form|
|基本形|token.base_form|
|読み|token.reading|
|発音|token.phonetic|

- - -

#### 表層形
```py
for token in t.tokenize(s):
    print(token.surface)
```
```sh
紅茶
を
飲ん
だ
```

#### 品詞
```py
for token in t.tokenize(s):
    print(token.part_of_speech)  
```

```sh
名詞,一般,*,*
助詞,格助詞,一般,*
動詞,自立,*,*
助動詞,*,*,*
```

#### 活用型

```py
for token in t.tokenize(s):
    print(token.infl_type)  
```

```sh
*
*
五段・マ行
特殊・タ
```

#### 活用形
```py
for token in t.tokenize(s):
    print(token.infl_form)  
```

```sh
*
*
連用タ接続
基本形
```

#### 基本形

```py
for token in t.tokenize(s):
    print(token.base_form)
```

```sh
紅茶
を
飲む
だ
```

#### 読み

```py
for token in t.tokenize(s):
    print(token.reading)
```

```sh
コウチャ
ヲ
ノン
ダ
```

#### 発音

```py
for token in t.tokenize(s):
    print(token.phonetic)
```

```sh
コーチャ
ヲ
ノン
ダ
```