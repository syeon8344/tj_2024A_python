# 1_클래스.py
"""
    객체란? 논리적/물리적으로 정의된 실체
    클래스란? 객체를 물리적으로 표현하기 위한 설계도
    인스턴스란? 클래스를 이용해서 객체를 물리적으로(메모리상) 만든 실체

    JAVA :
    class Calculator{
        int result;  // 필드
        Calculator(){}  // 생성자
        int add( int num ){  // 메서드
            this.result += num
            return this.result
        }
    }
    JAVA 객체 :
    Calculator cal1 = new Calculator();
    Calculator cal2 = new Calculator();
    객체 메서드 호출:
    cal1.add(3)
"""


# [1] 파이썬 클래스 만들기
class Calculator:
    # 생성자 역할 (initializing)
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


# [2] 파이썬 객체 만들기 - 변수명 = 클래스명()
cal1 = Calculator()
cal2 = Calculator()
print(cal1)  # <__main__.Calculator object at 0x000002648B56D4F0>
print(cal2)  # <__main__.Calculator object at 0x000002648B56D460>

# [3] 파이썬 객체 내 메서드 호출
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# [4] 클래스의 생성자 정의


# (1) 과자 클래스 정의
class CookieCutter:
    # 파이썬은 기본적으로 다중생성자를 지원하지 않는다, __init__ 메서드는 1개
    # # 기본 생성자
    # def __init__(self):
    #     self.과자재료1 = None  # None = 데이터가 없다
    #     self.과자재료2 = None

    # 생성자 1 : 매개변수 2개를 갖는 생성자
    def __init__(self, 재료1, 재료2):  # __init__ : 생성자 역할을 하는 메서드
        # self : 해당 메서드를 실행하는 객체
        self.과자재료1 = 재료1  # self.필드명 = 매개변수: 매개변수로 필드값 초기화하기
        self.과자재료2 = 재료2  # self.필드명 = 매개변수: 매개변수로 필드값 초기화하기


# (2) 과자 객체 생성
var1 = CookieCutter('밀가루', '초코'); print(var1)  # <__main__.CookieCutter object at 0x00000264A7CDE060>
var2 = CookieCutter('밀가루', '치즈'); print(var2)  # <__main__.CookieCutter object at 0x00000264A7CDE0C0>
# (3) 객체 필드 호출: 객체변수명.필드명
print(var1.과자재료1)  # 밀가루, 첫번쨰 과자의 과자재료1 필드값 호출
print(var1.과자재료2)  # 초코, 첫번쨰 과자의 과자재료2 필드값 호출
print(var2.과자재료1)  # 밀가루, 두번째 과자의 과자재료1 필드값 호출
print(var2.과자재료2)  # 치즈, 두번째 과자의 과자재료2 필드값 호출
# (4) 객체의 필드값 수정
# var3 = CookieCutter(); print(var3)
var2.과자재료2 = '녹차'
print(var2.과자재료2)  # 녹차, 필드값 수정된 값
