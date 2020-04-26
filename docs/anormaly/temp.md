# 単純ベイズ法による異常検知


## 変数が統計的に独立な場合の最尤推定

$M$次元ベクトル$\boldsymbol{x}$とラベル$y\in\{0(正常),1(異常)\}$がある$N$個の標本をもつデータ$\mathcal{D}$を考える。

$$
\mathcal{D} = \bigr\{(\boldsymbol{x}^{(1)},y^{(1)}), (\boldsymbol{x}^{(2)},y^{(2)}), ..., (\boldsymbol{x}^{(N)},y^{(N)}) \bigl\} \\
$$

ラベル付きデータがある場合、異常度(anormaly score)は
条件付き確率 $p(x|y)$ を用いて、以下のように表される。

$$
a(x) = \ln \frac{p(x|y=1)}{p(x|y=0)}
$$

$M$次元のそれぞれが統計的に独立であるとして、$y$を与えられたときの$\boldsymbol{x}$の条件付き分布$p(\boldsymbol{x}|y)$は次のように仮定される。

$$
p(\boldsymbol{x}|y) = p(x_1|y)p(x_2|y)p(x_M|y) = \prod^M_{i=1} p(x_i|y)
$$

異常度を計算するためには、この$p(\boldsymbol{x}|y)$をモデルとして、それに含まれるパラメータを決定する必要があるため、最尤推定を行う。

このとき、**M変数のそれぞれに対して別々に最尤推定することでモデルのパラメータを求めることが可能。**(変数が統計的に独立な場合)

### 説明

- - -

データ$\mathcal{D}$が異常標本を含まないか、圧倒的少数であるという仮定のもと、以下の確率密度関数に従うとする。

$$
\mathcal{N}(\boldsymbol{x}^{(n)} | \boldsymbol{\mu} ,\Sigma) \equiv \frac{|\Sigma|^{-1/2}}{(2\pi)^{M/2}} \exp\{-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu})^T\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu})\} \\
$$

この確率密度関数を正規分布またはガウス分布と呼ぶ。  
$\mu$は平均,$\Sigma$は共分散行列を表し、この２つが確率分布のパラメータ。

このパラメータの決定には最尤推定を用いるのが一般的。  
最尤推定ではデータ集合$\mathcal{D}$の対数尤度$L(\mu,\Sigma| \mathcal{D})$を最大化する$\mu$と$\Sigma$を求める。

まず、$\mathcal{D}$の対数尤度$L(\mu,\Sigma| \mathcal{D})$は以下の式で表せる。

$$
L(\mu,\Sigma| \mathcal{D}) = \ln \prod^N_{n=1}\mathcal{N}(\boldsymbol{x}^{(n)} | \boldsymbol{\mu} ,\Sigma) = \sum^N_{n=1} \mathcal{N}(\boldsymbol{x}^{(n)} | \boldsymbol{\mu} , \Sigma) \\
$$

ガウス分布($\mathcal{N}(\boldsymbol{x}^{(n)} | \boldsymbol{\mu} ,\Sigma)$)の定義より、

$$
L(\boldsymbol{\mu}, \Sigma | \mathcal{D}) = -\frac{MN}{2}\ln(2\pi) - \frac{N}{2} \ln|\Sigma| - \frac{1}{2} \sum^N_{n=1}(\boldsymbol{x}^{(n)}-\boldsymbol{\mu})^T \Sigma^{-1} (\boldsymbol{x}^{(n)} - \boldsymbol{\mu})
$$

これを最大化する$\mu$と$\Sigma$を求めるので、$L(\boldsymbol{\mu}, \Sigma | \mathcal{D})$ を$\boldsymbol{\mu}$に関して微分する。

$$
\frac{\partial L(\boldsymbol{\mu}, \Sigma | \mathcal{D})}{\partial \mu} = \sum^{N}_{n=1}\Sigma^{-1} (\boldsymbol{x}^{(n)} - \boldsymbol{\mu})
$$

<!-- これより平均の最尤解$\hat{\mu}$は
$$
\hat{\mu} = \frac{1}{N} \sum^N_{n=1} \boldsymbol{x}^{(n)}
$$
これは最尤解$\hat{\mu}$が$x$の相加平均であることを示す。


