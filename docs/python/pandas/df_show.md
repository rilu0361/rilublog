# データフレームの全表示

## 概要
jupyter notebook上でDataFrameを表示させたら、列数が多すぎて中間の列が `...` で省略されてしまう。


## 対処

第二引数に任意の列数を入力。(今回は50)

```py
pd.set_option('display.max_columns', 50)
```


## 参考

[Qiita Jupyter notebookで列をすべて表示したい](https://qiita.com/daifuku_mochi2/items/30258e58750ff8e85d37)