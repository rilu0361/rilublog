# Seriesの生成

### 辞書から生成
```py
import pandas as pd
dic = {"ix1":"a1", "ix2":"b1", "ix3":"c1"}
series = pd.Series(dic)
```

]- 結果
```sh
>>> series
ix1    a1
ix2    b1
ix3    c1
dtype: object
```

### numpy配列から生成

```py
import pandas as pd
arr = np.array([17,25,13,10])
series = pd.Series(arr)
```


- 結果
```sh
>>> series
0    17
1    25
2    13
3    10
dtype: int32
```