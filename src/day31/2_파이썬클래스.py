# day31 > 2_파이썬클래스.py
# [1] 클래스 멤버가 없는 구조
# 1) 파이썬 클래스 정의
class Member:
    pass


# 2) 파이썬 객체 생성
m1 = Member()


# [2] 클래스 생성자(__init__) 가 있는 경우
# 1) 파이썬 클래스 정의
class User:
    def __init__(self,name):  # 생성자
        self.name = name  # 속성/필드 정의


# 2) 파이썬 객체 2개 생성
u1 = User("유재석")
u2 = User("강호동")


# [3] 클래스
class Student:
    def __init__(self, name):  # 생성자
        self.name = name  # name

    def __call__(self, val):
        print(self.name, val)


# 2) 파이썬 객체 생성
s1 = Student("유재석")
s2 = Student("강호동")
# call 함수 호출해보기: 객체변수명() <--- call 함수 호출
s1(10)  # 유재석 10
s2(20)  # 강호동 20
Student("신동엽")(30)  # call 함수는 call이라는 함수명을 생략하여 호출한다. (.call(30) X)
# 객체를 생성하고 바로 call 함수 호출, 출력값: 신동엽 30
s1(s2)  # 유재석  <__main__.Student object at 0x000001C4C2478110>

# ---> 딥러닝 신경망 모델에서 레이어들을 서로 연결 시 call 함수가 사용된다
# 새 래이어 클래스명(레이어속성명=속성값, 레이어속성명=속성값)(이전 레이어 객체 변수명)
# Functional API 구조
# 1. 입력 레이어 변수명 = 입력 레이어 클래스명(속성명=값)
# 2. 새로운 레이어 변수명 1 = 새로운 레이어 클래스명(속성명=값)(입력 레이어 변수명)