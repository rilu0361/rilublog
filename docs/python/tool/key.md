# key入力

## 概要
キーボードの入力をpythonに任せる。

pyautoGUIを用いる。

```sh
pip install pyautogui
```
でインストール可能。

## 内容

import する。

```py
import pyautogui as pgui
```

キーを押す。(ctrl)
```py
pgui.keyDown("ctrlleft")
```

キーを離す。(z)
```py
pgui.keyUp("z")
```

## 例
++ctrl+z++

```py
import pyautogui as pgui

pgui.keyDown("ctrlleft")
pgui.keyDown("z")
pgui.keyUp("z")
pgui.keyUp("ctrlleft")
```


## 備考
マウス操作とかもできるらしい。