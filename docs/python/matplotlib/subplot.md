# 複数の図をまとめて表示
2019/07/16

## 概要
複数のグラフをまとめて表示する。

## ポイント

以下の関数を使用する。

```py
plt.subplot(行の分割数,列の分割数,何番目の図か)
```

## サンプル

```py
import matplotlib.pyplot as plt
import numpy as np

x  = np.arange(0, 2*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1 + y2
plt.figure(figsize=(16, 8))

plt.subplot(2,2,1) # 左上
plt.plot(x, y1, 'g')
plt.xlim([0, 2*np.pi])
plt.ylim([-1.2, 1.2])

plt.subplot(2,2,2) # 右上
plt.plot(x, y2, 'b')
plt.xlim([0, 2*np.pi])
plt.ylim([-1.2, 1.2])

plt.subplot(2,2,3) # 左下
plt.plot(x, y3, 'r')
plt.xlim([0, 2*np.pi])
plt.ylim([-2, 2])

plt.subplot(2,2,4) # 右下
plt.xlim([0, 2*np.pi])
plt.ylim([-2, 2])
plt.plot(x, y1, 'g')
plt.plot(x, y2, 'b')
plt.plot(x, y3, 'r')

plt.show()
```
