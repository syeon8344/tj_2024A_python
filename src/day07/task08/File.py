# day07 > task08 > File.py

from User import User


def save(names):
    # 1. 쓰기 모드 파일 객체
    f = open("data.txt", 'w')
    # 2. 내용 구성
    data = ""
    for user in names:  # 객체를 문자열로 변환
        data += f"{user.name},{user.age}\n"
    # 3. 출력 및 닫기
    f.write(data)
    f.close()
    return True


def load():
    # 1. 읽기 모드 파일 객체
    try:
        f = open("data.txt", 'r')
    # 처음에 파일 없을 시 예외 발생 -> 예외가 발생했을 때 실행되는 구역
    except FileNotFoundError:
        f = open("data.txt", 'x')
        f.close()
        return []  # 빈 리스트 반환
    # 2. 읽어오기
    names = []
    while True:
        # 파일 줄마다 line 변수에 대입, \n 제거
        line = f.readline().strip()
        if not line:
            break
        data = line.split(",")
        u = User(data[0], data[1])
        names.append(u)
    f.close()
    return names
