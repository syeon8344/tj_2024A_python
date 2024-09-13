# day21 > 2_유방암진단분석.py
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler  # 피처 데이터 정규분포화
from sklearn.linear_model import LogisticRegression  # 로지스틱 회귀 분석 함수
from sklearn.model_selection import train_test_split  # 데이터 훈련/테스트 분할
from sklearn.metrics import confusion_matrix  # 오차 행렬 계산
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score  # 로지스틱 회귀 평가지표

# 유방암 데이터 불러오기
b_cancer = load_breast_cancer()
# print(b_cancer.DESCR)  # load_breast_cancer() 내장 설명서: .DESCR
b_cancer_df = pd.DataFrame(b_cancer.data, columns=b_cancer.feature_names)
b_cancer_df['diagnosis'] = b_cancer.target
# print(b_cancer_df.head())
print('유방암 진단 데이터셋 크기: ', b_cancer_df.shape)
# print(b_cancer_df.info())

# 데이터를 평균이 0이고 분산이 1인 정규분포화: 알고리즘 성능 향상 가능
scaler = StandardScaler()
'''
    데이터의 평균, 표준편차, 원본값
    평균= 50, 표준편차= 10, 원본값= 60
    표준화값= (원본값-평균)/표준편차
    - 데이터 크기가 크게 다를 경우 모델 성능이 저하될 수 있다
    - 주로 이진분류 회귀분석이나 k-평균 군집화 등에서 사용
'''
b_cancer_scaled = scaler.fit_transform(b_cancer.data)
# print(b_cancer.data[0])
"""
[1.799e+01 1.038e+01 1.228e+02 1.001e+03 1.184e-01 2.776e-01 3.001e-01
 1.471e-01 2.419e-01 7.871e-02 1.095e+00 9.053e-01 8.589e+00 1.534e+02
 6.399e-03 4.904e-02 5.373e-02 1.587e-02 3.003e-02 6.193e-03 2.538e+01
 1.733e+01 1.846e+02 2.019e+03 1.622e-01 6.656e-01 7.119e-01 2.654e-01
 4.601e-01 1.189e-01]
"""
# print(b_cancer_scaled[0])  # 정규분포 스케일링 후 데이터
"""
[ 1.09706398 -2.07333501  1.26993369  0.9843749   1.56846633  3.28351467
  2.65287398  2.53247522  2.21751501  2.25574689  2.48973393 -0.56526506
  2.83303087  2.48757756 -0.21400165  1.31686157  0.72402616  0.66081994
  1.14875667  0.90708308  1.88668963 -1.35929347  2.30360062  2.00123749
  1.30768627  2.61666502  2.10952635  2.29607613  2.75062224  1.93701461]
"""
# 독립변수들, 종속변수 설정
y = b_cancer_df['diagnosis']
x = b_cancer_scaled
# 훈련용 데이터와 평가용 데이터 분할
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
# 로지스틱 회귀 모델 객체 생성
lr_b_cancer = LogisticRegression()
# 훈련 데이터로 모델 훈련
lr_b_cancer.fit(x_train, y_train)
# 평가 데이터에 대한 예측 수행 및 예측 결과 y_predict
y_predict = lr_b_cancer.predict(x_test)

# 모델 성능 확인
# 오차 행렬
print(confusion_matrix(y_test, y_predict))
"""
            예측값
    실제값[[ 60   3]   TN FP
           [ 1 107]]   FN TP
"""
# 모델 평가 지수 5가지 계산 방법
accuracy = accuracy_score(y_test, y_predict)  # 정확도: 실제 값을 잘 예측했는가 (TN + TP) / (TN + FP + FN + TP)
precision = precision_score(y_test, y_predict)  # 정밀도: 참으로 예측한 값이 진짜 참인가 TP / (TP + FP)
recall = recall_score(y_test, y_predict)  # 재현율: 실제 값이 참인 것들을 참으로 잘 예측했는가 TP / (TP + FN)
f1 = f1_score(y_test, y_predict)  # F1 score: 정밀도와 재현율의 균형 2 * (precision * recall) / (precision + recall)
auc = roc_auc_score(y_test, y_predict)  # ROC AUC score: FPR이 변할 때 TPR의 변화량 곡선(ROC) 아래의 면적, 1에 가까울수록 정확
print(f'정확도: {accuracy:.4f}, 정밀도: {precision:.4f}, 재현율: {recall:.4f}, F1: {f1:.4f}, ROC_AUC: {auc:.4f}')
"""
    대략 85% 이상이면 신뢰도가 높다고 볼 수 있다.
    정확도: 0.9766, 정밀도: 0.9727, 재현율: 0.9907, F1: 0.9817, ROC_AUC: 0.9716
"""