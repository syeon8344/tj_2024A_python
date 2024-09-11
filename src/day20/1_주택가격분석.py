# day20 > 1_주택가격분석.py

import pandas as pd
# 보스턴 주택 데이터 가져오기: sklearn 1.2 이후 deprecated
# from sklearn.datasets import load_boston
# boston = load_boston()
# print(boston)

# 1.2 이후
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  # 훈련용, 테스트용 데이터 나누기

# [1] 데이터 준비
# 1. 보스턴 주택 가격 가져오기
data_url = "http://lib.stat.cmu.edu/datasets/boston"
# 지정한 URL에서 데이터를 DataFrame으로 가져오기
# sep="\s+": 데이터 간의 공백으로 구분된 csv
# skiprows=22: 위에서부터 22번째 행까지 생략
# header=None: 헤더가 없다
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
# 주택 관련 변수들 (독립변수, 피처/피처변수)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
# 주택 가격 (종속변수, 타깃변수)
target = raw_df.values[1::2, 2]

# print(data.shape)  # (506, 13)
# print(target.shape)  # (506,)
# 2. 독립변수의 이름
feature_names = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"]
# 3. 독립변수 데이터와 독립변수의 이름으로 데이터프레임 생성
df_boston = pd.DataFrame(data, columns=feature_names)
# print(df_boston.head())
# 4. 데이터프레임에 주택가격 열 추가
df_boston["PRICE"] = target
# print(df_boston)
# print(df_boston.info())  # 열 이름, 열 데이터수, 데이터 타입, 메모리
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 506 entries, 0 to 505
Data columns (total 14 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   CRIM     506 non-null    float64
 1   ZN       506 non-null    float64
 2   INDUS    506 non-null    float64
 3   CHAS     506 non-null    float64
 4   NOX      506 non-null    float64
 5   RM       506 non-null    float64
 6   AGE      506 non-null    float64
 7   DIS      506 non-null    float64
 8   RAD      506 non-null    float64
 9   TAX      506 non-null    float64
 10  PTRATIO  506 non-null    float64
 11  B        506 non-null    float64
 12  LSTAT    506 non-null    float64
 13  PRICE    506 non-null    float64
dtypes: float64(14)
memory usage: 55.5 KB
None
'''

# [2] 분석 모델 구축 및 분석
# 1. 타겟과 피처 구분
y = df_boston["PRICE"]  # 종속변수, 타겟
x = df_boston.drop(["PRICE"], axis=1, inplace=False)  # 독립변수, 피처: 주택 가격 제외한 정보
# 2. 훈련용과 평가용 데이터 분할
# 훈련 독립변수, 테스트 독립변수, 훈련 종속변수, 테스트 종속변수 = train_test_split(독립변수, 종속변수, test_size=분할비율, random_state=난수)
# test_size=0.3: 분할 비율, 30%가 테스트 데이터, 70%가 훈련용 데이터, random_state=156: 난수 시드
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=156)
# print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)  # (354, 13) (152, 13) (354,) (152,)

# [3] 선형 회귀 분석 모델 구축
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# 1. 선형 회귀 분석 모델 생성
lr = LinearRegression()
# 2. 선형 회귀 분석 모델 훈련
lr.fit(x_train, y_train)
# print(lr.intercept_, np.round(lr.coef_, 1))  # intercept_: y 절편, coef_: 회귀계수, np.round(숫자, 자릿수): 자릿수에서 반올림
# 3. 테스트 데이터에 대한 예측 수행: 예측 결과 y_predict 구하기
# 테스트 데이터에 있는 주택 정보로 주택 가격 예측
# y_test: 동일한 피처 정보를 가진 실제 주택가격, y_predict: 동일한 피처 정보를 가진 예측된 주택가격
y_predict = lr.predict(x_test)
# 4. MSE, R^2 계산
mse = mean_squared_error(y_test, y_predict)
rmse = np.sqrt(mse)  # RMSE: square root of MSE
print(f"MSE: {mse:.2f}, RMSE: {rmse:1.3f}")  # MSE: 17.30, RMSE: 4.159
print(f"R^2(Variance score): {r2_score(y_test, y_predict):.2f}")  # R^2(Variance score): 0.76

# [3] 결과 시각화: 산점도 + 선형 회귀 그래프
import matplotlib.pyplot as plt
import seaborn as sns  # 회귀분석 관련 차트 구성
# 1. 그래프 칸 설정하기
fig, axs = plt.subplots(figsize=(16, 16), ncols=3, nrows=5)  # 3칸씩 5줄로 구성된 다중 차트
x_features = df_boston.columns[:-1]  # 마지막 y열을 제외한 13개 열
for i, feature in enumerate(x_features):  # enumerate(리스트): 인덱스와 요소값을 따로따로 빼올 수 있다.
    print(f"index: {i}, feature: {feature}")
    row = int(i / 3)  # 몫, 0 0 0 1 1 1 2 2 2
    col = i % 3  # 나머지,   0 1 2 0 1 2 0 1 2
    sns.regplot(x=feature, y="PRICE", data=df_boston, ax=axs[row][col])
plt.show()  # 차트 열기
# y 절편: 독립변수가 0일때 종속변수의 값
# 회귀계수: 독립변수가 1 증가할 때 종속변수의 증감 단위(기울기)
# 신뢰구간: 좁으면 에측이 안정적이고 관계가 명확하다, 넓으면 예측이 불안정하고 관계가 명확하지 않다: 보통 +-5%

