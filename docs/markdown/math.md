# 数式の挿入

自分が使うもの周辺のみまとめています。  
細かく知りたい方は他サイト様でもっと詳しく説明されていますのでそちらへ。

## 基本
### 数式を入れる
改行は　`\\` を文末に記入。
```md
$$
a^2 + b^2 = c_2 \\
a + b = 2
$$
```

$$
a^2 + b^2 = c_2 \\
a + b = 2
$$

### 文章中に数式を入れる $ $
```md
このとき $c=0.05$ とする。 
```
このとき  $c=0.05$ とする。 

## 上付き文字^と下付き文字_
2文字以上は `{}` で囲む。
```md
$$
a^{x+y_i} ,
a_i ,
a^i ,
a_{x+y_i}  
$$
```

$$
a^{x+y_i}  ,
a_i  ,
a^i  ,
a_{x+y_i}  
$$


## 分数 \frac{}{}
`\frac{}{}`
```md
$$
\frac{y_{i+j}}{x_i+x_j}
$$
```
$$
\frac{y_{i+j}}{x_i+x_j}
$$


## 平方根　\sqrt{}
```md
$$
\sqrt{x+y}
$$
```

$$
\sqrt{x+y}
$$

## 総和 総乗 \sum

```md
$$
\sum_{i=1}^N x_i \\
\prod_{j=1}^M y_j
$$
```

$$
\sum_{i=1}^N x_i \\
\prod_{j=1}^M y_j
$$

## 三角関数 \sin \cos \tan
```md
$$
\sin^2x + \cos^2y + \tan z
$$
```

$$
\sin^2x + \cos^2y + \tan z
$$

## 対数 \log \ln
```md
$$
\log_2x , \ln y
$$
```

$$
\log_2 x , \ln y
$$

## 指数関数 \exp e
```md
$$
\exp(x) , e^x
$$
```

$$
\exp(x) , e^x
$$

## 積分 \int
```md
$$
\int_0^{10} x
$$
```

$$
\int_0^{10} x
$$

## 極限 \lim
```md
$$
\lim_{x \to \infty} x
$$
```

$$
\lim_{x \to \infty} x
$$

## 床関数・天井関数 \lcsil \lfloor
```md
$$
\lceil x \rceil 
\lfloor x \rfloor
$$
```

$$
\lceil x \rceil 
\lfloor x \rfloor
$$

## 組み合わせ・順列 
```md
$$
{}_n \text C _r \\
{}_n \text P _r
$$
```

$$
{}_n \text C _r \\
{}_n \text P _r
$$

## =の位置の統一 \begin{align}

```md
$$
\begin{align}
a &= x+y+z \\
b + c &= x + y
\end{align}
$$
```

$$
\begin{align}
a &= x+y+z \\
b + c &= x + y
\end{align}
$$

## 数式に番号を割当 \tag{}

```md
$$
\begin{align}
a &= x+y+z \tag{2.11} \\
b + c &= x + y \tag{2.12}
\end{align}
$$
```

$$
\begin{align}
a &= x+y+z \tag{2.11} \\
b + c &= x + y \tag{2.12}
\end{align}
$$


## 行列 \begin{matrix}
```md
$$
\begin{bmatrix}
a & \cdots & b \\
c & \cdots & d 
\end{bmatrix}
$$
```

$$
\begin{bmatrix}
a & \cdots & b \\
c & \cdots & d 
\end{bmatrix}
$$

```md
$$
\begin{pmatrix}
a & b \\
c & d 
\end{pmatrix}
$$
```

$$
\begin{pmatrix}
a & b \\
c & d 
\end{pmatrix}
$$

## 場合分け 
```md
$$
f(x) = \left\{
\begin{array}{ll}
1 & (x \geq 1) \\
0 & (1 \lt x \lt 0) \\
-1 & (x \leq 0)
\end{array}
\right.
$$
```

$$
f(x) = \left\{
\begin{array}{ll}
1 & (x \geq 1) \\
0 & (1 \lt x \lt 0) \\
-1 & (x \leq 0)
\end{array}
\right.
$$


## 参考
もっと詳しく書いてくださっているものがあります。   
[Qiitaの数式チートシート](https://qiita.com/PlanetMeron/items/63ac58898541cbe81ada)
