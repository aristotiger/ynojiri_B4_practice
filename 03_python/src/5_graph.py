# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:24:36 2026

@author: yoshikazu.nojiri
"""

# コピペしたら練習にならないので、直打ちすること！

%matplotlib inline

############################
# 1
############################
# 折れ線グラフを作成
"""
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,8,9,1]

plt.plot(x,y)
plt.show()
"""
############################
# 2
############################
# 棒グラフを作成
"""
# pyplot:分かりやすいユーザインターフェース
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,8,9,1]

plt.bar(x,y)
plt.show()
"""
############################
# 3
############################
# 散布図（点グラフ）を作成
"""
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,8,9,1]

plt.scatter(x,y)
plt.show()
"""
############################
# 4
############################
# 二次元arrayの値を色の濃淡で表示
"""
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(9).reshape((3,3))

print(a)
# 行列の数字を「色の濃淡」に変換して画像として表示
#plt.imshow(a, cmap="gray", interpolation="None")
plt.imshow(a, cmap="viridis", interpolation="None")
plt.show()
"""
############################
# 5
############################
# 1つのグラフに2つの折れ線グラフを生成
"""
import matplotlib.pyplot as plt
x = [1,2,3,4]
y1 = [10,8,9,1]
y2 = [1,5,4,3]

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
"""
############################
# 6
############################
# x軸，y軸にラベルを付ける
"""
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,8,9,1]

plt.plot(x, y)

plt.xlabel("x jiku")
plt.ylabel("y jiku")

plt.show()
"""
############################
# 7
############################
# x軸，y軸の範囲を制限する
"""
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,8,9,1]

plt.plot(x,y)

plt.xlim(1,3)       # x軸の範囲を1から3に制限
plt.ylim(8,10.5)    # y軸の範囲を8から10.5に制限

plt.show()
"""
############################
# 8
############################
# グラフを画像(png)で保存
"""
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,8,9,1]

plt.plot(x,y)
plt.savefig("test.png")
"""
############################
# 9
############################
# 連続的なグラフを連番画像（パラパラ漫画）で保存
"""
import numpy as np
import matplotlib.pyplot as plt

for i in range(10):
    x = np.arange(0, 3.14*2*i/10, 0.314/2)
    y = np.sin(x)
    
    plt.clf()    # 前回のグラフ消去
    plt.plot(x,y)
    plt.xlim(0, 3.14*2)
    plt.ylim(-1,1)
    plt.savefig("%03d.png" % i)
    plt.show()
"""
############################
# 10
############################
# 連続的なグラフを動画に変換
import numpy as np
import matplotlib.pyplot as plt
import os

# 画像保存フォルダ作成
if not os.path.exists("graph"):
    os.mkdir("graph")       # フォルダ作成
    
for i in range(100):
    x = np.arange(0, 3.14*2*i/10, 0.314/2)
    y = np.sin(x)
    
    plt.plot(x,y)
    plt.xlim(0, 3.14*2)
    plt.ylim(-1,1)
    plt.savefig("graph\%03d.png" % i)
    plt.clf()    # 前回のグラフ消去
    
# 動画生成
#os.system("ffmpeg -r 10 -i graph/%03d.png -y -vcodec libx264 -pix_fmt yuv420p out.mp4")
# フレームレート半分
os.system("ffmpeg -r 5 -i graph/%03d.png -y -vcodec libx264 -pix_fmt yuv420p out.mp4")









