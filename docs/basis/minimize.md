# 最小値を求める

## 1.最小値を求める基礎(二次関数)

$$
J(\omega) = a\omega^2 +b\omega +c 　 (a>0) 
\tag{1.1}
$$
があったとき、この下向きに凸な関数の最小値をとる$\omega$は以下のように求められる。  

式(1.1)を微分すると、
$$
\frac{\partial}{\partial \omega} J(\omega) = 2a\omega + b
$$

最小値をとる点での微分した値は$0$になることを利用して、

$$
\begin{align}
2a\omega + b &= 0 \\
\omega &= -\frac{b^2}{2a}
\end{align}
$$

よって、

$$
\begin{align}
J( -\frac{b^2}{2a}) 
&= a( -\frac{b^2}{2a})^2 + b (-\frac{b^2}{2a}) +c \\
&= c - \frac{b^2}{4a}
\end{align}
$$

最小値は$\omega =  -\frac{b^2}{2a}$ のとき、$c - \frac{b^2}{4a}$となる。


## 2. 線形回帰モデル

線形回帰モデルは以下の式で表現される。

$$
y_n = \omega_0 + \omega_1 x_n + \epsilon_n
\tag{2.1}
$$

$x$が特徴量、$y$を出力とする。  
$\omega_0$が切片、$\omega_1$が傾きという一次関数に対して、$\epsilon_n$をノイズ(直線上の点と実データの点とのずれ)と考える。

データをよく捉えた直線というのは、この$\epsilon_n$が最小である。  
そこで、二乗誤差を求め、その誤差が最小となるパラメータを求めてみる。

$$
J(\omega) 
= \sum^N_{n=1} \epsilon_n^2 
= \sum^N_{n=1}\{y_n - (\omega_0 + \omega_1 x_n)\}^2
\tag{2.2}
$$

これが最小になるとき、$J(\omega)$は、パラメータ$\omega_0, \omega_1$に関して微分した値がそれぞれ$0$になる。

計算を簡単にするため

$$
J(\omega) = \frac{1}{2}  \sum^N_{n=1} \{(\omega_0+\omega_1 x_n) - y_n \}^2
\tag{2.3}
$$

とおく。(微分すると$\frac{1}{2}$が消えてくれる)

式(2.3)をそれぞれの変数によって微分する。このとき、$\mu$を平均、$\sigma^2$を分散とする。

??? 計算のテクニック
    
    $$
    \sum^N_{n=1}x_n = N\mu_x
    $$


まず$\omega_0$に関して、

$$
\begin{align}
\frac{\partial}{\partial \omega_0} J(\omega) 
&= \sum^N_{n=1} (\omega_0 + \omega_1 x_n - y_n) \\
&= N\omega_0 + (\sum^N_{n=1}x_n)\omega_1 - (\sum^N_{n=1}y_n) \\
&= N\omega_0 + N\mu_x\omega_1 - N\mu_y
\end{align}
\tag{2.4}
$$

次に$\omega_1$に関して、

$$
\begin{align}
\frac{\partial}{\partial \omega_1} J(\omega) 
&= \sum^N_{n=1} x_n (\omega_0 + \omega_1 x_n - y_n) \\
&= (\sum^N_{n=1}x_n)\omega_0 + (\sum^N_{n=1}x_n^2)\omega_1 - (\sum^N_{n=1}x_n y_n)  \\
&= N\mu_x\omega_0 + N\sigma_x^2\omega_1 - N\sigma^2_{xy}
\end{align}
\tag{2.5}
$$


(2.4),(2.5)より、

