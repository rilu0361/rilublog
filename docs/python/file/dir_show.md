# ディレクトリ一覧取得

## フォルダの中身のファイルのパスをすべて取得

### ディレクトリの中身全部の名前(特に細かな指定がない場合)

```py
import os
DIR_NAME = "../"
file_list = os.listdir(DIR_NAME)
print(file_list)
```
`DIR_NAME` にファイルの一覧を取得したい階層のパスを指定する。

- 結果
```sh
['.git', '.gitignore', '.vscode', 'docs', 'mkdocs.yml', 'mk_env.yml', 'README.md', 'site', 'temp', 'test.py', 'write.txt']
```

### 細かい指定がしたい場合
```py
from pathlib import Path
DIR_PATH = Path("絶対/相対パス")
FILE_PATH_LIST = list(DIR_PATH.glob("*"))
FILE_NAME_LIST = [str(path).split('/')[-1] for path in FILE_PATH_LIST]
```

`glob("*")` の*に正規表現でファイル名を指定して取得することができる。

上記プログラムの  
`FILE_PATH_LIST` はパスのリスト、  
`FILE_NAME_LIST` はファイル名のみのリストを作成している。

- 結果(`FILE_PATH_LIST`)
```sh
[PosixPath('../mk_web/.git'), PosixPath('../mk_web/.gitignore'),PosixPath('../mk_web/docs'), PosixPath('../mk_web/mkdocs.yml'), PosixPath('../mk_web/README.md'), PosixPath('../mk_web/site')]
```

- 結果(`FILE_NAME_LIST`)
```sh
['.git', '.gitignore', 'docs', 'mkdocs.yml','README.md', 'site']
```

