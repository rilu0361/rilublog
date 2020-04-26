# Tkinter

python の標準ライブラリなので何もinstallせずに使えるのがgood.

## 概要
`Frame` と `Widget` の２要素で主に構成していく。  
Frame はたいていの場合ウィンドウとして振る舞う。  
widget はボタンとかテキストボックスとかいう部品のこと。  

Frameクラスを継承したクラスを作成し、そのクラスにメソッドを定義し、機能を追加していく。

イベントドリブン（イベント駆動）で、イベント（ユーザの操作）をきっかけにプログラム(イベントハンドラ、コールバック関数)が動く。


## 参考
みんなのpython 第３版 p425~  
[お気楽 Python/Tkinter 入門](http://www.geocities.jp/m_hiroi/light/pytk01.html)  
[PythonのTkinterを使ってみる](https://qiita.com/nnahito/items/ad1428a30738b3d93762)  

# ウィンドウ(Frame)を作成する

```py
import tkinter as tk

f = tk.Tk()
f.mainloop()
```

ウィンドウができる。

`mainloop()` を呼ぶことで、Frameがユーザの操作を受け付けるようになる。（イベントループの開始）  
同時にシェルの入力が停止する。ウィンドウを閉じれば制御が戻る。

`Tk()` はクラス Tk のインスタンス（オブジェクト）を生成して返す。  
このインスタンスに部品（ウィジェット）を置いていく。

#### 備考
`import Tkinter` と言ってるのは,Python2系なので注意。
3系になってからは小文字(tkinter)になった。

## タイトルの追加
ウィンドウの上のバーに表示されるやつ。 

```py
f.title("Title")
```

英語じゃないと文字化けする罠。なぜ?

## ウィンドウの大きさ指定
```py
f.geometry("400x300")
```

# widgetの追加

ウィジェットには以下のものがある。

|クラス名|説明|
|:--:|:--:|
|Frame| ウィジェットを格納する枠組みを作る|
|Label	| 文字列やイメージを表示する|
|Message	| 複数行の文字列を表示する|
|Button	| ボタンを作る|
|Radiobutton	| ラジオボタンを作る|
|Checkbutton	| チェックボタンを作る|
|Listbox	| リストボックスを作る|
|Scrollbar	| スクロールバーを作る|
|Scale	| スケールを作る|
|Entry	| 1 行の文字列の入力と編集|
|Menu	| メニューを作る|
|Menubutton	| メニューボタンを作る|
|Bitmap	| ビットマップを作る|
|Canvas	| キャンバスを作る|
|Text	| テキストの入力と編集|
|LabelFrame	| ラベル付きフレーム|
|Spinbox	| スピンボックスを作る|
|PanedWindow	| ペインウィンドウを作る|

基本はこう。

```py
widget = widgetClass(parent, option = value, .... )
```

`parents` ：　メインウィンドウとか他のウィジェットのオブジェクトとか

`option = value` で指定するもの。

|オプション名|説明|
|:--:|:--:|
|foreground (fg)	|文字や線を描くのに使用する色を指定|
|background (bg)	|背景色の指定|
|text	|ウィジェット内に表示されるテキスト|
|textvariable	|テキストを格納するオブジェクトを指定|
|image	|ウィジェット内に表示されるイメージ|
|bitmap	|ウィジェット内に表示されるビットマップ|
|borderwidth (bd)	|ウィジェットの枠の幅|
|relief	|ウィジェットの枠のスタイル|
|height	|ウィジェットの高さ|
|width	|ウィジェットの幅|
|anchor	|ウィジェットや表示されるデータの位置を指定|

ウィジェットの幅と高さは、テキストを表示するウィジェットでは文字数。
それ以外のウィジェットはピクセル単位。

## ボタンの追加
```py
b = tk.Button(f, text="exit")
b.pack()
```

### ボタンの複数生成
```py
for x in range(4):
    button = tk.Button(f, text = "Button %d" % x, command = make_cmd(x))
    button.pack()
```

コールバック関数
```py
def make_cmd(n):
    return lambda : buff.set('button %d pressed' % n)
```

## ラベル

```py
la = tk.Label(text='test')
la.pack()
```

## スケール(スライダ)

|オプション|説明|
|:--:|:--:|
|label|スケールのラベル|
|from_|スケールの最小値|
|to|スケールの最大値|
|orient|v (h, v)スケールの方向|
|showvalue|値を表示するか|
|variable| スケールの値を格納するオブジェクトを指定|
|command|値が変化したときに実行するコマンド|
|resolution|解像度|

`variable` は整数値を扱う場合、`IntVar()` を使用

|メソッド|説明|
|:--:|:--:|
|coords(value)|指定した値に対応するぐらいだの座標をタプルで返す(x,y)|
|get(x,y)|指定した座標に対応するスケールの値を返す。引数なしで現在地を返す|
|set(value)|スケールの値をvalueに変更|
|identify(x,y)|指定した座標にスライダがあれば文字列 slider を返す。 スライダより上（左）にあれば trough1 を返し、下（右）にあれば trough2 を返す。|

あとでもう少しどうにかしたい↓
```py
import tkinter as tk

f = tk.Tk()
f.title("Title")
blue.set(0)
green = tk.IntVar()
green.set(0)

def change_color( n ):
    color = '#%02x%02x%02x' % (red.get(), green.get(), blue.get())
    button.configure(bg = color)

# ボタン
button = tk.Button(f, text = 'button', bg = '#000')
button.pack(fill = 'both')

# スケール
s1 = tk.Scale(f, label = 'red', orient = 'h',
           from_ = 0, to = 255, variable = red,
           command = change_color)

s2 = tk.Scale(f, label = 'blue', orient = 'h',
           from_ = 0, to = 255, variable = blue,
           command = change_color)

s3 = tk.Scale(f, label = 'green', orient = 'h',
           from_ = 0, to = 255, variable = green,
           command = change_color)

# ウィジェットの配置
s1.pack(fill = 'both')
s2.pack(fill = 'both')
s3.pack(fill = 'both')

f.mainloop()
```

## ウィジェットコマンド
ウィジェットを操作するコマンドのこと。

### オプションの値の参照
```py
widget.cget(option_name)
```
`cget()` の `option_name` はオプションを文字列で指定。

### オプションを後から変更する
`configure()` を使用。
```py
widget.configure(option = value, ...)
```

## 配置(ジオメトリマネージャー)

#### `pack()`

上から順に積んでいく。中身によってウィンドウの大きさも変化。

```py
widget.pack()
```

オプション  
- fill
ウィンドウいっぱいに広がる。x,y,both で指定できる。  
- side
積み込み方向を変更する。指定できるのは `top` , `left` ,`right` , `bottom` の４つ

```py
widget.pack(fill="y",side="left")
```

もしくは`anchor` を使う。  
中央は`c` そのほかは東西南北で表現する。

nw,n,ne,w,c,e,sw,s,se
```py
widget.pack(anchor="ne")
```

#### `place()`

x座標,y座標を指定し、任意の値における。
```py
widget.place(x=40, y=50)
```

#### `grid()`

格子状に配置。ものによってウィンドウの大きさも変化。

```py
widget.grid()
```

## コールバック関数

`command 関数` で指定する。
例えばボタンを押したときに終了するものは

```py
b = tk.Button(f, text="終了", command=lambda: sys.exit())
```

こういうとき`lambda` の出番。

## 色

大文字小文字の区別はなし。
red,green,blue などでも指定できるが、16進数でも指定可能。
その場合は`#RGB` もしくは`#RRGGBB` という感じで指定する。
`#RRRRGGGGBBBB` とかも指定可能。

```py
label = tk.Label(text='これはtestです。', fg="red", bg="#aabb33")
```

## フォント

フォントの指定はタプルでできる。
`(font , size, style1 , style2)`
`style1` : `normal` , `bold` , `roman` , `italic`
`style2` : `underline` , `overstrike`

```py
label = tk.Label(text='これはtestです。',  font=('ＭＳ ゴシック', 16, 'bold', 'underline'))
```

### 色やフォントのデフォルト設定をいじる(全体に適用する)

`widget.font` みたいな感じで対象指定できる。

```py
f.option_add('*font',('FixedSys 14',30))
f.option_add('*Label.font', ('ＭＳ ゴシック',20,'italic'))
f.option_add('*Button.background', 'yellow')
```

# イベント

ユーザの操作のこと。  
特定のイベントが起こった時に、あるメソッドを呼び出したいときはwidgetオブジェクトに対して`bind()` しておく。

# クラスを利用する方法

```py
import tkinter as tk

class App(tk.Frame):
    def init(self):
        button = tk.Button(self, text = "Python/Tkinter")
        button.pack()

    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.init()

app = App()
app.mainloop()
```
