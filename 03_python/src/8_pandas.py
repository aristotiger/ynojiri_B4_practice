# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 01:34:24 2026

@author: yoshikazu.nojiri
"""

###############################
# sries（名前付きの数値列）の作成
###############################
"""
import pandas as pd

# ラベル付き1次元配列(Series)の作成
s = pd.Series([1,2,5,4,5], index=["a","b","c","d","e"])
print(s)
"""
###############################
# 表（dataframe）の作成
###############################
"""
import pandas as pd
#import numpy as np

## テストの点数
points = [
    [91, 80],
    [50, 90],
    [80, 85]    
]
# リストや辞書などのデータを、DataFrame（表）形式のオブジェクトに変換
df = pd.DataFrame(points)
print(df)
"""
###############################
# 行と列に名前をつけて表（dataframe）の作成
###############################
"""
import pandas as pd
#import numpy as np

## 名前・科目・点数のデータ
names = ['taro','jiro','hanako']
subjects = ['math','japanese']
points = [
    [91, 80],
    [50, 90],
    [80, 85]
]

## 表を作成
df = pd.DataFrame(points, columns=subjects, index=names)
print(df)
"""
###############################
# 表の保存と読み込み
###############################
"""
import pandas as pd
import numpy as np

## 名前・科目・点数のデータ
names = ['taro','jiro','hanako']
subjects = ['math','japanese']
points = [
    [91, 80],
    [50, 90],
    [80, 85]
]

## 表を作成
df = pd.DataFrame(points, columns=subjects, index=names)
print(df)

## 保存 (test.csvに保存)
## 日本語有の場合： df.to_csv("xxx.csv", encoding="shift_jis")
df.to_csv("test.csv", sep=",")

## 読み込み（編集したファイルを確認）
df2 = pd.read_csv('test.csv', index_col=0, header=0)
print(df2)

## +α
## pickleでの保存
df.to_pickle("test.pkl")
## 読み込み
df3=pd.read_pickle("test.pkl")
print(df3)
"""
###############################
# 表（dataframe）からデータの取り出し
###############################
"""
import pandas as pd
import numpy as np

## 名前・科目・点数のデータ
names = ['taro','jiro','hanako']
subjects = ['math','japanese']
points = [
    [91, 80],
    [50, 90],
    [80, 85]
]

## 表を作成
df = pd.DataFrame(points, columns=subjects, index=names)
print(df)
print()

## 確認
print("---全員の点数の取得---")
print(df.values)

print()
print("---列の名前の取得---")
print(df.columns)
print(df.columns[0])

print()
print("---行の名前の取得---")
print(df.index)
print(df.index[0])

print()
print("---リスト化---")
print(df.columns.to_list())
print(df.index.to_list())
"""
###############################
# column（科目名）やindex（人物名）の変更
###############################
"""
import pandas as pd
import numpy as np

## 名前・科目・点数のデータ
names = ['taro','jiro','hanako']
subjects = ['math','japanese']
points = [
    [91, 80],
    [50, 90],
    [80, 85]
]

## 表を作成
df = pd.DataFrame(points, columns=subjects, index=names)
print("---変更前---")
print(df)
print()

## column変更
df.columns=['english', 'math']

## index変更
df.index=['goro', 'jiro', 'hanako']

print("---変更後---")
print(df)
"""
###############################
# 単独の要素の選択&抽出
###############################
"""
import pandas as pd
import numpy as np

## 名前・科目・点数のデータ
names=['taro', 'jiro', 'hanako']
subjects=['math','japanese']
points = [
    [91, 80],
    [50, 90],
    [80, 85]
]

## 表を作成
df = pd.DataFrame(points, columns=subjects, index=names)

## 行・列名で指定
print(df.at['taro', 'japanese'])

## 行・列番号で指定
print(df.iat[0,1])
"""
###############################
# 複数要素の選択&抽出
###############################
"""
import pandas as pd
import numpy as np

