# 3_문자열.py

# [1] Python에서 문자열 사용하기
# 1. 큰따옴표
print("Hello World")
# 2. 작은따옴표
print('Python is Fun ')
# 3. 큰따옴표 3개
print("""Hello world""")
# 4, 작은따옴표 3개
print(' Hello World ')

# [2] 문자열 안에 작은 따옴표, 큰따옴표 표현할 때
print("Hello 'World!")
print("Hello 'World'")
# ''' 3개 또는 """ 3개로 문자열 출력 가능
print("""    
    Hello World
    """)
print(''' 
    Hello World
     ''')

# [3] 이스케이프 문자
print("Hello \"World\"")

# [4] 이스케이프 종류
''' 
\n 줄바꿈 
\t 들여쓰기 
\\ 백슬래시 출력 
\' 작은따옴표 출력 
\" 큰따옴표 출력
'''
# [5] 문자열 연산하기

# 1. 문자열 더해서 연결하기
print("Python" + " is fun")

# 2. 문자열 곱하기 (문자열 * 반복수)
print("Python" * 2)
print("=" * 50)
print("My Program")
print("=" * 50)

# 3. 문자열 길이, len(문자열) : 해당 문자열의 길이 반환하는 함수
print(len("Python"))

# 4. 문자열 인덱싱 : 문자열 내 문자 위치를 인덱스(번호)로 표현
# 인덱스는 왼쪽부터 0에서부터 시작, 오른쪽부터는 -1부터 시작
# P[0] y[1] t[2] h[3] o[4] n[5]
# [-6] [-5] [-4] [-3] [-2] [-1]
print("Python"[0])  # P, java : "Python".charAt(0)
print("Python"[2])  # t
print("Python"[4])  # o
# print("Python"[7]) IndexError: string index out of range
print("Python"[-1])  # n, 뒤에서부터 세는 인덱스
print("Python"[-3])  # h

# 5. 문자열 슬라이싱, 인덱싱 이용한 문자열 잘라내기
print("Python"[0:2])  # Py 인덱스 0부터 인덱스 2 전까지 : [0], [1] <--> java : "Python".subString(0,2)
print("Python"[:3])  # 앞부분 생략하면 0
print("Python"[2:6])  # thon, [2]부터 [6] 바로 전까지 ( [5] )
print("Python"[2:])  # 뒷부분 생략하면 문자열 끝까지
print("Python"[:])  # Python, [0]부터 끝까지
print("Python"[2:-1])  # tho, [2]부터 [-1] 전까지
print("Python"[-5:3])  # yt, [-5]부터 [3] 전까지
# 활용 1.
date = "2024-08-12"
print(date[0:4])  # 2024, [0]부터 [3]까지, ([4]는 포함 X)
print(date[5-7])  # 08, [5], [6]
print(date[8-10])  # 12, [8], [9]

# 6. 문자열 포매팅, python3.6이상부터 가능
# f(접두사) 붙이고 ''문자열 안에서 {} 이용한 연산 가능
# {데이터 :<자릿수} : 왼쪽 정렬
# {데이터 :>자릿수} : 오른쪽 정렬
# {데이터 :^자릿수} : 가운데 정렬
# {데이터:[공백문자][정렬기호][자릿수]}
# {데이터:[총자릿수].[소수자리수]f}, 표현 자리 바로 뒤에서 반올림
print(f"나의 이름은 {'홍길동'}. 나이는{30} 입니다")
print(f"나의 이름은 {'홍길동' + '님'}. 나이는{30+1} 입니다")
print(f"{"Python":>10}")  # 왼쪽 정렬, 10칸 차지
print(f"{"Python":<10}")  # 오른쪽 정렬, 10칸 차지
print(f"{"Python":^10}")  # 가운데 정렬, 10칸 차지, 빈칸은 공백문자
print(f"{"Python":=^10}")  # 가운데 정렬, 10칸 차지, 빈칸은 "="
print(f"{3.14159:0.2f}")  # 3.14, 소수점 둘째자리까지 표현
print(f"{3.14159:5.3f}")  # 3.142, 소수점 셋째 자리까지 표현
print(f"{"{'Python'}"}")  # {'Python'}

print(f"{'python':!^12}")  # !!!python!!!
