import pandas as pd
iris = pd.read_csv('iris.csv', encoding = 'euc-kr')
# print(iris.head(5))

# 공분산
print(iris.cov().iloc[:2, :2])

# 상관계수
x = iris['꽃받침길이']
y = iris['꽃받침너비']
print(x.corr(y))
