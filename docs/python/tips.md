# ちょっとしたプログラム集

~~使うに便利な~~ちょっとしたプログラム集.  
あとでまとめ直して大幅な変更がある可能性があります。

ファイルのリストの取得
======================
特定フォルダ内のファイルリストを取得する。

```py
from pathlib import Path
DIR_PATH = Path("フォルダのパス ./path")
FILE_PATH_LIST = list(DIR_PATH.glob("*"))
```
