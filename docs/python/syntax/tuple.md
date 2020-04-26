# タプル tuple

## 基本

リストと違い中身の要素の変更ができない。

```py
a = (1,2,3,4,5)
a[0] = 5 # Error
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