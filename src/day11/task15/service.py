# day11 > task15 > service.py
# http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship
"""
    1. BeautifulSoup 이용한 쿠우쿠우 전국 매장 정보 크롤링
    2. 전국 쿠우쿠우 매장 정보(번호, 매장명, 연락처, 주소, 영업시간)
    3. pandas 이용해서 CSV 파일로 변환
    4. 3의 CSV 파일을 다시 읽어서 반환해주는 HTTP 매핑을 정의
        URL: ...:5000/qooqoo  # GET
        3번에서 생성된 CSV 파일을 DataFrame으로 읽고 DataFrame을 JSON 형식으로 반환
"""
# [3] 모듈 가져오기
from bs4 import BeautifulSoup
from urllib import request
import pandas as pd
import json

# [1] URL 판단
'''
    http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page=
    매개변수: page=1 ~ page=6
'''

# [2] 가져올 정보의 HTML 마크업 확인
'''
    1. 정보가 있는 위치: <tbody>
    2. <tr> 한개에 매장 정보 하나, 모바일 페이지용 <tr>도 존재 (홀수 - PC <tr>, 짝수 - 모바일 <tr>)
    3. <td> 하나의 매장의 각 속성: 1. 번호 2. 매장명 3. 연락처 4. 주소 5. 영업시간
        <td><div><a>[1]매장명
        <td><a>연락처, 주소, 영업시간
'''


# [4] 쿠우쿠우 매장 정보: 지정 URL을 호출해서 응답 받기
def qooqoo_info(result):
    for page in range(1, 7):
        url = f"http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page={page}"
        response = request.urlopen(url)
        if response.getcode() == 200:
            print("통신 성공.")
            # [5] 통신 응답 결과를 읽어와 크롤링 파싱
            soup = BeautifulSoup(response.read(), "html.parser")
            # print(soup)
            # [6] 분석한 HTML 식별자들을 파싱, find/findAll/select/select_one
            tbody = soup.find("tbody")  # 테이블 파싱
            rows = tbody.select("tr")  # 테이블(전체매장)의 각 행(매장) 파싱
            # print(rows)
            for row in rows:  # 행(매장)마다 열(매장정보) 파싱
                # print(row)
                cols = row.select('td')
                # 모바일 제외 (len(cols): PC버전은 6, 모바일은 1)
                if len(cols) == 1:
                    continue
                # 각 정보들 파싱, 양 끝 공백 제거
                번호 = int(cols[0].string.strip())
                매장명 = cols[1].select('a')[1].string.strip().replace("\"", "")  # 2번째 열의 div 안의 a태그 두개 존재, 그 중 두번째의 문자열 값
                연락처 = cols[2].select_one('a').string.strip().replace(" ", "")
                주소 = cols[3].select_one('a').string.strip().replace("\"", "")  # .replace -> 큰따옴표 제거
                영업시간 = cols[4].select_one('a').string.strip().replace("\"", "")
                # 리스트에 담아 DataFrame을 생성할 2차원 리스트 구성하기
                매장 = [번호, 매장명, 연락처, 주소, 영업시간]
                # print(매장)
                result.append(매장) # 리스트에 파싱한 (페이지별) 리스트를 담기 -> 2차원 리스트
        else:
            print("통신 실패.")
    # [7] 리스트 반환
    return result


# [8] 2차원 리스트를 CSV 변환하는 함수
def list_to_csv(data_list, file_name, col_names):
    try:
        # pandas 모듈 호출
        # DataFrame 객체 생성, 매개변수: 데이터, 열 이름 목록
        df = pd.DataFrame(data_list, columns=col_names)
        # DataFrame 객체를 CSV로 변환 및 파일 생성
        df.to_csv(f"{file_name}.csv", encoding="utf-8", mode='w')
        return True
    except Exception as e:
        print(e)
        return False


# [9] CSV 파일을 JSON타입으로 가져오기, 매개변수: 파일명
def load_csv_to_json(file_name):
    # 1. CSV 파일 읽기: 파일명, 파일 인코딩, 사용 엔진, 인덱스로 사용할 열 인덱스
    df = pd.read_csv(f"{file_name}.csv", encoding="utf-8", engine="python", index_col=0)
    # print(df)

    # 2. DF 객체를 JSON으로 변환: orient=JSON 키 값 방향, 'records': 키:값 목록이 한 줄에 하나씩, force_ascii=데이터의 문자를 ASCII문자로만 한정 및 치환할지 여부
    # 변환된 json은 파이썬 타입이 아닌 문자열
    json_result = df.to_json(orient="records", force_ascii=False)  # <class 'str'>

    # 3. JSON 형식의 파이썬 타입으로 변환 (dict, list, ...) json_loads() <-> json.dumps()
    # PY :  json.loads( ) JSON형식 --> PY형식 변환 함수  , json.dumps( ) PY형식 ---> JSON형식(문자열타입) 변환 함수
    # JS : JSON.parse( ) JSON형식 --> JS형식 변환 함수  , JSON.stringify( ) JS형식 ---> JSON형식(문자열타입) 변환 함수
    result_json = json.loads(json_result)  # <class 'list'>
    # print(type(result_json))
    return result_json


# 서비스 확인하기
if __name__ == "__main__":
    result = []
    qooqoo_info(result)
    # print(result)
    list_to_csv(result, '전국쿠우쿠우매장', ["번호", "매장명", "연락처", "주소", "영업시간"])
    result2 = load_csv_to_json("전국쿠우쿠우매장")
    print(result2)
