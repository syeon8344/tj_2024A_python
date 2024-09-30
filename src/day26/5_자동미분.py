# day26 > 5_자동미분.py  # 45p
"""
    함수(function)
        어떤 집합의 각 원소를 다른 어떤 집합의 유일한 원소에 대응시키는 이항 관계
        *프로그래밍의 함수: 어떠한 코드 집합에 매개변수 N개를 대입하고 결과변수 하나를 받는 구조
        x = 3 -> [3x+4] -> y = 13
    기울기: 기울기 정도, 계산식: y증가량/x증가량 e.g. (1,1) -> (5, 3): (y1-y0)/(x1-x0) = 2/4 = 0.5
    미분(differentiation): 미세한 부분(차이)
        실제 y와 예측 y -> 평균제곱오차, 딥러닝: 더 깊게, 복잡하게 계산
    일차 방정식 구하기
        기울기 m, 지나는 점 (a,b), (x,y)
        m = (y-b)/(x-a) -> (x-a)m = y-b -> y = m(x-a) + b
        -> 기울기 3, 점 (1,2)의 경우 y = 3(x-1) + 2
    일차 방정식: y = ax + b
        b(y절편): y절편 = x가 0일 때 y의 값 <---> x절편: y값이 0일 때 x의 값
        Y = 3X - 2
            X = 0, Y = -2, X = 1, Y = 1
"""
import tensorflow as tf  # 1. 텐서플로 모듈

# 2. 선형 관계를 갖는 데이터 샘플
# 텐서플로의 랜덤 숫자 생성객체
g = tf.random.Generator.from_seed(2024)  # 2024: 시드, 랜덤생성시 사용되는 제어용 정수값
# 객체 g에서 정규분포 난수 10개를 벡터(리스트) 형태로 x에 할당
# .normal(shape=(축1, 축2, ..))
x = g.normal(shape=(10,))  # x: 독립 변수/피처
y = 3 * x - 2  # y: 종속 변수/타겟
print("X: ", x.numpy())  # [ 0.9029707 0.08384313 -0.43693087 -0.28045923 -0.922128 -0.20875743 ... ]
print("Y: ", y.numpy())  # [ 0.7089119 -1.7484705 -3.3107924 -2.8413777 ... ]


# 3. Loss 함수 정의: 손실 함수 (평균 제곱 오차 MSE)를 정의하는 함수
def calc_mse(x, y, a, b):
    y_pred = a * x + b  # y예측값 = 계수(기울기)a * x(독립변수/피처) + 상수항(y절편)
    sq_error = (y_pred-y) ** 2  # 예측 y와 실제 y 차이의 제곱 = 오차제곱
    mean_sq_error = tf.reduce_mean(sq_error)
    # print(mean_sq_error)
    return mean_sq_error


# 4. 자동 미분 과정을 기록
# a와 b를 미세하게 변경하기를 반복하며 계산하여 손실을 최소화하는 것이 목적
a = tf.Variable(0.0)  # 계수, 텐서플로 변수에 0으로 초기화
b = tf.Variable(0.0)  # y절편

EPOCHS = 200  # 반복 계산 횟수
for epoch in range(1, EPOCHS + 1):  # 1~200까지 200번 반복
    # 200번 반복하는 동안 a, b를 미세조정하며 MSE가 가장 낮은 값을 찾기
    # 4-1. tf.GradientTape() as 변수: with 안에 있는 계산식들을 기록, 계산된 mse를 tape에 기록
    with tf.GradientTape() as tape:
        mse = calc_mse(x, y, a, b)  # 위에서 정의한 손실함수 게산
    # 4-2. 기울기 계산: tape.gradient()를 이용하여 mse에 대한 a, b의 미분값(기울기)을 구한다
    grad = tape.gradient(mse, {"a": a, "b": b})  # mse에 대한 a, b를 딕셔너리로 반환
    d_a = grad['a']
    d_b = grad['b']

    # 4-3 .assig_sub(): 텐서플로 변수의 매개변수를 원본값에서 뺀 값으로 변수값을 수정
    a.assign_sub(d_a * 0.05)  # 현재값의 5 % 감소
    b.assign_sub(d_b * 0.05)  # 현재값의 5 % 감소

    # 4-4 중간 과정 확인
    if epoch % 20 == 0:  # 매 20 루프마다 epoch 반복횟수, mse 평균제곱오차, a계수, b상수항
        print(f"EPOCH: {epoch}, MSE: {mse:.4f}, a: {a.numpy():.4f}, b: {b.numpy():.4f}")



