# day18 > 4_한글기사분석.py
# 주제: 다음뉴스 경제섹션 최신 기사 10페이지 기사들의 제목 단어분석

from bs4 import BeautifulSoup
import urllib.request # URL 크롤링 라이브러리
import re
from konlpy.tag import Okt  # konlpy 패키지 불러오기
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager
from wordcloud import WordCloud
from collections import Counter

# [1] 데이터 준비
titles_string = ""
for page in range(1, 11):
    news_url = f"https://news.daum.net/breakingnews/economic?page={page}"
    response = urllib.request.urlopen(news_url)  # 지정 url 요청후 응답 받기
    html_data = response.read()  # 응답 받은 내용물 전체 읽어오기
    # print(html_data)  # 체크
    soup = BeautifulSoup(html_data, "html.parser")  # 지정 html 문자열로 html 파싱 객체 생성
    titles = soup.select(".list_news2 > li > .cont_thumb > .tit_thumb > a")
    # print(titles)
    for title in titles:
        # print(title)
        title_re = re.sub(r"[^\w]", " ", title.string)
        # print(title_re)
        titles_string += title_re + " "

# [2] 품사 태깅
okt = Okt()
title_tagged = okt.pos(titles_string)
# print(title_tagged)

# [3] 단어 빈도수 분석
title_nouns = okt.nouns(titles_string)
word_count = Counter(title_nouns)
# print(word_count)

# [4] 시각화 1. 히스토그램
word_count_dict = {}
for word, count in word_count.most_common(30):
    if len(word) > 1:
        word_count_dict[word] = count

matplotlib.rc('font', family='Malgun Gothic')
plt.bar(word_count_dict.keys(), word_count_dict.values())
plt.xticks(rotation=45)
plt.show()

# [4-1] 시각화 2. 워드클라우드
wc = WordCloud(font_path="C:/windows/fonts/malgun.ttf", background_color='ivory').generate_from_frequencies(word_count_dict)
plt.imshow(wc)
plt.axis('off')
plt.show()
