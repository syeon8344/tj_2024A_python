# day29 > 1_합성곱신경망.py
# 1. 142p ~ 149p 개념 정리
# 2. 150p ~ 162p (model.input -> inputs, model.output -> output)
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 1. mnist 손글씨 데이터
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train, x_test: 28x28 픽셀로 된 0~9 숫자
# y_train, y_test: 정답 0~9 숫자
print(x_train.shape, y_train.shape)  # (60000, 28, 28) (60000,)
print(x_test.shape, y_test.shape)  # (10000, 28, 28) (10000,)


# 2. 샘플 확인
# print(x_train[0, :, :])  # 첫번째 x 데이터
# print(y_train[0])  # 첫번째 y 값
def plot_image(data, index):
    plt.figure(figsize=(5, 5))
    plt.imshow(x_train[index], cmap='gray')
    plt.axis('off')
    plt.show()


# plot_image(x_train, 0)

# 3. 이미지 픽셀 범위
print(x_train.min(), x_train.max())  # 0 255
print(x_test.min(), x_test.max())  # 0 255

# 4. 정규화: 각 픽셀값을 최대값 255로 나눠 0~1 사이 값으로 변환, 모델 학습을 더 빠르고 안정적으로 만든다.
x_train = x_train / 255.0
x_test = x_test / 255.0
print(x_train.min(), x_train.max())  # 0.0 1.0
print(x_test.min(), x_test.max())  # 0.0 1.0

# 4. mnist 데이터셋은 단색 이미지셋, CNN 모델에 사용하기 위해 색상 채널 축 추가
# "...", tf.newaxis: 새 축을 마지막에, tf.newaxis, ...: 새 축을 처음에, 중간: [:,tf.newaxis,:,:]
x_train_color = x_train[..., tf.newaxis]
x_test_color = x_test[..., tf.newaxis]
print(x_train_color.shape, x_test_color.shape)  # (60000, 28, 28, 1) (10000, 28, 28, 1)

# 6. Sequential API를 사용해 샘플 모델 생성
model = tf.keras.models.Sequential([
    # Convolution 레이어 1: 필터 32개, 3x3 사이즈, ReLU 활성 함수 사용
    # name="레이어에 지정할 이름"
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1), name="conv"),
    # Max pooling 레이어 2: 2x2 사이즈
    tf.keras.layers.MaxPooling2D((2, 2), name="max_pool"),
    # Flatten 레이어 3: 2차원 배열 -> 1차원 벡터, Dense 출력층 사용을 위해 적용
    tf.keras.layers.Flatten(),
    # Dense 레이어 4: 출력층, 분류값이 10개인 다중 분류 문제이므로 softmax 활성화 함수 사용
    tf.keras.layers.Dense(10, activation='softmax')
])

# 7. 모델 컴파일, 옵티마이저, 손실함수, 평가지표 설정
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 8. 모델 훈련
history = model.fit(x_train_color, y_train, epochs=10, validation_data=(x_test_color, y_test))

# 9. 모델 평가
model.evaluate(x_test_color, y_test)


# 10. 모델 손실함수, 정확도 시각화
def plot_loss_acc(history, epoch):
    fig, axes = plt.subplots(1, 2)
    # 손실함수 시각화
    axes[0].plot(range(1, epoch + 1), history.history['loss'])
    axes[0].plot(range(1, epoch + 1), history.history['val_loss'])
    axes[0].set_title('Model Loss')
    axes[0].set_ylabel('Loss')
    axes[0].set_xlabel('Epoch')
    axes[0].legend(['Train', 'Test'], loc='best')
    # 정확도 시각화
    axes[1].plot(range(1, epoch + 1), history.history['accuracy'])
    axes[1].plot(range(1, epoch + 1), history.history['val_accuracy'])
    axes[1].set_title('Model Accuracy')
    axes[1].set_ylabel('Accuracy')
    axes[1].set_xlabel('Epoch')
    axes[1].legend(['Train', 'Test'], loc='best')
    plt.show()


# plot_loss_acc(history, 10)

# 모델 구조
model.summary()

# 11. 훈련된 모델로 예측
predictions = model.predict(x_test_color)
print(predictions[0])  # 첫번째 예측
print(np.argmax(predictions[0]))  # 첫번째 예측 리스트의 최댓값 인덱스 (=예측값), 7
print(y_test[0])  # 7
# # 모델 입력 텐서 형태
# print(model.inputs)
#
# # 모델 출력 텐서 형태
# print(model.output)

# 모델 레이어
print(model.layers)
"""
[<Conv2D name=conv, built=True>, <MaxPooling2D name=max_pool, built=True>, 
<Flatten name=flatten, built=True>, <Dense name=dense, built=True>]
"""
print(model.layers[0])  # <Conv2D name=conv, built=True>

# 첫번째 레이어 입출력, 가중치, 커널 가중치, bias 가중치
print(model.layers[0].input)
print(model.layers[0].output)
print(model.layers[0].weights)
print(model.layers[0].kernel)
print(model.layers[0].bias)

# 레이어 이름으로 선택
print(model.get_layer('conv'))

# 샘플 이미지의 레이어 별 출력을 리스트에 추가하기 (1,2번째 레이어)
activator = tf.keras.Model(inputs=model.inputs, outputs=[layer.output for layer in model.layers[:2]])
activations = activator.predict(x_test_color[0][tf.newaxis, ...])
len(activations)  # 출력값 2개

# 첫 번째 레이어 (conv) 출력층
conv_activation = activations[0]
print(conv_activation.shape)  # (1, 26, 26, 32)

# Convolution 시각화
plt.figure(figsize=(10, 10))
for i in range(32):
    plt.subplot(4, 8, i+1)
    plt.imshow(conv_activation[0, :, :, i], cmap='viridis')
    plt.axis('off')
    plt.title(f'Kernel {i+1}')
plt.tight_layout()
plt.show()

