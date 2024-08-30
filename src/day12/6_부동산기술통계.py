# day12 > 6_부동산기술통계.py
# 부동산 실거래가: https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=
"""
    [1] 인천광역시 부평구 전월세 1년치 csv 수집
    [2] CSV 파일을 pandas DataFrame으로 변경
    [3] 데이터 모델링, 기술통계
    기술통계 탐색 결과를 Spring index6.html 아래쪽 테이블로 출력 (HTTP매핑 임의 정의)
    [4] 데이터 모델링(그룹화): 전월세 기준
    전월세 기준 그룹해서 전용면적의 기술통계를 위쪽 테이블에 출력
    [5] 추가
        1. 부평구의 동 명을 중복없이 출력하시오.
        2. 가장 거래수가 많은 단지명 을 1~5 등까지 출력하시오.
"""
from flask import Flask
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)


# [1] 인천광역시 부평구 전월세 1년치 csv 수집
"csv/아파트(전월세)_실거래가_20240829161812.csv"

# [2] CSV 파일을 pandas DataFrame으로 변경
# header: 헤더 행을 지정 + 리스트로 다중 헤더 표현 + 헤더 지정된 행 윗부분은 패스 vs
# skiprows: n개의 행 패스(패스 안된 바로 다음 행이 헤더) + 리스트로 헤더 안쪽의 스킵할 행 지정 가능 (리스트 전에 행이 있으면 헤더)
year = 2022
df_list = []
while True:
    try:
        df_temp = pd.read_csv(f"csv/아파트(전월세)_실거래가_{year}.csv", skiprows=15, encoding="cp949")
        df_list.append(df_temp)
        year += 1
    except Exception as e:
        print(e)
        break

df = pd.concat(df_list)
print(df.shape)
# print(df)
# df.to_csv("csv/2022-2024_아파트_실거래가.csv", index=False)

# [3] 데이터 모델링, 기술통계
# 기술통계 탐색 결과를 Spring index6.html 아래쪽 테이블로 출력 (HTTP매핑 임의 정의)
# print("전용면적(㎡)")
# print(round(df.describe(), 3).to_json(force_ascii=False))
# print(df['전용면적(㎡)'].describe())
# print(sorted(df['전용면적(㎡)'].unique(), reverse=True))


@app.route("/housing")
def df_housing():
    # .to_json(orient="values"): 값만 배열로
    data = round(df.describe(), 3).to_json(force_ascii=False)
    return json.loads(data)


# [4] 데이터 모델링(그룹화): 전월세 기준
# 전월세 기준 그룹해서 전용면적의 기술통계를 위쪽 테이블에 출력
# .to_json() -> 모든 값을 따옴표로, .to_dict() -> str들만 따옴표로
# json.loads(df.to_json())이면 인덱스와 키 값들이 문자열인 딕셔너리
@app.route("/area")
def area():
    data = round(df.groupby('전월세구분')['전용면적(㎡)'].describe(), 3).to_json(force_ascii=False)
    return json.loads(data)


# [5] 추가: 1. 부평구의 동 이름을 중복 없이 출력
@app.route("/uniquenames")
def unique_names():
    return df['시군구'].unique().tolist()


# 2. 가장 거래수가 많은 단지명 을 1~5 등까지 출력하시오.
# df.value_counts(): 특정 열의 레코드(행) 수
# df.head(): 위에서 5개 추출
@app.route("/toptrades")
def top_trades():
    data = df['단지명'].value_counts().head().to_json(orient="split", force_ascii=False)
    return json.loads(data)


if __name__ == "__main__":
    app.run(debug=True)

