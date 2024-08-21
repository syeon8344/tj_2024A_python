# day06 > Task6.py
# 객체/리스트 활용
# [조건1] : 각 함수들 구현해서 프로그램 완성
# [조건2] :  1. 한명의 이름과 나이를 입력받아 객체 생성, 리스트에 여러명의 이름을 저장
#           2. 저장된 여러 이름과 나이를 모두 출력
#           3. 수정할 이름을 입력받아 존재하면 새로운 이름과 나이를 입력받아 수정
#           4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 전역변수 생성 X

# 전역 변수
names = []  # 객체를 담는 리스트


class NameAge:
    def __init__(self, name, age):  # self = 생성된 객체 자신
        self.name = name
        self.age = age


# 함수 정의 -> def 함수명(매개변수들):
def name_create():
    global names
    new_name = input("new name : ")
    new_age = int(input("new age : "))
    names.append(NameAge(new_name, new_age))
    return


def name_read():
    for o in names:
        print(f"name = {o.name}, age = {o.age}")
    return


def name_update():
    global names
    old_name = input("old name : ")
    updated = False  # 오류 메시지를 위한 체크 변수
    for o in names:
        if o.name == old_name:  # 객체마다 순회하며 찾는 값을 가진 객체가 있으면
            o.name = input("new name : ")
            o.age = int(input("new age : "))
            updated = True
            print("수정 완료.")
            return
    if not updated:
        print("이름이 존재하지 않습니다.")
    return


def name_delete():
    global names
    delete_name = input("delete name : ")
    deleted = False  # 오류 메시지를 위한 체크 변수
    for o in names:
        if o.name == delete_name:  # 객체마다 순회하며 찾는 값을 가진 객체가 있으면
            names.remove(o)
            deleted = True
            print("삭제 완료.")
            return
    if not deleted:
        print("이름이 존재하지 않습니다.")
    return


while True:  # :과 들여쓰기로 구분, true가 아니라 True 첫글자 대문자로 작성
    try:
        ch = int(input('1)Create 2)Read 3)Update 4)Delete : '))  # ch = 변수명, 타입 지정은 하지 않음 int(): 정수로 타입 변환 함수, input(): 입력함수, 입력받은 데이터를 문자열로 반환
    except Exception:
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
