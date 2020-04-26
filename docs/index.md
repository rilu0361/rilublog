# 備忘録と雑記

## このサイトについて
個人的なプログラムのメモや、勉強のメモなどを書き残した自分用の備忘録的なものになる予定です。主にPython関連がメインになるかとは思います。

間違いには気をつけておりますが、内容を保証できるものではありませんのでご注意ください。  
あくまで備忘録程度であることを理解いただいたうえでお読みください。  
また、予告のない編集により内容が改変されることもご容赦ください。


## 更新履歴
(2019/10/05 : ここから大幅に改変します！！たぶん！！)

2019/10/23 : pytorchモデル構築編追加。  
2019/10/22 : pytorch導入編・基本操作追加。
2019/10/15 : 色々更新したよー(継続)  
2019/10/14 : 色々更新したよー

### ひとこと 
お腹痛いです。
(2019/10/23)

- - -
## 目次

### Python 一般

[Anacondaコマンド集](./python/anaconda_cmd.md)：よく使うAnacondaのコマンド集  

??? 文法基礎
    [繰り返し](./python/syntax/for.md)：for,while  
    [条件分岐](./python/syntax/if.md)：if True False  
    [リスト](python/syntax/list.md)：追加・結合・検索・ソート  
    [タプル](python/syntax/tuple.md)：  
    [集合](python/syntax/set.md)：和,差,共通集合  
    [辞書](python/syntax/dict.md)：結合・get  
    [内包表記](python/syntax/comprehension.md)：後置if,三項演算子も   
    [型注釈](python/syntax/typehint.md)：型ヒント  
    [fizzbuzz](python/syntax/fizzbuzz.md)：fizzbuzz例

??? numpy
    [乱数生成](python/numpy/random.md)：乱数生成とその設定  
    [ランダムに選ぶ](python/numpy/choice.md)：リストからランダムに抽出  
    [配列の要素を見る](python/numpy/element.md)：要素のチェック

??? pandas
    [表形式データの保存](python/pandas/save.md)：excelとcsvへの保存  
    [csvデータの読込](python/pandas/csv_load.md)：CSVデータの読込  
    [excelデータの読込](python/pandas/excel_load.md)：シートの扱い  
    [重複の削除](python/pandas/remove.md)：duplicated()  
    [DetaFrameの生成](python/pandas/df_create.md)：DataFrameの生成  
    [DataFrameの参照](python/pandas/df_look.md)：データの参照  
    [DataFrameの操作](python/pandas/df_ope)：追加・削除・合成・結合・転置  
    [DataFrameの全表示](python/pandas/df_show.md)：表示の省略を防ぐ  
    [Seriesの生成](python/pandas/sr_create.md)：1次元配列

??? matplotlib
    [matplotlibの基本](python/matplotlib/plot.md)  
    [複数の図をまとめて表示](python/matplotlib/subplot.md)：subplot()   
    [ヒストグラムを描く](python/matplotlib/hist.md)：hist()   
    [散布図を描く](python/matplotlib/scatter.md)：scatter()  

??? scipy
    [確率密度関数](python/scipy/prob_density.md)

??? ファイル関連
    [ファイル一覧取得](python/file/dir_show.md)：2通り  
    [ファイル読み込み](python/file/file_r.md)：テキストファイルの読込  
    [ファイル書き込み](python/file/file_w.md)：テキストファイルの書込  
    [ファイル削除](python/file/file_d.md)：削除  
    [ディレクトリ作成](python/file/dir_create.md)：フォルダの作成  
    [ディレクトリ削除](python/file/dir_d.md)：フォルダの削除  

??? 便利ツール
    [pythonのexe化](python/tool/exe.md)：pythonをexeにまとめる  
    [プログレスバーの表示](python/tool/progress.md)：tqdm  
    [コマンドライン引数](python/tool/commandLine_option.md)  
    [現在時間の取得](python/tool/time.md):現在時刻をファイル名に  
    [ログの表示](python/tool/log.md)：所説あり?  
    [キーボード操作](python/tool/key.md)：自動キー入力  
    [tkinter](python/tool/tkinter.md)：簡単なGUI作成  

??? その他
    [統計基礎](python/other/statistic.md)：平均分散中央値など

??? 環境構築
    [Anacondaによる環境構築](python/env/anaconda_install.md)  
    [pyenvでの環境構築](python/env/pyenv.md)

### 自然言語処理

[データサンプル](nlp/sample.md)：動作確認用のちょっとしたデータサンプル

??? 前処理  
    [前処理の一連の流れ](nlp/data/prepare.md)：前処理全般  
    [データの読み込みと保存](nlp/data/textdata.md)：テキストデータの扱い  
    [ストップワード除去](nlp/data/stopword.md)  
    [mecabの導入](nlp/data/mecab.md)：環境構築  
    [mecabユーザー辞書の追加](nlp/data/mecab_add_userdic.md)：カスタム  
    [mecabを使用する](nlp/data/mecab_usage.md)：単語分割  
    [janome](nlp/data/janome.md)：単語分割  
    [stanfordnlp](nlp/data/stanford.md)：単語分割  
    [単語のパース](nlp/data/parse.md)  
    [半角全角変換](nlp/data/zenhan.md)  
    <!-- 正規表現: nlp/data/regex.md -->

