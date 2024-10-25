# day39 > 1_시퀀스2시퀀스.py
import pandas as pd
import re
# 챗봇 질문 응답 데이터
from Korpora import KoreanChatbotKorpus
# 형태소 분석기
from konlpy.tag import Okt
# 단어사전 토큰화
import numpy as np
import warnings
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
# 모델 학습
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import ModelCheckpoint

# 챗봇 라이브러리 불러오기
# 소스에서 URL 오류, 'url': 'https://raw.githubusercontent.com/songys/Chatbot_data/master/ChatbotData.csv'로 변경
corpus = KoreanChatbotKorpus()
print(type(corpus.train))  # <class 'Korpora.korpora.LabeledSentencePairKorpusData'> DataFrame과 비슷하다
corpus_df = pd.DataFrame(corpus.train)
print(corpus_df.head())

# 챗봇 데이터 샘플 확인
print(corpus.get_all_texts()[:5])  # 질문 "열"의 상단 5개 데이터 확인
print(corpus.get_all_pairs()[:5])  # 응답 "열"의 상단 5개 데이터 확인

# text와 pair 쌍
print("Q: ", corpus.train[0].text)  # Q:  12시 땡!
print("A: ", corpus.train[0].pair)  # A:  하루가 또 가네요.

# 전체 코퍼스 크기 11823
print("Total Corpus Size: ", len(corpus.get_all_texts()))
print(corpus_df.shape)  # .shape: DataFrame 객체의 차원 확인, (11823, 3)

# 1000개 샘플링
texts = []
pairs = []
# for index, value in enumerate(list/tuple)
# for value in list/tuple
for i in range(1000):
    # print("Q: ", corpus_df["text"][i])
    # print("A: ", corpus_df["pair"][i])
    texts.append(corpus.train[i].text)
    pairs.append(corpus.train[i].pair)

print(texts[:5])
print(pairs[:5])


# 2. 데이터 전처리
# 정규식 regex로 데이터 전처리 함수
def clean_sentence(sentence):
    # 한글, 숫자, 띄어쓰기를 제외한 모든 문자를 제거, re.sub(): 파이썬 내장 문자열 정규표현식 함수
    # pd['열이름'].str.replace(정규식, 변환 결과 문자, regex=True): DataFrame 내 정규표현식 적용
    sentence = re.sub(r'[^0-9ㄱ-ㅎㅏ-ㅣ가-힣\s]', '', sentence)  # ' ' == \s
    return sentence


# 전처리 함수 테스트
print(clean_sentence("텐서플로!@#$%^"))  # 텐서플로
print(clean_sentence("하루가 또 가네요."))  # 하루가 또 가네요

# konlpy > Okt 형태소
okt = Okt()  # 한글 분석기 개체


def process_morph(sentence):
    return ' '.join(okt.morphs(sentence))  # 사이에_추가할_문자열.join(문자열 리스트)


# Seq2Seq 모델 훈련시 필요 데이터셋: 전체 질문, 답변 시작, 답변 끝
# 인코더 question(질문 전체), 디코더에 입력 answer_input(<START>를 앞에 추가), 디코더 출력할 answer_output(<END>를 끝에 추가)
# 한글 문장 전처리
def clean_and_morph(sentence, is_question=True):  # 매개변수명=초기값: 매개변수의 초기값 설정
    # 한글 문장 전처리
    sentence = clean_sentence(sentence)
    # konlpy > Okt 형태소 변환
    sentence = process_morph(sentence)
    # 질문인 경우와 답변인 경우 분기
    if is_question:
        return sentence
    else:
        # START 토큰은 decoder input, END 토큰은 decoder output에 추가
        return "<START> " + sentence, sentence + " <END>"  # 소괄호가 생략된 튜플 반환 (함수의 연산 결과는 항상 1개)


