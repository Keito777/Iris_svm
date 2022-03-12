from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split as split
from sklearn import svm

iris = load_iris()

# 学習用データとテストデータにシャッフルして分割
x_train,x_test,y_train,y_test = split(iris.data,iris.target,train_size=0.8,test_size=0.2)

#SVCアルゴリズムのオブジェクトを生成
clf = svm.SVC() #SCVはSVMに基づくクラス分類方法　

# fitメソッドで学習
clf.fit(x_train, y_train)

# predictメソッドでテスト用データを利用して予測
pred = clf.predict(x_test)

# 予測と答えがどれくらいあっているか
result = list(pred == y_test).count(True) / len(y_test) # 正解した数を全体数で割る
print("正解率"+str(result))
