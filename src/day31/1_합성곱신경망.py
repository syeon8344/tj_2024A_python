# day31 > 1_합성곱신경망.py  # Functional API
"""
딥러닝 프로세스 (절차)
    1. 데이터 수집
    2. 데이터 전처리: 신경망 모델에 적합하도록 수집한 데이터 수정
    3. 데이터 분할: 훈련용/검증용으로 분할, 주로 7:3 또는 8:2
    4. 모델 설계 (구축)
        a. Sequential API 클래스, Functional API 클래스
        b. 레이어 구성: 입력층 ---> 은닉층(Conv2D, MaxPooling2D, Flatten 등) ---> 은닉층 ---> ... ---> 출력층
        c. 활성화 함수: 각 레이어에서 학습된 값을 비선형으로 변환할 때 사용: ReLU, softmax 함수 등 사용
    5. 모델 컴파일: 모델을 어떻게 학습하고 평가할 것인지 설정
        a. 옵티마이저: 모델의 가중치를 업데이트하는 알고리즘, 주로 adam(학습률 기반으로 최적화하는 알고리즘), sgd(확률적 경사 하강법) 사용
        b. 손실함수: 실제값과 예측값의 차이, 분류는 sparse_categorical_crossentropy, 회귀는 mean_squared_error 주로 사용
        c. 평가지표: 모델 성능을 평가하는 지표, 주로 accuracy (in 분류), mse (in 회귀) 등의 지표 사용
    6. 모델 학습 (fitting)
        a. 에포크: 전체 훈련 데이터를 한 번 순회하면 1 에포크
        b. 검증: validation_data 파라미터로 학습 중에 검증/테스트 데이터로 모델 손실 및 평가 확인, validation_data=(x검증, y검증)
    7. 모델 평가 ---> 모델 튜닝 (하이퍼파라미터 수정)
        a. .evaluate(): 최종 성능의 손실함수와 평가지표 결과 확인
        b. 모델 튜닝: 하이퍼파라미터 수정으로 모델 조정
            - 학습률, 배치 크기, 레이어 수, 뉴런(노드) 수, 활성화 함수, 에포크 등의 하이퍼파라미터 수정
    8. 모델 예측
        a. .predict()
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.utils import plot_model

# 1. 데이터셋 준비 (mnist 손글씨)
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_valid, y_valid) = mnist.load_data()

print(x_train.shape, y_train.shape)  # (60000, 28, 28) (60000,)
print(x_valid.shape, y_valid.shape)  # (10000, 28, 28) (10000,)

# 2. 새로운 출력 값 배열: 짝수 0, 홀수 1
y_train_odd = []
for y in y_train:
    if y % 2 == 0:  # 짝수
        y_train_odd.append(0)
    else:  # 홀수
        y_train_odd.append(1)

# 리스트 -> numpy 배열
y_train_odd = np.array(y_train_odd)
print(y_train_odd.shape)  # (60000,)

print(y_train[:10])  # [5 0 4 1 9 2 1 3 1 4]
print(y_train_odd[:10])  # [1 0 0 1 1 0 1 1 1 0]

# Validation 데이터셋도 처리
y_valid_odd = []
for y in y_valid:
    if y % 2 == 0:  # 짝수
        y_valid_odd.append(0)
    else:  # 홀수
        y_valid_odd.append(1)

y_valid_odd = np.array(y_valid_odd)
print(y_valid_odd.shape)  # (10000,)

# 3. 데이터 정규화 (Normalization)
x_train = x_train / 255.0
x_valid = x_valid / 255.0
# 4. 색상 채널 축 추가
x_train_color = x_train[..., tf.newaxis]
x_valid_color = tf.expand_dims(x_valid, -1)

print(x_train_color.shape, x_valid_color.shape)  # (60000, 28, 28, 1) (10000, 28, 28, 1)

# 5. Functional API로 모델 생성: 레이어 객체들을 연결
# 1) 입력 레이어
inputs = tf.keras.layers.Input(shape=(28, 28, 1))
# 2) 합성곱 레이어, 입력 레이어 연결
conv = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(inputs)
# 3) 풀링 레이어, 합성곱 레이어 연결
pool = tf.keras.layers.MaxPooling2D((2, 2))(conv)
# 4) 플래튼 레이어, 풀링 레이어 연결
flat = tf.keras.layers.Flatten()(pool)
# a) 단순 입력 구조
flat_inputs = tf.keras.layers.Flatten()(inputs)
# 5) 2개 입력 구조를 하나로 합치기, 입력 -> 합성곱 -> 풀링 -> 플래튼
concat = tf.keras.layers.Concatenate()([flat, flat_inputs])
# 6) 출력 레이어
outputs = tf.keras.layers.Dense(10, activation='softmax')(concat)
# 7) 모델
model = tf.keras.Model(inputs=inputs, outputs=outputs)

print(model.summary())

# 모델 구조 출력 및 이미지 파일로 저장
plot_model(model, show_shapes=True, show_layer_names=True, to_file='functional_cnn.png')

# 6. 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 7. 모델 훈련
history = model.fit(x_train_color, y_train, epochs=10, validation_data=(x_valid_color, y_valid))

# 8. 모델 평가
val_loss, val_acc = model.evaluate(x_valid_color, y_valid)
print(val_loss, val_acc)

# 다중 출력 분류 모델 (1. 다중 분류[0~9], 2. 이진 분류[0~1])
# 1) 입력 레이어
inputs = tf.keras.layers.Input(shape=(28, 28, 1), name='inputs')
# 2) 합성곱 레이어, 입력 레이어 연결
conv = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', name='conv2d_layer')(inputs)
# 3) 풀링 레이어, 합성곱 레이어 연결
pool = tf.keras.layers.MaxPooling2D((2, 2), name='maxpool_layer')(conv)
# 4) 플래튼 레이어, 풀링 레이어 연결
flat = tf.keras.layers.Flatten(name='flatten_layer')(pool)
# a) 단순 입력 구조
flat_inputs = tf.keras.layers.Flatten()(inputs)
# 5) 2개 입력 구조를 하나로 합치기, 입력 -> 합성곱 -> 풀링 -> 플래튼
concat = tf.keras.layers.Concatenate()([flat, flat_inputs])
# 6-1) 다중 분류 출력 레이어
digit_outputs = tf.keras.layers.Dense(10, activation='softmax', name='digit_dense')(concat)
# 6-2) 이진 출력 레이어
odd_outputs = tf.keras.layers.Dense(1, activation='sigmoid', name='odd_dense')(flat_inputs)
# 7) 모델
model = tf.keras.Model(inputs=inputs, outputs=[digit_outputs, odd_outputs])

print(model.summary())

# 모델 입출력 확인
print(model.inputs)  # [<tf.Tensor 'inputs:0' shape=(None, 28, 28, 1) dtype=float32>]
print(model.outputs)  # [<tf.Tensor 'digit_dense/Softmax:0' shape=(None, 10) dtype=float32>, <tf.Tensor 'odd_dense/Sigmoid:0' shape=(None,) dtype=float32>]

# 모델 구조 출력
plot_model(model, show_shapes=True, show_layer_names=True, to_file='multi_output_cnn.png')

# 모델 컴파일: 다중 출력 손실함수: loss={}
# loss = 1 * sparse..., 0.5 * binary... -> dictionary 형태로 레이어 별 지정
model.compile(optimizer='adam', loss={'digit_dense': 'sparse_categorical_crossentropy', 'odd_dense': 'binary_crossentropy'},
              # 0~9 예측에 더 비중을 두도록 가중치 설정 (0~9 예측 100%, 홀짝 50%), 평가지표도 다중 설정(['accuracy', 'accuracy'])
              loss_weights={'digit_dense': 1, 'odd_dense': 0.5}, metrics=['accuracy', 'accuracy'])

# 모델 훈련: 다중 출력시 훈련용과 검증용이 다중이므로 {'출력레이어명': 출력레이어변수} 딕셔너리 구조로 입력
history = model.fit({'inputs': x_train_color}, {'digit_dense': y_train, 'odd_dense': y_train_odd}, epochs=10,
                    validation_data=({'inputs': x_valid_color}, {'digit_dense': y_valid, 'odd_dense': y_valid_odd}))

# 모델 평가
print(model.evaluate({'inputs': x_valid_color}, {'digit_dense': y_valid, 'odd_dense': y_valid_odd}))


# 샘플 이미지 출력
def plot_image(data, index):
    plt.figure(figsize=(5, 5))
    plt.imshow(data[index])
    plt.axis('off')
    plt.show()


plot_image(x_valid, 0)

# 모델 예측
digit_preds, odd_preds = model.predict(x_valid_color)
print(digit_preds[0])
print(odd_preds[0])

print(y_valid[0:10])

digit_labels = np.argmax(digit_preds, axis=-1)
print(digit_labels[0:10])

odd_labels = (odd_preds > 0.5).astype(np.int32).reshape(1, -1)[0]
print(odd_labels[0:10])

