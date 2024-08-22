# day07 > task09 > Main.py
"""
    csv 파일 다루기
    파일 : 인천광역시_부평구_인구현황.csv
    [조건1] 부평구의 동 마다 Region 객체를 생성해서 리스트에 담기
    [조건2] Region 객체 변수 5개
    [조건3] 모든 객체를 리스트에 담고 모든 객체의 정보를 f포매팅해서 콘솔에 출력
    [조건4] 출력시 동마다 남녀비율 계산해서 출력
    출력예시:
    부평1동,35141,16835,18306,16861,2024-02-14, 남자%, 여자%
"""
from Region import Region

if __name__ == "__main__":
    print("--start--")
    regions = []
    f = open("인천광역시_부평구_인구현황.csv", 'r')
    column_name = f.readline()
    while True:
        line = f.readline().strip()
        if not line:
            break
        r = Region(line.split(",")[0], line.split(",")[1], line.split(",")[2], line.split(",")[3], line.split(",")[4])
        regions.append(r)
    print(f"| {"동 이름"} | {"총 인구"} | {"남성 인구"} | {"여성 인구"} | {"세대수"} | {"남성 비율"} | {"여성 비율"} |")
    for region in regions:
        print(f"  {region.name:<4}{region.total:>9}{region.man:>10}{region.woman:>10}{region.house:>9}{region.man_percent():>9.2f}%{region.woman_percent():>9.2f}%")
