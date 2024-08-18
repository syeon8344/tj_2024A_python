import random


def case_based_on_remainder(number):
    remainder = number % 15
    # 50 > 20, 42 > 12
    if remainder == 0:
        return 15
    elif remainder == 1:
        return 16
    elif remainder == 2:
        return 17
    elif remainder == 3:
        return 18
    elif remainder == 4:
        return 19
    elif remainder == 5:
        return 20
    elif remainder == 6:
        return 6
    elif remainder == 7:
        return 7
    elif remainder == 8:
        return 8
    elif remainder == 9:
        return 9
    elif remainder == 10:
        return 10
    elif remainder == 11:
        return 11
    elif remainder == 12:
        return 12
    elif remainder == 13:
        return 13
    elif remainder == 14:
        return 14
    else:
        return "Unexpected case"


# 예제 사용
number = 37
result = case_based_on_remainder(number)
print(f"The case for {number} is: {result}")

# 사이즈 목록
sizes = ['S', 'M', 'L', 'XL', 'XXL']

# 데이터 삽입
for i in range(21, 51):  # prodcode와 prodcatecode는 1부터 50까지
    prodcatecode = case_based_on_remainder(i)
    numList = []
    for j in range(1, 11):
        prodcode = i

        while True:
            randNum = random.randint(1, 20)
            if randNum not in numList:
                colorcode = randNum  # colorcode는 1부터 20까지 랜덤
                numList.append(randNum)
                break

        prodsize = f"'{sizes[(j - 1) % len(sizes)]}'"  # 사이즈는 'S', 'M', 'L', 'XL', 'XXL'을 반복
        print(
            f'insert into productdetail (prodcode, prodcatecode, colorcode, prodsize) values ({prodcode}, {prodcatecode}, {colorcode}, {prodsize});')

from datetime import datetime, timedelta


def generate_random_date(start_date, end_date):
    # 시작과 종료 날짜를 datetime 객체로 변환
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    # 두 날짜 사이의 일수 차이를 계산
    delta_days = (end - start).days

    # 랜덤한 일수 계산
    random_days = random.randint(0, delta_days)

    # 랜덤 날짜 생성
    random_date = start + timedelta(days=random_days)

    # YYYY-MM-DD 형식으로 반환
    return random_date.strftime('%Y-%m-%d')


# 예제 사용
start_date = '2021-01-01'
end_date = '2024-08-18'

for i in range(1, 256):
    memcode = random.randint(1, 50)
    orddate = generate_random_date(start_date, end_date)
    print(f'insert into orders (memcode, orddate) values ({memcode}, \'{orddate}\');')

print()
print()

for i in range(1, 201):
    ordcode = random.randint(1, 255)
    proddetailcode = random.randint(156, 456)
    ordamount = random.randint(1, 10)
    ordstate = random.randint(1, 5)
    coupcode = random.randint(1, 5)
    ordprice = 1000 + 1000 * random.randint(1, 99)
    print(f'insert into orderdetail (ordcode, proddetailcode, ordamount, ordstate, coupcode, ordprice) values ({ordcode}, {proddetailcode}, {ordamount}, {ordstate}, {coupcode}, {ordprice});')

for i in range(1,15):
    print(f'    sum(case when ordstate = 5 and orddate = curdate() - interval {i} day then ordamount else 0 end) "{i}일 전",')


num1 = 6
for i in range(1,14):
    print(f'daysMap.put("{i}일 전", rs.getInt({num1}));')
    num1+=1
