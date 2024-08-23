# day08 > task12 > service.py
import datetime
import locale

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


# 결과 데이터
# {'location': '인천광역시 서구 청라동', 'name': '호반베르디움앤영무예다음', 'area': '59.8600', 'year_month': '202308', 'day': '24', 'contract_amount': '44700', 'floor': '19'}




# [1] 인천광역시 아파트 실거래가의 모든 내역 정보 출력하시오.
def getall():
    return data

# [2] 가장 높은 거래금액 과 가장 낮은 거래금액의 해당 하는 거래의 시군구,단지명,전용면적 출력
def max_min_list():
    newList = []
    for dic in data:
        newList.append(int(dic['contract_amount']))
    maxValue = max(newList)
    minValue = min(newList)
    print(maxValue)
    max_min_list = []
    maxlist = []
    minlist = []
    for dic in data:
        if int(dic['contract_amount']) == maxValue:
            max_min_list.append(dic)
        if int(dic['contract_amount']) == minValue:
            max_min_list.append(dic)
    return max_min_list
    print(max_min_list)
    return max_min_list

# print(max_min_list())
from collections import Counter
# [3] OO 구별 거래량 수 계산해서 출력
def totaltradingvolume():
    newList = []
    location = []
    var = []
    for dic in data:
        newList.append(dic['location'])
    for i in newList:
        location.append(i.split(" "))
    for j in location:
        var.append(j[1])
    print(var)
    collec = Counter(var)
    print(collec)
print(totaltradingvolume())







# [4] 단지명 별로 거래량 계산해서 거래량이 많은 단지명 TOP10 출력
def top_ten_transaction():
    transaction = []  # 출력할 거래량 순위 목록
    complex_name = []  # 단지명 리스트
    for row in data:  # 단지명 목록에 없으면 추가하고 거래량 +1
        if row['name'] not in complex_name:
            complex_name.append(row['name'])
            transaction.append(1)
        else:
            transaction[complex_name.index(row['name'])] += 1
    tuples = list(zip(complex_name, transaction))  # 단지명, 거래량 합치기
    result = []
    for tup in tuples:
        result.append({'complex_name': tup[0], 'transaction': tup[1]})
    result = sorted(result, key=lambda x: x['transaction'], reverse=True)
    return result[:10]


# [5] 년 월 별 거래량과 전월대비 증감 계산, 첫 월과 끝 월은 거래량만
def compare_transaction():
    # {년월, 거래량}
    dates = []
    transaction = []
    rate = [0]  # 인덱스) 0과 1, 1과 2 ... n-1과 n, 0은 맨 처음 연월은 증감 계산이 안 되므로
    for row in data:
        if row['year_month'] not in dates:  # 처음 보는 연월이면 목록에 추가하고 거래량 +1, 인덱스로 논리적 같은 값을 구분
            dates.append(row['year_month'])
            transaction.append(1)
        else:
            transaction[dates.index(row['year_month'])] += 1
    print(transaction)

    # 증감율 계산하기
    old_num = 0
    new_num = 0
    for num in transaction:
        if not old_num:  # 처음 값은 old_num에 한번만 저장되고 넘어가도록
            old_num = num
            continue
        else:
            new_num = num
        rate.append(round((new_num/old_num)*100-100, 2))
        # 새 값을 이전 값으로 넘기고 새 값은 0으로 -> 다음 루프에서 새 값이 채워지고 반복된다
        old_num = new_num
        new_num = 0
    rate = rate[:-1]  # 마지막 값은 올바른 값이 아니므로 빼기 (8월 도중 값이므로)
    rate.append(0)  # 마지막 값 대신 0 대입
    zipped = list(zip(dates, transaction, rate))
    result = []
    for z in zipped:
        result.append({"year_month": z[0], "amount": z[1], "rate": z[2]})
    return result


# [6] 가장 거래가 많은 요일 계산 및 출력
def weekday_most_transactions():
    locale.setlocale(locale.LC_ALL, "ko_KR.UTF-8")
    year_month = []
    day = []
    # [일 월 화 수 목 금 토]
    weekday_transactions = [0, 0, 0, 0, 0, 0, 0]
    for row in data:
        year_month.append(row['year_month'])
        day.append(row['day'])
    row_data = zip(year_month, day)
    for row in row_data:  # 연월일을 합쳐 요일을 구하고 각 요일 카운트 배열 (인덱스로 구분) 칸에 더하기
        weekday = datetime.datetime.strptime("".join([row[0], row[1]]), '%Y%m%d').strftime('%w')
        weekday_transactions[int(weekday)] += 1
    max_num = max(weekday_transactions)  # 최대 거래량
    day_name = ["일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일"]
    # 최고 거래량, 거래량 인덱스에 맞는 요일 이름 딕셔너리로 반환
    return {'max_num': max_num, 'name': day_name[weekday_transactions.index(max_num)]}
