# 異常検知基礎


## 異常検知

外れ値検知
    大多数の標本と値が大きく異なるものの検知。時系列的にずれている場合もある。

変化検知
    パターン的にずれが起こっている場所の検知。


## 異常度

### ラベル付きデータがある場合

異常度(anormaly score)は
条件付き確率 $p(x|y)$ を用いて、以下のように表す。

$$
a(x) = \ln \frac{p(x|y=1)}{p(x|y=0)}
$$

このとき $x$ は入力標本、 $y$ は0のとき正常、1のとき異常データである。
$a(x)$ が所定の閾値を超えたとき異常とみなす。


### ラベル付きデータがない場合

ラベル付きデータがない場合は正常データのみで分布を作成する。
この正常データのモデルにおいて、出現確率が小さい観測値は異常の可能性が高い。

$$
a(x) = \ln p(x)
$$

シャノンの情報量の観点からも考えることができる。

これは $a(x) = \ln \frac{p(x|y=1)}{p(x|y=0)}$ の $p(x|y=1)$ を与えていないものとも言える。


## 評価


通常、訓練データとテストデータに分けて評価を行う。

### 検証法

交差検証法
    データをn分割し、:math:`\frac{1}{n}` で評価、それ以外で訓練を行う。評価を行う :math:`\frac{1}{n}` のデータを入れ替えながらn回の評価を行い、平均を計算する。

1つ抜き交差検証法
    外れ値検出のとき使用。:math:`n-1` のデータで訓練し、:math:`1` のデータを評価する。評価するデータを入れ替えながらn回行う。

### 結果

<!-- +------------------+---------------------------------------+
|                  | Ground Truth(正解)                    |
+------------------+-------------------+-------------------+
|                  | 正常              | 異常              |
+-----------+------+-------------------+-------------------+
| 予測結果  | 正常 | True Positive(TP) | False Negative(FP)|
|           +------+-------------------+-------------------+
| (predict) | 異常 | False Positive(FP)| True Negative(TN) |
+-----------+------+-------------------+-------------------+ -->

| Predict(予測結果)\\Ground Truth(正解)    |正常   |異常         |
|:----:|:-----------------:|:-------------------:|
|正常  | True Positive(**TP**) | False Negative(**FP**)  |
|異常  |False Positive(**FP**) | True Negative(**TN**)   |

### 評価指標


#### 正常標本精度(accuracy)
正常標本の中でいくつ正常だと正しく判定できたか。

$$
acc = \frac{TP}{TP+FP}
$$

#### 誤報率
本来正常のものを異常と言ってしまった割合。

$$
誤報率 = 1 - acc
$$

#### 異常標本精度(Recall)
異常標本の中でいくつ異常だと正しく判定できたか。

$$
recall = \frac{TN}{TN+FP}
$$

#### F値
正常標本精度と異常標本精度の調和平均

$$
f = \frac{2*acc*recall}{acc+recall}
$$

#### AUC(area under curve)
ROC曲線の下部面積。

##### ROC曲線
通常、縦軸:異常標本精度、横軸:誤報率のグラフを定義。  
閾値を $\tau$ とする。
$$
(x, y) = (1-acc(\tau), recall(\tau) )
$$

## 参考文献

異常検知と変化検知　-井出剛　杉山将