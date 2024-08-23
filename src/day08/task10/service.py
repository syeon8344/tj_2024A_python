# day08 > task10 > service.py
from region import Region


def person_data():
    print("--start--")
    regions = []
    f = open("인천광역시_부평구_인구현황.csv", 'r')
    f.readline()  # 제목 줄은 버리기
    while True:
        line = f.readline().strip()
        if not line or not line.split(",")[0]:
            break
        r = Region(line.split(",")[0], line.split(",")[1], line.split(",")[2], line.split(",")[3], line.split(",")[4])
        regions.append(r)
    return regions
