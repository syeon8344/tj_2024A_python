# day27 > 1_케라스.py  # p50
import numpy as np
import matplotlib.pyplot as plt


def make_linear(w=0.5, b=0.8, size=50, noise=1.0):
    x = np.random.rand(size)  # 0 ~ 1 사이의 난수 size개가 있는 x 배열 선언
    print(x)
    y = w * x + b
    print(y)
    print(y.shape)  # e.g. (100,0)
    # 음수 noise ~ 양수 noise 사이의 난수를 y.shape개 생성
    # 실제 y값에 노이즈(작은 변화)를 주고 확인하는 예제
    noise = np.random.uniform(-abs(noise), abs(noise), size=y.shape)
    print(noise)
    y_noisy = y + noise
    # 시각화
    plt.plot(x, y, c='r')  # y 선 차트
    plt.scatter(x, y_noisy)  # 노이즈 y 산점도
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('y = 0.3x + 0.5')
    plt.show()
    return x, y_noisy


x, y = make_linear(w=0.3, b=0.5, size=100, noise=0.01)

# [2] w(기울기)와 b(y절편)를 학습률(업데이트)하며 손실(오차)를 최소화하는 방법을 찾는 예제
num_epoch = 1000  # 학습 횟수 한도, 1000번
learning_rate = 0.005  # 업데이트 크기/학습률
errors = []  # 에러 기록/손실(오차)을 기록할 리스트

w = np.random.uniform(low=0.0, high=1.0)  # w: 기울기, 0~1 사이 랜덤 값으로 초기화
print(w)
b = np.random.uniform(low=0.0, high=1.0)  # b: y절편, 0~1 사이 랜덤 값으로 초기화
print(b)

for epoch in range(num_epoch):  # 최대 에포크 수만큼 반복
    y_hat = w * x + b  # y예측값, 주어진 x에 따른 최적의 오차를 찾는 w와 b 찾기
    # 오차 계산식: 평균 제곱 오차 계산식
    # 예측값과 실제값 차이를 제곱하여 평균한 값
    error = 0.5*((y_hat - y) ** 2).sum()
    # 오차가 0.005 미만이면 종료
    if error < 0.005:
        break
    # 기울기 미분 계산
    # 1. 기울기 업데이트
    w -= learning_rate * ((y_hat - y) * x).sum()
    # 2. y절편 업데이트
    b -= learning_rate * (y_hat - y).sum()
    # 손실(오차) 기록
    errors.append(error)
    print(f'에포크/학습수: {epoch}, 기울기: {w:.1f}, y절편: {b:.1f}, 오차: {error:.5f}')

# 시각화
plt.plot(errors)
plt.xlabel('epoch')
plt.ylabel('error')
plt.show()
