# day08 > 3_FlaskCors.py
"""
    CORS: Cross Origin Resource Sharing, 교차 출처 자원 공유
        - 규정상 서로 다른 주소들 간의 통신은 불가
        - 현재 주소에서 다른 주소로 통신 요청하고 현재 주소로 응답받기

    HTTP
        (유재석) 안녕 -- 요청 -->  (유재석)
                    <-- 응답 --
        8080 <-----------------> 8080

    CORS 통신
        (유재석) 안녕 -- 요청 --> (강호동)
                    <-- 응답 --
        8080 <------------------> 5000

    CORS 허용
        1) Flask-Cors 모듈 설치
            메뉴 > 파일 > 설정 > 사이드바: 프로젝트 > 인터프리터 > [+] 또는 alt+insert
        2) 모듈 가져오기
            from flask import Flask
        3) CORS 허용
            CORS(app)
"""
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 모든 경로에 대해 CORS 허용


@app.route("/")
def index():
    return "Hello Python Flask-Cors"


if __name__ == "__main__":
    app.run()
