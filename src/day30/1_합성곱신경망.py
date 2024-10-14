# day30 > 1_합성곱신경망.py  # (CNN)
"""
데이터셋을 이용한 합성곱 모델을 구축하고 학습시켜 정확도(accuracy)를 95% 이상이 되도록 최적의 하이퍼파라미터 설정하기
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 1. 데이터셋 로드하기
fashion_mnist = tf.keras.datasets.fashion_mnist
(x_train, y_train), (x_valid, y_valid) = fashion_mnist.load_data()
print(x_train.shape, y_train.shape)  # (60000, 28, 28) (60000,)
print(x_valid.shape, y_valid.shape)  # (10000, 28, 28) (10000,)
print(np.unique(y_valid))  # [0 1 2 3 4 5 6 7 8 9]
print(np.min(x_train), np.max(x_train))  # 0 255


# 2. 로드한 데이터 시각화
def visualize_mnist(x):
    for i in range(32):
        plt.subplot(4, 8, i+1)
        plt.imshow(x[i], cmap='gray')
        plt.axis('off')
    plt.show()


# visualize_mnist(x_train)

# 3. 데이터 전처리
x_train = x_train / 255
x_valid = x_valid / 255

# 4. 단색 데이터셋이므로 1 채널 추가
x_train_ch = x_train[..., tf.newaxis]
x_valid_ch = x_valid[..., tf.newaxis]

# 5. 모델 설계
# 최적의 파라미터 찾기: 1. epochs 조정, 2. 레이어 조정
# 손실값이 증가하지 않고 정화도가 떨어지지 않는 지점
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(48, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1), padding='same'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu', padding='same'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# 6. 모델 컴파일: 옵티마이저, 손실함수, 평가지표
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 7. 모델 훈련
history = model.fit(x_train_ch, y_train, epochs=20, validation_data=(x_valid_ch, y_valid))

# 8. 모델 평가 지표 확인
model.evaluate(x_valid[..., np.newaxis], y_valid)
