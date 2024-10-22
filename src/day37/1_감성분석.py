# day37 > 1_감성분석.py (python 3.8)
# 네이버 영화 리뷰 데이터
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
import konlpy
from konlpy.tag import Kkma, Komoran, Okt, Mecab
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM, Bidirectional, GlobalAveragePooling1D

# 1. 훈련용 파일 불러오기
train_file = tf.keras.utils.get_file(
    'ratings_train.txt',
    origin='https://raw.githubusercontent.com/e9t/nsmc/refs/heads/master/ratings_train.txt', extract=True)
# 2. pandas로 데이터 불러오기
train = pd.read_csv(train_file, sep='\t', encoding='utf-8')

# 3. 데이터 크기 및 샘플 확인
print("train shape: ", train.shape)  # (150000, 3)
print(train.head())  # id = 게시물 번호, document = 리뷰내용, label = 0 (부정), 1 (긍정)
'''
         id                                           document  label
0   9976970                                아 더빙.. 진짜 짜증나네요 목소리      0
1   3819312                  흠...포스터보고 초딩영화줄....오버연기조차 가볍지 않구나      1
2  10265843                                  너무재밓었다그래서보는것을추천한다      0
3   9045019                      교도소 이야기구먼 ..솔직히 재미는 없다..평점 조정      0
4   6483659  사이몬페그의 익살스런 연기가 돋보였던 영화!스파이더맨에서 늙어보이기만 했던 커스틴 ...      1
'''

# 4. 레이블 별 개수
print(train['label'].value_counts())
'''
label
0    75173
1    74827
Name: count, dtype: int64
'''

# 5. 레이블 별 비율
# sns.countplot(x='label', data=train)
# plt.show()

# 6. 결측치 확인: pd객체.isnull()
print(train.isnull().sum())
'''
id          0
document    5
label       0
dtype: int64
'''

# 7. document 열의 결측치(의견 없음)가 특정 label 값을 갖는지 확인
print(train[train['document'].isnull()])  # 1 1 0 0 0

# 8. 레이블 별 텍스트 길이
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
# data_len = train[train['label'] == 1]['document'].str.len()
# ax1.hist(data_len)  # 히스토그램
# ax1.set_title('positive')
#
# data_len = train[train['label'] == 0]['document'].str.len()
# ax2.hist(data_len)
# ax2.set_title('negative')
# fig.suptitle('# of characters')
# plt.show()

# 9. Mecab 형태소 설치 후 Kkma, Komora, Okt, Mecab import
# pip install Mecab-ko
# pip install konlpy
# Mecab은 별도의 설치과정 필요 https://github.com/jonghwanhyeon/python-mecab-ko
kkma = Kkma()
komoran = Komoran()
okt = Okt()
# MeCab 단어사전 경로 지정 필요
mecab = Mecab(dicpath="C:/Users/tj-bu-703-06/PycharmProjects/tj_2024A_python/.venv8/Lib/site-packages/mecab-ko-dic")

# 9. 형태소별 샘플
text = '영실아안녕오늘날씨어때?'


def sample_ko_pos(txt):
    print(f"==== {txt} ====")
    print(f"Kkma: {kkma.pos(txt)}")
    print(f"Komoran: {komoran.pos(txt)}")
    print(f"Okt: {okt.pos(txt)}")
    print(f"Mecab: {mecab.pos(txt)}")
    print()


