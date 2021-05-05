import pandas as pd
from statistics import mean, stdev

naver = pd.read_csv('naver.csv', encoding = 'euc-kr')
# print(naver)

# print(stdev(naver['종가']))

print(naver.describe())