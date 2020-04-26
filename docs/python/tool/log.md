# logの表示

## 概要
logを表示したい。  
なんか所説あるらしいので調査推奨。

## プログラム

```py
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
```
