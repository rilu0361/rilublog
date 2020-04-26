# 次元削減
2018/07/02
2018/08/20 追記

### 参考
[【python】pca、mds、nmds、tsneとmatplotlibでデータの可視化をしてみる)](https://hayataka2049.hatenablog.jp/entry/2017/02/26/182916)

### PCA
```py
from typing import List
from sklearn.decomposition import PCA
def pca(vectors:List[List[float]]) -> List[List[float]]:
    pca = PCA(n_components=2)
    return pca.fit_transform(vectors)
```
> 主成分分析（PCA）:
データの特異値分解を用いた線形次元削減により、より低次元の空間に投影することができる。  
[sklearn.decomposition.PCA ](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA)

AutoEncoder がPCAの上位互換になるらしいという話を聞いたのでAutoEncoderをやるべきかも？  

### t-SNE
```py
from typing import List
from sklearn.manifold import TSNE
def tsne(vectors:List[List[float]]) -> List[List[float]]:
    tsne = TSNE()
    return tsne.fit_transform(vectors)
```
> t-SNE(t-distributed Stochastic Neighbor Embedding) :
(1)高次元空間上の類似度 と (2)低次元空間上の類似度 をそれぞれ確率分布 $p_{ij}$ と $q_{ij}$ で表現して， $p_{ij}$ と $q_{ij}$ を最小化するように確率分布のパラメータを最適化します．  
[引用：t-SNEによるイケてる次元圧縮&可視化](https://qiita.com/stfate/items/8988d01aad9596f9d586)

「可視化」ということに重点を置いた手法。実はグラフ上の距離が正しくないとかいう話を見たが、詳しいことまで勉強してないので不明。

グラフを読み解く際の注意点  
[高次元のデータを可視化するt-SNEの効果的な使い方](https://deepage.net/machine_learning/2017/03/08/tsne.html)

上のリンクの記事にも書いてあった通り、上手く可視化できないときはパラメータをいじるといいかも。  
ということで、以下公式のリンク。  
パラメーター関連  
[sklearn.manifold.TSNE](http://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)

perplexity, learning_rateあたりはいじれそうなので、いろいろ試してみたり。  
perplexityは元論文で5～50が推奨されているらしく、デフォルトで30なので元から妥当なところ感があるので果たしてという感じ。  
learning_rateはデフォルトで200。  

```py
TSNE(perplexity=30, learning_rate=200)
```

引数を何もとらないデフォルトで上記の指定と同じ状態。中身の数値をいじれば多少変化があるかも。  
文書分類の際いろいろやってみたが、結局綺麗に可視化できなかったのでよくわからない。  
元のベクトルの次元が大きすぎた気がする。  

次元の呪い についてなどもう少し調べるべきなのかもしれない。

### 補足
```py
if(vectors.shape[1] > 15):
    vectors = PCA(n_components=15).fit_transform(vectors)
```
計算コストを減らすために上記を各々の関数に追記するのもあり？  
PCAで15次元程度に落としてからやるらしい。  
元論文でこの方法は推奨されているらしく、ライブラリの中で元から実装されている可能性あり。なのであえてやる必要ない？  

> 可視化を主な目的とした次元削減の問題は，「高次元空間上の類似度をよく表現する低次元空間の類似度を推定する」問題



<!-- #### MDS
```py
from sklearn.manifold import MDS
def mds(vectors):
    mds = MDS(n_jobs=4)
    return mds.fit_transform(vectors)
```
> 多次元尺度法 (MDS: multi-dimensional scaling) :
 個体間の親近性データを、2次元あるいは3次元空間に類似したものを近く、そうでないものを遠くに配置する方法で、データの構造を考察する方法である。
[引用：Rと多次元尺度法](https://www1.doshisha.ac.jp/~mjin/R/Chap_27/27.html)

#### NMDS
```py
from sklearn.manifold import MDS
def nmds(vectors):
    nmds = MDS(metric=False, n_jobs=4)
    return nmds.fit_transform(vectors)
```
> 非計量（Non-metric）MDS：
NMDS、nMDS、またはNMSなどと略される。非類似度の順序関係と低次元空間上でのユークリッド距離の順序関係が一致するような布置を探すノンパラメトリックなMDS。単調性を保つような操作の典型はIsotonic回帰であり、Louis Guttmanの最小空間解析（smallest space analysis, SSA）などがある。
[引用：MDSとその愉快な仲間たち](http://d.hatena.ne.jp/fronori/20140517) -->
