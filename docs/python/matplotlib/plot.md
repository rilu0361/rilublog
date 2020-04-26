# matplotlib基本
2019/07/16

## 概要
matplotlibによる図示。  

## 導入
```py
import matplotlib.pyplot as plt
```

## とりあえず結論
sinカーブの描画

```py
import matplotlib.pyplot as plt
import numpy as np

x  = np.arange(0, 2*np.pi, 0.1)
y  = np.sin(x)

plt.figure(figsize=(16, 8))
plt.plot(x, y, 'g', label='1')
plt.xlim([0, 10])
plt.ylim([-10, 10])
plt.title('Title', fontsize=18, color='k')
plt.xlabel('x', fontsize=15, color='k')
plt.ylabel('y', fontsize=15, color='k')
plt.legend(loc='best', frameon=False)
plt.grid()
plt.show()
# plt.savefig('sample.png')  # 保存
```

## 図の大きさの指定
```py
plt.figure(figsize=(16, 8))
```

## プロット
```py
plt.plot(x, y, 'g', label='1')
```
#### 色の指定

以下のリンクにあるものは指定可能。  
[https://matplotlib.org/examples/color/named_colors.html](https://matplotlib.org/examples/color/named_colors.html)


#### 線の指定

|記号|線種|
|:-:|:-:|
|-|通常線|
|--|破線|
|-.|一点鎖線|
|:|点線|

#### 点の指定

|記号|点|
|:-:|:-:|
|.|点|
|o|丸|
|v|下三角|
|*|星|
|s|四角|

## 表示範囲の指定

```py
plt.xlim([0, 10])
plt.ylim([-10, 10])
```

## タイトル,x軸,y軸

```py
plt.title('Title', fontsize=18, color='k')
plt.xlabel('x', fontsize=15, color='k')
plt.ylabel('y', fontsize=15, color='k')
```

## 凡例

```py
plt.legend(loc='best', frameon=False)
```

## 表示

```py
plt.show()
```

## 保存
```py
plt.savefig('sample.png') 
```

## おまけ

2つの曲線を図示する。

```py
import matplotlib.pyplot as plt
import numpy as np

x  = np.arange(0, 2*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(16, 8))
plt.plot(x, y1, 'g', label='1')
plt.plot(x, y2, 'b', label='2')
plt.xlim([0, 10])
plt.ylim([-10, 10])
plt.title('Title', fontsize=18, color='k')
plt.xlabel('x', fontsize=15, color='k')
plt.ylabel('y', fontsize=15, color='k')
plt.legend(loc='best', frameon=False)
plt.grid()
plt.show()
# plt.savefig('sample.png')  # 保存
```