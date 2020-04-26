# 書き込み・保存

- 前提  
Pandasを利用するときには以下を記述しておく。
```py
import pandas as pd
```

## CSVファイルとして保存
データフレームをcsvなどに保存できる。
基本。
```py
df.to_csv("hoge.csv")
```

## Excelファイルとして保存
excelへの書き込みにも対応している。
csvでエンコードをどうにかしてExcelで見るよりもこっちのほうが圧倒的に楽。

```py
df.to_excel('hoge.xlsx', sheet_name='Sheet1')
```

ただし、`openpyxl` が必要。

```sh
pip install openpyxl
```

## 例
リストからのデータフレーム化も含め以下に例を記載

```py
import pandas as pd
data = {"key1" : value1,
        "key2" : value2,
        "key3" : value3}
df = pd.DataFrame(data)
df.to_excel('test.xlsx', sheet_name='Sheet1')
df.to_csv('./test.csv')
```

## 追記事項?

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

- - -
おわりですー