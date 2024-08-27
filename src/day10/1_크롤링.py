# day10 > 1_크롤링.py

"""
    정적 웹 페이지 크롤링
    # 1. "bs4" 느낌표 -> 패키지 설치
    # 2. 설정-프로젝트에서 + 버튼으로 검색창에서 검색 및 설치

    HTML 객체 파싱
    변수명 = BeautifulSoup(html파일객체, "html.parser")
    변수명 = BeautifulSoup(html형식문자열, "html.parser")

    파싱 메서드, 속성
    1. .find(식별자, 속성명=값): 지정한 식별자와 속성명이 동일한 태그 조회
        find(div), find(div, class_="box1"), find(div, id="box2")
    2. .select_one()
        select_one(div / .box1 / #box2)
    3. .findAll(): 지정한 식별자가 일치하는 태그 여러 개 추출해서 리스트로 반환
    4. .select()
        .태그명: 해당 태그들의 첫번쨰 태그 추출
        .text: 마크업 사이의 문자열 반환, 자식 & 자손 가능, 주로 중첩텍스트에 사용
        .string: 마크업 사이의 문자열, 자식만 가능하고 자손은 불가, 주로 단일텍스트일때
        .attrs: 해당 마크업의 속성 목록/리스트 반환
"""

# [1] 설치 및 import
from bs4 import BeautifulSoup

# [2] HTML 파일 객체
html_file = open("1_웹페이지.html", encoding="utf-8")

# [3] BeautifulSoup 객체 생성
html_obj = BeautifulSoup(html_file, "html.parser")
print(html_obj)

# [4] .find(식별자) & .select_one(식별자): 지정한 식별자의 마크업 조회하기
print(html_obj.find("div"))  # <div>[1] 여기를 크롤링하세요.</div>
print(html_obj.select_one("div"))  # <div>[1] 여기를 크롤링하세요.</div>

# [5] .findAll(식별자) & .select(식별자): 특정 마크업 여러 개 조회하기
print(html_obj.findAll("div"))  # [<div>[1] 여기를 크롤링하세요.</div>, <div class="box1">[2] 여기를 크롤링하세요!</div>, <div id="box2">[3] 여기를 크롤링하세요?</div>]
print(html_obj.select("div"))  # [<div>[1] 여기를 크롤링하세요.</div>, <div class="box1">[2] 여기를 크롤링하세요!</div>, <div id="box2">[3] 여기를 크롤링하세요?</div>]

# [6] .text: 호출된 마크업의 내용(문자열)만 추출
print(html_obj.find("div").text)  # [1] 여기를 크롤링하세요.
print(html_obj.find("div").string)  # [1] 여기를 크롤링하세요.

# [7] 반복문과 같이 활용
for div in html_obj.select("div"):  # 모든 div 마크업을 추출해서 리스트로 반환하고 리스트 반복문으로 처리
    print(div.string)

# [8] class 식별자를 조회
print(html_obj.find('box1'))  # None
print(html_obj.find('.box1'))  # None
print(html_obj.find('div', class_="box1"))  # <div class="box1">[2] 여기를 크롤링하세요!</div>
print(html_obj.select_one(".box1"))  # <div class="box1">[2] 여기를 크롤링하세요!</div>

# [9] id 식별자로 조회
print(html_obj.find("div", id="box2"))  # <div id="box2">[3] 여기를 크롤링하세요?</div>
print(html_obj.select_one("#box2"))  # <div id="box2">[3] 여기를 크롤링하세요?</div>

# 연습
html = '''
    <h1 id="title">한빛출판네트워크</h1>
    <div class="top">
        <ul class="menu">
            <li><a href="http://wwww.hanbit.co.kr/member/login.html"class="login">로그인</a>
            </li>
        </ul>
        <ul class="brand">
            <li><a href="http://www.hanbit.co.kr/media/">한빛미디어</a></li>
            <li><a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li>
        </ul>
    </div>'''

# [1] html 파싱 객체
soup = BeautifulSoup(html, 'html.parser')
print(soup)
print(soup.prettify())  # HTML 문서 들여쓰기 양식으로 출력

# [2] 태그(마크업) 파싱하기
# 파싱객체.마크업명
print(soup.h1)  # 1. 파싱객체.마크업명  # <h1 id="title">한빛출판네트워크</h1>
print(soup.div)  # <div class="top"> ~~ </div>
print(soup.ul)  # <ul class="menu"><li><a class="login" href="http://wwww.hanbit.co.kr/member/login.html">로그인</a></li></ul>
print(soup.li)  # <li><a class="login" href="http://wwww.hanbit.co.kr/member/login.html">로그인</a></li>
print(soup.a)  # <a class="login" href="http://wwww.hanbit.co.kr/member/login.html">로그인</a>
print(soup.findAll("ul"))  # [<ul class="menu"> ~~ </ul>]
print(soup.findAll("li"))  # [<li><a class="login" ...> ~~ <li><a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li>]
print(soup.findAll("a"))  # [[<a class="login" ...> ~~ <a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a>]
# .attrs : 지정한 마크업의 속성 목록을 딕셔너리 반환
print(soup.findAll('a')[0].attrs)  # {'href': 'http://wwww.hanbit.co.kr/member/login.html', 'class': ['login'] }
print(soup.findAll('a')[0]['href'])  # http://wwww.hanbit.co.kr/member/login.html
print(soup.findAll('a')[0]['class'])  # ['login']
print(soup.find('ul', attrs={'class': 'brand'}))  # vs find( 마크업 , class_='클래스명' )
print(soup.find(id="title"))  # vs .select_one(#ID명)
li_list = soup.select('div > ul.brand>li ')
for li in li_list:
    print(li.string)
