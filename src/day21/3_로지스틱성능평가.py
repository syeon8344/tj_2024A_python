# day21 > 3_로지스틱성능평가.py
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# 실제 시험 합격 목록
y_true = [1, 1, 0, 1, 0, 0, 1, 0, 1, 0]
# 예측 시험 합격 목록
y_pred = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1]

"""
    오차 행렬
        - 실제 클래스(값): 행
        - 예측 클래스(값): 열
        - True Positive: 참을 참으로 예측
        - False Positive: 거짓을 참으로 예측
        - True Negative: 거짓을 거짓으로 예측
        - False Negative: 참을 거짓으로 예측
        [[3 2]    [[TN, FP]
         [1 4]]    [FN, TP]]
         
    로지스틱 분석 평가 지표
        - 정밀도: TP/(FP+TP), 참으로 예측한 값들 중의 진짜 참값 비율
        - 재현율: TP/(FN+TP), 진짜 참값들 중에서 참으로 예측된 비율
        - F1 Score: 2*(정밀도*재현율)/(정밀도+재현율), 정밀도와 재현율의 조화평균으로 서로간의 균형 측정
"""
# [1] 오차 행렬
print(confusion_matrix(y_true, y_pred))
# [2] 정밀도 함수
print(precision_score(y_true, y_pred))  # [4/2+4] = 0.67
# [3] 재현율 함수
print(recall_score(y_true, y_pred))  # [4/1+4] = 0.8
# [4] F1 점수
print(f1_score(y_true, y_pred))  # [2*0.67*0.8 / (0.67+0.8)] = 0.73
# [5] AUC (Area Under the Curve)
print(roc_auc_score(y_true, y_pred))  # 0.70,  1에 가까울수록 성능이 좋다.

