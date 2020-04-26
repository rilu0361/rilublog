# 特徴量

## 明度と輝度

$$
明度 = \frac{\max(\text{RGB}) + \min(\text{RGB})}{2} 
$$


$$
輝度 = 0.3R + 0.6G + 0.1B
$$

## 2値化

しきい値を決めて、白か黒の2値にしてしまう。

- グローバルしきい値法
大津の二値化
- ローカルしきい値法

## Haar-like特徴

$$
(黒領域の輝度値の総和) - (白領域の輝度値の総和) 
$$

Haar-like特徴量をAda Boostと組み合わせて識別を行う。

#### Ada Boost
一つでは精度の低い弱識別器を多数用いることで強い識別器を作る手法。


## EOH(Edge of Orientation Histogram)



## HOG (Histograms of Orientation Gradient)


## SIFT (Scale Invariant Feature Transform)
照明変化、拡大縮小、回転などの変化に頑健。

## HLAC (High-order Local Auto Correlation)


## CHLAC (Cubic High-order Local Auto Correlation)

