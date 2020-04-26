# データフレームの生成

2019/09/25

## DataFrameの生成
```py
import pandas as pd
dic = {"key1":["a1","a2","a3"],
       "key2":["b1","b2","b3"],
       "key3":["c1","c2","c3"]}
df = pd.DataFrame(dic)
```

- 結果
```sh
>>> df
  key1 key2 key3
0   a1   b1   c1
1   a2   b2   c2
2   a3   b3   c3
```

### indexの指定
```py
import pandas as pd
dic = {"key1":["a1","a2","a3"],
       "key2":["b1","b2","b3"],
       "key3":["c1","c2","c3"]}
df = pd.DataFrame(dic, index=["x","y","z"])
```

- 結果
```sh
>>> df
  key1 key2 key3
x   a1   b1   c1
y   a2   b2   c2
z   a3   b3   c3
```