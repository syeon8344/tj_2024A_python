# day05 Task2.py
# 리스트 활용, p.77 ~ p.88
# [조건1] : 각 함수들 구현해서 프로그램 완성
# [조건2] :  1. 이름을 입력받아 여러명의 이름을 저장
#           2. 저장된 여러 이름을 모두 출력
#           3. 수정할 이름과 새로운 이름을 입력받아 수정
#           4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 전역변수 생성 X
names = []  # global 사용


def name_create():
    global names  # 전역 변수를 쓰겠다고 알려준다
    names.append(input("추가할 이름을 입력해주세요 : "))  # 리스트.append() : 마지막 위치에 요소 추가
    print("추가 완료.")
    return


def name_read():
    for name in names:  # 쉼표 표시 처리를 위한 if문
        if len(names) == 1:  # 리스트 요소가 하나일 때
            print(name)
            return
        elif names.index(name) + 1 == len(names):  # 리스트 내 요소가 여럿일 때 마지막 요소
            print(name)
            return
        else:  # 리스트 내 요소가 여럿이고 마지막 요소가 아닐 때
            print(name, end=", ")
    return


def name_update():
    global names
    updating_name = input("수정할 이름을 입력해 주세요 : ")
    if updating_name in names:
        new_name = input("새 이름을 입력해 주세요 : ")
        names[names.index(updating_name)] = new_name  # 바꿀 이름의 리스트 인덱스 확인 후 요소 교체
        print("수정 완료.")
    else:
        print("수정 실패, 이름을 다시 확인해 주세요.")

    return


def name_delete():
    global names
    deleting_name = input("삭제할 이름을 입력해 주세요 : ")
    if deleting_name in names:
        names.remove(deleting_name)  # 리스트.remove() : 해당 요소를 리스트에서 삭제
        print("삭제 완료.")
    else:
        print("삭제 실패, 이름을 다시 확인해 주세요.")
    return


while True:  # 무한루프
    ch = input('1)Create 2)Read 3)Update 4)Delete : ')
    if ch == "1":
        name_create()
    elif ch == "2":
        name_read()
    elif ch == "3":
        name_update()
    elif ch == "4":
        name_delete()
