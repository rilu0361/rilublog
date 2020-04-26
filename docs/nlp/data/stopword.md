# stop wordの除去


## 概要

邪魔な単語を削除する。
単語のリストになっていることが前提。

## 数字の除去

```py
import re
target_word = [word for word in target_word if not re.match(r'\d', word)]
```

## 小文字に統一

```py
target_word = [word.lower() for word in target_word if re.match(r'\w', word)]
```

大文字に統一したい場合は `word.upper()` 。

ただし、その他のライブラリでは小文字に統一をするほうがよく見かけるのでそれらに合わせて小文字に統一している。


## 特定単語の除去

別ファイルでストップワードを記述しておき、それを読み込んで使う。

```py
with open('/xxxx/yyyy/Japanese.txt', 'r') as f:
    stop_word_list = f.read().split('\n')

target_word = [word for word in target_word if word not in stop_word_list]
```

除去したい単語が1単語/行になっているtxtファイルを読み込みリストに変換して使った。  
以下のリンクは日本語ストップワードの辞書。  
[http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt](http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt)
