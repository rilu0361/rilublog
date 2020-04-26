# 確率分布

## ベルヌーイ分布

コイントスの表裏のような二値の確率分布を表す。   
$\mu$を表が出る確率と考えると、$(1-\mu)$は裏が出る確率となる。  
$x$を表(0)か裏(1)とする。($x\in\{0,1\}$)

$$
\text{Bern}(x|\mu) = \mu^x (1-\mu)^{1-x}
$$

#### 平均
$$
\mathbb{E}[x] = \mu
$$

#### 分散
$$
\text{Var}[x] = \mu (1-\mu)
$$

### 二項分布
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

ここで、

$$
\begin{pmatrix}
N \\
m
\end{pmatrix}
= {}_N \text C _m = \frac{N!}{m!(N-m)!}
$$

試行回数1回の二項分布はベルヌーイ分布と等価。

$$
\text{Bin}(m|1, \mu) = \text{Bern}(x|\mu)
$$

#### 平均
$$
\mathbb{E}[x] = N\mu
$$

#### 分散
$$
\text{Var}[x] = N\mu (1-\mu)
$$

## カテゴリ分布

起こりうる事象が多数ある場合を考える。($x\in\{0,1,2,...,K\}$)  
例えば、サイコロの出る目であれば$K=6$となる。

それぞれの事象の出現確率を$\mu_k$とする。($k=1,2,...,K$)  


### 多項分布
$N$が試行回数、$m_k$が各事象の出現回数とする。
このとき、

$$
\text{Multi}(\boldsymbol{m} |N, \boldsymbol{\mu}) 
= \frac{N!}{\prod^K_{k=1} m_k!} \prod^K_{k=1} \mu_k^{m_k}
$$

試行回数1回の多項分布とカテゴリ分布は等価。  
K=2のとき多項分布は二項分布と等価。

#### 平均
$$
\mathbb{E}[x] = N\mu
$$

#### 分散
$$
\text{Var}[x] = N\mu (1-\mu)
$$

## ベータ分布

二項分布のパラメータ$\mu$は$0\leq\mu\leq1$の制約をもつ。
これを満たすパラメータを生成する分布にベータ分布が存在する。

$$
Beta(\mu|a,b) = \frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)} \mu^{a-1} (1-\mu)^{b-1}
$$

$a=1, b=1$のとき一様分布になる。

$$
\Gamma(x) = \int^{\infty}_0 u^{x-1} \exp(-u) du
$$

$$
\begin{align}
\Gamma(x+1) &= x\Gamma(x) \\
\Gamma(1) &= 1
\end{align}
$$

$x$が自然数の場合

$$
\Gamma(x+1) = x!
$$

??? 導出
    $$
    \begin{align}
    \Gamma(x+1) 
    &= \int^{\infty}_0 u^x (-\exp(-u))' du \\
    &= [-u^x \exp(-u)]^{\infty}_0 + x \int^{\infty}_0 u^{x-1} \exp(-u) du \\
    &= x\Gamma(x)
    \end{align}
    $$

#### 平均

$$
\mathbb{E}[x] = \frac{a}{a+b}
$$

#### 最頻値

$$
\text{mode}[x] = \frac{a-1}{a+b-2} \\
(a>1, b>1)
$$

#### 分散

$$
\text{Var}[x] = \frac{ab}{(a+b)^2(a+b+1)}
$$



## ディリクレ分布

**多項分布** のパラメータ$\mu$は $0\leq\mu$、 $\sum^{K}_{k=1}\mu_k =1$ の制約をもつ。  
これを満たすパラメータを生成する分布にディリクレ分布が存在する。

$$
\text{Dir}(\mu|a) = \frac{\Gamma(\sum^K_{k=1} a_k)}{\prod^K_{k=1} \Gamma(a_k)} \prod^K_{k=1} \mu^{a_k-1}_k \\
(a_k > 0 : パラメータ)
$$

$\mu$が2次元のときベータ分布と等価。  
$a=1$のとき一様分布。

### ディリクレ分布の正則化項

$$
\int \prod^K_{k=1} \mu^{a_k-1}_k d\mu = \frac{\prod^K_{k=1} \Gamma(a_k)}{\Gamma(\sum^K_{k=1} a_k)}
$$

導出は省略。~~大変そう~~

#### 平均

$$
\mathbb{E}[\mu_k] = \frac{a_k}{\sum^{K}_{k=1}a_k}
$$

#### 最頻値

$$
\text{mode}[\mu_k] = \frac{a_k-1}{\sum^{K}_{k=1}a_k - K} \\
(a_k>1)
$$

#### 分散

$$
\text{Var}[\mu_k] = \frac{a_k(\sum^{K}_{k=1}a_k - a_k)}{(\sum^{K}_{k=1}a_k)^2(\sum^{K}_{k=1}a_k+1)}
$$

