import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # version 0.11.0

df1 = pd.read_csv('sample1.csv')

X = df1.drop('y', axis=1)

y = df1['y']

#산점도 도출
sns.scatterplot(data=df1, x='x1', y='x2', hue='y')#, palette="Set2")
#plt.show()

#의사결정나무 작성
from sklearn.tree import DecisionTreeClassifier
#트리 모형으로 그림을 그리는 기능
from sklearn.tree import plot_tree
c_tree = DecisionTreeClassifier(min_impurity_decrease=0.05,random_state=0)
c_tree.fit(X, y)

#변수 이름 출력
xname = X.columns
yname = ['0','1']
plt.figure(figsize=(10,8)) #가로 10, 세로 8
#그래프로 구현함
plot_tree(c_tree, feature_names=xname, class_names=yname, filled=True, fontsize=12) #filled: 칼러
# plt.show()

direct2 = pd.read_csv('direct2.csv')
#전처리

direct2 = direct2.dropna()
print(direct2.isnull().sum())
X = direct2.drop('Buy',axis = 'columns')
y = direct2['Buy']

model_tree = DecisionTreeClassifier(max_depth=2,random_state=0)
model_tree.fit(X, y)

plt.figure(figsize=(12, 6)) #가로 12, 세로 6
xname = X.columns
yname = ['Nonbuyer','Buyer'] #[0,1]
plot_tree(model_tree, feature_names=xname, class_names=yname, filled=True, fontsize=12) 
plt.show()

#회귀 나무
from sklearn.tree import DecisionTreeRegressor
r_tree = DecisionTreeRegressor(min_impurity_decrease=10, random_state=0) 
r_tree.fit(X, y)

df2 = pd.read_csv('sample2.csv')
X = df2.drop('y', axis=1)
y = df2['y']
sns.scatterplot(data=df2, x='x', y='y', palette="Set2")
plt.show()

df=pd.read_csv('copdcat.csv' ,header=0)
X=df.drop(["CATScore"],axis=1)
y=df["CATScore"]

model_tree = DecisionTreeRegressor(max_depth=2, random_state=0)
fit_tree = model_tree.fit(X, y)

plt.figure(figsize=(10, 6))
xname = X.columns
plot_tree(fit_tree, feature_names=xname, filled=True, fontsize=12) 
# plt.show()







