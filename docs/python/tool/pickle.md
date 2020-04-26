# データの保存(pickle)

## 概要
pythonのオブジェクトを保存できる。  
(辞書,リストなど...)

## 保存
ファイルの`open()` は`wb` を指定する。
バイナリじゃないとダメというわけではないが、そのほうがいいらしい。

```py
import pickle
mydict = {1: 'one',
          2: 'two',
          3: 'three'}
with open('./mydict.pkl', 'wb') as f:
    pickle.dump(mydict, f)
```

## 読み込み

```py
import pickle
with open('./mydict.pkl', 'rb') as f:
    mydict_load = pickle.load(f)
```


## 参考

[ライブラリ：pickle](https://www.lifewithpython.com/2013/05/pickle.html)  

[【Python入門】pythonオブジェクトをpickleで保存しよう！](https://www.sejuku.net/blog/31480)
