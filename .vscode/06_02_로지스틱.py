
#%%

import pandas as pd
import numpy as np
import statsmodels.api as sm # 통계모형
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt  # 박스플랏, 산점도

#그래프 탐색
import seaborn as sns


direct1  = pd.read_csv('direct1.csv')
# print(direct1)

# 데이터 결측시 확인 - isnull: 결측치 = true 반환
missing = direct1.isnull().sum()
# print(missing) #Age는 234의 결측치 존재
# Buy      0
# Age    234

#결측치 제거 dropna
direct1 = direct1.dropna()

# 특정변수 구성 확인
buy = direct1['Buy'].value_counts()
# print(buy)

sns.boxplot(x= 'Buy', y = 'Age', data = direct1)

# buy_0 = direct1['Age'].loc[direct1['Buy'] == 0]
# buy_1 = direct1['Age'].loc[direct1['Buy'] == 1]
# plt.hist(buy_0, alpha = 0.5)
# plt.hist(buy_1, alpha = 0.5)

direct1.logit = smf.glm('Buy ~ Age', data = direct1, family = sm.families.Binomial()).fit()
# print(direct1.logit.summary())

#설명력 측정
from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(direct1['Buy'], direct1.logit.fittedvalues)
# print(roc_auc)

direct2 = pd.read_csv('direct2.csv')
direct2.isnull().sum()
# print(direct2.isnull().sum())

direct2 = direct2.dropna()
direct2.shape
# print(direct2.shape)

direct2.logit = smf.glm('Buy ~ Age + Gender + Married + Children + Income + Ccard + Recent + Climate + Urban', data = direct2, family = sm.families.Binomial()).fit()
# print(direct2.logit.summary())

direct2.logit2 = smf.glm('Buy ~ Age + Gender + Married + Children + Income + Ccard + Recent + Urban', data = direct2, family = sm.families.Binomial()).fit()
# print(direct2.logit2.summary())

direct2.logit3 = smf.glm('Buy ~ Age + Gender + Married + Children + Income + Recent + Urban', data = direct2, family = sm.families.Binomial()).fit()
# print(direct2.logit3.summary())

roc_auc = roc_auc_score(direct2['Buy'], direct2.logit3.fittedvalues)
print(roc_auc)

#결과 해석을 위해 각 변수의 베타값을 exp(계수)으로 전환
np.exp(direct2.logit3.params)
print(np.exp(direct2.logit3.params))
# Age          0.940726 1살 증가하면 구매 가능성이 94%수준으로 하락
# Gender       1.555601 여성(1)이 남성보다 구매 가능성이 1.56배 높음
# Married      2.120887
# Children     1.462480
# Income       1.002069
# Recent       1.642137
# Urban        1.607687

#구매확률 예측

smith = [35,1,1,1,500,1,1]
johnson = [36,0,1,2,550,0,0]

people = pd.DataFrame([smith, johnson], columns=['Age', 'Gender', 'Married', 'Children', 'Income', 'Recent', 'Urban'])

direct2.logit3.predict(people)
print(direct2.logit3.predict(people))




# %%
