# day17 > 1_영문분석.py

import pandas as pd  # DataFrame, to csv & from csv
import glob  # 파일 경로와 이름을 지정해서 파일 처리
import re  # regex 정규식
from functools import reduce  # 2차원 리스트를 1차원 리스트로 차원 낮추기
from nltk.tokenize import word_tokenize  # nltk: 자연어 처리 패키지, 단어 토큰화
from nltk.corpus import stopwords  # 불용어
from nltk.stem import WordNetLemmatizer  # 단어 형태 일반화를 위한 표제어 추출
from collections import Counter  # 데이터 집합에서 특정 갯수 자동 계산
import matplotlib.pyplot as plt  # 그래프 그리기
from wordcloud import STOPWORDS, WordCloud  # 워드클라우드용 불용어 모듈, 워드클라우드

# 컴퓨터마다 최초 1번 실행, 다운후 주석처리
# import nltk
# nltk.download()

# [1] 여러개의 파일명을 불러오기: glob.glob(): 특정 배열과 필치하는 파일명들을 모두 찾기
all_files = glob.glob('./excel/myCabinetExcelData*.xls')
# *: 와일드카드, 모든 문자 대응
# print(all_files)

# [2] 여러개 파일명에 해당하는 엑셀파일을 호출해서 pd로 변환하기  # 엑셀 파일 -> pd -> df
all_files_data = []
for file in all_files:  # 모든 파일명을 하나씩 반복
    # print(file)
    df = pd.read_excel(file)  # 엑셀 모듈 xlrd 에러 발생 -> 모듈 설치하기
    # print(df)
    all_files_data.append(df)

# print(all_files_data)  # 여러 df 존재

# [3] 데이터프레임 합치기: .concat(여러 데이터프레임이 저장된 리스트, axis='0: 세로방향, 1: 가로방향')
all_files_data_concat = pd.concat(all_files_data, axis=0, ignore_index=True)
# print(all_files_data_concat)

# [4] 데이터프레임을 csv로 변환 및 내보내기
all_files_data_concat.to_csv('./excel/riss_bigdata.xls', encoding="UTF-8", index=False)

# 목표(학술 문서의 제목 분석)을 위한 데이터 전처리
# [5] 데이터프레임의 제목열만 추출
all_title = all_files_data_concat['제목']
# print(all_title)

# [6] 단어 토큰화 준비
# stopwords.words(''): 영어 불용어 목록 가져오는 함수
# WordNetLemmatizer(): 표제어 추출기 객체 생성
# 표제어: 단어의 원형(기본형)을 찾는 과정: running -> run, better -> good, 시제, 단/복수, 진행어 등등을 일반화하는 과정
eng_stopwords = stopwords.words('english')
# print(eng_stopwords)
lemma = WordNetLemmatizer()

# [7] 단어 토큰화
words = []
for title in all_title:  # 제목 목록에서 제목 하나씩 반복
    # print(title)

    # 7-1 영문이 아닌 것을 정규표현식으로 치환
    en_words = re.sub(r'[^a-zA-Z]+', " ", str(title))
    # print(en_words)

    # 7-2 소문자로 변환
    en_words_token = word_tokenize(en_words.lower())  # 지정한 문자열을 토큰화(단어 추출)하여 리스트로 반환
    # print(en_words_token)

    # 7-3 불용어 제거(해당 토큰리스트에 불용어가 포함되어 있으면 제외)
    # 리스트 컴프리헨션 사용 X
    # en_words_token_stop = []  # 불용어가 제거된 토큰 리스트
    # for w in en_words_token:
    #     if w not in eng_stopwords:  # 해당 단어가 불용어목록에 없으면(포함 X이면)
    #         en_words_token_stop.append(w)
    # 리스트 컴프리헨션 사용 O
    en_words_token_stop = [w for w in en_words_token if w not in eng_stopwords]
    #   if 값 in 리스트 :  리스트내 해당 값이 존재하면 true 아니면 false
    #   if 값 not in 리스트 : 리스트내 해당 값이 존재하면 false 아니면 true

    # 7-4 표제어 추출: lemma.lemmatize( 단어 ) # 단어에서 시제, 단/복수, 진행형 등을 일반화된 단어로 추출
    # 리스트 컴프리헨션 사용 O
    # en_words_token_stop_lemma = [lemma.lemmatize(w) for w in en_words_token_stop]
    # 리스트 컴프리헨션 사용 X
    en_words_token_stop_lemma = []
    for w in en_words_token_stop:  # 불용어가 제거된 리스트(en_words_token_stop) 에서 표제어 추출
        en_words_token_stop_lemma.append(lemma.lemmatize(w))

    # print(en_words_token_stop_lemma)
    # 제목을 정규화->토큰화->불용어제거->표제어추출 한 결과를 리스트에 담기
    words.append(en_words_token_stop_lemma)

