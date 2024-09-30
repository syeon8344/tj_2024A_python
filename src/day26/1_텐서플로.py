# day26 > 1_텐서플로.py
"""
    텐서플로
        1. 구글에서 개발한 오픈소스 딥러닝 프레임워크
        2. 머신러닝, 딥러닝 모델을 만들고 훈련하는 데 사용
        3. 특히 신경망 기반 모델 구축 및 학습에 주로 사용
        4. Keras 고수준 API를 제공하여 보다 간단하게 모델을 정의하고 훈련할 수 있다
        5. 그 외에도 이미지 처리, 자연어 처리, 음성 인식 등의 여러 분야에서 사용
    텐서
        1. 텐서플로에서 다루는 기본 데이터 구조
        2. 다차원의 배열 또는 리스트와 비슷하다
        3. 텐서플로: 텐서 데이터의 흐름, 데이터를 처리하고 학습시키는 과정
        4. 종류:
            a. 스칼라: 0차원 텐서, 상수, 랭크 0 = 차수 0, 방향 없음 e.g. 5
            b. 벡터: 1차원 텐서, 1차원 리스트, 랭크 1 = 차수 1, (X), 단방향 e.g. [10, 20, 30]
            c. 매트릭스(행렬): 2차원 텐서, 2차원 리스트, 랭크 2 = 차수 2, (Y, X), 방향: (행 (개수), 열 (개수)) e.g. [[1,2], [3,4]]
            d. 고차원 텐서:
                - 3차원 텐서: 3차원 리스트, 랭크 3 = 차수 3, (Z, Y, X), 방향: (높이, 행, 열)
                - 4차원 텐서: 4차원 리스트, 랭크 4 = 차수 4, (W, Z, Y, X), 방향: (W축, 높이, 행, 열)
"""
import tensorflow as tf  # 텐서플로 모듈
# [1] 스칼라
a = tf.constant(5)  # 스칼라 정의
print(a)  # tf.Tensor(5, shape=(), dtype=int32)
print(tf.rank(a))  # tf.Tensor(0, shape=(), dtype=int32)
print(a.numpy())  # 5
print(tf.rank(a).numpy())  # 0
# [2] 벡터
b = tf.constant([5, 10, 15])  # 벡터 정의
print(b)  # tf.Tensor([5 10 15], shape=(3,), dtype=int32)
print(tf.rank(b))  # tf.Tensor(1, shape=(), dtype=int32)
print(b.numpy())  # [5 10 15]
print(tf.rank(b).numpy())  # 1
# [3] 행렬
c = tf.constant([[5, 10], [15, 20]])  # 행렬 정의
print(c)  # tf.Tensor([[5 10] [15 20]], shape=(2, 2), dtype=int32)
print(tf.rank(c))  # tf.Tensor(2, shape=(), dtype=int32)
print(c.numpy())  # [[5 10] [15 20]]
print(tf.rank(c).numpy())  # 2
# [4] 고차원 텐서
# 1. 2차원 텐서 만들기
mat1 = [[1, 2, 3, 4], [5, 6, 7, 8]]  # 2차원 리스트
mat2 = [[9, 10, 11, 12], [13, 14, 15, 16]]  # 2행 4열
mat3 = [[17, 18, 19, 20], [21, 22, 23, 24]]  # (2, 4)
# 2. 같은 축 방향으로 2차원 텐서 나열 -> 3차원 텐서
tensor1 = tf.constant([mat1, mat2, mat3])  # 리스트 3개를 하나의 리스트로 감싼다
# 3. 텐서 확인, 랭크 확인
print(tensor1)  # shape=(3, 2, 4), dtype=int32: 높이 3, 행 2, 열 4
print(tf.rank(tensor1))  # tf.Tensor(3, shape=(), dtype=int32)
# 4. 다른 방법
tensor2 = tf.stack([mat1, mat2, mat3])
print(tensor2)  # shape=(3, 2, 4), dtype=int32: 높이 3, 행 2, 열 4
print(tf.rank(tensor2))  # tf.Tensor(3, shape=(), dtype=int32)
# 5. 벡터로 3차원 만들기
vec1 = [1, 2, 3, 4]; vec2 = [5, 6, 7, 8]; vec3 = [9, 10, 11, 12]
vec4 = [13, 14, 15, 16]; vec5 = [17, 18, 19, 20]; vec6 = [21, 22, 23,24]
# 6. 3차원 텐서 만들기: [[], [], []]
tensor3 = tf.stack([[vec1, vec2], [vec3, vec4], [vec5, vec6]])  # 벡터 6개 -> 행렬 3개 -> 3차원 텐서 1개
print(tensor3)  # shape=(3, 2, 4), dtype=int32
print(tf.rank(tensor3))  # tf.Tensor(4, shape=(), dtype=int32)
# 7. 4차원 텐서 만들기 # [3차원 리스트, 3차원 리스트] (2, 3, 2, 4)
tensor4 = tf.stack([tensor1, tensor2])
print(tensor4)  # shape=(2, 3, 2, 4), dtype=int32
print(tf.rank(tensor4))  # tf.Tensor(4, shape=(), dtype=int32)
'''
# 벡터 4개
arr1 = []  # 벡터
arr2 = [] 
arr3 = []  
arr4 = []
# 행렬
arr5 = [arr1, arr2]  # [리스트, 리스트] = 2차원 리스트
arr6 = [arr3, arr4]  # [행 [열], [열]] = 2차원 리스트
# 3차원 텐서
tensor = [arr5, arr6]  # [행렬, 행렬] = 3차원 리스트
'''