$\Sigma$の最尤解$\hat{\Sigma}$は、$-\ln |\Sigma| = \ln|\Sigma^{-1}|$に注意して、$\Sigma^{-1}$で微分すると以下のように求められる。

$$
\hat{\Sigma} = \frac{1}{N} \sum^N_{n=1}(\boldsymbol{x}^{(n)}-\boldsymbol{\hat{\mu}})(\boldsymbol{x}^{(n)} - \boldsymbol{\hat{\mu}})^T
$$ -->
- - -

$x_i$の条件付き分布を、未知パラメータ$\boldsymbol{\theta}^y_i$を用いて、$p(x_i|\boldsymbol{\theta}^y_i, y)$と仮定する。このとき対数尤度は以下の式で表せる。

$$
L(\Theta | \mathcal{D}) = \sum^N_{n=1}\sum^M_{i=1} \ln p(x_i^{(n)} | \boldsymbol{\theta}^{y^{n}}_i , y^{(n)}) \\
= \sum^M_{i=1}\bigr\{\sum_{n \in \mathcal{D}^1} \ln p(x_i^{(n)} | \boldsymbol{\theta}^{1}_i , y=1) + \sum_{n \in \mathcal{D}^0} \ln p(x_i^{(n)} | \boldsymbol{\theta}^{0}_i , y=0)  \bigl\}
$$

$\mathcal{D}^0, \mathcal{D}^1$はそれぞれ$y=0,1$の標本集合。  
$\Theta$はパラメータ$\theta$をまとめた記号として表記している。

$y=1$のとき$\theta^1_{i}$の最尤解を与える条件式は以下のようになる。


$$
\boldsymbol{0} 
= \frac{\partial L}{\partial  \boldsymbol{\theta}^{1}_i} 
= \frac{\partial}{\partial  \boldsymbol{\theta}^{1}_i} \sum_{n\in \mathcal{D^1}} \ln p(x_i^{(n)} | \theta^1_{i}, y=1)
$$

以上より、$i$と$y=1$に対応する項しか寄与していないことが分かる。
よって、この問題は、各変数($x_i$)ごと、ラベルごと($y\in\{0,1\}$)に独立していることを意味する。  


## 独立変数モデルのもとでのホテリング$T^2$法

多変量正規分布

$$
\mathcal{N}(\boldsymbol{x}^{(n)} | \boldsymbol{\mu} ,\Sigma) 
\equiv \frac{|\Sigma|^{-1/2}}{(2\pi)^{M/2}} \exp\{-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu})^T\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu})\} 
$$

において、共分散行列$\Sigma$の非対角成分をすべて$0$に置き換え以下の式を考える。  
これは各変数の相関係数が$0$であることを意味する。

$$
p(x) 
= \prod^M_{i=1} \mathcal{N}(x^{(n)} |\mu_i ,\Sigma_{ii}) 
= \prod^M_{i=1} \frac{1}{\sqrt{2\pi \Sigma_{ii}}} \exp \{-\frac{1}{2\Sigma_{ii}}(x_i - \mu_i)^2\} 
$$

この場合も、**M変数のそれぞれに対して別々に最尤推定することでモデルのパラメータを求めることが可能。**

対数尤度を$\mu_i$および、$\Sigma^{-1}_{ii}$に関して微分することで以下の最尤解が求められる。

$$
\hat{\mu_i} = \frac{1}{N} \sum^N_{n=1} x_i^{(n)}
$$

$$
\hat{\Sigma}_{ii} 
= \hat{\sigma}_i^2 
\equiv \frac{1}{N} \sum^N_{n=1}(x^{(n)}_i-\hat{\mu}_i)^2
$$ 

これを使って異常度を求めると、以下の式で定義できる。  
異常度は$M$個の変数の異常度の和として表す。

$$
a(\boldsymbol{x}) = \sum^M_{i=1} (\frac{x_i - \hat{\mu}_i}{\hat{\sigma_i}})^2
$$

計算が面倒でない(逆行列の計算など不要)ので   
$M$個の変数が独立なら実用上有用。  
独立でなくとも異常度の大きさを見積もるために有用。

変数を個々に見ると異常判定の枠が不当に大きくなる場合があり、変数に線形相関がありそうな場合に上手く対応できない。

これに対処するため、変数を2つずつ組にして処理する方法がある。

## 多項分布による単純ベイズ分類

