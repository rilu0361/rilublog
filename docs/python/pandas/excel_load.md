# Excelデータの読み込み

Pandasを利用するときには以下を記述しておく。
```py
import pandas as pd
```

## xlsxデータの読み込み

xlsxを読み込んでデータフレームに格納する。

```py
hoge = pd.read_excel('my_data.xlsx', index_col=0)
```

indexがある場合は`index_col=0` 。(0列目がindexの場合)

headerがない場合は`header = None` と指定すれば、列名として数字を振ってくれる。
`names = []` すれば、列名を任意に割り当てられる。

## シート別に読み込み

```py
df = pd.read_excel("test.xlsx", index_col=0, sheet_name=2) # Sheet3
# df = pd.read_excel("test.xlsx", index_col=0, sheet_name="Sheet3") # これでもOK
```

`sheet_name` は0番目から始まるので、デフォルトのExcelのシート名`Sheet1`などの番号とずれるのは注意。

### 複数シートの一斉読み込み

```py
df_dict = pd.read_excel("test.xlsx", index_col=0, sheet_name=None)
```
`sheet_name=None`にする。  


```py
df_dict['Sheet1'] # Sheet1のデータフレームを参照
```
DataFrame(Sheet1つ)の中身を参照するには、`df_dict["シート名"]` のようにする。  

```py
df_dict.keys()  # key(sheet名の確認)
```
シート名を確認したい場合は上記のように。

### 列を指定して取り出す

`read_csv()` とたぶん同じ。~~確認してない~~

```py
hoge = pd.read_excel('my_data.xlsx', index_col=0, usecols=[2])
```
```py
hoge = pd.read_excel('my_data.xlsx', index_col=0, usecols=['列名'])
```
引数に `usecols` を使用するとできる。
列名もしくは順番で指定する。

列の複数指定もできる。その場合データフレームが返ってくる。
列が単独指定なら、リストが返ってくるっぽい。


- - -
おわりですよー