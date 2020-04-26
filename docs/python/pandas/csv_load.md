# csvデータの読み込み

Pandasを利用するときには以下を記述しておく。

```py
import pandas as pd
```

## csvデータの読み込み

xlsxを読み込んでデータフレームに格納する。

```py
hoge = pd.read_csv('my_data.csv', index_col=0)
```

indexがある場合は`index_col=0` 。(0列目がindexの場合)  
`read_table()` もあるそうだが、それは`.tsv`のときに使える。  
ただ`read_csv()` で `sep=\t` にすれば(区切り文字の指定)たぶん同じ結果が得られそう。


headerがない場合は`header = None` と指定すれば、列名として数字を振ってくれる。  
`names = []` すれば、列名を任意に割り当てられる。


### 列を指定して取り出す


```py
hoge = pd.read_csv('my_data.csv', index_col=0, usecols=[2])
```
```py
hoge = pd.read_csv('my_data.csv', index_col=0, usecols=['列名'])
```
引数に `usecols` を使用するとできる。  
列名もしくは順番で指定する。  

列の複数指定もできる。その場合データフレームが返ってくる。  
列が単独指定なら、リストが返ってくるっぽい。


- - -
おわりですよー