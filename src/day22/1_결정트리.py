# day22 > 1_결정트리.py
"""
    1. 분류분석
        1. 로지스틱 회귀 분석: 이진 분류
        2. 결정트리 분석: 다중 값 분류 - 여러 개의 클래스로 분류
            - 피처: 독립변수
            - 클래스/타겟: 종속변수
    2. 결정트리란
        - 트리 구조 기반으로 의사 결정, 조건은 규칙노드들로 표현하고 최종 리프노드들로 결과 제공
            - 종류
                - 루트 노드: 트리 최상단
                - 내부/규칙 노드: 속성(특징)에 기반해 데이터를 분할하는 기준이 되는 노드
                - 리프 노드: 더 이상 분할되지 않고 최종 결과를 나타내는 노드
            - 노드 선택 기준
                - 엔트로피: 정보 이득 지수(1-엔트로피, 혼잡도가 줄어들어 얻는 이득)가 높은 피처를 분할 기준으로
                    e.g. 과일 주스: 여러 과일이 섞여있으면 혼잡도 높음, 엔트로피가 높다
                    => 불확실성 측정 지표, 값이 낮을수록 분류가 잘 된다
                - 지니 계수: 지니 계수(데이터 순도, 낮을수록 데이터 순도가 높다)가 낮은 피처를 분할 기준으로
                    e.g. 과일 주스: 사과맛만 느껴지면 예측이 쉽고 혼잡도가 낮다, 지니 계수가 낮다
                    => 불순도 측정 지표, 값이 낮을수록 분류가 잘 된다
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # 모델 호출
import matplotlib.pyplot as py
from sklearn import tree
# [1] 데이터 샘플
data = {
    'size': [1, 2, 3, 3, 2, 1, 3, 1, 2, 3, 2, 1, 3, 1, 2],  # 과일의 크기
    'color': [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 1, 2, 2, 3, 3],  # 1: 빨간색, 2: 주황색, 3: 노란색
    'labels': [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 1, 1, 0, 2, 2]  # 0: 사과, 1: 오렌지, 2: 바나나
}
# [2] 데이터프레임 생성
df = pd.DataFrame(data)
print(df)
# [3] 독립변수/피처, 종속변수/클래스/타겟 나누기
x = df[['size', 'color']]
print(x)
y = df['labels']


print(y)
# [4] 결정 트리 모델 생성
model = DecisionTreeClassifier()

# [8] 훈련용, 테스트용 데이터 분할
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# [5] 모델 피팅
model.fit(x_train, y_train)
# [8] 예측
y_pred = model.predict(x_test)
print(y_pred)

# [9] 정확도
from sklearn.metrics import accuracy_score  # 정확도 함수
accuracy = accuracy_score(y_test, y_pred)  # accuracy_score(실제값, 예측값)으로 정확도 확인
print(accuracy)  # 0.6666666666666666

# [6] 확인
print(model.get_depth())  # 4, 트리의 깊이
print(model.get_n_leaves())  # 6, 리프 노드의 개수
# [7] 시각화
import matplotlib.pyplot as plt
tree.plot_tree(model, feature_names=['size', 'color'], class_names=['apple', 'orange', 'banana'])
plt.show()