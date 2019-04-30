
2018/06/25

## 平均
```py
from statistics import mean
print("平均 : ",mean(list))
```
### 調和平均
```py
from statistics import harmonic_mean
print("平均 : ", harmonic_mean(list))
```

## 中央値
```py
from statistics import median
print("中央値 : ",median(list))
```

## 分散
```py
from statistics import variance
print("不偏分散 : ",variance(list))
```
```py
from statistics import pvariance
print("母分散 : ",pvariance(list))
```

## 標準偏差
### 標本標準偏差
```py
from statistics import stdev
print("標本標準偏差 : ",stdev(list))
```
### 母集団の標準偏差
```py
from statistics import pstdev
print("母集団の標準偏差 : ",pstdev(list))
```

## いろいろ
```py
from statistics import mean, median, variance, stdev, harmonic_mean
def statistic(target: list) -> None:
    print("要素数 : ", len(target))
    print("最大 : ",max(target))
    print("最小 : ",min(target))
    print("中央値 : ",median(target))
    print("平均 : ",mean(target))
    print("不偏分散 : ",variance(target))
    print("標本標準偏差 : ",stdev(target))
    print("調和平均 : ", harmonic_mean(target) )
```

## リストに含まれる要素の出現回数を調べる
`Counter()` の引数に調べたいリストを入れる。
`.most_common()` で出現度順にソート。引数に数字nを入れれば上位n位を出力。

```py
from collections import Counter
cnt_element = Counter(list).most_common()
```

### 最頻値
```py
from statistics import mode
print("最頻値 : ", mode(list))
```
ただし最頻値が2つ以上ある場合エラーを返すので使い勝手が悪そう。

