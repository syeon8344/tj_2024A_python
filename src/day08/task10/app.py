# day08 > task10 > app.py
from flask import Flask  # 1) Flask 모듈 가져오기
app = Flask(__name__)  # 2) Flask 객체 생성
from flask_cors import CORS  # 3) CORS 모듈 가져오기
CORS(app)  # 4) 모든 HTTP 경로에 CORS 허용

# 5) HTTP 매핑, controller 호출
from controller import *


# 6) Flask 실행
if __name__ == "__main__":
    app.run(debug=True)