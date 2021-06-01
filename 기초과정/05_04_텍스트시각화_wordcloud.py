import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as MImage
from IPython.display import Image
import re
import requests as req
from bs4 import BeautifulSoup as bs
from wordcloud import WordCloud, STOPWORDS
import nltk #자연서 형태소 분석 라이브러리

    # 명사 추출
import nltk
# nltk.download('averaged_perceptron_tagger')

# 영어 불용어(stopwords) 사전
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

# 단어/문장 단위로 토큰화
nltk.download('punkt')
from nltk.tokenize import word_tokenize,sent_tokenize

url = 'https://www.google.com/amp/s/nymag.com/intelligencer/amp/2020/05/scott-galloway-future-of-college.html'
res = req.get(url)
soup = bs(res.text, 'html.parser')

text = soup.select('section > div.article-content.special-feature')[0].text
print(text[463:637])

#공백 제거
text_filtered = text.replace('\n', '').replace('\u200b','')

#불필요한 문자 제거
text_filtered = re.sub(r'[@%\\*=()/~#&\+á?\xc3\xa1\-\|\-\:\;\!\-\,\_\~\$\'\"]',' ',text_filtered.lower())

#숫자 제거
text_filtered = re.sub('\\d',' ',text_filtered)

#토큰화 하기
word_tokens = word_tokenize(text_filtered)

#토큰에 품사 할당
word_tokens_tag = nltk.pos_tag(word_tokens)
# print(word_tokens_tag[:10])

#명사만 추출
word_tokens = [word for (word, pos) in word_tokens_tag if (pos[:2] == 'NN')]

#3글자 이상만 추출
word_tokens = [word for word in word_tokens if len(word)>2]
#기본적인 불용어 제거
# list = list(stopwords)[:10]

result = [w for w in word_tokens if w not in stopwords]

#각 단어별 개수 튜플 형태로 리스트
from collections import Counter
word_freq = Counter(result)
# print(word_freq.most_common())

stopwords2 = ['year', 'part']
result = [w for w in result if w not in stopwords2]

# 복수명사랑 단수명사 결합
result = [re.sub("universities","university",x) for x in result]
word_freq = Counter(result)

# list 형태로 결합
words = ' '.join(result)

mask = np.array(MImage.open('University.png'))
mask = mask[:,:,0]

wc = WordCloud(background_color='white', mask = mask)
wc = wc.generate(words)
plt.figure(figsize=(10,10))
plt.imshow(wc, interpolation='bilinear') #경계선을 부드럽게 표현하기
plt.axis("off")
plt.show()

#단어별 상대 빈도 계산
# print(wc.words_)

wc.to_file("wordcloud.jpg")
