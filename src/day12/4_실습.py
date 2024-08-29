# day12 > 4_실습.py
# 실습 1: 삼성전자 최근 주가 1
# http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd
# 정보데이터시스템
# 1. DataFrame 객체를 콘솔에 출력 (CSV -> 데이터프레임)
# 2. 삼성전자의 최근 1년 시세 중 일자별 종가를 막대차트로 표현하시오 (일자: X축, 종가: Y축)

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

try:
    df = pd.read_csv("csv/삼성전자_20240829.csv", encoding='utf-8', engine="python")
except Exception as e:  # 인코딩 오류시 cp-949 인코딩 사용
    print(e)
    df = pd.read_csv("csv/삼성전자_20240829.csv", encoding='cp-949', engine="python")

print(df)
df_data = df.to_dict(orient="records")  # 행마다 열 이름을 키로 해서 딕셔너리 변환
print(df_data)
x = []
y = []
for row in df_data:
    x.append(datetime.strptime(row['일자'], "%Y/%m/%d").date())
    y.append(row['종가'])
plt.title('Samsung')
plt.xlabel('date')
plt.ylabel('price')
plt.plot(x, y)
plt.xlim(x[-1], x[1])  # 날짜 순서를 반대로 (최신 먼저 -> 이전 날짜 먼저) 또는 .reverse()
print(x)
print(y)

plt.show()
