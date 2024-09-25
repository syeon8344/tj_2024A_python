# day24 > 1_군집분석.py
"""
    비지도 학습: 타깃(종속)값이 없는 상태에서 학습 수행, <---> 지도 학습: 회귀분석, 분류분석
    - 군집분석: 데이터포인트(군집)을 사전에 정의된 군집개수(K)로 그룹화해서 새로운 데이터의 그룹 예측
        - 특징: 1. 비지도학습, 2. 사전에 클러스터수(K)정의, 3. K 평균 알고리즘
        - 군집화: 학습을 수행하여 데이터 간의 관계를 분석하고 유사한 데이터들을 군집으로 구성
        - 최적의 클러스터 수(K) 찾기: 1. 엘보 방법, 2. 실루엣 방법
"""
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler  # 표준화 함수

# [1] 데이터 수집 (종속변수 없음)
# weight: 과일 무게, sweetness: 과일 당도
data = {
    'weight': [110, 160, 130, 320, 370, 300, 55, 65, 60, 210, 220, 200, 90, 80, 100, 190, 180, 170, 100, 90,
               140, 280, 320, 130, 200, 140, 250, 150, 70, 80, 200, 300, 220, 140, 180, 230, 220, 250],
    'sweetness': [6.2, 7.2, 6.8, 8.1, 8.6, 8.1, 5.2, 5.7, 6.1, 7.2, 7.6, 6.7, 7.3, 6.9, 7.3, 7.5, 7.4, 7.3, 7.0, 6.8,
                  6.9, 8.0, 8.1, 6.7, 7.0, 6.6, 7.8, 7.1, 6.7, 6.5, 7.0, 7.6, 7.3, 7.0, 7.2, 7.5, 7.4, 7.7]
}

df = pd.DataFrame(data)

# [2] k-평균 군집 분석 모델 # KMeans
model = KMeans()  # 군집분석 모델 객체 생성, n_clusters=군집 갯수
model.fit(df)  # 데이터 피팅/비지도학습이므로 종속변수가 없다

# [3] 클러스터/군집/중심지 확인 # .cluster_centers_
print(model.cluster_centers_)
"""
리스트 8개: 군집 8개, 각 군집들의 평균 무게와 당도
    [0] 무게       [1] 당도
[[ 81.81818182   6.51818182]
 [320.           8.1       ]
 [210.           7.17142857]
 [141.42857143   6.9       ]
 [293.33333333   7.9       ]
 [370.           8.6       ]
 [243.33333333   7.66666667]
 [180.           7.35      ]]
"""
# [4] 군집 결과 확인 # .labels_
print(model.labels_)

# [5] 결과를 데이터프레임에 추가
df["cluster"] = model.labels_
print(df)  # 무게와 당도에 따른 군집(번호) 확인

# [6] 새로운 데이터로 군집 예측
new_df = pd.DataFrame({'weight': [240], 'sweetness': [7.5]})   # 새로운 과일 하나의 무게와 당도
print(new_df)

# [7] 예측
c_pred = model.predict(new_df)
print(c_pred)  # [0]

# 시각화
plt.scatter(df["weight"], df["sweetness"], c=df["cluster"], marker="o")  # 산점도
plt.scatter(new_df["weight"], new_df["sweetness"], marker="^")
plt.show()

# 개선방안 1: 무게와 당도의 범위가 크다(스케일 차이가 크다: 무게 100단위, 당도 1단위)
# - 데이터 분석에서 스케일 차이가 크면 특정 속성의 비중이 커진다
# - 스케일 표준화: 알고리즘에서 성능을 개선하여 좀 더 좋은 학습을 위해 필요 -> StandardScaler
# [1] 스케일러 객체 생성
st_scaler = StandardScaler()
# 무게와 당도의 스케일 맞추기: 데이터 표준화
# 데이터 표준화: 평균을 0으로 하고 표준편차를 1이 되도록 변환하는 과정(스케일 차이, 100 무게 vs 1 당도)
# 큰 표준편차: 데이터가 평균으로부터 멀리 있다, 데이터가 매우 다양하다
# 작은 표준편차: 데이터가 평균에 가깝다. 데이터가 비슷비슷하다
scaled_data = st_scaler.fit_transform(df[["weight", "sweetness"]])
print(data)
print(scaled_data)
# [2] 스케일된 데이터로 모델 학습
model_st = KMeans(n_clusters=3)
model_st.fit(scaled_data)  # 스케일 된 데이터 학습
df["cluster"] = model_st.labels_  # 클러스터 결과를 데이터프레임에 저장
df["weight"] = scaled_data[:, 0]  # 첫번째 열의 모든 행 추출(스케일된 후 무게)
df["sweetness"] = scaled_data[:, 1]  # 두번째 열의 모든 행 (스케일된 후 당도)
# [3] 새로운 데이터 예측
new_data_scaled = st_scaler.fit_transform(new_df[["weight", "sweetness"]])  # 새로운 데이터를 스케일
c_pred_2 = model_st.predict(scaled_data)
# 시각화
plt.scatter(df["weight"], df["sweetness"], c=df["cluster"], marker="o")  # 산점도
plt.scatter(new_data_scaled[:, 0], new_data_scaled[:, 1], marker="^")
plt.show()

# 개선방안 2: 최적의 K(클러스터수) 찾기 (엘보 방법)
# 그래프에서 SSE(왜곡)가 급격히 줄어드는 지점을 찾아 그 값을 k로 사용
errors = [] # 오차들 저장하는 리스트
for k in range(1, 11):  # 클러스터수 k 1~10까지 테스트 (10회 반복)
    model = KMeans(n_clusters=k)
    model.fit(scaled_data)
    print(model.inertia_)  # 데이터들의 거리 차이의 제곱값 합: 총 제곱 오차 (SSE)를 계산하고 반환
    errors.append(model.inertia_)  # SSE를 errors 리스트에 저장
# 클러스터 1~10개까지의 SSE가 저장된 errors 리스트
print(errors)
# 오차 시각화
plt.plot(errors, marker="o")  # 선 차트, 데이터포인트 표시
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()

# 그래프 확인 후 최적의 K를 이용한 재모델링
model_3 = KMeans(n_clusters=2)
model_3.fit(scaled_data)  # 스케일된 데이터로 모델 학습



