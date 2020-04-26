# 半角全角変換

## 概要

全角から半角にしたり、半角から全角にできる。  
数字だけは半角のままという指定もできる。

自然言語処理の際には、半角と全角の違いで別語彙になってしまわないようにどちらかに統一する。

## 導入

```
pip install mojimoji
```

### 半角から全角(mojimoji.zen_to_han(text,kana= ,digit= , ascii= ))

```py
import mojimoji
zen_txt = 'いろは！アイウ、１２３。ｂｃｄ・'
text = mojimoji.zen_to_han(zen_txt,kana=False)
```

### 全角から半角(mojimoji.han_to_zen(text,kana= ,digit= , ascii= ))

```py
import mojimoji
han_text = 'いろは!ｱｲｳ、123。bcd・'
text = mojimoji.han_to_zen(han_txt,digit=False,ascii=False)
```

### 英数字を半角、日本語は全角に統一する
```py
import mojimoji
def zen_han(text: str) -> str:
    text = mojimoji.zen_to_han(text,kana=False)
    text = mojimoji.han_to_zen(text,digit=False,ascii=False)
    return text
```

## 参考

[https://github.com/studio-ousia/mojimoji](https://github.com/studio-ousia/mojimoji)

[Pythonで半角・全角の変換を高速に行う](https://qiita.com/ikuyamada/items/fea6c8f81e7cac7cf318)

