# day08 > task11 > app.py
"""
    삼성전자주가.csv 파일의 정보를 테이블 형식으로 localhost:8080/index3.html에 출력
        1. csv 파일을 읽어 행마다 딕셔너리로
        2. Flask를 이용해 해당 정보를 HTTP 매핑
        3. Spring 서버에서 AJAX로 Flask 서버에서부터 데이터 받기
"""
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/samsungcsv", methods=["GET"])
def index():
    csv_data = []
    f = open("삼성전자주가.csv", 'r')
    f.readline()  # 제목 줄 읽고 버리기
    while True:
        # 각 문장 끝의 \n을 없애고 큰따옴표를 없앤 후 쉼표 단위로 자르기 (또는 eval() 사용해서 큰따옴표 삭제 가능)
        # 천단위 쉼표 표시하기 : format(정수형 데이터, ',')
        data = f.readline().strip().replace("\"", "").split(',')
        if data == [""]:  # 공백이면 = 데이터 끝, 종료
            break
        dic = {"date": data[0], "ending": int(data[1]), "delta": int(data[2]), "rate": float(data[3]),
               "current": int(data[4]), "highest": int(data[5]), "lowest": int(data[6]), "trans_amount": int(data[7]),
               "trans_money": int(data[8]), "comp_value": int(data[9]), "total_stock": int(data[10])}
        csv_data.append(dic)
    f.close()
    return csv_data


if __name__ == "__main__":
    app.run()