$$
\begin{align}
\left\{
\begin{array}{ll}
N\omega_0 + N\mu_x\omega_1 - N\mu_y &= 0 
\tag{2.6} \\
N\mu_x\omega_0 + N\sigma_x^2\omega_1 - N\sigma^2_{xy} &= 0
\end{array}
\right.
\end{align}
$$

$N\omega_0 + N\mu_x\omega_1 - N\mu_y = 0$ を変形して、

$$
\omega_0 = \mu_y - \mu_x\omega_1 
$$

これを $N\mu_x\omega_0 + N\sigma_x^2\omega_1 - N\sigma^2_{xy} = 0$ に代入すると

$$
\begin{align}
N(\mu_y - \mu_x\omega_1 )\mu_x + N \sigma_x^2 \omega_1 - N \sigma_{xy}^2 &= 0 \\
\mu_x \mu_y - \mu_x^2 \omega_1 + \sigma_x^2 \omega_1 - \sigma^2_{xy} &= 0 \\
(\sigma_x^2 - \mu_x^2)\omega_1 + \mu_x\mu_y - \sigma_{xy}^2 &= 0 \\
\{(\frac{1}{N} \sum^N_{n=1} x_n^2)-(\frac{1}{N} \sum^N_{n=1} x_n)^2\} \omega_1 
+ (\frac{1}{N} \sum^N_{n=1} x_n) (\frac{1}{N} \sum^N_{n=1} y_n) 
- (\frac{1}{N} \sum^N_{n=1} x_n y_n) &= 0  \\
\{\frac{1}{N} \sum^N_{n=1}(x_n-\mu_n)^2\} \omega_1 
- \{\frac{1}{N} \sum^N_{n=1}(x_n-\mu_x)(y_n-\mu_y)\} &= 0 \\ 
\end{align}
$$

よって

$$
\omega_1 = \frac{ \sum^N_{n=1}(x_n-\mu_x)(y_n-\mu_y) }{\sum^N_{n=1} (x_n-\mu_x)^2} 
$$

以上から

$$
\begin{align}
\left\{
\begin{array}{ll}
\omega_0 &= \mu_y - \mu_x\omega_1 \\  
\tag{2.7}
\omega_1 &= \frac{ \sum^N_{n=1}(x_n-\mu_x)(y_n-\mu_y) }{\sum^N_{n=1} (x_n-\mu_x)^2} 
\end{array}
\right.
\end{align}
$$

となることがわかる。


### xが多次元になったとき

$D$次元の特徴量をもつ$\boldsymbol x$を考える。

$$
\boldsymbol x = (x_1, x_2 ,..., x_D)^T
$$

線形回帰モデルは

$$
y(\boldsymbol x, \boldsymbol \omega) = \omega_0 + \omega_1 x_1 + ... +\omega_D x_D
$$

ここで、

$$
\boldsymbol x = (1, x_1, x_2 ,..., x_D)^T \\
\boldsymbol \omega = (\omega_0, \omega_1, \omega_2 ,..., \omega_D)^T
$$

と考えると、

$$
\begin{align}
y(\boldsymbol x, \boldsymbol \omega) 
&= \omega_0・1 + \omega_1 x_1 + ... +\omega_D x_D \\
&= \sum^D_{d=0} \omega_d x_d \\
&= \boldsymbol{\omega}^T \boldsymbol{x}
\end{align}
$$

と表現できる。

$D$次元の変数$x$をもつ、$N$個のデータは以下のように表現できる。

$$
\boldsymbol{y} = 
\begin{pmatrix}
y_1 \\
y_2 \\
\vdots \\
y_N
\end{pmatrix}
\boldsymbol{x} = 
\begin{pmatrix}
1 & x_{11} & \cdots & x_{1D} \\
1 & x_{21} & \cdots & x_{2D} \\
\vdots & \vdots & \ddots & \vdots \\
1 & x_{N1} & \cdots & x_{ND} \\
\end{pmatrix}
\boldsymbol{\omega} =
\begin{pmatrix}
\omega_1 \\
\omega_2 \\
\vdots \\
\omega_N
\end{pmatrix}
$$

このとき、

$$
\boldsymbol{\hat{y}} = \boldsymbol{X} \boldsymbol{\omega}
$$


