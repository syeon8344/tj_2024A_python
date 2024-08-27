# day10 > 5_쿠우쿠우매장.py
# http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship
"""
    1. BeautifulSoup 이용한 쿠우쿠우 전국 매장 정보 크롤링
    2. 전국 쿠우쿠우 매장 정보(번호, 매장명, 연락처, 주소, 영업시간)
    3. pandas 이용해서 CSV 파일로 변환
    4. 3의 CSV 파일을 다시 읽어서 반환해주는 HTTP 매핑을 정의
        URL: ...:5000/qooqoo  # GET
        3번에서 생성된 CSV 파일을 DataFrame으로 읽고 DataFrame을 JSON 형식으로 반환
"""
from flask import Flask
from flask_cors import CORS
import pandas as pd
from bs4 import BeautifulSoup
from urllib import request

app = Flask("__name__")
CORS(app)


def main():
    # 각 열 리스트
    names = []
    contacts = []
    addresses = []
    hours = []
    page = 1  # 페이지 변수
    while True:  # 내용이 없을 때까지 페이지를 넘기면서 데이터 추출
        # 페이지마다 tbody 추출 및 유효성검사
        url = f"http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page={page}"
        response = request.urlopen(url)
        soup = BeautifulSoup(response, "html.parser")
        trs = soup.select("tbody > tr")
        if len(trs) == 1:  # 정보 없는 trs의 len == 1 <td class="text-center" colspan="7">게시물이 없습니다.</td>
            break
        page += 1
        # 데이터 추출
        name_divs = soup.select("tbody > tr > td > div")  # 지점명이 포함된 div
        tdas = soup.select("tbody > tr > td > a")  # 나머지 정보가 포함된 td 안의 a태그들
        for name in name_divs:  # 지점명
            names.append(name.select("a")[1].string.strip())
        count = 0
        for tda in tdas:  # tda: 연락처,주소,운영시간,연락처,주소,운영시간, ...
            data = tda.text  # 각 <a> 태그 안의 문자열
            if count % 3 == 0:
                contacts.append(data)
            elif count % 3 == 1:
                addresses.append(data)
            elif count % 3 == 2:
                hours.append(data)
            count += 1

    data_dict = {'name': names, 'contact': contacts, 'address': addresses, 'operation_hour': hours}
    df = pd.DataFrame(data_dict)

    df.to_csv("qooqoo.csv", encoding='utf-8')


# GET HTTP mapping
@app.route("/qooqoo")
def index():
    # pandas로 csv 파일 읽어오기
    csv_df = pd.read_csv("qooqoo.csv", encoding='utf-8', index_col=0)
    # 반환: dataframe을 딕셔너리로, 딕셔너리 기준: 레코드 (orient="records")
    return pd.DataFrame.to_dict(csv_df, orient="records")

# 이 파일을 직접 실행했을 때만 실행되는 main함수
if __name__ == "__main__":
    main()  # 먼저 CSV 파일에 크롤링 데이터를 작성한 후 플라스크 실행
    app.run(debug=True)


