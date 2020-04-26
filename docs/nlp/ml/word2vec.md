# word2vec
2019/07/17

## 概要
単語をベクトル表現する。  

## 導入

gensimのword2vecを使用する。
```sh
conda install gensim
```

## プログラム

```py

docs = ["I have a pen.",
        "You have an apple",
        "He make a pen"]
sentences = [text.split() for text in docs]

from gensim.models import Word2Vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

VECTOR_DIM = 100
model = Word2Vec(sentences, iter=50, min_count=1, size=VECTOR_DIM, workers=6, sg=1)
print("model : " ,model)

model.save("w2v_model")
print("w2v_modelとして単語ベクトルのセーブを完了。")
```

## モデルのロードとテスト

#### ベクトルの確認
```py
from gensim.models import Word2Vec
model = Word2Vec.load("w2v_model")
print("単語例:",list(model.wv.vocab)[0:10]) # 前10単語の表示
print("語彙数:",len(model.wv.vocab)) # 学習された語彙数
print(model.wv["紅茶"]) # 紅茶のベクトル
```

#### 類似する単語を見つける

```py
word = "紅茶" # 単語
results = model.wv.most_similar(positive=[word])
for result in results:
    print(result)
```

#### 単語同士の類似度を調べるs

```py
word1 = "紅茶"
word2 = "烏龍茶"
print(word1, word2,'の類似度')
print(model.similarity(word1, word2))
```