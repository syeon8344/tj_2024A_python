# day07 > task08 > Main.py
"""
    User.py: User 정보를 가지는 클래스 정의
    File.py: save(), load() 함수를 정의
    [조건1] 이름과 나이 입력받아 저장
    [조건2] 프로그램이 종료되고 다시 실행되어도 names 데이터 유지
    -> 리스트에 User 객체만 들어가고 나오도록
"""
from File import save, load
from User import User

# 전역 변수
names = []  # 객체를 담는 리스트


# 함수 정의 -> def 함수명(매개변수들):
def name_create():
    new_name = input("new name : ")
    new_age = int(input("new age : "))
    u = User(new_name, new_age)
    names.append(u)
    save(names)
    print("added")
    return


def name_read():
    if not names:
        return
    for user in names:
        print(f"name: {user.name}, age: {user.age}")
    return


def name_update():
    old_name = input("old name : ")
    for user in names:
        if user.name == old_name:
            new_name = input("new name : ")
            new_age = input("new age : ")
            user.name = new_name
            user.age = new_age
            print("updated")
            return
    print("name not found")
    return


def name_delete():
    del_name = input("delete name : ")
    for user in names:
        if user.name == del_name:
            names.remove(user)
            print("deleted")
            return
    print("name not found")
    return


if __name__ == "__main__":
    names = load()
    while True:  # :과 들여쓰기로 구분, true가 아니라 True 첫글자 대문자로 작성
        try:
            # ch = 변수명, 타입 지정은 하지 않음 int(): 정수로 타입 변환 함수, input(): 입력함수, 입력받은 데이터를 문자열로 반환
            ch = int(input('1)Create 2)Read 3)Update 4)Delete : '))
        except ValueError:
            continue
        if ch == 1:  # if 조건문
            # 주의점: 들여쓰기
            name_create()
        # 들여쓰기 1번: while문
        # 들여쓰기 2번: if문에 포함
        elif ch == 2:
            name_read()
        elif ch == 3:
            name_update()
        elif ch == 4:
            name_delete()
