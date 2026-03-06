# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 02:42:49 2026

@author: yoshikazu.nojiri
"""

# コピペしたら練習にならないので、直打ちすること！

%matplotlib inline

############################
# 画像を読み込んで表示
############################
"""
import cv2        # 画像処理ライブラリ OpenCV
import matplotlib.pyplot as plt

# imread で、静止画 bmp,jpg,png 読める
img = cv2.imread("test.bmp")

# imshow で、画像表示の準備、 interpolationは補完処理の有無
plt.imshow(img, interpolation="None")
plt.show()
"""
############################
# 画像の平滑化
############################
"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("test.bmp")

# 平均化フィルタ
# 周囲の画素の平均値をとって画像をぼかす(5*5範囲)
img2 = cv2.blur(img,(5,5))
plt.imshow(img2, interpolation="None")

# ガウシアンフィルタ
# 中心に近いピクセルを重視し、遠いピクセルを軽視して重み付け平均（ガウス分布）
img2 = cv2.GaussianBlur(img,(5,5),0)
# 新しい像を乗せる場所を作る -> 作らないと先のimshowで準備した像を上書きしてしまう
plt.figure()
plt.imshow(img2, interpolation="None")

# メディアンフィルタ
# 常に正方形の範囲を扱うため、一辺の長さだけを指定
img2 =cv2.medianBlur(img,5)
plt.figure()
plt.imshow(img2, interpolation="None")

# 2枚の画像を同時に表示
plt.show()
"""
############################
# エッジを抽出
############################
"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("test.bmp")

# ラプラシアンフィルタ
# 画像の「2次微分」を計算するため、画素値の変化（傾き）が急激に変わる場所を特定
# cv2.CV_64F:出力データの型（ビット深度） 64bit 浮動小数点型
img2 = cv2.Laplacian(img,cv2.CV_64F)

plt.imshow(img2, interpolation="None")
plt.show()
"""
############################
# 収縮処理
############################
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("test.bmp")

# 全ての値が1である3*3行列(フィルタ)作成
kernel = np.ones((3,3),np.uint8)
# print(kernel)
# 収縮(erode)処理
# kernelの範囲内に一つでも黒い画素(0)があれば、その中心の画素を黒にする
# iterationsの回数だけ繰り返す
# img2 = cv2.erode(img, kernel, iterations=1)
img2 = cv2.erode(img, kernel, iterations=2)

plt.imshow(img2, interpolation="None")
plt.show()
"""
############################
# 膨張処理
############################
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("test.bmp")
# 全ての値が1である3*3行列(フィルタ)作成
kernel = np.ones((3,3), np.uint8)
print(kernel)
# 膨張（Dilation）処理
# カーネルの範囲内に一つでも白い画素(255）があれば、その中心の画素を白にする
img2 = cv2.dilate(img, kernel, iterations=1)

plt.imshow(img2, interpolation="None")
plt.show()

