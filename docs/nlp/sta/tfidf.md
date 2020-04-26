# TF-IDF


## 概要
ある文書中の単語の頻度(term frequency; TF)と、ある単語が文書に出現する頻度(document freqency; DF)を使って特徴のある単語を統計的に見つけることができる。

基本的な考え方として、単語の出現頻度が高いほど重要そうだという考え方と、特定文書にしか出現していない単語はその文書を特徴付ける単語であるという考え方が元になっている。


## プログラム(sklearn利用)

```py
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

docs = ["I have a pen.",
        "You have an apple",
        "He make a pen"]

vectorizer = TfidfVectorizer(use_idf=True, smooth_idf=True, lowercase=True, token_pattern=u'(?u)\\b\\w+\\b')
vecs = vectorizer.fit_transform(docs)

print("語彙 : ",vectorizer.get_feature_names())
print("IDF : ",vectorizer.idf_)
print("Stop words: ",vectorizer.stop_words_)
print("語彙とindexの辞書: ", vectorizer.vocabulary_)

# print(vecs.toarray())

for doc, vec in zip(docs, vecs):
    print(doc)
    print(vec.toarray())

## index順にソートして表示
# for k,v in sorted(vectorizer.vocabulary_.items(), key=lambda x:x[1]):
    # print(k,v)
```

`token_pattern` をこのように指定しておかないと1文字が除去されてしまう。  
英語においてはそれでいいかもしれないが、日本語で処理するときは問題がありそうなので注意する。

すべて小文字にするのがデフォルトであったり、色々と注意すべき点も多いので、自分で書いたほうが意外に安心かもしれない。

オプションでidfを使うか、idfの値をスムージングするかなどが決められる。デフォルトの指定がどうなっているか気にしておかないと、計算式が違ったりするので注意。

以下出力結果

```sh
語彙 :  ['a', 'an', 'apple', 'have', 'he', 'i', 'make', 'pen', 'you']
IDF :  [1.28768207 1.69314718 1.69314718 1.28768207 1.69314718 1.69314718 1.69314718 1.28768207 1.69314718]
Stop words:  set()
語彙とindexの辞書:  {'i': 5, 'have': 3, 'a': 0, 'pen': 7, 'you': 8, 'an': 1, 'apple': 2, 'he': 4, 'make': 6}
I have a pen.
[[0.45985353 0.         0.         0.45985353 0.         0.60465213     0.         0.45985353 0.        ]]
You have an apple
[[0.         0.52863461 0.52863461 0.40204024 0.         0.       0.         0.         0.52863461]]
He make a pen
[[0.42804604 0.         0.         0.         0.5628291  0.       0.5628291  0.42804604 0.        ]]
```

## プログラム2

tf値を求める

```py
docs = ["I have a pen.",
        "You have an apple",
        "He make a pen"]

all_tf_list = []
for doc in docs:
    tf_dict = {}
    # words = [token.surface for token in t.tokenize(doc) if token.part_of_speech.split(',')[0] == "名詞"]
    words = doc.split() # 分かち書き
    for word in words:
        if word not in tf_dict:
            tf_dict[word] = 0
        tf_dict[word] += 1
    norm_tf_dict = {} # 正規化tf
    for key, value in tf_dict.items():
        norm_tf_dict[key] = value / len(words)
    all_tf_list.append(norm_tf_dict)
all_tf_list[0]
```

DF値を求める。

```py
df_dict = {}
for doc in docs:
    # words = [token.surface for token in t.tokenize(doc) if token.part_of_speech.split(',')[0] == "名詞"]
    words = doc.split()  # 分かち書き
    for word in set(words):
        if word not in df_dict:
            df_dict[word] = 0
        df_dict[word] += 1
print(df_dict)
```

IDF値を求める。

```py
import math
idf_dict = {}
for word in df_dict.keys():
    idf_dict[word] = math.log(len(docs) / df_dict[word] ) + 1
print(idf_dict)
```

TF-IDF値を求める
```py
all_tfidf_list = []
for tf_dict in all_tf_list:
    tfidf_dict = {}
    for word, tf in tf_dict.items():
        tfidf_dict[word] = tf * idf_dict[word]
    all_tfidf_list.append(tfidf_dict)
```

確認(0番目の文書のtfidf)

```py
for key, value in all_tfidf_list[0].items():
    print(key, value)
```


<!-- ## プログラム3 -->

<!-- 
gensimのtfidfは以下の式で計算される

$$
\text{tfidf} = \text{tf}_{i,j} * \log_2(\frac{|D|}{\text{df}_i})
$$

$\text{tf}_{i,j}$ :  文書jの中の単語iの出現回数(頻度)

$\text{df}_i$  : 単語iがいくつの文書に出現するか

$|D|$ : 文書数 -->

