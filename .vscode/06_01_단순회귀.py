import pandas as pd
import numpy as np
import statsmodels.api as sm # 통계모형
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt  # 박스플랏, 산점도

usedcar1 = pd.read_csv('usedcar1.csv')
# print(usedcar1)

usedcar1.lm = smf.ols('Price ~ Odometer', data=usedcar1).fit()
print(usedcar1.lm.summary())

plt.scatter(x='Odometer', y='Price', data=usedcar1)
plt.plot(usedcar1['Odometer'], usedcar1.lm.fittedvalues, color='red', linewidth=1)
plt.title('Scatter Plot')
plt.xlabel('Odometer')
plt.ylabel('Price')