# pyenvでの環境構築
2018/03/07

**環境**
- Ubuntu16.04LTS
(WSL(Windows Subsystem for Linux))

## pyenv
pythonの環境管理のために導入。

## 必要なもののインストール
openSSL他、必要なパッケージをインストールするらしい。
```sh
sudo apt install git gcc make openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev
```
これをしてないとpythonのインストール時にエラーが出る可能性が。対処方法はそのエラーにのっているのでエラーに出会ってからやってもいいかもしれない。

gitのインストール
```sh
sudo apt install git
```

## pyenvのインストール
gitからpyenvの構成ファイルをダウンロード
```sh
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
```

```sh
vim ~/.bashrc
```
で/.bashrcを開く。

vimがないって言われた場合は他のでやるかvimをインストールする。
```sh
sudo apt install vim
```
でできる。

下記のものを書き込む。中身の一番下にでも書いておけばいい。

vim は `i`で編集モードに、`esc`で編集モードから抜ける。
編集モードから抜けた状態で`:wq`と打つことで保存して終了する。
```
export PYENV_ROOT=$HOME/.pyenv
export PATH=$PYENV_ROOT/bin:$PATH
eval "$(pyenv init -)"
```
書き換え後は端末を再起動するか
```sh
source ~/.bashrc
```
で、更新する。

## pyenv-virtualenvのインストール
gitからpyenv-virtualenvの構成ファイルをダウンロード
```sh
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
```
先ほどと同じ手順で~/.bashrcを開き、下記のものを書き込む
```
eval "$(pyenv virtualenv-init -)"
```
パスを書き換えた後は `$ source ~/.bashrc` を実行するか、もしくは端末を再起動して設定ファイルをリロード。

## pyenvの使い方
ヘルプの参照
```sh
pyenv --help
```
インストールできるバージョンの確認。
```sh
pyenv install --list
```
インストールしたいものを選んでインストール。以下は2018/03/07現在最新（ベータ除く）
```sh
pyenv install 3.6.4
```

uninstallするときは
```sh
pyenv uninstall 3.6.4
```
(2018/03/13)なんか謎エラーが出ていたのでもう一度インストールし直そうと考えた。
`rm: cannot remove ... Permission denied`
とか言われるのでできていない可能性が。
しかし`python --version`とすると出てこないので一部だけ消せないっぽさ。
とりあえずもう一度`pyenv install 3.6.4`したらエラーは出ず正常に動いた謎。


### バージョンの切り替え
pyenvにどのバージョンをいれてあるかの確認
```sh
pyenv versions
```
現在のpythonのバージョンを確認したいときは
```sh
python --version
```

`pyenv global x.x.x` または、 `pyenv local x.x.x` でバージョンの切り替え。
`global` とすると全体に、 `local` にするとそのカレントディレクトリに反映。
この反映はterminalを終了しても続くので、localでフォルダごとに設定するととても便利らしい。

シェルでの変更は、`shell`。今使用してるシェルでのみ、その環境が反映される。
シェルを閉じた時、後に再度開いた場合やシェルを複数開いた場合はその環境変更は他に影響されることはない。

```sh
pyenv global x.x.x
```
```sh
pyenv local x.x.x
```
```sh
pyenv shell x.x.x
```
`x.x.x`の場所には環境名。

### moduleのインストール
`pip install`で好きなものを入れていく。
`pip freeze`で中に何が入っているか確認できる。

## pyenv-virtualenv

### 新しい環境の作成

```sh
pyenv virtualenv バージョン 環境名
```
で作成可能。
環境削除は以下。
```sh
pyenv uninstall 環境名
```

環境に入る時は、
```sh
pyenv activate 環境名
```
抜けるときは
```sh
pyenv deactivate
```

## 参考
- [pyenv と pyenv-virtualenv で環境構築](https://qiita.com/Kodaira_/items/feadfef9add468e3a85b)
- [PyenvによるPython3.x環境構築(CentOS, Ubuntu)](https://qiita.com/akito1986/items/be5dcd1a502aaf22010b)
- [UbuntuでPythonの開発環境を整える](https://qiita.com/uryyyyyyy/items/268f8dc0d6ec3d7da7e3)
