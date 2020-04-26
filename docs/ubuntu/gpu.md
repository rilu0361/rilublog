# GPU for tensorflow-gpu

2018/12/18

deep learningをするためにGPU (GeForce 1080ti)を導入したときの備忘録。

## ドライバのインストール

1. aptリポジトリ追加
```sh
sudo add-apt-repository ppa:graphics-drivers/ppa
```

2. 更新
```sh
sudo apt update
```
3. ドライバのインストール
```
sudo apt install nvidia-390
```

*2019/3/29　追記*  
GPUのサポート情報→
[GPU support TensorFlow](https://www.tensorflow.org/install/gpu)

4. 確認
```sh
nvidia-smi
```

## tensorflow-gpu の環境構築

環境構築は ~~脳死で~~ Anacondaを頼ることにした。

pip でのinstall よりもconda でのinstallのほうが、tensorflowのパフォーマンスがよくなるとか。
(8倍以上？)

[Stop Installing Tensorflow using pip for performance sake!](https://towardsdatascience.com/stop-installing-tensorflow-using-pip-for-performance-sake-5854f9d9eb0c?mkt_tok=eyJpIjoiWTJabE5tTXlZbU5oTXpGaSIsInQiOiJOU0dRRmFoRUpGc0VONjBJeVFsZmdtK1cxV2ZHbGxUMEJlaUZnek96UWxRTFR4KzNMREx6V3pya240cUozVitFMWJRKzN2MVBQd2FFQjdLb2tzdEVxUW1UZ0hlazc0WUVsc0NSWnJnWUtWWXJzZXQ1RHlQbVFnN1RjalA1VUlVdCJ9)

また、pip でやるよりも簡単にできそうなのがいいところ。

```sh
conda install tensorflow
```

してから

```sh
conda install tensotflow-gpu
```

するだけらしいのだが、これをすると、cuda9.2が導入されてしまい、tensorflowのサポート対象外になってしまった。(2018/12/18現在)

よってcudnnのバージョンを7.2.1から7.1.2に下げる。

```sh
conda install cudnn=7.1.2
```

を実行する。

その後
```sh
conda install tensorflow
```
```sh
conda install tensorflow-gpu
```

して実行して問題なく、GPUを使用するプログラムは動作した。


## 参考

[nvidia driverのバージョン](https://www.nvidia.co.jp/Download/Find.aspx?lang=jp)

[cudnnのバージョン](https://repo.anaconda.com/pkgs/main/linux-64/)

