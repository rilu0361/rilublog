# DataFrameのデータの参照

## 前提

```py
dic = {"drink":["tea", "coffee", "water", "cola"],
       "price" :[170, 350, 200, 420],
       "size" :["S", "L", "M", "S"]}
df = pd.DataFrame(dic)
```
- 結果
```sh
    drink  price size
0     tea    170    S
1  coffee    350    L
2   water    200    M
3    cola    420    S
```
以上のDataFrameを作った前提で以降を説明する。

## 基本

#### 列名で参照
```py
df["price"]
# df.price
```

- 結果
```sh
0    170
1    350
2    200
3    420
Name: price, dtype: int64
```

#### 列名+index

```py
df["price"][1] 
# >>> 350
```

#### スライス

```py
df[1:3]
```
- 結果
```sh
    drink  price size
1  coffee    350    L
2   water    200    M
```

#### ブール値

```py
df[df["size"]=="S"]
```

- 結果
```sh
  drink  price size
0   tea    170    S
3  cola    420    S
```

- - -
おわりー