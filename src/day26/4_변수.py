# day26 > 4_변수.py  # 43p
import tensorflow as tf

# 1. 행렬 텐서
tensor1 = tf.constant([[0, 1, 2], [3, 4, 5]])
print(tensor1)
"""
tf.Tensor(
[[0 1 2]
 [3 4 5]], shape=(2, 3), dtype=int32)
"""

# 2. 텐서플로 변수 생성
tensor_var1 = tf.Variable(tensor1)
print(tensor_var1)
"""
<tf.Variable 'Variable:0' shape=(2, 3) dtype=int32, numpy=
array([[0, 1, 2],
       [3, 4, 5]])>
"""
# tf.constant()는 값 변경 불가, tf.Variable()은 값 변경 가능.

# 3. 텐서플로 변수 속성 확인
print("name: ", tensor_var1.name)  # 텐서플로 변수명: Variable:0
print("shape: ", tensor_var1.shape)  # 크기: (2, 3)
print("dtype: ", tensor_var1.dtype)  # 데이터타입: <dtype: 'int32'>
print("numpy: ", tensor_var1.numpy())  # 데이터: [[0 1 2] [3 4 5]]

# 4. 텐서플로 변수 데이터 변경/수정/새로 할당: 현재 변수에 할당된 데이터와 크기가 같아야 한다
tensor_var1.assign(tf.constant([[1, 1, 1], [2, 2, 2]]))
print(tensor_var1)
"""
<tf.Variable 'Variable:0' shape=(2, 3) dtype=int32, numpy=
array([[1, 1, 1],
       [2, 2, 2]])>
"""
print(tensor1)  # 변하지 않고 유지되어 있다.

# 5. 텐서플로 변수를 텐서로 변환
tensor2 = tf.convert_to_tensor(tensor_var1)
print(tensor_var1)
"""
<tf.Variable 'Variable:0' shape=(2, 3) dtype=int32, numpy=
array([[1, 1, 1],
       [2, 2, 2]])>
"""
print(tensor2)  # 텐서 크기와 저장하고 있는 값 변경 불가
"""
tf.Tensor(
[[1 1 1]
 [2 2 2]], shape=(2, 3), dtype=int32)
"""

# 6. 텐서플로 변수의 name 속성 정의
tensor_var2 = tf.Variable(tensor2, name="new_name")  # 변수 이름 설정 -> new_name:0
print(tensor_var2)

# 7. 텐서플로 변수 연산
print(tensor_var1 + tensor_var2)  # [[2 2 2] [4 4 4]]
