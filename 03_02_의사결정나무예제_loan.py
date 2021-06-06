import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('loan.csv')
# print(df)

df.isnull().sum().sum()
# print(df.isnull().sum().sum())

df.groupby('job').mean()
# print(df.groupby('job').mean())

#job의 범주형 변수를 평균에 따라 수치화
df['job'] = df['job'].replace({'Office':0, 'ProfExe':1, 'Other':2, 'Mgr':3, 'Self':4, 'Sales':5})
# df.groupby('job').mean()

#correlation 그림
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cmap='coolwarm',annot=True)
# plt.show()

#density plot
plt.figure(figsize=(15,15))
for i in range(0,9):
    plt.subplot(3,3,i+1)
    sns.kdeplot(data=df, x=df.columns[1:][i], hue="y")
# plt.show()

# 산점도
plt.figure(figsize=(10,5))
sns.scatterplot(data=df, x='DTI', y='delinquency', hue='y')
# plt.show()

from sklearn.tree import DecisionTreeClassifier
#그래프로 변경
from sklearn.tree import plot_tree

X = df.drop(['y'], axis=1)
y = df['y']
xname = X.columns
yname = ['Normal', 'Bad']

#기본 트리 생성
# c_tree = DecisionTreeClassifier(random_state=0) 
# c_tree.fit(X, y)
# plt.figure(figsize=(20,15))
# plot_tree(c_tree, filled=True) 
# plt.show()

# max_depth = 1 노드의 깊이
c_tree = DecisionTreeClassifier(max_depth=1,random_state=0) 
c_tree.fit(X, y)
plt.figure(figsize=(10,5))
plot_tree(c_tree, feature_names=xname, class_names=yname, filled=True, fontsize=12) 

c_tree = DecisionTreeClassifier(max_depth=2,random_state=0) 
c_tree.fit(X, y)
plt.figure(figsize=(10,5))
plot_tree(c_tree, feature_names=xname, class_names=yname, filled=True, fontsize=12) 

#분할 대상이 되는 노드의 샘플수의 최소값 설정
c_tree = DecisionTreeClassifier(min_samples_split=4000,random_state=0)
c_tree.fit(X, y)
plt.figure(figsize=(10,5))
plot_tree(c_tree, feature_names=xname, class_names=yname, filled=True, fontsize=12) 

#향상도의 크기
c_tree = DecisionTreeClassifier(min_impurity_decrease=0.005,random_state=0) 
c_tree.fit(X, y)
plt.figure(figsize=(10,10))
plot_tree(c_tree, feature_names=xname, class_names=yname, filled=True, fontsize=12) 

#복잡도 함수의 알파값 - 트리 크기 제한
c_tree = DecisionTreeClassifier(ccp_alpha=0.005,random_state=0) 
c_tree.fit(X, y)
plt.figure(figsize=(15,10))
plot_tree(c_tree, feature_names=xname, class_names=yname, filled=True, fontsize=12) 
# plt.show()

#비용복잡도 함수 계산
c_tree = DecisionTreeClassifier(random_state=0) 
path = c_tree.cost_complexity_pruning_path(X, y)
path = pd.DataFrame(path)
# print(path)

#학습데이터의 그래프
fig, ax = plt.subplots()
ax.plot(path.ccp_alphas, path.impurities, marker='o', drawstyle="steps-post")
ax.set_xlim(0.1, 0)  # decreasing order

fig, ax = plt.subplots()
ax.plot(path.ccp_alphas, path.impurities, marker='o', drawstyle="steps-post")
ax.set_xlim(0.004, 0)  # decreasing order
# plt.show()

#최적의 알파 찾기
from sklearn.model_selection import GridSearchCV
np.random.seed(0)
g_cv = GridSearchCV(DecisionTreeClassifier(random_state=0),
              param_grid={'ccp_alpha': np.arange(0.000, 0.005, 0.0001)}, cv=10, n_jobs=-1) #10개 데이터로 교차타당성 검증
g_cv.fit(X, y)

c_tree = DecisionTreeClassifier(ccp_alpha=0.0033,random_state=0) 
c_tree.fit(X, y)
plt.figure(figsize=(15,10))
plot_tree(c_tree, feature_names=xname, class_names=yname, filled=True, fontsize=10) 
# plt.show()

np.random.seed(0)
g_cv = GridSearchCV(DecisionTreeClassifier(random_state=0),
              param_grid={'ccp_alpha': np.arange(0.000, 0.005, 0.0001),
                          'min_impurity_decrease': np.arange(0,0.003,0.0005),
                          'min_samples_split': np.arange(800,1200,200)},ㅕㅗㅠ
                    cv=10, n_jobs=-1)
g_cv.fit(X, y)

# print('selected:',g_cv.best_params_)
# print('score   :',g_cv.best_score_)

# 최종 최적의 의사결정 나무 생성
c_tree = DecisionTreeClassifier(ccp_alpha=0.0,min_impurity_decrease=0.001,min_samples_split=1000,random_state=0) 
c_tree.fit(X, y)
plt.figure(figsize=(15,15))
plot_tree(c_tree, feature_names=xname, class_names=yname, filled=True, fontsize=9) 
plt.show()




