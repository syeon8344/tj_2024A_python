# day12 > 6_부동산기술통계.py
# 부동산 실거래가: https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=
"""
    [1] 인천광역시 부평구 전월세 1년치 csv 수집
    [2] CSV 파일을 pandas DataFrame으로 변경
    [3] 데이터 모델링, 기술통계
    기술통계 탐색 결과를 Spring index6.html 아래쪽 테이블로 출력 (HTTP매핑 임의 정의)
    [4] 데이터 모델링(그룹화): 전월세 기준
    전월세 기준 그룹해서 전용면적의 기술통계를 위쪽 테이블에 출력
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
df = pd.read_csv("csv/아파트(전월세)_실거래가_20240829161812.csv", encoding="utf-8", engine="python", header=14, index_col=0)
print(df)

# [3] 데이터 모델링, 기술통계
# 기술통계 탐색 결과를 Spring index6.html 아래쪽 테이블로 출력 (HTTP매핑 임의 정의)
print("전용면적(㎡)")
print(round(df.describe(), 3).to_json(force_ascii=False))
print(df['전용면적(㎡)'].describe())
print(sorted(df['전용면적(㎡)'].unique(), reverse=True))


@app.route("/housing")
def df_housing():
    data = round(df.describe(), 3).to_dict(orient="records")
    return json.dumps(data, ensure_ascii=False)
# [4] 데이터 모델링(그룹화): 전월세 기준
# 전월세 기준 그룹해서 전용면적의 기술통계를 위쪽 테이블에 출력


str = "NO	시군구	번지	본번	부번	단지명	전월세구분	전용면적(㎡)	계약년월	계약일	보증금(만원)	월세금(만원)	층	건축년도	도로명	계약기간	계약구분	갱신요구권 사용	종전계약 보증금(만원)	종전계약 월세(만원)	주택유형"
strlist = str.split()
print(strlist)
for item in strlist:
    print(f"<th>{item}</th>")


if __name__ == "__main__":
    app.run(debug=True)


