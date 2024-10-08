# day27 > 2_단순신경망.py
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# 1. 임의 데이터
x = np.arange(1, 6)
print(x)  # [1 2 3 4 5]
y = 3 * x + 2
print(y)  # [5 8 11 14 17]
# 2. 시각화
plt.plot(x, y)
# plt.show()
# 3. Sequential API 모델: 여러 층을 이어붙이듯 시퀀스에 맞게 일렬로 연결 (입력층 -> 출력층)
# 순서대로 각 층/레이어를 하나씩 통과하며 딥러닝 연산 수행
# (1) 방법 1: 리스트형
# model = tf.keras.Sequential([층1, 층2, 층3])
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10),  # 레이어 1
    tf.keras.layers.Dense(5),  # 레이어 2
    tf.keras.layers.Dense(1)  # 레이어 3
])  # Dense 레이어 3개를 갖는 모델 생성
# (2) 방법 2: add 함수
model = tf.keras.models.Sequential()  # 빈 레이어를 가진 객체 생성
model.add(tf.keras.layers.Dense(10))  # 레이어 1 추가
model.add(tf.keras.layers.Dense(5))  # 레이어 2 추가
model.add(tf.keras.layers.Dense(1))  # 레이어 3 추가
# 레이어의 개수는 제한 없음
# (3) 입력 데이터의 형태
model = tf.keras.models.Sequential([
    # 데이터셋이 (150, 4)인 경우 데이터 150개, 각 데이터마다 변수가 4개
    tf.keras.layers.Dense(1, input_shape=[4]),  # 레이어 1
    tf.keras.layers.Dense(5),  # 레이어 2
    tf.keras.layers.Dense(1)  # 레이어 3
])  # Dense 레이어 3개를 갖는 모델 생성
# (4) 단순선형회귀모델 정의: y = wx + b에서 데이터는 x값 입력변수 1개만 존재하므로 input_shape[1]
# 1개의 노드(뉴런)을 갖는 레이어는 1개의 출력값을 가지므로 출력값은 y에 대한 모델의 예측값
# [1] 모델 생성
model = tf.keras.models.Sequential([tf.keras.layers.Dense(1, input_shape=[1])])
print(model.summary())  # b(y절편)은 기본값으로 추가된다
"""
 Total params: 2 (8.00 B)  # 모델 내부의 총 파라미터 수
 Trainable params: 2 (8.00 B)  # 모델의 업데이트할 파라미터 수 (w 가중치, b 편향)
 Non-trainable params: 0 (0.00 B)  # 업데이트하지 않을 파라미터 수
"""
# [2] 모델 컴파일
# 1. 긴 문자열 지정
model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['mean_squared_error', 'mean_absolute_error'])
# 2. 짧은 문자열 지정
model.compile(optimizer='sgd', loss='mse', metrics=['mse', 'mae'])
# 3. 클래스 인스턴스 지정
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.005),
              loss=tf.keras.losses.MeanSquaredError(),
              metrics=[tf.keras.metrics.MeanSquaredError(), tf.keras.metrics.MeanAbsoluteError()])
# 단순선형회귀모델의 컴파일
model.compile(optimizer='sgd', loss='mse', metrics=['mse', 'mae'])
# [3] 모델 훈련
history = model.fit(x, y, epochs=1200)  # x(독립변수)와 y(종속변수)를 epochs번 학습, loss: 오차, mae: 평가지표 절대오차평균
# [4] 시각화
# history.history: epoch별 훈련 손실과 평가지표가 딕셔너리 형태로 저장되어 있다 {'loss': [], 'mae': [], 'mse': []}
plt.plot(history.history['loss'])
plt.plot(history.history['mae'])
plt.show()
# [5] 모델 검증
print(model.evaluate(x, y))
# [6] 모델 예측
print(model.predict(np.array([10])))
