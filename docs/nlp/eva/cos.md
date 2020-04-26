# コサイン類似度を測る
2019/07/12

## 概要
作成したベクトルの類似度を測るのに使用する。  
ユークリッド距離などではなく、コサイン類似度(距離)を使うことが多い。
数式は以下の通り。

$$
\cos(\vec p, \vec q) = \frac{\sum_{i=1}^{|V|}p_i q_i}{\sqrt{ \sum^{|V|}_{i=1}p_i^2}  ・  \sqrt{ \sum^{|V|}_{i=1}q_i^2} }
$$

## プログラム1

```py
list1 = [1,2,1,0]
list2 = [1,0,2,1]

import numpy as np
def cul_cos(vec1, vec2):
    vec1,vec2 = np.array(vec1), np.array(vec2) 
    numer = np.sum(vec1 * vec2) # 分子
    denom = np.sqrt(np.sum(vec1**2)) * np.sqrt(np.sum(vec2**2)) # 分母
    return numer/denom

print("cos:",cul_cos(list1,list2))
```

## プログラム2

scipyを利用する。
<!-- scipy.spatial.distance.cosine -->
```py
list1 = [1,2,1,0]
list2 = [1,0,2,1]
vec1, vec2 = np.array(list1), np.array(list2)
from scipy import spatial
cos_sim = 1 - spatial.distance.cosine(vec1, vec2)
```
