# day18 > 2_한글단어분석.py
# 자료 준비: etnews json 파일
import json  # json 처리
import re  # regex
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager
from wordcloud import WordCloud

# 1. 데이터 준비
# 1-1. 파일 읽기
file_name = "etnews.kr_facebook_2016-01-01_2018-08-01_4차 산업혁명.json"
file = open(file_name, 'r', encoding='utf-8')
file_data = file.read()
json_data = json.loads(file_data)  # json.loads(): json 문자열 -> python dict <-> json.dumps(): python dict -> json 문자열
# print(json_data)  # 리스트 타입

# 1-2 분석할 내용 추출
message = ""
for item in json_data:
    # 만약에 item(요소) 내 'message' 키가 있으면
    if 'message' in item.keys():
        # 전처리 (regex)
        # print(item['message'])  # 분석할 문장
        # 특수문자 제거: 정규표현식 regex로 특수문자를 공백으로 치환
        message += re.sub(r'[^\w]', " ", item['message'])
# print(message)  # 결과 확인

# 1-3 품사 태깅: 명사 추출
from konlpy.tag import Okt
okt = Okt()
words = okt.nouns(message)  # 명사만 추출
# print(words)  # 결과 확인

# 2. 데이터 분석
# 2-1. 단어 빈도 분석
from collections import Counter
words_count = Counter(words)  # Counter(리스트/튜플/문자열): 요소들의 빈도수를 계산하는 객체
print(words_count)

# 2-2 단어 빈도 딕셔너리화
word_count = {}
# word_count = dict() vs word_count = {}
for word, count in words_count.most_common(80):
    if len(word) > 1:  # 단어 길이가 1인 경우는 제외
        word_count[word] = count
        # {'단어': 빈도수}
print(word_count)

# 3. 시각화
# matplotlib 한글 표시하기
# 1) 폰트 경로
font_path = "C:/windows/fonts/malgun.ttf"  # 윈도우에서 폰트 설치된 경롬
# 2) 폰트 설정 객체로 폰트 설정
font_name = font_manager.FontProperties(fname=font_path).get_name()  # 지정 경로의 폰트 파일에서 폰트 이름 가져오기
# 3) 차트에 적용
matplotlib.rc('font', family=font_name)
# 시스템 폰트 경로가 명확하면
# matplotlib.rc('font', family='Malgun Gothic')

plt.bar(word_count.keys(), word_count.values())  # plt.bar(x축, y축)
plt.xticks(rotation=45)  # x축 레이블 기울기
plt.show()

# 4. 시각화 2: 워드클라우드

wc = WordCloud(font_path, background_color='ivory').generate_from_frequencies(word_count)
# .generate_from_frequencies(dict): 단어와 빈도수를 dict()로 받아 시각화

plt.imshow(wc)  # 워드클라우드 표시 설정
plt.axis('off')  # x, y축 표시 X
plt.show()

