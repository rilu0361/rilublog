# WSL上でAnacondaを使う

## Anacondaのダウンロード

[https://www.anaconda.com/](https://www.anaconda.com/)
から、Linux版のをダウンロードしてくる。

WSLを開いて

```sh
bash Anaconda3-2019.03-Linux-x86_64.sh(ダウンロードしたファイル名)
```

## PATHを通す

`.bashrc` を開く(vimとかで)

```sh
vim .bashrc
```

以下の文を付け足す
```sh
# my setting
export PATH=/home/ユーザー名/anaconda3/bin:$PATH
```

## 確認

```sh
conda info -e
```

などをしてみて、できればOK

## 問題

```sh
conda activate myenv
```

ができなかった。以下エラー。

```sh
CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run
```

## 対処?

```sh
source activate myenv
```
ならできた。

## 対処 追記
condaのバージョンが新しくなってからは `source activate` ではなく、`conda activate` が推奨されているらしい。

`conda activate` をすると、

```
CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.
```
と言われたとき、

よくわからないが `conda init` した結果、

`.bashrc` に以下が追加されていた。

```
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/name/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/name/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/name/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/name/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup

# <<< conda initialize <<<
```

ここにさらに以下の文を追加する。

```
conda activate base
```

これで解決した。