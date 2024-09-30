# day26 > 2_인덱싱.py
import tensorflow as tf

# 1. 벡터
vec = tf.constant([10, 20, 30, 40, 50])
print(vec)  # tf.Tensor([10 20 30 40 50], shape=(5,), dtype=int32)
print(vec[0])  # 스칼라, tf.Tensor(10, shape=(), dtype=int32)
print(vec[0].numpy())  # 10
print(vec[-1])  # 스칼라, tf.Tensor(50, shape=(), dtype=int32)
print(vec[0:3])  # 0 ~ 2, tf.Tensor([10 20 30], shape=(3,), dtype=int32)
# 2. 행렬
mat = tf.constant([[10, 20, 30], [40, 50, 60]])
print(mat[0:2])  # [행인덱스, 열인덱스] # 철번쨰 행 ,세번째 열 # 스칼라
print(mat[0, :])  # [행 (슬라이싱) : 열(슬라이싱)] # 첫번째 행, 전체 열[:] # 벡터
print(mat[:, 1])  # 전체 행[:] 및 전체 열 # 행렬
# 3. 3차원 텐서
tensor = tf.constant(
    # 축 1: 고차원 텐서 (3차원 리스트)
    [
        # 축 2: 행렬 (2차원 리스트)
        [
            # 축 3: 벡터 (1차원 리스트)
            [10, 20, 30],
            [40, 50, 60]
        ],
        [
            [-10, -20, -30],
            [-40, -50, -60]
        ]
    ]
)

print(tensor)  # shape=(2, 2, 3), dtype=int32
print(tensor[0, :, :])  # 축 1 첫번쨰, 행 전체 열 전체 # shape=(2, 3), dtype=int32
print(tensor[:, :2, :2])  # 축 1 전체, 행 0 1, 열 0 1 # shape=(2, 2, 2), dtype=int32

# 연습
# 1. 벡터
vector = tf.constant([10, 20, 30, 40, 50])
# 문제 1. 첫번째 스칼라 요소 인덱싱
print(vector[0])  # 10
# 문제 2. 뒤에서부터 2번째 요소 인덱싱
print(vector[-2])  # 40
# 문제 3. 앞에서 3개 요소 슬라이싱
print(vector[:3])  # [10 20 30]
# 문제 4. 뒤에서 4개 요소 슬라이싱
print(vector[-4:])  # [20 30 40 50]

# 2. 행렬
matrix = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 문제 1. 첫번쨰 행, 두번째 열 인덱싱
print(matrix[0, 1])  # 2
# 문제 2. 세번째 행, 첫번째 열 인덱싱
print(matrix[2, 0])  # 7
# 문제 3. 첫번째 행 전체 슬라이싱
print(matrix[0])  # [1 2 3]
# 문제 4. 두번쨰 열 전체 슬라이싱
print(matrix[:, 1])  # [2 5 8]

# 3. 텐서
tensor = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# 문제 1. 가장 첫번째 요소 인덱싱 e.g. 1
print(tensor[0, 0, 0])  # 1
# 문제 2. 가장 마지막 요소 인덱싱 e.g. 8
print(tensor[-1, -1, -1])  # 8
# 문제 3. 첫번째 행렬 슬라이싱
print(tensor[0])  # [[1 2] [3 4]]
# 문제 4. 두번째 행렬의 첫번째 행 슬라이싱
print(tensor[1, 0])  # [5 6]
