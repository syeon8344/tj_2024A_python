# day25 > 1_텐서플로.py
"""
    텐서플로: 텐서(다차원 데이터)의 flow(흐름)에 따라 연산하는 과정 제공 라이브러리
"""
# [1] 텐서플로 설치 및 가져오기
import tensorflow as tf
import numpy as np

# [2] 텐서플로 2 즉시 실행 모드인지 확인
print(tf)  # 모듈
print(tf.executing_eagerly())

# [3] 텐서플로 연산
a, b = 1, 2
c = tf.math.add(a, b)  # 텐서플로 수학 모듈의 add 함수
print(c)  # tf.Tensor(3, shape=(), dtype=int32): 텐서 객체로 반환됨
print(type(c))  # <class 'tensorflow.python.framework.ops.EagerTensor'>

# [4] 텐서 객체에서 결과값 추출: .numpy()
print(c.numpy())  # 3

# [5] 텐서: 스칼라 (상수): tf.Tensor(값, shape=(배열크기), dtype=타입)
# 1. 스칼라 정의
a, b = tf.constant(1), tf.constant(2)
print(a, b)  # tf.Tensor(1, shape=(), dtype=int32), tf.Tensor(2, shape=(), dtype=int32)
# 2. 랭크 확인: tf.rank(텐서 객체)
print(tf.rank(a), tf.rank(b))  # tf.Tensor(0, shape=(), dtype=int32)
# 3. 스칼라 데이터 타입 변환: tf.cast(스칼라객체, tf.타입)
a = tf.cast(a, tf.float32)  # a 스칼라 객체 값 타입을 실수로 변환
b = tf.cast(b, tf.float32)
print(a, b)  # tf.Tensor(1.0, shape=(), dtype=float32)
# 4. 수학 함수: tf.math
# 1) tf.math.add(): 덧셈
c = tf.math.add(a, b)
print(c)  # tf.Tensor(3.0, shape=(), dtype=float32)
print(tf.rank(c))  # tf.Tensor(0, shape=(), dtype=int32)
# 2) tf.math.subtract(): 뺄셈 (= a - b)
print(tf.math.subtract(a, b))  # tf.Tensor(-1.0, shape=(), dtype=float32)
# 3) tf.math.divide(): 나눗셈 (= a / b)
print(tf.math.divide(a, b))  # tf.Tensor(0.5, shape=(), dtype=float32))
# 4) tf.math.multiply(): 곱셈 (= a * b)
print(tf.math.multiply(a, b))  # tf.Tensor(2.0, shape=(), dtype=float32)
# 5) tf.math.mod(): 나눗셈의 나머지 (= a % b)
print(tf.math.mod(a, b))  # tf.Tensor(1.0, shape=(), dtype=float32)
# 6) tf.math.floordiv(): 나눗셈의 몫 (= a // b)
print(tf.math.floordiv(a, b))  # tf.Tensor(0, shape=(), dtype=int32)

# [6] 텐서: 벡터 (1차원 리스트): tf.Tensor( , shape=(원소개수,), dtype=)
# 벡터 정의
vec1 = tf.constant([10, 20, 30], dtype=tf.float32)  # 파이썬 리스트
vec2 = tf.constant(np.array([10, 20, 30]), dtype=tf.float32)  # numpy 배열
print(vec1)  # tf.Tensor([10 20 30], shape=(3,), dtype=float32)
print(vec2)  # tf.Tensor([10 20 30], shape=(3,), dtype=float32)
# 랭크 확인
print(tf.rank(vec1))  # tf.Tensor(1, shape=(), dtype=float32)
print(tf.rank(vec2))  # tf.Tensor(1, shape=(), dtype=float32)
# 벡터 연산
print(vec1 + vec2)  # 덧셈
print([10, 20, 30] + [10, 20, 30])  # 리스트가 계산되지 않고 연결된다
print(vec1 - vec2)  # 뺄셈  # tf.Tensor([0. 0. 0.], shape=(3,), dtype=float32)
print(vec1 * vec2)  # 곱셈  # tf.Tensor([100. 400. 900.], shape=(3,), dtype=float32)
print(vec1 / vec2)  # 나눗셈  # tf.Tensor([1. 1. 1.], shape=(3,), dtype=float32)
print(vec1 % vec2)  # 나눗셈 몫  # tf.Tensor([0. 0. 0.], shape=(3,), dtype=float32)
print(vec1 // vec2)  # 나눗셈 나머지  # tf.Tensor([1. 1. 1.], shape=(3,), dtype=float32)
print(vec1 ** 2)  # 거듭제곱, tf.math.square()  # tf.Tensor([100. 400. 900.], shape=(3,), dtype=float32)
print(vec2 ** 0.5)  # 제곱근, tf.math.sqrt()  # tf.Tensor([3.1622777 4.472136  5.477226 ], shape=(3,), dtype=float32)
# 벡터 요소들의 합
print(tf.reduce_sum(vec1))  # tf.Tensor(60.0, shape=(), dtype=float32)
print(vec1 + 1)  # 브로드캐스팅 연산, 각 요소마다 1 더하기  # tf.Tensor([11. 21. 31.], shape=(3,), dtype=float32)

# [7] 텐서: 배열 (2차원 리스트: 행렬): tf.Tensor([[][]], shape(행개수(벡터 개수), 열개수=벡터내 원소 개수), dtype=)
mat1 = tf.constant([[10, 20], [30, 40]])  # 큰 대괄호 내 원소개: 행개수/벡터개수
print(mat1)
"""
tf.Tensor(
[[10 20]
 [30 40]], shape=(2, 2), dtype=int32)
"""
# 랭크 확인
print(tf.rank(mat1))  # tf.Tensor(2, shape=(), dtype=int32))
# mat2 = tf.stack(벡터, 벡터)
mat2 = tf.stack([[1, 1], [-1, 2]])  # 1차원 리스트 2개를 2차원으로 변환
print(mat2)
print(tf.rank(mat2))  # tf.Tensor(2, shape=(), dtype=int32)
# 행렬 연산
print(mat1 * mat2)  # tf.Tensor([[10, 0], [-30, 80]], shape=(2, 2), dtype=int32)
print(mat1 + mat2)
print(mat1 - mat2)
print(mat1 / mat2)
# print(mat1 % mat2)  # GPu 계산시 %연산자 X
# print(tf.math.mod(mat1, mat2))
# print(mat1 // mat2)
print(tf.math.multiply(mat1, 3))  # 브로드캐스팅
# 행렬의 행(가로줄) 열(세로줄) 곱연산
# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# tf. matmul(A, B):
# [[(1*5 + 2*7), (1*6 + 2*8)], [(3*5 + 4*7), (3*6 + 4*8)]]
print(tf.matmul(mat1, mat2))
"""
    tf.Tensor(
    [[-10  40]
     [-10  80]], shape=(2, 2), dtype=int32)
"""

"""
    인공지능(AI)
        - 빅데이터: 많은 자료들
        - 머신러닝: 자료들의 학습 모델 (scikit-learn)
        - 딥러닝: 복잡한 자료들의 학습 모델 (tenserflow 라이브러리)
    
    텐서플로 자료구조
    
    스칼라     벡터        매트릭스(행렬)      텐서
    rank-0    rank-1      rank-2             rank-3
    값        리스트       2차원 리스트        3차원 리스트
    차수-0    차수(축)-1   차수-2             차수-3
    x         단방향 x     가로(|)x 세로(-)y  가로(|)x 세로(-)y 높이(z) 
"""