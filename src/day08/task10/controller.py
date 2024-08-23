# day08 > task10 > controller.py
from app import app  # Flask 객체
from service import person_data  # service에서 함수 불러오기


@app.route('/', methods=['GET'])
def index():
    data = person_data()  # 서비스에서 함수 처리후 받는 결과
    # 파이썬 객체로는 JSON 전송 불가
    # 파이썬 객체를 딕셔너리로 변경, # 객체명.__dict__
    # new_data = []
    # for obj in data:
    #     new_data.append(obj.__dict__)
    # return new_data
    return list(map(lambda obj: obj.__dict__, person_data()))
