# day28 > 1_심층신경망.py  # p73
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 케라스 내장 데이터셋에서 mnist(손글씨 이미지) 데이터셋 로드
mnist = tf.keras.datasets.mnist
print(mnist)
# 데이터셋을 훈련용과 테스트용으로 구분
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape, y_train.shape)  # (60000, 28, 28) (60000,) -> (데이터 수, 세로픽셀, 가로픽셀)
print(x_test.shape, y_test.shape)  # (10000, 28, 28) (10000,) -> 정사각형 28픽셀 이미지들, y는 1차원 벡터 형태
# 시각화
fig, axes = plt.subplots(3, 5)
fig.set_size_inches(8, 5)
image_no = 0
for i in range(3):  # 또는 ax = axes[i//5, i%5] -> [5로 나눈 몫(행), 5로 나눈 나머지(열)]
    for j in range(5):
        axes[i][j].imshow(x_train[image_no], cmap='grey')  # imgshow(): 이미지를 차트에 출력
        axes[i][j].set_title(str(y_train[image_no]))  # 정답을 제목으로
        axes[i][j].axis('off')  # 축 표시 끄기
        image_no += 1
plt.tight_layout()
# plt.show()
# 데이터 전처리
print(x_train[0, 10:15, 10:15])  # [이미지 번호, 세로 특정 픽셀, 가로 특정 픽셀]
'''
[[  1 154 253  90   0]
 [  0 139 253 190   2]
 [  0  11 190 253  70]
 [  0   0  35 241 225]
 [  0   0   0  81 240]]
'''
# 0 ~ 255에서 0 ~ 1 사이 값을 가지도록 값 범위 정규화
print(x_train.min(), x_train.max())  # min(): 최솟값, 0, max(): 최댓값, 255
# 데이터 정규화
x_train = x_train / x_train.max()  # 값/최댓값 == /255
x_test = x_test / x_test.max()  # 테스트용 데이터도 변환
print(x_train.min(), x_train.max())  # min(): 최솟값, 0, max(): 최댓값, 255
print(x_train[0, :, :])  # "5" 손글씨 정규화 후 출력

# Dense 레이어에는 1차원 배열만 들어갈 수 있으므로 2차원 배열을 1차원으로 변경
print(x_train.shape)  # (60000, 28, 28) 2차원(데이터 수, 세로, 가로)
# 방법 1: 텐서플로 방법
print(x_train.reshape(60000, -1).shape)  # (60000, 784) 1차원(데이터 수, 가로)
# 방법 2. 레이어 플래튼
print(tf.keras.layers.Flatten()(x_train).shape) # (60000, 784)

# 방법 1. 레이어에 활성화 함수 적용: relu 함수
tf.keras.layers.Dense(128, activation="relu")  # 노드 128개, relu 활성화 함수를 적용하는 레이어
# 방법 2.
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128),  # 128개의 노드짜리 레이어 1개
    tf.keras.layers.Activation("relu"),  # relu 활성화 함수
])  # 입력층이 명시된 상태 아니고 1개의 레이어만 정의되면 출력층 -> 출력층이 128개의 노드로 구성된 모델

# 모델 생성
model = tf.keras.Sequential([
    # 2차원(이미지)를 1차원으로 변환: Flatten() 패턴 -> 28** =
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # 입력층
    tf.keras.layers.Dense(256, activation="relu"),  # 은닉층
    tf.keras.layers.Dense(64, activation="relu"),  # 은닉층
    tf.keras.layers.Dense(32, activation="relu"),  # 은닉층
    # 각 레이어들 간의 연결된 완전연결층
    # 각 256, 64, 32개의 노드를 가지는 은닉층 3개
    # 각 relu는 비선형성 활성화 함수 적용
    tf.keras.layers.Dense(10, activation="softmax")  # 출력층, 종속변수 10개, 분류 모델
    # 정답: 0 ~ 9 사이 손글씨 정답, e.g. 0 또는 1 또는 ... 9
])
# 각 레이어(은닉층) 갯수, 각 노드 갯수는 중요한 하이퍼파라미터가 된다.

