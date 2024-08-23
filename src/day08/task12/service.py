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
    # 데이터 CSV상 순서 (인덱스 찾기용)
    # "X","시군구","X","X","X","단지명","전용면적(㎡)","계약년월","계약일","거래금액(만원)[금액1,금액2]","동","층","X","X","X","X","X","X","X","X"
    contract_amount = ''.join([line[9], line[10]])
    data.append({"location": line[1], "name": line[5], "area": line[6],
                 "year_month": line[7], "day": line[8],"contract_amount": contract_amount, "bldg_no": line[11], "floor": line[12]})  # data 리스트에 line 추가
print(data)

# [4] 단지명 별로 거래량 계산해서 거래량이 많은 단지명 TOP10 출력
def top_ten_transaction():
    top_list = []  # 출력할 거래량 순위 목록
    complex_name = []  # 단지명 리스트


    return