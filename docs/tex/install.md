# tex

2019/08/02

## 導入

texliveをダウンロードしてくるのが無難らしい。  
以下リンク  

TEXWiki
[https://texwiki.texjp.org/?TeX%20Live](https://texwiki.texjp.org/?TeX%20Live)

から頑張ってインストールする。  
各OSによって違うので割愛。

自分の場合は  
[https://www.tug.org/texlive/acquire-netinstall.html](https://www.tug.org/texlive/acquire-netinstall.html)  
から ` install-tl-windows.exe` をダウンロードした。

実行するとインストーラーが出てくるので、指示にしたがってインストールする。

2時間くらい時間がかかるので注意。


## VSCodeで書く

++ctrl++ + , を押して、`setteing.json` を検索バーに入れると `Edit in settings.json` を押す。  
`settings.json` が開くので、そこの`{}`の中に以下を追記。

```json
    "latex-workshop.latex.tools": [{
        "name": "ptex2pdf (platex)",
        "command": "ptex2pdf",
        "args": [
          "-l",
          "-ot",
          "-kanji=utf8 -synctex=1",
          "%DOC%"
        ]
      },
    ],
    "latex-workshop.latex.recipes": [
      {
        "name": "ptex2pdf (platex) * 1",
        "tools": [
          "ptex2pdf (platex)"
        ]
      },
    ],
    "latex-workshop.synctex.afterBuild.enabled": true,
    "latex-workshop.view.pdf.viewer": "tab"
```

ここまでで設定終わり。

### テスト

どこかのフォルダで`hoge.tex` を作成する。  
何か適当に書いてみる。

```tex
\documentclass{jsarticle}
\begin{document}
数式：

$$
Ax = b
$$

\end{document}
```

