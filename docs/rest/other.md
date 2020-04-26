# その他

## Rubric

    .. rubric::
        文章の構造に対応していない見出しとして使用できる


## 今日


    |today|

|today|

## バージョン

    |version|

|version|


## リリース

    |release|

|release|


## スタイルシートの適用

例えば、取り消し線などはcssを適用しないとダメっぽい。
以下取り消し線の適用

1. `_static` 内に `mycss.css` を作成。

2. `mycss.css` に以下を記述

```css
.strike {
    text-decoration: line-through;
}
```

3. `conf.py` に以下を記述

```py
def setup(app):
    app.add_stylesheet('strike.css')
```

4. 使用するページにてロールを追加
```rest
.. role:: strike
```

5. 使用する
```rest
:strike:`取り消したい文章`
```

~~取り消したい文章~~