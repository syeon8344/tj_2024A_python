# day18 > 3_지리정보.py
# 주제: 커피매장의 주소를 이용해서 지도에 마커 표시하기
# 실습 파일: CoffeeBean.csv
import pandas as pd
import json

# [1] 데이터 준비
df = pd.read_csv("CoffeeBean.csv", encoding='cp949', index_col=0)
print(df)

# [2] 데이터 가공: 주소 데이터를 행정구역 주소 체계에 갖도록 정리
# 포리움 대신 카카오 지도로 실습

# 플라스크
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    # df 객체 -> JSON
    json_data = df.to_json(orient='records', force_ascii=False)

    result = json.loads(json_data)
    return result


if __name__ == "__main__":
    app.run()