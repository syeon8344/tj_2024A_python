# day08 > task10 > region.py
# Region 객체변수 : 동이름,인구수(총합계),인구수(남),인구수(여),세대수,데이터기준일자
class Region:

    def __init__(self, name, total, man, woman, house):
        self.name = name
        self.total = total
        self.man = man
        self.woman = woman
        self.house = house
        self.man_percent = round(((int(self.man) / (int(self.total))) * 100), 2)
        self.woman_percent = round(((int(self.woman) / (int(self.total))) * 100), 2)
