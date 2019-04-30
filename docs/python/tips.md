# ちょっとしたなにか


## バージョンの確認
```py
import sys
s = "バージョン：{0.version}".format(sys)
print(s)
# > バージョン：3.6.4 (default, Mar 13 2018, 08:59:38)
# [GCC 5.4.0 20160609]
```

## 1行で書く
文末に`;` をつけても問題ない。
改行扱いになるので、短いものを1行にまとめて綺麗にできそうだが、あまりやっているのを見かけたことはない。

```py
print("a"); print("b"); print("c")
# > a
# > b
# > c
```



## ファイルのリストの取得

特定フォルダ内のファイルリストを取得する。

```py
from pathlib import Path
DIR_PATH = Path("フォルダのパス ./path")
FILE_PATH_LIST = list(DIR_PATH.glob("*"))
```