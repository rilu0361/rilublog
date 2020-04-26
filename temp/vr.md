# VR 




- - -

Motion Sickness Prediction in Stereoscopic Videos Using 3D Convolutional Neural Networks
Tae Min Lee (Yonsei University), Jong-Chul Yoon (Kangwon National University), In-Kwon Lee (Yonsei University)

TVCG

Abstract: In this paper, we propose a three-dimensional (3D) convolutional neural network (CNN)-based method for predicting the degree of motion sickness induced by a 360° stereoscopic video. We consider the user’s eye movement as a new feature, in addition to the motion velocity and depth features of a video used in previous work. For this purpose, we use saliency, optical flow, and disparity maps of an input video, which represent eye movement, velocity, and depth, respectively, as the input of the 3D CNN. To train our machine-learning model, we extend the dataset established in the previous work using two data augmentation techniques: frame shifting and pixel shifting. Consequently, our model can predict the degree of motion sickness more precisely than the previous method, and the results have a more similar correlation to the distribution of ground-truth sickness.


3D畳込みニューラルネットワークを用いた立体ビデオの乗り物酔い予測
テミン・リー（延世大学）、チョンチュルヨン（江原大学）、インクォンリー（延世大学校）

TVCG

抄録本論文では、360°立体ビデオによって引き起こされる乗り物酔いの程度を予測するための三次元（3D）畳込みニューラルネットワーク（CNN）ベースの方法を提案した。これまでの研究で使用されてきたビデオの動きの速度や奥行きの特徴に加えて、ユーザーの目の動きも新しい特徴と見なしています。この目的のために、本発明者らは、３Ｄ ＣＮＮの入力として、それぞれ眼球運動、速度、および深度を表す入力ビデオの顕著性マップ、オプティカルフローマップ、および視差マップを使用する。私たちの機械学習モデルを訓練するために、私たちは2つのデータ拡張技術を使って前の研究で確立されたデータセットを拡張します：フレームシフトとピクセルシフト。その結果、我々のモデルは以前の方法よりも正確に乗り物酔いの程度を予測することができます。

- - -


Real-time panoramic depth maps from omni-directional stereo images for 6 DoF videos in virtual reality
Po Kong Lai (University of Ottawa), Shuang Xie (University of Ottawa), Jochen Lang (University of Ottawa), Robert Laganière (University of Ottawa)

Conference

Abstract: In this paper we present an approach for 6 DoF panoramic videos from omni-directional stereo (ODS) images using convolutional neural networks (CNNs). More specifically, we use CNNs to generate panoramic depth maps from ODS images in real-time. These depth maps would then allow for re-projection of panoramic images thus providing 6 DoF to a viewer in virtual reality (VR). As the boundaries of a panoramic image must touch in order to envelope a viewer, we introduce a border weighted loss function as well as new error metrics specifically tailored for panoramic images. We show experimentally that training with our border weighted loss function improves performance by benchmarking a baseline skip-connected encoder-decoder style network as well as other state-of-the-art methods in depth map esimation from mono and stereo images. Finally, a practical application for VR using real world data is also demonstrated.

仮想現実における6つのDoFビデオのための全方向ステレオ画像からのリアルタイムパノラマ深度マップ
Po Kong Lai（オタワ大学）、Shuang Xie（オタワ大学）、Jochen Lang（オタワ大学）、RobertLaganière（オタワ大学）

会議

要約：本論文では、畳み込みニューラルネットワーク（CNN）を用いた全方向ステレオ（ODS）画像からの6つのDoFパノラマビデオのためのアプローチを提示する。具体的には、CNNを使用してODS画像からリアルタイムでパノラマ深度マップを生成します。これらの深度マップは、パノラマ画像の再投影を可能にし、したがって仮想現実（ＶＲ）において６ＤｏＦを視聴者に提供する。パノラマ画像の境界は視聴者を包み込むために触れなければならないので、境界重み付き損失関数と、パノラマ画像用に特別に調整された新しい誤差測定基準とを導入する。我々は実験的に我々の境界加重損失関数を用いたトレーニングがモノラルおよびステレオ画像からの深さマップ推定におけるベースラインスキップ接続エンコーダ - デコーダスタイルネットワークならびに他の最先端の方法をベンチマークすることによって性能を改善することを示す。最後に、


- - -

Cybersickness Analysis with EEG using Deep Learning Algorithms
Dae kyo Jeong (Data Visualization Lab, Sejong University), Sangbong Yoo (Sejong University), Yun Jang (Sejong University)

Conference

