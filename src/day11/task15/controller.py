# day11 > task15 > controller.py
# [1] 플라스크 객체 가져오기
from app import app

# [2] 서비스 모듈 가져오기
import service


# [4] app.run() 코드위에 HTTP 매핑 주소 정의, methods=["GET"]은 GET일시 생략가능
@app.route("/qooqoo")
def qooqoo_store_info():
    # 1. 크롤링된 CSV 파일이 없거나 최신화하려면
    result = []
    service.qooqoo_info(result)
    service.list_to_csv(result, '전국쿠우쿠우매장', ["번호", "매장명", "연락처", "주소", "영업시간"])

    # 2. CSV에 저장된 JSON 가져오기
    result = service.load_csv_to_json('전국쿠우쿠우매장')

    # 3. 서비스에서 받은 데이터로 HTTP 응답하기
    return result
