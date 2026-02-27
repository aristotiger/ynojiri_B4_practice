# -*- coding: 9utf-8 -*-
"""
Created on Thu Feb 26 20:13:16 2026

@author: yoshikazu.nojiri
"""

# コピペしたら練習にならないので、直打ちすること！

############################
# 1
############################
# リストからarrayを生成
"""
import numpy as np      # 数値計算ライブラリ
a = np.array([1,2,3])   # array型：リストではなく、numpy配列

print(a)
"""
############################
# 2
############################
# リストから二次元arrayを生成
"""
import numpy as np
a = np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]])

print(a)
"""
############################
# 3
############################
# 0～9の要素を持った一次元arrayの生成
"""
import numpy as np
a = np.arange(9)   # Numpy配列 0～8を返す

print(a)
"""
############################
# 4
############################
# 0～9の要素を持った一次元arrayを3×3の二次元arrayに変換
"""
import numpy as np
a = np.arange(9)      # Numpy配列 0～8を返す
b = a.reshape((3,3))  # データの順番はそのままで、配列の次元だけを変更

print(b)
"""
############################
# 5
############################
# 二次元arrayの要素を一列（１次元）に並べる
"""
import numpy as np
a = np.arange(9).reshape((3,3))
b = a.flatten()

print(a)
print(b)
"""
############################
# 6
############################
# arrayの要素に定数を足す
"""
import numpy as np
a = np.arange(9)
a = a.reshape((3,3))

b = a + 100         # array型のすべての要素に加算

print(b)
"""
############################
# 7
############################
# 2つのarrayの要素同士の足し算
"""
import numpy as np
a = np.arange(9)
a = a.reshape((3,3)) 

b = np.arange(100,109)
b = b.reshape((3,3)) 

c = a + b

print(a)
print("+")
print(b)
print("=")
print(c)
"""
############################
# 8
############################
# 2つのarrayの要素同士の掛け算（アダマール積）
"""
import numpy as np
a = np.arange(9)
a = a.reshape((3,3))

b = np.arange(100,109)
b = b.reshape((3,3))

c = a * b

print(a)
print("*")
print(b)
print("=")
print(c)
"""
############################
# 9
############################
# 2つのarrayの行列の掛け算
"""
import numpy as np
a = np.arange(3)
a = a.reshape((3,1))

b = np.arange(100,103)
b = b.reshape((1,3))

c = a * b

print(a)
print("*")
print(b)
print("=")
print(c)
"""
############################
# 12
############################
# arrayの行方向の合計，列方向の合計，全ての要素の合計を計算
"""
import numpy as np
a = np.arange(9).reshape((3,3))

print(a)
print("====")
print("rows: ", np.sum(a,1))
print("cols: ", np.sum(a,0))
print("total: ", np.sum(a))
"""
############################
# 13
############################
# arrayの行方向の平均，列方向の平均，全ての要素の平均を計算
"""
import numpy as np
a = np.arange(9).reshape((3,3))

print(a)
print("----")
print("rows", np.mean(a,1))
print("cols", np.mean(a,0))
print("total", np.mean(a))
"""
############################
# 14
############################
# arrayの一部を取り出し
"""
import numpy as np
a = np.arange(81).reshape((9,9))
#3行目から6行目 (実際の4行目から7行目)を取り出し
#2列目から4列目 (実際の3列目から5列目)を取り出し
b = a[3:7,2:5]  # 4×3行列

print(b)
"""
############################
# 15
############################
# arrayの各要素に対して，sin, con, log, expを一括で計算
"""
import numpy as np
# +0.1は、数学的なエラー（log(0)）を回避するため
a = np.arange(9).reshape((3,3))+0.1

print("-sin")
print(np.sin(a))
print("-cos")
print(np.cos(a))
print("-log")
print(np.log(a))
print("-exp")
print(np.exp(a))
"""
############################
# 16
############################
# 名前のarray["Taro", "Hanako", "Jiro"]と，テストの点数のarray[95, 80, 90]がある時，
# 点数が90点以上の人を抽出
"""
import numpy as np

names = np.array(["Taro","Hanako","Jiro"])
points = np.array([95,80,90])

print( names[ points>=90 ] )
"""
############################
# 17
############################
# 特定の条件を満たすarrayのインデックスを取得
"""
import numpy as np
a = np.arange(1,10).reshape((3,3))

y,x = np.where( a>5 )

print(y)        # 5より大きい成分がある行
print(x)        # 5より大きい成分がある列
"""
############################
# 18
############################
# 行列をファイルに保存
"""
import numpy as np
a = np.arange(9).reshape((3,3))

np.savetxt("npdata.txt", a)

# または以下のコード
# NumPy専用のバイナリ形式データ
# np.save("npdata.npy", a)
"""
############################
# 19
############################
# ファイルから行列を読み込み
import numpy as np

a = np.loadtxt("npdata.txt")

# または以下のコード
b = np.load("npdata.npy")

print(a)
print(b)















