# day17 > 3_영문분석.py
# 한국학술연구학술정보원(https://www.riss.kr)에서 "Artificial Intelligence" 검색, 해외학술논문, 영어, 500건
# 'Artificial'과 'Intelligence'를 제외한 학술논문의 제목 텍스트 빈도수 분석해서 시각화

# [1] import
import glob
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from collections import Counter
from functools import reduce
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# [2] csv에서 읽기 / 엑셀 파일들에서 DataFrame들을 읽어와서 하나로 합치기 및 CSV 생성
try:
    df = pd.read_csv("./excel/AI.xls", encoding="UTF-8")
except FileNotFoundError:
    excel_list = glob.glob('./excel/exportExcelData*.xls')
    # print(excel_list)
    df_list = []
    for path in excel_list:
        df = pd.read_excel(path)
        df_list.append(df)
    # print(df_list)
    df = pd.concat(df_list, axis=0, ignore_index=True)
    df = df.drop(columns=['Unnamed: 0'])
    df.to_csv("./excel/AI.xls", encoding="UTF-8", index=False)

# [3] 제목 빈도수 분석

# 1. 제목 칼럼 추출
titles = df['제목']
# print(title)

# 2. 정규화 > 토큰화 > 불용어제거 > 표제어추출
en_stopwords = stopwords.words('english')
lemma = WordNetLemmatizer()
words = []
for title in titles:
    # 2-1. re.sub('정규식', '치환문자', '데이터'): 정규식 대입으로 영문자만 추출
    title_re = re.sub(r'[^a-zA-Z]+', " ", str(title))
    # print(title_re)
    # 2-2. str.lower() + word_tokenize(): 소문자로 변환 후 토큰화(단어 추출)
    title_re_token = word_tokenize(title_re.lower())
    # print(title_re_token)
    # 2-3. 불용어 제거
    title_re_token_stop = [word for word in title_re_token if word not in en_stopwords]
    # print(title_re_token_stop)
    # 2-4. 표제어 추출  # 단어에서 시제, 단/복수, 진행형 등을 일반화된 단어로 추출
    title_re_token_stop_lemma = [lemma.lemmatize(word) for word in title_re_token_stop]
    # print(title_re_token_stop_lemma)
    # 2-5. words 리스트에 추출된 단어들 추가
    words.append(title_re_token_stop_lemma)
# print(words)

# 3. words 리스트 1차원으로 변환
words_flat = reduce(lambda x, y: x + y, words)
# print(words_flat)

# 4. 빈도수 계산
word_count = Counter(words_flat)
# print(word_count.most_common(50))
word_count_dict = {}
for key, value in word_count.most_common(50):
    word_count_dict[key] = value
# print(word_count_dict)

# [3] 히스토그램
word_count_dict.pop('artificial')
word_count_dict.pop('intelligence')
plt.figure(figsize=(12, 6))  # 12 inches wide, 6 inches tall
plt.bar(range(len(word_count_dict.keys())), list(word_count_dict.values()))
plt.xticks(range(len(word_count_dict.keys())), list(word_count_dict.keys()), rotation=90)
# plt.show()

# [4] 출판일 별로 통계
year = df['출판일']
# print(year)
year_count = Counter(year)

year_count_dict = dict(year_count)
# print(year_count_dict)
year_count_dict_sorted = dict(sorted(year_count_dict.items()))
print(year_count_dict_sorted)

plt.figure(figsize=(12, 6))
plt.plot(list(year_count_dict_sorted.keys()), list(year_count_dict_sorted.values()))
plt.grid(True)
plt.show()

# [5] 워드클라우드
stopwords = set(STOPWORDS)
wc = WordCloud(background_color="white", stopwords=stopwords, width=1200, height=800)
cloud = wc.generate_from_frequencies(word_count_dict)
plt.figure(figsize=(12, 8))
plt.imshow(cloud)
plt.axis("off")
plt.show()