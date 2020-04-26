# 時間の取得

現在時刻を取得してそのままファイル名にするなどに使える。

## 年月日の出力

年月日

```py
import datetime
now = datetime.datetime.now()
print('{0:%Y%m%d}.txt'.format(now))
```

出力
```sh
20180831.txt
```

## 年月日時分の出力

```py
import datetime
now = datetime.datetime.now()
print('{0:%Y%m%d%H%M}.txt'.format(now))
```

出力
```sh
201905240922.txt
```