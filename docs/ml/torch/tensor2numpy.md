# tensor<-->Numpy

## テンソルからNumpy配列

```py
>>> x = torch.randn(2,3)
tensor([[-0.2520,  1.5178, -0.1606],
        [-0.1414,  0.7792,  1.1737]])
```

```py
>>> a = x.numpy()
array([[-0.2519832 ,  1.5177612 , -0.16061842],
       [-0.14137174,  0.77923495,  1.1737281 ]], dtype=float32)
```

!!! WARNING
    `x` を次のように変更すると`a` も変わります。
    ```py
    >>> x.add_(1) # 1を足す
    tensor([[0.7480, 2.5178, 0.8394],
            [0.8586, 1.7792, 2.1737]])
    >>> a
    array([[0.74801683, 2.5177612 , 0.8393816 ],
           [0.8586283 , 1.7792349 , 2.173728  ]], dtype=float32)
    ```

## Numpy配列からテンソル

```py
import numpy as np
import torch
a = np.ones(3)
x = torch.from_numpy(a)
```

- 結果
```sh
>>> a
array([1., 1., 1.])

>>> x
tensor([1., 1., 1.], dtype=torch.float64)
```

!!! WARNING
    `a` を以下のように変更すると`x` も変わります。
    ```py
    >>> np.add(a, 1, out=a) # 1を足す
    array([2., 2., 2.])
    >>> x
    tensor([2., 2., 2.], dtype=torch.float64)
    ```
    次の場合は変わらない.
    ```py
    >>> a = a + 1 # 1を足す
    array([2., 2., 2.])

    >>> x
    tensor([1., 1., 1.], dtype=torch.float64)
    ```

- - -
おわりー
(2019/10/22)