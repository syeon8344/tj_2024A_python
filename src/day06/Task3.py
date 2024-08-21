# day06 > Task3.py
# [조건1] : 각 함수들 구현해서 프로그램 완성
# [조건2] :  1. 이름을 입력받아 여러명의 이름을 저장
#           2. 저장된 여러 이름을 모두 출력
#           3. 수정할 이름과 새로운 이름을 입력받아 수정
#           4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 전역변수 생성 X

# 전역 변수
names = ("유재석", "강호동")  # 샘플 데이터
# 튜플: 리스트와 비슷하지만 요소의 삽입/삭제가 불가능
# 리터럴과 같이 불변성을 가진다

# 함수 정의 -> def 함수명(매개변수들):
def name_create():
    global names
    new_name = input("new name : ")
    # 기본적으로 반복 가능한 요소는 튜플로 만들면 반복해서 튜플 요소로 생성 -> ('유', '재', '석'), 방지하려면 요소 하나임을 쉼표를 붙여 표시
    # 튜플은 불변이므로 새 튜플을 만들어 이름을 붙여 변수에 대입
    names += (new_name,)
    return
def name_read():
    print(names)
    for name in names:
        print("name : " + name)
    return
def name_update():
    global names
    old_name = input("old name : ")
    new_names = ()  # 튜플은 불변이므로 새 튜플을 만들어 이름을 붙여 변수에 대입
    updated = False
    for name in names:
        if name == old_name:  # 수정될 이름
            new_name = input("new name : ")
            new_names += new_name,
            updated = True  # 안내 메시지를 위한 수정 여부 불린 변수
            print("이름 수정 완료.")
            continue
        new_names += name,
    names = new_names
    if not updated:
        print("이름이 존재하지 않습니다.")
    return
def name_delete():
    global names
    del_name = input("delete name : ")
    if names.count(del_name) == -1:
        print("이름이 존재하지 않습니다.")
        return
    else:
        new_names = ()  # 튜플은 불변이므로 새 튜플을 만들어 이름을 붙여 변수에 대입
        for name in names:
            if name == del_name:
                print("이름 삭제 완료.")
                continue
            else:
                new_names += name,
        names = new_names
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
