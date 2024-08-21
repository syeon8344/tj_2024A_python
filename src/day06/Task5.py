# day06 > Task5.py
# 딕셔너리/리스트 이용, 파일처리 p.93 ~ p.101
# [조건1] : 각 함수들 구현해서 프로그램 완성
# [조건2] :  1. 이름과 나이를 입력받아 여러명의 이름을 저장
#           2. 저장된 여러 이름과 나이를 모두 출력
#           3. 수정할 이름 입력받고 있으면 새로운 이름과 나이를 입력받아 수정
#           4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 외 전역변수 생성 X
# [조건4] : 프로그램이 꺼져도 데이터가 남아있도록 파일처리
# 파일 내 데이터 설계 : 다수의 이름과 나이가 있을 떄 데이터 저장하는 방법 설계
# CSV : 필드 구분은 , 객체 구분은 \n : 유재석,20\n강호동,30
# 전역 변수
names = []  # 샘플 데이터


# def data_load():  # 파일 내 데이터 불러오기
#     global names
#     try:
#         f = open("name_age.txt", 'r')
#         while True:
#             line = f.readline().strip()  # 매 줄 읽어오기 + \n strip()으로 제거
#             print(line)
#             if not line:  # 읽어온 줄이 공백이면 무한루프 끝
#                 break
#             data_list = line.split(',')
#             names.append({'name': data_list[0], 'age': data_list[1]})
#
#     except FileNotFoundError:
#         f = open("name_age.txt", 'x')  # 파일 없음 오류 발생시 x 모드 (파일 생성 후 쓰기 모드)로 파일 열고 샘플 데이터 넣기
#         f.write("강호동,20")
#     finally:
#         f.close()


def data_load():
    global names
    f = open('name_age.txt', 'r')
    file = f.read()  # 파일 내용을 전부 읽어서 변수명에 대입
    # 문자열 -> 딕셔너리 후 리스트에 담기
    for line in file.split('\n')[:len(file.split(
            '\n')) - 1]:  # 읽어온 파일 내용 : 줄1\n 줄2\n 빈줄 -> split('\n')시 3개, 라인 2개여야 하므로 [0:\n으로 쪼갠 갯수 - 1]
        dic = {'name': line.split(',')[0], 'age': line.split(',')[1]}  # 해당 줄마다 쉼표로 분해, [0] 이름 [1] 나이
        names.append(dic)
    f.close()  # 파일 객체 닫기
    return


def data_save():  # 파일에 데이터 저장하기
    f = open("name_age.txt", mode='w')
    file_str = ""
    for dic in names:
        file_str += f"{dic['name']},{dic['age']}\n"
    f.write(file_str)
    f.close()


# 함수 정의 -> def 함수명(매개변수들):
def name_create():
    global names
    names.append({'name': input("새 이름을 입력해 주세요 : "), 'age': int(input("나이를 입력해 주세요 : "))})
    data_save()
    return


def name_read():
    global names
    for dic in names:
        print(f"name: {dic['name']}, age: {dic['age']}")
    return


def name_update():
    global names
    old_name = input("수정할 이름을 입력해 주세요 : ")
    updated = False
    for dic in names:
        if dic['name'] == old_name:
            dic['name'] = input("새 이름을 입력해 주세요 : ")
            dic['age'] = int(input("새 나이를 입력해 주세요 : "))
            data_save()
            print("수정 완료.")
            return
    if not updated:
        print("이름을 찾을 수 없습니다.")
    return


def name_delete():
    global names
    del_name = input("삭제할 이름을 입력해 주세요 : ")
    deleted = False
    for dic in names:
        if dic['name'] == del_name:
            names.remove(dic)
            data_save()
            deleted = True
            print("삭제 완료.")
            return
    if not deleted:
        print("이름을 찾을 수 없습니다.")
    return


data_load()
while True:  # :과 들여쓰기로 구분, true가 아니라 True 첫글자 대문자로 작성
    try:
        ch = int(input(
            '1)Create 2)Read 3)Update 4)Delete : '))  # ch = 변수명, 타입 지정은 하지 않음 int(): 정수로 타입 변환 함수, input(): 입력함수, 입력받은 데이터를 문자열로 반환
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
