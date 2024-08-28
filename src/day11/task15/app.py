# day11 > task15 > app.py
# 플라스크: 파이썬 사용한 경량 웹 프레임워크
# [1] 플라스크 모듈 가져오기
from flask import Flask
from flask_cors import CORS

# [2] 플라스크 객체 생성
app = Flask(__name__)
CORS(app)

# [4] controller 모듈 가져오기
from controller import *



# [3] 플라스크 웹 실행
if __name__ == "__main__":
    # host='0.0.0.0' 설정: ip 127.0.0.1:5000, localhost:5000, 192.168.30.nnn:5000 다 사용가능
    app.run(host='0.0.0.0', debug=True)
    # 서버 재시작시 프로세스 실행 중지하고 실행하기
