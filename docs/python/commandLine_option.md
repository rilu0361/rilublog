# コマンドライン引数を使ってオプションを指定する
2018/05/07

## sys.argv

```py
import sys

args = sys.argv

print(args)
print('第１引数：' + args[1])
print('第２引数：' + args[2])
print('第３引数：' + args[3])
```
結果
```
$ python test_par.py あ い う
['test_par.py', 'あ', 'い', 'う']
第１引数：あ
第２引数：い
第３引数：う
```

[コマンドライン引数](https://www.python-izm.com/basic/command_line_arguments/)

## argparseの使用方法

オプションを作成するのに使用した。

### 基本
```py
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
```
これだけで`-h`,`--help` を勝手に作ってくれるので素敵。
ヘルプには「使用方法(usage)」と「オプションの引数」の説明が書かれる。
```sh
$ python test_par.py -h
usage: test_par.py [-h]

optional arguments:
  -h, --help  show this help message and exit
```
ヘルプの
`optional argument` がオプションで、指定しなくてもしてもいいもの。
`positional argument` が位置引数。指定必須。

#### 位置引数

```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("hoge")
args = parser.parse_args()
print(args.hoge)
```
コマンドライン引数に例えば`aaaaaaa`を入れたら、それを`args.hoge`で呼び出せる。
```
$ python test_par.py aaaaaaa
aaaaaaa
```

なにかを入れないとエラーが出る。
```
$ python test_par.py
usage: test_par.py [-h] hoge
test_par.py: error: the following arguments are required: hoge
```
ヘルプを見ると追加されていることが分かる。
```
$ python test_par.py --help
usage: test_par.py [-h] hoge

positional arguments:
 hoge

optional arguments:
 -h, --help  show this help message and exit
```
この状態では`hoge`の説明が何も書かれていないので`help`を指定する。
```py
parser.add_argument("hoge",help='hogeの説明')
```
以下のようになる。
```
positional arguments:
  hoge        hogeの説明
```
と追加される。

引数でひっぱってくるのは、文字列なので注意。
数字を入れたい場合は`type=int`の指定をする。
```py
parser.add_argument("hoge",help='hogeの説明',type=int)
args.hoge**2
```
引数に`int`を指定しているので`args.hoge`を`**2`すると数値を入れれば２乗の値が返ってくる。文字列を入れても数値の操作をしないならエラーは出ない。
`args.hoge`に入れる段階でエラーが出ているわけではなく、それに数値的な操作を行うときにエラーが出る。
```
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
```

#### Optional引数の導入
```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--fuga",action='store_true', help="せつめい")
args = parser.parse_args()
if args.fuga:
    print("fuga turned on")
```
`--fuga` を引数に指定すると`if`の中のプログラムが動く。

```
$ python test_par.py --fuga
fuga turned on
```

`action='store_true'`が必須。この指定により、オプションが指定されたとき`args.fuga=True`になる。値を指定するとエラー。
ヘルプを見てみると追加されていることが分かる。

```
$ python test_par.py -h
usage: test_par.py [-h] [-f fuga]

optional arguments:
  -h, --help            show this help message and exit
  --fuga fuga
                        せつめい
```

`parser.add_argument("-f","--fuga", help="せつめい")` とすれば `-f`でも同じものが指定できるようになる。

`-h` を新しく指定することはできない。(すでに`help`があるため)

```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--fuga",'-f',type=int, help="せつめい")
args = parser.parse_args()
if args.fuga == 1:
    print("fuga turned on")
```
`action = 'store_true'` を `type=int` に変更するとオプションの後に数値を指定させられるようになり、`args.fuga`にはその数値が入る。

```
$ python test_par.py -f 1
fuga turned on
```
何も数値が指定されない場合、`args.fuga`は`None`になるため、エラー。
デフォルトの値を設定しておくために以下のように変更する。
```py
parser.add_argument("--fuga",'-f',type=int, default=1 ,help="せつめい")
```
これでオプション`-f`が指定されないとき`args.fuga`はデフォルトの値になる。
`-f`が指定されているのに`-f`に引数がないときはエラーになることに注意。

`action=count`の場合、そのオプションの指定回数がとれる。

```
$ python3 prog.py 4 -ff
the square of 4 equals 16
```

#### 位置引数とoptional引数の併用

```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-f", "--fuga", action="store_true",
                    help="increase output fuga")
args = parser.parse_args()
answer = args.square**2
if args.fuga:
    print("the square of {} equals {}".format(args.square, answer))
else:
    print(answer)
```
`square`は位置引数、`varbose`がoptional引数。
コマンドラインに`-f`を指定したら`if args.fuga`以下が実行される。
指定しなければ`else`以下を実行。

`square`は位置引数で何か値が入っていないとダメなので、何も引数がないとエラー。


## もう少し応用

混在するとまずいオプション。

```py
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))
```

今回重要`group`。`-v`と`-q`が一緒にあるとまずいもの同士。
混在した場合の出力結果は以下。

```sh
$ python3 prog.py 4 2 -vq
usage: prog.py [-h] [-v | -q] x y
prog.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
```

ヘルプの中身のusageの部分も変わっている。  
`|`でどっちかしか使えないことを示している。

```sh
usage: test_par.py [-h] [-v | -q] x y
```

[Argparse チュートリアル](https://docs.python.jp/3/howto/argparse.html#id1)

