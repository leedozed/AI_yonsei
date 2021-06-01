#euclidean 거리 측정
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock
import pandas as pd
import numpy as np
# One-Hot Encoding: 문장을 토큰화한 후에 각 단어와 문자 간의 비교를 통해 1,0으로 표현
from sklearn.preprocessing import MultiLabelBinarizer

# #문자열 비교 
# from distance import jaccard
# #levenshtein

# from distance import levenshtein

# blood_type = ['A']

# s1 = '데이터사이언스'
# s2 = '빅데이터'
# print(jaccard(s1, s2))

diamonds = pd.read_csv('diamonds.csv')
print(diamonds.head( ))

vector1 = [diamonds['carat'][0], diamonds['price'][0]]
vector2 = [diamonds['carat'][100], diamonds['price'][100]]

# np.cov: 공분산 계산 / np.linalg.inv(): 역행렬 구하기
V_inv = np.linalg.inv(np.cov(diamonds['carat'], diamonds['price']))

print('<caraat 변수와 price 변수의 표본 공분산의 역행렬>')
print(V_inv)

sent1 = '빅데이터는 여러 분야에서 주목받고 있습니다'.split(' ')
sent2 = '빅데이터는 통계와 밀접한 관련이 있습니다'.split(' ')

sentences = [sent1, sent2]

print(f'문장1의 토큰화 결과: {sent1}')
print(f'문장2의 토큰화 결과: {sent2}')

mlb = ModuleNotFoundError()
df = pd.DataFrame(mlb.fit_transform(sentences), columns= mlb.classes_, index=['문장1', '문장2'])

print(df)
