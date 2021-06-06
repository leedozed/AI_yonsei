import pandas as pd
from pandas import Series, DataFrame
import numpy as np                                             #넘파이:벡터행렬연산, 수학함수계산
from scipy import stats                                        #싸이파이:수치해석, stats:확률분포

path = '/Users/yhjeon/Dropbox/_lecture/Yonsei-Naver/python/'

dft = pd.read_csv('Default.csv')
dft.head()

# print(dft.head())

#student 값이 yes 이면 1을 반환 후 astype(np.int)로 숫자로 변횐 후 더미 변수를 생성
dft['studentYes'] = (dft['student']=='Yes').astype(np.int)      #또는 np.multiply(dft['student']=='Yes',1)\n,
dft['defaultYes'] = (dft['default']=='Yes').astype(np.int)      #또는 np.multiply(dft['default']=='Yes',1)\n,
dft['income'] = dft['income']/1000                              #income in tho. dollars\n,
dft.head()
# print(dft.head())

#로지스틱 회귀모형 적합을 위해 라이브러리 호출(glm 함수)
import statsmodels.api as sm                                    #통계모형  \n",

#R과 유사하게 로지스틱 회귀가 가능함
import statsmodels.formula.api as smf

#glm함수로 함수 적합 / family=sm.families.Binomial(): Binomial이 로직함수 의미함 / fit()를 통해 함수 적합
fit1 = smf.glm(formula = 'defaultYes~studentYes', data=dft, family=sm.families.Binomial()).fit()
fit1.summary()
#print(fit1.summary())

#family가 없으면  Gaussian default
fit0 = smf.glm(formula = 'defaultYes~studentYes', data=dft).fit()
fit0.summary()
#print(fit0/.summary())

fit2 = smf.glm(formula = 'defaultYes~balance', data=dft, family=sm.families.Binomial()).fit()
fit2.summary()
print(fit2.summary())