# day30 > 2_합성곱신경망.py  # (CNN)
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2

# 데이터셋: 10가지 컬러 이미지셋 (0~9, 비행기, 자동차, 새, 고양이, 사슴, 개, 개구리, 말, 배, 트럭)
cifar10 = tf.keras.datasets.cifar10
(x_train, y_train), (x_valid, y_valid) = cifar10.load_data()

# 데이터셋 정보
print(x_train.shape, y_train.shape)  # RGB 채널이 이미 포함되어 있다 (50000, 32, 32, 3) (50000,)
print(x_valid.shape, y_valid.shape)  # (10000, 32, 32, 3) (10000,)
print(np.min(x_train), np.max(x_train))


# 샘플 이미지
def plot_image(index):
    plt.imshow(x_train[index])
    plt.title(y_train[index])
    plt.show()


# plot_image(0)

# 데이터 전처리
x_train = x_train / 255.0
x_valid = x_valid / 255.0

# 모델 구조
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(48, kernel_size=(3, 3), padding='same', input_shape=(32, 32, 3), activation='relu'))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Conv2D(64, kernel_size=(3, 3), padding='same', activation='relu'))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# Compile the new Sequential model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the new Sequential model
history = model.fit(x_train, y_train, epochs=10, validation_data=(x_valid, y_valid))

# 모델 구조
model.summary()

# 이미지 예측
# 1. 파이썬 OpenCV: 이미지를 파이썬으로 호출하는 모듈  # import cv2
# 2. 외부 이미지 가져오기
img = cv2.imread("dog.png")
img2 = cv2.imread("car.png")
# 3. 이미지 사이즈 변경
img = cv2.resize(img, dsize=(32, 32))
img2 = cv2.resize(img2, dsize=(32, 32))
img = img / 255
img2 = img2 / 255.0
# 4. 변경된 이미지 시각화
# cv2.imshow("dog.png", img)
# cv2.waitKey()
# 5. 모델을 이용하여 새로운 이미지 예측
result = model.predict(img[tf.newaxis, ...])  # (32, 32, 3) -> (1, 32, 32, 3)
result2 = model.predict(img2[tf.newaxis, ...])  # (32, 32, 3) -> (1, 32, 32, 3)
print(tf.argmax(result[0]).numpy())
print(tf.argmax(result2[0]).numpy())
