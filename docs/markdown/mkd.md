# markdown記法の基本

## 見出し
```md
# 見出し1
## 見出し2
### 見出し3
```
# 見出し1
## 見出し2
### 見出し3

## 改行
行の最後にスペースを2つ入れる。
または、空行をはさむ。
`\\` を文末に記述する場合もある。

```md
1行目  
2行目
```
1行目  
2行目

## 線を引く
```md
- - -
```
- - -

## リスト
```md

- ひとつ
    * ふたつ
- みっつ
```

- ひとつ
    * ふたつ
- みっつ

## コードブロック
````
```py
print("aaa")
```
````

```py
print("aaa")
```

## インラインのコードブロック
```md
`print("aaa")`
```
`print("aaa")`

## 引用
```md
> これは引用です
```

> これは引用です

## 文字の装飾など
```md
通常
**太字**
_ストライド_
~~取り消し線~~
```
通常
**太字**
_ストライド_
~~取り消し線~~

## チェックボックス
チェックの[x]はx(エックス)です。
```md
- [ ] チェック1
    - [x] チェック済み
- [ ] チェック2
```

- [ ] チェック1
    - [x] チェック済み
- [ ] チェック2

## 表・テーブル

```md
|hoge  |fuga  |piyo  |
|:----:|:----:|:----:|
|1     |2     |3     |
|
|7     |8     |9     |
```

|hoge  |fuga  |piyo  |
|:----:|:----:|:----:|
|1     |2     |3     |
|
|7     |8     |9     |

## 画像の挿入
![日々草](image/nichi)


