# day31 > 3_합성곱신경망.py  # Functional API
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 1. 데이터셋 로드: 의류 mnist (10종류 의류 데이터셋)
fashion_mnist = tf.keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
print(x_train.shape, y_train.shape)  # (60000, 28, 28) (60000,)
print(x_test.shape, y_test.shape)  # (10000, 28, 28) (10000,)

# 분류별 이름
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# 2. 정규화
x_train = x_train / 255.0
x_test = x_test / 255.0

# 3. 색상 축 설정
x_train_co = x_train[..., tf.newaxis]
x_test_co = x_test[..., tf.newaxis]

# Functional API를 이용하여 모델 생성(다중 입력), 컴파일, 훈련 및 예측 테스트
# 4. 모델 구성
inputs = tf.keras.layers.Input(shape=(28, 28, 1))  # 28x28 grayscale image
conv = tf.keras.layers.Conv2D(32, (3, 3), activation='relu')(inputs)
pool = tf.keras.layers.MaxPooling2D((2, 2))(conv)
flat = tf.keras.layers.Flatten()(pool)
input_flat = tf.keras.layers.Flatten()(inputs)
concat = tf.keras.layers.Concatenate()([flat, input_flat])
outputs = tf.keras.layers.Dense(10, activation='softmax')(concat)

model = tf.keras.models.Model(inputs=inputs, outputs=outputs)

print(model.summary())

# 5. 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 6. 모델 훈련
history = model.fit(x_train_co, y_train, epochs=1, validation_data=(x_test_co, y_test))

# 7. 모델 평가
print(model.evaluate(x_test_co, y_test))

# 8. 모델 예측
print(y_test[:10])
y_pred = model.predict(x_test_co)
print(y_pred.shape)  # (10000, 10)
# np.argmax(axis=-1): 가장 오른쪽 차원 (벡터 배열)
print(np.argmax(y_pred, axis=-1)[:10])
