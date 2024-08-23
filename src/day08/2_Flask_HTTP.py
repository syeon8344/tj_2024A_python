# day08 > 2_Flask_HTTP.py
# 1) import Flask
from flask import Flask
# 2) app = Flask(__name__)
app = Flask(__name__)


class Test:
    pass


# ==================== HTTP 매핑 ==================== #
# 논리타입, 정수타입, 객체타입은 전송 불가, 리스트와 딕셔너리 및 문자열 사용해서 통신
# @app.route("HTTP 경로 정의", methods = ['HTTP 메서드']
@app.route("/", methods=['GET'])  # @GetMapping()
def index1():
    return "Hello HTTP GET"


@app.route("/", methods=['POST'])  # @PostMapping()
def index2():
    # return True: 500 internal error, 타입 오류
    # return 3 : 500 internal eror: 오류
    return [3, 3]  # Content-Type:	application/json


@app.route("/", methods=['PUT'])  # @PutMapping()
def index3():
    return {"result": True}


@app.route("/", methods=['DELETE'])  # @DeleteMapping()
def index4():
    # return Test()
    return "true"
# =================================================== #


# 3) app.run()
if __name__ == "__main__":
    app.run(debug=True)  # debug = True: 디버그(정보 또는 오큐를 콘솔에 출력) 모드
