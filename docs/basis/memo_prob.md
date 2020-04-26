# 確率

### 同時確率
事象AとBが同時に起こる確率(Joint probability)

$$
p(A,B)
$$

### 条件付き確率
Aが起こったという条件のもと、Bが起こる確率(conditional probability)

$$
p(B|A)
$$

### 乗法定理

$$
p(A,B) = p(B|A)p(A) = p(A|B)p(B)
$$

### 周辺化

$$
\begin{align}
p(A) 
&= \sum_{B}p(A,B) \\
&= \sum_{B}p(A|B)p(B)
\end{align}
$$

このときp(A)を周辺確率と呼ぶ。乗法定理より、最後の式が得られる。

### ベイズの定理
乗法定理より、

$$
p(B|A) = \frac{p(A|B)p(B)}{p(A)}
$$

分母はBに関する全事象の和を1にするための正規化項。  
分母Aを周辺化すると

$$
p(B|A) = \frac{p(A|B)p(B)}{\sum_B p(A|B)p(B)}
$$



### 独立

以下のとき、AとBは独立。

$$
p(A,B) = p(A)p(B)
$$

以下のとき、AとBはCのもとで独立。(条件付き独立)

$$
p(A,B|C) = p(A|C)p(B|C)
$$

## 期待値
確率$p(x)$に従う$x$の関数$f(x)$の期待値$\mathbb{E}[f(x)]$は、$f(x)$を$p(x)$で重み付けした総和をとったもの。

$$
\mathbb{E}[f(x)] = \sum_{x\in\mathcal{X}} p(x)f(x)
$$

#### 平均
$f(x)=x$のときの期待値を平均と呼ぶ

$$
\mathbb{E}[x] = \sum_{x\in\mathcal{X}} p(x)x
$$

#### 最頻値
最も確率が高くなる値は最頻値と呼ばれる

$$
\text{mode}[x] = \underset{x\in\mathcal{X}}{\text{argmax}} p(x)
$$

#### 分散
平均からのずれの二乗の期待値。  
分布の散らばり具合の指標。

$$
\text{Var}[x] = \mathbb{E}[(x-\mathbb{E}[x])^2] = \mathbb{E}[x^2] - \mathbb{E}[x]^2
$$

#### 共分散
2変数の平均からのずれの積の期待値。  
2変数の相関を示す指標。正であれば同じ振る舞い、負であれば逆の振る舞いをする。

$$
\text{Cov}[x, x'] = \mathbb{E}[(x-\mathbb{E}[x]) (x' - \mathbb{E}[x'])  ]
$$



## カルバック・ライブラー・ダイバージェンス

KLダイバージェンス。  
2つの確率分布p(x)とq(x)があったとき、その確率分布間の非類似度を示す。

$$
KL(p(x), q(x)) = \sum_x p(x) \log \frac{p(x)}{q(x)}
$$

p(x)とq(x)が同じ分布であるとき、$KL(p,q)=0$。  




## 連続確率変数

### 確率密度関数

連続値をとる確率変数Xのとき、aからbの間をとる確率は

$$
p(a \leq X \leq b) = \int^b_a p(x) dx
$$

$p(x)$を **確率密度関数** と呼ぶ

すべての範囲で積分すると1になる

$$
\int^{\infty}_{-\infty} p(x) dx = 1
$$

### 連続型において
連続の場合、離散変数における和を積分に置き換えると、同様に周辺化、期待値、KLダイバージェンスの計算が可能。

- 期待値

$$
\mathbb{E}[f(x)] = \int_{x\in\mathcal{X}} p(x) f(x) dx
$$


#### 連続型におけるベイズの定理

ベイズ統計学で使われる事例に合わせて、$x$をデータ、$\theta$をパラメータとすると、**離散** の場合、分母に関して周辺化を行って以下の式で表せる。

$$
p(\theta_k|x) = \frac{p(x|\theta_k)p(\theta_k)}{\sum^K_{k=1} p(x|\theta_k)p(\theta_k)}
$$

$p(\theta_k|x)$ : 事後確率  、$f(x|\theta_k)$ : 尤度   、$p(\theta_k)$   : 事前確率  
$\sum^K_{k=1} p(x|\theta_k)p(\theta_k)$ : 周辺尤度 

**連続** の場合は、**和を積分に置き換えた形** になる。

$$
p(\theta|x) = \frac{p(x|\theta)p(\theta)}{\int_{\theta} p(x|\theta)p(\theta) d\theta}
$$

$p(\theta|x)$ : 事後分布  、$f(x|\theta)$ : 尤度   、$p(\theta)$   : 事前分布  
$\int_{\theta} p(x|\theta)p(\theta) d\theta$ : 周辺尤度 

$x$が定数であり、$\theta$で積分しているため、周辺尤度は定数になる。  
よって、$p(\theta|x)$ はベイズの定理の分子に比例する。

$$
p(\theta|x) \propto f(x|\theta)p(\theta)
$$
