# ワードクラウドでの可視化

2019/11/30

## 概要
よく見るワードクラウドをpythonを使って可視化する方法に関して。

## 準備

```sh
pip install wordcloud
```
condaにはなかった

通常では日本語は文字化けするため、フォントの指定をする必要がある。  
WSLだとひと手間必要になる点に注意。この記事の一番下に記述する。

参考:  
[WSLに開発環境完全移行してみる](https://qiita.com/LeftLetter/items/0eda1834a46c3b3bff60)


## プログラム
font_pathは環境によって正しいものに書き換える必要あり。

半角スペース区切りの文章を渡す場合は以下。
```py
from wordcloud import WordCloud

font_path = "/usr/share/fonts/windows/yumin.ttf"
wordcloud = WordCloud(width=480, height=320, background_color='white', font_path=font_path)

text = 'dog cat monkey'
wordcloud.generate(text)
wordcloud.to_file('wordcloud.png')
```

単語とその値がペアとなった辞書を渡す場合は以下。
```py
from wordcloud import WordCloud

font_path = "/usr/share/fonts/windows/yumin.ttf"
wordcloud = WordCloud(width=480, height=320, background_color='white', font_path=font_path)

# 単語がキー、出現頻度が値となった辞書を渡す。
words = {'いぬ': 0.2, 'ねこ': 0.4, 'さる': 0.7}
wordcloud.fit_words(words)
wordcloud.to_file('wordcloud.png')
```

## WSL使用時のフォントの指定

```sh
sudo apt install -y fontconfig
sudo ln -s /mnt/c/Windows/Fonts /usr/share/fonts/windows
sudo fc-cache -fv
```

ここで,
```sh
fc-list
```
すると、Windows側のフォントが追加できていることが確認できる。
プログラムのフォントのパスにはこれを指定する。


- - - 
おわりー