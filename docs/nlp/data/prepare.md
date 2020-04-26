# 前処理の一連の流れ
2019/07/12

## 概要
自然言語処理における前処理の流れを示す。  
これでいいのか確証は特にない。

## 流れ

1. データの読み出し  
[データの読み出しと保存](textdata.md)  
2. 半角/全角の統一  
[半角全角変換](zenhan.md)    
3. アルファベットの小文字統一  
[ストップワードの除去](stopword.md)  
4. 単語ごとにパース   
[mecabを使用する](mecab_usage.md)  
5. 数字の除去(場合による)  
[ストップワードの除去](stopword.md)  
6. ストップワードの削除  
[ストップワードの除去](stopword.md)  
7. データの保存  
[データの読み出しと保存](textdata.md)  

## 一連のプログラムのまとめ

データは .txtファイルに1文改行ごとにあるとする。
`sample.txt` というファイルを読み込むとする。  
最終的に処理済みのテキストをexcelファイルに落とし込む。  
途中経過を見るために tqdm を使用していることに注意。  
tqdmに関しては以下を参照のこと。  
[プログレスバーの表示](../python/tool/progress.md)

```py
# 文字列の正規化(前処理)
import mojimoji
import re, regex
def norm(text):
   # 日本語は全角、数字アルファベットは半角
   text = mojimoji.zen_to_han(text,kana=False)
   text = mojimoji.han_to_zen(text,digit=False,ascii=False)
   text = text.lower() # アルファベットを小文字に統一
#    text = re.sub("\d","", text) # 数字の除去
   text = ''.join(regex.findall(r'[\p{Han}&&\p{Katakana}&&\p{Hiragana}&&\p{L}&&\d&&\s]',text))
   return text

# 分かち書きの関数
import MeCab
mecab = MeCab.Tagger("-Owakati")
def wakati(text : str) -> list[str]:
    text = mecab.parse(str(text))
    return text.split()

# ファイルの読み込み
READ_FILE_PATH = 'sample.txt'
with open(READ_FILE_PATH, 'r') as f_r:
    text_list = f_r.readlines()

# stopwordの設定
# stop_word_list = ["*"]

# 前処理
from tqdm import tqdm
import re
split_texts = []  # 単語ごとにスペース区切りしたテキスト集合
for line in tqdm(text_list):
    line  = norm(line)    # 正規化
    words = wakati(line)  # 分かち書き
    # words = [word for word in words if word not in stop_word_list] # ストップワードの除去
    split_text = ' '.join(words) # スペース区切りのテキストに変更
    split_texts.append(split_text)

# データフレームに変換
dic = {"text":words_list}
df = pd.DataFrame(dic)
df.head() # 確認用

# 保存
df.to_excel("new_sample.xlsx")
```



