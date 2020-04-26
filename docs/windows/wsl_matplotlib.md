# WSLでmatplotlibが使えない問題への対処

## 参考
[[WSL] WindowsのLinuxでmatplotlibを使おうとしたらエラーになった話](http://k28h.blogspot.com/2018/04/wsl-windowslinuxmatplotlib.html)

xmingのダウンロードの際に見た参考サイト
[https://mag.osdn.jp/09/10/14/0753240](https://mag.osdn.jp/09/10/14/0753240)

ここからxmingのダウンロード可能
[https://sourceforge.net/projects/xming/](https://sourceforge.net/projects/xming/)

## 手順
基本参考サイトの通りに。

色々やる前に
`sudo apt update` をしておく。

サイトには `apt-get` と書いてあるが、`apt` でOK。

Google "xming" (x11 server) をダウンロードしてインストール、実行。  
[https://sourceforge.net/projects/xming/](https://sourceforge.net/projects/xming/)

端末で以下を実行
```sh
sudo apt install x11-apps
```

.bashrcに以下を追加。vimで編集した。
```
export DISPLAY=localhost:0.0
```

端末で以下を実行
```sh
sudo apt install gnome-calculator
```

pyenvを利用している場合、各環境の `site-package` 内にある `matplotlibrc` を開いてbackendの設定を以下のように書き換え。  
例）`~/.pyenv/versions/my_env/lib/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc`

```sh
# backend     : Qt5Agg
backend     : TkAgg
```
最初からTkAggだった場合は何もいじらずに変更せず終了。

完了。
