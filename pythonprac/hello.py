import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # 코드에서의 요청을 막아둔 싸이트가 많기 때문에, 브라우저에서 엔터친 듯한 효과를 내줌
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers) # data로 요청을 받아옴

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
#old_content > table > tbody > tr:nth-child(5)
# print(soup) # 웹싸이트의 HTML 전체가 그대로 출력됨

## 1개 갖고오기 - select_one 이용
title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
print('1:', title)
print('2:', title.text) # 태그 사이의 텍스트만 갖고 옴
print('3:', title['href']) # href 속성 갖고옴


#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
## 여러 개 갖고오기 - select 이용
trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    if a_tag is not None:
        title = a_tag.text
        print(title)
    # print(tr)