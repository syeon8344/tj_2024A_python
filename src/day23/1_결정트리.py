# day22 > 2_센서데이터분석.py
"""
    결정트리: 결정트리(다중분류) vs 로지스틱 회귀(이진분류)
    모델 생성 및 예측
"""
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # 결정 트리 모델
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score  # 정확도 점수 함수
from sklearn.model_selection import GridSearchCV  # 정확도를 검사해서 하이퍼 매개변수 최적화 함수
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz  # graphviz dot확장자 파일 생성
import graphviz

# [1] 데이터 수집
# UCI_HAR_Dataset: UCI 머신러닝 레포에서 human activity recognition using smartphones 다운로드한 자료
# 1. feature_name
# CSV 데이터 구분: 공백으로 구분 -> sep=r'\s+', 헤더 없음: header=None, 열 레이블: names=[]
feature_name_df = pd.read_csv("UCI_HAR_Dataset/features.txt", sep=r"\s+", header=None, names=["index", "feature_name"],engine="python")
# print(feature_name_df.head())
# print(feature_name_df.shape)
# 인덱스 제거하고 독립변수 이름만 리스트에 저장
# iloc[행 슬라이싱, 열 번호]: (아래로, 오른쪽으로) index 기반 row와 column 선택, [:, 1]은 전체 행의 index 1인 (두번째) 열 선택
# 선택된 행 열의 값만(.values) 리스트로 반환(.tolist())
feature_name = feature_name_df.iloc[:, 1].values.tolist()
# print(feature_name[:5])  # ['tBodyAcc-mean()-X', 'tBodyAcc-mean()-Y', 'tBodyAcc-mean()-Z', 'tBodyAcc-std()-X', 'tBodyAcc-std()-Y']
# 2. x y train test 데이터
# delim_whitespace=True: 공백을 구분문자로 쓸 것인지에 대한 여부, 대신 sep=r'\s+' 사용
x_train = pd.read_csv("UCI_HAR_Dataset/train/X_train.txt", sep=r'\s+', header=None, encoding='latin1')
x_train.columns = feature_name  # 피처(열) 이름 대입
x_test = pd.read_csv("UCI_HAR_Dataset/test/X_test.txt", sep=r'\s+', header=None, encoding='latin1')
x_test.columns = feature_name
y_train = pd.read_csv("UCI_HAR_Dataset/train/Y_train.txt", sep=r"\s+", header=None, names=["action"], engine="python")
y_test = pd.read_csv("UCI_HAR_Dataset/test/Y_test.txt", sep=r"\s+", header=None, names=["action"], engine="python")
# print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
# print(x_train.head())
# print(y_train['action'].value_counts())
# 3. 레이블명
label_name_df = pd.read_csv("UCI_HAR_Dataset/activity_labels.txt", sep=r"\s+", header=None, names=["index", "label"],engine="python")
# 데이터프레임객체.iloc[행 슬라이싱]
# 데이터프레임객체.iloc[행 슬라이싱, 열번호]
# feature_name_df.iloc[:]: 모든 행, feature_name_df.iloc[:, 1]: 모든 행의 두번째 열 (첫번째 열 제외)
# .values 열의 모든 값들을 추출, .tolist() 리스트로 반환 함수
label_name = label_name_df.iloc[:, 1].values.tolist()
# print(label_name)
# 데이터 수집 정리
"""
    1. activity_lables.txt: 클래스(종속변수) 값에 따른 분류값
    2. features.txt: 피처(독립변수)값에 따른 필드(열) 이름
    3. 데이터
        1. 훈련용 x_train.txt, y_train.txt
        2. 테스트용 x_test.txt, y_test.txt
    - 변수
        1. x_train: 독립변수 df (훈련용)
        2. y_train: 종속변수 df
        3. x_test: 독립변수 df (테스트용)
        4. y_test: 종속변수 df
        5. label_name: 종속변수 값에 따른 분류값
            1 = WALKING, 2 = W_UPSTAIRS, 3 = W_DOWNSTAIRS, 4 = SITTING, 5 = STANDING, 6 = LAYING
"""
# [2] 분석 모델 구축
# 결정 트리 모델 생성, random_state=랜덤 시드
dt_HAR = DecisionTreeClassifier(random_state=156)
# 결정 트리 모델 훈련
dt_HAR.fit(x_train, y_train)
# 모델 분류 분석: 평가 데이터에 예측한 결과로 y_predict
y_predict = dt_HAR.predict(x_test)

