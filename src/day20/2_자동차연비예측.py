# day20 > 2_자동차연비예측.py
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
# [1] 데이터 준비
# 1. CSV 파일에서 데이터 읽기
df = pd.read_csv('auto_mpg.csv')
# print(df)
# 2. 쓰지 않을 데이터열 .drop()
df.drop(['car_name', 'origin', 'horsepower'], axis=1, inplace=True)
print(df.shape)
print(df.info())
'''
RangeIndex: 398 entries, 0 to 397
Data columns (total 6 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   mpg           398 non-null    float64
 1   cylinders     398 non-null    int64  
 2   displacement  398 non-null    float64
 3   weight        398 non-null    int64  
 4   acceleration  398 non-null    float64
 5   model_year    398 non-null    int64  
dtypes: float64(3), int64(3)
memory usage: 18.8 KB
None
'''

# [2] 선형 회귀 모델
# 독립 변수와 종속 변수 분리
y = df['mpg']
x = df.drop(['mpg'], axis=1, inplace=False)
# 훈련용, 테스트용 데이터 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
# 선형 회귀 분석 모델
lr = LinearRegression()
# 선형 회귀 분석 모델 훈련
lr.fit(x_train, y_train)
# 테스트 데이터에 대한 예측 수행: y_predict
y_predict = lr.predict(x_test)

# [3] 훈련된 선형 회귀 분석 모델 평가
mse = mean_squared_error(y_test, y_predict)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_predict)
print(f"MSE: {mse:.2f}, RMSE: {rmse:.2f}, R^2: {r2:.2f}")
print(f"y 절편: {np.round(lr.intercept_, 2)}, 회귀계수: {np.round(lr.coef_, 2)}")
coef = pd.Series(data=np.round(lr.coef_, 2), index=x.columns)
coef.sort_values(ascending=False)
print(coef)

# [4] 결과 시각화
fig, axs = plt.subplots(figsize=(16, 16), ncols=3, nrows=2)
x_features = ['model_year', 'acceleration', 'displacement', 'weight', 'cylinders']
# 그래프 색상
plot_color = ['r', 'b', 'y', 'g', 'r']
for i, feature in enumerate(x_features):
    row, col = i // 3, i % 3
    sns.regplot(x=feature, y='mpg', data=df, ax=axs[row][col], color=plot_color[i])
plt.show()

# [5] 완성된 연비 예측 모델 사용
print("연비를 예측할 차의 정보를 입력해 주세요.")
cylinders_1 = float(input("cylinders: "))
displacement_1 = float(input("displacement: "))
weight_1 = float(input("weight: "))
acceleration_1 = float(input("acceleration: "))
model_year_1 = int(input("model_year(연식): "))
# lr.predict()는 2차원 배열을 입력받으므로 2차원 리스트 형식으로 입력 (여러 데이터를 입력받음 -> 한 데이터마다 독립 변수 값이 여러 개 있음)
predict_mpg = lr.predict([[cylinders_1, displacement_1, weight_1, acceleration_1, model_year_1]])
print(f"이 차량의 예상 연비는 {predict_mpg[0]:.2f} MPG 입니다.")

# + 결론 및 제언, 한계점