## 名前・科目・点数のデータ
names=['taro', 'jiro', 'hanako']
subjects=['math','japanese']
points = [
    [91, 80],
    [50, 90],
    [80, 85]
]

## 表を作成
df = pd.DataFrame(points, columns=subjects, index=names)

## 特定の列
print(df['math'])
print(df.math)
print()

## columnやindexによる選択
print(df.loc[:,'math'])
print(df.loc['jiro',:])
print(df.loc['taro':'jiro',:])
print(df.loc[['taro','jiro'],['math','japanese']])
print()

#行列・番号で指定
print(df.iloc[[0,2],[0,1]])
print()

## 条件により行を抽出
print(df.query('math > 80'))
print(df[(df['math']>80) & (df['japanese']<90)])
print(df[(df['math']>80) | (df['japanese']<90)])
print(df[~(df['math']>80)])
"""
###############################
# 要素の変更
###############################
"""
import pandas as pd
import numpy as np

## 名前・科目・点数のデータ
names=['taro', 'jiro', 'hanako']
subjects=['math','japanese']
points = [
    [91, 80],
    [50, 90],
    [80, 85]
]

## 表を作成
df = pd.DataFrame(points, columns=subjects, index=names)

## 列(特定科目の点数)の変更
df.loc[:, 'japanese']=[10,50,90]
print(df)

## 行(特定生徒の点数)の変更
df.loc['hanako',:]=[100,100]
print(df)

## 全体
df.loc[:]=np.arange(6).reshape(3,2) * 100/6
print(df)

## 転置
df_t=df.T
print(df_t)
"""
###############################
# 様々な配列からの作成
###############################
"""
import pandas as pd
import numpy as np

## 空配列に追加
df=pd.DataFrame(index=[], columns=[])
print("---空配列---")
print(df)

## 行を一つづつ追加
## df.append() がもう存在しないため、例題のままでは動作しない
# df=pd.DataFrame(index=[], columns=['japanese','math','english','sports'])
dfs=[]
for i in range(4):
   # tempdf=pd.Series(np.random.randint(0,100,4),index=df.columns)
   # df=df.append(tempdf, ignore_index=True)
    tempdf = pd.Series(np.random.randint(0,100,4), index=['japanese','math','english','sports'])
    dfs.append(tempdf.to_frame().T)   # 行方向にする

df = pd.concat(dfs, ignore_index=True)
print(df)

## 辞書'dict'から作成
data = {
    "math":[100,60,80],
    "english":[40,20,50],
    "phｙsics":[90,85,70]
}
df=pd.DataFrame(data,index=['taro','jiro','hanako'])
print("\n---辞書から作成---")
print(df)

## 要素がない箇所は欠損値で埋められる
data={
    "math":{"taro":100, "jiro":60, "hanako":80},
    "english":{"taro":40, "hanako":50},
    "phｙsics":{"jiro":85, "hanako":70}    
}
df=pd.DataFrame(data)
print("\n---欠損値を含むデータ---")
print(df)
"""
###############################
# 欠損値の扱い
###############################
"""
import pandas as pd
import numpy as np
Nan=np.nan

## 名前・科目・点数のデータ
names=['taro','jiro','hanako']
subjects=['math','japanese','programming']
points=[
    [91, Nan, 50],
    [50, Nan, 40],
    [Nan, Nan, Nan]       
]
df=pd.DataFrame(points, columns=subjects, index=names)
print(df)

## すべてが欠損値の行を削除する
print(df.dropna(how='all'))
print()

## すべてが欠損値の列を削除する
print(df.dropna(how='all',axis=1))
print

## 名前・科目・点数のデータ
points=[
    [91, Nan, 50],
    [50, 80, 40],        
    [60, Nan, Nan]    
]
df2=pd.DataFrame(points, columns=subjects, index=names)
print(df2)
print()

## 欠損値が一つでも含まれる行を削除
print(df2.dropna())
print()
## 置換
print(df2.fillna(0))
print()

## 欠損値が一つでも含まれる行・列を抽出する
print(df2)
print(df2[df2.isnull().any(axis=1)])
print()

