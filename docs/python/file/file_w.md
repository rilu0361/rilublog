# ファイル書き込み

`f = open(...)` でもいいが、その場合ファイル操作の最後に `f.close()` を記述する。  
`with` で作れば`close()` は不要。


## 基本

```py
WRITE_FILE_PATH = './test.txt'
with open(WRITE_FILE_PATH, 'w') as f_w:
    f_w.write("紅茶が飲みたい")
```

- 結果
```sh
紅茶が飲みたい
```

追記の場合は`a`,上書きの場合は`w`


## リストの書き込み(改行つき)

```py
WRITE_FILE_PATH = './write.txt'
docs = ["紅茶が飲みたい",
        "緑茶が飲みたい"]
docs = '\n'.join(docs)
with open(WRITE_FILE_PATH, 'w') as f_w:
    f_w.write(docs)
```

リストを `\n` で結合したのちに、普通に書き込めばよい。

- 結果
```sh
紅茶が飲みたい
緑茶が飲みたい
```

### おまけ

`writelines()` でリストを扱うことはできるが、自動的に改行を入れてくれないので若干不便。

```py
WRITE_FILE_PATH = './test.txt'
docs = ["紅茶が飲みたい",
        "緑茶が飲みたい"]
with open(WRITE_FILE_PATH, 'w') as f_w:
    f_w.writelines(docs)
```

- 結果
```sh
紅茶が飲みたい緑茶が飲みたい
```

## もっとおまけ～
中身がリスト、その中身が数字のとき。  
`str` しか書き込めないので注意。

```py
WRITE_FILE_PATH = './write.txt'
vecs = [[1,2,3,4,5],
        [6,7,8,9,0]]

with open(WRITE_FILE_PATH, 'w') as f_w:
    for vec in vecs:
        vec = [str(num) for num in vec]
        vec = ','.join(vec)
        f_w.writelines(vec)
        f_w.write("\n")
```

- 結果
```sh
1,2,3,4,5
6,7,8,9,0
```  


- - -
おわり～