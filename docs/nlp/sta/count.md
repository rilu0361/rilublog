# 統計・カウント
2019/07/23


## 単語のカウント(TF値)
```py
from collections import Counter

words = ['a', 'an', 'in', 'on', 'in', 'a', 'in']
tf = Counter(words)
print(tf)
```

```sh
Counter({'in': 3, 'a': 2, 'an': 1, 'on': 1})
```
辞書ではないが辞書っぽいものが返ってくる。  

文書が複数ある場合
```py
from collections import Counter
docs =  [['a', 'an', 'in', 'on', 'in', 'a', 'in'],
         ['a', 'no', 'no', 'no', 'in', 'a', 'no'],
         ['a', 'no', 'ok', 'on', 'in', 'a', 'no']]

sum_tf = Counter()
for words in docs:
    sum_tf = sum_tf + Counter(words)
print(tf)
```

#### 出現頻度の高い単語

```py
most_tf = sum_tf.most_common()
print(most_tf)
```

```sh
[('in', 3), ('a', 2), ('an', 1), ('on', 1)]
```

### 単語の出現文書のカウント(DF値)

```py
from collections import Counter
docs =  [['a', 'an', 'in', 'on', 'in', 'a', 'in'],
         ['a', 'no', 'no', 'no', 'in', 'a', 'no'],
         ['a', 'no', 'ok', 'on', 'in', 'a', 'no']]

df = Counter()
for words in docs:
    df = df + Counter(set(words))

print(df)
```



## 統計情報としてまとめる

列：TF, DF
行：各単語

```py
from collections import Counter
docs =  [['a', 'an', 'in', 'on', 'in', 'a', 'in'],
         ['a', 'no', 'no', 'no', 'in', 'a', 'no'],
         ['a', 'no', 'ok', 'on', 'in', 'a', 'no']]

sum_tf = Counter()
df = Counter()
for words in docs:
    sum_tf = sum_tf + Counter(words)
    df = df + Counter(set(words))

print(sum_tf)
print(df)

import pandas as pd
dic = {"sum_TF":sum_tf,
        "DF":df}
data = pd.DataFrame(dic)
pd.to_excel("sum_tf_DF.xlsx")
```




