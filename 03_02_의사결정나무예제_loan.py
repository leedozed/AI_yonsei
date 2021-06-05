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

#기본 트리 생성
c_tree = DecisionTreeClassifier(random_state=0) 
c_tree.fit(X, y)
plt.figure(figsize=(20,15))
plot_tree(c_tree, filled=True) 
plt.show()


