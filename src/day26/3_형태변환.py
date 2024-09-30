# day26 > 3_형태변환.py
import tensorflow as tf

# 1. 벡터 정의
tensor = tf.constant(range(0, 24))
print(tensor)  # [0 ~ 24] # (24, 0)
# 2. 벡터를 행렬로 변환: reshape(tensor, [행, 열])
tensor1 = tf.reshape(tensor, [3, 8])  # 개수가 맞지 않으면 오류 발생!
print(tensor1)
# tensor2 = tf.reshape(tensor, [6, 4])
tensor2 = tf.reshape(tensor, [-1, 4])  # -1: 와일드카드 값
print(tensor2)
# 3. 행렬 -> 벡터
tensor3 = tf.reshape(tensor2, [-1])  # 요소 개수를 모르므로 -1
print(tensor3)
# 4. 벡터 - > 3차원 텐서 변환
# tensor4 = tf.reshape(tensor3, [2, 3, 4] )
tensor4 = tf.reshape(tensor3, [-1, 3, 4])
print(tensor4)
tensor5 = tf.reshape(tensor4, [3, 2, 4])
# 6. 3차원 텐서 -> 4차원 텐서 변환  # (3,2,4) -> (3, 2, 2, 2)
print(tensor5)
tensor6 = tf.reshape(tensor5, [3, 2, 2, 2])
