# Pandas

工事中…

## csvに保存
```py
df.to_csv('./csv_data.csv')
```

例)
```py
import pandas as pd
data = {"key1" : value1,
        "key2" : value2,
        "key3" : value3}
df = pd.DataFrame(data)
    
df.to_csv('./csv_data.csv')
```

## 重複を削除する

```py
df = df[df.duplicated(keep='last', subset="query") == False]
```