Abstract: Cybersickness is a symptom of dizziness that occurs while experiencing Virtual Reality (VR) technology and it is presumed to occur mainly by crosstalk between the sensory and cognitive systems. However, since the sensory and cognitive systems cannot be measured objectively, it is difficult to measure cybersickness. Therefore, methodologies for measuring cybersickness have been studied in various ways. Traditional studies have collected answers to questionnaires or analyzed EEG data using machine learning algorithms. However, the system relying on the questionnaires lacks objectivity, and it is difficult to obtain highly accurate measurements with the machine learning algorithms in the previous work. In this work, we apply and compare Deep Neural Network (DNN) and Convolutional Neural Network (CNN) deep learning algorithms for objective cybersickness measurement from EEG data. We also propose a data preprocessing for learning and signal quality weights allowing us to achieve high performance when learning EEG data with the deep learning algorithms. Besides, we analyze video characteristics where cybersickness occurs by examining the video segments causing cybersickness in the experiments. We find common patterns that causes cybersickness.

ディープラーニングアルゴリズムを用いたEEGによるサイバー酔い解析
大興チョン（世宗大学データビジュアライゼーションラボ）、Sangbong Yoo（世宗大学）、Yun Jang（世宗大学）

会議

要約：サイバーシックネスは、バーチャルリアリティ（VR）技術を経験している間に起こるめまいの症状であり、主に感覚系と認知系との間のクロストークによって起こると推定されています。しかしながら、感覚および認知システムは客観的に測定することができないので、サイバーシックネスを測定することは困難である。したがって、サイバーシックネスを測定するための方法論は様々な方法で研究されてきた。伝統的な研究では、アンケートへの回答を収集したり、機械学習アルゴリズムを使用してEEGデータを分析したりしてきました。しかしながら、アンケートに頼るシステムは客観性に欠け、以前の研究における機械学習アルゴリズムを用いて非常に正確な測定値を得ることは困難である。この仕事で、脳波データからの客観的サイバー酔い測定のためにディープニューラルネットワーク（DNN）と畳み込みニューラルネットワーク（CNN）ディープラーニングアルゴリズムを適用して比較した。また、学習のためのデータ前処理と信号品質の重み付けを提案し、ディープラーニングアルゴリズムでEEGデータを学習する際に高いパフォーマンスを達成できるようにします。さらに、実験でサイバーシックネスを引き起こすビデオセグメントを調べることによって、サイバーシックネスが発生するビデオ特性を分析します。サイバー酔いを引き起こす一般的なパターンを見つけます。実験でサイバーシックネスを引き起こすビデオセグメントを調べることにより、サイバーシックネスが発生するビデオ特性を分析します。サイバー酔いを引き起こす一般的なパターンを見つけます。実験でサイバーシックネスを引き起こすビデオセグメントを調べることにより、サイバーシックネスが発生するビデオ特性を分析します。サイバー酔いを引き起こす一般的なパターンを見つけます。

- - -

Improving Walking in Place Methods with Individualization and Deep Networks
Sara Hanson (University of Southern California), Richard Paris (Vanderbilt University), Haley Alexander Adams (Vanderbilt University), Bobby Bodenheimer (Vanderbilt University)

Conference

Abstract: Walking in place is a standard method for moving through large virtual environments when the physical space or tracking range is limited. It has become increasingly significant with the advent of mobile virtual reality where external tracking may not be present. In this paper we revisit walking in place algorithms to improve some of their typical difficulties, such as starting and stopping for individual users and controlling the speed with which users travel through the environment. Starting from a hand-tuned threshold based algorithm we provide a fast method for individualizing the walking in place algorithm based on standard biomechanics. In addition, we introduce a new walking in place model based on a convolutional neural network trained to differentiate walking and standing. In two experiments we assess these methods on two mobile virtual reality platforms based on controllability, scale, and presence. Our results suggest that an adequately trained convolutional neural network can be an effective way of implementing walking in place.


個別化とディープネットワークによるインプレース歩行方法の改善
サラ・ハンソン（南カリフォルニア大学）、リチャード・パリ（ヴァンダービルト大学）、ヘイリー・アレクサンダー・アダムズ（ヴァンダービルト大学）、ボビー・ボーデンハイマー（ヴァンダービルト大学）

会議

