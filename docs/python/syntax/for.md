
# 繰り返し for, while



## for 

`for 変数 in イテレータ:` という形。

## 基本
`in` の後はリスト等のシーケンス。
```py
for i in [1,2,3,4,5]:
    print(i, end=" ")
```

```sh
1 2 3 4 5
```

## ループを抜け出す

### 終了 break
`break` : ループを終了してループを終える。

```py
for i in [1,2,3,4,5]:
    if i == 3:
        break
    print(i, end=" ")
```
```sh
1 2
```

### 先頭に戻る continue

`continue` : ループを終了してループの先頭に戻る。

```py
for i in [1,2,3,4,5]:
    if i == 3:
        continue
    print(i, end=" ")
```
```sh
1 2 4 5
```

## range(開始, 終了, step)

**終了位置は含まない。** 開始とstepはオプション。
終了だけ指定すればOK。
```py
for i in range(10,20,2):
    print(i, end=" ")
> 10 12 14 16 18
```