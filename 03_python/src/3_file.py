# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 16:57:10 2026

@author: yoshikazu.nojiri
"""

# コピペしたら練習にならないので、直打ちすること！

############################
# 1
############################
# リストの値を改行区切りのファイルに保存
"""
import codecs   #ファイルの文字コード（今回は Shift-JIS）ライブラリ
a = range(10)
#読み書きモードかつShift-JISでOPEN
f = codecs.open("test.txt","w","sjis") 

for i in a:
    f.write(i)
    #f.write(str(i))
    f.write("\n")

f.close()
"""
############################
# 2
############################
# 読み込んだファイルを1行づつ読み込んで表示
"""
import codecs
f = codecs.open("test.txt","r","sjis")

for line in f.readlines():
    line = line.replace("\n","") # 改行文字を削除
    print( line )

f.close()
"""
#上記のコードでは、エラーが発生するため、以下のように修正
"""
f = open("test.txt","r",encoding="sjis")

for line in f.readlines():
    line = line.replace("\n","") # 改行文字を削除
    print( line )

f.close()
"""
############################
# 3
############################
# 読み込んだファイルを1つの文字列として読み込み
"""
import codecs
f = codecs.open("test.txt","r","sjis")
txt = f.read()
f.close()

print( txt )
"""
############################
# 4
############################
# ファイルに書かれた数値を読み込んで，二次元のリストを生成
# open関数に.で繋げて、readlineを続けて実行（メソッドチェーン）
"""
data = []
for line in open("test.txt","r").readlines():
    line = line.strip()
    data.append([int(i) for i in line.split(",")])

print( data )
"""
############################
# 5
############################
# フォルダの作成
"""
import os    #オペレーティングシステムを操作するためのライブラリ

if not os.path.exists("test"):
    os.mkdir("test")
"""
############################
# 6
############################
# testフォルダ内に１０個のテキストファイルを作成（以降のプログラムで利用）
"""
import os
import codecs

if not os.path.exists("test"):
    os.mkdir("test")

for i in range(10):
    f = codecs.open("test/%03d.txt" % i, "w")
    f.write(str(i))
    f.close()
"""
############################
# 6
############################
# フォルダ内にあるテキストファイルのリストを取得
"""
# ワイルドカード（*）などを使って、ファイル名やパスを検索するために使う標準ライブラリ
import glob

# txtファイルを検索
files = glob.glob("test/*.txt")    # glob.globはlist型で返す
print(files)
"""
############################
# 7
############################
# ファイルのコピー
"""
# ファイルのコピー、移動、削除など、ファイルやフォルダを操作するためのライブラリ
import shutil

shutil.copy("test/005.txt", "copy.txt")
"""
############################
# 8
############################
# フォルダのコピー
import shutil

shutil.copytree("test","test_copy")











