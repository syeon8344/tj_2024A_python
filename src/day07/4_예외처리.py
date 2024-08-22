# day07 > 4_예외처리.py

# [1] try - else: 예외가 발생하지 않았을 때 실행되는 코드
try:
    age = int(input("나이를 입력하세요: "))
except:
    print("입력이 바르지 않습니다.")
else:
    # 예외가 발생하지 않으면 else부분이 실행된다
    if age <= 18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")

# [2] 예외 회피하기: pass, 예외 발생시 통과
try:
    f = open("없는파일", 'r')
except FileNotFoundError:
    pass


# [3] 예외 일부러 발생시키기: raise
# raise ArithmeticError  # 에러 강제 발생
class Bird:
    def fly(self):  # 하위 클래스가 해당 메서드를 오버라이드하지 않으면 예외 발생
        raise NotImplementedError


class Eagle(Bird):  # Eagle 클래스는 Bird 클래스로부터 상속받는다.
    def fly(self):  # 메서드 재정의하기
        print("fast")


e = Eagle()
e.fly()


# [4] 예외 만들기
class MyError(Exception):  # Exception 클래스로부터 상속
    def __str__(self):
        return "허용되지 않는 별명입니다."


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)

