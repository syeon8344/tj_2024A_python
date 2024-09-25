# day23 > 2_결정트리.py
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
# [1] 데이터 수집
# 어종 데이터셋: https://raw.githubusercontent.com/rickiepark/hg-mldl/master/fish.csv
# Species: 어종명, Weight: 무게, Length: 길이, Diagonal: 대각선길이, Height: 높이, Width: 너비
# 어종명을 결정트리로 예측하기
df_fish = pd.read_csv("fish.csv")
# print(df_fish)

# [2] 훈련 7: 테스트 3으로 데이터 분리
x = df_fish.drop(["Species"], axis="columns", inplace=False)
# print(x)
y = df_fish["Species"]
labels = ["Perch", "Bream", "Roach", "Pike", "Smelt", "Parkki", "Whitefish"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=777)

# [3] 결정 트리 모델에 훈련 데이터 피팅
tree_model = tree.DecisionTreeClassifier(random_state=777)
tree_model.fit(x_train, y_train)
y_predict = tree_model.predict(x_test)

# [4] 훈련된 모델 기반으로 테스트 데이터 예측, 정확도 확인
# e.g. 개선 전 결정트리모델 정확도: 0.625
accuracy = accuracy_score(y_test, y_predict)
print(f"개선 전 결정트리모델 정확도: {accuracy:.3f}")  # 개선 전 결정트리모델 정확도: 0.812

# [5] 최적 하이퍼 파라미터 찾기
# params = {"max_depth": [2, 6, 10, 14], "min_samples_split": [2, 4, 6, 8]}
# e.g. 평균 정확도: ... , 최적 하이퍼 파라미터: { "max_depth": .. , "min_samples_split": ...}
params = {"max_depth": [2, 6, 10, 14], "min_samples_split": [2, 4, 6, 8]}
grid_cv = GridSearchCV(tree_model, param_grid=params, scoring="accuracy", cv=5, return_train_score=True)
grid_cv.fit(x_train, y_train)
print(f"최고 평균 정확도: {grid_cv.best_score_:.3f}, 최적 하이퍼 파라미터: {grid_cv.best_params_}")  # 14, 2

# [6] 최적의 하이퍼 파라미터 기반으로 모델 개선 후 테스트용 데이터 예측하고 예측 정확도 확인하기 (시각화 포함)
# e.g. 개선 후 결정트리모델 정확도: ...
tree_model_best = tree.DecisionTreeClassifier(max_depth=14, min_samples_split=2, random_state=777)
tree_model_best.fit(x_train, y_train)
y_predict_best = tree_model_best.predict(x_test)
accuracy_best = accuracy_score(y_test, y_predict_best)
print(f"개선 후 결정트리모델 정확도: {accuracy_best:.3f}")
# 차트 시각화
plt.figure(figsize=(10, 8))
tree.plot_tree(tree_model_best, feature_names=x.columns, class_names=labels)
plt.show()

