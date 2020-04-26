# 確率密度関数

## 前提

データを乱数で生成し、ヒストグラムに描画する。

```py
import numpy as np
import matplotlib.pyplot as plt

g1 = np.random.normal(loc=0.0, scale=0.15,size=1000)
g2 = np.random.normal(loc=3.0, scale=1.0, size=1000)
plt.xlabel('Temperature', fontsize=10, color='k')
plt.ylabel('Frequency',   fontsize=10, color='k')
plt.hist([g1,g2],bins=50, color=["g","r"], alpha=0.5, width=0.09)
plt.show()
```


## 基本

`norm.pdf()` を使う。

```py
p_s1_list = []
p_s2_list = []
for t in np.arange(-5,5,0.1):
    p_s1 = norm.pdf(x=t, loc=g1_mean, scale=g1_std)
    p_s2 = norm.pdf(x=t, loc=g2_mean, scale=g2_std)
    p_s2_list.append(p_s2)
    p_s1_list.append(p_s1)
    
# 図示
x  = np.arange(-5,5,0.1)
y1 = p_s1_list
y2 = p_s2_list

plt.plot(x, y1, 'g', label='health')
plt.plot(x, y2, 'b', label='sick')
plt.title('Title', fontsize=18, color='k')
plt.xlabel('Temperature', fontsize=15, color='k')
plt.ylabel('Cumulative density probability', fontsize=15, color='k')
plt.legend(loc='best', frameon=False)
plt.grid()
plt.show()
```

## 累積を見たい場合

```py
s1_list = []
for t in np.arange(-5,5,0.1):
    s1 = norm.cdf(x=t, loc=g2_mean, scale=g2_std)
    s1_list.append(s1)
# 表示
import pandas as pd
data = {"temperature":np.arange(-5,5,0.1),
      "s1(sick)":s1_list}
df = pd.DataFrame(data)
print(df)
```