def preprocess(texts, pairs):
    questions = []
    answer_in = []
    answer_out = []
    # 질의 전처리
    for text in texts:
        # 전처리와 morph 수행
        question = clean_and_morph(text, is_question=True)
        questions.append(question)
    # 답변 전처리
    for pair in pairs:
        # pair: (입력 답변, 출력 답변)
        in_, out_ = clean_and_morph(pair, is_question=False)
        answer_in.append(in_)
        answer_out.append(out_)
    return questions, answer_in, answer_out


questions, answer_in, answer_out = preprocess(texts, pairs)
print(questions[:2])
print(answer_in[:2])
print(answer_out[:2])

# 전체 문장을 하나의 리스트로 만들기
all_sentences = questions + answer_in + answer_out

# 단어 사전 만들기
# filters='': 토큰화 과정에서 특정 기호를 제거(필터)
# lower=False: 영문을 소문자로 전부 변환할지 (기본값 True: 전부 소문자로)
# oov_token: 단어 사전에 없는 문자를 매칭하면 <OOV> 문자열로 표현
tokenizer = Tokenizer(filters='', lower=False, oov_token='<OOV>')
tokenizer.fit_on_texts(all_sentences)
print(tokenizer.word_index)  # 단어 사전 확인
# {'<OOV>': 1, '<START>': 2, '<END>': 3, '이': 4, '거': 5, '을': 6, '가': 7, '나': 8, '예요': 9, ... }
print(len(tokenizer.word_index))  # 단어의 총 개수

# .texts_to_sequences(): 등록된 단어사전에 따라 문장의 단어들을 벡터(숫자) 매칭하여 변환
# 치환: 텍스트를 시퀀스로 인코딩
question_sequence = tokenizer.texts_to_sequences(questions)
print(question_sequence[0])  # [1608, 1609]
answer_in_sequence = tokenizer.texts_to_sequences(answer_in)
print(answer_in_sequence[0])  # [2, 391, 7, 356, 1234]
answer_out_sequence = tokenizer.texts_to_sequences(answer_out)
print(answer_out_sequence[0])  # [391, 7, 356, 1234, 3]
# 문장의 길이 맞추기 (pad_sequences)
MAX_LENGTH = 30  # 임의값
question_padded = pad_sequences(question_sequence, maxlen=MAX_LENGTH, truncating='post', padding='post')
answer_in_padded = pad_sequences(answer_in_sequence, maxlen=MAX_LENGTH, truncating='post', padding='post')
answer_out_padded = pad_sequences(answer_out_sequence, maxlen=MAX_LENGTH, truncating='post', padding='post')

print(question_padded.shape, answer_in_padded.shape, answer_out_padded.shape)  # (1000, 30) (1000, 30) (1000, 30)


