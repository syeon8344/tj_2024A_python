# day32 > 1_위성이미지분류.py
import tensorflow as tf
import numpy as np
import json
import matplotlib.pyplot as plt
import tensorflow_datasets as datasets  # 텐서플로 데이터셋 라이브러리

# 1. 데이터 수집
# 데이터 위치
DATA_DIR = "dataset/"  # 데이터셋 저장할 위치/폴더
(train_ds, test_ds), info = datasets.load('eurosat/rgb',  # 데이터셋 이름
                                          split=['train[:80%]', 'train[80%:]'],  # 80% 데이터 훈련용, 20% 검증용
                                          shuffle_files=True,  # 파일을 무작위로 섞어 데이터 로드
                                          as_supervised=True,  # 이미지와 레이블로 구성된 튜플로 가져오기
                                          with_info=True,  # 데이터셋 메타정보(데이터셋 설명) 가져오기
                                          data_dir=DATA_DIR)  # 현재 py 파일이 위치한 폴더 내의 하위 폴더 dataset에 다운로드
print(train_ds)
print(test_ds)
# 데이터셋에 딸려오는 메타데이터
print(info)
# 데이터셋 내 데이터 확인
datasets.show_examples(train_ds, info)
# as_datasets() 함수로 샘플 출력
datasets.as_dataframe(test_ds.take(10), info)
# 목표 클래스 갯수
NUM_CLASSES = info.features["label"].num_classes
print(NUM_CLASSES)
# 숫자 레이블을 사용해 문자열 메타 데이터로 변환
print(info.features["label"].int2str(6))

# 2. 데이터 전처리
# 데이터 전처리 파이프라인
BATCH_SIZE = 64  # 배치: 한번에 처리하는 데이터의 묶음 단위, 배치 처리시 메모리 사용 최적화 가능. 전체 한번에 대신 배치 단위로
BUFFER_SIZE = 1000  # 버퍼: 임시 저장공간, 셔플시 버퍼에 데이터 1000개를 가져와 임시 저장, 데이터 순서가 학습되는 걸 깨기 위해 사용


def preprocess_data(image, label):
    image = tf.cast(image, tf.float32) / 255.0  # 0 ~ 1 정규화 및 float32로 변환
    return image, label


# num_parallel_calls=tf.data.AUTOTUNE: 병렬 처리 (훈련 중에도 병렬 처리로 매핑하여 시간 단축)
train_data = train_ds.map(preprocess_data, num_parallel_calls=tf.data.AUTOTUNE)
test_data = test_ds.map(preprocess_data, num_parallel_calls=tf.data.AUTOTUNE)

# 훈련용 데이터는 셔플링 및 오토튠, 검증용 데이터는 캐시 및 오토튠 (업데이트되는 데이터가 아니므로 캐시가 효과가 있다)
# .prefetch(tf.data.AUTOTUNE): 훈련과 데이터 전처리를 병렬로 수행하여 효율 향상
# .cache(): 캐시(기록), 검증 데이터셋 메모리를 캐시하고 한번 호출된 검증 데이터는 다음에 호출할 시 빠르게 접근할 수 있도록 한다.
train_data = train_data.shuffle(BUFFER_SIZE).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
test_data = test_data.batch(BATCH_SIZE).cache().prefetch(tf.data.AUTOTUNE)
for images, labels in train_data.take(1):
    print("Shape of train_data batch:", images.shape)  # (64, 64, 64, 3) 배치크기, 높이, 폭, 색상채널
# 3. 데이터 분할: 데이터셋 로드시 설정됨


# 4. 모델 설계(구축)
# Sequential API로 샘플 모델 생성
def build_model():
    model = tf.keras.Sequential([
        # Convolution 층
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(32, (3, 3), padding="same", activation="relu"),
        tf.keras.layers.MaxPooling2D((2, 2)),

        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(64, (3, 3), padding="same", activation="relu"),
        tf.keras.layers.MaxPooling2D((2, 2)),
        # Classifier 출력층
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(NUM_CLASSES, activation="softmax"),
    ])
    return model


model = build_model()

# 5. 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 6. 모델 훈련/학습: 최적 하이퍼파라미터 찾기
history = model.fit(train_data, validation_data=test_data, epochs=5)


# 7. 모델 평가
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


plot_loss_acc(history, 5)

# 8. 모델 예측
for images, labels in test_ds.take(1):
    test_image = images
    real_label = labels
# Preprocess the image
test_image = tf.expand_dims(test_image, axis=0)  # Add a batch dimension
test_image = tf.cast(test_image, tf.float32) / 255.0  # Normalize the image

# Get the predicted probabilities for each class
predictions = model.predict(test_image)

# Convert the predicted probabilities to class labels
predicted_label = np.argmax(predictions[0])

# Compare the predicted label with the real label
print("Predicted label:", info.features["label"].int2str(predicted_label))
print("Real label:", info.features["label"].int2str(real_label))