# 반복문 종료
print(words)
# [8] 2차원 리스트를 1차원으로 변환  # reduce
# reduce 사용
words2 = reduce(lambda x, y: x + y, words)

# 매개변수의 제곱을 하는 함수를 람다식으로 표현
# 제곱함수 = lambda x : x**2     # JS  x => x**2   # JAVA x -> x**2
# print(제곱함수(1))  # 1
# print(제곱함수(2))  # 4
# 람다식이 아닌 일반 함수
# def 제곱함수2(x) :
#     return x ** 2
# print(제곱함수2(2))  # 4

# reduce 사용 X
# words2 = []
# for w in words :
#     words2.extend(w) # 리스트1.extend(리스트2): .extend() 두 리스트를 하나의 리스트로 반환하는 함수
# print(words2)

# [9] 리스트 내 요소 개수 세기(단어 빈도 구하기)
count = Counter(words2)
print(count.most_common(50))  # Counter({단어: 수}, {단어: 수}, ...)

# [10] 빈도가 높은 것만 추출, 상위 50개
word_count = dict()
# for e in count.most_common(50):
#     print(e)  # ('단어', 수)
for (tag, counts) in count.most_common(50):
    # print(tag)
    # print(counts)
    if len(tag) > 1:  # 단어 길이가 1 초과하면
        word_count[tag] = counts  # 단어를 key, 빈도수를 value로 하는 딕셔너리 쌍으로 저장
print(word_count)

# [11] 히스토그램
# plt.bar(x축값, y축값)
# dict.keys(): 딕셔너리 내 모든 key 값 호출 및 반환, dict.values(): 모든 value값 호출 및 반환
# 함수 호출시 소괄호 차이: function(): 함수를 실행한 후 값을 전달, function: 함수를 참조하도록 함
sorted_keys = sorted(word_count, key=word_count.get, reverse=True)
print(sorted_keys)
sorted_values = sorted(word_count.values(), reverse=True)
print(sorted_values)
plt.bar(range(len(word_count)), sorted_values, align="center")
plt.xticks(range(len(word_count)), list(sorted_keys), rotation=85)
plt.show()

# [12] 연도별 학술문서 수
all_files_data_concat['doc_count'] = 0  # DataFrame 필드(열) 추가
# 출판일 별로 'doc_count'의 기술통계
summary_year = all_files_data_concat.groupby('출판일', as_index=False)['doc_count'].count()
# 데이터프레임에서 '출판일' 열 기준으로 그룹화
# as_index = False: 그룹화시 인덱스 제외
# .count(): 행 개수
print(summary_year)

plt.figure(figsize=(12, 5))
plt.xlabel("year")
plt.ylabel('doc-count')
plt.grid(True)
plt.plot(range(len(summary_year)), summary_year['doc_count'])
plt.xticks(range(len(summary_year)), [text for text in summary_year['출판일']])
plt.show()

# [13] 워드클라우드
# 1) 문자열 타입 텍스트들의 워드클라우드
stopwords = set(STOPWORDS)
wc = WordCloud(background_color='ivory', stopwords=stopwords, width=800, height=600)
# 2) 딕셔너리타입 텍스트들의 워드클라우드
cloud = wc.generate_from_frequencies(word_count)
plt.figure(figsize=(8, 8))
plt.imshow(cloud)
plt.axis("off")
plt.show()

# 3) 워드클라우드 결과를 이미지로 저장하가
wc.to_file("wordcloud.jpg")
