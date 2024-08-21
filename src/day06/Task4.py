# day06 > Task4.py
# [조건1] : 각 함수들 구현해서 프로그램 완성
# [조건2] :  1. 이름을 입력받아 여러명의 이름을 저장
#           2. 저장된 여러 이름을 모두 출력
#           3. 수정할 이름과 새로운 이름을 입력받아 수정
#           4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 전역변수 생성 X

# 전역 변수
names = [{'name': "유재석"}, {'name': "강호동"}]  # 샘플 데이터

# 함수 정의 -> def 함수명(매개변수들):
def name_create():
    global names
    new_dict = {'name': input("new name : ")}
    names.append(new_dict)
    return
def name_read():
    for dic in names:
        print(f"name: {dic['name']}")
    return
def name_update():
    global names
    old_name = input("old name : ")
    updated = False
    for dic in names:
        if old_name == dic.get('name'):
            dic['name'] = input("new name : ")
            updated = True
            print("이름 수정 완료.")
    if not updated:
        print("이름이 존재하지 않습니다.")
    return
def name_delete():
    global names
    delete_name = input("delete name : ")
    deleted = False
    for dic in names:
        if delete_name == dic['name']:
            deleted = True
            names.remove(dic)
            print("이름 삭제 완료.")
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
