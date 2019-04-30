# 正規表現を使う
2018/08/05



## コンパイルあり

パターンをコンパイルしておく方法が高速。

```py
import re
pattern = r"ca"
text = "caabsacasca"
repatter = re.compile(pattern)
matchOB = repatter.match(text)
```

## コンパイルなし
```py
import re
pattern = r"ca"
text = "caabsacasca"
matchOB = re.match(pattern , text)
```

パターンに `r` をつけるのは、文字列中のバックスラッシュ文字をそのままバックスラッシュとして扱えるようにするため。

## メソッド一覧

|メソッド|目的|
|:-----:|:--:|
|match(pattern, str)|文字列の先頭とマッチするか|
|search(pat, str)|文字列のどこにマッチするか|
|findall(pat, str)|マッチする部分文字列をすべて探してリストで返す|
|finditer(pat, str)|マッチする部分文字列を探し、イテレータとして返す|
|split(pat, str)|マッチする部分があるたびに分割して返す|
|sub(pat, repl, str)|マッチする部分をreplに置換|

オブジェクトから情報を取り出すための関数
|メソッド|目的|
|:-----:|:--:|
|group()|マッチした文字列を返す|
|start()|マッチした開始位置を返す|
|end()|マッチした終了位置を返す|
|span()|マッチした位置(start,end)のタプルを返す|

プロパティ
|プロパティ|意味|
|:-----:|:--:|
|ASCII,A|ASCII文字だけにマッチさせる|
|DOTALL, S|.を改行含む任意の文字にマッチするようにする|
|IGNORECASE, I|大文字小文字の区別をなくす|
|LOCALE, L|ロケールに対応したマッチングをする|
|MULTILINE, M|^, $に作用して、複数行にマッチング|
|VERBOSE, X|冗長な正規表現を利用できるようにする。|

## 日本語を扱うとき
Unicodeにしたほうがいい?
```py
matchOB = re.match(u"[ぁ-ゞ]",u"あ")
```

## 参考
[Pythonでの正規表現の使い方](https://qiita.com/wanwanland/items/ce272419dde2f95cdabc)
