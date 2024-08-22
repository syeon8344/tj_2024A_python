# day07 > task07 > Main.py
# import될 경우에는 __name__이 __main__이 아니므로 실행되지 않을 부분
# 파일을 직접 실행하면 실행되는 구역, java main함수와 비슷하다
from User import NameAge  # NameAge 클래스 가져오기

# 전역 변수
names = []  # 객체를 담는 리스트


# 함수 정의 -> def 함수명(매개변수들):
def name_create():
    global names
    new_name = input("new name : ")
    new_age = int(input("new age : "))
    names.append(NameAge(new_name, new_age))
    return


def name_read():
    for obj in names:
        print(f"name = {obj.name}, age = {obj.age}")
    return


def name_update():
    global names
    old_name = input("old name : ")
    updated = False  # 오류 메시지를 위한 체크 변수
    for obj in names:
        if obj.name == old_name:  # 객체마다 순회하며 찾는 값을 가진 객체가 있으면
            obj.name = input("new name : ")
            obj.age = int(input("new age : "))
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
    for obj in names:
        if obj.name == delete_name:  # 객체마다 순회하며 찾는 값을 가진 객체가 있으면
            names.remove(obj)
            deleted = True
            print("삭제 완료.")
            return
    if not deleted:
        print("이름이 존재하지 않습니다.")
    return


if __name__ == "__main__":
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
