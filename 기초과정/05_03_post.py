import re
from IPython.display import Image
import requests as req
from bs4 import BeautifulSoup as bs

# url = 'https://search.naver.com/search.naver?query=%EC%97%B0%EC%84%B8%EB%8C%80%ED%95%99%EA%B5%90&nso=&where=blog&sm=tab_opt'
# # Image(filename = 'Yonsei.png', width = 700)
# res = req.get(url = url)
# # print(res)
# soup = bs(res.text, 'html.parser')

# html = soup.select('div > div > a')
# # print(html[2].text)
# html[2].get('href')

url = 'http://kiss.kstudy.com/search/sch-result.asp'
data = {'json': '{"prefixQuery":{"inst":null,"publ":null,"exYear":null,"issn":null,"mbcdls":[],"publPldv":null,"ciInfo":null},"collectionQuery":{"queries":[{"field":"전체","value":"빅데이터","prefix":""}],"reQueries":[]},"dateRange":null,"sort":null,"isForwardMatch":false}',
    'startCount': '0', 
    'pageScale': '100'}
# data = {'json': '{"prefixQuery":{"inst":null,"publ":null,"exYear":null,"issn":null,"mbcdls":[],"publPldv":null,"ciInfo":{"title":"등재정보","field":"CI_INFO","value":[{"title":"KCI등재","value":"KCI등재"},{"title":"SCOPUS","value":"SCOPUS"}]}},"collectionQuery":{"queries":[{"field":"전체","value":"빅데이터","prefix":""}],"reQueries":[]},"dateRange":null,"sort":null,"isForwardMatch":false,"isContainsAttach":false}',
#         'startCount': '0',  # 첫 번째 페이지
#         'pageScale': '100'} # 한 페이지에 100개의 논문 리스트 나열

res = req.post(url = url, data = data)

soup = bs(res.text, 'html.parser')
kws = soup.select('div.key-words')
# print(kws[0]) #이중 리스트 형태

kws = [kw.select('span > a') for kw in kws]

# 1) kws 논문들 중 각각 논문을 선택 후 2) 각 논문의 키워드를 찾고 공백을 제거
kws = [[x.text.strip() for x in kw] for kw in kws]
#한글이 아닌 경우 제외

kws = [[re.sub("[^가-힣]","",x) for x in kw] for kw in kws]

print(kws[:3])


# Dart 공시 정보 가져오기
url = 'http://dart.fss.or.kr/dsab001/main.do?autoSearch=true#'
data = {'currentPage': '1'
, 'maxResults': '100'
, 'maxLinks': '10'
, 'sort': 'date'
, 'series': 'desc'
, 'textCrpCik': '00266961'
, 'textCrpNm': 'naver'
, 'finalReport': 'recent'
, 'startDate': '20201129'
, 'endDate': '20210529'}

res = req.post(url = url, data = data)
soup = bs(res.text, 'html.parser')
data_list = soup.select('title')
print(data_list)