# 인코더
# 상속: 하나의 클래스가 다른 클래스에게 속성/필드와 함수/기능을 물려주는 행위
# JAVA: class A extends B, this, super
# python: class A(B), self, super
class Encoder(tf.keras.Model):
    # 초기화 함수 (생성자): 사용할 변수, 레이어를 미리 불러와 파라미터 값들을 설정
    def __init__(self, units, vocab_size, embedding_dim, time_steps):
        # 1. units: LSTM에서 사용할 유닛/노드/뉴런 수
        # 2. vocab_size: 임베딩 레이어로 들어가는 단어 크기, 문장 내 단어마다 +1
        # 3. embedding_dim: 임베딩 레이어의 각 단어 출력 벡터의 차원 (한 단어를 몇 차원으로 구성할 것인가?)
        # 4. time_steps: 임베딩 레이어 입력으로 들어가는 시퀀스 길이 (한번에 학습할 단어 수)
        # super(): 상속하는 부모 클래스, .__init__(): 생성자를 불러온다 -> Model 클래스의 모든 속성 이용 가능.
        super(Encoder, self).__init__()
        # 1. Embed 레이어
        self.embedding = Embedding(vocab_size, embedding_dim, input_length=time_steps)
        # 2. 드롭아웃 레이어: 매 회차마다 매개변수 비율만큼 랜덤하게 학습 X
        self.dropout = Dropout(0.2)
        # 3. LSTM 레이어
        self.lstm = LSTM(units, return_state=True)

    # 실행 함수 .call()
    def call(self, inputs):
        x = self.embedding(inputs)
        x = self.dropout(x)
        x, hidden_state, cell_state = self.lstm(x)
        # x: 현재 문장의 특징/정보/패턴
        # 은닉 상태: LSTM 층에서 현재 + 바로 직전 시점까지 기록한 특징/정보/패턴 (단기기억 STM)
        # 셀 상태: LSTM 알고리즘이 전체 단어들에서 습득한 중요 특징/정보/패턴 (장기기억 LTM)
        # 특징, 정보, 패턴?
        # CNN: 이미지 분석 - 곡선, 색감, 사이즈, 비율, 질감(텍스처) 등 (RGB 0~255)
        # RNN: 텍스트 분석 - 빈도, 형태소(동사, 형용사), 감정, 단어의 의미 등 (텍스트 대신 벡터 밀집 행렬)
        # 인코더는 입력 과정이므로 출력층 Dense가 없다
        return [hidden_state, cell_state]


# 디코더 (출력 단계)
class Decoder(tf.keras.Model):
    def __init__(self, units, vocab_size, embedding_dim, time_steps):
        super(Decoder, self).__init__()
        self.embedding = Embedding(vocab_size, embedding_dim, input_length=time_steps)
        self.dropout = Dropout(0.2)
        self.lstm = LSTM(units, return_sequences=True, return_state=True)
        # return_state: 기본값 True, 은닉 상태와 셀 상태를 반환
        # return_sequences: 모든 시점의 출력을 반환
        self.dense = Dense(vocab_size, activation='softmax')  # 최종 출력 레이어

    def call(self, inputs, initial_state):
        x = self.embedding(inputs)
        x = self.dropout(x)
        x, hidden_state, cell_state = self.lstm(x, initial_state=initial_state)  # LSTM 레이어 변수
        # initial_state: 초기화 상태 속성, 인코더와 결합 이후 인코더가 생성한 은닉 상태와 셀 상태를 대입
        x = self.dense(x)  # 출력층의 값 "x"
        return x, hidden_state, cell_state


# Seq2Seq Model 모델 결합
class Seq2Seq(tf.keras.Model):
    def __init__(self, units, vocab_size, embedding_dim, time_steps, start_token, end_token):
        super(Seq2Seq, self).__init__()
        self.start_token = start_token
        self.end_token = end_token
        self.time_steps = time_steps
        self.encoder = Encoder(units, vocab_size, embedding_dim, time_steps)
        self.decoder = Decoder(units, vocab_size, embedding_dim, time_steps)

    def call(self, inputs, training=True):
        if training:
            encoder_inputs, decoder_inputs = inputs
            context_vector = self.encoder(encoder_inputs)
            decoder_outputs, _, _ = self.decoder(inputs=decoder_inputs, initial_state=context_vector)
            return decoder_outputs
        else:
            context_vector = self.encoder(inputs)
            target_seq = tf.constant([[self.start_token]], dtype=tf.float32)
            results = tf.TensorArray(tf.int32, self.time_steps)

            for i in tf.range(self.time_steps):
                decoder_output, decoder_hidden, decoder_cell = self.decoder(target_seq, initial_state=context_vector)
                decoder_output = tf.cast(tf.argmax(decoder_output, axis=-1, dtype=tf.int32))
                decoder_output = tf.reshape(decoder_output, shape=(1, 1))
                results = results.write(i, decoder_output)

                if decoder_output == self.end_token:
                    break

                target_seq = decoder_output
                context_vector = [decoder_hidden, decoder_cell]

            return tf.reshape(results.stack(), shape=(1, self.time_steps))
