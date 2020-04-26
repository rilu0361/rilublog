# 集合 set

集合なので、順序なし、重複なし。
順序がないので、インデックスでの参照もできない。

```py
a = {1,1,3,4,5,5}
print(a)
# > {1,3,4,5}
```

### 関数
`add()` : 追加  
`remove()` : 削除  
`union()` : 和集合  
`intersection()` : 共通集合  
`differrence()` : 差集合  
`symmetric_difference()` : 対照的差集合(両方共にないもの?)

算術演算子でも挙動は同じ（以下）

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