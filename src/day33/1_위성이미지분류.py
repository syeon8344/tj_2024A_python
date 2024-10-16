# day33 > 1_위성이미지분류.py
import tensorflow as tf  # windows GPU 버전: tensorflow-gpu 2.10 w/ python 3.8
import numpy as np
import json
import matplotlib.pyplot as plt
import tensorflow_datasets as datasets  # 텐서플로 데이터셋 라이브러리 (python 3.8: 4.9.2, 또는 pip 업그레이드)
from tensorflow.keras.utils import plot_model
# 새로 설치: matplotlib pandas flask scikit-learn tensorflow
print(f'gpu: {tf.test.gpu_device_name()}')  # 0 필요
# 1. 데이터 수집
# 데이터 위치
DATA_DIR = "../day32/dataset"  # 데이터셋 저장할 위치/폴더
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
# datasets.show_examples(train_ds, info)
# as_datasets() 함수로 샘플 출력
# datasets.as_dataframe(test_ds.take(10), info)
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
        # Convolution 층: 합성곱, 연산층 -> 특징 찾기
        tf.keras.layers.BatchNormalization(),
        # 배치 batch: 모델링에 있어 병렬처리에 배치(묶음) 단위로 처리하면 더 빠르고 안정적인 학습이 가능, 과대적합을 줄이기 좋다
        # BatchNormalization(): AUTOTUNE 설정과 주로 같이 쓰이는 최적화 층
        tf.keras.layers.Conv2D(32, (3, 3), padding="same", activation="relu"),
        tf.keras.layers.MaxPooling2D((2, 2)),
        # 복잡한 신경망 구현을 위해 합성곱 2번 실행
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(64, (3, 3), padding="same", activation="relu"),
        tf.keras.layers.MaxPooling2D((2, 2)),
        # Classifier 출력층: 출력층, 예측분류층 -> 특징 학습
        tf.keras.layers.Flatten(),
        # 노드 수는 주로 128, 64, 32 사용
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.3),  # 드롭아웃 (p89) 일정 비율의 노드를 제외하고 학습시킨다
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(NUM_CLASSES, activation="softmax"),
    ])
    return model


model = build_model()

# 5. 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 6. 모델 훈련/학습: 최적 하이퍼파라미터 찾기
# history = model.fit(train_data, validation_data=test_data, epochs=20)


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


# plot_loss_acc(history, 20)

# 8. 데이터 증강
# 샘플 이미지
image_batch, label_batch = next(iter(train_data.take(1)))
image = image_batch[0]
label = label_batch[0].numpy()

plt.imshow(image)
plt.title(info.features["label"].int2str(label))


# 데이터 증강 전 후를 비교하는 시각화 함수
def plot_augment(original, augmented):
    # Ensure tensors are converted to NumPy arrays if needed
    if tf.is_tensor(original):
        original = original.numpy()
    if tf.is_tensor(augmented):
        augmented = augmented.numpy()
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].imshow(original)
    axes[0].set_title('Original Image')
    axes[1].imshow(augmented)
    axes[1].set_title('Augmented Image')
    plt.show()

#
# # 좌우 뒤집기
# lr_flip = tf.image.flip_left_right(image)
# plot_augment(image, lr_flip)
#
# # 상하 뒤집기
# ud_flip = tf.image.flip_up_down(image)
# plot_augment(image, ud_flip)
#
# # rot90: 반시계 방향으로 90도 회전
# rotate90 = tf.image.rot90(image)
# plot_augment(image, rotate90)
#
# # transpose: 이미지 텐서 행렬의 행과 열의 위치를 바꾼다 (도치)
# transpose = tf.image.transpose(image)
# plot_augment(image, transpose)
#
# # 이미지 자르기 1: 이미지 중심 기준으로 가장자리부터 일정 부분을 잘라낸다
# crop1 = tf.image.central_crop(image, central_fraction=0.6)
# plot_augment(image, crop1)
#
# # 이미지 자르기 2: 이미지를 shift 이동시키고 빈칸을 검은 픽셀로 채운다
# img = tf.image.resize_with_crop_or_pad(image, target_height=64 + 20, target_width=64 + 20)
# crop2 = tf.image.random_crop(img, size=[64, 64, 3])
# plot_augment(image, crop2)
#
# # 이미지 밝기 조정
# brightened = tf.image.adjust_brightness(image, delta=0.5)
# plot_augment(image, brightened)
#
# # 이미지 채도 변경
# saturated = tf.image.adjust_saturation(image, saturation_factor=0.5)
# plot_augment(image, saturated)
#
# # 이미지 대비 조정
# contrasted = tf.image.adjust_contrast(image, contrast_factor=2)
# plot_augment(image, contrasted)


# 이미지 증강 전처리
def data_augment(image, label):
    image = tf.image.random_flip_left_right(image)  # 좌우로 뒤집기
    image = tf.image.random_flip_up_down(image)  # 위 아래로 뒤집기
    image = tf.image.rot90(image)  # 반시계 90도 회전
    image = tf.image.transpose(image)  # 이미지 행 및 렬 도치
    image = tf.image.adjust_brightness(image, delta=tf.random.uniform(shape=[], minval=-0.2, maxval=0.3))
    image = tf.image.adjust_saturation(image, saturation_factor=tf.random.uniform(shape=[], minval=-0.2, maxval=0.3))
    image = tf.cast(image, tf.float32) / 255  # 0 ~ 1 정규화
    return image, label


train_aug = train_ds.map(data_augment, num_parallel_calls=tf.data.AUTOTUNE)
test_aug = test_ds.map(data_augment, num_parallel_calls=tf.data.AUTOTUNE)

train_aug = train_aug.shuffle(BUFFER_SIZE).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
test_aug = test_aug.batch(BATCH_SIZE).cache().prefetch(tf.data.AUTOTUNE)

print(train_aug)
print(test_aug)

# 모델 생성
aug_model = build_model()

# 모델 컴파일
aug_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# # 모델 훈련
# aug_history = aug_model.fit(train_aug, validation_data=test_aug, epochs=20)
#
# plot_loss_acc(aug_history, 20)

# ResNet 사전 학습 모델
pretrained_base_model = tf.keras.applications.ResNet50V2(weights='imagenet', include_top=False, input_shape=(64, 64, 3))
pretrained_base_model.trainable = False  # ResNet50V2의 가중치 고정

plot_model(pretrained_base_model, show_shapes=True, show_layer_names=True, to_file='resnet50v2.png')


# Top층 Classifier 추가
def build_transfer_classifier():
    model = tf.keras.Sequential([
        # 사전 훈련된 모델
        pretrained_base_model,
        # Classifier: 출력층
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(NUM_CLASSES, activation='softmax'),
    ])
    return model


# 모델 구조
tc_model = build_transfer_classifier()
print(tc_model.summary())

# 모델 컴파일
tc_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 모델 훈련
tc_history = tc_model.fit(train_aug, validation_data=test_aug, epochs=50)

# 손실함수 및 정확도 그래프
plot_loss_acc(tc_history, 50)