# sample_ko_pos(text)
'''
==== 영실아안녕오늘날씨어때? ====
Kkma: [('영', 'MAG'), ('싣', 'VV'), ('아', 'ECD'), ('안녕', 'NNG'), ('오늘날', 'NNG'), ('씨', 'VV'), ('어', 'ECD'), ('때', 'NNG'), ('?', 'SF')]
Komoran: [('영', 'NNP'), ('실', 'NNP'), ('아', 'NNP'), ('안녕', 'NNP'), ('오늘날', 'NNP'), ('씨', 'NNB'), ('어떻', 'VA'), ('어', 'EF'), ('?', 'SF')]
Okt: [('영', 'Modifier'), ('실아', 'Noun'), ('안녕', 'Noun'), ('오늘날', 'Noun'), ('씨', 'Suffix'), ('어때', 'Adjective'), ('?', 'Punctuation')]
Mecab: [('영실', 'NNG'), ('아', 'IC'), ('안녕', 'IC'), ('오늘', 'MAG'), ('날씨', 'NNG'), ('어때', 'VA+EF'), ('?', 'SF')]
'''
# 신조어 또는 맞춤법이 틀린 단어 포함
text2 = "영실아안뇽오늘날씨어때?"
# sample_ko_pos(text2)
'''
==== 영실아안뇽오늘날씨어때? ====
Kkma: [('영', 'MAG'), ('싣', 'VV'), ('아', 'ECD'), ('안', 'MAG'), ('뇽', 'UN'), ('오늘날', 'NNG'), ('씨', 'NNB'), ('어', 'VV'), ('어', 'ECS'), ('때', 'NNG'), ('?', 'SF')]
Komoran: [('영실아안뇽오늘날씨어때?', 'NA')]
Okt: [('영', 'Modifier'), ('실아', 'Noun'), ('안뇽', 'Noun'), ('오늘날', 'Noun'), ('씨', 'Suffix'), ('어때', 'Adjective'), ('?', 'Punctuation')]
Mecab: [('영실', 'NNG'), ('아안', 'NNG'), ('뇽오늘날씨어때', 'UNKNOWN'), ('?', 'SF')]
'''
# 샘플 문장
text3 = "정말 재미있고 매력적인 영화에요 추천합니다."
# sample_ko_pos(text3)
'''
==== 정말 재미있고 매력적인 영화에요 추천합니다. ====
Kkma: [('정말', 'MAG'), ('재미있', 'VA'), ('고', 'ECE'), ('매력적', 'NNG'), ('이', 'VCP'), ('ㄴ', 'ETD'), ('영화', 'NNG'), ('에', 'JKM'), ('요', 'JX'), ('추천', 'NNG'), ('하', 'XSV'), ('ㅂ니다', 'EFN'), ('.', 'SF')]
Komoran: [('정말', 'MAG'), ('재미있', 'VA'), ('고', 'EC'), ('매력', 'NNG'), ('적', 'XSN'), ('이', 'VCP'), ('ㄴ', 'ETM'), ('영화', 'NNG'), ('에', 'JKB'), ('요', 'JX'), ('추천', 'NNG'), ('하', 'XSV'), ('ㅂ니다', 'EF'), ('.', 'SF')]
Okt: [('정말', 'Noun'), ('재미있고', 'Adjective'), ('매력', 'Noun'), ('적', 'Suffix'), ('인', 'Josa'), ('영화', 'Noun'), ('에요', 'Josa'), ('추천', 'Noun'), ('합니다', 'Verb'), ('.', 'Punctuation')]
Mecab: [('정말', 'MAG'), ('재미있', 'VA'), ('고', 'EC'), ('매력', 'NNG'), ('적', 'XSN'), ('인', 'VCP+ETM'), ('영화', 'NNG'), ('에', 'JKB'), ('요', 'MM'), ('추천', 'NNG'), ('합니다', 'XSV+EF'), ('.', 'SF')]
EOS
'''

# 10. 데이터 전처리 - 텍스트 전처리 (영어와 한글만 남기고 삭제)
train['document'] = train['document'].str.replace(r"[^A-Za-zㄱ-ㅎㅏ-ㅣ가-힣 ]", "", regex=True)
print(train['document'].head())
# 결측치 제거, .dropna( ) : 결측치 제거 함수
train = train.dropna()
print(train.shape)  # (149995, 3)


# 스탑워드와 형태소 분석 (한글 불용어)
def word_tokenization(txt):
    # 불용어 목록 : 관사, 전치사, 조사, 접속사 등 의미 없는 단어를 제거
    stop_words = ["는", "을", "를", "이", "가", "의", "던", "고", "하", "다", "은", "에", "들", "지", "게", "도"]
    return [word for word in mecab.morphs(txt) if word not in stop_words]


data = train['document'].apply(lambda x: word_tokenization(x))
print(data.head())
'''
0                        [아, 더, 빙, 진짜, 짜증, 나, 네요, 목소리]
1       [흠, 포스터, 보고, 초딩, 영화, 줄, 오버, 연기, 조차, 가볍, 않, 구나]
2                              [너무, 재, 밓었다그래서보는것을추천한다]
3                   [교도소, 이야기, 구먼, 솔직히, 재미, 없, 평점, 조정]
4    [사이몬페그, 익살, 스런, 연기, 돋보였, 영화, 스파이더맨, 에서, 늙, 어, ...
'''

# 11. 훈련용과 테스트용 데이터 분할
# tensorflow 모델 훈련시에도 바로 split 가능
# model.fit(x_train, y_train, epochs=20, batch_size=64, validation_split=0.2)
training_size = 120000
# train 분할
train_sentences = data[:training_size]
valid_sentences = data[training_size:]
# label 분할
train_labels = train['label'][:training_size]
valid_labels = train['label'][training_size:]

