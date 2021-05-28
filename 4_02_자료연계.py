import recordlinkage
import pandas as pd
local = pd.read_csv('Local_Restaurant.csv', encoding= 'utf-8')
Naver = pd.read_csv('Naver_Restaurant.csv', encoding= 'utf-8')

# print(local.head())
# print(Naver.head())


# 함수명 = lambda X값 : y값
# map(함수, 입력들): 입력 개수만큼 함수를 호출
# ' '.join(): 괄호 안의 문자를 ' ' 를 사이로 붙여줌
Naver['구이하주소'] = Naver['주소'].map(lambda x: ' '.join(x.split(' ')[1:])) #두번째 단어부터 빈칸으로 재결합 진행
local['구이하주소'] = local['주소'].map(lambda x: ' '.join(x.split(' ')[1:]))
local['구이하주소'] = local['구이하주소'].map(lambda x: x[:x.find('(')].strip()) #( 이하의 주소는 제거

# print(Naver.head())

# Naver.shape[0]: 1번째 열의 개수
# Naver.index: 리스트로 자료 입력
Naver.index = [f'rec-Naver-{i}' for i in range(Naver.shape[0])]
local.index = [f'rec-local-{i}' for i in range(local.shape[0])]

Naver.index.name = 'rec_id'
local.index.name = 'rec_id'


Naver['구'] = Naver['구이하주소'].map(lambda x:x.split(' ')[0])
local['구'] = local['구이하주소'].map(lambda x:x.split(' ')[0])

Naver['구미만주소'] = Naver['구이하주소'].map(lambda x: ' '.join(x.split(' ')[1:])) #두번째 단어부터 빈칸으로 재결합 진행
local['구미만주소'] = local['구이하주소'].map(lambda x: ' '.join(x.split(' ')[1:]))

# print(Naver.head())
# print(local.shape[0])
# print(local.head())

indexer = recordlinkage.Index()

indexer.full()
candidate_links = indexer.index(Naver, local)
print(len(candidate_links))

# '구'로 block 하는 경우
indexer = recordlinkage.Index()

indexer.block('구')
candidate_links = indexer.index(Naver, local)
print(len(candidate_links))