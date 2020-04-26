# 重複を削除する

!!! Dangar
    未検証...

```py
df = df[df.duplicated(keep='last', subset="col1") == False]
```

`keep=last` は重複しているものの最後のみを残す指定。のはず。

`subset` でリストの要素に列名を指定すれば、指定列を対象にできる。

```py
df = df[df.duplicated(keep='last', subset=["col1","col2"]) == False]
```
