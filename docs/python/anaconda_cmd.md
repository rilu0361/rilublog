# Anacondaコマンド集

2019/3/29

`myenv` は任意の環境名に置き換え.

### 仮想環境の作成
```sh
conda create -n myenv
```

pythonのバージョンを指定したい場合は
```sh
conda create -n myenv python=3.6.8
```

### 仮想環境のアクティブ化
```sh
conda activate myenv
```
もしかしたら
```sh
source activate myenv
```
### 仮想環境の非アクティブ化
```sh
conda deactivate
```

### 仮想環境の削除
```
conda remove -n myenv -a
```

### 仮想環境一覧の確認
```sh
conda info -e
```

### パッケージのインストール
```sh
conda install numpy
```

パッケージのバージョンを指定してインストールしたい場合は
```sh
conda install numpy=1.15.1
```

condaでのinstallができない場合は `pip` を使うとできるかもしれない。
ただし、`conda` と `pip` が競合して良くないという話も聞くのでこのあたりは要検証。

```sh
pip install numpy
```
### パッケージのアンインストール
```sh
conda uninstall numpy
```
### インストールしたパッケージ一覧の表示
```sh
conda list
```
### condaのアップデート
```sh
conda update conda 
```
### パッケージのアップデート
```sh
conda update numpy
```

### インストールしたパッケージ一覧の書き出し
他の人と環境を共有したい場合に。
yamlファイルに書き出しを行える。

```sh
conda env export > myenv.yml
```

### パッケージの検索
```sh
conda search numpy
```
### ymlから同一環境の作成

他の人と環境を共有したい場合に。
パッケージの一覧を書き出したyamlファイルがあることが前提。

```sh
conda env create -f myenv.yml
```

yamlファイルの手動作成

`name` に環境名
`dependencies` にパッケージ名を記載。バージョンも必要な場合は書く。

```yml
name: myenv
channels:
- defaults
dependencies:
- jupyter
- numpy
- pandas
- tensorflow=1.12
- tensorflow-gpu
- keras
- python==3.6.8
- cudnn=7.1.2
```

### 環境のクローンの作成

`myclone` は適宜置き換え。

```sh
conda create -n myclone --clone myenv
```

### 参考

[https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually)