
## 微分

$$
\frac{\partial}{\partial \boldsymbol{x}} f(\boldsymbol{x})
= (\frac{\partial}{\partial x_1} f(\boldsymbol{x})
, \frac{\partial}{\partial x_2} f(\boldsymbol{x})
, ...
, \frac{\partial}{\partial x_D} f(\boldsymbol{x}))^T
$$


$$
\frac{\partial}{\partial \boldsymbol{x}} (\boldsymbol{x}^T \boldsymbol{a})
= \boldsymbol{a} 
\tag{1}
$$

??? 導出
    $$
    \begin{align}
    \frac{\partial}{\partial \boldsymbol{x}} (\boldsymbol{x}^T \boldsymbol{a})
    &= \biggr(\frac{\partial}{\partial x_1}  (\boldsymbol{x}^T \boldsymbol{a})
    , \frac{\partial}{\partial x_2}  (\boldsymbol{x}^T \boldsymbol{a})
    , ...
    , \frac{\partial}{\partial x_D}  (\boldsymbol{x}^T \boldsymbol{a}) \biggl)^T  \\
    \tag{1}
    &= \biggr(\frac{\partial}{\partial x_1}  (\sum^D_{d=1}x_d a_d)
    , \frac{\partial}{\partial x_2}  (\sum^D_{d=1}x_d a_d)
    , ...
    , \frac{\partial}{\partial x_D} (\sum^D_{d=1}x_d a_d) \biggl)^T \\
    &= (a_1,a_2,...,a_D)^T \\
    &= \boldsymbol{a}
    \end{align}
    $$

$$
\frac{\partial}{\partial \boldsymbol{x}} (\boldsymbol{x}^T \boldsymbol{x})
= 2 \boldsymbol{x} 
\tag{2}
$$

??? 導出
    $$
    \begin{align}
    \frac{\partial}{\partial \boldsymbol{x}} (\boldsymbol{x}^T \boldsymbol{x})
    &= \biggr(\frac{\partial}{\partial x_1}  (\boldsymbol{x}^T \boldsymbol{x})
    , \frac{\partial}{\partial x_2}  (\boldsymbol{x}^T \boldsymbol{x})
    , ...
    , \frac{\partial}{\partial x_D}  (\boldsymbol{x}^T \boldsymbol{x}) \biggl)^T   \\
    \tag{2}
    &= \biggr(\frac{\partial}{\partial x_1}  (\sum^D_{d=1}x_d^2)
    , \frac{\partial}{\partial x_2}  (\sum^D_{d=1}x_d^2)
    , ...
    , \frac{\partial}{\partial x_D} (\sum^D_{d=1}x_d^2) \biggl)^T \\
    &= (2x_1,2x_2,...,2x_D)^T \\
    &= 2\boldsymbol{x}
    \end{align}
    $$

    $$
    （\boldsymbol{x}^T \boldsymbol{x} = |x|^2
    = x_1^2 + x_2^2 + ... + x_D^2）
    $$


$$
\frac{\partial}{\partial \boldsymbol{x}} (\boldsymbol{x}^T \boldsymbol{A} \boldsymbol{x})
= 2\boldsymbol{A}\boldsymbol{x} 
\tag{3}
$$

??? 導出
    $$
    \boldsymbol{x}^T \boldsymbol{A} \boldsymbol{x} 
    = \sum^D_{i=1} \sum^D_{j=1} x_iA_{ij} x_j
    $$
    
    に注意して、

    $$
    \begin{align}
    \frac{\partial}{\partial \boldsymbol{x}} (\boldsymbol{x}^T \boldsymbol{A} \boldsymbol{x})
    &= \biggr(\frac{\partial}{\partial x_1}  (\sum^D_{i=1} \sum^D_{j=1} x_iA_{ij} x_j)
    , \frac{\partial}{\partial x_2}  (\sum^D_{i=1} \sum^D_{j=1} x_iA_{ij} x_j)
    , ...
    , \frac{\partial}{\partial x_D}  (\sum^D_{i=1} \sum^D_{j=1} x_iA_{ij} x_j) \biggl)^T   \\
    \tag{3}
    &= \biggr(\frac{\partial}{\partial x_1}  (\sum^D_{d=1}A_{1j}x_j)
    , \frac{\partial}{\partial x_2}  (\sum^D_{d=1}A_{2j}x_j)
    , ...
    , \frac{\partial}{\partial x_D} (\sum^D_{d=1}A_{Dj}x_j) \biggl)^T \\
    &= 2(A_1\boldsymbol{x},A_2\boldsymbol{x},...,A_D \boldsymbol{x})^T \\
    &= 2\boldsymbol{A}\boldsymbol{x}
    \end{align}
    $$