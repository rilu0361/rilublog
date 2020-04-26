# ファイル読み込み

`f = open(...)` でもいいが、その場合ファイル操作の最後に `f.close()` を記述する。  
`with` で作れば`close()` は不要。


## 基本

`read()` : ファイルを一括読み込み  
`readlines()` : リストに格納(1行1要素になる)  
`readline()` : 1行ずつ読み込み    


### `read()` : ファイルを一括読み込み  

```py
READ_FILE_PATH = ''
with open(READ_FILE_PATH, 'r') as f_r:
    target = f_r.read()
```

### `readlines()` : リストに格納(1行1要素)  

```py
READ_FILE_PATH = ''
with open(READ_FILE_PATH, 'r') as f_r:
    target = f_r.readlines()
```

```sh
["1行目","2行目",...,"最終行"]
```

### `readline()` : 1行ずつ読み込み  

~~使いどころがいまいち思いつかない~~

```py
READ_FILE_PATH = ''
with open(READ_FILE_PATH, 'r') as f_r:
    target = f_r.readline()
    while target:
        print(target)
        target = f_r.readline()
```

### Generator的に読み込み

メモリに乗りきらないなどの事情がある場合。  
1行ずつ読みだして処理していく。

```py
READ_FILE_PATH = './write.txt'
for sent in open(READ_FILE_PATH, 'r'):
    print(sent, end="")
```

- 結果(元ファイル通り)
```sh
1,2,3,4,5
6,7,8,9,0
```

!!! memo
    `print(xxx, end="")` でendの指定をしているのは `print()` のデフォルトで改行が入るのを防ぐため

- - -

おわり～