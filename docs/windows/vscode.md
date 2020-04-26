# VScodeの設定(Windows編)

## markdownを使う
拡張機能として
「markdown preview Enhanced」をインストールする。

## pythonを使う
「Python」をインストールする。

## iconをいい感じにする
「vscode-icons」をインストールする。


## VScodeをslack風にする
「Slack Theme」をインストールする。

## Terminalを開いたときにWSLを使用する

「Ctrl」+「,」 を押して、 `search setteing` から `setting.json` を探す。

で `setting.json` に以下を追加

```sh
"terminal.integrated.shell.windows": "C:/Windows/System32/wsl.exe",
```

