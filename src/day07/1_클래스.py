# day07 > 1_클래스.py
# 클래스: 객체를 실체화하기 위한 설계도
# 인스턴스: 객체가 메모리에 실체화된 것
# 객체: 추상적 개념, 물리적 개념으로 고유 성질(변수)과 행위(함수)를 정의한 것
# [1] 클래스 구조 만들기
# 1) 간단한 클래스
class FourCal:
    pass  # 아무것도 수행하지 않는 문법, 임시로 코드 작성시 주로 사용된다


# 2) 객체 생성, 클래스명()
a = FourCal()
print(type(a))  # <class '__main__.FourCal'>, type(): 변수의 타입을 반환하는 함수


# [2] 클래스 내 메서드(함수) 만들기
# 1) 클래스 내 메서드 선언
class FourCal:
    # 생성자, 다중생성자는 없다
    def __init__(self, first, second):
        self.first = first
        self.second = second

    # 함수 코드는 객체들이 공유해서 사용하므로 self키워드로 자신을 구분
    def set_data(self, first, second):  # 함수/메서드 정의, 매개변수: 함수 호출시 전달되는 인자값을 저장하는 변수
        self.first = first  # self: 객체 자신, first 필드와 값이 객체변수로 생성됨
        self.second = second  # 함수 호출한 객체 내 second 변수를 선언하고 매개변수를 저장

    def add(self):
        return self.first + self.second  # return: 함수 종료시 함수를 호출했던 곳으로 반환되는 값

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.second

    def div(self):
        return self.first / self.second


# 2) 객체 생성
# a = FourCal()
# 객체내 메서드 실행
# a.set_data(4, 2)  # self = a, first = 4, second = 2
# FourCal.set_data(a, 4, 2)  # 클래스명 먼저 쓰면 변수명도 매개변수로 전달
# 객체내 필드 값 호출
# print(a.first)
# print(a.second)
# print(a.add()); print(a.mul()); print(a.sub()); print(a.div())
# 3) 객체 생성, a 객체와 b 객체는 타입만 같고 서로 다르다.
# b = FourCal()
# b.set_data(3, 7)
# print(b.first)
# print(b.second)

# 4) 객체 생성, 생성자 매개변수
c = FourCal(4, 2)


# [4] 상속
# 1) 하위 클래스 정의: class 클래스명(상위클래스명)
class MoreFourCal(FourCal):
    # 메서드 정의
    def pow(self):
        return self.first ** self.second
    # 오버라이딩: 상위클래스의 메서드 재정의
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/ self.second

# 2) 하위 클래스로 객체 생서
a = MoreFourCal(4, 2)
print(type(a))  # <class '__main__.MoreFourCal'>
print(a.add())  # 6

print(a.pow())  # 본인 클래스의 메서드 호출

# [5] 클래스 변수
# 객체 변수: 객체마다 사용되는 변수, 필드, 멤버변수라고도 한다
# 클래스 변수: 클래스명.변수명(), 모든 객체가 공유해서 사용하는 변수
# 객체변수와 클래스변수의 이름이 같아도 식별이 가능하다


class Family:
    last_name = "김"


print(Family.last_name)  # 김
a = Family()
print(a.last_name)
b = Family
print(b.last_name)  # 김
Family.last_name = '박'
print(a.last_name); print(b.last_name);  # 박, 박