要約：物理的な空間や追跡範囲が限られている場合は、定位置に歩くことが大きな仮想環境を移動するための標準的な方法です。外部追跡が存在しない可能性があるモバイル仮想現実の出現と共に、それはますます重要になっています。このホワイトペーパーでは、個々のユーザーの開始と停止、およびユーザーが環境内を移動する速度を制御するなど、典型的な問題のいくつかを改善するために、ウォークインプレースアルゴリズムを再検討します。手動で調整された閾値ベースのアルゴリズムから始めて、我々は標準的なバイオメカニクスに基づいてウォーキングインプレースアルゴリズムを個別化するための速い方法を提供する。さらに、歩行と立位を区別するように訓練された畳み込みニューラルネットワークに基づいて、新しいウォーキングインプレースモデルを紹介します。2つの実験で、制御性、規模、およびプレゼンスに基づいて、2つのモバイルバーチャルリアリティプラットフォームでこれらの方法を評価します。我々の結果は、適切に訓練された畳み込みニューラルネットワークが所定の位置でウォーキングを実行する効果的な方法であり得ることを示唆している。



- - -

Remapped Physical-Virtual Interfaces with Bimanual Haptic Retargeting
Brandon J Matthews (University of South Australia), Bruce H Thomas (University of South Australia), G Stewart Von Itzstein (University of South Australia), Ross Smith (University of South Australia)

Conference

Abstract: This paper proposes a novel interface for virtual reality in which physical interface components are mapped to multiple virtual coun- terparts using haptic retargeting illusions. This gives virtual reality interfaces the ability to have correct haptic sensations for many vir- tual buttons although in the physical space there is only one. This is a generic system that can be applied to areas including design, inter- action tasks, product prototype development and interactive games in virtual reality. The system presented extends existing retargeting algorithms to support bi-manual interactions. A new warp algorithm, called interface warp, was developed to support remapped virtual reality user interfaces. Through an experimental user study, we explore the effects of bimanual retargeting and the interface warp technique on task response time, errors, presence, perceived manipu- lation compared to unimanual (single handed) retargeting and other existing warp techniques. The experiment was conducted to explore the operating parameters of the system which demonstrated faster task response time and less errors for the interface warp technique and shows no significant impact of bimanual interactions.

自動VR画像直立調整のためのディープラーニングベースのアプローチ
Raehyuk Jung（KAIST）、Aiden Seung Joon Lee（ブラウン大学）、Amirsaman Ashtari（KAIST）、Jean-Charles Bazin（KAIST）

会議

要約：最近の球面VRカメラは360°の視野で低コストでVR画像をキャプチャできるため、実世界のVRコンテンツの取得を大幅に民主化し、簡素化しました。しかしながら、実際には、カメラの向きがまっすぐでない場合、取得されたＶＲ画像は垂直に整列されず、したがって、ＶＲヘッドセットに表示されるときに傾斜して見え、これはＶＲ体験の質を低下させる。この問題を克服するために、VR画像の向きを自動的に推定してその直立バージョンを返すことができるディープラーニングベースのアプローチを提示します。既存の方法とは対照的に、我々のアプローチは画像中に線、消失点または地平線の存在を必要とせず、したがって広範囲のシーンに適用することができる。定量的および定性的評価による実際のデータセットの実験

- - -


A Deep Learning-based Framework for Intersectional Traffic Simulation and Editing
Huikun Bi, Tianlu Mao, Zhaoqi Wang, Zhigang Deng

TVCG-Invited

Abstract: Most of existing traffic simulation methods have been focused on simulating vehicles on freeways or city-scale urban networks. However, relatively little research has been done to simulate intersectional traffic to date despite its obvious importance in real-world traffic phenomena. In this paper we propose a novel deep learning-based framework to simulate and edit intersectional traffic. Specifically, based on an in-house collected intersectional traffic dataset, we employ the combination of convolution network (CNN) and recurrent network (RNN) to learn the patterns of vehicle trajectories in intersectional traffic. Besides simulating novel intersectional traffic, our method can be used to edit existing intersectional traffic. Through many experiments as well as comparison user studies, we demonstrate that the results by our method are visually indistinguishable from ground truth and perform better than other methods.


交差点交通シミュレーションと編集のための深層学習ベースのフレームワーク
Huikun Bi、Tianlu Mao、Zhaoqi Wang、Zhigang Deng

TVCG招待

要約：既存の交通シミュレーション手法のほとんどは、高速道路や都市規模の都市ネットワークでの車両のシミュレーションに焦点が当てられています。しかしながら、現実世界の交通現象において明らかに重要であるにもかかわらず、今日まで交差点交通をシミュレートするための研究は比較的少ない。本論文では、交差点交通をシミュレートし編集するための新しいディープラーニングベースのフレームワークを提案した。具体的には、社内で収集した交差点交通データセットに基づいて、交差点交通における車両軌跡のパターンを学習するために畳み込みネットワーク（CNN）と回帰ネットワーク（RNN）の組み合わせを採用しています。新規の交差点交通をシミュレートすることに加えて、我々の方法は既存の交差点交通を編集するために使用することができる。多くの実験や比較ユーザースタディを通して、