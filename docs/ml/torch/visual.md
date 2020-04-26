# tensorboardによる可視化


```py
from torch.utils.tensorboard import SummaryWriter

# default `log_dir` is "runs" - we'll be more specific here
writer = SummaryWriter('runs/fashion_mnist_experiment_1')
```

この行だけで `runs/fashion_mnist_experiment_1` フォルダが作成される





