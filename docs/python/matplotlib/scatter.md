# 散布図を描く


## 概要
散布図を描く

## ポイント

```py
plt.scatter(x, y, s=100, c="r", marker="*", alpha=0.5)
```

## サンプル
```py
x = [3,5,1,5,7,2,7,8,2,7]
y = [6,4,6,3,8,1,5,7,8,4]

# 散布図を描画
plt.scatter(x, y, s=100, c="r", marker="*", alpha=0.5)
plt.title('scatter')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
```

#### 座標のリストがあったとき?

```py
pair = [(4,7),(3,6),(2,1),(6,2),(1,5)]
x = [a for a,_ in pair]
y = [b for _,b in pair]

plt.scatter(x, y, s=100, c="r", marker="*", alpha=0.5)
plt.title('scatter')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
```