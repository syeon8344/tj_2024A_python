# day05 Task1.py
# 문자열 활용, p.50 ~ p.76
# [조건1] : 각 함수들 구현해서 프로그램 완성
# [조건2] :  1. 이름을 입력받아 여러명의 이름을 저장
#           2. 저장된 여러 이름을 모두 출력
#           3. 수정할 이름과 새로운 이름을 입력받아 수정
#           4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 전역변수 생성 X
# [조건4] : 최대한 리스트 타입 사용하지 않기

# 하나의 변수에 여러 가지 정보 : 1. JSON [키:값] 2. CSV [,] 주로 문자열 타입 사용
# "aaa,bbb,ccc"

names = ""  # 여러개의 name을 저장하는 문자열, global 사용 X


def name_create():
    name_input = input("이름을 입력해주세요 : ")
    if names == "" or None:  # names가 비어있거나 None이면 바로 새 이름 반환
        print("이름 추가 완료.")
        return name_input
    else:  # names가 비어있지 않으면 ", "을 붙여 새 이름 목록 names를 반환
        new_names = names + ", " + name_input
        print("이름 추가 완료.")
        return new_names


def name_read():
    print(names)  # names를 출력
    return


def name_update():
    global names
    name_input = input("이름을 입력해주세요 : ")
    if names.count(name_input) >= 1:  # 이름이 names 문자열 안에 있으면 .count()가 1 이상, .replace(바꿀 문자열, 새 문자열)
        new_names = names.replace(name_input, input("새 이름을 입력해주세요 : "))
        print("이름 수정 완료.")
        return new_names
    else:
        print("이름이 존재하지 않습니다.")
    return


def name_delete():
    name_input = input("이름을 입력해주세요 : ")
    if ", " + name_input in names:  # 첫번째로 목록의 중간 이름인지 확인 (a, 삭제할이름, b)
        new_names = names.replace(", "+name_input, "")
        print("이름 삭제 완료.")
        return new_names
    elif name_input in names:  # 두번째로 목록의 첫번째 이름인지 확인
        new_names = names.replace(name_input, "")
        print("이름 삭제 완료.")
        return new_names
    else:
        print("이름이 존재하지 않습니다.")
    return


while True:  # 무한루프
    ch = input('1)Create 2)Read 3)Update 4)Delete : ')
    if ch == "1":
        names = name_create()
    elif int(ch) == 2:
        name_read()
    elif ch == "3":
        names = name_update()
    elif ch == "4":
        names = name_delete()
