# ディレクトリの作成

## 基本

```py
os.makedirs(DIR_NAME, exist_ok=True)
```

`exist_ok=False` で、すでに存在する場合はエラーを返す。
`exist_ok=True` で、存在していても続行する。  
(作り直されるわけではない)


## おまけ

フォルダの存在があるかをif文で確認することもできる。
(明示的なので確認を取ってることが分かりやすい?)

```py
import os
DIR_NAME = ''
if not os.path.exists(DIR_NAME):
     os.mkdir(DIR_NAME)
```

`DIR_NAME` と同じパスをもつディレクトリがなければその名前のディレクトリを作る。

