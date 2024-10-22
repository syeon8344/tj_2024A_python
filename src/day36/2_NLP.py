# day36 > 2_NLP 자연어처리 Natural Language Processing.py

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
# 텐서플로 토크나이저
sentences = [
    # 문장들
    "영실이는 나를 정말 정말 좋아해",
    "영실이는 영화를 좋아해"
]
tokenizer = Tokenizer()  # 토크나이저 객체 생성
tokenizer.fit_on_texts(sentences)  # .fit_on_texts(문장목록)
print("단어 인덱스: ", tokenizer.word_index)  # 문장들의 단어들에 인덱스 매칭 -> 단어 사전{단어: 인덱스}, 빈도수, 위치 순, 중복 X
# {'영실이는': 1, '정말': 2, '좋아해': 3, '나를': 4, '영화를': 5}

# 인코딩
word_encoding = tokenizer.texts_to_sequences(sentences)
print(word_encoding)  # [[1, 4, 2, 2, 3], [1, 5, 3]]

# 사전에 없는 단어를 인코딩할 경우 무시된다.
new_sentence = ["영실이는 경록이와 나를 좋아해"]  # 새 단어 '경록이와'
new_word_encoding = tokenizer.texts_to_sequences(new_sentence)
print(new_word_encoding)  # [[1, 4, 3]]

# 사전에 없는 단어를 처리하는 방법: 사전에 등록되지 않은 단어들을 <OOV>로 표현한다.
tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)  # 첫번째 문장 목록 단어사전화
print(tokenizer.word_index)  # {'<OOV>': 1, '영실이는': 2, '정말': 3, '좋아해': 4, '나를': 5, '영화를': 6}
print(tokenizer.texts_to_sequences(sentences))  # [[2, 5, 3, 3, 4], [2, 6, 4]]
print(tokenizer.texts_to_sequences(new_sentence))  # [[2, 1, 5, 4]] -> 1은 Out Of Vocabulary 값

# 단어 사전의 최대 개수 설정: num_words=, 최대 개수 범위 밖의 단어들도 <OOV>로 표현된다 (단어 사전이 줄어드는 것은 아니다.)
# tensorflow 2.10 문제? *** num_words = n-1 개
tokenizer = Tokenizer(num_words=3, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
print(tokenizer.word_index)  # {'<OOV>': 1, '영실이는': 2, '정말': 3, '좋아해': 4, '나를': 5, '영화를': 6}
print(tokenizer.texts_to_sequences(sentences))  # [[2, 1, 1, 1, 1], [2, 1, 1]]
print(tokenizer.texts_to_sequences(new_sentence))  # [[2, 1, 1, 1]]

# 문장 길이 맞추기: 패딩 -> .pad_seqences(인코딩 된 단어들), (기본값)앞에서부터 0을 채워 길이를 맞춘다.
word_encoding = tokenizer.texts_to_sequences(sentences)
print(word_encoding)  # [[2, 1, 1, 1, 1], [2, 1, 1]]
# paddings='post' 일 경우 뒤에 0을 붙인다.
print(pad_sequences(word_encoding))  # [[2 1 1 1 1] [0 0 2 1 1]] -> 두번째 문장의 길이를 맞추기 위해 0 패딩
# 문장 길이의 최댓값 설정: maxlen=, 잘리는 방향 설정: truncating='post' 설정시 뒤쪽에서, 기본값은 앞에서부터
print(pad_sequences(word_encoding, padding='post', maxlen=4))  # [[1 1 1 1] [2 1 1 0]]
print(pad_sequences(word_encoding, padding='post', maxlen=4, truncating='post'))  # [[1 1 1 1] [2 1 1 0]]