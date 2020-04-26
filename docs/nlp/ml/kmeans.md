# kmeansによるクラスタリング
2019/07/17

## 概要
k-means法によるクラスタリング

## 導入
`from sklearn.cluster import KMeans` を使う。

```sh
conda install scikit-learn
```
が必要。

## kmenas with tfidf

```py

import numpy as np
import pandas as pd
df = pd.read_excel("new_sample.xlsx")

# 文書IDを格納
vecs_label = df.index

# ベクトルを作成する
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(use_idf=True, smooth_idf=True, lowercase=True, token_pattern=u'(?u)\\b\\w+\\b')
vecs = vectorizer.fit_transform(df["text"])
vecs_array = np.array(vecs)
print("語彙 : ",vectorizer.get_feature_names())
print("IDF : ",vectorizer.idf_)
print("Stop words: ",vectorizer.stop_words_)
print("語彙とindexの辞書: ", vectorizer.vocabulary_)

# k-means法の実行
from sklearn.cluster import KMeans
clusters = KMeans(n_clusters=2, random_state=0).fit_predict(vecs)

# Excelに格納
dic = {"cluster":clusters,
        "text":df["text"]}
df_new = pd.DataFrame(dic, index=vecs_label)
df_new.to_excel("kmeans_tfidf.xlsx")
```
