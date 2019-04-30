# 型注釈

python3.5以降

[PEP484 Type Hints](https://www.python.org/dev/peps/pep-0484/)

型が明示されていなくて辛い思いをしたので、今後はある程度型ヒントを書きたいと思いました。

## 関数の引数の型のアノテーション

```py
def hoge(a: int, b:int , name:str) -> str:
    c = a + b
    print(name, c)
    return name
```

~~なんだこの関数~~  
`(a:int, b:int, name:str)` が `a, b` が `int`, `name`が`str` であることを明示している。  
`-> str` が `return` で返すものの型。
特に強制力があるわけではない。

## コメントに型を書いておく

https://www.python.org/dev/peps/pep-0484/#type-comments

構文としてサポートされているわけではないので、現状特に意味はないが、書くのであれば公式に従っておくのがよさそう。

公式より引用
```py
x = []                # type: List[Employee]
x, y, z = [], [], []  # type: List[int], List[int], List[str]
x, y, z = [], [], []  # type: (List[int], List[int], List[str])
a, b, *c = range(5)   # type: float, float, List[float]
x = [1, 2]            # type: List[int]
```

for文
```py
for x, y in mylist:  # type: int, int
    print(x + y)
```


## 参考

[Pythonではじまる、型の世界](https://qiita.com/icoxfog417/items/c17eb042f4735b7924a3)

[PEP484 Type Hints](https://www.python.org/dev/peps/pep-0484/)
