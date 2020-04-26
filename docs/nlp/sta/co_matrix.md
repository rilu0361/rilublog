# 共起行列の作成

2019/07/14

## 概要
特定の単語の周辺語の頻度を見る(共起している単語を見る)ことで、単語の特徴を疑似的に表す。  

分布仮説に従う。

> ” words that occur in the same contexts tend to have similar meanings ” (Harris, 1954).  
(同じ文脈上に現れる単語は同じような意味を持つことが多い)

単語は周辺の単語によってその単語たらしめるというような感じ。  

## プログラム

例文の分割
```py
text = 'This is a pen'
words = text.split() # 空白がある度に分割
print(words)
```

単語にIDを付与する。
```py
word2id = {}
id2word = {}
#単語リスト内の各単語でループを回す
for word in words:
    if word not in word2id: #単語→単語ID の辞書に登録されていない単語ならば
        new_id = len(word2id)#新たな単語の単語IDを作成
        word2id[word] = new_id #単語をkey,IDをvalueとして辞書に登録
        id2word[new_id] = word #IDをkey,単語をvalueとして辞書に登録
        
print(word2id)
print(id2word)
```

例文を単語ID列に置換
```py
import numpy as np
corpus = [word2id[w] for w in words]
corpus = np.array(corpus)
print(corpus)
```

共起行列の作成  
まずは0を要素とする共起行列の形を作る。
```py
vocab_size = len(word2id) #語彙数
corpus_size = len(corpus)    #コーパスサイズ(文の総単語数)
co_matrix = np.zeros((vocab_size, vocab_size)) #語彙数×語彙数の零ベクトルを定義
```

共起される語を数え、共起行列を完成させる。
```py
window_size = 1 # 左右どこまで見るか
# idxは参照しているindex,word_idは参照する単語IDとなる
for idx, word_id in enumerate(corpus):
    #windosサイズ1つ毎に操作を行う
    for i in range(1, window_size + 1):
        left_idx = idx - i #左の位置を定義
        right_idx= idx + i #右の位置を定義

        if left_idx >= 0: # 左側に単語が存在する場合
            left_word_id = corpus[left_idx]   # 左側の単語IDを取得
            co_matrix[word_id, left_word_id] += 1 # [単語ID,左の単語ID]に一致する要素に+1

        if right_idx < corpus_size: # 右側に単語がある場合
            right_word_id = corpus[right_idx] # 右側の単語IDを取得
            co_matrix[word_id, right_word_id] += 1 # [単語ID,右の単語ID]に一致する要素に+1
            
print(co_matrix)
```
