# 内包表記

## リスト内包表記

```py
hoge = [x for x in range(10)]
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```py
hoge = [x*2 for x in range(10)]
```
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

以下と同等
```py
hoge = []
for x in range(10):
    hoge.append(x*2)
```

#### 後置if

```py
hoge = [x for x in range(10) if x%2==0]
```

[0, 2, 4, 6, 8]

#### 三項演算子
`else` がある場合は三項演算子を使った書き方になるため、`if` の位置が変わることに注意

```py
hoge = [x if x%2==0 else x*10 for x in range(10)]
```
[0, 10, 2, 30, 4, 50, 6, 70, 8, 90]

```py
hoge = [x if x%2==0 else x*3 for x in range(10) if x%3==1]
```
[3, 4, 21]

以下と同等(おそらく)

```py
hoge = []
for x in range(10):
    if x%3==1:
        if x%2==0: hoge.append(x)
        else: hoge.append(x*3)
```

## ディクショナリ内包表記

```py
hoge = {i:x for i, x in zip(range(2), ['a','b'])}
```
{0: 'a', 1: 'b'}

#### key と valueの入れ替え

```py
hoge = {x:i for i, x in hoge.items()}
```
{'a': 0, 'b': 1}

## セット内包表記

```py
hoge = {x for x in [1,1,2,2,3,4,5,5]}
```
{1, 2, 3, 4, 5}

