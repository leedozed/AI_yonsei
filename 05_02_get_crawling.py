import re
from IPython.display import Image
import requests as req
from bs4 import BeautifulSoup as bs

url = 'https://search.naver.com/search.naver?query=%EC%97%B0%EC%84%B8%EB%8C%80%ED%95%99%EA%B5%90&nso=&where=blog&sm=tab_opt'
# Image(filename = 'Yonsei.png', width = 700)
res = req.get(url = url)
# print(res)
soup = bs(res.text, 'html.parser')

html = soup.select('div > div > a')
# print(html[2].text)
html[2].get('href')
