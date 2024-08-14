# 3_함수.py
"""
    입력값을 가지고 어떤 일을 수행한 후 그 결과물을 내어놓는 것
    사용목적 : 1. 반복(재사용) 2. 기능 단위별 분리 (가독성 향상)
"""

# 1) 파이썬 함수의 구조
'''
(1) py
def 함수명 (매개변수1, 매개변수2)
    실행문
    return 반환값 또는 생략
(2) JS
function 함수명(매개변수, 매개변수){
    실행문
    return 반환값 또는 생략
}
(3) JAVA
반환타입 함수명(타입 매개변수, 타입 매개변수){

};
'''


# 2) 매개변수와 리턴값에 따른 함수 종류
# 1. 매개변수 O 리턴 0
def add(a, b):
    # {} 없으므로 들여쓰기 주의
    return a + b


# 함수 호출
a = add(a=3, b=4)
print(a)


# 2. 매개변수 X 리턴 O
# 함수 정의
def say():
    return "Hi"


# 함수 호출시 인수 전달이 없고 반환값을 받아 'a'에 저
a = say()
print(a)


# 3. 매개변수 O 리턴 X
# 함수 정의
def add(a, b):
    print(f"{a}, {b}의 값은 {a + b}입니다")


# 함수 호출시 인수 2개 전달하고 반환값은 없다
add(3, 4)


# 4. 매개변수 X 리턴 X
# 함수 정의
def say():
    print("Hi")


# 함수 호출 시 인수와 반환값이 모두 없다
say()


# 3) 매개변수를 지정하여 호출하기
def sub(a, b):
    # print(a, b) : 7, 3
    return a - b


# 함수 호출시 인수의 값을 대입할 매개변수명을 지정해서 호출
print(sub(b=3, a=7))


# 4) 입력값이 몇개가 될지 모를 때 : 가변 매개변수
# 1. *매개변수 : 갯수를 모르는 매개변수
def add_many(*args):  # 함수 정의, *매개변수 : 갯수를 모르는 매개변수
    print(args)  # 여러개의 매개변수 값이 들어있는 튜플
    result = 0  # 더한 값을 저장할 변수
    for i in args:  # 매개변수 튜플을 반복처리
        result += i  # 누적합계
    # for 종료후
    return result  # 함수 종료시 반환할 값


# 함수 호출
print(add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# 2. 특정 매개변수와 여러 매개변수일 시 특정 매개변수를 먼저 써준다
def add_mul(choice, *args):  # 특정 매개변수와 매개변수 여러개
    print(choice)
    print(args)
    if choice == 'add':  # 자료 매개변수 1개
        result = 0
        for i in args:  # 여러개의 자료를 가지는 튜플(매개변수)
            result += i  # 누적합
    elif choice == 'mul':  # else if가 아닌 elif
        result = 1
        for i in args:
            result *= i  # 누적곱
    return result  # 반환값


# 함수 호출
print(add_mul('add', 1, 2, 3, 4, 5, 6, 7))
print(add_mul('mul', 1, 2, 3, 4, 5, 6, 7))


# 5) 키워드 매개변수 kwargs : *은 튜플, **은 딕셔너리
def print_kwargs(**kwargs):
    print(kwargs)  # 딕셔너리 타입으로 매개변수를 받는다


# 함수 호출
print_kwargs(a=1)  # {'a': 1}, 인수로 전달시 키와 값으로 전달
print_kwargs(name='foo', age=3)  # {'name': 'foo', 'age': 3}


# 6) 함수의 리턴값은 항상 하나, 여러개일 경우 [],{},() 활용
# 1.
def add_and_mul(a, b):
    tup = 1, 2  # () 생략시 튜플로 생성된다
    print(tup)  # (1, 2)
    return a + b, a * b


# 함수 호출
result = add_and_mul(3, 4)
print(result)  # (7, 12) : 튜플 1개, 튜플 내 요소 2개


# 2. 동일한 수준의 return은 하나만 있어도 된다
def add_and_mul2(a, b):
    return a + b
    return a * b  # 위에 리턴이 있어 도달할 수 없다


# 3. 서로 다른 수준의 return은 공존 가능
def add_and_mul3(a, b):
    if a < 0:
        return  # a가 0보다 작으면 함수 강제 종료, 아래 코드 실행 막기
    return a + b


# 7) 매개변수에 초깃값 미리 설정하기, 함수 정의시 매개변수 디폴트값 설정하기
# 주의사항 : 초기화 하고 싶은 매개변수는 항상 뒤쪽에 놓여야 한다
# name, man=True, age X | name, age, man=True O
def say_myself(name, age, man=True):
    print(f"나의 이름은 {name}입니다.")
    print(f"나의 나이는 {age}살 입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


# 함수 호출
# 해당 매개변수 인자값이 없으면 디폴트 초깃값이 대입된다
say_myself("박응용", 27)  # 남자입니다
say_myself("박응용", 29, man=False)  # 여자입니다

# 8) 함수 안에서 선언한 변수의 효력 범위, 지역변수
# 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과 상관이 없다
a = 1  # 전역변수 'a'


def vartest(a):
    a += 1  # 지역변수 'a'의 값은 2, 함수 종료시 사라진다.


# 함수 호출
vartest(a)
print(a)  # 전역변수 'a'의 값을 확인

# 함수 안의 변수를 함수 밖에서 활용하는 방법, return 사용 권장
# 1. return *권장
a = 1


def vartest(a):
    a += 1
    return a


a = vartest(a)
print(a)  # 2

# 2. global 키워드
a = 1


def vartest():
    global a
    a += 1


vartest()
print(a)  # 2

# 3. 함수 밖에서 안으로는 접근 가능하지만 안에서 밖으로는 접근 불가
b = 1


def vartest():
    c = b + 1  # 함수 밖에 있는 b 변수를 함수 안에서 호출 : global 없이도 가능
    return c


b = vartest()
print(b)
