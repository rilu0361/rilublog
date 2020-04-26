# pythonスクリプトのexe化

## 概要

Python がインストールされていない Windowsパソコンでも実行することができる。

## 準備

必要なもののインストール
```sh
pip install pyinstaller
```
winの場合
```sh
python -m pip install pyinstaller
```

## 実行
実行。カレントディレクトリに色々ファイルができる。  
`dist` のなかにexeファイルが作成されている。

```sh
pyinstaller test.py --onefile --noconsole
```

`--onefile` : 関連ファイルをひとつにまとめてexeにする。  
`--noconsole` : 実行時コマンドプロンプトを出さない。

--onefile しないほうが、exeの起動が速かった。  
--oneline をしない場合、たくさんの関連ファイルが生成されてしまうので驚く。


Windows環境(python 3.6.4 venv)ではできたが、WSLのUbuntu16.04上でうまく実行できなかった。

## 備考

友人がやったとき、完成したexeファイルがものすごい大きさになってしまったらしい。  
同じpythonファイルを自分がexe化したときにはもっと小さいファイルができたので、なぜなのかは疑問に思っているところ。

自分の場合は新しく仮想環境を作って最小構成でやっていたという違いくらいしかないので、もしかしたらそこが原因かもしれない。  
わからないので教えてください。

## 参考
[Pythonのファイルをexe化する方法【初心者向け】](https://techacademy.jp/magazine/18963)
