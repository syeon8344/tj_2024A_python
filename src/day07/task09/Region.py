# day07 > task09 > Region.py
# Region 객체변수 : 동이름,인구수(총합계),인구수(남),인구수(여),세대수,데이터기준일자
class Region:

    def __init__(self, name, total, man, woman, house):
        self.name = name
        self.total = total
        self.man = man
        self.woman = woman
        self.house = house

    def man_percent(self):
        return (int(self.man) / (int(self.man) + int(self.woman)))*100

    def woman_percent(self):
        return (int(self.woman) / (int(self.man) + int(self.woman)))*100
