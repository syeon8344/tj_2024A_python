# 4_사용자_입출력.py
""""""

# 1) 사용자 입력 : input()
# input('안내문구')
# 콘솔에 입력받은 값을 문자열(str)로 반환
# 타입 확인 함수 : type(자료)
# 타입 변환 함수 : int(), float(), list(), ...
'''
a = input()  # JS : prompt(), JAVA : scanner
print(a)
num = input("숫자를 입력하세요")
print(num)
print(type(num))
'''
# 2) print() 자세히 보기
# print(리터럴 / 변수명 / 연산식)
# print(f"문자열 {리터럴 / 변수명 / 연산식} 문자열") : f포메팅 (~~ 백틱)
# print(리터럴 / 변수명 / 연산식, end="출력후 대입할 문자열, 기본값 : \n")
print(123)  # 숫자 출력
print("Python")  # 문자열 출력
print([1, 2, 3])  # 리스트 출력
# + 연산자를 이용한 문자열 연결 = 띄어쓰기 없음
print('python' + 'is fun')  # pythonis fun
# , = 띄어쓰기 연결
print('python', 'is fun')  # python is fun
# 출력후 결과값 변경하기 : 줄바꿈 대신에 다른 문자열 쓰기
print('python', end=" ")  # end="\n"이 기본값이지만 변경 가능
print('is fun')
