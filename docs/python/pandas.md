# Pandas

工事中…

Pandasを利用するときには以下を記述しておく。
```py
import pandas as pd
```

## csvデータの読み込み
csvを読み込んでデータフレームに格納する。
```py
hoge = pd.read_csv('my_data.csv', index_col=0)
```
indexがある場合は`index_col=0` 。
`read.table()` もあるそうだが、それは区切り文字がタブの場合(.tsv)に使用する。
でも、`read_csv()` でも `sep=` で指定してあげればできるはず（区切り文字の指定）。

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

## 書き込み(保存)
データフレームをcsvなどに保存できる。
基本。
```py
df.to_csv("hoge.csv")
```
保存をする際にエンコーディングなどの指定が可能。
```py
f.to_csv("hoge.tsv", encoding="shift_jis",sep='\t',index='False')
```
その他オプション
`sep` : 区切り文字の指定。デフォルトは `,`
`index` : 行名を入れるかどうか。デフォルトは `True`

Windows環境でExcelを開く予定がある場合、デフォルトだと文字化けを起こす。
タブ区切りUTF-16を指定するとうまくいった気がする。
```py
df.to_csv("hoge.csv",encoding="UTF-16",sep='\t')
```

### Excelファイルとして保存
excelへの書き込みにも対応している。
```
df.to_excel('document.xlsx', sheet_name='Sheet1')
```
ただし、`openpyxl` が必要。
```sh
pip install openpyxl
```

### 例
リストからのデータフレーム化も含め以下に例を記載
```py
# 保存
import pandas as pd
data = {"id" : id_list,
        "title" : title_list}
w_df = pd.DataFrame(data)
w_df.to_excel('document.xlsx', sheet_name='Sheet1')
print("excelへの書き込みを完了しました")
w_df.to_csv('document.csv')
print("csvへの書き込みを完了しました")
```

例2)
```py
import pandas as pd
data = {"key1" : value1,
        "key2" : value2,
        "key3" : value3}
df = pd.DataFrame(data)
    
df.to_csv('./csv_data.csv')
```

## 重複を削除する

```py
df = df[df.duplicated(keep='last', subset="query") == False]
```



