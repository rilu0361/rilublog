# 辞書 dictionary


## 基本

インデックスが数値ではなく、keyになったものという捉え方。
インデックスでの参照ではなくkeyによって参照する。

```py
dic = {"a":"あ","b":"い","c":"う"}
print(dic["a"])
# > `あ`
print(dic.keys())
# > dict_keys(['a', 'b', 'c'])
print(dic.values())
# > dict_values(['あ', 'い', 'う'])
print(dic.items())
# > dict_items([('a', 'あ'), ('b', 'い'), ('c', 'う')])
```

`keys()` と`values()` の返り値がリストではないことに注意。`dic.keys()[1]` では中身を参照できない。  

`items()` はタプルなのでアンパック代入ができる。
`for key, value in dic.items():` のように使えて便利。

### 辞書同士の結合
```py
dic1 = {"a":1, "b":2, "c":3}
dic2 = {"b":4, "d":5}
dic1.update(dic2)
print(dic1)
# > {'a': 1, 'b': 4, 'c': 3, 'd': 5}
```

keyが同一だと上書きされてしまうので注意。

### get()
`get(key,デフォルト値)` 
:   引数にkeyを渡して、それに対応する値を取り出す。keyがない場合はデフォルト値が入る。

例えば以下のように、単語の出現回数を数えることが簡単にできる。~~Counter()を使ったほうが簡単~~

第２引数にデフォルト値を入れることができるため、keyに存在しないものをgetに渡したとき、返す値が指定できるのは使い勝手が良い。
```py
word_cnt = {}
sent = "I have a pen I have a apple"
for word in sent.split():
    word_cnt[word] = word_cnt.get(word,0) + 1
print(word_cnt)
> {'I': 2, 'have': 2, 'a': 2, 'pen': 1, 'apple': 1}
```
`setdefault()` との違いが分からなかった記憶がある。

### 辞書の定義方法色々

```py
d1 = dict([["a",1],["b",2],["c",3]])
d2 = dict(a=1,b=2,c=3)
d3 = dict({"a":1,"b":2,"c":3})
d4 = dict(zip([a,b,c], [1,2,3]))
# > {'a': 1, 'b': 2, 'c': 3}
```


