# テンプレートマッチング

入力画像($I$)とテンプレート画像($T$)の相違を調べる。

## SSD(Sum of Squared Difference)

画素ごとの輝度値の差の二乗。

$$
R_{SSD} = \sum^{N-1}_{j=0} \sum^{M-1}_{i=0} \{I(i,j) - T(i,j) \}^2
$$

## SAD(Sum of Absolute Difference)

画素ごとの輝度値の差の絶対値。

$$
R_{SAD} = \sum^{N-1}_{j=0} \sum^{M-1}_{i=0} |I(i,j) - T(i,j) |
$$

## NCC(Normalized Cross-Correlation)

画像同士の相関をとる。

$$
R_{NCC} = \frac{ \sum^{N-1}_{j=0} \sum^{M-1}_{i=0} I(i,j) T(i,j) }{\sqrt{\sum^{N-1}_{j=0} \sum^{M-1}_{i=0} I(i,j)^2 ・ \sum^{N-1}_{j=0} \sum^{M-1}_{i=0} T(i,j)^2 }}
$$


## ZNCC(Zero-mean Normalized Cross-Correlation)

画像同士の相関をとる。  
明るさに変動があっても安定して相関がとれる。  
入力画像、テンプレート画像それぞれの画像全体の輝度値の平均をとる。($\bar I , \bar T$)

$$
R_{ZNCC} = \frac{ \sum^{N-1}_{j=0} \sum^{M-1}_{i=0} \{I(i,j)-\bar I \} \{T(i,j) - \bar T\} }{\sqrt{\sum^{N-1}_{j=0} \sum^{M-1}_{i=0} \{ I(i,j)-\bar I \}^2 ・ \sum^{N-1}_{j=0} \sum^{M-1}_{i=0} \{T(i,j) - \bar T\}^2 }}
$$



