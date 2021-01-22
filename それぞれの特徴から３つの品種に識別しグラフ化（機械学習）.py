# アヤメデータを表データに変換
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris()

# DataFrameでデータを確認
# iris.dataの中身をDataFrameに変換
df1 = pd.DataFrame(iris.data,columns=["がく片の長さ","がく片の幅","花びらの長さ","花びらの幅"])
# iris.targetの中身をDataFrameに変換
df2 = pd.DataFrame(iris.target,columns=["品種"])
# df1とdf2を結合
df = pd.concat([df1,df2],axis=1)

# 品種ごとに表データを分ける
df_setosa = df[df["品種"] == 0]
df_versicolor =  df[df["品種"] == 1]
df_virginica =  df[df["品種"] == 2]

# 花びらの長さと幅で散布図を作る
plt.scatter(df_setosa["花びらの長さ"],df_setosa["花びらの幅"], label="setosa",cmap="terrain")
plt.scatter(df_versicolor["花びらの長さ"],df_versicolor["花びらの幅"], label="versicolor",cmap="terrain")
plt.scatter(df_virginica["花びらの長さ"],df_virginica["花びらの幅"], label="virginica",cmap="terrain")

# X軸の名前
plt.xlabel("petal length (cm)")
# Y軸の名前
plt.ylabel("petal width (cm)")

# 凡例を出力
plt.legend()

plt.show()
