# day33 > 2_개, 고양이 분류.py
# 실무에서는 데이터셋을 웹에서 로드하기보단 직접 로드하는 경우가 더 많다.
# https://www.kaggle.com/datasets/tongpython/cat-and-dog?resource=download에서 archive.zip -> cat_and_dog.zip으로 day33 폴더에 넣기
import os
import zipfile
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 1. 데이터 준비
# 데이터 경로 위치
SOURCE_FILENAME = 'cat_and_dog.zip'  # zip 파일명
EXTRACT_FOLDER = 'C:/datasets/archive'  # zip 압축해제할 폴더명
# 압축 해제 코드
with zipfile.ZipFile(SOURCE_FILENAME, 'r') as zip_ref:  # zip 파일을 읽기 모드 r로 zip_ref 변수에 담는다
    zip_ref.extractall(EXTRACT_FOLDER)  # 지정한 경로에 압축풀기 (파일객체변수명.extractall(압축해제할 폴더 경로)
# 훈련용/검증용 데이터 저장위치 지정
TRAIN_DIR = os.path.join(EXTRACT_FOLDER, 'training_set/training_set')
TEST_DIR = os.path.join(EXTRACT_FOLDER, 'test_set/test_set')
print(TRAIN_DIR)
print(TEST_DIR)

# 2. 정규화
# ImageDataGenerator 모듈
image_gen = ImageDataGenerator(rescale=(1/255.0))  # 이미지 데이터를 0 ~ 255 -> 0 ~ 1 범위로 변경 (rescale 값을 곱하기)

# 3. 이미지 제네레이터: 한번에 많은 데이터를 갖고 오면 메모리 문제가 발생할 수 있어 이미지를 배치 단위로 반복해서 가져오기
train_data_gen = image_gen.flow_from_directory(
    TRAIN_DIR,  # 훈련용 데이터 경로
    target_size=(224, 224),  # 224 x 224 픽셀로 리사이즈
    batch_size=32,  # 이미지 배치 단위
    classes=['cats', 'dogs'],  # 문자로 된 클래스(종속)를 cats: 0, dogs: 1
    class_mode='binary',  # 이진 분류
    seed=2024
    )
test_data_gen = image_gen.flow_from_directory(
    TEST_DIR,  # 검증용 데이터 경로
    target_size=(224, 224),  # 224 x 224 픽셀로 리사이즈
    batch_size=32,  # 이미지 배치 단위
    classes=['cats', 'dogs'],  # 문자로 된 클래스(종속)를 cats: 0, dogs: 1
    class_mode='binary',  # 이진 분류
    seed=2024
    )

# 샘플 이미지 출력
class_labels = ['cats', 'dogs']
batch = next(train_data_gen)
images = batch[0]  # 독립 변수, 개/고양이 이미지
labels = batch[1]  # 종속 변수, 이미지 정답

for i in range(32):
    ax = plt.subplot(4, 8, i+1)
    plt.axis('off')
    plt.title(class_labels[int(labels[i])])  # labels[i] -> 0 or 1 -> 'cats' or 'dogs'
    plt.imshow(images[i])
plt.show()

# 모델 구성
model = tf.keras.Sequential([
    # Convolution
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu'),  # 32 filters, 3x3 kernel size, ReLU func
    tf.keras.layers.MaxPooling2D(2, 2),  # 2x2 max pooling

    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'),  # 64 filters
    tf.keras.layers.MaxPooling2D(2, 2),  # 2x2 max pooling

    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Conv2D(128, (3, 3), padding='same', activation='relu'),  # 128 filters
    tf.keras.layers.MaxPooling2D(2, 2),  # 2x2 max pooling

    # Classifier 출력층
    tf.keras.layers.Flatten(),  # 1D vector로 flattening
    tf.keras.layers.Dense(256, activation='relu'),  # fully connected layer, 512 neurons, ReLU func
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1, activation='sigmoid')  # output layer, sigmoid func for binary classification
])

# 모델 컴파일
model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

# 모델 훈련
history = model.fit(train_data_gen, epochs=10, validation_data=test_data_gen)

# 손실함수, 정확도 그래프


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


plot_loss_acc(history, 10)