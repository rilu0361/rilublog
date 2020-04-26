# ベイズ推定

## 背景
最尤推定とMAP推定では、パラメータを一つ求めた。  
ベイズ推定では **パラメータの分布** を求める。

分布を推定することにより、そのパラメータ推定の信頼度が表現できるのがメリット。

## 概要

ベイズの定理を用いてデータ$D$を観測した後のパラメータ$\mu$の事後分布を推定する。

$$
p(\mu|D, \alpha) = \frac{p(D|\mu)p(\mu|a)}{p(D|a)}
$$

??? ベイズの定理
    $$
    \begin{align}
    p(\mu|D, \alpha) 
    &= \frac{p(D,\alpha|\mu)p(\mu)}{p(D,\alpha)} \\
    &= \frac{p(D|\mu)p(\alpha|\mu)p(\mu)}{\int p((\alpha, D), \alpha) d\mu} \\
    &= \frac{p(D|\mu)p(\mu|\alpha)p(\alpha)}{\int p(\alpha, D|\mu) p(\mu)d\mu} \\
    &= \frac{p(D|\mu)p(\mu|\alpha)p(\alpha)}{\int p(\alpha|\mu) p(D|\mu) p(\mu)d\mu} \\
    &= \frac{p(D|\mu)p(\mu|\alpha)p(\alpha)}{\int p(\mu|\alpha)p(\alpha) p(D|\mu)d\mu} \\
    &= \frac{p(D|\mu)p(\mu|\alpha)}{\int p(D|\mu) p(\mu|\alpha) d\mu} \\
    \end{align}
    $$

### 多項分布

起こりうる事象が多数ある場合を考える。($x\in\{0,1,2,...,K\}$)  
それぞれの事象の出現確率を$\mu_k$とする。($k=1,2,...,K$)  
ここで、$\sum^K_{k=1} \mu_k = 1$という制約が存在することに注意する。

試行回数を$N$、$m_k$が各事象の出現回数とする。

$$
\text{Multi}(\boldsymbol{m} |N, \boldsymbol{\mu}) 
= \frac{N!}{\prod^K_{k=1} m_k!} \prod^K_{k=1} \mu_k^{m_k}
$$

多項分布の共役事前分布はディリクレ分布であることから、事前分布にはディリクレ分布を用いる。  
このとき、ベイズの定理を用いて、パラメータ$\mu$の事後確率$p(\boldsymbol{\mu}|\boldsymbol{m}, \boldsymbol{D},\boldsymbol{\alpha})$は以下のように示される。  
($\boldsymbol{\alpha}$はディリクレ分布のハイパーパラメータ)

$$
\begin{align}
p(\boldsymbol{\mu}|\boldsymbol{m}, \boldsymbol{D}, \boldsymbol{\alpha}) 
&= \frac{\text{Multi}(\boldsymbol{m}|N, \boldsymbol{\mu}) \text{Dir}(\boldsymbol{\mu}|\boldsymbol{\alpha})}{\int_{\boldsymbol{\mu}} \text{Multi}(\boldsymbol{m}|N, \boldsymbol{\mu}) \text{Dir}(\boldsymbol{\mu}|\boldsymbol{\alpha}) d\boldsymbol{\mu}} \\
&\propto \text{Multi}(\boldsymbol{m}|N, \boldsymbol{\mu}) \text{Dir}(\boldsymbol{\mu}|\boldsymbol{\alpha}) \\
&= \frac{N!}{\prod^K_{k=1} m_k!} \prod^K_{k=1} \mu_k^{m_k} 
\frac{\Gamma(\sum^K_{k=1} \alpha_k)}{\prod^K_{k=1} \Gamma(\alpha_k)} \prod^K_{k=1} \mu^{\alpha_k-1}_k \\
&\propto \prod^K_{k=1} \mu^{m_k+a_k-1}_k
\end{align}
$$

この形から事後分布もディリクレ分布の形式になっていることが分かる。  
よって、正則化項を付け足すと、パラメータ$\boldsymbol{\mu}$の事後分布は、

$$
\begin{align}
p(\boldsymbol{\mu}|\boldsymbol{m}, \boldsymbol{D},\boldsymbol{\alpha}) 
&= \frac{\Gamma(\sum^K_{k=1} (m_k + \alpha_k))}{\prod^K_{k=1} \Gamma(m_k + \alpha_k)} \prod^K_{k=1} \mu^{m_k+\alpha_k-1}_k  \\
&= \frac{\Gamma(N + \sum^K_{k=1} \alpha_k)}{\prod^K_{k=1} \Gamma(m_k + \alpha_k)} \prod^K_{k=1} \mu^{m_k+\alpha_k-1}_k \\
&= \text{Dir}(\boldsymbol{\mu} | \boldsymbol{m} + \boldsymbol{\alpha})
\end{align}
$$

で示されるディリクレ分布になる。

!!! 導出2
    $$
    \begin{align}
    p(\boldsymbol{\mu}|\boldsymbol{m}, \boldsymbol{D}, \boldsymbol{\alpha}) 
    &= \frac{\text{Multi}(\boldsymbol{m}|N, \boldsymbol{\mu}) \text{Dir}(\boldsymbol{\mu}|\boldsymbol{\alpha})}{\int_{\boldsymbol{\mu}} \text{Multi}(\boldsymbol{m}|N, \boldsymbol{\mu}) \text{Dir}(\boldsymbol{\mu}|\boldsymbol{\alpha}) d\boldsymbol{\mu}} \\
    &= \frac{\frac{N!}{\prod^K_{k=1} m_k!} \prod^K_{k=1} \mu_k^{m_k} 
    \frac{\Gamma(\sum^K_{k=1} \alpha_k)}{\prod^K_{k=1} \Gamma(\alpha_k)} \prod^K_{k=1} \mu^{\alpha_k-1}_k}{\int_{\boldsymbol{\mu}} \frac{N!}{\prod^K_{k=1} m_k!} \prod^K_{k=1} \mu_k^{m_k} 
    \frac{\Gamma(\sum^K_{k=1} \alpha_k)}{\prod^K_{k=1} \Gamma(\alpha_k)} \prod^K_{k=1} \mu^{\alpha_k-1}_k d\boldsymbol{\mu} } \\
    &= \frac{\prod^K_{k=1} \mu^{m_k+a_k-1}_k}{\int_{\boldsymbol{\mu}}\prod^K_{k=1} \mu^{m_k+a_k-1}_k d\boldsymbol{\mu}} \\
    &= \frac{\Gamma(N + \sum^K_{k=1} \alpha_k)}{\prod^K_{k=1} \Gamma(m_k + \alpha_k)} \prod^K_{k=1} \mu^{m_k+\alpha_k-1}_k \\
    &= \text{Dir}(\boldsymbol{\mu} | \boldsymbol{m} + \boldsymbol{\alpha})
    \end{align} \\
    $$

    1つ目の等号はベイズの定理より。  
    5つ目の等号は$\int_{\boldsymbol{\mu}}\prod^K_{k=1} \mu^{m_k+a_k-1}_k d\boldsymbol{\mu} = \frac{\prod^K_{k=1} \Gamma(m_k + \alpha_k)}{\Gamma(N + \sum^K_{k=1} \alpha_k)}$ より。
    
