# day12 > 5_와인통계분석.py
# 목표: 와인 속성을 분석하여 품질 등급을 예측하기
import pandas as pd
# [1] 데이터 수집: winequality-red.csv & winequality-white.csv

# [2] 데이터 준비
# [2-1] csv 파일의 열 구분자를 ;에서 ,로 바꾸기

# read_csv 속성에서 구분자 설정하기: sep="구분자" 기본값은 ","
# header=숫자: 숫자 행을 열 이름으로 지정, 기본값은 0
red_df = pd.read_csv("csv/winequality-red.csv", sep=";", engine="python", header=0)
white_df = pd.read_csv("csv/winequality-white.csv", sep=";", engine="python", header=0)
print(red_df)
print(white_df)
red_df.to_csv("csv/red_wine_quality.csv", mode='w', index=False)
white_df.to_csv("csv/white_wine_quality.csv", mode='w', index=False)

# [2-2] 데이터 병합하기: 레드와인과 화이트와인의 데이터
print(red_df.head())  # .head(): 데이터프레임 위에서부터 5개 행 출력
# 1. 열 추가: 0번째(첫번째) 열에 type 열 이름으로 red 값들을 추가
red_df.insert(0, column='type', value="red")
print(red_df.head())
print(red_df.shape)  # .shape: 행의 갯수와 열의 개수 (1599, 13), .shape[0]: 행 개수, .shape[1]: 열 개수
# 2.
print(white_df.head())
white_df.insert(0, column='type', value="white")
print(white_df.shape)  # (4898, 13)
# 3. 데이터프레임 합치기: pd.concat([Df1, Df2])
wine = pd.concat([red_df, white_df])
print(wine.shape)
# 4. 합친 와인 데이터프레임을 CSV로 저장
wine.to_csv("csv/wine.csv", index=False)

# [3] 데이터 탐색
# 1. 데이터프레임 기본 정보 출력
print(wine.info())
# 2. 기술 통계
wine.columns = wine.columns.str.replace(" ", "_")  # 열 이름의 공백을 _로 치환
print(wine.head())
# 기술 통계 표시: .describe() = count, mean, std표준편차, min, 25%백분율, 50%, 75%, max
print(wine.describe())
print(wine.describe()['quality'])  # 와인의 등급 통계
print(wine.describe()['quality'].round(5).to_list())  # 와인 등급의 통계 계산결과 리스트

print(wine['quality'].unique())  # [5 6 7 4 8 3 9]
print(wine.quality.unique())  # [5 6 7 4 8 3 9]  -> 레이블명에 특수문자가 있으면 대괄호 + 따옴표 버전 사용 필요.
print(sorted(wine.quality.unique()))  # 와인 등급의 중복값 제거 후 정렬 [3 4 5 6 7 8 9]

print(wine['quality'].value_counts())  # 특정 열 기준으로 count한 결과를 Series로 반환
print(wine.quality.value_counts().to_json())  # {"6":2836,"5":2138,"7":1079,"4":216,"8":193,"3":30,"9":5}, 등급 점수: 갯수
# [4] 데이터 모델링
# 1. .groupby('기준 그릅 열이름')['속성명']
# type 속성으로 그룹해  quality 속성의 기술 통계 구하기
print(wine.groupby('type')['quality'].describe())
# 2. type 속성으로 그룹해서  quality 속성의 평균
print(wine.groupby('type')['quality'].mean())
# 2. type 속성으로 그룹해서  quality 속성의의 표준편차
print(wine.groupby('type')['quality'].std())
# 2. type 속성으로 그룹해서  quality 평균, 표준편차
print(wine.groupby('type')['quality'].agg(['mean', 'std']))
