# day17 > 2_텍스트빈도분석.py

# 1. 분석할 텍스트 준비
text_data = """Big data refers to the large volume of data – both structured and unstructured – that inundates a 
business on a day-to-day basis. But it’s not the amount of data that’s important. It’s what organizations do with the 
data that matters. Big data can be analyzed for insights that lead to better decisions and strategic business moves."""

# 2. 다양한 전처리
# 1) 정규화: 모든 문자를 소문자로
text_data = text_data.lower()  # .lower() <-> .upper() (소문자로 <-> 대문자로)
print(text_data)
# 2) 구두점과 불필요한 특수문자/기호 제거: 정규표현식
import re  # 정규표현식, python 내장lib

text_data = re.sub(r'[^\w\s]', '', text_data)
# \w: 문자 혹은 숫자, \s: 공백(스페이스바, 탭)  ^: 부정
# [^\w\s] : 문자, 숫자, 공백 아닌 것들 찾기
# re.sub[r'정규식', '대체할 문자', '기존 문자열']
# 기존 문자열에서 정규표현식에 해당되는 문자를 찾아 대체하는 함수
print(text_data)
# 3) 문자열 토큰(단어)화
words = text_data.split(" ")  # 띄어쓰기 기준으로 문자 구분
print(words)

# 3. 문자 개수 세기
from collections import Counter  # 컬렉션 (리스트, 딕셔너리, 집합)

word_count = Counter(words)  # 중복된 요소들의 개수를 튜플 형식으로 반환
print(word_count)  # ({단어:개수}, {단어:개수}, ...)

# 4. 빈도가 높은 상위 n개만큼 출력: .most_common(n): 상위 n개 반환
print(word_count.most_common(10))

# 5. 시각화: 워드클라우드
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 1) 워드클라우드 객체 생성
word_cloud = WordCloud(width=800, height=800, background_color='grey').generate(text_data)

# 2)
plt.imshow(word_cloud)  # 워드클라우드 객체를 matplotlib에 적용
plt.axis('off')  # 그래프 축 숨기기
plt.show()
