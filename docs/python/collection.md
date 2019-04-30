# コレクション

シーケンス型：リスト、タプル

マップ型：ディクショナリ


## リスト list
[start, stop, step] で参照可能。
stopまで含まないことに注意。
```py
a = [1,2,3,4,5]
print(a[0])
# > 1
print(a[-2])
# > 4
print(a[1:2])
# > [2]
print(a[2:4])
# > [3,4]
print(a[3:])
# > [4,5]
print(a[:2])
# > [1,2]
print(a[::2])
# > [1,3,5]
a[0] = 9
print(a)
# > [9,2,3,4,5]
```

### 追加・結合

```py
a = [1,2,3,4,5]
a.append(6)
print(a)
# > [1,2,3,4,5,6]
```

```py
a = [1,2,3]
print(a+[10,20])
# > [1, 2, 3, 10, 20]
```

`extend()` や `appned()` はリスト自体を変更してしまい何も返さないことに注意。

```py
a.extend([20,30])
print(a)
# > [1, 2, 3, 20, 30]
```

### 複製して結合

```py
print([1,2,3]*3)
# > [1,2,3,1,2,3,1,2,3]
```

### 末尾を指定
`-` (マイナス)を指定すると後ろから取り出せる。
```py
a = [1,2,3,4,5]
print(a[-2])
# > 4
```

### スライス

リストで返ってくる。[start:stop:step]でstopを含ま **ない** ことに注意。

```py
a = [1,2,3,4,5]
print(a[1:2],a[2:4],a[3:],a[:2],a[::2])
# > [2] [3,4] [4, 5] [1, 2] [1,3,5]
```

### 削除
```py
a = [1,2,3,4,5]
del a[2]
print(a)
# > [1,2,4,5]
```

### 要素の検索
```py
a = "hoge" in ["hoge","fuga", "piyo"]
print(a)
# > True
```

### ソート

```py
a = ['a','C','B','b','c','A']
a.sort()
print(a)
# > ['A', 'B', 'C', 'a', 'b', 'c']
```
key が指定できる。  
keyにlamda関数を使うことも。
```py
a = ['a','C','B','b','c','A']
a.sort(key=lambda hoge:hoge.lower())
print(a)
# > ['a', 'A', 'B', 'b', 'C', 'c']
```

## タプル tuple

リストと違い中身の要素の変更ができない。

```py
a = (1,2,3,4,5)
a[0] = 2 # 書き換えようとするがエラーになる
# > Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
print(a[0])
# > 1
```

タプルはそのままディクショナリのキーにできるがリストはキーにできない。
```py
dic = {(0,1) : "ああああ"
      (0,2,3) : "いいいいい"}
```


## 集合 set
集合なので、順序なし、重複なし。
順序がないので、インデックスでの参照もできない。

```py
a = {1,1,3,4,5,5}
print(a)
# > {1,3,4,5}
```

`add()` : 追加
`remove()` : 削除
`union()` : 和集合
`intersection()` : 共通集合
`differrence()` : 差集合
`symmetric_difference()` : 対照的差集合(両方共にないもの?)
算術演算子でも挙動は同じ。

```py
s = {1,2,3,4}
s.add(5)
print(s)
# > {1,2,3,4,5}
s2 = {2,3,7,'4'}
print(s | s2, s.union(s2))
# > {1, 2, 3, 4, 5, '4', 7} {1, 2, 3, 4, 5, '4', 7}
print(s & s2, s.intersection(s2))
# > {2, 3} {2, 3}
print(s - s2, s.difference(s2))
# > {1, 4, 5} {1, 4, 5}
print(s ^ s2, s.symmetric_difference(s2))
# > {1, '4', 4, 5, 7} {1, '4', 4, 5, 7}
```

## 辞書 dictionary

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
：  引数にkeyを渡して、それに対応する値を取り出す。keyがない場合はデフォルト値が入る。

例えば以下のように、単語の出現回数を数えることが簡単にできる。~~Counter()を使ったほうが簡単~~

```py
word_cnt = {}
sent = "I have a pen I have a apple"
for word in sent.split():
    word_cnt[word] = word_cnt.get(word,0) + 1
print(word_cnt)
> {'I': 2, 'have': 2, 'a': 2, 'pen': 1, 'apple': 1}
```
`setdefault()` との違いが分からない。

### 辞書の定義方法色々

```py
d1 = dict([["a",1],["b",2],["c",3]])
d2 = dict(a=1,b=2,c=3)
d3 = dict({"a":1,"b":2,"c":3})
d4 = dict(zip([a,b,c], [1,2,3]))
# > {'a': 1, 'b': 2, 'c': 3}
```


