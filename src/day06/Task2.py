# day06 > Task2.py
# [조건1] : 각 함수들 구현해서 프로그램 완성
# [조건2] :  1. 이름을 입력받아 여러명의 이름을 저장
#           2. 저장된 여러 이름을 모두 출력
#           3. 수정할 이름과 새로운 이름을 입력받아 수정
#           4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 전역변수 생성 X

# 전역 변수
# 리스트 : 여러개의 자료들을 인덱스로 구분해서 하나의 리스트 자료로 구성
names = ["유재석", "강호동"]  # 샘플 데이터

# 함수 정의 -> def 함수명(매개변수들):
def name_create():
    global names
    names.append(input("new name : "))
    return
def name_read():
    for name in names:
        print("name : " + name)
    return
def name_update():
    global names
    old_name = input("old name : ")
    if old_name in names:
        names[names.index(old_name)] = input("new name : ")
        print("이름 수정 완료.")
    else:
        print("이름이 존재하지 않습니다.")
    return
def name_delete():
    global names
    try:  # try/error in Python : try/except/else/finally, try: 시험할 코드
        names.remove(input("remove name : "))
    except ValueError:  # execpt 오류명: 캐치할 오류명 및 오류 발생시 실행할 코드
        print("이름이 존재하지 않습니다.")
        return
    else:  # else: 오류가 없을 때 실행할 코드
        print("이름 삭제 완료.")
        return
    finally:  # finally: 무조건 실행할 코드
        return

while True:  # :과 들여쓰기로 구분, true가 아니라 True 첫글자 대문자로 작성
    ch = int(input('1)Create 2)Read 3)Update 4)Delete : '))  # ch = 변수명, 타입 지정은 하지 않음 int(): 정수로 타입 변환 함수, input(): 입력함수, 입력받은 데이터를 문자열로 반환
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
