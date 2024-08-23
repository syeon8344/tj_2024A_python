# day08 > task12 > service.py
import datetime

f = open("아파트(매매)_실거래가_20240823.csv", 'r')
data = []

while True:  # 안내문 부분 잘라내기
    line = f.readline().strip().strip("\"").split("\",\"")
    if line[0] == "NO":  # 데이터 제목 부분 : 안내문 마지막 부분까지 읽어서 버리고 루프 끝
        break
while True:  # 데이터 부분
    # 한 문장씩 읽고 / "\n" 제거 / 큰따옴표 제거 / 쉼표 단위로 나눠 리스트 형태로 line 변수명에 대입
    line = f.readline().strip().strip("\"").split("\",\"")
    if line == ['']:  # 공백이면 끝
        break
    # 데이터 CSV상 순서 (인덱스 찾기용)
    # "X","시군구","X","X","X","단지명","전용면적(㎡)","계약년월","계약일","거래금액(만원)[**금액1,금액2]","X","층","X","X","X","X","X","X","X","X"
    line[9] = "".join(line[9].split(','))
    data.append({"location": line[1], "name": line[5], "area": line[6], "year_month": line[7], "day": line[8],
                 "contract_amount": line[9], "floor": line[11]})  # data 리스트에 line 추가
print(data)

# 결과 데이터
# {'location': '인천광역시 서구 청라동', 'name': '호반베르디움앤영무예다음', 'area': '59.8600', 'year_month': '202308', 'day': '24', 'contract_amount': '44700', 'floor': '19'}

# [4] 단지명 별로 거래량 계산해서 거래량이 많은 단지명 TOP10 출력
def top_ten_transaction():
    top_list = []  # 출력할 거래량 순위 목록
    complex_name = []  # 단지명 리스트

    return


# [5] 년 월 별 거래량과 전월대비 증감 계산


# [6] 가장 거래가 많은 요일 계산 및 출력
def weekday_most_transactions():
    year_month = []
    day = []
    weekday_transactions = [0, 0, 0, 0, 0, 0, 0]
    for row in data:
        year_month.append(row['year_month'])
        day.append(row['day'])
    datetime.datetime.strptime('January 11, 2010', '%B %d, %Y').strftime('%A')
