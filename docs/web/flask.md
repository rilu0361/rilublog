# flaskを使ったwebアプリ導入編

## 概要
Pythonで簡単なwebアプリを作りたい。  
フレームワークはいろいろあるが、今回はflaskで行う。  
(Djangoなどもあるが、今回は小規模なのでそこまで必要なさそうという考え)


## 導入
```sh
conda install flask
```

以下のようなフォルダ構成を用意する。  

```sh
$ tree
.
├── app.py
├── static
│   ├── css
│   └── js
└── templates
    └── index.html

4 directories, 6 files
```


### bootstrapを使用する

```sh
$ tree
.
├── app.py
├── static
│   ├── css
│   │   └── bootstrap.min.css
│   └── js
│       ├── bootstrap.min.js
│       ├── jquery-3.4.1.min.js
│       └── popper.min.js
└── templates
    └── index.html

4 directories, 6 files
```


- - -
おわり～
(2019/10/24)