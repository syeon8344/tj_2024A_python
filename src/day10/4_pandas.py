# day10 > 4_pandas.py
# 판다스: 테이블 형태의 자료를 다룰 수 있는 라이브러리
# 1차원 자료: Series시리즈, 2차원 자료: DataFrame데이터프레임, 3차원 자료: Panel패널
# 설치 필요
# 모듈
import pandas as pd  # as: 별칭

print(pd.__version__)  # 2.2.2
print(type(pd))  # <class 'module'>

# [1] Series: 1차원 자료형
data1 = [10, 20, 30, 40, 50]
sr1 = pd.Series(data1)  # Series 객체 생성
print(sr1)
'''
0    10
1    20
2    30
3    40
4    50
dtype: int64
'''
data2 = ['1반', '2반', '3반', '4반', '5반']
sr2 = pd.Series(data2)
print(sr2)
'''
0    1반
1    2반
2    3반
3    4반
4    5반
dtype: object
'''

# [2] Series 직접 생성
sr3 = pd.Series([101, 102, 103, 104, 105])
print(sr3)
sr4 = pd.Series(['월', '화', '수', '목', '금'])
print(sr4)

# [3] Series 인덱스 속성
sr5 = pd.Series(data1, index=[1000, 1001, 1002, 1003, 1004]); print(sr5)
sr6 = pd.Series(data1, index=data2); print(sr6)
sr7 = pd.Series(data2, index=data1); print(sr7)
sr8 = pd.Series(data2, index=sr4); print(sr8)

# [4] 인덱싱
# print(sr8[2])  # 3반, 인덱스 2 -> 3번째 행
# 경고: 인덱싱할 시 인덱스 위치를 직접 쓰지 말고 .iloc[pos]를 사용하시오. -> 정수 입력도 키처럼 처리할 예정
print(sr8.iloc[2])  # 3반
print(sr8['수'])  # 3반
print(sr8.iloc[-1])  # 5반

# [5] 슬라이싱
print(sr8[0:4])  # [0:4]: 0부터 3 인덱스까지 추출, 1~4반 출력

# [6] 인덱스 확인
print(sr8.index)  # 인덱스만 확인
print(sr8.values)  # 값만 확인

# [7] 덧셈 연산: 숫자값 + 숫자값 = 숫자 연산, 문자열 + 문자열 = 문자열 연결
print(sr1 + sr3)  # 111, 122, 133, 144...
print(sr4 + sr2)  # 월1반, 월2반...

# [8] DataFrame: 2차원 자료구조 객체
# 딕셔너리로 생성: 키 = 열, 값 = 행
data_dict = {'year': [2018, 2019, 2020], 'sales': [350, 480, 1099]}
df1 = pd.DataFrame(data_dict)
print(df1)
# 2차원 리스트를 이용한 생성
df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]], index=['중간고사', '기말고사'], columns=data2[0:3])
print(df2)

data_list = [['20201101', 'Hong', '90', '95'], ['20201102', 'Kim', '93', '94'], ['20201103', 'Lee', '87', '97']]
df3 = pd.DataFrame(data_list)
# 열 이름 추가
df3.columns = ['학번', '이름', '중간고사', '기말고사']
# 조회방법
print(df3.head(2))  # 위에서부터 행 2개 조회
print(df3.tail(2))  # 아래서부터 행 2개 조회
print(df3['이름'])  # 열 조회

# DataFrame -> CSV 저장
df3.to_csv("score.csv", encoding='utf-8')
# CSV -> DataFrame으로 불러오기: index_col = 0: 첫번째 열을 DataFrame 인덱스로 사용, encoding = "c": 데이터 파서 엔진, C 또는 Pyt
df4 = pd.read_csv('score.csv', encoding='utf-8', index_col=0, engine="c")
print(df4)
