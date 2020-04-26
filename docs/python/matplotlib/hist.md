# matplotlibでヒストグラムを描画

## 基本
```py
g1 = np.random.normal(loc=10.0, scale=0.15, size=1000)

plt.title("Title")
plt.xlabel('X', fontsize=10, color='k')
plt.ylabel('Y', fontsize=10, color='k')
plt.hist(g1, bins=50, color="g", alpha=1.0)
plt.show()
```


## おまけ

2つのグループのヒストグラムの描画
```py
g1 = np.random.normal(loc=10.0, scale=0.15, size=1000)
g2 = np.random.normal(loc=30.0, scale=1.0,  size=1000)

plt.title("Title")
plt.xlabel('X', fontsize=10, color='k')
plt.ylabel('Y', fontsize=10, color='k')
plt.hist([g1,g2], bins=50, color=["g","r"], alpha=0.5, width=0.09)
plt.show()
```