# * (개선된) 결정트리 모델 시각화
better_model = DecisionTreeClassifier(max_depth=8, min_samples_split=16)
better_model.fit(x_train, y_train)
plot_tree(better_model, feature_names=feature_name, class_names=label_name)
plt.show()


# [3] 분석 모델 결과 분석 및 최적의 모델 찾기
accuracy = accuracy_score(y_test, y_predict)  # 모델 예측 정확도, 실제값과 예측값을 비교
print(f"결정 트리 예측 정확도: {accuracy:.4f}")
print(f"결정 트리의 현재 하이퍼 매개변수: {dt_HAR.get_params()}")
# 모델 성능 개선: GridSearchCV
# "max_depth": [6, 8, 10, 12, 16, 20, 24]의 경우 최고 평균 정확도: 0.8513, 최적 하이퍼 매개변수: {'max_depth': 16}
# 최고 평균 정확도: 0.8549, 최적 하이퍼 매개변수: {'max_depth': 8, 'min_samples_split': 16}
# params - depth:트리의 깊이, max_depth:최대 트리의 깊이, criterion:노드 결정 방식
params = {"max_depth": [8, 16, 20], 'min_samples_split': [8, 16, 24]}
grid_cv = GridSearchCV(dt_HAR, param_grid=params, scoring="accuracy", cv=5, return_train_score=True)
"""
    1. GridSearchCV: 하이퍼 매개변수를 받아서 최적의 하이퍼 매개변수를 찾는 API
    2. param_grid: GridSearchCV를 사용하려는 하이퍼 매개변수의 가능한 값
        - max_depth: 트리 최대 깊이, min_sample_split: 노드 분할시 최소 샘플 수
    3. scoring: 평가 지표
    4. cv: 교차 검증(cross-validation) folds
    5. return_train_score: True로 설정하면 훈련 데이터에 대한 성능(mean_train_score)도 반환
"""
grid_cv.fit(x_train, y_train)
cv_results_df = pd.DataFrame(grid_cv.cv_results_)
print(cv_results_df[["param_max_depth", "param_min_samples_split", "mean_test_score", "mean_train_score"]])
print(f"최고 평균 정확도: {grid_cv.best_score_:.4f}, 최적 하이퍼 매개변수: {grid_cv.best_params_}")
# 최적 모델로 테스트 데이터 예측: GridSearchCV 최적 모델은 자동으로 best_estimator_에 저장된다
# 사용처: 다음 모델 생성시 최적 매개변수로 설정해서 생성하기
# e.g. model = DecisionTreeClassifier(max_depth=8, min_samples_split=16)
best_dt_HAR = grid_cv.best_estimator_
best_y_predict = best_dt_HAR.predict(x_test)
best_accuracy = accuracy_score(y_test, best_y_predict)
print(f"best 결정 트리 예측 정확도: {best_accuracy:.4f}")  # 0.8717
# 중요도가 높은 피처 10개를 찾아 그래프로 나타내기
feature_importance_values = best_dt_HAR.feature_importances_
# 독립변수 이름을 인덱스로 하고 중요도 수치를 행으로
feature_importance_values_s = pd.Series(feature_importance_values, index=x_train.columns)
feature_top_10 = feature_importance_values_s.sort_values(ascending=False)[:10]
plt.figure(figsize=(10, 5))
plt.title('Feature importance top 10')
sns.barplot(x=feature_top_10, y=feature_top_10.index)
plt.show()

# GraphViz (별도 설치 필요)
export_graphviz(best_dt_HAR, out_file="tree.dot", class_names=label_name, feature_names=feature_name, impurity=True, filled=True)
# 생성된 tree.dot 파일을 시각화
with open("tree.dot") as f:
    dot_graph = f.read()
graph = graphviz.Source(dot_graph)
graph.view()
