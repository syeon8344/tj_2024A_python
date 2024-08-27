# day10 > 3_할리스커피매장.py
# [1] 모듈 가져오기
from bs4 import BeautifulSoup
from urllib import request, parse
import pandas as pd
print(pd.__version__)

# [2] 페이지 순회하며 정보 추출
def hollys_store(result):
    for page in range(1, 51):  # 1 ~ 50까지 반복
        # 할리스 커피 매장 정보 URL
        url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}"
        response = request.urlopen(url)
        soup = BeautifulSoup(response, "html.parser")
        # print(soup.prettify())
        t_body = soup.select_one("tbody")
        # print(t_body)
        for row in t_body.select('tr'):
            # print(row)
            if len(row) <= 3:
                break
            tds = row.select("td")
            store_location = tds[0].string  # 매장위치
            # print(store_location)
            store_name = tds[1].string  # 매장명
            # print(store_name)
            store_address = tds[3].string  # 매장주소
            # print(store_address)
            store_contact = tds[5].string  # 매장연락처
            # print(store_contact)
            store = [store_location, store_name, store_address, store_contact]
            result.append(store)  # 리스트 안에 리스트 요소 추가, 2차원 리스트 [[], [], [], []]
    return


# [1] 메인 함수
def main():
    result = []  # 할리스 매장정보 리스트 여러 개 저장하는 리스트
    print("Hollys store crawling >>>>>>>>>>>>>>>>>")
    hollys_store(result)
    print(result)
    # python List 객체를 DataFrame 객체로 변환
    hollys_table = pd.DataFrame(result, columns=("store", "location", "address", "contact"))
    # DataFrame 객체를 csv 파일로 생성
    hollys_table.to_csv("hollys_csv.csv", encoding='cp949', mode='w', index=True)
    del result[:]


if __name__ == "__main__":
    main()