print(model.summary())
"""
Model: "sequential_1"
┌─────────────────────────────────┬────────────────────────┬───────────────┐
│ Layer (type)                    │ Output Shape           │       Param # │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ flatten_1 (Flatten)             │ (None, 784)            │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_2 (Dense)                 │ (None, 256)            │       200,960 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_3 (Dense)                 │ (None, 64)             │        16,448 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_4 (Dense)                 │ (None, 32)             │         2,080 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_5 (Dense)                 │ (None, 10)             │           330 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 219,818 (858.66 KB)
 Trainable params: 219,818 (858.66 KB)
 Non-trainable params: 0 (0.00 B)
"""
# [3-6] 손실함수
# (1) 이진 분류: 출력 노드가 1개, sigmoid 함수를 사용할 경우
model.compile(loss="binary_crossentropy")

# (2) y가 원핫 벡터인 경우
# y = 5일 때 5를 출력할 때 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]인 경우
model.compile(loss="categorical_crossentropy")

# (3) y가 원핫 벡터가 아닌 경우
model.compile(loss="sparse_categorical_crossentropy")
'''
원핫 벡터/인코딩: one-hot encoding
e.g. 결과가 (0 1 2 3 4)일 경우 출력 형태가 [1, 0, 0, 0, 0], [0, 1, 0, 0, 0] 등으로 1 하나, 나머지 0인 경우
'''
# [3-7] 옵티마이저
# (1) 클래스로 지정하는 방법 (TensorFlow 2부터는 lr 대신 learning_rate= 사용)
adam = tf.keras.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=adam)
# (2) 문자열로 지정하는 방법
model.compile(optimizer="adam")

# [3-8] 평가지표
# (1) 클래스 지정
acc = tf.keras.metrics.SparseCategoricalAccuracy()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=[acc])
# (2) 문자열로 지정
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# [3-9] 훈련
# fit(훈련독립, 훈련종속, epochs=학습반복수, validation_data=[테스트 독립, 테스트 종속])
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
"""
Epoch 10/10
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 4s 2ms/step - accuracy: 0.9951 - loss: 0.0156 - val_accuracy: 0.9823 - val_loss: 0.0780
    1. Epoch 10/10: 현재 에포크
    2. 1875/1875: 현재 진행중인 배치 번호 (총 데이터/총 배치수(32개))
        - 배치: 모델 훈련에서 전체를 구분한 집합 수 (주로 32, 64, 128 사용, 기본값은 32개)
"""

# [3-10] 평가
test_loss, test_acc = model.evaluate(x_test, y_test)
print(test_acc)  # 1에 가까울수록 좋은 성능 (퍼센티지)  0.9794999957084656

# [3-11] 예측
y_predict = model.predict(x_test)
print(y_predict[0])
'''
각 번호마다의 확률
[7.7464787e-13 3.1592888e-11 3.7277174e-11 4.4571431e-09 2.9495945e-10
 3.5251874e-11 3.7223337e-14 1.0000000e+00 1.2977961e-12 4.9240022e-08]
'''
# argmax(): 배열 내 가장 높은 수의 인덱스 == 가장 높은 확률
print(np.argmax(y_predict[0]))  # 7
# 앞에서부터 10개의 예측 값 확인, axis: 차원/축
print(np.argmax(y_predict[:10], axis=1))  # [7 2 1 0 4 1 4 9 5 9]
# 앞에서부터 정답 10개
print(y_test[:10])


# [3-12] 시각화
def get_result(index):
    img = x_test[index]
    y_value = y_test[index]
    y_pred = np.argmax(y_predict[index])
    confidence = 100 * np.max(y_predict[index])
    return img, y_value, y_pred, confidence


# plt 캔버스
fig, axes = plt.subplots(3, 5)
fig.set_size_inches(12, 10)
for i in range(15):
    ax = axes[i // 5, i % 5]
    img, y_true, y_pred, confidence = get_result(i)
    # imshow로 이미지 시각화
    ax.imshow(img.reshape(28, 28), cmap='gray')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"True: {y_true}")
    ax.set_xlabel(f"Prediction: {y_pred}, Confidence: {confidence:.2f}%")
plt.tight_layout()
plt.show()
