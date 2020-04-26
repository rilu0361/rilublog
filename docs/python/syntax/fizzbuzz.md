# fizzbuzz


## プログラム1

```py
for i in range(1,31):
    if i%3==0 and i%5==0:
        print("fizzbuzz", end=' ')
    elif i%3==0:
        print("fizz", end=' ')
    elif i%5==0:
        print("buzz", end=' ')
    else:  
        print(i, end=' ')
```
1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz fizz 22 23 fizz buzz 26 fizz 28 29 fizzbuzz 

これが一番素直。  

- `print(xxx, end='')`  
`end`はプリントの終わり文字の指定。デフォルトは改行になっている。


## プログラム2

```py
print(*['fizzbuzz' if i%3==0 and i%5==0 else "fizz" if i%3==0 else "buzz" if i%5==0 else i for i in range(1,31)])
```
1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz fizz 22 23 fizz buzz 26 fizz 28 29 fizzbuzz

三項演算子を使ったプログラム。一行で書けるが長いのがネック。

- 三項演算子  
`a = "fizz" i%3==0 else 0` のように`(Trueでの値) if (条件) else (Falseでの値)` にする。
今回はそれを連接させて書いている。

- print(*list  )   
`*` 記号はリストの要素をスペース付きの1行で出力するために使用。  
要素の間を指定したい場合は`print(*list, seq='\n')` みたくする。


## プログラム3

```py
print(*[(i%3==0)*'fizz'+(i%5==0)*'buzz' or i for i in range(1,31)])
```

1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 fizz 19 buzz fizz 22 23 fizz buzz 26 fizz 28 29 fizzbuzz

きれい。仕様が分かっていないと分からないところがある。

#### ポイント
- `or` による短絡評価  
`A or B` で`A` がFalseのとき、Aは評価されずBが評価される。

- `False`は`0`扱い  
`(i%3==0)`がFalseのとき、`0*'fizz'` をしているようなもの。 

- 文字列の繰り返し  
`2*'fizz'` が '`fizzfizz'`になるように、`0*'fizz'`は`''`

- `''`は`False`扱い  

要するに、`(i%3==0)`または`(i%5==0)`を満たない場合、`or`の左側はFalseになるので、右側`i`が出力され、条件を満たしている場合は左側の文字列(fizzとかbuzzとか)が出力されるようになっている。

- print(*list  )
`*` 記号はリストの要素をスペース付きの1行で出力するために使用。  
要素の間を指定したい場合は`print(*list, sep='\n')` みたくする。

