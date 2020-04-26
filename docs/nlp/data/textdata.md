# データの読み込みと保存
2019/07/14

## 概要

**読み込み**   
1. .txt ファイル１つにつき１データ(テキスト)が入っている場合  
2. .txt ファイルに改行ごとにテキストが全て入っている場合  
3. .csv ファイルの場合  
4. .xlsx ファイルの場合  

その後扱うことを考え、pandasを使ってデータフレームにする。

**保存**  
1. Pandasでデータフレームにして表形式データとして保存  
2. pickle化する

## 読み込み

読み込みについていくつか。

### 1. .txtファイル１つにつき１データ(テキスト)が入っている場合

読み込みたい.txtファイルを一つのディレクトリにまとめておく。  
そのPATHを`DIR_PATH`に入れる。

```py
from pathlib import Path
DIR_PATH = Path("絶対/相対パス")
FILE_PATH_LIST = list(DIR_PATH.glob("*"))
FILE_NAME_LIST = [str(path).split('/')[-1] for path in FILE_PATH_LIST]

text_list = []
for file_path in FILE_PATH_LIST:
    with open(file_path, 'r') as f_r:
        target = f_r.read()
    text_list.append(target)

dic = {"text":text_list}
df = pd.DataFrame(dic)
df.head()
```

上記のプログラムで、`text_list`　に各ファイルのテキストが要素のリストが手に入る。  
その後、データフレームに変換し、`df` に中身が入る。

### 2. .txt ファイルに改行ごとにテキストが全て入っている場合

読み込みたいテキストファイルを`sample.txt` とする。  
中身は以下のように1行1データ(テキスト)が入っているものとする。

```py
READ_FILE_PATH = 'sample.txt'
with open(READ_FILE_PATH, 'r') as f_r:
    text_list = f_r.readlines()

dic = {"text":text_list}
df = pd.DataFrame(dic)
df.head()
```

上記のプログラムで、`text_list`　に各ファイルのテキストが要素のリストが手に入る。  
その後、データフレームに変換し、`df` に中身が入る。

#### データ容量が大きく、一度でメモリに乗りきらない場合など
ジェネレータを使うとよいかもしれない。  
下記のプログラムは .txt の１行ずつ読みだして出力していくプログラム。

```py
def read_text_line(file_path:str) -> str:
    with open(file_path, 'r') as f_r:
        for line in f_r:
            yield line.strip("\n") # 末尾の改行を削除

lines_iter = read_text_line("sample.txt")
for line in lines_iter:
    print(line)
```

### 3. .csv ファイルの場合

pandasを使う。  
読み込み方のオプションは以下を参照のこと。  
[csvデータの読み込み](../../python/pandas/csv_load.md)

```py
import pandas as pd
df = pd.read_csv('sample.csv', index_col=0)
```

### 4. .xlsx ファイルの場合

pandasを使う。  
読み込み方のオプションは以下を参照のこと。  
[表形式データの読み込み](../../python/pandas/excel_load.md)

```py
import pandas as pd
df = pd.read_excel('sample.xlsx', index_col=0)
```

## 保存

### 1. Pandasでデータフレームにして表形式データとして保存 

オプションは以下を参照  
[表形式データの保存](../../python/pandas/save.md)

csvファイルにする。  
```py
df.to_csv("new_sample.csv")
```

excelファイルにする。 
```py
df.to_excel("new_sample.xlsx")
```

### 2. pickle化する

`text_list` を保存することにする。  
[データの保存(pickle)]("../../pandas/syntax/pickle.md")

```py
import pickle
with open('./text_list.pkl', 'wb') as f:
    pickle.dump(text_list, f)
```