# 12. 단어 사전 만들기, .fit_on_texts( ): 문자와 숫자(인덱스)를 매칭한다 -> 문자를 숫자로 변환
tokenizer = Tokenizer()  # 토크나이저 객체 생성
tokenizer.fit_on_texts(data)  # 빈도수 기준으로 토큰(단어) 사전 생성
print('총 단어 개수: ', len(tokenizer.word_index))  # 총 단어 개수:  52171


# 5회 이상만 vocab_size에 포함
def get_vocab_size(threshold):
    cnt = 0
    for x in tokenizer.word_counts.values():
        if x >= threshold:
            cnt += 1
    return cnt


vocab_size = get_vocab_size(5)
print('vocab_size: ', vocab_size)  # vocab_size:  15567

# 13. <OOV>: 사전에 없는 단어
oov_token = '<OOV>'
vocab_size = 15000
tokenizer = Tokenizer(num_words=vocab_size + 1, oov_token=oov_token)
tokenizer.fit_on_texts(data)
# print(tokenizer.word_index)
print("단어 사전 개수: ", len(tokenizer.word_counts))

# 14. 숫자 벡터로 변환
print(train_sentences[:2])
train_sequences = tokenizer.texts_to_sequences(train_sentences)
valid_sentences = tokenizer.texts_to_sequences(valid_sentences)
print(train_sequences[:2])

# 15. 문장 중 최대 길이 구하기 (모든 문장 길이를 맞춰 모델 성능 향상을 위함)
max_length = max(len(x) for x in train_sequences)
print("문장 최대 길이: ", max_length)

# 16. 패딩을 상용하여 문장 길이를 맞추기
trunc_type = 'post'  # 길이를 초과하면 뒷부분을 자르기
padding_type = 'post'  # 길이가 부족하면 뒷부분을 0으로 채우기
train_padded = pad_sequences(train_sequences, maxlen=max_length, truncating=trunc_type, padding=padding_type)
valid_padded = pad_sequences(valid_sentences, maxlen=max_length, truncating=trunc_type, padding=padding_type)
train_labels = np.asarray(train_labels)
valid_labels = np.asarray(valid_labels)
print(f"샘플: {train_padded[:1]}")


# 17. 모델
def create_model():
    model = Sequential([
        Embedding(vocab_size, 32),
        Bidirectional(LSTM(16, return_sequences=False)),  # 양방향이므로 유닛 X 2로 맞추기
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')  # 이진분류시 주로 사용되는 활성함수, 출력 레이어
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


model = create_model()
model.summary()

# 18. 가장 좋은 loss 가중치 저장
checkpoint_path = "best_performed_model.ckpt"
checkpoint = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, save_weights_only=True, save_best_only=True, monitor="val_loss", verbose=1)

# 19. 학습 조기 종료
early_stop = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=2)

# 20. 학습
# history = model.fit(train_padded, train_labels,  # 훈련용 데이터들
#                     epochs=10,
#                     batch_size=64,  # 한번에 처리되는 데이터 수
#                     validation_data=(valid_padded, valid_labels),  # 검증용
#                     callbacks=[checkpoint, early_stop])


# 21. 평가 시각화
def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(len(acc))

    plt.plot(epochs, acc, 'r', label='Training accuracy')
    plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
    plt.title('Training and validation accuracy')
    plt.legend(loc=0)
    plt.figure()

    plt.plot(epochs, loss, 'r', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend(loc=0)

    plt.show()


# plot_history(history)

# 22. 새 리뷰들로 예측하기
new_reviews = ['영화 정말 재미있다', '정말 지루하다', '그냥 보통이었어요', '생각보다 재미가 없다']
# 데이터 전처리
new_reviews_df = pd.DataFrame(new_reviews)
print(new_reviews_df)
new_reviews = new_reviews_df.replace(r"[^A-Za-zㄱ-ㅎㅏ-ㅣ가-힣 ]", "", regex=True)
new_reviews_data = new_reviews_df[0].apply(lambda x: word_tokenization(x))
test_data = tokenizer.texts_to_sequences(new_reviews_data)
test_data = pad_sequences(test_data, truncating=trunc_type, padding=padding_type, maxlen=max_length)
print("predicted labels pre-trained: ", model.predict(test_data))
'''
predicted labels pre-trained:  [[0.5004916 ]
 [0.5008362 ]
 [0.49866486]
 [0.49954504]]
'''
model.load_weights(checkpoint_path)
print("predicted labels using checkpoint: ", model.predict(test_data))
'''
predicted labels using checkpoint:  [[0.93743885]
 [0.02615228]
 [0.17351997]
 [0.11709426]]
 '''

