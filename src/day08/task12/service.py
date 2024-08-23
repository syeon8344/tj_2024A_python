# day08 > task12 > service.py
f = open("아파트(매매)_실거래가_20240823.csv", 'r')
data = []

while True:  # 안내문 부분 잘라내기
    line = f.readline().strip().replace("\"","").split(",")
    print(line)
    if line[0] == "NO":  # 데이터 제목 부분 : 안내문 마지막 부분까지 읽어서 버리고 루프 끝
        break
while True:  # 데이터 부분
    # 한 문장씩 읽고 / "\n" 제거 / 큰따옴표 제거 / 쉼표 단위로 나눠 리스트 형태로 line 변수명에 대입
    line = f.readline().strip().replace("\"","").split(",")
    if line == ['']:  # 공백이면 끝
        break
    data.append(line)  # data 리스트에 line 추가


for row in data:


def getall():



    return