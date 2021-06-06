import warnings

import numpy as np
import pandas as pd

from scipy import stats
from statsmodels.formula.api import ols
import statsmodels.api as sm

from sklearn.linear_model import Lasso
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns


ad_data = pd.DataFrame({'x': [5,  6,  7,  8,  9, 11, 12, 13, 14, 15],
                        'y': [16, 19, 18, 20, 24, 26, 30, 32, 31, 34]})


# plt.scatter('x', 'y', data=ad_data)
# plt.xlabel('Advertising expenses')
# plt.ylabel('Sales')
# plt.show() #데이터 산점도 출력                        

ad_model = ols('y~x', data = ad_data).fit()
print(ad_model.summary()) 