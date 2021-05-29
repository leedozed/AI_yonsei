import re

e = 'taeyoungp@yonsei.ac.kr'
a = re.split('@', e)
# print(a)

# ['taeyoungp', 'yonsei.ac.kr']
# 첫번째 값의 4개 문자 + 한글이 아닌 값을 , *로 변환, 첫번째 값의 5번째 문자 중에서
d = a[0][:4] + re.sub('[^가-힣]', '*', a[0][4:])
# print(d)

text = "Yesterday is history, \ntomorrow is a mystery, \nbut today is a gift.\nThat's why it's called present."
# print(text)

text = text.lower()
# print(text)

# p = re.compile('day') #day를 포함
# p = re.compile('[day]') #d 또는 a 또는 y를 포함
# p = re.compile('[^day]') #d,a,y 를 제외
# p = re.compile('y.*y') #y롤 시작해서 임의의 문자가 0개 이상이고 y로 끝나는 가능한 긴 문자열
# p = re.compile('y.*?y') #y롤 시작해서 중간에 0개 이상의 임의의 문자를 포함하고 y로 끝나는 가능한 짮은 문자열(?의 기능)
# p = re.compile('^y.*y') #첫문자를 y롤 시작해서 중간에 0개 이상의 임의의 문자를 포함하고 y로 끝나는 가능한 긴 문자열
# p = re.compile('.+y') #앞에서 1개 이상의 임의의 문자를 포함하고 y로 끝나는 가능한 긴 문자열
p = re.compile('.+?y') #앞에서 1개 이상의 임의의 문자를 포함하고 y로 끝나는 가능한 짧은 문자열

print(p.search(text)) #전체에서 text 값을 검색 후 첫번째 결과 도출
print(p.match(text)) #처음부터 text 값을 검색
print(p.findall(text)) #전체에서 text값을 모두 검색 후 리스트로 호출
print(p.finditer(text)) #전체에서 text값을 모두 검색 후 반복문이 가능한 객체로 호출
for x in p.finditer(text): print(x.group(), x.span())
# day (6, 9) / day (53, 56) : 2개의 객체 검색 후 각 위치를 반환

p = re.compile('\n')
print(p.split(text))
print(re.sub('ry', 'gram', text))
# 한글이 아닌 것 | (, ), 줄바꿈, , . 가 아닌 것들을 _로 변경
print(re.sub('[^가-힝 | ^( | ^) | ^\n | ^, | ^.]', '_', text))

