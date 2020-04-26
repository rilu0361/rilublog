# 最尤推定(likelihood)

## 二項分布

コイントスの表裏のような二値の確率分布を表す。(ベルヌーイ試行)  
$\mu$を表が出る確率と考えると、$(1-\mu)$は裏が出る確率となる。  
$x$を表(0)か裏(1)とする。($x\in\{0,1\}$)

$$
\text{Bern}(x|\mu) = \mu^x (1-\mu)^{1-x}
$$

試行を繰り返すことで$\mu$を推測したい。

繰り返す回数(試行回数)を$N$回、その中で表が出た回数を$m$回とする。  
このとき、

$$
\text{Bin}(m|N, \mu) = 
\begin{pmatrix}
N \\
m
\end{pmatrix}
\mu^m (1-\mu)^{N-m}
$$

以上の式は **二項分布** と呼ばれる。  
ここで二項係数

$$
\begin{pmatrix}
N \\
m
\end{pmatrix}
= {}_N \text C _m = \frac{N!}{m!(N-m)!}
$$

に注意する。

尤もらしい$\mu$を推測するために、**最尤推定** を用いる。

$$
\begin{align}
L(\mu) 
&= \log \text{Bin}(m|N, \mu) \\
&= \log (\frac{N!}{m!(N-m)!} \mu^m (1-\mu)^{N-m}) \\
&= \log N! - (\log m! + \log (N-m)!) + m\log \mu + (N-m)\log(1-\mu)  \\
\end{align}
$$

ここで、$\log N! - (\log m! + \log (N-m)!)$ は、$\mu$と無関係なため、$\text{Const.}$(定数)で置換しておく。(考えない)

$$
L(\mu) = m\log \mu + (N-m)\log(1-\mu) + Const. 
$$

これは上に凸な関数となる。微分して0になるとき、最大となるので、まず$\mu$に関して微分して、

$$
\begin{align}
\frac{\partial}{\partial \mu} L(\mu) 
&= \frac{m}{\mu} + (N-m) \frac{-1}{1-\mu} \\
&= \frac{m}{\mu} - \frac{N-m}{1-\mu}
\end{align}
$$

($- \frac{N-m}{1-\mu}$になることに注意。($-\mu$なので微分したとき$-$が出てくる))  
よって、

$$
\begin{align}
0 &= \frac{m}{\mu} - \frac{N-m}{1-\mu} \\
0 &= (1-\mu)m - \mu(N-m) \\
0 &= m - m\mu - N\mu + m\mu \\
N\mu &= m \\
\mu &= \frac{m}{N}
\end{align}
$$

これは、「表が出る確率は試行回数分の実際に表が出た回数」となるので、直感にもあう結果となる。

## 多項分布

先ほどはコイントスでの表か裏という二値の場合を考えたが($x\in\{0,1\}$)、起こりうる事象が多数ある場合を考える。($x\in\{0,1,2,...,K\}$)  
例えば、サイコロの出る目であれば$K=6$となる。

それぞれの事象の出現確率を$\mu_k$とする。($k=1,2,...,K$)  
$N$が試行回数、$m_k$が各事象の出現回数とする。

このとき

$$
\text{Multi}(\boldsymbol{m} | \boldsymbol{\mu}) 
= \frac{N!}{\prod^K_{k=1} m_k!} \prod^K_{k=1} \mu_k^{m_k}
$$

対数尤度を考え、

$$
\begin{align}
L(\boldsymbol{\mu}) 
&= \log \text{Multi}(\boldsymbol{m} | \boldsymbol{\mu}) \\
&= \log (\frac{N!}{\prod^K_{k=1} m_k!} \prod^K_{k=1} \mu_k^{m_k}) \\
&= \log N! - \log \prod^K_{k=1} m_k! + \sum^K_{k=1} (m_k \log \mu_k) \\
&= \sum^K_{k=1} (m_k \log \mu_k) + Const.
\end{align} 
$$

ここで、$\sum^K_{k=1}\mu_k = 1$の制約を考慮して、ラグランジュ乗数を用いて以下の式を最大化することを考える。

$$
L(\boldsymbol{\mu}) = \sum^K_{k=1} (m_k \log \mu_k) + \lambda(\sum^K_{k=1}\mu_k - 1)
$$

$\boldsymbol{\mu}$に関して微分すると、

$$
\begin{align}
& \frac{\partial}{\partial \boldsymbol{\mu}} L(\boldsymbol{\mu}) \\
&= \biggr(\frac{\partial}{\partial \mu_1} (\sum^K_{k=1} (m_k \log \mu_k) + \lambda(\sum^K_{k=1}\mu_k - 1))
, \frac{\partial}{\partial \mu_2} (\sum^K_{k=1} (m_k \log \mu_k) + \lambda(\sum^K_{k=1}\mu_k - 1))
, ... 
, \frac{\partial}{\partial \mu_K} (\sum^K_{k=1} (m_k \log \mu_k)+ \lambda(\sum^K_{k=1}\mu_k - 1)) \biggl )^T \\
&= \biggr(\frac{m_1}{\mu_1}+ \lambda, \frac{m_2}{\mu_2}+ \lambda, ... , \frac{m_K}{\mu_K}+ \lambda \biggl)^T \\
\end{align}
$$

$\mu_k$のとき

$$
\begin{align}
0 &= \frac{m_k}{\mu_k} + \lambda \\
-\lambda \mu_k &= m_k \\
\mu_k &= -\frac{m_k}{\lambda}
\end{align}
\tag{1}
$$

制約条件$\sum^K_{k=1}\mu_k = 1$に(1)を代入すると、

$$
\begin{align}
\sum^K_{k=1} (\frac{m_k}{\lambda}) &= 1 \\
- \sum^K_{k=1} m_k &= \lambda \\
\lambda &= -N
\end{align}
$$

(mは各事象の発生回数なので、その総和$\sum^K_{k=1} m_k$は試行回数Nになる)

よって、この結果を(1)に代入して、

$$
\mu_k = -\frac{m_k}{N}
$$
