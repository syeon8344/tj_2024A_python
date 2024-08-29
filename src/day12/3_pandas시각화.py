# day12 > 3_pandas시각화.py
# p.124 연습문제
import pandas as pd
import matplotlib.pyplot as plt

# Q7
index = [2015, 2016, 2017, 2018, 2019, 2020]
data = [[500, 450, 520, 610], [690, 700, 820, 900], [1100, 1030, 1200, 1380], [1500, 1650, 1700, 1850],
        [1990, 2020, 2300, 2420], [1020, 1600, 2200, 2550]]
columns = ['1분기', '2분기', '3분기', '4분기']

df = pd.DataFrame(data, index=index, columns=columns)  # index를 인덱스로, colums를 세로열 레이블 이름으로, data는 요소 리스트 하나당 한줄씩
# print(df)
df.to_csv("csv/Q07.csv", encoding='utf-8', mode='w')

# # Q8
for line in data:
    plt.plot(['first', 'second', 'third', 'fourth'], line)
    # x축: ['first', 'second', 'third', 'fourth'], y축: line: data 안의 리스트들
plt.legend(index)
plt.title('2015~2020 Quarterly sales')
plt.ylabel('sales')
plt.xlabel('Quarters')
plt.show()  # 그래프 표시

