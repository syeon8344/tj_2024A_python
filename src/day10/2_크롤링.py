# day10 > 2_크롤링.py
from bs4 import BeautifulSoup  # 모듈 가져오기
import urllib.request, urllib.parse  # URL 크롤링 라이브러리
# [실습1] http://quotes.toscrape.com
url = "http://quotes.toscrape.com"  # 크롤링할 url
response = urllib.request.urlopen(url)  # 지정 url 요청후 응답 받기
html_data = response.read()  # 응답 받은 내용물 전체 읽어오기
# print(html_data)  # 체크
soup = BeautifulSoup(html_data, "html.parser")  # 지정 html 문자열로 html 파싱 객체 생성
# print(soup.prettify())  # 체크

# 특정 마크업/태그 파싱
quote_divs = soup.select(".quote")
print(quote_divs)
for quote in quote_divs:
    # 각 명언 문구 추출
    print(quote.select_one('.text').string)
    # 각 명언 저자 추출
    print(quote.select_one('small').string)
    # 각 명언 태그들 추출
    for tag in list(map(lambda x: x.text, quote.select('.tag'))):
        print(tag, end="\t")
    print("\n")

# [실습2] https://v.daum.net/v/20240827074833139
url = "https://v.daum.net/v/20240827074833139"
response = urllib.request.urlopen(url)
html_data = response.read()
soup = BeautifulSoup(html_data, "html.parser")
# print(soup.prettify())  # 확인

# 파싱하기
ps = soup.select("p")
# print(ps)
# 기사 제목
print(soup.select_one(".tit_view").text)
for p in ps:
    # 기사 본문
    if p.text != "":
        print(p.text)

print(soup.select_one(".news_view").text)

# [실습3] https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=부평구+날씨 <- 인식 안된다.
# 방법 1: 한글 변환된 문자열 https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B6%80%ED%8F%89%EA%B5%AC+%EB%82%A0%EC%94%A8
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=" + urllib.parse.quote("부평구+날씨")
response = urllib.request.urlopen(url)
html_data = response.read()
# print(html_data)
soup = BeautifulSoup(html_data, "html.parser")
# print(soup.prettify())
# 온도 추출
print(soup.select(".temperature_text"))
# <div class="temperature_text"> <strong><span class="blind">현재 온도</span>27.2<span class="celsius">°</span></strong> </div>
print(soup.select(".temperature_text")[0].text)  # 현재 온도27.2°
print(soup.select(".summary_list")[0].select(".sort")[1].text)  # 습도 68%