## df.mean()などの演算では、NaNは除外される
#print(df2.mean())
"""
###############################
# 要素や行・列の削除
###############################
"""
import pandas as pd
#import numpy as np

## 名前・科目・点数のデータ
names = ['taro', 'jiro', 'hanako']
subjects = ['math', 'japanese', 'programming']
points = [
    [91, 80, 100],
    [50, 90, 100],
    [80, 85, 100]
]

## 表を作成
df = pd.DataFrame(points, columns=subjects, index=names)

## 行削除
print(df.drop(index='taro'))
print()

## 列の削除
print(df.drop(columns='math'))
print()

## 複数の行と列の削除
print(df.drop(index=['taro', 'hanako'],columns=df.columns[[0,2]]))
"""
###############################
# 行・列の追加&結合
###############################
"""
import pandas as pd
import numpy as np

## 名前・科目・点数のデータ
names = ['taro', 'jiro', 'hanako']
subjects = ['grade', 'math', 'japanese', 'programming']
points = [
    ['A', 91, 80, 100],
    ['B', 50, 90, 100],
    ['S', 80, 85, 100]
]

## 表を作成
df = pd.DataFrame( points, columns=subjects, index=names )

## 列(科目)
## 列にスカラーや配列を追加
df['chemistry']=30
print(df)
print()

df['physics']=[40,45,45]
print(df)
print()

## 各列を用いて、新たな列の作成
df['science']=df['physics']+df['chemistry']
df['grade']=df['grade'].str.lower()  #大文字小文字変換
print(df)
print()

## 任意の場所に要素を追加
df.insert(1, 'history', pd.Series(['D', 'A',], index=['taro','hanako']))
print(df)
print()

### 行(名前)
## 行の追加
df.loc['goro']=0
print(df)
print()

## データフレームを追加
df2 = pd.DataFrame(np.ones(16).reshape(2,8)*100, index=['amuro', 'char'], columns=df.columns)
#print(df.append(df2))
print(pd.concat([df,df2]))
"""
###############################
# dataframeの結合
###############################
"""
import pandas as pd
#import numpy as np

## 名前・科目・点数のデータ
names=['taro', 'jiro']
points1=[
    [80, 100],
    [90, 100],
]

points2=[
    [60, 50],
    [90, 40],
]

df=pd.DataFrame(points1, columns=['physics', 'chemistry'], index=names)
df3=pd.DataFrame(points2, columns=['physics', 'chemistry'], index=["hanako", "maruko"])

## 横に結合(科目を追加)
df2=pd.DataFrame(points2, columns=['history','economics'], index=names)
print(pd.concat([df, df2], axis=1))
print()

## 盾に結合(生徒を追加)
print(pd.concat([df, df3]))
"""
###############################
# 行・列の追加&結合
###############################
import pandas as pd
import numpy as np

## 名前・科目・点数のデータ
names = ['taro', 'jiro', 'hanako']
subjects = ['grade', 'math', 'japanese', 'programming']
points = [
    ['A', 91, 80, 100],
    ['B', 50, 90, 100],
    ['S', 80, 85, 100]
]

## 表を作成
df=pd.DataFrame(points, columns=subjects, index=names)

## 列(科目)
## 列にスカラーや配列を追加
df['chemistry']=30
print(df)
print()

df['physics']=[40, 45, 45]
print(df)
print()

## 各列を用いて、新たな列を追加
df['science']=df['physics']+df['chemistry']
df['grade']=df['grade'].str.lower()  #大文字小文字変換
print(df)
print()

## 任意の場所に要素を追加
df.insert(1, 'history', pd.Series(['D','A',], index=['taro','hanako']))
print(df)
print()

## 行(名前)
## 行の追加
df.loc['goro']=0
print(df)
print()

## データフレーム追加
df2=pd.DataFrame(np.ones(16).reshape(2,8)*100, index=['amuro', 'char'], columns=df.columns)
print(pd.concat([df,df2]))






















