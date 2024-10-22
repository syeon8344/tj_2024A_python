# day36 > 1_RNN.py
"""
    RNN (Recurrent Neural Network)
        1. 이전에 읽은 input data를 feedback 받아서 hidden state를 update
        2. hidden state를 input data와 함께 feedforward neural network에 input
        3. output layer에서 prediction
        4. RNNs are particularly useful for tasks that require sequential data (like language modeling, speech recognition)
    RNNs in TensorFlow
        1. tf.keras.layers.SimpleRNN: Simple RNN layer
        2. tf.keras.layers.RNN: Base class for recurrent layers
        3. tf.keras.layers.GRU: Gated Recurrent Unit (GRU) layer
        4. tf.keras.layers.LSTM: Long Short Term Memory (LSTM) layer
    RNNs in PyTorch
        1. torch.nn.RNN: Base class for all RNN modules
        2. torch.nn.GRU: Gated Recurrent Unit (GRU)
"""
import tensorflow as tf

# 1. 임베딩 레이어 구현 - Embedding(단어 수, 차원 수): 임베딩 클래스
embedding_layer = tf.keras.layers.Embedding(100, 3)  # 100개의 단어, 3차원
result = embedding_layer(tf.constant([12, 8, 15, 20]))  # 숫자 4개 더미 입력데이터를 넣는다
print(result)  # 각 더미데이터를 임베딩 레이어를 거쳐 3개의 숫자로 변환하여 각각 표현한다.
'''
tf.Tensor(
[[-0.02585657 -0.00977025  0.02053776]
 [-0.0086012   0.01150449 -0.01737566]
 [-0.02200922  0.00931903  0.01529716]
 [-0.00936393  0.02963153 -0.02943133]], shape=(4, 3), dtype=float32)
 -> 임베딩 레이어는 각 숫자(단어)를 의미하는 벡터로 바꿔주는 역할
'''

# 2. 임베딩 레이어 활용
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(100, 3, input_length=32))  # 100개의 단어를 3차원 벡터로 변환, 입력 길이 32
model.add(tf.keras.layers.LSTM(32))  # Long Short-Term Memory 긴 문장에서 중요한 정보는 기억하는 RNN 클래스, 32개의 결과 예측
model.add(tf.keras.layers.Dense(1))  # 출력 레이어, 결과 1개로

print(model.summary())

# 3. 양방향 순환 신경망: Bidirectional RNN
bidirectional_model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(100, 3, input_length=32),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),  # LSTM 구조를 양방향으로, 유닛 개수가 2배인 64개
    tf.keras.layers.Dense(1)
])

print(bidirectional_model.summary())

# 4. 스태킹 RNN
stack_model = tf.keras.models.Sequential([
    # 100개의 단어목록, 3차원 텐서 -> 입력 파라미터 수 300개
    tf.keras.layers.Embedding(100, 3, input_length=32),
    # return_sequences=True: return_sequences=True로 설정하면 LSTM output shape: (batch_size, timesteps, units)
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32, return_sequences=True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
    tf.keras.layers.Dense(1)
])

print(stack_model.summary())

# 5. RNN Dropout
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(100, 3, input_length=32),
    # recurrent_dropout: 순환 상태의 Dropout 비율, dropout: 입력에 대한 Dropout 비율
    tf.keras.layers.LSTM(32, recurrent_dropout=0.2, dropout=0.2),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

print(model.summary())