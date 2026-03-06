# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 01:37:19 2026

@author: yoshikazu.nojiri
"""

# コピペしたら練習にならないので、直打ちすること！

###############################
# 外部プログラムを実行
###############################
"""
import os

os.system('"C:/Program Files/Internet Explorer/iexplore.exe" google.com')
"""

###############################
# マルチスレッドで関数を同時に実行
###############################
"""
import time
import random
from multiprocessing import Pool

def func(args):
    a,b = args
    t = random.random()
    # 0〜1秒の間、ランダムに待機
    time.sleep(t)
    print("compute %d + %d" % (a,b))
    return a+b

if __name__ == '__main__':   # Windowsでマルチプロセッシングを行う場合、この一文を書く
    # プロセスをCPUのコア数だけ準備
    p = Pool()
    
    # リスト内の3つのデータ(1,4),(2,9),(10,100)を準備したプロセスに割り振り
    # p.map：各プロセスにデータを渡して、funcを実行
    results = p.map(func, [(1,4),(2,9),(10,100)])
    print(results)
    time.sleep(5)
"""

###############################
# numbaを使って関数を高速化しなさい
###############################
from numba import jit
import time
import numpy as np

def calc_sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

# numbaによる高速化
# デコレータ コンパイルオプション
# 型推論ありのJIT 関数が呼び出された瞬間、Numbaが解析し、機械語に変換
@jit
def calc_sum_jit1(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

# nambaの型指定による高速化
# デコレータ コンパイルオプション
# 型指定ありのJIT 型推論しない分、更に速い
@jit('i8(i8[:])')
def calc_sum_jit2(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

arr = np.arange(10000000, dtype=np.int64)  # 0-999999

start = time.time()
sum = calc_sum(arr)
print("time (python): %1f sec" % (time.time()-start)) 

start = time.time()
sum = calc_sum_jit1(arr)
print("time (jit1): %1f sec" % (time.time()-start)) 
     
start = time.time()
sum = calc_sum_jit2(arr)
print("time (jit2): %1f sec" % (time.time()-start)) 
time.sleep(5)