??? 統計処理
    [TF-IDF](nlp/sta/tfidf.md)：TF-IDF  
    [単語のカウント](nlp/sta/count.md)：カウント   
    [共起行列の作成](nlp/sta/co_matrix.md)：共起
    [ワードクラウド](nlp/sta/wordcloud.md)：ワードクラウドによる可視化

??? 機械学習
    [word2vec](nlp/ml/word2vec.md)：単語ベクトルの生成  
    [k-menas](nlp/ml/kmeans.md):非階層型クラスタリング  
    [次元削減](nlp/ml/dimention.md)：PCAなど

??? 評価
    [コサイン類似度](nlp/eva/cos.md)：文書間の類似度を測る


### 画像

??? データの読み込みと加工
    [画像の読み込み](image/img_load.md)：with keras   
    [画像のデータ拡張](image/img_aug.md)：工事中  
    [フィルタ](image/filter.md)  
    [特徴量](image/feature.md)  

??? 画像処理
    [テンプレートマッチング](image/template_matching.md)

### 音声

??? 基礎
    [基本的な流れ](audio/general.md)  
    [特徴量](audio/feature.md)

### 異常検知

??? 基礎
    [異常検知基礎](anormaly/base.md)


### 機械学習フレームワーク

??? pytorch
    [pytorch導入編](ml/torch/intro.md)：インストールと動作確認   
    [データ取得と加工](ml/torch/data.md)：dataloder  
    [モデル作成](ml/torch/model.md)：modelクラスの作成と動作確認  
    [tensorboard可視化](ml/torch/visual.md)：tensorboardによる可視化  
    [テンソルサイズ操作](ml/torch/tensor_size.md)：sizeとreshape(view)  
    [テンソル計算基礎](ml/torch/tensor_culc.md)：加算  
    [tensor<-->Numpy](ml/torch/tensor2numpy.md)：相互変換方法  
    [テンソル生成](ml/torch/tensor_c.md)：乱数,0,1,既存テンソルと同サイズ  
    [テンソル参照](ml/torch/tensor_o.md)：numpyと同様  

??? keras
    工事中...

??? tensorflow
    工事中...

??? scikit-learn
    工事中...

### アプリケーション

??? 言語処理
    工事中...  
    [pdfからテキストを抽出する](create/pdf2md.md)

??? webアプリ
    工事中...


### 数学

??? 公式など
    [確率メモ](basis/memo_prob.md)  
    [微積分メモ](basis/memo_culculus.md)  
    [確率分布メモ](basis/memo_distribution.md)  

??? 推定
    [最小値を求める基礎](basis/minimize.md)  
    [最尤推定](basis/likelihood.md)  
    [MAP推定](basis/map.md)  
    [ベイズ推定](basis/bayesian.md)

### Ubuntu

??? コマンド
    [シェルコマンド集](./ubuntu/cmd.md)

??? 設定関連
    [2TB以上のHDDのマウント](./ubuntu/hdd_mnt.md)  
    [ログインループの対処](./ubuntu/login_loop.md)  
    [ファイル名の英語化](./ubuntu/setting.md)

### Windows

??? ツール
    [VScode設定おまけ](./windows/vscode.md)  
    [ショートカットキー一覧](./windows/shortcut.md)

??? WindowsSubsystemforLinux
    [WSL導入](./windows/wsl.md)  
    [WSL+Anaconda](./windows/wsl_python.md)  
    [WSL+matplotlib](./windows/wsl_matplotlib.md)  
    [xming文字化け対処](./windows/xming_char.md)


### 文章を書く

??? Markdown
    [markdown基本](markdown/mkd.md)  
    [markdown数式](markdown/math.md)  
    [markdown数式 記号](markdown/math_symbol.md)  
    [markdown拡張](markdown/mkdocs_md.md)  
    [markdown例](markdown/mkd_ex.md)  
    [mkdocsによるwebページの公開](markdown/mkdocs.md)

??? Tex
    [Texのインストール(Windows)](tex/install.md)

??? RestructuredText
    [Rest基本構文](rest/fund.md)  
    [注意 強調](rest/admotions.md)  
    [リンク 脚注](rest/link.md)  
    [数式の挿入](rest/math.md)  
    [コード 表 画像 サイドバー](rest/module.md)  
    [その他](rest/other.md)  
    [sphinxによるwebページの公開](rest/sphinx.md)

### その他

??? その他
    [Git](other/git.md)  
    [RPA概要](other/rpa.md)

### 雑記・ひとこと

??? ひとことアーカイブ
    [2019年10月](blog/201910.md)：10月のひとこと  
    [2019年07月](blog/201907.md)：07月のひとこと  
    [2019年06月](blog/201906.md)：06月のひとこと  
    [2019年05月](blog/201905.md)：05月のひとこと  
    [2019年04月](blog/201904.md)：04月のひとこと

### 免責事項

[免責事項](disclaimer.md)


