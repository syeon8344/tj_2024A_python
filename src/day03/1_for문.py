# 1_for문.py
#   while문과 비슷한 반복문
#   for문은 한눈에 들어오는 장점이 있다

# 1) for문의 기본 구조
"""
for 변수 in 리스트/튜플/문자열:
    실행문;
"""

# 141p 예제
test_list = ['one', 'two', 'three']
# 'test_list' 변수가 ['one', 'two', 'three']를 참조
# JS : let test_list = ['one', 'two', 'three']
for i in test_list:
    # : 다음의 실행문 작성시 띄어쓰기 주의, { }는 없음
    # 리스트 내 문자열을 하나씩 문자열 타입으로 반환해서 반복처리한다
    print(i)
'''
(JS)
let test_list = ['one', 'two', 'three']
test_list.forEach( i => {
    console.log(i);
})
'''

# 142p 예제
a = [(1, 2), (3, 4), (5, 6)]
# [1, 2, 3] : 리스트 타입 ( 여러 요소를 저장 , 요소 수정/삭제 가능 )
# (1, 2, 3) : 튜플 타입 ( 여러 요소를 저장, 요소 수정/삭제 불가 = 고정값 )
for (first, last) in a:
    # 리스트 내 튜플을 하나씩 (요소1, 요소2) 튜플 타입으로 반환해서 반복처리한다
    print(first + last)

# 143p, 144p 예제
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    # 띄어쓰기 주의
    number += 1  # 학생 번호 1 증기
    if mark >= 60:  # 값이 60 이상이면
        print(f"{number}번 학생은 합격입니다.")
    else:
        print("%d번 학생은 불합격입니다." % number)
    # 파이썬 if 조건문에는 { }가 없다

# 2) continue : 가장 가까운 for문의 처음으로 돌아가는 키워드
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue  # 가장 가까운 for문으로 이동, 아래 코드는 실행되지 않음
    print(f"{number}번 학생 축하합니다. 합격입니다.")

# 3) range() : 숫자 리스트를 생성해서 반환하는 함수
# range(숫자) : 0부터 숫자 *미만까지 포함하는 range 객체 생성
# range(시작, 끝숫자) : 시작숫자부터 끝 미만까지 포함하는 range 객체 생성
# range(시작, 끝, 증감식) : 시작숫자부터 끝 미만까지 증감식 적용한 range 객체 생성
a = range(10)
print(a)  # 0 1 2 3 4 5 6 7 8 9
a = range(1, 11)
print(a)  # 1 2 3 4 5 6 7 8 9 10

# 예제
for val in range(10):  # 0~9
    print(val, end=' ')  # print( ... , end='') : 줄바꿈 처리를 하지 않는 출력문 (기본값 = \n)
print()  # 예제 구분 \n
for val in range(1, 11):  # 1~10
    print(val, end=' ')
print()
for val in range(1, 11, 2):  # 1~10 2씩 증가 - 1, 3, 5, 7, 9
    print(val, end=' ')

# 예제 2, 1부터 10까지 누적합계 구하기
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

# 예제 3, 1부터 100까지 누적합계 구하기
num = 0
for n in range(1, 101):
    num += n
print(num)

# 예제 4. 구구단
for i in range(2, 10):  # 단 출력, 2~9
    print(f"{i}단", end=' | ')
    for j in range(1, 10):  # 곱 출력, 1~9 : 단마다 곱 루프 중첩
        print(f"{i * j:<2}", end=' ')
    print()

# 4) 리스트 컴프리헨션 사용
# [표현식 for 항목 in 반복가능객체 if 조건문]
# [연산식 for 반복변수 in 리스트 if 조건문]
# 2개 이상
# [표현식 for 항목 in 반복가능객체 if 조건문
#        for 항목 in 반복가능객체 if 조건문]
# 1.
a = [1, 2, 3, 4]
result = [n * 3 for n in a]
# [] 안에서 for문 사용
# [for 반복변수 in 리스트명]
# 반복되는 n값을 하나씩 리스트 요소로 대입해 리스트 생성
print(result)

# 3. 기존 리스트를 반복문 활용해서 새로운 리스트 생성
print([i for i in a])  # java : 리스트명.map()
# 4.
result = [n for n in a if n % 2 == 0]
print(result)
# 5. 2개 이상, 구구단 예시
result = [x * y for x in range(2, 10)
          for y in range(1, 10)]
print(result)
