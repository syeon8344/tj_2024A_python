# day06 > Task1.py
# [조건1] : 각 함수들 구현해서 프로그램 완성
# [조건2] :  1. 이름을 입력받아 여러명의 이름을 저장
#           2. 저장된 여러 이름을 모두 출력
#           3. 수정할 이름과 새로운 이름을 입력받아 수정
#           4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 전역변수 생성 X

# 전역 변수
names = "유재석,강호동,신동엽"
# 하나의 변수에 여러개의 이름을 저장하는 방법
# 변수: 하나의 자료를 저장하는 메모리 공간
# 하나의 자료에 여러 속성 담기: 1.객체 2.문자열(JSON) 3.리스트 4.튜플 5.딕셔너리
# 타입(자료 분류) vs 형식(자료 모양)
# "10": 문자열 타입, 숫자형식, 10: 정수 타입, 숫자형식
# "{key : value}": 문자열 타입, JSON형식, {key:value} : JSON/딕셔너리 타입, JSON/딕셔너리 형식
# CSV: 몇 가지 필드를 쉼표로 구분한 텍스트

# 함수 정의 -> def 함수명(매개변수들):
def name_create():
    global names  # 함수 안에서 전역변수 호출: global 전역변수명
    new_name = input("new_name : ")  # 저장할 새 이름 입력
    # 첫 등록이면 앞에 쉼표 없애기
    # 삼항연산: (true구문) if 조건문 else (false구문)
    names += f'{""if names.count(",") == 0 else ","}{new_name}'  # , : 여러 이름중에 이름 구분하는 구분문자(CSV)
    return
def name_read():
    # for 반복변수 in 리스트명:  # 리스트 내 요소 하나씩 반복변수에 대입, JS: 리스트명.forEach(반복변수 => {})
    # 문자열.split('특정문자'): 문자열 내 특정문자 기준으로 분해해서 리스트로 반환
    for name in names.split(','):
        print(f"name : {name}")  # f"문자열{코드}문자열" f포매팅, JS 백틱
    return
def name_update():
    global names  # 전역변수 호출
    # 문자열 내 문자를 다른 문자로 바꾸기
    # 문자열: 불변성, 부분 수정 X
    # 동일한 문자를 찾아 새로운 문자열로 변경
    old_name = input("old name : ")
    if names.find(old_name) == -1:
        return
    else:
        new_name = input("new name : ")
        # names = names.replace(old_name, new_name)
        # 문자열이 불변 -> 새 문자열을 생성해서 전역변수에 대입
        new_names = ""
        for name in names.split(','):  # 이름 하나씩 반복
            print(new_names)
            if name == old_name:  # 수정할 이름과 같으면
                new_names += f'{"," if new_names != "" else ""}{new_name}' # 새로운 이름
            else:
                new_names += f'{"" if new_names == "" else ","}{name}'  # 아니면 기존 이름
        names = new_names  # 새로 구성한 이름 명단을 전역변수에 대입
    return
def name_delete():
    global names
    # 동일한 문자를 찾아 ''로 변경
    delete_name = input("delete name : ")
    if names.find(delete_name) == -1:
        return
    else:
        # .replace('기존문자', '새로운문자'): 기존 문자가 있으면 새로운 문자로 치환해서 반환
        # if names.find(f",{delete_name}") >= 0:
            # names = names.replace(f",{delete_name}", "")
        # names = names.replace(delete_name, "")
        new_names = ''
        for name in names.split(','):
            if name == delete_name:
                continue  # 가장 가까운 반복문으로 이동
            else:
                new_names += f'{"," if new_names != "" else ""}{name}'

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