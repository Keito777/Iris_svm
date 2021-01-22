import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv("train.csv")
df_test = pd.read_csv("test.csv")

#それぞれの年齢の平均を見る
print(df_train["Age"].mean())
print(df_test["Age"].mean())
#平均に少しズレがあるのでtrainデータとtestデータを結合
df_w = pd.concat([df_train,df_test])
print(len(df_w))
#＜結合したデータから、敬称ごとの平均値の算出＞
#①結合した表データから、新しい表データにそれぞれの敬称に分ける
#contains()はこの中に指定した値を含むものを取得。strで文字列のみの指定
df_mr = df_w[df_w["Name"].str.contains("Mr.")]
df_miss = df_w[df_w["Name"].str.contains("Miss.")]
df_mrs = df_w[df_w["Name"].str.contains("Mrs.")]
df_master = df_w[df_w["Name"].str.contains("Master.")]

#②それぞれの敬称の平均値を取得
mr_mean = df_mr["Age"].mean()
miss_mean = df_miss["Age"].mean()
mrs_mean = df_mrs["Age"].mean()
master_mean = df_master["Age"].mean()
all_mean = df_w["Age"].mean()               #敬称が入ってないデータもあるかも
#＜欠損値の補完＞
#❶Mr.が付く要素かつ欠損値であるものの行とAgeの列の要素を取得。#2年P７９の応用
#print(df_train.loc[df_train["Name"].str.contains("Mr.")]["Age"]) 
#print(df_train.loc[df_train["Name"].str.contains("Mr.")&df_train["Age"].isnull()]["Age"]) 
#❷欠損値の補完（欠損値を②で作った平均値に補完する）
df_train.loc[df_train["Name"].str.contains("Mr.")&df_train["Age"].isnull()]["Age"] = mr_mean
df_train.loc[df_train["Name"].str.contains("Miss.")&df_train["Age"].isnull()]["Age"] = miss_mean
df_train.loc[df_train["Name"].str.contains("Mrs.")&df_train["Age"].isnull()]["Age"] = mrs_mean
df_train.loc[df_train["Name"].str.contains("Master")&df_train["Age"].isnull()]["Age"] = master_mean
df_train["Age"].fillna(all_mean,inplace=True)#敬称がないデータの補完。inplace=Trueで上書きをする
print(df_train.isnull().sum())

#❷（test用）
df_test.loc[df_test["Name"].str.contains("Mr.")&df_test["Age"].isnull()]["Age"] = mr_mean
df_test.loc[df_test["Name"].str.contains("Miss.")&df_test["Age"].isnull()]["Age"] = miss_mean
df_test.loc[df_test["Name"].str.contains("Mrs.")&df_test["Age"].isnull()]["Age"] = mrs_mean
df_test.loc[df_test["Name"].str.contains("Master")&df_test["Age"].isnull()]["Age"] = master_mean
df_test["Age"].fillna(all_mean,inplace=True)
print(df_test.isnull().sum())

#<ヒストグラム化（年齢と生存率の関係性）>
#⑴生存と死亡を分ける
df_w_0 = df_train[df_train["Survived"]==0]
df_w_1 = df_train[df_train["Survived"]==1]
#ヒストグラム化
#plt.figure(figsize=(15,20))
plt.hist(x=[df_w_0.Age,df_w_1.Age])
plt.legend(["died","survived"])
plt.show()
